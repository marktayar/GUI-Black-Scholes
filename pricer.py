import numpy as np
import streamlit as st
import pandas as pd
from scipy.stats import norm

# Add a selectbox to the sidebar:
add_selectbox = st.sidebar.selectbox(
    'What kind of option would you like?',
    ('Call', 'Put')
)
st.sidebar.markdown(f"<small>You selected: {add_selectbox}</small>", unsafe_allow_html=True)

# Current Price
add_textbox_price = st.sidebar.text_input("Current Price", key="current_price")
st.sidebar.markdown(f"<small>You entered: {add_textbox_price}</small>", unsafe_allow_html=True)

# Strike Price
add_textbox_strike = st.sidebar.text_input("Strike Price", key="strike_price")
st.sidebar.markdown(f"<small>You entered: {add_textbox_strike}</small>", unsafe_allow_html=True)

# Time to Maturity
add_textbox_matu = st.sidebar.text_input("Time to Maturity", key="maturity")
st.sidebar.markdown(f"<small>You entered: {add_textbox_matu}</small>", unsafe_allow_html=True)

# Volatility
add_textbox_sigma = st.sidebar.text_input("Volatility in percentage", key="vol")
st.sidebar.markdown(f"<small>You entered: {add_textbox_sigma}%</small>", unsafe_allow_html=True)

# Risk-Free Rate
add_textbox_rf = st.sidebar.text_input("Risk free rate in percentage", key="rf")
st.sidebar.markdown(f"<small>You entered: {add_textbox_rf}%</small>", unsafe_allow_html=True)

# Dividend Rate
add_textbox_dividend = st.sidebar.text_input("Dividend Rate in percentage", key="dividend_rate")
st.sidebar.markdown(f"<small>You entered: {add_textbox_dividend}%</small>", unsafe_allow_html=True)


