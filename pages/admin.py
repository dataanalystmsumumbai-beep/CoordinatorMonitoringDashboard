import streamlit as st

st.set_page_config(
    page_title="Admin Panel",
    page_icon="⚙️",
    layout="wide"
)

st.title("⚙️ Admin Panel")

tab1, tab2 = st.tabs([
    "👤 Coordinators",
    "📋 Master Tasks"
])

with tab1:
    st.subheader("Coordinator Management")
    st.info("Coming in next step...")

with tab2:
    st.subheader("Master Task Management")
    st.info("Coming in next step...")
