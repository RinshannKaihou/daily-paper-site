---
title: "Daily arXiv Digest — 2026-07-14"
date: 2026-07-14
tags:
  - llm-agents
  - evaluation
  - mechanistic-interpretability
  - confidence-calibration
  - training-dynamics
  - quantization
  - benchmarks
  - llm-as-judge
papers: 39
---

# Daily arXiv Digest — 2026-07-14

今日共 **39** 篇论文，横跨智能体评测、机制可解释性、训练动力学理论、量化效率、置信度与安全、以及多类应用方向。整体基调是"对评测与训练经验法则的反思"——多篇工作（harness 演化、冷却调度、长度归一化、聚合鲁棒性）证伪或重新框定了社区默认接受的结论。The day leans heavily into **re-examining accepted evaluation and training heuristics**: several papers (harness evolution, LR cooldown, length normalization, aggregate robustness) falsify or reframe defaults the community has taken for granted.

---

## 今日必读 / Must Read Today

### 1. [[2607.12279]] A Shared Subcircuit Lets LLMs Count Down Across Tasks

**推荐理由 / Why read:** 通过因果干预在 Llama-3.1-70B 中定位出三个"倒计时注意力头"，并证明同一子回路在推文、SHA-256、俳句、DNA 等大量任务中被复用，其几何与 Claude 3.5 Haiku 的换行回路一致——为"跨任务甚至跨模型的共享机制"提供了干净实证。Using activation patching the authors isolate three "countdown" attention heads in Llama-3.1-70B and show the same subcircuit is reused across tweets, SHA-256 hashes, haikus and DNA, with key/query geometry matching Claude 3.5 Haiku's line-wrapping circuit — concrete evidence for motifs shared across both tasks and models. (Yale + Anthropic)

### 2. [[2607.12266]] Saturation Makes Quantization Error Additive: A Coverage Model with a Certificate

**推荐理由 / Why read:** 把混合精度量化的损失形式化为布尔立方体上的集合函数，证明 4-bit 下 85–99% 方差来自一阶项（根源是"饱和"），并据此给出闭式误差下限；在匹配内存下比 NVIDIA ModelOpt 基线低 17–21% KL 散度，子 4-bit 区间决定模型能否存活。Reframes mixed-precision quantization loss as a set function and proves 85–99% of variance is first-order at W4A4 (root cause: saturation), giving a closed-form error certificate; beats the production NVIDIA ModelOpt baseline by 17–21% KL at matched memory and decides model survival below 4 bits. (Waterloo / Baseten)

### 3. [[2607.12227]] Rethinking the Evaluation of Harness Evolution for Agents

**推荐理由 / Why read:** 在统一反馈与推理预算下，harness 演化既未稳定超越并行采样等简单基线（pass@1 75.8 vs 并行采样 86.0），演化出的 harness 也几乎不泛化到 held-out 任务（平均仅 +0.6 分），提示当前收益主要来自额外搜索而非真正的 harness 设计——直接挑战了一个热门方向。Under matched feedback and inference budgets, harness evolution neither consistently beats simple baselines (pass@1 75.8 vs parallel sampling 86.0) nor generalizes to held-out tasks (avg +0.6 points), showing reported gains stem from extra test-time search rather than genuine harness design — a sharp challenge to a fashionable subfield. (AI2 + UW)

---

## 按主题分类 / Papers by Topic

### A. 智能体、记忆与失败归因 / Agents, Memory & Failure Attribution

