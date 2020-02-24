Codified 5 of 6 trading strategies listed here: https://www.johndeoresearch.com/mean-reversion-trading-strategies/.

This includes:

1. 90/30 MOVING AVERAGE (**90_30_MA_position.py**)
2. (LARRY CONNOR'S) RSI 2 (**2period_rsi_intraday.py** & **2period_rsi_swing.py**)
3. MA 200/MA 20 (**200_20_MA_position.py**)
4. PRICE CHANGE (**dramatic_price_change.py**)
6. LONG STOCKS AT MINUS TWO TIMES AVERAGE TRUE RANGE(ATR) (**atr_deviation.py**)

In his book *Introduction to ConnorsRSI*, Larry Connors explains how to calculate the ConnorsRSI. He incorporates this indicator in his own official options pullback strategy. Files **official_2period_rsi_swing.py** and **larry_connors_pullback.py** implement the indicator and pullback strategy respectively, using the rules from his book.

Please make sure the following dependencies are installed before running any script(s): 

```
brew install talib
pip3 install talib
pip3 install pytz
pip3 install numpy
```

My API Key is provided if you are interesting in cloning the repository and trying out some test calls, but please keep in mind the API is capped at 5 calls per minute. To get around this, I use the time library to pause execution while looping through a tuple of tickers. 

For any questions or concerns, please contact volynsal@gmail.com.