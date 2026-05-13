# Ghost Research — Autonomous Marketing System

Hi Shreyanshi. This folder is your AI marketing team for **Ghost Research**, the world's first AI-native market research agency. Each "agent" is a skill — a set of instructions Claude follows when you ask for that task. You don't need to know how the skills work inside; you just type a command and Claude runs the right one.

---

## About the brand (pre-loaded — Claude already knows this)

**Ghost Research** is positioned as a credentialed research institution where AI precision meets human expertise — powered by Caspr.ai, with every report expert-vetted. Reports sell at ~$500. Custom research is delivered within 24 hours. Target markets: US, Europe, India, Middle East.

**Brand voice** (every ad must respect):
- ✅ Use: precise, authoritative, evidence-based, expert-verified, AI-native, depth, insight, strategic
- ❌ Never use: game-changing, revolutionary, disrupting, unlock, supercharge — anything that sounds like a SaaS growth hack

**Visual identity** (every ad must respect):
- Primary red `#EF4444` for CTAs and accents (one focal point per frame)
- Deep indigo / navy backgrounds (`#181650` → `#06062D` gradient)
- Light backgrounds: `#F8F8FF`, `#F1F3FF`
- Fonts: Oranienbaum (serif) for headlines, Manrope for body
- Imagery: real professionals with data, dashboards, charts — color-graded to deep indigo
- ❌ Forbidden: robots, AI clichés, glowing nodes, holograms, neon, high-fives, AI-generated faces, sci-fi UI

---

## What this system does

Every Ghost Research report runs through this loop:

1. **Researches** the market and finds report topics worth ~$500 to your buyer
2. **Scores** them by Ghost brand fit + market potential
3. **Writes the campaign brief** — your existing skill, locked to a $500 hard budget cap, 2-week structure, dynamically-selected platforms (IG / X / Facebook / LinkedIn), feasibility math, day-by-day calendar, full copy vault, KPI dashboard, and a kill switch
4. **Designs ad concepts** — expands the brief's 3 hooks into 8–12 Ghost-branded visual concepts (no robots, deep indigo grade, real professionals with data)
5. **Writes generation prompts** — ready-to-paste Veo 3 + nanobanana + ElevenLabs prompts that bake in Ghost brand rules
6. **Preps the launch** — pre-flight checklist (the critical OG meta tag fix, pixels, audiences, UTMs) and click-by-click Ads Manager guide
7. **Reviews performance** — pulls live data via your Supermetrics integration, compares to brief targets
8. **Decides** — SCALE / HOLD / REGENERATE / KILL per ad, applies the brief's Kill Switch when triggered, writes lessons.md so next round learns

---

## How to use it

Open this folder in Claude Code, then type any of these:

| What you want | Type this |
|---|---|
| Run the whole pipeline end-to-end | `/ghost` |
| Find new report topics | `/research-topics` |
| Score the topics you found | `/score-topics` |
| Write the 2-week campaign brief | `/make-proposal` |
| Design ad concepts from the brief | `/design-ads` |
| Write Veo 3 / nanobanana / ElevenLabs prompts | `/write-prompts` |
| Prep technical setup + Ads Manager checklist | `/prep-campaign` |
| Review how live ads are performing | `/review-ads` |
| Get a recommendation on what to do next | `/decide-action` |

Or describe what you want in plain English — Claude will pick the right skill.

---

## Where everything is saved

