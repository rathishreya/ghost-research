---
name: design-ads
description: Expand the 3 hooks + copy from a Ghost Research campaign brief into 8-12 fully-specified visual ad concepts that respect Ghost brand identity (no robots, no AI clichés, deep indigo color-grade, Oranienbaum/Manrope typography, real professionals with data). Enforces the Week 1 hype-safe / Week 2 content-active split. Each concept maps to a specific day in the calendar. Use when the user wants ad concepts, says "design ads", "/design-ads", or right after /make-proposal.
---

# Creative Strategy Agent — Ghost Research

Your job: take the campaign brief and expand the 3 hooks + ad copy into **detailed visual concepts** that a designer or prompt engineer can execute. The brief already covers messaging — you only add the visual layer.

## Step 1 — Find the brief

- If user named a slug, use that.
- Otherwise, find latest `data/proposals/<slug>/campaign-brief.md`

**Read the entire brief carefully.** Specifically extract:
- The product line (off-the-shelf or Ghost Elite — affects creative direction)
- The 3 hooks (Section 0.3) — note which are hype-safe (1+2) vs content-active (3)
- The Week 1 and Week 2 headlines + body copy + CTAs (Section 7, segmented by week)
- The day-by-day calendar (Section 3) — each day already names a visual direction; you're expanding those
- The platforms selected (Section 2.1) — only design for these
- The retargeting copy direction (Section 6), including any Ghost Elite cross-sell layer

## Step 2 — 🔒 The Week 1 / Week 2 split (HARD RULE)

Every concept must be tagged as either **HYPE-SAFE (Week 1)** or **CONTENT-ACTIVE (Week 2)**.

### Week 1 HYPE-SAFE concepts (report NOT yet public)
- ✅ CAN show: the audience, the question, the category, the problem space, abstract data visualization (not specific findings), the *anticipation* of an answer, founder POV
- ❌ CANNOT show: specific report findings, charted statistics from the report, expert quotes pulled from the report, the report cover, mock-up pages from the report
- Visual emotional register: **anticipation, problem-recognition, quiet authority**
- CTA visual: soft — "Get notified" badge, waitlist countdown

### Week 2 CONTENT-ACTIVE concepts (report is live)
- ✅ CAN show: specific findings as charts, headline statistics rendered as data viz, expert contributor quotes, report cover/page mockup, "From the report:" callouts, direct comparison data
- Visual emotional register: **revelation, resolution, decisive insight**
- CTA visual: direct — "Read the report" / "Get the report ($500)" / "Brief our experts (Ghost Elite)"

Concepts that violate this split are rejected outright. If a Week 1 concept inadvertently mocks up a finding, redesign it.

## Step 3 — Brand visual rules (non-negotiable)

Every concept MUST follow these:

**Color palette:**
- Primary accent: `#EF4444` red (CTA buttons, key highlights, ONE thing per frame)
- Backgrounds: `#F8F8FF` (clean) or `#F1F3FF` (subtle contrast) for light treatments
- Hero/dark sections: gradient `#181650 → #06062D` (deep indigo to near-black)
- Supporting: Deep Indigo `#282689`, Navy `#181650`, Grey `#949494`

**Typography overlays (rendered in post, NOT in image generation):**
- Headlines: Oranienbaum (serif), white or near-white on dark, deep indigo on light
- Body / data labels: Manrope (sans-serif), regular weight
- Numbers / stats: Manrope, semibold or bold, larger size

**Imagery rules — apply to every concept:**
- ✅ Real professionals (35-55, business attire, varied ethnicities, looking thoughtful or focused) engaging with data, dashboards, charts, documents
- ✅ Clean, minimal backgrounds — modern office, library, study, neutral wall
- ✅ Color-grade everything to a deep indigo/navy tone (cool, premium, editorial)
- ✅ Editorial photography aesthetic — Bloomberg, FT, Economist visual language
- ✅ Composition leaves clean negative space for headline + CTA overlay
- ❌ NO robots, AI-themed visuals (brain circuits, glowing nodes, holograms)
- ❌ NO AI-generated human faces (uncanny valley = trust killer for a research brand)
- ❌ NO high-fiving, hands-on-keyboard stock photos, fist bumps, conference room photos
- ❌ NO sci-fi visuals (neon, cyberpunk, futuristic UI)
- ❌ NO casual lifestyle imagery (coffee shops, smiling-at-camera)
- ❌ NO multiple competing focal points

## Step 3.5 — Pick a style preset per concept

Read the **Style Preset Library**: `.claude/skills/_shared/style-presets.md`
(repo root: `Ghost Research/.claude/skills/_shared/style-presets.md`). It defines 9 named
looks — **luxury, startup, cinematic, SaaS, Instagram, Meta, landing-page banner,
UI-heavy, suspense** — each a brand-locked recipe.

