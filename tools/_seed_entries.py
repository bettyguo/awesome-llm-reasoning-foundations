#!/usr/bin/env python3
"""One-time seed-entry generator.

Writes a curated set of verified entries to entries/<cat>/<slug>.yaml.
Each record is a tuple: (slug, category_dir, payload_dict).

Run from repo root:

    python tools/_seed_entries.py

This script is kept in tools/ for reproducibility but is not part of the
runtime tooling (linkcheck / validate / build_readme). It is safe to delete
after the seed pass — entries/ is the source of truth from then on.
"""
from __future__ import annotations

import pathlib
import sys

try:
    import yaml
except ImportError:
    print("ERROR: install PyYAML first.", file=sys.stderr)
    sys.exit(2)

REPO_ROOT = pathlib.Path(__file__).resolve().parent.parent
ENTRIES = REPO_ROOT / "entries"
ADDED = "2026-05-14"


def E(slug, cat_dir, category, title, authors, year, venue, paper_url, annotation, **extra):
    return (slug, cat_dir, {
        "title": title,
        "authors": authors,
        "year": year,
        "venue": venue,
        "category": category,
        "links": {
            "paper": paper_url,
            **{k: v for k, v in extra.get("links", {}).items()},
        },
        "annotation": annotation,
        "tags": extra.get("tags"),
        "added": ADDED,
    })


