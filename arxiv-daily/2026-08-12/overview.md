---
title: "Daily arXiv Digest — 2026-08-12"
date: 2026-08-12
tags: [arxiv, daily-paper, llm, research, agents, interpretability, reasoning]
papers: 50
---

# 每日 arXiv 精选 — 2026-08-12 / Daily arXiv Digest — 2026-08-12

> 共精选 50 篇论文，覆盖 LLM 训练/强化学习、可解释性、智能体、推理与校准、评测、量化与硬件、理论与基础、安全与可信等方向。
> 50 curated papers spanning LLM training/RL, interpretability, agents, reasoning & calibration, evaluation, quantization & hardware, theory & foundations, and safety/trustworthiness.

---

## 今日必读 / Must Read Today

### 1. [[2608.12036]] — Mechanist: AI as a Scientific Instrument for Discovering the Mechanisms of Intelligence

> **中文理由：** 这是一个把 AI 当作"科学仪器"来自主发现可解释性机制的多智能体系统——配以约 1.3 万篇论文知识图谱、32 种机制分析方法，复现可靠性显著超过 Claude Code 和 AI Scientist，并独立发现了跨模态"潜意识学习"安全风险与可分离的信念机制理论，还能将其转化为对 Pythia 和 Evo2 的可控干预。兼具"自主科研智能体"与"机制发现"两大用户兴趣点，影响力极高。
>
> **English reason:** An agentic system that autonomously generates, executes, and verifies mechanistic-interpretability hypotheses, beating Claude Code and AI Scientist on a 16-paper reproduction benchmark while independently uncovering a cross-modal subliminal-learning safety risk, a separable belief-mechanism theory, and turning them into controllable interventions on Pythia and Evo2. Sits squarely at the intersection of autonomous-research agents and mechanistic discovery.

### 2. [[2608.11674]] — GCPO: Diagnosing and Constraining Subspace Geometry in Rollout RL for LLMs

> **中文理由：** 提出主子空间重叠度诊断，发现 GRPO 中与预训练主子空间重叠的更新尖峰预示性能下降；据此用双侧正交投影把策略更新约束在正交补空间中，在数学/代码/工具使用上稳定超越 GRPO、DAPO、GSPO、GMPO，并关键地防止了 GRPO 在跨任务时的能力崩溃（数学训练后工具能力 −14.97，GCPO 仅 +0.91）。对 LLM 强化学习训练极有指导价值。
>
> **English reason:** Introduces a principal-subspace-overlap diagnostic showing transient GRPO update spikes precede degradation, then enforces a hard bilateral-orthogonality constraint that beats GRPO/DAPO/GSPO/GMPO on math/code/tool-use while critically preventing capability collapse (GRPO loses −14.97 on tool-use after math-only training; GCPO retains +0.91). A substantive, broadly-validated contribution to LLM RL training.

### 3. [[2608.11941]] — OEIS Open: How Many Conjectures Can Language Models Turn Into Theorems?

> **中文理由：** 基于 OEIS 中 492 个已 Lean 形式化的开放数学猜想构建基准，仅配备极简工具（bash、编辑器、Lean 工具链）的 ReAct 智能体在 50 美元/题预算下解出 30%（147/492），大幅超过 AlphaProof Nexus 的 9%（44/492），是 LLM 形式化推理能力的标志性结果。
>
> **English reason:** Releases OEIS_OPEN, a benchmark of 492 open OEIS conjectures formalized in Lean, where a minimal ReAct agent (bash + editor + Lean) solves 30% (147/492) at $50/conjecture versus AlphaProof Nexus's 9% (44/492). A landmark result for LLM formal-reasoning capability, with a clean open-source secure harness.

---

## 按主题分类 / Papers by Topic

### A. LLM 训练、强化学习与蒸馏 / LLM Training, RL & Distillation

