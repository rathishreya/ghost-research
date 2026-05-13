---
name: review-ads
description: Pull live ad performance via Supermetrics MCP for a Ghost Research campaign and compare against the brief's KPI Dashboard (Section 8) and Kill Switch thresholds (Section 10). Saves a snapshot tagged HOT/WARM/COLD per the brief's demand classification. Use when the user wants to check performance, says "how are the ads doing", "review the campaign", "/review-ads".
---

# Analytics Review Agent — Ghost Research

Your job: pull real performance data for the live campaign, compare against the **KPIs and thresholds the brief already defined**, and produce a clear digest.

## Step 1 — Find the active campaign

- If user named a slug, use that.
- Otherwise: read `data/pipeline.md`, find most recent slug with status `ready-to-publish` or later.
- Confirm: "Reviewing performance for: [slug]"

## Step 2 — Read the brief's KPI targets

Open `data/proposals/<slug>/campaign-brief.md`. Extract:
- **Feasibility math** (Section 0) — expected purchases, expected CPA, expected ROAS
- **Demand classification** (Section 0.1) — HOT / WARM / COLD (changes how aggressively to read signal)
- **Per-platform KPI tables** (Section 4)
- **Master KPI Dashboard** (Section 8) — the 3 numbers that matter most
- **Kill Switch triggers** (Section 10)

These are your benchmarks. Use them, not generic industry averages.

## Step 3 — Pull the data via Supermetrics MCP

Use the Supermetrics tools. For each platform listed in the brief's Section 2.1:

1. `data_source_discovery()` — find the platform's data source ID
2. `data_source_discovery(ds_id=X)` — get config
3. `accounts_discovery(ds_id=X)` — pick the ad account (if multiple, ask user; if one, use it)
4. `field_discovery(ds_id=X)` — get available fields
5. `data_query(...)` — pull date range = campaign start → today (or last 7 days, whichever is shorter)
6. `get_async_query_results(schedule_id=...)` — poll until ready

**Fields to pull per platform per ad:**
- Impressions, Reach, Frequency
- Clicks, CTR (link clicks specifically, not all clicks)
- CPM, CPC, Spend
- Conversions: `page_view` (report page), `initiate_checkout`, `purchase`
- Cost per conversion (cost per purchase)
- For video ads: video view percentages (25%, 50%, 75%, 100%)

Filter to ads where ad name contains `[slug]`.

If Supermetrics is unavailable or returns no data, tell the user and stop — never fabricate numbers.

## Step 4 — Compare to brief targets

For each metric, color-code:
- 🟢 At or beating brief target
- 🟡 Within 20% of target (margin)
- 🔴 Worse than 20% off target

For HOT classification campaigns, be stricter (10% margin instead of 20%) — there's no excuse to underperform when trend is in your favor.

For COLD classification campaigns, give 30% margin — building demand from cold takes longer.

## Step 5 — Check Kill Switch triggers

Explicitly check Section 10 conditions:

- [ ] **CTR check:** is CTR below brief threshold on ALL platforms simultaneously?
- [ ] **Page visit check:** zero report page visits after $[brief threshold] spent?
- [ ] **CPC check:** any platform CPC exceeding brief threshold with no improvement trend?
- [ ] **Days elapsed:** is campaign at Day 5+?

If ANY trigger fires → flag `KILL_SWITCH_RECOMMENDED` in the snapshot.

## Step 6 — Write the snapshot

Save to `data/proposals/<slug>/analytics/<YYYY-MM-DD>.md`:

