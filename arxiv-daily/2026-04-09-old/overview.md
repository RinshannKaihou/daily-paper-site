---
title: "Daily Paper Overview — 2026-04-09"
date: 2026-04-09
tags:
  - daily-overview
  - paper-digest
papers: 34
---

# Daily Paper Overview — 2026-04-09

## Quick Stats

| Metric | Value |
|--------|-------|
| Papers reviewed | 34 |
| Categories | cs.CL, cs.AI, cs.LG, cs.CV, cs.PF, cs.AR, stat.ML |
| Source papers scanned | 364 |
| Filter pass rate | 9.3% |
| Time range | 2026-04-09 |

## Must Read Today

> Top picks based on relevance to your interests (LLM training stability, interpretability, quantization, computation reliability).

| Paper | Why |
|-------|-----|
| [[2604.08527v1]] Demystifying OPD | Identifies truncation-collapse + length inflation as fundamental failure mode in on-policy distillation; proposes Stable-OPD fixing it |
| [[2604.08524v1]] Representation Steering | Mechanistic case study revealing steering vectors act via OV circuits, can be sparsified 90-99% with minimal loss |
| [[2604.08510v1]] Implicit Curriculum | Shows LLMs learn skills in compositional curriculum during pretraining, enabling trajectory prediction (R²=.68-.84) |
| [[2604.07955v1]] Residual Errors in Quantization | ICLR 2026 paper finding sub-optimal calibration in GPTQ/GPTAQ; fixes Llama2-7B perplexity from 13.60→8.34 |
| [[2604.08118v1]] Codebook Initialisation | Proves codebook init dominates optimization at 2-bit; OA-EM method achieves Pareto dominance |

---

## Papers by Topic

### LLM Training Stability & Dynamics

| Paper | Key Finding | Tags |
|-------|-------------|------|
| [[2604.08527v1]] Demystifying OPD | Repetition-saturation causes length inflation in on-policy distillation; Stable-OPD fixes it (+7.2% avg accuracy) | `training-stability` `distillation` |
| [[2604.07963v1]] Rethinking Data Mixing | Gradient-geometry based domain definition; DoGraph achieves 37.9% avg accuracy on GPT-2 with 4.5% overhead | `data-mixing` `training-dynamics` |
| [[2604.07941v1]] LLM Post-Training Survey | Unified framework for off-policy/on-policy learning via trajectory provenance lens (Huawei, 13 authors) | `post-training` `RLHF` `survey` |
| [[2604.08539v1]] OpenVLThinkerV2 | Gaussian GRPO via optimal transport for RL training stability; beats GPT-4o on MMMU (71.6%) | `RLVR` `training-stability` `multimodal` |

### Mechanistic Interpretability & Hidden States

| Paper | Key Finding | Tags |
|-------|-------------|------|
| [[2604.08524v1]] Representation Steering | Steering vectors act through OV circuits (>90% method overlap); 90-99% sparsification possible | `mechanistic-interpretability` `steering` |
| [[2604.08510v1]] Implicit Curriculum | Compositional skill emergence during pretraining; cross-model Spearman ρ=.81 | `pretraining-dynamics` `emergence` |
| [[2604.08039v1]] LINE | LLM-driven iterative neuron explanations for vision models; up to +0.18 AUC on CoSy | `neuron-interpretability` `vision` |
| [[2604.08284v1]] DMLE | Causal tracing reveals formulas/descriptions vs instances localize to different layers | `knowledge-editing` `mechanistic` |
| [[2604.08169v1]] Activation Steering | Projection-aware steering methods (StTP/StMP) for aligned generation; multi-turn evaluation | `activation-steering` `alignment` |
| [[2604.08271v1]] Illusion of Unlearning | Hidden features remain discriminative despite apparent unlearning (92.5% linear-probe accuracy) | `unlearning` `representations` |

### Quantization & Numerical Precision

| Paper | Key Finding | Tags |
|-------|-------------|------|
| [[2604.07955v1]] Residual Errors | Compensation-aware error r₂ in GPTQ/GPTAQ; Llama2-7B C4 PPL 13.60→8.34 (ICLR 2026) | `quantization` `LLM` |
| [[2604.08118v1]] Codebook Initialisation | Init dominates optimization at 2-bit; OA-EM achieves Pareto frontier (Sheffield) | `quantization` `vector-quantization` |
| [[2604.08474v1]] Quantization in FL | INT4 matches FP32 at 8x comm reduction; INT2 causes catastrophic score instability | `quantization` `federated-learning` |
| [[2604.07925v1]] Sinkhorn Attention Rank | Doubly exponential rank decay proof for Sinkhorn attention; empirically mitigates collapse vs Softmax | `attention` `rank-collapse` `theory` |

