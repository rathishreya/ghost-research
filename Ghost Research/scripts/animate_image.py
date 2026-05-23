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
import re
import sys
import tempfile
import textwrap
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


def _font_paths() -> tuple[Path | None, Path | None, Path | None]:
    """Resolve brand fonts. Prefer bundled Ghost fonts in assets/fonts/, fall back to Windows fonts."""
    from _common import REPO_ROOT
    brand = REPO_ROOT / "assets" / "fonts"
    serif = brand / "Oranienbaum-Regular.ttf"
    manrope_var = brand / "Manrope-VariableFont_wght.ttf"
    if not serif.exists():
        serif = None
    if not manrope_var.exists():
        manrope_var = None

    # If brand fonts missing, fall back to Windows fonts so the script still runs.
    if serif is None or manrope_var is None:
        win = Path(os.environ.get("WINDIR", r"C:\Windows")) / "Fonts"
        if serif is None:
            for name in ("timesbd.ttf", "times.ttf"):
                p = win / name
                if p.exists():
                    serif = p
                    break
        if manrope_var is None:
            for name in ("arial.ttf", "segoeui.ttf"):
                p = win / name
                if p.exists():
                    manrope_var = p
                    break
    return serif, manrope_var, manrope_var


def _load_variable(path: Path, size: int, weight: int) -> "object":
    """Load a TTF, optionally setting a variable-axis weight if supported."""
    from PIL import ImageFont
    font = ImageFont.truetype(str(path), size)
    try:
        font.set_variation_by_axes([weight])
    except (AttributeError, OSError, ValueError):
        pass
    return font


def _wrap_to_width(draw, text: str, font, max_width: int) -> list[str]:
    """Greedy word-wrap by *pixel* width (not char count), so larger fonts wrap correctly."""
    lines: list[str] = []
    for paragraph in text.split("\n"):
        if not paragraph.strip():
            continue
        words = paragraph.split()
        if not words:
            continue
        current = words[0]
        for w in words[1:]:
            trial = f"{current} {w}"
            tb = draw.textbbox((0, 0), trial, font=font)
            if (tb[2] - tb[0]) <= max_width:
                current = trial
            else:
                lines.append(current)
                current = w
        lines.append(current)
    return lines


def _draw_wrapped(
    draw,
    text: str,
    *,
    font,
    x: int,
    y: int,
    max_width: int,
    line_gap: int,
) -> int:
    """Return next y after drawing wrapped lines."""
    if not text.strip():
        return y
    lines: list[str] = []
    for para in text.split("\n"):
        lines.extend(textwrap.wrap(para, width=42) if len(para) > 42 else ([para] if para else []))
    cy = y
    for line in lines:
        draw.text((x, cy), line, font=font, fill=(248, 248, 255, 255))
        bbox = draw.textbbox((x, cy), line, font=font)
        cy = bbox[3] + line_gap
    return cy


def _draw_logo_mark(draw, x: int, y: int, size: int) -> None:
    """Paint the Ghost Research icon mark (red rounded-square + white inset circle).

    MANDATORY on every creative — sits in top-left of every frame, never fades.
    Matches `Ghost Research/assets/brand/logo-mark.svg`.
    """
    corner_radius = int(size * 0.22)
    draw.rounded_rectangle(
        (x, y, x + size, y + size),
        radius=corner_radius,
        fill=(239, 68, 68, 255),
    )
    circle_radius = int(size * 0.19)
    cx, cy = x + size // 2, y + size // 2
    draw.ellipse(
        (cx - circle_radius, cy - circle_radius, cx + circle_radius, cy + circle_radius),
        fill=(255, 255, 255, 255),
    )


