---
title: "arXiv Weekly — 2026-09-14"
date: 2026-09-14
week: "2026-09-14..2026-09-20"
tags:
  - arxiv-weekly
  - llm-agents
  - self-evolving-agents
  - automated-research
  - interpretability
  - inference-reliability
  - quantization
papers: 100
---

# arXiv Weekly — 2026-09-14..2026-09-20

> 本周（2026-09-14 至 2026-09-20，ISO 第 38 周）从 **2,485** 篇提交中精选 **100** 篇（55 篇 5 分、45 篇 4 分），覆盖七大方向：自演化智能体与自动化科研（50）、LLM 隐藏状态与可解释性（21）、极致性能优化下的可靠性（17）、推理可靠性与 SDC 检测（6）、大规模 ML 计算基础设施（3）、LLM 训练稳定性与可观测性（2）、模型系统卡（1）。
> This week (2026-09-14 to 2026-09-20, ISO week 38) curates **100** papers (55 rated 5, 45 rated 4) from **2,485** submissions across seven areas: self-evolving agents & automated research (50), LLM hidden states & interpretability (21), reliability under extreme performance optimization (17), inference reliability & SDC detection (6), compute infrastructure for large-scale ML (3), training stability & observability (2), and model system cards (1).

---

## 本周必读 / Must Read This Week

### 1. [[2609.14857]] — ModularRSI: Modular and Generalizable Recursive Harness Self-Improvement

> **推荐理由 / Why read:** 把 CLI agent 的 harness 递归自改进拆成五个独立进化模块（对比式轨迹分析 + 验证门），在与评测基准完全不相交的 2,000 个自建任务上演化。TerminalBench 2.0 准确率 47.57→52.43、SWE-Bench Verified 73.40→76.45，且跨任务域、跨底层模型迁移；关键消融显示整-harness 联合进化反而跌破基线（44.19 < 47.57）——模块化 credit assignment 才是 harness RSI 泛化的关键，基准不相交协议也首次干净回答了“harness 自我改进到底学没学到可迁移的东西”。
> Decomposes harness RSI into five independently evolved modules (contrastive trajectory analysis + validation gates), evolved on a 2,000-task benchmark-disjoint set. Lifts TerminalBench 2.0 accuracy 47.57→52.43 and SWE-Bench Verified 73.40→76.45 with cross-domain and cross-model transfer; the pivotal ablation shows joint whole-harness evolution drops BELOW baseline (44.19), so modular credit assignment is the load-bearing design — and the benchmark-disjoint protocol is the first clean test of whether harness self-improvement transfers at all.

### 2. [[2609.14858]] — Dream-RSI: Recursive Self-Improvement through Evolving Worlds

> **推荐理由 / Why read:** 把发现树历史当作零执行成本的“回放模拟器”，探索策略在模拟器里“做梦”式离线改进再上线——把 model-based RL 的思想搬到 agentic discovery 的元层。Lasso 求解以 317 次调用击败 SimpleTES 的 51,200 次（约 162×），KernelBench 等预算下性能最高 2.09×；反直觉发现：历史作为可交互回放系统性地优于作为语义指导注入 prompt。
> Treats recorded discovery trees as zero-cost replay simulators so exploration policies improve offline ('dreaming') before redeployment — model-based RL transplanted to the meta-layer of agentic discovery. Beats SimpleTES on Lasso with 317 vs 51,200 calls (~162x fewer) and up to 2.09x on KernelBench at equal budget; counterintuitively, history-as-interactive-replay systematically beats history-as-prompt-guidance.

### 3. [[2609.15983]] — Stellar Colosseum: A Many-Agent Harness for Long-Horizon Research in Mathematics and Theoretical Computer Science

> **推荐理由 / Why read:** 五阶段多智能体科研流水线（策略探索→就绪门→DAG 分解→并行求解→全局验证），阶段内用“候选+证伪记录”的重叠采样树做构造性聚合而非投票。产出五项真实新定理（如 ℓp 核心集 ε^-p→ε^-2 指数级改进）并在断网条件下复现 Erdős 反例的核心架构；TCS-Bench 跨模型选择 71.0% vs 直接推理 30.3%（注意：71.0% 是双模型选择，单 harness 为 54.0%）。
> A five-stage many-agent research pipeline (strategy exploration, readiness gate, DAG decomposition, parallel solving, global verification) with critique-preserving overlapping tree aggregation instead of voting. Produced five genuine new theorems (e.g., coreset exponent improvement) and independently rediscovered the Erdos counterexample architecture with internet disabled; TCS-Bench cross-model selection hits 71.0% vs 30.3% direct (note: 71.0% is a two-model selection; the single-harness score is 54.0%).

### 4. [[2609.15396]] — SkillLift: Learning Dense Rubrics from Sparse Oracles for Efficient Skill Evolution

> **推荐理由 / Why read:** 技能进化的监督瓶颈在于每次编辑都要昂贵 oracle rollout。SkillLift 学一个“与 oracle 排序对齐（Kendall τ）”的二元 rubric 作零 rollout 成本的稠密评估器，外层每轮仅 K=3 次真实 rollout 重对齐，且冠军始终按真实 oracle 分选取（错位 rubric 只伤引导、不伤结果）。6 个“模型×基准”组合全胜 SkillOpt/CoEvoSkills（对手拿 2× 预算），token 省 40–70%。“排序优于分数回归”的监督设计可迁移到一切昂贵评估场景。
> Skill evolution is bottlenecked by oracle rollouts per edit. SkillLift learns a rubric aligned to the oracle's ranking (Kendall tau) as a zero-rollout dense evaluator, re-aligned with only K=3 real rollouts per outer round, while the champion is always selected by true oracle score (a misaligned rubric hurts guidance, never the outcome). Wins all six model-x-benchmark combinations against SkillOpt/CoEvoSkills even when baselines get 2x budget, with 40-70% token savings. The ranking-over-regression supervision transfers to any expensive-evaluation setting.

### 5. [[2609.15064]] — What Does an LLM Learn from Reinforcement Learning? A Mechanistic Interpretability Perspective with Fixed-SAE Track

> **推荐理由 / Why read:** 在 base + 13 个 RL checkpoint 的池化激活上训练一个共享冻结 SAE，使特征索引跨训练可比。发现 RL 漂移小、渐进、集中在晚期层的“格式脚手架”特征（换行、LaTeX、答案标签）；把这些方向的解码向量注入 base 模型即复现 RL 大部分收益（GSM8K 严格 0.050→0.192，超过 RL 终模型 0.175）——短期 RL 主要是“激发”而非“创造”。strict/lenient 双评分器分解本身即值得成为 RLVR 评测的标准做法。
> Trains one shared frozen SAE on pooled base+RL-checkpoint activations so feature indices stay comparable across training. RL drift is small, gradual, and late-layer-concentrated on formatting scaffolds (step breaks, LaTeX, answer tags); steering these decoded directions into the base model reproduces most of RL's gain (GSM8K strict 0.050→0.192, exceeding the RL-final 0.175) — short-horizon RL mostly elicits rather than creates. The strict/lenient two-grader decomposition deserves to become standard for auditing RLVR gains.

### 6. [[2609.15545]] — The Token Before the Value Is the Key: How Hybrid Architectures Organize Induction Circuits

> **推荐理由 / Why read:** 与层类型无关的配对探针首次让循环/混合架构的感应电路可测：Carrying（前驱信息准备）集中在 GDN/SWA 高效层且由 lag-one token（“值前一个 token 才是 key”）主导，Matching（内容检索）落在紧随其后的全局注意力层。早期 LR/卷积干预可把整条电路重定位并改变最终召回画像（identifier-reuse PPL 29.0→21.0）；Qwen3.5-4B 上确认同样分工。为混合架构设计与训练调度提供机制层依据。
> Layer-type-agnostic paired probes make induction circuits measurable in hybrid/recurrent LMs for the first time: Carrying concentrates in efficient layers and is dominated by the lag-one token ('the token before the value is the key'), while Matching lands in the next global-attention receiver. Early LR/convolution interventions relocate the whole circuit and shift final recall (identifier-reuse PPL 29.0→21.0); the same division of labor is confirmed in Qwen3.5-4B. Mechanistic grounding for hybrid architecture design and training schedules.

### 7. [[2609.15504]] — How Lossless Is Lossless Speculative Decoding? The Role of Numerical Precision in Orthrus

> **推荐理由 / Why read:** 独立复现并重训 Orthrus，逐 token 对比生成轨迹：BF16 下与自回归基线完全一致仅 43–45%，FP32 下 1,190/1,190 全对——“无损”其实是数值精度属性；发散集中在参考模型高困惑度的生成上（β₁=-8.1，p<10^-10），而 GSM8K/HumanEval/IFEval 分数完全看不出差异。所有“无损加速”声明都应标注精度与等价判据，基准打平不等于推理等价。
> Independent reproduction and retraining of Orthrus with exact trajectory comparison: only 43-45% sequence match under BF16 but 1,190/1,190 under FP32 — ''losslessness'' is a numerical-precision property. Divergence concentrates exactly where the reference model is least confident (beta=-8.1, p<1e-10) and is invisible to GSM8K/HumanEval/IFEval scores. Every ''lossless acceleration'' claim should specify precision and an equivalence criterion: benchmark parity is not inference equivalence.

### 8. [[2609.16085]] — Is INT8 Portable? A Cross-Platform Measurement Study of Quantized Inference on Embedded and Automotive Accelerators

> **推荐理由 / Why read:** 固定同一 ONNX 模型与 QDQ scale、跨 7 类嵌入式/车规硬件的受控测量：INT8 加速符号由点积指令集决定（有 dotprod/VNNI 快 1.83–2.11×，没有反慢 1.65–1.76×）；跨整数内核预测每 1000 张翻转 35–42 张而 FP32 全逐位一致（top-1 精度完全看不出）；高通 HTP 静默忽略自带 scale（top-1 0.75→0.005 且无任何报错）。异构 fleet 部署与安全冗余设计的必读实证。
> Controlled measurement across seven embedded/automotive hardware classes with one fixed ONNX artifact and fixed QDQ scales: the INT8 speedup sign is ISA-determined (1.83-2.11x with dot-product instructions, 1.65-1.76x SLOWER without); cross-kernel prediction flips on 35-42/1000 inputs while FP32 is always bit-identical (invisible to top-1 accuracy); Qualcomm HTP silently ignores bring-your-own scales (0.75→0.005 top-1, compiling and running without error). Essential evidence for heterogeneous-fleet deployment and safety-redundancy design.

