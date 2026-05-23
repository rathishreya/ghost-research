---
slug: de-minimis-repeal-ecommerce-2026
created: 2026-05-23
brief: campaign-brief.md
concepts: visual-concepts.md
status: ready-to-generate
total_prompts: 15
template_library: ".claude/skills/_shared/template-library.md"
note: "v2 rebuild — every card on an approved template (A/B/C/D). Image-only (videos paused 2026-05-23). Thin red frame, blobs, bottom-anchored column, corrected footer sizes, CTA on every card."
---

# Generation Prompts — The End of De Minimis (v2, template-library rebuild)

## How to use this file
1. `/generate-assets` or `PYTHONUTF8=1 python scripts/run_full_delivery.py --slug de-minimis-repeal-ecommerce-2026 --overwrite`
2. Image-only — no video this run.
3. `/edit-ad <id> "instruction"` to iterate. `/prep-campaign` when right.

## Brand reminder (this rebuild)
- Every card uses a **named template** from `_shared/template-library.md` (A Dark Photo Hero · B Journal Cover · C Pull-Quote · D Light Stat Card).
- Shared chassis: thin red rounded frame · standalone icon mark · top eyebrow + drop date · **headline/stat/sub in ONE bottom-anchored column** · blob structures behind (consistent) · `Ghostresearch.com` ≤23px + credibility line ≥19px · red CTA on every card.
- 🚫 No icon-as-O wordmark, no orange banner strip, no AI faces, no 50/50 split, no busy dashboard, no videos.
- 🔒 Week 1 (C01–C07) hype, no findings. Week 2 (C08–C12) findings allowed.

---

## Concept 01 — Parcel at the Border (base still)

**Tool:** pollinations
**Aspect:** 1:1
**Suggested filename:** `concept-01-parcel-base.jpg`
**Maps to:** Visual C01 · Day 1

### Generation prompt
```
A single brown corrugated cardboard shipping parcel, sealed with a paper international
customs declaration form and a strip of red-and-white customs tape, resting alone on a dark
matte sorting-table surface. A small embossed date stamp catches a sliver of light on the
box side. The parcel sits in the lower-right third of the frame, emerging from deep shadow,
upper-left two-thirds an empty pool of deep indigo for headline overlay. Single soft cool
key light from upper-left casting a long shadow to the right; the red customs tape the only
saturated colour. Editorial product photography, color-graded to deep indigo (#181650) and
cool navy (#06062D), high detail, sharp focus on the box, background falling to near-black,
premium B2B aesthetic like the Financial Times. Photoreal, shot on Arri Alexa Mini with 50mm
prime, shallow depth of field. No text, no logos, no watermarks.

NEGATIVE: no robots, no AI-themed imagery, no brain circuits, no glowing nodes, no holograms,
no neon, no cyberpunk, no sci-fi UI, no high-fiving, no hands on keyboards, no fist bumps,
no smiling-at-camera lifestyle, no AI-generated faces, no uncanny features, no people,
no text in image, no logos, no watermarks.
```

---

## Concept 01 — Parcel at the Border (composite · Template A)

**Tool:** editorial
**Style preset:** Template A — Dark Photo Hero (Suspense + Instagram)
**Aspect:** 1:1
**Suggested filename:** `concept-01-parcel.png`
**Maps to:** Visual C01 · Day 1 (Week 1 hype)

### Generation prompt
```html
<!doctype html><html><head><meta charset="utf-8"/>
<link href="https://fonts.googleapis.com/css2?family=Oranienbaum&family=Manrope:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<style>
*{box-sizing:border-box;margin:0;padding:0}
:root{--ink:#F8F8FF;--red:#EF4444;--blob-stroke:rgba(248,248,255,.14)}
body{width:100%;height:100vh;font-family:'Manrope',sans-serif;color:var(--ink);position:relative;overflow:hidden;
  background:linear-gradient(0deg,rgba(6,6,45,.96) 8%,rgba(6,6,45,.5) 48%,rgba(6,6,45,.12) 100%),
  url("GHOST_ASSET:concept-01-parcel-base.jpg");background-size:cover;background-position:center}
.frame{position:absolute;inset:18px;border:2px solid var(--red);border-radius:28px;z-index:3;pointer-events:none}
.blob-ring{position:absolute;z-index:0;top:-12%;right:-8%;width:46%;aspect-ratio:1;border-radius:50%;border:1.5px solid var(--blob-stroke)}
.wrap{position:relative;z-index:1;height:100%;padding:8.5%;display:flex;flex-direction:column;justify-content:space-between}
.top{display:flex;justify-content:space-between;align-items:flex-start}
.gh-logo{width:clamp(72px,8.5vh,100px);height:clamp(72px,8.5vh,100px)}.gh-logo svg{width:100%;height:100%;display:block}
.eyebrow{font-size:clamp(18px,2.1vh,21px);font-weight:700;letter-spacing:.15em;text-transform:uppercase;text-align:right;line-height:1.5}
.eyebrow .red{color:var(--red)}
.btm{display:flex;flex-direction:column;gap:3vh}
.col{display:flex;flex-direction:column;align-items:flex-start;gap:2.2vh;max-width:24ch}
.lead{font-size:clamp(22px,2.6vh,30px);color:rgba(248,248,255,.85)}
.h1{font-family:'Oranienbaum',serif;font-size:clamp(64px,11vh,140px);line-height:.98}
.h1 em{font-style:italic;color:var(--red)}
.sub{font-size:clamp(22px,2.6vh,29px);color:rgba(248,248,255,.82);line-height:1.45;max-width:26ch}
.sub .red{color:var(--red);font-weight:600}
.cta{display:inline-flex;align-items:center;gap:10px;background:var(--red);color:#fff;padding:16px 28px;border-radius:8px;font-weight:700;font-size:clamp(22px,2.4vh,26px)}
.foot{display:flex;justify-content:space-between;align-items:flex-end;gap:18px}
.url{font-size:clamp(19px,2.1vh,23px);font-weight:600}
.cred{font-size:clamp(19px,2vh,21px);color:rgba(248,248,255,.62);text-align:right;max-width:26ch;line-height:1.4}
</style></head>
<body>
<div class="frame"></div><div class="blob-ring"></div>
<div class="wrap">
  <div class="top">
    <div class="gh-logo" aria-label="Ghost Research"><svg viewBox="0 0 100 100"><rect width="100" height="100" rx="22" fill="#EF4444"/><circle cx="50" cy="50" r="19" fill="#fff"/></svg></div>
    <div class="eyebrow">The De-Minimis Reset<br><span class="red">Drops 7 June 2026</span></div>
  </div>
  <div class="btm">
    <div class="col">
      <div class="lead">On 1 July, your landed-cost model</div>
      <h1 class="h1"><em>expires.</em></h1>
      <div class="sub">The €150 free-clearance window every cross-border <span class="red">SKU</span> relied on closes.</div>
      <span class="cta">Notify me on launch →</span>
    </div>
    <div class="foot"><span class="url">Ghostresearch.com</span><span class="cred">1M+ curated sources · transparent citation · expert-vetted</span></div>
  </div>
</div>
</body></html>
```

---

## Concept 02 — The €3 Reframe (Template C — Pull-Quote, dark)

