#!/usr/bin/env python3
"""Generate Ghost Research images via Pollinations.ai (free, FLUX-based, no API key).

Reads `data/proposals/<slug>/prompts.md`, finds every image concept, sends the prompt
to Pollinations and saves the JPG/PNG into `data/proposals/<slug>/assets/`.

Pollinations is a free, no-auth wrapper around FLUX. Quality is solid for premium
B2B aesthetics when paired with strong style anchors. Use `editorial` model for the
sharpest editorial look, `flux` for general-purpose.

Concepts matched when **Tool:** contains: pollinations, flux, nanobanana, imagen,
image, photo (any image generator alias).
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
    ConceptPrompt,
    normalize_aspect,
    parse_concepts,
    proposal_paths,
)

POLL_BASE = "https://image.pollinations.ai/prompt/"

IMAGE_TOOL_KEYWORDS = (
    "pollinations", "flux", "nanobanana", "imagen", "image", "photo", "static",
)

ASPECT_TO_DIMS = {
    "1:1":  (1024, 1024),
    "4:5":  (1024, 1280),
    "5:4":  (1280, 1024),
    "9:16": (1080, 1920),
    "16:9": (1920, 1080),
    "4:3":  (1280, 960),
    "3:4":  (960, 1280),
}


def select_image_concepts(concepts: list[ConceptPrompt], selected_ids: set[str] | None) -> list[ConceptPrompt]:
    out: list[ConceptPrompt] = []
    for concept in concepts:
        tool = concept.tool.lower()
        if "veo" in tool or "video" in tool:
            continue
        if "editorial" in tool:
            # editorial cards are handled by render_editorial.py, not this script
            continue
        if not any(k in tool for k in IMAGE_TOOL_KEYWORDS):
            continue
        if selected_ids and concept.concept_id not in selected_ids:
            continue
        out.append(concept)
    return out


def build_prompt(concept: ConceptPrompt) -> str:
    body = concept.prompt
    if "no robots" not in body.lower():
        body = f"{body}\n\nNEGATIVE: {BRAND_NEGATIVE}"
    return body


def stable_seed(prompt: str) -> int:
    return int(hashlib.sha256(prompt.encode("utf-8")).hexdigest()[:8], 16) % 2_000_000


def generate_one(concept: ConceptPrompt, output_path: Path, *, model: str, retries: int = 3) -> None:
    aspect = normalize_aspect(concept.aspect)
    width, height = ASPECT_TO_DIMS.get(aspect, ASPECT_TO_DIMS["1:1"])
    prompt = build_prompt(concept)
    encoded = urllib.parse.quote(prompt[:1800])
    seed = stable_seed(prompt + concept.concept_id)
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

    last_err: Exception | None = None
    for attempt in range(1, retries + 1):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "ghost-research/1.0"})
            with urllib.request.urlopen(req, timeout=180) as resp:
                data = resp.read()
            if len(data) < 5000:
                raise RuntimeError(f"Pollinations returned too-small payload ({len(data)} bytes) — likely an error image")
            output_path.write_bytes(data)
            return
        except Exception as exc:  # noqa: BLE001
            last_err = exc
            if attempt < retries:
                wait = 5 * attempt
                print(f"  - attempt {attempt} failed ({exc}), retrying in {wait}s...")
                time.sleep(wait)
            else:
                raise


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate Ghost Research images via Pollinations.ai (free FLUX).")
    parser.add_argument("--slug", required=True, help="Proposal slug under data/proposals/")
    parser.add_argument("--concept", action="append", help="Specific concept id(s), e.g. --concept 01")
    parser.add_argument("--model", default="flux",
                        choices=["flux", "flux-realism", "flux-anime", "flux-3d", "turbo"],
                        help="Pollinations model. flux = balanced; turbo = fastest.")
    parser.add_argument("--overwrite", action="store_true", help="Overwrite existing assets")
    parser.add_argument("--dry-run", action="store_true", help="Parse only; do not call API")
    return parser.parse_args()


def main() -> int:
    args = parse_args()

    proposal_dir, prompts_path, assets_dir = proposal_paths(args.slug)
    if not prompts_path.exists():
        print(f"Could not find prompts file: {prompts_path}", file=sys.stderr)
        return 1

    prompts_text = prompts_path.read_text(encoding="utf-8")
    concepts = parse_concepts(prompts_text)
    if not concepts:
        print(f"No concepts parsed from {prompts_path}", file=sys.stderr)
        return 1

    selected_ids = {c.zfill(2) for c in args.concept} if args.concept else None
    target = select_image_concepts(concepts, selected_ids)
    if not target:
        print("No image concepts matched.")
        return 0

    print(f"Pollinations model: {args.model}")
    print(f"Generating {len(target)} image(s) for slug '{args.slug}'\n")
    failures = 0

    for concept in target:
        output_path = assets_dir / concept.suggested_filename
        if output_path.suffix.lower() not in {".jpg", ".jpeg", ".png"}:
            output_path = output_path.with_suffix(".jpg")
        print(f"[{concept.concept_id}] {concept.name}")
        print(f"  aspect: {normalize_aspect(concept.aspect)}")
        print(f"  output: {output_path}")

        if output_path.exists() and not args.overwrite:
            print("  - skipped (exists; use --overwrite to replace)")
            continue
        if args.dry_run:
            print("  - dry run: prompt parsed OK")
            continue

        try:
            generate_one(concept, output_path, model=args.model)
            print(f"  - saved ({output_path.stat().st_size // 1024} KB)")
        except Exception as exc:  # noqa: BLE001
            failures += 1
            print(f"  - failed: {exc}", file=sys.stderr)

    if failures:
        print(f"\nCompleted with {failures} failure(s).", file=sys.stderr)
        return 1
    print("\nAll requested image assets generated.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
