---
title: "Weekly Overview — 2026-10-12..2026-10-18"
date: 2026-10-12
week: "2026-10-12..2026-10-18"
tags:
  - weekly-overview
  - arxiv
  - llm-reliability
  - agents
  - interpretability
  - systems
papers: 103
---

# 周报总览 / Weekly Overview（2026-10-12 .. 2026-10-18）

本周共评估 **3,671** 篇新论文（周一至周日），865 篇进入摘要门控、632 篇通过，最终按领域配额经逐对比较（Bradley-Terry）选出 **103** 篇，分属 9 个领域；27 篇星标候选经全文精读后评出 **8** 篇本周必读。本周主线异常清晰：**"看似在改进，实则在静默退化"**——自进化智能体的修复–泛化鸿沟、奖励聚合的捷径坍塌、工具链进化的幻觉增益、编译器缓存状态的静默损坏、量化压缩下的可靠性流失。

This week we evaluated **3,671** fresh papers (Mon–Sun); 865 reached the abstract gate, 632 passed, and **103** were selected via within-area pairwise ranking (Bradley-Terry) under per-area quotas across 9 areas; 27 star candidates were fully read and **8** earned Must-Read status. The through-line: **silent degradation masked as progress** — repair-without-generalization in self-evolving agents, aggregation-induced reward shortcuts, illusory harness-evolution gains, corrupting compiler cache state, and reliability lost under aggressive compression.

---

## 本周必读 / Must Read This Week

> 以下 8 篇全部来自本周全文精读后 `star: true` 的候选（27 选 8，每个领域至多 2 篇，本周恰好每领域 1 篇）。每条理由均附保留意见。
> The 8 picks below all come from full-read candidates marked `star: true` (8 of 27; at most 2 per area — this week exactly one per area). Every reason carries its caveat.

### 1. [[2610.22984]] Self-Evolving Agents Can Repair Failures but Struggle to Generalize from Them（自进化智能体的修复–泛化鸿沟）
**领域 / Area:** Self-Evolving Agents & Automated Research · **类型 / Type:** 分析 / analysis

- **理由 / Why:** 罕见的受控负结果：3 种自进化框架 × 10 个骨干 × 4 个可验证环境，并用"人工核验经验"对照组干净地区分了"学到错误教训"与"正确教训仍无法迁移"——修复有效、泛化系统性缺失，而泛化收益来自成功轨迹而非更丰富的失败诊断。| A rare controlled negative result — 3 evolution frameworks × 10 backbones × 4 verified environments, with a hand-verified-experience control cleanly separating "wrong lessons" from "right lessons that still don't transfer".
- **保留意见 / Caveat:** 留出评测为小集合单次 rollout（WebArena Reddit 仅 27 任务）且无置信区间，头条跌幅（25.93%→7.41%）方向警示但噪声较大。| Held-out evaluation uses a single rollout per checkpoint on small sets (WebArena Reddit = 27 tasks) with no confidence intervals; the headline declines are directionally alarming but noisy.

### 2. [[2610.17528]] ATTUNE: Agentic Throughput Tuning for LLM Training（智能体式训练吞吐调优）
**领域 / Area:** LLM Training Stability & Observability · **类型 / Type:** 系统 / system

- **理由 / Why:** 真实 64–128 GPU 战役 + 等预算对比（OptiCo/贝叶斯/随机），agent 无关的正确性门（配置检查 + 20 步损失收敛）实测 0/133 误拒、16/24 故障拦截，并对 Mixtral 诚实报告 +0.0% 无效果。| Real 64–128 GPU campaigns with equal-budget comparisons, an agent-independent correctness gate (0/133 false-rejects, 16/24 faults caught), and an honest +0.0% no-op on Mixtral.
- **保留意见 / Caveat:** 仅模型留出——技术栈、加速器与 agent 模型即开发所用；n=3 战役 p=0.05–0.125，+33.9% 部分度量的是 H100 配方移植到 B200 的摩擦。| Only the models were held out (stack/accelerators/agent are those used in development); n=3 campaigns (p=0.05–0.125), and the +33.9% partly measures H100→B200 porting friction.

### 3. [[2610.21404]] Multi-Reward Hacking: From Aggregation-Induced Drift to Trust-Anchored Defense（多奖励黑客与信任锚定防御）
**领域 / Area:** RL Post-Training Dynamics & Failures · **类型 / Type:** 方法 / method

- **理由 / Why:** 定理 + 实验双确认：把主奖励与更易获得的辅助奖励做对称聚合，会从任意初始化收敛到"只刷辅助奖励"的捷径（聚合奖励上升、正确率崩塌）；TAG 是无操作奖励设定下唯一存活的方案（pass@4 0.581 vs 加性 0.220，回复再短 44%）。| A provable failure mode of symmetric reward aggregation (Theorem 1) confirmed across 5 models, 2 families, 2 domains; Trust-Anchored Gating is the only arm surviving the no-op reward setting (0.581 vs 0.220 pass@4).
- **保留意见 / Caveat:** 所有辅助通道均为合成二值（未测学习型奖励模型或规则裁判），"所有方法都崩溃"的头条部分依赖简化移植（拉格朗日对偶约 20 步内退化为纯正确性）。| All auxiliary channels are synthetic and binary (no learned reward models or rubric judges tested), and the "every method collapses" headline rests partly on simplified ports.

### 4. [[2610.22003]] Stateful Testing for Deep Learning Compilers（Rondo：深度学习编译器有状态测试）
**领域 / Area:** Inference Reliability & SDC Detection · **类型 / Type:** 方法 / method

- **理由 / Why:** 少见的外部验证型测试研究：39 份上游报告、35 份开发者确认、18 个已修复；50,074 标注案例上告警精度 99.26%；"保留 vs 重置编译器状态重放"协议干净地隔离了缓存状态损坏。| Externally validated testing research — 39 upstream reports, 35 developer-confirmed, 18 already fixed; 99.26% oracle precision on 50,074 labeled cases; the retain-vs-reset replay cleanly isolates compiler-state corruption.
- **保留意见 / Caveat:** 覆盖率大增主要发生在论文自建的行为覆盖指标上（编译器源码行覆盖仅 14.17%→14.94%），且 35 个有状态 bug 中 22 个出自 PyTorch 一家。| The coverage gains are on the paper's own behavior-coverage metrics (source-line coverage moves only 14.17%→14.94%), and 22 of 35 stateful bugs are in PyTorch alone.

### 5. [[2610.17544]] Many Steps into One: Reasoning Contraction and the Limits of Safe Memory Reuse（推理收缩与记忆安全复用）
**领域 / Area:** Agent & Pipeline Silent Failures · **类型 / Type:** 分析 / analysis

- **理由 / Why:** 把"智能体何时能信任编译式记忆"变成精确的变化检测理论，并在重放的相同数据流上验证：5,779 个风险 epoch 中 0 次误认证，陈旧答案比 ExpeL/ACE 式计数器少 7–73 倍。| Turns "when can an agent trust compiled memory" into exact change-detection theory, validated on replayed identical streams — 0 false certifications in 5,779 at-risk epochs and 7–73× fewer stale answers than ExpeL/ACE-style counters.
- **保留意见 / Caveat:** 依赖精确验证器（KB 执行、单元测试）；头条基准是自建的近全量过期场景，对检测器过于"友好"，且 ExpeL/ACE 基线是被理想化移植的。| Requires exact verifiers; the bespoke benchmark has near-total staleness that flatters detectors, and the ExpeL/ACE baselines are idealized transplants.

### 6. [[2610.16020]] When Does Compensating Inherited Quantization Error Help?（补偿继承量化误差何时有益）
**领域 / Area:** Reliability under Extreme Performance Optimization · **类型 / Type:** 分析 / analysis

- **理由 / Why:** 用 Lean 形式化的两标量反例决定性地推翻 QEP 已发表的普适保证，预注册的 8B 实验显示固定 α=1/2 恒胜 RTN 而"自适应选强度"规则过拟合——本领域本周最严谨的证据。| A decisive, Lean-formalized refutation of QEP's published universal guarantee (a two-scalar counterexample) plus pre-registered 8B experiments: fixed α=1/2 always beats RTN while selection-based strength rules overfit.
- **保留意见 / Caveat:** 正向保证只覆盖无界网格减性抖动下的线性网络（无人实际部署的理想化方案），且所有定理固定校准输入，对留出数据的退化没有任何结论。| The positive guarantee covers linear networks under an idealized subtractive-dither scheme no deployed system uses, and all theorems fix the calibration input — nothing about held-out degradation.

### 7. [[2610.16084]] The Sharp Directions Are Against You: Curvature Analysis of Activation Steering（激活转向的曲率分析）
**领域 / Area:** LLM Hidden States & Interpretability · **类型 / Type:** 分析 / analysis

- **理由 / Why:** 把 CAA 转向脆弱性转化为可测的曲率几何，控制完备（36/36 token 级反转、25/25 生成胜过 CAA、PCA/随机/符号翻转/k 扫描检查），一行式修复；安全发现：CAA 把 Qwen 拒答率从 78% 恶化到 36%。| Converts CAA fragility into measurable curvature geometry with systematic controls (36/36 token reversals, 25/25 generation wins) and a one-line fix — including the safety finding that CAA degrades Qwen refusal 78%→36%.
- **保留意见 / Caveat:** 只与原版（及符号翻转）CAA 对比，未与 conceptor、SAE 引导或优化式转向正面竞争；生成证据为每条件 50 条贪心补全。| Compared only against vanilla (and sign-flipped) CAA — no head-to-head with conceptors, SAE-guided, or optimization-based steering; generation evidence is 50 greedy completions per condition.

