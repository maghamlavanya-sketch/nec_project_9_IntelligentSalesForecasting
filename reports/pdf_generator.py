from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import (
    getSampleStyleSheet
)

def generate_pdf(df):

    file_path = "reports/sales_report.pdf"

    doc = SimpleDocTemplate(
        file_path
    )

    styles = getSampleStyleSheet()

    content = []

    content.append(
        Paragraph(
            "Sales Report",
            styles["Title"]
        )
    )

    content.append(
        Spacer(1,20)
    )

    content.append(
        Paragraph(
            f"Total Revenue : ₹{df['Revenue'].sum():,.0f}",
            styles["Normal"]
        )
    )

    content.append(
        Paragraph(
            f"Total Orders : {len(df)}",
            styles["Normal"]
        )
    )

    doc.build(content)

    return file_path