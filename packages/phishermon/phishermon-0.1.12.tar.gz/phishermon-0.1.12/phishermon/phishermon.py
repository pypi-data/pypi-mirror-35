import os
import json
import platform
from electus import Electus
from .sysmon_helper import SysmonHelper
from .action import Action
from .utils import format_pretty

class Phishermon(object):

    def __init__(self, library_conf=None, job_conf=None, action_conf=None, evtx_file=None, etw=False, evtx=True, output_file=None, 
                 silent=False, pretty_print=False, continuous=False):

        self.library_conf = library_conf
        self.job_conf = job_conf
        self.action_conf = action_conf
        self.evtx_file = evtx_file
        self.etw = etw
        self.evtx = evtx
        self.output_file = output_file
        self.silent = silent
        self.pretty_print = pretty_print
        self.continuous = continuous

        if self.action_conf:
            if platform.system() == 'Windows' and not self.etw:
                raise ValueError('Actions can only be taken on Windows machines when ETW is True.')
            elif platform.system() != 'Windows':
                raise NotImplementedError('Actions can only be taken on Windows machines.')

        if not self.etw and not self.evtx:
            raise ValueError("No data source specified. At least one of etw or evtx must be True.")

        # Instantiate electus
        self.sig_engine = Electus(self.library_conf, self.job_conf)
        # Instantiate sysmon parser 
        self.sysmon = SysmonHelper(etw=self.etw, evtx=self.evtx, evtx_file=self.evtx_file, continuous=self.continuous)

        # Will return empty list if actions are not defined
        self.actions = self.get_actions()

    @property
    def library_conf(self):
        """Path to an electus library configuration file."""
        return self._library_conf 

    @library_conf.setter
    def library_conf(self, conf):
        if conf is not None:
            if os.path.exists(conf):
                self._library_conf = conf
            else:
                raise ValueError('Could not find library configuration file {}'.format(conf))
        else:
            raise ValueError('Library configuration file must be specified')

    @property
    def job_conf(self):
        """Path to an electus job configuration file."""
        return self._job_conf 

    @job_conf.setter
    def job_conf(self, conf):
        if conf is not None:
            if os.path.exists(conf):
                self._job_conf = conf
            else:
                raise IOError('Could not find job configuration file {}'.format(conf))   
        else:
            raise ValueError('Job configuration file must be specified')

    @property
    def action_conf(self):
        return self._action_conf
    
    @action_conf.setter
    def action_conf(self, conf):
        if conf is not None:
            if not os.path.exists(conf):
                raise IOError('Could not find actions configuration file {}'.format(conf))
            
        self._action_conf = conf

    @property
    def evtx_file(self):
        """Path to the Sysmon event log file. Default on Windows is C:\\Windows\\System32\\winevt\\Logs\\Microsoft-Windows-Sysmon%4Operational.evtx.
        On all other systems the default is None.
        """
        return self._evtx_file

    @evtx_file.setter
    def evtx_file(self, fname):
        self._evtx_file = fname

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
    def output_file(self):
        """File to log alerts to."""
        return self._output_file

    @output_file.setter
    def output_file(self, fname):
        self._output_file = fname

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
    def pretty_print(self):
        """Use indented JSON for all output."""
        return self._pretty_print
    
    @pretty_print.setter
    def pretty_print(self, p):
        if isinstance(p, bool):
            self._pretty_print = p
        else:
            raise ValueError('Pretty_print must be True or False')

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

    def get_actions(self):
        """Load the actions defined in the action configuration file."""
        if self.action_conf:
            actions = []
            with open(self.action_conf, 'r') as f:
                loaded_config = json.load(f)
            for action_name in loaded_config:
                actions.append(Action(action_name, loaded_config[action_name]))

            return actions
        else:
            return []

    def take_action(self, alert):
        """Evaluate if actions should be taken and execute them if needed.
        
        :param alert: An electus Alert object.
        """

        for action in self.actions:
            if action.name == alert.name:
                for correlation in action.correlations:
                    to_match = []
                    for ind in correlation:
                        for hit in alert.hits:
                            if ind.name == hit.name:
                                ind.extract_data(hit.event)
                                to_match.append(hit.event[ind.field])
                    if (len(set(to_match)) == 1) and len(to_match) >= len(correlation):
                        for ind in correlation:
                            ind.take_action(action.name)

    def run(self):

        for event in self.sysmon.read_event():
            alerts = self.sig_engine.evaluate_event(event)

            if alerts:
                for alert in alerts:

                    if self.actions:
                        self.take_action(alert)

                    if self.output_file:
                        with open(self.output_file, 'a') as f:
                            json.dump(alert.to_dict(), f, indent=4)
                    if not self.silent:
                        if self.pretty_print:
                            print(format_pretty(alert.to_dict()))
                        else:
                            print(alert.to_dict())



