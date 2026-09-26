# Codex Handoff Prompt

You are building an Overleaf-compatible arXiv manuscript from a frozen research source pack.

## Non-negotiable authority

Read these files first and treat them as immutable scientific constraints:
1. `02_CLAIM_EVIDENCE_MATRIX.md`
2. `04_RESULTS_FROZEN_NUMBERS.json`
3. `03_METHODS_FROZEN_PROTOCOL.md`
4. `07_PSF_DEFINITIONS_v0.2.md`
5. `05_LIMITATIONS_AND_NONCLAIMS.md`

Do not strengthen claims beyond the matrix. Do not change numerical results. Do not revise PSF v0.2 definitions to remove disagreements.

## Task

Build a professional, compile-clean, Overleaf-compatible LaTeX project for an arXiv v1 paper provisionally titled:

**From Objective to Outcome: A Process Safety Framework for Diagnosing Safety Failures in Agentic AI**

Use `manuscript_blueprint/` for section content and ordering. Use the CSV tables and figures already supplied. Use `references/references_seed.bib` as a seed, not as permission to invent missing metadata.

## Scientific rules

- “demonstrated recognition,” not “the model knew,” unless operationally defined.
- repeated runs are stability probes, not independent coders.
- corpus is purposive, not a prevalence sample.
- B is untested.
- G and X are revision targets.
- mitigation differentiation is exploratory/descriptive, not causal.
- philosophy is a design resource, not historical equivalence.
- technical recovery was triggered only by token censoring.

## Engineering rules

- Use modular `sections/*.tex`.
- Put manuscript tables under `tables/`.
- Put figures under `figures/`.
- Centralize commands/macros in the preamble.
- Use stable citation keys.
- Run `latexmk` until there are no fatal errors, undefined references, or undefined citations.
- Report unresolved overfull boxes rather than hiding them.
- Keep a `CHANGELOG.md`.
- Preserve a clear separation between main paper and appendices.
- Do not delete raw source-pack materials.

## Citation rule

For any assertion not supported by the frozen source pack, mark it `TODO-CITATION-VERIFY` instead of inventing a citation.
