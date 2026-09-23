---
title: "Daily Paper Overview — 2026-08-06"
date: 2026-08-06
tags: [arxiv-daily, llm, agents, self-evolution, interpretability, quantization, learning-theory]
papers: 40
---

# 每日论文速览 / Daily Paper Overview — 2026-08-06

> 本日共精选 **40** 篇论文，覆盖 LLM 智能体自进化与安全、推理可解释性、VLM 读图可靠性、模型压缩、学习理论、系统基础设施等方向。智能体技能系统的"自进化—污染—门控"是今日最密集的主题脉络。

> **40 papers** curated today. Dominant theme: agent skill systems — self-evolution, contamination/poisoning, and gating. Also notable: LLM reasoning interpretability, VLM figure-reading reliability, compression/quantization, and several tight learning-theory results.

---

## 今日必读 / Must Read Today

### 1. [[2608.05810]] — When Self-Evolution Backfires: Pre-Commit Gating against Skill Contamination

> **推荐理由：** 首次揭示自进化智能体的"能力—污染相变"——技能池超过临界规模后性能反而崩塌（62%→50%），且因衍生技能血缘传递而不可逆。提出的 VaG 三级预提交门控把 pass@1 单调提升至 72%，技能池缩小 5 倍并跨模型正向迁移。
>
> **Why read:** First to expose a "capability–contamination tipping point" in self-evolving agents: ungated skill accumulation peaks then collapses to 50% as descendants inherit flawed reasoning. The Verifier-as-Gatekeeper (VaG) pre-commit gate lifts pass@1 monotonically to 72% with a 5× smaller pool and positive cross-model transfer — a clean, deployable fix for a problem the field is just recognizing.

### 2. [[2608.06352]] — CalibForge: Adversarial Solver Calibration for Scaling Learnable Terminal Tasks

> **推荐理由：** 把终端任务构造建模为"作者—求解器"对抗循环，用多求解器分歧 + 强过弱失败对比信号把任务迭代修订到"可解但不被一致求解"的可学习区间。在 Terminal-Bench 2.0 上把 Qwen3-30B 从 7.87% 拉到 32.58%（+24.71pp），并显著迁移到 SWE-bench Pro 与 Doc2Repo，消融干净地隔离了校准而非数据量的贡献。
>
> **Why read:** Reframes terminal-task construction as an adversarial author–solver loop calibrated to a "solvable but not uniformly solved" learnable zone. Ablations cleanly isolate the gain to calibration (contrastive +8.62pp, multi-solver +6.74pp) over trajectory volume, and the +24.71pp Terminal-Bench lift transfers to SWE-bench Pro (+27.68pp) and Doc2Repo (+30.04pp).

### 3. [[2608.05670]] — When Does Consensus Mean Correctness? Measuring Agreement-Accuracy Coupling

> **推荐理由：** 构建 RENDEQ 渲染等价基准精确度量"一致性—正确性"耦合，得出一个反直觉的负面结论：在 Qwen2.5-VL-7B 上用自身 K=8 多数共识做微调，准确率在全部 5 个复现 run 中反而下降——直接反驳了一篇已发表的正面结果。重绘优于重采样这一结论对 VLM 部署有直接指导意义。
>
> **Why read:** The RENDEQ benchmark isolates agreement–accuracy coupling with programmatic ground truth. The headline negative result — fine-tuning a VLM on its own majority consensus *inverts* accuracy in all 5 replication runs — directly contradicts a published positive finding, and the "re-rendering beats resampling" result has immediate deployment implications.

---

## 按主题分类 / Papers by Topic

### 智能体技能系统与自进化 / Agent Skill Systems & Self-Evolution

