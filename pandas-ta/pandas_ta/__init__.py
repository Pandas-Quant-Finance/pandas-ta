"""Augment pandas DataFrame with methods for technical quant analysis"""
__version__ = open(f"{__file__.replace('__init__.py', '')}VERSION").read()

from functools import partial as _partial

from pandas_df_commons._utils.patching import _monkey_patch_dataframe, _add_functions


_TA = _add_functions('pandas_ta.technical_analysis', filter=lambda _, x: x[3:] if x.startswith("ta_") else None)
monkey_patch_dataframe = _partial(_monkey_patch_dataframe, extension_default_value='ta', extension_class=_TA)


_current_module = __import__(__name__)
for name, func in _TA._functions.items():
    setattr(_current_module, name, func)
