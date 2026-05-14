# Reading paths

Curated ordered sequences for getting into a sub-area of the list. Each path is dependency-ordered: read top-down. Annotations are intentionally brief — the entry's own annotation in [`../README.md`](../README.md) is the source of truth for what the paper proves.

## 1. The expressivity ceiling (where do transformers sit in the complexity zoo?)

The single most important fact about transformers as computational devices is that, without chain-of-thought, a single forward pass lives in a small complexity class.

1. **Strobl, Merrill, Weiss, Chiang, Angluin (2024) — *What Formal Languages Can Transformers Express? A Survey*.** Start here. Tabulates the upper and lower bounds you are about to read in detail.
2. **Hahn (2020) — *Theoretical Limitations of Self-Attention in Neural Sequence Models*.** The first formal-language lower bound: hard-attention transformers cannot recognize Parity or Dyck-2.
3. **Merrill, Sabharwal, Smith (2022) — *Saturated Transformers are Constant-Depth Threshold Circuits*.** Places saturated attention in TC0.
4. **Merrill & Sabharwal (2023) — *The Parallelism Tradeoff: Limitations of Log-Precision Transformers*.** Extends the TC0 result to the realistic log-precision regime.
5. **Merrill & Sabharwal (2023) — *A Logic for Expressing Log-Precision Transformers*.** Gives a logical (FOM) characterization to match the circuit-class one.
6. **Yang, Chiang, Angluin (2024) — *Masked Hard-Attention Transformers Recognize Exactly the Star-Free Languages*.** A tight exact characterization for a clean variant.

You now own the architecture's representational ceiling.

## 2. Chain of thought theory (does intermediate generation actually buy you compute?)

Once you've read path 1, the CoT story makes much more sense: CoT is the lever that lifts transformers out of TC0.

1. **Merrill & Sabharwal (2024) — *The Expressive Power of Transformers with Chain of Thought*.** The headline result. Log-many steps → TC0; linear → P; polynomial → EXPTIME.
2. **Feng et al. (2023) — *Towards Revealing the Mystery behind Chain of Thought*.** Constructive separation: arithmetic and dynamic programming reachable with CoT, unreachable without.
3. **Li, Liu, Zhou, Ma (2024) — *Chain of Thought Empowers Transformers to Solve Inherently Serial Problems*.** Matches the upper-bound side: T(n) CoT steps simulate T(n)-step circuits.
4. **Prystawski, Li, Goodman (2023) — *Why think step by step?*** A data-distribution-level story for why CoT helps when training is locally consistent.
5. **Malach (2023) — *Auto-Regressive Next-Token Predictors are Universal Learners*.** Universality of next-token-prediction-with-CoT, packaged as a learnability statement.
6. **Pfau, Merrill, Bowman (2024) — *Let's Think Dot by Dot*.** Empirically separates the compute-extension role of CoT from its interpretability role.

## 3. Learnability of in-context learning (when does ICL emerge, and what does it implement?)

ICL is the most-studied transformer-emergent capability with theoretical traction.

1. **Xie, Raghunathan, Liang, Ma (2022) — *An Explanation of In-context Learning as Implicit Bayesian Inference*.** The HMM-prior story; the prediction that motivates everything below.
2. **Garg, Tsipras, Liang, Valiant (2022) — *What Can Transformers Learn In-Context?*.** Synthetic-function-class study; the empirical anchor.
3. **von Oswald et al. (2023) — *Transformers learn in-context by gradient descent*.** Constructive: linear-attention transformers can implement one step of GD; trained models converge there.
4. **Akyürek et al. (2023) — *What learning algorithm is in-context learning?*.** Independent confirmation across linear-regression tasks with explicit weight constructions.
5. **Mahankali, Hashimoto, Ma (2024) — *One Step of Gradient Descent is Provably Optimal*.** The optimality counterpart to (3).
6. **Bai et al. (2023) — *Transformers as Statisticians*.** Generalizes from GD to a broader "algorithm-selection" view of ICL.
7. **Raventós et al. (2023) — *Pretraining task diversity and the emergence of non-Bayesian ICL*.** Sharp threshold result: when does ICL switch from in-distribution-Bayes to ridge-regression-like behavior?
8. **Olsson et al. (2022) — *In-context Learning and Induction Heads*.** Mechanistic counterpart: the circuit responsible and the loss-bump signature of its formation.