| Paper | 一句话总结 / One-line Summary |
|-------|------|
| [[2608.05563]] | 轨迹投毒攻击：攻击者贡献约 10% 正常轨迹即可让自进化系统把恶意行为蒸馏进持久化技能，SkillClaw 上 91% 嵌入率。/ Trajectory-poisoning attack: ~10% benign-looking trajectories get the evolver to embed malicious behavior into a persistent skill (91% embedding rate on SkillClaw). |
| [[2608.05604]] | SkillZip 把技能库重构为带契约的 section 级过程图，可逆压缩 + 预算水合，ALFWorld +12.2pp，3.46× 压缩比。/ SkillZip reframes skill libraries as contract-bearing procedural graphs with reversible macro compression and budget-bounded hydration (+12.2pp ALFWorld, 3.46× compression). |
| [[2608.05628]] | SkillHEX 用可证伪假设驱动自验证充当稠密语义梯度，PUCT 式补丁树搜索在 SkillsBench 超越人工技能。/ SkillHEX turns falsifiable failure hypotheses into executable self-verifier tests as dense "semantic gradients," steering PUCT-style patch-tree search past human-curated skills. |
| [[2608.05810]] | 揭示自进化"能力—污染相变"，VaG 三级预提交门控把 Terminal-Bench 2 单调提升至 72% pass@1 并跨模型迁移。/ Exposes the capability–contamination tipping point; the VaG pre-commit gate lifts Terminal-Bench 2 to 72% pass@1 monotonically and transfers across backbones. |
| [[2608.05987]] | AgentOPSD 把 token 级师生差聚合为轮级证据，递归贝叶斯信念重塑优势，ALFWorld 89.1%，步数衰减仅 -0.54/步。/ AgentOPSD aggregates token-level teacher–student gaps into turn-level evidence for recursive Bayesian belief that reshapes sequence-level advantages (ALFWorld 89.1%, -0.54/step decay). |
| [[2608.06153]] | GSE 用技能关系图与聚类合并把编码 Agent 技能进化重构为全局优化，F1 最高 +93.8%。/ GSE reframes coding-agent skill evolution as global optimization via a Skill Relation Graph + cluster consolidation (up to +93.8% F1). |
| [[2608.06352]] | CalibForge 对抗式作者—求解器循环合成终端任务，Terminal-Bench 2.0 +24.71pp 并迁移到 SWE-bench Pro。/ CalibForge's adversarial author–solver loop synthesizes terminal tasks in a learnable zone (+24.71pp Terminal-Bench 2.0, transfers to SWE-bench Pro). |

### 智能体可靠性、调试与失败归因 / Agent Reliability, Debugging & Failure Attribution

| Paper | 一句话总结 / One-line Summary |
|-------|------|
| [[2608.05490]] | 为仅用成功轨迹的智能体失败归因方法建立完整统计理论，证明可归因误差下界受表示维度而非数据量约束。/ Builds full statistical theory for success-only step-level failure attribution; the attributable-error floor is bounded by representation dimension, not data volume. |
| [[2608.06346]] | TRAJDEBUG 三阶段错误生命周期追踪，在 486 条轨迹基准上精确步定位 34.11%，长轨迹优势更明显。/ TRAJDEBUG's three-stage error-lifecycle tracing reaches 34.11% exact-step accuracy on a 486-trajectory benchmark, strongest on long trajectories. |
| [[2608.05906]] | MERIT 因果跨查询记忆做 Text-to-SQL 修复，Spider +3.45pp，但 BIRD 证据较弱且与无类型 Dynamic RAG 难区分。/ MERIT's causally time-restricted memory lifts Spider +3.45pp, but BIRD evidence is weak and it cannot reliably beat untyped Dynamic RAG. |

### 智能体基准与评估 / Agent Benchmarks & Evaluation

