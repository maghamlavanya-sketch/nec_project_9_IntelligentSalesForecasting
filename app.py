import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Intelligent Sales",
    layout="wide"
)

st.title("📈 Intelligent Sales")

st.caption(
    "AI-Powered Sales Forecasting & Inventory Optimization"
)

df = pd.read_csv(
    "data/default_dataset.csv"
)

col1,col2,col3,col4 = st.columns(4)

col1.metric(
    "Revenue",
    f"₹{df['Revenue'].sum():,.0f}"
)

col2.metric(
    "Orders",
    len(df)
)

col3.metric(
    "Products",
    df["Product_Name"].nunique()
)

col4.metric(
    "Regions",
    df["Region"].nunique()
)

st.divider()

st.subheader(
    "Live Preview - Default Dataset"
)

st.dataframe(
    df.head(20),
    use_container_width=True
)