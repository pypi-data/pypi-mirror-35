KEY_EVENT_ID = 'System.EventID.text'
KEY_P_GUID = 'EventData.Data.ProcessGuid'
KEY_PP_GUID = 'EventData.Data.ParentProcessGuid'
KEY_TIMESTAMP = 'System.TimeCreated.SystemTime'
KEY_IMAGE = 'EventData.Data.Image'
GUID_ROOT = ''

EVENT_KEYS_ALL = [
    KEY_TIMESTAMP,
    # KEY_P_GUID,
]

EVENT_KEYS = {
    '1': [
        'Process Create',
        'EventData.Data.Image',
        'EventData.Data.CommandLine',
        'EventData.Data.ProcessGuid',
        'EventData.Data.ProcessId',
        'EventData.Data.LogonGuid',
        'EventData.Data.ParentImage',
        'EventData.Data.ParentProcessGuid',
        'EventData.Data.ParentProcessId',
        'EventData.Data.Hashes',
    ],
    '2': [
        'Changed File Creation Time',
        'EventData.Data.Image',
    ],
    '3': [
        'Network Connection',
        'EventData.Data.Protocol',
        'EventData.Data.SourceIp',
        'EventData.Data.SourcePort',
        'EventData.Data.DestinationIp',
        'EventData.Data.DestinationPort',
    ],
    '4': [
        'SYSMON State Changed',
    ],
    '5': [
        'Process Terminated',
    ],
    '6': [
        'Driver Load',
        'EventData.Data.ImageLoaded',
        'Realtek Semiconductor Corp.',
    ],
    '7': [
        'Image Load',
        'EventData.Data.ImageLoaded',
        'EventData.Data.Signature',
        'EventData.Data.SignatureStatus',
    ],
    '8': [
        'Create Remote Thread',
        'EventData.Data.SourceImage',
        'EventData.Data.SourceProcessGuid',
        'EventData.Data.SourceProcessId',
        'EventData.Data.TargetImage',
        'EventData.Data.TargetProcessGuid',
        'EventData.Data.TargetProcessId',
        'EventData.Data.StartAddress',
        'EventData.Data.StartModule',
        'EventData.Data.StartFunction',
    ],
    '9': [
        'Raw Access Read',
    ],
    '10': [
        'Process Access',
    ],
    '11': [
        'File Create',
        'EventData.Data.TargetFilename',
    ],
    '12': [
        'Registry Object',
        'EventData.Data.EventType',
        'EventData.Data.TargetObject',
    ],
    '13': [
        'Registry Value Set',
        'EventData.Data.TargetObject',
        'EventData.Data.Details',
    ],
    '14': [
        'Registry Object Renamed',
        'EventData.Data.EventType',
        'EventData.Data.TargetObject',
        'EventData.Data.NewName',
    ],
    '15': [
        'File Create Stream Hash',
        'EventData.Data.TargetFilename',
        'EventData.Data.Hashes',
    ],
    '16': [
        'SYSMON Config Change',
    ],
    '17': [
        'Pipe Created',
    ],
    '18': [
        'Pipe Connected',
    ],
    '19': [
        'WMI Event Filter',
    ],
    '20': [
        'WMI Event Consumer',
    ],
    '21': [
        'WMI Event Connector',
    ],
    '255': [
        'SYSMON ERROR',
    ],
}