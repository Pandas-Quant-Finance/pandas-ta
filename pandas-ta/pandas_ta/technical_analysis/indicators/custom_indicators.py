import numpy as np
import pandas as pd

from pandas_df_commons.extensions.functions import rolling_apply
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


@foreach_top_level_row
def ta_mamentum(df: pd.Series, period, real='Close', mas=None):
    data = get_columns(df, real) if real is not None and df.ndim > 1 else df

    class Object(object):
        def __init__(self, value):
            self.value = value

    @foreach_column
    @rename_with_parameters(function_name='mamemntum', parameter_names=['period', 'mas'], output_names=["momentum", "overdrive", "drag"])
    def wrapped(s, period, mas):
        mas = np.linspace(period - 1, 0, mas, endpoint=True, dtype=int)
        scale = (len(mas) / 2) - 1

        def mamentum_basis(window):
            means = []
            sum = 0

            for i in mas:
                sum += float(window.iloc[i])
                means.append(sum / (len(means) + 1))

            return Object(np.array(means))

        mmeans = rolling_apply(s, 60, mamentum_basis)
        return ["momentum", "overdrive", "drag"], pd.concat(
            [
                s.to_frame()[[]],
                rolling_apply(mmeans, 2, lambda x: np.sum(x.iloc[-1, 0].value >= x.iloc[0, 0].value) / scale),
                mmeans.apply(lambda x: x[0].value[-1] / x[0].value[0] - 1, axis=1),
                mmeans.apply(lambda x: np.abs(x[0].value[0] - x[0].value[1:]).argmin(), axis=1)
            ],
            axis=1,
            join='outer'
        ).values

    return wrapped(data, period, mas if mas is not None else period)
