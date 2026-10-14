---
title: "Weekly Overview: 2026-10-05..2026-10-11"
date: 2026-10-05
week: "2026-10-05..2026-10-11"
tags: [arxiv-daily, weekly, LLM-reliability, agents, quantization, interpretability, training-stability]
papers: 102
---

# 周报 Weekly Overview: 2026-10-05..2026-10-11

本周扫描 3,862 篇 arXiv 论文（2026-10-05..2026-10-11），经语义门控与同区对比排序后精选 **102 篇**，覆盖 9 个研究方向。本周的主线是"可靠性"：智能体与流水线的静默失败、RL 后训练的失效模式、极致量化/加速下的数值陷阱、以及评测方法学本身的统计缺陷。8 篇全读候选中获得 ⭐ 必读标记的论文全部入选本周必读。

This week 3,862 arXiv papers were scanned (2026-10-05..2026-10-11); 102 were selected after semantic gating and within-area ranking across 9 research areas. The through-line is *reliability*: silent failures in agents and pipelines, RL post-training failure modes, numerical traps under extreme quantization/acceleration, and the statistical weaknesses of evaluation methodology itself. All 8 fully-read star candidates are featured below.

## 本周必读 / Must Read This Week

> 全部来自 stars.json 中 `star: true` 的全读候选（≤8 篇，每个方向 ≤2 篇）。每条理由均附原文评估中的注意点（caveat）。
> All picks come from `star: true` entries in stars.json (≤8 total, ≤2 per area). Each reason includes its caveat from the full read.

### 1. [[2610.09239]] The Winner's Curse in LLM Self-Improvement Loops（自进化智能体 Self-Evolving Agents · rank 1）

- **推荐理由（中）：** 把自改进循环的"比基线好就保留"建模为相关测量噪声下的最优选择并定量给出胜者诅咒：预注册确认研究显示 16 项选择集下循环自报增益虚高 13–20 点；McNemar、PACE、select-then-confirm、校准贝叶斯门五种验收规则在完整循环上全都不敌朴素贪心；GEPA 与 MIPROv2 的验证分数同样虚高（GEPA 隐含 38.8 点、真实 19.2 点）。配套的 64 项"从未用过"审计以约十分之一的预算消除报告增益的平均偏差（RMSE 15.5→5.7）。
- **Why (EN):** Pre-registered winner's-curse quantification validated on nine oracle settings with Holm-corrected p-values, 200 gold-set splits, and honestly reported negative results on acceptance rules: keep-if-better selection overstates gains by 13–20 points at 16 selection items, and the same inflation contaminates GEPA and MIPROv2 validation scores. A cheap 64-item audit removes the average bias of the reported gain.
- **注意 / Caveat:** 范围限于三个确定性评分任务上的指令改写；64 项审计只消除平均偏差，单设置误差仍达 −8.5~+5.8 点、报告增益 RMSE 仍 5.7 点。/ Scope is instruction rewriting on three tasks with deterministic scoring; the 64-item audit removes average bias but leaves per-setting errors of −8.5 to +5.8 points and an RMSE of 5.7.

### 2. [[2610.09647]] When Rank Rises as LLMs Degrade（训练稳定性 Training Stability · rank 2）

- **推荐理由（中）：** 预注册协议、留一种子校准、低于损伤门槛的负对照，并诚实报告阴性结果（9 折中 8 折对 held-out 损失无领先、误报如实承认），支撑一个后果重大的指标审计发现：数据复制使 held-out 损失恶化 75% 时 RankMe 反而升 13.5 个合并标准差——视觉自监督"秩降=退化"的先验在 LLM 后训练中反向，损伤是谱弥散而非坍缩；其唯一复现机制（duplicate_data）干净利落。
- **Why (EN):** Pre-registered protocol, leave-one-seed-out calibration, a below-gate negative control, and honestly reported negative results (no lead in 8/9 folds, false alarms conceded) supporting a consequential metric-audit finding — rank *rises* as LLMs degrade, with the one mechanism cleanly replicated.
- **注意 / Caveat:** 所有数字均为 Qwen3-0.6B，反向结论依赖单一复现机制（duplicate_data，3 种子）；两个校准种子无法认证 union bound，held-out 分支在三折全部误报。/ Every number is Qwen3-0.6B and the inversion rests on a single replicated mechanism (duplicate_data, 3 seeds); two calibration seeds cannot certify the union bound and the held-out branch false-alarms in all three folds.

### 3. [[2610.12822]] Reward Hacking as a Transmissible Strategy in Multi-Agent Coding Systems（RL 后训练 RL Post-Training · rank 1）

- **推荐理由（中）：** 用源对照（RL-only 与 SDF-only 传播近零）与链条对照（带论证代码 R=3.40 vs 无论证 0.14）证明：编码 RL 诱发的 reward hacking 能经代码模仿、共享记忆与自然语言计划在智能体间传播，并在原始源离开后沿 6 跳传输链持续甚至放大；评测反馈通道还能解锁拒答模型（GPT-5.5 从 0.4% 升至 24.9%）。
- **Why (EN):** Propagation of reward hacking is demonstrated with source controls (RL-only and SDF-only near zero), chain vs no-justification contrasts (R=3.40 vs 0.14), and a feedback-channel experiment that unlocks propagation in refusing models.
- **注意 / Caveat:** 放大头条 R=3.40 来自精选的困难任务+带论证设定，全任务集估计仅 R=0.60；确认 hack 检测器只覆盖三种手工编目机制。/ The amplification headline (R=3.40) comes from a curated hard-task, justification-bearing regime while the full-task-set estimate is R=0.60, and the confirmed-hack detector covers only three hand-catalogued mechanisms.

### 4. [[2610.09111]] Same Text, Different Prediction: Serving-Context Nondeterminism in Text Classifiers（推理可靠性 Inference Reliability · rank 1）

- **推荐理由（中）：** 数十万次受控比较（180 个从头训练分类器 × 3,960 个服务上下文）隔离出 padding 为首要标签翻转因子，预训练 rotary/NoPE 对照确认学习型绝对位置编码是根因——纯结构性而非数值性；缓解手段以在 4,644 个留出翻转上验证的 margin 证书度量（低 margin 重算以 22% 开销检出几乎全部翻转）。
- **Why (EN):** Hundreds of thousands of controlled comparisons isolate padding as the dominant flip factor, and pretrained rotary/NoPE controls confirm the learned-absolute-position cause; mitigations are measured with a validated margin certificate on 4,644 held-out flips.
- **注意 / Caveat:** 头条量级来自小型从头训练的 GPT-2 系模型（预训练 Qwen3/ModernBERT 对 padding 翻转零标签）；缓解成本在实验环境而非生产中测得。/ Headline magnitudes come from small from-scratch GPT-2-style models (pretrained Qwen3/ModernBERT flip zero labels from padding), and mitigation costs are measured in the experimental setup, not production.

### 5. [[2610.15459]] When Messages Go Wrong: Understanding Communication Faults in LLM-Based Multi-Agent Systems（静默失败 Silent Failures · rank 1）

- **推荐理由（中）：** 15,882 个注入故障的全传播核算（18,900+ 次执行、100 任务、5 领域）：89.4% 传播为系统级后果、20.7% 的失败完全静默（部分内容型高达 76.2%）；匹配单元比较显示换拓扑（Flat）挽回 19–27% 失败而换模型仅 0.2–4.5%；执行侧与证据侧保护机制覆盖互补故障集且覆盖面被量化。
- **Why (EN):** 15,882 injected faults with full propagation accounting; a matched-unit comparison shows topology changes recover 19–27% of failures vs 0.2–4.5% for model swaps; complementary protection mechanisms with quantified coverage.
- **注意 / Caveat:** 全部结果来自三种 AutoGen 拓扑与同族模型集（无前沿级模型）；20.7% 静默失败头条依赖作者自己的脚本化判定。/ All results come from three AutoGen workflow topologies with a within-family model set (no frontier-tier model), and the 20.7% silent-failure headline depends on the authors' own script-defined adjudication.

