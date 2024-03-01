from __future__ import annotations

from typing import Callable, List

import pandas as pd

from pandas_df_commons.extensions.functions import rolling_apply
from pandas_df_commons.indexing.decorators import foreach_column, foreach_top_level_row_and_column
from pandas_ta.ta_decorators import apply_appendable


@apply_appendable
@foreach_top_level_row_and_column(parallel=False)
def ta_rolling_lambda(
        df: pd.DataFrame | pd.Series,
        period: int,
        func: Callable[[pd.DataFrame], pd.DataFrame | pd.Series],
        columns:str|List[str] = None,
        for_each_column=False,
        parallel=False,
) -> pd.DataFrame:
    if columns is not None:
        df = df[columns]

    if for_each_column:
        @foreach_column
        def f(*args, **kwargs):
            return func(*args, **kwargs)
    else:
        f = func

    return rolling_apply(df, period, f, parallel)
