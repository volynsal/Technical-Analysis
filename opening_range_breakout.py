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
aapl_ticker = 'SNAP'


def two_period_rsi (ticker) : 
    url_prices = 'https://www.alphavantage.co/query?' + urllib.parse.urlencode({'interval': '15min', 'outputsize': 'full', 'function':'TIME_SERIES_INTRADAY', 'symbol': ticker, 'apikey': '2VNO5H70PQ6GSC98'})   

    pre_json_prices = urllib.request.urlopen(url_prices, context = ctx).read().decode()

    loaded_json_prices = json.loads(pre_json_prices)['Time Series (15min)']

    # Latest data point
    latest_fifteen_minute = list(loaded_json_prices.keys()).pop(0)
    first_fifteen_minute = list(loaded_json_prices.keys()).pop()

    high = float(loaded_json_prices['2. high'])
    low = float(loaded_json_prices['3. low'])

    floated_price = float(loaded_json_prices[last_minute]['4. close'])
    if (last_minute[:-3] in loaded_json_SMA) : floated_SMA = float(loaded_json_SMA[last_minute[:-3]]['SMA'])
    if (last_minute[:-3] in loaded_json_rsi) : floated_rsi = float(loaded_json_rsi[last_minute[:-3]]['RSI'])

    if (floated_SMA and floated_rsi and floated_price >= floated_SMA and floated_rsi >= 95) : 
        return ('(' + str(datetime.now(tz)) + ') ' + ticker + ' overbought')
    elif (floated_SMA and floated_rsi and floated_price >= floated_SMA and floated_rsi <= 5) : 
        return ('(' + str(datetime.now(tz)) + ') ' + ticker + ' oversold')
    else : 
        return ('(' + str(datetime.now(tz)) + ') ' + ticker + ' stable') 

print(two_period_rsi(aapl_ticker))