| Paper | 一句话总结 / One-line Summary |
|-------|------|
| [[2608.06329]] | 无参考 LLM-judge 框架从任务一致性、复杂度、策略覆盖评估对话 Agent 基准，Airline 排序分 1.0。/ A reference-free LLM-judge framework scores conversational-agent benchmarks on consistency/complexity/policy-coverage (Airline ordering score 1.0). |
| [[2608.06144]] | FinEvo-Bench 纵向金融 Agent 基准，120 任务 + 全局交错流协议度量跨任务经验复用，演化得分 +9.33–19.37pp。/ FinEvo-Bench longitudinally measures financial-agent self-evolution across 120 tasks with interleaved-stream + state-reset protocol (+9.33–19.37pp evolution gain). |
| [[2608.06301]] | HarnessOpt-Bench 评测 LLM 优化 Agent harness 的能力，优化器模型影响约为编码 harness 的 1.8 倍，Claude Opus 5 居首。/ HarnessOpt-Bench shows the optimizer model matters ~1.8× more than the coding harness; Claude Opus 5 is sole tier-1. |
| [[2608.05797]] | 跨 17 基准预测智能体任务难度，AUC 会掩盖糟糕估计，OOD Spearman ρ 仅 0.225，残差可揭示污染任务。/ Predicts agentic task difficulty across 17 benchmarks; AUC masks poor estimates, OOD ρ drops to 0.225, residuals flag contaminated tasks. |
| [[2608.05778]] | 冻结 prompt-side playbook 跨模型迁移研究：ALFWorld 有效（+23.6pp），TAU2-Bench 多重校正后仅 1/135 显著，128K 运行时偏移致成本膨胀。/ Frozen prompt-side playbook transfer helps on ALFWorld (+23.6pp) but largely fails TAU2-Bench and destabilizes under 32K→128K runtime shift. |

### LLM 推理与可解释性 / LLM Reasoning & Interpretability

| Paper | 一句话总结 / One-line Summary |
|-------|------|
| [[2608.05660]] | 三流式内部状态检测器叠加运动+区域+方向视图，OOD 推理选择准确率比位移 SOTA 高达 +12pp，仅 +0.31M 参数。/ Three-stream internal-state detector (motion+region+direction) lifts OOD reasoning selection by up to +12pp over displacement-only SOTA with only +0.31M params. |
| [[2608.05732]] | CircuitSteer 用 SAE 特征共激活 + 解码器方向对齐构造多层稠密干预向量，唯一在 8 个模型×数据集组合都有效且保流畅。/ CircuitSteer builds multi-layer dense steering vectors via SAE feature co-activation + decoder cosine-alignment; only method valid-fluent across all 8 model×dataset cells. |
| [[2608.05872]] | MACRO 把冻结 LLM 层执行建模为马尔可夫策略，GSM8K 把 Qwen3-1.7B 从 43.44% 提到 69.52%，搜索快 9.4×。/ MACRO rewrites frozen-LLM layer order as a Markov policy (Qwen3-1.7B GSM8K 43.44%→69.52%, search 9.4× faster). |
| [[2608.05726]] | 让 LLM 生成随机数测量潜在数字偏好并做 logit 修正，SummEval MSE 减半，STS-B Spearman 提升至 71.5。/ Mitigates LLM-judge bias by measuring latent number preference via RNG and applying logit-space correction (SummEval MSE halved, STS-B Spearman 71.5). |

### VLM 读图可靠性 / VLM Figure-Reading Reliability

| Paper | 一句话总结 / One-line Summary |
|-------|------|
| [[2608.05670]] | RENDEQ 基准精确度量一致性—正确性耦合，重绘优于重采样，自共识微调反而使准确率在 5 个 run 全下降。/ RENDEQ isolates agreement–accuracy coupling: re-rendering beats resampling, and self-consistency fine-tuning inverts accuracy in all 5 runs. |
| [[2608.05675]] | 证明 VLM 读图误差不可见当且仅当与编辑答案变换可交换，提出无需标注的 ECS 分数，AUROC 0.788→0.906。/ Proves a VLM error is invisible iff it commutes with the edit's answer-transform; label-free ECS lifts correctness-detection AUROC 0.788→0.906. |

### 不确定性与保形预测 / Uncertainty & Conformal Prediction

