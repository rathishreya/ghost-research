# Ghost Research — Autonomous Marketing System

Hi Shreyanshi. This folder is your AI marketing team for **Ghost Research**, the world's first AI-native market research agency. Each "agent" is a skill — a set of instructions Claude follows when you ask for that task. You don't need to know how the skills work inside; you just type a command and Claude runs the right one.

---

## About the brand (pre-loaded — Claude already knows this)

**Ghost Research** is a credentialed research institution where AI precision meets human expertise — powered by Caspr.ai, with every report expert-vetted. **Founded by Joy Sharma** (ex-McKinsey, based in Dubai) — founder POV is a usable angle on LinkedIn. Target markets: US, Europe, India, Middle East.

### Two product lines (both in scope for marketing)

| Product | Description | Typical funnel | Default working price |
|---|---|---|---|
| **Caspr. Self-Serve (off-the-shelf reports)** | Published research downloads, on-demand. The default product this pipeline markets. | Ad → report page → direct purchase | ~$500 (working benchmark) |
| **Ghost Elite (custom mandates)** | Bespoke research delivered in 24 hours. Mission-critical, often six-figure decisions. | Ad → enquiry form → human contact → custom scope → delivery | Custom (much higher) |

When you run `/make-proposal`, Claude asks which product the campaign is for. **By default, off-the-shelf campaigns also cross-sell Ghost Elite in Week 2 retargeting** — engaged prospects who didn't buy the report are exactly the audience for custom work.

### What makes Ghost Research credible (use these in ad copy)

- **1M+ curated sources** — government databases, verified trade journals, financial filings. Caspr does NOT scrape the open web indiscriminately.
- **Transparent citation** — every claim in every report is sourced. Anti-"black box" positioning.
- **Weeks → minutes** — traditional agencies take weeks; Caspr synthesizes in minutes. Ghost Elite delivers in 24 hours.
- **Human-vetted / expert-validated** — every report passes through a subject matter expert with 10+ years of domain experience before delivery.
- **Predictive, not lagging** — moves the buyer from "what happened last quarter" to "what will happen next."

### Target buyer (use this language in targeting + creative)

The site calls these buyers "Prosumers." Don't use that word in ads — too jargon-y — but target them:

- **Investment Analysts** — PE/M&A due diligence, market sizing for deal flow
- **Strategy Consultants** — partner-level and senior consultants at boutiques + Big-4 alumni shops
- **Corporate decision-makers** — VPs, Directors, Heads-of, C-suite, founders making market-entry / competitive / regulatory decisions
- **Investment Professionals** — IB, equity research, hedge funds

Geography: US / Europe / India / Middle East — weight by topic, not region. (No structural ME upweight even though the CEO is based there.)

### Sector coverage (much broader than "just AI")

Topic research and proposals should fish across all of these — not just AI-native verticals:

- Logistics, global supply chain, real estate M&A
- FinTech, investment banking, private equity due diligence
- AI adoption curves, SaaS growth forecasts, telecom infrastructure
- Healthcare regulatory shifts, medical device adoption, pharma
- Energy / commodity volatility, sustainable sourcing
- E-commerce growth, CPG innovation, retail strategy
- Defense, climate, geopolitics where relevant