**Tool:** editorial
**Style preset:** Template C — Pull-Quote
**Aspect:** 1:1
**Suggested filename:** `concept-02-3euro.png`
**Maps to:** Visual C02 · Day 2 (Week 1 hype)

### Generation prompt
```html
<!doctype html><html><head><meta charset="utf-8"/>
<link href="https://fonts.googleapis.com/css2?family=Oranienbaum&family=Manrope:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<style>
*{box-sizing:border-box;margin:0;padding:0}
:root{--ink:#F8F8FF;--red:#EF4444;--blob-stroke:rgba(248,248,255,.14);--blob-fill:rgba(239,68,68,.12)}
body{width:100%;height:100vh;font-family:'Manrope',sans-serif;color:var(--ink);position:relative;overflow:hidden;
  background:linear-gradient(135deg,#181650 0%,#06062D 100%)}
.frame{position:absolute;inset:18px;border:2px solid var(--red);border-radius:28px;z-index:3;pointer-events:none}
.blob-ring{position:absolute;z-index:0;top:-12%;right:-8%;width:46%;aspect-ratio:1;border-radius:50%;border:1.5px solid var(--blob-stroke)}
.blob-soft{position:absolute;z-index:0;bottom:-10%;left:-6%;width:42%;aspect-ratio:1;border-radius:50%;background:radial-gradient(circle,var(--blob-fill),transparent 70%);filter:blur(8px)}
.wrap{position:relative;z-index:1;height:100%;padding:8.5%;display:flex;flex-direction:column;justify-content:space-between}
.top{display:flex;justify-content:space-between;align-items:flex-start}
.gh-logo{width:clamp(72px,8.5vh,100px);height:clamp(72px,8.5vh,100px)}.gh-logo svg{width:100%;height:100%;display:block}
.eyebrow{font-size:clamp(18px,2.1vh,21px);font-weight:700;letter-spacing:.15em;text-transform:uppercase;text-align:right;line-height:1.5}
.eyebrow .red{color:var(--red)}
.btm{display:flex;flex-direction:column;gap:3vh}
.col{display:flex;flex-direction:column;align-items:flex-start;gap:2vh}
.quote{font-family:'Oranienbaum',serif;color:var(--red);font-size:clamp(120px,16vh,180px);line-height:.6;height:.55em}
.q{font-family:'Oranienbaum',serif;font-size:clamp(50px,7vh,86px);line-height:1.08;max-width:18ch}
.q em{font-style:italic;color:var(--red)}
.dash{display:flex;align-items:center;gap:14px;font-size:clamp(19px,2.1vh,22px);color:rgba(248,248,255,.7)}
.dash:before{content:"";width:42px;height:2px;background:var(--red)}
.cta{display:inline-flex;align-items:center;gap:10px;background:var(--red);color:#fff;padding:16px 28px;border-radius:8px;font-weight:700;font-size:clamp(22px,2.4vh,26px)}
.foot{display:flex;justify-content:space-between;align-items:flex-end;gap:18px}
.url{font-size:clamp(19px,2.1vh,23px);font-weight:600}
.cred{font-size:clamp(19px,2vh,21px);color:rgba(248,248,255,.62);text-align:right;max-width:26ch;line-height:1.4}
</style></head>
<body>
<div class="frame"></div><div class="blob-ring"></div><div class="blob-soft"></div>
<div class="wrap">
  <div class="top">
    <div class="gh-logo" aria-label="Ghost Research"><svg viewBox="0 0 100 100"><rect width="100" height="100" rx="22" fill="#EF4444"/><circle cx="50" cy="50" r="19" fill="#fff"/></svg></div>
    <div class="eyebrow">The De-Minimis Reset<br><span class="red">Drops 7 June 2026</span></div>
  </div>
  <div class="btm">
    <div class="col">
      <div class="quote">“</div>
      <div class="q">It isn't the duty that breaks the margin. It's the <em>€3 per parcel</em> you're not pricing.</div>
      <div class="dash">The reframe behind the landed-cost model</div>
      <span class="cta">Get the model when it drops →</span>
    </div>
    <div class="foot"><span class="url">Ghostresearch.com</span><span class="cred">1M+ curated sources · transparent citation · expert-vetted</span></div>
  </div>
</div>
</body></html>
```

---

## Concept 03 — The Lane P&L (base still)

**Tool:** pollinations
**Aspect:** 1:1
**Suggested filename:** `concept-03-lane-pnl-base.jpg`
**Maps to:** Visual C03 · Day 3

### Generation prompt
```
A single printed financial profit-and-loss statement lying on a dark walnut executive desk,
angled slightly, with visible column headers and a bold bottom summary row; a slim red
felt-tip pen rests across the page, its tip beginning a stroke through the bottom line; a
folded paper shipping label peeks from beneath one corner. The document fills the lower two
thirds at a slight angle, leaving the upper-left third clean dark negative space. Warm-cool
desk-lamp light from the right, cool ambient fill, the red pen the only saturated element.
Editorial photography, color-graded to deep indigo (#181650) and cool navy (#06062D), paper
pulled cool toward #F8F8FF, high detail, sharp focus on the document, premium B2B aesthetic
like The Economist. Photoreal, shot on Arri Alexa Mini with 50mm prime, shallow depth of
field. No legible text, no logos, no watermarks.

NEGATIVE: no robots, no AI-themed imagery, no brain circuits, no glowing nodes, no holograms,
no neon, no cyberpunk, no sci-fi UI, no high-fiving, no hands on keyboards, no fist bumps,
no smiling-at-camera lifestyle, no AI-generated faces, no uncanny features, no people,
no readable text, no logos, no watermarks.
```

---

## Concept 03 — The Lane P&L (composite · Template A)

**Tool:** editorial
**Style preset:** Template A — Dark Photo Hero (Cinematic + LinkedIn)
**Aspect:** 1:1
**Suggested filename:** `concept-03-lane-pnl.png`
**Maps to:** Visual C03 · Day 3 (Week 1 hype, LinkedIn)

