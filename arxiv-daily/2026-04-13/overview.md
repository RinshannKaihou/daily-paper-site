---
title: "Daily Paper Overview — 2026-04-13"
date: 2026-04-13
tags:
  - daily-overview
  - paper-digest
papers: 31
---

# Daily Paper Overview — 2026-04-13

## Quick Stats

| Metric | Value |
|--------|-------|
| Papers reviewed | 395 |
| Papers summarized | 31 |
| Categories | cs.CL, cs.AI, cs.LG, cs.CV, cs.PF, cs.AR, stat.ML |
| Relevance score 5 | 7 |
| Relevance score 4 | 16 |
| Relevance score 3 | 8 |

## 今日必读 / Must Read Today

> Top picks based on relevance to your interests.

| Paper                                                        | 推荐理由 / Why                                                                                                                                      |
| ------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| [[2604.11791v1]] Looped Reasoning LM Mechanistic Analysis    | 循环推理模型隐空间不动点分析，来自顶级研究团队（Courville, Bronstein）。First mechanistic analysis of fixed-point convergence in looped reasoning LMs with formal proofs. |
| [[2604.11663v1]] Why LLMs Generate Harmful Content           | 因果中介分析定位有害生成的关键层和MLP模块。Causal mediation analysis identifying MLP modules and late-layer neurons driving harmful generation.                     |
| [[2604.11581v1]] Hidden Measurement Error in LLM Eval        | 用概化理论分解LLM评估管道的测量误差，MMLU误差减半。G-theory decomposition of LLM eval pipelines halves MMLU estimation error.                                         |
| [[2604.11662v1]] Hidden Failures in Robustness               | 2000+探针揭示UQ方法在OOD下严重失效。2,000+ probes reveal supervised UQ methods collapse OOD, especially for long-form generation.                            |
| [[2604.11501v1]] Quantization vs Rank Reduction for KV-Cache | 量化一致优于秩缩减（4-364 PPL差距），理论证明来自softmax Fisher度量。Quantization dominates rank reduction at matched storage, formalized via softmax Fisher metric.   |

---

## 按主题分类 / Papers by Topic

### 可解释性与机制分析 / Interpretability & Mechanistic Analysis

| Paper | 一句话总结 / TL;DR | Tags |
|-------|-------------------|------|
| [[2604.11791v1]] Looped Reasoning LM | 循环推理LM中每层收敛到不同不动点，揭示隐空间循环轨迹机制。Fixed-point convergence analysis in looped reasoning LMs reveals cyclic latent trajectories. | `mechanistic-interpretability` `reasoning` |
| [[2604.11802v1]] Psychological Concept Neurons | 识别LLM中大五人格特质的概念选择性神经元，表征干预成功但行为影响弱。Big Five personality concept neurons identified in LLMs; representation control ≠ behavioral control. | `probing` `neuron-intervention` |
| [[2604.11663v1]] Harmful Content Causality | 后层MLP模块驱动有害生成，最终层稀疏神经元门控拒绝机制。Late-layer MLP modules drive harmful generation; sparse final-layer neurons gate refusal. | `causal-mediation` `safety` |
| [[2604.11613v1]] Layerwise ICL Dynamics | 从Transformer中提取首个端到端可识别的涌现更新规则——耦合均值漂移动力学。First end-to-end identified emergent update rule from transformers: coupled mean-shift dynamics. | `in-context-learning` `symmetry` |
| [[2604.11467v1]] SAE + Activation Steering | SAE归因+激活转向使从业者从观察转向干预假设检验，发现涟漪效应风险。SAE attribution + activation steering enables intervention-based debugging with ripple effect risks. | `SAE` `activation-steering` |
| [[2604.11749v1]] HistLens Concept History | SAE分解概念表征追踪跨语料跨时间激活动态变化。SAE decomposes concept representations for cross-corpus temporal activation tracking. | `SAE` `conceptual-history` |
| [[2604.11399v1]] Reasoning in Layers | 免训练层选择性合并恢复VLM中被削弱的时序推理能力。Training-free layer-selective merging restores temporal reasoning in video-language models. | `layer-analysis` `model-merging` |
| [[2604.11322v1]] Tool Irrelevance Bias | 对比注意力归因揭示语义检查与结构匹配两条竞争通路。Contrastive attention attribution reveals competing semantic vs. structural pathways in tool invocation. | `attention-attribution` `tool-use` |
| [[2604.11662v1]] UQ Probe Robustness | 中间层表征+跨token聚合显著优于最终层/单token特征。Middle-layer + token-aggregation consistently more robust than final-layer / single-token features. | `uncertainty-quantification` `probing` |

