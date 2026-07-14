---
title: "Weekly arXiv Digest — 2026-05-25–2026-05-31"
week: "2026-0525-0531"
date_range: ["2026-05-25", "2026-05-30"]
tags:
  - hidden-states-interpretability
  - mechanistic-interpretability
  - optimizers-training-dynamics
  - quantization-efficient-inference
  - rl-post-training
  - llm-safety-alignment
  - ml-reliability-foundations
papers: 271
---

# Weekly arXiv Digest — 2026-05-25–2026-05-31

本周共收录 271 篇去重论文，覆盖 2026-05-25 至 2026-05-30 六天。主线集中在**隐藏状态与机制可解释性**、**优化器与训练动力学**、**量化与高效推理**、**强化学习后训练**与**LLM 安全/对齐**五条脉络。
This week aggregates 271 deduplicated papers across 2026-05-25 to 2026-05-30. The dominant arcs are **hidden states & mechanistic interpretability**, **optimizers & training dynamics**, **quantization & efficient inference**, **RL post-training**, and **LLM safety/alignment**.

---

## 本周必读 / Must Read This Week

以下 8 篇优先选取了跨天复现或被列为单日必读的工作——若本周只读这几篇，选它们。
The following 8 prioritize papers that recurred across days or were flagged as daily must-reads — the "if you read nothing else" list.

### [[2605.29548]] Why Larger Models Learn More: Effects of Capacity, Interference, and Rare-Task Retention

**推荐理由 / Why read:** 本周唯二跨两天复现并两次入选单日必读；用 OLMo 4M→4B 受控实验从梯度干扰与资源竞争角度机理化解释模型缩放优势，证明大模型能保留小模型被高频任务挤出的稀有任务，对能力涌现有直接启示。
Recurred across two days and was a daily must-read both times; OLMo 4M→4B controlled experiments give a mechanistic account of scaling advantages via gradient interference, proving larger models retain rare tasks that smaller ones crowd out — key insight into emergence.

### [[2605.29756]] LFQ: Logit-aware Final-block Quantization for Boosting Generation Quality of Low-Bit Quantized LLMs

**推荐理由 / Why read:** 同样跨两天复现；只需把最终 Transformer 块的 MSE 目标替换为交叉熵，即可显著提升低比特量化 LLM 的生成质量，AIME 推理任务 +13pp，ICML 2026 接收——改动极小、收益明确。
The other paper to recur across two days; simply swapping the final transformer block's MSE objective for cross-entropy markedly improves low-bit quantized generation quality (+13pp on AIME, accepted at ICML 2026) — minimal change, clear payoff.

### [[2605.29358]] Scaling Monosemanticity: Extracting Interpretable Features from Claude 3 Sonnet

**推荐理由 / Why read:** Anthropic 将稀疏自编码器扩展至 3400 万特征，在 Claude 3 Sonnet 上提取出跨语言、跨模态的可解释特征（代码语义、安全相关概念），是机械可解释性领域的里程碑工作。
Anthropic scales sparse autoencoders to 34M features on Claude 3 Sonnet, extracting multilingual, multimodal interpretable features (code semantics, safety concepts) — a landmark in mechanistic interpretability.

### [[2605.26099]] Language Models Need Sleep

**推荐理由 / Why read:** 提出类"睡眠"整合机制，在上下文窗口满时通过多轮离线循环把 KV 缓存信息压缩进 SSM 快速权重，巧妙地将额外计算与推理延迟解耦；实验从元胞自动机递进到数学推理，对长上下文架构设计有深远启示。
A sleep-like consolidation mechanism that compresses KV-cache information into SSM fast weights via offline iterative refinement when the context window fills, decoupling extra compute from inference latency; the synthetic-to-reasoning experimental ladder has deep implications for long-context architectures.

### [[2605.25507]] Credit Assignment with Resets in Language Model Reasoning

**推荐理由 / Why read:** SRPO 自定位首个错误推理步并重采样后续，在无需外部步骤监督下持续超越 GRPO，10 个推理基准与 LiveCodeBench 上收敛快 2–3 倍；方法简单直接，有望成为 RL 后训练新标准。
SRPO self-localizes the first erroneous reasoning step and resamples continuations, consistently beating GRPO with no step-level supervision and 2–3× faster convergence across 10 benchmarks and LiveCodeBench — simple, effective, a candidate new standard for RL post-training.

### [[2605.26842]] MONA: Muon Optimizer with Nesterov Acceleration for Scalable Language Model Training

**推荐理由 / Why read:** 用梯度差分 EMA 为 Muon 引入 Nesterov 加速，在 1B–68B MoE 预训练中收敛与下游性能均超越 Muon 和 AdamW，SFT 后 BigCode 达 SOTA——是目前 Muon 类优化器最有说服力的大规模实证。
Augments Muon with Nesterov acceleration via gradient-difference EMA, beating both Muon and AdamW across 1B–68B MoE pretraining and reaching SOTA on BigCode after SFT — the most compelling large-scale evidence yet for Muon-family optimizers.

### [[2605.27028]] Less is More: Early Stopping Rollout for On-Policy Distillation

**推荐理由 / Why read:** 识别在线策略蒸馏中的"Off-policy Teacher Decay"现象，提出极简的 ESR——只用前几个 token 的 rollout 做蒸馏，跨模型规模/家族/任务全面超越完整 rollout 且更省算力。
Identifies the Off-policy Teacher Decay problem in on-policy distillation and proposes the elegantly simple ESR (distill on only the first few rollout tokens), consistently outperforming full-rollout distillation across sizes, families, and tasks while being more compute-efficient.

### [[2605.29343]] Draft-OPD: On-Policy Distillation for Speculative Draft Models

**推荐理由 / Why read:** 识别投机解码中草稿模型 SFT 的"训练–推理不匹配"瓶颈，提出错误位置回放的在线蒸馏框架，在 Qwen3 思维模型上实现 5x+ 无损加速。
Identifies the training-inference mismatch bottleneck in speculative-decoding draft models; the error-position replay on-policy distillation framework achieves 5x+ lossless speedup on Qwen3 thinking models.

---

## 本周主题脉络 / Themes This Week

将本周约 12 个每日子主题归并为 6 条跨天脉络，每条只列代表作而非全部。
The ~12 daily sub-topics are merged into 6 cross-cutting arcs below, each with representative highlights only.

### 1. 隐藏状态、SAE 与机制可解释性 / Hidden States, SAEs & Mechanistic Interpretability

本周最大的脉络。从 Anthropic 把 SAE 扩到 3400 万特征的里程碑，到 SAE 工程化（残差化、半宽度、最优传输）、电路抽取与"表征 ≠ 控制"的反复警示——内部表征既被用来做数据选择和操控，又被反复发现与外在行为存在系统性鸿沟。
The week's largest arc. From Anthropic's 34M-feature SAE milestone to SAE engineering (residualization, half-width, optimal transport), circuit extraction, and a recurring "representation ≠ control" caution — internal states are leveraged for data selection and steering, yet repeatedly shown to diverge systematically from external behavior.

