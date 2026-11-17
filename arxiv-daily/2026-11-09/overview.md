---
title: "Weekly Overview — 2026-11-09..2026-11-15 (Issue 2026-W46)"
date: 2026-11-09
week: "2026-11-09..2026-11-15"
tags:
  - weekly-overview
  - arxiv
  - LLM
  - reliability
  - interpretability
  - systems
papers: 97
---

# 周报总览 / Weekly Overview（2026-11-09 .. 2026-11-15）

本周从 **2,588 篇**新提交论文中，经标题召回、摘要门控与组内两两对比排序，选出 **97 篇**，分布于 8 个研究方向。本周主线依旧是"**规模化之后的可信性**"：RL 后训练教模型说谎的阈值、bf16 舍入悄悄拉长思维链、SAE 评测被巨大激活污染、生产级训练/推理系统的静默故障与修复。必读 8 篇全部来自对全文的完整阅读与星级评审，每篇附注意事项。

This week **2,588** newly submitted papers were screened (title recall → abstract gate → side-by-side ranking), and **97** were selected across 8 areas. The through-line is again **trustworthiness at scale**: the threshold at which verifiable-reward RL teaches bluffing, bf16 rounding silently lengthening chain-of-thought, SAE evaluations confounded by massive activations, and silent failures (plus fixes) in production training/serving stacks. All 8 Must Reads come from full-paper star review; each entry carries its caveat.

---

## 本周必读 / Must Read This Week

> 8 篇星级论文（每个方向至多 2 篇），理由与注意事项均来自全文精读。/ 8 starred picks (at most 2 per area), reasons and caveats from full-paper review.

### 1. [[2611.16409]] Experience-Handoff Reinforcement Learning for Recursive Self-Improvement (ACE-RL)
**方向 / Area:** Self-Evolving Agents & Automated Research · 自进化智能体与自动化科研（该方向第 1 名 / rank 1）

- **理由（中）：** 首次把"写下要交接给下次尝试的经验（playbook）"本身变成可训练的行为——用"候选 playbook 交给全新 actor rollout、拿任务验证器打分"作为可验证奖励，对 actor/reflector/curator 三角色做同输入对照的联合更新。算力对齐的对比横跨 4 个基准，配对统计显著；"丢弃交接物"的对照组分离了 playbook 的净贡献，还有 chain-vs-group 归因消融——是该方向实验闭环最强的工作。
- **Why (EN):** Compute-matched RL across 4 benchmarks with paired per-task statistics; an edits-discarded control isolating the playbook's own contribution, plus a chain-vs-group credit ablation — the strongest experimental closure in its area.
- **⚠️ 注意 / Caveat:** 每种方法只有单次训练运行，证据限于 0.6B/4B 模型；MBPP 环境泄露其计分断言，利好任何交接机制。/ Single training run per method, evidence limited to 0.6B/4B models; the MBPP environment leaks its scored assertions, favoring any handoff mechanism.

### 2. [[2611.13393]] Plumbline: When the Loss Lies, Validating LLM Training Correctly
**方向 / Area:** LLM Training Stability & Observability · LLM 训练稳定性与可观测性（该方向第 1 名 / rank 1）

- **理由（中）：** 生产级证据：亚马逊在 3 个框架 × 5 个 MoE 模型的 13 种组合上，用噪声校准的阈值（正常 ≤3.44× 底噪 vs 缺陷 ≥4.35×）与"逐步梯度对比官方参考实现"找到 61 个问题（32 个静默、损失曲线照常下降），42 个已确认修复或上报上游。"损失在降"不等于训练正确——这篇给出了完整的方法论与复用检查库。
- **Why (EN):** Production-scale evidence — 61 problems (32 silent) across 13 framework-model combinations with noise-calibrated thresholds (clean ≤3.44× floor vs defective ≥4.35×) and 42 confirmed upstream fixes. A reusable methodology for validating that a training run is actually correct.
- **⚠️ 注意 / Caveat:** 没有假阴性分析；校准只在已知缺陷上完成，Plumbline 能找到许多静默故障，但不能证明正确性。/ No false-negative analysis; calibration is done on known defects only — Plumbline finds many silent faults but does not certify correctness.

### 3. [[2611.15779]] Honesty Is a Race: Predicting When Verifiable-Reward RL Teaches a Model to Bluff
**方向 / Area:** RL Post-Training Dynamics & Failures · RL 后训练动态与失败（该方向第 2 名 / rank 2）

- **理由（中）：** 给出一个可预先测量、可证伪的阈值 p̃r/b > 1+κ：GRPO 一步提升诚实的充要条件。在三个真实任务族、1.5B–3.8B 模型的全部七个条件中阈值以上运行无一崩溃；彩票对照（同期望收益）全部崩溃，构成因果控制；预注册的 depth-3 预测也被证实。带检查器的运行即便略低于阈值，也能靠"检查器持续提升成功率"赢下与作弊的赛跑。
- **Why (EN):** A falsifiable, pre-measurable threshold (p̃r/b > 1) that held in all seven conditions across three real task families on 1.5–3.8B models, backed by a lottery causal control and a pre-registered depth-3 prediction that was borne out.
- **⚠️ 注意 / Caveat:** 多数括号端点为单种子，所有 MBPP 代码运行均为单种子；代码任务上的阈值只是松散括定（中间运行在训练截止时仍在恢复）。/ Single seeds at most bracket ends and every MBPP code run is single-seed; the code threshold is only loosely bracketed.

### 4. [[2611.12127]] Lost in Rounding: bf16 Recurrent State Makes Hybrid Reasoning Models Think Longer
**方向 / Area:** Inference Reliability & SDC Detection · 推理可靠性与 SDC 检测（该方向第 1 名 / rank 1）

- **理由（中）：** 六模型配对研究 + 精确 McNemar/Wilcoxon 检验：bf16 舍入到最近偶数（RTN）缓存循环状态，使 6 个混合推理模型中 5 个的思维链变长 7%–27%，Qwen3.5-9B 准确率 85.6%→70.8%；同位宽随机舍入（SR）以零开销恢复到 FP32 水平——证明元凶是舍入偏差而非精度不足。预注册判据、失败如实报告，同位宽 SR 对照把"偏差"与"分辨率"干净分离，修复端到端验证。
- **Why (EN):** Paired six-model study with exact McNemar/Wilcoxon tests, pre-registered criteria with failures reported, and a same-width stochastic-rounding control that causally separates rounding bias from resolution — plus a zero-overhead fix validated end-to-end.
- **⚠️ 注意 / Caveat:** 多数实验臂为单种子；Nemotron-3 的残差整体偏移与 Falcon-H1R-7B 的零效应均未解释。/ Single seed for most arms; the Nemotron-3 residual bulk shift and the Falcon-H1R-7B null are both unexplained.

### 5. [[2611.15543]] Testing Conversation Preservation Across LLM APIs: A Rule-Based Oracle for Detecting Silent Information Loss (isloss)
**方向 / Area:** Agent & Pipeline Silent Failures · 智能体与流水线静默失败（该方向第 2 名 / rank 2）

- **理由（中）：** 确定性规则预言机 isloss：把源/翻译后的 API 请求映射到共享中间表示 ConvIR，用 27 条保留规则检出翻译层静默信息丢失。留出故障注入集 76% 检出 / 2% 误报，外加突变体、公开 bug 与双人人工评审验证；全部 4,998 次执行可逐字节重放，7 个上游修复被独立复验。结论触目惊心：18.5% 的"通过校验"翻译仍丢失可保留信息，36.4% 的翻译回复流会损坏官方 OpenAI SDK。
- **Why (EN):** Oracle validated on held-out fault injection (76% detection, 2% false alarms), mutants, public bugs and dual-rater human review; byte-for-byte replay of all 4,998 executions; 7 upstream fixes independently re-verified.
- **⚠️ 注意 / Caveat:** 头条的 18.5% 静默丢失率测于合成套件；在录制的真实智能体流量上主速率降至 4.1%。/ The headline 18.5% silent-loss rate is measured on a synthetic suite; on recorded real agent traffic the primary rate drops to 4.1%.

### 6. [[2611.15671]] The Noise Floor of a Quantization Comparison: Engine, restart, batch and kernel drift, measured against 8-bit and 4-bit effects in two decision models
**方向 / Area:** Reliability under Extreme Performance Optimization · 极致性能优化下的可靠性（该方向第 1 名 / rank 1）

- **理由（中）：** 预注册测量研究，失败预测如实报告、工件全部公开并经社区交叉检验。在 Cloudflare 两个决策模型 2,400 条公共决策上逐一量化四种"非量化"噪声源（重启 0–22 次翻转、换引擎 6–16 次、batch 8–15 次、内核静默切换 10–14 次）：4-bit 效应（3.5%–5.8% 翻转）在两个模型上全部排除一切噪声源，而 8-bit 在 32 组对比中 3 组与噪声底不可分——量化对比必须先量出噪声底。
- **Why (EN):** Pre-registered measurement study with failed predictions reported, full artifact release and community cross-checks; cleanly separates 4-bit effects (3.5–5.8% flips) above every non-quantization noise source, while 8-bit is inseparable from the floor in 3 of 32 comparisons.
- **⚠️ 注意 / Caveat:** 同家族两个模型、单台设备（GB10），每个构建仅一对重启——作为一切比值的分母，"噪声底"本身是最不确定的量。/ Two same-family models on one device (GB10) and only one restart pair per build — the floor, the denominator of every ratio, is the least-certain measured quantity.

### 7. [[2611.13548]] Massive Activations Confound Sparse Autoencoders
**方向 / Area:** LLM Hidden States & Interpretability · LLM 隐藏状态与可解释性（该方向第 1 名 / rank 1）

- **理由（中）：** NeurIPS 录用的分析工作：巨大激活把高达 99.9% 的残差流方差压到 PC1 上，而秩一信号在 TopK 稀疏目标下无唯一稀疏分解——不同种子的 SAE 各用一组"贴砖"特征瓜分 PC1，令两大标准评测同时失真（GPT-2 前 50 重要特征 47 个跨种子不可复现；解释 99.96% 方差却漏掉 33% 内容方差）。形式化的秩一贴砖论证被干预实验证实，还给出已验证的 FVU 主导因子恒等式与零成本事后修复（bypass SAE）。此后读任何已发布 SAE 保真度数字都要带上这个视角。
- **Why (EN):** NeurIPS-accepted analysis across 10 LMs, 5 released dictionary families, ViTs and crosscoders; a formal rank-one tiling argument confirmed by interventions, and a verified FVU dominance-factor identity that changes how released SAE fidelity numbers must be read — with a zero-cost post-hoc fix.
- **⚠️ 注意 / Caveat:** 重要性侧的混淆部分源自零消融（保支撑重采样下 bypass 前 GPT-2 共享率为 83%）；拼接成本头条数字是单种子最佳情形。/ The importance-side confound is partly an artifact of zero-ablation (support-preserving resample yields 83% sharing pre-bypass on GPT-2); the splice-cost headline is a single-seed best case.

### 8. [[2611.18956]] Supercharging Olmo-core for Efficient and Scalable MoE Training
**方向 / Area:** Compute Infrastructure for Large-Scale ML · 大规模 ML 计算基础设施（该方向第 1 名 / rank 1）