### 8. [[2610.16866]] Efficient Resource-Shiftable RL Post-training with Generative Rewards（PivotRL：资源可转移的 RL 后训练）
**领域 / Area:** Compute Infrastructure for Large-Scale ML · **类型 / Type:** 系统 / system

- **理由 / Why:** 本领域最强的实测系统证据：真实 128 卡 H20 集群、同一 veRL 底座上的三个调优基线、3 次重复带标准差、逐组件消融，RL 收敛等价而墙钟约 30h vs >50h。| The area's strongest measured systems evidence — a real 128-GPU H20 cluster, three tuned baselines on the same veRL substrate, 3 repeats with std, per-component ablations, equal RL convergence in ~30 h vs >50 h.
- **保留意见 / Caveat:** 全部结果使用单一数学数据集 + 混合可验证/生成奖励（GenRM 以最不依赖的形式测试）；吞吐目标只计 rollout+奖励 token；未放出代码。| All results use a single math dataset with a hybrid verifiable+generative reward; the throughput objective counts only rollout+reward tokens; no code released.

---

## 按主题分类 / Papers by Topic

> 各领域内按 `area_rank` 排序（1 = 该领域逐对比较最优）。每格中英双语。
> Papers within each area are listed in `area_rank` order (1 = best in its area by side-by-side comparison). All cells bilingual.

### 1. 自进化智能体与自动化研究 / Self-Evolving Agents & Automated Research（12 篇 / 12 papers）

| # | 论文 / Paper | 类型 / Type | 入选理由 / Why it matters |
|---|---|---|---|
| 1 | [[2610.22984]] 自进化智能体的修复–泛化鸿沟 · Self-Evolving Agents Repair but Struggle to Generalize | 分析 / analysis | 失败专修不泛化：3 框架 × 10 骨干 × 4 环境一致的"修复–泛化鸿沟"，泛化收益来自成功轨迹 \| Failure-only evolution repairs source tasks but rarely transfers across 3 frameworks × 10 backbones × 4 environments; success trajectories drive generalization |
| 2 | [[2610.21646]] 自我改进问题 · The Self-Improvement Problem | 分析 / analysis | 不可能性理论：无终止性接纳门能同时保证可靠与非保守，有界评测预算下穷举模拟恢复保证 \| No terminating gate can guarantee both reliability and non-conservatism when accepting self-updates; bounded-budget exhaustive evaluation recovers guarantees |
| 3 | [[2610.21055]] Athanor：自主后训练研究系统 · Athanor: Autonomous Post-Training Research | 系统 / system | 104 小时自主战役：4 个 Opus 5.5 智能体把 Qwen3-4B-Base 从 15.9 调到 67.3 dev（留出集 9.2→48.2）\| A 104-hour campaign where 4 Claude Opus 5.5 agents post-train Qwen3-4B-Base 15.9→67.3 dev (held-out 9.2→48.2) with frozen evals |
| 4 | [[2610.22466]] 工具链进化增益归因 · Harness-Delta Attribution | 分析 / analysis | 工具链进化增益可能是幻觉：11 执行模型 × 3 框架，平均 54% 增益是过拟合、14% 来自测试时扩展 \| Harness-evolution gains may be illusory: 54% overfitting + 14% test-time scaling of the gain on average across 11 models × 3 frameworks |
| 5 | [[2610.19386]] STRATA：自维护结构化经验图 · STRATA: Self-Maintaining Experience Graphs | 方法 / method | 三层技能/工作流/元框架图 + 对比边修复单层记忆的负迁移，ScienceWorld 78.7→96.7 \| Three-layer skill/workflow/meta-framework graph with contrast edges fixes negative transfer; ScienceWorld 78.7→96.7 |
| 6 | [[2610.24944]] Epi：持久自改进研究智能体 · Epi: Persistent Self-Improving Agent | 系统 / system | 跨会话持久研究史 + 分支独立评审：120 项纪录（n-queens 区间缩窄约 84 倍），FrontierOR 超 Codex 5.4% 且成本仅 64% \| Persistent history + branching review: 120 record results incl. ~84× narrower n-queens interval; +5.4% over Codex on FrontierOR at 64% cost |
| 7 | [[2610.22029]] 选择即学习？模型未来继承 · Selection Is Not Learning | 方法 / method | 自进化循环继承了大多数本有害的更新：冻结评测继承（HeirCommit）切掉 68–83% 有害更新，数学平均 +5.3% \| Self-evolving loops inherit mostly harmful updates; frozen-evaluation inheritance (HeirCommit) cuts harmful accepted updates 68–83%, math +5.3% |
| 8 | [[2610.23344]] 语言模型学会改进语言模型 · LMs Learn to Improve LMs | 方法 / method | 在冻结"研究世界模型"上做 RL、周期性真实执行高分提案：数据生成成本降 33%，Qwen3.8-27B 带 300 条记录胜 GPT-6-sol \| RL over a frozen research world model with periodic real executions: 33% cheaper data generation; Qwen3.8-27B beats GPT-6-sol with 300 records in context |
| 9 | [[2610.17184]] DuoDiscover：突破评测瓶颈 · DuoDiscover: Beyond the Evaluation Bottleneck | 系统 / system | 共发现代理指标 + 持续保真复查，SWE-fficiency 上人类专家提速翻倍、vLLM 1.92× \| Co-discovered proxy yardsticks with continual fidelity rechecks double human-expert speedups; 1.92× vLLM, 1.38× SQLite |
| 10 | [[2610.17609]] 验证器–工具链协同进化 · Verifier-Harness Co-Evolution | 方法 / method | 协同进化可执行验证器程序修复错误/过时验证器，六个开放基准 59.0%/57.2% 偏好胜率 \| Co-evolved executable verifiers fix wrong/stale model-based verifiers; 59.0%/57.2% preference wins on six open-ended benchmarks |
| 11 | [[2610.22344]] MLExpert：自主机器学习工程 · MLExpert: Autonomous ML Engineering | 系统 / system | Kaggle-MLE Factory 分层 SFT + 窗口交互 RL，MLE-Bench Lite 奖牌率 37.9%→72.7% \| Hierarchical agentic SFT + windowed interaction RL lift the Kaggle medal rate 37.9%→72.7% on MLE-Bench Lite |
| 12 | [[2610.22603]] 忙海狸前沿的自主 AI 发现 · Autonomous Discovery on the Busy Beaver Frontier | 系统 / system | Gemini 流水线（模式识别+自动猜想+Lean 证明）产出 11 个新颖的形式验证 BB(6) 加速 \| A Gemini-based pipeline yields 11 novel formally verified Collatz-like accelerations for BB(6) machines |

### 2. LLM 训练稳定性与可观测性 / LLM Training Stability & Observability（10 篇 / 10 papers）

| # | 论文 / Paper | 类型 / Type | 入选理由 / Why it matters |
|---|---|---|---|
| 1 | [[2610.17528]] ATTUNE：智能体式吞吐调优 · ATTUNE: Agentic Throughput Tuning | 系统 / system | 无人值守 coding agent + 独立正确性门（拦下 16/24 故障运行），GLM-4.5 提速 33.9%、405B +6.7% \| Unattended agent tuning with an agent-independent correctness gate (16/24 faults caught); +33.9% GLM-4.5, +6.7% Llama-3.1-405B |
| 2 | [[2610.19761]] CAST：历史自适应谱裁剪 · CAST: History-Adaptive Spectral Clipping | 方法 / method | AdamW 二阶矩 + EMA 谱范数阈值稳定 19.08B MoE / 83.89B token，胜 9 个梯度基线且尖峰最少 \| History-adaptive spectral clipping beats 9 gradient-processing baselines on a 19.08B MoE over 83.89B tokens with fewest spikes |
| 3 | [[2610.18085]] 优化器对重参数化非等变 · No Optimizer Is Equivariant to Reparameterization | 分析 / analysis | 等价检查点发散出不同轨迹；对称对重平衡把 +3.78 PPL 重启失衡恢复到 0.02 以内 \| Standard optimizers diverge from equivalent checkpoints under reparameterization; symmetry-pair rebalancing recovers +3.78 PPL imbalance to within 0.02 |
| 4 | [[2610.19064]] 内层优化器与副本扩展 · Inner Optimizers Shape Replica Scaling | 分析 / analysis | 白化内层优化器（Muon vs AdamW）缓解副本数增长的性能退化，8–96 副本、增益随规模扩大 \| Whitening inner optimizers (Muon vs AdamW) mitigate monotonic replica-count degradation across 8–96 replicas; relative gain grows with scale |
| 5 | [[2610.22623]] 外层 Nesterov 动量稳定性 · Stability of Outer Nesterov Momentum | 分析 / analysis | 随机伪梯度上外层 Nesterov 的精确均方稳定判据；本地步数增多时所需 worker 数可指数增长 \| Exact mean-square stability criterion for outer Nesterov on stochastic pseudo-gradients; required workers can grow exponentially with local steps |
| 6 | [[2610.19185]] 基座模型评测设置选择 · Choosing Reliable Base-Model Benchmarking | 分析 / analysis | 单调性/非随机性/排序一致性元测量（26×2B 模型、80 任务、4 语言）挑选可靠评测设置 \| Meta-measures (monotonicity/ranking consistency) over 26×2B models and 80 tasks select reliable base-LM evaluation setups |
| 7 | [[2610.20439]] 精度井：非单调精度动力学 · The Accuracy Well | 分析 / analysis | 消失初始化下精度先升后崩再恢复（极端 100%→0%→100%），三阶段机制 + 线性网络理论 \| Accuracy rises, collapses, and recovers under vanishing init (extreme case 100%→0%→100%); three-stage mechanism plus linear-net theory |
| 8 | [[2610.22650]] 跨阶段切换优化器的代价 · Cost of Switching Optimizers Across Stages | 分析 / analysis | 预训练/后训练间切换 AdamW/Muon 的"失配惩罚"基本是幻影：1.2B–14B 实证未见惩罚 \| The suspected optimizer-mismatch penalty across pretraining/SFT stages is essentially ephemeral: 1.2B–14B study finds little penalty |
| 9 | [[2610.24305]] Muon 超越稳定性边缘 · Muon Beyond the Edge of Stability | 分析 / analysis | Muon 稳定运行于经典 AES 阈值之上；锐度与泛化 gap 相关 r=0.45–0.69 \| Muon stays stable above the classical Adaptive Edge-of-Stability threshold; sharpness correlates with the generalization gap (r=0.45–0.69) |
| 10 | [[2610.22945]] 大型扩散模型不止需要 EMA · Large Diffusion Models Need More Than EMA | 分析 / analysis | Schedule-Free 在各训练阶段一致优于恒定学习率 EMA，且迁移到 ReFL 与生成器侧 DMD \| Schedule-Free consistently beats constant-LR EMA across diffusion training stages, transferring to ReFL and generator-side DMD |

