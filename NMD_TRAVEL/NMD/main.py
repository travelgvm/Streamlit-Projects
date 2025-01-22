import streamlit as st
#from obiwan import *
from viz import *
from get_data import *
from config import *
import warnings
warnings.filterwarnings("ignore")
from datetime import datetime
import datetime
from xlsxwriter import Workbook
from datetime import timedelta
import requests
import streamlit.components.v1 as components

#################################################### BUILD DASHBOARD ############################################

st.set_page_config(page_title=dashboard_main_title, layout="wide")
st.markdown(f"<h1 style='color:{default_color1};'>{dashboard_main_title}</h1>", unsafe_allow_html=True)

st.sidebar.markdown(f'<a><img src="{travel_logo_url}" alt="Logo" style="width: 100%;"></a>', unsafe_allow_html=True)

df_nmd = get_nmd_data()
raw_df = get_raw_data()

numeric_columns = df_nmd.select_dtypes(include=['number']).columns.tolist()

# Data range
min_date = df_nmd['Date'].min().date()
max_date = df_nmd['Date'].max().date()

st.sidebar.header("Select index:")
indicador = st.sidebar.selectbox(
    "Choose an indicator to analyse:", sidebar_indicators
)

default_start_date = max_date - timedelta(days=365*5)
default_end_date = max_date

if indicador == "Correlation matrix analysis":
    st.markdown(f"<div style='text-align: center;'><h2>Correlation Matrix Analysis</h2></div>", unsafe_allow_html=True)

    start_date, end_date = st.slider(
        'Select the date range',
        min_value=min_date,
        max_value=max_date,
        value=(default_start_date, default_end_date),
        format="YYYY-MM-DD"
    )

    selected_columns = st.multiselect(
        'Select columns for correlation matrix',
        options=numeric_columns,
        default=corr_default_columns,
        label_visibility="visible",
        help="Press Ctrl to select more than one column",
        key='selected_columns',
    )

    if st.button('Generate Correlation Matrix'):
        plot_interact_corr_matrix(df_nmd, start_date, end_date, selected_columns)

elif indicador == "Raw data":
    st.markdown(f"<h6 style='color:{default_color1};'>Raw data</h6>", unsafe_allow_html=True)
    st.dataframe(raw_df, hide_index=True)
    st.download_button(label="Download in xlsx format",
                       data=convert_df_to_excel(raw_df),
                       file_name='NMD.xlsx',
                       mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')

if indicador == "Interactive Plots":
    st.write("Choose columns for interactive time evolution plot:")

    type = st.selectbox(
        "Choose an indicator to analyse:",
        ('Interest rates', 'Notionals')
    )

    if type == "Interest rates":

        selected_columns = st.multiselect(
            'Select columns to plot',
            options=interest_rate_cols,
            default=['Taxa de juro (TAA) do stock de depósitos à ordem dos particulares',
                     'Taxa de juro (TAA) do stock de depósitos a prazo dos particulares', 'Euribor 3M'])
    elif type == "Notionals":
        cols = notional_cols

        selected_columns = st.multiselect(
            'Select columns to plot',
            options=cols,
            default=[
                'Montante de novos depósitos a prazo dos particulares',
                'Montante de novos depósitos a prazo das empresas não financeiras',
                'Responsabilidades à vista-Particulares-PRT-M€ (OIFM)',
                'Responsabilidades à vista-SNF-PRT-M€ (OIFM)',
                'Dívida direta do Estado - certificados de aforro'])

    if selected_columns:
        selected_columns.insert(0, 'Date')
        plot_interactive_graph(df_nmd[selected_columns])


if indicador == "Dual Axis Interactive Plots":
    st.write("Choose columns for interactive dual-axis time evolution plot:")

    type1 = st.selectbox(
        "Choose an indicator for the left y-axis (Interest rates):",
        ('Interest rates',)
    )

    type2 = st.selectbox(
        "Choose an indicator for the right y-axis (Notionals):",
        ('Notionals',)
    )

    selected_interest_columns = st.multiselect(
        'Select columns for the left y-axis (Interest rates)',
        options=interest_rate_cols,
        default=['Taxa de juro (TAA) do stock de depósitos à ordem dos particulares',
                 'Euribor 3M']
    )

    selected_notional_columns = st.multiselect(
        'Select columns for the right y-axis (Notionals)',
        options=notional_cols,
        default=['Montante de novos depósitos a prazo dos particulares',
                 'Responsabilidades à vista-Particulares-PRT-M€ (OIFM)']
    )

    if selected_interest_columns and selected_notional_columns:
        selected_interest_columns.insert(0, 'Date')  # Garantir que 'Date' esteja presente
        selected_notional_columns.insert(0, 'Date')
        plot_dual_axis_graph(df_nmd[selected_interest_columns], df_nmd[selected_notional_columns])


elif indicador == "Deposits prediction challenge":

    st.write(notebooks_str1)

    #html_file1 = path_ts_notebook

    #with open(html_file1, 'r', encoding='utf-8') as f:
    #    html_content1 = f.read()

    html_content1 = requests.get(path_ts_notebook).text   

    st.title('Challenges using Holt-Winters and ARIMA')

    components.html(html_content1, height=800, scrolling=True)

    #html_file2 = path_ts_notebook1

    #with open(html_file2, 'r', encoding='utf-8') as i:
    #    html_content2 = i.read()

    html_content2 = requests.get(path_ts_notebook1).text 
    
    st.title('Challenges using LSTM and Prophet')

    st.write(notebooks_str2)

    components.html(html_content2, height=800, scrolling=True)