| Paper | Title | 描述 / Description |
|-------|-------|--------------------|
| [[2608.11669]] | Rubric Dropout: A Simple Way to Mitigate Reward Hacking in Rubric-as-Reward RL | 每步随机丢弃部分评分准则以缓解奖励黑客，OOD 金标分数提升 2–7pp / Drops a random rubric subset each RL step to curb reward hacking, lifting OOD gold scores by 2–7pp. |
| [[2608.11674]] | GCPO: Diagnosing and Constraining Subspace Geometry in Rollout RL for LLMs | 用双侧正交投影约束策略更新，稳定超越 GRPO/DAPO 并防止跨任务能力崩溃 / Projects updates orthogonally to pretrained principal subspaces, beating GRPO/DAPO while preventing cross-task collapse. |
| [[2608.11698]] | REOPD: Reliability-Adaptive Reward Extrapolation for On-Policy Distillation | 用 token 级自适应外推系数替代全局 λ，无需 verifier 即超越逐域调优蒸馏 / Token-level adaptive extrapolation replaces global λ, beating per-domain-tuned distillation with no verifier. |
| [[2608.11829]] | Towards Understanding On-Policy Distillation Through the Lens of Test-Time Scaling | 揭示在策略蒸馏只提升采样效率而非扩展能力边界，称其为"虚假蒸馏" / Shows on-policy distillation only improves sampling efficiency, not the capability boundary—"illusory distillation." |
| [[2608.11758]] | AWARe: Mitigating Catastrophic Forgetting via Activation-Weighted Adaptive Retention | 按激活显著度冻结最关键 30% 参数，仅训 ~17.5% 即缓解遗忘并提升下游 / Freezes top-30% saliency params to mitigate forgetting while training only ~17.5%. |
| [[2608.12218]] | Information Abundance Paradox: Long-Context Training Undermines Parametric Knowledge | 训练上下文越长越相关，模型越依赖上下文而非写入参数，呈倒 U 型并损害鲁棒性 / Richer/longer training context makes models read from context instead of encoding weights, yielding an inverted-U. |

### B. 推理、测试时计算与校准 / Reasoning, Test-Time Compute & Calibration

| Paper | Title | 描述 / Description |
|-------|-------|--------------------|
| [[2608.11941]] | OEIS Open: How Many Conjectures Can Language Models Turn Into Theorems? | 极简 ReAct 智能体解出 30% 的开放 OEIS 猜想，远超 AlphaProof Nexus 的 9% / A minimal ReAct agent solves 30% of open OEIS conjectures vs AlphaProof Nexus's 9%. |
| [[2608.11994]] | Claim-Level Reliability Assessment for Efficient Test-Time Reasoning | 把推理 trace 压缩为关键 claim 做证伪式验证，同等预算下提准确率并省 token / Condenses traces into critical claims for falsification verification, boosting accuracy at lower token cost. |
| [[2608.12008]] | Asymptotic Risk Calibration for Selective Question Answering | 事后阈值校准使被接受答案错误率渐近控制到 α，多保留约 7pp 答案 / Post-hoc calibration asymptotically controls accepted-answer error to α, retaining ~7pp more answers. |
| [[2608.12100]] | Confidence Calibration of Deep Learning Systems | 博士论文系统解决标签噪声/隐私/域漂移下的校准，逼近干净标签 Oracle 上界 / Ph.D. thesis making calibration robust to noise/privacy/shift, approaching clean-label oracle bounds. |

### C. 智能体与工具使用 / Agents & Tool Use

