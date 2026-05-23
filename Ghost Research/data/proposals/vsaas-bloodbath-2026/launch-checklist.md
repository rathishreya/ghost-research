# Launch checklist — The vSaaS Bloodbath Audit 2026

For **Monday 2026-06-15 08:00 UTC**.

## T-7 days

- [ ] Open every asset in `data/proposals/vsaas-bloodbath-2026/assets/`. Anything off → `/edit-ad <id> "fix"`.
- [ ] Confirm load-bearing numbers (80 / 20 / 12 / 4 / 32 / 25%) match the published audit. Any change → regenerate every asset that uses them.

## T-5 days

- [ ] LP live in staging — methodology TOC + SME count + email capture form.
- [ ] OG meta tags per ad URL.
- [ ] Stripe tested with US, UK, EUR cards.
- [ ] Mailchimp/Klaviyo automation: Day 8 08:00 UTC → C08 launch email.

## T-3 days

- [ ] Pixels firing: LinkedIn Insight, Meta Pixel, X Pixel, GA4.
- [ ] UTM: `?utm_source={platform}&utm_medium=cpc&utm_campaign=vsaas-bloodbath-2026&utm_content=C{NN}&utm_term={hook}`.
- [ ] Audiences built per platform-playbook.md.

## T-1 day (Sunday)

- [ ] Upload all 16 deliverables to LI Campaign Manager, X Ads, Meta Ads.
- [ ] Build 16 campaigns with budget caps per timeline.
- [ ] Schedule each at 08:00 local geo.
- [ ] Frequency caps: LI 4/14d, X 3/14d, Meta 4/14d.
- [ ] Kill-switch Slack alerts:
  - CPS > $15 on LI after Day 5
  - CTR < 0.35% on LI after Day 4
  - ROAS < 1.0x after Day 12
- [ ] Joy posts C07 organic LI 20:00 UTC.

## T-0 (Monday)

- [ ] 08:00 UTC — all campaigns live.
- [ ] 08:30 — screenshot C08 live on LI.
- [ ] First 6 hours — watch CTR. Pause below 0.25% after $5 spend.
- [ ] Day 8 (LAUNCH) — $80 on C08 + email fires.

## Daily

- [ ] 08:00 — check CTR + CPS + ROAS.
- [ ] 15:00 — LP → checkout funnel. Bounce > 75% by Day 7 → fix page.
- [ ] 20:00 — reply on Joy's organic posts.

## Day 14 close

- [ ] 23:59 UTC — stop all paid spend.
- [ ] +1 day — `/review-ads` + `/decide-action`. Write `lessons.md`.
- [ ] +3 days — if ROAS > 3.0x, propose extended flight.

---

*Skip the OG meta tag step at your peril. LinkedIn share without OG image = 40% CTR collapse.*
