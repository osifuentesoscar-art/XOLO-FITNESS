"""
XOLOKAN 30-Day Dancer Foundation — sellable PDF program generator.

Exercise selection, sets, and reps are pulled LIVE from generateProgram()
(via generateSampleCli.ts) at build time -- never hardcoded here -- so this
PDF and the actual program generator can't drift apart as
packages/xolokan-agent/src/archetypes.ts evolves. Only coaching cues, RIR
targets, and rest times are authored in this script, since the generator
doesn't produce those yet.

Usage:
  python3 scripts/dancer_30_day_pdf.py --equipment bodyweight-only [output_path]
  python3 scripts/dancer_30_day_pdf.py --equipment full-gym [output_path]
"""

import argparse
import json
import subprocess
import sys
from pathlib import Path

from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    PageBreak, HRFlowable,
)
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfgen import canvas as canvas_mod

REPO_ROOT = Path(__file__).resolve().parent.parent

# =========================================================
# CLI
# =========================================================
parser = argparse.ArgumentParser()
parser.add_argument("output", nargs="?", default=None)
parser.add_argument("--equipment", choices=["bodyweight-only", "full-gym"], default="bodyweight-only")
args = parser.parse_args()

EQUIPMENT = args.equipment
EDITION_LABEL = "GYM EDITION" if EQUIPMENT == "full-gym" else "BODYWEIGHT EDITION"
OUT_PATH = args.output or (
    "XOLOKAN_30Day_Dancer_Foundation_Gym.pdf" if EQUIPMENT == "full-gym"
    else "XOLOKAN_30Day_Dancer_Foundation_Bodyweight.pdf"
)

# =========================================================
# Pull live program data from the generator (source of truth)
# =========================================================
def get_program():
    result = subprocess.run(
        [
            "npx", "tsx", "packages/xolokan-agent/src/generateSampleCli.ts",
            "--name", "Dancer",
            "--discipline", "dancer",
            "--level", "intermediate",
            "--days", "4",
            "--equipment", EQUIPMENT,
        ],
        cwd=REPO_ROOT, capture_output=True, text=True,
    )
    if result.returncode != 0:
        print(result.stderr, file=sys.stderr)
        raise SystemExit("generateSampleCli.ts failed")
    return json.loads(result.stdout)

program = get_program()
week1_days = program["weeks"][0]["days"]  # weeks 1-4 are identical content in Phase 1

# =========================================================
# Coaching cues -- authored here, keyed by exercise name.
# Covers both bodyweight and loaded exercise names so either
# equipment edition renders correctly from the same lookup.
# =========================================================
CUES = {
    "Pull-Ups":            {"rir": "2", "rest": "90s", "cue": "Full hang to chin over bar, control the descent."},
    "Banded Pull-Ups":     {"rir": "2", "rest": "90s", "cue": "Full hang to chin over bar, control the descent."},
    "Seated Overhead Press": {"rir": "2", "rest": "90s", "cue": "Ribs down, press straight overhead, no lean-back."},
    "Pike Push-Ups":       {"rir": "2", "rest": "75s", "cue": "Hips high, crown of the head toward the floor."},
    "Bent-Over Row":       {"rir": "2", "rest": "75s", "cue": "Flat back, pull to the lower ribs, squeeze at the top."},
    "Inverted Row":        {"rir": "2", "rest": "75s", "cue": "Squeeze shoulder blades together at the top."},
    "Depth Jumps":         {"rir": "-", "rest": "90s", "cue": "Step off, land soft, rebound immediately — quality over height."},
    "Sprint Intervals":    {"rir": "-", "rest": "60s", "cue": "Build to top speed over the first 10m, hold form."},
    "Front Squat":         {"rir": "2", "rest": "90s", "cue": "Elbows up, bar in the fingers, chest tall out of the hole."},
    "Bulgarian Split Squat": {"rir": "2", "rest": "90s", "cue": "Rear foot elevated, front shin stays vertical."},
    "Weighted Pull-Ups":   {"rir": "2", "rest": "90s", "cue": "Same strict standard as bodyweight, just heavier."},
    "Single-Leg RDL":      {"rir": "2", "rest": "60s", "cue": "Hips square, soft knee, reach through the heel."},
    "Hanging Leg Raise":   {"rir": "2", "rest": "60s", "cue": "Curl the pelvis, no swinging."},
    "Copenhagen Plank":    {"rir": "-", "rest": "45s", "cue": "Top leg on the bench, hips stay level — adductor strength for hip stability."},
    "Pogo Jumps":          {"rir": "-", "rest": "45s", "cue": "Stiff ankles, minimal knee bend, quick ground contact."},
    "Single-Leg Bounds":   {"rir": "-", "rest": "60s", "cue": "Drive the opposite knee, stick every landing."},
    "Ankle Isometric Hold (single-leg calf raise)": {"rir": "-", "rest": "30s", "cue": "Hold at the top — ankle resilience for jump-heavy work."},
    "Lateral Skater Jumps": {"rir": "-", "rest": "60s", "cue": "Land soft on the outside foot, control the stick."},
    "Jump Rope":           {"rir": "-", "rest": "-", "cue": "Small hops, wrists do the work, relax the shoulders."},
    "Sled Push":           {"rir": "-", "rest": "60s", "cue": "Low shin angle, drive through the whole foot, short powerful steps."},
    "Bear Crawl Sprint":   {"rir": "-", "rest": "60s", "cue": "Hips low, opposite hand/foot, don't let the hips rise."},
    "Push-Ups":            {"rir": "2", "rest": "60s", "cue": "Straight line head to heel, full lockout."},
    "Kettlebell Swings":   {"rir": "-", "rest": "60s", "cue": "Hip hinge, not a squat — the bell floats from hip drive."},
    "Broad Jumps":         {"rir": "-", "rest": "60s", "cue": "Reset fully between reps — this is a power drill, not conditioning."},
    "Battle Ropes":        {"rir": "-", "rest": "30s", "cue": "Stay low, alternate waves stay consistent, breathe."},
    "Mountain Climbers 30s": {"rir": "-", "rest": "30s", "cue": "Hips stay low, drive the knees to the chest."},
}

