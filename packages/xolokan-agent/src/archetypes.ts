import type { Discipline, ExercisePrescription } from "./programSchema.js";

export interface ArchetypeDefinition {
  id: Discipline;
  label: string;
  audience: string;
  emphasis: string;
  prehabFocus: string[];
  days: [ExercisePrescription[], ExercisePrescription[], ExercisePrescription[], ExercisePrescription[]];
}

const dayLabels = [
  "Neural Speed & Power / Upper Strength",
  "Strength & Control / Lower Power",
  "Reactive Jump Training / Conditioning",
  "Athletic Endurance / Explosive Full Body",
] as const;

export { dayLabels };

export const ARCHETYPES: Record<Discipline, ArchetypeDefinition> = {
  dancer: {
    id: "dancer",
    label: "XOLOKAN Dancer Protocol",
    audience: "Professional and pre-professional dancers, choreographers, movement performers",
    emphasis:
      "Ankle resilience for jump-heavy repertoire, hip stability for held positions and extension work, isometric control for line quality.",
    prehabFocus: ["ankle", "hip"],
    days: [
      [
        { name: "Pull-Ups", sets: 5, reps: "5", bodyweightAlt: "Banded Pull-Ups" },
        { name: "Seated Overhead Press", sets: 4, reps: "6", bodyweightAlt: "Pike Push-Ups" },
        { name: "Bent-Over Row", sets: 4, reps: "8", bodyweightAlt: "Inverted Row" },
        { name: "Depth Jumps", sets: 4, reps: "3" },
        { name: "Sprint Intervals", sets: 5, reps: "30m" },
      ],
      [
        { name: "Front Squat", sets: 5, reps: "4", bodyweightAlt: "Bulgarian Split Squat" },
        { name: "Weighted Pull-Ups", sets: 5, reps: "5", bodyweightAlt: "Pull-Ups" },
        { name: "Single-Leg RDL", sets: 3, reps: "8/leg", correctivePriority: true },
        { name: "Hanging Leg Raise", sets: 4, reps: "12" },
        { name: "Copenhagen Plank", sets: 3, reps: "20-30s/side", correctivePriority: true },
      ],
      [
        { name: "Pogo Jumps", sets: 4, reps: "20" },
        { name: "Single-Leg Bounds", sets: 4, reps: "6/leg" },
        { name: "Ankle Isometric Hold (single-leg calf raise)", sets: 3, reps: "30-45s/side", correctivePriority: true },
        { name: "Lateral Skater Jumps", sets: 4, reps: "10" },
        { name: "Jump Rope", sets: 1, reps: "5 min continuous" },
      ],
      [
        { name: "Sled Push", sets: 5, reps: "30m", bodyweightAlt: "Bear Crawl Sprint" },
        { name: "Push-Ups", sets: 5, reps: "20" },
        { name: "Pull-Ups", sets: 5, reps: "10" },
        { name: "Kettlebell Swings", sets: 5, reps: "20", bodyweightAlt: "Broad Jumps", bodyweightAltSets: 4, bodyweightAltReps: "8" },
        { name: "Battle Ropes", sets: 5, reps: "30s", bodyweightAlt: "Mountain Climbers 30s" },
      ],
    ],
  },
  "gymnast-aerialist": {
    id: "gymnast-aerialist",
    label: "XOLOKAN Gymnast / Aerialist Protocol",
    audience: "Gymnasts, aerialists, circus performers, acrobats",
    emphasis:
      "Relative strength-to-bodyweight ratio, shoulder/wrist resilience for apparatus work, grip and isometric hold capacity.",
    prehabFocus: ["hip", "ankle"],
    days: [
      [
        { name: "Weighted Pull-Ups", sets: 5, reps: "5", bodyweightAlt: "Pull-Ups" },
        { name: "Ring Support Hold", sets: 4, reps: "20-30s", correctivePriority: true },
        { name: "Handstand Push-Ups", sets: 4, reps: "5-8", bodyweightAlt: "Pike Push-Ups" },
        { name: "Depth Jumps", sets: 4, reps: "3" },
        { name: "Sprint Intervals", sets: 5, reps: "30m" },
      ],
      [
        { name: "Front Squat", sets: 5, reps: "4", bodyweightAlt: "Pistol Squat Progression" },
        { name: "Dips", sets: 4, reps: "8" },
        { name: "L-Sit Progression", sets: 4, reps: "15-20s", correctivePriority: true },
        { name: "Hanging Leg Raise", sets: 4, reps: "12" },
        { name: "Farmer Carry", sets: 4, reps: "40m" },
      ],
      [
        { name: "Pogo Jumps", sets: 4, reps: "20" },
        { name: "Single-Leg Bounds", sets: 4, reps: "6/leg" },
        { name: "Ankle Isometric Hold (single-leg calf raise)", sets: 3, reps: "30-45s/side", correctivePriority: true },
        { name: "Wall Handstand Hold", sets: 4, reps: "30-45s", correctivePriority: true },
        { name: "Jump Rope", sets: 1, reps: "5 min continuous" },
      ],
      [
        { name: "Sled Push", sets: 5, reps: "30m", bodyweightAlt: "Bear Crawl Sprint" },
        { name: "Push-Ups", sets: 5, reps: "20" },
        { name: "Pull-Ups", sets: 5, reps: "10" },
        { name: "Kettlebell Swings", sets: 5, reps: "20", bodyweightAlt: "Broad Jumps", bodyweightAltSets: 4, bodyweightAltReps: "8" },
        { name: "Battle Ropes", sets: 5, reps: "30s", bodyweightAlt: "Mountain Climbers 30s" },
      ],
    ],
  },
  "general-performer": {
    id: "general-performer",
    label: "XOLOKAN Performer Protocol",
    audience: "Actors, musicians, and high-performing professionals training for stage-ready athleticism",
    emphasis:
      "Balanced strength and conditioning base, general injury resilience, work capacity for demanding rehearsal/travel schedules.",
    prehabFocus: ["lower-back", "hip"],
    days: [
      [
        { name: "Pull-Ups", sets: 4, reps: "6", bodyweightAlt: "Banded Pull-Ups" },
        { name: "Seated Overhead Press", sets: 4, reps: "8", bodyweightAlt: "Pike Push-Ups" },
        { name: "Bent-Over Row", sets: 4, reps: "10", bodyweightAlt: "Inverted Row" },
        { name: "Medicine Ball Slams", sets: 4, reps: "10" },
        { name: "Sprint Intervals", sets: 4, reps: "30m" },
      ],
      [
        { name: "Front Squat", sets: 4, reps: "6", bodyweightAlt: "Bulgarian Split Squat" },
        { name: "Weighted Pull-Ups", sets: 4, reps: "6", bodyweightAlt: "Pull-Ups" },
        { name: "Hanging Leg Raise", sets: 4, reps: "12" },
        { name: "Farmer Carry", sets: 4, reps: "40m" },
        { name: "Dead Bug", sets: 3, reps: "12/side", correctivePriority: true },
      ],
      [
        { name: "Pogo Jumps", sets: 3, reps: "20" },
        { name: "Lateral Skater Jumps", sets: 4, reps: "10" },
        { name: "Jump Rope", sets: 1, reps: "5 min continuous" },
        { name: "Hip Airplane", sets: 3, reps: "8/side", correctivePriority: true },
      ],
      [
        { name: "Sled Push", sets: 4, reps: "30m", bodyweightAlt: "Bear Crawl Sprint" },
        { name: "Push-Ups", sets: 4, reps: "20" },
        { name: "Pull-Ups", sets: 4, reps: "10" },
        { name: "Kettlebell Swings", sets: 4, reps: "20", bodyweightAlt: "Broad Jumps", bodyweightAltSets: 4, bodyweightAltReps: "8" },
      ],
    ],
  },
};