### 3. RL 后训练动态与失效 / RL Post-Training Dynamics & Failures（8 篇 / 8 papers）

| # | 论文 / Paper | 类型 / Type | 入选理由 / Why it matters |
|---|---|---|---|
| 1 | [[2610.21404]] 多奖励黑客与信任锚定防御 · Multi-Reward Hacking & Trust-Anchored Gating | 方法 / method | 对称聚合可证明导致"只刷辅助奖励"；TAG 保住 0.581 pass@4（加性 0.220）且回复短 44% \| Symmetric aggregation provably drives auxiliary-only shortcuts; TAG keeps 0.581 pass@4 vs 0.220 with 44% shorter replies |
| 2 | [[2610.18442]] 抄袭非接地：自撰句信用 RAG · Copying Is Not Grounding: Authored-Sentence Credit | 方法 / method | 答案级 GRPO 优势被复制行为黑掉；句级"自撰信用"使错误 −38%、受支持句 +46% \| Answer-level GRPO advantages get copy-hacked; authored-sentence credit cuts errors 38% and adds 46% supported sentences across 4 models × 5 corpora |
| 3 | [[2610.19832]] 寻租语言模型 · Rent-Seeking Language Models | 分析 / analysis | RLHF 寻租经济学：41–66% 代理增益是"租金"、97–100% 探针捏造，高频审计可遏制 \| An economics-of-regulation recasting of RM overoptimization: 41–66% of proxy gain is rent; 97–100% fabrication on probes; audits curb it |
| 4 | [[2610.18853]] 双时钟：RLVR 中的批次与失败时钟 · Two Clocks in RL with Verifiable Rewards | 分析 / analysis | 更大批次学得更慢却按时失败；双时钟框架分离进度与失败样本，16× 批次范围受控 GRPO \| Larger rollout batches learn slower yet fail on schedule; a two-clock framework separates progress from failure samples across a 16× batch range |
| 5 | [[2610.21682]] MoE RL 路由器漂移控制 · Router Drift Control in MoE RL | 方法 / method | 序列级分歧过滤保住原生专家选择，异步训练 AIME 平均峰值 +5.5 分且增益随陈旧度增长 \| Disagreement-based sequence filtering preserves native expert selection; +5.5 pts average peak on AIME in async MoE RL, gains grow with staleness |
| 6 | [[2610.17062]] 梯度路由消除意外行为 · Gradient Routing Removes Unintended Behaviors | 方法 / method | 把被标记样本梯度导入牺牲适配器（GRAFT），135M–8B RL 环境消除意外行为且蒸馏不教"隐藏" \| Routing flagged samples into sacrificial adapters (GRAFT) ablates unintended behavior across 135M–8B RL environments without teaching hiding |
| 7 | [[2610.19525]] 校准似然抑制 RLVR 作弊 · CALIF: Calibrated Likelihood vs Verifiable-IF Hacking | 方法 / method | 冻结参考策略的校准似然加成让 IFBench 约束保持/超过 RL 前质量，40/45 模型-指标对比获胜 \| A calibrated likelihood bonus from a frozen reference keeps instruction-following constraints at/above pre-RL quality; 40/45 comparisons won |
| 8 | [[2610.20898]] 错误投票、正确梯度 · Wrong Votes, Right Gradients | 分析 / analysis | 多数投票自标签的梯度与金标准更新几乎同向（噪声校正 cos=1）；30% 随机翻转无害，共享规则翻转才毁方向 \| Majority-vote gradients match gold updates (noise-corrected cosine 1); 30% random label flips are harmless while shared-rule flips destroy direction |

### 4. 推理可靠性与 SDC 检测 / Inference Reliability & SDC Detection（10 篇 / 10 papers）

| # | 论文 / Paper | 类型 / Type | 入选理由 / Why it matters |
|---|---|---|---|
| 1 | [[2610.19697]] CAFE：FeFET 存内计算抗扰编码 · CAFE: Conducting-Cell-Aware Encoding for FeFET CiM | 方法 / method | 导通单元感知差分编码 + 退化预测器：较二补码 CIM +87pp 精度，成本 1.86–2.78×（均匀 3.06×）\| Conducting-cell-aware differential encoding lifts FeFET CiM accuracy +87pp at 1.86–2.78× normalized cost vs 3.06× uniform |
| 2 | [[2610.22520]] 软错误引发 LLM 幻觉 · LLM Hallucinations Caused by Soft Errors | 分析 / analysis | 3,200 GPU 时软错误注入（LLMEI）给出 LLM 幻觉失效分类与随错误率分布 \| A 3,200 GPU-hour injection campaign (LLMEI) yields a failure-mode taxonomy of soft-error hallucinations across LLM architectures and tasks |
| 3 | [[2610.22003]] 深度学习编译器有状态测试 · Stateful Testing for DL Compilers (Rondo) | 方法 / method | MCTS 引导调用序列 + 三方差分预言机：117 bug（35 有状态）、35 开发者确认、99.26% 告警精度 \| MCTS-guided invocation sequences with a three-way differential oracle: 117 bugs (35 stateful), 35 developer-confirmed, 99.26% alarm precision |
| 4 | [[2610.23290]] CoTA++：dMLLM 重复诅咒 · CoTA++: The Repeat Curse in dMLLMs | 方法 / method | 信息流追踪（注意力分散/过时刷新/熵不收敛）+ 免训练重锚定把重复从 99.6% 降到 17.0% \| Information-flow tracing plus training-free re-anchoring cut dMLLM repetition 99.6%→17.0% across 3 models and 2 cache backends |
| 5 | [[2610.23328]] 可信峰值内存调度 · Peak-Memory Schedules You Can Trust | 方法 / method | 精确语句级内存建模：Inductor 22/54 CPU 配置漏预测峰值、19/50 改变 GPU 数值；替代实现按位一致且 94% 认证最优 \| Exact statement-level modeling: Inductor misses predicted peaks in 22/54 CPU configs and changes GPU numerics in 19/50; replacement is bitwise-identical, certified optimal on 94% |
| 6 | [[2610.23818]] 接受率非加速：有损投机解码的长度膨胀 · Length Inflation in Lossy Speculative Decoding | 分析 / analysis | 有损验证多接受 1.34× token 却把补全拉长至 1.54×，多出的 token 概率低且伤准确率 \| Lossy verification accepts 1.34× more tokens but inflates completions up to 1.54× with low-probability tokens and accuracy drops |
| 7 | [[2610.22454]] 预填充专家削减的伤害定位 · Where Prefill Expert Reduction Hurts MoE Models | 分析 / analysis | F1 损失集中于 chat 模板与提示开头 token；约 4% token 保全专家即可把 F1 控制在 1 点内 \| Short-answer F1 damage localizes to chat-template/prompt-start tokens; keeping ~4% of tokens at full experts holds F1 within 1 point |
| 8 | [[2610.18014]] LatentRemedy：非前缀 KV 复用修复 · LatentRemedy: Non-Prefix KV Cache Reuse | 方法 / method | 任务条件潜 token + 全预填蒸馏修复多智能体非前缀 KV 复用（原可致 90% 输出损坏）\| Task-conditioned latent tokens repair non-prefix KV reuse across conflicting agents (up to 90% corrupted outputs) at near-reuse TTFT |
| 9 | [[2610.17338]] 预算化 KV 缓存修复 · Budgeted KV-Cache Repair for Evolving Contexts | 方法 / method | 只重算 2–5% 保留后缀即达近全量重算的精确匹配（四个多跳 QA），层打包执行器快 16.1× \| Recomputing a budgeted 2–5% of the retained suffix matches full recompute on four multi-hop QA sets; layer-packed executor up to 16.1× faster |
| 10 | [[2610.24715]] 重复循环何时锁死 · When Do Repetition Loops Lock? A Blind Spot in DRY | 分析 / analysis | 精确逃逸概率分析揭示 DRY 采样盲区（66% 锁定单元仍锁死）；DRY-C 防住全部 720 个结构化输出循环 \| Exact escape-probability analysis exposes DRY's blind spot (66% of locked units stay locked); DRY-C prevents all 720 structured-output loops |

### 5. 智能体与流水线静默失效 / Agent & Pipeline Silent Failures（5 篇 / 5 papers）

