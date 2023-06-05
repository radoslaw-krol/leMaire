#!/usr/bin/env python3

import yfinance as yf


    ticker = yf.Ticker(ticker_symbol)
    result = ticker.info

    # Remove unnecessary fields from the result
    fields_to_keep = ['previousClose', 'open', 'dayLow', 'dayHigh', 'volume', 'bid', 'ask']
    filtered_result = {key: result[key] for key in fields_to_keep if key in result}

