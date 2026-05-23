# Ghost Research — Style Preset Library

A shared menu of named visual styles that `/design-ads` and `/write-prompts` read.
A preset is **not** a new tool or model — it's a visual-treatment recipe that the
existing generators (Pollinations FLUX, editorial HTML, animate, animated-html)
render. Pick a preset per concept; the campaign can mix several.

**How to invoke:** the user names one or more presets in plain English —
"design the ads in a luxury style", "/design-ads cinematic + suspense",
"make me UI-heavy SaaS creatives", "I need landing-page banners". If the user
names none, `/design-ads` chooses per concept from this library to fit the hook.

---

## 0. Global locks — every preset inherits these, no exceptions

> **Build from the Template Library.** Before applying any preset, read
> `_shared/template-library.md` — it defines the six approved layouts (A–F) from
> Shreyanshi's file-by-file review and is the authority on alignment, blobs, footer
> sizes, the masthead lockup, and the campaign-killer anti-patterns. Presets set the
> *mood*; the template sets the *bones*.

These come from the brand bible and the hard-rules memory. A preset may change the
*mood*, *layout*, and *texture* — it may **never** break any of these:

1. **Icon mark on every image / video / VFX frame.** `Ghost Research/assets/brand/logo-mark.svg` (red `#EF4444` rounded-square + white inset circle), top-left, 88–112px on a 1080-wide canvas. No text wordmark substitute.
2. **Two neutrals + one accent only.** Accent `#EF4444`. Dark: `#181650 → #06062D`. Light: `#F8F8FF` / `#F1F3FF`, ink `#06062D`. No tonal middles, no extra colors.
3. **Type: Oranienbaum (serif headlines) + Manrope (body/UI) only.**
4. **No price in any ad copy** — no "$500", no "from $X". The *only* exception is the **Landing-page banner** preset, where price may appear because the landing page is where price reveals.
5. **Voice stays institutional** — precise, authoritative, evidence-based. Never "game-changing / revolutionary / disrupt / unlock / supercharge", never SaaS-hack tone. This holds even for the Startup and SaaS presets (those change the *look*, not the *voice*).
6. **No robots, no AI clichés** — no brain circuits, glowing nodes, holograms, neon, cyberpunk, sci-fi UI, no AI-generated faces, no uncanny humans.
7. **One hero element per frame · ≥70% negative space · info-gap headline** (named villain / contrarian / hidden cost / time-decay / specificity / insider POV).
8. **Report-specific (swap test).** Subject + props must reference something only the actual report buyer would recognize. If the concept still fits any other Ghost report, it's too generic — rewrite before shipping.
9. **9:16 video ≥15s · 6.5% uniform padding · legibility floors** (headline ≥56pt, sub ≥22pt, eyebrow ≥18pt, CTA ≥22pt on a 1080 canvas).
10. **Week-1 / Week-2 law.** Week 1 = hype only, the report is unpublished — never quote, chart, or visually preview report content. Week 2 = report content allowed. Each preset notes its natural week.
11. **Image-only by default — videos are paused (2026-05-23).** No `animate` / `animated-html` / `veo` unless the user explicitly asks for video this run.
12. **Banned layouts (template-library §2 — campaign-killers):** AI-generated human faces (use real licensed stock only); the "GH⬛ST RESEARCH" icon-as-letter-O wordmark (use standalone icon, or icon + clean caps); full-width solid orange/red banner strips; crude redaction-bar ledgers with dead space; busy SaaS dashboards with KPI tiles + lock icons; rigid 50/50 photo-top/text-bottom splits.
13. **Alignment + blobs + CTA:** headline + stat + sub in ONE bottom-anchored column (no mid "weird space"); blob structures behind every light card (consistent across the campaign); a red CTA on every card; `Ghostresearch.com` ≤23px, credibility line ≥19px.

---

## 1. Aesthetic presets

Each defines mood + layout + texture. Combine with a Placement preset (§2) to lock format.

### LUXURY
- **Use when:** high-WTP buyers (PE/IB/C-suite), prestige positioning, Ghost Elite mandates.
- **Maps to lane:** `cinematic-ink`. **Route:** `pollinations` (material/object scene, no people-as-hero) → `editorial` composite for type. **Default aspect:** 1:1 or 4:5.
- **Visual treatment:** premium materials as subject — marble, brushed metal, dark walnut, leather, heavy paper stock — lit like a watch or spirits ad. Single soft red specular highlight. Macro texture, shallow DoF, deep indigo grade. Generous void. No faces.
- **Copy register:** minimal word count, declarative, confident restraint. Let the negative space carry the prestige.
- **Flexes:** richer material texture than the usual flat editorial bg. **Locks:** palette, type, no-faces-in-hero, info-gap headline.
- **Week:** either. Week 1 = the question rendered in luxury; Week 2 = a single headline finding.
- **RavenMCP consult:** `visual trends & branding` (2026 premium/luxury cues), `design principles` (color theory, restraint, contrast), `brand voice` (premium register).

