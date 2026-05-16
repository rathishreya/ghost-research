---
name: write-prompts
description: Convert Ghost Research visual concepts into prompts tagged by Tool (`pollinations` default, optional `nanobanana-api` with paid key, `editorial`, `animate`, `animated-html`, `veo`) so `/generate-assets` and `/generate-video` dispatch scripts — never chat inline images as deliverables.
---

# Prompt Engineering Agent — Ghost Research

Your job: turn each visual concept from `visual-concepts.md` into a generation block that downstream scripts can execute automatically. The user is non-technical — `/generate-assets` must run with zero edits. **Do not sketch ad frames with chat-native image tooling** — all raster deliverables flow through Pollinations/editorial/API scripts into `assets/`.

## The Tool routes (pick one per concept)

| Tool value | What it produces | Backed by | When to pick |
|---|---|---|---|
| `pollinations` | Photo / scene image (JPG) | Pollinations.ai (defaults to `flux-realism` profile via launcher) | Default hero scenes / human+dashboard photography |
| `nanobanana-api` | Photo / scene (JPG/PNG) | Paid NanoBanana REST (`NANOBANANA_API_KEY`; `scripts/nanobanana_generate.py`) | Same use-case as pollinations — only when the user insists on NanoBanana output |
| `editorial` | Typography / data viz card (PNG) | HTML/CSS rendered via Playwright | Headlines, big stats, "report cover" style cards, document mock-ups |
| `animate` | Cinematic short video (MP4) | Static image + Ken Burns motion (ffmpeg) | Animating any `pollinations` or `editorial` image into a 6–8s scroll-stopper |
| `animated-html` | Pure-typography video (MP4) | HTML + CSS animations recorded by Playwright | Kinetic-type spots, "counting up" stat reveals, headline reveals |
| `composite-editorial` | (alias) same as `editorial` when HTML uses `GHOST_ASSET:` | Use `Tool: editorial` and embed `GHOST_ASSET:filename.jpg` in CSS `url(...)` | **Ad-ready static ads:** photo + headline + sub + CTA in one PNG |
| `veo` | Photoreal video (MP4) | Veo 3 Fast | **Paid Google AI Studio only.** Skip unless the user has upgraded. |

### Two-week calendar default (off-the-shelf campaigns)

Ship **14 concepts minimum** (one primary asset per day): **Days 1–7 = Week 1 hype** (problem, category, waitlist language — no fake report excerpts). **Days 8–14 = Week 2 sales** (offer, price anchor ~$500, proof, urgency, Ghost Elite cross-sell where the brief allows).

### Conversion-grade copy conventions (do this every time)

These are baked into the renderer's output quality — **violating them costs sales**.

1. **Every CTA ends with `→`** (the U+2192 right arrow). On editorial composites, append the arrow in the HTML CTA string. On animate / kinetic, the renderer appends it for you when the CTA field has no arrow.
2. **Week 1 CTAs trade in *waitlist* energy:** "Get on the list", "Reserve early access", "Notify me on launch". Avoid "Save the date" (event-y, not B2B).
3. **Week 2 CTAs *anchor the price*:** "Read the brief — $500", "Get the report — $500", "Download now — $500", "Buy for $500". Price anchoring is non-negotiable for $500 reports — confidence in pricing builds trust, and the $500 looks small next to "Bloomberg terminal" mental anchors.
4. **Every Week-2 eyebrow includes "$500"** (e.g. `AVAILABLE NOW · $500`, `BUNDLE-READY · $500`). The Week-1 eyebrow uses the publish date instead (`DROPS JUNE 1, 2026`, `CASPR. SELF-SERVE · DROPS <date>`).
5. **Every animate concept ships an `**On-screen eyebrow:**`** field — the renderer paints it in accent red above the headline. Default eyebrow: `GHOST RESEARCH` if you don't write one, but always write one.
6. **Headlines are *concrete, not categorical*.** "Demand signals are moving faster than ERP exports" beats "AI for supply chains". Lead with a specific job, a specific stack, a specific stakeholder.
7. **Subs are exactly two sentences max,** and one of those is a credibility line (`1M+ curated sources. Vetted by 10+ year domain SMEs.`).