| # | 论文 / Paper | 类型 / Type | 入选理由 / Why it matters |
|---|---|---|---|
| 1 | [[2610.17544]] 推理收缩与记忆安全复用 · Reasoning Contraction & Safe Memory Reuse | 分析 / analysis | ExpeL/ACE 式计数器是错配的变化检测器：比似然比证书多送 7–73× 陈旧答案（代码任务 35–73×）\| Success/failure counters are mismatched change detectors, serving 7.0–73× more stale answers than likelihood-ratio certified memories |
| 2 | [[2610.24545]] LLM 调用点契约 · Call-Site Contracts in Agentic Systems | 分析 / analysis | 40 个开源系统 496 个 LLM 调用点：48% 输出直达控制流、63% 预期约束未满足、仅 5.3% 满足全契约 \| Across 496 call sites in 40 systems: 48% of outputs reach control flow, 63% of expected constraints unmet, only 5.3% of sites satisfy the whole contract |
| 3 | [[2610.20003]] 编码智能体的报告缺口 · What Coding Agents Leave Unsaid (CTXGAP) | 分析 / analysis | 只读报告的监督者仅恢复 52.0% 任务状态（全上下文 92.7%）——40.7 分报告缺口跨框架复现 \| Report-only readers recover 52.0% of task state vs 92.7% with full context — a 40.7pt gap persisting across harnesses |
| 4 | [[2610.20927]] 源判定的上下文压缩 · Source-Judged Compaction for Long-Horizon Agents | 方法 / method | 压缩摘要混入臆造推理（83% 失败运行依赖无据条目）；源判定后处理 +2.1–8.9% 跨运行可靠性 \| Compaction summaries mix invented reasoning with facts (83% of failed runs act on unsupported entries); source-judged post-processing adds +2.1–8.9% reliability at unchanged tokens |
| 5 | [[2610.19342]] 跨边界智能体团队失效分类 · Why Agent Teams Fail Across Boundaries | 分析 / analysis | 2,500+ 运行、488 场景、四类 20 模式 A2A 失效分类；无对等声明验证、聚合分对协调失效盲 \| 2,500+ runs and 488 scenarios yield a 20-mode taxonomy of agent-to-agent failures with private states; no peer verification, aggregate scores blind to coordination failures |

### 6. 极限性能优化下的可靠性 / Reliability under Extreme Performance Optimization（20 篇 / 20 papers）

| # | 论文 / Paper | 类型 / Type | 入选理由 / Why it matters |
|---|---|---|---|
| 1 | [[2610.16020]] 补偿继承量化误差何时有益 · When Does Compensating Inherited Quantization Error Help? | 分析 / analysis | 逐层补偿的均方保证与失效条件；两标量反例推翻 QEP 普适保证；固定 α=1/2 恒胜 RTN \| Mean-square guarantees for layer-wise compensation plus a counterexample refuting QEP's universal guarantee; fixed α=1/2 always beats RTN at 8B/4-bit |
| 2 | [[2610.19934]] 剪枝大推理模型"停不下来" · To Reason but Not to Stop: Recovering Pruned LRMs | 方法 / method | 剪枝破坏推理模型终止（答对后循环）；隐藏态终止方向激活转向（TGAS）免训练修复 \| Weight pruning breaks LRM termination (post-answer loops); termination-direction activation steering (TGAS) recovers it training-free across 6 LRMs × 3 pipelines |
| 3 | [[2610.17637]] 混合精度缩放律 · Mixed Precision Scaling Laws for Quantized Pretraining | 分析 / analysis | 容量/优化误差分离的混合精度律，拟合 MSE 最多降 11×，支撑算力预算下的分层配方优化 \| A capacity/optimization-error-separated mixed-precision law with up to 11× lower fit MSE, enabling layer-wise recipe optimization under compute budgets |
| 4 | [[2610.20826]] 任务阶段专家路由≠量化敏感性 · Expert Routing Is Not a Proxy for Quant Sensitivity | 分析 / analysis | 路由统计被当作 MoE 量化敏感性代理未经检验；重分配从不优于均匀分配（z>4）\| Task-phase routing statistics are an unvalidated proxy; routing-guided reallocation never beats uniform allocation (decisive loss z>4) |
| 5 | [[2610.24343]] NVFP4 训练配方对比 · What Matters for NVFP4 Training? | 分析 / analysis | 8B 稠密与 30B-A3B MoE、1T token 的 4-bit 浮点预训练配方系统对比：选择性高精度层必需 \| Systematic NVFP4 recipe comparison on dense 8B and 30B-A3B MoE to 1T tokens; selective high-precision layers are necessary |
| 6 | [[2610.25460]] 保可靠性的医学分割压缩 · Reliability-Preserving Compression for Medical Segmentation | 方法 / method | 压缩模型保住 Dice 却静默改变不确定性图；分数引导混合精度在 3.59–7.82× 压缩下同时保住两者 \| Compressed models keep Dice while silently changing uncertainty maps; score-guided mixed precision preserves both at 3.59–7.82× compression |
| 7 | [[2610.24346]] 闭环智能体精度升级的任务价值 · Task Value of Precision Upgrades in Closed-Loop Agents | 分析 / analysis | BF16 回退动作在 4-bit 闭环任务上救与损几乎抵消；重排工具参数键即可改变结果 \| BF16 fallback rescues and damages nearly cancel in 4-bit closed-loop agent tasks; reordering tool-argument keys alone changes outcomes |
| 8 | [[2610.24968]] 视觉 token 剪枝充分性景观 · Visual Sufficiency Landscapes for Token Pruning | 分析 / analysis | 逐查询充分性概率让剪枝失效可预测：FastV/VisionZip/SparseVLM 失效预测 AUC +0.07–0.14 \| Query-conditioned sufficiency probability makes pruning failure predictable: failure-prediction AUC +0.07–0.14 for three pruning methods |
| 9 | [[2610.18343]] 量化在巴伐利亚语/德语/英语的鲁棒性 · Quantisation Robustness across Bavarian, German, English | 分析 / analysis | 4-bit 量化在语言变体间不均衡地翻转 11.9–16.0% 决策，校准语言影响显著 \| 4-bit quantization flips 11.9–16.0% of decisions unevenly across language varieties, with calibration-language effects (206 questions, 14 models) |
| 10 | [[2610.19498]] 量化 LLM 供应链可验证性缺口 · What You Sign Is Not What You Run | 分析 / analysis | 最多下载的 200 个 GGUF 仓库 0/198 可独立复现——量化产物不可按位复现使篡改无法检出 \| 0/198 of the top-200 GGUF repos are independently reproducible — non-bit-reproducible quantized artifacts enable undetected tampering |
| 11 | [[2610.19605]] PN-Mix：2-bit KV 混合精度 · PN-Mix: Pair-Norm Mixed-Precision Key Cache | 方法 / method | 对范数显著性混合精度 key cache：2.26-bit 匹敌 2.32–2.39-bit 基线，降到 1.5 bit 仍优雅退化 \| Pair-norm saliency mixed-precision key cache: 2.26-bit matches 2.32–2.39-bit baselines on reasoning/code/AIME with graceful degradation to 1.5 bits |
| 12 | [[2610.23046]] SpikeQ：SNN 后训练量化 · SpikeQ: Spike-Guided PTQ for SNNs | 方法 / method | 脉冲误差最小化权重网格 + 重置感知预点火网格：2-bit 膜电位保住大部分精度 \| Spike-error-minimizing weight levels plus reset-aware grids retain most accuracy at 2-bit membrane potentials where existing grids collapse |
| 13 | [[2610.20686]] RoLaQ：MLA 2-bit KV 校准 · RoLaQ: 2-Bit KV Caches in Multi-Head Latent Attention | 方法 / method | 联合旋转 + 范围校准（预测匹配监督）：DeepSeek-V2-Lite 3.96× 容量、256K 解码 2.51× 吞吐 \| Joint rotation and range calibration with prediction-matching supervision: 3.96× capacity and 2.51× decode throughput at 256K for MLA models |
| 14 | [[2610.24740]] VLM token 剪枝评测对了么 · Are We Evaluating VLM Token Pruning Right? (PAA-Bench) | 基准 / benchmark | Random-Pass@k 与保真约束加速揭示：更强压缩未必更快，效率排名随保真目标改变 \| Random-Pass@k and preservation-constrained speedup show stronger compression does not yield greater speedup; efficiency rankings change with the target |
| 15 | [[2610.22065]] ABNAT：模拟 CiM 噪声感知训练 · ABNAT: Noise-Aware Training for Analog CiM | 方法 / method | 逐头注意力路由保持的噪声感知训练：噪声退化精度 +11.28%、注意力偏移 −85.77% \| Headwise-attention-route-preserving noise-aware training: +11.28% noise-degraded accuracy and −85.77% attention deviation vs NAT baselines |
| 16 | [[2610.21808]] RoleQ：三值化角色对齐缩放 · RoleQ: Role-Aligned Ternary Conversion | 方法 / method | 角色对齐缩放 + Fisher 稀疏第二三值平面：半位比特即可恢复 8B 上约一半 MMLU 损失 \| Role-aligned scale placement plus a Fisher-saliency second ternary plane: half a bit recovers about half the MMLU loss at 8B |
| 17 | [[2610.21257]] 分数二次幂量化 · Fractional Power-of-Two Quantization | 方法 / method | base-√2 分数 PoT 网格 + 校准吸收近似算术：Llama-3-8B W4A4 零样本 +8.72% \| A base-√2 fractional PoT grid with calibration-absorbed arithmetic: +8.72% zero-shot on Llama-3-8B W4A4 across 7 models |
| 18 | [[2610.21126]] 稀疏 KV 的位置几何修复 · Post-Selection Positional Geometry for Sparse KV Caches | 方法 / method | RoPERelay 逆旋转再旋转修复被驱逐 token 的 RoPE 空洞：LongMemEval-S 23.6%→35.4%（开销 1–3%）\| Order-preserving re-coordination of RoPE gaps left by evicted tokens lifts LongMemEval-S 23.6%→35.4% at 1–3% overhead |
| 19 | [[2610.18139]] 重审量化误差反馈 · Revisiting Error Feedback for Quantization | 分析 / analysis | 度量相关的迹形式误差反馈 + Jacobian 感知最优点；迹最优未必带来有限级数下的性能提升 \| A metric-dependent trace formulation with a Jacobian-aware optimum; trace optimality need not improve finite-level LM performance |
| 20 | [[2610.20303]] SpectrumQuant：谱对齐量化 · SpectrumQuant: Spectrum Alignment for LLM Quantization | 方法 / method | 协方差对齐闭式旋转（Hadamard 为特例）：<1/3 显存、远快于 SpinQuant/DartQuant 且性能持平 \| Covariance-aligned closed-form rotations (Hadamard as special case) match SOTA at <1/3 the GPU memory and far less time |

