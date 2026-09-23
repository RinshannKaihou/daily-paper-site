---
title: "arXiv Daily — 2026-08-07"
date: 2026-08-07
tags:
  - arxiv-daily
  - llm-agents
  - self-evolving-agents
  - interpretability
  - statistical-learning-theory
  - agent-safety
  - benchmarks
papers: 50
---

# arXiv Daily — 2026-08-07

> 本日共收录 **50** 篇论文，覆盖 LLM 智能体、自演化技能系统、可解释性、统计学习理论、智能体评测、安全与对齐、优化与量化、世界模型等多个方向。
> This issue covers **50** papers spanning LLM agents, self-evolving skill systems, interpretability, statistical learning theory, agent evaluation, safety & alignment, optimization & quantization, world models, and more.

---

## 今日必读 / Must Read Today

### 1. [[2608.05810]] — When Self-Evolution Backfires: Pre-Commit Gating against Skill Contamination in LLM Agents

> **推荐理由 / Why read:** 揭示自演化智能体在技能库越过临界规模后出现"能力-污染相变"——新增技能反而持续拉低性能，且事后删除有害技能仅能挽回约 17%。提出 Pre-Commit 门控，对任何自演化智能体系统都是必读的安全/可靠性警示。
> Reveals a "capability–contamination phase transition" once self-evolving agents' skill libraries pass a critical size, with post-hoc deletion recovering only ~17%. The proposed Pre-Commit gate is essential reading for anyone building self-evolving agent stacks.

### 2. [[2608.05490]] — Innovation-Residual Auditing of Autonomous Analysis Agents

> **推荐理由 / Why read:** 为"无标注、仅用成功轨迹训练"的自主数据分析 Agent 逐操作失败归因建立了完整统计理论，给出任意依赖下的错误控制与可识别性证明。理论 + 工程 + 基准三位一体，是 failure attribution 领域的奠基性工作。
> Establishes the complete statistical theory (localization, detection limits, error control, identifiability) for one-class, step-level failure attribution in autonomous agents. A foundational, theory-plus-practice contribution to failure attribution.

### 3. [[2608.06362]] — AV-AIVAT: 74x Cheaper Agent Evaluation with Certified Anytime-Valid Stopping

> **推荐理由 / Why read:** 将 AIVAT 方差缩减与置信序列结合，在不完美信息博弈评测中实现 74× 成本下降并保证 anytime-valid 终止。对所有需要评测高方差智能体的研究者和工程师都有立竿见影的实用价值。
> Combines AIVAT variance reduction with confidence sequences to cut imperfect-information-game agent evaluation cost by 74× with certified anytime-valid stopping. Immediately useful to anyone evaluating high-variance agents.

---

## 按主题分类 / Papers by Topic

### A. LLM 智能体：技能、记忆与自演化 / LLM Agents: Skills, Memory & Self-Evolution

| Paper | 中文要点 | English Highlight |
|-------|---------|-------------------|
| [[2608.05604]] SkillZip | 把技能库重构为节级过程子图，在保留契约前提下用 MotifZip 重写重复子图实现压缩 | Replaces whole-package retrieval with node-level procedural subgraphs; MotifZip rewrites repeats while preserving interface/dependency/verifier contracts |
| [[2608.05628]] SkillHEX | 用可证伪的失败假设生成稠密诊断证据，引导测试时按需技能演化 | Closed-loop test-time skill evolution driven by falsifiable failure hypotheses turned into executable tests |
| [[2608.05563]] PoisonedEvolution | 仅约 10% 占比的"看似正常"轨迹投毒即可劫持自演化技能系统的演化器 | ~10% of benign-looking trajectory poison is enough to hijack a self-evolving skill (SES) system's evolver |
| [[2608.05810]] Pre-Commit Gating | 发现技能库越过临界规模后的"能力-污染相变"，提出 Pre-Commit 门控 | Identifies capability–contamination phase transition; proposes pre-commit gating to keep self-evolution safe |
| [[2608.06153]] GSE | 用 Skill Relation Graph 联合演化技能间依赖/共用/冲突，聚类合并把局部 trace 抽象为全局可复用技能 | Skill Relation Graph co-evolves dependency/sharing/conflict relations; clustering abstracts local traces into globally reusable coding-agent skills |
| [[2608.05784]] Activity Frames | 零模型、确定性的屏幕活动流编译器，把一天原始活动压缩为可审计活动帧 | Zero-model deterministic compiler turning raw screen-activity streams into auditable Activity Frames for agent memory/replay |
| [[2608.05906]] MERIT | 免训练 Text-to-SQL 修复智能体，用"双极性"情景记忆按错误类型检索修复 | Training-free Text-to-SQL repair agent using bipolar episodic memory indexed by error type |
| [[2608.05778]] Playbook Transfer | 用统一"蒸馏-验证-迁移"协议研究冻结 prompt 侧 playbook 的跨域/跨模型/跨运行时可迁移性 | Unified distill-verify-transfer protocol measuring frozen prompt-side playbook transfer across domains/models/runtimes |

