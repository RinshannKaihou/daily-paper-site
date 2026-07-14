---
title: "arXiv Daily — 2026-05-13"
date: 2026-05-13
tags: [daily-overview]
papers: 50
---

# arXiv Daily — 2026-05-13

> 50 篇论文，涵盖优化器理论、量化方法、可解释性、强化学习训练、MoE 系统、架构创新等方向。
> 50 papers covering optimizer theory, quantization, interpretability, RL training, MoE systems, architecture innovation, and more.

---

## 今日必读 / Must Read Today

### 1. [[2605.12426]] Geometric Factual Recall in Transformers

**为什么必读：** 从理论上证明 Transformer 仅需 O(R log N) 维嵌入即可通过线性叠加 + ReLU 门控实现事实记忆，MLP 并非传统的键值存储，而是关系条件选择器——从根本上重新理解 Transformer 的知识存储机制。

**Why must-read:** Proves Transformers memorize facts via O(R log N) linear superposition with ReLU-gated selection, not key-value associative memory—fundamentally reinterprets how Transformers store knowledge, with zero-shot transfer to unseen mappings and CoT complexity analysis for multi-hop reasoning.

### 2. [[2605.11775]] Entropy Polarity in Reinforcement Fine-Tuning (PAPO)

**为什么必读：** 提出 token 级熵极性理论（P = A·T），揭示 RLVR 中熵收缩的结构性不对称性，并据此设计 PAPO 算法在数学推理和智能体任务上一致超越 DAPO——对理解与控制 RLVR 训练动态有直接实践价值。

**Why must-read:** Introduces entropy polarity P = A·T at the token level, reveals structural asymmetry causing entropy collapse in RLVR, and proposes PAPO that consistently outperforms DAPO on math reasoning (+3.3% AIME24) and agentic benchmarks—directly practical for controlling RLVR training dynamics.

### 3. [[2605.11181]] Muon is Not That Special: Random or Inverted Spectra Work Just as Well

**为什么必读：** 提出用随机噪声替代奇异值的 Kaon 优化器竟能匹敌 Muon，证明 Muon 的成功并非源于精确的谱几何结构，而是批次梯度对齐度和下降潜力的交互——颠覆性地重新解释了现代优化器的成功机制。

**Why must-read:** Kaon replaces gradient singular values with chaotic random noise yet matches Muon, debunking the geometric explanation for Muon's success. Performance is governed by gradient alignment (γ) and descent potential (Φ), not spectral geometry—a paradigm-shifting insight for optimizer design.

---

## 按主题分类 / Papers by Topic

### 优化器与训练理论 / Optimizers & Training Theory

| Paper | Title (EN) | 核心要点 / Key Takeaway |
|-------|-----------|----------------------|
| [[2605.11172]] | SODA: Optimistic Dual Averaging Unifies Modern Optimizers | 将 Muon/Lion/NAdam 统一为乐观对偶平均框架，提供免调参的 1/(k+2) 权重衰减调度 / Unifies Muon, Lion, NAdam under Optimistic Dual Averaging with parameter-free weight decay schedule |
| [[2605.11181]] | Muon is Not That Special (Freon/Kaon) | 随机奇异值的 Kaon 匹敌 Muon，成功来自梯度对齐而非谱几何 / Kaon with random singular values matches Muon; success is from gradient alignment, not spectral geometry |
| [[2605.11316]] | Error Whitening: Why Gauss-Newton Outperforms Newton | GN 通过消除参数化扭曲实现"误差白化"，在回归/PINN/RL 上超越 Adam/Muon 数量级 / Gauss-Newton removes parameterization distortion via error whitening, orders-of-magnitude improvement |
| [[2605.11838]] | Spectral Clipping for Matrix-Valued Gradients | SVD 分解梯度矩阵截断奇异值，重尾噪声下理论最优收敛 / Truncate singular values via SVD, optimal convergence under heavy-tailed noise |
| [[2605.12492]] | Pion: Spectrum-Preserving Optimizer | 正交等价变换保持奇异值不变，无归一化层下仍稳定收敛 / Bilateral orthogonal transforms preserve singular values; stable without normalization |
| [[2605.11396]] | MuonQ: 4-bit Muon Quantization | 预归一化+结构分解+μ律压扩实现 Muon 4 位量化，显存降 7.3× / 4-bit Muon states via pre-norm + structural decomposition + μ-law, 7.3× memory saving |
| [[2605.11059]] | Uniform Scaling Limits in AdamW Transformers | 隐藏状态动力学收敛到 McKean-Vlasov ODE，界不依赖 token 数 / Hidden-state dynamics converge to McKean-Vlasov ODEs, bounds independent of token count |
| [[2605.11570]] | OUI as a Structural Observable | 过拟合-欠拟合指标作为训练的结构可观测量，收敛前揭示训练质量 / OUI as structural observable reveals training quality before convergence |
| [[2605.12394]] | Correlation Traps (Random Matrix Theory) | 随机矩阵谱异常检测过拟合，发现 grokking 后的"反 grokking"阶段 / Marchenko-Pastur outliers detect overfitting; post-grokking "anti-grokking" phase discovered |