DAY_INTRO = {
    1: None,
    2: None,
    3: "New to plyometric work? Take the lower end of each range, or drop to 3 sets across the board — see the note below the table.",
    4: None,
}
DAY_OUTRO = {
    3: (
        "This is the highest-impact day in the program. As written it's roughly "
        "intermediate-level jump volume. If today's the first time you've trained plyometrics "
        "in a while, cut every set count by one and build up over the four weeks — landing "
        "mechanics earn their place gradually, not all at once."
    ),
}

# =========================================================
# brand tokens
# =========================================================
INK = colors.HexColor("#14150C")
ACCENT = colors.HexColor("#94A812")
ACCENT_FILL = colors.HexColor("#F4F5EA")
MUTED = colors.HexColor("#6B6C58")
RULE = colors.HexColor("#D9D7C4")
WHITE = colors.white

PW, PH = letter
ML = MR = 0.75 * inch
MT = 0.85 * inch
MB = 0.75 * inch

def style(name, **kw):
    base = dict(fontName="Helvetica", fontSize=9.5, leading=13, textColor=INK)
    base.update(kw)
    return ParagraphStyle(name, **base)

S_BRAND = style("brand", fontName="Helvetica-Bold", fontSize=10, textColor=MUTED, alignment=TA_CENTER)
S_TITLE = style("title", fontName="Helvetica-Bold", fontSize=30, leading=34, textColor=INK, alignment=TA_CENTER)
S_SUBTITLE = style("subtitle", fontName="Helvetica-Bold", fontSize=13, textColor=ACCENT, alignment=TA_CENTER)
S_DEK = style("dek", fontName="Helvetica", fontSize=10.5, leading=15, textColor=MUTED, alignment=TA_CENTER)
S_H1 = style("h1", fontName="Helvetica-Bold", fontSize=16, textColor=INK, spaceAfter=6)
S_H2 = style("h2", fontName="Helvetica-Bold", fontSize=11, textColor=ACCENT, spaceBefore=10, spaceAfter=4)
S_BODY = style("body", fontSize=9.5, leading=13.5, spaceAfter=6)
S_MUTED = style("mutedtext", fontSize=8.5, leading=12, textColor=MUTED)
S_DAYTAG = style("daytag", fontName="Helvetica-Bold", fontSize=9, textColor=WHITE)
S_CELL = style("cell", fontSize=8.3, leading=10.5)
S_CELL_BOLD = style("cellbold", fontSize=8.3, leading=10.5, fontName="Helvetica-Bold")
S_CUE = style("cue", fontSize=7.8, leading=10, textColor=MUTED)

story = []

def brand_header():
    story.append(Paragraph("X O L O &nbsp; F I T N E S S", S_BRAND))
    story.append(Spacer(1, 4))

