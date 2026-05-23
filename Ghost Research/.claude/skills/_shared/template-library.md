# Ghost Research — Approved Template Library

This is the **canonical visual-template spec**, derived directly from Shreyanshi's
file-by-file review of the `ai-energy-demand-2026` deck (2026-05-23). `/design-ads`
and `/write-prompts` MUST read this and build every editorial concept from one of the
named templates below. These templates are *what good looks like*. The anti-patterns at
the bottom are campaign-killers — never ship them.

> This library refines (does not replace) the brand bible, `style-presets.md`, and the
> hard-rules memory. Where this file is more specific, this file wins.

---

## 0. The shared chassis — every template inherits this

Every editorial card (dark or light) is built on the same skeleton:

1. **Thin red rounded-frame border.** A `2px solid #EF4444` border, `border-radius: 26–30px`, inset ~18px from all four canvas edges (`position:absolute; inset:18px`). This is a Ghost signature — it appears on the loved photo templates (real-stat, FINAL-dark2, T5, house-darkx). Optional on pure-paper light cards, mandatory on photo cards.
2. **Icon mark, top-left.** The standalone red rounded-square + white-circle SVG, 88–104px. **Optionally** followed by `GHOST RESEARCH` in letterspaced Manrope/Oranienbaum caps as a *separate* element (the loved "journal" masthead).
   - 🚫 **NEVER the "GH⬛ST RESEARCH" lockup** where the icon replaces the letter O. It renders small, low-contrast, and tacky. Every disliked card used it (C06, C08, C11, launch-econ, C03). Banned.
3. **Top-right eyebrow.** Publication line + drop date, e.g. `THE AI ENERGY DEMAND ATLAS` / `DROPS JUNE 1, 2026` — uppercase, letterspaced, the date (or "AVAILABLE NOW") in red. Week 1 uses the date; Week 2 uses `AVAILABLE NOW`.
4. **One bottom-anchored content column** (see §0.1 — the alignment law).
5. **Footer row.** `Ghostresearch.com` bottom-left + optional credibility line bottom-right (`EXPERT-VETTED · FULLY CITED` or `1M+ curated sources · transparent citation · expert-vetted`).
6. **A red CTA button — on every template, no exceptions** (even the journal cover). `#EF4444` fill, white Manrope semibold, trailing ` →`.
7. **Blob structures behind the content** (see §0.2).

### 0.1 — THE ALIGNMENT LAW (Shreyanshi's most-repeated note)

> "text placement could be better", "align the text properly such that there is no weird space", "work on text alignment" — flagged on T2, T4, T5, T6, T7, FINAL-dark2.

