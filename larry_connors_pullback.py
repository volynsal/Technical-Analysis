import urllib, urllib.parse, urllib.error, urllib.request
import ssl
import json
from datetime import datetime
from pytz import timezone
import time
import numpy as np
from talib import ADX
# import pprint

from official_2period_rsi_swing import two_period_rsi

tz = timezone('EST')

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

favorites = ('CRM', 'MSFT', 'AAPL', 'FB', 'NVDA', 'NFLX', 'TGT', 'COST', 'JD', 'VZ', 'PFE', 'GOOGL', 'PYPL', 'BA', 'CSCO', 'MU', 'NKE', 'SQ', 'DIS')

def pullback_strategy_scan (ticker="AAPL") : 
    url_prices = 'https://www.alphavantage.co/query?' + urllib.parse.urlencode({'interval': 'daily', 'outputsize': 'compact', 'function':'TIME_SERIES_DAILY', 'symbol': ticker, 'apikey': 'YSPOO5FANVL57LQ2'})   
    pre_json_prices = urllib.request.urlopen(url_prices, context = ctx).read().decode()
    loaded_json_prices = json.loads(pre_json_prices)['Time Series (Daily)'].values()
        
    prices = list(float(price['4. close']) for price in loaded_json_prices)

    # 1. Calculate ADX
    prices_close = list(reversed(prices))
    prices_high = list(reversed(list(float(price['2. high']) for price in loaded_json_prices)))
    prices_low = list(reversed(list(float(price['3. low']) for price in loaded_json_prices)))
    
    latest_ADX = ADX(np.asarray(prices_high), np.asarray(prices_low), np.asarray(prices_close), timeperiod=10).tolist()
    latest_ADX.reverse()

    # 2. Confirm stock's lowest price is at least W% below the previous day's close
    url_prices_intraday = 'https://www.alphavantage.co/query?' + urllib.parse.urlencode({'outputsize': 'full', 'interval': '1min', 'function':'TIME_SERIES_INTRADAY', 'symbol': ticker, 'apikey': 'N69PE58L8L68YV07'})
    pre_json_prices_intraday = urllib.request.urlopen(url_prices_intraday, context = ctx).read().decode()
    loaded_json_prices_intraday = list(json.loads(pre_json_prices_intraday)['Time Series (1min)'].values())[:390]

    # lowest_price_today
    prices_intraday = [float(price['4. close']) for price in loaded_json_prices_intraday]
    lowest_price = min(prices_intraday)
    
    # close_day_before
    second_to_last_day_price = prices[1]

    # 3. Check if today's close is in bottom 25% of day's range
    latest_price = prices[0]
    percent_rank = 0 

    for index in range(1, len(prices_intraday)) :
        if (latest_price > prices_intraday[index]) : percent_rank += 1

    percent_rank = percent_rank / 390 * 100
    
    # 4. ConnorsRSI calculation
    official_rsi = two_period_rsi(ticker, prices)

    if (latest_ADX.pop(0) > 30 and official_rsi <= 15 and second_to_last_day_price * 0.96 >= lowest_price and percent_rank <= 25) : 
        return ('(' + str(datetime.now(tz))[:10] + ') ' + ticker + ': OVERSOLD')
    else :
        return ('(' + str(datetime.now(tz))[:10] + ') ' + ticker + ': STABLE')

for ticker in favorites : 
        print(pullback_strategy_scan(ticker))
        time.sleep(61) 

