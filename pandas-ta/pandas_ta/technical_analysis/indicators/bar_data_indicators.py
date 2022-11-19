from __future__ import annotations

import pandas as pd

from pandas_df_commons.indexing import get_columns
from pandas_df_commons.indexing.decorators import foreach_column, foreach_top_level_row_and_column, rename_with_parameters

import tulipy


@foreach_top_level_row_and_column(parallel=True)
@rename_with_parameters(function_name='ad', parameter_names=[], output_names=['ad'])
def ta_ad(df: pd.DataFrame,  high='High', low='Low', close='Close', volume='Volume',  **kwargs) -> pd.DataFrame:
    """
    Accumulation/Distribution Line (indicator)
    """
    
    data = get_columns(df, [high, low, close, volume, ])
    
    # result gets converted by rename_with_parameters to DataFrame
    columns = data.columns.tolist()
    values = data.values.astype('float64')
    if values.ndim > 1: 
        return columns, tulipy.ad(*[values[:, i].copy(order='C') for i in range(values.shape[1])], )
    else:
        return columns, tulipy.ad(values.copy(order='C'), )


@foreach_top_level_row_and_column(parallel=True)
@rename_with_parameters(function_name='adosc', parameter_names=['short_period', 'long_period'], output_names=['adosc'])
def ta_adosc(df: pd.DataFrame, short_period, long_period,  high='High', low='Low', close='Close', volume='Volume',  **kwargs) -> pd.DataFrame:
    """
    Accumulation/Distribution Oscillator (indicator)
    """
    
    data = get_columns(df, [high, low, close, volume, ])
    
    # result gets converted by rename_with_parameters to DataFrame
    columns = data.columns.tolist()
    values = data.values.astype('float64')
    if values.ndim > 1: 
        return columns, tulipy.adosc(*[values[:, i].copy(order='C') for i in range(values.shape[1])], short_period, long_period, )
    else:
        return columns, tulipy.adosc(values.copy(order='C'), short_period, long_period, )


@foreach_top_level_row_and_column(parallel=True)
@rename_with_parameters(function_name='adx', parameter_names=['period'], output_names=['dx'])
def ta_adx(df: pd.DataFrame, period,  high='High', low='Low', close='Close',  **kwargs) -> pd.DataFrame:
    """
    Average Directional Movement Index (indicator)
    """
    
    data = get_columns(df, [high, low, close, ])
    
    # result gets converted by rename_with_parameters to DataFrame
    columns = data.columns.tolist()
    values = data.values.astype('float64')
    if values.ndim > 1: 
        return columns, tulipy.adx(*[values[:, i].copy(order='C') for i in range(values.shape[1])], period, )
    else:
        return columns, tulipy.adx(values.copy(order='C'), period, )


@foreach_top_level_row_and_column(parallel=True)
@rename_with_parameters(function_name='adxr', parameter_names=['period'], output_names=['dx'])
def ta_adxr(df: pd.DataFrame, period,  high='High', low='Low', close='Close',  **kwargs) -> pd.DataFrame:
    """
    Average Directional Movement Rating (indicator)
    """
    
    data = get_columns(df, [high, low, close, ])
    
    # result gets converted by rename_with_parameters to DataFrame
    columns = data.columns.tolist()
    values = data.values.astype('float64')
    if values.ndim > 1: 
        return columns, tulipy.adxr(*[values[:, i].copy(order='C') for i in range(values.shape[1])], period, )
    else:
        return columns, tulipy.adxr(values.copy(order='C'), period, )


@foreach_top_level_row_and_column(parallel=True)
@rename_with_parameters(function_name='ao', parameter_names=[], output_names=['ao'])
def ta_ao(df: pd.DataFrame,  high='High', low='Low',  **kwargs) -> pd.DataFrame:
    """
    Awesome Oscillator (indicator)
    """
    
    data = get_columns(df, [high, low, ])
    
    # result gets converted by rename_with_parameters to DataFrame
    columns = data.columns.tolist()
    values = data.values.astype('float64')
    if values.ndim > 1: 
        return columns, tulipy.ao(*[values[:, i].copy(order='C') for i in range(values.shape[1])], )
    else:
        return columns, tulipy.ao(values.copy(order='C'), )