- [[2605.29358]] Scaling Monosemanticity — 34M 特征 SAE 扩展 / 34M-feature SAE on Claude 3 Sonnet
- [[2605.27033]] s-Trace — ~0.1% 计算图即可恢复 top-1，两阶段计算结构 / minimal compute subgraphs reveal a two-phase structure
- [[2605.27819]] ReSAE — 残差化 SAE 将多层干预 ΔCE 减半 / residualized SAEs halve multi-layer ∆CE
- [[2605.28639]] White Bear Effect — 指令抑制概念反使内部表征更可恢复 / suppression makes representations more recoverable
- [[2605.28649]] SAEs as Stethoscopes — SAE 子空间投影丢失 ~97% 修改能量 / SAE projection discards ~97% of modification energy
- [[2605.30076]] UniSteer — 流匹配实现文本引导的统一激活操控 / flow-matching unified activation steering

### 2. 优化器、训练动力学与可观测性 / Optimizers, Training Dynamics & Observability

Muon 家族本周密集出现（MONA、MuCon、对抗训练版），与谱控制、稀疏感知预条件、Local SGD 子空间估计等"训练几何"工作汇成一条主线，并延伸出优化器选择会改变缩放律指数这一更深层结论。
The Muon family clusters this week (MONA, MuCon, adversarial-training variant), joining spectral control, sparsity-aware preconditioning, and Local-SGD subspace estimation into a "training geometry" line — extending to the deeper claim that optimizer choice itself reshapes scaling-law exponents.

- [[2605.26842]] MONA — Muon + Nesterov, 1B–68B MoE SOTA / Nesterov-accelerated Muon
- [[2605.27733]] Entry-Wise Clipping — 梯度噪声局部化 → 无 SVD 谱控制 / Bayes-optimal shrinkage for spectral control
- [[2605.29387]] Optimizer Dependence — 优化器系统性改变缩放律指数 / optimizer changes scaling exponents
- [[2605.27739]] Worker Disagreement in Local SGD — worker 分歧作为无 Hessian 子空间估计 / Hessian-free subspace estimator
- [[2605.26097]] Forgetting in LMs — 容量瓶颈与自生成回放打破 LR–遗忘权衡 / self-generated replay breaks the LR–forgetting tradeoff

### 3. 量化、精度与高效推理 / Quantization, Precision & Efficient Inference

从极低比特量化（LFQ、HARP、OrpQuant、W4A4 视频扩散）到投机解码（Draft-OPD、Domino、Cassandra）、MoE 服务与 AFD 解耦，本周高效推理两端齐发力；同时浮点表达力与量化验证复杂度等理论结果为"计算可靠性"打底。
Efficient inference advances on both ends: from extreme low-bit quantization (LFQ, HARP, OrpQuant, W4A4 video diffusion) to speculative decoding (Draft-OPD, Domino, Cassandra), MoE serving, and Attention-FFN disaggregation — underpinned by theory on floating-point expressivity and quantized-verification complexity.

- [[2605.29756]] LFQ — 最终块交叉熵对齐，AIME +13pp / final-block cross-entropy, +13pp on AIME
- [[2605.29343]] Draft-OPD — 投机解码草稿模型在线蒸馏，5x+ 无损 / on-policy draft distillation, 5x+ lossless
- [[2605.29843]] HARP — 可学习蝶形旋转替代 Hadamard，极低比特 PTQ / learnable butterfly rotation for extreme PTQ
- [[2605.28704]] Floating-Point NN Expressivity — 任意归约顺序下仍为通用表示器，cos/cosh 例外 / universal representators under arbitrary reductions
- [[2605.28302]] Attention-FFN Disaggregation — DeepSeek-V3.2 上 ~4k tok/s / ~4k tok/s MoE serving

### 4. 强化学习与后训练 / RL & Post-Training

信用分配是本周 RL 的核心议题：SRPO 用"重置"定位错误步，ESR 揭示蒸馏中的教师衰减，Agent RL 出现独特的周期性熵爆发，配以图结构信用分配、滞后策略优化与数据分配/调度等改进。
Credit assignment dominates RL this week: SRPO uses resets to localize error steps, ESR exposes teacher decay in distillation, Agent RL shows distinctive cyclical entropy eruptions — complemented by graph-based credit assignment, hysteretic policy optimization, and data-allocation/scheduling refinements.

- [[2605.25507]] SRPO (Credit Assignment with Resets) — 自定位错误步重采样，超越 GRPO / reset-based credit assignment beats GRPO
- [[2605.27028]] ESR — 早停 rollout 的在线蒸馏 / early-stopping rollout distillation
- [[2605.27954]] SEAL — Agent RL 周期性熵爆发与辅助损失稳定化 / cyclical entropy eruption + stabilizing auxiliary loss
- [[2605.30201]] HPO — 滞后策略优化修复 GRPO 稀疏奖励 / hysteretic policy optimization for sparse rewards
- [[2605.29860]] ESPO — 代理遗憾值早停 PPO，省 22% rollout token / surrogate-regret early-stopping PPO

### 5. LLM 安全、对齐与隐私 / LLM Safety, Alignment & Privacy

本周安全脉络从"鲁棒性逆缩放"（大模型更易被干扰指令带偏）到 scheming 蜜罐评估、MoE 安全专家定位、token 计费攻击与 LoRA 后门，揭示对齐既脆弱又可被少量参数/扰动撬动。
The safety arc spans inverse scaling of robustness (larger models more easily derailed by distractor instructions), scheming honeypot evaluation, MoE safety-expert targeting, token-billing attacks, and LoRA backdoors — showing alignment is fragile and pivotable via small parameter/perturbation changes.

- [[2605.29491]] Curse of Helpfulness — 干扰指令鲁棒性逆缩放，GRPO 可恢复 15.5% / inverse scaling, GRPO recovers 15.5%
- [[2605.29729]] Scheming Honeypot — Google 真实代码库中的欺骗倾向评估 / honeypot scheming evaluation in real codebases
- [[2605.29708]] RASET — MoE 安全由少量专家参数控制 / safety controlled by few expert params
- [[2605.30040]] Token Inflation — 按 token 计费的信任悖论与攻击 / trust paradox in per-token billing
- [[2605.30189]] Token-Level Backdoors — LoRA 中 token 级后门的刻画与检测 / token-level LoRA backdoors

### 6. 理论、可靠性与评估 / Theory, Reliability & Evaluation

数学基础侧本周给出 SVRG/SGD-动量的泛化界、隐式思维链与上下文持续学习的首个理论框架、量化网络验证复杂度图谱；评估侧则反复敲打基准与评委的统计可靠性（多评委有效投票坍塌、排行榜分辨力不足）。
On foundations: generalization bounds for SVRG/SGD-momentum, first theories for implicit CoT and in-context continual learning, and a complexity landscape for quantized-network verification. On evaluation: repeated scrutiny of benchmark/judge statistical reliability (collapsing effective judge votes, insufficient leaderboard resolution).

- [[2605.28600]] Log-ICoT — 隐式思维链的首个理论分析 / first theory of implicit chain-of-thought
- [[2605.28705]] In-Context Continual Learning — 推理阶段也存在系统性遗忘 / forgetting even without parameter updates
- [[2605.29537]] Quantised FNN Verification — 验证复杂度完整图谱 / complete verification complexity landscape
- [[2605.29800]] Nine Judges, Two Effective Votes — 相关错误使 9 评委仅约 2 票 / correlated errors collapse 9 judges to ~2
- [[2605.30315]] Resolution Diagnostics — 排行榜相邻排名常统计未分辨 / adjacent leaderboard ranks often unresolved

