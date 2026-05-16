#!/usr/bin/env python3
"""Record a CSS-animated HTML page as an MP4 via Playwright.

Used for Ghost Research editorial video ads where the motion comes from
CSS animation (headlines fading in, rules drawing, numbers counting up) rather
than from a photo. Pure typography, deep indigo background, the most premium-
feeling free option for "stop scroll" social video.

The HTML page should:
- include a `<script>` that sets `window.__GHOST_DONE = true` when the animation
  is complete (the recorder uses this to know when to stop). If absent, the
  recorder runs for the full --duration.
- use the brand fonts from Google Fonts (Oranienbaum + Manrope)
- size content to the target viewport — recorder uses --aspect to pick dims

Usage:
    python scripts/render_animated.py --html ad.html --out ad.mp4 --aspect 9:16 --duration 8
"""

from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path

# Bundle ffmpeg via imageio-ffmpeg so we don't require a system install
import imageio_ffmpeg
os.environ.setdefault("IMAGEIO_FFMPEG_EXE", imageio_ffmpeg.get_ffmpeg_exe())
FFMPEG_EXE = imageio_ffmpeg.get_ffmpeg_exe()

from _common import REPO_ROOT, inject_ghost_asset_urls, normalize_aspect


ASPECT_TO_DIMS = {
    "1:1":  (1080, 1080),
    "4:5":  (1080, 1350),
    "9:16": (1080, 1920),
    "16:9": (1920, 1080),
}


