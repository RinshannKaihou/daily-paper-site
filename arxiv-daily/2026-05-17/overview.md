---
title: "Daily Paper Overview — 2026-05-17"
date: 2026-05-17
tags:
  - daily-papers
  - arxiv
  - research-digest
papers: 28
---

## 今日必读 / Must Read Today

### 1. [[2605.17295]] DISA: Offline Importance Sampling for Distribution-Matching LLM-RL

> **推荐理由：** 将分布匹配RL中的配分函数估计从在线训练中解耦，通过离线重要性采样预先冻结配分函数，解决了FlowRL等方法的策略-配分函数耦合问题，在6个数学+3个代码基准上匹配或超越现有方法，多样性保留远超GRPO。
>
> **Why read:** Decouples partition-function estimation from policy learning in distribution-matching RL via offline importance sampling, eliminating the error-coupling that plagues online methods, while matching or beating FlowRL/GRPO across 9 benchmarks with superior diversity retention.

### 2. [[2605.17613]] VeriCache: Turning Lossy KV Cache into Lossless LLM Inference

> **推荐理由：** 首个将有损KV缓存压缩转化为无损推理的框架，利用压缩KV作为投机解码draft并通过跨资源交错调度，在保证输出与全量KV完全一致的前提下实现最高4.26倍吞吐提升，支持7种压缩方法。
>
> **Why read:** First framework to make KV cache compression lossless by drafting from compressed KV and verifying against off-GPU full KV, achieving up to 4.26X throughput with bit-identical outputs across 7 compressors and 3 models.

### 3. [[2605.17672]] PUMA: Stop When Reasoning Converges — Semantic-Preserving Early Exit

> **推荐理由：** 提出推理级语义冗余检测实现CoT早退出，发现LRM中41–52%的token生成于最终答案之后，PUMA通过微调的冗余检测器+答案验证在5个模型上平均减少26.2% token，准确率不降反升，保留推理链质量最优。
>
> **Why read:** Identifies that 41–52% of LRM tokens are wasted post-answer redundancy; uses a contrastive-trained redundancy detector plus answer verification for plug-and-play early exit, achieving 26.2% token reduction with preserved/improved accuracy and highest retained CoT quality.

---

## 按主题分类 / Papers by Topic

### LLM 强化学习与训练优化 / LLM RL & Training Optimization

| Paper | 一句话描述 / One-line Description |
|-------|----------------------------------|
| [[2605.17295]] DISA | 离线重要性采样解耦配分函数估计，解决分布匹配RL中策略-配分函数耦合问题 / Offline IS decouples partition-function estimation, solving policy-Z coupling in distribution-matching RL |
| [[2605.17497]] SSOPD | 利用GRPO组内正确-错误对比实现自监督过程蒸馏，无需外部解答 / Self-supervised process distillation from intra-group correct-wrong contrast without external solutions |
| [[2605.17570]] μ-GRPO | 揭示GRPO可容忍极高过期数据（μ=1024），通过负优势否决实现约2倍加速 / GRPO tolerates extreme staleness (μ=1024) via negative-advantage veto for ~2X speedup |
| [[2605.17342]] HRC-DSPPO | 博弈论分解偏好为传递性和循环性分量，配合动态自博弈对齐算法 / Game-theoretic decomposition of preferences into transitive and cyclic components with dynamic self-play alignment |

### 训练理论与动力学 / Training Theory & Dynamics

| Paper | 一句话描述 / One-line Description |
|-------|----------------------------------|
| [[2605.17606]] NTK for Classification | 将NTK理论从回归扩展到分类，证明参数正则化或标签平滑可保持惰性训练区间 / Extends NTK from regression to classification; regularization or label smoothing preserves lazy training regime |
| [[2605.17660]] Infinitely Deep/Wide Transformers | 均值场极限下将无限深宽Transformer训练建模为神经PDE最优控制，证明梯度流线性收敛 / Mean-field neural PDE formulation for infinite transformers with proven linear convergence of gradient flow |
| [[2605.17659]] Bug or Feature² | 严格证明标准损失与正偏置激活函数导致负权重漂移，发现~70%稀疏度处精度断崖 / Proves negative weight drift from loss-activation interaction; identifies ~70% sparsity accuracy cliff |

