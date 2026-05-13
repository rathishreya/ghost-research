---
name: write-prompts
description: Convert Ghost Research visual concepts into ready-to-paste prompts for Veo 3 (video), nanobanana / Imagen (image), and ElevenLabs (voiceover). Every prompt encodes Ghost brand rules — deep indigo color grade, real professionals only, no robots, no AI clichés. Use when the user wants generation prompts, says "write prompts", "/write-prompts", or right after /design-ads.
---

# Prompt Engineering Agent — Ghost Research

Your job: turn each visual concept into a prompt the user can paste directly into Veo 3, nanobanana, or ElevenLabs. The user is non-technical — prompts must work on the first paste.

## Step 1 — Read inputs

- `data/proposals/<slug>/visual-concepts.md` (the concept portfolio from `/design-ads`)
- `data/proposals/<slug>/campaign-brief.md` (for copy + CTA cross-reference)

## Step 2 — Brand encoding (must appear in every prompt)

### Universal positive style anchors (use across all prompts)

For every image/video prompt, weave in these style anchors:

```
Editorial photography, color-graded to deep indigo and cool navy tones,
high detail, sharp focus on subject, soft natural light, clean minimalist
composition with negative space, premium B2B aesthetic similar to
Bloomberg, Financial Times, or The Economist.
```

### Universal negative anchors (use across all prompts)

Every prompt must include negatives to prevent off-brand outputs:

```
No robots, no AI-themed imagery, no brain circuits, no glowing nodes,
no holograms, no neon, no cyberpunk, no sci-fi UI, no high-fiving,
no hands on keyboards, no fist bumps, no smiling-at-camera lifestyle,
no AI-generated faces, no uncanny features, no text in image,
no logos, no watermarks.
```

### Color palette references (when relevant)

If the concept calls for specific palette elements, name the hex values:
- Red accent: `#EF4444`
- Deep indigo: `#181650`
- Near-black: `#06062D`
- Clean background: `#F8F8FF`

## Step 3 — Map concepts to generators

| Concept format from visual-concepts.md | Tool | Aspect / duration |
|---|---|---|
| Static — single image | **nanobanana** (or Imagen 4) | 1:1 / 4:5 / 1.91:1 |
| Static — data viz | **nanobanana** | 1:1 |
| Carousel / document ad | **nanobanana** — one prompt per slide | 1:1 |
| Short video — 8s | **Veo 3** | 9:16 |
| Cinematic video — 15-30s | **Veo 3** (multiple stitched clips) | 9:16 or 1:1 |

For every concept with voiceover, also write an **ElevenLabs script**.

## Step 4 — Write the prompts

Save to `data/proposals/<slug>/prompts.md`:

````markdown
---
slug: [slug]
created: [YYYY-MM-DD]
brief: campaign-brief.md
concepts: visual-concepts.md
status: ready-to-generate
total_prompts: [N]
---

# Generation Prompts — [Report Title]

## 📋 How to use this file

1. For each prompt block (between triple backticks), copy the entire block
2. Paste into the named tool — Veo 3 / nanobanana / Imagen / ElevenLabs
3. Generate; if first result is off, regenerate 1-2 more times before tweaking the prompt
4. Save generated files into `data/proposals/[slug]/assets/` using the suggested filename
5. Composite final assets (overlay headline + CTA in Figma/Canva/Premiere)
6. When all assets are done, run `/prep-campaign`

## ⚠️ Brand reminder for everything you generate

- All visuals get a **deep indigo / navy color grade** in post if the generator didn't bake it in
- **NO text or logos in the generated image** — always add Oranienbaum headlines and the `#EF4444` red CTA button in your design tool over the generated image
- If a generated person looks AI-uncanny (waxy skin, weird eyes, wrong hands), regenerate. Ghost Research is a credible research brand; uncanny people = trust collapse.

---

## Concept 01 — [Name from visual-concepts.md]

**Tool:** [Veo 3 / nanobanana]
**Aspect:** [9:16 / 1:1 / 4:5]
**Duration:** [for video: 8s / 15s]
**Suggested filename:** `[concept-01-name].[mp4|jpg]`
**Maps to:** [Day X, Week Y]

### Generation prompt
```
[Single paragraph. Structure:
Sentence 1: Subject + setting — concrete people, specific clothing, specific environment
Sentence 2: Camera + composition — lens, framing, negative space location
Sentence 3: Lighting + mood — light source, direction, quality
Sentence 4: (Video only) Motion — camera move + subject action
Sentence 5: Style anchors — editorial photography, deep indigo grade, Bloomberg/FT aesthetic, [film stock or lens reference if it helps]
Then: Negative anchors block — no robots, no AI imagery, no text, etc.
End with: "Photoreal, shot on Arri Alexa Mini with 50mm prime, shallow depth of field, natural skin tones graded toward cool blue."
]

NEGATIVE: no robots, no AI-themed imagery, no brain circuits, no glowing
nodes, no holograms, no neon, no cyberpunk, no sci-fi UI, no high-fiving,
no hands on keyboards, no fist bumps, no smiling-at-camera lifestyle,
no AI-generated faces, no uncanny features, no text in image,
no logos, no watermarks.
```

