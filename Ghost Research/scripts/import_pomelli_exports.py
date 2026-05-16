#!/usr/bin/env python3
"""Bridge Google Labs Pomelli (web UI, no API) into Ghost Research assets.

Export PNG/JPEG/MP4 from Pomelli, drop them under::

    data/proposals/<slug>/pomelli-inbox/

Name files so we can map them to concept IDs (see patterns below), then run::

    python scripts/import_pomelli_exports.py --slug <slug> [--overwrite]

Copies each matched file to ``assets/<Suggested filename>`` from ``prompts.md``.

Pomelli product URL: https://labs.google.com/pomelli/
"""

from __future__ import annotations

import argparse
import json
import re
import shutil
import sys
import webbrowser
from pathlib import Path

from _common import parse_concepts, proposal_paths

POMELLI_APP_URL = "https://labs.google.com/pomelli/"

# concept-01, concept-01-w1d1, concept_01_foo (stem, no extension)
RE_CONCEPT_STEM = re.compile(r"^concept[_-](?P<id>\d{1,2})(?P<rest>[_\-.].*)?$", re.IGNORECASE)
# Stem exactly "01" … "14" — two-digit id
RE_TWO_DIGIT_STEM = re.compile(r"^(?P<id>\d{2})$", re.IGNORECASE)


def inbox_dir_for(slug: str) -> Path:
    proposal_dir, _, _ = proposal_paths(slug)
    d = proposal_dir / "pomelli-inbox"
    d.mkdir(parents=True, exist_ok=True)
    return d


def concept_targets_by_id(prompts_path: Path) -> dict[str, Path]:
    concepts = parse_concepts(prompts_path.read_text(encoding="utf-8"))
    assets_dir = prompts_path.parent / "assets"
    assets_dir.mkdir(parents=True, exist_ok=True)
    out: dict[str, Path] = {}
    for c in concepts:
        cid = c.concept_id.zfill(2)
        name = c.suggested_filename.strip().strip("`")
        if not name:
            name = f"concept-{cid}.jpg"
        out[cid] = (assets_dir / name).resolve()
    return out


def infer_concept_id(filename: str) -> str | None:
    stem = Path(filename).stem
    m = RE_CONCEPT_STEM.match(stem)
    if m:
        return m.group("id").zfill(2)
    m = RE_TWO_DIGIT_STEM.match(stem)
    if m:
        return m.group("id")
    return None


def load_manifest(path: Path) -> dict[str, Path]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError("Manifest JSON must be an object: {\"01\": \"path/to/file.png\", ...}")
    out: dict[str, Path] = {}
    for k, v in data.items():
        cid = str(k).zfill(2)
        p = Path(str(v))
        if not p.is_absolute():
            p = (path.parent / p).resolve()
        out[cid] = p
    return out


def collect_inbox_files(inbox: Path) -> list[Path]:
    if not inbox.is_dir():
        return []
    allowed = {".png", ".jpg", ".jpeg", ".webp", ".mp4", ".mov", ".webm"}
    files: list[Path] = []
    for p in sorted(inbox.iterdir()):
        if p.is_file() and p.suffix.lower() in allowed and not p.name.startswith("."):
            files.append(p)
    return files


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(
        description="Copy Pomelli exports from pomelli-inbox/ into assets/ using prompts.md filenames.",
    )
    p.add_argument("--slug", required=True, help="Proposal slug under data/proposals/")
    p.add_argument(
        "--from-dir",
        type=Path,
        help="Override inbox directory (default: data/proposals/<slug>/pomelli-inbox/)",
    )
    p.add_argument(
        "--manifest",
        type=Path,
        help='JSON map of concept id -> file path, e.g. {"01": "C:/Downloads/hero.png"}',
    )
    p.add_argument("--overwrite", action="store_true", help="Replace existing files in assets/")
    p.add_argument("--dry-run", action="store_true", help="Print planned copies only")
    p.add_argument(
        "--open-ui",
        action="store_true",
        help=f"Open {POMELLI_APP_URL} in your default browser (then export into pomelli-inbox/)",
    )
    p.add_argument(
        "--optional",
        action="store_true",
        help="If nothing matches, exit 0 (used when chained from generate_proposal_assets).",
    )
    p.add_argument(
        "--status",
        action="store_true",
        help="Show Pomelli inbox + concepts 15–22 asset files on disk; no copy.",
    )
    return p.parse_args()


def print_pack_status(slug: str, inbox: Path, assets_dir: Path, prompts_path: Path) -> None:
    """Help debug 'where is my Pomelli video' — shows 15–22 targets + inbox."""
    concepts = parse_concepts(prompts_path.read_text(encoding="utf-8"))
    pack = [c for c in concepts if c.concept_id.isdigit() and 15 <= int(c.concept_id) <= 22]
    pack.sort(key=lambda c: int(c.concept_id))

    print(f"Pomelli pack status — slug {slug!r}\n")
    print(f"Inbox: {inbox}")
    if inbox.is_dir():
        files = sorted(inbox.iterdir(), key=lambda p: p.name.lower())
        files = [p for p in files if p.is_file() and not p.name.startswith(".")]
        if not files:
            print("  (empty — drop exports here before import)\n")
        else:
            for p in files:
                print(f"  - {p.name}  ({p.stat().st_size // 1024} KB)")
            print()
    else:
        print("  (folder missing)\n")

    print("Expected files under assets/ (concepts 15–22 in prompts.md):\n")
    for c in pack:
        name = c.suggested_filename.strip().strip("`")
        path = assets_dir / name
        ok = path.is_file()
        sz = f"  {path.stat().st_size // 1024} KB" if ok else ""
        mark = "yes" if ok else "MISSING"
        print(f"  [{c.concept_id}] {c.tool[:40]:40} {mark:8} {name}{sz}")

    print(
        "\nHow to get MP4s on disk:\n"
        "  A) Pomelli gave you STILLS -> save as 15.jpg ... 18.jpg in the inbox above, run import,\n"
        "     then: python scripts/animate_image.py --slug SLUG --concept 19 --concept 20 --concept 21 --concept 22 --overwrite\n"
        "  B) Pomelli gave you VIDEOS -> save as 19.mp4 ... 22.mp4 in the inbox, run import --overwrite\n"
        "     (no animate step -- files land as concept-19-...-motion-v1.mp4 etc.)\n"
        "Replace SLUG with your proposal folder name.\n"
    )


