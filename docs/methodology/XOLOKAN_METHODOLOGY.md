# XOLOKAN Training Methodology

**Status: Approved.** Reviewed by Oscar; this governs XOLOKAN's persona and
program generator as written below.

This is the canonical training-science layer behind XOLOKAN. It grounds every
program XOLOKAN writes in three inputs: the two Soviet-system source
documents the method is built on, published dance-science research on
calisthenics-based strength training, and injury-prevention evidence for
artist-athletes (dancers, gymnasts, performers). Do not deviate from this
without flagging it.

Source documents live in `docs/methodology/sources/`:
- `dancer_war_manual_12_week.pdf` — 12-week Soviet-system periodization block
- `soviet_advanced_gymnast_dancer_program.pdf` — weekly training split

This doc is under continuous review — a daily automated research pass checks
for new evidence and makes small, cited, incremental updates when warranted.
See `docs/methodology/RESEARCH_LOG.md` for the audit trail of what's been
checked and when.

---

## 1. Periodization framework (Soviet block system)

**Origins.** "Soviet periodization" is two related but distinct lineages, and
it's worth knowing which one a given rule comes from. Matveyev's 1962 model
(the classical version most Western coaches learned) runs high volume/low
intensity early in a training year, sliding toward low volume/high intensity
at a single peak. Verkhoshansky's 1979 **block periodization** — closer to
what the two source manuals actually describe — was a direct critique of
Matveyev: instead of one long taper, it concentrates a narrow set of
qualities inside each block (here: base strength, then power, then peak) and
sequences the blocks so each one's residual training effect feeds the next.
The 12-week phase table below is a block model, not a Matveyev taper — that
distinction is why volume drops sharply from Phase 2 to Phase 3 instead of
gliding down gradually.

The specific three-phase shape XOLOKAN uses traces to Vladimir Issurin, who
systematized Verkhoshansky's block concept into three named blocks:
**Accumulation** (basic strength and technical ability — this is Phase 1,
Base Strength & Control), **Transmutation** (event-specific ability,
built on what accumulation established — Phase 2, Power & Volume), and
**Realization** (peak-specific expression, full adaptation before
performance — Phase 3, Peak Performance). Knowing the block names isn't
trivia: Issurin's sequencing principle is that each block only works
because the one before it left a residual training effect to build on —
skipping or reordering blocks breaks that chain, which is the real reason
"establish current phase before setting intensity" is checklist item #2.

Three 4-week phases, undulating intensity as %1RM (or %effort for bodyweight
work), volume moving inversely to intensity:

| Phase | Weeks | Focus | Intensity |
|---|---|---|---|
| 1 — Base Strength & Control | 1–4 | Form, stability, endurance base | 70–75% |
| 2 — Power & Volume | 5–8 | Explosive movement added, volume increases | 75–85% |
| 3 — Peak Performance | 9–12 | Max explosiveness, volume drops, speed rises | 85–90% |

**Soviet periodization principles to apply, not just the phase table:**
- Decouple volume and intensity across the week rather than moving both up
  together — e.g. one high-intensity/low-volume day paired with a
  high-volume/moderate-intensity day, not two maximal days back to back.
- "Doing less but more": prefer several submaximal sets (e.g. 5×3 at
  moderate load) over a single max-effort set — more total quality volume,
  far less technical breakdown and joint cost.
- Bodyweight proficiency (squat, push-up, pull-up patterns) precedes loaded
  work — this is the on-ramp into the calisthenics layer below, not a
  separate track from it.
- Coach's eye over rigid adherence: the written phase is the default: adjust
  in-session for fatigue, technical breakdown, or pain.
- Deload every 4th week inside any Peak-intensity block — never chain two
  peak weeks without a volume drop. This is an injury-prevention rule, not
  just a performance one (see §3).

**An honest caveat on why block periodization, specifically.** The same
ACSM 2026 position stand cited below (137 pooled systematic reviews,
30,000+ adults) found that periodization models — linear, undulating, or
block — don't consistently outperform each other, or plain progressive
overload, on strength/hypertrophy outcomes for a general population. That
finding doesn't undercut the case for block periodization here: this
method's population isn't the general population in those pooled reviews
— it's artist-athletes stacking training load on top of rehearsal and
performance schedules, where the real value of block structure is
*fatigue and skill-load management* (the deload rule above, sequencing
peak-intensity work around performance dates) rather than a claimed
strength/hypertrophy edge over simpler programming. Say that plainly if
asked "why not just add weight every week" — the honest answer is
injury/fatigue management for a high-demand population, not a hypertrophy
advantage the general-population evidence doesn't support.

**A balancing note, though: for trained athletes specifically, block
periodization does show a real edge.** A 2026 randomized crossover study
in experienced athletes found that concentrating high-intensity load into
blocks produced more favorable maximal-strength outcomes than an evenly-
distributed ("traditional") periodization model — without compromising
conditioning or cardiovascular markers. This is a narrower, different
comparison than the ACSM caveat above (block vs. an alternative
periodized structure, in *trained* athletes — not periodization vs. plain
progressive overload in a general population), so the two findings don't
contradict each other; they apply to different populations and different
questions. Worth stating plainly: this method's actual client base is
professional/pre-professional performers, not general-population
beginners — closer to the trained-athlete population where block
structure's edge actually shows up, which is a real point in favor of the
approach here, not just the fatigue-management case above.

**Intensity and volume landmarks (ACSM 2026 resistance-training update).**
The phase table gives %1RM ranges; these are the volume/effort landmarks
that fill in the rest of the prescription within each phase:

| Goal | Load | Volume | Effort |
|---|---|---|---|
| Maximal strength | ~80% 1RM | 2–3 sets/exercise | Near the top of the rep range in reserve |
| Hypertrophy / general strength | Moderate load | ~10 sets/muscle/week | RPE 7–9, i.e. 2–3 reps in reserve (RIR) |
| Power | 30–70% 1RM | Lower volume | Maximal concentric bar/limb speed, not maximal load |

