---
title: "Daily Paper Overview — 2026-06-26"
date: 2026-06-26
tags: [daily-overview, 2026-06-26]
papers: 50
---

# 📰 每日论文速递 / Daily Paper Overview — 2026-06-26

> 共筛选 50 篇相关论文（共检索 311 篇）。/ 50 relevant papers selected (out of 311 fetched).

## 🔥 今日必读 / Must Read Today

### 1. [[2606.28116]] — Mechanism-Driven Monitors for LLM Training Instability
> **为什么必读：** 该工作提出"机制驱动"的训练监测范式，从模块功能角色推导内部指标，在低精度 FlashAttention 与 MoE 路由器上实现训练失稳的提前数千步预警——直击大模型训练可观测性的核心痛点。
> **Why must-read:** It derives module-internal monitors from each module's functional role, flagging training instability thousands of steps before loss divergence—directly advancing LLM training observability.

### 2. [[2606.28277]] — Google's Paper Assistant Tool for Automated Scientific Review
> **为什么必读：** 谷歌基于推理缩放的智能体框架可在投稿前自动验证数学证明与实验，在 STOC/ICML 试点中服务 4700+ 篇投稿，是 AI 介入同行评审的标志性规模化实践。
> **Why must-read:** An agentic pipeline built on inference-scaling that validates proofs and experiments pre-submission across 4,700+ STOC/ICML papers—a landmark, at-scale deployment of AI in peer review.

### 3. [[2606.28432]] — Spectral Perturbation of the Fisher Matrix under Weight Quantization
> **为什么必读：** 用 Weyl 特征值扰动理论严格证明权重量化噪声会抬高经验 Fisher 矩阵的最大特征值，为"部署期谱监控阈值必须按目标硬件实测量化校准"提供了理论机制解释。
> **Why must-read:** A clean theoretical result proving quantization noise inflates the Fisher matrix's dominant eigenvalue, explaining why runtime spectral-monitoring thresholds must be hardware-calibrated.

## 📂 按主题分类 / Papers by Topic

### 可解释性与机制分析 / Interpretability & Mechanistic Analysis

| 论文 / Paper | 一句话总结 / TL;DR | 相关度 |
|---|---|---|
| [[2606.27941]] VASAE | 在 SAE 训练中加入词汇对齐锚定损失，让每个字典方向获得内在 token 名称。/ Vocabulary-aligned anchor loss gives each SAE decoder direction an intrinsic token name. | ⭐⭐⭐⭐⭐ |
| [[2606.28153]] Robust Harmful Features | 越狱攻击只抑制早期 ACHs，中层 SAHs 仍鲁棒激活，支持免训练内部激活检测。/ Jailbreaks selectively suppress early-layer heads while safety heads keep firing; enables training-free detector. | ⭐⭐⭐⭐⭐ |
| [[2606.28273]] Vision-Default, Prior-Override | VLM 感知-知识冲突呈"视觉默认、先验覆盖"不对称因果，依赖 2.5–4.8% 稀疏路由/写入头。/ Visual grounding is default; prior knowledge depends on a sparse 2.5–4.8% set of late-layer heads. | ⭐⭐⭐⭐⭐ |
| [[2606.28548]] Turn-Averaged SAEs | 在对话回合平均隐藏状态上训练 SAE，使特征规模与上下文长度解耦，简化长上下文归因。/ SAEs on turn-averaged hidden states decouple feature scale from context length. | ⭐⭐⭐⭐⭐ |
| [[2606.27679]] Probe-Based Uncertainty | 探针式不确定性估计的分解研究：简单特征域内占优，结构化特征分布偏移下更鲁棒。/ Factorised study: simple features dominate in-domain, structured features transfer better under shift. | ⭐⭐⭐⭐ |
| [[2606.28050]] LLM Self-Evaluation Asymmetry | 受控 QA 下自评并非总比生成容易，评测器对上下文关注度下降 3–5×。/ Self-eval isn't uniformly easier than generation; evaluator de-attends to context 3–5×. | ⭐⭐⭐⭐ |
| [[2606.28455]] Object-State World Models | 被动世界模型隐藏状态编码事件信息并重新加权运动/接触/客体恒常性潜场。/ Hidden states encode event-regime info and reweight kinematic/contact/permanence latent fields. | ⭐⭐⭐⭐ |
| [[2606.28615]] Explanation Sufficiency | 将特征归因充分性推广到自由文本解释，证明充分性相对输入分布。/ Generalizes attribution sufficiency to free-text explanations; shows they're generally insufficient. | ⭐⭐⭐⭐ |
| [[2606.28589]] DynaSteer | 免训练动态表示编辑，在高熵推理分叉处注入纯化真相转向向量。/ Training-free RepE that injects a purified truth steering vector at high-entropy reasoning forks. | ⭐⭐⭐⭐ |

