from __future__ import annotations

from typing import Callable, Any

import numpy as np
import pandas as pd

from pandas_df_commons.extensions.functions import rolling_apply
from pandas_df_commons.indexing.decorators import foreach_top_level_row, foreach_column, convert_series_as_data_frame
from pandas_ta.ta_decorators import apply_appendable


@apply_appendable
@foreach_top_level_row
@foreach_column
@convert_series_as_data_frame
def ta_lambda_signal(
        df: pd.DataFrame,
        enter_condition: Callable[[Any, Any], bool],
        exit_condition: Callable[[Any, Any], bool],
        enter_value: Any = 1,
        exit_value: Any = 0,
        default_value: Any = np.nan,
        period: int = 2,
):
    assert period > 1, "period needs to be > 1"

    def _signal(previous, current):
        if enter_condition(previous, current):
            return enter_value(current) if callable(enter_value) else enter_value
        elif exit_condition(previous, current):
            return exit_value(current) if callable(exit_value) else exit_value
        else:
            return default_value(current) if callable(default_value) else default_value

    return rolling_apply(df, period, lambda row: _signal(row.iloc[0].squeeze(), row.iloc[-1].squeeze()))\
        .rename(columns=lambda x: f"signal_{x}")


@apply_appendable
@foreach_top_level_row
@foreach_column
@convert_series_as_data_frame
def ta_lambda_position():
    # do some stateful rolling apply

    pass