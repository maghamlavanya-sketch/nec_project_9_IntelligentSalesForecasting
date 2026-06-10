import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score

# Load dataset
df = pd.read_csv("data/default_dataset.csv")

# Create Month column
df["Order_Date"] = pd.to_datetime(df["Order_Date"])
df["Month"] = df["Order_Date"].dt.month

# Features
X = df[
    [
        "Quantity",
        "Unit_Price",
        "Month"
    ]
]

# Target
y = df["Revenue"]

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Model
model = RandomForestRegressor(
    random_state=42
)

model.fit(
    X_train,
    y_train
)

# Predictions
preds = model.predict(X_test)

# Accuracy
score = r2_score(
    y_test,
    preds
)

print(f"R² Score: {score:.4f}")

# Save model
joblib.dump(
    model,
    "models/revenue_model.pkl"
)

print("Model saved successfully.")