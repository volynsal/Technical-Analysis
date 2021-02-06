import urllib, urllib.parse, urllib.error, urllib.request
import ssl
import json
from datetime import datetime
from pytz import timezone
from talib import SMA, RSI
import numpy as np

import quandl

tz = timezone('EST')

# import pprint

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

def fear_gauge () :
    url_prices = vix = quandl.get("CBOE/VIX")
    
    print(url_prices)
    
    pre_json_prices = urllib.request.urlopen(url_prices, context = ctx).read().decode()
    loaded_json_prices = json.loads(pre_json_prices)['Time Series (1min)'].values()
    
    last_minute = list(json.loads(pre_json_prices)['Time Series (1min)'].keys()).pop(0)

    prices = list(float(price['4. close']) for price in loaded_json_prices)
    floated_price = prices[0]

    floated_SMAs_10 = SMA(np.asarray(prices)[::-1], timeperiod=10).tolist()[::-1]
    floated_SMA_10 = floated_SMAs_10.pop(0)
    
    if (floated_price < floated_SMA_10 * 0.95) : 
        return ('Be careful buying / lock in gains')
    elif (floated_price > floated_SMA_10 * 1.05) : 
        return ('Great time to buy')
    else : 
        return ('No direction yet') 

print(fear_gauge())