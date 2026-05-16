#!/usr/bin/env python3
"""Render Ghost Research editorial HTML cards to PNG via headless Chromium.

Two modes:
1. Bulk:    --slug <slug>       — scan prompts.md, render every Tool=editorial concept
2. Single:  --html <path> --out <png> --aspect 1:1

The bulk mode is what /generate-assets calls. The single mode is for ad-hoc
testing or one-off renders.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from _common import (
    ConceptPrompt,
    REPO_ROOT,
    inject_ghost_asset_urls,
    normalize_aspect,
    parse_concepts,
    proposal_paths,
)


ASPECT_TO_DIMS = {
    "1:1":  (1080, 1080),
    "4:5":  (1080, 1350),
    "5:4":  (1350, 1080),
    "9:16": (1080, 1920),
    "16:9": (1920, 1080),
    "4:3":  (1440, 1080),
    "3:4":  (1080, 1440),
}


def html_path_to_url(path: Path) -> str:
    return path.resolve().as_uri()


def render(html_input: str | Path, out_path: Path, aspect: str, scale: float = 2.0) -> None:
    from playwright.sync_api import sync_playwright

    aspect = normalize_aspect(aspect)
    width, height = ASPECT_TO_DIMS.get(aspect, ASPECT_TO_DIMS["1:1"])

    out_path.parent.mkdir(parents=True, exist_ok=True)

    with sync_playwright() as p:
        browser = p.chromium.launch()
        context = browser.new_context(
            viewport={"width": width, "height": height},
            device_scale_factor=scale,
        )
        page = context.new_page()
        if isinstance(html_input, Path):
            page.goto(html_path_to_url(html_input), wait_until="networkidle")
        else:
            page.set_content(html_input, wait_until="networkidle")
        page.wait_for_timeout(500)  # let webfonts settle
        page.screenshot(path=str(out_path), full_page=False, omit_background=False, type="png")
        browser.close()


def select_editorial_concepts(concepts: list[ConceptPrompt], selected_ids: set[str] | None) -> list[ConceptPrompt]:
    out: list[ConceptPrompt] = []
    for concept in concepts:
        if "editorial" not in concept.tool.lower():
            continue
        if selected_ids and concept.concept_id not in selected_ids:
            continue
        out.append(concept)
    return out


def bulk_render(slug: str, selected_ids: set[str] | None, scale: float, overwrite: bool, dry_run: bool) -> int:
    proposal_dir, prompts_path, assets_dir = proposal_paths(slug)
    if not prompts_path.exists():
        print(f"Prompts file not found: {prompts_path}", file=sys.stderr)
        return 1
    concepts = parse_concepts(prompts_path.read_text(encoding="utf-8"))
    target = select_editorial_concepts(concepts, selected_ids)
    if not target:
        print("No editorial concepts matched.")
        return 0

    target.sort(key=lambda c: int(c.concept_id))
    failures = 0
    for concept in target:
        suggested = concept.suggested_filename
        if not suggested.lower().endswith(".png"):
            suggested = Path(suggested).with_suffix(".png").name
        output_path = assets_dir / suggested
        print(f"[{concept.concept_id}] {concept.name}")
        print(f"  aspect: {normalize_aspect(concept.aspect)}")
        print(f"  output: {output_path}")
        if output_path.exists() and not overwrite:
            print("  - skipped (exists; use --overwrite)")
            continue
        if dry_run:
            print("  - dry run: HTML parsed OK")
            continue
        try:
            html_ready = inject_ghost_asset_urls(concept.prompt, assets_dir)
            # Write HTML to disk so Chromium loads it via file:// origin.
            # Required: about:blank pages cannot fetch file:// resources, so
            # background-image: url(file:///...) silently fails when we use
            # page.set_content(). page.goto(file://...) makes those fetches work.
            editorial_dir = proposal_dir / "editorial"
            editorial_dir.mkdir(parents=True, exist_ok=True)
            html_path = editorial_dir / (Path(suggested).stem + ".html")
            html_path.write_text(html_ready, encoding="utf-8")
            render(html_path, output_path, concept.aspect, scale)
            print(f"  - saved ({output_path.stat().st_size // 1024} KB)")
        except Exception as exc:  # noqa: BLE001
            failures += 1
            print(f"  - failed: {exc}", file=sys.stderr)
    if failures:
        print(f"\nCompleted with {failures} failure(s).", file=sys.stderr)
        return 1
    print("\nAll requested editorial cards rendered.")
    return 0


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Render Ghost Research editorial HTML cards to PNG.")
    parser.add_argument("--slug", help="Proposal slug — bulk mode: render every Tool=editorial concept")
    parser.add_argument("--concept", action="append", help="Specific concept id(s) in bulk mode")
    parser.add_argument("--html", help="Single-render mode: path to an .html file")
    parser.add_argument("--out", help="Single-render mode: PNG output path")
    parser.add_argument("--aspect", default="1:1", help="Single-render mode aspect")
    parser.add_argument("--scale", type=float, default=2.0, help="Device pixel ratio (default 2.0 retina)")
    parser.add_argument("--overwrite", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    return parser.parse_args()


def main() -> int:
    args = parse_args()

    if args.slug:
        selected_ids = {c.zfill(2) for c in args.concept} if args.concept else None
        return bulk_render(args.slug, selected_ids, args.scale, args.overwrite, args.dry_run)

    if args.html and args.out:
        html_path = Path(args.html)
        if not html_path.is_absolute():
            html_path = REPO_ROOT / html_path
        if not html_path.exists():
            print(f"HTML file not found: {html_path}", file=sys.stderr)
            return 1
        out_path = Path(args.out)
        if not out_path.is_absolute():
            out_path = REPO_ROOT / out_path
        text = html_path.read_text(encoding="utf-8")
        assets_dir = out_path.parent
        render(inject_ghost_asset_urls(text, assets_dir), out_path, args.aspect, args.scale)
        print(f"Rendered -> {out_path}  ({out_path.stat().st_size // 1024} KB)")
        return 0

    print("Provide --slug (bulk) or --html + --out (single).", file=sys.stderr)
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
