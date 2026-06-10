import streamlit as st
import joblib
import pandas as pd

st.title("📈 Sales Forecasting")

model = joblib.load(
    "models/revenue_model.pkl"
)

quantity = st.number_input(
    "Quantity",
    1,
    100
)

unit_price = st.number_input(
    "Unit Price",
    100,
    100000
)

month = st.slider(
    "Month",
    1,
    12
)

if st.button(
    "Predict"
):

    sample = pd.DataFrame(
        {
            "Quantity":[quantity],
            "Unit_Price":[unit_price],
            "Month":[month]
        }
    )

    prediction = model.predict(
        sample
    )[0]

    st.success(
        f"Predicted Revenue: ₹{prediction:,.2f}"
    )