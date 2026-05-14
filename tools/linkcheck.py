#!/usr/bin/env python3
"""HTTP-check every URL appearing in entries/*.yaml.

Exits non-zero if any URL fails to resolve (status >= 400, connection error,
or timeout after retry). Writes a JSON report to linkcheck-report.json.

Run locally:

    python tools/linkcheck.py
"""
from __future__ import annotations

import json
import pathlib
import sys
import time
from dataclasses import dataclass, asdict
from typing import Iterable

try:
    import httpx
    import yaml
except ImportError:
    print("ERROR: dependencies missing. Run: pip install -r tools/requirements.txt", file=sys.stderr)
    sys.exit(2)

REPO_ROOT = pathlib.Path(__file__).resolve().parent.parent
ENTRIES_DIR = REPO_ROOT / "entries"
REPORT_PATH = REPO_ROOT / "linkcheck-report.json"

USER_AGENT = (
    "awesome-llm-reasoning-foundations-linkcheck/1.0 "
    "(+https://github.com/bettyguo/awesome-llm-reasoning-foundations)"
)
TIMEOUT = httpx.Timeout(20.0, connect=10.0)
RETRY_DELAY = 2.0


@dataclass
class CheckResult:
    slug: str
    role: str
    url: str
    status: int | None
    ok: bool
    error: str | None


def iter_urls(entries: Iterable[pathlib.Path]) -> list[tuple[str, str, str]]:
    out: list[tuple[str, str, str]] = []
    for path in entries:
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
        if not isinstance(data, dict):
            continue
        links = data.get("links") or {}
        slug = path.stem
        for role, url in links.items():
            if isinstance(url, str) and url.startswith(("http://", "https://")):
                out.append((slug, role, url))
    return out


def check_one(client: httpx.Client, slug: str, role: str, url: str) -> CheckResult:
    for attempt in range(2):
        try:
            try:
                r = client.head(url, follow_redirects=True)
                if r.status_code in (403, 405, 501) or r.status_code >= 500:
                    r = client.get(url, follow_redirects=True)
            except httpx.HTTPError:
                r = client.get(url, follow_redirects=True)
            ok = r.status_code < 400
            if ok or attempt == 1:
                return CheckResult(slug, role, url, r.status_code, ok, None if ok else f"HTTP {r.status_code}")
        except httpx.HTTPError as exc:
            if attempt == 1:
                return CheckResult(slug, role, url, None, False, str(exc))
            time.sleep(RETRY_DELAY)
    return CheckResult(slug, role, url, None, False, "unreachable")


def main() -> int:
    yaml_files = sorted(ENTRIES_DIR.glob("**/*.yaml"))
    targets = iter_urls(yaml_files)
    if not targets:
        print("ERROR: no URLs to check (no entries?)", file=sys.stderr)
        return 2

    results: list[CheckResult] = []
    with httpx.Client(headers={"User-Agent": USER_AGENT}, timeout=TIMEOUT) as client:
        for i, (slug, role, url) in enumerate(targets, 1):
            res = check_one(client, slug, role, url)
            results.append(res)
            flag = "OK " if res.ok else "FAIL"
            print(f"[{i:3d}/{len(targets)}] {flag} {res.status if res.status is not None else '---':>4}  {role:>10}  {url}")

    failures = [r for r in results if not r.ok]
    REPORT_PATH.write_text(
        json.dumps(
            {
                "total": len(results),
                "failures": len(failures),
                "results": [asdict(r) for r in results],
            },
            indent=2,
        )
    )

    if failures:
        print(f"\nLINK CHECK FAILED: {len(failures)} broken link(s):", file=sys.stderr)
        for r in failures:
            print(f"  - [{r.slug}] {r.role}: {r.url}  ({r.error})", file=sys.stderr)
        return 1

    print(f"\nOK: {len(results)} URLs reachable.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