def hr(color=RULE, thickness=0.75):
    story.append(HRFlowable(width="100%", thickness=thickness, color=color, spaceBefore=4, spaceAfter=10))

def day_table(exercises):
    header = ["EXERCISE", "SETS", "REPS", "RIR", "REST", "COACHING CUE"]
    data = [header]
    for ex in exercises:
        cue_info = CUES.get(ex["name"])
        if cue_info is None:
            raise SystemExit(f"Missing cue for exercise: {ex['name']!r} -- add it to CUES before shipping.")
        corrective = bool(ex.get("correctivePriority"))
        name_cell = Paragraph(f"<b>{ex['name']}</b>" + (" *" if corrective else ""), S_CELL)
        cue_cell = Paragraph(cue_info["cue"], S_CUE)
        data.append([name_cell, str(ex["sets"]), ex["reps"], cue_info["rir"], cue_info["rest"], cue_cell])
    t = Table(data, colWidths=[1.55*inch, 0.4*inch, 0.6*inch, 0.42*inch, 0.5*inch, 2.53*inch])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), INK),
        ("TEXTCOLOR", (0, 0), (-1, 0), WHITE),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTSIZE", (0, 0), (-1, 0), 7.5),
        ("ALIGN", (1, 0), (4, -1), "CENTER"),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [WHITE, ACCENT_FILL]),
        ("GRID", (0, 0), (-1, -1), 0.5, RULE),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
        ("LEFTPADDING", (0, 0), (-1, -1), 6),
    ]))
    return t

def day_banner(tag, title):
    data = [[Paragraph(tag, S_DAYTAG), Paragraph(f"<b>{title}</b>", style("banner", fontSize=12, textColor=WHITE))]]
    t = Table(data, colWidths=[1.1*inch, 5.4*inch])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), INK),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("TOPPADDING", (0, 0), (-1, -1), 8),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
        ("LEFTPADDING", (0, 0), (-1, -1), 10),
    ]))
    story.append(t)
    story.append(Spacer(1, 8))

def mobility_block():
    story.append(Paragraph("MOBILITY &amp; RECOVERY (attach after today's session)", S_H2))
    for i in [
        "Hip Flexor Stretch — 2 minutes each side",
        "Hamstring Stretch — 2 minutes",
        "Thoracic Spine Rotations — 2 minutes",
        "Deep Squat Hold — 2 minutes",
    ]:
        story.append(Paragraph(f"- {i}", S_BODY))

def render_day_page(day):
    brand_header()
    day_banner(f"DAY {day['dayNumber']}", day["focus"])
    intro = DAY_INTRO.get(day["dayNumber"])
    if intro:
        story.append(Paragraph(intro, S_MUTED))
        story.append(Spacer(1, 6))
    story.append(day_table(day["exercises"]))
    outro = DAY_OUTRO.get(day["dayNumber"])
    if outro:
        story.append(Spacer(1, 8))
        story.append(Paragraph(outro, S_MUTED))
    if day.get("mobilitySession"):
        story.append(Spacer(1, 10))
        mobility_block()
    story.append(PageBreak())

# =========================================================
# COVER
# =========================================================
story.append(Spacer(1, 1.5*inch))
brand_header()
story.append(Spacer(1, 0.4*inch))
story.append(Paragraph("XOLOKAN", S_TITLE))
story.append(Paragraph("DANCER PROTOCOL", style("t2", fontName="Helvetica-Bold", fontSize=18, textColor=INK, alignment=TA_CENTER)))
story.append(Spacer(1, 10))
story.append(Paragraph("30-DAY FOUNDATION", S_SUBTITLE))
story.append(Paragraph(EDITION_LABEL, style("edition", fontName="Helvetica-Bold", fontSize=10, textColor=MUTED, alignment=TA_CENTER, spaceBefore=4)))
story.append(Spacer(1, 16))
story.append(Paragraph(
    "Soviet-block periodization, calisthenics-built relative strength, and "
    "dance-specific injury prevention.",
    S_DEK
))
story.append(Spacer(1, 0.9*inch))
if EQUIPMENT == "full-gym":
    story.append(Paragraph("FULL STRENGTH TRAINING &nbsp;&#8212;&nbsp; 4 TRAINING DAYS / WEEK &nbsp;&#8212;&nbsp; BUILT FOR DANCERS", S_MUTED))