### B. 智能体调试、错误归因与可观测性 / Agent Debugging, Failure Attribution & Observability

| Paper | 中文要点 | English Highlight |
|-------|---------|-------------------|
| [[2608.05490]] Innovation-Residual Auditing | 为自主 Agent 逐操作失败归因建立完整统计理论：定位、检测极限、错误控制、可识别性 | Complete statistical theory for step-level failure attribution in autonomous agents via one-class innovation residuals |
| [[2608.06346]] TrajDebug | 三阶段"错误生命周期追踪"：历史压缩定位本地错误 + 证据约束触发器检测 + 状态化分类 | Three-stage error-lifecycle tracing that localizes, detects, and classifies critical errors in long-horizon trajectories |
| [[2608.05863]] WitCert | 为异构注意力记忆（稠密/潜在 KV、稀疏选择器、循环状态）提出带类型误差度量的运行时可观测性契约 | Typed-error observability contract for heterogeneous attention memory (dense/latent KV, sparse selectors, recurrent states) |
| [[2608.05797]] Ex-ante Difficulty | 在执行 rollout 前仅凭任务描述预测难度；用 IRT 拟合 17 个基准的难度作为目标 | Predicts LLM-agent task difficulty from description alone before any rollout, using IRT-fitted difficulty on 17 benchmarks |
| [[2608.06057]] ContextPollute-Bench | 揭示"历史误导劫持"失效模式（污染历史可翻转 32.1% 正确决策）并提出 Oracle-OPD | Exposes misleading-history hijack failure (32.1% decision flips) and proposes ContextPollute-Bench + Oracle-OPD |

### C. 智能体安全、防护与可信执行 / Agent Safety, Guardrails & Trusted Execution

| Paper | 中文要点 | English Highlight |
|-------|---------|-------------------|
| [[2608.05695]] DreamGuard | 用 GRU 循环动力学风险感知世界模型（RSSM）维护轨迹隐状态，Noisy-Or 融合即时危害与累积风险 | GRU-based risk-aware world model (RSSM) maintaining fixed-dim trajectory state; Noisy-Or fuses immediate + cumulative risk |
| [[2608.06130]] Zero-Trust MCP | 用 PKCS#11 硬件隔离密钥替换软件私钥，叠加 SAGA/Chist/RAV 栈实现零信任 MCP 签名 | Replaces software keys with PKCS#11 hardware-isolated keystores, with SAGA/Chist/RAV zero-trust enforcement stack |
| [[2608.05624]] AI Sycophancy | 形式化"偏好诱导立场反转谄媚"(PSRS) 检测任务；CAP 框架在 17 个 LLM 上收集 29 万余条带标签回复 | Formalizes preference-induced stance-reversal sycophancy detection; CAP collects 290k+ labeled responses across 17 LLMs |

### D. 智能体与 LLM 评测 / Agent & LLM Evaluation

