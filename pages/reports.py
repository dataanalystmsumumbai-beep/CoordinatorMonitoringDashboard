import streamlit as st
import pandas as pd

from utils.export import dataframe_to_excel

st.set_page_config(
    page_title="Reports",
    page_icon="📄",
    layout="wide"
)

st.title("📄 Reports")

st.divider()

sample = pd.DataFrame({

    "Coordinator":[
        "Coordinator 1",
        "Coordinator 2",
        "Coordinator 3",
        "Coordinator 4"
    ],

    "Completed":[15,14,13,12],

    "Pending":[1,2,3,4]

})

st.dataframe(
    sample,
    use_container_width=True
)

excel = dataframe_to_excel(sample)

st.download_button(

    "📥 Download Excel Report",

    data=excel,

    file_name="Coordinator_Report.xlsx",

    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"

)
