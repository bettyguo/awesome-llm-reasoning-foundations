<!-- Thanks for contributing! Please tick the boxes that apply. -->

## What is this PR?

- [ ] Adds a new entry
- [ ] Edits an existing entry
- [ ] Tooling / docs change

## For new or edited entries — required

- [ ] The YAML lives at `entries/<category>/<slug>.yaml`.
- [ ] `python tools/validate_entries.py` passes locally.
- [ ] `python tools/linkcheck.py` passes locally (or you have a reasonable explanation for transient failures).
- [ ] `python tools/build_readme.py` regenerated the README and the diff is committed.

### Verification link (mandatory for new entries)

Paste the canonical URL where the paper / talk / lecture notes can be confirmed (arXiv abstract page, OpenReview, ACL Anthology, official proceedings, or author homepage):

```
<paste URL here>
```

I confirm that, at the URL above:

- [ ] The exact title in the YAML matches the source.
- [ ] The full author list in the YAML matches the source.
- [ ] The year matches the source.
- [ ] (If `venue` is set) the venue matches the source.

### Scope

- [ ] The entry is in-scope: it advances the *theoretical foundations* of LLM reasoning (expressivity, complexity, logical characterization, CoT theory, learnability, knowledge-editing impossibility, parallel/architectural theory, or a survey/lecture covering these).
- [ ] I have read the OUT-of-scope list in the [README scope statement](../README.md#scope). If unsure, I have explained why this entry belongs in the description below.

### Annotation style

- [ ] Annotation is 1–3 sentences.
- [ ] Annotation names the formal result (e.g. "places X in TC0", "shows lower bound Y").
- [ ] No superlatives ("seminal", "groundbreaking", etc.).

## Anything else reviewers should know?

<!-- Optional: context, alternative categorizations considered, related entries, etc. -->
