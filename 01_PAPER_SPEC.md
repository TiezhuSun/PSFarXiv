# Paper Specification — arXiv v1

## Recommended title

**From Objective to Outcome: A Process Safety Framework for Diagnosing Safety Failures in Agentic AI**

### Alternative titles

1. **Process Safety for Agentic AI: Diagnosing Where Safety Breaks from Objective to Outcome**
2. **A Process Safety Framework for Agentic AI: Operationalizing Classical Chinese Philosophical Resources**
3. **Diagnosing Safety Transitions in Agentic AI: The Process Safety Framework**

The recommended title foregrounds the technical contribution and keeps the philosophical provenance visible in the body rather than making the title sound like a metaphor paper.

## Paper type

Framework + operationalization + blinded pilot evaluation.

## Central proposition

> AI safety failures in agentic systems can be diagnostically decomposed not only by risk domain or threat source, but by conditional failures in the translation of intended objectives into situated behavior and consequences. Distinguishing objective/role representation, situated recognition, enactment consistency, oversight invariance, adaptive restraint, and relational/system effects yields different evaluation targets and mitigation strategies.

The empirical burden is **diagnostic reliability and actionability**, not ingredient novelty.

## Recommended contribution statement

The manuscript should claim four contributions:

1. **Process-oriented unit of analysis.** PSF locates *where safety ceases to hold* in the translation from intended/authorized objectives to situated behavior and consequences.
2. **Operational codebook.** PSF v0.2 defines seven core nodes (A–G), two cross-cutting dimensions (X/Y), U for insufficient evidence, and per-code evidence tiers.
3. **Blinded pilot corpus and reproducibility protocol.** A stratified 30-case corpus was selected from 60 candidates before coding; two frontier-model coder systems each completed three isolated runs.
4. **Initial empirical evaluation.** The pilot shows strong reproducibility for several nodes, localized construct-boundary disagreements, and diagnosis-specific mitigation families.

## What the paper is NOT

- Not a claim that “safety as process” is new.
- Not a claim that existing AI-risk taxonomies are flat.
- Not the first specification, monitoring, prompt-injection, multi-agent, or control framework.
- Not the discovery of the knowledge–behavior gap.
- Not the first abstention / “knowing when not to act” benchmark.
- Not human-expert validation.
- Not a prevalence study.
- Not proof that Chinese philosophical doctrines are historically equivalent to modern AI-safety constructs.

## Target readers

AI safety / alignment researchers; agent-safety benchmark researchers; AI security researchers; risk-taxonomy and governance researchers; technically oriented AI ethics researchers.

## Main empirical story

The strongest story is **not** “all categories work.” It is:

- A, D, E, and F form a reproducible diagnostic spine.
- C has a positive empirical footprint but an evidence-threshold boundary with U.
- B is under-sampled / untested.
- G exposes a specific unresolved standalone-primary criterion.
- X is less stable than Y and needs a sharper minimum-evidence rule.
- The disagreements are localized rather than diffuse.
- Mitigation recommendations cluster by diagnosis, supporting exploratory actionability.

## Recommended main figures

1. Final PRIMARY agreement summary.
2. Cross-model PRIMARY confusion matrix.
3. Per-code Dice/F1.
4. Stratum-level descriptive agreement.

## Recommended main tables

1. PSF construct table (A–G, X/Y, evidence boundary, mitigation family).
2. Main reliability table.
3. Per-code and stratum summary.
4. Stable disagreement / falsification targets.
5. Optional: diagnosis → mitigation families.

## ArXiv-v1 positioning

Use phrases such as:
- “initial evidence”
- “blind pilot evaluation”
- “reproducible diagnostic spine”
- “localized construct-boundary disagreement”
- “exploratory actionability evidence”

Avoid:
- “validated taxonomy”
- “proves”
- “first process framework”
- “first knowledge–action gap”
- “human-level reliability”
