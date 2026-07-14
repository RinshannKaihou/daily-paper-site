---
title: "Daily Arxiv Digest — 2026-07-08"
date: 2026-07-08
tags:
  - self-evolving-agents
  - mechanistic-interpretability
  - llm-training
  - rlhf
  - reliability
  - ai-safety
  - evaluation
  - scientific-ml
papers: 31
---

# Daily Arxiv Digest — 2026-07-08

共筛选 231 篇，入选 31 篇（评分 4–5）。 / Of 231 papers screened, 31 were selected (relevance score 4–5).

---

## 今日必读 / Must Read Today

### 1. [[2607.07663]] Recursive Self-Improvement Survey（递归自改进综述）

**为什么必读 / Why read it:** 这是迄今为止最系统的递归自改进（RSI）综述，梳理了 1250+ 篇文献并建立了一个验证层级分类法（形式化验证 → 测试 → 启发式 → 无验证），明确指出现有"自改进"工作大多缺乏可验证的进步闭环。对任何研究自演化 Agent、auto-research loop、self-improvement 的人都提供了地图与术语基准。 / The most systematic RSI survey to date, organizing 1250+ works into a verification-hierarchy taxonomy (formal proof → test → heuristic → none) and bluntly flagging that most "self-improvement" claims lack a verifiable improvement loop. Required map-and-vocabulary reading for anyone working on self-evolving agents or auto-research loops.

### 2. [[2607.07436]] The Blind Curator（有偏裁判杀死技能退役）

**为什么必读 / Why read it:** 本文给出了一个清晰的解析结果——当判别器自身存在偏置时，技能退役阈值被钉死在 ρ_F→P = (1−τ)/2，意味着"用有偏裁判来决定保留哪些技能"在结构上会扼杀自改进。这对所有依赖 LLM-as-judge 的自演化系统都是一个警钟：先修裁判，再谈改进。 / A clean analytical result showing that a biased judge pins the skill-retirement threshold at ρ_F→P = (1−τ)/2 — structurally, judging skill retention with a biased evaluator kills self-improvement. A wake-up call for every self-evolving pipeline that leans on LLM-as-judge: fix the judge before claiming improvement.

### 3. [[2607.07321]] EVOSOP（迭代工具优化，ACEBench +24pp）

**为什么必读 / Why read it:** EVOSOP 把"工具"本身作为可优化的artifact，让 Agent 在 ACEBench 上以单rollout方式迭代改写工具描述/签名，取得 +24pp 的显著提升。它示范了"如何让 Agent 修改自己的工具栈"这一自演化范式的落地形态，与 RSI 综述形成方法—理论的对偶。 / EVOSOP makes the tool itself the optimizable artifact: a single-rollout iterative loop rewrites tool descriptions/signatures and gains +24pp on ACEBench. A concrete demonstration of "agents that edit their own toolkit," directly complementing the RSI survey's theory with a working mechanism.

---

## 按主题分类 / Papers by Topic

### 自演化 Agent 与技能 / 工具学习 — Self-Evolving Agents & Skill/Tool Learning

| 论文 / Paper | 一句话总结 / One-line summary |
|---|---|
| [[2607.07663]] RSI Survey | 1250+ 篇 RSI 文献的系统综述，按验证强度分级；指出多数"自改进"缺乏可验证闭环。 / Survey of 1250+ RSI works graded by verification rigor; most "self-improvement" lacks a verifiable loop. |
| [[2607.07321]] EVOSOP | 以单rollout迭代优化工具描述/签名，ACEBench +24pp。 / Single-rollout iterative tool optimization, +24pp on ACEBench. |
| [[2607.07676]] SkillCenter | 216,938 个技能的大规模基准，发现关键词检索≈安慰剂效应。 / 216,938-skill benchmark; keyword retrieval is near-placebo. |
| [[2607.07504]] Skills Ablation | 10,584 次实验的零结果：LLM 技能使用 ≈ 无技能基线。 / Null result over 10,584 runs: LLM skill use ≈ no-skill baseline. |
| [[2607.07052]] Progressive Crystallization | 生产中把 Agent 探索固化为确定性工作流，8 个月成本降 70%+。 / Crystallize agent exploration into deterministic workflows, >70% cost drop in 8 months. |
| [[2607.06974]] MILES | 冻结 LLM + 模块化记忆 + 可学习选择头，测试时自改进。 / Frozen LLM + modular memory + learnable selection heads for test-time self-improvement. |

### 机制可解释性 — Mechanistic Interpretability

