---
title: "Daily arXiv Overview — 2026-05-29"
date: 2026-05-29
tags:
  - llm-optimization
  - mechanistic-interpretability
  - reinforcement-learning
  - llm-safety
  - model-compression
  - vision-language-models
  - distributed-systems
  - bayesian-methods
  - neural-network-theory
papers: 50
---

## 今日必读 / Must Read Today

### 1. [[2605.29358]] Scaling Monosemanticity: Extracting Interpretable Features from Claude 3 Sonnet

**推荐理由 / Why read:** Anthropic 将稀疏自编码器扩展至 3400 万特征，在 Claude 3 Sonnet 上提取出跨语言、跨模态的可解释特征（代码语义追踪、安全相关概念），是机械可解释性领域的里程碑工作。
Anthropic scales sparse autoencoders to 34M features on Claude 3 Sonnet, extracting multilingual, multimodal interpretable features (code semantics, safety concepts) -- a landmark in mechanistic interpretability.

### 2. [[2605.29548]] Why Larger Models Learn More: Effects of Capacity, Interference, and Rare-Task Retention

**推荐理由 / Why read:** 从梯度干扰和资源竞争角度提供了模型缩放优势的机理化解释，证明大模型能学到小模型学不到的稀有任务，对理解能力涌现有重要启示。
Provides a mechanistic explanation for model scaling advantages via gradient interference analysis, proving larger models learn rare tasks smaller models cannot -- key insights on emergence.

### 3. [[2605.29343]] Draft-OPD: On-Policy Distillation for Speculative Draft Models

**推荐理由 / Why read:** 识别了投机解码中草稿模型 SFT 训练的"训练-推理不匹配"瓶颈，提出的错误位置回放在线蒸馏框架在 Qwen3 思维模型上实现 5x+ 无损加速。
Identifies the training-inference mismatch bottleneck in speculative decoding draft models; the error-position replay framework achieves 5x+ lossless speedup on Qwen3 thinking models.

---

## 按主题分类 / Papers by Topic

### LLM 推理加速与量化 / LLM Inference Acceleration & Quantization

| Paper | 简述 / Summary |
|-------|---------------|
| [[2605.29343]] Draft-OPD | 针对投机解码草稿模型的在线策略蒸馏 / On-policy distillation for speculative decoding draft models |
| [[2605.29350]] ConMoE | 免训练的 MoE 专家池压缩 / Train-free MoE expert-pool consolidation via prototype reassignment |
| [[2605.29535]] AsymVLM | 视觉语言模型的非对称 token 剪枝 / Asymmetric token pruning for efficient VLM inference |
| [[2605.29756]] LFQ | 基于交叉熵的最终块量化提升生成质量 / Logit-aware final-block quantization for low-bit LLMs |
| [[2605.29843]] HARP | 可学习的蝶形正交旋转处理器用于极低比特量化 / Learnable butterfly rotation for extreme LLM quantization |
| [[2605.30218]] MarginGate | 稀疏 margin 触发的批量不变确定性解码 / Sparse margin-triggered verification for deterministic LLM inference |

### 机械可解释性 / Mechanistic Interpretability

| Paper | 简述 / Summary |
|-------|---------------|
| [[2605.29358]] Scaling Monosemanticity | 34M 特征 SAE 在 Claude 3 Sonnet 上的可解释特征提取 / 34M-feature SAE on Claude 3 Sonnet |
| [[2605.29634]] Relational Rank Geometry | Plucker 符号熵检测 LLM 隐藏状态中的关系帧 / Plucker sign entropy for detecting relation frames in LLM hidden states |
| [[2605.29901]] Circuit-Level Analysis | LLM 漏洞检测的电路级分析 / Circuit-level analysis of LLM vulnerability detection |
| [[2605.30076]] UniSteer | 基于条件流匹配的统一 LLM 激活空间干预 / Unified text-guided flow matching for LLM activation steering |
| [[2605.30022]] Give it Space! | Transformer 编码器中位置与语义信息的显式解耦 / Explicit disentangling of positional and semantic representations |
| [[2605.30117]] VLA-Trace | 视觉-语言-动作模型的表示与行为追踪诊断 / Representation and behavior tracing for VLA models |
| [[2605.30232]] How's it going? | RL 训练激活语言模型中的功能性福祉轴 / RL recruits a functional welfare axis in language models |