**AI-native synthesis** (multi-source pattern detection that's hard for a human to do manually) is a **preference**, not a filter. A great real-estate-M&A topic is still a great Ghost topic even if the synthesis isn't AI-flavored.

### Brand voice (every ad must respect)

- ✅ Use: precise, authoritative, evidence-based, expert-verified, human-vetted, transparent citation, AI-native, depth, insight, strategic, **institutional-grade**, **boardroom-ready**, **weeks to minutes**, **mission-critical**
- ❌ Never use: game-changing, revolutionary, disrupting, unlock, supercharge — anything that sounds like a SaaS growth hack. Also avoid internal jargon like "Prosumers" or "calibrated strategic instrument" in actual ad copy.

### Visual identity (every ad must respect)

- Primary red `#EF4444` for CTAs and accents (one focal point per frame)
- Deep indigo / navy backgrounds (`#181650` → `#06062D` gradient)
- Light backgrounds: `#F8F8FF`, `#F1F3FF`
- Fonts: Oranienbaum (serif) for headlines, Manrope for body
- Imagery: real professionals with data, dashboards, charts — color-graded to deep indigo
- ❌ Forbidden: robots, AI clichés, glowing nodes, holograms, neon, high-fives, AI-generated faces, sci-fi UI

---

## 🔒 Hard structural rule for every campaign

**Week 1 = hype only. The report is NOT yet published.** Ads can talk about the *question*, the *problem*, the *category*, the *audience* — but cannot quote, excerpt, chart, or visually preview anything from inside the report. The report does not exist publicly yet.

**End of Week 1 = publish day.**

**Week 2 = ads can use actual report content.** Headline findings, charts, expert quotes, specific stats — all in scope from Day 8 onward.

This is non-negotiable. It's baked into `/make-proposal` (the calendar), `/design-ads` (the visual concepts), and `/write-prompts` (the generation prompts). Don't break it — Week 1 ads that pretend to quote a not-yet-published report damage credibility for a brand whose entire moat is "expert-vetted."

---

## What this system does

Every Ghost Research report runs through this loop:

1. **Researches** the market and finds report topics worth selling to your buyer
2. **Scores** them by Ghost brand fit + market potential (off-the-shelf OR Ghost Elite suitability)
3. **Writes the campaign brief** — your existing skill, locked to a $500 hard budget cap, 2-week structure (Week 1 hype / Week 2 reveal), dynamically-selected platforms (IG / X / Facebook / LinkedIn), feasibility math, day-by-day calendar, full copy vault, KPI dashboard, and a kill switch
4. **Designs ad concepts** — expands the brief's 3 hooks into 8–12 Ghost-branded visual concepts (no robots, deep indigo grade, real professionals with data), split between Week 1 hype-safe concepts and Week 2 content-revealing concepts
5. **Writes generation prompts** — ready-to-paste Veo 3 + nanobanana + ElevenLabs prompts that bake in Ghost brand rules
6. **Generates image assets** — runs Pollinations.ai (free FLUX) for photo/scene ads and renders editorial HTML/CSS cards (typography + stat cards) via headless Chromium. No API key required.
7. **Preps the launch** — pre-flight checklist (the critical OG meta tag fix, pixels, audiences, UTMs) and click-by-click Ads Manager guide
8. **Reviews performance** — pulls live data via your Supermetrics integration, compares to brief targets
9. **Decides** — SCALE / HOLD / REGENERATE / KILL per ad, applies the brief's Kill Switch when triggered, writes lessons.md so next round learns

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
| Write generation prompts (pollinations / editorial / animate / animated-html) | `/write-prompts` |
| Generate image assets (Pollinations + editorial cards) | `/generate-assets` |
| Generate video assets (Ken-Burns animations + animated HTML) | `/generate-video` |
| Iterate on a single ad (change something you don't like) | `/edit-ad <id> "instruction"` |
| Prep technical setup + Ads Manager checklist | `/prep-campaign` |
| Review how live ads are performing | `/review-ads` |
| Get a recommendation on what to do next | `/decide-action` |

Or describe what you want in plain English — Claude will pick the right skill.

---

## Where everything is saved

```
Ghost research/
├── CLAUDE.md                  ← this file
├── .claude/skills/            ← the Ghost agents (don't edit unless tweaking)
├── scripts/                   ← local automation helpers (e.g. Nanobanana generation)
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
   /research-topics  ──▶  8-12 candidates (off-the-shelf + Ghost Elite-fit, B2B)
        ↓
   /score-topics     ──▶  ranked by Ghost brand fit + market potential
        ↓
   👋 PAUSE — confirm which topic, which product line, publish date, geography
        ↓
   /make-proposal    ──▶  full 2-week brief: hooks, day-by-day, copy, KPIs, kill switch
                          Week 1 = hype only | Week 2 = report content live
        ↓
   /design-ads       ──▶  8-12 Ghost-branded concepts split into hype-safe + content-live
        ↓
   /write-prompts    ──▶  Veo 3 + nanobanana + ElevenLabs prompts
        ↓
   /generate-assets  ──▶  auto-generates Nanobanana image assets into assets/
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
| Static image generation (Pollinations FLUX) | ✅ Claude does it — free, no API key |
| Editorial HTML/CSS card rendering | ✅ Claude does it — free, headless Chromium |
| Short video generation (Ken-Burns animation on stills) | ✅ Claude does it — free, bundled ffmpeg |
| Animated kinetic-typography spots | ✅ Claude does it — free, Playwright recording |
| Iterating on an ad you don't like | ✅ Claude does it via `/edit-ad <id> "instruction"` |
| Pulling ad performance numbers | ✅ Claude does it (via Supermetrics MCP — already connected) |
| Photoreal video via Veo 3 (paid Google AI Studio plan) | ⚠️ Optional upgrade; free animations cover most cases |
| Compositing final headlines + CTA overlays | ⚠️ Optional — only when you want headline text baked into the asset |
| Publishing ads to Ads Managers | ⚠️ You follow the launch-checklist.md in each platform |

The whole creative loop is free today — no API keys required. If you upgrade
your Google AI Studio plan, set `GEMINI_API_KEY` in `.env` and Veo 3 photoreal
video becomes available via `scripts/gemini_video.py`.

---

## How the "self-healing" loop works

When `/decide-action` recommends **REGENERATE**, it writes a `lessons.md` file inside the proposal folder describing what failed and what to try instead. Next time `/design-ads` runs for that report, it auto-reads `lessons.md` + the cross-report `winning-patterns.md` / `losing-patterns.md` — so new creatives skip the patterns that failed and lean into what's worked elsewhere.

When `/decide-action` triggers the **Kill Switch** (from the brief's Section 10), it applies the protocol verbatim — no soft-pedaling.

---

## A reminder: $500 hard cap (for off-the-shelf campaigns)

Every off-the-shelf report campaign is math'd against $500 total spend. Not negotiable. If you want to scale a winner after the 2 weeks, that's a new campaign decision — make it deliberately, with fresh feasibility math, not by quietly raising budgets in Ads Manager.

**Ghost Elite campaigns may need a different budget** — they're lead-gen, not direct purchase, and the unit economics support more spend per lead. `/make-proposal` will surface this when you choose Ghost Elite as the product line.

---

## Running on a schedule (truly autonomous)

Once you're comfortable with the manual flow, you can tell Claude:

> "Schedule /review-ads to run every Monday at 9am for the currently-live campaign"
> "Schedule /research-topics to run every other Sunday so I always have fresh ideas in the pipeline"

Claude uses the `/schedule` system to make those recurring.

---

## Getting started right now

Type `/ghost` and Claude will run the full pipeline from "nothing" to "ready-to-launch campaign with rendered assets" in about 12-18 minutes of automated work. Image generation (Pollinations FLUX + editorial HTML cards) and video generation (Ken-Burns animation + animated HTML spots) all run for free without any API key — first-time setup just needs `pip install -r requirements.txt` if you haven't already.

Or, if you already have a specific report in mind, just type `/make-proposal` and answer the input questions.