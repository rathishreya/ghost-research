---
name: write-prompts
description: Convert Ghost Research visual concepts into prompts tagged by Tool (`pollinations` default, optional `nanobanana-api` with paid key, `editorial`, `animate`, `animated-html`, `veo`) so `/generate-assets` and `/generate-video` dispatch scripts — never chat inline images as deliverables.
---

# Prompt Engineering Agent — Ghost Research

Your job: turn each visual concept from `visual-concepts.md` into a generation block that downstream scripts can execute automatically. The user is non-technical — `/generate-assets` must run with zero edits. **Do not sketch ad frames with chat-native image tooling** — all raster deliverables flow through Pollinations/editorial/API scripts into `assets/`.

## 🔒 READ THE TEMPLATE LIBRARY FIRST — `.claude/skills/_shared/template-library.md`

Every editorial card MUST be built from one of the named templates there (A Dark Photo Hero · B Journal Cover · C Pull-Quote · D Light Stat Card · E Carousel · F Light Banner). It encodes Shreyanshi's file-by-file taste review and is the authority on layout, the alignment law, blob structures, footer font sizes, the masthead lockup, and the campaign-killer anti-patterns. When this library and an older example disagree, the library wins.

**🚫 VIDEOS ARE PAUSED (since 2026-05-23).** Default to **image-only**. Do NOT emit `animate`, `animated-html`, or `veo` concepts unless the user explicitly asks for video this run. Spend the effort on stronger editorial cards instead.

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

### The three aesthetic lanes (every concept must declare one)

Every concept block now carries a `**Lane:**` field. The lane decides the visual
vocabulary. Three lanes only — pick one per concept; do not blend.

| Lane value | Reference | Visual code | Use case |
|---|---|---|---|
| `cinematic-ink` | Apple keynote stills, Linear product surfaces, Tesla reveals, OpenAI launch | Deep navy/black gradient · single hero element · soft red specular highlight · generous negative space · Oranienbaum serif headline ≤ 16ch · italic-red emphasis on the value claim | Reels / Stories / hero ads / brand video frames |
| `editorial-paper` | Stripe Press, NYT Magazine, Information is Beautiful | Cream `#F4EFE6` or off-white `#F8F8FF` background · oversized serif number or pull-quote · Newsreader/Oranienbaum body type · footnote markers · tiny price + CTA at the very bottom | Static feed posts, LinkedIn squares, Meta carousels |
| `methodology-specimen` | Academic journal, Bloomberg terminal export, leaked memo | Two columns of justified body type · running header with date + page number · section markers § 4.3 · footnote with red [N] · single oversized pull-quote with red marginal rule | Authority moments, retargeting, Day-8 launch announcement |

**Brand bible is preserved across all three:** Oranienbaum + Manrope only. Two
neutrals + one accent (`#EF4444`). Voice is precise / authoritative / institutional —
never "game-changing" / "supercharge" / hype-startup vocabulary.

### Style presets → generator routes

Each concept from `visual-concepts.md` carries a `**Style preset:**` field (luxury /
startup / cinematic / SaaS / UI-heavy / suspense, plus optional Instagram / Meta /
landing-page-banner placement). The preset decides the **Tool route** and prompt
modifiers. Read `.claude/skills/_shared/style-presets.md` (repo root:
`Ghost Research/.claude/skills/_shared/style-presets.md`) for the full spec, then map:

| Preset | Tool route | Default aspect | Prompt modifier |
|---|---|---|---|
| Luxury | `pollinations` (material/object, no faces) → `editorial` composite | 1:1 / 4:5 | Premium materials (marble/metal/walnut/leather) as subject, macro texture, single red specular, deep void. |
| Startup | `editorial` / `animated-html` | 1:1 / 9:16 | Bold oversized serif claim, high contrast, fast clean reveal. **Voice stays institutional** — no growth-hack words. |
| Cinematic | `animate` / `animated-html` | 9:16 ≥15s | Navy→black gradient, one hero element from darkness, soft red specular, slow push-in, ≥15s. |
| SaaS | `editorial` (UI in HTML, **never** pollinations) | 1:1 / 16:9 | One minimal product panel — a real chart/KPI/table — Manrope UI type, one red hero metric. Visually SaaS, voice institutional. |
| UI-heavy | `editorial` (real data UI in HTML) | 1:1 / 16:9 | Dense dashboard/terminal export, exactly ONE red-highlighted hero metric, footnote source line. Report-specific data only. |
| Suspense | `animate` / `animated-html` | 9:16 ≥15s | Near-black, slow reveal, red accent arrives late, redacted/blurred document motif, withheld answer. |
| Instagram | (placement — keep route) | 1:1 / 4:5 / 9:16 | Thumb-stop frame 1, mobile-high type sizes, 9:16 safe zones (logo y≈290). |
| Meta | (placement — keep route) | 1:1 + 4:5 + 9:16 | Emit all three Meta copy fields: *primary text / headline / description*. |
| Landing-page banner | `editorial` | 16:9 / 21:9 / 1.91:1 | Left headline column + right negative space/UI panel. **Only preset where price may appear** (landing page reveals price). |

