---
slug: de-minimis-repeal-ecommerce-2026
created: 2026-05-23
publish_date: 2026-06-07
product: Off-the-shelf report ($500) + Ghost Elite cross-sell
platforms: [Meta (Instagram + Facebook), LinkedIn, X/Twitter]
total_budget: $500
status: ready-to-publish
---

# Launch Checklist — The End of De Minimis: The 2026 Landed-Cost Reset

> Follow this top to bottom. Don't skip pre-flight — Ghost Research's #1 launch failure is OG meta tags missing on a JS-rendered page, which makes every link preview render blank and wastes spend.
>
> **Calendar:** Week 1 hype **Mon 1 Jun → Sun 7 Jun** · Report publishes **end of Sun 7 Jun** · Week 2 conversion **Mon 8 Jun → Sun 14 Jun**.

---

## 🚨 PRE-FLIGHT — complete before any ad goes live

### Website / landing flow
- [ ] Product path confirmed: **off-the-shelf report** (with Ghost Elite cross-sell in Week 2)
- [ ] **Week 1 landing page ready** — waitlist / "get notified" page: `ghostresearch.com/reports/de-minimis-reset-2026/notify`
- [ ] **Week 2 landing page ready** — live report page: `ghostresearch.com/reports/de-minimis-reset-2026`
- [ ] Both pages load correctly **on mobile** (test on your phone, not just desktop)
- [ ] 🔴 **OG meta tags set on BOTH pages** (the report page AND the /notify page):
  - [ ] `og:title` = "The End of De Minimis: The 2026 Landed-Cost Reset"
  - [ ] `og:description` = "On 1 July the EU ends the €150 de-minimis exemption and adds €3 per parcel. We modeled the new landed cost — by SKU, by lane. 1M+ curated sources, expert-vetted."
  - [ ] `og:image` = a 1200×630 export (use `concept-08-lane-loss.png` cropped to 1.91:1, or `concept-04-150.png`)
  - [ ] `og:url` = the full live URL of each page
  - [ ] `twitter:card` = "summary_large_image"
  - **Verify:** paste each live URL into [opengraph.xyz](https://www.opengraph.xyz) — preview must show the image + title, not blank
- [ ] Publish timing confirmed: the report genuinely goes live **end of Day 7 (Sun 7 Jun)** — the entire Week 2 engine depends on it
- [ ] Conversion flow works end-to-end:
  - [ ] Week 1: waitlist signup captures email + fires `waitlist_signup`
  - [ ] Week 2: purchase flow completes and fires `purchase`
  - [ ] Ghost Elite enquiry form (`ghostresearch.com/ghost-elite`) submits and routes to a human
- [ ] A human is on standby to follow up Ghost Elite enquiries within 24 hours

### Tracking pixels
- [ ] **Meta Pixel** installed on both pages (test with Meta Pixel Helper → "active")
- [ ] **LinkedIn Insight Tag** installed (Campaign Manager → Account Assets → Insight Tag)
- [ ] **X / Twitter Pixel** installed (Ads Manager → Tools → Conversion Tracking)
- [ ] Conversion events defined on each pixel:
  - [ ] `page_view` · `waitlist_signup` (Wk1 primary) · `initiate_checkout` (Wk2) · `purchase` (Wk2 primary) · `lead_submission` (Elite)

### Audiences (create BEFORE Day 1 — retargeting needs them populated by Day 8)
- [ ] **Meta:** Custom audience "Visited de-minimis landing flow — last 30d"
- [ ] **Meta:** Custom audience "Waitlist signup — last 14d"
- [ ] **Meta:** Custom audience "Watched ≥50% of any campaign video — last 14d"
- [ ] **Meta:** Custom audience "Initiated checkout — no purchase — last 14d"
- [ ] **Meta:** Lookalike 1% off the waitlist audience (build once source ≥100)
- [ ] **LinkedIn:** Matched audience "Visited de-minimis landing flow — last 30d"
- [ ] **X:** Tailored audience "Engaged with the de-minimis campaign post"

### Budget caps (account-level safety net — protects the $500 hard cap)
- [ ] **Meta:** Account spending limit = **$230** (Billing settings)
- [ ] **LinkedIn:** Campaign group total budget = **$170**
- [ ] **X:** Daily account spend cap = **~$7/day** (≈ $100 ÷ 14)
- [ ] **All platforms:** each campaign end date = **Sun 14 Jun 2026** (nothing runs past the 14-day window)

### UTM scheme — keep this doc open while building ads

```
https://ghostresearch.com/[path]?utm_source=[platform]&utm_medium=paidsocial&utm_campaign=de-minimis-reset-2026&utm_content=[concept]&utm_term=[week1-hype|week2-launch|retargeting|elite-cross-sell]
```

**Pre-built URLs (copy directly when setting up ads):**

| Platform | Phase | URL |
|---|---|---|
| Meta IG | Wk1 Hype | `https://ghostresearch.com/reports/de-minimis-reset-2026/notify?utm_source=instagram&utm_medium=paidsocial&utm_campaign=de-minimis-reset-2026&utm_content=concept-01-parcel&utm_term=week1-hype` |
| Meta IG | Wk1 Hype (pull-quote) | `https://ghostresearch.com/reports/de-minimis-reset-2026/notify?utm_source=instagram&utm_medium=paidsocial&utm_campaign=de-minimis-reset-2026&utm_content=concept-02-3euro&utm_term=week1-hype` |
| Meta IG | Wk2 Launch | `https://ghostresearch.com/reports/de-minimis-reset-2026?utm_source=instagram&utm_medium=paidsocial&utm_campaign=de-minimis-reset-2026&utm_content=concept-08-lane-loss&utm_term=week2-launch` |
| Meta IG | Retargeting | `https://ghostresearch.com/reports/de-minimis-reset-2026?utm_source=instagram&utm_medium=paidsocial&utm_campaign=de-minimis-reset-2026&utm_content=concept-12-market-vs-catalogue&utm_term=retargeting` |
| Meta IG | Elite cross-sell | `https://ghostresearch.com/ghost-elite?utm_source=instagram&utm_medium=paidsocial&utm_campaign=de-minimis-reset-2026&utm_content=concept-12-market-vs-catalogue&utm_term=elite-cross-sell` |
| LinkedIn | Wk1 Hype | `https://ghostresearch.com/reports/de-minimis-reset-2026/notify?utm_source=linkedin&utm_medium=paidsocial&utm_campaign=de-minimis-reset-2026&utm_content=concept-03-lane-pnl&utm_term=week1-hype` |
| LinkedIn | Wk1 Document | `https://ghostresearch.com/reports/de-minimis-reset-2026/notify?utm_source=linkedin&utm_medium=paidsocial&utm_campaign=de-minimis-reset-2026&utm_content=concept-05-skus&utm_term=week1-hype` |
| LinkedIn | Wk2 Launch | `https://ghostresearch.com/reports/de-minimis-reset-2026?utm_source=linkedin&utm_medium=paidsocial&utm_campaign=de-minimis-reset-2026&utm_content=concept-10-three-lanes&utm_term=week2-launch` |
| LinkedIn | Elite cross-sell | `https://ghostresearch.com/ghost-elite?utm_source=linkedin&utm_medium=paidsocial&utm_campaign=de-minimis-reset-2026&utm_content=concept-12-market-vs-catalogue&utm_term=elite-cross-sell` |
| X | Wk1 Hype | `https://ghostresearch.com/reports/de-minimis-reset-2026/notify?utm_source=twitter&utm_medium=paidsocial&utm_campaign=de-minimis-reset-2026&utm_content=concept-04-150&utm_term=week1-hype` |
| X | Wk2 Launch | `https://ghostresearch.com/reports/de-minimis-reset-2026?utm_source=twitter&utm_medium=paidsocial&utm_campaign=de-minimis-reset-2026&utm_content=concept-10-three-lanes&utm_term=week2-launch` |

---

## 🚀 DAY 1 (Mon 1 Jun) — WEEK 1 HYPE LAUNCH

### Step 1 — Open the campaign brief alongside this checklist
Have `campaign-brief.md` open. You'll reference Section 3 (calendar), Section 4 (per-platform), Section 7 (copy vault) constantly. **Week 1 = hype only. No report findings in any ad.**

### Step 2 — Meta (Instagram + Facebook) — highest budget, the retargeting engine (~25 min)
1. [ ] Meta Ads Manager → Create campaign → name `2026-06 de-minimis-reset`
2. [ ] Campaign budget (CBO) Week 1 ≈ **$110** total; objective: **Traffic / Leads** (waitlist)
3. [ ] Ad set audience: paste the **primary audience** from brief Section 4 (Instagram block); geo US+EU+India+UAE/Saudi; add the **negative audiences**
4. [ ] Build the Week-1 ads (per Section 3 calendar):
   - [ ] Day 1 — upload `assets/concept-01-parcel.png` — Headline: brief §7 Wk1 #1 — CTA "Sign Up" — URL: Meta IG Wk1 Hype
   - [ ] Day 2 — upload `assets/concept-02-3euro.png` — Hook 2 (pull-quote) — URL: concept-02 Wk1
   - [ ] Day 4 — upload `assets/concept-04-150.png` — Hook 1 — URL: concept-04 Wk1
   - [ ] Day 6 — upload `assets/concept-06-routes.png` — Hook 2 — URL: Meta IG Wk1
   - [ ] Day 7 — upload `assets/concept-07-publish-eve.png` — publish-eve teaser
5. [ ] Use **Week 1 hype-safe** headlines + body from brief §7. CTA button = "Sign Up".
6. [ ] **Do NOT build retargeting yet** — calendar reminder for Day 8.

### Step 3 — LinkedIn — the senior buyer + Elite cross-sell (~20 min)
1. [ ] Campaign Manager → new campaign group `2026-06 de-minimis-reset` → group budget **$170**
2. [ ] Week 1 campaign ≈ **$85**; objective: **Website visits / Lead gen**
3. [ ] Audience: paste job-titles + seniority + industries from brief §4 (LinkedIn block); geo US+EU+India+GCC
4. [ ] Build Week-1 ads:
   - [ ] Day 3 — single image `assets/concept-03-lane-pnl.png` — Hook 1 — URL: LinkedIn Wk1 Hype
   - [ ] Day 5 — Document ad using `assets/concept-05-skus.png` as the title slide (build the other slides per visual-concepts.md C05) — URL: LinkedIn Wk1 Document
   - [ ] Thought-Leader Ad: Joy Sharma POV text from brief §4 (no report content) — boost as TL ad
5. [ ] CTA = "Sign up". Intro text = brief §7 Wk1 long copy.

### Step 4 — X / Twitter — cheap deadline amplifier (~12 min)
1. [ ] Ads Manager → new campaign `2026-06 de-minimis-reset` → daily cap ~$8 (Wk1 ≈ $60)
2. [ ] Audience: follower-lookalikes of supply-chain/retail/customs media + keyword targeting ("de minimis", "Section 321", "landed cost", "Shein Temu")
3. [ ] Build Week-1 ads:
   - [ ] Day 1 — `assets/concept-01-parcel.png` — Hook 1 — URL: X Wk1
   - [ ] Day 4 — `assets/concept-04-150.png` — Hook 1 — URL: X Wk1 (concept-04)
4. [ ] CTA = "Sign up" / link.

### Step 5 — Verify (2–4 hrs after submission)
- [ ] All ads submitted on all platforms?
- [ ] All ads APPROVED? (de-minimis/customs copy is clean; if any rejected, paste the reason into Claude for a revision)
- [ ] Spend ~$5/platform: click your own ad → land on `/notify` → confirm:
  - [ ] Correct URL + UTM params present after redirect
  - [ ] Pixel fires `page_view`; signup fires `waitlist_signup`
  - [ ] UTMs appear in your website analytics within 30 min

---

## 🔁 DAY 5 (Fri 5 Jun) — HYPE PIVOT CHECK
1. [ ] Check brief Week-1 checkpoint: **waitlist signups ≥120** and blended CTR ≥1.2%
2. [ ] **Swap Hook 1 → Hook 2** creative across all platforms (concept-02, concept-05, concept-06 lead)
3. [ ] Confirm the report still publishes **Sun 7 Jun**

---

## 📅 DAY 8 (Mon 8 Jun) — LAUNCH + RETARGETING ACTIVATION
(Calendar reminder set on Day 1.) Report is now live.

1. [ ] Verify retargeting audience sizes: Meta "Visited page" >200, LinkedIn matched >300. If too small, extend a Week-1 cold creative 2 days before scaling retargeting.
2. [ ] **Pause Week-1 hype ads** on all platforms.
3. [ ] **Activate Week-2 launch ads (Hook 3 — content live):**
   - [ ] Meta: `concept-08-lane-loss.png` + `concept-09-launch.png` — CTA "Download" — Wk2 Launch URL
   - [ ] LinkedIn: `concept-10-three-lanes.png` (+ Document variant) — CTA "Learn more" — Wk2 URL
   - [ ] X: `concept-10-three-lanes.png` — Wk2 URL
   - [ ] Day 13: `concept-11-which-skus.png` (light) on Meta + X
4. [ ] **Build retargeting** per brief §6 — total **$100** (Meta $60 + LinkedIn $40):
   - [ ] Audiences: page-visitors no-purchase, ≥50% video viewers, LinkedIn clickers
   - [ ] Ad: `concept-12-market-vs-catalogue.png` + Wk2 retargeting copy (brief §6)
   - [ ] **Day 11+: launch the Ghost Elite cross-sell layer** ($50 min) → `concept-12` with the Elite CTA → `ghost-elite` URL
5. [ ] Verify retargeting is spending within 4 hrs.

---

## 📊 DAY 3 / 7 / 10 / 14 — CHECK-IN POINTS

| Day | Action |
|---|---|
| Day 3 (Wed 3 Jun) | `/review-ads` — first signal. If CTR < brief target on any platform, `/decide-action`. |
| Day 7 (Sun 7 Jun) | End of Week 1. `/review-ads` then `/decide-action`. Decide if Week-2 strategy needs adjustment. Confirm publish went live. |
| Day 10 (Wed 10 Jun) | Mid-Week 2. `/review-ads` + `/decide-action`. Activate **Kill Switch** if any trigger hit. |
| Day 14 (Sun 14 Jun) | Close. Final `/review-ads` + `/decide-action`. Document `lessons.md`. |

---

## 🛡 KILL SWITCH (from brief Section 10)

**Activate by Day 5 if ANY:**
- Blended CTR < 0.8% on all platforms simultaneously
- Zero waitlist signups after **$120** spent in Week 1
- Blended CPC > **$4.50** with no improvement
- (Wk2 Elite layer) zero enquiries after $50 spent

**Protocol:**
- Hooks failing → pause, swap to Hook 2, tighten Meta interests, relaunch in 24hr
- Signups zero by Day 4 → audience misfit (are we hitting operators, not consumers?) before re-hooking
- Landing page failing (visits, no signups) → fix the `/notify` form first
- A platform's CPC unworkable → cut **X first**, reallocate to Meta; if LinkedIn CPC >$14 keep only Thought-Leader + Document ads
- Wk2 conversion failing despite good Wk1 → capture-first (email-gate a preview), activate Elite cross-sell early
- All platforms failing → stop paid, go organic (Joy Sharma LinkedIn post + email the waitlist)

**Don't burn $500 on zero signal. The hard 1-July deadline means a stalled campaign won't "warm up" in time — make the call by Day 5.**

---

## ✅ POST-LAUNCH SANITY CHECK (Day 14+)
- [ ] Pause all ad sets on every platform
- [ ] Export final performance from each platform → `data/proposals/de-minimis-repeal-ecommerce-2026/analytics/final-day14.csv`
- [ ] `/review-ads` for the final snapshot, then `/decide-action` for the post-mortem
- [ ] Keep retargeting audiences active (reusable for the next Ghost report)
- [ ] Log any clear winner in `data/memory/winning-patterns.md`; any clear failure in `data/memory/losing-patterns.md`