### STARTUP
- **Use when:** founder-POV angle (Joy Sharma), momentum/energy, "the new institution" framing.
- **Maps to lane:** `cinematic-ink` or `editorial-paper`. **Route:** `editorial` or `animated-html`. **Default aspect:** 1:1 / 9:16.
- **Visual treatment:** bold oversized serif claim, high contrast, confident single red accent, clean fast fade+translate motion. Energetic but never cluttered.
- **Copy register:** ⚠️ confident and concrete but **strictly institutional** — NO "game-changing / disrupt / supercharge". Use founder-POV info-gap ("Here's what every market-research RFP gets wrong"). The look is startup; the voice is McKinsey.
- **Flexes:** punchier pace and scale than editorial-paper. **Locks:** voice (hardest lock for this preset), palette, type.
- **Week:** either.
- **RavenMCP consult:** `business strategy` (positioning/growth framing), `brand voice systems`, `content patterns`.

### CINEMATIC
- **Use when:** hero brand video frames, Week-2 launch hero, the "C15-style" reveal the campaigns already run.
- **Maps to lane:** `cinematic-ink`. **Route:** `animate` (Ken-Burns on a still) or `animated-html`. **Default aspect:** 9:16 ≥15s (or 1:1 hero still).
- **Visual treatment:** navy→black gradient, one hero element emerging from darkness, soft red specular, slow push-in, anamorphic feel, heavy negative space. Optional film-grain via grade, never neon.
- **Copy register:** one statement; italic-red emphasis on the single value claim; staggered editorial pacing (kicker → headline → sub → CTA).
- **Flexes:** motion + filmic grade. **Locks:** ≥15s for 9:16, persistent logo every frame, one hero element.
- **Week:** either; strongest as the Day-8 launch hero.
- **RavenMCP consult:** `visual trends & branding` (2026 motion/film cues), `design principles` (motion/easing — opacity + 6px translate, Apple/Linear ease).

### SAAS
- **Use when:** "the tool / the dashboard / the data product" angle. Conveys a clean software surface.
- **Maps to lane:** `cinematic-ink` (dark UI) or `editorial-paper` (light UI). **Route:** `editorial` — render the UI in HTML/CSS, **not** Pollinations (FLUX garbles real UI). **Default aspect:** 1:1 or 16:9.
- **Visual treatment:** a single minimal product panel — one real chart, one KPI tile, one clean table — Manrope UI type, indigo dark-UI or cream light-UI, one red highlight on the hero metric/CTA. Looks like Linear / Stripe / a Bloomberg-grade tool.
- **Copy register:** ⚠️ **visually** SaaS, **voice** institutional. The dashboard is product-grade; the words are research-grade. No growth-hack copy.
- **Flexes:** product-UI surface as the hero. **Locks:** voice, palette, type, real (report-specific) data only.
- **Week:** **Week 2** if the UI shows real report data/findings; Week 1 only if the panel shows the *category/question* with placeholder/withheld values.
- **RavenMCP consult:** `UI patterns` (dashboards, data display, pricing, forms), `design tokens` (Stripe / Linear / Apple registries), `design principles` (accessibility, contrast).

### UI-HEAVY
- **Use when:** data product as proof — terminal exports, dashboards, dense tables, KPI grids carry the ad.
- **Maps to lane:** `methodology-specimen` or `cinematic-ink`. **Route:** `editorial` (real UI in HTML). **Default aspect:** 1:1 or 16:9.
- **Visual treatment:** realistic data UI — charts, tables, KPI tiles, a Bloomberg-terminal / Linear feel — dense but with exactly ONE red-highlighted hero metric so the eye still lands in 0.2s. Footnote markers + source line reinforce "transparent citation".
- **Copy register:** terse data labels in Manrope; the hero metric is the headline; one-line caption explains it in plain English.
- **Flexes:** higher information density than the 70%-negative-space norm — but still ONE hero metric. **Locks:** report-specific data (swap test is critical here), single focal metric, palette, type.
- **Week:** **Week 2** (showing real report data) unless the UI is a generic category dashboard with withheld numbers (Week 1).
- **RavenMCP consult:** `UI patterns` (data tables, charts, dashboards, empty/loading states), `design tokens`, `research & metrics frameworks` (HEART / North Star framing for which metric to feature).

