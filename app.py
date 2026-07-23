import streamlit as st
from config import APP_NAME, APP_ICON

st.set_page_config(
    page_title=APP_NAME,
    page_icon=APP_ICON,
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title(f"{APP_ICON} {APP_NAME}")

st.info("👈 Open a module from the left sidebar.")
