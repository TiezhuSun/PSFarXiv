# Citation Audit and Remaining Bibliography Work

## Status legend

- **VERIFIED** — primary/current source checked during source-pack construction.
- **SOURCE-DERIVED** — retained from prior SLR/framework-gap artifact; not re-verified here.
- **CASE-INDEX** — authoritative case source URL/locator comes from the frozen Master Audit.
- **TODO-METADATA** — URL is authoritative but final BibTeX should be normalized before submission.

## High-priority related-work anchors

| Work | Status | Manuscript role |
|---|---|---|
| NIST AI RMF 1.0 | VERIFIED | governance/lifecycle baseline |
| ISO/IEC 23894:2023 | VERIFIED | AI risk-management baseline |
| OpenAI Preparedness Framework (2025) | VERIFIED | frontier capability/safeguard governance |
| Google DeepMind Frontier Safety Framework, third iteration / 2026 update | VERIFIED | frontier safety framework |
| Anthropic Responsible Scaling Policy v3.4 (2026 current page) | VERIFIED | frontier governance / safeguards |
| AI Risk Repository, Patterns 2026 | VERIFIED | risk-domain and causal-taxonomy baseline |
| Microsoft Agentic Failure Modes v2.0 | VERIFIED | agentic failure-mode baseline |
| GovTech Singapore ARC Framework | VERIFIED | capability/risk/control agentic framework |
| Valenta et al. 2026 structured review | VERIFIED | eight-family agentic-safety review |
| AgentAbstain | VERIFIED | restraint/abstention novelty correction |
| CulShield | VERIFIED | knowledge–behavior novelty correction |
| Alignment Faking | VERIFIED | D-adjacent work |
| Needham et al. evaluation awareness | VERIFIED | D-adjacent evaluation awareness |
| Hawthorne Effect | VERIFIED | causal steering of test awareness |
| InjecAgent | VERIFIED | Y/X prompt-injection adjacent work |

## Case bibliography

`data/case_source_index.csv` is the authoritative 30-case source list and includes:
- final case ID,
- candidate ID,
- stratum,
- neutral title,
- primary source,
- source URL,
- source locator,
- QA adjustment.

Before arXiv submission, normalize every row into BibTeX. Do **not** replace case-source URLs with secondary summaries.

## Philosophy bibliography gap

The current seed bibliography contains modern Chinese-philosophy/AI sources from the prior SLR, but the final paper should add authoritative primary/secondary citations for:
- 正名,
- 慎独,
- 知行合一,
- 知止 / 无为,
- 兼爱 / 恕,
- 法 / 术 / 势 / 形名,
- 兵家.

Do not let Codex invent historical quotations or translations. Use a dedicated citation-verification pass (preferably Work/web or a human philosophy review) before finalizing these passages.

## Citation hygiene

- Prefer primary papers, official standards/framework pages, or publisher proceedings.
- Avoid citing a vendor blog when the underlying paper is available, except when the blog itself is the primary source (e.g., CoastRunners historical example).
- Any “current version” claim must include a dated source or access date.
- Do not cite a 2024 preprint as if it were the final 2026 published version when a version of record exists.