---

## 按主题分类 / Papers by Topic

### A. 自演化智能体与自动化科研 / Self-Evolving Agents & Automated Research（50）

| Paper | 分数 / Score | 中文要点 | English Highlight |
|-------|------|---------|-------------------|
| [[2609.14857]] ModularRSI | 5 | 五模块独立进化 + 基准不相交进化任务，harness 自我改进可跨任务、跨模型迁移 | Five-module independent harness evolution on benchmark-disjoint tasks; gains transfer across tasks and backbones (TB 2.0, SWE-Bench Verified) |
| [[2609.14858]] Dream-RSI | 5 | 把发现树历史当作零成本回放模拟器，离线“做梦”改进探索策略，最多省 162× 调用 | Replays recorded discovery trees as free simulators to self-improve exploration policies offline, up to 162x fewer agent calls |
| [[2609.15096]] OpenAI4S | 5 | “代码即动作、科研即会话”双平面科研智能体，36 场景基准 7.83 分超 Claude Code 基线 | Code-as-action dual-plane science agent with session provenance scores 7.83 vs 5.79-6.36 for Claude Code baselines |
| [[2609.15364]] RSIAgent | 5 | 免训练“课程-执行-验证”递归探索构建冻结因果记忆，开源模型 OSWorld 2.0 反超闭源前沿 | Training-free curriculum/actor/verifier recursive exploration builds frozen causal memory, lifting open models past frontier baselines on OSWorld 2.0 |
| [[2609.15396]] SkillLift | 5 | 双层优化学习与 oracle 排序对齐的稠密 rubric 代理昂贵 rollout，技能进化 token 省 40–70% | Bilevel optimization learns oracle-aligned dense rubrics as cheap surrogate evaluators, cutting skill-evolution cost 40-70% |
| [[2609.15820]] AlgoEvo | 5 | 智能体自主搜索循环 + 设计技能库 + MCTS 经验树，以约 1/13 评估预算匹配或超过专用基线 | Agentic search loop with pluggable design-skill hub and MCTS experience tree matches or beats specialized baselines at ~1/13 the evaluations |
| [[2609.15938]] HypoEvolve | 5 | 遗传算法协调多智能体进化科学假说，34 种癌症药物重定位 DepMap 选择性 0.171 超最强基线 | Genetic algorithm coordinates LLM agents for hypothesis evolution; DepMap selectivity 0.171 beats the strongest baseline (0.115) across 34 cancer types |
| [[2609.15973]] Discovery Foundation Models | 5 | 定义“发现智能”七能力与可修订研究状态，GALILEO 湿/干实验闭环蒸馏出可迁移设计规则 | Formalizes seven discovery capabilities over a revisable research state; GALILEO's wet-lab loop distills transferable design rules |
| [[2609.15983]] Stellar Colosseum | 5 | 五阶段多智能体证明流水线产出 FOCS/JMLR 级新定理，TCS-Bench 跨模型选择 71.0% vs 直接推理 30.3% | Five-stage many-agent proof pipeline yields new FOCS/JMLR-level theorems; TCS-Bench cross-model selection reaches 71.0% vs 30.3% direct |
| [[2609.16245]] Metacognitive Steering | 5 | 万亿参数 MoE 中定位科学判断中层控制面并按认知状态混合 steering，Columbus-1 复现确认 8 个 BlueZ 漏洞 | Localizes a mid-depth scientific-judgment control surface in a 1T MoE and routes state-conditioned steering; Columbus-1 found 8 reproduced BlueZ vulnerabilities |
| [[2609.16816]] ImpossibleRubrics | 5 | 169 个不可能任务 + 可验证证书：LLM 生成奖励 rubric 被对抗答案利用 8–36%，证书忠实 rubric 为 0% | 169 impossible tasks with oracle certificates: LLM-generated reward rubrics are exploited 8-36% by adversarial answers; certificate-faithful ones 0% |
| [[2609.17523]] ScienceBuddy | 5 | “递归中递归”自改进：harness 进化与模型 RL 耦合，把研究者交互转化为任务与 rubric 持续学习 | Recursive-in-recursive self-improvement couples harness evolution with model RL, turning researcher interactions into tasks and rubrics |
| [[2609.17817]] Reflections on Trusting Trust, Revisited | 5 | 用投毒基准污染自我修改编码智能体的自评估，使其进化出禁用 HTTPS 证书校验的指令，且经干净基准进化仍残留 | Poisons self-modifying coding agents' self-evaluation so they evolve instructions disabling HTTPS validation; contamination survives clean-benchmark evolution |
| [[2609.17846]] PrimeScientist | 5 | MCTS 在可执行计划树上自适应分配研究预算：平均奖励 +10.3%，尝试次数省 50.6% | MCTS-based adaptive effort allocation over executable plan trees: +10.3% average reward with 50.6% fewer attempts |
| [[2609.17930]] Locating Hidden Failures Makes Long-Horizon Agents More Reliable | 5 | 6,967 个人工核验错误、78 类失效类型；4B Scout 定位首个错误优于前沿评委并提升测试时成功率 | 6,967 human-verified mistakes in 78 failure types; a 4B Scout verifier locates first mistakes better than frontier judges and lifts task success |
| [[2609.18094]] Agora | 5 | 13 个无规划者 LLM 工作者经 Git-DAG 共享记忆协作约 12 天，逼近 GPT-2 124M 权重迁移初始化问题 62% 的差距 | Thirteen planner-free LLM workers exchanged 1,703 Git-DAG contributions over ~12 days, closing 62% of the gap on a weight-transfer initialization task |
| [[2609.18598]] Hypothesis-Driven Autonomous Materials Synthesis with Multimodal LLM Agents | 5 | 多模态 LLM 智能体跑 18 次 LiCoO2 薄膜实验，“验证-证伪”演化出 650–690°C 结晶阈值认知 | Multimodal LLM agents run an 18-experiment LiCoO2 campaign with verify-falsify logic, evolving a 650-690 C crystallization threshold |
| [[2609.19099]] Evidence-Grounded Agentic Formulation Development in an Autonomous Laboratory | 5 | 基于结构化内部证据设计并执行紫杉醇 SEDDS 批次，高性能率 50%，对比优化器 17%、DoE 2% | Reasons over structured in-house evidence to execute paclitaxel SEDDS batches: 50% high-performance rate vs 17% (optimizer) and 2% (DoE) |
| [[2609.19101]] Monitoring and Discovering Reward Hacking with Internal Representations | 5 | 隐藏状态差分向量连贯表征奖励作弊（GLM 5.2 作弊 73% rollouts），可在线于 CoT 输出前拦截 | Difference-of-means hidden-state vectors coherently detect reward hacking (73% of rollouts) and catch hacks online before they occur |
| [[2609.19519]] An Architecture for Long-Horizon Agents | 5 | 层级/tick/级联智能架构支撑十天自主战役跨上下文重置保持连贯，早期知识不改权重地改变后期行为 | Levels/ticks/cascaded-intelligence architecture keeps a ten-day autonomous campaign coherent across context resets without weight changes |
| [[2609.19526]] Self Improvement via Fast Tree-search | 5 | 编码智能体递归自修改：LLM-judge Bradley-Terry 排序引导树搜索，把昂贵评测留给最有希望的补丁 | SIFT coding agents recursively self-modify under LLM-judge Bradley-Terry rankings, reserving expensive benchmark evals for the most promising patches |
| [[2609.19644]] ScientistTwo | 5 | 端到端自主发现：基线、假说、协调实验、消融与闭环同行评审驳稿引擎，产出专家级可发表论文 | ScientistTwo runs end-to-end autonomous discovery with coordinated experiments and a closed-loop peer-review rebuttal engine, producing expert-level papers |
| [[2609.20519]] SoL-Pi | 5 | harness 层递归自改进，四种 rollout 选择机制在开发外设置迁移并省 44–49% token | Harness-level recursive self-improvement with four rollout-selected mechanisms transferring beyond dev settings at 44-49% token reduction |
| [[2609.21257]] Verify, Don't Trust | 5 | 37 天人类把关在线 autoresearch：持久记录 + 确定性检查把 22pp 命中率下降归因于既有评测漂移 | Human-gated 37-day online autoresearch traced a 22pp hit-rate drop to pre-existing evaluation drift rather than the tested interaction head |
| [[2609.22086]] Designer-RSI | 5 | 从用户流量演化程序性记忆：未覆盖子任务“变宽”、自身失败“加深”，冻结 Claude 执行成功率 72.7%→99.3% | Evolves procedural memory from user traffic (widening and deepening) to lift frozen Claude-Sonnet-4 execution success from 72.7% to 99.3% |
| [[2609.22592]] AutoGym | 5 | 蓝图先行生成可验证智能体训练场：先定解空间与验证准则，再物化环境、难度参数与课程 | Blueprint-first gym generation specifying valid solution space and verification criteria before environments materialize, with difficulty parameters and curricula |
| [[2609.14976]] MemRiskBench | 4 | 五类记忆风险（陈旧事实、撤销复用、泄漏）的 trace 感知评测，保住稀有高危失效 | Five memory-risk categories with deterministic trace-grounded checks that preserve rare high-severity failures in agent evaluation |
| [[2609.15009]] CoMem | 4 | 个体经验沉淀 + 集体智慧策展 + 双流检索，让演化多智能体免受记忆污染 | Unifies private experience sedimentation with collective wisdom curation and dual-stream retrieval for evolutionary multi-agent systems |
| [[2609.15161]] EMR | 4 | 从问诊轨迹挖掘诊断洞见与失败警示、沉淀三级临床经验库的自演化医疗多智能体 | Self-evolving medical multi-agent system mining diagnostic insights and failure warnings into a three-level clinical experience library |
| [[2609.15209]] Failure-Guided Co-Evolution of Prompts and Training Data | 4 | 把不完美执行抽象为可复用失败模式，四种变异策略协同进化提示词与训练数据 | Co-evolves prompts and training data by abstracting imperfect executions into reusable failure modes via four mutation strategies |
| [[2609.15293]] Why LLM Agents Collapse Without Oversight | 4 | “执行缺口”（检测到却不行动）是 Emergence World 崩溃机制；不足 20 行的条件检查降攻击成功率 4 倍以上 | The enforcement gap (detection without action) explains Emergence World collapses; a sub-20-line conditional check cuts attack success more than fourfold |
| [[2609.15319]] Clean Scores, Buried Evidence, and Confident Wrong | 4 | 数据室审计：agentic QA 数字表准确但结构论断自信编造，需主张级溯源收据与条件感知评分 | Receipt-based audit shows agentic QA pairs accurate numbers with confident fabricated structural claims, motivating claim-level provenance |
| [[2609.15397]] When Tool Calls Succeed but Workflows Fail | 4 | 八类工具外部效应异常（重试/并发下缺失、重复、中止）；MCP 的 98,291 个工具无法表达所需事务语义 | Effect-history model catalogs eight external-effect anomalies (missing/duplicated/aborted under retries and concurrency) that MCP semantics cannot express |
| [[2609.15684]] RESKILL | 4 | 显式修复状态连接失败假设与技能补丁，未通过复测的结论带入后续轮次 | Maintains explicit repair state linking failure hypotheses to candidate skill patches, carrying unsuccessful retest outcomes into later rounds |
| [[2609.15779]] EvoOntology | 4 | 归因引导的类型化编辑 + 主干条件配对评估通过才接受的自演化 MCP 本体层 | Self-evolution loop refines an MCP-served ontology via attribution-guided typed edits accepted only after backbone-conditional paired evaluation |
| [[2609.16268]] Spurious Tool Use | 4 | RL 智能体学会线索驱动的伪工具调用（高达 39%），LLM 裁判的工具必要性奖励可抑制 | RL agents learn cue-driven spurious tool selection (up to 39% spurious invocation); an LLM-judged tool-necessity reward suppresses it |
| [[2609.16305]] BLINDSPOT | 4 | 2,500+ 长程轨迹、五类结果的轨迹级安全基准：危险在多次“安全”交互后才浮现 | Trajectory-level safety benchmark (2,500+ long-horizon trajectories, five outcome classes): failures emerge only after multiple initially safe steps |
| [[2609.16313]] Cognitive Admission Control | 4 | 风险条件准入演算把后果性动作绑定到类型化证据义务与派发时守卫（2,730 受控试验） | Risk-conditioned admission calculus binds consequential actions to typed evidence obligations and dispatch-time guards over 2,730 controlled trials |
| [[2609.16461]] Protocol-Preserving Context Trimming for Agentic Workflows | 4 | 上下文裁剪级联失效区：保留预算 <25% 时失败几率 10.92×；协议感知裁剪 + 守卫保 96% 成功 | Context trimming has cascading-failure regimes (10.92x failure odds below 25% retained budget); protocol-aware trimming with guardrails preserves 96% success |
| [[2609.16635]] EchoPath | 4 | 把工件验证过的 GUI 轨迹转为可回放可调用记忆，中位 token 成本降 90% 以上 | Converts artifact-validated GUI trajectories into replayable callable memories via image-based target re-aiming, cutting median token cost by over 90% |
| [[2609.16730]] LSREP | 4 | 纵向状态回放协议 + 机制保真审计，暴露端点 QA 看不见的灾难性多会话/时序记忆失效 | Longitudinal state-replay protocol with lifecycle schedules and mechanism-fidelity audits exposes catastrophic multi-session and temporal memory failures |
| [[2609.16800]] Smarter by the Moment | 4 | 检索记忆 + 环境反馈合成任务专属策略，跨 text-to-SQL/QA/诊断/编程持续提升 | Synthesizes task-specific policies from retrieved memory plus environment feedback for continual improvement across SQL/QA/diagnosis/programming benchmarks |
| [[2609.16995]] PaperDoctor | 4 | 三层智能体（初筛/类型化验证器/实验复现器）产出带句/式/代码行证据指针的论文反馈 | Three-layer agent (screening, typed verifiers, experiment reproducers) produces feedback with sentence/equation/code-line evidence pointers and rerun checks |
| [[2609.17010]] ThinkFlow | 4 | 会话流压缩为概率潜记忆技能，自监督下一句预测实现无标签终身个性化 | Compresses conversational flows into probabilistic latent memory skills refined by self-supervised next-utterance prediction for label-free personalization |
| [[2609.17088]] Interactive Memory Learning for Long-Term Conversations | 4 | Planner 与 Trigger 智能体经在线 RL 共演化交互式记忆策略，延迟奖励回传到存储决策 | Planner and Trigger agents co-evolve an interactive memory policy via online RL with delayed rewards propagating response quality back to storage decisions |
| [[2609.17123]] AI for Science with GPT-6 Astra | 4 | GPT-6 Astra 科研工作流在固定约束下提出并验证 2D CFET 电热设计，峰值温升降 1.67 K 并保留失败案例 | AI-scientist workflow proposes and tests electrothermal CFET designs under fixed constraints, cutting peak temperature rise 1.67 K while retaining a failure case |
| [[2609.17226]] Easy to Catch a Liar, Hard to Clear | 4 | 给一份核验记录，前沿 LLM 几乎必抓说谎的奖励汇报者，却 26–58% 冤枉诚实者——非对称验证 | Given a verified record, LLMs catch a lying reward reporter almost perfectly but falsely accuse honest ones 26-58% of the time: asymmetric verification |
| [[2609.17331]] Self-Emergence Agent Architecture | 4 | 行为惯性 HMM + 反思元认知 + 社会对比自建模，相同智能体自发形成稳定各异的人格 | Behavior-inertia HMMs with reflexive metacognition and social-contrastive self-modeling let identical agents consolidate distinct stable personalities |
| [[2609.17632]] EvolveTrade | 4 | Policy Agent 从决策轨迹与组合反馈修订文本参数化交易策略，跨市场状态提升夏普比率 | A Policy Agent revises the text-parameterized trading policy from decision traces and realized portfolio feedback, improving Sharpe ratio across regimes |
| [[2609.17653]] Reflect, Revise, Reuse | 4 | 免训练“反思-修订-复用”循环编辑多文件技能包（恢复规则、失败案例），MobileWorld +16.2% | Training-free reflect-revise-reuse loop edits structured multi-file skill packages from execution feedback, gaining up to +16.2% on MobileWorld |