### 高效推理与压缩 / Efficient Inference & Compression

| Paper | 一句话描述 / One-line Description |
|-------|----------------------------------|
| [[2605.17613]] VeriCache | 压缩KV作为draft+全量KV验证，实现无损KV缓存推理，最高4.26X加速 / Lossless KV cache inference via compressed-KV drafting with full-KV verification, up to 4.26X speedup |
| [[2605.17289]] LEAP | 逐权重Bernoulli-Gumbel-sigmoid松弛实现端到端非结构化剪枝，50/60%稀疏度下超越ADMM / Per-weight Bernoulli relaxation for end-to-end unstructured pruning, beating ADMM at 50-60% sparsity |
| [[2605.17471]] WinQ | Hessian谱分析揭示QAT鞍点停滞，周期性权重插值+噪声注入实现4倍收敛加速 / Hessian analysis reveals QAT saddle-point trapping; weight interpolation + noise injection for 4X convergence speedup |
| [[2605.17524]] Binary Quantization | 坐标异质性决定二元量化质量，统一旋转与保轴两种对立策略的理论框架 / Coordinate heterogeneity governs binary quantization quality, unifying rotation vs axis-preserving strategies |
| [[2605.17672]] PUMA | 推理级语义冗余检测实现CoT早退出，5个模型平均减少26.2% token / Reasoning-level semantic redundancy detection for CoT early exit, 26.2% token reduction across 5 models |

### 机械可解释性与稀疏自编码器 / Mechanistic Interpretability & SAE

| Paper | 一句话描述 / One-line Description |
|-------|----------------------------------|
| [[2605.17204]] Event-Grounded SAE | 运动学事件锚定的SAE可解释性流水线，揭示不同VLA架构的可解释性差异 / Kinematic-event-grounded SAE pipeline revealing architecture-dependent interpretability in VLA policies |
| [[2605.17504]] KL-Minimal Visual MI | 分布视角统一视觉MI方法论，提出EnergyDPS实现忠实性与可解释性最优平衡 / Distributional framework unifying visual MI; EnergyDPS achieves best faithfulness-interpretability tradeoff |
| [[2605.17493]] KAN-SAE | 用KAN可学习B-spline替代SAE的ReLU，在天气模型中发现因果验证的热浪和台风特征 / KAN B-spline activations replace SAE ReLU, discovering causally validated heatwave and typhoon features |
| [[2605.17231]] FishBack | Fisher信息拉回度量揭示激活空间非欧本质，推导闭式最优激活导向方程 / Pullback Fisher metric reveals non-Euclidean activation geometry; derives closed-form optimal steering equation |

### LLM 安全与鲁棒性 / LLM Safety & Robustness

| Paper | 一句话描述 / One-line Description |
|-------|----------------------------------|
| [[2605.17329]] LPG | 10个隐空间token实现策略感知安全审核，84.5%准确率且比显式推理快11倍 / 10 latent tokens for policy-grounded safety moderation at 84.5% accuracy and ~11X faster than explicit reasoning |
| [[2605.17288]] Cascade Failure | 首次揭示LLM级联系统的对抗脆弱性，联合攻击可同时降低准确率84.6%和增加成本148.9% / First systematic study of adversarial vulnerabilities in LLM cascades; joint attack degrades accuracy 84.6% and inflates cost 148.9% |
| [[2605.17413]] Ablating Safety | 将对齐移除建模为效用-风险前沿，任务导向LoRA实现最佳权衡（安全0.87，越界仅0.13）/ Alignment removal as utility-risk frontier; task-only LoRA achieves best tradeoff (security 0.87, spillover 0.13) |

