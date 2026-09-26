# Frozen Methods Protocol

This file describes the experiment that the arXiv v1 must report. It should not be retroactively redesigned.

## 1. Ontology freeze

Pilot framework: **PSF v0.2**.

The codebook was frozen before the 30-case formal coding phase. Post-pilot observations about B, G, and X are prospective **v0.3 revision targets**, not changes to the evaluated v0.2 ontology.

## 2. Corpus construction

### Strata

Six strata, five final cases each:

- S1 Objective / Generalization
- S2 Harmful Tool-use / Agentic Misalignment
- S3 Evaluation Awareness / Strategic Compliance
- S4 Prompt Injection / Tool Security
- S5 Restraint / Abstention / Corrigibility
- S6 Multi-agent / Systemic Effects

### Candidate pool and anti-cherry-picking

- 60 total audited candidates.
- 30 final selected cases.
- Selection criteria were source quality, public verifiability, case-level detail, reproducibility, and within-stratum source/mechanism diversity.
- **Expected PSF label was not a selection criterion.**
- Selection was completed before the formal coding results were observed.
- CoinRun was removed because it overlapped with the calibration set; the pre-audited CoastRunners reserve was substituted before 30-case coding. No coding result motivated this swap.

### Blind packet

Final blind case records contain:
- Agent/system
- Objective/task
- Environment/setup
- Constraints/boundary
- Behavioral evidence
- Context/interaction
- Oversight information
- Stop/defer opportunity
- Affected parties/system
- Observed outcome

Source identity, stratum labels, and selection rationale were hidden from coders.

### Randomization

Final IDs P01–P30 were assigned using the frozen seed:

`PSF-PILOT-2026-09-17-FINAL-V1`

The merge used block-balanced randomization: five blocks × six cases, one case from each stratum per block.

## 3. Coder systems

- GPT-5.6 Sol
- Claude Opus 5

Each system completed three replicate runs.

### Execution unit

**One case = one fresh isolated API call.**

Each request contained only:
1. frozen PSF Coder Manual v0.2,
2. one blind case,
3. frozen v1.1 coding instructions/schema.

No model saw another case in the same context. No web/search/source-paper lookup was allowed.

### Sampling / reasoning

- Reasoning effort: `high`
- Structured JSON output schema
- Three runs used different operational presentation orders, but the case-level prompt for a given case was held constant across runs.
- Repeated runs are stability/sensitivity probes, **not independent human-style coders**.

## 4. Output schema

For every case:
- exactly one PRIMARY A–G or U;
- optional independently supported SECONDARY core codes;
- X/Y recorded cross-cutting;
- per-code evidence tier and verbatim evidence span;
- rationale;
- evidence that would change coding;
- mitigation family;
- model-native confidence.

## 5. Technical-recovery rule

Initial output ceiling: 3,000 tokens.

- 26/180 observations were mechanically truncated at exactly 3,000 tokens.
- Only those 26 technical missing observations were rerun, with every substantive input frozen and the ceiling raised to 6,000.
- 22/26 became VALID.
- Four Opus observations again truncated at 6,000.
- Only those four were given a second and final recovery at 12,000.
- All four became VALID.
- Recovery stopped permanently.

All original 3k, 6k, and 12k records were preserved separately.

This is an instrumentation correction, not outcome-driven rerunning.

## 6. One bounded schema-invalid record

Opus P01/run2 returned a duplicate X entry. Its PRIMARY=A and primary tier=E2 are intact.

- Strict full-record analysis: exclude the record.
- PRIMARY-only sensitivity: include its PRIMARY judgment.
- Do not silently rewrite or deduplicate the original record.

## 7. Reliability metrics

Primary:
- exact agreement,
- Cohen’s κ for pairwise nominal agreement,
- nominal Krippendorff’s α across replicate runs,
- case-level modal consensus,
- per-code Dice/F1.

Secondary:
- evidence-tier exact agreement and ordinal distance,
- SECONDARY exact/Jaccard,
- X/Y exact/Jaccard and consensus presence agreement,
- evidence-span overlap,
- confidence agreement (descriptive only).

### Statistical interpretation

Pooled run-pairs share underlying cases and are therefore descriptive repeated-measure summaries, not independent samples.

Case-level consensus is the unique modal PRIMARY among at least two usable runs per model.

## 8. Mitigation differentiation

Exploratory text analysis compares mitigation-family text similarity within versus across model-assigned PRIMARY diagnoses.

Interpretation must remain descriptive because diagnosis and mitigation text are generated in the same response.

## 9. Reporting hierarchy

Main paper:
1. strict full-record analysis;
2. bounded PRIMARY-only sensitivity for Opus P01;
3. technical-recovery procedure in Methods/Limitations.

Do not report only the sensitivity result.