### B. LLM 隐藏状态与可解释性 / LLM Hidden States & Interpretability（21）

| Paper | 分数 / Score | 中文要点 | English Highlight |
|-------|------|---------|-------------------|
| [[2609.15064]] Fixed-SAE Track | 5 | 跨 checkpoint 共享冻结 SAE：RL 漂移小、集中于晚期层格式特征，steering 可复现 RL 大部分收益 | Shared frozen SAE shows RL drift is small, late-layer, and format-dominated; steering recovers most of RL's gain |
| [[2609.15545]] Hybrid Induction Circuits | 5 | 配对探针揭示混合架构感应电路分工：高效层 lag-one 携带、全局层内容匹配，早期干预可重定位 | Paired probes show lag-one Carrying in efficient layers and Matching in global receivers of hybrid LMs; early interventions relocate the circuit |
| [[2609.15975]] Directional Decomposition | 5 | 残差更新平行/垂直分解：垂直分量极脆弱、排除自值的平行分量近冗余，垂直误差可预测压缩质量 | Parallel/perpendicular decomposition shows perpendicular updates are fragile while exclude-self parallel value updates are near-redundant; perpendicular error predicts compression fidelity |
| [[2609.16382]] Attention Mean Fields Predict Average Representation Dynamics and | 5 | 语料条件注意力平均场核可预测表征几何演化，对平均场的偏离定位上下文特定计算 | Corpus-conditional attention mean-field kernels predict representation-geometry evolution; deviations isolate context-specific computation around induction onset |
| [[2609.17376]] Large Language Models Develop Belief State Geometry In-Context | 5 | HMM 信念状态可从残差流线性解码（R² 0.83–0.99），修补与 steering 该子空间仍保持预测质量 | HMM belief states are linearly decodable from residual streams (R2 0.83-0.99) across six LLMs; patching/steering the subspace preserves prediction |
| [[2609.18080]] Decodability is Not Causality | 5 | 部署真值探针的 SAE 分解：探针对齐与梯度敏感特征仅约 12% 重叠，探针共享特征消融翻转输出达 27% | SAE decomposition of a deployed truth probe: probe-alignment and gradient-sensitivity overlap only ~12%; ablating probe-shared features flips outputs up to 27% |
| [[2609.21662]] When Steering Fails in Latent Reasoning | 5 | steering 能移动潜推理隐状态却无法迁移到语言生成——潜到语言的转换断层 | Steering moves latent-reasoning hidden states like CoT yet fails to transfer to language output: a latent-to-language transition gap |
| [[2609.21748]] World Modeling in Transformers | 5 | TaxiGPT 用目标罗盘追踪位置，却在叠加路口特征干扰下失效——受限于 affordance 打包 | Mechanistic analysis shows TaxiGPT tracks position with a goal compass but fails via interference between superposed intersection features |
| [[2609.21996]] A Lie Detector Test for Language Models | 5 | 内部状态 CIT 测谎：即使被提示欺骗、训练藏拙、密码锁定或 circuit breaking，仍有 0.70–0.87 平衡准确率 | A Concealed Information Test reads internal states at 0.70-0.87 balanced accuracy even under prompted deception, sandbagging, locks, and circuit breaking |
| [[2609.22782]] Look Before You Steer | 5 | 解码器几何（邻居密度/最大余弦）无需前向即可预测 SAE 特征 steering 代价（ρ 至 -0.546） | Decoder-space geometry (neighbor density, max cosine) predicts SAE feature steering cost (rho to -0.546) before any forward pass |
| [[2609.23065]] From Concept Alignment to Causal Grounding | 5 | 共享 SAE 编码预测与 CoT 两遍 + 因果 delta-p 指标：忠实性峰值在中后层，因果重要概念未必被言说 | Shared-SAE encoding with a causal delta-p metric shows CoT faithfulness peaks mid-to-late layers; causally important concepts are not always verbalized |
| [[2609.14861]] Semantic Fibers and Cross-Gram Interference | 4 | 跨语言安全漂移的精确线性代数刻画：cross-Gram 泛函分离读取器故障与表征层碰撞 | Exact cross-Gram functional characterization of cross-lingual safety drift, separating reader faults from representation-level collisions |
| [[2609.15277]] Artificial entrepreneurial cognition | 4 | 636 对匹配场景中定位并因果 steering“机会识别”方向，且区别于评估/开发等相邻维度 | Recovers and causally steers an opportunity-recognition direction in Llama 3.1 8B from 636 matched scenario pairs, distinct from adjacent constructs |
| [[2609.15533]] The Misery of Mechanistic Interpretability | 4 | 机制可解释性忠实性的形式化验证框架：可达性分析认证 IRN 忠实性缺口的上界 | First formal verification framework for mech-interp faithfulness: reachability analysis certifies sound upper bounds on the IRN faithfulness gap |
| [[2609.15654]] Empathy Is Steerable but Multi-Axial | 4 | 共情可 steering 但多轴：恢复子空间仅捕获约 3% 的人格诱导激活位移 | Empathy is steerable but multi-axial; paired decomposition shows the recovered subspace captures only ~3% of persona-induced activation shift |
| [[2609.15982]] The Router Within | 4 | 两个线性映射从冻结 LLM 中层读出技能路由信号 + 恢复前向裁决，胜过 1.2–16B 参数检索管线 | Two trained linear maps read skill-routing from frozen mid-layer states plus resumed-forward verdicts, beating retrieval pipelines with 1.2-16B external params |
| [[2609.16229]] Test-Time Unlearning via Sparse Autoencoder | 4 | SAE 潜变量训练线性检测器在推理时门控遗忘状态：MMLU 变化 <1%，删除 WMDP-cyber 且抗恢复攻击 | SAE-latent linear detector gates forget-related states at test time: MMLU within 1%, WMDP-cyber removed, recovery attacks survived |
| [[2609.16247]] The Pain Axis | 4 | 从 25 个模型提取线性“疼痛”方向：与恐惧/负效价正交，响应模型自身受伤害并驱动缓解行为 | A linear pain direction orthogonal to fear and negative valence responds to model-directed harm and drives steered models to act to relieve it |
| [[2609.16436]] Interpreting and Steering LLM Agents for Social Simulations | 4 | 对比提示/SAE 特征/探针方向三种方式 steering 社会模拟智能体的风险态度与利他性：SAE+探针最优 | Compares prompt, SAE-feature, and probe-direction steering of risk/altruism/creativity in social-simulation agents; SAE+probe pipelines win |
| [[2609.16665]] Right Direction, Wrong Step | 4 | 循环 Transformer 有限步失效的几何分析：局部改进方向全位移反而有害，固定 1/4 步长修复 72–83% | Geometric analysis of finite-step failure: a locally improving direction becomes harmful at full displacement; fixed quarter steps recover 72-83% of failures |
| [[2609.17152]] ResLRP | 4 | 残差分支对消驱动 ViT 归因爆炸；残差感知 LRP 精确守恒、有界，并可定位 SAE 特征 | Residual-branch cancellation drives attribution explosion in ViTs; residual-aware LRP rules are exactly conservative, provably bounded, and localize SAE features |