else:
    story.append(Paragraph("BODYWEIGHT-FOCUSED &nbsp;&#8212;&nbsp; 4 TRAINING DAYS / WEEK &nbsp;&#8212;&nbsp; BUILT FOR DANCERS", S_MUTED))
story.append(PageBreak())

# =========================================================
# HOW THIS WORKS
# =========================================================
brand_header()
story.append(Paragraph("How This Works", S_H1))
hr()
story.append(Paragraph(
    "This is Phase 1 of the XOLOKAN Method — Base Strength &amp; Control. Four weeks "
    "of technique-first strength, calisthenics-built relative strength, and dance-specific "
    "injury prevention, at 70–75% intensity. Form over load, every session.",
    S_BODY
))

story.append(Paragraph("Before Day 1 — record your baseline", S_H2))
story.append(Paragraph(
    "Log these four numbers before your first session. You'll retest them on Day 29 "
    "to see exactly what changed: max pull-ups (or assisted pull-ups to failure), max plank "
    "hold, single-leg balance (eyes closed, each side), and standing broad jump distance.",
    S_BODY
))

story.append(Paragraph("Effort: RIR, not percentages", S_H2))
story.append(Paragraph(
    "RIR means Reps In Reserve — how many more reps you could do before failure. Most "
    "working sets in this program are RIR 2: stop with two clean reps left in the tank. "
    "<b>Progression rule:</b> if you hit the top of a rep range at RIR 2+ with clean form, "
    "add a rep or a small load/difficulty bump next session. If form breaks down or you're at "
    "RIR 0–1 before the last set, hold where you are.",
    S_BODY
))

story.append(Paragraph("Warm up with RAMP, every session", S_H2))
story.append(Paragraph(
    "<b>Raise</b> — 3–5 min light cardio (jog in place, jumping jacks) to raise core "
    "and muscle temperature. <b>Activate &amp; Mobilise</b> — active-range movement through "
    "today's actual patterns (leg swings, hip circles, arm circles), not static stretching. "
    "<b>Potentiate</b> — a few submaximal reps of today's first exercise to prime the nervous "
    "system. Static stretching, if you use it, belongs after training — not before.",
    S_BODY
))

story.append(Paragraph("What you'll need", S_H2))
if EQUIPMENT == "full-gym":
    story.append(Paragraph(
        "Full gym access: a squat rack or heavy dumbbells, a pull-up bar, a barbell or "
        "dumbbells for pressing and rowing, a kettlebell, and a sled (or a heavy dumbbell/"
        "plate to push instead).",
        S_BODY
    ))
else:
    story.append(Paragraph(
        "A pull-up bar (doorway bars work), a resistance band, and a bench or sturdy elevated "
        "surface. Everything else is bodyweight. Want to lift instead? Ask for the Gym Edition "
        "of this program — same method, real weights.",
        S_BODY
    ))

story.append(Paragraph("Read this before you start", S_H2))
story.append(Paragraph(
    "This program is training education, not medical advice. It doesn't replace guidance "
    "from a doctor or physical therapist. If you have an existing injury, are pregnant, or "
    "are returning from injury, get cleared before starting. Stop any exercise that produces "
    "sharp pain, and check with a medical professional rather than pushing through it.",
    S_MUTED
))
story.append(PageBreak())

# =========================================================
# WEEKLY RHYTHM
# =========================================================
brand_header()
story.append(Paragraph("Your Weekly Rhythm", S_H1))
hr()
story.append(Paragraph(
    "The same 7-day pattern repeats for all four weeks. Four training days, two of which "
    "carry a built-in mobility block, and three rest days — recovery is part of the program, "
    "not a gap in it.",
    S_BODY
))
story.append(Spacer(1, 6))

# Rest days (3, 6, 7) aren't in the generator's output -- it only models the
# 4 training days -- so they're inserted here to complete the 7-day week.
rhythm_rows = [
    ["DAY", "FOCUS"],
    ["1", week1_days[0]["focus"]],
    ["2", week1_days[1]["focus"] + "  +  Mobility & Recovery"],
    ["3", "Rest"],
    ["4", week1_days[2]["focus"]],
    ["5", week1_days[3]["focus"] + "  +  Mobility & Recovery"],
    ["6", "Rest (optional light walk or stretch)"],
    ["7", "Rest"],
]
t = Table(rhythm_rows, colWidths=[0.6*inch, 5.9*inch])
t.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (-1, 0), INK),
    ("TEXTCOLOR", (0, 0), (-1, 0), WHITE),
    ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
    ("FONTSIZE", (0, 0), (-1, -1), 9),
    ("ROWBACKGROUNDS", (0, 1), (-1, -1), [WHITE, ACCENT_FILL]),
    ("GRID", (0, 0), (-1, -1), 0.5, RULE),
    ("TOPPADDING", (0, 0), (-1, -1), 6),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
    ("LEFTPADDING", (0, 0), (-1, -1), 8),
    ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
]))
story.append(t)
story.append(Spacer(1, 14))
story.append(Paragraph(
    "* marks a corrective-priority exercise — these are here specifically for "
    "dance-injury prevention (ankle, hip, adductor), not general conditioning. Don't skip them "
    "even on a short session.",
    S_MUTED
))
story.append(PageBreak())

