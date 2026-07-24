import streamlit as st
import pandas as pd
import plotly.express as px

from utils.google_sheets import load_reviews

st.set_page_config(
    page_title="Weekly Review",
    page_icon="📅",
    layout="wide"
)

st.title("📅 Weekly Review")

df = load_reviews()

if df.empty:
    st.warning("No Review Data Found")
    st.stop()

# Column names normalize
df.columns = (
    df.columns
    .astype(str)
    .str.strip()
    .str.lower()
    .str.replace(" ", "_")
)

required = [
    "date",
    "coordinator",
    "task",
    "frequency",
    "priority",
    "status"
]

missing = [c for c in required if c not in df.columns]

if missing:
    st.error(f"Missing Columns: {missing}")
    st.write("Available Columns:", list(df.columns))
    st.stop()
# ---------------- Filters ----------------

c1, c2, c3 = st.columns(3)

with c1:
    coordinator = st.selectbox(
        "Coordinator",
        ["All"] + sorted(df["coordinator"].dropna().unique().tolist())
    )

with c2:
    status = st.selectbox(
        "Status",
        ["All"] + sorted(df["status"].dropna().unique().tolist())
    )

with c3:
    priority = st.selectbox(
        "Priority",
        ["All"] + sorted(df["priority"].dropna().unique().tolist())
    )

if coordinator != "All":
    df = df[df["coordinator"] == coordinator]

if status != "All":
    df = df[df["status"] == status]

if priority != "All":
    df = df[df["priority"] == priority]

# ---------------- KPI ----------------

total = len(df)

completed = len(df[df["status"] == "Completed"])

pending = len(df[df["status"] == "Pending"])

percent = round((completed / total) * 100, 1) if total else 0

a, b, c, d = st.columns(4)

a.metric("Total Tasks", total)
b.metric("Completed", completed)
c.metric("Pending", pending)
d.metric("Completion %", f"{percent}%")

st.progress(percent / 100)

st.divider()

# ---------------- Coordinator Summary ----------------

summary = (

    df.groupby(
        ["coordinator", "status"]
    )

    .size()

    .unstack(fill_value=0)

    .reset_index()

)

st.subheader("Coordinator Summary")

st.dataframe(
    summary,
    use_container_width=True,
    hide_index=True
)

# ---------------- Chart ----------------

chart = (

    df[df["status"] == "Completed"]

    .groupby("coordinator")

    .size()

    .reset_index(name="Completed")

)

if not chart.empty:

    fig = px.bar(

        chart,

        x="coordinator",

        y="Completed",

        text="Completed",

        color="Completed"

    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# ---------------- Recent ----------------

st.subheader("Review Records")

st.dataframe(
    df.sort_values("date", ascending=False),
    use_container_width=True,
    hide_index=True
)