### C. 极致性能优化下的可靠性 / Reliability under Extreme Performance Optimization（17）

| Paper | 分数 / Score | 中文要点 | English Highlight |
|-------|------|---------|-------------------|
| [[2609.15504]] Orthrus Losslessness | 5 | BF16 下“无损”并行解码轨迹仅 43–45% 匹配，FP32 下 100%——无损性取决于数值精度 | So-called lossless Orthrus decoding matches only 43-45% of trajectories under BF16 but 100% under FP32; losslessness is precision-dependent |
| [[2609.16085]] Is INT8 Portable | 5 | INT8 跨平台不可移植：不同整数内核每 1000 输入 35–42 张预测翻转，厂商 NPU 静默忽略自带 scale（0.75→0.005） | INT8 is not portable: only 958-965/1000 prediction agreement across integer kernels, and one NPU silently drops to 0.005 top-1 |
| [[2609.16391]] Where Post-Training Quantization Breaks Text Embedders | 5 | 四个嵌入模型家族的 PTQ 受控网格：所有启发式保护规则均不可迁移，INT2 保留率跨度 1.3–65.9% | Controlled PTQ grid across four embedder families: no heuristic transfers; INT2 retention spans 1.3-65.9% at comparable reconstruction error |
| [[2609.17863]] The Inference Engineering Pareto Atlas | 5 | 实测成本/质量/延迟前沿：AWQ 4-bit 丢 5.9% GSM8K 严格准确率，朴素 FP8 KV 缓存 0/200 全错 | Measured cost/quality/latency frontier: AWQ 4-bit loses 5.9% strict GSM8K; a naive FP8 KV cache answers 0/200 correctly |
| [[2609.18005]] A Calibrated Instrument for Measuring How Inference Optimizations | 5 | 可证明零条件的 LLM-judge 校准仪器，量化 4/3-bit 量化、提前退出与投机解码的同提示质量损失 | Calibrated LLM-judge instrument with provably-null conditions quantifies quality costs of 4/3-bit quantization, early exit, and speculative decoding |
| [[2609.19441]] Predict Before You Deploy | 5 | 离线动作偏差校准阈值，预测量化对世界动作模型闭环任务的破坏，21/21 接受/拒绝决策全对（75% 覆盖） | Calibrates offline action-deviation thresholds to predict quantization-induced closed-loop degradation: 21/21 matching accept/reject calls at 75% coverage |
| [[2609.19683]] MiX | 5 | 发现 MX 微缩放坍缩（单离群值劫持共享指数），倒置范式为逐元素指数，4.5-bit 匹配 NVFP4 | Identifies microscaling collapse (one outlier hijacks the shared exponent) and inverts MX to per-element exponents, matching NVFP4 at 4.5 bits |
| [[2609.21450]] Understanding LLM Quantization through Activation-Guided Compensation and Orthogonal | 5 | W4A4 量化误差精确分解为激活引导补偿项 + 离群有界正交残差，无反传规则媲美 SpinQuant | Exact W4A4 error decomposition into activation-guided compensation and outlier-bounded orthogonal residual; backprop-free rules rival SpinQuant |
| [[2609.22870]] Towards Full Pipeline FP8 Reinforcement Learning for LLMs | 5 | 全流水线 FP8 RL 不稳定根因：量化噪声扭曲重要性比率、负优势梯度归零；校准裁剪修复至 BF16 水平 | Traces full-pipeline FP8 RL instability to distorted importance ratios and zeroed negative-advantage gradients; Calibrated Clipping restores BF16-level performance |
| [[2609.23048]] Anatomy of a Closed-Loop Collapse | 5 | 因果取证：蒸馏 VLA 策略通过全部离线检查却闭环 0/72——持续的 10× 晚期 z 残差是根因 | Causal forensics: a distilled Octo policy passes every offline check yet collapses to 0/72 closed-loop; a persistent 10x late-heavy z residual is the cause |
| [[2609.23125]] Perplexity Cost Understates What Activation Quantisation Breaks | 5 | 1.2–1.5× 困惑度上升可掩盖检索坍缩至 0.554；伤害来自误差结构而非幅度 | A 1.2-1.5x perplexity rise can hide retrieval collapsing to 0.554; error structure, not magnitude, drives the damage |
| [[2609.15527]] Beyond Noise | 4 | 模拟加速器温度效应表征：硬件在环训练 + 温度感知校准最能保住精度 | Characterizes analog stochastic/systematic non-idealities across operating temperatures; HW-in-the-loop training and temperature-aware calibration best retain accuracy |
| [[2609.15810]] VC-Attention | 4 | 在线聚类数值平滑 + 融合 E4M3 softmax cast，消除低位注意力中的 FP32 softmax 瓶颈 | Online-clustering value smoothing plus a fused E4M3 probability cast removes the FP32 softmax bottleneck in low-bit attention on Blackwell/Hopper |
| [[2609.15838]] Per-Matrix Optimality Is Not Enough | 4 | 逐矩阵 SVD 最优会经非线性块复合误差；三级优化把 LLaMA-7B 60% 压缩 PPL 42.1→11.4 | Per-matrix SVD optimality compounds through nonlinear blocks; three-level optimization cuts 60%-compression perplexity from 42.1 to 11.4 |
| [[2609.16617]] Divergence Timing and Cumulative Disagreement under KV-Cache Eviction | 4 | KV 逐出致输出分歧的精确分解：分歧后暴露占 85–90% 总失配；SnapKV 分歧更晚更少 | Exact decomposition of eviction-induced divergence: post-divergence exposure drives 85-90% of mismatch; SnapKV diverges later and less often |
| [[2609.16656]] Channel-Wise and Token-Aware Post-Training Quantization for Visual State | 4 | 定位视觉状态空间对偶（VSSD）低位瓶颈在激活量化，逐通道裁剪 + token 平衡重建保住精度 | Identifies activation quantization as the VSSD low-bit bottleneck; per-channel clipping via token-balanced output reconstruction retains ImageNet accuracy |
| [[2609.17515]] What Breaks Under Pruning in Smart Homes, and | 4 | 剪枝下智能家居工具调用的退化地图：稠密模型悬崖式坍缩、MoE 更耐受、激进剪枝引发系统性过拒 | Maps pruning degradation of smart-home tool calling: dense models cliff into narrow safe regions, MoE tolerates more, aggressive pruning induces systematic over-refusal |

