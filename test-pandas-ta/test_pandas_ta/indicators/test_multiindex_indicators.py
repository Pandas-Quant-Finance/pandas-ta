
from unittest import TestCase

import pandas as pd
from pandas import testing
from config import DF_TEST, DF_TEST_MULTI_ROW_MULTI_COLUMN
from pandas_ta.technical_analysis import *


class TestIndicator(TestCase):

    def test_ta_rsi(self):
        df = ta_rsi(DF_TEST, *[14], None)

        self.assertEquals(len(df.columns), len(DF_TEST.columns))
        self.assertListEqual(
            df.columns.tolist(),
            ["rsi('Open', 14)", "rsi('High', 14)", "rsi('Low', 14)", "rsi('Close', 14)", "rsi('Adj Close', 14)", "rsi('Volume', 14)"]
        )

    def test_ta_adx(self):
        df = ta_adx(DF_TEST_MULTI_ROW_MULTI_COLUMN, *[14])

        self.assertListEqual(
            df.columns.tolist(),
            [('spy', "adx('High', 'Low', 'Close', 14)"), ('gld', "adx('High', 'Low', 'Close', 14)")]
        )
        testing.assert_frame_equal(df.loc["A"], df.loc["B"])
