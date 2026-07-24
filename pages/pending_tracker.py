import streamlit as st
from utils.google_sheets import load_reviews

st.set_page_config(
    page_title="Pending Tracker",
    page_icon="🚨",
    layout="wide"
)

st.title("🚨 Pending Tracker")

df = load_reviews()

if df.empty:
    st.warning("No Data")
    st.stop()

pending = df[df["status"] == "Pending"]

c1, c2, c3 = st.columns(3)

c1.metric("Pending", len(pending))
c2.metric("High Priority", len(pending[pending["priority"]=="High"]))
c3.metric("Medium Priority", len(pending[pending["priority"]=="Medium"]))

st.dataframe(
    pending,
    use_container_width=True,
    hide_index=True
)

st.bar_chart(
    pending.groupby("coordinator").size()
)
