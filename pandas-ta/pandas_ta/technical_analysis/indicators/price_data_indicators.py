from __future__ import annotations

import pandas as pd

from pandas_df_commons.indexing import get_columns
from pandas_df_commons.indexing.decorators import for_each_column, for_each_top_level_row, for_each_top_level_column, rename_with_parameters
import tulipy


@for_each_top_level_row
@for_each_top_level_column
def ta_apo(df: pd.DataFrame | pd.Series, short_period, long_period,  real='Close',  **kwargs) -> pd.DataFrame:
    """
    Absolute Price Oscillator (indicator)
    """
    
    data = get_columns(df, [real, ]) if [real, ][0] is not None and df.ndim > 1 else df  

    @for_each_column
    @rename_with_parameters(function_name='apo', parameter_names=['short_period', 'long_period'], output_names=['apo'])
    def wrapped_ta_apo(data, short_period, long_period, ):
        # result gets converted by rename_with_parameters to DataFrame
        columns = data.columns.tolist() if data.ndim > 1 else [data.name]
        values = data.values.astype('float64')
        return columns, tulipy.apo(values.copy(order='C'), short_period, long_period, )
    
    return wrapped_ta_apo(data, short_period, long_period, )
        

@for_each_top_level_row
@for_each_top_level_column
def ta_bbands(df: pd.DataFrame | pd.Series, period, stddev,  real='Close',  **kwargs) -> pd.DataFrame:
    """
    Bollinger Bands (overlay)
    """
    
    data = get_columns(df, [real, ]) if [real, ][0] is not None and df.ndim > 1 else df  

    @for_each_column
    @rename_with_parameters(function_name='bbands', parameter_names=['period', 'stddev'], output_names=['bbands_lower', 'bbands_middle', 'bbands_upper'])
    def wrapped_ta_bbands(data, period, stddev, ):
        # result gets converted by rename_with_parameters to DataFrame
        columns = data.columns.tolist() if data.ndim > 1 else [data.name]
        values = data.values.astype('float64')
        return columns, tulipy.bbands(values.copy(order='C'), period, stddev, )
    
    return wrapped_ta_bbands(data, period, stddev, )
        

@for_each_top_level_row
@for_each_top_level_column
def ta_cmo(df: pd.DataFrame | pd.Series, period,  real='Close',  **kwargs) -> pd.DataFrame:
    """
    Chande Momentum Oscillator (indicator)
    """
    
    data = get_columns(df, [real, ]) if [real, ][0] is not None and df.ndim > 1 else df  

    @for_each_column
    @rename_with_parameters(function_name='cmo', parameter_names=['period'], output_names=['cmo'])
    def wrapped_ta_cmo(data, period, ):
        # result gets converted by rename_with_parameters to DataFrame
        columns = data.columns.tolist() if data.ndim > 1 else [data.name]
        values = data.values.astype('float64')
        return columns, tulipy.cmo(values.copy(order='C'), period, )
    
    return wrapped_ta_cmo(data, period, )
        

@for_each_top_level_row
@for_each_top_level_column
def ta_decay(df: pd.DataFrame | pd.Series, period,  real='Close',  **kwargs) -> pd.DataFrame:
    """
    Linear Decay (math)
    """
    
    data = get_columns(df, [real, ]) if [real, ][0] is not None and df.ndim > 1 else df  

    @for_each_column
    @rename_with_parameters(function_name='decay', parameter_names=['period'], output_names=['decay'])
    def wrapped_ta_decay(data, period, ):
        # result gets converted by rename_with_parameters to DataFrame
        columns = data.columns.tolist() if data.ndim > 1 else [data.name]
        values = data.values.astype('float64')
        return columns, tulipy.decay(values.copy(order='C'), period, )
    
    return wrapped_ta_decay(data, period, )
        

@for_each_top_level_row
@for_each_top_level_column
def ta_dema(df: pd.DataFrame | pd.Series, period,  real='Close',  **kwargs) -> pd.DataFrame:
    """
    Double Exponential Moving Average (overlay)
    """
    
    data = get_columns(df, [real, ]) if [real, ][0] is not None and df.ndim > 1 else df  

    @for_each_column
    @rename_with_parameters(function_name='dema', parameter_names=['period'], output_names=['dema'])
    def wrapped_ta_dema(data, period, ):
        # result gets converted by rename_with_parameters to DataFrame
        columns = data.columns.tolist() if data.ndim > 1 else [data.name]
        values = data.values.astype('float64')
        return columns, tulipy.dema(values.copy(order='C'), period, )
    
    return wrapped_ta_dema(data, period, )
        