def build_text_overlay_png(width: int, height: int, headline: str, sub: str, cta: str,
                           *, eyebrow: str = "GHOST RESEARCH",
                           brand_mark: str = "Ghost Research.") -> Path:
    """Full-frame RGBA PNG: dark lower scrim + eyebrow + serif headline + sub + pill CTA.

    Designed for 1080x1920 9:16, scales reasonably for 1:1 / 16:9 / 4:5.
    Brand-locked: Oranienbaum serif (headline), Manrope (eyebrow + body + CTA),
    accent red #EF4444 button, MANDATORY Ghost icon mark in top-left
    (red rounded-square with white inset circle — see assets/brand/logo-mark.svg).
    """
    from PIL import Image, ImageDraw

    img = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    serif_p, manrope_p, _ = _font_paths()

    # Size everything off the short edge so 1:1 and 9:16 both look right.
    short_edge = min(width, height)
    head_size = int(short_edge * 0.082)       # ~88px on 1080
    sub_size = int(short_edge * 0.030)        # ~32px
    eyebrow_size = int(short_edge * 0.020)    # ~22px
    cta_size = int(short_edge * 0.030)        # ~32px
    brand_size = int(short_edge * 0.024)      # ~26px

    if serif_p and manrope_p:
        font_h = _load_variable(serif_p, head_size, 400)
        font_e = _load_variable(manrope_p, eyebrow_size, 600)
        font_s = _load_variable(manrope_p, sub_size, 400)
        font_c = _load_variable(manrope_p, cta_size, 800)
        font_b = _load_variable(manrope_p, brand_size, 700)
    else:
        from PIL import ImageFont
        font_h = font_e = font_s = font_c = font_b = ImageFont.load_default()

    # Lower scrim: gradient from transparent to deep ink so text reads.
    # Stronger ramp so light photos don't bleed through and kill text contrast.
    bar_h = int(height * 0.62)
    y0 = height - bar_h
    for row in range(bar_h):
        y = y0 + row
        t = row / max(1, bar_h - 1)
        # Steeper curve + higher peak: empty at top, ~99% solid at bottom.
        a = int(255 * (t ** 1.3) * 0.99)
        draw.line([(0, y), (width, y)], fill=(6, 6, 45, a))
    # Solid floor: bottom 18% is near-fully opaque so CTA + spec line read on any photo.
    floor_h = int(height * 0.18)
    draw.rectangle((0, height - floor_h, width, height), fill=(6, 6, 45, 245))

    # Top-left brand mark — MANDATORY icon (red rounded-square with white circle).
    # Lives on every frame from 0s to last, never fades. The text wordmark is gone —
    # the icon mark IS the brand mark now (per 2026-05-20 brand directive).
    margin = int(short_edge * 0.052)
    logo_size = int(short_edge * 0.095)        # ~103px on 1080 short edge
    # subtle dark scrim behind the badge zone so the mark reads on bright photos
    scrim_pad = int(short_edge * 0.022)
    draw.rectangle((0, 0, width, margin + logo_size + scrim_pad),
                   fill=(6, 6, 45, 80))
    _draw_logo_mark(draw, margin, margin, logo_size)

    # ---- body block ----
    inner_w = width - 2 * margin
    x = margin
    y = y0 + int(height * 0.04)

    # Eyebrow (UPPERCASE, letter-spaced look via tracking emulation: drawing twice with extra char-space).
    eb = (eyebrow or "").strip().upper()
    if eb:
        # accent red eyebrow
        draw.text((x, y), eb, font=font_e, fill=(239, 68, 68, 255), spacing=0)
        ytb = draw.textbbox((x, y), eb, font=font_e)
        y = ytb[3] + int(short_edge * 0.018)

    # Headline (Oranienbaum, big, with strong drop shadow for legibility over any photo).
    head_lines = _wrap_to_width(draw, headline.strip(), font_h, inner_w)
    line_gap_h = int(head_size * 0.05)
    for line in head_lines:
        # multi-pass drop shadow: wider soft blur + tight hard shadow
        for dx, dy, alpha in ((6, 6, 220), (4, 4, 200), (2, 2, 180)):
            draw.text((x + dx, y + dy), line, font=font_h, fill=(0, 0, 0, alpha))
        draw.text((x, y), line, font=font_h, fill=(248, 248, 255, 255))
        bb = draw.textbbox((x, y), line, font=font_h)
        y = bb[3] + line_gap_h
    y += int(short_edge * 0.015)

    # Thin accent rule
    rule_w = int(short_edge * 0.06)
    rule_h = max(2, int(short_edge * 0.004))
    draw.rectangle((x, y, x + rule_w, y + rule_h), fill=(239, 68, 68, 255))
    y += int(short_edge * 0.025)

    # Sub
    sub_lines = _wrap_to_width(draw, sub.strip(), font_s, inner_w)
    line_gap_s = int(sub_size * 0.30)
    for line in sub_lines:
        # stronger shadow on sub too
        for dx, dy, alpha in ((4, 4, 200), (2, 2, 170)):
            draw.text((x + dx, y + dy), line, font=font_s, fill=(0, 0, 0, alpha))
        draw.text((x, y), line, font=font_s, fill=(232, 232, 245, 252))
        bb = draw.textbbox((x, y), line, font=font_s)
        y = bb[3] + line_gap_s
    y += int(short_edge * 0.028)

    # CTA pill with arrow.
    cta_label = cta.strip() or "Read the brief"
    arrow = "  →"
    cta_text = cta_label + arrow
    pad_x = int(short_edge * 0.030)
    pad_y = int(short_edge * 0.018)
    radius = int(short_edge * 0.010)
    ctb = draw.textbbox((0, 0), cta_text, font=font_c)
    tw, th = ctb[2] - ctb[0], ctb[3] - ctb[1]
    bx0, by0 = x, y
    bx1, by1 = bx0 + tw + 2 * pad_x, by0 + th + 2 * pad_y
    # button shadow
    shadow_pad = int(short_edge * 0.006)
    draw.rounded_rectangle(
        (bx0 + shadow_pad, by0 + shadow_pad, bx1 + shadow_pad, by1 + shadow_pad),
        radius=radius, fill=(0, 0, 0, 110),
    )
    draw.rounded_rectangle(
        (bx0, by0, bx1, by1),
        radius=radius, fill=(239, 68, 68, 255),
    )
    draw.text((bx0 + pad_x, by0 + pad_y - int(th * 0.15)), cta_text,
              font=font_c, fill=(255, 255, 255, 255))

    tmp = tempfile.NamedTemporaryFile(suffix=".png", delete=False)
    img.save(tmp.name)
    return Path(tmp.name)