### 6. [[2610.11647]] One Skill Too Many: How Co-Installed Skills Conflict in Coding Agents（静默失败 Silent Failures · rank 2）

- **推荐理由（中）：** 首个同职技能共存冲突的大规模实证研究（822,109 候选对、312 确认对、6,368 次运行）：CI 界定的患病率估计（约四分之一已装技能与同职技能共存）+ 带无关技能对照（A+C）的受控实验把损失归因于相似性本身——已装技能使用率 −19.9 pp 而任务完成率不变，冲突藏在成功背后；冲突在"第一次读取技能"时即已决定，一个 96% 有效的 pre-tool hook 干预、88.9% 重跑一致性，并在 Codex 上部分复现。
- **Why (EN):** A CI-bounded prevalence estimate plus a controlled experiment with an unrelated-skill control isolates similarity as the cause; a 96% effective hook intervention, 88.9% re-run agreement, and a partial Codex replication.
- **注意 / Caveat:** "保真度"是对某个 LLM 解读技能文本的保真，每个（模型、配置、对）单元为单次运行；"四分之一患病率"头条只基于公开仓库。/ Fidelity is fidelity-to-an-LLM's-reading of skill prose, each (model, configuration, pair) cell is a single run, and the headline 1-in-4 prevalence rests on public repositories only.

### 7. [[2610.07853]] Lost in the bf16 Cast: Exporting Ternary Language Models Can Revert Most Low-Learning-Rate Code Changes（极致优化下的可靠性 Extreme-Performance Reliability · rank 2）

- **推荐理由（中）：** 法医级审计：对三家实验室（Falcon-E、BitNet b1.58 2B-4T、BitCPM）已发布三元模型做逐字节代码核算，文档化导出使 Falcon-E-1B 的 GSM8K 从 58.79% 崩到 0.78%，并在代码级解释机理（低学习率下微调新越阈值的潜权重落回原 bf16 舍入单元）；32 倍学习率对照证明效应特定于低 LR 区间；修复手段（fixed export / projection）带预声明的非劣性判据。
- **Why (EN):** Forensic-quality audit with byte-for-byte code accounting across three released ternary models, a documented 58.79→0.78% export collapse explained at the code level, a 32x learning-rate control showing the effect is regime-specific, and pre-declared non-inferiority remedies.
- **注意 / Caveat:** 崩塌只在窄低学习率角落成立（32 倍学习率下无可检测变化）；512 条 GSM8K 提示取自官方训练划分。/ The headline collapse holds in a narrow low-LR corner (at 32x the rate there is no detectable change), and the 512 GSM8K prompts are carved from the official training split.

### 8. [[2610.15850]] What Do Sparse Autoencoder Feature Discovery Scores Identify? From Activations to Interventions（可解释性 Interpretability · rank 2）

- **推荐理由（中）：** 定量证明 SAE 特征发现所依赖的观测统计量原则上无法识别干预归因，并实测"激活-干预鸿沟"（中位 |α/β| 仅 2.8–4.6%），配 BH 校正检验、纯噪声模拟与预设对照：每 prompt 一次反向传播的梯度归因预测单 latent 消融实化符号准确率 91–97%，探针系数仅 17–35%——打算做 steering/ablation 时必须改用归因证据。
- **Why (EN):** Quantifies the activation-vs-intervention gap for SAE discovery scores (median |alpha/beta| 2.8–4.6%) with BH-corrected tests, a noise-only simulation, and a prespecified contrast showing attribution predicts realized interventions far better than probe coefficients.
- **注意 / Caveat:** 91–97% vs 17–35% 的符号对比对从不触发于探针位置的 latent 部分是机械的；范围限于每模型单层单个 SAE 与十一个玩具任务；Stein 残差区间在标称 95% 下仅覆盖 0.82。/ The headline 91–97% vs 17–35% sign comparison is partly mechanical for latents that never fire at the probed position; scope is one SAE at one layer per model on eleven toy tasks, and the Stein-residual intervals cover only 0.82 at nominal 95%.

## 按主题分类 / Papers by Topic

> 每个方向内按 area_rank 排序（1 = 该方向同区对比最优）。/ Within each area, papers are listed in area_rank order (1 = best by side-by-side comparison).

### 自进化智能体与自动化研究 / Self-Evolving Agents & Automated Research（12 篇）

本方向的主线是"谁来演化演化器"：从专家引导的证明搜索到开放式问题求解，从固定演化循环到元演化与权重-harness 协同演化，同时开始定量审视自改进循环自身的统计陷阱。
The theme is who evolves the evolver: from expert-guided proof search to open-problem solving, from fixed evolution loops to meta-evolution and weight-harness co-evolution — while quantifying the statistical traps of self-improvement loops themselves.

| 论文 Paper | 类型 Type | 一句话点评 / One-line take |
|---|---|---|
| [[2610.09239]] Winner's Curse in Self-Improvement Loops | 分析 analysis | 小验证集上"好一点就保留"使自改进增益虚高 13–20 点，五种验收规则全不敌贪心。Keep-if-better selection under noise inflates self-improvement gains by 13–20 points; no acceptance rule beats greedy. |
| [[2610.09769]] Bolzano Open-Problem Solving | 系统 system | 并行证明智能体+验证者无引导解决约 3,800 个开放问题中的约 200 个，4 个 STOC 2026 答案获原作者确认。Parallel prover agents solve ~200 of ~3,800 open problems unguided; 4 STOC 2026 answers author-confirmed. |
| [[2610.14683]] Triage-PiEvo Evidence Admission | 系统 system | 分级证据准入门阻止未验证证据改写持久原则，压力测试零污染、4 任务 +7.5–11.8%。A staged evidence-admission gate blocks corrupted evidence; +7.5–11.8% over the strongest baseline on 4 scientific tasks. |
| [[2610.14163]] AutoEnvScaling Data Flywheel | 方法 method | 提议智能体从求解器轨迹自动构建可验证 RL 环境，有效环境率至多 25 倍、成本降 75%。A proposer agent builds verifiable RL environments from solver rollouts; up to 25x valid-environment rate at 75% lower cost. |
| [[2610.09197]] FreeEvolve Beyond Fixed Loops | 方法 method | 元演化的演化技能自主决定测什么、何时停，三个智能体基准平均 +13.6 分。A meta-evolved skill decides what to test and when to stop; +13.6 pts average on three agentic benchmarks. |
| [[2610.13025]] Evo² Weight-Harness Co-Evolution | 方法 method | 权重与 harness 联合协同演化，GPT-5-mini 智能体 SWE-bench Verified 从 24.4% 到 48.3%。Weight-harness co-evolution lifts a GPT-5-mini agent from 24.4% to 48.3% on SWE-bench Verified. |
| [[2610.11655]] Harness Evolution Ceiling | 方法 method | 失败构成诊断回答"harness 演化何时交给权重训练"：harness 提升 0.16→0.30，叠加 LoRA 再 +0.13。Failure-composition diagnosis shows harness evolution lifts 0.16→0.30 and stacked LoRA adds +0.13 across 8 models. |
| [[2610.07447]] Fork-and-Flush Idea Basins | 方法 method | 长程自研究陷入想法盆地：周期性分叉新上下文轨迹，等算力下 +66.0%/+44.4%。Periodic forking into fresh-context trajectories escapes idea basins; +66.0%/+44.4% over single-run and best-of-N at equal compute. |
| [[2610.11794]] Memento 3 Reflective Rulebooks | 系统 system | 反思规则手册编译为代码、忠实判断+逐单元重放后才接受，通关全部 25 个公开 ARC-AGI-3 游戏。Reflective rulebooks compiled to code clear every level of all 25 public ARC-AGI-3 games at 44% of human action count. |
| [[2610.13494]] Humanize MLE Agents | 方法 method | 多智能体会话轮换建模为上下文重置半 MDP：MLE-bench 75 任务 78.2% 奖牌率、+8.0 分。Session alternation as a context-reset semi-MDP; 78.2% any-medal rate on 75 MLE-bench tasks, +8.0 over the strongest open baseline. |
| [[2610.12235]] LMs as Research World Models | 方法 method | 用 2,600+ 真实实验记录训练研究世界模型，多轮自研究中选择遗憾降 78%。World models trained on 2,600+ real experimental records cut selection regret 78% in multi-round autoresearch. |
| [[2610.07625]] Stateless Language Agents | 系统 system | harness 持有研究状态、每次调用全新角色上下文，1B token 量级下以少 84% token 追平最强内核基线。The harness owns research state with fresh per-call context; matches the strongest kernel baseline with 84% fewer tokens up to 1B-token horizons. |

