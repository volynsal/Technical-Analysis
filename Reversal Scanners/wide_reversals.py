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
others = ('BA')

def wide_reversals(ticker="SPY") : 
    data = yf.download(ticker, start="2020-01-01", end="2021-02-07")
    
    open = data['Open']
    high = data['High']
    low = data['Low']
    close = data['Close']

    current_date = datetime.today().strftime('%Y-%m-%d')

    two_crows = talib.CDL2CROWS(open, high, low, close)['2021-02-05']
    three_black_crows = talib.CDL3BLACKCROWS(open, high, low, close)['2021-02-05']
    three_inside = talib.CDL3INSIDE(open, high, low, close)['2021-02-05']
    three_line_strike = talib.CDL3LINESTRIKE(open, high, low, close)['2021-02-05']
    three_outside = talib.CDL3OUTSIDE(open, high, low, close)['2021-02-05']
    three_stars_in_south = talib.CDL3STARSINSOUTH(open, high, low, close)['2021-02-05']
    three_white_soldiers = talib.CDL3WHITESOLDIERS(open, high, low, close)['2021-02-05']
    abandoned_baby = talib.CDLABANDONEDBABY(open, high, low, close)['2021-02-05']
    advance_block = talib.CDLADVANCEBLOCK(open, high, low, close)['2021-02-05']
    belt_hold = talib.CDLBELTHOLD(open, high, low, close)['2021-02-05']
    breakaway = talib.CDLBREAKAWAY(open, high, low, close)['2021-02-05']
    closing_marubozu = talib.CDLCLOSINGMARUBOZU(open, high, low, close)['2021-02-05']
    concealing_baby_swallow = talib.CDLCONCEALBABYSWALL(open, high, low, close)['2021-02-05']
    talib.CDLCOUNTERATTACK(open, high, low, close)['2021-02-05']
    dark_cloud_cover = talib.CDLDARKCLOUDCOVER(open, high, low, close, penetration=0)['2021-02-05']
    doji = talib.CDLDOJI(open, high, low, close)['2021-02-05']
    doji_star = talib.CDLDOJISTAR(open, high, low, close)['2021-02-05']
    dragonfly_doji = talib.CDLDRAGONFLYDOJI(open, high, low, close)['2021-02-05']
    engulfing_candle = talib.CDLENGULFING(open, high, low, close)['2021-02-05']
    evening_doji_star = talib.CDLEVENINGDOJISTAR(open, high, low, close, penetration=0)['2021-02-05']
    evening_star = talib.CDLEVENINGSTAR(open, high, low, close, penetration=0)['2021-02-05']
    gaps = talib.CDLGAPSIDESIDEWHITE(open, high, low, close)['2021-02-05']
    gravestone_doji = talib.CDLGRAVESTONEDOJI(open, high, low, close)['2021-02-05']
    hammer = talib.CDLHAMMER(open, high, low, close)['2021-02-05']
    hanging_man = talib.CDLHANGINGMAN(open, high, low, close)['2021-02-05']
    harami = talib.CDLHARAMI(open, high, low, close)['2021-02-05']
    harami_cross = talib.CDLHARAMICROSS(open, high, low, close)['2021-02-05']
    high_wave = talib.CDLHIGHWAVE(open, high, low, close)['2021-02-05'][talib.CDLHIGHWAVE != 0]
    hikkake = talib.CDLHIKKAKE(open, high, low, close)['2021-02-05']
    hikkakemod = talib.CDLHIKKAKEMOD(open, high, low, close)['2021-02-05']
    homing_pigeon = talib.CDLHOMINGPIGEON(open, high, low, close)['2021-02-05']
    identical_three_crows = talib.CDLIDENTICAL3CROWS(open, high, low, close)['2021-02-05']
    in_neck = talib.CDLINNECK(open, high, low, close)['2021-02-05']
    inverted_hammer = talib.CDLINVERTEDHAMMER(open, high, low, close)['2021-02-05']
    kicking = talib.CDLKICKING(open, high, low, close)['2021-02-05']
    kicking_by_length = talib.CDLKICKINGBYLENGTH(open, high, low, close)['2021-02-05']
    ladder_bottom = talib.CDLLADDERBOTTOM(open, high, low, close)['2021-02-05']
    long_legged_doji = talib.CDLLONGLEGGEDDOJI(open, high, low, close)['2021-02-05']
    long_line = talib.CDLLONGLINE(open, high, low, close)['2021-02-05']
    marubozu = talib.CDLMARUBOZU(open, high, low, close)['2021-02-05']
    matching_low = talib.CDLMATCHINGLOW(open, high, low, close)['2021-02-05']
    mat_hold = talib.CDLMATHOLD(open, high, low, close, penetration=0)['2021-02-05']
    morning_doji_star = talib.CDLMORNINGDOJISTAR(open, high, low, close, penetration=0)['2021-02-05']
    morning_star = talib.CDLMORNINGSTAR(open, high, low, close, penetration=0)['2021-02-05']
    on_neck = talib.CDLONNECK(open, high, low, close)['2021-02-05']
    piercing = talib.CDLPIERCING(open, high, low, close)['2021-02-05']
    rickshawman = talib.CDLRICKSHAWMAN(open, high, low, close)['2021-02-05']
    rise_fall_3_methods = talib.CDLRISEFALL3METHODS(open, high, low, close)['2021-02-05']
    separating_lines = talib.CDLSEPARATINGLINES(open, high, low, close)['2021-02-05']
    shooting_star = talib.CDLSHOOTINGSTAR(open, high, low, close)['2021-02-05']
    shortline = talib.CDLSHORTLINE(open, high, low, close)['2021-02-05']
    spinning_top = talib.CDLSPINNINGTOP(open, high, low, close)['2021-02-05']
    stalled_pattern = talib.CDLSTALLEDPATTERN(open, high, low, close)['2021-02-05']
    stick_sandwich = talib.CDLSTICKSANDWICH(open, high, low, close)['2021-02-05']
    takuri = talib.CDLTAKURI(open, high, low, close)['2021-02-05']
    tasuki_gap = talib.CDLTASUKIGAP(open, high, low, close)['2021-02-05']
    thrusting = talib.CDLTHRUSTING(open, high, low, close)['2021-02-05']
    tristar = talib.CDLTRISTAR(open, high, low, close)['2021-02-05']
    unique_three_river = talib.CDLUNIQUE3RIVER(open, high, low, close)['2021-02-05']
    upside_gap_two_crows = talib.CDLUPSIDEGAP2CROWS(open, high, low, close)['2021-02-05']
    upside_downside_gap_three_methods = talib.CDLXSIDEGAP3METHODS(open, high, low, close)['2021-02-05']

    print(type(two_crows))


wide_reversals()

# print('Market Indices:')
# for ticker in market_indices : 
#     print(ticker)
#     print(wide_reversals(ticker))

# print('Tech Favorites:')
# for ticker in tech_favorites : 
#     print(ticker)
#     print(wide_reversals(ticker))

# print('Financial Favorites:')
# for ticker in financial_favorites : 
#     print(ticker)
#     print(wide_reversals(ticker))

# print('Retail Favorites:')
# for ticker in retail_favorites : 
#     print(ticker)
#     print(wide_reversals(ticker))

# print('Others:')
# for ticker in others : 
#     print(ticker)
#     print(wide_reversals(ticker))