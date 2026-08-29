# XOLOKAN Methodology — Research Log

Append-only log of the daily research pass. Most recent entry on top. Exists
so each day's run knows what's already been checked and when, independent of
conversation memory — the methodology doc's own Sources section is the
citation list, this log is the audit trail of what was searched and why
nothing changed (or did).

Topic rotation the daily pass draws from: periodization, calisthenics /
relative strength, dance-injury prevention, gymnast/aerialist-specific
injury prevention, plyometrics, RPE/autoregulation, warm-up & recovery,
nutrition for performers.

## 2026-08-29 — correction: RIR doesn't apply cleanly to isometric holds

**Checked:** RPE/autoregulation (stalest topic, last touched 2026-08-21).

**Found:** The 2026-08-25 entry added an intensity spec to isometric
holds ("coach these with a clear RIR like any other set") but that's an
imprecise fit — RIR presumes reps in reserve, and a hold has no reps. A
validated alternative exists specifically for this: the Isometric
Exercise Scale (IES), a 0-10 perceived-exertion scale purpose-built for
continuous isometric work, strongly correlates with the standard CR-10
scale as well as heart rate and blood pressure. This is a genuine
correction to how the effort-level guidance was phrased, not a new
finding about the holds themselves — the ≥70% MVC intensity target from
08-25 stands, only the coaching language changes.

**Action:** Corrected the isometrics passage in methodology §3 and the
mirrored passage in persona.ts: use IES-style perceived-exertion language
("this should feel like an 8-9 out of 10") for holds instead of RIR
terminology borrowed from rep-based sets. One source added.

## 2026-08-28 (later) — name a validated RED-S screening tool (LEAF-Q)

**Checked:** Nutrition for performers (stalest topic, last touched
2026-08-20).

**Found:** The LEAF-Q (Low Energy Availability in Females Questionnaire)
is a validated screening tool specifically in dancers (alongside
endurance athletes), not just adapted from a generic athlete population.
A dance-specific alternative (DEAQ) also exists but isn't yet externally
validated. This is a real gap: the existing "Watch for" list is an
informal symptom checklist with no named, validated instrument behind
it — the injury-prevention section already names IADMS's screening
standard, and nutrition deserved the equivalent specificity.

**Action:** Added a paragraph naming the LEAF-Q (and the DEAQ caveat) to
methodology §6, between "Watch for" and the existing dietary-patterns
paragraph, and the mirrored passage in persona.ts — framed as something
XOLOKAN can point a client's doctor/dietitian toward, not a tool XOLOKAN
administers itself, consistent with the existing referral boundary. Two
sources added.

## 2026-08-28 — jump interval training as a concrete Potentiate default

**Checked:** Warm-up & recovery (stalest topic, last touched 2026-08-19).

**Found:** A 6-month cohort study in female dancers found that using jump
interval training (JIT — 3 sets of 30-second bilateral squat jumps) as
the RAMP protocol's Potentiate content produced significantly better
long-term gains in aerobic capacity, isometric strength, and jump power
(squat jump, countermovement jump) than potentiating with ballistic dance
movements instead. This closes a real specificity gap: the existing RAMP
description leaves Potentiate as "a few submaximal jumps or
accelerations" with no concrete default, and this gives one, specifically
for power/reactive-jump days.

**Action:** Added a JIT paragraph to methodology §2 (right after the RAMP
steps) and the mirrored passage in persona.ts, framed as a concrete
option for the Potentiate step on Day 1/Day 3, not a change to RAMP
itself. One source added.

---

## 2026-08-26 — pair balance training with plyometric work generally

**Checked:** Plyometrics (stalest topic, last touched 2026-08-18).

**Found:** A 12-week study in college dancers found combined balance +
plyometric training outperformed plyometric training alone at improving
dynamic balance and reducing single-leg landing instability (measured via
center-of-pressure displacement) — a genuine additive effect. This
extends the existing standing rule #4 (prior ankle sprain gets
proprioceptive work), which only applied balance training as a corrective
for clients with an injury history — this new evidence supports pairing
balance work with plyometric volume more generally, for any jump-heavy
artist, not just as post-injury remediation.

**Action:** Added a paragraph to methodology §4 (plyometric dosage
section, right before Standing Rules) and the mirrored passage in
persona.ts, framing balance training as a default pairing with Day 3
plyometric work rather than only a corrective for prior-sprain clients.
One source added.

