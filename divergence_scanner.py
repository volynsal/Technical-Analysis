import urllib, urllib.parse, urllib.error, urllib.request
import ssl
import json
from datetime import datetime
from pytz import timezone
from talib import SMA, RSI
import numpy as np
from scipy import signal

tz = timezone('EST')

# import pprint

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

def divergence_scanner (ticker="SPY") :
    url_prices = 'https://www.alphavantage.co/query?' + urllib.parse.urlencode({'interval': '1min', 'outputsize': 'full', 'function':'TIME_SERIES_INTRADAY', 'symbol': ticker, 'apikey': 'YSPOO5FANVL57LQ2'})   
    pre_json_prices = urllib.request.urlopen(url_prices, context = ctx).read().decode()
    loaded_json_prices = json.loads(pre_json_prices)['Time Series (1min)'].values()
    
    last_minute = list(json.loads(pre_json_prices)['Time Series (1min)'].keys()).pop(0)

    prices = list(float(price['4. close']) for price in loaded_json_prices)
    floated_price = prices[0]
    prices.reverse()

    x = np.array(prices)

    rsi = RSI(x, timeperiod=14).tolist()
    rsi.reverse()

    # min_indices = signal.argrelmin(x)
    # max_indices = signal.argrelmax(x)

    # mins = []
    # maxs = []

    # for min in min_indices[0] : 
    #     mins.append(prices[min])

    # for max in max_indices: 
    #     maxs.append(prices[max])

    if (floated_price < floated_SMA_10 * 0.95) : 
        return ('Be careful buying / lock in gains')
    elif (floated_price > floated_SMA_10 * 1.05) : 
        return ('Great time to buy')
    else : 
        return ('No direction yet') 

print(divergence_scanner())