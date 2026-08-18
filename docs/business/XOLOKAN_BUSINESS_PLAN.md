# XOLO FITNESS / XOLOKAN — Business Plan

**Status: Draft v1 — internal operating plan, not investor-facing.** Written
for Oscar to run the business by: goals, financial scenarios, marketing
plan, and a scaling path. Companion to
[`XOLOKAN_PRODUCT_SYSTEM.md`](XOLOKAN_PRODUCT_SYSTEM.md) (what's built and
how it's priced) and [`PRODUCT_CHANGELOG.md`](PRODUCT_CHANGELOG.md) (weekly
catalog maintenance log) — this document doesn't repeat the catalog, pricing
ladder, or storefront detail already covered there; it covers everything
around them: market, money, marketing, and how the business scales past
Oscar's own hours.

Every market figure below is cited to its source, current as of the
research date. Every financial figure is a modeled scenario, not a
forecast from real transaction data — **XOLO FITNESS has not taken a live
payment yet** (the storefront's Stripe Payment Links are still
placeholders, see `packages/storefront/SETUP.md`). Treat the numbers here
as the starting assumptions to replace with real data the moment the first
cohort of subscribers exists — that swap is listed explicitly in §9.

---

## 1. Executive summary

XOLO FITNESS sells a named training system — the XOLOKAN Method — as a
tiered virtual subscription ($75 / $150 / $200 per month) to dancers,
gymnasts/aerialists, and performers. The product is built and functioning
today: three program archetypes, a working AI program generator
(`generateProgram()`) that personalizes by discipline, equipment, injury
history, age, and anatomical sex, a full 12-PDF sellable catalog, and a
storefront landing page. What's not yet live is the business around the
product: payment collection, a marketing engine, and a plan for what
happens when Oscar's personal coaching time is the bottleneck.

This document is that plan. Three things it establishes:

1. **The market is real and growing**, but the addressable niche (dancers,
   gymnasts, aerialists specifically) is small and underserved by
   anything discipline-specific — that's the opening, not a mass-market
   play (§2, §3).
2. **The unit economics have to work on personalization, not volume.**
   XOLOKAN's moat is depth per client, not the lowest price in the
   category — the financial model in §4 is built around that.
3. **Scaling past Oscar's own hours is a real constraint that needs a plan
   now**, not after it becomes a bottleneck — §7 lays out three phases,
   the last of which turns the AI system into the tool other coaches use,
   not just Oscar.

---

## 2. Market opportunity

### Overall market: large and growing, but that's not who XOLOKAN sells to

The online/virtual fitness market broadly is valued around **$30-36
billion** as of 2026 and growing at a roughly **25-27% CAGR**, with
subscription models now accounting for **more than 60%** of total market
usage — the subscription-first structure XOLO FITNESS is already built
around is the way this market is moving, not against the grain.

That figure is not XOLO FITNESS's real addressable market, though — it's
the size of "online fitness" broadly (generic workout apps, gym-adjacent
content, mass-market coaching). XOLOKAN doesn't compete there and
shouldn't try to; a $75-200/month discipline-specific product isn't
positioned to win a race to the bottom against $10/month apps.

### The actual niche: small, specific, and underserved

- The U.S. had an estimated **135,000 professional dancers** as of 2023
  (60% working freelance — a population that is, by definition, without
  an employer-provided training staff and paying for their own
  conditioning). A narrower estimate (BLS-style formal employment counts)
  puts salaried dancer/choreographer roles closer to 13,900, with roughly
  3,000 new job openings/year — the gap between those two numbers is
  exactly the freelance, self-funded population this product targets.
- The U.S. gymnastics classes market alone is **~$960 million** (2025),
  growing at an 8.5% CAGR (2020-2025) — that's participants and their
  families, a different (younger, often parent-paying) buyer than the
  Gymnast/Aerialist Protocol's primary target, but it's evidence the
  category supports real spend.
