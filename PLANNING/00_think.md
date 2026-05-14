# PHASE 0 — THINK

## 1. Landscape Scan

A web survey of existing "awesome LLM reasoning" repositories was conducted to confirm the theoretical-foundations niche is unoccupied.

| Repository | Scope | What it omits |
|---|---|---|
| `atfortes/Awesome-LLM-Reasoning` | Methods-focused: CoT prompting → o1 → DeepSeek-R1. Practical techniques to "unlock" reasoning. | No expressivity theorems, no circuit complexity, no logical characterizations, no learnability bounds. |
| `luban-agi/Awesome-LLM-reasoning` | A broad paper list of LLM reasoning papers (largely empirical). | Same omissions: theory is incidental, not central. |
| `Junting-Lu/Awesome-LLM-Reasoning-Techniques` | Techniques, CoT variants, o1 follow-ups. | No theory spine. |
| `samkhur006/awesome-llm-planning-reasoning` | Planning + reasoning, benchmarks, limitations (empirical). | No formal expressivity/complexity results. |
| `srush/awesome-o1` (Sasha Rush) | An o1-centric bibliography with light theory; well-curated but framed around o1. | Doesn't aspire to be the theory map. The theory-adjacent papers it includes are a subset of what we cover. |
| `reasoning-survey/Awesome-Reasoning-Foundation-Models` | Catalogue of foundation models for reasoning across modalities. | Not theoretical — about models, not their formal properties. |
| `LightChen233/Awesome-Long-Chain-of-Thought-Reasoning` | Long-CoT survey companion. | Empirical scaling, not the formal theory of CoT. |
| `hemingkx/Awesome-Efficient-Reasoning`, `fscdc/Awesome-Efficient-Reasoning-Models`, `Eclipsess/Awesome-Efficient-Reasoning-LLMs` | Efficient reasoning surveys. | Engineering/efficiency, not foundational theory. |
| `Hannibal046/Awesome-LLM` | Catch-all LLM list with a CoT subsection. | Too broad to qualify as a theory list. |

**Adjacent but tangential:** `JShollaj/awesome-llm-interpretability` (mechanistic interpretability — a sibling, but distinct from formal expressivity/learnability theory). The NeurIPS 2025 workshop "What Can('t) Transformers Do?" (`transformerstheory.github.io`) confirms the field's coherence as a research community without a corresponding curated map.

**Conclusion:** No existing list maps the *theoretical foundations* of LLM reasoning — expressivity bounds, CoT theory, circuit/communication complexity, logical characterizations (FOC[Attn], FO+MOD, etc.), learnability of in-context tasks, knowledge-editing impossibility results, parallel-attention complexity. This list is genuinely first-mover in its niche. The differentiation is sharp enough to be defensible (anyone trying to displace us must rebuild verified provenance for the same 200 papers).

## 2. Taxonomy (the spine of the list)

Top-level categories (8), each with intended sub-themes:

