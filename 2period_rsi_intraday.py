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
aapl_ticker = 'NVDA'


def two_period_rsi (ticker) : 
    url_SMA = 'https://www.alphavantage.co/query?' + urllib.parse.urlencode({'time_period': '200', 'function':'SMA', 'symbol': aapl_ticker, 'interval':'1min', 'apikey': '2VNO5H70PQ6GSC98', 'series_type': 'close'})
    url_prices = 'https://www.alphavantage.co/query?' + urllib.parse.urlencode({'interval': '1min', 'outputsize': 'full', 'function':'TIME_SERIES_INTRADAY', 'symbol': ticker, 'apikey': '2VNO5H70PQ6GSC98'})   
    url_rsi = 'https://www.alphavantage.co/query?' + urllib.parse.urlencode({'interval':'1min', 'function': 'RSI', 'time_period':'2', 'series_type':'close', 'symbol': ticker, 'apikey': '2VNO5H70PQ6GSC98'})   

    pre_json_SMA = urllib.request.urlopen(url_SMA, context = ctx).read().decode()
    pre_json_prices = urllib.request.urlopen(url_prices, context = ctx).read().decode()
    pre_json_rsi = urllib.request.urlopen(url_rsi, context = ctx).read().decode()

    loaded_json_SMA = json.loads(pre_json_SMA)['Technical Analysis: SMA']
    loaded_json_prices = json.loads(pre_json_prices)['Time Series (1min)']
    loaded_json_rsi = json.loads(pre_json_rsi)['Technical Analysis: RSI']

    # Latest data point
    last_minute = list(loaded_json_prices.keys()).pop(0)

    floated_price = float(loaded_json_prices[last_minute]['4. close'])
    if (last_minute[:-3] in loaded_json_SMA) : floated_SMA = float(loaded_json_SMA[last_minute[:-3]]['SMA'])
    if (last_minute[:-3] in loaded_json_rsi) : floated_rsi = float(loaded_json_rsi[last_minute[:-3]]['RSI'])

    if (floated_SMA and floated_rsi and floated_price >= floated_SMA and floated_rsi <= 5) : 
        return ('(' + str(datetime.now(tz)) + ') ' + ticker + ' oversold')
    elif (floated_SMA and floated_rsi and floated_price <= floated_SMA and floated_rsi >= 95) : 
        return ('(' + str(datetime.now(tz)) + ') ' + ticker + ' overbought')
    else : 
        return ('(' + str(datetime.now(tz)) + ') ' + ticker + ' stable') 

print(two_period_rsi(aapl_ticker))
