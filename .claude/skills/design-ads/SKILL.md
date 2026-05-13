---
name: design-ads
description: Expand the 3 hooks + copy from a Ghost Research campaign brief into 8-12 fully-specified visual ad concepts that respect Ghost brand identity (no robots, no AI clichés, deep indigo color-grade, Oranienbaum/Manrope typography, real professionals with data). Each concept maps to a specific day in the calendar. Use when the user wants ad concepts, says "design ads", "/design-ads", or right after /make-proposal.
---

# Creative Strategy Agent — Ghost Research

Your job: take the campaign brief and expand the 3 hooks + ad copy into **detailed visual concepts** that a designer or prompt engineer can execute. The brief already covers messaging — you only add the visual layer.

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

## Step 3 — Design the concept portfolio

Generate **8–12 concepts**, distributed by what the calendar in Section 3 needs:

| Bucket | Typical count | Use when |
|---|---|---|
| Static — single image (1:1) | 3-4 | Most calendar days. Cheapest to test. |
| Static — square data viz (1:1) | 1-2 | When the hook is a number/stat |
| Carousel / LinkedIn document (5-7 slides) | 1-2 | Week 1 thought leadership on LinkedIn |
| Short video — 8s clip (9:16) | 2-3 | Week 1 awareness on IG/Meta. Week 2 retargeting. |
| Cinematic video — 15-30s (9:16 or 1:1) | 1 | Week 2 launch hero ad (if budget supports premium creative) |

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

---

## Concept 01 — [Memorable name, e.g. "The Empty Boardroom"]

**Maps to calendar:** [Day X, Week Y — from Section 3 of brief]
**Platform:** [IG / LinkedIn / X / FB]
**Format:** [Static 1:1 / Video 9:16 / Carousel / etc.]
**Hook used:** [Hook 1, 2, or 3 from Section 0.3]
**Ad copy (from brief):**
- Headline: [exact text from Section 7]
- Body: [exact text from Section 7]
- CTA: [exact text from Section 7]

### Visual specification

**Subject:** [Specific person. e.g. "A woman in her 40s, dark blazer over white shirt, mid-length dark hair, looking thoughtfully at a printed report on a desk." Be this concrete.]

**Setting:** [Specific environment. e.g. "Modern executive office, large window showing soft city light, dark wood desk, single open report visible, minimal — no plants, no laptops in frame."]

**Composition:**
- Subject placement: [e.g. "Subject occupies right third of frame, looking down-left at report"]
- Negative space: [Where the headline overlay will sit — "Upper-left third, clean grey wall"]
- Depth: [e.g. "Subject in sharp focus, background slight soft blur"]

**Lighting:** [e.g. "Soft window light from camera left, slight cool tone. Subtle rim light on subject's right side. No harsh shadows."]

**Color grade:** Deep indigo / navy tonal grade. Reduce warmth, lift shadows slightly to navy. Skin tones natural but cool. Whites pulled toward `#F8F8FF`.

**On-screen elements (added in design tool, NOT generated):**
- Headline overlay: "[Exact headline text]" in Oranienbaum, white, [position]
- Sub-text: "[Body text]" in Manrope regular, white 80% opacity, [position]
- Ghost Research wordmark: bottom-left, small
- CTA button: "[Exact CTA]" — `#EF4444` red background, white Manrope semibold text, [position]

**For VIDEO concepts only — add:**
- Opening frame (0s): [What we see immediately]
- Motion: [Camera move + subject action — keep simple. "Slow push-in, subject lifts gaze from report toward window."]
- Closing frame (8s or 15s): [Final freeze frame that holds for CTA]
- Voiceover script: [Exact words, under 25 words for 8s / under 60 for 15s. Mark pauses ///]

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
