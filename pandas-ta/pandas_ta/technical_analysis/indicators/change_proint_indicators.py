from __future__ import annotations

import numpy as np
import pandas as pd

from pandas_df_commons.extensions.functions import rolling_apply
from pandas_df_commons.indexing.decorators import foreach_top_level_row, foreach_column
from pandas_ta.ta_decorators import apply_appendable


@apply_appendable
@foreach_column
@foreach_top_level_row
def ta_std_ratio(df: pd.DataFrame, slow: int, fast: int, relative_loc: bool = False) -> pd.DataFrame:
    def change_point(df):
        tmp = np.abs(((df.rolling(fast).std() / df.iloc[-slow:].std()) - 1)).dropna()
        return {
            f"loc_{slow}_{fast}": (np.argmax(np.abs(tmp)) / slow) if relative_loc else tmp.index[np.argmax(tmp)],
            f"score_{slow}_{fast}": np.max(tmp)
        }

    return rolling_apply(df, slow+fast, change_point)
