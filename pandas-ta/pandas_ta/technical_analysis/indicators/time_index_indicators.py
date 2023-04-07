from __future__ import annotations

import numpy as _np
import pandas as _pd
import pandas as pd
from dateutil.relativedelta import relativedelta

from pandas_df_commons.indexing.decorators import *
from pandas_ta.pandas_ta_utils.time_utils import opex_date_of_date
import pylunar

# Location: Boston, MA, USA
_MOON_INFO = pylunar.MoonInfo((42, 21, 30), (-71, 3, 35))


@foreach_top_level_row
def ta_decimal_year(df: _pd.DataFrame | _pd.Series):
    return ((df.index.strftime("%j").astype(float) - 1) / 366 + df.index.strftime("%Y").astype(float))\
        .to_series(index=df.index, name="decimal_time")


@foreach_top_level_row
def ta_sinusoidal_week_day(po: _pd.DataFrame | _pd.Series):
    if not isinstance(po.index, _pd.DatetimeIndex):
        df = po.copy()
        df.index = _pd.to_datetime(df.index)
    else:
        df = po

    return _np.sin(2 * _np.pi * (df.index.dayofweek / 6.0)).to_series(index=po.index, name="dow")


@foreach_top_level_row
def ta_sinusoidal_week(po: _pd.DataFrame | _pd.Series):
    if not isinstance(po.index, _pd.DatetimeIndex):
        df = po.copy()
        df.index = _pd.to_datetime(df.index)
    else:
        df = po

    return _np.sin(2 * _np.pi * (df.index.isocalendar().week / 52.0)).rename("week")


@foreach_top_level_row
def ta_dist_opex(po: _pd.DataFrame | _pd.Series):
    if not isinstance(po.index, _pd.DatetimeIndex):
        df = po.copy()
        df.index = _pd.to_datetime(df.index)
    else:
        df = po

    def dist_next_opex(ts: pd.Timestamp):
        d = ts.date()
        opex = opex_date_of_date(d)
        if opex.day < d.day:
            next_opex = opex_date_of_date(d + relativedelta(months=1))
        else:
            next_opex = opex
            opex = opex_date_of_date(d - relativedelta(months=1))

        dist = (next_opex - d).days / (next_opex - opex).days
        return dist

    return df.index.to_series().apply(dist_next_opex).rename("dist_2_opex")


@foreach_top_level_row
def ta_moon_phase(df: _pd.DataFrame | _pd.Series):
    if not isinstance(df.index, _pd.DatetimeIndex):
        df = df.copy()
        df.index = _pd.to_datetime(df.index)

    def moon_phase(t: pd.Timestamp):
        t = t.tz_localize(tz='UTC') if t.tzinfo is None else t.astimezone(tz='UTC')
        _MOON_INFO.update((t.year, t.month, t.day, t.hour, t.minute, t.second))
        return _MOON_INFO.fractional_phase()

    return df.index.to_series().apply(moon_phase).rename("moonphase")