- **89% of fitness enthusiasts now discover their personal trainers
  through social media** — validates the Instagram-first acquisition
  strategy in §6 as the right channel, not a fallback.

**Practical read:** this is a five-to-six-figure-subscriber ceiling
market, not a millions-of-users one. That's a feature for a $75-200/month
personalized product, not a bug — the business plan here is built to be
profitable and sustainable at hundreds to low thousands of subscribers,
not to chase venture-scale user counts.

### Competitive landscape

No direct competitor combines discipline-specific programming (dancer/
gymnast/aerialist, not "athletes" generically) with AI-driven
personalization by age, anatomical sex, and injury history at this price
point. What exists instead:

| Category | Examples | Gap vs. XOLOKAN |
|---|---|---|
| Dance-specific coaching platforms | Dancer Fitness Courses, Elevate (Dance Performance Training), Veyette Virtual Ballet School | Skill/technique-focused (turns, flexibility, competition prep), not strength & conditioning built on periodization science; static or live-coached, not AI-personalized |
| General coaching delivery platforms | TrueCoach, Trainerize | Infrastructure, not content — a coach still has to write every program by hand; XOLOKAN *is* the content engine, these are the delivery rails a competitor coach would need to build on top of |
| Generic fitness apps/subscriptions | The broad $30B+ market above | No discipline specificity, no injury-prevention science layer, no age/sex-factored programming — closer to a workout library than a coaching system |
| Dance-specific fitness certifications | ASFA Dance Fitness, ACE | Sell instructor credentials, not client-facing programs — different buyer entirely |

**The honest gap in XOLOKAN's own positioning right now**: none of the
above compete on personalization depth, but none of them need to yet
either — XOLO FITNESS has no live customers, reviews, or case studies to
point to. Early marketing (§6) has to lead with the demonstrable mechanism
(watch the program change live for a 22-year-old vs. a 38-year-old, a
different injury history) rather than claimed superiority, because
claimed superiority isn't earned until there's a track record.

---

## 3. Product & pricing (summary — full detail in the product system doc)

Already built, reviewed, and approved — not re-litigated here:

- **Three archetypes**: Dancer, Gymnast/Aerialist, Performer Protocol.
- **Three tiers**: Self-Guided ($75/mo), XOLOKAN-Personalized ($150/mo),
  Premium/Hybrid ($200/mo) — see
  [`XOLOKAN_PRODUCT_SYSTEM.md`](XOLOKAN_PRODUCT_SYSTEM.md) §3 for exactly
  what each tier includes.
- **12-PDF sellable catalog** (3 archetypes × 2 equipment modes × 2
  scopes), live-generated from the same code that drives the personalized
  tier — audited weekly, see `PRODUCT_CHANGELOG.md`.
