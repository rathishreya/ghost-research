#!/usr/bin/env python3
"""Build a multi-shot edited Reels MP4 by cross-dissolving Ken-Burns clips.

Pure-Python pipeline: Pillow + moviepy + bundled ffmpeg. No After Effects.

Takes a list of source images, animates each as a 2-second Ken-Burns clip,
cross-fades them together with a final text-reveal frame, and exports MP4.

Usage:
    python scripts/edit_multishot_reels.py \
        --slug cfo-defense-pack-q2-2026 \
        --clips P4-empty-boardroom.jpg,P3-sensitivity-chart.jpg,P2-window-executive.jpg,P8-hero-finale.jpg \
        --out  C16-multishot.mp4 \
        --headline "The receipts are in." \
        --sub "1,047 audited deployments. 8 survived diligence." \
        --cta "Read the pack — $500" \
        --aspect 9:16 \
        --clip-duration 2.0 \
        --crossfade 0.6
"""

from __future__ import annotations

import argparse
import os
import sys
import tempfile
from pathlib import Path

import imageio_ffmpeg

os.environ.setdefault("IMAGEIO_FFMPEG_EXE", imageio_ffmpeg.get_ffmpeg_exe())
os.environ.setdefault("FFMPEG_BINARY", imageio_ffmpeg.get_ffmpeg_exe())

from _common import REPO_ROOT, normalize_aspect, proposal_paths
from animate_image import build_text_overlay_png, make_video, ASPECT_TO_DIMS


def render_kenburns_clip(input_image: Path, out_path: Path, *, aspect: str,
                         duration: float, motion: str, fps: int = 30,
                         overlay: tuple[str, str, str, str] | None = None) -> None:
    """Render a single Ken-Burns clip, optionally with a persistent text overlay (headline+sub+cta+eyebrow)."""
    make_video(input_image, out_path, aspect=aspect, duration=duration,
               motion=motion, fps=fps, overlay=overlay)


def build_text_card_clip(width: int, height: int, *,
                         headline: str, sub: str, cta: str,
                         duration: float, fps: int, out_path: Path) -> None:
    """Render a final text-card MP4 — black background + animated reveal."""
    from PIL import Image
    from moviepy import ImageClip, ColorClip, CompositeVideoClip, vfx

    overlay = build_text_overlay_png(width, height, headline, sub, cta,
                                     eyebrow="GHOST RESEARCH")

    bg = ColorClip(size=(width, height), color=(6, 6, 45)).with_duration(duration)
    text_clip = ImageClip(str(overlay)).with_duration(duration)
    text_clip = text_clip.with_effects([vfx.FadeIn(0.5), vfx.FadeOut(0.4)])

    final = CompositeVideoClip([bg, text_clip], size=(width, height)).with_duration(duration)
    final.write_videofile(str(out_path), fps=fps, codec="libx264", bitrate="6M",
                          audio=False, threads=4, preset="medium", logger=None)


def crossfade_concat(clip_paths: list[Path], out_path: Path, *,
                     crossfade: float, fps: int) -> None:
    """Concatenate clips with cross-dissolve transitions using ffmpeg xfade filter."""
    import subprocess
    FFMPEG = imageio_ffmpeg.get_ffmpeg_exe()

    if len(clip_paths) < 2:
        # Single clip — just copy
        subprocess.run([FFMPEG, "-y", "-i", str(clip_paths[0]), "-c", "copy", str(out_path)], check=True)
        return

    # Build the filter_complex chain.
    # Inputs:  [0:v][1:v][2:v]...[N:v]
    # Need offsets accumulating: first xfade at (dur0 - crossfade), then (dur0+dur1-2*crossfade), etc.
    # Probe durations.
    durations: list[float] = []
    for p in clip_paths:
        result = subprocess.run([FFMPEG, "-i", str(p)], capture_output=True, text=True)
        # ffmpeg writes duration to stderr "Duration: HH:MM:SS.ss"
        for line in result.stderr.splitlines():
            if "Duration:" in line:
                token = line.split("Duration:")[1].split(",")[0].strip()
                h, m, s = token.split(":")
                durations.append(int(h) * 3600 + int(m) * 60 + float(s))
                break

    parts: list[str] = []
    cum = 0.0
    last_label = "0:v"
    for i in range(1, len(clip_paths)):
        offset = cum + durations[i - 1] - crossfade
        cum = offset
        new_label = f"v{i}"
        parts.append(
            f"[{last_label}][{i}:v]xfade=transition=fade:duration={crossfade}:offset={offset:.3f}[{new_label}]"
        )
        last_label = new_label

    filter_complex = ";".join(parts)
    cmd = [FFMPEG, "-y"]
    for p in clip_paths:
        cmd.extend(["-i", str(p)])
    cmd.extend([
        "-filter_complex", filter_complex,
        "-map", f"[{last_label}]",
        "-c:v", "libx264",
        "-pix_fmt", "yuv420p",
        "-r", str(fps),
        "-preset", "medium",
        "-crf", "20",
        "-movflags", "+faststart",
        str(out_path),
    ])
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        raise RuntimeError(f"ffmpeg xfade failed: {result.stderr[-800:]}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Multi-shot cross-dissolve Reels.")
    parser.add_argument("--slug", required=True, help="Proposal slug")
    parser.add_argument("--clips", required=True, help="Comma-separated source image filenames in assets/")
    parser.add_argument("--out", required=True, help="Output MP4 filename (relative to assets/)")
    parser.add_argument("--aspect", default="9:16", choices=list(ASPECT_TO_DIMS.keys()))
    parser.add_argument("--clip-duration", type=float, default=2.0, help="Seconds per Ken-Burns clip")
    parser.add_argument("--crossfade", type=float, default=0.6, help="Cross-dissolve duration (sec)")
    parser.add_argument("--final-duration", type=float, default=2.0, help="Seconds for the final text card")
    parser.add_argument("--headline", required=True)
    parser.add_argument("--sub", default="")
    parser.add_argument("--cta", default="Read the pack — $500")
    parser.add_argument("--fps", type=int, default=30)
    return parser.parse_args()