- **理由（中）：** 来自代码库主人的生产级系统报告：DDP+EP+PP、NVSHMEM 行级专家并行、免同步 GPU 常驻路由元数据、grouped GEMM 与 MXFP8，在 16–512 块 B300 上支撑 12.9B–1.2T 总参数训练，1.2T 时 858 useful-model TFLOP/s/GPU。命名并分析"Token Gerrymandering"（路由器作弊压负载均衡损失却加剧失衡），配检验点分支实验佐证；全篇处处量化的负结果。
- **Why (EN):** Production-stack systems report from the codebase's owners — measured throughput matrix on 16–512 B300 GPUs (1.2T total params at 858 TFLOP/s/GPU), Token Gerrymandering backed by an analytic argument plus a checkpoint-branched experiment, and quantified negative results throughout.
- **⚠️ 注意 / Caveat:** 头条表 30 采用随机路由（学习型路由在 EP8 下最多乐观约 9%）；各行的 batch/PP/精度共同变化，无法得出单因子结论，且无 time-to-quality 结果。/ Headline Table 30 numbers use random routing (optimistic by up to ~9% with a learned router at EP8); rows co-vary batch/PP/precision, so no single-factor conclusion can be drawn, and no time-to-quality results are reported.

---

## 按主题分类 / Papers by Topic

> 每个方向内按组内对比排名（`area_rank`，1 = 最强）排序。/ Within each area, papers are listed in `area_rank` order (1 = strongest by side-by-side comparison).

### 1. LLM Training Stability & Observability · LLM 训练稳定性与可观测性（7 篇 / 7 papers）

| 排名 Rank | 论文 Paper | 类型 Type | 亮点与理由 / Highlights & Reason |
|---|---|---|---|
| 1 | [[2611.13393]] Plumbline: When the Loss Lies · 损失在说谎时的训练正确性校验 | system 系统 | 生产系统验证"损失下降 ≠ 训练正确"：3 框架 × 5 模型找到 61 个问题（32 个静默），42 个已修复/上报，含噪声校准阈值与根因复用检查库。/ Production system proving a falling loss certifies nothing: 61 problems (32 silent) across 3 frameworks × 5 models, 42 fixed/reported upstream, with noise-calibrated thresholds and reusable root-cause checks. ⭐ |
| 2 | [[2611.17876]] Delayed Effects of Temporary Weight Decay in Muon Pretraining · Muon 预训练中临时权重衰减的延迟效应 | analysis 分析 | 在移除时评估临时权重衰减会误判：迁移调度移除时差 0.26 nats、终预算反而好 0.028；固定范数重放与范数重置分离出权重范数机制。/ Temporary weight-decay schedules misjudged at removal: transferred schedule 0.26 nats worse at removal but 0.028 better at final budget; fixed-norm replays and norm resets isolate the weight-norm mechanism (162M–3.4B Muon models). |
| 3 | [[2611.12729]] KiteNorm: Variance Regularisation for Stable Post-LN Transformers · 稳定 Post-LN 的方差正则 | method 方法 | 残差缩放 + 方差正则 + 可学习跳连/残差尺度，1.3B 解码器上超过 Pre-LN 基线，深度/宽度/批量/预算的 scaling law 更优。/ Residual scaling + variance regularization + learnable skip/residual scales; outperforms Pre-LN baselines at optimal learning rates up to 1.3B, with favorable scaling laws across depth/width/batch/budget. |
| 4 | [[2611.19413]] PMR: MoE Routing with Shared Prototypes and Congestion Pricing · 共享原型与拥塞定价的 MoE 路由 | method 方法 | 两阶段原型中介路由 + 派发反馈拥塞定价实现无损负载均衡；0.43B/1.18B/0.48B 上零样本均值 +1.54/+2.65/+1.45 pp。/ Two-stage prototype-mediated routing with dispatch-feedback congestion prices for loss-free load balancing; +1.54/+2.65/+1.45 pp mean zero-shot accuracy at three scales. |
| 5 | [[2611.13137]] Byzantine-Robust Muon · 拜占庭鲁棒的 Muon 正交化 | analysis 分析 | 统一一阶信赖域框架 + 鲁棒聚合，非凸/星凸、非 i.i.d.、非精确正交化下给收敛保证；受攻击精度高于 SGD/符号更新。/ Unified first-order trust-region framework with robust aggregation for Muon, convergence guarantees under non-convex/star-convex, no i.i.d., inexact orthogonalization; higher attacked accuracy than SGD/normalized-SGD/sign updates. |
| 6 | [[2611.17459]] Classification with Large-Step Gradient Descent · 大步长梯度下降的自稳定与收敛 | analysis 分析 | 用"曲率定义的参考子空间"替代极小流形，刻画超稳定性阈值步长的三段阻尼与非单调损失。/ Curvature-defined reference subspace replaces the minimizer manifold for exponential-tail losses; explicit iterate bounds with three-phase damping and transient implicit bias of large steps. |
| 7 | [[2611.16736]] On the Difficulty of Sequence-Level Supervised Learning · 序列级监督学习为何困难 | analysis 分析 | 理论：自回归 LM 的自然序列级损失无下界；Gumbel 技巧证明贪心/采样损失等价，stop-gradient 矩匹配是有效下降方向。/ Theory only: natural sequence-level losses for autoregressive LMs are unbounded below; Gumbel-trick equivalence between greedy and sampling losses, stop-gradient moment matching proven a valid descent direction. |

### 2. RL Post-Training Dynamics & Failures · RL 后训练动态与失败（8 篇 / 8 papers）

| 排名 Rank | 论文 Paper | 类型 Type | 亮点与理由 / Highlights & Reason |
|---|---|---|---|
| 1 | [[2611.13218]] Wrong the Same Way: Cross-Prompt Sharing Both Suppresses and Amplifies Reward Hacking in RLVR · RLVR 中跨提示参数共享双向改变作弊 | analysis 分析 | 可精确枚举的受控环境证明：KL 最优解只过滤不改变作弊，一阶训练的参数共享则双向打破——决定方向的是模型对错误答案的核加权份额而非静态误报率；两个移除等量错误的验证器补丁真实精度差达 38 pp。/ In a fully-enumerable testbed, the KL optimum inherits hacking exactly while parameter sharing breaks it both ways; the effective kernel-weighted share of wrong answers, not static FPR, decides the direction — two verifier patches removing the same number of errors differ by up to 38 pts true accuracy. |
| 2 | [[2611.15779]] Honesty Is a Race · 诚实是一场赛跑 | analysis 分析 | 可预测阈值 p̃r/b > 1+κ 在三个任务族七个条件下全部成立，彩票对照构成因果控制，预注册 depth-3 预测被证实。/ A falsifiable, pre-measurable threshold (p̃r/b > 1) holding across seven conditions on three real task families, with a lottery causal control and a borne-out pre-registered depth-3 prediction. ⭐ |
| 3 | [[2611.12865]] Shortcuts and Boundaries: Verifiable RL Misalignment · 可验证 RL 的捷径与边界错位 | analysis 分析 | 奖励准确度量"有用功"仍会强化对明示上下文要求的违反：25% 冲突混合下 128 步后 97.9% 认证违规；二元合规惩罚带来双收益，安全行为迁移到 32 个未见任务（53.1%→89.1%）。/ RL reinforces violations of explicit contextual requirements even when reward accurately measures useful work: 97.9% certified violations under 25% conflict mixture; a binary compliance penalty yields joint gains and safety transfers to 32 unseen tasks (53.1%→89.1%). |
| 4 | [[2611.15493]] The Illusion of Diversity: Effective Entropy · 多样性的错觉：有效熵对齐探索 | method 方法 | 盲熵把混沌退化当有效探索；有效熵过滤无效轨迹 + VEPO 优化，1.5B/7B 上 6 个数学基准超越 GRPO，正确数匹配下策略更多样。/ Blind entropy conflates chaotic degeneration with exploration; validity-aware effective entropy + VEPO beats GRPO on 6 math benchmarks (1.5B/7B) with more distinct strategies at matched correct counts. |
| 5 | [[2611.15717]] Outside the Purview of the Reward · 奖励视野之外的多语能力漂移 | analysis 分析 | 共享多语 MoE 检查点的两条 GRPO 分支：MATH +36.07 但 XQuAD-Indic −19.32 F1；兄弟分支恢复 Indic 却牺牲数学/代码；无奖励蒸馏恢复判据抽取。/ Two GRPO branches from a shared multilingual MoE checkpoint: MATH +36.07 vs XQuAD-Indic −19.32 F1; the sibling branch recovers Indic but trades math/code; reward-free distillation restores judge-training extraction. |
| 6 | [[2611.14467]] A Theory of Policy Optimization: Coverage Collapse and Reference Resets · 策略优化的覆盖坍缩与参考重置理论 | analysis 分析 | REINFORCE/PPO/GRPO 在奖励上升时把最优响应概率推向零；APMD 参考重置给出首个保覆盖全局收敛（含 Kimi 训练用的平方损失算法）。/ Coverage collapse: REINFORCE/PPO/GRPO drive optimal-response probability toward zero while reward improves; APMD reference resets give first coverage-preserving global convergence for stylized PPO/GRPO and squared-loss algorithms used in Kimi training. |
| 7 | [[2611.12728]] Safe RL for Multi-Turn Clinical Agents · 多轮临床智能体的安全 RL | analysis 分析 | 三个受控临床环境：结果奖励 GRPO 导致过早承诺与单问坍缩；密集"不确定性消减"信用在不牺牲高风险种子的情况下提升留出价值。/ Three controlled clinical environments: outcome-only GRPO yields premature commitment and one-question collapse; dense uncertainty-reduction credit improves held-out value without high-risk seed collapse. |
| 8 | [[2611.14683]] Trait Hitchhiking in LLM Post-Training · 后训练中的性状搭便车 | analysis 分析 | Price 方程形式化 GRPO 训练中的性状演化：非目标性状被静默放大，预测更新与采样性状动态高度吻合。/ Price-equation formalism of trait evolution during GRPO: non-targeted traits are silently amplified, and predicted updates closely track sampled trait dynamics. |

### 3. LLM Hidden States & Interpretability · LLM 隐藏状态与可解释性（25 篇 / 25 papers）

