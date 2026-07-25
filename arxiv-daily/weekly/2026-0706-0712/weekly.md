---
title: "Weekly arXiv Digest — 2026-07-06–2026-07-12"
week: 2026-0706-0712
date_range:
  - 2026-07-06
  - 2026-07-10
tags:
  - llm-agents
  - self-evolving
  - autonomous-research
  - mechanistic-interpretability
  - interpretability
  - ai-safety
  - reliability
  - uncertainty-quantification
  - calibration
  - long-context
  - model-compression
  - quantization
  - efficient-inference
  - llm-scaling
  - optimization-theory
  - evaluation
papers: 169
---

# 每周 arXiv 速递 / Weekly arXiv Digest — 2026-07-06–2026-07-12

本周共收录 **169** 篇去重论文，覆盖 2026-07-06 至 2026-07-10 五个交易日。主线集中在：自演化/自主研究智能体、机制可解释性及其评估、可靠性与不确定性量化、长上下文失效模式、模型压缩与高效推理、以及优化与学习理论。

This week indexes **169** unique papers across 2026-07-06 → 2026-07-10. The dominant arcs are self-evolving & autonomous-research agents, mechanistic interpretability and (critically) its evaluation, reliability/UQ, long-context failure modes, compression & efficient inference, and optimization/learning theory.

---

## 本周必读 / Must Read This Week

> "如果你本周只读几篇，读这些。" 八篇均跨日复现或为当日 must-read。

### [[2607.08124]] TTHE: Test-Time Harness Evolution

- **推荐理由：** 把 agent 的可执行控制程序（harness）当作测试时适应的状态——仅用无标签执行轨迹驱动种群搜索改写 harness 代码，不更新权重、不需 gold 标签，把 BIRD 困难切片从 12.0% 拉到 50.0%。一种"改程序而非改权重"的测试时适应范式，简洁实用。
- **Why read:** TTHE reformulates test-time adaptation as evolution over an agent's executable harness — proposers rewrite harness code from unlabeled traces, a label-free judge commits changes, lifting BIRD hard-slice 12.0% → 50.0% with zero weight updates or gold labels. A clean, practical idea that directly inspires agent engineering.

### [[2607.08284]] PredicateLongBench

- **推荐理由：** 令人不安的基准——闭源强模型在 baseline 长上下文任务上达 87%–97%，但只要插入 8 个分散的 near-sorted decoy，所有前沿模型（Opus 4.6、GPT-5.4、Gemini 3.1 Pro）全部崩溃到 ≤2%。任何依赖长上下文 LLM 做检索/推理/Agent 的人都必须知道这个失效模式。
- **Why read:** A sobering benchmark: inserting just 8 scattered near-sorted decoys collapses every frontier long-context model to ≤2% on synthetic data (≤36% on real text), despite 87–97% baseline accuracy. An essential failure mode for retrieval, reasoning, and agent builders.

### [[2607.08349]] Certified Interventional Fidelity (CIF)

- **推荐理由：** 为机制可解释性评估（IIA、activation patching、circuit completeness）提出首个统一的"因果被估量 + anytime-valid 置信序列"统计层，betting 序列使认证成本降低 10–30 倍，并暴露在强扰动下没有任何非恒等抽象能通过 F≥0.90——一个可能改变评估规范的模块化框架。
- **Why read:** CIF wraps heterogeneous interpretability metrics into one bounded causal estimand with anytime-valid confidence sequences, cutting certification cost 10–30× via variance-adaptive betting, and exposes a point-estimate-hidden negative result (no non-identity abstraction reaches F≥0.90 at p=0.5). A modular layer that could change how the community reports interventional evidence.

### [[2607.08456]] Two Axes of LLM Abstention

- **推荐理由：** 揭示被忽视的几何结构——拒答在"答案正确性"与"问题可答性"两轴上分离，单一置信度阈值只能读前者；隐藏状态探针在可答性上达 0.97–0.99 AUROC，"因子化拒答"在 8B 模型上以 0.75 覆盖率同时认证两个误差预算（单阈值仅 0.31）。
- **Why read:** Abstention decomposes along two axes (answer correctness vs. question answerability) that need different signals; a hidden-state answerability probe (0.97–0.99 AUROC) enables Factorized Abstention certifying both error budgets at 0.75 coverage where confidence-only conformal abstention manages only 0.31.

### [[2607.07663]] Recursive Self-Improvement Survey

- **推荐理由：** 迄今最系统的 RSI 综述，梳理 1250+ 篇文献并建立验证层级分类法（形式化验证 → 测试 → 启发式 → 无验证），明确指出现有"自改进"工作大多缺乏可验证的进步闭环。任何研究自演化 Agent、auto-research loop 的人都需要这张地图。
- **Why read:** The most systematic RSI survey to date, organizing 1250+ works into a verification-hierarchy taxonomy (formal proof → test → heuristic → none) and bluntly flagging that most "self-improvement" claims lack a verifiable improvement loop. Required map-and-vocabulary reading for self-evolving agent research.

### [[2607.07436]] The Blind Curator

- **推荐理由：** 清晰的解析结果——当判别器自身有偏时，技能退役阈值被钉死在 ρ_F→P = (1−τ)/2，结构性地扼杀自改进。对所有依赖 LLM-as-judge 的自演化系统都是警钟：先修裁判，再谈改进。
- **Why read:** A clean analytical result: a biased judge pins the skill-retirement threshold at ρ_F→P = (1−τ)/2, structurally killing self-improvement. A wake-up call for every self-evolving pipeline that leans on LLM-as-judge — fix the judge before claiming improvement.

