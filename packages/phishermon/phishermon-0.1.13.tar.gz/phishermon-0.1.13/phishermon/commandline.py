import argparse
from phishermon import Phishermon, SysmonHelper

def phishermon_cmdline():

    parser = argparse.ArgumentParser('Read sysmon data and apply behavioural signatures.')
    parser.add_argument('--library', '-l', help='Path to library configuration file', type=str, default=None)
    parser.add_argument('--jobs', '-j', help='Path to job configuration file', type=str, default=None)
    parser.add_argument('--actions', '-a' , help='Path to actions configuration file', type=str, default=None)
    parser.add_argument('--etw', '-e', action='store_true', help='Get events using Event Tracing for Windows', default=False)
    parser.add_argument('--evtx', '-E', action='store_true', help='Use saved sysmon log', default=False)
    parser.add_argument('--evtx-file', '-f', dest='evtx_file', help='Path to the sysmon .evtx file', default=None)
    parser.add_argument('--silent', '-s',  action='store_true', help='Suppress standard output', default=False)
    parser.add_argument('--output', '-o', help='Path to output file', type=str, default=None)
    parser.add_argument('--pretty', '-p',  action='store_true', help='Use indented JSON for all output.', default=False)
    parser.add_argument('--continuous', action='store_true', help='Stop reading the log when the end is reached.', default=False)
    
    args = parser.parse_args()

    p = Phishermon(library_conf=args.library, job_conf=args.jobs, action_conf=args.actions, evtx_file=args.evtx_file, 
                   etw=args.etw, evtx=args.evtx, output_file=args.output, silent=args.silent, pretty_print=args.pretty, continuous=args.continuous)

    p.run()

def sysmon_parser_cmdline():
    parser = argparse.ArgumentParser('Read and output sysmon logs in a reader-friendly format. Use CTRL+C to stop monitoring.')
    parser.add_argument('--etw', '-e', action='store_true', help='Get events using Event Tracing for Windows', default=False)
    parser.add_argument('--evtx', '-E', action='store_true', help='Use saved sysmon log', default=False)
    parser.add_argument('--evtx-file', '-f', dest='evtx_file', help='Path to the sysmon .evtx file.', default=None)
    parser.add_argument('--silent', '-s', action='store_true', help='Suppress standard output.', default=False)
    parser.add_argument('--output', '-o', help='Also write output to this file.', type=str, default=None)
    parser.add_argument('--compact', '-c', action='store_true', help='Use one JSON record per line for all output.', default=False)
    parser.add_argument('--verycompact', '-C', dest='very_compact', action='store_true', help='Print the first 80 characters of each record', default=False)
    parser.add_argument('--pretty', '-p',  action='store_true', help='Use indented JSON for all output.', default=False)
    parser.add_argument('--append', '-a', action='store_true', help='Append to output file instead of overwriting.', default=False)
    parser.add_argument('--continuous', action='store_true', help='Stop reading the log when the end is reached.', default=False)
    parser.add_argument('--tree', '-t', action='store_true', help='Write a process tree to the output-file.', default=False)

    args = parser.parse_args()

    sysmon = SysmonHelper(etw=args.etw, evtx=args.evtx, evtx_file=args.evtx_file, continuous=args.continuous, silent=args.silent, 
                          outfile=args.output, append_to_outfile=args.append, compact=args.compact, very_compact=args.very_compact, 
                          pretty_print=args.pretty, tree=args.tree)

    sysmon.event_processor()
