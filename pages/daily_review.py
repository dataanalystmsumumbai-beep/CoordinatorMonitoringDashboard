import streamlit as st
import pandas as pd

from config import MASTER_TASKS, COORDINATORS

st.set_page_config(
    page_title="Daily Review",
    page_icon="📋",
    layout="wide"
)

st.title("📋 Daily Review")

st.divider()

# -----------------------------
# Top Filters
# -----------------------------

col1, col2 = st.columns(2)

with col1:
    review_date = st.date_input("Review Date")

with col2:
    coordinator = st.selectbox(
        "Coordinator",
        COORDINATORS
    )

st.divider()

# -----------------------------
# Create Table
# -----------------------------

rows = []

for task in MASTER_TASKS:

    rows.append({
        "Task": task["name"],
        "Frequency": task["frequency"],
        "Priority": task["priority"],
        "Completed": False,
        "Remarks": ""
    })

df = pd.DataFrame(rows)

edited_df = st.data_editor(

    df,

    use_container_width=True,

    hide_index=True,

    num_rows="fixed"

)

st.divider()

# -----------------------------
# Summary
# -----------------------------

completed = edited_df["Completed"].sum()

total = len(edited_df)

pending = total - completed

percent = round((completed / total) * 100, 1)

c1, c2, c3, c4 = st.columns(4)

c1.metric("Total", total)

c2.metric("Completed", completed)

c3.metric("Pending", pending)

c4.metric("Completion", f"{percent}%")

st.progress(percent / 100)

st.divider()

# -----------------------------
# Save Button
# -----------------------------

if st.button("💾 Save Review"):

    st.success(
        "Review Saved Successfully (Google Sheet Integration Next Step)"
    )
