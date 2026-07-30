---
title: "Daily arXiv Digest — 2026-07-27"
date: 2026-07-27
tags:
  - mechanistic-interpretability
  - representation-geometry
  - self-improving-agents
  - training-stability
  - quantization
  - conformal-prediction
  - LLM-evaluation
  - failure-modes
  - statistical-foundations
papers: 38
---

# Daily arXiv Digest — 2026-07-27

> 今日精选 38 篇论文，围绕**机制可解释性与表示几何、自我改进 Agent 与编码 Agent 可靠性、LLM 训练稳定性与量化计算可靠性、评估失效模式与统计保证、以及统计/优化基础理论**五条主线。 / Today's digest covers 38 papers across five threads: **mechanistic interpretability & representation geometry, self-improving/coding-agent reliability, LLM training stability & quantized-compute reliability, evaluation failure modes & statistical guarantees, and statistical/optimization foundations.**

---

## 今日必读 / Must Read Today

### 1. [[2607.24645]] Sparse Autoencoders Encode Both Concepts and Functions

> **推荐理由：** 本文提出 FEGA（Feature-Effect Geometry Analysis），首次证明稀疏自编码器（SAE）的特征同时编码"概念"与"函数效应"——即特征对模型 logit 的下游影响具有可解释的几何结构。这对以 SAE 为核心的可解释性研究是范式性补充，让"特征→行为"的因果链条从相关性升级为可定位、可操纵的几何对象。
>
> **Why read:** FEGA is the first framework showing that SAE features encode not just concepts but their downstream *functional effects* on model logits, with a learnable geometry that makes feature→behavior steering tractable. A foundational upgrade for anyone working on sparse-coding interpretability — it reframes what a "feature" means.

### 2. [[2607.24425]] Context Is King — How In--Context Specification Shapes the Geometry of Concepts

> **推荐理由：** 本文用因果实验（RSA + 激活修补）证明：LLM 使用的概念关系几何（环/树拓扑）并非固定的"世界模型"，而是由上下文中的声明式规则即时设定并因果性使用。能力足够强的模型会以上下文几何压倒预训练先验（RSA 0.6–0.9 vs ~0）。这直接挑战"LLM 内含稳定世界模型"的常见假设。
>
> **Why read:** Causal activation-patching shows an LLM's relational geometry over concepts is set on-demand by in-context rules, not fixed in weights — the imposed order dominates the pretrained prior (RSA +0.87 vs −0.03). A sharp challenge to the "LLMs harbor a stable world model" assumption, with clean scale-gated fidelity findings.

### 3. [[2607.24300]] Self-Authored Verification Is Unreliable in Heuristic Self-Improving Agents

> **推荐理由：** 本文直击自我改进 Agent 的核心隐患：在启发式自改进（SEAL 类）系统中，模型自评分数与真实部署性能出现系统性"验证者-部署鸿沟"——自评分居高不下而真实表现退化。这对所有构建"自我改进闭环"的团队是必须正视的安全信号。
>
> **Why read:** Documents a systematic *verifier–deployment gap* in heuristic self-improving agents: self-authored verification scores stay high while ground-truth performance degrades — reward-hacking at the self-improvement loop level. Essential reading for anyone building self-improving/closed-loop agent systems.

---

## 按主题分类 / Papers by Topic

### A. 机制可解释性与表示几何 / Mechanistic Interpretability & Representation Geometry

| Paper | 概述 / Overview |
|-------|-----------------|
| [[2607.24645]] FEGA: SAEs Encode Concepts & Functions | 首次系统刻画 SAE 特征的下游函数效应几何（FEGA），并证明其对 logit 的因果影响可被定位与操纵 / First systematic geometry of SAE features' downstream functional effects on logits, shown to be causally localizable and steerable. |
| [[2607.24425]] Context Is King | 概念关系几何由上下文声明式规则即时设定，大模型以上下文几何因果压倒预训练先验（RSA +0.87 vs −0.03）/ Concept relational geometry is set on-demand by in-context declarative rules; large models let context causally dominate pretrained priors. |
| [[2607.24471]] Grounding Latent Algorithm Routing | ROUTEBENCH 证明稠密 Transformer 能发展出"类路由"内部变量，可被中层探针解码、可被激活编辑翻转 / ROUTEBENCH shows dense transformers develop route-like internal variables decodable by mid-layer probes and flippable by activation edits. |
| [[2607.24586]] D-Score: Spectral Hallucination Signal | 用隐藏层激活的相对数值秩（奇异方向）作为无外部检索的幻觉检测信号，超越 LLM-Check 的 Hidden Score / Uses relative numerical rank of hidden-state singular directions as a retrieval-free hallucination signal, beating LLM-Check's Hidden Score. |
| [[2607.24017]] Disentangling Semantic-Structural Attention | 把注意力 sink/register token 重构为注意力流形上的结构性偏置，训练免调地解耦语义与结构 / Reframes attention sinks/register tokens as structural bias in the attention manifold, training-freely disentangling semantic from structural attention. |
| [[2607.24502]] RoPE Self-Attention Dynamics | 严格分析 RoPE 注入球形自注意力后的动力学，给出 Bessel-混叠共识谱与扭转平衡分支 / Rigorous analysis of RoPE-injected spherical self-attention dynamics, yielding a Bessel-aliasing consensus spectrum and twisted equilibria. |

