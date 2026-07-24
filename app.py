import streamlit as st
from config import *

st.set_page_config(
    page_title=APP_NAME,
    page_icon=APP_ICON,
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title(f"{APP_ICON} {APP_NAME}")

st.caption(
    f"{DEPARTMENT} | {APP_YEAR}"
)

st.success(
    "👈 Select a page from the left sidebar."
)
