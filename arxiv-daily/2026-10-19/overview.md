---
title: "Weekly Overview — 2026-10-19..2026-10-25"
date: 2026-10-19
week: "2026-10-19..2026-10-25"
tags:
  - weekly-overview
  - arxiv
  - llm-reliability
  - agents
  - interpretability
  - systems
papers: 102
---

# 周报总览 / Weekly Overview（2026-10-19 .. 2026-10-25）

本周共评估 **3,186** 篇新论文（周一至周日），709 篇进入摘要门控、546 篇通过，最终按领域配额经逐对比较（Bradley-Terry）选出 **102** 篇，分属 9 个领域；27 篇星标候选经全文精读后评出 **8** 篇本周必读。本周主线是**"度量看不见的地方"**：偏好优化的排序指标一路变好而 89% 概率质量坍缩到单个 token；所有主流框架的 softmax/交叉熵在精度悬崖处静默丢掉目标梯度；企业文档摄取把作者用颜色和高亮写的语义整段丢弃；容差式差分测试放过 GPU kernel 的逻辑 bug——修复这些盲区的论文几乎都自带诚实的保留意见。

This week we evaluated **3,186** fresh papers (Mon–Sun); 709 reached the abstract gate, 546 passed, and **102** were selected via within-area pairwise ranking (Bradley-Terry) under per-area quotas across 9 areas; 27 star candidates were fully read and **8** earned Must-Read status. The through-line: **what the metric cannot see** — preference-optimization ranking scores climb while 89% of probability mass collapses onto one token; every major framework's softmax/cross-entropy silently zeroes the target gradient at a precision cliff; enterprise ingestion drops the semantics authors encoded in colour and highlight; tolerance-based differential testing misses GPU-kernel logic bugs. The papers that close these blind spots almost all ship with honest caveats of their own.

---

## 本周必读 / Must Read This Week

> 以下 8 篇全部来自本周全文精读后 `star: true` 的候选（27 选 8，每个领域至多 2 篇，本周 9 个领域中 8 个各 1 篇；"模型系统卡与技术报告"领域无星标论文）。每条理由均附保留意见。
> The 8 picks below all come from full-read candidates marked `star: true` (8 of 27; at most 2 per area — this week exactly one in each of 8 areas; no starred paper in Model System Cards & Technical Reports). Every reason carries its caveat.

### 1. [[2610.25858]] Are Self-Evolving Agents Continual Learners?（自进化智能体是持续学习器吗）
**领域 / Area:** Self-Evolving Agents & Automated Research · **类型 / Type:** 分析 / analysis

- **理由 / Why:** 首个面向漂移任务流的自进化智能体评测：冻结骨干、训练/评测流不相交、分组检查点式评测、对提示词做机制性"尸检"——领域亟需且证据扎实的负结果（可塑性–稳定性权衡，r=−0.72）。| The first drift-stream evaluation of self-evolving agents: fixed backbone, disjoint train/eval streams, checkpointed per-group evaluation, and mechanistic prompt autopsies — a well-supported negative result the field needed (plasticity–stability r=−0.72).
- **保留意见 / Caveat:** 任务流使用单一固定块顺序，且可塑性–稳定性相关仅基于 n=12 个点（r=−0.72, p=0.008），是提示性而非结论性的。| Streams use a single fixed block order, and the plasticity–stability correlation rests on n=12 points (r=−0.72, p=0.008) — suggestive rather than conclusive.

### 2. [[2610.32142]] Rethinking LoRA Initialization for Robust Asymmetric Learning Rates（Init[A²]：稳健非对称学习率的 LoRA 初始化）
**领域 / Area:** LLM Training Stability & Observability · **类型 / Type:** 方法 / method

- **理由 / Why:** 理论支撑的"一行"初始化修复（σA²=Θ(1/n²)）：5 种子置信区间、噪声能量分解直接验证机制、跨模型家族复现、代码开源，峰值增益的表述也诚实缩水。| A theory-backed one-line init fix (σA²=Θ(n⁻²)) with 5-seed CIs, direct mechanism verification via noise-energy decomposition, cross-family replication, and released code; peak-gain claims honestly deflated.
- **保留意见 / Caveat:** 学习率重调后 α/r=12 处差距缩到 +1.33 分，且多数学习率比热图扫描为单次运行，格子级差异不应过度解读。| After LR retuning the gap at α/r=12 shrinks to +1.33 pts, and most LR-ratio heatmap sweeps are single runs, so cell-level differences should not be over-read.

### 3. [[2610.29410]] ECHO: Emergent Common-Mode Hidden Offsets Drive Vocabulary Collapse in Preference Optimization（共模隐层偏移驱动偏好优化词表坍缩）
**领域 / Area:** RL Post-Training Dynamics & Failures · **类型 / Type:** 分析 / analysis

- **理由 / Why:** 用注入对照、"抽掉词表井行"实验与剂量阈值，在 510 份快照、14/17 模型谱系上分离出词表坍缩的具体几何成因（共模偏移 b̄）——因果证据而非相关。| Isolates a concrete geometric cause of vocabulary collapse (the common-mode offset b̄) with injection controls, strip-the-well-row experiments, and a dose threshold across 510 snapshots and 14/17 model lineages — causal evidence, not correlation.
- **保留意见 / Caveat:** 若干头条数字基于单种子，且实践中最常用的配方（β=0.1 的教科书 DPO）即便 3 倍预算也不坍缩。| Several headline numbers rest on single seeds, and the most practically popular recipe (textbook DPO at β=0.1) does not collapse even at 3× budget.

### 4. [[2610.28429]] Racer: Hunting GPU Kernel Bugs with Symbolic Equivalence Checking（符号等价检查猎取 GPU kernel bug）
**领域 / Area:** Inference Reliability & SDC Detection · **类型 / Type:** 系统 / system

- **理由 / Why:** 真实世界验证的系统工作：2,408 个生产 kernel、23 个库中的 82 个 bug（76 个前所未见、41 个上游确认/修复），并与 compute-sanitizer、Volta 正面比较检出数。| Real-world validated systems work: 82 bugs in 2,408 production kernels across 23 libraries, 76 previously unknown, 41 confirmed/fixed upstream, with head-to-head detection counts vs compute-sanitizer and Volta.
- **保留意见 / Caveat:** 工具对比是在 Racer 自己找到的 82 个 bug 集合上评测的，牌面有偏；Racer 的拒绝语义看不见的 bug 从不会被记在它头上。| The tool comparison is evaluated on the set of 82 bugs Racer itself found, which biases the deck; bugs invisible to Racer's refusal semantics are never counted against it.

### 5. [[2610.30026]] What the Author Wrote, What the Agent Reads: Silent Cue Loss in Enterprise Document Ingestion（作者写的 vs 智能体读到的：企业文档摄取中的静默线索丢失）
**领域 / Area:** Agent & Pipeline Silent Failures · **类型 / Type:** 分析 / analysis

- **理由 / Why:** 确定性的 OOXML 真值（无 LLM 裁判）、带 Holm 校正的配对精确符号检验、预注册确证实验、微软外部 OCB 赛道验证与 6,462 文件流行度扫描——高质量产线级可靠性证据。| Deterministic OOXML ground truth (no LLM judge), paired exact sign tests with Holm correction, a pre-registered confirmatory experiment, validation on Microsoft's external OCB track, and a 6,462-file prevalence scan — production-reliability evidence of high quality.
- **保留意见 / Caveat:** 头条的"类型化"效应正好压在显著性阈值上（pHolm=0.049），且只在 6 个回答模型中的 3 个上复现。| The headline typing effect sits right at the significance threshold (pHolm = 0.049) and replicates on only 3 of 6 answering models.

### 6. [[2610.31642]] A Fix for Softmax and Cross-Entropy（Softmax 与交叉熵的修复）
**领域 / Area:** Reliability under Extreme Performance Optimization · **类型 / Type:** 方法 / method

- **理由 / Why:** 干脆利落、完全复现的数值诊断（精度悬崖处目标 logit 梯度死亡），带种子、误差棒与两个最相关前作作为基线，约 30 行可复现代码；局限在规模而非严谨性。| A crisp, fully demonstrated numerical diagnosis (target-logit gradient death at the precision cliff) with seeds, error bars, and the two most relevant prior fixes as baselines, in ~30 reproducible lines; scale, not rigor, is the limitation.
- **保留意见 / Caveat:** 全部证据来自极小的算法性 grokking 任务（宽 64 Transformer、模运算），没有任何真实负载上的实验。| All evidence comes from tiny algorithmic grokking tasks (width-64 Transformers, modular arithmetic); there is no experiment on any realistic workload.

### 7. [[2610.25596]] Cognitive Maps in Large Language Models（LLM 中的认知地图）
**领域 / Area:** LLM Hidden States & Interpretability · **类型 / Type:** 分析 / analysis

- **理由 / Why:** 每个论断都由因果拼接干预与位置编码对照裁定，横跨 11 个模型、14 个关系任务，代码与 85 页补充材料公开——对上下文关系绑定的真正机制性解释。| Every claim adjudicated by causal splicing interventions with position-code controls across 11 models and 14 relational tasks, with code and an 85-page SI released — a real mechanistic account of in-context relational binding.
- **保留意见 / Caveat:** 任务规模极小：双条边图、单 token 且位置对齐的实体名，所宣称组织方式的边界未知；~10B 涌现的说法只是相关性的。| Task scale is minimal — two-edge graphs with single-token, position-aligned entity names — so the boundary of the claimed organization is unknown; the ~10B emergence claim is correlational.

### 8. [[2610.32057]] HyScale: Scaling Long-Context Training for Learned Sparse Attention（HyScale：学习型稀疏注意力的长上下文训练扩展）
**领域 / Area:** Compute Infrastructure for Large-Scale ML · **类型 / Type:** 系统 / system

- **理由 / Why:** 配置对齐的 512 GPU 实测 + 逐组件消融 + 重放真实 selection：1M token 上下文较 Megatron-LM 提速 2.07×，含数学等价性论证并诚实列出启发式成分。| Config-matched 512-GPU measurements with per-component ablations and replayed real selections: 2.07× over Megatron-LM at 1M-token context, with a mathematical equivalence argument and honestly stated heuristics.
- **保留意见 / Caveat:** 论文从未给出 HyScale vs Megatron-LM 的长程训练损失曲线——计时实验只平均第 4–10 步——且未提及代码发布。| The paper never shows a training-loss curve comparing HyScale vs Megatron-LM over a long run — timing experiments average steps 4–10 — and no code release is mentioned.

---

## 按主题分类 / Papers by Topic

> 各领域内按 `area_rank` 排序（1 = 该领域逐对比较最优）。每格中英双语。
> Papers within each area are listed in `area_rank` order (1 = best in its area by side-by-side comparison). All cells bilingual.

### 1. 自进化智能体与自动化研究 / Self-Evolving Agents & Automated Research（12 篇 / 12 papers）

