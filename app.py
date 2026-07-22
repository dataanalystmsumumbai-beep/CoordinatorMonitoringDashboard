import streamlit as st

st.set_page_config(
    page_title="Ward Coordinator Monitoring Dashboard",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("🏥 Ward Coordinator Monitoring Dashboard")

st.markdown("---")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Tasks", "15")
col2.metric("Completed", "0")
col3.metric("Pending", "15")
col4.metric("Completion", "0%")

st.markdown("---")

st.subheader("📋 Reports to be Monitored")

tasks = [
    "Daily Non Reporting",
    "Health Post Wise Report",
    "ARV & Tamiflu Stock",
    "Ward Profiling",
    "Action Taken Report",
    "Lab Tech Report",
    "Death CIF",
    "Lepto CIF",
    "IHIP Issues",
    "Ebola Follow-up",
    "Address Verification",
    "Other Ward Issues",
    "S,P & L Form",
    "Disease Trend Analysis",
    "Health Infrastructure"
]

for task in tasks:
    st.checkbox(task)
