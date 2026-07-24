import streamlit as st
import plotly.express as px
import pandas as pd

from utils.google_sheets import load_reviews

st.set_page_config(
    page_title="Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Executive Dashboard")

df = load_reviews()

if df.empty:
    st.warning("No Review Data")
    st.stop()

total = len(df)
completed = len(df[df.status=="Completed"])
pending = len(df[df.status=="Pending"])
percent = round((completed/total)*100,1) if total else 0

a,b,c,d=st.columns(4)

a.metric("Total Reviews",total)
b.metric("Completed",completed)
c.metric("Pending",pending)
d.metric("Completion %",f"{percent}%")

st.progress(percent/100)

left,right=st.columns(2)

pie=pd.DataFrame({
    "Status":["Completed","Pending"],
    "Count":[completed,pending]
})

with left:
    st.plotly_chart(
        px.pie(
            pie,
            names="Status",
            values="Count",
            hole=.55
        ),
        use_container_width=True
    )

rank=(
    df[df.status=="Completed"]
    .groupby("coordinator")
    .size()
    .reset_index(name="Completed")
)

with right:
    st.plotly_chart(
        px.bar(
            rank,
            x="coordinator",
            y="Completed",
            text="Completed"
        ),
        use_container_width=True
    )

st.subheader("Recent Reviews")

st.dataframe(
    df.tail(20),
    use_container_width=True,
    hide_index=True
)
