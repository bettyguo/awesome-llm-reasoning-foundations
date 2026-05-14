# Verification Log

Every entry in `entries/` must have a `PASS` row below before it appears in the published list. `validate_entries.py` enforces this — adding a YAML without a row will fail CI.

**Format:** `| status | slug | source URL inspected | YYYY-MM-DD checked | evidence |`

- `status` is `PASS` (entry passes the gate; goes in the list) or `DROP` (failed verification; not in list).
- `evidence` is a one-line note about what was confirmed: title / authors / year / venue match.

## Seed pass — Phase 2 (2026-05-14)

| status | slug | source URL | date | evidence |
|--------|------|------------|------|----------|
| PASS | `yun-2020-universal-approx` | https://arxiv.org/abs/1912.10077 | 2026-05-14 | arxiv abstract confirms title, authors (Yun, Bhojanapalli, Rawat, Reddi, Kumar), and ICLR 2020 comment. |
| PASS | `hahn-2020-self-attention-limits` | https://arxiv.org/abs/1906.06755 | 2026-05-14 | arxiv abstract confirms title, sole author Hahn, and TACL acceptance comment. |
| PASS | `bhattamishra-2020-formal-languages` | https://arxiv.org/abs/2009.11264 | 2026-05-14 | arxiv abstract confirms title, authors (Bhattamishra, Ahuja, Goyal), and EMNLP 2020 comment. |
| PASS | `bhattamishra-2020-computational-power` | https://arxiv.org/abs/2006.09286 | 2026-05-14 | arxiv abstract confirms title, authors (Bhattamishra, Patel, Goyal), and CoNLL 2020 comment. |
| PASS | `yao-2021-bounded-hierarchical` | https://arxiv.org/abs/2105.11115 | 2026-05-14 | arxiv abstract confirms title, authors (Yao, Peng, Papadimitriou, Narasimhan), ACL 2021 comment, and code URL. |
| PASS | `merrill-2022-saturated-tc0` | https://arxiv.org/abs/2106.16213 | 2026-05-14 | arxiv abstract confirms title, authors (Merrill, Sabharwal, Smith), TACL acceptance comment. |
| PASS | `perez-2019-turing-completeness` | https://arxiv.org/abs/1901.03429 | 2026-05-14 | arxiv abstract confirms title, authors (Pérez, Marinković, Barceló), ICLR 2019 camera-ready comment. |
| PASS | `perez-2021-attention-turing` | https://jmlr.org/papers/v22/20-302.html | 2026-05-14 | JMLR landing page confirms title, authors (Pérez, Barceló, Marinkovic), JMLR vol 22 (2021). |
| PASS | `chiang-2023-tighter-bounds` | https://arxiv.org/abs/2301.10743 | 2026-05-14 | arxiv abstract confirms title, authors (Chiang, Cholak, Pillay), ICML 2023 comment. |
| PASS | `merrill-sabharwal-2024-cot` | https://arxiv.org/abs/2310.07923 | 2026-05-14 | arxiv abstract confirms title, authors (Merrill, Sabharwal), ICLR 2024 camera-ready comment. |
| PASS | `feng-2023-cot-mystery` | https://arxiv.org/abs/2305.15408 | 2026-05-14 | arxiv abstract confirms title, authors (Feng, Zhang, Gu, Ye, He, Wang), NeurIPS 2023 oral comment. |
| PASS | `li-2024-cot-serial` | https://arxiv.org/abs/2402.12875 | 2026-05-14 | arxiv abstract confirms title, authors (Li, Liu, Zhou, Ma), ICLR 2024 comment. |
| PASS | `prystawski-2023-step-by-step` | https://arxiv.org/abs/2304.03843 | 2026-05-14 | arxiv abstract confirms title, authors (Prystawski, Li, Goodman); venue intentionally left null since arxiv does not state. |
| PASS | `wies-2023-subtask-decomposition` | https://arxiv.org/abs/2204.02892 | 2026-05-14 | arxiv abstract confirms title, authors (Wies, Levine, Shashua), ICLR 2023 comment. |
| PASS | `malach-2023-universal-learners` | https://arxiv.org/abs/2309.06979 | 2026-05-14 | arxiv abstract confirms title, sole author Malach; venue null pending confirmation. |
| PASS | `merrill-sabharwal-2023-parallelism` | https://arxiv.org/abs/2207.00729 | 2026-05-14 | arxiv abstract confirms title, authors (Merrill, Sabharwal), TACL acceptance. |
| PASS | `sanford-2024-log-depth` | https://arxiv.org/abs/2402.09268 | 2026-05-14 | arxiv abstract confirms title, authors (Sanford, Hsu, Telgarsky); venue null pending confirmation. |
| PASS | `sanford-2023-representational` | https://arxiv.org/abs/2306.02896 | 2026-05-14 | arxiv abstract confirms title, authors (Sanford, Hsu, Telgarsky); venue NeurIPS 2023 from common citation. |
| PASS | `peng-2024-limitations` | https://arxiv.org/abs/2402.08164 | 2026-05-14 | arxiv abstract confirms title, authors (Peng, Narayanan, Papadimitriou); venue null pending confirmation. |
| PASS | `merrill-2024-illusion-of-state` | https://arxiv.org/abs/2404.08819 | 2026-05-14 | arxiv abstract confirms title, authors (Merrill, Petty, Sabharwal), ICML 2024 comment. |
| PASS | `merrill-sabharwal-2023-logic` | https://arxiv.org/abs/2210.02671 | 2026-05-14 | arxiv abstract confirms title, authors (Merrill, Sabharwal), NeurIPS 2023 acceptance. |
| PASS | `barcelo-2024-uhat-fol` | https://arxiv.org/abs/2310.03817 | 2026-05-14 | arxiv abstract confirms title, authors (Barceló, Kozachinskiy, Lin, Podolskii); ICLR 2024 confirmed via OpenReview entry returned by search. |
| PASS | `chiang-2022-overcoming` | https://arxiv.org/abs/2202.12172 | 2026-05-14 | arxiv abstract confirms title, authors (Chiang, Cholak), ACL 2022 comment. |
| PASS | `yang-2024-masked-star-free` | https://arxiv.org/abs/2310.13897 | 2026-05-14 | arxiv abstract confirms title, authors (Yang, Chiang, Angluin), NeurIPS 2024 comment. |
| PASS | `garg-2022-icl-function-classes` | https://arxiv.org/abs/2208.01066 | 2026-05-14 | arxiv abstract confirms title, authors (Garg, Tsipras, Liang, Valiant); venue NeurIPS 2022 from common citation. |
| PASS | `akyurek-2023-icl-linear` | https://arxiv.org/abs/2211.15661 | 2026-05-14 | arxiv abstract confirms title, authors (Akyürek, Schuurmans, Andreas, Ma, Zhou), ICLR 2023 camera-ready comment. |
| PASS | `vonoswald-2023-icl-gd` | https://arxiv.org/abs/2212.07677 | 2026-05-14 | arxiv abstract confirms title, authors (von Oswald, Niklasson, Randazzo, Sacramento, Mordvintsev, Zhmoginov, Vladymyrov); venue ICML 2023 from common citation. |
| PASS | `xie-2022-icl-bayes` | https://arxiv.org/abs/2111.02080 | 2026-05-14 | arxiv abstract confirms title, authors (Xie, Raghunathan, Liang, Ma), ICLR 2022 comment. |
| PASS | `raventos-2023-task-diversity` | https://arxiv.org/abs/2306.15063 | 2026-05-14 | arxiv abstract confirms title, authors (Raventós, Paul, Chen, Ganguli); venue NeurIPS 2023 from common citation. |
| PASS | `edelman-2022-inductive-biases` | https://arxiv.org/abs/2110.10090 | 2026-05-14 | arxiv abstract confirms title, authors (Edelman, Goel, Kakade, Zhang), ICML 2022 camera-ready comment. |
| PASS | `zhang-2023-trained-transformers-linear` | https://arxiv.org/abs/2306.09927 | 2026-05-14 | arxiv abstract confirms title, authors (Zhang, Frei, Bartlett); venue null pending confirmation. |
| PASS | `ahn-2023-preconditioned-gd` | https://arxiv.org/abs/2306.00297 | 2026-05-14 | arxiv abstract confirms title, authors (Ahn, Cheng, Daneshmand, Sra), NeurIPS 2023 comment. |
| PASS | `hahn-2023-emergent-icl` | https://arxiv.org/abs/2303.07971 | 2026-05-14 | arxiv abstract confirms title, authors (Hahn, Goyal); venue null pending confirmation. |
| PASS | `meng-2022-rome` | https://arxiv.org/abs/2202.05262 | 2026-05-14 | arxiv abstract confirms title, authors (Meng, Bau, Andonian, Belinkov), NeurIPS 2022. |
| PASS | `meng-2023-memit` | https://arxiv.org/abs/2210.07229 | 2026-05-14 | arxiv abstract confirms title, authors (Meng, Sen Sharma, Andonian, Belinkov, Bau); venue ICLR 2023 from common citation. |
| PASS | `hase-2023-localization` | https://arxiv.org/abs/2301.04213 | 2026-05-14 | arxiv abstract confirms title, authors (Hase, Bansal, Kim, Ghandeharioun), NeurIPS 2023 spotlight comment. |
| PASS | `cohen-2024-ripple-effects` | https://arxiv.org/abs/2307.12976 | 2026-05-14 | arxiv abstract confirms title, authors (Cohen, Biran, Yoran, Globerson, Geva), TACL 2024 acceptance. |
| PASS | `hahn-2024-sensitive-functions` | https://arxiv.org/abs/2402.09963 | 2026-05-14 | arxiv abstract confirms title, authors (Hahn, Rofin), ACL 2024 comment. |
| PASS | `liu-2023-shortcuts-automata` | https://arxiv.org/abs/2210.10749 | 2026-05-14 | arxiv abstract confirms title, authors (Liu, Ash, Goel, Krishnamurthy, Zhang); venue ICLR 2023 from common citation. |
| PASS | `zhou-2024-length-generalization` | https://arxiv.org/abs/2310.16028 | 2026-05-14 | arxiv abstract confirms title, authors (Zhou, Bradley, Littwin, Razin, Saremi, Susskind, Bengio, Nakkiran); venue ICLR 2024 from common citation. |
| PASS | `strobl-2024-formal-languages-survey` | https://arxiv.org/abs/2311.00208 | 2026-05-14 | arxiv abstract confirms title, authors (Strobl, Merrill, Weiss, Chiang, Angluin), TACL 12:543-561 (2024). |

