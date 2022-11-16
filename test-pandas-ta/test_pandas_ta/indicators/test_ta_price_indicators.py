
from unittest import TestCase

from config import DF_TEST
from pandas_ta.technical_analysis import *


class TestIndicator(TestCase):

    def test_ta_apo(self):
        df = ta_apo(DF_TEST, *[12, 26])

    def test_ta_bbands(self):
        df = ta_bbands(DF_TEST, *[5, 2.0])

    def test_ta_cmo(self):
        df = ta_cmo(DF_TEST, *[14])

    def test_ta_dema(self):
        df = ta_dema(DF_TEST, *[30])

    def test_ta_ema(self):
        df = ta_ema(DF_TEST, *[30])

    def test_ta_kama(self):
        df = ta_kama(DF_TEST, *[30])

    def test_ta_macd(self):
        df = ta_macd(DF_TEST, *[12, 26, 9])

    def test_ta_max(self):
        df = ta_max(DF_TEST, *[30])

    def test_ta_min(self):
        df = ta_min(DF_TEST, *[30])

    def test_ta_mom(self):
        df = ta_mom(DF_TEST, *[10])

    def test_ta_ppo(self):
        df = ta_ppo(DF_TEST, *[12, 26])

    def test_ta_roc(self):
        df = ta_roc(DF_TEST, *[10])

    def test_ta_rocr(self):
        df = ta_rocr(DF_TEST, *[10])

    def test_ta_rsi(self):
        df = ta_rsi(DF_TEST, *[14])

    def test_ta_sma(self):
        df = ta_sma(DF_TEST, *[30])

    def test_ta_stddev(self):
        df = ta_stddev(DF_TEST, *[5])

    def test_ta_stochrsi(self):
        df = ta_stochrsi(DF_TEST, *[14])

    def test_ta_sum(self):
        df = ta_sum(DF_TEST, *[30])

    def test_ta_tema(self):
        df = ta_tema(DF_TEST, *[30])

    def test_ta_trima(self):
        df = ta_trima(DF_TEST, *[30])

    def test_ta_trix(self):
        df = ta_trix(DF_TEST, *[30])

    def test_ta_tsf(self):
        df = ta_tsf(DF_TEST, *[14])

    def test_ta_var(self):
        df = ta_var(DF_TEST, *[5])