@foreach_top_level_row_and_column(parallel=True)
@rename_with_parameters(function_name='aroon', parameter_names=['period'], output_names=['aroon_down', 'aroon_up'])
def ta_aroon(df: pd.DataFrame, period,  high='High', low='Low',  **kwargs) -> pd.DataFrame:
    """
    Aroon (indicator)
    """
    
    data = get_columns(df, [high, low, ])
    
    # result gets converted by rename_with_parameters to DataFrame
    columns = data.columns.tolist()
    values = data.values.astype('float64')
    if values.ndim > 1: 
        return columns, tulipy.aroon(*[values[:, i].copy(order='C') for i in range(values.shape[1])], period, )
    else:
        return columns, tulipy.aroon(values.copy(order='C'), period, )


@foreach_top_level_row_and_column(parallel=True)
@rename_with_parameters(function_name='aroonosc', parameter_names=['period'], output_names=['aroonosc'])
def ta_aroonosc(df: pd.DataFrame, period,  high='High', low='Low',  **kwargs) -> pd.DataFrame:
    """
    Aroon Oscillator (indicator)
    """
    
    data = get_columns(df, [high, low, ])
    
    # result gets converted by rename_with_parameters to DataFrame
    columns = data.columns.tolist()
    values = data.values.astype('float64')
    if values.ndim > 1: 
        return columns, tulipy.aroonosc(*[values[:, i].copy(order='C') for i in range(values.shape[1])], period, )
    else:
        return columns, tulipy.aroonosc(values.copy(order='C'), period, )


@foreach_top_level_row_and_column(parallel=True)
@rename_with_parameters(function_name='atr', parameter_names=['period'], output_names=['atr'])
def ta_atr(df: pd.DataFrame, period,  high='High', low='Low', close='Close',  **kwargs) -> pd.DataFrame:
    """
    Average True Range (indicator)
    """
    
    data = get_columns(df, [high, low, close, ])
    
    # result gets converted by rename_with_parameters to DataFrame
    columns = data.columns.tolist()
    values = data.values.astype('float64')
    if values.ndim > 1: 
        return columns, tulipy.atr(*[values[:, i].copy(order='C') for i in range(values.shape[1])], period, )
    else:
        return columns, tulipy.atr(values.copy(order='C'), period, )


@foreach_top_level_row_and_column(parallel=True)
@rename_with_parameters(function_name='avgprice', parameter_names=[], output_names=['avgprice'])
def ta_avgprice(df: pd.DataFrame,  open='Open', high='High', low='Low', close='Close',  **kwargs) -> pd.DataFrame:
    """
    Average Price (overlay)
    """
    
    data = get_columns(df, [open, high, low, close, ])
    
    # result gets converted by rename_with_parameters to DataFrame
    columns = data.columns.tolist()
    values = data.values.astype('float64')
    if values.ndim > 1: 
        return columns, tulipy.avgprice(*[values[:, i].copy(order='C') for i in range(values.shape[1])], )
    else:
        return columns, tulipy.avgprice(values.copy(order='C'), )


@foreach_top_level_row_and_column(parallel=True)
@rename_with_parameters(function_name='bop', parameter_names=[], output_names=['bop'])
def ta_bop(df: pd.DataFrame,  open='Open', high='High', low='Low', close='Close',  **kwargs) -> pd.DataFrame:
    """
    Balance of Power (indicator)
    """
    
    data = get_columns(df, [open, high, low, close, ])
    
    # result gets converted by rename_with_parameters to DataFrame
    columns = data.columns.tolist()
    values = data.values.astype('float64')
    if values.ndim > 1: 
        return columns, tulipy.bop(*[values[:, i].copy(order='C') for i in range(values.shape[1])], )
    else:
        return columns, tulipy.bop(values.copy(order='C'), )


