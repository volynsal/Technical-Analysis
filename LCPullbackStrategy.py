import urllib, urllib.parse, urllib.error, urllib.request
import ssl
import json
from datetime import datetime
from pytz import timezone
import time

from OC2period_rsi import two_period_rsi

tz = timezone('EST')

import pprint

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

robinhood_100_most_popular = ('ACB', 'F', 'GE', 'GPRO', 'FIT' 'AAPL', 'DIS', 'SNAP', 'MSFT', 'TSLA', 'AMZN', 'FB', 'GOOGL', 'NVDA', 'INTC', 'BABA', 'UBER', 'BAC', 'T', 'SBUX')
# vix = 'VIX'
tesla_ticker = 'AMZN'


def pullback_strategy_scan (ticker) : 
    url_ADX = 'https://www.alphavantage.co/query?' + urllib.parse.urlencode({'time_period': '10', 'function':'ADX', 'symbol': ticker, 'interval':'daily', 'apikey': 'IXV1N1AE5OTCW4KR', 'series_type': 'close'})
    pre_json_ADX = urllib.request.urlopen(url_ADX, context = ctx).read().decode()
    loaded_json_ADX = json.loads(pre_json_ADX)['Technical Analysis: ADX']

    # Latest ADX data point
    latest_date = list(loaded_json_ADX.keys()).pop(0)
    latest_ADX = float(loaded_json_ADX[latest_date]['ADX'])

    # Confirmation stock's lowest price is at least W% below the previous day's close
    url_prices = 'https://www.alphavantage.co/query?' + urllib.parse.urlencode({'outputsize': 'full', 'interval': '1min', 'function':'TIME_SERIES_INTRADAY', 'symbol': ticker, 'apikey': '2VNO5H70PQ6GSC98'})
    pre_json_prices = urllib.request.urlopen(url_prices, context = ctx).read().decode()
    loaded_json_prices = list(json.loads(pre_json_prices)['Time Series (1min)'].values())[:390]

    # lowest_price_today
    prices = [float(price['4. close']) for price in loaded_json_prices]
    lowest_price = min(prices)
    
    # close_day_before
    url_prices_daily = 'https://www.alphavantage.co/query?' + urllib.parse.urlencode({'outputsize': 'full', 'function':'TIME_SERIES_DAILY', 'symbol': ticker, 'apikey': '2VNO5H70PQ6GSC98'})
    pre_json_prices_daily = urllib.request.urlopen(url_prices_daily, context = ctx).read().decode()
    loaded_json_prices_daily = json.loads(pre_json_prices_daily)['Time Series (Daily)']

    second_to_last_day = list(loaded_json_prices_daily.keys()).pop(1)
    second_to_last_day_price = float(loaded_json_prices_daily[second_to_last_day]['4. close'])

    # checking if today's close is in bottom 25% of day's range
    latest_price = float(loaded_json_prices_daily[latest_date]['4. close'])

    percent_rank = 0 

    for index in range(1, len(prices) - 1) :
        price_change = (prices[index] - prices[index+1])/prices[index]
        if (latest_price > price_change) : percent_rank += 1

    percent_rank = percent_rank / 99 * 100

    # pp = pprint.PrettyPrinter(indent=4)
    # pp.pprint(loaded_json_prices_daily)

    # ConnorsRSI 
    official_rsi = two_period_rsi(ticker)

    if (latest_ADX > 30 and official_rsi <= 15 and second_to_last_day_price * 0.96 >= lowest_price and percent_rank <= 25) : 
        return 'BUY'
    else :
        return 'STABLE'


    # if (floated_SMA and floated_rsi and floated_price >= floated_SMA and floated_rsi >= 95) : 
    #     return ('(' + str(datetime.now(tz)) + ') ' + ticker + ' overbought')
    # elif (floated_SMA and floated_rsi and floated_price >= floated_SMA and floated_rsi <= 5) : 
    #     return ('(' + str(datetime.now(tz)) + ') ' + ticker + ' oversold')
    # else : 
    #     return ('(' + str(datetime.now(tz)) + ') ' + ticker + ' stable') 

# print(pullback_strategy_scan(tesla_ticker))

for ticker in robinhood_100_most_popular : 
    print(pullback_strategy_scan(ticker))
    time.sleep(60)