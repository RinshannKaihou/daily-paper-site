---
title: "Daily Arxiv Digest — 2026-05-19"
date: 2026-05-19
tags:
  - daily-digest
  - arxiv
papers: 22
---

## 今日必读 / Must Read Today

### 1. [[2605.19461]] DMPO: Distribution-Matching Policy Optimization for Diverse Reasoning

> **推荐理由：** 揭示GRPO等主流RL方法因反向KL散度导致模式坍塌的根本缺陷，提出简洁的分布匹配正则项即可在组合优化和数学推理上获得显著提升 / Diagnoses GRPO's mode collapse as a consequence of reverse KL divergence and proposes DMPO with a lightweight distribution-matching term, achieving 9–12% relative gains on NP-hard tasks and +2.0% on math reasoning.

### 2. [[2605.19775]] Understanding Inference Scaling for LLMs

> **推荐理由：** 首次系统揭示推理型工作负载（长CoT）下KV-cache导致的"容量陷阱"，给出从14B到671B模型的DP→TP拐点与稠密/MoE架构的最优并行策略 / First comprehensive systems characterization revealing the "capacity trap" in reasoning workloads and providing concrete parallelism guidance for models from 8B to 671B parameters.

### 3. [[2605.20005]] FINCH: Fine-Tuning Without Forgetting via Loss-Adaptive Learning Rates

> **推荐理由：** 理论推导出遗忘上界由η·√L决定，提出极简的loss自适应学习率调度，平均减少93%灾难性遗忘且不牺牲目标任务性能 / Theoretically motivates η = κ/√L̄ schedule that reduces catastrophic forgetting by 93% on average while matching standard SFT task performance — simple, principled, and highly practical.

---

## 按主题分类 / Papers by Topic

### 高效推理与量化 / Efficiency & Quantization

| Paper | 一句话描述 / Brief Description |
|-------|-------------------------------|
| [[2605.19660]] OScaR | 通过识别Token范数失衡（TNI）并用两级旋转+缩放实现INT2近乎无损KV缓存压缩 / Identifies Token Norm Imbalance as the root bottleneck and proposes Canalized Rotation + Omni-Token Scaling for near-lossless INT2 KV cache compression |
| [[2605.19561]] TORQ | 两级正交旋转实现MXFP4量化，Qwen3-32B上精度从38.40%提升至73.63% / Two-level orthogonal rotation for MXFP4 quantization, lifting Qwen3-32B accuracy from 38.40% to 73.63% (vs. 74.82% BF16) |
| [[2605.19929]] SplitQ | MOCD将VLM通道分为文本/视觉/兼容三组分别量化+ACC双分支校准，Qwen2.5-VL-7B W3A3下保留93.5% FP16精度(69.5 vs 74.3) / MOCD splits VLM channels into text/vision/compatible sets + ACC dual-branch calibration, preserving 93.5% FP16 accuracy at W3A3 (69.5 vs 74.3) on Qwen2.5-VL-7B |
| [[2605.19645]] K-Quantization | 用llama.cpp k-quant量化8个LLM(2B-70B)，Phi-3 Mini Q2_K困惑度飙至195.79，7-9B为效率精度最优区间 / k-quantizes 8 LLMs (2B-70B) via llama.cpp; Phi-3 Mini Q2_K perplexity hits 195.79, 7-9B is optimal efficiency-accuracy range |

### LLM系统与推理 / LLM Systems & Inference

| Paper | 一句话描述 / Brief Description |
|-------|-------------------------------|
| [[2605.19775]] Inference Scaling | 揭示推理型负载的"容量陷阱"与DP→TP拐点，覆盖8B到671B模型 / Reveals the "capacity trap" and DP→TP crossover points for reasoning workloads across 8B–671B models |
| [[2605.19945]] GEM | 感知GPU硬件差异进行MoE专家映射，端到端延迟平均降低7.9% / GPU-variability-aware MoE expert mapping achieving 7.9% average latency reduction |
| [[2605.19537]] The Silent Hyperparameter | 推理后端选择可导致高达16.6个百分点差异，35000篇论文中几乎未被报告 / Inference backends can shift benchmark scores by up to 16.6pp, yet are almost never reported in 35K ML papers |

### 优化与训练 / Optimization & Training

| Paper | 一句话描述 / Brief Description |
|-------|-------------------------------|
| [[2605.19282]] Rethinking Muon | 揭示Muon在VLA(低秩动作梯度)和RLVR(低SNR策略梯度)中谱白化放大噪声导致失效，提出高通NS迭代Pion，真机抓取成功率从31.1%升至85.6% / Diagnoses Muon's spectral whitening failure in VLA (low-rank) and RLVR (low-SNR); Pion high-pass NS lifts real-robot grasp success from 31.1% to 85.6% |
| [[2605.20005]] FINCH | Loss自适应学习率调度η=κ/√L̄，平均减少93%灾难性遗忘 / Loss-adaptive learning rate schedule reducing catastrophic forgetting by 93% on average |
| [[2605.19856]] StableGrad | 优化器级梯度重缩放，使深度PINN和BatchNorm-free CNN可稳定训练 / Optimizer-level gradient rescaling enabling stable training of deep PINNs and BatchNorm-free CNNs |
| [[2605.19458]] Mirror Flow Implicit Bias | 推导镜面流平衡方程与Q-边缘，证明收敛到地平线函数φ_α的最大边缘解；α=1诱导稀疏、α≥2诱导稠密，VGG-16上双曲熵达81.96% / Derives mirror flow balance equation + Q-margin, proves convergence to horizon-function max-margin; α=1 sparse, α≥2 dense, hyperbolic entropy 81.96% on VGG-16 |

