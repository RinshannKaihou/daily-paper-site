---
title: "Daily Paper Overview — 2026-06-01"
date: "2026-06-01"
tags: ["daily-overview", "arxiv", "machine-learning", "AI-safety", "optimization"]
papers: 50
---

## 今日必读 / Must Read Today

> 从 50 篇论文中精选 3 篇兼具理论深度与工程影响力的工作。

### 1. [[2606.02288]] Massive Spikes in LLMs are Bias Vectors: Mechanistic Uncovering and Spike-Free Quantization

**推荐理由 / Why Read:** 本文将大语言模型中巨大的激活尖峰重新定义为特定 sink token 所承载的刚性向量偏置（而非传统标量偏置），通过定量几何与谱分析揭示了 attention sink 和 value-state drain 的形成机制，并据此提出了跨模态通用的无尖峰后训练量化框架 INSERTQUANT，在 LLaMA 和 ViT 上均实现了高性能低比特量化。这项工作将机制可解释性与量化工程无缝结合，其跨模态泛化能力尤为突出。This paper reframes massive activation spikes as structural vector biases carried by sink tokens, provides rigorous geometric and spectral mechanistic analysis, and proposes INSERTQUANT—a cross-modal post-training quantization framework achieving high-fidelity low-bit quantization on both LLMs and ViTs.

### 2. [[2606.02423]] Investigating and Alleviating Harm Amplification in LLM Interactions

**推荐理由 / Why Read:** 提出了首个针对多轮对话中有害放大现象的系统性基准 HarmAmp（覆盖 12 类风险场景、878 个场景），并设计了基于树形 GRPO 训练的主动式轨迹级安全监控器 TrajSafe。在三个目标模型上显著降低有害性（Llama-3.1-8B 从 86.36% 降至 9.85%），同时保持所有防御方法中最低的过度拒绝率。填补了单轮 jailbreak 研究之外的多轮交互安全空白。This paper introduces the first systematic benchmark for multi-turn harm amplification (HarmAmp) and TrajSafe, a proactive trajectory-level monitor trained with tree-based RL that reduces harmfulness to near-zero while maintaining the lowest over-refusal rate among all defenses.

### 3. [[2606.02398]] A Local Perturbation Theory for Cross-Domain Interference and Recovery in Multi-Domain RL

**推荐理由 / Why Read:** 揭示了多领域 RL 后训练中跨领域干扰的局部化机制——即使全局梯度近乎正交，后续领域训练仍可通过共享计算路径上的二阶曲率效应选择性损害先前领域。提出的"低维冲突子空间"框架与短时刷新恢复策略，在 Code→Math→QA→CW 序列后使 Math 性能从 57.66 恢复至 66.04。This paper shows that cross-domain interference is driven by localized second-order damage in a low-dimensional shared "conflict subspace" rather than global gradient conflict, and demonstrates selective recovery via short domain refresh, fundamentally advancing our understanding of multi-domain RL post-training.

---

## 按主题分类 / Papers by Topic

### 优化与训练动态 / Optimization & Training Dynamics

| 论文 / Paper | 一句话总结 / One-Line Summary |
|-------------|------------------------------|
| [[2606.01521]] GROKtimizer | 基于梯度子空间结构的二阶优化器，利用 FGM 近似 Fisher 信息矩阵的梯度子空间结构 / A gradient-subspace-aware second-order optimizer leveraging FGM to approximate Fisher-like curvature structure |
| [[2606.01787]] ASADPREC | 自适应缩放异步分布式预处理共轭梯度法，解决预处理子空间的 stale gradient 问题 / Adaptive-scaling async distributed preconditioned CG addressing stale gradients in preconditioned subspaces |
| [[2606.01827]] SAM + Polyak Step Size | 将 Sharpness-Aware Minimization 与自适应 Polyak 步长结合，无需学习率调参 / Combines SAM with adaptive Polyak step sizes, eliminating learning-rate tuning |
| [[2606.02078]] Dynamic lp-norm Optimizers | 动态自适应 p-范数优化器，根据梯度统计自动选择最优 p 值 / Dynamically adapts the p-norm exponent based on gradient statistics |
| [[2606.02365]] FOAM | 基于 stale preconditioner 误差自适应调节 damping 与特征分解频率的 Shampoo 优化算法 / Feedback-controlled adaptive damping and EVD-frequency scheduling for Shampoo, reducing EVD calls by 80–95% |
| [[2606.02008]] Meta-Learning Scaling Laws | 元学习样本效率的扩展律，揭示了任务数、支撑集大小与泛化误差之间的幂律关系 / Scaling laws for meta-learning sample efficiency revealing power-law relationships |

