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