### Generation prompt
```html
<!doctype html><html><head><meta charset="utf-8"/>
<link href="https://fonts.googleapis.com/css2?family=Oranienbaum&family=Manrope:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<style>
*{box-sizing:border-box;margin:0;padding:0}
:root{--ink:#F8F8FF;--red:#EF4444;--blob-stroke:rgba(248,248,255,.14)}
body{width:100%;height:100vh;font-family:'Manrope',sans-serif;color:var(--ink);position:relative;overflow:hidden;
  background:linear-gradient(10deg,rgba(6,6,45,.95) 6%,rgba(6,6,45,.5) 46%,rgba(6,6,45,.12) 100%),
  url("GHOST_ASSET:concept-03-lane-pnl-base.jpg");background-size:cover;background-position:center}
.frame{position:absolute;inset:18px;border:2px solid var(--red);border-radius:28px;z-index:3;pointer-events:none}
.blob-ring{position:absolute;z-index:0;top:-12%;right:-8%;width:46%;aspect-ratio:1;border-radius:50%;border:1.5px solid var(--blob-stroke)}
.wrap{position:relative;z-index:1;height:100%;padding:8.5%;display:flex;flex-direction:column;justify-content:space-between}
.top{display:flex;justify-content:space-between;align-items:flex-start}
.gh-logo{width:clamp(72px,8.5vh,100px);height:clamp(72px,8.5vh,100px)}.gh-logo svg{width:100%;height:100%;display:block}
.eyebrow{font-size:clamp(18px,2.1vh,21px);font-weight:700;letter-spacing:.14em;text-transform:uppercase;text-align:right;line-height:1.5;max-width:16ch}
.eyebrow .red{color:var(--red)}
.btm{display:flex;flex-direction:column;gap:3vh}
.col{display:flex;flex-direction:column;align-items:flex-start;gap:2.2vh;max-width:22ch}
.h1{font-family:'Oranienbaum',serif;font-size:clamp(58px,8vh,100px);line-height:1.03}
.h1 em{font-style:italic;color:var(--red)}
.sub{font-size:clamp(22px,2.6vh,29px);color:rgba(248,248,255,.82);line-height:1.45;max-width:30ch}
.sub .red{color:var(--red);font-weight:600}
.cta{display:inline-flex;align-items:center;gap:10px;background:var(--red);color:#fff;padding:16px 28px;border-radius:8px;font-weight:700;font-size:clamp(22px,2.4vh,26px)}
.foot{display:flex;justify-content:space-between;align-items:flex-end;gap:18px}
.url{font-size:clamp(19px,2.1vh,23px);font-weight:600}
.cred{font-size:clamp(19px,2vh,21px);color:rgba(248,248,255,.62);text-align:right;max-width:26ch;line-height:1.4}
</style></head>
<body>
<div class="frame"></div><div class="blob-ring"></div>
<div class="wrap">
  <div class="top">
    <div class="gh-logo" aria-label="Ghost Research"><svg viewBox="0 0 100 100"><rect width="100" height="100" rx="22" fill="#EF4444"/><circle cx="50" cy="50" r="19" fill="#fff"/></svg></div>
    <div class="eyebrow"><span class="red">For heads of</span><br>cross-border &amp; supply chain</div>
  </div>
  <div class="btm">
    <div class="col">
      <h1 class="h1">Your landed-cost model was built for a world that <em>ends 1 July.</em></h1>
      <div class="sub">We re-ran the math the rule change breaks — by SKU, by lane. <span class="red">Publishes 7 June.</span></div>
      <span class="cta">Reserve early access →</span>
    </div>
    <div class="foot"><span class="url">Ghostresearch.com</span><span class="cred">1M+ curated sources · transparent citation · expert-vetted</span></div>
  </div>
</div>
</body></html>
```

---

## Concept 04 — €150 → ? (Template D — Light Stat Card)

**Tool:** editorial
**Style preset:** Template D — Light Stat Card (LIGHT THEME)
**Aspect:** 1:1
**Suggested filename:** `concept-04-150.png`
**Maps to:** Visual C04 · Day 4 (Week 1 hype) · LIGHT THEME + blobs

### Generation prompt
```html
<!doctype html><html><head><meta charset="utf-8"/>
<link href="https://fonts.googleapis.com/css2?family=Oranienbaum&family=Manrope:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<style>
*{box-sizing:border-box;margin:0;padding:0}
:root{--ink:#0B0B14;--red:#EF4444;--blob-stroke:rgba(239,68,68,.22);--blob-fill:rgba(239,68,68,.08)}
body{width:100%;height:100vh;font-family:'Manrope',sans-serif;color:var(--ink);position:relative;overflow:hidden;background:#F1F3FF}
.blob-ring{position:absolute;z-index:0;top:-14%;right:-10%;width:50%;aspect-ratio:1;border-radius:50%;border:1.5px solid var(--blob-stroke)}
.blob-soft{position:absolute;z-index:0;bottom:-12%;left:-8%;width:44%;aspect-ratio:1;border-radius:50%;background:radial-gradient(circle,var(--blob-fill),transparent 70%);filter:blur(8px)}
.wrap{position:relative;z-index:1;height:100%;padding:8.5%;display:flex;flex-direction:column;justify-content:space-between}
.top{display:flex;justify-content:space-between;align-items:flex-start}
.gh-logo{width:clamp(72px,8.5vh,100px);height:clamp(72px,8.5vh,100px)}.gh-logo svg{width:100%;height:100%;display:block}
.mast{font-family:'Oranienbaum',serif;font-size:clamp(20px,2.4vh,26px);letter-spacing:.03em;text-align:right;line-height:1.3}
.mast b{color:#000}
.btm{display:flex;flex-direction:column;gap:3vh}
.col{display:flex;flex-direction:column;align-items:flex-start;gap:2vh;padding-left:26px;border-left:4px solid var(--red)}
.eyebrow{font-size:clamp(18px,2.1vh,21px);font-weight:700;letter-spacing:.14em;text-transform:uppercase;color:var(--red)}
.stat{font-family:'Oranienbaum',serif;font-size:clamp(130px,21vh,250px);line-height:.9;letter-spacing:-.03em;color:#000}
.stat em{font-style:normal;color:var(--red)}
.sub{font-size:clamp(24px,2.8vh,32px);color:var(--ink);line-height:1.4;max-width:26ch}
.cta{display:inline-flex;align-items:center;gap:10px;background:var(--red);color:#fff;padding:16px 28px;border-radius:8px;font-weight:700;font-size:clamp(22px,2.4vh,26px)}
.foot{display:flex;justify-content:space-between;align-items:flex-end;gap:18px}
.url{font-size:clamp(19px,2.1vh,23px);font-weight:700;color:#000}
.cred{font-size:clamp(19px,2vh,21px);color:rgba(11,11,20,.6);text-align:right;max-width:26ch;line-height:1.4}
</style></head>
<body class="light">
<div class="blob-ring"></div><div class="blob-soft"></div>
<div class="wrap">
  <div class="top">
    <div class="gh-logo" aria-label="Ghost Research"><svg viewBox="0 0 100 100"><rect width="100" height="100" rx="22" fill="#EF4444"/><circle cx="50" cy="50" r="19" fill="#fff"/></svg></div>
    <div class="mast"><b>GHOST RESEARCH</b><br>De-minimis reset · drops 7 June</div>
  </div>
  <div class="btm">
    <div class="col">
      <div class="eyebrow">The threshold that disappears</div>
      <div class="stat">€150 <em>→ ?</em></div>
      <div class="sub">The free-clearance threshold every cross-border SKU relied on closes 1 July.</div>
      <span class="cta">Notify me on launch →</span>
    </div>
    <div class="foot"><span class="url">Ghostresearch.com</span><span class="cred">1M+ curated sources · transparent citation · expert-vetted</span></div>
  </div>
</div>
</body></html>
```

---

## Concept 05 — The Questions (Template B — Journal Cover, dark)

**Tool:** editorial
**Style preset:** Template B — Journal Cover
**Aspect:** 1:1
**Suggested filename:** `concept-05-skus.png`
**Maps to:** Visual C05 · Day 5 (Week 1 hype, Hook 1→2 swap) · LinkedIn

