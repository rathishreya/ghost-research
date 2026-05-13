---
name: prep-campaign
description: Pre-flight technical setup + click-by-click Ads Manager checklist for a Ghost Research campaign. Verifies OG meta tags, pixels, UTMs, retargeting audiences, $500 budget caps are all in place before Day 1. The campaign brief already has platform splits + ad copy — this skill is the launch operations layer. Use when assets are generated and the user is ready to publish, says "prep the campaign", "/prep-campaign".
---

# Campaign Launch Operations — Ghost Research

Your job: verify everything is technically ready and produce a click-by-click checklist the user follows in Meta / LinkedIn / X / Instagram Ads Manager. The campaign brief already specifies budgets, audiences, copy, and visuals — you do NOT redesign those. You produce the **launch operations layer**.

## Step 1 — Confirm assets exist

Check `data/proposals/<slug>/assets/`. If it's empty or missing final composited files, tell the user:

```
⚠️ Assets folder is empty or incomplete: data/proposals/[slug]/assets/
Please generate and composite assets using prompts.md first, then re-run /prep-campaign.
```

Then stop.

## Step 2 — Read inputs

- `data/proposals/<slug>/campaign-brief.md` — for platforms, budgets, audiences, copy, schedule, KPIs
- `data/proposals/<slug>/visual-concepts.md` — for asset-to-day mapping
- `data/proposals/<slug>/prompts.md` — for asset filenames

## Step 3 — Write the launch checklist

Save to `data/proposals/<slug>/launch-checklist.md`:

