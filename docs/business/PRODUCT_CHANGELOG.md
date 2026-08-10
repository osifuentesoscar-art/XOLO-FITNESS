# 30-Day Dancer Foundation — Product Changelog

Weekly log for `scripts/dancer_30_day_pdf.py`, the first sellable product.
Distinct from `docs/methodology/RESEARCH_LOG.md` (which tracks methodology
research) — this tracks changes to the actual sellable deliverable: content
accuracy, drift against the live generator, and audit results. Most recent
entry on top.

---

## 2026-08-10 (later) — synced injury-prevention and hypertrophy research into the PDF

**Note:** this is the first scheduled firing of the weekly Routine, landing
the same day it was created (next Monday 18:00 UTC after setup) rather
than a week later — so "this week" below covers everything since the
product changelog began, not a full week.

**Reviewed:** RESEARCH_LOG.md entries since the last product changelog
entry — 2026-08-10 (dance injury prevention deep dive, deferred by that
entry's own "next week" note) and 2026-08-11 (block periodization lineage
+ load-independent hypertrophy).

**Changed:**
- Added a "Why strength-first works" paragraph to the How This Works page
  (both editions), citing the Houston Ballet RCT's 82% injury-rate
  reduction — gives the program's strength-first approach a concrete,
  credible reason instead of asserting it.
- Added a "history of ankle sprains?" note to the Day 3 outro (both
  editions): sprain recurrence is driven by balance/proprioception, not
  just strength, so it points clients to add single-leg balance work
  rather than assuming the existing Ankle Isometric Hold covers it.
- Added a bodyweight-specific reassurance paragraph (Bodyweight Edition
  only) citing the load-independent hypertrophy research — addresses the
  natural customer question "does bodyweight-only actually build muscle?"
  directly instead of leaving it unaddressed.

**Not changed:** Issurin's block terminology (Accumulation/Transmutation/
Realization) stays in the methodology/persona only — customer-facing copy
doesn't need that level of periodization jargon, the existing "Phase 1 of
the XOLOKAN Method" framing is the right altitude for a sold product.

**Drift check:** Both editions regenerated clean, no CUES lookup failures
— `archetypes.ts` hasn't changed since last week.

**Audit:** Both editions — 11 pages each, zero overflow, zero glyph
corruption, zero Brace Life/ICONS contamination. Spot-checked the new
paragraphs render correctly on the How This Works and Day 3 pages.

## 2026-08-10 — Gym Edition + live-data refactor

**Changed:**
- Refactored the script to pull exercises/sets/reps live from
  `generateProgram()` (via `generateSampleCli.ts`) instead of hardcoded
  Python tuples that duplicated `archetypes.ts`. The PDF can no longer
  drift from the generator silently.
- Added `--equipment full-gym` as a second edition alongside the existing
  bodyweight-only edition — real loaded strength work (Front Squat,
  Weighted Pull-Ups, Seated Overhead Press, Sled Push, Kettlebell Swings)
  instead of bodyweight substitutions.
- Added a hard failure (not a silent gap) if any exercise from the live
  generator data has no authored coaching cue — caught one real mismatch
  immediately (`Ankle Isometric Hold (single-leg calf raise)` naming).

**Audit:** Both editions — 11 pages each, zero overflow, zero glyph
corruption, zero Brace Life/ICONS contamination. Full pdfplumber
page-by-page check on both.

**Next week:** check whether that week's `RESEARCH_LOG.md` entries changed
anything the day pages, warm-up section, or nutrition page should reflect.