### SUSPENSE
- **Use when:** withheld-information tension — "named villain", "time-decay", "hidden cost" hooks; Week-1 pre-launch teasing is the sweet spot.
- **Maps to lane:** `cinematic-ink`. **Route:** `animate` or `animated-html` (reveal pacing). **Default aspect:** 9:16 ≥15s or 1:1.
- **Visual treatment:** near-black frame, one element surfacing slowly from shadow, red accent arrives *late* as the payoff, redacted / blurred / partially-revealed document motif (perfect for an unpublished report), staggered type reveal that withholds the answer.
- **Copy register:** a question or a deliberately incomplete statement; the info-gap is the whole point; CTA resolves the tension ("See what we found →").
- **Flexes:** darkness + delayed reveal + redaction motif. **Locks:** Week-1 honesty (a redacted document must not fake real findings before publish), ≥15s, persistent logo.
- **Week:** **Week 1** is ideal (tease the question); Week 2 can pay it off with the real finding.
- **RavenMCP consult:** `design principles` (motion/easing, progressive disclosure), `visual trends & branding`, `content patterns`.

---

## 2. Placement presets — layer one of these on top of an aesthetic preset

These lock **format/dimensions/safe-zones**, not mood. "Instagram + Cinematic" = cinematic
mood in IG-correct frames. If the user names only a placement, pair it with a sensible
aesthetic (default `cinematic-ink`).

### INSTAGRAM
- **Formats:** Feed 1:1 (1080×1080), Portrait 4:5 (1080×1350), Reels/Stories 9:16 (1080×1920).
- **Safe zones (9:16):** keep the top ~270px and bottom ~320px clear of text/logo-critical content (UI chrome). Logo at x≈60, y≈290.
- **Rules:** thumb-stop in the first frame; mobile legibility (bump type toward the high end of the floors); hook in the first ~3 words; one CTA. Reels ≥15s.
- **RavenMCP consult:** `content patterns`, `design principles` (mobile readability, visual hierarchy).

### META
- **Formats:** ship 1:1 (feed) + 4:5 (portrait) as primaries, plus 9:16 for Stories/Reels placements (Advantage+ uses all).
- **Rules:** headline must read with heavy text-overlay legibility across FB + IG feeds; provide the three Meta copy fields explicitly in the concept — *primary text*, *headline*, *description*; CTA button overlay matches the platform CTA. Keep overlay text light enough to stay legible on small feed renders.
- **RavenMCP consult:** `business strategy` / `research & metrics` (which CTA + funnel framing), `content patterns`.

### LANDING-PAGE BANNER
- **Formats:** web hero — 16:9 (1920×1080), wide hero 21:9, plus standard web banner ratios (1.91:1, 3:1) as needed. **Route:** `editorial` (HTML is native for web).
- **Layout:** left-aligned headline column + right negative space or a SaaS/UI panel; single red CTA; indigo gradient or cream.
- **Price exception:** this is the **one** preset where price may appear, because the landing page is where price reveals. Use it only if the banner sits on the actual report/landing page, not as a paid social ad.
- **RavenMCP consult:** `UI patterns` (hero sections, navigation, pricing blocks), `design tokens`, `design principles` (above-the-fold hierarchy, CTA contrast).

---

## 3. RavenMCP consult — how the design layer is used

RavenMCP (`raven` server) serves *design knowledge*, not pixels. Before writing
concepts/prompts for a preset, query the raven tools noted above to ground the
treatment in real patterns/tokens/trends, then translate the guidance into
Ghost-brand-locked specs. **RavenMCP advises; it never overrides §0 global locks.**
If the `raven` server isn't connected, every preset still works — RavenMCP only
sharpens UI-heavy / SaaS / banner / luxury concepts; it's a quality multiplier,
not a dependency.

Map of preset → most useful raven domain:

| Preset | Primary raven domains |
|---|---|
| Luxury | visual trends, color theory, brand voice |
| Startup | business strategy, brand voice, content patterns |
| Cinematic | visual trends, motion/easing principles |
| SaaS | UI patterns, design tokens, accessibility |
| UI-heavy | UI patterns (data viz), design tokens, metrics frameworks |
| Suspense | motion/progressive-disclosure principles, content patterns |
| Instagram / Meta | content patterns, mobile heuristics, metrics frameworks |
| Landing-page banner | UI patterns (hero/pricing), design tokens, CTA hierarchy |

---

## 4. Quick reference — preset → route → default aspect

| Preset | Default route | Default aspect | Natural week |
|---|---|---|---|
| Luxury | pollinations → editorial | 1:1 / 4:5 | either |
| Startup | editorial / animated-html | 1:1 / 9:16 | either |
| Cinematic | animate / animated-html | 9:16 ≥15s | Week 2 hero |
| SaaS | editorial | 1:1 / 16:9 | Week 2 |
| UI-heavy | editorial | 1:1 / 16:9 | Week 2 |
| Suspense | animate / animated-html | 9:16 ≥15s | Week 1 |
| Instagram | (placement) | 1:1 / 4:5 / 9:16 | per aesthetic |
| Meta | (placement) | 1:1 + 4:5 + 9:16 | per aesthetic |
| Landing-page banner | editorial | 16:9 / 21:9 / 1.91:1 | Week 2 |