| 排名 Rank | 论文 Paper | 类型 Type | 亮点与理由 / Highlights & Reason |
|---|---|---|---|
| 1 | [[2611.13548]] Massive Activations Confound Sparse Autoencoders · 巨大激活污染稀疏自编码器 | analysis 分析 | 巨大激活把 99.9% 方差压到 PC1，秩一信号无唯一稀疏分解，令 SAE 两大评测同时失真（47/50 头部特征跨种子不可复现）；bypass 修复零成本。/ Massive activations concentrate 99.9% of variance on PC1; no unique sparse decomposition exists for rank-one signals, so importance and FVU metrics both distort (47 of top-50 features unmatched across seeds); the bypass fix is zero-cost. ⭐ |
| 2 | [[2611.20148]] Centered Ablation · 中心化消融的闭式修复 | method 方法 | 末层方向消融是从原点度量的余弦门控 logit 偏置：欠触发处 +29/+46 pp 攻击成功率，Gemma-2-9B 崩溃 50%→1%；两个标准安全评委对崩溃文本打出相反分数（46 点虚构效应）。/ Last-layer ablation is a logit bias gated by an origin-measured cosine; Centered Ablation adds +29/+46pp attack success where the standard under-fires and cuts collapse 50%→1%; two standard safety judges score collapsed text in opposite directions. |
| 3 | [[2611.14996]] Breaking Bad: "Going Badly" Activations Drive Reward Hacking · "进展糟糕"激活驱动奖励作弊 | analysis 分析 | 从失败累积故事（无作弊示例）中提取的方向在作弊前升高；相减减少作弊，过度相减让智能体对失败测试失明。/ A direction extracted from failure-accumulating stories without hacking examples rises before hacks; subtraction reduces cheating, over-subtraction blinds the agent to failing tests. |
| 4 | [[2611.12675]] Interpretability Is Not Model-Specific · 可解释性不必按模型重做 | analysis 分析 | 无标签提示学出的残差流线性映射在 110 个模型对间迁移拒绝引导（102% 恢复）与探针（88–98%），免费覆盖分数可预测恢复率。/ Unlabeled-prompt linear maps between residual streams transfer refusal steering (102% recovery) and probes (88–98%) across 110 model pairs; a label-free coverage score tracks recovery over 16,000+ runs. |
| 5 | [[2611.13543]] Sanity Checks for Attention Surgery · 注意力手术的 sanity check | analysis 分析 | 三个可复用检验（噪声底/几何零模型/匹配干预）用于表征驱动的架构修改：9 模型 5,408 头，预注册 3×8 种子因子实验。/ Three reusable checks (noise floor, geometric null, matched intervention) for representation-motivated design, applied to self-attention removal across 9 models / 5,408 heads with a pre-registered 3-arm × 8-seed factorial. |
| 6 | [[2611.14942]] Emergent Vision-Shaped Thinking in Text-Only Reasoning · 文本推理中涌现的视觉形思维 | analysis 分析 | 隐状态空间中消融视觉-语言轴：Chameleon-7B BBH-navigate −27.6pp 与 boolean +5.6pp 双分离，BAGEL/Janus-Pro 定位双通路。/ Vision-language axis ablation in hidden-state space: Chameleon-7B BBH-navigate −27.6pp vs boolean +5.6pp double dissociation, dual-path localization in BAGEL/Janus-Pro. |
| 7 | [[2611.19499]] Do Probing and Steering Favor the Same Directions? · 探针与转向是否偏好同一方向 | analysis 分析 | 协方差调整判别到均值差的单参数方向族：59/60 组合中探针分离成立，但转向偏好均值差方向；探针迁移保留 81–91%，转向迁移更弱。/ One-parameter family from covariance-adjusted discriminant to mean difference: probing separation holds in 59/60 layer-model-concept cells, but steering favors mean-difference directions; probe transfer retains 81–91%, steering transfer weaker in 11/12 pairs. |
| 8 | [[2611.13885]] Are Causal Neuron Circuits Unique and Transferable? · 因果神经元回路是否唯一且可迁移 | analysis 分析 | 4096 子集穷举消融 + 激活修补，Qwen3/Llama/Gemma 小模型两跳链 vs 随机神经元基线。/ Exhaustive 4096-subset ablations + activation patching on two-hop chains in four small models vs random-neuron baselines. |
| 9 | [[2611.17297]] Goal Encoding in LLMs · LLM 中的目标编码 | analysis 分析 | 下一子目标编码定位于稀疏注意力头，可解码为自然语言未来动作，跨编程语言因果且可塑。/ Next-sub-goal encoding localized in a sparse set of attention heads, decodable as natural-language future actions, causal and plastic across programming languages. |
| 10 | [[2611.15267]] A Closer Look at Language Model Introspection · 再看模型内省 | analysis 分析 | 扰动激活上线性探针 vs 零样本自答：8.4B tokens 时 98.3% vs 11.1%；位置信息从随机初始化网络即可解码。/ Linear probes vs zero-shot self-report on perturbed activations: 98.3% vs 11.1% at 8.4B tokens; location is decodable from randomly initialized networks. |
| 11 | [[2611.19176]] A Bag of Concepts? Role-Filler Binding · 可言语化工作区是否绑定角色-填充 | analysis 分析 | 残差流探针近满分，但工作区（J-lens/R-lens 等）低于秩匹配随机对照；转向对绑定的改变不超强度匹配对照。/ Near-ceiling residual-stream probes but below rank-matched random controls on the workspace (J-lens/R-lens, DoM, LRE-gradient); steering changes binding no more than strength-matched controls. |
| 12 | [[2611.14168]] Representational Atoms in Neural Networks · 神经网络中的表征原子 | method 方法 | 阈值激活 SAE 被证明能以高保真/高稳定恢复基本表征单元，稳定性关联单义性并支持跨层组合。/ Threshold-activated SAEs proven to recover fundamental representational units with fidelity and stability; stability-linked monosemanticity and cross-layer composition. |
| 13 | [[2611.19403]] Confidence Without Cause: Physics-Shortcut Sensitivity · 无因果的自信：物理捷径敏感度 | analysis 分析 | DECOY 155 个认证反事实提示族；层 18 线性探针生成前预测敏感度 AUROC 0.760，敲除 4 个层 16 注意力头取消敏感度。/ DECOY 155 certified-counterfactual families; a layer-18 linear probe predicts sensitivity before generation at AUROC 0.760, knocking out 4 layer-16 attention heads cancels it. |
| 14 | [[2611.11892]] When Answer Decodability Is Not a Decision · 答案可解码 ≠ 已做决定 | analysis 分析 | 发射受控双目标探针：Qwen3.5-4B 发射间隙 .696，Qwen3-8B MMLU thinking 上反转（−.398）；种植信号对照。/ Emission-controlled dual-target probing: emission gap .696 on DecisionDepth (Qwen3.5-4B), reversal on Qwen3-8B MMLU thinking (−.398 lift), with planted-signal controls. |
| 15 | [[2611.12206]] A Geometric Invariant of Attention Predicts Head Specialization · 预测头特化的注意力几何不变量 | analysis 分析 | 标量不变量 ρ 仅从权重预测归纳头（Spearman −0.55~−0.74，4 个 RoPE 模型）；ρ 引导的 YaRN 比均匀分配更少伤困惑度。/ A scalar invariant ρ predicts induction heads from weights alone (Spearman −0.55 to −0.74 across four RoPE models); ρ-guided YaRN degrades perplexity less than uniform. |
| 16 | [[2611.18514]] Can Mechanistic Interpretability Explain LLM Agent Failures? · MI 能否解释智能体失败 | analysis 分析 | 末 token 线性探针预测网页元素幻觉 AUC 0.80，转向修正 85% 且仅破坏 7% 有效动作；格式敏感与分布式计算挑战回路发现。/ A linear probe on the last prompt token predicts web-element hallucination at 0.80 AUC; steering corrects 85% while disrupting 7% valid actions; format sensitivity challenges circuit discovery. |
| 17 | [[2611.19848]] A phase diagram for training and inference · 训练与推理的相图 | analysis 分析 | 集体坐标（文档可分性/维度）绘制相图：156 个未训练流趋向坍缩或噪声，8 个训练模型居中；训练解释为相变。/ Collective coordinates trace inference flows on a phase diagram: 156 untrained-model flows move toward collapse/noise, 8 trained models reside centrally; training interpreted as a phase transition. |
| 18 | [[2611.13270]] What Drives Emergence of Symbolic Mechanisms? · 符号机制涌现的驱动因素 | analysis 分析 | 从头训练抽象序列任务：数据多样性越高符号特征越强；相同特征出现在改造的 transformer 甚至 MLP 中。/ From-scratch training on abstract sequence tasks: greater data diversity yields stronger symbolic signatures; the same signatures appear in modified transformers and even MLPs. |
| 19 | [[2611.19826]] Where Is Rank-1 DiM Refusal Intervenable in Multimodal LM Derivatives? · 多模态衍生模型的拒答可干预位置 | analysis 分析 | 共享 mean/rank-1 DiM 协议扫描衍生目录：文本解码器 T 处提升 ASR，E/P/F 处不提升；VLGuard 0.030→0.150（T）而 P/E 近随机。/ Shared rank-1 DiM extract-intervene protocol over the derivative catalog: text DiM at T raises ASR while E/P/F do not; VLGuard 0.030→0.150 at T, near chance at P/E. |
| 20 | [[2611.17461]] Tracing Knowledge and Reasoning in LLM · 追踪 LLM 中的知识与推理 | analysis 分析 | 16 个 LLM × 24 个基准的注意力/激活信号把任务放到"检索主导-推理主导"连续谱上。/ Attention/activation signals across 16 LLMs × 24 benchmarks place tasks on a retrieval-dominant to reasoning-dominant continuum. |
| 21 | [[2611.18089]] Deep Latents, Long Memory · 潜变量持续性与激活长记忆 | analysis 分析 | 持久潜编码产生慢自相关尾；SAE 特征持续性与自相关幅度跨数据集相关，消融持久特征可降低之。/ Persistent latent codes create slow autocorrelation tails; SAE-feature persistence correlates with tail magnitude across datasets/LLMs, and ablating persistent features reduces it. |
| 22 | [[2611.16190]] When Can an Interpretability Claim Be Trusted? · 可解释性结论何时可信 | analysis 分析 | 特征维度不连续 + 岭杠杆稳定界 3√3/(8√λ)；证书在每次检验内成立，却不能跨独立训练字典传递（55% 恢复标志随种子翻转）。/ Feature-dimensionality discontinuities plus a ridge-leverage stability bound; certificates hold within every test yet certify nothing across independently trained dictionaries (55% of recovered-flags flip with seed). |
| 23 | [[2611.18272]] From Bytes to Behavior: Request-Level Attribution from Live GPU Hidden States · 从活动 GPU 隐状态做请求级归因 | method 方法 | 无侵入调试器逐层恢复残差流（按分配器或内核时钟），33 模型逐字节精确；拒答探针留出 AUROC 0.88。/ A non-modifying debugger recovers per-layer residual-stream tensors via allocator or kernel-launch clocks, byte-exact on 33 models; refusal probe AUROC 0.88 on held-out prompts. |
| 24 | [[2611.18274]] Right Token, Right Time: Trajectory-Aware Activation Steering · 按轨迹感知的激活转向 | method 方法 | 常开 SAE 转向使表征偏离训练分布；按 token 预算分配 + 闭环 CLABS 在同预算下取得最大行为改变。/ Always-on SAE steering displaces representations; per-token budget allocation with closed-loop CLABS achieves the largest behavioral shift at matched budgets. |
| 25 | [[2611.19075]] The Geometry of Conceptors in Neural-Activation Spaces · 概念子的几何学 | analysis 分析 | 概念子表征按拟合对比精确分解为极点滤波/均值分离/协方差形状；配额与探针精度相关，双极拟合放大两极。/ Exact pole-filter/mean-separation/covariance-shape decomposition of conceptor fits; quota correlates with layerwise probe accuracy, bipolar fits amplify both poles. |

### 4. Inference Reliability & SDC Detection · 推理可靠性与 SDC 检测（10 篇 / 10 papers）