**RavenMCP consult (optional).** When the `raven` MCP server is connected, query its
design tools for the preset's domains (UI patterns + design tokens for SaaS / UI-heavy /
landing-page banner; visual trends + color theory for luxury; motion/easing for cinematic /
suspense), then bake the guidance into Ghost-locked specs. RavenMCP supplies design
knowledge, never pixels — it improves the prompt, it does not generate the asset, and it
never overrides the brand locks. If `raven` is absent, write prompts normally.

### The six creative laws (non-negotiable across lanes)

1. **One hero element per frame.** A number, a question, or a statement — never all three.
2. **70% negative space minimum.** If it feels empty, it's right.
3. **Two neutrals + one accent only.** No tonal middles.
4. **The price is the proof.** $500 appears as a value claim, not as a button label. "Read for $500" beats "Buy Now".
5. **No people in disrupt-grade work.** Pollinations human imagery goes only into retargeting / founder context, never into hero.
6. **Motion is opacity + 6px translate-y.** No bounces, no slides. Linear/Apple ease everything, never animate everything.

### Conversion-grade copy conventions (do this every time)

These are baked into the renderer's output quality — **violating them costs sales**.

1. **Every CTA ends with `→`** (the U+2192 right arrow). On editorial composites, append the arrow in the HTML CTA string. On animate / kinetic, the renderer appends it for you when the CTA field has no arrow.
2. **Week 1 CTAs trade in *waitlist* energy:** "Get on the list", "Reserve early access", "Notify me on launch". Avoid "Save the date" (event-y, not B2B).
3. **Week 2 CTAs *anchor the price*:** "Read the brief — $500", "Get the report — $500", "Download now — $500", "Buy for $500". Price anchoring is non-negotiable for $500 reports — confidence in pricing builds trust, and the $500 looks small next to "Bloomberg terminal" mental anchors.
4. **Every Week-2 eyebrow includes "$500"** (e.g. `AVAILABLE NOW · $500`, `BUNDLE-READY · $500`). The Week-1 eyebrow uses the publish date instead (`DROPS JUNE 1, 2026`, `CASPR. SELF-SERVE · DROPS <date>`).
5. **Every animate concept ships an `**On-screen eyebrow:**`** field — the renderer paints it in accent red above the headline. Default eyebrow: `GHOST RESEARCH` if you don't write one, but always write one.
6. **Headlines are *concrete, not categorical*.** "Demand signals are moving faster than ERP exports" beats "AI for supply chains". Lead with a specific job, a specific stack, a specific stakeholder.
7. **Subs are exactly two sentences max,** and one of those is a credibility line (`1M+ curated sources. Vetted by 10+ year domain SMEs.`).
8. **Ghost Research icon mark on every composite — NON-NEGOTIABLE.** Editorial HTML, animate, animated-html, and any composite step paints the icon mark (red `#EF4444` rounded-square with white inset circle) at the top-left of the safe zone. Source: `Ghost Research/assets/brand/logo-mark.svg` (vector, preferred for HTML) or `logo-mark.png` (512×512 transparent, for raster compositing). Inline the SVG into HTML via `<svg viewBox="0 0 100 100"><rect width="100" height="100" rx="22" fill="#EF4444"/><circle cx="50" cy="50" r="19" fill="#fff"/></svg>` — do NOT replace with a text wordmark. Badge size 88–112px on a 1080-wide canvas (always square, height = width). The mark works as-is on both dark and light backgrounds — no recolor needed. For video, the icon stays visible from frame 1 to last frame, including transitions and VFX cuts — never fades. Per-format placement (must respect ghost_visual_format_specs safe zones): 9:16 at x≈60, y≈290; 4:5 at x≈60, y≈60; 1:1 at x≈70, y≈70.
9. **9:16 video minimum runtime is 15 seconds.** Animate / animated-html / Veo prompts that target Reels or Stories must specify ≥15s. No 6/8/10s clips for vertical video.
10. **Uniform padding, no nested offsets.** Every composite uses 6.5% padding on all four sides of the canvas. If a concept uses a colored panel (e.g. red accent block), the panel must either bleed flush to the canvas edge OR respect the same 6.5% inset — never sit at a random offset like the Taylor Swift competitor ad. Text inside any panel inherits the same 6.5% inset from that panel's edges. Headline + sub live in the SAME left-aligned column.
11. **Font-size legibility floors** (on 1080-wide canvas; scale proportionally): headline ≥48px, sub/body ≥22px, eyebrow/kicker ≥18px, CTA ≥24px, wordmark ≥32px. Renderer's `editorial_template.html` enforces these via `clamp()` — don't override downward in concept-specific HTML.
12. **Every base-image prompt must be REPORT-SPECIFIC — #1 PRIORITY.** Subject's role and Setting's props/documents/screens must reference something only the actual report buyer would recognize — NOT generic editorial-business imagery. Apply the swap test: if the prompt still works with any other Ghost report title, rewrite it with a topic-specific prop. Examples: an IPO-window concept includes a printed S-1 prospectus or a Bloomberg pricing screen; a CFO defense concept includes a sensitivity analysis printout; a supply-chain concept includes a port congestion dashboard or container manifest. Forbidden: celebrity stock photos, generic "executive at laptop," generic "team in meeting room." If the visual-concepts.md Subject/Setting fails the swap test, do NOT pass it through — rewrite the generation prompt with topic-specific props before emitting.
13. **Light-theme concepts use `<body class="light">`.** Every campaign ships 1–2 light-theme concepts. When a visual concept's Color grade field begins with `LIGHT THEME`, the editorial HTML's opening body tag must be `<body class="light">` so editorial_template.html applies the cream/ink overrides. Dark-theme concepts use `<body>` (no class). When writing the animate or animated-html prompt for a light-theme concept, swap "deep indigo / navy color grade" for "paper-cream `#F8F8FF` background, deep ink `#06062D` text, accent red `#EF4444` unchanged, editorial daylight tonality, soft cool window light" in the base-image prompt. The base photo for light-theme concepts is shot in natural-daylight tonality, not cool indigo.
14. **Every headline uses an info-gap mechanism (see ghost_copy_uncommon_hooks).** Named villain / contrarian counter / hidden cost / time-decay urgency / specificity / insider POV. No generic "Discover insights..." filler — rewrite at the prompt-writing layer if visual-concepts.md let one slip through.
15. **NEVER mention any price in any ad copy** — not "$500", not "$1,000", not "starting at $X". Price reveals on the landing page only. CTAs become "Read the Atlas →" not "Read the Atlas — $500 →". Eyebrows become "AVAILABLE NOW" not "AVAILABLE NOW · $500". Subs strip "$500" too. Source: 2026-05-19 deck review.
16. **ICON MARK ON EVERY CREATIVE — non-negotiable, applies to every image, every video, every VFX frame.** Every composite HTML must embed the Ghost Research icon mark — a `#EF4444` rounded-square with a white inset circle — as inline SVG (NOT a text wordmark, NOT the stacked GHOST/RESEARCH text, NOT a "Ghost Research." string). Standard block:

    ```html
    <div class="gh-logo" aria-label="Ghost Research">
      <svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
        <rect x="0" y="0" width="100" height="100" rx="22" ry="22" fill="#EF4444"/>
        <circle cx="50" cy="50" r="19" fill="#FFFFFF"/>
      </svg>
    </div>
    ```

    CSS: `.gh-logo { width: clamp(72px, 8.5vh, 112px); height: clamp(72px, 8.5vh, 112px); display: block; flex-shrink: 0; } .gh-logo svg { width: 100%; height: 100%; display: block; }`

    The icon mark works as-is on both dark and light backgrounds — no recolor or `class="dark"` swap is needed. Source files: `Ghost Research/assets/brand/logo-mark.svg` and `logo-mark.png`. For video, the icon overlay paints automatically via animate_image.py's `build_text_overlay_png` (`_draw_logo_mark` helper) and stays on every frame including transitions.
