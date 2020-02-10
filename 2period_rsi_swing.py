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


def two_period_rsi (ticker) : 
    url_EMA = 'https://www.alphavantage.co/query?' + urllib.parse.urlencode({'time_period': '200', 'function':'EMA', 'symbol': tesla_ticker, 'interval':'daily', 'apikey': '2VNO5H70PQ6GSC98', 'series_type': 'close'})
    url_prices = 'https://www.alphavantage.co/query?' + urllib.parse.urlencode({'interval': 'daily', 'outputsize': 'compact', 'function':'TIME_SERIES_DAILY', 'symbol': ticker, 'apikey': '2VNO5H70PQ6GSC98'})   
    url_rsi = 'https://www.alphavantage.co/query?' + urllib.parse.urlencode({'interval':'daily', 'function': 'RSI', 'time_period':'2', 'series_type':'close', 'symbol': ticker, 'apikey': '2VNO5H70PQ6GSC98'})   

    pre_json_EMA = urllib.request.urlopen(url_EMA, context = ctx).read().decode()
    pre_json_prices = urllib.request.urlopen(url_prices, context = ctx).read().decode()
    pre_json_rsi = urllib.request.urlopen(url_rsi, context = ctx).read().decode()

    loaded_json_EMA = json.loads(pre_json_EMA)['Technical Analysis: EMA']
    loaded_json_prices = json.loads(pre_json_prices)['Time Series (Daily)']
    loaded_json_rsi = json.loads(pre_json_rsi)['Technical Analysis: RSI']

    # pp = pprint.PrettyPrinter(indent=4)
    # pp.pprint(loaded_json_prices)

    # Latest data point
    last_day = list(loaded_json_prices.keys()).pop(0)

    floated_price = float(loaded_json_prices[last_day]['4. close'])
    floated_EMA = float(loaded_json_EMA[last_day]['EMA'])
    floated_rsi = float(loaded_json_rsi[last_day]['RSI'])

    if (floated_EMA and floated_rsi and floated_price >= floated_EMA and floated_rsi >= 95) : 
        return ('(' + str(datetime.now(tz)) + ') ' + ticker + ' overbought')
    elif (floated_EMA and floated_rsi and floated_price >= floated_EMA and floated_rsi <= 5) : 
        return ('(' + str(datetime.now(tz)) + ') ' + ticker + ' oversold')
    else : 
        return ('(' + str(datetime.now(tz)) + ') ' + ticker + ' stable') 

print(two_period_rsi(tesla_ticker))


