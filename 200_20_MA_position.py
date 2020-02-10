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


def twohundred_twenty_ma (ticker) : 
    url_EMA_20_day = 'https://www.alphavantage.co/query?' + urllib.parse.urlencode({'time_period': '20', 'function':'EMA', 'symbol': tesla_ticker, 'interval':'daily', 'apikey': your_api_key, 'series_type': 'close'})
    url_EMA_200_day = 'https://www.alphavantage.co/query?' + urllib.parse.urlencode({'time_period': '200', 'function':'EMA', 'symbol': tesla_ticker, 'interval':'daily', 'apikey': your_api_key, 'series_type': 'close'})

    pre_json_EMA_20_day = urllib.request.urlopen(url_EMA_20_day, context = ctx).read().decode()
    pre_json_EMA_200_day = urllib.request.urlopen(url_EMA_200_day, context = ctx).read().decode()

    loaded_json_EMA_20_day = json.loads(pre_json_EMA_20_day)['Technical Analysis: EMA']
    loaded_json_EMA_200_day = json.loads(pre_json_EMA_200_day)['Technical Analysis: EMA']

    # Latest data point
    last_day = list(loaded_json_EMA_20_day.keys()).pop(0)
    EMA_20_day = float(loaded_json_EMA_20_day[last_day]['EMA'])
    EMA_200_day = float(loaded_json_EMA_200_day[last_day]['EMA'])

    if (EMA_20_day < EMA_200_day) : 
        return ('(' + str(datetime.now(tz)) + ') ' + ticker + ' oversold')
    elif (EMA_20_day > EMA_200_day) : 
        return ('(' + str(datetime.now(tz)) + ') ' + ticker + ' overbought')
    else : 
        return ('(' + str(datetime.now(tz)) + ') ' + ticker + ' stable') 


print(twohundred_twenty_ma(tesla_ticker))


