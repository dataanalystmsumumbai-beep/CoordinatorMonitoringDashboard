import streamlit as st
import pandas as pd
from config import *

from utils.theme import load_css

st.set_page_config(
    page_title="Settings",
    page_icon="⚙️",
    layout="wide"
)

load_css()

st.title("⚙️ Settings")

tab1, tab2, tab3 = st.tabs([
    "👨‍💼 Coordinators",
    "📋 Master Tasks",
    "ℹ️ Application"
])

# -------------------------------------------------------
# Coordinators
# -------------------------------------------------------

with tab1:

    st.subheader("Coordinator Master")

    df = pd.DataFrame({
        "Coordinator Name": COORDINATORS
    })

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True
    )

    st.info(
        "Coordinator list is managed from config.py"
    )

# -------------------------------------------------------
# Tasks
# -------------------------------------------------------

with tab2:

    st.subheader("Master Task List")

    task_df = pd.DataFrame(MASTER_TASKS)

    task_df.index = task_df.index + 1

    st.dataframe(
        task_df,
        use_container_width=True
    )

    st.metric(
        "Total Tasks",
        len(task_df)
    )

# -------------------------------------------------------
# Application
# -------------------------------------------------------

with tab3:

    c1, c2 = st.columns(2)

    c1.metric(
        "Application",
        APP_NAME
    )

    c2.metric(
        "Year",
        APP_YEAR
    )

    st.write("Department")

    st.success(DEPARTMENT)

    st.divider()

    st.write("Theme")

    st.code(PRIMARY_COLOR)

    st.write("Version")

    st.success("Version 1.0")

    st.divider()

    st.caption(
        "Developed using Streamlit + Google Sheets + Apps Script"
    )
