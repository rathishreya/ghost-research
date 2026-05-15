#!/usr/bin/env python3
"""Edit / iterate on an existing image using Gemini 2.5 Flash Image (Nano Banana).

Examples:
    python scripts/gemini_edit.py --input assets/hero.jpg --instruction "Change the background to deep navy #06062D" --output assets/hero-navy.jpg
    python scripts/gemini_edit.py --slug ai-due-diligence --concept 03 --instruction "Make the analyst look more senior; remove the laptop"

When --slug + --concept is used, the script edits the existing asset for that
concept and saves a new file alongside with an `-edit-N` suffix.
"""

from __future__ import annotations

import argparse
import os
import sys
from io import BytesIO
from pathlib import Path

from _common import (
    BRAND_NEGATIVE,
    parse_concepts,
    proposal_paths,
    require_api_key,
)


def find_next_edit_path(base: Path) -> Path:
    """Return next available `<stem>-edit-N.<ext>` path so we never overwrite."""
    stem = base.stem
    ext = base.suffix or ".jpg"
    parent = base.parent
    n = 1
    while True:
        candidate = parent / f"{stem}-edit-{n}{ext}"
        if not candidate.exists():
            return candidate
        n += 1


def edit_image(client, model: str, image_path: Path, instruction: str, output_path: Path) -> None:
    from google.genai import types
    from PIL import Image as PILImage

    pil_image = PILImage.open(image_path)
    full_prompt = (
        f"Edit this Ghost Research ad image. Instruction: {instruction.strip()}.\n\n"
        f"Keep the existing composition, lighting and Ghost brand grade (deep indigo #181650, near-black #06062D, "
        f"accent red #EF4444). Stay editorial / Bloomberg-FT aesthetic. {BRAND_NEGATIVE}"
    )

    response = client.models.generate_content(
        model=model,
        contents=[full_prompt, pil_image],
        config=types.GenerateContentConfig(response_modalities=["IMAGE", "TEXT"]),
    )

    saved = False
    for part in response.candidates[0].content.parts:
        inline = getattr(part, "inline_data", None)
        if inline is not None and getattr(inline, "data", None):
            data = inline.data
            if isinstance(data, str):
                import base64
                data = base64.b64decode(data)
            output_path.write_bytes(data)
            saved = True
            break

    if not saved:
        text = ""
        for part in response.candidates[0].content.parts:
            if getattr(part, "text", None):
                text += part.text
        raise RuntimeError(f"Nano Banana returned no image. Model said: {text[:300]}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Edit an image with Gemini 2.5 Flash Image (Nano Banana).")
    parser.add_argument("--input", help="Path to image to edit (relative to repo root or absolute)")
    parser.add_argument("--output", help="Where to save the edited image")
    parser.add_argument("--slug", help="Proposal slug — used with --concept to find the source")
    parser.add_argument("--concept", help="Concept id (e.g. 03) to edit; reads suggested filename from prompts.md")
    parser.add_argument("--instruction", required=True, help="The edit instruction in plain English")
    return parser.parse_args()


def resolve_input_and_output(args: argparse.Namespace) -> tuple[Path, Path]:
    if args.input:
        in_path = Path(args.input)
        if not in_path.is_absolute():
            from _common import REPO_ROOT
            in_path = REPO_ROOT / in_path
        if not in_path.exists():
            print(f"Input image not found: {in_path}", file=sys.stderr)
            sys.exit(1)
        out_path = Path(args.output) if args.output else find_next_edit_path(in_path)
        if not out_path.is_absolute():
            from _common import REPO_ROOT
            out_path = REPO_ROOT / out_path
        return in_path, out_path

    if not (args.slug and args.concept):
        print("Provide either --input/--output or --slug + --concept.", file=sys.stderr)
        sys.exit(1)

    proposal_dir, prompts_path, assets_dir = proposal_paths(args.slug)
    if not prompts_path.exists():
        print(f"Prompts file not found: {prompts_path}", file=sys.stderr)
        sys.exit(1)
    concepts = parse_concepts(prompts_path.read_text(encoding="utf-8"))
    cid = args.concept.zfill(2)
    target = next((c for c in concepts if c.concept_id == cid), None)
    if not target:
        print(f"Concept {cid} not found in {prompts_path}", file=sys.stderr)
        sys.exit(1)
    in_path = assets_dir / target.suggested_filename
    if in_path.suffix.lower() not in {".jpg", ".jpeg", ".png"}:
        # fall back: any file in assets_dir with this concept's stem
        matches = list(assets_dir.glob(f"{Path(target.suggested_filename).stem}*"))
        if not matches:
            print(f"No generated asset found for concept {cid} in {assets_dir}", file=sys.stderr)
            sys.exit(1)
        in_path = matches[0]
    if not in_path.exists():
        print(f"Source image missing: {in_path}\nRun /generate-assets first.", file=sys.stderr)
        sys.exit(1)
    out_path = find_next_edit_path(in_path)
    return in_path, out_path


def main() -> int:
    api_key = require_api_key()
    args = parse_args()
    model = os.environ.get("GHOST_EDIT_MODEL", "gemini-2.5-flash-image")

    in_path, out_path = resolve_input_and_output(args)
    print(f"Editing:     {in_path}")
    print(f"Instruction: {args.instruction}")
    print(f"Model:       {model}")
    print(f"Output:      {out_path}")

    from google import genai
    client = genai.Client(api_key=api_key)

    try:
        edit_image(client, model, in_path, args.instruction, out_path)
    except Exception as exc:  # noqa: BLE001
        print(f"Failed: {exc}", file=sys.stderr)
        return 1

    print(f"Saved -> {out_path}  ({out_path.stat().st_size // 1024} KB)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
