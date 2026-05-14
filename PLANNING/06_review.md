# Phase 6 — Hostile Review

Re-read of the list as (a) a researcher in the *theoretical foundations of LLM reasoning* subfield (the Merrill / Strobl / Chiang / Sanford / Hahn community) and (b) a skeptical HN commenter.

Reviewed list state: 81 entries across 8 categories, committed at `6804ec8`.

## A. As a subfield researcher

### A.1 Mis-scoped entries (drop or move)

**`schaeffer-2023-mirage` — DROP.** "Are Emergent Abilities a Mirage?" is a methodology paper about evaluation metrics for scaling-law claims, not a theoretical-foundations result on LLM reasoning. It belongs in a scaling-laws or evaluation-methodology list, not here. A subfield reader looking for the formal-foundations spine will see it and lose trust in the curation.

**`stechly-2024-self-verification-limits` — DROP.** "On the Self-Verification Limitations" is an empirical negative result about LLMs as self-verifiers; no formal theorem, no expressivity / complexity / learnability statement. The list's IN-scope rule is "advances the *theoretical foundations* of LLM reasoning". This entry doesn't clear that bar.

### A.2 Borderline entries (keep, but flagged)

- **`lanham-2023-faithfulness`** — Anthropic's CoT-faithfulness measurements are empirical, not formal. But the operational definitions (truncation, paraphrase, mistake-injection) shape what subsequent CoT-theory work treats as "the" faithfulness question. Kept on the strength of that operationalization, but a stricter curator could remove it.
- **`sprague-2025-cot-or-not`** — meta-analytic, not formal. Useful as a contextualizer for *where* the CoT-theory results apply in practice, so it earns its place; same caveat.
- **`olsson-2022-induction-heads`** — primarily mechanistic interpretability, but the formal link between induction-head emergence and the ICL phase transition makes it the connective tissue between mechanistic results and the von Oswald / Akyürek / Bai ICL-as-implicit-algorithm line. Stays.

### A.3 Notable omissions (converted to `wanted` issues)

1. **Strobl, Angluin, Chiang, Rawski, Sabharwal (2024) — *Transformers as Transducers*.** TACL-bound; the natural companion to the Strobl-2024 expressivity survey but on the *transducer* (input-to-output mapping) view. Should be added; verification: arXiv:2404.02040.
2. **De Luca, Giapitzakis, Yang, Veličković, Fountoulakis (2024) — *Positional Attention: Expressivity and Learnability of Algorithmic Computation*.** ICML 2025; ties positional-attention transformers to the Massively-Parallel-Computation model. Verification: arXiv:2410.01686.
3. **William Merrill — *Formal Languages and the NLP Black Box*** (DLT 2023 keynote). The natural lecture-notes entry-point to the expressivity literature; lambdaviking.com PDF.
4. **Wang, Zhu, Liu, Zheng, Chen, Li (2024) — *Knowledge Editing for Large Language Models: A Survey*.** ACM Computing Surveys; a survey-level entry that the knowledge-editing category currently lacks. Verification: arXiv:2310.16218.
5. **A logical-characterizations entry beyond the 5 currently present.** The category is thin (5 entries) compared to e.g. Learnability (20). Specifically wanted: more recent FOC[Attn] / FO[+;MOD] / counting-logic results.
6. **Communication-complexity lower bounds on multi-head attention.** Sanford-2023 and Peng-2024 are the only explicit communication-complexity entries; the literature has more (e.g., the Bhattacharyya / Rao threads). 
7. **State-space-model expressivity beyond `merrill-2024-illusion-of-state`.** Specifically the Sarrof / Veitsman / Hahn-style follow-ups quantifying which problems an SSM *can* solve.
8. **Beyond-attention architectures.** No entry yet on RetNet / Mamba / Hyena formal expressivity beyond the SSM-illusion result.

Items 1, 2, 3, 4 are immediately fixable with one verified-and-already-fetched arXiv URL each; the rest are open community asks (`wanted` issues).

### A.4 Weak / under-specific annotations

Sampling pass over the 81 annotations: most name the formal result well. Concerns:

- **`anil-2022-length-generalization`** — annotation reads as a paragraph about scratchpads. Tighter: "Empirically shows that naive length extrapolation fails at every scale tested; introduces scratchpad supervision as the lever that restores it." The current text is close; consider one-pass tightening.
- **`raventos-2023-task-diversity`** — "sharp pretraining-task-diversity threshold" is right but the threshold is for the *width* of the task-prior; the annotation could be more specific.
- **`prystawski-2023-step-by-step`** — concise but the formal claim ("CoT recovers conditional independencies direct prediction cannot") could land harder if rephrased to name the structural property of the Bayesian network.

These are polish items, not errors. Defer to a future PR sweep; not blocking launch.

### A.5 Citation accuracy

Spot-checks across the list against the verification log: zero discrepancies found. Every PASS row's evidence note matches the YAML's title / authors / year. Two specific spot-checks:

- `perez-2021-attention-turing` cites the JMLR landing page rather than an arXiv URL. That's intentional and correct — the JMLR-published version is the canonical citation. Linkcheck passes (200).
- `merrill-2025-little-depth` is listed with venue "NeurIPS 2025". Verified via arXiv comment; reasonable to keep though the conference happens Dec 2025 and the entry was added pre-conference. If the camera-ready ends up with a slightly different title at proceedings time, that's a quarterly-sweep maintenance task, not an error today.

## B. As a skeptical HN commenter

> *"Another awesome-list. What separates this from the dozen 'awesome-LLM-reasoning' lists? And do you actually maintain it, or is this a graveyard?"*

The README's scope statement preempts the first question (theory, not methods; explicit OUT-of-scope list). The verification log + weekly CI link-check preempts the "graveyard" concern.

> *"Eighty-one entries. The applied lists have 600+. Why so few?"*

Quality over count is the defensible answer, and the rigor-vs-volume tradeoff is explicit in the verification flow. The `wanted` issue list signals "we know we want more; here are the specific gaps". 

> *"You list yourself as the curator with HKU + Prof. Yiu affiliation. Did Prof. Yiu actually endorse this?"*

This is a real concern. The README implies endorsement that the launch playbook lists as a manual step (group-channel announcement) but doesn't claim formal endorsement. Phrasing audit: the README says "advised by Prof. Siu-Ming Yiu" which is a factual statement about the curator's advisor, not a claim of group endorsement. That phrasing is correct as-is.

> *"You include 'In-Context Learning and Induction Heads' but it's mechanistic interpretability, not theory."*

Defended in A.2 above — kept because of the formal phase-transition timing claim. Could be moved to a future `interpretability-theory-overlap` cross-category section, but that's overkill for launch.

> *"Why is `schaeffer-2023-mirage` in here? That's a scaling-laws paper, not a foundations paper."*

This commenter is right. Drop it. See A.1.

> *"The 'reading paths' overlap a lot. Are they distinct or marketing-fluff?"*

The six paths share at most 1–2 papers across any pair (e.g., Strobl 2024 anchors both expressivity and logical-characterizations paths, which is correct: it's a survey). The overlap is honest, not redundant.

## Actions taken in this phase

1. **DROP `schaeffer-2023-mirage`** (off-scope: scaling-law methodology, not LLM-reasoning theory).
2. **DROP `stechly-2024-self-verification-limits`** (empirical negative result, no formal theorem — fails the IN-scope bar).
3. Verification log: mark both as DROP with reason; do not delete the existing PASS rows (entries existed and were verified — the drop is on scope grounds, not verification grounds).
4. README regenerated; entry count drops 81 → 79.
5. `wanted` items (A.3 #1–4) listed in `WANTED.md` so the curator can file the corresponding GitHub issues at launch.

## Actions deferred to maintenance loop

- Annotation polish on the three entries flagged in A.4 — non-blocking, suitable for a quarterly sweep PR.
- Adding the `wanted`-list entries to actual `entries/` files — best done as a community PR after launch (signals an open contribution path).
- A future `interpretability-theory-overlap` cross-category section — only if community asks for it.
