---
title: "Daily arXiv Digest — 2026-04-11"
date: 2026-04-11
tags:
  - llm-interpretability
  - mechanistic-interpretability
  - representation-geometry
  - training-reliability
  - quantization
  - model-editing
  - machine-unlearning
  - attribution-graphs
  - steering
  - implicit-curriculum
  - lossy-compression
  - inference-optimization
  - spectral-theory
papers: 39
---

## 今日必读 / Must Read Today

### 1. [[2604.08271]] An Illusion of Unlearning? Assessing Machine Unlearning Through Internal Representations

**推荐理由 / why-read:** 这篇直击 LLM/模型可靠性核心：主流机器遗忘方法（NegGrad+、SalUn、SCRUB、UNSIR）虽把遗忘类输出精度降到 0%，但冻结特征上线性探针即可恢复约 92% 精度——遗忘只发生在分类器头、特征表示里信息仍在。作者用 Neural Collapse 下的特征-分类器错配诊断根因，并提出 CMF 分类器强制特征对齐，使特征级遗忘精度远低于 Retrain 基线。对任何依赖"已遗忘"声明的安全/合规场景，这是必须知道的反例。
*Why read:* A direct reliability gut-punch: SOTA machine-unlearning methods drive forget-class output accuracy to 0%, yet a linear probe on frozen features recovers ~92% — unlearning happens only in the classifier head while the representation still leaks the information. The authors diagnose this as feature-classifier misalignment under Neural Collapse and propose CMF to force true feature-level removal (forget acc well below Retrain). Anyone relying on "we unlearned it" claims for safety/compliance needs this counterexample.

### 2. [[2604.08524]] What Drives Representation Steering? A Mechanistic Case Study on Steering Refusal

**推荐理由 / why-read:** 把激活补丁扩展到多 token 引导生成，对 Llama 3.2 3B / Gemma 2 2B 的拒绝引导做机制分析，得到三个对安全编辑与可解释性实践都尖锐的结论：DIM/NTP/PO 三种引导向量产生功能可互换的电路（重叠 ≳90%）；引导主要经 OV 电路传播（冻结全部 QK 注意力分数 ASR 仅降 8.75%，冻结 OV 降 71.75%）；且引导向量可稀疏化 90–99% 仍保留大部分性能，存活维度跨方法显著共享。给"引导向量到底在改什么"一个机制级答案。
*Why read:* Extends activation patching to multi-token steered generation and gives mechanistic answers practitioners need: three steering-vector methods (DIM/NTP/PO) yield functionally interchangeable circuits (≳90% overlap); steering propagates mainly through the OV circuit (freezing all QK scores drops ASR only 8.75% vs. 71.75% for OV); and steering vectors sparsify 90–99% with shared surviving dimensions across methods — a mechanism-level account of what steering actually changes.

### 3. [[2604.08510]] What Do Language Models Learn and When? The Implicit Curriculum Hypothesis

**推荐理由 / why-read:** 提出"隐式课程假说"——预训练中技能以跨模型一致、尊重组合依赖的顺序涌现。用 91 个可组合任务在 9 个模型（410M–13B，4 个家族）上验证：涌现顺序 Spearman ρ=.81（45 对模型，p<10⁻⁷），组合任务不早于其组件出现；并用 function vector 表示空间留一预测 held-out 组合任务的训练轨迹（R²=.68–.84）。把"模型什么时候学会什么"从黑箱变成可预测的结构，对训练监控与课程设计都有直接意义。
*Why read:* Proposes the Implicit Curriculum Hypothesis — skills emerge during pretraining in a stable, compositional order consistent across models. Across 91 composable tasks and 9 models (410M–13B, 4 families), emergence orderings correlate at Spearman ρ=.81 (45 model pairs, p<10⁻⁷), composite tasks emerge no earlier than their parents, and function-vector similarity predicts held-out composite training trajectories (R²=.68–.84). Turns "what the model learns when" from a black box into predictable structure, directly relevant to training monitoring and curriculum design.

---

## 按主题分类 / Papers by Topic

### 可解释性与机制分析 / Interpretability & Mechanistic Analysis

