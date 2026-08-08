# XOLOKAN Product System

**Status: Approved — methodology, archetype catalog, and pricing.** Pricing
below is Oscar's actual confirmed virtual subscription pricing, not a market
benchmark. See §6 for what's still outstanding.

How the training methodology in `docs/methodology/XOLOKAN_METHODOLOGY.md`
turns into programs Oscar can actually sell — repeatably, not as one-off
custom work each time. This is a business document, not training science;
it's sourced from market research on how fitness coaches productize and
price digital programs, current as of the research date below.

---

## 1. Name the method

A named, proprietary system is what separates "Oscar writes you a program"
from a sellable product — it converts coaching know-how into intellectual
property a client can recognize, compare, and pay a premium for, and it's
what lets the business scale past Oscar's own hours. Coaches with a named
signature framework command higher fees precisely because the client knows
what they're buying before the first session.

**Working name: the XOLOKAN Method.** Keep it consistent everywhere —
website, program covers, the AI agent's own introduction of itself — so the
brand and the training system reinforce each other instead of competing for
attention.

## 2. The catalog: three sellable archetypes

The methodology isn't sold as one generic program — it's three, each built
for a distinct, clearly-nameable client (this specificity is itself a sales
asset: "a program for you" outsells "a program for anyone"). These map
directly to `packages/xolokan-agent/src/archetypes.ts`, so the catalog and
the code that generates it never drift apart:

| Archetype | Who it's for | What's tailored |
|---|---|---|
| **XOLOKAN Dancer Protocol** | Professional / pre-professional dancers, choreographers | Ankle resilience for jump-heavy repertoire, hip stability for held positions, isometric control for line quality |
| **XOLOKAN Gymnast / Aerialist Protocol** | Gymnasts, aerialists, circus performers, acrobats | Strength-to-bodyweight ratio, shoulder/wrist resilience, grip and hold capacity |
| **XOLOKAN Performer Protocol** | Actors, musicians, high-performing professionals | Balanced general resilience, work capacity for demanding rehearsal/travel schedules |

Each archetype is a full 12-week block-periodized program (base → power →
peak, per the methodology) with its own default injury-prehab emphasis.
Adding a fourth archetype later is a data change in `archetypes.ts`, not a
rewrite — that's the point of building it as a system instead of a
one-off document.

## 3. Delivery tiers and pricing

All three tiers are **virtual/remote** subscriptions at Oscar's confirmed
pricing — not one-time purchases, and not the market-benchmark ranges a
generic pricing study would suggest. The training content doesn't change
per tier; the delivery format and personalization depth does:

| Tier | What they get | Delivery | Price |
|---|---|---|---|
| **Self-guided** | One archetype's full 12-week program, regenerated at each block transition | Static export of `generateProgram()` output, refreshed monthly | **$75/mo** |
| **XOLOKAN-personalized** | Same program, generated live from real intake (discipline, equipment, injury history) via the chat agent, editable, regenerates each block | The XOLOKAN web/chat app, `generate_program` tool | **$150/mo** |
| **Premium / hybrid** | Personalized program plus check-ins, form feedback, and direct virtual access to Oscar layered on top | Virtual coaching relationship, program as the backbone | **$200/mo** |

This is a tight ladder ($75 → $150 → $200) rather than the wide bands a
generic digital-product pricing study would suggest — appropriate for a
single virtual-coaching funnel where the jump between tiers is about
access to Oscar, not a jump from "cheap template" to "full 1:1 coaching."
If an in-person or higher-touch premium offering gets added later, it's a
fourth tier above $200, not a replacement for this ladder.

Two mechanics worth building in regardless of tier, because they measurably
lift revenue on digital fitness products specifically: a one-click upsell
at checkout (order bumps — a nutrition guide, an extra archetype, a
check-in call — convert 30–40% on fitness products), and tiered pricing
itself, so a client self-selects by budget rather than bouncing.

## 4. Where this actually lives

- **Self-guided tier**: a lightweight recurring-billing checkout (Stripe on
  a landing page, or a membership plugin) delivering a regenerated static
  program each month — no client-management features needed at this tier.
- **XOLOKAN-personalized tier**: the web chat app already being built in
  this repo (`packages/server`, `packages/web`) *is* this tier's delivery
  mechanism — it's the product, not just a support tool.
- **Premium/hybrid tier**: a coaching platform (TrueCoach is the cheaper,
  simpler option for 1:1 delivery; Trainerize if this grows into a
  multi-coach studio) layers messaging, check-ins, and progress tracking on
  top of the program XOLOKAN generates.

## 5. The differentiator to lead with

Most sellable fitness programs are static PDFs — the entire market of
"pre-made workout plans" is priced low precisely because they're generic
and can't adapt. XOLOKAN's actual moat is that the personalized tier isn't
static: it's a real generator (`generateProgram()` in
`packages/xolokan-agent/src/`) that takes a client's discipline, experience,
equipment access, and injury history and produces a genuinely different
12-week program — deload weeks, corrective exercises, and equipment
substitutions all computed, not hand-edited. That's the pitch: not "a PDF
from a trainer," but "an AI coach running Oscar's own method." Lead
marketing copy with that distinction, not with generic AI-coaching
language — the specificity is what a $47 template can't compete with.

## 6. Immediate next steps

1. Build a PDF/print export of `GeneratedProgram` (the ICONS project in
   this account already has a proven pattern for this — a template engine
   that takes a structured data object and renders a branded document) so
   the self-guided tier has an actual deliverable, not just JSON.
2. Set up recurring billing for the $75/$150/$200 ladder — Stripe
   subscriptions are the natural fit given all three tiers are monthly.
3. Write the sales page copy around the archetype catalog in §2 — each
   archetype is close to a landing-page section already.
4. Decide the exact trigger for "regenerates each block" at the $75/$150
   tiers — automatic on a 12-week timer, or on client request.

---

## Sources

- [How to Sell Fitness Programs Online in 2026 — SamCart](https://www.samcart.com/blog/sell-fitness-programs-online)
- [How to Create a Signature Coaching Program That Explodes Your Biz — Paperbell](https://paperbell.com/blog/how-to-create-a-signature-coaching-program/)
- [Craft your signature coaching framework — CoachVox](https://coachvox.ai/signature-coaching-framework/)
- [Top TrueCoach Alternatives and Competitors for 2026](https://www.trainerize.com/blog/top-truecoach-alternatives/)
- [Everfit vs Trainerize vs TrueCoach: The Honest Review (2026)](https://blog.everfit.io/everfit-vs-trainerize-vs-truecoach)
