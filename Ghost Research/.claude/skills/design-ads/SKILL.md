---
name: design-ads
description: Expand the 3 hooks + copy from a Ghost Research campaign brief into 8-12 fully-specified visual ad concepts that respect Ghost brand identity (no robots, no AI clichés, deep indigo color-grade, Oranienbaum/Manrope typography, real professionals with data). Each concept maps to a specific day in the calendar. Use when the user wants ad concepts, says "design ads", "/design-ads", or right after /make-proposal.
---

# Creative Strategy Agent — Ghost Research

Your job: take the campaign brief and expand the 3 hooks + ad copy into **detailed visual concepts** that a designer or prompt engineer can execute. The brief already covers messaging — you only add the visual layer.

## 🔒 READ THE TEMPLATE LIBRARY FIRST — `.claude/skills/_shared/template-library.md`

Every concept must map to one of the named templates there (A Dark Photo Hero · B Journal Cover · C Pull-Quote · D Light Stat Card · E Carousel · F Light Banner) — these are the layouts Shreyanshi reviewed file-by-file and approved. Name the template in each concept's `Style preset:` / a `Template:` line. Honor its alignment law, blob structures, masthead lockup, footer sizes, and the §2 anti-patterns (campaign-killers).

**🚫 VIDEOS ARE PAUSED (since 2026-05-23).** Design **image-only** concepts by default — no 8s/15s video, no carousel-as-video, no cinematic clips — unless the user explicitly asks for video this run. Put the creative energy into stronger stills.

## Step 1 — Find the brief

- If user named a slug, use that.
- Otherwise, find latest `data/proposals/<slug>/campaign-brief.md`

**Read the entire brief carefully.** Specifically extract:
- The 3 hooks (Section 0.3)
- The 5 headlines + body copy + CTAs (Section 7)
- The day-by-day calendar (Section 3) — each day already names a visual direction; you're expanding those
- The platforms selected (Section 2.1) — only design for these
- The retargeting copy direction (Section 6)

## Step 2 — Brand visual rules (non-negotiable)

Every concept MUST follow these:

**🔒 LOGO RULE — APPLIES TO EVERY IMAGE, VIDEO, AND VFX FRAME:**
The Ghost Research icon mark (`Ghost Research/assets/brand/logo-mark.svg` — a red `#EF4444` rounded-square with a white inset circle) is composited in the top-left of every single output. This is not optional, not skippable, not a "designer's choice." It applies to: static ads, carousels, Reels, Stories, LinkedIn documents, retargeting clips, multi-shot videos, kinetic-typography spots, transition frames, and any VFX. The text wordmark "Ghost Research." is retired — the icon mark IS the brand mark now. Per-format placement spec lives in Step 4 under "On-screen elements."

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

## Step 2.5 — Pick a style preset per concept

Read the **Style Preset Library**: `.claude/skills/_shared/style-presets.md`
(from repo root: `Ghost Research/.claude/skills/_shared/style-presets.md`). It defines
9 named looks — **luxury, startup, cinematic, SaaS, Instagram, Meta, landing-page banner,
UI-heavy, suspense** — each a brand-locked visual recipe.

- If the user named a preset (e.g. "/design-ads luxury + suspense", "make UI-heavy SaaS ads"), apply it to the relevant concepts.
- If the user named none, choose the preset per concept that best fits the hook (e.g. a time-decay hook → Suspense; a data-proof hook → UI-heavy; a Ghost Elite prestige angle → Luxury).
- Aesthetic presets (luxury/startup/cinematic/SaaS/UI-heavy/suspense) set mood + layout; placement presets (Instagram/Meta/landing-page banner) lock format. They combine — e.g. "Instagram + Cinematic".
- **Every preset still obeys §0 global locks** in the library (logo on every frame, two-neutrals+one-accent, Oranienbaum/Manrope, no price in ad copy, institutional voice, no AI clichés, info-gap headline, Week-1/Week-2 law). A preset changes the *look*, never these.

**Design-intelligence consult (RavenMCP, optional).** If the `raven` MCP server is
connected, query it for the design domains the chosen preset names (UI patterns +
design tokens for SaaS / UI-heavy / banner; visual trends + color theory for luxury;
motion/easing for cinematic/suspense), then translate that guidance into Ghost-locked
specs. RavenMCP serves design *knowledge*, not images — it sharpens concepts, it never
overrides the locks. If `raven` isn't connected, proceed normally; presets don't depend on it.

## Step 3 — Design the concept portfolio