### [[2607.08066]] Persuasion Attacks on Chain-of-Thought Monitoring

- **推荐理由：** 随着 CoT 监控成为前沿 AI 安全的主要防线，本文系统研究其脆弱性——对抗性 CoT 能通过说服策略使监控者误判危险行为，揭示"监控者与被监控者能力不对称"这一根本风险。
- **Why read:** As CoT monitoring becomes a primary frontier-AI defense, this work systematically studies its vulnerability to persuasion attacks, where adversarial reasoning persuades the monitor to misclassify dangerous behavior — exposing the fundamental risk of a capability asymmetry between monitor and monitored.

### [[2607.08186]] Hidden Decoding at Scale (WeChat AI)

- **推荐理由：** 首次将"序列长度扩展"作为固定主干缩放路径推到 100B+ MoE 规模——每个 token 展开为多个流并通过 Stream-Factorized Attention 把注意力代价从二次降到近线性，WeLM-HD4-617B 在全部九项共享难基准上击败匹配的非 HD 基线。继稀疏 MoE 之后又一个被工程验证的正向缩放维度。
- **Why read:** The first sequence-length scaling method at the 100B+ MoE scale: expanding each token into n streams with Stream-Factorized Attention (quadratic → near-linear), WeLM-HD4-617B beats matched non-HD baselines on all nine shared hard benchmarks (e.g., GPQA Diamond 89.1 → 91.2). A genuinely new, engineered scaling dimension beyond sparse MoE.

---

## 本周主题脉络 / Themes This Week

### 1. 自演化与自主研究智能体 / Self-Evolving & Autonomous-Research Agents

本周最强的主线：让 Agent 改写自己的工具、记忆与流程。综述层面 [[2607.07663]] 给出 RSI 的验证层级地图；机制层面 [[2607.07321]] EVOSOP 把工具描述/签名当作可优化 artifact（ACEBench +24pp），[[2607.08124]] TTHE 把整段 harness 代码作为测试时适应的状态。应用侧 [[2607.08010]]（Amazon 工具制造）、[[2607.08662]] WebSwarm（递归多智能体网页搜索 +17.5pp）、[[2607.08332]] XALPHA（记忆驱动量化研究员，CSI300 IR 1.59）和 [[2607.08758]] IdeaGene-Bench（科学谱系推理，最强系统仅 27.3%）共同把"自主研究闭环"从口号推向可评测。同时 [[2607.07436]] The Blind Curator 给出冷峻反例：有偏 LLM-as-judge 会结构性地杀死技能退役。

The week's strongest arc: agents rewriting their own tools, memory, and workflows. [[2607.07663]] maps the RSI verification hierarchy; [[2607.07321]] EVOSOP optimizes tool descriptions/signatures (+24pp on ACEBench); [[2607.08124]] TTHE evolves the whole harness program at test time. Applications span [[2607.08010]] (Amazon tool-making), [[2607.08662]] WebSwarm (+17.5pp), [[2607.08332]] XALPHA (IR 1.59), and [[2607.08758]] IdeaGene-Bench (best system 27.3%). Counterpoint: [[2607.07436]] shows a biased judge structurally kills self-improvement.

### 2. 机制可解释性及其评估 / Mechanistic Interpretability & Its Evaluation

可解释性本周的双重焦点是"做机制"和"评估机制"。评估侧 [[2607.08349]] CIF 用 anytime-valid 置信序列统一了 IIA/patching/circuit-completeness，并暴露强扰动下无抽象通过 F≥0.90；[[2607.07316]] MI Survey 给出领域综述。机制侧 [[2607.04640]] Wrong-Dip 因果验证"中层先错后对"并预测结构化压缩失败，[[2607.05355]] Faithfulness-to-Refusal 证明神经元选择器的排名稳定性与因果有效性完全解离，[[2607.08393]] Knowing-Using Gap 形式化"记住但不会用"并用 self-patching 恢复 58–75%，[[2607.08499]] Procrustes Joint SAE 与 [[2607.08605]] S²AE 推进跨种子/跨模态特征对齐，[[2607.08173]] Overthinking 与 [[2607.08339]] TypeProbe 把探针用于安全审计与代码模型。

Dual focus: doing mechanistic interpretability and evaluating it. On evaluation, [[2607.08349]] CIF unifies IIA/patching/completeness under anytime-valid confidence sequences; [[2607.07316]] surveys the field. On mechanism, [[2607.04640]] causally verifies a mid-layer "wrong-dip," [[2607.05355]] shows rank-stability ≠ causal-validity for neuron selectors, [[2607.08393]] formalizes the memorize-but-can't-use gap, [[2607.08499]]/[[2607.08605]] push cross-seed and cross-modal SAEs, and [[2607.08173]]/[[2607.08339]] turn probes toward safety and code models.

### 3. 可靠性、安全与不确定性量化 / Reliability, Safety & UQ

