# Wanted entries

This file lists entries the curator would like to add but is leaving as community-contribution opportunities, plus broader gaps surfaced by Phase 6 hostile review. The goal is to give first-time contributors a low-activation-energy starting point and to signal that the list is alive.

At launch, each item below should be filed as a GitHub issue with the `wanted` label so they appear in the README's *Wanted entries* link.

## Specific papers (verified, ready to be turned into entries)

These are verified-real, in-scope, and the curator simply hasn't written the YAML yet.

1. **Strobl, Angluin, Chiang, Rawski, Sabharwal (2024) — *Transformers as Transducers*.** TACL. arXiv:2404.02040.
2. **Back de Luca, Giapitzakis, Yang, Veličković, Fountoulakis (2024) — *Positional Attention: Expressivity and Learnability of Algorithmic Computation*.** ICML 2025. arXiv:2410.01686.
3. **William Merrill — *Formal Languages and the NLP Black Box*.** DLT 2023 keynote. https://lambdaviking.com/assets/pdf/papers/formal-languages-and-nlp-blackbox.pdf
4. **Wang, Zhu, Liu, Zheng, Chen, Li (2024) — *Knowledge Editing for Large Language Models: A Survey*.** ACM Computing Surveys. arXiv:2310.16218.

## Topic gaps (community asks)

Categories where the launch coverage is thinner than the literature warrants.

- **Logical Characterizations** (5 entries). Specifically wanted: recent FOC[Attn] / FO[+;MOD] / counting-logic results beyond the four entries already listed.
- **Communication-complexity lower bounds on multi-head attention.** Currently the only entries are `sanford-2023-representational` and `peng-2024-limitations`. The Bhattacharyya / Rao threads and related lower-bound work would broaden the picture.
- **State-space-model expressivity beyond `merrill-2024-illusion-of-state`.** Specifically the Sarrof / Veitsman / Hahn-style follow-ups quantifying which problems an SSM *can* solve.
- **Beyond-attention architectures.** Formal expressivity results on Mamba, RetNet, Hyena beyond the SSM-illusion entry.
- **Knowledge editing × theory crossovers.** Cohen-2024-ripple-effects opens a formal door; later impossibility-style theorems on knowledge editing belong on the list as they appear.
- **Recorded lecture-series / video courses on transformer theory.** Currently the surveys-and-talks category has only 2 published entries (after Phase 6 hostile-review drops). A high-quality recorded lecture series would substantially improve the entry-point experience.

## What "verified" means for contributors

See `PLANNING/01_design.md` § 4 — every new entry needs the canonical source URL (arXiv abstract / OpenReview / venue proceedings) confirming title, authors, year. The PR template walks through it; CI link-checks weekly.

## How to claim one

Open or comment on a `wanted` issue ("I'm taking #N") and submit a PR. The curator merges promptly when verification is clean. If a verification fails, the curator drops the entry rather than guessing — that's the whole bar.