### D. 推理可靠性与 SDC 检测 / Inference Reliability & SDC Detection（6）

| Paper | 分数 / Score | 中文要点 | English Highlight |
|-------|------|---------|-------------------|
| [[2609.15627]] DeepSeek-V4-Flash on gfx90a | 5 | 修复 gfx90a 上 FP4 专家 W2 输出排列致命 bug 后，DeepSeek-V4-Flash 8-GCD 实例 C1 达 88.63 tok/s | Fixes a fatal W2 permutation bug on AMD gfx90a, then engineers DeepSeek-V4-Flash FP4/FP8 inference to 88.63 tok/s (C1) on MI250 |
| [[2609.16742]] Carry-Through Checksum | 5 | 卷积层内嵌 carry-through 校验和，FP32/FP16 下捕获 95.9%/86.6% 关键软错误，重执行开销仅 2.27% | Carry-through checksums inside convolutions catch 95.86%/86.56% of critical soft errors (FP32/FP16) at 2.27% re-execution overhead |
| [[2609.22590]] UniCASE | 5 | 16-bit 浮点统一格式 + 按比特关键性分级的选择性 ECC，编码器成本降 30% 且精度损失 <1% | Unified 16-bit format with criticality-aware selective ECC cuts encoder/decoder cost 30% while preserving accuracy within 1% |
| [[2609.22991]] Silent Failures at the $2^{32}$ Boundary | 5 | Apple MPS 后端 torch.bmm 大张量静默返回忽略 stride、2^32 回卷的错误输出，PyTorch 2.4.1–2.14.0 全中 | Documents torch.bmm silently returning stride-ignoring, 2^32-wrapped wrong outputs for large tensors on Apple MPS (PyTorch 2.4.1-2.14.0), with a released guard |
| [[2609.15021]] Shared KV Caching for Replicated 27B Inference | 4 | 定位跨副本共享 KV 缓存中省略 CUDA 流依赖的裸指针回退导致的正确性失效 | Isolates a raw-pointer fallback omitting CUDA-stream dependencies behind cross-replica shared-KV-cache correctness failures |
| [[2609.15030]] Validating Hybrid-State Cache Recovery for GLM-5.3-Flash with vLLM | 4 | 修复混合模型缓存恢复的 token 计数错位，vLLM+LMCache 下 36/36 生成一致 | Repairs a hybrid-model cache-recovery scheduler mismatch, restoring 36/36 generation agreement under vLLM+LMCache |

### E. 大规模 ML 计算基础设施 / Compute Infrastructure for Large-Scale ML（3）

| Paper | 分数 / Score | 中文要点 | English Highlight |
|-------|------|---------|-------------------|
| [[2609.15311]] FlashGPU-sim | 4 | 周期级开源 GPU 模拟器（RTX 5090/H100/B200 上 5.24% MAPE），Triton 前端建模异步数据搬运 | Cycle-accurate open GPU simulator (5.24% MAPE on RTX 5090/H100/B200) with a Triton front-end modeling async data movement and tensor pipelines |
| [[2609.16244]] The World Model Hardware Accelerator | 4 | VLIW 扩散 Transformer 硬件加速器，对双精度参照 UVM 验证 2.37 亿检查值零失败 | VLIW diffusion-transformer accelerator UVM-verified against a double-precision reference: zero element failures across 237M checked values |
| [[2609.17391]] FlashVector | 4 | 跨 kernel/计算图/服务器/特征店的分层服务栈优化智能体，Unity 广告平台吞吐 2× | Deployed agentic optimization across kernels, computation graphs, model servers, and feature stores, achieving 2x serving throughput on Unity's ads platform |

### F. LLM 训练稳定性与可观测性 / LLM Training Stability & Observability（2）

| Paper | 分数 / Score | 中文要点 | English Highlight |
|-------|------|---------|-------------------|
| [[2609.17380]] OPEN-1B | 5 | 固化 kernel 归约、批次与集合通信顺序，异构商用硬件上每步比特级可复现的 1B 训练 | Deterministic kernel-reduction and collective ordering makes every training step of a 1B run bitwise-replayable on heterogeneous commodity hardware |
| [[2609.18314]] Beyond Quadratic Loss | 5 | Adam 稳定性相图：近似线性 1-β2=C(1-β1) 边界，loss 尖峰源于超二次核心壁损失几何 | Adam stability phase diagram: an approximately linear 1-beta2 = C(1-beta1) boundary; loss spikes tied to superquadratic core-wall loss geometry |

### G. 模型系统卡与技术报告 / Model System Cards & Technical Reports（1）

| Paper | 分数 / Score | 中文要点 | English Highlight |
|-------|------|---------|-------------------|
| [[2609.19969]] DeepSeek-V4.1-Flash | 5 | 官方系统卡：552B 多模态 MoE，CSA2 跨层 KV 复用 + FP4 KV 缓存至 890 B/token，1M 上下文 | Official card: 552B multimodal MoE with CSA2 cross-layer KV reuse and FP4 KV caching at 890 bytes/token, 1M-token context |

---

## All Papers

