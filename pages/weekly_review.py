import streamlit as st
import pandas as pd

from utils.google_sheets import load_reviews

st.set_page_config(

    page_title="Weekly Review",

    page_icon="📅",

    layout="wide"

)

st.title("📅 Weekly Review")

df = load_reviews()

if df.empty:

    st.warning("No Data")

    st.stop()

summary = (

    df.groupby(

        [

            "coordinator",

            "status"

        ]

    )

    .size()

    .unstack(fill_value=0)

    .reset_index()

)

st.dataframe(

    summary,

    use_container_width=True,

    hide_index=True

)

st.bar_chart(

    summary.set_index("coordinator")
)