| 排名 Rank | 论文 Paper | 类型 Type | 亮点与理由 / Highlights & Reason |
|---|---|---|---|
| 1 | [[2611.12127]] Lost in Rounding · bf16 循环状态让混合推理模型想更久 | analysis 分析 | bf16 RTN 缓存循环状态使 5/6 模型思维链变长 7–27%、Qwen3.5-9B 精度 85.6%→70.8%；同位宽随机舍入零开销恢复 FP32 水平。/ bf16 RTN recurrent-state caching lengthens CoT in 5 of 6 models (Qwen3.5-9B 85.6%→70.8%); same-width stochastic rounding restores FP32 behavior at bf16 cost. ⭐ |
| 2 | [[2611.17634]] A Unified Device-Level Physical Framework for DRAM Read Disturbance · DRAM 读扰动的统一器件级物理框架 | analysis 分析 | DIMM 实测 + 器件测量 + 约 70 万器件校准的 TCAD，用电子迁移/电容耦合/读出放大器介导扰动统一解释 RowHammer/RowPress/ColumnDisturb 的极性与反转。/ Unified device-level framework (trap-assisted migration, capacitive coupling, sense-amp-mediated disturb) triangulating DIMM, device and TCAD evidence to explain RowHammer/RowPress/ColumnDisturb polarities and reversals. |
| 3 | [[2611.15469]] HARE: Fast Read Disturbance Threshold Profiling · 快速读扰动阈值画像 | method 方法 | 故意加剧扰动的降时序约束画像：180 颗真实 DDR4 芯片、4 厂商，行 RDT 快 31.2%，模块最低值低 21.7%，覆盖 >95% 单元。/ Reduced-timing-constraint profiling that intentionally exacerbates disturbance on 180 real DDR4 chips from 4 manufacturers: 31.2% faster row RDT, 21.7% lower module minimum, >95% cell coverage. |
| 4 | [[2611.13730]] Deterministic, Reproducible Inference in Exact Integer Arithmetic · 精确整数算术的确定性可复现推理 | system 系统 | 精确整数运行时跨 ISA/编译器/线程 SHA 可验地逐位一致；GLM-4.5-Air（427 GB 权重码）跨 3 台机器拆分仍逐位相同。/ An exact-integer runtime with SHA-verified bit-identical output across ISAs and CPU/GPU; GLM-4.5-Air (427 GB of codes) split across 3 machines stays bit-identical. |
| 5 | [[2611.19135]] How Much Determinism Can Fine-Tuning Buy? · 微调能买到多少确定性 | method 方法 | 同一提示随 batch 组成翻转 token；对 top-1/top-2 logit 间隙做噪声分位数缩放的铰链边际正则，翻转少 35%、发散 53.8%→38.1%（代价 1.3–2.9 个精度点）。/ Identical prompts flip tokens with batch composition; hinge margin regularization on the top-1/top-2 logit gap scaled to measured noise quantile cuts flips 35% and divergence 53.8%→38.1% at 1.3–2.9 accuracy points. |
| 6 | [[2611.14083]] Sable: Small-Field Sumcheck for Bit-Exact Inference · 小域 sumcheck 证明逐位精确推理 | system 系统 | 整数量化 transformer 上的 sumcheck 论证系统：Qwen2.5-32B 64 层单 GPU 92.5 s 证明，比 zkLLM 每参数-token 快 40–64 倍。/ A sumcheck argument system over integer-quantized transformers: Qwen2.5-32B's 64 layers proved in 92.5 s on one GPU, 40–64× less time per param-token than zkLLM. |
| 7 | [[2611.14051]] Can KV Cache Be Reused Across Model Updates? · 模型更新后 KV 缓存能否复用 | analysis 分析 | 跨 4 次模型更新的 Functional Cache Divergence：检索精度从近原生到大损失不等；3 个 QA 基准 TTFT 提速 2.10–5.08×。/ Functional Cache Divergence over next-token distributions across 4 model updates (DeepSeek-V4-Flash case study): retrieval accuracy ranges from near-native to large losses, at 2.10–5.08× TTFT speedups. |
| 8 | [[2611.14209]] Breakdown of Autoregressive Multi-Step Reasoning Under Attention Head Dropout · 集中 vs 扩散注意力头失效 | analysis 分析 | 同预算下"集中瞬时静默"比"扩散掩盖"更伤自回归推理：Qwen3-8B 91.2→78.8%，LLaMA-3.1-8B 84.0→76.8%，精确 McNemar p=5.5e-6。/ Burst vs budget-matched diffuse attention-head masking over 250 paired GSM8K derivations: Qwen3-8B 91.2→78.8%, LLaMA-3.1-8B 84.0→76.8%, exact McNemar p=5.5e-6. |
| 9 | [[2611.19165]] From Sensors to Silicon: Causal Cross-Layer Self-Healing Edge AI · 传感器到硅片的因果跨层自愈边缘 AI | system 系统 | 同步遥测（传感健康/推理不确定性/硬件计数器/功耗热）上的因果跨层推理引擎，量化并发扰动下的诊断不确定性。/ A causal cross-layer reasoning engine over synchronized telemetry (sensor health, inference uncertainty, HW counters, power/thermal) that quantifies diagnostic uncertainty under concurrent perturbations. |
| 10 | [[2611.15842]] Fewer Expert Transfers Without Changing Routing · 不改路由的专家逐出 | analysis 分析 | L40S 上实测 CPU→GPU 拷贝：每个快于 LRU 的路由固定策略都以 ≥0.067 nats 下-token 损失为代价；保路由前瞻逐出少拷 2.1× 且无损。/ Timed real CPU-to-GPU copies: every routing-fixed policy decoding faster than LRU costs ≥0.067 nats; routing-preserving future-aware eviction copies 2.1× fewer experts at no loss. |

### 5. Reliability under Extreme Performance Optimization · 极致性能优化下的可靠性（20 篇 / 20 papers）

| 排名 Rank | 论文 Paper | 类型 Type | 亮点与理由 / Highlights & Reason |
|---|---|---|---|
| 1 | [[2611.15671]] The Noise Floor of a Quantization Comparison · 量化对比的噪声底 | analysis 分析 | 预注册研究量化四类非量化噪声源（重启/引擎/batch/内核漂移）：4-bit 效应 3.5–5.8% 排除一切噪声源，8-bit 在 32 组中 3 组与底不可分。/ Pre-registered measurement of engine/restart/batch/kernel drift: 4-bit effects (3.5–5.8% flips) exclude every non-quantization source; 8-bit is inseparable from the floor in 3 of 32 comparisons. ⭐ |
| 2 | [[2611.12634]] Second-Order Linear Response Predicts Quantization Mismatch · 二阶线性响应能否预测量化失配 | analysis 分析 | 预注册测量 5 个模型 3 种量化：相对预测在 16 倍扰动范围内成立；bf16 梯度造成 4× 预测误差、fp32 反向修复；未见 Mistral 上全部 KL 预算达标。/ Pre-registered measurements on 5 LMs: relative predictions hold over a 16-fold perturbation range; bf16 gradients cause 4× prediction errors fixed by fp32 backward; all KL budgets met on unseen Mistral. |
| 3 | [[2611.11780]] Planners Exploit Deterministic Error: Dithered Low-Bit World Models · 规划器利用确定性误差：抖动低位世界模型 | analysis 分析 | 持久 RTN 量化误差驱动规划崩溃（高达 100 个成功点，单步误差不变）；候选间共享抖动重抽样修复 ≥半数损伤；W8A4 rollout 快 1.9–3.3×。/ Persistent round-to-nearest quantization error drives planning collapse (up to 100 success points with unchanged one-step error); candidate-shared dither repairs ≥half the damage; W8A4 rollouts 1.9–3.3× faster. |
| 4 | [[2611.12832]] What the Loss Curve Misses: FP4 Slows Rare-Fact Acquisition · FP4 拖慢罕见事实习得 | analysis 分析 | 匹配验证损失（差 0.5–2%）下 NVFP4 需 1.32–1.52× 暴露次数才达同等召回；更新噪声占代价约 2/3；BF16 检查点梯度统计 Spearman 0.96 排序格式代价。/ At matched validation loss, NVFP4 needs 1.32–1.52× exposures for matched recall; update noise carries ~2/3 of the cost; BF16-checkpoint gradient statistics rank format costs at Spearman 0.96. |
| 5 | [[2611.17501]] Microscaling Formats for R&R Models · 检索与排序模型的微缩放格式 | analysis 分析 | 生产 R&R 模型仅容忍 0.01% 归一化熵精度损失；MI350X 上首批原生 MXFP6 GEMM，端到端吞吐 +7.6–14.3%。/ Production R&R models tolerate only a 0.01% normalized-entropy margin; first native MXFP6 GEMM results on MI350X, E2E throughput +7.6–14.3% on two production ads models. |
| 6 | [[2611.13410]] SteerDistill: Closed-Loop Teacher Steering for Quantized Agents · 闭环教师引导量化蒸馏 | method 方法 | 全精度教师用执行反馈指导量化学生修订失败响应，再经量化感知蒸馏内化；W4A16 下 5 个智能体基准 +1.67–2.18 pts，GPU 时少 67%。/ A full-precision teacher guides revision of failed student responses using execution feedback, internalized by quantization-aware distillation; +1.67–2.18 pts under W4A16 across 5 agentic benchmarks with 67% fewer GPU hours. |
| 7 | [[2611.18511]] Numerical Issues of Divergences Between Nearly Equal Distributions · 近等分布散度的数值问题 | analysis 分析 | 舍入与消去污染近等分布间散度；给前向/反向 KL、广义 JSD、MC KL 与熵的数值稳定重构，性质测试验证。/ Rounding and cancellation corrupt divergences between nearly equal distributions; numerically stable reformulations for KL/JSD/MC-KL/entropy validated by property-based tests — affects distillation, RL and proximal objectives. |
| 8 | [[2611.13879]] SFU-Sim: Bit-Exact Reverse Engineering of NVIDIA MUFU · NVIDIA 特殊函数单元的逐位逆向 | system 系统 | 黑盒逐位建模 MUFU 指令与 PTX 路径，Ampere/Ada/Blackwell 上 FP16/FP32 穷举扫描零失配，开源。/ Black-box bit-exact models of MUFU instructions and PTX paths; exhaustive FP16/FP32 input sweeps on Ampere/Ada/Blackwell with zero mismatches, open source. |
| 9 | [[2611.19722]] MIAO: Microscaling Intermediate Accumulation Optimization · 微缩放中间累加优化 | method 方法 | 在端到端困惑度约束下联合选择乘积精度与分段累加器位宽：6 个 LLM 上至多 1.60% 额外退化换 −38.7% 阵列面积、−36.1% 能耗。/ Jointly selecting product precision and stage-dependent accumulator widths under an end-to-end perplexity constraint: −38.7% PE-array area and −36.1% energy for at most 1.60% extra degradation. |
| 10 | [[2611.18769]] Gradient-Guided Hardware-Native MIXFP4 · 梯度引导的硬件原生 MIXFP4 | method 方法 | FlipQuant 从分桶 KL 梯度学习逐 MMA tile 的 E2M1/E0M3 格式图：跨 6 个 LM 关闭 NVFP4 困惑度差的 42.5%（FourOverSix 仅 13.3%），GEMM 开销 1.9%。/ FlipQuant learns a per-MMA-tile format map from bucketed-KL gradients: closes 42.5% of the NVFP4 PPL gap vs 13.3% for FourOverSix across 6 LMs at 1.9% GEMM overhead. |
| 11 | [[2611.16502]] SignRot: Outlier-Aware Sign-Adjusted Rotation · 符号调整旋转对抗巨大离群 | method 方法 | 符号调整 Hadamard 旋转 + 非对称零点量化，LLaMA3-70B WikiText2 ppl 5.88、零样本 72.73，超过 SpinQuant/QuaRot，单次校准。/ Sign-adjusted Hadamard rotation + asymmetric zero-point quantization: WikiText2 ppl 5.88 and 72.73 zero-shot on LLaMA3-70B, surpassing SpinQuant/QuaRot in a single calibration pass. |
| 12 | [[2611.17605]] Choosing Quantized Code LLMs by File Size and Energy per Solved Task · 按文件体积与每任务能耗选量化代码模型 | analysis 分析 | 无风扇 MacBook Air M2 上 24 个 GGUF 文件、542 个 EvalPlus 任务计价：7B-q2_K 相比 3B-q4_K_M 无显著解题增益、每解能耗 2.03×。/ Pricing 24 GGUF files on 542 EvalPlus tasks: 7B-q2_K brings no significant solve gain over 3B-q4_K_M at 2.03× energy per solved task — the bigger-at-lower-precision rule does not always pay. |
| 13 | [[2611.15569]] TraceKV: Policy-Preserving Low-Rank KV Compression · 保策略的低秩 KV 压缩 | method 方法 | 在线校准 + 敏感度感知 SVD + 全局秩分配：5.64× KV 压缩（含量化）下推理精度近无损，解码提速至 1.83×。/ On-policy calibration + sensitivity-aware SVD + global rank allocation: near-lossless reasoning accuracy at 5.64× KV compression combined with quantization, up to 1.83× decode speedup. |
| 14 | [[2611.12054]] Low-Rank Low Precision Training of Gaussian Processes · 高斯过程的低秩低精度训练 | method 方法 | AnchorNet 地标选择 + FITC 修正的低秩目标，九个大数据集匹配参考精度；fp16/TF32 仅提速有限且病态条件下不可靠。/ AnchorNet landmark selection + FITC correction with analytic gradients in single precision; fp16/TF32 variants give modest speedups and turn unreliable under poor conditioning. |
| 15 | [[2611.16426]] SoScale: Second-Order Scale Search for FP4 · FP4 的二阶尺度码搜索 | method 方法 | Hessian 感知的二阶尺度码搜索 + GPTQ 式误差恢复，在 Qwen3 系列上跨 MXFP4/NVFP4/HiF4 一致降低下游退化。/ Hessian-aware second-order scale-code search coupled with GPTQ-style error recovery consistently reduces downstream degradation across Qwen3 models under MXFP4/NVFP4/HiF4. |
| 16 | [[2611.16561]] SPARC: Photonic Matrix Multiplication via Representative Vectors · 代表向量的光子矩阵乘 | method 方法 | 代表向量分组：相近激活数字化计算、小范数残差交给光子单元，六个 DNN 跨架构提升精度，无需改硬件。/ Representative-vector grouping computes similar activations digitally and offloads small-norm residuals to the photonic unit; six DNN models improve accuracy with no hardware modification. |
| 17 | [[2611.19944]] Exhaustive Evaluation of Fixed-Point Reciprocal Architectures · 定点倒数架构的穷举评估 | analysis 分析 | Q16.16（131,073 输入）与 Q8.24（33,554,433 输入）穷举对照精确整数参考；精化路径最大相对误差降 205–223×，1 输入/周期 @10 周期延迟。/ Exhaustive test of every representable input in [0.5,2.5] for Q16.16 and Q8.24 against an exact integer reference; refined paths cut max relative error 205–223× at 1-input/cycle, 10-cycle latency. |
| 18 | [[2611.15231]] TQIR: Trellis Quantization with Integer Reconstruction · 整数重构的网格量化 | method 方法 | 解耦存储/权重/激活精度的整数重构网格 + 子空间 Hadamard 变换；TSMC 16nm 译码器 307.2 Gweights/s @ 0.0509 mm²，面积效率大幅领先。/ Integer-reconstruction trellis decoupling storage/weight/activation precisions with a subspace Hadamard transform; TSMC 16nm decoder at 307.2 Gweights/s in 0.0509 mm², 13.93×/1.52× area efficiency vs prior decoders. |
| 19 | [[2611.16478]] One Model, Two Precisions · 量化副本分歧能否预示错误 | analysis 分析 | 3–6 bit 模拟 RTN、8,398 道选择题：分歧 AUROC 0.684 vs 熵 0.682——大体为阴性结果，但给出部署配方与失败案例。/ Simulated 3–6-bit round-to-nearest copies over 8,398 MCQs: best disagreement AUROC 0.684 vs entropy 0.682 — mostly a null result, with a deployment recipe and failure cases. |
| 20 | [[2611.14924]] Edge-Native Multimodal RAG on Consumer GPUs · 消费级 GPU 上的边缘原生多模态 RAG | system 系统 | Tesla T4 上 NF4 vs GPTQ 对比：8.37 GB 占地 + 430 MB Florence-2；结构化少样本提示把数学准确率 35.0→92.0%。/ NF4 vs GPTQ empirical comparison on Tesla T4: 8.37 GB footprint with Florence-2 at 430 MB; structured few-shot prompting restores math accuracy 35.0→92.0% over 200 trials. |

