import io
import pandas as pd


def export_excel(df):

    output = io.BytesIO()

    with pd.ExcelWriter(
        output,
        engine="openpyxl"
    ) as writer:

        df.to_excel(
            writer,
            index=False,
            sheet_name="Report"
        )

        ws = writer.sheets["Report"]

        for col in ws.columns:

            length = max(
                len(str(cell.value))
                if cell.value
                else 0
                for cell in col
            )

            ws.column_dimensions[
                col[0].column_letter
            ].width = length + 4

    return output.getvalue()
