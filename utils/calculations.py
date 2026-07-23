import pandas as pd


def total_tasks(df):
    return len(df)


def completed_tasks(df):

    if df.empty:
        return 0

    return len(
        df[df["status"] == "Completed"]
    )


def pending_tasks(df):

    if df.empty:
        return 0

    return len(
        df[df["status"] == "Pending"]
    )


def completion_percentage(df):

    total = total_tasks(df)

    if total == 0:
        return 0

    completed = completed_tasks(df)

    return round(
        completed / total * 100,
        1
    )


def coordinator_summary(df):

    if df.empty:
        return pd.DataFrame()

    return (

        df.groupby(
            [
                "coordinator",
                "status"
            ]
        )

        .size()

        .unstack(fill_value=0)

        .reset_index()

    )


def daily_summary(df):

    if df.empty:
        return pd.DataFrame()

    return (

        df.groupby(
            [
                "date",
                "status"
            ]
        )

        .size()

        .reset_index(name="Count")

    )


def pending_dataframe(df):

    if df.empty:
        return pd.DataFrame()

    return df[
        df["status"] == "Pending"
    ]
