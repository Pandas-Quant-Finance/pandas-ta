from collections import defaultdict

import numpy as np
import pandas as pd

from pandas_df_commons.extensions.functions import rolling_apply
from pandas_df_commons.indexing import get_columns
from pandas_df_commons.indexing.decorators import foreach_column, foreach_top_level_row, rename_with_parameters, \
    foreach_top_level_column


@foreach_top_level_row
def ta_gmean(df: pd.Series, period, real='Close'):
    from scipy.stats import gmean

    data = get_columns(df, real) if real is not None and df.ndim > 1 else df

    @foreach_column
    @rename_with_parameters(function_name='gmean', parameter_names=['period'])
    def wrapped(s, period):
        if period <= 1.0:
            raise NotImplementedError()
            # return [df.name], df.ewm(alpha=period).apply(gmean).values
        else:
            return [s.name], s.rolling(period).apply(gmean).values

    return wrapped(data, period)


@foreach_top_level_row
def ta_mamentum(df: pd.Series, period, real='Close', mas=None):
    data = get_columns(df, real) if real is not None and df.ndim > 1 else df

    class Object(object):
        def __init__(self, value):
            self.value = value

    @foreach_column
    @rename_with_parameters(function_name='mamemntum', parameter_names=['period', 'mas'], output_names=["momentum", "overdrive", "drag"])
    def wrapped(s, period, mas):
        mmas = np.linspace(period - 1, 0, mas, endpoint=True, dtype=int)
        scale = (len(mmas) / 2)

        def mamentum_basis(window):
            means = []
            sum = 0

            for i in mmas:
                sum += float(window.iloc[i])
                means.append(sum / (len(means) + 1))

            return Object(np.array(means))

        mmeans = rolling_apply(s, period, mamentum_basis)
        return ["momentum", "overdrive", "drag"], pd.concat(
            [
                s.to_frame()[[]],
                rolling_apply(mmeans, 2, lambda x: np.sum(x.iloc[-1, 0].value >= x.iloc[0, 0].value) / scale - 1),
                mmeans.apply(lambda x: x[0].value[-1] / x[0].value[min(2, mas)] - 1, axis=1),
                mmeans.apply(lambda x: np.abs(x[0].value[0] - x[0].value[1:]).argmin(), axis=1)
            ],
            axis=1,
            join='outer'
        ).values

    return wrapped(data, period, mas if mas is not None else period)


@foreach_top_level_row
def ta_mdd(df: pd.DataFrame, period):
    """
    Indicator: Maximum Draw Down
    Parameters
    ----------
    df
    period

    Returns
    -------
    DataFrame[draw_down, max_draw_down]
    """

    @foreach_column
    def wrapped(s, period):
        roll_max = s.rolling(period).max(axis=None)
        drawdown = s / roll_max - 1.0
        max_draw_down = drawdown.rolling(period).min()

        return pd.concat([drawdown, max_draw_down], axis=1, keys=[f"drawdown({period})", f"max_draw_down({period})"])

    return wrapped(df, period)


@foreach_top_level_row
@foreach_top_level_column
def ta_hh_ll(df: pd.DataFrame, period=None, high='Close', low='Close', ignore_quantile_move=.05):
    assert period is None, "None None period not yet implemented!"
    h_data = get_columns(df, high) if high is not None and df.ndim > 1 else df
    l_data = get_columns(df, low) if low is not None and df.ndim > 1 else df

    # high:
    # if hh slope is negative
    #   a: go back until slope is not 0
    #     if last hh slope was positive
    #       go back until ll slope is not 0
    #         if ll slope was positive "a" was a high
    #
    # low:
    # if ll slope is positive
    #   a: go back until slope is not 0
    #     if last ll slope was negative
    #       go back until hh slope is not 0
    #         if hh slope was netgatoive "a" was a low
    def wrapped(df):
        hh, ll = None, None
        reset_hh, reset_ll = False, False

        # ignore very small moves
        h_min_change_needed = h_data.pct_change().abs().replace(0, None).dropna().quantile(ignore_quantile_move)
        l_min_change_needed = l_data.pct_change().abs().replace(0, None).dropna().quantile(ignore_quantile_move) if low != high else h_min_change_needed

        for (_, vh), (_, vl) in zip(h_data.items(), l_data.items()):
            if hh is None:
                hh = vh
            elif vh > hh:
                reset_hh = False
                if abs(hh / vh - 1) > h_min_change_needed:
                    reset_ll = True
                    hh = vh
            elif reset_hh and vh > ll:
                reset_hh = False
                if abs(hh / vh - 1) > h_min_change_needed:
                    hh = vh

            if ll is None:
                ll = vl
            elif vl < ll:
                reset_ll = False
                if abs(ll / vl - 1) > l_min_change_needed:
                    reset_hh = True
                    ll = vl
            elif reset_ll and vl < hh:
                reset_ll = False
                if abs(ll / vl - 1) > l_min_change_needed:
                    ll = vl

            yield hh, ll

    hh_ll = pd.DataFrame([i for i in wrapped(df)], index=df.index, columns=["hh", "ll"])
    return hh_ll


