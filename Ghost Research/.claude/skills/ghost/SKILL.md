---
name: ghost
description: Run the full Ghost Research marketing pipeline end-to-end through real disk deliverables. Supports a default market-quality path (Google Imagen 4 Ultra stills when GEMINI_API_KEY is set, editorial cards, Ken-Burns + animated HTML MP4s; optional Veo 3 with user approval) plus optional free Pollinations tier. Use for "/ghost", "run the pipeline", or end-to-end delivery.
---

# Ghost — Master Pipeline Orchestrator

You are running the full Ghost Research marketing pipeline. Walk the user
through it step by step, but do not stop unless you need a decision from them.

**Baseline (no Google key):** Pollinations FLUX + Playwright + ffmpeg cover all
raster + motion.

**Market quality (recommended for flagship creative):** Put `GEMINI_API_KEY` from
https://aistudio.google.com/apikey in `Ghost Research/.env` so raster stills route
through **Imagen 4 Ultra**. Optional Veo clips need an upgraded Google AI Studio
plan and explicit user consent (`--veo` on `scripts/run_full_delivery.py`).

## Sequence

Execute these skills in order. After each, give the user a one-line status update.

1. **research-topics** — find 8–12 Ghost-fit opportunities (off-the-shelf + Elite)
2. **score-topics** — rank by Ghost brand fit + market potential + product-fit
3. **PAUSE** — confirm top pick: "Top pick is **[title]** (score [X], brand fit [Y]). Proceed with this one, or want me to use #2 / #3?"
4. **PAUSE** — collect remaining `/make-proposal` inputs:
   - **publish date**
   - **specific geography** within their region (e.g. `US only` vs `US+UK+Canada`)
   - **which product line to lead with** if the topic's `product_fit` is `both`
   - **Ghost Elite budget** if they choose Ghost Elite
   - **lead angle** if they already have one (optional)
5. **make-proposal** — produces the full 2-week campaign brief with the hard Week 1 hype-only / Week 2 content-live split
6. **design-ads** — expands the brief's 3 hooks into 8–12 Ghost-branded concepts (hype-safe + content-active)
7. **write-prompts** — turns each concept into a `prompts.md` block tagged with one of:
   - `Tool: pollinations` for photo / scene images
   - `Tool: editorial` for HTML/CSS typography & stat cards
   - `Tool: animate` for Ken-Burns motion on a still
   - `Tool: animated-html` for CSS-animated kinetic-type spots
   - `Tool: veo` (skipped on free tier — paid Google AI Studio only)
8. **media delivery (images + videos)** — run the one-shot helper from the
   `Ghost Research` directory so files land in `data/proposals/<slug>/assets/`:

   ```bash
   pip install -r requirements.txt    # first time only
   playwright install chromium        # first time only

   python scripts/run_full_delivery.py --slug <slug>
   ```

   - **Default `--tier market`:** Imagen 4 Ultra raster stills whenever
     `GEMINI_API_KEY` exists; otherwise stderr warns and Pollinations `flux-realism`
     is used. Editorial HTML → PNG and both free MP4 paths run automatically.
     Optional NanoBanana REST still works for `Tool: nanobanana-api` rows if
     `NANOBANANA_API_KEY` is configured.
   - **Free-only raster path:** add `--tier free` to force Pollinations.
   - **Veo photoreal video spots:** append `--veo` **only** after the user confirms
     paid Google AI Studio access (billable quota).

   *Legacy split:* you may still invoke `/generate-assets` + `/generate-video`
   manually if you need intermediate control.

9. **prep-campaign** — pre-flight checklist + click-by-click Ads Manager guide

After step 8, BEFORE prep-campaign, PAUSE and tell the user:

```
All ad assets are generated and saved in data/proposals/[slug]/assets/.
Open the folder and skim them.

If anything needs to change, run:
   /edit-ad <concept-id> "your instruction"
e.g. /edit-ad 03 "make the analyst look older and remove the city background"

When everything looks right, type /prep-campaign (or tell me "looks good" and I'll continue).
```

This pause is critical - it's where iteration happens. Don't skip it.

## Final hand-off

After step 9, hand off cleanly:

```
Ghost pipeline complete for: [topic title]
   Product: [off-the-shelf | Ghost Elite]
   Total budget: [$500 or confirmed Elite budget] | Publish date: [date] | Platforms: [list]

Everything is in: data/proposals/[slug]/
   ├── campaign-brief.md       <- the strategy + copy + day-by-day
   ├── visual-concepts.md      <- what each ad should look like
   ├── prompts.md              <- generation prompts, dispatched by Tool
   ├── editorial/              <- per-card HTML sources (for editorial / animated-html)
   ├── assets/                 <- final JPG / PNG / MP4 assets
   └── launch-checklist.md     <- step-by-step Ads Manager guide

Your next steps:
1. Decide which assets to use as primary vs A/B variants (you already have them all rendered)
2. (Optional) Composite final headlines + red CTAs onto images in Figma/Canva - about 1 hour total
3. Follow launch-checklist.md to publish on Ads Manager (~60-90 minutes)
   The OG meta tags check at the top is critical - don't skip it.
4. Keep the structure intact:
   - Week 1 (Days 1-7) = hype only, no report findings shown
   - Day 8 onward = report live, findings/charts/quotes can appear
   - Off-the-shelf campaigns default to a Ghost Elite cross-sell retargeting layer in Week 2

Once ads are live for 3 days, type /review-ads.
Once ads are live for 7 days, type /review-ads then /decide-action.
On Day 14, run /review-ads + /decide-action one final time and close the campaign.
```

## After the pipeline

Update `data/pipeline.md`: append a row with the new slug and `awaiting-publish` status.

## Resuming mid-pipeline

If the user runs `/ghost` for an existing slug:
- Read `data/pipeline.md` to find the last completed stage
- Resume from the next stage instead of starting over
- Skip stages whose output files already exist

## Rules

- **Do NOT skip steps.** Each output feeds the next.
- **Never substitute inline chat images** for `data/proposals/<slug>/assets/`
  - always run **`python scripts/run_full_delivery.py --slug <slug>`** (preferred) or the
  granular image scripts so Pollinations / Imagen / editorial / optional NanoBanana
  REST write real files.
- **Always complete media delivery before `/prep-campaign`.** The one-shot script
  renders both stills and motion; use `--tier free` only if the user refuses API keys.
- **Always pause after media delivery** - surface the assets folder so the user
  can spot anything off-brand and call `/edit-ad`.
- **Do NOT auto-run** `/review-ads` or `/decide-action` - those need live ad
  data that does not exist until ads have been published.
- **Veo is paid-only.** Only add `--veo` after the user explicitly acknowledges
  Google AI Studio billing; otherwise skip Veo rows.
- **Save everything under** `data/proposals/<slug>/` where slug = kebab-case of the topic title.
- **Total Claude-side runtime** depends on Imagen/Veo usage; budget enough time
  for multiple high-res stills plus ffmpeg motion.
- **Always enforce the Week 1 / Week 2 split.**
- **If the topic is `both`, do not guess the lead product line.** Ask first.
- **Always remind about budget reality in the handoff.** Off-the-shelf stays
  capped at $500; Ghost Elite needs the user's higher budget from the brief.
