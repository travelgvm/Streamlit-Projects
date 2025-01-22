import streamlit as st
import yfinance as yf
from viz import *
from get_data import *
from config import *
import plotly.graph_objects as go
import warnings
warnings.filterwarnings("ignore")

######################## LOAD DATA


def load_data():
    # MARKET BENCHMARKS INDEXS
    df_benchmarks = get_closing_prices(start_date='2020-01-01')

    # Residential property prices, Portugal, Quarterly vs EURO AREA
    df_hpi = get_residential_property_index_data(start_date='2000-01')

    # cppi pt anual
    df_cppi_pt = get_pt_cppi_annual_data_v2(start_year=2000)

    # cppi euro area 18 quarterly
    df_cppi_euro = get_euroarea18_cppi_annual_data(start_date='2000-01')
    df_aux_cppi = df_cppi_euro.copy()
    df_aux_cppi['Year'] = df_aux_cppi['Date'].dt.year
    df_aux_cppi = df_aux_cppi.groupby('Year').mean().reset_index().drop(columns=['Date'])
    df_aux_cppi = df_aux_cppi.merge(df_cppi_pt, on='Year', how='outer').dropna()

    # FEAR & GREED INDEX
    df_greed_fear = get_fear_greed_index()

    # WARREN BUFFET INDEX
    df_warren_buff = get_warren_buffet(start_date='2016-01-01')
    df_warren_buff['Date'] = df_warren_buff['Date'].dt.to_timestamp()
    df_warren_buff['Date'] = pd.to_datetime(df_warren_buff['Date'])
    # VOLATILITY Index
    df_vix = get_vix_data()

    # inflation
    df_ipc_pt = extract_data_from_bank_pt(5721524, 'Inflation')
    df_ipc_pt['Date'] = pd.to_datetime(df_ipc_pt['Date'])
    df_ipc_pt = df_ipc_pt[df_ipc_pt['Date'] >= '2000-01-01']

    # bonds
    df_bonds_pt = get_bonds_data('pt')
    df_bonds_es = get_bonds_data('es')
    df_bonds_ger = get_bonds_data('ger')
    df_bonds_euro = get_data_bonds_euro_area(start_date='2020-01')
    df_all_bonds = get_all_bonds_data().dropna()

    # cds
    df_cds_us = get_cds_data('us')
    df_cds_es = get_cds_data('es')
    df_cds_ger = get_cds_data('ger')
    df_all_cds = df_cds_us.merge(df_cds_es, on='Date', how='outer').merge(df_cds_ger, on='Date', how='outer')
    df_all_cds['Date'] = pd.to_datetime(df_all_cds['Date'], format='%d-%m-%Y')
    df_all_cds['Date'] = df_all_cds['Date'].dt.strftime('%Y-%m-%d')
    df_all_cds = df_all_cds.sort_values(by='Date')

    # EURIBOR
    df_eur = extract_euribors('2020-01')

    # SOFR
    df_sofr = extract_daily_ts_from_fred('SOFR', 'SOFR', observation_start='2020-01-01').dropna() #KEY SOFRINDEX

    # IPC USA
    # df_ipc_usa = get_us_annual_inflation_data(start_date='2000-01-01')

    # FX EUR vs USD
    df_fx_eur_usd = get_exchange_rate_from_yf('EUR', 'USD', start_date='2020-01-01', end_date=None)
    df_fx_eur_gbp = get_exchange_rate_from_yf('EUR', 'GBP', start_date='2020-01-01', end_date=None)
    df_fx = df_fx_eur_usd.merge(df_fx_eur_gbp, on='Date', how='outer')

    # KEY ECB IR (deposit facility & refinancing)
    df_key_ecb_ir = get_key_ecb_ir(start_year=2015)

    # IR STR
    df_ir_str = extract_data_from_bank_pt(12559714, 'IR STR') # retirar estatisticas do site
    df_ir_str['Date'] = pd.to_datetime(df_ir_str['Date'])
    df_ir_str = df_ir_str[df_ir_str['Date'] >= '2000-01-01']

    return df_benchmarks, df_hpi, df_aux_cppi, df_greed_fear, df_warren_buff, df_vix, df_ipc_pt, df_all_bonds, df_all_cds, df_eur, df_sofr, df_fx, df_key_ecb_ir, df_ir_str