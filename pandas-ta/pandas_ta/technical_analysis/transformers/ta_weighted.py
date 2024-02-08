from __future__ import annotations

from typing import List

import pandas as pd

from pandas_df_commons import foreach_top_level_row
from pandas_df_commons.indexing import get_columns


def ta_weighted_row(
        df: pd.DataFrame | pd.Series,
        weights: str | List[str] | pd.Series,
        columns: str | List[str] = None,
):
    data = get_columns(df, [columns]) if columns is not None and df.ndim > 1 else df
    weights = get_columns(df, [weights])

    if not isinstance(weights, (pd.Series, pd.DataFrame)):
        data = data.drop(weights.columns, axis=1, errors="ignore")

    assert weights.shape == data.shape, f"weight shape need to match {weights.shape} != {data.shape}"

    return (data * weights.values).div(weights.sum(axis=1), axis=0)


def ta_average_weighted_column(
        df: pd.DataFrame | pd.Series,
        weights: str | List[str] | pd.Series,
        period: int,
        columns: str | List[str] = None,
):
    data = get_columns(df, [columns]) if columns is not None and df.ndim > 1 else df
    weights = get_columns(df, [weights])

    @foreach_top_level_row
    def wrapped(dfv: pd.DataFrame, dfw: pd.DataFrame):
        return dfv.rolling(period).sum().div(dfw.rolling(period).sum(), axis=0)

    return wrapped(data * weights.values, weights)
