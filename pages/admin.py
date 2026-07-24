import streamlit as st
from utils.google_sheets import add_coordinator

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

    st.subheader("👤 Coordinator Management")

    name = st.text_input(
        "Coordinator Name"
    )

    if st.button(
        "➕ Add Coordinator",
        use_container_width=True
    ):

        if name.strip() == "":

            st.warning("Enter Coordinator Name")

        else:

            result = add_coordinator(name)

            if result["success"]:

                st.success("Coordinator Added Successfully")

            else:

                st.error(result)

with tab2:
    st.subheader("Master Task Management")
    st.info("Coming in next step...")
