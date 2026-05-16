# Launch checklist — The 2026 IPO Window

Click-by-click for **Monday 2026-06-09 08:00 UTC**.

## T-minus 7

- [ ] Open every asset in `data/proposals/ipo-window-2026/assets/`. Anything off → `/edit-ad <id> "fix"`.
- [ ] Confirm load-bearing audit numbers (73 / 22 / 12 / 4 / 32 / 30%) match the published report. Any change → regenerate every asset that uses them.

## T-minus 5

- [ ] LP live in staging — methodology TOC above the fold + SME count + email-capture form.
- [ ] OG meta tags per ad URL. Map each `/ipo-window-2026?ad=NN` to the matching concept PNG.
- [ ] Stripe checkout tested with US, UK, EUR cards.
- [ ] Email automation triggers Day 8 08:00 UTC → sends C08 launch email.

## T-minus 3

- [ ] Pixels firing: LinkedIn Insight, Meta Pixel, X Pixel, GA4 on LP + checkout success.
- [ ] UTM convention: `?utm_source={platform}&utm_medium=cpc&utm_campaign=ipo-window-2026&utm_content=C{NN}&utm_term={hook}`.
- [ ] Audiences built per platform-playbook.md.

## T-minus 1 (Sunday 2026-06-08)

- [ ] Upload all 16 deliverables to LI Campaign Manager, X Ads, Meta Ads.
- [ ] Build 16 campaigns with budget caps per timeline.
- [ ] Schedule each for its calendar day at 08:00 local geo.
- [ ] Frequency caps: LI 4/14d, X 3/14d, Meta 4/14d.
- [ ] Kill-switch Slack alerts:
  - CPS > $15 on LI after Day 5
  - CTR < 0.35% on LI after Day 4
  - ROAS < 1.0x after Day 12
- [ ] Joy posts C07 organic LinkedIn 20:00 UTC.

## T-0 (Monday)

- [ ] 08:00 UTC — all campaigns live.
- [ ] 08:30 — screenshot C08 ad live on LI for archive.
- [ ] First 6 hours — watch CTR. Pause any below 0.25% after $5 spend.
- [ ] Day 8 (LAUNCH) — $80 on C08 + email automation fires.

## Daily during flight

- [ ] 08:00 — check CTR + CPS + ROAS. Decide top-up / pause per kill-switch.
- [ ] 15:00 — check LP → checkout funnel. Bounce > 75% by Day 7 → fix page, not ad.
- [ ] 20:00 — engagement-bait reply on Joy's organic posts.

## Day 14 close

- [ ] 23:59 UTC — stop all paid spend.
- [ ] +1 day — `/review-ads` + `/decide-action`. Write `lessons.md`.
- [ ] +3 days — if ROAS > 3.0x, propose extended flight as a new campaign.

---

*Skip the OG meta tag step at your peril. LinkedIn share without OG image = 40% CTR collapse.*
