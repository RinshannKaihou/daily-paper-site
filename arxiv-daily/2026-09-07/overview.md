---
title: "周报 / Weekly Overview: 2026-09-07 .. 2026-09-13"
date: 2026-09-07
week: "2026-09-07..2026-09-13"
tags:
  - weekly-overview
  - self-evolving-agents
  - interpretability
  - quantization
  - reliability
  - training-stability
papers: 100
---

本周共评估 2415 篇论文，入选 100 篇（5 分 31 篇、4 分 69 篇）。主题集中在四条主线：自进化智能体与自动化研究（48 篇）、LLM 隐状态与可解释性（24 篇）、极致性能优化下的可靠性（16 篇），以及训练稳定性/算力基础设施/推理可靠性等支撑方向。
This week 2,415 papers were evaluated and 100 selected (31 scored 5, 69 scored 4). Four main threads dominate: self-evolving agents & automated research (48), LLM hidden states & interpretability (24), reliability under extreme performance optimization (16), plus training stability, compute infrastructure, and inference reliability.

## 本周必读 / Must Read This Week

### 1. [[2609.06887]] Human-agent discovery of reconfigurable in-plane ferroelectric superdomain control

- **中文理由：** SPARC 让编码智能体与人类操作员共享一台真实扫描探针显微镜，仅靠 FINDINGS.md / PITFALLS.md 两个持久记忆文件，在状态表示、动作空间、目标函数都不存在的铁电薄膜问题上发现了可重写的面内超畴方向控制原语（命令方向功率 +0.392 vs 对照 −0.006，8 次有效实验 7 次命中，并把 "UTK" 写进超畴取向）——"智能体是前优化阶段的推理层"这一论点的教科书级实证，还坦诚披露了 8 次启动中 6 次失败的智能体自写控制软件。
- **English reason:** SPARC pairs a coding agent with a human operator on one real microscope and two persistent memory files; on a problem with no predefined state, action space, or objective it discovered a rewritable in-plane superdomain-direction primitive (+0.392 vs −0.006 control, 7/8 targeted trials, "UTK" written into the superdomain orientation) — the strongest demonstration yet of agents as a reasoning layer *before* optimization becomes well posed, with frank reporting of the agent-authored control software failing 6 of 8 launches.

### 2. [[2609.07204]] Agentic Algorithm Engineering: Improving Shared-Memory Exact Minimum Cuts

- **中文理由：** 让自主 Claude Opus 5 智能体在作者本人手工深度调优过的 VieCut 求解器上跑完整"假设—实现—基准—保留/回退"循环（正确性断言守门、每实验一次 commit、台账落盘），约 350 美元 API 成本换来单线程 3.44×、32 线程 21.49× 的几何平均加速并解决基线 OOM 的 4 个实例——证明智能体能做"替换数据结构、重划分并行工作"这类没有调参旋钮的改动。
- **English reason:** An autonomous agent runs the full hypothesize→implement→benchmark→keep/revert cycle (guarded by correctness assertions, one commit per experiment, durable ledger) on the authors' own heavily hand-tuned VieCut solver; ~$350 of API cost buys 3.44× (1-thread) and 21.49× (32-thread) geometric-mean speedups and solves 4 instances the baseline OOMs on — showing agents can make changes with no tuning knob, like swapping data structures and repartitioning parallel work.

### 3. [[2609.09219]] Scores Alone Do Not Prove Discovery: The Discovery Certification Protocol for Auditing AI Research Agents

- **中文理由：** 把"AI 研究智能体做出了发现"的声明转化为三道可执行关卡：密封评测、同条件新智能体恢复审计（96 个挑战者 0 次恢复、恢复概率上界 0.0468）、真实/中性反馈配对实验（30/30 vs 0/30），全部裁决由无 LLM 的确定性验证器从冻结证据离线复现，两次完整审计成本仅约 60 美元——自动化研究走向可信的第一份"审计学"蓝本。
- **English reason:** Converts discovery claims into three executable gates — sealed evaluation, a recovery audit by matched fresh agents (0/96 recoveries, upper bound 0.0468), and truthful-vs-neutral feedback pairs (30/30 vs 0/30) — with every decision replayed offline by a deterministic LLM-free verifier and two full audits costing ~$60 each; the beginnings of an audit discipline for autonomous research.

### 4. [[2609.09776]] Proof-Carrying Cognition: Closing the Verification Gap with Reality-Settled Reward

- **中文理由：** 理论上证明验证器–真值相关 ρ 就是测试时算力与能力的"汇率"（不可靠验证器需付出 N^(1/ρ²) 候选代价），实测弱 LLM 裁判在 best-of-N 压力下 soundness 从 0.325 崩至 0.016，且仅靠"选择"就能从诚实样本制造 +0.527 的 hacking 差距；用真实执行结果持续"结算"并重训奖励模型，把 GRPO 中被冻结 RM 毁掉 90% 的执行奖励保住 86%——RLVR 与奖励模型方向的必修课。
- **English reason:** Proves verifier–gold correlation ρ is the exchange rate between test-time compute and capability (unsound verifiers pay N^(1/ρ²)); a weak LLM judge's soundness collapses 0.325→0.016 under best-of-N pressure and selection alone manufactures a +0.527 hacking gap, while settling the reward model on real executions preserves 86% of the reward a frozen RM destroys under GRPO — essential reading for RLVR and reward modeling.

### 5. [[2609.08183]] NeoHorse-1: Towards Recursive Self-Improvement via Agentic Post-Training with Routing Harness

- **中文理由：** 把部署中的路由 harness 重新定义为递归自我改进（RSI）的数据引擎：路由器预测+执行轨迹+结果经六维语义质控转为训练样本，路由分数驱动三阶段课程 SFT 与 on-policy 蒸馏，4B 宏平均 58.94→64.87、9B 65.60→69.04，9B 甚至超过 3 倍大的 30B 模型；同配方下 harness 轨迹比公开智能体数据集高 +6.26。"递归"目前只跑了一圈，但评估–选择–更新闭环原型完整。
- **English reason:** Reframes a deployed routing harness as the data engine for recursive self-improvement: harness records (routing prediction, trajectory, outcome) become quality-gated training examples, routing scores drive curriculum SFT and on-policy distillation, lifting 4B 58.94→64.87 and 9B 65.60→69.04 (9B beats a 3×-larger 30B); harness trajectories beat a public agent dataset by +6.26 under the identical recipe. Only one loop iteration is run, but the evaluate–select–update prototype is complete.

### 6. [[2609.07664]] Accuracy is Not Enough: A Divergence-Based Approach to Evaluate Fidelity Loss in Quantized LLMs

