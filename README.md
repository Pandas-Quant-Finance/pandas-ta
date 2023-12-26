# Pandas TA Quant

Basically a wrapper around [tulipy][e1] indicators. The library fully builds on top of pandas and pandas_df_commons, 
therefore allows to deal with MultiIndex easily. For example, it is very convenient to have bars 
(open, high, low, close data) of multiple assets as a MultiIndex in either rows or columns or both.

| Date                |   ('spy', 'Open') |   ('spy', 'High') |   ('spy', 'Low') |   ('spy', 'Close') |   ('spy', 'Volume') |   ('spy', 'Dividends') |   ('spy', 'Stock Splits') |   ('gld', 'Open') |   ('gld', 'High') |   ('gld', 'Low') |   ('gld', 'Close') |   ('gld', 'Volume') |   ('gld', 'Dividends') |   ('gld', 'Stock Splits') |
|:--------------------|------------------:|------------------:|-----------------:|-------------------:|--------------------:|-----------------------:|--------------------------:|------------------:|------------------:|-----------------:|-------------------:|--------------------:|-----------------------:|--------------------------:|
| 2020-02-07 00:00:00 |            332.82 |            333.99 |           331.6  |             332.2  |         6.41394e+07 |                      0 |                         0 |            147.83 |            148.18 |           147.34 |             147.79 |         6.3793e+06  |                      0 |                         0 |
| 2020-02-10 00:00:00 |            331.23 |            334.75 |           331.19 |             334.68 |         4.207e+07   |                      0 |                         0 |            148.21 |            148.45 |           147.91 |             148.17 |         5.7936e+06  |                      0 |                         0 |

## Usage

You can either import an already patched pandas object or you can patch the extension by yourself. 
So the shorthand

```python
from pandas_ta.patched import pd
```

is equivalent to

```python
import pandas_ta as pta
pta.monkey_patch_dataframe("ta")
```
   
After import and patching you can use the indicators directly from your DataFrame:

```python
from pandas_ta.patched import pd
import yfinance as yf

df = yf.Ticker("TSLA").history('max')['2020-01-1':]
ax = df["Close"].plot()
df.ta.ema(20).plot(ax=ax)
```

As already mentioned it is fully compatible with MultilevelIndex, so you can just 
call the indicator on the whole DataFrame.

```python
from pandas_ta.patched import pd
import yfinance as yf

df = pd.concat(
    [yf.Ticker("TSLA").history('max')['2020-01-1':], yf.Ticker("MSFT").history('max')['2020-01-1':]],
    axis=1,
    keys=["TSLA", "MSFT"]
)


df.ta.natr(20).head()
```

| Date                      |   ('TSLA', "natr('High', 'Low', 'Close', 20)") |   ('MSFT', "natr('High', 'Low', 'Close', 20)") |
|:--------------------------|-----------------------------------------------:|-----------------------------------------------:|
| 2020-01-30 00:00:00-05:00 |                                        4.13781 |                                        1.56065 |
| 2020-01-31 00:00:00-05:00 |                                        4.02935 |                                        1.59882 |
| 2020-02-03 00:00:00-05:00 |                                        4.06173 |                                        1.60517 |
| 2020-02-04 00:00:00-05:00 |                                        4.45821 |                                        1.65009 |
| 2020-02-05 00:00:00-05:00 |                                        6.35866 |                                        1.73042 |

## List of indicators:
  * ad
  * adosc
  * adx
  * adxr
  * ao
  * aroon
  * aroonosc
  * atr
  * avgprice
  * bop
  * cci
  * cvi
  * di
  * dm
  * dx
  * emv
  * fisher
  * kvo
  * marketfi
  * mass
  * medprice
  * mfi
  * natr
  * nvi
  * obv
  * psar
  * pvi
  * qstick
  * stoch
  * tr
  * typprice
  * ultosc
  * vwma
  * wad
  * wcprice
  * willr
  * apo
  * bbands
  * cmo
  * decay
  * dema
  * dpo
  * edecay
  * ema
  * fosc
  * hma
  * kama
  * lag
  * linreg
  * linregintercept
  * linregslope
  * macd
  * max
  * md
  * min
  * mom
  * msw
  * ppo
  * roc
  * rocr
  * rsi
  * sma
  * stddev
  * stderr
  * stochrsi
  * sum
  * tema
  * trima
  * trix
  * tsf
  * var
  * vhf
  * vidya
  * volatility
  * vosc
  * wilders
  * wma
  * zlema
  * crossany
  * crossover
  * decimal_year
  * sinusoidal_week_day
  * sinusoidal_week
  * dist_opex
  * hurst_volatility
  * gkyz_volatility
  * cc_volatility
  * zscore
  * up_down_volatility_ratio
  * repeat
  * apply
  * resample

  
[e1]: https://github.com/cirla/tulipy