| Paper | 描述 (中 / EN) |
|---|---|
| [[2607.12254]] Recursively Self-Improving Agents | 提出受治理的多智能体架构（目标/范围/工具/基准契约）以实现递归自我改进，并定义"个人奇点"为有界目标；纯立场论文，无实验。 / A governed multi-agent architecture (goal/scope/tool/benchmark contracts) for recursive self-improvement, with "personal singularity" as a bounded objective; position paper, no experiments. |
| [[2607.12625]] KnowAct-GUIClaw | "Know-Route-Act-Reflect" 闭环 + 类型化黑板 + 自演化技能库，在 MobileWorld 上以开源 Kimi-K2.6 取得 64.1% SOTA，超 GPT-5.5。 / Know-Route-Act-Reflect loop with typed blackboard and self-evolving skills reaches 64.1% SOTA on MobileWorld with open-source Kimi-K2.6, beating GPT-5.5. |
| [[2607.12747]] Oat — Unsupervised Failure Attribution | 仅用约 100 条成功轨迹训练 Neural CDE，对失败轨迹做步骤级异常定位，F1 超 GPT-4o/5 提示法 +20%，推理快 200–5000×、零 token 成本。 / Trains a Neural CDE on ~100 successful trajectories only, flags per-step errors in failed runs; F1 beats GPT-4o/5 prompting by +20%, 200–5000× faster with zero token cost. |
| [[2607.12790]] Double Ratchet | 把评估指标当作可演化对象（原子缺陷检测器组合 + 锚定 + 共识），与技能环路协同，恢复 88–110% 的 oracle 提升，并捕获一个真实 Goodhart 投机失败。 / Co-evolves an evaluation metric (compositions of atomic drawback detectors, anchored + consensus-regularized) with a skill loop, recovering 88–110% of oracle lift and catching a real Goodhart gaming failure. |
| [[2607.12893]] MemOps — Lifecycle Memory Benchmark | 把长期对话记忆重定义为生命周期操作（记忆/遗忘/更新/反思/轨迹），最强模型在长上下文重建有序状态轨迹时仍严重退化，session 级检索远胜 turn 级。 / Reformulates long-conversation memory as lifecycle operations; even top models degrade sharply at reconstructing ordered state trajectories under long context, and session-level RAG beats turn-level by ~23 pts. |
| [[2607.12640]] GRPO Failure in Small Web Agent | 在 4B/8B Qwen3-VL 上严格证明：对已掌握任务 GRPO 无可信提升，中高学习率反而损害能力；该零结果源于任务缺乏 headroom，并给出权重嫁接的因果机制。 / Rigorously shows GRPO adds no credible skill on mastered tasks (4B/8B Qwen3-VL) and mid/high LRs degrade it; the null is a headroom property, with a weight-grafting causal mechanism. |

### B. 智能体基准与评测 / Agent Benchmarks & Evaluation

| Paper | 描述 (中 / EN) |
|---|---|
| [[2607.12227]] Rethinking Harness Evolution | 统一预算 + disjoint 评估证伪 harness 演化优势，held-out 仅 +0.6 分，增益主要来自额外搜索。 / Unified-budget + disjoint-split evaluation falsifies harness evolution's advantage (held-out +0.6 pts); gains are mostly extra search. |
| [[2607.12338]] How Many Tasks Are Enough | 重放 SWE-bench/AppWorld/tau-bench，定义"最小充分任务预算"，发现其随基准剧烈变化（AppWorld 15% vs SWE-bench Lite 95% 仍未达标），任务比例不是决策规则。 / Replays public agent benchmarks and defines a minimum sufficient task budget that varies sharply (AppWorld 15% vs SWE-bench Lite failing by 95%); task fraction is not a decision rule. |
| [[2607.12385]] PM-Bench — Prospective Memory | 受认知科学"Virtual Week"启发，评测智能体"前瞻记忆"；最佳方法（GPT-5.4）仅 65.1% Set-F1，"该出手时不出手"仍是核心瓶颈。 / Adapts cognitive science's Virtual Week to test agent prospective memory; best setup (GPT-5.4) reaches only 65.1% Set-F1 — "acting at the right moment" remains the bottleneck. |
| [[2607.12252]] FinResearchBench II | 104 真实金融查询 × 10 报告，经一致性 + 可区分性过滤得到 2,600 条"共识金标准"评分细则，对 10 个深度研究产品给出 22%–59% 的清晰分层。 / 104 real financial queries × 10 reports, filtered to 2,600 consensus gold rubrics, cleanly tiering 10 deep-research products from 22%–59% pass rate. |
| [[2607.12469]] Agent-Safety Reconstructability | 厂商中立的"重构性"指标，按八类决策属性打分；四张证据充分性卡 0.458–0.833，所有卡的反事实重放前置条件均未满足。 / A vendor-neutral reconstructability metric scoring 8 decision-property classes; sufficiency spans 0.458–0.833 and replay preconditions are unmet in all cards. |

### C. 评判者与打分方法学 / LLM-as-Judge & Scoring Methodology

