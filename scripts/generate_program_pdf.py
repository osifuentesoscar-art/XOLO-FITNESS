"""
XOLOKAN sellable PDF program generator — all archetypes, both scopes.

Exercise selection, sets, and reps are pulled LIVE from generateProgram()
(via generateSampleCli.ts) at build time -- never hardcoded here -- so
these PDFs and the actual program generator can't drift apart as
archetypes.ts evolves. Only coaching cues, RIR targets, rest times, and
marketing copy are authored in this script.

Usage:
  python3 scripts/generate_program_pdf.py --archetype dancer --equipment bodyweight-only --scope 30-day [output_path]
  python3 scripts/generate_program_pdf.py --archetype gymnast-aerialist --equipment full-gym --scope 12-week [output_path]

Archetypes: dancer | gymnast-aerialist | general-performer
Equipment:  bodyweight-only | full-gym
Scope:      30-day (Phase 1 entry product) | 12-week (full Method, all 3 phases)
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
parser.add_argument("--archetype", choices=["dancer", "gymnast-aerialist", "general-performer"], required=True)
parser.add_argument("--equipment", choices=["bodyweight-only", "full-gym"], default="bodyweight-only")
parser.add_argument("--scope", choices=["30-day", "12-week"], default="30-day")
args = parser.parse_args()

ARCHETYPE = args.archetype
EQUIPMENT = args.equipment
SCOPE = args.scope
EDITION_LABEL = "GYM EDITION" if EQUIPMENT == "full-gym" else "BODYWEIGHT EDITION"
SCOPE_LABEL = "30-DAY FOUNDATION" if SCOPE == "30-day" else "12-WEEK METHOD"

DEFAULT_OUT = f"XOLOKAN_{ARCHETYPE.replace('-', '_')}_{SCOPE.replace('-', '_')}_{EQUIPMENT.replace('-', '_')}.pdf"
OUT_PATH = args.output or DEFAULT_OUT

# =========================================================
# Product marketing metadata per archetype -- authored here,
# not in the generator, same reasoning as CUES below.
# =========================================================
PRODUCT_META = {
    "dancer": {
        "client_name": "Dancer",
        "cover_dek": "Soviet-block periodization, calisthenics-built relative strength, and dance-specific injury prevention.",
        "why_line": (
            "the first randomized controlled trial of an injury prevention program in professional ballet "
            "(Houston Ballet) ran a strength-focused program 3x/week for a year and cut injury rate by 82%, "
            "with 45% longer time between injuries. This program is built on that same principle, not a "
            "stretching routine with some strength bolted on."
        ),
    },
    "gymnast-aerialist": {
        "client_name": "Gymnast/Aerialist",
        "cover_dek": "Soviet-block periodization, apparatus-ready relative strength, and shoulder/wrist/ankle resilience for gymnasts and aerialists.",
        "why_line": (
            "relative strength-to-bodyweight ratio is what actually transfers to apparatus work -- a heavier "
            "external load doesn't help a ring support hold or a handstand. This program builds strength the "
            "way your body actually performs in, not in a way that fights it."
        ),
    },
    "general-performer": {
        "client_name": "Performer",
        "cover_dek": "Soviet-block periodization and balanced strength/conditioning built for the demands of rehearsal, travel, and stage-ready athleticism.",
        "why_line": (
            "actors, musicians, and performers rarely get injured from one big moment -- it's cumulative load "
            "from packed schedules with no structure underneath. This program gives you that structure without "
            "assuming you live in a gym."
        ),
    },
}

# =========================================================
# Pull live program data from the generator (source of truth)
# =========================================================
def get_program():
    result = subprocess.run(
        [
            "npx", "tsx", "packages/xolokan-agent/src/generateSampleCli.ts",
            "--name", PRODUCT_META[ARCHETYPE]["client_name"],
            "--discipline", ARCHETYPE,
            "--level", "intermediate",
            "--age", "25-30",
            "--sex", "female",
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
archetype_label = program["title"].split(" — ")[0]  # e.g. "XOLOKAN Dancer Protocol"

# =========================================================
# Coaching cues -- authored here, keyed by exercise name.
# Covers every exercise across all 3 archetypes, both equipment modes.
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
    "Banded Lateral Walk": {"rir": "-", "rest": "30s", "cue": "Band above the knees, stay low, knees track over toes — not a warm-up, this is ACL prehab."},
    # Gymnast/Aerialist-specific
    "Ring Support Hold":   {"rir": "-", "rest": "60s", "cue": "Arms locked, shoulders down and back, rings turned out."},
    "Handstand Push-Ups":  {"rir": "2", "rest": "90s", "cue": "Head stays neutral, press to a full lockout."},
    "Pistol Squat Progression": {"rir": "2", "rest": "90s", "cue": "Work the range you actually control — box or assisted is fine, chase depth over time."},
    "Dips":                {"rir": "2", "rest": "75s", "cue": "Full lockout at the top, control the bottom, slight forward lean."},
    "L-Sit Progression":   {"rir": "-", "rest": "60s", "cue": "Legs as straight as your current level allows, shoulders depressed."},
    "Farmer Carry":        {"rir": "-", "rest": "60s", "cue": "Tall posture, braced core, don't let the weight pull you sideways."},
    "Wall Handstand Hold": {"rir": "-", "rest": "60s", "cue": "Heels on the wall, hollow body, push the floor away."},
    # General-Performer-specific
    "Medicine Ball Slams": {"rir": "-", "rest": "60s", "cue": "Full extension overhead, drive through the hips, slam — not a controlled lower."},
    "Dead Bug":            {"rir": "-", "rest": "45s", "cue": "Low back stays flat against the floor the whole rep."},
    "Hip Airplane":        {"rir": "-", "rest": "45s", "cue": "Slow and controlled, hips stay square as you rotate."},
}

DAY_OUTRO_30DAY = {
    3: (
        "This is the highest-impact day in the program. As written it's roughly "
        "intermediate-level jump volume. If today's the first time you've trained plyometrics "
        "in a while, cut every set count by one and build up over the four weeks — landing "
        "mechanics earn their place gradually, not all at once. "
        "<b>History of ankle sprains?</b> Add single-leg balance work (eyes closed, 30s each "
        "side) on a rest day — sprain recurrence is driven more by balance and joint sense "
        "than by strength alone."
    ),
}

# Archetype-specific overrides, checked before the day-number default above.
DAY_OUTRO_30DAY_BY_ARCHETYPE = {
    ("gymnast-aerialist", 1): (
        "Ring and handstand support work loads the shoulder differently than pressing does. "
        "Before progressing Ring Support Hold or Handstand Push-Ups, screen shoulder internal "
        "rotation and scapular control — labral and rotator-cuff strain in ring/bar work tracks "
        "with rotation deficits and scapular dyskinesia, not just hold volume. If shoulder ROM "
        "feels limited, regress to shorter holds and build periscapular strength first rather "
        "than pushing hold time."
    ),
}

def get_day_outro(day_number):
    return DAY_OUTRO_30DAY_BY_ARCHETYPE.get((ARCHETYPE, day_number)) or DAY_OUTRO_30DAY.get(day_number)

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
S_TITLE = style("title", fontName="Helvetica-Bold", fontSize=26, leading=30, textColor=INK, alignment=TA_CENTER)
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

def render_day_page(day, day_outro=None):
    brand_header()
    day_banner(f"DAY {day['dayNumber']}", day["focus"])
    story.append(day_table(day["exercises"]))
    if day_outro:
        story.append(Spacer(1, 8))
        story.append(Paragraph(day_outro, S_MUTED))
    if day.get("mobilitySession"):
        story.append(Spacer(1, 10))
        mobility_block()
    story.append(PageBreak())

def what_youll_need_paragraph():
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
        story.append(Paragraph(
            "Bodyweight-only isn't a lesser version of this program. Research on load and muscle "
            "growth shows low-load training taken close to effort builds muscle comparably to "
            "heavy weights — max strength still favors load, but hypertrophy doesn't require it. "
            "Push these sets hard and you'll get real results.",
            S_MUTED
        ))

def read_this_before_you_start():
    story.append(Paragraph("Read this before you start", S_H2))
    story.append(Paragraph(
        "This program is training education, not medical advice. It doesn't replace guidance "
        "from a doctor or physical therapist. If you have an existing injury, are pregnant, or "
        "are returning from injury, get cleared before starting. Stop any exercise that produces "
        "sharp pain, and check with a medical professional rather than pushing through it.",
        S_MUTED
    ))

def footer_page():
    story.append(Spacer(1, 20))
    story.append(Paragraph("X O L O &nbsp; F I T N E S S", S_BRAND))
    story.append(Paragraph("PRECISION. DISCIPLINE. PERFORMANCE.", style("tag", fontSize=9, textColor=MUTED, alignment=TA_CENTER, fontName="Helvetica-Oblique")))

def nutrition_page():
    brand_header()
    story.append(Paragraph("Nutrition & Recovery Baseline", S_H1))
    hr()
    story.append(Paragraph(
        "Dancers, gymnasts, and other lean, aesthetic-conscious performers are a documented "
        "at-risk group for RED-S (Relative Energy Deficiency in Sport) — the consequence of "
        "chronically under-fueling relative to training and rehearsal demand. This is a "
        "baseline, not a full nutrition plan.",
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
        "Unintentional weight loss, irregular or missed menstrual cycles, fatigue "
        "disproportionate to the training load, or repeated stress-response injuries (stress "
        "fractures, frequent soft-tissue injury). These are RED-S indicators, not just "
        "overtraining — iron and calcium are the micronutrients most often low in this "
        "population's diets.",
        S_BODY
    ))
    story.append(Paragraph("Sleep", S_H2))
    story.append(Paragraph(
        "Target 7–9 hours. Deep sleep specifically — not just total time in bed — is where "
        "growth hormone release, protein synthesis, and connective-tissue repair concentrate. "
        "If you're stacking rehearsal on top of this program, treat sleep debt as a cue to "
        "pull back volume, the same way you'd respond to pain or missed reps.",
        S_BODY
    ))
    story.append(Paragraph("Creatine", S_H2))
    story.append(Paragraph(
        "3-5g creatine monohydrate daily, no loading phase needed, taken consistently rather "
        "than only on training days. The evidence here isn't just extrapolated from male "
        "strength athletes — a trial in female collegiate dancers found increased lean mass "
        "with no adverse effects, and separate research found creatine measurably reduces "
        "cognitive decline under sleep deprivation — directly useful if you're stacking "
        "rehearsal on top of this program.",
        S_BODY
    ))
    story.append(Paragraph(
        "Actual RED-S risk assessment and individualized nutrition prescription belong to a "
        "doctor or sports dietitian — this page is baseline awareness, not a diagnosis or a "
        "meal plan.",
        S_MUTED
    ))
    story.append(PageBreak())


# =========================================================
# COVER
# =========================================================
meta = PRODUCT_META[ARCHETYPE]
story.append(Spacer(1, 1.4*inch))
brand_header()
story.append(Spacer(1, 0.35*inch))
story.append(Paragraph(archetype_label.upper(), S_TITLE))
story.append(Spacer(1, 10))
story.append(Paragraph(SCOPE_LABEL, S_SUBTITLE))
story.append(Paragraph(EDITION_LABEL, style("edition", fontName="Helvetica-Bold", fontSize=10, textColor=MUTED, alignment=TA_CENTER, spaceBefore=4)))
story.append(Spacer(1, 16))
story.append(Paragraph(meta["cover_dek"], S_DEK))
story.append(Spacer(1, 0.8*inch))
equip_tag = "FULL STRENGTH TRAINING" if EQUIPMENT == "full-gym" else "BODYWEIGHT-FOCUSED"
scope_tag = "4 WEEKS" if SCOPE == "30-day" else "12 WEEKS · 3 PHASES"
story.append(Paragraph(f"{equip_tag} &nbsp;&#8212;&nbsp; {scope_tag} &nbsp;&#8212;&nbsp; 4 TRAINING DAYS / WEEK", S_MUTED))
story.append(PageBreak())

# =========================================================
# HOW THIS WORKS
# =========================================================
brand_header()
story.append(Paragraph("How This Works", S_H1))
hr()
if SCOPE == "30-day":
    story.append(Paragraph(
        f"This is Phase 1 of the XOLOKAN Method — Base Strength &amp; Control. Four weeks "
        f"of technique-first strength, calisthenics-built relative strength, and "
        f"injury-prevention work built for you specifically, at 70–75% intensity. Form over "
        f"load, every session.",
        S_BODY
    ))
else:
    story.append(Paragraph(
        "This is the complete XOLOKAN Method: 12 weeks across three phases, each building on "
        "the one before it. <b>Phase 1, Base Strength &amp; Control</b> (weeks 1-4, 70-75%): "
        "form and stability. <b>Phase 2, Power &amp; Volume</b> (weeks 5-8, 75-85%): the same "
        "movement patterns, more explosive and higher volume. <b>Phase 3, Peak Performance</b> "
        "(weeks 9-12, 85-90%): maximal expression, volume drops as speed rises. The exercises "
        "don't change between phases — this is a Soviet-block system, and the phases are how "
        "hard you push the same movements, not a new program every 4 weeks.",
        S_BODY
    ))
story.append(Paragraph(f"<b>Why this works:</b> {meta['why_line']}", S_BODY))

story.append(Paragraph("Before Day 1 — record your baseline", S_H2))
story.append(Paragraph(
    "Log these four numbers before your first session: max pull-ups (or assisted to failure), "
    "max plank hold, single-leg balance (eyes closed, each side), and standing broad jump "
    "distance." + (" You'll retest them on Day 29." if SCOPE == "30-day" else " You'll retest them at the end of each phase (weeks 4, 8, and 12)."),
    S_BODY
))

story.append(Paragraph("Effort: RIR, not percentages", S_H2))
story.append(Paragraph(
    "RIR means Reps In Reserve — how many more reps you could do before failure. Most working "
    "sets in this program are RIR 2: stop with two clean reps left in the tank. "
    "<b>Progression rule:</b> if you hit the top of a rep range at RIR 2+ with clean form, add "
    "a rep or a small load/difficulty bump next session. If form breaks down or you're at RIR "
    "0–1 before the last set, hold where you are.",
    S_BODY
))

story.append(Paragraph("Warm up with RAMP, every session", S_H2))
story.append(Paragraph(
    "<b>Raise</b> — 3–5 min light cardio to raise core and muscle temperature. "
    "<b>Activate &amp; Mobilise</b> — active-range movement through today's actual patterns, "
    "not static stretching. <b>Potentiate</b> — a few submaximal reps of today's first "
    "exercise to prime the nervous system. Static stretching, if you use it, belongs after "
    "training — not before.",
    S_BODY
))

what_youll_need_paragraph()
read_this_before_you_start()
story.append(PageBreak())

# =========================================================
# WEEKLY RHYTHM
# =========================================================
week1_days = program["weeks"][0]["days"]

brand_header()
story.append(Paragraph("Your Weekly Rhythm", S_H1))
hr()
story.append(Paragraph(
    "This 7-day pattern repeats every week of the program. Four training days, two of which "
    "carry a built-in mobility block, and three rest days — recovery is part of the program, "
    "not a gap in it.",
    S_BODY
))
story.append(Spacer(1, 6))
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
    "* marks a corrective-priority exercise — these are here specifically for injury "
    "prevention, not general conditioning. Don't skip them even on a short session.",
    S_MUTED
))
story.append(PageBreak())

# =========================================================
# SCOPE-SPECIFIC BODY
# =========================================================
if SCOPE == "30-day":
    for day in week1_days:
        render_day_page(day, get_day_outro(day["dayNumber"]))

    # 30-day calendar
    brand_header()
    story.append(Paragraph("Your 30-Day Calendar", S_H1))
    hr()
    story.append(Paragraph(
        "Check off each day as you go. Same four training days on repeat for weeks 1–4 — "
        "the work is to execute and progress within them, not to chase novelty.",
        S_BODY
    ))
    story.append(Spacer(1, 8))
    cal_data = [["WEEK", "DAY", "FOCUS", "DONE"]]
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

    nutrition_page()

    brand_header()
    day_banner("DAY 29", "Progress Check")
    story.append(Paragraph(
        "Retest the same four numbers from before Day 1, same conditions if you can:",
        S_BODY
    ))
    for item in ["Max pull-ups (or assisted to failure)", "Max plank hold", "Single-leg balance, eyes closed, each side", "Standing broad jump distance"]:
        story.append(Paragraph(f"- {item}", S_BODY))
    story.append(Spacer(1, 4))
    story.append(Paragraph(
        "The number matters less than the trend. Cleaner form at the same load, less wobble "
        "on the single-leg work, a longer jump — all of that is the program working.",
        S_MUTED
    ))
    story.append(Spacer(1, 16))
    day_banner("DAY 30", "Rest & Reflect")
    story.append(Paragraph("Full rest. Deep sleep, hydration, and mobility only today — no training.", S_BODY))
    story.append(Spacer(1, 14))
    story.append(Paragraph("What's Next", S_H1))
    hr()
    story.append(Paragraph(
        "This 30-day block is Phase 1 of the full XOLOKAN Method — a 12-week arc that moves "
        "through Base Strength &amp; Control, into Power &amp; Volume, and peaks at 85–90% "
        "intensity. Ask about the full 12-Week Method, or XOLOKAN's Personalized tier for a "
        "program built from your actual training history and goals.",
        S_BODY
    ))
    footer_page()

else:  # 12-week
    phase_info = [
        (1, "base", "Base Strength & Control", "70-75%", program["weeks"][0]),
        (2, "power-volume", "Power & Volume", "75-85%", program["weeks"][4]),
        (3, "peak", "Peak Performance", "85-90%", program["weeks"][8]),
    ]
    phase_intros = {
        1: "Weeks 1-4. Form and stability first — every rep here is the technical foundation the next two phases load on top of.",
        2: "Weeks 5-8. Same exercises, more explosive intent and higher volume. If a movement felt clean in Phase 1, this is where it gets tested.",
        3: "Weeks 9-12. Peak intensity, volume drops as speed rises. Week 12 is a deload — reduced volume by design, not a sign to push harder.",
    }

    for phase_num, phase_key, phase_name, intensity, week_data in phase_info:
        brand_header()
        story.append(Paragraph(f"Phase {phase_num}: {phase_name}", S_H1))
        story.append(Paragraph(f"Intensity: {intensity}", S_SUBTITLE))
        hr()
        story.append(Paragraph(phase_intros[phase_num], S_BODY))
        story.append(PageBreak())

        for day in week_data["days"]:
            outro = get_day_outro(day["dayNumber"]) if phase_num == 1 else None
            render_day_page(day, outro)

        brand_header()
        day_banner(f"END OF PHASE {phase_num}", "Progress Check")
        story.append(Paragraph(
            "Retest your baseline numbers: max pull-ups (or assisted to failure), max plank "
            "hold, single-leg balance (eyes closed, each side), and standing broad jump "
            "distance.",
            S_BODY
        ))
        if phase_num < 3:
            story.append(Paragraph(
                f"Trend matters more than the number. When you're ready, move to Phase "
                f"{phase_num + 1} — same exercises, higher intensity.",
                S_MUTED
            ))
        story.append(PageBreak())

    # 12-week phase map
    brand_header()
    story.append(Paragraph("Your 12-Week Phase Map", S_H1))
    hr()
    story.append(Paragraph(
        "The weekly 7-day rhythm (previous page) repeats identically inside every phase — "
        "what changes week to week is intensity, tracked here.",
        S_BODY
    ))
    story.append(Spacer(1, 8))
    map_rows = [["WEEK", "PHASE", "INTENSITY", "NOTE"]]
    for w in program["weeks"]:
        phase_display = {"base": "1 — Base", "power-volume": "2 — Power & Volume", "peak": "3 — Peak"}[w["phase"]]
        note = "Deload" if w["isDeload"] else ""
        map_rows.append([str(w["weekNumber"]), phase_display, w["intensity"], note])
    t = Table(map_rows, colWidths=[0.7*inch, 2.3*inch, 1.3*inch, 1.9*inch], repeatRows=1)
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), INK),
        ("TEXTCOLOR", (0, 0), (-1, 0), WHITE),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTSIZE", (0, 0), (-1, -1), 9),
        ("ALIGN", (0, 0), (0, -1), "CENTER"),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [WHITE, ACCENT_FILL]),
        ("GRID", (0, 0), (-1, -1), 0.5, RULE),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
        ("LEFTPADDING", (0, 0), (-1, -1), 8),
    ]))
    story.append(t)
    story.append(PageBreak())

    nutrition_page()

    brand_header()
    story.append(Paragraph("What's Next", S_H1))
    hr()
    story.append(Paragraph(
        "You've completed the full XOLOKAN Method — all three phases. From here: retest your "
        "full baseline, and either run the arc again from Phase 1 with your new numbers as the "
        "starting point, or move to XOLOKAN's Personalized tier for a program built around "
        "where you actually are now, not where this program assumed you'd start.",
        S_BODY
    ))
    footer_page()


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
    c.drawString(ML, MB - 22, f"{archetype_label} — {SCOPE_LABEL.title()} ({EDITION_LABEL.title()})")
    c.drawRightString(PW - MR, MB - 22, f"Page {doc.page}")
    c.restoreState()

doc = SimpleDocTemplate(
    OUT_PATH, pagesize=letter,
    leftMargin=ML, rightMargin=MR, topMargin=MT, bottomMargin=MB,
    title=f"{archetype_label} — {SCOPE_LABEL.title()} ({EDITION_LABEL.title()})",
    author="XOLO FITNESS",
)
doc.build(story, onFirstPage=on_page, onLaterPages=on_page)
print(f"Wrote {OUT_PATH}")