```markdown
---
slug: [slug]
date: [YYYY-MM-DD]
period: "[start] to [end]"
days_live: [N]
days_remaining: [14 - N]
total_spend: $[X]
total_budget: $500
budget_consumed_pct: [X]%
demand_class: [HOT/WARM/COLD from brief]
kill_switch: [active / not-active]
status: snapshot
---

# Performance Snapshot — [slug] — [date]

## 🎯 Headline
[2-3 sentences. What's working, what's not, biggest surprise. Reference brief expectations.]

## 📊 Topline vs brief targets

| Metric | Actual | Brief target | Status |
|---|---|---|---|
| Total spend | $[X] of $500 | $[X] expected by day [N] | 🟢/🟡/🔴 |
| Total clicks | [N] | [from brief Section 0] | 🟢/🟡/🔴 |
| Report page visits | [N] | [from brief Section 8] | 🟢/🟡/🔴 |
| Purchases | [N] | [from brief Section 0] | 🟢/🟡/🔴 |
| Revenue | $[X] | $[X] | 🟢/🟡/🔴 |
| **Cost per purchase** | $[X] | $[X] from brief | 🟢/🟡/🔴 |
| **Blended CTR** | [X]% | [X]% from brief | 🟢/🟡/🔴 |
| **ROAS** | [X]× | [X]× from brief | 🟢/🟡/🔴 |

## 🚨 Kill Switch check

- CTR below brief threshold on ALL platforms? [Yes/No]
- Zero report page visits after brief threshold spend? [Yes/No]
- Any platform CPC exceeding brief threshold? [Yes/No — name platform if yes]
- Days elapsed ≥ 5? [Yes/No]

**Verdict:** [KILL SWITCH RECOMMENDED / no kill switch needed]

## 📈 Per-platform breakdown

### [Platform 1] — $[spend] of $[budgeted]
| Ad | Format | Impressions | CTR | CPC | CPL | Purchases | Verdict |
|---|---|---|---|---|---|---|---|
| [name] | | | | | | | 🟢/🟡/🔴 |

[Repeat for each platform from the brief]

## 🔥 Top performers (scale candidates)
| Ad | Platform | Why it's winning |
|---|---|---|

## ❄️ Underperformers (pause/replace candidates)
| Ad | Platform | Likely issue (from brief's expected failure modes) |
|---|---|---|

## 🔍 Funnel diagnosis

- Impressions → Clicks: [X]% (CTR)
- Clicks → Page visits: [X]% (clickthrough quality)
- Page visits → Initiate checkout: [X]%
- Initiate checkout → Purchase: [X]%

**Biggest leak:** [stage] — [why this is the weak link, and whether it's an ad problem or a landing page problem]

## 🎨 Creative fatigue check

[For each ad with frequency > 3.0, flag. If CTR has dropped >25% vs first 3 days, flag as fatigued.]

## 💡 What's surprising
[1-2 sentences. Something the data shows that wasn't predicted in the brief. Useful signal for memory: winning-patterns.md or losing-patterns.md.]

## ⏱ Time-remaining strategic note
Days remaining: [14 - N]. Budget remaining: $[X].
[1 sentence on what the optimal use of remaining budget + days looks like.]
```

## Step 7 — Update pipeline

Append: `[date] | [slug] | reviewed | day [N]/14 | spent $[X] | purchases [N] | ROAS [X]x`

## Step 8 — Hand off

Print the headline + topline table + kill switch verdict in chat. Then:

```
✅ Snapshot saved: data/proposals/[slug]/analytics/[date].md

[If kill switch triggered:]
🚨 KILL SWITCH RECOMMENDED — run /decide-action immediately for the protocol.

[Otherwise:]
Next step: /decide-action — read this snapshot and recommend SCALE / HOLD / REGENERATE / KILL per ad.
```

## Rules

- **Only report real data.** If Supermetrics returns nothing or fails, tell the user — never fabricate.
- **Always compare to the brief's targets first**, then to industry benchmarks as a secondary anchor. The brief is the contract; industry averages are just context.
- **If campaign is at Day < 3, warn the user** that data is too early for confident calls. Day 3-5 is when signal starts to mean something.
- **If total spend < $80, warn explicitly** — the brief's $500 cap means meaningful signal needs at least 15-20% of budget consumed before reading too much into it.
- **Always note the date range explicitly** so the user knows what window they're looking at.
- **For HOT campaigns, be aggressive.** For COLD campaigns, be patient. The classification in the brief tells you which lens to apply.