@for_each_top_level_row
@for_each_top_level_column
def ta_dpo(df: pd.DataFrame | pd.Series, period,  real='Close',  **kwargs) -> pd.DataFrame:
    """
    Detrended Price Oscillator (indicator)
    """
    
    data = get_columns(df, [real, ]) if [real, ][0] is not None and df.ndim > 1 else df  

    @for_each_column
    @rename_with_parameters(function_name='dpo', parameter_names=['period'], output_names=['dpo'])
    def wrapped_ta_dpo(data, period, ):
        # result gets converted by rename_with_parameters to DataFrame
        columns = data.columns.tolist() if data.ndim > 1 else [data.name]
        values = data.values.astype('float64')
        return columns, tulipy.dpo(values.copy(order='C'), period, )
    
    return wrapped_ta_dpo(data, period, )
        

@for_each_top_level_row
@for_each_top_level_column
def ta_edecay(df: pd.DataFrame | pd.Series, period,  real='Close',  **kwargs) -> pd.DataFrame:
    """
    Exponential Decay (math)
    """
    
    data = get_columns(df, [real, ]) if [real, ][0] is not None and df.ndim > 1 else df  

    @for_each_column
    @rename_with_parameters(function_name='edecay', parameter_names=['period'], output_names=['edecay'])
    def wrapped_ta_edecay(data, period, ):
        # result gets converted by rename_with_parameters to DataFrame
        columns = data.columns.tolist() if data.ndim > 1 else [data.name]
        values = data.values.astype('float64')
        return columns, tulipy.edecay(values.copy(order='C'), period, )
    
    return wrapped_ta_edecay(data, period, )
        

@for_each_top_level_row
@for_each_top_level_column
def ta_ema(df: pd.DataFrame | pd.Series, period,  real='Close',  **kwargs) -> pd.DataFrame:
    """
    Exponential Moving Average (overlay)
    """
    
    data = get_columns(df, [real, ]) if [real, ][0] is not None and df.ndim > 1 else df  

    @for_each_column
    @rename_with_parameters(function_name='ema', parameter_names=['period'], output_names=['ema'])
    def wrapped_ta_ema(data, period, ):
        # result gets converted by rename_with_parameters to DataFrame
        columns = data.columns.tolist() if data.ndim > 1 else [data.name]
        values = data.values.astype('float64')
        return columns, tulipy.ema(values.copy(order='C'), period, )
    
    return wrapped_ta_ema(data, period, )
        

@for_each_top_level_row
@for_each_top_level_column
def ta_fosc(df: pd.DataFrame | pd.Series, period,  real='Close',  **kwargs) -> pd.DataFrame:
    """
    Forecast Oscillator (indicator)
    """
    
    data = get_columns(df, [real, ]) if [real, ][0] is not None and df.ndim > 1 else df  

    @for_each_column
    @rename_with_parameters(function_name='fosc', parameter_names=['period'], output_names=['fosc'])
    def wrapped_ta_fosc(data, period, ):
        # result gets converted by rename_with_parameters to DataFrame
        columns = data.columns.tolist() if data.ndim > 1 else [data.name]
        values = data.values.astype('float64')
        return columns, tulipy.fosc(values.copy(order='C'), period, )
    
    return wrapped_ta_fosc(data, period, )
        

@for_each_top_level_row
@for_each_top_level_column
def ta_hma(df: pd.DataFrame | pd.Series, period,  real='Close',  **kwargs) -> pd.DataFrame:
    """
    Hull Moving Average (overlay)
    """
    
    data = get_columns(df, [real, ]) if [real, ][0] is not None and df.ndim > 1 else df  

    @for_each_column
    @rename_with_parameters(function_name='hma', parameter_names=['period'], output_names=['hma'])
    def wrapped_ta_hma(data, period, ):
        # result gets converted by rename_with_parameters to DataFrame
        columns = data.columns.tolist() if data.ndim > 1 else [data.name]
        values = data.values.astype('float64')
        return columns, tulipy.hma(values.copy(order='C'), period, )
    
    return wrapped_ta_hma(data, period, )
        

