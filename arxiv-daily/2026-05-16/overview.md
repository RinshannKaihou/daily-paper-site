---
title: "Daily Arxiv Overview — 2026-05-16"
date: 2026-05-16
tags:
  - daily-paper
  - llm
  - quantization
  - reasoning
  - efficient-inference
  - representation-learning
  - safety
papers: 32
---

# Daily Arxiv Overview — 2026-05-16

共 **32** 篇论文 / **32** papers total.

---

## 今日必读 / Must Read Today

### 1. [[2605.16928]] RTPurbo: Full Attention Strikes Back
**理由 / Reason:** 揭示全注意力LLM仅15%查询头为检索头，通过~600步训练即实现1M上下文9.36倍prefill加速，实用价值极高。 / Reveals only 15% of query heads are retrieval heads in full-attention LLMs; achieves 9.36x prefill speedup at 1M context with ~600 training steps — extremely practical.

### 2. [[2605.16787]] The Unlearnability Phenomenon in RLVR
**理由 / Reason:** 发现RLVR训练中16-30%困难样本即使有正确rollout也无法学会，根因在表征缺陷而非优化，挑战了RL训练的核心假设。 / Discovers 16-30% of hard examples remain unlearnable despite correct rollouts in RLVR; root cause is representation deficiency, not optimization — challenges core RL training assumptions.

### 3. [[2605.17028]] PARALLAX: Hallucination Detection Benchmark Artifacts
**理由 / Reason:** 揭示幻觉检测领域6个基准中4个存在teacher-forcing构造伪影，多数方法在受控条件下接近随机水平，是领域重置级工作。 / Exposes systematic teacher-forcing artifacts in 4/6 hallucination detection benchmarks; most methods collapse to near-chance under controlled conditions — a field-resetting paper.

---

## 按主题分类 / Papers by Topic

### 模型量化与高效推理 / Model Quantization & Efficient Inference

| Paper | 一句话摘要 / One-line Summary |
|-------|------------------------------|
| [[2605.16732]] DiRotQ | PCA子空间分解的旋转感知量化，W4A4下FID优于FP16基线 / PCA-based rotation-aware W4A4 quantization achieving FID better than FP16 baseline |
| [[2605.16882]] E-PMQ | 模型合并后量化的专家引导校准框架，锚定消融准确率从68%降至5% / Expert-guided calibration for post-merge quantization; anchor ablation collapses accuracy from 68% to 5% |
| [[2605.16901]] CAR-SAM | SAM解码器交叉注意力的MatMul感知补偿，W4A4提升14.6% mAP / MatMul-aware compensation for SAM decoder cross-attention; +14.6% mAP at W4A4 |
| [[2605.17093]] HEED | 混合VLM蒸馏的密度加权残差对齐，OCRBench v2提升8.7分 / Density-weighted residual alignment for hybrid VLM distillation; +8.7 on OCRBench v2 |
| [[2605.16928]] RTPurbo | 15%检索头+动态top-p实现1M上下文9.36倍加速 / 15% retrieval heads + dynamic top-p achieve 9.36x speedup at 1M context |
| [[2605.17170]] TriAxialKV | 三轴混合精度KV-cache量化，代理推理4.5倍压缩 / Triaxial mixed-precision KV-cache quantization; 4.5x compression for agentic inference |
| [[2605.17164]] Charon | 统一LLM训练与推理模拟器，万卡预测误差<3.74% / Unified LLM training+inference simulator; <3.74% error at ~10K GPUs |

### 推理模型与训练动态 / Reasoning Models & Training Dynamics

| Paper | 一句话摘要 / One-line Summary |
|-------|------------------------------|
| [[2605.16787]] Unlearnability in RLVR | 16-30%困难样本表征缺陷导致不可学习，mid-training是解法 / 16-30% hard examples unlearnable due to representation deficiency; mid-training is the fix |
| [[2605.16874]] Reasoning Restored by Decision Tokens | 8%早期规划决策token驱动推理优势，4%干预恢复91%差距 / ~8% early planning decision tokens drive reasoning advantage; 4% intervention recovers 91% gap |
| [[2605.17026]] Forks in the Road | SFT覆盖率下降根因是决策分叉点，问题级多样性是关键 / Coverage shrinkage caused by decision forks in SFT data; problem-level diversity is key |
| [[2605.17109]] DynMuon | 谱塑形优化器动态调度指数p，10.6-26.5%步数减少 / Dynamic spectral shaping optimizer; 10.6-26.5% step reduction over Muon |

### LLM安全与可靠性 / LLM Safety & Reliability