### B. 自我改进 / 编码 / 自主研究 Agent / Self-Improving, Coding & Autonomous-Research Agents

| Paper | 概述 / Overview |
|-------|-----------------|
| [[2607.24300]] Self-Authored Verification Unreliable | 揭示启发式自改进 Agent 中"验证者-部署鸿沟"：自评分虚高而真实性能退化 / Exposes a verifier–deployment gap in heuristic self-improving agents where self-scores stay inflated while real performance degrades. |
| [[2607.24647]] Efficiency Matters in Autonomous Research | 提出以搜索效率（Pareto AUC）为 AR 评估首要目标，并设计 fluid search（UCB 组合 bandit）逼近 per-task oracle / Proposes search efficiency (Pareto AUC) as a first-class AR metric; fluid search (UCB bandit portfolio) near-matches the per-task oracle. |
| [[2607.24604]] Looping Is Not Reliability (StateSeal) | 证明编码 Agent 的"生成-测试-修订"循环本身不保证可靠性，并提出证据-状态绑定、带类型动作的修订契约 / Shows generate-test-revise loops in coding agents do not guarantee reliability; proposes evidence-state-bound, typed-action revision contracts (StateSeal). |
| [[2607.24459]] SciConsolidate | 将执行验证经验抽象为程序性知识并具体化为代码监督，揭示"抽象-执行鸿沟"，9B 学生在无程序部署下显著提升 / Consolidates verified execution experience into procedural knowledge (SOPs) then concretizes to code supervision; reveals an abstraction–execution gap. |
| [[2607.24419]] RecursiveECG | LLM-as-Designer Agent 从具体失败递归精修 ECG 分类器，证据驱动地补齐指标盲区 / An LLM-as-Designer agent recursively refines ECG classifiers from concrete failures, evidence-drivenly filling metric blind spots. |
| [[2607.23975]] Plato-Bio | 验证优先的科学代理基础设施，含历史重发现基准与 AlphaFold 结构对比，作为可审计基线而非发现声明 / Verification-first scientific-agent infrastructure with temporal-rediscovery benchmark and AlphaFold structural screen, shipped as an auditable baseline. |
| [[2607.23942]] Cognitive Architectures → Language Agents | 机制级综述用七字段重构法与双轴证据编码，将历史认知架构与现代语言 Agent 运行时映射为可审计迁移账本 / Mechanism-level review mapping historical cognitive architectures to modern language-agent runtimes via a 7-field reconstruction and dual-axis evidence coding. |
| [[2607.23925]] Greedy Dynamical Meta-Learning | 纯概念性框架，将元学习重构为对随机动力系统两个时间尺度（变异 µ/评估 ν）的整定问题 / A purely conceptual framework reframing meta-learning as tuning two timescales (mutation µ / evaluation ν) of a stochastic dynamical system. |

### C. LLM 训练稳定性、强化学习与训练动力学 / Training Stability, RL & Training Dynamics