| 论文 / Paper | 一句话总结 / One-line summary |
|---|---|
| [[2607.07316]] MI Survey | PRISMA-ScR 综述，覆盖 circuits/SAE/steering/神经符号四条主线。 / PRISMA-ScR review spanning circuits, SAE, steering, neurosymbolic. |
| [[2607.07066]] Stratified Fourier Mechanisms | 用 Monoid Extension 解释 Z_165 乘法回路。 / Monoid Extension explains Z_165 multiplication circuits. |
| [[2607.07003]] Dissociating Sycophancy | Gemma 用统一表征、Llama 用分离表征实现谄媚。 / Gemma uses unified, Llama distinct representations for sycophancy. |
| [[2607.07128]] DSI | 仅 8–64 个神经元即可激活特定任务。 / 8–64 neurons suffice to activate a given task. |
| [[2607.07670]] Bielik Activation Dispersion | 熟悉度 vs 可靠度可分离，AUROC 0.95–1.00。 / Familiarity vs reliability dissociable, AUROC 0.95–1.00. |
| [[2607.07626]] Future Confidence Distillation | FOK/JOL 时序置信度，66.1% gap recovery。 / Temporal FOK/JOL confidence, 66.1% gap recovery. |
| [[2607.07264]] LAD | 语言锚定的分解，得到既命名又忠实的概念。 / Language-anchored decomposition yielding named + faithful concepts. |
| [[2607.07035]] Deep ReLU Principles | 深层 ReLU 单元形成分段线性流形而非超平面。 / Deep ReLU units form piecewise-linear manifolds, not hyperplanes. |
| [[2607.07047]] Riemannian Mean Pooling | SPD 流形 Fréchet 均值聚合，CREAK AUC +0.060。 / SPD-manifold Fréchet aggregation, +0.060 AUC on CREAK. |

### LLM 训练与强化学习 — LLM Training & RL

| 论文 / Paper | 一句话总结 / One-line summary |
|---|---|
| [[2607.07494]] GIFT | K-FAC 白化 + FP8 梯度通信，训练加速 7.6%。 / K-FAC whitening + FP8 gradient comm, 7.6% speedup. |
| [[2607.07508]] SAO | 单rollout异步 RL，AIME2025 97.3 vs GRPO 84.2。 / Single-rollout async RL, AIME2025 97.3 vs 84.2 GRPO. |
| [[2607.06987]] UP | 不对称优化：正优势无界、负优势裁剪，Pass@1 平均 +1.16%。 / Asymmetric objective: unbounded positive, clipped negative, avg +1.16% Pass@1. |

### 可靠性、安全与审计 — Reliability, Safety & Auditing

| 论文 / Paper | 一句话总结 / One-line summary |
|---|---|
| [[2607.07436]] Blind Curator | 有偏裁判把技能退役阈值钉在 (1−τ)/2，杀死自改进。 / Biased judge pins retirement threshold at (1−τ)/2, killing self-improvement. |
| [[2607.07405]] Deterministic Gates | 静默策略违规检测，τ²-bench +12.4pp。 / Silent policy-violation detection, +12.4pp on τ²-bench. |
| [[2607.07395]] ARG-TCA | 图属性推理做 VLM 校准，ECE −48%。 / Graph-attribute reasoning for VLM calibration, −48% ECE. |
| [[2607.07538]] Langevin Dynamics | 给出不安全集合界，随维度 d 指数衰减。 / Unsafe-set bounds decaying exponentially in dimension d. |
| [[2607.07229]] Reasoning Consistency Scanning | CoT 一致性审计，不一致率 0–26%。 / CoT consistency auditing, 0–26% inconsistency. |
| [[2607.07184]] Deployment Simulation | OpenAI 用部署模拟预测发布前安全，方向准确率 92%。 / OpenAI simulates deployment to predict safety, 92% directional accuracy. |
| [[2607.06871]] Geometric Collapse | 深度模型无法验证物理因果，崩溃比达 3.2×。 / Depth models fail to verify physical causality, collapse ratio 3.2×. |
| [[2607.06893]] Stochastic Oracles | LLM 作预言的 token 复杂度上界（TV/Chernoff/KL）。 / Token-complexity ceilings for LLM-as-oracle (TV/Chernoff/KL). |

### 科学与领域机器学习 — Scientific & Domain ML

| 论文 / Paper | 一句话总结 / One-line summary |
|---|---|
| [[2607.07467]] SpaCellAgent | LLM 多智能体做空间转录组轨迹推断，时间 −41.2%。 / LLM multi-agent for spatial transcriptomics trajectory inference, −41.2% time. |
| [[2607.07379]] PA-SciML | 物理审计的 Agent 式科学发现，检测因果违例。 / Physics-audited agentic discovery, detects causality violations. |
| [[2607.06924]] Doob-Barrier Consolidation | 模拟噪声经 Doob h-变换转为持续学习资源，+10.9pp。 / Analog noise turned into a continual-learning resource via Doob h-transform, +10.9pp. |

