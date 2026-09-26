# Results Specification

Recommended ordering:

## 5.1 Data completeness and recovery
179 strict VALID, 1 bounded INVALID, 0 residual truncation.
Keep technical recovery concise in main text; details in appendix.

## 5.2 Overall PRIMARY reliability
Main numbers:
- GPT pooled within 86.7%, κ=.838.
- Opus pooled within 95.5%, κ=.943.
- same-run cross-model 88.8%, κ=.862.
- case consensus 93.3%, κ=.918.
- descriptive six-run α=.874.

## 5.3 Localized disagreement structure
Ten same-run disagreements; two stable consensus disagreements:
P12 C vs U; P16 G vs U.

## 5.4 Per-code
A .927; C .667; D .941; E .960; F 1.000; G .400; U .833; B not observed.

## 5.5 Strata
Highlight:
- Multi-agent/Systemic 100%.
- Prompt Injection/Tool Security 73.3%.
Interpret carefully as descriptive.

## 5.6 Evidence/auxiliary layers
- same-PRIMARY evidence tier 86.1%; all residual disagreements E2↔E3.
- SECONDARY 87.6%.
- X/Y 82.0%; X weaker than Y.
- confidence only 53.9% exact → not a cross-model endpoint.

## 5.7 Mitigation differentiation
Report exploratory TF-IDF similarity and p<.001 with noncausal caveat.
