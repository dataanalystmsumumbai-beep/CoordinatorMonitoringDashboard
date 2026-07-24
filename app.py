import streamlit as st
from config import *
from utils.theme import load_css

st.set_page_config(
    page_title=APP_NAME,
    page_icon=APP_ICON,
    layout="wide",
    initial_sidebar_state="expanded"
)

load_css()

st.title(f"{APP_ICON} {APP_NAME}")

st.caption(
    f"{DEPARTMENT} | {APP_YEAR}"
)

st.success(
    "👈 Select a page from the left sidebar."
)
