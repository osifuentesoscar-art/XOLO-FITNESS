import type { AgeRange, BiologicalSex, ExercisePrescription } from "./programSchema.js";

/**
 * Age- and sex-based programming factors. Full research and citations live
 * in docs/methodology/XOLOKAN_METHODOLOGY.md (Demographic Factors section).
 * Keep this file's notes and that doc's summary in sync.
 */

export function getAgeNotes(ageRange: AgeRange): string[] {
  switch (ageRange) {
    case "20-25":
    case "25-30":
      return [
        "Peak bone mass is typically reached by the mid-20s and plateaus for " +
          "decades after -- this window has an outsized long-term payoff for " +
          "heavy compound loading (squat, deadlift, overhead press patterns). " +
          "Prioritize it now rather than easing in.",
      ];
    case "30-35":
      return [
        "Recovery capacity begins a gradual, normal decline from the early-to-" +
          "mid 30s. If two consecutive high-intensity sessions leave more " +
          "residual fatigue than they used to, that's expected, not a sign of " +
          "doing something wrong -- consider a deload every 3rd peak week " +
          "instead of every 4th if fatigue is accumulating faster than the " +
          "default schedule assumes.",
      ];
    case "35-40":
      return [
        "Research on training-age recovery suggests roughly 10-20% longer " +
          "regeneration windows compared to the early 20s, driven by declining " +
          "anabolic hormone levels, reduced satellite cell responsiveness, and " +
          "changes in slow-wave sleep architecture. Build the extra recovery " +
          "in rather than cutting it to hit the same weekly volume -- stronger, " +
          "well-recovered athletes at this age tolerate load spikes far better " +
          "than fatigued ones do.",
      ];
  }
}

export function getSexNotes(sex: BiologicalSex): string[] {
  if (sex === "female") {
    return [
      "ACL injury risk is 3-8x higher in women, driven by anatomical (a " +
        "greater Q-angle) and biomechanical (a more erect, quad-dominant " +
        "landing pattern with greater knee valgus) factors. Posterior chain " +
        "and hip-abductor strength plus explicit landing-mechanics cueing " +
        "(soft knees, hips back, land quiet) are the modifiable " +
        "countermeasures, and are weighted into this program accordingly.",
      "Heavy lifting and jump-landing work meaningfully raise intra-" +
        "abdominal pressure. Research on young female strength athletes " +
        "(not just postpartum or older populations) found significant rates " +
        "of pelvic floor dysfunction. Cue \"the Knack\" -- a conscious pelvic " +
        "floor contraction just before the effort -- on heavy lifts and " +
        "landings, and flag any leaking, heaviness, or pressure to a pelvic " +
        "floor physical therapist rather than pushing through it.",
      "No reliable evidence supports programming around menstrual cycle " +
        "phase (2023 umbrella review, the highest tier of evidence available). " +
        "Train at consistent intensity and autoregulate via RIR/RPE around " +
        "individual symptoms over multiple cycles, not a fixed calendar.",
    ];
  }
  return [
    "Baseline strength differs by sex, but the training response doesn't -- " +
      "this program tracks relative, bodyweight-scaled strength as its " +
      "primary metric rather than absolute load, which is the fairer " +
      "standard regardless of starting point.",
  ];
}

export function getSexCorrective(sex: BiologicalSex): ExercisePrescription | null {
  if (sex === "female") {
    return {
      name: "Banded Lateral Walk",
      sets: 3,
      reps: "12/side",
      correctivePriority: true,
    };
  }
  return null;
}
