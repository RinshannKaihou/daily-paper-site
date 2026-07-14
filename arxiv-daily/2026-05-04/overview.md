---
title: "Daily Paper Overview — 2026-05-04"
date: 2026-05-04
tags:
  - daily-papers
  - arxiv
  - llm
  - ml-research
papers: 42
---

## 今日必读 / Must Read Today

### 1. [[2605.02442v1]] Measuring AI Reasoning: A Guide for Researchers

> **推荐理由 / Why read:** 本文从评估视角出发，提出推理链的忠实性（faithfulness）和有效性（validity）应作为推理评估核心指标，而非仅依赖最终答案准确率。设计了分层的证据等级框架（Level 0-2）和可移植量化指标（SVR、VSR、IFR），为当前推理基准泛滥的研究生态提供了亟需的方法论锚点。
>
> A principled position paper arguing that outcome-only accuracy is insufficient for evaluating reasoning. Proposes an evidence-tier framework (Levels 0–2) with portable metrics (SVR, VSR, IFR) for process-based evaluation — a much-needed methodological anchor in the current proliferation of reasoning benchmarks.

### 2. [[2605.02398v1]] The Compliance Trap: How Structural Constraints Degrade Frontier AI Metacognition

> **推荐理由 / Why read:** 首次通过6条件因子实验证明，"合规指令"（而非威胁内容本身）导致8/11个前沿模型发生灾难性元认知崩溃（准确率最多下降30.2pp），而Anthropic的宪法AI训练对此几乎免疫。揭示了标准安全评估无法捕获的具体部署漏洞。
>
> First empirical demonstration via 6-condition factorial design that compliance-forcing instructions—not threat content—cause catastrophic metacognitive collapse in 8/11 frontier models (up to 30.2pp accuracy drop). Constitutional AI models show near-perfect immunity, revealing a concrete, deployment-relevant vulnerability invisible to standard safety evaluations.

### 3. [[2605.02658v2]] Deciphering Shortcut Learning from an Evolutionary Game Theory Perspective

> **推荐理由 / Why read:** 从演化博弈论视角严格证明全批量GD收敛到捷径策略、SGD收敛到核心特征策略，并通过SDE模型揭示数据噪声加剧捷径偏差、优化噪声抑制捷径偏差的双重效应。为"SGD为何泛化更好"提供了博弈论层面的全新数学解释。
>
> Proves via evolutionary game theory that full-batch GD converges to shortcut-dominated states while mini-batch SGD converges to core-feature states. An SDE model further reveals that data noise amplifies shortcut bias while optimization noise suppresses it — a rigorous new mathematical explanation for SGD's superior generalization.

---

## 按主题分类 / Papers by Topic

### LLM Training, RL & Optimization / LLM训练、强化学习与优化

| Paper | Title (Short) | Description |
|-------|--------------|-------------|
| [[2605.02435v1]] | GAME-GRPO | 系统性解决答案级微调中Jensen不等式偏差，提供无偏多项式估计和零开销查表替换。/ Systematically resolves O(1/K) Jensen inequality bias in ALFT with unbiased polynomial estimators and zero-overhead table-lookup replacements. |
| [[2605.02375v1]] | Binary Rewards RL | 揭示二元奖励导致策略梯度的根本退化，模型误设定下降低温度导致多样性崩溃。/ Reveals fundamental degeneracy of binary rewards for policy gradients; diversity collapse under misspecification at low temperature. |
| [[2605.02469v1]] | BOLT | 证明参考采样Boltzmann加权SFT精确等价于KL正则化RLVR最优策略，训练时间减少75–85%。/ Proves reference-sampled Boltzmann-weighted SFT exactly equals the KL-regularized RLVR optimum, with 75–85% training time reduction. |
| [[2605.02626v1]] | Gate-DPO | 基于概率几何门控DPO中拒绝样本梯度，解决概率挤压效应和分布崩塌。/ Gates rejected-sample gradients in DPO based on probability geometry, fixing the squeezing effect and distribution collapse. |
| [[2605.02701v1]] | PS-Clip-SGD | 逐样本梯度裁剪在重尾噪声下达到最优非凸收敛率，AlexNet验证精度+6%。/ Per-sample gradient clipping achieves optimal non-convex convergence under heavy-tailed noise; +6% AlexNet validation accuracy. |
| [[2605.02317v1]] | Anon Optimizer | 连续可调自适应系数在SGD和Adam之间插值甚至外推，引入IDU机制保证全频谱收敛。/ Continuously tunable adaptivity interpolates/extrapolates between SGD and Adam with IDU for full-spectrum convergence. |
| [[2605.02320v1]] | ANO | 统一信赖域框架引入Redescending Influence Principle，3倍学习率下仍保持策略稳定。/ Unified trust-region framework with Redescending Influence Principle; stable under 3x learning rate. |
| [[2605.02364v1]] | InfoLaw | 信息论视角的缩放定律，统一量化数据质量、重复和模型规模对性能的影响，外推误差0.15%。/ Information-theoretic scaling law unifying quality, repetition, and scale; 0.15% mean extrapolation error. |
| [[2605.03229v1]] | SMF | 稀疏记忆微调以少量任务增益换取极低遗忘，形成LoRA和全量微调之外的Pareto最优点。/ Sparse memory finetuning trades smaller task gains for minimal forgetting, a Pareto-optimal point beyond LoRA and full FT. |