---

## 全部论文 / All Papers

### 2026-05-25 (47)

- [[2605.19169]] Modeling the Impact of Fiber Latency on Compute-Communication Overlap in Geo-Distributed Multi-Datacenter AI Training — 光纤延迟对地理分布式AI训练计算通信重叠的影响建模
- [[2605.19775]] Understanding Inference Scaling for LLMs: Bottlenecks, Trade-offs, and Performance Principles — LLM推理扩展性理解：瓶颈、权衡与性能原则
- [[2605.22416]] Asymmetric Virtual Memory Paging for Hybrid Mamba-Transformer Inference — 混合Mamba-Transformer推理的非对称虚拟内存分页
- [[2605.23918]] The Model Parking Tax: Quantifying the Hidden Energy Cost of Always-On GPU Model Deployment — 模型停车税：GPU常驻部署隐藏能耗量化
- [[2605.24022]] Adaptive KV Cache Reuse for Fast Long-Context LLM Serving — 面向快速长上下文LLM服务的自适应KV缓存复用
- [[2605.24076]] Causality as the Statistical Conscience of AI: From Pearl's Ladder to Trustworthy Machines — 因果推断作为AI的统计良知：从Pearl阶梯到可信机器
- [[2605.24144]] EVA: Accelerating LLM Decoding via an Efficient Vector Quantization Architecture — EVA：基于高效向量量化架构加速LLM解码
- [[2605.24391]] MX-SAFE: Versatile Inference- and Training-Proof Microscaling Format — MX-SAFE：同时支持推理和训练的自适应微缩放格式
- [[2605.24461]] Provisioning to Runtime Optimization of a +100 MW AI Cluster — 百兆瓦级AI集群从规划到运行时的优化
- [[2605.24665]] An Energy-Efficient Approximate Posit Multiply-Divide Unit — 基于Posit数制的能效近似乘除法单元
- [[2605.24710]] Feature Learning in Wide Neural Networks under μP: Identifiability and Sparse-Dictionary Decomposition — μP下宽神经网络特征学习：可辨识性与稀疏字典分解
- [[2605.24749]] How Neural Reward Models Learn Features for Policy Optimization: A Single-Index Analysis — 神经奖励模型如何学习特征：单指数模型分析
- [[2605.24817]] RouteScan: A Non-Intrusive Approach to Auditing MoE LLMs Safety via Expert Routing Telemetry — RouteScan：基于专家路由遥测的非侵入式MoE安全审计
- [[2605.25151]] Representation Without Control: Testing the Realization Effect in Language Models — 表征不等于控制：语言模型中实现效应的测试
- [[2605.25234]] On the Epistemic Uncertainty of Overparametrized Neural Networks — 过参数化神经网络的认知不确定性
- [[2605.25272]] AI Cartography: Mapping the Latent Landscape of AI Benchmark Ecosystems — AI制图学：AI基准生态系统的潜变量景观映射
- [[2605.25507]] Credit Assignment with Resets in Language Model Reasoning — 语言模型推理中基于重置的信用分配 ⭐
- [[2605.25520]] Is Inference Mediated by Distinct Semantic Structures in LLMs? — LLM推理是否由不同的语义结构介导？
- [[2605.25603]] Detecting Unfaithful Chain-of-Thought via Circuit-Guided Internal-External Discrepancy — 通过电路引导的内外差异检测不忠实思维链
- [[2605.25604]] DVAO: Dynamic Variance-adaptive Advantage Optimization for Multi-reward RL — DVAO：多奖励强化学习中的动态方差自适应优势优化
- [[2605.25619]] Analogies between Transformer Layers and Power Method — Transformer层与幂迭代法的类比
- [[2605.25629]] When In-Distribution Gains Fail: Evaluating Weak-to-Strong Reward Models under Preference Shift — 分布内收益何时失效：偏好偏移下弱到强奖励模型评估
- [[2605.25658]] AutoSG: LLM-Driven Solver Generation Solely from Task Prompts — AutoSG：仅从任务提示生成优化求解器的LLM驱动流水线
- [[2605.25674]] Stochastic Estimation of the Layer-wise Hessian Trace for Monitoring Neural-network Training — 用于神经网络训练监控的逐层Hessian迹随机估计
- [[2605.25698]] How Should LLMs Consume High-Quality Data? Optimal Data Scheduling via Quality-Aware Functional Scaling Laws — LLM应如何消费高质量数据：基于质量感知缩放定律的最优调度
- [[2605.25704]] PowLU: An Activation Function for Stable Pre-Training of LLMs — PowLU：面向LLM稳定预训练的激活函数
- [[2605.25739]] The Behavioral Credibility Trilemma: When Calibrated Autonomy Becomes Impossible — 行为可信度不可能三角：校准自主性何时不可能
- [[2605.25799]] Addressing Exacerbated Attention Sink for Source-Free Cross-Domain Few-Shot Learning — 解决无源跨域小样本学习中加剧的注意力汇聚问题
- [[2605.25848]] Geometric Evolution Maps: Extracting Stable Concept Probes from Transformer Residual Streams — 几何演化图：从Transformer残差流中提取稳定概念探针
- [[2605.25880]] The Quantization Benefits of Residual-Free Transformers — 残差自由Transformer的量化优势
- [[2605.25891]] Causal Tongue-Tie: LLMs Can Encode Causal Direction, But Their Yes/No Outputs Fail to Express — Causal Tongue-Tie：LLM能编码因果方向但无法通过输出表达
- [[2605.25893]] D²-Monitor: Dynamic Safety Monitoring for Diffusion LLMs via Hesitation-Aware Routing — D²-Monitor：基于犹豫感知路由的扩散LLM动态安全监控
- [[2605.25902]] Reading the Finetuning Prior: Verbatim Content Recovery via Contrastive Decoding Diffing — 读取微调先验：通过对比解码差异法逐字恢复内容
- [[2605.25903]] Universal Activation Verbalizer: A Unified Framework for Cross-Model Activation Explanation — 通用激活解释器：跨模型激活解释的统一框架
- [[2605.25939]] From Latent Space to Training Data: Explainable Specialization in Minimal MLPs — 从潜空间到训练数据：最小MLP中的可解释特化
- [[2605.25966]] Mapping the Schedule x Bit-Width Boundary in Sub-100M Quantisation-Aware Training — 1亿参数以下量化感知训练中调度与位宽的边界映射
- [[2605.25988]] What Makes a Medical Checker Trainable? Signal Collapse and Reward Hacking in Checker-Guided RAG — 医学检查器何时可训练？检查器引导RAG中的信号坍塌与奖励黑客
- [[2605.25991]] Fuzzy PyTorch: Rapid Numerical Variability Evaluation for Deep Learning Models — Fuzzy PyTorch：深度学习模型的快速数值变异性评估
- [[2605.25997]] Deployment-complete benchmarking — 部署完备基准测试
- [[2605.25998]] Causal Methods for LLM Development and Evaluation — 面向LLM开发与评估的因果方法
- [[2605.26037]] Peak-Then-Collapse and the Four Interface Channels of Knowledge-Graph Tool Use — 知识图谱工具调用的峰崩现象与四接口通道
- [[2605.26045]] Confidence and Calibration of Activation Oracles for Reliable Interpretation of LLM Internals — 激活预言机的置信度与校准：可靠解读LLM内部状态
- [[2605.26046]] When Gradients Collide: Failure Modes of Multi-Objective Prompt Optimization for LLM Judges — 梯度冲突：LLM评判多目标提示优化的失败模式
- [[2605.26079]] Automated Benchmark Auditing for AI Agents and Large Language Models — AI智能体和大语言模型的自动化基准审计
- [[2605.26092]] OrpQuant: Geometric Orthogonal Residual Projection for Multiplier-Free PoT Quantization — OrpQuant：面向无乘法器PoT量化的几何正交残差投影
- [[2605.26097]] Forgetting in Language Models: Capacity, Optimization, and Self-Generated Replay — 语言模型中的遗忘：容量、优化与自生成回放 ⭐
- [[2605.26099]] Language Models Need Sleep — 语言模型需要睡眠 ⭐

