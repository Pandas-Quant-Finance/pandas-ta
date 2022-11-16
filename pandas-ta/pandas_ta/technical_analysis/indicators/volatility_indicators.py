from __future__ import annotations

import numpy as np
import pandas as pd

from pandas_df_commons.indexing import get_columns
from pandas_ta.pandas_ta_utils.decorators import for_each_column, for_each_top_level_row, for_each_top_level_column, \
    rename_with_parameters, is_time_consuming


@is_time_consuming
@for_each_top_level_row
@for_each_top_level_column
@rename_with_parameters(function_name='hurst_volatility', parameter_names=['period'], output_names=['H', 'nu'])
def ta_hurst_volatility(df: pd.DataFrame, period=255*2, lags=30, open="Open", high="High", low="Low", close="Close") -> _PANDAS:
    x = np.arange(1, lags)
    v = ta_gkyz_volatility(df, period=1, open=open, high=high, low=low, close=close).iloc[:, 0]

    def hurst(sig):
        # def del_Raw(s, q, x):
        #    return [np.mean(np.abs(s - s.shift(lag)) ** q) for lag in x]
        #
        # zeta_q = [np.polyfit(np.log(x), np.log(del_Raw(s, q, x)), 1)[0] for q in qVec]
        # h_est = np.polyfit(qVec, zeta_q, 1)[0]

        def dlsig2(sig, x):
            return [np.mean((sig - sig.shift(lag)) ** 2) for lag in x]

        model = np.polyfit(np.log(x), np.log(dlsig2(sig, x)), 1)
        return np.array([model[0] / 2., np.sqrt(np.exp(model[1]))])

    e_hurst = np.array([hurst(v.iloc[i-period+1:i]) for i in range(period - 1, len(df))])

    return [open, high, low, close], [x for x in e_hurst.T]


@for_each_top_level_row
@for_each_top_level_column
@rename_with_parameters(function_name='gkyz_volatility', parameter_names=['period'], output_names=['gkyz_volatility'])
def ta_gkyz_volatility(df: pd.DataFrame, period=12, open="Open", high="High", low="Low", close="Close") -> pd.DataFrame:
    # sqrt (sum of (  ln(o[i] / c[i-1] )^2 + 1/2 * (ln(h[i] / l[i]))^2 - (2 * ln(2) - 1) * (ln(c[i] / o[i]))^2   ) / N)
    vdf = df[[open, high, low, close]].copy()
    vdf.columns = ["o", "h", "l", "c"]
    vdf["c_1"] = df[close].shift(1)
    ln = np.log

    def one(r):
        return ln(r["o"] / r["c_1"])**2 + 0.5*(ln(r["h"] / r["l"]))**2 - (2 * ln(2) - 1)*(ln(r["c"] / r["o"]))**2

    v = np.sqrt(vdf.apply(one, axis=1).rolling(period).mean())
    return vdf.columns.tolist(), v.values


@for_each_top_level_row
@for_each_top_level_column
def ta_cc_volatility(df: pd.Series | pd.DataFrame, period=12, real="Close") -> pd.DataFrame:
    data = get_columns(df, [real]) if real is not None and df.ndim > 1 else df

    @for_each_column
    @rename_with_parameters(function_name='cc_volatility', parameter_names=['period'], output_names=['cc_volatility'])
    def wrapped_cc_volatility(col, period):
        # result gets converted by rename_with_parameters to DataFrame
        columns = col.columns.tolist() if data.ndim > 1 else [col.name]
        return columns, np.sqrt((np.log(col / col.shift(1)) ** 2).rolling(period).mean()).values

    return wrapped_cc_volatility(data, period)

@for_each_top_level_row
@for_each_top_level_column
def ta_zscore(df: pd.Series | pd.DataFrame, period=12, real="Close") -> pd.DataFrame:
    data = get_columns(df, [real]) if real is not None and df.ndim > 1 else df
    alpha = 2 / (period + 1) if period > 1 else period

    @for_each_column
    @rename_with_parameters(function_name='zscore', parameter_names=['period'], output_names=['std', 'z'])
    def wrapped_cc_volatility(col: pd.Series, period):
        # result gets converted by rename_with_parameters to DataFrame
        columns = col.columns.tolist() if data.ndim > 1 else [col.name]
        ma = col.ewm(alpha=alpha).mean().values
        std = col.ewm(alpha=alpha).std().values
        res = (col - ma) / std
        return columns, (std, res.values)

    return wrapped_cc_volatility(data, period)


@for_each_column
@for_each_top_level_row
def ta_up_down_volatility_ratio(df: pd.Series, period=60, normalize=True):
    returns = df.pct_change() if normalize else df

    res = pd.DataFrame({}, index=df.index)
    res["std+"] = returns.rolling(period).apply(lambda x: x[returns > 0].std())
    res["std-"] = returns.rolling(period).apply(lambda x: x[returns < 0].std())

    #res = res.join(returns[returns > 0].rolling(period).std().rename("std+"), how='left')
    #res = res.join(returns[returns < 0].rolling(period).std().rename("std-"), how='left')

    res = res.ffill()

    ratio = (res["std+"] / res["std-"].replace(0, 1) - 1).rename("std +/-")
    return ratio