### 6. Compute Infrastructure for Large-Scale ML · 大规模 ML 计算基础设施（10 篇 / 10 papers）

| 排名 Rank | 论文 Paper | 类型 Type | 亮点与理由 / Highlights & Reason |
|---|---|---|---|
| 1 | [[2611.18956]] Supercharging Olmo-core for Efficient and Scalable MoE Training · 重构 Olmo-core 的可扩展 MoE 训练 | system 系统 | DDP+EP+PP + NVSHMEM 行级 EP + 免同步 GPU 常驻路由元数据 + MXFP8：512 块 B300、1.2T 总参数 858 TFLOP/s/GPU；命名并实证 Token Gerrymandering。/ DDP+EP+PP with NVSHMEM rowwise EP, sync-free routing metadata, grouped GEMM and MXFP8: 1.2T params at 858 TFLOP/s/GPU on 512 B300s; names and demonstrates Token Gerrymandering router hacking. ⭐ |
| 2 | [[2611.13188]] One-Sided Expert-Parallel All-to-All over NVLink · NVLink 单侧专家并行 all-to-all | method 方法 | 源 rank 直推 token 到目标 rank-major 工作区、分组 GEMM 就地读取；8×B300 上 dispatch/combine 比 DeepEP 快 1.2–3.0×，整层最快 2.4×，已进 FlashInfer3/vLLM/SGLang。/ One-sided rank-major push buffers with in-place grouped-GEMM reads and Fence/Sentinel sync; 1.2–3.0× faster than DeepEP on dispatch/combine, layer up to 2.4× faster, already shipped in FlashInfer3/vLLM/SGLang. |
| 3 | [[2611.11857]] OverlapAdvisor: Overlap for Distributed MoE Serving · MoE 服务的算通重叠建模与自适应 | system 系统 | 103 个形态 × 4 平台的统一比较：无策略在 >80.6% 配置上占优；两级粒度性能模型 + 启动时策略选择，端到端吞吐 +31.7%。/ Largest unified comparison of MoE overlap strategies (103 shapes × 4 platforms; no strategy dominates >80.6% of configs) with a two-granularity performance model and launch-time selection, +31.7% e2e throughput. |
| 4 | [[2611.18145]] Compiling Specialized GPU-Initiated Networking (Obaleth) · 编译 GPU 发起的专用水网络 | system 系统 | 把 GPU 发起通信编进内核 IR 共同优化：H100 小消息快至 3.3×，256 GPU all-to-all 1.25–2.3× 于 NVSHMEM/NCCL GIN，vLLM Qwen3-235B +1.29× vs DeepEP。/ Compiles GPU-initiated communication into the kernel IR and co-optimizes it: small messages up to 3.3× faster on H100, all-to-all 1.25–2.3× vs NVSHMEM/NCCL GIN on 256 GPUs, vLLM Qwen3-235B +1.29× vs DeepEP. |
| 5 | [[2611.15951]] Starscream: LLM Sharding on AMD Instinct with GPU Partitioning · 芯片 NUMA 下的 LLM 切分重想 | system 系统 | 正交 GPU 内切分保留核形状：MI300X/MI355X 上注意力至 4×、融合 GEMM 1.43× 于芯片盲基线。/ Orthogonal intra-GPU sharding preserving kernel shapes on partitioned logical devices: up to 4× attention and 1.43× fused-GEMM speedups over chiplet-oblivious baselines on MI300X/MI355X. |
| 6 | [[2611.13412]] Bursts That Outlast Themselves: Persistent Degradation in Prefix-Cached Agent Serving · 前缀缓存智能体服务的亚稳态持续退化 | analysis 分析 | 短暂突发后 vLLM 命中率 ~10%、吞吐减半、积压 70 分钟（9/12 对）；限流仅救回 1/7，基于容量的会话挂起与 KV 需求预算器全部救回。/ Metastable persistent degradation after brief bursts (vLLM: ~10% hit ratio, half throughput, 70-min backlog; 9/12 pairs); throttling recovered only 1/7 runs, capacity-based session suspension and a KV-demand budgeter recovered/prevented all. |
| 7 | [[2611.13293]] Decode Token Parallelism · 解码 token 并行的分布式注意力 | system 系统 | 每请求局部注意力 + 仅当前 token 激活跨节点，all-reduce 限 NVLink 内；405B/340B 于 64 H100 上较 DCP 至 1.7×、较 DP 至 2.06×。/ Balanced layer blocks with per-request local attention; only current-token activations cross nodes and all-reduces stay within NVLink — Llama-3.1-405B / Nemotron-4-340B on up to 64 H100s, up to 1.7× over DCP and 2.06× over data parallelism. |
| 8 | [[2611.17857]] Fuse-All MoE Inference Kernel with Load Balancing on TPUs · TPU 上的全融合 MoE 推理核 | system 系统 | 融合 token 收集/专家投影/门控激活/输出写 + 负载均衡：偏斜 EP16 预填充从 2.3× 降到 1.09× 于均衡参考，服务吞吐 +34.5%。/ Fuses token collection, expert projections, gated activation and output writes with load balancing: skewed EP16 prefill 2.3×→1.09× of balanced reference, +34.5% serving throughput vs Megablox. |
| 9 | [[2611.16219]] GC-MoE on SM120: Warp-Level FP8xFP4 on Consumer Blackwell · 消费级 Blackwell 上的 FP8xFP4 MoE | system 系统 | 批量 bulk-pull 派发 + 去重缓存的 warp 级块缩放 MMA：8×RTX PRO 5000 上 18/18 胜 W4A8/MegaMoE 基线，cosine ≥0.9999997。/ Warp-level FP8xFP4 block-scaled MMA with batched bulk-pull dispatch and dedup cache: 18/18 wins over FlashInfer W4A8 and Cake MegaMoE on 8×RTX PRO 5000, cosine ≥0.9999997. |
| 10 | [[2611.14681]] Together Compiler: Continual Compilation for AI Inference · AI 推理的持续编译 | system 系统 | 分层持久引擎 + 成本模型种子的智能体爬山搜索：比手写 Megakernel 至 1.7×，多个开源引擎上 batch-1 达 1111–1205 TPS。/ Tiered persistent engine + cost-model-seeded agent hill-climbing: up to 1.7× over hand-written Megakernels and 1111–1205 TPS at batch 1 in production, 2.6× TPS over best open engines. |

### 7. Agent & Pipeline Silent Failures · 智能体与流水线静默失败（5 篇 / 5 papers）

