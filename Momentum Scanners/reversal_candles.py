import urllib, urllib.parse, urllib.error, urllib.request
import ssl
import json
from datetime import datetime
from pytz import timezone
from talib import SMA, RSI, CDLHAMMER, CDLGRAVESTONEDOJI, CDLSHOOTINGSTAR
import numpy as np
from scipy.signal._peak_finding import argrelmax, argrelmin

tz = timezone('EST')

# import pprint

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

favorites = ('QQQ', 'SPY', 'FB', 'DIS', 'NVDA')

def reversal_candle_scanner(ticker="AMZN") : 
    url_prices = 'https://www.alphavantage.co/query?' + urllib.parse.urlencode({'interval': 'daily', 'outputsize': 'compact', 'function':'TIME_SERIES_DAILY', 'symbol': ticker, 'apikey': 'YSPOO5FANVL57LQ2'})   
    pre_json_prices = urllib.request.urlopen(url_prices, context = ctx).read().decode()
    loaded_json_prices = json.loads(pre_json_prices)['Time Series (Daily)'].values()
    
    open = list(float(price['1. open']) for price in loaded_json_prices)
    high = list(float(price['2. high']) for price in loaded_json_prices)
    low = list(float(price['3. low']) for price in loaded_json_prices)
    close = list(float(price['4. close']) for price in loaded_json_prices)
    
    hammers = CDLHAMMER(np.asarray(open[::-1]), np.asarray(high[::-1]), np.asarray(low[::-1]), np.asarray(close[::-1])).tolist()[::-1]
    gravestones = CDLGRAVESTONEDOJI(np.asarray(open[::-1]), np.asarray(high[::-1]), np.asarray(low[::-1]), np.asarray(close[::-1])).tolist()[::-1]
    shooting_stars = CDLSHOOTINGSTAR(np.asarray(open[::-1]), np.asarray(high[::-1]), np.asarray(low[::-1]), np.asarray(close[::-1])).tolist()[::-1]
    
    print(hammers[0], gravestones[0], shooting_stars[0])

    # return pre_json_prices
    # return open[28], high[28], low[28], close[28]
    return hammers
    
    # RSI(np.asarray(prices[::-1]), timeperiod=14).tolist()[::-1]
    # floated_RSI = floated_RSIs[0]
    
    # oversold_RSI_indices = []
    # overbought_RSI_indices = []

    # for index in list(range(7, 59)) :
    #     if (floated_RSIs[index] > 70) : 
    #         overbought_RSI_indices.append(index)
    #     elif (floated_RSIs[index] < 30) :
    #         oversold_RSI_indices.append(index)

    # if (floated_RSI <= 30) :
    #     for index in oversold_RSI_indices :
    #         if (floated_price < prices[index] and floated_RSI > floated_RSIs[index]) : return ('(' + str(datetime.now(tz)) + ') ' + ticker + ' oversold')
    # elif (floated_RSI >= 70) :
    #     for index in overbought_RSI_indices : 
    #         if (floated_price > prices[index] and floated_RSI < floated_RSIs[index]) : return ('(' + str(datetime.now(tz)) + ') ' + ticker + ' overbought')
    # else :
    #     return ('(' + str(datetime.now(tz)) + ') ' + ticker + ' stable') 

# for ticker in favorites : 
#     print(rsi_divergence_scanner(ticker))

print(reversal_candle_scanner())