### Inference Efficiency & Compression / 推理效率与压缩

| Paper | Title (Short) | Description |
|-------|--------------|-------------|
| [[2605.02404v1]] | SLQ | 区分任务无损（3.3–4.7 bpp）和分布无损（5.0–6.6 bpp）两层量化，获得1.7–3.6倍推理加速。/ Distinguishes task-lossless (3.3–4.7 bpp) from distribution-lossless (5.0–6.6 bpp) quantization with 1.7–3.6x speedup. |
| [[2605.02888v1]] | SpecKV | 自适应投机长度选择器利用draft model熵信号，跨压缩级别提升期望token产出56%。/ Adaptive speculation-length selector using draft entropy signals; 56% improvement across compression levels. |
| [[2605.03109v1]] | GSI | 门控残差直通机制利用激活低秩子空间，GPT-J 6B上实现15.6倍权重读取加速。/ Gated residual passthrough exploiting activation low-rank structure; 15.6x weight-read speedup on GPT-J 6B. |
| [[2605.03110v1]] | Cascade ADA | 级联式token选择利用层间代表集合一致性，节省22–63% Gram运算量。/ Cascade token selection exploiting inter-layer representative-set coherence; 22–63% Gram operation savings. |
| [[2605.02568v1]] | StreamIndex | 分块流式Top-k替代全量中间张量，将单GPU序列长度从65K扩展到1M以上。/ Chunked streaming top-k replaces full intermediate tensors, extending single-GPU sequences from 65K to 1M+. |
| [[2605.02829v1]] | JACTUS | 统一低秩压缩与参数高效微调，80%参数量超越100%参数的LoRA/DoRA。/ Unifies low-rank compression and PEFT; 80% params outperforms 100%-budget LoRA/DoRA. |

### Reasoning & Evaluation / 推理与评估

| Paper | Title (Short) | Description |
|-------|--------------|-------------|
| [[2605.02442v1]] | Measuring AI Reasoning | 提出忠实性和有效性为核心的推理评估分层框架，超越最终答案准确率。/ Proposes faithfulness/validity-centered tiered framework for reasoning evaluation beyond final-answer accuracy. |
| [[2605.02290v1]] | CoRD | 多教师协同逐步解码蒸馏，32B学生模型在AIME上超越所有教师。/ Multi-teacher step-wise collaborative distillation; 32B student surpasses all teachers on AIME. |
| [[2605.02396v1]] | HeavySkill | 并行推理+序列审议的"重度思考"范式，14+模型上持续优于多数投票。/ Parallel reasoning + sequential deliberation; consistently outperforms majority voting across 14+ models. |
| [[2605.02427v1]] | APPS | 块级粒子滤波推理框架逼近序列级幂分布，训练无关方法中达到最优推理性能。/ Blockwise particle filtering targeting sequence-level power distribution; best training-free inference performance. |
| [[2605.02395v1]] | PRM Data Synthesis | 基于符号推理的可控可验证过程监督数据合成，发现首个错误定位远难于整体步骤分类。/ Symbolic-reasoning-based controllable process data synthesis; first-error localization much harder than step classification. |
| [[2605.03227v1]] | Prompting vs Execution | LLM在序列级精确计算上不可靠（最低40%），Program-of-Thought通过代码执行达到100%。/ LLMs unreliable at exact computation (min 40%); Program-of-Thought achieves 100% via code execution. |
| [[2605.02363v1]] | Structured Output Reliability | 小模型答案正确但JSON格式不可用（output accuracy 0%），黑盒提示优化恢复至84–87%。/ Small models correct but JSON-unusable (0% output accuracy); black-box prompt optimization recovers to 84–87%. |