### 大模型安全与对齐 / LLM Safety & Alignment

| 论文 / Paper | 一句话总结 / One-Line Summary |
|-------------|------------------------------|
| [[2606.01695]] CANARY | 基于混淆文本检测越狱攻击的实时监控系统，在 7 个基准上达到 SOTA / Real-time jailbreak detection via obfuscated-text detection, achieving SOTA on 7 benchmarks |
| [[2606.02041]] SentGuard | 流式安全监控框架，在生成过程中逐 token 检测有害内容 / Streaming safety monitor detecting harmful content token-by-token during generation |
| [[2606.02111]] Multi-Clip Video Jailbreak | 利用多片段视频输入绕过视频理解模型安全对齐的越狱方法 / Jailbreak exploiting multi-clip video inputs to bypass safety alignment in video understanding models |
| [[2606.02119]] HAMU | 难度感知机器遗忘框架，根据样本硬度自适应调整遗忘强度 / Hardness-aware unlearning framework adapting forgetting intensity to sample hardness |
| [[2606.02423]] HarmAmp / TrajSafe | 首个多轮有害放大基准与基于树形 RL 的主动式轨迹级安全监控器 / First multi-turn harm amplification benchmark and proactive trajectory-level safety monitor |
| [[2606.02530]] SafeSteer | 仅对安全相关 token 进行局部 on-policy 蒸馏的轻量级对齐方法，仅需 100 条有害样本 / Localized on-policy distillation targeting only safety-relevant tokens with only 100 harmful samples |
| [[2606.02562]] BeliefSF / JIST | 信念空间神经安全滤波器的概率安全认证框架，通过"可信推理区域"提升许可性 / Probabilistic safety certification for belief-space neural safety filters via "trusted inference regions" |

### 机制可解释性 / Mechanistic Interpretability

| 论文 / Paper | 一句话总结 / One-Line Summary |
|-------------|------------------------------|
| [[2606.02061]] Archetypal SAE Stability Critique | 对原型稀疏自编码器稳定性假设的系统性批判与修正 / Systematic critique and correction of archetypal SAE stability assumptions |
| [[2606.02288]] Massive Spikes / INSERTQUANT | 揭示 LLM 激活尖峰为 sink token 的刚性向量偏置，提出跨模态无尖峰量化框架 / Reveals activation spikes as rigid vector biases; proposes cross-modal spike-free quantization |
| [[2606.02378]] Attention Circuits Formation | 在三个 1B 级模型上系统追踪注意力电路发育轨迹，发现 induction 与 attention-sink 是独立过渡阶段 / Tracks attention circuit formation across three 1B-class models, finding induction and attention-sink are separable transitions |
| [[2606.02385]] SAE Dictionary Learning Theory | 将局部最优性分析扩展到非负联合优化问题，解释 SAE 特征分裂与吸收现象 / Extends local optimality analysis to nonnegative joint optimization, explaining SAE feature splitting and absorption |
| [[2606.02528]] Bitcoin SAE Audit | 首个连接 LLM 输出偏好、内部表征与下游金融决策的三层审计框架，通过 SAE 定位因果性比特币偏好特征 / First three-level audit linking LLM preferences, internal representations, and financial decisions via SAE steering |

### 持续学习与联邦学习 / Continual & Federated Learning

| 论文 / Paper | 一句话总结 / One-Line Summary |
|-------------|------------------------------|
| [[2606.02322]] AdvCL | 将对抗扰动重新定义为持续学习中的几何控制信号，三模块框架同时提升标准性能与对抗鲁棒性 / Repurposes adversarial perturbations as geometric control signals for continual learning |
| [[2606.02461]] AGENTCL | 首个针对语言智能体持续学习的严格评估框架，强调组合式任务流的关键作用 / First rigorous evaluation framework for continual learning in language agents |
| [[2606.02502]] CRAM | 语义分组路由 + 自适应秩实例化 + 质心引导正交学习的多模态持续指令微调框架 / Semantic group routing with adaptive-rank instantiation and centroid-guided orthogonal learning for MCIT |
| [[2606.02576]] ProtoAda | 格式感知任务原型与几何感知参数整合，缓解多模态持续学习中的格式混淆 / Format-aware task prototypes with geometry-aware consolidation for multimodal continual learning |
| [[2606.02172]] FedSAP | 基于语义感知原型的联邦学习方法，通过类别级原型聚合缓解数据异构性 / Federated semantic-aware prototype learning addressing data heterogeneity |
| [[2606.01717]] MERIT | 去中心化指令调优框架，无需中央服务器协调的多智能体协作学习 / Decentralized instruction tuning without central server coordination |