### 强化学习与推理 / Reinforcement Learning & Reasoning

| Paper | 一句话描述 / Brief Description |
|-------|-------------------------------|
| [[2605.19461]] DMPO | 诊断GRPO模式坍塌并提出分布匹配策略，在NP-hard任务上提升9-12% / Diagnoses GRPO mode collapse and proposes distribution matching, achieving 9–12% gains on NP-hard tasks |
| [[2605.19444]] TTRL-Guard | 发现TTRL中的"正确答案灭绝窗口"并提出三机制防护框架 / Identifies the "Correct-Answer Extinction Window" in TTRL and proposes a three-mechanism guard framework |

### 理论分析 / Theory

| Paper | 一句话描述 / Brief Description |
|-------|-------------------------------|
| [[2605.19483]] Dynamical Systems Memorization | 从动力系统视角用随机逼近理论解释生成模型的记忆化现象 / Explains generative model memorization via stochastic approximation and multi-time-scale SGD dynamics |
| [[2605.19813]] DP Federated Learning Bounds | 建立最一般交互模型下联邦差分隐私估计的极小化下界 / Proves minimax lower bounds for DP federated estimation under the most general interaction model |
| [[2605.20074]] Distillation Guarantees | τ-local-iteration alignment(LRH特化)下GNN蒸馏，样本poly(1/ε,s,n log(d/δ))、时间poly(s^n,2^{nlr},1/ε)；n=6图上深度3蒸馏精度0.911 / τ-local-iteration alignment enables GNN distillation: samples poly(1/ε,s,n log(d/δ)), time poly(s^n,2^{nlr},1/ε); 0.911 distillation acc at depth 3 on n=6 graphs |
| [[2605.20151]] Model Collapse in Interactive Learning | 有向交互图建模多模型协同训练，证明坍缩充要条件=可达不稳定源；加一条边即从稳定变全坍缩，MNIST/CIFAR-10 GAN实验验证 / Directed interaction graph; collapse iff reachable from unstable source; one added edge flips stable→full collapse, validated on MNIST/CIFAR-10 GANs |

### Agent与LLM系统 / Agents & LLM Systems

| Paper | 一句话描述 / Brief Description |
|-------|-------------------------------|
| [[2605.20173]] Runtime Architecture Patterns | 提出"随机-确定边界"原语和六种可组合运行时模式 / Formalizes the Stochastic-Deterministic Boundary primitive and six composable runtime patterns for production LLM agents |
| [[2605.19576]] Library Drift | 定义"库漂移"静默失效(累积技能使性能低于无技能基线)，Ratchet治理(结果驱动退役+有界上限+元技能)将MBPP+ pass@1从0.258提升至0.584(+0.328) / Defines "library drift" silent failure; Ratchet governance (retirement+cap+meta-skill) lifts MBPP+ pass@1 from 0.258 to 0.584 (+0.328) |

### 表示学习 / Representation Learning

| Paper | 一句话描述 / Brief Description |
|-------|-------------------------------|
| [[2605.20107]] HamJEPA | 从哈密顿几何角度证明JEPA各向同性正则化的缺陷，用辛预测器在CIFAR-100上提升+10.64线性探测 / Proves isotropic Gaussian suboptimality in JEPAs and proposes symplectic leapfrog predictor, gaining +10.64 linear probe on CIFAR-100 |

### 评估与基准 / Evaluation & Benchmarking

| Paper | 一句话描述 / Brief Description |
|-------|-------------------------------|
| [[2605.19999]] Contamination-Resistant Datasets | 利用Transformer训练-推理不对称提出KV缓存形式的抗污染基准 / Exploits Transformer train-inference asymmetry to propose KV-cache-based benchmarks unlearnable during pretraining |

### 多模态与可解释性 / Multimodal & Interpretability

| Paper | 一句话描述 / Brief Description |
|-------|-------------------------------|
| [[2605.19250]] MACI | 通过路径修补揭示幻觉驱动/抵抗头的不对称分布，条件干预实现最大幻觉降低 / Path-patching reveals asymmetric hallucination-driving/resisting heads; MACI achieves largest hallucination reduction on MMMC |

---

## All Papers

