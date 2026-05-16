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
SKIP_PARTS = {".ghost-recording"}


def default_export_root() -> Path:
    return Path.home() / "Desktop" / "Ghost Research Exports"


def collect_media(assets_dir: Path) -> list[Path]:
    out: list[Path] = []
    if not assets_dir.is_dir():
        return out
    for path in assets_dir.rglob("*"):
        if not path.is_file():
            continue
        if any(part in SKIP_PARTS for part in path.parts):
            continue
        if path.suffix.lower() not in MEDIA_SUFFIXES:
            continue
        out.append(path)
    return sorted(out, key=lambda p: p.name.lower())


def export_slug(slug: str, export_root: Path, *, overwrite: bool) -> tuple[int, int]:
    proposal_dir, _, assets_dir = proposal_paths(slug)
    if not proposal_dir.is_dir():
        print(f"[skip] unknown slug: {slug}")
        return 0, 0

    dest = export_root / slug
    if dest.exists() and overwrite:
        shutil.rmtree(dest)
    dest.mkdir(parents=True, exist_ok=True)

    files = collect_media(assets_dir)
    total_bytes = 0
    for src in files:
        target = dest / src.name
        shutil.copy2(src, target)
        total_bytes += src.stat().st_size
    return len(files), total_bytes


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Export Ghost Research campaign assets to Desktop (or --out).")
    p.add_argument("--slug", action="append", help="Campaign slug(s). Default: every folder under data/proposals/")
    p.add_argument(
        "--out",
        type=Path,
        help="Export root directory (default: Desktop/Ghost Research Exports)",
    )
    p.add_argument("--overwrite", action="store_true", help="Replace existing export folder contents")
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
            d.name for d in PROPOSALS_DIR.iterdir() if d.is_dir() and (d / "assets").is_dir()
        )

    print(f"Exporting to: {export_root}\n")
    grand_files = 0
    grand_bytes = 0
    for slug in slugs:
        n, b = export_slug(slug, export_root, overwrite=args.overwrite)
        if n:
            print(f"  {slug}: {n} file(s), {b // 1024 // 1024} MB")
        grand_files += n
        grand_bytes += b

    if not args.no_readme:
        readme = export_root / "README.txt"
        readme.write_text(
            f"Ghost Research — exported campaign assets\n"
            f"Exported: {datetime.now():%Y-%m-%d %H:%M}\n\n"
            f"Each subfolder is one campaign. Upload PNG/JPG/MP4 to your ad platforms.\n\n"
            f"Re-export from Ghost Research:\n"
            f"  python scripts/export_campaign_assets.py\n",
            encoding="utf-8",
        )

    print(f"\nDone — {grand_files} file(s), {grand_bytes // 1024 // 1024} MB total.")
    print(f"Open folder: {export_root}")
    return 0 if grand_files else 1


if __name__ == "__main__":
    raise SystemExit(main())
