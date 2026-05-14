# PHASE 1 — DESIGN

## 1. Repository Layout

```
awesome-llm-reasoning-foundations/
├── README.md                          # THE LIST — primary artifact, generated
├── LICENSE                            # CC0 1.0 for list content
├── LICENSE-CODE                       # MIT for tools/
├── CONTRIBUTING.md                    # how to propose an entry (verification required)
├── CODE_OF_CONDUCT.md                 # contributor covenant
├── .github/
│   ├── workflows/
│   │   ├── linkcheck.yml              # weekly + on-PR link verification
│   │   └── validate.yml               # on-PR schema + duplicate check + README sync
│   ├── PULL_REQUEST_TEMPLATE.md       # requires verification URL for new entries
│   └── ISSUE_TEMPLATE/
│       ├── new_entry.md
│       └── wanted_entry.md
├── entries/                           # STRUCTURED SOURCE OF TRUTH
│   ├── 01-expressivity/               # one YAML file per entry
│   │   ├── merrill-sabharwal-2024-cot.yaml
│   │   └── ...
│   ├── 02-cot-theory/
│   ├── 03-circuit-complexity/
│   ├── 04-logical-characterizations/
│   ├── 05-learnability/
│   ├── 06-knowledge-editing/
│   ├── 07-parallel-architectural/
│   └── 08-surveys-and-talks/
├── tools/
│   ├── linkcheck.py                   # HTTP(S) HEAD/GET every URL, fail on 4xx/5xx
│   ├── validate_entries.py            # schema + duplicate + verification-log check
│   ├── build_readme.py                # entries/*.yaml → README.md
│   └── requirements.txt               # PyYAML, httpx
├── PLANNING/
│   ├── 00_think.md
│   ├── 01_design.md
│   ├── 02_verification_log.md         # PASS/DROP row per entry
│   └── 06_review.md                   # Phase 6 output
├── docs/
│   ├── LAUNCH.md                      # Show HN / X / r/ML drafts + advice
│   ├── PROFILE_SNIPPET.md             # markdown for curator's GitHub profile
│   └── reading-paths.md               # curated ordered sequences
└── assets/
    └── banner.svg                     # README hero (text-based SVG — no binary blobs)
```

Rationale for the structured source: keeping each entry as YAML in `entries/<category>/<slug>.yaml` (rather than hand-writing Markdown) lets `linkcheck.py` and `validate_entries.py` consume clean data, prevents drift between the README and reality, and makes contributor PRs reviewable as data diffs rather than Markdown reflows.

## 2. Entry Schema

Every entry is a YAML file at `entries/<category>/<slug>.yaml`. The slug is `<lead-author-surname-lowercased>-<year>-<short-keyword>` (e.g. `merrill-sabharwal-2024-cot.yaml`).

```yaml
# Required fields
title: "The Expressive Power of Transformers with Chain of Thought"
authors:
  - "William Merrill"
  - "Ashish Sabharwal"
year: 2024                          # publication year (venue) or first arXiv year if no venue
venue: "ICLR 2024"                  # null if preprint only
category: expressivity              # one of: expressivity, cot-theory, circuit-complexity,
                                    # logical-characterizations, learnability,
                                    # knowledge-editing, parallel-architectural,
                                    # surveys-and-talks
links:
  paper: "https://arxiv.org/abs/2310.07923"   # REQUIRED — abstract or canonical landing page
  openreview: "https://openreview.net/forum?id=NjNGlPh8Wh"  # optional
  code: null                                                # optional repo URL
  project: null                                             # optional project page
annotation: |
  Characterizes the expressive power of decoder-only transformers with intermediate
  CoT tokens as a function of generation length: log-many steps stay in TC0, linear-many
  reach P, polynomial-many reach EXPTIME.
tags:                                # optional, free-form, used for tag filtering
  - chain-of-thought
  - complexity-class
added: 2026-05-14                    # ISO date the entry first entered the list
```

### Schema rules (enforced by `validate_entries.py`)

- `title`, `authors`, `year`, `category`, `links.paper`, `annotation`, `added` are required.
- `category` must be one of the eight defined values.
- `links.paper` must resolve (link-checker).
- `annotation` must be 1–3 sentences. Style rule: name the formal result. No superlatives ("groundbreaking", "seminal"). No "this paper..." padding.
- `slug` (from filename) must be unique across the repo.
- A `PASS` row in `PLANNING/02_verification_log.md` keyed by slug must exist.

## 3. README Structure

The README is **generated** from `entries/*.yaml` by `tools/build_readme.py`. Order of sections:

1. **Hero banner** — `assets/banner.svg` (SVG text — renders crisp, no binary baggage).
2. **One-paragraph scope statement** — explicitly tells readers *this list is theory, not methods*. Names what is OUT of scope (CoT prompting tricks, agent frameworks, RLHF for reasoning, o1 follow-ups, jailbreaks, leaderboards) and what is IN scope (formal expressivity, circuit/communication complexity, logical characterizations, CoT error bounds, learnability theory, knowledge-editing limits).
3. **Curator block** — Betty Guo (Dongxin Guo), HKU, advised by Prof. Siu-Ming Yiu. GitHub badge, ORCID, Google Scholar link. Establishes that an active researcher in the niche is maintaining this.
4. **Table of contents** — clickable anchors to each of the 8 categories.
5. **The list** — one section per category. Each entry rendered as one Markdown line:
   ```markdown
   - **Title** — Authors (Year, Venue). [paper](url) · [code](url) · [openreview](url). _Why it matters:_ annotation.
   ```
6. **Reading paths** — 2–3 curated ordered sequences (e.g. "Start here for CoT theory" → 4 papers in dependency order). Links into the list.
7. **Recent additions** — last 10 entries by `added` date, auto-generated.
8. **Related lists** — generous links to competing/adjacent lists (atfortes, srush/awesome-o1, etc.) with one-line scope descriptions. Good-faith linking earns reciprocal links.
9. **Wanted entries** — link to the open issues filed under the `wanted` label, so contributors see clear gaps.
10. **Contributing** — link to `CONTRIBUTING.md`; one sentence: "every new entry needs a verification link".
11. **Star history** — embed (commented out until repo is public).
12. **License** — CC0 1.0 (content) + MIT (tools); pointer to LICENSE files.

## 4. Tooling Design

### `tools/linkcheck.py`
- Loads every YAML in `entries/**.yaml`.
- For each non-null URL in the `links` map, issues an HTTP GET (HEAD first, fall back to GET — some arXiv mirrors 405 on HEAD) with a 15-second timeout, sane User-Agent.
- Exit non-zero if any URL returns ≥400 or fails to resolve. Allow-listed transient failures retried once.
- Logs a JSON report at `linkcheck-report.json` for CI artifact upload.
- Runs in `.github/workflows/linkcheck.yml` on `pull_request` AND on a weekly `schedule:` (cron `0 6 * * 1`).

### `tools/validate_entries.py`
- Loads every YAML; validates against schema (required fields, type, category enum, annotation length).
- Checks slug uniqueness.
- Checks `PLANNING/02_verification_log.md` has a `PASS` row for every published entry's slug.
- Checks `build_readme.py` output matches checked-in `README.md` (drift detection).
- Runs in `.github/workflows/validate.yml` on every PR.

### `tools/build_readme.py`
- Renders `entries/*.yaml` → `README.md` using a Jinja-free pure-Python template (keep dependencies minimal: PyYAML only, stdlib for HTTP).
- Sort within each category: by year DESC, then by lead author surname ASC. Deterministic — no clock dependence.

### `tools/requirements.txt`
```
PyYAML>=6.0
httpx>=0.27
```
That's it. Keeping the dependency surface tiny because (a) anyone can run the tools locally without ceremony, (b) supply-chain risk on a public list is asymmetric — a compromised dev-dep is much worse than for a private repo.

## 5. Contribution Flow

`.github/PULL_REQUEST_TEMPLATE.md` (excerpt):

```
## What is this PR?
- [ ] Adds a new entry
- [ ] Edits an existing entry
- [ ] Tooling / docs change

## If adding/editing an entry — required:
- [ ] The YAML lives in `entries/<category>/<slug>.yaml` and validates (`python tools/validate_entries.py`).
- [ ] Verification link (arXiv abstract page, OpenReview, or proceedings URL) for the paper:

      <paste URL here>

- [ ] The entry is in-scope (theoretical foundations — see README scope statement).
- [ ] Annotation is 1–3 sentences, names the formal result, no superlatives.
- [ ] If a code/project link is included, it resolves (linkcheck CI will verify).
```

`CONTRIBUTING.md` spells out:
- The in-scope / out-of-scope list.
- How to run validators locally.
- How "wanted entries" issues work (community fills declared gaps).
- That ambiguous-scope PRs may be closed with a pointer to a more applied list — that's not a rejection of the work, it's the boundary of *this* list.

---

**CHECKPOINT 1 — DONE.** Proceeding to Phase 2.
