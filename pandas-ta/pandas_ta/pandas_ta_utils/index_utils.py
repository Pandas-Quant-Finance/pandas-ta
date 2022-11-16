import pandas as pd

from pandas_df_commons.indexing import unique_level_values


def same_columns_after_level(df: pd.DataFrame, level=0):
    """

    :param df:
    :param level:
    :return: returns True if the columns below a given level are similar
    """
    if df.ndim < 2:
        return None

    df = df[:1].copy()
    top_level_columns = unique_level_values(df, level, axis=1)
    last_columns = None
    for tlc in top_level_columns:
        xs = df.xs(tlc, axis=1, level=level)
        this_columns = xs.columns.to_list()
        if last_columns is None or last_columns == this_columns:
            last_columns = this_columns
        else:
            return False

    return True