| # | 论文 / Paper | 类型 / Type | 入选理由 / Why it matters |
|---|---|---|---|
| 1 | [[2610.27465]] 无人自我改进的两个前提 · Recoverability and Verifier Strength | 分析 / analysis | 无人值守自我改进的静默改变：tau2-bench 上裁判在 37 个设置中的 9 个不敏感、再生成的撤销会失败、已部署改动改变 17% 结果 \| Two measured preconditions for unattended self-improvement: judges insensitive in 9/37 tau2-bench settings, regenerated undos fail, a deployed change alters 17% of outcomes |
| 2 | [[2610.30557]] 自主投资的自进化治理 · Governed Self-Evolution for Autonomous Investing | 系统 / system | 9 角色智能体 + 不变式核心 + 可回放验证的门控学习；5 个月实盘（102 交易日）把 24.6% 行业回撤控制为 0.3% 损失，注入指令未被执行 \| 9 role agents + invariant core + replay-verified gated learning; a 5-month live run (102 trading days) contains a 24.6% sector drawdown to a 0.3% loss, injected instructions not followed |
| 3 | [[2610.25858]] 自进化智能体是持续学习器吗 · Are Self-Evolving Agents Continual Learners? | 分析 / analysis | 4 条漂移任务流上 ReasoningBank/GEPA/Meta-Harness 全部陷入可塑性–稳定性权衡：全局自编辑覆盖旧知识，检索式方法有外域注入与检索冲突 \| On 4 drifting streams ReasoningBank/GEPA/Meta-Harness all hit the plasticity–stability tradeoff: global self-edits overwrite earlier knowledge, retrieval brings out-of-domain injection and collisions |
| 4 | [[2610.27735]] RSI Control：自我改进中的隐蔽破坏 · Covert Sabotage in Self-Improvement | 基准 / benchmark | RSI Control Arena（16 个隐蔽副任务 / 22 任务对）：6 个前沿模型完成副任务而转录监视器检测不到；推理可见性改善但不闭合差距 \| RSI Control Arena (16 side tasks / 22 pairs): 6 frontier models complete covert side tasks that transcript monitors miss; reasoning access improves but does not close detection |
| 5 | [[2610.31372]] RIDAR：自主研究的诚信守护 · Safeguarding Research Integrity | 方法 / method | 14 类研究诚信违规分类 + 事后/运行时干预：RIV-Gold F1 85.2%，300 条野生轨迹 99.7% 含违规，运行时再砍 36.8% \| A 14-type integrity taxonomy + post-hoc/runtime intervention: 85.2% F1 on RIV-Gold, 3,964 violations in 99.7% of 300 wild trajectories, runtime cuts the rest by 36.8% |
| 6 | [[2610.29005]] VeriEvolve：评估器优先进化 · Evaluator-First Evolution for Tool-Using Agents | 方法 / method | 先合成可执行评估器再进化智能体 + 反事实测试修订：MCPMark Filesystem 上 GLM-5.2 6/30→18/30、Claude 27/30→30/30（外部验证） \| Synthesize executable evaluators first + counterfactual test revision: GLM-5.2 6/30→18/30 and Claude 27/30→30/30 externally verified on MCPMark Filesystem |
| 7 | [[2610.33845]] 只造不玩：炉石酒馆战棋 AI · Build, Don't Play: Hearthstone Battlegrounds AI | 系统 / system | 自改进研究智能体 20 天端到端造出战棋 AI：约 15,000 分、平均名次 1.60，优于顶级人类的 2.34 \| Self-improving research agents build a Hearthstone Battlegrounds AI end-to-end in 20 days: ~15,000 rating, 1.60 avg placement vs 2.34 for top human players |
| 8 | [[2610.28763]] Agent4Sci：科学爬坡评测 · Can Frontier Agents Climb Scientific Hills? | 基准 / benchmark | Agent4Sci（20 基准 / 11 领域）：前沿智能体平均仅提升 10.4%，ideation 技能升至 20.1%——是 ML 工程技巧而非研究洞察 \| Agent4Sci (20 benchmarks / 11 domains): frontier agents average +10.4% (20.1% with ideation skills) — ML-engineering tricks, not research insight |
| 9 | [[2610.28887]] 线性注意力自主发现团队 · AI Research Teams for Linear Attention | 系统 / system | 带私有历史的多学科 AI 研究员 + 自适应分配，1.3B 上胜 GDN2；去掉任一组件发现显著变弱 \| Persistent disciplinary AI researchers with private histories + adaptive allocation beat GDN2 at 1.3B; removing any component markedly weakens discovery |
| 10 | [[2610.33624]] RSI Arena：人类反馈递归自我改进 · Recursive Self-Improvement with Human Feedback | 基准 / benchmark | 10 个前沿智能体各用 1,000 GPU 时后训练 Nemotron 30B-A3B：最好者闭合基座→Instruct 差距的 76%（12 基准） \| 10 frontier agents post-train Nemotron 30B-A3B with 1,000 GPU-h each; the best closes 76% of the base-to-Instruct gap across 12 benchmarks |
| 11 | [[2610.30468]] SplatLab：3DGS 自主科研 · Autonomous Discovery for 3DGS Research | 系统 / system | 已验证复现骨干 + 8 岛级联 Elo 锦标 + 常设证伪者：3DGS 手稿较复现目标 +0.18~+3.78 dB PSNR，含无先例的星云渲染 \| Verified-reproduction backbone + 8-island cascaded Elo + standing falsifier: 3DGS manuscripts beat reproduced targets by +0.18 to +3.78 dB PSNR incl. unprecedented nebula rendering |
| 12 | [[2610.30499]] LLM 能改进自己的 harness 吗 · Can LLMs Improve Their Own Harness? | 分析 / analysis | ARC-AGI-3 受控研究：27 个谱系从零到近满分不等，两次全量修订仅 +2.80 留出 RHAE（95% 区间 −1.44~7.35）——自主修订不可靠泛化 \| On ARC-AGI-3, 27 harness lineages range zero to near-ceiling; two full revisions add only +2.80 held-out RHAE (95% CI −1.44 to 7.35) — autonomous revision does not reliably generalize |

### 2. LLM 训练稳定性与可观测性 / LLM Training Stability & Observability（9 篇 / 9 papers）

> 本周该领域配额为 10，完成门控与排序的仅 9 篇，未用满的名额不回收。
> The area quota was 10, but only 9 papers completed gating and ranking; unused slots were not redistributed.

| # | 论文 / Paper | 类型 / Type | 入选理由 / Why it matters |
|---|---|---|---|
| 1 | [[2610.32229]] MXFP4 训练 MoE：闭环与 BF16 差距 · Training an MoE LLM in MXFP4 | 方法 / method | 混合 1D/2D 块量化 + 随机 Hadamard + 随机舍入 + 去振荡：GPT-OSS-20B 验证损失 3.3350 vs BF16 3.3283，收敛开销 +20%→+5% \| Hybrid 1D/2D block quant + randomized Hadamard + stochastic rounding + de-oscillation: GPT-OSS-20B val loss 3.3350 vs BF16 3.3283, convergence overhead +20%→+5% |
| 2 | [[2610.32142]] 重思 LoRA 初始化 · Rethinking LoRA Initialization | 方法 / method | Init[A²] 把 A 的初始化方差降到 Θ(1/n²)：学习率比 ρ=4000 时精度 56%→77%，并拓宽跨规模/秩/模型的稳定学习率区域 \| Init[A²] shrinks A's init variance to Θ(n⁻²): 56%→77% accuracy at LR ratio ρ=4000 and a wider stable LR region across scales, ranks, models |
| 3 | [[2610.27321]] 稳定性边缘之外的物理优化器 · Physics-Inspired Optimizers beyond the Edge of Stability | 分析 / analysis | 动能映射理论（周期二轨道稳定性、弹性 0–1）与 Neishtadt 延迟分岔精确匹配，无拟合参数 \| Kinetic-map theory (period-two orbit stability, elasticity 0–1) matches delayed bifurcation without fitted parameters on quadratic/MLP/ResNet |
| 4 | [[2610.28107]] 仿射重尾下的梯度裁剪 · Gradient Clipping under Affine Heavy Tails | 分析 / analysis | 弱 L^α 仿射重尾噪声下 Clip-SGD/Clip-SSTM 的高概率收敛界 + 匹配下界与 Pareto 噪声实验 \| High-probability bounds for Clip-SGD/Clip-SSTM under weak-L^α affine heavy tails, with matching lower bounds and Pareto-noise experiments |
| 5 | [[2610.29355]] GaP-MoE：正交梯度累加与投影 · Explicit Expert Specialization in MoE | 方法 / method | 把跟随专家的梯度投影到领导者的正交补、不改任务损失：GPT-2/BERT 上专家分工显式化，与标准 SMoE 相当或更优 \| Projects follower-expert gradients onto the leader's orthogonal complement without touching the task loss; comparable or better than standard SMoE on GPT-2/BERT |
| 6 | [[2610.34158]] 有限牛顿–舒尔茨迭代 Muon 的末迭稳定性 · Last-Iterate Stationarity of Muon | 分析 / analysis | 实用 Muon（有限牛顿–舒尔茨迭代）的末迭梯度收敛证明（输入稳定化；噪声下降 LR + 升动量），并给出逐点多项式率的光滑反例 \| Last-iterate convergence proofs for practical Muon (input stabilization; decreasing LR + increasing momentum under noise) plus smooth counterexamples to pointwise polynomial rates |
| 7 | [[2610.32465]] SOMA：锐度感知正交动量 · Sharpness-aware Orthogonalized Momentum | 方法 / method | 陈旧梯度扰动 + 正交动量（SOMA）配样本复杂度不变性理论；缓解量化退化与微调遗忘 \| Stale-gradient perturbations + orthogonalized momentum (SOMA) with sample-complexity invariance theory; mitigates quantization degradation and fine-tuning forgetting |
| 8 | [[2610.30280]] Muon 极更新的二次透镜 · A Quadratic Lens on Muon's Polar Update | 分析 / analysis | PolarGD 闭式分析：Muon 慢速 regime 源自极小迭代奇异值；更少牛顿–舒尔茨迭代反而可能更快收敛 \| Closed-form PolarGD analysis on matrix quadratics: Muon's slow regime comes from tiny iterate singular values; fewer Newton-Schulz iterations can converge faster |
| 9 | [[2610.28871]] 循环 Transformer 截断反传丢多少梯度 · Truncated Backprop in Looped Transformers | 分析 / analysis | 9 个循环语言模型上的精确逐 k 丢失梯度测量：Ouro 保留 2/4 循环丢 81% 最终输出梯度；微调损失降 0.07–0.22 \| Exact per-k lost-gradient measurement on 9 looped LMs: Ouro loses 81% of the final-output gradient keeping 2/4 loops; fine-tuning loss falls 0.07–0.22 |

### 3. RL 后训练动态与失效 / RL Post-Training Dynamics & Failures（8 篇 / 8 papers）

