from unittest import TestCase

import pandas as pd

from config import DF_TEST_MULTI_ROW_MULTI_COLUMN as DF_TEST
from pandas_ta.technical_analysis import ta_gmean, ta_mamentum, ta_mdd, ta_top_bottom, ta_bbands


class TestAppendableDecorator(TestCase):

    def test_bbands(self):
        df = ta_bbands(DF_TEST, *[5, 2.0], append=True)
        print(df.columns)



