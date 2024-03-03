from __future__ import annotations

from typing import Iterable

import pandas as pd

from pandas_df_commons.indexing import get_columns


# NOTE extending functions call already annotated functions
def ta_crossunder(df: pd.DataFrame, real=None, real1=None, **kwargs) -> pd.DataFrame:
    from pandas_ta.technical_analysis import ta_crossover
    return ta_crossover(df, real1 or df.columns[1], real or df.columns[0], **kwargs)


# NOTE extending functions call already annotated functions
def ta_crossover_value(df: pd.DataFrame, real=None, real1=None, value=1, **kwargs) -> pd.DataFrame:
    from pandas_ta.technical_analysis import ta_crossover
    res = ta_crossover(df, real, real1, **kwargs).astype(bool)

    try:
        value = get_columns(df, [value])
    except KeyError as ke:
        if isinstance(value, str) or not isinstance(value, Iterable):
            value = pd.Series(value, index=df.index)
        else:
            raise ke

    value = value[res.index].copy()
    value[~res.values.squeeze()] = None
    return value.to_frame() if value.ndim < 2 else value


# NOTE extending functions call already annotated functions
def ta_crossunder_value(df: pd.DataFrame, real=None, real1=None, value=1, **kwargs) -> pd.DataFrame:
    return ta_crossover_value(df, real1, real, value, **kwargs)