### 强化学习与后训练 / Reinforcement Learning & Post-Training

| Paper | 简述 / Summary |
|-------|---------------|
| [[2605.29782]] Hista and Numca | 改进 LLM RL 中状态价值估计的两种方法 / Two methods for better state value estimation in LLM RL |
| [[2605.29860]] ESPO | 利用代理遗憾值进行早期停止的 PPO / Early-stopping PPO via surrogate regret for math reasoning |
| [[2605.30201]] HPO | 迟滞策略优化解决 GRPO 稀疏奖励问题 / Hysteretic policy optimization for sparse-reward LLM training |
| [[2605.29496]] Asymmetric Optimization | VLM 后训练中推理与感知的不对称优化 / Asymmetric optimization of reasoning and perception in VLM post-training |

### LLM 安全与鲁棒性 / LLM Safety & Robustness

| Paper | 简述 / Summary |
|-------|---------------|
| [[2605.29396]] Aligned but Fragile | 零阶优化增强 LLM 安全对齐鲁棒性 / Zeroth-order optimization for robust LLM safety alignment |
| [[2605.29524]] KBF | 知识边界指纹识别黑盒 LLM API 审计 / Knowledge boundary fingerprinting for black-box LLM API auditing |
| [[2605.29708]] RASET | MoE LLM 安全关键专家定位与红队攻击 / Router-agnostic safety-critical expert tuning for MoE red-teaming |
| [[2605.29816]] Harnessing Non-Adversarial Robustness | LLM 提示扰动的去偏与鲁棒性认证 / Debiasing and robustness certification for LLM prompt perturbations |
| [[2605.29979]] Fingerprinting Inference Systems | 基于数值偏差的 LLM 推理系统指纹识别 / Numerical-deviation fingerprinting of LLM inference systems |
| [[2605.30189]] Token-Level Backdoors | LoRA 适配器中 token 级后门攻击的刻画与检测 / Token-level backdoor attack characterization and detection in LoRA |

### 模型评估与基准 / Model Evaluation & Benchmarks

| Paper | 简述 / Summary |
|-------|---------------|
| [[2605.29800]] Nine Judges, Two Effective Votes | LLM 评委面板中相关错误导致有效投票量仅为名义的约 25% / Correlated errors reduce 9 LLM judges to ~2 effective votes |
| [[2605.29360]] MiraBench | 机器人世界模型的动作条件可靠性基准 / Action-conditioned reliability benchmark for robotic world models |
| [[2605.30085]] CROP | 推理链前缀的保形认证 / Conformal certification of reasoning trace prefixes |
| [[2605.30104]] SEAL | 通过元评委恢复饱和基准排名信号 / Reviving saturated benchmarks via LLM-as-meta-judge |
| [[2605.30315]] Resolution Diagnostics | 配对 LLM 评估的统计分辨率诊断 / Statistical resolution diagnostics for paired LLM evaluation |

### 微调与持续学习 / Fine-Tuning & Continual Learning

| Paper | 简述 / Summary |
|-------|---------------|
| [[2605.29495]] On-Policy Replay | 在线策略回放缓解 LLM 持续微调中的灾难性遗忘 / On-policy replay mitigates catastrophic forgetting in continual LLM SFT |
| [[2605.29498]] Mask the Target | 屏蔽目标 token 的 KL 正则化缓解 LoRA 遗忘 / Target-masked KL regularization against LoRA forgetting |
| [[2605.29716]] NaRA | 噪声感知 LoRA 适配扩散语言模型 / Noise-aware LoRA for diffusion language model fine-tuning |
| [[2605.29580]] LoRA-Curve | LoRA 空间中的 Bezier 曲线模式连通 / Bezier curve mode connectivity in LoRA weight space |
| [[2605.29380]] TRACER | WMA 教师解决 EMA 坍塌的多模态对比微调 / WMA teacher fixes EMA collapse in multimodal contrastive finetuning |

### 优化理论与缩放律 / Optimization Theory & Scaling Laws

