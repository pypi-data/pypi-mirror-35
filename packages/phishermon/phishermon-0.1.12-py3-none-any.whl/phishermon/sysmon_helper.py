import argparse
import os
import json
import time
import platform
from datetime import datetime, timedelta
from queue import Queue, Empty
from threading import Thread

import Evtx.Evtx as evtx
import sys
import xmltodict
from collections import OrderedDict

from .utils import flatten_dict, timestamp_to_epoch, format_compact, format_pretty, flatten_xml_event, convert_ad_timestamp
from . import constants

if platform.system() == 'Windows':
    import etw

class ProcessNode(object):
    def __init__(self, guid, events):
        self.events = events
        self.children = {}
        self.name = ''
        self.timestamp = 0

        for event in self.events:
            if not self.name and constants.KEY_IMAGE in event:
                self.name = event[constants.KEY_IMAGE]
            if constants.KEY_TIMESTAMP in event:
                self.timestamp = min(timestamp_to_epoch(event[constants.KEY_TIMESTAMP]), self.timestamp)

        if not self.name:
            self.name = guid


class ProcessTree(object):
    def __init__(self):
        self.process_events = {}
        self.parents = {}
        self.process_chains = []
        self.tree = None

    def add_event(self, event):
        """Adds an event to the tree."""
        guid = event[constants.KEY_P_GUID] if constants.KEY_P_GUID in event else constants.GUID_ROOT
        if guid not in self.process_events:
            self.process_events[guid] = [event]
        else:
            self.process_events[guid].append(event)

        if guid and (guid not in self.parents or not self.parents[guid]):
            if constants.KEY_PP_GUID in event:
                self.parents[guid] = event[constants.KEY_PP_GUID]
            else:
                self.parents[guid] = ''

    def _build_chain(self, guid, chain):
        chain.insert(0, guid)
        if guid in self.parents:
            self._build_chain(self.parents[guid], chain)

    def _build_chains(self):
        chains = []
        for guid in self.process_events:
            chain = []
            try:
                self._build_chain(guid, chain)
            except RecursionError:
                pass
            top_chain = chain[0]
            if top_chain != '' and (top_chain not in self.process_events or not self.process_events[top_chain]):
                chain.insert(0, '')
            chains.append(chain)

        self.process_chains = sorted(chains, key=lambda x: x[0])

    def build_process_tree(self):
        """Builds an entire process tree."""
        self._build_chains()
        if constants.GUID_ROOT not in self.process_events:
            self.process_events[constants.GUID_ROOT] = []
        self.tree = ProcessNode(constants.GUID_ROOT, self.process_events[constants.GUID_ROOT])

        for chain in self.process_chains:
            node = self.tree
            for guid in chain:
                if guid not in node.children:
                    if guid in self.process_events:
                        events = self.process_events[guid]
                    else:
                        events = []
                    node.children[guid] = ProcessNode(guid, events)
                node = node.children[guid]

    @staticmethod
    def _abbreviate_event(event):
        abbreviated = OrderedDict()
        event_id = event[constants.KEY_EVENT_ID]
        event_description = constants.EVENT_KEYS[event_id][0]
        keys = constants.EVENT_KEYS_ALL + constants.EVENT_KEYS[event_id][1:]
        abbreviated['event'] = '%s (%s)' % (event_description, event_id)
        for key in keys:
            if key and key in event and event[key]:
                abbreviated[key] = event[key]

        return abbreviated

    def _abbreviate_process(self, process_node):
        abbreviated = OrderedDict()
        if process_node.events:
            events = [self._abbreviate_event(event) for event in process_node.events if event and event[constants.KEY_EVENT_ID] in constants.EVENT_KEYS]
            abbreviated_events = sorted(events, key=lambda e: timestamp_to_epoch(e[constants.KEY_TIMESTAMP]))
            if abbreviated_events:
                abbreviated['events'] = abbreviated_events

        if process_node.children:
            children_order = sorted([(child, node.timestamp) for child, node in process_node.children.items()],
                                    key=lambda c: c[1])
            abbreviated['children'] = OrderedDict()
            for child, _ in children_order:
                abbreviated['children'][process_node.children[child].name] = self._abbreviate_process(process_node.children[child])
        return abbreviated

    def abbreviate_tree(self):
        """Abbreviate the entire tree"""
        abbreviated = OrderedDict()
        if self.tree.events:
            events = [self._abbreviate_event(event) for event in self.tree.events if event]
            abbreviated['system_events'] = sorted(events, key=lambda e: timestamp_to_epoch(e[constants.KEY_TIMESTAMP]))
        abbreviated['processes'] = OrderedDict()
        for _, node in self.tree.children[''].children.items():
            abbreviated_node = self._abbreviate_process(node)
            if ('events' in abbreviated_node and abbreviated_node['events']) or \
                    ('children' in abbreviated_node and abbreviated_node['children']):
                abbreviated['processes'][node.name] = abbreviated_node
        return abbreviated


