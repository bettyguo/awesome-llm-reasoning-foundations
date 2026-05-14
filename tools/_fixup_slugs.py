#!/usr/bin/env python3
"""Fixup: write the canonical-slug entries that match existing PASS rows.

I created Phase 3 entries with slightly different slug names from the canonical
ones in PLANNING/02_verification_log.md. This script re-creates the entries
under the canonical slug names so the validator can map every YAML to its
PASS row.
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


REWRITES = [
    E("weiss-2021-rasp", "01-expressivity", "expressivity",
      "Thinking Like Transformers",
      ["Gail Weiss", "Yoav Goldberg", "Eran Yahav"],
      2021, "ICML 2021",
      "https://arxiv.org/abs/2106.06981",
      "Introduces RASP, a small functional language compiled into transformer circuits, giving researchers a concrete handle on which algorithms a transformer can express and grounding many later expressivity proofs.",
      tags=["RASP", "expressivity", "compilation"]),

    E("friedman-2023-transformer-programs", "01-expressivity", "expressivity",
      "Learning Transformer Programs",
      ["Dan Friedman", "Alexander Wettig", "Danqi Chen"],
      2023, "NeurIPS 2023",
      "https://arxiv.org/abs/2306.01128",
      "Trains transformers under a discrete parameterization that compiles directly to RASP programs, turning expressivity-via-RASP into a recipe for mechanistic readability of trained models.",
      tags=["RASP", "interpretability", "expressivity"]),

    E("liu-2023-flip-flop", "01-expressivity", "expressivity",
      "Exposing Attention Glitches with Flip-Flop Language Modeling",
      ["Bingbin Liu", "Jordan T. Ash", "Surbhi Goel", "Akshay Krishnamurthy", "Cyril Zhang"],
      2023, "NeurIPS 2023",
      "https://arxiv.org/abs/2306.00946",
      "Identifies the 'attention glitch' failure mode on a minimal flip-flop language: transformers fit the train distribution exactly yet fail one-token tasks at distribution edges, exposing a sharp generalization gap in the attention mechanism.",
      tags=["attention-glitches", "flip-flop", "generalization"]),

    E("strobl-2023-ahat-tc0", "03-circuit-complexity", "circuit-complexity",
      "Average-Hard Attention Transformers are Constant-Depth Uniform Threshold Circuits",
      ["Lena Strobl"],
      2023, None,
      "https://arxiv.org/abs/2308.03212",
      "Strengthens the Merrill-Sabharwal-Smith TC0 bound by showing it holds for average-hard attention (a more realistic attention idealization) and with uniform circuits, not merely DLOGTIME-uniform circuits.",
      tags=["TC0", "average-hard-attention", "uniform-circuits"]),

    E("dziri-2023-faith-fate", "07-parallel-architectural", "parallel-architectural",
      "Faith and Fate: Limits of Transformers on Compositionality",
      ["Nouha Dziri", "Ximing Lu", "Melanie Sclar", "Xiang Lorraine Li", "Liwei Jiang", "Bill Yuchen Lin", "Peter West", "Chandra Bhagavatula", "Ronan Le Bras", "Jena D. Hwang", "Soumya Sanyal", "Sean Welleck", "Xiang Ren", "Allyson Ettinger", "Zaid Harchaoui", "Yejin Choi"],
      2023, "NeurIPS 2023",
      "https://arxiv.org/abs/2305.18654",
      "Quantifies how transformer accuracy on multi-step compositional tasks (multi-digit multiplication, logic grids, dynamic programming) degrades with computation-graph depth, supporting parallel-depth-bound theory predictions empirically.",
      tags=["compositionality", "multi-step", "scaling"]),

    E("bai-2023-statisticians", "05-learnability", "learnability",
      "Transformers as Statisticians: Provable In-Context Learning with In-Context Algorithm Selection",
      ["Yu Bai", "Fan Chen", "Huan Wang", "Caiming Xiong", "Song Mei"],
      2023, "NeurIPS 2023",
      "https://arxiv.org/abs/2306.04637",
      "Constructs transformers that approximate a broad family of statistical estimators (OLS, ridge, lasso, even cross-validated selection among them) at inference, formalizing ICL as in-context algorithm selection.",
      tags=["in-context-learning", "algorithm-selection"]),

    E("mahankali-2024-onestep-gd", "05-learnability", "learnability",
      "One Step of Gradient Descent is Provably the Optimal In-Context Learner with One Layer of Linear Self-Attention",
      ["Arvind Mahankali", "Tatsunori B. Hashimoto", "Tengyu Ma"],
      2023, "ICLR 2024",
      "https://arxiv.org/abs/2307.03576",
      "Proves that for ICL on linear regression with a single linear-attention layer, the global-minimum solution is exactly one step of gradient descent on the in-context dataset — the tightest characterization in this regime.",
      tags=["in-context-learning", "linear-attention", "optimality"]),

    E("wu-2024-pretraining-tasks", "05-learnability", "learnability",
      "How Many Pretraining Tasks Are Needed for In-Context Learning of Linear Regression?",
      ["Jingfeng Wu", "Difan Zou", "Zixiang Chen", "Vladimir Braverman", "Quanquan Gu", "Peter L. Bartlett"],
      2024, "ICLR 2024",
      "https://arxiv.org/abs/2310.08391",
      "Proves a sharp threshold on the number of pretraining tasks required for a linear-attention model to ICL-generalize to unseen tasks, complementing Raventós et al.'s empirical task-diversity phase transition with closed-form bounds.",
      tags=["in-context-learning", "sample-complexity"]),

    E("kazemnejad-2023-pos-enc", "07-parallel-architectural", "parallel-architectural",
      "The Impact of Positional Encoding on Length Generalization in Transformers",
      ["Amirhossein Kazemnejad", "Inkit Padhi", "Karthikeyan Natesan Ramamurthy", "Payel Das", "Siva Reddy"],
      2023, "NeurIPS 2023",
      "https://arxiv.org/abs/2305.19466",
      "Compares positional-encoding choices (absolute, ALiBi, RoPE, none) under controlled length-generalization tests and finds that no-positional-encoding (NoPE) generalizes best on small reasoning tasks — counterintuitive yet repeatable.",
      tags=["positional-encoding", "length-generalization", "NoPE"]),

    E("ruoss-2023-random-pos", "07-parallel-architectural", "parallel-architectural",
      "Randomized Positional Encodings Boost Length Generalization of Transformers",
      ["Anian Ruoss", "Grégoire Delétang", "Tim Genewein", "Jordi Grau-Moya", "Róbert Csordás", "Mehdi Bennani", "Shane Legg", "Joel Veness"],
      2023, "ACL 2023",
      "https://arxiv.org/abs/2305.16843",
      "Shows randomizing the index set of absolute positions during training extends transformers' length-generalization range by 20× or more on synthetic algorithmic tasks, with no architectural change.",
      tags=["positional-encoding", "length-generalization", "randomization"]),
]


def main() -> int:
    written = 0
    for slug, cat_dir, payload in REWRITES:
        out_path = ENTRIES / cat_dir / f"{slug}.yaml"
        out_path.parent.mkdir(parents=True, exist_ok=True)
        text = yaml.safe_dump(payload, sort_keys=False, allow_unicode=True, width=120)
        out_path.write_text(text, encoding="utf-8", newline="\n")
        written += 1
    print(f"Wrote {written} canonical-slug entries.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