| Paper | 概述 / Overview |
|-------|-----------------|
| [[2607.24062]] ACRL | 自适应控制训练-推理差异（含低精度量化），稳定 LLM 强化学习，解决 GRPO 训练中的重要性采样偏移 / Adaptively controls training-inference discrepancy (incl. low-precision quantization) to stabilize LLM RL, fixing importance-sampling drift in GRPO. |
| [[2607.23967]] Grokking on the Weight-Decay Clock | 为线性模型 grokking 给出严格可解的"权重衰减时钟"机制，导出精确离散速率与迭代尺度律 / An exactly-solvable "weight-decay clock" mechanism for grokking in linear models, deriving exact discrete rates and iteration-scale laws. |
| [[2607.23970]] Mode Connectivity in Unlearning (MCU) | 首次将模式连通性引入机器遗忘，揭示遗忘损失地形平滑性、近似与重训练机制本质不同 / First application of mode connectivity to machine unlearning, revealing smooth forgetting landscapes and a mechanistic gap between approximate and retrained unlearning. |
| [[2607.24484]] What do Reward Models Memorize? | 首次将反事实记忆引入奖励模型，揭示三类记忆缺陷（高 margin 对、数据集伪影、启发式过度泛化）/ First application of counterfactual memorization to reward models, exposing three memorization deficits that undermine context-sensitive quality judgments. |
| [[2607.24726]] Global Convergence of DGM/PINN | 首次对非线性半线性 PDE 的 DGM/PINN 训练证明全局收敛（截断梯度下降下收敛到唯一弱解）/ First global-convergence proof for DGM/PINN training on nonlinear semi-linear PDEs via clipped gradient descent, converging to the unique weak solution. |

### D. 计算可靠性与量化 / Computation Reliability & Quantization

| Paper | 概述 / Overview |
|-------|-----------------|
| [[2607.24377]] MXAttention | 数据免调的 MXFP4 注意力量化，解决 power-of-two 缩放与 softmax 归一化数值误差 / Data-free MXFP4 attention quantization resolving power-of-two scaling and softmax-normalization numerical errors. |
| [[2607.24692]] Denial of Deadline | 揭示分布式推理管线的新型攻击面：Yo-Yo 突发请求挤占慢路径使高精度云端预测超时丢弃，致精度坍塌 / Exposes a new attack surface in distributed inference pipelines where burst requests starve the slow path, causing accuracy collapse. |
| [[2607.24568]] Bit-Accurate FPGA Feature Gating | 比特精确 FPGA 对照实验表明学习型特征门只增硬件代价而无分类收益 / Bit-accurate FPGA ablation showing a learned feature gate adds pure hardware overhead with no accuracy benefit for the compressed feature representation. |
| [[2607.24440]] Bigger or Cheaper? (VLM Uncertainty) | 模型变大提升错误检测（AUROC 0.80→0.98），4-bit 量化几乎不损精度但严重破坏置信度信号 / Scaling lifts error-detection AUROC 0.80→0.98; 4-bit quantization barely hurts accuracy (−1.6 pp) but severely degrades confidence signals. |

### E. 评估失效模式与基准完整性 / Evaluation Failure Modes & Benchmark Integrity

| Paper | 概述 / Overview |
|-------|-----------------|
| [[2607.24268]] Accuracy Hides How LMs Fail | 双层评估（执行证据 + 评分验证）在匹配预算下揭示：准确率混淆了执行状态分布与评分策略 / A two-layer (execution-evidence + scoring-verification) framework shows accuracy conflates execution case mix with verification policy under matched budgets. |
| [[2607.24054]] AcquaBench (Success Provenance) | CLEAN/GOLD/SHAM 值替换审计揭示 Agent 基准成功可能依赖评估期获取的目标值而非授权信息 / CLEAN/GOLD/SHAM value-substitution audit shows agent-benchmark success may track acquired target values rather than authorized information. |
| [[2607.24176]] Staged Bottleneck Localization | 分阶段验证协议定位压缩短文本生成管线的主要语义损失在编码器重建阶段而非隐空间生成 / Staged validation localizes the main semantic loss in compressed short-text generation to the encoder-reconstruction stage, not latent generation. |
| [[2607.24577]] Evaluating Fuzz Testing for RL | 系统评估面向 RL Agent 的模糊测试方法在发现失效上的有效性 / Systematic evaluation of fuzz-testing methods' effectiveness at discovering failures in RL agents. |
| [[2607.24519]] Stress-Testing EEG Foundation Models | 对六个 EEG 基础模型做冻结线性探针压测，发现数据集身份近乎完美可解码，REVE 预训练反逊于随机初始化 / Stress-tests six EEG foundation models under frozen probing; dataset identity is near-perfectly decodable, and pretrained REVE can lose to random init. |

### F. 共形预测与统计保证 / Conformal Prediction & Statistical Guarantees

