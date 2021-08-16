import json
import yfinance as yf
from datetime import datetime
from pytz import timezone
import talib
import numpy as np

tz = timezone('EST')

market_indices = ('SPY', 'QQQ', 'DIA')
tech_favorites = ('PLTR', 'ROKU', 'ADSK', 'SPOT', 'TSLA', 'AMZN', 'LYFT', 'CRM', 'MSFT', 'AAPL', 'FB', 'NVDA', 'NFLX', 'JD', 'VZ', 'PFE', 'GOOGL', 'PYPL', 'BA', 'CSCO', 'MU', 'SQ', 'DIS')
financial_favorites = ('GS', 'BAC', 'JPM')
retail_favorites = ('LULU', 'NKE', 'TGT', 'WMT', 'COST')
others = ('BA', "GM", "GE", "NIO")

def wide_reversals(ticker="SPY") : 
    data = yf.download(ticker, start="2020-01-01", end=datetime.today().strftime('%Y-%m-%d'))   
    open = data['Open']
    high = data['High']
    low = data['Low']
    close = data['Close']

    current_date = datetime.today().strftime('%Y-%m-%d')

    two_crows = talib.CDL2CROWS(open, high, low, close)[current_date]
    three_black_crows = talib.CDL3BLACKCROWS(open, high, low, close)[current_date]
    three_inside = talib.CDL3INSIDE(open, high, low, close)[current_date]
    three_line_strike = talib.CDL3LINESTRIKE(open, high, low, close)[current_date]
    three_outside = talib.CDL3OUTSIDE(open, high, low, close)[current_date]
    three_stars_in_south = talib.CDL3STARSINSOUTH(open, high, low, close)[current_date]
    three_white_soldiers = talib.CDL3WHITESOLDIERS(open, high, low, close)[current_date]
    abandoned_baby = talib.CDLABANDONEDBABY(open, high, low, close)[current_date]
    advance_block = talib.CDLADVANCEBLOCK(open, high, low, close)[current_date]
    belt_hold = talib.CDLBELTHOLD(open, high, low, close)[current_date]
    breakaway = talib.CDLBREAKAWAY(open, high, low, close)[current_date]
    closing_marubozu = talib.CDLCLOSINGMARUBOZU(open, high, low, close)[current_date]
    concealing_baby_swallow = talib.CDLCONCEALBABYSWALL(open, high, low, close)[current_date]
    talib.CDLCOUNTERATTACK(open, high, low, close)[current_date]
    dark_cloud_cover = talib.CDLDARKCLOUDCOVER(open, high, low, close, penetration=0)[current_date]
    doji = talib.CDLDOJI(open, high, low, close)[current_date]
    doji_star = talib.CDLDOJISTAR(open, high, low, close)[current_date]
    dragonfly_doji = talib.CDLDRAGONFLYDOJI(open, high, low, close)[current_date]
    engulfing_candle = talib.CDLENGULFING(open, high, low, close)[current_date]
    evening_doji_star = talib.CDLEVENINGDOJISTAR(open, high, low, close, penetration=0)[current_date]
    evening_star = talib.CDLEVENINGSTAR(open, high, low, close, penetration=0)[current_date]
    gaps = talib.CDLGAPSIDESIDEWHITE(open, high, low, close)[current_date]
    gravestone_doji = talib.CDLGRAVESTONEDOJI(open, high, low, close)[current_date]
    hammer = talib.CDLHAMMER(open, high, low, close)[current_date]
    hanging_man = talib.CDLHANGINGMAN(open, high, low, close)[current_date]
    harami = talib.CDLHARAMI(open, high, low, close)[current_date]
    harami_cross = talib.CDLHARAMICROSS(open, high, low, close)[current_date]
    high_wave = talib.CDLHIGHWAVE(open, high, low, close)[current_date][talib.CDLHIGHWAVE != 0]
    hikkake = talib.CDLHIKKAKE(open, high, low, close)[current_date]
    hikkakemod = talib.CDLHIKKAKEMOD(open, high, low, close)[current_date]
    homing_pigeon = talib.CDLHOMINGPIGEON(open, high, low, close)[current_date]
    identical_three_crows = talib.CDLIDENTICAL3CROWS(open, high, low, close)[current_date]
    in_neck = talib.CDLINNECK(open, high, low, close)[current_date]
    inverted_hammer = talib.CDLINVERTEDHAMMER(open, high, low, close)[current_date]
    kicking = talib.CDLKICKING(open, high, low, close)[current_date]
    kicking_by_length = talib.CDLKICKINGBYLENGTH(open, high, low, close)[current_date]
    ladder_bottom = talib.CDLLADDERBOTTOM(open, high, low, close)[current_date]
    long_legged_doji = talib.CDLLONGLEGGEDDOJI(open, high, low, close)[current_date]
    long_line = talib.CDLLONGLINE(open, high, low, close)[current_date]
    marubozu = talib.CDLMARUBOZU(open, high, low, close)[current_date]
    matching_low = talib.CDLMATCHINGLOW(open, high, low, close)[current_date]
    mat_hold = talib.CDLMATHOLD(open, high, low, close, penetration=0)[current_date]
    morning_doji_star = talib.CDLMORNINGDOJISTAR(open, high, low, close, penetration=0)[current_date]
    morning_star = talib.CDLMORNINGSTAR(open, high, low, close, penetration=0)[current_date]
    on_neck = talib.CDLONNECK(open, high, low, close)[current_date]
    piercing = talib.CDLPIERCING(open, high, low, close)[current_date]
    rickshawman = talib.CDLRICKSHAWMAN(open, high, low, close)[current_date]
    rise_fall_3_methods = talib.CDLRISEFALL3METHODS(open, high, low, close)[current_date]
    separating_lines = talib.CDLSEPARATINGLINES(open, high, low, close)[current_date]
    shooting_star = talib.CDLSHOOTINGSTAR(open, high, low, close)[current_date]
    shortline = talib.CDLSHORTLINE(open, high, low, close)[current_date]
    spinning_top = talib.CDLSPINNINGTOP(open, high, low, close)[current_date]
    stalled_pattern = talib.CDLSTALLEDPATTERN(open, high, low, close)[current_date]
    stick_sandwich = talib.CDLSTICKSANDWICH(open, high, low, close)[current_date]
    takuri = talib.CDLTAKURI(open, high, low, close)[current_date]
    tasuki_gap = talib.CDLTASUKIGAP(open, high, low, close)[current_date]
    thrusting = talib.CDLTHRUSTING(open, high, low, close)[current_date]
    tristar = talib.CDLTRISTAR(open, high, low, close)[current_date]
    unique_three_river = talib.CDLUNIQUE3RIVER(open, high, low, close)[current_date]
    upside_gap_two_crows = talib.CDLUPSIDEGAP2CROWS(open, high, low, close)[current_date]
    upside_downside_gap_three_methods = talib.CDLXSIDEGAP3METHODS(open, high, low, close)[current_date]

    patterns = list(vars().keys())[7:]
    values = list(vars().values())[7:]

    for index in range(0,len(patterns)):
        if (values[index] != 0):
            print(patterns[index])
            print(values[index])


wide_reversals()

print('MARKET INDICES:')
for ticker in market_indices : 
    print(ticker)
    print(wide_reversals(ticker))

print('TECH FAVORITES:')
for ticker in tech_favorites : 
    print(ticker)
    print(wide_reversals(ticker))

print('FINANCIAL FAVORITES:')
for ticker in financial_favorites : 
    print(ticker)
    print(wide_reversals(ticker))

print('RETAIL FAVORITES:')
for ticker in retail_favorites : 
    print(ticker)
    print(wide_reversals(ticker))

print('OTHERS:')
for ticker in others : 
    print(ticker)
    print(wide_reversals(ticker))