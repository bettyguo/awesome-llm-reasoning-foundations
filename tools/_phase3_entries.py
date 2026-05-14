#!/usr/bin/env python3
"""Phase 3 expansion — adds verified entries to the seed list.

Same one-shot pattern as _seed_entries.py. Safe to delete after the pass.
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
    payload = {
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
    }
    return (slug, cat_dir, payload)


ENTRIES_PHASE3 = [

    # ====== §1 EXPRESSIVITY ======
    E("weiss-2021-thinking-like-transformers", "01-expressivity", "expressivity",
      "Thinking Like Transformers",
      ["Gail Weiss", "Yoav Goldberg", "Eran Yahav"],
      2021, "ICML 2021",
      "https://arxiv.org/abs/2106.06981",
      "Introduces RASP, a small functional language compiled into transformer circuits, giving researchers a concrete handle on which algorithms a transformer can express and grounding many later expressivity proofs.",
      tags=["RASP", "expressivity", "compilation"]),

    E("hao-2022-hard-attention-circuit", "01-expressivity", "expressivity",
      "Formal Language Recognition by Hard Attention Transformers: Perspectives from Circuit Complexity",
      ["Yiding Hao", "Dana Angluin", "Robert Frank"],
      2022, "TACL 2022",
      "https://arxiv.org/abs/2204.06618",
      "Places hard-attention transformer encoders inside AC0 and gives matching lower-bound separations between hard-attention variants, anchoring the circuit-complexity view of attention.",
      tags=["AC0", "hard-attention", "circuit-complexity"]),

    E("friedman-2023-learning-transformer-programs", "01-expressivity", "expressivity",
      "Learning Transformer Programs",
      ["Dan Friedman", "Alexander Wettig", "Danqi Chen"],
      2023, "NeurIPS 2023",
      "https://arxiv.org/abs/2306.01128",
      "Trains transformers under a discrete parameterization that compiles directly to RASP programs, turning the expressivity-via-RASP construction into a recipe for mechanistic readability of trained models.",
      tags=["RASP", "interpretability", "expressivity"]),

    E("strobl-2023-average-hard-tc0", "01-expressivity", "expressivity",
      "Average-Hard Attention Transformers are Constant-Depth Uniform Threshold Circuits",
      ["Lena Strobl"],
      2023, None,
      "https://arxiv.org/abs/2308.03212",
      "Strengthens the Merrill-Sabharwal-Smith TC0 bound by showing it holds for average-hard attention (a more realistic attention idealization) and with uniform — not merely DLOGTIME-uniform — circuits.",
      tags=["TC0", "average-hard-attention", "uniform-circuits"]),

    # ====== §2 CoT THEORY ======
    E("dziri-2023-faith-and-fate", "02-cot-theory", "cot-theory",
      "Faith and Fate: Limits of Transformers on Compositionality",
      ["Nouha Dziri", "Ximing Lu", "Melanie Sclar", "Xiang Lorraine Li", "Liwei Jiang", "Bill Yuchen Lin", "Peter West", "Chandra Bhagavatula", "Ronan Le Bras", "Jena D. Hwang", "Soumya Sanyal", "Sean Welleck", "Xiang Ren", "Allyson Ettinger", "Zaid Harchaoui", "Yejin Choi"],
      2023, "NeurIPS 2023",
      "https://arxiv.org/abs/2305.18654",
      "Quantifies how transformer accuracy on multi-step compositional tasks (multi-digit multiplication, logic grids, dynamic programming) degrades with computation-graph depth, supporting the parallel-depth-bound theory predictions empirically.",
      tags=["compositionality", "multi-step", "scaling"]),

    E("bachmann-2024-pitfalls-next-token", "02-cot-theory", "cot-theory",
      "The pitfalls of next-token prediction",
      ["Gregor Bachmann", "Vaishnavh Nagarajan"],
      2024, "ICML 2024",
      "https://arxiv.org/abs/2403.06963",
      "Identifies the 'Clever Hans cheat' and 'snowball error' failure modes of teacher-forced next-token training, showing planning-like tasks suffer in-principle even with perfect data — a formal critique of vanilla autoregressive learning.",
      tags=["next-token-prediction", "planning", "teacher-forcing"]),

    E("goyal-2024-pause-tokens", "02-cot-theory", "cot-theory",
      "Think before you speak: Training Language Models With Pause Tokens",
      ["Sachin Goyal", "Ziwei Ji", "Ankit Singh Rawat", "Aditya Krishna Menon", "Sanjiv Kumar", "Vaishnavh Nagarajan"],
      2024, "ICLR 2024",
      "https://arxiv.org/abs/2310.02226",
      "Shows that inserting dummy 'pause' tokens at train and inference time gives transformers extra parallel compute steps before emission, with measurable gains on reasoning benchmarks — an experimental counterpart to CoT-as-extra-computation theory.",
      tags=["chain-of-thought", "pause-tokens", "extra-compute"]),

    E("pfau-2024-dot-by-dot", "02-cot-theory", "cot-theory",
      "Let's Think Dot by Dot: Hidden Computation in Transformer Language Models",
      ["Jacob Pfau", "William Merrill", "Samuel R. Bowman"],
      2024, None,
      "https://arxiv.org/abs/2404.15758",
      "Demonstrates that filler tokens with no semantic content can serve the same expressivity-extension role as CoT for certain in-TC0-hard problems, separating CoT's parallel-compute benefit from its interpretability benefit.",
      tags=["chain-of-thought", "filler-tokens"]),

    # ====== §3 CIRCUIT COMPLEXITY ======
    E("liu-2023-flip-flop-glitches", "03-circuit-complexity", "circuit-complexity",
      "Exposing Attention Glitches with Flip-Flop Language Modeling",
      ["Bingbin Liu", "Jordan T. Ash", "Surbhi Goel", "Akshay Krishnamurthy", "Cyril Zhang"],
      2023, "NeurIPS 2023",
      "https://arxiv.org/abs/2306.00946",
      "Identifies the 'attention glitch' failure mode on a minimal flip-flop language — transformers fit the train distribution exactly yet fail one-token tasks at distribution edges, exposing a sharp generalization gap in the attention mechanism.",
      tags=["attention-glitches", "flip-flop", "generalization"]),

    E("mahdavi-2023-memorization-capacity", "03-circuit-complexity", "circuit-complexity",
      "Memorization Capacity of Multi-Head Attention in Transformers",
      ["Sadegh Mahdavi", "Renjie Liao", "Christos Thrampoulidis"],
      2023, "ICLR 2024",
      "https://arxiv.org/abs/2306.02010",
      "Proves that an H-head attention layer with O(Hd^2) parameters memorizes Θ(Hn) examples, isolating multi-head structure as the source of the memorization-vs-parameters scaling.",
      tags=["memorization", "multi-head", "capacity"]),

    E("chen-2024-provably-learning-mha", "03-circuit-complexity", "circuit-complexity",
      "Provably learning a multi-head attention layer",
      ["Sitan Chen", "Yuanzhi Li"],
      2024, None,
      "https://arxiv.org/abs/2402.04084",
      "Gives the first polynomial-time learning algorithm with provable guarantees for a single multi-head attention layer under non-degeneracy conditions, plus matching lower bounds — initiates the computational-learning-theory analysis of attention.",
      tags=["learning-theory", "multi-head"]),

    E("wang-2024-sparse-token-selection", "03-circuit-complexity", "circuit-complexity",
      "Transformers Provably Learn Sparse Token Selection While Fully-Connected Nets Cannot",
      ["Zixuan Wang", "Stanley Wei", "Daniel Hsu", "Jason D. Lee"],
      2024, None,
      "https://arxiv.org/abs/2406.06893",
      "Provides a learning separation between transformers and MLPs on a sparse-token-selection task, showing transformers learn the task in polynomial samples while any polynomial-width MLP requires exponentially many.",
      tags=["learning-separation", "sparse"]),

    # ====== §4 LOGICAL CHARACTERIZATIONS ======
    E("yang-2024-counting-like-transformers", "04-logical-characterizations", "logical-characterizations",
      "Counting Like Transformers: Compiling Temporal Counting Logic Into Softmax Transformers",
      ["Andy Yang", "David Chiang"],
      2024, None,
      "https://arxiv.org/abs/2404.04393",
      "Compiles temporal counting logic K[#] directly into softmax-attention transformers, giving a constructive lower bound and refining the logical characterization of soft-attention encoders.",
      tags=["counting-logic", "softmax", "first-order-logic"]),

    # ====== §5 LEARNABILITY ======
    E("bai-2023-transformers-statisticians", "05-learnability", "learnability",
      "Transformers as Statisticians: Provable In-Context Learning with In-Context Algorithm Selection",
      ["Yu Bai", "Fan Chen", "Huan Wang", "Caiming Xiong", "Song Mei"],
      2023, "NeurIPS 2023",
      "https://arxiv.org/abs/2306.04637",
      "Constructs transformers that approximate a broad family of statistical estimators (OLS, ridge, lasso, even cross-validated selection among them) at inference, formalizing ICL as in-context algorithm selection.",
      tags=["in-context-learning", "algorithm-selection"]),

    E("mahankali-2023-one-step-gd", "05-learnability", "learnability",
      "One Step of Gradient Descent is Provably the Optimal In-Context Learner with One Layer of Linear Self-Attention",
      ["Arvind Mahankali", "Tatsunori B. Hashimoto", "Tengyu Ma"],
      2023, None,
      "https://arxiv.org/abs/2307.03576",
      "Proves that for ICL on linear regression with a single linear-attention layer, the global-minimum solution is exactly one step of gradient descent on the in-context dataset — the tightest characterization in this regime.",
      tags=["in-context-learning", "linear-attention", "optimality"]),

    E("wu-2024-how-many-tasks", "05-learnability", "learnability",
      "How Many Pretraining Tasks Are Needed for In-Context Learning of Linear Regression?",
      ["Jingfeng Wu", "Difan Zou", "Zixiang Chen", "Vladimir Braverman", "Quanquan Gu", "Peter L. Bartlett"],
      2024, "ICLR 2024",
      "https://arxiv.org/abs/2310.08391",
      "Proves a sharp threshold on the number of pretraining tasks required for a linear-attention model to ICL-generalize to unseen tasks, complementing Raventós et al.'s empirical task-diversity phase transition with closed-form bounds.",
      tags=["in-context-learning", "sample-complexity"]),

    E("olsson-2022-induction-heads", "05-learnability", "learnability",
      "In-context Learning and Induction Heads",
      ["Catherine Olsson", "Nelson Elhage", "Neel Nanda", "Nicholas Joseph", "Nova DasSarma", "Tom Henighan", "Ben Mann", "Amanda Askell", "Yuntao Bai", "Anna Chen", "Tom Conerly", "Dawn Drain", "Deep Ganguli", "Zac Hatfield-Dodds", "Danny Hernandez", "Scott Johnston", "Andy Jones", "Jackson Kernion", "Liane Lovitt", "Kamal Ndousse", "Dario Amodei", "Tom Brown", "Jack Clark", "Jared Kaplan", "Sam McCandlish", "Chris Olah"],
      2022, None,
      "https://arxiv.org/abs/2209.11895",
      "Identifies 'induction heads' — small two-head circuits that implement copy-and-predict — as the mechanistic substrate of basic in-context learning, providing the empirical anchor against which later ICL theories are tested.",
      tags=["in-context-learning", "induction-heads", "mechanistic"]),

    E("wen-2024-rnns-not-transformers", "05-learnability", "learnability",
      "RNNs are not Transformers (Yet): The Key Bottleneck on In-context Retrieval",
      ["Kaiyue Wen", "Xingyu Dang", "Kaifeng Lyu"],
      2024, None,
      "https://arxiv.org/abs/2402.18510",
      "Proves a representational separation: RNNs of any polynomial size cannot perform in-context retrieval of length-Θ(n) keys, while transformers can, identifying retrieval as a hard ceiling for non-attention sequence models.",
      tags=["RNN", "in-context-retrieval", "separation"]),

    E("akyurek-2024-in-context-language", "05-learnability", "learnability",
      "In-Context Language Learning: Architectures and Algorithms",
      ["Ekin Akyürek", "Bailin Wang", "Yoon Kim", "Jacob Andreas"],
      2024, None,
      "https://arxiv.org/abs/2401.12973",
      "Extends ICL theory from regression to formal-language learning: builds a benchmark of in-context formal-language tasks and shows transformers approach the Bayes-optimal learner where state-space models lag.",
      tags=["in-context-learning", "formal-languages"]),

    E("allenzhu-2023-physics-part1", "05-learnability", "learnability",
      "Physics of Language Models: Part 1, Learning Hierarchical Language Structures",
      ["Zeyuan Allen-Zhu", "Yuanzhi Li"],
      2023, None,
      "https://arxiv.org/abs/2305.13673",
      "Controlled experiments on synthetic CFG-generated text show transformers acquire hierarchical syntactic structure through a specific attention pattern (\"diagonal then off-diagonal\") tied to grammar depth.",
      tags=["context-free-grammar", "syntactic-learning"]),

    # ====== §6 KNOWLEDGE EDITING ======
    E("mitchell-2022-mend", "06-knowledge-editing", "knowledge-editing",
      "Fast Model Editing at Scale",
      ["Eric Mitchell", "Charles Lin", "Antoine Bosselut", "Chelsea Finn", "Christopher D. Manning"],
      2022, "ICLR 2022",
      "https://arxiv.org/abs/2110.11309",
      "Introduces MEND, a hypernetwork that transforms gradients into rank-1 model edits — the canonical 'learned-editor' baseline that locate-and-edit approaches (ROME, MEMIT) are compared against.",
      tags=["knowledge-editing", "MEND", "hypernetwork"]),

    E("decao-2021-editing-factual", "06-knowledge-editing", "knowledge-editing",
      "Editing Factual Knowledge in Language Models",
      ["Nicola De Cao", "Wilker Aziz", "Ivan Titov"],
      2021, "EMNLP 2021",
      "https://arxiv.org/abs/2104.08164",
      "Introduces KnowledgeEditor, the first hypernetwork-based fact editor for masked language models — opens the formal study of how to surgically rewrite a model's facts without retraining.",
      tags=["knowledge-editing", "hypernetwork"]),

    E("geva-2021-ffn-key-value", "06-knowledge-editing", "knowledge-editing",
      "Transformer Feed-Forward Layers Are Key-Value Memories",
      ["Mor Geva", "Roei Schuster", "Jonathan Berant", "Omer Levy"],
      2021, "EMNLP 2021",
      "https://arxiv.org/abs/2012.14913",
      "Provides the load-bearing empirical claim that feed-forward sublayers behave as key-value memories — the mechanism that ROME, MEMIT, and later locate-and-edit work depend on.",
      tags=["feed-forward", "key-value-memory", "interpretability"]),

    E("geva-2023-dissecting-recall", "06-knowledge-editing", "knowledge-editing",
      "Dissecting Recall of Factual Associations in Auto-Regressive Language Models",
      ["Mor Geva", "Jasmijn Bastings", "Katja Filippova", "Amir Globerson"],
      2023, "EMNLP 2023",
      "https://arxiv.org/abs/2304.14767",
      "Decomposes factual recall into three stages (subject enrichment, relation propagation, attribute extraction), giving a refined picture of where edits do and do not propagate — directly relevant to ripple-effect and impossibility results.",
      tags=["factual-recall", "mechanistic"]),

    E("allenzhu-2023-physics-3-1", "06-knowledge-editing", "knowledge-editing",
      "Physics of Language Models: Part 3.1, Knowledge Storage and Extraction",
      ["Zeyuan Allen-Zhu", "Yuanzhi Li"],
      2023, "ICML 2024",
      "https://arxiv.org/abs/2309.14316",
      "Demonstrates that knowledge memorized without augmented paraphrasing during pretraining is not extractable downstream, with linear-probing evidence linking extraction success to specific token-embedding encodings.",
      tags=["knowledge-storage", "extraction", "data-augmentation"]),

    E("allenzhu-2023-physics-3-2", "06-knowledge-editing", "knowledge-editing",
      "Physics of Language Models: Part 3.2, Knowledge Manipulation",
      ["Zeyuan Allen-Zhu", "Yuanzhi Li"],
      2023, None,
      "https://arxiv.org/abs/2309.14402",
      "Shows that even when knowledge is reliably extractable, simple manipulations of that knowledge (inverse lookup, comparison, composition) systematically fail — formalizing a manipulation-vs-storage gap.",
      tags=["knowledge-manipulation", "inverse-lookup"]),

    # ====== §7 PARALLEL / ARCHITECTURAL ======
    E("anil-2022-length-generalization", "07-parallel-architectural", "parallel-architectural",
      "Exploring Length Generalization in Large Language Models",
      ["Cem Anil", "Yuhuai Wu", "Anders Andreassen", "Aitor Lewkowycz", "Vedant Misra", "Vinay Ramasesh", "Ambrose Slone", "Guy Gur-Ari", "Ethan Dyer", "Behnam Neyshabur"],
      2022, "NeurIPS 2022",
      "https://arxiv.org/abs/2207.04901",
      "Establishes the empirical baseline for length generalization: across model scales, naive next-token training fails to extrapolate to longer sequences, and CoT-style scratchpads help but do not close the gap.",
      tags=["length-generalization", "scratchpad"]),

    E("kazemnejad-2023-positional-encoding", "07-parallel-architectural", "parallel-architectural",
      "The Impact of Positional Encoding on Length Generalization in Transformers",
      ["Amirhossein Kazemnejad", "Inkit Padhi", "Karthikeyan Natesan Ramamurthy", "Payel Das", "Siva Reddy"],
      2023, "NeurIPS 2023",
      "https://arxiv.org/abs/2305.19466",
      "Compares positional-encoding choices (absolute, ALiBi, RoPE, none) under controlled length-generalization tests and finds that no-positional-encoding (NoPE) generalizes best on small reasoning tasks — counterintuitive yet repeatable.",
      tags=["positional-encoding", "length-generalization", "NoPE"]),

    E("ruoss-2023-randomized-pe", "07-parallel-architectural", "parallel-architectural",
      "Randomized Positional Encodings Boost Length Generalization of Transformers",
      ["Anian Ruoss", "Grégoire Delétang", "Tim Genewein", "Jordi Grau-Moya", "Róbert Csordás", "Mehdi Bennani", "Shane Legg", "Joel Veness"],
      2023, None,
      "https://arxiv.org/abs/2305.16843",
      "Shows randomizing the index set of absolute positions during training extends transformers' length-generalization range by 20×+ on synthetic algorithmic tasks, with no architectural change.",
      tags=["positional-encoding", "length-generalization", "randomization"]),

    E("stechly-2024-self-verification-limits", "07-parallel-architectural", "parallel-architectural",
      "On the Self-Verification Limitations of Large Language Models on Reasoning and Planning Tasks",
      ["Kaya Stechly", "Karthik Valmeekam", "Subbarao Kambhampati"],
      2024, None,
      "https://arxiv.org/abs/2402.08115",
      "Shows that LLMs asked to verify their own reasoning add no measurable signal beyond random self-criticism — a load-bearing negative result against self-consistency / self-correction loops as primitives for reliable reasoning.",
      tags=["self-verification", "self-correction", "planning"]),

    # ====== §8 SURVEYS / TALKS ======
    E("transformers-theory-workshop-2025", "08-surveys-and-talks", "surveys-and-talks",
      "What Can('t) Transformers Do? (NeurIPS 2025 Workshop)",
      ["Tobias Schnabel", "Kiran Tomlinson", "Lena Strobl", "Michael Hahn"],
      2025, "NeurIPS 2025 Workshop",
      "https://transformerstheory.github.io/",
      "Community gathering of the transformer-theory subfield: accepted papers and invited talks survey what is known and unknown about transformer expressivity, learnability, and complexity as of late 2025.",
      tags=["workshop", "community"]),

]


def main() -> int:
    written = 0
    skipped = 0
    for slug, cat_dir, payload in ENTRIES_PHASE3:
        out_path = ENTRIES / cat_dir / f"{slug}.yaml"
        if out_path.exists():
            print(f"SKIP exists: {out_path.relative_to(REPO_ROOT)}")
            skipped += 1
            continue
        out_path.parent.mkdir(parents=True, exist_ok=True)
        text = yaml.safe_dump(payload, sort_keys=False, allow_unicode=True, width=120)
        out_path.write_text(text, encoding="utf-8", newline="\n")
        written += 1

    print(f"Wrote {written} new entries; skipped {skipped} existing.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
