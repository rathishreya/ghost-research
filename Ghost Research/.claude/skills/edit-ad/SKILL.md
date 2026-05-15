---
name: edit-ad
description: Iterate on a single Ghost Research ad — change something the user doesn't like and regenerate. Handles all three asset types — Pollinations images (re-prompt with edit instruction via pollinations_edit.py), editorial HTML cards (rewrite the HTML in prompts.md and re-render), and animate videos (re-animate the underlying still or change motion params). Use when the user says "change this ad", "/edit-ad", "make the analyst look older", "swap the headline", "make it pan right instead of zoom in", or anything that's a per-ad refinement request.
---

# Edit Ad — Ghost Research

Your job: take a user's plain-English change request, locate the right concept
in `prompts.md`, route the edit to the right script, save a new versioned
output, and surface the result. Never overwrite the original — always create
a sibling `-edit-N` file.

## Step 1 — Parse the request

The user will say something like:
- `/edit-ad 03 make the analyst look older`
- `/edit-ad concept-05 swap headline to "The $47B question..."`
- "Make the third ad's background morning instead of dusk"
- "On concept 02, change the stat to 73%"
- "On concept 04, make it pan right instead of zoom in"

Identify:
- The **slug** (latest proposal if not specified)
- The **concept id** (e.g. `03`)
- The **edit instruction** (plain English)

If you can't identify the concept, ask the user — don't guess and waste a generation.

## Step 2 — Dispatch by Tool

Read the concept's `Tool:` field in `prompts.md`. Route accordingly.

### Tool: pollinations
The image is a FLUX-generated photo. Re-prompt with the edit instruction
appended, fresh seed:

```bash
python scripts/pollinations_edit.py --slug <slug> --concept <id> --instruction "<edit text>"
```

Saves to `assets/<original-stem>-edit-N.jpg`. Compare to the original; if the
new version is on-brand and addresses the instruction, recommend it as the
canonical asset (the user can rename `-edit-1` → drop the suffix to make it
canonical). If it didn't move the needle, re-run with a sharper instruction.

### Tool: editorial
The asset is an HTML/CSS card. Two paths:

**Path A — small text/value change** (e.g. swap the stat, fix a typo):
1. Read `data/proposals/<slug>/prompts.md` and find Concept N's HTML block.
2. Edit the HTML directly in `prompts.md` (precise change only — preserve all
   brand tokens: `#181650`, `#06062D`, `#EF4444`, Oranienbaum / Manrope).
3. Also write the edited HTML to
   `data/proposals/<slug>/editorial/<concept-stem>-edit-N.html`.
4. Re-render to a sibling PNG:

```bash
python scripts/render_editorial.py \
  --html data/proposals/<slug>/editorial/<concept-stem>-edit-N.html \
  --out  data/proposals/<slug>/assets/<concept-stem>-edit-N.png \
  --aspect <aspect from concept>
```

**Path B — layout / structural change** (e.g. "make it landscape", "add a
sub-headline", "move the CTA to top-right"):
1. Rewrite the full HTML inside the concept block to match.
2. Save and re-render as above.

In either case, preserve the brand: same gradient bg, same fonts, same red
accent, single focal element.

### Tool: animate
The asset is a still + Ken Burns motion. There are two flavours of edit:

**Edit A — change the underlying still:** route the instruction to the
SOURCE pollinations concept (use its concept id, not the animate concept's id).
After it generates, re-run animate for the dependent concept:

```bash
python scripts/pollinations_edit.py --slug <slug> --concept <source-id> --instruction "..."
# Then rename the resulting -edit-N back to the canonical filename so animate picks it up,
# OR pass --input directly:
python scripts/animate_image.py --input <new-still.jpg> --out <new-mp4.mp4> --aspect 9:16 --duration 8 --motion zoom-in
```

**Edit B — change the motion params:** if the instruction is about motion only
(pan instead of zoom, faster, slower), update the concept's `**Motion:**` and/or
`**Duration:**` fields in `prompts.md`, then re-animate:

```bash
python scripts/animate_image.py --slug <slug> --concept <id> --overwrite
```

(The `--overwrite` is intentional here because animate output is cheap and
re-derivable — and the user's intent is "replace the motion", not "stack
variants". Still, snapshot the previous MP4 to a `-prev` filename first if
the user might want to compare.)

### Tool: animated-html
The asset is a CSS-animated HTML page recorded as MP4. Same as editorial Path B:
rewrite the HTML in the concept block, re-record:

```bash
python scripts/render_animated.py --slug <slug> --concept <id> --overwrite
```

If the instruction is timing-only ("slow down the reveal", "delay the CTA by
a second"), edit the `@keyframes` delays in the HTML rather than regenerating
from scratch.

### Tool: veo
Skip on free tier. If the user has paid access, route to
`scripts/gemini_video.py --slug <slug> --concept <id> --overwrite`.

## Step 3 — Show the result

After the script returns, give the user:
1. Where the new file is saved
2. What changed (one line)
3. The option: "If this is good, run `/edit-ad <id> 'keep this version'` to
   make it canonical (rename) or run /generate-video / /prep-campaign next."

If the result is bad, suggest a sharper instruction the user could try.

## Step 4 — Update pipeline (optional)

For substantive edits (not micro tweaks), append:
`[date] | [slug] | edited concept [id] | "<instruction>" → <output>`

## Rules

- **Always create a sibling `-edit-N` file. Never overwrite the original**
  on the first edit pass. The user may want to revert.
- **Surface the actual generated file path** so the user can open it.
- **Bias toward small, targeted instructions.** "Make the analyst look older"
  is good. "Make this better" is not — push back and ask what specifically.
- **Brand must survive every edit.** Deep indigo grade, Oranienbaum + Manrope,
  single `#EF4444` accent, no robots, no AI-uncanny faces. If an edit drifts
  off-brand, regenerate with brand anchors re-emphasized.
- **For multi-asset campaigns,** don't auto-cascade edits across concepts.
  If the user says "make all the analysts look older", confirm scope before
  burning compute on every concept.
