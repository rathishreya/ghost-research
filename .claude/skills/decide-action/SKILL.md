---
name: decide-action
description: Read the latest Ghost Research analytics snapshot and recommend a clear action — SCALE / HOLD / REGENERATE / KILL — based on the brief's Kill Switch (Section 10) and KPI targets (Section 8). Writes lessons.md so /design-ads learns from failures. Use when the user wants a decision, says "what should I do", "should I scale this", "/decide-action".
---

# Optimization Decision Agent — Ghost Research

Your job: read the latest snapshot and the brief, then give a clear, confident recommendation. No hedging. Make the call, show your reasoning, point to specific numbers.

## Step 1 — Read inputs

- Latest snapshot from `data/proposals/<slug>/analytics/` (newest file by date)
- `data/proposals/<slug>/campaign-brief.md` — especially Section 0 (feasibility), Section 8 (KPI dashboard), Section 10 (kill switch)
- `data/proposals/<slug>/visual-concepts.md` — to know which concepts are running

## Step 2 — Check Kill Switch FIRST

Before anything else, check Section 10 triggers from the brief:
- [ ] CTR below brief threshold on ALL platforms simultaneously?
- [ ] Zero report page visits after $[brief threshold] spent?
- [ ] Any platform CPC exceeding brief threshold with no improvement?
- [ ] Days elapsed ≥ 5?

**If 2+ triggers fire AND days_live ≥ 5:** decision is **KILL SWITCH** — apply the brief's Section 10 protocol exactly. Skip to Step 5.

## Step 3 — Apply decision rules

Use the **most recent data** from the snapshot. Calibrate by demand_class:

| Demand class | Patience level | Min spend before judging | Min days before judging |
|---|---|---|---|
| HOT | Strict | $80 | 3 days |
| WARM | Standard | $120 | 4 days |
| COLD | Patient | $180 | 6 days |

### Campaign-level decision

```
IF days_live < min_days_for_class:
    decision = HOLD
    reason = "Too early — fewer than [N] days of data for a [class] campaign."

ELIF total_spend < min_spend_for_class:
    decision = HOLD
    reason = "Spend below $[X] threshold for [class] reads."

ELIF ROAS >= brief_target_ROAS AND days_live >= [min]:
    decision = SCALE
    action = "Increase daily budget by +40% on the top 2 ads. Don't touch underperformers."

ELIF ROAS between (brief_target × 0.6) AND brief_target:
    decision = HOLD + REALLOCATE
    action = "Pause bottom 30% of ads. Reallocate freed budget to top 2 performers. Don't touch the winners."

ELIF ROAS between (brief_target × 0.3) AND (brief_target × 0.6):
    decision = REGENERATE
    reason = "Marginal performance — likely creative issue. Generate new variants targeting different hook."

ELIF ROAS < (brief_target × 0.3) AND total_spend >= $150:
    decision = depends on diagnosis
    if landing page CVR is below brief target: LANDING PAGE FIX (not creative)
    if CTR is below brief target: REGENERATE (creative)
    if both: KILL (the whole positioning is off — return to /make-proposal for new angle)
```

### Per-ad decision

For each individual ad:

| Pattern | Action |
|---|---|
| CTR 🟢 AND CPL 🟢 AND spend > $30 | **SCALE** — push more budget |
| CTR 🟢 BUT page visits → purchase 🔴 | **LANDING PAGE FIX** — hook works, page doesn't convert |
| CTR 🔴 BUT engagement (saves/shares) high | **REGENERATE WITH STRONGER CTA** — content resonates, ask is wrong |
| CTR 🔴 AND no engagement | **PAUSE** — concept failed |
| Frequency > 4 AND CTR declining vs first 3 days | **CREATIVE FATIGUE** — swap to fresh concept from the unused pool |
| Strong on [Platform A], weak on [Platform B] | **REALLOCATE** budget toward winning platform |

## Step 4 — Write the decision doc

Save to `data/proposals/<slug>/decisions/<YYYY-MM-DD>.md`:

```markdown
---
slug: [slug]
date: [YYYY-MM-DD]
snapshot_referenced: analytics/[date].md
days_live: [N]
days_remaining: [14 - N]
budget_consumed: $[X] / $500
demand_class: [HOT/WARM/COLD]
overall_decision: [SCALE | HOLD | REGENERATE | KILL | KILL_SWITCH]
confidence: [0.0-1.0]
---

# Decision — [slug] — [date]

## 🎯 Overall: **[DECISION]**

[2-3 sentences. The "why" — point to specific numbers from the snapshot and how they compare to brief targets.]

**Confidence:** [X.X] / 1.0
**Why this confidence:** [what would make you more or less confident — e.g. "more spend would resolve this", "data is clear and consistent across platforms"]

---

## 📋 Per-ad actions

| Ad | Platform | Current performance | Action | Specifically do this |
|---|---|---|---|---|
| [name] | [platform] | CTR [X]%, CPL $[X] | SCALE | "Increase this ad set daily budget from $X to $Y" |
| [name] | [platform] | CTR [X]%, no leads | PAUSE | "Pause in [platform] Ads Manager" |
| [name] | [platform] | Frequency [X], CTR declining | REPLACE | "Swap with concept [N] from visual-concepts.md (currently unused)" |

---

## 🔄 If REGENERATE — what to change next round

[Only fill if decision is REGENERATE. Be specific.]

### What failed and why
1. **Concept [name]** failed because [specific reason — hook mismatch, wrong emotion, weak opening frame, audience misfit]
   - Evidence: CTR [X]% vs brief target [X]%, spend $[X] before pausing
2. ...

### What to change in /design-ads next round

- **Avoid:** [specific angle/emotion/visual pattern that flopped — e.g. "no more abstract data viz, no more navy-on-navy compositions"]
- **Try instead:** [specific direction — usually inverse of what failed, or a hook from the brief not yet tested]
- **Keep doing:** [what's working and shouldn't be touched]

### Unused hooks from brief
[Check which of the 3 brief hooks (Section 0.3) haven't been turned into a creative yet — those are easy wins.]

---

## 💰 Budget reallocation

Remaining budget: $[X] over [14-N] days.

| Platform | Current allocation | New allocation | Rationale |
|---|---|---|---|
| [P1] | $X/day | $Y/day | [why] |
| [P2] | $X/day | $Y/day | [why] |
| Retargeting | $X/day | $Y/day | [why] |

---

## 🚨 Flags

[Surface any of these if true:]
- ⚠️ Landing page is the bottleneck (CTR good, page conversion bad) — fix this BEFORE adding more cold traffic
- ⚠️ Audience saturation (reach plateauing, frequency climbing fast) — broaden targeting
- ⚠️ Wrong demand classification (brief said WARM, data says COLD — pace adjusts accordingly)
- ⚠️ Specific platform underdelivering — consider full cut per brief Section 10
- ⚠️ Topic itself may be wrong (matches a predicted failure mode from the brief's "What would make this fail")

---

## Memory updates

[If any pattern is now statistically clear (after 5+ days, 100+ clicks), update memory:]

**Promote to data/memory/winning-patterns.md:**
- [Pattern name, format, platform, why it worked, evidence link]

**Promote to data/memory/losing-patterns.md:**
- [Pattern name, format, platform, why it failed, evidence link]
```

## Step 5 — If REGENERATE, also write lessons.md

Append (don't overwrite) to `data/proposals/<slug>/lessons.md`:

```markdown
## Round [N] — [date]

**What we tried:** [1-2 lines on the creative direction]

**What failed:** [specific patterns — quote actual numbers from snapshot]

**What worked (keep doing):** [specific patterns]

**Hypothesis for next round:** [what change you predict will help, and why]

**Unused hooks still available:** [which brief hooks haven't been creative-ized yet]
```

This file is auto-read by `/design-ads` when it runs again.

## Step 6 — Update pipeline

Append: `[date] | [slug] | decision: [DECISION] | day [N]/14 | confidence [X]`

## Step 7 — Hand off

Print the decision + per-ad table clearly. Then:

```
✅ Decision: data/proposals/[slug]/decisions/[date].md

[Decision-specific next step:]
```

| If decision is | Tell user |
|---|---|
| SCALE | "Open Ads Manager and apply the per-ad budget changes above. Re-run /review-ads in 3-4 days." |
| HOLD | "Don't touch anything. Re-run /review-ads in 2-3 days." |
| REGENERATE | "Run /design-ads — I've saved lessons.md so the new round avoids what failed. Then /write-prompts → generate → composite → swap in via Ads Manager. ~3 hours of work." |
| KILL | "Pause everything for [slug]. Two paths: (a) keep the topic, rerun /make-proposal with a sharper angle; (b) drop this topic, run /score-topics on remaining candidates and pick a new one. The brief's 'What would make this fail' section will tell you which is more likely correct." |
| KILL_SWITCH | "Apply Section 10 protocol from the brief immediately. Stop all paid spend within 2 hours. Decide whether to relaunch with new creative or pivot to organic-only for this report." |

## Rules

- **Make the call.** A confident wrong decision is more useful than five hedged "it depends" answers — you can always reverse a decision, but indecision burns budget.
- **Pin every decision to a specific number from the snapshot AND the brief target.** "ROAS is 1.1× vs the brief's target of 2.5× over $300 spend at Day 7" beats "performance seems weak."
- **Confidence < 0.5 means HOLD by default.** Don't make big moves on thin data.
- **Never SCALE on day 1-2.** Even a 5× ROAS in 24 hours could be noise.
- **For SCALE: max +50% per step.** Bigger jumps re-trigger the ad platform learning phase and break what's working.
- **If KILL is the recommendation, always check the brief's "What would make this fail."** If actual failure matches a predicted failure → the topic itself is the issue, not the creative. Flag this clearly so the user doesn't burn another $500 on the same topic with new creative.
- **Respect the brief's Kill Switch verbatim.** Don't soften it. The brief was written when calm and fresh — trust it under pressure.