- **Storefront**: `packages/storefront/index.html`, pricing live, Stripe
  Payment Links still placeholders (§9, action item #1).

---

## 4. Financial model

**Read this section as scenario planning, not a forecast.** Every
assumption below is either an industry benchmark (cited) or an explicit
placeholder Oscar should override with real numbers once the business has
even one month of live data. The goal is a usable framework for deciding
"is this working," not a number to hit.

### 4.1 Unit economics assumptions

| Metric | Assumption | Source / reasoning |
|---|---|---|
| Customer acquisition cost (CAC) | $100-150 per subscriber (base case) | Subscription fitness CAC benchmarks run $100-300 depending on channel; organic-first Instagram strategy (§6) should sit toward the low end before any paid spend starts |
| Monthly churn | 8% (base case) — range 5% (optimistic, top-quartile) to 12% (conservative, category median) | Fitness app median monthly churn is 10-13%, top-quartile apps hold 4-6%; a coached/personalized relationship (not a passive app) should outperform the median, but this is unproven until measured |
| Average subscriber lifetime | ~12.5 months at 8% monthly churn (1 ÷ churn rate) | Direct math from the churn assumption above — reforecast the moment real cohort data exists |
| LTV target ratio | ≥3:1 LTV:CAC | Standard SaaS/subscription health benchmark; below 3:1 the business is spending more to acquire a customer than that customer is worth |
| CAC payback period | Target under 12 months | Standard subscription benchmark; at $100-150 CAC and $75-200/mo pricing, this is achievable even at the low tier within 1-2 months of gross revenue, well before churn assumptions matter |
| Order bump / upsell conversion | 30-40% | Already cited in `XOLOKAN_PRODUCT_SYSTEM.md` §3 — a nutrition guide, second archetype, or check-in call add-on at checkout |

**LTV math at the base-case assumptions**, by tier (before subtracting
CAC or variable costs):

| Tier | Price/mo | Est. lifetime (12.5 mo) | Gross LTV |
|---|---|---|---|
| Self-Guided | $75 | 12.5 mo | ~$938 |
| Personalized | $150 | 12.5 mo | ~$1,875 |
| Premium | $200 | 12.5 mo | ~$2,500 |

Against a $100-150 CAC, every tier clears the 3:1 LTV:CAC bar comfortably
at these assumptions — **the real risk isn't unit economics on paper, it's
whether churn actually lands near 8% instead of 12%+** once real
subscribers exist. Watch churn as the single most important number in the
first 90 days of live billing, not signups.

### 4.2 Cost structure

| Cost | Type | Notes |
|---|---|---|
| Stripe processing fees | Variable, ~2.9% + $0.30/transaction | Standard Payment Links pricing; no custom backend needed (§9) |
| Claude API usage (XOLOKAN chat, Personalized/Premium tiers) | Variable, scales with active chat usage | **Not yet measured** — this is a real per-user cost the personalized tiers depend on and it has never been benchmarked against actual usage. Action item: instrument and log token usage per conversation once the chat app has real users, so cost-per-active-subscriber is known within the first month, not assumed. |
| Hosting (`packages/server`, `packages/web`) | Fixed, low | Render or equivalent — sub-$50/mo at this scale |
| Marketing spend | Discretionary | $0 required to start (§6 is organic-first); budget for paid amplification only once the organic funnel is proven to convert |
| Oscar's time | Opportunity cost, not cash | The real constraint in Phase 1 (§7) — priced implicitly by how many Premium/hybrid clients one person can actually serve well |
| Contractor coaches (Phase 2+) | Variable, future | See §7 — not a Phase 1 cost |

### 4.3 Revenue scenarios (Year 1, illustrative)

Three subscriber-count scenarios by month 12, assuming a tier mix skewed
toward the entry and mid tier (typical for a 3-tier ladder where the
middle tier is marketed as "most personalized" — matches the storefront's
existing "Most Personalized" badge on the $150 tier):

| Scenario | Self-Guided ($75) | Personalized ($150) | Premium ($200) | Total subscribers | Monthly recurring revenue (MRR) at month 12 |
|---|---|---|---|---|---|
| Conservative | 15 | 10 | 3 | 28 | $3,225/mo |
| Base | 35 | 25 | 8 | 68 | $6,925/mo |
| Optimistic | 70 | 50 | 18 | 138 | $14,850/mo |

These are **month-12 snapshots on a ramp, not day-1 numbers** — realistic
early-stage growth for an organic, Instagram-first launch (§6) is closer
to single digits in month 1-2, building through content compounding and
word-of-mouth in a tight-knit dance/performer community (a community where
reputation travels fast — both the upside and the risk of that is worth
naming explicitly). Rebuild this table with real signup data after month 3
— three data points is enough to tell if the ramp is tracking conservative,
base, or optimistic.

**What "success" looks like in dollar terms at each scenario**: the
Conservative case (~$39K annualized run rate at month 12) validates the
model and funds itself; the Base case (~$83K annualized) is a real
part-to-full-time income; the Optimistic case (~$178K annualized) is where
Phase 2 hiring (§7) becomes necessary just to keep Premium-tier service
quality from degrading.

---

## 5. Marketing & customer acquisition plan

### 5.1 Why Instagram-first, not paid-first

89% of fitness enthusiasts now discover their personal trainers through
social media, and Oscar already has two active accounts
(**@xolo.fitness**, the brand, and **@oscarxsifuentes**, the founder) with
an existing audience and content history — this is a warm start, not a
cold one. Paid advertising is most effective once an organic funnel
already converts; running paid spend before that is proven wastes the
budget amplifying an unproven message. **Sequence: organic funnel first,
paid amplification second, once conversion is measured.**

### 5.2 The funnel

Content (Reels/posts) → Capture (comment-to-DM) → Qualify (DM script) →
Convert (discovery call or direct checkout) → Retain (program
upsells/tier upgrades). Coaches running this funnel with fast DM response
book measurably more conversions than slow manual replies — **a DM
response-time target (same-day, ideally same-hour) is a real operational
commitment**, not just a nice-to-have, especially before there's budget
for automation tooling.

### 5.3 Content strategy — lead with the mechanism, not claims

Given the competitive honesty in §2 (no case studies yet), the strongest
content isn't testimonial-based — it's **demonstrating the actual
personalization mechanism**, which is XOLOKAN's real, currently-unmatched
differentiator:

- **Screen-recording Reels**: show a program actually regenerating live
  for two different client profiles (a 24-year-old vs. a 37-year-old; a
  client with a shoulder flag vs. one without) — this is the single most
  concrete, unfakeable proof point XOLO FITNESS has, and no static-PDF
  competitor can replicate it on camera.
- **Educational carousels**: pull directly from
  `XOLOKAN_METHODOLOGY.md`'s cited science (ACL risk mechanisms, RED-S
  awareness, the strength-first injury-prevention RCT) — this content
  already exists as source material, it just needs a visual translation
  pass, not new research.
  **Do not name real clients or share identifiable injury/health
  information in this content without their explicit, specific consent
  for that post** — the methodology's own science is fair game, a real
  client's ACL flag is not, regardless of how compelling the story would
  be.