### 不确定性量化与鲁棒性 / Uncertainty Quantification & Robustness

| 论文 / Paper | 一句话总结 / One-Line Summary |
|-------------|------------------------------|
| [[2606.01850]] Conformal Quantized LLMs | 为量化后 LLM 提供具有有限样本覆盖保证的预测集 / Prediction sets with finite-sample coverage guarantees for post-quantization LLMs |
| [[2606.01973]] Open-Set TTA | 针对开放集分布偏移的测试时自适应方法，同时处理已知与未知类别 / Test-time adaptation for open-set distribution shifts handling both known and unknown classes |
| [[2606.02081]] Decision-Calibrated Sets | 决策校准的预测集，在保持覆盖保证的同时优化下游决策质量 / Decision-calibrated prediction sets optimizing downstream decision quality |
| [[2606.02093]] Ambiguity in UQ | 揭示基于不确定性量化的错误预测中固有的歧义性，提出歧义感知校准方法 / Reveals inherent ambiguity in UQ-based error prediction and proposes ambiguity-aware calibration |
| [[2606.02134]] IBP Certified Training | 对基于区间边界传播的训练后模型进行严格的能力评估与局限分析 / Rigorous evaluation of Interval Bound Propagation certified training capabilities and limitations |
| [[2606.02267]] Noise + Bilateral Filter | 噪声与双边滤波结合的图像鲁棒性增强方法，在对抗攻击下保持视觉质量 / Image robustness enhancement combining noise and bilateral filtering under adversarial attacks |
| [[2606.02430]] LLMFI | 首个针对 LLM 推理阶段的可配置确定性故障注入框架，提出四种软件级可靠性增强方案 / First configurable deterministic fault-injection framework for LLM inference stages |

### 多智能体系统与分布式优化 / Multi-Agent Systems & Distributed Optimization

| 论文 / Paper | 一句话总结 / One-Line Summary |
|-------------|------------------------------|
| [[2606.01680]] OptCC | 面向大规模分布式系统的通信压缩与收敛优化框架 / Communication compression and convergence optimization for large-scale distributed systems |
| [[2606.02282]] POIROT | 去中心化多智能体故障诊断协议，通过同伴质询与危险感知聚合实现准确故障归因 / Decentralized peer-interrogation protocol for LLM-MAS fault detection and attribution |
| [[2606.02218]] SAGC | 基于强化学习的掉队者感知组大小自适应方法，优化分布式训练效率 / Straggler-aware RL-based group sizing for distributed training efficiency |
| [[2606.02363]] POMG Policy Regret | 首次在部分可观测马尔可夫博弈中建立策略遗憾的极小极大最优理论界限 / First minimax-optimal policy regret bounds in partially observable Markov games |

### 量化与高效推理 / Quantization & Efficient Inference

| 论文 / Paper | 一句话总结 / One-Line Summary |
|-------------|------------------------------|
| [[2606.02011]] 2-Bit Reasoning | 2-bit 推理模型的高效推理方法，在极低比特下保持推理能力 / Efficient 2-bit inference for reasoning models preserving capability at extreme quantization |
| [[2606.02288]] INSERTQUANT | 跨模态通用无尖峰后训练量化框架，系统开销极低（延迟 +4.69%，内存 +0.007%）/ Cross-modal spike-free post-training quantization with minimal overhead |
| [[2606.01850]] Conformal Quantized LLMs | 为量化 LLM 提供有限样本统计保证的保形预测方法 / Conformal prediction for quantized LLMs with finite-sample guarantees |

### 因果推断与最优传输 / Causal Inference & Optimal Transport

| 论文 / Paper | 一句话总结 / One-Line Summary |
|-------------|------------------------------|
| [[2606.02047]] CDOT | 因果最优传输方法，用于观测数据中的因果效应估计 / Causal optimal transport for causal effect estimation from observational data |
| [[2606.02221]] CORE-MTL | 基于因果发现的多任务学习框架，显式建模任务间因果关系 / Causal multi-task learning framework explicitly modeling inter-task causal relationships |
| [[2606.02232]] Doeblin-Anchored Chart | 基于 Doeblin  minorization 条件的对比图表，用于马尔可夫链收敛性分析 / Doeblin-anchored contrastive chart for Markov chain convergence analysis |
| [[2606.02515]] OMT | 最优混合传输框架，将熵正则化 OT 提升到混合模型子群体映射，保证唯一全局解 / Optimal Mixture Transport lifting entropic OT to mixture-model subpopulation mapping with unique global solution |

