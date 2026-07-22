import streamlit as st
from datetime import date

from config import MASTER_TASKS, COORDINATORS
from utils.google_sheets import save_review

st.set_page_config(
    page_title="Daily Review",
    page_icon="📋",
    layout="wide"
)

st.title("📋 Daily Review")

st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    review_date = st.date_input(
        "Review Date",
        value=date.today()
    )

with col2:
    coordinator = st.selectbox(
        "Coordinator",
        COORDINATORS
    )

st.markdown("---")

st.subheader("Task Review")

for task in MASTER_TASKS:

    with st.container(border=True):

        st.markdown(f"### {task['name']}")

        c1, c2 = st.columns([1,2])

        with c1:

            status = st.selectbox(

                "Status",

                [

                    "Completed",

                    "Pending",

                    "Not Applicable"

                ],

                key=task["name"]

            )

        with c2:

            remarks = st.text_input(

                "Remarks",

                key=task["name"]+"_remarks"

            )

        if st.button(

            f"💾 Save {task['name']}",

            key="save_"+task["name"]

        ):

            result = save_review(

                review_date,

                coordinator,

                task["name"],

                task["frequency"],

                task["priority"],

                status,

                remarks

            )

            if result["success"]:

                st.success("Saved Successfully")

            else:

                st.error(result["message"])
