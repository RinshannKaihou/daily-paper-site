# Research Interests Configuration

Configure your research interests to personalize daily paper recommendations.
Edit this file to match your focus areas.

---

## Primary Areas

Describe your research interests in natural language. The more descriptive, the better the semantic filtering works.

```areas
LLM Training Stability & Observability — monitoring training runs, detecting anomalies, loss spikes, training instability, gradient issues, checkpoint reliability, distributed training robustness
LLM Inference Evaluation — benchmarking inference quality, output consistency, reproducibility of inference results, evaluating model outputs (NOT hallucination detection)
LLM Hidden States & Interpretability — mechanistic interpretability, representation geometry, information encoding in hidden states, probing, SAEs, circuits, representational similarity, latent structure analysis
Computation Reliability & Precision Errors — quantization errors, floating-point precision, numerical stability, catastrophic cancellation, mixed-precision training issues, hardware-level arithmetic errors
Model System Cards & Technical Reports — official system cards, technical reports, and safety evaluations from top-tier AI companies (OpenAI, Anthropic, Google DeepMind, Meta, Mistral, etc.)
Silent Data Corruption (SDC) — detection and mitigation of silent data corruption in ML training and inference hardware, bit-flip errors, DRAM errors, GPU fault detection
ML Reliability & Mathematical Foundations — general reliability, robustness, and mathematical analysis of ML/LLM/CV systems, formal guarantees, statistical bounds, failure mode analysis
Self-Evolving Agents & Automated Research — self-improving and self-evolving LLM agents, autonomous research loops, agentic scientific discovery, automated hypothesis generation and experimentation, self-modifying agent architectures, open-ended self-improvement, AI scientists / AI researchers, automated benchmark and reward design, recursive agent optimization
```

## Arxiv Categories

Categories to fetch all recent papers from (semantic filtering will pick the relevant ones).

```categories
cs.LG
cs.CL
cs.AI
cs.CV
cs.PF
cs.AR
stat.ML
```

## Settings

```settings
max_papers: 50
```

---

## Notes

- The `areas` section is read by an LLM for semantic filtering — write in natural language, be descriptive
- The `categories` section controls which arxiv categories to fetch from — keep broad to not miss papers
- Papers are fetched broadly from these categories, then an LLM ranks them by relevance to your areas
- Adjust max_papers to control how many papers to summarize each day
