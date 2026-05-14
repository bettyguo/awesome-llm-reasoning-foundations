#!/usr/bin/env python3
"""Validate every entry YAML in entries/ against the repo schema.

Exits non-zero on any failure. Run locally:

    python tools/validate_entries.py

CI invokes this on every PR.
"""
from __future__ import annotations

import datetime as _dt
import pathlib
import re
import sys
from collections import Counter
from typing import Any

try:
    import yaml
except ImportError:
    print("ERROR: PyYAML is not installed. Run: pip install -r tools/requirements.txt", file=sys.stderr)
    sys.exit(2)

REPO_ROOT = pathlib.Path(__file__).resolve().parent.parent
ENTRIES_DIR = REPO_ROOT / "entries"
VERIFICATION_LOG = REPO_ROOT / "PLANNING" / "02_verification_log.md"

ALLOWED_CATEGORIES = {
    "expressivity",
    "cot-theory",
    "circuit-complexity",
    "logical-characterizations",
    "learnability",
    "knowledge-editing",
    "parallel-architectural",
    "surveys-and-talks",
}

REQUIRED_FIELDS = ("title", "authors", "year", "category", "links", "annotation", "added")

SUPERLATIVES = {
    "groundbreaking", "seminal", "revolutionary", "game-changing", "landmark",
    "unprecedented", "world-class", "state-of-the-art breakthrough",
}


def _fail(errors: list[str], msg: str) -> None:
    errors.append(msg)


def validate_entry(path: pathlib.Path, slug_counter: Counter[str]) -> list[str]:
    errors: list[str] = []
    try:
        data: Any = yaml.safe_load(path.read_text(encoding="utf-8"))
    except yaml.YAMLError as exc:
        return [f"{path}: invalid YAML: {exc}"]

    if not isinstance(data, dict):
        return [f"{path}: top level must be a mapping"]

    for field in REQUIRED_FIELDS:
        if field not in data:
            _fail(errors, f"{path}: missing required field '{field}'")

    if "title" in data and (not isinstance(data["title"], str) or not data["title"].strip()):
        _fail(errors, f"{path}: title must be a non-empty string")

    if "authors" in data:
        authors = data["authors"]
        if not isinstance(authors, list) or not authors or not all(isinstance(a, str) and a.strip() for a in authors):
            _fail(errors, f"{path}: authors must be a non-empty list of non-empty strings")

    if "year" in data:
        year = data["year"]
        current = _dt.date.today().year
        if not isinstance(year, int) or year < 1950 or year > current + 1:
            _fail(errors, f"{path}: year must be an int between 1950 and {current + 1}")

    if "category" in data and data["category"] not in ALLOWED_CATEGORIES:
        _fail(errors, f"{path}: category '{data['category']}' not in allowed set {sorted(ALLOWED_CATEGORIES)}")

    if "links" in data:
        links = data["links"]
        if not isinstance(links, dict):
            _fail(errors, f"{path}: links must be a mapping")
        else:
            paper = links.get("paper")
            if not isinstance(paper, str) or not paper.startswith(("http://", "https://")):
                _fail(errors, f"{path}: links.paper is required and must be an http(s) URL")
            for key, value in links.items():
                if value is None:
                    continue
                if not isinstance(value, str) or not value.startswith(("http://", "https://")):
                    _fail(errors, f"{path}: links.{key} must be null or an http(s) URL")

    if "annotation" in data:
        ann = data["annotation"]
        if not isinstance(ann, str) or not ann.strip():
            _fail(errors, f"{path}: annotation must be a non-empty string")
        else:
            stripped = ann.strip()
            sentence_count = sum(stripped.count(c) for c in ".!?")
            if sentence_count < 1:
                _fail(errors, f"{path}: annotation must contain at least one sentence")
            if sentence_count > 4:
                _fail(errors, f"{path}: annotation should be 1–3 sentences (found ~{sentence_count})")
            lowered = stripped.lower()
            for sup in SUPERLATIVES:
                if sup in lowered:
                    _fail(errors, f"{path}: annotation contains banned superlative '{sup}'")
            if len(stripped) > 600:
                _fail(errors, f"{path}: annotation is too long ({len(stripped)} chars > 600)")

    if "added" in data:
        added = data["added"]
        if isinstance(added, _dt.date):
            pass
        elif isinstance(added, str):
            try:
                _dt.date.fromisoformat(added)
            except ValueError:
                _fail(errors, f"{path}: added must be ISO date YYYY-MM-DD (got {added!r})")
        else:
            _fail(errors, f"{path}: added must be an ISO date (YYYY-MM-DD)")

    if "tags" in data and data["tags"] is not None:
        tags = data["tags"]
        if not isinstance(tags, list) or not all(isinstance(t, str) and t.strip() for t in tags):
            _fail(errors, f"{path}: tags must be a list of non-empty strings")

    slug = path.stem
    slug_counter[slug] += 1
    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", slug):
        _fail(errors, f"{path}: slug '{slug}' must be lowercase kebab-case")

    expected_dir_category_map = {
        "01-expressivity": "expressivity",
        "02-cot-theory": "cot-theory",
        "03-circuit-complexity": "circuit-complexity",
        "04-logical-characterizations": "logical-characterizations",
        "05-learnability": "learnability",
        "06-knowledge-editing": "knowledge-editing",
        "07-parallel-architectural": "parallel-architectural",
        "08-surveys-and-talks": "surveys-and-talks",
    }
    parent_dir = path.parent.name
    expected_cat = expected_dir_category_map.get(parent_dir)
    if expected_cat is not None and data.get("category") != expected_cat:
        _fail(errors, f"{path}: directory {parent_dir} implies category '{expected_cat}' but YAML says '{data.get('category')}'")

    return errors


