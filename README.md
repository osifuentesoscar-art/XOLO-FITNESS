# XOLO FITNESS

A standalone project — separate from any other client/brand work — for **XOLO
FITNESS**, a performance-coaching brand founded by **Oscar "Xolo" Sifuentes
Jr**. This repo houses **XOLOKAN**, an AI performance-coach agent built on the
Claude Agent SDK, plus a minimal server + web chat UI to talk to it.

## Brand background (researched, not assumed)

- **Founder**: Oscar "Xolo" Sifuentes Jr — performance coach and movement
  specialist, 10+ years in athletic performance, physical education, and
  professional performance arts (dance/choreography/movement direction for
  touring artists including Pharrell Williams, Travis Scott, Mariah Angeliq,
  Ali Gatie).
- **Founded**: 2021, as XOLO FITNESS LLC.
- **Mission**: impact and improve every client's daily quality of life
  through a nutritious, health-conscious approach that treats mental and
  physical strength as equally important. Programs span beginner to
  professional-athlete level.
- **Methodology**: strength development + advanced calisthenics + athletic
  conditioning + recovery science + breathwork.
- **Audience**: artists, dancers, performers, athletes, and high-performing
  professionals whose lifestyles demand strength, endurance, agility, and
  resilience.
- **Channels**: [xolofit.com](https://www.xolofit.com) ·
  [Instagram @xolo.fitness](https://www.instagram.com/xolo.fitness) ·
  [YouTube](https://www.youtube.com/channel/UCbmfaWCzDVGMrZmXcCagh5w) ·
  founder's personal Instagram [@oscarxsifuentes](https://www.instagram.com/oscarxsifuentes)
- **Brand assets**: logos and video content live in the team Dropbox under
  `XOLO FITNESS BRAND` and `LOGOS` — mostly promo/recovery/workout video, no
  written brand voice doc existed yet, so the persona below was synthesized
  from the mission/methodology copy on xolofit.com and the coaches page.

Note: direct fetches to `xolofit.com`, Instagram, and YouTube were blocked by
this environment's network egress proxy, so the above is assembled from
indexed search results, not a live crawl. Worth re-verifying against the live
site/socials when you have unrestricted access.

## What's here

```
packages/
  xolokan-agent/   XOLOKAN persona, program generator, Claude Agent SDK chat loop
  server/          Express API wrapping the agent for the web UI
  web/             Minimal static chat UI
  storefront/      Sales landing page + pricing (packages/storefront/SETUP.md)
scripts/
  generate_program_pdf.py   Sellable PDF generator, any archetype/scope/equipment
docs/methodology/
  XOLOKAN_METHODOLOGY.md   Training-science layer XOLOKAN's persona is built on
  sources/                 Source documents the methodology is built from
docs/business/
  XOLOKAN_PRODUCT_SYSTEM.md   How the methodology turns into sellable programs
  XOLOKAN_BUSINESS_PLAN.md    Market, financial scenarios, marketing, and scaling plan
  PRODUCT_CHANGELOG.md        Weekly log of changes to the sellable catalog
```

## Training methodology

XOLOKAN's programming is built on a Soviet-block periodization system (base
strength -> power/volume -> peak, 12-week cycles), layered with
calisthenics-based relative-strength training and dance/artist-athlete
injury-prevention science (ankle, knee, lower back, and hip protocols;
mandatory single-leg work; isometric control training; RPE/RIR effort
landmarks; RAMP warm-up protocol; plyometric dosage by experience level).
Full detail, including cited research, is in
[`docs/methodology/XOLOKAN_METHODOLOGY.md`](docs/methodology/XOLOKAN_METHODOLOGY.md).
The source training documents it was built from are in
`docs/methodology/sources/`.

## Program generator — turning the methodology into a system

The methodology isn't just a reference doc XOLOKAN improvises from — it's
implemented as a deterministic generator in `packages/xolokan-agent/src/`:

- `programSchema.ts` / `archetypes.ts` — three sellable program archetypes
  (Dancer, Gymnast/Aerialist, General Performer), each a tailored version of
  the weekly split with its own injury-prehab emphasis.
- `generateProgram.ts` — pure function: client intake (discipline,
  experience, sessions/week, equipment access, injury history) in, a full
  structured 12-week program out. No API key needed — try it directly:
  ```bash
  npm run generate:sample --workspace=packages/xolokan-agent -- \
    --name "Test Client" --discipline dancer --days 4 \
    --equipment bodyweight-only --injuries ankle
  ```
- `tools.ts` — wraps the generator as a tool XOLOKAN calls mid-conversation
  when asked to actually build a program, rather than hand-writing one.

See [`docs/business/XOLOKAN_PRODUCT_SYSTEM.md`](docs/business/XOLOKAN_PRODUCT_SYSTEM.md)
for how this catalog maps to pricing tiers and delivery — the business layer
on top of the training science.

## Setup

```bash
npm install
cp .env.example .env   # add your ANTHROPIC_API_KEY
```

**Chat with XOLOKAN in the terminal:**
```bash
npm run chat
```

**Run the web chat UI:**
```bash
npm run dev:server
# open http://localhost:8787
```

## XOLOKAN persona

Defined in `packages/xolokan-agent/src/persona.ts`. It encodes the brand
mission, the training methodology above, target audience, and voice (direct,
disciplined, coach-energy — distinct from a clinical or luxury tone). Edit
that file to tune the agent as the brand voice solidifies.

## Status

Training methodology, the archetype catalog, and pricing ($75 / $150 / $200
monthly virtual subscription tiers) are all **reviewed and approved** by
Oscar (see the Status lines in `docs/methodology/XOLOKAN_METHODOLOGY.md` and
`docs/business/XOLOKAN_PRODUCT_SYSTEM.md`). The app itself is still an early
scaffold, not yet deployed.

**Full sellable catalog exists.** `scripts/generate_program_pdf.py`
generates a branded, print-ready PDF for any of the 3 archetypes, in a
30-day (Phase 1 entry product) or 12-week (complete Method) scope, in a
bodyweight-only or full-gym edition — 12 distinct PDFs from one script,
pulled live from `generateProgram()` so none of them can drift from the
generator. A landing page with pricing lives in
`packages/storefront/index.html` (Stripe Payment Links needed to go live —
see `packages/storefront/SETUP.md`). Full detail in
`docs/business/XOLOKAN_PRODUCT_SYSTEM.md` §7-8. A weekly Routine keeps the
catalog current — see `docs/business/PRODUCT_CHANGELOG.md`.

**Business plan exists.** `docs/business/XOLOKAN_BUSINESS_PLAN.md` covers
market sizing, competitive landscape, financial scenarios (unit
economics, revenue projections — modeled from industry benchmarks, not
yet real transaction data), the marketing/customer-acquisition plan, and
a three-phase scaling path past Oscar's own hours. Its own next-steps
list (§9) is the current source of truth for what's blocking launch —
recurring billing is still the first blocker.

Open next steps: pull in the real brand voice/style guide once written,
set up recurring billing for the three tiers (blocks everything else in
the business plan), and decide on a hosting target for the server + web
UI.
