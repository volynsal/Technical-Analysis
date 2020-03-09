import urllib, urllib.parse, urllib.error, urllib.request
import ssl
import json
from datetime import datetime
from pytz import timezone
from talib import SMA, RSI
import numpy as np

tz = timezone('EST')

# import pprint

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

favorites = ('AAPL', 'MSFT', 'FB', 'NVDA', 'NFLX')

def two_period_rsi (ticker) : 
    url_prices = 'https://www.alphavantage.co/query?' + urllib.parse.urlencode({'interval': '1min', 'outputsize': 'full', 'function':'TIME_SERIES_INTRADAY', 'symbol': ticker, 'apikey': '2VNO5H70PQ6GSC98'})   
    pre_json_prices = urllib.request.urlopen(url_prices, context = ctx).read().decode()
    loaded_json_prices = json.loads(pre_json_prices)['Time Series (1min)'].values()
    
    prices = list(float(price['4. close']) for price in loaded_json_prices)
    floated_price = prices[0]
    prices.reverse()

    floated_SMAs_200 = SMA(np.asarray(prices), timeperiod=200).tolist()
    floated_SMAs_200.reverse()
    floated_SMA_200 = floated_SMAs_200.pop(0)

    floated_SMAs_5 = SMA(np.asarray(prices), timeperiod=5).tolist()
    floated_SMAs_5.reverse()
    floated_SMA_5 = floated_SMAs_5.pop(0)

    floated_RSIs = RSI(np.asarray(prices), timeperiod=2).tolist()
    floated_RSIs.reverse()
    floated_RSI = floated_RSIs.pop(0)
    
    if (floated_price > floated_SMA_200 and floated_price < floated_SMA_5 and floated_RSI <= 5) : 
        return ('(' + str(datetime.now(tz)) + ') ' + ticker + ' oversold')
    elif (floated_price < floated_SMA_200 and floated_price > floated_SMA_5 and floated_RSI >= 95) : 
        return ('(' + str(datetime.now(tz)) + ') ' + ticker + ' overbought')
    else : 
        return ('(' + str(datetime.now(tz)) + ') ' + ticker + ' stable') 

# for ticker in favorites : 
#     print(two_period_rsi(ticker))