### 7. LLM 隐状态与可解释性 / LLM Hidden States & Interpretability（25 篇 / 25 papers）

| # | 论文 / Paper | 类型 / Type | 入选理由 / Why it matters |
|---|---|---|---|
| 1 | [[2610.16084]] 尖锐方向不利于你：转向曲率分析 · The Sharp Directions Are Against You | 分析 / analysis | CAA 向量中 1–5% 能量的高曲率"尖锐分量"是抗转向根源；一行移除全面超越 CAA \| The 1–5%-energy sharp components of CAA vectors cause anti-steering; one-line sharp removal wins all 25 generation conditions over CAA |
| 2 | [[2610.21708]] 人类干预作为标签定位智能体失效 · Human Interventions as Labels for Agent Failures | 分析 / analysis | 干预标签方向在 5/13 适用模型上翻转 72–100% 留出过度求助；探针门控转向卸下大部分监督负担 \| Intervention-labeled directions flip 72–100% of held-out over-asks in 5 of 13 eligible models; probe-gated steering removes most oversight burden |
| 3 | [[2610.22937]] 多偏见一回路 · Many Biases, One Circuit | 分析 / analysis | 四类看似独立的偏见共享同一预训练线索路由回路；RL 阶段强化线索跟随 \| Four separate-seeming biases rely largely on the same pretrained cue-routing heads; the RL stage strengthens cue-following |
| 4 | [[2610.20748]] 解释语言模型参数 · Interpreting Language Model Parameters | 方法 / method | 对抗式参数分解为消融稳健子组件 + 子组件交互的回路式分析 \| Adversarial parameter decomposition into ablation-robust subcomponents with circuit-style analysis of their interactions |
| 5 | [[2610.24133]] Transformer 条件无毛定理 · A Conditional No-Hair Theorem for Transformers | 分析 / analysis | 提示信息以幂律速率被遗忘（训练模型 α=0.55–0.7）；logit 偏置取消可停止并逆转衰减 \| Prompt-determined hidden-state distance decays by power law (α=0.55–0.7 trained); logit-bias cancellation stops and reverses the decay |
| 6 | [[2610.20683]] CodeLM 因果语法回路 · Causal Syntax Circuits in CodeLMs | 分析 / analysis | 探针与预算选择决定"看似局部化"：探针切换使测得偏好 1.6→0.01，显著性 1/15 vs 6/15 \| Probe and budget choices flip localization conclusions: probe swap moves measured preference 1.6→0.01 across 55 settings, 10 code models |
| 7 | [[2610.19709]] Mamba 检索为何失效 · Beyond State Capacity: Why Retrieval Breaks in Mamba | 分析 / analysis | 状态容量充足时检索仍失败：检索关键层门控未对齐相关性信号，门控干预使精度在极端间摆动 \| Mamba fails in-context retrieval even with sufficient state capacity; gate interventions at retrieval-critical layers swing accuracy between extremes |
| 8 | [[2610.22300]] 微调前线性可读的知识会泛化 · Knowledge Linear Before Fine-Tuning Generalizes After | 分析 / analysis | 预训练知识的线性可读性预测微调后泛化（11 LLM × 70 关系，r=0.87–0.92）\| Linear-probe readability of pretrained relations predicts post-fine-tuning generalization (r=0.87–0.92 across 11 LLMs, 70 relations) |
| 9 | [[2610.21176]] 共享的工作记忆读出瓶颈 · A Shared Readout Bottleneck in Working Memory | 分析 / analysis | 15 个 LLM 的工作记忆错误源于干扰下的读出而非注意力精度；干扰抑制提升 d′ \| Working-memory errors arise from reading items out under interference, not attention precision; interference suppression improves d′ |
| 10 | [[2610.24521]] 转码器特征是"伪装的神经元" · Many Transcoder Features Are Neurons in Disguise | 分析 / analysis | 13 个开源转码器中大量晚层特征实为单神经元对齐；只有神经元特征跨运行稳定 \| Many late-layer transcoder features align with single MLP neurons; only neuron features are stable across runs |
| 11 | [[2610.17301]] 智能体知情：内部状态预警越权 · The Agent Knew: Internal States Forecast Unauthorized Actions | 方法 / method | 残差流线性读出在发出前预警越权（AUROC 0.94）与谎报；门控把违规 0.70→0.09，预注册 \| Residual-stream readouts forecast violations (AUROC 0.94) and false reports before emission; gating cuts violations 0.70→0.09 at ~10^-8 compute, preregistered |
| 12 | [[2610.21182]] 潜思维链真的在推理吗 · Does Latent Chain-of-Thought Actually Reason? | 分析 / analysis | 21 配置系统检验：COCONUT 常携带已可读答案，有序链可作占位符而非推理 \| Across 21 model-task configs, COCONUT often carries an already-readable answer and ordered chains can act as placeholders |
| 13 | [[2610.20887]] 涌现失配模型共享回路吗 · Do Emergent Misalignment Models Share a Circuit? | 分析 / analysis | 三个涌现失配 LoRA 微调共享可迁移回路组件（EM 38.9→22.9% 等），跨个体转移 \| Three emergent-misalignment fine-tunes share transferable circuit components (EM 38.9→22.9% and similar), with cross-organism transfer |
| 14 | [[2610.19768]] 会算≠会留用：循环 Transformer · Learning to Compute Is Not Learning to Retain | 分析 / analysis | 循环 Transformer 过训练深度仅存 22% 答案（随机位置监督下 99.8%）；隐向量交换重定向全部 237/237 对 \| Looped transformers keep only 22% past trained depth (99.8% with random-position supervision); hidden-vector swaps redirect all 237/237 pairs |
| 15 | [[2610.23242]] 各向异性表示动力学 · Anisotropic Representation Dynamics | 分析 / analysis | 混合门控理论分离 value 传输与 query/key 门控，谱判据给出 regime 切换充要条件 \| Mixture-gated theory separates value transport from query/key gating with a necessary-and-sufficient spectral criterion, validated on 4 architectures |
| 16 | [[2610.21256]] 无标签子空间隔离模型判断 · Isolating a LM's Judgment with a Label-Free Subspace | 方法 / method | 移除"表达子空间"后否定指令下 AUROC 0.504→0.825；判断在早期层仍可读 \| Label-free expression-subspace removal lifts negation AUROC 0.504→0.825 (entailment) while judgment stays readable in earlier layers |
| 17 | [[2610.21240]] SAE 表示重分布 · Representation Redistribution in Sparse Autoencoders | 方法 / method | 重分布敏感性分数区分"表示变化"与"真失效"：冻结安全读出上 AUROC 0.935/0.958 \| A redistribution sensitivity score separates representation change from true failure: AUROC 0.935/0.958 on frozen safety readouts across 27 SAEs |
| 18 | [[2610.20851]] 完备或稀疏：两种可识别性 · Complete or Sparse: Two Identifiabilities | 分析 / analysis | 监督学习何时恢复真潜变量 vs 非线性混合：生成/判别方向的统一可识别性理论 \| Identifiability theory over generative/discriminative directions for when supervised learning recovers true latents; validated on LLM activations and cortex |
| 19 | [[2610.17117]] 层论分解 Transformer 表示 · A Sheaf-Theoretic Decomposition of Representations | 方法 / method | 层论内容子空间在留出 CounterFact 上超 LEACE +17.1pp；谐质量排序转向脆弱性（ρ=0.90）\| A sheaf content subspace beats LEACE +17.1pp on held-out CounterFact across 8 architectures; harmonic mass ranks steering fragility (ρ=0.90) |
| 20 | [[2610.21261]] SAE 表示的行为组合性 · Behavioral Compositionality of SAE Representations | 分析 / analysis | SAE 特征效应非加性组合；成对建模把转向排名保真 0.59→0.78 \| SAE feature effects fail to compose additively in behavior; pairwise modeling lifts steering rank fidelity 0.5874→0.7790 in all 18 settings |
| 21 | [[2610.20680]] SAE 数据收益递减 · Diminishing Returns of Data in Sparse Autoencoders | 分析 / analysis | 功能收敛不保证特征可复现：严格匹配特征 5M token 时 2%、50M 时 29% \| Functional convergence does not guarantee feature reproducibility: strictly matched features rise only 2%→29% from 5M to 50M tokens |
| 22 | [[2610.25026]] 一个注意力头引发语言混淆 · One Head Away from Language Confusion | 分析 / analysis | 12 检查点中 7 个单头可把 8.0–51.5% 续写移出提示语言；头输出替换重定向 84–99% 单语回复 \| Seven single heads move 8.0–51.5% of continuations out of the prompt language; head-output replacement redirects 84–99% of monolingual replies |
| 23 | [[2610.22046]] 隐状态探针定位推理失效 · Hidden-State Probes for Localizing Reasoning Failures | 分析 / analysis | 终答训练探针漏掉 81% 单步不可恢复案例；无探针的轨迹长度规则不输任何探针 \| Final-answer probes miss 81% of single-step-unrecoverable cases; no probe beats a trace-length rule at step localization |
| 24 | [[2610.25464]] 论推理正确性方向 · On Reasoning Correctness Directions | 分析 / analysis | 统计显著的正确性方向存在，但无一稳定改进推理——对线性表示假设的质疑 \| Statistically significant correctness directions exist, yet none consistently improves reasoning — questioning the linear representation hypothesis |
| 25 | [[2610.20067]] 知识冲突中该信谁 · Which Knowledge Should LLMs Trust? | 分析 / analysis | 单一线性残差流方向跨 4 模型族泛化，迁移到 RAG/记忆/规则遵循并一致提升上下文信息利用 \| One generalizable linear steering direction improves context use across conflict formats and transfers to RAG, memory, and rule-following |

