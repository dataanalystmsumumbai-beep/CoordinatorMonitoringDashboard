import streamlit as st

from utils.google_sheets import load_reviews
from utils.export import export_excel

st.set_page_config(

    page_title="Reports",

    page_icon="📄",

    layout="wide"

)

st.title("📄 Reports")

df = load_reviews()

if df.empty:

    st.warning("No Records")

    st.stop()

c1, c2, c3 = st.columns(3)

with c1:

    coordinator = st.selectbox(

        "Coordinator",

        ["All"] + sorted(df["coordinator"].unique())

    )

with c2:

    status = st.selectbox(

        "Status",

        ["All"] + sorted(df["status"].unique())

    )

with c3:

    priority = st.selectbox(

        "Priority",

        ["All"] + sorted(df["priority"].unique())

    )

if coordinator != "All":

    df = df[df["coordinator"] == coordinator]

if status != "All":

    df = df[df["status"] == status]

if priority != "All":

    df = df[df["priority"] == priority]

st.dataframe(

    df,

    use_container_width=True,

    hide_index=True

)

excel = export_excel(df)

st.download_button(

    "📥 Download Excel",

    excel,

    "Coordinator_Report.xlsx",

    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",

    use_container_width=True

)
