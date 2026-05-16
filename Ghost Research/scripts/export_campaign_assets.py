#!/usr/bin/env python3
"""Copy publishable images/videos from proposal assets/ to a folder on your Desktop.

Default output: ~/Desktop/Ghost Research Exports/<slug>/...

Usage:
    python scripts/export_campaign_assets.py
    python scripts/export_campaign_assets.py --slug cfo-defense-pack-q2-2026
    python scripts/export_campaign_assets.py --out "D:/My Exports"
"""

from __future__ import annotations

import argparse
import shutil
from datetime import datetime
from pathlib import Path

from _common import PROPOSALS_DIR, proposal_paths

MEDIA_SUFFIXES = {".jpg", ".jpeg", ".png", ".gif", ".webp", ".mp4", ".mov", ".webm"}
VIDEO_SUFFIXES = {".mp4", ".mov", ".webm"}
SKIP_PARTS = {".ghost-recording", "__pycache__"}
SKIP_SLUGS = {"does-not-exist-xyz", "test-smoke"}


def default_export_root() -> Path:
    return Path.home() / "Desktop" / "Ghost Research Exports"


def collect_media(root: Path, *, videos_only: bool = False) -> list[Path]:
    """Collect publishable media under a proposal folder (assets/, lux/, etc.)."""
    out: list[Path] = []
    if not root.is_dir():
        return out
    allowed = VIDEO_SUFFIXES if videos_only else MEDIA_SUFFIXES
    for path in root.rglob("*"):
        if not path.is_file():
            continue
        if any(part in SKIP_PARTS for part in path.parts):
            continue
        if path.suffix.lower() not in allowed:
            continue
        out.append(path)
    # Prefer shallower paths when same filename appears twice
    out.sort(key=lambda p: (p.name.lower(), len(p.parts)))
    seen: set[str] = set()
    deduped: list[Path] = []
    for p in out:
        if p.name.lower() in seen:
            continue
        seen.add(p.name.lower())
        deduped.append(p)
    return deduped


def export_slug(slug: str, export_root: Path, *, overwrite: bool) -> tuple[int, int, list[Path]]:
    proposal_dir, _, _ = proposal_paths(slug)
    if not proposal_dir.is_dir():
        print(f"[skip] unknown slug: {slug}")
        return 0, 0, []

    dest = export_root / slug
    if dest.exists() and overwrite:
        shutil.rmtree(dest)
    dest.mkdir(parents=True, exist_ok=True)

    files = collect_media(proposal_dir)
    total_bytes = 0
    videos: list[Path] = []
    for src in files:
        target = dest / src.name
        shutil.copy2(src, target)
        total_bytes += src.stat().st_size
        if src.suffix.lower() in VIDEO_SUFFIXES:
            videos.append(src)
    return len(files), total_bytes, videos


def export_all_videos_flat(export_root: Path, slug_videos: list[tuple[str, Path]], *, overwrite: bool) -> int:
    """Copy every MP4/MOV/WEBM into export_root/All-Videos/ with slug prefix."""
    flat = export_root / "All-Videos"
    if flat.exists() and overwrite:
        shutil.rmtree(flat)
    flat.mkdir(parents=True, exist_ok=True)
    count = 0
    for slug, src in slug_videos:
        # Keep subfolder hint when file lived outside assets/ (e.g. lux/LUX-4.mp4)
        rel = src.relative_to(proposal_paths(slug)[0])
        if rel.parent.name not in (slug, "assets"):
            prefix = f"{slug}__{rel.parent.name}__{src.name}"
        else:
            prefix = f"{slug}__{src.name}"
        target = flat / prefix
        shutil.copy2(src, target)
        count += 1
    return count


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Export Ghost Research campaign assets to Desktop (or --out).")
    p.add_argument("--slug", action="append", help="Campaign slug(s). Default: every folder under data/proposals/")
    p.add_argument(
        "--out",
        type=Path,
        help="Export root directory (default: Desktop/Ghost Research Exports)",
    )
    p.add_argument("--overwrite", action="store_true", help="Replace existing export folder contents")
    p.add_argument(
        "--videos-only",
        action="store_true",
        help="Only export MP4/MOV/WEBM (still builds All-Videos/ flat folder)",
    )
    p.add_argument(
        "--no-flat-videos",
        action="store_true",
        help="Skip creating All-Videos/ with every video in one place",
    )
    p.add_argument("--no-readme", action="store_true", help="Do not write README.txt in export root")
    return p.parse_args()


def main() -> int:
    args = parse_args()
    export_root = (args.out or default_export_root()).expanduser().resolve()
    export_root.mkdir(parents=True, exist_ok=True)

    if args.slug:
        slugs = args.slug
    else:
        slugs = sorted(
            d.name
            for d in PROPOSALS_DIR.iterdir()
            if d.is_dir() and d.name not in SKIP_SLUGS and (d / "assets").is_dir()
        )

    print(f"Exporting to: {export_root}\n")
    grand_files = 0
    grand_bytes = 0
    all_videos: list[tuple[str, Path]] = []
    for slug in slugs:
        if args.videos_only:
            proposal_dir, _, _ = proposal_paths(slug)
            vids = collect_media(proposal_dir, videos_only=True)
            dest = export_root / slug
            if dest.exists() and args.overwrite:
                shutil.rmtree(dest)
            dest.mkdir(parents=True, exist_ok=True)
            total_bytes = 0
            for src in vids:
                shutil.copy2(src, dest / src.name)
                total_bytes += src.stat().st_size
                all_videos.append((slug, src))
            n, b = len(vids), total_bytes
        else:
            n, b, vids = export_slug(slug, export_root, overwrite=args.overwrite)
            for src in vids:
                all_videos.append((slug, src))
        if n:
            vcount = sum(1 for s, _ in all_videos if s == slug)
            print(f"  {slug}: {n} file(s), {b // 1024 // 1024} MB ({vcount} video(s))")
        grand_files += n
        grand_bytes += b

    if not args.no_flat_videos and all_videos:
        flat_n = export_all_videos_flat(export_root, all_videos, overwrite=args.overwrite)
        print(f"\n  All-Videos/: {flat_n} MP4/MOV/WEBM in one folder (slug-prefixed names)")

    if not args.no_readme:
        readme = export_root / "README.txt"
        readme.write_text(
            f"Ghost Research — exported campaign assets\n"
            f"Exported: {datetime.now():%Y-%m-%d %H:%M}\n\n"
            f"Each subfolder is one campaign (images + videos).\n"
            f"All-Videos/ — every MP4/MOV/WEBM from all campaigns in one place.\n\n"
            f"Re-export from Ghost Research:\n"
            f"  python scripts/export_campaign_assets.py --overwrite\n",
            encoding="utf-8",
        )

    print(f"\nDone — {grand_files} file(s), {grand_bytes // 1024 // 1024} MB total.")
    print(f"Videos folder: {export_root / 'All-Videos'}")
    print(f"Open folder: {export_root}")
    return 0 if grand_files else 1


if __name__ == "__main__":
    raise SystemExit(main())
