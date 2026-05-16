---
name: generate-assets
description: Generate every static-image ad asset for a Ghost Research proposal. Prefer `scripts/generate_proposal_assets.py` (pins repo root): Tool=pollinations via Pollinations.ai (default flux-realism); Tool=nanobanana-api via paid REST when key set; Tool=editorial via Playwright PNG. Never substitute chat/inline images for campaign files. Use when the user wants `/generate-assets` or images in `data/proposals/<slug>/assets/`.
---

# Asset Generation — Ghost Research (free stack)

Your job: take a proposal's `prompts.md`, dispatch every image concept to its
correct backend, and save outputs into `data/proposals/<slug>/assets/`.

**Critical — outputs never come from chat or inline IDE image previews.** Do not
"draw" creatives, screenshot examples, or use multimodal image generation for
campaign assets. The only valid pipeline is executing the scripts below against
disk files so JPEG/PNG land in `data/proposals/<slug>/assets/` (video is `/generate-video`).

Free stack — no API keys required for Pollinations / editorial routing:

| Tool field in prompts.md | Backend | Routed by |
|---|---|---|
| `pollinations` (or legacy `nanobanana`, `flux`, `image`, `photo`) | Pollinations.ai free FLUX | `generate_proposal_assets.py` → `pollinations_image.py` |
| `nanobanana-api` | Paid NanoBanana REST (`NANOBANANA_API_KEY`) | Same launcher → `nanobanana_generate.py` (skipped if no key) |
| `editorial` | Playwright (headless Chromium) → PNG | `generate_proposal_assets.py` → `render_editorial.py` |
| `animate` / `animated-html` / `veo` | (deferred to /generate-video) | — |

**Composite ads (photo + headline + CTA in one PNG):** In `editorial` HTML, reference existing JPG/PNG in `assets/` with `url("GHOST_ASSET:filename.jpg")`. `render_editorial.py` rewrites that token to a `file://` URL before screenshot. Base photos must be generated first (lower concept IDs first helps).

**Pomelli (Google Labs):** There is **no public Pomelli API**. Use the inbox bridge: export from [Pomelli](https://labs.google.com/pomelli/) into `data/proposals/<slug>/pomelli-inbox/` (name files `concept-01.png` or `01.jpg`), then run `python scripts/import_pomelli_exports.py --slug <slug> --overwrite` or chain `python scripts/generate_proposal_assets.py --slug <slug> --import-pomelli-inbox` (runs import first; empty inbox is OK). See `import_pomelli_exports.py --help` for `--manifest` and `--open-ui`.

## Step 1 — Find the proposal

- If the user names a slug, use that.
- Otherwise, find the most recently modified `data/proposals/<slug>/prompts.md`.

Read `data/proposals/<slug>/prompts.md`. If it doesn't exist, tell the user to
run `/write-prompts` first and stop.

## Step 2 — Run the launcher (preferred)

Always run **`scripts/generate_proposal_assets.py`**. It pins the repo root (`Ghost Research/`), so cwd does not matter.

```bash
cd "Ghost Research"
python scripts/generate_proposal_assets.py --slug <slug>
```

On Windows in Cursor/PowerShell, if the workspace root is already `Ghost Research`, the same command works bare.

Equivalent low-level invocation (avoid unless debugging):

```bash
python scripts/pollinations_image.py --slug <slug>
python scripts/render_editorial.py    --slug <slug>
```

Useful launcher variants:

```bash
python scripts/generate_proposal_assets.py --slug <slug> --concept 03
python scripts/generate_proposal_assets.py --slug <slug> --overwrite
python scripts/generate_proposal_assets.py --slug <slug> --dry-run
python scripts/generate_proposal_assets.py --slug <slug> --pollinations-model flux-realism
python scripts/generate_proposal_assets.py --slug <slug> --import-pomelli-inbox
```

Default Pollinations profile is **`flux-realism`** (photoreal). Use `--pollinations-model turbo` only for speed drafts.

Paste full stdout/stderr into the transcript so failures are actionable.

**Market-tier still photos (recommended when `GEMINI_API_KEY` is in `.env`):**

```bash
python scripts/generate_proposal_assets.py --slug <slug> --premium
```

This routes every `Tool: pollinations` still through **Google Imagen 4 Ultra**, skips redundant Pollinations calls, keeps editorial renders, then optional NanoBanana REST.

**Manual Imagen invocation** only when debugging generators:

```bash
python scripts/gemini_image.py --slug <slug> --quality ultra --routes-pollinations
```

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

- Run **`generate_proposal_assets.py`** (preferred) or **both** standalone
  image scripts — each only acts on concepts it owns; the launcher runs them in
  order with a fixed working directory.
- **Never** illustrate campaign assets using chat/IDE image generation — only files
  saved under `assets/` are deliverables.
- Do **not** route video concepts here — they belong to `/generate-video`.
- Surface actual stderr output to the user when a concept fails. Common
  Pollinations failures: timeout (transient — retry), too-small payload
  (prompt triggered a safety filter — rewrite and retry).
- Editorial HTML must include the Google Fonts link to load Oranienbaum +
  Manrope. If a render comes back with fallback fonts (Times / system serif),
  the HTML is broken — fix and re-render before showing the user.
- Do not commit `.env` or anything inside `data/proposals/<slug>/assets/`.
