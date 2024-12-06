import numpy as np
import streamlit as st
import pandas as pd
from scipy.stats import norm

x = st.slider('x')  # 👈 this is a widget
st.write(x, 'squared is', x * x)