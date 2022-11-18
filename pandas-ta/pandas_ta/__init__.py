"""Augment pandas DataFrame with methods for technical quant analysis"""
__version__ = open(f"{__file__.replace('__init__.py', '')}VERSION").read()


class _TA(object):

    def __init__(self, df):
        from pandas_ta import technical_analysis as ta
        from functools import partial, wraps

        self.df = df

        for name, func in ta.__dict__.items():
            if name.startswith("ta_"):
                self.__dict__[name[3:]] = wraps(func)(partial(func, self.df))


def monkey_patch_dataframe(extender='ta'):
    from pandas.core.base import PandasObject

    existing = getattr(PandasObject, extender, None)
    if existing is not None:
        if not isinstance(existing.fget(None), _TA):
            raise ValueError(f"field already exists as {type(existing)}")

    setattr(PandasObject, extender, property(lambda self: _TA(self)))
