# Launch checklist — CFO Defense Pack, Q2 2026

Click-by-click setup for the 14-day flight launching **Monday 2026-06-09 at 08:00 UTC**.

---

## T-minus 7 days (today)

- [ ] Open every asset in `data/proposals/cfo-defense-pack-q2-2026/assets/` and eye-check it. Anything off-brand → `/edit-ad <id> "your fix"`.
- [ ] Confirm the audit's actual numbers will support the load-bearing claims: **1,047 deployments · 32 named SMEs · 8 survived diligence · $0.74 ROI · 6 unit-economics patterns · 4 categorical failure modes**. If any change at publication, regenerate every asset that uses them.

## T-minus 5 days

- [ ] Landing page live in staging — methodology TOC + reviewer count above the fold + email-capture form wired.
- [ ] OG meta tags per ad URL. Set `og:image` to the matching concept PNG (`/cfo-defense-pack?ad=01` → `C01-w1d1-linkedin.png`, etc.).
- [ ] Stripe checkout — test US, UK, EUR cards. Verify $500 reads correctly per locale.
- [ ] Email automation — Mailchimp/Klaviyo triggers on Day 8 08:00 UTC → sends C08 launch email + brief link.

## T-minus 3 days

- [ ] Pixels firing: LinkedIn Insight, Meta Pixel, X Pixel, GA4 — all on LP + checkout success.
- [ ] UTM convention applied: `?utm_source={platform}&utm_medium=cpc&utm_campaign=cfo-defense-q2&utm_content=C{NN}&utm_term={hook-slug}`.
- [ ] Audiences built per platform-playbook.md.

## T-minus 1 day (Sunday 2026-06-08)

- [ ] Upload all 14 assets to LinkedIn Campaign Manager, X Ads, Meta Ads Manager.
- [ ] Build 14 campaigns (one per concept) with budget caps per timeline table.
- [ ] Schedule each campaign for its calendar day at 08:00 local geography.
- [ ] Frequency caps: LinkedIn 4/14d, X 3/14d, Meta 4/14d.
- [ ] Kill-switch Slack alerts:
  - CPS > $15 on any LinkedIn ad after Day 5
  - CTR < 0.35% on any LinkedIn ad after Day 4
  - ROAS < 1.0x after Day 12
- [ ] Joy posts C07 organically to her LinkedIn at 20:00 UTC.

## T-0 (Monday 2026-06-09)

- [ ] 08:00 UTC — all 14-day campaigns go-live.
- [ ] 08:30 UTC — screenshot C08 launch ad live on LinkedIn (archive proof).
- [ ] First 6 hours — watch CTR per ad. Pause any below 0.25% after $5 spend.
- [ ] Day 8 — peak spend day. $80 on C08 + the email automation fires simultaneously.

## Daily during flight

- [ ] 08:00 — check yesterday's CTR + CPS + ROAS. Decide top-up / pause per kill-switch rules.
- [ ] 15:00 — check LP → checkout funnel. If bounce > 75% by Day 7 → fix the page, not the ad.
- [ ] 20:00 — engagement-bait reply to any organic post from Joy ("if you're a CFO prepping the Q2 board, this is the receipts").

## Day 14 close

- [ ] 23:59 UTC — stop all paid spend.
- [ ] +1 day — run `/review-ads` + `/decide-action`. Write `lessons.md`.
- [ ] +3 days — if ROAS > 3.0x → propose extended flight as a new campaign. Don't quietly raise budgets in Ads Manager.

---

*If you skip exactly one step in this checklist, do not let it be the OG meta tags. A LinkedIn share without an OG image collapses CTR by ~40%.*
