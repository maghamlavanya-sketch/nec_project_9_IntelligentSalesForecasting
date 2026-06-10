import pandas as pd

def generate_excel(df):

    file_path = "reports/sales_report.xlsx"

    with pd.ExcelWriter(
        file_path
    ) as writer:

        df.to_excel(
            writer,
            sheet_name="Sales Data",
            index=False
        )

    return file_path