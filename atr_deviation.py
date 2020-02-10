import urllib, urllib.parse, urllib.error, urllib.request
import ssl
import json
from datetime import datetime
from pytz import timezone

tz = timezone('EST')

# import pprint

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# robinhood_100_most_popular = ('ACB', 'F', 'GE', 'GPRO', 'FIT' 'AAPL', 'DIS', 'SNAP', 'MSFT', 'TSLA', 'AMZN', 'FB', 'GOOGL', 'NVDA', 'INTC', 'BABA', 'UBER', 'BAC', 'T', 'SBUX')
# vix = 'VIX'
tesla_ticker = 'TSLA'


def atr_deviation (ticker) : 
    url_atr = 'https://www.alphavantage.co/query?' + urllib.parse.urlencode({'time_period': '14', 'function':'ATR', 'symbol': tesla_ticker, 'interval':'1min', 'apikey': your_api_key})
    url_prices = 'https://www.alphavantage.co/query?' + urllib.parse.urlencode({'interval': '1min', 'outputsize': 'compact', 'function':'TIME_SERIES_INTRADAY', 'symbol': ticker, 'apikey': your_api_key})   

    pre_json_atr = urllib.request.urlopen(url_atr, context = ctx).read().decode()
    pre_json_prices = urllib.request.urlopen(url_prices, context = ctx).read().decode()

    loaded_json_atr = json.loads(pre_json_atr)['Technical Analysis: ATR']
    loaded_json_prices = json.loads(pre_json_prices)['Time Series (1min)']

    # Latest data point
    last_minute = list(loaded_json_prices.keys()).pop()
    first_minute = list(loaded_json_prices.keys()).pop(0)

    if (last_minute != first_minute) : 
        floated_price_last_minute = float(loaded_json_prices[last_minute]['4. close'])
        floated_price_first_minute = float(loaded_json_prices[first_minute]['4. close'])
        if (last_minute[:-3] in loaded_json_atr) : floated_atr = float(loaded_json_atr[last_minute[:-3]]['ATR'])

        if (floated_price_last_minute - floated_price_first_minute < -2 * floated_atr) : 
            return ('(' + str(datetime.now(tz)) + ') ' + ticker + ' oversold')

        elif (floated_price_last_minute - floated_price_first_minute < -2 * floated_atr) : 
            return ('(' + str(datetime.now(tz)) + ') ' + ticker + ' overbought')

        else : 
            return ('(' + str(datetime.now(tz)) + ') ' + ticker + ' stable')

print(atr_deviation(tesla_ticker))