一条贯穿全周的"可信部署"脉络。安全侧 [[2607.08066]] Persuasion Attacks 揭示 CoT 监控被说服攻击击穿；[[2607.08065]] Self-Consistency Audit 证明自一致性≠准确性；[[2607.08077]] GRAM 用梯度路由做访问控制。UQ 侧 [[2607.08456]] Two Axes 重构拒答几何，[[2607.08349]]/[[2607.08377]] Eigenvalue Calibration 与 [[2607.08017]] GRAPHEVAL 提供新的认证与校准工具，[[2607.08522]] 用分组序贯检验把 VLM 评测成本降约 80%。评测方法论上 [[2607.08535]] Auditing LLM-as-Judge 发现强裁判仍残留 14.7% 翻转且陪审投票因高相关几乎无效。

A week-long "trustworthy deployment" thread. Safety: [[2607.08066]] breaks CoT monitors via persuasion, [[2607.08065]] shows agreement≠accuracy, [[2607.08077]] adds gradient-routed access control. UQ: [[2607.08456]] reframes abstention geometry, [[2607.08377]]/[[2607.08017]] add calibration/UQ tools, [[2607.08522]] cuts VLM eval cost ~80%. Methodology: [[2607.08535]] finds strong judges still flip 14.7% of verdicts and jury voting adds ~nothing.

### 4. 长上下文失效与记忆 / Long-Context Failure Modes & Memory

长上下文本周的核心叙事是"看似很强的能力其实极脆"。[[2607.08284]] PredicateLongBench 用 8 个 decoy 把所有前沿模型打到 ≤2%；[[2607.08032]] COMPACT-Bench 给出率失真记忆压缩基准；[[2607.08393]] Knowing-Using Gap 揭示知识存储层与推理层错位；[[2607.08716]] Proactive Memory Agent 在 Terminal-Bench 2.0 上以主动干预为 Sonnet 4.5 提升 +8.3pp。综合来看，"塞进上下文 ≠ 用得上"是本周反复出现的设计教训。

The narrative: long-context capability that looks strong is often brittle. [[2607.08284]] collapses every frontier model to ≤2% with 8 decoys; [[2607.08032]] benchmarks memory compaction; [[2607.08393]] exposes storage-vs-inference circuit misalignment; [[2607.08716]]'s proactive memory agent adds +8.3pp on Terminal-Bench 2.0. The recurring design lesson: "in context" ≠ "usable."

### 5. 缩放、压缩与高效推理 / Scaling, Compression & Efficient Inference

架构缩放本周的明星是 [[2607.08186]] Hidden Decoding（WeLM-HD4-617B，序列长度缩放到 100B+ MoE）。压缩与量化方向则集中反思"哪些权重真的重要"：[[2607.08733]] Super Weights 证明单独训练最重要的权重反令精度跌回随机，[[2607.08734]] Illusion of Equivalency 用正确性一致度揭示量化行为漂移，[[2607.08643]] BiSCo-LLM 给出无码本 ~2-bit 球面编码，[[2607.08015]]/[[2607.08241]]/[[2607.08526]] 覆盖 ReRAM、CFG 扩散与端侧音频。训练效率侧 [[2607.05711]] FourTune（W4A4G4 扩散后训练）与 [[2607.07494]] GIFT（FP8 梯度通信）也值得关注。

On architecture, [[2607.08186]] Hidden Decoding (WeLM-HD4-617B) is the star — sequence-length scaling at 100B+ MoE. Compression week反思 "which weights actually matter": [[2607.08733]] shows training only super-weights collapses accuracy, [[2607.08734]] exposes quantization drift via correctness agreement, [[2607.08643]] offers codebook-free ~2-bit spherical coding, with [[2607.08015]]/[[2607.08241]]/[[2607.08526]] covering ReRAM, CFG diffusion, and on-device audio. Training efficiency: [[2607.05711]] FourTune (W4A4G4) and [[2607.07494]] GIFT (FP8 gradient comm).

### 6. 优化与学习理论 / Optimization & Learning Theory

理论侧本周有几条结实的进展：[[2607.04993]] 把有限步 GD 看作动力系统（稳定边界=首次分岔），[[2607.05836]] Two-Sided L-BFGS 给出一致条件数界，[[2607.05872]] 证明 GaLore 子空间仅 ~39/128 方向可识别，[[2607.06382]] NTK 在组合目标上样本复杂度指数次优，[[2607.08380]] 刻画大步长 GD 在平坦极小值流形附近的动力学，[[2607.08104]] 分析 vanilla SGD 的重尾噪声。共同主题是"把训练动态当作可分析的几何/随机对象"。

Solid theoretical progress: [[2607.04993]] treats finite-step GD as a dynamical system (edge-of-stability = first bifurcation), [[2607.05836]] gives a uniform L-BFGS condition-number bound, [[2607.05872]] shows GaLore's subspace is only ~39/128 identifiable, [[2607.06382]] proves NTK is exponentially sub-optimal on compositional targets, [[2607.08380]] characterizes large-step GD near flat-minima manifolds, and [[2607.08104]] analyzes heavy-tailed noise in vanilla SGD. Common thread: treating training dynamics as analyzable geometric/stochastic objects.

---

## 全部论文 / All Papers

### 2026-07-06 (28)

