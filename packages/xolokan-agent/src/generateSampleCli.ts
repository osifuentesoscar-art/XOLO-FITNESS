import { generateProgram } from "./generateProgram.js";
import type { ClientIntake } from "./programSchema.js";

const args = process.argv.slice(2);
const get = (flag: string, fallback: string) => {
  const idx = args.indexOf(flag);
  return idx !== -1 && args[idx + 1] ? args[idx + 1] : fallback;
};

const intake: ClientIntake = {
  clientName: get("--name", "Sample Client"),
  discipline: get("--discipline", "dancer") as ClientIntake["discipline"],
  experienceLevel: get("--level", "intermediate") as ClientIntake["experienceLevel"],
  ageRange: get("--age", "25-30") as ClientIntake["ageRange"],
  sex: get("--sex", "female") as ClientIntake["sex"],
  sessionsPerWeek: Number(get("--days", "4")) as ClientIntake["sessionsPerWeek"],
  equipmentAccess: get("--equipment", "full-gym") as ClientIntake["equipmentAccess"],
  injuryFlags: get("--injuries", "")
    .split(",")
    .filter(Boolean) as ClientIntake["injuryFlags"],
};

console.log(JSON.stringify(generateProgram(intake), null, 2));
