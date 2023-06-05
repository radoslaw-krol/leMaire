import json
import yfinance as yf


def chart_command(args):
    # Functionality for the "chart" command
    print("Executing chart command")

def opening_command(args):
    product = args.product
    ticker =  get_ticker_by_prodyct(product)
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



def get_ticker_by_prodyct(product):
    with open('command_mapping.json') as f:
        command_mapping = json.load(f)
    return command_mapping.get(product, '')