- [[2607.04562]] Heaviside Continuity of Rolling Coefficients (HCRC) — 验证门控把 LLM 降为"提议者"，虚假完成率 4–7%→0%。Verification gate reduces LLM to proposer; FCR 4–7%→0%.
- [[2607.04572]] Detecting Answer-Driven Reasoning (Truncated CoT Audit) — 截断式 CoT 探针检测答案驱动推理，AUC 0.375→0.900。Truncated CoT probing detects answer-driven reasoning; AUC 0.375→0.900.
- [[2607.04627]] Reliability of Persona-Trained Monte Carlo (PTMC) — 智能体市场仿真器的统计可靠性理论 + Lucas 极小化界。Statistical reliability theory for agent market simulators + Lucas minimax bound.
- [[2607.04640]] Wrong Before Right: Late Rescue (Wrong-Dip) — 因果验证中层"先错后对"，预测结构化压缩但盲于量化。Causally verifies mid-layer wrong-dip; predicts structural compression but not quantization. ⭐
- [[2607.04645]] Retroactive Chain-of-Thought (RETROCOT) — 法医式逆向重建越狱，GPT-4o ASR 0→58%。Forensic-reconstruction jailbreak; GPT-4o ASR 0→58%.
- [[2607.04668]] Elastic Gang (Per-Token Gang Co-Scheduling) — 弹性帮派在 token 间安全换核，输出比特精确。Elastic gang changes cores per-token, bit-exact output.
- [[2607.04681]] VLA Faithfulness (Pinocchio) — 区分功能/忠实推理，GRPO+评判器提升忠实性。Separates functional/faithful reasoning; GRPO+critic lifts faithfulness.
- [[2607.04683]] Attributing VLM Errors (Attribution Tree) — 归因树分解 VQA 错误为四类，解码前预测并路由。Attribution tree decomposes VQA errors; pre-decoding routing.
- [[2607.04686]] ToolFailBench (Tool-Use Failure Diagnosis) — 参数化陷阱分离 4 类工具失败，同规模差 89 分。Parametric traps isolate 4 tool failures; 89pt same-scale gap.
- [[2607.04728]] SIS (Selective Importance Sampling) — 拒绝采样把 off-policy token 转 on-policy，~1%开销。Rejection sampling converts off-policy→on-policy, ~1% overhead.
- [[2607.04800]] Compressed Computation in Superposition (L4-CiS) — L2→L4 损失即涌现超叠加，逆向工程稀疏码+伪逆。L2→L4 loss elicits superposition; reverse-engineered code+pseudoinverse.
- [[2607.04819]] Layer-Parallel Encrypted Inference (SNLP-FHE) — 层并行把加密自举次数 53→20，困惑度退化 1.2%。Layer-parallel cuts FHE bootstraps 53→20, +1.2% PPL.
- [[2607.04926]] Few-Shot Binding in Tiny Transformers (MicroGround) — 全枚举证明零样本绑定全失败，少样本只看共享+可读性。Exhaustive study: zero-shot binding fails all paths; few-shot = sharing + readability.
- [[2607.04969]] Memorization-Guided Data Reuse — 记忆窗口框架定义重用安全区间，挑战 4-epoch 上限。Memorization window defines safe reuse interval; challenges 4-epoch limit.
- [[2607.04993]] Finite-Step GD as Dynamical System — 稳定边界即首次分岔，Ricker 大深度极限，学习率是结构参数。Edge-of-stability = first bifurcation; Ricker depth limit; LR is structural.
- [[2607.05013]] Knowledge vs. Verbalization (Math Solvability) — 两探针解耦知道/说出不可解，编造源于语言化偏移。Two probes disentangle know/say of unsolvability; fabrication = verbalization shift.
- [[2607.05046]] CollabEval (Matrix Completion Evaluation) — 评测建模为矩阵补全，CI 宽度缩窄 20–30%。Eval as matrix completion; CIs 20–30% narrower.
- [[2607.05104]] Grokking Is Conditional and Fragile — 仅改 CPU 线程数翻转 16% 同种子 grok 结果。Changing CPU threads flips 16% same-seed grok outcomes.
- [[2607.05175]] Platonic Projection Structures (PPS) — 算子核定义输出可解释性的结构性盲区。Operator kernel defines structural limits of output interpretability.
- [[2607.05184]] Rethinking On-Policy Self-Distillation (OPSD) — 特权自蒸馏翻转自纠错 token 优势，伤害思维模型。Privileged self-distillation flips self-correction advantage; harms thinking models. ⭐
- [[2607.05188]] Latent Programming Horizons in Coding Agents — 编码 agent 残差流线性解码程序正确性，前 25 步可预测。Coding-agent residual stream decodes correctness, predicts ~25 steps ahead.
- [[2607.05198]] Noisy-Channel MBR Decoding — MBR 打分分解为四概率通道，统一 5 种变体。Decomposes MBR into 4 channels; unifies 5 variants.
- [[2607.05202]] EvoAgentBench (Agent Ability Transfer) — 首个能力支撑迁移基准，揭示自动方法脆弱性。First ability-supported transfer benchmark; exposes auto-method brittleness.
- [[2607.05297]] MetaSkill-Evolve (Recursive Skill Evolution) — 双时间尺度递归进化 meta-skill，+23.5/+16.1。Two-timescale recursive meta-skill evolution; +23.5/+16.1.
- [[2607.05316]] LLMs Linearly Encode Output Length — 残差流线性解码剩余长度，回撤 token 处上调。Residual stream linearly decodes remaining length; shifts at retractions.
- [[2607.05355]] Faithfulness to Refusal (Neuron Selector Audit) — 选择器排名稳定性与因果有效性完全解离。Rank-stability ≠ causal-validity; refusal subspace redundant. ⭐
- [[2607.05381]] What Does a Discrete Diffusion Model Learn? — 负 ELBO−熵=路径 KL，统一离散扩散方法。NELBO−entropy = path KL; unifies discrete diffusion methods.
- [[2607.05391]] LLM-as-a-Verifier (General Verification) — logits 期望连续奖励，三轴缩放，四基准 SOTA。Logit-expectation continuous reward; 3-axis scaling; SOTA on 4 benchmarks.