```
Ghost research/
├── CLAUDE.md                  ← this file
├── .claude/skills/            ← the 9 agents (don't edit unless tweaking)
└── data/
    ├── opportunities/         ← topics the researcher found, one file each
    ├── proposals/             ← one folder per report:
    │   └── <slug>/
    │       ├── campaign-brief.md     (output of /make-proposal — full strategy)
    │       ├── visual-concepts.md    (output of /design-ads)
    │       ├── prompts.md            (output of /write-prompts)
    │       ├── launch-checklist.md   (output of /prep-campaign)
    │       ├── assets/               (you save generated videos/images here)
    │       ├── analytics/            (snapshots from /review-ads)
    │       ├── decisions/            (recommendations from /decide-action)
    │       └── lessons.md            (what failed → fed to next /design-ads round)
    ├── memory/
    │   ├── winning-patterns.md       (cross-report — what's worked)
    │   └── losing-patterns.md        (cross-report — what's flopped)
    └── pipeline.md            ← bird's-eye view of every report and its stage
```

You can open any file in Notepad / Word / any editor.

---

## The full pipeline visualized

```
   /research-topics  ──▶  8-12 candidates (Ghost-publishable, AI-native, B2B)
        ↓
   /score-topics     ──▶  ranked by Ghost brand fit + market potential
        ↓
   👋 PAUSE — confirm which topic, give publish date + geography
        ↓
   /make-proposal    ──▶  full 2-week $500 brief: hooks, day-by-day, copy, KPIs, kill switch
        ↓
   /design-ads       ──▶  8-12 Ghost-branded visual concepts (no robots, deep indigo)
        ↓
   /write-prompts    ──▶  Veo 3 + nanobanana + ElevenLabs prompts
        ↓
   /prep-campaign    ──▶  pre-flight checklist + Ads Manager click-by-click
        ↓
   👋 YOU: generate assets, composite, publish (~3-4 hours of manual work)
        ↓
   (Day 3 / 7 / 10 / 14)
   /review-ads       ──▶  pulls Supermetrics data, compares to brief targets
        ↓
   /decide-action    ──▶  SCALE / HOLD / REGENERATE / KILL + lessons.md
        ↓
   (if regenerate)   loops back to /design-ads with lessons baked in
```

---

## What's fully automatic vs needs your hands

| Step | Automatic? |
|---|---|
| Research, scoring, campaign brief, ad concepts, prompts, launch checklist, decisions | ✅ Claude does it |
| Pulling ad performance numbers | ✅ Claude does it (via Supermetrics MCP — already connected) |
| Generating actual videos/images from prompts | ⚠️ You paste prompts into Veo 3 + nanobanana |
| Compositing final ads (headline + CTA overlay) | ⚠️ You do this in Figma / Canva / Premiere |
| Publishing ads to Ads Managers | ⚠️ You follow the launch-checklist.md in each platform |

The manual steps can be automated later (separate API integration project). Everything else is autonomous today.

---

## How the "self-healing" loop works

When `/decide-action` recommends **REGENERATE**, it writes a `lessons.md` file inside the proposal folder describing what failed and what to try instead. Next time `/design-ads` runs for that report, it auto-reads `lessons.md` + the cross-report `winning-patterns.md` / `losing-patterns.md` — so new creatives skip the patterns that failed and lean into what's worked elsewhere.

When `/decide-action` triggers the **Kill Switch** (from the brief's Section 10), it applies the protocol verbatim — no soft-pedaling.

---

## A reminder: $500 hard cap

Every campaign is math'd against $500 total spend. Not negotiable. If you want to scale a winner after the 2 weeks, that's a new campaign decision — make it deliberately, with fresh feasibility math, not by quietly raising budgets in Ads Manager.

---

## Running on a schedule (truly autonomous)

Once you're comfortable with the manual flow, you can tell Claude:

> "Schedule /review-ads to run every Monday at 9am for the currently-live campaign"
> "Schedule /research-topics to run every other Sunday so I always have fresh ideas in the pipeline"

Claude uses the `/schedule` system to make those recurring.

---

## Getting started right now

Type `/ghost` and Claude will run the full pipeline from "nothing" to "ready-to-launch campaign" in about 10-15 minutes of automated work. Then ~3-4 hours of manual asset generation + Ads Manager setup before the campaign goes live.

Or, if you already have a specific report in mind, just type `/make-proposal` and answer the 5 input questions.