### Generation prompt
```html
<!doctype html><html><head><meta charset="utf-8"/>
<link href="https://fonts.googleapis.com/css2?family=Oranienbaum&family=Manrope:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<style>
*{box-sizing:border-box;margin:0;padding:0}
:root{--ink:#F8F8FF;--red:#EF4444;--blob-stroke:rgba(248,248,255,.12)}
body{width:100%;height:100vh;font-family:'Manrope',sans-serif;color:var(--ink);position:relative;overflow:hidden;background:linear-gradient(150deg,#181650 0%,#06062D 100%)}
.frame{position:absolute;inset:18px;border:2px solid var(--red);border-radius:28px;z-index:3;pointer-events:none}
.blob-ring{position:absolute;z-index:0;bottom:-14%;right:-8%;width:48%;aspect-ratio:1;border-radius:50%;border:1.5px solid var(--blob-stroke)}
.wrap{position:relative;z-index:1;height:100%;padding:8.5%;display:flex;flex-direction:column;justify-content:space-between}
.mast{display:flex;justify-content:space-between;align-items:center;border-bottom:1px solid rgba(248,248,255,.22);padding-bottom:2.2vh}
.brand{display:flex;align-items:center;gap:16px}
.gh-logo{width:clamp(64px,7.5vh,90px);height:clamp(64px,7.5vh,90px)}.gh-logo svg{width:100%;height:100%;display:block}
.wm{font-family:'Manrope',sans-serif;font-weight:800;letter-spacing:.16em;font-size:clamp(22px,2.6vh,30px)}
.pub{font-size:clamp(17px,2vh,20px);font-weight:700;letter-spacing:.14em;text-transform:uppercase;text-align:right;line-height:1.5;color:rgba(248,248,255,.8)}
.pub .red{color:var(--red)}
.btm{display:flex;flex-direction:column;gap:2.6vh}
.eyebrow{font-size:clamp(18px,2.1vh,21px);font-weight:700;letter-spacing:.14em;text-transform:uppercase;color:var(--red)}
.h1{font-family:'Oranienbaum',serif;font-size:clamp(58px,8.4vh,108px);line-height:1.0;max-width:15ch}
.h1 em{font-style:italic;color:var(--red)}
.rule{height:1px;width:100%;background:rgba(248,248,255,.22)}
.list{display:flex;flex-direction:column;gap:1.3vh}
.li{display:flex;gap:16px;align-items:baseline;font-size:clamp(23px,2.7vh,31px);color:rgba(248,248,255,.9)}
.li b{color:var(--red)}
.cta{display:inline-flex;align-items:center;gap:10px;background:var(--red);color:#fff;padding:16px 28px;border-radius:8px;font-weight:700;font-size:clamp(22px,2.4vh,26px);width:fit-content}
.foot{display:flex;justify-content:space-between;align-items:flex-end;gap:18px}
.url{font-size:clamp(19px,2.1vh,23px);font-weight:600}
.cred{font-size:clamp(19px,2vh,21px);color:rgba(248,248,255,.62);text-align:right}
</style></head>
<body>
<div class="frame"></div><div class="blob-ring"></div>
<div class="wrap">
  <div class="mast">
    <div class="brand">
      <div class="gh-logo" aria-label="Ghost Research"><svg viewBox="0 0 100 100"><rect width="100" height="100" rx="22" fill="#EF4444"/><circle cx="50" cy="50" r="19" fill="#fff"/></svg></div>
      <div class="wm">GHOST RESEARCH</div>
    </div>
    <div class="pub">The De-Minimis Reset<br><span class="red">Drops 7 June</span></div>
  </div>
  <div class="btm">
    <div class="eyebrow">Before you reprice</div>
    <h1 class="h1">You can't reprice 10,000 SKUs in the <em>dark.</em></h1>
    <div class="rule"></div>
    <div class="list">
      <div class="li"><b>·</b>Which lanes break first?</div>
      <div class="li"><b>·</b>Which price bands go underwater?</div>
      <div class="li"><b>·</b>Bulk pre-clear, or localize like Shein &amp; Temu?</div>
      <div class="li"><b>·</b>Which SKUs do you touch first?</div>
    </div>
    <span class="cta">Reserve early access →</span>
    <div class="foot"><span class="url">Ghostresearch.com</span><span class="cred">DROPS 7 JUNE · EXPERT-VETTED</span></div>
  </div>
</div>
</body></html>
```

---

## Concept 06 — Two Routes Diverge (dark graphic · Template A chassis)

**Tool:** editorial
**Style preset:** Template A chassis — graphic (Suspense)
**Aspect:** 1:1
**Suggested filename:** `concept-06-routes.png`
**Maps to:** Visual C06 · Day 6 (Week 1 hype)

### Generation prompt
```html
<!doctype html><html><head><meta charset="utf-8"/>
<link href="https://fonts.googleapis.com/css2?family=Oranienbaum&family=Manrope:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<style>
*{box-sizing:border-box;margin:0;padding:0}
:root{--ink:#F8F8FF;--red:#EF4444}
body{width:100%;height:100vh;font-family:'Manrope',sans-serif;color:var(--ink);position:relative;overflow:hidden;background:linear-gradient(135deg,#181650 0%,#06062D 100%)}
.frame{position:absolute;inset:18px;border:2px solid var(--red);border-radius:28px;z-index:3;pointer-events:none}
.map{position:absolute;inset:0;z-index:0}
.lbl{font-size:20px;fill:rgba(248,248,255,.7);font-family:'Manrope',sans-serif}
.wrap{position:relative;z-index:1;height:100%;padding:8.5%;display:flex;flex-direction:column;justify-content:space-between}
.top{display:flex;justify-content:space-between;align-items:flex-start}
.gh-logo{width:clamp(72px,8.5vh,100px);height:clamp(72px,8.5vh,100px)}.gh-logo svg{width:100%;height:100%;display:block}
.eyebrow{font-size:clamp(18px,2.1vh,21px);font-weight:700;letter-spacing:.14em;text-transform:uppercase;text-align:right;color:var(--red)}
.btm{display:flex;flex-direction:column;gap:3vh}
.col{display:flex;flex-direction:column;align-items:flex-start;gap:2.2vh;max-width:20ch}
.h1{font-family:'Oranienbaum',serif;font-size:clamp(58px,8vh,100px);line-height:1.02}
.h1 em{font-style:italic;color:var(--red)}
.sub{font-size:clamp(22px,2.6vh,29px);color:rgba(248,248,255,.82);line-height:1.45;max-width:28ch}
.cta{display:inline-flex;align-items:center;gap:10px;background:var(--red);color:#fff;padding:16px 28px;border-radius:8px;font-weight:700;font-size:clamp(22px,2.4vh,26px)}
.foot{display:flex;justify-content:space-between;align-items:flex-end;gap:18px}
.url{font-size:clamp(19px,2.1vh,23px);font-weight:600}
.cred{font-size:clamp(19px,2vh,21px);color:rgba(248,248,255,.62);text-align:right;max-width:26ch;line-height:1.4}
</style></head>
<body>
<svg class="map" viewBox="0 0 1080 1080" preserveAspectRatio="xMidYMid slice">
  <g fill="none" stroke="rgba(248,248,255,.10)" stroke-width="1"><path d="M0 360 H1080 M0 540 H1080 M0 720 H1080 M360 0 V1080 M720 0 V1080"/></g>
  <circle cx="250" cy="430" r="9" fill="rgba(248,248,255,.55)"/>
  <path d="M250 430 C 500 340, 760 330, 980 320" stroke="rgba(248,248,255,.35)" stroke-width="3" stroke-dasharray="2 12" fill="none"/>
  <path d="M250 430 C 420 470, 560 560, 640 660" stroke="#EF4444" stroke-width="4" fill="none"/>
  <rect x="620" y="652" width="40" height="40" rx="6" fill="#EF4444"/>
  <text x="980" y="300" class="lbl" text-anchor="end">old direct lane</text>
  <text x="672" y="690" class="lbl">local fulfilment</text>
</svg>
<div class="frame"></div>
<div class="wrap">
  <div class="top">
    <div class="gh-logo" aria-label="Ghost Research"><svg viewBox="0 0 100 100"><rect width="100" height="100" rx="22" fill="#EF4444"/><circle cx="50" cy="50" r="19" fill="#fff"/></svg></div>
    <div class="eyebrow">The competitive response</div>
  </div>
  <div class="btm">
    <div class="col">
      <h1 class="h1">Shein re-localized. Have you <em>re-modeled?</em></h1>
      <div class="sub">The rule is everywhere. The math isn't. The landed-cost model drops 7 June.</div>
      <span class="cta">Get the model when it drops →</span>
    </div>
    <div class="foot"><span class="url">Ghostresearch.com</span><span class="cred">1M+ curated sources · transparent citation · expert-vetted</span></div>
  </div>
</div>
</body></html>
```

