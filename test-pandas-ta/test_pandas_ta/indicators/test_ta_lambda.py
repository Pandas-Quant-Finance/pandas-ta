
from unittest import TestCase

import pandas as pd

from config import DF_TEST
from pandas_ta.technical_analysis import *
from pandas_ta.technical_analysis.indicators.lambda_indicator import ta_rolling_lambda


class TestIndicator(TestCase):

    def test_ta_rolling_lambda(self):
        df = ta_rolling_lambda(DF_TEST[["Open", "Close"]], 10, lambda s: s.max().max())
        self.assertEqual(315.480011, df.iloc[-1,-1])

    def test_ta_strategy(self):
        df = ta_bbands(DF_TEST, 60, 1.5, append=True).droplevel(0, axis=1)
        df["open_long"] = ta_crossover_value(df, 'Close', 'bbands_lower', 'Close')
        df["close_long"] = ta_coalesce(
            ta_crossunder_value(df, 'Close', 'bbands_lower', 'Close'),  # crossing back under is a failed trade
            ta_crossover_value(df, 'Close', 'bbands_upper', 'Close'),   # crossing over upper is exit with success
        )

        print(df["open_long"].sum(), df["close_long"].sum())

        def strategy(state):
            last, current = state.get_last_current("open_long")
            close = state.t["close_long"]
            pos, _ = state.previous if state.previous is not None else (0, None)

            if not pd.isna(last) and current > last:
                # buy long
                return 1, 1
            elif pos > 0 and not pd.isna(close):
                return 0, -1
            else:
                return pos, None

        dfs = ta_strategy(df, strategy, names=["pos", "signal"])
        perf = ta_cumprod1p(df["Close"].pct_change() * dfs["pos"])

        print(dfs)