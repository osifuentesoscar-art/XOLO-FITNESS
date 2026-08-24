# Future Programs — Catalog Expansion Candidates

**Status: Draft v1 — candidates for evaluation, not yet built or
committed to.** The current sellable catalog is three archetypes (Dancer,
Gymnast/Aerialist, Performer Protocol — see
[`XOLOKAN_PRODUCT_SYSTEM.md`](XOLOKAN_PRODUCT_SYSTEM.md) §2). Adding a
fourth is explicitly designed to be a data change in `archetypes.ts`, not
a rewrite — this document is the research pass that should precede that
decision, not a commitment to build all of these. Sequencing lives in
[`ROADMAP.md`](ROADMAP.md).

Each candidate is scored on three things: **audience fit** (does the
[Artist Athlete](../brand/ARTIST_ATHLETE_BRAND.md) positioning apply
naturally, or would it need its own framing), **methodology overlap**
(how much of the existing cited science in
`docs/methodology/XOLOKAN_METHODOLOGY.md` already applies vs. needing
fresh research), and **build effort** (how much new work in
`archetypes.ts`, `demographics.ts`, and the PDF cue dictionaries a launch
would take).

---

## Near-term candidates

### 1. Stunt & Action Performer Protocol

**Audience**: Film/TV stunt performers, stunt doubles, action-focused
performers. **Why this fits particularly well**: it's the archetype
closest to the founder's own background (movement direction/choreography
for touring artists) — a credible, authentic entry point rather than a
cold market. Stunt performers train year-round across *multiple*
disciplines simultaneously (strength, cardio, martial arts, flexibility)
specifically because they need to adapt to whatever a role demands, and
injury prevention is treated as core, ongoing work, not an afterthought —
a strong match for this method's own "conditioning protects the
performance" positioning.

- **Audience fit**: Excellent. This is the most literal "artist athlete"
  of any candidate — the job title itself fuses the two words.
- **Methodology overlap**: High. Multi-disciplinary conditioning,
  injury-prevention-as-core-training, and the existing General Performer
  archetype's balanced-capacity approach transfer directly. Gap: no
  martial-arts-specific or fall/impact-landing-specific research yet in
  the methodology — worth a dedicated research pass before building.
- **Build effort**: Medium. Needs its own exercise selection (likely
  emphasizing multi-planar power, fall mechanics, grip/impact tolerance)
  more than a new demographic model — the existing age/sex factors and
  phase structure carry over directly.
- **Recommendation**: Strong near-term candidate. Do a dedicated
  injury-prevention research pass (stunt-specific fall mechanics, martial
  arts cross-training injury data) before drafting the archetype, same
  practice as every other archetype's science layer.

### 2. Figure Skating Protocol

**Audience**: Competitive figure skaters (off-ice conditioning).

- **Audience fit**: Good — jump-heavy, aesthetic-conscious, artist-athlete
  tension is well-documented in this population too (skating is judged
  on artistry as much as technical difficulty).
- **Methodology overlap**: Very high — this is the lowest-lift candidate.
  The existing plyometric dosage table, ankle/knee injury countermeasures,
  and landing-mechanics cueing (heel-high, short amortization) all
  transfer almost directly; figure skating's own injury literature
  echoes the same ankle/knee/quad-dominance patterns already cited for
  dancers and gymnasts, plus a skating-specific note (stiff boots impede
  force attenuation on landing, and skaters run more quad-dominant than
  hamstring/glute-balanced — the existing single-leg/posterior-chain
  emphasis is a direct fit, not a new build).
- **Build effort**: Low. Closest existing archetype to adapt from is
  Gymnast/Aerialist's jump-landing emphasis.
- **Recommendation**: Strong near-term candidate specifically *because*
  it's low-lift — a good second-archetype-expansion test case before
  committing to a heavier build like Stunt & Action.

## Middle-tier candidates

### 3. Cheerleading / Competitive Acro Protocol

**Audience**: Competitive cheerleaders, acro/tumbling athletes.

- **Audience fit**: Moderate — this population increasingly self-frames
  as athletes (the sport has professionalized rapidly), so the
  artist-athlete tension is less central here than for dance/skating —
  worth confirming before leaning hard on that specific positioning for
  this archetype.
- **Methodology overlap**: High — the injury profile (ankle, wrist,
  shoulder from tumbling/stunt work) overlaps substantially with
  Gymnast/Aerialist. The real differentiator would be partner-stunt-
  specific content (basing/flying roles, catch mechanics) that doesn't
  exist in the current archetype at all.
- **Build effort**: Medium — real market size ($1B+ equipment market
  alone, professionalizing fast), but partner/stunt-catch mechanics is
  genuinely new content, not an adaptation.
- **Recommendation**: Worth building once Stunt & Action or Figure
  Skating validate the "4th archetype" process — real market, but the
  partner-stunt content is enough new research to not be the first pick.

## Longer-term / higher-lift candidates

### 4. Musical Theatre / Touring Performer (split from General Performer)

Currently folded into the general Performer Protocol. Touring-specific
demands (6-8 shows/week, travel, minimal recovery windows between shows)
are real and distinct enough from the current archetype's "balanced
general resilience" framing to eventually warrant its own program — but
this is a *refinement* of an existing archetype's emphasis, not a new
build, so it's lower priority than a genuinely new audience.

### 5. Youth / Pre-Professional track (under-20)

The existing age-factor system (`demographics.ts`) covers 20-40 in 5-year
brackets deliberately — extending down into adolescent/pre-professional
training is a **materially different research problem** (growth-plate
and skeletal-maturity considerations, RED-S risk is often *higher* in
adolescent dancers/gymnasts specifically, parental/guardian consent and
communication norms differ entirely from an adult client relationship).
Flagging this explicitly: **do not treat this as a simple age-bracket
extension** — it needs its own dedicated research and program-design pass
before any building starts, not a data tweak to the existing brackets.
Longer-term, real opportunity (gymnastics/cheer skew young), but the
highest-lift item on this list by a wide margin.

---

## How this maps to the roadmap

Sequencing, ownership, and timing live in [`ROADMAP.md`](ROADMAP.md) —
this document is the research/evaluation layer underneath it, kept
separate so the roadmap can stay a short, scannable sequencing doc
without carrying all of this reasoning inline.

---

## Sources

- [Cheerleading Equipment Market Size and Forecast — Data Horizzon Research](https://datahorizzonresearch.com/cheerleading-equipment-market-21960)
- [A systematic review of cheerleading injuries: epidemiological characteristics, biomechanical mechanisms, and prevention strategies — Frontiers in Public Health, 2025](https://www.frontiersin.org/journals/public-health/articles/10.3389/fpubh.2025.1614164/full)
- [Actor Physical Preparation: The Best Ability Is Availability — Luke Worthington](https://www.lukeworthington.com/actor-physical-preparation-the-best-ability-is-availability/)
- [Preventing figure skating injuries — Boston Children's Hospital](https://answers.childrenshospital.org/figure-skating-injuries/)
- [Identifying training factors for injury risk reduction in UK elite figure skaters — a pilot study — ScienceDirect](https://www.sciencedirect.com/science/article/pii/S2772696725000262)