def main() -> int:
    args = parse_args()
    proposal_dir, prompts_path, assets_dir = proposal_paths(args.slug)
    inbox = args.from_dir.resolve() if args.from_dir else inbox_dir_for(args.slug)

    if args.status:
        if not prompts_path.exists():
            print(f"Missing prompts: {prompts_path}", file=sys.stderr)
            return 1
        print_pack_status(args.slug, inbox, assets_dir, prompts_path)
        return 0

    if args.open_ui:
        webbrowser.open(POMELLI_APP_URL)
        print(f"Opened (or attempted): {POMELLI_APP_URL}")

    if not prompts_path.exists():
        print(f"Missing prompts: {prompts_path}", file=sys.stderr)
        return 1

    targets = concept_targets_by_id(prompts_path)

    plan: list[tuple[str, Path, Path]] = []

    if args.manifest:
        manifest_paths = load_manifest(args.manifest.resolve())
        for cid, src in manifest_paths.items():
            if cid not in targets:
                print(f"[warn] manifest key {cid!r} not in prompts — skipped", file=sys.stderr)
                continue
            if not src.is_file():
                print(f"[warn] manifest path not a file: {src} — skipped", file=sys.stderr)
                continue
            plan.append((cid, src, targets[cid]))
    else:
        for src in collect_inbox_files(inbox):
            cid = infer_concept_id(src.name)
            if not cid:
                print(
                    f"[skip] {src.name!r} — rename to match concept-01-….ext or 01.ext (two-digit id)",
                    file=sys.stderr,
                )
                continue
            if cid not in targets:
                print(f"[warn] concept id {cid} from {src.name!r} not in prompts — skipped", file=sys.stderr)
                continue
            plan.append((cid, src, targets[cid]))

    # One source per concept: if multiple map to same id, keep last (sorted path order)
    dedup: dict[str, tuple[Path, Path]] = {}
    for cid, src, dst in plan:
        dedup[cid] = (src, dst)
    plan = [(cid, s, d) for cid, (s, d) in sorted(dedup.items())]

    if not plan:
        msg = (
            f"No imports planned. Add files to:\n  {inbox}\n"
            "Naming: concept-01.png / concept-01-anything.jpg / stem 01.png (see --help). Or use --manifest."
        )
        if args.optional:
            print(msg, file=sys.stderr)
            return 0
        print(msg, file=sys.stderr)
        return 1 if not args.open_ui else 0

    print(f"Pomelli import for slug {args.slug!r} ({len(plan)} file(s))\n")
    failures = 0
    for cid, src, dst in plan:
        print(f"[{cid}] {src.name}")
        print(f"  -> {dst.relative_to(proposal_dir)}")
        if dst.exists() and not args.overwrite:
            print("  - skipped (target exists; use --overwrite)", file=sys.stderr)
            continue
        if src.suffix.lower() != dst.suffix.lower() and {src.suffix.lower(), dst.suffix.lower()} != {".jpg", ".jpeg"}:
            print(
                f"  [warn] extension mismatch {src.suffix!r} -> {dst.suffix!r} "
                "(OK for video concepts; wrong extension may break downstream tools)",
                file=sys.stderr,
            )
        if args.dry_run:
            print("  - dry run")
            continue
        try:
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src, dst)
            print(f"  - copied ({dst.stat().st_size // 1024} KB)")
        except OSError as exc:
            failures += 1
            print(f"  - failed: {exc}", file=sys.stderr)

    if failures:
        return 1
    any_pack_still = any(cid in {"15", "16", "17", "18"} for cid, _, _ in plan)
    any_pack_mp4 = any(cid in {"19", "20", "21", "22"} for cid, _, _ in plan)
    print("\nDone.", flush=True)
    if any_pack_still:
        print(
            "Ken-Burns clips for the Pomelli stills (run after imports land):\n"
            f"  python scripts/animate_image.py --slug {args.slug} "
            "--concept 19 --concept 20 --concept 21 --concept 22 --overwrite\n",
            flush=True,
        )
    if any_pack_mp4:
        print(
            "Imported Pomelli MP4s into assets/ — open the folder above and play "
            f"`concept-19-pomelli-pack-motion-v1.mp4` … `concept-22-…-v4.mp4`.\n",
            flush=True,
        )
    if not any_pack_still and not any_pack_mp4:
        print(
            "\nNext: re-run editorial/motion if those concepts consume this asset, e.g.\n"
            f'  python scripts/generate_proposal_assets.py --slug {args.slug}\n'
            f"  python scripts/render_editorial.py --slug {args.slug} --overwrite\n"
            f"  python scripts/animate_image.py --slug {args.slug} --overwrite"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
