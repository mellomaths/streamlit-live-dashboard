import pandas as pd
import streamlit as st

from environment import get_environment


@st.cache_data
def get_bank_data(env = get_environment()) -> pd.DataFrame:
    return pd.read_csv(env.BANK_DATASET_URL)
