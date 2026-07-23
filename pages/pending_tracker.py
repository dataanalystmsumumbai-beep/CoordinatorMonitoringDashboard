import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Pending Tracker",
    page_icon="⏳",
    layout="wide"
)

st.title("⏳ Pending Tracker")

st.divider()

# -----------------------------
# Temporary Data
# (नंतर Google Sheet मधून येईल)
# -----------------------------

data = pd.DataFrame({

    "Coordinator":[

        "Coordinator 1",
        "Coordinator 1",
        "Coordinator 2",
        "Coordinator 2",
        "Coordinator 3",
        "Coordinator 4"

    ],

    "Task":[

        "Health Post Wise Report",

        "Death CIF",

        "Lab Tech Report",

        "Lepto CIF",

        "Disease Trend",

        "Action Taken Report"

    ],

    "Priority":[

        "High",

        "Medium",

        "High",

        "Low",

        "Medium",

        "High"

    ],

    "Status":[

        "Pending",

        "Pending",

        "Pending",

        "Pending",

        "Pending",

        "Pending"

    ]

})

# -----------------------------
# Filters
# -----------------------------

col1,col2=st.columns(2)

with col1:

    coordinator=st.selectbox(

        "Coordinator",

        ["All"]+sorted(data["Coordinator"].unique())

    )

with col2:

    priority=st.selectbox(

        "Priority",

        ["All","High","Medium","Low"]

    )

df=data.copy()

if coordinator!="All":

    df=df[df["Coordinator"]==coordinator]

if priority!="All":

    df=df[df["Priority"]==priority]

st.metric(

    "Pending Tasks",

    len(df)

)

st.dataframe(

    df,

    use_container_width=True,

    hide_index=True

)

st.divider()

st.subheader("Pending Summary")

summary=df.groupby("Coordinator").size().reset_index(name="Pending")

st.bar_chart(

    summary,

    x="Coordinator",

    y="Pending"

)