### 表示分析与激活导向 / Representation Analysis & Activation Steering

| Paper | 一句话描述 / One-line Description |
|-------|----------------------------------|
| [[2605.17482]] RSD Word Embeddings | 递归二进制加性分解提取词嵌入语义轴，残差方向作为语义诊断工具 / Recursive binary additive decomposition extracts semantic axes from word embeddings; residuals as diagnostic traces |
| [[2605.17658]] Zero-Shooter Cheats | VLM零样本年龄估计利用"身份捷径"，激活导向抑制身份检索方向可降低MAE最高25.3% / VLMs exploit identity shortcut in age estimation; activation steering suppresses it for up to 25.3% MAE reduction |

### MoE 与多语言 / MoE & Multilingual

| Paper | 一句话描述 / One-line Description |
|-------|----------------------------------|
| [[2605.17598]] MoE for Low-Resource LLMs | 发现MoE模型在低资源语言上出现深层路由崩塌，CPT比SFT更有效纠正路由失衡 / Deep-layer routing collapse in MoE for low-resource languages; CPT outperforms SFT for routing correction |

### 高效视觉模型 / Efficient Vision Models

| Paper | 一句话描述 / One-line Description |
|-------|----------------------------------|
| [[2605.17633]] SparseSAM | Z-order排列+残差一致性路由实现SAM无训练结构化稀疏化，2X加速仅损失0.004 mIoU / Training-free structured sparsification of SAM via Z-order permutation; 2X speedup with 0.004 mIoU loss |

### 硬件加速 / Hardware Acceleration

| Paper | 一句话描述 / One-line Description |
|-------|----------------------------------|
| [[2605.17683]] μ-ORCA | AIE阵列内512-bit级联直通通信实现0.93μs端到端DNN推理，满足高能物理1μs约束 / 512-bit cascade inter-layer communication in AIE array achieves 0.93μs DNN inference for jet-tagging |

### 联邦学习与隐私 / Federated Learning & Privacy

| Paper | 一句话描述 / One-line Description |
|-------|----------------------------------|
| [[2605.17552]] Q-LocalAdam | 分布感知8比特量化Adam优化器状态，3.37倍内存缩减，极端非IID下反而提升5.74pp / Distribution-aware 8-bit quantized Adam for FL; 3.37X memory reduction, +5.74pp under extreme non-IID |
| [[2605.17432]] DP-SelFT | 差分隐私合成数据驱动的层级选择，最坏情况扰动评估选择抗噪能力最强的层 / DP synthetic-data-driven layer selection with worst-case perturbation for robust DP fine-tuning |

### 基础模型评估 / Foundation Model Evaluation

| Paper | 一句话描述 / One-line Description |
|-------|----------------------------------|
| [[2605.17562]] EEG Foundation Models | 首次系统评估6个EEG基础模型的鲁棒性、可解释性和表达能力，发现池化策略是性能关键 / First systematic benchmark of 6 EEG FMs across robustness, interpretability, expressiveness; pooling strategy is key |

### 优化理论 / Optimization Theory

| Paper | 一句话描述 / One-line Description |
|-------|----------------------------------|
| [[2605.17692]] CP Lifting for Linear Nets | 完全正锥提升实现深层线性网络训练的精确凸优化重构，提升维度与深度和数据量无关 / Exact convex reformulation of deep linear network training via completely positive lifting; dimension independent of depth and data |

---

## All Papers