| # | Paper | Title | 一句话 / Summary |
|---|-------|-------|-------------------|
| 1 | [[2605.19282]] | Rethinking Muon Beyond Pretraining | Pion高通NS替代Muon均匀谱白化，真机抓取成功率从31.1%升至85.6%，RLVR中Muon崩溃而Pion稳定 / Pion high-pass NS replaces Muon whitening; real-robot grasp 31.1%→85.6%, Muon collapses in RLVR while Pion stays stable |
| 2 | [[2605.19250]] | Causal Evidence for Attention Head Imbalance | 路径修补揭示幻觉头不对称分布，MACI条件干预最大降低幻觉 / Path-patching reveals asymmetric hallucination heads; MACI achieves largest hallucination reduction |
| 3 | [[2605.19461]] | Beyond Mode Collapse (DMPO) | 诊断GRPO模式坍塌，DMPO分布匹配在NP-hard和数学推理上大幅提升 / Diagnoses GRPO mode collapse; DMPO distribution matching achieves 9–12% gains on NP-hard and math reasoning |
| 4 | [[2605.19483]] | Dynamical Systems Memorization | 用随机逼近和坍塌理论解释生成模型记忆化 / Explains generative memorization via stochastic approximation collapse theory |
| 5 | [[2605.19444]] | TTRL-Guard | 发现TTRL灭绝窗口并提出三机制防护 / Discovers TTRL extinction window and proposes three-mechanism guard |
| 6 | [[2605.19458]] | Mirror Flow Implicit Bias | 推导镜面流平衡方程与Q-边缘，α=1诱导稀疏α≥2诱导稠密，VGG-16双曲熵81.96% / Derives mirror flow balance equation + Q-margin; α=1 sparse, α≥2 dense, hyperbolic entropy 81.96% on VGG-16 |
| 7 | [[2605.19576]] | Library Drift | 定义库漂移静默失效，Ratchet治理将MBPP+ pass@1从0.258提升至0.584(+0.328) / Defines library drift silent failure; Ratchet governance lifts MBPP+ pass@1 from 0.258 to 0.584 (+0.328) |
| 8 | [[2605.19813]] | DP Federated Learning Bounds | 最一般交互模型下的联邦差分隐私极小化下界 / Minimax lower bounds for DP federated estimation under most general interaction model |
| 9 | [[2605.19775]] | Understanding Inference Scaling | 揭示推理负载容量陷阱与最优并行策略 / Reveals capacity trap and optimal parallelism strategies for reasoning workloads |
| 10 | [[2605.19660]] | OScaR | 两步方案实现INT2近乎无损KV缓存压缩 / Two-step fix achieving near-lossless INT2 KV cache compression |
| 11 | [[2605.19645]] | K-Quantization | llama.cpp k-quant量化8个LLM，Phi-3 Mini Q2_K困惑度195.79，7-9B最优 / k-quantizes 8 LLMs via llama.cpp; Phi-3 Mini Q2_K perplexity 195.79, 7-9B optimal |
| 12 | [[2605.19856]] | StableGrad | 优化器级梯度重缩放稳定深度PINN和CNN训练 / Optimizer-level gradient rescaling stabilizing deep PINN and CNN training |
| 13 | [[2605.20005]] | FINCH | Loss自适应学习率平均减少93%灾难性遗忘 / Loss-adaptive learning rate reducing catastrophic forgetting by 93% |
| 14 | [[2605.19999]] | Contamination-Resistant Datasets | KV缓存形式抗污染基准数据集 / KV-cache-based benchmark datasets resistant to pretraining contamination |
| 15 | [[2605.19945]] | GEM | GPU差异感知MoE专家映射降低7.9%延迟 / GPU-variability-aware MoE expert mapping reducing latency by 7.9% |
| 16 | [[2605.19929]] | SplitQ | MOCD三组通道+ACC双分支，Qwen2.5-VL-7B W3A3保留93.5% FP16(69.5 vs 74.3) / MOCD 3-way channels + ACC branches; Qwen2.5-VL-7B W3A3 preserves 93.5% FP16 (69.5 vs 74.3) |
| 17 | [[2605.20074]] | Distillation Guarantees | τ-local-iteration alignment下GNN蒸馏，n=6图深度3精度0.911 / GNN distillation under τ-local-iteration alignment; 0.911 acc at depth 3 on n=6 graphs |
| 18 | [[2605.20107]] | HamJEPA | 辛预测器在JEPA中替代各向同性正则化，CIFAR-100提升+10.64 / Symplectic predictor replacing isotropic regularization in JEPA, +10.64 on CIFAR-100 |
| 19 | [[2605.20173]] | Runtime Architecture Patterns | 随机-确定边界原语指导生产LLM Agent运行时设计 / SDB primitive guiding production LLM agent runtime design |
| 20 | [[2605.19561]] | TORQ | 两级正交旋转MXFP4量化，Qwen3-32B达73.63%精度 / Two-level orthogonal rotation MXFP4 quantization reaching 73.63% on Qwen3-32B |
| 21 | [[2605.19537]] | The Silent Hyperparameter | 推理后端可导致16.6pp差异但极少被报告 / Inference backends cause up to 16.6pp score differences yet are rarely reported |
| 22 | [[2605.20151]] | Model Collapse in Interactive Learning | 有向交互图坍缩充要条件=可达不稳定源，加一条边即全坍缩 / Directed graph collapse iff reachable from unstable source; one edge flips stable→collapse |