| Paper | 描述 (中 / EN) |
|---|---|
| [[2607.12545]] VanillaBench | 系统量化 186 个对抗训练模型相对 vanilla 基线的干净准确率差距，即使最强鲁棒模型也落后 vanilla SOTA 4–29 个百分点。 / Quantifies the clean-accuracy gap of all 186 RobustBench models vs vanilla references; even the most robust model trails vanilla SOTA by 4–29 pp. |
| [[2607.12767]] Bayesian Accuracy — Length Bias | 揭示标准准确率偏短、长度归一化偏长，提出即插即用的"贝叶斯准确率"将长度偏差降低 4–8×，无需额外前向传播。 / Shows standard accuracy is short-biased and normalization is long-biased; proposes drop-in Bayesian accuracy cutting length bias 4–8× with no extra forward passes. |
| [[2607.12835]] LLM Rubric Meta-Evaluation | 首个针对论文复现的 LLM 生成 rubric 元评估；最强"蒸馏技能"设置在外在对齐上逼近人类（Spearman 0.78 vs 0.83），但仍偏细粒度、代码中心化。 / First meta-evaluation of LLM-generated rubrics for paper reproduction; strongest Distilled Skill setting nears humans (Spearman 0.78 vs 0.83) but stays over-fine-grained and code-centric. |
| [[2607.12885]] LLM Judges Too Generous | 多语言 QA 上无参考答案时评判者过度放行（泰卢固语错误答案放行率高达 60%），引入参考答案最多翻转 85% 判定且更贴近人类。 / In reference-free settings judges over-credit incorrect answers (up to 60% on Telugu); reference-answer visibility flips up to 85% of verdicts toward human agreement. |
| [[2607.12739]] ESFP — Epistemic Stance | 固定内容、变化提问框架衡量"认知立场灵活性"；发现它与通用能力基本正交——27B 开源模型并列第一，旗舰 Gemini-3.1-Pro 反而垫底。 / Measures prompt-conditioned epistemic register shift; flexibility is orthogonal to capability — a 27B open model ties for first while flagship Gemini-3.1-Pro ranks last. |

### D. 置信度、校准与安全 / Confidence, Calibration & Safety

| Paper | 描述 (中 / EN) |
|---|---|
| [[2607.12447]] SDC — Computational Basis of Confidence | 借用神经科学的统计决策置信度框架，证明 logit 差在简单感知/记忆任务上满足全部四签名，驱动近最优拒答（92.2%→99.95%），但在 CLEVR 复杂推理上失效。 / Imports the statistical-decision-confidence framework; logit difference satisfies all four signatures on perceptual/memory tasks and drives near-optimal abstention (92.2%→99.95%), but fails on CLEVR. |
| [[2607.12397]] Critic Experience Bank (CEB) | 免训练、自进化的评论家，用事后回看的执行经验做步骤级置信度估计，9/9 组合全部最优，ECE 相对最强基线降低高达 54%。 / Training-free self-evolving critic using hindsight execution experience for step-level confidence; best ECE/Brier/AUC in all 9 combos, cutting ECE up to 54%. |
| [[2607.12687]] CARE-PPO | 把 PPO 的 critic 当作置信度估计器（奖励=预测误差单调函数），AUSE 相比 logit/verbalized 基线减半，仅 2.4% 额外推理延迟，OOD 下更鲁棒。 / Repurposes PPO's critic as a confidence estimator (reward = monotonic in error); halves AUSE vs logit/verbalized baselines at 2.4% extra latency, more robust OOD. |
| [[2607.12792]] JADR — J-Space Safety | 用雅可比透镜在生成前读取 J-space 刻画"危险识别"，单次前向传播、无需裁判；INT8 基本无害，INT4 主要伤害 compliance 而非 safety。 / Reads J-space via the Jacobian lens before generation to score danger recognition; INT8 is essentially neutral, INT4 hurts compliance more than safety. |
| [[2607.12796]] One-Word Census | 用 31 个"命名一个类别词"提示量化 44 个模型的从众性，跨度 1.05–3.21 比特，最新旗舰最从众；连"发散"本身也收敛到同一个亚军答案。 / Quantifies conformity of 44 models on 31 one-word prompts, spanning 1.05–3.21 bits; newest flagships conform most, and even divergence converges to the same runner-up. |
| [[2607.12963]] Illusion of Robustness | 揭示"鲁棒性错觉"：任务无关上下文下整体准确率几乎不变（±2.1%），但掩盖了严重的样本级双向波动（WTD 最高 53.2%），且 SFT/DPO 会放大它。 / Reveals an "illusion of robustness": aggregate accuracy is stable (±2.1%) under irrelevant context but masks large two-sided per-example flips (WTD up to 53.2%), amplified by SFT/DPO. |