Use RIR/RPE language over fixed %-effort cues in session — "leave 2 in the
tank on this set" is more actionable and more accurate than "go to 90%
effort," and it's what lets a program hold up across a client's daily
fluctuation in readiness (autoregulation) without XOLOKAN needing to see
them train live.

**Which autoregulation method, specifically.** A 2025 systematic review and
network meta-analysis ranked autoregulation approaches for max-strength
gains: **APRE** (Autoregulating Progressive Resistance Exercise — a test set
determines whether the next set's load goes up, holds, or drops, based on
reps actually achieved) ranked highest, ahead of plain RPE, velocity-based
training, and fixed-percentage programming. Use APRE-style set-to-set load
adjustment on primary lifts, where day-to-day readiness swings matter most;
RPE/RIR language is the simpler, sufficient default everywhere else.

**Two honest caveats on autoregulation, not just its upside.** (1)
**Correction to earlier guidance here**: RIR accuracy does not reliably
track training experience the way it's tempting to assume. A direct
experienced-vs-novice comparison (≥18 months training vs. <18 months,
back squat, objectively verified via bar velocity) found *no* significant
accuracy difference between the groups — and a separate study found RIR
accuracy varies hugely person-to-person with no clear experience effect
either. The practically useful takeaway isn't "coach novices more
carefully than experienced lifters," it's that **RIR accuracy is
individual, not experience-gated** — don't assume any client, regardless
of training age, is automatically a reliable judge of "2 reps in
reserve." Coach it explicitly for everyone (bar speed, form breakdown as
objective cross-checks), and treat a given client's own RIR reports as
something to calibrate against real performance over time, not something
that improves on a fixed experience timeline. (2) In
already-trained lifters on a well-designed periodized program, adding
autoregulated volume adjustment on top didn't outperform the fixed
periodized program for strength, power, or muscle thickness (10-week RCT,
resistance-trained men) — autoregulation is a safety valve for daily
readiness and injury/fatigue management, not a guaranteed strength-gain
multiplier once a program is already well periodized. Keep using RIR/RPE
for the reasons above, but don't oversell it as automatically superior to
a solid fixed plan for an experienced client.

## 2. Weekly training split

Blend of the two source documents' weekly structures — use the 4-day pattern
as the default, expand to 5–6 days for professional/pre-performance blocks:

- **Day 1 — Neural Speed & Power / Upper Strength**: pulls, presses, rows,
  paired with power cleans or med ball throws, depth jumps, short sprints.
- **Day 2 — Strength & Control / Lower Power**: front squats, weighted
  pull-ups, dips, hanging leg raises, farmer carries, squat and jump
  patterns.
- **Day 3 — Reactive Jump Training / Conditioning Circuits**: pogo jumps,
  single-leg bounds, lateral skater jumps, jump rope, or a
  sled-push/pull-up/kettlebell/battle-rope circuit — pick based on whether
  the priority that week is reactive power or work capacity.
- **Day 4 — Athletic Endurance / Explosive Full Body**: circuit-style full
  body work at 4–5 rounds, 2 min rest between rounds.
- **2x/week mobility & recovery**: hip flexor stretch, hamstring stretch,
  thoracic spine rotation, deep squat hold — 2 minutes each, non-negotiable,
  not an optional add-on.

**Warm-up protocol: RAMP.** "Warm up" is not a prescription on its own —
every session opens with Raise, Activate & Mobilise, Potentiate (Jeffreys):
1. **Raise** — light cardio (jogging, jumping jacks, high knees) to raise
   core and muscle temperature and switch on neural drive.
2. **Activate & Mobilise** — active-range movement through the patterns the
   session actually uses (lunges, hip circles, band work), not generic
   stretching.
3. **Potentiate** — a small dose of session-specific intensity (a few
   submaximal jumps or accelerations) that primes the nervous system for
   what's coming.

**A specific, evidence-backed option for the Potentiate step: jump
interval training (JIT).** A 6-month cohort study in female dancers found
3 sets of 30-second bilateral squat jumps during the potentiation phase
produced significantly better long-term gains in aerobic capacity,
isometric strength, and jump power (squat jump, countermovement jump)
than potentiating with ballistic dance movements (leaps, forceful limb
work) instead. This isn't a replacement for RAMP's Potentiate step, it's
a concrete way to fill it on days where building those specific
qualities matters — offer it as the default Potentiate content on
Day 1/Day 3 (power and reactive-jump days) rather than leaving
"submaximal jumps" undefined.

Dynamic, active-range warm-ups outperform static stretching for injury risk
and same-session performance — static stretching, if used at all, belongs in
cooldown, not warm-up. On modality choice for that cooldown: recent
comparisons favor percussion massage over static stretching for reducing
delayed-onset muscle soreness, and where cold water immersion is used for
recovery, 11-15 minutes of exposure is the effective dose (much shorter
soaks are largely symbolic). Neither is mandatory — the RAMP protocol above
is the non-negotiable; these are refinements for a client already asking
"what should I do after training."

**Sleep is a recovery non-negotiable, not a footnote.** Most physical
recovery — growth hormone release, protein synthesis, collagen/connective-
tissue repair — concentrates in deep (slow-wave) sleep specifically, not
just total time in bed. Target 7–9 hours. For performers stacking rehearsal
or performance load on top of training, treat sleep debt as a
volume-reduction trigger with the same weight as missed reps or pain — ask
about it alongside rehearsal hours and performance dates (§5, program design
checklist item 2).

**A strategic nap is a real tool, not a shortcut, for a population with
irregular rehearsal/performance schedules.** Two 2026 meta-analyses found
that — on top of normal nocturnal sleep — daytime napping produces a
large improvement in endurance performance, a moderate improvement in
agility, and significantly reduces fatigue and perceived exertion both
during and after exercise. This is genuinely useful for a client whose
schedule doesn't allow catching up on nighttime sleep debt between a
rehearsal day and an evening performance. Dosing matters: keep naps to
30 minutes or less (longer naps risk sleep inertia — grogginess that
outweighs the benefit) and schedule them early afternoon (roughly
1-3:30pm), which is where the supporting trials consistently placed
them. This is additive to the 7-9 hour nighttime target above, not a
substitute for it.

