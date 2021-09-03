import json
import yfinance as yf
from datetime import datetime
from datetime import timedelta
from pytz import timezone
import talib
import numpy as np

tz = timezone('EST')

market_indices = ('SPY', 'QQQ', 'DIA')
tech_favorites = ('PLTR', 'ROKU', 'ADSK', 'SPOT', 'TSLA', 'AMZN', 'LYFT', 'CRM', 'MSFT', 'AAPL', 'FB', 'NVDA', 'NFLX', 'JD', 'VZ', 'PFE', 'GOOGL', 'PYPL', 'BA', 'CSCO', 'MU', 'SQ', 'DIS')
financial_favorites = ('GS', 'BAC', 'JPM')
retail_favorites = ('LULU', 'NKE', 'TGT', 'WMT', 'COST')
others = ('BA', "GM", "GE", "NIO")

# For each ticker, if the value is equal to 100 or -100 this signifies the signal/technical trading pattern has been triggered, and to investigate the chart of the security even further

def built_in_scanners(ticker="SPY") : 
    data = yf.download(ticker, start="2020-01-01", end=datetime.today().strftime('%Y-%m-%d'))   
    open = data['Open']
    high = data['High']
    low = data['Low']
    close = data['Close']

    # The library's functions runs on yesterday's date, so subtract 1 from today's date.

    current_date = datetime.today() - timedelta(days = 1)
    current_date_formatted = current_date.strftime('%Y-%m-%d')

    two_crows = talib.CDL2CROWS(open, high, low, close)[current_date_formatted]
    three_black_crows = talib.CDL3BLACKCROWS(open, high, low, close)[current_date_formatted]
    three_inside = talib.CDL3INSIDE(open, high, low, close)[current_date_formatted]
    three_line_strike = talib.CDL3LINESTRIKE(open, high, low, close)[current_date_formatted]
    three_outside = talib.CDL3OUTSIDE(open, high, low, close)[current_date_formatted]
    three_stars_in_south = talib.CDL3STARSINSOUTH(open, high, low, close)[current_date_formatted]
    three_white_soldiers = talib.CDL3WHITESOLDIERS(open, high, low, close)[current_date_formatted]
    abandoned_baby = talib.CDLABANDONEDBABY(open, high, low, close)[current_date_formatted]
    advance_block = talib.CDLADVANCEBLOCK(open, high, low, close)[current_date_formatted]
    belt_hold = talib.CDLBELTHOLD(open, high, low, close)[current_date_formatted]
    breakaway = talib.CDLBREAKAWAY(open, high, low, close)[current_date_formatted]
    closing_marubozu = talib.CDLCLOSINGMARUBOZU(open, high, low, close)[current_date_formatted]
    concealing_baby_swallow = talib.CDLCONCEALBABYSWALL(open, high, low, close)[current_date_formatted]
    talib.CDLCOUNTERATTACK(open, high, low, close)[current_date_formatted]
    dark_cloud_cover = talib.CDLDARKCLOUDCOVER(open, high, low, close, penetration=0)[current_date_formatted]
    doji = talib.CDLDOJI(open, high, low, close)[current_date_formatted]
    doji_star = talib.CDLDOJISTAR(open, high, low, close)[current_date_formatted]
    dragonfly_doji = talib.CDLDRAGONFLYDOJI(open, high, low, close)[current_date_formatted]
    engulfing_candle = talib.CDLENGULFING(open, high, low, close)[current_date_formatted]
    evening_doji_star = talib.CDLEVENINGDOJISTAR(open, high, low, close, penetration=0)[current_date_formatted]
    evening_star = talib.CDLEVENINGSTAR(open, high, low, close, penetration=0)[current_date_formatted]
    gaps = talib.CDLGAPSIDESIDEWHITE(open, high, low, close)[current_date_formatted]
    gravestone_doji = talib.CDLGRAVESTONEDOJI(open, high, low, close)[current_date_formatted]
    hammer = talib.CDLHAMMER(open, high, low, close)[current_date_formatted]
    hanging_man = talib.CDLHANGINGMAN(open, high, low, close)[current_date_formatted]
    harami = talib.CDLHARAMI(open, high, low, close)[current_date_formatted]
    harami_cross = talib.CDLHARAMICROSS(open, high, low, close)[current_date_formatted]
    high_wave = talib.CDLHIGHWAVE(open, high, low, close)[current_date_formatted][talib.CDLHIGHWAVE != 0]
    hikkake = talib.CDLHIKKAKE(open, high, low, close)[current_date_formatted]
    hikkakemod = talib.CDLHIKKAKEMOD(open, high, low, close)[current_date_formatted]
    homing_pigeon = talib.CDLHOMINGPIGEON(open, high, low, close)[current_date_formatted]
    identical_three_crows = talib.CDLIDENTICAL3CROWS(open, high, low, close)[current_date_formatted]
    in_neck = talib.CDLINNECK(open, high, low, close)[current_date_formatted]
    inverted_hammer = talib.CDLINVERTEDHAMMER(open, high, low, close)[current_date_formatted]
    kicking = talib.CDLKICKING(open, high, low, close)[current_date_formatted]
    kicking_by_length = talib.CDLKICKINGBYLENGTH(open, high, low, close)[current_date_formatted]
    ladder_bottom = talib.CDLLADDERBOTTOM(open, high, low, close)[current_date_formatted]
    long_legged_doji = talib.CDLLONGLEGGEDDOJI(open, high, low, close)[current_date_formatted]
    long_line = talib.CDLLONGLINE(open, high, low, close)[current_date_formatted]
    marubozu = talib.CDLMARUBOZU(open, high, low, close)[current_date_formatted]
    matching_low = talib.CDLMATCHINGLOW(open, high, low, close)[current_date_formatted]
    mat_hold = talib.CDLMATHOLD(open, high, low, close, penetration=0)[current_date_formatted]
    morning_doji_star = talib.CDLMORNINGDOJISTAR(open, high, low, close, penetration=0)[current_date_formatted]
    morning_star = talib.CDLMORNINGSTAR(open, high, low, close, penetration=0)[current_date_formatted]
    on_neck = talib.CDLONNECK(open, high, low, close)[current_date_formatted]
    piercing = talib.CDLPIERCING(open, high, low, close)[current_date_formatted]
    rickshawman = talib.CDLRICKSHAWMAN(open, high, low, close)[current_date_formatted]
    rise_fall_3_methods = talib.CDLRISEFALL3METHODS(open, high, low, close)[current_date_formatted]
    separating_lines = talib.CDLSEPARATINGLINES(open, high, low, close)[current_date_formatted]
    shooting_star = talib.CDLSHOOTINGSTAR(open, high, low, close)[current_date_formatted]
    shortline = talib.CDLSHORTLINE(open, high, low, close)[current_date_formatted]
    spinning_top = talib.CDLSPINNINGTOP(open, high, low, close)[current_date_formatted]
    stalled_pattern = talib.CDLSTALLEDPATTERN(open, high, low, close)[current_date_formatted]
    stick_sandwich = talib.CDLSTICKSANDWICH(open, high, low, close)[current_date_formatted]
    takuri = talib.CDLTAKURI(open, high, low, close)[current_date_formatted]
    tasuki_gap = talib.CDLTASUKIGAP(open, high, low, close)[current_date_formatted]
    thrusting = talib.CDLTHRUSTING(open, high, low, close)[current_date_formatted]
    tristar = talib.CDLTRISTAR(open, high, low, close)[current_date_formatted]
    unique_three_river = talib.CDLUNIQUE3RIVER(open, high, low, close)[current_date_formatted]
    upside_gap_two_crows = talib.CDLUPSIDEGAP2CROWS(open, high, low, close)[current_date_formatted]
    upside_downside_gap_three_methods = talib.CDLXSIDEGAP3METHODS(open, high, low, close)[current_date_formatted]

    patterns = list(vars().keys())[7:]
    values = list(vars().values())[7:]

    for index in range(0,len(patterns)):
        if (values[index] != 0):
            print(patterns[index])
            print(values[index])

print('MARKET INDICES:')
for ticker in market_indices : 
    print(ticker)
    print(built_in_scanners(ticker))

print('TECH FAVORITES:')
for ticker in tech_favorites : 
    print(ticker)
    print(built_in_scanners(ticker))

print('FINANCIAL FAVORITES:')
for ticker in financial_favorites : 
    print(ticker)
    print(built_in_scanners(ticker))

print('RETAIL FAVORITES:')
for ticker in retail_favorites : 
    print(ticker)
    print(built_in_scanners(ticker))

print('OTHERS:')
for ticker in others : 
    print(ticker)
    print(built_in_scanners(ticker))