### 量化方法 / Quantization Methods

| Paper | Title (EN) | 核心要点 / Key Takeaway |
|-------|-----------|----------------------|
| [[2605.11222]] | ADMM-Q: Hessian-based Weight Quantizer | ADMM 交替优化替代 GPTQ 贪心列量化，Qwen3-8B W3A16 PPL 12.85→10.06 / ADMM alternation replaces GPTQ greedy columns; W3A16 PPL 12.85→10.06 on Qwen3-8B |
| [[2605.12327]] | Grid Games: Multiple Grids for 4-bit Quantization | 每 16 数值从多网格选最优，PO2(Split87) 精度恢复率 97.85% / Per-block grid selection; PO2(Split87) achieves 97.85% accuracy recovery |
| [[2605.12245]] | SOAR: Scale Optimization for NVFP4 | 闭式联合尺度优化+解耦搜索，Qwen3-8B 精度 68.75→70.68 / Closed-form joint scale optimization for NVFP4, accuracy 68.75→70.68 |
| [[2605.12464]] | ScaleSearch: Search Your Block Floating Point Scales | 搜索 NVFP4 最优 scale 降低 27% 量化误差，近无损 FP4 注意力 / Scale search reduces NVFP4 MSE by 27%, near-lossless FP4 attention |
| [[2605.11478]] | FibQuant: Vector Quantization for KV-Cache | 径向-角度向量码本匹配球形-Beta 分布，5×–34× KV 压缩 / Radial-angular codebook for spherical-Beta KV-cache, 5×–34× compression |
| [[2605.10959]] | QuIDE: Quantized Intelligence Trade-off | Intelligence Index I=(C×P)/log₂(T+1) 统一评估三维权衡 / Intelligence Index unifies compression-accuracy-latency evaluation |
| [[2605.10974]] | Vertex-Softmax: Exact Softmax Optimization | softmax 精确最优在约束盒顶点处取得，仅需 K+1 候选 / Exact softmax optimum at constraint box vertices, only K+1 candidates |

### 可解释性与机制分析 / Interpretability & Mechanistic Analysis

| Paper | Title (EN) | 核心要点 / Key Takeaway |
|-------|-----------|----------------------|
| [[2605.12426]] | Geometric Factual Recall in Transformers | 事实通过线性叠加编码，MLP 是 ReLU 门控选择器 / Facts encoded as linear superpositions, MLP is a ReLU-gated selector |
| [[2605.11887]] | Qwen-Scope: SAE as Development Tools | 开源 14 组 SAE，四大应用方向证明 SAE 是模型开发工具 / 14 SAE groups open-sourced, 4 practical applications beyond post-hoc analysis |
| [[2605.12290]] | CNA: Contrastive Neuron Attribution | 0.1% MLP 神经元操控使拒绝率下降 35%–98% / 0.1% MLP neuron ablation drops refusal rate 35–98% |
| [[2605.11426]] | Mechanistic Investigation of SFT | SAE 诊断 SFT：余弦相似 >0.96 但稀疏特征崩塌至 0.557 / SAE diagnostics: cosine >0.96 but sparse features collapse to 0.557 |
| [[2605.11920]] | Domain Restriction via SAE Layer Transitions | SAE 稀疏特征的层间转移建模实现 OOD 检测 / Layer-wise SAE feature transition modeling for OOD detection |
| [[2605.12225]] | Mechanistic Interpretability of ASR via SAE | 首次将 SAE 应用于 Whisper，发现跨语言学单语义特征 / First SAE study on Whisper, monosemantic cross-lingual features discovered |
| [[2605.10971]] | Steering Discrete Diffusion via SAE | 自适应干预调度器实现 93% 三属性同时控制 / Adaptive steering scheduler achieves 93% triple-attribute control |
| [[2605.11203]] | FeatMap: Feature Space Geometry | 语义操作可通过共享线性模型近似，特征空间呈线性子空间结构 / Semantic edits approximated by shared linear models, linear subspace structure |
| [[2605.11392]] | Transformer Interpretability (Attention+Gradient) | 梯度校正方案实现正负注意力分配和像素级类别重写 / Gradient correction enables pos/neg attention and pixel-level category rewriting |
| [[2605.11448]] | Deep Minds and Shallow Probes | 线性探针是仿射不变多项式族的一阶成员，支持零标签跨模型迁移 / Linear probes are degree-1 of affine-invariant polynomial hierarchy, zero-label transfer |
| [[2605.11161]] | Interpretability Can Be Actionable | 可操作性（具体性+验证性）应作为可解释性核心评估标准 / Actionability (concreteness + validation) as core interpretability metric |
| [[2605.11093]] | DMI-Lib: Model-Internal Observability | GPU-CPU 双环形缓冲区，LLM 推理观测仅 0.4%–6.8% 开销 / GPU-CPU ring buffer for LLM observability at 0.4–6.8% overhead |