@foreach_top_level_row_and_column(parallel=True)
@rename_with_parameters(function_name='cci', parameter_names=['period'], output_names=['cci'])
def ta_cci(df: pd.DataFrame, period,  high='High', low='Low', close='Close',  **kwargs) -> pd.DataFrame:
    """
    Commodity Channel Index (indicator)
    """
    
    data = get_columns(df, [high, low, close, ])
    
    # result gets converted by rename_with_parameters to DataFrame
    columns = data.columns.tolist()
    values = data.values.astype('float64')
    if values.ndim > 1: 
        return columns, tulipy.cci(*[values[:, i].copy(order='C') for i in range(values.shape[1])], period, )
    else:
        return columns, tulipy.cci(values.copy(order='C'), period, )


@foreach_top_level_row_and_column(parallel=True)
@rename_with_parameters(function_name='cvi', parameter_names=['period'], output_names=['cvi'])
def ta_cvi(df: pd.DataFrame, period,  high='High', low='Low',  **kwargs) -> pd.DataFrame:
    """
    Chaikins Volatility (indicator)
    """
    
    data = get_columns(df, [high, low, ])
    
    # result gets converted by rename_with_parameters to DataFrame
    columns = data.columns.tolist()
    values = data.values.astype('float64')
    if values.ndim > 1: 
        return columns, tulipy.cvi(*[values[:, i].copy(order='C') for i in range(values.shape[1])], period, )
    else:
        return columns, tulipy.cvi(values.copy(order='C'), period, )


@foreach_top_level_row_and_column(parallel=True)
@rename_with_parameters(function_name='di', parameter_names=['period'], output_names=['plus_di', 'minus_di'])
def ta_di(df: pd.DataFrame, period,  high='High', low='Low', close='Close',  **kwargs) -> pd.DataFrame:
    """
    Directional Indicator (indicator)
    """
    
    data = get_columns(df, [high, low, close, ])
    
    # result gets converted by rename_with_parameters to DataFrame
    columns = data.columns.tolist()
    values = data.values.astype('float64')
    if values.ndim > 1: 
        return columns, tulipy.di(*[values[:, i].copy(order='C') for i in range(values.shape[1])], period, )
    else:
        return columns, tulipy.di(values.copy(order='C'), period, )


@foreach_top_level_row_and_column(parallel=True)
@rename_with_parameters(function_name='dm', parameter_names=['period'], output_names=['plus_dm', 'minus_dm'])
def ta_dm(df: pd.DataFrame, period,  high='High', low='Low',  **kwargs) -> pd.DataFrame:
    """
    Directional Movement (indicator)
    """
    
    data = get_columns(df, [high, low, ])
    
    # result gets converted by rename_with_parameters to DataFrame
    columns = data.columns.tolist()
    values = data.values.astype('float64')
    if values.ndim > 1: 
        return columns, tulipy.dm(*[values[:, i].copy(order='C') for i in range(values.shape[1])], period, )
    else:
        return columns, tulipy.dm(values.copy(order='C'), period, )


@foreach_top_level_row_and_column(parallel=True)
@rename_with_parameters(function_name='dx', parameter_names=['period'], output_names=['dx'])
def ta_dx(df: pd.DataFrame, period,  high='High', low='Low', close='Close',  **kwargs) -> pd.DataFrame:
    """
    Directional Movement Index (indicator)
    """
    
    data = get_columns(df, [high, low, close, ])
    
    # result gets converted by rename_with_parameters to DataFrame
    columns = data.columns.tolist()
    values = data.values.astype('float64')
    if values.ndim > 1: 
        return columns, tulipy.dx(*[values[:, i].copy(order='C') for i in range(values.shape[1])], period, )
    else:
        return columns, tulipy.dx(values.copy(order='C'), period, )