@for_each_top_level_row
@for_each_top_level_column
def ta_kama(df: pd.DataFrame | pd.Series, period,  real='Close',  **kwargs) -> pd.DataFrame:
    """
    Kaufman Adaptive Moving Average (overlay)
    """
    
    data = get_columns(df, [real, ]) if [real, ][0] is not None and df.ndim > 1 else df  

    @for_each_column
    @rename_with_parameters(function_name='kama', parameter_names=['period'], output_names=['kama'])
    def wrapped_ta_kama(data, period, ):
        # result gets converted by rename_with_parameters to DataFrame
        columns = data.columns.tolist() if data.ndim > 1 else [data.name]
        values = data.values.astype('float64')
        return columns, tulipy.kama(values.copy(order='C'), period, )
    
    return wrapped_ta_kama(data, period, )
        

@for_each_top_level_row
@for_each_top_level_column
def ta_lag(df: pd.DataFrame | pd.Series, period,  real='Close',  **kwargs) -> pd.DataFrame:
    """
    Lag (math)
    """
    
    data = get_columns(df, [real, ]) if [real, ][0] is not None and df.ndim > 1 else df  

    @for_each_column
    @rename_with_parameters(function_name='lag', parameter_names=['period'], output_names=['lag'])
    def wrapped_ta_lag(data, period, ):
        # result gets converted by rename_with_parameters to DataFrame
        columns = data.columns.tolist() if data.ndim > 1 else [data.name]
        values = data.values.astype('float64')
        return columns, tulipy.lag(values.copy(order='C'), period, )
    
    return wrapped_ta_lag(data, period, )
        

@for_each_top_level_row
@for_each_top_level_column
def ta_linreg(df: pd.DataFrame | pd.Series, period,  real='Close',  **kwargs) -> pd.DataFrame:
    """
    Linear Regression (overlay)
    """
    
    data = get_columns(df, [real, ]) if [real, ][0] is not None and df.ndim > 1 else df  

    @for_each_column
    @rename_with_parameters(function_name='linreg', parameter_names=['period'], output_names=['linreg'])
    def wrapped_ta_linreg(data, period, ):
        # result gets converted by rename_with_parameters to DataFrame
        columns = data.columns.tolist() if data.ndim > 1 else [data.name]
        values = data.values.astype('float64')
        return columns, tulipy.linreg(values.copy(order='C'), period, )
    
    return wrapped_ta_linreg(data, period, )
        

@for_each_top_level_row
@for_each_top_level_column
def ta_linregintercept(df: pd.DataFrame | pd.Series, period,  real='Close',  **kwargs) -> pd.DataFrame:
    """
    Linear Regression Intercept (indicator)
    """
    
    data = get_columns(df, [real, ]) if [real, ][0] is not None and df.ndim > 1 else df  

    @for_each_column
    @rename_with_parameters(function_name='linregintercept', parameter_names=['period'], output_names=['linregintercept'])
    def wrapped_ta_linregintercept(data, period, ):
        # result gets converted by rename_with_parameters to DataFrame
        columns = data.columns.tolist() if data.ndim > 1 else [data.name]
        values = data.values.astype('float64')
        return columns, tulipy.linregintercept(values.copy(order='C'), period, )
    
    return wrapped_ta_linregintercept(data, period, )
        

@for_each_top_level_row
@for_each_top_level_column
def ta_linregslope(df: pd.DataFrame | pd.Series, period,  real='Close',  **kwargs) -> pd.DataFrame:
    """
    Linear Regression Slope (indicator)
    """
    
    data = get_columns(df, [real, ]) if [real, ][0] is not None and df.ndim > 1 else df  

    @for_each_column
    @rename_with_parameters(function_name='linregslope', parameter_names=['period'], output_names=['linregslope'])
    def wrapped_ta_linregslope(data, period, ):
        # result gets converted by rename_with_parameters to DataFrame
        columns = data.columns.tolist() if data.ndim > 1 else [data.name]
        values = data.values.astype('float64')
        return columns, tulipy.linregslope(values.copy(order='C'), period, )
    
    return wrapped_ta_linregslope(data, period, )
        