### 8. 大规模机器学习算力基础设施 / Compute Infrastructure for Large-Scale ML（10 篇 / 10 papers）

| # | 论文 / Paper | 类型 / Type | 入选理由 / Why it matters |
|---|---|---|---|
| 1 | [[2610.21500]] KV 缓存慢于 GPU：远端 KV 分层 · When the KV Cache Is Slower Than the GPU | 分析 / analysis | 远端 KV 层把命中变成排队不稳定（p99 3.96→17.3s）；MLA 分片 + 异步加载后 p99 0.67s、预填吞吐 +14–34% \| Remote KV tiers turn cache hits into queue instability; MLA-store sharding + async loading give p99 0.67 s and +14–34% prefill throughput |
| 2 | [[2610.17901]] FlashMask-3：掩码感知分布式注意力 · FlashMask-3: Mask-Aware Distributed Attention | 系统 / system | Hopper 掩码感知内核 + 零通信 CP：45–141% TFLOPs 提升，128 H100 上 118B MoE @128K \| A Hopper mask-aware kernel with zero-communication CP: 45–141% TFLOPs over FlashMask/FlexAttention; 118B MoE at 128K on 128 H100s |
| 3 | [[2610.16866]] PivotRL：资源可转移 RL 后训练 · PivotRL: Resource-Shiftable RL Post-training | 系统 / system | 集群 CPU 内存参数池 + shift-aware 迁移：128 卡 H20 上较 colocated 1.81–2.05×，收敛不受损 \| A global parameter pool plus shift-aware migration: 1.81–2.05× over colocated and 1.50–1.95× over disaggregated on a 128-GPU cluster |
| 4 | [[2610.22230]] Meta 的 AMD GPU 端到端协同设计 · Meta's Co-Design for AI Training on AMD GPUs | 报告 / report | 硬件建模协同设计 + 零预热内核选择 + 智能体 CUDA 移植：MI350X 上较直接移植至多 1.5× 端到端吞吐 \| Hardware-model co-design, zero-warmup kernel selection, and agentic CUDA porting yield up to 1.5× end-to-end throughput on MI350X vs direct ports |
| 5 | [[2610.19423]] 混合投影 + 自动调优分布式训练 · Hybrid Projection & Automated Tuning | 系统 / system | 微基准 + 缩放测量的投影引擎 + LLM 调优：1024 GPU DeepSeek V3 吞吐预测误差 4.7% \| A hybrid projection engine plus LLM tuning agent predicts multi-node throughput within ~10% (4.7% error at 1,024 GPUs) |
| 6 | [[2610.22035]] ETH：异构流水线并行 · ETH: Data-Balanced Heterogeneous Pipeline Parallelism | 系统 / system | 层次跨/阶段内负载均衡 + 分块梯度聚合：至多 2× 提速、配置搜索开销降 56× \| Hierarchical cross/intra-stage balance with block-wise gradient aggregation: up to 2× speedup and 56× less search overhead |
| 7 | [[2610.23086]] PairSight：GPU 共享算子级干扰预测 · PairSight: Operator-Level Interference in GPU Sharing | 分析 / analysis | SM 分区下共享内存路径争用的硬件计数器追踪：6 个 DNN 平均延迟预测误差 4.3%（规则法 19.0%）\| Hardware-counter tracing of shared-memory contention: 4.3% mean latency-prediction error vs 19.0% for the compute-memory rule |
| 8 | [[2610.18143]] RadixFlow：填补前缀缓存服务空泡 · RadixFlow: Filling Bubbles in Prefix-Cached Serving | 系统 / system | 状态就绪遍历解耦前缀匹配与就绪性：五个混合模型平均延迟 −3–24% 而复用率几乎不变 \| State-ready traversal decouples prefix match from readiness: 3–24% lower mean latency on five hybrid models at almost unchanged reuse |
| 9 | [[2610.21162]] 无协调负载正则化 · Coordination-Free Workload Regularization | 方法 / method | 批次成本前瞻的有界秩内重分区：8×H200 上较 pooled MFFD 1.05–1.17×，秩间成本波动 −82.8% \| Batch Cost Lookahead repartitioning: 1.050–1.167× over pooled MFFD on 8 H200s with −82.8% per-rank cost variability |
| 10 | [[2610.19405]] 并行推理的吞吐–延迟权衡 · Scaling LLM Inference via Parallelism | 分析 / analysis | TTFT-ITL 可行集、Pareto 前沿与 goodput 选型系统刻画并行配置（含 TP→PP 转折）\| TTFT-ITL feasible sets, Pareto frontiers, and goodput-based selection characterize parallelism choices, revealing TP-to-PP transitions |

### 9. 模型系统卡与技术报告 / Model System Cards & Technical Reports（3 篇 / 3 papers）

> 本周该领域配额为 5，但通过门控并完成排序的仅 3 篇，未用满的名额不回收。
> The area quota was 5, but only 3 reports passed the gate and completed ranking; unused slots were not redistributed.

| # | 论文 / Paper | 类型 / Type | 入选理由 / Why it matters |
|---|---|---|---|
| 1 | [[2610.19331]] LLM-jp-4 技术报告 · LLM-jp-4 Technical Report | 报告 / report | 日本主权 LLM：8B 稠密 + 32B-A3B MoE、约 12T token、全流程公开可复现，日语追平 Qwen3-8B/gpt-oss-20b \| A fully transparent Japanese sovereign effort: 8B dense + 32B-A3B MoE on ~12T tokens with reproducible data/model/software selection; on par in Japanese |
| 2 | [[2610.24628]] Muse Glimmer 30B 端侧智能体模型 · Muse Glimmer 30B: An On-Device Agentic Model | 报告 / report | Meta 开源 30B 蒸馏模型（4-bit 单卡、Apache 2.0）：多数 Agent 基准胜同量级，多语言 Agent 是最大差异化 \| Meta's open 30B distilled from Muse Spark (4-bit single-GPU, Apache 2.0): wins most agent/tool benchmarks in class, multilingual agency is the standout edge |
| 3 | [[2610.20818]] Intern Lumina U2 全视觉统一模型 · Intern Lumina U2: Omni-Visual Diffusion LLM | 报告 / report | 上海 AI Lab 多码本离散扩散 LM 统一图像/视频/3D 理解与生成编辑，理解优势集中于文档/图表 \| A multi-codebook discrete diffusion LM unifying image/video/3D understanding and generation; understanding wins concentrate in document/chart niches |

---

## All Papers

> 全部 103 篇入选论文完整索引（与 `filtered_papers.json` 的 `total_selected` 一致）。
> Complete index of all 103 selected papers (matches `total_selected` in `filtered_papers.json`).

