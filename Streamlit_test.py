"""
This app retrieves the 20 most recent announcements for selected securities from the Australian Securities Exchange (ASX)
"""

# cd ~/Documents/Jupiter\ notebooks/Streamlit/
# streamlit run Streamlit_test.py

import streamlit as st
import pandas as pd
import json

st.title('ASX announcements')

tickers_list_full = [
    'AEE',
    'REZ',
    '1AE',
    '1MC',
    'NRZ'
]

@st.cache_data
def get_announcement(ticker):
    with open(ticker+'.json', 'r') as file:
        json_string = file.read()
        return json_string

df_dict = {}
trading_halt_tickers = []


for ticker in tickers_list_full:    
    data = get_announcement(ticker)
    if 'Trading Halt' in data:
        trading_halt_tickers.append(ticker)
    json_data = json.loads(data)
    df_dict[ticker] = pd.DataFrame(json_data['data'])

show_halts = st.checkbox('Only containing traiding halts')

tickers_list = trading_halt_tickers if show_halts else tickers_list_full
    
selected_tickers = st.multiselect('Select securities:', options=tickers_list)

for ticker in selected_tickers:
    st.subheader(ticker)
    st.write(df_dict[ticker])