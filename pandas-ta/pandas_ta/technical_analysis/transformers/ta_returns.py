from __future__ import annotations

from functools import partial
from typing import List

import numpy as np
import pandas as pd

from pandas_df_commons.indexing import get_columns
from pandas_df_commons.indexing.decorators import foreach_top_level_row_and_column, convert_series_as_data_frame
from pandas_ta.ta_decorators import apply_appendable


@apply_appendable
def ta_returns(
        df: pd.DataFrame | pd.Series,
        period: int = 1,
        columns: str | List[str] = None,
        log: bool = False,
        parallel: bool = False,
) -> pd.DataFrame | pd.Series:

    data = get_columns(df, [columns]) if columns is not None and df.ndim > 1 else df

    if log:
        @foreach_top_level_row_and_column(parallel=parallel)
        @convert_series_as_data_frame
        def f(df):
            return (np.log(df) - np.log(df.shift(period))).replace([-np.inf, np.inf], 0).dropna()
    else:
        @foreach_top_level_row_and_column(parallel=parallel)
        @convert_series_as_data_frame
        def f(df):
            return df.pct_change(period).replace([-np.inf, np.inf], 0).fillna(0)

    return f(data)


ta_logreturns = partial(ta_returns, log=True)