---

## Concept 07 — Publish Eve (base still)

**Tool:** pollinations
**Aspect:** 1:1
**Suggested filename:** `concept-07-publish-eve-base.jpg`
**Maps to:** Visual C07 · Day 7

### Generation prompt
```
A closed hardcover research report resting on a dark desk at dawn, seen edge-on so only its
thick page block and a thin red ribbon bookmark catch the first cool light; a single brown
shipping parcel sits slightly behind it, softly out of focus. The report occupies the lower
third, the red ribbon the single focal accent, upper two thirds an empty pool of pre-dawn
indigo. One soft cool window-light edge from the left, everything else falling to near-black.
Editorial photography, color-graded to deep indigo (#181650) and cool navy (#06062D), accent
red (#EF4444) only on the ribbon, shallow depth of field, premium B2B aesthetic like a
Financial Times cover still. Photoreal, shot on Arri Alexa Mini with 50mm prime. No text,
no logos, no watermarks.

NEGATIVE: no robots, no AI-themed imagery, no brain circuits, no glowing nodes, no holograms,
no neon, no cyberpunk, no sci-fi UI, no high-fiving, no hands on keyboards, no fist bumps,
no smiling-at-camera lifestyle, no AI-generated faces, no uncanny features, no people,
no text in image, no logos, no watermarks.
```

---

## Concept 07 — Publish Eve (composite · Template A)

**Tool:** editorial
**Style preset:** Template A — Dark Photo Hero (Cinematic)
**Aspect:** 1:1
**Suggested filename:** `concept-07-publish-eve.png`
**Maps to:** Visual C07 · Day 7 (Week 1 hype, publish-eve)

### Generation prompt
```html
<!doctype html><html><head><meta charset="utf-8"/>
<link href="https://fonts.googleapis.com/css2?family=Oranienbaum&family=Manrope:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<style>
*{box-sizing:border-box;margin:0;padding:0}
:root{--ink:#F8F8FF;--red:#EF4444;--blob-stroke:rgba(248,248,255,.14)}
body{width:100%;height:100vh;font-family:'Manrope',sans-serif;color:var(--ink);position:relative;overflow:hidden;
  background:linear-gradient(8deg,rgba(6,6,45,.95) 6%,rgba(6,6,45,.45) 50%,rgba(6,6,45,.1) 100%),
  url("GHOST_ASSET:concept-07-publish-eve-base.jpg");background-size:cover;background-position:center}
.frame{position:absolute;inset:18px;border:2px solid var(--red);border-radius:28px;z-index:3;pointer-events:none}
.blob-ring{position:absolute;z-index:0;top:-12%;right:-8%;width:46%;aspect-ratio:1;border-radius:50%;border:1.5px solid var(--blob-stroke)}
.wrap{position:relative;z-index:1;height:100%;padding:8.5%;display:flex;flex-direction:column;justify-content:space-between}
.top{display:flex;justify-content:space-between;align-items:flex-start}
.gh-logo{width:clamp(72px,8.5vh,100px);height:clamp(72px,8.5vh,100px)}.gh-logo svg{width:100%;height:100%;display:block}
.eyebrow{font-size:clamp(18px,2.1vh,21px);font-weight:700;letter-spacing:.14em;text-transform:uppercase;text-align:right;color:var(--red)}
.btm{display:flex;flex-direction:column;gap:3vh}
.col{display:flex;flex-direction:column;align-items:flex-start;gap:2.2vh;max-width:20ch}
.h1{font-family:'Oranienbaum',serif;font-size:clamp(60px,8.4vh,104px);line-height:1.02}
.h1 em{font-style:italic;color:var(--red)}
.cta{display:inline-flex;align-items:center;gap:10px;background:var(--red);color:#fff;padding:16px 28px;border-radius:8px;font-weight:700;font-size:clamp(22px,2.4vh,26px)}
.foot{display:flex;justify-content:space-between;align-items:flex-end;gap:18px}
.url{font-size:clamp(19px,2.1vh,23px);font-weight:600}
.cred{font-size:clamp(19px,2vh,21px);color:rgba(248,248,255,.62);text-align:right;max-width:26ch;line-height:1.4}
</style></head>
<body>
<div class="frame"></div><div class="blob-ring"></div>
<div class="wrap">
  <div class="top">
    <div class="gh-logo" aria-label="Ghost Research"><svg viewBox="0 0 100 100"><rect width="100" height="100" rx="22" fill="#EF4444"/><circle cx="50" cy="50" r="19" fill="#fff"/></svg></div>
    <div class="eyebrow">Publishes tomorrow · 7 June</div>
  </div>
  <div class="btm">
    <div class="col">
      <h1 class="h1">Tomorrow it's live: the model for the <em>post-de-minimis</em> world.</h1>
      <span class="cta">Be first to read →</span>
    </div>
    <div class="foot"><span class="url">Ghostresearch.com</span><span class="cred">1M+ curated sources · transparent citation · expert-vetted</span></div>
  </div>
</div>
</body></html>
```

---

## Concept 08 — The Lane That Broke First (Template A — stat hero)

**Tool:** editorial
**Style preset:** Template A — Dark Photo Hero (UI-restraint, stat hero)
**Aspect:** 1:1
**Suggested filename:** `concept-08-lane-loss.png`
**Maps to:** Visual C08 · Days 8–9 (Week 2 — report live) · retargeting-coded