| Paper | Title | 描述 / Description |
|-------|-------|--------------------|
| [[2608.11552]] | Beyond Single-Turn Confidence: Trajectory-Adapted UQ for LLM Agents | 评估三类单轮不确定性方法迁移到多轮智能体，"有用但不均"、无普适方法 / Adapts single-turn UQ to multi-turn agents; transfer is "useful but uneven," no universally reliable scorer. |
| [[2608.11632]] | Beyond Memory: A Transactional Continuity Kernel for Long-Lived AI Agents | 为长生命周期智能体定义激活契约控制平面，280 万状态穷举验证零违反 / Defines an activation-contract control plane, exhaustively verifying zero violations over 2.8M states. |
| [[2608.11654]] | Towards a Formal Definition of Agent Memory: Basis, Span, Optimality... | 首个统一形式化——记忆是基、知识是张成、可回答性是覆盖问题，统一为序贯 MDP / First unified formalization: memory as basis, knowledge as span, answerability as coverage, a sequential MDP. |
| [[2608.11772]] | Diagnosis Before Recovery: Turning Agent Failures into Selective Self-Correction | 先诊断主导失败模式再裁剪恢复干预，自纠错成功率从 39% 提到 90% / Diagnoses failure modes then prunes recovery, lifting self-correction success from 39% to 90%. |
| [[2608.11888]] | Agent Skills Can Be Harmful: An Empirical Study of Skill-Induced Failures | 差分测试挖出 307 例技能诱导失败，"看似相关却误导"的技能最易致功能故障 / Differential testing mines 307 skill-induced failures; on-topic misleading skills cause most faults. |
| [[2608.11924]] | Spark-to-Paper: End-to-End Research Paper Generation as a Composable Skill | 把"想法到论文"实现为 13 个可组合技能，引用有效性 99.5%、捏造检测 14%→92% / Idea-to-paper as 13 composable skills, 99.5% citation validity, fabrication detection 14%→92%. |
| [[2608.11977]] | Retry, Switch, or Abstain? Learning Strategy-Aware Tool-Use Policies via Controlled Error Injection | 注入可控工具失败并配课程 RL，Retail 任务鲁棒性提升多达 16.8pp / Injects controllable tool failures plus curriculum RL, lifting robustness up to 16.8pp on Retail. |
| [[2608.12307]] | AI4AI at Test-Time: Strong-to-Weak Capability Transfer via Harnesses | 强模型自动为弱模型构建推理期脚手架，心智理论准确率 0.49→0.91 / A strong model auto-builds inference-time harnesses for a weak one, lifting ToM accuracy 0.49→0.91. |

### D. 可解释性与机制理解 / Interpretability & Mechanistic Understanding

| Paper | Title | 描述 / Description |
|-------|-------|--------------------|
| [[2608.11583]] | Localizing Safety Alignment: MLP Layers and Mid-Network Blocks Encode Refusal Behavior | 拒答主要由中层(8–11 层)MLP 权重承载，子集组合非加性地优于全量移植 / Refusal is carried by mid-layer (8–11) MLP weights; non-additive subsets beat full transplant. |
| [[2608.11735]] | Locating and Controlling Implicit Personalization in Large Language Models | 隐式人口线索的刻板偏移可定位到残差流方向(r 达 0.87)，投影消融可选择性抑制 / Stereotyped shifts localize to residual-stream directions (r up to 0.87), suppressible by projection. |
| [[2608.11767]] | Causal Structure is Inducible but Functionally Decoupled | 类型监督诱导槽位路由组织，但与读出锐利解耦，编辑状态不影响输出 / Type supervision induces routing but it is decoupled from readout—editing state doesn't affect output. |
| [[2608.11797]] | Orientation, not magnitude: the causal structure of task-vector interference in merged LLMs | 合并干扰由传播方向而非大小承载，指令模板在输出端淹没干扰约 20 倍 / Merging interference is directional, not magnitude; instruction templates bury it ~20× at output. |
| [[2608.11822]] | Located but not Releasable: Silent Gate Inversion and Bounded Linear Release | 定位成功(恢复 89%)但"释放"双重失败：OOD 检测零触发、线性释放被有界饱和 / Localization succeeds (89%) but release fails twice: OOD detector never fires, release bounded. |
| [[2608.12036]] | Mechanist: AI as a Scientific Instrument for Discovering the Mechanisms of Intelligence | 多智能体系统自主发现机制，复现超 Claude Code/AI Scientist 并发现跨模态安全风险 / Multi-agent system autonomously discovers mechanisms, beating baselines and finding a cross-modal risk. |
| [[2608.12149]] | Massive Activations in Hybrid Linear Attention LLMs: Pre-Attention Spikes and Inter-Spike Plateaus | 首次刻画混合线性注意力中前注意力尖峰与峰间高原，提出统一生命周期 / First characterizes pre-attention spikes & inter-spike plateaus, with a unified outlier lifecycle. |
| [[2608.12155]] | Understanding Why Foundation Models Work for Diffusion-Generated Image Detection | 视觉基础模型靠低-中频分布性差异检测扩散图，跨生成器 AUC 达 99.5 / Vision FMs detect diffusion images via low-mid frequency gaps, reaching 99.5 cross-generator AUC. |

