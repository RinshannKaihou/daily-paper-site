---
title: "Daily Paper Overview — 2026-05-26"
date: 2026-05-26
tags:
  - daily-paper
  - arxiv
  - research-digest
papers: 50
---

## 今日必读 / Must Read Today

### 1. [[2605.27033]] Tracing Computation Density in LLMs

**推荐理由：** 通过 s-Trace 方法对 10 个 LLM 的计算图进行贪心子图搜索，发现仅约 0.1% 的计算图即可恢复 top-1 预测，揭示 LLM 计算的两阶段组织结构（建设 vs. 精炼），对动态计算与高效推理具有深远启示。

**Why read:** Introduces s-Trace to extract minimal computational subgraphs from 10 LLMs (7B–14B), discovering that ~0.1% of the graph suffices for greedy decoding and revealing a universal two-phase computation structure with direct implications for dynamic inference and early exit.

### 2. [[2605.27028]] Less is More: Early Stopping Rollout for On-Policy Distillation

**推荐理由：** 发现 on-policy distillation 中存在"Off-policy Teacher Decay"现象（教师对学生前缀条件下的准确率在 ~300 token 内跌到学生基线水平），并提出极简的 ESR 策略——仅用前 N 个 token 做 rollout 蒸馏，跨家族跨规模全面超越完整 rollout，且训练成本降低 24×。

**Why read:** Identifies Off-policy Teacher Decay in on-policy distillation (teacher avg@4 on MATH-500 decays 65.30%→51.75% within 300 student tokens) and proposes the elegantly simple Early Stopping Rollout (ESR), which consistently beats full-rollout distillation across Qwen/Gemma families and 1.5B–32B scales while delivering 24× wall-clock speedup.

### 3. [[2605.26842]] MONA: Muon Optimizer with Nesterov Acceleration for Scalable Language Model Training

**推荐理由：** 在 Muon 优化器基础上引入 Nesterov 加速（正交化前加梯度差分 EMA），在 1B–68B MoE 预训练中收敛速度与下游性能均超越 Muon 和 AdamW，是 Muon 类优化器在大规模预训练中最有说服力的实证。

**Why read:** Augments Muon with Nesterov acceleration using a gradient-difference EMA, achieving superior convergence and downstream performance over both Muon and AdamW across 1B–68B MoE pretraining (up to 1T tokens), the most compelling large-scale evidence for Muon-family optimizers to date.

---

## 按主题分类 / Papers by Topic

### 优化器与训练动力学 / Optimizers & Training Dynamics

| Paper | 简述 / Summary |
|-------|----------------|
| [[2605.26842]] MONA | Muon+Nesterov 加速，1B–68B MoE 预训练 SOTA / Nesterov-accelerated Muon achieving SOTA in 1B–68B MoE pretraining |
| [[2605.26459]] MuCon | 裁剪 Muon 奇异值更新的谱范数控制 / Clipped Muon updates via singular-value thresholding for spectral norm control |
| [[2605.26929]] Muon+Adversarial Training | Muon 在对抗训练中的理论与实证研究 / Theoretical and empirical study of Muon in adversarial training |
| [[2605.26977]] Spectral Descent | 谱下降在非光滑凸优化中的全局线性收敛 / Global linear convergence of Spectral Descent for non-smooth convex optimization |
| [[2605.26489]] Singular Distribution Stability | 谱视角揭示预训练两阶段动力学 / Spectral perspective on two-phase dynamics of LM pre-training |
| [[2605.27078]] Two Speeds of Learning | 表征-读出分解统一解释 grokking 和双下降 / Representation-readout decomposition unifying grokking and double descent |
| [[2605.26973]] SNR & Alignment | 信噪比和样本量决定神经网络表征对齐 / SNR and sample size govern representational alignment in neural networks |
| [[2605.26895]] Scale Vectors | 归一化层 scale vector 参数微小但至关重要 / Normalization scale vectors are negligible in size but critical for pretraining |
| [[2605.26919]] Agile Online Model Selection | 保护机制下的大学习率解决自适应滞后 / Safeguarded large learning rates resolving adaptation lag in online model selection |

### 强化学习后训练 / RL Post-Training

