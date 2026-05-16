#!/usr/bin/env python3
"""One-off emitter: writes 14-day prompts.md for supply-chain-ai-forecast (run from repo root)."""
from __future__ import annotations

from pathlib import Path

OUT = Path(__file__).resolve().parents[1] / "data" / "proposals" / "supply-chain-ai-forecast" / "prompts.md"

FONT = (
    '<link href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;600;700&family=Oranienbaum&display=swap" rel="stylesheet">'
)


def composite_9x16(bg: str, eyebrow: str, title: str, sub: str, cta: str) -> str:
    return f"""<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8"/>{FONT}
<style>
*{{box-sizing:border-box;margin:0;padding:0}}
body{{width:1080px;height:1920px;position:relative;font-family:Manrope,sans-serif;color:#F8F8FF;background:#06062D}}
.bg{{position:absolute;inset:0;background-image:linear-gradient(180deg,rgba(6,6,45,0.08)0%,rgba(6,6,45,0.55)45%,rgba(6,6,45,0.97)100%),url("GHOST_ASSET:{bg}");background-size:cover;background-position:center}}
.content{{position:relative;z-index:1;padding:56px 48px;height:100%;display:flex;flex-direction:column;justify-content:flex-end}}
.eyebrow{{font-size:26px;letter-spacing:0.22em;text-transform:uppercase;opacity:0.92;margin-bottom:20px;font-weight:600}}
h1{{font-family:Oranienbaum,serif;font-size:78px;line-height:1.04;max-width:980px;text-shadow:0 4px 28px rgba(0,0,0,0.55)}}
.sub{{font-size:34px;margin-top:20px;opacity:0.95;max-width:960px;line-height:1.38;text-shadow:0 2px 18px rgba(0,0,0,0.45)}}
.cta{{margin-top:40px;align-self:flex-start;background:#EF4444;color:#fff;font-weight:700;font-size:30px;padding:22px 40px;border-radius:8px;box-shadow:0 10px 40px rgba(0,0,0,0.35)}}
</style></head><body><div class="bg"></div><div class="content">
<div class="eyebrow">{eyebrow}</div><h1>{title}</h1><p class="sub">{sub}</p><div class="cta">{cta}</div>
</div></body></html>"""


def composite_1x1(bg: str, eyebrow: str, title: str, sub: str, cta: str) -> str:
    return f"""<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8"/>{FONT}
<style>
*{{box-sizing:border-box;margin:0;padding:0}}
body{{width:1080px;height:1080px;position:relative;font-family:Manrope,sans-serif;color:#F8F8FF;background:#06062D}}
.bg{{position:absolute;inset:0;background-image:linear-gradient(135deg,rgba(24,22,80,0.55)0%,rgba(6,6,45,0.94)100%),url("GHOST_ASSET:{bg}");background-size:cover;background-position:center}}
.content{{position:relative;z-index:1;padding:52px;height:100%;display:flex;flex-direction:column;justify-content:center}}
.eyebrow{{font-size:22px;letter-spacing:0.2em;text-transform:uppercase;opacity:0.9;margin-bottom:16px;font-weight:600}}
h1{{font-family:Oranienbaum,serif;font-size:56px;line-height:1.06;max-width:980px;text-shadow:0 3px 22px rgba(0,0,0,0.5)}}
.sub{{font-size:28px;margin-top:14px;opacity:0.94;max-width:940px;line-height:1.36;text-shadow:0 2px 14px rgba(0,0,0,0.45)}}
.cta{{margin-top:26px;align-self:flex-start;background:#EF4444;color:#fff;font-weight:700;font-size:24px;padding:18px 32px;border-radius:8px;box-shadow:0 8px 32px rgba(0,0,0,0.35)}}
</style></head><body><div class="bg"></div><div class="content">
<div class="eyebrow">{eyebrow}</div><h1>{title}</h1><p class="sub">{sub}</p><div class="cta">{cta}</div>
</div></body></html>"""


