import streamlit as st

def load_css():

    with open("assets/style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


def card(title, value, color):

    st.markdown(f"""
    <div style="
        background:white;
        border-radius:18px;
        padding:22px;
        box-shadow:0 4px 18px rgba(0,0,0,.08);
        border-top:6px solid {color};
        text-align:center;
        margin-bottom:10px;
    ">

    <div style="
        color:gray;
        font-size:17px;
        font-weight:600;
    ">
        {title}
    </div>

    <div style="
        font-size:38px;
        color:#0F172A;
        font-weight:bold;
        margin-top:8px;
    ">
        {value}
    </div>

    </div>
    """, unsafe_allow_html=True)