## 2026-08-25 — isometric hold intensity for tendon adaptation

**Checked:** Calisthenics/relative strength (stalest topic, last touched
2026-08-17).

**Found:** Research on isometric training and tendon adaptation found
high-intensity holds (≥70% MVC) are what's needed to meaningfully improve
tendon stiffness and structure, with longer muscle lengths favoring the
muscle-morphology side of the adaptation — genuinely hard holds, not a
passive static position. This is a real gap: the existing calisthenics
section prescribes isometric holds (support holds, L-sit progressions,
wall handstand holds, deep squat holds) for weak-leverage control but
never specified effort level, which matters for whether the hold actually
drives adaptation or is just time spent in a position.

**Action:** Added an effort-level specification to the isometrics bullet
in methodology §3 and the mirrored passage in persona.ts: coach these
holds as a real working effort with a clear RIR, same as any other
prescribed set, not "hold as long as you can." One source added.

## 2026-08-24 — balancing note: block periodization's edge in trained athletes

**Checked:** Periodization (stalest topic, last touched 2026-08-16 — the
same pass that added the honest caveat this entry now balances).

**Found:** A 2026 randomized crossover study in experienced
high-intensity-functional-training athletes found concentrating load into
blocks produced more favorable max-strength outcomes than an
evenly-distributed traditional periodized model, without compromising
conditioning. This is a different, narrower comparison than the existing
08-16 caveat (block vs. plain progressive overload in a general
population) — this one is block vs. another periodized structure, in
trained athletes specifically — so it doesn't contradict that caveat, it
adds a point actually in block periodization's favor for the population
this method actually serves (professional/pre-professional performers,
closer to "trained athlete" than "general population beginner").

**Action:** Added a balancing-note paragraph directly after the 08-16
caveat in methodology §1 and the mirrored passage in persona.ts, framed
explicitly as a different comparison rather than a reversal. One source
added.

## 2026-08-23 — pelvic floor risk in gymnasts from impact, not just lifting

**Checked:** Gymnast/aerialist-specific injury prevention (stalest topic,
last touched 2026-08-15).

**Found:** The existing pelvic floor bullet (§7, demographic factors)
already covered heavy-lifting and jump-landing intra-abdominal pressure
generically, but had no gymnast-specific detail. Research on rhythmic
gymnasts specifically found urinary incontinence prevalence above 30% in
young, nulliparous athletes — driven by repetitive high-impact landing
alone, no lifting required — and that most gymnasts had no prior
knowledge of the pelvic floor at all. A cluster-RCT also found basic PFM
warm-up training did *not* meaningfully reduce UI bother in this
population over 8 months — an honest caveat against overselling "the
Knack" cue as a proven fix for high-impact-specific exposure.

