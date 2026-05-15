#!/usr/bin/env python3
"""Generate Ghost Research short-form videos via Veo 3 Fast.

Reads `data/proposals/<slug>/prompts.md`, picks every concept whose **Tool:** contains
"veo" or "video", generates the video (max 8s on Veo 3 Fast), polls the long-running
operation, and saves the MP4 into `data/proposals/<slug>/assets/`.

Veo 3 Fast on the free tier has tight quotas — generate only the concept(s) you
care about with --concept rather than the whole batch.
"""

from __future__ import annotations

import argparse
import os
import sys
import time
from pathlib import Path

from _common import (
    BRAND_NEGATIVE,
    ConceptPrompt,
    normalize_aspect,
    parse_concepts,
    proposal_paths,
    require_api_key,
)


VIDEO_TOOL_KEYWORDS = ("veo", "video")


def select_video_concepts(concepts: list[ConceptPrompt], selected_ids: set[str] | None) -> list[ConceptPrompt]:
    out: list[ConceptPrompt] = []
    for concept in concepts:
        tool = concept.tool.lower()
        if not any(k in tool for k in VIDEO_TOOL_KEYWORDS):
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


def generate_one(client, model: str, concept: ConceptPrompt, output_path: Path, *,
                 poll_seconds: int, timeout_seconds: int) -> None:
    from google.genai import types

    aspect = normalize_aspect(concept.aspect, for_video=True)
    config_kwargs = {
        "aspect_ratio": aspect,
        "number_of_videos": 1,
        "person_generation": "allow_adult",
        "negative_prompt": BRAND_NEGATIVE,
    }
    # Veo 3 Fast supports 4/6/8 second durations on standard config; default to 8.
    try:
        config = types.GenerateVideosConfig(**config_kwargs)
    except TypeError:
        # SDK may evolve — fall back to minimal config
        config = types.GenerateVideosConfig(aspect_ratio=aspect, number_of_videos=1)

    operation = client.models.generate_videos(
        model=model,
        prompt=build_prompt(concept),
        config=config,
    )

    print(f"  - operation: {getattr(operation, 'name', '<unnamed>')}")
    deadline = time.time() + timeout_seconds
    while not operation.done:
        if time.time() > deadline:
            raise TimeoutError(f"Veo did not finish within {timeout_seconds}s")
        print("  - rendering video...")
        time.sleep(poll_seconds)
        operation = client.operations.get(operation)

    if operation.error:
        raise RuntimeError(f"Veo error: {operation.error}")

    response = operation.response
    videos = getattr(response, "generated_videos", None) or []
    if not videos:
        raise RuntimeError(f"Veo returned no videos. Response: {response}")

    video_obj = videos[0].video
    # Newer SDK: download via client.files.download; older: video.uri / video.video_bytes
    data = None
    try:
        client.files.download(file=video_obj)
        data = getattr(video_obj, "video_bytes", None)
    except Exception:  # noqa: BLE001
        data = None

    if data is None:
        # try direct video_bytes
        data = getattr(video_obj, "video_bytes", None)

    if data is None:
        # last resort: fetch by URI
        uri = getattr(video_obj, "uri", None)
        if uri:
            from urllib.request import Request, urlopen
            req = Request(uri, headers={"x-goog-api-key": os.environ["GEMINI_API_KEY"]})
            with urlopen(req) as resp:
                data = resp.read()

    if not data:
        raise RuntimeError("Veo finished but no video bytes were retrievable.")

    output_path.write_bytes(data)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate Ghost Research videos via Veo 3 Fast.")
    parser.add_argument("--slug", required=True, help="Proposal slug under data/proposals/")
    parser.add_argument("--concept", action="append", help="Specific concept id(s), e.g. --concept 04")
    parser.add_argument("--overwrite", action="store_true", help="Overwrite existing MP4s")
    parser.add_argument("--dry-run", action="store_true", help="Parse only; do not call API")
    return parser.parse_args()


def main() -> int:
    api_key = require_api_key()
    args = parse_args()

    model = os.environ.get("GHOST_VIDEO_MODEL", "veo-3.0-fast-generate-001")
    poll_seconds = int(os.environ.get("GHOST_POLL_SECONDS", "5"))
    timeout_seconds = int(os.environ.get("GHOST_TIMEOUT_SECONDS", "600"))

    proposal_dir, prompts_path, assets_dir = proposal_paths(args.slug)
    if not prompts_path.exists():
        print(f"Prompts file not found: {prompts_path}", file=sys.stderr)
        return 1

    concepts = parse_concepts(prompts_path.read_text(encoding="utf-8"))
    selected_ids = {c.zfill(2) for c in args.concept} if args.concept else None
    target = select_video_concepts(concepts, selected_ids)
    if not target:
        print("No video concepts matched.")
        return 0

    print(f"Veo model: {model}")
    print(f"Generating {len(target)} video(s) for slug '{args.slug}'\n")

    from google import genai
    client = genai.Client(api_key=api_key)
    failures = 0

    for concept in target:
        output_path = assets_dir / concept.suggested_filename
        if output_path.suffix.lower() != ".mp4":
            output_path = output_path.with_suffix(".mp4")
        print(f"[{concept.concept_id}] {concept.name}")
        print(f"  aspect: {normalize_aspect(concept.aspect, for_video=True)}")
        print(f"  output: {output_path}")

        if output_path.exists() and not args.overwrite:
            print("  - skipped (exists; use --overwrite)")
            continue
        if args.dry_run:
            print("  - dry run: prompt parsed OK")
            continue

        try:
            generate_one(
                client,
                model,
                concept,
                output_path,
                poll_seconds=poll_seconds,
                timeout_seconds=timeout_seconds,
            )
            print(f"  - saved ({output_path.stat().st_size // 1024} KB)")
        except Exception as exc:  # noqa: BLE001
            failures += 1
            print(f"  - failed: {exc}", file=sys.stderr)

    if failures:
        print(f"\nCompleted with {failures} failure(s).", file=sys.stderr)
        return 1
    print("\nAll requested videos generated.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