### 强化学习与策略优化 / Reinforcement Learning & Policy Optimization

| Paper | Title (EN) | 核心要点 / Key Takeaway |
|-------|-----------|----------------------|
| [[2605.11775]] | PAPO: Entropy Polarity in RLVR | 熵极性 P=A·T 揭示结构性不对称，PAPO 超越 DAPO / Entropy polarity reveals structural asymmetry, PAPO outperforms DAPO |
| [[2605.11491]] | OPEFO: On-Policy Entropy Flow Optimization | 自适应平衡熵增/熵减梯度，6 基准最优平均准确率 / Adaptive entropy flow balancing, best average accuracy across 6 benchmarks |
| [[2605.11908]] | Delightful Policy Gradient | 优势×surprisal 门控消除角点自陷，O(1/t) 全局收敛 / Advantage×surprisal gating removes corner trapping, O(1/t) global convergence |
| [[2605.11974]] | DGAO: Dual Group Advantage Optimization | RL 同时优化准确性和排列稳定性，3B–14B 模型均有效 / RL jointly optimizes accuracy and order stability across 3B–14B models |

### MoE 与分布式系统 / MoE & Distributed Systems

| Paper | Title (EN) | 核心要点 / Key Takeaway |
|-------|-----------|----------------------|
| [[2605.11005]] | DisagMoE: Disaggregated AF-Pipe Parallelism | Attention/FFN 解耦到不同 GPU 组，128×H800 上 1.81× 加速 / Attention/FFN disaggregation, 1.81× speedup on 128×H800 |
| [[2605.11800]] | ROMER: Expert Replacement for CIM MoE | 复制高激活专家替换空闲专家，CIM 噪声下 PPL 降低 59.8% / Duplicate top experts into idle slots, 59.8% PPL reduction under CIM noise |
| [[2605.12476]] | Routers Learn the Geometry of Their Experts | 路由器与专家梯度沿同方向累积，负载均衡损失破坏耦合 / Router-expert gradient co-alignment, load-balance loss breaks coupling |
| [[2605.11333]] | MLCommons Chakra | 标准化执行轨迹生态系统，NVIDIA/AMD/Meta 等采用 / Standardized execution trace ecosystem adopted by NVIDIA, AMD, Meta |

### 架构创新 / Architecture Innovation

| Paper | Title (EN) | 核心要点 / Key Takeaway |
|-------|-----------|----------------------|
| [[2605.12466]] | Attractor Model for Language and Reasoning | 循环精修建模为不动点求解，770M 超 1.3B Transformer / Recurrent refinement as fixed-point solving, 770M beats 1.3B Transformer |
| [[2605.11167]] | Bicameral Model: Bidirectional Hidden-State Coupling | 双冻结 LM 通过 1% 参数接口协作，算术 36%→96.5% / Dual frozen LMs via 1% interface, arithmetic 36%→96.5% |
| [[2605.11196]] | Variational Linear Attention (VLA) | 在线正则化最小二乘重构线性注意力，状态范数降 109× / Online regularized least-squares linear attention, 109× lower state norm |
| [[2605.11855]] | CMRU: Parallelizable RNN for Ultra-Low Power | 累积更新恢复梯度流，Pathfinder >90% vs 基线 ~50% / Cumulative update restores gradient flow, Pathfinder >90% vs ~50% baseline |

