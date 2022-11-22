import pandas as pd

from pandas_df_commons.indexing import get_columns
from pandas_df_commons.indexing.decorators import foreach_column, foreach_top_level_row, rename_with_parameters


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

