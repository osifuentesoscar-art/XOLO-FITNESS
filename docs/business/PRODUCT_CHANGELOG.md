# XOLOKAN Catalog — Product Changelog

Weekly log for `scripts/generate_program_pdf.py` and
`packages/storefront/`, the sellable products. Distinct from
`docs/methodology/RESEARCH_LOG.md` (which tracks methodology research) —
this tracks changes to the actual sellable deliverables: content accuracy,
drift against the live generator, and audit results. Most recent entry on
top.

---

## 2026-08-11 — full catalog + storefront (user-requested)

**Changed:**
- Generalized `scripts/dancer_30_day_pdf.py` into
  `scripts/generate_program_pdf.py`, parameterized by `--archetype`,
  `--equipment`, and a new `--scope` (`30-day` | `12-week`). One script
  instead of one-per-archetype, still pulling live from `generateProgram()`.
- Added the **12-week scope**: the complete Method across all 3 phases (24
  pages — phase intros, all 4 workout days per phase, end-of-phase
  progress checks, a 12-week phase map instead of a day-by-day calendar).
  This is the actual product behind the $150/$200 personalized/premium
  tiers, not just the $75 entry product.
- Added cues for 10 new exercises (Ring Support Hold, Handstand Push-Ups,
  Pistol Squat Progression, Dips, L-Sit Progression, Farmer Carry, Wall
  Handstand Hold, Medicine Ball Slams, Dead Bug, Hip Airplane) to cover
  the Gymnast/Aerialist and General-Performer archetypes.
- Built `packages/storefront/index.html` — a landing page with the
  3-protocol catalog, the differentiator pitch, and $75/$150/$200
  Stripe-ready pricing tiers. `packages/storefront/SETUP.md` documents the
  three Payment Link placeholders and what's still not wired (subscription
  access to the personalized tier).

**Generated:** all 12 combinations (3 archetypes × 2 equipment × 2 scopes).
Zero cue-lookup failures on the first full run.

**Audit:** all 12 PDFs — 11 or 24 pages depending on scope, zero overflow,
zero glyph corruption, zero Brace Life/ICONS contamination.

## 2026-08-10 (later, 2) — demographic factors (age/sex) reach the PDF

**Changed:**
- The generator's new `ageRange`/`sex` intake fields (see
  `docs/methodology/RESEARCH_LOG.md`) surfaced immediately when
  regenerating: the CLI's new default (`female`) meant Day 3 gained a
  Banded Lateral Walk (ACL prehab) with no authored cue — the script's
  fail-loud check caught it before anything shipped. Added the cue.
- Set the PDF's demographic profile explicitly (`PRODUCT_AGE_RANGE`,
  `PRODUCT_SEX` constants — female, 25-30) instead of leaving it as an
  implicit CLI default, with the reasoning documented in the script and
  in `docs/business/XOLOKAN_PRODUCT_SYSTEM.md` §7.

**Audit:** Both editions regenerated — still 11 pages each, zero overflow,
zero glyph corruption, zero Brace Life/ICONS contamination. Spot-checked
the new Day 3 row renders correctly.

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
