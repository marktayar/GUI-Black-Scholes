import numpy as np
import streamlit as st
import pandas as pd
from scipy.stats import norm


def BS_price(current_price, divident_rate, rf, vol, T, K):
    d1 = (np.log(current_price / K) + (rf - divident_rate + 0.5 * vol**2) * T) / (vol * np.sqrt(T))
    d2 = d1 - vol * np.sqrt(T)

    # Calculate call price
    call_price = (current_price * np.exp(-divident_rate * T) * norm.cdf(d1)) - (K * np.exp(-rf * T) * norm.cdf(d2))
    
    # Calculate put price
    put_price = (K * np.exp(-rf * T) * norm.cdf(-d2)) - (current_price * np.exp(-divident_rate * T) * norm.cdf(-d1))

    return call_price, put_price

def BS_greeks(current_price, dividend_rate, rf, vol, T, K):
    # Calculate d1 and d2
    d1 = (np.log(current_price / K) + (rf - dividend_rate + 0.5 * vol**2) * T) / (vol * np.sqrt(T))
    d2 = d1 - vol * np.sqrt(T)
    
    # Delta
    delta_call = np.exp(-dividend_rate * T) * norm.cdf(d1)
    delta_put = np.exp(-dividend_rate * T) * (norm.cdf(d1) - 1)
    
    # Rho
    rho_call = K * T * np.exp(-rf * T) * norm.cdf(d2)
    rho_put = -K * T * np.exp(-rf * T) * norm.cdf(-d2)
    
    # Vega (same for call and put)
    vega = current_price * np.exp(-dividend_rate * T) * norm.pdf(d1) * np.sqrt(T)
    
    # Theta
    term1 = -(current_price * norm.pdf(d1) * vol * np.exp(-dividend_rate * T)) / (2 * np.sqrt(T))
    term2_call = dividend_rate * current_price * norm.cdf(d1) * np.exp(-dividend_rate * T)
    term3_call = rf * K * np.exp(-rf * T) * norm.cdf(d2)
    theta_call = term1 - term2_call - term3_call
    
    term2_put = dividend_rate * current_price * norm.cdf(-d1) * np.exp(-dividend_rate * T)
    term3_put = rf * K * np.exp(-rf * T) * norm.cdf(-d2)
    theta_put = term1 + term2_put + term3_put
    
    return {
        "delta_call": delta_call,
        "delta_put": delta_put,
        "rho_call": rho_call,
        "rho_put": rho_put,
        "vega": vega,
        "theta_call": theta_call,
        "theta_put": theta_put
    }