@for_each_top_level_row
@for_each_top_level_column
def ta_macd(df: pd.DataFrame | pd.Series, short_period, long_period, signal_period,  real='Close',  **kwargs) -> pd.DataFrame:
    """
    Moving Average Convergence/Divergence (indicator)
    """
    
    data = get_columns(df, [real, ]) if [real, ][0] is not None and df.ndim > 1 else df  

    @for_each_column
    @rename_with_parameters(function_name='macd', parameter_names=['short_period', 'long_period', 'signal_period'], output_names=['macd', 'macd_signal', 'macd_histogram'])
    def wrapped_ta_macd(data, short_period, long_period, signal_period, ):
        # result gets converted by rename_with_parameters to DataFrame
        columns = data.columns.tolist() if data.ndim > 1 else [data.name]
        values = data.values.astype('float64')
        return columns, tulipy.macd(values.copy(order='C'), short_period, long_period, signal_period, )
    
    return wrapped_ta_macd(data, short_period, long_period, signal_period, )
        

@for_each_top_level_row
@for_each_top_level_column
def ta_max(df: pd.DataFrame | pd.Series, period,  real='Close',  **kwargs) -> pd.DataFrame:
    """
    Maximum In Period (math)
    """
    
    data = get_columns(df, [real, ]) if [real, ][0] is not None and df.ndim > 1 else df  

    @for_each_column
    @rename_with_parameters(function_name='max', parameter_names=['period'], output_names=['max'])
    def wrapped_ta_max(data, period, ):
        # result gets converted by rename_with_parameters to DataFrame
        columns = data.columns.tolist() if data.ndim > 1 else [data.name]
        values = data.values.astype('float64')
        return columns, tulipy.max(values.copy(order='C'), period, )
    
    return wrapped_ta_max(data, period, )
        

@for_each_top_level_row
@for_each_top_level_column
def ta_md(df: pd.DataFrame | pd.Series, period,  real='Close',  **kwargs) -> pd.DataFrame:
    """
    Mean Deviation Over Period (math)
    """
    
    data = get_columns(df, [real, ]) if [real, ][0] is not None and df.ndim > 1 else df  

    @for_each_column
    @rename_with_parameters(function_name='md', parameter_names=['period'], output_names=['md'])
    def wrapped_ta_md(data, period, ):
        # result gets converted by rename_with_parameters to DataFrame
        columns = data.columns.tolist() if data.ndim > 1 else [data.name]
        values = data.values.astype('float64')
        return columns, tulipy.md(values.copy(order='C'), period, )
    
    return wrapped_ta_md(data, period, )
        

@for_each_top_level_row
@for_each_top_level_column
def ta_min(df: pd.DataFrame | pd.Series, period,  real='Close',  **kwargs) -> pd.DataFrame:
    """
    Minimum In Period (math)
    """
    
    data = get_columns(df, [real, ]) if [real, ][0] is not None and df.ndim > 1 else df  

    @for_each_column
    @rename_with_parameters(function_name='min', parameter_names=['period'], output_names=['min'])
    def wrapped_ta_min(data, period, ):
        # result gets converted by rename_with_parameters to DataFrame
        columns = data.columns.tolist() if data.ndim > 1 else [data.name]
        values = data.values.astype('float64')
        return columns, tulipy.min(values.copy(order='C'), period, )
    
    return wrapped_ta_min(data, period, )
        

@for_each_top_level_row
@for_each_top_level_column
def ta_mom(df: pd.DataFrame | pd.Series, period,  real='Close',  **kwargs) -> pd.DataFrame:
    """
    Momentum (indicator)
    """
    
    data = get_columns(df, [real, ]) if [real, ][0] is not None and df.ndim > 1 else df  

    @for_each_column
    @rename_with_parameters(function_name='mom', parameter_names=['period'], output_names=['mom'])
    def wrapped_ta_mom(data, period, ):
        # result gets converted by rename_with_parameters to DataFrame
        columns = data.columns.tolist() if data.ndim > 1 else [data.name]
        values = data.values.astype('float64')
        return columns, tulipy.mom(values.copy(order='C'), period, )
    
    return wrapped_ta_mom(data, period, )
        

@for_each_top_level_row
@for_each_top_level_column
def ta_msw(df: pd.DataFrame | pd.Series, period,  real='Close',  **kwargs) -> pd.DataFrame:
    """
    Mesa Sine Wave (indicator)
    """
    
    data = get_columns(df, [real, ]) if [real, ][0] is not None and df.ndim > 1 else df  

    @for_each_column
    @rename_with_parameters(function_name='msw', parameter_names=['period'], output_names=['msw_sine', 'msw_lead'])
    def wrapped_ta_msw(data, period, ):
        # result gets converted by rename_with_parameters to DataFrame
        columns = data.columns.tolist() if data.ndim > 1 else [data.name]
        values = data.values.astype('float64')
        return columns, tulipy.msw(values.copy(order='C'), period, )
    
    return wrapped_ta_msw(data, period, )
        

