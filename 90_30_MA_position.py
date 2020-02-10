import urllib, urllib.parse, urllib.error, urllib.request
import ssl
import json
from datetime import datetime
from pytz import timezone

tz = timezone('EST')

import pprint

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# robinhood_100_most_popular = ('ACB', 'F', 'GE', 'GPRO', 'FIT' 'AAPL', 'DIS', 'SNAP', 'MSFT', 'TSLA', 'AMZN', 'FB', 'GOOGL', 'NVDA', 'INTC', 'BABA', 'UBER', 'BAC', 'T', 'SBUX')
tesla_ticker = 'TSLA'


def ninety_thirty_ma (ticker) : 
    url_EMA_30_day = 'https://www.alphavantage.co/query?' + urllib.parse.urlencode({'time_period': '30', 'function':'EMA', 'symbol': tesla_ticker, 'interval':'daily', 'apikey': your_api_key, 'series_type': 'close'})
    url_EMA_90_day = 'https://www.alphavantage.co/query?' + urllib.parse.urlencode({'time_period': '90', 'function':'EMA', 'symbol': tesla_ticker, 'interval':'daily', 'apikey': your_api_key, 'series_type': 'close'})

    pre_json_EMA_30_day = urllib.request.urlopen(url_EMA_30_day, context = ctx).read().decode()
    pre_json_EMA_90_day = urllib.request.urlopen(url_EMA_90_day, context = ctx).read().decode()

    loaded_json_EMA_30_day = json.loads(pre_json_EMA_30_day)['Technical Analysis: EMA']
    loaded_json_EMA_90_day = json.loads(pre_json_EMA_90_day)['Technical Analysis: EMA']

    # Latest data point
    last_day = list(loaded_json_EMA_30_day.keys()).pop(0)
    EMA_30_day = float(loaded_json_EMA_30_day[last_day]['EMA'])
    EMA_90_day = float(loaded_json_EMA_90_day[last_day]['EMA'])

    if (EMA_30_day < EMA_90_day) : 
        return ('(' + str(datetime.now(tz)) + ') ' + ticker + ' oversold')
    elif (EMA_30_day > EMA_90_day) : 
        return ('(' + str(datetime.now(tz)) + ') ' + ticker + ' overbought')
    else : 
        return ('(' + str(datetime.now(tz)) + ') ' + ticker + ' stable') 


print(ninety_thirty_ma(tesla_ticker))


