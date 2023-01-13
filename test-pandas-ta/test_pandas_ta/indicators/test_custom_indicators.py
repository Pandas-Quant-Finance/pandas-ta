from unittest import TestCase

import pandas as pd

from config import DF_TEST_MULTI_ROW_MULTI_COLUMN as DF_TEST
from pandas_ta.technical_analysis import ta_gmean, ta_mamentum


class TestCustomIndicators(TestCase):

    def test_gmean(self):
        df1 = ta_gmean(DF_TEST, 20)
        #df2 = ta_gmean(DF_TEST, 0.97)

        pd.testing.assert_frame_equal(df1.loc["A"], df1.loc["B"])
        #pd.testing.assert_frame_equal(df2.loc["A"], df2.loc["B"])

    def test_mamentum(self):
        mam = ta_mamentum(DF_TEST, 40, mas=20)
        print(mam)