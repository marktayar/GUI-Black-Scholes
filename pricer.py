import numpy as np
import streamlit as st
import pandas as pd
from scipy.stats import norm

# Add a selectbox to the sidebar:
add_selectbox = st.sidebar.selectbox(
    'What kind of option would you like?',
    ('Call', 'Put')
)

add_textbox_price = st.sidebar.text_input("Current Price" , key = "current_price")
add_textbox_strike = st.sidebar.text_input("Strike Price" , key = "strike_price")
add_textbox_matu = st.sidebar.text_input("Time to Maturity" , key = "Maturity")
add_textbox_sigma = st.sidebar.text_input("Volatility in percentage" , key = "vol")
add_textbox_rf = st.sidebar.text_input("Risk free rate in percentage" , key = "rf")
add_textbox_dividend = st.sidebar.text_input("Dividend Rate in percentage" , key = "dividend_rate")