### 2026-07-07 (50)

- [[2607.05708]] Akashic — 分块 MemAttention + 软硬件协同内存管理，精度+10.2 点、吞吐 1.21× / Chunk MemAttention + HW/SW co-design; +10.2 pt accuracy, 1.21× throughput
- [[2607.05711]] FourTune — 首个 W4A4G4 全 4 位扩散后训练，内存降 2.25×、训练加速 2.27× / First W4A4G4 diffusion post-training; memory 2.25× lower, 2.27× faster
- [[2607.05721]] SpanUQ — Span 级不确定性探针 AUROC 0.908–0.944，快 10–20× / Span-level UQ probe AUROC 0.908–0.944, 10–20× faster
- [[2607.05722]] Nemotron-Labs-Diffusion — 统一 AR/扩散/自推测三模式，吞吐 4× 于 Qwen3-8B / Unified tri-mode LM, 4× throughput vs Qwen3-8B
- [[2607.05726]] ART — 事后诊断揭示捷径仍可被恢复 / Post-hoc diagnostic showing shortcuts remain restorable
- [[2607.05735]] Width-Robust Mean-Field BNN — 无限宽度可学性等价于多项式宽度，由约化熵 s∞ 控制 / Infinite-width learnability iff polynomial-width, governed by s∞
- [[2607.05743]] Execution-Security SoK — 系统化 39 篇编码代理执行安全论文 / Systematizes 39 execution-security papers for AI coding agents
- [[2607.05744]] MCP TAG-Block Concealment — TAG-block 编码 8/8 到达模型上下文 / TAG-block encoding 8/8 reaches model context
- [[2607.05748]] HARVEY — 学习后门作毒样本预言机，ASR<2% (AAAI 2025) / Learns backdoor as poison oracle, ASR<2% (AAAI 2025)
- [[2607.05758]] Coupled Digital Twins — 样本+仪器数字孪生，相位误差降 82% / Sample+instrument digital twin, phase error down 82%
- [[2607.05764]] Inject or Navigate — navindex 在 18/18 打平 inject 且成本降 25% / navindex ties inject 18/18 at 25% lower cost
- [[2607.05775]] Beyond the Leaderboard — 六簇失败分类法，失败非线性累积 / Six-cluster failure taxonomy; failures compound non-linearly
- [[2607.05790]] Heading Activation Steering — 激活引导双向控制工具调用 / Bidirectional control of tool use via activation steering
- [[2607.05804]] TurnOPD — 轮次级预算蒸馏，最高 2.29× 加速 / Turn-level budgeting distillation, up to 2.29× speedup
- [[2607.05806]] Heckman UQ — Heckman 选择校正，oracle IW 仅覆盖 43.1% vs 88.9% / Heckman selection correction; oracle IW 43.1% vs 88.9%
- [[2607.05836]] Two-Sided L-BFGS — [ϵ,M] 包络证明条件数一致有界 / [ϵ,M] envelope proves uniform condition-number bound
- [[2607.05866]] DP-NGD — 差分隐私自然梯度，SVHN ε=1.0 上 84.65%，10× 加速 / DP natural gradient; 84.65% on SVHN ε=1.0, 10× speedup
- [[2607.05872]] No Subspace to Track — GaLore 子空间仅 ~39/128 可识别 / GaLore subspace only ~39/128 identifiable directions
- [[2607.05876]] Floor First Triage — 双侧 floor 解释 TP16 vs DP-attention 的相反选择 / Two-sided floors explain opposite TP16 vs DP-attention choices
- [[2607.05898]] Auditing Unlearning — MIA 审计器尖锐分离 certified vs 启发式遗忘 / MIA auditor sharply separates certified vs heuristic unlearning
- [[2607.05901]] BAR Loss Depression — 成对排序做抑郁检测 SOTA / Pairwise ranking for depression detection SOTA
- [[2607.05904]] Self-Play Reward Hacking — 自博弈让错误更可信而非更正确 / Self-play makes errors more convincing, not more correct
- [[2607.05908]] Drift Happens — 强归纳偏置漂移更快，冻结编码器更稳 / Stronger inductive biases drift faster; frozen encoders steadier
- [[2607.05933]] Energy-Efficient GPU DVFS — 决策树 governor 对 SLM 微调节能 13.11% / Decision-tree governor saves 13.11% energy for SLM fine-tuning
- [[2607.05969]] MemDefrag — 注意力密度做记忆碎片整理，43.0% vs 17.4% / Attention-density defragmentation; 43.0% vs 17.4%
- [[2607.05993]] Bit2Watt — GPU 工作负载调制 destabilize 电网 / GPU workload modulation destabilizes DER grids
- [[2607.06001]] LLM Agent Economies — 预注册确认信息→财富容量定律 / Pre-registered confirmation of information-to-wealth capacity law
- [[2607.06013]] Stability Annealing Sign Descent — 收敛到 Burg 障碍极小点，κ 作间隔约束 / Converges to Burg barrier minimizer; κ as margin constraint
- [[2607.06048]] Scattering Networks Capacity — 几何测度论刻画散射网络分离容量 / Geometric measure theory characterizes scattering-network separation capacity
- [[2607.06094]] LatAD — 联合潜聚类做 CPS 异常检测超 SOTA / Joint latent clustering beats deep SOTA for CPS anomaly detection
- [[2607.06111]] MCC — LLM 抽取测量语义校准，MAE 降 30.7% / LLM measurement-semantics correction; MAE down 30.7%
- [[2607.06140]] CURATE EVO — 数据清洗代码化演化，4B 超 8B 基线 / Data curation as evolving code; 4B beats 8B baselines
- [[2607.06151]] EISAM — Extragradient+SAM，CIFAR-100 85.85% vs 85.23% / Extragradient+SAM; CIFAR-100 85.85% vs 85.23%
- [[2607.06155]] Tool Use Expressive Power — 有限状态工具仍正则，无界磁带图灵完备 / Finite-state tools stay regular; unbounded tape enables Turing-completeness
- [[2607.06163]] X-FEMR — EHR 基础模型 token 级可解释 / Token-level explainability for EHR foundation models
- [[2607.06175]] RL-BPMN-Reward-Design — RL 奖励设计研究，等权奖励最优 / RL reward design study; equal-weight rewards win
- [[2607.06202]] UBEP — 生产级 superpod MoE 通信库，延迟降 52.4% (SIGCOMM 2026) / Production superpod MoE comm library; latency down 52.4% (SIGCOMM 2026)
- [[2607.06223]] IGRPO — 信息增益自适应 rollout，+3.1% EM / Information-gain adaptive rollout; +3.1% EM
- [[2607.06230]] Entanglement PAC-Bayes — 量子策略 PAC-Bayes 界由 Fisher 有效维数控制 / Quantum-policy PAC-Bayes bound governed by Fisher effective dimension
- [[2607.06290]] Quantitative GP Limits of Tensor Programs — 张量程序有限宽收敛 Wasserstein 误差 O(Σ1/√m) / Tensor-program finite-width Wasserstein rate O(Σ1/√m)
- [[2607.06320]] Dithered Gaussian Mechanism — 网格离散化高斯输出继承 DP 且规避浮点漏洞 / Grid-discretized Gaussian output inherits DP, avoids floating-point attacks
- [[2607.06327]] Multilingual UE from Reasoning — 22 语言 UE 评测，英语推理助低资源语言 / 22-language UE study; English reasoning helps low-resource
- [[2607.06328]] Driving the Wrong Way — SAE 分解驾驶潜在空间，消融 3 神经元 EPDMS 0.524→0.5926 / SAE driving-latent decomposition; ablating 3 neurons EPDMS 0.524→0.5926
- [[2607.06341]] Aria — 通用 LLM 代理 + Coq，Iris 4257 条 100% 证明 / LLM agent + Coq harness; 100% on Iris 4,257 lemmas
- [[2607.06382]] NTK Function-Space Dichotomy — NTK 在组合目标上样本复杂度指数次优 / NTK exponentially sub-optimal on compositional targets
- [[2607.06407]] ExplAIner — 声明式查询语言统一形式化解释 / Declarative query language unifying formal explanations
- [[2607.06413]] Experimental Design Agentic AI — 全因子评估编码代理，推理努力增成本不增质量 / Full-factorial coding-agent evaluation; effort raises cost not quality
- [[2607.06445]] Analysis-by-Proxy — Q-Former 代理发现 VLM 定位信号在中层 / Q-Former proxy finds VLM localization signals in mid-layers
- [[2607.06447]] Danus — 事实图编排数学推理，击败 Rethlas / Fact-graph orchestration for math reasoning, beats Rethlas
- [[2607.06503]] Doomed from the Start — 第 1–2 轮探针预测失败，省 47.1% 算力 / Round-1 probes predict failure, save 47.1% compute

