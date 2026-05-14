<!-- THIS FILE IS GENERATED. Edit entries/*.yaml and run `python tools/build_readme.py`. -->

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

## Contents

- [Expressivity & Representational Limits](#expressivity-representational-limits) (9)
- [Chain-of-Thought: Theory & Error Bounds](#chain-of-thought-theory-error-bounds) (6)
- [Circuit & Communication Complexity](#circuit-communication-complexity) (5)
- [Logical Characterizations](#logical-characterizations) (4)
- [Learnability & Sample Complexity](#learnability-sample-complexity) (9)
- [Knowledge Editing & Impossibility Results](#knowledge-editing-impossibility-results) (4)
- [Parallel / Architectural Complexity & Scaling](#parallel-architectural-complexity-scaling) (3)
- [Surveys, Lecture Notes & Talks](#surveys-lecture-notes-talks) (1)

## Expressivity & Representational Limits

- **Tighter Bounds on the Expressivity of Transformer Encoders** — David Chiang, Peter Cholak, Anand Pillay (2023, ICML 2023). [paper](https://arxiv.org/abs/2301.10743). _Why it matters:_ Sharpens the upper-bound side of transformer expressivity by characterizing fixed-precision soft-attention encoders within a counting-extension of first-order logic — a precursor to the logical-characterization line.
- **Saturated Transformers are Constant-Depth Threshold Circuits** — William Merrill, Ashish Sabharwal, Noah A. Smith (2022, TACL 2022). [paper](https://arxiv.org/abs/2106.16213). _Why it matters:_ Shows that saturated-attention transformers (a hard-attention idealization with averaging over maxima) are simulable by uniform TC0 circuits, placing a hard upper bound on what such transformers can compute.
- **Attention is Turing-Complete** — Jorge Pérez, Pablo Barceló, Javier Marinkovic (2021, JMLR 22(75):1-35, 2021). [paper](https://jmlr.org/papers/v22/20-302.html). _Why it matters:_ Refines the earlier ICLR 2019 result to show that a hard-attention Transformer alone — without residual or other architectural extras — already simulates any Turing machine under unbounded precision.
- **Self-Attention Networks Can Process Bounded Hierarchical Languages** — Shunyu Yao et al. (2021, ACL 2021). [paper](https://arxiv.org/abs/2105.11115) · [code](https://github.com/princeton-nlp/dyck-transformer). _Why it matters:_ Constructs O(log n)-depth transformers recognizing Dyck-k with bounded nesting depth, showing self-attention's depth-vs-stack tradeoff for hierarchical languages.
- **On the Computational Power of Transformers and its Implications in Sequence Modeling** — Satwik Bhattamishra, Arkil Patel, Navin Goyal (2020, CoNLL 2020). [paper](https://arxiv.org/abs/2006.09286). _Why it matters:_ Gives a Turing-completeness argument for transformer encoder-decoders under unbounded-precision assumptions and pinpoints residual connections and positional encodings as load-bearing for the construction.
- **On the Ability and Limitations of Transformers to Recognize Formal Languages** — Satwik Bhattamishra, Kabir Ahuja, Navin Goyal (2020, EMNLP 2020). [paper](https://arxiv.org/abs/2009.11264). _Why it matters:_ Empirically separates which counter, shuffle, and Dyck languages transformers can and cannot recognize, anchoring later theoretical work on transformer expressivity in concrete language-class boundaries.
- **Theoretical Limitations of Self-Attention in Neural Sequence Models** — Michael Hahn (2020, TACL 2020). [paper](https://arxiv.org/abs/1906.06755). _Why it matters:_ Shows that hard-attention transformers cannot model Parity or Dyck-2, and that soft-attention transformers solve them only with attention entropy growing in input length — an early formal obstruction to in-distribution length generalization.
- **Are Transformers universal approximators of sequence-to-sequence functions?** — Chulhee Yun et al. (2020, ICLR 2020). [paper](https://arxiv.org/abs/1912.10077). _Why it matters:_ Proves that transformers with fixed width can universally approximate continuous permutation-equivariant sequence-to-sequence functions on compact domains, isolating positional encodings as the source of the non-equivariant extension.
- **On the Turing Completeness of Modern Neural Network Architectures** — Jorge Pérez, Javier Marinković, Pablo Barceló (2019, ICLR 2019). [paper](https://arxiv.org/abs/1901.03429). _Why it matters:_ Proves Turing-completeness for the Transformer and Neural GPU under unbounded precision and arbitrary input access, while flagging that the construction relies on conditions not satisfied by practical implementations.

## Chain-of-Thought: Theory & Error Bounds

- **Chain of Thought Empowers Transformers to Solve Inherently Serial Problems** — Zhiyuan Li et al. (2024, ICLR 2024). [paper](https://arxiv.org/abs/2402.12875). _Why it matters:_ Proves that with T(n) steps of CoT a constant-depth transformer simulates T(n)-step sequential computation, recovering serial-complexity classes that lie outside the parallel reach of a single forward pass.
- **The Expressive Power of Transformers with Chain of Thought** — William Merrill, Ashish Sabharwal (2024, ICLR 2024). [paper](https://arxiv.org/abs/2310.07923) · [openreview](https://openreview.net/forum?id=NjNGlPh8Wh). _Why it matters:_ Characterizes the expressive power of decoder-only transformers with intermediate CoT tokens as a function of generation length: log-many steps stay in TC0, linear-many reach P, polynomial-many reach EXPTIME.
- **Towards Revealing the Mystery behind Chain of Thought: A Theoretical Perspective** — Guhao Feng et al. (2023, NeurIPS 2023). [paper](https://arxiv.org/abs/2305.15408). _Why it matters:_ Constructs a constant-size CoT transformer that solves arithmetic and dynamic-programming tasks unreachable by any fixed-depth no-CoT transformer, giving an unconditional separation between with-CoT and without-CoT expressivity.
- **Auto-Regressive Next-Token Predictors are Universal Learners** — Eran Malach (2023). [paper](https://arxiv.org/abs/2309.06979). _Why it matters:_ Shows that autoregressive next-token prediction with a chain of thought is a universal learner: any efficiently computable function can be expressed by an autoregressive predictor with polynomially-bounded intermediate token complexity.
- **Why think step by step? Reasoning emerges from the locality of experience** — Ben Prystawski, Michael Y. Li, Noah D. Goodman (2023). [paper](https://arxiv.org/abs/2304.03843). _Why it matters:_ Shows in a Bayesian-network model that CoT helps precisely when training-time evidence is locally connected but globally sparse — chained inference recovers conditional independencies that direct prediction cannot.
- **Sub-Task Decomposition Enables Learning in Sequence to Sequence Tasks** — Noam Wies, Yoav Levine, Amnon Shashua (2023, ICLR 2023). [paper](https://arxiv.org/abs/2204.02892). _Why it matters:_ Proves a learnability separation: composite sequence-to-sequence tasks that are hard to learn end-to-end become PAC-learnable once decomposed into sub-tasks at training time — an early formal case for intermediate-step supervision.

## Circuit & Communication Complexity

- **The Illusion of State in State-Space Models** — William Merrill, Jackson Petty, Ashish Sabharwal (2024, ICML 2024). [paper](https://arxiv.org/abs/2404.08819). _Why it matters:_ Shows that linear and Mamba-style state-space models, despite being marketed as recurrent, still live in TC0 — they cannot track state-dependent problems (e.g. S5 word problem) any better than transformers can.
- **On Limitations of the Transformer Architecture** — Binghui Peng, Srini Narayanan, Christos Papadimitriou (2024). [paper](https://arxiv.org/abs/2402.08164). _Why it matters:_ Uses communication-complexity arguments to show that bounded-depth, polynomial-width transformers cannot solve function composition or iterated reasoning at input length n unless they violate widely-believed complexity assumptions.
- **Transformers, parallel computation, and logarithmic depth** — Clayton Sanford, Daniel Hsu, Matus Telgarsky (2024). [paper](https://arxiv.org/abs/2402.09268). _Why it matters:_ Identifies a hierarchy of multi-hop tasks ('k-hop induction') where O(log n)-depth attention is necessary and sufficient, separating shallow transformers from MLPs and recurrent baselines by parallel-computation depth.
- **The Parallelism Tradeoff: Limitations of Log-Precision Transformers** — William Merrill, Ashish Sabharwal (2023, TACL 2023). [paper](https://arxiv.org/abs/2207.00729). _Why it matters:_ Proves that any log-precision transformer can be simulated by uniform constant-depth threshold circuits (TC0), so a single forward pass cannot decide problems believed to lie outside TC0 (e.g. matrix permanent, S5 word problem).
- **Representational Strengths and Limitations of Transformers** — Clayton Sanford, Daniel Hsu, Matus Telgarsky (2023, NeurIPS 2023). [paper](https://arxiv.org/abs/2306.02896). _Why it matters:_ Gives matching upper and lower bounds for transformer width/depth on three-way matching and triple-detection tasks, separating attention from MLPs and unidirectional RNNs via communication-complexity arguments.

## Logical Characterizations

- **Logical Languages Accepted by Transformer Encoders with Hard Attention** — Pablo Barceló et al. (2024, ICLR 2024). [paper](https://arxiv.org/abs/2310.03817). _Why it matters:_ Shows that unique-hard-attention encoders accept exactly the first-order definable languages with unary numerical predicates (a strict subset of AC0), and that average-hard-attention encoders climb to TC0 but no higher.
- **Masked Hard-Attention Transformers Recognize Exactly the Star-Free Languages** — Andy Yang, David Chiang, Dana Angluin (2024, NeurIPS 2024). [paper](https://arxiv.org/abs/2310.13897). _Why it matters:_ Proves an exact characterization: causal hard-attention transformers without position embeddings recognize precisely the star-free regular languages, equivalent to LTL or FO[<].
- **A Logic for Expressing Log-Precision Transformers** — William Merrill, Ashish Sabharwal (2023, NeurIPS 2023). [paper](https://arxiv.org/abs/2210.02671). _Why it matters:_ Embeds log-precision transformers in first-order logic with majority quantifiers (FOM), giving the first logical upper-bound characterization of a realistic transformer variant.
- **Overcoming a Theoretical Limitation of Self-Attention** — David Chiang, Peter Cholak (2022, ACL 2022). [paper](https://arxiv.org/abs/2202.12172). _Why it matters:_ Shows that augmenting attention with layer normalization in a particular way lets transformers recognize Parity and Dyck-1 — i.e. the Hahn 2020 obstruction is tied to the specific attention variant studied, not to attention per se.

## Learnability & Sample Complexity

- **Transformers learn to implement preconditioned gradient descent for in-context learning** — Kwangjun Ahn et al. (2023, NeurIPS 2023). [paper](https://arxiv.org/abs/2306.00297). _Why it matters:_ Shows that the loss landscape of trained linear-attention layers admits a stationary point implementing preconditioned gradient descent — sharper than 'plain GD' and matching empirical performance.
- **What learning algorithm is in-context learning? Investigations with linear models** — Ekin Akyürek et al. (2023, ICLR 2023). [paper](https://arxiv.org/abs/2211.15661). _Why it matters:_ Demonstrates that transformers trained on linear-regression ICL tasks implement gradient-descent and ridge-regression-like estimators internally, with explicit weight constructions reproducing the empirical behavior.
- **A Theory of Emergent In-Context Learning as Implicit Structure Induction** — Michael Hahn, Navin Goyal (2023). [paper](https://arxiv.org/abs/2303.07971). _Why it matters:_ Derives ICL as a consequence of compositional structure in pretraining data, predicting concrete scaling laws for the emergence threshold as a function of data compositionality.
- **Transformers learn in-context by gradient descent** — Johannes von Oswald et al. (2023, ICML 2023). [paper](https://arxiv.org/abs/2212.07677). _Why it matters:_ Constructs single-layer linear-attention transformers that exactly implement one step of gradient descent on a least-squares objective, and shows trained models converge to this construction.
- **Pretraining task diversity and the emergence of non-Bayesian in-context learning for regression** — Allan Raventós et al. (2023, NeurIPS 2023). [paper](https://arxiv.org/abs/2306.15063). _Why it matters:_ Identifies a sharp pretraining-task-diversity threshold beyond which transformers switch from in-distribution Bayesian ICL to ridge-regression-like behavior generalizing to unseen tasks.
- **Trained Transformers Learn Linear Models In-Context** — Ruiqi Zhang, Spencer Frei, Peter L. Bartlett (2023). [paper](https://arxiv.org/abs/2306.09927). _Why it matters:_ Proves that a single linear-attention layer trained on linear-regression ICL data converges to a one-step gradient-descent predictor, with explicit non-asymptotic optimization rates.
- **Inductive Biases and Variable Creation in Self-Attention Mechanisms** — Benjamin L. Edelman et al. (2022, ICML 2022). [paper](https://arxiv.org/abs/2110.10090). _Why it matters:_ Proves sample-complexity bounds for self-attention learning sparse Boolean functions, showing the head structure provides an inductive bias that is exponentially more sample-efficient than fully-connected networks on this class.
- **What Can Transformers Learn In-Context? A Case Study of Simple Function Classes** — Shivam Garg et al. (2022, NeurIPS 2022). [paper](https://arxiv.org/abs/2208.01066). _Why it matters:_ Shows empirically and analytically that transformers trained on synthetic regression data implement, at inference, a near-optimal learner for the underlying function class — the foundational ICL-as-meta-learning result.
- **An Explanation of In-context Learning as Implicit Bayesian Inference** — Sang Michael Xie et al. (2022, ICLR 2022). [paper](https://arxiv.org/abs/2111.02080). _Why it matters:_ Models pretraining as a mixture-of-HMMs prior and shows in-context learning emerges as posterior inference over latent task variables, predicting the empirical scaling of demo-count benefits.

## Knowledge Editing & Impossibility Results

- **Evaluating the Ripple Effects of Knowledge Editing in Language Models** — Roi Cohen et al. (2024, TACL 2024). [paper](https://arxiv.org/abs/2307.12976). _Why it matters:_ Defines logical ripple-effect tests (composition, two-hop, subject aliasing) for edited models and shows existing methods fail them, formalizing why naive locate-and-edit underspecifies knowledge editing.
- **Does Localization Inform Editing? Surprising Differences in Causality-Based Localization vs. Knowledge Editing in Language Models** — Peter Hase et al. (2023, NeurIPS 2023). [paper](https://arxiv.org/abs/2301.04213). _Why it matters:_ Shows that edit success is largely independent of the causal-trace 'hot' layer — a dissociation between localization signal and edit efficacy that complicates ROME's mechanistic interpretation.
- **Mass-Editing Memory in a Transformer** — Kevin Meng et al. (2023, ICLR 2023). [paper](https://arxiv.org/abs/2210.07229) · [project](https://memit.baulab.info). _Why it matters:_ Extends ROME to thousands of simultaneous edits by solving a per-layer normal-equation update, giving the canonical 'edit-scale' baseline that later impossibility-style results push against.
- **Locating and Editing Factual Associations in GPT** — Kevin Meng et al. (2022, NeurIPS 2022). [paper](https://arxiv.org/abs/2202.05262) · [project](https://rome.baulab.info). _Why it matters:_ Introduces causal tracing to localize factual recall to mid-layer MLPs and edits a single weight matrix (rank-one ROME update) to rewrite a fact — the load-bearing empirical claim that subsequent theoretical work tests.

## Parallel / Architectural Complexity & Scaling

- **Why are Sensitive Functions Hard for Transformers?** — Michael Hahn, Mark Rofin (2024, ACL 2024). [paper](https://arxiv.org/abs/2402.09963). _Why it matters:_ Proves a loss-landscape bias: transformer parameters minimizing training loss tend to compute functions of low average sensitivity, explaining why parity-like high-sensitivity targets fail to be learned even when expressible.
- **What Algorithms can Transformers Learn? A Study in Length Generalization** — Hattie Zhou et al. (2024, ICLR 2024). [paper](https://arxiv.org/abs/2310.16028). _Why it matters:_ Proposes the RASP-Generalization Conjecture: transformers length-generalize on a task iff the task admits a short, simple RASP-L program, and empirically supports the prediction across arithmetic and reasoning tasks.
- **Transformers Learn Shortcuts to Automata** — Bingbin Liu et al. (2023, ICLR 2023). [paper](https://arxiv.org/abs/2210.10749). _Why it matters:_ Shows that O(log T)-depth transformers can solve T-step automaton-simulation tasks via algebraic shortcuts (semigroup composition), but those shortcuts brittle-fail out of distribution — quantifying the length-generalization gap.

## Surveys, Lecture Notes & Talks

- **What Formal Languages Can Transformers Express? A Survey** — Lena Strobl et al. (2024, TACL 12:543-561, 2024). [paper](https://arxiv.org/abs/2311.00208). _Why it matters:_ The reference survey on transformer expressivity: organizes upper- and lower-bound results in terms of attention variant (hard / soft / saturated), precision regime, and logical / circuit characterizations.

## Reading paths

Curated ordered sequences for getting into a sub-area. See [`docs/reading-paths.md`](docs/reading-paths.md) for the full set.

- **Start here for CoT theory** → Merrill & Sabharwal (2024, CoT) → Feng et al. (2023, CoT mystery) → Li et al. (2024, serial problems).
- **Start here for expressivity** → Strobl et al. (2024, survey) → Hahn (2020, limitations) → Merrill, Sabharwal, Smith (2022, saturated → TC0) → Merrill & Sabharwal (2023, log-precision → TC0).
- **Start here for learnability of in-context learning** → Xie et al. (2022, implicit Bayes) → Garg et al. (2022, simple function classes) → von Oswald et al. (2023, GD).

## Recent additions

- 2026-05-14 — [On the Computational Power of Transformers and its Implications in Sequence Modeling](https://arxiv.org/abs/2006.09286)
- 2026-05-14 — [On the Ability and Limitations of Transformers to Recognize Formal Languages](https://arxiv.org/abs/2009.11264)
- 2026-05-14 — [Tighter Bounds on the Expressivity of Transformer Encoders](https://arxiv.org/abs/2301.10743)
- 2026-05-14 — [Theoretical Limitations of Self-Attention in Neural Sequence Models](https://arxiv.org/abs/1906.06755)
- 2026-05-14 — [Saturated Transformers are Constant-Depth Threshold Circuits](https://arxiv.org/abs/2106.16213)
- 2026-05-14 — [On the Turing Completeness of Modern Neural Network Architectures](https://arxiv.org/abs/1901.03429)
- 2026-05-14 — [Attention is Turing-Complete](https://jmlr.org/papers/v22/20-302.html)
- 2026-05-14 — [Self-Attention Networks Can Process Bounded Hierarchical Languages](https://arxiv.org/abs/2105.11115)
- 2026-05-14 — [Are Transformers universal approximators of sequence-to-sequence functions?](https://arxiv.org/abs/1912.10077)
- 2026-05-14 — [Towards Revealing the Mystery behind Chain of Thought: A Theoretical Perspective](https://arxiv.org/abs/2305.15408)

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

## License

- List content (`README.md`, `entries/`, `docs/`, `PLANNING/`) — [CC0 1.0](LICENSE), public domain.
- Source code under `tools/` — [MIT](LICENSE-CODE).