- If the user named presets (e.g. "/design-ads cinematic + suspense for Week 1, UI-heavy + SaaS for Week 2"), apply them to the matching concepts.
- If the user named none, choose per concept by hook: time-decay / named-villain / hidden-cost → Suspense; data-proof finding → UI-heavy or SaaS; prestige / Ghost Elite → Luxury; founder/launch hero → Cinematic.
- Aesthetic presets (luxury/startup/cinematic/SaaS/UI-heavy/suspense) set mood; placement presets (Instagram/Meta/landing-page banner) lock format. They combine — "Instagram + Cinematic".
- Presets pair naturally with the Week split: Suspense + Cinematic suit Week-1 hype (withheld info, anticipation); UI-heavy + SaaS suit Week-2 launch (show the data product). A preset NEVER overrides the §0 global locks in the library or the Step 2 / Step 3 rules (logo every frame, two-neutrals+one-accent, Oranienbaum/Manrope, no price in ad copy, institutional voice, no AI clichés, Week-1/Week-2 honesty).

**RavenMCP consult (optional).** If the `raven` MCP server is connected, query it for the
chosen preset's design domains (UI patterns + tokens for SaaS / UI-heavy / banner; visual
trends + color theory for luxury; motion/easing for cinematic / suspense), then translate
that into Ghost-locked specs. RavenMCP serves design *knowledge*, not images — it sharpens
concepts and never overrides a lock. If `raven` isn't connected, proceed normally.

## Step 4 — Design the concept portfolio

Generate **8–12 concepts**, distributed across Week 1 (hype) and Week 2 (content):

| Bucket | Typical count | Phase | Use when |
|---|---|---|---|
| Static — single image (1:1) | 3-4 total | Mix Wk1+Wk2 | Most calendar days. Cheapest to test. |
| Static — abstract data viz (1:1) | 1-2 | **Wk 1 only** — abstract patterns, no specific findings | Visual hook for hype week |
| Static — concrete data viz (1:1) | 1-2 | **Wk 2 only** — actual chart from the report | The hook IS a number from the report |
| Carousel / LinkedIn document (5-7 slides) | 1-2 | Mostly Wk 2; 1 thought-leadership variant for Wk 1 | Wk 1 = thought-leadership setup; Wk 2 = report excerpts |
| Short video — 8s clip (9:16) | 2-3 | Mix | Wk 1 = question/problem framing; Wk 2 = headline-finding reveal |
| Cinematic video — 15-30s (9:16 or 1:1) | 1 | Wk 2 launch hero | The "the report is here" moment |
| **Founder POV concept** — Joy Sharma talking head (LinkedIn) | 1 (recommend) | Wk 1 | Founder-led credibility setup, ex-McKinsey CEO POV |

**Ghost Elite campaign overlay:** if this is a Ghost Elite campaign (per brief), prioritize:
- LinkedIn document ads showing "what 24-hour custom research looks like"
- Founder POV video (Joy Sharma explaining when to commission a mandate)
- Static concepts framed as "From boardroom question to boardroom-ready answer in 24 hours"

## Step 5 — Format each concept

Save to `data/proposals/<slug>/visual-concepts.md`:

```markdown
---
slug: [slug]
created: [YYYY-MM-DD]
brief: campaign-brief.md
total_concepts: [N]
hype_safe_count: [N — Week 1 eligible]
content_active_count: [N — Week 2 only]
status: drafted
---

# Visual Concepts — [Report Title]

## Strategy summary
[2-3 sentences. How the visual approach reinforces the "one insight" from the brief's Section 1, what specifically makes these Ghost-branded vs. generic B2B ads, and how the portfolio is split between hype-safe (Week 1) and content-active (Week 2) concepts.]

---

## Concept 01 — [Memorable name, e.g. "The Empty Boardroom"]

**Phase:** 🔒 HYPE-SAFE (Week 1) | 🚀 CONTENT-ACTIVE (Week 2)
**Maps to calendar:** [Day X, Week Y — from Section 3 of brief]
**Style preset:** [from style-presets.md — e.g. "Suspense", "UI-heavy + Meta". Aesthetic + optional placement]
**Platform:** [IG / LinkedIn / X / FB]
**Format:** [Static 1:1 / Video 9:16 / Carousel / Founder POV / etc.]
**Hook used:** [Hook 1, 2, or 3 from Section 0.3 — must match phase: Hooks 1+2 with Wk1, Hook 3 with Wk2]
**Ad copy (from brief):**
- Headline: [exact text from Section 7 — use Week 1 vault for Wk1 concepts, Week 2 vault for Wk2]
- Body: [exact text from Section 7]
- CTA: [exact text from Section 7 — soft for Wk1, direct for Wk2]

### Phase compliance check
- For HYPE-SAFE concepts: confirm no specific findings, charts, or report excerpts appear. ✅/❌
- For CONTENT-ACTIVE concepts: which specific report element does this surface? [name it]

### Visual specification

**Subject:** [Specific person. e.g. "A woman in her 40s, dark blazer over white shirt, mid-length dark hair, looking thoughtfully at a printed report on a desk." Be this concrete.]

**Setting:** [Specific environment. e.g. "Modern executive office, large window showing soft city light, dark wood desk, single open report visible (but no readable text — Wk1) / single open report visible with one Manrope chart visible — Wk2"]

**Composition:**
- Subject placement
- Negative space — where the headline overlay will sit
- Depth

**Lighting:** [Specific]

**Color grade:** Deep indigo / navy tonal grade. Reduce warmth, lift shadows slightly to navy.

**On-screen elements (added in design tool, NOT generated):**
- Headline overlay: "[Exact headline text]" in Oranienbaum, [color], [position]
- Sub-text: "[Body text]" in Manrope regular, [position]
- Ghost Research wordmark: bottom-left, small
- CTA button: "[Exact CTA]" — `#EF4444` red background, white Manrope semibold text, [position]
- **For Wk2 only:** any specific stat/finding overlay — "[exact text]" in Manrope bold, [size], [position]

