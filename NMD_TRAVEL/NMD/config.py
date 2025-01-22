# nb default colors for plots and excel
default_color1 = '#179297'
default_color2 = '#BFCE28'

sidebar_indicators = ('Raw data', 'Deposits prediction challenge', 'Correlation matrix analysis',
                      'Interactive Plots', 'Dual Axis Interactive Plots')

dashboard_main_title = "Non-Maturity Deposits"

path_nmd = 'https://raw.githubusercontent.com/TRAVEL-GVM/NMD_TRAVEL/refs/heads/main/NMD/NMD.xlsx'
path_ts_notebook = 'https://raw.githubusercontent.com/TRAVEL-GVM/NMD_TRAVEL/refs/heads/main/NMD/TimeSeries.html'
path_ts_notebook1 = 'https://raw.githubusercontent.com/TRAVEL-GVM/NMD_TRAVEL/refs/heads/main/NMD/Challenges_TS.html'

travel_logo_url = "https://raw.githubusercontent.com/ricardoandreom/Webscrape/refs/heads/main/travel_logo.webp"

notebooks_str1 = """
## Deposits Forecasting Challenge

This section presents two Jupyter notebooks that showcase different approaches to forecasting future deposits for both
corporate and retail sectors. In the first notebook, we apply traditional statistical methods such as 
Holt-Winters and ARIMA to predict deposit trends. These methods are well-established for time series analysis and 
provide insights based on historical data patterns.

#### Holt-Winters
A time series forecasting method that captures seasonality and trends. It’s useful for data with repeating patterns, 
offering short-term predictions based on exponential smoothing.

#### ARIMA (AutoRegressive Integrated Moving Average)
A widely-used statistical model that predicts future values by combining autoregression, differencing, and moving 
averages. It is effective for non-seasonal data or when seasonality is integrated into the model.
"""

notebooks_str2 = """
In the second notebook, we explore more advanced machine learning techniques, including LSTM (Long Short-Term Memory) 
and Prophet. These models are designed to handle complex time dependencies and seasonality in data, offering a modern 
perspective on forecasting.

#### LSTM (Long Short-Term Memory)
A type of neural network designed to capture long-term dependencies in sequential data. LSTM is highly effective for 
complex time series, learning patterns over time.

#### Prophet
A forecasting tool developed by Facebook, designed for time series with daily data and missing values. It handles 
seasonality, holidays, and trend shifts, offering flexible and interpretable forecasts.
"""


corr_default_columns = ['Euribor 3M', 'Retail', 'Corporate', 'Dívida direta do Estado - certificados de aforro',
                        'Responsabilidades à vista-Particulares-PRT-M€ (OIFM)',
                        'Responsabilidades à vista-SNF-PRT-M€ (OIFM)',
                        'Taxa de juro (TAA) de novos depósitos a prazo dos particulares',
                        'Taxa de juro (TAA) de novos depósitos a prazo das empresas não financeiras',
                        'Montante de novos depósitos a prazo dos particulares',
                        'Montante de novos depósitos a prazo das empresas não financeiras']

notional_cols = ['Montante de novos depósitos a prazo até 1 ano dos particulares',
                 'Montante de novos depósitos a prazo dos particulares',
                 'Montante de novos depósitos a prazo das empresas não financeiras',
                 'Depósitos e equiparados-M€ (OIFM)',
                 'Depósitos e equiparados-Particulares-PRT-M€ (OIFM)',
                 'Depósitos e equiparados-SNF-PRT-M€ (OIFM)',
                 'Responsabilidades à vista-PRT-M€ (OIFM)',
                 'Responsabilidades à vista-Particulares-PRT-M€ (OIFM)',
                 'Responsabilidades à vista-SNF-PRT-M€ (OIFM)',
                 'Dívida direta do Estado - certificados de aforro']

interest_rate_cols = ['Taxa de juro (TAA) de novos depósitos a prazo até 1 ano dos particulares',
                      'Taxa de juro (TAA) de novos depósitos a prazo até 1 ano das empresas não financeiras',
                      'Taxa de juro (TAA) de novos depósitos a prazo dos particulares',
                      'Taxa de juro (TAA) de novos depósitos a prazo das empresas não financeiras',
                      'Taxa de juro (TAA) do stock de depósitos à ordem dos particulares',
                      'Taxa de juro (TAA) do stock de depósitos a prazo dos particulares',
                      'Taxa de juro (TAA) do stock de empréstimos às empresas não financeiras',
                      'Taxa de juro (TAA) do stock de depósitos a prazo a mais de 2 anos dos particulares',
                      'Euribor 3M']


###################################################

# Alphavantage API Key
alpha_api_key = 'EW4A338V8YGLZI3G'
# FRED API KEY
fred_api_key = 'eff3c719d275248bf5cdcfc836400e53'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML,'
                  ' like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Accept-Language': 'en-US,en;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Connection': 'keep-alive',
}


bank_pt_series_dict = {
    12519805: 'Taxa de juro (TAA) de novos depósitos a prazo até 1 ano dos particulares',
    12519806: 'Taxa de juro (TAA) de novos depósitos a prazo até 1 ano das empresas não financeiras',
    12519797: 'Montante de novos depósitos a prazo até 1 ano dos particulares',
    12519799: 'Montante de novos depósitos a prazo dos particulares',
    12519800: 'Montante de novos depósitos a prazo das empresas não financeiras',
    12519712: 'Taxa de juro (TAA) do stock de depósitos a prazo do setor não financeiro  '
              '(exceto administrações públicas)',
    12519807: 'Taxa de juro (TAA) de novos depósitos a prazo dos particulares',
    12519808: 'Taxa de juro (TAA) de novos depósitos a prazo das empresas não financeiras',
    12519717: 'Taxa de juro (TAA) do stock de depósitos à ordem dos particulares',
    12519720: 'Taxa de juro (TAA) do stock de depósitos a prazo dos particulares',
    12519785: 'Taxa de juro (TAA) do stock de empréstimos às empresas não financeiras',
    12519718: 'Taxa de juro (TAA) do stock de depósitos a prazo a mais de 2 anos dos particulares',
    12527037: 'Depósitos e equiparados-M€ (OIFM)',
    12556700: 'Depósitos e equiparados-Particulares-PRT-M€ (OIFM)',
    12529442: 'Depósitos e equiparados-SNF-PRT-M€ (OIFM)',
    12529238: 'Responsabilidades à vista-PRT-M€ (OIFM)',
    12556750: 'Responsabilidades à vista-Particulares-PRT-M€ (OIFM)',
    12529239: 'Responsabilidades à vista-SNF-PRT-M€ (OIFM)',
    12561438: 'Dívida direta do Estado - certificados de aforro'
    }