def record(html_path: Path, out_path: Path, *, aspect: str, duration: float, fps: int = 30) -> None:
    from playwright.sync_api import sync_playwright

    aspect = normalize_aspect(aspect)
    width, height = ASPECT_TO_DIMS.get(aspect, ASPECT_TO_DIMS["1:1"])
    out_path.parent.mkdir(parents=True, exist_ok=True)

    # Playwright records to WebM. We transcode to MP4 with the bundled ffmpeg.
    record_dir = out_path.parent / ".ghost-recording"
    record_dir.mkdir(parents=True, exist_ok=True)

    with sync_playwright() as p:
        browser = p.chromium.launch(args=["--autoplay-policy=no-user-gesture-required"])
        context = browser.new_context(
            viewport={"width": width, "height": height},
            device_scale_factor=1,
            record_video_dir=str(record_dir),
            record_video_size={"width": width, "height": height},
        )
        page = context.new_page()
        page.goto(html_path.resolve().as_uri(), wait_until="networkidle")
        page.wait_for_timeout(int(duration * 1000))
        page.close()
        context.close()
        browser.close()

    # find the webm Playwright dropped
    webm_files = sorted(record_dir.glob("*.webm"), key=lambda p: p.stat().st_mtime, reverse=True)
    if not webm_files:
        raise RuntimeError("Playwright produced no .webm file")
    webm = webm_files[0]

    # transcode to MP4 (H.264) at the requested fps
    import subprocess
    cmd = [
        FFMPEG_EXE, "-y",
        "-i", str(webm),
        "-r", str(fps),
        "-c:v", "libx264",
        "-pix_fmt", "yuv420p",
        "-preset", "medium",
        "-crf", "20",
        "-movflags", "+faststart",
        str(out_path),
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        raise RuntimeError(f"ffmpeg failed: {result.stderr[-500:]}")

    # cleanup
    try:
        webm.unlink()
        record_dir.rmdir()
    except OSError:
        pass


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Record CSS-animated HTML pages as MP4.")
    parser.add_argument("--slug", help="Proposal slug — bulk: render every Tool=animated-html concept")
    parser.add_argument("--concept", action="append", help="Specific concept id(s) in bulk mode")
    parser.add_argument("--html", help="Single mode: path to HTML")
    parser.add_argument("--out", help="Single mode: MP4 path")
    parser.add_argument("--aspect", default="9:16", choices=list(ASPECT_TO_DIMS.keys()))
    parser.add_argument("--duration", type=float, default=8.0)
    parser.add_argument("--fps", type=int, default=30)
    parser.add_argument("--overwrite", action="store_true")
    return parser.parse_args()


def _field(concept, key: str, default=None):
    import re
    m = re.search(rf"^\*\*{re.escape(key)}:\*\*\s*(.+)$", concept.raw_body, re.MULTILINE)
    if not m:
        return default
    return m.group(1).strip().strip("`")


def bulk_record(slug: str, selected_ids, default_aspect: str, default_duration: float, fps: int, overwrite: bool) -> int:
    from _common import parse_concepts, proposal_paths
    proposal_dir, prompts_path, assets_dir = proposal_paths(slug)
    if not prompts_path.exists():
        print(f"Prompts not found: {prompts_path}", file=sys.stderr)
        return 1
    concepts = parse_concepts(prompts_path.read_text(encoding="utf-8"))
    targets = [c for c in concepts if "animated-html" in c.tool.lower()
               and (not selected_ids or c.concept_id in selected_ids)]
    if not targets:
        print("No animated-html concepts matched.")
        return 0

    failures = 0
    print(f"Recording {len(targets)} animated HTML concept(s) for slug '{slug}'\n")
    for concept in targets:
        out_name = concept.suggested_filename
        if not out_name.lower().endswith(".mp4"):
            out_name = Path(out_name).with_suffix(".mp4").name
        out_path = assets_dir / out_name

        try:
            duration = float(_field(concept, "Duration", default_duration))
        except (TypeError, ValueError):
            duration = default_duration
        aspect = _field(concept, "Aspect", default_aspect) or default_aspect

        # write the HTML to a temp file alongside the asset for reproducibility
        html_dir = proposal_dir / "editorial"
        html_dir.mkdir(parents=True, exist_ok=True)
        html_path = html_dir / f"{Path(out_name).stem}.html"
        html_path.write_text(inject_ghost_asset_urls(concept.prompt, assets_dir), encoding="utf-8")

        print(f"[{concept.concept_id}] {concept.name}")
        print(f"  html:     {html_path.name}")
        print(f"  aspect:   {aspect}  duration={duration}s")
        print(f"  output:   {out_path}")

        if out_path.exists() and not overwrite:
            print("  - skipped (exists; use --overwrite)")
            continue

        try:
            record(html_path, out_path, aspect=aspect, duration=duration, fps=fps)
            print(f"  - saved ({out_path.stat().st_size // 1024} KB)")
        except Exception as exc:  # noqa: BLE001
            failures += 1
            print(f"  - failed: {exc}", file=sys.stderr)

    if failures:
        print(f"\nCompleted with {failures} failure(s).", file=sys.stderr)
        return 1
    print("\nAll requested animated-HTML videos rendered.")
    return 0


def main() -> int:
    args = parse_args()

    if args.slug:
        selected_ids = {c.zfill(2) for c in args.concept} if args.concept else None
        return bulk_record(args.slug, selected_ids, args.aspect, args.duration, args.fps, args.overwrite)

    if not (args.html and args.out):
        print("Provide --slug (bulk) or --html + --out (single).", file=sys.stderr)
        return 1

    html_path = Path(args.html)
    if not html_path.is_absolute():
        html_path = REPO_ROOT / html_path
    if not html_path.exists():
        print(f"HTML not found: {html_path}", file=sys.stderr)
        return 1

    out_path = Path(args.out)
    if not out_path.is_absolute():
        out_path = REPO_ROOT / out_path

    assets_dir = out_path.parent
    injected = inject_ghost_asset_urls(html_path.read_text(encoding="utf-8"), assets_dir)
    tmp = out_path.parent / f".ghost-animated-src-{html_path.stem}.html"
    tmp.write_text(injected, encoding="utf-8")
    print(f"HTML:     {html_path}")
    print(f"Aspect:   {args.aspect}  duration={args.duration}s")
    print(f"Output:   {out_path}")

    try:
        record(tmp, out_path, aspect=args.aspect, duration=args.duration, fps=args.fps)
    except Exception as exc:  # noqa: BLE001
        print(f"Failed: {exc}", file=sys.stderr)
        return 1
    finally:
        try:
            tmp.unlink(missing_ok=True)
        except OSError:
            pass
    print(f"Saved -> {out_path}  ({out_path.stat().st_size // 1024} KB)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