@foreach_top_level_row_and_column(parallel=True)
@rename_with_parameters(function_name='emv', parameter_names=[], output_names=['emv'])
def ta_emv(df: pd.DataFrame,  high='High', low='Low', volume='Volume',  **kwargs) -> pd.DataFrame:
    """
    Ease of Movement (indicator)
    """
    
    data = get_columns(df, [high, low, volume, ])
    
    # result gets converted by rename_with_parameters to DataFrame
    columns = data.columns.tolist()
    values = data.values.astype('float64')
    if values.ndim > 1: 
        return columns, tulipy.emv(*[values[:, i].copy(order='C') for i in range(values.shape[1])], )
    else:
        return columns, tulipy.emv(values.copy(order='C'), )


@foreach_top_level_row_and_column(parallel=True)
@rename_with_parameters(function_name='fisher', parameter_names=['period'], output_names=['fisher', 'fisher_signal'])
def ta_fisher(df: pd.DataFrame, period,  high='High', low='Low',  **kwargs) -> pd.DataFrame:
    """
    Fisher Transform (indicator)
    """
    
    data = get_columns(df, [high, low, ])
    
    # result gets converted by rename_with_parameters to DataFrame
    columns = data.columns.tolist()
    values = data.values.astype('float64')
    if values.ndim > 1: 
        return columns, tulipy.fisher(*[values[:, i].copy(order='C') for i in range(values.shape[1])], period, )
    else:
        return columns, tulipy.fisher(values.copy(order='C'), period, )


@foreach_top_level_row_and_column(parallel=True)
@rename_with_parameters(function_name='kvo', parameter_names=['short_period', 'long_period'], output_names=['kvo'])
def ta_kvo(df: pd.DataFrame, short_period, long_period,  high='High', low='Low', close='Close', volume='Volume',  **kwargs) -> pd.DataFrame:
    """
    Klinger Volume Oscillator (indicator)
    """
    
    data = get_columns(df, [high, low, close, volume, ])
    
    # result gets converted by rename_with_parameters to DataFrame
    columns = data.columns.tolist()
    values = data.values.astype('float64')
    if values.ndim > 1: 
        return columns, tulipy.kvo(*[values[:, i].copy(order='C') for i in range(values.shape[1])], short_period, long_period, )
    else:
        return columns, tulipy.kvo(values.copy(order='C'), short_period, long_period, )


@foreach_top_level_row_and_column(parallel=True)
@rename_with_parameters(function_name='marketfi', parameter_names=[], output_names=['marketfi'])
def ta_marketfi(df: pd.DataFrame,  high='High', low='Low', volume='Volume',  **kwargs) -> pd.DataFrame:
    """
    Market Facilitation Index (indicator)
    """
    
    data = get_columns(df, [high, low, volume, ])
    
    # result gets converted by rename_with_parameters to DataFrame
    columns = data.columns.tolist()
    values = data.values.astype('float64')
    if values.ndim > 1: 
        return columns, tulipy.marketfi(*[values[:, i].copy(order='C') for i in range(values.shape[1])], )
    else:
        return columns, tulipy.marketfi(values.copy(order='C'), )


@foreach_top_level_row_and_column(parallel=True)
@rename_with_parameters(function_name='mass', parameter_names=['period'], output_names=['mass'])
def ta_mass(df: pd.DataFrame, period,  high='High', low='Low',  **kwargs) -> pd.DataFrame:
    """
    Mass Index (indicator)
    """
    
    data = get_columns(df, [high, low, ])
    
    # result gets converted by rename_with_parameters to DataFrame
    columns = data.columns.tolist()
    values = data.values.astype('float64')
    if values.ndim > 1: 
        return columns, tulipy.mass(*[values[:, i].copy(order='C') for i in range(values.shape[1])], period, )
    else:
        return columns, tulipy.mass(values.copy(order='C'), period, )


@foreach_top_level_row_and_column(parallel=True)
@rename_with_parameters(function_name='medprice', parameter_names=[], output_names=['medprice'])
def ta_medprice(df: pd.DataFrame,  high='High', low='Low',  **kwargs) -> pd.DataFrame:
    """
    Median Price (overlay)
    """
    
    data = get_columns(df, [high, low, ])
    
    # result gets converted by rename_with_parameters to DataFrame
    columns = data.columns.tolist()
    values = data.values.astype('float64')
    if values.ndim > 1: 
        return columns, tulipy.medprice(*[values[:, i].copy(order='C') for i in range(values.shape[1])], )
    else:
        return columns, tulipy.medprice(values.copy(order='C'), )