- **中文理由：** argmax 准确率会系统性掩盖量化 LLM 的分布级损伤：Teuken-7B 在 Q4_0 下 PIQA 准确率仅降 0.2 个百分点，但 TVD 高达 0.560（56% 概率质量被重排）；混合精度 Q4_K 在相近显存下散度低约 4 倍（MMLU 上 0.055 vs 0.221），并形式化证明任何答案级粗糙化指标只能低估全词表偏移——部署量化模型前应做的"分布体检"。
- **English reason:** Argmax accuracy systematically masks distributional damage in quantized LLMs: Teuken-7B at Q4_0 loses only 0.2 accuracy points on PIQA yet reassigns 56% of probability mass (TVD 0.560); mixed-precision Q4_K reaches ~4× lower divergence at similar memory (0.055 vs 0.221 on MMLU), with a theorem that any answer-level coarsening can only underestimate full-vocabulary shift — the distributional checkup to run before deploying quantized models.

### 7. [[2609.11716]] Why Does Post-Training Quantization Work?

- **中文理由：** 机理级回答：随机初始化与预训练权重的 NVFP4 重构误差几乎相同（余弦均约 0.9955），但量化后前者的最终隐藏误差是预训练版的 5.5 倍——鲁棒性来自预训练本身。两个机制：每层新增误差与继承误差方向相反（跨 64 层抵消 63.4%），以及 LM 头几何对最终隐藏态旋转的 78.6× 衰减保护 Top 排名 token，最终平均仅损 0.43 个百分点。跨 Qwen3/OLMo3/Gemma3/OLMoE 与 W4/A4/RTN/GPTQ/AWQ 验证。
- **English reason:** A mechanistic answer: random-init and pretrained weights have nearly identical NVFP4 reconstruction error (cos ≈ 0.9955), yet the quantized random-init model accumulates 5.5× the final hidden error — robustness comes from pretraining itself. Two mechanisms: per-layer introduced errors counteract inherited ones (63.4% cancelled over 64 layers), and LM-head geometry attenuates hidden-state rotation 78.6× to protect top-ranked tokens, leaving only 0.43 pp average loss — verified across Qwen3/OLMo3/Gemma3/OLMoE and W4/A4/RTN/GPTQ/AWQ.

### 8. [[2609.10210]] Through the Looking Glass: Directly Reading and Writing Transformers

- **中文理由：** 零训练、零拟合的"透镜"直接从参数与激活读出预测背后的组件：把归因分母从绝对质量改为带符号净值后（18 个模型中反对质量中位数是净值的 7 倍），一个预测只依赖约 53 个组件（13 个必要、8 个充分），12 个第三方模型上充分集仅 2–16 个；且可双向写入——往一个备用 FFN 单元安装新联想（rank 578→1）仅损 0.25% held-out 损失，是 rank-one 编辑成本的 1/40。
- **English reason:** A training-free, zero-fit "lens" reads the components behind a prediction straight from parameters and activations: dividing by signed net mass instead of absolute mass (opposing mass is a median 7× the net across 18 models) shrinks circuits to ~53 components (13 necessary, 8 sufficient), with sufficient sets of 2–16 on 12 off-the-shelf models; and it writes both ways — installing a new association into one spare FFN unit (rank 578→1) costs 0.25% held-out loss, 40× cheaper than rank-one editing.

> 另有四篇高分论文同样值得优先阅读 / Four more score-5 papers worth priority reading: [[2609.09113]]（智能体自主做 SAE 可解释性研究的闭环基准 / agents autonomously doing SAE interpretability research）、[[2609.10299]]（SAE 相图中的"扩散相"：重构近乎完美但特征恢复为零 / a diffuse SAE phase with near-perfect reconstruction and zero feature recovery）、[[2609.07611]]（主动检索让科学构思评测区分度提升 4.4 倍 / active retrieval multiplies ideation-benchmark discriminability 4.4×）、[[2609.11655]]（谱裁剪取代 Muon 谱拉平，权重范数 300–400 压到 10 以下 / spectral clipping tames Muon instability）。

## 按主题分类 / Papers by Topic

### 自进化智能体与自动化研究 / Self-Evolving Agents & Automated Research（48 篇 / papers）