### 推理、思维链与幻觉 / Reasoning, Chain-of-Thought & Hallucinations

| 论文 / Paper | 一句话总结 / One-Line Summary |
|-------------|------------------------------|
| [[2606.02020]] CoT Entropy Dynamics | 分析思维链生成过程中的熵动态，揭示推理阶段的随机性与确定性转换 / Analyzes entropy dynamics during chain-of-thought generation revealing stochastic-to-deterministic transitions |
| [[2606.02060]] Deep-Research Error Localization | 深度研究智能体中的错误定位方法，识别并归因多步推理中的错误步骤 / Error localization in deep-research agents identifying and attributing faulty reasoning steps |
| [[2606.02289]] DECK | 基于一致性与置信度的 LLM 幻觉四象限分类法（漂移/固化/臆造/纠结）/ 2×2 taxonomy of LLM hallucinations by consistency and confidence (Drift/Entrenched/Confabulation/Knotted) |

### 多领域强化学习 / Multi-Domain Reinforcement Learning

| 论文 / Paper | 一句话总结 / One-Line Summary |
|-------------|------------------------------|
| [[2606.02398]] Local Perturbation Theory | 揭示多领域 RL 中跨领域干扰的局部化二阶机制，提出低维冲突子空间与刷新恢复 / Localized second-order mechanism for cross-domain interference in multi-domain RL with conflict subspace and refresh recovery |

### 扩散与生成模型 / Diffusion & Generative Models

| 论文 / Paper | 一句话总结 / One-Line Summary |
|-------------|------------------------------|
| [[2606.02211]] RMCT | 速率匹配一致性训练，改进扩散模型训练的一致性与收敛速度 / Rate Matching Consistency Training improving diffusion model consistency and convergence |

### 科学机器学习与应用 / Scientific ML & Applications

| 论文 / Paper | 一句话总结 / One-Line Summary |
|-------------|------------------------------|
| [[2606.01557]] Everywhere Learning | 基于约束优化的无处不在学习框架，将资源约束显式纳入训练目标 / Constrained optimization framework for everywhere learning incorporating resource constraints |
| [[2606.02231]] FlowMSM | 基于流的马尔可夫切换模型，用于非平稳时间序列建模 / Flow-based Markov Switching Model for non-stationary time series |
| [[2606.02427]] Spectral Audit of ICON | 基于 Jacobian 的频谱审计框架，诊断上下文算子网络是否学到真实 PDE 算子 / Jacobian-based spectral audit diagnosing whether ICONs learn true PDE operator structure |
| [[2606.02493]] FRANZ | 从文化定位、泛化语言、拟人化和对话准则四维度审计 LLM 回应框架 / Multi-dimensional audit of LLM response framing across cultural and communicative dimensions |
| [[2606.02528]] Bitcoin SAE Audit | 金融 LLM 资产偏好的三层审计框架，以比特币为案例研究 / Three-level audit framework for asset-specific preferences in financial LLMs |

---

## All Papers