@foreach_top_level_row_and_column(parallel=True)
@rename_with_parameters(function_name='mfi', parameter_names=['period'], output_names=['mfi'])
def ta_mfi(df: pd.DataFrame, period,  high='High', low='Low', close='Close', volume='Volume',  **kwargs) -> pd.DataFrame:
    """
    Money Flow Index (indicator)
    """
    
    data = get_columns(df, [high, low, close, volume, ])
    
    # result gets converted by rename_with_parameters to DataFrame
    columns = data.columns.tolist()
    values = data.values.astype('float64')
    if values.ndim > 1: 
        return columns, tulipy.mfi(*[values[:, i].copy(order='C') for i in range(values.shape[1])], period, )
    else:
        return columns, tulipy.mfi(values.copy(order='C'), period, )


@foreach_top_level_row_and_column(parallel=True)
@rename_with_parameters(function_name='natr', parameter_names=['period'], output_names=['natr'])
def ta_natr(df: pd.DataFrame, period,  high='High', low='Low', close='Close',  **kwargs) -> pd.DataFrame:
    """
    Normalized Average True Range (indicator)
    """
    
    data = get_columns(df, [high, low, close, ])
    
    # result gets converted by rename_with_parameters to DataFrame
    columns = data.columns.tolist()
    values = data.values.astype('float64')
    if values.ndim > 1: 
        return columns, tulipy.natr(*[values[:, i].copy(order='C') for i in range(values.shape[1])], period, )
    else:
        return columns, tulipy.natr(values.copy(order='C'), period, )


@foreach_top_level_row_and_column(parallel=True)
@rename_with_parameters(function_name='nvi', parameter_names=[], output_names=['nvi'])
def ta_nvi(df: pd.DataFrame,  close='Close', volume='Volume',  **kwargs) -> pd.DataFrame:
    """
    Negative Volume Index (indicator)
    """
    
    data = get_columns(df, [close, volume, ])
    
    # result gets converted by rename_with_parameters to DataFrame
    columns = data.columns.tolist()
    values = data.values.astype('float64')
    if values.ndim > 1: 
        return columns, tulipy.nvi(*[values[:, i].copy(order='C') for i in range(values.shape[1])], )
    else:
        return columns, tulipy.nvi(values.copy(order='C'), )


@foreach_top_level_row_and_column(parallel=True)
@rename_with_parameters(function_name='obv', parameter_names=[], output_names=['obv'])
def ta_obv(df: pd.DataFrame,  close='Close', volume='Volume',  **kwargs) -> pd.DataFrame:
    """
    On Balance Volume (indicator)
    """
    
    data = get_columns(df, [close, volume, ])
    
    # result gets converted by rename_with_parameters to DataFrame
    columns = data.columns.tolist()
    values = data.values.astype('float64')
    if values.ndim > 1: 
        return columns, tulipy.obv(*[values[:, i].copy(order='C') for i in range(values.shape[1])], )
    else:
        return columns, tulipy.obv(values.copy(order='C'), )


@foreach_top_level_row_and_column(parallel=True)
@rename_with_parameters(function_name='psar', parameter_names=['acceleration_factor_step', 'acceleration_factor_maximum'], output_names=['psar'])
def ta_psar(df: pd.DataFrame, acceleration_factor_step, acceleration_factor_maximum,  high='High', low='Low',  **kwargs) -> pd.DataFrame:
    """
    Parabolic SAR (overlay)
    """
    
    data = get_columns(df, [high, low, ])
    
    # result gets converted by rename_with_parameters to DataFrame
    columns = data.columns.tolist()
    values = data.values.astype('float64')
    if values.ndim > 1: 
        return columns, tulipy.psar(*[values[:, i].copy(order='C') for i in range(values.shape[1])], acceleration_factor_step, acceleration_factor_maximum, )
    else:
        return columns, tulipy.psar(values.copy(order='C'), acceleration_factor_step, acceleration_factor_maximum, )