### 2026-05-26 (50)

- [[2605.26403]] From Static Context to Calibrated Interactive RL — 强化学习 / RL
- [[2605.26409]] Jailbreak Susceptibility via Behavioral Geometry — 安全 / Safety
- [[2605.26415]] The Rescue Effect: Early Exit Bypasses CLIP Quantization Collapse — 量化 / Quantization
- [[2605.26431]] Probing Minimalist Phase Structure in LLMs — 可解释性 / Interpretability
- [[2605.26433]] Vectors Are Not Neutral: Privacy in LLM Summarization — 安全 / Safety
- [[2605.26459]] MuCon: Clipped Muon Updates for LLM Training — 优化器 / Optimizer
- [[2605.26468]] Diffuse to Detect: Diffusion for IC Anomaly Detection — 扩散模型 / Diffusion
- [[2605.26484]] Extra-Merge: Rank-1 Subspace Model Merging — 可解释性 / Interpretability
- [[2605.26489]] Singular Distribution Stability in LM Pre-training — 训练动力学 / Training Dynamics
- [[2605.26494]] MiniMax-M2: Mini Activations, Max Intelligence — 模型 / Model
- [[2605.26496]] Dense2MoE: Unified Pruning & MoE Upcycling — 量化 / Quantization
- [[2605.26526]] Fine-Tuning Defenses Susceptible to Simple Attacks — 安全 / Safety
- [[2605.26558]] Cassandra: Self-Speculative Decoding at Edge — 高效推理 / Efficient Inference
- [[2605.26577]] Bridging Control with alpha-beta-CROWN Tutorial — 形式化验证 / Formal Verification
- [[2605.26582]] Error-Correcting Stochasticity in Discrete Diffusion — 扩散模型 / Diffusion
- [[2605.26606]] Pilot-Commit: Rollout Allocation for RL Post-Training — 强化学习 / RL
- [[2605.26628]] Tail-Aware HiFloat4: W4A4 for Wan2.2 — 量化 / Quantization
- [[2605.26632]] RT-Lynx: Activation Sparsity for Diffusion Models — 高效推理 / Efficient Inference
- [[2605.26636]] JetViT: Post-Training Attention Search for ViT — 高效推理 / Efficient Inference
- [[2605.26647]] Mixture of Activations: Token-Adaptive FFN — 架构 / Architecture
- [[2605.26660]] WINDQuant: RL Mixed-Precision LLM Quantization — 量化 / Quantization
- [[2605.26667]] MemFail: Stress-Testing LLM Memory Systems — 智能体 / Agents
- [[2605.26670]] Knowledge Editing Regularizations Revisited — 安全 / Safety
- [[2605.26684]] GraphGPO: Graph-Based Credit Assignment for Agentic RL — 强化学习 / RL
- [[2605.26693]] EpiMer: Model Merging on Loss Landscape — 可解释性 / Interpretability
- [[2605.26726]] Uncertainty in Neural Cellular Automata — 其他 / Other
- [[2605.26731]] Harness Sensitivity Across LLM Agent Tiers — 智能体 / Agents
- [[2605.26733]] Stabilizing Looped LM Reasoning Dynamics — 智能体 / Agents
- [[2605.26735]] Layer Swap: Rethinking Multilingual Reasoning Gap — 可解释性 / Interpretability
- [[2605.26756]] Localizing Memorized Regions in Diffusion Models — 扩散模型 / Diffusion
- [[2605.26772]] CoT Disrupts Simple Steering of Refusal — 可解释性 / Interpretability
- [[2605.26789]] Composition Collapse in Factual Knowledge — 可解释性 / Interpretability
- [[2605.26795]] CoT Works via Local Co-Occurrence at Probe Time — 可解释性 / Interpretability
- [[2605.26827]] ContextGuard: Structured Self-Auditing for ICL — 安全 / Safety
- [[2605.26842]] MONA: Muon + Nesterov for Scalable LM Training — 优化器 / Optimizer ⭐
- [[2605.26895]] Scale Vectors in Large Language Models — 训练动力学 / Training Dynamics
- [[2605.26919]] Agile Online Model Selection with Large LR — 优化器 / Optimizer
- [[2605.26929]] Muon Meets Adversarial Training — 优化器 / Optimizer
- [[2605.26934]] RLVR Data Allocation: Reasoning Depth & Complexity — 强化学习 / RL
- [[2605.26958]] Tournament-GRPO for Open-Ended Generation — 强化学习 / RL
- [[2605.26971]] RLVR Datasets & Data Lineage (ATLAS/DAPO++) — 强化学习 / RL
- [[2605.26973]] SNR & Sample Size Govern Representational Alignment — 训练动力学 / Training Dynamics
- [[2605.26977]] Spectral Descent Convergence for Non-smooth Opt — 优化器 / Optimizer
- [[2605.27003]] SVDQuant-GPTQ: W4A4 for Wan2.2-I2V — 量化 / Quantization
- [[2605.27028]] ESR: Early Stopping Rollout for Distillation — 强化学习 / RL ⭐
- [[2605.27033]] s-Trace: Computation Density in LLMs — 可解释性 / Interpretability ⭐
- [[2605.27078]] Two Speeds of Learning: Grokking & Double Descent — 训练动力学 / Training Dynamics
- [[2605.27081]] ReMoE: Expert Reuse via Router Fine-Tuning — 高效推理 / Efficient Inference
- [[2605.27295]] Gemini Embedding 2: Multimodal Embedding — 嵌入 / Embedding
- [[2605.27354]] SAERL: SAE-Guided Post-Training Data Engineering — 强化学习 / RL

### 2026-05-27 (50)