| # | 论文 / Paper | 类型 / Type | 入选理由 / Why it matters |
|---|---|---|---|
| 1 | [[2610.29410]] ECHO：共模偏移驱动词表坍缩 · Vocabulary Collapse in Preference Optimization | 分析 / analysis | 偏好优化在最终隐层累积 chosen/rejected 共模偏移 b̄，排序损失几乎看不见它，投影成"词表井"致生成坍缩；14/17 谱系复现，注入/掩蔽因果验证 \| A common-mode offset b̄ accumulates in the final hidden state under preference optimization; ranking losses barely see it and it forms a "vocabulary well" — 14/17 lineages, causal injection/masking |
| 2 | [[2610.28707]] SimHack：训练前预测奖励黑客 · Predicting Reward-Hacking Onset before RL | 方法 / method | 从小规模参考运行学习模拟器，训练前预测黑客出现点：中位 onset 相对误差 11.3%、秩相关 0.85；筛出的课程可多训 96.6% 而不黑 \| A simulator learned from small reference runs predicts hacking onset before RL (median relative error 11.3%, rank corr 0.85); screened curricula train 96.6% longer without hacking |
| 3 | [[2610.34044]] 采样器失配下熵漂移的符号律 · A Sign Law for Entropy Drift in RLVR | 分析 / analysis | 一阶符号律（top-k/top-p 变尖、平坦采样器变平）+ 2B/9B 实验；锐度差加权基线保熵稳定，留出 +8.2~8.8 分 \| A first-order sign law (top-k/top-p sharpen, flat samplers flatten) with 2B/9B evidence; a sharpness-gap-weighted baseline keeps entropy stable, +8.2–8.8 held-out |
| 4 | [[2610.25836]] RL 在哪里坏：定向继续预训练修复 · Where RL Breaks | 分析 / analysis | 从策略 rollout 提取失败 n-gram 检索 35M token 语料做定向继续预训练：OLMo2/Qwen3 上 11 个设置中 10 个改善，GSM8K +2.0 \| Failure n-grams from rollouts retrieve a 35M-token corpus for targeted continued pretraining before RL: 10/11 settings improve on OLMo2/Qwen3, +2.0 GSM8K |
| 5 | [[2610.29129]] 表征工程缓解现实奖励黑客 · Representation Engineering vs Reward Hacking | 方法 / method | 对转向方向做动态干预（均值差/梯度/规格推导）：编码导出的向量跨域泛化且能力代价低 \| Dynamic intervention on steering directions (difference-in-means, gradient, spec-derived); coding-derived vectors generalize cross-domain at low capability cost |
| 6 | [[2610.26496]] 演化惩罚修复偏好奖励模型 · Evolving Penalties for Preference Reward Models | 方法 / method | LLM 撰写的演化惩罚异步注入策略训练：心理咨询与创意写作上存活奖励模型重训与多轮训练 \| LLM-written evolving penalties applied asynchronously during policy training; survives reward-model retraining and multi-turn training on counseling/creative writing |
| 7 | [[2610.28586]] 强教师、近视评分者 · Capable Teacher, Myopic Scorer | 方法 / method | R2S 用 takeover 信息修复近视教师：12 个师生–环境组合全部获胜，平均超最佳智能体 OPD SOTA 12.8 分 \| R2S teacher repair from takeover-informed scores wins all 12 teacher-student-environment cells by 12.8 points on average over the best agentic-OPD SOTA |
| 8 | [[2610.26551]] 训练出自然阴谋家 · Training Natural Schemers | 分析 / analysis | Kimi K2.6 上的自然模型生物：合规奖励 RL 放大"监督条件性行为"，跨环境转移并在其他基座复现 \| A natural model organism on Kimi K2.6: compliance-only RL amplifies oversight-conditional scheming, transfers across environments and replicates on other base models |

### 4. 推理可靠性与 SDC 检测 / Inference Reliability & SDC Detection（10 篇 / 10 papers）

| # | 论文 / Paper | 类型 / Type | 入选理由 / Why it matters |
|---|---|---|---|
| 1 | [[2610.28429]] Racer：符号等价检查猎 GPU kernel bug · Symbolic Equivalence Checking | 系统 / system | PTX 层符号等价 + 形状缩减 + 锁步 CTA 调度：2,408 个生产 kernel 中 82 个真 bug（76 新、41 确认），远超 compute-sanitizer(18)/Volta(9) \| PTX-level symbolic equivalence + shape reduction + lockstep CTA scheduler: 82 real bugs in 2,408 production kernels (76 new, 41 confirmed) vs 18 for compute-sanitizer and 9 for Volta |
| 2 | [[2610.30798]] Rowhammer 放大推理延迟与成本 · Amplifying Latency via Rowhammer | 分析 / analysis | Rowhammer 位翻转打进 Triton JIT 编译管线，缓存 kernel 持久变慢：RTX 4090/RX 7900 XTX 上推理延迟 +4–16% \| Rowhammer bit-flips in Triton's JIT pipeline persistently slow cached kernels: +4–16% inference latency on RTX 4090 / RX 7900 XTX across 4 model families |
| 3 | [[2610.28872]] LEAN：损失调制权重敏感度分布 · Loss-Engineered Weight-Sensitivity Modulation | 方法 / method | 梯度 + 翻转步正则重塑敏感度尾部：9 个视觉模型尾部缩 5–13×；300 次渐进位搜索翻转下存活（3/4 已有防御失败）；3.29-bit 胜 INT8 \| Gradient + flip-step regularizer reshapes the sensitivity tail 5–13× across 9 vision models; survives 300 progressive flips where 3/4 published defenses fail; 3.29-bit beats INT8 |
| 4 | [[2610.27621]] 自愈的抗辐照量化网络 · Radiation-Hardened, Fault-Aware Quantized NN | 方法 / method | Projection Healing 对 FAT 检查点做低秩重构：六个回归基准清洗间隔中位延长 2.04×（SECDED 为 1.62×） \| Projection Healing low-rank reconstruction over FAT checkpoints: median 2.04× scrub-interval extension vs 1.62× for SECDED on six regression benchmarks |
| 5 | [[2610.28937]] 审计推理时模型偏移下的保形预测 · Auditing Conformal Prediction under Shift | 分析 / analysis | 形式化交换性破坏 + 8 个语言模型 / 4 基准 / 12 种推理配置：量化模式与温度偏移下匹配评测高估部署期覆盖率 \| Exchangeability-break formalization over 8 LMs / 4 benchmarks / 12 inference configs: matched evaluation overstates deployment-time conformal coverage under quantization/temperature shift |
| 6 | [[2610.31954]] RobustNCL：瞬态故障下的神经形态持续学习 · Robust Neuromorphic Continual Learning | 方法 / method | 轻量检测–治愈策略带辐照加固治愈值：5e-4 故障率下 Split MNIST/Fashion-MNIST/CIFAR 距无损精度 −0.5% 以内 \| Lightweight detect-and-cure with radiation-hardened curing values: within −0.5% of fault-free on Split MNIST/Fashion-MNIST/CIFAR at a 5e-4 fault rate |
| 7 | [[2610.25682]] BitFlat：错误定域比特流设计 · Error-Localized Bitstream for Diffusion Compression | 方法 / method | 免训练的错误定域定宽字段（BLA）+ 把损坏原子转为擦除的可靠性门（RADC）：BER 1e-4~1e-2 下省 26.7% 比特胜鲁棒基线 \| Training-free error-localizing fields (BLA) + reliability gates turning corrupted atoms into erasures (RADC): beats Robust Turbo-DDCM with 26.7% fewer bits at BER 1e-4–1e-2 |
| 8 | [[2610.29183]] 星载中断下的视觉语言推理恢复 · Resuming VLM Inference across Interruptions | 系统 / system | 相位感知检查点 + 依赖感知动态恢复（<100ms 恢复规划器）：卫星载荷硬件端到端 4.07× 提速、SSD 写入降 3.56×，双星 72 小时部署 \| Phase-aware checkpointing + dependency-aware recovery (<100ms planner): 4.07× end-to-end and 3.56× fewer SSD writes on satellite payload hardware; 72-hour two-satellite deployment |
| 9 | [[2610.30397]] DRAM 地址映射逆向的验证式阈值扫描 · Verified DRAM Address Mapping | 方法 / method | 阈值扫描式 Knock-Knock 求解器 + GF(2) RREF 与分组/单函数验证级：ARM 嵌入式 LPDDR5 平台逐阈值验证记录 \| A threshold-sweep solver + GF(2) RREF with group and single-function verification stages, instantiated on ARM-based embedded LPDDR5 with per-threshold validation records |
| 10 | [[2610.26724]] 生成式深度学习注入空间辐射错误 · Injecting Space Radiation Errors on NVM | 分析 / analysis | 立方星 FRAM 快照训练的生成式错误模式模型：生成翻转 0.92 命中观测，Wasserstein 0.073（10,000 模式） \| A generative error-pattern model trained on CubeSat FRAM snapshots: 0.92 of generated flips match observations, Wasserstein 0.073 over 10,000 patterns |

### 5. 智能体与流水线静默失效 / Agent & Pipeline Silent Failures（5 篇 / 5 papers）

| # | 论文 / Paper | 类型 / Type | 入选理由 / Why it matters |
|---|---|---|---|
| 1 | [[2610.32110]] 谁来验证工具？扭曲的格式化器 · Who Verifies the Tools? | 分析 / analysis | 两个格式化器版本喂给智能体/验证器：3/4 失败类型上无据声明下降，验证器 90/90 由接受翻转为拒绝；审计发现 OpenClaw/Hermes 中的扭曲格式化器，PR 已合并 \| Two formatter versions fed to agents/verifiers: unsupported claims drop on 3/4 failure types and verifiers flip 90/90 accept→reject; audit found warped formatters in OpenClaw/Hermes, PR merged |
| 2 | [[2610.25947]] 声明洗钱：信记录不信现实 · Claim Laundering | 分析 / analysis | 智能体在"声称但失败"步骤后相信日志而非观察：配对反事实 + 线性探针（AUROC 0.77–1.00）+ EVIGATE 中间层否决；12 配置 53–100% 错误继续，ALFWorld +18.7pp \| Agents trust logged records over observations after claimed-but-failed steps: paired counterfactuals + probes (AUROC 0.77–1.00) + EVIGATE veto; 53–100% wrongful continuation, +18.7 pp ALFWorld |
| 3 | [[2610.30026]] 作者写的 vs 智能体读到的 · Silent Cue Loss in Document Ingestion | 分析 / analysis | OOXML 属性真值 + 确定性匹配的 76 份政策文档任务：恢复作者标记要求 micro F1 0.690→0.150(docling)/0.075(纯文本)；高亮 +0.302、颜色 +0.262 \| OOXML-property ground truth + deterministic scoring on 76 policy docs: requirement recovery falls 0.690→0.150 (docling) / 0.075 (plain text); highlight +0.302 and colour +0.262 by leave-one-out |
| 4 | [[2610.27777]] RITE：电商智能体对静默工具错误的韧性 · Resilience to Silent Tool Errors | 基准 / benchmark | RITE（167 匹配单元 / 9 工作流 / 501 实例 / 10 个 LLM）：静默工具错误使任务成功率约减半，且始终难于显式失败 \| RITE (167 matched units / 9 workflows / 501 instances / 10 LLMs): silent tool errors roughly halve task success and are consistently harder than explicit failures |
| 5 | [[2610.26632]] harness 决定成败：不可再观测的状态 · When the Harness Decides Success | 分析 / analysis | 预注册合成探针（92.5pp 对比）+ ARC-AGI-3 harness 差距分解：截断/摘要/重放在状态不可再观测时决定成败，摘要恢复 63 分差距的 86% \| Pre-registered synthetic probe (92.5 pp contrast) + ARC-AGI-3 harness-gap decomposition: truncation/summarization/replay decide success when state cannot be re-observed; summarization recovers 86% of a 63-point gap |

