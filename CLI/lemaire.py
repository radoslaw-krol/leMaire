import argparse
from commands import chart_command

# Create the main parser
parser = argparse.ArgumentParser(prog='lemaire')
subparsers = parser.add_subparsers(title='commands', dest='command')

# Create the parser for the "chart" command
chart_parser = subparsers.add_parser('chart', help='chart command help')
chart_parser.set_defaults(func=chart_command)

# Parse the command-line arguments
args = parser.parse_args()

# Call the appropriate function based on the command
if hasattr(args, 'func'):
    args.func(args)
else:
    parser.print_help()