### 评估方法论 / Evaluation Methodology

| Paper | Title (EN) | 核心要点 / Key Takeaway |
|-------|-----------|----------------------|
| [[2605.11209]] | Five-Nines Reliability | CEM 学习失败分布实现 156× 推理缩减，>99.9% 模型间差异 2.4× / CEM learns failure distribution for 156× inference reduction, 2.4× gap among >99.9% models |
| [[2605.11205]] | Scaling Law of Evaluation Failure | 稀疏度×难度差距交互使简单平均 ρ 降至 0.24，IRT 维持 0.993 / Sparsity×difficulty interaction drops avg ρ to 0.24, IRT maintains 0.993 |
| [[2605.11513]] | Hidden Layer Distillation for LLM Pre-Training | 首个计算等价 HLD 评估，HLD 未持续超越 logit 蒸馏 / First compute-controlled HLD study, HLD does not consistently beat logit KD |

### 理论 / Theory

| Paper | Title (EN) | 核心要点 / Key Takeaway |
|-------|-----------|----------------------|
| [[2605.12190]] | Information-Theoretic Bounds for Sequential Decisions | SCMI 框架将 CMI 泛化界推广到在线学习/主动学习/老虎机 / SCMI extends CMI generalization bounds to sequential decision-making |
| [[2605.11059]] | Uniform Scaling Limits in AdamW Transformers | 隐藏状态动力学收敛到 McKean-Vlasov ODE / Hidden-state dynamics converge to McKean-Vlasov ODEs |
| [[2605.12394]] | Correlation Traps (RMT) | 随机矩阵谱异常检测过拟合，前沿大模型中也发现信号 / Marchenko-Pastur outliers detect overfitting, found in frontier LLMs |

### 安全与对齐 / Safety & Alignment

| Paper | Title (EN) | 核心要点 / Key Takeaway |
|-------|-----------|----------------------|
| [[2605.12199]] | Overtrained, Not Misaligned | 涌现性失调仅出现在少数大模型，可通过早停消除 / Emergent misalignment is rare, mitigated by early stopping |
| [[2605.11836]] | StableEdit: Lifelong Normalization in Model Editing | 贝叶斯递归推断理论，百万级编辑 SOTA / Bayesian recursive tracking theory, SOTA on million-scale edits |

### 系统与能效 / Systems & Energy Efficiency

| Paper | Title (EN) | 核心要点 / Key Takeaway |
|-------|-----------|----------------------|
| [[2605.11999]] | Power Capping Illusion in LLM Decode | 功耗限制在内存受限解码阶段无效，SM 时钟锁定节省 32% 能耗 / Power capping ineffective for decode, SM clock locking saves 32% energy |
| [[2605.11333]] | MLCommons Chakra | 标准化执行轨迹，多公司采用 / Standardized execution traces, multi-company adoption |

### 联邦学习 / Federated Learning

| Paper | Title (EN) | 核心要点 / Key Takeaway |
|-------|-----------|----------------------|
| [[2605.11684]] | Byzantine Federated Conformal Prediction | 30% 参数共享+直方图检测，预测区间紧致 2.2× / 30% parameter sharing + histogram detection, 2.2× tighter intervals |

### 其他 / Other

| Paper | Title (EN) | 核心要点 / Key Takeaway |
|-------|-----------|----------------------|
| [[2605.11525]] | OverNaN: NaN-Aware Oversampling | 保留缺失值结构的过采样框架，NaN 作为信息特征 / Oversampling preserving missingness structure, NaN as informative feature |
| [[2605.11547]] | SharpEuler: Sharpness-Aware Flow Sampling | 离线标定轨迹加速度优化时间步，FLUX FID 90→33 / Offline trajectory acceleration profiling, FLUX FID 90→33 |
| [[2605.10971]] | Steering Discrete Diffusion via SAE | 自适应干预调度器实现 93% 三属性控制 / Adaptive intervention scheduler achieves 93% triple-attribute control |

---

## All Papers

