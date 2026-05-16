---
name: generate-video
description: Generate every video ad for a Ghost Research proposal. Dispatches by Tool field — animate routes through Ken-Burns motion on the source still (free, ffmpeg), animated-html records CSS-animated HTML pages via headless Chromium (free), veo routes through Google Veo 3 Fast (paid Google AI Studio only, skipped on free tier). Saves MP4s into `data/proposals/<slug>/assets/`. Use when the user runs `/generate-video`, wants to generate the campaign's videos, or moves from images to motion.
---

# Video Generation — Ghost Research (free stack)

Your job: take a proposal's `prompts.md`, dispatch every video concept to the
right script, and save MP4s into `data/proposals/<slug>/assets/`.

Free stack — no API keys required:

| Tool field | Backend | Script |
|---|---|---|
| `animate` | Static image + Ken-Burns motion (moviepy + ffmpeg) | `scripts/animate_image.py` |
| `animated-html` | CSS animation recorded by Playwright (Chromium) | `scripts/render_animated.py` |
| `veo` | Google Veo 3 Fast | `scripts/gemini_video.py` (paid plan only — skip on free tier) |

## Step 1 — Confirm prerequisites

- A `prompts.md` exists at `data/proposals/<slug>/prompts.md`. If not, stop and
  tell the user to run `/write-prompts`.
- For every `animate` concept, its source image must already exist in
  `data/proposals/<slug>/assets/`. The animator looks for either the concept's
  own `Suggested filename` (stem) or the file named in a `**Source image:**`
  field. If a source is missing, tell the user to run `/generate-assets` first.
- For **publication-ready motion with copy on frame**, the concept body can
  include `**On-screen headline:**`, `**On-screen sub:**`, and
  `**On-screen CTA:**`. `animate_image.py` burns these in (Pillow overlay) on
  top of the Ken-Burns clip so the MP4 is not a silent plate.

## Step 2 — Dispatch

Run both free-tier scripts in order. Each is a no-op when no matching concept
is present.

```bash
python scripts/animate_image.py   --slug <slug>
python scripts/render_animated.py --slug <slug>
```

If the user has upgraded their Google AI Studio plan AND there are `veo`
concepts in `prompts.md`, also run:

```bash
python scripts/gemini_video.py --slug <slug>
```

Default behaviour: Veo concepts on the free tier are SKIPPED with a printed
notice. Do not call `gemini_video.py` unless the user has confirmed paid access.

Useful variants:

```bash
# Single concept
python scripts/animate_image.py   --slug <slug> --concept 04
python scripts/render_animated.py --slug <slug> --concept 05

# Override defaults on a one-off (only for single-concept use)
python scripts/animate_image.py --input assets/hero.jpg --out assets/hero.mp4 \
    --aspect 9:16 --duration 8 --motion zoom-in
```

## Step 3 — Quality bar

After all videos render, sanity-check each by reading the file size:

- `animate` outputs at ~3–6 MB for an 8-second 1080×1920 clip — anything
  under 300 KB means the source image was probably broken or the clip is
  too short. Surface this to the user.
- `animated-html` outputs are smaller (~1–4 MB) because the source is mostly
  flat colour with text.
- If a file is missing entirely, the script's stderr will say why. Don't pretend
  it succeeded.

## Step 4 — Update pipeline

Append: `[date] | [slug] | videos generated | [N] mp4s in assets/`

## Step 5 — Hand off

```
Video assets saved: data/proposals/[slug]/assets/

What you should do next:
1. Open the assets folder and play each MP4 — judge whether the motion sells
   the still. If a clip feels static where you wanted energy, switch its
   Motion: in prompts.md to a different option (zoom-out / pan-right / pan-left)
   and re-run /generate-video.
2. To change the still that an animate concept rides on:
     /edit-ad [source-concept-id] "your instruction"
   then re-run /generate-video for just the dependent video concept(s).
3. When everything looks right: /prep-campaign
```

## Rules

- Always run **both** `animate_image.py` and `render_animated.py` (each filters
  to its own Tool, so calling both is safe).
- Never silently call `gemini_video.py` — Veo requires a paid Google AI
  Studio plan and will 429 immediately on free tier. Only call it when the
  user has explicitly confirmed paid access.
- If an `animate` concept's source image is missing, do NOT generate a black
  video — print a clear error pointing the user to `/generate-assets`.
- For `animated-html`, the rendered HTML is also written to
  `data/proposals/<slug>/editorial/<filename>.html` so you can hand-tweak the
  animation timing and re-render with `--overwrite`.
- For `animate`, optional `**Skip if source missing:** yes` skips without failing
  the whole video batch when a source still (e.g. Pomelli import) is not on disk yet.
- Do not commit `data/proposals/<slug>/assets/` or `.../editorial/`.
