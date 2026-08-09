import { z } from "zod";

export const DisciplineSchema = z.enum([
  "dancer",
  "gymnast-aerialist",
  "general-performer",
]);
export type Discipline = z.infer<typeof DisciplineSchema>;

export const ExperienceLevelSchema = z.enum([
  "beginner",
  "intermediate",
  "advanced",
]);
export type ExperienceLevel = z.infer<typeof ExperienceLevelSchema>;

export const EquipmentAccessSchema = z.enum(["full-gym", "bodyweight-only"]);
export type EquipmentAccess = z.infer<typeof EquipmentAccessSchema>;

export const PhaseSchema = z.enum(["base", "power-volume", "peak"]);
export type Phase = z.infer<typeof PhaseSchema>;

export const ClientIntakeSchema = z.object({
  clientName: z.string(),
  discipline: DisciplineSchema,
  experienceLevel: ExperienceLevelSchema,
  sessionsPerWeek: z.union([z.literal(3), z.literal(4), z.literal(5), z.literal(6)]),
  equipmentAccess: EquipmentAccessSchema,
  injuryFlags: z.array(z.enum(["ankle", "knee", "lower-back", "hip"])).default([]),
});
export type ClientIntake = z.infer<typeof ClientIntakeSchema>;

export interface ExercisePrescription {
  name: string;
  sets: number;
  reps: string;
  bodyweightAlt?: string;
  /** Only used when bodyweightAlt is set and the alt needs a different
   * volume than the loaded exercise (e.g. a jump substitution shouldn't
   * inherit a kettlebell-swing rep scheme). Falls back to sets/reps above
   * when omitted. */
  bodyweightAltSets?: number;
  bodyweightAltReps?: string;
  correctivePriority?: boolean;
}

export interface ProgramDay {
  dayNumber: number;
  focus: string;
  exercises: ExercisePrescription[];
  mobilitySession: boolean;
}

export interface ProgramWeek {
  weekNumber: number;
  phase: Phase;
  intensity: string;
  isDeload: boolean;
  days: ProgramDay[];
}

export interface GeneratedProgram {
  title: string;
  archetypeId: Discipline;
  client: ClientIntake;
  weeks: ProgramWeek[];
  prehabFocus: string[];
  disclaimers: string[];
}
