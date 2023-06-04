#!/usr/bin/env python3

import yfinance as yf

ticker = yf.Ticker("GC=F")
print(ticker.info)

