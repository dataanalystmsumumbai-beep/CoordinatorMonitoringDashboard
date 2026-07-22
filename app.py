import streamlit as st
from config import APP_NAME, APP_ICON, APP_YEAR, DEPARTMENT

# -------------------------------------------------------
# Page Config
# -------------------------------------------------------

st.set_page_config(
    page_title=APP_NAME,
    page_icon=APP_ICON,
    layout="wide",
    initial_sidebar_state="expanded"
)

# -------------------------------------------------------
# Sidebar
# -------------------------------------------------------

with st.sidebar:

    st.image(
        "https://img.icons8.com/color/96/hospital-3.png",
        width=70
    )

    st.title("Coordinator Portal")

    page = st.radio(
        "Navigation",
        [
            "🏠 Dashboard",
            "📋 Daily Review",
            "📅 Weekly Review",
            "🚨 Pending Tracker",
            "📊 Reports",
            "⚙ Settings"
        ]
    )

    st.divider()

    st.caption(APP_YEAR)
    st.caption(DEPARTMENT)

# -------------------------------------------------------
# Header
# -------------------------------------------------------

st.title(f"{APP_ICON} {APP_NAME}")

st.markdown("---")

# -------------------------------------------------------
# Dashboard Cards
# -------------------------------------------------------

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("📋 Total Tasks", 15)

with col2:
    st.metric("✅ Completed", 0)

with col3:
    st.metric("⏳ Pending", 15)

with col4:
    st.metric("📈 Completion", "0 %")

st.markdown("---")

# -------------------------------------------------------
# Navigation
# -------------------------------------------------------

if page == "🏠 Dashboard":

    st.header("Executive Dashboard")

    st.info("Dashboard Module Coming Soon")

elif page == "📋 Daily Review":

    st.header("Daily Review")

    st.info("Daily Review Module Coming Soon")

elif page == "📅 Weekly Review":

    st.header("Weekly Review")

    st.info("Weekly Review Module Coming Soon")

elif page == "🚨 Pending Tracker":

    st.header("Pending Tracker")

    st.info("Pending Tracker Module Coming Soon")

elif page == "📊 Reports":

    st.header("Reports")

    st.info("Reports Module Coming Soon")

elif page == "⚙ Settings":

    st.header("Settings")

    st.info("Settings Module Coming Soon")

st.markdown("---")

st.caption("Ward Coordinator Monitoring Dashboard | Public Health Department")