### 训练稳定性与优化 / Training Stability & Optimization

| 论文 / Paper | 一句话总结 / TL;DR | 相关度 |
|---|---|---|
| [[2606.28116]] Mechanism-Driven Monitors | 从模块功能角色推导监测指标，提前数千步预警低精度注意力与 MoE 路由失稳。/ Module-internal monitors flag instability thousands of steps before loss divergence. | ⭐⭐⭐⭐⭐ |
| [[2606.28438]] Recursive Self-Training Collapse | 代码 LLM 递归自训练在各评审机制下都崩溃，AI 自评退化为橡皮图章。/ Recursive self-training collapses under all review regimes; AI self-review degrades to rubber-stamping. | ⭐⭐⭐⭐⭐ |
| [[2606.27634]] Continual Personalization Stability | 序列化 LoRA 个性化下 KL 散度作为阶序无关的模型崩溃早预警信号。/ KL divergence acts as an order-invariant early-warning signal of model collapse in sequential LoRA. | ⭐⭐⭐⭐ |
| [[2606.27715]] Aurora Optimizer | Muon 在高瘦 MLP 上致神经元死亡，Aurora 强制行更新均匀并保留极分解几何。/ Aurora enforces uniform row updates, fixing Muon's neuron death on tall MLP matrices. | ⭐⭐⭐⭐ |
| [[2606.28486]] Spectral Phase Transitions | 将训练建模为随机矩阵演化，刻画 BBP 谱相变与可训练性相图。/ Recasts training as random-matrix evolution; maps a trainability phase diagram via BBP transitions. | ⭐⭐⭐⭐ |
| [[2606.27759]] Layerwise Progressive Freezing | 逐层渐进冻结二值网络，隔离激活导致的梯度阻塞为核心训练难点。/ Progressive layer freezing isolates activation-induced gradient blockades as the core binary-net difficulty. | ⭐⭐⭐ |
| [[2606.27855]] Memorization Indicators | 激活率记忆指标可作为低样本微调过拟合的早预警无验证信号。/ Activation-rate memorization indicators give a validation-free early overfitting signal. | ⭐⭐⭐ |
| [[2606.28123]] Dangerous Liaisons | 凸学习中单调性保持当且仅当聚合规则正仿射，非仿射聚合破坏末轮收敛。/ Monotonicity preserved iff aggregation is positively affine; non-affine rules break last-iterate convergence. | ⭐⭐⭐ |
| [[2606.28242]] Width & Data Scaling Laws | 可解二次网络中有限宽度作为隐式正则，调宽或正则可达贝叶斯最优率。/ Finite width acts as implicit regularizer; optimal width/regularization reaches Bayes-optimal rates. | ⭐⭐⭐ |

### 量化与高效推理 / Quantization & Efficient Inference

| 论文 / Paper | 一句话总结 / TL;DR | 相关度 |
|---|---|---|
| [[2606.28432]] Fisher Spectral Perturbation | Weyl 理论证明权重量化噪声抬高 Fisher 最大特征值，监控阈值需硬件校准。/ Proves quantization noise inflates Fisher's dominant eigenvalue; thresholds need hardware calibration. | ⭐⭐⭐⭐⭐ |
| [[2606.27884]] SEADA | 协同优化层精度与工作负载映射的多精度空间加速器方法，单次微调即大幅节能。/ Co-optimizes precision and mapping on multi-precision spatial accelerators in one fine-tune pass. | ⭐⭐⭐⭐ |
| [[2606.27949]] Mixed-Precision Energy | Verifarlot 驱动混合精度在 HPC 求解器上节能达约 30% 且保精度。/ Verificarlo-driven mixed precision cuts time/energy ~30% on HPC solvers while keeping accuracy. | ⭐⭐⭐⭐ |
| [[2606.28565]] KernelSight-LM | 仅凭数据表预测未见 GPU 上逐内核延迟的内核级推理模拟器。/ Kernel-level LLM inference simulator predicting per-kernel latency from datasheets alone. | ⭐⭐⭐⭐ |
| [[2606.28529]] Speedup Paradox | 具身闭环控制下有损推理优化呈非单调任务级效应，甜点随硬件漂移。/ Lossy inference optimization in embodied control yields non-monotonic task-level effects. | ⭐⭐⭐⭐ |
| [[2606.27743]] End-to-End Dynamic Sparsity | 注入预算门控使单一冻结 LLM 按资源动态跳层/剪头/裁推理 token。/ Budget-conditioned gating lets one frozen LLM trace the accuracy-cost Pareto frontier. | ⭐⭐⭐ |
| [[2606.27785]] Output-Space Compression | 用白化输出误差替换 ROCKET 权重空间分配成本，精度微升但困惑度变差。/ Replacing ROCKET's weight-space cost with whitened output error gives small gain, worse perplexity. | ⭐⭐⭐ |
| [[2606.27797]] Teacher-Student Distillation | 解耦师生分区并加拓扑感知模型，Llama-3 HPC 上吞吐提升达 67%。/ Decoupled teacher/student partitioning gives up to 67% higher throughput on Llama-3 HPC clusters. | ⭐⭐⭐ |

