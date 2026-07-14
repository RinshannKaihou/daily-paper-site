---
title: "Daily Paper Overview — 2026-05-24"
date: 2026-05-24
tags:
  - daily-overview
  - arxiv
papers: 34
---

## 今日必读 / Must Read Today

### 1. [[2605.24846]] Tiny Brains, Giant Impact: Keystone Neurons of LLM

> **推荐理由 / Why Read:** 发现LLM中存在极少量"基石神经元"，仅微调这些神经元即可匹配甚至超越全参数微调效果 / Identifies a tiny subset of "keystone neurons" whose fine-tuning alone matches or exceeds full-parameter fine-tuning, opening a new path for efficient LLM adaptation.

### 2. [[2605.24941]] Memory-Induced Tool-Drift in LLM Agents

> **推荐理由 / Why Read:** 揭示带长期记忆的LLM智能体存在隐式工具调用偏移漏洞，对MCP生态和ChatGPT记忆系统有重要安全警示 / Reveals that biased personality memories silently alter tool-call parameters in LLM agents — a critical safety concern for MCP ecosystems and memory-enabled agents.

### 3. [[2605.24793]] Beyond the Target: Collaborative Speculative Decoding (CoSpec)

> **推荐理由 / Why Read:** 将投机解码从"模仿"重新定义为"协作"，在2–4×加速的同时超越target-only准确率 / Reframes speculative decoding as draft–target collaboration via RL, achieving 2–4× speedup while surpassing target-only accuracy — both faster and better.

---

## 按主题分类 / Papers by Topic

### LLM 推理效率 / LLM Inference Efficiency

| Paper | 描述 / Description |
|-------|-------------------|
| [[2605.24786]] CONF-KV | 基于置信度的KV cache自适应淘汰策略，混合精度存储，困惑度差距缩小74% / Confidence-aware KV cache eviction with mixed-precision storage, closing 74% perplexity gap |
| [[2605.25085]] Polynomial Truncation Sensitivity | KV cache压缩的序贯Wyner-Ziv理论框架，发现截断敏感度呈多项式衰减 / Sequential Wyner-Ziv framework for KV cache compression, polynomial truncation sensitivity |
| [[2605.24793]] CoSpec | 协作式投机解码，RL仲裁器选择更优draft分支 / Collaborative speculative decoding with RL arbitrator for better draft selection |
| [[2605.25244]] CDG Voting | 置信度动态增益投票，利用推理轨迹置信度趋势区分正确/错误答案 / Confidence Dynamic Gain voting exploits rising/falling confidence along reasoning traces |

### 机械可解释性 / Mechanistic Interpretability

| Paper | 描述 / Description |
|-------|-------------------|
| [[2605.24846]] Keystone Neurons | 发现LLM中少量"基石神经元"主导多任务推理，仅微调即可匹配全参数FT / Discovers keystone neurons whose fine-tuning alone matches full-parameter FT |
| [[2605.24856]] Concept Allocation Zone (CAZ) | 追踪Transformer残差流中概念形成的深度区间框架 / Framework tracking concept formation depth intervals in transformer residual stream |
| [[2605.24942]] Riemannian-Manifold Steering | 将激活操控定义为黎曼流形测地线，无需逐样本标签 / Reframes activation steering as Riemannian geodesics without per-sample labels |
| [[2605.24946]] VISTA | 通过文本SAE约束实现视觉到语言的可解释性迁移 / Cross-modal interpretability transfer from language to vision via sparse autoencoders |
| [[2605.25225]] Field Theory for Transformers | 将残差流建模为深度-token场，用格林函数/伴随灵敏度统一激活修补，GPT-2上线性区误差<20% / Field-theoretic framework treating residual stream as depth-token field with Green-function response, <20% linear-regime error on GPT-2 |
| [[2605.25151]] Representation Without Control | 证明线性可解码表征不等于因果可控，分离可读性与因果性 / Shows linearly decodable representations do not imply causal controllability |

### LLM 安全、对齐与验证 / LLM Safety, Alignment & Verification

| Paper | 描述 / Description |
|-------|-------------------|
| [[2605.24817]] RouteScan | 利用GPU遥测侧信道非侵入式审计MoE模型安全 / Non-intrusive MoE safety auditing via GPU expert routing telemetry |
| [[2605.24941]] Memory-Induced Tool-Drift | 揭示长期记忆导致LLM智能体工具调用参数被隐式篡改 / Reveals memory-induced tool-call parameter drift in LLM agents |
| [[2605.25189]] TDGA (Directional Alignment) | 从优化几何视角解决RLHF中的奖励作弊问题 / Mitigates reward hacking via trusted direction gradient alignment |
| [[2605.25133]] PVD (Prover-Verifier Deliberation) | 证明者-验证者对话实现选择性预测，GPQA上HC-Prec 84.2%@77%覆盖(+32pp)，约3次调用 / Prover-verifier deliberation for selective prediction, GPQA HC-Prec 84.2%@77% cov (+32pp gap), ~3 calls |