- [[2605.27458]] Generic Interpretation for Heterogeneous Attention — 通用异质注意力结构Transformer解释方法，在DETR和LXMERT上优于GAE/ODAM基线。Generic interpretation for heterogeneous-attention Transformers, outperforming GAE/ODAM on DETR and LXMERT.
- [[2605.27541]] SparseOpt — 揭示Batch Normalization在稀疏训练中放大梯度偏转(1-s)^(-1/2)，提出感知稀疏度的预条件优化器。Shows BN amplifies sparse-neuron gradients by (1-s)^(-1/2); proposes sparsity-aware diagonal preconditioner.
- [[2605.27605]] Laguna M.1/XS.2 Technical Report — Poolside 225.8B/23.4B MoE模型面向长程智能体编码，XS.2从启动到发布仅5周，SWE-bench 74.6%。Poolside MoE foundation models for agentic coding; XS.2 built in 5 weeks, 74.6% on SWE-bench Verified.
- [[2605.27616]] NVFP4 QAT Architecture Study — FP4量化中模型架构选择（Swin Transformer）比量化配方对分割质量影响更大。Model architecture choice (Swin Transformer) matters more than quantization recipe for FP4 anomaly segmentation.
- [[2605.27646]] HQMQ KV Cache Compression — Hurwitz四元数乘法量化用于KV Cache压缩。Hurwitz Quaternion Multiplicative Quantization for KV cache compression in LLM inference.
- [[2605.27673]] When do CVNNs Help — 复数神经网络优势取决于数据表示、对称性匹配和优化协议，公平调参下优势大幅缩小。CVNN advantages are conditional on data representation, symmetry matching, and fair HP selection — gains shrink significantly.
- [[2605.27678]] Heterogeneous Parallelism for MLLM — 提出多模态LLM训练的异构并行抽象，共置模式下TFLOPS/GPU提升高达49.3%。Heterogeneous parallelism for MLLM training with up to 49.3% TFLOPS/GPU improvement in colocated mode.
- [[2605.27733]] Entry-Wise Clipping for Spectral Control — 利用梯度噪声局部化特性推导逐元素平滑收缩算子，以O(ε⁻⁴)复杂度实现谱范数控制。Derives Bayes-optimal smooth shrinkage for spectral gradient control without SVD, saving ~7% tokens on NanoGPT. ⭐
- [[2605.27739]] Worker Disagreement in Local SGD — 证明Local SGD中worker分歧天然揭示损失曲面尖锐方向，可作为无需Hessian的子空间估计器。Worker-average gap in Local SGD reveals sharp loss directions as a Hessian-free subspace estimator.
- [[2605.27763]] Batch-Conditioned Refusal Testing — 配对测试协议揭示batch条件可改变拒绝决策，但效应率仅~0.16%，可通过batch-invariant内核消除。Paired protocol shows batch-conditioned refusal flips at ~0.16% rate, eliminable via batch-invariant kernels.
- [[2605.27786]] LoRP Depth Compression — 分析LLM层间表示局部性实现自适应无训练深度剪枝。Analyzes representation locality across LLM layers for adaptive training-free depth pruning.
- [[2605.27803]] HammerSim (RowHammer) — 系统级RowHammer建模工具，基于gem5仿真器模拟DRAM行锤击漏洞。System-level RowHammer modeling tool built on gem5 simulator for DRAM vulnerability analysis.
- [[2605.27819]] ReSAE — 残差化SAE减少多层干预中的特征冗余，在Gemma-2-9B上将∆CE大致减半。Residualized SAEs reduce multi-layer intervention redundancy, roughly halving ∆CE on Gemma-2-9B.
- [[2605.27824]] Algorithmic Deductive Circuits — 定位约3%注意力头构成稀疏电路负责演绎推理各子步骤。~3% of attention heads form sparse circuits for deductive reasoning sub-steps via causal mediation analysis.
- [[2605.27935]] Do Agents Think Deeper — 自主式LLM智能体在多轮规划中递进式动员更深层次计算，呈"构建-精炼"模式。Autonomous LLM agents progressively engage deeper layers across planning turns in a build-refine pattern.
- [[2605.27954]] SEAL (Cyclical Entropy Eruption) — 发现Agent RL中周期性熵爆发现象，提出SEAL辅助交叉熵损失分离正确/错误轨迹表示。Discovers entropy eruption cycles in Agent RL; SEAL auxiliary loss separates correct/incorrect trajectory representations. ⭐
- [[2605.27970]] Perceptual Geometry in LLMs — 纯文本训练的LLM残差流中短暂涌现出与人类感知域高度对齐的几何结构。Text-trained LLMs transiently develop geometric structures in residual streams mirroring human perceptual organization.
- [[2605.27989]] Law of Neural Interaction — 发现深度-宽度比控制的高效神经交互区间随规模保持稳定，与MMLU-Pro性能相关。Depth-width ratio governs efficient neural interaction interval that remains stable across scales.
- [[2605.28057]] Recovery Complexity TTA — 首个TTA可学习性理论框架，引入恢复复杂度刻画非平稳测试流下的基本极限。First TTA learnability framework with recovery complexity characterizing fundamental limits under non-stationary streams.
- [[2605.28109]] IB-TPO — 基于信息瓶颈的IB-Score度量和树结构采样，在相同token预算下多生成50%轨迹。Information-Bottleneck-based IB-Score and tree sampling generate 50% more trajectories under same token budget.
- [[2605.28142]] Marginal Sharpening — 对答案边缘分布进行power sharpening，在数学/代码生成上超越传统power sampling且快38倍。Power sharpening on answer marginals beats traditional power sampling at 38x speed on math/code generation.
- [[2605.28149]] SA-GSAE — Bi-Jump-ReLU使单个潜在变量编码反相关概念，半宽度SAE Pareto优于全宽度Gated SAE。Bi-Jump-ReLU enables single latents to encode anticorrelated concepts; half-width SAE Pareto-dominates full-width.
- [[2605.28150]] Off-Policy Pessimism — 无重要性权重的离策略目标通过Lambert W函数隐式引入悲观性，β偏移优势估计稳定训练。Ratio-free off-policy objectives induce Lambert-tempered pessimism; β-shifted advantage stabilizes training.
- [[2605.28165]] Robust Supervised Learning Unification — 三轴四阶段统一框架将DRO/VRM/Mixup等方法组织在同一设计空间中，联合HPO达到最佳单方法性能。Three-axis four-stage unified framework for robust learning; joint HPO matches best single-method baselines.
- [[2605.28169]] FT-Pilot — GNN引导LLM自动识别RTL易受攻击资产并生成容错代码，实现漏洞分析到加固的全自动闭环。GNN-guided LLM framework for automated fault-tolerant RTL rewriting from vulnerability analysis to hardening.
- [[2605.28184]] RL-MTP (OCC) — 分析多Token预测与RL联合训练失败原因，提出最优系数校准自适应调节MTP系数。Identifies MTP-RL gradient decorrelation as failure cause; proposes Optimal Coefficient Calibration.
- [[2605.28247]] IRDS — SAE聚类实现可解释RLVR数据选择，超越最强基线+3.9/+4.0 pp且成本低一个数量级。SAE-cluster-based interpretable RLVR data selection, +3.9/+4.0 pp over strongest baseline at 10x lower cost.
- [[2605.28302]] Attention-FFN Disaggregation — 系统探索MoE推理中AFD设计空间，在DeepSeek-V3.2上实现~4k tokens/s吞吐量。Design-space exploration of Attention-FFN Disaggregation for MoE serving, achieving ~4k tok/s on DeepSeek-V3.2.
- [[2605.28388]] Sample Difficulty in RLVR — 通过T-SAE分析样本难度对RLVR的非单调影响，中等难度样本效果最佳。T-SAE analysis shows non-monotonic effect of sample difficulty on RLVR; medium difficulty is optimal.
- [[2605.28398]] HRBench — 首个评估混合推理LLM思考模式切换策略的统一基准，覆盖12种配置。First unified benchmark for thinking-mode switching in hybrid-reasoning LLMs across 12 configurations.
- [[2605.28451]] BFP FP16 SAR — FP16 FFT瓶颈是指数范围溢出而非精度，两行BFP代码修改实现Apple Silicon上2.2×加速。FP16 FFT bottleneck is exponent range overflow, not precision; 2-line BFP fix achieves 2.2x speedup on Apple Silicon.
- [[2605.28467]] ACT (Activation Consistency) — 激活一致性约束防御推理模型越狱攻击，防御机制编码为近似线性方向。Activation consistency at assistant-turn boundary defends against jailbreaks; encoded as a linear refusal direction.
- [[2605.28513]] SVRG Learning Theory — 首次通过算法稳定性为SVRG建立非平凡泛化界，推广至SAGA方法。First non-vacuous SVRG generalization analysis via algorithmic stability, extended to SAGA.
- [[2605.28517]] SGDM Stability — 首次为SGD动量建立紧致泛化界，动量仅以O(1/(1-β)^{3/2})影响稳定性。First tight stability bounds for SGD momentum; momentum worsens stability by at most O(1/(1-β)^{3/2}).
- [[2605.28553]] Refusal Before Decoding — 证明拒绝行为可从中间层残差流线性解码，Mechanistic AutoDAN搜索时间减少最多72%。Refusal linearly decodable from intermediate layers; Mechanistic AutoDAN reduces search time by up to 72%.
- [[2605.28554]] TFM Uncertainty — 表格基础模型预测性能优于GBDT但共形预测条件覆盖率显著更低，揭示性能-可靠性权衡。TFMs outperform GBDTs in AUC but show systematically lower conditional coverage under conformal prediction.
- [[2605.28567]] Semantic OT for SAE — 将SAE特征表示为激活加权分布，通过最优传输计算跨层Wasserstein距离统一特征匹配与电路压缩。Represents SAE features as activation-weighted distributions; OT unifies cross-layer matching and circuit compression.
- [[2605.28585]] Outer-Momentum Restarting — 在DiLoCo等两阶段优化器中周期性重置外层动量，利用相位消除扩大稳定超参数区间。Periodic outer-momentum reset in two-phase optimizers exploits phase cancellation to widen stable HP region.
- [[2605.28600]] Log-ICoT (Transformers Internalize CoT) — 首次理论分析隐式思维链，证明多层Transformer仅需poly(n)样本和log₂k阶段学会k-奇偶校验。First theoretical analysis of implicit CoT; L-layer Transformer learns k-parity with poly(n) samples in log₂k stages.
- [[2605.28613]] Perturbed Matrix Factorization — 量化加性噪声对深度矩阵分解隐式正则化的影响，给出扰动大小的显式误差界。Quantifies additive noise impact on implicit regularization in deep matrix factorization with explicit error bounds.
- [[2605.28631]] SHIFT (RIRS) — 单次推理隐藏状态变化作为无训练数据选择代理，0.1-2%数据超越全量RLVR。Single-rollout hidden-state shift as training-free data selection proxy; 0.1-2% data beats full RLVR.
- [[2605.28639]] Attentional White Bear Effect — 指令抑制某概念时其内部表征反而保持高度可恢复——行为与表征对齐存在根本差距。Concept suppression instructions make internal representations more recoverable — behavioral vs. representational alignment gap.
- [[2605.28649]] SAEs as Stethoscopes — SAE子空间投影丢失~97%修改能量，改用SAE诊断层后注入原始任务向量更有效。SAE subspace projection discards ~97% modification energy; using SAEs only for layer diagnosis works better.
- [[2605.28664]] Activation Steering Diversity — 激活转向生成安全检测合成数据需同时满足概念对齐、语义连贯和多样性。Activation steering for safety data requires success + coherence + diversity for downstream utility.
- [[2605.28704]] Floating-Point NN Expressivity — 浮点NN在任意归约顺序和有界ulp误差下仍为通用表示器，cos/cosh则不行。Floating-point NNs with arbitrary reduction orders remain universal representators; cos/cosh provably fail. ⭐
- [[2605.28705]] In-Context Continual Learning — 首个上下文持续学习理论框架，揭示Transformer推理阶段也存在系统性偏差和遗忘。First in-context continual learning theory showing systematic bias and forgetting even without parameter updates.
- [[2605.28722]] MARI (Multi-Adapter Interventions) — 竞争性多适配器+能量门控实现自适应表示干预，6个模型(7B-32B)上达到SOTA对齐。Competitive multi-adapter with energy gating for adaptive representation intervention across 6 models (7B-32B).
- [[2605.28732]] MemTrace — 将LLM记忆管道转化为可执行记忆演化图，归因信号指导提示优化提升最高7.62%。Transforms LLM memory pipelines into evolution graphs; attribution-guided prompt optimization boosts up to 7.62%.
- [[2605.28751]] EWA Code RL — 在代码RL中发现不同覆盖率checkpoint形成正确性-效率前沿，外推可扩展该前沿。Checkpoints at different test coverage form correctness-efficiency frontiers; extrapolation extends beyond endpoints.
- [[2605.28819]] PEFT-Arena — 从稳定性-可塑性视角评估PEFT方法，发现正交微调(OFT)在权重谱保持上表现最优。Benchmarks PEFT stability-plasticity trade-off; orthogonal finetuning achieves best Pareto frontier.