### Voiceover (ElevenLabs) — only if video concept has VO

**Voice:** [Suggested: "Adam (calm authority, mid-30s American male)" / "Rachel (warm warmth)" / "Antoni (energetic founder)" — pick one that fits the hook's emotion]
**Direction:** [e.g. "Measured pace. Slight emphasis on the word 'evidence'. Pause after the question. No exclamation."]
**Script:**
```
[Exact words. Mark pauses with /// and emphasis with CAPS. Under 25 words for 8s, under 60 for 15s, under 110 for 30s.]
```

### Overlay specs (added in design tool, NOT generated)

- **Headline:** "[Exact text from brief Section 7]" — Oranienbaum, [white on dark / `#181650` on light], [position]
- **Body / data label:** "[Exact text]" — Manrope regular, [color], [position]
- **CTA button:** "[Exact CTA]" — fill `#EF4444`, text white Manrope semibold, [position]
- **Ghost Research wordmark:** bottom-left, small, [white or `#181650` depending on background]

### After generation — checklist

- [ ] Generated → saved to assets/`[filename]`
- [ ] VO recorded → saved to assets/`[filename]-vo.mp3` (if applicable)
- [ ] Headline + body + CTA overlay composited → saved to assets/`[filename]-final.[mp4|jpg]`
- [ ] Quick brand check: deep indigo grade present? No accidental robots? Text overlays in correct fonts?

---

## Concept 02 — [Name]
[... same structure ...]

---

[... continue for all concepts ...]

---

## 🎤 ElevenLabs voice consistency note

If multiple video concepts share the same Hook (per the brief), use the **same voice** across them for brand continuity. Different hooks can use different voices to signal a different angle.

Recommended voice cast for Ghost Research:
- **The Data Hook / Authority angle:** Adam (calm, mid-30s American male) — measured, factual
- **The Consequence Hook / Fear angle:** Rachel (warm, mature female) — serious, weight-of-experience
- **The Gap Hook / Contrarian angle:** Antoni (clear, slightly younger male) — direct, slightly provocative

## 💰 Rough generation cost estimate

- Veo 3 (8s clip): ~$1.50-3.00 per generation → [N video concepts × 2 regenerations avg] = ~$[X]
- nanobanana (1 image): ~$0.05-0.15 per generation → [N image concepts × 3 regenerations avg] = ~$[X]
- ElevenLabs VO: ~$0.05 per script × [N scripts] = ~$[X]
- **Total estimated:** ~$[X]

All assets stay reusable across this campaign + future Ghost campaigns where they fit, so cost amortizes.

---

## ✅ Generation complete checklist

When the assets folder is complete, you should have:

- [ ] [N] final composited images / videos
- [ ] All filenames match what's listed above
- [ ] Each asset has been brand-checked (deep indigo grade, no robots, no uncanny faces, fonts correct)
- [ ] If any concept refused to generate well after 3 tries, note here why: ____

Once complete, run: `/prep-campaign`
````

## Step 5 — Update pipeline

Append: `[date] | [slug] | prompts written | [N] prompts ready`

## Step 6 — Hand off

```
✅ Prompts ready: data/proposals/[slug]/prompts.md

Manual step (about 1-2 hours):
1. Open prompts.md
2. Copy each prompt block into the named tool
3. Save outputs into data/proposals/[slug]/assets/
4. Composite final assets — overlay Oranienbaum headlines + `#EF4444` red CTA buttons in Figma/Canva
5. When done, type /prep-campaign

Brand reminder: deep indigo grade on every final, NO robots or AI-uncanny faces. Regenerate anything off-brand.

Rough cost: ~$[X] total in generation credits.
```

## Rules — Veo 3 specifically

- **Never put dialogue or on-screen text in the Veo 3 prompt.** It's unreliable. Generate visuals only; add text + VO in post.
- **Anchor lighting and lens.** "Shot on Arri Alexa Mini, 50mm prime, soft window light from camera left, deep navy color grade" produces consistent Ghost-brand results.
- **One subject per shot.** Multi-character scenes drift in Veo. If a concept needs two people, prompt for one establishing shot + close-ups separately.
- **Describe the FIRST FRAME explicitly.** "Opens on [X]" — this is the scroll-stop frame.
- **For motion, describe the camera not the subject.** "Slow push-in" / "static locked-off" / "subtle handheld" — these give predictable, premium results.

## Rules — nanobanana / Imagen specifically

- **Always describe the negative space.** Most generators ignore "leave room for text"; describe the composition that creates it (subject in lower-left third, negative space upper-right).
- **Never ask the generator to render text.** All text goes on top in your design tool.
- **Color palette as specific hex** beats vague words. "#181650 navy background" beats "dark blue background."

## Rules — ElevenLabs specifically

- **Under 25 words for 8s.** Audio paces at 130-150 wpm.
- **Mark pauses (`///`) and emphasis (`CAPS`).** ElevenLabs respects both.
- **No exclamations.** Ghost voice is measured, not hype-y. Statements end with confidence, not excitement.
- **Pick one voice per hook angle** for brand consistency across the campaign.
