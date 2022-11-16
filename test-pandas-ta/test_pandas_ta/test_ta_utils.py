from unittest import TestCase

import numpy as np
import pandas as pd

from config import DF_TEST, DF_TEST_MULTI_ROW_MULTI_COLUMN
from pandas_ta.pandas_ta_utils.index_utils import same_columns_after_level
from pandas_ta.technical_analysis import ta_apply, ta_resample, ta_repeat, ta_gkyz_volatility, ta_cc_volatility


class TestTaUtils(TestCase):

    def test_similar_columns_multi_index(self):
        df1 = pd.DataFrame({}, index=[1, 2, 3, 4], columns=pd.MultiIndex.from_product([["a", "b"], range(3)]))
        df2 = pd.DataFrame({}, index=[1, 2, 3, 4], columns=pd.MultiIndex.from_tuples([("a", 1), ("a", 2), ("b", 1), ("b", 3)]))

        self.assertTrue(same_columns_after_level(df1))
        self.assertFalse(same_columns_after_level(df2))

    def test_ta_repeat(self):
        df = DF_TEST[-100:]

        def vol_ratio_multi_periods(df, param):
            return (ta_gkyz_volatility(df, period=param) / ta_cc_volatility(df, period=param) - 1)

        result = ta_repeat(df, vol_ratio_multi_periods, range(2, 10), multiindex="HF/RF Vola Ratio")
        # print(result)

        self.assertEqual(result.shape, (100, 16))
        self.assertEqual(df.index.to_list(), result.index.to_list())

    def test_ta_apply(self):
        df = DF_TEST_MULTI_ROW_MULTI_COLUMN
        res = ta_apply(df, lambda x: (np.min(x.values), np.max(x.values)), period=10, columns=['High', 'Low'])
        self.assertEqual((7670, 4), res.shape)
        self.assertEqual(df.index.to_list(), res.index.to_list())

    def test_ta_resample(self):
        df = DF_TEST_MULTI_ROW_MULTI_COLUMN
        res = ta_resample(df, list, 'W')
        self.assertEqual((1592, 14), res.shape)
