import urllib, urllib.parse, urllib.error, urllib.request
import ssl
import json
from datetime import datetime
from pytz import timezone
import statistics

tz = timezone('EST')

import pprint

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url_SPY_Daily = 'https://www.alphavantage.co/query?' + urllib.parse.urlencode({'function':'TIME_SERIES_DAILY', 'symbol': 'SPY', 'apikey': '2VNO5H70PQ6GSC98'})

pre_json_SPY_Daily = urllib.request.urlopen(url_SPY_Daily, context = ctx).read().decode()

loaded_json_SPY_Daily = json.loads(pre_json_SPY_Daily)['Time Series (Daily)']
loaded_list_SPY_Daily = list(loaded_json_SPY_Daily)

minimum_gap = 10
gaps = []
count = 0

for key, value in loaded_json_SPY_Daily.items(): 
    if (key != loaded_list_SPY_Daily[-1]) :
        prev_day = loaded_list_SPY_Daily[loaded_list_SPY_Daily.index(key)+1]

        gap = (float(value['1. open']) - float(loaded_json_SPY_Daily[prev_day]['4. close'])) / float(loaded_json_SPY_Daily[prev_day]['4. close']) * 100
        intraday_change = (float(value['4. close']) - float(value['1. open'])) / float(value['1. open']) * 100

        if (intraday_change >= 0.5 and gap > 0.58):
            if (minimum_gap > gap): minimum_gap = gap
            gaps.append(gap)
            count += 1

# print(minimum_gap)
# print(statistics.mean(gaps))
# print(statistics.median(gaps))
# print(len(gaps))

print(len(gaps))