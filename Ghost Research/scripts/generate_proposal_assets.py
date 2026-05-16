#!/usr/bin/env python3
"""Single entrypoint for Ghost `/generate-assets` pipeline.

Runs Pollinations (or Imagen 4 Ultra when `--premium` + GEMINI_API_KEY),
editorial renders, and optional NanoBanana REST with cwd pinned to `Ghost Research/`.
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


def run_step(name: str, argv: list[str], *, env: dict[str, str]) -> int:
    print(f"\n=== {name} ===", flush=True)
    proc = subprocess.run(
        [sys.executable, *argv],
        cwd=str(REPO_ROOT),
        env=env,
    )
    return proc.returncode


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(
        description="Generate all static image assets for a proposal (Pollinations + editorial HTML).",
    )
    p.add_argument("--slug", required=True, help="Proposal slug under data/proposals/")
    p.add_argument("--concept", action="append", help="Limit to concept id(s), e.g. --concept 01")
    p.add_argument("--overwrite", action="store_true", help="Regenerate even if files exist")
    p.add_argument("--dry-run", action="store_true", help="Parse only; no network or browser")
    p.add_argument(
        "--premium",
        action="store_true",
        help=(
            "Market-quality stills: if GEMINI_API_KEY is set, use Imagen 4 Ultra for pollinations "
            "photo concepts (--routes-pollinations). Otherwise fall back to Pollinations.ai."
        ),
    )
    p.add_argument(
        "--pollinations-model",
        default="flux-realism",
        help="Pollinations model (default: flux-realism = photoreal B2B; use 'flux' for legacy behavior)",
    )
    p.add_argument(
        "--skip-pollinations",
        action="store_true",
        help="Raster only: skip Pollinations, Imagen, and NanoBanana (editorial-only pass).",
    )
    p.add_argument(
        "--skip-editorial",
        action="store_true",
        help="Only run Pollinations (debug).",
    )
    p.add_argument(
        "--import-pomelli-inbox",
        action="store_true",
        help=(
            "Run first: copy Pomelli exports from data/proposals/<slug>/pomelli-inbox/ "
            "into assets/ (see scripts/import_pomelli_exports.py). No API — file bridge only."
        ),
    )
    return p.parse_args()


def main() -> int:
    load_dotenv(REPO_ROOT / ".env")
    args = parse_args()

    env = os.environ.copy()
    shared: list[str] = ["--slug", args.slug]
    if args.concept:
        for c in args.concept:
            shared.extend(["--concept", c])
    if args.overwrite:
        shared.append("--overwrite")
    if args.dry_run:
        shared.append("--dry-run")

    codes: list[int] = []

    if args.import_pomelli_inbox:
        pom = [str(SCRIPTS / "import_pomelli_exports.py"), "--slug", args.slug, "--optional"]
        if args.overwrite:
            pom.append("--overwrite")
        if args.dry_run:
            pom.append("--dry-run")
        codes.append(run_step("Pomelli inbox → assets (import_pomelli_exports.py)", pom, env=env))

    use_imagen_stills = False
    if not args.skip_pollinations:
        if args.premium and os.environ.get("GEMINI_API_KEY"):
            gi = [
                str(SCRIPTS / "gemini_image.py"),
                *shared,
                "--quality",
                "ultra",
                "--routes-pollinations",
            ]
            gi_rc = run_step("Imagen 4 Ultra (Tool: pollinations + raster aliases)", gi, env=env)
            if gi_rc == 0:
                use_imagen_stills = True
            else:
                print(
                    "[warn] Imagen failed or your Google AI plan lacks Imagen. "
                    "Falling back to Pollinations.ai for photo concepts.",
                    file=sys.stderr,
                )
        elif args.premium:
            print(
                "[warn] --premium requested but GEMINI_API_KEY is not set - "
                "using Pollinations instead (good, not flagship). "
                "Add a key from https://aistudio.google.com/apikey\n",
                file=sys.stderr,
            )

    if not args.skip_pollinations and not use_imagen_stills:
        pi = [str(SCRIPTS / "pollinations_image.py"), *shared, "--model", args.pollinations_model]
        codes.append(run_step("Pollinations (FLUX image concepts)", pi, env=env))

    if not args.skip_editorial:
        ed = [str(SCRIPTS / "render_editorial.py"), *shared]
        codes.append(run_step("Editorial HTML -> PNG", ed, env=env))

    nano_key_present = bool(os.environ.get("NANOBANANA_API_KEY"))
    if nano_key_present and not args.skip_pollinations:
        nb = [str(SCRIPTS / "nanobanana_generate.py"), *shared]
        codes.append(run_step("NanoBanana REST API (Tool: nanobanana-api only)", nb, env=env))

    if any(c != 0 for c in codes):
        print("\nOne or more generation steps failed - see stderr above.", file=sys.stderr)
        return 1
    print("\nAll image generation steps finished successfully.", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