| # | 论文 ID / Paper ID | 标题 / Title | 核心标签 / Key Tags |
|---|-------------------|-------------|-------------------|
| 1 | [[2606.01521]] | GROKtimizer: Gradient Subspace Optimization | optimization, second-order |
| 2 | [[2606.01557]] | Everywhere Learning: Constrained Optimization | optimization, resource-constraints |
| 3 | [[2606.01680]] | OptCC: Distributed Communication Compression | distributed-systems, optimization |
| 4 | [[2606.01695]] | CANARY: Real-Time Jailbreak Detection | AI-safety, jailbreak-detection |
| 5 | [[2606.01717]] | MERIT: Decentralized Instruction Tuning | federated-learning, instruction-tuning |
| 6 | [[2606.01787]] | ASADPREC: Async Distributed Preconditioned CG | optimization, distributed |
| 7 | [[2606.01827]] | SAM + Polyak Step Size | optimization, generalization |
| 8 | [[2606.01850]] | Conformal Prediction for Quantized LLMs | quantization, uncertainty-quantification |
| 9 | [[2606.01973]] | Open-Set Test-Time Adaptation | robustness, test-time-adaptation |
| 10 | [[2606.02008]] | Meta-Learning Scaling Laws | meta-learning, theory |
| 11 | [[2606.02011]] | 2-Bit Reasoning Model Inference | quantization, efficient-inference |
| 12 | [[2606.02020]] | CoT Entropy Dynamics | reasoning, chain-of-thought |
| 13 | [[2606.02041]] | SentGuard: Streaming Safety Monitor | AI-safety, streaming |
| 14 | [[2606.02047]] | CDOT: Causal Optimal Transport | causal-inference, optimal-transport |
| 15 | [[2606.02060]] | Deep-Research Agent Error Localization | agents, error-localization |
| 16 | [[2606.02061]] | Archetypal SAE Stability Critique | mechanistic-interpretability, SAE |
| 17 | [[2606.02078]] | Dynamic lp-norm Optimizers | optimization, adaptive |
| 18 | [[2606.02081]] | Decision-Calibrated Prediction Sets | uncertainty-quantification, calibration |
| 19 | [[2606.02093]] | Ambiguity in UQ-Based Error Prediction | uncertainty-quantification, ambiguity |
| 20 | [[2606.02111]] | Multi-Clip Video Jailbreak | AI-safety, multimodal, jailbreak |
| 21 | [[2606.02119]] | HAMU: Hardness-Aware Machine Unlearning | AI-safety, unlearning |
| 22 | [[2606.02134]] | IBP Certified Training Evaluation | robustness, certified-training |
| 23 | [[2606.02158]] | Low-Probability Token AIGT Detection | AI-safety, detection, AIGT |
| 24 | [[2606.02172]] | FedSAP: Federated Semantic-Aware Prototypes | federated-learning, prototypes |
| 25 | [[2606.02211]] | RMCT: Rate Matching Consistency Training | diffusion, generative-models |
| 26 | [[2606.02218]] | SAGC: Straggler-Aware RL Group Sizing | distributed-training, RL |
| 27 | [[2606.02221]] | CORE-MTL: Causal Multi-Task Learning | multi-task, causal-inference |
| 28 | [[2606.02231]] | FlowMSM: Flow-Based Markov Switching Model | time-series, generative-models |
| 29 | [[2606.02232]] | Doeblin-Anchored Contrastive Chart | Markov-chains, theory |
| 30 | [[2606.02267]] | Noise + Bilateral Filter Robustness | robustness, adversarial, vision |
| 31 | [[2606.02282]] | POIROT: Multi-Agent Failure Detection | multi-agent, AI-safety, fault-detection |
| 32 | [[2606.02288]] | Massive Spikes are Bias Vectors / INSERTQUANT | quantization, interpretability, LLM |
| 33 | [[2606.02289]] | DECK: Consistency × Confidence Hallucination Taxonomy | hallucination, uncertainty, taxonomy |
| 34 | [[2606.02322]] | AdvCL: Adversarial Perturbations for Continual Learning | continual-learning, adversarial, LLM |
| 35 | [[2606.02363]] | Minimax-Optimal Policy Regret in POMGs | RL-theory, multi-agent, POMG |
| 36 | [[2606.02365]] | FOAM: Adaptive Damping for Shampoo | optimization, Shampoo, preconditioner |
| 37 | [[2606.02378]] | Attention Circuits Formation Trajectories | mechanistic-interpretability, training-dynamics |
| 38 | [[2606.02385]] | How Optimality Structures Sparse Dictionaries | SAE, dictionary-learning, theory |
| 39 | [[2606.02398]] | Local Perturbation Theory for Multi-Domain RL | multi-domain-RL, interference, LLM |
| 40 | [[2606.02423]] | HarmAmp / TrajSafe: Multi-Turn Harm Amplification | AI-safety, multi-turn, RL |
| 41 | [[2606.02427]] | Spectral Audit of In-Context Operator Networks | scientific-ML, neural-operators, PDE |
| 42 | [[2606.02430]] | LLMFI: Error Propagation in LLM Inference | reliability, fault-injection, LLM |
| 43 | [[2606.02461]] | AGENTCL: Continual Learning in Language Agents | agents, continual-learning, evaluation |
| 44 | [[2606.02493]] | FRANZ: Communicative Audit of LLM Response Framing | evaluation, cultural, communicative |
| 45 | [[2606.02502]] | CRAM: Centroid-Routing Adaptive MoE for MCIT | multimodal, continual-learning, MoE |
| 46 | [[2606.02515]] | OMT: Optimal Mixture Transport | optimal-transport, computational-biology |
| 47 | [[2606.02528]] | Auditing Asset-Specific Preferences in Financial LLMs | finance, SAE, mechanistic-interpretability |
| 48 | [[2606.02530]] | SafeSteer: Localized On-Policy Distillation for Safety | safety, alignment, distillation |
| 49 | [[2606.02562]] | BeliefSF / JIST: Neural Safety Filters for Robotics | robotics, safety-filters, conformal-prediction |
| 50 | [[2606.02576]] | ProtoAda: Prototype-Guided Adaptive Adapter Expansion | multimodal, continual-learning, adapter |
