---
title: "Daily Paper Overview — 2026-05-21"
date: 2026-05-21
tags:
  - daily-paper
  - arxiv
  papers: 50
---

## 今日必读 / Must Read Today

### 1. [[2605.22672]] Is Capability a Liability? More Capable LLMs Make Worse Forecasts When It Matters Most
> **推荐理由 / Reason:** 发现LLM在尾部风险预测中的逆向缩放现象——能力越强的模型在指数增长+制度突变时间序列的上尾预测越差，且标准评估指标（Brier）会掩盖这一失败。实验设计极为出色，包含因果机制隔离、信息性负对照和跨域复现。 / Reveals a counterintuitive inverse-scaling phenomenon where more capable LLMs produce worse distributional forecasts precisely when accuracy matters most (tail risk), and standard evaluation metrics systematically mask this failure. Exceptional experimental design with causal mechanism isolation, informative negative controls, and multi-domain replication.

### 2. [[2605.21958]] Diagnosis Is Not Prescription: Linguistic Co-Adaptation Explains Patching Hazards in LLM Pipelines
> **推荐理由 / Reason:** 揭示LLM Agent调试中的"诊断悖论"——因果分析定位的瓶颈反而是最差的修补目标。提出"语言契约"假设解释模块间共适应机制，对Agent可靠性工程具有直接指导意义。 / Uncovers the Diagnostic Paradox in multi-module LLM agent pipelines: the module identified as the bottleneck is the worst target for correction, because downstream modules have co-adapted to upstream error distributions (the "Linguistic Contract"). Directly challenges default debugging workflows.

### 3. [[2605.21851]] OPPO: Bayesian Value Recursion for Token-Level Credit Assignment in LLM Reasoning
> **推荐理由 / Reason:** 将oracle条件似然比识别为贝叶斯充分统计量，推导出闭式价值递归实现无需critic的token级信用分配，在7个基准上持续优于GRPO/DAPO，且优势随序列长度单调增长。 / Identifies the oracle log-likelihood ratio as simultaneously a distillation signal and Bayesian sufficient statistic, deriving a closed-form value recursion that achieves token-level credit assignment without a learned critic. Gains over GRPO/DAPO widen monotonically with response length.

---

## 按主题分类 / Papers by Topic

### LLM Training Optimization & Stability / LLM训练优化与稳定性

| Paper | 核心发现 / Core Finding |
|-------|----------------------|
| [[2605.21851]] OPPO: Bayesian Value Recursion | 闭式贝叶斯递归实现无需critic的token级信用分配，长序列优势更显著 / Closed-form Bayesian recursion for critic-free token-level credit assignment with widening gains on longer sequences |
| [[2605.22217]] Survive or Collapse: Self-Play RL | 数据门控比奖励设计更关键——移除门控后所有奖励变体均崩溃 / Data gating is the binding constraint on stability, not reward design — every reward variant collapses without the gate |
| [[2605.22620]] Collapse-free Multi-Reward RLIF | 多奖励+KL-Cov正则化解决无监督RL中的熵坍塌 / Multi-reward + KL-Cov regularization prevents entropy collapse in unsupervised RL for LLM reasoning |
| [[2605.22432]] AMUSE: Anytime Muon | 时变插值结合Muon与Schedule-Free，无需LR调度，720M LLM上1.51倍加速 / Time-varying interpolation combining Muon with Schedule-Free, 1.51x speedup on 720M LLM without LR scheduling |
| [[2605.22297]] Heavy-Tail Guided Layerwise LR | 谱分析揭示Transformer层间异质性，自适应层学习率带来1.5倍训练加速 / Spectral analysis reveals Transformer layer heterogeneity; adaptive layerwise LR yields 1.5x training speedup |
| [[2605.22703]] Clipping Bottleneck: NSR | 硬裁剪的二元决策是RLVR瓶颈，随机恢复近边界信号带来2-6%提升 / Hard clipping's binary decision is the RLVR bottleneck; stochastic near-boundary rescue yields 2-6% gains |
| [[2605.22731]] Post-Training is About States | 状态分布视角统一SFT/RL/蒸馏，在线蒸馏可从退化教师中恢复 / State-distribution view unifies post-training; on-policy distillation recovers from degraded teachers |
| [[2605.22579]] Hyperfitting as Geometric Expansion | 超拟合改善贪心解码的机制是末端层的几何维度展开，仅微调最后5层即可复现 / Hyperfitting improves greedy decoding via terminal-layer geometric expansion; last-5-layer LoRA suffices |
| [[2605.21968]] IAdaPID-ADG Optimizer | 融合AMSGrad和DiffGrad的PID优化器，训练损失降低2-3个数量级 / PID optimizer integrating AMSGrad and DiffGrad, reducing training loss by 2-3 orders of magnitude |
| [[2605.22644]] Why SGD is not Brownian Motion | 离散Fokker-Planck推导证明标准Langevin近似遗漏O(η²)项，SGD在临界点分解为受限/扩散两种模式 / Discrete Fokker-Planck derivation shows Langevin approximation omits O(η²) terms; SGD splits into confined/diffusive modes near critical points |
| [[2605.21933]] Thermodynamic Irreversibility of Training | 四种不可逆性度量等价，学习率产生打破时间反演对称的涌现力 / Four irreversibility measures are equivalent; learning rate creates an emergent symmetry-breaking force |

