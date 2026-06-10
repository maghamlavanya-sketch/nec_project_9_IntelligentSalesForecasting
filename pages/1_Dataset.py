import streamlit as st
import pandas as pd

from utils.data_manager import (
    load_data,
    set_data
)

st.title("Dataset Manager")

uploaded = st.file_uploader(
    "Upload Dataset",
    type=["csv"]
)

if uploaded:

    df = pd.read_csv(uploaded)

    set_data(df)

    st.success(
        "Dataset Uploaded Successfully"
    )

df = load_data()

st.subheader("Current Dataset")

st.dataframe(
    df,
    use_container_width=True
)

st.write(
    f"Rows : {len(df)}"
)

st.write(
    f"Columns : {len(df.columns)}"
)