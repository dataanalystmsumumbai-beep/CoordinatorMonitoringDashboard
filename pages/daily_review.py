import streamlit as st
from datetime import date
from config import MASTER_TASKS
from utils.google_sheets import load_coordinators
from utils.google_sheets import save_review
from utils.theme import load_css

st.set_page_config(
    page_title="Daily Review",
    page_icon="📋",
    layout="wide"
)

load_css()

st.title("📋 Daily Review")
st.divider()

col1, col2 = st.columns(2)

with col1:
    review_date = st.date_input(
        "Review Date",
        value=date.today()
    )

with col2:
    coordinators = load_coordinators()

if isinstance(coordinators, list):

    coordinator_list = []

    for row in coordinators:

        if "Coordinator" in row:

            coordinator_list.append(
                row["Coordinator"]
            )

else:

    coordinator_list = []

coordinator = st.selectbox(

    "Coordinator",

    coordinator_list

)

st.divider()

st.subheader("Reports Review")

records = []

completed = 0

for task in MASTER_TASKS:

    c1, c2, c3 = st.columns([5,2,4])

    with c1:
        st.write(task["name"])

    with c2:
        done = st.checkbox(
            "Completed",
            key=task["name"]
        )

    with c3:
        remarks = st.text_input(
            "Remarks",
            key=task["name"]+"_remarks",
            label_visibility="collapsed",
            placeholder="Remarks..."
        )

    status = "Completed" if done else "Pending"

    if done:
        completed += 1

    records.append({

        "date": str(review_date),

        "coordinator": coordinator,

        "task": task["name"],

        "frequency": task["frequency"],

        "priority": task["priority"],

        "status": status,

        "remarks": remarks

    })

total = len(records)

pending = total - completed

percent = round(completed / total * 100, 1)

st.divider()

a, b, c, d = st.columns(4)

a.metric("Total Tasks", total)

b.metric("Completed", completed)

c.metric("Pending", pending)

d.metric("Completion", f"{percent}%")

st.progress(percent / 100)

st.divider()

if st.button(
    "💾 SAVE TODAY'S REVIEW",
    use_container_width=True,
    type="primary"
):

    progress = st.progress(0)

    saved = 0

    for i, row in enumerate(records):

        response = save_review(

            row["date"],
            row["coordinator"],
            row["task"],
            row["frequency"],
            row["priority"],
            row["status"],
            row["remarks"]

        )

        if response.get("success", False):
            saved += 1

        progress.progress((i + 1) / len(records))

    st.success(f"✅ {saved} / {len(records)} Tasks Saved Successfully")

    st.balloons()

    st.rerun()
