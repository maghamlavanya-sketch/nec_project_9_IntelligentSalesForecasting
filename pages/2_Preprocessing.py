import streamlit as st
import pandas as pd
import plotly.express as px

from utils.data_manager import load_data
from pipelines.preprocessing import clean_data
from pipelines.feature_engineering import create_features

st.title("⚙️ Data Preprocessing")

# =====================================
# LOAD DATA
# =====================================

df = load_data()

# =====================================
# DATASET OVERVIEW
# =====================================

st.subheader("Dataset Overview")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Rows", len(df))
col2.metric("Columns", len(df.columns))
col3.metric("Missing Values", int(df.isnull().sum().sum()))
col4.metric("Duplicates", int(df.duplicated().sum()))

st.divider()

# =====================================
# RAW DATA
# =====================================

st.subheader("Raw Dataset Preview")

st.dataframe(
    df.head(20),
    use_container_width=True
)

st.divider()

# =====================================
# MISSING VALUES
# =====================================

st.subheader("Missing Values Analysis")

missing_df = (
    df.isnull()
      .sum()
      .reset_index()
)

missing_df.columns = [
    "Column Name",
    "Missing Values"
]

st.dataframe(
    missing_df,
    use_container_width=True
)

if missing_df["Missing Values"].sum() > 0:

    fig_missing = px.bar(
        missing_df,
        x="Column Name",
        y="Missing Values",
        title="Missing Values by Column"
    )

    st.plotly_chart(
        fig_missing,
        use_container_width=True
    )

else:

    st.success(
        "✅ No Missing Values Found"
    )

st.divider()

# =====================================
# DUPLICATES
# =====================================

duplicates = df.duplicated().sum()

st.subheader("Duplicate Records")

st.info(
    f"Duplicate Rows Found : {duplicates}"
)

st.divider()

# =====================================
# REGION ANALYSIS
# =====================================

if "Region" in df.columns:

    st.subheader("📍 Region Distribution")

    region_counts = (
        df["Region"]
        .value_counts()
        .reset_index()
    )

    region_counts.columns = [
        "Region",
        "Count"
    ]

    fig_region = px.bar(
        region_counts,
        x="Region",
        y="Count",
        title="Records by Region"
    )

    st.plotly_chart(
        fig_region,
        use_container_width=True
    )

# =====================================
# CATEGORY ANALYSIS
# =====================================

if "Category" in df.columns:

    st.subheader("🪑 Category Distribution")

    fig_category = px.pie(
        df,
        names="Category",
        title="Category Distribution"
    )

    st.plotly_chart(
        fig_category,
        use_container_width=True
    )

# =====================================
# REVENUE ANALYSIS
# =====================================

if "Revenue" in df.columns:

    st.subheader("💰 Revenue Distribution")

    fig_revenue = px.histogram(
        df,
        x="Revenue",
        nbins=30,
        title="Revenue Distribution"
    )

    st.plotly_chart(
        fig_revenue,
        use_container_width=True
    )

    st.subheader("📦 Revenue Outlier Detection")

    fig_box = px.box(
        df,
        y="Revenue",
        title="Revenue Boxplot"
    )

    st.plotly_chart(
        fig_box,
        use_container_width=True
    )

# =====================================
# REVENUE BY REGION
# =====================================

if (
    "Region" in df.columns
    and
    "Revenue" in df.columns
):

    st.subheader("📈 Revenue by Region")

    region_sales = (
        df.groupby("Region")["Revenue"]
        .sum()
        .reset_index()
    )

    fig_sales = px.bar(
        region_sales,
        x="Region",
        y="Revenue",
        color="Revenue",
        title="Revenue by Region"
    )

    st.plotly_chart(
        fig_sales,
        use_container_width=True
    )

st.divider()

# =====================================
# PROCESS DATASET
# =====================================

st.subheader(
    "Data Cleaning & Feature Engineering"
)

if st.button("Process Dataset"):

    processed = clean_data(df)

    processed = create_features(
        processed
    )

    processed.to_csv(
        "data/processed_dataset.csv",
        index=False
    )

    st.success(
        "Processed Dataset Saved Successfully"
    )

    st.subheader(
        "Processed Dataset Preview"
    )

    st.dataframe(
        processed.head(20),
        use_container_width=True
    )

    with open(
        "data/processed_dataset.csv",
        "rb"
    ) as file:

        st.download_button(
            label="⬇ Download Processed Dataset",
            data=file,
            file_name="processed_dataset.csv",
            mime="text/csv"
        )