### 智能体与自动化研究 / Agents & Automated Research

| 论文 / Paper | 一句话总结 / TL;DR | 相关度 |
|---|---|---|
| [[2606.28277]] Paper Assistant Tool | 基于推理缩放的智能体评审流水线，STOC/ICML 试点服务 4700+ 篇投稿。/ Agentic inference-scaling review pipeline serving 4,700+ STOC/ICML submissions. | ⭐⭐⭐⭐⭐ |
| [[2606.28279]] HORIZON Agentic Hardware | 将 RTL 设计视为仓库级代码进化，四套基准全部收敛到 100% 通过率。/ Hands-free self-evolving agent drives four RTL benchmark suites to 100% completion. | ⭐⭐⭐⭐⭐ |
| [[2606.28471]] Data-Eval Closed-Loop | 用"能力切片"打通评测与训练数据，将基准失败转为可测试的数据干预。/ The "capability slice" bridges eval and training data, turning failures into testable interventions. | ⭐⭐⭐⭐⭐ |
| [[2606.28430]] Coding Agents Build-to-Test | 受控研究显示编码智能体交付被测行为而非请求的可复用库。/ Copilot agents deliver tested behavior, not the requested reusable library. | ⭐⭐⭐⭐ |
| [[2606.27757]] Symbolic Self-Refinement | 神经符号框架用多维符号验证器迭代自精炼长程规划。/ Neural-symbolic framework with a symbolic verifier iteratively self-refines long-horizon plans. | ⭐⭐⭐ |
| [[2606.27806]] GILP | 参数化世界模型骨干加 Jaccard 一致性门，幻觉状态率降 80%。/ Parameterized world-model backbone cuts hallucinated-state rate 80% in agents. | ⭐⭐⭐ |
| [[2606.27814]] ATOD | 多轮智能体混合策略蒸馏，退火教师蒸馏与奖励驱动 GRPO。/ Hybrid on-policy distillation anneals teacher distillation into reward-driven GRPO for multi-turn agents. | ⭐⭐⭐ |
| [[2606.28235]] Govern the Repository | 集成摩擦是不可简化的仓库级属性，智能体 PR 风险约为人工 2×。/ Integration friction is irreducible repository-level risk, ~2× higher in agent-authored PRs. | ⭐⭐⭐ |

### 安全、对齐与鲁棒性 / Safety, Alignment & Robustness

| 论文 / Paper | 一句话总结 / TL;DR | 相关度 |
|---|---|---|
| [[2606.28525]] Gravitational Fine-Tuning Reversion | 把对齐安全侵蚀重述为向早期有用流形的引力回归，因果阻断该方向有害率 19→8.5%。/ Reframes safety erosion as gravitational reversion; blocking the witness direction cuts harmfulness 19→8.5%. | ⭐⭐⭐⭐ |
| [[2606.28639]] Undecidability of AGI Alignment | 证明 AGI 对齐结构上不可验证，可靠-完备-可行三难是描述复杂性的必然结果。/ Proves AGI alignment is structurally unverifiable; the Soundness-Completeness-Tractability trilemma is necessary. | ⭐⭐⭐⭐ |
| [[2606.27622]] FoggyTrust | 两级雾节点层级信任联邦学习，异质感知全局优化器提升非 IID 鲁棒性。/ Two-level fog-node hierarchical trust improves federated robustness in non-IID settings. | ⭐⭐⭐ |
| [[2606.27632]] Yuvion LLM | 阿里将安全视为对抗属性，渐进式流水线超越更大模型。/ Alibaba safety LLM treats safety as adversarial, outperforming much larger models. | ⭐⭐⭐ |
| [[2606.27685]] AC-IHT | 对抗污染下双阈值 AC-IHT 达信号自适应极小极大近最优估计。/ Two-stage AC-IHT achieves signal-adaptive minimax-optimal estimation under adversarial contamination. | ⭐⭐⭐ |
| [[2606.27694]] Halt Fast | 元学习 anytime-valid E-value 把随机平滑认证成本降低约 20×。/ Meta-learned anytime-valid E-values cut randomized smoothing certification cost ~20×. | ⭐⭐⭐ |
| [[2606.27709]] Low-Agreeableness Persona | 改写用户轮为低宜人性人格，无需安全标签即降低越狱与有害输出。/ Rewriting user turns as low-agreeableness cuts jailbreak rates without safety labels. | ⭐⭐⭐ |
| [[2606.27786]] SHIFT | 将知识冲突干预重构为 FFN 上可学习门控调制，冻结骨干训练 <0.01% 参数。/ Reframes knowledge-conflict intervention as learnable FFN gate modulation, training <0.01% of params. | ⭐⭐⭐ |

