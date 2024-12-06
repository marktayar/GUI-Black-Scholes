import numpy as np
import streamlit as st
import pandas as pd
from scipy.stats import norm

# Add a selectbox to the sidebar:
add_selectbox = st.sidebar.selectbox(
    'What kind of option would you like?',
    ('Call', 'Put')
)

add_slider = st.sidebar.slider('Actual Price', 0.0, 1000.0)  # 👈 this is a widget

