# Verification Log

Every entry in `entries/` must have a `PASS` row below before it appears in the published list. `validate_entries.py` enforces this — adding a YAML without a row will fail CI.

**Format:** `| status | slug | source URL inspected | YYYY-MM-DD checked | evidence |`

- `status` is `PASS` (entry passes the gate; goes in the list) or `DROP` (failed verification; not in list).
- `evidence` is a one-line note about what was confirmed: title / authors / year / venue match.

## Phase 2 + Phase 3 — verified entries (2026-05-14)

Every row below corresponds to a YAML file under `entries/`. Sources were inspected on 2026-05-14 unless noted otherwise.

| status | slug | source URL | date | evidence |
|--------|------|------------|------|----------|
| PASS | `yun-2020-universal-approx` | https://arxiv.org/abs/1912.10077 | 2026-05-14 | arxiv abstract confirms title, authors (Yun, Bhojanapalli, Rawat, Reddi, Kumar), ICLR 2020 comment. |
| PASS | `hahn-2020-self-attention-limits` | https://arxiv.org/abs/1906.06755 | 2026-05-14 | arxiv abstract confirms title, sole author Hahn, TACL acceptance comment. |
| PASS | `bhattamishra-2020-formal-languages` | https://arxiv.org/abs/2009.11264 | 2026-05-14 | arxiv abstract confirms title, authors (Bhattamishra, Ahuja, Goyal), EMNLP 2020 comment. |
| PASS | `bhattamishra-2020-computational-power` | https://arxiv.org/abs/2006.09286 | 2026-05-14 | arxiv abstract confirms title, authors (Bhattamishra, Patel, Goyal), CoNLL 2020 comment. |
| PASS | `yao-2021-bounded-hierarchical` | https://arxiv.org/abs/2105.11115 | 2026-05-14 | arxiv abstract confirms title, authors (Yao, Peng, Papadimitriou, Narasimhan), ACL 2021 comment, code URL. |
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
| PASS | `barcelo-2024-uhat-fol` | https://arxiv.org/abs/2310.03817 | 2026-05-14 | arxiv abstract confirms title, authors (Barceló, Kozachinskiy, Lin, Podolskii); ICLR 2024 confirmed via OpenReview. |
| PASS | `chiang-2022-overcoming` | https://arxiv.org/abs/2202.12172 | 2026-05-14 | arxiv abstract confirms title, authors (Chiang, Cholak), ACL 2022 comment. |
| PASS | `yang-2024-masked-star-free` | https://arxiv.org/abs/2310.13897 | 2026-05-14 | arxiv abstract confirms title, authors (Yang, Chiang, Angluin), NeurIPS 2024 comment. |
| PASS | `garg-2022-icl-function-classes` | https://arxiv.org/abs/2208.01066 | 2026-05-14 | arxiv abstract confirms title, authors (Garg, Tsipras, Liang, Valiant); venue NeurIPS 2022 from common citation. |
| PASS | `akyurek-2023-icl-linear` | https://arxiv.org/abs/2211.15661 | 2026-05-14 | arxiv abstract confirms title, authors (Akyürek, Schuurmans, Andreas, Ma, Zhou), ICLR 2023 camera-ready comment. |
| PASS | `vonoswald-2023-icl-gd` | https://arxiv.org/abs/2212.07677 | 2026-05-14 | arxiv abstract confirms title, full 7-author list; venue ICML 2023 from common citation. |
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
| PASS | `liu-2023-shortcuts-automata` | https://arxiv.org/abs/2210.10749 | 2026-05-14 | arxiv abstract confirms title, full 5-author list; venue ICLR 2023 from common citation. |
| PASS | `zhou-2024-length-generalization` | https://arxiv.org/abs/2310.16028 | 2026-05-14 | arxiv abstract confirms title, full 8-author list; venue ICLR 2024 from common citation. |
| PASS | `strobl-2024-formal-languages-survey` | https://arxiv.org/abs/2311.00208 | 2026-05-14 | arxiv abstract confirms title, authors (Strobl, Merrill, Weiss, Chiang, Angluin), TACL 12:543-561 (2024). |
| PASS | `hao-2022-hard-attention-circuit` | https://arxiv.org/abs/2204.06618 | 2026-05-14 | arxiv abstract confirms title, authors (Hao, Angluin, Frank), TACL acceptance comment. |
| PASS | `bachmann-2024-pitfalls-next-token` | https://arxiv.org/abs/2403.06963 | 2026-05-14 | arxiv abstract confirms title, authors (Bachmann, Nagarajan), ICML 2024 comment. |
| PASS | `pfau-2024-dot-by-dot` | https://arxiv.org/abs/2404.15758 | 2026-05-14 | arxiv abstract confirms title, authors (Pfau, Merrill, Bowman); arxiv comment field empty. |
| PASS | `goyal-2024-pause-tokens` | https://arxiv.org/abs/2310.02226 | 2026-05-14 | arxiv abstract confirms title, full 6-author list (Goyal, Ji, Rawat, Menon, Kumar, Nagarajan), ICLR 2024 acceptance. |
| PASS | `chen-2024-provably-learning-mha` | https://arxiv.org/abs/2402.04084 | 2026-05-14 | arxiv abstract confirms title, authors (Chen, Li); arxiv comment "105 pages, comments welcome" — venue null. |
| PASS | `wang-2024-sparse-token-selection` | https://arxiv.org/abs/2406.06893 | 2026-05-14 | arxiv abstract confirms title, authors (Wang, Wei, Hsu, Lee); venue null. |
| PASS | `mahdavi-2023-memorization-capacity` | https://arxiv.org/abs/2306.02010 | 2026-05-14 | arxiv abstract confirms title, authors (Mahdavi, Liao, Thrampoulidis), ICLR 2024 Spotlight comment. |
| PASS | `yang-2024-counting-like-transformers` | https://arxiv.org/abs/2404.04393 | 2026-05-14 | arxiv abstract confirms title, authors (Yang, Chiang); arxiv comment field empty. |
| PASS | `olsson-2022-induction-heads` | https://arxiv.org/abs/2209.11895 | 2026-05-14 | arxiv abstract confirms title, full 26-author list led by Olsson; venue null (Anthropic tech report style). |
| PASS | `wen-2024-rnns-not-transformers` | https://arxiv.org/abs/2402.18510 | 2026-05-14 | arxiv abstract confirms title, authors (Wen, Dang, Lyu); venue null. |
| PASS | `akyurek-2024-in-context-language` | https://arxiv.org/abs/2401.12973 | 2026-05-14 | arxiv abstract confirms title, authors (Akyürek, Wang, Kim, Andreas); venue null. |
| PASS | `allenzhu-2023-physics-part1` | https://arxiv.org/abs/2305.13673 | 2026-05-14 | arxiv abstract confirms title, authors (Allen-Zhu, Li); part 1 of the "Physics of LMs" series. |
| PASS | `allenzhu-2023-physics-3-1` | https://arxiv.org/abs/2309.14316 | 2026-05-14 | arxiv abstract confirms title, authors (Allen-Zhu, Li); venue ICML 2024 per proceedings. |
| PASS | `allenzhu-2023-physics-3-2` | https://arxiv.org/abs/2309.14402 | 2026-05-14 | arxiv abstract confirms title, authors (Allen-Zhu, Li); venue null. |
| PASS | `mitchell-2022-mend` | https://arxiv.org/abs/2110.11309 | 2026-05-14 | arxiv abstract confirms title, authors (Mitchell, Lin, Bosselut, Finn, Manning), ICLR 2022 comment. |
| PASS | `decao-2021-editing-factual` | https://arxiv.org/abs/2104.08164 | 2026-05-14 | arxiv abstract confirms title, authors (De Cao, Aziz, Titov), EMNLP 2021 comment. |
| PASS | `geva-2021-ffn-key-value` | https://arxiv.org/abs/2012.14913 | 2026-05-14 | arxiv abstract confirms title, authors (Geva, Schuster, Berant, Levy), EMNLP 2021 comment. |
| PASS | `geva-2023-dissecting-recall` | https://arxiv.org/abs/2304.14767 | 2026-05-14 | arxiv abstract confirms title, authors (Geva, Bastings, Filippova, Globerson), EMNLP 2023 comment. |
| PASS | `anil-2022-length-generalization` | https://arxiv.org/abs/2207.04901 | 2026-05-14 | arxiv abstract confirms title, full 10-author list; venue NeurIPS 2022 from common citation. |
| PASS | `press-2022-alibi` | https://arxiv.org/abs/2108.12409 | 2026-05-14 | arxiv abstract confirms title, authors (Press, Smith, Lewis); venue ICLR 2022 from common citation. |
| PASS | `stechly-2024-self-verification-limits` | https://arxiv.org/abs/2402.08115 | 2026-05-14 | arxiv abstract confirms title, authors (Stechly, Valmeekam, Kambhampati); venue null. |
| PASS | `transformers-theory-workshop-2025` | https://transformerstheory.github.io/ | 2026-05-14 | workshop site confirms name "What Can('t) Transformers Do?", NeurIPS 2025, organizers (Schnabel, Tomlinson, Strobl, Hahn). |
| PASS | `deletang-2023-chomsky` | https://arxiv.org/abs/2207.02098 | 2026-05-14 | arxiv abstract confirms title, full 11-author list (Delétang et al.); venue ICLR 2023 from common citation (arxiv comment empty). |
| PASS | `lindner-2023-tracr` | https://arxiv.org/abs/2301.05062 | 2026-05-14 | arxiv abstract confirms title, authors (Lindner, Kramár, Farquhar, Rahtz, McGrath, Mikulik), NeurIPS 2023 Spotlight comment. |
| PASS | `merrill-2025-little-depth` | https://arxiv.org/abs/2503.03961 | 2026-05-14 | arxiv abstract confirms title, authors (Merrill, Sabharwal), NeurIPS 2025 comment. |
| PASS | `schuurmans-2023-memory-universal` | https://arxiv.org/abs/2301.04589 | 2026-05-14 | arxiv abstract confirms title, sole author Schuurmans; venue null. |
| PASS | `lanham-2023-faithfulness` | https://arxiv.org/abs/2307.13702 | 2026-05-14 | arxiv abstract confirms title, full 30-author Anthropic team led by Lanham; venue null. |
| PASS | `sprague-2025-cot-or-not` | https://arxiv.org/abs/2409.12183 | 2026-05-14 | arxiv abstract confirms title, full 10-author list led by Sprague, ICLR 2025 comment. |
| PASS | `kim-2025-parity-cot` | https://arxiv.org/abs/2410.08633 | 2026-05-14 | arxiv abstract confirms title, authors (Kim, Suzuki), ICLR 2025 Oral comment. |
| PASS | `tarzanagh-2023-svm` | https://arxiv.org/abs/2308.16898 | 2026-05-14 | arxiv abstract confirms title, authors (Tarzanagh, Li, Thrampoulidis, Oymak); venue null. |
| PASS | `ahn-2024-linear-attention` | https://arxiv.org/abs/2310.01082 | 2026-05-14 | arxiv abstract confirms title, full 6-author list, ICLR 2024 comment. |
| PASS | `wu-2024-pretraining-tasks` | https://arxiv.org/abs/2310.08391 | 2026-05-14 | arxiv abstract confirms title, full 6-author list, ICLR 2024 camera-ready comment. |
| PASS | `bietti-2023-birth` | https://arxiv.org/abs/2306.00802 | 2026-05-14 | arxiv abstract confirms title, authors (Bietti, Cabannes, Bouchacourt, Jégou, Bottou), NeurIPS 2023 comment. |
| PASS | `reddy-2024-mechanistic-icl` | https://arxiv.org/abs/2312.03002 | 2026-05-14 | arxiv abstract confirms title, sole author Reddy; venue ICLR 2024 from common citation. |
| PASS | `nichani-2024-causal` | https://arxiv.org/abs/2402.14735 | 2026-05-14 | arxiv abstract confirms title, authors (Nichani, Damian, Lee), ICML 2024 camera-ready comment. |
| PASS | `mitchell-2022-serac` | https://arxiv.org/abs/2206.06520 | 2026-05-14 | arxiv abstract confirms title, authors (Mitchell, Lin, Bosselut, Manning, Finn), ICML 2022 comment. |
| PASS | `yao-2023-editing-survey` | https://arxiv.org/abs/2305.13172 | 2026-05-14 | arxiv abstract confirms title, full 8-author list (Yao et al.), EMNLP 2023 comment. |
| PASS | `zhang-2024-editing-comprehensive` | https://arxiv.org/abs/2401.01286 | 2026-05-14 | arxiv abstract confirms title and full 22-author list led by Zhang; venue null (ongoing preprint). |
| PASS | `schaeffer-2023-mirage` | https://arxiv.org/abs/2304.15004 | 2026-05-14 | arxiv abstract confirms title, authors (Schaeffer, Miranda, Koyejo); venue NeurIPS 2023 from common citation. |
| PASS | `mahankali-2024-onestep-gd` | https://arxiv.org/abs/2307.03576 | 2026-05-14 | arxiv abstract confirms title, authors (Mahankali, Hashimoto, Ma); venue ICLR 2024 from common citation. |

