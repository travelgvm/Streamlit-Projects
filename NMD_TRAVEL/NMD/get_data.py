import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup
import yfinance as yf
from ecbdata import ecbdata
from pyjstat import pyjstat
from io import BytesIO
import requests
from io import StringIO
from config import *

import warnings
warnings.filterwarnings("ignore")


def get_nmd_data():
    df = pd.read_excel(path_nmd,
                       sheet_name='Dados').drop(columns=['Unnamed: 0', 'PT', 'PT 1 MÊS LAG', 'Evolução Euribor GVM'])
    df['Date'] = pd.to_datetime(df['Date'], format='%Y-%m-%d')
    return df


def get_raw_data():
    raw_df = get_nmd_data().copy()
    raw_df['Date'] = raw_df['Date'].dt.strftime('%Y-%m-%d')
    return raw_df


def convert_df_to_excel(df):

    output = BytesIO()

    with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
        df.to_excel(writer, index=False, sheet_name='Sheet1')

        workbook = writer.book
        worksheet = writer.sheets['Sheet1']

        for idx, col in enumerate(df.columns):
            max_len = max(df[col].astype(str).map(len).max() + 2, len(col) + 2) # Calcula o tamanho máximo da coluna + padding
            worksheet.set_column(idx, idx, max_len)  # Define a largura de cada coluna

        # Formatar o cabeçalho (linha das colunas)
        header_format = workbook.add_format({
            'bold': True,
            'text_wrap': True,
            'font_color': '#FFFFFF',
            'valign': 'center',
            'align': 'center',
            'fg_color': default_color1,
            'border': 1
        })

        cell_format = workbook.add_format({
            'align': 'center',
            'valign': 'vcenter',
        })

        for col_num, value in enumerate(df.columns.values):
            worksheet.write(0, col_num, value, header_format)

        for row_num in range(1, len(df) + 1):
            worksheet.set_row(row_num, None, cell_format)

    output.seek(0)
    return output