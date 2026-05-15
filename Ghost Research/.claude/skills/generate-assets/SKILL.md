---
name: generate-assets
description: Generate every static-image ad asset for a Ghost Research proposal. Dispatches each concept in `prompts.md` to the right backend — Tool=pollinations runs through Pollinations.ai (free FLUX), Tool=editorial renders HTML/CSS cards to PNG via headless Chromium. Saves all outputs into `data/proposals/<slug>/assets/`. Video concepts (Tool=animate / animated-html / veo) are handled by /generate-video, not this skill. Use when the user wants to generate images, runs `/generate-assets`, or moves from prompts into saved JPG/PNG assets.
---

# Asset Generation — Ghost Research (free stack)

Your job: take a proposal's `prompts.md`, dispatch every image concept to its
correct backend, and save outputs into `data/proposals/<slug>/assets/`.

Free stack — no API keys required for image generation:

| Tool field in prompts.md | Backend | Script |
|---|---|---|
| `pollinations` (or `nanobanana`, `flux`, `image`, `photo`) | Pollinations.ai free FLUX | `scripts/pollinations_image.py` |
| `editorial` | Playwright (headless Chromium) → PNG | `scripts/render_editorial.py` |
| `animate` / `animated-html` / `veo` | (deferred to /generate-video) | — |

## Step 1 — Find the proposal

- If the user names a slug, use that.
- Otherwise, find the most recently modified `data/proposals/<slug>/prompts.md`.

Read `data/proposals/<slug>/prompts.md`. If it doesn't exist, tell the user to
run `/write-prompts` first and stop.

## Step 2 — Dispatch by Tool

Run BOTH of these — each script only acts on its own Tool concepts and is a no-op
for the others.

```bash
python scripts/pollinations_image.py --slug <slug>
python scripts/render_editorial.py    --slug <slug>
```

Useful variants:

```bash
# Only one concept
python scripts/pollinations_image.py --slug <slug> --concept 03
python scripts/render_editorial.py    --slug <slug> --concept 02

# Regenerate over existing files
python scripts/pollinations_image.py --slug <slug> --overwrite

# Dry run — parse without calling APIs
python scripts/pollinations_image.py --slug <slug> --dry-run

# Pollinations model variants (flux is the default; try turbo for fastest)
python scripts/pollinations_image.py --slug <slug> --model flux-realism
```

Run both scripts in order. Surface their per-concept stdout to the user so
they can spot any failed concept and re-run it individually.

## Step 3 — Outputs

Saved into:

```text
data/proposals/<slug>/assets/
   ├── concept-01-*.jpg     ← Pollinations
   ├── concept-02-*.png     ← Editorial HTML
   └── ...
```

Editorial HTML source files are also persisted under
`data/proposals/<slug>/editorial/` so the user (or `/edit-ad`) can tweak and
re-render them.

## Step 4 — Update pipeline

Append a row to `data/pipeline.md`:

```text
[date] | [slug] | image assets generated | [N] images saved to assets/
```

## Step 5 — Hand off

```
Image assets saved: data/proposals/[slug]/assets/

What you should do next:
1. Open the assets folder and skim the outputs. Pollinations images can be hit-or-miss on first run — note any concept you want to change.
2. To change an ad: /edit-ad [concept-id] "your instruction in plain English"
   e.g. /edit-ad 03 "make the analyst look older and remove the city background"
3. To generate the videos: /generate-video
4. When everything looks right: /prep-campaign
```

## Rules

- Run **both** `pollinations_image.py` and `render_editorial.py` even if you
  don't think one will match — the scripts are no-ops if no concept matches.
- Do **not** route video concepts here — they belong to `/generate-video`.
- Surface actual stderr output to the user when a concept fails. Common
  Pollinations failures: timeout (transient — retry), too-small payload
  (prompt triggered a safety filter — rewrite and retry).
- Editorial HTML must include the Google Fonts link to load Oranienbaum +
  Manrope. If a render comes back with fallback fonts (Times / system serif),
  the HTML is broken — fix and re-render before showing the user.
- Do not commit `.env` or anything inside `data/proposals/<slug>/assets/`.