### Interpretability & Representation Geometry / 可解释性与表征几何

| Paper | Title (Short) | Description |
|-------|--------------|-------------|
| [[2605.03052v1]] | How LLMs Process Negation | LLM内部同时存在否定机制和捷径机制，注意力汇聚消融提升否定准确率最高17%。/ Negation and shortcut mechanisms co-exist; attention sink ablation improves negation accuracy by up to 17%. |
| [[2605.03058v1]] | MechaRule | 将符号规则与神经元因果关联，对比层次消融高效定位稀疏激动子神经元。/ Anchors symbolic rules to causal neurons via contrastive hierarchical ablation of sparse agonist neurons. |
| [[2605.03160v1]] | Pairwise Matrices for SAEs | 标准SAE单特征标注遗漏非单调剂量响应和联合结构性角色，成对矩阵协议揭示因果结构。/ Standard SAE labeling misses non-monotonic dose-response and joint structural roles; pairwise matrix reveals causal structure. |
| [[2605.03222v1]] | S-RAS | 基于Fisher信息的敏感性对齐框架，通过局部表示几何补充传统激活对齐方法。/ Fisher-information-based sensitivity alignment framework complementing activation-based methods via local geometry. |
| [[2605.02735v1]] | Visual Latents (MLLM) | 多模态模型视觉隐变量被自回归目标"静默"，推理时优化可重新激活其推理能力。/ Visual latents "silenced" by autoregressive objective in multimodal models; inference-time optimization reactivates reasoning. |
| [[2605.03196v1]] | Geometric Deviation | 隐藏状态到参考质心的余弦距离可无监督检测不可回答数学查询（AUC 0.78–0.84）。/ Cosine distance from hidden states to reference centroid detects unanswerable math queries unsupervised (AUC 0.78–0.84). |
| [[2605.03217v1]] | Moral Sensitivity | 推理蒸馏以U型曲线重新引入大规模模型已抑制的刑事偏见，行为-机制双向验证。/ Reasoning distillation reintroduces suppressed criminal bias in a U-curve; behavioral-mechanistic bidirectional validation. |

### Safety, Alignment & Trustworthy AI / 安全、对齐与可信AI

| Paper | Title (Short) | Description |
|-------|--------------|-------------|
| [[2605.02398v1]] | The Compliance Trap | 合规指令导致8/11模型元认知崩溃，Anthropic宪法AI免疫，揭示部署级漏洞。/ Compliance instructions collapse metacognition in 8/11 models; Constitutional AI immune; deployment-level vulnerability. |
| [[2605.03034v1]] | Stable Agentic Control | 工具中介LLM架构配合Lean 4机器验证Lyapunov稳定性证书，Claude Sonnet 4实现零方差防御。/ Tool-mediated LLM architecture with Lean 4-verified Lyapunov certificate; Claude Sonnet 4 achieves zero-variance defense. |
| [[2605.02640v1]] | Trustworthy AI & Causality | 将公平性、鲁棒性、隐私、可解释性间的矛盾统一为不变性冲突，因果推理提供选择性不变性。/ Reinterprets trustworthy AI trade-offs as invariance conflicts; causal reasoning provides selective invariance. |

### Theory & Mathematical Foundations / 理论与数学基础