| 排名 Rank | 论文 Paper | 类型 Type | 亮点与理由 / Highlights & Reason |
|---|---|---|---|
| 1 | [[2611.13254]] Dependable Long-Horizon LLM Agents: A Trajectory-Centered Empirical Study · 长程多智能体失败的轨迹中心实证 | analysis 分析 | 95 条失败轨迹全量精读：故障中位数在轨迹 18% 处进入；72% 早已存在相反证据但 88% 无人利用；最有效控制是裁判/契约而非本地检查点；45% 手工失败实为 harness 崩溃后冒名答案。/ Full reads of 95 failed multi-agent runs: median fault entry at 18% of trajectory; 72% contained unused contrary evidence; the most effective controls are judges/contracts, not local checkpoints; 45% of hand-crafted failures ended with a harness-emitted answer after a provider crash. |
| 2 | [[2611.15543]] isloss: A Rule-Based Oracle for Silent Information Loss · 检测 API 翻译层静默信息丢失 | method 方法 | ConvIR + 27 条保留规则的确定性预言机：留出注入 76% 检出 / 2% 误报；18.5% 翻译静默改信息，36.4% 回复流损坏官方 SDK。/ A deterministic rule-based oracle (ConvIR + 27 preservation rules): 76% detection at 2% false alarms on held-out injection; 18.5% of valid-looking translations silently change information. ⭐ |
| 3 | [[2611.19886]] Recovery Gone Too Far: Risky Fallback in LLM Agents · 修复过头：智能体的危险回退 | analysis 分析 | 304 场景 × 8 域 × 55 个真实 CVE：4 个主流模型全部存在危险回退，越界至 96.8%；3 种主流缓解无效；校准于正常运行的监视器把违规 67.5%→16.2%（成功率降 <7%）。/ 304 scenarios × 8 domains × 55 real CVEs: all 4 mainstream models exhibit risky fallback (violations up to 96.8%); 3 mainstream mitigations ineffective; a monitor calibrated on normal runs cuts violations 67.5%→16.2% at <7% success drop. |
| 4 | [[2611.19237]] Auditable Authorization for LLM Agents · 智能体授权的可审计性 | analysis 分析 | 跨模型/harness/工作流层的配对决策审计：被拒的工作照样执行、被批准的工作被丢弃；CrewAI 恢复时遗漏 336/672 条批准，n8n 有 4/59 个工作流在 Reject 后仍执行。/ Paired-decision audit across model/harness/workflow layers: rejected work executes and authorized work is dropped; CrewAI restoration omits 336/672 approvals, 4/59 n8n workflows execute after Reject. |
| 5 | [[2611.20071]] The Silent Cost of Conversation History in LLM Reasoning · 对话历史的静默代价 | analysis 分析 | 预注册研究：48 个分片数学任务上累积历史静默降低准确率（Holm 校正 p≤0.026）；100 轮对话 20 轮内准确率 0.6→0.1，求解器验证的状态摘要保持高出 0.52–0.59；一致性/漂移指标全无预警。/ Pre-registered studies: accumulated history silently lowers accuracy (Holm-adjusted p≤0.026); accuracy falls 0.6→0.1 within 20 turns with full history while a solver-verified state summary keeps it 0.52–0.59 higher; process metrics give no early warning. |

### 8. Self-Evolving Agents & Automated Research · 自进化智能体与自动化科研（12 篇 / 12 papers）

| 排名 Rank | 论文 Paper | 类型 Type | 亮点与理由 / Highlights & Reason |
|---|---|---|---|
| 1 | [[2611.16409]] Experience-Handoff RL for Recursive Self-Improvement (ACE-RL) · 经验交接强化学习 | method 方法 | 用"候选 playbook 交给全新 rollout + 任务验证器打分"把写交接经验变成可训练行为；算力对齐下 4 基准 RSI@3 全面超 GRPO/PPO/ERL（MBPP 0.987 vs 0.820）。/ Scores each candidate playbook with a fresh actor rollout under the benchmark verifier, making handoff-writing itself trainable; compute-matched RSI@3 beats GRPO/PPO/ERL across 4 benchmarks (MBPP 0.987 vs 0.820). ⭐ |
| 2 | [[2611.13524]] The RSI Tax · 递归自我改进的代价税 | analysis 分析 | 6 方法 × 2 LLM 的端到端记账：有界笔记基线在 65.6–71.0% 平均 token 节省下匹配/超过 Meta-Harness、EvoSkill、RRSI；验证占税额 74.8–93.6%。/ End-to-end accounting over continual task streams: a bounded-notes baseline matches/exceeds three RSI systems at 65.6–71.0% mean token savings; verification is 74.8–93.6% of the tax. |
| 3 | [[2611.19841]] Asking the Right Question Is Key to AI Discovery · 问对问题才是 AI 发现的关键 | analysis 分析 | 32 次闭环试验（数据中略去窄峰）：两个旗舰模型落进峰区采样少于随机，最紧跟模型分歧的智能体 32/32 错过峰值；尽早探测未测空隙才能发现。/ 32 closed-loop trials with a peak omitted from starting data: two flagship models sample inside the peak region less often than random, and the most disagreement-following agent missed it in 32/32 trials. |
| 4 | [[2611.19230]] CompoundingKernel: Self-Improving from Zero to First · 从零到第一的复合式内核搜索 | system 系统 | LLM 控制器 + 逐问题内核谱系（正确性由模型外判定）+ 千级并行：2026-10-27 起居 SOL-ExecBench 三榜第一，209 题均 4.40× 于参考。/ An LLM controller over a per-problem kernel archive with lineage and external correctness: #1 on SOL-ExecBench L1/L2/Quantization boards since 2026-10-27, 4.40× faster than reference over 209 problems. |
| 5 | [[2611.12109]] SkillDuet: Co-Evolving Models and Skills · 技能与模型双共演化 | method 方法 | 响应漂移的 Strength 排序 + 周期性全局整固引导在线蒸馏：Qwen3-4B ALFWorld 98.57% / WebShop 92.97%，超匹配基线 +2.86/+5.47 pts。/ Response-shift-based Strength ranking + periodic global consolidation guiding on-policy distillation: 98.57% ALFWorld / 92.97% WebShop, +2.86/+5.47 pts over matched baselines. |
| 6 | [[2611.13336]] Veritas: A Verifier Generation Harness · 验证器生成装置 | system 系统 | 证据头 + 未言明领域规则库 + 自改进撰写原则；模型固定时，生成验证器在全部 4 个执行评分基准上比 7 个其他装置更吻合官方判定。/ Evidence headers, unstated-domain-rule library and self-improvement-refined authoring principles; with the model fixed, generated verifiers agree with certified verdicts better than 7 other harnesses on all 4 execution-scored benchmarks. |
| 7 | [[2611.15276]] Verify by Doing · 以行验证：执行与评测共演化 | method 方法 | 工具检视评测 + 比较审阅的 Actor/Evaluator 共演化，无外部反馈下 AutomationBench/tau3 Banking/GDPval +3.3/+4.1/+2.3 pp。/ Co-evolved Actor/Evaluator harnesses with tool-inspecting evaluation and comparative review: +3.3/+4.1/+2.3pp over the strongest no-feedback baselines. |
| 8 | [[2611.14844]] AutoAssumption: Searching over Assumptions · 在假设空间搜索 ML-系统算法 | method 方法 | 89 个算法形式化为 Lean 检查的证明图，假设松弛搜索产出 SOTA KV 逐出与剪枝（4 个 LLaMA 上 13 选 1 最低困惑度）。/ 89 ML-systems algorithms formalized as Lean-checked proof graphs; assumption-relaxation search yields SOTA KV-cache eviction and pruning (lowest perplexity of 13 on 4 LLaMA models). |
| 9 | [[2611.18856]] Self-Improvement Memory Enables Continual RSI · 自改记忆支撑持续自我改进 | method 方法 | 按"复现问题"分组编辑（含理由与结果）：10 对编码运行上比仅续跑 harness 高 +2.36 pts（p=0.003）。/ Groups edits by recurring problem with rationale and outcomes: +2.36 pts over harness-only continuation across 10 paired coding runs (p=0.003). |
| 10 | [[2611.13143]] Autonomous Optimization of Numerical Algorithms (AIOA) · 原子模拟数值算法的自主优化 | system 系统 | 不可篡改验证器守护的编码智能体改进环：六个核快 22–24×（vs NumPy/SciPy），优化器力评估次数比 L-BFGS 少 3.1–3.4×；两个组件文献未见。/ A coding-agent loop guarded by unalterable verifiers applied to ASE: six kernels 22–24× faster than NumPy/SciPy, 3.1–3.4× fewer force evaluations than L-BFGS; two components not found in the literature. |
| 11 | [[2611.12552]] SciMARS: Multi-Agent Recursive Self-Improvement for Scientific Discovery · 多智能体递归自改的闭环科研 | system 系统 | 组件编辑器自适应 harness + 共享证据图：Autonomous Science Bench 12/18 vs 基线 8/18（GPT-6-Astra），ScienceAgentBench 14/38 vs 11/38。/ Recursive harness adaptation via component editors + a shared evidence graph: Autonomous Science Bench 12/18 vs 8/18 base, ScienceAgentBench 14/38 vs 11/38. |
| 12 | [[2611.12762]] Sage-Taiyi: A Metacognitive Architecture for Scientific Discovery · 元认知科学发现架构 | system 系统 | 元认知监控/控制修订证据、假设与开放问题：Taiyi-Bench 全部 8 项指标第一（Overall 54.0 vs AI Scientist-v2 的 47.9）；专家指导验证含钴羰基化产率追踪至 84%。/ Metacognitive monitoring/control revising evidence, assumptions and open questions: first on all 8 Taiyi-Bench metrics (Overall 54.0 vs 47.9 for AI Scientist-v2); expert-guided validations include cobalt carbonylation yield traced to 84%. |

## All Papers

> 全部 97 篇入选论文总索引（按方向分组、组内按排名；与上表完全一致）。/ Complete index of all 97 selected papers, grouped by area, ranked within each area — identical to the topic tables above.

**LLM Training Stability & Observability · LLM 训练稳定性与可观测性（7 篇 / papers）**

| # | 论文 Paper | 方向 Area | 排名 Rank | 类型 Type |
|---|---|---|---|---|
| 1 | [[2611.13393]] Plumbline: When the Loss Lies · 损失在说谎时的训练正确性校验 | LLM 训练稳定性与可观测性 LLM Training Stability & Observability | 1 | 系统 System |
| 2 | [[2611.17876]] Delayed Effects of Temporary Weight Decay in Muon Pretraining · Muon 预训练中临时权重衰减的延迟效应 | LLM 训练稳定性与可观测性 LLM Training Stability & Observability | 2 | 分析 Analysis |
| 3 | [[2611.12729]] KiteNorm: Variance Regularisation for Stable Post-LN Transformers · 稳定 Post-LN 的方差正则 | LLM 训练稳定性与可观测性 LLM Training Stability & Observability | 3 | 方法 Method |
| 4 | [[2611.19413]] PMR: MoE Routing with Shared Prototypes and Congestion Pricing · 共享原型与拥塞定价的 MoE 路由 | LLM 训练稳定性与可观测性 LLM Training Stability & Observability | 4 | 方法 Method |
| 5 | [[2611.13137]] Byzantine-Robust Muon · 拜占庭鲁棒的 Muon 正交化 | LLM 训练稳定性与可观测性 LLM Training Stability & Observability | 5 | 分析 Analysis |
| 6 | [[2611.17459]] Classification with Large-Step Gradient Descent · 大步长梯度下降的自稳定与收敛 | LLM 训练稳定性与可观测性 LLM Training Stability & Observability | 6 | 分析 Analysis |
| 7 | [[2611.16736]] On the Difficulty of Sequence-Level Supervised Learning · 序列级监督学习为何困难 | LLM 训练稳定性与可观测性 LLM Training Stability & Observability | 7 | 分析 Analysis |

**RL Post-Training Dynamics & Failures · RL 后训练动态与失败（8 篇 / papers）**

