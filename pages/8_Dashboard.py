import streamlit as st
import pandas as pd
import plotly.express as px

st.title("📊 Intelligent Sales Dashboard")

# =========================
# LOAD DATA
# =========================

df = pd.read_csv(
    "data/default_dataset.csv"
)

df["Order_Date"] = pd.to_datetime(
    df["Order_Date"]
)

df["Year"] = df["Order_Date"].dt.year
df["Month"] = df["Order_Date"].dt.month
df["Day"] = df["Order_Date"].dt.day

# =========================
# KPI SECTION
# =========================

total_revenue = df["Revenue"].sum()
total_orders = len(df)
products = df["Product_Name"].nunique()
regions = df["Region"].nunique()

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Revenue",
    f"₹{total_revenue:,.0f}"
)

col2.metric(
    "Orders",
    total_orders
)

col3.metric(
    "Products",
    products
)

col4.metric(
    "Regions",
    regions
)

st.divider()

# =========================
# FILTERS
# =========================

st.subheader("Sales Filters")

col1, col2, col3 = st.columns(3)

selected_year = col1.selectbox(
    "Year",
    sorted(df["Year"].unique())
)

selected_region = col2.selectbox(
    "Region",
    ["All"] + sorted(df["Region"].unique())
)

selected_category = col3.selectbox(
    "Category",
    ["All"] + sorted(df["Category"].unique())
)

filtered_df = df[
    df["Year"] == selected_year
]

if selected_region != "All":
    filtered_df = filtered_df[
        filtered_df["Region"] == selected_region
    ]

if selected_category != "All":
    filtered_df = filtered_df[
        filtered_df["Category"] == selected_category
    ]

# =========================
# DAILY SALES TREND
# =========================

st.subheader("📈 Daily Revenue Trend")

daily_sales = (
    filtered_df
    .groupby("Order_Date")["Revenue"]
    .sum()
    .reset_index()
)

fig1 = px.line(
    daily_sales,
    x="Order_Date",
    y="Revenue",
    markers=True
)

st.plotly_chart(
    fig1,
    use_container_width=True
)

# =========================
# DAILY ORDER FREQUENCY
# =========================

st.subheader("📅 Daily Order Frequency")

daily_orders = (
    filtered_df
    .groupby("Order_Date")
    .size()
    .reset_index(name="Orders")
)

fig_orders = px.line(
    daily_orders,
    x="Order_Date",
    y="Orders",
    markers=True
)

st.plotly_chart(
    fig_orders,
    use_container_width=True
)

# =========================
# HIGHEST / LOWEST SALES
# =========================

if not daily_sales.empty:

    highest_day = daily_sales.loc[
        daily_sales["Revenue"].idxmax()
    ]

    lowest_day = daily_sales.loc[
        daily_sales["Revenue"].idxmin()
    ]

    col1, col2 = st.columns(2)

    col1.success(
        f"Highest Sales Day: {highest_day['Order_Date'].date()} | ₹{highest_day['Revenue']:,.0f}"
    )

    col2.error(
        f"Lowest Sales Day: {lowest_day['Order_Date'].date()} | ₹{lowest_day['Revenue']:,.0f}"
    )

st.divider()

# =========================
# MONTHLY REVENUE
# =========================

st.subheader("📊 Monthly Revenue")

monthly_sales = (
    filtered_df
    .groupby("Month")["Revenue"]
    .sum()
    .reset_index()
)

fig2 = px.bar(
    monthly_sales,
    x="Month",
    y="Revenue"
)

st.plotly_chart(
    fig2,
    use_container_width=True
)

# =========================
# MONTHLY GROWTH
# =========================

monthly_sales["Growth %"] = (
    monthly_sales["Revenue"]
    .pct_change() * 100
)

st.subheader("📈 Monthly Growth Rate")

fig_growth = px.line(
    monthly_sales,
    x="Month",
    y="Growth %",
    markers=True
)

st.plotly_chart(
    fig_growth,
    use_container_width=True
)

st.divider()

# =========================
# REGION PERFORMANCE
# =========================

st.subheader("🌍 Region Performance")

region_sales = (
    filtered_df
    .groupby("Region")["Revenue"]
    .sum()
    .reset_index()
)

fig3 = px.bar(
    region_sales,
    x="Region",
    y="Revenue",
    color="Revenue"
)

st.plotly_chart(
    fig3,
    use_container_width=True
)

# =========================
# REGION FREQUENCY
# =========================

st.subheader("📦 Order Frequency By Region")

region_frequency = (
    filtered_df
    .groupby("Region")
    .size()
    .reset_index(name="Orders")
)

fig_freq = px.bar(
    region_frequency,
    x="Region",
    y="Orders"
)

st.plotly_chart(
    fig_freq,
    use_container_width=True
)

# =========================
# REGION CLASSIFICATION
# =========================

st.subheader(
    "🏆 Leading / Medium / Low Regions"
)

if not region_sales.empty:

    max_revenue = region_sales["Revenue"].max()

    def classify_region(revenue):

        ratio = revenue / max_revenue

        if ratio >= 0.80:
            return "Leading"

        elif ratio >= 0.50:
            return "Medium"

        else:
            return "Low"

    region_sales["Level"] = (
        region_sales["Revenue"]
        .apply(classify_region)
    )

    st.dataframe(
        region_sales,
        use_container_width=True
    )

    fig4 = px.pie(
        region_sales,
        names="Level",
        values="Revenue"
    )

    st.plotly_chart(
        fig4,
        use_container_width=True
    )

# =========================
# REGION LEADERBOARD
# =========================

st.subheader("🥇 Region Leaderboard")

leaderboard = (
    region_sales
    .sort_values(
        "Revenue",
        ascending=False
    )
)

st.dataframe(
    leaderboard,
    use_container_width=True
)

st.divider()

# =========================
# TOP PRODUCTS
# =========================

st.subheader(
    "🪑 Top Products By Revenue"
)

top_products = (
    filtered_df
    .groupby("Product_Name")["Revenue"]
    .sum()
    .reset_index()
    .sort_values(
        "Revenue",
        ascending=False
    )
    .head(10)
)

fig5 = px.bar(
    top_products,
    x="Product_Name",
    y="Revenue",
    color="Revenue"
)

st.plotly_chart(
    fig5,
    use_container_width=True
)

# =========================
# PRODUCT FREQUENCY
# =========================

st.subheader(
    "📦 Product Frequency"
)

product_frequency = (
    filtered_df
    .groupby("Product_Name")
    .size()
    .reset_index(name="Frequency")
    .sort_values(
        "Frequency",
        ascending=False
    )
    .head(10)
)

fig6 = px.bar(
    product_frequency,
    x="Product_Name",
    y="Frequency",
    color="Frequency"
)

st.plotly_chart(
    fig6,
    use_container_width=True
)

st.divider()

# =========================
# RECENT SALES
# =========================

st.subheader(
    "📋 Recent Sales"
)

st.dataframe(
    filtered_df.tail(20),
    use_container_width=True
)