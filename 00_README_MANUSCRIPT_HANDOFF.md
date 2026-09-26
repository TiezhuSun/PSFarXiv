# PSF arXiv v1 Source Pack

This package is the canonical handoff from the research-design / analysis conversation to a LaTeX/Overleaf implementation workflow.

## Authority hierarchy

When files conflict, use this order:

1. `02_CLAIM_EVIDENCE_MATRIX.md`
2. `04_RESULTS_FROZEN_NUMBERS.json`
3. `03_METHODS_FROZEN_PROTOCOL.md`
4. `07_PSF_DEFINITIONS_v0.2.md`
5. `05_LIMITATIONS_AND_NONCLAIMS.md`
6. Final analysis report/workbook in `source_documents/`
7. Prior SLR / framework-gap documents
8. Related-work seed materials

Do not “improve” a claim by making it stronger than the higher-priority file permits.

## What is frozen

- PSF v0.2 ontology evaluated in the pilot
- 30-case corpus membership and P01–P30 mapping
- three-run × two-model isolated-call design
- strict vs PRIMARY-only sensitivity treatment of Opus P01/run2
- all final numerical results in `04_RESULTS_FROZEN_NUMBERS.json`
- technical-recovery audit trail

## What remains open for manuscript drafting

- exact title
- narrative ordering
- amount of Chinese-philosophy historical detail in the main text vs appendix
- target venue-specific formatting
- final bibliography normalization
- figure/table aesthetics
- prospective PSF v0.3 discussion

## Important rule for Codex / Work

Do not revise PSF v0.2 definitions in the manuscript to eliminate pilot disagreements. Any proposed B/G/X clarifications must be labeled prospective **PSF v0.3** changes.

## Directory guide

- `00_README_MANUSCRIPT_HANDOFF.md` — this file.
- `01_PAPER_SPEC.md` — recommended paper positioning.
- `02_CLAIM_EVIDENCE_MATRIX.md` — allowed and prohibited claims.
- `03_METHODS_FROZEN_PROTOCOL.md` — exact study design.
- `04_RESULTS_FROZEN_NUMBERS.json` — canonical numerical source.
- `05_LIMITATIONS_AND_NONCLAIMS.md` — required limitations.
- `06_RELATED_WORK_MAP.md` — novelty baseline and neighboring work.
- `07_PSF_DEFINITIONS_v0.2.md` — frozen ontology.
- `08_WRITING_TERMINOLOGY_GUARDRAILS.md` — wording discipline.
- `data/` — final observation, corpus, case-source, and consensus data.
- `tables/` — manuscript-ready CSV tables.
- `figures/` — final analysis figures.
- `references/` — seed BibTeX and citation audit.
- `manuscript_blueprint/` — section-by-section writing specification.
- `source_documents/` — canonical research artifacts.
- `reproducibility/` — prompts, schemas, run manifests, raw result archives.
- `overleaf_starter/` — compile-oriented skeleton for Codex to expand.

## Recommended next workflow

1. Put this folder under Git.
2. Open the repository in VS Code / Codex.
3. Give Codex `CODEX_HANDOFF_PROMPT.md`.
4. Instruct it to treat the claim matrix and frozen-results JSON as immutable.
5. Build and compile the Overleaf project iteratively.
6. Use Work/current-chat web research only for citation freshness and reviewer-style scientific QA.
