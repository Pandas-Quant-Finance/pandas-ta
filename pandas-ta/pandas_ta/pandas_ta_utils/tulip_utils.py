import os.path

import tulipy as ti
from string import Template

default_values = {
    "acos":  [],
    "ad":  [],
    "add":  [],
    "adosc":  [3, 10],
    "adx":  [14],
    "adxr":  [14],
    "apo":  [12, 26],
    "aroon":  [14],
    "aroonosc":  [14],
    "asin":  [],
    "atan":  [],
    "atr":  [14],
    "avgprice":  [],
    "bbands":  [5, 2.0],
    "bop":  [],
    "cci":  [14],
    "ceil":  [],
    "cmo":  [14],
    "cos":  [],
    "cosh":  [],
    "dema":  [30],
    "div":  [],
    "dx":  [14],
    "ema":  [30],
    "exp":  [],
    "floor":  [],
    "kama":  [30],
    "ln":  [],
    "log10":  [],
    "macd":  [12, 26, 9],
    "max":  [30],
    "medprice":  [],
    "mfi":  [14],
    "min":  [30],
    "mom":  [10],
    "natr":  [14],
    "obv":  [],
    "ppo":  [12, 26],
    "roc":  [10],
    "rocr":  [10],
    "rsi":  [14],
    "sin":  [],
    "sinh":  [],
    "sma":  [30],
    "sqrt":  [],
    "stddev":  [5],
    "stochrsi":  [14],
    "sub":  [],
    "sum":  [30],
    "tan":  [],
    "tanh":  [],
    "tema":  [30],
    "trima":  [30],
    "trix":  [30],
    "tsf":  [14],
    "typprice":  [],
    "ultosc":  [7, 14, 28],
    "var":  [5],
    "willr":  [14],
}

prolog = '''from __future__ import annotations

import pandas as pd

from pandas_df_commons.indexing import get_columns
from pandas_df_commons.indexing.decorators import foreach_column, foreach_top_level_row_and_column,\
 rename_with_parameters

import tulipy

'''

test_prolog='''
from unittest import TestCase

from config import DF_TEST_MULTI_ROW_MULTI_COLUMN as DF_TEST
from pandas_ta.technical_analysis import *


class TestIndicator(TestCase):
'''

bar_template = Template('''
@foreach_top_level_row_and_column(parallel=True)
@rename_with_parameters(function_name='$name', parameter_names=[$parameter_names], output_names=[$output_names])
def ta_$name(df: pd.DataFrame, $parameters $inputs **kwargs) -> pd.DataFrame:
    """
    $fullname ($type)
    """
    
    data = get_columns(df, [$tulip_inputs])
    
    # result gets converted by rename_with_parameters to DataFrame
    columns = data.columns.tolist()
    values = data.values.astype('float64')
    if values.ndim > 1: 
        return columns, tulipy.$name(*[values[:, i].copy(order='C') for i in range(values.shape[1])], $tulip_options)
    else:
        return columns, tulipy.$name(values.copy(order='C'), $tulip_options)

''')

price_template = Template('''
@foreach_top_level_row_and_column(parallel=False)
def ta_$name(df: pd.DataFrame | pd.Series, $parameters $inputs **kwargs) -> pd.DataFrame:
    """
    $fullname ($type)
    """
    
    data = get_columns(df, [$tulip_inputs]) if [$tulip_inputs][0] is not None and df.ndim > 1 else df  

    @foreach_column
    @rename_with_parameters(function_name='$name', parameter_names=[$parameter_names], output_names=[$output_names])
    def wrapped_ta_$name(data, $parameters):
        # result gets converted by rename_with_parameters to DataFrame
        columns = data.columns.tolist() if data.ndim > 1 else [data.name]
        values = data.values.astype('float64')
        return columns, tulipy.$name(values.copy(order='C'), $tulip_options)
    
    return wrapped_ta_$name(data, $parameters)
        
''')

test_template = Template('''
    def test_ta_$name(self):
        df = ta_$name(DF_TEST, *$parameter_defaults)
        pd.testing.assert_frame_equal(df.loc["A"], df.loc["B"])
''')


def create_wrapper_source_code():
    indicators = discover_indicators()

    bar_indicators = {name: desc for name, desc in indicators.items() if desc["target_module"] != "price" and desc["type"] != "math"}
    write_source_file(
        os.path.join(os.path.dirname(__file__), "..", "technical_analysis", "indicators", "bar_data_indicators.py"),
        os.path.join(os.path.dirname(__file__), "..", "..", "..", "test-pandas-ta", "test_pandas_ta", "indicators", "test_ta_bar_indicators.py"),
        bar_indicators,
        bar_template,
    )

    price_indicators = {name: desc for name, desc in indicators.items() if desc["target_module"] == "price"}
    write_source_file(
        os.path.join(os.path.dirname(__file__), "..", "technical_analysis", "indicators", "price_data_indicators.py"),
        os.path.join(os.path.dirname(__file__), "..", "..", "..", "test-pandas-ta", "test_pandas_ta", "indicators", "test_ta_price_indicators.py"),
        price_indicators,
        price_template,
    )


def write_source_file(filename, test_filename, indicators, template):
    with open(filename, "w") as f:
        with open(test_filename, "w") as tf:

            f.write(prolog)
            tf.write(test_prolog)

            for name, desc in indicators.items():
                inputs = ""
                tulip_inputs = ""
                parameters = ""
                tulip_options = ""

                for p in desc['options']:
                    parameters += f"{p}, "
                    tulip_options += f"{p}={p}, "

                for i in desc['inputs']:
                    if i in ['open', 'high', 'low', 'close', 'volume']:
                        inputs += f"{i}='{i.capitalize()}', "
                        tulip_inputs += f"{i}, "
                    else:
                        inputs += f"{i}=None, " if len(desc['inputs']) > 1 else f"{i}='Close', "
                        tulip_inputs += f"{i}, "

                f.write(
                    template.substitute(
                        name=name,
                        type=desc['type'],
                        fullname=desc['name'],
                        parameters=parameters,
                        inputs=inputs,
                        tulip_inputs=tulip_inputs,
                        tulip_options=parameters,
                        parameter_names=f"""'{"', '".join(desc['options'])}'""" if len(desc['options']) > 0 else "",
                        output_names=f"""'{"', '".join(desc['outputs'])}'""" if len(desc['outputs']) > 0 else "",
                    )
                )

                if desc["default_values"] is not None:
                    tf.write(
                        test_template.substitute(
                            name=name,
                            type=desc['type'],
                            parameter_defaults=desc["default_values"],
                        )
                    )


def discover_indicators():
    all_indicators = {name: get_info(func) for name, func in ti.__dict__.items() if hasattr(func, 'full_name')}
    indicators = {name: desc for name, desc in all_indicators.items() if desc["type"] != 'simple'}
    return indicators


def get_info(indicator):

    inp, tmp = [], []
    for i in indicator.inputs:
        tmp.append(i)
        if i in inp:
            inp.append(f"{i}{tmp.count(i)-1}")
        else:
            inp.append(i)

    return {
        "type": indicator.type,
        "name": indicator.full_name,
        "inputs": inp,
        "options": [o.replace(" ", "_").replace("%", "") for o in indicator.options],
        "default_values": default_values.get(indicator.__name__, None),
        "outputs": [o.replace(" ", "_") for o in indicator.outputs],
        "target_module": "price" if len(indicator.inputs) == 1 else "bar"
    }


if __name__ == '__main__':
    x = ti.macd
    create_wrapper_source_code()