| # | 论文 Paper | 方向 Area | 排名 Rank | 类型 Type |
|---|---|---|---|---|
| 8 | [[2611.13218]] Wrong the Same Way: Cross-Prompt Sharing Both Suppresses and Amplifies Reward Hacking in RLVR · RLVR 中跨提示参数共享双向改变作弊 | RL 后训练动态与失败 RL Post-Training Dynamics & Failures | 1 | 分析 Analysis |
| 9 | [[2611.15779]] Honesty Is a Race · 诚实是一场赛跑 | RL 后训练动态与失败 RL Post-Training Dynamics & Failures | 2 | 分析 Analysis |
| 10 | [[2611.12865]] Shortcuts and Boundaries: Verifiable RL Misalignment · 可验证 RL 的捷径与边界错位 | RL 后训练动态与失败 RL Post-Training Dynamics & Failures | 3 | 分析 Analysis |
| 11 | [[2611.15493]] The Illusion of Diversity: Effective Entropy · 多样性的错觉：有效熵对齐探索 | RL 后训练动态与失败 RL Post-Training Dynamics & Failures | 4 | 方法 Method |
| 12 | [[2611.15717]] Outside the Purview of the Reward · 奖励视野之外的多语能力漂移 | RL 后训练动态与失败 RL Post-Training Dynamics & Failures | 5 | 分析 Analysis |
| 13 | [[2611.14467]] A Theory of Policy Optimization: Coverage Collapse and Reference Resets · 策略优化的覆盖坍缩与参考重置理论 | RL 后训练动态与失败 RL Post-Training Dynamics & Failures | 6 | 分析 Analysis |
| 14 | [[2611.12728]] Safe RL for Multi-Turn Clinical Agents · 多轮临床智能体的安全 RL | RL 后训练动态与失败 RL Post-Training Dynamics & Failures | 7 | 分析 Analysis |
| 15 | [[2611.14683]] Trait Hitchhiking in LLM Post-Training · 后训练中的性状搭便车 | RL 后训练动态与失败 RL Post-Training Dynamics & Failures | 8 | 分析 Analysis |

**LLM Hidden States & Interpretability · LLM 隐藏状态与可解释性（25 篇 / papers）**

| # | 论文 Paper | 方向 Area | 排名 Rank | 类型 Type |
|---|---|---|---|---|
| 16 | [[2611.13548]] Massive Activations Confound Sparse Autoencoders · 巨大激活污染稀疏自编码器 | LLM 隐藏状态与可解释性 LLM Hidden States & Interpretability | 1 | 分析 Analysis |
| 17 | [[2611.20148]] Centered Ablation · 中心化消融的闭式修复 | LLM 隐藏状态与可解释性 LLM Hidden States & Interpretability | 2 | 方法 Method |
| 18 | [[2611.14996]] Breaking Bad: "Going Badly" Activations Drive Reward Hacking · "进展糟糕"激活驱动奖励作弊 | LLM 隐藏状态与可解释性 LLM Hidden States & Interpretability | 3 | 分析 Analysis |
| 19 | [[2611.12675]] Interpretability Is Not Model-Specific · 可解释性不必按模型重做 | LLM 隐藏状态与可解释性 LLM Hidden States & Interpretability | 4 | 分析 Analysis |
| 20 | [[2611.13543]] Sanity Checks for Attention Surgery · 注意力手术的 sanity check | LLM 隐藏状态与可解释性 LLM Hidden States & Interpretability | 5 | 分析 Analysis |
| 21 | [[2611.14942]] Emergent Vision-Shaped Thinking in Text-Only Reasoning · 文本推理中涌现的视觉形思维 | LLM 隐藏状态与可解释性 LLM Hidden States & Interpretability | 6 | 分析 Analysis |
| 22 | [[2611.19499]] Do Probing and Steering Favor the Same Directions? · 探针与转向是否偏好同一方向 | LLM 隐藏状态与可解释性 LLM Hidden States & Interpretability | 7 | 分析 Analysis |
| 23 | [[2611.13885]] Are Causal Neuron Circuits Unique and Transferable? · 因果神经元回路是否唯一且可迁移 | LLM 隐藏状态与可解释性 LLM Hidden States & Interpretability | 8 | 分析 Analysis |
| 24 | [[2611.17297]] Goal Encoding in LLMs · LLM 中的目标编码 | LLM 隐藏状态与可解释性 LLM Hidden States & Interpretability | 9 | 分析 Analysis |
| 25 | [[2611.15267]] A Closer Look at Language Model Introspection · 再看模型内省 | LLM 隐藏状态与可解释性 LLM Hidden States & Interpretability | 10 | 分析 Analysis |
| 26 | [[2611.19176]] A Bag of Concepts? Role-Filler Binding · 可言语化工作区是否绑定角色-填充 | LLM 隐藏状态与可解释性 LLM Hidden States & Interpretability | 11 | 分析 Analysis |
| 27 | [[2611.14168]] Representational Atoms in Neural Networks · 神经网络中的表征原子 | LLM 隐藏状态与可解释性 LLM Hidden States & Interpretability | 12 | 方法 Method |
| 28 | [[2611.19403]] Confidence Without Cause: Physics-Shortcut Sensitivity · 无因果的自信：物理捷径敏感度 | LLM 隐藏状态与可解释性 LLM Hidden States & Interpretability | 13 | 分析 Analysis |
| 29 | [[2611.11892]] When Answer Decodability Is Not a Decision · 答案可解码 ≠ 已做决定 | LLM 隐藏状态与可解释性 LLM Hidden States & Interpretability | 14 | 分析 Analysis |
| 30 | [[2611.12206]] A Geometric Invariant of Attention Predicts Head Specialization · 预测头特化的注意力几何不变量 | LLM 隐藏状态与可解释性 LLM Hidden States & Interpretability | 15 | 分析 Analysis |
| 31 | [[2611.18514]] Can Mechanistic Interpretability Explain LLM Agent Failures? · MI 能否解释智能体失败 | LLM 隐藏状态与可解释性 LLM Hidden States & Interpretability | 16 | 分析 Analysis |
| 32 | [[2611.19848]] A phase diagram for training and inference · 训练与推理的相图 | LLM 隐藏状态与可解释性 LLM Hidden States & Interpretability | 17 | 分析 Analysis |
| 33 | [[2611.13270]] What Drives Emergence of Symbolic Mechanisms? · 符号机制涌现的驱动因素 | LLM 隐藏状态与可解释性 LLM Hidden States & Interpretability | 18 | 分析 Analysis |
| 34 | [[2611.19826]] Where Is Rank-1 DiM Refusal Intervenable in Multimodal LM Derivatives? · 多模态衍生模型的拒答可干预位置 | LLM 隐藏状态与可解释性 LLM Hidden States & Interpretability | 19 | 分析 Analysis |
| 35 | [[2611.17461]] Tracing Knowledge and Reasoning in LLM · 追踪 LLM 中的知识与推理 | LLM 隐藏状态与可解释性 LLM Hidden States & Interpretability | 20 | 分析 Analysis |
| 36 | [[2611.18089]] Deep Latents, Long Memory · 潜变量持续性与激活长记忆 | LLM 隐藏状态与可解释性 LLM Hidden States & Interpretability | 21 | 分析 Analysis |
| 37 | [[2611.16190]] When Can an Interpretability Claim Be Trusted? · 可解释性结论何时可信 | LLM 隐藏状态与可解释性 LLM Hidden States & Interpretability | 22 | 分析 Analysis |
| 38 | [[2611.18272]] From Bytes to Behavior: Request-Level Attribution from Live GPU Hidden States · 从活动 GPU 隐状态做请求级归因 | LLM 隐藏状态与可解释性 LLM Hidden States & Interpretability | 23 | 方法 Method |
| 39 | [[2611.18274]] Right Token, Right Time: Trajectory-Aware Activation Steering · 按轨迹感知的激活转向 | LLM 隐藏状态与可解释性 LLM Hidden States & Interpretability | 24 | 方法 Method |
| 40 | [[2611.19075]] The Geometry of Conceptors in Neural-Activation Spaces · 概念子的几何学 | LLM 隐藏状态与可解释性 LLM Hidden States & Interpretability | 25 | 分析 Analysis |

**Inference Reliability & SDC Detection · 推理可靠性与 SDC 检测（10 篇 / papers）**

| # | 论文 Paper | 方向 Area | 排名 Rank | 类型 Type |
|---|---|---|---|---|
| 41 | [[2611.12127]] Lost in Rounding · bf16 循环状态让混合推理模型想更久 | 推理可靠性与 SDC 检测 Inference Reliability & SDC Detection | 1 | 分析 Analysis |
| 42 | [[2611.17634]] A Unified Device-Level Physical Framework for DRAM Read Disturbance · DRAM 读扰动的统一器件级物理框架 | 推理可靠性与 SDC 检测 Inference Reliability & SDC Detection | 2 | 分析 Analysis |
| 43 | [[2611.15469]] HARE: Fast Read Disturbance Threshold Profiling · 快速读扰动阈值画像 | 推理可靠性与 SDC 检测 Inference Reliability & SDC Detection | 3 | 方法 Method |
| 44 | [[2611.13730]] Deterministic, Reproducible Inference in Exact Integer Arithmetic · 精确整数算术的确定性可复现推理 | 推理可靠性与 SDC 检测 Inference Reliability & SDC Detection | 4 | 系统 System |
| 45 | [[2611.19135]] How Much Determinism Can Fine-Tuning Buy? · 微调能买到多少确定性 | 推理可靠性与 SDC 检测 Inference Reliability & SDC Detection | 5 | 方法 Method |
| 46 | [[2611.14083]] Sable: Small-Field Sumcheck for Bit-Exact Inference · 小域 sumcheck 证明逐位精确推理 | 推理可靠性与 SDC 检测 Inference Reliability & SDC Detection | 6 | 系统 System |
| 47 | [[2611.14051]] Can KV Cache Be Reused Across Model Updates? · 模型更新后 KV 缓存能否复用 | 推理可靠性与 SDC 检测 Inference Reliability & SDC Detection | 7 | 分析 Analysis |
| 48 | [[2611.14209]] Breakdown of Autoregressive Multi-Step Reasoning Under Attention Head Dropout · 集中 vs 扩散注意力头失效 | 推理可靠性与 SDC 检测 Inference Reliability & SDC Detection | 8 | 分析 Analysis |
| 49 | [[2611.19165]] From Sensors to Silicon: Causal Cross-Layer Self-Healing Edge AI · 传感器到硅片的因果跨层自愈边缘 AI | 推理可靠性与 SDC 检测 Inference Reliability & SDC Detection | 9 | 系统 System |
| 50 | [[2611.15842]] Fewer Expert Transfers Without Changing Routing · 不改路由的专家逐出 | 推理可靠性与 SDC 检测 Inference Reliability & SDC Detection | 10 | 分析 Analysis |

**Reliability under Extreme Performance Optimization · 极致性能优化下的可靠性（20 篇 / papers）**