### Generation prompt
```html
<!doctype html><html><head><meta charset="utf-8"/>
<link href="https://fonts.googleapis.com/css2?family=Oranienbaum&family=Manrope:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<style>
*{box-sizing:border-box;margin:0;padding:0}
:root{--ink:#F8F8FF;--red:#EF4444;--blob-stroke:rgba(248,248,255,.14)}
body{width:100%;height:100vh;font-family:'Manrope',sans-serif;color:var(--ink);position:relative;overflow:hidden;
  background:linear-gradient(0deg,rgba(6,6,45,.96) 8%,rgba(6,6,45,.55) 48%,rgba(6,6,45,.2) 100%),
  url("GHOST_ASSET:concept-01-parcel-base.jpg");background-size:cover;background-position:center}
.frame{position:absolute;inset:18px;border:2px solid var(--red);border-radius:28px;z-index:3;pointer-events:none}
.blob-ring{position:absolute;z-index:0;top:-12%;right:-8%;width:46%;aspect-ratio:1;border-radius:50%;border:1.5px solid var(--blob-stroke)}
.wrap{position:relative;z-index:1;height:100%;padding:8.5%;display:flex;flex-direction:column;justify-content:space-between}
.top{display:flex;justify-content:space-between;align-items:flex-start}
.gh-logo{width:clamp(72px,8.5vh,100px);height:clamp(72px,8.5vh,100px)}.gh-logo svg{width:100%;height:100%;display:block}
.eyebrow{font-size:clamp(18px,2.1vh,21px);font-weight:700;letter-spacing:.14em;text-transform:uppercase;text-align:right;color:var(--red)}
.btm{display:flex;flex-direction:column;gap:3vh}
.col{display:flex;flex-direction:column;align-items:flex-start;gap:2vh;max-width:24ch}
.lead{font-size:clamp(22px,2.6vh,30px);color:rgba(248,248,255,.85)}
.stat{font-family:'Oranienbaum',serif;color:var(--red);font-size:clamp(120px,17vh,200px);line-height:.85;letter-spacing:-.02em}
.sub{font-size:clamp(22px,2.6vh,29px);color:rgba(248,248,255,.82);line-height:1.45;max-width:28ch}
.sub .red{color:var(--red);font-weight:600}
.cta{display:inline-flex;align-items:center;gap:10px;background:var(--red);color:#fff;padding:16px 28px;border-radius:8px;font-weight:700;font-size:clamp(22px,2.4vh,26px)}
.foot{display:flex;justify-content:space-between;align-items:flex-end;gap:18px}
.url{font-size:clamp(19px,2.1vh,23px);font-weight:600}
.cred{font-size:clamp(19px,2vh,21px);color:rgba(248,248,255,.62);text-align:right;max-width:30ch;line-height:1.4}
</style></head>
<body>
<div class="frame"></div><div class="blob-ring"></div>
<div class="wrap">
  <div class="top">
    <div class="gh-logo" aria-label="Ghost Research"><svg viewBox="0 0 100 100"><rect width="100" height="100" rx="22" fill="#EF4444"/><circle cx="50" cy="50" r="19" fill="#fff"/></svg></div>
    <div class="eyebrow">Available now · published 7 June</div>
  </div>
  <div class="btm">
    <div class="col">
      <div class="lead">On the China→EU lane, a $22 SKU now lands at</div>
      <div class="stat">−100%</div>
      <div class="sub">net margin. The brief models <span class="red">every price band, every lane</span> — and where it breaks first.</div>
      <span class="cta">Read the brief →</span>
    </div>
    <div class="foot"><span class="url">Ghostresearch.com</span><span class="cred">Illustrative · China→EU lane · source: Ghost Research, De-Minimis Reset 2026</span></div>
  </div>
</div>
</body></html>
```

---

## Concept 09 — It's Live (Template B — Journal Cover, launch)

**Tool:** editorial
**Style preset:** Template B — Journal Cover (Week-2 launch)
**Aspect:** 1:1
**Suggested filename:** `concept-09-launch.png`
**Maps to:** Visual C09 · Day 8 launch + Day 14 close-out (Week 2)

### Generation prompt
```html
<!doctype html><html><head><meta charset="utf-8"/>
<link href="https://fonts.googleapis.com/css2?family=Oranienbaum&family=Manrope:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<style>
*{box-sizing:border-box;margin:0;padding:0}
:root{--ink:#F8F8FF;--red:#EF4444;--blob-stroke:rgba(248,248,255,.12)}
body{width:100%;height:100vh;font-family:'Manrope',sans-serif;color:var(--ink);position:relative;overflow:hidden;background:linear-gradient(150deg,#181650 0%,#06062D 100%)}
.frame{position:absolute;inset:18px;border:2px solid var(--red);border-radius:28px;z-index:3;pointer-events:none}
.blob-ring{position:absolute;z-index:0;bottom:-14%;right:-8%;width:48%;aspect-ratio:1;border-radius:50%;border:1.5px solid var(--blob-stroke)}
.wrap{position:relative;z-index:1;height:100%;padding:8.5%;display:flex;flex-direction:column;justify-content:space-between}
.mast{display:flex;justify-content:space-between;align-items:center;border-bottom:1px solid rgba(248,248,255,.22);padding-bottom:2.2vh}
.brand{display:flex;align-items:center;gap:16px}
.gh-logo{width:clamp(64px,7.5vh,90px);height:clamp(64px,7.5vh,90px)}.gh-logo svg{width:100%;height:100%;display:block}
.wm{font-weight:800;letter-spacing:.16em;font-size:clamp(22px,2.6vh,30px)}
.pub{font-size:clamp(17px,2vh,20px);font-weight:700;letter-spacing:.14em;text-transform:uppercase;text-align:right;line-height:1.5;color:rgba(248,248,255,.8)}
.pub .red{color:var(--red)}
.btm{display:flex;flex-direction:column;gap:2.4vh}
.eyebrow{font-size:clamp(18px,2.1vh,21px);font-weight:700;letter-spacing:.14em;text-transform:uppercase;color:var(--red)}
.h1{font-family:'Oranienbaum',serif;font-size:clamp(60px,8.6vh,112px);line-height:1.0;max-width:14ch}
.h1 em{font-style:italic;color:var(--red)}
.rule{height:1px;width:100%;background:rgba(248,248,255,.22)}
.list{display:flex;flex-direction:column;gap:1.2vh}
.li{display:flex;gap:16px;align-items:baseline;font-size:clamp(22px,2.6vh,30px);color:rgba(248,248,255,.9)}
.li b{color:var(--red)}
.cta{display:inline-flex;align-items:center;gap:10px;background:var(--red);color:#fff;padding:16px 28px;border-radius:8px;font-weight:700;font-size:clamp(22px,2.4vh,26px);width:fit-content}
.foot{display:flex;justify-content:space-between;align-items:flex-end;gap:18px}
.url{font-size:clamp(19px,2.1vh,23px);font-weight:600}
.cred{font-size:clamp(19px,2vh,21px);color:rgba(248,248,255,.62);text-align:right}
</style></head>
<body>
<div class="frame"></div><div class="blob-ring"></div>
<div class="wrap">
  <div class="mast">
    <div class="brand">
      <div class="gh-logo" aria-label="Ghost Research"><svg viewBox="0 0 100 100"><rect width="100" height="100" rx="22" fill="#EF4444"/><circle cx="50" cy="50" r="19" fill="#fff"/></svg></div>
      <div class="wm">GHOST RESEARCH</div>
    </div>
    <div class="pub">The De-Minimis Reset<br><span class="red">Available now</span></div>
  </div>
  <div class="btm">
    <div class="eyebrow">It's live</div>
    <h1 class="h1">The <em>$147B</em> landed-cost map is published.</h1>
    <div class="rule"></div>
    <div class="list">
      <div class="li"><b>·</b>The China→EU lane, modeled band by band.</div>
      <div class="li"><b>·</b>Where margin breaks first — and which SKUs to touch.</div>
      <div class="li"><b>·</b>The Shein &amp; Temu localization response, mapped.</div>
    </div>
    <span class="cta">Read the brief →</span>
    <div class="foot"><span class="url">Ghostresearch.com</span><span class="cred">EXPERT-VETTED · FULLY CITED</span></div>
  </div>
</div>
</body></html>
```