def kinetic_mp4(bg: str, headline: str, accent: str, cta: str, done_ms: int = 8200) -> str:
    return f"""<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8"/>{FONT}
<style>
*{{box-sizing:border-box;margin:0;padding:0}}
body{{width:1080px;height:1920px;font-family:Manrope,sans-serif;overflow:hidden;
  background-image:linear-gradient(180deg,rgba(6,6,45,0.42)0%,rgba(6,6,45,0.93)100%),url("GHOST_ASSET:{bg}");
  background-size:cover;background-position:center;color:#F8F8FF;
  display:flex;flex-direction:column;justify-content:center;padding:64px}}
h1{{font-family:Oranienbaum,serif;font-size:76px;line-height:1.05;max-width:980px;opacity:0;animation:rise 1.05s ease-out 0.3s forwards;text-shadow:0 4px 26px rgba(0,0,0,0.55)}}
.accent{{display:block;margin-top:22px;font-size:44px;color:#EF4444;font-weight:600;opacity:0;animation:rise 0.95s ease-out 1.2s forwards;text-shadow:0 2px 18px rgba(0,0,0,0.45)}}
.cta{{margin-top:32px;font-size:32px;font-weight:700;opacity:0;animation:rise 0.9s ease-out 2s forwards}}
.bar{{margin-top:36px;height:6px;width:0;background:#EF4444;animation:grow 0.85s ease-out 2.55s forwards}}
@keyframes rise{{from{{transform:translateY(24px);opacity:0}}to{{transform:translateY(0);opacity:1}}}}
@keyframes grow{{from{{width:0}}to{{width:440px}}}}
</style>
<script>window.addEventListener("load",()=>{{setTimeout(()=>{{window.__GHOST_DONE=true}}, {done_ms});}});</script>
</head><body>
<h1>{headline}</h1><span class="accent">{accent}</span><div class="cta">{cta}</div><div class="bar"></div>
</body></html>"""