MOTIONS = ["zoom-in", "pan-right", "zoom-out", "pan-left"]


def main() -> int:
    args = parse_args()
    proposal_dir, prompts_path, assets_dir = proposal_paths(args.slug)
    aspect = normalize_aspect(args.aspect, for_video=True)
    width, height = ASPECT_TO_DIMS[aspect]

    clip_names = [c.strip() for c in args.clips.split(",") if c.strip()]
    if len(clip_names) < 2:
        print("Need at least 2 clips for cross-dissolve.", file=sys.stderr)
        return 1

    # Validate sources
    src_paths: list[Path] = []
    for name in clip_names:
        p = assets_dir / name
        if not p.exists():
            print(f"Source image missing: {p}", file=sys.stderr)
            return 1
        src_paths.append(p)

    out_path = assets_dir / args.out
    print(f"Building multi-shot Reels:")
    print(f"  aspect:   {aspect} ({width}x{height})")
    print(f"  clips:    {len(src_paths)} sources × {args.clip_duration}s + {args.final_duration}s text card")
    print(f"  crossfade: {args.crossfade}s")
    print(f"  output:   {out_path}")
    print()

    # Build persistent overlay tuple — applied to every Ken-Burns clip so text is on every frame
    overlay_tuple = (args.headline, args.sub, args.cta, "GHOST RESEARCH")

    tmpdir = Path(tempfile.mkdtemp(prefix="ghost-multishot-"))
    try:
        clip_paths: list[Path] = []
        # Ken-Burns clips — now with persistent headline+sub+cta+eyebrow overlay on every frame
        for i, src in enumerate(src_paths):
            motion = MOTIONS[i % len(MOTIONS)]
            clip_path = tmpdir / f"clip-{i:02d}.mp4"
            print(f"  [{i+1}/{len(src_paths)+1}] {src.name} -> {motion}, {args.clip_duration}s (with persistent overlay)")
            render_kenburns_clip(src, clip_path, aspect=aspect, duration=args.clip_duration,
                                 motion=motion, fps=args.fps, overlay=overlay_tuple)
            clip_paths.append(clip_path)

        # Final text card
        text_path = tmpdir / f"clip-text.mp4"
        print(f"  [{len(src_paths)+1}/{len(src_paths)+1}] final text card, {args.final_duration}s")
        build_text_card_clip(width, height, headline=args.headline, sub=args.sub, cta=args.cta,
                             duration=args.final_duration, fps=args.fps, out_path=text_path)
        clip_paths.append(text_path)

        # Cross-dissolve concat
        print(f"\n  cross-dissolving {len(clip_paths)} clips with {args.crossfade}s xfade...")
        out_path.parent.mkdir(parents=True, exist_ok=True)
        crossfade_concat(clip_paths, out_path, crossfade=args.crossfade, fps=args.fps)
    finally:
        # Cleanup
        for p in tmpdir.glob("*"):
            try: p.unlink()
            except OSError: pass
        try: tmpdir.rmdir()
        except OSError: pass

    print(f"\nSaved -> {out_path}  ({out_path.stat().st_size // 1024} KB)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
