import streamlit as st
from viz import *
from get_data import *
from config import *
from load_data import load_data
import warnings
warnings.filterwarnings("ignore")
from xlsxwriter import Workbook

@st.cache_data(ttl=3600)  # Atualiza os dados a cada 3600 segundos (1 hora)
def get_data_cached():
    return load_data()

#################################################### BUILD DASHBOARD ############################################

st.set_page_config(page_title=dashboard_main_title, layout="wide")
st.markdown(f"<h1 style='color:{default_color1};'>{dashboard_main_title}</h1>", unsafe_allow_html=True)

# white Logo
st.sidebar.markdown(f'<a><img src="{travel_logo_url}" alt="Logo" style="width: 100%;"></a>', unsafe_allow_html=True)

df_benchmarks, df_hpi, df_aux_cppi, df_greed_fear, df_warren_buff, df_vix, df_ipc_pt, df_all_bonds, df_all_cds, df_eur, df_sofr, df_fx, df_key_ecb_ir, df_ir_str = get_data_cached()

st.sidebar.header("Select index:")
indicador = st.sidebar.selectbox(
    "Choose an indicator to analyse:", sidebar_indicators
)

if indicador == "Fear & Greed Index":
    st.markdown(f"<div style='text-align: center;'><h2>Fear & Greed (CNN index)</h2></div>", unsafe_allow_html=True)
    if st.sidebar.checkbox("Show raw data"):
        st.markdown(f"<h6 style='color:{default_color1};'>Raw data</h6>", unsafe_allow_html=True)
        st.dataframe(df_greed_fear, hide_index=True)

        st.download_button(label="Download in xlsx format",
                           data=convert_df_to_excel(df_greed_fear),
                           file_name='greed_fear.xlsx',
                           mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')

    fear_greed_plot(df_greed_fear)

    plot_interactive_time_series(df_greed_fear[['Date', 'Rating']], option_to_choose_variables='no')

    if st.sidebar.checkbox("Show anomalies"):
        method = st.selectbox("Select anomaly detection method", options=["isolation_forest", "HMM", "zscore"])
        plot_anomalies(df_greed_fear, 'Rating', method)

    st.write("**Source:** https://edition.cnn.com/markets/fear-and-greed?utm_source=hp")
    st.markdown(fear_greed_str, unsafe_allow_html=True)

elif indicador == "Warren Buffett indicator - Marketcap to GDP":
    st.markdown(f"<div style='text-align: center;'><h2>Warren Buffett indicator - Marketcap to GDP</h2></div>", unsafe_allow_html=True)

    if st.sidebar.checkbox("Show raw data"):
        st.markdown(f"<h6 style='color:{default_color1};'>Raw data</h6>", unsafe_allow_html=True)
        st.dataframe(df_warren_buff, hide_index=True)

        st.download_button(label="Download in xlsx format",
                           data=convert_df_to_excel(df_warren_buff),
                           file_name='warren_buffett_index.xlsx',
                           mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')

    plot_interactive_time_series(df_warren_buff[['Date', 'Indicador de Warren Buffett (%)']], option_to_choose_variables='no')

    if st.sidebar.checkbox("Show anomalies"):
        method = st.selectbox("Select anomaly detection method", options=["isolation_forest", "HMM", "zscore"])
        plot_anomalies(df_warren_buff, 'Indicador de Warren Buffett (%)', method)

    #st.write("**Source:** https://edition.cnn.com/markets/fear-and-greed?utm_source=hp")
    st.markdown(warren_str, unsafe_allow_html=True)

elif indicador == "VIX":
    st.markdown(f"<div style='text-align: center;'><h2>VIX - Volatility index</h2></div>", unsafe_allow_html=True)

    if st.sidebar.checkbox("Show raw data"):
        st.markdown(f"<h6 style='color:{default_color1};'>Raw data</h6>", unsafe_allow_html=True)
        st.dataframe(df_vix, hide_index=True)

        st.download_button(label="Download in xlsx format",
                           data=convert_df_to_excel(df_vix),
                           file_name='vix.xlsx',
                           mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')

    plot_interactive_time_series(df_vix, option_to_choose_variables='no')

    if st.sidebar.checkbox("Show anomalies"):
        method = st.selectbox("Select anomaly detection method", options=["isolation_forest", "HMM", "zscore"])
        plot_anomalies(df_vix, 'VIX', method)

    st.write("**Source:** https://finance.yahoo.com/quote/%5EVIX/")
    st.markdown(vix_str, unsafe_allow_html=True)

elif indicador == "Benchmark Indexs":
    st.markdown(f"<div style='text-align: center;'><h2>Benchmark Indexs</h2></div>", unsafe_allow_html=True)

    if st.sidebar.checkbox("Show raw data"):
        st.markdown(f"<h6 style='color:{default_color1};'>Raw data</h6>", unsafe_allow_html=True)
        st.dataframe(df_benchmarks, hide_index=True)

        st.download_button(label="Download in xlsx format",
                           data=convert_df_to_excel(df_benchmarks),
                           file_name='benchmarks.xlsx',
                           mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')

    plot_interactive_time_series(df_benchmarks)
    correlation_matrix(df_benchmarks, "My Correlation Matrix")

    st.write("**Source:** Yahoo Finance")
    st.markdown(index_str, unsafe_allow_html=True)

    if st.sidebar.checkbox("Show anomalies"):
        column = st.selectbox("Select column to analyze anomalies", options=df_benchmarks.columns[1:], index=0)
        method = st.selectbox("Select anomaly detection method", options=["isolation_forest", "HMM", "zscore"])
        plot_anomalies(df_benchmarks, column, method)

elif indicador == "Euribor rates - 1M, 3M, 6M, 12M":
    st.markdown(f"<div style='text-align: center;'><h2>Euribor rates - 1M, 3M, 6M, 12M</h2></div>", unsafe_allow_html=True)

    if st.sidebar.checkbox("Show raw data"):
        st.markdown(f"<h6 style='color:{default_color1};'>Raw data</h6>", unsafe_allow_html=True)
        st.dataframe(df_eur, hide_index=True)

        st.download_button(label="Download in xlsx format",
                           data=convert_df_to_excel(df_eur),
                           file_name='euribors.xlsx',
                           mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')

    plot_interactive_time_series(df_eur)
    st.write("**Source:** Yahoo Finance")
    st.markdown(euribor_str, unsafe_allow_html=True)


elif indicador == "Yield Bonds 5Y - Spain, Germany, Portugal, Euro Area":
    st.markdown(f"<div style='text-align: center;'><h2>Yield Bonds 5Y - Spain, Germany, Portugal, Euro Area</h2></div>", unsafe_allow_html=True)

    if st.sidebar.checkbox("Show raw data"):
        st.markdown(f"<h6 style='color:{default_color1};'>Raw data</h6>", unsafe_allow_html=True)
        st.dataframe(df_all_bonds, hide_index=True)

        st.download_button(label="Download in xlsx format",
                           data=convert_df_to_excel(df_all_bonds),
                           file_name='bonds_5y.xlsx',
                           mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')

    plot_interactive_time_series(df_all_bonds)
    st.write("**Source:** Investing.com")
    st.markdown(bonds_str, unsafe_allow_html=True)

elif indicador == "Yield CDS 5Y - Spain, Germany, USA":
    st.markdown(f"<div style='text-align: center;'><h2>Yield bonds 5Y - Spain, Germany, USA</h2></div>", unsafe_allow_html=True)

    if st.sidebar.checkbox("Show raw data"):
        st.markdown(f"<h6 style='color:{default_color1};'>Raw data</h6>", unsafe_allow_html=True)
        st.dataframe(df_all_cds, hide_index=True)

        st.download_button(label="Download in xlsx format",
                           data=convert_df_to_excel(df_all_cds),
                           file_name='cds_5y.xlsx',
                           mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')

    plot_interactive_time_series(df_all_cds)
    st.write("**Source:** Investing.com")
    st.markdown(cds_str, unsafe_allow_html=True)

elif indicador == "Commercial Property prices":
    st.markdown(f"<div style='text-align: center;'><h2>Commercial Property prices - Portugal and Euro Area</h2></div>", unsafe_allow_html=True)

    if st.sidebar.checkbox("Show raw data"):
        st.markdown(f"<h6 style='color:{default_color1};'>Raw data</h6>", unsafe_allow_html=True)
        st.dataframe(df_aux_cppi, hide_index=True)

        st.download_button(label="Download in xlsx format",
                           data=convert_df_to_excel(df_aux_cppi),
                           file_name='cppi.xlsx',
                           mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')

    plot_interactive_time_series_years(df_aux_cppi)
    st.write("**Source:** ECB & BIS")
    st.markdown(cpp_str, unsafe_allow_html=True)

elif indicador == "Residential Property prices":
    st.markdown(f"<div style='text-align: center;'><h2>Residential Property prices - Portugal and Euro Area</h2></div>", unsafe_allow_html=True)

    if st.sidebar.checkbox("Show raw data"):
        st.markdown(f"<h6 style='color:{default_color1};'>Raw data</h6>", unsafe_allow_html=True)
        st.dataframe(df_hpi, hide_index=True)

        st.download_button(label="Download in xlsx format",
                           data=convert_df_to_excel(df_hpi),
                           file_name='residential_price_index.xlsx',
                           mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')

    plot_interactive_time_series(df_hpi)
    st.write("**Source:** ECB")
    st.markdown(resi_str, unsafe_allow_html=True)

    if st.sidebar.checkbox("Show anomalies"):
        column = st.selectbox("Select column to analyze anomalies", options=df_hpi.columns[1:], index=0)
        method = st.selectbox("Select anomaly detection method", options=["isolation_forest", "HMM", "zscore"])
        plot_anomalies(df_hpi, column, method)

elif indicador == "Inflation (CPI) - Portugal":
    st.markdown(f"<div style='text-align: center;'><h2>Inflation (CPI) - Portugal</h2></div>", unsafe_allow_html=True)

    if st.sidebar.checkbox("Show raw data"):
        st.markdown(f"<h6 style='color:{default_color1};'>Raw data</h6>", unsafe_allow_html=True)
        st.dataframe(df_ipc_pt, hide_index=True)

        st.download_button(label="Download in xlsx format",
                           data=convert_df_to_excel(df_ipc_pt),
                           file_name='inflation_portugal.xlsx',
                           mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')

    plot_interactive_time_series(df_ipc_pt, option_to_choose_variables='no')
    st.write("**Source:** https://bpstat.bportugal.pt/serie/5721524")
    st.markdown(inflation_str, unsafe_allow_html=True)

elif indicador == "Currency exchange rates":
    st.markdown(f"<div style='text-align: center;'><h2>Currency exchange rates</h2></div>", unsafe_allow_html=True)

    if st.sidebar.checkbox("Show raw data"):
        st.markdown(f"<h6 style='color:{default_color1};'>Raw data</h6>", unsafe_allow_html=True)
        st.dataframe(df_fx, hide_index=True)

        st.download_button(label="Download in xlsx format",
                           data=convert_df_to_excel(df_fx),
                           file_name='fx_rates.xlsx',
                           mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')

    plot_interactive_time_series(df_fx)
    st.write("**Source:** https://finance.yahoo.com/quote/EURUSD=X/")

elif indicador == "Euro short-term rate (€STR)":
    st.markdown(f"<div style='text-align: center;'><h2>Euro short-term rate (€STR)</h2></div>", unsafe_allow_html=True)

    if st.sidebar.checkbox("Show raw data"):
        st.markdown(f"<h6 style='color:{default_color1};'>Raw data</h6>", unsafe_allow_html=True)
        st.dataframe(df_ir_str, hide_index=True)

        st.download_button(label="Download in xlsx format",
                           data=convert_df_to_excel(df_ir_str),
                           file_name='short_term_rates.xlsx',
                           mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')

    plot_interactive_time_series(df_ir_str, option_to_choose_variables='no')

    if st.sidebar.checkbox("Show anomalies"):
        method = st.selectbox("Select anomaly detection method", options=["isolation_forest", "HMM", "zscore"])
        plot_anomalies(df_ir_str, 'IR STR', method)

    st.write("**Source:** https://bpstat.bportugal.pt/dados/series?mode=graphic&svid=6698&series=12559714")
    st.markdown(ir_str_str, unsafe_allow_html=True)


elif indicador == "SOFR":
    st.markdown(f"<div style='text-align: center;'><h2>SOFR</h2></div>", unsafe_allow_html=True)

    if st.sidebar.checkbox("Show raw data"):
        st.markdown(f"<h6 style='color:{default_color1};'>Raw data</h6>", unsafe_allow_html=True)
        st.dataframe(df_sofr, hide_index=True)

        st.download_button(label="Download in xlsx format",
                           data=convert_df_to_excel(df_sofr),
                           file_name='sofr.xlsx',
                           mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')

    plot_interactive_time_series(df_sofr, option_to_choose_variables='no')

    st.write("**Source:**  https://fred.stlouisfed.org/")
    st.markdown(sofr_str, unsafe_allow_html=True)

elif indicador == "Key ECB interest rates":
    st.markdown(f"<div style='text-align: center;'><h2>Key ECB interest rates</h2></div>", unsafe_allow_html=True)

    if st.sidebar.checkbox("Show raw data"):
        st.markdown(f"<h6 style='color:{default_color1};'>Raw data</h6>", unsafe_allow_html=True)
        st.dataframe(df_key_ecb_ir, hide_index=True)

        st.download_button(label="Download in xlsx format",
                           data=convert_df_to_excel(df_key_ecb_ir),
                           file_name='key_ecb_ir.xlsx',
                           mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')

    plot_interactive_time_series(df_key_ecb_ir)

    st.write("**Source:**  https://www.ecb.europa.eu/stats/policy_and_exchange_rates/key_ecb_interest_rates/html/index.pt.html")
    st.markdown(key_ecb_str, unsafe_allow_html=True)

elif indicador == "CME Tool":
    st.markdown(f"<div style='text-align: center;'><h2>CME FedWatch Tool</h2></div>", unsafe_allow_html=True)
    st.markdown(cme_tool_str, unsafe_allow_html=True)

    st.markdown(md_botao_cme, unsafe_allow_html=True)




