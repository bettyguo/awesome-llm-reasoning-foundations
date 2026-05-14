#!/usr/bin/env python3
"""Generate README.md from entries/*.yaml.

The README is the primary artifact. It is generated, not hand-edited, so that
the link-checker and validators always see clean data. Run locally:

    python tools/build_readme.py

CI checks that the checked-in README matches the generated one (drift detection).
"""
from __future__ import annotations

import datetime as _dt
import pathlib
import sys
from typing import Any

try:
    import yaml
except ImportError:
    print("ERROR: PyYAML is not installed. Run: pip install -r tools/requirements.txt", file=sys.stderr)
    sys.exit(2)

REPO_ROOT = pathlib.Path(__file__).resolve().parent.parent
ENTRIES_DIR = REPO_ROOT / "entries"
README_PATH = REPO_ROOT / "README.md"

CATEGORIES = [
    ("expressivity",               "Expressivity & Representational Limits"),
    ("cot-theory",                 "Chain-of-Thought: Theory & Error Bounds"),
    ("circuit-complexity",         "Circuit & Communication Complexity"),
    ("logical-characterizations",  "Logical Characterizations"),
    ("learnability",               "Learnability & Sample Complexity"),
    ("knowledge-editing",          "Knowledge Editing & Impossibility Results"),
    ("parallel-architectural",     "Parallel / Architectural Complexity & Scaling"),
    ("surveys-and-talks",          "Surveys, Lecture Notes & Talks"),
]


HEADER = """<!-- THIS FILE IS GENERATED. Edit entries/*.yaml and run `python tools/build_readme.py`. -->

<p align="center">
  <img src="assets/banner.svg" alt="Awesome LLM Reasoning Foundations" width="720"/>
</p>

<h1 align="center">Awesome LLM Reasoning Foundations</h1>

<p align="center">
  <a href="https://awesome.re"><img src="https://awesome.re/badge.svg" alt="Awesome"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/list-CC0%201.0-blue.svg" alt="CC0"></a>
  <a href="LICENSE-CODE"><img src="https://img.shields.io/badge/code-MIT-green.svg" alt="MIT"></a>
  <a href="https://github.com/bettyguo/awesome-llm-reasoning-foundations/actions/workflows/linkcheck.yml"><img src="https://github.com/bettyguo/awesome-llm-reasoning-foundations/actions/workflows/linkcheck.yml/badge.svg" alt="Link check"></a>
</p>

A curated, rigorously-verified map of the **theoretical foundations of LLM reasoning** — expressivity, chain-of-thought error bounds, circuit complexity, logical characterizations, learnability of in-context tasks, and knowledge-editing impossibility results.

## Scope

**IN scope:** formal expressivity results for transformers; chain-of-thought theory and error bounds; circuit / communication / parallel complexity; logical characterizations (FOC[Attn], FO+MOD, counting logics); learnability and sample-complexity theory; knowledge-editing impossibility results; lecture notes and surveys covering the above.

**OUT of scope (intentionally):** CoT prompting tricks and engineering recipes; agent frameworks; RLHF / RLVR methodology; o1 / DeepSeek-R1 follow-ups that don't carry a formal result; jailbreaks; leaderboards; multimodal CoT applications. Excellent applied lists already exist — see *Related lists* below.

Every entry below was verified against arXiv / OpenReview / ACL Anthology before inclusion. Entries that could not be verified are dropped, not guessed.

## Curator

Maintained by **Betty Guo (Dongxin Guo)** — final-year CS PhD candidate, University of Hong Kong, advised by Prof. Siu-Ming Yiu. Research in the formal foundations of LLM reasoning.

- GitHub: [@bettyguo](https://github.com/bettyguo)
- ORCID: [0009-0000-2388-1072](https://orcid.org/0009-0000-2388-1072)

If you spot an error, please open an issue — citation accuracy is the whole point of this list.

"""


FOOTER_TEMPLATE = """## Reading paths

Curated ordered sequences for getting into a sub-area. See [`docs/reading-paths.md`](docs/reading-paths.md) for the full set.

- **Start here for CoT theory** → Merrill & Sabharwal (2024, CoT) → Feng et al. (2023, CoT mystery) → Li et al. (2024, serial problems).
- **Start here for expressivity** → Strobl et al. (2024, survey) → Hahn (2020, limitations) → Merrill, Sabharwal, Smith (2022, saturated → TC0) → Merrill & Sabharwal (2023, log-precision → TC0).
- **Start here for learnability of in-context learning** → Xie et al. (2022, implicit Bayes) → Garg et al. (2022, simple function classes) → von Oswald et al. (2023, GD).

## Recent additions

{recent_additions}

## Related lists

Adjacent and complementary lists. Linked in good faith — these cover the *methods* side of LLM reasoning, which this list deliberately excludes.

- [atfortes/Awesome-LLM-Reasoning](https://github.com/atfortes/Awesome-LLM-Reasoning) — methods, CoT → o1 → DeepSeek-R1.
- [srush/awesome-o1](https://github.com/srush/awesome-o1) — o1-centric bibliography.
- [luban-agi/Awesome-LLM-reasoning](https://github.com/luban-agi/Awesome-LLM-reasoning) — broad reasoning paper list.
- [reasoning-survey/Awesome-Reasoning-Foundation-Models](https://github.com/reasoning-survey/Awesome-Reasoning-Foundation-Models) — survey of foundation models for reasoning.
- [JShollaj/awesome-llm-interpretability](https://github.com/JShollaj/awesome-llm-interpretability) — mechanistic interpretability (sibling, not overlap).
- [hemingkx/Awesome-Efficient-Reasoning](https://github.com/hemingkx/Awesome-Efficient-Reasoning) — efficient reasoning.

## Wanted entries

Gaps we want filled by the community are tracked under the [`wanted`](https://github.com/bettyguo/awesome-llm-reasoning-foundations/issues?q=is%3Aissue+label%3Awanted) issue label. Pick one, submit a PR.

## Contributing

Every new entry needs a verification link (arXiv abstract page, OpenReview, or proceedings URL). See [CONTRIBUTING.md](CONTRIBUTING.md). Out-of-scope PRs may be redirected to one of the related lists above — that's the boundary of *this* list, not a judgment of the work.

## Star history

<!--
  Uncomment after the repo is public. The badge service 404s on private repos,
  which would make the README render a broken image on github.com.

  <a href="https://star-history.com/#bettyguo/awesome-llm-reasoning-foundations&Date">
    <img src="https://api.star-history.com/svg?repos=bettyguo/awesome-llm-reasoning-foundations&type=Date" alt="Star History Chart"/>
  </a>
-->

## License

- List content (`README.md`, `entries/`, `docs/`, `PLANNING/`) — [CC0 1.0](LICENSE), public domain.
- Source code under `tools/` — [MIT](LICENSE-CODE).
"""