## Drops

| status | slug candidate | reason |
|--------|----------------|--------|
| DROP | `bills-2023-explain-neurons` | OpenAI tech report; mechanistic-interpretability work, not a formal foundations result. Better fit for `JShollaj/awesome-llm-interpretability`. |
| DROP | `wei-2022-cot-prompting` | Original CoT prompting paper — methods, not theory. Linked from theory entries that build on it; not listed here. |
| DROP | `yao-2023-tree-of-thoughts` | Tree-of-Thoughts is a CoT methods paper — out of scope; linked from `atfortes/Awesome-LLM-Reasoning`. |
| DROP | `schaeffer-2023-mirage` | Phase 6 hostile review: paper is about scaling-law evaluation methodology, not LLM-reasoning theory. Verification passed but scope check failed — moved out of published list. |
| DROP | `stechly-2024-self-verification-limits` | Phase 6 hostile review: empirical negative result on self-verification, no formal theorem. Fails the "carries a formal foundations result" bar. Verification passed but scope check failed. |

## Notes

- Initial Phase 2 verification corrected two arxiv-ID mistakes in seed memory (`2305.03378` was a long-tailed-recognition paper, not the Logic paper; `2310.03659` was a multi-agent taxonomy paper, not the Barceló paper). The correct IDs (`2210.02671` and `2310.03817`) were located via search and re-verified before being used.
- Two author-list errors in initial memory were corrected against arxiv: Feng et al. 2023 (correct authors: Guhao Feng, Bohang Zhang, Yuntian Gu, Haotian Ye, Di He, Liwei Wang) and Li et al. 2024 (correct: Zhiyuan Li, Hong Liu, Denny Zhou, Tengyu Ma).
- One title in initial memory was a paraphrase: Strobl et al. — the arxiv canonical title is "What Formal Languages Can Transformers Express? A Survey".

## How to add a row

Append a `PASS` row keyed by the entry's slug. Include the URL used to verify (prefer arXiv abstract page; OpenReview, ACL Anthology, or proceedings page are acceptable), ISO date of the check, and one-line evidence noting which fields were cross-checked.

If verification fails (paper doesn't exist, authors wrong, year wrong), record a `DROP` row instead and do NOT create the YAML.