@for_each_top_level_row
@for_each_top_level_column
def ta_ppo(df: pd.DataFrame | pd.Series, short_period, long_period,  real='Close',  **kwargs) -> pd.DataFrame:
    """
    Percentage Price Oscillator (indicator)
    """
    
    data = get_columns(df, [real, ]) if [real, ][0] is not None and df.ndim > 1 else df  

    @for_each_column
    @rename_with_parameters(function_name='ppo', parameter_names=['short_period', 'long_period'], output_names=['ppo'])
    def wrapped_ta_ppo(data, short_period, long_period, ):
        # result gets converted by rename_with_parameters to DataFrame
        columns = data.columns.tolist() if data.ndim > 1 else [data.name]
        values = data.values.astype('float64')
        return columns, tulipy.ppo(values.copy(order='C'), short_period, long_period, )
    
    return wrapped_ta_ppo(data, short_period, long_period, )
        

@for_each_top_level_row
@for_each_top_level_column
def ta_roc(df: pd.DataFrame | pd.Series, period,  real='Close',  **kwargs) -> pd.DataFrame:
    """
    Rate of Change (indicator)
    """
    
    data = get_columns(df, [real, ]) if [real, ][0] is not None and df.ndim > 1 else df  

    @for_each_column
    @rename_with_parameters(function_name='roc', parameter_names=['period'], output_names=['roc'])
    def wrapped_ta_roc(data, period, ):
        # result gets converted by rename_with_parameters to DataFrame
        columns = data.columns.tolist() if data.ndim > 1 else [data.name]
        values = data.values.astype('float64')
        return columns, tulipy.roc(values.copy(order='C'), period, )
    
    return wrapped_ta_roc(data, period, )
        

@for_each_top_level_row
@for_each_top_level_column
def ta_rocr(df: pd.DataFrame | pd.Series, period,  real='Close',  **kwargs) -> pd.DataFrame:
    """
    Rate of Change Ratio (indicator)
    """
    
    data = get_columns(df, [real, ]) if [real, ][0] is not None and df.ndim > 1 else df  

    @for_each_column
    @rename_with_parameters(function_name='rocr', parameter_names=['period'], output_names=['rocr'])
    def wrapped_ta_rocr(data, period, ):
        # result gets converted by rename_with_parameters to DataFrame
        columns = data.columns.tolist() if data.ndim > 1 else [data.name]
        values = data.values.astype('float64')
        return columns, tulipy.rocr(values.copy(order='C'), period, )
    
    return wrapped_ta_rocr(data, period, )
        

@for_each_top_level_row
@for_each_top_level_column
def ta_rsi(df: pd.DataFrame | pd.Series, period,  real='Close',  **kwargs) -> pd.DataFrame:
    """
    Relative Strength Index (indicator)
    """
    
    data = get_columns(df, [real, ]) if [real, ][0] is not None and df.ndim > 1 else df  

    @for_each_column
    @rename_with_parameters(function_name='rsi', parameter_names=['period'], output_names=['rsi'])
    def wrapped_ta_rsi(data, period, ):
        # result gets converted by rename_with_parameters to DataFrame
        columns = data.columns.tolist() if data.ndim > 1 else [data.name]
        values = data.values.astype('float64')
        return columns, tulipy.rsi(values.copy(order='C'), period, )
    
    return wrapped_ta_rsi(data, period, )
        

@for_each_top_level_row
@for_each_top_level_column
def ta_sma(df: pd.DataFrame | pd.Series, period,  real='Close',  **kwargs) -> pd.DataFrame:
    """
    Simple Moving Average (overlay)
    """
    
    data = get_columns(df, [real, ]) if [real, ][0] is not None and df.ndim > 1 else df  

    @for_each_column
    @rename_with_parameters(function_name='sma', parameter_names=['period'], output_names=['sma'])
    def wrapped_ta_sma(data, period, ):
        # result gets converted by rename_with_parameters to DataFrame
        columns = data.columns.tolist() if data.ndim > 1 else [data.name]
        values = data.values.astype('float64')
        return columns, tulipy.sma(values.copy(order='C'), period, )
    
    return wrapped_ta_sma(data, period, )
        