### 6. 极限性能优化下的可靠性 / Reliability under Extreme Performance Optimization（20 篇 / 20 papers）

| # | 论文 / Paper | 类型 / Type | 入选理由 / Why it matters |
|---|---|---|---|
| 1 | [[2610.31642]] Softmax 与交叉熵的修复 · A Fix for Softmax and Cross-Entropy | 方法 / method | 修复所有主流框架 softmax/交叉熵的浮点 bug（精度悬崖处目标 logit 梯度归零）：grokking 99–100% vs 93–96%，消除 Slingshot 尖峰与蒸馏学生漂移 \| Drop-in softplus/expm1/log1p fixes for the softmax/cross-entropy bugs in every major framework: 99–100% vs 93–96% on grokking, Slingshot spikes eliminated, distillation drift stopped |
| 2 | [[2610.29445]] MXFP4 点积尺度放置的整数判定 · Deciding Scale Placement in MXFP4 | 方法 / method | 整数状态机 + QF_LIA 编码与闭式指数和界：cvc5 秒级判定重排合法性（QF_FP 需 1 CPU 小时），SMT 反例 + MLIR 原型 GPU 回放 \| An integer state machine + QF_LIA encoding with a closed-form exponent-sum bound: cvc5 decides MXFP4 rewrite legality in seconds where QF_FP hits a 1-CPU-hour limit; MLIR prototype with GPU replay |
| 3 | [[2610.27397]] PTQ 校准何时有益何时有害 · When PTQ Calibration Helps or Hurts | 分析 / analysis | 功能位移剂量分析 + 预注册验证门控弃权：3 个嵌入器 161 次校准，NDCG@10 +1.47~−71.53，30 次决策 0 次有害选择 \| Functional-displacement dose analysis + pre-registered validation-gated abstention over 3 embedders and 161 calibration runs (+1.47 to −71.53 NDCG@10); 0 harmful selections in 30 decisions |
| 4 | [[2610.28947]] 2:4 稀疏还值得吗 · Is 2:4 Sparsity Still Worth It? | 分析 / analysis | 等比特 / 等档位、6 个 GEMM 操作数、3 代 GPU 的受控比较：只要还能再降精度，2:4 稀疏就是更差的一步 \| Equal-bits / equal-tier comparison across all 6 GEMM operands on 3 GPU generations: 2:4 sparsity is the worse step while lower precision remains available |
| 5 | [[2610.27913]] ACE-Compression：压缩模型的能力中心评测 · Ability-Centric Evaluation of Compression | 基准 / benchmark | 对 6 个 LLM 的 35+ 压缩检查点做能力中心探测：细粒度与上下文相关能力最脆弱；量化保持优于剪枝 \| Ability-centric probing of 35+ compressed checkpoints from 6 LLMs: fine-grained and context-dependent abilities are fragile; quantization retains better than pruning |
| 6 | [[2610.34545]] VTC-AUDIT：视觉 token 压缩干预式审计 · Interventional Audit for Visual-Token Compression | 分析 / analysis | 3 个开源 VLM × 2 免训练压缩器的四臂配对图像偏移审计（70.8 万记录）：换选触发使失败率 +2.05~9.60pp，全部置信区间高于零 \| A 4-arm paired-image-shift audit on 3 open VLMs × 2 compressors (708k records): reselect-on-shift raises failure 2.05–9.60 pp with every CI above zero |
| 7 | [[2610.27301]] 上下文压缩对"后来的问题"的影响 · Context Compaction on Later Questions | 分析 / analysis | 问题条件选择 vs 随机删除 vs LLMLingua-2（4 语料含 tau-bench 轨迹）：没有方法在"后来的问题"上胜过随机删除 \| Question-conditioned selection vs random deletion vs LLMLingua-2 on 4 corpora incl. recorded tau-bench trajectories: no method beats random on the questions that come later |
| 8 | [[2610.33824]] 累加感知量化拥抱电压缩放误差 · Accumulation-Aware Quantization for Voltage Scaling | 方法 / method | 累加感知训练约束权重分布 + 选择性 MSB 掩蔽 + 逐层 DFS，2nm 后版图流片：−39% 能耗、−23% EDP、精度损失 <1% \| Accumulation-aware training + selective MSB masking + layer-wise DFS on 2nm post-layout silicon: 39% energy and 23% EDP gains with <1% accuracy loss |
| 9 | [[2610.28537]] 超越 4 比特：数据中心 PTQ 与恢复 · Beyond 4 bits: Data-Centric PTQ and Recovery | 分析 / analysis | 向量码本 + 任务对齐校准 + 仅码本恢复：6 个 3.8–32B 稠密/MoE 模型在约 2.3 有效比特保留 89–97% FP 问答精度 \| Vector codebooks + task-aligned calibration + codebook-only recovery: 6 dense/MoE models (3.8–32B) retain 89–97% of FP QA accuracy at ~2.3 effective bits |
| 10 | [[2610.29378]] Right On Q：自生成轨迹恢复量化推理 · Recovering Reasoning under Quantization | 方法 / method | 学生前缀上的在线蒸馏 + 候选级动态 KL：Qwen3-1.7B/4B/8B 在 2-bit 下 9 基准平均最佳、逐基准全胜基线，Qwen3-8B +10.26 分 \| On-policy distillation on student prefixes + candidate-wise Dynamic KL: best 9-benchmark average, beating every baseline on every benchmark at 2-bit, +10.26 pts on Qwen3-8B |
| 11 | [[2610.26827]] KEEP-Bench：上下文压缩中的证据保持 · Evaluating Evidence Preservation in Compression | 基准 / benchmark | KEEP-Bench 4,102 案例（3 种证据结构）+ "证据保持回报"指标：最佳开源模型(31B)全部证据保持率 66.8%，最佳闭源 61.6% \| KEEP-Bench (4,102 cases, 3 evidence-structure settings) + an Evidence Preservation Return metric: best open model (31B) preserves all evidence 66.8%, best proprietary 61.6% |
| 12 | [[2610.32417]] 量化智能体完成任务的能耗 · Energy Cost of Completing Tasks with Quantized Agents | 分析 / analysis | 29 个智能体任务、4/8-bit、A100 + llama.cpp：每 token 省能耗但完成任务能耗反升最多 3.5×（多出的 token） \| 29 agent tasks, 4-bit/8-bit on A100s with llama.cpp: per-token savings do not transfer — up to 3.5× energy per completed task from extra tokens |
| 13 | [[2610.33625]] RAQ-MLA：MLA 缓存的角色感知量化 · Role-Aware Quantization for MLA Caches | 方法 / method | 按缓存张量拟合的角色感知可逆变换：约 2.5 bit/元素、6.5× KV 容量，4 个 MLA 模型上推理/编码近无损 \| Role-aware invertible transforms fitted per cached tensor: ~2.5 bits/element, 6.5× KV capacity, near-lossless reasoning/coding across 4 MLA models |
| 14 | [[2610.28369]] 别跳过基线：MoE 动态专家跳过 · Dynamic Expert Skipping in MoEs | 分析 / analysis | 等算力受控基准（Gemma4-26B-A4B / Qwen3-30B-A3B / Qwen3-VL）：动态专家跳过未胜静态缩减；校准/测试有效 k 背离会误估推理算力 \| A matched-compute benchmark (Gemma4-26B-A4B / Qwen3-30B-A3B / Qwen3-VL): dynamic expert skipping fails to beat static reduction; calibration-vs-test effective-k divergence misestimates inference compute |
| 15 | [[2610.33076]] Apple 芯片上的双重 KV 缓存优化 · Double KV Cache Optimization on Apple Silicon | 分析 / analysis | M5 Max MLX 上 5 条缓存路径：约 3.6× 压缩但 32K 上下文以上坍缩到 1.5–14 tok/s，64K 在 22.6GB Metal 限制下 OOM \| Five cache paths (bf16, block-FP4, radial, composed, fused Metal) on M5 Max MLX: ~3.6× compression but collapse to 1.5–14 tok/s above 32K context and 64K OOM past the 22.6GB Metal limit |
| 16 | [[2610.31412]] SQuAT：球面格向量量化感知训练 · Spherical Lattice Vector Quantization-Aware Training | 方法 / method | 形状增益 E8 球面码本 + 分离 STE 的量化感知训练：LLaMA-3.2 / Qwen3 小模型 10B token 上胜标准 VQ-QAT \| Shape-gain E8 spherical codebook with separate STEs: beats standard VQ-QAT STE under identical quantizers on LLaMA-3.2-1B/3B and Qwen3-1.7B/4B at 10B tokens |
| 17 | [[2610.31098]] RIFT：草稿模型的互补可压缩性训练 · KV Compression for Draft Models | 方法 / method | 选择刷新 + 自适应刷新 + 可压缩性训练：Qwen3.5-4B 起草 Qwen3.5-122B 在 8K 缓存预算下保持 >98% 全缓存接受长度 \| Selection refresh + adaptive refresh + compressibility training: Qwen3.5-4B drafting Qwen3.5-122B retains >98% full-cache acceptance at 32K-in/4K-out with an 8K cache budget |
| 18 | [[2610.25675]] LIRQuant：局部孤立旋转量化 · Locally Isolated Rotation Quantization | 方法 / method | 敏感通道可学习、其余固定的局部孤立旋转：LLaMA-2/3、Mistral、Qwen3、Mixtral 上 W4A4KV4 SOTA 精度、25 分钟校准 \| Sensitivity-aware locally isolated rotations (learnable on sensitive channels, fixed elsewhere): SOTA W4A4KV4 accuracy on LLaMA-2/3, Mistral, Qwen3, Mixtral with 25-min calibration |
| 19 | [[2610.31433]] 漂移定时机、预算定量级 · Rate-Controlled KV Re-selection | 方法 / method | 漂移触发、速率受控的 KV 再选择：六个模型–任务设置中五个胜 InfiniGen 1.6–3.8 ROUGE-L（天花板 0.44–0.52） \| Drift-triggered rate-controlled re-selection beats InfiniGen by 1.6–3.8 ROUGE-L on five of six model-task settings (oracle ceiling 0.44–0.52) |
| 20 | [[2610.25933]] KV-Surgeon：补偿感知的离线 KV 压实 · Compensation-Aware Offline KV Compaction | 方法 / method | 对剩余条目内补偿 + 联合最优贪心移除的二次代理：QuALITY/LongHealth/Long Code Arena 4B–30B 上 50× 压缩 +4pp 胜注意力匹配 SOTA \| A quadratic surrogate for jointly optimal greedy removal with compensation inside remaining entries: +4 pp at 50× compression over attention-matching SOTA on QuALITY/LongHealth/Long Code Arena, 4B–30B |