def _slug_to_anchor(slug: str) -> str:
    return slug.replace(".", "").lower()


def render_entry(data: dict[str, Any]) -> str:
    title = data["title"].strip()
    authors = data["authors"]
    if len(authors) <= 3:
        authors_str = ", ".join(authors)
    else:
        authors_str = f"{authors[0]} et al."
    year = data["year"]
    venue = data.get("venue")
    venue_str = f"{year}, {venue}" if venue else f"{year}"

    links = data["links"]
    link_parts: list[str] = [f"[paper]({links['paper']})"]
    for role in ("openreview", "code", "project"):
        if links.get(role):
            link_parts.append(f"[{role}]({links[role]})")
    links_str = " · ".join(link_parts)

    annotation = " ".join(data["annotation"].split())
    return f"- **{title}** — {authors_str} ({venue_str}). {links_str}. _Why it matters:_ {annotation}"


def load_entries() -> list[tuple[pathlib.Path, dict[str, Any]]]:
    out: list[tuple[pathlib.Path, dict[str, Any]]] = []
    for path in sorted(ENTRIES_DIR.glob("**/*.yaml")):
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
        if isinstance(data, dict):
            out.append((path, data))
    return out


def _normalize_added(value: Any) -> _dt.date:
    if isinstance(value, _dt.date):
        return value
    if isinstance(value, str):
        return _dt.date.fromisoformat(value)
    raise ValueError(f"cannot parse added field: {value!r}")


def _surname(author: str) -> str:
    return author.strip().split()[-1].lower()


def build_toc(by_cat: dict[str, list[dict[str, Any]]]) -> str:
    lines = ["## Contents", ""]
    for cat, label in CATEGORIES:
        count = len(by_cat.get(cat, []))
        if count == 0:
            continue
        anchor = label.lower()
        for ch in [" ", "/", ",", "&", "(", ")"]:
            anchor = anchor.replace(ch, "-")
        anchor = anchor.replace(":", "")
        while "--" in anchor:
            anchor = anchor.replace("--", "-")
        anchor = anchor.strip("-")
        lines.append(f"- [{label}](#{anchor}) ({count})")
    return "\n".join(lines)


def build_sections(by_cat: dict[str, list[dict[str, Any]]]) -> str:
    sections: list[str] = []
    for cat, label in CATEGORIES:
        items = by_cat.get(cat, [])
        if not items:
            continue
        items_sorted = sorted(items, key=lambda d: (-int(d["year"]), _surname(d["authors"][0])))
        body = "\n".join(render_entry(d) for d in items_sorted)
        sections.append(f"## {label}\n\n{body}")
    return "\n\n".join(sections)


def build_recent(entries: list[tuple[pathlib.Path, dict[str, Any]]]) -> str:
    enriched = [(d, _normalize_added(d["added"])) for _, d in entries]
    enriched.sort(key=lambda x: x[1], reverse=True)
    top = enriched[:10]
    if not top:
        return "_(no entries yet)_"
    lines = []
    for d, added in top:
        title = d["title"].strip()
        url = d["links"]["paper"]
        lines.append(f"- {added.isoformat()} — [{title}]({url})")
    return "\n".join(lines)


def main() -> int:
    entries = load_entries()
    if not entries:
        print("ERROR: no entries found.", file=sys.stderr)
        return 2

    by_cat: dict[str, list[dict[str, Any]]] = {cat: [] for cat, _ in CATEGORIES}
    for _, data in entries:
        by_cat.setdefault(data["category"], []).append(data)

    toc = build_toc(by_cat)
    sections = build_sections(by_cat)
    recent = build_recent(entries)

    output = HEADER + toc + "\n\n" + sections + "\n\n" + FOOTER_TEMPLATE.format(recent_additions=recent)
    if not output.endswith("\n"):
        output += "\n"

    README_PATH.write_text(output, encoding="utf-8", newline="\n")
    total = sum(len(v) for v in by_cat.values())
    print(f"OK: wrote {README_PATH} ({total} entries across {sum(1 for v in by_cat.values() if v)} categories).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