| Paper | Title (Short) | Description |
|-------|--------------|-------------|
| [[2605.02658v2]] | Shortcut Learning (EGT) | 演化博弈论严格证明GD收敛到捷径、SGD收敛到核心特征，优化噪声抑制捷径偏差。/ Evolutionary game theory proves GD→shortcuts, SGD→core features; optimization noise suppresses shortcut bias. |
| [[2605.02509v1]] | MPCS | 11种可塑性机制消融发现傅里叶编码最关键、全局EWC反而有害，帕累托压缩移除劣势组件。/ 11 plasticity mechanisms ablated; Fourier encoding most critical, global EWC harmful; Pareto compression removes dominated components. |
| [[2605.02771v1]] | Universality in DNNs | Lindeberg交换原理给出有限宽度DNN到高斯极限的2-Wasserstein收敛速率O(n^{-1/4})。/ Lindeberg exchange gives O(n^{-1/4}) 2-Wasserstein convergence rate of finite-width DNNs to Gaussian limit. |
| [[2605.02853v1]] | YES Training Monitoring | 逐层剥离构建轻量参考解，发现量化微调中训练模型甚至不如2层YES基线。/ Layer-wise peeling constructs lightweight reference solutions; trained model sometimes underperforms 2-layer YES baseline under quantization. |

### Systems, Speech & Specialized Applications / 系统、语音与专业应用

| Paper | Title (Short) | Description |
|-------|--------------|-------------|
| [[2605.02371v1]] | MRDIMM Performance | 首个生产级MRDIMM-8800评估，带宽+41%、延迟更低、带宽密集型负载能耗降低18–30%。/ First production MRDIMM-8800 evaluation: +41% bandwidth, lower latency, 18–30% energy savings on bandwidth-intensive workloads. |
| [[2605.02821v2]] | LLM API Heterogeneity | 同一开源模型在不同API提供商的服务异质性测量，智能路由可降低成本37.8%。/ Cross-provider heterogeneity measurement for hosted open-weight LLMs; smart routing reduces cost by 37.8%. |
| [[2605.02572v1]] | Long-Horizon RL Training | 任务步数本身是LLM agent RL训练瓶颈，宏动作稳定训练且短步数训练可泛化到长步数。/ Horizon length itself is a training bottleneck for LLM agents; macro actions stabilize training with horizon generalization. |
| [[2605.03096v1]] | HyPA | 混合提示算术结合非线性任务向量和线性化混淆因子向量，缓解文本分类分布偏移。/ Hybrid prompt arithmetic combining non-linear task and linearized confounder vectors mitigates distribution shift. |
| [[2605.02715v1]] | GRIDS (Speech) | 局部内在维度分析WavLM和wav2vec 2.0在对抗攻击下的表征几何变化，AUROC 0.78–1.00。/ Local intrinsic dimensionality reveals adversarial perturbation effects in speech models; AUROC 0.78–1.00. |
| [[2605.03039v1]] | MP-IB (Bipolar) | 混合精度量化作为信息瓶颈实现双相障碍躁动检测中的特质-状态分离，657K参数超越94M WavLM。/ Mixed-precision quantization as information bottleneck for bipolar agitation detection; 657K params beats 94M WavLM. |

---

## All Papers