17. **All static ads default to 1:1 (1080×1080)** unless a specific format requirement says otherwise. Reels/Stories video stay 9:16. 4:5 portrait feed is an exception that needs explicit justification.
18. **Every multi-shot video must pass persistent overlay to every Ken-Burns clip** — the headline + sub + CTA + eyebrow appear on EVERY frame from frame 1, not only at the final text card. `edit_multishot_reels.py` now passes the overlay tuple automatically when given headline/sub/cta args.
19. **Padding consistency rule made stricter:** outer padding is 6.5% of short edge, uniform on all four sides. Nested panels (red blocks, photo halves, document zones) all use the SAME 6.5% inset from their parent's edge. No random offsets, no nested 8%+6%+4% layers.
20. **Font-size legibility floors (updated 2026-05-19 review):** headline ≥56pt · sub/body ≥22pt · eyebrow/kicker ≥18pt · CTA button text ≥22pt · footer credibility line ("Caspr-powered · Expert-vetted · FERC-traceable") ≥17pt (bumped from prior 16pt floor — Shreyanshi explicitly flagged the C01 footer as 1-2 sizes too small) · wordmark visual height ≥32pt.

### 🆕 Template-review laws (2026-05-23 — Shreyanshi's file-by-file rating of the ai-energy deck)