## 4. Knowledge editing (where is a fact stored, and can we surgically rewrite it?)

The most concrete intersection of mechanistic interpretability and formal-foundations work.

1. **Geva et al. (2021) — *Transformer Feed-Forward Layers Are Key-Value Memories*.** Locates *what* the MLP layers represent.
2. **Meng et al. (2022) — *Locating and Editing Factual Associations in GPT* (ROME).** Causal tracing + rank-one editing.
3. **Meng et al. (2023) — *Mass-Editing Memory in a Transformer* (MEMIT).** Scales ROME to thousands of edits.
4. **Mitchell et al. (2022) — *Fast Model Editing at Scale* (MEND).** The hypernetwork-edit baseline against which ROME competes.
5. **Hase et al. (2023) — *Does Localization Inform Editing?*.** Surprising negative result: causal-trace signal is largely decoupled from edit efficacy.
6. **Cohen et al. (2024) — *Evaluating the Ripple Effects of Knowledge Editing*.** Formalizes why naive locate-and-edit underspecifies knowledge editing.
7. **Allen-Zhu & Li (2023) — *Physics of Language Models: Part 3.1 / 3.2*.** Controlled-data experiments separating storage from manipulation; clarifies what each editing method actually rewrites.

## 5. Length generalization and architectural limits (why don't transformers extrapolate?)

1. **Anil et al. (2022) — *Exploring Length Generalization in Large Language Models*.** Establishes the empirical baseline: naive length extrapolation fails at every scale.
2. **Press, Smith, Lewis (2022) — *Train Short, Test Long* (ALiBi).** The first positional-encoding intervention to substantially help.
3. **Liu et al. (2023) — *Transformers Learn Shortcuts to Automata*.** Why O(log T) depth often suffices in-distribution but breaks out of distribution.
4. **Zhou et al. (2024) — *What Algorithms can Transformers Learn? A Study in Length Generalization*.** The RASP-L generalization conjecture.
5. **Kazemnejad et al. (2023) — *The Impact of Positional Encoding on Length Generalization*.** Systematic ablation — NoPE often wins.
6. **Hahn & Rofin (2024) — *Why are Sensitive Functions Hard for Transformers?*.** A loss-landscape bias explanation for why parity-like targets fail to learn.

## 6. Logical characterizations (transformers ↔ logic — an exact translation)

For readers comfortable with descriptive complexity.

1. **Chiang & Cholak (2022) — *Overcoming a Theoretical Limitation of Self-Attention*.** Shows the Hahn obstruction is variant-specific.
2. **Chiang, Cholak, Pillay (2023) — *Tighter Bounds on the Expressivity of Transformer Encoders*.** Finite-precision encoders embed in FOC[+;MOD].
3. **Merrill & Sabharwal (2023) — *A Logic for Expressing Log-Precision Transformers*.** Log-precision transformers embed in FOM.
4. **Barceló et al. (2024) — *Logical Languages Accepted by Transformer Encoders with Hard Attention*.** Tight matches between UHAT/AHAT and FOL fragments / TC0.
5. **Yang, Chiang, Angluin (2024) — *Masked Hard-Attention Transformers Recognize Exactly the Star-Free Languages*.** The tightest exact characterization in the line.
6. **Yang & Chiang (2024) — *Counting Like Transformers*.** A counting-logic compiler that turns logical specs into concrete softmax-transformer weights.

---

Suggestions for additional paths are welcome — open an issue with the `wanted` label.
