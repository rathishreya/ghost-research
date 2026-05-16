"""Shared helpers for Ghost Research generation scripts.

All Ghost generation scripts use the official Google Gemini SDK (`google-genai`)
authenticated by `GEMINI_API_KEY` from `.env` or the shell.
"""

from __future__ import annotations

import os
import re
import sys
from dataclasses import dataclass
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
PROPOSALS_DIR = REPO_ROOT / "data" / "proposals"


def load_dotenv(path: Path | None = None) -> None:
    """Load `KEY=value` pairs from a `.env` file into os.environ (without overriding existing values)."""
    if path is None:
        path = REPO_ROOT / ".env"
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


def require_api_key() -> str:
    load_dotenv()
    key = os.environ.get("GEMINI_API_KEY")
    if not key:
        print(
            "Missing GEMINI_API_KEY. Add it to Ghost Research/.env or export it in your shell.",
            file=sys.stderr,
        )
        sys.exit(1)
    return key


@dataclass
class ConceptPrompt:
    concept_id: str
    name: str
    tool: str
    aspect: str
    duration: str | None
    suggested_filename: str
    prompt: str
    raw_body: str


CONCEPT_HEADER = re.compile(
    r"^## Concept\s+(?P<id>\d+)\s+[—-]\s+(?P<name>.+?)\n(?P<body>.*?)(?=^## Concept\s+\d+\s+[—-]|\Z)",
    re.MULTILINE | re.DOTALL,
)

FIELD_RE = re.compile(r"^\*\*(?P<field>[^:]+):\*\*\s*(?P<value>.+)$", re.MULTILINE)

PROMPT_BLOCK_RE = re.compile(
    r"### Generation prompt\s*```(?:\w+)?\s*\n(?P<prompt>.*?)```",
    re.DOTALL,
)


def parse_concepts(prompts_text: str) -> list[ConceptPrompt]:
    concepts: list[ConceptPrompt] = []
    for match in CONCEPT_HEADER.finditer(prompts_text):
        body = match.group("body")
        fields = {m.group("field").strip().lower(): m.group("value").strip() for m in FIELD_RE.finditer(body)}
        prompt_match = PROMPT_BLOCK_RE.search(body)
        if not prompt_match:
            continue
        concepts.append(
            ConceptPrompt(
                concept_id=match.group("id"),
                name=match.group("name").strip(),
                tool=fields.get("tool", ""),
                aspect=fields.get("aspect", "1:1").strip("`"),
                duration=fields.get("duration"),
                suggested_filename=fields.get("suggested filename", f"concept-{match.group('id')}.jpg").strip("`"),
                prompt=prompt_match.group("prompt").strip(),
                raw_body=body,
            )
        )
    return concepts


def normalize_aspect(raw: str, *, for_video: bool = False) -> str:
    aspect = raw.strip().strip("`").lower()
    aliases = {"1.91:1": "16:9", "1.91 : 1": "16:9"}
    aspect = aliases.get(aspect, aspect)
    valid_image = {"1:1", "9:16", "16:9", "4:3", "3:4", "4:5", "5:4", "2:3", "3:2", "21:9"}
    valid_video = {"16:9", "9:16"}
    if for_video:
        return aspect if aspect in valid_video else "9:16"
    return aspect if aspect in valid_image else "1:1"


def proposal_paths(slug: str) -> tuple[Path, Path, Path]:
    proposal_dir = PROPOSALS_DIR / slug
    prompts_path = proposal_dir / "prompts.md"
    assets_dir = proposal_dir / "assets"
    assets_dir.mkdir(parents=True, exist_ok=True)
    return proposal_dir, prompts_path, assets_dir


BRAND_NEGATIVE = (
    "no robots, no AI-themed imagery, no brain circuits, no glowing nodes, "
    "no holograms, no neon, no cyberpunk, no sci-fi UI, no high-fiving, "
    "no hands on keyboards, no fist bumps, no smiling-at-camera lifestyle, "
    "no AI-generated faces, no uncanny features, no text in image, "
    "no logos, no watermarks, no embedded captions."
)

# In editorial / animated-html prompts, use `GHOST_ASSET:filename.jpg` anywhere you need
# a `file://` URL to an existing file in `assets/` (e.g. CSS background-image). Scripts
# replace the token before Playwright loads the page.
GHOST_ASSET_TOKEN = re.compile(r"GHOST_ASSET:([\w\-.]+)")


def inject_ghost_asset_urls(html: str, assets_dir: Path) -> str:
    """Resolve GHOST_ASSET:file.ext tokens to absolute file:/// URIs for local Playwright loads."""

    def repl(match: re.Match[str]) -> str:
        name = match.group(1)
        target = (assets_dir / name).resolve()
        if not target.is_file():
            raise FileNotFoundError(
                f"GHOST_ASSET references missing file: {name} (expected at {target})"
            )
        return target.as_uri()

    return GHOST_ASSET_TOKEN.sub(repl, html)
