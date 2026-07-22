# ==========================================================
# helper.py
# Common Helper Functions
# ==========================================================

from datetime import datetime
import pandas as pd


# ----------------------------------------------------------
# Current Date
# ----------------------------------------------------------

def today():
    return datetime.now().strftime("%d-%m-%Y")


# ----------------------------------------------------------
# Current Time
# ----------------------------------------------------------

def current_time():
    return datetime.now().strftime("%I:%M %p")


# ----------------------------------------------------------
# Current Week Number
# ----------------------------------------------------------

def current_week():
    return datetime.now().isocalendar()[1]


# ----------------------------------------------------------
# Current Month
# ----------------------------------------------------------

def current_month():
    return datetime.now().strftime("%B")


# ----------------------------------------------------------
# Completion Percentage
# ----------------------------------------------------------

def completion_percentage(total, completed):

    if total == 0:
        return 0

    return round((completed / total) * 100, 2)


# ----------------------------------------------------------
# Pending Count
# ----------------------------------------------------------

def pending_count(total, completed):

    return total - completed


# ----------------------------------------------------------
# Performance Grade
# ----------------------------------------------------------

def performance_grade(score):

    if score >= 95:
        return "Excellent"

    elif score >= 85:
        return "Very Good"

    elif score >= 70:
        return "Good"

    elif score >= 50:
        return "Average"

    else:
        return "Poor"


# ----------------------------------------------------------
# Status Color
# ----------------------------------------------------------

def status_color(status):

    status = str(status).lower()

    if status == "completed":
        return "🟢"

    elif status == "pending":
        return "🟡"

    elif status == "overdue":
        return "🔴"

    else:
        return "⚪"


# ----------------------------------------------------------
# Empty Daily Review DataFrame
# ----------------------------------------------------------

def create_daily_dataframe(tasks, coordinators):

    data = []

    for task in tasks:

        row = {
            "Task": task["name"],
            "Frequency": task["frequency"],
            "Priority": task["priority"]
        }

        for coordinator in coordinators:
            row[coordinator] = False

        row["Remarks"] = ""

        data.append(row)

    return pd.DataFrame(data)


# ----------------------------------------------------------
# Score Calculation
# ----------------------------------------------------------

def calculate_score(completed, total):

    if total == 0:
        return 0

    return round((completed / total) * 100)


# ----------------------------------------------------------
# Ranking
# ----------------------------------------------------------

def rank_dataframe(df, score_column="Score"):

    df = df.copy()

    df["Rank"] = (
        df[score_column]
        .rank(method="dense", ascending=False)
        .astype(int)
    )

    return df