| Paper | Short Title 简称 | Key Contribution 核心贡献 |
|-------|------------------|---------------------------|
| [[2604.08271]] | Illusion of Unlearning 遗忘幻象 / Unlearning via Internal Representations | 线性探针可从"已遗忘"特征恢复 ~92% 精度；CMF 强制特征级真遗忘。Linear probe recovers ~92% from "unlearned" features; CMF forces true feature-level removal. |
| [[2604.08524]] | Steering Refusal Mechanism 拒绝引导机制 / Mechanistic Case Study on Steering | 多 token 补丁显示引导经 OV 电路传播，向量可稀疏化 90–99%。Multi-token patching shows steering propagates via OV circuit; vectors sparsify 90–99%. |
| [[2604.07615]] | ADAG 归因图描述 / Automated Attribution Graph Descriptions | 首个全自动归因图描述管道，无人工复现多跳推理电路并定位越狱特征簇。First fully automated attribution-graph description pipeline; recovers multi-hop circuit and locates jailbreak feature clusters. |
| [[2604.08284]] | DMLE 规则知识编辑 / Distributed Multi-Layer Editing | 因果追踪揭示规则知识按形式分层，DMLE 实例可移植性 +13.91pp、规则理解 +50.19pp。Causal tracing shows form-specific layering; DMLE improves instance portability +13.91pp, rule understanding +50.19pp. |
| [[2604.08039]] | LINE 视觉神经元解释 / LLM-based Iterative Neuron Explanations | 训练无关黑盒迭代框架，AUC 提升最多 0.18，发现 29% 词表遗漏概念。Training-free black-box iterative pipeline; AUC +0.18, discovers 29% missed concepts. |
| [[2604.08335]] | Frozen LLM Feedforward Graph 冻结LLM前馈图 / Dead Weights, Live Signals | 异构冻结 LLM 组成前馈图，仅训 17.6M 投影参数，ARC-C 达 87.3%。Heterogeneous frozen LLMs as feedforward graph; 17.6M trainable params, ARC-C 87.3%. |
| [[2604.07886]] | LHE 层级线性编码 / Linear Hierarchical Hierarchies | 为每层学线性变换映射子→父概念，层级关系因果可导且编码在 ~150–250 维子空间。Learns linear transforms mapping child→parent; hierarchy causally steerable in ~150–250d subspace. |
| [[2604.07766]] | Sensitivity-Positional Co-Localization 敏感层与RoPE反共定位 / GQA Transformer Layer Localization | 任务敏感层与 RoPE 影响层强反共定位（rs=−0.735），但同层施加仍最优。Sensitive layers and RoPE-influential layers anti-colocalize (rs=−0.735); co-applying still optimal. |
| [[2604.08192]] | Inside-Out 电路泛化度量 / Measuring ViT Generalization via Inner Workings | 电路导出的 DDB/CSS 度量将 OOD 泛化相关性提升 13.4%/34.1%，静默失效 F1 +45%。Circuit-derived DDB/CSS metrics improve OOD generalization correlation 13.4%/34.1%, silent-failure F1 +45%. |
| [[2604.07382]] | Affective Representations 情感表示 / Latent Structure of Affective Reps | LLM 情感表示与心理学效价-唤醒模型对齐（p<0.05），可用超平面距离做校准 UQ。LLM affective reps align with valence-arousal model (p<0.05); hyperplane distance enables calibrated UQ. |
| [[2604.07855]] | Hidden Inferential Bias 隐式推断偏差 / Biases in Conditioning Autoregressive | 形式化自回归约束生成的隐式偏差，证明精确句子级 MAP 是 NP-hard、条件归一化是 #P-hard。Formalizes hidden inferential bias; exact sentence MAP is NP-hard, conditioned normalization #P-hard. |
| [[2604.07925]] | Sinkhorn Rank Decay 双随机注意力秩坍缩 / Doubly Stochastic Attention Rank Decay | 证明 Sinkhorn 双随机注意力也双指数坍缩到秩一，但经验上比 Softmax 更好保秩。Proves Sinkhorn doubly stochastic attention also collapses to rank-one doubly exponentially; empirically preserves more rank than Softmax. |

### 训练可靠性与动力学 / Training Reliability & Dynamics