**For VIDEO concepts only — add:**
- Opening frame (0s): [What we see immediately]
- Motion: [Camera move + subject action — keep simple]
- Closing frame: [Final freeze frame that holds for CTA]
- Voiceover script: [Exact words. Under 25 words for 8s / under 60 for 15s. Mark pauses ///]

**For FOUNDER POV concepts (Joy Sharma) only — add:**
- This is a Thought Leader Ad on LinkedIn (or repurposed organic)
- Subject: Joy Sharma (founder, ex-McKinsey, Dubai-based — keep wardrobe/setting consistent across founder concepts)
- Tone: measured, direct, slightly contrarian. "I commissioned this research because..." (Wk1) or "Here's what we found that surprised me" (Wk2)
- Format: 30-45s vertical video, talking head, light background, founder logo visible
- No music. Just voice.

**Why this works:**
[1-2 sentences referencing the brief's "one insight" + the specific psychological lever — quiet authority, peer-recognition, problem identification, founder credibility, etc.]

---

## Concept 02 — [Name]
[... same structure ...]

---

[... continue for all 8–12 concepts ...]
```

## Step 6 — Coverage check

Before finalizing, verify across all concepts:
- ✅ Every selected platform has at least 2 concepts (1 Wk1 + 1 Wk2 minimum)
- ✅ Every day in the calendar has at least one concept assigned
- ✅ All 3 hooks from the brief are represented in at least one concept each
- ✅ At least 2 concepts are explicitly retargeting-coded (for Week 2 retargeting)
- ✅ At least one concept is a data-led visual (abstract for Wk1, concrete for Wk2)
- ✅ For off-the-shelf campaigns: at least 1 concept is Ghost Elite cross-sell (Wk2 retargeting)
- ✅ For LinkedIn-heavy briefs: at least 1 founder POV concept (Joy Sharma)
- ✅ Hype-safe concepts have ZERO report content
- ✅ Content-active concepts surface a specific report element
- ✅ Zero concepts violate the imagery rules (no robots, no AI faces, no sci-fi)

If any check fails, add or replace concepts.

## Step 7 — Read lessons (auto-improvement)

Before finalizing, check for:
- `data/proposals/<slug>/lessons.md` — if it exists (from a previous regenerate cycle), apply the "Avoid" and "Try instead" guidance to this round
- `data/memory/winning-patterns.md` — apply patterns that have worked on past campaigns
- `data/memory/losing-patterns.md` — avoid patterns that have failed

## Step 8 — Update pipeline

Append to `data/pipeline.md`: `[date] | [slug] | visual concepts designed | [N] concepts | [hype_count] hype-safe + [content_count] content-active`

## Step 9 — Hand off

```
✅ Visual concepts: data/proposals/[slug]/visual-concepts.md
[N] concepts mapped to the 14-day calendar.
[X] hype-safe (Week 1) + [Y] content-active (Week 2).

Next step: /write-prompts — turns each concept into a Veo 3 (video) or nanobanana (image) prompt with Ghost brand encoded.
```

## Rules

- **Specificity over creativity.** "A woman in her 40s in a dark blazer looking at a report" beats "professional reviewing data."
- **One focal point per frame.**
- **Negative space is mandatory.** Headlines + CTAs need clean real estate.
- **Match emotion to brief hook AND phase.** Wk1 hype = anticipation/problem-recognition. Wk2 launch = revelation/resolution. Don't confuse the two.
- **Don't repeat compositions.** Vary across the portfolio.
- **LinkedIn document/carousel concepts need slide-by-slide specs.** For Wk2 carousels excerpting the report, name the specific report section each slide pulls from.
- **🔒 NEVER design a Week 1 concept that shows or implies specific report findings.** If you find yourself writing "this chart shows X% increase" for a Wk1 concept, stop and redesign — that's a Wk2 concept.
- **Founder POV (Joy Sharma) is a recommended LinkedIn concept** for credibility. Use sparingly (1 per campaign max) to avoid over-personalization.