| # | arXiv ID | Title |
|---|----------|-------|
| 1 | [[2605.10959]] | QuIDE: Mastering the Quantized Intelligence Trade-off |
| 2 | [[2605.10971]] | Steering Without Breaking: Discrete Diffusion Steering |
| 3 | [[2605.10974]] | Vertex-Softmax: Tight Transformer Verification |
| 4 | [[2605.11005]] | DisagMoE: Disaggregated MoE Training |
| 5 | [[2605.11059]] | Uniform Scaling Limits in AdamW Transformers |
| 6 | [[2605.11093]] | DMI-Lib: Model-Internal Observability |
| 7 | [[2605.11161]] | Interpretability Can Be Actionable |
| 8 | [[2605.11167]] | Bicameral Model: Bidirectional Hidden-State Coupling |
| 9 | [[2605.11172]] | SODA: Optimistic Dual Averaging Unifies Optimizers |
| 10 | [[2605.11181]] | Muon is Not That Special (Freon/Kaon) |
| 11 | [[2605.11196]] | Variational Linear Attention (VLA) |
| 12 | [[2605.11203]] | FeatMap: Feature Space Geometry |
| 13 | [[2605.11205]] | Scaling Law of Evaluation Failure |
| 14 | [[2605.11209]] | Five-Nines Reliability |
| 15 | [[2605.11222]] | ADMM-Q: Hessian-based Weight Quantizer |
| 16 | [[2605.11316]] | Error Whitening: Why Gauss-Newton Outperforms Newton |
| 17 | [[2605.11333]] | MLCommons Chakra |
| 18 | [[2605.11392]] | Transformer Interpretability (Attention+Gradient) |
| 19 | [[2605.11396]] | MuonQ: 4-bit Muon Quantization |
| 20 | [[2605.11426]] | Mechanistic Investigation of SFT |
| 21 | [[2605.11448]] | Deep Minds and Shallow Probes |
| 22 | [[2605.11478]] | FibQuant: Vector Quantization for KV-Cache |
| 23 | [[2605.11491]] | OPEFO: On-Policy Entropy Flow Optimization |
| 24 | [[2605.11513]] | Hidden Layer Distillation for LLM Pre-Training |
| 25 | [[2605.11525]] | OverNaN: NaN-Aware Oversampling |
| 26 | [[2605.11547]] | SharpEuler: Sharpness-Aware Flow Sampling |
| 27 | [[2605.11570]] | OUI as a Structural Observable |
| 28 | [[2605.11684]] | Byzantine Federated Conformal Prediction |
| 29 | [[2605.11775]] | PAPO: Entropy Polarity in RLVR |
| 30 | [[2605.11800]] | ROMER: Expert Replacement for CIM MoE |
| 31 | [[2605.11836]] | StableEdit: Lifelong Normalization in Model Editing |
| 32 | [[2605.11838]] | Spectral Clipping for Matrix-Valued Gradients |
| 33 | [[2605.11855]] | CMRU: Parallelizable RNN for Ultra-Low Power |
| 34 | [[2605.11887]] | Qwen-Scope: SAE as Development Tools |
| 35 | [[2605.11908]] | Delightful Policy Gradient |
| 36 | [[2605.11920]] | Domain Restriction via SAE Layer Transitions |
| 37 | [[2605.11974]] | DGAO: Dual Group Advantage Optimization |
| 38 | [[2605.11999]] | Power Capping Illusion in LLM Decode |
| 39 | [[2605.12190]] | Information-Theoretic Bounds for Sequential Decisions |
| 40 | [[2605.12199]] | Overtrained, Not Misaligned |
| 41 | [[2605.12225]] | Mechanistic Interpretability of ASR via SAE |
| 42 | [[2605.12245]] | SOAR: Scale Optimization for NVFP4 |
| 43 | [[2605.12290]] | CNA: Contrastive Neuron Attribution |
| 44 | [[2605.12327]] | Grid Games: Multiple Grids for 4-bit Quantization |
| 45 | [[2605.12394]] | Correlation Traps (Random Matrix Theory) |
| 46 | [[2605.12426]] | Geometric Factual Recall in Transformers |
| 47 | [[2605.12464]] | ScaleSearch: Block Floating Point Scale Search |
| 48 | [[2605.12466]] | Attractor Model for Language and Reasoning |
| 49 | [[2605.12476]] | Routers Learn the Geometry of Their Experts |
| 50 | [[2605.12492]] | Pion: Spectrum-Preserving Optimizer |