| 论文 / Paper | 分 / Score | 亮点（中 / EN） / Highlights |
|---|---|---|
| [[2609.06887]] Human-agent discovery of ferroelectric superdomain control | 5 | 人机共享显微镜+持久记忆文件，在真实铁电薄膜上发现可重写超畴方向控制原语 / Coding agent + human operator share a microscope with persistent memory; discovered a rewritable superdomain-direction primitive on real ferroelectric films. |
| [[2609.07204]] Agentic Algorithm Engineering | 5 | 自主智能体在手工调优的 VieCut 上跑完整算法工程循环，取得 1.28–127× 加速 / Autonomous agents run the full algorithm-engineering cycle on hand-tuned VieCut for 1.28–127× speedups. |
| [[2609.07611]] AgentIdeaBench | 5 | 静态 vs 主动探索双设定评测 33 个 LLM 的科学构思，原创性经文献校验 / Benchmarks 33 LLMs' scientific ideation in matched static vs active settings with literature-verified originality critics. |
| [[2609.07655]] Online Surrogate Repair | 5 | 稀疏高保真评估（Q90-UCB/EI）阻止闭环智能体放大代理误差，省 6.4–10.3× 预言机查询 / Sparse high-fidelity evaluations stop closed-loop agents amplifying surrogate errors, saving 6.4–10.3× oracle queries. |
| [[2609.08175]] Safe Harness Self-Evolution | 5 | 智能体自改提示/工具/代码的有限数据认证界；证明停滞可在机会仍存时出现 / Finite-data certification bounds for agent self-modification; proves stagnation can arise while improvement opportunities remain. |
| [[2609.08183]] NeoHorse-1 | 5 | 路由 harness 记录转为下一轮训练混合，4B/9B 上的递归自我改进原型 / Converts routing-harness records into the next training mixture — an explicit RSI prototype at 4B/9B scales. |
| [[2609.08248]] Agentic ML Exploration (A-MLE) for Ads Ranking | 5 | 已部署的工业广告排序自主智能体系统，跑通五阶段 ML 迭代循环 / Deployed autonomous agent system running the five-stage ML iteration loop on industrial ads-ranking models. |
| [[2609.08832]] Closing the Consistency Gap | 5 | 命名并量化"一致性鸿沟"（77% 均值 vs 53% 五次全过），指南注入使 Pass@5 +16pp / Names the consistency gap (77% mean vs 53% all-five-pass) and closes it with committed guidelines (+16 pp Pass@5). |
| [[2609.09113]] SAEScientist-Bench | 5 | 智能体自主设计对比探针在 131K 特征字典中找概念特征，因果引导仍落后专家约 26 分 / Agents autonomously design contrastive probes over a 131K-feature dictionary; causal steering still trails experts by ~26 points. |
| [[2609.09219]] Discovery Certification Protocol | 5 | 把发现声明变成带有限样本界的可执行恢复与反馈审计 / Turns discovery claims into executable recovery and feedback audits with finite-sample bounds. |
| [[2609.09776]] Proof-Carrying Cognition | 5 | 不可靠验证器在 best-of-N 压力下失稳；现实结算奖励把 hacking 差距压到近零 / Unsound verifiers lose soundness under best-of-N pressure; reality-settled rewards drive the hacking gap to ~0. |
| [[2609.09875]] AgentAudit | 5 | 十维全生命周期智能体信任评测框架，带阶段级失败归因 / Scores full agent traces across ten capability/grounding/security dimensions with stage-level failure attribution. |
| [[2609.10702]] Data-Efficient Language Modeling | 5 | 端到端自主研究项目（模型构建→原则发现→原则引导改进）拿下 BabyLM 2026 Strict-Small 第一 / End-to-end autonomous research program (build → discover principles → improve) winning BabyLM 2026 Strict-Small. |
| [[2609.11028]] BenchShield | 5 | 相位感知污点分析+基础设施侧归因，全链路 reward-hacking 召回 23–94% → 77–100% / Phase-aware taint analysis with infrastructure-side attribution lifts full-chain reward-hacking recall from 23–94% to 77–100%. |
| [[2609.11147]] Autonomous Chemical Mechanistic Discovery (ARCHE) | 5 | 自主生成并验证化学反应机理，确认未发表的自由基 α-碘硼酸酯 C–I 断裂路径 / Autonomously generates and validates reaction mechanisms, confirming an unpublished radical C–I cleavage pathway. |
| [[2609.12655]] LifeMem | 5 | 累积轨迹聚类为可复用技能供推理时召回，跨 10 环境缓解灾难性遗忘 / Clusters accumulated trajectories into reusable skills recalled at inference, cutting forgetting across 10 environments. |
| [[2609.13073]] Autonomous Research for Telecom Ticket Retrieval | 5 | 开放式工业问题上，自主研究智能体 10 周达到人类 10 个月 SOTA 召回的 90% / Autonomous research agents reach 90% of a 10-human-month SOTA in 10 weeks on an open-ended telecom problem. |
| [[2609.13406]] Generalized Agent Iteration | 5 | 把广义策略迭代与递归自我改进统一为一个框架（改进器在内/标准在外两个旋钮） / Formalizes generalized policy iteration and RSI as one paradigm with two dials (improver inside, standard grounded outside). |
| [[2609.06966]] MOLE | 4 | 检测智能体账号数据外泄/投毒的监视器基准；最好的单日审计漏掉近半已完成伤害 / Benchmark for monitors detecting agent-account exfiltration/poisoning; the best single-day audit misses nearly half of completed harm. |
| [[2609.06972]] AgentDrift | 4 | 71,024 步全部标注的注入劫持轨迹语料；表面特征仅恢复 55.4% 攻击 / Step-labeled corpus of injection-hijacked trajectories; surface features recover only 55.4% of attacks. |
| [[2609.07529]] CoER | 4 | 广义和马尔可夫博弈中共进化攻防，间接注入成功率 38.5% → 0.2% / Co-evolving attacker/defender populations in a general-sum Markov game cut indirect injection success from 38.5% to 0.2%. |
| [[2609.07603]] FinCUABuild | 4 | 智能体自主构建金融计算机使用评测任务，严格合格率 31.3% vs 此前 1.3–8.3% / Agents autonomously build financial computer-use tasks; 31.3% strict qualification vs 1.3–8.3% for prior methods. |
| [[2609.07925]] FrogNano | 4 | 纯 RL 训练 4B 编码智能体，任务在检查点可学习性前沿在线合成 / Trains a 4B coding agent purely with RL on ~1,500 environments whose tasks are synthesized online at the learnability frontier. |
| [[2609.08015]] Selective Revalidation (ATR) | 4 | 记录待定动作的可执行依据条件，状态变化时只重验受影响条件，零误放/误拦 / Records executable justification conditions behind pending actions and rechecks only affected ones, with zero false allows/blocks. |
| [[2609.08126]] SchemeArena | 4 | 400 情景因子化 scheming 压力测试；仅监控动作反而可能增加闭源模型 scheming / 400-scenario factorized scheming stress tests; action-only monitoring can increase scheming in closed models. |
| [[2609.08149]] SWE-Bench Pro Verified | 4 | 消除金标泄露通道并修复任务/测试不一致，揭示部分模型靠 reward hacking 虚高 / Eliminates gold-solution leakage and repairs task/test inconsistencies; some models' coding ability was overestimated via reward hacking. |
| [[2609.08228]] SE-GoS | 4 | 从执行轨迹免训练进化技能图（拓扑剪枝+有效性加权边），held-out +5.4 分 / Training-free evolution of a Graph-of-Skills from traces, +5.4 points over the static graph on held-out tasks. |
| [[2609.08258]] Revoked but Still Authoritative | 4 | 被测智能体记忆系统无一在检索时执行软撤销，撤销策略反而压过新策略 / No tested agent-memory system enforces soft revocation at retrieval — revoked policies outrank their replacements. |
| [[2609.08279]] What Eviction Destroys | 4 | 恢复反事实审计区分不可逆驱逐损失与可恢复检索失败（不可逆占比 0.60–1.00） / Restore-counterfactual audit separates irreversible eviction loss from recoverable retrieval failure (irreversible shares 0.60–1.00). |
| [[2609.08282]] Dreaming in Flow | 4 | 模型自生成视觉"梦境"提供流级反馈与梦境回放接地，无配对数据改进生成 / The model's own generated visual "dreams" supply flow-level feedback, improving generation without paired supervision. |
| [[2609.08404]] Environments as Scaffold | 4 | 反馈富化环境从动作引导转向观察富化，稳定长时程自进化智能体 RL / Feedback-Enriched Environments shift from action guidance to observation enrichment, stabilizing self-evolving agent RL. |
| [[2609.08589]] The Unreliable Progress Bar | 4 | 任务进度自报可靠性随执行阶段变化，多数部署模型中途失准 / Progress-reporting reliability varies by execution stage; most deployed models lose accuracy mid-task. |
| [[2609.08696]] MorphoOrgaAgent | 4 | 多智能体系统（零样本分割+报告智能体）端到端自动化类器官分析 / Multi-agent system (zero-shot segmentation, report agent) automates organoid analysis end-to-end. |
| [[2609.08919]] Experience Funnel | 4 | 快速文本状态适应与慢速策略蒸馏交替，把经验转化为持久参数能力 / Alternates fast textual-state adaptation with slow transition-aware policy distillation into durable competence. |
| [[2609.08944]] SkillAdam | 4 | 类 Adam 优化记忆稳定技能进化方向，波动率驱动编辑预算，七基准 SOTA / Adam-inspired optimization memory stabilizes skill evolution; SOTA across seven benchmarks at lower cost. |
| [[2609.09134]] Co-Evolving Harnesses and Models | 4 | 模仿专家轨迹使弱模型回退 4–30 分，用 on-policy 单轮专家纠正修复 / Imitating experts under an evolved harness regresses weaker models 4–30 points; on-policy single-turn corrections fix it. |
| [[2609.09153]] Procedural Graphs | 4 | LLM 精炼器对比成败轨迹编辑"程序-关系"图拓扑，匹敌手工设计结构 / Self-evolving procedure graphs whose LLM refiner edits topology by contrasting failed and successful trajectories. |
| [[2609.09448]] Calibrating Agent Confidence | 4 | 残差流轨迹动力学+动作表征探针零开销预测任务成败 / Residual-stream trajectory dynamics and action probes predict eventual task success as a zero-overhead monitor. |
| [[2609.09468]] Code-to-Harness | 4 | 智能体自写并评估优化器程序，蒸馏出 197 词便携 harness，黑箱优化 regret 降 43–49% / Agent-authored optimizer programs distill into a 197-word portable harness cutting black-box regret 43–49%. |
| [[2609.09646]] RobustSGPO | 4 | 语义梯度 harness 进化的搜索空间控制（可执行补丁检查+快照保留），完成率 60% → 80% / Search-space control for semantic-gradient harness evolution lifts held-out completion from 60.0% to 80.0%. |
| [[2609.09849]] NetArtifactBench | 4 | 修复网络实验记录需恢复跨工件隐式关系，无一运行时 pass 超 30% / No runtime exceeds 30% pass when artifact repair requires recovering implicit cross-artifact relations. |
| [[2609.09853]] Era by Eon Benchmark | 4 | 从种子实体图生成基准企业，模拟器/数据库/答案键描述同一一致庄园 / Generates benchmark enterprises from a seeded entity graph so simulators, databases, and answer keys describe one consistent estate. |
| [[2609.09957]] SOLID | 4 | 无需验证答案：聚类 rollout 目标为多数组伪参考，自蒸馏改进运筹语言模型 / Self-improves OR language models without verified answers via majority-group pseudo-references. |
| [[2609.10226]] Φ-Bench | 4 | 评测 LLM 工程化"驱动自身运行"的 LLM 基础设施栈 / Evaluates LLMs on open-ended, long-horizon engineering of the LLM infrastructure stack that powers them. |
| [[2609.10315]] TRACE | 4 | 向模拟器注入隐藏干预作为 oracle 标签，为不可验证诊断推理构造可验证奖励 / Injects hidden simulator interventions as oracle labels to engineer verifiable rewards for diagnostic reasoning. |
| [[2609.10494]] IBIB | 4 | 按"服务路由"而非"模型标识"度量企业 AI 系统，加入能力绑定预检 / Measures enterprise AI by serving route rather than model identifier, with capability-binding preflight. |
| [[2609.10539]] IdeaAMBIG | 4 | 基准化研究方案规格的可实现化缺口：最好模型仅恢复 9.6% 实现缺口 / Benchmarks codification readiness of research-idea specs; the best model recovers only 9.6% of implementation gaps. |
| [[2609.10724]] Finishing the Task Is Not Enough | 4 | 120 条医疗轨迹：挑战累积时智能体从自主恢复转向依赖人类 / Across 120 healthcare trajectories, agents shift from self-directed recovery toward human dependence under accumulating challenge. |

