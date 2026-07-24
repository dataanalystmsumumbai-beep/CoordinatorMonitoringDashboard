import streamlit as st
import pandas as pd
import plotly.express as px

from utils.google_sheets import load_reviews

st.set_page_config(
    page_title="Pending Tracker",
    page_icon="🚨",
    layout="wide"
)

st.title("🚨 Pending Tracker")

df = load_reviews()

if isinstance(df, list):
    df = pd.DataFrame(df)

if df.empty:
    st.warning("No Data Found")
    st.stop()

pending = df[df["status"] == "Pending"].copy()

if pending.empty:
    st.success("🎉 No Pending Tasks")
    st.stop()

# ---------------- FILTERS ----------------

c1, c2 = st.columns(2)

with c1:
    coordinator = st.selectbox(
        "Coordinator",
        ["All"] + sorted(
            pending["coordinator"].dropna().unique().tolist()
        )
    )

with c2:
    priority = st.selectbox(
        "Priority",
        ["All"] + sorted(
            pending["priority"].dropna().unique().tolist()
        )
    )

if coordinator != "All":
    pending = pending[
        pending["coordinator"] == coordinator
    ]

if priority != "All":
    pending = pending[
        pending["priority"] == priority
    ]

# ---------------- KPI ----------------

high = len(
    pending[pending["priority"] == "High"]
)

medium = len(
    pending[pending["priority"] == "Medium"]
)

low = len(
    pending[pending["priority"] == "Low"]
)

a, b, c, d = st.columns(4)

a.metric("Pending Tasks", len(pending))
b.metric("High", high)
c.metric("Medium", medium)
d.metric("Low", low)

st.divider()

# ---------------- COORDINATOR CHART ----------------

chart = (

    pending.groupby("coordinator")

    .size()

    .reset_index(name="Pending")

)

if not chart.empty:

    fig = px.bar(

        chart,

        x="coordinator",

        y="Pending",

        text="Pending",

        color="Pending"

    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

st.divider()

# ---------------- PRIORITY CHART ----------------

pie = (

    pending.groupby("priority")

    .size()

    .reset_index(name="Count")

)

fig = px.pie(

    pie,

    names="priority",

    values="Count",

    hole=0.55

)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.divider()

# ---------------- TABLE ----------------

st.subheader("Pending Review List")

st.dataframe(
    pending.sort_values(
        ["priority", "coordinator"]
    ),
    use_container_width=True,
    hide_index=True
)
