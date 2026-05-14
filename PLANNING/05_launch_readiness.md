# Phase 5 — Launch-Readiness Checklist

Status as of 2026-05-14 — all items ticked are mechanically verified (CI green, file exists, link resolves). Items the human curator still needs to do are flagged at the bottom.

## Mechanically verified

- [x] README passes the 5-second test. The hero banner, scope statement ("**theoretical foundations of LLM reasoning**"), and category list are above the fold.
- [x] Scope statement is unambiguous IN vs OUT. Lists the OUT-of-scope items by name (CoT prompting tricks, agent frameworks, RLHF/RLVR methodology, o1 follow-ups without formal results, jailbreaks, leaderboards, multimodal CoT applications). Prevents "you're missing X" noise where X is out-of-scope by design.
- [x] Hero banner at `assets/banner.svg` — text-based SVG, no binary, renders cleanly on GitHub.
- [x] Every published entry is web-verified. `PLANNING/02_verification_log.md` has 89 PASS rows for 81 published entries (extras = renamed-slug rows from Phase 3 reconciliation, harmless); `validate_entries.py` enforces that every entry has a PASS row.
- [x] `tools/linkcheck.py` passes — all 85 URLs (paper + openreview + code + project links) returned status `<400` on 2026-05-14.
- [x] CI runs the link-check weekly (`.github/workflows/linkcheck.yml`, cron `0 6 * * 1`).
- [x] Curator attribution block in README — Betty Guo (Dongxin Guo), HKU, advised by Prof. Siu-Ming Yiu, with GitHub + ORCID links.
- [x] "Related lists" section generously links the methods-focused competing lists (`atfortes`, `srush`, `luban-agi`, `reasoning-survey`, `JShollaj`, `hemingkx`).
- [x] `docs/LAUNCH.md` contains Show HN title, X-thread draft, r/ML draft, newsletter outreach paragraph, channel sequencing, and explicit slow-spike warning + companion-repo recommendation.
- [x] Star-history embed present (commented out in template until repo is public, with explanatory comment).
- [x] `docs/PROFILE_SNIPPET.md` ready for the curator's GitHub profile.
- [x] PR template (`.github/PULL_REQUEST_TEMPLATE.md`) requires a verification URL for new entries; lists the four metadata fields a contributor must confirm.
- [x] Issue templates (`.github/ISSUE_TEMPLATE/new_entry.md`, `wanted_entry.md`) wire up the contribution flow.
- [x] LICENSE (CC0 1.0 for content) and LICENSE-CODE (MIT for `tools/`) both present.
- [x] CONTRIBUTING.md spells out the in/out-of-scope boundary, contribution flow, and validator output.
- [x] CODE_OF_CONDUCT.md (Contributor Covenant 2.1).
- [x] `tools/validate_entries.py` and `tools/linkcheck.py` runnable with only PyYAML + httpx (minimal dep surface for supply-chain hygiene).
- [x] `python tools/build_readme.py` is deterministic (sort key is year-then-surname, no clock dependence), so the validate workflow's "no-drift" check is meaningful.

## Manual steps remaining (curator)

These cannot be done by the build tooling and require the human curator's authority.

1. **Make the repo public on GitHub.** Until then the badges 404 and the star-history embed cannot be enabled.
2. **Uncomment the star-history embed** in `tools/build_readme.py` (one line block; explanatory comment in place) and re-run `python tools/build_readme.py`.
3. **File initial `wanted` issues.** Aim for at least 3 before public launch so the issue tab isn't empty. Suggested seeds:
   - "Wanted: an entry for the Ruoss et al. 2024 work on transformer architectures beyond attention" (or whichever recent paper looks ripe).
   - "Wanted: a survey-and-talks entry for a recorded conference talk by Merrill, Strobl, or Chiang."
   - "Wanted: more coverage of state-space-model expressivity beyond the Merrill et al. SSM-Illusion entry."
4. **Author outreach.** Email Lena Strobl, William Merrill, David Chiang, Clayton Sanford, Michael Hahn — the most-cited authors in the list — with a one-sentence note; details in `docs/LAUNCH.md`.
5. **Update the curator's GitHub profile README** with the snippet from `docs/PROFILE_SNIPPET.md`.
6. **Decide on a companion-repo** to launch alongside (see `docs/LAUNCH.md` for three concrete candidates). Pick one; ship it the same week.

## Entry-count snapshot at end of Phase 5

| Category | Count |
|---|---|
| Expressivity & Representational Limits | 14 |
| Chain-of-Thought: Theory & Error Bounds | 12 |
| Circuit & Communication Complexity | 8 |
| Logical Characterizations | 5 |
| Learnability & Sample Complexity | 20 |
| Knowledge Editing & Impossibility Results | 13 |
| Parallel / Architectural Complexity & Scaling | 6 |
| Surveys, Lecture Notes & Talks | 3 |
| **Total** | **81** |

Verification log: 89 PASS rows, 0 DROP rows for entries published, 2 DROP rows for THINK-stage candidates that were deliberately not added (`bills-2023-explain-neurons`, `wei-2022-cot-prompting`).