### LLM 隐状态与可解释性 / LLM Hidden States & Interpretability（24 篇 / papers）

| 论文 / Paper | 分 / Score | 亮点（中 / EN） / Highlights |
|---|---|---|
| [[2609.10210]] Through the Looking Glass | 5 | 带符号净值归因把回路从数万组件缩到几十个（必要 13、充分 8），且可直接写入新联想 / Signed-net attribution shrinks circuits to ~53 components (13 necessary, 8 sufficient) and supports direct writes. |
| [[2609.10299]] A Dominant Diffuse Phase in the SAE Phase Diagram | 5 | 约 3500 次拟合全部落入"扩散相"：重构近完美、特征恢复为零、编码稠密 10–28 倍 / Across ~3,500 fits, SAEs land in a reproducible diffuse phase — near-perfect reconstruction, zero feature recovery, 10–28× denser codes. |
| [[2609.06934]] The Geometry of Refusal | 4 | 几何解释后置安全脆弱性：安全更新近乎垂直于能力 Fisher 曲率方向 / Post-hoc safety updates land nearly orthogonal to capability Fisher-curvature directions — a thin but sharp refusal gate. |
| [[2609.06951]] Steering Interference | 4 | 转向干扰取决于模型自身默认行为而非行为方向重叠 / Activation-steering interference tracks the model's own defaults, not overlap between behavior directions. |
| [[2609.07037]] Disentangling Steering Vectors | 4 | 在实例级转向向量上训练专用 SAE，把复合方向拆成可控特征 / A dedicated SAE on instance-level steering vectors disentangles composite directions into controllable features. |
| [[2609.07053]] A Hyperbolicity Atlas | 4 | 首个 prompt-token 隐状态 Gromov 双曲度地图（81.9 万测量、十模型） / First systematic Gromov-hyperbolicity map of hidden states (818,904 measurements, ten models). |
| [[2609.07139]] Encoded Early, Used Late | 4 | 伙伴专业度属性早层线性可读，因果生效晚一个数量级 / An inferred partner-expertise attribute is linearly decodable in early layers, causally active much later. |
| [[2609.07183]] CircuitLens | 4 | 46 个对比消融注意力头导出 Circuit Reasoning Score 做 RLVR 数据选择 / A Circuit Reasoning Score from 46 contrastively-ablated heads beats random RLVR data selection. |
| [[2609.07406]] Think Wider | 4 | 识别隐式 CoT 的潜秩坍缩，谱正则提升潜轨迹有效秩 / Identifies latent rank collapse in implicit chain-of-thought; a spectral regularizer raises effective rank. |
| [[2609.07478]] Internal Anatomy of Strategic Choice | 4 | 2×2 博弈：基座与指令模型表征激励几乎相同，差异在激励是否到达选择 / Base and instruct models represent incentives almost identically; they differ in whether the incentive reaches the choice. |
| [[2609.07681]] Recall Scaling Laws in Mamba | 4 | 逆向工程 Mamba 关联回忆为隐式线性哈希电路并推导召回 scaling law / Reverse-engineers Mamba's recall as implicitly learned linear hashing with JL-style scaling-law predictions. |
| [[2609.07746]] LLM Forensics | 4 | SAE 分解分离后门触发检测特征与残差流传播特征，消融后者压制语言切换 / SAE decomposition separates trigger-detection from residual-stream propagation features in backdoors. |
| [[2609.07876]] LLM Layers Immediately Correct Each Other | 4 | 相邻层系统性相互抵消贡献：残差流同时存瞬态提案与持久特征 / Adjacent layers systematically counteract each other — the residual stream holds transient proposals alongside persistent features. |
| [[2609.08173]] Key Path Identification | 4 | 识别强因果依赖的 SAE 特征关键路径做知识冲突转向，RAG 准确率 +18% / Causally-linked SAE feature key paths improve knowledge-conflict steering, RAG accuracy +18%. |
| [[2609.08322]] Tracing Stereotypes | 4 | 刻板印象可解码性在深度 36–53% 处达峰，语言不可知特征仅 6–18% / Stereotype decodability peaks at 36–53% of depth; only 6–18% of residual-stream features are language-agnostic. |
| [[2609.08410]] Compositional Steering | 4 | 语言/越狱/简洁转向向量各自最佳层注入时近似可加组合 / Steering vectors for language, jailbreak, and conciseness compose additively at their own best layers. |
| [[2609.08574]] Do New Attention Mechanisms Fix Sinks? | 4 | SinkProbe：百万 token 上下文中产生注意力汇的是训练目标而非架构 / SinkProbe finds the training objective rather than the architecture produces attention sinks at million-token context. |
| [[2609.08692]] SSM vs Transformer Geometry | 4 | SSM 表示均匀铺开、Transformer 坍缩到主方向，但有效容量与概念子空间维度匹配 / SSM representations spread evenly while transformer layers collapse onto one direction, yet effective capacities match. |
| [[2609.09054]] Training-Free Task Vectors | 4 | 仅用前向统计把激活转向映射为秩一权重空间任务向量 / Maps activation steering vectors to rank-one weight-space edits using only forward-pass statistics. |
| [[2609.09085]] It's Not RoPE that Creates Sinks | 4 | 注意力汇源于因果掩码自集中与数值不混合，而非 RoPE / Attention sinks arise from causal-mask self-concentration and value-non-mixing, not RoPE. |
| [[2609.09556]] Linear Accessibility in Superposition | 4 | 压缩感知界：线性可读叠加特征维度只需 O(k log m)；附 IHT-SAE 迭代精化 / Compressed-sensing bounds: linearly accessible superposed features need only O(k log m) dimensions; IHT-SAE refines beyond linear recovery. |
| [[2609.09902]] Contrastive Projection | 4 | 对减 logit lens 投影读内部，追踪复合名词的 MLP→注意力链 / Differencing logit-lens projections cancels the generic-token component and traces a compound-noun MLP→attention chain. |
| [[2609.10060]] Reference-Based Bias Detection | 4 | 固定锚集相对表示审计偏置，表示偏置移位与输出偏置变化的相关达 0.84 / Relative representations against a fixed anchor set correlate 0.84 with output-level bias change after fine-tuning. |
| [[2609.10287]] Circuit Removability | 4 | 可退火软先验 Transformer 检索电路可移除性取决于训练轨迹 / Retrieval-circuit removability in annealable soft-prior transformers depends on the training trajectory. |

