# ==========================================================
# Ward Coordinator Monitoring Dashboard
# config.py
# ==========================================================

APP_NAME = "Ward Coordinator Monitoring Dashboard"

APP_YEAR = "2026"

DEPARTMENT = "Public Health Department"

APP_ICON = "🏥"

# ----------------------------------------------------------
# Coordinators
# ----------------------------------------------------------

COORDINATORS = [
    "Coordinator 1",
    "Coordinator 2",
    "Coordinator 3",
    "Coordinator 4"
]

# ----------------------------------------------------------
# Frequencies
# ----------------------------------------------------------

FREQUENCIES = [
    "Daily",
    "Weekly",
    "Monthly",
    "As Required"
]

# ----------------------------------------------------------
# Priority
# ----------------------------------------------------------

PRIORITY = [
    "High",
    "Medium",
    "Low"
]

# ----------------------------------------------------------
# Status
# ----------------------------------------------------------

STATUS = [
    "Completed",
    "Pending",
    "Overdue"
]

# ----------------------------------------------------------
# Master Reports
# ----------------------------------------------------------

MASTER_TASKS = [

{
"name":"Daily Non Reporting Wards",
"frequency":"Daily",
"priority":"High"
},

{
"name":"Health Post Wise Report",
"frequency":"Daily",
"priority":"High"
},

{
"name":"ARV & Tamiflu Stock",
"frequency":"Weekly",
"priority":"Medium"
},

{
"name":"Ward Profiling",
"frequency":"Monthly",
"priority":"Low"
},

{
"name":"Action Taken Report",
"frequency":"Weekly",
"priority":"High"
},

{
"name":"Lab Tech Report",
"frequency":"Weekly",
"priority":"Medium"
},

{
"name":"Death CIF",
"frequency":"Daily",
"priority":"High"
},

{
"name":"Lepto CIF",
"frequency":"Daily",
"priority":"High"
},

{
"name":"IHIP Issues",
"frequency":"Daily",
"priority":"High"
},

{
"name":"Ebola Follow-up",
"frequency":"Weekly",
"priority":"Medium"
},

{
"name":"Address Verification",
"frequency":"Daily",
"priority":"High"
},

{
"name":"Other Ward Issues",
"frequency":"As Required",
"priority":"Medium"
},

{
"name":"S, P & L Form",
"frequency":"Daily",
"priority":"High"
},

{
"name":"Disease Trend Analysis",
"frequency":"Weekly",
"priority":"Medium"
},

{
"name":"Health Infrastructure",
"frequency":"Weekly",
"priority":"Medium"
},

{
"name":"Additional Tasks",
"frequency":"As Required",
"priority":"Low"
}

]

# ----------------------------------------------------------
# Dashboard Cards
# ----------------------------------------------------------

KPI_CARDS = [

"Total Tasks",

"Completed",

"Pending",

"Completion %"

]

# ----------------------------------------------------------
# Theme
# ----------------------------------------------------------

PRIMARY_COLOR = "#1565C0"

SUCCESS_COLOR = "#2E7D32"

WARNING_COLOR = "#F9A825"

DANGER_COLOR = "#C62828"
