from unittest import TestCase

import numpy.testing
import pandas as pd
from numpy import nan
from pandas_ta.technical_analysis.signals.lambda_signals import ta_lambda_signal


class TestLambdaSignal(TestCase):

    def test_lambda_signal(self):
        df = pd.DataFrame({"a": [0, 0, 0, 1, 1, 1, 1, 0, 0]})
        res = ta_lambda_signal(
            df,
            lambda prev, curr: prev <= 0 < curr,
            lambda prev, curr: prev > 0 >= curr,
        )

        numpy.testing.assert_array_almost_equal(
            [nan, nan, 1.0, nan, nan, nan, 0.0, nan],
            res["signal_0"].tolist()
        )