- **Founder-credibility content** (@oscarxsifuentes specifically): the
  performance/movement-direction background (touring artist work) is a
  legitimate trust signal already in the brand story. **Any reference to
  specific past collaborators or clients in marketing copy needs their
  explicit permission first** — don't use a name or likeness for
  promotional credibility without it, even if the association is true and
  the work is public knowledge.

### 5.4 Cadence and format (industry-benchmark starting point)

Start with a sustainable, real cadence rather than an aspirational one
that burns out in month two — 3-4 Reels/week, daily Stories, 1-2
educational carousels/week is a defensible starting rhythm for a solo
operator also delivering coaching. Revisit cadence once there's enough
data (4-6 weeks) to see what's actually converting, not before.

### 5.5 Launch sequence (first 90 days)

1. **Weeks 1-2**: Stripe Payment Links live (§9 #1), storefront fully
   functional, existing Instagram audience gets the first announcement —
   this converts the warmest possible audience (people already following)
   before spending any effort on new discovery.
2. **Weeks 3-6**: Content engine running at the cadence above, DM funnel
   live, no paid spend yet. Goal: first 10-15 subscribers from the
   existing audience + organic reach, and a working DM→conversion script
   refined from real conversations.
3. **Weeks 7-12**: Reassess churn and conversion data from the first
   cohort (§4.1's real-data swap). If the funnel is converting, consider a
   small paid-amplification test on the highest-performing organic
   content (not a new campaign from scratch) — that content already
   proved it resonates.

---

## 6. Operations & scaling plan

The real constraint isn't demand generation, it's **Oscar's own time**
once the Personalized and Premium tiers require direct involvement (chat
availability, check-ins, form feedback). Plan for that constraint now,
in three phases:

### Phase 1 — Solo + AI (0 to ~50 subscribers)

XOLOKAN handles the Self-Guided and Personalized tiers' actual program
generation and day-to-day chat entirely — that's the point of building it
as a system (§8 of the product doc). Oscar's time goes to: content
creation (§5), Premium-tier check-ins, and DM conversion. No hiring yet —
this phase should comfortably absorb the Conservative and most of the
Base revenue scenario (§4.3) on Oscar's time alone.

### Phase 2 — First hire (~50-150 subscribers)

Two candidate hires, in likely order:

1. **A part-time VA or content coordinator** — handles the DM funnel's
   first-response layer and content scheduling, freeing Oscar's time for
   the coaching work only he can do. This is the highest-leverage first
   hire because it protects the "fast DM response" commitment in §5.2 as
   volume grows past what one person can answer same-day.
2. **An assistant coach for Premium check-ins** — a certified trainer
   (per the IRS contractor-classification caution below) who runs
   check-ins/form-feedback under Oscar's system, not replacing his
   coaching but extending its reach. Bring this in when Premium-tier
   volume alone starts crowding out content/business-development time.

**Contractor classification matters here**: the IRS uses behavioral,
financial, and relationship criteria to determine employee vs.
independent-contractor status, and treating a contractor like an employee
(fixed hours, mandated tools, no autonomy in how the work gets done)
risks misclassification penalties. If Phase 2 hiring happens, structure
it deliberately as genuine contractor work (their own schedule, their own
client-interaction style within brand guardrails) or as a real
employee relationship — not an ambiguous middle that looks like
misclassification on paper. This is a real legal/financial risk worth a
short conversation with an accountant or employment attorney before the
first hire, not something to improvise.

### Phase 3 — Multi-coach studio (~150+ subscribers)

This is where XOLOKAN stops being "Oscar's tool" and becomes **the
system other coaches deliver through** — additional certified coaches,
each running their own client roster on the XOLOKAN Method (the named,
systematized IP from `XOLOKAN_PRODUCT_SYSTEM.md` §1 is exactly what makes
this possible: the method is documented and productized, not locked in
Oscar's head). At this scale, the coaching-platform layer already scoped
in the product system doc (Trainerize, for a multi-coach studio
specifically) becomes worth adopting instead of the current lightweight
web chat app. This phase is a genuine business-model shift — from
"Oscar's coaching business" to "a studio running Oscar's method" — and
deserves its own planning pass when subscriber count actually approaches
this range, not before.

---

## 7. Risks & assumptions to watch

Named plainly, not buried in the numbers above:

1. **Churn is unmeasured.** The entire financial model in §4 hinges on an
   8%-monthly-churn assumption that has never been tested against a real
   XOLO FITNESS cohort. This is the single most important number to watch
   once billing goes live.
2. **Claude API cost per active subscriber is unmeasured.** The
   Personalized/Premium tiers' actual gross margin depends on it and it's
   currently unknown — instrument this in month 1 (§4.2).
3. **The addressable market is genuinely small** (§2) — this caps how far
   the Optimistic scenario in §4.3 can realistically run without either
   expanding into adjacent disciplines (a real option — the archetype
   system in `archetypes.ts` is built to add a fourth archetype as a data
   change, not a rewrite) or accepting a lower ceiling than a generic
   fitness product would have.
4. **No case studies or reviews exist yet** — early marketing (§5.3) has
   to work harder because it can't lean on social proof. This resolves
   itself with the first real client results, but the first 90 days carry
   more of that burden than later months will.
5. **Reputation travels fast in a small, connected community** (dance/
   performer circles) — this cuts both ways: strong early results compound
   into referrals faster than in a generic market, but a bad experience
   does too. Weight client experience quality accordingly, especially in
   the Premium tier where Oscar's own name is directly attached.

---

## 8. Milestones — next 90 days

Concrete, checkable, and small — matching the "keep this lightweight"
posture of the rest of this repo's operating cadence:

- [ ] Stripe Payment Links live, storefront fully functional (§9 #1)
- [ ] First announcement to existing Instagram audience
- [ ] Content cadence running for 4+ consecutive weeks (§5.4)
- [ ] First 10 paying subscribers, any tier
- [ ] Claude API cost per active chat user measured and logged (§4.2,
      §7 #2)
- [ ] Real churn data from the first cohort's first full month — replace
      the 8% assumption in §4.1 with it
- [ ] Revisit this document's §4 revenue scenarios against real numbers

---

## 9. Immediate next steps

1. **Set up recurring billing** — still the single blocker on everything
   else in this plan. Create the three Stripe products and drop the
   Payment Link URLs into `packages/storefront/index.html` per
   `packages/storefront/SETUP.md`. Nothing else here can start until this
   is done.
2. **Wire Stripe subscription status to XOLOKAN chat access** — noted as
   outstanding in `SETUP.md`; becomes urgent the moment the Personalized/
   Premium tiers have paying subscribers who need actual access.
3. **Instrument Claude API usage per conversation** — so §4.2's unknown
   cost line becomes a known one within the first month of real usage,
   not an assumption carried indefinitely.
4. **Launch the content cadence in §5.4** — doesn't depend on billing
   being live; can start building the funnel now.
5. **Revisit this plan at the 90-day mark** (§8) with real subscriber,
   churn, and cost data, and replace every "assumption" and "benchmark"
   citation in §4 with XOLO FITNESS's own numbers.

---

## Sources

- [Online Fitness Market Size — Mordor Intelligence](https://www.mordorintelligence.com/industry-reports/online-fitness-market)
- [Breaking Down the Digital Fitness Trends — WellnessLiving](https://www.wellnessliving.com/blog/breaking-down-the-digital-fitness-market-latest-share-insights-emerging-trends/)
- [Fitness App Churn Rate Benchmarks 2026 — Lifecycle Architect](https://lifecyclearchitect.com/benchmarks/fitness-apps-churn-rate-benchmarks/)
- [In-app subscription benchmarks for Health & Fitness apps — Adapty](https://adapty.io/blog/health-fitness-app-subscription-benchmarks/)
- [LTV to CAC in Fitness Business — The Fitness Operator](https://thefitnessoperator.com/maximize-gym-profitability-understanding-ltv-and-cac-ratios)
- [Unit Economics Explained: LTV, CAC & the 3:1 Ratio — LTV CAC Book](https://ltvcacbook.com/guides/unit-economics)
- [Fitness Coach Instagram Content Ideas: 2026 Marketing Guide — FitBudd](https://www.fitbudd.com/academy/fitness-coach-instagram-content-ideas-guide-to-marketing-for-professionals-2026)
- [Instagram Funnel for Fitness Coaches: 2026 Playbook — CreatorFlow](https://creatorflow.so/blog/instagram-funnel-fitness-coaches/)
- [How to Scale a Coaching Business: 2026 Guide — EntrepreneursHQ](https://entrepreneurshq.com/how-to-scale-a-coaching-business/)
- [Business Scaling Strategies: Expanding Your LLC From Solo to Team — InCorp](https://www.incorp.com/resources/knowledge-base/business-scaling-solo-to-team)
- [Dance Industry Statistics — Gitnux](https://gitnux.org/dance-industry-statistics/)
- [Gymnastics Classes in the US — Market Size — IBISWorld](https://img3.ibisworld.com/united-states/market-size/gymnastics-classes/6322)
- Market/pricing context also draws on `docs/business/XOLOKAN_PRODUCT_SYSTEM.md`'s own sources (SamCart, Paperbell, CoachVox, Trainerize/TrueCoach comparisons), not repeated here.