# =========================================================
# WORKOUT DAY PAGES (from live generator data)
# =========================================================
for day in week1_days:
    render_day_page(day)

# =========================================================
# 30-DAY CALENDAR
# =========================================================
brand_header()
story.append(Paragraph("Your 30-Day Calendar", S_H1))
hr()
story.append(Paragraph(
    "Check off each day as you go. Same four training days on repeat for weeks 1–4 "
    "— the work is to execute and progress within them, not to chase novelty.",
    S_BODY
))
story.append(Spacer(1, 8))

cal_header = ["WEEK", "DAY", "FOCUS", "DONE"]
cal_data = [cal_header]
week_plan = [
    f"Day 1 — {week1_days[0]['focus']}",
    f"Day 2 — {week1_days[1]['focus']} + Mobility",
    "Day 3 — Rest",
    f"Day 4 — {week1_days[2]['focus']}",
    f"Day 5 — {week1_days[3]['focus']} + Mobility",
    "Day 6 — Rest (optional light walk)",
    "Day 7 — Rest",
]
day_counter = 1
for wk in range(1, 5):
    for i, focus in enumerate(week_plan):
        cal_data.append([f"W{wk}" if i == 0 else "", str(day_counter), Paragraph(focus, S_CELL), "[ ]"])
        day_counter += 1
cal_data.append(["W5", "29", Paragraph("Progress Check — retest your Day 1 baseline", S_CELL_BOLD), "[ ]"])
cal_data.append(["", "30", Paragraph("Rest & Reflect + What's Next", S_CELL_BOLD), "[ ]"])

t = Table(cal_data, colWidths=[0.5*inch, 0.4*inch, 4.9*inch, 0.4*inch], repeatRows=1)
t.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (-1, 0), INK),
    ("TEXTCOLOR", (0, 0), (-1, 0), WHITE),
    ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
    ("FONTSIZE", (0, 0), (-1, -1), 8),
    ("ALIGN", (0, 0), (1, -1), "CENTER"),
    ("ALIGN", (3, 0), (3, -1), "CENTER"),
    ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
    ("ROWBACKGROUNDS", (0, 1), (-1, -1), [WHITE, ACCENT_FILL]),
    ("GRID", (0, 0), (-1, -1), 0.5, RULE),
    ("TOPPADDING", (0, 0), (-1, -1), 4),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
]))
story.append(t)
story.append(PageBreak())

# =========================================================
# NUTRITION
# =========================================================
brand_header()
story.append(Paragraph("Nutrition & Recovery Baseline", S_H1))
hr()
story.append(Paragraph(
    "Dancers are a documented at-risk group for RED-S (Relative Energy Deficiency in "
    "Sport) — the consequence of chronically under-fueling relative to training and "
    "rehearsal demand. This is a baseline, not a full nutrition plan.",
    S_BODY
))

macro_rows = [
    ["TARGET", "RANGE"],
    ["Carbohydrate", "3-5 g/kg bodyweight/day"],
    ["Protein", "1.2-1.7 g/kg bodyweight/day"],
    ["Fat", "20-35% of total energy intake"],
    ["Energy floor", ">=30 kcal/kg fat-free mass/day, plus training expenditure"],
]
t = Table(macro_rows, colWidths=[2.1*inch, 4.1*inch])
t.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (-1, 0), INK),
    ("TEXTCOLOR", (0, 0), (-1, 0), WHITE),
    ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
    ("FONTSIZE", (0, 0), (-1, -1), 9),
    ("ROWBACKGROUNDS", (0, 1), (-1, -1), [WHITE, ACCENT_FILL]),
    ("GRID", (0, 0), (-1, -1), 0.5, RULE),
    ("TOPPADDING", (0, 0), (-1, -1), 6),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
    ("LEFTPADDING", (0, 0), (-1, -1), 8),
]))
story.append(t)
story.append(Spacer(1, 12))