### E. 机制可解释性 / Mechanistic Interpretability

| Paper | 描述 (中 / EN) |
|---|---|
| [[2607.12279]] Countdown Subcircuit | 因果定位三个"倒计时注意力头"，跨任务（推文/SHA-256/俳句/DNA）甚至跨模型（Claude 3.5 Haiku 几何一致）复用。 / Causally isolates three "countdown" attention heads reused across tasks (tweets/SHA-256/haiku/DNA) and even across models (geometry matches Claude 3.5 Haiku). |
| [[2607.12526]] Source-Grounded Feature Inversion | 把特征反演重构为沿源-局部计算 DAG 的闭式 Wiener 修复，单次标定复用，像素余弦 0.939 vs 迭代法 0.035，176× 在线加速。 / Reframes feature inversion as closed-form Wiener repair along the source-local DAG; one calibration reused, pixel cosine 0.939 vs 0.035 for iterative search, 176× faster online. |
| [[2607.12863]] ROBIN — Attention Head Bias | 白盒头部级公平性调试：Fisher 敏感度排序 + 子空间投影去除偏置，BERT WinoBias 差距 45.97→19.14，且语言建模损失增加 ≤7.2%，远优于整头置零。 / White-box head-level fairness debugging via Fisher-sensitivity ranking + subspace projection; BERT WinoBias gap 45.97→19.14 with ≤7.2% LM loss increase, far better than whole-head zeroing. |

### F. 训练动力学与优化理论 / Training Dynamics & Optimization Theory

| Paper | 描述 (中 / EN) |
|---|---|
| [[2607.12332]] Diagonal Linear Network Dynamics | 推广鞍点到鞍点动力学到深层与一般两层对角线性网络，证明隐式偏置是"修正的 ℓ1 范数"（权重依赖初始化方向），并用结构不变流形解释机制。 / Extends saddle-to-saddle dynamics to deep/general two-layer diagonal linear networks; implicit bias is a modified ℓ1 (weights depend on init direction), explained via Structural Invariant Manifolds. |
| [[2607.12360]] LR Cooldown — Noise Structure | 证明冷却是否有益由噪声结构（各向同性 vs 各向异性）与优化器归一化共同决定，而非损失本身；同一损失同一噪声大小可产生相反效果。 / Shows cooldown's benefit is jointly set by noise structure (iso- vs anisotropic) and optimizer normalization, not the loss; same loss/noise can yield opposite outcomes. |
| [[2607.12438]] Fisher Rank Inflation | 发现含噪标签训练中 Fisher 有效秩在记忆噪声时先膨胀后塌缩，噪声样本在峰值期留一归因中高度富集（top-100 占比高达 96.2%），是记忆的谱签名。 / Identifies Fisher Rank Inflation — effective rank inflates then collapses during memorization; corrupted samples dominate peak-rank attribution (top-100 up to 96.2%), a spectral signature. |
| [[2607.12616]] FTSS — Flow Matching Memorization | 提出有限时间谱敏感度，无梯度、仅前向传播地暴露流匹配的"谱坍缩"，谱坍缩比 M 在 N≥1000 时饱和至 ~1.0，无需访问训练集即可判定记忆。 / Proposes Finite-Time Spectral Sensitivity, a gradient-free forward-pass metric exposing spectral collapse in flow matching; ratio M saturates at ~1.0 for N≥1000, auditing memorization without training-pool access. |
| [[2607.12735]] Grokking Representational Priors | 在模运算 grokking 上证明泛化由特征族对齐（而非"连贯性"）决定，完全无标签的交换不变性先验即足够，配合范数钳制获 17× 加速。 / Shows grokking generalization is gated by feature-family alignment (not coherence); a fully label-free commutativity prior suffices, and with a norm clamp yields 17× speedup. |

### G. 量化与效率 / Quantization & Efficiency

| Paper | 描述 (中 / EN) |
|---|---|
| [[2607.12266]] Saturation Quantization Coverage Model | 把量化损失分解为一阶主导（85–99% 方差，根源是饱和），给出闭式误差下限，匹配内存下比 ModelOpt 低 17–21% KL，子 4-bit 区间决定模型存活。 / Decomposes quantization loss as first-order dominated (85–99% variance, cause: saturation), gives a closed-form certificate, beats ModelOpt by 17–21% KL at matched memory, decides survival below 4 bits. |