class SysmonHelper(object):

    def __init__(self, etw=False, evtx=True, evtx_file=None, continuous=False, 
                 silent=True, outfile=None, append_to_outfile=True, compact=False, 
                 very_compact=False, pretty_print=False, tree=False):

        self.evtx_queue = None
        self.etw_queue = None
        self.event_queue = None
        self.shutdown = False
        self.etw_parsers = []

        self.etw = etw
        self.evtx = evtx
        self.evtx_file = evtx_file
        self.continuous = continuous
        self.silent = silent
        self.outfile = outfile
        self.append_to_outfile = append_to_outfile
        self.compact = compact
        self.very_compact = very_compact
        self.pretty_print = pretty_print
        self.tree = tree

        if (self.compact or self.very_compact) and self.pretty_print:
            raise ValueError('Pretty_print cannot be used if compact or very_compact are set.')

        if self.very_compact and not self.compact:
            self.very_compact = True

        if self.outfile and os.path.exists(self.outfile) and not self.append_to_outfile:
            os.remove(self.outfile)

        if not self.etw and not self.evtx:
            raise ValueError("No data source specified. At least one of etw or evtx must be True.")

        if self.etw:
            # Start the ETW parser
            self.etw_queue = Queue()
            self.event_queue = self.etw_queue
            self.etw_parsers.append(self.start_etw_parser('Microsoft-Windows-Sysmon', '{5770385F-C22A-43E0-BF4C-06F5698FFBD9}'))
            self.etw_parsers.append(self.start_etw_parser('Microsoft-Windows-FileInfoMinifilter', '{A319D300-015C-48BE-ACDB-47746E154751}'))
            # etw_providers = {'Microsoft-Windows-Sysmon': '{5770385F-C22A-43E0-BF4C-06F5698FFBD9}', 
            #                 'Microsoft-Windows-FileInfoMinifilter': '{A319D300-015C-48BE-ACDB-47746E154751}'}
            # for name, guid in etw_providers.items():
            #     self.etw_parsers.append(self.start_etw_parser(name, guid))

        if self.evtx:
            # Start the EVXT parser
            self.evtx_queue = Queue()
            # Evtx should be parsed first if selected and then switch to ETW
            self.event_queue = self.evtx_queue
            self.evtx_parser = Thread(target=self.start_evtx_parser)
            self.evtx_parser.daemon = False
            self.evtx_parser.start()

    @property
    def etw(self):
        """Get sysmon events using Event Tracing for Windows (ETW)."""
        return self._etw

    @etw.setter
    def etw(self, e):
        if isinstance(e, bool):
            if e and platform.system() != 'Windows':
                raise NotImplementedError('Event Tracing for Windows (ETW) is only available on Windows platforms.')
            self._etw = e
        else:
            raise ValueError('ETW parameter must be True or False.')

    @property
    def evtx(self):
        """Get sysmon events from event log file."""
        return self._evtx

    @evtx.setter
    def evtx(self, e):
        if isinstance(e, bool):
            self._evtx = e
        else:
            raise ValueError('EVTX parameter must be True or False')

    @property
    def evtx_file(self):
        """Path to the SYSMON ".evtx" file. Default on Windows is C:\\Windows\\System32\\winevt\\Logs\\Microsoft-Windows-Sysmon%4Operational.evtx.
        On all other systems the default is None.
        """
        return self._evtx_file

    @evtx_file.setter
    def evtx_file(self, file_name):
        if file_name is not None:
            if os.path.exists(file_name):
                self._evtx_file = file_name
            else:
                raise ValueError('Cannot find evtx_file {}.'.format(file_name))
        elif file_name is None and platform.system() == 'Windows' and self.evtx:
            default = r"C:\Windows\System32\winevt\Logs\Microsoft-Windows-Sysmon%4Operational.evtx"
            if os.path.exists(default):
                self._evtx_file = default
            else:
                raise ValueError('Cannot find default evtx_file {}. Is sysmon installed and running?'.format(default))
        elif file_name is None and self.evtx:
            raise ValueError('Evtx flag was set but no evtx_file was given')
        else:
            self._evtx_file = None

    @property
    def continuous(self):
        """Keep reading the log when the end is reached."""
        return self._continuous
    
    @continuous.setter
    def continuous(self, c):
        if isinstance(c, bool):
            self._continuous = c
        else:
            raise ValueError("Continuous must be True or False.")
        
    @property
    def silent(self):
        """Supress printing to stdout."""
        return self._silent
    
    @silent.setter
    def silent(self, s):
        if isinstance(s, bool):
            self._silent = s
        else:
            raise ValueError('Silent must be True or False')

    @property
    def outfile(self):
        """Write output to this file."""
        return self._outfile

    @outfile.setter
    def outfile(self, o):
        self._outfile = o

    @property
    def append_to_outfile(self):
        """Append to output file instead of overwriting."""
        return self._append_to_outfile

    @append_to_outfile.setter
    def append_to_outfile(self, a):
        if isinstance(a, bool):
            self._append_to_outfile = a
        else:
            raise ValueError('Append_to_outfile must be True or False.')

    @property
    def compact(self):
        """Use one JSON record per line for all output."""
        return self._compact

    @compact.setter
    def compact(self, c):
        if isinstance(c, bool):
            self._compact = c
        else:
            raise ValueError('Compact must be True or False.')

    @property
    def very_compact(self):
        """Print the first 80 characters of each record."""
        return self._very_compact
    
    @very_compact.setter
    def very_compact(self, v):
        if isinstance(v, bool):
            self._very_compact = v
        else:
            raise ValueError('Very_compact must be True or False.')

    @property
    def tree(self):
        """Write a process tree to the output-file."""
        return self._tree
    
    @tree.setter
    def tree(self, t):
        if isinstance(t, bool):
            self._tree = t
        else:
            raise ValueError('Tree must be True or False.')

    @property
    def pretty_print(self):
        """Use indented JSON for all output."""
        return self._pretty_print
    
    @pretty_print.setter
    def pretty_print(self, p):
        if isinstance(p, bool):
            self._pretty_print = p
        else:
            raise ValueError('Pretty_print must be True or False')

    def start_etw_parser(self, name, guid):
        providers = [etw.ProviderInfo(name, etw.GUID(guid))]
        job = etw.ETW(session_name=name, event_callback=self.on_etw_event, providers=providers)
        job.start()
        
        return job

    def start_evtx_parser(self):
        for event in self.read_sysmon_log(self.evtx_file, continuous=self.continuous):
            if self.evtx_queue:
                self.evtx_queue.put((event,"evtx"))
            else:
                break

    def read_sysmon_log(self, sysmon_file, continuous=False):
        log = evtx.Evtx(sysmon_file)
        log = log.__enter__()

        # TODO: Add an argument so a specific record ID can be specified (for testing)
        # Finds the first record ID (required if the log has been cleared)
        counter = log.get_file_header().first_chunk().log_first_record_number()
        while not self.shutdown:
            event_record = log.get_record(counter)
            if event_record is None:
                if continuous:
                    time.sleep(0.2)
                    continue
                else:
                    break
            else:
                counter += 1
            event = flatten_xml_event(event_record.xml())
            if not event:
                continue
            yield event

    def read_event(self):
        changeover_event = {}
        while not self.shutdown:
            try:
                event, source = self.event_queue.get(block=True, timeout=3)
                if source is "evtx":
                    if changeover_event:
                        if event['EventData.Data.UtcTime'] == changeover_event['EventData.Data.UtcTime'] \
                                and event['EventData.Data.ProcessGuid'] == changeover_event['EventData.Data.ProcessGuid'] \
                                and event['System.Execution.ProcessID'] == changeover_event['System.Execution.ProcessID'] \
                                and event['System.Execution.ThreadID'] == changeover_event['System.Execution.ThreadID']:
                            self.event_queue = self.etw_queue
                            self.evtx_queue = None
                    else:
                        if self.etw and self.etw_queue.not_empty:
                            changeover_event = self.etw_queue.get(block=False)
                yield event
            except Empty:
                try:
                    if self.continuous:
                        sleep_len = 0.2
                        print('Sleeping for {} seconds'.format(sleep_len))
                        time.sleep(sleep_len)
                    else:
                        self.cleanup()
                        break
                except KeyboardInterrupt:
                    self.cleanup()
            except KeyboardInterrupt:
                self.cleanup()

    def cleanup(self):
        self.shutdown = True
        for parser in self.etw_parsers:
            parser.stop()

    def on_etw_event(self, event):
        formatted_event = {}
        for field in event[1]:
            if field is "EventHeader":
                # Manually rename event header fields as they don't match the EVTX field names
                formatted_event["System.Provider.Name"] = "Microsoft-Windows-Sysmon"
                formatted_event["System.Provider.Guid"] = event[1][field]['ProviderId']
                formatted_event["System.EventID.Qualifiers"] = "NA"
                formatted_event["System.EventID.text"] = str(event[1][field]['EventDescriptor']['Id'])
                formatted_event["System.Version"] = str(event[1][field]['EventDescriptor']['Version'])
                formatted_event["System.Level"] = str(event[1][field]['EventDescriptor']['Level'])
                formatted_event["System.Task"] = str(event[1][field]['EventDescriptor']['Task'])
                formatted_event["System.Opcode"] = str(event[1][field]['EventDescriptor']['Opcode'])
                formatted_event["System.Keywords"] = str(hex(event[1][field]['EventDescriptor']['Keyword']))
                formatted_event["System.TimeCreated.SystemTime"] = str(convert_ad_timestamp(int(event[1][field]['TimeStamp'])))
                formatted_event["System.EventRecordID"] = "NA"
                formatted_event["System.Correlation.ActivityID"] = str(event[1][field]['ActivityId'])
                formatted_event["System.Correlation.RelatedActivityID"] = "NA"
                formatted_event["System.Execution.ProcessID"] = str(event[1][field]['ProcessId'])
                formatted_event["System.Execution.ThreadID"] = str(event[1][field]['ThreadId'])
                formatted_event["System.Channel"] = "NA"
                formatted_event["System.Computer"] = "NA"
                formatted_event["System.Security.UserID"] = "NA"
            else:
                formatted_event["EventData.Data." + field] = str(event[1][field])
        # Add event to the queue
        self.etw_queue.put((OrderedDict(formatted_event),"etw"))

    def event_processor(self):
        process_tree = ProcessTree()
        try:
            for event in self.read_event():
                if self.tree:
                    process_tree.add_event(event)

                if not self.silent:
                    output_string = format_compact(event) if self.compact else format_pretty(event)
                    output_string = "{} - PID: {} TID: {} GUID: {}".format(event['EventData.Data.UtcTime'], event['System.Execution.ProcessID'], event['System.Execution.ThreadID'], event['EventData.Data.ProcessGuid']) if self.very_compact else output_string
                    print(output_string)

                if self.outfile and not self.tree:
                    output_string = format_pretty(event) if self.pretty_print else format_compact(event)
                    output_string = "{} - PID: {} TID: {} GUID: {}".format(event['EventData.Data.UtcTime'], event['System.Execution.ProcessID'], event['System.Execution.ThreadID'], event['EventData.Data.ProcessGuid']) if self.very_compact else output_string
                    try:
                        with open(self.outfile, 'a') as f:
                            f.write('%s\n' % output_string)
                    except IOError:
                        print('Error writing to %s' % self.outfile)
        except KeyboardInterrupt:
            self.cleanup()
        if self.tree:
            process_tree.build_process_tree()
            tree = process_tree.abbreviate_tree()
            mode = 'a' if self.append_to_outfile else 'w'
            with open(self.outfile, mode) as f:
                json.dump(tree, f, indent=4)
