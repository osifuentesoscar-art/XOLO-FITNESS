# 30-Day Dancer Foundation — Product Changelog

Weekly log for `scripts/dancer_30_day_pdf.py`, the first sellable product.
Distinct from `docs/methodology/RESEARCH_LOG.md` (which tracks methodology
research) — this tracks changes to the actual sellable deliverable: content
accuracy, drift against the live generator, and audit results. Most recent
entry on top.

---

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
