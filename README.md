leMaire Program Documentation

leMaire is a command-line program developed for analyzing and visualizing stock market data. It utilizes the Python programming language and various libraries to provide insights into stock market trends.

The program uses the following libraries:

    argparse: This library is used for parsing command-line arguments and generating the program's command-line interface.
    json: The json library is used to read and parse JSON data files that contain stock market data.
    dateutil.parser: This library is used to parse date and time strings from the stock market data.
    plotext: The plotext library is used for creating candlestick charts to visualize stock market data.

By running the leMaire program with appropriate commands, such as lemaire stockcandle, users can generate candlestick charts based on the stock market data stored in a JSON file. The program reads the JSON data, extracts the necessary information (open, high, low, close prices), converts the data types as required, and plots the candlestick chart using plotext. The resulting chart provides a visual representation of the stock market's price movements over time.


    chart: This command is used to plot historical data for a specific value (e.g., open price, volume, high, low, close) over a specified time period. It reads data from a JSON file (history.json, history6M.json, history1Y.json, or periodical.json) and uses the plotext library to create the chart.

    stockcandle: This command plots candlestick charts for a specific stock using data from a CSV file (AAPL.csv). It uses the mplfinance library to generate the candlestick chart.

    shortcandle: This command plots candlestick charts for a specific product using data from Yahoo Finance. It uses the yfinance library to download the data and the plotext library to create the chart.

    opening: This command retrieves the opening price for a specific product from Yahoo Finance.

    day: This command retrieves the opening price, day low price, day high price, and volume traded for a specific product from Yahoo Finance.

    history30, history6M, history1Y: These commands download historical data for a specific product from Yahoo Finance and save it in JSON files (history.json, history6M.json, history1Y.json) for 30 days, 6 months, or 1 year, respectively.

    period1M: This command downloads periodic data (monthly) for a specific product from Yahoo Finance and saves it in a JSON file (periodical.json).

    stock: This command downloads stock data for a specific product from Yahoo Finance and saves it in a JSON file (stock.json).

The code uses the command_mapping.json file to map product names to their corresponding tickers on Yahoo Finance. The argparse module is used to define command-line arguments and subcommands, and each command is associated with a specific function that is called when the command is executed.

To run this program, you would need to provide the necessary input files (CSV and JSON files) and ensure that the required libraries (yfinance, plotext, mplfinance) are installed.
