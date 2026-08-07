import { createInterface } from "node:readline/promises";
import { stdin, stdout } from "node:process";
import { runXolokanTurn } from "./agent.js";

async function main() {
  const rl = createInterface({ input: stdin, output: stdout });
  let sessionId: string | undefined;

  console.log("XOLOKAN — XOLO FITNESS AI coach. Type 'exit' to quit.\n");

  while (true) {
    const userInput = await rl.question("you> ");
    if (userInput.trim().toLowerCase() === "exit") break;

    const { reply, sessionId: nextSessionId } = await runXolokanTurn(userInput, sessionId);
    sessionId = nextSessionId;
    console.log(`xolokan> ${reply}\n`);
  }

  rl.close();
}

main().catch((err) => {
  console.error(err);
  process.exit(1);
});
