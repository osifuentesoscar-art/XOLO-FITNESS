# Website, App & Ecommerce — Future Project Scope

**Status: Draft v1 — scoping for a future standalone project, not a build
plan for right now.** Oscar's stated intent: this eventually launches as
its own project (website + app + ecommerce), separate from the current
lightweight scaffold in this repo. This document exists so that when the
time comes, the decision points are already thought through instead of
being figured out from scratch. Sequencing against everything else lives
in [`ROADMAP.md`](ROADMAP.md).

---

## 1. What exists today vs. what "the separate project" actually means

**Today, in this repo:**
- `packages/xolokan-agent` — the actual product engine: persona, program
  generator, the science layer. This is IP, not UI.
- `packages/server` + `packages/web` — a minimal Express API + static
  chat UI. Functional, not a polished consumer product.
- `packages/storefront` — a single static landing page with pricing and
  placeholder Stripe Payment Links (`packages/storefront/SETUP.md`).
- No database, no accounts, no login. Nothing persists between sessions.

**"The separate project"** is the polished, consumer-facing surface built
on top of the engine above: a real marketing website, an actual app
experience for the Personalized/Premium tiers (not just a bare chat
window), and a real ecommerce/subscription flow with accounts. It's a
different kind of build — production UX, not a working prototype — which
is exactly why it's being scoped as its own project rather than an
incremental feature of what's here.

## 2. Relationship to this repo: two real options

**Option A — separate repo, this repo becomes a backend dependency.**
The website/app project is its own codebase (its own repo, its own
deploy). It calls into `packages/xolokan-agent`'s generator and agent
logic either as a published internal package or via an API this repo's
server exposes. Cleanest separation of concerns; the "engine" stays
independently versioned and testable, and a future multi-coach studio
(Phase 3, `XOLOKAN_BUSINESS_PLAN.md` §6) could reuse the same engine
behind a completely different frontend without touching it.

**Option B — new packages inside this monorepo.** The website/app
becomes `packages/site` and `packages/app` alongside what's already here,
sharing the existing npm workspace setup.

**Recommendation: Option A**, once there's an actual reason to build it
(real subscriber volume, per the roadmap) — the whole point of "eventually
launch as a separate project" in Oscar's own framing is separation, and a
monorepo makes that harder to unwind later, not easier. Keep building
methodology/catalog/agent work here in the meantime; that work is the
dependency the future project will consume, not something that needs to
move preemptively.

## 3. Ecommerce & account flow — what "real" means beyond Payment Links

The current plan (`XOLOKAN_PRODUCT_SYSTEM.md` §4, `SETUP.md`) is
deliberately minimal: Stripe Payment Links, no backend, good enough to
take a first payment. A real app needs more, in roughly this order of
necessity:

1. **Subscription status → access wiring** (already flagged as the
   single most important gap in `SETUP.md`): a Stripe webhook that fires
   on subscription created/updated/canceled, updates a stored record of
   who has access to what tier, and gates the chat/app experience on
   that record. This is the one piece worth building *before* the
   separate project exists at all — it's needed the moment there's a
   single real Personalized-tier subscriber, regardless of what UI sits
   in front of it.
2. **A real database.** Nothing here persists today. Minimum viable
   schema: users, subscriptions (tier, status, renewal date), and
   generated-program history (so a client's program isn't regenerated
   from scratch every session — continuity matters for a coaching
   relationship). A lightweight hosted Postgres (Render, which is already
   in this session's toolset, is a reasonable default) is enough at this
   scale — no need to over-engineer this before there's real usage to
   size against.
3. **Authentication.** Account creation/login for clients to access their
   program and chat history. A managed auth provider (rather than
   building this from scratch) is the right call at this scale — keeps
   the team's build effort on the actual product (the coaching
   experience), not on solved problems like password resets and session
   security.
4. **Stripe Billing Portal** (not just Payment Links) once tier
   upgrades/downgrades/cancellations need to be self-serve rather than
   "email us to change your plan" — not needed on day one, needed before
   this scales past a handful of manually-managed subscribers.
5. **The order-bump/upsell mechanics** already scoped in
   `XOLOKAN_PRODUCT_SYSTEM.md` §3 (nutrition guide, extra archetype,
   check-in call add-ons) — these convert meaningfully on digital fitness
   products specifically, worth building into checkout from the start of
   the real ecommerce flow rather than retrofitting later.

## 4. The app experience itself — beyond a bare chat window

The current `packages/web` is a functional but minimal chat UI. The
future app should surface what the chat interface currently hides:

- The actual generated program (exercises, sets/reps, phase, week) as a
  real, navigable view — not just prose XOLOKAN describes in chat.
- Progress tracking against the baseline log the PDFs already include
  (Day 1 baseline → 4/8-week retest) — this is already a designed part
  of the product, just not yet surfaced as a UI.
- Program history across blocks, so a returning client can see how their
  12-week arc evolved, not just their current state.
- Where the [Artist Athlete](../brand/ARTIST_ATHLETE_BRAND.md) brand
  positioning should show up visually, not just in copy — this is the
  primary surface a paying client actually lives in.

## 5. What NOT to build prematurely

Named explicitly so this doesn't become scope creep once building starts:

- **No native mobile app at launch.** A responsive web app covers the
  Personalized/Premium tiers' actual need (chat + program view); native
  apps are a real, separate investment worth revisiting only once web
  usage data justifies it.
- **No multi-coach/studio features** until Phase 3 of the business plan
  actually arrives (`XOLOKAN_BUSINESS_PLAN.md` §6) — building for a
  hypothetical future coach roster before there's a second coach is
  exactly the kind of premature complexity worth avoiding.
- **No custom-built auth, billing, or CMS** — every one of these has a
  mature, off-the-shelf solution at this company's scale; building any of
  them from scratch is time spent on solved problems instead of the
  actual product.

## 6. Sequencing

Full milestone sequencing lives in [`ROADMAP.md`](ROADMAP.md). In brief:
the subscription-access wiring (§3, item 1) is worth doing now,
independent of everything else here — it unblocks real subscribers on
the *current* lightweight app. Everything else in this document is real
work for when the business has validated demand and revenue to justify
the separate-project investment, not a queue to start immediately.
