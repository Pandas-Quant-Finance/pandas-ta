
from unittest import TestCase

from config import DF_TEST
from pandas_ta.technical_analysis import *
from pandas_ta.technical_analysis.indicators.lambda_indicator import ta_rolling_lambda


class TestIndicator(TestCase):

    def test_ta_apo(self):
        df = ta_rolling_lambda(DF_TEST[["Open", "Close"]], 10, lambda s: s.max().max())
        self.assertEqual(315.480011, df.iloc[-1,-1])