| Paper | 中文要点 | English Highlight |
|-------|---------|-------------------|
| [[2608.05519]] EcoAgent-Bench | 首个把"预算约束下的工具/模型选择"作为任务本身的基准（304 任务）；引入经济一致性指标 min(Up, Save) | First benchmark where budget-constrained tool/model choice is the task itself (304 tasks); economic-consistency metric min(Up, Save) |
| [[2608.06144]] FinEvo-Bench | 金融专业工作流自演化智能体纵向评测基准：120 个真实案例、20 个业务场景、6 大金融领域 | Longitudinal benchmark for self-evolving agents in professional financial workflows: 120 cases, 20 scenarios, 6 sub-domains |
| [[2608.06329]] Benchmarking Benchmarks | 无需参考基准的对话智能体基准质量评估框架：从一致性、复杂度、策略覆盖度三维度评估 | Reference-free framework grading conversational-agent benchmarks on consistency, complexity, and policy coverage |
| [[2608.06362]] AV-AIVAT | AIVAT 方差缩减 + 置信序列，实现不完美信息博弈 74× 更便宜的 anytime-valid 终止评测 | AIVAT + confidence sequences yield 74× cheaper anytime-valid stopping for imperfect-information-game agent evaluation |
| [[2608.06202]] Unmeasured Benchmarks | 审计 ChatGPT 在 BBQ/SafetyBench 上聊天界面 vs API 的模态/检索/引用差距及其安全含义 | Audits ChatGPT chat-vs-API gaps in modality, search, and citations on BBQ/SafetyBench and the safety implications |
| [[2608.05726]] LLM-Judge Bias | 让 LLM 先生成随机数估计其数值偏好，再用反方向 logits 去偏项缓解 LLM-as-Judge 评分偏差 | Estimate latent number bias via RNG, then subtract counter-direction logits to debias LLM-as-a-Judge scoring |
| [[2608.06262]] Conditional Query Testing | 严格证明条件查询假设检验的可学习性与自适应界 | Proves learnability and adaptivity gap for hypothesis testing with conditional queries |

### E. 可解释性、机制与探测 / Interpretability, Mechanistic & Probing

| Paper | 中文要点 | English Highlight |
|-------|---------|-------------------|
| [[2608.05660]] Residual-Stream Errors | 三流检测器融合跨层位移 + 向量量化 region + 归一化 direction，单标记检测推理有效性 | Three-stream detector fusing cross-layer motion + VQ region + normalized direction for single-token validity detection |
| [[2608.05732]] CircuitSteer | 用 SAE 在多层间基于"特征共激活 + 解码器方向几何对齐"构建跨层特征流子电路并叠加稠密方向转向 | SAE-based cross-layer feature-flow subcircuits via co-activation + decoder-direction geometric alignment for steering |
| [[2608.05734]] Subliminal Learning | 证明 Subliminal Learning 由权重中的非语义噪声驱动，是对教师偏置的非语义蒸馏 | Shows Subliminal Learning is driven by non-semantic noise structure in weights — non-semantic distillation of teacher bias |
| [[2608.05741]] EchoPrompt | 免训练 LLM 生成文本检测器：用统一助手风格前缀恢复隐式响应上下文再比较 | Training-free detector restoring latent response context via a uniform assistant-style prefix, then comparing |
| [[2608.05889]] em-dash in Congress | 预注册研究：2021–2025 美国国会新闻稿中无空格破折号密度从 0.2 跃升至 1.3/千字符，疑为 LLM 介入 | Preregistered study: em-dash density in U.S. congressional press releases jumps from 0.2 to 1.3/1k chars (2021–2025), suggesting LLM use |

### F. 视觉-语言模型与多模态 / Vision-Language Models & Multimodal

| Paper | 中文要点 | English Highlight |
|-------|---------|-------------------|
| [[2608.05670]] RENDEQ | 通过重绘同一份数据生成语义等价、答案已知的图表集，把"一致性"与"正确性"的耦合变成可测量对象 | Render-equivalent chart sets make the agreement–accuracy coupling measurable for VLM chart QA |
| [[2608.05675]] Consistency Blind Spot | 用交换代数刻画一致性检测的可计算盲区；提出等变-一致性得分 REND-EQUIV | Commutation theory characterizes a computable blind spot in consistency checks; proposes equivariance-consistency score |
| [[2608.06270]] Illusion of Visual Tool-Use | 用 Pearl 因果图审计"以图思考"：观察中介路径贡献微小，动作捷径路径占主导，视觉工具多为假象 | Pearl-style causal audit of "thinking with images": action-shortcut path dominates, observation-mediation is negligible — visual tool-use is largely illusory |
| [[2608.05948]] GAUGE | 基于真实动捕数据的物理保真度评测基准（22 类任务、~1,560 实测轨迹），评 Isaac Sim/Genesis/Newton 与 6 个图生视频世界模型 | Motion-capture-grounded physical-fidelity benchmark (22 tasks, ~1,560 real trajectories) grading sim engines and video world models |

