import pandas as pd

from pandas_df_commons.indexing.multiindex_utils import add_to_multi_index


def apply_appendable(func):
    def wrapper(df, *args, **kwargs):
        append = kwargs.pop("append", False)
        res = func(df, *args, **kwargs)

        if append:
            while res.columns.nlevels > df.columns.nlevels:
                # we need to append an empty level to df
                df = add_to_multi_index(df, "*", level=(1 if df.columns.nlevels > 1 else 0))

        res = pd.concat([df, res], axis=1).sort_index() if append else res
        if df.columns.nlevels > 1:
            res.sort_index(axis=1, level=0)

        return res

    return wrapper


