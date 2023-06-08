import os
import argparse
from commands import chart_command, json, opening_command, day_command, history30_command, history6M_command, history1Y_command, period1M_command, stock_command, stockcandle_command
from commands import shortcandle_command
# Determine location of command_mapping.json file

json_loc = os.path.dirname(os.path.abspath(__file__))

#Construct the full path to the JSON file

command_mapping_loc = os.path.join(json_loc, 'command_mapping.json')


# Import JSON

with open(command_mapping_loc) as f:
    command_mapping = json.load(f)

#  Main parser
parser = argparse.ArgumentParser(prog='lemaire')
subparsers = parser.add_subparsers(title='commands', dest='command')

# Parser for the "chart" command
chart_parser = subparsers.add_parser('chart', help='chart command help')
chart_subparsers = chart_parser.add_subparsers(dest='choice', required=True)


# Parser for the "stockcandle" command
stockcandle_parser = subparsers.add_parser('stockcandle', help='stockcandle command help')
stockcandle_parser.set_defaults(func=stockcandle_command)

# Parser for the "shortcandle" command

shortcandle_parser = subparsers.add_parser('shortcandle', help='shortcandle command help')
shortcandle_parser.add_argument('product', choices=list(command_mapping.keys()), help = 'product name')
shortcandle_parser.set_defaults(func=shortcandle_command)



# Parser for the "history30" command
history30_parser = chart_subparsers.add_parser('history30', help='history30 command help')
history30_parser.add_argument('value', choices=['Open', 'Volume', 'High', 'Low', 'Close'], help='value to display')
history30_parser.set_defaults(func=chart_command)


# Parser for the "history6M" command
history6M_parser = chart_subparsers.add_parser('history6M', help='history6M command help')
history6M_parser.add_argument('value', choices=['Open', 'Volume', 'High', 'Low', 'Close'], help='value to display')
history6M_parser.set_defaults(func=chart_command)


# Parser for the "history1Y" command
history1Y_parser = chart_subparsers.add_parser('history1Y', help='history1Y command help')
history1Y_parser.add_argument('value', choices=['Open', 'Volume', 'High', 'Low', 'Close'], help='value to display')
history1Y_parser.set_defaults(func=chart_command)

# Parser for the "chart period1M" command
period1M_parser = chart_subparsers.add_parser('period1M', help = 'period1M command help')
period1M_parser.add_argument('value', choices=['Open', 'Volume', 'High', 'Low', 'Close'], help='value to display')
period1M_parser.set_defaults(func=chart_command)


# Parser for the "opening" command
opening_parser = subparsers.add_parser('opening', help='opening command help')
opening_parser.add_argument('product', choices=list(command_mapping.keys()), help='product name')
opening_parser.set_defaults(func=opening_command)

# Parser for the "day" command
day_parser = subparsers.add_parser('day', help='day command help')
day_parser.add_argument('product', choices=list(command_mapping.keys()), help='product name')
day_parser.set_defaults(func=day_command)


# Parser for the "history30" command
history30_parser = subparsers.add_parser('history30', help='history30 command help')
history30_parser.add_argument('product', choices=list(command_mapping.keys()), help='product name')
history30_parser.set_defaults(func=history30_command)


# Parser for the "history6M" command

history6M_parser = subparsers.add_parser('history6M', help='history6M command help')
history6M_parser.add_argument('product', choices=list(command_mapping.keys()), help='product name')
history6M_parser.set_defaults(func=history6M_command)

# Parser for the "history1Y" command

history1Y_parser = subparsers.add_parser('history1Y', help='history1Y command help')
history1Y_parser.add_argument('product', choices=list(command_mapping.keys()), help='product name')
history1Y_parser.set_defaults(func=history1Y_command)

# Parser for the "period1M" command

period1M_parser = subparsers.add_parser('period1M', help = 'period1M command help')
period1M_parser.add_argument('product', choices=list(command_mapping.keys()), help='product name')
period1M_parser.set_defaults(func=period1M_command)


# Parser for the "stock" command

stock_parser = subparsers.add_parser('stock', help = 'stock command help')
stock_parser.add_argument('product', choices=list(command_mapping.keys()), help='product name')
stock_parser.set_defaults(func=stock_command)



#Parse the command-line arguments

args = parser.parse_args()

# Call the appropriate function based on the command
if hasattr(args, 'func'):
    if args.func == stockcandle_command:
        args.func()  # Call the function without passing any arguments
    else:
        args.func(args)  # Call the function with the 'args' argument
else:
    parser.print_help()