| Paper | 简述 / Summary |
|-------|---------------|
| [[2605.29387]] Optimizer Dependence | 优化器选择改变神经缩放律指数 / Optimizer choice changes neural scaling law exponents |
| [[2605.29547]] S-Adam | 基于局部几何不稳定性的非光滑优化器 / Singularity-aware Adam for non-smooth optimization |
| [[2605.29494]] Gradient Perturbation | 统一的梯度扰动框架与类别感知训练 / Unified gradient perturbation framework with category-aware training |
| [[2605.29440]] SkillBrew | LLM Agent 技能库的多目标帕累托策展 / Multi-objective Pareto curation of LLM agent skill banks |

### 神经网络理论与复杂度 / Neural Network Theory & Complexity

| Paper | 简述 / Summary |
|-------|---------------|
| [[2605.29351]] Attention as Empirical Bayes | 注意力机制的两阶段经验贝叶斯解释 / Two-stage empirical Bayes view of attention mechanism |
| [[2605.29537]] Complexity of Verifying FNNs | 量化前馈神经网络验证的完整复杂度图谱 / Complete complexity landscape for quantised FNN verification |
| [[2605.30155]] PMNR | 部分多神经元松弛提升 DNN 验证 / Partial multi-neuron relaxation improves DNN verification |
| [[2605.29684]] Kernel Renormalization | 等价 Wishart 假设下贝叶斯深度网络的核重正化 / Kernel renormalization in Bayesian DNNs via equivalent Wishart ansatz |
| [[2605.29448]] Dataset Worth Scaling Laws | 矩阵谱函数统一 Vendi Score 与数据选择 / Matrix spectral functions unify Vendi Score and data selection |
| [[2605.29664]] AMDP | 异步多方向流水线并行训练 / Asynchronous multi-directional pipeline parallelism |

### 分布式训练与 AI 治理 / Distributed Training & AI Governance

| Paper | 简述 / Summary |
|-------|---------------|
| [[2605.29359]] Distributed Training Governance | 分布式训练可突破所有现行算力治理阈值 / Distributed training evades all compute governance thresholds |
| [[2605.30334]] Data Organization for LLM Training | 数据排序策略对 LLM 训练效率的系统性研究 / Systematic study of data ordering strategies for LLM training |

### 科学计算与具身智能 / Scientific Computing & Embodied AI

| Paper | 简述 / Summary |
|-------|---------------|
| [[2605.29467]] Composing Factor Graphs | 闭式变分推断的因子图组合框架 / Closed-form variational inference via factor graph composition |
| [[2605.30112]] Striding Across Reynolds Numbers | 神经 PDE 求解器跨雷诺数泛化的表征几何分析 / Representation geometry in cross-regime neural PDE generalization |
| [[2605.30184]] AI Weather Models | 九个 AI 天气模型的两年长期预测基准 / Two-year rollout benchmark of nine AI weather models |

### 数据污染与可解释性 / Data Contamination & Explainability

| Paper | 简述 / Summary |
|-------|---------------|
| [[2605.29888]] LaRA | 层级表示几何分析检测 RL 后训练数据污染 / Layer-wise representation geometry for detecting RL data contamination |

---

## All Papers