### Mechanistic Interpretability & Representation Analysis / 机制可解释性与表示分析

| Paper | 核心发现 / Core Finding |
|-------|----------------------|
| [[2605.21958]] Diagnosis Is Not Prescription | 诊断悖论：瓶颈模块是最差修补目标，语言契约解释共适应机制 / Diagnostic Paradox: the bottleneck is the worst patching target; Linguistic Contract explains co-adaptation |
| [[2605.22007]] Hallucination as Commitment Failure | 幻觉不是知识缺失而是"承诺失败"——概率分散随模型规模单调增加 / Hallucination is commitment failure, not knowledge absence — probability dispersion rises monotonically with scale |
| [[2605.21849]] GAE: Geometry-Adaptive Explainer | 分布偏移旋转激活子空间导致字典解释器失效，闭式Procrustes旋转3秒修复 / Distribution shift rotates activation subspaces; closed-form Procrustes rotation fixes explainer in <3s |
| [[2605.21980]] Emotional Circuits in LVLMs | 揭示LVLM中"适配-聚合-执行"三阶段情感处理及特异性/通用通路解耦 / Reveals 3-stage emotion processing in LVLMs with sentiment-specific/universal pathway decoupling |
| [[2605.22005]] Check Your LLM's Secret Dictionary | lm_head SVD五行代码揭示训练数据组成和有害词汇子空间，RLHF无法消除预训练有害子空间 / 5-line lm_head SVD reveals training data composition and harmful subspaces; RLHF fails to remove them |
| [[2605.22488]] Represented Is Not Computed | 可解码≠被因果使用：探针成功解码中间量但因果回路不通过它们 / Decodable ≠ causally used: probes decode intermediates but the causal circuit bypasses them |
| [[2605.22532]] Relational Linear Properties | KL-RP探针揭示时态和真实性在中间层具有强线性结构 / KL-RP probe reveals strong linear structure for tense and truthfulness in middle layers |
| [[2605.22170]] Factual Recall: Text to Speech | 文本模态事实召回机制完整迁移，语音模态因果效应大幅减弱 / Factual recall mechanisms transfer fully in text but are drastically weakened in speech |
| [[2605.22658]] SegCompass: SAE for Segmentation | SAE映射CoT和视觉特征到共享稀疏概念空间，实现可解释推理分割 / SAE maps CoT and visual features to shared sparse concept space for interpretable reasoning segmentation |
| [[2605.22679]] CEDAR: Sparse Disentanglement for VLMs | 正交变换在不扩展维度的情况下解耦VLM嵌入，用户研究验证优于MSAE / Orthogonal transformation disentangles VLM embeddings without dimensionality expansion; user studies confirm superiority over MSAE |
| [[2605.22462]] Five-Stage Causal Feature Analysis | SAE特征选择性与因果力负相关(r=-0.56)，检测鲁棒性≠因果鲁棒性 / SAE feature selectivity anticorrelates with causal force (r=-0.56); detection robustness ≠ causal robustness |
| [[2605.22719]] Reading Task Failure Off Activations | SAE最强失败相关特征是词汇混淆而非因果机制，SAE附加值在可解释性而非预测力 / Strongest SAE failure correlate is a lexical confound, not causal; SAE adds interpretability, not predictive power |
| [[2605.22377]] Token Level Activation in SLMs | BERT Layer 8隐藏状态L2范数量化token重要性，语义内容词占主导 / L2 norms of BERT Layer-8 hidden states quantify token importance; semantic content words dominate |

