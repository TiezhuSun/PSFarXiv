# Work / Research QA Prompt

Use this after a first manuscript draft exists.

Goal: reviewer-style scientific and citation audit, not rewriting the paper from scratch.

1. Verify all current-framework claims against primary/current sources.
2. Check whether any 2025–2026 work weakens the novelty statement.
3. For each manuscript citation, verify that the cited source supports the exact sentence.
4. Flag unsupported historical claims about Chinese philosophy.
5. Search specifically for:
   - transition-based agent-safety taxonomies,
   - recognition→action safety benchmarks,
   - dynamic stopping/runtime restraint frameworks,
   - oversight invariance/evaluation-awareness frameworks,
   - agentic failure taxonomies with explicit conditional-transition structure.
6. Return a claim-by-claim audit with severity:
   - BLOCKING
   - SHOULD FIX
   - OPTIONAL
7. Do not strengthen the manuscript's claims.