| # | ArXiv ID | Title | One-line Summary (中文) |
|---|----------|-------|----------------------|
| 1 | [[2605.02290v1]] | CoRD | 多教师协同逐步解码蒸馏，32B学生超越所有教师 |
| 2 | [[2605.02317v1]] | Anon Optimizer | 连续可调自适应系数在SGD和Adam之间插值，IDU保证收敛 |
| 3 | [[2605.02320v1]] | ANO | 统一信赖域+Redescending Influence，3倍学习率下策略稳定 |
| 4 | [[2605.02363v1]] | Structured Output Reliability | 小模型JSON格式不可用（0%），黑盒提示优化恢复至84–87% |
| 5 | [[2605.02364v1]] | InfoLaw | 信息论缩放定律统一量化质量、重复和规模，外推误差0.15% |
| 6 | [[2605.02371v1]] | MRDIMM Performance | 生产级MRDIMM评估：+41%带宽，18–30%能效提升 |
| 7 | [[2605.02375v1]] | Binary Rewards RL | 二元奖励导致策略梯度根本退化和多样性崩溃 |
| 8 | [[2605.02395v1]] | PRM Data Synthesis | 符号推理可控可验证过程数据合成，首个错误定位远难于步骤分类 |
| 9 | [[2605.02396v1]] | HeavySkill | 并行推理+序列审议，14+模型持续优于多数投票 |
| 10 | [[2605.02398v1]] | The Compliance Trap | 合规指令导致8/11模型元认知崩溃，宪法AI免疫 |
| 11 | [[2605.02404v1]] | SLQ | 任务无损3.3–4.7bpp + 分布无损5.0–6.6bpp两层量化 |
| 12 | [[2605.02427v1]] | APPS | 块级粒子滤波逼近幂分布，训练无关方法中最优推理性能 |
| 13 | [[2605.02435v1]] | GAME-GRPO | 解决ALFT中Jensen不等式偏差，零开销查表替换 |
| 14 | [[2605.02442v1]] | Measuring AI Reasoning | 忠实性/有效性为核心的推理评估分层框架 |
| 15 | [[2605.02469v1]] | BOLT | Boltzmann加权SFT精确等价RLVR最优，训练时间减少75–85% |
| 16 | [[2605.02509v1]] | MPCS | 11种可塑性消融：傅里叶编码最关键，全局EWC有害 |
| 17 | [[2605.02568v1]] | StreamIndex | 分块流式Top-k将单GPU序列从65K扩展到1M+ |
| 18 | [[2605.02572v1]] | Long-Horizon RL Training | 任务步数本身是RL训练瓶颈，宏动作+horizon generalization |
| 19 | [[2605.02626v1]] | Gate-DPO | 基于概率几何门控DPO梯度，解决概率挤压和分布崩塌 |
| 20 | [[2605.02640v1]] | Trustworthy AI & Causality | 可信AI权衡统一为不变性冲突，因果推理提供选择性不变性 |
| 21 | [[2605.02658v2]] | Shortcut Learning (EGT) | 演化博弈论：GD→捷径，SGD→核心特征；优化噪声抑制捷径 |
| 22 | [[2605.02701v1]] | PS-Clip-SGD | 逐样本裁剪达到最优重尾噪声收敛率，+6% AlexNet精度 |
| 23 | [[2605.02715v1]] | GRIDS | LID分析语音模型对抗攻击表征变化，AUROC 0.78–1.00 |
| 24 | [[2605.02735v1]] | Visual Latents (MLLM) | 视觉隐变量被"静默"，推理时优化可重新激活 |
| 25 | [[2605.02771v1]] | Universality in DNNs | Lindeberg原理给出W_2收敛O(n^{-1/4}) |
| 26 | [[2605.02821v2]] | LLM API Heterogeneity | 跨提供商服务异质性测量，智能路由降低成本37.8% |
| 27 | [[2605.02829v1]] | JACTUS | 统一压缩+PEFT，80%参数超越100% LoRA/DoRA |
| 28 | [[2605.02853v1]] | YES Training Monitoring | 逐层剥离发现量化微调中模型不如2层YES基线 |
| 29 | [[2605.02888v1]] | SpecKV | 自适应投机长度，跨压缩级别+56%期望token产出 |
| 30 | [[2605.03034v1]] | Stable Agentic Control | Lean 4验证Lyapunov证书+工具中介架构，零方差防御 |
| 31 | [[2605.03039v1]] | MP-IB | 混合精度作信息瓶颈，657K参数超越94M WavLM |
| 32 | [[2605.03052v1]] | How LLMs Process Negation | 否定+捷径机制共存，注意力汇聚消融+17%准确率 |
| 33 | [[2605.03058v1]] | MechaRule | 符号规则锚定因果神经元，对比层次消融定位激动子 |
| 34 | [[2605.03096v1]] | HyPA | 混合提示算术缓解分布偏移中的混淆因子 |
| 35 | [[2605.03109v1]] | GSI | 门控残差直通，GPT-J 6B上15.6倍权重读取加速 |
| 36 | [[2605.03110v1]] | Cascade ADA | 级联token选择利用层间一致性，节省22–63% Gram运算 |
| 37 | [[2605.03160v1]] | Pairwise Matrices for SAEs | 成对矩阵协议揭示SAE标注遗漏的因果结构 |
| 38 | [[2605.03196v1]] | Geometric Deviation | 余弦距离无监督检测不可回答查询，AUC 0.78–0.84 |
| 39 | [[2605.03217v1]] | Moral Sensitivity | 推理蒸馏U型曲线重新引入刑事偏见，行为-机制双向验证 |
| 40 | [[2605.03222v1]] | S-RAS | Fisher信息敏感性对齐框架补充传统激活对齐 |
| 41 | [[2605.03227v1]] | Prompting vs Execution | LLM精确计算不可靠，PoT通过代码执行达100% |
| 42 | [[2605.03229v1]] | SMF | 稀疏记忆微调以极少遗忘换取任务适配，Pareto最优点 |