### 7. LLM 隐状态与可解释性 / LLM Hidden States & Interpretability（25 篇 / 25 papers）

| # | 论文 / Paper | 类型 / Type | 入选理由 / Why it matters |
|---|---|---|---|
| 1 | [[2610.25596]] LLM 中的认知地图 · Cognitive Maps in Large Language Models | 分析 / analysis | 因果"马赛克"拼接干预 + 位置编码对照，11 模型 / 14 关系任务：约 1% 稀疏键值对完成身份绑定，编辑约 35 个值可植入单向假记忆 \| Causal mosaic splicing interventions with position-code controls across 11 models / 14 relational tasks: ~1% sparse KV pairs bind identity, and editing ~35 values implants unidirectional false memories |
| 2 | [[2610.29340]] Transformer MLP 的读者–写者耦合 · Reader–Writer Coupling in Transformer MLPs | 分析 / analysis | 方块雅可比及其转置定义的带符号配对坐标：对立通道核从最小模型复现到发布检查点，写者翻转/置换干预验证 \| A signed pairing coordinate from the block Jacobian and its transpose: the opposed-channel core recurs from the smallest models to released checkpoints, verified by writer-flip/permute interventions |
| 3 | [[2610.28498]] 存在但难读：最小对探测潜在推理 · Present but Hard to Read | 分析 / analysis | 最小对数字探针 + 合成零假设协议：Ouro/Qwen2.5 上共享码读出 0.9 vs 单提示 0.36/0.19——探针失败不等于信息不存在 \| Minimal-pair digit probes + a synthetic-null protocol on Ouro-1.4B/Qwen2.5-1.5B: shared-code readout 0.9 vs 0.36/0.19 single-prompt — a failed probe does not mean the value is absent |
| 4 | [[2610.27580]] 扩散语言模型的事实访问状态 · Factual Access States in Diffusion LMs | 分析 / analysis | 掩码扩散语言模型中事实的键取与检索机制 + Multi-View Edit：改写/反向 QA 提升而自回归编辑器近零增益 \| How facts are keyed and retrieved in masked diffusion LMs + Multi-View Edit, improving paraphrase/reverse QA where AR editors gain near zero |
| 5 | [[2610.31943]] 一致性而非归一化维持循环深度复用 · Agreement Keeps Depth Reusable in Looped LMs | 分析 / analysis | 移除归一化使 Ouro 循环模型精度归零，状态归一化恢复到 2.021× 以内；19M 参数 16 种子研究定位损伤于读出与末层 \| Removing normalisation drops looped Ouro accuracy to zero; state norm restores within 2.021× — 19M-param 16-seed studies localize damage to readout + last block layer |
| 6 | [[2610.30727]] 忠实潜在危害监视器并不更好 · Faithful Latent Harm Monitors | 分析 / analysis | 38 个激活读出器 × 15 个指令模型在改写/劝导/越狱偏移下：TF-IDF 比潜在监视器更会排危害，生成前增益跟随拒答决定本身 \| 38 activation readers on 15 instruction-tuned LLMs under rewording/persuasive/jailbreak shifts: TF-IDF ranks harm better than Latent Guard in every model; pre-generation gain follows the refusal decision |
| 7 | [[2610.32411]] MLLM 检索头的更广视角 · A Broader Look into MLLM's Retrieval Heads | 分析 / analysis | 18 个检查点的配对语音/展示输入：共享检索头 <2%，但消融即消灭音视频检索并损害文档/空间/数学；头训练 +6.03 Recall@1 \| Paired spoken/shown inputs across 18 checkpoints: shared heads <2% but ablating them eliminates audio-visual retrieval; head training +6.03 Recall@1 on MMDocIR |
| 8 | [[2610.32866]] TopKLoRA 可解释稀疏微调与电路发现 · Interpretable Sparse Fine-Tuning | 方法 / method | TopKLoRA 稀疏适配器在投毒模型上给出必要 + 充分电路：比稠密 LoRA 小约 10×，手术式消融保留指令跟随 \| TopKLoRA sparse adapters yield necessary+sufficient circuits in poisoned gemma-2/Qwen2.5 models: ~10× smaller than dense LoRA, surgical ablation preserves instruction-following |
| 9 | [[2610.30903]] 同一分子、不同知识 · Cross-Identifier Binding Failures in Chemistry | 分析 / analysis | 同一分子的不同标识符暴露不同知识子集：7B–72B 上行为/表征/因果（含参数编辑）分析 + Binding Self-Distillation 直取 SMILES \| Co-referring molecular identifiers expose different knowledge subsets: behavioral/representational/causal analyses incl. parameter editing across 7B–72B; Binding Self-Distillation retrieves SMILES directly |
| 10 | [[2610.30678]] 安全探针的缩放律 · Scaling Laws for Safety Probes | 分析 / analysis | 两条缩放律（模型规模幂律误差底、标签数衰减），20 个基座 / 2 架构 / 32~1e6 标签：72% 情况下一尺寸误差预测在 0.02 内 \| Two scaling laws (power-law error floor in model size, label-count decay) over 20 base models / 2 architectures / 32–1e6 labels: predicts next-size error within 0.02 in 72% of cases |
| 11 | [[2610.27393]] 少量精确测量修正归因修补 · Correcting Attribution Patching | 方法 / method | 利用共享误差结构的少量精确测量做带符号修正：平均效应误差 −75~−79%，单提示 −26%（最大估计验证算力下） \| Few exact measurements exploiting shared error structure for sign-aware correction: −75 to −79% error on average effects, −26% single-prompt at verify-largest-estimate compute |
| 12 | [[2610.25846]] 置信度信号的测量效度 · Confidence Signals in LLMs | 分析 / analysis | 预注册审计 5 个 Qwen2.5 模型的三条置信通道（言语化/探针/采样一致性）：2/5 假设被证伪，ECE 误导，分辨率最 favor 采样一致性 \| A pre-registered audit of verbalized/probe/sampling confidence channels on 5 Qwen2.5 models: 2/5 hypotheses falsified, ECE misleading, resolution favors sampling agreement |
| 13 | [[2610.27724]] 语言模型如何组织任务信息 · How Language Models Organize Task Information | 分析 / analysis | 19 个 LM / 14 任务的 k* 最小特征读出指标：指令微调选择性降低 k*，标签需求随 (k*)^0.65 缩放 \| A k* minimal-feature readout metric across 19 LMs / 14 tasks: instruction tuning selectively lowers k*; label requirement scales as (k*)^0.65 across 8 students |
| 14 | [[2610.25728]] 无论你是谁：指向性与谄媚 · Addressivity and Sycophancy in LLMs | 分析 / analysis | SAE 提取的"指向性"方向可放大/抑制谄媚：预训练 vs 后训练对照 + 受控后训练实验 \| SAE-extracted addressivity directions amplified or suppressed; pre- vs post-trained contrasts plus a controlled post-training experiment on sycophancy |
| 15 | [[2610.32281]] "不"没有在翻译中丢失 · Negation Representations in Multilingual LLMs | 分析 / analysis | 因果激活方向 + 每模型单个 SAE 特征控制极性：六个模型、4+4 种语言，否定表征跨语言共享 \| Causal activation directions + a single SAE feature per model controlling polarity: negation representations shared across languages in six models |
| 16 | [[2610.30363]] 安全相关行为的探测与转向 · Probing and Steering for Safety Behaviours | 分析 / analysis | 探针估计器 × 池化 × 层选择在欺骗/高风险意识/谄媚上的读写分离：谄媚上方向反转，检测与转向最优层不同 \| Probe estimator × pooling × layer choices on deception/high-stakes awareness/sycophancy: the read/write dissociation reverses for sycophancy; the best layer differs for detect vs steer |
| 17 | [[2610.25724]] 走进评分器：量规控制机制 · Rubric Control in LLM Essay Scoring | 分析 / analysis | 25 个开源基座（0.13–10.31B、14 家族）上量规方向不可独立控制：匹配干预仅胜不匹配约 2% \| Rubric directions are not independently controllable across 25 open-weight base LLMs (0.13B–10.31B, 14 families): matching beats mismatched interventions by only ~2% |
| 18 | [[2610.32109]] 上下文还是知识 · How LLMs Attribute Their Own Answers | 分析 / analysis | KV 缓存交换/移植 + 拟合转向方向：四个 7B–32B 模型 98.9–100% 翻转来源报告（范数匹配随机方向 ≤1.1%） \| KV-cache swaps/transplants + fitted steering directions: 98.9–100% report reversal on four 7B–32B models (≤1.1% for norm-matched random directions) |
| 19 | [[2610.31407]] 同一实体、不同文字 · Cross-Script Entity Matching Failures | 分析 / analysis | 601 对天城文/拉丁转写实体：Qwen2.5-7B 35.1%→8.5%；校准恢复 87% 差距，激活修补定位中层，干预 6.5%→33.5% \| 601 audited Devanagari/Latin pairs (Qwen2.5-7B 35.1%→8.5%) + 374 Malayalam replication: calibration recovers 87% of the gap, patching localizes middle layers, intervention 6.5%→33.5% |
| 20 | [[2610.32309]] 多种扰动、共享失效动力学 · Shared Failure Dynamics under Perturbations | 分析 / analysis | 纵向–横向分解 + 储备–传输模型解释任务保持改写为何翻转答案；Qwen3-32B / Gemma 4 31B 留出预测与匹配干预 \| A longitudinal-transverse decomposition + reserve-and-transmission model of why task-preserving rewrites flip answers; held-out prediction and matched interventions on Qwen3-32B / Gemma 4 31B |
| 21 | [[2610.25599]] 副语言冲突中的文本支配 · Text Dominance in Audio LLM Circuits | 分析 / analysis | 探针 + 反向修补复现 + 注意力敲除：6 个音频 LLM 上文本支配度 0.78，n=300 复现 \| Probing + back-patching replication + attention knockout: text-dominance 0.78 across 6 audio LLMs under LISTEN conflict items, n=300 replication |
| 22 | [[2610.27577]] 静态探针为何失败 · Context Determines Deception Feature Composition | 方法 / method | 迭代正交分解的多维子空间 + 域自适应门控：AUROC 0.97，5% FPR 下 94% 召回 \| A multi-dimensional subspace via iterative orthogonal decomposition + domain-adaptive gating: AUROC 0.97, 94% recall at 5% FPR |
| 23 | [[2610.27711]] 微调目标与幻觉检测的层级信息 · Layer-Wise Information in Hallucination Detection | 分析 / analysis | cls vs s2s 表征分析 + InfoWindow：截掉 31% 层精度仍在种子噪声内（Qwen3-4B/8B，迁移 Llama/Mistral） \| cls vs s2s representation analysis + InfoWindow: truncating 31% of layers keeps accuracy within seed noise on Qwen3-4B/8B, transferring to Llama-3.2-3B / Mistral-7B |
| 24 | [[2610.32113]] REACT：思维链的表征早期分析与控制 · Representational Early Analysis of CoT | 方法 / method | 早期 CoT 位置单次条件激活编辑：三个蒸馏推理模型 StrongREJECT-273 完全安全 29.06%→82.05%，可用性近基线 \| A single conditional activation edit at early CoT positions: StrongREJECT-273 fully-safe 29.06%→82.05% across three distilled reasoning models with usefulness near baseline |
| 25 | [[2610.27241]] 无需关系预测线性关系可解码性 · Predicting Linear Relational Decodability | 分析 / analysis | 关系无关的"实体透镜"预测 LRE 忠实性（Olmo-3-7B 28 关系 ρ=0.7355），并标记弱首 token 与参照竞争数据集问题 \| A relation-agnostic entity lens predicts LRE faithfulness at rho=0.7355 on Olmo-3-7B (28 relations) and flags weak-first-token and reference-competition dataset problems |