| Paper | 概述 / Overview |
|-------|-----------------|
| [[2607.24562]] HG-CRC | 无需重训练的后处理框架，为 LLM 选择性预测提供跨用户定义分组层级的"同时"风险保证 / A post-hoc, retrain-free framework providing simultaneous risk guarantees across user-defined group hierarchies for LLM selective prediction. |
| [[2607.24343]] Role-Stratified CRC for LLM Tool Calls | 角色/字段分层的共形风险控制，为 LLM 工具调用参数提供形式化逐字段风险预算 / Role-/field-stratified conformal risk control providing formal per-field risk budgets for LLM tool-call arguments. |
| [[2607.24401]] proxymate | 四层（代表性/单元/估计/域）代理指标诊断-调整框架，在 Meta 生产场景中拒绝误用代理 / A four-tier proxy-estimate diagnosis-and-adjustment framework, rejecting proxy misuse across Meta production scenarios. |

### G. 统计、优化与理论基础 / Statistical, Optimization & Theoretical Foundations

| Paper | 概述 / Overview |
|-------|-----------------|
| [[2607.23914]] Online PCA Phase Transition | 严格证明 Oja 在线 PCA 相变由 n/(d·log d) 决定（非离线的 n/d），给出精确阈值与临界窗口随机极限 / Proves Oja's online-PCA phase transition is governed by n/(d·log d), not n/d, with exact thresholds and a random critical-window limit law. |
| [[2607.24041]] Zero Pattern Drives Multiple Descent | 证明过参数化回归中协方差秩亏损（零模式）与样本依赖性本身驱动多次下降，给出 Dulmage-Mendelsohn 组合定位规则 / Proves covariance rank-loss (zero pattern) and sample dependence alone drive multiple descent in over-parameterized regression, with a Dulmage-Mendelsohn localization rule. |
| [[2607.24235]] Minimax Lower Bounds (MMD/HSIC/KSD) | 用 Le Cam 两点法在一般拓扑空间对无界核证明 MMD/HSIC/KSD 估计的极小化极大下界均为 n^{-1/2}，与上界匹配 / Proves matching n^{-1/2} minimax lower bounds for MMD/HSIC/KSD estimation over general topological spaces with unbounded kernels. |
| [[2607.24662]] Temporal Graph Drift Impossibility | 给出时序图生成中分布漂移观测校正的形式化不可能性结果（锐化-漂移张力）/ A formal impossibility result for observation-based correction of distribution drift in temporal graph generation (sharpening–drift tension). |

### H. 前沿模型、安全与认知 / Frontier Models, Safety & Cognition

| Paper | 概述 / Overview |
|-------|-----------------|
| [[2607.24653]] Kimi K3 | Moonshot 首个开源 3T 级 MoE（总参 2.8T、激活 104B、1M 上下文），较 K2 约 2.5× scaling 效率，全面领先其他开源模型 / Moonshot's first open 3T-class MoE (2.8T total / 104B active / 1M context), ~2.5× scaling efficiency over K2, leading open-weights across agent/coding/knowledge benchmarks. |
| [[2607.24243]] Epistemic Norms for AI Safety (ECAISA) | 论证 AI 安全研究需以"证明危险不存在"和"灾难尾部风险"为评估范式，提出含八原则的审核治理框架 / Argues AI-safety research must prove absence-of-hazard and bound worst-case tail risk; proposes an 8-principle epistemic audit framework (ECAISA). |
| [[2607.23927]] Reality Monitoring in LLMs | 将认知心理学"现实监控"范式移植到 LLM，发现区分自生成/外部信息的能力随对话记忆结构动态变化 / Ports cognitive-psychology "reality monitoring" to LLMs, finding self-generated vs. externally-provided discrimination shifts dynamically with conversation-memory structure. |

---

## All Papers

