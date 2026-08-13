# XOLOKAN Methodology — Research Log

Append-only log of the daily research pass. Most recent entry on top. Exists
so each day's run knows what's already been checked and when, independent of
conversation memory — the methodology doc's own Sources section is the
citation list, this log is the audit trail of what was searched and why
nothing changed (or did).

Topic rotation the daily pass draws from: periodization, calisthenics /
relative strength, dance-injury prevention, gymnast/aerialist-specific
injury prevention, plyometrics, RPE/autoregulation, warm-up & recovery,
nutrition for performers.

---

## 2026-08-13 — RIR-accuracy-by-experience + autoregulation-vs-fixed-periodization nuance

**Checked:** RPE/autoregulation (stalest topic, last touched 2026-08-09).

**Found:** Two honest caveats not yet in the methodology, both refining
rather than contradicting the existing APRE/RIR guidance: (1) self-reported
RIR accuracy improves with training experience, meaning novice clients
aren't yet reliable judges of "2 reps in reserve" — worth coaching more
conservatively and explicitly (bar speed, form breakdown) until that skill
develops. (2) A 10-week RCT in resistance-trained men found autoregulated
volume adjustment layered onto an already well-periodized program produced
no additional strength, power, or muscle-thickness gains over the fixed
periodized program alone — a useful check against overselling
autoregulation as a strength-gain multiplier rather than what it actually
is: a readiness/fatigue safety valve.

**Action:** Added both caveats to methodology §1 (Periodization framework,
autoregulation subsection) and the mirrored block in persona.ts. Framed as
nuance on existing guidance, not a correction — the "leave 2 in the tank"
default and APRE-for-primary-lifts guidance are unchanged. Two sources
added, both new.

## 2026-08-12 — creatine for performers + recovery-modality dosing

**Checked:** Nutrition for performers (stalest topic, last touched
2026-08-08) and, as a secondary pass, warm-up & recovery (last touched
2026-08-09).

**Found:** (1) The Nutrition & Energy Availability section covered macros
and RED-S but had zero creatine content, despite creatine being one of the
best-evidenced, safest supplements for exactly this population. Two
concrete findings closed that gap: a 42-day trial in female collegiate
dancers found increased total body water and DXA lean mass with
supplementation (direct evidence in the target demographic, not an
extrapolation from male strength-athlete data), and separate research
found a single dose of creatine measurably reduces sleep-deprivation-
induced cognitive decline (processing speed, working memory) — directly
relevant since the methodology already treats sleep debt as a
training-load variable. (2) On recovery modality: a 2025 RCT found
percussion massage outperforms static stretching for DOMS recovery, and a
2025 network meta-analysis pinned the effective cold water immersion dose
at 10-15 minutes (shorter soaks are largely symbolic) — new, specific,
citable numbers beyond the existing generic "static stretching belongs in
cooldown" line.

**Action:** Added a Creatine paragraph to methodology §6 (Nutrition &
Energy Availability) and persona.ts section 5, with standard protocol
(3-5 g/day monohydrate, no loading phase). Added a brief recovery-modality
note (percussion massage vs. static stretching, cold water immersion
dosing) to methodology §2's warm-up/cooldown passage and persona.ts's
mirrored RAMP bullet, framed as optional refinements, not a change to the
non-negotiable RAMP protocol. Four sources added. Both incremental edits,
scoped to the existing sections — no restructuring.

## 2026-08-11 — plyometric dosing mechanism + gymnast spondylolysis

**Checked:** Plyometrics (untouched since the original baseline build — no
dedicated daily pass had revisited it) and gymnast/aerialist-specific
injury prevention (last touched 2026-08-08, for wrist only).

**Found:** (1) A 2025/2026 dosing consensus for plyometrics: tendons adapt
slower than muscle, which is the mechanistic reason for the existing
48-72h spacing rule (not just a conservative default), plus a 4-6 week
block-progression framing and a concrete landing cue (heel stays high,
short amortization — a long amortization phase bleeds the elastic energy
the training is supposed to build). (2) Spondylolysis (pars interarticularis
stress fracture) is the dominant cause of low back pain in adolescent/young
gymnasts specifically — a real gap, since the methodology's lower-back row
only covered the generic dancer mechanism (disc/muscle strain from axial
loading). Spondylolysis is driven by repetitive spinal hyperextension +
rotation (backbends, walkovers, aerial arch work) instead, and needs deep
trunk/lumbar stabilization in a neutral spine, not generic core work.

**Action:** Added the tendon-adaptation rationale, block-progression
framing, and landing cue to the plyometric dosage section (methodology +
persona). Added a second, gymnast-specific Lower Back row to the injury
table (methodology + persona) alongside the existing generic one, making
clear it's a different mechanism requiring a different countermeasure.
Both incremental, six sources added.