def _slugs_in_verification_log() -> set[str]:
    if not VERIFICATION_LOG.exists():
        return set()
    text = VERIFICATION_LOG.read_text(encoding="utf-8")
    return set(re.findall(r"^\|\s*(?:PASS|DROP)\s*\|\s*`([a-z0-9-]+)`", text, flags=re.MULTILINE))


def _pass_slugs_in_verification_log() -> set[str]:
    if not VERIFICATION_LOG.exists():
        return set()
    text = VERIFICATION_LOG.read_text(encoding="utf-8")
    return set(re.findall(r"^\|\s*PASS\s*\|\s*`([a-z0-9-]+)`", text, flags=re.MULTILINE))


def main() -> int:
    if not ENTRIES_DIR.exists():
        print(f"ERROR: entries directory not found at {ENTRIES_DIR}", file=sys.stderr)
        return 2

    yaml_files = sorted(ENTRIES_DIR.glob("**/*.yaml"))
    if not yaml_files:
        print(f"ERROR: no YAML entries found under {ENTRIES_DIR}", file=sys.stderr)
        return 2

    all_errors: list[str] = []
    slug_counter: Counter[str] = Counter()

    for path in yaml_files:
        all_errors.extend(validate_entry(path, slug_counter))

    duplicates = [s for s, c in slug_counter.items() if c > 1]
    for dup in duplicates:
        all_errors.append(f"duplicate slug across entries/: {dup}")

    pass_slugs = _pass_slugs_in_verification_log()
    missing_in_log = sorted({p.stem for p in yaml_files} - pass_slugs)
    for slug in missing_in_log:
        all_errors.append(f"entry '{slug}' has no PASS row in PLANNING/02_verification_log.md")

    if all_errors:
        print(f"VALIDATION FAILED ({len(all_errors)} error(s)):", file=sys.stderr)
        for e in all_errors:
            print(f"  - {e}", file=sys.stderr)
        return 1

    print(f"OK: {len(yaml_files)} entries validated, {len(pass_slugs)} PASS rows in verification log.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
