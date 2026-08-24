# XOLO FITNESS / XOLOKAN — Roadmap

**Status: Living document.** A single, sequenced view across everything
already scoped in separate docs — the CEO hire, billing, brand rollout,
catalog expansion, and the future website/app/ecommerce project. This
doc doesn't repeat their reasoning, it sequences their action items into
one place so nothing agreed to in any one document gets lost or
duplicated. Update it as items move, don't let it drift stale — that's
the whole reason it's separate from any single planning doc.

A structured, checkable mirror of this file also lives in Airtable (see
the base linked from this repo's README) for anyone who'd rather work
from a tracker than a markdown file — same items, kept in sync.

---

## Now (active / no blockers)

- [ ] **Wire Stripe subscription status to XOLOKAN chat access** —
  `packages/storefront/SETUP.md`, `WEBSITE_APP_ECOMMERCE_PLAN.md` §3.1.
  The single highest-priority item on this whole roadmap: unblocks real
  paying subscribers on the *current* lightweight app, independent of
  the future separate project.
- [ ] **Set up Stripe Payment Links** for the three tiers —
  `packages/storefront/SETUP.md`. Blocks everything downstream in the
  business plan's launch sequence.
- [ ] **Screen and hire the CEO** — `CEO_HIRING_PLAN.md`. In progress;
  full role split, comp structure, and screening process already
  defined, not yet executed.
- [ ] **Instrument Claude API cost per active chat user** —
  `XOLOKAN_BUSINESS_PLAN.md` §4.2, §7. Currently an unmeasured, real
  cost line for the Personalized/Premium tiers.
- [ ] **Launch the content cadence** — `XOLOKAN_BUSINESS_PLAN.md` §5.4,
  §5.5. Doesn't depend on billing being live; can start immediately.
- [ ] **Daily/weekly methodology and catalog research passes** — already
  running (`docs/methodology/RESEARCH_LOG.md`,
  `docs/business/PRODUCT_CHANGELOG.md`), no action needed, listed here
  only so this roadmap reflects everything actually in motion.

## Next 90 days

- [ ] **CEO onboarding** (once hired) — `CEO_HIRING_PLAN.md` §6's 90-day
  plan: product onboarding, audience trust-transfer, first real client
  cohort under their direct delivery.
- [ ] **Revisit the business plan's financial scenarios with real data**
  — `XOLOKAN_BUSINESS_PLAN.md` §8's own 90-day checkpoint: replace churn
  and CAC assumptions with real numbers from the first cohort.
- [ ] **Decide the Artist Athlete positioning's reach** —
  `ARTIST_ATHLETE_BRAND.md` §6: confirm whether it extends naturally to
  the Performer Protocol archetype or needs its own framing, before
  leaning on it universally in customer-facing copy.
- [ ] **Small persona update for the Artist Athlete voice** —
  `ARTIST_ATHLETE_BRAND.md` §5: encode the positioning explicitly into
  `persona.ts`'s VOICE section, once confirmed above.
- [ ] **Research pass: Figure Skating Protocol** — `FUTURE_PROGRAMS.md`
  #2, the lowest-lift catalog expansion candidate. Good first test of the
  "4th archetype" process before committing to a heavier build.

## 6-12 months (conditional on subscriber growth per the business plan)

- [ ] **First operational hire** (VA/content coordinator) —
  `XOLOKAN_BUSINESS_PLAN.md` §6, Phase 2 — once the CEO's content/DM
  volume alone justifies it.
- [ ] **Build the Stunt & Action Performer Protocol** —
  `FUTURE_PROGRAMS.md` #1, pending its own dedicated injury-prevention
  research pass first (fall mechanics, martial-arts cross-training data).
- [ ] **Stripe Billing Portal + real account/database layer** —
  `WEBSITE_APP_ECOMMERCE_PLAN.md` §3.2-3.4 — needed before self-serve
  tier changes and program-history continuity are possible; still
  reasonable to build inside the current lightweight app, doesn't yet
  require the separate project.
- [ ] **Cheerleading / Competitive Acro Protocol** —
  `FUTURE_PROGRAMS.md` #3, once the 4th-archetype process is validated by
  Figure Skating or Stunt & Action.

## 12+ months (the separate project, and beyond)

- [ ] **Scope and begin the standalone website/app/ecommerce project** —
  `WEBSITE_APP_ECOMMERCE_PLAN.md` in full, once subscriber volume and
  revenue justify the investment (per `XOLOKAN_BUSINESS_PLAN.md` §4.3's
  Base/Optimistic scenarios) — Option A (separate repo, this repo as a
  backend dependency) is the recommended shape.
- [ ] **Multi-coach studio phase** — `XOLOKAN_BUSINESS_PLAN.md` §6, Phase
  3 — the Method as shared, documented IP other coaches deliver through,
  not just the founding CEO.
- [ ] **Musical Theatre / Touring Performer split** —
  `FUTURE_PROGRAMS.md` #4 — a refinement of the existing Performer
  Protocol, lower priority than a genuinely new audience.
- [ ] **Youth / Pre-Professional track** — `FUTURE_PROGRAMS.md` #5 —
  explicitly flagged as needing its own dedicated research pass
  (growth-plate/skeletal-maturity science, consent/communication norms
  with minors), not a simple age-bracket extension. The highest-lift item
  on the entire roadmap; don't start this without treating it as its own
  project.

---

## How to keep this current

- When an item completes, check it off here and in the Airtable mirror —
  don't just note it in the source doc and forget to update this file.
- When a new commitment gets made in any planning doc (business plan,
  hiring plan, future programs, ecommerce plan), add it here in the right
  horizon — this file's whole value is being the one place that reflects
  everything in motion, not a subset.
- Re-sequence horizons as reality changes (e.g., if subscriber growth
  outpaces the Base scenario, "12+ months" items may move up) — this is
  a living document, not a fixed plan.