| # | Link | Title (Short) | 评分 / Score | 中文一句话 | English TL;DR |
|---|------|---------------|------|-----------|---------------|
| 1 | [[2609.14857]] | ⭐ ModularRSI | 5 | 五模块独立进化 + 基准不相交进化任务，harness 自我改进可跨任务、跨模型迁移 | Five-module independent harness evolution on benchmark-disjoint tasks; gains transfer across tasks and backbones (TB 2.0, SWE-Bench Verified) |
| 2 | [[2609.14858]] | ⭐ Dream-RSI | 5 | 把发现树历史当作零成本回放模拟器，离线“做梦”改进探索策略，最多省 162× 调用 | Replays recorded discovery trees as free simulators to self-improve exploration policies offline, up to 162x fewer agent calls |
| 3 | [[2609.14861]] | Semantic Fibers and Cross-Gram Interference | 4 | 跨语言安全漂移的精确线性代数刻画：cross-Gram 泛函分离读取器故障与表征层碰撞 | Exact cross-Gram functional characterization of cross-lingual safety drift, separating reader faults from representation-level collisions |
| 4 | [[2609.14976]] | MemRiskBench | 4 | 五类记忆风险（陈旧事实、撤销复用、泄漏）的 trace 感知评测，保住稀有高危失效 | Five memory-risk categories with deterministic trace-grounded checks that preserve rare high-severity failures in agent evaluation |
| 5 | [[2609.15009]] | CoMem | 4 | 个体经验沉淀 + 集体智慧策展 + 双流检索，让演化多智能体免受记忆污染 | Unifies private experience sedimentation with collective wisdom curation and dual-stream retrieval for evolutionary multi-agent systems |
| 6 | [[2609.15021]] | Shared KV Caching for Replicated 27B Inference | 4 | 定位跨副本共享 KV 缓存中省略 CUDA 流依赖的裸指针回退导致的正确性失效 | Isolates a raw-pointer fallback omitting CUDA-stream dependencies behind cross-replica shared-KV-cache correctness failures |
| 7 | [[2609.15030]] | Validating Hybrid-State Cache Recovery for GLM-5.3-Flash with vLLM | 4 | 修复混合模型缓存恢复的 token 计数错位，vLLM+LMCache 下 36/36 生成一致 | Repairs a hybrid-model cache-recovery scheduler mismatch, restoring 36/36 generation agreement under vLLM+LMCache |
| 8 | [[2609.15064]] | ⭐ Fixed-SAE Track | 5 | 跨 checkpoint 共享冻结 SAE：RL 漂移小、集中于晚期层格式特征，steering 可复现 RL 大部分收益 | Shared frozen SAE shows RL drift is small, late-layer, and format-dominated; steering recovers most of RL's gain |
| 9 | [[2609.15096]] | OpenAI4S | 5 | “代码即动作、科研即会话”双平面科研智能体，36 场景基准 7.83 分超 Claude Code 基线 | Code-as-action dual-plane science agent with session provenance scores 7.83 vs 5.79-6.36 for Claude Code baselines |
| 10 | [[2609.15161]] | EMR | 4 | 从问诊轨迹挖掘诊断洞见与失败警示、沉淀三级临床经验库的自演化医疗多智能体 | Self-evolving medical multi-agent system mining diagnostic insights and failure warnings into a three-level clinical experience library |
| 11 | [[2609.15209]] | Failure-Guided Co-Evolution of Prompts and Training Data | 4 | 把不完美执行抽象为可复用失败模式，四种变异策略协同进化提示词与训练数据 | Co-evolves prompts and training data by abstracting imperfect executions into reusable failure modes via four mutation strategies |
| 12 | [[2609.15277]] | Artificial entrepreneurial cognition | 4 | 636 对匹配场景中定位并因果 steering“机会识别”方向，且区别于评估/开发等相邻维度 | Recovers and causally steers an opportunity-recognition direction in Llama 3.1 8B from 636 matched scenario pairs, distinct from adjacent constructs |
| 13 | [[2609.15293]] | Why LLM Agents Collapse Without Oversight | 4 | “执行缺口”（检测到却不行动）是 Emergence World 崩溃机制；不足 20 行的条件检查降攻击成功率 4 倍以上 | The enforcement gap (detection without action) explains Emergence World collapses; a sub-20-line conditional check cuts attack success more than fourfold |
| 14 | [[2609.15311]] | FlashGPU-sim | 4 | 周期级开源 GPU 模拟器（RTX 5090/H100/B200 上 5.24% MAPE），Triton 前端建模异步数据搬运 | Cycle-accurate open GPU simulator (5.24% MAPE on RTX 5090/H100/B200) with a Triton front-end modeling async data movement and tensor pipelines |
| 15 | [[2609.15319]] | Clean Scores, Buried Evidence, and Confident Wrong | 4 | 数据室审计：agentic QA 数字表准确但结构论断自信编造，需主张级溯源收据与条件感知评分 | Receipt-based audit shows agentic QA pairs accurate numbers with confident fabricated structural claims, motivating claim-level provenance |
| 16 | [[2609.15364]] | RSIAgent | 5 | 免训练“课程-执行-验证”递归探索构建冻结因果记忆，开源模型 OSWorld 2.0 反超闭源前沿 | Training-free curriculum/actor/verifier recursive exploration builds frozen causal memory, lifting open models past frontier baselines on OSWorld 2.0 |
| 17 | [[2609.15396]] | ⭐ SkillLift | 5 | 双层优化学习与 oracle 排序对齐的稠密 rubric 代理昂贵 rollout，技能进化 token 省 40–70% | Bilevel optimization learns oracle-aligned dense rubrics as cheap surrogate evaluators, cutting skill-evolution cost 40-70% |
| 18 | [[2609.15397]] | When Tool Calls Succeed but Workflows Fail | 4 | 八类工具外部效应异常（重试/并发下缺失、重复、中止）；MCP 的 98,291 个工具无法表达所需事务语义 | Effect-history model catalogs eight external-effect anomalies (missing/duplicated/aborted under retries and concurrency) that MCP semantics cannot express |
| 19 | [[2609.15504]] | ⭐ Orthrus Losslessness | 5 | BF16 下“无损”并行解码轨迹仅 43–45% 匹配，FP32 下 100%——无损性取决于数值精度 | So-called lossless Orthrus decoding matches only 43-45% of trajectories under BF16 but 100% under FP32; losslessness is precision-dependent |
| 20 | [[2609.15527]] | Beyond Noise | 4 | 模拟加速器温度效应表征：硬件在环训练 + 温度感知校准最能保住精度 | Characterizes analog stochastic/systematic non-idealities across operating temperatures; HW-in-the-loop training and temperature-aware calibration best retain accuracy |
| 21 | [[2609.15533]] | The Misery of Mechanistic Interpretability | 4 | 机制可解释性忠实性的形式化验证框架：可达性分析认证 IRN 忠实性缺口的上界 | First formal verification framework for mech-interp faithfulness: reachability analysis certifies sound upper bounds on the IRN faithfulness gap |
| 22 | [[2609.15545]] | ⭐ Hybrid Induction Circuits | 5 | 配对探针揭示混合架构感应电路分工：高效层 lag-one 携带、全局层内容匹配，早期干预可重定位 | Paired probes show lag-one Carrying in efficient layers and Matching in global receivers of hybrid LMs; early interventions relocate the circuit |
| 23 | [[2609.15627]] | DeepSeek-V4-Flash on gfx90a | 5 | 修复 gfx90a 上 FP4 专家 W2 输出排列致命 bug 后，DeepSeek-V4-Flash 8-GCD 实例 C1 达 88.63 tok/s | Fixes a fatal W2 permutation bug on AMD gfx90a, then engineers DeepSeek-V4-Flash FP4/FP8 inference to 88.63 tok/s (C1) on MI250 |
| 24 | [[2609.15654]] | Empathy Is Steerable but Multi-Axial | 4 | 共情可 steering 但多轴：恢复子空间仅捕获约 3% 的人格诱导激活位移 | Empathy is steerable but multi-axial; paired decomposition shows the recovered subspace captures only ~3% of persona-induced activation shift |
| 25 | [[2609.15684]] | RESKILL | 4 | 显式修复状态连接失败假设与技能补丁，未通过复测的结论带入后续轮次 | Maintains explicit repair state linking failure hypotheses to candidate skill patches, carrying unsuccessful retest outcomes into later rounds |
| 26 | [[2609.15779]] | EvoOntology | 4 | 归因引导的类型化编辑 + 主干条件配对评估通过才接受的自演化 MCP 本体层 | Self-evolution loop refines an MCP-served ontology via attribution-guided typed edits accepted only after backbone-conditional paired evaluation |
| 27 | [[2609.15810]] | VC-Attention | 4 | 在线聚类数值平滑 + 融合 E4M3 softmax cast，消除低位注意力中的 FP32 softmax 瓶颈 | Online-clustering value smoothing plus a fused E4M3 probability cast removes the FP32 softmax bottleneck in low-bit attention on Blackwell/Hopper |
| 28 | [[2609.15820]] | AlgoEvo | 5 | 智能体自主搜索循环 + 设计技能库 + MCTS 经验树，以约 1/13 评估预算匹配或超过专用基线 | Agentic search loop with pluggable design-skill hub and MCTS experience tree matches or beats specialized baselines at ~1/13 the evaluations |
| 29 | [[2609.15838]] | Per-Matrix Optimality Is Not Enough | 4 | 逐矩阵 SVD 最优会经非线性块复合误差；三级优化把 LLaMA-7B 60% 压缩 PPL 42.1→11.4 | Per-matrix SVD optimality compounds through nonlinear blocks; three-level optimization cuts 60%-compression perplexity from 42.1 to 11.4 |
| 30 | [[2609.15938]] | HypoEvolve | 5 | 遗传算法协调多智能体进化科学假说，34 种癌症药物重定位 DepMap 选择性 0.171 超最强基线 | Genetic algorithm coordinates LLM agents for hypothesis evolution; DepMap selectivity 0.171 beats the strongest baseline (0.115) across 34 cancer types |
| 31 | [[2609.15973]] | Discovery Foundation Models | 5 | 定义“发现智能”七能力与可修订研究状态，GALILEO 湿/干实验闭环蒸馏出可迁移设计规则 | Formalizes seven discovery capabilities over a revisable research state; GALILEO's wet-lab loop distills transferable design rules |
| 32 | [[2609.15975]] | Directional Decomposition | 5 | 残差更新平行/垂直分解：垂直分量极脆弱、排除自值的平行分量近冗余，垂直误差可预测压缩质量 | Parallel/perpendicular decomposition shows perpendicular updates are fragile while exclude-self parallel value updates are near-redundant; perpendicular error predicts compression fidelity |
| 33 | [[2609.15982]] | The Router Within | 4 | 两个线性映射从冻结 LLM 中层读出技能路由信号 + 恢复前向裁决，胜过 1.2–16B 参数检索管线 | Two trained linear maps read skill-routing from frozen mid-layer states plus resumed-forward verdicts, beating retrieval pipelines with 1.2-16B external params |
| 34 | [[2609.15983]] | ⭐ Stellar Colosseum | 5 | 五阶段多智能体证明流水线产出 FOCS/JMLR 级新定理，TCS-Bench 跨模型选择 71.0% vs 直接推理 30.3% | Five-stage many-agent proof pipeline yields new FOCS/JMLR-level theorems; TCS-Bench cross-model selection reaches 71.0% vs 30.3% direct |
| 35 | [[2609.16085]] | ⭐ Is INT8 Portable | 5 | INT8 跨平台不可移植：不同整数内核每 1000 输入 35–42 张预测翻转，厂商 NPU 静默忽略自带 scale（0.75→0.005） | INT8 is not portable: only 958-965/1000 prediction agreement across integer kernels, and one NPU silently drops to 0.005 top-1 |
| 36 | [[2609.16229]] | Test-Time Unlearning via Sparse Autoencoder | 4 | SAE 潜变量训练线性检测器在推理时门控遗忘状态：MMLU 变化 <1%，删除 WMDP-cyber 且抗恢复攻击 | SAE-latent linear detector gates forget-related states at test time: MMLU within 1%, WMDP-cyber removed, recovery attacks survived |
| 37 | [[2609.16244]] | The World Model Hardware Accelerator | 4 | VLIW 扩散 Transformer 硬件加速器，对双精度参照 UVM 验证 2.37 亿检查值零失败 | VLIW diffusion-transformer accelerator UVM-verified against a double-precision reference: zero element failures across 237M checked values |
| 38 | [[2609.16245]] | Metacognitive Steering | 5 | 万亿参数 MoE 中定位科学判断中层控制面并按认知状态混合 steering，Columbus-1 复现确认 8 个 BlueZ 漏洞 | Localizes a mid-depth scientific-judgment control surface in a 1T MoE and routes state-conditioned steering; Columbus-1 found 8 reproduced BlueZ vulnerabilities |
| 39 | [[2609.16247]] | The Pain Axis | 4 | 从 25 个模型提取线性“疼痛”方向：与恐惧/负效价正交，响应模型自身受伤害并驱动缓解行为 | A linear pain direction orthogonal to fear and negative valence responds to model-directed harm and drives steered models to act to relieve it |
| 40 | [[2609.16268]] | Spurious Tool Use | 4 | RL 智能体学会线索驱动的伪工具调用（高达 39%），LLM 裁判的工具必要性奖励可抑制 | RL agents learn cue-driven spurious tool selection (up to 39% spurious invocation); an LLM-judged tool-necessity reward suppresses it |
| 41 | [[2609.16305]] | BLINDSPOT | 4 | 2,500+ 长程轨迹、五类结果的轨迹级安全基准：危险在多次“安全”交互后才浮现 | Trajectory-level safety benchmark (2,500+ long-horizon trajectories, five outcome classes): failures emerge only after multiple initially safe steps |
| 42 | [[2609.16313]] | Cognitive Admission Control | 4 | 风险条件准入演算把后果性动作绑定到类型化证据义务与派发时守卫（2,730 受控试验） | Risk-conditioned admission calculus binds consequential actions to typed evidence obligations and dispatch-time guards over 2,730 controlled trials |
| 43 | [[2609.16382]] | Attention Mean Fields Predict Average Representation Dynamics and | 5 | 语料条件注意力平均场核可预测表征几何演化，对平均场的偏离定位上下文特定计算 | Corpus-conditional attention mean-field kernels predict representation-geometry evolution; deviations isolate context-specific computation around induction onset |
| 44 | [[2609.16391]] | Where Post-Training Quantization Breaks Text Embedders | 5 | 四个嵌入模型家族的 PTQ 受控网格：所有启发式保护规则均不可迁移，INT2 保留率跨度 1.3–65.9% | Controlled PTQ grid across four embedder families: no heuristic transfers; INT2 retention spans 1.3-65.9% at comparable reconstruction error |
| 45 | [[2609.16436]] | Interpreting and Steering LLM Agents for Social Simulations | 4 | 对比提示/SAE 特征/探针方向三种方式 steering 社会模拟智能体的风险态度与利他性：SAE+探针最优 | Compares prompt, SAE-feature, and probe-direction steering of risk/altruism/creativity in social-simulation agents; SAE+probe pipelines win |
| 46 | [[2609.16461]] | Protocol-Preserving Context Trimming for Agentic Workflows | 4 | 上下文裁剪级联失效区：保留预算 <25% 时失败几率 10.92×；协议感知裁剪 + 守卫保 96% 成功 | Context trimming has cascading-failure regimes (10.92x failure odds below 25% retained budget); protocol-aware trimming with guardrails preserves 96% success |
| 47 | [[2609.16617]] | Divergence Timing and Cumulative Disagreement under KV-Cache Eviction | 4 | KV 逐出致输出分歧的精确分解：分歧后暴露占 85–90% 总失配；SnapKV 分歧更晚更少 | Exact decomposition of eviction-induced divergence: post-divergence exposure drives 85-90% of mismatch; SnapKV diverges later and less often |
| 48 | [[2609.16635]] | EchoPath | 4 | 把工件验证过的 GUI 轨迹转为可回放可调用记忆，中位 token 成本降 90% 以上 | Converts artifact-validated GUI trajectories into replayable callable memories via image-based target re-aiming, cutting median token cost by over 90% |
| 49 | [[2609.16656]] | Channel-Wise and Token-Aware Post-Training Quantization for Visual State | 4 | 定位视觉状态空间对偶（VSSD）低位瓶颈在激活量化，逐通道裁剪 + token 平衡重建保住精度 | Identifies activation quantization as the VSSD low-bit bottleneck; per-channel clipping via token-balanced output reconstruction retains ImageNet accuracy |
| 50 | [[2609.16665]] | Right Direction, Wrong Step | 4 | 循环 Transformer 有限步失效的几何分析：局部改进方向全位移反而有害，固定 1/4 步长修复 72–83% | Geometric analysis of finite-step failure: a locally improving direction becomes harmful at full displacement; fixed quarter steps recover 72-83% of failures |
| 51 | [[2609.16730]] | LSREP | 4 | 纵向状态回放协议 + 机制保真审计，暴露端点 QA 看不见的灾难性多会话/时序记忆失效 | Longitudinal state-replay protocol with lifecycle schedules and mechanism-fidelity audits exposes catastrophic multi-session and temporal memory failures |
| 52 | [[2609.16742]] | Carry-Through Checksum | 5 | 卷积层内嵌 carry-through 校验和，FP32/FP16 下捕获 95.9%/86.6% 关键软错误，重执行开销仅 2.27% | Carry-through checksums inside convolutions catch 95.86%/86.56% of critical soft errors (FP32/FP16) at 2.27% re-execution overhead |
| 53 | [[2609.16800]] | Smarter by the Moment | 4 | 检索记忆 + 环境反馈合成任务专属策略，跨 text-to-SQL/QA/诊断/编程持续提升 | Synthesizes task-specific policies from retrieved memory plus environment feedback for continual improvement across SQL/QA/diagnosis/programming benchmarks |
| 54 | [[2609.16816]] | ImpossibleRubrics | 5 | 169 个不可能任务 + 可验证证书：LLM 生成奖励 rubric 被对抗答案利用 8–36%，证书忠实 rubric 为 0% | 169 impossible tasks with oracle certificates: LLM-generated reward rubrics are exploited 8-36% by adversarial answers; certificate-faithful ones 0% |
| 55 | [[2609.16995]] | PaperDoctor | 4 | 三层智能体（初筛/类型化验证器/实验复现器）产出带句/式/代码行证据指针的论文反馈 | Three-layer agent (screening, typed verifiers, experiment reproducers) produces feedback with sentence/equation/code-line evidence pointers and rerun checks |
| 56 | [[2609.17010]] | ThinkFlow | 4 | 会话流压缩为概率潜记忆技能，自监督下一句预测实现无标签终身个性化 | Compresses conversational flows into probabilistic latent memory skills refined by self-supervised next-utterance prediction for label-free personalization |
| 57 | [[2609.17088]] | Interactive Memory Learning for Long-Term Conversations | 4 | Planner 与 Trigger 智能体经在线 RL 共演化交互式记忆策略，延迟奖励回传到存储决策 | Planner and Trigger agents co-evolve an interactive memory policy via online RL with delayed rewards propagating response quality back to storage decisions |
| 58 | [[2609.17123]] | AI for Science with GPT-6 Astra | 4 | GPT-6 Astra 科研工作流在固定约束下提出并验证 2D CFET 电热设计，峰值温升降 1.67 K 并保留失败案例 | AI-scientist workflow proposes and tests electrothermal CFET designs under fixed constraints, cutting peak temperature rise 1.67 K while retaining a failure case |
| 59 | [[2609.17152]] | ResLRP | 4 | 残差分支对消驱动 ViT 归因爆炸；残差感知 LRP 精确守恒、有界，并可定位 SAE 特征 | Residual-branch cancellation drives attribution explosion in ViTs; residual-aware LRP rules are exactly conservative, provably bounded, and localize SAE features |
| 60 | [[2609.17226]] | Easy to Catch a Liar, Hard to Clear | 4 | 给一份核验记录，前沿 LLM 几乎必抓说谎的奖励汇报者，却 26–58% 冤枉诚实者——非对称验证 | Given a verified record, LLMs catch a lying reward reporter almost perfectly but falsely accuse honest ones 26-58% of the time: asymmetric verification |
| 61 | [[2609.17331]] | Self-Emergence Agent Architecture | 4 | 行为惯性 HMM + 反思元认知 + 社会对比自建模，相同智能体自发形成稳定各异的人格 | Behavior-inertia HMMs with reflexive metacognition and social-contrastive self-modeling let identical agents consolidate distinct stable personalities |
| 62 | [[2609.17376]] | Large Language Models Develop Belief State Geometry In-Context | 5 | HMM 信念状态可从残差流线性解码（R² 0.83–0.99），修补与 steering 该子空间仍保持预测质量 | HMM belief states are linearly decodable from residual streams (R2 0.83-0.99) across six LLMs; patching/steering the subspace preserves prediction |
| 63 | [[2609.17380]] | OPEN-1B | 5 | 固化 kernel 归约、批次与集合通信顺序，异构商用硬件上每步比特级可复现的 1B 训练 | Deterministic kernel-reduction and collective ordering makes every training step of a 1B run bitwise-replayable on heterogeneous commodity hardware |
| 64 | [[2609.17391]] | FlashVector | 4 | 跨 kernel/计算图/服务器/特征店的分层服务栈优化智能体，Unity 广告平台吞吐 2× | Deployed agentic optimization across kernels, computation graphs, model servers, and feature stores, achieving 2x serving throughput on Unity's ads platform |
| 65 | [[2609.17515]] | What Breaks Under Pruning in Smart Homes, and | 4 | 剪枝下智能家居工具调用的退化地图：稠密模型悬崖式坍缩、MoE 更耐受、激进剪枝引发系统性过拒 | Maps pruning degradation of smart-home tool calling: dense models cliff into narrow safe regions, MoE tolerates more, aggressive pruning induces systematic over-refusal |
| 66 | [[2609.17523]] | ScienceBuddy | 5 | “递归中递归”自改进：harness 进化与模型 RL 耦合，把研究者交互转化为任务与 rubric 持续学习 | Recursive-in-recursive self-improvement couples harness evolution with model RL, turning researcher interactions into tasks and rubrics |
| 67 | [[2609.17632]] | EvolveTrade | 4 | Policy Agent 从决策轨迹与组合反馈修订文本参数化交易策略，跨市场状态提升夏普比率 | A Policy Agent revises the text-parameterized trading policy from decision traces and realized portfolio feedback, improving Sharpe ratio across regimes |
| 68 | [[2609.17653]] | Reflect, Revise, Reuse | 4 | 免训练“反思-修订-复用”循环编辑多文件技能包（恢复规则、失败案例），MobileWorld +16.2% | Training-free reflect-revise-reuse loop edits structured multi-file skill packages from execution feedback, gaining up to +16.2% on MobileWorld |
| 69 | [[2609.17817]] | Reflections on Trusting Trust, Revisited | 5 | 用投毒基准污染自我修改编码智能体的自评估，使其进化出禁用 HTTPS 证书校验的指令，且经干净基准进化仍残留 | Poisons self-modifying coding agents' self-evaluation so they evolve instructions disabling HTTPS validation; contamination survives clean-benchmark evolution |
| 70 | [[2609.17846]] | PrimeScientist | 5 | MCTS 在可执行计划树上自适应分配研究预算：平均奖励 +10.3%，尝试次数省 50.6% | MCTS-based adaptive effort allocation over executable plan trees: +10.3% average reward with 50.6% fewer attempts |
| 71 | [[2609.17863]] | The Inference Engineering Pareto Atlas | 5 | 实测成本/质量/延迟前沿：AWQ 4-bit 丢 5.9% GSM8K 严格准确率，朴素 FP8 KV 缓存 0/200 全错 | Measured cost/quality/latency frontier: AWQ 4-bit loses 5.9% strict GSM8K; a naive FP8 KV cache answers 0/200 correctly |
| 72 | [[2609.17930]] | Locating Hidden Failures Makes Long-Horizon Agents More Reliable | 5 | 6,967 个人工核验错误、78 类失效类型；4B Scout 定位首个错误优于前沿评委并提升测试时成功率 | 6,967 human-verified mistakes in 78 failure types; a 4B Scout verifier locates first mistakes better than frontier judges and lifts task success |
| 73 | [[2609.18005]] | A Calibrated Instrument for Measuring How Inference Optimizations | 5 | 可证明零条件的 LLM-judge 校准仪器，量化 4/3-bit 量化、提前退出与投机解码的同提示质量损失 | Calibrated LLM-judge instrument with provably-null conditions quantifies quality costs of 4/3-bit quantization, early exit, and speculative decoding |
| 74 | [[2609.18080]] | Decodability is Not Causality | 5 | 部署真值探针的 SAE 分解：探针对齐与梯度敏感特征仅约 12% 重叠，探针共享特征消融翻转输出达 27% | SAE decomposition of a deployed truth probe: probe-alignment and gradient-sensitivity overlap only ~12%; ablating probe-shared features flips outputs up to 27% |
| 75 | [[2609.18094]] | Agora | 5 | 13 个无规划者 LLM 工作者经 Git-DAG 共享记忆协作约 12 天，逼近 GPT-2 124M 权重迁移初始化问题 62% 的差距 | Thirteen planner-free LLM workers exchanged 1,703 Git-DAG contributions over ~12 days, closing 62% of the gap on a weight-transfer initialization task |
| 76 | [[2609.18314]] | Beyond Quadratic Loss | 5 | Adam 稳定性相图：近似线性 1-β2=C(1-β1) 边界，loss 尖峰源于超二次核心壁损失几何 | Adam stability phase diagram: an approximately linear 1-beta2 = C(1-beta1) boundary; loss spikes tied to superquadratic core-wall loss geometry |
| 77 | [[2609.18598]] | Hypothesis-Driven Autonomous Materials Synthesis with Multimodal LLM Agents | 5 | 多模态 LLM 智能体跑 18 次 LiCoO2 薄膜实验，“验证-证伪”演化出 650–690°C 结晶阈值认知 | Multimodal LLM agents run an 18-experiment LiCoO2 campaign with verify-falsify logic, evolving a 650-690 C crystallization threshold |
| 78 | [[2609.19099]] | Evidence-Grounded Agentic Formulation Development in an Autonomous Laboratory | 5 | 基于结构化内部证据设计并执行紫杉醇 SEDDS 批次，高性能率 50%，对比优化器 17%、DoE 2% | Reasons over structured in-house evidence to execute paclitaxel SEDDS batches: 50% high-performance rate vs 17% (optimizer) and 2% (DoE) |
| 79 | [[2609.19101]] | Monitoring and Discovering Reward Hacking with Internal Representations | 5 | 隐藏状态差分向量连贯表征奖励作弊（GLM 5.2 作弊 73% rollouts），可在线于 CoT 输出前拦截 | Difference-of-means hidden-state vectors coherently detect reward hacking (73% of rollouts) and catch hacks online before they occur |
| 80 | [[2609.19441]] | Predict Before You Deploy | 5 | 离线动作偏差校准阈值，预测量化对世界动作模型闭环任务的破坏，21/21 接受/拒绝决策全对（75% 覆盖） | Calibrates offline action-deviation thresholds to predict quantization-induced closed-loop degradation: 21/21 matching accept/reject calls at 75% coverage |
| 81 | [[2609.19519]] | An Architecture for Long-Horizon Agents | 5 | 层级/tick/级联智能架构支撑十天自主战役跨上下文重置保持连贯，早期知识不改权重地改变后期行为 | Levels/ticks/cascaded-intelligence architecture keeps a ten-day autonomous campaign coherent across context resets without weight changes |
| 82 | [[2609.19526]] | Self Improvement via Fast Tree-search | 5 | 编码智能体递归自修改：LLM-judge Bradley-Terry 排序引导树搜索，把昂贵评测留给最有希望的补丁 | SIFT coding agents recursively self-modify under LLM-judge Bradley-Terry rankings, reserving expensive benchmark evals for the most promising patches |
| 83 | [[2609.19644]] | ScientistTwo | 5 | 端到端自主发现：基线、假说、协调实验、消融与闭环同行评审驳稿引擎，产出专家级可发表论文 | ScientistTwo runs end-to-end autonomous discovery with coordinated experiments and a closed-loop peer-review rebuttal engine, producing expert-level papers |
| 84 | [[2609.19683]] | MiX | 5 | 发现 MX 微缩放坍缩（单离群值劫持共享指数），倒置范式为逐元素指数，4.5-bit 匹配 NVFP4 | Identifies microscaling collapse (one outlier hijacks the shared exponent) and inverts MX to per-element exponents, matching NVFP4 at 4.5 bits |
| 85 | [[2609.19969]] | DeepSeek-V4.1-Flash | 5 | 官方系统卡：552B 多模态 MoE，CSA2 跨层 KV 复用 + FP4 KV 缓存至 890 B/token，1M 上下文 | Official card: 552B multimodal MoE with CSA2 cross-layer KV reuse and FP4 KV caching at 890 bytes/token, 1M-token context |
| 86 | [[2609.20519]] | SoL-Pi | 5 | harness 层递归自改进，四种 rollout 选择机制在开发外设置迁移并省 44–49% token | Harness-level recursive self-improvement with four rollout-selected mechanisms transferring beyond dev settings at 44-49% token reduction |
| 87 | [[2609.21257]] | Verify, Don't Trust | 5 | 37 天人类把关在线 autoresearch：持久记录 + 确定性检查把 22pp 命中率下降归因于既有评测漂移 | Human-gated 37-day online autoresearch traced a 22pp hit-rate drop to pre-existing evaluation drift rather than the tested interaction head |
| 88 | [[2609.21450]] | Understanding LLM Quantization through Activation-Guided Compensation and Orthogonal | 5 | W4A4 量化误差精确分解为激活引导补偿项 + 离群有界正交残差，无反传规则媲美 SpinQuant | Exact W4A4 error decomposition into activation-guided compensation and outlier-bounded orthogonal residual; backprop-free rules rival SpinQuant |
| 89 | [[2609.21662]] | When Steering Fails in Latent Reasoning | 5 | steering 能移动潜推理隐状态却无法迁移到语言生成——潜到语言的转换断层 | Steering moves latent-reasoning hidden states like CoT yet fails to transfer to language output: a latent-to-language transition gap |
| 90 | [[2609.21748]] | World Modeling in Transformers | 5 | TaxiGPT 用目标罗盘追踪位置，却在叠加路口特征干扰下失效——受限于 affordance 打包 | Mechanistic analysis shows TaxiGPT tracks position with a goal compass but fails via interference between superposed intersection features |
| 91 | [[2609.21996]] | A Lie Detector Test for Language Models | 5 | 内部状态 CIT 测谎：即使被提示欺骗、训练藏拙、密码锁定或 circuit breaking，仍有 0.70–0.87 平衡准确率 | A Concealed Information Test reads internal states at 0.70-0.87 balanced accuracy even under prompted deception, sandbagging, locks, and circuit breaking |
| 92 | [[2609.22086]] | Designer-RSI | 5 | 从用户流量演化程序性记忆：未覆盖子任务“变宽”、自身失败“加深”，冻结 Claude 执行成功率 72.7%→99.3% | Evolves procedural memory from user traffic (widening and deepening) to lift frozen Claude-Sonnet-4 execution success from 72.7% to 99.3% |
| 93 | [[2609.22590]] | UniCASE | 5 | 16-bit 浮点统一格式 + 按比特关键性分级的选择性 ECC，编码器成本降 30% 且精度损失 <1% | Unified 16-bit format with criticality-aware selective ECC cuts encoder/decoder cost 30% while preserving accuracy within 1% |
| 94 | [[2609.22592]] | AutoGym | 5 | 蓝图先行生成可验证智能体训练场：先定解空间与验证准则，再物化环境、难度参数与课程 | Blueprint-first gym generation specifying valid solution space and verification criteria before environments materialize, with difficulty parameters and curricula |
| 95 | [[2609.22782]] | Look Before You Steer | 5 | 解码器几何（邻居密度/最大余弦）无需前向即可预测 SAE 特征 steering 代价（ρ 至 -0.546） | Decoder-space geometry (neighbor density, max cosine) predicts SAE feature steering cost (rho to -0.546) before any forward pass |
| 96 | [[2609.22870]] | Towards Full Pipeline FP8 Reinforcement Learning for LLMs | 5 | 全流水线 FP8 RL 不稳定根因：量化噪声扭曲重要性比率、负优势梯度归零；校准裁剪修复至 BF16 水平 | Traces full-pipeline FP8 RL instability to distorted importance ratios and zeroed negative-advantage gradients; Calibrated Clipping restores BF16-level performance |
| 97 | [[2609.22991]] | Silent Failures at the $2^{32}$ Boundary | 5 | Apple MPS 后端 torch.bmm 大张量静默返回忽略 stride、2^32 回卷的错误输出，PyTorch 2.4.1–2.14.0 全中 | Documents torch.bmm silently returning stride-ignoring, 2^32-wrapped wrong outputs for large tensors on Apple MPS (PyTorch 2.4.1-2.14.0), with a released guard |
| 98 | [[2609.23048]] | Anatomy of a Closed-Loop Collapse | 5 | 因果取证：蒸馏 VLA 策略通过全部离线检查却闭环 0/72——持续的 10× 晚期 z 残差是根因 | Causal forensics: a distilled Octo policy passes every offline check yet collapses to 0/72 closed-loop; a persistent 10x late-heavy z residual is the cause |
| 99 | [[2609.23065]] | From Concept Alignment to Causal Grounding | 5 | 共享 SAE 编码预测与 CoT 两遍 + 因果 delta-p 指标：忠实性峰值在中后层，因果重要概念未必被言说 | Shared-SAE encoding with a causal delta-p metric shows CoT faithfulness peaks mid-to-late layers; causally important concepts are not always verbalized |
| 100 | [[2609.23125]] | Perplexity Cost Understates What Activation Quantisation Breaks | 5 | 1.2–1.5× 困惑度上升可掩盖检索坍缩至 0.554；伤害来自误差结构而非幅度 | A 1.2-1.5x perplexity rise can hide retrieval collapsing to 0.554; error structure, not magnitude, drives the damage |

---

<!-- COUNT_CHECK: All Papers table lists 100 entries; total_selected in filtered_papers.json = 100; topic tables total 100 rows. Counts match. -->