```markdown
---
slug: [slug]
created: [YYYY-MM-DD]
publish_date: [from brief]
platforms: [list from brief Section 2.1]
total_budget: $500
status: ready-to-publish
---

# Launch Checklist — [Report Title]

> Follow this top to bottom. Don't skip pre-flight — Ghost Research's #1 launch failure is OG meta tags missing, which makes every link preview render blank.

---

## 🚨 PRE-FLIGHT — must complete before any ad goes live

### Website / report page
- [ ] Report URL is live: `ghostresearch.com/[report-slug]`
- [ ] Page loads correctly on **mobile** (test on your phone, not just desktop)
- [ ] **OG meta tags set on the report page:**
  - [ ] `og:title` = "[Report title]"
  - [ ] `og:description` = "[2-line description from brief]"
  - [ ] `og:image` = a 1200×630 hero image (use one of the concepts from visual-concepts.md, or design tool)
  - [ ] `og:url` = the full report URL
  - [ ] `twitter:card` = "summary_large_image"
  - **How to verify:** paste the report URL into [opengraph.xyz](https://www.opengraph.xyz) — preview should show the hero image and title, not blank
- [ ] Purchase flow works end-to-end (test with a $0.01 transaction or coupon)

### Tracking pixels
- [ ] **Meta Pixel** installed on report page (test with Meta Pixel Helper Chrome extension — must show "active")
- [ ] **LinkedIn Insight Tag** installed (only if running LinkedIn — verify in Campaign Manager → Account Assets → Insight Tag)
- [ ] **X / Twitter Pixel** installed (only if running X — verify in Ads Manager → Tools → Conversion Tracking)
- [ ] Conversion events defined on each pixel:
  - [ ] `page_view` (fires on report page load)
  - [ ] `initiate_checkout` (fires on add-to-cart click)
  - [ ] `purchase` (fires on order confirmation)

### Audiences (create BEFORE Day 1 — retargeting needs them ready by Day 8)
- [ ] **Meta:** Custom audience "Visited [slug] page — last 30d" (URL contains [report-slug])
- [ ] **Meta:** Custom audience "Initiated checkout — no purchase, last 14d"
- [ ] **Meta:** Lookalike audience 1% off Initiate Checkout audience (requires source size 100+)
- [ ] **LinkedIn:** Matched audience "Visited [slug] page — last 30d"
- [ ] **X:** Tailored audience "Engaged with [campaign hashtag] tweet"

### Budget caps (account-level safety net)
- [ ] **Meta:** Account spending limit set to $[total Meta budget] in Billing settings
- [ ] **LinkedIn:** Campaign group total budget set to $[LinkedIn budget]
- [ ] **X:** Daily account spend cap to $[X budget / 14] in Settings
- [ ] **All platforms:** Each campaign has end date = publish_date + 7 days (so nothing runs longer than 14 days total)

### UTM scheme — paste into a doc you keep open

All destination URLs use this scheme:

```
https://ghostresearch.com/[report-slug]?utm_source=[platform]&utm_medium=paidsocial&utm_campaign=[slug]&utm_content=[concept-name]&utm_term=[week1|week2|retargeting]
```

**Pre-built URLs for this campaign** (copy these directly when setting up ads):

| Platform | Week | URL |
|---|---|---|
| Meta IG | Week 1 | https://ghostresearch.com/[slug]?utm_source=instagram&utm_medium=paidsocial&utm_campaign=[slug]&utm_content=[concept-01]&utm_term=week1 |
| Meta IG | Week 2 | https://ghostresearch.com/[slug]?utm_source=instagram&utm_medium=paidsocial&utm_campaign=[slug]&utm_content=[concept-02]&utm_term=week2 |
| Meta IG | Retargeting | https://ghostresearch.com/[slug]?utm_source=instagram&utm_medium=paidsocial&utm_campaign=[slug]&utm_content=[concept-rtg]&utm_term=retargeting |
| LinkedIn | Week 1 | ... |
| ... | ... | ... |

[Generate one row per platform × week × concept actually being run, based on the calendar in campaign-brief.md Section 3.]

---

## 🚀 DAY 1 — LAUNCH SEQUENCE

Read these in order. Don't skip ahead.

### Step 1 — Open the campaign brief alongside this checklist
Have `data/proposals/[slug]/campaign-brief.md` open in another tab. You'll reference Section 3 (calendar), Section 4 (per-platform), and Section 7 (copy vault) constantly.

### Step 2 — [Highest-priority platform from brief, e.g. LinkedIn]

Time required: ~20 minutes

1. [ ] Open [LinkedIn] Campaign Manager → Create new campaign group → name it `[YYYY-MM] [Slug]`
2. [ ] Set group total budget: $[LinkedIn budget from brief]
3. [ ] Create Campaign 1 with these settings (copied from brief Section 4):
   - **Objective:** [from brief]
   - **Audience:** [paste targeting from brief Section 4]
   - **Daily budget:** $[from brief]
   - **Bid:** [from brief]
   - **Schedule:** Start [publish_date − 7], end [publish_date + 7]
4. [ ] For each ad in Week 1 (per Section 3 calendar):
   - [ ] Click "Create Ad"
   - [ ] Format: [from brief]
   - [ ] Upload: `data/proposals/[slug]/assets/[filename].[ext]`
   - [ ] Headline: paste from Section 7 of brief
   - [ ] Intro text: paste from Section 7
   - [ ] CTA: [from brief]
   - [ ] Destination URL: [paste pre-built UTM URL from table above]
5. [ ] Submit all ads for review
6. [ ] **Do NOT yet build retargeting campaign** — set a calendar reminder for Day 8

### Step 3 — [Next platform]

Time required: ~20 minutes

[Same structure as above]

### Step 4 — [Next platform if applicable]

[Same structure]

### Step 5 — Verify
- [ ] All ads submitted on all platforms?
- [ ] All ads APPROVED (check 2-4 hours after submission)?
- [ ] If any rejected: paste the rejection reason into Claude chat and ask for a copy/visual revision
- [ ] Spend $5 on each platform (visit your own ad → click → land on report page). Verify:
  - [ ] Click lands on correct URL
  - [ ] UTM parameters appear in URL after redirect
  - [ ] Meta Pixel Helper / LinkedIn Insight Tag fires page_view
  - [ ] UTMs show up in your website analytics within 30 minutes

---

## 📅 DAY 8 — RETARGETING ACTIVATION

(Calendar reminder you set on Day 1.)

By now you'll have ~7 days of cold traffic data. Retargeting audiences should be populated.

1. [ ] Verify retargeting audience sizes:
   - Meta "Visited page" audience > 200 users
   - LinkedIn matched audience > 300 (LinkedIn needs more)
   - If audiences are too small, retargeting will be expensive — note this and consider extending Week 1 cold by 2-3 days before launching retargeting
2. [ ] Build retargeting campaigns per brief Section 6:
   - Budget: $[from brief, total $100 minimum]
   - Audiences: [from brief Section 6]
   - Ads: use retargeting-specific assets from `assets/` (concepts tagged as retargeting in visual-concepts.md)
   - Destination URL: use retargeting UTMs from table above
3. [ ] Launch all retargeting campaigns
4. [ ] Verify they're spending within 4 hours of activation

---

## 📊 DAY 3, 7, 10, 14 — CHECK-IN POINTS

| Day | What to do |
|---|---|
| Day 3 | Type `/review-ads` in Claude — first signal check. If CTR is below brief target on any platform, type `/decide-action` for fix recommendation. |
| Day 7 | End of Week 1. Type `/review-ads` then `/decide-action`. This is the moment you decide whether Week 2 strategy needs adjustment based on what Week 1 taught us. |
| Day 10 | Mid-Week 2 check. `/review-ads` + `/decide-action`. Activate **Kill Switch** (brief Section 10) if trigger conditions are hit. |
| Day 14 | Campaign close. Final `/review-ads`. Decide: was this report's campaign a win, a wash, or a fail? Document lessons in `data/proposals/[slug]/lessons.md` so the next report's campaign learns from it. |

---

## 🛡 KILL SWITCH (full text from brief Section 10)

**Activate by Day 5 if ANY of these:**
- CTR below [from brief] on all platforms simultaneously
- Zero report page visits after $[from brief] spent
- CPC exceeding $[from brief] with no improvement

**Protocol:**
- Creative failing → swap to Hook [X] (from brief Section 0.3), relaunch in 24hr
- Landing page failing → switch to lead-gen form objective, capture email instead
- Platform CPC unworkable → cut that platform, reallocate to highest-ROI platform
- All platforms failing → stop paid, redirect remaining budget to organic amplification

**Don't burn $500 on zero signal.** Pulling spend early is not failure.

---

## ✅ POST-LAUNCH SANITY CHECK (Day 14+)

Once campaign is done:

- [ ] Pause all ad sets in every platform
- [ ] Export final performance from each platform's reports → save as CSV in `data/proposals/[slug]/analytics/final-day14.csv`
- [ ] Type `/review-ads` one last time for the final snapshot
- [ ] Type `/decide-action` for a post-mortem and lessons-learned note
- [ ] Keep retargeting audiences active in each platform — they're reusable for the next Ghost Research report campaign
- [ ] If any creative was a clear winner, note it in `data/memory/winning-patterns.md` so future campaigns reuse the approach
- [ ] If any creative clearly failed, note it in `data/memory/losing-patterns.md` so we don't repeat
```

## Step 4 — Update pipeline

Append: `[date] | [slug] | launch checklist ready | publishing window: [start]-[end]`

## Step 5 — Hand off

```
✅ Launch checklist: data/proposals/[slug]/launch-checklist.md

This is your operational playbook. Total time to launch is ~60-90 minutes if assets and pixels are ready. Critical pre-flight items at the top — especially OG meta tags.

When ads have been live 3-7 days, come back and type /review-ads.
```

## Rules

- **NEVER invent ad account IDs, pixel IDs, campaign IDs, or URLs.** Leave them as `[your account ID]` for the user.
- **The OG meta tag check is the MOST important pre-flight item** — Ghost Research's site is JS-rendered, and missing OG tags = blank link previews = wasted spend. Always surface this in red.
- **Pre-build UTM URLs** for the user. Non-technical users get UTMs wrong constantly; pre-built URLs save 30 minutes of confusion and prevent broken attribution.
- **Match the platform list in this checklist to the platforms ACTUALLY selected in the brief.** Do not include sections for excluded platforms.
- **Mention the Day 8 retargeting delay explicitly** — non-technical users often try to launch retargeting on Day 1 (it has no audience yet) and waste budget.
