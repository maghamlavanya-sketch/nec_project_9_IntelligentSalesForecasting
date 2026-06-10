import streamlit as st
import pandas as pd
import plotly.express as px
import joblib

from sklearn.model_selection import (
    train_test_split
)

from sklearn.ensemble import (
    RandomForestRegressor
)

from sklearn.metrics import (
    r2_score,
    mean_absolute_error
)

st.title("Model Training")

df = pd.read_csv(
    "data/processed_dataset.csv"
)

X = df[
    [
        "Quantity",
        "Unit_Price",
        "Month"
    ]
]

y = df["Revenue"]

X_train,X_test,y_train,y_test = (
    train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )
)

model = RandomForestRegressor(
    random_state=42
)

model.fit(
    X_train,
    y_train
)

preds = model.predict(X_test)

r2 = r2_score(
    y_test,
    preds
)

mae = mean_absolute_error(
    y_test,
    preds
)

col1,col2 = st.columns(2)

col1.metric(
    "R² Score",
    round(r2,4)
)

col2.metric(
    "MAE",
    round(mae,2)
)

results = pd.DataFrame(
    {
        "Actual Sales": y_test,
        "Predicted Sales": preds
    }
)

st.subheader(
    "Actual vs Predicted Sales"
)

fig = px.scatter(
    results,
    x="Actual Sales",
    y="Predicted Sales"
)

st.plotly_chart(fig)

st.dataframe(
    results.head(30)
)

joblib.dump(
    model,
    "models/revenue_model.pkl"
)