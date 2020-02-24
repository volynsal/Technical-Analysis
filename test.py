import pandas_datareader.data as web
import pandas as pd
import numpy as np
import os
from talib import RSI, BBANDS
# import matplotlib.pyplot as plt
start = '2015-04-22'
end = '2020-02-20'
os.environ["QUANDL_API_KEY"] = "EQTC8DVGuhfscH6tzoxx"

symbol = 'AAPL'
max_holding = 100
price = web.DataReader(name=symbol, data_source='quandl', start=start, end=end)
price = price.iloc[::-1]
price = price.dropna()
close = price['AdjClose'].tolist()

print(close)

# up, mid, low = BBANDS(close, timeperiod=20, nbdevup=2, nbdevdn=2, matype=0)
# rsi = RSI(close, timeperiod=14)
# print("RSI (first 10 elements)\n", rsi.tolist().pop())