---
title: "Daily Paper Overview — 2026-04-10"
date: 2026-04-10
tags:
  - daily-overview
  - paper-digest
papers: 11
---

# Daily Paper Overview — 2026-04-10

## Quick Stats

| Metric | Value |
|--------|-------|
| Papers reviewed | 11 |
| Categories | cs.CL, cs.LG, cs.AI, cs.CV, cs.CC, stat.ML, eess.SY |
| Time range | 2026-04-08 |
| Total fetched | 18 |
| Filtered in | 11 |

## Must Read Today

> Top picks based on relevance to your interests.

| Paper | Why |
|-------|-----|
| [[2604.07343]] Personalized RewardBench | SOTA reward models only 75.94% on personalization; NDCG 0.92 correlation with downstream BoN/PPO — directly evaluates LLM inference quality |
| [[2604.07328]] How to sketch a learning algorithm | Provably accurate data deletion via forward-mode AD sketches — novel connection between training stability and interpretability |
| [[2604.07306]] Beyond Loss Values | Loss trajectory analysis (DAS) replaces per-sample loss ranking for robust pruning under noise — CVPR 2026 Findings, directly about training reliability |

---

## Papers by Topic

### LLM Inference Evaluation

| Paper | TL;DR | Tags |
|-------|-------|------|
| [[2604.07343]] Personalized RewardBench | Personalized RewardBench reveals SOTA reward models peak at 75.94% on personalization, with 0.92 NDCG correlation to downstream BoN/PPO performance | `reward-models` `llm-evaluation` `personalization` |
| [[2604.07321]] Syntax Is Easy, Semantics Is Hard | LLMs produce syntactically valid LTL but only ~24% semantic equivalence; Python AST reformulation boosts to 61%+ | `llm-evaluation` `formal-logic` `inference-quality` |
| [[2604.07320]] Evaluating In-Context Translation with Synchronous C... | LLM in-context translation accuracy degrades sharply with grammar size; BLEU/chrF++ overestimate true quality by ~2x | `llm-evaluation` `in-context-learning` `formal-grammar` |

### Training Stability & Observability

| Paper | TL;DR | Tags |
|-------|-------|------|
| [[2604.07306]] Beyond Loss Values | AlignPrune uses Dynamic Alignment Score (loss trajectory Pearson correlation) to replace loss-value ranking for robust pruning under noisy labels | `data-pruning` `loss-trajectory` `training-reliability` |
| [[2604.07350]] Fast Spatial Memory with Elastic Test-Time Training | Elastic TTT applies Fisher-weighted EWC-inspired priors to stabilize fast-weight updates against catastrophic forgetting in multi-chunk test-time training | `test-time-training` `catastrophic-forgetting` `elastic-weight-consolidation` |
| [[2604.07345]] Measurement of Generative AI Workload Power Profiles... | Public 0.1s-resolution H100 power profiles for AI training/inference + DIPLOEE facility-level energy simulation framework | `power-profiling` `training-observability` `data-center` |
| [[2604.07316]] SL-FAC | DCT-based frequency decomposition + adaptive quantization for split learning communication compression | `split-learning` `quantization` `distributed-training` |

### ML Mathematical Foundations

| Paper | TL;DR | Tags |
|-------|-------|------|
| [[2604.07328]] How to sketch a learning algorithm | Data deletion via Taylor expansion sketches using forward-mode AD, poly(1/epsilon) overhead under stability assumption | `interpretability` `data-deletion` `training-stability` |
| [[2604.07349]] Toward a Tractability Frontier for Exact Relevance C... | Meta-impossibility theorem: no closure-invariant structural predicate can exactly characterize the tractability frontier for relevance certification | `formal-guarantees` `impossibility-theorem` `relevance-certification` |
| [[2604.07325]] Conformal Prediction with Time-Series Data via Seque... | SCDR: doubly robust conformal prediction for time series with asymptotic conditional coverage guarantees | `conformal-prediction` `statistical-guarantees` `time-series` |
| [[2604.07323]] Gaussian Approximation for Asynchronous Q-learning | High-dimensional CLT for async Q-learning Polyak-Ruppert averages at rate n^{-1/6} log^4(nSA) | `convergence-theory` `q-learning` `mathematical-foundations` |

---

## All Papers

| # | Paper | Authors | Key Topic | TL;DR |
|---|-------|---------|-----------|-------|
| 1 | [[2604.07343]] Personalized RewardBench | Qiyao Ma et al. | Reward Model Eval | Personalized RewardBench reveals SOTA reward models peak at 75.94% on personalization, with 0.92 NDCG correlation to downstream BoN/PPO performance |
| 2 | [[2604.07328]] How to sketch a learning algorithm | Sam Gunn | Data Deletion | Data deletion via Taylor expansion sketches using forward-mode AD, poly(1/epsilon) overhead under stability assumption |
| 3 | [[2604.07306]] Beyond Loss Values | Huaiyuan Qin et al. | Loss Trajectory | AlignPrune uses Dynamic Alignment Score (loss trajectory Pearson correlation) to replace loss-value ranking for robust pruning under noisy labels |
| 4 | [[2604.07350]] Fast Spatial Memory with Elastic Test-Time Training | Ziqiao Ma et al. | Test-Time Training | Elastic TTT applies Fisher-weighted EWC-inspired priors to stabilize fast-weight updates against catastrophic forgetting in multi-chunk test-time training |
| 5 | [[2604.07349]] Toward a Tractability Frontier for Exact Relevance C... | Tristan Simas | Formal Guarantees | Meta-impossibility theorem: no closure-invariant structural predicate can exactly characterize the tractability frontier for relevance certification |
| 6 | [[2604.07345]] Measurement of Generative AI Workload Power Profiles... | Roberto Vercellino et al. | Power Profiling | Public 0.1s-resolution H100 power profiles for AI training/inference + DIPLOEE facility-level energy simulation framework |
| 7 | [[2604.07325]] Conformal Prediction with Time-Series Data via Seque... | M. Sampson & K.S. Chan | Conformal Prediction | SCDR: doubly robust conformal prediction for time series with asymptotic conditional coverage guarantees |
| 8 | [[2604.07323]] Gaussian Approximation for Asynchronous Q-learning | Artemy Rubtsov et al. | Convergence Theory | High-dimensional CLT for async Q-learning Polyak-Ruppert averages at rate n^{-1/6} log^4(nSA) |
| 9 | [[2604.07321]] Syntax Is Easy, Semantics Is Hard | Priscilla Kyei Danso et al. | LLM Eval | LLMs produce syntactically valid LTL but only ~24% semantic equivalence; Python AST reformulation boosts to 61%+ |
| 10 | [[2604.07320]] Evaluating In-Context Translation with Synchronous C... | Jackson Petty et al. | LLM Eval | LLM in-context translation accuracy degrades sharply with grammar size; BLEU/chrF++ overestimate true quality by ~2x |
| 11 | [[2604.07316]] SL-FAC | Zehang Lin et al. | Split Learning | DCT-based frequency decomposition + adaptive quantization for split learning communication compression |

---
*Overview generated on 2026-04-10*