### H. 代码、可靠性与软件工程 / Code, Reliability & Software Engineering

| Paper | 描述 (中 / EN) |
|---|---|
| [[2607.12273]] Code-MUE | 纯黑盒、基于执行的代码不确定性量化：构建语义交互图并用 Von Neumann 熵，与功能正确性的 Spearman 相关高达 -0.98，远超词法基线。 / Black-box execution-based code uncertainty via Semantic Interaction Graphs + Von Neumann entropy; Spearman ρ up to -0.98 with correctness, far beating lexical baselines. (ISSTA 2026) |
| [[2607.12962]] PoPE — Self-Repair Negative Result | 预注册、安慰剂对照评估冻结小代码模型（≤1.5B）的"学习式错误条件自修复"，提示/权重两通道均未超过安慰剂孪生，并撤回自身最强正向收益。 / Preregistered placebo-controlled evaluation of learned self-repair in frozen small code models (≤1.5B); neither prompt nor weight channel beats form-matched placebo, and its own positive is withdrawn. |
| [[2607.12868]] Deep4ge — DNN Fault Dataset | 发布 14,227 次 DNN 训练运行的公开故障轨迹数据集（27 变异算子 × 7 类故障），证明完整轨迹特征（MCC 0.227）显著优于末轮特征（0.150）。 / Releases 14,227 public DNN training-run trajectories (27 mutation operators × 7 fault categories); trajectory features (MCC 0.227) substantially beat final-epoch features (0.150). |

### I. 应用与立场论文 / Applications & Position Papers

| Paper | 描述 (中 / EN) |
|---|---|
| [[2607.12474]] Mechanistic World Models (Oxford) | 立场论文：把科学发现重构为"知识组织"问题，提出以可复用"机制"为中心的表征范式，统一变量/机制/结构发现与简约性、组合性。 / Position paper reframing scientific discovery as knowledge organisation around reusable "mechanisms," unifying variable/mechanism/structure discovery with parsimony and compositionality. |
| [[2607.12455]] EvoQuant — Quant Trading | 把量化策略优化定义为"验证器引导的程序进化"，A 股 + 比特币 7 个策略家族平均 Sharpe +0.829，自适应晋升引擎是核心（去掉则跌至 +0.128）。 / Frames quant strategy optimization as verifier-guided program evolution; +0.829 avg Sharpe across 7 A-share/Bitcoin families, with the adaptive promotion engine as the key enabler. |
| [[2607.12954]] PV Power Forecasting Robustness | 物理约束的 NWP 误差注入框架跨 5 美国气候区压测 6 个预测模型，LightGBM 干净数据最强但随噪声劣化，GRU/PatchTST 在中高噪声下更韧。 / Physically constrained NWP error-injection benchmark across 5 US climate zones; LightGBM is strongest on clean data but degrades fast, while GRU/PatchTST are more robust under noise. |
| [[2607.12780]] Quantum Circuit Autoregressive Drift | 44.8M Transformer 做量子电路优化，参数化电路达中位保真度 1.000，但 Clifford+T 因"自回归漂移"（长度主导）从 88% 跌到 ≥26 门的近 0%。 / A 44.8M transformer optimizes quantum circuits: median fidelity 1.000 on parameterized circuits, but Clifford+T exact-match collapses from 88% to ~0% beyond 26 gates due to autoregressive drift. |
| [[2607.12298]] EIR — FPGA Self-Healing | 层次化数字孪生（Rabbit 快检 + Tortoise 精确恢复）在 FPGA SoC 上实现自愈，≥95% 故障检出率且保持基线面积，DMR 则把功耗提升 +89%。 / Hierarchical digital twins (Rabbit fast-detect + Tortoise precise-recover) enable FPGA SoC self-healing at ≥95% detection preserving baseline area, vs DMR's +89% power. |

---

## All Papers