### 评测、理论与系统 / Evaluation, Theory & Systems

| 论文 / Paper | 一句话总结 / TL;DR | 相关度 |
|---|---|---|
| [[2606.27934]] Self-Verifying Measurement Records | 用内容哈希把硬件基准数值绑定到观测与验证记录，构成防篡改证据图谱。/ Hash-links every benchmark number to its observation, making a tamper-evident evidence graph. | ⭐⭐⭐⭐⭐ |
| [[2606.28534]] Resilient Multi-GPU PIC | BIT1 等离子 PIC/MC 的可移植 MPI+OpenMP 扩展，Frontier 上扩展至 800 GPU、29× 加速。/ Portable hybrid BIT1 extension scales to 800 GPUs on Frontier with 29× speedup. | ⭐⭐⭐⭐ |
| [[2606.27666]] MultModLM | 首个 RTL 到硬件原理图的多模态基准，LLM 评委与人工 κ≈0。/ First RTL-to-schematic multimodal benchmark; LLM-as-judge shows κ≈0 vs humans. | ⭐⭐⭐ |
| [[2606.27687]] Preregistering for Next LLM | 预注册实验并在发布后的首个 LLM 上确认，规避 p-hacking。/ Preregister then confirm on the first LLM released afterward, defeating p-hacking. | ⭐⭐⭐ |
| [[2606.27780]] Graph World Model Rollout | 把 rollout 误差理论推广到图结构世界模型，提出拓扑感知误差放大因子。/ Extends rollout-error theory to graph world models with a topology-aware amplification factor. | ⭐⭐⭐ |
| [[2606.27895]] Mosaic | 包装 14 个可微 PDE 求解器的统一基准套件，暴露梯度精度/代价差异。/ Uniform benchmark wrapping 14 differentiable PDE solvers, surfacing gradient cost/accuracy gaps. | ⭐⭐⭐ |
| [[2606.27997]] Rank-Preserving Selection | 把基准子集选择框定为保序问题，几何选择在表征充分时远优于随机。/ Frames dataset selection as rank preservation; geometry-based selection preserves rankings far better. | ⭐⭐⭐ |
| [[2606.28013]] Signal-Coverage Matrix | 用 2×2 信号覆盖矩阵分解 autoformalization 的类型层与语义误差。/ A 2×2 signal-coverage matrix decomposes autoformalization type vs semantic errors. | ⭐⭐⭐ |

## 📋 全部论文 / All Papers