| Paper | Short Title 简称 | Key Contribution 核心贡献 |
|-------|------------------|---------------------------|
| [[2604.08510]] | Implicit Curriculum 隐式课程 / Implicit Curriculum Hypothesis | 技能以跨模型一致顺序涌现（ρ=.81），function vector 预测组合任务轨迹 R²=.68–.84。Skills emerge in stable cross-model order (ρ=.81); function vectors predict composite trajectories R²=.68–.84. |
| [[2604.07569]] | Learning is Forgetting 训练即有损压缩 / LLM Training As Lossy Compression | OLMo2 预训练验证信息瓶颈两阶段，压缩最优性预测下游性能（r=0.52）。OLMo2 pretraining follows IB two-phase; compression optimality predicts downstream performance (r=0.52). |
| [[2604.07380]] | Spectral Edge Lifecycle 谱边缘生命周期 / Spectral Edge: Gradient to Weight-Decay | grokking 时谱边缘从梯度驱动翻转为 WD 驱动压缩轴，消融灾难性敏感 >4000×。Spectral edge flips gradient→WD-driven at grok; ablation-critical, >4000× sensitive vs random. |
| [[2604.07405]] | Conservation Law Breaking 守恒律破缺 / Spectral Theory of Non-Convex Optimization | 推导离散 GD 下守恒律以 η^α 破缺，交叉熵 24× 压缩 Hessian 谱。Derives conservation-law breaking as η^α; cross-entropy compresses Hessian spectrum 24×. |
| [[2604.07603]] | Implicit Regularization 隐式正则 / Overparameterized Generalization | 统一框架检验五种泛化解释，小 batch 测试准确率高 2.25pp、Hessian 曲率差 11.8×。Unified framework tests 5 generalization explanations; small batch +2.25pp acc, 11.8× Hessian curvature. |
| [[2604.07822]] | Recurrent-Depth Reasoning 循环深度推理 / Implicit Reasoning in Looped Transformers | 循环深度 Transformer 经三阶段 grokking 实现系统性泛化，vanilla 完全失败。Recurrent-depth transformers achieve systematic generalization via 3-stage grokking; vanilla fails. |
| [[2604.07963]] | DoGraph 数据混合 / Rethinking Data Mixing via Gradient Geometry | 域差异=梯度 MMD，图约束权重使 SlimPajama 困惑度降到 3.09（vs Uniform 4.13）。Domain difference = gradient MMD; graph-constrained weights cut SlimPajama PPL to 3.09 vs 4.13. |

### 量化与压缩 / Quantization & Compression

| Paper | Short Title 简称 | Key Contribution 核心贡献 |
|-------|------------------|---------------------------|
| [[2604.07888]] | Bit-by-Bit 渐进QAT / Progressive QAT for Low-Bit LLMs | 分块精度退火+离群通道切分，LLaMA-2 7B W2A2 仅 +2.25 PPL，token 预算少 3600×。Block-wise annealing + OCS; LLaMA-2 7B W2A2 +2.25 PPL, 3600× fewer tokens. |
| [[2604.07955]] | Compensation-Aware Residual 补偿感知残差 / Rethinking Residual Errors in Quantization | 重定义残差为层间+层内补偿感知误差，Llama2-7B 3-bit C4 PPL 13.60→8.34。Redefines residual as inter+intra-layer compensation-aware error; Llama2-7B 3-bit C4 PPL 13.60→8.34. |
| [[2604.08118]] | OA-EM 码本初始化 / Output-Aware EM for AQLM | 初始化决定优化盆地，OA-EM 比 greedy b=16 快 2.8× 还更好。Initialization determines basin; OA-EM 2.8× faster than greedy b=16 with better quality. |
| [[2604.07853]] | QaRL 量化感知RL / Rollout-Aligned Quantization-Aware RL | 训练侧前向与量化 rollout 对齐+TBPO，Qwen3-30B MoE 数学 51.2 接近 BF16 52.1。Aligns learner forward with quantized rollout + TBPO; Qwen3-30B MoE math 51.2 vs BF16 52.1. |
| [[2604.07663]] | SAGE 符号自适应优化器 / Sign-Adaptive Gradient for LLMs | O(d) 有界阻尼驯服嵌入稀疏梯度，1.3B PPL 24.33 vs AdamW 27.81，显存 9.83→0.98GB。O(d) bounded damper tames sparse embedding grads; 1.3B PPL 24.33 vs 27.81, memory 9.83→0.98GB. |
| [[2604.08474]] | FL Gradient Quantization 联邦学习量化 / Quantization in FL for Aerospace | INT4 与 FP32 统计无差异且 8× 降通信，INT2 是过正则假象。INT4 statistically parity with FP32 and 8× less communication; INT2 is over-regularization artifact. |

### 训练效率与微调 / Training Efficiency & Fine-tuning

| Paper | Short Title 简称 | Key Contribution 核心贡献 |
|-------|------------------|---------------------------|
| [[2604.07808]] | GRASS 层重要性采样 / Gradient-based Adaptive Layer Sampling | 平均梯度范数动态采样+层粒度 offloading，精度 +4.38pp、峰值显存 −19.97%。MGN dynamic sampling + layer-wise offloading; +4.38pp acc, −19.97% peak memory. |
| [[2604.07397]] | Data Warmup 扩散课程 / Complexity-Aware Curricula for Diffusion | DINO-v2 复杂度评分+温度退火，ImageNet-256 IS +6.11、FID −3.41。DINO-v2 complexity scoring + temperature annealing; ImageNet-256 IS +6.11, FID −3.41. |
| [[2604.07402]] | Local Optimization+ReCo 视频生成训练 / Accelerating AR Video Training | 窗口内优化+Lipschitz 连续性约束，~2× 训练加速，FFS FVD 42.5。Window optimization + Lipschitz continuity; ~2× speedup, FFS FVD 42.5. |
| [[2604.07658]] | PoST 谱衰减锥化 / Optimal Decay Spectra for Linear Recurrences | 谱重参数化+位置自适应缩放，零开销改善 Mamba-2 MQAR 54.2→61.0。Spectral reparam + position-adaptive scaling; zero-overhead, Mamba-2 MQAR 54.2→61.0. |