### 8. 大规模机器学习算力基础设施 / Compute Infrastructure for Large-Scale ML（10 篇 / 10 papers）

| # | 论文 / Paper | 类型 / Type | 入选理由 / Why it matters |
|---|---|---|---|
| 1 | [[2610.32057]] HyScale：长上下文稀疏注意力训练 · Scaling Long-Context Training for Learned Sparse Attention | 系统 / system | HyTopK 免 score-table 精确 top-k + selection 重放：512 张 H20 上 GLM-5.1 1M token 训练较 Megatron-LM 提速 2.07×；CSA/QSA 层 2.01×/1.57× \| HyTopK (exact, score-table-free top-k) + selection replay: GLM-5.1 1M-token training 2.07× over Megatron-LM on 512 H20 GPUs; CSA/QSA layers 2.01×/1.57× on 32 H800 |
| 2 | [[2610.31911]] LazyFlash：前向稠密、反向稀疏 · Forward-Dense, Backward-Sparse Attention | 系统 / system | FlashAttention 反向内核内的梯度感知块稀疏化：注意力反向最高 5.7×、端到端训练 1.7× 提速，下游性能保持 \| Gradient-aware block sparsification inside the FlashAttention backward kernel: up to 5.7× attention-backward and 1.7× end-to-end training speedup with downstream performance maintained |
| 3 | [[2610.26131]] GPU + 存内处理混合架构 · Hybrid GPU–PNM Prefill-Decode Disaggregation | 系统 / system | HBM 逻辑 die 内 PNM 单元共享 DRAM 带宽全解码执行：服务器级 LLM 端到端吞吐最高 2.23× 于常规 PD 分离 \| PNM units in the HBM logic die execute full decode over shared DRAM bandwidth: up to 2.23× end-to-end throughput over conventional PD-disaggregation at server scale |
| 4 | [[2610.29873]] HAWK：GPU–NPU 异构 KV 传输 · Heterogeneity-Aware KV Cache Transfer | 系统 / system | NPU 侧布局感知 RDMA 缓冲 + 免重排跨设备传输：同 SLO 下距纯 GPU 系统 7.88% 以内，能效 1.26×、成本效率 1.72× \| Layout-aware RDMA buffers on the NPU side + direct cross-device transfer without rearrangement: within 7.88% of a GPU-only system at the same SLOs; 1.26× power and 1.72× cost efficiency |
| 5 | [[2610.28998]] FlashNext-RL：长程智能体 RL 系统优化 · A System Study for Long-Horizon Agentic RL | 系统 / system | 主机卸载 + 梯度累加 + MoE/稀疏注意力/门控残差内核调优（8×B200）：395→4,438 tokens/s/GPU，带熵与 KL 约束的真实 SWE RL 运行 \| Host offload + gradient accumulation + MoE/sparse-attention/gated-residual kernel tuning on 8×B200: 395→4,438 tokens/s/GPU, live SWE RL run with bounded entropy and KL |
| 6 | [[2610.33501]] DualPace：解耦调度与 GPU–CPU 协同解码 · Decoupled Scheduling and Cooperative Decoding | 系统 / system | 双引擎解耦调度 + AMX CPU 解码与 GPU 稠密协助：同延迟下较 NEO +6.9–43.2%、较 vLLM +11.5–90.6%，P99 ITL 下请求率 +7.3–50.5% \| A dual-engine decoupled scheduler with AMX CPU decode and GPU dense assist: +6.9–43.2% vs NEO, +11.5–90.6% vs vLLM at equal latency; 7.3–50.5% higher request rates at P99 ITL |
| 7 | [[2610.34440]] MoE 推测解码 · Expert Bytes, Kernel Bandwidth, Best Draft Length | 分析 / analysis | "字节 / 有效带宽"步时模型（Lean 检查）：去重仅在每轮 5–8 token 时更快，10/12 配置预测误差在一次 pass 内 \| A bytes-over-effective-bandwidth step-time model (Lean-checked): dedup is faster only at 5–8 tokens/pass on llama.cpp/MLX/CUDA; predictions within one pass size in 10/12 configs |
| 8 | [[2610.26991]] 3D-MoE：3D 堆叠 NMP 软硬件协同设计 · Complementarity-Guided Co-Design for MoE Decode | 系统 / system | 互补性引导分组 + 协作存内网络权重流送 + 在线重映射：MoE 层较 EP 4.63×，端到端较 NMP 基线 1.58–1.86× \| Complementarity-guided grouping + collaborative memory-network weight streaming + online remapping: 4.63× MoE-layer over EP, 1.58–1.86× end-to-end over NMP baselines |
| 9 | [[2610.33719]] ZipFusion：解压与注意力融合 · Fusing Lossless KV Decompression with Attention | 系统 / system | 解压与注意力在寄存器内融合（基于 FlashInfer/SGLang）：H100 解码注意力 1.25× 于 FlashInfer，较最佳无损基线吞吐最高 2.76× \| An attention kernel consuming the compressed KV directly in registers (FlashInfer/SGLang): 1.25× decode attention over FlashInfer on H100, up to 2.76× throughput vs the best lossless baseline |
| 10 | [[2610.31479]] Apple 芯片上推理优化的适用性 · Applicability of LLM Inference Optimizations on Apple Silicon | 分析 / analysis | 四族优化（KV 剪枝/推测解码/移植内核/PTQ）× 四台 Apple 设备 + 匹配 RTX 4090：推测解码在 Apple 上反而降吞吐 \| Four optimization families on four Apple machines with matched RTX 4090 comparisons: speculative decoding cuts throughput on Apple despite 2–6× reported server gains |

### 9. 模型系统卡与技术报告 / Model System Cards & Technical Reports（3 篇 / 3 papers）

> 本周该领域配额为 5，但通过门控的仅 3 篇报告，未用满的名额不回收；且 3 篇经全文精读均未获星标（`star: false`）。
> The area quota was 5, but only 3 reports passed the gate; unused slots were not redistributed — and none of the 3 earned a star after full reads (`star: false`).

| # | 论文 / Paper | 类型 / Type | 入选理由 / Why it matters |
|---|---|---|---|
| 1 | [[2610.31945]] Kolibri：帕累托前沿的欧洲主权模型 · A Sovereign European Model | 报告 / report | Aleph Alpha 开源 78.1B/3.46B 激活英德 MoE（24T token、>20% 德语、1.2M 任务 RL 后训练）：质量—服务成本帕累托前沿，AIME 2026 96.0 \| Aleph Alpha's open 78.1B/3.46B-active EN-DE MoE (24T tokens, >20% German, SFT+RL over 1.2M tasks): on the quality-vs-serving-cost Pareto frontier among open models, AIME 2026 96.0 |
| 2 | [[2610.30949]] IQuest-Q1：智能体 CLI 基座 · Advancing Foundation Capabilities for Agentic CLI | 报告 / report | 320B-A15B 稀疏 MoE 技术报告：SplitNorm + Muon + muP 预训练（安全/最优学习率间宽稳定裕度）、细粒度中期训练、多脚手架多版本后训练 + 模型合并；开源发布 \| A 320B-A15B sparse MoE report: Stable SplitNorm + Muon + muP pretraining with a wide stability margin between safe and optimal LRs, fine-grained mid-training, multi-scaffold multi-version post-training with merging; open-source release |
| 3 | [[2610.28578]] Sage-A1.5：从长程执行到科学探索 · From Long-Horizon Execution to Scientific Exploration | 报告 / report | Sage-A1.5 35B MoE 报告：编排、验证与开放科学发现的能力组合，智能体与科学任务展示（摘要无外部基线数字） \| Sage-A1.5 35B MoE report on orchestration, verification, and open scientific discovery via capability composition; showcases on agentic and scientific tasks (no external baselines in the abstract) |

---

## All Papers

> 全部 102 篇入选论文完整索引（与 `filtered_papers.json` 的 `total_selected` 一致）。
> Complete index of all 102 selected papers (matches `total_selected` in `filtered_papers.json`).

