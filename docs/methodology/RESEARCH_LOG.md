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