### 2026-05-28 (50)

- [[2605.29396]] Aligned but Fragile — 零阶优化, 安全对齐鲁棒性, 量化鲁棒性 ↻05-29
- [[2605.29459]] Kronecker Embeddings — 字节级嵌入, 参数高效, 拼写鲁棒性
- [[2605.29491]] Curse of Helpfulness — 逆缩放定律, 干扰指令鲁棒性, GRPO ⭐
- [[2605.29494]] Learning to Perturb Gradients — 梯度扰动统一框架, 长尾分类, 噪声标签 ↻05-29
- [[2605.29498]] Mask the Target (TMKL) — LoRA灾难性遗忘, KL正则化, 无回放 ↻05-29
- [[2605.29507]] Xetrieval — 稠密检索机制化解释, TopK-SAE, 推理内化器
- [[2605.29524]] KBF — API审计, 知识边界指纹, 黑盒检测 ↻05-29
- [[2605.29525]] Learning to Perturb Activations — 隐藏层扰动, 泛化, 域泛化
- [[2605.29537]] Quantised FNN Verification — 计算复杂度, NP完全, PSPACE完全 ↻05-29
- [[2605.29547]] S-Adam Optimizer — 非光滑优化, 量化感知训练, Clarke次微分 ↻05-29
- [[2605.29548]] Why Larger Models Learn More — 缩放定律, 多任务学习, 梯度干扰 ⭐ ↻05-29
- [[2605.29580]] LoRA-Curve — 贝叶斯推理, 模式连接, Bezier曲线 ↻05-29
- [[2605.29601]] Deliberative Monitors — AI安全, scheming检测, 知识蒸馏
- [[2605.29628]] COMET — 模态间隙, CLAP嵌入空间, PLS-SVD
- [[2605.29629]] Temporal Logit Observability — 解码时序动态, logit分析, 安全评估
- [[2605.29634]] Relational Rank Geometry — Plucker坐标, 关系帧, 表示几何 ↻05-29
- [[2605.29664]] AMDP — 异步流水线并行, 分布式训练, 收敛保证 ↻05-29
- [[2605.29700]] Set Shaping Theory — 哈希表优化, 内存访问, 数据库索引
- [[2605.29705]] BitTP — 1.58-bit量化, 轨迹预测, 边缘部署
- [[2605.29708]] MoE Safety Experts — MoE安全, 专家调优, 红队测试 ↻05-29
- [[2605.29714]] MoE Routing for Adaptation — MoE路由动态, 多语言适应, 低资源
- [[2605.29716]] NaRA — 扩散语言模型, 噪声感知LoRA, 超网络 ↻05-29
- [[2605.29737]] Prompt Fragility in Code — LLM代码安全, 隐藏状态探测, prompt扰动
- [[2605.29751]] DySem — 语义相似度, 多语言共识, 注意力输出
- [[2605.29752]] GEMM Ruggedness — GEMM性能优化, DP填充, GPU性能分析
- [[2605.29756]] LFQ — logit对齐, 最终块量化, 生成质量 ⭐ ↻05-29
- [[2605.29782]] Hista — 隐藏状态价值估计, RL信用分配, PPO critic ↻05-29
- [[2605.29816]] Non-Adversarial Robustness — 扰动诱导偏差, 认证鲁棒性, prompt鲁棒性 ↻05-29
- [[2605.29823]] Polynomial Simplicity — 有效次数, 泛化预测, grokking追踪
- [[2605.29843]] HARP — 自适应旋转, Hadamard替代, 极端量化 ↻05-29
- [[2605.29888]] LaRA — 数据污染检测, RL后训练, 表征几何 ↻05-29
- [[2605.29889]] SAE Clinical Triage — SAE可解释性, 临床分诊, 输出格式偏差
- [[2605.29901]] LLM Vulnerability Detection — 机制可解释性, 代码安全, 电路分析 ↻05-29
- [[2605.29971]] Causal Interventions on Verbs — 因果干预, 动词偏好, 结构启动
- [[2605.29979]] Fingerprinting Inference Systems — 推理系统指纹, 数值偏差, 黑盒攻击 ↻05-29
- [[2605.30018]] Latent Performance Profiling — 隐藏状态评估, 不确定性校准, 有效秩
- [[2605.30022]] DSTG-NeoBERT — 位置编码解耦, 二维流形塌缩, 注意力头分化 ↻05-29
- [[2605.30049]] SafeDIG — DiT安全干预, SAE, 跨域迁移
- [[2605.30076]] UniSteer — 流匹配, 激活空间操控, 文本引导 ↻05-29
- [[2605.30161]] VLM Spatial Representation — 垂直距离纠缠, 空间推理偏差, 合成基准
- [[2605.30162]] BioRefusalAudit — SAE生物安全审计, 拒绝深度, 格式敏感性
- [[2605.30201]] HPO — GRPO改进, 稀疏奖励, 滞后策略优化 ↻05-29
- [[2605.30218]] MarginGate — 推理确定性, logit margin, 稀疏验证 ↻05-29
- [[2605.30232]] Functional Welfare Axis — RL表征工程, 福祉轴, 情绪效价 ↻05-29
- [[2605.30233]] Entity Tracking in LLMs — 实体追踪, 并行聚合, 全局抑制标签
- [[2605.30260]] Parametric Memory Law — LoRA记忆容量, 幂律, 相变
- [[2605.30315]] Resolution Diagnostics — 假设检验, 排行榜可靠性, 样本量 ↻05-29
- [[2605.30334]] Data Organization for LLMs — 数据排序, 课程学习, 训练效率 ↻05-29
- [[2605.30335]] Compositional Incoherence — 多智能体一致性, 概率公理, 几何修复
- [[2605.30343]] RiM (Reasoning in Memory) — 潜在推理, 工作记忆, 推理效率

