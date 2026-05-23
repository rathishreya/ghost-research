# Ghost Pipeline — Live Status

This file tracks every topic and where it is in the pipeline. Updated automatically by each skill.

## Stages

`researched` → `scored` → `proposal drafted` → `creatives designed` → `prompts written` → `assets generated` → `campaign prepped` → `awaiting publish` → `live` → `reviewed` → `decision [X]`

## Active topics

- **de-minimis-repeal-ecommerce-2026** — campaign prepped / awaiting publish (Mon 2026-06-01 start, publish Sun 2026-06-07) ← new, full /ghost run
- **ai-energy-demand-2026** — campaign prepped / awaiting publish (Mon 2026-06-01)
- **vsaas-bloodbath-2026** — proposals folder in flight
- **ipo-window-2026** — shipped (assets generated, campaign prepped)
- **cfo-defense-pack-q2-2026** — shipped
- **enterprise-ai-roi-2026** — shipped
- **supply-chain-ai-forecast** — shipped (demo run 2026-05-16)

## Log

| Date | Slug | Stage | Notes |
|---|---|---|---|
| 2026-05-16 | supply-chain-ai-forecast | prompts written | Automated pipeline seed + media delivery |
| 2026-05-16 | supply-chain-ai-forecast | assets generated | 14-day prompts: composites (GHOST_ASSET) + 3 Pollinations bases + 2 animate + 2 animated-html |
| 2026-05-18 | ai-energy-demand-2026 | proposal drafted | First campaign on new quality standards: image-relevance gate, 2 light-theme concepts, info-gap hooks (5 of 6 mechanisms used) |
| 2026-05-18 | ai-energy-demand-2026 | creatives designed | 12 concepts (10 dark + 2 light); every concept swap-test verified; videos ≥15s |
| 2026-05-18 | ai-energy-demand-2026 | prompts written | 22 prompts: 8 Imagen Ultra bases + 12 editorial composites (2 with body.light) + 2 animate motion |
| 2026-05-18 | ai-energy-demand-2026 | campaign prepped | launch-checklist.md ready; awaiting Mon 2026-05-25 launch |
| 2026-05-19 | ai-energy-demand-2026 | creatives v2 (bold) | 4 hero photos + 4 composites rewritten with Platon-portrait recipe + red-block tabloid layout; light-theme text fixed to #000000 |
| 2026-05-19 | ai-energy-demand-2026 | videos v2 (multi-shot) | C04 (16.2s) + C10 (18.2s) re-rendered as 3-clip cross-dissolve trailers via edit_multishot_reels.py |
| 2026-05-22 | ai-energy-demand-2026 | creatives designed (preset edition) | 13 concepts in visual-concepts-presets.md (7 hype-safe + 6 content-active); preset mix: Wk1 cinematic+suspense, Wk2 UI-heavy+SaaS; original visual-concepts.md preserved |
| 2026-05-22 | ai-energy-demand-2026 | creatives REDESIGNED (premium editorial, free) | After quality feedback: tested all paid generators (Vibiz 0 credits, Imagen=paid plan) → went free editorial. 8 cards on shared editorial/_ghost-kit.css: Economist-style masthead+data charts, Wk1 REDACTED / Wk2 revealed, light+dark, legibility floors raised, 2025→2026 fixed. REDO-*.png in assets/. Videos (animated-html) pending. |
| 2026-05-23 | (research batch) | researched | 12 fresh topics across 12 untapped verticals (CRE, reinsurance, pharma GLP-1, PE/NAV-loans, stablecoin/GENIUS, defense/ReArm, fiber-DC, legacy chips, de-minimis, MDR, EU-AI-Act, IMO shipping). 3 real URLs each. |
| 2026-05-23 | (scoring batch) | scored | Top 5: fiber-glass-bottleneck (0.794), nav-lending (0.727), de-minimis-repeal (0.727), cre-maturity-wall (0.726), reinsurance-reversal (0.724). Awaiting topic confirmation. |
| 2026-05-23 | de-minimis-repeal-ecommerce-2026 | proposal drafted | Off-the-shelf $500 + Elite cross-sell. Global/multi. Publish Sun 7 Jun 2026 (Wk1 1-7 Jun hype / Wk2 8-14 Jun convert). HOT demand. Platforms: Meta $230 / LinkedIn $170 / X $100. Hooks: time-decay / hidden-cost / specificity. |
| 2026-05-23 | de-minimis-repeal-ecommerce-2026 | creatives designed | 12 concepts (10 dark + 2 light: C04 €150→?, C11 which-SKUs). No AI humans — objects/UI/type. Swap-test verified. 2 videos ≥15s (C02 16s kinetic, C09 17s cinematic). |
| 2026-05-23 | de-minimis-repeal-ecommerce-2026 | prompts written | 14 generation blocks: 3 Imagen/FLUX photo bases + 9 editorial cards/composites (2 body.light, 3 GHOST_ASSET composites) + 2 videos. Icon-mark SVG on every card. No price in copy. |
| 2026-05-23 | de-minimis-repeal-ecommerce-2026 | assets generated | 14 files in assets/ (FLUX bases — Google plan lacks Imagen; composites 2.6-3MB OK). QA'd C01/C03/C04/C08: logo present, no AI humans, legible, single red focal point, light-theme cream/ink correct. Videos: C02 16s kinetic, C09 17s cinematic. Ran with PYTHONUTF8=1 (cp1252 console + → arrow). |
| 2026-05-23 | de-minimis-repeal-ecommerce-2026 | campaign prepped | launch-checklist.md ready: OG-tag pre-flight (both pages), pixels, audiences, $230/$170/$100 caps, pre-built UTM URLs per concept, Day 1/5/8 + check-ins, kill switch. Awaiting Mon 2026-06-01 launch. Full /ghost run complete end-to-end. |
| 2026-05-23 | de-minimis-repeal-ecommerce-2026 | creatives REBUILT (template-library v2) | After Shreyanshi's taste review: rebuilt all 12 cards on approved templates (A Dark Photo Hero, B Journal Cover, C Pull-Quote, D Light Stat Card). Added red frame, clean icon+wordmark masthead, blobs, bottom-anchored alignment, corrected footer sizes, CTA on every card. Videos dropped (C02→pull-quote, C09→journal launch stills); C08 table→stat-hero. 12 PNGs re-rendered, QA'd. launch-checklist + visual-concepts updated. New rules codified in _shared/template-library.md + design-ads/write-prompts/style-presets. |
