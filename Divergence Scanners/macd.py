import urllib, urllib.parse, urllib.error, urllib.request
import ssl
import json
from datetime import datetime
from pytz import timezone
from talib import SMA, RSI
import numpy as np
from scipy.signal._peak_finding import argrelmax, argrelmin

tz = timezone('EST')

# import pprint

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

favorites = ('QQQ', 'SPY', 'FB', 'DIS', 'NVDA')

def rsi_divergence_scanner(ticker="QQQ") : 
    url_prices = 'https://www.alphavantage.co/query?' + urllib.parse.urlencode({'interval': '1min', 'outputsize': 'compact', 'function':'TIME_SERIES_INTRADAY', 'symbol': ticker, 'apikey': '2VNO5H70PQ6GSC98'})   
    pre_json_prices = urllib.request.urlopen(url_prices, context = ctx).read().decode()
    loaded_json_prices = json.loads(pre_json_prices)['Time Series (1min)'].values()
    
    prices = list(float(price['4. close']) for price in loaded_json_prices)
    floated_price = prices[0]
    
    floated_RSIs = RSI(np.asarray(prices[::-1]), timeperiod=14).tolist()[::-1]
    floated_RSI = floated_RSIs[0]
    
    oversold_RSI_indices = []
    overbought_RSI_indices = []

    for index in list(range(7, 59)) :
        if (floated_RSIs[index] > 70) : 
            overbought_RSI_indices.append(index)
        elif (floated_RSIs[index] < 30) :
            oversold_RSI_indices.append(index)

    if (floated_RSI <= 30) :
        for index in oversold_RSI_indices :
            if (floated_price < prices[index] and floated_RSI > floated_RSIs[index]) : return ('(' + str(datetime.now(tz)) + ') ' + ticker + ' oversold')
    elif (floated_RSI >= 70) :
        for index in overbought_RSI_indices : 
            if (floated_price > prices[index] and floated_RSI < floated_RSIs[index]) : return ('(' + str(datetime.now(tz)) + ') ' + ticker + ' overbought')
    else :
        return ('(' + str(datetime.now(tz)) + ') ' + ticker + ' stable') 

# for ticker in favorites : 
#     print(rsi_divergence_scanner(ticker))

print(rsi_divergence_scanner('SPY'))

