import os
import json
import yfinance as yf
import plotext as plt
from datetime import date, timedelta


# Define base directory to support files like history.json being saved in the same directory, regardless of where from the system file was executed
base_dir = os.path.dirname(os.path.abspath(__file__))


def chart_command(args):
    # Functionality for the "chart" command
    print("Executing chart command")
    
    if args.choice == 'history30':
        json_file = 'history.json'
    elif args.choice == 'history6M':
        json_file = 'history6M.json'
    elif args.choice == 'history1Y':
        json_file = 'history1Y.json'
    else:
        print("Invalid choice")
        return


    with open(json_file, "r") as file:
        json_data = file.read()

    data =  json.loads(json_data)

    open_values = list(data["Open"].values())


    plt.plot_size(90,20)

    plt.plot(open_values)

    plt.show()


def opening_command(args):
    product = args.product
    ticker =  get_ticker_by_product(product)
    apiPull = yf.Ticker(ticker)
    result = apiPull.info

    # Remove unnecessary fields from the result
    fields_to_keep = ['previousClose', 'open', 'dayLow', 'dayHigh', 'volume', 'bid', 'ask']
    filtered_result = {key: result[key] for key in fields_to_keep if key in result}

    if 'open' in filtered_result:
        print(f"Opening {product} ({ticker})")
        print(f"Opening Price: {filtered_result['open']}")
    else:
        print(f"Unable to retrieve opening price for {product} ({ticker})")

def day_command(args):
    product = args.product
    ticker =  get_ticker_by_product(product)
    apiPull = yf.Ticker(ticker)
    result = apiPull.info

    # Remove unnecessary fields from the result
    fields_to_keep = ['previousClose', 'open', 'dayLow', 'dayHigh', 'volume', 'bid', 'ask']
    filtered_result = {key: result[key] for key in fields_to_keep if key in result}

    if 'dayLow' in filtered_result:
        print(f"Opening {product} ({ticker})")
        print(f"Day Low Price: {filtered_result['dayLow']}")
        print(f"Day High Price: {filtered_result['dayHigh']}")
        print(f"Volume Traded: {filtered_result['volume']}")
    else:
        print(f"Unable to retrieve one of the following: dayLow,dayHigh,volume for {product} ({ticker})")


def history30_command(args):
    product = args.product
    ticker = get_ticker_by_product(product)
    
    historical_data = yf.download(ticker, start=date.today() - timedelta(days=30) , end=date.today())
    historical_data_json = historical_data.to_json(orient="columns")
    file_path = "history.json"
   
    with open(file_path, "w") as json_file:
        json_file.write(historical_data_json)

    print(f"Data saved in: {os.path.abspath(file_path)}")


def history6M_command(args):
    product = args.product
    ticker = get_ticker_by_product(product)
    
    historical_data = yf.download(ticker, start=date.today() - timedelta(days = 182) , end=date.today())
    historical_data_json = historical_data.to_json(orient="columns")
    file_path = "history6M.json"
   
    with open(file_path, "w") as json_file:
        json_file.write(historical_data_json)

    print(f"Data saved in: {os.path.abspath(file_path)}")


def history1Y_command(args):
    product = args.product
    ticker = get_ticker_by_product(product)
    
    historical_data = yf.download(ticker, start=date.today() - timedelta(days = 365) , end=date.today())
    historical_data_json = historical_data.to_json(orient="columns")
    file_path = "history1Y.json"
   
    with open(file_path, "w") as json_file:
        json_file.write(historical_data_json)

    print(f"Data saved in: {os.path.abspath(file_path)}")



def get_ticker_by_product(product):

    json_loc = os.path.dirname(os.path.abspath(__file__))
    command_mapping_loc = os.path.join(json_loc, 'command_mapping.json')


    with open(command_mapping_loc) as f:
        command_mapping = json.load(f)



    ticker =  command_mapping.get(product)

    if ticker is None:
        print (f"Ticker not found for product: {product}")
        return ''

    return ticker