| Paper | 简述 / Summary |
|-------|----------------|
| [[2605.26606]] Pilot-Commit | 两阶段 rollout 分配，更少 rollout 达同等准确率 / Two-phase rollout allocation achieving same accuracy with fewer rollouts |
| [[2605.26958]] Tournament-GRPO | 锦标赛式相对评分用于开放长文本 RL / Tournament-style relative rewards for open-ended long-form RL generation |
| [[2605.26934]] RLVR Data Allocation | 推理深度与环境复杂度联合覆盖最优 / Joint coverage of reasoning depth and environment complexity is optimal for RLVR |
| [[2605.26971]] RLVR Datasets (ATLAS) | 溯源 RLVR 训练数据并构建去污染数据集 DAPO++ / Tracing RLVR data lineage and building decontaminated DAPO++ dataset |
| [[2605.27354]] SAERL | SAE 模型内部信号指导 RL 数据工程，1.5B 平均准确率 +3% / SAE-based model internals guiding post-training data engineering, +3% avg on 1.5B |
| [[2605.26403]] Calibrated Interactive RL | 校准交互式 RL 解决多轮对话分布偏移 / Calibrated interactive RL mitigating distribution shift in multi-turn dialogue |
| [[2605.26684]] GraphGPO | 图结构信用分配提升 LLM 智能体训练 / Graph-based credit assignment improving agentic RL training |
| [[2605.27028]] ESR | 早停 rollout 蒸馏，全面超越完整 rollout / Early Stopping Rollout outperforming full-rollout on-policy distillation |

### 量化与高效推理 / Quantization & Efficient Inference

| Paper | 简述 / Summary |
|-------|----------------|
| [[2605.27003]] SVDQuant-GPTQ (Wan2.2-I2V) | W4A4 量化视频 DiT，显存降低 59.3% / W4A4 quantization for video DiT with 59.3% memory reduction |
| [[2605.26628]] Tail-Aware HiFloat4 | HiFloat4 W4A4 量化 Wan2.2 视频生成 / HiFloat4 W4A4 quantization for Wan2.2 video generation |
| [[2605.26660]] WINDQuant | RL 混合精度量化 LLM，~2-bit 最优权衡 / RL-based mixed-precision LLM quantization at ~2-bit Pareto frontier |
| [[2605.26496]] Dense2MoE | 统一剪枝+MoE 升级端侧 LLM / Unified pruning and MoE upcycling for on-device LLMs |
| [[2605.26558]] Cassandra | 自推测解码实现边缘推理 2.41x 加速 / Self-speculative decoding achieving 2.41x edge inference speedup |
| [[2605.27081]] ReMoE | 微调路由器提升 MoE 专家复用，延迟降 43–50% / Router fine-tuning boosting expert reuse with 43–50% latency reduction |
| [[2605.26632]] RT-Lynx | Diffusion Transformer 激活稀疏化实现 1.55x 加速 / Activation sparsification for Diffusion Transformers with 1.55x speedup |
| [[2605.26636]] JetViT | 后训练注意力搜索 ViT 加速 1.79x / Post-training attention search achieving 1.79x ViT inference speedup |
| [[2605.26647]] Mixture of Activations | Token 自适应 FFN 激活函数混合 / Token-adaptive mixing of FFN activation functions |

### 可解释性与机理分析 / Interpretability & Mechanistic Analysis

| Paper | 简述 / Summary |
|-------|----------------|
| [[2605.27033]] s-Trace | LLM 计算密度追踪，0.1% 图即可 top-1 预测 / Tracing computation density in LLMs, 0.1% graph suffices for top-1 |
| [[2605.26795]] CoT at Probe Time | CoT 增益来自局部 token 共现而非逻辑推导 / CoT gains from local co-occurrence rather than global derivation |
| [[2605.26772]] CoT & Refusal Steering | CoT 联合编码拒绝机制，单一方向调控失效 / CoT jointly encodes refusal; single-direction steering fails |
| [[2605.26789]] Composition Collapse | 原子知识稳定不等于组合推理能力 / Stable factual knowledge does not imply compositional reasoning |
| [[2605.26735]] Layer Swap | Layer Swap 消除多语言推理差距 / Layer Swap eliminating multilingual reasoning gap |
| [[2605.26431]] Phase Structure in LLMs | LLM 表征阶段结构的语言学证据 / Evidence of minimalist phase structure in LLM representations |
| [[2605.26693]] EpiMer (Model Merging) | Riemannian 流形上的 Fréchet 均值模型合并 / Model merging as Fréchet mean on Riemannian manifold |
| [[2605.26484]] Extra-Merge | Rank-1 子空间外推实现无需训练的模型合并 / Rank-1 subspace extrapolation for training-free model merging |

### 安全与隐私 / Safety & Privacy