### 2026-07-08 (31)

- [[2607.06871]] Geometric Collapse / 几何崩溃 — Reliability/Safety
- [[2607.06893]] Stochastic Oracles / 随机预言 — Reliability/Safety
- [[2607.06924]] Intrinsic-Noise Consolidation / 噪声巩固 — Scientific ML
- [[2607.06940]] MFSS / 多因子打分系统 — Evaluation
- [[2607.06974]] MILES / 模块化指令记忆 — Self-Evolving Agents
- [[2607.06987]] UP / 不对称优化 — LLM Training
- [[2607.07003]] Dissociating Sycophancy / 分离谄媚 — Mech. Interpretability
- [[2607.07035]] Principles of Deep Feedforward ReLU Networks / 深 ReLU 网络原理 — Mech. Interpretability
- [[2607.07040]] Measuring Intelligence Beyond Human Scale / SepaRank — Evaluation
- [[2607.07047]] Riemannian Mean Pooling / 黎曼均值池化 — Mech. Interpretability
- [[2607.07052]] Progressive Crystallization / 渐进式结晶 — Self-Evolving Agents
- [[2607.07066]] Stratified Fourier Mechanisms / 分层傅里叶机制 — Mech. Interpretability
- [[2607.07128]] DSI / 分布式稀疏干预 — Mech. Interpretability
- [[2607.07184]] Deployment Simulation / 部署模拟 — Reliability/Safety
- [[2607.07229]] Reasoning Consistency Scanning / 推理一致性扫描 — Reliability/Safety
- [[2607.07264]] LAD / 语言锚定分解 — Mech. Interpretability
- [[2607.07316]] MI Survey / 机制可解释性综述 — Mech. Interpretability
- [[2607.07321]] EVOSOP / 迭代工具优化 — Self-Evolving Agents ⭐
- [[2607.07379]] PA-SciML / 物理审计科学发现 — Scientific ML
- [[2607.07395]] ARG-TCA / 图属性推理校准 — Reliability/Safety
- [[2607.07405]] Deterministic Gates / 确定性门 — Reliability/Safety
- [[2607.07436]] The Blind Curator / 有偏裁判杀死技能退役 — Reliability/Safety ⭐
- [[2607.07467]] SpaCellAgent / 空间转录组 Agent — Scientific ML
- [[2607.07494]] GIFT / FP8 梯度通信 — LLM Training
- [[2607.07504]] Skills Ablation / 技能消融零结果 — Self-Evolving Agents
- [[2607.07508]] SAO / 单rollout异步 RL — LLM Training
- [[2607.07538]] Langevin Dynamics / 朗之万动力学安全界 — Reliability/Safety
- [[2607.07626]] Future Confidence Distillation / 未来置信度蒸馏 — Mech. Interpretability
- [[2607.07663]] Recursive Self-Improvement Survey / 递归自改进综述 — Self-Evolving Agents ⭐
- [[2607.07670]] Bielik Activation Dispersion / 激活分散度 — Mech. Interpretability
- [[2607.07676]] SkillCenter / 技能中心 — Self-Evolving Agents