@for_each_top_level_row
@for_each_top_level_column
def ta_stddev(df: pd.DataFrame | pd.Series, period,  real='Close',  **kwargs) -> pd.DataFrame:
    """
    Standard Deviation Over Period (math)
    """
    
    data = get_columns(df, [real, ]) if [real, ][0] is not None and df.ndim > 1 else df  

    @for_each_column
    @rename_with_parameters(function_name='stddev', parameter_names=['period'], output_names=['stddev'])
    def wrapped_ta_stddev(data, period, ):
        # result gets converted by rename_with_parameters to DataFrame
        columns = data.columns.tolist() if data.ndim > 1 else [data.name]
        values = data.values.astype('float64')
        return columns, tulipy.stddev(values.copy(order='C'), period, )
    
    return wrapped_ta_stddev(data, period, )
        

@for_each_top_level_row
@for_each_top_level_column
def ta_stderr(df: pd.DataFrame | pd.Series, period,  real='Close',  **kwargs) -> pd.DataFrame:
    """
    Standard Error Over Period (math)
    """
    
    data = get_columns(df, [real, ]) if [real, ][0] is not None and df.ndim > 1 else df  

    @for_each_column
    @rename_with_parameters(function_name='stderr', parameter_names=['period'], output_names=['stderr'])
    def wrapped_ta_stderr(data, period, ):
        # result gets converted by rename_with_parameters to DataFrame
        columns = data.columns.tolist() if data.ndim > 1 else [data.name]
        values = data.values.astype('float64')
        return columns, tulipy.stderr(values.copy(order='C'), period, )
    
    return wrapped_ta_stderr(data, period, )
        

@for_each_top_level_row
@for_each_top_level_column
def ta_stochrsi(df: pd.DataFrame | pd.Series, period,  real='Close',  **kwargs) -> pd.DataFrame:
    """
    Stochastic RSI (indicator)
    """
    
    data = get_columns(df, [real, ]) if [real, ][0] is not None and df.ndim > 1 else df  

    @for_each_column
    @rename_with_parameters(function_name='stochrsi', parameter_names=['period'], output_names=['stochrsi'])
    def wrapped_ta_stochrsi(data, period, ):
        # result gets converted by rename_with_parameters to DataFrame
        columns = data.columns.tolist() if data.ndim > 1 else [data.name]
        values = data.values.astype('float64')
        return columns, tulipy.stochrsi(values.copy(order='C'), period, )
    
    return wrapped_ta_stochrsi(data, period, )
        

@for_each_top_level_row
@for_each_top_level_column
def ta_sum(df: pd.DataFrame | pd.Series, period,  real='Close',  **kwargs) -> pd.DataFrame:
    """
    Sum Over Period (math)
    """
    
    data = get_columns(df, [real, ]) if [real, ][0] is not None and df.ndim > 1 else df  

    @for_each_column
    @rename_with_parameters(function_name='sum', parameter_names=['period'], output_names=['sum'])
    def wrapped_ta_sum(data, period, ):
        # result gets converted by rename_with_parameters to DataFrame
        columns = data.columns.tolist() if data.ndim > 1 else [data.name]
        values = data.values.astype('float64')
        return columns, tulipy.sum(values.copy(order='C'), period, )
    
    return wrapped_ta_sum(data, period, )
        

@for_each_top_level_row
@for_each_top_level_column
def ta_tema(df: pd.DataFrame | pd.Series, period,  real='Close',  **kwargs) -> pd.DataFrame:
    """
    Triple Exponential Moving Average (overlay)
    """
    
    data = get_columns(df, [real, ]) if [real, ][0] is not None and df.ndim > 1 else df  

    @for_each_column
    @rename_with_parameters(function_name='tema', parameter_names=['period'], output_names=['tema'])
    def wrapped_ta_tema(data, period, ):
        # result gets converted by rename_with_parameters to DataFrame
        columns = data.columns.tolist() if data.ndim > 1 else [data.name]
        values = data.values.astype('float64')
        return columns, tulipy.tema(values.copy(order='C'), period, )
    
    return wrapped_ta_tema(data, period, )
        

