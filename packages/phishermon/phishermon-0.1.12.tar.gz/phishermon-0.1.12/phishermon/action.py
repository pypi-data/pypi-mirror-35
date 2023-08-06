import os
from .mitigations import MitigateFile, MitigateProcess, MitigateRegistry

mitigate_proc = MitigateProcess()
mitigate_file = MitigateFile()
mitigate_reg = MitigateRegistry()

class Action(object):

    def __init__(self, name, correlations):

        self.name = name
        self.correlations = correlations

    @property
    def name(self):
        """A unique name for the action."""
        return self._name

    @name.setter
    def name(self, n):
        if isinstance(n, str):
            self._name = n
        else:
            raise ValueError('Name must be a string')

    @property
    def correlations(self):
        """List of :class:`~phishermon.action.CorrelationIndicator` objects. Defined in the action configuration file."""
        return self._correlations

    @correlations.setter
    def correlations(self, corrs):
        if not isinstance(corrs, list):
            raise ValueError('Value for action {} must be a list'.format(self.name))

        self._correlations = [CorrelationIndicator(c) for c in corrs]


class CorrelationIndicator(object):

    valid_types = {'process': ['process', 'pid'], 'file': ['path'], 'registry': ['path', 'key']}

    def __init__(self, conf):

        self.name = conf['name']
        self.field = conf['field']
        self.event_type = conf.get('type', None)
        self.extract = conf.get('to_extract', {})

        if self.event_type and not self.extract:
            raise ValueError('Type is specified but there are no fields to extract. Please specify a to_extract field.')

    @property
    def name(self):
        """Name of the job in the job configuration file"""
        return self._name

    @name.setter
    def name(self, n):
        if isinstance(n, str):
            self._name = n
        else:
            raise ValueError('Name must be a string')

    @property
    def field(self):
        """Field name to compare between hit objects. An action will only be taken if all the values of field in the hit objects match."""
        return self._field

    @field.setter
    def field(self, f):
        if isinstance(f, str):
            self._field = f
        else:
            raise ValueError('Field must be a string')

    @property
    def extract(self):
        """A dictionary of fields to extract to take action.
        The required fields for each type are {'process': ['process', 'pid'], 'file': ['path'], 'registry': ['path', 'key']}
        """
        return self._extract

    @extract.setter
    def extract(self, e):

        if e and self.event_type is None:
            raise ValueError('extract is set but type is not specified')

        if not e:
            self._extract = None
        elif isinstance(e, dict):
            e = {k.lower(): v for k,v in e.items()}
            for f in self.valid_types[self.event_type]:
                if f not in e:
                    raise ValueError('Type {} must have keys {} in the extract field. Given keys were {}'
                                        .format(self.event_type, self.valid_types[self.event_type], list(e.keys())))

            self._extract = e
        else:
            raise ValueError('to_extract must be a dictionary')

    @property
    def event_type(self):
        """The type of event to take action on. Valid event types are process, file, or registry."""
        return self._event_type

    @event_type.setter
    def event_type(self, t):
        if t is None:
            self._event_type = None
        elif not isinstance(t, str):
            raise ValueError('type must be a string')
        elif t.lower() not in self.valid_types:
            raise ValueError('type {} is not a valid type. Valid types are: {}'.format(t, self.valid_types.keys()))
        else:
            self._event_type = t.lower()

    def extract_data(self, event):
        """Get the data from the fields defined by to_extract."""
        if self.extract:
            self.extracted_data = {k: event[v] for k, v in self.extract.items()}
        else:
            self.extracted_data = None

    def take_action(self, action_name=None):
        """Take the action specified."""
        if not self.extracted_data:
            return None

        if self.event_type == 'process':
            proc = self.extracted_data.get('process', None)
            if proc is not None:
                proc = os.path.basename(proc)
            pid = self.extracted_data.get('pid', None)

            if proc is not None and pid is not None:
                mitigate_proc.kill_process(int(pid), proc)

        elif self.event_type == 'file':
            path = self.extracted_data.get('path', None)

            if path is not None:
                mitigate_file.delete_file(path)
        
        elif self.event_type == 'registry':
            path = self.extracted_data.get('path', None)
            key = self.extracted_data.get('key', None)

            if path is not None and key is not None:
                mitigate_reg.delete_registry_key(path, key)













