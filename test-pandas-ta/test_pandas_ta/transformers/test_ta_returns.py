from unittest import TestCase

from pandas_ta.technical_analysis import ta_returns, ta_logreturns
from config import DF_TEST


class TaReturnTransformer(TestCase):

    def test_ta_returns(self):
        res = ta_returns(DF_TEST)
        print(res.tail())

    def test_ta_logreturns(self):
        res = ta_logreturns(DF_TEST, parallel=True)
        print(res.tail())

