# Launch checklist — Enterprise AI ROI 2026

Click-by-click setup for the 14-day flight launching **Monday 2026-06-09 at 08:00 UTC**.

---

## T-minus 7 days (today)

- [ ] Open every asset in `data/proposals/enterprise-ai-roi-2026/assets/` and eye-check it. Anything off → `/edit-ad <id> "your fix"`.
- [ ] Confirm the audit's actual numbers will support the load-bearing claims used in the creative: **1,047 deployments · 32 named SMEs · 4 survived diligence · 0.93 ROI · $300B spend reference · 22% claimed vs 6% verified headcount displacement.** If any of these change at publication, every asset using them must be regenerated.

## T-minus 5 days

- [ ] **Landing page live in staging:** methodology TOC above the fold + named SME count visible + email-capture form wired.
- [ ] **OG meta tags per ad URL.** Set `og:image` to the matching concept PNG:
  - `/ai-roi-2026?ad=01` → `concept-01-w1d1-hero-linkedin.png`
  - `/ai-roi-2026?ad=02` → `concept-02-w1d2-x-methodology.png`
  - … (repeat for all 14)
- [ ] **Stripe checkout:** test with US, UK, EUR cards. Verify $500 reads as `USD $500.00` in receipt.
- [ ] **Email automation:** Mailchimp / Klaviyo automation triggers on Day 8 at 08:00 UTC → sends `concept-08-w2d8-now-live.png` + brief link.

## T-minus 3 days

- [ ] **Pixels:** LinkedIn Insight Tag, Meta Pixel, X Pixel, GA4 — all firing on landing page + checkout success.
- [ ] **UTM convention live:** every ad URL uses `?utm_source={platform}&utm_medium=cpc&utm_campaign=ai-roi-2026&utm_content=concept-{NN}&utm_term={hook-slug}`.
- [ ] **Audiences built:**
  - LinkedIn: Sales-Nav-style {CFO/VPFin/HoStrategy/PEAssoc/StratConsultant/HoAI/CIO} × ${1B+ companies} × US/UK/EU.
  - X: keyword + follower-of {a16z, Stratechery, Matt Levine}, geo US/UK/EU.
  - Meta: Custom Audience uploaded from LinkedIn page visitors + lookalike.

## T-minus 1 day (Sunday 2026-06-08)

- [ ] **Upload all 14 assets** to LinkedIn Campaign Manager, X Ads, Meta Ads Manager.
- [ ] **Build the 14 campaigns** (one per concept) with budget caps per the playbook.
- [ ] **Schedule each campaign** for its calendar day at 08:00 local in the target geo.
- [ ] **Frequency caps:** LinkedIn 4/14d, X 3/14d, Meta 4/14d.
- [ ] **Kill-switch alerts:**
  - Slack alert if CPS > $18 on any LinkedIn ad after Day 5.
  - Slack alert if CTR < 0.30% on any LinkedIn ad after Day 4.
  - Slack alert if ROAS < 1.0x after Day 12.
- [ ] **Joy posts** Concept 07 organically to her LinkedIn at 20:00 UTC. **Tag a peer** to surface in connections' feeds.

## T-minus 0 (Monday 2026-06-09)

- [ ] **08:00 UTC:** all 14-day campaign go-live.
- [ ] **08:30 UTC:** screenshot of Concept 01 ad live on LinkedIn (proof for archive).
- [ ] **First 6 hours:** watch CTR per ad. Pause any below 0.20% CTR after $5 of spend.
- [ ] **Day 8 (launch day):** Concept 08 launch sponsored slot, $80 budget. Send the launch email at 08:00 UTC simultaneous with the ad.

## Daily during flight

- [ ] **08:00:** check yesterday's CTR + CPS + ROAS. Decide top-up / pause per kill-switch rules.
- [ ] **15:00:** check landing-page → checkout funnel. If bounce > 75% by Day 7 → fix the page, not the ad.
- [ ] **20:00:** any organic post by Joy gets the engagement-bait reply ("if you're an AI buyer / a board member preparing for Q2, this is the receipts").

## Day 14 close

- [ ] **23:59 UTC:** stop all paid spend.
- [ ] **+1 day:** run `/review-ads` and `/decide-action`. Write `lessons.md`.
- [ ] **+3 days:** if ROAS > 2.5x → propose extended flight as a new campaign. Don't quietly raise budgets in Ads Manager.

---

*If you skip exactly one step in this checklist, do not let it be the OG meta tags. A LinkedIn share without an OG image collapses CTR by ~40%.*
