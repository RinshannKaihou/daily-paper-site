# Research Interests Configuration

Configure your research interests to personalize daily paper recommendations.
Edit this file to match your focus areas.

---

## Primary Areas

Describe your research interests in natural language. The more descriptive, the better the semantic filtering works.

```areas
Self-Evolving Agents & Automated Research — HIGH PRIORITY, ranked above all other areas: self-improving and self-evolving LLM agents, autonomous research loops, agentic scientific discovery, automated hypothesis generation and experimentation, self-modifying agent architectures, open-ended self-improvement, AI scientists / AI researchers, automated benchmark and reward design, and the reliability and trustworthiness of long-running autonomous agent systems. When a paper partially overlaps this area and another, assign it here.
LLM Training Stability & Observability — monitoring training runs, detecting anomalies, loss spikes, training instability, gradient issues, divergence, checkpoint reliability, fault detection and robustness of distributed training at scale.
Inference Reliability & SDC Detection — CORE PROGRAM: detection and mitigation of silent data corruption and hardware-induced faults in ML training and inference (bit-flip errors, DRAM/memory errors, accelerator fault detection), and infrastructure-caused corruption of model outputs. Model-side issues (hallucination, alignment, safety) are explicitly OUT of scope.
Reliability under Extreme Performance Optimization — precision and correctness problems introduced by aggressive optimization of training and inference: quantization errors, low-precision and mixed-precision computation, floating-point precision, numerical stability, catastrophic cancellation, hardware-level arithmetic errors. Pure speed/memory/cost wins WITHOUT a reliability or precision angle are NOT relevant.
LLM Hidden States & Interpretability — mechanistic interpretability, internal representations and hidden states of LLMs, probing, SAEs, circuits, representation geometry, latent structure analysis.
Compute Infrastructure for Large-Scale ML — operators and kernels, communication and interconnect (collectives, allreduce, RDMA), cluster scheduling and management, hardware and node failures and their detection (failed or degraded accelerators, 掉卡), slow nodes and stragglers — on ANY hardware platform.
Model System Cards & Technical Reports — official system cards, technical reports, and safety evaluations from major AI companies (OpenAI, Anthropic, Google DeepMind, Meta, Mistral, Qwen, etc.).
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
max_papers: 100
```

---

## Notes

- The `areas` section is read by an LLM for semantic filtering — write it in natural language, be descriptive
- The `categories` section controls which arxiv categories to fetch from — keep broad to not miss papers
- Weekly mode (default): papers are fetched once per week (Mon..Sun), pre-filtered by title, then rated on abstracts; `max_papers` caps the WEEKLY selection (aim 50-100 — fewer is fine when quality drops off, the cap is a hard bound)
- Daily mode (legacy): `max_papers` caps the per-day selection