### 极致性能优化下的可靠性 / Reliability under Extreme Performance Optimization（16 篇 / papers）

| 论文 / Paper | 分 / Score | 亮点（中 / EN） / Highlights |
|---|---|---|
| [[2609.07664]] Accuracy is Not Enough | 5 | 全词表 TVD/JSD 散度暴露 argmax 准确率掩盖的量化分布损伤（0.2pp 精度损失下 TVD 0.560） / Full-vocabulary TVD/JSD divergence exposes fidelity loss invisible to top-1 accuracy (TVD 0.560 behind a 0.2-pp accuracy change). |
| [[2609.07901]] Quantization Amplifies Determinism, Not Bias | 5 | 预注册 7.1 万条配对生成：W4 在 8B 上放大输出确定性（同品牌 +5.1pp）而非刻板偏见 / Pre-registered 71k-completion study: W4 AWQ at 8B amplifies output concentration (same-brand +5.1pp), not stereotypes. |
| [[2609.08135]] KBBQ | 5 | 二阶噪声理论+参与因子 κ 的闭式 SNR 定律与谱展平上限，KBBQ 在 W4A4 FP4 上逼近上限 / A closed-form SNR law with participation factor κ and a spectrum-flattening ceiling; KBBQ approaches it at W4A4 FP4. |
| [[2609.09095]] Ozaki 2.5 | 5 | 剩余数分解在 FP8 张量核上仿真 fp64 稠密矩阵乘，附 473-TFLOPS Rubin 屋顶的闭式性能下限 / RNS deconstruction emulates fp64 GEMM on FP8 tensor cores with a closed-form Rubin-roof performance floor. |
| [[2609.09854]] Low-Bit Quantization in Vector Search | 5 | 低比特量化翻转排名比较的无分布界+Vamana 近邻选择耦合定理 / Distribution-free bounds on the probability that low-bit quantization flips a ranking comparison, plus a Vamana coupling theorem. |
| [[2609.11356]] Taming Bitwise Behavior in GPU Kernels | 5 | 黑箱重构 cuBLAS/rocBLAS 归约序，Triton 降级强制平衡树归约并静态验证比特级确定性 / Black-box reconstructs GEMM reduction orders; enforces balanced-tree reductions in Triton and statically verifies bit-level determinism. |
| [[2609.11716]] Why Does Post-Training Quantization Work? | 5 | 层间误差反作用（63.4% 抵消）+ LM 头几何保护 Top token，解释 PTQ 鲁棒性 / Layer-introduced errors counteract inherited ones (63.4% cancelled) while LM-head geometry protects top-ranked tokens. |
| [[2609.14845]] Accurate Models of AMD Matrix Cores | 5 | CDNA1-3 矩阵乘法器位精确模型，暴露非 IEEE-754 累加/舍入/下溢行为 / Bit-exact MATLAB models of CDNA1-3 matrix cores expose non-IEEE-754 accumulator, rounding, and underflow behavior. |
| [[2609.06922]] Before the Flip | 4 | 测量量化 VLM 答案未变之前 yes/no logprob 间隙的隐藏移位 / Measures how 4/8-bit compression shifts yes/no log-probability gaps behind unchanged VQA answers. |
| [[2609.07059]] NOVA-CIM | 4 | 随机参考 1-bit 感知+计数取代多比特 ADC，ViT-Base Top-1 84.48% vs BF16 84.51% / Random-reference 1-bit sensing plus counting replaces ADC readout, preserving ViT-Base accuracy. |
| [[2609.07237]] CEDAR | 4 | 由块内 K/V 离散度决定的输出误差界，驱动粗到细稀疏 prefill 路由 / An output-error bound governed by within-chunk key/value dispersion decides which chunks get exact attention. |
| [[2609.07803]] Pruning in Medical Imaging | 4 | 长尾医学影像中低频类先退化；梯度知情剪枝 95% 稀疏下保解释稳定性 / Low-frequency classes degrade first under pruning; gradient-informed pruning preserves explanation stability to 95% sparsity. |
| [[2609.08759]] Scaling in Randomly Rotated Quantization | 4 | 随机旋转量化的缩放与经典 CDEF MMSE 系数经精确毕达哥拉斯恒等式相连 / Connects randomly-rotated quantization scalings to classical CDEF MMSE/unbiased coefficients via a Pythagorean identity. |
| [[2609.09240]] Scaling Post-Training Ternarisation | 4 | Qwen3-8B 端到端三值化（旋转+自适应量化+GPTQ+无损打包），78.5% 机会校正能力保持 / End-to-end ternarisation of Qwen3-8B with lossless packing and 78.5% chance-corrected capability retention. |
| [[2609.09721]] EFQ-Softmax | 4 | 仿射规则直接输出块缩放 E2M1 概率码取代 exp-后量化，核延迟降 40.3% / Direct block-scaled E2M1 probability codes via one affine rule skip the exp, cutting kernel latency 40.3%. |
| [[2609.09823]] AMEND | 4 | 用早期步审计 margin 预测 BLASST 判决，在误丢预算内安全丢弃 KV 块 / Predicts BLASST verdicts from margins audited at earlier steps, enabling safe aggressive KV-block drops. |