story.append(Paragraph("Watch for", S_H2))
story.append(Paragraph(
    "Unintentional weight loss during this program, irregular or missed menstrual cycles, "
    "fatigue disproportionate to the training load, or repeated stress-response injuries "
    "(stress fractures, frequent soft-tissue injury). These are RED-S indicators, not just "
    "overtraining — iron and calcium are the micronutrients most often low in dancers' "
    "diets specifically.",
    S_BODY
))

story.append(Paragraph("Sleep", S_H2))
story.append(Paragraph(
    "Target 7–9 hours. Deep sleep specifically — not just total time in bed — "
    "is where growth hormone release, protein synthesis, and connective-tissue repair "
    "concentrate. If you're stacking rehearsal on top of this program, treat sleep debt as "
    "a cue to pull back volume, the same way you'd respond to pain or missed reps.",
    S_BODY
))

story.append(Paragraph(
    "Actual RED-S risk assessment and individualized nutrition prescription belong to a "
    "doctor or sports dietitian — this page is baseline awareness, not a diagnosis or "
    "a meal plan.",
    S_MUTED
))
story.append(PageBreak())

# =========================================================
# DAY 29-30
# =========================================================
brand_header()
day_banner("DAY 29", "Progress Check")
story.append(Paragraph(
    "Retest the same four numbers from before Day 1, same conditions if you can (same "
    "time of day, warmed up the same way):",
    S_BODY
))
for item in ["Max pull-ups (or assisted pull-ups to failure)", "Max plank hold", "Single-leg balance, eyes closed, each side", "Standing broad jump distance"]:
    story.append(Paragraph(f"- {item}", S_BODY))
story.append(Spacer(1, 4))
story.append(Paragraph(
    "The number matters less than the trend. Cleaner form at the same load, less wobble on "
    "the single-leg work, a longer jump — all of that is the program working, even if "
    "the headline number moves less than you'd expect in four weeks.",
    S_MUTED
))
story.append(Spacer(1, 16))

day_banner("DAY 30", "Rest & Reflect")
story.append(Paragraph(
    "Full rest. Deep sleep, hydration, and mobility only today — no training.",
    S_BODY
))
story.append(Spacer(1, 14))

story.append(Paragraph("What's Next", S_H1))
hr()
story.append(Paragraph(
    "This 30-day block is Phase 1 of the full XOLOKAN Method — a 12-week arc that moves "
    "through Base Strength &amp; Control, into Power &amp; Volume, and peaks at 85–90% "
    "intensity. The next block is where load and difficulty actually progress past where this "
    "one leaves off.",
    S_BODY
))
story.append(Paragraph(
    "XOLOKAN, the AI coach built on this same method, can build your personalized next block "
    "from your actual training history, equipment, and goals — or you can work directly "
    "with Oscar for hands-on coaching. Ask your coach about the Personalized and Premium tiers.",
    S_BODY
))
story.append(Spacer(1, 20))
story.append(Paragraph("X O L O &nbsp; F I T N E S S", S_BRAND))
story.append(Paragraph("PRECISION. DISCIPLINE. PERFORMANCE.", style("tag", fontSize=9, textColor=MUTED, alignment=TA_CENTER, fontName="Helvetica-Oblique")))


# =========================================================
# PAGE FRAME (footer / margins)
# =========================================================
def on_page(c: canvas_mod.Canvas, doc):
    c.saveState()
    c.setStrokeColor(RULE)
    c.setLineWidth(0.5)
    c.line(ML, MB - 10, PW - MR, MB - 10)
    c.setFont("Helvetica", 7.5)
    c.setFillColor(MUTED)
    c.drawString(ML, MB - 22, f"XOLOKAN Dancer Protocol — 30-Day Foundation ({EDITION_LABEL.title()})")
    c.drawRightString(PW - MR, MB - 22, f"Page {doc.page}")
    c.restoreState()

doc = SimpleDocTemplate(
    OUT_PATH, pagesize=letter,
    leftMargin=ML, rightMargin=MR, topMargin=MT, bottomMargin=MB,
    title=f"XOLOKAN Dancer Protocol — 30-Day Foundation ({EDITION_LABEL.title()})",
    author="XOLO FITNESS",
)
doc.build(story, onFirstPage=on_page, onLaterPages=on_page)
print(f"Wrote {OUT_PATH}")
