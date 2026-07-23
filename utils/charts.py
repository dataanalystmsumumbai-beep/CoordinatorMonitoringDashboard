import plotly.express as px


def pie_chart(df):

    fig = px.pie(

        df,

        names="Status",

        values="Count",

        hole=.60

    )

    fig.update_layout(
        height=400
    )

    return fig


def coordinator_chart(df):

    fig = px.bar(

        df,

        x="coordinator",

        y="Completed",

        text="Completed",

        color="Completed"

    )

    fig.update_layout(
        height=400
    )

    return fig


def trend_chart(df):

    fig = px.line(

        df,

        x="date",

        y="Count",

        color="status",

        markers=True

    )

    fig.update_layout(
        height=450
    )

    return fig