21. **Build every editorial card from a named template** in `_shared/template-library.md` (A–F). Do not invent ad-hoc layouts. The loved set: Dark Photo Hero (real-stat), Journal Cover (T1), Pull-Quote (T8), Light Stat Card (FINAL-light2 / V3-C). Reproduce their chassis.
22. **The alignment law:** headline + big red stat + sub live in ONE left-aligned, bottom-anchored column with a single uniform vertical gap between elements. NEVER split headline-to-top and sub-to-bottom with dead space in the middle (the "weird space" flagged on T2/T4/T5/T6/T7). Every text element's left edge aligns to the same line.
23. **Thin red rounded-frame border** (`2px solid #EF4444`, radius 26–30px, inset ~18px) on every photo card. It's a Ghost signature.
24. **Blob structures behind content** — mandatory on every LIGHT card, subtle on dark. Use the standard `.blob-ring` (off-canvas thin circle, house position top-right) + `.blob-soft` (blurred radial fill) from template-library §0.2. Keep blob positions/sizes IDENTICAL across all cards in one campaign so the deck reads as a system. ("add blob structure" — c9, redo-launch-light, t8.)
25. **Footer sizes corrected:** `Ghostresearch.com` URL ≤23px (`clamp(19px,2.1vh,23px)`) — it was too large; the credibility line ≥19px for readability ("1M+ curated sources … increase font size a little" — c5). Neither dominates.
26. **🚫 BANNED — campaign-killers (template-library §2):** (a) AI-generated human faces — for humans use **real licensed stock only (e.g. Pexels), never FLUX**; (b) the **"GH⬛ST RESEARCH" icon-as-letter-O wordmark** — use the standalone icon, or icon + clean `GHOST RESEARCH` caps; (c) full-width solid orange/red banner strips (C8 "tacky"); (d) crude redaction-bar ledgers with dead space (T9); (e) busy SaaS dashboards with KPI tiles + lock icons (T3); (f) rigid 50/50 photo-top/text-bottom splits (C06/C11).
27. **CTA on every template, no exceptions** — even the journal cover (T1 was loved but lacked a CTA; always add the red `#EF4444` button with ` →`).
28. **Carousel consistency law:** every slide shares the IDENTICAL chassis — same background treatment, same masthead, same type scale, same frame, same footer/indicator. NEVER change panel/background color slide-to-slide (the C03 set failed: navy slide → red slide). Use Template E. A `→` button top-right + `/// ` or `1 / N · SWIPE →` indicator bottom-right.
29. **Framed-image (Template D / V3-C):** when a card shows a framed image on the right, make it confidently large (~38–42% width) — FINAL-light2's image was flagged "very small." Rounded-rect with a thin red edge.

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

**Default routing in 2026** (free tier, **image-only — videos paused since 2026-05-23**):
- Hero / scene shots → `pollinations` (text-free base) → `editorial` composite
- Headline / data / stat card → `editorial` (built from a template-library template)
- Hero "video" → **don't.** Ship a stronger Dark Photo Hero or Journal Cover still instead. Only emit `animate` / `animated-html` if the user explicitly asks for video this run.

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
**Style preset:** [carry over from visual-concepts.md — e.g. "Luxury", "Suspense + Instagram"]
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