@foreach_top_level_row
@foreach_top_level_column
def ta_top_bottom(df: pd.DataFrame, period=None, high='Close', low='Close', ignore_quantile_move=.05):
    # algorithm:
    #  when the next highest high is a lower high and the slope of the lest low before the current high was positive
    #  then we have found a top. on the other hand if the next lowest low is higher and the latest slope of the previous
    #  highest high was negative we have found a bottom.
    # however, this algorithm fails on sharpe swings and consecutive tops or bottoms which need to be fixed afterward.
    hh_ll = ta_hh_ll(df, period, high, low, ignore_quantile_move)

    hh = hh_ll[["hh"]].copy()
    hh["hh%"] = hh["hh"].pct_change().fillna(0)
    hh = hh.loc[hh["hh%"] != 0]

    ll = hh_ll[["ll"]].copy()
    ll["ll%"] = ll["ll"].pct_change().fillna(0)
    ll = ll.loc[ll["ll%"] != 0]

    top = hh[(hh["hh%"] > 0) & (hh["hh%"].shift(-1) < 0)]
    top_join_index = ll.index.get_indexer(top.index, method='pad')
    top = top[-len(top_join_index):].copy()
    top["ll%"] = ll.iloc[top_join_index]["ll%"].values

    bottom = ll[(ll["ll%"] < 0) & (ll["ll%"].shift(-1) > 0)]
    bottom_join_index = hh.index.get_indexer(bottom.index, method='pad')
    bottom = bottom[-len(bottom_join_index):].copy()
    bottom["hh%"] = hh.iloc[bottom_join_index]["hh%"].values

    top = top[top["ll%"] > 0]["hh"].rename("top")
    bottom = bottom[bottom["hh%"] < 0]["ll"].rename("bottom")

    top_bottom = pd.concat(
        [hh_ll, top, bottom],
        axis=1,
        join="outer"
    )

    # fix sharp turnings, if a high pokes above the interpolated highest high we need to add this high
    #  similarly if a low pokes below the interpolated lowest lows we need to add this turning point as well
    idx_top_poke = top_bottom["hh"] > top_bottom["top"].interpolate()
    top_bottom.loc[idx_top_poke, "top"] = top_bottom.loc[idx_top_poke, "hh"]

    idx_bottom_poke = top_bottom["ll"] < top_bottom["bottom"].interpolate()
    top_bottom.loc[idx_bottom_poke, "bottom"] = top_bottom.loc[idx_bottom_poke, "ll"]

    # finally fix recurring tops / and bottoms in the same period
    excl_idx = defaultdict(set)
    for period, counter_events, selector in [("top", "bottom", np.nanargmin), ("bottom", "top", np.nanargmax)]:
        for idx, row in top_bottom[~pd.isna(top_bottom[period])].index.to_series().shift(1).dropna().items():
            tmp = top_bottom.loc[row:idx + 1, counter_events]
            try:
                extrema = selector(tmp)

                if len(tmp) > 1 and extrema >= 0:
                    excl_idx[counter_events].update(tmp.index.drop(tmp.index[extrema]))
            except ValueError as ignore:
                pass

    for k, v in excl_idx.items():
        top_bottom.loc[list(v), k] = None

    return top_bottom[["top", "bottom"]]