### 2026-07-09 (50)

- [[2607.08002]] Stochastic Activity Prediction — Wallace-tree 乘法器的随机活动预测理论 / Stochastic activity prediction for Wallace-tree multipliers. ↻07-10
- [[2607.08003]] CoThinker — LLM 驱动的 CO2 电还原催化剂发现 / LLM-driven catalyst discovery for CO2 electroreduction. ↻07-10
- [[2607.08010]] Tool-Making Agents — 亚马逊生产环境的工具制造智能体 / Tool-making agents in Amazon production. ↻07-10
- [[2607.08015]] CRIMP — ReRAM 交叉栏压缩方法 / ReRAM crossbar compression. ↻07-10
- [[2607.08017]] GRAPHEVAL — 基于图的 LLM 推理不确定性量化 / Graph-based UQ for LLM reasoning. ↻07-10
- [[2607.08029]] Small VLM Quantization (Jetson) — Jetson 上小型 VLM 量化 / Small VLM quantization on Jetson. ↻07-10
- [[2607.08032]] COMPACT-Bench — 率失真记忆压缩综述与基准 / Rate-distortion memory compaction benchmark. ↻07-10
- [[2607.08041]] BIRD — 贝叶斯扩散模型信息论分析 / Information theory of Bayesian diffusion. ↻07-10
- [[2607.08046]] LLM Forecaster Probing — 探针研究 LLM 预测器校准 / Probing LLM forecaster calibration. ↻07-10
- [[2607.08054]] Constitutional Meta-STPA — LLM 安全规约自验证 / LLM safety self-validation.
- [[2607.08059]] When Thinking Hurts — VLM 推理时答案熵坍缩 / Answer-entropy collapse in VLM reasoning. ↻07-10
- [[2607.08065]] Self-Consistency Audit — 自一致性≠准确性 / Agreement≠accuracy. ↻07-10
- [[2607.08066]] Persuasion Attacks on CoT — 对抗推理说服 CoT 监控者 / Persuasion attacks on CoT monitors. ⭐
- [[2607.08077]] GRAM — 梯度路由辅助模块做访问控制 / Gradient-routed access control.
- [[2607.08104]] Vanilla SGD — SGD 重尾噪声理论分析 / Heavy-tailed noise in vanilla SGD. ↻07-10
- [[2607.08124]] TTHE — 测试时工具自主演化 / Test-time harness evolution for agents. ⭐ ↻07-10
- [[2607.08170]] Layer Patching — 层级补丁做模型尺寸插值 / Layer patching for size interpolation. ↻07-10
- [[2607.08173]] Overthinking — 审计过度思考行为 / Auditing overthinking. ↻07-10
- [[2607.08193]] VIP — 多智能体策略视觉检查 / Visual inspection of MARL policies. ↻07-10
- [[2607.08194]] Low-Rank VL Alignment — 低秩视觉语言对齐 / Low-rank vision-language alignment.
- [[2607.08203]] Polyp Segmentation Audit — 息肉分割基准审计 / Polyp segmentation benchmark audit. ↻07-10
- [[2607.08241]] GAMP — CFG 扩散模型量化 / CFG diffusion quantization. ↻07-10
- [[2607.08252]] AutoPersonas — 自动角色智能体生成 / Automated persona agents.
- [[2607.08256]] Best-of-N TTS ASR — TTS/ASR 家族混淆因素 / TTS/ASR family confounds in Best-of-N. ↻07-10
- [[2607.08284]] PredicateLongBench — 谓词级长上下文难度基准 / Predicate-level long-context benchmark. ⭐ ↻07-10
- [[2607.08312]] Write-Protected Bottlenecks — 写保护离散瓶颈 / Write-protected discrete bottlenecks. ↻07-10
- [[2607.08317]] Blind-Spots-Bench — 235 题多模态盲点基准 / 235-question multimodal blind-spots benchmark.
- [[2607.08332]] XALPHA — 记忆驱动 AI 量化研究员 (IR=1.59) / Memory-driven AI quant researcher. ↻07-10
- [[2607.08339]] TypeProbe — 代码模型跨语言类型表示恢复 / Cross-lingual type representation recovery from code models. ↻07-10
- [[2607.08349]] Certified Interventional Fidelity — 干预式可解释性的 anytime-valid 置信序列 / Anytime-valid CS for interventional interpretability. ⭐ ↻07-10
- [[2607.08377]] Eigenvalue Calibration — 密度矩阵特征值矩阵温度缩放校准 / Matrix temperature scaling for eigenvalue calibration. ↻07-10
- [[2607.08380]] GD Large Step Size — 大步长 GD 在平坦极小值流形的动力学 / Large-step GD dynamics near flat-minima manifolds. ↻07-10
- [[2607.08393]] Knowing-Using Gap — 微调知识电路错位与 self-patching 修复 / Knowledge-circuit misalignment and self-patching repair. ↻07-10
- [[2607.08399]] Activation Prompt Compression — 激活空间提示压缩 patch 向量 / Activation-space prompt compression patch vector. ↻07-10
- [[2607.08456]] Two Axes of Abstention — 拒答分解为正确性与可答性两轴 / Abstention decomposes into correctness and answerability axes. ⭐ ↻07-10
- [[2607.08499]] Procrustes Joint SAE — Procrustes 对齐的跨种子通用 SAE / Procrustes-aligned cross-seed universal SAE. ↻07-10
- [[2607.08522]] Stop Guessing When to Stop Testing — 分组序贯检验降 VLM 评测成本 80% / Group sequential testing cuts VLM eval cost ~80%.
- [[2607.08526]] aria — 无依赖量化运行时跑 Stable Audio 3 / Dependency-free quantized runtime for Stable Audio 3. ↻07-10
- [[2607.08535]] Auditing LLM-as-Judge — 换裁判的测量效度问题 / Measurement-validity of judge replacement. ↻07-10
- [[2607.08550]] ESBMC-Arduino — 修复 PLC 形式化验证部署鸿沟 (54→0 误报) / Closes PLC formal verification deployment gap.
- [[2607.08581]] Spectral Stability ELM — 伪逆 ELM 谱稳定性分析 / Spectral stability of pseudoinverse ELM. ↻07-10
- [[2607.08605]] S²AE — 结构化稀疏自编码器改善 VLM 概念一致性 / Structured SAE improves VLM concept consistency. ↻07-10
- [[2607.08643]] BiSCo-LLM — 无码本二进制球面编码 2-bit 压缩 / Codebook-free binary spherical coding at ~2-bit. ↻07-10
- [[2607.08662]] WebSwarm — 递归多智能体网页搜索 (+17.5 ACC) / Recursive multi-agent web search. ↻07-10
- [[2607.08665]] RoR — 预算感知重采样或重路由 (+10.7 pts GPQA) / Budget-aware resample-or-reroute selection.
- [[2607.08700]] Citation Verifier Benchmark — 深度研究引文验证：廉价 judge 足够 / Citation verification: cheaper judges suffice.
- [[2607.08733]] Super Weights — 超级权重重要但不可孤立训练 / Super Weights important but not isolately trainable. ↻07-10
- [[2607.08734]] Illusion of Equivalency — 正确性一致度揭示量化行为漂移 / Correctness agreement exposes quantization drift. ↻07-10
- [[2607.08757]] Score Stability — on-path score 误差不保证采样稳定性 / On-path score error does not certify sampling stability. ↻07-10
- [[2607.08758]] IdeaGene-Bench — 科学谱系推理与创意生成基准 / Scientific lineage reasoning and idea generation benchmark. ↻07-10

