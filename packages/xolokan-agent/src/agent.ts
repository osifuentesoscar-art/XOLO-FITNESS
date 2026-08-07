import { query } from "@anthropic-ai/claude-agent-sdk";
import { XOLOKAN_SYSTEM_PROMPT } from "./persona.js";

export interface TurnResult {
  reply: string;
  sessionId: string | undefined;
}

export async function runXolokanTurn(
  prompt: string,
  resumeSessionId?: string
): Promise<TurnResult> {
  const stream = query({
    prompt,
    options: {
      systemPrompt: XOLOKAN_SYSTEM_PROMPT,
      resume: resumeSessionId,
    },
  });

  let reply = "";
  let sessionId = resumeSessionId;

  for await (const event of stream) {
    if (event.type === "system" && event.subtype === "init") {
      sessionId = event.session_id;
    }
    if (event.type === "assistant") {
      for (const block of event.message.content) {
        if (block.type === "text") reply += block.text;
      }
    }
  }

  return { reply, sessionId };
}
