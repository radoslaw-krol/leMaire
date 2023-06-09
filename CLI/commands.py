import os
import json
from numpy import product
import yfinance as yf
import plotext as plt
import pandas as pd
from datetime import date, timedelta
from dateutil import parser



#matplot

import mplfinance as mpf

# Define base directory to support files like history.json being saved in the same directory, regardless of where from the system program was executed
base_dir = os.path.dirname(os.path.abspath(__file__))
json_dir = os.path.join(base_dir, 'JSON')
csv_dir  = os.path.join(base_dir, 'CSV')


def chart_command(args):
    # Functionality for the "chart" command
    print("Executing chart command")

    if args.choice == 'history30':
        json_file =os.path.join(json_dir, 'history.json')
    elif args.choice == 'history6M':
        json_file =os.path.join(json_dir, 'history6M.json')
    elif args.choice == 'history1Y':
        json_file =os.path.join(json_dir, 'history1Y.json')
    elif args.choice == 'period1M':
        json_file =os.path.join(json_dir, 'periodical.json')
    else:
        print("Invalid choice")
        return


    with open(json_file, "r") as file:
        json_data = file.read()

    data =  json.loads(json_data)
   
    timestamps = list(data.keys())


    
    if args.value not in data[timestamps[0]]:
        print("Invalid value choice")
        return

    values = [entry[args.value] for entry in data.values()]
    
    formatted_timestamps = [parser.parse(timestamp).strftime('%d/%m/%Y') for timestamp in timestamps]

    plt.plot_size(90,20)
    plt.plot(formatted_timestamps, values, fillx=True)

    plt.show()

def stockcandle_command():

    file = os.path.join(csv_dir, "AAPL.csv")


    data = pd.read_csv(file)
    
    data.Date = pd.to_datetime(data.Date)

    data = data.set_index('Date')
   


    mpf.plot(data,type='candle',mav=(20),volume=True,tight_layout=True,figratio=(20,12))


def shortcandle_command(args):
            
    product = args.product
    ticker = get_ticker_by_product(product)
    data = yf.download(ticker, period='30d')

    plt.date_form('d/m/Y')

    dates = plt.datetimes_to_string(data.index)

    plt.candlestick(dates, data)

    plt.title(f"{product} Stock Price Candlesticks")
    plt.xlabel("Date")
    plt.ylabel("Stock Price $")
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

    historical_data_dict = historical_data.to_dict(orient="index")

    historical_data_dict = {
            str(key): value
            for key, value in historical_data_dict.items()
            }

    file_path = os.path.join(json_dir, "history.json")

   
    with open(file_path, "w") as json_file:
        json.dump(historical_data_dict, json_file)

    print(f"Data saved in: {os.path.abspath(file_path)}")


def history6M_command(args):
    product = args.product
    ticker = get_ticker_by_product(product)
    
    historical_data = yf.download(ticker, start=date.today() - timedelta(days = 182) , end=date.today())

    historical_data_dict = historical_data.to_dict(orient="index")

    historical_data_dict = {
            str(key): value
            for key, value in historical_data_dict.items()
            }

    file_path = os.path.join(json_dir, "history6M.json")
   
    with open(file_path, "w") as json_file:
        json.dump(historical_data_dict, json_file)

    print(f"Data saved in: {os.path.abspath(file_path)}")


def history1Y_command(args):
    product = args.product
    ticker = get_ticker_by_product(product)
    
    historical_data = yf.download(ticker, start=date.today() - timedelta(days = 365) , end=date.today())

    historical_data_dict = historical_data.to_dict(orient="index")

    historical_data_dict = {
            str(key): value
            for key, value in historical_data_dict.items()
            }

    file_path = os.path.join(json_dir, "history1Y.json")
   
    with open(file_path, "w") as json_file:
        json.dump(historical_data_dict, json_file)

    print(f"Data saved in: {os.path.abspath(file_path)}")

def period1M_command(args):
    product = args.product
    ticker = get_ticker_by_product(product)

    tickerYF = yf.Ticker(ticker)

    periodical_data = tickerYF.history(period="1mo")

    periodical_data_dict = periodical_data.to_dict(orient="index")
    
    periodical_data_dict ={ 
    
        str(key): value
        for key, value in periodical_data_dict.items()


    }

    file_path = os.path.join(json_dir, "periodical.json")

    with open(file_path, "w") as json_file:
        json.dump(periodical_data_dict, json_file)
    print(f"Data saved in: {os.path.abspath(file_path)}")



def stock_command(args):
    product = args.product
    ticker = get_ticker_by_product(product)
    
    stock_data = yf.download(ticker, start=date.today() - timedelta(days=30), end=date.today())

    file_path = os.path.join(json_dir, "stock.json")
   
    # Convert index to datetime objects
    stock_data.index = pd.to_datetime(stock_data.index, unit='ms')



    # Convert timestamps to human-readable dates
    stock_data['Date'] = stock_data.index.strftime('%d/%m/%Y')
    
    # Convert the stock_data DataFrame to a dictionary with string keys
    stock_dict = stock_data.rename(index=str).to_dict(orient='index')

    # Write the JSON data to a file
    with open(file_path, "w") as json_file:
        json.dump(stock_dict, json_file)

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

