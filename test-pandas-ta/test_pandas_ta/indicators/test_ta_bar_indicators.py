
from unittest import TestCase

from config import DF_TEST_MULTI_ROW_MULTI_COLUMN as DF_TEST
from pandas_ta.technical_analysis import *


class TestIndicator(TestCase):

    def test_ta_ad(self):
        df = ta_ad(DF_TEST, *[])
        pd.testing.assert_frame_equal(df.loc["A"], df.loc["B"])

    def test_ta_adosc(self):
        df = ta_adosc(DF_TEST, *[3, 10])
        pd.testing.assert_frame_equal(df.loc["A"], df.loc["B"])

    def test_ta_adx(self):
        df = ta_adx(DF_TEST, *[14])
        pd.testing.assert_frame_equal(df.loc["A"], df.loc["B"])

    def test_ta_adxr(self):
        df = ta_adxr(DF_TEST, *[14])
        pd.testing.assert_frame_equal(df.loc["A"], df.loc["B"])

    def test_ta_aroon(self):
        df = ta_aroon(DF_TEST, *[14])
        pd.testing.assert_frame_equal(df.loc["A"], df.loc["B"])

    def test_ta_aroonosc(self):
        df = ta_aroonosc(DF_TEST, *[14])
        pd.testing.assert_frame_equal(df.loc["A"], df.loc["B"])

    def test_ta_atr(self):
        df = ta_atr(DF_TEST, *[14])
        pd.testing.assert_frame_equal(df.loc["A"], df.loc["B"])

    def test_ta_avgprice(self):
        df = ta_avgprice(DF_TEST, *[])
        pd.testing.assert_frame_equal(df.loc["A"], df.loc["B"])

    def test_ta_bop(self):
        df = ta_bop(DF_TEST, *[])
        pd.testing.assert_frame_equal(df.loc["A"], df.loc["B"])

    def test_ta_cci(self):
        df = ta_cci(DF_TEST, *[14])
        pd.testing.assert_frame_equal(df.loc["A"], df.loc["B"])

    def test_ta_dx(self):
        df = ta_dx(DF_TEST, *[14])
        pd.testing.assert_frame_equal(df.loc["A"], df.loc["B"])

    def test_ta_medprice(self):
        df = ta_medprice(DF_TEST, *[])
        pd.testing.assert_frame_equal(df.loc["A"], df.loc["B"])

    def test_ta_mfi(self):
        df = ta_mfi(DF_TEST, *[14])
        pd.testing.assert_frame_equal(df.loc["A"], df.loc["B"])

    def test_ta_natr(self):
        df = ta_natr(DF_TEST, *[14])
        pd.testing.assert_frame_equal(df.loc["A"], df.loc["B"])

    def test_ta_obv(self):
        df = ta_obv(DF_TEST, *[])
        pd.testing.assert_frame_equal(df.loc["A"], df.loc["B"])

    def test_ta_typprice(self):
        df = ta_typprice(DF_TEST, *[])
        pd.testing.assert_frame_equal(df.loc["A"], df.loc["B"])

    def test_ta_ultosc(self):
        df = ta_ultosc(DF_TEST, *[7, 14, 28])
        pd.testing.assert_frame_equal(df.loc["A"], df.loc["B"])

    def test_ta_willr(self):
        df = ta_willr(DF_TEST, *[14])
        pd.testing.assert_frame_equal(df.loc["A"], df.loc["B"])
