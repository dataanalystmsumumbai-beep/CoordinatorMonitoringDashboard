import io
import pandas as pd


def dataframe_to_excel(df):

    output = io.BytesIO()

    with pd.ExcelWriter(output, engine="openpyxl") as writer:

        df.to_excel(
            writer,
            index=False,
            sheet_name="Report"
        )

    return output.getvalue()
