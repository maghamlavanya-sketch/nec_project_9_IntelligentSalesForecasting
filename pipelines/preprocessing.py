import pandas as pd

def clean_data(df):

    df = df.drop_duplicates()

    numeric_cols = [
        "Quantity",
        "Unit_Price",
        "Revenue"
    ]

    for col in numeric_cols:

        df[col] = df[col].fillna(
            df[col].median()
        )

    return df