from collections import defaultdict

import pandas as pd


class _ItemFaker(object):

    def __getitem__(self, item):
        return None


class StrategyState(object):

    def __init__(self):
        self.t_1: pd.Series = _ItemFaker()
        self.t: pd.Series = _ItemFaker()
        self.previous = None
        self.state = {}
        self._cache = {}

    def _with_row(self, row: pd.Series):
        self.t_1 = self.t
        self.t = row
        self._cache = {}
        return self

    def __getitem__(self, item):
        return self.state.get(item, None)

    def __setitem__(self, key, value):
        self.state[key] = value

    def get_last_current(self, key, default_last=None):
        if key in self._cache: return self._cache[key]

        last = self.state.get(key, default_last)
        current = self.t[key]

        if not pd.isna(current):
            self[key] = current

        self._cache[key] = last, current
        return last, current
