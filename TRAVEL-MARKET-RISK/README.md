**https://travel-market-risk.streamlit.app/**


# TRAVEL Market Risk Portal

This is a **Streamlit** application that provides real-time visualizations of macroeconomic and financial data, allowing users to analyze market indicators, detect anomalies, and download data for further use.

## Features

- Display of various financial indicators, including:
  - **Fear & Greed Index**
  - **Warren Buffett Indicator**
  - **VIX**
  - **Euribor Rates**
  - **Commercial and Residential Property Prices**
  - **Interest Rates and Exchange Rates**
  - **Sovereign Bond Yields (CDS and Bonds)**
  - **European Central Bank (ECB) Key Indicators**
  - **SOFR and other short-term rate indicators**

- Anomaly detection in time series using methods such as:
  - Isolation Forest
  - Hidden Markov Models (HMM)
  - Z-Score

- Downloadable data in **XLSX** format for further analysis.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/TRAVEL-GVM/TRAVEL-MARKET-RISK.git

2. Install the required dependencies:

    ```bash
    Copy code
    pip install -r requirements.txt

3. Run the app
    ```bash
    streamlit run main.py

## Data Sources

- **Fear & Greed Index**: [CNN Fear & Greed Index](https://edition.cnn.com/markets/fear-and-greed)
- **VIX Index**: [Yahoo Finance](https://finance.yahoo.com/quote/%5EVIX/)
- **ECB Data**: [ECB Statistics](https://www.ecb.europa.eu/stats/policy_and_exchange_rates/key_ecb_interest_rates/html/index.pt.html)
- **SOFR Rates**: [FRED SOFR](https://fred.stlouisfed.org/)
- **Benchmark Indices**: [Yahoo Finance](https://finance.yahoo.com/)
- **Commercial and Residential Property Prices**: [ECB](https://www.ecb.europa.eu/) and [BIS](https://www.bis.org/)
- **Currency Exchange Rates**: [Yahoo Finance](https://finance.yahoo.com/)
- **Key ECB Interest Rates**: [ECB Official Website](https://www.ecb.europa.eu/stats/policy_and_exchange_rates/key_ecb_interest_rates/html/index.pt.html)
- **Yield Bonds and CDS**: [Investing.com](https://www.investing.com/)

## Anomaly Detection

For each indicator, users can enable anomaly detection using the following methods:

- **Isolation Forest**: Identifies outliers by isolating observations.
- **Hidden Markov Models (HMM)**: Detects irregularities based on probabilistic models.
- **Z-Score**: Standardized score to detect values deviating significantly from the mean.

## Customization

The app can be customized through `config.py` to change titles, colors, and other display options. This includes:

- **Titles and labels**: Customizable for different sections.
- **Colors**: Adjust theme colors of the dashboard.
- **Logos and images**: Change logos in the sidebar.
