from unittest import TestCase

from config import DF_TEST, DF_TEST_MULTI
from pandas_ta.technical_analysis.transformers.ta_intraday_bar import ta_hlc3, ta_garman_klass, ta_satchell_yoon


class TestIntradayTransformer(TestCase):

    def test_ta_hlc3(self):
        res = ta_hlc3(DF_TEST)
        print(res.tail())
        self.assertAlmostEqual(311.640035, res.iloc[-1])

    def test_ta_garman_klass(self):
        res = ta_garman_klass(DF_TEST_MULTI)
        print(res.columns)
        res = ta_garman_klass(DF_TEST)
        print(res.tail())
        self.assertAlmostEqual(0.000014, res.iloc[-1], 6)

    def test_ta_satchell_yoon(self):
        res = ta_satchell_yoon(DF_TEST)
        print(res.tail())
        self.assertAlmostEqual(0.000026, res.iloc[-1], 6)

