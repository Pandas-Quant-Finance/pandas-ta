from unittest import TestCase

import pandas as pd

from config import DF_TEST_MULTI_ROW_MULTI_COLUMN as DF_TEST
from pandas_ta.technical_analysis import ta_gmean, ta_mamentum, ta_mdd, ta_top_bottom


class TestCustomIndicators(TestCase):

    def test_gmean(self):
        df1 = ta_gmean(DF_TEST, 20)
        df2 = ta_gmean(DF_TEST, 20, append=True)

        pd.testing.assert_frame_equal(df1.loc["A"], df1.loc["B"])
        pd.testing.assert_frame_equal(df2.loc["A"], df2.loc["B"])
        self.assertGreater(df2.shape[1], df1.shape[1])

    def test_mamentum(self):
        mam1 = ta_mamentum(DF_TEST, 40)
        mam2 = ta_mamentum(DF_TEST, 90, mas=40)
        print(mam1, mam2)

    def test_max_draw_down(self):
        df = ta_mdd(DF_TEST["spy"][["Open", "Close"]], 20)
        print(df.iloc[-1])

    def test_top_bottom(self):
        df = ta_top_bottom(DF_TEST["spy"])
        print(df.tail())
