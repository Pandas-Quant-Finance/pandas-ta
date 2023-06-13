from __future__ import annotations

from typing import Callable, Any

import numpy as np
import pandas as pd

from pandas_df_commons.indexing.decorators import foreach_top_level_row, foreach_column, convert_series_as_data_frame


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
    assert period > 1

    def _signal(previous, current):
        if enter_condition(previous, current):
            return enter_value(current) if callable(enter_value) else enter_value
        elif exit_condition(previous, current):
            return exit_value(current) if callable(exit_value) else exit_value
        else:
            return default_value(current) if callable(default_value) else default_value

    return df.rolling(period).apply(lambda row: _signal(row.iloc[0], row.iloc[-1]))
