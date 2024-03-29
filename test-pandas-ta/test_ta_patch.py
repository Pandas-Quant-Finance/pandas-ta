from unittest import TestCase

import pandas as pd

import pandas_ta as pta
from config import DF_TEST
from pandas_ta.technical_analysis import ta_sma

pta.monkey_patch_dataframe("TA")


class TestPatchDataFrame(TestCase):

    def test_exising_patch(self):
        pta.monkey_patch_dataframe("TA")

    def test_ta_indicator_access(self):
        self.assertIsNotNone(getattr(DF_TEST, "TA", None))
        pd.testing.assert_frame_equal(DF_TEST.TA.sma(20), ta_sma(DF_TEST, 20))

    def test_import_patched(self):
        from pandas_ta.patched import pd
        self.assertIsNotNone(getattr(pd.DataFrame({}), "ta", None))

    def test_random_patch(self):
        from pandas_ta.patched import pd
        self.assertIsNotNone(getattr(getattr(pd.DataFrame({}), "ta", None), 'garman_klass', None))

    def test_import_all_ta_functions(self):
        import pandas_ta as ta
        self.assertTrue(callable(ta.sma))
        pd.testing.assert_frame_equal(DF_TEST.TA.sma(20), ta.sma(DF_TEST, 20))
