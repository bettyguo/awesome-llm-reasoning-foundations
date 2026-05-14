# Contributing

Thanks for considering a contribution. This list lives or dies on citation accuracy, so the contribution process is built around verification.

## TL;DR

1. Open an issue first if you're proposing a new entry — that's the fastest way to confirm scope before you do the writing work.
2. Add or edit one YAML file under `entries/<category>/<slug>.yaml`.
3. Run the validators locally.
4. Open a PR with a verification URL.

## Is my entry in scope?

**In scope:** formal expressivity results for transformers (universal approximation, formal-language recognition, saturation, hard vs. soft attention); chain-of-thought theory and error bounds; circuit / communication / parallel complexity; logical characterizations (FOC[Attn], FO+MOD, counting logics); learnability and sample-complexity theory; knowledge-editing impossibility results; surveys and lecture notes covering the above.

**Out of scope** (intentionally — excellent applied lists exist for these):

- Chain-of-thought prompting recipes, decoding tricks, self-consistency variants.
- Agent and tool-use frameworks.
- RLHF / RLVR methodology, reward modeling, preference learning *applications*.
- o1 / DeepSeek-R1 follow-ups that don't carry a formal result.
- Jailbreaks, prompt-injection attacks.
- Leaderboards and benchmark releases without a theoretical contribution.
- Multimodal CoT *applications*.

If you're unsure, file a `new-entry` issue and we'll discuss before you write the YAML.

## Local setup

```
pip install -r tools/requirements.txt
```

That's the entire dependency surface: PyYAML and httpx.

## Adding an entry

1. Pick a category directory under `entries/` (the leading number is for sort-order convenience only; the category in the YAML is the source of truth).
2. Create `entries/<category>/<slug>.yaml`. Slug format: `<lead-author-surname-lowercased>-<year>-<short-keyword>`. Example: `merrill-sabharwal-2024-cot.yaml`.
3. Fill in the schema (copy an existing entry for reference). All fields documented in `PLANNING/01_design.md`.
4. Run:

   ```
   python tools/validate_entries.py
   python tools/linkcheck.py        # may be slow due to network
   python tools/build_readme.py
   git add entries/ README.md
   ```

5. Add a `PASS` row for your entry's slug to `PLANNING/02_verification_log.md` recording where you verified title/authors/year.
6. Open a PR. The template asks you to paste the verification URL.

## What the validators enforce

- `validate_entries.py`: schema (required fields, types, category enum, annotation length, slug format, no banned superlatives), slug uniqueness across the repo, that every entry has a `PASS` row in `PLANNING/02_verification_log.md`.
- `linkcheck.py`: every URL in every entry resolves with status `< 400` (retry once on transient failure).
- The validate workflow rebuilds the README from `entries/` and fails if it differs from the checked-in README (drift detection).

## Annotation style

One to three sentences. Name the formal result. No "this paper..." padding. No superlatives. Concrete examples that read well:

> Characterizes the expressive power of decoder-only transformers with CoT as a function of generation length: log-many steps stay in TC0, linear-many reach P.

> Shows that log-precision transformers can be simulated by uniform constant-depth threshold circuits (TC0), placing a hard upper bound on what a single forward pass can compute.

Counter-examples to avoid:

> ❌ "This seminal paper introduces a groundbreaking framework..."
> ❌ "A must-read for anyone interested in..."
> ❌ "Discusses chain-of-thought." (too vague — name the result)

## Code of Conduct

Be respectful. Disagreements over categorization or scope are expected; ad-hominem is not. See [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md).

## Reporting an error

If you find a wrong author, wrong year, or broken link: open an issue (or just a PR with the fix) — citation accuracy is the whole point of this list.
