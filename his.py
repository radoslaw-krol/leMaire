import json
import yfinance as yf
from datetime import date, timedelta
import os
ticker_symbol = "CL=F"


# Get the current date
current_date = date.today().strftime("%Y-%m-%d")



historical_data = yf.download(ticker_symbol, start=date.today() - timedelta(days=30) , end=date.today())

# Check if the file exists
if os.path.exists('historical.json'):
    with open('historical.json', 'r') as json_file:
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
    with open('historical.json', 'w') as json_file:
        json.dump(data,json_file, indent=4)