## 3. Calisthenics layer for dancers/artists

Calisthenics is not a substitute for the periodized strength work above —
it's how relative strength and control get built without adding mass that
compromises line or aesthetic, which matters for this audience in a way it
doesn't for a general lifter.

- **Bodyweight mastery before load**: squat, push-up, and pull-up pattern
  proficiency comes first, same as the Soviet youth-athlete principle above.
- **Isometrics for weak-leverage control**: holds at the sticking point of a
  movement (support holds, L-sit progressions, wall handstand holds, deep
  squat holds) build strength precisely where dancers need controlled
  eccentric lowering and held positions — this is a direct performance
  transfer, not general conditioning. **Effort level matters, not just the
  position**: research on isometric training and tendon adaptation found
  high-intensity holds (≥70% MVC — genuinely hard, not a passive static
  stretch-like position) are what's needed to meaningfully improve tendon
  stiffness and structure, with longer muscle lengths favoring the
  muscle-morphology side of the adaptation. **A correction on how to coach
  that effort, though**: RIR itself doesn't cleanly apply to a hold — "reps
  in reserve" presumes reps, and a hold has none. A validated alternative
  exists specifically for this: the Isometric Exercise Scale (IES), a
  0-10 perceived-exertion scale purpose-built for continuous isometric
  work, strongly correlates with the standard CR-10 exertion scale as
  well as heart rate and blood pressure. Use IES-style effort language for
  holds ("this should feel like an 8-9 out of 10, not a resting position")
  rather than forcing RIR terminology onto a movement pattern it wasn't
  built for.
- **Progression model**: support/assisted → full range of motion →
  weighted or tempo-loaded. Never skip straight to weighted variations
  before full-ROM bodyweight control is clean.
- **Strength-to-bodyweight ratio is the target metric**, not absolute load —
  pull-up, dip, and pistol squat strength scale with the body the artist
  actually performs in.

**Why bodyweight-only can still build real hypertrophy and strength.** This
isn't a compromise XOLOKAN accepts for equipment-limited clients — it's
supported by the load-hypertrophy literature directly. Schoenfeld et al.'s
meta-analysis found low-load training (≤60% 1RM equivalent — squarely where
most bodyweight work sits) taken close to failure builds muscle size
comparably to high-load training; maximal *strength* still favors heavy
loads, but hypertrophy doesn't require them. What matters is proximity to
failure and total volume, not the number on the bar — which is exactly why
the calisthenics progression model above (support → full ROM → weighted)
works as a real strength-building path, not just a bodyweight-only
fallback.

## 4. Injury prevention layer (artist-athlete specific)

Dancers and performers are athletes, and strength & conditioning measurably
reduces their injury risk — this is not optional add-on programming, it's
core to the method.

**The strongest evidence available: a structured, strength-first program
works.** The first prospective randomized controlled trial of an injury
prevention program in professional ballet (Houston Ballet, published in the
*Orthopaedic Journal of Sports Medicine*, 2020) had dancers run a 30-minute,
**strength-focused** program 3x/week for 52 weeks — deliberately built on
"strength beats stretch," not flexibility work. Result: an **82% reduction
in injury rate** and **45% longer time between injuries** versus control.
This directly validates XOLOKAN's own bias (periodized strength +
calisthenics, dynamic RAMP warm-ups over static stretching) — it isn't a
generic best practice, it's the specific approach the best available trial
data supports for this population.

**Screening, not just training.** IADMS (International Association for
Dance Medicine & Science) is the field's standard-setting body for injury
surveillance — its Standard Measures Initiative calls for a pre-season
screen of risk factors and capacities before programming, not just reactive
treatment after injury. Practically: establish baseline numbers (e.g.
strength/balance benchmarks) before a client's first block, the same way
the Day 1 baseline log works in a XOLOKAN program — screening is part of
program design, not a separate clinical step.

**Not every common screening measure actually predicts injury, though —
prioritize balance.** A study of preprofessional ballet dancers found no
significant association between injury and several widely-used screens
(ankle/hip range of motion, active straight leg raise, Y Balance Test
reach distances) — but balance-related measures specifically did show a
protective effect, more so with more years of training. Practical
takeaway: a baseline screen heavy on isolated ROM testing isn't wasted,
but it also isn't where the injury-prediction value actually is — weight
balance/proprioceptive assessment (single-leg stability, reactive
balance) as the higher-priority baseline measure, not just one item on an
equal-weighted checklist.

**Most common injury sites and the countermeasure XOLOKAN should default to:**

