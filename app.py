import streamlit as st

# -------------------------------
# Page Configuration
# -------------------------------
st.set_page_config(
    page_title="Ward Coordinator Monitoring Dashboard",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -------------------------------
# Sidebar
# -------------------------------
st.sidebar.title("🏥 Coordinator Dashboard")

menu = st.sidebar.radio(
    "Navigation",
    [
        "Dashboard",
        "Daily Review",
        "Weekly Review",
        "Pending Tracker",
        "Reports",
        "Settings"
    ]
)

# -------------------------------
# Home Page
# -------------------------------
st.title("🏥 Ward Coordinator Monitoring Dashboard")

st.caption("Public Health Department")

st.divider()

col1,col2,col3,col4=st.columns(4)

col1.metric("Total Tasks","15")
col2.metric("Completed","0")
col3.metric("Pending","15")
col4.metric("Completion","0%")

st.divider()

if menu=="Dashboard":

    st.subheader("Dashboard")

    st.info("Dashboard will be available soon.")

elif menu=="Daily Review":

    st.subheader("Daily Review")

elif menu=="Weekly Review":

    st.subheader("Weekly Review")

elif menu=="Pending Tracker":

    st.subheader("Pending Tracker")

elif menu=="Reports":

    st.subheader("Reports")

elif menu=="Settings":

    st.subheader("Settings")
