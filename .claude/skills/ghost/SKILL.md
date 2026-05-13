---
name: ghost
description: Run the full Ghost Research marketing pipeline end-to-end — research topics, score Ghost fit and product-line fit, write the 2-week campaign brief for the chosen product, design Ghost-branded visual concepts, write Veo 3 + nanobanana prompts, and produce the launch operations checklist. Use when the user wants the whole loop, says "run the pipeline", "do the whole thing", "/ghost", or wants to start fresh on a new Ghost Research report.
---

# Ghost — Master Pipeline Orchestrator

You are running the full Ghost Research marketing pipeline. Walk the user through it step by step, but do not stop unless you need a decision from them.

## Sequence

Execute these skills in order. After each, give the user a one-line status update so they know where you are.

1. **research-topics** — find 8–12 Ghost-fit opportunities across off-the-shelf + Ghost Elite
2. **score-topics** — rank by Ghost brand fit + market potential, including product-fit
3. **PAUSE** — ask: "Top pick is **[title]** (score [X], brand fit [Y]). Proceed with this one, or want me to use #2/#3?" Wait for confirmation.
4. **PAUSE** — collect the remaining `/make-proposal` inputs:
   - **publish date**
   - **specific geography** within their region (e.g. `US only` vs `US+UK+Canada`)
   - **which product line to lead with** if the topic's `product_fit` is `both`
   - **Ghost Elite budget** if they choose Ghost Elite
   - **lead angle** if they already have one (optional)
5. **make-proposal** — produces the full 2-week campaign brief with the hard Week 1 hype-only / Week 2 content-live split
6. **design-ads** — expands the brief's 3 hooks + copy into 8–12 Ghost-branded visual concepts, split between hype-safe and content-active
7. **write-prompts** — turns concepts into ready-to-paste Veo 3 + nanobanana + ElevenLabs prompts
8. **prep-campaign** — produces the launch operations checklist (pre-flight, OG tags, pixels, click-by-click Ads Manager guide)

After step 8, hand off cleanly:

```
✅ Ghost pipeline complete for: [topic title]
   Product: [off-the-shelf | Ghost Elite]
   Total budget: [$500 or confirmed Elite budget] | Publish date: [date] | Platforms: [list]

📁 Everything is in: data/proposals/[slug]/
   ├── campaign-brief.md      ← the strategy + copy + day-by-day
   ├── visual-concepts.md     ← what each ad should look like
   ├── prompts.md             ← paste these into Veo 3 / nanobanana / ElevenLabs
   └── launch-checklist.md    ← step-by-step Ads Manager guide

Your next steps:
1. Generate assets (paste prompts.md prompts into Veo 3 + nanobanana) — ~1-2 hours
2. Composite final ads (overlay headlines + red CTA in Figma/Canva) — ~1 hour
3. Save assets into data/proposals/[slug]/assets/
4. Follow launch-checklist.md to publish on Ads Manager — ~60-90 minutes
   ⚠️ The OG meta tags check at the top is critical — don't skip it
5. Keep the structure intact:
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

- **Do NOT skip steps.** Each output feeds the next — `/design-ads` needs the brief, `/write-prompts` needs the concepts.
- **Do NOT auto-run** `/review-ads` or `/decide-action` — those require live ad data that doesn't exist until ads have been published and running.
- **If any sub-skill fails or asks for clarification, stop and surface that to the user** rather than guessing.
- **Save everything under** `data/proposals/<slug>/` where slug = kebab-case of the topic title.
- **Total Claude-side time** for the full pipeline is ~10-15 minutes of automated runs. The user then needs ~3-4 hours of manual asset generation + Ads Manager setup before ads go live.
- **Always enforce the Week 1 / Week 2 split.** Week 1 is hype-safe only; Week 2 is when report content becomes fair game.
- **If the topic is `both`, do not guess the lead product line.** Ask the user which one to lead with before `/make-proposal`.
- **Always remind about budget reality in the handoff.** Off-the-shelf stays capped at $500; Ghost Elite requires the user-confirmed higher budget from the brief.