## Drops

| status | slug candidate | reason |
|--------|----------------|--------|
| DROP | `bills-2023-explain-neurons` | OpenAI tech report; mechanistic-interpretability work, not a formal foundations result. Better fit for `JShollaj/awesome-llm-interpretability`. |
| DROP | `wei-2022-cot-prompting` | The original CoT prompting paper is a methods paper, not theory. Linked from theory entries that build on it; not listed in this repo. |

## Notes from seed pass

- Two arxiv IDs from initial memory turned out to point at unrelated papers (`2305.03378` is a long-tailed-recognition paper, not the Logic paper; `2310.03659` is a multi-agent taxonomy paper, not the Barceló paper). The correct IDs (`2210.02671` and `2310.03817`) were located via web search and re-verified before being used. This is exactly what the verification gate is for.
- Two author-list errors in initial memory were corrected against the arxiv abstract pages: Feng et al. 2023 (correct: Guhao Feng, Bohang Zhang, Yuntian Gu, Haotian Ye, Di He, Liwei Wang) and Li et al. 2024 (correct: Zhiyuan Li, Hong Liu, Denny Zhou, Tengyu Ma).
- One title in the seed bibliography was a paraphrase rather than the published title (Strobl et al. — correct arxiv title: "What Formal Languages Can Transformers Express? A Survey").

## How to add a row

When you add a new entry, append a `PASS` row keyed by the entry's slug. Include:
- the URL used to verify (prefer arXiv abstract page; OpenReview, ACL Anthology, or proceedings page are acceptable);
- ISO date of the check;
- one-line evidence noting which fields were cross-checked.

If verification fails (paper doesn't exist, authors wrong, year wrong), record a `DROP` row instead and do NOT create the YAML.
