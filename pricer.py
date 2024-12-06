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


# Title and Introduction
st.title("Pricing a Black-Scholes Option")

st.write(
    """
    The Black-Scholes model is a widely used framework for pricing European-style options. 
    It calculates the fair value of options based on key parameters such as:
    - Current price of the underlying asset (\(S_0\))
    - Strike price (\(K\))
    - Time to maturity (\(T\))
    - Volatility (\(\\sigma\))
    - Risk-free rate (\(r\))
    - Dividend yield (\(q\))

    The formulas for Call and Put options are shown below, based on your selection:
    """
)

# Sidebar selection
option_type = st.sidebar.selectbox("Select Option Type", ["Call", "Put"])

# Display the formula dynamically
if option_type == "Call":
    st.markdown(
        r"""
        ### Call Option Formula:
        \[
        C = S_0 \cdot e^{-qT} \cdot N(d_1) - K \cdot e^{-rT} \cdot N(d_2)
        \]
        """
    )
elif option_type == "Put":
    st.markdown(
        r"""
        ### Put Option Formula:
        \[
        P = K \cdot e^{-rT} \cdot N(-d_2) - S_0 \cdot e^{-qT} \cdot N(-d_1)
        \]
        """
    )

# Common for both options
st.write(
    r"""
    where:
    - \(C\): Price of the Call option
    - \(P\): Price of the Put option
    - \(S_0\): Current price of the underlying asset
    - \(K\): Strike price
    - \(T\): Time to maturity (in years)
    - \(r\): Risk-free interest rate (annualized)
    - \(q\): Dividend yield (annualized)
    - \(\\sigma\): Volatility (annualized)
    - \(N(x)\): Cumulative distribution function of the standard normal distribution
    - \(d_1\) and \(d_2\) are given by:
    """
)

st.markdown(
    r"""
    \[
    d_1 = \frac{\ln(S_0 / K) + (r - q + \sigma^2 / 2) T}{\sigma \sqrt{T}}
    \]
    \[
    d_2 = d_1 - \sigma \sqrt{T}
    \]
    """
)