| Paper | 简述 / Summary |
|-------|----------------|
| [[2605.26409]] Behavioral Geometry | 行为几何预测越狱脆弱性，2% 探测达 0.94 AUPRC / Behavioral geometry predicting jailbreak susceptibility with 0.94 AUPRC at ~2% probe cost |
| [[2605.26526]] Fine-Tuning Defenses | 微调安全防护可被简单攻击绕过 / Fine-tuning safety defenses susceptible to simple attacks |
| [[2605.26433]] Vectors & Privacy | LLM 表示向量泄露敏感属性，SurfaceLoRA 防御 / LLM representation vectors leak sensitive attributes; SurfaceLoRA defense |
| [[2605.26670]] Knowledge Editing | 顺序知识编辑稳定性源于数学等价性而非正则化 / Sequential knowledge editing stability from mathematical equivalence, not regularization |
| [[2605.26827]] ContextGuard | 结构化自审计框架提升上下文学习可靠性 / Structured self-auditing improving in-context learning reliability |

### 扩散模型 / Diffusion Models

| Paper | 简述 / Summary |
|-------|----------------|
| [[2605.26582]] Stochasticity in Discrete Diffusion | 离散扩散中随机性通过冗余转移实现纠错 / Error-correcting effects of stochasticity in discrete diffusion via redundant transitions |
| [[2605.26756]] Memorized Regions Localization | 坐标曲率差异定位扩散模型记忆区域 / Coordinate-wise curvature differences localizing memorized regions in diffusion models |
| [[2605.26468]] Diffuse to Detect | DiT1D 用于 16nm IC 无监督异常检测，AUROC 0.771 / Diffusion Transformer for unsupervised 16nm IC anomaly detection at AUROC 0.771 |

### 智能体与系统 / Agents & Systems

| Paper | 简述 / Summary |
|-------|----------------|
| [[2605.26731]] Harness Sensitivity | LLM 代理最优 harness 复杂度非单调 / Optimal harness complexity is non-monotone across LLM agent tiers |
| [[2605.26667]] MemFail | LLM 记忆系统失败模式压力测试 / Stress-testing failure modes of LLM memory systems |
| [[2605.26733]] Looped LM Reasoning | Jacobian 谱半径正则化稳定循环推理 / Jacobian spectral radius regularization stabilizing looped LM reasoning |

### 其他 / Other

| Paper | 简述 / Summary |
|-------|----------------|
| [[2605.26494]] MiniMax-M2 | Mini 激活实现 Max 实世界智能的新模型系列 / New model series with mini activations for max real-world intelligence |
| [[2605.26577]] alpha-beta-CROWN Tutorial | 神经网络验证器形式化验证学习型控制器 / Tutorial on formal verification of learned controllers with alpha-beta-CROWN |
| [[2605.26415]] Rescue Effect (CLIP) | 空间语义早退绕过 CLIP 量化崩塌 / Spatio-semantic early exit bypassing quantization collapse in CLIP |
| [[2605.26726]] NCA Uncertainty | 扰动最终状态量化 NCA 预测不确定性 / Perturbation-based uncertainty quantification for Neural Cellular Automata |
| [[2605.27295]] Gemini Embedding 2 | Google 原生多模态嵌入，MSCOCO R@1 62.9 / Native multimodal embedding from Gemini, MSCOCO R@1 62.9 |

---

## All Papers

