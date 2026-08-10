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
equipment access, injury history, **age range, and anatomical sex** and
produces a genuinely different 12-week program — deload weeks, corrective
exercises, equipment substitutions, age-specific recovery pacing, and
sex-specific injury countermeasures (ACL/landing-mechanics work and pelvic
floor guidance for female clients) all computed, not hand-edited. That's
the pitch: not "a PDF from a trainer," but "an AI coach running Oscar's own
method, factoring in who you actually are." Lead marketing copy with that
distinction, not with generic AI-coaching language — the specificity is
what a $47 template can't compete with.

**Sell the personalization dimension directly.** "Same 12-week arc,
programmed differently for a 22-year-old and a 38-year-old, for a man and
a woman" is a concrete, demonstrable claim competitors with a static PDF
can't make — worth a line in sales copy, not just an engineering detail.

## 6. Immediate next steps

1. ~~Build a PDF/print export of `GeneratedProgram`~~ — done for one
   archetype, see §7.
2. Set up recurring billing for the $75/$150/$200 ladder — Stripe
   subscriptions are the natural fit given all three tiers are monthly.
3. Write the sales page copy around the archetype catalog in §2 — each
   archetype is close to a landing-page section already.
4. Decide the exact trigger for "regenerates each block" at the $75/$150
   tiers — automatic on a 12-week timer, or on client request.
5. Generalize the PDF export (§7) to the Gymnast/Aerialist and
   General-Performer archetypes, and to full-gym equipment mode.

## 7. First sellable product: 30-Day Dancer Foundation

`scripts/dancer_30_day_pdf.py` renders a branded, print-ready 30-day PDF —
Phase 1 (Base Strength & Control) of the Dancer archetype. It pulls
exercises, sets, and reps **live from `generateProgram()`** at build time
(via `generateSampleCli.ts`) rather than duplicating that data as hardcoded
Python — so the PDF and the actual generator can never drift apart as
`archetypes.ts` evolves. Only coaching cues, RIR targets, and rest times
are authored in the script, keyed by exercise name, since the generator
doesn't produce those yet. 11 pages: cover, how-it-works (RIR, RAMP
warm-up, equipment, disclaimer), weekly rhythm, four workout day pages, a
30-day calendar/checklist, nutrition & recovery baseline, progress-check
day, and a next-steps upsell into the Personalized/Premium tiers.

**Two editions, one script:**
```bash
python3 scripts/dancer_30_day_pdf.py --equipment bodyweight-only [output_path]
python3 scripts/dancer_30_day_pdf.py --equipment full-gym [output_path]
```
The Gym Edition uses real loaded strength work (Front Squat, Weighted
Pull-Ups, Seated Overhead Press, Sled Push, Kettlebell Swings) instead of
the bodyweight substitutions — same method, same phase, same days, real
weights. This widens the addressable market for the self-guided tier
beyond bodyweight-only clients.

This is the natural entry point for the **self-guided ($75/mo) tier**: a
lower-commitment, broadly-marketable "start here" product ahead of the
full 12-week personalized program.

**Demographic default is an explicit product decision, not an accident.**
The generator now factors in age range and anatomical sex
(`packages/xolokan-agent/src/demographics.ts` — see the methodology's
§7), but this static PDF is one broad-market SKU, not the personalized
tier, so it needs one fixed profile: **female, 25–30**, chosen because
ballet/dance participation skews heavily female and that age band covers
the bulk of the professional/pre-professional market. This is set
explicitly in the script (`PRODUCT_AGE_RANGE` / `PRODUCT_SEX`), not left
as an implicit CLI default. A client going through the Personalized tier
gets their own actual age/sex from XOLOKAN, not this default. Revisit if
a male-specific or different-age edition becomes worth building as a
fourth SKU.

Building this surfaced real fixes applied upstream, not just to the PDF:
a bodyweight substitution bug in the generator (`Kettlebell Swings ->
Broad Jumps` was inheriting an unsafe 5x20 rep scheme), and a
font-encoding issue where several Unicode glyphs (check marks, bullets,
the "&#8805;" symbol) aren't in the base Helvetica encoding reportlab uses
and silently render as wrong characters. The script now fails loudly with
a clear error if it hits an exercise name with no authored cue, rather
than silently shipping a gap — caught immediately when the Gym Edition
was added (`Ankle Isometric Hold (single-leg calf raise)`'s exact archetype
name didn't match the cue lookup key). Lesson for any future PDF work in
this repo: stick to plain ASCII or em/en-dash entities in table cells, and
always audit with pdfplumber before calling a PDF done.

**Weekly improvement routine**: a scheduled Routine reviews this product
every week — syncing in anything from that week's methodology research
that should reach the PDF's cues or notes, catching drift against the live
generator, and re-running the full overflow + contamination audit before
anything ships. See `docs/business/PRODUCT_CHANGELOG.md` for the log.

---

## Sources

- [How to Sell Fitness Programs Online in 2026 — SamCart](https://www.samcart.com/blog/sell-fitness-programs-online)
- [How to Create a Signature Coaching Program That Explodes Your Biz — Paperbell](https://paperbell.com/blog/how-to-create-a-signature-coaching-program/)
- [Craft your signature coaching framework — CoachVox](https://coachvox.ai/signature-coaching-framework/)
- [Top TrueCoach Alternatives and Competitors for 2026](https://www.trainerize.com/blog/top-truecoach-alternatives/)
- [Everfit vs Trainerize vs TrueCoach: The Honest Review (2026)](https://blog.everfit.io/everfit-vs-trainerize-vs-truecoach)