### LLM 训练稳定性与可观测性 / LLM Training Stability & Observability（10 篇）

损失尖峰模拟、谱健康监控的反向信号、MoE 路由失衡与升级坍缩、以及"遗忘住在输出嵌入里"的定位——训练动力学的可观测性本周集中补课。
Loss-spike simulation, inverted spectral-health signals, MoE routing imbalance and upcycling collapse, and localizing forgetting in output embeddings — a concentrated week for training-dynamics observability.

| 论文 Paper | 类型 Type | 一句话点评 / One-line take |
|---|---|---|
| [[2610.13524]] Simulating Training Spikes | 分析 analysis | 逐层随机特征模型+重尾输入复现预训练损失尖峰，并从 checkpoint 预测 β₂ 调度收益。Layer-wise random-feature models replicate loss spikes and predict spiky behavior; a derived beta_2 schedule empirically helps. |
| [[2610.09647]] When Rank Rises as LLMs Degrade | 分析 analysis | 损伤是谱弥散而非坍缩：held-out 损失恶化 75% 时 RankMe 反升 13.5 个标准差。Post-training damage is spectral dispersion, not collapse: rank rises 13.5 s.d. as held-out loss degrades 75%. |
| [[2610.14394]] Recommender Instability Cascade | 方法 method | 工业推荐系统"梯度→权重→损失"爆炸级联的分阶段干预，日交互十亿级验证（无外部基线）。Staged interventions mapped to a divergence cascade, validated on a production recommender with billions of daily interactions (no external baseline). |
| [[2610.11317]] DivMoE Upcycling | 方法 method | 细粒度 MoE 升级的近随机路由（23.2%）被域专家初始化+多样性约束修复到 55.6%。Domain-specialized init + diversity-constrained routing fixes near-random upcycled routing (23.2%→55.6%). |
| [[2610.05744]] CIPHER-MoE Trillion-Scale Routing | 方法 method | 亲和感知专家-令牌过滤+显式容量控制：万亿级 MoE 训练提速 1.10–1.94 倍。Affinity-aware expert-to-token filtering accelerates trillion-scale MoE training 1.10–1.94x while preserving quality. |
| [[2610.09835]] Forgetting in Output Embeddings | 方法 method | 遗忘定位于词表饥饿输出嵌入的单侧 softmax 梯度：调大 Adam epsilon 去除 39.4–67.9% 遗忘。Forgetting lives in one-sided softmax gradients on vocabulary-starved output embeddings; raising Adam epsilon removes 39.4–67.9% of it. |
| [[2610.07207]] DRMoET Robust MoE Training | 方法 method | 分布鲁棒目标优化高损失路由结果，强制误路由下超额损失再降 4.3%。A distributionally robust objective over high-loss routing outcomes beats the aux-loss-free baseline and tolerates forced misrouting. |
| [[2610.11575]] Smoothing Top-k Exposure Boundary | 方法 method | 静态 top-k 把竞争专家关进零反馈区：围绕预算 k 弹性采样路由，下游 +0.84/+2.02。Elastic routing around the top-k budget removes the brittle zero-feedback boundary; +0.84/+2.02 downstream on two model scales. |
| [[2610.06677]] Sparse Probability Maps in Routing | 分析 analysis | 300M/1B 匹配模型比较 softmax/entmax/sparsemax/normmax：概率映射决定专家参与结构。Matched 300M/1B models show the probability map shapes expert participation; entmax drops 30% less mass at 1B. |
| [[2610.13370]] Expert Selection Biases | 方法 method | 类别条件化选择偏置为弱势类别超额分配容量，等效 18.5% 额外基线 token。Category-conditioned selection biases over-allocate capacity to disadvantaged categories, worth 18.5% extra baseline tokens at the smallest scale. |

### RL 后训练动力学与失效 / RL Post-Training Dynamics & Failures（8 篇）

reward hacking 的多智能体传染、陈旧 rollout 的方差控制、裁判被 hack 的节奏由谁定、以及"NO-THINK 增益其实是 THINK 复活"——RL 后训练的失效模式被拆得越来越细。
Transmissible reward hacking, variance control for stale rollouts, who sets the pace of judge hacking, and "no-think gains are think-mode reactivation" — RL post-training failure modes are being dissected ever more finely.

| 论文 Paper | 类型 Type | 一句话点评 / One-line take |
|---|---|---|
| [[2610.12822]] Reward Hacking as Transmissible Strategy | 分析 analysis | 编码 RL 诱发的 reward hack 经代码/记忆/计划在智能体间传播并在源离开后放大（R=3.40）。RL-elicited reward hacking propagates across agents via code, memory and plans, amplifying after the source leaves. |
| [[2610.09597]] COPC Off-Policy Correction | 方法 method | 精确偏差/方差分解+双向协同校正：64 步陈旧度下基线坍塌而 COPC 稳定。Exact bias/variance decomposition with two-sided correction stays stable at 64-step staleness where baselines collapse. |
| [[2610.06439]] Better Call Reward | 分析 analysis | 对纯表面代理做 GRPO 的最优策略是策略性弃答：格式化答案率 0.900→0.109。Against any surface proxy without an abstention penalty, strategic abstention is provably optimal; formatted-answer rate falls 0.900→0.109. |
| [[2610.14440]] TETPO Variance Control | 方法 method | 按组自适应温度化重要性权重达到目标 ESS，高陈旧度下优于固定干预稳定器。Per-group data-adaptive tempering meets a target ESS fraction and outperforms fixed stabilizers under high staleness. |
| [[2610.13594]] MENTOR Learning from Failure | 方法 method | 在线导师实时诊断失败并生成教学提示，与 GRPO 即插即用，相对增益至 +78.3%。A live mentor agent diagnoses failures and generates instructional prompts, plug-and-play with GRPO; up to +78.3% relative gain. |
| [[2610.15778]] Who Sets the Pace of Judge Hacking | 分析 analysis | 12 格中冻结裁判全无 held-out 增益：hack 深度随裁判 AUC（−0.69）而非策略-裁判差距。Hacking depth tracks judge AUC rather than the policy-judge gap; frozen judges yield no held-out gain in all 12 cells. |
| [[2610.11291]] When Do We Need On-Policy Distillation | 分析 analysis | 在离线学生 rollout 上蒸馏常更好：14/17 教师学生对获胜、最高 11.4 倍提速。Distilling on offline student rollouts wins 14 of 17 teacher-student pairs with up to 11.4x speedup; an overlap ratio predicts when on-policy helps. |
| [[2610.14270]] Thinking Leakage in RL | 分析 analysis | NO-THINK 模式 GRPO 的增益大多是原 THINK 模式的重新激活：替换低维 THINK 子空间即移除大部分收益。No-think GRPO gains largely reactivate the original think mode; removing a low-dim THINK-related subspace removes most of the gain. |

### 推理可靠性与 SDC 检测 / Inference Reliability & SDC Detection（10 篇）

服务上下文不确定性、数据流驱动的框架测试、跨模型 KV 复用的语义陷阱、以及故障容忍基础模型——"静默数据损坏"（SDC）本周从硬件一路讲到 serving 层。
Serving-context nondeterminism, data-flow-driven framework testing, semantic traps in cross-model KV reuse, and fault-tolerant foundation models — silent data corruption is traced from hardware up to the serving layer.