def main() -> None:
    blocks: list[str] = [
        """---
slug: supply-chain-ai-forecast
created: 2026-05-16
brief: campaign-brief.md
concepts: visual-concepts.md
status: ready-to-generate
total_prompts: 14
calendar: "14 days - Week 1 hype (Days 1-7), Week 2 sales (Days 8-14)"
---

# Generation prompts — Supply chain AI forecast accuracy (14-day flight)

**How ads are built now**

1. **Photo bases** (`pollinations`) = scene only (no burned-in ad copy — safer for image models).
2. **Ad-ready frames** (`editorial`) = HTML compositing photo + **headline + sub + CTA** via `GHOST_ASSET:filename.jpg` tokens (resolved at render time).
3. **Motion** (`animate`) = Ken-Burns on a **composite PNG** so typography rides with the shot.
4. **Kinetic** (`animated-html`) = full-screen **photo + animated type** (not flat color only).

Optional: polish in **[Pomelli](https://labs.google.com/pomelli/)** (no API) — export into `pomelli-inbox/` as `concept-01.png` / `01.jpg`, then `python scripts/import_pomelli_exports.py --slug <slug> --overwrite` (or `--import-pomelli-inbox` on `generate_proposal_assets.py`).

Run: `python scripts/run_full_delivery.py --slug supply-chain-ai-forecast --overwrite`

""",
    ]

    # 01 photo base
    blocks.append(
        """## Concept 01 — W1 D1 photo base (no type — used under composites)

**Tool:** pollinations
**Aspect:** 9:16
**Suggested filename:** `concept-01-w1d1-base-hero.jpg`
**Maps to:** Day 1, Week 1 (hype)

### Generation prompt
```
Editorial photograph, logistics control room at blue hour, senior operator in silhouette reviewing wall of abstract network maps and heat tiles on monitors, faces not visible to camera, deep indigo (#181650) and navy (#06062D) color grade, single small accent of red (#EF4444) on one UI bezel only, Bloomberg documentary lighting, photoreal, Arri Alexa Mini 50mm, shallow depth of field, generous lower third negative space for post. No readable screen text, no logos, no watermarks, no robots, no sci-fi HUD.

NEGATIVE: no robots, no AI clichés, no glowing nodes, no neon, no uncanny faces, no text in image, no logos, no watermarks.
```
"""
    )

    # 02 composite
    blocks.append(
        f"""## Concept 02 — W1 D2 hero ad (photo + on-frame type)

**Tool:** editorial
**Aspect:** 9:16
**Suggested filename:** `concept-02-w1d2-hero-ad-composite.png`
**Maps to:** Day 2, Week 1 (hype)

### Generation prompt
```
{composite_9x16(
    "concept-01-w1d1-base-hero.jpg",
    "Coming soon",
    "Your forecast stack still reads last quarter.",
    "Curated, expert-vetted synthesis for operators who cannot ship another lagging dashboard to the board.",
    "Save the date",
)}
```
"""
    )

    # 03 type on blurred same photo
    blocks.append(
        f"""## Concept 03 — W1 D3 LinkedIn square (image + type)

**Tool:** editorial
**Aspect:** 1:1
**Suggested filename:** `concept-03-w1d3-li-square.png`
**Maps to:** Day 3, Week 1 (hype)

### Generation prompt
```
{composite_1x1(
    "concept-01-w1d1-base-hero.jpg",
    "Ghost Research",
    "Demand signals are moving faster than ERP exports.",
    "Transparent citation. Human SME review. Built for mission-critical calls.",
    "Join the waitlist",
)}
```
"""
    )

    # 04 second photo
    blocks.append(
        """## Concept 04 — W1 D4 photo grid scene

**Tool:** pollinations
**Aspect:** 4:5
**Suggested filename:** `concept-04-w1d4-analyst-grid.jpg`
**Maps to:** Day 4, Week 1 (hype)

### Generation prompt
```
Overhead editorial photograph of a war-room table covered with printed heatmaps and tablet devices showing abstract logistics curves, hands visible only from wrists down adjusting markers, deep indigo color grade, cool fill, premium consulting firm aesthetic, sharp micro-contrast, photoreal, 50mm lens look, no readable text on paper or screens, no logos, no watermarks.

NEGATIVE: no robots, no sci-fi UI, no uncanny faces, no text in image, no logos, no watermarks.
```
"""
    )

    # 05 composite 4:5
    c5 = composite_1x1(
        "concept-04-w1d4-analyst-grid.jpg",
        "Research note",
        "Pattern detection across vetted trade, filings, and enterprise telemetry.",
        "Stop pretending CSV refreshes are strategy.",
        "Notify me",
    ).replace("1080px;height:1080px", "1080px;height:1350px")
    blocks.append(
        f"""## Concept 05 — W1 D5 Meta feed (photo + type)

**Tool:** editorial
**Aspect:** 4:5
**Suggested filename:** `concept-05-w1d5-meta-composite.png`
**Maps to:** Day 5, Week 1 (hype)

### Generation prompt
```
{c5}
```
"""
    )

    # 06 motion: base photo + burned-in copy (matches Concept 02 on-frame text)
    blocks.append(
        """## Concept 06 — W1 D6 motion (photo + on-screen copy)

**Tool:** animate
**Aspect:** 9:16
**Suggested filename:** `concept-06-w1d6-hero-motion.mp4`
**Maps to:** Day 6, Week 1 (hype)
**Source image:** `concept-01-w1d1-base-hero.jpg`
**Motion:** zoom-in
**Duration:** 8
**On-screen headline:** Your forecast stack still reads last quarter.
**On-screen sub:** Curated, expert-vetted synthesis for operators who cannot ship another lagging dashboard to the board.
**On-screen CTA:** Save the date

### Generation prompt
```
Ken-Burns zoom on the Day 1 hero photo with the exact headline, subcopy, and CTA from the Day 2 static ad burned in as legible lower-third typography (Oranienbaum + Manrope, Ghost red CTA). 8 seconds, subtle fades.
```
"""
    )

    # 07 kinetic with bg
    blocks.append(
        f"""## Concept 07 — W1 D7 kinetic (photo + animated type)

**Tool:** animated-html
**Aspect:** 9:16
**Suggested filename:** `concept-07-w1d7-kinetic-hype.mp4`
**Maps to:** Day 7, Week 1 (hype)
**Duration:** 8

### Generation prompt
```
{kinetic_mp4(
    "concept-01-w1d1-base-hero.jpg",
    "The report drops soon.",
    "Expert-vetted supply chain AI forecast accuracy.",
    "Join the waitlist",
    8200,
)}
```
"""
    )

    # 08 W2 pure editorial stat (could add tiny bg via same pattern - use composite with 01)
    blocks.append(
        f"""## Concept 08 — W2 D8 sales proof card

**Tool:** editorial
**Aspect:** 1:1
**Suggested filename:** `concept-08-w2d8-proof-card.png`
**Maps to:** Day 8, Week 2 (sales - publish day framing)

### Generation prompt
```
{composite_1x1(
    "concept-01-w1d1-base-hero.jpg",
    "Now live",
    "1M+ curated sources. Every claim cited.",
    "Download the institutional-grade brief your competitors will wish they bought first.",
    "See pricing",
)}
```
"""
    )

    # 09 sale hero
    blocks.append(
        f"""## Concept 09 — W2 D9 Reels hero (photo + price + CTA)

**Tool:** editorial
**Aspect:** 9:16
**Suggested filename:** `concept-09-w2d9-reels-sale.png`
**Maps to:** Day 9, Week 2 (sales)

### Generation prompt
```
{composite_9x16(
    "concept-01-w1d1-base-hero.jpg",
    "Available now",
    "Supply Chain AI Forecast Accuracy - boardroom edition.",
    "Self-serve report benchmarked near $500. SME-reviewed before it hits your inbox.",
    "Buy now",
)}
```
"""
    )

    # 10 photo evidence
    blocks.append(
        """## Concept 10 — W2 D10 evidence still

**Tool:** pollinations
**Aspect:** 16:9
**Suggested filename:** `concept-10-w2d10-evidence-wide.jpg`
**Maps to:** Day 10, Week 2 (sales)

### Generation prompt
```
Editorial photograph of two executives reviewing a printed sensitivity chart on a conference table, shallow depth of field, indigo color grade, warm skin tones, cinematic office windows, photoreal, no readable text on documents, no logos, no watermarks, premium B2B research aesthetic.

NEGATIVE: no robots, no uncanny faces, no text in image, no logos, no watermarks.
```
"""
    )

    # 11 bundle composite
    blocks.append(
        f"""## Concept 11 — W2 D11 LinkedIn carousel lead (photo + type)

**Tool:** editorial
**Aspect:** 4:5
**Suggested filename:** `concept-11-w2d11-li-bundle.png`
**Maps to:** Day 11, Week 2 (sales)

### Generation prompt
```
{composite_1x1(
    "concept-10-w2d10-evidence-wide.jpg",
    "Bundle-ready",
    "Pair the forecast brief with your diligence stack this week.",
    "Transparent methodology section + expert commentary included.",
    "Get the report",
).replace("1080px;height:1080px", "1080px;height:1350px")}
```
"""
    )

    # 12 motion: base photo + same copy as Day 9 Reels static
    blocks.append(
        """## Concept 12 — W2 D12 motion (photo + on-screen offer)

**Tool:** animate
**Aspect:** 9:16
**Suggested filename:** `concept-12-w2d12-sale-motion.mp4`
**Maps to:** Day 12, Week 2 (sales)
**Source image:** `concept-01-w1d1-base-hero.jpg`
**Motion:** pan-right
**Duration:** 8
**On-screen headline:** Supply Chain AI Forecast Accuracy - boardroom edition.
**On-screen sub:** Self-serve report benchmarked near $500. SME-reviewed before it hits your inbox.
**On-screen CTA:** Buy now

### Generation prompt
```
Pan across the hero photo with the Day 9 offer headline, supporting line, and red CTA pinned to the safe zone. 8 seconds, gentle fade in/out.
```
"""
    )

    # 13 kinetic sales
    blocks.append(
        f"""## Concept 13 — W2 D13 kinetic (photo + type + CTA)

**Tool:** animated-html
**Aspect:** 9:16
**Suggested filename:** `concept-13-w2d13-kinetic-offer.mp4`
**Maps to:** Day 13, Week 2 (sales)
**Duration:** 8

### Generation prompt
```
{kinetic_mp4(
    "concept-04-w1d4-analyst-grid.jpg",
    "Stop guessing next quarter's exposure.",
    "Expert-vetted forecast pack with transparent citations.",
    "Download tonight",
    8200,
)}
```
"""
    )

    # 14 finale
    blocks.append(
        f"""## Concept 14 — W2 D14 finale frame

**Tool:** editorial
**Aspect:** 9:16
**Suggested filename:** `concept-14-w2d14-finale.png`
**Maps to:** Day 14, Week 2 (sales)

### Generation prompt
```
{composite_9x16(
    "concept-10-w2d10-evidence-wide.jpg",
    "Ghost Research",
    "Institutional-grade supply chain intelligence.",
    "Expert-vetted synthesis with transparent citations. Built for board-ready decisions.",
    "Buy the report",
)}
```
"""
    )

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text("\n".join(blocks), encoding="utf-8")
    print(f"Wrote {OUT}")


if __name__ == "__main__":
    main()