| Paper | 一句话总结 / One-line Summary |
|-------|------|
| [[2608.05995]] | 把不确定性统一为样本条件逐点后验风险，半合成 GP 基准显示即使预测准确也不保证可解耦，集成类最稳。/ Unifies uncertainty as pointwise posterior risk; semi-synthetic GP benchmark shows accurate prediction ≠ reliable disentanglement, ensembles most stable. |
| [[2608.06206]] | 为随机化局部保形预测给出已实现局部预测集的有限样本高概率界，覆盖误差与 oracle 长度误差一致受控。/ Proves finite-sample high-probability bounds for randomly localized conformal prediction on both conditional-coverage gap and oracle-relative length error. |

### 学习理论 / Learning Theory

| Paper | 一句话总结 / One-line Summary |
|-------|------|
| [[2608.06363]] | 构造性给出任意噪声下都达统计最优超额风险的二分类 PAC 学习器，匹配 Devroye–Györfi–Lugosi 下界，彻底解决不可知 PAC 样本复杂度。/ Constructive optimal agnostic PAC learner matching the DGL'96 minimax lower bound at every noise level, resolving agnostic PAC sample complexity. |
| [[2608.06337]] | 确定单调对手模型最优学习速率：d≥2 时 Θ((d/n)log(n/d))，比 i.i.d. 多不可消对数因子；d=1 保持 Θ(1/n)。/ Settles optimal rates under monotone adversaries: Θ((d/n)log(n/d)) for d≥2 (inherent log gap), Θ(1/n) preserved at d=1. |
| [[2608.06262]] | 有限分布条件查询下，交互式测试相对静态的最坏情况查询数增益恰好为 Θ(N²)，非指数节省。/ Under conditional queries, the worst-case adaptivity gap is exactly Θ(N²) — interaction saves a quadratic, not exponential, factor. |

### 模型压缩与量化 / Model Compression & Quantization

| Paper | 一句话总结 / One-line Summary |
|-------|------|
| [[2608.05499]] | APQF 由 LLM 智能体驱动的剪枝+混合精度量化流水线，计算量压到原始 BOP 的 5.6%–7.7%，ImageNet 比 GETA 高 17 个点。/ APQF: LLM-agent-driven pruning + mixed-precision quantization, compressing to 5.6–7.7% BOPs while beating GETA by 17 Top-1 points. |
| [[2608.06291]] | BaKron 把双边 Kronecker-Hessian GPTQ 复杂度降到 O(mn(m+n))，Llama-3-8B 2.81-bit PPL 11.9 vs GPTQ 53.47。/ BaKron accelerates two-sided Kronecker-Hessian adaptive rounding to O(mn(m+n)); Llama-3-8B 2.81-bit PPL 11.9 vs GPTQ's 53.47. |
| [[2608.06177]] | 二值激活网络的免重训阈值提前终止，VGG11 最深卷积省 86.6% 累加项仅降 0.37pp 精度。/ Retraining-free threshold early-stopping for binary-activation nets: removes 86.6% of deepest-conv accumulations for 0.37pp accuracy drop. |

### 机器遗忘 / Machine Unlearning

| Paper | 一句话总结 / One-line Summary |
|-------|------|
| [[2608.05783]] | GROM 把 LLM 遗忘建模为岭回归最小二乘，闭式解一次前向完成，比 SimNPO 快 180× 且对 4-bit 量化攻击鲁棒。/ GROM casts unlearning as closed-form ridge regression, ~180× faster than SimNPO and robust to the 4-bit quantization attack. |

### 高效进化与成本优化 / Efficient Evolution & Cost Optimization

| Paper | 一句话总结 / One-line Summary |
|-------|------|
| [[2608.05651]] | RelayEvolve 种群交接框架：廉价模型探索 + 强模型精修，12 个设定中 11 项最高均分，无需训练。/ RelayEvolve: training-free population handoff (cheap-model exploration → strong-model refinement), highest mean in 11/12 settings. |