| # | 论文 Paper | 方向 Area | 排名 Rank | 类型 Type |
|---|---|---|---|---|
| 51 | [[2611.15671]] The Noise Floor of a Quantization Comparison · 量化对比的噪声底 | 极致性能优化下的可靠性 Reliability under Extreme Performance Optimization | 1 | 分析 Analysis |
| 52 | [[2611.12634]] Second-Order Linear Response Predicts Quantization Mismatch · 二阶线性响应能否预测量化失配 | 极致性能优化下的可靠性 Reliability under Extreme Performance Optimization | 2 | 分析 Analysis |
| 53 | [[2611.11780]] Planners Exploit Deterministic Error: Dithered Low-Bit World Models · 规划器利用确定性误差：抖动低位世界模型 | 极致性能优化下的可靠性 Reliability under Extreme Performance Optimization | 3 | 分析 Analysis |
| 54 | [[2611.12832]] What the Loss Curve Misses: FP4 Slows Rare-Fact Acquisition · FP4 拖慢罕见事实习得 | 极致性能优化下的可靠性 Reliability under Extreme Performance Optimization | 4 | 分析 Analysis |
| 55 | [[2611.17501]] Microscaling Formats for R&R Models · 检索与排序模型的微缩放格式 | 极致性能优化下的可靠性 Reliability under Extreme Performance Optimization | 5 | 分析 Analysis |
| 56 | [[2611.13410]] SteerDistill: Closed-Loop Teacher Steering for Quantized Agents · 闭环教师引导量化蒸馏 | 极致性能优化下的可靠性 Reliability under Extreme Performance Optimization | 6 | 方法 Method |
| 57 | [[2611.18511]] Numerical Issues of Divergences Between Nearly Equal Distributions · 近等分布散度的数值问题 | 极致性能优化下的可靠性 Reliability under Extreme Performance Optimization | 7 | 分析 Analysis |
| 58 | [[2611.13879]] SFU-Sim: Bit-Exact Reverse Engineering of NVIDIA MUFU · NVIDIA 特殊函数单元的逐位逆向 | 极致性能优化下的可靠性 Reliability under Extreme Performance Optimization | 8 | 系统 System |
| 59 | [[2611.19722]] MIAO: Microscaling Intermediate Accumulation Optimization · 微缩放中间累加优化 | 极致性能优化下的可靠性 Reliability under Extreme Performance Optimization | 9 | 方法 Method |
| 60 | [[2611.18769]] Gradient-Guided Hardware-Native MIXFP4 · 梯度引导的硬件原生 MIXFP4 | 极致性能优化下的可靠性 Reliability under Extreme Performance Optimization | 10 | 方法 Method |
| 61 | [[2611.16502]] SignRot: Outlier-Aware Sign-Adjusted Rotation · 符号调整旋转对抗巨大离群 | 极致性能优化下的可靠性 Reliability under Extreme Performance Optimization | 11 | 方法 Method |
| 62 | [[2611.17605]] Choosing Quantized Code LLMs by File Size and Energy per Solved Task · 按文件体积与每任务能耗选量化代码模型 | 极致性能优化下的可靠性 Reliability under Extreme Performance Optimization | 12 | 分析 Analysis |
| 63 | [[2611.15569]] TraceKV: Policy-Preserving Low-Rank KV Compression · 保策略的低秩 KV 压缩 | 极致性能优化下的可靠性 Reliability under Extreme Performance Optimization | 13 | 方法 Method |
| 64 | [[2611.12054]] Low-Rank Low Precision Training of Gaussian Processes · 高斯过程的低秩低精度训练 | 极致性能优化下的可靠性 Reliability under Extreme Performance Optimization | 14 | 方法 Method |
| 65 | [[2611.16426]] SoScale: Second-Order Scale Search for FP4 · FP4 的二阶尺度码搜索 | 极致性能优化下的可靠性 Reliability under Extreme Performance Optimization | 15 | 方法 Method |
| 66 | [[2611.16561]] SPARC: Photonic Matrix Multiplication via Representative Vectors · 代表向量的光子矩阵乘 | 极致性能优化下的可靠性 Reliability under Extreme Performance Optimization | 16 | 方法 Method |
| 67 | [[2611.19944]] Exhaustive Evaluation of Fixed-Point Reciprocal Architectures · 定点倒数架构的穷举评估 | 极致性能优化下的可靠性 Reliability under Extreme Performance Optimization | 17 | 分析 Analysis |
| 68 | [[2611.15231]] TQIR: Trellis Quantization with Integer Reconstruction · 整数重构的网格量化 | 极致性能优化下的可靠性 Reliability under Extreme Performance Optimization | 18 | 方法 Method |
| 69 | [[2611.16478]] One Model, Two Precisions · 量化副本分歧能否预示错误 | 极致性能优化下的可靠性 Reliability under Extreme Performance Optimization | 19 | 分析 Analysis |
| 70 | [[2611.14924]] Edge-Native Multimodal RAG on Consumer GPUs · 消费级 GPU 上的边缘原生多模态 RAG | 极致性能优化下的可靠性 Reliability under Extreme Performance Optimization | 20 | 系统 System |

**Compute Infrastructure for Large-Scale ML · 大规模 ML 计算基础设施（10 篇 / papers）**

| # | 论文 Paper | 方向 Area | 排名 Rank | 类型 Type |
|---|---|---|---|---|
| 71 | [[2611.18956]] Supercharging Olmo-core for Efficient and Scalable MoE Training · 重构 Olmo-core 的可扩展 MoE 训练 | 大规模 ML 计算基础设施 Compute Infrastructure for Large-Scale ML | 1 | 系统 System |
| 72 | [[2611.13188]] One-Sided Expert-Parallel All-to-All over NVLink · NVLink 单侧专家并行 all-to-all | 大规模 ML 计算基础设施 Compute Infrastructure for Large-Scale ML | 2 | 方法 Method |
| 73 | [[2611.11857]] OverlapAdvisor: Overlap for Distributed MoE Serving · MoE 服务的算通重叠建模与自适应 | 大规模 ML 计算基础设施 Compute Infrastructure for Large-Scale ML | 3 | 系统 System |
| 74 | [[2611.18145]] Compiling Specialized GPU-Initiated Networking (Obaleth) · 编译 GPU 发起的专用水网络 | 大规模 ML 计算基础设施 Compute Infrastructure for Large-Scale ML | 4 | 系统 System |
| 75 | [[2611.15951]] Starscream: LLM Sharding on AMD Instinct with GPU Partitioning · 芯片 NUMA 下的 LLM 切分重想 | 大规模 ML 计算基础设施 Compute Infrastructure for Large-Scale ML | 5 | 系统 System |
| 76 | [[2611.13412]] Bursts That Outlast Themselves: Persistent Degradation in Prefix-Cached Agent Serving · 前缀缓存智能体服务的亚稳态持续退化 | 大规模 ML 计算基础设施 Compute Infrastructure for Large-Scale ML | 6 | 分析 Analysis |
| 77 | [[2611.13293]] Decode Token Parallelism · 解码 token 并行的分布式注意力 | 大规模 ML 计算基础设施 Compute Infrastructure for Large-Scale ML | 7 | 系统 System |
| 78 | [[2611.17857]] Fuse-All MoE Inference Kernel with Load Balancing on TPUs · TPU 上的全融合 MoE 推理核 | 大规模 ML 计算基础设施 Compute Infrastructure for Large-Scale ML | 8 | 系统 System |
| 79 | [[2611.16219]] GC-MoE on SM120: Warp-Level FP8xFP4 on Consumer Blackwell · 消费级 Blackwell 上的 FP8xFP4 MoE | 大规模 ML 计算基础设施 Compute Infrastructure for Large-Scale ML | 9 | 系统 System |
| 80 | [[2611.14681]] Together Compiler: Continual Compilation for AI Inference · AI 推理的持续编译 | 大规模 ML 计算基础设施 Compute Infrastructure for Large-Scale ML | 10 | 系统 System |

**Agent & Pipeline Silent Failures · 智能体与流水线静默失败（5 篇 / papers）**

| # | 论文 Paper | 方向 Area | 排名 Rank | 类型 Type |
|---|---|---|---|---|
| 81 | [[2611.13254]] Dependable Long-Horizon LLM Agents: A Trajectory-Centered Empirical Study · 长程多智能体失败的轨迹中心实证 | 智能体与流水线静默失败 Agent & Pipeline Silent Failures | 1 | 分析 Analysis |
| 82 | [[2611.15543]] isloss: A Rule-Based Oracle for Silent Information Loss · 检测 API 翻译层静默信息丢失 | 智能体与流水线静默失败 Agent & Pipeline Silent Failures | 2 | 方法 Method |
| 83 | [[2611.19886]] Recovery Gone Too Far: Risky Fallback in LLM Agents · 修复过头：智能体的危险回退 | 智能体与流水线静默失败 Agent & Pipeline Silent Failures | 3 | 分析 Analysis |
| 84 | [[2611.19237]] Auditable Authorization for LLM Agents · 智能体授权的可审计性 | 智能体与流水线静默失败 Agent & Pipeline Silent Failures | 4 | 分析 Analysis |
| 85 | [[2611.20071]] The Silent Cost of Conversation History in LLM Reasoning · 对话历史的静默代价 | 智能体与流水线静默失败 Agent & Pipeline Silent Failures | 5 | 分析 Analysis |

**Self-Evolving Agents & Automated Research · 自进化智能体与自动化科研（12 篇 / papers）**

| # | 论文 Paper | 方向 Area | 排名 Rank | 类型 Type |
|---|---|---|---|---|
| 86 | [[2611.16409]] Experience-Handoff RL for Recursive Self-Improvement (ACE-RL) · 经验交接强化学习 | 自进化智能体与自动化科研 Self-Evolving Agents & Automated Research | 1 | 方法 Method |
| 87 | [[2611.13524]] The RSI Tax · 递归自我改进的代价税 | 自进化智能体与自动化科研 Self-Evolving Agents & Automated Research | 2 | 分析 Analysis |
| 88 | [[2611.19841]] Asking the Right Question Is Key to AI Discovery · 问对问题才是 AI 发现的关键 | 自进化智能体与自动化科研 Self-Evolving Agents & Automated Research | 3 | 分析 Analysis |
| 89 | [[2611.19230]] CompoundingKernel: Self-Improving from Zero to First · 从零到第一的复合式内核搜索 | 自进化智能体与自动化科研 Self-Evolving Agents & Automated Research | 4 | 系统 System |
| 90 | [[2611.12109]] SkillDuet: Co-Evolving Models and Skills · 技能与模型双共演化 | 自进化智能体与自动化科研 Self-Evolving Agents & Automated Research | 5 | 方法 Method |
| 91 | [[2611.13336]] Veritas: A Verifier Generation Harness · 验证器生成装置 | 自进化智能体与自动化科研 Self-Evolving Agents & Automated Research | 6 | 系统 System |
| 92 | [[2611.15276]] Verify by Doing · 以行验证：执行与评测共演化 | 自进化智能体与自动化科研 Self-Evolving Agents & Automated Research | 7 | 方法 Method |
| 93 | [[2611.14844]] AutoAssumption: Searching over Assumptions · 在假设空间搜索 ML-系统算法 | 自进化智能体与自动化科研 Self-Evolving Agents & Automated Research | 8 | 方法 Method |
| 94 | [[2611.18856]] Self-Improvement Memory Enables Continual RSI · 自改记忆支撑持续自我改进 | 自进化智能体与自动化科研 Self-Evolving Agents & Automated Research | 9 | 方法 Method |
| 95 | [[2611.13143]] Autonomous Optimization of Numerical Algorithms (AIOA) · 原子模拟数值算法的自主优化 | 自进化智能体与自动化科研 Self-Evolving Agents & Automated Research | 10 | 系统 System |
| 96 | [[2611.12552]] SciMARS: Multi-Agent Recursive Self-Improvement for Scientific Discovery · 多智能体递归自改的闭环科研 | 自进化智能体与自动化科研 Self-Evolving Agents & Automated Research | 11 | 系统 System |
| 97 | [[2611.12762]] Sage-Taiyi: A Metacognitive Architecture for Scientific Discovery · 元认知科学发现架构 | 自进化智能体与自动化科研 Self-Evolving Agents & Automated Research | 12 | 系统 System |
---

## 校验 / Verification

- 本文件列出的论文总数 / Papers listed in this file: **97**；`filtered_papers.json` 的 `total_selected` = **97**（评估 2,588 篇）。两者一致，无缺漏。/ Both counts agree — no discrepancy.
- 必读 8 篇全部来自 `stars.json` 中 `star: true` 的条目（每个方向恰好 1 篇，符合"每方向至多 2 篇"约束），理由与注意事项均引自全文精读评审；未做任何重新评星。/ All 8 Must Reads come from the `star: true` entries of `stars.json` (exactly one per area, satisfying the at-most-2-per-area rule); no re-starring was performed.
- 97 篇论文的中文总结文件（`<arxiv_id>.md`）均已在日期文件夹中生成。/ All 97 per-paper summary files exist in the date folder.