- **Headline + stat + sub live in ONE left-aligned column, anchored to the lower portion** of the frame. Do **NOT** split headline-to-top and sub-to-bottom with a dead gap in the middle (that gap is the "weird space" — it's why T2-dossier underwhelmed).
- Vertical rhythm inside the column is uniform: `eyebrow → (gap) → headline → (gap) → big stat → (gap) → sub → (gap) → CTA`. Use one consistent gap unit (e.g. `margin-top: 2.4vh`) between every element. No ad-hoc spacing.
- The big serif stat sits *inside* this column, between the small headline line and the sub — not floating elsewhere.
- Left edge of every text element aligns to the same vertical line (the column's left margin, ~6.5% inset or aligned to a left red rule).

### 0.2 — BLOB STRUCTURES (requested repeatedly, esp. light themes)

> "add some blob structures at the end" (c9), "just add blob structure, rest is completely fine" (redo-launch-light), "whenever you are creating these light templates: add blob structures behind and keep them consistent" (t8).

- **Every light-theme card gets blobs.** Dark cards may use them subtly.
- Blobs are **faint, organic background shapes** behind the content (`z-index:0`, content `z-index:1`). Two consistent types:
  - **Outline circle:** a large thin-stroke circle/ellipse partly off-canvas (top-right is the house position). `border:1.5px solid rgba(239,68,68,.22)` on light, `rgba(248,248,255,.14)` on dark.
  - **Soft fill blob:** a blurred radial-gradient ellipse in a corner, very low opacity (`radial-gradient(circle, rgba(239,68,68,.10), transparent 70%)`, `filter: blur(10px)`).
- **Keep them consistent across a campaign** — same blob positions/sizes on every card in the set, so the deck reads as a system.
- Standard CSS block (paste into any card, light or dark):
  ```css
  .blob{position:absolute;z-index:0;pointer-events:none}
  .blob-ring{top:-12%;right:-8%;width:46%;aspect-ratio:1;border-radius:50%;border:1.5px solid var(--blob-stroke)}
  .blob-soft{bottom:-10%;left:-6%;width:40%;aspect-ratio:1;border-radius:50%;
    background:radial-gradient(circle,var(--blob-fill),transparent 70%);filter:blur(8px)}
  /* dark: --blob-stroke:rgba(248,248,255,.14); --blob-fill:rgba(239,68,68,.10);
     light: --blob-stroke:rgba(239,68,68,.22); --blob-fill:rgba(239,68,68,.08); */
  ```
  Wrap all real content in a `<div style="position:relative;z-index:1; ...">`.

### 0.3 — FOOTER FONT SIZES (corrected per review)

- `Ghostresearch.com` URL: **smaller than before** — `clamp(19px, 2.1vh, 23px)`, Manrope medium. (Notes on FINAL-light1 and FINAL-light2: "ghostresearch.com cld be a lil font less.") It must not compete with the headline.
- Credibility line ("1M+ curated sources · …"): **slightly larger / more legible** — `clamp(19px, 2.1vh, 22px)`, never below 19px. (Note on c5: "1M+ curated sources line — we can increase font size a little so the user can easily read it.")
- The two footer items are visually balanced; neither dominates.

### 0.4 — TYPE & COLOR (unchanged brand locks, restated)

- Oranienbaum (serif) for headlines + the big hero stat; Manrope for everything else.
- The **hero number/stat is red `#EF4444` Oranienbaum**, oversized. Key words in the sub are red-highlighted inline (e.g. `9 utilities`, `$147 billion`).
- Two neutrals + one accent only. Dark: `#181650 → #06062D`. Light: `#F1F3FF` / `#F8F8FF`, ink `#0B0B14`/`#06062D`.
- Legibility floors: headline ≥56px, big stat ≥120px, sub ≥22px, eyebrow ≥18px, CTA ≥22px, URL ≥19px, credibility ≥19px (1080 canvas).

---

## 1. The named templates (build every concept from one of these)

### TEMPLATE A — "Dark Photo Hero" ⭐ (real-stat / FINAL-dark2 / T5 / T6)
**Loved.** The flagship. Full-bleed topic photo, thin red frame, icon top-left, eyebrow top-right, then the bottom-anchored column: small headline line → huge red Oranienbaum stat → sub with red keywords → footer + CTA. A dark gradient scrim sits over the lower photo so text stays legible.
- Use for: hero scenes, stat reveals, authority/citation moments.
- Photo: a real topic-specific scene/object (transmission tower, datacenter, documents+loupe). **Never an AI human face.** Color-graded deep indigo.
- The stat (`$147B`, `31 GW`, `18–22%`) is the single hero element.

### TEMPLATE B — "Journal Cover" ⭐ (T1-journal-cover)
**Absolutely loved.** Magazine-cover authority. Top masthead = icon + `GHOST RESEARCH` caps on the left, publication + drop-date on the right, a full-width hairline rule beneath. Dark gradient photo body. Bottom: red eyebrow → big Oranienbaum headline with red stat → hairline rule → **red-bullet list (3 items, red-highlighted keywords)** → footer (`Ghostresearch.com` + `EXPERT-VETTED · FULLY CITED`).
- **FIX vs original: T1 had no CTA. ALWAYS add the red CTA button** (place it bottom-right in the footer row).
- Use for: launch announcements, Day-8 "it's live", the campaign hero post.

### TEMPLATE C — "Pull-Quote" ⭐ (T8-pullquote)
**Loved.** A single oversized Oranienbaum pull-quote, opened by a big red quotation mark, key figure in red, then a red em-dash + attribution line, footer + CTA. Light or dark.
- **On light: add blobs behind (per §0.2).**
- Use for: the thesis line, a contrarian claim, an expert quote (Week 2).

### TEMPLATE D — "Light Stat Card" ⭐ (FINAL-light2 / V3-C-framed)
**Loved ("perfect template").** Cream/lavender bg, **vertical red rule on the left margin**, red eyebrow → bold **Manrope** headline (black) → huge red **Oranienbaum** stat → sub → footer + CTA. Blobs behind (mandatory on light).
- Optional **framed image on the right** (rounded-rect, thin red edge) — the V3-C variant. If a person is shown it MUST be a **real licensed stock photo (e.g. Pexels), never FLUX/AI-generated**. Prefer a topic object/scene if no licensed portrait is available.
- **FIX vs original: make the framed/right image LARGER** — FINAL-light2's cooling-towers image was too small. The framed image should occupy a confident ~38–42% of width.
- Use for: the 1–2 mandatory light-theme cards per campaign, Week-2 stat reveals, premium/Elite angles.

### TEMPLATE E — "Carousel Slide" ⭐ (REDO-house-darkx is the reference)
**Good for carousels.** Dark navy, thin red frame, icon top-left, a small circular `→` button top-right, big Oranienbaum headline, a consistent supporting graphic (chart/number), `Ghostresearch.com` bottom-left, and a page indicator bottom-right (`/// ` slashes or `1 / 3 · SWIPE →`).
- 🔒 **CAROUSEL CONSISTENCY LAW:** every slide in a carousel shares the **identical chassis** — same background treatment, same masthead, same type scale, same frame, same footer/indicator position. **Do NOT change the panel/background color between slides** (the C03 set failed because slide 1 was navy and slide 2 was solid red). One coherent system across all slides.
- Slide roles: S1 cover (headline) → S2–S4 one idea each (same layout, different content) → final slide CTA.

### TEMPLATE F — "Light Banner / Announcement" (redo-launch-light)
**Liked ("rest is completely fine, just add blob").** Light landing-style banner: left headline column + right negative space, red CTA, blobs behind. Essentially Template D without the framed image. Always blobs.

---

## 2. Anti-patterns — NEVER ship these (campaign-killers)

| ✗ Banned | Why | Seen in (disliked) |
|---|---|---|
| **AI-generated human faces** | Uncanny = instant trust-kill for a research brand. For humans use real licensed stock only. | C11, C03a/b |
| **"GH⬛ST RESEARCH" icon-as-letter-O wordmark** | Small, low-contrast, tacky. Use standalone icon, or icon + clean caps. | C06, C08, C11, launch-econ, C03 |
| **Rigid 50/50 photo-top / text-bottom split** | Looks like a template, not a brand. Use full-bleed photo + bottom-anchored text + frame instead. | C06, C11 |
| **Full-width solid orange/red banner strip** | Tacky. Use a thin rule or red text, never a fat color bar across the layout. | C08 |
| **Crude redaction-bar "ledger" with dead space** | Wireframe-y, sterile, half-empty. If redaction is the motif, do it inside a photo (T5), not as black bars on white. | T9 ("never make this") |
| **Busy SaaS dashboard** (KPI tiles + lock icons + many progress bars) | Cluttered, generic SaaS, off-brand. One hero metric, not a dashboard. | T3, launch-econ |
| **Headline-top / sub-bottom with a big mid gap** | The "weird space." Keep headline+stat+sub in one bottom column. | T2 |
| **Carousel slides that change background color slide-to-slide** | Breaks the system. One chassis across all slides. | C03a→C03b |
| **`Ghostresearch.com` set too large** | Competes with the headline. Keep URL ≤23px. | FINAL-light1/2 |
| **VIDEOS (for now)** | Paused by user 2026-05-23. Default to image-only — no animate / animated-html / veo unless explicitly asked. | C04, T10, V2 |

---

## 3. Quick decision guide

| Need | Template |
|---|---|
| Hero scene + a big stat | A — Dark Photo Hero |
| Launch / "it's live" / cover post | B — Journal Cover (with CTA) |
| Thesis line / contrarian claim / quote | C — Pull-Quote |
| Mandatory light card / premium / Elite | D — Light Stat Card (blobs; bigger framed image) |
| LinkedIn document / multi-slide | E — Carousel (one chassis across slides) |
| Light announcement banner | F — Light Banner (blobs) |

**Per campaign:** ship the dark-photo-hero + journal-cover as anchors, 1–2 light cards (D/F, always blobs), pull-quote for the thesis, and a consistent carousel for LinkedIn. **No videos** unless the user asks.
