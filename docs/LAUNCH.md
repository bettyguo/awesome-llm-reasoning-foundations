# Launch playbook

This document is the curator's playbook for going public with the list. It contains the launch advice, the channels, the message drafts, and the post-launch maintenance loop.

## Strategic note: pure lists spike slowly

Pure curated lists tend to compound on GitHub stars *slowly* compared to runnable code. The discoverable list of "awesome-X" repos is large, and a list without a tool, demo, or paper to anchor the social-media wave on accrues stars over months, not days. There are exceptions (`sindresorhus/awesome` itself, well-timed launches from already-prominent authors), but the base rate is slow-spike.

The recommended mitigation: **launch alongside a companion working repo in the same week.** Concretely, candidates the curator could ship in parallel:

1. A small reproducible reproduction of one CoT-theory result (e.g. a clean RASP / Tracr implementation of a circuit-complexity construction). Pairs naturally with `entries/01-expressivity/lindner-2023-tracr.yaml` and `entries/01-expressivity/weiss-2021-thinking-like-transformers.yaml`.
2. A literate-Python notebook walking through the Merrill–Sabharwal log-precision argument step by step.
3. A small interactive web demo of the Strobl 2024 survey's expressivity table — "click a transformer variant, see which formal-language classes it can recognize."

Pick *one*. Bundle the link in the launch posts below.

## Pre-flight checklist (run before going public)