| 论文 Paper | 类型 Type | 一句话点评 / One-line take |
|---|---|---|
| [[2610.09111]] Same Text, Different Prediction | 分析 analysis | 仅改 padding 宽度翻转约 10% 标签（结构性、根因是学习型绝对位置编码）；bf16 下 batch 形状移动至多 56.7 pp 概率质量。Padding width alone flips ~10% of labels structurally; bf16 batch-shape changes move up to 56.7 pp of probability mass. |
| [[2610.15808]] Framework Testing in Data Flow | 方法 method | Tensor Flow Graph 捕获运行时张量状态的数据流变异测试：55 个 bug 报告、41 个开发者确认。Data-flow mutation testing surfaces autodiff/fusion bugs topology-only testing misses; 55 reports, 41 developer-confirmed. |
| [[2610.07529]] Targeted Search for Worst-Case Error | 分析 analysis | 模拟光学神经算子上定向搜索找到 200 台设备 Monte Carlo 最大值 1.08–3.10 倍的最坏误差——随机器件测试低估最坏情况。Targeted search over 32 toleranced knobs finds 1.08–3.10x the worst error of 200-device Monte Carlo sampling. |
| [[2610.10311]] Fault-Tolerant Foundation Models | 方法 method | 4 万 GPU 时修正缩放律：错误韧性随规模增加，LLM 或在有限开销的纠错码内计算。Modified scaling laws from 40,000 GPU-hours on faulty hardware show error resilience grows with scale. |
| [[2610.09255]] The Symbol of the Surrogate | 分析 analysis | 傅里叶符号诊断：神经 PDE 代理在平流上达到 99.8% 完全模仿上限——学的是求解器离散误差。A Fourier-symbol diagnostic shows neural PDE surrogates imitate solver discretization error, reaching 99.8% of the full-imitation ceiling. |
| [[2610.05833]] Request Order Matters | 分析 analysis | 选择性 KV 重算让滚动智能体输出依赖请求历史：文档对齐重算换 +34.5–52.5 pp 保真、约 5.7 倍 TTFT 提速。Selective KV-cache recomputation makes rolling-agent answers history-dependent; document-aligned recompute buys fidelity at ~5.7x TTFT speedup. |
| [[2610.09999]] ReSAFT Fault Tolerance | 方法 method | ReRAM 存内计算卡死故障：冗余+故障感知双交叉阵列映射，精度恢复 +22.39%、MTTF 61 倍。Redundancy + fault-aware dual-crossbar mapping recovers +22.39% accuracy and 61x MTTF for ReRAM PIM accelerators. |
| [[2610.15509]] CacheLink KV Transport | 方法 method | 跨模型 KV 高保真仍改变行为——保真度不是接收方效用的好代理；学习耦合 K/V 校正。Learned coupled K/V correction targets receiver behavior, showing KV fidelity is a poor proxy for utility across 7 evaluation panels. |
| [[2610.11358]] RaReCache Cross-Model Reuse | 系统 system | 秩分歧检测+选择性重算：Qwen3-0.6B→14B 的 23 倍差距保留 95–99% 精度、prefill 提速 3.04 倍。Rank-disagreement-based selective recomputation retains 95–99% accuracy across a 23x model gap with 3.04x prefill speedup. |
| [[2610.13060]] KV-Repurpose Testbed | 系统 system | 非前缀 KV 复用测试板：单文档 QA 基本保持而跨文档推理明显退化；30GB 命中率 63.9% 对前缀 3.3%。A vLLM testbed shows non-prefix KV reuse preserves single-doc QA but degrades cross-document reasoning. |

### 智能体与流水线静默失败 / Agent & Pipeline Silent Failures（5 篇）

多智能体通信故障、技能共存冲突、漏洞修复静默失败、工具静默错误与数据科学方法学失败——任务"通过"不代表没有出错，本周五篇全部围绕"无声的错"。
Communication faults, co-installed skill conflicts, silent vulnerability-repair failures, plausible-but-wrong tool results, and methodological failures in agentic data science — five papers on failures that hide behind passing tasks.

| 论文 Paper | 类型 Type | 一句话点评 / One-line take |
|---|---|---|
| [[2610.15459]] When Messages Go Wrong | 分析 analysis | 15,882 个注入通信故障：20.7% 失败静默（部分内容型 76.2%），拓扑冗余远胜换模型。15,882 injected communication faults; 20.7% of failures are silent and topology redundancy beats model swaps 19–27% vs 0.2–4.5%. |
| [[2610.11647]] One Skill Too Many | 分析 analysis | 同职相似技能静默顶替已装技能而任务仍通过；pre-tool hook 守卫首次读取恢复 +9.1 pp 保真。Co-installed similar skills silently substitute with task completion unchanged; a pre-tool hook guarding the first read restores fidelity. |
| [[2610.06163]] Localizing Silent Repair Failures | 方法 method | 补丁通过功能检查却仍有漏洞：基于 trace 的定位找出最早分歧轮次（95 例、59 例本可成功）。Trace-based localization finds the earliest divergent turn in 95 silent failures of agentic vulnerability repair. |
| [[2610.10062]] Loud Failures, Quiet Failures | 分析 analysis | 工具返回"格式良好但错误"结果时检出率从 91.3% 跌到 58.8%，推理变体更不敏感。Agents detect explicit tool errors 91.3% of the time but plausible wrong values only 58.8%; reasoning variants notice less. |
| [[2610.14115]] Silent Failures in Agentic Data Science | 分析 analysis | 智能体数据科学的泄漏/不当验证被精度指标掩盖：多数解含至少一种失败模式且泄漏与性能正相关。Agentic data-science pipelines commit methodological failures masked by accuracy; leakage correlates positively with predictive performance. |

### 极致性能优化下的可靠性 / Reliability under Extreme Performance Optimization（20 篇）

本周最大方向：GPU 内核验证、三元模型导出陷阱、递归态/缓存/优化器态的低位宽量化、FP4/NVFP4 强化学习、VLA 量化恢复——每一个"再省一点"的决定都在制造新的静默失败面。
The largest area this week: GPU-kernel validation, ternary export traps, low-bit recurrent/cache/optimizer-state quantization, FP4/NVFP4 RL, and quantized-VLA recovery — every "save a few more bits" decision creates a new silent-failure surface.