### Ad-ready frames (photo + type in one file)

1. **Base still** (`pollinations`): scene only — **no burned-in marketing copy** (image models garble small type).  
2. **Composite** (`editorial`): full HTML card with `background-image: linear-gradient(...), url("GHOST_ASSET:concept-01-your-base.jpg")` plus Oranienbaum/Manrope headline, subcopy, and red `#EF4444` CTA. At render time, scripts rewrite `GHOST_ASSET:` to a `file://` URL so Chromium loads the JPG from `assets/`.  
3. **Motion** (`animate`): set `**Source image:**` to the **composite PNG** (not the raw base JPG) so Ken-Burns clips carry the typography.  
4. **Kinetic video** (`animated-html`): use the same photo+type layout in HTML; optional `GHOST_ASSET:` background so the MP4 is not flat color only.

### Pomelli (Google Labs)

**There is no Pomelli HTTP API** for this repo. For studio polish, use [Pomelli](https://labs.google.com/pomelli/), export PNG/MP4, then either:

- Drop files into `data/proposals/<slug>/pomelli-inbox/` named `concept-01.png` or `01.jpg` and run `python scripts/import_pomelli_exports.py --slug <slug> --overwrite`, **or**
- Chain `python scripts/generate_proposal_assets.py --slug <slug> --import-pomelli-inbox` so imports run before Pollinations (existing files skip regeneration).

Imports copy into the exact **`Suggested filename`** from each concept block in `prompts.md` (so editorial `GHOST_ASSET:` paths stay valid).

**Default routing in 2026** (free tier):
- Hero / scene shots → `pollinations`
- Headline / data card → `editorial`
- Hero video → `animate` (with a `pollinations` image as its source) OR `animated-html`

## Step 1 — Read inputs

- `data/proposals/<slug>/visual-concepts.md`
- `data/proposals/<slug>/campaign-brief.md`

## Step 2 — Brand encoding (every prompt)

### Universal style anchors (positive)
Weave these into every image / animate prompt:

```
Editorial photography, color-graded to deep indigo (#181650) and cool navy
(#06062D) tones, accent red (#EF4444) sparingly, high detail, sharp focus,
soft natural light, clean minimalist composition with negative space upper-
right, premium B2B aesthetic similar to Bloomberg, Financial Times, The
Economist. Real professional adults in their 30s-50s, business attire,
photoreal, shot on Arri Alexa Mini with 50mm prime, shallow depth of field,
natural skin tones, cinematic dusk light.
```

### Universal negatives (every **pollinations / Imagen raster** prompt)

Use these for **scene generators only**. HTML `editorial` composites intentionally contain **marketing typography** in the DOM (not inside the raster JPG).

```
no robots, no AI-themed imagery, no brain circuits, no glowing nodes,
no holograms, no neon, no cyberpunk, no sci-fi UI, no high-fiving,
no hands on keyboards, no fist bumps, no smiling-at-camera lifestyle,
no AI-generated faces, no uncanny features, no text in image,
no logos, no watermarks, no embedded captions.
```

### Palette reference
- Accent red: `#EF4444`
- Deep indigo: `#181650`
- Near-black: `#06062D`
- Clean background: `#F8F8FF`

## Step 3 — Write `prompts.md`

Save to `data/proposals/<slug>/prompts.md`:

````markdown
---
slug: [slug]
created: [YYYY-MM-DD]
brief: campaign-brief.md
concepts: visual-concepts.md
status: ready-to-generate
total_prompts: [N]
---

# Generation Prompts — [Report Title]

## How to use this file

1. Run `/generate-assets` — this runs `scripts/generate_proposal_assets.py` for every concept whose `Tool:` is `pollinations`, legacy aliases, optional `nanobanana-api` (paid key only), or `editorial`.
2. Run `/generate-video` — this auto-runs every `animate` and `animated-html` concept
3. Want a change? Run `/edit-ad [concept-id] "your instruction"`
4. When all assets look right, run `/prep-campaign`

## Brand reminder

- Pollinations / Imagen **base stills** stay text-free (models hallucinate copy). **All marketing copy** lives in `editorial` HTML composites using `GHOST_ASSET:your-base.jpg`, or in Pomelli exports you import into `assets/` via `pomelli-inbox/` + `import_pomelli_exports.py`.
- Ghost color grade must be visible in every output (deep indigo + cool navy)
- If a generated person looks AI-uncanny, run `/edit-ad` with "regenerate with a different face" until clean

---

## Concept 01 — [Name from visual-concepts.md]

**Tool:** pollinations
**Aspect:** 1:1
**Suggested filename:** `concept-01-[short-name].jpg`
**Maps to:** [Day X, Week Y]

### Generation prompt
```
[Single paragraph, 80-140 words. Structure:
Sentence 1: Subject + setting — concrete person, specific clothing, environment, what they hold/do
Sentence 2: Composition — framing, where the subject sits in frame, where the negative space is
Sentence 3: Lighting + mood — direction, quality, source
Sentence 4: Style anchors — editorial photography, deep indigo grade, Bloomberg/FT aesthetic, lens reference
End with: "Photoreal, shot on Arri Alexa Mini with 50mm prime, shallow depth of field, natural skin tones graded toward cool blue. No text, no logos, no watermarks."]

NEGATIVE: no robots, no AI-themed imagery, no brain circuits, no glowing
nodes, no holograms, no neon, no cyberpunk, no sci-fi UI, no high-fiving,
no hands on keyboards, no fist bumps, no smiling-at-camera lifestyle,
no AI-generated faces, no uncanny features, no text in image,
no logos, no watermarks.
```

### Overlay specs (added in design tool, NOT generated)

- **Headline:** "[Exact text from brief]" — Oranienbaum, [white on dark / `#181650` on light], [position]
- **CTA button:** "[Exact CTA]" — fill `#EF4444`, text white Manrope semibold, [position]

---

## Concept 02 — [Editorial Card Name]

**Tool:** editorial
**Aspect:** 1:1
**Suggested filename:** `concept-02-stat-card.png`
**Maps to:** [Day X]

### Generation prompt
```html
<!doctype html>
<html><head><meta charset="utf-8"/>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Oranienbaum&family=Manrope:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
<style>
  *{box-sizing:border-box;margin:0;padding:0}
  body{
    background:linear-gradient(135deg,#181650 0%,#06062D 100%);
    color:#F8F8FF;font-family:'Manrope',system-ui,sans-serif;
    width:100%;height:100vh;padding:7%;
    display:flex;flex-direction:column;justify-content:space-between;
  }
  .wm{font-family:'Oranienbaum',serif;font-size:22px;letter-spacing:.04em}
  .wm i{color:#EF4444;font-style:normal}
  .kicker{font-size:13px;font-weight:600;letter-spacing:.18em;text-transform:uppercase;
    color:rgba(255,255,255,.62)}
  .stat{font-family:'Oranienbaum',serif;color:#EF4444;
    font-size:clamp(120px,18vh,210px);line-height:.88;letter-spacing:-.04em}
  .unit{font-family:'Oranienbaum',serif;color:#F8F8FF;font-size:clamp(40px,6vh,72px)}
  .row{display:flex;align-items:baseline;gap:18px}
  .caption{font-size:18px;color:rgba(255,255,255,.7);max-width:32ch;margin-top:14px;line-height:1.5}
  .rule{height:1px;width:64px;background:#EF4444;margin-top:24px}
  .cta{display:inline-flex;align-items:center;gap:12px;background:#EF4444;color:#fff;
    padding:16px 28px;border-radius:4px;font-weight:700;font-size:16px;
    letter-spacing:.02em}.cta:after{content:"→"}
  .src{font-size:11px;color:rgba(255,255,255,.5);max-width:32ch;text-align:right}
  .bottom{display:flex;align-items:flex-end;justify-content:space-between;gap:20px}
</style></head>
<body>
  <header style="display:flex;justify-content:space-between">
    <div class="wm">Ghost Research<i>.</i></div>
    <div class="kicker">[REPORT KICKER e.g. "AI Due Diligence · Q3 2026"]</div>
  </header>
  <main>
    <div class="kicker" style="color:#EF4444">[EYEBROW e.g. "By the numbers"]</div>
    <div class="row" style="margin-top:24px">
      <div class="stat">[BIG NUMBER e.g. 73%]</div>
      <div class="unit">[BIG UNIT e.g. "of PE deals"]</div>
    </div>
    <div class="caption">[ONE LINE OF CAPTION — explain what the number means in plain English. Max 18 words.]</div>
    <div class="rule"></div>
  </main>
  <footer class="bottom">
    <span class="cta">Read the brief</span>
    <div class="src">1M+ curated sources · transparent citations · expert-vetted</div>
  </footer>
</body></html>
```

Notes for `editorial` concepts:
- The `Generation prompt` is the **full HTML document** that gets rendered. Use the structure above; fill in the bracketed zones with concept-specific copy.
- For other layout types (headline-only, split, document mockup), build them out of the same primitives (`.wm`, `.kicker`, `.stat`, `.cta`).
- Keep the indigo gradient bg, the Oranienbaum serif headlines, and the single red accent — these are non-negotiable.

---

## Concept 03 — [Video name]

**Tool:** animate
**Aspect:** 9:16
**Duration:** 6
**Motion:** zoom-in
**Source image:** concept-01-[short-name].jpg
**Suggested filename:** `concept-03-[short-name].mp4`
**Maps to:** [Day X]

### Generation prompt
```
[Same as Concept 01 if reusing its source image — or describe a new still here
and add a new pollinations concept earlier in the file with this filename.]
```

Motion options for the `Motion:` field: `zoom-in` | `zoom-out` | `pan-right` | `pan-left` | `static`

---

## Concept 04 — [Kinetic typography spot]

**Tool:** animated-html
**Aspect:** 9:16
**Duration:** 8
**Suggested filename:** `concept-04-headline-reveal.mp4`
**Maps to:** [Day X]

### Generation prompt
```html
<!doctype html>
<html><head><meta charset="utf-8"/>
<link href="https://fonts.googleapis.com/css2?family=Oranienbaum&family=Manrope:wght@400;700&display=swap" rel="stylesheet">
<style>
  *{box-sizing:border-box;margin:0;padding:0}
  body{background:linear-gradient(135deg,#181650 0%,#06062D 100%);color:#F8F8FF;
    font-family:'Manrope',sans-serif;width:100%;height:100vh;padding:8%;
    display:flex;flex-direction:column;justify-content:center;overflow:hidden}
  .kicker{font-size:14px;font-weight:600;letter-spacing:.18em;text-transform:uppercase;
    color:#EF4444;opacity:0;animation:fadeIn .6s ease forwards .3s}
  .h1{font-family:'Oranienbaum',serif;font-size:clamp(56px,9vh,112px);line-height:1.05;
    letter-spacing:-.02em;margin-top:20px;opacity:0;
    animation:fadeUp 1s cubic-bezier(.2,.7,.2,1) forwards .9s}
  .h1 em{font-style:italic;color:#EF4444}
  .sub{font-size:22px;color:rgba(255,255,255,.7);margin-top:28px;max-width:34ch;
    opacity:0;animation:fadeUp .8s ease forwards 2.4s}
  .rule{height:1px;width:64px;background:#EF4444;margin-top:36px;transform:scaleX(0);
    transform-origin:left;animation:slideRule .8s ease forwards 3.4s}
  .cta{display:inline-flex;align-items:center;gap:12px;background:#EF4444;color:#fff;
    padding:18px 32px;border-radius:4px;font-weight:700;font-size:18px;margin-top:36px;
    opacity:0;animation:fadeUp .6s ease forwards 4.4s}.cta:after{content:"→"}
  @keyframes fadeIn{to{opacity:1}}
  @keyframes fadeUp{from{opacity:0;transform:translateY(20px)}to{opacity:1;transform:none}}
  @keyframes slideRule{to{transform:scaleX(1)}}
</style></head>
<body>
  <div class="kicker">[KICKER]</div>
  <h1 class="h1">[HEADLINE — split a key word with <em>...</em>]</h1>
  <p class="sub">[ONE LINE SUPPORT, 18-22 words max]</p>
  <div class="rule"></div>
  <span class="cta">Read the brief</span>
</body></html>
```

---

[... continue for all concepts ...]

---

## Generation cost reality (2026 free tier)

- Pollinations.ai (FLUX): **free, unlimited**
- Editorial HTML render: **free, unlimited** (your own CPU)
- Animate (Ken Burns): **free, unlimited** (your own CPU + bundled ffmpeg)
- Animated-HTML: **free, unlimited** (Playwright + bundled ffmpeg)
- Veo 3 Fast: **NOT free** on Google AI Studio API as of 2026-05 — skip unless paid

Free tier delivers ~80% of the visual quality of the paid stack. The unlock is
strong prompts + strong editorial-card design, not bigger models.

````

## Step 4 — Update pipeline

Append: `[date] | [slug] | prompts written | [N] prompts ready`

## Step 5 — Hand off

```
Prompts ready: data/proposals/[slug]/prompts.md

Next steps (all free, all automatic):
1. /generate-assets   ← runs every pollinations + editorial concept
2. /generate-video    ← runs every animate + animated-html concept
3. /edit-ad [id] "instruction"  ← iterate on any ad you don't like
4. /prep-campaign     ← launch checklist when ads look right

All generation is free in the current setup. No API keys, no quotas.
```

## Rules

### pollinations
- Always include a clear subject + setting in sentence 1; FLUX gets vague prompts wrong.
- Always name the negative space ("subject in lower-left third, negative space upper-right") so headlines fit later.
- Never ask for text rendering — all text is added later via design tool or via an `editorial` concept layered on top.
- Use `1:1`, `4:5`, or `9:16` aspects. Avoid `1.91:1`.

### editorial
- The "Generation prompt" is a **complete HTML document**, not a prose description. The script renders it as-is.
- Always include the Google Fonts link for Oranienbaum + Manrope at the top of the HTML.
- Use ONE big focal element per card — either a headline, or a stat, or a key sentence. Not all three.
- Keep the Ghost color tokens exact: `#181650`, `#06062D`, `#EF4444`, `#F8F8FF`.

### animate
- Always reference an existing `pollinations` or `editorial` concept's `Suggested filename` as the source.
- Default `zoom-in` for hero subjects, `pan-right` for cityscapes, `static` if the still is busy.
- Duration: 6s for IG/TikTok cuts; 8s for LinkedIn / YouTube Shorts.

### animated-html
- Stagger animation delays so the kicker → headline → sub → CTA reveal feels like editorial pacing (0.3s → 0.9s → 2.4s → 4.4s).
- Use Oranienbaum italic + `#EF4444` for the emphasized word in any headline.
- The single CTA must always be `#EF4444` background, white text.

### veo (paid-tier only)
- Skip in the default free flow.
- If the user has upgraded their Google AI Studio plan, `/generate-video` can route Veo concepts through `scripts/gemini_video.py`.
