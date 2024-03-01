from __future__ import annotations
import typing as _t
import pandas as _pd

from pandas_df_commons.indexing.multiindex_utils import add_to_multi_index
from pandas_df_commons.indexing.decorators import foreach_top_level_row, foreach_top_level_column
from pandas_ta.ta_decorators import apply_appendable


@apply_appendable
def ta_repeat(
        df: _pd.DataFrame,
        func: _t.Callable[[_pd.DataFrame, _t.Any], _pd.DataFrame],
        repetition: _t.Iterable,
        multiindex=None,
        *args,
        **kwargs):
    parameters = list(repetition)
    res = _pd.concat(
            [func(df, param, *args, **kwargs) for param in parameters] + [_pd.DataFrame({}, index=df.index)],
            axis=1,
            join='outer',
            keys=parameters
        ).swaplevel(-2, -1, 1)

    return add_to_multi_index(res, multiindex) if multiindex else res


@apply_appendable
@foreach_top_level_row
@foreach_top_level_column
def ta_apply(df: _pd.DataFrame, func: _t.Callable | _t.Dict[str, _t.Callable], period=None, columns=None):
    if isinstance(func, dict):
        keys = []
        frames = []
        for k, f in func.items():
            frames.append(ta_apply(df, f, period=period, columns=columns))
            keys.append(k)

        res = _pd.concat(frames, axis=1, names=keys)

        if not isinstance(res.columns, _pd.MultiIndex):
            res.columns = keys

        return res

    if columns:
        df = df[columns]

    def as_pandas(x):
        if not isinstance(x, (_pd.Series, _pd.DataFrame)):
            if hasattr(x, 'ndim'):
                if x.ndim > 1:
                    return _pd.DataFrame(x)

            return _pd.DataFrame(x if isinstance(x, (list, set, tuple)) else [x]).T

    if not period:
        return df.apply(func, axis=1, result_type='reduce')
    else:
        rdf = _pd.concat(
            [as_pandas(func(df.iloc[i - period: i])) for i in range(period, len(df))],
            axis=0
        )

        rdf.index = df.index[period:]
        return _pd.concat([_pd.DataFrame({}, index=df.index), rdf], axis=1, join='outer')


@apply_appendable
@foreach_top_level_row
def ta_resample(df: _pd.DataFrame, func, freq='D', **kwargs):
    return df.resample(freq, **kwargs).apply(func)