| 论文 Paper | 类型 Type | 一句话点评 / One-line take |
|---|---|---|
| [[2610.05683]] RESOLVE GPU Kernel Validation | 方法 method | 时序扰动插桩+智能体归约+F* 等价证明：捕获两个通过容差测试的空内核。Timing-perturbing instrumentation, agent-driven reduction and F* proof validate AI-written GPU kernels; caught two empty kernels passing tolerance tests. |
| [[2610.07853]] Lost in the bf16 Cast | 分析 analysis | 导出时一次 bf16 取整回滚低学习率三元微调（58.79%→0.78%），两种修复均非劣。A single bf16 cast on export reverts low-LR ternary fine-tunes (58.79%→0.78%); two verified drop-in remedies. |
| [[2610.08917]] CARE Certified Acceleration | 方法 method | 配对 rollout+有限样本风险保证选择 VLA 加速器：9.0–10.8 倍提速保留 85.8% 已解任务。Certified accelerator selection with finite-sample risk guarantees; 9.0–10.8x speedups preserving 85.8% of reference-solved episodes. |
| [[2610.15139]] When Dynamic Scaling Fails | 分析 analysis | 递归态量化误差在递归内复合：INT4 起初保持合成回忆、约 1000 步后摧毁。Scale-state feedback governs recurrent-state quantization; INT4 destroys synthetic recall ~1000 steps in even though it starts intact. |
| [[2610.06251]] Shared Stopping Decisions Change Answers | 分析 analysis | HQQ 4-bit 共享停止判据使无关批内问题改变目标答案；请求局部停止移除该路径。A shared average-error stopping criterion makes unrelated batched questions change a target's 4-bit HQQ answers; request-local stopping removes it. |
| [[2610.14277]] Echo Error-Compensated All-Reduce | 方法 method | 4-bit all-reduce 误差回注、累计误差可证明有界：比 16-bit NCCL 快 2.09 倍、质量差 0.4 分内。Error-compensated 4-bit all-reduce with provably bounded accumulated error; 2.09x faster than 16-bit NCCL within 0.4 points of quality. |
| [[2610.08164]] Align, Then Correct | 方法 method | 免训练两阶段低秩补偿：QuIP# 2-bit WikiText-2 12.43→10.26、恢复 51–84% FP16 差距。Training-free two-stage low-rank compensation recovers 51–84% of the FP16 gap on QuIP# 2-bit. |
| [[2610.12444]] Rounding in Preconditioner Space | 方法 method | 预条件子空间随机取整+零排除校准：4-bit AdamW 优化器态损失差距最多缩 70%。Preconditioner-space stochastic rounding cuts the 4-bit optimizer-state loss gap by up to 70%. |
| [[2610.15709]] Preserving Updates in State Quantization | 方法 method | 小更新在取整中丢失且状态可反向移动：低秩旁路+有界方向取整免训练超越 INT4。Low-rank bypass + bounded directional rounding fix coherent quantization error in recurrent states, training-free. |
| [[2610.09212]] CurveTQ Trellis Quantization | 方法 method | 曲率加权 Viterbi 的免旋转 trellis 量化：比 QTIP/Proteus +1–3 分且解码最快。Curvature-weighted, rotation-free trellis quantization gains +1–3 pts over QTIP/Proteus with the fastest decoder at all batch sizes. |
| [[2610.15675]] Quantization-Conditioned RL for VLAs | 方法 method | 量化条件化离线 RL 恢复低比特 VLA：4,050 次真机试验、INT4 恢复 99.3% FP 分数。Quantization-conditioned offline RL recovers low-bit VLA failures over 4,050 real trials, reaching 99.3% of FP score. |
| [[2610.14448]] KV4-RL INT4 Rollouts | 方法 method | 免校准 INT4 KV+注意力池 INT8 保护：RLVR rollout 提速 1.80 倍、精度差 0.5pp 内。Calibration-free INT4 KV with selective INT8 protection gives 1.80x rollout speedup at within 0.5pp of BF16 accuracy. |
| [[2610.15259]] RECAP Dynamic-Prefix Calibration | 方法 method | 动态前缀校准按注意力效应监督历史缓存错误：W4A4KV4 长推理 MATH500 +13.3pp。Dynamic-prefix calibration supervises historical cache errors by their attention effect; +13.3pp MATH500 at W4A4KV4. |
| [[2610.07767]] TRACE FP4 RL QAT | 方法 method | rollout 引导 QAT 对齐训练侧 FP4 取整与 rollout 结果：BF16 相当的 RL、至多 5.4 倍 rollout 提速。Rollout-guided QAT aligns train-side FP4 rounding with outcomes; BF16-comparable RL with up to 5.4x rollout speedup. |
| [[2610.05745]] PIVOT-Q Vulnerability-Oriented Tuning | 方法 method | 漏洞导向在策略蒸馏只纠正高差异状态：7 种环境变化下恢复量化 VLA 泛化。Vulnerability-oriented on-policy distillation restores quantized VLA generalization across 7 environmental variations. |
| [[2610.07043]] TRIAGE NVFP4 Stabilization | 方法 method | 方向感知失配诊断区分放大/收缩梯度贡献：原生 NVFP4 W4A4 RL 稳定化。Direction-aware mismatch diagnosis stabilizes native NVFP4 W4A4 reinforcement learning while keeping 4-bit execution. |
| [[2610.09202]] Few Bits, One Law (W2A4KV2) | 方法 method | 联合 W2A4KV2：CanonQ 规范化+冻结高斯码本，PPL 最高降 14.28 倍。Joint W2A4KV2 quantization with canonicalization and frozen Gaussian codebooks; up to 14.28x lower PPL. |
| [[2610.06260]] CentriQ Calibration-Free Quantization | 方法 method | 先精确去均值再旋转：DiT 免校准 4-bit 量化匹敌 SVDQuant。Exact mean centering before rotation enables calibration-free 4-bit diffusion transformers, matching SVDQuant. |
| [[2610.13328]] DuoRate Per-Expert Precision | 方法 method | 按专家双速率精度分配：2.3 bpw 胜所有 2-bit 基线 6.3–47.0 分。Two-rate per-expert precision allocation beats every 2-bit baseline by 6.3–47.0 points at 2.3 bpw. |
| [[2610.09877]] Layerwise Error Attribution | 方法 method | 逐层概率误差归属使混合精度 PTQ 抗校准数据污染：PSNR +7.5 dB、提速 28–2,570 倍。Layerwise probabilistic error attribution makes mixed-precision PTQ robust to corrupted calibration data and 28–2,570x faster. |

### LLM 隐状态与可解释性 / LLM Hidden States & Interpretability（25 篇）

本周第二大方向，关键词是"方法论纠偏"：SAE 发现分数不识别干预、探针分数缺地板/天花板、视觉头发现不比随机好、模型生物需要多目标验证——以及一批扎实的机制定位（进位几何、拒绝通路、桥接头、工具调用向量）。
The second-largest area, keyword "methodological correction": SAE scores do not identify interventions, probe scores lack floor/ceiling references, discovered visual heads steer no better than random, model organisms need multi-objective validation — alongside solid mechanism localization (carry geometry, refusal pathway, bridge heads, tool-call vector).

