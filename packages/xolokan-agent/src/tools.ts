import { z } from "zod";
import { createSdkMcpServer, tool } from "@anthropic-ai/claude-agent-sdk";
import { generateProgram } from "./generateProgram.js";
import {
  DisciplineSchema,
  ExperienceLevelSchema,
  EquipmentAccessSchema,
  AgeRangeSchema,
  BiologicalSexSchema,
} from "./programSchema.js";

const generateProgramTool = tool(
  "generate_program",
  "Generate a structured 12-week XOLOKAN training program (Soviet-block periodization, discipline-specific exercises, injury prehab, age- and sex-specific factors) for a client. Use this whenever asked to build, write, or put together an actual training program — do not hand-write a program in prose.",
  {
    clientName: z.string().describe("Client's name, used in the program title"),
    discipline: DisciplineSchema.describe(
      "dancer | gymnast-aerialist | general-performer"
    ),
    experienceLevel: ExperienceLevelSchema,
    ageRange: AgeRangeSchema.describe(
      "20-25 | 25-30 | 30-35 | 35-40 -- drives recovery pacing and bone-loading guidance"
    ),
    sex: BiologicalSexSchema.describe(
      "female | male -- anatomical/biomechanical, drives ACL/landing-mechanics and pelvic floor guidance for female clients specifically. Ask, don't guess."
    ),
    sessionsPerWeek: z
      .union([z.literal(3), z.literal(4), z.literal(5), z.literal(6)])
      .describe("Training days per week, 3-6"),
    equipmentAccess: EquipmentAccessSchema,
    injuryFlags: z
      .array(z.enum(["ankle", "knee", "lower-back", "hip"]))
      .default([])
      .describe("Any known injury history or areas to prioritize prehab for"),
  },
  async (args) => {
    const program = generateProgram(args);
    return {
      content: [{ type: "text", text: JSON.stringify(program, null, 2) }],
    };
  }
);

export const xolokanProgramServer = createSdkMcpServer({
  name: "xolokan-programs",
  version: "1.0.0",
  tools: [generateProgramTool],
});

export const XOLOKAN_ALLOWED_TOOLS = ["mcp__xolokan-programs__generate_program"];
