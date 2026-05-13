---
name: score-topics
description: Score and rank all unscored topic candidates in data/opportunities/ for Ghost Research fit. Adds a brand_fit score on top of urgency/gap/WTP/competition/ad-friendliness/SEO, and surfaces which product line (off-the-shelf vs Ghost Elite) each topic best fits. Use when the user wants to rank topics, says "score the topics", "which topic is best", "/score-topics", or right after /research-topics.
---

# Opportunity Scoring Engine — Ghost Research

Your job: read every unscored topic in `data/opportunities/` and assign scores so the user can pick the best one to spend ad budget on.

## What to score (each on 0.0–1.0 unless noted)

For each topic file with `status: unscored`:

| Field | Meaning | How to judge |
|---|---|---|
| `urgency` | How soon does the buyer need this? | 0.9+ = regulatory deadline / market shift within 90 days. 0.5 = nice to have. |
| `market_gap` | Is this info already easily available? | 1.0 = nobody is selling this synthesis. 0.3 = many competing reports cover it. |
| `willingness_to_pay` | $ amount (NOT 0-1) — realistic price | $500 / $750 / $1000 for off-the-shelf. For Ghost Elite, anchor at $5K-$25K+ depending on scope. Anchor on what comparable reports sell for. |
| `competition_density` | How many competitors exist? | 0.1 = no one. 1.0 = saturated (Gartner, Forrester, McKinsey, BCG, all here). |
| `ad_friendliness` | How easy is it to advertise on Meta/LinkedIn/X? | 0.9 = clean B2B topic. 0.3 = sensitive (health claims, financial advice, politically loaded). |
| `seo_potential` | Can we also rank organically? | 0.8 = clear search demand, low competition. 0.2 = no search volume. |
| `brand_fit` | How well does this play to Ghost Research's institutional, expert-verified, B2B-premium positioning? | 1.0 = ideal Ghost topic. 0.3 = doesn't really fit Ghost's brand. |
| `composite_score` | Weighted blend (formula below) | Auto-compute |
| `confidence` | How sure are you about these scores? | 0.7 = solid evidence. 0.3 = mostly guessing. |

## Brand fit factor — how to score it

`brand_fit` is the Ghost-specific filter. Score high if:
- ✅ B2B audience with budget authority (Investment Analysts, PE/M&A, Strategy Consultants, VPs/Directors/C-suite)
- ✅ Expert verification feasible (named domain experts exist who can vet)
- ✅ Audience in US/Europe/India/Middle East
- ✅ Topic benefits from 1M+ source synthesis and/or transparent citation as a credibility moat
- ✅ The buyer would describe Ghost as "the smartest analyst" not "a tool" or "a SaaS"
- ✅ Topic can be marketed in Ghost's voice — precise, authoritative, institutional-grade — without hype words
- ✅ Plays to "weeks → minutes" speed positioning OR "boardroom-ready synthesis" positioning

**AI-native synthesis bonus:** topics where the work is genuinely AI-leveraged (multi-source pattern detection at scale, comparative analysis across thousands of filings, real-time monitoring) get a small brand-fit bonus — Ghost's positioning is strongest here. But this is a bonus, not a requirement. Strong non-AI topics (e.g. real estate M&A landscape, healthcare device adoption) still score well if all the other criteria hold.

Score low if:
- ❌ Consumer / B2C / lifestyle
- ❌ Pure data dump with no synthesis required
- ❌ Saturated incumbent space with no clear angle (Gartner already owns it with no Ghost-side advantage)
- ❌ Requires generative AI clichés in marketing
- ❌ Sensitive regulated category that limits ad creative options

## Product line consideration

The topic's `product_fit` from `/research-topics` informs strategy but not scoring directly. Note in the output table which product line each topic targets:

- **off-the-shelf** topics → standard $500 campaign math, direct purchase funnel
- **ghost-elite** topics → lead-gen campaign math, enquiry form funnel, higher unit economics
- **both** topics → most flexible; can run as off-the-shelf with Elite cross-sell in Week 2

## Composite score formula

```
composite_score = (
    urgency * 0.20 +
    market_gap * 0.18 +
    (willingness_to_pay / 1000) * 0.15 +    # for Ghost Elite topics, cap this contribution at 1.0
    (1 - competition_density) * 0.13 +
    ad_friendliness * 0.10 +
    seo_potential * 0.07 +
    brand_fit * 0.17                              # weighted heavily — Ghost positioning matters
)
```

For Ghost Elite topics, cap the `willingness_to_pay` contribution at 1.0 (i.e. treat $10K+ WTP as 1.0 not 10.0) so it doesn't dominate the composite.

Round to 3 decimal places.

## How to apply scores

1. List all files in `data/opportunities/` where `status: unscored`.
2. For each: **read the evidence and reasoning** — don't just guess. Scores must reflect what's actually in the file.
3. If evidence is thin, lower `confidence` and be conservative on `urgency` and `willingness_to_pay`.
4. Edit the frontmatter to fill in all scoring fields and change `status: unscored` → `status: scored`.

## Output to the user

After scoring all files, print a ranked table:

```
RANKED OPPORTUNITIES — Ghost Research fit + market potential

#  Score  Brand fit  Title                                      Buyer                Region  Product       Conf
1  0.847  0.92       AI Compliance Playbook for Pharma R&D...   VP-AI at pharma      US      off-the-shelf 0.78
2  0.812  0.88       MENA Logistics M&A Landscape...            PE Director          ME      ghost-elite   0.71
...

Top pick: [Title]
Why: [2-3 sentences — usually the combination of high urgency × clear market gap × strong brand fit × ad-friendly. Note product line and what that means for the campaign.]

⚠️ Flags:
- [Any topic with ad_friendliness < 0.4] — regulated/sensitive, may face ad approval issues
- [Any topic with brand_fit < 0.5] — included but doesn't really fit Ghost; consider dropping
- [Any topic with confidence < 0.5] — evidence was thin, treat scores as provisional

Next step: /make-proposal (uses topic #1 by default — say "use #2" or name another to override)
```

## Rules

- **Don't be optimistic.** Inflated scores waste ad budget on bad picks.
- **Brand fit is a veto.** A topic scoring 0.9 on everything except 0.2 brand fit should NOT win — Ghost's positioning is more important than short-term ad performance. Flag it but rank it below better-fitting alternatives.
- **Tie-breaker:** higher `confidence`, then higher `ad_friendliness`, then higher `brand_fit`.
- **Flag risky topics explicitly** — anything with `ad_friendliness < 0.4` gets a ⚠️ in the table.
- Update `data/pipeline.md` with the scoring batch.