| # | ID | Title | 一句话描述 / One-line Description |
|---|-----|-------|---------------------------------|
| 1 | [[2605.29343]] | Draft-OPD | 在线策略蒸馏框架解决投机解码草稿模型训练瓶颈 / On-policy distillation solves draft model training bottleneck in speculative decoding |
| 2 | [[2605.29350]] | ConMoE | 免训练 MoE 专家池压缩通过确定性重映射 / Train-free MoE compression via deterministic prototype reassignment |
| 3 | [[2605.29351]] | Attention as Empirical Bayes | 注意力机制的两阶段经验贝叶斯去噪解释 / Two-stage empirical Bayes interpretation of attention denoising |
| 4 | [[2605.29358]] | Scaling Monosemanticity | 34M 特征 SAE 在 Claude 3 Sonnet 上的可解释性扩展 / 34M-feature SAE scaling on Claude 3 Sonnet |
| 5 | [[2605.29359]] | Distributed Training Governance | 分布式训练模拟器揭示算力治理漏洞 / Distributed training simulator reveals compute governance loopholes |
| 6 | [[2605.29360]] | MiraBench | 机器人世界模型动作条件可靠性分层基准 / Hierarchical benchmark for robotic world model reliability |
| 7 | [[2605.29380]] | TRACER | WMA 教师替代 EMA 解决对比微调中的坍塌 / WMA teacher replaces EMA to fix collapse in contrastive finetuning |
| 8 | [[2605.29387]] | Optimizer Dependence | 优化器选择系统性地改变缩放律指数 / Optimizer choice systematically changes scaling law exponents |
| 9 | [[2605.29396]] | Aligned but Fragile | 零阶优化精修增强 LLM 安全对齐鲁棒性 / ZO refinement enhances LLM safety alignment robustness |
| 10 | [[2605.29440]] | SkillBrew | LLM Agent 技能库的多目标帕累托策展 / Multi-objective Pareto curation of LLM agent skill banks |
| 11 | [[2605.29448]] | Dataset Worth Scaling Laws | 矩阵谱函数统一数据评估目标与 secular equation 加速 / Matrix spectral functions unify data appraisal with secular equation speedup |
| 12 | [[2605.29467]] | Composing Factor Graphs | 五种因子图基元实现闭式变分推断 / Five factor-graph primitives enable closed-form variational inference |
| 13 | [[2605.29494]] | Gradient Perturbation | 统一梯度扰动框架与类别感知训练 LPG / Unified gradient perturbation with category-aware LPG training |
| 14 | [[2605.29495]] | On-Policy Replay | 在线策略回放将持续 SFT 遗忘降低 42-46% / On-policy replay cuts continual SFT forgetting by 42-46% |
| 15 | [[2605.29496]] | Asymmetric Optimization | VLM 后训练中推理与感知的不对称优化诊断 / Diagnosing asymmetric optimization of reasoning vs. perception in VLM post-training |
| 16 | [[2605.29498]] | Mask the Target | 屏蔽目标 token 的 KL 正则化即插即用缓解 LoRA 遗忘 / Plug-and-play target-masked KL regularization against LoRA forgetting |
| 17 | [[2605.29524]] | KBF | 知识边界指纹实现低成本 LLM API 黑盒审计 / Knowledge boundary fingerprinting for low-cost black-box LLM API auditing |
| 18 | [[2605.29535]] | AsymVLM | 非对称 token 剪枝节省 VLM 54% FLOPs / Asymmetric token pruning saves 54% FLOPs for VLMs |
| 19 | [[2605.29537]] | Complexity of Verifying FNNs | 量化神经网络验证的完整计算复杂度图谱 / Complete computational complexity landscape for quantised NN verification |
| 20 | [[2605.29547]] | S-Adam | 局部几何不稳定性感知的自适应优化器 / Local geometric instability-aware adaptive optimizer for non-smooth training |
| 21 | [[2605.29548]] | Why Larger Models Learn More | 梯度干扰与临界宽度解释模型缩放优势 / Gradient interference and critical width explain model scaling advantages |
| 22 | [[2605.29580]] | LoRA-Curve | Bezier 曲线在 LoRA 空间构建连续低损失谷 / Bezier curves build continuous low-loss valleys in LoRA space |
| 23 | [[2605.29634]] | Relational Rank Geometry | Plucker 符号熵探测 LLM 关系帧的秩索引方向签名 / Plucker sign entropy detects rank-indexed orientation signatures of relation frames |
| 24 | [[2605.29664]] | AMDP | 异步多方向流水线并行提升吞吐 17% / Asynchronous multi-directional pipeline parallelism improves throughput 17% |
| 25 | [[2605.29684]] | Kernel Renormalization | 等价 Wishart 假设预测有限宽度贝叶斯深度网络 / Equivalent Wishart ansatz predicts finite-width Bayesian deep networks |
| 26 | [[2605.29708]] | RASET | MoE 安全关键专家定位实现 50.5% 高质量红队攻击 / Safety-critical expert targeting achieves 50.5% quality attack rate on MoE |
| 27 | [[2605.29716]] | NaRA | 噪声感知 LoRA 通过超网络动态适配扩散 LLM / Noise-aware LoRA with hypernetwork adapts diffusion LLMs along denoising trajectory |
| 28 | [[2605.29756]] | LFQ | 交叉熵 logit 对齐提升低比特量化 LLM 生成质量 / Cross-entropy logit alignment improves low-bit quantized LLM generation |
| 29 | [[2605.29782]] | Hista and Numca | 改进 LLM RL 中 PPO critic 的状态价值估计 / Improving PPO critic state value estimation in LLM RL |
| 30 | [[2605.29800]] | Nine Judges | 9 个 LLM 评委仅提供约 2 个有效独立投票 / 9 LLM judges provide only ~2 effective independent votes |
| 31 | [[2605.29816]] | Non-Adversarial Robustness | 提示扰动的去偏与可证明鲁棒性认证 / Debiasing and certifiable robustness for LLM prompt perturbations |
| 32 | [[2605.29843]] | HARP | 蝶形正交旋转处理器优化极低比特 PTQ / Butterfly rotation processor optimizes extreme low-bit PTQ |
| 33 | [[2605.29860]] | ESPO | 早期停止 PPO 利用代理遗憾值节省 22% rollout token / Early-stopping PPO saves 22% rollout tokens via surrogate regret |
| 34 | [[2605.29888]] | LaRA | 层级表示几何检测 RL 后训练数据污染 / Layer-wise representation geometry detects RL post-training data contamination |
| 35 | [[2605.29901]] | Circuit-Level Analysis | LLM 漏洞检测的电路级机制分析 / Circuit-level mechanistic analysis of LLM vulnerability detection |
| 36 | [[2605.29979]] | Fingerprinting Inference | 数值偏差指纹识别 LLM 推理系统组件 / Numerical deviation fingerprinting identifies LLM inference stack components |
| 37 | [[2605.30022]] | Give it Space! | Transformer 编码器中位置与语义信息流的显式解耦 / Explicit disentangling of positional and semantic streams in encoder |
| 38 | [[2605.30076]] | UniSteer | 条件流匹配实现统一的文本引导 LLM 激活空间控制 / Conditional flow matching for unified text-guided LLM activation steering |
| 39 | [[2605.30085]] | CROP | 保形风险控制认证推理链前缀的正确性 / Conformal risk control certifies reasoning trace prefix correctness |
| 40 | [[2605.30104]] | SEAL | 种子淘汰赛与元评委恢复饱和基准排名信号 / Seeded elimination with meta-judge revives saturated benchmark signals |
| 41 | [[2605.30112]] | Striding Reynolds | 表征几何决定神经 PDE 求解器跨雷诺数泛化 / Representation geometry governs neural PDE cross-regime generalization |
| 42 | [[2605.30117]] | VLA-Trace | 渐进式诊断框架揭示 VLA 模型模态适应差异 / Progressive diagnostic framework reveals VLA model modality adaptation differences |
| 43 | [[2605.30155]] | PMNR | 部分多神经元松弛比基线多解决 49% 验证查询 / Partial multi-neuron relaxation solves 49% more verification queries |
| 44 | [[2605.30184]] | AI Weather Models | 九个 AI 天气模型两年滚动预测的失败模式分类 / Failure mode taxonomy from 2-year rollouts of nine AI weather models |
| 45 | [[2605.30189]] | Token-Level Backdoors | LoRA 后门在 token 特征级泛化的刻画与检测 / Characterization and detection of token-level generalizing LoRA backdoors |
| 46 | [[2605.30201]] | HPO | 迟滞策略优化解决 GRPO 稀疏奖励下的训练不稳定 / Hysteretic policy optimization fixes GRPO instability under sparse rewards |
| 47 | [[2605.30218]] | MarginGate | 稀疏 margin 触发验证实现确定性 LLM 解码 / Sparse margin-triggered verification achieves deterministic LLM decoding |
| 48 | [[2605.30232]] | Functional Welfare Axis | RL 训练激活语言模型中的预存功能性福祉轴 / RL training recruits a preexisting functional welfare axis in LMs |
| 49 | [[2605.30315]] | Resolution Diagnostics | 配对 LLM 评估中非配对捷径低估所需样本约一半 / Unpaired shortcut underestimates required sample size by ~2x in paired LLM eval |
| 50 | [[2605.30334]] | Data Organization | 数据排序四原则提升 LLM 预训练和 SFT 效率 / Four data ordering principles improve LLM pretraining and SFT efficiency |
