leMaire Program Documentation

leMaire is a command-line program developed for analyzing and visualizing stock market data. It utilizes the Python programming language and various libraries to provide insights into stock market trends.

The program uses the following libraries:

    argparse: This library is used for parsing command-line arguments and generating the program's command-line interface.
    json: The json library is used to read and parse JSON data files that contain stock market data.
    dateutil.parser: This library is used to parse date and time strings from the stock market data.
    plotext: The plotext library is used for creating candlestick charts to visualize stock market data.

By running the leMaire program with appropriate commands, such as lemaire stockcandle, users can generate candlestick charts based on the stock market data stored in a JSON file. The program reads the JSON data, extracts the necessary information (open, high, low, close prices), converts the data types as required, and plots the candlestick chart using plotext. The resulting chart provides a visual representation of the stock market's price movements over time.
