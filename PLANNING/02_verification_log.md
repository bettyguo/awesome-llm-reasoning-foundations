# Verification Log

Every published entry must have a `PASS` row here, keyed by slug, recording where title/authors/year/venue were verified. `DROP` rows record entries we considered but rejected (with a one-line reason).

`validate_entries.py` enforces this: any entry under `entries/` without a matching `PASS` row is a CI failure.

The verification URL listed is the source-of-truth used at the time of the check (typically the arXiv abstract page).

| Status | Slug | Title (as verified) | Source URL | Date checked |
|---|---|---|---|---|
| PASS | `yun-2020-universal-approx` | Are Transformers universal approximators of sequence-to-sequence functions? | https://arxiv.org/abs/1912.10077 | 2026-05-14 |
| PASS | `hahn-2020-self-attention-limits` | Theoretical Limitations of Self-Attention in Neural Sequence Models | https://arxiv.org/abs/1906.06755 | 2026-05-14 |
| PASS | `bhattamishra-2020-formal-languages` | On the Ability and Limitations of Transformers to Recognize Formal Languages | https://arxiv.org/abs/2009.11264 | 2026-05-14 |
| PASS | `bhattamishra-2020-computational-power` | On the Computational Power of Transformers and its Implications in Sequence Modeling | https://arxiv.org/abs/2006.09286 | 2026-05-14 |
| PASS | `yao-2021-bounded-hierarchical` | Self-Attention Networks Can Process Bounded Hierarchical Languages | https://arxiv.org/abs/2105.11115 | 2026-05-14 |
| PASS | `merrill-2022-saturated-tc0` | Saturated Transformers are Constant-Depth Threshold Circuits | https://arxiv.org/abs/2106.16213 | 2026-05-14 |
| PASS | `perez-2019-turing-completeness` | On the Turing Completeness of Modern Neural Network Architectures | https://arxiv.org/abs/1901.03429 | 2026-05-14 |
| PASS | `perez-2021-attention-turing` | Attention is Turing-Complete | https://jmlr.org/papers/v22/20-302.html | 2026-05-14 |
| PASS | `chiang-2023-tighter-bounds` | Tighter Bounds on the Expressivity of Transformer Encoders | https://arxiv.org/abs/2301.10743 | 2026-05-14 |
| PASS | `merrill-sabharwal-2024-cot` | The Expressive Power of Transformers with Chain of Thought | https://arxiv.org/abs/2310.07923 | 2026-05-14 |
| PASS | `feng-2023-cot-mystery` | Towards Revealing the Mystery behind Chain of Thought: A Theoretical Perspective | https://arxiv.org/abs/2305.15408 | 2026-05-14 |
| PASS | `li-2024-cot-serial` | Chain of Thought Empowers Transformers to Solve Inherently Serial Problems | https://arxiv.org/abs/2402.12875 | 2026-05-14 |
| PASS | `prystawski-2023-step-by-step` | Why think step by step? Reasoning emerges from the locality of experience | https://arxiv.org/abs/2304.03843 | 2026-05-14 |
| PASS | `wies-2023-subtask-decomposition` | Sub-Task Decomposition Enables Learning in Sequence to Sequence Tasks | https://arxiv.org/abs/2204.02892 | 2026-05-14 |
| PASS | `malach-2023-universal-learners` | Auto-Regressive Next-Token Predictors are Universal Learners | https://arxiv.org/abs/2309.06979 | 2026-05-14 |
| PASS | `merrill-sabharwal-2023-parallelism` | The Parallelism Tradeoff: Limitations of Log-Precision Transformers | https://arxiv.org/abs/2207.00729 | 2026-05-14 |
| PASS | `sanford-2024-log-depth` | Transformers, parallel computation, and logarithmic depth | https://arxiv.org/abs/2402.09268 | 2026-05-14 |
| PASS | `sanford-2023-representational` | Representational Strengths and Limitations of Transformers | https://arxiv.org/abs/2306.02896 | 2026-05-14 |
| PASS | `peng-2024-limitations` | On Limitations of the Transformer Architecture | https://arxiv.org/abs/2402.08164 | 2026-05-14 |
| PASS | `merrill-2024-illusion-of-state` | The Illusion of State in State-Space Models | https://arxiv.org/abs/2404.08819 | 2026-05-14 |
| PASS | `merrill-sabharwal-2023-logic` | A Logic for Expressing Log-Precision Transformers | https://arxiv.org/abs/2210.02671 | 2026-05-14 |
| PASS | `barcelo-2024-uhat-fol` | Logical Languages Accepted by Transformer Encoders with Hard Attention | https://arxiv.org/abs/2310.03817 | 2026-05-14 |
| PASS | `chiang-2022-overcoming` | Overcoming a Theoretical Limitation of Self-Attention | https://arxiv.org/abs/2202.12172 | 2026-05-14 |
| PASS | `yang-2024-masked-star-free` | Masked Hard-Attention Transformers Recognize Exactly the Star-Free Languages | https://arxiv.org/abs/2310.13897 | 2026-05-14 |
| PASS | `garg-2022-icl-function-classes` | What Can Transformers Learn In-Context? A Case Study of Simple Function Classes | https://arxiv.org/abs/2208.01066 | 2026-05-14 |
| PASS | `akyurek-2023-icl-linear` | What learning algorithm is in-context learning? Investigations with linear models | https://arxiv.org/abs/2211.15661 | 2026-05-14 |
| PASS | `vonoswald-2023-icl-gd` | Transformers learn in-context by gradient descent | https://arxiv.org/abs/2212.07677 | 2026-05-14 |
| PASS | `xie-2022-icl-bayes` | An Explanation of In-context Learning as Implicit Bayesian Inference | https://arxiv.org/abs/2111.02080 | 2026-05-14 |
| PASS | `raventos-2023-task-diversity` | Pretraining task diversity and the emergence of non-Bayesian in-context learning for regression | https://arxiv.org/abs/2306.15063 | 2026-05-14 |
| PASS | `edelman-2022-inductive-biases` | Inductive Biases and Variable Creation in Self-Attention Mechanisms | https://arxiv.org/abs/2110.10090 | 2026-05-14 |
| PASS | `zhang-2023-trained-transformers-linear` | Trained Transformers Learn Linear Models In-Context | https://arxiv.org/abs/2306.09927 | 2026-05-14 |
| PASS | `ahn-2023-preconditioned-gd` | Transformers learn to implement preconditioned gradient descent for in-context learning | https://arxiv.org/abs/2306.00297 | 2026-05-14 |
| PASS | `hahn-2023-emergent-icl` | A Theory of Emergent In-Context Learning as Implicit Structure Induction | https://arxiv.org/abs/2303.07971 | 2026-05-14 |
| PASS | `meng-2022-rome` | Locating and Editing Factual Associations in GPT | https://arxiv.org/abs/2202.05262 | 2026-05-14 |
| PASS | `meng-2023-memit` | Mass-Editing Memory in a Transformer | https://arxiv.org/abs/2210.07229 | 2026-05-14 |
| PASS | `hase-2023-localization` | Does Localization Inform Editing? Surprising Differences in Causality-Based Localization vs. Knowledge Editing in Language Models | https://arxiv.org/abs/2301.04213 | 2026-05-14 |
| PASS | `cohen-2024-ripple-effects` | Evaluating the Ripple Effects of Knowledge Editing in Language Models | https://arxiv.org/abs/2307.12976 | 2026-05-14 |
| PASS | `hahn-2024-sensitive-functions` | Why are Sensitive Functions Hard for Transformers? | https://arxiv.org/abs/2402.09963 | 2026-05-14 |
| PASS | `liu-2023-shortcuts-automata` | Transformers Learn Shortcuts to Automata | https://arxiv.org/abs/2210.10749 | 2026-05-14 |
| PASS | `zhou-2024-length-generalization` | What Algorithms can Transformers Learn? A Study in Length Generalization | https://arxiv.org/abs/2310.16028 | 2026-05-14 |
| PASS | `strobl-2024-formal-languages-survey` | What Formal Languages Can Transformers Express? A Survey | https://arxiv.org/abs/2311.00208 | 2026-05-14 |

## Drops at THINK stage (kept for transparency)

| Status | Slug candidate | Reason for drop |
|---|---|---|
| DROP | `bills-2023-explain-neurons` | OpenAI tech report; mechanistic-interpretability sibling, not a formal foundations result — better placed in `JShollaj/awesome-llm-interpretability`. |
| DROP | `wei-2022-cot-prompting` | Original CoT prompting paper is methods, not theory. Referenced by theoretical entries that build on it; not listed itself. |

## How to add a row

When you add a new entry, append a `PASS` row keyed by the entry's slug. Include:
- The exact title from the source.
- The URL you used to verify (prefer arXiv abstract page; OpenReview, ACL Anthology, or proceedings page are acceptable).
- ISO date of the check.

If verification fails (paper doesn't exist, authors wrong, year wrong), record a `DROP` row instead and do NOT create the YAML.