### G. 后训练、RL、优化与量化 / Post-Training, RL, Optimization & Quantization

| Paper | 中文要点 | English Highlight |
|-------|---------|-------------------|
| [[2608.05600]] LC-GRPO | 解决 flow-based GRPO 中"训练 SDE / 推理 ODE"不一致：每 rollout 步先做 ODE Euler 推进再加 Langevin 校正 | Bridges train (SDE) vs inference (ODE) gap in flow-based GRPO with per-rollout ODE Euler step + Langevin correction |
| [[2608.05499]] APQF | 五个协作 LLM 智能体在逐层敏感度证据下自动完成结构化剪枝 + 混合精度 QAT + 精度恢复 | Five cooperative LLM agents drive profiling-grounded structured pruning + mixed-precision QAT + accuracy recovery |
| [[2608.06291]] BaKron | 把反并行化 + 递归分治结合进向量化 GPTQ 求解器，将 Kronecker-Hessian 量化复杂度从 O(m²n²) 降到更低 | Combines anti-parallelization + recursive divide-and-conquer to cut Kronecker-Hessian GPTQ complexity below O(m²n²) |
| [[2608.06218]] Skewon | 证明 Muon 在 Stiefel 流形上的线性最小化子有精确闭式解（skew(MX^T) 的矩阵符号函数），提出 Skewon 算法 | Muon's Stiefel-manifold linear-minimization oracle has an exact closed form; yields the Skewon optimizer |
| [[2608.06246]] Post-Training Taxonomy | 用 Multivocal 综述提出六维（机制/目标/数据/持久性/范围/模型类型）分类法，覆盖 48 种训练后适配技术 | Multivocal review proposing a six-dimensional taxonomy covering 48 post-training adaptation techniques for AI governance |
| [[2608.06283]] SG-TULA | 提出 SG-TULA：直接作用于次梯度、用 taming 稳定超线性漂移的 Langevin 离散，首次在非光滑+超线性+非凸同时成立下收敛 | SG-TULA tames subgradient-driven superlinear drift, first convergence guarantee under joint non-smooth + superlinear-growth + non-convex |

### H. 训练系统、基础设施与协同优化 / Training Systems, Infra & Co-Optimization

| Paper | 中文要点 | English Highlight |
|-------|---------|-------------------|
| [[2608.05944]] B300 FSDP Field Report | 16×NVIDIA B300 双节点 FSDP/ZeRO-3 全参微调 Qwen3-32B 的坦诚工程现场报告（功耗/通信/配置四类实操产物） | Candid 2-node 16×B300 FSDP/ZeRO-3 full fine-tune of Qwen3-32B field report with telemetry, negative results, and hardening |
| [[2608.06046]] ML-for-ML | 提出把网络侧旋钮（梯度压缩精度）与 ML 侧旋钮（梯度累积/批大小）放入同一"到达目标 loss 时间"目标进行跨层协同优化（vision） | Co-optimize network knobs (gradient compression) and ML knobs (batch size) under a single time-to-target-loss objective (vision paper) |

### I. 学习理论、统计与不确定性 / Learning Theory, Statistics & Uncertainty

