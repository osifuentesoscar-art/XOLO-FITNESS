import express from "express";
import { randomUUID } from "node:crypto";
import { runXolokanTurn } from "@xolo-fitness/xolokan-agent";

const app = express();
app.use(express.json());
app.use(express.static("../web"));

const sessions = new Map<string, string>();

app.post("/api/chat", async (req, res) => {
  const { conversationId, message } = req.body as {
    conversationId?: string;
    message?: string;
  };

  if (!message || typeof message !== "string") {
    res.status(400).json({ error: "message is required" });
    return;
  }

  const convId = conversationId ?? randomUUID();
  const priorSessionId = sessions.get(convId);

  try {
    const { reply, sessionId } = await runXolokanTurn(message, priorSessionId);
    if (sessionId) sessions.set(convId, sessionId);
    res.json({ conversationId: convId, reply });
  } catch (err) {
    console.error(err);
    res.status(500).json({ error: "XOLOKAN failed to respond" });
  }
});

const port = Number(process.env.PORT ?? 8787);
app.listen(port, () => {
  console.log(`XOLOKAN server listening on http://localhost:${port}`);
});
