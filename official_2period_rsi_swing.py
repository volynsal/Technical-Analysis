import urllib, urllib.parse, urllib.error, urllib.request
import ssl
import json
from datetime import datetime
from pytz import timezone
from talib import RSI
import numpy as np

# import pandas, pandas_datareader.data as web
# import time
# import pprint

tz = timezone('EST')

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# The ConnorsRSI combines three composite components: price momentum, duration of up/down trend, and the relative magnitude of the price change

favorites = ('BA', 'AAPL', 'MSFT', 'FB', 'NVDA', 'NFLX')


def two_period_rsi (ticker, prices) : 
    component_one = price_change(ticker, prices)
    component_two = duration_of_trend(ticker, prices)
    component_three = relative_magnitude_price_change(ticker, prices)

    official_rsi = (component_one + component_two + component_three) / 3
    return float(official_rsi)

def price_change (ticker, prices):
    prices_reversed = list(reversed(prices))
    rsi = RSI(np.asarray(prices_reversed), timeperiod=3).tolist()
    rsi.reverse()

    return rsi.pop(0)

#Applying the RSI formula to the duration_of_trend as opposed to close values
def duration_of_trend (ticker, prices):            
    streak = 0
    streaks = []

    for index in reversed(range(0, len(prices) - 1)) : 
        if (prices[index] > prices[index+1]) :
            if (streak < 0) : streak = 0
            streak += 1
        elif (prices[index] < prices[index+1]) : 
            if (streak > 0) : streak = 0
            streak -= 1
        else :
            streak = 0

        streaks.append(float(streak))

    rsi = RSI(np.asarray(streaks), timeperiod=2).tolist()
    rsi.reverse()

    return rsi.pop(0)

def relative_magnitude_price_change (ticker, prices):    
    percent_rank = 0
    previous_day_price = prices.pop(0)

    previous_day_return = (previous_day_price - prices[0])/previous_day_price

    for index in range(0, len(prices) - 1) : 
        price_change = (prices[index] - prices[index+1])/prices[index]
        if (previous_day_return > price_change) : percent_rank += 1

    return percent_rank / 98 * 100
    
# To execute the script independently, without larry_connors_pullback.py, please run the code below:

# print('(' + str(datetime.now(tz))[:10] + ') ')
# for ticker in favorites : 
#     url_prices = 'https://www.alphavantage.co/query?' + urllib.parse.urlencode({'interval': 'daily', 'outputsize': 'compact', 'function':'TIME_SERIES_DAILY', 'symbol': ticker, 'apikey': 'N69PE58L8L68YV07'})   
#     pre_json_prices = urllib.request.urlopen(url_prices, context = ctx).read().decode()
#     loaded_json_prices = json.loads(pre_json_prices)['Time Series (Daily)'].values()

#     prices = list(float(price['4. close']) for price in loaded_json_prices)
#     print(ticker + ': ' + str(two_period_rsi(ticker, prices)))

