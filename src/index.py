import streamlit as st
import pandas as pd
import plotly.express as px

from datasets import get_bank_data


st.set_page_config(
    page_title="Live Dashboard",
    page_icon="✅",
    layout="wide",
)

st.title("Live Dashboard")


df = get_bank_data()

job_filter = st.selectbox("Select the Job", pd.unique(df["job"]))
df = df[df["job"] == job_filter]

placeholder = st.empty()
with placeholder.container():
    col1, col2, col3 = st.columns(3)
    with col1:
        avg_age = df["age"].mean()
        st.metric(
            label="Age ⏳",
            value=round(avg_age),
            delta=round(avg_age) - 10,
        )

    with col2:
        marital_count = df["marital"].value_counts()
        count_married = int(marital_count["married"])

        st.metric(
            label="Married Count 💍",
            value=count_married,
            delta=-10 + count_married,
        )

    with col3:
        balance = df["balance"].mean()
        st.metric(
            label="A/C Balance ＄",
            value=f"$ {round(balance,2)} ",
            delta=-round(balance / count_married) * 100,
        )

    fig_col1, fig_col2 = st.columns(2)
    with fig_col1:
        st.markdown("### Density Heatmap (Marital x Age)")
        fig = px.density_heatmap(data_frame=df, y = 'age', x = 'marital')
        st.write(fig)

    with fig_col2:
        st.markdown("### Histogram (Age x Count)")
        fig2 = px.histogram(data_frame = df, x = 'age')
        st.write(fig2)

    st.markdown("### Detailed Data View")
    st._legacy_dataframe(df) # st.dataframe will not go wide following the page layout

