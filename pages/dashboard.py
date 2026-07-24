import streamlit as st
import pandas as pd
import plotly.express as px

from utils.theme import load_css

from utils.google_sheets import load_reviews

st.set_page_config(
    page_title="Executive Dashboard",
    page_icon="📊",
    layout="wide"
)

load_css()

from datetime import datetime

today = datetime.now().strftime("%d %B %Y")

st.markdown(f"""
<div style="background:linear-gradient(90deg,#1565C0,#1E88E5);
padding:20px;
border-radius:15px;
color:white;
margin-bottom:20px;">

<h1 style="color:white;margin:0;">
🏥 Ward Coordinator Monitoring Dashboard
</h1>

<p style="font-size:18px;margin:5px 0;">
Public Health Department | BMC
</p>

<p style="margin:0;">
📅 {today}
</p>

</div>
""", unsafe_allow_html=True)

st.title("📊 Executive Dashboard")

data = load_reviews()

if isinstance(data, list):
    df = pd.DataFrame(data)
else:
    df = data.copy()

if df.empty:
    st.warning("No Review Data Available")
    st.stop()

# ---------------- Clean ----------------

df.columns = [str(c).strip().lower() for c in df.columns]

required = [
    "date",
    "coordinator",
    "task",
    "frequency",
    "priority",
    "status"
]

for col in required:
    if col not in df.columns:
        st.error(f"Missing Column : {col}")
        st.stop()

# ---------------- KPIs ----------------

total = len(df)

completed = len(df[df["status"] == "Completed"])

pending = len(df[df["status"] == "Pending"])

completion = round(
    completed / total * 100,
    1
) if total else 0

high_pending = len(
    df[
        (df["status"] == "Pending") &
        (df["priority"] == "High")
    ]
)

c1, c2, c3, c4, c5 = st.columns(5)

with c1:
    st.metric("📋 Total Tasks", total)

with c2:
    st.metric("✅ Completed", completed)

with c3:
    st.metric("⏳ Pending", pending)

with c4:
    st.metric("🔥 High Priority", high_pending)

with c5:
    st.metric("📈 Completion", f"{completion}%")

st.subheader("Overall Progress")

st.progress(completion / 100)

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

        hole=.55

    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# ---------------- Ranking ----------------

rank = (

    df[df["status"] == "Completed"]

    .groupby("coordinator")

    .size()

    .reset_index(name="Completed")

    .sort_values(
        "Completed",
        ascending=False
    )

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

# ---------------- Priority ----------------

priority = (

    df.groupby("priority")

    .size()

    .reset_index(name="Count")

)

fig = px.bar(

    priority,

    x="priority",

    y="Count",

    text="Count",

    color="priority"

)

st.plotly_chart(
    fig,
    use_container_width=True
)

# ---------------- Daily Trend ----------------

trend = (

    df.groupby(
        [
            "date",
            "status"
        ]
    )

    .size()

    .reset_index(name="Count")

)

fig = px.line(

    trend,

    x="date",

    y="Count",

    color="status",

    markers=True

)

st.plotly_chart(
    fig,
    use_container_width=True
)

# ---------------- Recent Reviews ----------------

st.subheader("Latest Reviews")

st.dataframe(

    df.sort_values(
        "date",
        ascending=False
    ),

    use_container_width=True,

    hide_index=True

)

# ---------------- Coordinator Score ----------------

st.subheader("🏆 Coordinator Performance")

score = (

    df.groupby("coordinator")

    .agg(

        Total=("task", "count"),

        Completed=("status", lambda x: (x == "Completed").sum()),

        Pending=("status", lambda x: (x == "Pending").sum())

    )

    .reset_index()

)

score["Completion %"] = round(
    score["Completed"] /
    score["Total"] * 100,
    1
)

score = score.sort_values(
    "Completion %",
    ascending=False
)

st.dataframe(
    score,
    use_container_width=True,
    hide_index=True
)

st.markdown("---")

st.caption(
    "Ward Coordinator Monitoring Dashboard | Version 1.1 | Public Health Department"
)
