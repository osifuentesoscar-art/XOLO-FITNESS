import { ARCHETYPES, dayLabels } from "./archetypes.js";
import type {
  ClientIntake,
  ExercisePrescription,
  GeneratedProgram,
  Phase,
  ProgramDay,
  ProgramWeek,
} from "./programSchema.js";

const PHASE_BY_WEEK: Record<number, { phase: Phase; intensity: string }> = {};
for (let w = 1; w <= 4; w++) PHASE_BY_WEEK[w] = { phase: "base", intensity: "70-75%" };
for (let w = 5; w <= 8; w++) PHASE_BY_WEEK[w] = { phase: "power-volume", intensity: "75-85%" };
for (let w = 9; w <= 12; w++) PHASE_BY_WEEK[w] = { phase: "peak", intensity: "85-90%" };

const CORRECTIVE_EXERCISES: Record<string, ExercisePrescription> = {
  ankle: { name: "Ankle Eccentric Heel Drop", sets: 3, reps: "12/side", correctivePriority: true },
  knee: { name: "Terminal Knee Extension (banded)", sets: 3, reps: "15/side", correctivePriority: true },
  "lower-back": { name: "Bird Dog", sets: 3, reps: "10/side", correctivePriority: true },
  hip: { name: "Clamshell (banded)", sets: 3, reps: "15/side", correctivePriority: true },
};

function applyEquipment(
  exercises: ExercisePrescription[],
  equipmentAccess: ClientIntake["equipmentAccess"]
): ExercisePrescription[] {
  if (equipmentAccess !== "bodyweight-only") return exercises;
  return exercises.map((ex) =>
    ex.bodyweightAlt ? { ...ex, name: ex.bodyweightAlt, bodyweightAlt: undefined } : ex
  );
}

function buildDaysForWeek(client: ClientIntake): ProgramDay[] {
  const archetype = ARCHETYPES[client.discipline];
  const [day1, day2, day3, day4] = archetype.days.map((exs) => applyEquipment(exs, client.equipmentAccess));

  const extraInjuryFlags = client.injuryFlags.filter((f) => !archetype.prehabFocus.includes(f));
  const correctiveInserts = extraInjuryFlags.map((f) => CORRECTIVE_EXERCISES[f]).filter(Boolean);

  const baseDays: ProgramDay[] = [
    { dayNumber: 1, focus: dayLabels[0], exercises: day1, mobilitySession: false },
    {
      dayNumber: 2,
      focus: dayLabels[1],
      exercises: [...correctiveInserts, ...day2],
      mobilitySession: true,
    },
    { dayNumber: 3, focus: dayLabels[2], exercises: day3, mobilitySession: false },
    { dayNumber: 4, focus: dayLabels[3], exercises: day4, mobilitySession: true },
  ];

  if (client.sessionsPerWeek === 3) {
    const mergedDay3: ProgramDay = {
      dayNumber: 3,
      focus: `${dayLabels[2]} + Conditioning Finisher`,
      exercises: [...day3, ...day4.slice(0, 2)],
      mobilitySession: true,
    };
    return [baseDays[0], baseDays[1], mergedDay3];
  }

  if (client.sessionsPerWeek === 4) return baseDays;

  const supplementaryDay = (dayNumber: number): ProgramDay => ({
    dayNumber,
    focus: "Supplementary Mobility & Prehab",
    exercises: archetype.prehabFocus.map((f) => CORRECTIVE_EXERCISES[f]).filter(Boolean),
    mobilitySession: true,
  });

  if (client.sessionsPerWeek === 5) return [...baseDays, supplementaryDay(5)];

  return [...baseDays, supplementaryDay(5), supplementaryDay(6)];
}

export function generateProgram(client: ClientIntake): GeneratedProgram {
  const archetype = ARCHETYPES[client.discipline];
  const weeks: ProgramWeek[] = [];

  for (let weekNumber = 1; weekNumber <= 12; weekNumber++) {
    const { phase, intensity } = PHASE_BY_WEEK[weekNumber];
    const isDeload = phase === "peak" && weekNumber % 4 === 0;
    weeks.push({
      weekNumber,
      phase,
      intensity,
      isDeload,
      days: buildDaysForWeek(client),
    });
  }

  return {
    title: `${archetype.label} — ${client.clientName}`,
    archetypeId: client.discipline,
    client,
    weeks,
    prehabFocus: Array.from(new Set([...archetype.prehabFocus, ...client.injuryFlags])),
    disclaimers: [
      "XOLOKAN is not a medical provider. Any pain, sharp discomfort, or injury history should be referred to a doctor or physical therapist.",
      "This program does not prescribe rehabilitation beyond general mobility guidance.",
    ],
  };
}