@for_each_top_level_row
@for_each_top_level_column
def ta_trima(df: pd.DataFrame | pd.Series, period,  real='Close',  **kwargs) -> pd.DataFrame:
    """
    Triangular Moving Average (overlay)
    """
    
    data = get_columns(df, [real, ]) if [real, ][0] is not None and df.ndim > 1 else df  

    @for_each_column
    @rename_with_parameters(function_name='trima', parameter_names=['period'], output_names=['trima'])
    def wrapped_ta_trima(data, period, ):
        # result gets converted by rename_with_parameters to DataFrame
        columns = data.columns.tolist() if data.ndim > 1 else [data.name]
        values = data.values.astype('float64')
        return columns, tulipy.trima(values.copy(order='C'), period, )
    
    return wrapped_ta_trima(data, period, )
        

@for_each_top_level_row
@for_each_top_level_column
def ta_trix(df: pd.DataFrame | pd.Series, period,  real='Close',  **kwargs) -> pd.DataFrame:
    """
    Trix (indicator)
    """
    
    data = get_columns(df, [real, ]) if [real, ][0] is not None and df.ndim > 1 else df  

    @for_each_column
    @rename_with_parameters(function_name='trix', parameter_names=['period'], output_names=['trix'])
    def wrapped_ta_trix(data, period, ):
        # result gets converted by rename_with_parameters to DataFrame
        columns = data.columns.tolist() if data.ndim > 1 else [data.name]
        values = data.values.astype('float64')
        return columns, tulipy.trix(values.copy(order='C'), period, )
    
    return wrapped_ta_trix(data, period, )
        

@for_each_top_level_row
@for_each_top_level_column
def ta_tsf(df: pd.DataFrame | pd.Series, period,  real='Close',  **kwargs) -> pd.DataFrame:
    """
    Time Series Forecast (overlay)
    """
    
    data = get_columns(df, [real, ]) if [real, ][0] is not None and df.ndim > 1 else df  

    @for_each_column
    @rename_with_parameters(function_name='tsf', parameter_names=['period'], output_names=['tsf'])
    def wrapped_ta_tsf(data, period, ):
        # result gets converted by rename_with_parameters to DataFrame
        columns = data.columns.tolist() if data.ndim > 1 else [data.name]
        values = data.values.astype('float64')
        return columns, tulipy.tsf(values.copy(order='C'), period, )
    
    return wrapped_ta_tsf(data, period, )
        

@for_each_top_level_row
@for_each_top_level_column
def ta_var(df: pd.DataFrame | pd.Series, period,  real='Close',  **kwargs) -> pd.DataFrame:
    """
    Variance Over Period (math)
    """
    
    data = get_columns(df, [real, ]) if [real, ][0] is not None and df.ndim > 1 else df  

    @for_each_column
    @rename_with_parameters(function_name='var', parameter_names=['period'], output_names=['var'])
    def wrapped_ta_var(data, period, ):
        # result gets converted by rename_with_parameters to DataFrame
        columns = data.columns.tolist() if data.ndim > 1 else [data.name]
        values = data.values.astype('float64')
        return columns, tulipy.var(values.copy(order='C'), period, )
    
    return wrapped_ta_var(data, period, )
        

@for_each_top_level_row
@for_each_top_level_column
def ta_vhf(df: pd.DataFrame | pd.Series, period,  real='Close',  **kwargs) -> pd.DataFrame:
    """
    Vertical Horizontal Filter (indicator)
    """
    
    data = get_columns(df, [real, ]) if [real, ][0] is not None and df.ndim > 1 else df  

    @for_each_column
    @rename_with_parameters(function_name='vhf', parameter_names=['period'], output_names=['vhf'])
    def wrapped_ta_vhf(data, period, ):
        # result gets converted by rename_with_parameters to DataFrame
        columns = data.columns.tolist() if data.ndim > 1 else [data.name]
        values = data.values.astype('float64')
        return columns, tulipy.vhf(values.copy(order='C'), period, )
    
    return wrapped_ta_vhf(data, period, )
        

@for_each_top_level_row
@for_each_top_level_column
def ta_vidya(df: pd.DataFrame | pd.Series, short_period, long_period, alpha,  real='Close',  **kwargs) -> pd.DataFrame:
    """
    Variable Index Dynamic Average (overlay)
    """
    
    data = get_columns(df, [real, ]) if [real, ][0] is not None and df.ndim > 1 else df  

    @for_each_column
    @rename_with_parameters(function_name='vidya', parameter_names=['short_period', 'long_period', 'alpha'], output_names=['vidya'])
    def wrapped_ta_vidya(data, short_period, long_period, alpha, ):
        # result gets converted by rename_with_parameters to DataFrame
        columns = data.columns.tolist() if data.ndim > 1 else [data.name]
        values = data.values.astype('float64')
        return columns, tulipy.vidya(values.copy(order='C'), short_period, long_period, alpha, )
    
    return wrapped_ta_vidya(data, short_period, long_period, alpha, )
        

