import streamlit as st
import pandas as pd
from config import COORDINATORS, MASTER_TASKS

st.set_page_config(
    page_title="Settings",
    page_icon="⚙️",
    layout="wide"
)

st.title("⚙️ Settings")

tab1, tab2 = st.tabs(["Coordinators", "Master Tasks"])

with tab1:

    st.subheader("Coordinator List")

    st.dataframe(
        pd.DataFrame(
            {"Coordinator": COORDINATORS}
        ),
        use_container_width=True,
        hide_index=True
    )

with tab2:

    st.subheader("Master Task List")

    df = pd.DataFrame(MASTER_TASKS)

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True
    )