Generate **8–12 concepts**, distributed by what the calendar in Section 3 needs:

| Bucket | Typical count | Template (library) | Use when |
|---|---|---|---|
| Dark Photo Hero (1:1) | 3-4 | A | Most calendar days; hero scene + a big red stat |
| Journal Cover (1:1) | 1-2 | B | Launch / "it's live" / campaign anchor (always add a CTA) |
| Pull-Quote (1:1) | 1 | C | The thesis line / contrarian claim / expert quote |
| Light Stat Card (1:1) | 1-2 | D / F | The mandatory 1-2 light cards — blobs behind, framed image ~38-42% |
| Carousel / LinkedIn document (5-7 slides) | 1-2 | E | LinkedIn thought leadership — IDENTICAL chassis every slide |

**🚫 No video buckets — videos are paused (2026-05-23).** If the user later asks for video, add `animate` / `animated-html` concepts then; otherwise every concept is a still.

## Step 4 — Format each concept

Save to `data/proposals/<slug>/visual-concepts.md`:

```markdown
---
slug: [slug]
created: [YYYY-MM-DD]
brief: campaign-brief.md
total_concepts: [N]
status: drafted
---

# Visual Concepts — [Report Title]

## Strategy summary
[2-3 sentences. How the visual approach reinforces the "one insight" from the brief's Section 1, and what specifically makes these Ghost-branded vs. generic B2B ads.]

**Theme mix required:** This deck of N concepts must include **at least 1 and at most 2 LIGHT-theme concepts** alongside the dark-mode majority. Light theme uses `#F8F8FF` paper background, `#06062D` ink text, accent red `#EF4444` unchanged, wordmark flips to ink. Best lanes for light theme: stat-reveal ads (one big red number on cream), Week-2 publish announcements, or Ghost Elite enquiry ads (premium-consultancy feel vs. trading-floor feel). Mark these concepts' Color grade field with **"LIGHT THEME"** at the top.

---

## Concept 01 — [Memorable name, e.g. "The Empty Boardroom"]

**Maps to calendar:** [Day X, Week Y — from Section 3 of brief]
**Style preset:** [luxury / startup / cinematic / SaaS / UI-heavy / suspense — plus optional placement: Instagram / Meta / landing-page banner. From style-presets.md. e.g. "Suspense + Instagram"]
**Platform:** [IG / LinkedIn / X / FB]
**Format:** [Static 1:1 / Video 9:16 / Carousel / etc.]
**Hook used:** [Hook 1, 2, or 3 from Section 0.3]
**Ad copy (from brief):**
- Headline: [exact text from Section 7]
- Body: [exact text from Section 7]
- CTA: [exact text from Section 7]

### Visual specification

