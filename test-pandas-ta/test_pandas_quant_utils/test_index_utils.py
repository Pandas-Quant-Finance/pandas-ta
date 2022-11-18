from unittest import TestCase

import pandas as pd

from pandas_df_commons.indexing._utils import same_columns_after_level


class TestQuantIndexUtils(TestCase):

    def test_similar_columns_multi_index(self):
        df1 = pd.DataFrame({}, index=[1, 2, 3, 4], columns=pd.MultiIndex.from_product([["a", "b"], range(3)]))
        df2 = pd.DataFrame({}, index=[1, 2, 3, 4], columns=pd.MultiIndex.from_tuples([("a", 1), ("a", 2), ("b", 1), ("b", 3)]))

        self.assertTrue(same_columns_after_level(df1))
        self.assertFalse(same_columns_after_level(df2))