### 系统与基础设施 / Systems & Infrastructure

| Paper | 一句话总结 / One-line Summary |
|-------|------|
| [[2608.05863]] | WitCert 异构注意力记忆可观测性契约平台，Lean 证明逐级打标，一层探针开销仅 -0.94% 吞吐，精确定位静默退化边界。/ WitCert runtime-observability platform with Lean-verified typed error contracts for heterogeneous attention memory; -0.94% throughput probe, localizes silent-corruption boundary. |
| [[2608.05944]] | 16×NVIDIA B300 双节点全参数微调 Qwen3-32B 工程报告：功率分诊表、负面结果、强扩展数据与 NCCL 死锁案例。/ Field report on 16×B300 full fine-tuning of Qwen3-32B: power triage table, negative results, strong-scaling data, and a worked NCCL deadlock case. |
| [[2608.06046]] | ML-for-ML 倡导网络侧与 ML 侧旋钮在同一 time-to-target-loss 下联合优化，解耦组合慢 1.13–1.42×。/ ML-for-ML advocates jointly tuning network-side and ML-side knobs under shared time-to-target-loss; decoupled composition is 1.13–1.42× slower. |

### 嵌入模型分析 / Embedding Model Analysis

| Paper | 一句话总结 / One-line Summary |
|-------|------|
| [[2608.05857]] | SQP 用 LLM 生成不同相关度合成查询学习跨嵌入模型相似度映射，跨模型呈 S 型非线性，跨维近无损。/ SQP learns cross-embedding similarity maps via LLM-generated synthetic queries; cross-model maps are sigmoidal nonlinear, cross-dimension near-lossless. |
| [[2608.05980]] | 9 个异构嵌入模型上简单变换器仅在共享架构/目标/池化的少数模型对有效，e5-large-v2 是硬异类，质疑潜在空间普适性。/ Across 9 embedding models, simple translators work only on architecturally similar pairs; e5-large-v2 is a hard outlier, challenging latent-space universality. |

### 科学机器学习与动力系统 / Scientific ML & Dynamical Systems

| Paper | 一句话总结 / One-line Summary |
|-------|------|
| [[2608.05702]] | SEAM 用有限层球把局部科学解释能否拼成全局自洽建模为可计算问题，即便所有局部 R²>0.999 也能检出全局不可容许。/ SEAM makes "can locally-valid explanations glue into one globally admissible explanation" computable via cellular sheaves; detects global inadmissibility even when all local R²>0.999. |
| [[2608.05522]] | 无方程周期感知方法从短轨迹估计主导负 Lyapunov 指数，逻辑斯蒂映射覆盖 92/112，R²=0.886。/ Equation-free period-aware method estimates dominant negative Lyapunov exponents from short trajectories (logistic map 92/112, R²=0.886). |

### 持续学习与量子纠错 / Continual Learning & Quantum Error Correction

| Paper | 一句话总结 / One-line Summary |
|-------|------|
| [[2608.06216]] | 综述把 LLM/智能体时代的持续学习重构为 When×Where×How 三轴"能力持续演化"，经典 CL 只是其中一个点。/ Survey reframes continual learning for the LLM/Agentic era as three orthogonal axes (When×Where×How), with classical CL as a single point. |
| [[2608.05686]] | 证明经 randomized compiling 后量子纠错检测事件率在校准点局部强凸，零阶 SPSA 在线恢复漂移，O(1/ε²) 收敛且与码距无关。/ Proves the QEC detector-event rate is locally strongly convex after randomized compiling; zeroth-order SPSA recovers drift in O(1/ε²), distance-independent for LDPC codes. |

---

## All Papers