**Action:** Extended the existing pelvic floor bullet in methodology §7
and the mirrored passage in persona.ts with gymnast/aerialist-specific
prevalence, the knowledge-gap point (worth raising proactively, not
assuming it's known), and the null-RCT caveat reinforcing the referral-out
boundary. Three sources added.

## 2026-08-22 — prioritize balance testing in the preseason screen

**Checked:** Dance-injury prevention (stalest topic, last touched
2026-08-14).

**Found:** A study of preprofessional ballet dancers found no significant
association between injury and several commonly-used screening measures
(ankle/hip range of motion, active straight leg raise, Y Balance Test
reach distances) — but balance-specific measures did show a protective
effect, more so with more training years. This refines rather than
contradicts the existing IADMS screening guidance: the methodology
already calls for a pre-season baseline screen but treats it generically
("strength/balance benchmarks") without saying which measures actually
carry injury-prediction value.

**Action:** Added a paragraph to methodology §4 (right after the existing
"Screening, not just training" passage) and the mirrored addition in
persona.ts: weight balance/proprioceptive testing as the higher-priority
baseline measure rather than an equal-weighted checklist item alongside
ROM-based screens. One source added.

## 2026-08-21 — correction: RIR accuracy doesn't track training experience

**Checked:** RPE/autoregulation (stalest topic, last touched 2026-08-13 —
the same pass that originally added the "RIR accuracy improves with
training experience" caveat this entry now corrects).

**Found:** Two studies directly contradict that earlier caveat. A
purpose-built experienced-vs-novice comparison (≥18 months training vs.
<18 months, back squat, objectively verified via bar velocity) found *no*
significant difference in RIR-estimation accuracy between the groups. A
separate 2025 study found RIR accuracy varies hugely person-to-person
with no clear training-experience effect either. This is a real
correction, not just an addition — the 08-13 entry's framing ("novices
need more conservative coaching, experienced lifters are more reliable")
isn't well supported by this more direct, targeted evidence.

**Action:** Corrected the caveat in methodology §1 (autoregulation
subsection) and the mirrored passage in persona.ts: RIR accuracy is
framed as individual and not experience-gated, so coach it explicitly for
every client regardless of training age, and calibrate against each
client's actual performance rather than assuming reliability scales with
experience. Explicitly marked as a correction to the prior entry, not a
silent overwrite. Two sources added.

## 2026-08-20 — where dancers actually get nutrition advice

**Checked:** Nutrition for performers (stalest topic, last touched
2026-08-12).

**Found:** A 2026 scoping review on dancers' nutrition knowledge found
they overwhelmingly source dietary advice from peers (65.7%) or friends
(57.1%) rather than credentialed sources, and over a third (37.1%) follow
a restrictive diet (vegan, pescatarian, lactose-free, etc.), often
self-adopted rather than clinically supervised. This is a real, practical
gap: the existing nutrition section gives baseline macronutrient targets
but never addressed that a client's actual starting diet may already be
restrictive in a way that makes those targets harder to hit, or that
peer-sourced misinformation is the norm rather than an edge case in this
population.

**Action:** Added a paragraph to methodology §6 (between "Watch for" and
the referral "Boundary") on asking about existing dietary patterns rather
than assuming a clean slate, and the mirrored addition in persona.ts. One
source added.

## 2026-08-19 — strategic napping as a recovery tool

**Checked:** Warm-up & recovery (tied stalest at 2026-08-12 along with
nutrition for performers). Also checked whether the RAMP protocol's
Potentiate phase had new dosing specifics — an 8-week targeted-potentiation
study on female police officers turned up, but it's a different population
and application (change-of-direction under load) with no clear
translation to this methodology's existing Potentiate guidance, so no
action there.

**Found:** Two 2026 meta-analyses on daytime napping in athletes: on top
of normal nocturnal sleep, napping produces a large improvement in
endurance performance, a moderate improvement in agility, and
significantly reduces fatigue and perceived exertion during and after
exercise. Dosing specifics: keep naps to 30 minutes or less (longer risks
sleep inertia) and schedule early afternoon (roughly 1-3:30pm), where
supporting trials consistently placed them. This is a real gap: the
existing sleep guidance only covered nighttime sleep target and treating
sleep debt as a volume-reduction trigger — nothing on napping as an
actionable tool for a population with genuinely irregular rehearsal/
performance schedules that often can't fix sleep debt with nighttime
sleep alone.

**Action:** Added a napping paragraph directly after the existing sleep
guidance in methodology §2 and the mirrored passage in persona.ts, framed
as additive to the nighttime target, not a substitute. Two sources added.

## 2026-08-18 — plyometric microdosing option for heavy rehearsal weeks

**Checked:** Plyometrics (stalest topic, last touched 2026-08-11).

**Found:** A 2025 RCT compared microdosed plyometric training (4x/week,
~100 jumps/session, 400 total) against a concentrated high-dose schedule
(2x/week, ~200 jumps/session, 800 total) in athletes and found no
difference in reactive strength, jump, or sprint gains — the microdosed
group matched the high-dose group's results at half the total volume.
This is directly actionable for this population: artist-athletes
regularly stack conditioning on top of rehearsal/performance load, and
the existing plyometric dosage section only offered one schedule shape
(concentrated 2-3x/week). This adds a legitimate, evidence-backed
alternative for weeks when total load needs to come down.

**Action:** Added a microdosing-option paragraph to the plyometric dosage
section in methodology §4 and the mirrored passage in persona.ts, framed
as an adjustment option, not a replacement for the default concentrated
schedule. One source added.

## 2026-08-17 — unilateral training performance evidence for the standing rule

**Checked:** Calisthenics/relative strength (tied stalest at 2026-08-11
along with plyometrics). Initial searches on general bodyweight-hypertrophy
research and advanced lower-body bodyweight progression turned up nothing
new or citable beyond what's already covered (Schoenfeld load-independent
hypertrophy) or non-rigorous blog content — a unilateral-vs-bilateral
training angle turned up two real 2025/2026 meta-analyses instead.

**Found:** Two meta-analyses (Sports Medicine 2025; BMC Sports Science,
Medicine and Rehabilitation 2026) found unilateral training specifically
improves unilateral strength and unilateral jump performance over
bilateral training, with equivalent hypertrophy either way. The
methodology's standing rule #1 (single-leg/unilateral work every week) was
justified only by landing-mechanics/asymmetry injury-prevention reasoning
— this adds direct performance-transfer evidence for a jump-heavy artist
population specifically.

**Action:** Added the finding to standing rule #1 in methodology §4 and
the mirrored bullet in persona.ts, framing unilateral work as the more
specific tool for single-leg jump/landing skill, not just injury
prevention. Two sources added.

## 2026-08-16 — honest caveat on block periodization vs. progressive overload

**Checked:** Periodization (tied stalest at 2026-08-11 along with
calisthenics and plyometrics).

**Found:** The full ACSM 2026 position stand (already cited for effort
landmarks, but not for this finding) pools 137 systematic reviews and
30,000+ adults and found periodization models — linear, undulating, or
block — don't consistently outperform each other or plain progressive
overload on strength/hypertrophy for a general population. This is a real
gap: the methodology asserts block periodization (Verkhoshansky/Issurin)
as the structural foundation without ever addressing the "why not just
add weight every week" question against current evidence, and the honest
answer isn't a hypertrophy advantage — it's fatigue/skill-load management
for a population stacking training on top of rehearsal and performance
schedules.

**Action:** Added an honest-caveat paragraph to methodology §1 (right
after the Soviet periodization principles, before the ACSM effort
landmarks) and the mirrored passage in persona.ts, explicitly reframing
block periodization's value here as fatigue/injury management rather than
a claimed strength/hypertrophy edge — doesn't change the phase structure,
deload rule, or any programming default, just corrects the stated
rationale. One source added.

## 2026-08-15 — gymnast/aerialist shoulder injury row (ring & bar work)

**Checked:** Gymnast/aerialist-specific injury prevention (tied stalest at
2026-08-11 along with periodization, calisthenics, and plyometrics — picked
this one to keep topic diversity after two straight dance-focused entries).

**Found:** The injury table had a Wrist row for gymnast/aerialist work but
no Shoulder row, despite ring/bar work (Ring Support Hold, Wall Handstand
Hold) already being prescribed in the gymnast-aerialist archetype. A
still-rings biomechanics systematic review identifies the actual risk
profile for labral tears, rotator cuff strain, and shoulder instability in
this population: lack of shoulder internal rotation, weak external
rotation, and scapular dyskinesia — not just cumulative ring-support
volume, which is what the existing wrist row's "dose with discipline"
framing might imply applies here too without more specificity.

**Action:** Added a Shoulder (gymnast/aerialist ring & bar work) row to the
injury table in methodology §4 and the mirrored bullet in persona.ts:
screen rotation ROM/scapular control before progressing holds, prioritize
periscapular + external-rotation strengthening, load ring support
progressively (dumbbell-assisted before full bodyweight). One source
added.

## 2026-08-14 — sex-specific injury site distribution in dancers

**Checked:** Dance-injury prevention (stalest topic, last touched
2026-08-10).

**Found:** A 2025 epidemiology review found dance-injury site distribution
differs by sex beyond the ACL-risk finding already in the methodology:
female dancers are more susceptible to lower back and knee injuries, male
dancers to acute lower back and foot injuries, and male dancers also show
a higher share of craniofacial injury (19.4% vs. 13.7%) — likely a
partnering/lift exposure difference. This is new: the existing Sex section
covered ACL risk, pelvic floor, and menstrual-cycle myth-busting, but
nothing on where else to weight prehab attention by sex across the rest
of the body.

**Action:** Added a new bullet to methodology §7 (Sex subsection) and the
mirrored block in persona.ts, explicitly framed as sitting alongside the
existing ACL bullet, not replacing it. One source added.

## 2026-08-13 — RIR-accuracy-by-experience + autoregulation-vs-fixed-periodization nuance

**Checked:** RPE/autoregulation (stalest topic, last touched 2026-08-09).

**Found:** Two honest caveats not yet in the methodology, both refining
rather than contradicting the existing APRE/RIR guidance: (1) self-reported
RIR accuracy improves with training experience, meaning novice clients
aren't yet reliable judges of "2 reps in reserve" — worth coaching more
conservatively and explicitly (bar speed, form breakdown) until that skill
develops. (2) A 10-week RCT in resistance-trained men found autoregulated
volume adjustment layered onto an already well-periodized program produced
no additional strength, power, or muscle-thickness gains over the fixed
periodized program alone — a useful check against overselling
autoregulation as a strength-gain multiplier rather than what it actually
is: a readiness/fatigue safety valve.

**Action:** Added both caveats to methodology §1 (Periodization framework,
autoregulation subsection) and the mirrored block in persona.ts. Framed as
nuance on existing guidance, not a correction — the "leave 2 in the tank"
default and APRE-for-primary-lifts guidance are unchanged. Two sources
added, both new.

## 2026-08-12 — creatine for performers + recovery-modality dosing

**Checked:** Nutrition for performers (stalest topic, last touched
2026-08-08) and, as a secondary pass, warm-up & recovery (last touched
2026-08-09).

**Found:** (1) The Nutrition & Energy Availability section covered macros
and RED-S but had zero creatine content, despite creatine being one of the
best-evidenced, safest supplements for exactly this population. Two
concrete findings closed that gap: a 42-day trial in female collegiate
dancers found increased total body water and DXA lean mass with
supplementation (direct evidence in the target demographic, not an
extrapolation from male strength-athlete data), and separate research
found a single dose of creatine measurably reduces sleep-deprivation-
induced cognitive decline (processing speed, working memory) — directly
relevant since the methodology already treats sleep debt as a
training-load variable. (2) On recovery modality: a 2025 RCT found
percussion massage outperforms static stretching for DOMS recovery, and a
2025 network meta-analysis pinned the effective cold water immersion dose
at 10-15 minutes (shorter soaks are largely symbolic) — new, specific,
citable numbers beyond the existing generic "static stretching belongs in
cooldown" line.

**Action:** Added a Creatine paragraph to methodology §6 (Nutrition &
Energy Availability) and persona.ts section 5, with standard protocol
(3-5 g/day monohydrate, no loading phase). Added a brief recovery-modality
note (percussion massage vs. static stretching, cold water immersion
dosing) to methodology §2's warm-up/cooldown passage and persona.ts's
mirrored RAMP bullet, framed as optional refinements, not a change to the
non-negotiable RAMP protocol. Four sources added. Both incremental edits,
scoped to the existing sections — no restructuring.

## 2026-08-11 — plyometric dosing mechanism + gymnast spondylolysis

**Checked:** Plyometrics (untouched since the original baseline build — no
dedicated daily pass had revisited it) and gymnast/aerialist-specific
injury prevention (last touched 2026-08-08, for wrist only).

**Found:** (1) A 2025/2026 dosing consensus for plyometrics: tendons adapt
slower than muscle, which is the mechanistic reason for the existing
48-72h spacing rule (not just a conservative default), plus a 4-6 week
block-progression framing and a concrete landing cue (heel stays high,
short amortization — a long amortization phase bleeds the elastic energy
the training is supposed to build). (2) Spondylolysis (pars interarticularis
stress fracture) is the dominant cause of low back pain in adolescent/young
gymnasts specifically — a real gap, since the methodology's lower-back row
only covered the generic dancer mechanism (disc/muscle strain from axial
loading). Spondylolysis is driven by repetitive spinal hyperextension +
rotation (backbends, walkovers, aerial arch work) instead, and needs deep
trunk/lumbar stabilization in a neutral spine, not generic core work.

**Action:** Added the tendon-adaptation rationale, block-progression
framing, and landing cue to the plyometric dosage section (methodology +
persona). Added a second, gymnast-specific Lower Back row to the injury
table (methodology + persona) alongside the existing generic one, making
clear it's a different mechanism requiring a different countermeasure.
Both incremental, six sources added.

## 2026-08-10 (later) — age & sex as demographic programming factors (user-requested)

**Checked:** Requested by Oscar, not the daily rotation — build age range
(20-25/25-30/30-35/35-40) and anatomical sex (female/male) into the
generator as real programming factors, not just documentation. Researched
fresh and independently for this project: bone-density age curves, tendon/
connective-tissue adaptation timelines, training-age recovery research,
ACL injury risk and Q-angle/landing-mechanics differences by sex, pelvic
floor dysfunction in young female strength athletes specifically, relative
vs. absolute strength gains by sex, and the current menstrual-cycle-and-
performance evidence base.

**Found:** (1) Peak bone mass hits ~25.7y (men) / ~24.8y (women), then
plateaus for decades — makes 20-25/25-30 the highest-leverage window for
heavy compound loading. (2) Recovery capacity declines gradually from the
early-to-mid 30s, ~10-20% longer regeneration windows by 35-40 (hormonal,
satellite cell, sleep-architecture factors) — a pacing adjustment, not a
capability cliff. (3) ACL injury risk is 3-8x higher in women (Q-angle +
quad-dominant landing pattern), directly actionable via posterior-chain/
hip-abductor work and landing cues. (4) Pelvic floor dysfunction is
significantly prevalent in young female strength athletes specifically —
not just postpartum/older populations, which is a common and incorrect
assumption. (5) A 2023 umbrella review (top of the evidence hierarchy)
found no reliable menstrual-cycle-phase effect on strength performance or
adaptation — cycle-syncing programming is not evidence-supported. (6)
Women show greater *relative* strength gains than men despite smaller
absolute ones — validates the method's existing relative-strength-as-
primary-metric framework as sex-fair by design already.

**Action:** Added `ageRange` and `sex` as required `ClientIntake` fields
(`programSchema.ts`), a new `demographics.ts` module producing age/sex
notes plus a sex-specific corrective exercise (Banded Lateral Walk, ACL
prehab) for female clients, wired into `generateProgram()` — every program
now carries `demographicNotes` and the corrective is inserted
automatically. Updated the SDK tool schema, CLI, methodology doc (new §7),
and persona to match. All 3 archetypes x both sexes x all 4 age brackets
smoke-tested. The 30-Day Foundation PDF's fixed demographic default
(female, 25-30) is now an explicit, documented product decision rather
than an implicit CLI default — see `docs/business/PRODUCT_CHANGELOG.md`.

**Framing note:** the sex field is explicitly documented as
anatomical/biomechanical (tied to Q-angle, ACL risk, pelvic floor
anatomy), not a claim about ability, preference, or identity — worth
preserving that framing in any future edits to this content.

**Also completed (standing practice):** full contamination scan across
repo source and both regenerated PDFs. Clean.

## 2026-08-11 — block periodization lineage + load-independent hypertrophy

**Checked:** Periodization and calisthenics/relative strength — both only
touched at baseline (2026-08-08), never revisited since, unlike every other
topic in the rotation which has had a dedicated pass in the last two days.

**Found:** (1) Vladimir Issurin systematized Verkhoshansky's block concept
into three named blocks — Accumulation, Transmutation, Realization — which
map almost exactly onto XOLOKAN's Base Strength & Control / Power & Volume
/ Peak Performance phases. The methodology cited Matveyev vs. Verkhoshansky
already but hadn't credited the specific three-block structure it actually
uses. (2) Schoenfeld et al.'s meta-analysis: low-load (<=60% 1RM-equivalent)
resistance training taken close to failure builds hypertrophy comparably to
high-load training — max strength still favors heavy loads, but muscle
growth doesn't require them. Directly validates that bodyweight-only
programming isn't a lesser version of the method, it's evidence-supported.

**Action:** Added Issurin's block terminology to §1's Origins paragraph,
mapping each block to its XOLOKAN phase and stating the sequencing
principle explicitly (each block depends on the residual effect of the one
before it — the real reason phase order can't be skipped). Added a
load-independent hypertrophy callout to §3 (methodology + persona), citing
Schoenfeld directly. Both incremental, no restructuring — two sources
added.

## 2026-08-10 — dance injury prevention deep dive (user-requested)

**Checked:** Requested by Oscar, not the daily rotation — a deeper look at
structured dance injury prevention protocols and screening standards,
beyond the risk-factor studies already cited.

**Found:** (1) The first prospective RCT of an injury prevention program in
professional ballet (Houston Ballet, 2020): a strength-focused 30-min
program 3x/week for 52 weeks cut injury rate 82% and extended time between
injuries 45% — direct validation of XOLOKAN's existing strength-first,
RAMP-over-static-stretch bias, not just a generic best practice. (2) IADMS
(International Association for Dance Medicine & Science) is the field's
standard-setting body for injury screening — its Standard Measures
Initiative calls for pre-season baseline screening, which the methodology
didn't explicitly frame as part of program design before this. (3)
Concrete epidemiology: ankle sprains at 0.27/1000h in elite ballet (~13-14
days lost each), ACL injuries with 92% occurring on single-leg jump
landings — reinforces existing ankle/knee content with real numbers. (4) A
genuine gap: ankle sprain *recurrence* is driven by degraded
proprioception, not just weakness — the existing ankle countermeasure
(isometric + eccentric + plyometric) doesn't address this; prior-sprain
clients need balance/joint-reposition-sense work specifically.

**Action:** Added a validating-evidence callout and IADMS screening
principle to §4 opening, updated the Ankle and Knee table rows with the
epidemiology, added a new Standing Rule (#4) and checklist item for
proprioceptive work after a prior ankle sprain, and added an IADMS-based
baseline-screening item as checklist item #1 (previously the checklist
started at "establish phase" with no screening step). All cited, all
incremental — six sources added.

**Also completed (explicit request):** A full repo + generated-PDF scan
for any Brace Life Studios / ICONS content bleeding into XOLO FITNESS
material, following the tagline mixup caught last session. Scanned repo
source (grep across all files for brand terms, hex codes, client names,
script names) and the actual generated PDF's extracted text. Result:
clean — no contamination found anywhere, including git history commit
messages.

## 2026-08-09 — autoregulation method ranking + sleep as recovery baseline

**Checked:** RPE/autoregulation (previously only touched briefly inside the
ACSM effort-landmarks table, no dedicated look at which method is best) and
warm-up & recovery (RAMP covered warm-up already; sleep/recovery specifically
was only a passing mention, no target or rationale).

**Found:** (1) A 2025 systematic review and network meta-analysis ranking
autoregulation methods for max-strength gains: APRE (Autoregulating
Progressive Resistance Exercise — test-set-driven load adjustment) ranked
highest, ahead of plain RPE, velocity-based training, and fixed-percentage
programming. (2) Sleep research confirming deep/slow-wave sleep specifically
(not just total sleep time) is where growth hormone release, protein
synthesis, and collagen/connective-tissue repair concentrate — supports a
concrete 7-9 hour target and treating sleep debt as a volume-reduction
trigger.

**Action:** Added an APRE recommendation to §1 (methodology + persona) for
primary-lift load adjustment specifically, keeping RPE/RIR as the simpler
default elsewhere. Added a sleep subsection to §2 (methodology + persona)
with a concrete duration target and the volume-reduction-trigger framing.
Both cited, both incremental — no restructuring.

## 2026-08-08 — gymnast/aerialist injury prevention + performer nutrition

**Checked:** Gymnast/aerialist-specific injury prevention (previously
unaddressed — the injury table only covered ankle/knee/lower-back/hip) and
nutrition for performers (previously not in the methodology's scope at
all).

**Found:** (1) A 2026 systematic review of 185,107 gymnasts found 53%
pooled wrist pain prevalence, with decreased shoulder ROM identified as a
risk factor alongside training intensity/volume — a real gap since the
gymnast-aerialist archetype already emphasizes "shoulder/wrist resilience"
in the product catalog but the methodology never actually addressed wrist
injury. (2) Dance-specific RED-S (Relative Energy Deficiency in Sport)
research: one study found 65% of vocational ballet students at risk of
RED-S, with concrete macronutrient/energy-floor targets available.

**Action:** Added a Wrist row to the §4 injury table (methodology + persona)
tied to the shoulder-ROM link, and a new §6 "Nutrition & Energy Availability"
section with baseline macro targets and RED-S watch-for signs, boundaried
the same way as the injury-referral rule. Both cited, both incremental.

**Follow-up not done today (scope discipline):** `archetypes.ts`'s
gymnast-aerialist prehab focus is still `["hip", "ankle"]` — doesn't yet
include `"wrist"` as a formal injury flag in `programSchema.ts`, so the
program generator can't auto-insert wrist prehab yet even though the
methodology now covers it. Worth a small follow-up PR to add `"wrist"` to
the injury-flag enum and a corrective exercise mapping, separate from this
research pass.

## 2026-08-08 — baseline

**Checked:** Initial methodology build. Full source list as of this date is
in `docs/methodology/XOLOKAN_METHODOLOGY.md`'s Sources section (14 cited
studies across periodization, ACSM 2026 guidelines, dance injury prevention,
plyometric dosage, and RAMP warm-up protocol).

**Found:** N/A — baseline entry. Future entries log incremental findings
only, not the full source list.

**Action:** Baseline established. Daily research pass begins from here.
