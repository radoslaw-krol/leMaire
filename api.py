#!/usr/bin/env python3

import os
import yfinance as yf
import json
from datetime import date

# Read the ticker symbol from ticker_symbol.txt

with open('ticker_symbol.txt','r+') as file:
    ticker_symbol = file.read().strip()

# Get the current date
current_date = date.today().strftime("%Y-%m-%d")


# Check if the file exists
if os.path.exists('result.json'):
    with open('result.json', 'r') as json_file:
        file_content = json_file.read()

        # Check if the file content is empty or not valid JSON
        if not file_content or not file_content.strip():
            data = {}
        else:
            try:
                data = json.loads(file_content)
            except json.JSONDecodeError:
                data = {}
else:
    data = {}

# Check if the file content contains a header with the current date
if current_date in data:
    print(f"Data for {current_date} already exists in the file.")
else:
    ticker = yf.Ticker(ticker_symbol)
    result = ticker.info

    # Remove unnecessary fields from the result
    fields_to_keep = ['previousClose', 'open', 'dayLow', 'dayHigh', 'volume', 'bid', 'ask']
    filtered_result = {key: result[key] for key in fields_to_keep if key in result}

    # Update the data with the new result
    data[current_date] = filtered_result

    with open('result.json', 'w') as json_file:
        json.dump(data, json_file, indent=4)