| Paper | 中文要点 | English Highlight |
|-------|---------|-------------------|
| [[2608.06206]] Localized Conformal | 为随机局部化保形预测（RLCP）给出有限样本高概率联合保证：条件覆盖误差与得分锐度的联合控制 | Finite-sample high-probability joint guarantees for RLCP controlling conditional coverage error and score sharpness |
| [[2608.06155]] CEO Regularity | 证明条件期望算子有界性/Hilbert–Schmidt 性质可由 RN 密度的 η ∈ L²(ν_Y; H) 正则性直接推出 | Verifiable criterion: boundedness / Hilbert–Schmidt of conditional expectation operators follows from RN density regularity |
| [[2608.06182]] SEG vs I-SEG | 系统比较单调变分不等式上同样本 S-SEG 与独立样本 I-SEG 两种 extragradient 采样变体的收敛性与高概率 gap 界 | Systematic comparison of same-sample vs independent-sample stochastic extragradient for monotone VIs with high-probability gap bounds |
| [[2608.06250]] Early-Stopped GD | 在协方差谱快速连续衰减时，oracle 时间提前停止的逻辑回归梯度下降对带标签翻转噪声的高斯混合分类达到极小极大最优 | Early-stopped logistic-regression GD is minimax optimal for Gaussian-mixture classification with label noise under fast-decaying spectra |
| [[2608.06337]] Monotone Adversary | 证明在单调对手模型下 VC 维 d≥2 二分类的最优期望误差率为 Θ((d/n)·log(n/d))，含对数损失 | Optimal expected-error rate under monotone adversaries is Θ((d/n)·log(n/d)) for VC dimension d≥2, including logarithmic loss |
| [[2608.06363]] Optimal Agnostic PAC | 构造确定性 improper PAC 学习器，在 VC 维 d 的任意二元假设类上达到与 Devroye-Györfi-Lugosi 下界匹配的最优超额风险 | Deterministic improper PAC learner achieving the Devroye-Györfi-Lugosi lower-bound-matching optimal excess risk on any VC-d class |
| [[2608.05995]] Posterior Risk | 把不确定性统一为"样本条件逐点后验风险"，在 14 个真实协变量 GP 基准上提供超越代理指标的评价 | Unifies uncertainty as sample-conditional pointwise posterior risk, evaluated on 14 real-covariate GP benchmarks beyond proxies |
| [[2608.06004]] TFM Self-Agreement | 提出并验证表格基础模型的边际化一致性与因子分解一致性两条准则，证明所有 SOTA TFM 均违反 | Proposes and validates marginalization + factorization consistency criteria; shows all SOTA tabular foundation models violate them |

### J. 事实性、幻觉与 NLP / Factuality, Hallucination & NLP

| Paper | 中文要点 | English Highlight |
|-------|---------|-------------------|
| [[2608.05823]] HallDetect | 原子命题分解 + 对比式多尺度 NLI 验证的轻量、黑盒、无参考幻觉检测；4-bit 量化消费级 GPU 上达标 | Atomic-proposition decomposition + contrastive multi-scale NLI for lightweight black-box reference-free hallucination detection |

### K. 量子计算 / Quantum Computing

| Paper | 中文要点 | English Highlight |
|-------|---------|-------------------|
| [[2608.05686]] Self-Calibrating FT | 证明随机化编译后探测器事件率构成局部强凸标定目标；用零阶在线优化 SPSA/LSPSI 无需噪声模型即可自校准量子纠错 | Proves randomized-compiled detection rates are locally strongly convex; SPSA/LSPSA zeroth-order online optimization self-calibrates quantum error correction without noise models |

---

## All Papers

