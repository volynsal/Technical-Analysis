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


def dramatic_price_change (ticker) : 
    url_prices = 'https://www.alphavantage.co/query?' + urllib.parse.urlencode({'interval': 'daily', 'outputsize': 'compact', 'function':'TIME_SERIES_DAILY', 'symbol': ticker, 'apikey': your_api_key})   
    pre_json_prices = urllib.request.urlopen(url_prices, context = ctx).read().decode()
    loaded_json_prices = json.loads(pre_json_prices)['Time Series (Daily)']

    # pp = pprint.PrettyPrinter(indent=4)
    # pp.pprint(loaded_json_prices)

    last_30_days = list(loaded_json_prices.keys())[2:33]
    price_changes = []

    for index in range(0,len(last_30_days)) :
        floated_price_current = float(loaded_json_prices[last_30_days[index]]['4. close'])
        floated_price_day_before = float(loaded_json_prices[last_30_days[index-1]]['4. close'])

        price_changes.append(floated_price_current-floated_price_day_before)

    average_30_day_price_change = sum(price_changes) / 30

    # Latest data point
    last_day = list(loaded_json_prices.keys()).pop(0)
    second_to_last_day = list(loaded_json_prices.keys()).pop(0)

    last_price_change = float(loaded_json_prices[last_day]['4. close']) - float(loaded_json_prices[second_to_last_day]['4. close'])

    if (last_price_change > average_30_day_price_change * 1.1) : 
        return ('(' + str(datetime.now(tz)) + ') ' + ticker + ' overbought')
    elif (last_price_change < average_30_day_price_change * 1.1) : 
        return ('(' + str(datetime.now(tz)) + ') ' + ticker + ' oversold')
    else : 
        return ('(' + str(datetime.now(tz)) + ') ' + ticker + ' stable') 

print(dramatic_price_change(tesla_ticker))