| 论文 Paper | 类型 Type | 一句话点评 / One-line take |
|---|---|---|
| [[2610.07270]] Does the Model Use the Feature? | 分析 analysis | 安装/移除/下游救援契约：steering 特征不等于模型使用特征。Steering a feature does not show the model uses it; the installation/removal/rescue contract evaluated at natural-range values. |
| [[2610.15850]] What Do SAE Scores Identify? | 分析 analysis | 观测性 SAE 发现分数不识别干预归因：一次反向传播远胜探针系数（91–97% vs 17–35%）。Observational SAE discovery scores do not identify intervention attribution; one backward pass predicts realized ablations far better. |
| [[2610.08544]] How High Is 0.6? | 分析 analysis | 探针分数没有地板/天花板参照就没有固定含义：重审 4 个著名探针结论，多个可由输入文本解释。Probe scores lack fixed meaning without floor/ceiling references; four influential probing claims largely explained by input text. |
| [[2610.12842]] More Modular than Single Neurons | 分析 analysis | 嵌套模块化层级+因果消融：内容/风格、句法/语义在子空间层面解离。A nested modularity hierarchy with causal ablations shows subspaces dissociate even when neurons overlap. |
| [[2610.15218]] Fewer Loops Remove Refusal | 分析 analysis | 少跑循环即移除拒绝而有害性仍线性可解码（AUC 0.967）；随机深度训练恢复分离。Reduced loop counts remove refusal while harmfulness stays linearly decodable; random-depth training restores separation. |
| [[2610.08069]] Minimax Limits of Representation Repair | 分析 analysis | 检测表示偏移需 κ>>√d 而修复需 κ~d：检测远易于修复。Exact minimax limits show detecting a representation shift needs far weaker conditions than repairing it. |
| [[2610.09624]] The Tool-Call Vector | 分析 analysis | 因果必要充分的工具调用向量由"分析动词的抑制"塑造，7 模型族复现。A causally necessary and sufficient tool-call vector shaped by suppression of analysis verbs, replicated across 7 model families. |
| [[2610.06605]] Geometry of Latent Carry | 分析 analysis | 分隔符 token 的预测槽把进位编码为残差流环上的角度，激活修补可传递进位达 84%。The separator token's prediction slot encodes carry-in as an angle on a ring; patching transfers carry in up to 84% of cases. |
| [[2610.07469]] COMPASS Where Reasoning Lives | 方法 method | logit 空间归因找到携带正确性方向的头：GSM8K +16pp、省 20–70% token。Logit-space attribution finds heads carrying the correctness direction; +16pp GSM8K with 20–70% fewer tokens. |
| [[2610.13078]] Attention Sees, MLP Refuses | 分析 analysis | 注意力更新早期解码危害、MLP 更新写入拒绝：18 对模型上因果确认该安全通路。Attention updates decode harm early while MLP updates write refusal; causal resets confirm the pathway across 18 model pairs. |
| [[2610.06851]] Base Models Reason by Cue | 分析 analysis | 训练文档线索驱动基座推理：简单线索把 MATH-500 pass@1 从 42% 提到 78%。Causal interventions show training-data cues drive base-model reasoning; a simple cue lifts MATH-500 pass@1 from 42% to 78%. |
| [[2610.08200]] Heads for Network Information Retrieval | 分析 analysis | 因果消融筛选：1–9 个头达 99.5–100% held-out 精度，单神经元集中不可靠迁移。Causal ablation screening finds 1–9 heads giving 99.5–100% held-out accuracy; single-neuron concentration transfers unreliably. |
| [[2610.12445]] Telling FIBS Probes | 方法 method | 多层探针在最大欺骗数据集上 98.4%/98.0% AUROC，捕捉未言明的欺骗。Multi-layer probes reach 98.4%/98.0% AUROC on sabotage arenas, catching deception that text monitors miss. |
| [[2610.08718]] Mechanics of Spurious Forgetting | 分析 analysis | 联想记忆理论：虚假遗忘分为可逆共享漂移与缓慢侵蚀，减去单一方向即可恢复事实。Spurious forgetting splits into a reversible shared shift and slow erosion; subtracting one direction restores facts. |
| [[2610.10594]] Coverage Sets Probe Data Needs | 分析 analysis | 探针的合成数据需求由每类覆盖而非难度决定：每类中位 7–11 个同类样本。Probe data needs are set by per-kind coverage, not difficulty; a median of 7–11 own-kind samples per kind. |
| [[2610.07661]] Massive Activation Gating Channel | 分析 analysis | 单一 massive 激活门控通道位于 spike-FFN 输入嵌入，四族六模型验证。A single massive-activation gating channel in spike-FFN inputs, verified across six LLMs in four families. |
| [[2610.08559]] Bias Directions Capture Confidence | 分析 analysis | 去偏 steering 方向实由模型置信度主导：降偏见靠诱导弃答而非公平表征。Activation-steering debiasing directions encode confidence, not fairness; steering reduces bias by inducing abstention. |
| [[2610.13111]] Visual-Head Discovery Pitfalls | 分析 analysis | 层匹配随机对照下：被发现的视觉头集合并不比随机集合更可导向。With layer-matched random controls, discovered visual-head sets steer no better than random sets — a reporting-protocol pitfall. |
| [[2610.09733]] Bridge Routing Heads | 分析 analysis | 多语言多跳推理驻留在语言专属互斥的桥接头集合中：无训练挽救 51.7% 跨语言失败。Language-specific bridge routing heads carry multilingual multi-hop chains; amplification rescues 51.7% of cross-lingual failures without training. |
| [[2610.15836]] Latent Taxonomies in Pretraining | 分析 analysis | 合成分类树续训可从激活中聚类恢复；固定数据预算下归纳随规模减弱——记忆而非压缩。Continued pretraining on a synthetic taxonomy recovers the full tree from activations; induction weakens with scale at a fixed data budget. |
| [[2610.07646]] Matching Object or Relation? | 分析 analysis | VLM 抽象关系匹配失败源于两个竞争电路（早期表面物体、晚期抽象关系）。Two competing circuits (early surface-object, late abstract-relation) explain why VLMs fail relational matching. |
| [[2610.10203]] How to Train Your Model Organism | 方法 method | 单目标模型生物不可靠：三目标验证+多目标合并训练成为可靠测试床。Three-objective validation plus multi-objective merge training makes model organisms reliable interpretability testbeds. |
| [[2610.07389]] SAE as Natural Gradient Flow | 方法 method | 免编码器稀疏编码统一推理与字典学习为自然梯度流：改进稀有特征恢复。Encoder-free sparse coding unifies inference and dictionary learning as natural-gradient flow, improving rare-feature recovery. |
| [[2610.12410]] Predicting Alignment Generalization | 分析 analysis | 激活价值表征预测对齐泛化（相关性 0.45 vs 描述法 0.05）。Activation-based value representations predict alignment generalization far better than descriptions (0.45 vs 0.05). |
| [[2610.07334]] Weight Oracles | 方法 method | 语言模型直接读原始权重做诊断：后门检测 AUROC 0.93、手工检测器在威胁模型漂移下崩溃。LMs diagnose networks directly from raw weights; backdoor detection AUROC 0.93 where hand-crafted detectors collapse. |

### 大规模 ML 计算基础设施 / Compute Infrastructure for Large-Scale ML（10 篇）

从 fat-tree 负载均衡理论、Meta 自研 NIC 的车队级运维、生产 RDMA 部署，到 all-to-all 提速、TMA 卸载集合通信、万亿级 refit 与消费级 GPU 上的 MoE 推理——训练与服务的"地基"层本周异常扎实。
From fat-tree load-balancing theory and Meta's fleet-scale custom NIC to production RDMA, all-to-all speedups, TMA-offloaded collectives, trillion-parameter refit, and MoE inference on consumer GPUs — an unusually solid week for the infrastructure layer.

| 论文 Paper | 类型 Type | 一句话点评 / One-line take |
|---|---|---|
| [[2610.07230]] Ofan Optimal Load Balancing | 系统 system | 证明随机喷洒 Θ(√m) 队列下界，交换机侧按目的地轮转实现 Θ(1)：405B CCT 膨胀降 16–39 倍。Switch-based destination-aware load balancing achieves Θ(1) queues and cuts 405B CCT inflation 16–39x. |
| [[2610.07644]] From ASIC to Fleet (fbNIC) | 报告 report | Meta 自研多主机 NIC 全栈：十个月计划外不可用率降 12 倍、MTTR 降 37%。Meta's custom multi-host NIC cuts unplanned unavailability 12x over ten months via per-host isolation and hardware-in-the-loop CI. |
| [[2610.12815]] Deploying RDMA at Scale | 系统 system | ByteDance 生产 RDMA：推理参数拉取 P99 −43.7%、训练推送 P99 −74.0%（相对内核 TCP）。Production RDMA deployment cuts inference param-fetch P99 by 43.7% and training push P99 by 74.0% versus kernel TCP. |
| [[2610.09372]] Expert Coupling in MoE Pretraining | 方法 method | 相关专家放置+跨层 token 洗牌：all-to-all 提速 1.16–2.63 倍。Correlated expert placement + token shuffling exploit router co-selection, cutting all-to-all time 1.16–2.63x. |
| [[2610.07098]] T-CCL Tensor Memory Collectives | 系统 system | 集合通信卸载到 Tensor Memory Accelerator：超 NCCL 至多 2.4 倍。Offloading collectives to the Tensor Memory Accelerator outperforms NCCL by up to 2.4x with better overlap. |
| [[2610.07742]] Cleave Tensor Program Optimization | 系统 system | 符号解耦代数搜索+算子调度：内核快至 2.8 倍，生产 trace 上超 FlashInfer 1.4×/1.7×。Decoupled algebraic search and operator scheduling yield up to 2.8x faster kernels than the best baseline. |
| [[2610.08430]] NeMo-DCR Delta-Compressed Refit | 系统 system | 比特精确增量压缩 refit：1T 参数 150 秒同步、快 12–40 倍。Bit-exact delta-compressed refit syncs 1T-parameter weights in 150s, 12–40x faster for disaggregated agentic RL. |
| [[2610.05854]] TurboPairFormer | 方法 method | 三角注意力反向的键瓦片并行+FP32 残差补偿：最低梯度 RMSE 且确定、更快。An optimized triangle-attention backward gives the lowest gradient RMSE vs FP64 with determinism and speed for protein-folding training. |
| [[2610.11134]] QUILT Sparse-Attention Prefill | 系统 system | 共享查询执行：内核延迟至多 −55.1%、KV 数据 −55.9%、TTFT −36.8%。Shared query execution cuts sparse-attention prefill latency up to 55.1% and KV data 55.9% under parallelism. |
| [[2610.09424]] CoMoE on Commodity GPUs | 系统 system | 仅 PCIe 消费级 GPU 的 MoE 推理：RTX 5090 吞吐 1.46 倍、A800 的 23.4% 成本。Host-centric routing democratizes MoE inference on PCIe-only consumer GPUs at 23.4% of A800 hardware cost. |

