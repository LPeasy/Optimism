from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.pagesizes import landscape, letter
from reportlab.pdfgen import canvas


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "assets" / "ai-workflow-fit-worksheet-v1.pdf"

INK = colors.HexColor("#111716")
MUTED = colors.HexColor("#5f6a67")
LINE = colors.HexColor("#cbd8d3")
SOFT = colors.HexColor("#f4f8f6")
SOFT_2 = colors.HexColor("#edf5f1")
ACCENT = colors.HexColor("#127966")
ACCENT_DARK = colors.HexColor("#0c5f51")
FIELD_FILL = colors.HexColor("#ffffff")


def text(c, value, x, y, size=8.5, font="Helvetica", fill=INK):
    c.setFont(font, size)
    c.setFillColor(fill)
    c.drawString(x, y, value)


def wrapped_text(c, value, x, y, width, size=8.2, leading=10, font="Helvetica", fill=MUTED):
    words = value.split()
    lines = []
    current = ""
    for word in words:
        candidate = f"{current} {word}".strip()
        if c.stringWidth(candidate, font, size) <= width:
            current = candidate
        else:
            if current:
                lines.append(current)
            current = word
    if current:
        lines.append(current)
    c.setFont(font, size)
    c.setFillColor(fill)
    for offset, line in enumerate(lines):
        c.drawString(x, y - offset * leading, line)
    return len(lines) * leading


def section(c, title, x, y, width, height, fill=SOFT):
    c.setStrokeColor(LINE)
    c.setFillColor(fill)
    c.roundRect(x, y, width, height, 7, stroke=1, fill=1)
    text(c, title, x + 10, y + height - 17, 10, "Helvetica-Bold", ACCENT_DARK)


def field(c, name, x, y, width, height=18, multiline=False, maxlen=250):
    c.acroForm.textfield(
        name=name,
        tooltip=name.replace("_", " "),
        x=x,
        y=y,
        width=width,
        height=height,
        borderColor=LINE,
        fillColor=FIELD_FILL,
        textColor=INK,
        borderWidth=0.8,
        fontName="Helvetica",
        fontSize=8,
        fieldFlags="multiline" if multiline else "",
        maxlen=maxlen,
    )


def checkbox(c, name, x, y, label):
    c.acroForm.checkbox(
        name=name,
        tooltip=label,
        x=x,
        y=y,
        size=9,
        borderColor=ACCENT_DARK,
        fillColor=FIELD_FILL,
        textColor=ACCENT_DARK,
        borderWidth=0.8,
        fieldFlags="",
    )
    text(c, label, x + 14, y + 1.5, 7.2, "Helvetica", INK)


def labeled_field(c, label, name, x, y, width, height=18, multiline=False):
    text(c, label, x, y + height + 4, 7.4, "Helvetica-Bold", ACCENT_DARK)
    field(c, name, x, y, width, height, multiline=multiline)


