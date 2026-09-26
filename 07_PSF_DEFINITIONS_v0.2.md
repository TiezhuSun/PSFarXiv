# PSF v0.2 — Canonical Operational Definitions

**Authority:** source-derived from `PSF_Coder_Manual_Blind_v0.2.docx`.  
**Status:** frozen pilot ontology. Do not revise these definitions inside the arXiv v1 analysis. Prospective clarifications belong to PSF v0.3.

## Core diagnostic graph

Intended/authorized objective → objective/role representation → situated recognition → action selection/execution → behavior under altered oversight → continue/defer/stop decision → third-party/system effects → outcome/feedback.

This is a **diagnostic graph**, not a literal chronological law. X and Y can modify any node.

| Code | Working label | Operational diagnostic question | Key evidence boundary |
|---|---|---|---|
| A | Objective & Role Representation (正名-inspired) | Is the operative objective, role, authorization boundary, or task representation aligned with the intended/authorized one? | Requires evidence of intended vs operative objective/role; generic bad action is not enough. |
| B | Situated Recognition (知) | Does the agent demonstrably identify the relevant risk, constraint, uncertainty, provenance distinction, or authorization state? | Unsafe action alone does **not** establish B. |
| C | Enactment Consistency (知行合一-inspired) | When relevant safe conduct is demonstrably recognized, does that recognition govern action? | Requires positive recognition evidence before/during the focal unsafe action. If absent, C=U. |
| D | Oversight Invariance (慎独-inspired) | Does safety-relevant behavior remain stable as perceived monitoring, evaluation, training, logging, auditability, or observation changes? | Requires a credible oversight contrast; generic deception is insufficient. |
| E | Adaptive Restraint (知止 / 无为-inspired) | Does the agent appropriately continue, defer, abstain, or stop when risk, uncertainty, authorization, interruption, or environment state changes? | Requires a meaningful runtime continue/defer/stop transition. |
| F | Relational / System Effects (兼爱 / 恕-inspired) | Can locally successful/aligned behavior create unacceptable externalities, collusion, conflict, collective failure, or welfare loss? | Relational/system structure must be essential; ordinary harm alone is insufficient. |
| G | Outcome & Feedback | Does an apparently acceptable action/policy produce a distinct unsafe outcome, or is corrective feedback ignored? | Use only when outcome/feedback adds a distinct diagnosis; not merely because harm occurred. |
| U | Unknown / Insufficient Evidence | Can the focal core transition be identified from the supplied evidence? | U means insufficient evidence, not “no failure.” |

## Cross-cutting dimensions

| Code | Label | Definition |
|---|---|---|
| X | External Control (法 / 术 / 势 / 形名-inspired) | A technical/institutional control that should constrain the failure is absent, bypassed, misconfigured, or ineffective. |
| Y | Adversarial Context (兵家-inspired) | An attacker, malicious data source, strategic opponent, colluding agent, or adaptive adversary materially induces or shapes the failure. |

## Primary/secondary rule

1. Locate the **earliest evidence-supported** failed core transition.
2. Assign that transition as PRIMARY.
3. Add SECONDARY codes only if each independently meets the same minimum-evidence rule it would need as PRIMARY.
4. Record X/Y separately.
5. Record a **per-code** evidence tier and evidence span.
6. Do not infer latent beliefs, goals, or awareness from behavior alone.

## Evidence tiers

- **E3 Direct** — diagnostic link for the specific code is directly stated, paired, or experimentally manipulated.
- **E2 Strong indirect** — strongly supported but one inferential link remains.
- **E1 Contextual** — surrounding mechanism/context is supported but the focal core transition is not identified.
- **E0 None/insufficient** — no positive evidence for that code. PRIMARY=U has E0 by definition.

## Philosophical guardrail

The classical concepts are **design resources**, not historical equivalences. The paper must not claim that classical Chinese thinkers anticipated modern AI safety constructs.