SEED = [

    # ====== §1 EXPRESSIVITY ======
    E("yun-2020-universal-approx", "01-expressivity", "expressivity",
      "Are Transformers universal approximators of sequence-to-sequence functions?",
      ["Chulhee Yun", "Srinadh Bhojanapalli", "Ankit Singh Rawat", "Sashank J. Reddi", "Sanjiv Kumar"],
      2020, "ICLR 2020",
      "https://arxiv.org/abs/1912.10077",
      "Proves that transformers with fixed width can universally approximate continuous permutation-equivariant sequence-to-sequence functions on compact domains, isolating positional encodings as the source of the non-equivariant extension.",
      tags=["universal-approximation", "expressivity"]),

    E("hahn-2020-self-attention-limits", "01-expressivity", "expressivity",
      "Theoretical Limitations of Self-Attention in Neural Sequence Models",
      ["Michael Hahn"],
      2020, "TACL 2020",
      "https://arxiv.org/abs/1906.06755",
      "Shows that hard-attention transformers cannot model Parity or Dyck-2, and that soft-attention transformers solve them only with attention entropy growing in input length — an early formal obstruction to in-distribution length generalization.",
      tags=["formal-languages", "hard-attention", "soft-attention"]),

    E("bhattamishra-2020-formal-languages", "01-expressivity", "expressivity",
      "On the Ability and Limitations of Transformers to Recognize Formal Languages",
      ["Satwik Bhattamishra", "Kabir Ahuja", "Navin Goyal"],
      2020, "EMNLP 2020",
      "https://arxiv.org/abs/2009.11264",
      "Empirically separates which counter, shuffle, and Dyck languages transformers can and cannot recognize, anchoring later theoretical work on transformer expressivity in concrete language-class boundaries.",
      tags=["formal-languages", "counter-languages"]),

    E("bhattamishra-2020-computational-power", "01-expressivity", "expressivity",
      "On the Computational Power of Transformers and its Implications in Sequence Modeling",
      ["Satwik Bhattamishra", "Arkil Patel", "Navin Goyal"],
      2020, "CoNLL 2020",
      "https://arxiv.org/abs/2006.09286",
      "Gives a Turing-completeness argument for transformer encoder-decoders under unbounded-precision assumptions and pinpoints residual connections and positional encodings as load-bearing for the construction.",
      tags=["turing-completeness"]),

    E("yao-2021-bounded-hierarchical", "01-expressivity", "expressivity",
      "Self-Attention Networks Can Process Bounded Hierarchical Languages",
      ["Shunyu Yao", "Binghui Peng", "Christos Papadimitriou", "Karthik Narasimhan"],
      2021, "ACL 2021",
      "https://arxiv.org/abs/2105.11115",
      "Constructs O(log n)-depth transformers recognizing Dyck-k with bounded nesting depth, showing self-attention's depth-vs-stack tradeoff for hierarchical languages.",
      tags=["formal-languages", "dyck"],
      links={"code": "https://github.com/princeton-nlp/dyck-transformer"}),

    E("merrill-2022-saturated-tc0", "01-expressivity", "expressivity",
      "Saturated Transformers are Constant-Depth Threshold Circuits",
      ["William Merrill", "Ashish Sabharwal", "Noah A. Smith"],
      2022, "TACL 2022",
      "https://arxiv.org/abs/2106.16213",
      "Shows that saturated-attention transformers (a hard-attention idealization with averaging over maxima) are simulable by uniform TC0 circuits, placing a hard upper bound on what such transformers can compute.",
      tags=["circuit-complexity", "TC0", "saturated-attention"]),

    E("perez-2019-turing-completeness", "01-expressivity", "expressivity",
      "On the Turing Completeness of Modern Neural Network Architectures",
      ["Jorge Pérez", "Javier Marinković", "Pablo Barceló"],
      2019, "ICLR 2019",
      "https://arxiv.org/abs/1901.03429",
      "Proves Turing-completeness for the Transformer and Neural GPU under unbounded precision and arbitrary input access, while flagging that the construction relies on conditions not satisfied by practical implementations.",
      tags=["turing-completeness"]),

    E("perez-2021-attention-turing", "01-expressivity", "expressivity",
      "Attention is Turing-Complete",
      ["Jorge Pérez", "Pablo Barceló", "Javier Marinkovic"],
      2021, "JMLR 22(75):1-35, 2021",
      "https://jmlr.org/papers/v22/20-302.html",
      "Refines the earlier ICLR 2019 result to show that a hard-attention Transformer alone — without residual or other architectural extras — already simulates any Turing machine under unbounded precision.",
      tags=["turing-completeness", "hard-attention"]),

    E("chiang-2023-tighter-bounds", "01-expressivity", "expressivity",
      "Tighter Bounds on the Expressivity of Transformer Encoders",
      ["David Chiang", "Peter Cholak", "Anand Pillay"],
      2023, "ICML 2023",
      "https://arxiv.org/abs/2301.10743",
      "Sharpens the upper-bound side of transformer expressivity by characterizing fixed-precision soft-attention encoders within a counting-extension of first-order logic — a precursor to the logical-characterization line.",
      tags=["first-order-logic", "counting", "fixed-precision"]),

    # ====== §2 CoT THEORY ======
    E("merrill-sabharwal-2024-cot", "02-cot-theory", "cot-theory",
      "The Expressive Power of Transformers with Chain of Thought",
      ["William Merrill", "Ashish Sabharwal"],
      2024, "ICLR 2024",
      "https://arxiv.org/abs/2310.07923",
      "Characterizes the expressive power of decoder-only transformers with intermediate CoT tokens as a function of generation length: log-many steps stay in TC0, linear-many reach P, polynomial-many reach EXPTIME.",
      tags=["chain-of-thought", "complexity-class"],
      links={"openreview": "https://openreview.net/forum?id=NjNGlPh8Wh"}),

    E("feng-2023-cot-mystery", "02-cot-theory", "cot-theory",
      "Towards Revealing the Mystery behind Chain of Thought: A Theoretical Perspective",
      ["Guhao Feng", "Bohang Zhang", "Yuntian Gu", "Haotian Ye", "Di He", "Liwei Wang"],
      2023, "NeurIPS 2023",
      "https://arxiv.org/abs/2305.15408",
      "Constructs a constant-size CoT transformer that solves arithmetic and dynamic-programming tasks unreachable by any fixed-depth no-CoT transformer, giving an unconditional separation between with-CoT and without-CoT expressivity.",
      tags=["chain-of-thought", "arithmetic", "dynamic-programming"]),

    E("li-2024-cot-serial", "02-cot-theory", "cot-theory",
      "Chain of Thought Empowers Transformers to Solve Inherently Serial Problems",
      ["Zhiyuan Li", "Hong Liu", "Denny Zhou", "Tengyu Ma"],
      2024, "ICLR 2024",
      "https://arxiv.org/abs/2402.12875",
      "Proves that with T(n) steps of CoT a constant-depth transformer simulates T(n)-step sequential computation, recovering serial-complexity classes that lie outside the parallel reach of a single forward pass.",
      tags=["chain-of-thought", "P-completeness", "sequential"]),

    E("prystawski-2023-step-by-step", "02-cot-theory", "cot-theory",
      "Why think step by step? Reasoning emerges from the locality of experience",
      ["Ben Prystawski", "Michael Y. Li", "Noah D. Goodman"],
      2023, None,
      "https://arxiv.org/abs/2304.03843",
      "Shows in a Bayesian-network model that CoT helps precisely when training-time evidence is locally connected but globally sparse — chained inference recovers conditional independencies that direct prediction cannot.",
      tags=["chain-of-thought", "bayesian-network", "locality"]),

    E("wies-2023-subtask-decomposition", "02-cot-theory", "cot-theory",
      "Sub-Task Decomposition Enables Learning in Sequence to Sequence Tasks",
      ["Noam Wies", "Yoav Levine", "Amnon Shashua"],
      2023, "ICLR 2023",
      "https://arxiv.org/abs/2204.02892",
      "Proves a learnability separation: composite sequence-to-sequence tasks that are hard to learn end-to-end become PAC-learnable once decomposed into sub-tasks at training time — an early formal case for intermediate-step supervision.",
      tags=["learnability", "decomposition"]),

    E("malach-2023-universal-learners", "02-cot-theory", "cot-theory",
      "Auto-Regressive Next-Token Predictors are Universal Learners",
      ["Eran Malach"],
      2023, None,
      "https://arxiv.org/abs/2309.06979",
      "Shows that autoregressive next-token prediction with a chain of thought is a universal learner: any efficiently computable function can be expressed by an autoregressive predictor with polynomially-bounded intermediate token complexity.",
      tags=["chain-of-thought", "universal-learning"]),

    # ====== §3 CIRCUIT COMPLEXITY ======
    E("merrill-sabharwal-2023-parallelism", "03-circuit-complexity", "circuit-complexity",
      "The Parallelism Tradeoff: Limitations of Log-Precision Transformers",
      ["William Merrill", "Ashish Sabharwal"],
      2023, "TACL 2023",
      "https://arxiv.org/abs/2207.00729",
      "Proves that any log-precision transformer can be simulated by uniform constant-depth threshold circuits (TC0), so a single forward pass cannot decide problems believed to lie outside TC0 (e.g. matrix permanent, S5 word problem).",
      tags=["TC0", "log-precision", "circuit-complexity"]),

    E("sanford-2024-log-depth", "03-circuit-complexity", "circuit-complexity",
      "Transformers, parallel computation, and logarithmic depth",
      ["Clayton Sanford", "Daniel Hsu", "Matus Telgarsky"],
      2024, None,
      "https://arxiv.org/abs/2402.09268",
      "Identifies a hierarchy of multi-hop tasks ('k-hop induction') where O(log n)-depth attention is necessary and sufficient, separating shallow transformers from MLPs and recurrent baselines by parallel-computation depth.",
      tags=["depth", "log-depth", "k-hop"]),

    E("sanford-2023-representational", "03-circuit-complexity", "circuit-complexity",
      "Representational Strengths and Limitations of Transformers",
      ["Clayton Sanford", "Daniel Hsu", "Matus Telgarsky"],
      2023, "NeurIPS 2023",
      "https://arxiv.org/abs/2306.02896",
      "Gives matching upper and lower bounds for transformer width/depth on three-way matching and triple-detection tasks, separating attention from MLPs and unidirectional RNNs via communication-complexity arguments.",
      tags=["communication-complexity", "lower-bounds"]),

    E("peng-2024-limitations", "03-circuit-complexity", "circuit-complexity",
      "On Limitations of the Transformer Architecture",
      ["Binghui Peng", "Srini Narayanan", "Christos Papadimitriou"],
      2024, None,
      "https://arxiv.org/abs/2402.08164",
      "Uses communication-complexity arguments to show that bounded-depth, polynomial-width transformers cannot solve function composition or iterated reasoning at input length n unless they violate widely-believed complexity assumptions.",
      tags=["communication-complexity", "function-composition"]),

    E("merrill-2024-illusion-of-state", "03-circuit-complexity", "circuit-complexity",
      "The Illusion of State in State-Space Models",
      ["William Merrill", "Jackson Petty", "Ashish Sabharwal"],
      2024, "ICML 2024",
      "https://arxiv.org/abs/2404.08819",
      "Shows that linear and Mamba-style state-space models, despite being marketed as recurrent, still live in TC0 — they cannot track state-dependent problems (e.g. S5 word problem) any better than transformers can.",
      tags=["state-space-models", "TC0", "mamba"]),

    # ====== §4 LOGICAL CHARACTERIZATIONS ======
    E("merrill-sabharwal-2023-logic", "04-logical-characterizations", "logical-characterizations",
      "A Logic for Expressing Log-Precision Transformers",
      ["William Merrill", "Ashish Sabharwal"],
      2023, "NeurIPS 2023",
      "https://arxiv.org/abs/2210.02671",
      "Embeds log-precision transformers in first-order logic with majority quantifiers (FOM), giving the first logical upper-bound characterization of a realistic transformer variant.",
      tags=["FOM", "majority-logic", "log-precision"]),

    E("barcelo-2024-uhat-fol", "04-logical-characterizations", "logical-characterizations",
      "Logical Languages Accepted by Transformer Encoders with Hard Attention",
      ["Pablo Barceló", "Alexander Kozachinskiy", "Anthony Widjaja Lin", "Vladimir Podolskii"],
      2024, "ICLR 2024",
      "https://arxiv.org/abs/2310.03817",
      "Shows that unique-hard-attention encoders accept exactly the first-order definable languages with unary numerical predicates (a strict subset of AC0), and that average-hard-attention encoders climb to TC0 but no higher.",
      tags=["AC0", "TC0", "hard-attention", "first-order-logic"]),

    E("chiang-2022-overcoming", "04-logical-characterizations", "logical-characterizations",
      "Overcoming a Theoretical Limitation of Self-Attention",
      ["David Chiang", "Peter Cholak"],
      2022, "ACL 2022",
      "https://arxiv.org/abs/2202.12172",
      "Shows that augmenting attention with layer normalization in a particular way lets transformers recognize Parity and Dyck-1 — i.e. the Hahn 2020 obstruction is tied to the specific attention variant studied, not to attention per se.",
      tags=["parity", "layer-norm"]),

    E("yang-2024-masked-star-free", "04-logical-characterizations", "logical-characterizations",
      "Masked Hard-Attention Transformers Recognize Exactly the Star-Free Languages",
      ["Andy Yang", "David Chiang", "Dana Angluin"],
      2024, "NeurIPS 2024",
      "https://arxiv.org/abs/2310.13897",
      "Proves an exact characterization: causal hard-attention transformers without position embeddings recognize precisely the star-free regular languages, equivalent to LTL or FO[<].",
      tags=["star-free", "regular-languages", "FO"]),

    # ====== §5 LEARNABILITY ======
    E("garg-2022-icl-function-classes", "05-learnability", "learnability",
      "What Can Transformers Learn In-Context? A Case Study of Simple Function Classes",
      ["Shivam Garg", "Dimitris Tsipras", "Percy Liang", "Gregory Valiant"],
      2022, "NeurIPS 2022",
      "https://arxiv.org/abs/2208.01066",
      "Shows empirically and analytically that transformers trained on synthetic regression data implement, at inference, a near-optimal learner for the underlying function class — the foundational ICL-as-meta-learning result.",
      tags=["in-context-learning", "regression"]),

    E("akyurek-2023-icl-linear", "05-learnability", "learnability",
      "What learning algorithm is in-context learning? Investigations with linear models",
      ["Ekin Akyürek", "Dale Schuurmans", "Jacob Andreas", "Tengyu Ma", "Denny Zhou"],
      2023, "ICLR 2023",
      "https://arxiv.org/abs/2211.15661",
      "Demonstrates that transformers trained on linear-regression ICL tasks implement gradient-descent and ridge-regression-like estimators internally, with explicit weight constructions reproducing the empirical behavior.",
      tags=["in-context-learning", "gradient-descent"]),

    E("vonoswald-2023-icl-gd", "05-learnability", "learnability",
      "Transformers learn in-context by gradient descent",
      ["Johannes von Oswald", "Eyvind Niklasson", "Ettore Randazzo", "João Sacramento", "Alexander Mordvintsev", "Andrey Zhmoginov", "Max Vladymyrov"],
      2023, "ICML 2023",
      "https://arxiv.org/abs/2212.07677",
      "Constructs single-layer linear-attention transformers that exactly implement one step of gradient descent on a least-squares objective, and shows trained models converge to this construction.",
      tags=["in-context-learning", "gradient-descent", "linear-attention"]),

    E("xie-2022-icl-bayes", "05-learnability", "learnability",
      "An Explanation of In-context Learning as Implicit Bayesian Inference",
      ["Sang Michael Xie", "Aditi Raghunathan", "Percy Liang", "Tengyu Ma"],
      2022, "ICLR 2022",
      "https://arxiv.org/abs/2111.02080",
      "Models pretraining as a mixture-of-HMMs prior and shows in-context learning emerges as posterior inference over latent task variables, predicting the empirical scaling of demo-count benefits.",
      tags=["in-context-learning", "bayesian-inference", "HMM"]),

    E("raventos-2023-task-diversity", "05-learnability", "learnability",
      "Pretraining task diversity and the emergence of non-Bayesian in-context learning for regression",
      ["Allan Raventós", "Mansheej Paul", "Feng Chen", "Surya Ganguli"],
      2023, "NeurIPS 2023",
      "https://arxiv.org/abs/2306.15063",
      "Identifies a sharp pretraining-task-diversity threshold beyond which transformers switch from in-distribution Bayesian ICL to ridge-regression-like behavior generalizing to unseen tasks.",
      tags=["in-context-learning", "task-diversity", "regression"]),

    E("edelman-2022-inductive-biases", "05-learnability", "learnability",
      "Inductive Biases and Variable Creation in Self-Attention Mechanisms",
      ["Benjamin L. Edelman", "Surbhi Goel", "Sham Kakade", "Cyril Zhang"],
      2022, "ICML 2022",
      "https://arxiv.org/abs/2110.10090",
      "Proves sample-complexity bounds for self-attention learning sparse Boolean functions, showing the head structure provides an inductive bias that is exponentially more sample-efficient than fully-connected networks on this class.",
      tags=["sample-complexity", "sparse-functions"]),

    E("zhang-2023-trained-transformers-linear", "05-learnability", "learnability",
      "Trained Transformers Learn Linear Models In-Context",
      ["Ruiqi Zhang", "Spencer Frei", "Peter L. Bartlett"],
      2023, None,
      "https://arxiv.org/abs/2306.09927",
      "Proves that a single linear-attention layer trained on linear-regression ICL data converges to a one-step gradient-descent predictor, with explicit non-asymptotic optimization rates.",
      tags=["in-context-learning", "linear-attention", "optimization"]),

    E("ahn-2023-preconditioned-gd", "05-learnability", "learnability",
      "Transformers learn to implement preconditioned gradient descent for in-context learning",
      ["Kwangjun Ahn", "Xiang Cheng", "Hadi Daneshmand", "Suvrit Sra"],
      2023, "NeurIPS 2023",
      "https://arxiv.org/abs/2306.00297",
      "Shows that the loss landscape of trained linear-attention layers admits a stationary point implementing preconditioned gradient descent — sharper than 'plain GD' and matching empirical performance.",
      tags=["in-context-learning", "gradient-descent", "linear-attention"]),

    E("hahn-2023-emergent-icl", "05-learnability", "learnability",
      "A Theory of Emergent In-Context Learning as Implicit Structure Induction",
      ["Michael Hahn", "Navin Goyal"],
      2023, None,
      "https://arxiv.org/abs/2303.07971",
      "Derives ICL as a consequence of compositional structure in pretraining data, predicting concrete scaling laws for the emergence threshold as a function of data compositionality.",
      tags=["in-context-learning", "compositionality"]),

    # ====== §6 KNOWLEDGE EDITING ======
    E("meng-2022-rome", "06-knowledge-editing", "knowledge-editing",
      "Locating and Editing Factual Associations in GPT",
      ["Kevin Meng", "David Bau", "Alex Andonian", "Yonatan Belinkov"],
      2022, "NeurIPS 2022",
      "https://arxiv.org/abs/2202.05262",
      "Introduces causal tracing to localize factual recall to mid-layer MLPs and edits a single weight matrix (rank-one ROME update) to rewrite a fact — the load-bearing empirical claim that subsequent theoretical work tests.",
      tags=["knowledge-editing", "causal-tracing", "ROME"],
      links={"project": "https://rome.baulab.info"}),

    E("meng-2023-memit", "06-knowledge-editing", "knowledge-editing",
      "Mass-Editing Memory in a Transformer",
      ["Kevin Meng", "Arnab Sen Sharma", "Alex Andonian", "Yonatan Belinkov", "David Bau"],
      2023, "ICLR 2023",
      "https://arxiv.org/abs/2210.07229",
      "Extends ROME to thousands of simultaneous edits by solving a per-layer normal-equation update, giving the canonical 'edit-scale' baseline that later impossibility-style results push against.",
      tags=["knowledge-editing", "MEMIT"],
      links={"project": "https://memit.baulab.info"}),

    E("hase-2023-localization", "06-knowledge-editing", "knowledge-editing",
      "Does Localization Inform Editing? Surprising Differences in Causality-Based Localization vs. Knowledge Editing in Language Models",
      ["Peter Hase", "Mohit Bansal", "Been Kim", "Asma Ghandeharioun"],
      2023, "NeurIPS 2023",
      "https://arxiv.org/abs/2301.04213",
      "Shows that edit success is largely independent of the causal-trace 'hot' layer — a dissociation between localization signal and edit efficacy that complicates ROME's mechanistic interpretation.",
      tags=["knowledge-editing", "localization"]),

    E("cohen-2024-ripple-effects", "06-knowledge-editing", "knowledge-editing",
      "Evaluating the Ripple Effects of Knowledge Editing in Language Models",
      ["Roi Cohen", "Eden Biran", "Ori Yoran", "Amir Globerson", "Mor Geva"],
      2024, "TACL 2024",
      "https://arxiv.org/abs/2307.12976",
      "Defines logical ripple-effect tests (composition, two-hop, subject aliasing) for edited models and shows existing methods fail them, formalizing why naive locate-and-edit underspecifies knowledge editing.",
      tags=["knowledge-editing", "evaluation", "ripple-effects"]),

    # ====== §7 PARALLEL / ARCHITECTURAL ======
    E("hahn-2024-sensitive-functions", "07-parallel-architectural", "parallel-architectural",
      "Why are Sensitive Functions Hard for Transformers?",
      ["Michael Hahn", "Mark Rofin"],
      2024, "ACL 2024",
      "https://arxiv.org/abs/2402.09963",
      "Proves a loss-landscape bias: transformer parameters minimizing training loss tend to compute functions of low average sensitivity, explaining why parity-like high-sensitivity targets fail to be learned even when expressible.",
      tags=["sensitivity", "loss-landscape", "parity"]),

    E("liu-2023-shortcuts-automata", "07-parallel-architectural", "parallel-architectural",
      "Transformers Learn Shortcuts to Automata",
      ["Bingbin Liu", "Jordan T. Ash", "Surbhi Goel", "Akshay Krishnamurthy", "Cyril Zhang"],
      2023, "ICLR 2023",
      "https://arxiv.org/abs/2210.10749",
      "Shows that O(log T)-depth transformers can solve T-step automaton-simulation tasks via algebraic shortcuts (semigroup composition), but those shortcuts brittle-fail out of distribution — quantifying the length-generalization gap.",
      tags=["automata", "length-generalization", "shortcuts"]),

    E("zhou-2024-length-generalization", "07-parallel-architectural", "parallel-architectural",
      "What Algorithms can Transformers Learn? A Study in Length Generalization",
      ["Hattie Zhou", "Arwen Bradley", "Etai Littwin", "Noam Razin", "Omid Saremi", "Josh Susskind", "Samy Bengio", "Preetum Nakkiran"],
      2024, "ICLR 2024",
      "https://arxiv.org/abs/2310.16028",
      "Proposes the RASP-Generalization Conjecture: transformers length-generalize on a task iff the task admits a short, simple RASP-L program, and empirically supports the prediction across arithmetic and reasoning tasks.",
      tags=["length-generalization", "RASP"]),

    # ====== §8 SURVEYS / TALKS ======
    E("strobl-2024-formal-languages-survey", "08-surveys-and-talks", "surveys-and-talks",
      "What Formal Languages Can Transformers Express? A Survey",
      ["Lena Strobl", "William Merrill", "Gail Weiss", "David Chiang", "Dana Angluin"],
      2024, "TACL 12:543-561, 2024",
      "https://arxiv.org/abs/2311.00208",
      "The reference survey on transformer expressivity: organizes upper- and lower-bound results in terms of attention variant (hard / soft / saturated), precision regime, and logical / circuit characterizations.",
      tags=["survey", "expressivity"]),

]


def main() -> int:
    written = 0
    for slug, cat_dir, payload in SEED:
        out_path = ENTRIES / cat_dir / f"{slug}.yaml"
        out_path.parent.mkdir(parents=True, exist_ok=True)
        payload = {k: v for k, v in payload.items() if v is not None or k in ("venue",)}
        text = yaml.safe_dump(payload, sort_keys=False, allow_unicode=True, width=120)
        out_path.write_text(text, encoding="utf-8", newline="\n")
        written += 1

    print(f"Wrote {written} seed entries.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
