from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import PageBreak, Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "assets" / "optimism-ai-workflow-setup-brief-v1.pdf"

INK = colors.HexColor("#111716")
MUTED = colors.HexColor("#5f6a67")
LINE = colors.HexColor("#cbd8d3")
SOFT = colors.HexColor("#f4f8f6")
SOFT_2 = colors.HexColor("#edf5f1")
ACCENT = colors.HexColor("#127966")
ACCENT_DARK = colors.HexColor("#0c5f51")
GRAPHITE = colors.HexColor("#26302d")
WHITE = colors.white


def build_styles():
    base = getSampleStyleSheet()
    return {
        "eyebrow": ParagraphStyle(
            "eyebrow",
            parent=base["BodyText"],
            fontName="Helvetica-Bold",
            fontSize=8,
            leading=10,
            textColor=ACCENT_DARK,
            spaceAfter=7,
        ),
        "title": ParagraphStyle(
            "title",
            parent=base["Title"],
            fontName="Helvetica-Bold",
            fontSize=29,
            leading=33,
            textColor=INK,
            spaceAfter=10,
        ),
        "subtitle": ParagraphStyle(
            "subtitle",
            parent=base["BodyText"],
            fontName="Helvetica",
            fontSize=12,
            leading=17,
            textColor=MUTED,
            spaceAfter=14,
        ),
        "section": ParagraphStyle(
            "section",
            parent=base["Heading2"],
            fontName="Helvetica-Bold",
            fontSize=16,
            leading=20,
            textColor=INK,
            spaceBefore=6,
            spaceAfter=8,
        ),
        "body": ParagraphStyle(
            "body",
            parent=base["BodyText"],
            fontName="Helvetica",
            fontSize=9.4,
            leading=13,
            textColor=GRAPHITE,
        ),
        "body_white": ParagraphStyle(
            "body_white",
            parent=base["BodyText"],
            fontName="Helvetica",
            fontSize=10,
            leading=14,
            textColor=WHITE,
        ),
        "card_title": ParagraphStyle(
            "card_title",
            parent=base["Heading3"],
            fontName="Helvetica-Bold",
            fontSize=10.4,
            leading=12,
            textColor=ACCENT_DARK,
            spaceAfter=4,
        ),
        "small": ParagraphStyle(
            "small",
            parent=base["BodyText"],
            fontName="Helvetica",
            fontSize=8,
            leading=10.5,
            textColor=MUTED,
        ),
        "small_center": ParagraphStyle(
            "small_center",
            parent=base["BodyText"],
            alignment=TA_CENTER,
            fontName="Helvetica-Bold",
            fontSize=8,
            leading=10,
            textColor=ACCENT_DARK,
        ),
    }


STYLES = build_styles()


def p(value, style="body"):
    return Paragraph(value, STYLES[style])


def card(title, body, width):
    table = Table(
        [[p(title, "card_title")], [p(body, "body")]],
        colWidths=[width],
        style=[
            ("BACKGROUND", (0, 0), (-1, -1), SOFT),
            ("BOX", (0, 0), (-1, -1), 0.7, LINE),
            ("LEFTPADDING", (0, 0), (-1, -1), 9),
            ("RIGHTPADDING", (0, 0), (-1, -1), 9),
            ("TOPPADDING", (0, 0), (-1, -1), 8),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
        ],
    )
    return table


def header_card(title, body):
    return Table(
        [[p(title, "body_white")], [p(body, "body_white")]],
        colWidths=[7.5 * inch],
        style=[
            ("BACKGROUND", (0, 0), (-1, -1), ACCENT_DARK),
            ("BOX", (0, 0), (-1, -1), 0.7, ACCENT_DARK),
            ("LEFTPADDING", (0, 0), (-1, -1), 14),
            ("RIGHTPADDING", (0, 0), (-1, -1), 14),
            ("TOPPADDING", (0, 0), (-1, -1), 11),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 11),
        ],
    )


