# Verification Log

Every entry in `entries/` must have a `PASS` row below before it appears in the published list. `validate_entries.py` enforces this — adding a YAML without a row will fail CI.

**Format:** `| status | slug | source URL inspected | YYYY-MM-DD checked | evidence |`

- `status` is `PASS` (entry passes the gate; goes in the list) or `DROP` (failed verification; not in list).
- `evidence` is a one-line note about what was confirmed: title / authors / year / venue match.

## Seed + Phase-3 expansion pass (2026-05-14)

| status | slug | source URL | date | evidence |
|--------|------|------------|------|----------|
| PASS | `ahn-2023-preconditioned-gd` | https://arxiv.org/abs/2306.00297 | 2026-05-14 | arxiv abstract confirms title, authors (Ahn, Cheng, Daneshmand, Sra), NeurIPS 2023. |
| PASS | `ahn-2024-linear-attention` | https://arxiv.org/abs/2310.01082 | 2026-05-14 | arxiv abstract confirms title, authors (Ahn, Cheng, Song, Yun, Jadbabaie, Sra), ICLR 2024. |
| PASS | `akyurek-2023-icl-linear` | https://arxiv.org/abs/2211.15661 | 2026-05-14 | arxiv abstract confirms title, authors (Akyürek, Schuurmans, Andreas, Ma, Zhou), ICLR 2023 camera-ready. |
| PASS | `akyurek-2024-in-context-language` | https://arxiv.org/abs/2401.12973 | 2026-05-14 | arxiv abstract confirms title, authors (Akyürek, Wang, Kim, Andreas). |
| PASS | `allenzhu-2023-physics-3-1` | https://arxiv.org/abs/2309.14316 | 2026-05-14 | arxiv abstract confirms title, authors (Allen-Zhu, Li). |
| PASS | `allenzhu-2023-physics-3-2` | https://arxiv.org/abs/2309.14402 | 2026-05-14 | arxiv abstract confirms title, authors (Allen-Zhu, Li). |
| PASS | `allenzhu-2023-physics-part1` | https://arxiv.org/abs/2305.13673 | 2026-05-14 | arxiv abstract confirms current title ("Learning Hierarchical Language Structures"), authors (Allen-Zhu, Li). |
| PASS | `anil-2022-length-generalization` | https://arxiv.org/abs/2207.04901 | 2026-05-14 | arxiv abstract confirms title, full author list. |
| PASS | `bachmann-2024-pitfalls-next-token` | https://arxiv.org/abs/2403.06963 | 2026-05-14 | arxiv abstract confirms title, authors (Bachmann, Nagarajan), ICML 2024. |
| PASS | `bai-2023-statisticians` | https://arxiv.org/abs/2306.04637 | 2026-05-14 | arxiv abstract confirms title, authors (Bai, Chen, Wang, Xiong, Mei). |
| PASS | `barcelo-2024-uhat-fol` | https://arxiv.org/abs/2310.03817 | 2026-05-14 | arxiv abstract confirms title, authors (Barceló, Kozachinskiy, Lin, Podolskii); ICLR 2024 via OpenReview. |
| PASS | `bhattamishra-2020-computational-power` | https://arxiv.org/abs/2006.09286 | 2026-05-14 | arxiv abstract confirms title, authors (Bhattamishra, Patel, Goyal), CoNLL 2020. |
| PASS | `bhattamishra-2020-formal-languages` | https://arxiv.org/abs/2009.11264 | 2026-05-14 | arxiv abstract confirms title, authors (Bhattamishra, Ahuja, Goyal), EMNLP 2020. |
| PASS | `bietti-2023-birth` | https://arxiv.org/abs/2306.00802 | 2026-05-14 | arxiv abstract confirms title, authors (Bietti, Cabannes, Bouchacourt, Jegou, Bottou), NeurIPS 2023. |
| PASS | `chen-2024-provably-learning-mha` | https://arxiv.org/abs/2402.04084 | 2026-05-14 | arxiv abstract confirms title, authors (Chen, Li). |
| PASS | `chiang-2022-overcoming` | https://arxiv.org/abs/2202.12172 | 2026-05-14 | arxiv abstract confirms title, authors (Chiang, Cholak), ACL 2022. |
| PASS | `chiang-2023-tighter-bounds` | https://arxiv.org/abs/2301.10743 | 2026-05-14 | arxiv abstract confirms title, authors (Chiang, Cholak, Pillay), ICML 2023. |
| PASS | `cohen-2024-ripple-effects` | https://arxiv.org/abs/2307.12976 | 2026-05-14 | arxiv abstract confirms title, authors (Cohen, Biran, Yoran, Globerson, Geva), TACL 2024. |
| PASS | `decao-2021-editing-factual` | https://arxiv.org/abs/2104.08164 | 2026-05-14 | arxiv abstract confirms title, authors (De Cao, Aziz, Titov), EMNLP 2021. |
| PASS | `deletang-2023-chomsky` | https://arxiv.org/abs/2207.02098 | 2026-05-14 | arxiv abstract confirms title, full Delétang et al. author list. |
| PASS | `dziri-2023-faith-fate` | https://arxiv.org/abs/2305.18654 | 2026-05-14 | arxiv abstract confirms title, full Dziri et al. author list, NeurIPS 2023. |
| PASS | `edelman-2022-inductive-biases` | https://arxiv.org/abs/2110.10090 | 2026-05-14 | arxiv abstract confirms title, authors (Edelman, Goel, Kakade, Zhang), ICML 2022. |
| PASS | `feng-2023-cot-mystery` | https://arxiv.org/abs/2305.15408 | 2026-05-14 | arxiv abstract confirms title, authors (Feng, Zhang, Gu, Ye, He, Wang), NeurIPS 2023 oral. |
| PASS | `friedman-2023-transformer-programs` | https://arxiv.org/abs/2306.01128 | 2026-05-14 | arxiv abstract confirms title, authors (Friedman, Wettig, Chen), NeurIPS 2023 oral. |
| PASS | `garg-2022-icl-function-classes` | https://arxiv.org/abs/2208.01066 | 2026-05-14 | arxiv abstract confirms title, authors (Garg, Tsipras, Liang, Valiant), NeurIPS 2022. |
| PASS | `geva-2021-ffn-key-value` | https://arxiv.org/abs/2012.14913 | 2026-05-14 | arxiv abstract confirms title, authors (Geva, Schuster, Berant, Levy), EMNLP 2021. |
| PASS | `geva-2023-dissecting-recall` | https://arxiv.org/abs/2304.14767 | 2026-05-14 | arxiv abstract confirms title, authors (Geva, Bastings, Filippova, Globerson), EMNLP 2023. |
| PASS | `goyal-2024-pause-tokens` | https://arxiv.org/abs/2310.02226 | 2026-05-14 | arxiv abstract confirms title, full author list, ICLR 2024. |
| PASS | `hahn-2020-self-attention-limits` | https://arxiv.org/abs/1906.06755 | 2026-05-14 | arxiv abstract confirms title, sole author Hahn, TACL. |
| PASS | `hahn-2023-emergent-icl` | https://arxiv.org/abs/2303.07971 | 2026-05-14 | arxiv abstract confirms title, authors (Hahn, Goyal). |
| PASS | `hahn-2024-sensitive-functions` | https://arxiv.org/abs/2402.09963 | 2026-05-14 | arxiv abstract confirms title, authors (Hahn, Rofin), ACL 2024. |
| PASS | `hao-2022-hard-attention-circuit` | https://arxiv.org/abs/2204.06618 | 2026-05-14 | arxiv abstract confirms title, authors (Hao, Angluin, Frank), TACL. |
| PASS | `hase-2023-localization` | https://arxiv.org/abs/2301.04213 | 2026-05-14 | arxiv abstract confirms title, authors (Hase, Bansal, Kim, Ghandeharioun), NeurIPS 2023 spotlight. |
| PASS | `kazemnejad-2023-pos-enc` | https://arxiv.org/abs/2305.19466 | 2026-05-14 | arxiv abstract confirms title, authors (Kazemnejad, Padhi, Ramamurthy, Das, Reddy), NeurIPS 2023. |
| PASS | `kim-2025-parity-cot` | https://arxiv.org/abs/2410.08633 | 2026-05-14 | arxiv abstract confirms title, authors (Kim, Suzuki), ICLR 2025 Oral. |
| PASS | `lanham-2023-faithfulness` | https://arxiv.org/abs/2307.13702 | 2026-05-14 | arxiv abstract confirms title, full Anthropic author list. |
| PASS | `li-2024-cot-serial` | https://arxiv.org/abs/2402.12875 | 2026-05-14 | arxiv abstract confirms title, authors (Li, Liu, Zhou, Ma), ICLR 2024. |
| PASS | `lindner-2023-tracr` | https://arxiv.org/abs/2301.05062 | 2026-05-14 | arxiv abstract confirms title, authors (Lindner et al.), NeurIPS 2023 Spotlight. |
| PASS | `liu-2023-flip-flop` | https://arxiv.org/abs/2306.00946 | 2026-05-14 | arxiv abstract confirms title, authors (Liu, Ash, Goel, Krishnamurthy, Zhang), NeurIPS 2023. |
| PASS | `liu-2023-shortcuts-automata` | https://arxiv.org/abs/2210.10749 | 2026-05-14 | arxiv abstract confirms title, authors (Liu, Ash, Goel, Krishnamurthy, Zhang), ICLR 2023. |
| PASS | `mahankali-2024-onestep-gd` | https://arxiv.org/abs/2307.03576 | 2026-05-14 | arxiv abstract confirms title, authors (Mahankali, Hashimoto, Ma), ICLR 2024. |
| PASS | `mahdavi-2023-memorization-capacity` | https://arxiv.org/abs/2306.02010 | 2026-05-14 | arxiv abstract confirms title, authors (Mahdavi, Liao, Thrampoulidis), ICLR 2024 Spotlight. |
| PASS | `malach-2023-universal-learners` | https://arxiv.org/abs/2309.06979 | 2026-05-14 | arxiv abstract confirms title, sole author Malach. |
| PASS | `meng-2022-rome` | https://arxiv.org/abs/2202.05262 | 2026-05-14 | arxiv abstract confirms title, authors (Meng, Bau, Andonian, Belinkov), NeurIPS 2022. |
| PASS | `meng-2023-memit` | https://arxiv.org/abs/2210.07229 | 2026-05-14 | arxiv abstract confirms title, authors (Meng, Sen Sharma, Andonian, Belinkov, Bau), ICLR 2023. |
| PASS | `merrill-2022-saturated-tc0` | https://arxiv.org/abs/2106.16213 | 2026-05-14 | arxiv abstract confirms title, authors (Merrill, Sabharwal, Smith), TACL. |
| PASS | `merrill-2024-illusion-of-state` | https://arxiv.org/abs/2404.08819 | 2026-05-14 | arxiv abstract confirms title, authors (Merrill, Petty, Sabharwal), ICML 2024. |
| PASS | `merrill-2025-little-depth` | https://arxiv.org/abs/2503.03961 | 2026-05-14 | arxiv abstract confirms title, authors (Merrill, Sabharwal), NeurIPS 2025. |
| PASS | `merrill-sabharwal-2023-logic` | https://arxiv.org/abs/2210.02671 | 2026-05-14 | arxiv abstract confirms title, authors (Merrill, Sabharwal), NeurIPS 2023. |
| PASS | `merrill-sabharwal-2023-parallelism` | https://arxiv.org/abs/2207.00729 | 2026-05-14 | arxiv abstract confirms title, authors (Merrill, Sabharwal), TACL. |
| PASS | `merrill-sabharwal-2024-cot` | https://arxiv.org/abs/2310.07923 | 2026-05-14 | arxiv abstract confirms title, authors (Merrill, Sabharwal), ICLR 2024. |
| PASS | `mitchell-2022-mend` | https://arxiv.org/abs/2110.11309 | 2026-05-14 | arxiv abstract confirms title, authors (Mitchell, Lin, Bosselut, Finn, Manning), ICLR 2022. |
| PASS | `mitchell-2022-serac` | https://arxiv.org/abs/2206.06520 | 2026-05-14 | arxiv abstract confirms title, authors (Mitchell, Lin, Bosselut, Manning, Finn), ICML 2022. |
| PASS | `nichani-2024-causal` | https://arxiv.org/abs/2402.14735 | 2026-05-14 | arxiv abstract confirms title, authors (Nichani, Damian, Lee), ICML 2024. |
| PASS | `olsson-2022-induction-heads` | https://arxiv.org/abs/2209.11895 | 2026-05-14 | arxiv abstract confirms title, full Anthropic author list. |
| PASS | `peng-2024-limitations` | https://arxiv.org/abs/2402.08164 | 2026-05-14 | arxiv abstract confirms title, authors (Peng, Narayanan, Papadimitriou). |
| PASS | `perez-2019-turing-completeness` | https://arxiv.org/abs/1901.03429 | 2026-05-14 | arxiv abstract confirms title, authors (Pérez, Marinković, Barceló), ICLR 2019. |
| PASS | `perez-2021-attention-turing` | https://jmlr.org/papers/v22/20-302.html | 2026-05-14 | JMLR landing confirms title, authors (Pérez, Barceló, Marinkovic), JMLR vol 22 (2021). |
| PASS | `pfau-2024-dot-by-dot` | https://arxiv.org/abs/2404.15758 | 2026-05-14 | arxiv abstract confirms title, authors (Pfau, Merrill, Bowman). |
| PASS | `press-2022-alibi` | https://arxiv.org/abs/2108.12409 | 2026-05-14 | arxiv abstract confirms title, authors (Press, Smith, Lewis); ICLR 2022. |
| PASS | `prystawski-2023-step-by-step` | https://arxiv.org/abs/2304.03843 | 2026-05-14 | arxiv abstract confirms title, authors (Prystawski, Li, Goodman). |
| PASS | `raventos-2023-task-diversity` | https://arxiv.org/abs/2306.15063 | 2026-05-14 | arxiv abstract confirms title, authors (Raventós, Paul, Chen, Ganguli), NeurIPS 2023. |
| PASS | `reddy-2024-mechanistic-icl` | https://arxiv.org/abs/2312.03002 | 2026-05-14 | arxiv abstract confirms title, sole author Reddy. |
| PASS | `ruoss-2023-random-pos` | https://arxiv.org/abs/2305.16843 | 2026-05-14 | arxiv abstract confirms title, full author list (Ruoss et al.). |
| PASS | `sanford-2023-representational` | https://arxiv.org/abs/2306.02896 | 2026-05-14 | arxiv abstract confirms title, authors (Sanford, Hsu, Telgarsky), NeurIPS 2023. |
| PASS | `sanford-2024-log-depth` | https://arxiv.org/abs/2402.09268 | 2026-05-14 | arxiv abstract confirms title, authors (Sanford, Hsu, Telgarsky). |
| PASS | `schaeffer-2023-mirage` | https://arxiv.org/abs/2304.15004 | 2026-05-14 | arxiv abstract confirms title, authors (Schaeffer, Miranda, Koyejo), NeurIPS 2023. |
| PASS | `schuurmans-2023-memory-universal` | https://arxiv.org/abs/2301.04589 | 2026-05-14 | arxiv abstract confirms title, sole author Schuurmans. |
| PASS | `sprague-2025-cot-or-not` | https://arxiv.org/abs/2409.12183 | 2026-05-14 | arxiv abstract confirms title, full author list, ICLR 2025. |
| PASS | `stechly-2024-self-verification-limits` | https://arxiv.org/abs/2402.08115 | 2026-05-14 | arxiv abstract confirms title, authors (Stechly, Valmeekam, Kambhampati). |
| PASS | `strobl-2023-ahat-tc0` | https://arxiv.org/abs/2308.03212 | 2026-05-14 | arxiv abstract confirms title, sole author Strobl. |
| PASS | `strobl-2024-formal-languages-survey` | https://arxiv.org/abs/2311.00208 | 2026-05-14 | arxiv abstract confirms title, authors (Strobl, Merrill, Weiss, Chiang, Angluin), TACL 2024. |
| PASS | `tarzanagh-2023-svm` | https://arxiv.org/abs/2308.16898 | 2026-05-14 | arxiv abstract confirms title, authors (Tarzanagh, Li, Thrampoulidis, Oymak). |
| PASS | `transformers-theory-workshop-2025` | https://transformerstheory.github.io/ | 2026-05-14 | workshop landing page confirms NeurIPS 2025 workshop, organizers Schnabel/Tomlinson/Strobl/Hahn. |
| PASS | `vonoswald-2023-icl-gd` | https://arxiv.org/abs/2212.07677 | 2026-05-14 | arxiv abstract confirms title, full author list, ICML 2023. |
| PASS | `wang-2024-sparse-token-selection` | https://arxiv.org/abs/2406.06893 | 2026-05-14 | arxiv abstract confirms title, authors (Wang, Wei, Hsu, Lee). |
| PASS | `weiss-2021-rasp` | https://arxiv.org/abs/2106.06981 | 2026-05-14 | arxiv abstract confirms title "Thinking Like Transformers", authors (Weiss, Goldberg, Yahav), ICML 2021. |
| PASS | `wen-2024-rnns-not-transformers` | https://arxiv.org/abs/2402.18510 | 2026-05-14 | arxiv abstract confirms title, authors (Wen, Dang, Lyu). |
| PASS | `wies-2023-subtask-decomposition` | https://arxiv.org/abs/2204.02892 | 2026-05-14 | arxiv abstract confirms title, authors (Wies, Levine, Shashua), ICLR 2023. |
| PASS | `wu-2024-pretraining-tasks` | https://arxiv.org/abs/2310.08391 | 2026-05-14 | arxiv abstract confirms title, full author list, ICLR 2024. |
| PASS | `xie-2022-icl-bayes` | https://arxiv.org/abs/2111.02080 | 2026-05-14 | arxiv abstract confirms title, authors (Xie, Raghunathan, Liang, Ma), ICLR 2022. |
| PASS | `yang-2024-counting-like-transformers` | https://arxiv.org/abs/2404.04393 | 2026-05-14 | arxiv abstract confirms title, authors (Yang, Chiang). |
| PASS | `yang-2024-masked-star-free` | https://arxiv.org/abs/2310.13897 | 2026-05-14 | arxiv abstract confirms title, authors (Yang, Chiang, Angluin), NeurIPS 2024. |
| PASS | `yao-2021-bounded-hierarchical` | https://arxiv.org/abs/2105.11115 | 2026-05-14 | arxiv abstract confirms title, authors (Yao, Peng, Papadimitriou, Narasimhan), ACL 2021. |
| PASS | `yao-2023-editing-survey` | https://arxiv.org/abs/2305.13172 | 2026-05-14 | arxiv abstract confirms title, full author list (Yao et al.), EMNLP 2023. |
| PASS | `yun-2020-universal-approx` | https://arxiv.org/abs/1912.10077 | 2026-05-14 | arxiv abstract confirms title, authors (Yun, Bhojanapalli, Rawat, Reddi, Kumar), ICLR 2020. |
| PASS | `zhang-2023-trained-transformers-linear` | https://arxiv.org/abs/2306.09927 | 2026-05-14 | arxiv abstract confirms title, authors (Zhang, Frei, Bartlett). |
| PASS | `zhang-2024-editing-comprehensive` | https://arxiv.org/abs/2401.01286 | 2026-05-14 | arxiv abstract confirms title, full author list (Zhang et al., 22 authors). |
| PASS | `zhou-2024-length-generalization` | https://arxiv.org/abs/2310.16028 | 2026-05-14 | arxiv abstract confirms title, full author list, ICLR 2024. |

## Drops at THINK stage (kept for transparency)

| status | slug candidate | reason for drop |
|--------|----------------|-----------------|
| DROP | `bills-2023-explain-neurons` | OpenAI tech report; mechanistic-interpretability sibling, not a formal foundations result — better placed in `JShollaj/awesome-llm-interpretability`. |
| DROP | `wei-2022-cot-prompting` | Original CoT prompting paper is methods, not theory. Referenced by theoretical entries that build on it; not listed itself. |

## Notes for contributors

When you add a new entry, append a `PASS` row keyed by the entry's slug:
1. Use the exact title from the source (arXiv abstract, OpenReview, ACL Anthology, JMLR landing page, or official proceedings).
2. Record the URL you consulted.
3. Use today's date (ISO format).
4. One-line evidence: "arxiv abstract confirms title, authors, venue."

If verification fails (paper doesn't exist, authors wrong, year wrong), add a `DROP` row instead and do NOT create the YAML.
