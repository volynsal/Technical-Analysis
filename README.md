Codified 5 of 6 trading strategies listed here: https://www.johndeoresearch.com/mean-reversion-trading-strategies/.

This includes:

1. 90/30 MOVING AVERAGE (**90_30_MA_position.py**)
2. (LARRY CONNOR'S) RSI 2 (**2period_rsi_intraday.py** & **2period_rsi_swing.py**)
3. MA 200/MA 20 (**200_20_MA_position.py**)
4. PRICE CHANGE (**dramatic_price_change.py**)
6. LONG STOCKS AT MINUS TWO TIMES AVERAGE TRUE RANGE(ATR) (**atr_deviation.py**)

In his book *Introduction to ConnorsRSI*, Larry Connors uses slightly different rules to calculate the ConnorsRSI. He incorporates this indicator in his official options pullback strategy. Files **official_2period_rsi_swing.py** and **pullback.py** implement the indicator and strategy respectively. Meanwhile, the technical trading library TA-Lib holds dozens of superb trading scanners, and **built_in_scanners.py** implements all of them for a number of example tickers. 

Please make sure the following dependencies are installed before running any script(s): 

```
brew install ta-lib
pip3 install -r requirements.txt
```

My API Key is provided if you are interesting in cloning the repository and trying out some test calls, but please keep in mind the API is capped at 5 calls per minute. To get around this, I use the time library to pause execution while looping through tickers.

For any questions or concerns, please contact volynsal@gmail.com.