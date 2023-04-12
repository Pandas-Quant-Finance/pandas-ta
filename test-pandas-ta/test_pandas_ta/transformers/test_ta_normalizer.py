from __future__ import annotations

from unittest import TestCase
from pandas_ta.technical_analysis import ta_returns

from config import DF_TEST
from pandas_ta.technical_analysis.transformers.ta_normalizer import ta_standardized


class TestNormalizer(TestCase):

    def test_ta_standardized(self):
        res = ta_standardized(ta_returns(DF_TEST["Close"][-40:]))
        print(res.tail())
