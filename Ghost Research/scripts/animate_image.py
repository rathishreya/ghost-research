#!/usr/bin/env python3
"""Turn a static Ghost Research image into a premium-feel short video.

Free alternative to Veo / Runway. Uses subtle Ken-Burns-style motion
(slow zoom-in / zoom-out / pan) + cinematic fade-in / fade-out, optional
title-card freeze frames, and exports a 1080p MP4 you can paste into Reels /
Stories / Shorts.

This won't match Veo's photoreal motion — it intentionally mimics editorial
documentary cinematography (think NYT video op-eds), which is *on brand* for
Ghost Research.

Usage:
    python scripts/animate_image.py --input assets/concept-01.jpg --out assets/concept-01.mp4 \
        --aspect 9:16 --duration 8 --motion zoom-in

    python scripts/animate_image.py --slug ai-due-diligence --concept 01 \
        --duration 6 --motion pan-right

Motion presets:
    zoom-in     subject grows slowly larger (most premium-feeling default)
    zoom-out    starts tight, pulls back to reveal
    pan-right   slow horizontal drift right
    pan-left    slow horizontal drift left
    static      no motion (just fade in/out)
"""

from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path

# Make sure moviepy uses the bundled ffmpeg
import imageio_ffmpeg
os.environ.setdefault("IMAGEIO_FFMPEG_EXE", imageio_ffmpeg.get_ffmpeg_exe())
os.environ.setdefault("FFMPEG_BINARY", imageio_ffmpeg.get_ffmpeg_exe())

from _common import REPO_ROOT, parse_concepts, proposal_paths


ASPECT_TO_DIMS = {
    "1:1":  (1080, 1080),
    "4:5":  (1080, 1350),
    "9:16": (1080, 1920),
    "16:9": (1920, 1080),
    "4:3":  (1440, 1080),
}


def make_video(input_image: Path, output_path: Path, *,
               aspect: str, duration: float, motion: str, fps: int = 30) -> None:
    from moviepy import ImageClip, vfx

    width, height = ASPECT_TO_DIMS.get(aspect, ASPECT_TO_DIMS["1:1"])

    base = ImageClip(str(input_image)).with_duration(duration)

    # Resize / crop the source to fill the target aspect from the center
    src_w, src_h = base.size
    src_aspect = src_w / src_h
    target_aspect = width / height
    if src_aspect > target_aspect:
        # source is wider — fit height, crop sides
        scale = height / src_h
    else:
        # source is taller — fit width, crop top/bottom
        scale = width / src_w
    # Oversample 1.18x so we have room for motion without showing edges.
    over = 1.18
    fitted_w = int(src_w * scale * over)
    fitted_h = int(src_h * scale * over)
    base = base.resized(new_size=(fitted_w, fitted_h))

    # Compute motion as a position(t) function on a black canvas.
    from moviepy import ColorClip, CompositeVideoClip

    bg = ColorClip(size=(width, height), color=(6, 6, 45)).with_duration(duration)
    cx = (width - fitted_w) / 2
    cy = (height - fitted_h) / 2

    if motion == "zoom-in":
        def resize_factor(t):
            return 1.0 + 0.08 * (t / duration)  # 1.00 -> 1.08
        clip = base.resized(resize_factor).with_position("center")
    elif motion == "zoom-out":
        def resize_factor(t):
            return 1.08 - 0.08 * (t / duration)
        clip = base.resized(resize_factor).with_position("center")
    elif motion == "pan-right":
        drift = (fitted_w - width) * 0.6
        def pos(t):
            x = cx - drift / 2 + drift * (t / duration)
            return (x, cy)
        clip = base.with_position(pos)
    elif motion == "pan-left":
        drift = (fitted_w - width) * 0.6
        def pos(t):
            x = cx + drift / 2 - drift * (t / duration)
            return (x, cy)
        clip = base.with_position(pos)
    else:  # static
        clip = base.with_position("center")

    # Fade in/out
    clip = clip.with_effects([vfx.FadeIn(0.4), vfx.FadeOut(0.4)])

    final = CompositeVideoClip([bg, clip], size=(width, height)).with_duration(duration)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    final.write_videofile(
        str(output_path),
        fps=fps,
        codec="libx264",
        bitrate="6M",
        audio=False,
        threads=4,
        preset="medium",
        logger=None,
    )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Animate Ghost Research static images into short cinematic MP4s.")
    parser.add_argument("--input", help="Image path (single mode)")
    parser.add_argument("--out", help="MP4 output (single mode)")
    parser.add_argument("--slug", help="Proposal slug — bulk: animate every Tool=animate concept")
    parser.add_argument("--concept", action="append", help="Specific concept id(s) in bulk mode")
    parser.add_argument("--aspect", default="9:16", choices=list(ASPECT_TO_DIMS.keys()))
    parser.add_argument("--duration", type=float, default=8.0, help="Seconds (default 8)")
    parser.add_argument("--motion", default=None,
                        choices=[None, "zoom-in", "zoom-out", "pan-right", "pan-left", "static"])
    parser.add_argument("--fps", type=int, default=30)
    parser.add_argument("--overwrite", action="store_true")
    return parser.parse_args()