### 推理与强化学习训练 / Reasoning & RL Training

| Paper | 描述 / Description |
|-------|-------------------|
| [[2605.24998]] HSIR | 自改进推理框架，VeriExit复用部分正确步骤 + InDiv过滤过度思考 / Self-improvement framework with partial-reasoning reuse and overthinking filtration |
| [[2605.25252]] RLVR Compute-Supervision | 实证发现计算量无法弥补验证器噪声，假阴性比假阳性危害更大 / Shows compute cannot compensate for verifier noise; false negatives are worse |

### 评估与基准测试 / Evaluation & Benchmarking

| Paper | 描述 / Description |
|-------|-------------------|
| [[2605.24818]] Spiking Training Data | 通过注入已知比例测试样本修正基准污染分数 / Corrects contaminated benchmark scores by spiking training data at known rates |
| [[2605.25052]] BonaFide | 构建CoT忠实性元评估基准(3066条标注)，最佳指标仅0.70 AUROC，多数接近随机 / Ground-truth faithfulness benchmark (3,066 labeled CoTs); best metric only 0.70 AUROC, most near-chance |
| [[2605.24960]] FaithMate | 统一CoT忠实性的上下文/参数两种优化范式 / Unifies contextual and parametric CoT faithfulness optimization |
| [[2605.25240]] JudgmentBench | 法律任务上成对偏好恢复质量排序远优于rubric(ρ=0.908 vs 0.150)，标注时间仅40% / Pairwise preference recovers quality ordering far better than rubric (ρ=0.908 vs 0.150) on legal tasks, at 40% annotation time |
| [[2605.25272]] AI Cartography | 用心理测量学分析4000+模型排行榜，揭示双因子结构 / Psychometric analysis of 4,000+ models revealing bifactor latent structure |
| [[2605.24850]] Repeated Sequences | 通过Rényi熵分析发现LLM生成文本与自然语言的长程结构差异 / Rényi entropy analysis reveals LLM text diverges from natural language in long-range structure |

### 幻觉检测与控制 / Hallucination Detection & Control

| Paper | 描述 / Description |
|-------|-------------------|
| [[2605.24919]] MultiHaluDet | 多语言幻觉检测堆叠框架，英语AUROC 98.55%，跨语言泛化强 / Multilingual hallucination detection stacking framework, 98.55% AUROC on English |
| [[2605.24977]] SAE Steering for Medical VLM | 推理时SAE残差编辑减医学VLM幻觉，三模型复合指标+5.4%/+7.2%/+17.0%，GREEN p<0.001 / Inference-only SAE residual steering cuts medical VLM hallucinations, Composite +5.4%/+7.2%/+17.0% rel., GREEN p<0.001 |

### 模型压缩与量化 / Model Compression & Quantization

| Paper | 描述 / Description |
|-------|-------------------|
| [[2605.25054]] NMP-QAT | 神经元级自适应混合精度量化训练 / Neuron-level adaptive mixed-precision quantization aware training |
| [[2605.25203]] Spectral Rotations | Walsh-Hadamard谱旋转用于极低位宽LLM量化 / Walsh-Hadamard spectral rotations for extreme low-bit LLM quantization |

### LLM 训练与隐私 / LLM Training & Privacy

| Paper | 描述 / Description |
|-------|-------------------|
| [[2605.24956]] NITP | 下一隐式token预测，用余弦相似度补充NTP，MMLU-Pro提升5.7% / Next Implicit Token Prediction augments NTP with cosine similarity, +5.7% MMLU-Pro |
| [[2605.24879]] DP-SGD-RC | 随机迹估计替代精确梯度范数计算，LLM差分隐私训练减15-40%内存 / Stochastic trace estimation for efficient DP-SGD on LLMs, 15-40% memory reduction |
| [[2605.24908]] Class Imbalance in DNNs | 系统分析类别不平衡下DNN"先欠拟合后过拟合"的少数类学习动态 / Systematic analysis of underfit-then-overfit minority class learning dynamics |

### 深度学习理论 / Deep Learning Theory

| Paper | 描述 / Description |
|-------|-------------------|
| [[2605.25234]] Epistemic Uncertainty | 证明过参数化ReLU网络即使函数完全识别参数不确定性仍持续存在 / Proves epistemic uncertainty persists even when function is fully identified |
| [[2605.25275]] Label-NTK Alignments | 发现标签-NTK特征谱对齐关系，大幅缩紧收敛界 / Discovers label-NTK alignment properties enabling tighter convergence bounds |
| [[2605.25001]] CAML for PINNs | 从损失景观分析PINN梯度病理，提出对齐约束方法 / Analyzes PINN gradient pathology via loss landscape, proposes constraint-aligned method |

### 系统与可观测性 / Systems & Observability

