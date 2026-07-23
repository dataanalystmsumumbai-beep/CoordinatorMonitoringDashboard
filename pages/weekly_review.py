import streamlit as st
import pandas as pd

from utils.google_sheets import load_reviews

st.set_page_config(
    page_title="Weekly Review",
    page_icon="📅",
    layout="wide"
)

st.title("📅 Weekly Review")

st.divider()

# -----------------------
# Load Google Sheet Data
# -----------------------

data = load_reviews()

if len(data) == 0:

    st.warning("No Review Data Found")

    st.stop()

df = pd.DataFrame(data)

# -----------------------
# Rename Columns (if required)
# -----------------------

rename_map = {
    "Review Date": "Date",
    "Coordinator": "Coordinator",
    "Task": "Task",
    "Frequency": "Frequency",
    "Priority": "Priority",
    "Status": "Status",
    "Remarks": "Remarks"
}

df.rename(columns=rename_map, inplace=True)

# -----------------------
# KPIs
# -----------------------

total = len(df)

completed = len(df[df["Status"] == "Completed"])

pending = len(df[df["Status"] == "Pending"])

percent = round((completed / total) * 100, 1) if total else 0

c1, c2, c3, c4 = st.columns(4)

c1.metric("Total Reviews", total)

c2.metric("Completed", completed)

c3.metric("Pending", pending)

c4.metric("Completion %", f"{percent}%")

st.progress(percent / 100)

st.divider()

# -----------------------
# Coordinator Summary
# -----------------------

st.subheader("Coordinator Summary")

summary = (

    df.groupby(["Coordinator", "Status"])

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

    summary.set_index("Coordinator")

)

st.divider()

# -----------------------
# Pending Tasks
# -----------------------

st.subheader("Pending Tasks")

pending_df = df[df["Status"] == "Pending"]

st.dataframe(

    pending_df,

    use_container_width=True,

    hide_index=True

)