| ID | 标题 / Title | 相关度 |
|---|---|---|
| [[2606.27622]] | FoggyTrust: Robust Federated Learning with Hierarchical Trust Networks | 3 |
| [[2606.27632]] | Yuvion LLM: An Adversarially-Aware LLM for Content and AI Safety | 3 |
| [[2606.27634]] | Continual Learning for Sequential Personalization of Small Language Models | 4 |
| [[2606.27666]] | MultModLM: A Multi-Modal Benchmark for Hardware Schematic Generation | 3 |
| [[2606.27679]] | From Signals to Transfer: Probe-Based Uncertainty Estimation in LLMs | 4 |
| [[2606.27685]] | Adversarial Contamination Meets Hard Thresholding (AC-IHT) | 3 |
| [[2606.27687]] | Mitigating LLM-Based p-Hacking by Preregistering for the Next LLM | 3 |
| [[2606.27694]] | Halt Fast! Early Stopping for Certified Robustness | 3 |
| [[2606.27709]] | Low-Agreeableness Persona Conditioning for Safe LLM Fine-Tuning | 3 |
| [[2606.27715]] | Aurora: A Leverage-Aware Spectral Optimizer | 4 |
| [[2606.27743]] | End-to-End Dynamic Sparsity for Resource-Adaptive LLM Inference | 3 |
| [[2606.27757]] | Towards Reliable and Robust LLM Planning: Symbolic Self-Refinement | 3 |
| [[2606.27759]] | Layerwise Progressive Freezing for Depth-Scalable Binary Networks | 3 |
| [[2606.27780]] | Understanding Rollout Error in Graph World Models | 3 |
| [[2606.27785]] | Output-Space Allocation Costs for Calibration-Guided LLM Compression | 3 |
| [[2606.27786]] | SHIFT: Gate-Modulated Activation Steering for Knowledge Conflict in RAG | 3 |
| [[2606.27797]] | Optimizing Teacher-Student Partitioning for Scalable Knowledge Distillation | 3 |
| [[2606.27806]] | GILP: Parameterized World Models Reduce Hallucination in LLM Agents | 3 |
| [[2606.27814]] | ATOD: Annealed Turn-aware On-policy Distillation for Multi-turn Agents | 3 |
| [[2606.27855]] | Memorization Indicators for Early Spotting of Overfitting (sEMG) | 3 |
| [[2606.27884]] | SEADA: Mixed-Precision DNNs on Multi-Precision Spatial Architectures | 4 |
| [[2606.27895]] | Mosaic: A Benchmark Suite for Differentiable Physics Solvers | 3 |
| [[2606.27934]] | Self-Verifying Measurement Records: Hash-Linked Evidence Graphs | 5 |
| [[2606.27941]] | VASAE: Naming SAE Dictionary Directions with Vocabulary-Aligned Anchoring | 5 |
| [[2606.27949]] | Mixed-Precision for Energy Efficient Computations | 4 |
| [[2606.27997]] | Benchmarking on Tasks That Matter: Dataset Selection for Rankings | 3 |
| [[2606.28013]] | The Signal-Coverage Matrix: Stratifying Errors in Autoformalization | 3 |
| [[2606.28050]] | Can LLMs Judge Better Than They Generate? Task Asymmetry & Interpretability | 4 |
| [[2606.28116]] | Mechanism-Driven Monitors for Preemptive Detection of LLM Training Instability | 5 |
| [[2606.28123]] | Dangerous Liaisons of Convex Learning and Non-Affine Aggregation | 3 |
| [[2606.28153]] | Robust Harmful Features Under Jailbreak Attacks: Attention Head Specialization | 5 |
| [[2606.28235]] | Govern the Repository, Not the Agent: Ecosystem-Level Risk in AI-Native Software | 3 |
| [[2606.28242]] | How Width and Data Shape Generalization Scaling Laws in Quadratic Networks | 3 |
| [[2606.28273]] | Vision-Default, Prior-Override: Perception-Knowledge Conflict in VLMs | 5 |
| [[2606.28277]] | Towards Automating Scientific Review with Google's Paper Assistant Tool | 5 |
| [[2606.28279]] | Agentic Hardware Design as Repository-Level Code Evolution (HORIZON) | 5 |
| [[2606.28430]] | Building to the Test: Coding Agents Deliver What You Check | 4 |
| [[2606.28432]] | Spectral Perturbation of the Empirical Fisher Matrix under Weight Quantization | 5 |
| [[2606.28438]] | When AI Reviews Its Own Code: Recursive Self-Training Collapse in Code LLMs | 5 |
| [[2606.28455]] | Event-Conditioned Diagnostics of Object-State World Models | 4 |
| [[2606.28471]] | Data and Evaluation Closed-Loop for Model Capability Enhancement | 5 |
| [[2606.28486]] | Spectral Phase Transitions and Trainability in Neural Network Learning Dynamics | 4 |
| [[2606.28525]] | A Gravitational Interpretation of Fine-Tuning Reversion | 4 |
| [[2606.28529]] | The Speedup Paradox: Inference Speed-Quality Trade-off in Embodied Tasks | 4 |
| [[2606.28534]] | High-Performance Resilient Multi-GPU Hybrid Particle-in-Cell Simulations | 4 |
| [[2606.28548]] | Turn-Averaged SAEs for Feature Discovery and Long-Context Attribution | 5 |
| [[2606.28565]] | KernelSight-LM: A Kernel-Level LLM Inference Simulator | 4 |
| [[2606.28589]] | DynaSteer: Dynamic Representation Editing for Steering LLM Trajectories | 4 |
| [[2606.28615]] | What LLMs Explain Is Not What They Believe: Explanation Sufficiency | 4 |
| [[2606.28639]] | The Undecidability of Artificial General Intelligence (AGI) Alignment | 4 |

## 🔗 相关链接
- arXiv listing: https://arxiv.org/list/cs.LG/2026-06-26
- 上一期 / Previous: [[2026-06-25]]