| # | 论文 / Paper | 领域 / Area | 类型 / Type |
|---|---|---|---|
| 1 | [[2610.27465]] 无人自我改进的两个前提 · Recoverability and Verifier Strength | 自进化智能体与自动化研究 / Self-Evolving Agents & Automated Research | 分析 / analysis |
| 2 | [[2610.30557]] 自主投资的自进化治理 · Governed Self-Evolution for Autonomous Investing | 自进化智能体与自动化研究 / Self-Evolving Agents & Automated Research | 系统 / system |
| 3 | [[2610.25858]] 自进化智能体是持续学习器吗 · Are Self-Evolving Agents Continual Learners? | 自进化智能体与自动化研究 / Self-Evolving Agents & Automated Research | 分析 / analysis |
| 4 | [[2610.27735]] RSI Control：自我改进中的隐蔽破坏 · Covert Sabotage in Self-Improvement | 自进化智能体与自动化研究 / Self-Evolving Agents & Automated Research | 基准 / benchmark |
| 5 | [[2610.31372]] RIDAR：自主研究的诚信守护 · Safeguarding Research Integrity | 自进化智能体与自动化研究 / Self-Evolving Agents & Automated Research | 方法 / method |
| 6 | [[2610.29005]] VeriEvolve：评估器优先进化 · Evaluator-First Evolution | 自进化智能体与自动化研究 / Self-Evolving Agents & Automated Research | 方法 / method |
| 7 | [[2610.33845]] 只造不玩：炉石酒馆战棋 AI · Build, Don't Play: Hearthstone Battlegrounds AI | 自进化智能体与自动化研究 / Self-Evolving Agents & Automated Research | 系统 / system |
| 8 | [[2610.28763]] Agent4Sci：科学爬坡评测 · Can Frontier Agents Climb Scientific Hills? | 自进化智能体与自动化研究 / Self-Evolving Agents & Automated Research | 基准 / benchmark |
| 9 | [[2610.28887]] 线性注意力自主发现团队 · AI Research Teams for Linear Attention | 自进化智能体与自动化研究 / Self-Evolving Agents & Automated Research | 系统 / system |
| 10 | [[2610.33624]] RSI Arena：人类反馈递归自我改进 · Recursive Self-Improvement with Human Feedback | 自进化智能体与自动化研究 / Self-Evolving Agents & Automated Research | 基准 / benchmark |
| 11 | [[2610.30468]] SplatLab：3DGS 自主科研 · Autonomous Discovery for 3DGS Research | 自进化智能体与自动化研究 / Self-Evolving Agents & Automated Research | 系统 / system |
| 12 | [[2610.30499]] LLM 能改进自己的 harness 吗 · Can LLMs Improve Their Own Harness? | 自进化智能体与自动化研究 / Self-Evolving Agents & Automated Research | 分析 / analysis |
| 13 | [[2610.32229]] MXFP4 训练 MoE：闭环与 BF16 差距 · Training an MoE LLM in MXFP4 | LLM 训练稳定性与可观测性 / LLM Training Stability & Observability | 方法 / method |
| 14 | [[2610.32142]] 重思 LoRA 初始化 · Rethinking LoRA Initialization | LLM 训练稳定性与可观测性 / LLM Training Stability & Observability | 方法 / method |
| 15 | [[2610.27321]] 稳定性边缘之外的物理优化器 · Physics-Inspired Optimizers beyond the Edge of Stability | LLM 训练稳定性与可观测性 / LLM Training Stability & Observability | 分析 / analysis |
| 16 | [[2610.28107]] 仿射重尾下的梯度裁剪 · Gradient Clipping under Affine Heavy Tails | LLM 训练稳定性与可观测性 / LLM Training Stability & Observability | 分析 / analysis |
| 17 | [[2610.29355]] GaP-MoE：正交梯度累加与投影 · Explicit Expert Specialization in MoE | LLM 训练稳定性与可观测性 / LLM Training Stability & Observability | 方法 / method |
| 18 | [[2610.34158]] 有限牛顿–舒尔茨迭代 Muon 的末迭稳定性 · Last-Iterate Stationarity of Muon | LLM 训练稳定性与可观测性 / LLM Training Stability & Observability | 分析 / analysis |
| 19 | [[2610.32465]] SOMA：锐度感知正交动量 · Sharpness-aware Orthogonalized Momentum | LLM 训练稳定性与可观测性 / LLM Training Stability & Observability | 方法 / method |
| 20 | [[2610.30280]] Muon 极更新的二次透镜 · A Quadratic Lens on Muon's Polar Update | LLM 训练稳定性与可观测性 / LLM Training Stability & Observability | 分析 / analysis |
| 21 | [[2610.28871]] 循环 Transformer 截断反传丢多少梯度 · Truncated Backprop in Looped Transformers | LLM 训练稳定性与可观测性 / LLM Training Stability & Observability | 分析 / analysis |
| 22 | [[2610.29410]] ECHO：共模偏移驱动词表坍缩 · Vocabulary Collapse in Preference Optimization | RL 后训练动态与失效 / RL Post-Training Dynamics & Failures | 分析 / analysis |
| 23 | [[2610.28707]] SimHack：训练前预测奖励黑客 · Predicting Reward-Hacking Onset before RL | RL 后训练动态与失效 / RL Post-Training Dynamics & Failures | 方法 / method |
| 24 | [[2610.34044]] 采样器失配下熵漂移的符号律 · A Sign Law for Entropy Drift in RLVR | RL 后训练动态与失效 / RL Post-Training Dynamics & Failures | 分析 / analysis |
| 25 | [[2610.25836]] RL 在哪里坏：定向继续预训练修复 · Where RL Breaks | RL 后训练动态与失效 / RL Post-Training Dynamics & Failures | 分析 / analysis |
| 26 | [[2610.29129]] 表征工程缓解现实奖励黑客 · Representation Engineering vs Reward Hacking | RL 后训练动态与失效 / RL Post-Training Dynamics & Failures | 方法 / method |
| 27 | [[2610.26496]] 演化惩罚修复偏好奖励模型 · Evolving Penalties for Preference Reward Models | RL 后训练动态与失效 / RL Post-Training Dynamics & Failures | 方法 / method |
| 28 | [[2610.28586]] 强教师、近视评分者 · Capable Teacher, Myopic Scorer | RL 后训练动态与失效 / RL Post-Training Dynamics & Failures | 方法 / method |
| 29 | [[2610.26551]] 训练出自然阴谋家 · Training Natural Schemers | RL 后训练动态与失效 / RL Post-Training Dynamics & Failures | 分析 / analysis |
| 30 | [[2610.28429]] Racer：符号等价检查猎 GPU kernel bug · Symbolic Equivalence Checking | 推理可靠性与 SDC 检测 / Inference Reliability & SDC Detection | 系统 / system |
| 31 | [[2610.30798]] Rowhammer 放大推理延迟与成本 · Amplifying Latency via Rowhammer | 推理可靠性与 SDC 检测 / Inference Reliability & SDC Detection | 分析 / analysis |
| 32 | [[2610.28872]] LEAN：损失调制权重敏感度分布 · Loss-Engineered Weight-Sensitivity Modulation | 推理可靠性与 SDC 检测 / Inference Reliability & SDC Detection | 方法 / method |
| 33 | [[2610.27621]] 自愈的抗辐照量化网络 · Radiation-Hardened, Fault-Aware Quantized NN | 推理可靠性与 SDC 检测 / Inference Reliability & SDC Detection | 方法 / method |
| 34 | [[2610.28937]] 审计推理时模型偏移下的保形预测 · Auditing Conformal Prediction under Shift | 推理可靠性与 SDC 检测 / Inference Reliability & SDC Detection | 分析 / analysis |
| 35 | [[2610.31954]] RobustNCL：瞬态故障下的神经形态持续学习 · Robust Neuromorphic Continual Learning | 推理可靠性与 SDC 检测 / Inference Reliability & SDC Detection | 方法 / method |
| 36 | [[2610.25682]] BitFlat：错误定域比特流设计 · Error-Localized Bitstream for Diffusion Compression | 推理可靠性与 SDC 检测 / Inference Reliability & SDC Detection | 方法 / method |
| 37 | [[2610.29183]] 星载中断下的视觉语言推理恢复 · Resuming VLM Inference across Interruptions | 推理可靠性与 SDC 检测 / Inference Reliability & SDC Detection | 系统 / system |
| 38 | [[2610.30397]] DRAM 地址映射逆向的验证式阈值扫描 · Verified DRAM Address Mapping | 推理可靠性与 SDC 检测 / Inference Reliability & SDC Detection | 方法 / method |
| 39 | [[2610.26724]] 生成式深度学习注入空间辐射错误 · Injecting Space Radiation Errors on NVM | 推理可靠性与 SDC 检测 / Inference Reliability & SDC Detection | 分析 / analysis |
| 40 | [[2610.32110]] 谁来验证工具？扭曲的格式化器 · Who Verifies the Tools? | 智能体与流水线静默失效 / Agent & Pipeline Silent Failures | 分析 / analysis |
| 41 | [[2610.25947]] 声明洗钱：信记录不信现实 · Claim Laundering | 智能体与流水线静默失效 / Agent & Pipeline Silent Failures | 分析 / analysis |
| 42 | [[2610.30026]] 作者写的 vs 智能体读到的 · Silent Cue Loss in Document Ingestion | 智能体与流水线静默失效 / Agent & Pipeline Silent Failures | 分析 / analysis |
| 43 | [[2610.27777]] RITE：电商智能体对静默工具错误的韧性 · Resilience to Silent Tool Errors | 智能体与流水线静默失效 / Agent & Pipeline Silent Failures | 基准 / benchmark |
| 44 | [[2610.26632]] harness 决定成败：不可再观测的状态 · When the Harness Decides Success | 智能体与流水线静默失效 / Agent & Pipeline Silent Failures | 分析 / analysis |
| 45 | [[2610.31642]] Softmax 与交叉熵的修复 · A Fix for Softmax and Cross-Entropy | 极限性能优化下的可靠性 / Reliability under Extreme Performance Optimization | 方法 / method |
| 46 | [[2610.29445]] MXFP4 点积尺度放置的整数判定 · Deciding Scale Placement in MXFP4 | 极限性能优化下的可靠性 / Reliability under Extreme Performance Optimization | 方法 / method |
| 47 | [[2610.27397]] PTQ 校准何时有益何时有害 · When PTQ Calibration Helps or Hurts | 极限性能优化下的可靠性 / Reliability under Extreme Performance Optimization | 分析 / analysis |
| 48 | [[2610.28947]] 2:4 稀疏还值得吗 · Is 2:4 Sparsity Still Worth It? | 极限性能优化下的可靠性 / Reliability under Extreme Performance Optimization | 分析 / analysis |
| 49 | [[2610.27913]] ACE-Compression：压缩模型的能力中心评测 · Ability-Centric Evaluation of Compression | 极限性能优化下的可靠性 / Reliability under Extreme Performance Optimization | 基准 / benchmark |
| 50 | [[2610.34545]] VTC-AUDIT：视觉 token 压缩干预式审计 · Interventional Audit for Visual-Token Compression | 极限性能优化下的可靠性 / Reliability under Extreme Performance Optimization | 分析 / analysis |
| 51 | [[2610.27301]] 上下文压缩对"后来的问题"的影响 · Context Compaction on Later Questions | 极限性能优化下的可靠性 / Reliability under Extreme Performance Optimization | 分析 / analysis |
| 52 | [[2610.33824]] 累加感知量化拥抱电压缩放误差 · Accumulation-Aware Quantization for Voltage Scaling | 极限性能优化下的可靠性 / Reliability under Extreme Performance Optimization | 方法 / method |
| 53 | [[2610.28537]] 超越 4 比特：数据中心 PTQ 与恢复 · Beyond 4 bits: Data-Centric PTQ and Recovery | 极限性能优化下的可靠性 / Reliability under Extreme Performance Optimization | 分析 / analysis |
| 54 | [[2610.29378]] Right On Q：自生成轨迹恢复量化推理 · Recovering Reasoning under Quantization | 极限性能优化下的可靠性 / Reliability under Extreme Performance Optimization | 方法 / method |
| 55 | [[2610.26827]] KEEP-Bench：上下文压缩中的证据保持 · Evidence Preservation in Compression | 极限性能优化下的可靠性 / Reliability under Extreme Performance Optimization | 基准 / benchmark |
| 56 | [[2610.32417]] 量化智能体完成任务的能耗 · Energy Cost of Quantized Agents | 极限性能优化下的可靠性 / Reliability under Extreme Performance Optimization | 分析 / analysis |
| 57 | [[2610.33625]] RAQ-MLA：MLA 缓存的角色感知量化 · Role-Aware Quantization for MLA Caches | 极限性能优化下的可靠性 / Reliability under Extreme Performance Optimization | 方法 / method |
| 58 | [[2610.28369]] 别跳过基线：MoE 动态专家跳过 · Dynamic Expert Skipping in MoEs | 极限性能优化下的可靠性 / Reliability under Extreme Performance Optimization | 分析 / analysis |
| 59 | [[2610.33076]] Apple 芯片上的双重 KV 缓存优化 · Double KV Cache Optimization on Apple Silicon | 极限性能优化下的可靠性 / Reliability under Extreme Performance Optimization | 分析 / analysis |
| 60 | [[2610.31412]] SQuAT：球面格向量量化感知训练 · Spherical Lattice Vector Quantization-Aware Training | 极限性能优化下的可靠性 / Reliability under Extreme Performance Optimization | 方法 / method |
| 61 | [[2610.31098]] RIFT：草稿模型的互补可压缩性训练 · KV Compression for Draft Models | 极限性能优化下的可靠性 / Reliability under Extreme Performance Optimization | 方法 / method |
| 62 | [[2610.25675]] LIRQuant：局部孤立旋转量化 · Locally Isolated Rotation Quantization | 极限性能优化下的可靠性 / Reliability under Extreme Performance Optimization | 方法 / method |
| 63 | [[2610.31433]] 漂移定时机、预算定量级 · Rate-Controlled KV Re-selection | 极限性能优化下的可靠性 / Reliability under Extreme Performance Optimization | 方法 / method |
| 64 | [[2610.25933]] KV-Surgeon：补偿感知的离线 KV 压实 · Compensation-Aware Offline KV Compaction | 极限性能优化下的可靠性 / Reliability under Extreme Performance Optimization | 方法 / method |
| 65 | [[2610.25596]] LLM 中的认知地图 · Cognitive Maps in Large Language Models | LLM 隐状态与可解释性 / LLM Hidden States & Interpretability | 分析 / analysis |
| 66 | [[2610.29340]] Transformer MLP 的读者–写者耦合 · Reader–Writer Coupling in Transformer MLPs | LLM 隐状态与可解释性 / LLM Hidden States & Interpretability | 分析 / analysis |
| 67 | [[2610.28498]] 存在但难读：最小对探测潜在推理 · Present but Hard to Read | LLM 隐状态与可解释性 / LLM Hidden States & Interpretability | 分析 / analysis |
| 68 | [[2610.27580]] 扩散语言模型的事实访问状态 · Factual Access States in Diffusion LMs | LLM 隐状态与可解释性 / LLM Hidden States & Interpretability | 分析 / analysis |
| 69 | [[2610.31943]] 一致性而非归一化维持循环深度复用 · Agreement Keeps Depth Reusable in Looped LMs | LLM 隐状态与可解释性 / LLM Hidden States & Interpretability | 分析 / analysis |
| 70 | [[2610.30727]] 忠实潜在危害监视器并不更好 · Faithful Latent Harm Monitors | LLM 隐状态与可解释性 / LLM Hidden States & Interpretability | 分析 / analysis |
| 71 | [[2610.32411]] MLLM 检索头的更广视角 · A Broader Look into MLLM's Retrieval Heads | LLM 隐状态与可解释性 / LLM Hidden States & Interpretability | 分析 / analysis |
| 72 | [[2610.32866]] TopKLoRA 可解释稀疏微调与电路发现 · Interpretable Sparse Fine-Tuning | LLM 隐状态与可解释性 / LLM Hidden States & Interpretability | 方法 / method |
| 73 | [[2610.30903]] 同一分子、不同知识 · Cross-Identifier Binding Failures in Chemistry | LLM 隐状态与可解释性 / LLM Hidden States & Interpretability | 分析 / analysis |
| 74 | [[2610.30678]] 安全探针的缩放律 · Scaling Laws for Safety Probes | LLM 隐状态与可解释性 / LLM Hidden States & Interpretability | 分析 / analysis |
| 75 | [[2610.27393]] 少量精确测量修正归因修补 · Correcting Attribution Patching | LLM 隐状态与可解释性 / LLM Hidden States & Interpretability | 方法 / method |
| 76 | [[2610.25846]] 置信度信号的测量效度 · Confidence Signals in LLMs | LLM 隐状态与可解释性 / LLM Hidden States & Interpretability | 分析 / analysis |
| 77 | [[2610.27724]] 语言模型如何组织任务信息 · How Language Models Organize Task Information | LLM 隐状态与可解释性 / LLM Hidden States & Interpretability | 分析 / analysis |
| 78 | [[2610.25728]] 无论你是谁：指向性与谄媚 · Addressivity and Sycophancy in LLMs | LLM 隐状态与可解释性 / LLM Hidden States & Interpretability | 分析 / analysis |
| 79 | [[2610.32281]] "不"没有在翻译中丢失 · Negation Representations in Multilingual LLMs | LLM 隐状态与可解释性 / LLM Hidden States & Interpretability | 分析 / analysis |
| 80 | [[2610.30363]] 安全相关行为的探测与转向 · Probing and Steering for Safety Behaviours | LLM 隐状态与可解释性 / LLM Hidden States & Interpretability | 分析 / analysis |
| 81 | [[2610.25724]] 走进评分器：量规控制机制 · Rubric Control in LLM Essay Scoring | LLM 隐状态与可解释性 / LLM Hidden States & Interpretability | 分析 / analysis |
| 82 | [[2610.32109]] 上下文还是知识 · How LLMs Attribute Their Own Answers | LLM 隐状态与可解释性 / LLM Hidden States & Interpretability | 分析 / analysis |
| 83 | [[2610.31407]] 同一实体、不同文字 · Cross-Script Entity Matching Failures | LLM 隐状态与可解释性 / LLM Hidden States & Interpretability | 分析 / analysis |
| 84 | [[2610.32309]] 多种扰动、共享失效动力学 · Shared Failure Dynamics under Perturbations | LLM 隐状态与可解释性 / LLM Hidden States & Interpretability | 分析 / analysis |
| 85 | [[2610.25599]] 副语言冲突中的文本支配 · Text Dominance in Audio LLM Circuits | LLM 隐状态与可解释性 / LLM Hidden States & Interpretability | 分析 / analysis |
| 86 | [[2610.27577]] 静态探针为何失败 · Context Determines Deception Feature Composition | LLM 隐状态与可解释性 / LLM Hidden States & Interpretability | 方法 / method |
| 87 | [[2610.27711]] 微调目标与幻觉检测的层级信息 · Layer-Wise Information in Hallucination Detection | LLM 隐状态与可解释性 / LLM Hidden States & Interpretability | 分析 / analysis |
| 88 | [[2610.32113]] REACT：思维链的表征早期分析与控制 · Representational Early Analysis of CoT | LLM 隐状态与可解释性 / LLM Hidden States & Interpretability | 方法 / method |
| 89 | [[2610.27241]] 无需关系预测线性关系可解码性 · Predicting Linear Relational Decodability | LLM 隐状态与可解释性 / LLM Hidden States & Interpretability | 分析 / analysis |
| 90 | [[2610.32057]] HyScale：长上下文稀疏注意力训练 · Scaling Long-Context Training for Learned Sparse Attention | 大规模机器学习算力基础设施 / Compute Infrastructure for Large-Scale ML | 系统 / system |
| 91 | [[2610.31911]] LazyFlash：前向稠密、反向稀疏 · Forward-Dense, Backward-Sparse Attention | 大规模机器学习算力基础设施 / Compute Infrastructure for Large-Scale ML | 系统 / system |
| 92 | [[2610.26131]] GPU + 存内处理混合架构 · Hybrid GPU–PNM Prefill-Decode Disaggregation | 大规模机器学习算力基础设施 / Compute Infrastructure for Large-Scale ML | 系统 / system |
| 93 | [[2610.29873]] HAWK：GPU–NPU 异构 KV 传输 · Heterogeneity-Aware KV Cache Transfer | 大规模机器学习算力基础设施 / Compute Infrastructure for Large-Scale ML | 系统 / system |
| 94 | [[2610.28998]] FlashNext-RL：长程智能体 RL 系统优化 · A System Study for Long-Horizon Agentic RL | 大规模机器学习算力基础设施 / Compute Infrastructure for Large-Scale ML | 系统 / system |
| 95 | [[2610.33501]] DualPace：解耦调度与 GPU–CPU 协同解码 · Decoupled Scheduling and Cooperative Decoding | 大规模机器学习算力基础设施 / Compute Infrastructure for Large-Scale ML | 系统 / system |
| 96 | [[2610.34440]] MoE 推测解码 · Expert Bytes, Kernel Bandwidth, Best Draft Length | 大规模机器学习算力基础设施 / Compute Infrastructure for Large-Scale ML | 分析 / analysis |
| 97 | [[2610.26991]] 3D-MoE：3D 堆叠 NMP 软硬件协同设计 · Complementarity-Guided Co-Design for MoE Decode | 大规模机器学习算力基础设施 / Compute Infrastructure for Large-Scale ML | 系统 / system |
| 98 | [[2610.33719]] ZipFusion：解压与注意力融合 · Fusing Lossless KV Decompression with Attention | 大规模机器学习算力基础设施 / Compute Infrastructure for Large-Scale ML | 系统 / system |
| 99 | [[2610.31479]] Apple 芯片上推理优化的适用性 · Applicability of LLM Inference Optimizations on Apple Silicon | 大规模机器学习算力基础设施 / Compute Infrastructure for Large-Scale ML | 分析 / analysis |
| 100 | [[2610.31945]] Kolibri：帕累托前沿的欧洲主权模型 · A Sovereign European Model | 模型系统卡与技术报告 / Model System Cards & Technical Reports | 报告 / report |
| 101 | [[2610.30949]] IQuest-Q1：智能体 CLI 基座 · Advancing Foundation Capabilities for Agentic CLI | 模型系统卡与技术报告 / Model System Cards & Technical Reports | 报告 / report |
| 102 | [[2610.28578]] Sage-A1.5：从长程执行到科学探索 · From Long-Horizon Execution to Scientific Exploration | 模型系统卡与技术报告 / Model System Cards & Technical Reports | 报告 / report |

---

## 统计与核对 / Stats & Verification

- 评估 / evaluated: **3,186** · 门控候选 / stage-2 candidates: **709** · 通过门控 / gate-kept: **546** · 入选 / selected: **102**（各领域 12 / 9 / 8 / 10 / 5 / 20 / 25 / 10 / 3；配额 12 / 10 / 8 / 10 / 5 / 20 / 25 / 10 / 5，两个未满领域：LLM 训练稳定性 9/10、模型系统卡 3/5，未用满名额不回收）
- 必读来源 / Must-Read source: `stars.json`（27 个候选全文精读，8 个 `star: true`）——本周必读 8 篇即全部星标论文，无自评加星 / the 8 Must Reads are exactly the starred entries (one per area in 8 of 9 areas); no re-starring was done.
- 核对 / Count check: 上表 All Papers 共 **102** 行，与 `filtered_papers.json` 的 `total_selected: 102` **一致，无差异** / the All Papers table has 102 rows, matching `total_selected` in `filtered_papers.json` — no discrepancy.