### E. 评测与基准 / Evaluation & Benchmarks

| Paper | Title | 描述 / Description |
|-------|-------|--------------------|
| [[2608.11584]] | EnterpriseRAG: Benchmarking LLM Instruction Adherence and Robustness under Non-Ideal Retrieval | 六领域 983 样本基准揭示 57pp 编排断层(整体合规仅 26.8%)与知识交互瓶颈 / 983-instance benchmark revealing a 57pp orchestration gap (26.8% full compliance). |
| [[2608.11694]] | The Wording Effect: Quantifying Two-Way Drift in LLM Benchmark Performance | 保持题意的改写使准确率跨度达 74.7pp，漂移方向随模型变强而反转 / Meaning-preserving rewrites cause up to 74.7pp swings; drift direction reverses with strength. |
| [[2608.11727]] | Harness-IF: Evaluating Instruction Following Across Instruction Surfaces in Coding Agents | 首个规则级评估编码智能体多指令面的基准，反先验准确率揭示系统性高估 / First rule-level coding-agent instruction benchmark; against-prior accuracy reveals overestimation. |
| [[2608.11947]] | Accuracy and Order Sensitivity Diverge Under Label-Free Strategies | 去标签 MCQ 策略反降准确率(11/12 下降)，降低顺序敏感与提准确率相互解耦 / Label-free MCQ hurts accuracy (11/12 pairs); order-sensitivity decouples from accuracy. |
| [[2608.12097]] | Graph-Structured Rubrics: Compiling Rubrics into Typed Evaluation Graphs for LLM Judges | 把评分规则编译成类型化评估 DAG 确定性执行，逐点一致率提升 0.6–6.75pp / Compiles rubrics into a typed evaluation DAG, lifting exact agreement 0.6–6.75pp. |
| [[2608.12144]] | ADEPT: A Unified Framework for Deep Learning Test Adequacy | 统一深度学习测试充分性指标的开放框架，解决指标碎片化难复现对比的痛点 / Unifies fragmented DL test-adequacy metrics behind one framework for reproducible comparison. |
| [[2608.12150]] | Who Thinks Best Depends on How Long You Let Them: Budget-Dependent Rankings | LLM 排名随 token 预算剧烈翻转(56k 推理)，预算感知路由捕获 14.1% oracle 差距 / Rankings flip sharply with token budget (56k runs); budget-aware router captures 14.1% oracle gap. |
| [[2608.12197]] | NetlistBench: Evaluating LLM Reliability in SPICE Netlist Recognition and Manipulation | 结构等价校验的 SPICE 网表基准，多步复合编辑随步数从 ~80% 退化为 0% / Structure-verified SPICE benchmark; compound editing collapses from ~80% to 0% with more steps. |

### F. 量化、效率与硬件 / Quantization, Efficiency & Hardware

