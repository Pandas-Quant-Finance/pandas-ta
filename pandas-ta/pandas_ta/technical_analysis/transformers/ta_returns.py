from __future__ import annotations

from typing import List

import numpy as np
import pandas as pd

from pandas_df_commons.indexing.decorators import foreach_top_level_row_and_column


def ta_returns(
        df: pd.DataFrame | pd.Series,
        period: int = 1,
        columns:str|List[str] = None,
        parallel=False,
) -> pd.DataFrame | pd.Series:
    @foreach_top_level_row_and_column(parallel=parallel)
    def f(df):
        if columns is not None:
            df = df[columns]

        return df.pct_change(period).dropna()

    return f(df)

@foreach_top_level_row_and_column(parallel=False)
def ta_logreturns(
        df: pd.DataFrame | pd.Series,
        period: int = 1,
        columns:str|List[str] = None,
        parallel=False,
) -> pd.DataFrame | pd.Series:

    @foreach_top_level_row_and_column(parallel=parallel)
    def f(df):
        if columns is not None:
            df = df[columns]

        return (np.log(df) - np.log(df.shift(period))).dropna()

    return f(df)