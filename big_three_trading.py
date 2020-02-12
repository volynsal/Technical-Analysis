import urllib, urllib.parse, urllib.error, urllib.request
import ssl
import jsonds
from datetime import datetime
from pytz import timezone

from threading import Timer

tz = timezone('EST')

# import pprint

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

robinhood_100_most_popular = ('ACB', 'F', 'GE', 'GPRO', 'FIT' 'AAPL', 'DIS', 'SNAP', 'MSFT', 'TSLA', 'AMZN', 'FB', 'GOOGL', 'NVDA', 'INTC', 'BABA', 'UBER', 'BAC', 'T', 'SBUX')
# vix = 'VIX'
# aapl_ticker = 'SNAP'


def big_three_trading (ticker) : 
    url_prices = 'https://www.alphavantage.co/query?' + urllib.parse.urlencode({'interval': 'daily', 'outputsize': 'full', 'function':'TIME_SERIES_INTRADAY', 'symbol': ticker, 'apikey': '2VNO5H70PQ6GSC98'})   
    url_SMA_twenty = 'https://www.alphavantage.co/query?' + urllib.parse.urlencode({'time_period': '20', 'function':'SMA', 'symbol': aapl_ticker, 'interval':'daily', 'apikey': '2VNO5H70PQ6GSC98', 'series_type': 'close'})
    url_SMA_forty = 'https://www.alphavantage.co/query?' + urllib.parse.urlencode({'time_period': '40', 'function':'SMA', 'symbol': aapl_ticker, 'interval':'daily', 'apikey': '2VNO5H70PQ6GSC98', 'series_type': 'close'})
    url_SMA_eighty = 'https://www.alphavantage.co/query?' + urllib.parse.urlencode({'time_period': '80', 'function':'SMA', 'symbol': aapl_ticker, 'interval':'daily', 'apikey': '2VNO5H70PQ6GSC98', 'series_type': 'close'})

    pre_json_prices = urllib.request.urlopen(url_prices, context = ctx).read().decode()
    pre_json_SMA_twenty = urllib.request.urlopen(url_SMA_twenty, context = ctx).read().decode()
    pre_json_SMA_forty = urllib.request.urlopen(url_SMA_forty, context = ctx).read().decode()
    pre_json_SMA_eighty = urllib.request.urlopen(url_SMA_eighty, context = ctx).read().decode()
    
    loaded_json_prices = json.loads(pre_json_prices)['Time Series (daily)']
    loaded_json_SMA_twenty = json.loads(pre_json_SMA)['Technical Analysis: SMA']
    loaded_json_SMA_forty = json.loads(pre_json_SMA)['Technical Analysis: SMA']
    loaded_json_SMA_eighty = json.loads(pre_json_SMA)['Technical Analysis: SMA']

    # Latest data point
    last_day = list(loaded_json_prices.keys()).pop(0)

    floated_price = float(loaded_json_prices[last_minute]['4. close'])
    if (last_minute[:-3] in loaded_json_SMsA) : floated_SMA = float(loaded_json_SMA[last_minute[:-3]]['SMA'])
    if (last_minute[:-3] in loaded_json_rsi) : floated_rsi = float(loaded_json_rsi[last_minute[:-3]]['RSI'])

    if (floated_SMA and floated_rsi and floated_price >= floated_SMA and floated_rsi <= 5) : 
        return ('(' + str(datetime.now(tz)) + ') ' + ticker + ' overbought')
    elif (floated_SMA and floated_rsi and floated_price >= floated_SMA and floated_rsi >= 95) : 
        return ('(' + str(datetime.now(tz)) + ') ' + ticker + ' oversold')
    else : 
        return ('(' + str(datetime.now(tz)) + ') ' + ticker + ' stable') 

print(two_period_rsi(aapl_ticker))