| # | arXiv ID | Title | Topic |
|---|----------|-------|-------|
| 1 | [[2607.23914]] | The Phase Transition in Online PCA Depends on n/d log(d), not n/d | Statistical foundations / 统计基础 |
| 2 | [[2607.23925]] | Greedy Dynamical Meta-Learning | Meta-learning / 元学习 |
| 3 | [[2607.23927]] | Reality Monitoring in Large Language Models | Cognition & safety / 认知与安全 |
| 4 | [[2607.23942]] | From Cognitive Architectures to Language Agents | Agent review / 智能体综述 |
| 5 | [[2607.23967]] | Grokking on the Weight-Decay Clock | Training dynamics / 训练动力学 |
| 6 | [[2607.23970]] | Understanding Machine Unlearning Through Mode Connectivity | Unlearning / 遗忘 |
| 7 | [[2607.23975]] | Plato-Bio: Verification-First Biological Novelty Screening | Autonomous science / 自主科研 |
| 8 | [[2607.24017]] | Disentangling Semantic Attention from Structural Bias | Interpretability / 可解释性 |
| 9 | [[2607.24041]] | The Zero Pattern of a Design Matrix Drives Multiple Descent | Regression theory / 回归理论 |
| 10 | [[2607.24054]] | Success Is Not Self-Explanatory (AcquaBench) | Agent evaluation / 智能体评估 |
| 11 | [[2607.24062]] | ACRL: Adaptive Control of Training-Inference Discrepancy | LLM RL training / LLM 强化学习训练 |
| 12 | [[2607.24176]] | Where Quality Breaks in Compressed Short-Text Generation | Text generation / 文本生成 |
| 13 | [[2607.24235]] | Minimax Lower Bounds of Kernel Discrepancy Estimation | Statistical theory / 统计理论 |
| 14 | [[2607.24243]] | Epistemic Norms for AI Safety and Alignment Research | AI safety / AI 安全 |
| 15 | [[2607.24268]] | Accuracy Hides How Language Models Fail | LLM evaluation / LLM 评估 |
| 16 | [[2607.24300]] | Self-Authored Verification Is Unreliable in Self-Improving Agents | Self-improving agents / 自改进智能体 |
| 17 | [[2607.24343]] | Beyond Aggregate Risk: Role-Stratified CRC for LLM Tool Calls | Conformal prediction / 共形预测 |
| 18 | [[2607.24377]] | MXAttention: Data-Free MXFP4 Attention Quantization | Quantization / 量化 |
| 19 | [[2607.24401]] | proxymate: Diagnosis and Adjustment of Proxy Estimates | Statistical inference / 统计推断 |
| 20 | [[2607.24419]] | Failures Reveal What Metrics Miss (RecursiveECG) | Self-evolving agent / 自演化智能体 |
| 21 | [[2607.24425]] | Context Is King: Geometry of Concepts | Representation geometry / 表示几何 |
| 22 | [[2607.24440]] | Bigger or Cheaper? Scale & Quantization on VLM Uncertainty | VLM uncertainty / 视觉语言模型不确定性 |
| 23 | [[2607.24459]] | From Execution to Capability (SciConsolidate) | Self-improving LLM / 自改进 LLM |
| 24 | [[2607.24471]] | Grounding Latent Algorithm Routing in Transformer Reasoning | Mechanistic interp / 机制可解释性 |
| 25 | [[2607.24484]] | What do Reward Models Memorize? | Reward models / 奖励模型 |
| 26 | [[2607.24502]] | Self-Attention Dynamics with Rotary Position Embeddings | Transformer dynamics / Transformer 动力学 |
| 27 | [[2607.24519]] | Stress-Testing EEG Foundation Models | Foundation-model eval / 基础模型评估 |
| 28 | [[2607.24562]] | Hierarchical Group-Conditional Conformal Risk Control | Conformal prediction / 共形预测 |
| 29 | [[2607.24568]] | Bit-Accurate FPGA Evaluation of Learned Feature Gating | Hardware/quantization / 硬件量化 |
| 30 | [[2607.24577]] | Evaluating Fuzz Testing for Reinforcement Learning Agents | RL testing / RL 测试 |
| 31 | [[2607.24586]] | D-Score: Spectral Hidden-State Signal for Hallucination | Hallucination detection / 幻觉检测 |
| 32 | [[2607.24604]] | Looping Is Not Reliability (StateSeal) | Coding agents / 编码智能体 |
| 33 | [[2607.24645]] | Sparse Autoencoders Encode Both Concepts and Functions (FEGA) | Mechanistic interp / 机制可解释性 |
| 34 | [[2607.24647]] | Efficiency Matters in Autonomous Research (Fluid Search) | Autonomous research / 自主科研 |
| 35 | [[2607.24653]] | Kimi K3: Open Frontier Intelligence | Frontier model / 前沿模型 |
| 36 | [[2607.24662]] | Distribution Drift Correction Impossibility in Temporal Graphs | Graph generation / 图生成 |
| 37 | [[2607.24692]] | Denial of Deadline: Network-Driven Accuracy Collapse | Distributed inference / 分布式推理 |
| 38 | [[2607.24726]] | Global Convergence of DGM and PINN Algorithms for PDEs | PDE solvers / PDE 求解 |

---

## 计数核验 / Count Verification

- **Overview 中收录的论文数 / Papers in this overview:** 38
- **目录中实际 `.md` 文件数（排除 overview.md）/ Actual `.md` files in directory (excluding overview.md):** 38
- **状态 / Status:** ✓ 匹配 / Match confirmed. No discrepancy.
