import plotly.express as px

def revenue_by_region(df):

    fig = px.bar(
        df,
        x="Region",
        y="Revenue",
        color="Region"
    )

    return fig


def revenue_trend(df):

    fig = px.line(
        df,
        x="Order_Date",
        y="Revenue"
    )

    return fig