### 推理与评估 / Inference & Evaluation

| Paper | Short Title 简称 | Key Contribution 核心贡献 |
|-------|------------------|---------------------------|
| [[2604.08075]] | Dual-Pool Token Routing 双池路由 / Cost-Efficient LLM Serving | 短/长上下文双池按 token 预算分发，GPU-hours −31–42%、抢占 −5.4×。Short/long-context dual-pool routing; GPU-hours −31–42%, preemption −5.4×. |
| [[2604.07737]] | SepSeq 数值序列分隔 / Training-Free Long Numerical Sequence Processing | 每 k token 插分隔符作注意力汇，9 LLM 平均准确率 +35.6%、token −16.4%。Insert separator every k tokens as attention sink; +35.6% acc, −16.4% tokens. |
| [[2604.07931]] | ProD 长度预测 / Robust Length Prediction | 把长度预测重定义为重尾分布鲁棒估计，MAE 较 SOTA 降最多 25%。Reframes length prediction as robust heavy-tailed estimation; MAE −25% vs SOTA. |
| [[2604.07801]] | TEMPER 情感扰动推理 / Emotional Perturbation in Quantitative Reasoning | 仅改情感基调即降准确率 2–10pp，中和化恢复 ~70% 损失。Emotional framing alone drops accuracy 2–10pp; neutralization recovers ~70%. |

### 表示几何与理论 / Representation Geometry & Theory

| Paper | Short Title 简称 | Key Contribution 核心贡献 |
|-------|------------------|---------------------------|
| [[2604.07363]] | Benchmark Shadows 基准阴影 / Data Alignment & Parameter Footprints | 受控数据干预证明频率集中型数据留持久谱签名，与跨基准非对称能力一致。Controlled data interventions show frequency-concentrated data leaves persistent spectral signatures aligned with asymmetric capability. |
| [[2604.08492]] | Node Embedding Dimensionality 节点嵌入维度稳定性 / Stability of Node Embeddings | 五种方法稳定性随维度呈方法依赖模式，最高稳定性未必对应最优性能。Stability-vs-dimension is method-dependent; max stability ≠ optimal performance. |

### 应用与其他 / Applications & Other

| Paper | Short Title 简称 | Key Contribution 核心贡献 |
|-------|------------------|---------------------------|
| [[2604.07393]] | DSPR 双流物理残差 / Trustworthy Industrial Time Series Forecasting | 统计趋势流+物理感知残差流，四基准 SOTA 且物理保真度 MCA>99%。Statistical trend + physics-aware residual stream; SOTA with MCA>99% physical fidelity. |
| [[2604.08357]] | Bias-Constrained Diffusion 偏差约束扩散 / PDE Emulation Schedules | 自适应噪声调度+代理展开训练，Kolmogorov 流 FSD 改善数个数量级。Adaptive noise schedule + proxy unrolled training; Kolmogorov FSD improved by orders of magnitude. |
| [[2604.08333]] | Medical MLLM Degradation 医疗MLLM性能退化 / Lost in the Hype | 逐模块特征探针诊断 14 个医疗 MLLM 四种失效模式，提出 FHS。Module-by-module probing diagnoses 4 failure modes in 14 medical MLLMs; introduces FHS. |
| [[2604.07527]] | TIC-460388167 PCEB 发现 / Nearby Post-Common-Envelope Binary | 发现近邻食双星 PCEB，白矮星 7607K 属最冷之列，首次给出伴星速率分辨自转轮廓。Discovery of nearby PCEB; 7607K WD among coolest; first velocity-resolved companion rotation profile. |

---

## All Papers