### Inference Reliability & Serving

| Paper | Key Finding | Tags |
|-------|-------------|------|
| [[2604.07931v1]] Robust Length Prediction | Output lengths follow heavy-tailed distribution; ProD achieves up to 25% MAE reduction | `inference` `serving` `LLM` |
| [[2604.08075v1]] Dual-Pool Routing | Token-budget routing reduces GPU-hours 31-42%, saves $2.86M/yr on A100 | `LLM-serving` `cost-optimization` |
| [[2604.08133v1]] Alloc-MoE | Budget-aware expert activation; 1.15-1.34x speedup at half budget (ACL 2026) | `MoE` `inference` |
| [[2604.08541v1]] Routing Distraction | Cross-modal semantic sharing causes routing divergence in multimodal MoE | `MoE` `multimodal` `routing` |

### Representation Analysis & Evaluation

| Paper | Key Finding | Tags |
|-------|-------------|------|
| [[2604.08192v1]] Inside-Out ViT | Circuit-discovery metrics DDB/CSS predict generalization (+13.4%/+34.1% over baselines) | `generalization` `ViT` `circuits` |
| [[2604.08492v1]] Node Embedding Stability | No universal dimension-stability trend; max stability ≠ optimal performance | `embeddings` `stability` |
| [[2604.08502v1]] C-Score | Annotation-free metric for CAM explanation consistency; detects pre-collapse signals | `explainability` `medical-imaging` |
| [[2604.08513v1]] Semantic Drift | Fine-tuning causes architecture-dependent semantic drift in medical explanations | `fine-tuning` `explainability` |
| [[2604.08335v1]] Dead Weights, Live Signals | Feedforward graph of 5 frozen LLMs; only 17M trained params beat individual models | `model-combination` `frozen-models` |

### Machine Unlearning & Bias

| Paper | Key Finding | Tags |
|-------|-------------|------|
| [[2604.08111v1]] Bias Redistribution | Unlearning redistributes bias along gender (not age) boundaries in CLIP space | `unlearning` `fairness` `CLIP` |
| [[2604.08271v1]] Illusion of Unlearning | Feature-classifier misalignment; unlearned models retain 92.5% linear-probe accuracy (AISTATS 2026) | `unlearning` `representations` |

### RL for Reasoning

| Paper | Key Finding | Tags |
|-------|-------------|------|
| [[2604.08476v1]] Faithful GRPO | Constrains GRPO for visual-spatial reasoning; prevents CoT-answer inconsistency | `GRPO` `spatial-reasoning` |
| [[2604.08299v1]] SeLaR | Entropy-gated latent reasoning; +4.63% avg improvement on Qwen3-8B (ACL 2026) | `latent-reasoning` `inference` |

### Mathematical Foundations & Architecture

| Paper | Key Finding | Tags |
|-------|-------------|------|
| [[2604.07904v1]] Kuramoto Phase Encoding | Neuro-inspired synchronization in transformers; 0.1-0.7pp gains on SSL benchmarks | `attention` `synchronization` |
| [[2604.07935v1]] Hyperscale Lottery | Mamba-1→3 trades edge latency for cloud throughput; 28-48% edge penalty | `SSM` `edge-efficiency` |
| [[2604.08245v1]] Meta-Principle Physics | Embeds physical meta-principles as architectural modules; "436x" claim is misleading | `physics-informed` `architecture` |

### Hardware & Systems

| Paper | Key Finding | Tags |
|-------|-------------|------|
| [[2604.08044v1]] 3D-DRAM LLM Accelerators | Full-stack evaluation framework; 2.53x speedup / 6.66x energy efficiency over H200 | `hardware` `LLM-accelerator` |
| [[2604.08182v1]] Wattlytics | HPC cluster co-optimization platform for performance/energy/TCO | `HPC` `energy` `systems` |
| [[2604.08357v1]] Bias-Constrained Diffusion | Adaptive noise schedules for PDE emulation; dramatic FSD improvements | `diffusion` `PDE` `training-stability` |

### Neuroscience & Brain Decoding

| Paper | Key Finding | Tags |
|-------|-------------|------|
| [[2604.08537v1]] Meta-learning Brain Decoding | Hierarchical ICL for cross-subject brain decoding; 22.7% Top-1 vs 3.9% prior work | `brain-decoding` `meta-learning` `fMRI` |

---

## All Papers