**Subject:** [Specific person. e.g. "A woman in her 40s, dark blazer over white shirt, mid-length dark hair, looking thoughtfully at a printed report on a desk." Be this concrete. **Must reference the report's specific audience role** — not a generic "professional" but the actual buyer (IPO syndicate MD / sector CFO / strategy partner / supply-chain ops director). The Subject answers "who buys this report?"]

**Setting:** [Specific environment. e.g. "Modern executive office, large window showing soft city light, dark wood desk, single open report visible, minimal — no plants, no laptops in frame." **Must contain at least one prop, document, screen, or environmental detail tied to the report's specific topic.** Examples: an IPO-window concept shows a Bloomberg terminal with pricing screen + printed S-1 prospectus; a music-economy concept shows tour-P&L spreadsheet + label-deal contracts, NOT a celebrity stock photo.

**⚠️ IMAGE-RELEVANCE GATE — apply the swap test before shipping every concept:** Replace the report title with any other Ghost Research report. Does the Subject + Setting still fit? If YES, the concept is too generic — REGENERATE the prompt with topic-specific props before letting it through to `/generate-assets`. This is the #1 quality issue Shreyanshi has flagged. Failing this test ships generic stock-feel imagery that loses the campaign.

**Headline must use an info-gap mechanism** (see [[ghost_copy_uncommon_hooks]]): named villain, contrarian counter, hidden cost, time-decay urgency, specificity, or insider POV. Generic "Discover insights..." copy is forbidden.

**Composition:**
- Subject placement: [e.g. "Subject occupies right third of frame, looking down-left at report"]
- Negative space: [Where the headline overlay will sit — "Upper-left third, clean grey wall"]
- Depth: [e.g. "Subject in sharp focus, background slight soft blur"]

**Lighting:** [e.g. "Soft window light from camera left, slight cool tone. Subtle rim light on subject's right side. No harsh shadows."]

**Color grade:** Deep indigo / navy tonal grade. Reduce warmth, lift shadows slightly to navy. Skin tones natural but cool. Whites pulled toward `#F8F8FF`.

**On-screen elements (added in design tool, NOT generated):**
- Headline overlay: "[Exact headline text]" in Oranienbaum, white, [position]
- Sub-text: "[Body text]" in Manrope regular, white 80% opacity, [position]
- **Ghost Research icon mark — MANDATORY on every creative, every image, every video, every VFX frame, no exceptions.** Use the file at `Ghost Research/assets/brand/logo-mark.svg` (vector) or `Ghost Research/assets/brand/logo-mark.png` (512×512 transparent raster). The mark is a `#EF4444` red rounded-square with a white inset circle — the icon-only brand mark. Do NOT replace with a text wordmark. Do NOT recolor. Do NOT add a drop shadow or stroke. The mark works as-is on both dark and light backgrounds. Always square (height = width). Placement by format (must sit inside the safe zone):
  - **9:16 Reels/Stories (1080×1920):** top-left, x≈60px, y≈290px (just below the 270px top no-text margin), badge size 96–112px
  - **4:5 Portrait Feed (1080×1350):** top-left, x≈60px, y≈60px, badge size 96–112px
  - **1:1 Square Feed (1080×1080):** top-left, x≈70px, y≈70px (inside 50–90px clean margin), badge size 88–104px
- CTA button: "[Exact CTA]" — `#EF4444` red background, white Manrope semibold text, [position]

**For VIDEO concepts only — add:**
- Opening frame (0s): [What we see immediately]
- Motion: [Camera move + subject action — keep simple. "Slow push-in, subject lifts gaze from report toward window."]
- Closing frame (8s or 15s): [Final freeze frame that holds for CTA]
- Voiceover script: [Exact words, under 25 words for 8s / under 60 for 15s. Mark pauses ///]
- **Logo persistence:** Ghost Research icon mark (`assets/brand/logo-mark.svg`) stays in its top-left position on every single frame from 0s to last frame, including any VFX/transition frames. Do NOT fade in/out — any scrub-position or thumbnail must carry the brand mark.
- **Minimum runtime for 9:16 (Reels/Stories): 15 seconds.** No 6s / 8s / 10s clips for vertical video.

**Why this works:**
[1-2 sentences referencing the brief's "one insight" + the specific psychological lever — quiet authority, peer-recognition, problem identification, etc.]

---

## Concept 02 — [Name]
[... same structure ...]

---

[... continue for all 8–12 concepts ...]
```

## Step 5 — Coverage check

Before finalizing, verify across all concepts:
- ✅ Every selected platform has at least 2 concepts
- ✅ Every day in the calendar has at least one concept assigned
- ✅ All 3 hooks from the brief are represented in at least one concept each
- ✅ At least 2 concepts are explicitly retargeting-coded (for Week 2 retargeting)
- ✅ At least one concept is a data-led visual (chart, number, finding visualized)
- ✅ Zero concepts violate the imagery rules (no robots, no AI faces, no sci-fi)

If any check fails, add or replace concepts.

## Step 6 — Update pipeline

Append to `data/pipeline.md`: `[date] | [slug] | visual concepts designed | [N] concepts`

## Step 7 — Hand off

```
✅ Visual concepts: data/proposals/[slug]/visual-concepts.md
[N] concepts mapped to the 14-day calendar.

Next step: /write-prompts — turns each concept into a Veo 3 (video) or nanobanana (image) prompt with Ghost brand encoded.
```

## Rules

- **Specificity over creativity.** "A woman in her 40s in a dark blazer looking at a report" beats "professional reviewing data." Generative models and designers both need the concrete details.
- **One focal point per frame.** If you can't name what the eye lands on in 0.2 seconds, the concept is broken.
- **Negative space is mandatory.** Headlines + CTAs need clean real estate — engineer the composition to provide it.
- **Match emotion to brief hook.** If Hook 1 is "The Consequence Hook" (fear), the visual mood is somber/serious — not aspirational. The visual must reinforce the copy's emotional register, not fight it.
- **Don't repeat compositions.** If concept 01 has subject on the right looking left, concept 02 should NOT also have that. Vary across the portfolio so a scroll-by viewer sees variety.
- **LinkedIn document/carousel concepts need slide-by-slide specs.** Don't just say "5 slides about the report" — write each slide's content direction.