| # | Paper | Title |
|---|-------|-------|
| 1 | [[2604.07363]] | Benchmark Shadows: Data Alignment, Parameter Footprints, and Generalization in Large Language Models |
| 2 | [[2604.07380]] | The Lifecycle of the Spectral Edge: From Gradient Learning to Weight-Decay Compression |
| 3 | [[2604.07382]] | Latent Structure of Affective Representations in Large Language Models |
| 4 | [[2604.07393]] | DSPR: Dual-Stream Physics-Residual Networks for Trustworthy Industrial Time Series Forecasting |
| 5 | [[2604.07397]] | Data Warmup: Complexity-Aware Curricula for Efficient Diffusion Training |
| 6 | [[2604.07402]] | Accelerating Training of Autoregressive Video Generation Models via Local Optimization with Representation Continuity |
| 7 | [[2604.07405]] | Conservation Law Breaking at the Edge of Stability: A Spectral Theory of Non-Convex Neural Network Optimization |
| 8 | [[2604.07527]] | Searching for GEMS: Discovery of the Nearby Post-Common-Envelope Binary System TIC-460388167 |
| 9 | [[2604.07569]] | Learning is Forgetting: LLM Training As Lossy Compression |
| 10 | [[2604.07603]] | Implicit Regularization and Generalization in Overparameterized Neural Networks |
| 11 | [[2604.07615]] | ADAG: Automatically Describing Attribution Graphs |
| 12 | [[2604.07658]] | Optimal Decay Spectra for Linear Recurrences |
| 13 | [[2604.07663]] | SAGE: Sign-Adaptive Gradient for Memory-Efficient LLM Optimization |
| 14 | [[2604.07737]] | SepSeq: A Training-Free Framework for Long Numerical Sequence Processing in LLMs |
| 15 | [[2604.07766]] | Sensitivity-Positional Co-Localization in GQA Transformers |
| 16 | [[2604.07801]] | TEMPER: Testing Emotional Perturbation in Quantitative Reasoning |
| 17 | [[2604.07808]] | GRASS: Gradient-based Adaptive Layer-wise Importance Sampling for Memory-efficient Large Language Model Fine-tuning |
| 18 | [[2604.07822]] | Loop, Think, & Generalize: Implicit Reasoning in Recurrent-Depth Transformers |
| 19 | [[2604.07853]] | QaRL: Rollout-Aligned Quantization-Aware RL for Fast and Stable Training under Training–Inference Mismatch |
| 20 | [[2604.07855]] | Hidden Biases in Conditioning Autoregressive Models |
| 21 | [[2604.07886]] | Linear Representations of Hierarchical Concepts in Language Models |
| 22 | [[2604.07888]] | Bit-by-Bit: Progressive QAT Strategy with Outlier Channel Splitting for Stable Low-Bit LLMs |
| 23 | [[2604.07925]] | Sinkhorn Doubly Stochastic Attention Rank Decay Analysis |
| 24 | [[2604.07931]] | Robust Length Prediction: A Perspective from Heavy-Tailed Prompt-Conditioned Distributions |
| 25 | [[2604.07955]] | Rethinking Residual Errors in Compensation-based LLM Quantization |
| 26 | [[2604.07963]] | Rethinking Data Mixing from the Perspective of Large Language Models |
| 27 | [[2604.08039]] | LINE: LLM-based Iterative Neuron Explanations for Vision Models |
| 28 | [[2604.08075]] | Dual-Pool Token-Budget Routing for Cost-Efficient and Reliable LLM Serving |
| 29 | [[2604.08118]] | Initialisation Determines the Basin: Efficient Codebook Optimisation for Extreme LLM Quantization |
| 30 | [[2604.08192]] | Inside-Out: Measuring Generalization in Vision Transformers Through Inner Workings |
| 31 | [[2604.08271]] | An Illusion of Unlearning? Assessing Machine Unlearning Through Internal Representations |
| 32 | [[2604.08284]] | Distributed Multi-Layer Editing for Rule-Level Knowledge in Large Language Models |
| 33 | [[2604.08333]] | Lost in the Hype: Revealing and Dissecting the Performance Degradation of Medical Multimodal Large Language Models in Image Classification |
| 34 | [[2604.08335]] | Dead Weights, Live Signals: Feedforward Graphs of Frozen Language Models |
| 35 | [[2604.08357]] | Bias-Constrained Diffusion Schedules for PDE Emulations: Reconstruction Error Minimization and Efficient Unrolled Training |
| 36 | [[2604.08474]] | Quantization Impact on the Accuracy and Communication Efficiency Trade-off in Federated Learning for Aerospace Predictive Maintenance |
| 37 | [[2604.08492]] | The Impact of Dimensionality on the Stability of Node Embeddings |
| 38 | [[2604.08510]] | What Do Language Models Learn and When? The Implicit Curriculum Hypothesis |
| 39 | [[2604.08524]] | What Drives Representation Steering? A Mechanistic Case Study on Steering Refusal |
