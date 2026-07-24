import streamlit as st
import pandas as pd

from utils.google_sheets import load_reviews
from utils.export import export_excel

st.set_page_config(
    page_title="Reports",
    page_icon="📄",
    layout="wide"
)

st.title("📄 Reports")

data = load_reviews()

if isinstance(data, list):
    df = pd.DataFrame(data)
else:
    df = data.copy()

if df.empty:
    st.warning("No Review Records Found")
    st.stop()

df.columns = [str(c).strip().lower() for c in df.columns]

# ---------------- Filters ----------------

c1, c2, c3, c4 = st.columns(4)

with c1:

    coordinator = st.selectbox(

        "Coordinator",

        ["All"] + sorted(
            df["coordinator"].dropna().unique().tolist()
        )

    )

with c2:

    status = st.selectbox(

        "Status",

        ["All"] + sorted(
            df["status"].dropna().unique().tolist()
        )

    )

with c3:

    priority = st.selectbox(

        "Priority",

        ["All"] + sorted(
            df["priority"].dropna().unique().tolist()
        )

    )

with c4:

    frequency = st.selectbox(

        "Frequency",

        ["All"] + sorted(
            df["frequency"].dropna().unique().tolist()
        )

    )

# ---------------- Apply Filters ----------------

report = df.copy()

if coordinator != "All":
    report = report[
        report["coordinator"] == coordinator
    ]

if status != "All":
    report = report[
        report["status"] == status
    ]

if priority != "All":
    report = report[
        report["priority"] == priority
    ]

if frequency != "All":
    report = report[
        report["frequency"] == frequency
    ]

# ---------------- KPIs ----------------

a, b, c, d = st.columns(4)

a.metric("Total Records", len(report))

b.metric(
    "Completed",
    len(report[report.status == "Completed"])
)

c.metric(
    "Pending",
    len(report[report.status == "Pending"])
)

d.metric(
    "High Priority",
    len(
        report[
            report.priority == "High"
        ]
    )
)

st.divider()

# ---------------- Table ----------------

st.dataframe(

    report,

    use_container_width=True,

    hide_index=True

)

# ---------------- Download ----------------

excel = export_excel(report)

st.download_button(

    "📥 Download Excel Report",

    data=excel,

    file_name="Coordinator_Report.xlsx",

    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",

    use_container_width=True

)

# ---------------- Summary ----------------

st.subheader("Coordinator Summary")

summary = (

    report.groupby(

        "coordinator"

    )

    .agg(

        Total=("task", "count"),

        Completed=("status", lambda x: (x == "Completed").sum()),

        Pending=("status", lambda x: (x == "Pending").sum())

    )

    .reset_index()

)

summary["Completion %"] = round(

    summary["Completed"]

    /

    summary["Total"]

    * 100,

    1

)

st.dataframe(

    summary,

    use_container_width=True,

    hide_index=True

)
