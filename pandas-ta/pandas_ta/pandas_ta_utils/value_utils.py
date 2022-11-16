import numpy as np


def symmetric_quantile_factors(a, bins=11):
    return np.linspace(1-a, 1+a, bins)