def make_video(input_image: Path, output_path: Path, *,
               aspect: str, duration: float, motion: str, fps: int = 30,
               overlay: tuple[str, str, str] | tuple[str, str, str, str] | None = None) -> None:
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

    layers: list = [bg, clip]
    overlay_path: Path | None = None
    if overlay and any(str(x).strip() for x in overlay):
        # overlay may be (h, s, c) or (h, s, c, eyebrow)
        if len(overlay) == 4:
            h, s, c, eb = (str(x).strip() for x in overlay)
        else:
            h, s, c = (str(x).strip() for x in overlay[:3])
            eb = ""
        if h or s or c:
            overlay_path = build_text_overlay_png(
                width, height, h, s, c,
                eyebrow=eb or "GHOST RESEARCH",
            )
            from moviepy import ImageClip
            ov = ImageClip(str(overlay_path)).with_duration(duration)
            layers.append(ov)

    final = CompositeVideoClip(layers, size=(width, height)).with_duration(duration)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    try:
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
    finally:
        if overlay_path and overlay_path.exists():
            try:
                overlay_path.unlink()
            except OSError:
                pass


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
    m = re.search(rf"^\*\*{re.escape(key)}:\*\*\s*(.+)$", concept.raw_body, re.MULTILINE)
    if not m:
        return default
    return m.group(1).strip().strip("`")


def _overlay_from_concept(concept) -> tuple[str, str, str, str] | None:
    h = _field(concept, "On-screen headline", None)
    s = _field(concept, "On-screen sub", None)
    c = _field(concept, "On-screen CTA", None)
    e = _field(concept, "On-screen eyebrow", None)
    if h is None and s is None and c is None:
        return None
    return (h or "", s or "", c or "", e or "GHOST RESEARCH")


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
    targets.sort(key=lambda c: int(c.concept_id))
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
            skip_flag = (_field(concept, "Skip if source missing", "") or "").lower()
            if skip_flag in ("yes", "true", "1", "y"):
                print(
                    f"[{concept.concept_id}] {concept.name} — skipped (no source yet; "
                    f"add the file named in **Source image:** or generate upstream stills, then re-run).",
                    flush=True,
                )
                continue
            failures += 1
            print(f"[{concept.concept_id}] {concept.name} - SKIPPED (no source image at {in_path})", file=sys.stderr)
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
            ov = _overlay_from_concept(concept)
            make_video(
                in_path, out_path, aspect=aspect, duration=duration, motion=motion, fps=fps, overlay=ov
            )
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
