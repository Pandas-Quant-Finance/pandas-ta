import numpy as np
import pandas as pd

from pandas_df_commons.indexing.decorators import foreach_top_level_column
TWO_LOG2_MINUS_1 = 2 * np.log(2) - 1


@foreach_top_level_column
def ta_hlc3(df: pd.DataFrame, high='High', low='Low', close='Close') -> pd.DataFrame:
    return df[[high, low, close]].mean(axis=1).rename("HLC3")


@foreach_top_level_column
def ta_garman_klass(df: pd.DataFrame, open='Open', high='High', low='Low', close='Close') -> pd.DataFrame:
    return (
        0.5 * (np.log(df[high]) - np.log(df[low])) ** 2 - TWO_LOG2_MINUS_1 * (np.log(df[close]) - np.log(df[open])) ** 2
    ).rename("GKHF-Vol")


@foreach_top_level_column
def ta_satchell_yoon(df: pd.DataFrame, open='Open', high='High', low='Low', close='Close') -> pd.DataFrame:
    # [ln(H) - ln(O)] * [ln(H) - ln(C)] + [ln(L) - ln(O)] * [ln(L) - ln(C)]
    return (
        (np.log(df[high]) - np.log(df[open])) * (np.log(df[high]) - np.log(df[close])) +\
        (np.log(df[low]) - np.log(df[open])) * (np.log(df[low]) - np.log(df[close]))
    ).rename("SYHF-Vol")

