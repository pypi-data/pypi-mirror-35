import json
import xmltodict
from collections import OrderedDict
from datetime import datetime, timedelta
from dateutil import parser

def timestamp_to_epoch(timestamp_str):
    """Convert the specified timestamp to seconds since the UNIX epoch."""
    #return datetime.strptime(timestamp_str, '%Y-%m-%d %H:%M:%S.%f').timestamp()
    return parser.parse(timestamp_str).timestamp()

# Taken from http://timestamp.ooz.ie/p/time-in-python.html
def convert_ad_timestamp(timestamp):
    """Convert Windows system time format to UNIX"""
    epoch_start = datetime(year=1601, month=1,day=1)
    seconds_since_epoch = timestamp/10**7
    return epoch_start + timedelta(seconds=seconds_since_epoch)


def flatten_dict(branch, flat={}, current_path=''):
    """Flattens all the keys in the path of a nested dictionary to one string.
    
    >>> nested = {'lvl1':{'lvl2':{'lvl3': 'value'}}}
    >>> flatten_dict(nested, {})
    {'lvl1.lvl2.lvl3': 'value'}
    """
    for k, v in branch.items():
        key = k.lstrip('#@')
        path = key if not current_path else '%s.%s' % (current_path, key)
        if isinstance(v, dict):
            flatten_dict(v, flat, current_path=path)
        else:
            flat[path] = v
    return flat

def join_key_value_pairs(data_list):
    """Joins the key value pairs in the parsed event data field.
    
    :param data_list: A list of ordered dictionaries given by calling xmltodict.parse() on the EventData field.

    :returns: An OrderedDict containing the data fields and their values

    >>> example = [OrderedDict({'@Name': 'foo', '#text': 'bar'})]
    >>> join_key_value_pairs(example)
    OrderedDict([('foo', 'bar')])
    """

    flat = OrderedDict()
    for pair in data_list:
        name, value = '', ''
        try:
            name = pair['@Name']
            value = pair['#text']
        except KeyError:
            pass
        if name in flat:
            raise KeyError('Duplicate key: "%s"' % name)
        if name:
            flat[name] = value

    return flat

def flatten_xml_event(xml_event):
    """Converts an XML event into a flattened dictionary.
    
    :param xml_event: Event from Sysmon as an XML string.
    """
    xml = xmltodict.parse(xml_event)
    try:
        del xml['Event']['@xmlns']  # xml version is redundant
    except KeyError:
        pass
    
    xml['Event']['EventData']['Data'] = join_key_value_pairs(xml['Event']['EventData']['Data'])
    flat = OrderedDict()
    flatten_dict(xml['Event'], flat)
    return flat

def format_compact(record):
    """Return the record as a JSON string."""
    return json.dumps(record)

def format_pretty(record):
    """Return the record as a pretty printed JSON string"""
    return json.dumps(record, indent=4)