def build_pdf():
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    page_width, page_height = landscape(letter)
    c = canvas.Canvas(str(OUTPUT), pagesize=(page_width, page_height))
    c.setTitle("AI Workflow Intake Worksheet v1")
    c.setAuthor("Optimism")
    c.setSubject("Optional prep worksheet for human-first AI-assisted workflow systems")

    margin = 32
    content_width = page_width - margin * 2

    c.setFillColor(colors.white)
    c.rect(0, 0, page_width, page_height, stroke=0, fill=1)

    text(c, "Optimism", margin, page_height - 35, 10.5, "Helvetica-Bold", ACCENT_DARK)
    text(c, "AI Workflow Intake Worksheet v1", margin, page_height - 62, 23, "Helvetica-Bold", INK)
    wrapped_text(
        c,
        "Use this optional worksheet to name the messy workflow, list current tools, and clarify where custom software or AI assistance may help.",
        margin,
        page_height - 81,
        625,
        8.8,
        10.5,
    )
    text(c, "Bring it to a 20-minute Workflow Fit Call.", page_width - margin - 210, page_height - 43, 8.5, "Helvetica-Bold", ACCENT_DARK)
    c.setStrokeColor(LINE)
    c.line(margin, page_height - 105, page_width - margin, page_height - 105)

    col_gap = 14
    col_w = (content_width - col_gap) / 2
    left_x = margin
    right_x = margin + col_w + col_gap
    top_y = page_height - 122

    section(c, "1. Business snapshot", left_x, top_y - 132, col_w, 132)
    labeled_field(c, "Company or organization", "company", left_x + 10, top_y - 58, 165)
    labeled_field(c, "Your role", "role", left_x + 185, top_y - 58, col_w - 195)
    labeled_field(c, "What does the business or team do?", "business_summary", left_x + 10, top_y - 103, col_w - 20, 30, multiline=True)
    labeled_field(c, "Main customer, stakeholder, or internal user", "main_user", left_x + 10, top_y - 128, col_w - 20, 14)

    section(c, "2. Tools and AI reality", right_x, top_y - 132, col_w, 132)
    text(c, "Which stage is closest?", right_x + 10, top_y - 35, 7.4, "Helvetica-Bold", ACCENT_DARK)
    options = [
        ("ai_stage_none", "Not using AI yet"),
        ("ai_stage_experimenting", "Experimenting"),
        ("ai_stage_regular", "Regular use"),
        ("ai_stage_blocked", "Blocked by risk"),
        ("ai_stage_unmanaged", "Hard to manage"),
    ]
    for i, (name, label) in enumerate(options):
        checkbox(c, name, right_x + 10 + (i % 3) * 113, top_y - 53 - (i // 3) * 17, label)
    labeled_field(c, "Tools already used", "tools_used", right_x + 10, top_y - 94, col_w - 20, 14)
    labeled_field(c, "Where is AI creating questions, delay, rework, or risk?", "current_ai_challenge", right_x + 10, top_y - 124, col_w - 20, 18, multiline=True)

    mid_y = top_y - 150
    section(c, "3. Workflow opportunity", left_x, mid_y - 148, col_w, 148)
    labeled_field(c, "One recurring workflow worth improving first", "workflow_candidate", left_x + 10, mid_y - 50, col_w - 20, 20)
    labeled_field(c, "Where does it waste time, create errors, slow sales, weaken reporting, or increase risk?", "current_pain", left_x + 10, mid_y - 93, col_w - 20, 30, multiline=True)
    labeled_field(c, "What would better look like in business terms?", "desired_outcome", left_x + 10, mid_y - 136, col_w - 20, 30, multiline=True)

    section(c, "4. System design signals", right_x, mid_y - 148, col_w, 148)
    wrapped_text(c, "Check the areas where the team needs clarity before building or adding AI assistance.", right_x + 10, mid_y - 36, col_w - 20, 7.6, 9)
    signals = [
        ("need_workflow", "Workflow: trigger, owner, output, review point"),
        ("need_tools", "Tools: current apps, spreadsheets, inboxes, docs"),
        ("need_handoffs", "Handoffs: who receives what and when"),
        ("need_data", "Data: approved inputs, sensitive data, access"),
        ("need_ai_fit", "AI fit: drafting, summaries, checks, extraction"),
        ("need_support", "Support: training, docs, stop rules, changes"),
    ]
    for i, (name, label) in enumerate(signals):
        checkbox(c, name, right_x + 10, mid_y - 58 - i * 15, label)

    bottom_y = 58
    section(c, "5. Next step fit", margin, bottom_y, content_width, 102, SOFT_2)
    text(c, "Desired result", margin + 10, bottom_y + 72, 7.4, "Helvetica-Bold", ACCENT_DARK)
    result_options = [
        ("result_time", "Save time"),
        ("result_quality", "Improve quality"),
        ("result_revenue", "Support revenue"),
        ("result_risk", "Reduce risk"),
        ("result_reporting", "Speed reporting"),
        ("result_clarity", "Clarify fit"),
    ]
    for i, (name, label) in enumerate(result_options):
        checkbox(c, name, margin + 10 + i * 90, bottom_y + 52, label)

    text(c, "Timeline", margin + 565, bottom_y + 72, 7.4, "Helvetica-Bold", ACCENT_DARK)
    timeline_options = [
        ("timeline_now", "Now"),
        ("timeline_30", "30 days"),
        ("timeline_90", "90 days"),
        ("timeline_later", "Later"),
    ]
    for i, (name, label) in enumerate(timeline_options):
        checkbox(c, name, margin + 565 + i * 45, bottom_y + 52, label)

    text(c, "Budget readiness", margin + 10, bottom_y + 34, 7.4, "Helvetica-Bold", ACCENT_DARK)
    budget_options = [
        ("budget_5k_build", "Ready for a $5k+ build"),
        ("budget_blueprint", "Need a smaller blueprint first"),
        ("budget_exploring", "Exploring fit"),
    ]
    for i, (name, label) in enumerate(budget_options):
        checkbox(c, name, margin + 10 + i * 185, bottom_y + 15, label)

    labeled_field(c, "Fit-call value", "fit_call_value", margin + 565, bottom_y + 10, content_width - 575, 20)

    footer_y = 33
    c.setStrokeColor(LINE)
    c.line(margin, footer_y + 14, page_width - margin, footer_y + 14)
    text(c, "Worksheet for call prep only. The web form is the submitted intake record.", margin, footer_y, 8, "Helvetica-Bold", ACCENT_DARK)
    text(c, "Source controls: Workflow, Tools, Handoffs, Data, AI Fit, Support.", margin + 335, footer_y, 8, "Helvetica", MUTED)
    c.drawRightString(page_width - margin, footer_y, "optimism - ai workflow intake worksheet v1")

    c.showPage()
    c.save()


if __name__ == "__main__":
    build_pdf()
    print(OUTPUT)