@for_each_top_level_row
@for_each_top_level_column
def ta_volatility(df: pd.DataFrame | pd.Series, period,  real='Close',  **kwargs) -> pd.DataFrame:
    """
    Annualized Historical Volatility (indicator)
    """
    
    data = get_columns(df, [real, ]) if [real, ][0] is not None and df.ndim > 1 else df  

    @for_each_column
    @rename_with_parameters(function_name='volatility', parameter_names=['period'], output_names=['volatility'])
    def wrapped_ta_volatility(data, period, ):
        # result gets converted by rename_with_parameters to DataFrame
        columns = data.columns.tolist() if data.ndim > 1 else [data.name]
        values = data.values.astype('float64')
        return columns, tulipy.volatility(values.copy(order='C'), period, )
    
    return wrapped_ta_volatility(data, period, )
        

@for_each_top_level_row
@for_each_top_level_column
def ta_vosc(df: pd.DataFrame | pd.Series, short_period, long_period,  volume='Volume',  **kwargs) -> pd.DataFrame:
    """
    Volume Oscillator (indicator)
    """
    
    data = get_columns(df, [volume, ]) if [volume, ][0] is not None and df.ndim > 1 else df  

    @for_each_column
    @rename_with_parameters(function_name='vosc', parameter_names=['short_period', 'long_period'], output_names=['vosc'])
    def wrapped_ta_vosc(data, short_period, long_period, ):
        # result gets converted by rename_with_parameters to DataFrame
        columns = data.columns.tolist() if data.ndim > 1 else [data.name]
        values = data.values.astype('float64')
        return columns, tulipy.vosc(values.copy(order='C'), short_period, long_period, )
    
    return wrapped_ta_vosc(data, short_period, long_period, )
        

@for_each_top_level_row
@for_each_top_level_column
def ta_wilders(df: pd.DataFrame | pd.Series, period,  real='Close',  **kwargs) -> pd.DataFrame:
    """
    Wilders Smoothing (overlay)
    """
    
    data = get_columns(df, [real, ]) if [real, ][0] is not None and df.ndim > 1 else df  

    @for_each_column
    @rename_with_parameters(function_name='wilders', parameter_names=['period'], output_names=['wilders'])
    def wrapped_ta_wilders(data, period, ):
        # result gets converted by rename_with_parameters to DataFrame
        columns = data.columns.tolist() if data.ndim > 1 else [data.name]
        values = data.values.astype('float64')
        return columns, tulipy.wilders(values.copy(order='C'), period, )
    
    return wrapped_ta_wilders(data, period, )
        

@for_each_top_level_row
@for_each_top_level_column
def ta_wma(df: pd.DataFrame | pd.Series, period,  real='Close',  **kwargs) -> pd.DataFrame:
    """
    Weighted Moving Average (overlay)
    """
    
    data = get_columns(df, [real, ]) if [real, ][0] is not None and df.ndim > 1 else df  

    @for_each_column
    @rename_with_parameters(function_name='wma', parameter_names=['period'], output_names=['wma'])
    def wrapped_ta_wma(data, period, ):
        # result gets converted by rename_with_parameters to DataFrame
        columns = data.columns.tolist() if data.ndim > 1 else [data.name]
        values = data.values.astype('float64')
        return columns, tulipy.wma(values.copy(order='C'), period, )
    
    return wrapped_ta_wma(data, period, )
        

@for_each_top_level_row
@for_each_top_level_column
def ta_zlema(df: pd.DataFrame | pd.Series, period,  real='Close',  **kwargs) -> pd.DataFrame:
    """
    Zero-Lag Exponential Moving Average (overlay)
    """
    
    data = get_columns(df, [real, ]) if [real, ][0] is not None and df.ndim > 1 else df  

    @for_each_column
    @rename_with_parameters(function_name='zlema', parameter_names=['period'], output_names=['zlema'])
    def wrapped_ta_zlema(data, period, ):
        # result gets converted by rename_with_parameters to DataFrame
        columns = data.columns.tolist() if data.ndim > 1 else [data.name]
        values = data.values.astype('float64')
        return columns, tulipy.zlema(values.copy(order='C'), period, )
    
    return wrapped_ta_zlema(data, period, )
        