@foreach_top_level_row_and_column(parallel=True)
@rename_with_parameters(function_name='pvi', parameter_names=[], output_names=['pvi'])
def ta_pvi(df: pd.DataFrame,  close='Close', volume='Volume',  **kwargs) -> pd.DataFrame:
    """
    Positive Volume Index (indicator)
    """
    
    data = get_columns(df, [close, volume, ])
    
    # result gets converted by rename_with_parameters to DataFrame
    columns = data.columns.tolist()
    values = data.values.astype('float64')
    if values.ndim > 1: 
        return columns, tulipy.pvi(*[values[:, i].copy(order='C') for i in range(values.shape[1])], )
    else:
        return columns, tulipy.pvi(values.copy(order='C'), )


@foreach_top_level_row_and_column(parallel=True)
@rename_with_parameters(function_name='qstick', parameter_names=['period'], output_names=['qstick'])
def ta_qstick(df: pd.DataFrame, period,  open='Open', close='Close',  **kwargs) -> pd.DataFrame:
    """
    Qstick (indicator)
    """
    
    data = get_columns(df, [open, close, ])
    
    # result gets converted by rename_with_parameters to DataFrame
    columns = data.columns.tolist()
    values = data.values.astype('float64')
    if values.ndim > 1: 
        return columns, tulipy.qstick(*[values[:, i].copy(order='C') for i in range(values.shape[1])], period, )
    else:
        return columns, tulipy.qstick(values.copy(order='C'), period, )


@foreach_top_level_row_and_column(parallel=True)
@rename_with_parameters(function_name='stoch', parameter_names=['k_period', 'k_slowing_period', 'd_period'], output_names=['stoch_k', 'stoch_d'])
def ta_stoch(df: pd.DataFrame, k_period, k_slowing_period, d_period,  high='High', low='Low', close='Close',  **kwargs) -> pd.DataFrame:
    """
    Stochastic Oscillator (indicator)
    """
    
    data = get_columns(df, [high, low, close, ])
    
    # result gets converted by rename_with_parameters to DataFrame
    columns = data.columns.tolist()
    values = data.values.astype('float64')
    if values.ndim > 1: 
        return columns, tulipy.stoch(*[values[:, i].copy(order='C') for i in range(values.shape[1])], k_period, k_slowing_period, d_period, )
    else:
        return columns, tulipy.stoch(values.copy(order='C'), k_period, k_slowing_period, d_period, )


@foreach_top_level_row_and_column(parallel=True)
@rename_with_parameters(function_name='tr', parameter_names=[], output_names=['tr'])
def ta_tr(df: pd.DataFrame,  high='High', low='Low', close='Close',  **kwargs) -> pd.DataFrame:
    """
    True Range (indicator)
    """
    
    data = get_columns(df, [high, low, close, ])
    
    # result gets converted by rename_with_parameters to DataFrame
    columns = data.columns.tolist()
    values = data.values.astype('float64')
    if values.ndim > 1: 
        return columns, tulipy.tr(*[values[:, i].copy(order='C') for i in range(values.shape[1])], )
    else:
        return columns, tulipy.tr(values.copy(order='C'), )


@foreach_top_level_row_and_column(parallel=True)
@rename_with_parameters(function_name='typprice', parameter_names=[], output_names=['typprice'])
def ta_typprice(df: pd.DataFrame,  high='High', low='Low', close='Close',  **kwargs) -> pd.DataFrame:
    """
    Typical Price (overlay)
    """
    
    data = get_columns(df, [high, low, close, ])
    
    # result gets converted by rename_with_parameters to DataFrame
    columns = data.columns.tolist()
    values = data.values.astype('float64')
    if values.ndim > 1: 
        return columns, tulipy.typprice(*[values[:, i].copy(order='C') for i in range(values.shape[1])], )
    else:
        return columns, tulipy.typprice(values.copy(order='C'), )