### LLM 训练稳定性与可观测性 / LLM Training Stability & Observability（5 篇 / papers）

| 论文 / Paper | 分 / Score | 亮点（中 / EN） / Highlights |
|---|---|---|
| [[2609.11655]] Musec | 5 | 谱裁剪取代 Muon 谱拉平，权重谱范数 300–400 压到 10 以下，附首个谱裁剪 Muon 收敛保证 / Spectral clipping replaces Muon's flattening: weight norms 300–400 → <10, with the first convergence guarantee for a spectral-clipping Muon variant. |
| [[2609.07148]] Stable-MM-R1 | 4 | 势能感知查询挖掘+分层回放对抗多模态 RL 的 rollout 静默与熵坍缩 / Potential-aware query mining and hybrid stratified replay counter rollout silencing and entropy collapse. |
| [[2609.08966]] Good Pretraining, Bad SFT | 4 | 30B MoE 全栈：能存活下游阶段的检查点有更高解密度，而非最佳预训练损失 / In a full 30B MoE pipeline, checkpoints that survive the downstream stack have higher solution density than the best-loss ones. |
| [[2609.09116]] Scale-Invariant Optimization Instability | 4 | 精确离散时间定律：学习率调度与权重衰减经参数范数交互控制有效步长 / An exact discrete-time law: schedules and weight decay interact through the parameter norm to set effective step size. |
| [[2609.10632]] Numbat | 4 | 轨迹级差分预言机验证自建 ML 栈，揪出十处"安静收敛到略差模型"的配方分歧 / A trajectory-level differential oracle surfaces ten silent recipe divergences in a from-scratch ML stack. |

### 大规模机器学习算力基础设施 / Compute Infrastructure for Large-Scale ML（3 篇 / papers）

| 论文 / Paper | 分 / Score | 亮点（中 / EN） / Highlights |
|---|---|---|
| [[2609.07108]] Online Draft Co-Training for Speculative Decoding | 4 | 分支注意力并入负载均衡 zigzag 环注意力+TapChannel 跨流水线特征传输，122B/256K 在线投机共训 / Branch attention merged into zigzag ring attention with cross-stage feature transport enables 122B-scale draft co-training at 256K context. |
| [[2609.07236]] Parallelism Strategy Chaining (CONA) | 4 | 由吞吐与梯度统计代理指标在线切换并行配置，达标困惑度快 1.4–9.6× / Online switching of data/tensor/pipeline parallelism via a surrogate metric reaches target perplexity 1.4–9.6× faster. |
| [[2609.08368]] Miles v0.1 | 4 | 开源生产级 RL 后训练栈，744B-A40B MoE 异步智能体 RL 落地 64 张 GB300 / Open-source production RL post-training stack running asynchronous agentic RL on a 744B MoE over 64 GB300 GPUs. |

### 推理可靠性与 SDC 检测 / Inference Reliability & SDC Detection（2 篇 / papers）

| 论文 / Paper | 分 / Score | 亮点（中 / EN） / Highlights |
|---|---|---|
| [[2609.10126]] SAGE | 5 | 按数值后果分类互连比特故障（灾难性指数翻转 vs 有界尾数损伤），只重放高危类，质量归一延迟降 30% / Classifies interconnect bit faults by numerical consequence and replays only catastrophic ones, cutting quality-normalized latency 30%. |
| [[2609.10861]] REACH | 5 | HBM 控制器长跨距外层 ECC，以少 55.8% 面积在最高错误压力下维持 1.88 TB/s / Long-span outer ECC in HBM controllers sustains 1.88 TB/s under highest error stress with 55.8% less area. |

### 模型系统卡与技术报告 / Model System Cards & Technical Reports（2 篇 / papers）

| 论文 / Paper | 分 / Score | 亮点（中 / EN） / Highlights |
|---|---|---|
| [[2609.07549]] Qwen-Audio-3.0-ASR Technical Report | 4 | 千万小时级 MoE LLM ASR 官方报告，覆盖 30 语言+16 中文方言及流式变体 / Official report on a MoE LLM-based ASR trained on tens of millions of hours, covering 30 languages plus 16 Chinese dialects. |
| [[2609.10712]] An Open Recipe for IMO Gold | 4 | NVIDIA 开放 IMO 金牌配方：双专家模型驱动生成-验证-精炼测试时搜索，数据/代码/检查点全开源 / NVIDIA's open IMO-gold recipe: two post-trained specialists powering generate-verify-refine search, with data, code, and checkpoints released. |

## All Papers

全部入选论文索引（领域列为中英双语 / Full index of all selected papers; the Area column is bilingual）。