### LLM Agents & Reasoning Systems / LLM智能体与推理系统

| Paper | 核心发现 / Core Finding |
|-------|----------------------|
| [[2605.22102]] ExComm: Exploration-Stage Communication | 探索阶段通信检测跨智能体事实冲突，软信念更新保持轨迹多样性 / Exploration-stage communication detects cross-agent factual conflicts with soft belief updates preserving diversity |
| [[2605.22166]] Life-Harness: Runtime Adaptation | 运行时接口适配不修改模型权重，88.5%平均提升且跨17个模型迁移 / Runtime interface adaptation without weight modification; 88.5% avg improvement with cross-model transfer to 17 backbones |
| [[2605.22781]] DeltaBox: Millisecond Sandbox C/R | OS级增量检查点/回滚14ms/5ms，MCTS状态管理开销从47-77%降至3-6% / OS-level delta checkpoint/rollback at 14ms/5ms; MCTS state overhead drops from 47-77% to 3-6% |

### Evaluation Reliability & Benchmarking / 评估可靠性与基准测试

| Paper | 核心发现 / Core Finding |
|-------|----------------------|
| [[2605.21856]] Illusion of Reasoning: Data Contamination | CoT推理主动掩盖记忆，Zero-CoT Probe检测隐蔽数据污染 / CoT reasoning actively masks memorization; Zero-CoT Probe detects evasive data contamination |
| [[2605.22672]] Is Capability a Liability? | 能力越强的模型在尾部风险预测中越差，标准指标掩盖失败 / More capable models are worse at tail-risk forecasting; standard metrics mask the failure |
| [[2605.22544]] Instruction Sensitivity in Embeddings | 单提示词评估系统性歪曲模型排名，对抗性提示词选择可使任意模型登顶 / Single-prompt evaluation systematically misrepresents rankings; adversarial prompt selection makes any model rank first |
| [[2605.22714]] AMEL: Accumulated Message Effects | 对话历史偏置LLM判断(d=-0.17)，负面历史影响比正面强62%，5轮即饱和 / Conversation history biases LLM judgments (d=-0.17); negativity asymmetry 1.62x; saturates after 5 turns |

### Model Architecture & Expressivity / 模型架构与表达能力

| Paper | 核心发现 / Core Finding |
|-------|----------------------|
| [[2605.22223]] Transformer Output Accessibility | 严格证明Transformer可输出序列数量有限，可访问序列长度随prompt线性增长 / Proves finite accessible sequences for transformers; max length scales linearly with prompt length |
| [[2605.22791]] Gated DeltaNet-2 | 擦除/写入门解耦提升线性注意力，MK-NIAH多键检索优势显著 / Decoupled erase/write gates improve linear attention; strong gains on MK-NIAH multi-key retrieval |

### Robustness & Safety / 鲁棒性与安全性

| Paper | 核心发现 / Core Finding |
|-------|----------------------|
| [[2605.22496]] SITN: OOD Detection via GoF Testing | 噪声空间拟合优度检测OOD，无需OOD数据且可控制假阳性率 / Goodness-of-fit testing in noise space for OOD detection; no OOD data needed with controlled FPR |
| [[2605.21999]] Why Robust Teachers Fail | 鲁棒不可学习样本集上的教师置信度失配导致学生过拟合 / Teacher confidence mismatch on robustly unlearnable samples drives student overfitting |
| [[2605.22800]] The Matching Principle | 统一鲁棒性/域适应/对抗训练为编码器Jacobian的几何正则化 / Unifies robustness/domain adaptation/adversarial training as geometric regularization of encoder Jacobian |
| [[2605.22472]] WTA Bottlenecks for Disentanglement | 理论证明WTA瓶颈在多任务学习中精确恢复分类潜变量 / Proves WTA bottlenecks exactly recover categorical latents under multi-task learning |
| [[2605.22593]] Deep Ensembles for GNN Uncertainty | GNN深度集成存在"认知坍塌"——独立训练模型收敛到近乎相同的预测 / GNN deep ensembles suffer epistemic collapse — independently trained models converge to nearly identical predictions |
| [[2605.22493]] Multimodal Failure in Action-Chunking | Fano不等式和Lipschitz分析揭示行为克隆中多模态策略失效的信息论机制 / Fano inequality and Lipschitz analysis reveal information-theoretic mechanism of multimodal failure in BC |
| [[2605.22446]] Pre-VLA: Runtime Verification | PPO Critic构建安全信号在动作执行前拦截低质量VLA动作 / PPO Critic-based safety signal intercepts low-quality VLA actions before execution |
| [[2605.22441]] Constant-Time Activation Functions | 无分支+Padé逼近实现ARM Cortex-M4上所有激活函数相同时钟周期 / Branchless + Padé approximation makes all activation functions execute in identical cycles on ARM Cortex-M4 |
| [[2605.22437]] Intel NCS2 EMFI Fault Response | 电磁故障注入可破坏空闲设备上已加载模型权重，架构依赖的鲁棒性差异 / EM fault injection corrupts pre-loaded model weights on idle devices; architecture-dependent robustness differences |