## 2026-08-10 (later) — age & sex as demographic programming factors (user-requested)

**Checked:** Requested by Oscar, not the daily rotation — build age range
(20-25/25-30/30-35/35-40) and anatomical sex (female/male) into the
generator as real programming factors, not just documentation. Researched
fresh and independently for this project: bone-density age curves, tendon/
connective-tissue adaptation timelines, training-age recovery research,
ACL injury risk and Q-angle/landing-mechanics differences by sex, pelvic
floor dysfunction in young female strength athletes specifically, relative
vs. absolute strength gains by sex, and the current menstrual-cycle-and-
performance evidence base.

**Found:** (1) Peak bone mass hits ~25.7y (men) / ~24.8y (women), then
plateaus for decades — makes 20-25/25-30 the highest-leverage window for
heavy compound loading. (2) Recovery capacity declines gradually from the
early-to-mid 30s, ~10-20% longer regeneration windows by 35-40 (hormonal,
satellite cell, sleep-architecture factors) — a pacing adjustment, not a
capability cliff. (3) ACL injury risk is 3-8x higher in women (Q-angle +
quad-dominant landing pattern), directly actionable via posterior-chain/
hip-abductor work and landing cues. (4) Pelvic floor dysfunction is
significantly prevalent in young female strength athletes specifically —
not just postpartum/older populations, which is a common and incorrect
assumption. (5) A 2023 umbrella review (top of the evidence hierarchy)
found no reliable menstrual-cycle-phase effect on strength performance or
adaptation — cycle-syncing programming is not evidence-supported. (6)
Women show greater *relative* strength gains than men despite smaller
absolute ones — validates the method's existing relative-strength-as-
primary-metric framework as sex-fair by design already.

**Action:** Added `ageRange` and `sex` as required `ClientIntake` fields
(`programSchema.ts`), a new `demographics.ts` module producing age/sex
notes plus a sex-specific corrective exercise (Banded Lateral Walk, ACL
prehab) for female clients, wired into `generateProgram()` — every program
now carries `demographicNotes` and the corrective is inserted
automatically. Updated the SDK tool schema, CLI, methodology doc (new §7),
and persona to match. All 3 archetypes x both sexes x all 4 age brackets
smoke-tested. The 30-Day Foundation PDF's fixed demographic default
(female, 25-30) is now an explicit, documented product decision rather
than an implicit CLI default — see `docs/business/PRODUCT_CHANGELOG.md`.

**Framing note:** the sex field is explicitly documented as
anatomical/biomechanical (tied to Q-angle, ACL risk, pelvic floor
anatomy), not a claim about ability, preference, or identity — worth
preserving that framing in any future edits to this content.

**Also completed (standing practice):** full contamination scan across
repo source and both regenerated PDFs. Clean.

## 2026-08-11 — block periodization lineage + load-independent hypertrophy

**Checked:** Periodization and calisthenics/relative strength — both only
touched at baseline (2026-08-08), never revisited since, unlike every other
topic in the rotation which has had a dedicated pass in the last two days.

**Found:** (1) Vladimir Issurin systematized Verkhoshansky's block concept
into three named blocks — Accumulation, Transmutation, Realization — which
map almost exactly onto XOLOKAN's Base Strength & Control / Power & Volume
/ Peak Performance phases. The methodology cited Matveyev vs. Verkhoshansky
already but hadn't credited the specific three-block structure it actually
uses. (2) Schoenfeld et al.'s meta-analysis: low-load (<=60% 1RM-equivalent)
resistance training taken close to failure builds hypertrophy comparably to
high-load training — max strength still favors heavy loads, but muscle
growth doesn't require them. Directly validates that bodyweight-only
programming isn't a lesser version of the method, it's evidence-supported.

