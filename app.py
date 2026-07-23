import streamlit as st

from config import *

st.set_page_config(
    page_title=APP_NAME,
    page_icon=APP_ICON,
    layout="wide"
)

st.logo("https://img.icons8.com/color/96/hospital-3.png")

st.title(f"{APP_ICON} {APP_NAME}")

st.caption(f"{DEPARTMENT} | {APP_YEAR}")

st.markdown("---")

st.success("✅ Use the LEFT SIDEBAR to open Dashboard, Daily Review, Weekly Review, Pending Tracker and Reports.")