### Generative Models & Theoretical Foundations / 生成模型与理论基础

| Paper | 核心发现 / Core Finding |
|-------|----------------------|
| [[2605.22723]] Lanczos Sampler for DDPM | 匹配完整后验协方差将路径KL从Ω(1/T)降至O(1/T²)，3次JVP即可实现 / Full covariance matching reduces path KL from Ω(1/T) to O(1/T²); 3 JVPs suffice |
| [[2605.22795]] Finite-Particle Convergence for Drifting | 保守型drifting方法的有限粒子收敛速率N^{-1/(d+4)}，Laplace核的不可约尺度失配残差 / Conservative drifting achieves N^{-1/(d+4)} convergence; irreducible scale-mismatch residual for Laplace kernel |
| [[2605.22691]] Posterior Collapse as Spectral Pruning | β-VAE后验坍缩是自动谱剪枝机制，坍缩谱/效用谱/PCA谱三者一致 / β-VAE posterior collapse is automatic spectral pruning; collapse/utility/PCA spectra coincide |
| [[2605.22223]] Transformer Output Accessibility | （见模型架构分类 / See Model Architecture section） |

### Applied ML Systems / 应用ML系统

| Paper | 核心发现 / Core Finding |
|-------|----------------------|
| [[2605.22098]] TextTeacher: Text-Guided Vision | 文本语义锚点引导视觉模型训练，推理时无需文本组件，提升最高+2.7pp / Text semantic anchors guide vision training with no inference overhead; up to +2.7pp on ImageNet |
| [[2605.22769]] Data Temporality in Pre-training | 时序预训练的6B模型在近期事实上超越更大的打乱训练模型 / Chronologically pre-trained 6B model beats larger shuffled models on recent facts |
| [[2605.21969]] LLM Retrieval for Ad Recommendations | 微调LLaMA-8B语义候选生成，A/B实验中可预测性降低8.62%同时性能提升0.45% / Fine-tuned LLaMA-8B semantic retrieval reduces prediction instability 8.62% while lifting performance 0.45% |
| [[2605.22779]] FAME: Log Anomaly Detection | 失败感知MoE实现消息级日志异常检测，标注量减少76倍 / Failure-aware MoE for message-level log anomaly detection with 76x annotation reduction |
| [[2605.22401]] Cross-Species RSA | 早期视觉皮层对齐跨物种一致，局部学习规则优于反向传播 / Early visual alignment is conserved across species; local learning rules outperform backpropagation |

---

## All Papers