1. **Expressivity & Representational Limits** — what classes of functions / formal languages transformers (with various precision, attention types, depths) can compute. *Sub-themes:* universal approximation, formal-language recognition (regular, DCFL, etc.), saturation, hard vs. soft attention.
2. **Chain-of-Thought: Theory & Error Bounds** — formal results on what CoT buys (or doesn't), error propagation in multi-step reasoning, latent vs. discrete CoT, continuous CoT, length-generalization theory.
3. **Circuit & Communication Complexity** — placing transformers in TC0, AC0, TC^k; communication-complexity lower bounds; parallelism tradeoffs.
4. **Logical Characterizations** — exact-equivalence results between transformer variants and logical formalisms (FOC[Attn], FOM[+], counting logics).
5. **Learnability & Sample Complexity** — in-context learning theory; minimax rates; statistical learning of attention; learnability of function classes via Transformers; pretraining-data theoretical results.
6. **Knowledge Editing & Impossibility Results** — formal limits on locating, editing, unlearning; ROME and successors as objects of theoretical study; impossibility theorems.
7. **Parallel / Architectural Complexity & Scaling** — depth vs. width vs. context-length tradeoffs; log-depth simulation results; state-space-model vs. attention separations.
8. **Surveys, Lecture Notes & Talks** — high-quality entry points (Strobl et al. survey on transformer expressivity; Merrill lectures; Schwartz-lab notes).

Refinements to consider: a separate "Synthetic-Data Learnability" sub-category may be promoted once seed coverage warrants it (currently folded into §5).

## 3. Seed Bibliography (40–60 confident candidates)

Status legend: `verified` = web-confirmed at THINK stage; `needs-check` = high-confidence but to be verified before entering the published list in Phase 2.

> Verification target: every published entry must be `verified` (arXiv abstract page resolved AND title/authors/year cross-checked). The two below already verified during this phase:

### §1 Expressivity & Representational Limits
- `needs-check` Yun, Bhojanapalli, Rawat, Reddi, Kumar (2020). *Are Transformers Universal Approximators of Sequence-to-Sequence Functions?* ICLR.
- `needs-check` Hahn (2020). *Theoretical Limitations of Self-Attention in Neural Sequence Models.* TACL.
- `needs-check` Bhattamishra, Ahuja, Goyal (2020). *On the Ability and Limitations of Transformers to Recognize Formal Languages.* EMNLP.
- `needs-check` Bhattamishra, Patel, Goyal (2020). *On the Computational Power of Transformers and its Implications in Sequence Modeling.* CoNLL.
- `needs-check` Yao, Peng, Papadimitriou, Narasimhan (2021). *Self-Attention Networks Can Process Bounded Hierarchical Languages.* ACL.
- `needs-check` Merrill, Sabharwal, Smith (2022). *Saturated Transformers are Constant-Depth Threshold Circuits.* TACL.
- `needs-check` Pérez, Barceló, Marinkovic (2021). *Attention is Turing-Complete.* JMLR.
- `needs-check` Pérez, Marinkovic, Barceló (2019). *On the Turing Completeness of Modern Neural Network Architectures.* ICLR.
- `needs-check` Chiang, Cholak, Pillay (2023). *Tighter Bounds on the Expressivity of Transformer Encoders.* ICML.
- `needs-check` Strobl, Merrill, Weiss, Chiang, Angluin (2024). *Transformers as Recognizers of Formal Languages: A Survey on Expressivity.* TACL. *(also belongs to §8.)*

### §2 Chain-of-Thought: Theory & Error Bounds
- `verified` Merrill & Sabharwal (2024). *The Expressive Power of Transformers with Chain of Thought.* ICLR. [arXiv:2310.07923]
- `needs-check` Feng, Zhang, Yan, Liu, Du, Wang, Wang, He (2023). *Towards Revealing the Mystery behind Chain of Thought: A Theoretical Perspective.* NeurIPS.
- `needs-check` Li, Liu, Hartford, Welleck, Zhang, Du (2024). *Chain of Thought Empowers Transformers to Solve Inherently Serial Problems.* ICLR.
- `needs-check` Prystawski, Li, Goodman (2023). *Why think step by step? Reasoning emerges from the locality of experience.* NeurIPS.
- `needs-check` Wies, Levine, Shashua (2023). *Sub-Task Decomposition Enables Learning in Sequence to Sequence Tasks.* ICLR.
- `needs-check` Malach (2023). *Auto-Regressive Next-Token Predictors are Universal Learners.*
- `needs-check` Hahn & Goyal (2023). *A Theory of Emergent In-Context Learning as Implicit Structure Induction.*

### §3 Circuit & Communication Complexity
- `verified` Merrill & Sabharwal (2023). *The Parallelism Tradeoff: Limitations of Log-Precision Transformers.* TACL. [arXiv:2207.00729]
- `needs-check` Sanford, Hsu, Telgarsky (2024). *Transformers, parallel computation, and logarithmic depth.* ICML.
- `needs-check` Sanford, Hsu, Telgarsky (2023). *Representational Strengths and Limitations of Transformers.* NeurIPS.
- `needs-check` Peng, Narayanan, Papadimitriou (2024). *On Limitations of the Transformer Architecture.* COLM.
- `needs-check` Merrill, Petty, Sabharwal (2024). *The Illusion of State in State-Space Models.* ICML.

### §4 Logical Characterizations
- `needs-check` Merrill & Sabharwal (2023). *A Logic for Expressing Log-Precision Transformers.* NeurIPS.
- `needs-check` Barceló, Kozachinskiy, Lin, Podolskii (2024). *Logical Languages Accepted by Transformer Encoders with Hard Attention.* ICLR.
- `needs-check` Chiang & Cholak (2022). *Overcoming a Theoretical Limitation of Self-Attention.* ACL.
- `needs-check` Angluin, Chiang, Yang (2023). *Masked Hard-Attention Transformers Recognize Exactly the Star-Free Languages.*

### §5 Learnability & Sample Complexity
- `needs-check` Garg, Tsipras, Liang, Valiant (2022). *What Can Transformers Learn In-Context? A Case Study of Simple Function Classes.* NeurIPS.
- `needs-check` Akyürek, Schuurmans, Andreas, Ma, Zhou (2023). *What learning algorithm is in-context learning? Investigations with linear models.* ICLR.
- `needs-check` von Oswald, Niklasson, Randazzo, Sacramento, Mordvintsev, Zhmoginov, Vladymyrov (2023). *Transformers Learn In-Context by Gradient Descent.* ICML.
- `needs-check` Xie, Raghunathan, Liang, Ma (2022). *An Explanation of In-Context Learning as Implicit Bayesian Inference.* ICLR.
- `needs-check` Raventós, Paul, Chen, Ganguli (2023). *Pretraining task diversity and the emergence of non-Bayesian in-context learning for regression.* NeurIPS.
- `needs-check` Edelman, Goel, Kakade, Zhang (2022). *Inductive Biases and Variable Creation in Self-Attention Mechanisms.* ICML.
- `needs-check` Zhang, Frei, Bartlett (2024). *Trained Transformers Learn Linear Models In-Context.* JMLR.
- `needs-check` Ahn, Cheng, Daneshmand, Sra (2023). *Transformers Learn to Implement Preconditioned Gradient Descent for In-Context Learning.* NeurIPS.
- `needs-check` Ahn, Cheng, Song, Yun, Krishnamurthy, Sra (2024). *Linear Attention is (Maybe) All You Need (to Understand Transformer Optimization).* ICLR.

### §6 Knowledge Editing & Impossibility
- `needs-check` Meng, Bau, Andonian, Belinkov (2022). *Locating and Editing Factual Associations in GPT.* NeurIPS. *(ROME)*
- `needs-check` Meng, Sharma, Andonian, Belinkov, Bau (2023). *Mass-Editing Memory in a Transformer.* ICLR. *(MEMIT)*
- `needs-check` Hase, Bansal, Kim, Ghandeharioun (2023). *Does Localization Inform Editing? Surprising Differences in Causality-Based Localization vs. Knowledge Editing in Language Models.* NeurIPS.
- `needs-check` Cohen, Biran, Yoran, Globerson, Geva (2024). *Evaluating the Ripple Effects of Knowledge Editing in Language Models.* TACL.
- `needs-check` Bills, Cammarata, Mossing, Tillman, Gao, Goh, Sutskever, Leike, Wu, Saunders (2023). *Language models can explain neurons in language models.* OpenAI tech report.

### §7 Parallel / Architectural Complexity & Scaling
- `needs-check` Hahn & Rofin (2024). *Why are sensitive functions hard for transformers?* ACL.
- `needs-check` Liu, Ash, Goel, Krishnamurthy, Zhang (2023). *Transformers Learn Shortcuts to Automata.* ICLR.
- `needs-check` Zhou, Bradley, Littwin, Razin, Saremi, Susskind, Bengio, Nakkiran (2024). *What Algorithms can Transformers Learn? A Study in Length Generalization.* ICLR.
- `needs-check` Yang, Wang, Chen, Smola, Hou, Soltanolkotabi (2024). *Sharp Analysis for KV Cache Compression.* (provisional — may drop if too applied)

### §8 Surveys, Lecture Notes & Talks
- `needs-check` Strobl, Merrill, Weiss, Chiang, Angluin (2024). *Transformers as Recognizers of Formal Languages.* TACL. *(also §1)*
- `needs-check` Merrill (2023). *Formal Languages and the NLP Black Box.* Lecture notes / blog series.
- `needs-check` Sasha Rush — *Lectures on Transformers and o1* (talk + GitHub).
- `needs-check` What Can('t) Transformers Do? NeurIPS 2025 workshop (`transformerstheory.github.io`).

**Seed total: ~46 candidates.** All but 2 are `needs-check` and will be web-verified before entering the published list. Anything that fails verification is dropped.

## 4. Verification Plan

Per-entry gate (must all pass to enter the list):

1. **Existence.** arXiv abstract page resolves with HTTP 200 OR Semantic Scholar / DBLP entry resolves.
2. **Title.** Exact title from the arXiv abstract page or venue PDF — no paraphrasing.
3. **Authors.** Full author list from the arXiv abstract page (not from memory).
4. **Year.** First-submission year on arXiv OR official venue year — whichever is reported, must match what the entry claims.
5. **Venue.** If a venue is claimed (e.g. "ICLR 2024"), confirm via the arXiv comment field, the proceedings page, or OpenReview.
6. **Code/project link** (if claimed) — `linkcheck.py` must HEAD it green.

Allowed primary sources, in order of preference: arXiv abstract page → OpenReview → ACL Anthology → official proceedings → Semantic Scholar → DBLP. Authors' personal pages are acceptable secondary evidence.

Verification outcomes for each entry are logged in `PLANNING/02_verification_log.md` with: status (`PASS` / `DROP`), the URL inspected, the date checked, and one-line evidence. An entry without a `PASS` row is not allowed in `entries/` (enforced by `validate_entries.py`).

## 5. Risk Log

| Risk | Severity | Mitigation |
|---|---|---|
| **Wrong citation under real academic identity.** A single hallucinated author / wrong year is a public-facing reputational injury. | High | Mandatory per-entry verification log; CI lint that rejects any entry missing a verification row; bias toward DROP when in doubt. |
| **Slow-spike phenomenon.** Pure lists tend to compound slowly on GitHub stars vs. tools/working code. | Medium | Launch alongside a companion repo (e.g. a working reproduction of a CoT theory result) so the social-media wave catches both. Documented in `docs/LAUNCH.md`. |
| **Overlap perception.** Readers may confuse with `atfortes/Awesome-LLM-Reasoning`. | Medium | Strong, repeated scope statement ("theory, NOT methods"); generous "Related lists" linking competitors (good-faith linking is rewarded). |
| **Subfield-insider scrutiny.** Researchers in this exact niche (Merrill, Sanford, Chiang, Strobl, Hahn, …) WILL read it. Miscategorizations or weak annotations land badly. | High | Phase 6 hostile re-read pass as a subfield insider. Annotations stay terse and technically precise; categorizations cross-checked. |
| **Annotation tone.** "Why it matters" lines can drift promotional or wrong. | Medium | Style rule: one sentence, names the formal result (e.g. "Places log-precision transformers in TC0"); no superlatives. |
| **Decay.** Theory papers get revised; venues change between preprint and acceptance. | Low | Weekly CI link-check; quarterly "stale entry" sweep tracked in CONTRIBUTING.md. |
| **Scope drift via PRs.** Contributors may push applied/empirical CoT papers. | Medium | PR template requires verification link + matches a defined category; CONTRIBUTING.md gives a clear OUT-of-scope list. |

## 6. Open Questions

(Per the operating contract, the user has asked me to work without stopping for clarifying questions. These are noted for the record; I will resolve each with the reasonable default in parentheses, and the user can redirect.)

- **Q1 — Curator handle?** README assumes `bettyguo` GitHub handle and Betty Guo (Dongxin Guo). *(Default: use as given in the master prompt. If the GitHub username turns out to be different, README references are search-and-replace-clean.)*
- **Q2 — Companion repo for launch.** The master prompt mentions launching alongside a companion working repo to escape the slow-spike. *(Default: I write the recommendation into `docs/LAUNCH.md` but do not build the companion repo in this session — that's a separate piece of work.)*
- **Q3 — Markdown vs. structured source.** The design phase chooses between hand-written README or generated-from-YAML. *(Default: generate from per-entry YAML in `entries/` — gives `linkcheck.py` clean data and avoids drift between source and README. This is the recommendation in Phase 1.)*
- **Q4 — Star-history embed.** README spec says embed star-history badge. *(Default: include but commented out until the repo is public, since the badge will 404 until then.)*
- **Q5 — License.** Master prompt says "CC0 / MIT for any code". *(Default: dual-license — `LICENSE` = CC0 for list content; `LICENSE-CODE` = MIT for `tools/`.)*
- **Q6 — How aggressive on launch-size?** Master prompt asks 150–250 entries but warns quality > quantity. *(Default: aim for ~150 highly-verified entries at launch, with a clean "wanted" issue list signaling expansion paths. Better to ship 150 perfect than 250 shaky.)*

---

**CHECKPOINT 0 — DONE.** Proceeding to Phase 1.
