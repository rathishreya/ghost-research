---
slug: ai-energy-demand-2026
created: 2026-05-18
brief: campaign-brief.md
publish_date: 2026-06-01
launch_date: 2026-05-25
status: pre-flight
---

# Launch Checklist — The AI Energy Demand Atlas 2026

**T-7 days from launch (2026-05-25).** Work through this checklist sequentially. The OG meta tag check at the top is the most common single failure point — do not skip.

---

## 🔴 Phase 1 — Landing page + tracking (TODAY, T-7)

### 1.1 Landing page sanity (CRITICAL — do not skip)

The AI Energy Demand Atlas landing page must exist at `ghostresearch.com/atlas/ai-energy-demand-2026` (or your platform's equivalent route) BEFORE Day 1.

- [ ] Page is live and loading in <2 seconds on 4G mobile
- [ ] Page has both a Week-1 mode (drop-list signup) and a Week-2 mode (direct purchase) — OR a single mode that switches based on date
- [ ] `<title>` reads exactly: **"The AI Energy Demand Atlas 2026 — 9 utilities, 31 GW, the trades that priced — Ghost Research"**
- [ ] Meta description (≤155 chars): "$147B in announced hyperscaler capex mapped to 9 utility balance sheets. 3 already repriced 18-22%. Caspr-powered. Expert-vetted. $500."
- [ ] **OG meta tags present and correct** (this is the single most-common LinkedIn-ad rejection cause):
  - `og:title` = same as `<title>` above
  - `og:description` = same as meta description above
  - `og:image` = **`C08-w2d8-its-live.png` uploaded to your CDN** (1080×1080, <1MB, public URL)
  - `og:image:width` = 1080, `og:image:height` = 1080
  - `og:type` = "article"
  - `og:url` = canonical URL of the page
- [ ] Twitter card tags: `twitter:card = "summary_large_image"`, `twitter:image` = same as og:image
- [ ] **Verify with both:**
  - [ ] LinkedIn Post Inspector: https://www.linkedin.com/post-inspector/ — paste the URL, confirm the preview shows your title + description + image
  - [ ] X Cards Validator (or just pasting the URL into a DM to yourself) — confirm same
- [ ] Pricing displays exactly as: **"$500 USD"** — not "$499" or "USD 500" (the cold ad copy anchors against the literal "$500")

### 1.2 Drop-list form (Week 1 capture)

- [ ] Email signup form active on the page during Week 1 mode
- [ ] Form integrates with Mailchimp / HubSpot / your tool of choice
- [ ] **Auto-reply email goes out within 5 minutes** of signup with one-liner: "You're on the list. Atlas drops Monday June 1. Expect one email then."
- [ ] Form fires a tracked event (`atlas_drop_list_signup`) into both platform pixels (see 1.4)
- [ ] Form does NOT require company / role / phone — email-only, friction-minimal

### 1.3 Ghost Elite enquiry form (Week 2 retargeting destination)

- [ ] Form at `ghostresearch.com/elite` is live
- [ ] Required fields: name, work email, company, role/title, one-line "what we're looking at"
- [ ] Form auto-routes to the Elite team alias (Joy + 1 SME on-call)
- [ ] **Slack notification + CRM ticket created on submission** — Elite enquiries are time-sensitive (24-hr delivery promise)
- [ ] Form fires `elite_enquiry_submitted` event into both pixels

### 1.4 Platform pixels — install + fire test

- [ ] **LinkedIn Insight Tag** installed on every page of ghostresearch.com (one-line JS in `<head>`)
- [ ] **X / Twitter Pixel** installed sitewide
- [ ] **Meta Pixel** installed (for IG retargeting fallback)
- [ ] Test fires in each platform's events manager — see "Test events" with your IP

### 1.5 UTM tracking conventions (LOCK THIS NOW — don't change mid-campaign)

Every ad URL must carry these UTMs:
```
utm_source = linkedin | x | meta
utm_medium = paid
utm_campaign = ai-energy-demand-2026
utm_content = [concept ID, e.g. C01, C04, C12]
utm_term = [week1 | week2 | retarget | elite-crosssell]
```

Example URL for Concept C01 (Day 1 LinkedIn):
```
https://ghostresearch.com/atlas/ai-energy-demand-2026?utm_source=linkedin&utm_medium=paid&utm_campaign=ai-energy-demand-2026&utm_content=C01&utm_term=week1
```

- [ ] Build all 12 concept URLs in a spreadsheet now — paste-ready when you load Ads Manager

---

## 🟡 Phase 2 — Audience prep (T-5)

### 2.1 LinkedIn audience build

In Campaign Manager, build these saved audiences before launch:

- [ ] **Audience: Energy/Utility Tier-1 (Cold)**
  - Job titles: Portfolio Manager (Energy), Energy Analyst, Utility Analyst, Utilities Equity Analyst, Head of Infrastructure (Hyperscale), Data Center Site Selection, Energy Trader, Macro Strategist, Director Energy Markets, VP Investments (Infra/Energy)
  - Seniority: Director+ AND Manager+ (use OR)
  - Industries: Investment Management, Capital Markets, Utilities, Renewable Energy, Computer Hardware
  - Geography: US (state-level: NY, CA, TX, IL, MA, DC, CT), UK, DE, NL, FR, IE
  - Estimated size: 80K-140K — confirm in LI estimator
  - Exclusions: Job seekers; consumer-marketing roles; recent grads
  - **Save as:** `Atlas-2026-Cold-Tier1`

- [ ] **Audience: Energy/Utility Tier-2 (Cold, broader)** — same titles but Manager+ only, broader industries (Banking, Financial Services). Save as: `Atlas-2026-Cold-Tier2`

- [ ] **Matched company list** (manual upload)
  - Build a CSV of ~250 target companies: top-50 US energy/utility funds + top-15 US/UK/EU utilities + AWS/MSFT/GOOG/META infra teams + top-10 infra-credit shops + top-20 macro hedge funds
  - Upload to Campaign Manager → Matched Audiences → Companies → CSV upload
  - Save as: `Atlas-2026-Target-Companies`

- [ ] **Retargeting audiences** (will populate from Day 1 onward; create the rules now)
  - All site visitors: 14-day window
  - Atlas page visitors (URL contains `/atlas/ai-energy-demand-2026`): 14-day window — `Atlas-2026-Page-Visitors`
  - Engaged with any campaign ad (15s+ video or click): 30-day window — `Atlas-2026-Engaged`
  - **CRITICAL:** `Atlas-2026-Page-Visitors` EXCLUDE list = anyone who fired `purchase_completed` event (avoid burning retargeting dollars on people who already bought)

### 2.2 X / Twitter audience build

- [ ] **Follower lookalikes** — in X Ads, add custom audiences with these target handles' followers:
  - `@doomberg` · `@DataCentreDynamics` · `@nephronresearch` · `@JZ_NYC` · `@AnasAlhajji` · `@energybellwx` · `@PJMInterconnect` · `@AdamRozencwajg`
- [ ] **Keyword targeting:** "energy macro", "utility analyst", "PJM", "ERCOT", "hyperscaler power", "data center capacity"
- [ ] **Engagement remarketing audience:** users who engaged with our cold ads in last 30 days — name `Atlas-2026-X-Engaged`
- [ ] Geo lock: US + UK + DE/NL/FR/IE

---

## 🟢 Phase 3 — Asset upload + ad creation (T-3 to T-1)

### 3.1 Assets confirmation

Open `data/proposals/ai-energy-demand-2026/assets/` and confirm every file is rendered:

- [ ] `P01-utility-cfo-capex.jpg` (base photo for C01)
- [ ] `P02-energy-analyst-monitors.jpg` (base for C02)
- [ ] `P03-grid-campus-dusk.jpg` (base for C04 video)
- [ ] `P04-trader-pjm-heatmap.jpg` (base for C05)
- [ ] `P05-atlas-closed-light.jpg` (base for C06 LIGHT)
- [ ] `P06-atlas-open-hand-pen.jpg` (base for C08 and C10 video)
- [ ] `P07-boardroom-occupied-atlas.jpg` (base for C11)
- [ ] `P08-analyst-two-documents.jpg` (base for C12 Elite cross-sell)
- [ ] `C01-w1d1-balance-sheet.png` (Day 1 LI)
- [ ] `C02-w1d2-x-9-names.png` (Day 2 X)
- [ ] `C03a-w1d3-method-slide1.png` · `C03b-w1d3-method-slide2.png` · `C03c-w1d3-method-slide3.png` (Day 3 LI doc — bundle as 3-slide PDF on upload)
- [ ] `C04-w1d4-slow-pan-reels.mp4` (Day 4 LI Reels, 16s) — **verify wordmark visible from frame 1 to last**
- [ ] `C05-w1d5-pjm-nodes.png` (Day 5 X)
- [ ] `C06-w1d6-atlas-closed-light.png` (Day 6 LI 4:5 LIGHT) — **verify this is cream/paper not indigo**
- [ ] `C07-w1d7-tomorrow.png` (Day 7 LI+X)
- [ ] `C08-w2d8-its-live.png` (Day 8 LI+X launch)
- [ ] `C09-w2d9-31gw-light.png` (Day 9 LI LIGHT stat-reveal) — **verify cream + huge red 31 GW**
- [ ] `C10-w2d10-page47-reels.mp4` (Day 10 LI Reels, 18s)
- [ ] `C11-w2d11-you-looked.png` (Day 11 retargeting)
- [ ] `C12-w2d12-elite-cross-sell.png` (Day 12 LI Elite cross-sell)

**Spot-check each asset for the four hard rules:**
- [ ] Ghost Research wordmark visible top-left on every still + every video frame
- [ ] No platform-UI-overlap (top 14% safe + bottom 35% safe on 9:16)
- [ ] Headline + sub readable at thumbnail size (load each asset at 480px wide preview and confirm)
- [ ] 6.5% padding uniform, no nested offset panels

### 3.2 LinkedIn Campaign Manager setup

Create ONE campaign group: **"AI Energy Demand Atlas 2026 — Cold + Retarget + Elite Cross-sell"**

Inside it, three campaigns:

**Campaign A — Week 1 Hype (LinkedIn)**
- [ ] Objective: Website Visits (NOT Lead-gen Forms — we want them on our owned drop-list form)
- [ ] Schedule: Mon 2026-05-25 00:01 UTC → Sun 2026-05-31 23:59 UTC
- [ ] Total budget: **$192** (daily cap ~$32; pacing: standard)
- [ ] Audience: `Atlas-2026-Target-Companies` AND (`Atlas-2026-Cold-Tier1` OR `Atlas-2026-Cold-Tier2`)
- [ ] Ad creatives:
  - C01 (Day 1, 24-hr run)
  - C03 doc ad (Day 3, 24-hr run) — upload 3 PNG slides as PDF using e.g. Smallpdf
  - C04 Reels video (Day 4, 24-hr run)
  - C06 LIGHT theme (Day 6, 24-hr run)
  - C07 "Tomorrow." (Day 7, 24-hr run)
- [ ] Bidding: Manual CPC, **max bid $13** (kill-switch threshold)
- [ ] All ads point to the Atlas landing page URL with proper UTMs (see 1.5)

**Campaign B — Week 2 Conversion (LinkedIn)**
- [ ] Objective: Website Conversions (fire on `purchase_completed`)
- [ ] Schedule: Mon 2026-06-01 00:01 UTC → Sun 2026-06-07 23:59 UTC
- [ ] Total budget: **$174** (daily cap ~$32-42 with frontload Days 8-9)
- [ ] Audience: same Cold audiences PLUS `Atlas-2026-Engaged` (Week-1 engaged users seeing the launch)
- [ ] Ad creatives: C08, C09 (LIGHT), C10 video
- [ ] Bidding: Manual CPC, max bid $12

**Campaign C — Week 2 Retargeting + Elite Cross-sell (LinkedIn)**
- [ ] Objective: Website Conversions
- [ ] Schedule: Mon 2026-06-01 00:01 UTC → Sun 2026-06-07 23:59 UTC
- [ ] Total budget: **$50** (retarget) + **$60** (Elite cross-sell) = $110
- [ ] Retarget audience: `Atlas-2026-Page-Visitors` EXCLUDING `purchase_completed` (C11 ad)
- [ ] Elite cross-sell audience: same retarget pool + 72-hr delay rule (C12 ad)
- [ ] Bidding: Manual CPC, max bid $14 (retargeting CPC tolerance is higher)

### 3.3 X / Twitter Ads setup

Single campaign: **"Atlas 2026 — X"**

- [ ] Objective: Website clicks
- [ ] Total budget: **$134** ($84 Week-1, $50 Week-2)
- [ ] Audience: follower lookalikes + keyword targeting (see 2.2)
- [ ] Ad creatives:
  - C02 (Day 2, $14 daily)
  - C05 (Day 5, $14 daily) — also promote a 3-tweet thread with C05 as the lead image
  - C07 (Day 7, $14 daily, paired with LinkedIn)
  - C08 (Day 8, $18 daily, launch)
  - C11 retargeting (Day 11, $10 daily)
  - C13 — pure-X variant only (Day 13, $14 daily)
- [ ] Bidding: Auto-CPC, max **$5** (kill-switch threshold)

---

## 🔵 Phase 4 — Final pre-flight (T-1, Sun 2026-05-24 evening)

- [ ] Run each ad through LinkedIn Post Inspector ONE more time — confirm the OG image is the right one
- [ ] Send a test ad to yourself (LinkedIn lets you preview without publishing) — open it on mobile, click through, complete a drop-list signup, verify the auto-reply lands
- [ ] Same on X — promote one ad to a $1 test audience, confirm tracking fires
- [ ] Set calendar reminders for the four checkpoints:
  - Day 3 (Wed 2026-05-27 evening) — first KPI snapshot
  - Day 7 (Sun 2026-05-31 evening) — Week 1 close, GO/NO-GO for Week 2 launch
  - Day 10 (Wed 2026-06-03 evening) — mid Week 2 KPI snapshot, decide on Elite cross-sell amplification
  - Day 14 (Sun 2026-06-07 evening) — final review, run `/review-ads` + `/decide-action`
- [ ] **Joy Sharma Thought Leader Ad (optional, T-1):** if running her POV ad on Day 2-3, post the organic version to her LinkedIn FIRST, then sponsor it via Campaign Manager. (Thought Leader Ads require an existing organic post as the source.)

---

## 🟣 Phase 5 — Launch day (Mon 2026-05-25)

- [ ] 09:00 local — flip Campaign A live in LinkedIn
- [ ] 10:00 local — flip the X campaign live
- [ ] 11:00 — confirm both showing impressions in their respective managers (within 1-2 hours)
- [ ] 16:00 — first impression-rate check; CPC sanity (< $13 on LI, < $5 on X)
- [ ] EOD — verify drop-list captured at least 5 signups (proof-of-life)

---

## ⚠️ Kill-switch reminders (from brief Section 10)

These conditions trigger immediate action — do not deliberate:

| Condition | Action |
|---|---|
| Week-1 waitlist signups = 0 by EOD Day 3 | Pause LinkedIn. Audit company-list targeting. |
| LinkedIn CTR < 0.5% by Day 4 | Swap Hook 1 → Hook 2 across all LinkedIn ads within 24 hrs. |
| LinkedIn CPC > $18 by Day 3 | Narrow company-list; if still > $18 by Day 5, shift $50 to X. |
| Week-2 purchases = 0 by EOD Day 10 | Pause launch ads. Audit landing page. Amplify Bloomberg-$30K vs Atlas-$500 headline. |
| Week-2 cost per purchase > $500 by Day 12 | Pause underperforming platform. Concentrate budget on the lower-CPC channel. |
| Ghost Elite enquiries = 0 by EOD Day 13 | Rewrite Day-12 cross-sell with sharper insider POV. |
| **Hard kill** — Day 7 close: signups < 20 AND CPC > $20 | Kill campaign. Write lessons.md. Topic+hook combination is wrong. |

---

## 📊 Post-Day 3 — first /review-ads call

Run `/review-ads` for slug `ai-energy-demand-2026` on the evening of Wed 2026-05-27. The skill will pull live Supermetrics data, compare against the KPI targets in brief Section 8, and surface action items. Don't skip this — the Day-3 read is the earliest signal whether hook + audience are landing.

---

**Atlas drops:** Mon 2026-06-01 at 09:00 ET.
**First Elite cross-sell goes live:** Fri 2026-06-05.
**Campaign closes:** Sun 2026-06-07 at 23:59 ET.
**Final `/decide-action` review:** Mon 2026-06-08 morning.