| # | arXiv ID | Title (Short) |
|---|----------|---------------|
| 1 | [[2605.21849]] | GAE: Geometry-Adaptive Explainer for Dictionary-Based Interpretability |
| 2 | [[2605.21851]] | OPPO: Bayesian Value Recursion for Token-Level Credit Assignment |
| 3 | [[2605.21856]] | The Illusion of Reasoning: Evasive Data Contamination in LLMs |
| 4 | [[2605.21933]] | Thermodynamic Irreversibility of Training Algorithms |
| 5 | [[2605.21958]] | Diagnosis Is Not Prescription: Linguistic Co-Adaptation in LLM Pipelines |
| 6 | [[2605.21968]] | IAdaPID-ADG: Improved Adaptive PID Optimizer |
| 7 | [[2605.21969]] | LLM Retrieval for Stable Ad Recommendations |
| 8 | [[2605.21980]] | Interpreting Emotional Circuits in LVLMs via Cross-Modal Information Flow |
| 9 | [[2605.21999]] | Toward Understanding Adversarial Distillation: Why Robust Teachers Fail |
| 10 | [[2605.22005]] | Check Your LLM's Secret Dictionary! |
| 11 | [[2605.22007]] | Hallucination as Commitment Failure |
| 12 | [[2605.22098]] | TextTeacher: What Can Language Teach About Images? |
| 13 | [[2605.22102]] | ExComm: Exploration-Stage Communication for Agentic Test-Time Scaling |
| 14 | [[2605.22166]] | Life-Harness: Runtime Harness Adaptation for Deterministic LLM Agents |
| 15 | [[2605.22170]] | Do Factual Recall Mechanisms Carry over from Text to Speech? |
| 16 | [[2605.22217]] | Survive or Collapse: Data Gating vs Reward in Self-Play RL |
| 17 | [[2605.22223]] | How Many Different Outputs Can a Transformer Generate? |
| 18 | [[2605.22297]] | One LR Doesn't Fit All: Heavy-Tail Guided Layerwise Learning Rates |
| 19 | [[2605.22377]] | Towards Explainability of SLMs by Token Level Activation |
| 20 | [[2605.22401]] | Cross-Species RSA Reveals Conserved Early Visual Alignment |
| 21 | [[2605.22432]] | AMUSE: Anytime Muon with Stable Gradient Evaluation |
| 22 | [[2605.22437]] | Intel NCS2 EMFI Fault Response Characterization |
| 23 | [[2605.22441]] | Constant-Time Activation Functions on Microcontrollers |
| 24 | [[2605.22446]] | Pre-VLA: Preemptive Runtime Verification for VLA Models |
| 25 | [[2605.22462]] | From Correlation to Cause: Five-Stage Feature Analysis |
| 26 | [[2605.22472]] | Winner-Take-All Bottlenecks for Disentangled Representations |
| 27 | [[2605.22488]] | Represented Is Not Computed: A Causal Test in Transformers |
| 28 | [[2605.22493]] | Understanding Multimodal Failure in Action-Chunking Behavioral Cloning |
| 29 | [[2605.22496]] | SITN: OOD Detection Through Goodness-of-Fit Testing |
| 30 | [[2605.22532]] | Relational Linear Properties in Language Models |
| 31 | [[2605.22544]] | One Prompt Is Not Enough: Instruction Sensitivity in Embedding Models |
| 32 | [[2605.22579]] | Beyond Temperature: Hyperfitting as Late-Stage Geometric Expansion |
| 33 | [[2605.22593]] | Do Deep Ensembles Capture Uncertainty in GNNs? |
| 34 | [[2605.22620]] | Collapse-free Multi-Reward RLIF Training Framework |
| 35 | [[2605.22644]] | Why SGD Is Not Brownian Motion |
| 36 | [[2605.22658]] | SegCompass: SAE for Interpretable Reasoning Segmentation |
| 37 | [[2605.22672]] | Is Capability a Liability? Inverse Scaling in LLM Forecasting |
| 38 | [[2605.22679]] | CEDAR: Conceptualizing Embeddings via Sparse Disentanglement |
| 39 | [[2605.22691]] | Posterior Collapse as Automatic Spectral Pruning |
| 40 | [[2605.22703]] | Clipping Bottleneck: Stabilizing RLVR via Stochastic Recovery |
| 41 | [[2605.22714]] | AMEL: Accumulated Message Effects on LLM Judgments |
| 42 | [[2605.22719]] | Reading Task Failure Off the Activations: SAE Audit of IOI |
| 43 | [[2605.22723]] | The Value of Covariance Matching in Gaussian DDPMs |
| 44 | [[2605.22731]] | Post-Training Is About States, Not Tokens |
| 45 | [[2605.22769]] | Understanding Data Temporality Impact on LLM Pre-training |
| 46 | [[2605.22779]] | FAME: Failure-Aware MoE for Log Anomaly Detection |
| 47 | [[2605.22781]] | DeltaBox: Millisecond-Level Sandbox Checkpoint/Rollback |
| 48 | [[2605.22791]] | Gated DeltaNet-2: Decoupling Erase and Write in Linear Attention |
| 49 | [[2605.22795]] | Finite-Particle Convergence Rates for Drifting Models |
| 50 | [[2605.22800]] | The Matching Principle: A Geometric Theory of Loss Functions |