### 训练稳定性与优化 / Training Stability & Optimization

| Paper | 一句话总结 / TL;DR | Tags |
|-------|-------------------|------|
| [[2604.11639v1]] Inter-Layer Hessian | DAG架构的完整层间Hessian分解框架，O(P)时间诊断曲率交互。Full inter-layer Hessian decomposition with O(P) diagnostic metrics for DAG architectures. | `hessian-analysis` `curvature` |
| [[2604.11446v1]] Low-rank RLVR | 非线性外推低秩参数轨迹加速RLVR训练，减少37.5%计算。Nonlinear extrapolation of low-rank trajectories reduces RLVR compute by ~37.5%. | `RLVR` `training-acceleration` |
| [[2604.11554v1]] Relax RL Engine | 故障隔离服务+异步训练总线，全模态RL后训练提速2.0x。Fault-isolated services + async TransferQueue achieves 2.0x speedup on omni-modal RL. | `distributed-training` `fault-isolation` |
| [[2604.11508v1]] Forgetting Dynamics | CNN和ViT遗忘完全不同的样本（Jaccard 0.15-0.34），挑战样本难度内在性假设。CNN and ViT forget fundamentally different samples; per-sample forgetting is stochastic across seeds. | `fine-tuning` `catastrophic-forgetting` |
| [[2604.11297v1]] MEDS Reward Shaping | 密度聚类识别重复错误模式并加重惩罚，最高提升4.13 pass@1。Density clustering of recurring errors with heavier penalties yields up to 4.13 pass@1 improvement. | `reward-shaping` `diversity` |
| [[2604.11416v1]] Exact Certification | 首个神经网络抗标签投毒的精确多项式时间证书。First exact polynomial-time certificate for neural networks against label poisoning via NTK. | `certification` `label-poisoning` |
| [[2604.11465v1]] Role Orchestration | 同一模型扮演三个角色使8B模型超越33B，纯推理时干预。Three-role scaffolding with frozen 8B model surpasses 33B model without any training. | `inference-time` `small-models` |

### 计算可靠性与硬件 / Computation Reliability & Hardware

| Paper | 一句话总结 / TL;DR | Tags |
|-------|-------------------|------|
| [[2604.11501v1]] Quantization vs Rank Reduction | softmax Fisher度量下投影损伤超过量化损伤3×2^{2b}，量化在所有设置中胜出。Projection damage exceeds quantization damage by 3×2^{2b}; INT4 dominates rank reduction. | `quantization` `kv-cache` |
| [[2604.11288v1]] Transactional Attention | 结构锚定赞助保护休眠token，K=16时100%凭证检索。Structural anchor sponsorship achieves 100% credential retrieval at K=16 tokens. | `kv-cache` `attention` |
| [[2604.11615v1]] CUTEv2 Matrix Extension | 解耦CPU矩阵单元支持混合精度，利用率超90%。Decoupled CPU matrix extension with mixed-precision, >90% utilization across 4 platforms. | `cpu-architecture` `mixed-precision` |
| [[2604.11512v1]] EdgeCIM | 65nm CIM实现INT4 SLM边缘推理，7.3x吞吐量优于Orin Nano。65nm CIM with INT4 achieves 7.3x throughput over Orin Nano for edge SLM inference. | `compute-in-memory` `INT4` |
| [[2604.11391v1]] H100 vs H200 Power | H100计算密集型略优，H200内存密集型能效更佳。H100 better for compute-bound; H200 better for memory-bound workloads under power capping. | `GPU` `energy-efficiency` |
| [[2604.11659v1]] FHE DNN GPU | AMD GPU加速稀疏FHE矩阵乘法，3.0x优于CPU。Sparse FHE ciphertext matmul on AMD GPUs achieves 3.0x over CPU. | `homomorphic-encryption` `GPU` |
| [[2604.11582v1]] Triadic Tokenization | 三位后缀分词方案覆盖33个数量级，但无实验验证。Triadic suffix tokenization covers 33 orders of magnitude but lacks experimental validation. | `tokenization` `precision` |
| [[2604.11530v1]] SVD-Prune | SVD杠杆分数选择全局方差贡献最大的视觉token。SVD leverage scores select tokens contributing to dominant global variance for VLM pruning. | `token-pruning` `SVD` |

