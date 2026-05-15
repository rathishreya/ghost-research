#!/usr/bin/env python3
"""Generate Ghost Research image assets via the official Google Gemini API.

Uses Imagen 4 (Ultra/Standard/Fast) for hero-quality generation.
Reads `data/proposals/<slug>/prompts.md`, picks every image concept,
generates the image, and saves the JPG/PNG into `data/proposals/<slug>/assets/`.

Concepts are matched when **Tool:** contains any of: nanobanana, imagen, image, photo.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from _common import (
    BRAND_NEGATIVE,
    ConceptPrompt,
    REPO_ROOT,
    normalize_aspect,
    parse_concepts,
    proposal_paths,
    require_api_key,
)


IMAGE_TOOL_KEYWORDS = ("nanobanana", "imagen", "image", "photo", "static")


def select_image_concepts(concepts: list[ConceptPrompt], selected_ids: set[str] | None) -> list[ConceptPrompt]:
    out: list[ConceptPrompt] = []
    for concept in concepts:
        tool = concept.tool.lower()
        if "veo" in tool or "video" in tool:
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


def generate_one(client, model: str, concept: ConceptPrompt, output_path: Path) -> None:
    from google.genai import types

    aspect = normalize_aspect(concept.aspect, for_video=False)
    config = types.GenerateImagesConfig(
        number_of_images=1,
        aspect_ratio=aspect,
        output_mime_type="image/jpeg" if output_path.suffix.lower() in {".jpg", ".jpeg"} else "image/png",
        safety_filter_level="BLOCK_ONLY_HIGH",
        person_generation="ALLOW_ADULT",
    )

    response = client.models.generate_images(
        model=model,
        prompt=build_prompt(concept),
        config=config,
    )

    images = getattr(response, "generated_images", None) or []
    if not images:
        raise RuntimeError("No images returned by Imagen — check prompt for safety blocks.")

    img = images[0].image
    image_bytes = getattr(img, "image_bytes", None)
    if image_bytes is None and hasattr(img, "_pil_image"):
        from io import BytesIO
        buf = BytesIO()
        img._pil_image.save(buf, format="JPEG")
        image_bytes = buf.getvalue()
    if image_bytes is None:
        raise RuntimeError("Imagen returned an image with no bytes.")

    output_path.write_bytes(image_bytes)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate Ghost Research images via Google Imagen 4.")
    parser.add_argument("--slug", required=True, help="Proposal slug under data/proposals/")
    parser.add_argument("--concept", action="append", help="Specific concept id(s), e.g. --concept 01")
    parser.add_argument("--quality", choices=["ultra", "standard", "fast"], default="ultra",
                        help="Image quality. ultra = Imagen 4 Ultra (best, slower), fast = Imagen 4 Fast (cheap free-tier).")
    parser.add_argument("--overwrite", action="store_true", help="Overwrite existing assets")
    parser.add_argument("--dry-run", action="store_true", help="Parse only; do not call API")
    return parser.parse_args()


QUALITY_MODEL_ENV = {
    "ultra": ("GHOST_IMAGE_MODEL", "imagen-4.0-ultra-generate-001"),
    "standard": ("GHOST_IMAGE_MODEL_STANDARD", "imagen-4.0-generate-001"),
    "fast": ("GHOST_IMAGE_MODEL_FAST", "imagen-4.0-fast-generate-001"),
}


def main() -> int:
    api_key = require_api_key()
    args = parse_args()

    import os
    env_var, default = QUALITY_MODEL_ENV[args.quality]
    model = os.environ.get(env_var, default)

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
        print("No image concepts matched (none with Tool containing nanobanana/imagen/image/photo).")
        return 0

    print(f"Imagen model: {model}  (quality={args.quality})")
    print(f"Generating {len(target)} image(s) for slug '{args.slug}'\n")

    from google import genai
    client = genai.Client(api_key=api_key)
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
            generate_one(client, model, concept, output_path)
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
