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

    st.warning("No Data Available")

    st.stop()

st.dataframe(

    df,

    use_container_width=True,

    hide_index=True

)

excel = export_excel(df)

st.download_button(

    "📥 Download Excel Report",

    excel,

    "Coordinator_Report.xlsx",

    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",

    use_container_width=True

)