| Paper | Title | 描述 / Description |
|-------|-------|--------------------|
| [[2608.11533]] | Testing the EPYC Conjecture on Real Hardware: MoA-Guided Dense Matrix Multiplication | 按真实 512KB L2 推导块大小 M_C=256 后，EPYC 上 matmul 提升 30–59% / Recalibrating block M_C=256 from real 512KB L2 lifts matmul 30–59% on EPYC. |
| [[2608.11577]] | Uni-SFU: Algorithm-HW Co-Design for Universal SFUs via Mixed-Degree Piecewise Approximation | 混合阶分段多项式+RTL 面积模型统一六种激活函数硬件，仅 6800µm²、精度损<1.12% / Mixed-degree polynomials unify 6 activations in 6800µm² with <1.12% accuracy drop. |
| [[2608.11693]] | Spec Sheets Are Not Kernels: An ISA- and Source-Level Audit of INT8 on Blackwell Ultra | 四层审计证明 INT8 在 Blackwell Ultra(B300)默认不可部署，是全栈属性 / Four-layer audit shows INT8 undeployable by default on Blackwell Ultra—a full-stack problem. |
| [[2608.11786]] | Language-Conditional Dequantization: Recovering What Quantization Steals from Non-English Languages | 为量化模型挂按语言 rank-2 LoRA，恢复非英语 70–83% 困惑度差距、每语言仅 0.12% 参数 / Per-language rank-2 LoRA recovers 70–83% non-English perplexity gap at 0.12% params. |
| [[2608.11919]] | LazyTrain: Limited-resource Allocation toward Zero-waste Yield Optimization in LLM Training | 把检查点/放置/通信重叠统一为 MILP 调度，单卡训 Qwen3.6-27B 吞吐 1.24× / Unifies checkpoint/placement/overlap as MILP, lifting single-GPU Qwen3.6-27B throughput 1.24×. |
| [[2608.12026]] | SoftWater: Class-Aware Rate Allocation for Softmax Quantization | 把 softmax 头量化建模为率失真按类别分配比特，60 测试点赢 59 个、2-bit 省 45–60% 存储 / Reframes softmax quantization as rate-distortion, winning 59/60 cells, cutting 2-bit storage 45–60%. |
| [[2608.12140]] | FQTree: Fine-grained Quantization and Hardware Generation of Boosted Decision Trees | 按叶值幅度自适应分配比特的 BDT 量化训练+FPGA 生成，比 SOTA 省 26–57% LUT / Magnitude-adaptive BDT QAT plus FPGA generation cuts LUT 26–57% vs SOTA. |
| [[2608.12239]] | HAMP-LIC: Hessian-Aware Mixed-Precision PTQ for Learned Image Compression | 基于 Hessian 迹的混合精度 PTQ，4.85× 压缩仅 0.59% BD-rate 损耗并消除跨平台解码错误 / Hessian-trace mixed-precision PTQ: 4.85× compression at 0.59% BD-rate, no cross-platform errors. |
| [[2608.12259]] | Calibration Bets on the Past: PTQ for Financial Time-Series Forecasting | 金融时序 walk-forward 研究显示 W4A4 默认校准抹去 11–62% IC，百分位校准恢复 53–94% / Default W4A4 strips 11–62% of financial IC, recoverable 53–94% by percentile calibration. |

### G. 理论与基础 / Theory & Foundations

| Paper | Title | 描述 / Description |
|-------|-------|--------------------|
| [[2608.11657]] | Semantic Lenia: Emergence of Homeostatic Solitons Within the Semantic Space of LLMs | 把 Lenia 连续细胞自动机映射到 LLM logit 单纯形，生成稳定的自治语义孤子极限环 / Maps Lenia CA onto the LLM logit simplex, producing stable homeostatic-soliton limit cycles. |
| [[2608.11690]] | Drift and Dependence: Layer-wise Information-Theoretic Bounds for Replay-Based Continual Learning | 逐层信息论分解持续学习误差，梯度对齐 cos_H 与遗忘偏相关达 −0.948 / Layer-wise info-theoretic error decomposition; gradient alignment correlates with forgetting at −0.948. |
| [[2608.11859]] | Small-Scale Experiments: Are We There Yet? | 小模型经 256+ 次充分调参后 scaling law 即浮现，超参内禀维度随规模降至 1 / Scaling laws emerge at 4M params once tuned; intrinsic hyperparameter dim drops to 1 with scale. |
| [[2608.11909]] | Disentangling the Expressivity of RoPE | 分量周期型 RoPE 恰好识别 LTL[P,MOD]，常规非周期 RoPE 仅给有界局部性偏置 / Periodic RoPE recognizes exactly LTL[P,MOD]; non-periodic RoPE gives only a bounded locality bias. |