| # | Link | Title (Short) | 中文一句话 | English TL;DR |
|---|------|---------------|-----------|---------------|
| 1 | [[2608.05490]] | Innovation-Residual Auditing | 自主 Agent 逐操作失败归因的完整统计理论 | Complete statistical theory for one-class step-level failure attribution in autonomous agents |
| 2 | [[2608.05499]] | APQF | 五个协作 LLM 智能体驱动结构化剪枝 + 混合精度量化 + 精度恢复 | Five cooperative LLM agents drive profiling-grounded pruning + mixed-precision QAT |
| 3 | [[2608.05519]] | EcoAgent-Bench | 首个把预算约束下工具/模型选择作为任务的 agent 基准 | First benchmark where budget-constrained tool/model choice is the task |
| 4 | [[2608.05563]] | PoisonedEvolution | ~10% 轨迹投毒即可劫持自演化技能系统 | ~10% trajectory poison hijacks self-evolving skill systems |
| 5 | [[2608.05600]] | LC-GRPO | 解决 flow-based GRPO 训练 SDE/推理 ODE 不一致 | Bridges train/inference gap in flow-based GRPO via Langevin correction |
| 6 | [[2608.05604]] | SkillZip | 节级过程子图 + MotifZip 在保留契约下压缩技能库 | Node-level subgraphs + MotifZip compress skill libraries while preserving contracts |
| 7 | [[2608.05624]] | AI Sycophancy | 形式化偏好诱导立场反转谄媚检测（17 LLM、29 万样本） | Formalizes preference-induced stance-reversal sycophancy detection |
| 8 | [[2608.05628]] | SkillHEX | 可证伪失败假设驱动的测试时技能演化 | Test-time skill evolution driven by falsifiable failure hypotheses |
| 9 | [[2608.05660]] | Residual-Stream Errors | 三流检测器融合跨层位移+VQ region+方向的单标记推理有效性检测 | Three-stream single-token reasoning-validity detector |
| 10 | [[2608.05670]] | RENDEQ | 用语义等价重绘图表集把一致性-正确性耦合变为可测量对象 | Render-equivalent chart sets make agreement-accuracy coupling measurable |
| 11 | [[2608.05675]] | Consistency Blind Spot | 用交换代数刻画一致性检测的可计算盲区并提等变-一致性得分 | Commutation theory + equivariance-consistency score for VLM reliability |
| 12 | [[2608.05686]] | Self-Calibrating Quantum FT | 证明检测率构成局部强凸目标，零阶在线优化自校准量子纠错 | Zeroth-order online optimization self-calibrates quantum error correction |
| 13 | [[2608.05695]] | DreamGuard | GRU 世界模型 + Noisy-Or 融合的 LLM 智能体运行时防护栏 | GRU world model + Noisy-Or runtime guardrail for LLM agents |
| 14 | [[2608.05726]] | LLM-Judge Bias | 用随机数生成估计数值偏好并反方向去偏 | RNG-estimated latent number bias debiasing for LLM-as-Judge |
| 15 | [[2608.05732]] | CircuitSteer | SAE 构建跨层特征流子电路并几何对齐方向转向 | SAE cross-layer feature-flow subcircuits + geometrically aligned steering |
| 16 | [[2608.05734]] | Subliminal Learning | 证明 Subliminal Learning 是权重非语义噪声驱动的非语义蒸馏 | Subliminal Learning is non-semantic distillation via weight noise |
| 17 | [[2608.05741]] | EchoPrompt | 免训练 LLM 生成文本检测器：恢复隐式响应上下文再比较 | Training-free detector via latent prompt restoration |
| 18 | [[2608.05778]] | Playbook Transfer | 统一协议测量冻结 prompt playbook 的跨域/模型/运行时迁移 | Unified protocol measuring frozen playbook transfer |
| 19 | [[2608.05784]] | Activity Frames | 零模型确定性屏幕活动流编译为可审计活动帧 | Zero-model deterministic compilation of screen activity into auditable frames |
| 20 | [[2608.05797]] | Ex-ante Difficulty | 仅凭任务描述在 rollout 前预测智能体难度 | Predicts agent task difficulty from description before rollout |
| 21 | [[2608.05810]] | Pre-Commit Gating | 揭示技能库临界规模后的能力-污染相变，提 Pre-Commit 门控 | Capability-contamination phase transition; pre-commit gating defense |
| 22 | [[2608.05823]] | HallDetect | 原子命题分解 + 多尺度 NLI 的轻量黑盒幻觉检测 | Atomic decomposition + multi-scale NLI lightweight hallucination detection |
| 23 | [[2608.05863]] | WitCert | 异构注意力记忆的带类型误差度量运行时可观测性契约 | Typed-error observability contract for heterogeneous attention memory |
| 24 | [[2608.05889]] | em-dash in Congress | 预注册研究：国会新闻稿破折号密度 4 年内从 0.2 升至 1.3/千字符 | Preregistered study of em-dash rise in congressional press releases |
| 25 | [[2608.05906]] | MERIT | 免训练 Text-to-SQL 修复，双极性情景记忆按错误类型检索 | Training-free Text-to-SQL repair with bipolar episodic memory |
| 26 | [[2608.05944]] | B300 FSDP Report | 16×B300 双节点 Qwen3-32B 全参微调的工程现场报告 | Field report on 2-node 16×B300 full fine-tune of Qwen3-32B |
| 27 | [[2608.05948]] | GAUGE | 基于动捕数据的物理保真度基准，评仿真引擎与世界模型 | Motion-capture-grounded physical-fidelity benchmark for sim engines and world models |
| 28 | [[2608.05995]] | Posterior Risk | 把不确定性统一为样本条件逐点后验风险 | Unifies uncertainty as sample-conditional pointwise posterior risk |
| 29 | [[2608.06004]] | TFM Agreement | 两条自洽性准则揭示所有 SOTA 表格基础模型不自洽 | Two consistency criteria show all SOTA tabular FMs are incoherent |
| 30 | [[2608.06046]] | ML-for-ML | 把网络侧与 ML 侧旋钮放入同一 time-to-loss 目标协同优化 | Co-optimize network + ML knobs under time-to-target-loss (vision) |
| 31 | [[2608.06057]] | ContextPollute-Bench | 多轮工具调用中历史误导可翻转 32.1% 正确决策 | Misleading history flips 32.1% of correct tool-use decisions |
| 32 | [[2608.06130]] | Zero-Trust MCP | 用 PKCS#11 硬件密钥 + SAGA/Chist/RAV 栈实现零信任 MCP 签名 | PKCS#11 hardware keystores + SAGA/Chist/RAV zero-trust MCP enforcement |
| 33 | [[2608.06144]] | FinEvo-Bench | 金融专业工作流自演化智能体纵向评测基准 | Longitudinal benchmark for self-evolving agents in finance |
| 34 | [[2608.06153]] | GSE | Skill Relation Graph 把局部 trace 抽象为全局可复用技能 | Skill Relation Graph abstracts local traces into globally reusable skills |
| 35 | [[2608.06155]] | CEO Regularity | 条件期望算子有界性可由 RN 密度正则性直接推出 | Verifiable regularity criterion for conditional expectation operators |
| 36 | [[2608.06182]] | SEG vs I-SEG | 系统比较单调 VI 上两种 extragradient 采样变体的收敛性 | Systematic comparison of SEG sampling variants for monotone VIs |
| 37 | [[2608.06202]] | Unmeasured Benchmarks | 审计 ChatGPT 聊天界面 vs API 的模态/检索/引用差距及安全含义 | Audits ChatGPT chat-vs-API modality/search/citation gaps |
| 38 | [[2608.06206]] | Localized Conformal | 为 RLCP 给出有限样本高概率联合覆盖保证 | Finite-sample joint guarantees for localized conformal prediction |
| 39 | [[2608.06218]] | Skewon | 证明 Muon 在 Stiefel 流形上存在精确闭式更新 | Muon admits exact closed-form update on the Stiefel manifold |
| 40 | [[2608.06246]] | Post-Training Taxonomy | 六维分类法覆盖 48 种训练后适配技术 | Six-dimensional taxonomy covering 48 post-training techniques |
| 41 | [[2608.06250]] | Early-Stopped GD | 高斯混合+标签噪声下 oracle 提前停止 GD 达极小极大最优 | Early-stopped GD minimax-optimal for Gaussian mixture with label noise |
| 42 | [[2608.06262]] | Conditional Queries | 条件查询假设检验的可学习性与自适应界 | Learnability and adaptivity gap for hypothesis testing with conditional queries |
| 43 | [[2608.06270]] | Illusion Visual Tool-Use | 因果审计揭示"以图思考"中动作捷径主导、观察中介微弱 | Causal audit: action-shortcut dominates, visual tool-use is illusory |
| 44 | [[2608.06283]] | SG-TULA | 非光滑+超线性+非凸同时成立下收敛的次梯度 Langevin | Subgradient Langevin converging under joint non-smooth + superlinear + non-convex |
| 45 | [[2608.06291]] | BaKron | 反并行化+递归分治降低 Kronecker-Hessian GPTQ 复杂度 | Anti-parallelization + recursion cut Kronecker-Hessian GPTQ complexity |
| 46 | [[2608.06329]] | Benchmarking Benchmarks | 无需参考基准的对话智能体基准质量评估 | Reference-free framework for grading conversational-agent benchmarks |
| 47 | [[2608.06337]] | Monotone Adversary | 单调对手下 VC 维 d≥2 二分类最优误差率 Θ((d/n)·log(n/d)) | Optimal rate Θ((d/n)·log(n/d)) for learning with monotone adversaries |
| 48 | [[2608.06346]] | TrajDebug | 错误生命周期追踪：定位+检测+状态化分类长轨迹关键失败 | Error-lifecycle tracing for long-horizon agent trajectories |
| 49 | [[2608.06362]] | AV-AIVAT | AIVAT + 置信序列使不完美信息博弈评测成本降 74× | 74× cheaper anytime-valid agent evaluation in imperfect-info games |
| 50 | [[2608.06363]] | Optimal Agnostic PAC | 确定性 improper PAC 学习器匹配 Devroye-Györfi-Lugosi 下界 | Deterministic improper PAC learner matching the DGL lower bound |

---

<!-- COUNT_CHECK: All Papers table lists 50 entries; directory contains 50 .md files excluding overview.md. Counts match. -->
