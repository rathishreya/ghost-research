#!/usr/bin/env python3
"""Re-generate an existing image with an edit instruction via Pollinations.

Pollinations doesn't expose true img2img on its free endpoint, but it produces
stable, repeatable variations when you reuse the original prompt with the edit
instruction appended and a new random seed.

Used by /edit-ad. For Ghost Research:
- input: existing JPG in assets/
- instruction: plain-English change ("change the background to navy", "make the analyst look older")
- output: <stem>-edit-N.<ext> alongside the original

Workflow:
1. We look up the concept block in prompts.md (via --slug + --concept) and
   re-use its full original prompt as the base.
2. We append the edit instruction.
3. We send to Pollinations with a fresh seed.
4. Save as a sibling -edit-N file.
"""

from __future__ import annotations

import argparse
import hashlib
import sys
import time
import urllib.parse
import urllib.request
from pathlib import Path

from _common import (
    BRAND_NEGATIVE,
    REPO_ROOT,
    parse_concepts,
    proposal_paths,
)

POLL_BASE = "https://image.pollinations.ai/prompt/"

ASPECT_TO_DIMS = {
    "1:1":  (1024, 1024),
    "4:5":  (1024, 1280),
    "5:4":  (1280, 1024),
    "9:16": (1080, 1920),
    "16:9": (1920, 1080),
}


def find_next_edit_path(base: Path) -> Path:
    stem = base.stem
    ext = base.suffix or ".jpg"
    parent = base.parent
    n = 1
    while True:
        candidate = parent / f"{stem}-edit-{n}{ext}"
        if not candidate.exists():
            return candidate
        n += 1


def generate(prompt: str, aspect: str, output_path: Path, model: str = "flux") -> None:
    aspect_l = aspect.lower().strip("`")
    width, height = ASPECT_TO_DIMS.get(aspect_l, (1024, 1024))
    encoded = urllib.parse.quote(prompt[:1900])
    seed = int(hashlib.sha256((prompt + str(time.time())).encode()).hexdigest()[:8], 16) % 2_000_000
    qs = urllib.parse.urlencode({
        "width": width,
        "height": height,
        "model": model,
        "nologo": "true",
        "private": "true",
        "enhance": "true",
        "seed": seed,
    })
    url = f"{POLL_BASE}{encoded}?{qs}"
    req = urllib.request.Request(url, headers={"User-Agent": "ghost-research/1.0"})
    with urllib.request.urlopen(req, timeout=180) as resp:
        data = resp.read()
    if len(data) < 5000:
        raise RuntimeError(f"Pollinations returned too-small payload ({len(data)} bytes)")
    output_path.write_bytes(data)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Iterate on a Ghost Research image (Pollinations FLUX).")
    parser.add_argument("--slug", help="Proposal slug")
    parser.add_argument("--concept", help="Concept id (e.g. 03) — uses its original prompt as base")
    parser.add_argument("--instruction", required=True, help="The edit instruction")
    parser.add_argument("--input", help="Optional: edit a specific image path instead of by concept")
    parser.add_argument("--output", help="Optional: explicit output path")
    parser.add_argument("--aspect", default="1:1", help="Output aspect (defaults to 1:1)")
    parser.add_argument("--model", default="flux")
    return parser.parse_args()


def main() -> int:
    args = parse_args()

    if args.slug and args.concept:
        proposal_dir, prompts_path, assets_dir = proposal_paths(args.slug)
        if not prompts_path.exists():
            print(f"Prompts not found: {prompts_path}", file=sys.stderr)
            return 1
        concepts = parse_concepts(prompts_path.read_text(encoding="utf-8"))
        cid = args.concept.zfill(2)
        target = next((c for c in concepts if c.concept_id == cid), None)
        if not target:
            print(f"Concept {cid} not found in {prompts_path}", file=sys.stderr)
            return 1
        original_prompt = target.prompt
        aspect = target.aspect
        in_path = assets_dir / target.suggested_filename
        if in_path.suffix.lower() not in {".jpg", ".jpeg", ".png"}:
            matches = list(assets_dir.glob(f"{Path(target.suggested_filename).stem}*"))
            if matches:
                in_path = matches[0]
        if not in_path.exists():
            print(f"Source image missing: {in_path}\nRun /generate-assets first.", file=sys.stderr)
            return 1
        out_path = find_next_edit_path(in_path)
    elif args.input:
        in_path = Path(args.input)
        if not in_path.is_absolute():
            in_path = REPO_ROOT / in_path
        if not in_path.exists():
            print(f"Input not found: {in_path}", file=sys.stderr)
            return 1
        # No base prompt available; use the instruction alone with brand anchors
        original_prompt = (
            "Editorial photograph, deep indigo and navy color grade, soft natural light, "
            "premium B2B aesthetic similar to Bloomberg / Financial Times / The Economist, "
            "shallow depth of field, real professionals, no logos, no text."
        )
        aspect = args.aspect
        out_path = Path(args.output) if args.output else find_next_edit_path(in_path)
        if not out_path.is_absolute():
            out_path = REPO_ROOT / out_path
    else:
        print("Provide --slug + --concept OR --input.", file=sys.stderr)
        return 1

    edited_prompt = (
        f"{original_prompt}\n\nEDIT: {args.instruction.strip()}.\n\n"
        f"Keep all other elements consistent with the original frame: same subject, "
        f"same lighting key, same Ghost Research brand grade (deep indigo #181650, "
        f"near-black #06062D, occasional accent red #EF4444). "
        f"Editorial / Bloomberg-FT aesthetic. NEGATIVE: {BRAND_NEGATIVE}"
    )

    print(f"Editing concept image: {in_path}")
    print(f"Instruction:           {args.instruction}")
    print(f"Output:                {out_path}")

    try:
        generate(edited_prompt, aspect, out_path, model=args.model)
    except Exception as exc:  # noqa: BLE001
        print(f"Failed: {exc}", file=sys.stderr)
        return 1

    print(f"Saved -> {out_path}  ({out_path.stat().st_size // 1024} KB)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
