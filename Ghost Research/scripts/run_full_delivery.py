#!/usr/bin/env python3
"""Full media delivery for one proposal slug: raster images + MP4 outputs.

Pins ``Ghost Research/`` as cwd for every subprocess regardless of caller location.

Tier ``market`` (default):
  • ``GEMINI_API_KEY`` → Imagen 4 Ultra for Tool=pollinations (and aliases) raster stills,
    plus editorial HTML renders, optional NanoBanana REST, then motion (Ken-Burns + animated-html).
  • No Google key → falls back to Pollinations ``flux-realism`` with a stderr notice.

Tier ``free``:
  • Pollinations + editorial (same as ``generate_proposal_assets.py`` without ``--premium``).

Optional ``--veo``: run ``gemini_video.py`` for Tool=``veo`` concepts (paid quota / billing).

Run after Claude has produced ``data/proposals/<slug>/prompts.md``.
"""

from __future__ import annotations

import argparse
import os
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = REPO_ROOT / "scripts"


def load_dotenv(path: Path) -> None:
    if not path.exists():
        return
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        key = key.strip()
        value = value.strip().strip('"').strip("'")
        os.environ.setdefault(key, value)


def run(argv: list[str], *, env: dict[str, str]) -> int:
    print("\n>>> " + " ".join(argv), flush=True)
    return subprocess.run(
        [sys.executable, *argv],
        cwd=str(REPO_ROOT),
        env=env,
    ).returncode


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(
        description="End-to-end still + motion generation for Ghost Research proposals.",
    )
    p.add_argument("--slug", required=True, help="Proposal slug under data/proposals/")
    p.add_argument(
        "--tier",
        choices=("market", "free"),
        default="market",
        help="'market' = Imagen 4 Ultra raster stills when GEMINI_API_KEY is set "
        "(else Pollinations). 'free' = Pollinations flux-realism only.",
    )
    p.add_argument(
        "--veo",
        action="store_true",
        help="Also run Google Veo 3 Fast for veo-tool rows (consumes paid Google AI Studio quota).",
    )
    p.add_argument("--overwrite", action="store_true")
    p.add_argument("--dry-run", action="store_true")
    return p.parse_args()


def main() -> int:
    load_dotenv(REPO_ROOT / ".env")
    args = parse_args()

    env = os.environ.copy()
    ext: list[str] = [str(SCRIPTS / "generate_proposal_assets.py"), "--slug", args.slug]
    if args.tier == "market":
        ext.append("--premium")
    if args.overwrite:
        ext.append("--overwrite")
    if args.dry_run:
        ext.append("--dry-run")

    codes: list[int] = []
    codes.append(run(ext, env=env))

    if args.dry_run:
        print(
            "\n[dry-run] Skipping animate_image.py and render_animated.py "
            "(no --dry-run support; stills would not exist yet).",
            flush=True,
        )
    else:
        vid_shared: list[str] = ["--slug", args.slug]
        if args.overwrite:
            vid_shared.append("--overwrite")

        codes.append(run([str(SCRIPTS / "animate_image.py"), *vid_shared], env=env))
        codes.append(run([str(SCRIPTS / "render_animated.py"), *vid_shared], env=env))

    if args.veo:
        veo_argv = [str(SCRIPTS / "gemini_video.py"), "--slug", args.slug]
        if args.overwrite:
            veo_argv.append("--overwrite")
        if args.dry_run:
            veo_argv.append("--dry-run")
        codes.append(run(veo_argv, env=env))

    assets = REPO_ROOT / "data" / "proposals" / args.slug / "assets"

    if any(c != 0 for c in codes):
        print(f"\nDelivery finished with failures. Inspect stderr and: {assets}", file=sys.stderr)
        return 1

    print(f"\nDeliverables folder: {assets}", flush=True)
    print("(Open JPG/PNG/MP4 files here - these are production outputs.)", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