### 2026-07-10 (10)

- [[2607.08027]] Structured Pruning of Large Language Models via Power Transformation and Sign-Preserving Score Aggregation — Model Compression & Efficient Inference
- [[2607.08093]] CausalDS: Benchmarking Causal Reasoning in Data-Science Agents — LLM Agents & Autonomous Research
- [[2607.08186]] Hidden Decoding at Scale: Latent Computation Scaling for Large Language Models — LLM Scaling & Multi-modal RL ⭐
- [[2607.08254]] CASL-VAE: Learning Structured Latent Variables from Unpaired Data — Memory, Context & World Models
- [[2607.08370]] Tubular Neighbourhoods of Pfaffian Sets and Applications to Neural Networks — Theory & Mathematical Foundations
- [[2607.08406]] Beyond Backpropagation: Monte Carlo Method Can Train Deep Neural Networks — Optimization & Training
- [[2607.08511]] Systematic Evaluation of Learning Rate Scheduling Strategies Across Heterogeneous Architectures — Optimization & Training
- [[2607.08590]] Robust Bayesian Decision Making under Adversarial Uncertainty — Optimization & Training
- [[2607.08690]] A Practical Investigation of Training-free Relaxed Speculative Decoding — Model Compression & Efficient Inference
- [[2607.08716]] Remember When It Matters: Proactive Memory Agent for Long-Horizon Agents — LLM Agents & Autonomous Research


---

*本周摘要是每日速递的汇总；如需逐篇细读请回到对应日期。 / This weekly digest rolls up the daily digests; for per-paper detail, return to each day.*

[2026-07-06](../../2026-07-06/overview.md) · [2026-07-07](../../2026-07-07/overview.md) · [2026-07-08](../../2026-07-08/overview.md) · [2026-07-09](../../2026-07-09/overview.md) · [2026-07-10](../../2026-07-10/overview.md)