| Paper | 一句话摘要 / One-line Summary |
|-------|------------------------------|
| [[2605.16746]] State Contamination | 多智能体记忆清洗攻击，毒性通过摘要逃避检测 / Memory laundering attack in multi-agent systems; toxicity evades detection through summarization |
| [[2605.17028]] PARALLAX | 幻觉检测基准构造伪影，多数方法受控下接近随机 / Hallucination detection benchmark artifacts; most methods near-chance when controlled |
| [[2605.16993]] Adversarial Fragility in Clinical AI | 临床AI对抗扰动+跨语言漂移双重脆弱性审计 / Dual audit of adversarial fragility + cross-lingual drift in clinical AI |
| [[2605.17153]] VeriStress-GT | 神经网络验证器压力测试框架，发现实现bug / Stress-testing framework for NN verifiers; uncovers real implementation bugs |
| [[2605.28850]] LLM Trading Agents | 交易代理相关性盲点与失败前表征签名 / Correlation blind spots and pre-failure representation signatures in LLM trading agents |

### 表征学习与几何分析 / Representation Learning & Geometry

| Paper | 一句话摘要 / One-line Summary |
|-------|------------------------------|
| [[2605.17084]] Scale Determines Representation Geometry | 大模型中间层保持预测对齐，小模型出现绕行现象 / Large models maintain prediction-aligned geometry; small models exhibit detour phenomenon |
| [[2605.17180]] Geometry of Projection Heads | 投影头黎曼度量理论，Swish比ReLU更抗维度坍缩 / Riemannian metric theory for projection heads; Swish more collapse-resistant than ReLU |
| [[2605.28854]] LLM Representational Geometry in ICL | ICL受预训练表征几何约束，原型学习最匹配LLM行为 / ICL constrained by pretraining representation geometry; prototype learning best matches LLM behavior |
| [[2605.16824]] Confidence Geometry | token级置信度轨迹蕴含正确性几何结构 / Token-level confidence trajectories encode correctness geometry |

### 优化理论与学习动态 / Optimization Theory & Learning Dynamics

| Paper | 一句话摘要 / One-line Summary |
|-------|------------------------------|
| [[2605.16913]] Fourier Perspective on NN Dynamics | 幂律谱加速相位学习，幅值先于相位被学习 / Power-law spectra accelerate phase learning; amplitude learned before phase |
| [[2605.17177]] High-dim SGD for Diagonal Linear Networks | 高维SGD的SDE逼近与确定性PDE极限 / SDE approximation and deterministic PDE limit for high-dimensional SGD |
| [[2605.17126]] Multi-task Linear Regression (MTLR) | 矩阵加权正则化替代特征值下界假设，含安全保证 / Matrix-weighted regularization replacing eigenvalue lower bound; safety guarantee included |

### 生成模型与蒸馏 / Generative Models & Distillation

| Paper | 一句话摘要 / One-line Summary |
|-------|------------------------------|
| [[2605.16949]] sREPA | 结构化表征对齐加速DiT训练，400K迭代FID 7.17 / Structural representation alignment accelerates DiT training; FID 7.17 at 400K iterations |

### 机器人学习与具身智能 / Robot Learning & Embodied AI

| Paper | 一句话摘要 / One-line Summary |
|-------|------------------------------|
| [[2605.17144]] COAST | Conceptor引导的VLA推理时策略优化，仿真+20%真实+40% / Conceptor-guided inference-time VLA steering; +20% sim, +40% real success rate |

### 多智能体系统与供应链 / Multi-Agent Systems & Supply Chain

| Paper | 一句话摘要 / One-line Summary |
|-------|------------------------------|
| [[2605.17036]] Autonomous AI in Supply Chain | 智能体牛鞭效应+GRPO后训练降低成本40% / Agent bullwhip effect + GRPO post-training reduces costs by 40% |

### 公平性与可解释性 / Fairness & Explainability

| Paper | 一句话摘要 / One-line Summary |
|-------|------------------------------|
| [[2605.17160]] Counterfactual-Faithful Quantization | 量化破坏算法反事实，CFQ方法降低Validity Drop约2倍 / Quantization breaks algorithmic recourse; CFQ reduces Validity Drop ~2x |

### 计算机视觉与情感计算 / Computer Vision & Affective Computing

| Paper | 一句话摘要 / One-line Summary |
|-------|------------------------------|
| [[2605.17179]] iMiGUE-3K | 最大规模自然场景微手势数据集+双模态自监督基础模型 / Largest in-the-wild micro-gesture dataset + dual-modality SSL foundation models |

### 物理模拟与科学计算 / Physics Simulation & Scientific Computing

| Paper | 一句话摘要 / One-line Summary |
|-------|------------------------------|
| [[2605.18883]] Prediction Is Not Physics | 扩散模型预测精度高但能量守恒差3-4个数量级 / Diffusion models predict well but violate energy conservation by 3-4 orders of magnitude |

### 系统与硬件 / Systems & Hardware

| Paper | 一句话摘要 / One-line Summary |
|-------|------------------------------|
| [[2605.17158]] SPARK ILP Accelerator | 近缓存ILP加速器，相对CPU 12-15倍加速 / Near-cache ILP accelerator; 12-15x speedup over CPU |
| [[2605.17182]] Workload-Aware PDN Optimization | 基于架构功耗轨迹的早期PDN优化，面积缩减32% / Architecture power-trace-driven early PDN optimization; 32% area reduction |

