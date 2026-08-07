const log = document.getElementById("log");
const form = document.getElementById("composer");
const input = document.getElementById("input");

let conversationId = null;

function addMessage(role, text) {
  const el = document.createElement("div");
  el.className = `msg ${role}`;
  el.textContent = text;
  log.appendChild(el);
  log.scrollTop = log.scrollHeight;
}

form.addEventListener("submit", async (e) => {
  e.preventDefault();
  const message = input.value.trim();
  if (!message) return;

  addMessage("user", message);
  input.value = "";

  const res = await fetch("/api/chat", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ conversationId, message }),
  });

  if (!res.ok) {
    addMessage("xolokan", "XOLOKAN hit an error. Try again.");
    return;
  }

  const data = await res.json();
  conversationId = data.conversationId;
  addMessage("xolokan", data.reply);
});