| # | ID | Title | Topics |
|---|----|-------|--------|
| 1 | [[2605.17204]] | Event-Grounded Sparse Autoencoders for VLA Policies | mechanistic-interpretability, SAE, robot-learning |
| 2 | [[2605.17231]] | FishBack: Pullback Fisher Geometry for Activation Steering | activation-steering, Fisher-information, interpretability |
| 3 | [[2605.17288]] | When Efficiency Backfires: Cascade Failure under Adversarial Attack | LLM-cascade, adversarial-attack, system-security |
| 4 | [[2605.17289]] | LEAP: Learnable End-to-End Adaptive Pruning of LLMs | llm-pruning, unstructured-sparsity, model-compression |
| 5 | [[2605.17295]] | DISA: Offline Importance Sampling for Distribution-Matching LLM-RL | reinforcement-learning, distribution-matching, LLM-reasoning |
| 6 | [[2605.17329]] | LPG: Latent Policy Guardrails | LLM-safety, latent-reasoning, guardrails |
| 7 | [[2605.17342]] | Transitivity Meets Cyclicity: HRC-DSPPO | RLHF, preference-modeling, game-theory |
| 8 | [[2605.17413]] | Ablating Safety: Mechanisms for Removing Alignment | llm-safety, mechanistic-interpretability, representation-engineering |
| 9 | [[2605.17432]] | DP-SelFT: Differentially Private Selective Fine-Tuning | differential-privacy, LLM-fine-tuning, privacy-utility-tradeoff |
| 10 | [[2605.17471]] | WinQ: Accelerating QAT Around Saddle Points | quantization-aware-training, Hessian-analysis, LLM-compression |
| 11 | [[2605.17482]] | Residual Semantic Decomposition of Word Embeddings | word-embeddings, semantic-decomposition, interpretability |
| 12 | [[2605.17493]] | KAN-SAE: Climate Features in AI Weather Models | mechanistic-interpretability, SAE, weather-prediction |
| 13 | [[2605.17497]] | SSOPD: Self-Supervised On-Policy Distillation for Reasoning LMs | RLVR, knowledge-distillation, mathematical-reasoning |
| 14 | [[2605.17504]] | KL-Minimal Visual Mechanistic Interpretability | mechanistic-interpretability, vision-models, diffusion-models |
| 15 | [[2605.17524]] | Coordinate Heterogeneity Governs Binary Quantization | binary-quantization, contrastive-learning, vector-search |
| 16 | [[2605.17552]] | Q-LocalAdam: Memory-Efficient FL Optimization | federated-learning, optimization, quantization |
| 17 | [[2605.17562]] | Beyond Accuracy: EEG Foundation Models | EEG, foundation-models, robustness, interpretability |
| 18 | [[2605.17570]] | μ-GRPO: How Off-Policy Can GRPO Be? | reinforcement-learning, GRPO, RLVR, training-efficiency |
| 19 | [[2605.17598]] | MoE for Low-Resource LLMs | mixture-of-experts, multilingual-LLM, routing-dynamics |
| 20 | [[2605.17606]] | NTK for Classification | neural-tangent-kernel, classification-theory, generalization |
| 21 | [[2605.17613]] | VeriCache: Lossless KV Cache Inference | kv-cache, lossless-inference, speculative-decoding, llm-serving |
| 22 | [[2605.17633]] | SparseSAM: Structured Sparsification of SAM | model-compression, segmentation, efficient-inference |
| 23 | [[2605.17658]] | When a Zero-Shooter Cheats: Age Estimation via Activation Steering | vlm-robustness, activation-steering, interpretability |
| 24 | [[2605.17659]] | Bug or Feature²: Weight Drift, Activation Sparsity, and Spikes | optimization, activation-functions, training-dynamics |
| 25 | [[2605.17660]] | Training Infinitely Deep and Wide Transformers | neural-pde, mean-field-theory, transformer-theory |
| 26 | [[2605.17672]] | PUMA: Semantic-Preserving Early Exit for Reasoning Models | early-exit, chain-of-thought, reasoning-efficiency |
| 27 | [[2605.17683]] | μ-ORCA: Microsecond DNN Inference on ACAP | hardware-accelerator, ultra-low-latency-inference, heterogeneous-computing |
| 28 | [[2605.17692]] | Exact Convex Reformulations via Completely Positive Lifting | convex-optimization, linear-neural-networks, optimization-theory |