| # | Link | Short Title | Topic |
|---|------|-------------|-------|
| 1 | [[2608.05490]] | Innovation-Residual Auditing of Agents | Failure attribution theory |
| 2 | [[2608.05499]] | APQF: Profiling-Guided Pruning + Quantization | Model compression |
| 3 | [[2608.05522]] | Lyapunov Exponent Estimation (Negative) | Dynamical systems |
| 4 | [[2608.05563]] | PoisonedEvolution: Trajectory Poisoning | Agent security |
| 5 | [[2608.05604]] | SkillZip: Contract-Preserving Skill Compression | Agent skills |
| 6 | [[2608.05628]] | SkillHEX: Hypothesis-Driven Exploration | Agent skills |
| 7 | [[2608.05651]] | RelayEvolve: Population Handoff | Efficient evolution |
| 8 | [[2608.05660]] | Reasoning Errors Region & Direction | Interpretability |
| 9 | [[2608.05670]] | Consensus vs Correctness (RENDEQ) | VLM reliability |
| 10 | [[2608.05675]] | Consistency Blind Spot (ECS) | VLM reliability |
| 11 | [[2608.05686]] | Self-Calibrating Quantum Fault Tolerance | Quantum computing |
| 12 | [[2608.05702]] | SEAM: Global Consistency in SciML | Scientific ML |
| 13 | [[2608.05726]] | LLM-Judge Bias via Random Numbers | Evaluation |
| 14 | [[2608.05732]] | CircuitSteer: SAE Circuit Steering | Interpretability |
| 15 | [[2608.05778]] | Agent Playbook Transfer | Agent deployment |
| 16 | [[2608.05783]] | GROM: Gradient-Free Unlearning | Machine unlearning |
| 17 | [[2608.05797]] | Predicting Task Difficulty (No Rollouts) | Agent evaluation |
| 18 | [[2608.05810]] | Pre-Commit Gating (VaG) | Agent self-evolution |
| 19 | [[2608.05857]] | SQP: Embedding Similarity Mapping | Embedding analysis |
| 20 | [[2608.05863]] | WitCert: Attention Memory Observability | Systems |
| 21 | [[2608.05872]] | MACRO: Markov Chain Layer Routing | Efficient inference |
| 22 | [[2608.05906]] | MERIT: Causal Episodic Memory | Agent repair |
| 23 | [[2608.05944]] | B300 Multi-Node Fine-Tuning Report | Systems |
| 24 | [[2608.05980]] | Simple Transformations Across Embeddings | Embedding analysis |
| 25 | [[2608.05987]] | AgentOPSD: Recursive Self-Distillation | Agent RL |
| 26 | [[2608.05995]] | Unified Risk View of Uncertainty | Uncertainty |
| 27 | [[2608.06046]] | ML-for-ML: Joint Knob Optimization | Systems |
| 28 | [[2608.06144]] | FinEvo-Bench: Financial Self-Evolving | Agent benchmark |
| 29 | [[2608.06153]] | GSE: Globally Reusable Coding Skills | Agent skills |
| 30 | [[2608.06177]] | Threshold Early Stopping (Binary Activation) | Efficient inference |
| 31 | [[2608.06206]] | Localized Conformal Prediction Bounds | Conformal prediction |
| 32 | [[2608.06216]] | Continual Learning in Transition | Survey |
| 33 | [[2608.06262]] | Hypothesis Testing with Conditional Queries | Learning theory |
| 34 | [[2608.06291]] | BaKron: Kronecker-Hessian Quantization | Model compression |
| 35 | [[2608.06301]] | HarnessOpt-Bench | Agent benchmark |
| 36 | [[2608.06329]] | Benchmarking Conversational Benchmarks | Agent benchmark |
| 37 | [[2608.06337]] | Optimal Rates for Monotone Adversaries | Learning theory |
| 38 | [[2608.06346]] | TRAJDEBUG: Error Lifecycle Tracing | Agent debugging |
| 39 | [[2608.06352]] | CalibForge: Adversarial Solver Calibration | Agent training data |
| 40 | [[2608.06363]] | Optimal Agnostic PAC Algorithm | Learning theory |