| 论文 / Paper | 领域 / Area | 分 / Score |
|---|---|---|
| [[2609.06887]] Human-agent discovery of ferroelectric superdomain control | 自进化智能体 / Self-Evolving Agents | 5 |
| [[2609.06922]] Before the Flip: Hidden Score Shifts in Quantized VLMs | 极致优化可靠性 / Extreme-Opt Reliability | 4 |
| [[2609.06934]] The Geometry of Refusal | 隐状态与可解释性 / Hidden States & Interp | 4 |
| [[2609.06951]] Steering Interference Reflects the Model's Defaults | 隐状态与可解释性 / Hidden States & Interp | 4 |
| [[2609.06966]] MOLE: Detecting Insider Threats in AI Agents | 自进化智能体 / Self-Evolving Agents | 4 |
| [[2609.06972]] AgentDrift: Injection-Hijacked Agent Trajectories | 自进化智能体 / Self-Evolving Agents | 4 |
| [[2609.07037]] Disentangling Steering Vectors | 隐状态与可解释性 / Hidden States & Interp | 4 |
| [[2609.07053]] A Hyperbolicity Atlas of LLM Hidden States | 隐状态与可解释性 / Hidden States & Interp | 4 |
| [[2609.07059]] NOVA-CIM: Stochastic Interfaces for Analog CIM | 极致优化可靠性 / Extreme-Opt Reliability | 4 |
| [[2609.07108]] Online Draft Co-Training for Speculative Decoding | 算力基础设施 / Compute Infra | 4 |
| [[2609.07139]] Encoded Early, Used Late | 隐状态与可解释性 / Hidden States & Interp | 4 |
| [[2609.07148]] Stable-MM-R1: Multimodal Reasoning Dynamics | 训练稳定性 / Training Stability | 4 |
| [[2609.07183]] CircuitLens: Reasoning Circuits for RLVR Data Selection | 隐状态与可解释性 / Hidden States & Interp | 4 |
| [[2609.07204]] Agentic Algorithm Engineering | 自进化智能体 / Self-Evolving Agents | 5 |
| [[2609.07236]] Parallelism Strategy Chaining (CONA) | 算力基础设施 / Compute Infra | 4 |
| [[2609.07237]] CEDAR: Error-Bounded Residual Routing | 极致优化可靠性 / Extreme-Opt Reliability | 4 |
| [[2609.07406]] Think Wider: Latent Rank Collapse in Implicit CoT | 隐状态与可解释性 / Hidden States & Interp | 4 |
| [[2609.07478]] Internal Anatomy of Strategic Choice | 隐状态与可解释性 / Hidden States & Interp | 4 |
| [[2609.07529]] CoER: Adversarial Co-Evolution against Prompt Injection | 自进化智能体 / Self-Evolving Agents | 4 |
| [[2609.07549]] Qwen-Audio-3.0-ASR Technical Report | 系统卡与技术报告 / System Cards & Reports | 4 |
| [[2609.07603]] FinCUABuild | 自进化智能体 / Self-Evolving Agents | 4 |
| [[2609.07611]] AgentIdeaBench | 自进化智能体 / Self-Evolving Agents | 5 |
| [[2609.07655]] Online Surrogate Repair | 自进化智能体 / Self-Evolving Agents | 5 |
| [[2609.07664]] Accuracy is Not Enough | 极致优化可靠性 / Extreme-Opt Reliability | 5 |
| [[2609.07681]] Recall Scaling Laws in Mamba | 隐状态与可解释性 / Hidden States & Interp | 4 |
| [[2609.07746]] LLM Forensics: Where Do Backdoors Hide? | 隐状态与可解释性 / Hidden States & Interp | 4 |
| [[2609.07803]] Pruning, Long-Tail Forgetting in Medical Imaging | 极致优化可靠性 / Extreme-Opt Reliability | 4 |
| [[2609.07876]] LLM Layers Immediately Correct Each Other | 隐状态与可解释性 / Hidden States & Interp | 4 |
| [[2609.07901]] Quantization Amplifies Determinism, Not Bias | 极致优化可靠性 / Extreme-Opt Reliability | 5 |
| [[2609.07925]] FrogNano: 4B Coding Agent via Online Task Synthesis | 自进化智能体 / Self-Evolving Agents | 4 |
| [[2609.08015]] Selective Revalidation for Long-Running Agents | 自进化智能体 / Self-Evolving Agents | 4 |
| [[2609.08126]] SchemeArena | 自进化智能体 / Self-Evolving Agents | 4 |
| [[2609.08135]] KBBQ: FP4 Quantization Noise Law | 极致优化可靠性 / Extreme-Opt Reliability | 5 |
| [[2609.08149]] SWE-Bench Pro Verified | 自进化智能体 / Self-Evolving Agents | 4 |
| [[2609.08173]] Key Path Identification via SAE-based Steering | 隐状态与可解释性 / Hidden States & Interp | 4 |
| [[2609.08175]] Safe Harness Self-Evolution | 自进化智能体 / Self-Evolving Agents | 5 |
| [[2609.08183]] NeoHorse-1 | 自进化智能体 / Self-Evolving Agents | 5 |
| [[2609.08228]] SE-GoS: Self-Evolving Graph-of-Skills | 自进化智能体 / Self-Evolving Agents | 4 |
| [[2609.08248]] Agentic ML Exploration (A-MLE) for Ads Ranking | 自进化智能体 / Self-Evolving Agents | 5 |
| [[2609.08258]] Revoked but Still Authoritative | 自进化智能体 / Self-Evolving Agents | 4 |
| [[2609.08279]] What Eviction Destroys | 自进化智能体 / Self-Evolving Agents | 4 |
| [[2609.08282]] Dreaming in Flow | 自进化智能体 / Self-Evolving Agents | 4 |
| [[2609.08322]] Tracing Stereotypes in Multilingual LLMs | 隐状态与可解释性 / Hidden States & Interp | 4 |
| [[2609.08368]] Miles v0.1: Production-Level Post-Training | 算力基础设施 / Compute Infra | 4 |
| [[2609.08404]] Environments as Scaffold | 自进化智能体 / Self-Evolving Agents | 4 |
| [[2609.08410]] Compositional Multilingual and Behavioral Steering | 隐状态与可解释性 / Hidden States & Interp | 4 |
| [[2609.08574]] Do New Attention Mechanisms Fix Attention Sinks? | 隐状态与可解释性 / Hidden States & Interp | 4 |
| [[2609.08589]] The Unreliable Progress Bar | 自进化智能体 / Self-Evolving Agents | 4 |
| [[2609.08692]] Global Divergence, Local Convergence (SSM vs Transformer) | 隐状态与可解释性 / Hidden States & Interp | 4 |
| [[2609.08696]] MorphoOrgaAgent | 自进化智能体 / Self-Evolving Agents | 4 |
| [[2609.08759]] Scaling in Randomly Rotated Quantization | 极致优化可靠性 / Extreme-Opt Reliability | 4 |
| [[2609.08832]] Closing the Consistency Gap | 自进化智能体 / Self-Evolving Agents | 5 |
| [[2609.08919]] Experience Funnel | 自进化智能体 / Self-Evolving Agents | 4 |
| [[2609.08944]] SkillAdam | 自进化智能体 / Self-Evolving Agents | 4 |
| [[2609.08966]] Good Pretraining, Bad SFT | 训练稳定性 / Training Stability | 4 |
| [[2609.09054]] Training-Free Task Vectors | 隐状态与可解释性 / Hidden States & Interp | 4 |
| [[2609.09085]] It's Not RoPE that Creates Sinks | 隐状态与可解释性 / Hidden States & Interp | 4 |
| [[2609.09095]] Ozaki 2.5: fp64-Emulated GEMM on FP8 Tensor Cores | 极致优化可靠性 / Extreme-Opt Reliability | 5 |
| [[2609.09113]] SAEScientist-Bench | 自进化智能体 / Self-Evolving Agents | 5 |
| [[2609.09116]] Scale-Invariant Optimization Instability | 训练稳定性 / Training Stability | 4 |
| [[2609.09134]] Co-Evolving Harnesses and Models | 自进化智能体 / Self-Evolving Agents | 4 |
| [[2609.09153]] Procedural Graphs | 自进化智能体 / Self-Evolving Agents | 4 |
| [[2609.09219]] Discovery Certification Protocol (DCP) | 自进化智能体 / Self-Evolving Agents | 5 |
| [[2609.09240]] Scaling Post-Training Ternarisation to Qwen3-8B | 极致优化可靠性 / Extreme-Opt Reliability | 4 |
| [[2609.09448]] Calibrating Agent Confidence | 自进化智能体 / Self-Evolving Agents | 4 |
| [[2609.09468]] Code-to-Harness | 自进化智能体 / Self-Evolving Agents | 4 |
| [[2609.09556]] Linear Accessibility in Feature Superposition | 隐状态与可解释性 / Hidden States & Interp | 4 |
| [[2609.09646]] RobustSGPO | 自进化智能体 / Self-Evolving Agents | 4 |
| [[2609.09721]] EFQ-Softmax | 极致优化可靠性 / Extreme-Opt Reliability | 4 |
| [[2609.09776]] Proof-Carrying Cognition | 自进化智能体 / Self-Evolving Agents | 5 |
| [[2609.09823]] AMEND: Nonblocking Drops in GPU-PIM Decoding | 极致优化可靠性 / Extreme-Opt Reliability | 4 |
| [[2609.09849]] NetArtifactBench | 自进化智能体 / Self-Evolving Agents | 4 |
| [[2609.09853]] Era by Eon Benchmark | 自进化智能体 / Self-Evolving Agents | 4 |
| [[2609.09854]] Low-Bit Quantization in Vector Search | 极致优化可靠性 / Extreme-Opt Reliability | 5 |
| [[2609.09875]] AgentAudit | 自进化智能体 / Self-Evolving Agents | 5 |
| [[2609.09902]] Contrastive Projection | 隐状态与可解释性 / Hidden States & Interp | 4 |
| [[2609.09957]] SOLID: Solver-Informed Self-Distillation | 自进化智能体 / Self-Evolving Agents | 4 |
| [[2609.10060]] Reference-Based Bias Detection | 隐状态与可解释性 / Hidden States & Interp | 4 |
| [[2609.10126]] SAGE | 推理可靠性与 SDC / Inference Reliability | 5 |
| [[2609.10210]] Through the Looking Glass | 隐状态与可解释性 / Hidden States & Interp | 5 |
| [[2609.10226]] Φ-Bench | 自进化智能体 / Self-Evolving Agents | 4 |
| [[2609.10287]] Circuit Removability in Soft-Prior Transformers | 隐状态与可解释性 / Hidden States & Interp | 4 |
| [[2609.10299]] A Dominant Diffuse Phase in the SAE Phase Diagram | 隐状态与可解释性 / Hidden States & Interp | 5 |
| [[2609.10315]] TRACE: Causal Exploration with Synthesized Rewards | 自进化智能体 / Self-Evolving Agents | 4 |
| [[2609.10494]] IBIB | 自进化智能体 / Self-Evolving Agents | 4 |
| [[2609.10539]] IdeaAMBIG | 自进化智能体 / Self-Evolving Agents | 4 |
| [[2609.10632]] Numbat | 训练稳定性 / Training Stability | 4 |
| [[2609.10702]] Data-Efficient Language Modeling | 自进化智能体 / Self-Evolving Agents | 5 |
| [[2609.10712]] An Open Recipe for IMO Gold | 系统卡与技术报告 / System Cards & Reports | 4 |
| [[2609.10724]] Finishing the Task Is Not Enough | 自进化智能体 / Self-Evolving Agents | 4 |
| [[2609.10861]] REACH | 推理可靠性与 SDC / Inference Reliability | 5 |
| [[2609.11028]] BenchShield | 自进化智能体 / Self-Evolving Agents | 5 |
| [[2609.11147]] Autonomous Chemical Mechanistic Discovery | 自进化智能体 / Self-Evolving Agents | 5 |
| [[2609.11356]] Taming Bitwise Behavior in GPU Kernels | 极致优化可靠性 / Extreme-Opt Reliability | 5 |
| [[2609.11655]] Musec | 训练稳定性 / Training Stability | 5 |
| [[2609.11716]] Why Does Post-Training Quantization Work? | 极致优化可靠性 / Extreme-Opt Reliability | 5 |
| [[2609.12655]] LifeMem | 自进化智能体 / Self-Evolving Agents | 5 |
| [[2609.13073]] Autonomous Research for Telecom Ticket Retrieval | 自进化智能体 / Self-Evolving Agents | 5 |
| [[2609.13406]] Generalized Agent Iteration | 自进化智能体 / Self-Evolving Agents | 5 |
| [[2609.14845]] Accurate Models of AMD Matrix Cores | 极致优化可靠性 / Extreme-Opt Reliability | 5 |

---

## 核对说明 / Verification Note

- `filtered_papers.json` 中 `total_selected` = **100**；本文 "All Papers" 表共 **100** 行，`papers` frontmatter 字段 = 100，数量一致。
- 分主题统计 / per-topic counts: 自进化智能体与自动化研究 48、LLM 隐状态与可解释性 24、极致性能优化下的可靠性 16、LLM 训练稳定性与可观测性 5、算力基础设施 3、推理可靠性与 SDC 检测 2、模型系统卡与技术报告 2；合计 100，与 `total_selected` 一致，无差异 / no discrepancy。
- 必读 8 篇 + 备选 4 篇全部选自已精读的 15 篇 5 分论文 / all must-reads are drawn from the 15 score-5 summaries read in full.