- [ ] `python tools/validate_entries.py` — green.
- [ ] `python tools/linkcheck.py` — green. (May be slow; that's expected.)
- [ ] `python tools/build_readme.py && git diff --exit-code -- README.md` — no drift.
- [ ] Repo is public, badges on README all show green.
- [ ] At least 3 GitHub issues already filed under the `wanted` label, so the issue tab isn't empty when the first wave of visitors arrives.
- [ ] The curator's GitHub profile README contains the snippet from `PROFILE_SNIPPET.md`.
- [ ] `assets/banner.svg` renders correctly when the README is viewed on GitHub (mobile + desktop).

## Channels to launch on (in roughly the order they should fire)

1. **The curator's own X account / personal site.** This is the warmest audience; a soft launch here surfaces typos before the wider waves.
2. **r/MachineLearning** — Sunday or Monday morning UTC tends to do best for theory-oriented posts. Tag `[R]` (research) since the content is theoretical, not a project release.
3. **Hacker News (Show HN).** Submit Wednesday or Thursday morning Pacific. Title is in the draft below.
4. **The HKU CS / Yiu group internal channels.** Free, warm, and a research-group endorsement signals durability.
5. **Author outreach.** Email Lena Strobl, William Merrill, David Chiang, Clayton Sanford, Michael Hahn — the most-cited authors in the list — with a one-sentence note: "I made an awesome-list of the theoretical-foundations work in our area; happy to add corrections you spot, and would love a link from your group page if you find it useful." Author reciprocity is the highest-conversion signal an awesome-list can get.
6. **The Anthropic / DeepMind / Meta AI / FAIR internal Slacks of friendly co-authors** — they propagate organically if the list is useful, no public ask needed.
7. **`awesome` (sindresorhus/awesome) submission.** Only after week one — they prefer well-trafficked lists.

## Draft posts

### Show HN

```
Title:  Show HN: A curated map of the theoretical foundations of LLM reasoning

Body:
  Hi HN — I'm a final-year CS PhD candidate at HKU working on the formal
  theory of LLM reasoning. The existing "awesome-LLM-reasoning" lists are
  excellent but methods-focused: CoT prompting tricks, o1 follow-ups,
  agent frameworks. The *theory* side — expressivity, chain-of-thought
  error bounds, circuit complexity, logical characterizations, learnability
  of in-context tasks — was scattered across arXiv and a few authors'
  homepages.

  I built a curated, rigorously-verified map of that subfield. Every
  entry was checked against arXiv / OpenReview / proceedings before
  inclusion; the verification log is part of the repo. A CI link-checker
  runs weekly and fails the build on any broken citation.

  Currently 81 entries across 8 categories. PRs welcome; the
  contribution flow requires a verification URL.

  https://github.com/bettyguo/awesome-llm-reasoning-foundations

  Happy to take corrections — citation accuracy is the whole point.
```

### X / Twitter thread draft

```
1/ I built an awesome-list of the THEORY of LLM reasoning — expressivity,
   CoT error bounds, circuit complexity, learnability. Distinct from the
   methods-focused lists you've seen.

   https://github.com/bettyguo/awesome-llm-reasoning-foundations

2/ Why I made this: when I started my PhD, I wanted a map of the theoretical
   foundations literature on transformers. The applied lists were great
   but didn't cover Merrill, Strobl, Chiang, Hahn, Sanford et al.

3/ Every entry was web-verified against arXiv / OpenReview / proceedings.
   The verification log is part of the repo. CI link-checks weekly.
   When I couldn't verify a paper's claimed metadata, I dropped it —
   no guessing.

4/ Currently 81 entries across:
   • Expressivity & Representational Limits
   • Chain-of-Thought Theory
   • Circuit & Communication Complexity
   • Logical Characterizations
   • Learnability & Sample Complexity
   • Knowledge Editing & Impossibility
   • Parallel / Architectural Complexity
   • Surveys & Lecture Notes

5/ Includes "reading paths" — dependency-ordered sequences for getting
   into a subarea (e.g. CoT theory: Merrill-Sabharwal 2024 → Feng 2023
   → Li-Liu-Zhou-Ma 2024).

6/ Contributions welcome. PRs need a verification URL — if I can't
   re-verify your entry against arXiv/proceedings, it doesn't go in.
   Out-of-scope (CoT prompting, o1 follow-ups, agents) — point me at
   the great applied lists in the README.
```

### r/MachineLearning post draft

```
Title:  [R] Awesome-LLM-Reasoning-Foundations: a curated map of the THEORY of LLM reasoning

Body:
  Hi r/ML — I'm a PhD candidate working on the formal foundations of LLM
  reasoning. The applied/CoT/o1 lists on awesome-X are well-maintained,
  but I couldn't find an analogous curated index for the theory side of
  the field — Merrill et al. on circuit complexity, Strobl et al. on
  expressivity surveys, Chiang et al. on logical characterizations, the
  ICL-as-implicit-GD line from Garg / von Oswald / Akyürek / Bai, etc.

  So I made one. Every entry was checked against the canonical source
  (arXiv abstract page, OpenReview, ACL Anthology) — the verification
  log lives in the repo, and CI link-checks weekly.

  https://github.com/bettyguo/awesome-llm-reasoning-foundations

  Things I'd value feedback on:

  - The category structure (8 top-level).
  - Annotations — I'm aiming for "names the formal result; no
    superlatives". Calling out anything that drifts is welcome.
  - Important entries I missed. I deliberately left a few off because I
    couldn't verify them in time — the issue tab has a `wanted` label
    for community-filled gaps.

  Out of scope on purpose: methods (CoT prompting, scratchpads as a
  technique, agents). The README lists generous pointers to those lists.
```

### Newsletter outreach paragraph

For "The Batch" (DeepLearning.AI), "Import AI" (Jack Clark), or "Last Week in AI":

> A new curated bibliography of the *theoretical foundations* of LLM reasoning — expressivity, CoT error bounds, circuit / communication complexity, logical characterizations, learnability — has been published. Built by Betty Guo (Dongxin Guo), a PhD candidate at HKU working in the area; every entry was web-verified before inclusion; CI link-checks weekly. The list is deliberately distinct from the existing methods-focused lists. Currently 81 entries across 8 categories. https://github.com/bettyguo/awesome-llm-reasoning-foundations

## Post-launch loop (week 1)

- Triage incoming PRs and issues daily. The first wave decides whether contributors find the bar reasonable.
- For each `wanted` issue filed, post a one-line acknowledgment + an arXiv-search seed. Reduces the activation energy for first-time contributors.
- Track GitHub stars; expect a slow ramp. The week-1 number is uninformative; the month-1 number predicts everything.
- If a high-profile author in the list cites or links it from their group page, that's a stronger signal than any star spike. Note who and update outreach.

## Maintenance loop (ongoing)

- Weekly CI link-check (already scheduled in `.github/workflows/linkcheck.yml`).
- Quarterly "stale entry" sweep — re-check that every venue label still matches the canonical source (preprints get accepted, ICLR submissions become camera-ready, etc.).
- After each major venue cycle (ICLR / NeurIPS / ICML / ACL), spend an afternoon adding new in-scope papers from the proceedings.