### 提示与ICL / Prompting & In-Context Learning

| Paper | 一句话摘要 / One-line Summary |
|-------|------------------------------|
| [[2605.17088]] ACIL | Auto-CoT用于ICL的四阶段流水线 / Four-stage Auto-CoT pipeline for in-context learning |

---

## All Papers

| # | ID | Short Title | Tags |
|---|-----|------------|------|
| 1 | [[2605.16732]] | DiRotQ: Rotation-Aware Quantization for DiT | quantization, diffusion-models |
| 2 | [[2605.16746]] | State Contamination in Memory-Augmented LLM Agents | llm-safety, multi-agent-systems |
| 3 | [[2605.16787]] | Unlearnability Phenomenon in RLVR | RLVR, training-dynamics, reasoning |
| 4 | [[2605.16824]] | Confidence Geometry in LLM Reasoning | llm-reasoning, confidence-estimation |
| 5 | [[2605.16874]] | Reasoning Restored by Decision Tokens | reasoning-models, token-level-analysis |
| 6 | [[2605.16882]] | E-PMQ: Expert-Guided Post-Merge Quantization | model-merging, quantization |
| 7 | [[2605.16901]] | CAR-SAM: Cross-Attention Reconstruction for SAM | model-quantization, segment-anything |
| 8 | [[2605.16913]] | Fourier Perspective on NN Learning Dynamics | neural-network-dynamics, fourier-analysis |
| 9 | [[2605.16928]] | RTPurbo: Full Attention Strikes Back | sparse-attention, long-context, LLM-optimization |
| 10 | [[2605.16949]] | sREPA: Structural Representation Alignment for DiT | diffusion-transformers, training-acceleration |
| 11 | [[2605.16993]] | Adversarial Fragility in Clinical AI | clinical-ai, adversarial-robustness, cross-lingual-NLP |
| 12 | [[2605.17026]] | Forks in the Road: Coverage Shrinkage in Reasoning | reasoning-models, coverage-shrinkage, data-centric-ai |
| 13 | [[2605.17028]] | PARALLAX: Hallucination Detection Benchmark Artifacts | hallucination-detection, benchmark-artifacts |
| 14 | [[2605.17036]] | Autonomous AI Agents in Supply Chain | llm-agents, supply-chain, reinforcement-learning |
| 15 | [[2605.17084]] | Scale Determines Representation Geometry | representation-geometry, scaling-laws |
| 16 | [[2605.17088]] | ACIL: Auto Chain of Thoughts for ICL | chain-of-thought, in-context-learning |
| 17 | [[2605.17093]] | HEED: Density-Weighted Residual Alignment for VLM | knowledge-distillation, vision-language-models |
| 18 | [[2605.17109]] | DynMuon: Dynamic Spectral Shaping of Muon | optimization, muon, llm-training |
| 19 | [[2605.17126]] | MTLR: Multi-task Linear Regression without Eigenvalue Bounds | multi-task-learning, robust-statistics |
| 20 | [[2605.17144]] | COAST: Conceptor Activation Steering for VLA | vision-language-action, activation-steering, robot-learning |
| 21 | [[2605.17153]] | VeriStress-GT: Stress-Testing NN Verifiers | neural-network-verification, benchmarking |
| 22 | [[2605.17158]] | SPARK: Near-Cache ILP Accelerator | ILP-solver, near-memory-computing |
| 23 | [[2605.17160]] | Counterfactual-Faithful Quantization (CFQ) | model-quantization, algorithmic-recourse, fairness |
| 24 | [[2605.17164]] | Charon: Unified LLM Training & Inference Simulator | llm-simulation, distributed-training |
| 25 | [[2605.17170]] | TriAxialKV: Extreme Low-Precision KV-Cache Quantization | kv-cache-quantization, llm-inference, agentic-ai |
| 26 | [[2605.17177]] | High-dim SGD for Diagonal Linear Networks | SGD-theory, high-dimensional-limits |
| 27 | [[2605.17179]] | iMiGUE-3K: Large-Scale Micro-Gesture Benchmark | micro-gesture, self-supervised-learning, affective-computing |
| 28 | [[2605.17180]] | Geometry of Projection Heads in SSL | self-supervised-learning, representation-learning |
| 29 | [[2605.17182]] | Workload-Aware Early-Stage PDN Optimization | power-delivery-network, EDA |
| 30 | [[2605.18883]] | Prediction Is Not Physics: Conservation in Neural Simulators | neural-simulation, hamiltonian-systems |
| 31 | [[2605.28850]] | Representation Signatures in LLM Trading Agents | llm-agents, financial-trading, risk-alignment |
| 32 | [[2605.28854]] | LLM Representational Geometry in In-Context Learning | in-context-learning, representational-geometry |