| Site | Common injuries | Default countermeasure |
|---|---|---|
| Ankle | Sprains (0.27 injuries/1000h in elite ballet, ~13-14 days lost per sprain), Achilles tendinopathy, impingement | Ankle-focused isometric + eccentric + plyometric block. A 12-week ankle program in the literature raised jump peak power ~60%, braking stiffness ~70%, and leap height ~12%. **For anyone with a prior sprain, add balance/proprioceptive work specifically** (single-leg balance, ankle joint reposition-sense drills) — recurrence risk is driven by degraded proprioception, not just strength, and strength work alone doesn't fully address it. |
| Knee | Patellofemoral pain, ACL/MCL strain from landing/pivoting (92% of ballet ACL injuries occur landing a jump on one leg) | Quad + glute strengthening, single-leg landing mechanics drilled explicitly, not assumed — the single-leg landing emphasis in the Standing Rules below is the direct countermeasure to how these injuries actually happen. |
| Lower back | Disc strain, muscle strain, spinal instability | Core and hip strengthening, posture work, avoid unbroken high-volume loading without a deload. |
| Lower back (gymnast/aerialist) | Spondylolysis (pars interarticularis stress fracture) — the dominant cause of low back pain in adolescent/young gymnasts specifically, a different mechanism than the generic row above | Driven by repetitive spinal hyperextension + rotation (backbends, walkovers, aerial arch work), not axial loading. Deep trunk/lumbar stabilization work in a neutral spine, not generic "core strengthening" — and cap hyperextension-heavy skill volume the same disciplined way plyometric contacts are capped, since this is also a cumulative-load injury. |
| Hip | Snapping hip, impingement, labral irritation, flexor tendinopathy, bursitis, SI dysfunction | Hip mobility work + glute medius / lateral stability training. |
| Wrist (gymnast/aerialist) | Chronic wrist pain from repetitive weight-bearing on an extended wrist | Shoulder ROM work alongside wrist loading progression — a 2026 systematic review of 185,107 gymnasts found 53% pooled wrist pain prevalence, with **decreased shoulder ROM** an identified risk factor, not just wrist-local overuse. Risk climbs with training intensity, years training, and weekly hours, so dose wrist-loaded calisthenics (ring support holds, handstand work) with the same discipline as plyometric contacts below. |
| Shoulder (gymnast/aerialist ring & bar work) | Labral tears (especially SLAP tears on ring/bar apparatus), rotator cuff strain, shoulder instability | A systematic review of still-rings biomechanics identifies the risk profile: lack of shoulder internal rotation, weakness in external rotation, and scapular dyskinesia — not just cumulative ring-support volume. Screen internal/external rotation ROM and scapular control before progressing ring-support holds; prioritize periscapular and rotator-cuff strengthening (external-rotation work specifically), and load ring support progressively (dumbbell-assisted before full bodyweight support) rather than jumping straight to unassisted holds. Directly relevant to this method's Ring Support Hold and Wall Handstand Hold work. |

**Plyometric dosage (governs Day 3 — Reactive Jump Training).** Volume here
is measured in foot contacts per session, not just sets/reps, and it's a
real injury lever if overdosed on a jump-heavy artist:

| Experience | Contacts / session | Frequency |
|---|---|---|
| Beginner | 50–80 | 2x/week |
| Intermediate (3+ months consistent training) | 80–120 | 2–3x/week |
| Advanced (6+ months progressive training) | 100–140 high-intensity (up to ~200 low-intensity) | 2–3x/week |

Always on non-consecutive days, 48–72 hours apart, so the ankle/knee
countermeasures above have time to do their job between sessions. The
underlying reason: **tendons adapt more slowly than muscle**, so the
48–72h spacing isn't conservative padding, it's matched to the slower
tissue. Run plyometric progression in 4–6 week blocks rather than
open-ended increases — this is also where the tendon-stiffness adaptation
actually shows up (better energy return, shorter ground contact time),
not just injury avoidance. Landing cue to standardize across Day 3:
**heel stays high, short amortization** (minimal pause between landing
and the next takeoff) — a longer amortization phase bleeds the elastic
energy the plyometric work is supposed to build.

**Microdosing option for heavy rehearsal/performance weeks.** A 2025 RCT
found that splitting the same total plyometric stimulus into more,
smaller sessions (4x/week at ~100 jumps/session) produced equivalent
gains in reactive strength, jump performance, and sprint speed as a
concentrated schedule (2x/week at ~200 jumps/session) — no difference
between approaches, and the microdosed version needed a fraction of the
per-session volume to get there. This is a real, evidence-backed option
for this population specifically: when rehearsal or performance load is
already high, spreading the weekly contact total across more, lighter
sessions is not a compromise — it's a legitimate alternative dosing
strategy, not just "less training." Default to the concentrated 2–3x/week
model in the table above; offer the microdosed spread as the adjustment
when a client's total weekly load (training + rehearsal) needs to come
down without dropping the plyometric stimulus entirely.