@foreach_top_level_row_and_column(parallel=True)
@rename_with_parameters(function_name='ultosc', parameter_names=['short_period', 'medium_period', 'long_period'], output_names=['ultosc'])
def ta_ultosc(df: pd.DataFrame, short_period, medium_period, long_period,  high='High', low='Low', close='Close',  **kwargs) -> pd.DataFrame:
    """
    Ultimate Oscillator (indicator)
    """
    
    data = get_columns(df, [high, low, close, ])
    
    # result gets converted by rename_with_parameters to DataFrame
    columns = data.columns.tolist()
    values = data.values.astype('float64')
    if values.ndim > 1: 
        return columns, tulipy.ultosc(*[values[:, i].copy(order='C') for i in range(values.shape[1])], short_period, medium_period, long_period, )
    else:
        return columns, tulipy.ultosc(values.copy(order='C'), short_period, medium_period, long_period, )


@foreach_top_level_row_and_column(parallel=True)
@rename_with_parameters(function_name='vwma', parameter_names=['period'], output_names=['vwma'])
def ta_vwma(df: pd.DataFrame, period,  close='Close', volume='Volume',  **kwargs) -> pd.DataFrame:
    """
    Volume Weighted Moving Average (overlay)
    """
    
    data = get_columns(df, [close, volume, ])
    
    # result gets converted by rename_with_parameters to DataFrame
    columns = data.columns.tolist()
    values = data.values.astype('float64')
    if values.ndim > 1: 
        return columns, tulipy.vwma(*[values[:, i].copy(order='C') for i in range(values.shape[1])], period, )
    else:
        return columns, tulipy.vwma(values.copy(order='C'), period, )


@foreach_top_level_row_and_column(parallel=True)
@rename_with_parameters(function_name='wad', parameter_names=[], output_names=['wad'])
def ta_wad(df: pd.DataFrame,  high='High', low='Low', close='Close',  **kwargs) -> pd.DataFrame:
    """
    Williams Accumulation/Distribution (indicator)
    """
    
    data = get_columns(df, [high, low, close, ])
    
    # result gets converted by rename_with_parameters to DataFrame
    columns = data.columns.tolist()
    values = data.values.astype('float64')
    if values.ndim > 1: 
        return columns, tulipy.wad(*[values[:, i].copy(order='C') for i in range(values.shape[1])], )
    else:
        return columns, tulipy.wad(values.copy(order='C'), )


@foreach_top_level_row_and_column(parallel=True)
@rename_with_parameters(function_name='wcprice', parameter_names=[], output_names=['wcprice'])
def ta_wcprice(df: pd.DataFrame,  high='High', low='Low', close='Close',  **kwargs) -> pd.DataFrame:
    """
    Weighted Close Price (overlay)
    """
    
    data = get_columns(df, [high, low, close, ])
    
    # result gets converted by rename_with_parameters to DataFrame
    columns = data.columns.tolist()
    values = data.values.astype('float64')
    if values.ndim > 1: 
        return columns, tulipy.wcprice(*[values[:, i].copy(order='C') for i in range(values.shape[1])], )
    else:
        return columns, tulipy.wcprice(values.copy(order='C'), )


@foreach_top_level_row_and_column(parallel=True)
@rename_with_parameters(function_name='willr', parameter_names=['period'], output_names=['willr'])
def ta_willr(df: pd.DataFrame, period,  high='High', low='Low', close='Close',  **kwargs) -> pd.DataFrame:
    """
    Williams %R (indicator)
    """
    
    data = get_columns(df, [high, low, close, ])
    
    # result gets converted by rename_with_parameters to DataFrame
    columns = data.columns.tolist()
    values = data.values.astype('float64')
    if values.ndim > 1: 
        return columns, tulipy.willr(*[values[:, i].copy(order='C') for i in range(values.shape[1])], period, )
    else:
        return columns, tulipy.willr(values.copy(order='C'), period, )

