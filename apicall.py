#!/usr/bin/env python


import yfinance as yf
import json
from datetime import date


#Get Current Date
current_date = date.today().strftime("%Y-%m-%d")


msft = yf.Ticker("CL=F")
result = msft.info

# Convert result to JSON
result_json = json.dumps(result, indent=4)

# Append the JSON result to a file
with open('result.json', 'a') as json_file:
    json_file.write(f"\n\n----- {current_date} -----\n\n") # add date separation
    json_file.write(result_json)
    json_file.write('\n')  # Add a newline character for readability if desired