### 推理评估与基准 / Inference Evaluation & Benchmarking

| Paper | 一句话总结 / TL;DR | Tags |
|-------|-------------------|------|
| [[2604.11581v1]] Measurement Error | G-theory分解评估管道方差，MMLU误差减半。G-theory variance decomposition halves MMLU estimation error. | `evaluation` `variance-decomposition` |
| [[2604.11589v1]] MLLM Judge Bias | 12个MLLM普遍存在自偏好和同族互偏好偏见。12 MLLMs exhibit self-preference and within-family mutual preference bias (1.29M pairs). | `evaluation-bias` `preference` |
| [[2604.11287v1]] AI Exercise Consistency | 语义一致但运动强度等定量组件变异显著。High semantic consistency but significant variability in quantitative exercise components. | `output-consistency` `reproducibility` |
| [[2604.11704v1]] Geometric Phase Transitions | 线性捷径剪枝后网络被迫使用更高几何容量弯曲决策边界。Pruning linear shortcuts forces networks into higher geometric capacity, reducing gender vulnerability. | `shortcut-learning` `fairness` |

### 数学基础与理论 / Mathematical Foundations & Theory

| Paper | 一句话总结 / TL;DR | Tags |
|-------|-------------------|------|
| [[2604.11729v1]] First-Order Methods Universality | 首次计算Walsh-Hadamard等确定性矩阵的GFOM极限动力学。First calculation of deterministic matrix traffic distributions; unified AMP with Gaussian dynamics. | `random-matrices` `AMP` |
| [[2604.11665v1]] Hyper-Dimensional System | 超维SRAM-CAM架构作为LLM替代方案的理论提案。Hyper-dimensional SRAM-CAM (VaCoAl) proposed as alternative to LLMs and neuromorphics. | `hyper-dimensional-computing` |
| [[2604.11315v1]] Structured Sparsity S3 | View+Block+Scope三组件统一结构化稀疏规范。View+Block+Scope algebraic framework unifies structured sparsity specification. | `structured-sparsity` `pruning` |

---

## All Papers

