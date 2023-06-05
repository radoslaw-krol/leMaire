import argparse
from commands import chart_command, json, opening_command 

# Import JSON

with open("command_mapping.json") as f:
    command_mapping = json.load(f)




# Create the main parser
parser = argparse.ArgumentParser(prog='lemaire')
subparsers = parser.add_subparsers(title='commands', dest='command')

# Create the parser for the "chart" command
chart_parser = subparsers.add_parser('chart', help='chart command help')
chart_parser.set_defaults(func=chart_command)

# Creare the parser for the "opening" command
opening_parser = subparsers.add_parser('opening', help='opening command help')
opening_parser.add_argument('product', choices=list(command_mapping.keys()), help='product name')
opening_parser.set_defaults(func=opening_command)



# Parse the command-line arguments
args = parser.parse_args()

# Call the appropriate function based on the command
if hasattr(args, 'func'):
    args.func(args)
else:
    parser.print_help()

