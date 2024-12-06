import numpy as np
import streamlit as st
import pandas as pd
from scipy.stats import norm

st.text_input("Your name", key="name")

# You can access the value at any point with:
st.session_state.name