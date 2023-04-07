from unittest import TestCase

from config import DF_TEST
from pandas_ta.technical_analysis import *


class TestTaTime(TestCase):

    def test_ta_sinusoidial_weekday(self):
        me = ta_sinusoidal_week_day(DF_TEST["Close"])[-1:]

        np.testing.assert_almost_equal(me.values[0], 1.2246467991473532e-16, 6)

    def test_ta_sinusoidial_week(self):
        me = ta_sinusoidal_week(DF_TEST["Close"])

        np.testing.assert_almost_equal(me.values[-1], -0.35460488704253595, 4)
        np.testing.assert_almost_equal(me.loc["2017-01-03"], 0.12053668025532306, 4)
        np.testing.assert_almost_equal(me.loc["2017-12-29"], -2.4492935982947064e-16, 4)

    def test_moon_phase(self):
        mp = ta_moon_phase(DF_TEST["Close"])

        np.testing.assert_almost_equal(mp.loc["2017-01-03"], 0.2134034931525374, 4)
        np.testing.assert_almost_equal(mp.loc["2017-12-29"], 0.7724928582285524, 4)
