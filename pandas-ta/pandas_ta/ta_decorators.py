import pandas as pd

from pandas_df_commons.indexing.multiindex_utils import add_to_multi_index


def apply_appendable(func):
    def wrapper(df, *args, **kwargs):
        append = kwargs.pop("append", False)
        res = func(df, *args, **kwargs)

        if append:
            while res.columns.nlevels > df.columns.nlevels:
                # we need to append an empty level to df
                df = add_to_multi_index(df, ["*" for i in range(df.shape[1])], level=-1)

        return pd.concat([df, res], sort=True) if append else res

    return wrapper