**Pair plyometric work with balance training, not just for prior-injury
clients.** A 12-week study in college dancers found combined balance +
plyometric training outperformed plyometric training alone at improving
dynamic balance and reducing single-leg landing instability (measured as
center-of-pressure displacement) — a genuine additive effect, not just
overlap between two similar interventions. This extends beyond the
existing prior-ankle-sprain rule below (standing rule #4): balance work
belongs alongside Day 3's plyometric volume as a general pairing for any
jump-heavy artist, not only as a corrective bolted on after an injury
history.

**Standing rules:**
1. **Single-leg / unilateral work every week, no exceptions.** Landing
   mechanics and side-to-side asymmetry are the biggest lever for jump-heavy
   artists — this cannot be an afterthought accessory movement. A 2025/2026
   pair of meta-analyses adds direct performance evidence, not just an
   injury-prevention rationale: unilateral training specifically improves
   unilateral strength and unilateral jump performance over bilateral
   training, while both produce equivalent hypertrophy — exactly the
   performance quality (single-leg jump/landing) this population needs, so
   unilateral work isn't a lesser substitute for bilateral lifts, it's the
   more specific tool for the actual skill.
2. **Isometric holds at least 1x/week** for control-heavy artists (dancers,
   aerialists, gymnasts) — ties directly to the calisthenics layer above.
3. **Ankle and hip prehab by default** for anyone doing regular jumping or
   pivoting work, not just after an injury.
4. **Prior ankle sprain gets proprioceptive work, not just more strength.**
   Ask about sprain history before programming — a history of ankle sprain
   is itself the strongest predictor of another one, and the fix is
   balance/joint-reposition-sense training layered on top of the standard
   ankle block, not a heavier dose of the same isometric/eccentric work.
5. **Deload every 4th peak week** (restated from §1 — this is as much an
   injury rule as a performance one).
6. **Cross-training and periodization are injury-prevention strategies.**
   Planning volume across a season, not just within a week, is what keeps an
   artist at peak condition for performance dates instead of managing
   overuse injuries around them.
7. **Baseline non-negotiables**: warm-up before every session, hydration,
   sleep, and not stacking overtraining on top of rehearsal/performance load
   that XOLOKAN doesn't see directly — always ask what else is on the
   client's week before prescribing volume.

## 5. Program design checklist (apply before writing any program)

1. Establish baseline first (IADMS screening principle): before a client's
   first block, get their injury history and, where possible, simple
   strength/balance benchmarks — screening is part of program design, not
   a step that happens separately.
2. Establish current phase (Base / Power-Volume / Peak) before setting
   intensity.
3. Confirm outside load: rehearsal hours, performance dates, other training
   — periodize around it, don't ignore it.
4. Include unilateral/single-leg work this week. No exceptions.
5. Include an isometric control element if the client is a dancer,
   aerialist, gymnast, or otherwise control-dependent performer.
6. Include ankle and/or hip prehab by default for jump/pivot-heavy artists.
   If there's a prior ankle sprain, add proprioceptive/balance work, not
   just more strength work.
7. If this is week 4 of a peak block, deload — drop volume, hold or reduce
   intensity.
8. Any pain, sharp discomfort, or injury history gets referred out — flag
   to a doctor or physical therapist, don't diagnose or prescribe rehab
   beyond general mobility guidance.

## 6. Nutrition & energy availability

Not previously in scope, and it should be: dancers specifically — and by
extension other lean, aesthetic-conscious performers — are a documented
at-risk population for **RED-S (Relative Energy Deficiency in Sport)**, the
consequence of chronically under-fueling relative to training demand. This
isn't a fringe concern: one study of vocational ballet students found 65%
at risk of RED-S, with 40% reporting menstrual dysfunction. Training
prescription without a baseline nutrition awareness is incomplete for this
audience.

**Baseline macronutrient targets** (adjust for individual training load):
- Carbohydrate: 3–5 g/kg/day
- Protein: 1.2–1.7 g/kg/day
- Fat: 20–35% of total energy intake
- Minimum energy floor: ≥30 kcal/kg fat-free mass/day, plus training energy
  expenditure — this is a floor to avoid low energy availability, not a
  target to hit exactly.

**Watch for**: unintentional weight loss during a peak block, missed or
irregular menstrual cycles, persistent fatigue disproportionate to training
load, or repeated stress-response injuries (stress fractures, frequent soft
tissue injury) — these are RED-S indicators, not just overtraining. Iron and
calcium are the micronutrients most often low in dancers' diets specifically
and worth flagging.

**A validated screening tool exists for this, and it's worth naming
specifically rather than leaving "watch for" as an informal checklist.**
The LEAF-Q (Low Energy Availability in Females Questionnaire) is validated
specifically in dancers (alongside endurance athletes), not just adapted
from a generic athlete population — a real advantage over informal symptom
review. A dance-specific tool also exists (the DEAQ, Dance-specific Energy
Availability Questionnaire) but isn't yet externally validated, so treat
it as promising, not equivalent to LEAF-Q's evidence base. XOLOKAN can
mention the LEAF-Q by name as something a client's doctor or sports
dietitian may use — this isn't a tool for XOLOKAN to administer or score
itself, same referral posture as the rest of this section.

**Ask about existing dietary patterns, don't assume a clean slate.** A
2026 scoping review found dancers overwhelmingly source nutrition advice
from peers (65.7%) or friends (57.1%) rather than credentialed sources,
and over a third (37.1%) follow a restrictive diet (vegan, pescatarian,
lactose-free, etc.) — often self-adopted, not clinically supervised. This
matters practically: a restrictive diet can make the protein and energy
targets above genuinely harder to hit, not just a lifestyle detail to
note in passing, so ask what a client is already doing before assuming
the macronutrient targets are a clean starting point. It also reinforces
why the referral boundary below is worth stating plainly rather than
softening — nutrition misinformation from non-expert sources is already
the norm in this population, not an edge case.

**Boundary**: XOLOKAN can share these baseline targets and watch-for signs.
Actual RED-S risk assessment, diagnosis, and individualized nutrition
prescription belong to a doctor or sports dietitian — refer out rather than
managing it in-app, same posture as the injury-referral rule above.

**Creatine monohydrate** is the one supplement worth naming specifically,
because the evidence base is unusually strong for exactly this population
and it's still underused by performers who associate it with bodybuilding
rather than recovery/cognition. A 42-day trial in female collegiate dancers
found increased total body water and lean mass with no adverse effects —
direct evidence in the target demographic, not an extrapolation from male
strength-athlete data. Separately, creatine has a documented cognitive
benefit specifically under sleep deprivation (faster processing speed,
better working memory) — directly relevant here since the methodology
already treats sleep debt as a training-load variable (see the sleep
section above). Standard protocol: 3-5 g/day monohydrate, no loading phase
needed, taken consistently rather than only on training days.

## 7. Demographic factors: age & sex

Client age (in 5-year brackets, 20–40) and anatomical sex are intake
inputs that measurably change programming — implemented in
`packages/xolokan-agent/src/demographics.ts`, wired into
`generateProgram()` so every program picks these up automatically, not
just this document. A note on scope: within 20–40, the real physiological
differences are more "20s vs 30s" than four sharply distinct 5-year zones
— the brackets below are honest about where the science actually
differentiates versus where they're a reasonable segmentation choice.

### Age

| Bracket | What's actually different |
|---|---|
| 20–25 | Peak bone mass is typically reached by the mid-20s (~25.7y men, ~24.8y women) and plateaus for decades after — this is the single highest-leverage window for heavy compound loading's long-term payoff. |
| 25–30 | Still inside or just past the peak bone-mass window — same guidance as 20–25, no meaningful physiological gap between these two brackets. |
| 30–35 | Recovery capacity begins a gradual, normal decline. Consider a deload every 3rd peak week instead of every 4th if fatigue accumulates faster than the default schedule assumes — this is a pacing adjustment, not a reduction in what's achievable. |
| 35–40 | Research on training-age recovery suggests ~10–20% longer regeneration windows than the early 20s (declining anabolic hormone levels, reduced satellite cell responsiveness, changing slow-wave sleep architecture). Build the extra recovery in rather than cutting it to preserve the same weekly volume. |

### Sex (anatomical/biomechanical, not identity or ability)

These factors exist because of documented anatomical and biomechanical
differences tied to biological sex — not because training capacity or
preference differs by sex. Framing matters here: the countermeasures below
are about risk factors with a known anatomical mechanism, not a claim that
women need an easier program.

- **ACL injury risk is 3–8x higher in women.** Driven by a greater Q-angle
  (anatomical) and a more erect, quad-dominant landing pattern with
  greater knee valgus (biomechanical) — not by weakness alone.
  Countermeasure: posterior chain / hip-abductor strength plus explicit
  landing-mechanics cueing. `generateProgram()` inserts a Banded Lateral
  Walk into the reactive-jump day for female clients specifically, on top
  of the standing single-leg-work rule that already applies to everyone.
- **Pelvic floor dysfunction is under-recognized in young female strength
  athletes, not just postpartum or older populations.** Research on this
  population found significant prevalence of dysfunction from the
  intra-abdominal pressure spikes of heavy lifting and jump-landing work.
  Cue "the Knack" (a conscious pelvic floor contraction just before the
  effort) on heavy lifts and landings; any leaking, heaviness, or pressure
  gets referred to a pelvic floor physical therapist, not pushed through.
  **This is especially relevant for the Gymnast/Aerialist archetype
  specifically**: prevalence of urinary incontinence in young, nulliparous
  rhythmic gymnasts runs above 30% — driven by repetitive high-impact
  landing exposure, not heavy barbell loading, so it's a real risk even
  for clients who've never touched a loaded lift. Most gymnasts in this
  research had no prior knowledge of the pelvic floor or PFM training at
  all — this is a genuine education gap XOLOKAN can close simply by
  raising it, not something to assume is already understood. **One honest
  caveat**: a cluster-randomized trial found that basic PFM training added
  to warm-up (8-12 near-maximal contractions, 8 months) did *not*
  meaningfully reduce UI bother in competitive rhythmic gymnasts — so
  treat "the Knack" cue as a reasonable default, not a proven fix for this
  specific population's high-impact exposure, and lean harder on the
  referral-out boundary rather than implying a simple cue resolves it.
- **No reliable evidence supports programming around menstrual cycle
  phase.** A 2023 umbrella review — the highest tier of evidence available,
  reviewing every meta-analysis and systematic review on the topic —
  found no basis for cycle-phase-based training recommendations. Train at
  consistent intensity and autoregulate via RIR/RPE around individual
  symptoms over multiple cycles, never a fixed calendar. Don't build
  cycle-syncing into programming even though it's a common trend.
- **Baseline strength differs by sex; the training response doesn't.**
  Female upper-body strength averages ~56% of male, lower-body ~72% — but
  women show *greater relative* strength gains from training than men do.
  This is exactly why the method already tracks relative,
  bodyweight-scaled strength as its primary metric rather than absolute
  load — that framework is sex-fair by construction, not by adjustment.
- **Injury *site* distribution differs by sex in dancers specifically, not
  just ACL risk.** A 2025 epidemiology review found female dancers are more
  susceptible to lower back and knee injuries, while male dancers face
  higher rates of acute lower back and foot injuries (and a higher share
  of craniofacial injury, 19.4% vs. 13.7% — a partner-work/lift-related
  exposure difference worth a caution note for male dancers in
  partnering-heavy rehearsal). This sits alongside the ACL bullet above,
  not in place of it: ACL risk explains one specific injury type, this is
  about where to weight prehab attention across the whole body by sex.

## 8. From methodology to product

This document is the science layer. It's implemented as a deterministic
program generator — not left as prose XOLOKAN has to reconstruct per
conversation — in `packages/xolokan-agent/src/`:

- `programSchema.ts` — the intake and output data shapes.
- `archetypes.ts` — three sellable program archetypes (dancer,
  gymnast-aerialist, general-performer), each a discipline-tailored version
  of the §2 weekly split with its own §4 prehab emphasis.
- `generateProgram.ts` — pure function: client intake in, a full structured
  12-week program out, phase/deload/prehab/equipment-substitution logic all
  applied per the rules above. No LLM call required — run it directly via
  `npm run generate:sample --workspace=packages/xolokan-agent`.
- `tools.ts` — wraps the generator as a tool XOLOKAN can call mid-conversation.

See `docs/business/XOLOKAN_PRODUCT_SYSTEM.md` for how this turns into
sellable programs — archetype catalog, pricing, and positioning.

---

## Sources

- Uploaded: 12-Week Dancer War Manual (Soviet System)
- Uploaded: Advanced Soviet Gymnast / Dancer Performance System
- [A meta-analysis of the effects of strength training on physical fitness in dancers — Frontiers in Physiology, 2025](https://www.frontiersin.org/journals/physiology/articles/10.3389/fphys.2025.1511833/full)
- [Strength and conditioning in dance: A systematic review and meta-analysis — Ngo et al., European Journal of Sport Science, 2024](https://onlinelibrary.wiley.com/doi/full/10.1002/ejsc.12111)
- [The Impact of Dance-Specific Neuromuscular Conditioning and Injury Prevention Training on Motor Control, Stability, Balance, Function and Injury in Professional Ballet Dancers — PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC8016435/)
- [Preventing dance injuries: current perspectives](https://www.tandfonline.com/doi/full/10.2147/OAJSM.S36529)
- [Common Dance Injuries and Prevention Tips — Johns Hopkins Medicine](https://www.hopkinsmedicine.org/health/conditions-and-diseases/sports-injuries/common-dance-injuries-and-prevention-tips)
- [Isolated Joint Block Progression Training Improves Leaping Performance in Dancers — PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8712483/)
- [Association between 2D landing biomechanics, isokinetic muscle strength and asymmetry — PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12212501/)
- [Periodization in Dance Training — Kinetic Wellness](https://kineticwellness.newzenler.com/blog/periodization-in-dance-training)
- [Cross Training & Injury Prevention — Gaynor Minden](https://dancer.com/ballet-info/dancers-health/cross-training-injury-prevention/)
- [The System: Soviet Periodization Adapted for the American Strength Coach — Nie Lasher](https://nielasher.com/products/the-system-soviet-periodization-adapted-for-the-american-strength-coach)
- [Comparison of the Matveev Periodization Model and the Verkhoshansky Periodization Model — ResearchGate](https://www.researchgate.net/publication/329281437_Comparison_of_the_Matveev_Periodization_Model_and_the_Verkhoshansky_Periodization_Model)
- [ACSM Unveils Landmark 2026 Resistance Training Guidelines](https://acsm.org/resistance-training-guidelines-update-2026/)
- [The Effect of Load and Volume Autoregulation on Muscular Strength and Hypertrophy: A Systematic Review and Meta-Analysis — PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8762534/)
- [Why every dancer should use the RAMP warm-up — Ausdance VIC](https://ausdancevic.org.au/resource/why-every-dancer-should-use-the-ramp-warm-up/)
- [Plyometric Training Injury Prevention / Jump Training Volume Progression — True Sports Physical Therapy](https://www.truesportsphysicaltherapy.com/blogs/plyometric-training-that-builds-power-without-breaking-down-your-body)
- [Epidemiology and Risk Factors of Wrist Pain and Injury in Adolescent Artistic Gymnasts: A Systematic Review and Meta-analysis — PMC, 2026](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12804664/)
- [What Do We Know About the Energy Status and Diets of Pre-Professional and Professional Dancers: A Scoping Review — Nutrients](https://doi.org/10.3390/nu16244293)
- [Assessment of Dietary Intake, Energy Status, and Factors Associated With RED-S in Vocational Female Ballet Students — Frontiers in Nutrition / PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6333673/)
- [Autoregulated Resistance Training for Maximal Strength Enhancement: A Systematic Review and Network Meta-Analysis, 2025 — PubMed](https://pubmed.ncbi.nlm.nih.gov/40791980/)
- [Sleep and Athletic Performance: A Multidimensional Review of Physiological and Molecular Mechanisms — MDPI](https://www.mdpi.com/2077-0383/14/21/7606)
- [An Injury Prevention Program for Professional Ballet: A Randomized Controlled Investigation — Houston Methodist / Orthopaedic Journal of Sports Medicine, 2020](https://pmc.ncbi.nlm.nih.gov/articles/PMC7388110/)
- [An Update on the Six Recommendations from the 2012 IADMS Standard Measures Initiative: Assessing and Reporting Dancer Capacities, Risk Factors, and Injuries, 2024](https://pubmed.ncbi.nlm.nih.gov/39392612/)
- [Epidemiology and management of ankle sprain injuries over seven seasons in an elite professional ballet company — Journal of Science and Medicine in Sport](https://www.jsams.org/article/S1440-2440(23)00508-X/fulltext)
- [Incidence of anterior cruciate ligament injuries among elite ballet and modern dancers: a 5-year prospective study — PubMed](https://pubmed.ncbi.nlm.nih.gov/18753681/)
- [Strength and Hypertrophy Adaptations Between Low- vs. High-Load Resistance Training: A Systematic Review and Meta-analysis — Schoenfeld et al., JSCR, 2017](https://pubmed.ncbi.nlm.nih.gov/28834797/)
- [Block Periodization versus Traditional Training Theory: A Review — Issurin](https://www.researchgate.net/profile/Vladimir-Issurin/publication/5638447_Block_periodization_versus_traditional_training_theory_A_review/)
- [Creatine monohydrate supplementation changes total body water and DXA lean mass estimates in female collegiate dancers — Journal of the International Society of Sports Nutrition, 2023](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10044149/)
- [Single-Dose Creatine Reduces Sleep Deprivation-Induced Deterioration in Cognitive Performance — Nutrients / Scientific Reports](https://www.nature.com/articles/s41598-024-54249-9)
- [The effect of percussion massage therapy on the recovery of delayed onset muscle soreness — randomized controlled trial, Frontiers in Public Health, 2025](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11979224/)
- [Impact of different doses of cold water immersion (duration and temperature variations) on recovery from acute exercise-induced muscle damage: a network meta-analysis — Frontiers in Physiology, 2025](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11897523/)
- [Autoregulation Does Not Provide Additional Benefits to a Mixed Session Periodized Resistance Training Program in Trained Men — Journal of Strength and Conditioning Research, 2024](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11343444/)
- [Dance-Related Injuries: An Evidence-Based Review of Epidemiology, Mechanisms, and Prevention Strategies — Current Physical Medicine and Rehabilitation Reports, 2025](https://link.springer.com/article/10.1007/s40141-025-00523-4)
- [A Systematic Review of Dynamic, Kinematic, and Muscle Activity during Gymnastic Still Rings Elements — PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC10059656/)
- [ACSM 2026 Resistance Training Position Stand — periodization models vs. progressive overload finding (137 pooled systematic reviews, 30,000+ adults) — Medicine & Science in Sports & Exercise, April 2026](https://acsm.org/resistance-training-guidelines-update-2026/)
- [Comparison of Muscle Growth and Dynamic Strength Adaptations Induced by Unilateral and Bilateral Resistance Training: A Systematic Review and Meta-analysis — Sports Medicine, 2025](https://pubmed.ncbi.nlm.nih.gov/39794667/)
- [Comparative effects of unilateral versus bilateral training on performance adaptations: a systematic review and multilevel meta-analysis — BMC Sports Science, Medicine and Rehabilitation, 2026](https://link.springer.com/article/10.1186/s13102-026-01834-2)
- [Plyometric jump training micro- and high-dose effects on amateur basketball players' athletic performance: a randomized controlled trial — Frontiers in Physiology, 2025](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12518302/)
- [The effect of daytime napping on the athletic performance of team ball sports athletes: systematic review and meta-analysis — Frontiers in Physiology, 2026](https://www.frontiersin.org/journals/physiology/articles/10.3389/fphys.2026.1878224/full)
- [The effects of daytime napping on psychophysiological measures in physically active individuals and athletes: a systematic review, meta-analysis, and meta-regression — PMC, 2026](https://pmc.ncbi.nlm.nih.gov/articles/PMC12884900/)
- [Nutrition Knowledge of Dancers: A Scoping Review — Nutrients, 2026](https://doi.org/10.3390/nu18152461)
- [Objective Accuracy in Estimating Repetitions in Reserve in the Back Squat: An Analysis between Experienced vs. Novice Subjects — Journal of Human Kinetics](https://pmc.ncbi.nlm.nih.gov/articles/PMC13215226/)
- [Exercise type, training load, velocity loss threshold, and sets affect the relationship between lifting velocity and perceived repetitions in reserve in strength-trained individuals — PeerJ, 2025](https://pmc.ncbi.nlm.nih.gov/articles/PMC12360324/)
- [Relationships Between Common Preseason Screening Measures and Dance-Related Injuries in Preprofessional Ballet Dancers — Journal of Orthopaedic & Sports Physical Therapy, 2023](https://doi.org/10.2519/jospt.2023.11835)
- [High level rhythmic gymnasts and urinary incontinence: Prevalence, risk factors, and influence on performance — Scandinavian Journal of Medicine & Science in Sports, 2020](https://onlinelibrary.wiley.com/doi/10.1111/sms.13548)
- [Pelvic floor muscle training by competitive rhythmic gymnasts at regular training sessions did not reduce urinary incontinence: a cluster-randomised trial — ScienceDirect](https://www.sciencedirect.com/science/article/pii/S1836955325000189)
- [Urinary Incontinence in Young Gymnastics Athletes: A Scoping Review — Sports, 2025](https://doi.org/10.3390/sports13090319)
- [Block periodization vs. traditional periodization in high-intensity functional training: a randomized crossover study — Frontiers in Physiology, 2026](https://www.frontiersin.org/journals/physiology/articles/10.3389/fphys.2026.1810477/full)
- [Bone Mineral Accrual From Adolescence Into Young Adulthood and Peak Bone Mass: A Longitudinal Cohort Study — PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12560013/)
- [The ACL Female Athlete Crisis — AOSSM](https://www.sportsmed.org/membership/sports-medicine-update/summer-2026/the-acl-female-athlete-crisis)
- [Sex specific considerations in anterior cruciate ligament injuries in the female athlete: State of the art — ScienceDirect](https://www.sciencedirect.com/science/article/pii/S205977542400172X)
- [Factors Associated with Urinary Incontinence in Female Weightlifters — PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12897852/)
- [Pelvic Floor Muscle Training on Stress Urinary Incontinence in Power- and Weightlifters: a Pilot Study — PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC11245411/)
- [Current evidence shows no influence of women's menstrual cycle phase on acute strength performance or adaptations to resistance exercise training — Colenso-Semple, D'Souza, Elliott-Sale, Phillips, Frontiers in Sports and Active Living, 2023](https://www.frontiersin.org/journals/sports-and-active-living/articles/10.3389/fspor.2023.1054542/full)
- [Narrative Review of Sex Differences in Muscle Strength, Endurance, Activation, Size, Fiber Type, and Strength Training — JSCR, 2023](https://journals.lww.com/nsca-jscr/fulltext/2023/02000/narrative_review_of_sex_differences_in_muscle.28.aspx)
- [Resistance training induces similar adaptations of upper and lower-body muscles between sexes — Scientific Reports](https://www.nature.com/articles/s41598-021-02867-y)
- [Tendon Adaptation to Plyometric Training — Wheeler Sports Tech](https://www.wheelersportstech.com/2026/02/05/tendon-adaptation-to-plyometric-training/)
- [Effects of plyometrics training on lower limb strength, power, agility, and body composition in athletically trained adults: systematic review and meta-analysis — Scientific Reports, 2025](https://www.nature.com/articles/s41598-025-10652-4)
- [Spondylolysis: A Narrative Review of Etiology, Diagnosis, and Management — MDPI](https://www.mdpi.com/1660-4601/23/2/153)
- [Injuries in Artistic Gymnastics: Etiology, Prevention Strategies, and Multifactorial Perspectives — A Systematic Review, 2026 — PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12652705/)
- [Prevention and Treatment of Low Back Pain in Young Female TeamGym Gymnasts — ClinicalTrials.gov](https://clinicaltrials.gov/study/NCT04778215)
- [Isometric training and long-term adaptations: Effects of muscle length, intensity, and intent: A systematic review — ResearchGate](https://www.researchgate.net/publication/329881153_Isometric_training_and_long-term_adaptations_Effects_of_muscle_length_intensity_and_intent_A_systematic_review)
- [The effect of 12-week combined balance and plyometric training on dynamic balance and lower extremity injury risk in college dancers — PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC11851013/)
- [Additional jump interval training as a form of warm-up on enhancing aerobic capacity, muscular strength, and power in female dancers: a cohort study — PMC, 2025](https://pmc.ncbi.nlm.nih.gov/articles/PMC12259603/)
- [The LEAF questionnaire: A screening tool for the identification of female athletes at risk for the female athlete triad — ResearchGate](https://www.researchgate.net/publication/260376095_The_LEAF_questionnaire_A_screening_tool_for_the_identification_of_female_athletes_at_risk_for_the_female_athlete_triad)
- [From validation to application: a methodological review of relative energy deficiency in sport (REDs) screening — Performance Nutrition, 2026](https://link.springer.com/article/10.1186/s44410-026-00020-2)
- [Validity and reliability of the 'Isometric Exercise Scale' (IES) for measuring ratings of perceived exertion during continuous isometric exercise — Scientific Reports, 2021](https://www.nature.com/articles/s41598-021-84803-8)
