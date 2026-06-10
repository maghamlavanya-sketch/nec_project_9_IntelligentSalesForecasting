import streamlit as st

st.title(
    "📦 Inventory Optimization"
)

tab1,tab2 = st.tabs(
    [
        "Manual Calculator",
        "Data Driven Insights"
    ]
)

with tab1:

    avg_sales = st.number_input(
        "Average Daily Sales"
    )

    lead_time = st.number_input(
        "Lead Time"
    )

    safety_stock = st.number_input(
        "Safety Stock"
    )

    reorder = (
        avg_sales *
        lead_time
        +
        safety_stock
    )

    st.success(
        f"Recommended Inventory: {reorder}"
    )