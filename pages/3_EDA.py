import streamlit as st
import pandas as pd
import plotly.express as px

st.title("EDA Analysis")

df = pd.read_csv(
    "data/processed_dataset.csv"
)

tab1,tab2,tab3 = st.tabs(
    [
        "Revenue",
        "Region",
        "Category"
    ]
)

with tab1:

    fig = px.histogram(
        df,
        x="Revenue"
    )

    st.plotly_chart(fig)

with tab2:

    region_sales = (
        df.groupby("Region")
        ["Revenue"]
        .sum()
        .reset_index()
    )

    fig = px.bar(
        region_sales,
        x="Region",
        y="Revenue"
    )

    st.plotly_chart(fig)

with tab3:

    fig = px.pie(
        df,
        names="Category"
    )

    st.plotly_chart(fig)