| # | Paper | Authors | Key Topic | Score |
|---|-------|---------|-----------|-------|
| 1 | [[2604.08527v1]] Demystifying OPD | Feng Luo et al. | Training Stability | 5 |
| 2 | [[2604.08524v1]] Representation Steering | Stephen Cheng et al. | Mechanistic Interpretability | 5 |
| 3 | [[2604.08510v1]] Implicit Curriculum | Emmy Liu et al. | Pretraining Dynamics | 5 |
| 4 | [[2604.07955v1]] Residual Errors in Quantization | Shuaiting Li et al. | Quantization (ICLR 2026) | 5 |
| 5 | [[2604.08118v1]] Codebook Initialisation | Ian W. Kennedy et al. | Extreme Quantization | 5 |
| 6 | [[2604.08474v1]] Quantization in FL | Abdelkarim Loukili | Quantization / Federated | 5 |
| 7 | [[2604.08539v1]] OpenVLThinkerV2 | Wenbo Hu et al. | Multimodal RL Training | 4 |
| 8 | [[2604.08541v1]] Routing Distraction | Haolei Xu et al. | MoE Interpretability | 4 |
| 9 | [[2604.08502v1]] C-Score Metric | Kabilan Elangovan et al. | Explanation Consistency | 4 |
| 10 | [[2604.08513v1]] Semantic Drift | Kabilan Elangovan et al. | Fine-tuning Stability | 4 |
| 11 | [[2604.08492v1]] Node Embedding Stability | Tobias Schumacher et al. | Embedding Reliability | 4 |
| 12 | [[2604.08271v1]] Illusion of Unlearning | Yichen Gao et al. | Unlearning (AISTATS 2026) | 4 |
| 13 | [[2604.08335v1]] Dead Weights, Live Signals | Marcus Armstrong et al. | Frozen Model Graphs | 4 |
| 14 | [[2604.08333v1]] Lost in the Hype | Xun Zhu et al. | Medical MLLM Failure | 4 |
| 15 | [[2604.08284v1]] DMLE | Yating Wang et al. | Knowledge Editing | 4 |
| 16 | [[2604.08192v1]] Inside-Out ViT | Yunxiang Peng et al. | ViT Generalization | 4 |
| 17 | [[2604.08039v1]] LINE | Vladimir Zaigrajew et al. | Neuron Explanations | 4 |
| 18 | [[2604.08075v1]] Dual-Pool Routing | Xunzhuo Liu et al. | LLM Serving | 4 |
| 19 | [[2604.07931v1]] Robust Length Prediction | Jing Wang et al. | Inference Reliability | 4 |
| 20 | [[2604.07925v1]] Sinkhorn Attention Rank | Michela Lapenna et al. | Attention Theory | 4 |
| 21 | [[2604.07935v1]] Hyperscale Lottery | Robin Geens et al. | SSM Edge Efficiency | 4 |
| 22 | [[2604.08169v1]] Activation Steering | Niklas Herbster et al. | Alignment Steering | 4 |
| 23 | [[2604.08357v1]] Bias-Constrained Diffusion | Constantin Le Clei et al. | Diffusion Training | 3 |
| 24 | [[2604.08245v1]] Meta-Principle Physics | Helong Hu et al. | Physics-Informed | 3 |
| 25 | [[2604.08133v1]] Alloc-MoE | Baihui Liu et al. | MoE Inference (ACL 2026) | 3 |
| 26 | [[2604.08182v1]] Wattlytics | Ayesha Afzal et al. | HPC Energy | 3 |
| 27 | [[2604.08044v1]] 3D-DRAM Accelerators | Cong Li et al. | Hardware Evaluation | 3 |
| 28 | [[2604.07904v1]] Kuramoto Phase | Mingqing Xiao et al. | Attention Mechanism | 3 |
| 29 | [[2604.07963v1]] Data Mixing | Yuanjian Xu et al. | Training Data | 3 |
| 30 | [[2604.08476v1]] Faithful GRPO | Sai Srinivas Kancheti et al. | RL Reasoning | 3 |
| 31 | [[2604.08111v1]] Bias Redistribution | Yunusa Haruna et al. | Unlearning Bias | 3 |
| 32 | [[2604.08537v1]] Brain Decoding | Mu Nan et al. | fMRI / Meta-learning | 3 |
| 33 | [[2604.07941v1]] LLM Post-Training Survey | Shiwan Zhao et al. | RLHF Survey (Huawei) | 3 |
| 34 | [[2604.08299v1]] SeLaR | Renyu Fu et al. | Latent Reasoning (ACL 2026) | 3 |

---

*Overview generated on 2026-04-11 from arxiv papers dated 2026-04-09*
