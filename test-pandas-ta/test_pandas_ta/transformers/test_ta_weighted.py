from unittest import TestCase

from pandas_df_commons.indexing import get_columns
from pandas_ta.technical_analysis import ta_weighted_row, ta_average_weighted_column
from config import DF_TEST_MULTI, DF_TEST


class TaWeightedTransformer(TestCase):

    def test_ta_weighted_row(self):
        res = ta_weighted_row(DF_TEST_MULTI, columns='Close', weights='Volume')
        expected = (DF_TEST_MULTI.iloc[-1][("spy", "Close")] * DF_TEST_MULTI.iloc[-1][("spy", "Volume")]) / get_columns(DF_TEST_MULTI, "Volume").iloc[-1].mean()
        print(res.tail())
        print(expected)
        self.assertAlmostEqual(res.iloc[-1, 0], expected)

    def test_ta_average_weighted_column(self):
        # TODO test dollar volume weighted average
        res = ta_average_weighted_column(DF_TEST.tail(), columns='Close', weights='Volume', period=3)
        expected = (DF_TEST["Close"].tail(3) * DF_TEST["Volume"].tail(3)).sum() / DF_TEST["Volume"].tail(3).sum()
        print(DF_TEST[["Close", "Volume"]].tail(3))
        print(res.tail())
        print(expected)
        self.assertAlmostEqual(res.iloc[-1], expected)