**Action:** Added Issurin's block terminology to §1's Origins paragraph,
mapping each block to its XOLOKAN phase and stating the sequencing
principle explicitly (each block depends on the residual effect of the one
before it — the real reason phase order can't be skipped). Added a
load-independent hypertrophy callout to §3 (methodology + persona), citing
Schoenfeld directly. Both incremental, no restructuring — two sources
added.

## 2026-08-10 — dance injury prevention deep dive (user-requested)

**Checked:** Requested by Oscar, not the daily rotation — a deeper look at
structured dance injury prevention protocols and screening standards,
beyond the risk-factor studies already cited.

**Found:** (1) The first prospective RCT of an injury prevention program in
professional ballet (Houston Ballet, 2020): a strength-focused 30-min
program 3x/week for 52 weeks cut injury rate 82% and extended time between
injuries 45% — direct validation of XOLOKAN's existing strength-first,
RAMP-over-static-stretch bias, not just a generic best practice. (2) IADMS
(International Association for Dance Medicine & Science) is the field's
standard-setting body for injury screening — its Standard Measures
Initiative calls for pre-season baseline screening, which the methodology
didn't explicitly frame as part of program design before this. (3)
Concrete epidemiology: ankle sprains at 0.27/1000h in elite ballet (~13-14
days lost each), ACL injuries with 92% occurring on single-leg jump
landings — reinforces existing ankle/knee content with real numbers. (4) A
genuine gap: ankle sprain *recurrence* is driven by degraded
proprioception, not just weakness — the existing ankle countermeasure
(isometric + eccentric + plyometric) doesn't address this; prior-sprain
clients need balance/joint-reposition-sense work specifically.

**Action:** Added a validating-evidence callout and IADMS screening
principle to §4 opening, updated the Ankle and Knee table rows with the
epidemiology, added a new Standing Rule (#4) and checklist item for
proprioceptive work after a prior ankle sprain, and added an IADMS-based
baseline-screening item as checklist item #1 (previously the checklist
started at "establish phase" with no screening step). All cited, all
incremental — six sources added.

**Also completed (explicit request):** A full repo + generated-PDF scan
for any Brace Life Studios / ICONS content bleeding into XOLO FITNESS
material, following the tagline mixup caught last session. Scanned repo
source (grep across all files for brand terms, hex codes, client names,
script names) and the actual generated PDF's extracted text. Result:
clean — no contamination found anywhere, including git history commit
messages.

## 2026-08-09 — autoregulation method ranking + sleep as recovery baseline

**Checked:** RPE/autoregulation (previously only touched briefly inside the
ACSM effort-landmarks table, no dedicated look at which method is best) and
warm-up & recovery (RAMP covered warm-up already; sleep/recovery specifically
was only a passing mention, no target or rationale).

**Found:** (1) A 2025 systematic review and network meta-analysis ranking
autoregulation methods for max-strength gains: APRE (Autoregulating
Progressive Resistance Exercise — test-set-driven load adjustment) ranked
highest, ahead of plain RPE, velocity-based training, and fixed-percentage
programming. (2) Sleep research confirming deep/slow-wave sleep specifically
(not just total sleep time) is where growth hormone release, protein
synthesis, and collagen/connective-tissue repair concentrate — supports a
concrete 7-9 hour target and treating sleep debt as a volume-reduction
trigger.

**Action:** Added an APRE recommendation to §1 (methodology + persona) for
primary-lift load adjustment specifically, keeping RPE/RIR as the simpler
default elsewhere. Added a sleep subsection to §2 (methodology + persona)
with a concrete duration target and the volume-reduction-trigger framing.
Both cited, both incremental — no restructuring.

## 2026-08-08 — gymnast/aerialist injury prevention + performer nutrition

**Checked:** Gymnast/aerialist-specific injury prevention (previously
unaddressed — the injury table only covered ankle/knee/lower-back/hip) and
nutrition for performers (previously not in the methodology's scope at
all).

**Found:** (1) A 2026 systematic review of 185,107 gymnasts found 53%
pooled wrist pain prevalence, with decreased shoulder ROM identified as a
risk factor alongside training intensity/volume — a real gap since the
gymnast-aerialist archetype already emphasizes "shoulder/wrist resilience"
in the product catalog but the methodology never actually addressed wrist
injury. (2) Dance-specific RED-S (Relative Energy Deficiency in Sport)
research: one study found 65% of vocational ballet students at risk of
RED-S, with concrete macronutrient/energy-floor targets available.

**Action:** Added a Wrist row to the §4 injury table (methodology + persona)
tied to the shoulder-ROM link, and a new §6 "Nutrition & Energy Availability"
section with baseline macro targets and RED-S watch-for signs, boundaried
the same way as the injury-referral rule. Both cited, both incremental.

**Follow-up not done today (scope discipline):** `archetypes.ts`'s
gymnast-aerialist prehab focus is still `["hip", "ankle"]` — doesn't yet
include `"wrist"` as a formal injury flag in `programSchema.ts`, so the
program generator can't auto-insert wrist prehab yet even though the
methodology now covers it. Worth a small follow-up PR to add `"wrist"` to
the injury-flag enum and a corrective exercise mapping, separate from this
research pass.

## 2026-08-08 — baseline

**Checked:** Initial methodology build. Full source list as of this date is
in `docs/methodology/XOLOKAN_METHODOLOGY.md`'s Sources section (14 cited
studies across periodization, ACSM 2026 guidelines, dance injury prevention,
plyometric dosage, and RAMP warm-up protocol).

**Found:** N/A — baseline entry. Future entries log incremental findings
only, not the full source list.

**Action:** Baseline established. Daily research pass begins from here.
