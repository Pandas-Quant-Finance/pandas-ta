from __future__ import annotations
from functools import wraps
from typing import Dict, Callable, Any, T

import numpy as np
import pandas as pd
import logging

from pandas_df_commons.indexing import unique_level_values
from pandas_df_commons.indexing.multiindex_utils import add_to_multi_index
from pandas_ta.pandas_ta_utils.index_utils import same_columns_after_level

_log = logging.getLogger(__name__)


def for_each_column(func):
    @wraps(func)
    def exec_on_each_column(df: pd.DataFrame, *args, **kwargs):
        if df.ndim > 1 and df.shape[1] > 0:
            results = [func(df[col], *args, **kwargs) for col in df.columns]  # theoretically could be done parallel
            if results[0].ndim > 1 and results[0].shape[1] > 1:
                for i, col in enumerate(df.columns):
                    results[i].columns = pd.MultiIndex.from_product([[col], results[i].columns.tolist()])

            return pd.concat(results, axis=1, join='inner')
        else:
            return func(df, *args, **kwargs)

    return exec_on_each_column


def convert_series_as_data_frame(func):
    @wraps(func)
    def to_dataframe(df: pd.DataFrame | pd.Series, *args, **kwargs):
        return func(df.to_frame() if df.ndim < 2 else df, *args, **kwargs)

    return to_dataframe


def for_each_top_level_column(func):
    def agg(results, level):
        groups = [add_to_multi_index(res, group, inplace=True, level=level) for group, res in results.items()]
        return pd.concat(groups, axis=1)

    return for_each_top_level_column_aggregate(agg)(func)


def for_each_top_level_column_aggregate(aggregator: Callable[[Dict[Any, T], int], T], level=0):
    def decorator(func):
        @wraps(func)
        def exec_on_each_tl_column(df: pd.DataFrame, *args, **kwargs):
            if df.ndim > 1 and isinstance(df.columns, pd.MultiIndex):
                # check if the shape of the 2nd level is identical else threat as if not multi index
                if same_columns_after_level(df, level):
                    top_level = unique_level_values(df, level, axis=1)
                    results = {group: func(df.xs(group, axis=1, level=level), *args, **kwargs) for group in top_level}
                    return aggregator(results, level)
                else:
                    _log.warning(f"columns in further levels do not follow the same structure! Treat as normal Index")
                    return func(df, *args, **kwargs)
            else:
                return func(df, *args, **kwargs)

        return exec_on_each_tl_column
    return decorator


def for_each_top_level_row(func):
    def agg(results: Dict):
        return pd.concat(results.values(), keys=results.keys(), axis=0)

    return for_each_top_level_row_aggregate(agg)(func)


def for_each_top_level_row_aggregate(aggregator: Callable[[Dict[Any, T]], T]):
    def decorator(func):
        @wraps(func)
        def exec_on_each_tl_row(df: pd.DataFrame, *args, **kwargs):
            if isinstance(df.index, pd.MultiIndex):
                top_level = unique_level_values(df, level=0, axis=0)
                if len(top_level) > 1:
                    results = {group: func(df.loc[group], *args, **kwargs) for group in top_level}
                    return aggregator(results)
                else:
                    return func(df, *args, **kwargs)
            else:
                return func(df, *args, **kwargs)

        return exec_on_each_tl_row
    return decorator


def is_time_consuming(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)

    wrapper._is_timeconsuming = True
    return wrapper


def rename_with_parameters(function_name, parameter_names, output_names=None):
    def decorator(func):
        def wrapper(*args, **kwargs):
            columns, result = func(*args, **kwargs)
            length = max([len(r) for r in result]) if isinstance(result, (tuple, list)) else len(result)

            argvalues = list(args[1:])
            if len(argvalues) < len(parameter_names):
                argvalues += [kwargs.get(pn, "None") for pn in parameter_names[len(args) - 1:]]
            argvaluestring = f', {str(argvalues)[1:-1]}' if len(argvalues) > 0 else ""

            if output_names is None or len(output_names) < 2:
                column_names = [f"{function_name}({str(columns)[1:-1]}{argvaluestring})"]
            else:
                column_names = pd.MultiIndex.from_tuples([
                    (f"{function_name}({str(columns)[1:-1]}{argvaluestring})", out_name) for out_name in output_names
                ])

            index = args[0].index[-length:]
            df = pd.DataFrame(np.array(result).T, index=index, columns=column_names)

            return df
        return wrapper
    return decorator