def footer(canvas, doc):
    canvas.saveState()
    canvas.setStrokeColor(LINE)
    canvas.line(0.5 * inch, 0.48 * inch, 8.0 * inch, 0.48 * inch)
    canvas.setFont("Helvetica", 7.5)
    canvas.setFillColor(MUTED)
    canvas.drawString(0.5 * inch, 0.32 * inch, "Optimism - Workflow Software Brief v1")
    canvas.drawRightString(8.0 * inch, 0.32 * inch, f"Page {doc.page}")
    canvas.restoreState()


def build_pdf():
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    doc = SimpleDocTemplate(
        str(OUTPUT),
        pagesize=letter,
        leftMargin=0.5 * inch,
        rightMargin=0.5 * inch,
        topMargin=0.55 * inch,
        bottomMargin=0.65 * inch,
        title="Optimism Workflow Software Brief v1",
        author="Optimism",
        subject="Sales leave-behind for human-first AI-assisted workflow systems",
    )

    full = 7.5 * inch
    half = (full - 0.18 * inch) / 2
    third = (full - 0.36 * inch) / 3

    story = [
        p("OPTIMISM", "eyebrow"),
        p("Human-First AI-Assisted Systems Design", "title"),
        p(
            "A practical path for turning one messy recurring workflow into custom workflow software an owner can use, explain, and improve.",
            "subtitle",
        ),
        header_card(
            "The point is not broad AI transformation.",
            "The point is one useful internal system: clearer intake, cleaner tracking, better handoffs, faster documents or emails, useful reporting, and AI assistance only where it improves the work.",
        ),
        Spacer(1, 0.18 * inch),
        p("Where Optimism fits", "section"),
        Table(
            [
                [
                    card("Good first workflow", "Repeated work with visible delay, missed follow-up, manual copying, unclear status, reporting burden, or review friction.", third),
                    card("Weak first workflow", "No named owner, no repeatable process, unclear data boundary, autonomous AI action, or no measurable business pain.", third),
                    card("Buyer pattern", "An owner-led business with one practical workflow worth fixing before broader automation.", third),
                ]
            ],
            colWidths=[third, third, third],
            style=[("VALIGN", (0, 0), (-1, -1), "TOP"), ("LEFTPADDING", (0, 0), (-1, -1), 0), ("RIGHTPADDING", (0, 0), (-1, -1), 0)],
        ),
        Spacer(1, 0.16 * inch),
        p("What the system needs to know", "section"),
        Table(
            [
                [
                    card("Workflow", "One trigger, owner, output, handoff, and review point.", half),
                    card("Tools", "The current inboxes, calendars, spreadsheets, documents, forms, CRM, and job software already in use.", half),
                ],
                [
                    card("Data", "Approved inputs, sensitive information, retention, and access limits.", half),
                    card("Handoffs", "Who receives what, when, and with what context.", half),
                ],
                [
                    card("AI fit", "Where drafting, summarizing, classifying, extracting, or checking can help without replacing judgment.", half),
                    card("Support", "Training, documentation, stop rules, change control, and iteration path.", half),
                ],
            ],
            colWidths=[half, half],
            rowHeights=None,
            style=[
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 0),
                ("RIGHTPADDING", (0, 0), (-1, -1), 0),
                ("TOPPADDING", (0, 0), (-1, -1), 3),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
            ],
        ),
        PageBreak(),
        Spacer(1, 0.16 * inch),
        p("How the engagement moves", "section"),
        Table(
            [
                [p("1. AI Workflow Intake", "card_title"), p("Capture the business, current tools, messy workflow, AI questions, timeline, and budget readiness.", "body")],
                [p("2. Workflow Fit Call", "card_title"), p("Confirm whether the workflow is specific enough and valuable enough for a fixed-scope build.", "body")],
                [p("3. Workflow Blueprint", "card_title"), p("Optional smaller package, starting at $1,500, to map the workflow, define the system, and price the build.", "body")],
                [p("4. Workflow Build Sprint", "card_title"), p("Main package, starting at $5,000, to build the system, wire handoffs, test the workflow, and hand it off.", "body")],
                [p("5. Support and Iteration", "card_title"), p("Tune the system after real use and identify adjacent workflows when useful.", "body")],
            ],
            colWidths=[1.95 * inch, 5.55 * inch],
            style=[
                ("BACKGROUND", (0, 0), (-1, -1), WHITE),
                ("BOX", (0, 0), (-1, -1), 0.7, LINE),
                ("INNERGRID", (0, 0), (-1, -1), 0.4, LINE),
                ("LEFTPADDING", (0, 0), (-1, -1), 8),
                ("RIGHTPADDING", (0, 0), (-1, -1), 8),
                ("TOPPADDING", (0, 0), (-1, -1), 7),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ],
        ),
        Spacer(1, 0.2 * inch),
        p("PROOF AND NEXT STEP", "eyebrow"),
        p("Controls make the build easier to trust.", "title"),
        p(
            "Optimism's governance kit supports the software build with a visible operating spine: scope, data boundaries, tool permissions, human review, change control, and acceptance checks.",
            "subtitle",
        ),
        p("What the controls prove", "section"),
        Table(
            [
                [
                    card("GOV-001", "Baseline package is complete, internally linked, and manager-readable.", third),
                    card("GOV-002/003", "Data handling and tool permissions are explicitly bounded before implementation.", third),
                    card("GOV-004/005", "Source evidence and manager handoff are reviewable before pilot use.", third),
                ]
            ],
            colWidths=[third, third, third],
            style=[("VALIGN", (0, 0), (-1, -1), "TOP"), ("LEFTPADDING", (0, 0), (-1, -1), 0), ("RIGHTPADDING", (0, 0), (-1, -1), 0)],
        ),
        PageBreak(),
        Spacer(1, 0.16 * inch),
        p("Modeled ExampleCo demo", "section"),
        Table(
            [
                [p("Before", "card_title"), p("Spreadsheet-heavy commission packet review with unclear scope, no formal data boundary, weak approval trace, and inconsistent evidence.", "body")],
                [p("After setup", "card_title"), p("A structured workflow package defines owners, approved inputs, approval gates, risk controls, evaluation checks, source records, and stop rules.", "body")],
                [p("Modeled pilot signal", "card_title"), p("Manager prep time down 66%, rework down 12 points, approval trace complete, and unresolved high risks closed before pilot. Synthetic demo metrics, not client production claims.", "body")],
            ],
            colWidths=[1.45 * inch, 6.05 * inch],
            style=[
                ("BACKGROUND", (0, 0), (-1, -1), SOFT_2),
                ("BOX", (0, 0), (-1, -1), 0.7, LINE),
                ("INNERGRID", (0, 0), (-1, -1), 0.4, LINE),
                ("LEFTPADDING", (0, 0), (-1, -1), 8),
                ("RIGHTPADDING", (0, 0), (-1, -1), 8),
                ("TOPPADDING", (0, 0), (-1, -1), 7),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ],
        ),
        Spacer(1, 0.16 * inch),
        p("The six proof metrics", "section"),
        Table(
            [
                [p("Time saved", "small_center"), p("Faster follow-up", "small_center"), p("Fewer handoff misses", "small_center")],
                [p("Error reduction", "small_center"), p("Better visibility", "small_center"), p("Repeat usage", "small_center")],
            ],
            colWidths=[third, third, third],
            style=[
                ("BACKGROUND", (0, 0), (-1, -1), SOFT),
                ("BOX", (0, 0), (-1, -1), 0.7, LINE),
                ("INNERGRID", (0, 0), (-1, -1), 0.4, LINE),
                ("LEFTPADDING", (0, 0), (-1, -1), 8),
                ("RIGHTPADDING", (0, 0), (-1, -1), 8),
                ("TOPPADDING", (0, 0), (-1, -1), 9),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 9),
            ],
        ),
        Spacer(1, 0.18 * inch),
        header_card(
            "Next step: start the AI Workflow Intake.",
            "The intake should answer what the business does, what tools it already uses, where work gets messy, whether AI fits, and whether the next step is a Workflow Build Sprint, smaller Blueprint, or no project yet.",
        ),
        Spacer(1, 0.14 * inch),
        p(
            "Source basis: Optimism sales value deck, GOV-001 demo deck, ExampleCo synthetic case study, AI Agent Working Group Governance Kit, and proof-metrics playbook.",
            "small",
        ),
    ]

    doc.build(story, onFirstPage=footer, onLaterPages=footer)


if __name__ == "__main__":
    build_pdf()
    print(OUTPUT)
