import joblib
import pandas as pd

model = joblib.load(
    "models/revenue_model.pkl"
)

def predict(
        quantity,
        unit_price,
        month):

    sample = pd.DataFrame(
        {
            "Quantity":[quantity],
            "Unit_Price":[unit_price],
            "Month":[month]
        }
    )

    return model.predict(
        sample
    )[0]