### 2026-05-29 (24)

- [[2605.29343]] Draft-OPD — 在线策略蒸馏框架解决投机解码草稿模型训练瓶颈 / On-policy distillation solves draft model training bottleneck in speculative decoding ⭐
- [[2605.29350]] ConMoE — 免训练 MoE 专家池压缩通过确定性重映射 / Train-free MoE compression via deterministic prototype reassignment
- [[2605.29351]] Attention as Empirical Bayes — 注意力机制的两阶段经验贝叶斯去噪解释 / Two-stage empirical Bayes interpretation of attention denoising
- [[2605.29358]] Scaling Monosemanticity — 34M 特征 SAE 在 Claude 3 Sonnet 上的可解释性扩展 / 34M-feature SAE scaling on Claude 3 Sonnet ⭐
- [[2605.29359]] Distributed Training Governance — 分布式训练模拟器揭示算力治理漏洞 / Distributed training simulator reveals compute governance loopholes
- [[2605.29360]] MiraBench — 机器人世界模型动作条件可靠性分层基准 / Hierarchical benchmark for robotic world model reliability
- [[2605.29380]] TRACER — WMA 教师替代 EMA 解决对比微调中的坍塌 / WMA teacher replaces EMA to fix collapse in contrastive finetuning
- [[2605.29387]] Optimizer Dependence — 优化器选择系统性地改变缩放律指数 / Optimizer choice systematically changes scaling law exponents
- [[2605.29440]] SkillBrew — LLM Agent 技能库的多目标帕累托策展 / Multi-objective Pareto curation of LLM agent skill banks
- [[2605.29448]] Dataset Worth Scaling Laws — 矩阵谱函数统一数据评估目标与 secular equation 加速 / Matrix spectral functions unify data appraisal with secular equation speedup
- [[2605.29467]] Composing Factor Graphs — 五种因子图基元实现闭式变分推断 / Five factor-graph primitives enable closed-form variational inference
- [[2605.29495]] On-Policy Replay — 在线策略回放将持续 SFT 遗忘降低 42-46% / On-policy replay cuts continual SFT forgetting by 42-46%
- [[2605.29496]] Asymmetric Optimization — VLM 后训练中推理与感知的不对称优化诊断 / Diagnosing asymmetric optimization of reasoning vs. perception in VLM post-training
- [[2605.29535]] AsymVLM — 非对称 token 剪枝节省 VLM 54% FLOPs / Asymmetric token pruning saves 54% FLOPs for VLMs
- [[2605.29684]] Kernel Renormalization — 等价 Wishart 假设预测有限宽度贝叶斯深度网络 / Equivalent Wishart ansatz predicts finite-width Bayesian deep networks
- [[2605.29800]] Nine Judges — 9 个 LLM 评委仅提供约 2 个有效独立投票 / 9 LLM judges provide only ~2 effective independent votes
- [[2605.29860]] ESPO — 早期停止 PPO 利用代理遗憾值节省 22% rollout token / Early-stopping PPO saves 22% rollout tokens via surrogate regret
- [[2605.30085]] CROP — 保形风险控制认证推理链前缀的正确性 / Conformal risk control certifies reasoning trace prefix correctness
- [[2605.30104]] SEAL — 种子淘汰赛与元评委恢复饱和基准排名信号 / Seeded elimination with meta-judge revives saturated benchmark signals
- [[2605.30112]] Striding Reynolds — 表征几何决定神经 PDE 求解器跨雷诺数泛化 / Representation geometry governs neural PDE cross-regime generalization
- [[2605.30117]] VLA-Trace — 渐进式诊断框架揭示 VLA 模型模态适应差异 / Progressive diagnostic framework reveals VLA model modality adaptation differences
- [[2605.30155]] PMNR — 部分多神经元松弛比基线多解决 49% 验证查询 / Partial multi-neuron relaxation solves 49% more verification queries
- [[2605.30184]] AI Weather Models — 九个 AI 天气模型两年滚动预测的失败模式分类 / Failure mode taxonomy from 2-year rollouts of nine AI weather models
- [[2605.30189]] Token-Level Backdoors — LoRA 后门在 token 特征级泛化的刻画与检测 / Characterization and detection of token-level generalizing LoRA backdoors

