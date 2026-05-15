#!/usr/bin/env python3
"""Generate Ghost Research image assets via the NanoBanana API.

This script reads a proposal's ``prompts.md`` file, extracts every concept whose
tool is ``nanobanana``, submits the prompt to NanoBanana, polls until the task
completes, and downloads the resulting image into ``data/proposals/<slug>/assets``.

Environment variables:
    NANOBANANA_API_KEY           Required. Bearer token for the API.
    NANOBANANA_MODEL             Optional. "generate-2" (default) or "generate".
    NANOBANANA_RESOLUTION        Optional. Used by generate-2. Default: "1K".
    NANOBANANA_POLL_SECONDS      Optional. Poll interval. Default: 3.
    NANOBANANA_TIMEOUT_SECONDS   Optional. Max wait per image. Default: 300.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import Request, urlopen


REPO_ROOT = Path(__file__).resolve().parents[1]
PROPOSALS_DIR = REPO_ROOT / "data" / "proposals"
API_BASE_URL = "https://api.nanobananaapi.ai/api/v1/nanobanana"


@dataclass
class ConceptPrompt:
    concept_id: str
    name: str
    tool: str
    aspect: str
    suggested_filename: str
    prompt: str


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


def read_json(request: Request) -> dict:
    try:
        with urlopen(request) as response:
            return json.loads(response.read().decode("utf-8"))
    except HTTPError as exc:
        body = exc.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"HTTP {exc.code}: {body}") from exc
    except URLError as exc:
        raise RuntimeError(f"Network error: {exc.reason}") from exc


def post_json(url: str, payload: dict, api_key: str) -> dict:
    request = Request(
        url,
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        method="POST",
    )
    return read_json(request)


def get_json(url: str, api_key: str) -> dict:
    request = Request(
        url,
        headers={"Authorization": f"Bearer {api_key}"},
        method="GET",
    )
    return read_json(request)


def normalize_aspect_ratio(raw_aspect: str) -> str:
    aspect = raw_aspect.strip().strip("`")
    replacements = {
        "1.91:1": "16:9",
    }
    return replacements.get(aspect, aspect if aspect else "1:1")


def parse_concepts(prompts_text: str) -> list[ConceptPrompt]:
    section_pattern = re.compile(
        r"^## Concept\s+(?P<id>\d+)\s+—\s+(?P<name>.+?)\n(?P<body>.*?)(?=^## Concept\s+\d+\s+—|\Z)",
        re.MULTILINE | re.DOTALL,
    )
    concepts: list[ConceptPrompt] = []

    for match in section_pattern.finditer(prompts_text):
        body = match.group("body")
        tool = extract_field(body, "Tool")
        aspect = extract_field(body, "Aspect")
        suggested_filename = extract_field(body, "Suggested filename")
        prompt = extract_generation_prompt(body)
        concepts.append(
            ConceptPrompt(
                concept_id=match.group("id"),
                name=match.group("name").strip(),
                tool=tool,
                aspect=aspect,
                suggested_filename=suggested_filename.strip("`"),
                prompt=prompt.strip(),
            )
        )

    return concepts


def extract_field(section_body: str, field_name: str) -> str:
    pattern = re.compile(rf"^\*\*{re.escape(field_name)}:\*\*\s*(.+)$", re.MULTILINE)
    match = pattern.search(section_body)
    if not match:
        raise ValueError(f"Missing field '{field_name}' in prompts.md concept block")
    return match.group(1).strip()


def extract_generation_prompt(section_body: str) -> str:
    pattern = re.compile(r"### Generation prompt\s*```(?:\r?\n)(.*?)```", re.DOTALL)
    match = pattern.search(section_body)
    if not match:
        raise ValueError("Missing generation prompt code block in prompts.md concept block")
    return match.group(1).strip()


def submit_task(concept: ConceptPrompt, api_key: str, model: str, resolution: str) -> str:
    aspect_ratio = normalize_aspect_ratio(concept.aspect)

    if model == "generate":
        payload = {
            "prompt": concept.prompt,
            "type": "TEXTTOIAMGE",
            "numImages": 1,
            "image_size": aspect_ratio,
            "callBackUrl": "https://example.com/nanobanana-placeholder",
        }
        response = post_json(f"{API_BASE_URL}/generate", payload, api_key)
    elif model == "generate-2":
        output_format = Path(concept.suggested_filename).suffix.lower().lstrip(".") or "jpg"
        if output_format not in {"jpg", "png"}:
            output_format = "jpg"
        payload = {
            "prompt": concept.prompt,
            "imageUrls": [],
            "aspectRatio": aspect_ratio,
            "resolution": resolution,
            "googleSearch": False,
            "outputFormat": output_format,
        }
        response = post_json(f"{API_BASE_URL}/generate-2", payload, api_key)
    else:
        raise ValueError(f"Unsupported model: {model}")

    task_id = response.get("data", {}).get("taskId")
    if not task_id:
        raise RuntimeError(f"Nanobanana did not return a taskId: {response}")
    return task_id


def wait_for_result(task_id: str, api_key: str, poll_seconds: int, timeout_seconds: int) -> str:
    deadline = time.time() + timeout_seconds
    while time.time() < deadline:
        query = urlencode({"taskId": task_id})
        response = get_json(f"{API_BASE_URL}/record-info?{query}", api_key)
        data = response.get("data", response)
        success_flag = data.get("successFlag")

        if success_flag == 0:
            print(f"  - task {task_id}: generating...")
            time.sleep(poll_seconds)
            continue
        if success_flag == 1:
            result_url = data.get("response", {}).get("resultImageUrl")
            if not result_url:
                raise RuntimeError(f"Task {task_id} succeeded but returned no resultImageUrl")
            return result_url
        if success_flag in {2, 3}:
            message = data.get("errorMessage") or response.get("msg") or "Generation failed"
            raise RuntimeError(f"Task {task_id} failed: {message}")

        time.sleep(poll_seconds)

    raise TimeoutError(f"Timed out waiting for task {task_id}")


def download_file(url: str, destination: Path) -> None:
    request = Request(url, method="GET")
    try:
        with urlopen(request) as response:
            destination.write_bytes(response.read())
    except HTTPError as exc:
        body = exc.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"Failed to download image ({exc.code}): {body}") from exc
    except URLError as exc:
        raise RuntimeError(f"Failed to download image: {exc.reason}") from exc


def select_concepts(concepts: Iterable[ConceptPrompt], selected_ids: set[str] | None) -> list[ConceptPrompt]:
    selected = []
    for concept in concepts:
        if "nanobanana" not in concept.tool.lower():
            continue
        if selected_ids and concept.concept_id not in selected_ids:
            continue
        selected.append(concept)
    return selected


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate Ghost Research images through NanoBanana.")
    parser.add_argument("--slug", required=True, help="Proposal slug under data/proposals/")
    parser.add_argument(
        "--concept",
        action="append",
        help="Specific concept id(s) to generate, e.g. --concept 01 --concept 03",
    )
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="Regenerate even if the suggested filename already exists in assets/",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Parse prompts and print what would be generated without calling the API.",
    )
    return parser.parse_args()


def main() -> int:
    load_dotenv(REPO_ROOT / ".env")
    args = parse_args()

    api_key = os.environ.get("NANOBANANA_API_KEY")
    if not api_key:
        print("Missing NANOBANANA_API_KEY. Add it to .env or your shell environment.", file=sys.stderr)
        return 1

    model = os.environ.get("NANOBANANA_MODEL", "generate-2").strip()
    resolution = os.environ.get("NANOBANANA_RESOLUTION", "1K").strip()
    poll_seconds = int(os.environ.get("NANOBANANA_POLL_SECONDS", "3"))
    timeout_seconds = int(os.environ.get("NANOBANANA_TIMEOUT_SECONDS", "300"))

    proposal_dir = PROPOSALS_DIR / args.slug
    prompts_path = proposal_dir / "prompts.md"
    assets_dir = proposal_dir / "assets"
    assets_dir.mkdir(parents=True, exist_ok=True)

    if not prompts_path.exists():
        print(f"Could not find prompts file: {prompts_path}", file=sys.stderr)
        return 1

    prompts_text = prompts_path.read_text(encoding="utf-8")
    concepts = parse_concepts(prompts_text)
    selected_ids = {concept_id.zfill(2) for concept_id in args.concept} if args.concept else None
    nanobanana_concepts = select_concepts(concepts, selected_ids)

    if not nanobanana_concepts:
        print("No nanobanana concepts found for the requested selection.")
        return 0

    print(f"Found {len(nanobanana_concepts)} nanobanana concept(s) in {prompts_path}.")
    failures = 0

    for concept in nanobanana_concepts:
        output_path = assets_dir / concept.suggested_filename
        print(f"\n[{concept.concept_id}] {concept.name}")
        print(f"  tool: {concept.tool}")
        print(f"  aspect: {normalize_aspect_ratio(concept.aspect)}")
        print(f"  output: {output_path}")

        if output_path.exists() and not args.overwrite:
            print("  - skipped: file already exists (use --overwrite to replace)")
            continue

        if args.dry_run:
            print("  - dry run: prompt parsed successfully")
            continue

        try:
            task_id = submit_task(concept, api_key, model, resolution)
            print(f"  - submitted task: {task_id}")
            result_url = wait_for_result(task_id, api_key, poll_seconds, timeout_seconds)
            print(f"  - downloading: {result_url}")
            download_file(result_url, output_path)
            print("  - saved")
        except Exception as exc:  # noqa: BLE001
            failures += 1
            print(f"  - failed: {exc}", file=sys.stderr)

    if failures:
        print(f"\nCompleted with {failures} failure(s).", file=sys.stderr)
        return 1

    print("\nAll requested nanobanana image assets were generated successfully.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
