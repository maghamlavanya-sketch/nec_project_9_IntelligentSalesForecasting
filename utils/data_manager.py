import streamlit as st
import pandas as pd

DEFAULT_PATH = "data/default_dataset.csv"

def load_data():

    if "dataset" in st.session_state:
        return st.session_state["dataset"]

    return pd.read_csv(DEFAULT_PATH)


def set_data(df):

    st.session_state["dataset"] = df


def get_source():

    if "dataset" in st.session_state:
        return "Uploaded Dataset"

    return "Default Dataset"