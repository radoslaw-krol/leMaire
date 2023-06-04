import json
import yfinance as yf
from datetime import date, timedelta
import os
ticker_symbol = "CL=F"


# Get the current date
current_date = date.today().strftime("%Y-%m-%d")



historical_data = yf.download(ticker_symbol, start=date.today() - timedelta(days=30) , end=date.today())
historical_data_json = historical_data.to_json(orient="columns")
file_path = "history.json"

with open(file_path, "w") as json_file:
    json_file.write(historical_data_json)

print(f"Data saved in: {os.path.abspath(file_path)}")

