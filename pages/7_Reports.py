import streamlit as st
import pandas as pd

from reports.excel_generator import (
    generate_excel
)

from reports.pdf_generator import (
    generate_pdf
)

st.title("Reports")

df = pd.read_csv(
    "data/default_dataset.csv"
)

col1,col2 = st.columns(2)

with col1:

    if st.button(
        "Generate Excel Report"
    ):

        path = generate_excel(df)

        with open(
            path,
            "rb"
        ) as file:

            st.download_button(
                "Download Excel",
                file,
                file_name="sales_report.xlsx"
            )

with col2:

    if st.button(
        "Generate PDF Report"
    ):

        path = generate_pdf(df)

        with open(
            path,
            "rb"
        ) as file:

            st.download_button(
                "Download PDF",
                file,
                file_name="sales_report.pdf"
            )

st.subheader("Dataset Preview")

st.dataframe(
    df.head(20),
    use_container_width=True
)