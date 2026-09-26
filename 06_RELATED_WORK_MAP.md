# Related-Work Map

**Cutoff for web verification:** 2026-09-25.

This file combines (A) source-derived framing from the prior SLR / Framework Gap Analysis and (B) a web-verified update of key neighboring frameworks as of the cutoff date. It is a manuscript map, not an exhaustive literature review.

## A. Governance and lifecycle frameworks

### NIST AI RMF 1.0 (2023)
- Voluntary, rights-preserving, use-case-agnostic risk-management framework.
- Important correction to novelty: NIST already treats AI risk management as an ongoing organizational process.
- PSF contrast: NIST organizes risk-management functions and organizational practice; PSF asks where an observed safety translation fails in a bounded case.
- URL: https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-ai-rmf-10

### ISO/IEC 23894:2023
- Guidance for integrating AI-specific risk management into organizational activities.
- PSF contrast: organizational/lifecycle risk-management guidance versus case-level diagnostic transition coding.
- URL: https://www.iso.org/standard/77304.html

### OpenAI Preparedness Framework (updated 2025)
- Severe-harm capability tracking, safeguards reports, and deployment decision processes.
- PSF contrast: capability/safeguard governance versus post hoc/prospective diagnosis of the transition at which safety breaks.
- URL: https://openai.com/index/updating-our-preparedness-framework/

### Google DeepMind Frontier Safety Framework
- Current public framing (third iteration, updated 2026) emphasizes capability thresholds, detection, security, and mitigation protocols.
- PSF contrast: frontier capability governance versus process-location diagnosis.
- URL: https://deepmind.google/blog/strengthening-our-frontier-safety-framework/

### Anthropic Responsible Scaling Policy
- Current public page lists RSP v3.4 as effective July 8, 2026 and emphasizes risk reports, safeguards, and frontier safety roadmaps.
- PSF contrast: organizational commitments / risk governance versus case-level transition diagnosis.
- URL: https://www.anthropic.com/responsible-scaling-policy

## B. Risk taxonomies and agentic frameworks

### MIT AI Risk Repository
- Meta-review/database plus Domain and Causal taxonomies; current published version organizes risks by domains and causal factors such as entity, intent, and timing.
- Important correction: existing taxonomies are not simply “flat.”
- PSF contrast: PSF's unit is not risk domain or broad causal factor but the conditional transition from objective representation through recognition/action/oversight/restraint/system effects.
- URL: https://airisk.mit.edu/risks
- Paper DOI: https://doi.org/10.1016/j.patter.2026.101517

### Microsoft Taxonomy of Failure Modes in Agentic AI Systems v2.0 (2026)
- Agentic failure modes organized along novel/existing and safety/security axes.
- PSF contrast: failure-mode vocabulary versus a process-location coding graph.
- URL: https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/bade/documents/products-and-services/en-us/security/Taxonomy-of-Failure-Modes-in-Agentic-AI-Systems-v2-0.pdf

### GovTech Singapore Agentic Risk & Capability (ARC) Framework (2026)
- Capability-centric governance framework linking system components/design/capabilities to materialized risks and technical controls.
- PSF contrast: ARC asks where risk arises in agent elements/capabilities and what controls mitigate it; PSF asks at which safety translation transition the observed case ceases to satisfy the intended objective.
- URL: https://govtech-responsibleai.github.io/agentic-risk-capability-framework/

### Valenta, Rozinek & Horálek (2026), structured review
- Eight problem families spanning goal specification, inner alignment, safe learning/robustness, scalable oversight, interpretability, tool-use security, multi-agent safety, and evaluation/assurance; explicitly mapped to EU AI Act/NIST.
- Important correction: recent agentic-safety reviews already use layered/interactive structures.
- PSF contrast: problem-family research taxonomy versus evidence-grounded failure-location coding.
- DOI: https://doi.org/10.3390/ai7080298

## C. Adjacent empirical constructs

### Objective/specification / goal failures — PSF A
- AI Safety Gridworlds: specification problems, reward gaming, interruptibility, distribution shift.
- Sycophancy to Subterfuge: specification gaming can generalize to reward tampering.
- CoastRunners: classic misspecified reward example.
- These literatures predate PSF; the novelty claim is not the existence of specification failure.

### Situated recognition / knowledge–behavior — PSF B/C
- R-Judge operationalizes safety-risk awareness for LLM agents.
- CulShield (ACL 2026) explicitly reports a “knowledge–behavior gap” in cultural taboo safety.
- Therefore do **not** claim that PSF discovers the generic knowledge–behavior gap.
- PSF-specific angle: separate demonstrated recognition from enactment in situated agent trajectories, with C requiring positive recognition evidence.

### Evaluation awareness / alignment faking — PSF D
- Alignment Faking in Large Language Models (2024).
- Large Language Models Often Know When They Are Being Evaluated (2025).
- The Hawthorne Effect in Reasoning Models (NeurIPS 2025).
- Deployment Simulation (2026) explicitly studies evaluation awareness under more production-like replay.
- Therefore D must be framed as an operational mapping/diagnostic node, not a newly discovered phenomenon.

### Restraint / abstention — PSF E
- AgentAbstain (2026) is a systematic paired-task benchmark with 263 task pairs across 42 sandbox environments and explicitly studies post-hoc abstention after irreversible actions.
- Therefore do not claim first “knowing when not to act.”
- PSF E's narrower potential contribution: dynamic runtime continuation / stopping-time diagnosis under changed conditions, including shutdown/interrupt and irreversible-before-check cases.

### Prompt injection / tool security — PSF Y and often X; core may be U
- InjecAgent demonstrates indirect prompt injection in tool-integrated agents.
- AgentDojo and later agent-security benchmarks similarly establish attack surfaces.
- PSF contribution is not a new prompt-injection category; it is the rule that adversarial context (Y) does not itself identify the agent-side A/B/C core transition.

### Multi-agent/systemic effects — PSF F
- Algorithmic pricing/collusion, multi-agent escalation, commons collapse, and welfare allocation already provide established systemic-risk examples.
- PSF F operationalizes when relational/system structure is essential to the diagnosis rather than treating “someone was harmed” as sufficient.

## D. Novelty statement to use

> Existing frameworks already capture risk domains, lifecycle processes, frontier capabilities, agentic failure modes, controls, adversarial threats, and multi-agent hazards. PSF instead tests a complementary diagnostic unit: the earliest evidence-supported transition at which an intended or authorized objective ceases to yield safe situated behavior and consequences.

## E. Novelty statements to avoid

- “PSF is the first process-based AI safety framework.”
- “Existing taxonomies are flat.”
- “No framework links failures to mitigations.”
- “慎独 uniquely predicts alignment faking.”
- “知行合一 reveals the knowledge–behavior gap for the first time.”
- “知止 introduces agent abstention.”
