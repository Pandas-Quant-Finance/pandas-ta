from unittest import TestCase

from config import DF_TEST
from pandas_ta.technical_analysis import *


class TestVolatilityIndicators(TestCase):

    def test_ta_hurst_volatility(self):
        df = ta_hurst_volatility(DF_TEST[-100:], period=20, lags=3)


    def test_ta_gkyz_volatility(self):
        df = ta_gkyz_volatility(DF_TEST)

    def test_ta_cc_volatility(self):
        df = ta_cc_volatility(DF_TEST)

    def test_ta_zscore(self):
        df = ta_zscore(DF_TEST)
