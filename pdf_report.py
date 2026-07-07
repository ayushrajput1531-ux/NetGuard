from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from datetime import datetime


def save_pdf_report(report_text, file_path):

    doc = SimpleDocTemplate(file_path)

    styles = getSampleStyleSheet()

    story = []

    # Title
    story.append(
        Paragraph(
            "<b><font size=22 color='blue'>NetGuard Report</font></b>",
            styles["Title"]
        )
    )

    story.append(Spacer(1, 20))

    # Date & Time
    current_time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    story.append(
        Paragraph(
            f"<b>Generated :</b> {current_time}",
            styles["Normal"]
        )
    )

    story.append(Spacer(1, 20))

    # Report
    for line in report_text.split("\n"):

        if line.strip() == "":
            continue

        story.append(
            Paragraph(
                line.replace(" ", "&nbsp;"),
                styles["Normal"]
            )
        )

    doc.build(story)