### 评测方法论 — Evaluation Methodology

| 论文 / Paper | 一句话总结 / One-line summary |
|---|---|
| [[2607.06940]] MFSS | 六维加权打分系统，TruthfulQA 上 Gemini-2.0-flash 居首（0.6104）。 / Six-factor weighted scoring; Gemini-2.0-flash tops TruthfulQA (0.6104). |
| [[2607.07040]] SepaRank | 模型出题+群体作答+方差打分，排序与人直觉一致。 / Models author items, panel answers, variance scores; ordering matches intuition. |

---

## All Papers

| arXiv ID | 标题 / Title | 主题 / Topic | 评分 / Score |
|---|---|---|---|
| [[2607.07663]] | Recursive Self-Improvement Survey / 递归自改进综述 | Self-Evolving Agents | 5 |
| [[2607.07436]] | The Blind Curator / 有偏裁判杀死技能退役 | Reliability/Safety | 5 |
| [[2607.07321]] | EVOSOP / 迭代工具优化 | Self-Evolving Agents | 5 |
| [[2607.07316]] | MI Survey / 机制可解释性综述 | Mech. Interpretability | 5 |
| [[2607.07066]] | Stratified Fourier Mechanisms / 分层傅里叶机制 | Mech. Interpretability | 5 |
| [[2607.07003]] | Dissociating Sycophancy / 分离谄媚 | Mech. Interpretability | 5 |
| [[2607.07494]] | GIFT / FP8 梯度通信 | LLM Training | 4 |
| [[2607.07467]] | SpaCellAgent / 空间转录组 Agent | Scientific ML | 4 |
| [[2607.07128]] | DSI / 分布式稀疏干预 | Mech. Interpretability | 4 |
| [[2607.07676]] | SkillCenter / 技能中心 | Self-Evolving Agents | 4 |
| [[2607.07670]] | Bielik Activation Dispersion / 激活分散度 | Mech. Interpretability | 4 |
| [[2607.07626]] | Future Confidence Distillation / 未来置信度蒸馏 | Mech. Interpretability | 4 |
| [[2607.07538]] | Langevin Dynamics / 朗之万动力学安全界 | Reliability/Safety | 4 |
| [[2607.07508]] | SAO / 单rollout异步 RL | LLM Training | 4 |
| [[2607.07504]] | Skills Ablation / 技能消融零结果 | Self-Evolving Agents | 4 |
| [[2607.07405]] | Deterministic Gates / 确定性门 | Reliability/Safety | 4 |
| [[2607.07395]] | ARG-TCA / 图属性推理校准 | Reliability/Safety | 4 |
| [[2607.07379]] | PA-SciML / 物理审计科学发现 | Scientific ML | 4 |
| [[2607.07264]] | LAD / 语言锚定分解 | Mech. Interpretability | 4 |
| [[2607.07229]] | Reasoning Consistency Scanning / 推理一致性扫描 | Reliability/Safety | 4 |
| [[2607.07184]] | Deployment Simulation / 部署模拟 | Reliability/Safety | 4 |
| [[2607.07052]] | Progressive Crystallization / 渐进式结晶 | Self-Evolving Agents | 4 |
| [[2607.07047]] | Riemannian Mean Pooling / 黎曼均值池化 | Mech. Interpretability | 4 |
| [[2607.07040]] | Measuring Intelligence Beyond Human Scale / SepaRank | Evaluation | 4 |
| [[2607.07035]] | Principles of Deep Feedforward ReLU Networks / 深 ReLU 网络原理 | Mech. Interpretability | 4 |
| [[2607.06987]] | UP / 不对称优化 | LLM Training | 4 |
| [[2607.06974]] | MILES / 模块化指令记忆 | Self-Evolving Agents | 4 |
| [[2607.06940]] | MFSS / 多因子打分系统 | Evaluation | 4 |
| [[2607.06924]] | Intrinsic-Noise Consolidation / 噪声巩固 | Scientific ML | 4 |
| [[2607.06893]] | Stochastic Oracles / 随机预言 | Reliability/Safety | 4 |
| [[2607.06871]] | Geometric Collapse / 几何崩溃 | Reliability/Safety | 4 |

---

## 计数核验 / Count Verification

- 概览中列出的论文数 / Papers listed in this overview: **31**
- 目录中实际 `.md` 文件数（不含 `overview.md`）/ Actual `.md` files in directory (excluding `overview.md`): **31**
- 状态 / Status: **匹配 / Matched ✓**