| # | Paper | Authors | Key Topic | 一句话总结 / TL;DR |
|---|-------|---------|-----------|-------------------|
| 1 | [[2604.11791v1]] Looped Reasoning LM | Blayney et al. | Interpretability | 循环推理模型层间不动点收敛机制。Fixed-point convergence in looped reasoning LMs. |
| 2 | [[2604.11802v1]] Concept Neurons | Harada & Hamada | Interpretability | 大五人格概念神经元探测与干预。Big Five personality neuron probing and intervention. |
| 3 | [[2604.11663v1]] Harmful Content | Ganguli & Moraffah | Safety/Interpretability | 因果中介分析定位有害生成关键层。Causal mediation of harmful generation. |
| 4 | [[2604.11639v1]] Inter-Layer Hessian | Bolshim & Kugaevskikh | Training Theory | DAG架构层间Hessian分解诊断指标。Inter-layer Hessian diagnostics for DAG networks. |
| 5 | [[2604.11662v1]] UQ Probe Robustness | Stacey et al. | Evaluation/Interpretability | 监督式UQ探针OOD严重失效。Supervised UQ probes fail severely OOD. |
| 6 | [[2604.11501v1]] Quantization vs Rank | Salfati | Computation | 量化一致优于秩缩减KV-cache压缩。Quantization dominates rank reduction for KV-cache. |
| 7 | [[2604.11581v1]] Measurement Error | Messing | Evaluation | G-theory分解LLM评估管道方差。G-theory variance decomposition for LLM eval. |
| 8 | [[2604.11613v1]] ICL Dynamics | Lutz et al. | Interpretability | Transformer涌现均值漂移更新规则。Emergent mean-shift dynamics in transformers. |
| 9 | [[2604.11467v1]] SAE Steering | Labarta et al. | Interpretability | SAE+激活转向可视化调试工作流。SAE + activation steering visual debugging. |
| 10 | [[2604.11749v1]] HistLens | Jing et al. | Interpretability | SAE分解概念表征追踪历史变迁。SAE concept decomposition for historical analysis. |
| 11 | [[2604.11446v1]] RLVR Acceleration | Chen et al. | Training | 非线性外推低秩轨迹加速RLVR 37.5%。Nonlinear trajectory extrapolation for RLVR. |
| 12 | [[2604.11399v1]] Reasoning in Layers | Fu et al. | Interpretability | 层选择性合并恢复VLM时序推理。Layer-selective merging restores temporal reasoning. |
| 13 | [[2604.11554v1]] Relax Engine | Zhang et al. | Training Systems | 故障隔离异步RL训练提速2.0x。Fault-isolated async RL training, 2.0x speedup. |
| 14 | [[2604.11288v1]] Transactional Attn | Basu | Computation | 结构锚定保护休眠token免于驱逐。Structural anchor sponsorship for dormant tokens. |
| 15 | [[2604.11615v1]] CUTEv2 | Ye et al. | Hardware | 解耦CPU矩阵扩展支持混合精度。Decoupled CPU matrix extension with mixed-precision. |
| 16 | [[2604.11512v1]] EdgeCIM | Bazzi et al. | Hardware | CIM实现INT4 SLM边缘推理7.3x加速。CIM-based INT4 edge inference, 7.3x speedup. |
| 17 | [[2604.11530v1]] SVD-Prune | Apedo et al. | Efficiency | SVD杠杆分数VLM视觉token剪枝。SVD leverage score token pruning for VLMs. |
| 18 | [[2604.11704v1]] Geometric Phase | Rodriguez-Alvarez et al. | Fairness | 容量相变缓解shortcut学习。Capacity phase transition against shortcut learning. |
| 19 | [[2604.11665v1]] Hyper-Dimensional | Chuma et al. | Theory | 超维SRAM-CAM替代计算架构。Hyper-dimensional SRAM-CAM alternative computing. |
| 20 | [[2604.11391v1]] H100 vs H200 | Ujeniya et al. | Hardware | H100计算型优，H200内存型优。H100 compute-bound, H200 memory-bound efficiency. |
| 21 | [[2604.11589v1]] MLLM Judge Bias | Koyama et al. | Evaluation | MLLM评估存在自偏好和同族偏见。MLLM self-preference and family bias in judging. |
| 22 | [[2604.11287v1]] Exercise Consistency | Lee | Evaluation | LLM运动处方语义一致但定量变异。Semantic consistency but quantitative variability. |
| 23 | [[2604.11322v1]] Tool Irrelevance | Liu et al. | Interpretability | 结构对齐偏见和竞争注意力通路。Structural alignment bias with competing pathways. |
| 24 | [[2604.11659v1]] FHE GPU | D'Agata et al. | Hardware | GPU加速稀疏FHE矩阵乘法3.0x。GPU sparse FHE matmul 3.0x speedup. |
| 25 | [[2604.11416v1]] Exact Certification | Mohgaonkar et al. | Theory | 首个精确多项式时间标签投毒证书。First exact polynomial-time label poisoning certificate. |
| 26 | [[2604.11582v1]] Triadic Tokenization | Chetverina | Computation | 三位后缀分词覆盖33个数量级。Triadic suffix tokenization, 33 orders of magnitude. |
| 27 | [[2604.11508v1]] Forgetting Dynamics | Daga & Ramu | Training | CNN和ViT架构依赖性遗忘动力学。Architecture-dependent forgetting in fine-tuning. |
| 28 | [[2604.11315v1]] S3 Sparsity | Ghriss | Theory | View+Block+Scope结构化稀疏框架。Algebraic structured sparsity specification. |
| 29 | [[2604.11465v1]] Role Orchestration | McClendon et al. | Evaluation | 三角色脚手架使8B超越33B模型。Three-role scaffolding: 8B beats 33B. |
| 30 | [[2604.11729v1]] First-Order Universality | Gorini et al. | Theory | 确定性矩阵的一阶方法普适性。Universality of first-order methods on deterministic matrices. |
| 31 | [[2604.11297v1]] MEDS Reward | Liu et al. | Training | 记忆增强动态奖励塑形提升多样性。Memory-enhanced reward shaping for diversity. |

---

*Overview generated on 2026-04-14*
