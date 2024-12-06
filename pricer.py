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

# Title and Introduction
st.title("Pricing a Black-Scholes Option")

st.write(
    """
    The Black-Scholes model is a widely used framework for pricing European-style options. 
    It calculates the fair value of options based on key parameters.

    The formulas for the""", add_selectbox, """option is shown below:"""
    
)



# Display the formula dynamically
if add_selectbox == "Call":
    st.markdown(
        """
        ### Call Option Formula:
        """,
        unsafe_allow_html=True,
    )
    st.latex("C = S_0 \cdot e^{-qT} \cdot N(d_1) - K \cdot e^{-rT} \cdot N(d_2)")
elif add_selectbox == "Put":
    st.markdown(
        """
        ### Put Option Formula:
        """,
        unsafe_allow_html=True,
    )
    st.latex("P = K \cdot e^{-rT} \cdot N(-d_2) - S_0 \cdot e^{-qT} \cdot N(-d_1)")

# Common for both options
st.markdown(
    """
    The parameters used in the formulas are explained below:
    """,
    unsafe_allow_html=True,
)

st.write(
    """
    - **C**: Price of the Call option  
    - **P**: Price of the Put option  
    - **S₀**: Current price of the underlying asset  
    - **K**: Strike price  
    - **T**: Time to maturity (in years)  
    - **r**: Risk-free interest rate (annualized)  
    - **q**: Dividend yield (annualized)  
    - **σ**: Volatility (annualized)  
    - **N(x)**: Cumulative distribution function of the standard normal distribution  
    """
)

st.markdown("### Calculation of CDF Parameters:")

st.latex(
    r"""
    d_1 = \frac{\ln\left(\frac{S_0}{K}\right) + \left(r - q + \frac{\sigma^2}{2}\right) T}{\sigma \sqrt{T}}
    """
)
st.latex("d_2 = d_1 - {\sigma \sqrt{T}}")


def BS_price(current_price, dividend_rate, rf, vol, T, K):
    # Calculate d1 and d2
    d1 = (np.log(current_price / K) + (rf - dividend_rate + 0.5 * vol**2) * T) / (vol * np.sqrt(T))
    d2 = d1 - vol * np.sqrt(T)

    # Calculate call price
    call_price = (current_price * np.exp(-dividend_rate * T) * norm.cdf(d1)) - (K * np.exp(-rf * T) * norm.cdf(d2))
    
    # Calculate put price
    put_price = (K * np.exp(-rf * T) * norm.cdf(-d2)) - (current_price * np.exp(-dividend_rate * T) * norm.cdf(-d1))

    return call_price, put_price

    

# Display the results if all fields are filled
if add_textbox_price and add_textbox_strike and add_textbox_matu and add_textbox_sigma and add_textbox_rf and add_textbox_dividend:
    # Convert input fields to appropriate data types
    current_price = float(add_textbox_price)
    strike_price = float(add_textbox_strike)
    maturity = float(add_textbox_matu)
    volatility = float(add_textbox_sigma) / 100  # Convert to decimal
    rf = float(add_textbox_rf) / 100  # Convert to decimal
    dividend_rate = float(add_textbox_dividend) / 100  # Convert to decimal

    # Display a loading spinner while the calculation is in progress
    with st.spinner("Calculating the option price..."):
        # Calculate option prices
        call_price, put_price = BS_price(current_price, dividend_rate, rf, volatility, maturity, strike_price)

    # Display the results in an aesthetically pleasing format
    st.markdown("### Option Prices")
    if add_selectbox == "Call":
        st.success(f"The **Call Option Price** is: **${call_price:.2f}**")
    elif add_selectbox == "Put":
        st.success(f"The **Put Option Price** is: **${put_price:.2f}**")

else:
    st.warning("Please fill out all fields in the sidebar to calculate the option price.")