---

## Concept 10 — Three Lanes, Three Answers (dark bar graphic · Template A chassis)

**Tool:** editorial
**Style preset:** Template A chassis — comparison graphic
**Aspect:** 1:1
**Suggested filename:** `concept-10-three-lanes.png`
**Maps to:** Visual C10 · Days 10 & 12 (Week 2 — report live)

### Generation prompt
```html
<!doctype html><html><head><meta charset="utf-8"/>
<link href="https://fonts.googleapis.com/css2?family=Oranienbaum&family=Manrope:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<style>
*{box-sizing:border-box;margin:0;padding:0}
:root{--ink:#F8F8FF;--red:#EF4444;--blob-stroke:rgba(248,248,255,.12)}
body{width:100%;height:100vh;font-family:'Manrope',sans-serif;color:var(--ink);position:relative;overflow:hidden;background:linear-gradient(135deg,#181650 0%,#06062D 100%)}
.frame{position:absolute;inset:18px;border:2px solid var(--red);border-radius:28px;z-index:3;pointer-events:none}
.blob-ring{position:absolute;z-index:0;top:-12%;right:-8%;width:44%;aspect-ratio:1;border-radius:50%;border:1.5px solid var(--blob-stroke)}
.wrap{position:relative;z-index:1;height:100%;padding:8.5%;display:flex;flex-direction:column;justify-content:space-between}
.top{display:flex;justify-content:space-between;align-items:flex-start}
.gh-logo{width:clamp(72px,8.5vh,100px);height:clamp(72px,8.5vh,100px)}.gh-logo svg{width:100%;height:100%;display:block}
.eyebrow{font-size:clamp(18px,2.1vh,21px);font-weight:700;letter-spacing:.14em;text-transform:uppercase;text-align:right;color:var(--red)}
.btm{display:flex;flex-direction:column;gap:2.6vh}
.h1{font-family:'Oranienbaum',serif;font-size:clamp(54px,7.4vh,92px);line-height:1.02;max-width:16ch}
.h1 em{font-style:italic;color:var(--red)}
.bars{display:flex;flex-direction:column;gap:1.6vh}
.row{display:flex;align-items:center;gap:18px}
.name{width:9ch;font-size:clamp(20px,2.3vh,26px);font-weight:600}
.track{flex:1;height:30px;background:rgba(248,248,255,.12);border-radius:6px;overflow:hidden}
.fill{height:100%;background:rgba(248,248,255,.4);border-radius:6px}
.row.worst .fill{background:var(--red)}
.v{width:5ch;text-align:right;font-size:clamp(20px,2.3vh,26px);font-weight:800}
.row.worst .v{color:var(--red)}
.foot{display:flex;justify-content:space-between;align-items:flex-end;gap:18px}
.cta{display:inline-flex;align-items:center;gap:10px;background:var(--red);color:#fff;padding:14px 24px;border-radius:8px;font-weight:700;font-size:clamp(21px,2.3vh,25px)}
.url{font-size:clamp(19px,2.1vh,23px);font-weight:600}
.cred{font-size:clamp(19px,2vh,21px);color:rgba(248,248,255,.62);text-align:right;max-width:24ch;line-height:1.4}
</style></head>
<body>
<div class="frame"></div><div class="blob-ring"></div>
<div class="wrap">
  <div class="top">
    <div class="gh-logo" aria-label="Ghost Research"><svg viewBox="0 0 100 100"><rect width="100" height="100" rx="22" fill="#EF4444"/><circle cx="50" cy="50" r="19" fill="#fff"/></svg></div>
    <div class="eyebrow">Available now</div>
  </div>
  <div class="btm">
    <h1 class="h1">Three lanes. Three completely different <em>answers.</em></h1>
    <div class="bars">
      <div class="row worst"><span class="name">China→EU</span><span class="track"><span class="fill" style="width:14%"></span></span><span class="v">−100%</span></div>
      <div class="row"><span class="name">China→US</span><span class="track"><span class="fill" style="width:55%"></span></span><span class="v">−7 pts</span></div>
      <div class="row"><span class="name">Intra-EU</span><span class="track"><span class="fill" style="width:82%"></span></span><span class="v">−2 pts</span></div>
    </div>
    <div class="foot">
      <span class="cta">Read the brief →</span>
      <span class="cred">Net-margin retained by lane · Ghost Research, De-Minimis Reset 2026</span>
    </div>
    <div class="url">Ghostresearch.com</div>
  </div>
</div>
</body></html>
```

---

## Concept 11 — Which SKUs First? (Template D — Light Stat Card, ranked)

**Tool:** editorial
**Style preset:** Template D — Light Stat Card (LIGHT THEME)
**Aspect:** 1:1
**Suggested filename:** `concept-11-which-skus.png`
**Maps to:** Visual C11 · Day 13 (Week 2 — report live) · LIGHT THEME + blobs

