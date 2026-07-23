import streamlit as st
import pandas as pd
import plotly.express as px

from utils.google_sheets import load_reviews

st.set_page_config(
    page_title="Executive Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Executive Dashboard")

df = load_reviews()

if df.empty:
    st.warning("No Review Data Found")
    st.stop()

# ---------------- KPIs ----------------

total = len(df)

completed = len(df[df["status"] == "Completed"])

pending = total - completed

percent = round((completed / total) * 100, 1) if total else 0

c1, c2, c3, c4 = st.columns(4)

c1.metric("📋 Total Reviews", total)

c2.metric("✅ Completed", completed)

c3.metric("⏳ Pending", pending)

c4.metric("📈 Completion", f"{percent}%")

st.progress(percent / 100)

st.divider()

# ---------------- Pie ----------------

left, right = st.columns(2)

pie = pd.DataFrame({

    "Status": ["Completed", "Pending"],

    "Count": [completed, pending]

})

with left:

    fig = px.pie(

        pie,

        names="Status",

        values="Count",

        hole=.6

    )

    st.plotly_chart(

        fig,

        use_container_width=True

    )

# ---------------- Coordinator Ranking ----------------

rank = (

    df[df["status"] == "Completed"]

    .groupby("coordinator")

    .size()

    .reset_index(name="Completed")

)

with right:

    fig = px.bar(

        rank,

        x="coordinator",

        y="Completed",

        text="Completed",

        color="Completed"

    )

    st.plotly_chart(

        fig,

        use_container_width=True

    )

st.divider()

# ---------------- Daily Summary ----------------

summary = (

    df.groupby(["date", "status"])

    .size()

    .reset_index(name="Count")

)

fig = px.line(

    summary,

    x="date",

    y="Count",

    color="status",

    markers=True

)

st.plotly_chart(

    fig,

    use_container_width=True

)

st.divider()

st.subheader("Recent Reviews")

st.dataframe(

    df.tail(20),

    use_container_width=True,

    hide_index=True

)