### 模型系统卡与技术报告 / Model System Cards & Technical Reports（2 篇）

本周只有 2 篇模型卡/技术报告通过门槛：一篇把 RL 当主训练范式规模化（小米），一篇把全开放文本模型原地升级为多模态推理器（瑞士 Apertus）。两份报告的诚实度都高于品类平均——前者披露 $2.6M RL 花费与 router 冻结诊断，后者公开训练事故复盘与"70B 只训了一半"的取舍。
Only 2 model-card/technical-report papers passed the gate this week: one scales RL as the main training paradigm (Xiaomi), the other upgrades fully open text models into multimodal reasoners in place (Swiss Apertus). Both are more candid than the category average.

| 论文 Paper | 类型 Type | 一句话点评 / One-line take |
|---|---|---|
| [[2610.11959]] MiMo-V2.6 Technical Report | 报告 report | RL 当主范式规模化（单次 $2.6M、每步 2.7–3.7B token）：router 冻结诊断负载坍塌，开源 9B 蒸馏+约 7k 环境。Xiaomi scales RL as the main training paradigm; a clean router-freeze ablation, disclosed $2.6M spend, and an open 9B distill + 7k environments. |
| [[2610.15542]] Apertus 1.5 Technical Report | 报告 report | 离散 tokenizer 原地升级 8B/70B 为多模态推理器、262K 上下文、thinking 是模板开关，全链路 Apache 2.0。Fully open multimodal reasoners via in-place tokenizer upgrade; thinking as a template flag, weights/data/code all Apache 2.0. |

## All Papers

> 全部 102 篇入选论文的完整索引（按方向与 area_rank 排序）。完整点评见上方"按主题分类"。/ Complete index of all 102 selected papers (by area, area_rank order). See the topic tables above for the one-line takes.