### H. 安全、对齐与可信 / Safety, Alignment & Trustworthiness

| Paper | Title | 描述 / Description |
|-------|-------|--------------------|
| [[2608.11705]] | Making Your LLMs More Objective: Stabilizing Safety Across Traits with TIST | 发现系统提示人设会翻转拒答决策，提出自蒸馏 trait 不变微调稳定跨人设安全 / Personas flip refusal; self-distillation trait-invariant tuning stabilizes safety across traits. |
| [[2608.11981]] | Benchmarking Trustworthiness of SLMs: Pre-trained vs. Compressed | 量化(尤其 GPTQ)比剪枝更保可信，量化大模型显著优于从头训练的小模型 / Quantization preserves trust better than pruning; quantized large models beat from-scratch SLMs. |
| [[2608.12273]] | Convergent Detour Hijacking: Task-Preserving Resource Amplification in Skill-Based Agents | 仅发布单个静态技能的供应链攻击，使 Agent token 增 66.9%、耗时增 92.5% 而不破坏任务 / Publisher-only supply-chain attack raising agent tokens 66.9% and time 92.5% without breaking tasks. |

---

## All Papers

| arXiv ID | Title | Topic | 一句话 / One-line |
|----------|-------|-------|-------------------|
| [[2608.11533]] | Testing the EPYC Conjecture on Real Hardware | F | 按真实 L2 推导块大小后 matmul 提升 30–59% / Block recalibration lifts matmul 30–59%. |
| [[2608.11552]] | Beyond Single-Turn Confidence: Trajectory-Adapted UQ for LLM Agents | C | 多轮智能体不确定性量化"有用但不均" / Multi-turn agent UQ is useful but uneven. |
| [[2608.11577]] | Uni-SFU: Algorithm-HW Co-Design for Universal SFUs | F | 混合阶多项式统一六种激活函数硬件 / Unify 6 activation-function hardware via mixed-degree polynomials. |
| [[2608.11583]] | Localizing Safety Alignment: MLP Layers Encode Refusal | D | 拒答主要由中层 MLP 权重承载 / Refusal is carried by mid-layer MLP weights. |
| [[2608.11584]] | EnterpriseRAG: LLM Robustness under Non-Ideal Retrieval | E | 揭示 57pp RAG 编排断层 / Reveals a 57pp enterprise-RAG orchestration gap. |
| [[2608.11632]] | Beyond Memory: A Transactional Continuity Kernel | C | 长生命周期智能体的激活契约控制平面 / Activation-contract control plane for long-lived agents. |
| [[2608.11654]] | Towards a Formal Definition of Agent Memory | C | 首个统一智能体记忆形式化框架 / First unified formal framework for agent memory. |
| [[2608.11657]] | Semantic Lenia: Homeostatic Solitons in LLM Semantic Space | G | LLM 语义空间中的稳定自治孤子极限环 / Stable homeostatic-soliton limit cycles in LLM semantic space. |
| [[2608.11669]] | Rubric Dropout: Mitigating Reward Hacking | A | 随机丢弃评分准则缓解 RL 奖励黑客 / Random rubric dropout mitigates RL reward hacking. |
| [[2608.11674]] | GCPO: Constraining Subspace Geometry in Rollout RL | A | 正交投影约束使 RL 稳定且防能力崩溃 / Orthogonal projection stabilizes RL and prevents capability collapse. |
| [[2608.11690]] | Drift and Dependence: Info-Theoretic Bounds for Continual Learning | G | 逐层信息论分解持续学习泛化误差 / Layer-wise info-theoretic decomposition of continual-learning error. |
| [[2608.11693]] | Spec Sheets Are Not Kernels: INT8 on Blackwell Ultra | F | INT8 在 B300 默认不可部署的全栈审计 / Full-stack audit: INT8 undeployable by default on B300. |
| [[2608.11694]] | The Wording Effect: Two-Way Drift in Benchmarks | E | 题意改写致准确率跨度 74.7pp / Rewrites cause 74.7pp accuracy swings. |
| [[2608.11698]] | REOPD: Reliability-Adaptive Reward Extrapolation for Distillation | A | token 级自适应系数的无 verifier 蒸馏 / Token-level adaptive distillation without a verifier. |
| [[2608.11705]] | Making LLMs More Objective: Trait-Invariant Safety Tuning | H | 自蒸馏 trait 不变微调稳定安全行为 / Self-distillation trait-invariant tuning stabilizes safety. |
| [[2608.11727]] | Harness-IF: Instruction Following in Coding Agents | E | 规则级编码智能体指令遵循基准 / Rule-level coding-agent instruction-following benchmark. |
| [[2608.11735]] | Locating and Controlling Implicit Personalization | D | 隐式人口线索偏移可定位与抑制 / Implicit-cue personalization localized and suppressible. |
| [[2608.11758]] | AWARe: Mitigating Catastrophic Forgetting | A | 按显著度冻结 30% 参数缓解遗忘 / Saliency-based 30% freeze mitigates forgetting. |
| [[2608.11767]] | Causal Structure is Inducible but Functionally Decoupled | D | 类型监督诱导结构但与读出解耦 / Type supervision induces structure decoupled from readout. |
| [[2608.11772]] | Diagnosis Before Recovery: Selective Self-Correction | C | 诊断失败模式后自纠错 39%→90% / Diagnose-then-recover lifts self-correction 39%→90%. |
| [[2608.11786]] | Language-Conditional Dequantization | F | 按语言 LoRA 恢复量化非英语损失 / Per-language LoRA recovers quantization's non-English loss. |
| [[2608.11797]] | Orientation, not magnitude: task-vector interference | D | 合并干扰由方向而非大小承载 / Merging interference is directional, not magnitude. |
| [[2608.11822]] | Located but not Releasable: Silent Gate Inversion | D | 定位成功但释放双重失败 / Localization succeeds but release fails twice. |
| [[2608.11829]] | On-Policy Distillation Through Test-Time Scaling | A | 在策略蒸馏只是"虚假蒸馏" / On-policy distillation is "illusory." |
| [[2608.11859]] | Small-Scale Experiments: Are We There Yet? | G | 充分调参后小模型 scaling law 即浮现 / Scaling laws emerge at small scale once tuned. |
| [[2608.11888]] | Agent Skills Can Be Harmful | C | 挖出 307 例技能诱导 Agent 失败 / Mines 307 skill-induced agent failures. |
| [[2608.11909]] | Disentangling the Expressivity of RoPE | G | 周期 vs 非周期 RoPE 的表达力分离 / Split between periodic and non-periodic RoPE expressivity. |
| [[2608.11919]] | LazyTrain: Zero-waste Yield Optimization in LLM Training | F | MILP 调度使单卡训练吞吐 1.24× / MILP scheduling lifts single-GPU throughput 1.24×. |
| [[2608.11924]] | Spark-to-Paper: End-to-End Paper Generation | C | 13 技能端到端生论文，引用有效 99.5% / 13-skill idea-to-paper with 99.5% citation validity. |
| [[2608.11941]] | OEIS Open: Conjectures into Theorems | B | 解出 30% 开放 OEIS 猜想 / Solves 30% of open OEIS conjectures. |
| [[2608.11947]] | Accuracy and Order Sensitivity Diverge Under Label-Free Strategies | E | 去标签 MCQ 反降准确率 / Label-free MCQ hurts accuracy. |
| [[2608.11977]] | Retry, Switch, or Abstain? Tool-Use Robustness | C | 注入失败+课程 RL 提升工具鲁棒性 / Error injection + curriculum RL boosts tool robustness. |
| [[2608.11981]] | Benchmarking Trustworthiness of SLMs | H | 量化比剪枝更保可信 / Quantization preserves trust better than pruning. |
| [[2608.11994]] | Claim-Level Reliability Assessment for Test-Time Reasoning | B | claim 级证伪验证提效测试时推理 / Claim-level falsification boosts test-time reasoning. |
| [[2608.12008]] | Asymptotic Risk Calibration for Selective QA | B | 事后阈值校准控制接受错误率 / Post-hoc calibration controls accepted-answer error. |
| [[2608.12026]] | SoftWater: Class-Aware Rate Allocation for Softmax Quantization | F | 率失真 softmax 头量化省 45–60% 存储 / Rate-distortion softmax quantization cuts storage 45–60%. |
| [[2608.12036]] | Mechanist: AI for Discovering Mechanisms of Intelligence | D | 多智能体自主发现可解释性机制 / Multi-agent system autonomously discovers mechanisms. |
| [[2608.12097]] | Graph-Structured Rubrics for LLM Judges | E | 类型化评估图提升裁判一致率 / Typed evaluation graphs lift judge agreement. |
| [[2608.12100]] | Confidence Calibration of Deep Learning Systems | B | 系统解决噪声/隐私/漂移下校准的博士论文 / Ph.D. thesis on calibration under noise/privacy/shift. |
| [[2608.12140]] | FQTree: Quantization and HW Generation of BDTs | F | BDT 量化训练+FPGA 生成省 26–57% LUT / BDT QAT + FPGA generation cuts LUT 26–57%. |
| [[2608.12144]] | ADEPT: A Unified Framework for DL Test Adequacy | E | 统一深度学习测试充分性指标 / Unifies DL test-adequacy metrics. |
| [[2608.12149]] | Massive Activations in Hybrid Linear Attention LLMs | D | 刻画混合注意力中巨型激活两种形态 / Characterizes two massive-activation forms in hybrid attention. |
| [[2608.12150]] | Who Thinks Best Depends on How Long You Let Them | E | LLM 排名随 token 预算翻转 / Rankings flip with token budget. |
| [[2608.12155]] | Why Foundation Models Work for Diffusion Image Detection | D | 基础模型靠低中频差异检测扩散图 / FMs detect diffusion images via low-mid frequency gaps. |
| [[2608.12197]] | NetlistBench: LLM Reliability in SPICE Netlist Editing | E | 网表多步编辑随步数退化为 0% / Netlist compound editing collapses to 0% with steps. |
| [[2608.12218]] | Information Abundance Paradox: Long-Context Training | A | 长上下文训练损害参数化知识 / Long-context training undermines parametric knowledge. |
| [[2608.12239]] | HAMP-LIC: Hessian-Aware Mixed-Precision PTQ | F | Hessian 混合精度 PTQ 仅 0.59% 损耗 / Hessian mixed-precision PTQ at 0.59% loss. |
| [[2608.12259]] | Calibration Bets on the Past: PTQ for Finance | F | 金融 W4A4 校准研究 / Study of W4A4 calibration for financial forecasting. |
| [[2608.12273]] | Convergent Detour Hijacking in Skill-Based Agents | H | 静态技能供应链攻击增耗不破任务 / Static-skill supply-chain attack raises cost without breaking tasks. |
| [[2608.12307]] | AI4AI at Test-Time: Strong-to-Weak via Harnesses | C | 强模型为弱模型建脚手架 0.49→0.91 / Strong model builds harnesses lifting weak model 0.49→0.91. |

---

> **Topic key / 主题索引:** A = LLM 训练、强化学习与蒸馏 / Training, RL & Distillation · B = 推理、测试时计算与校准 / Reasoning, Test-Time & Calibration · C = 智能体与工具使用 / Agents & Tool Use · D = 可解释性与机制理解 / Interpretability & Mechanistic Understanding · E = 评测与基准 / Evaluation & Benchmarks · F = 量化、效率与硬件 / Quantization, Efficiency & Hardware · G = 理论与基础 / Theory & Foundations · H = 安全、对齐与可信 / Safety, Alignment & Trustworthiness