### Generation prompt
```html
<!doctype html><html><head><meta charset="utf-8"/>
<link href="https://fonts.googleapis.com/css2?family=Oranienbaum&family=Manrope:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<style>
*{box-sizing:border-box;margin:0;padding:0}
:root{--ink:#0B0B14;--red:#EF4444;--blob-stroke:rgba(239,68,68,.22);--blob-fill:rgba(239,68,68,.08)}
body{width:100%;height:100vh;font-family:'Manrope',sans-serif;color:var(--ink);position:relative;overflow:hidden;background:#F1F3FF}
.blob-ring{position:absolute;z-index:0;top:-14%;right:-10%;width:50%;aspect-ratio:1;border-radius:50%;border:1.5px solid var(--blob-stroke)}
.blob-soft{position:absolute;z-index:0;bottom:-12%;left:-8%;width:44%;aspect-ratio:1;border-radius:50%;background:radial-gradient(circle,var(--blob-fill),transparent 70%);filter:blur(8px)}
.wrap{position:relative;z-index:1;height:100%;padding:8.5%;display:flex;flex-direction:column;justify-content:space-between}
.top{display:flex;justify-content:space-between;align-items:flex-start}
.gh-logo{width:clamp(72px,8.5vh,100px);height:clamp(72px,8.5vh,100px)}.gh-logo svg{width:100%;height:100%;display:block}
.mast{font-family:'Oranienbaum',serif;font-size:clamp(20px,2.4vh,26px);letter-spacing:.03em;text-align:right;line-height:1.3}
.mast b{color:#000}
.btm{display:flex;flex-direction:column;gap:2.6vh;padding-left:26px;border-left:4px solid var(--red)}
.eyebrow{font-size:clamp(18px,2.1vh,21px);font-weight:700;letter-spacing:.14em;text-transform:uppercase;color:var(--red)}
.hero{font-family:'Oranienbaum',serif;font-size:clamp(70px,11vh,128px);line-height:.96;letter-spacing:-.02em;color:#000;max-width:11ch}
.hero em{font-style:normal;color:var(--red)}
.list{display:flex;flex-direction:column;gap:1.4vh;font-size:clamp(24px,2.8vh,32px)}
.li{display:flex;gap:18px;align-items:baseline}
.num{font-family:'Oranienbaum',serif;color:var(--red);font-size:clamp(28px,3.2vh,38px);min-width:1.4ch}
.li.top b{color:var(--red)}
.cta{display:inline-flex;align-items:center;gap:10px;background:var(--red);color:#fff;padding:16px 28px;border-radius:8px;font-weight:700;font-size:clamp(22px,2.4vh,26px);width:fit-content}
.foot{display:flex;justify-content:space-between;align-items:flex-end;gap:18px}
.url{font-size:clamp(19px,2.1vh,23px);font-weight:700;color:#000}
.cred{font-size:clamp(19px,2vh,21px);color:rgba(11,11,20,.6);text-align:right;max-width:22ch;line-height:1.4}
</style></head>
<body class="light">
<div class="blob-ring"></div><div class="blob-soft"></div>
<div class="wrap">
  <div class="top">
    <div class="gh-logo" aria-label="Ghost Research"><svg viewBox="0 0 100 100"><rect width="100" height="100" rx="22" fill="#EF4444"/><circle cx="50" cy="50" r="19" fill="#fff"/></svg></div>
    <div class="mast"><b>GHOST RESEARCH</b><br>Available now</div>
  </div>
  <div class="btm">
    <div class="eyebrow">Two weeks to reprice</div>
    <div class="hero">Which SKUs <em>first?</em></div>
    <div class="list">
      <div class="li top"><span class="num">1</span><b>Highest-volume China→EU bands</b></div>
      <div class="li"><span class="num">2</span><span>Thin-margin $10–$35 price points</span></div>
      <div class="li"><span class="num">3</span><span>Lanes with no localization fallback</span></div>
    </div>
    <span class="cta">Get the report →</span>
  </div>
  <div class="foot"><span class="url">Ghostresearch.com</span><span class="cred">The model ranks where margin breaks hardest</span></div>
</div>
</body></html>
```

---

## Concept 12 — Market vs Your Catalogue (Template D split — Elite cross-sell)

**Tool:** editorial
**Style preset:** Template D — split (retargeting + Ghost Elite cross-sell)
**Aspect:** 1:1
**Suggested filename:** `concept-12-market-vs-catalogue.png`
**Maps to:** Visual C12 · Days 11–14 (Week 2 — retargeting + Elite cross-sell)

### Generation prompt
```html
<!doctype html><html><head><meta charset="utf-8"/>
<link href="https://fonts.googleapis.com/css2?family=Oranienbaum&family=Manrope:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<style>
*{box-sizing:border-box;margin:0;padding:0}
:root{--ink:#F8F8FF;--red:#EF4444;--blob-stroke:rgba(248,248,255,.12)}
body{width:100%;height:100vh;font-family:'Manrope',sans-serif;color:var(--ink);position:relative;overflow:hidden;background:linear-gradient(135deg,#181650 0%,#06062D 100%)}
.frame{position:absolute;inset:18px;border:2px solid var(--red);border-radius:28px;z-index:3;pointer-events:none}
.blob-ring{position:absolute;z-index:0;bottom:-14%;right:-8%;width:46%;aspect-ratio:1;border-radius:50%;border:1.5px solid var(--blob-stroke)}
.wrap{position:relative;z-index:1;height:100%;padding:8.5%;display:flex;flex-direction:column;justify-content:space-between}
.top{display:flex;justify-content:space-between;align-items:flex-start}
.gh-logo{width:clamp(72px,8.5vh,100px);height:clamp(72px,8.5vh,100px)}.gh-logo svg{width:100%;height:100%;display:block}
.eyebrow{font-size:clamp(17px,2vh,20px);font-weight:700;letter-spacing:.13em;text-transform:uppercase;text-align:right;color:var(--red);max-width:18ch;line-height:1.4}
.btm{display:flex;flex-direction:column;gap:2.6vh}
.h1{font-family:'Oranienbaum',serif;font-size:clamp(50px,6.6vh,82px);line-height:1.03;max-width:20ch}
.h1 em{font-style:italic;color:var(--red)}
.split{display:flex;gap:20px}
.pane{flex:1;padding:24px;border:1px solid rgba(248,248,255,.18);border-radius:14px}
.pane.right{border:1px solid var(--red);background:rgba(239,68,68,.08)}
.ph{font-size:clamp(16px,1.8vh,19px);text-transform:uppercase;letter-spacing:.1em;color:rgba(248,248,255,.6);font-weight:700}
.pane.right .ph{color:var(--red)}
.pt{font-family:'Oranienbaum',serif;font-size:clamp(28px,3.3vh,40px);margin-top:8px;line-height:1.08}
.pd{font-size:clamp(19px,2.1vh,23px);color:rgba(248,248,255,.78);margin-top:10px;line-height:1.4}
.tag{display:inline-block;margin-top:12px;background:var(--red);color:#fff;font-size:clamp(15px,1.7vh,18px);font-weight:700;padding:7px 13px;border-radius:6px;letter-spacing:.04em}
.cta{display:inline-flex;align-items:center;gap:10px;background:var(--red);color:#fff;padding:15px 26px;border-radius:8px;font-weight:700;font-size:clamp(21px,2.3vh,25px);width:fit-content}
.foot{display:flex;justify-content:space-between;align-items:flex-end;gap:18px}
.url{font-size:clamp(19px,2.1vh,23px);font-weight:600}
.cred{font-size:clamp(19px,2vh,21px);color:rgba(248,248,255,.62);text-align:right}
</style></head>
<body>
<div class="frame"></div><div class="blob-ring"></div>
<div class="wrap">
  <div class="top">
    <div class="gh-logo" aria-label="Ghost Research"><svg viewBox="0 0 100 100"><rect width="100" height="100" rx="22" fill="#EF4444"/><circle cx="50" cy="50" r="19" fill="#fff"/></svg></div>
    <div class="eyebrow">For those who saw it<br>but didn't buy</div>
  </div>
  <div class="btm">
    <h1 class="h1">You saw the deadline. Here's the part you <em>didn't.</em></h1>
    <div class="split">
      <div class="pane">
        <div class="ph">The report</div>
        <div class="pt">Models the market</div>
        <div class="pd">Landed cost by band and by lane, across the cross-border market.</div>
      </div>
      <div class="pane right">
        <div class="ph">Ghost Elite</div>
        <div class="pt">Models your catalogue</div>
        <div class="pd">Your SKUs, your lanes — a bespoke landed-cost model.</div>
        <span class="tag">24-HR CUSTOM MANDATE</span>
      </div>
    </div>
    <span class="cta">Commission a custom mandate →</span>
    <div class="foot"><span class="url">Ghostresearch.com</span><span class="cred">1M+ curated sources · expert-vetted</span></div>
  </div>
</div>
</body></html>
```

---

## Asset count
3 photo bases (reused) + 12 editorial cards = **15 production files**, all stills, mapping to all 14 calendar days. No videos (paused 2026-05-23).