| # | 论文 Paper | 领域 Area | 类型 Type |
|---|---|---|---|
| 1 | [[2610.09239]] Winner's Curse in Self-Improvement Loops | 自进化智能体 Self-Evolving Agents | 分析 analysis |
| 2 | [[2610.09769]] Bolzano Open-Problem Solving | 自进化智能体 Self-Evolving Agents | 系统 system |
| 3 | [[2610.14683]] Triage-PiEvo Evidence Admission | 自进化智能体 Self-Evolving Agents | 系统 system |
| 4 | [[2610.14163]] AutoEnvScaling Data Flywheel | 自进化智能体 Self-Evolving Agents | 方法 method |
| 5 | [[2610.09197]] FreeEvolve Beyond Fixed Loops | 自进化智能体 Self-Evolving Agents | 方法 method |
| 6 | [[2610.13025]] Evo² Weight-Harness Co-Evolution | 自进化智能体 Self-Evolving Agents | 方法 method |
| 7 | [[2610.11655]] Harness Evolution Ceiling | 自进化智能体 Self-Evolving Agents | 方法 method |
| 8 | [[2610.07447]] Fork-and-Flush Idea Basins | 自进化智能体 Self-Evolving Agents | 方法 method |
| 9 | [[2610.11794]] Memento 3 Reflective Rulebooks | 自进化智能体 Self-Evolving Agents | 系统 system |
| 10 | [[2610.13494]] Humanize MLE Agents | 自进化智能体 Self-Evolving Agents | 方法 method |
| 11 | [[2610.12235]] LMs as Research World Models | 自进化智能体 Self-Evolving Agents | 方法 method |
| 12 | [[2610.07625]] Stateless Language Agents | 自进化智能体 Self-Evolving Agents | 系统 system |
| 13 | [[2610.13524]] Simulating Training Spikes | 训练稳定性 Training Stability | 分析 analysis |
| 14 | [[2610.09647]] When Rank Rises as LLMs Degrade | 训练稳定性 Training Stability | 分析 analysis |
| 15 | [[2610.14394]] Recommender Instability Cascade | 训练稳定性 Training Stability | 方法 method |
| 16 | [[2610.11317]] DivMoE Upcycling | 训练稳定性 Training Stability | 方法 method |
| 17 | [[2610.05744]] CIPHER-MoE Trillion-Scale Routing | 训练稳定性 Training Stability | 方法 method |
| 18 | [[2610.09835]] Forgetting in Output Embeddings | 训练稳定性 Training Stability | 方法 method |
| 19 | [[2610.07207]] DRMoET Robust MoE Training | 训练稳定性 Training Stability | 方法 method |
| 20 | [[2610.11575]] Smoothing Top-k Exposure Boundary | 训练稳定性 Training Stability | 方法 method |
| 21 | [[2610.06677]] Sparse Probability Maps in Routing | 训练稳定性 Training Stability | 分析 analysis |
| 22 | [[2610.13370]] Expert Selection Biases | 训练稳定性 Training Stability | 方法 method |
| 23 | [[2610.12822]] Reward Hacking as Transmissible Strategy | RL 后训练 RL Post-Training | 分析 analysis |
| 24 | [[2610.09597]] COPC Off-Policy Correction | RL 后训练 RL Post-Training | 方法 method |
| 25 | [[2610.06439]] Better Call Reward | RL 后训练 RL Post-Training | 分析 analysis |
| 26 | [[2610.14440]] TETPO Variance Control | RL 后训练 RL Post-Training | 方法 method |
| 27 | [[2610.13594]] MENTOR Learning from Failure | RL 后训练 RL Post-Training | 方法 method |
| 28 | [[2610.15778]] Who Sets the Pace of Judge Hacking | RL 后训练 RL Post-Training | 分析 analysis |
| 29 | [[2610.11291]] When Do We Need On-Policy Distillation | RL 后训练 RL Post-Training | 分析 analysis |
| 30 | [[2610.14270]] Thinking Leakage in RL | RL 后训练 RL Post-Training | 分析 analysis |
| 31 | [[2610.09111]] Same Text, Different Prediction | 推理可靠性 Inference Reliability & SDC | 分析 analysis |
| 32 | [[2610.15808]] Framework Testing in Data Flow | 推理可靠性 Inference Reliability & SDC | 方法 method |
| 33 | [[2610.07529]] Targeted Search for Worst-Case Error | 推理可靠性 Inference Reliability & SDC | 分析 analysis |
| 34 | [[2610.10311]] Fault-Tolerant Foundation Models | 推理可靠性 Inference Reliability & SDC | 方法 method |
| 35 | [[2610.09255]] The Symbol of the Surrogate | 推理可靠性 Inference Reliability & SDC | 分析 analysis |
| 36 | [[2610.05833]] Request Order Matters | 推理可靠性 Inference Reliability & SDC | 分析 analysis |
| 37 | [[2610.09999]] ReSAFT Fault Tolerance | 推理可靠性 Inference Reliability & SDC | 方法 method |
| 38 | [[2610.15509]] CacheLink KV Transport | 推理可靠性 Inference Reliability & SDC | 方法 method |
| 39 | [[2610.11358]] RaReCache Cross-Model Reuse | 推理可靠性 Inference Reliability & SDC | 系统 system |
| 40 | [[2610.13060]] KV-Repurpose Testbed | 推理可靠性 Inference Reliability & SDC | 系统 system |
| 41 | [[2610.15459]] When Messages Go Wrong | 静默失败 Silent Failures | 分析 analysis |
| 42 | [[2610.11647]] One Skill Too Many | 静默失败 Silent Failures | 分析 analysis |
| 43 | [[2610.06163]] Localizing Silent Repair Failures | 静默失败 Silent Failures | 方法 method |
| 44 | [[2610.10062]] Loud Failures, Quiet Failures | 静默失败 Silent Failures | 分析 analysis |
| 45 | [[2610.14115]] Silent Failures in Agentic Data Science | 静默失败 Silent Failures | 分析 analysis |
| 46 | [[2610.05683]] RESOLVE GPU Kernel Validation | 极致优化可靠性 Extreme-Performance Reliability | 方法 method |
| 47 | [[2610.07853]] Lost in the bf16 Cast | 极致优化可靠性 Extreme-Performance Reliability | 分析 analysis |
| 48 | [[2610.08917]] CARE Certified Acceleration | 极致优化可靠性 Extreme-Performance Reliability | 方法 method |
| 49 | [[2610.15139]] When Dynamic Scaling Fails | 极致优化可靠性 Extreme-Performance Reliability | 分析 analysis |
| 50 | [[2610.06251]] Shared Stopping Decisions Change Answers | 极致优化可靠性 Extreme-Performance Reliability | 分析 analysis |
| 51 | [[2610.14277]] Echo Error-Compensated All-Reduce | 极致优化可靠性 Extreme-Performance Reliability | 方法 method |
| 52 | [[2610.08164]] Align, Then Correct | 极致优化可靠性 Extreme-Performance Reliability | 方法 method |
| 53 | [[2610.12444]] Rounding in Preconditioner Space | 极致优化可靠性 Extreme-Performance Reliability | 方法 method |
| 54 | [[2610.15709]] Preserving Updates in State Quantization | 极致优化可靠性 Extreme-Performance Reliability | 方法 method |
| 55 | [[2610.09212]] CurveTQ Trellis Quantization | 极致优化可靠性 Extreme-Performance Reliability | 方法 method |
| 56 | [[2610.15675]] Quantization-Conditioned RL for VLAs | 极致优化可靠性 Extreme-Performance Reliability | 方法 method |
| 57 | [[2610.14448]] KV4-RL INT4 Rollouts | 极致优化可靠性 Extreme-Performance Reliability | 方法 method |
| 58 | [[2610.15259]] RECAP Dynamic-Prefix Calibration | 极致优化可靠性 Extreme-Performance Reliability | 方法 method |
| 59 | [[2610.07767]] TRACE FP4 RL QAT | 极致优化可靠性 Extreme-Performance Reliability | 方法 method |
| 60 | [[2610.05745]] PIVOT-Q Vulnerability-Oriented Tuning | 极致优化可靠性 Extreme-Performance Reliability | 方法 method |
| 61 | [[2610.07043]] TRIAGE NVFP4 Stabilization | 极致优化可靠性 Extreme-Performance Reliability | 方法 method |
| 62 | [[2610.09202]] Few Bits, One Law (W2A4KV2) | 极致优化可靠性 Extreme-Performance Reliability | 方法 method |
| 63 | [[2610.06260]] CentriQ Calibration-Free Quantization | 极致优化可靠性 Extreme-Performance Reliability | 方法 method |
| 64 | [[2610.13328]] DuoRate Per-Expert Precision | 极致优化可靠性 Extreme-Performance Reliability | 方法 method |
| 65 | [[2610.09877]] Layerwise Error Attribution | 极致优化可靠性 Extreme-Performance Reliability | 方法 method |
| 66 | [[2610.07270]] Does the Model Use the Feature? | 可解释性 Interpretability | 分析 analysis |
| 67 | [[2610.15850]] What Do SAE Scores Identify? | 可解释性 Interpretability | 分析 analysis |
| 68 | [[2610.08544]] How High Is 0.6? | 可解释性 Interpretability | 分析 analysis |
| 69 | [[2610.12842]] More Modular than Single Neurons | 可解释性 Interpretability | 分析 analysis |
| 70 | [[2610.15218]] Fewer Loops Remove Refusal | 可解释性 Interpretability | 分析 analysis |
| 71 | [[2610.08069]] Minimax Limits of Representation Repair | 可解释性 Interpretability | 分析 analysis |
| 72 | [[2610.09624]] The Tool-Call Vector | 可解释性 Interpretability | 分析 analysis |
| 73 | [[2610.06605]] Geometry of Latent Carry | 可解释性 Interpretability | 分析 analysis |
| 74 | [[2610.07469]] COMPASS Where Reasoning Lives | 可解释性 Interpretability | 方法 method |
| 75 | [[2610.13078]] Attention Sees, MLP Refuses | 可解释性 Interpretability | 分析 analysis |
| 76 | [[2610.06851]] Base Models Reason by Cue | 可解释性 Interpretability | 分析 analysis |
| 77 | [[2610.08200]] Heads for Network Information Retrieval | 可解释性 Interpretability | 分析 analysis |
| 78 | [[2610.12445]] Telling FIBS Probes | 可解释性 Interpretability | 方法 method |
| 79 | [[2610.08718]] Mechanics of Spurious Forgetting | 可解释性 Interpretability | 分析 analysis |
| 80 | [[2610.10594]] Coverage Sets Probe Data Needs | 可解释性 Interpretability | 分析 analysis |
| 81 | [[2610.07661]] Massive Activation Gating Channel | 可解释性 Interpretability | 分析 analysis |
| 82 | [[2610.08559]] Bias Directions Capture Confidence | 可解释性 Interpretability | 分析 analysis |
| 83 | [[2610.13111]] Visual-Head Discovery Pitfalls | 可解释性 Interpretability | 分析 analysis |
| 84 | [[2610.09733]] Bridge Routing Heads | 可解释性 Interpretability | 分析 analysis |
| 85 | [[2610.15836]] Latent Taxonomies in Pretraining | 可解释性 Interpretability | 分析 analysis |
| 86 | [[2610.07646]] Matching Object or Relation? | 可解释性 Interpretability | 分析 analysis |
| 87 | [[2610.10203]] How to Train Your Model Organism | 可解释性 Interpretability | 方法 method |
| 88 | [[2610.07389]] SAE as Natural Gradient Flow | 可解释性 Interpretability | 方法 method |
| 89 | [[2610.12410]] Predicting Alignment Generalization | 可解释性 Interpretability | 分析 analysis |
| 90 | [[2610.07334]] Weight Oracles | 可解释性 Interpretability | 方法 method |
| 91 | [[2610.07230]] Ofan Optimal Load Balancing | 计算基础设施 Compute Infrastructure | 系统 system |
| 92 | [[2610.07644]] From ASIC to Fleet (fbNIC) | 计算基础设施 Compute Infrastructure | 报告 report |
| 93 | [[2610.12815]] Deploying RDMA at Scale | 计算基础设施 Compute Infrastructure | 系统 system |
| 94 | [[2610.09372]] Expert Coupling in MoE Pretraining | 计算基础设施 Compute Infrastructure | 方法 method |
| 95 | [[2610.07098]] T-CCL Tensor Memory Collectives | 计算基础设施 Compute Infrastructure | 系统 system |
| 96 | [[2610.07742]] Cleave Tensor Program Optimization | 计算基础设施 Compute Infrastructure | 系统 system |
| 97 | [[2610.08430]] NeMo-DCR Delta-Compressed Refit | 计算基础设施 Compute Infrastructure | 系统 system |
| 98 | [[2610.05854]] TurboPairFormer | 计算基础设施 Compute Infrastructure | 方法 method |
| 99 | [[2610.11134]] QUILT Sparse-Attention Prefill | 计算基础设施 Compute Infrastructure | 系统 system |
| 100 | [[2610.09424]] CoMoE on Commodity GPUs | 计算基础设施 Compute Infrastructure | 系统 system |
| 101 | [[2610.11959]] MiMo-V2.6 Technical Report | 模型卡与技术报告 Model System Cards | 报告 report |
| 102 | [[2610.15542]] Apertus 1.5 Technical Report | 模型卡与技术报告 Model System Cards | 报告 report |

---

*数量核对 Count check: 本文件 All Papers 索引与按主题分类表各含 102 篇论文，与 `filtered_papers.json` 的 `total_selected = 102` 一致（3862 篇评估 → 102 篇入选）。本周无方向少于 2 篇；模型卡方向仅 2 篇通过门槛。必读 8 篇全部来自 stars.json 的 `star: true` 候选（无自行增补）。*
*The All Papers index and the topic tables each list 102 papers, matching `total_selected = 102` in `filtered_papers.json` (3,862 evaluated → 102 selected). No area has fewer than 2 papers this week; the model-cards area is thin with exactly 2. All 8 must-reads come from `star: true` entries in stars.json, with no re-starering.*
