import yfinance as yf
import json
from datetime import date

# Get the current date
current_date = date.today().strftime("%Y-%m-%d")

#Define the ticker symbol variable

ticker_symbol = "CL-F"


# Perform the check and save data if necessary
with open('result.json', 'r+') as json_file:
    file_content = json_file.read()

    # Check if the file content contains a header with the current date
    if f"----- {current_date} -----" in file_content:
        print(f"Data for {current_date} already exists in the file.")
    else:
        ticker = yf.Ticker(ticker_symbol)
        result = ticker.info

        # Convert result to JSON
        result_json = json.dumps(result, indent=4)

        # Append the JSON result to the file with the date as a separator
        if file_content:
            json_file.write('\n\n')
        json_file.write(f"----- {current_date} -----\n\n")
        json_file.write(result_json)
        json_file.write('\n')