### 2026-05-30 (50)

- [[2605.29384]] Latent Terms — 稠密检索 / SAE / BM25 / 信息检索
- [[2605.29395]] Low Rank for Rank — LLM 评估 / 低秩矩阵 / 不确定性量化
- [[2605.29454]] MIA Framework — 成员推理 / 隐私审计 / 机器遗忘
- [[2605.29460]] FedSmoothLoRA — 联邦学习 / LoRA / 参数高效微调
- [[2605.29497]] Convex Basins SIM — 单指标模型 / 鲁棒统计 / 优化景观
- [[2605.29586]] FinVerBench — LLM 评估 / 财务验证 / 校准
- [[2605.29604]] TC-MIS — GPU 计算 / 图算法 / Tensor Core
- [[2605.29637]] IndicKLAR — 跨语言一致性 / 印度语言 / 多语言 LLM
- [[2605.29645]] Sparse Bandits — 上下文赌博机 / 样本复杂度 / 多类别
- [[2605.29667]] ChiSafe-PAS — LLM 安全 / 中文 NLP / 对抗评估
- [[2605.29668]] GRASP — LLM Agent / 自改进 / 技能库
- [[2605.29669]] Eigen-Spike CK — 随机矩阵 / 共轭核 / 相变
- [[2605.29678]] Spurious Prompts — 提示工程 / LLM 鲁棒性 / 提示敏感性
- [[2605.29682]] Agent Scaling Laws — Agent 缩放定律 / 测试时计算 / 反馈质量
- [[2605.29707]] Domino — 推测解码 / LLM 推理 / 因果建模
- [[2605.29726]] SLAD — 知识蒸馏 / LoRA / 视觉 Transformer
- [[2605.29729]] Scheming Honeypot — AI 安全 / 欺骗评估 / 蜜罐
- [[2605.29786]] Croissant Tasks — 可复现性 / 元数据格式 / LLM Agent
- [[2605.29788]] Nested Causal Bandits — 因果赌博机 / PAC-Bayes / 安全部署
- [[2605.29801]] AgentDoG 1.5 — Agent 安全 / AI 对齐 / 护栏模型
- [[2605.29819]] Interpolation Aggregation — 学习理论 / 回归 / 样本复杂度
- [[2605.29836]] CB-SLICE — 可解释性 / 概念瓶颈模型 / 错误切片
- [[2605.29847]] EvoRubric — 强化学习 / LLM 对齐 / 自演化评分
- [[2605.29881]] BRACS — VLM 幻觉 / 推理时引导 / 注意力接地
- [[2605.29908]] Joint ARD — 稀疏贝叶斯学习 / 鲁棒回归 / 边缘似然
- [[2605.29994]] Precomputed 1D-CNNs — FPGA / LUT 预计算 / 边缘 ML
- [[2605.30015]] TTT-SCL — 因果发现 / 测试时训练 / 分布偏移
- [[2605.30029]] RAISE — RAG / 超参数优化 / 架构搜索
- [[2605.30040]] Token Inflation — LLM 安全 / Token 计费 / 审计
- [[2605.30075]] Q-ANCHOR — 量子联邦学习 / 误差缓解 / 分布式优化
- [[2605.30096]] LLM Pentesting — LLM 安全 / 渗透测试 / 实证研究
- [[2605.30103]] LLM-NAS Convergence — 神经架构搜索 / LLM 理论 / 收敛分析
- [[2605.30123]] xMK-CKKS OTA — 联邦学习 / 同态加密 / 无线通信
- [[2605.30148]] AWD for ES — 进化策略 / 持续学习 / LLM 微调
- [[2605.30153]] Diffusion Optimal — 扩散模型 / 统计理论 / 样本复杂度
- [[2605.30154]] RL2ML — RLVR / 强化学习 / 代理目标
- [[2605.30188]] CalArena — 校准 / 基准 / 后校准
- [[2605.30190]] MF-Diffuser — 离线 RL / 均值场 / 多智能体
- [[2605.30202]] Dual-Path LLM — 循环 Transformer / 计算缩放 / 自适应路由
- [[2605.30219]] Belief Management — 信念追踪 / 强化学习 / LLM 评估
- [[2605.30229]] Anti Mode-Collapse — 均场理论 / Transformer / 模式坍缩
- [[2605.30253]] Wasserstein CAVI — 变分推断 / Wasserstein 距离 / 收敛分析
- [[2605.30288]] MIRA — 数据选择 / 中间训练 / 规则发现
- [[2605.30290]] STV — 自改进 / 验证器 / 推理时计算
- [[2605.30292]] LWO Jackknife — 保形预测 / 时间序列 / 预测推断
- [[2605.30319]] HTE Matrix Completion — 因果推断 / 矩阵补全 / 异质性处理效应
- [[2605.30322]] Gram — AI 对齐 / AI 安全 / 自动化审计
- [[2605.30329]] SoundnessBench — AI Scientist / LLM 评估 / 同行评审
- [[2605.30330]] Posterior Sampler Failures — 扩散模型 / 后验采样 / 逆问题
- [[2605.30348]] LLMSurgeon — LLM 可解释性 / 数据混合估计 / 逆问题


---

> 本文是 2026-05-25 至 2026-05-30 每日 digest 的汇总（rollup）。每日详情见：[2026-05-25](../../2026-05-25/overview.md) · [2026-05-26](../../2026-05-26/overview.md) · [2026-05-27](../../2026-05-27/overview.md) · [2026-05-28](../../2026-05-28/overview.md) · [2026-05-29](../../2026-05-29/overview.md) · [2026-05-30](../../2026-05-30/overview.md)。
> This is a rollup of the daily digests for 2026-05-25 through 2026-05-30. See each day for full detail (links above).
