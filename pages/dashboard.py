import streamlit as st
import plotly.express as px
import pandas as pd

st.set_page_config(
    page_title="Executive Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Executive Dashboard")

st.markdown("---")

# Dummy values (Google Sheet integration पुढच्या step मध्ये)
total = 16
completed = 10
pending = total - completed
percent = round(completed / total * 100, 1)

c1, c2, c3, c4 = st.columns(4)

c1.metric("📋 Total Tasks", total)
c2.metric("✅ Completed", completed)
c3.metric("⏳ Pending", pending)
c4.metric("📈 Completion", f"{percent}%")

st.progress(percent / 100)

st.markdown("---")

left, right = st.columns(2)

# Pie Chart
pie = pd.DataFrame({
    "Status": ["Completed", "Pending"],
    "Count": [completed, pending]
})

with left:
    fig = px.pie(
        pie,
        names="Status",
        values="Count",
        hole=0.5,
        title="Task Status"
    )
    st.plotly_chart(fig, use_container_width=True)

# Coordinator Performance
performance = pd.DataFrame({

    "Coordinator": [

        "Coordinator 1",
        "Coordinator 2",
        "Coordinator 3",
        "Coordinator 4"

    ],

    "Completed":[15,12,10,8]

})

with right:

    fig = px.bar(

        performance,

        x="Coordinator",

        y="Completed",

        text="Completed",

        title="Coordinator Performance"

    )

    st.plotly_chart(fig, use_container_width=True)

st.markdown("---")

trend = pd.DataFrame({

    "Day":[

        "Mon",

        "Tue",

        "Wed",

        "Thu",

        "Fri",

        "Sat",

        "Sun"

    ],

    "Completion":[

        55,

        65,

        72,

        80,

        75,

        90,

        82

    ]

})

fig = px.line(

    trend,

    x="Day",

    y="Completion",

    markers=True,

    title="Weekly Completion Trend"

)

st.plotly_chart(fig, use_container_width=True)

st.success("Dashboard Connected Successfully")
