
from unittest import TestCase

from config import DF_TEST
from pandas_ta.technical_analysis import *


class TestIndicator(TestCase):

    def test_ta_crossany(self):
        df = ta_crossany(DF_TEST[["Open", "Close"]], *[])

    def test_ta_crossover(self):
        df = ta_crossover(DF_TEST, *["Open", "Close"])
