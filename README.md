# XOLO FITNESS

A standalone project — separate from any other client/brand work — for **XOLO
FITNESS**, a performance-coaching brand founded by **Oscar "Xolo" Sifuentes
Jr**. This repo houses **XOLOKAN**, an AI performance-coach agent built on the
Claude Agent SDK, plus a minimal server + web chat UI to talk to it.

## Brand background (researched, not assumed)

- **Founder**: Oscar "Xolo" Sifuentes Jr — performance coach and movement
  specialist, 10+ years in athletic performance, physical education, and
  professional performance arts (dance/choreography/movement direction for
  touring artists including Pharrell Williams, Travis Scott, Mariah Angeliq,
  Ali Gatie).
- **Founded**: 2021, as XOLO FITNESS LLC.
- **Mission**: impact and improve every client's daily quality of life
  through a nutritious, health-conscious approach that treats mental and
  physical strength as equally important. Programs span beginner to
  professional-athlete level.
- **Methodology**: strength development + advanced calisthenics + athletic
  conditioning + recovery science + breathwork.
- **Audience**: artists, dancers, performers, athletes, and high-performing
  professionals whose lifestyles demand strength, endurance, agility, and
  resilience.
- **Channels**: [xolofit.com](https://www.xolofit.com) ·
  [Instagram @xolo.fitness](https://www.instagram.com/xolo.fitness) ·
  [YouTube](https://www.youtube.com/channel/UCbmfaWCzDVGMrZmXcCagh5w) ·
  founder's personal Instagram [@oscarxsifuentes](https://www.instagram.com/oscarxsifuentes)
- **Brand assets**: logos and video content live in the team Dropbox under
  `XOLO FITNESS BRAND` and `LOGOS` — mostly promo/recovery/workout video, no
  written brand voice doc existed yet, so the persona below was synthesized
  from the mission/methodology copy on xolofit.com and the coaches page.

Note: direct fetches to `xolofit.com`, Instagram, and YouTube were blocked by
this environment's network egress proxy, so the above is assembled from
indexed search results, not a live crawl. Worth re-verifying against the live
site/socials when you have unrestricted access.

## What's here

```
packages/
  xolokan-agent/   XOLOKAN persona + Claude Agent SDK chat loop (CLI + library)
  server/          Express API wrapping the agent for the web UI
  web/             Minimal static chat UI
docs/methodology/
  XOLOKAN_METHODOLOGY.md   Training-science layer XOLOKAN's persona is built on
  sources/                 Source documents the methodology is built from
```

## Training methodology

XOLOKAN's programming is built on a Soviet-block periodization system (base
strength -> power/volume -> peak, 12-week cycles), layered with
calisthenics-based relative-strength training and dance/artist-athlete
injury-prevention science (ankle, knee, lower back, and hip protocols;
mandatory single-leg work; isometric control training). Full detail,
including cited research, is in
[`docs/methodology/XOLOKAN_METHODOLOGY.md`](docs/methodology/XOLOKAN_METHODOLOGY.md).
The source training documents it was built from are in
`docs/methodology/sources/`.

## Setup

```bash
npm install
cp .env.example .env   # add your ANTHROPIC_API_KEY
```

**Chat with XOLOKAN in the terminal:**
```bash
npm run chat
```

**Run the web chat UI:**
```bash
npm run dev:server
# open http://localhost:8787
```

## XOLOKAN persona

Defined in `packages/xolokan-agent/src/persona.ts`. It encodes the brand
mission, the training methodology above, target audience, and voice (direct,
disciplined, coach-energy — distinct from a clinical or luxury tone). Edit
that file to tune the agent as the brand voice solidifies.

## Status

Early scaffold — not yet deployed. Next steps to consider: pull in the real
brand voice/style guide once written, add fitness-specific tools (program
generation, exercise library lookups) to the agent, and decide on a hosting
target for the server + web UI.