def _field(concept, key: str, default=None):
    # find a field like **Motion:** ... in the raw body
    import re
    m = re.search(rf"^\*\*{re.escape(key)}:\*\*\s*(.+)$", concept.raw_body, re.MULTILINE)
    return m.group(1).strip() if m else default


def bulk_animate(slug: str, selected_ids: set[str] | None,
                 default_aspect: str, default_duration: float, default_motion: str | None,
                 fps: int, overwrite: bool) -> int:
    proposal_dir, prompts_path, assets_dir = proposal_paths(slug)
    if not prompts_path.exists():
        print(f"Prompts not found: {prompts_path}", file=sys.stderr)
        return 1
    concepts = parse_concepts(prompts_path.read_text(encoding="utf-8"))
    targets = [c for c in concepts
               if "animate" in c.tool.lower() and "animated-html" not in c.tool.lower()
               and (not selected_ids or c.concept_id in selected_ids)]
    if not targets:
        print("No animate concepts matched.")
        return 0

    failures = 0
    print(f"Animating {len(targets)} concept(s) for slug '{slug}'\n")
    for concept in targets:
        # find source image: prefer **Source image:** field, else use the concept's own suggested filename
        source_name = _field(concept, "Source image", concept.suggested_filename)
        source_name = source_name.strip().strip("`")
        in_path = assets_dir / source_name
        if not in_path.exists():
            matches = list(assets_dir.glob(f"{Path(source_name).stem}*"))
            matches = [m for m in matches if m.suffix.lower() in {".jpg", ".jpeg", ".png"}]
            if matches:
                in_path = matches[0]
        if not in_path.exists():
            failures += 1
            print(f"[{concept.concept_id}] {concept.name} — SKIPPED (no source image at {in_path})", file=sys.stderr)
            continue

        out_name = concept.suggested_filename
        if not out_name.lower().endswith(".mp4"):
            out_name = Path(out_name).with_suffix(".mp4").name
        out_path = assets_dir / out_name

        motion = (_field(concept, "Motion", default_motion) or "zoom-in").lower()
        if motion not in {"zoom-in", "zoom-out", "pan-right", "pan-left", "static"}:
            motion = "zoom-in"
        try:
            duration = float(_field(concept, "Duration", default_duration))
        except (TypeError, ValueError):
            duration = default_duration
        aspect = _field(concept, "Aspect", default_aspect) or default_aspect

        print(f"[{concept.concept_id}] {concept.name}")
        print(f"  source: {in_path.name}")
        print(f"  motion: {motion}  duration={duration}s  aspect={aspect}")
        print(f"  output: {out_path}")

        if out_path.exists() and not overwrite:
            print("  - skipped (exists; use --overwrite)")
            continue

        try:
            make_video(in_path, out_path, aspect=aspect, duration=duration, motion=motion, fps=fps)
            print(f"  - saved ({out_path.stat().st_size // 1024} KB)")
        except Exception as exc:  # noqa: BLE001
            failures += 1
            print(f"  - failed: {exc}", file=sys.stderr)

    if failures:
        print(f"\nCompleted with {failures} failure(s).", file=sys.stderr)
        return 1
    print("\nAll requested animations rendered.")
    return 0


def main() -> int:
    args = parse_args()

    if args.slug:
        selected_ids = {c.zfill(2) for c in args.concept} if args.concept else None
        return bulk_animate(args.slug, selected_ids,
                            args.aspect, args.duration, args.motion, args.fps, args.overwrite)

    # Single-input mode
    if args.input:
        in_path = Path(args.input)
        if not in_path.is_absolute():
            in_path = REPO_ROOT / in_path
        if not in_path.exists():
            print(f"Input image missing: {in_path}", file=sys.stderr)
            return 1
        out_path = Path(args.out) if args.out else in_path.with_suffix(".mp4")
        if not out_path.is_absolute():
            out_path = REPO_ROOT / out_path
    else:
        print("Provide --slug (bulk) or --input/--out (single).", file=sys.stderr)
        return 1

    motion = args.motion or "zoom-in"
    print(f"Animating: {in_path}")
    print(f"Motion:    {motion}  duration={args.duration}s  aspect={args.aspect}")
    print(f"Output:    {out_path}")

    try:
        make_video(in_path, out_path, aspect=args.aspect,
                   duration=args.duration, motion=motion, fps=args.fps)
    except Exception as exc:  # noqa: BLE001
        print(f"Failed: {exc}", file=sys.stderr)
        return 1

    print(f"Saved -> {out_path}  ({out_path.stat().st_size // 1024} KB)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