| # | 论文 / Paper | 领域 / Area | 类型 / Type |
|---|---|---|---|
| 1 | [[2610.22984]] 自进化智能体的修复–泛化鸿沟 · Self-Evolving Agents Repair but Struggle to Generalize | 自进化智能体与自动化研究 / Self-Evolving Agents & Automated Research | 分析 / analysis |
| 2 | [[2610.21646]] 自我改进问题 · The Self-Improvement Problem | 自进化智能体与自动化研究 / Self-Evolving Agents & Automated Research | 分析 / analysis |
| 3 | [[2610.21055]] Athanor 自主后训练 · Athanor: Autonomous Post-Training Research | 自进化智能体与自动化研究 / Self-Evolving Agents & Automated Research | 系统 / system |
| 4 | [[2610.22466]] 工具链进化增益归因 · Harness-Delta Attribution | 自进化智能体与自动化研究 / Self-Evolving Agents & Automated Research | 分析 / analysis |
| 5 | [[2610.19386]] STRATA 自维护经验图 · STRATA: Self-Maintaining Experience Graphs | 自进化智能体与自动化研究 / Self-Evolving Agents & Automated Research | 方法 / method |
| 6 | [[2610.24944]] Epi 持久自改进智能体 · Epi: Persistent Self-Improving Agent | 自进化智能体与自动化研究 / Self-Evolving Agents & Automated Research | 系统 / system |
| 7 | [[2610.22029]] 选择即学习？ · Selection Is Not Learning | 自进化智能体与自动化研究 / Self-Evolving Agents & Automated Research | 方法 / method |
| 8 | [[2610.23344]] 语言模型学会改进语言模型 · LMs Learn to Improve LMs | 自进化智能体与自动化研究 / Self-Evolving Agents & Automated Research | 方法 / method |
| 9 | [[2610.17184]] DuoDiscover 突破评测瓶颈 · DuoDiscover: Beyond the Evaluation Bottleneck | 自进化智能体与自动化研究 / Self-Evolving Agents & Automated Research | 系统 / system |
| 10 | [[2610.17609]] 验证器–工具链协同进化 · Verifier-Harness Co-Evolution | 自进化智能体与自动化研究 / Self-Evolving Agents & Automated Research | 方法 / method |
| 11 | [[2610.22344]] MLExpert 自主 ML 工程 · MLExpert: Autonomous ML Engineering | 自进化智能体与自动化研究 / Self-Evolving Agents & Automated Research | 系统 / system |
| 12 | [[2610.22603]] 忙海狸前沿自主发现 · Busy Beaver Autonomous Discovery | 自进化智能体与自动化研究 / Self-Evolving Agents & Automated Research | 系统 / system |
| 13 | [[2610.17528]] ATTUNE 吞吐调优 · ATTUNE: Agentic Throughput Tuning | LLM 训练稳定性与可观测性 / LLM Training Stability & Observability | 系统 / system |
| 14 | [[2610.19761]] CAST 谱裁剪 · CAST: History-Adaptive Spectral Clipping | LLM 训练稳定性与可观测性 / LLM Training Stability & Observability | 方法 / method |
| 15 | [[2610.18085]] 优化器非等变 · No Optimizer Is Equivariant to Reparameterization | LLM 训练稳定性与可观测性 / LLM Training Stability & Observability | 分析 / analysis |
| 16 | [[2610.19064]] 内层优化器与副本扩展 · Inner Optimizers Shape Replica Scaling | LLM 训练稳定性与可观测性 / LLM Training Stability & Observability | 分析 / analysis |
| 17 | [[2610.22623]] 外层 Nesterov 稳定性 · Outer Nesterov Momentum Stability | LLM 训练稳定性与可观测性 / LLM Training Stability & Observability | 分析 / analysis |
| 18 | [[2610.19185]] 可靠基座评测设置 · Reliable Base-Model Benchmarking | LLM 训练稳定性与可观测性 / LLM Training Stability & Observability | 分析 / analysis |
| 19 | [[2610.20439]] 精度井 · The Accuracy Well | LLM 训练稳定性与可观测性 / LLM Training Stability & Observability | 分析 / analysis |
| 20 | [[2610.22650]] 切换优化器的代价 · Cost of Switching Optimizers | LLM 训练稳定性与可观测性 / LLM Training Stability & Observability | 分析 / analysis |
| 21 | [[2610.24305]] Muon 超越稳定性边缘 · Muon Beyond the Edge of Stability | LLM 训练稳定性与可观测性 / LLM Training Stability & Observability | 分析 / analysis |
| 22 | [[2610.22945]] 扩散模型不止需要 EMA · More Than EMA | LLM 训练稳定性与可观测性 / LLM Training Stability & Observability | 分析 / analysis |
| 23 | [[2610.21404]] 多奖励黑客 · Multi-Reward Hacking & TAG | RL 后训练动态与失效 / RL Post-Training Dynamics & Failures | 方法 / method |
| 24 | [[2610.18442]] 抄袭非接地 · Copying Is Not Grounding | RL 后训练动态与失效 / RL Post-Training Dynamics & Failures | 方法 / method |
| 25 | [[2610.19832]] 寻租语言模型 · Rent-Seeking Language Models | RL 后训练动态与失效 / RL Post-Training Dynamics & Failures | 分析 / analysis |
| 26 | [[2610.18853]] 双时钟 · Two Clocks in RLVR | RL 后训练动态与失效 / RL Post-Training Dynamics & Failures | 分析 / analysis |
| 27 | [[2610.21682]] 路由器漂移控制 · Router Drift Control in MoE RL | RL 后训练动态与失效 / RL Post-Training Dynamics & Failures | 方法 / method |
| 28 | [[2610.17062]] 梯度路由消除意外行为 · Gradient Routing Removes Unintended Behaviors | RL 后训练动态与失效 / RL Post-Training Dynamics & Failures | 方法 / method |
| 29 | [[2610.19525]] 校准似然抗作弊 · CALIF vs Verifiable-IF Hacking | RL 后训练动态与失效 / RL Post-Training Dynamics & Failures | 方法 / method |
| 30 | [[2610.20898]] 错误投票、正确梯度 · Wrong Votes, Right Gradients | RL 后训练动态与失效 / RL Post-Training Dynamics & Failures | 分析 / analysis |
| 31 | [[2610.19697]] CAFE FeFET 编码 · CAFE for FeFET CiM | 推理可靠性与 SDC 检测 / Inference Reliability & SDC Detection | 方法 / method |
| 32 | [[2610.22520]] 软错误致幻觉 · Soft-Error Hallucinations | 推理可靠性与 SDC 检测 / Inference Reliability & SDC Detection | 分析 / analysis |
| 33 | [[2610.22003]] 编译器有状态测试 · Stateful Testing for DL Compilers | 推理可靠性与 SDC 检测 / Inference Reliability & SDC Detection | 方法 / method |
| 34 | [[2610.23290]] dMLLM 重复诅咒 · CoTA++: Repeat Curse in dMLLMs | 推理可靠性与 SDC 检测 / Inference Reliability & SDC Detection | 方法 / method |
| 35 | [[2610.23328]] 可信峰值内存调度 · Certified Peak-Memory Schedules | 推理可靠性与 SDC 检测 / Inference Reliability & SDC Detection | 方法 / method |
| 36 | [[2610.23818]] 有损投机解码长度膨胀 · Length Inflation in Lossy Spec Decoding | 推理可靠性与 SDC 检测 / Inference Reliability & SDC Detection | 分析 / analysis |
| 37 | [[2610.22454]] 预填充专家削减伤害 · Where Prefill Expert Reduction Hurts | 推理可靠性与 SDC 检测 / Inference Reliability & SDC Detection | 分析 / analysis |
| 38 | [[2610.18014]] LatentRemedy 非前缀 KV 复用 · LatentRemedy: Non-Prefix KV Reuse | 推理可靠性与 SDC 检测 / Inference Reliability & SDC Detection | 方法 / method |
| 39 | [[2610.17338]] 预算化 KV 修复 · Budgeted KV-Cache Repair | 推理可靠性与 SDC 检测 / Inference Reliability & SDC Detection | 方法 / method |
| 40 | [[2610.24715]] 重复循环锁死 · When Do Repetition Loops Lock? | 推理可靠性与 SDC 检测 / Inference Reliability & SDC Detection | 分析 / analysis |
| 41 | [[2610.17544]] 推理收缩与记忆复用 · Reasoning Contraction & Memory Reuse | 智能体与流水线静默失效 / Agent & Pipeline Silent Failures | 分析 / analysis |
| 42 | [[2610.24545]] LLM 调用点契约 · Call-Site Contracts | 智能体与流水线静默失效 / Agent & Pipeline Silent Failures | 分析 / analysis |
| 43 | [[2610.20003]] 编码智能体报告缺口 · What Coding Agents Leave Unsaid | 智能体与流水线静默失效 / Agent & Pipeline Silent Failures | 分析 / analysis |
| 44 | [[2610.20927]] 源判定压缩 · Source-Judged Compaction | 智能体与流水线静默失效 / Agent & Pipeline Silent Failures | 方法 / method |
| 45 | [[2610.19342]] A2A 失效分类 · A2A Failure Taxonomy | 智能体与流水线静默失效 / Agent & Pipeline Silent Failures | 分析 / analysis |
| 46 | [[2610.16020]] 补偿继承量化误差 · Compensating Inherited Quantization Error | 极限性能优化下的可靠性 / Reliability under Extreme Performance Optimization | 分析 / analysis |
| 47 | [[2610.19934]] 剪枝模型停不下来 · To Reason but Not to Stop | 极限性能优化下的可靠性 / Reliability under Extreme Performance Optimization | 方法 / method |
| 48 | [[2610.17637]] 混合精度缩放律 · Mixed Precision Scaling Laws | 极限性能优化下的可靠性 / Reliability under Extreme Performance Optimization | 分析 / analysis |
| 49 | [[2610.20826]] 路由≠量化敏感性 · Routing ≠ Quant Sensitivity | 极限性能优化下的可靠性 / Reliability under Extreme Performance Optimization | 分析 / analysis |
| 50 | [[2610.24343]] NVFP4 训练配方 · What Matters for NVFP4 Training | 极限性能优化下的可靠性 / Reliability under Extreme Performance Optimization | 分析 / analysis |
| 51 | [[2610.25460]] 保可靠性医学压缩 · Reliability-Preserving Medical Compression | 极限性能优化下的可靠性 / Reliability under Extreme Performance Optimization | 方法 / method |
| 52 | [[2610.24346]] 精度升级任务价值 · Task Value of Precision Upgrades | 极限性能优化下的可靠性 / Reliability under Extreme Performance Optimization | 分析 / analysis |
| 53 | [[2610.24968]] 视觉剪枝充分性景观 · Visual Sufficiency Landscapes | 极限性能优化下的可靠性 / Reliability under Extreme Performance Optimization | 分析 / analysis |
| 54 | [[2610.18343]] 语言变体量化鲁棒性 · Quant Robustness across Language Varieties | 极限性能优化下的可靠性 / Reliability under Extreme Performance Optimization | 分析 / analysis |
| 55 | [[2610.19498]] 量化供应链可验证性 · Verifiability Gap in Quant Supply Chains | 极限性能优化下的可靠性 / Reliability under Extreme Performance Optimization | 分析 / analysis |
| 56 | [[2610.19605]] PN-Mix 2-bit KV · PN-Mix Mixed-Precision Key Cache | 极限性能优化下的可靠性 / Reliability under Extreme Performance Optimization | 方法 / method |
| 57 | [[2610.23046]] SpikeQ SNN 量化 · SpikeQ for SNN PTQ | 极限性能优化下的可靠性 / Reliability under Extreme Performance Optimization | 方法 / method |
| 58 | [[2610.20686]] RoLaQ MLA 2-bit KV · RoLaQ for 2-Bit MLA KV | 极限性能优化下的可靠性 / Reliability under Extreme Performance Optimization | 方法 / method |
| 59 | [[2610.24740]] VLM 剪枝评测 PAA-Bench · Are We Evaluating VLM Token Pruning Right? | 极限性能优化下的可靠性 / Reliability under Extreme Performance Optimization | 基准 / benchmark |
| 60 | [[2610.22065]] ABNAT 噪声感知训练 · ABNAT for Analog CiM | 极限性能优化下的可靠性 / Reliability under Extreme Performance Optimization | 方法 / method |
| 61 | [[2610.21808]] RoleQ 三值化 · RoleQ Ternary Conversion | 极限性能优化下的可靠性 / Reliability under Extreme Performance Optimization | 方法 / method |
| 62 | [[2610.21257]] 分数二次幂量化 · Fractional Power-of-Two Quantization | 极限性能优化下的可靠性 / Reliability under Extreme Performance Optimization | 方法 / method |
| 63 | [[2610.21126]] 稀疏 KV 位置几何 · Post-Selection Positional Geometry | 极限性能优化下的可靠性 / Reliability under Extreme Performance Optimization | 方法 / method |
| 64 | [[2610.18139]] 重审误差反馈 · Revisiting Error Feedback | 极限性能优化下的可靠性 / Reliability under Extreme Performance Optimization | 分析 / analysis |
| 65 | [[2610.20303]] SpectrumQuant 谱对齐 · SpectrumQuant: Spectrum Alignment | 极限性能优化下的可靠性 / Reliability under Extreme Performance Optimization | 方法 / method |
| 66 | [[2610.16084]] 转向曲率分析 · Curvature Analysis of Activation Steering | LLM 隐状态与可解释性 / LLM Hidden States & Interpretability | 分析 / analysis |
| 67 | [[2610.21708]] 干预标签定位失效 · Localizing Agent Failures via Interventions | LLM 隐状态与可解释性 / LLM Hidden States & Interpretability | 分析 / analysis |
| 68 | [[2610.22937]] 多偏见一回路 · Many Biases, One Circuit | LLM 隐状态与可解释性 / LLM Hidden States & Interpretability | 分析 / analysis |
| 69 | [[2610.20748]] 解释模型参数 · Interpreting LM Parameters | LLM 隐状态与可解释性 / LLM Hidden States & Interpretability | 方法 / method |
| 70 | [[2610.24133]] 条件无毛定理 · Conditional No-Hair Theorem | LLM 隐状态与可解释性 / LLM Hidden States & Interpretability | 分析 / analysis |
| 71 | [[2610.20683]] CodeLM 语法回路 · Causal Syntax Circuits in CodeLMs | LLM 隐状态与可解释性 / LLM Hidden States & Interpretability | 分析 / analysis |
| 72 | [[2610.19709]] Mamba 检索失效 · Why Retrieval Breaks in Mamba | LLM 隐状态与可解释性 / LLM Hidden States & Interpretability | 分析 / analysis |
| 73 | [[2610.22300]] 线性知识泛化 · Linear Knowledge Generalizes | LLM 隐状态与可解释性 / LLM Hidden States & Interpretability | 分析 / analysis |
| 74 | [[2610.21176]] 工作记忆读出瓶颈 · Shared Readout Bottleneck | LLM 隐状态与可解释性 / LLM Hidden States & Interpretability | 分析 / analysis |
| 75 | [[2610.24521]] 转码器特征即神经元 · Transcoder Features Are Neurons | LLM 隐状态与可解释性 / LLM Hidden States & Interpretability | 分析 / analysis |
| 76 | [[2610.17301]] 智能体知情 · The Agent Knew | LLM 隐状态与可解释性 / LLM Hidden States & Interpretability | 方法 / method |
| 77 | [[2610.21182]] 潜思维链在推理吗 · Does Latent CoT Reason? | LLM 隐状态与可解释性 / LLM Hidden States & Interpretability | 分析 / analysis |
| 78 | [[2610.20887]] 涌现失配共享回路 · Emergent Misalignment Shared Circuit | LLM 隐状态与可解释性 / LLM Hidden States & Interpretability | 分析 / analysis |
| 79 | [[2610.19768]] 循环 Transformer 留存 · Loop Transformers Retention | LLM 隐状态与可解释性 / LLM Hidden States & Interpretability | 分析 / analysis |
| 80 | [[2610.23242]] 各向异性表示动力学 · Anisotropic Representation Dynamics | LLM 隐状态与可解释性 / LLM Hidden States & Interpretability | 分析 / analysis |
| 81 | [[2610.21256]] 无标签判断子空间 · Label-Free Judgment Subspace | LLM 隐状态与可解释性 / LLM Hidden States & Interpretability | 方法 / method |
| 82 | [[2610.21240]] SAE 表示重分布 · Representation Redistribution in SAEs | LLM 隐状态与可解释性 / LLM Hidden States & Interpretability | 方法 / method |
| 83 | [[2610.20851]] 两种可识别性 · Complete or Sparse Identifiability | LLM 隐状态与可解释性 / LLM Hidden States & Interpretability | 分析 / analysis |
| 84 | [[2610.17117]] 层论分解 · Sheaf-Theoretic Decomposition | LLM 隐状态与可解释性 / LLM Hidden States & Interpretability | 方法 / method |
| 85 | [[2610.21261]] SAE 行为组合性 · Behavioral Compositionality of SAEs | LLM 隐状态与可解释性 / LLM Hidden States & Interpretability | 分析 / analysis |
| 86 | [[2610.20680]] SAE 数据收益递减 · Diminishing Returns in SAEs | LLM 隐状态与可解释性 / LLM Hidden States & Interpretability | 分析 / analysis |
| 87 | [[2610.25026]] 单头引发语言混淆 · One Head from Language Confusion | LLM 隐状态与可解释性 / LLM Hidden States & Interpretability | 分析 / analysis |
| 88 | [[2610.22046]] 探针定位推理失效 · Probes for Reasoning Failures | LLM 隐状态与可解释性 / LLM Hidden States & Interpretability | 分析 / analysis |
| 89 | [[2610.25464]] 推理正确性方向 · On Reasoning Correctness Directions | LLM 隐状态与可解释性 / LLM Hidden States & Interpretability | 分析 / analysis |
| 90 | [[2610.20067]] 知识冲突该信谁 · Which Knowledge to Trust | LLM 隐状态与可解释性 / LLM Hidden States & Interpretability | 分析 / analysis |
| 91 | [[2610.21500]] 远端 KV 分层 · Remote KV Tiers for CP Prefill | 大规模机器学习算力基础设施 / Compute Infrastructure for Large-Scale ML | 分析 / analysis |
| 92 | [[2610.17901]] FlashMask-3 分布式注意力 · FlashMask-3 Mask-Aware Attention | 大规模机器学习算力基础设施 / Compute Infrastructure for Large-Scale ML | 系统 / system |
| 93 | [[2610.16866]] PivotRL 资源可转移 RL · PivotRL Resource-Shiftable RL | 大规模机器学习算力基础设施 / Compute Infrastructure for Large-Scale ML | 系统 / system |
| 94 | [[2610.22230]] Meta AMD GPU 协同设计 · Meta AMD GPU Co-Design | 大规模机器学习算力基础设施 / Compute Infrastructure for Large-Scale ML | 报告 / report |
| 95 | [[2610.19423]] 混合投影自动调优 · Hybrid Projection & Automated Tuning | 大规模机器学习算力基础设施 / Compute Infrastructure for Large-Scale ML | 系统 / system |
| 96 | [[2610.22035]] ETH 异构流水线并行 · ETH Heterogeneous Pipeline Parallelism | 大规模机器学习算力基础设施 / Compute Infrastructure for Large-Scale ML | 系统 / system |
| 97 | [[2610.23086]] PairSight 干扰预测 · PairSight Interference Prediction | 大规模机器学习算力基础设施 / Compute Infrastructure for Large-Scale ML | 分析 / analysis |
| 98 | [[2610.18143]] RadixFlow 服务空泡 · RadixFlow Filling Serving Bubbles | 大规模机器学习算力基础设施 / Compute Infrastructure for Large-Scale ML | 系统 / system |
| 99 | [[2610.21162]] 无协调负载正则化 · Coordination-Free Workload Regularization | 大规模机器学习算力基础设施 / Compute Infrastructure for Large-Scale ML | 方法 / method |
| 100 | [[2610.19405]] 并行推理权衡 · Parallelism Throughput-Latency Trade-off | 大规模机器学习算力基础设施 / Compute Infrastructure for Large-Scale ML | 分析 / analysis |
| 101 | [[2610.19331]] LLM-jp-4 技术报告 · LLM-jp-4 Technical Report | 模型系统卡与技术报告 / Model System Cards & Technical Reports | 报告 / report |
| 102 | [[2610.24628]] Muse Glimmer 30B · Muse Glimmer 30B On-Device Agent | 模型系统卡与技术报告 / Model System Cards & Technical Reports | 报告 / report |
| 103 | [[2610.20818]] Intern Lumina U2 · Intern Lumina U2 Omni-Visual | 模型系统卡与技术报告 / Model System Cards & Technical Reports | 报告 / report |

---

## 统计与核对 / Stats & Verification

- 评估 / evaluated: **3,671** · 门控候选 / stage-2 candidates: **865** · 通过门控 / gate-kept: **632** · 入选 / selected: **103**（各领域 12 / 10 / 8 / 10 / 5 / 20 / 25 / 10 / 3）
- 必读来源 / Must-Read source: `stars.json`（27 个候选全文精读，8 个 `star: true`）——本周必读 8 篇即全部星标论文，无自评加星 / the 8 Must Reads are exactly the starred entries; no re-starring was done.
- 核对 / Count check: 上表 All Papers 共 **103** 行，与 `filtered_papers.json` 的 `total_selected: 103` **一致，无差异** / the All Papers table has 103 rows, matching `total_selected` in `filtered_papers.json` — no discrepancy.