| # | ID | 标题 / Title | 主题 / Topic |
|---|-----|-------------|-------------|
| 1 | [[2605.26403]] | From Static Context to Calibrated Interactive RL | 强化学习 / RL |
| 2 | [[2605.26409]] | Jailbreak Susceptibility via Behavioral Geometry | 安全 / Safety |
| 3 | [[2605.26415]] | The Rescue Effect: Early Exit Bypasses CLIP Quantization Collapse | 量化 / Quantization |
| 4 | [[2605.26431]] | Probing Minimalist Phase Structure in LLMs | 可解释性 / Interpretability |
| 5 | [[2605.26433]] | Vectors Are Not Neutral: Privacy in LLM Summarization | 安全 / Safety |
| 6 | [[2605.26459]] | MuCon: Clipped Muon Updates for LLM Training | 优化器 / Optimizer |
| 7 | [[2605.26468]] | Diffuse to Detect: Diffusion for IC Anomaly Detection | 扩散模型 / Diffusion |
| 8 | [[2605.26484]] | Extra-Merge: Rank-1 Subspace Model Merging | 可解释性 / Interpretability |
| 9 | [[2605.26489]] | Singular Distribution Stability in LM Pre-training | 训练动力学 / Training Dynamics |
| 10 | [[2605.26494]] | MiniMax-M2: Mini Activations, Max Intelligence | 模型 / Model |
| 11 | [[2605.26496]] | Dense2MoE: Unified Pruning & MoE Upcycling | 量化 / Quantization |
| 12 | [[2605.26526]] | Fine-Tuning Defenses Susceptible to Simple Attacks | 安全 / Safety |
| 13 | [[2605.26558]] | Cassandra: Self-Speculative Decoding at Edge | 高效推理 / Efficient Inference |
| 14 | [[2605.26577]] | Bridging Control with alpha-beta-CROWN Tutorial | 形式化验证 / Formal Verification |
| 15 | [[2605.26582]] | Error-Correcting Stochasticity in Discrete Diffusion | 扩散模型 / Diffusion |
| 16 | [[2605.26606]] | Pilot-Commit: Rollout Allocation for RL Post-Training | 强化学习 / RL |
| 17 | [[2605.26628]] | Tail-Aware HiFloat4: W4A4 for Wan2.2 | 量化 / Quantization |
| 18 | [[2605.26632]] | RT-Lynx: Activation Sparsity for Diffusion Models | 高效推理 / Efficient Inference |
| 19 | [[2605.26636]] | JetViT: Post-Training Attention Search for ViT | 高效推理 / Efficient Inference |
| 20 | [[2605.26647]] | Mixture of Activations: Token-Adaptive FFN | 架构 / Architecture |
| 21 | [[2605.26660]] | WINDQuant: RL Mixed-Precision LLM Quantization | 量化 / Quantization |
| 22 | [[2605.26667]] | MemFail: Stress-Testing LLM Memory Systems | 智能体 / Agents |
| 23 | [[2605.26670]] | Knowledge Editing Regularizations Revisited | 安全 / Safety |
| 24 | [[2605.26684]] | GraphGPO: Graph-Based Credit Assignment for Agentic RL | 强化学习 / RL |
| 25 | [[2605.26693]] | EpiMer: Model Merging on Loss Landscape | 可解释性 / Interpretability |
| 26 | [[2605.26726]] | Uncertainty in Neural Cellular Automata | 其他 / Other |
| 27 | [[2605.26731]] | Harness Sensitivity Across LLM Agent Tiers | 智能体 / Agents |
| 28 | [[2605.26733]] | Stabilizing Looped LM Reasoning Dynamics | 智能体 / Agents |
| 29 | [[2605.26735]] | Layer Swap: Rethinking Multilingual Reasoning Gap | 可解释性 / Interpretability |
| 30 | [[2605.26756]] | Localizing Memorized Regions in Diffusion Models | 扩散模型 / Diffusion |
| 31 | [[2605.26772]] | CoT Disrupts Simple Steering of Refusal | 可解释性 / Interpretability |
| 32 | [[2605.26789]] | Composition Collapse in Factual Knowledge | 可解释性 / Interpretability |
| 33 | [[2605.26795]] | CoT Works via Local Co-Occurrence at Probe Time | 可解释性 / Interpretability |
| 34 | [[2605.26827]] | ContextGuard: Structured Self-Auditing for ICL | 安全 / Safety |
| 35 | [[2605.26842]] | MONA: Muon + Nesterov for Scalable LM Training | 优化器 / Optimizer |
| 36 | [[2605.26895]] | Scale Vectors in Large Language Models | 训练动力学 / Training Dynamics |
| 37 | [[2605.26919]] | Agile Online Model Selection with Large LR | 优化器 / Optimizer |
| 38 | [[2605.26929]] | Muon Meets Adversarial Training | 优化器 / Optimizer |
| 39 | [[2605.26934]] | RLVR Data Allocation: Reasoning Depth & Complexity | 强化学习 / RL |
| 40 | [[2605.26958]] | Tournament-GRPO for Open-Ended Generation | 强化学习 / RL |
| 41 | [[2605.26971]] | RLVR Datasets & Data Lineage (ATLAS/DAPO++) | 强化学习 / RL |
| 42 | [[2605.26973]] | SNR & Sample Size Govern Representational Alignment | 训练动力学 / Training Dynamics |
| 43 | [[2605.26977]] | Spectral Descent Convergence for Non-smooth Opt | 优化器 / Optimizer |
| 44 | [[2605.27003]] | SVDQuant-GPTQ: W4A4 for Wan2.2-I2V | 量化 / Quantization |
| 45 | [[2605.27028]] | ESR: Early Stopping Rollout for Distillation | 强化学习 / RL |
| 46 | [[2605.27033]] | s-Trace: Computation Density in LLMs | 可解释性 / Interpretability |
| 47 | [[2605.27078]] | Two Speeds of Learning: Grokking & Double Descent | 训练动力学 / Training Dynamics |
| 48 | [[2605.27081]] | ReMoE: Expert Reuse via Router Fine-Tuning | 高效推理 / Efficient Inference |
| 49 | [[2605.27295]] | Gemini Embedding 2: Multimodal Embedding | 嵌入 / Embedding |
| 50 | [[2605.27354]] | SAERL: SAE-Guided Post-Training Data Engineering | 强化学习 / RL |
