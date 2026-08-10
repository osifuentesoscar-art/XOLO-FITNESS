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
