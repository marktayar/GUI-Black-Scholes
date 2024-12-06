import numpy as np
import streamlit as st
import pandas as pd
from scipy.stats import norm

# Add a selectbox to the sidebar:
add_selectbox = st.sidebar.selectbox(
    'What kind of option would you like?',
    ('Call', 'Put')
)

# Add a slider to the sidebar:
add_slider = st.sidebar.slider(
    'Current Price',
    0.01, 1000, 25
)

