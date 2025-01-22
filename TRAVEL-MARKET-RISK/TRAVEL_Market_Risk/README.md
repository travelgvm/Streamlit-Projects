# Streamlit Dashboard Project

This project is a Streamlit-based dashboard that provides real-time or near-real-time financial data analysis. The app fetches, visualizes, and analyzes various economic indicators and financial data from different sources.

## Project Structure

**Configuration file for app settings (titles, colors, etc.)**

├── config.py 

**Data extraction functions from external sources**

├── get_data.py

**Folder containing CSV files for bond data downloaded and inputed manually from investing.com**

├── bonds_data │ └── <bonds_es_5y.csv> │ └── <bonds_ger_5y.csv> │ └── <bonds_pt_5y.csv> 


**Folder containing CSV files for CDS data downloaded and inputed manually from investing.com**

├── cds_data/ 

│ └── <cds_es_5y.csv> │ └── <cds_ger_5y.csv> │ └── <cds_us_5y.csv> 


**Loads and preprocesses data** 

├── load_data.py 


 **# Visualization functions for plotting data**

├── viz.py


**Main Streamlit application file**

├── main.py