| Paper | 描述 / Description |
|-------|-------------------|
| [[2605.25298]] Prism (eBPF) | 基于eBPF的应用无关性能退化诊断，开销仅0.06-0.37ms / Application-agnostic performance diagnosis via eBPF with 0.06-0.37ms overhead |
| [[2605.25066]] QML-PipeGuard | 量子ML管道的行为指纹验证框架 / Behavioral fingerprinting for quantum ML pipeline integrity verification |

---

## All Papers

| # | Paper | 标题 (短) / Short Title | 主题 / Topic |
|---|-------|------------------------|-------------|
| 1 | [[2605.24786]] | CONF-KV: Confidence-Aware KV Cache Eviction | LLM推理效率 / Inference Efficiency |
| 2 | [[2605.24793]] | CoSpec: Collaborative Speculative Decoding | LLM推理效率 / Inference Efficiency |
| 3 | [[2605.24817]] | RouteScan: MoE Safety Auditing | 安全与验证 / Safety & Verification |
| 4 | [[2605.24818]] | Spiking Training Data for Contamination Correction | 评估与基准 / Evaluation & Benchmarking |
| 5 | [[2605.24846]] | Keystone Neurons of LLM | 机械可解释性 / Mechanistic Interpretability |
| 6 | [[2605.24850]] | Repeated Sequences: LLM vs Natural Language | 评估与基准 / Evaluation & Benchmarking |
| 7 | [[2605.24856]] | Concept Allocation Zone (CAZ) | 机械可解释性 / Mechanistic Interpretability |
| 8 | [[2605.24879]] | DP-SGD-RC: Efficient DP-SGD for LLMs | 训练与隐私 / Training & Privacy |
| 9 | [[2605.24908]] | Class Imbalance in DNN Learning Dynamics | 训练与隐私 / Training & Privacy |
| 10 | [[2605.24919]] | MultiHaluDet: Multilingual Hallucination Detection | 幻觉检测 / Hallucination Control |
| 11 | [[2605.24941]] | Memory-Induced Tool-Drift in LLM Agents | 安全与验证 / Safety & Verification |
| 12 | [[2605.24942]] | Riemannian-Manifold Steering (GAGA) | 机械可解释性 / Mechanistic Interpretability |
| 13 | [[2605.24946]] | VISTA: Interpretability Transfer via SAE | 机械可解释性 / Mechanistic Interpretability |
| 14 | [[2605.24956]] | NITP: Next Implicit Token Prediction | 训练与隐私 / Training & Privacy |
| 15 | [[2605.24960]] | FaithMate: CoT Faithfulness Optimization | 评估与基准 / Evaluation & Benchmarking |
| 16 | [[2605.24977]] | SAE Steering for Medical VLM | 幻觉检测 / Hallucination Control |
| 17 | [[2605.24998]] | HSIR: Self-Improvement in Reasoning Models | 推理与RL / Reasoning & RL |
| 18 | [[2605.25001]] | CAML: Gradient Pathology in PINNs | 深度学习理论 / DL Theory |
| 19 | [[2605.25052]] | BonaFide: Faithfulness Metrics Meta-Evaluation | 评估与基准 / Evaluation & Benchmarking |
| 20 | [[2605.25054]] | NMP-QAT: Adaptive Neuron-level Mixed Precision | 模型压缩 / Model Compression |
| 21 | [[2605.25066]] | QML-PipeGuard: QML Pipeline Integrity | 系统与可观测性 / Systems & Observability |
| 22 | [[2605.25085]] | Polynomial Truncation Sensitivity for KV Cache | LLM推理效率 / Inference Efficiency |
| 23 | [[2605.25133]] | PVD: Prover-Verifier Deliberation | 安全与验证 / Safety & Verification |
| 24 | [[2605.25151]] | Representation Without Control | 机械可解释性 / Mechanistic Interpretability |
| 25 | [[2605.25189]] | TDGA: Directional Alignment for Reward Hacking | 安全与验证 / Safety & Verification |
| 26 | [[2605.25203]] | Spectral Rotations for Low-Bit Quantization | 模型压缩 / Model Compression |
| 27 | [[2605.25225]] | Field Theory for Transformer Patching | 机械可解释性 / Mechanistic Interpretability |
| 28 | [[2605.25234]] | Epistemic Uncertainty in Overparametrized Networks | 深度学习理论 / DL Theory |
| 29 | [[2605.25240]] | JudgmentBench: Rubric vs Preference Evaluation | 评估与基准 / Evaluation & Benchmarking |
| 30 | [[2605.25244]] | CDG Voting: Confidence Dynamics for Inference | LLM推理效率 / Inference Efficiency |
| 31 | [[2605.25252]] | Compute-Supervision Tradeoffs in RLVR | 推理与RL / Reasoning & RL |
| 32 | [[2605.25272]] | AI Cartography: Mapping Benchmark Ecosystems | 评估与基准 / Evaluation & Benchmarking |
| 33 | [[2605.25275]] | Label-NTK Alignments & Convergence Bounds | 深度学习理论 / DL Theory |
| 34 | [[2605.25298]] | Prism: eBPF Performance Diagnosis | 系统与可观测性 / Systems & Observability |