| # | arXiv ID | 标题 / Title | 主题 / Topic |
|---|---|---|---|
| 1 | [[2607.12227]] | Rethinking Harness Evolution Evaluation | Agent Benchmarks / 智能体基准 |
| 2 | [[2607.12252]] | FinResearchBench II | Agent Benchmarks / 智能体基准 |
| 3 | [[2607.12254]] | Recursively Self-Improving Agents | Agents & Memory / 智能体与记忆 |
| 4 | [[2607.12266]] | Saturation Quantization Coverage Model | Quantization / 量化 |
| 5 | [[2607.12273]] | Code-MUE | Code & SE / 代码与软件工程 |
| 6 | [[2607.12279]] | Countdown Subcircuit | Mechanistic Interp / 机制可解释性 |
| 7 | [[2607.12298]] | EIR FPGA Self-Healing | Applications / 应用 |
| 8 | [[2607.12332]] | Diagonal Linear Network Dynamics | Training Dynamics / 训练动力学 |
| 9 | [[2607.12338]] | How Many Tasks Are Enough | Agent Benchmarks / 智能体基准 |
| 10 | [[2607.12360]] | LR Cooldown Noise Structure | Training Dynamics / 训练动力学 |
| 11 | [[2607.12385]] | PM-Bench Prospective Memory | Agent Benchmarks / 智能体基准 |
| 12 | [[2607.12397]] | Critic Experience Bank (CEB) | Confidence & Safety / 置信度与安全 |
| 13 | [[2607.12438]] | Fisher Rank Inflation | Training Dynamics / 训练动力学 |
| 14 | [[2607.12447]] | SDC Confidence in LLMs | Confidence & Safety / 置信度与安全 |
| 15 | [[2607.12455]] | EvoQuant Trading | Applications / 应用 |
| 16 | [[2607.12469]] | Agent-Safety Reconstructability | Agent Benchmarks / 智能体基准 |
| 17 | [[2607.12474]] | Mechanistic World Models | Position / 立场论文 |
| 18 | [[2607.12526]] | Source-Grounded Feature Inversion | Mechanistic Interp / 机制可解释性 |
| 19 | [[2607.12545]] | VanillaBench | LLM-as-Judge / 评判者方法学 |
| 20 | [[2607.12616]] | FTSS Flow Matching Memorization | Training Dynamics / 训练动力学 |
| 21 | [[2607.12625]] | KnowAct-GUIClaw | Agents & Memory / 智能体与记忆 |
| 22 | [[2607.12640]] | GRPO Failure Web Agent | Agents & Memory / 智能体与记忆 |
| 23 | [[2607.12687]] | CARE-PPO | Confidence & Safety / 置信度与安全 |
| 24 | [[2607.12735]] | Grokking Representational Priors | Training Dynamics / 训练动力学 |
| 25 | [[2607.12739]] | ESFP Epistemic Stance | LLM-as-Judge / 评判者方法学 |
| 26 | [[2607.12747]] | Oat Failure Attribution | Agents & Memory / 智能体与记忆 |
| 27 | [[2607.12767]] | Bayesian Accuracy Length Bias | LLM-as-Judge / 评判者方法学 |
| 28 | [[2607.12780]] | Quantum Circuit Autoregressive Drift | Applications / 应用 |
| 29 | [[2607.12790]] | Double Ratchet | Agents & Memory / 智能体与记忆 |
| 30 | [[2607.12792]] | JADR J-Space Safety | Confidence & Safety / 置信度与安全 |
| 31 | [[2607.12796]] | One-Word Census | Confidence & Safety / 置信度与安全 |
| 32 | [[2607.12835]] | LLM Rubric Meta-Evaluation | LLM-as-Judge / 评判者方法学 |
| 33 | [[2607.12863]] | ROBIN Attention Bias | Mechanistic Interp / 机制可解释性 |
| 34 | [[2607.12868]] | Deep4ge DNN Faults | Code & SE / 代码与软件工程 |
| 35 | [[2607.12885]] | LLM Judges Too Generous | LLM-as-Judge / 评判者方法学 |
| 36 | [[2607.12893]] | MemOps Memory Benchmark | Agents & Memory / 智能体与记忆 |
| 37 | [[2607.12954]] | PV Forecasting Robustness | Applications / 应用 |
| 38 | [[2607.12962]] | PoPE Self-Repair | Code & SE / 代码与软件工程 |
| 39 | [[2607.12963]] | Illusion of Robustness | Confidence & Safety / 置信度与安全 |

---

**Count verification / 计数核对:** Overview lists **39** papers; the directory contains **39** `.md` files excluding `overview.md`. Counts match. / 本总览列出 **39** 篇；目录中除 `overview.md` 外共有 **39** 个 `.md` 文件，计数一致。
