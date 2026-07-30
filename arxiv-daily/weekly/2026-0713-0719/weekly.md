---
title: "Weekly arXiv Digest — 2026-07-13–2026-07-19"
week: 2026-0713-0719
date_range:
  - 2026-07-13
  - 2026-07-17
tags:
  - self-evolving-agents
  - mechanistic-interpretability
  - agent-evaluation
  - training-dynamics
  - quantization-efficiency
  - llm-reliability
papers: 183
---

# 每周 arXiv 速递 / Weekly arXiv Digest — 2026-07-13–2026-07-19

本周共收录 **183** 篇去重论文，覆盖 2026-07-13 至 2026-07-17 五个交易日。主线集中在**自演化智能体与自动化科研**（一周最大主题，12 篇）、**机制可解释性与探测**、**对评测/训练经验法则的反驳**（harness 演化、答案条件蒸馏、Edge-of-Stability、冷却调度）、**量化与高效推理**、以及**RLVR/校准的可靠性**。

This week indexes **183** unique papers across 2026-07-13 → 2026-07-17. The dominant arcs are **self-evolving agents & automated research** (the week's largest cluster, 12 papers), **mechanistic interpretability & probing**, a wave of **refutations of accepted eval/training heuristics** (harness evolution, answer-conditioned distillation, Edge-of-Stability, LR cooldown), **quantization & efficient inference**, and **RLVR/calibration reliability**.

---

## 本周必读 / Must Read This Week

> 若只读八篇，读这些。优先选取跨日复现或当日必读的论文。
> If you read nothing else this week, read these — prioritized by cross-day recurrence and daily-must-read status.

### [[2607.12227]] Rethinking Harness Evolution Evaluation

- **推荐理由：** 在统一反馈与推理预算下，harness 演化既未稳定超越并行采样等简单基线（pass@1 75.8 vs 并行采样 86.0），演化出的 harness 也几乎不泛化到 held-out 任务（平均仅 +0.6 分），提示当前收益主要来自额外测试时搜索——直接证伪了一个热门方向。
- **Why read:** Under matched feedback and inference budgets, harness evolution neither consistently beats simple baselines (pass@1 75.8 vs parallel sampling 86.0) nor generalizes to held-out tasks (avg +0.6 points), showing reported gains stem from extra test-time search rather than genuine harness design — a sharp falsification of a fashionable subfield.

### [[2607.12266]] Saturation Quantization Coverage Model

- **推荐理由：** 把混合精度量化损失形式化为布尔立方体上的集合函数，证明 4-bit 下 85–99% 方差来自一阶项（根源是"饱和"），并据此给出闭式误差下限；在匹配内存下比 NVIDIA ModelOpt 基线低 17–21% KL 散度，子 4-bit 区间决定模型能否存活。
- **Why read:** Reframes mixed-precision quantization loss as a set function and proves 85–99% of variance is first-order at W4A4 (root cause: saturation), giving a closed-form error certificate; beats the production NVIDIA ModelOpt baseline by 17–21% KL at matched memory and decides model survival below 4 bits.

### [[2607.12279]] Countdown Subcircuit

- **推荐理由：** 通过因果干预在 Llama-3.1-70B 中定位出三个"倒计时注意力头"，并证明同一子回路在推文、SHA-256、俳句、DNA 等任务中被复用，其几何与 Claude 3.5 Haiku 的换行回路一致——为"跨任务甚至跨模型的共享机制"提供了干净实证。
- **Why read:** Using activation patching the authors isolate three "countdown" attention heads in Llama-3.1-70B and show the same subcircuit is reused across tweets, SHA-256 hashes, haikus and DNA, with key/query geometry matching Claude 3.5 Haiku's line-wrapping circuit — concrete evidence for motifs shared across both tasks and models.

### [[2607.14552]] Answer-Conditioned CoT Degrades

- **推荐理由：** 用一个"控制单一变量"的实验干净地证明——让生成器在看到金答案后再写 CoT（即使最终答案正确）也会显著伤害学生模型的可验证推理能力，Qwen3-8B 在 MATH-500 上掉 16.2 分；直接冲击当下主流的"答案条件蒸馏"数据构造范式。
- **Why read:** A pristine one-bit controlled experiment shows that letting the generator write CoT after seeing the gold answer (even when correct) measurably degrades a student's verifiable reasoning — Qwen3-8B drops 16.2 points on MATH-500 — directly challenging the dominant answer-conditioned distillation recipe and immediately actionable for SFT data pipelines.

### [[2607.13631]] Hessian-Spectrum Depends on Data

- **推荐理由：** 在广义 Gauss-Newton 近似下给出任意宽度/深度线性网络 Hessian 特征值的闭式表达，并证明 MSE 分类解的锐度正比于最大类别占比 α_max——与 Cohen 等人 Edge-of-Stability 的两条经验论断直接矛盾，把训练稳定性归因到数据几何而非模型规模。
- **Why read:** Derives closed-form Hessian eigenvalues (via the GGN approximation) for linear networks of arbitrary width/depth and proves solution sharpness for MSE classification is proportional to the maximum class proportion α_max, directly contradicting two empirical claims of the Edge-of-Stability literature — re-rooting training stability in data geometry rather than model size.

### [[2607.13683]] GSME Self-Evolving Harness

- **推荐理由：** GSME 把"提出修改"与"归因增益"分离，由更强模型诊断失败写补丁，由确定性代码负责采样与三道门控（有效性/激活/配对 2σ 显著性），跨 7 个领域在冻结模型上拿到 +9~+15.5pp 的封存测试增益（保留训练增益的 86–147%）——补上了自演化 agent 一直欠缺的"可信归因"与"held-out 泛化"两块证据。
- **Why read:** GSME separates proposal from credit in a git-tracked self-evolving loop — a stronger model diagnoses failures and writes patches while deterministic code owns sampling and three gates (validity, activation, paired-2σ significance); it earns +9 to +15.5pp sealed-test gains across seven domains on a frozen model (retaining 86–147% of the training lift), supplying the trustworthy-credit-assignment and held-out-generalization evidence self-evolving-agent work has most lacked.

### [[2607.13918]] Partially Correlated Verifier Cascades

- **推荐理由：** 用 de Finetti 把每个错误实例的假接受率建模为潜在变量，证明级联后验对门数 k 严格凹、Beta 潜变量下失败概率按幂律（而非指数）衰减、盲点质量给出可靠性上限；独立性外推把失败率低估 20×（k=5）到约 3000×（k=10），核心结论是"把钱花在去相关而非加门"。
- **Why read:** Treats each erroneous instance's false-accept rate as a latent variable and proves the cascade posterior is strictly concave in k, that failure decays polynomially (not exponentially) under Beta latents, and that blind-spot mass caps the reliability ceiling; independence-based extrapolation underestimates the failure rate by 20× at k=5 and ~3000× at k=10 — the actionable lever is decorrelation (different model family/modality/oracle), not more gates.

### [[2607.14530]] xHC: Expanded Hyper-Connections

- **推荐理由：** xHC 是首个将 Hyper-Connections 的残差流扩展率 N 从 4 显著推到 16 的方法，通过多尺度因果卷积 + 稀疏残差流架构，在 18B/28B MoE 上让下游平均提升约 4.5 个点且 pretraining FLOPs 反而更低——本周最有工程价值的 Transformer 架构创新。
- **Why read:** xHC is the first Hyper-Connections variant to push the residual-stream expansion rate N meaningfully beyond 4 (up to 16); on 18B/28B MoE it lifts downstream average by ~4.5 points while *lowering* pretraining FLOPs — the most engineering-relevant architecture paper of the week for anyone tracking Transformer/MoE pretraining.

---

## 本周主题脉络 / Themes This Week

### 1. 自演化智能体与自动化科研 / Self-Evolving Agents & Automated Research

一周最大主线。核心是 [[2607.13683]] GSME 用三道统计门控补上"可信归因"，[[2607.14777]] SEED 让策略自做 hindsight 分析做密集蒸馏（ALFWorld 75→91.8），[[2607.14431]] 用字节精确 KV 嫁接把冻结小模型变成可信知识飞轮。自动化科研侧涌现一批可审计系统：[[2607.13608]] 自动发现生物 ODE、[[2607.14178]] 多智能体应用数学发现、[[2607.15001]] LQCDMaster 复现 63/70 格点 QCD 专家任务、[[2607.15079]] BrainPilot 脑科学、[[2607.15247]] AutoSynthesis 端到端 PRISMA 元分析（g=0.143 与专家一致）。反例来自 [[2607.12227]] 证伪 harness 演化与 [[2607.14004]] 质疑优化器是否真复利。

The week's largest arc. [[2607.13683]] GSME adds statistical gating for trustworthy credit assignment, [[2607.14777]] SEED turns the policy into its own hindsight analyzer (ALFWorld 75→91.8), and [[2607.14431]] grafts byte-exact KV state to make a frozen small model a verified knowledge flywheel. Automated research produced several auditable systems: [[2607.13608]] discovers biological ODEs, [[2607.14178]] does applied-math discovery, [[2607.15001]] reproduces 63/70 lattice-QCD tasks, [[2607.15079]] automates brain-science discovery, and [[2607.15247]] runs end-to-end PRISMA meta-analysis (g=0.143 matching experts). Counterpoint: [[2607.12227]] falsifies harness evolution and [[2607.14004]] questions whether optimizers truly compound.

代表 / Highlights: [[2607.13683]] · [[2607.14777]] · [[2607.14431]] · [[2607.15001]] · [[2607.15247]] · [[2607.12227]]

### 2. 机制可解释性与探测 / Mechanistic Interpretability & Probing

可解释性本周双重推进：一边定位**可复用的机制回路**，[[2607.12279]] 在 Llama-3.1-70B 中找到跨任务（推文/SHA-256/俳句/DNA）甚至跨模型（几何匹配 Claude 3.5 Haiku）复用的"倒计时子回路"；[[2607.11990]] 揭示 FFN 跨层稀疏依赖、[[2607.12166]] 用 SAE 因果审计追踪叠加到单语义的演化。另一边把**内部结构当操控对象**：[[2607.15175]] 在 25 个模型上验证合语法性是线性可解码方向、[[2607.15218]] 分离出"物理危险"与"内容危险"两个隐藏态方向（单层探针 86% 准确）、[[2607.14943]] 用 LQR 闭环把鲁棒性转向 WAM 激活（LIBERO +41pp）、[[2607.12985]] 因果识别报告坐标并用反事实钳制兼顾抵抗与更新。

Interpretability advanced on two fronts. One localizes reusable circuits: [[2607.12279]] finds countdown heads in Llama-3.1-70B reused across tweets/SHA-256/haiku/DNA and even matching Claude 3.5 Haiku's geometry; [[2607.11990]] maps sparse inter-layer FFN dependencies and [[2607.12166]] traces superposition-to-monosemanticity via SAE causal audits. The other treats internals as manipulable: [[2607.15175]] verifies grammaticality is a linear direction across 25 models, [[2607.15218]] separates physical- vs content-danger directions (single-layer probe 86% acc), [[2607.14943]] uses closed-loop LQR to steer WAM activations (LIBERO +41pp), and [[2607.12985]] causally identifies report coordinates and clamps them for dual control.

代表 / Highlights: [[2607.12279]] · [[2607.15175]] · [[2607.15218]] · [[2607.14943]] · [[2607.12985]] · [[2607.11990]]

### 3. LLM 评测、校准与可靠性反思 / LLM Evaluation, Calibration & Reliability Re-examination

贯穿全周的是"对评测经验法则的反驳"。[[2607.12227]] 证伪 harness 演化优势；[[2607.14552]] 一比特实验证明答案条件 CoT 伤可验证推理（MATH-500 掉 16.2 分）；[[2607.13707]] 揭示共用 max_tokens 制造假跨语言偏差且逃过四重稳健性检验；[[2607.14480]] 显示评估器在 23 语言下系统偏宽（ρ=−0.81）；[[2607.15190]] 模拟 18000 条件证明经典 IRT 在大基准上失效；[[2607.15277]] 用全概率公式检验指出前沿模型普遍违反统计自洽性。校准侧 [[2607.13753]] 三阶段分析后训练如何偏移置信度，[[2607.14528]] 证明高准确率≠逻辑一致。

The week's throughline is refuting accepted eval heuristics. [[2607.12227]] falsifies harness evolution; [[2607.14552]]'s one-bit experiment shows answer-conditioned CoT costs 16.2 MATH-500 points; [[2607.13707]] shows shared max_tokens fabricates a cross-lingual bias surviving four robustness checks; [[2607.14480]] finds evaluators systematically lenient across 23 languages (ρ=−0.81); [[2607.15190]] simulates 18,000 conditions to show classical IRT fails on large benchmarks; [[2607.15277]] checks the law of total probability and finds frontier models violate statistical self-consistency. Calibration: [[2607.13753]] analyzes how post-training shifts confidence, [[2607.14528]] shows high accuracy ≠ logical consistency.

代表 / Highlights: [[2607.14552]] · [[2607.12227]] · [[2607.13707]] · [[2607.14480]] · [[2607.15190]] · [[2607.15277]]

### 4. 量化、高效推理与计算可靠性 / Quantization, Efficient Inference & Computation Reliability

量化方向本周的理论明星是 [[2607.12266]]（饱和覆盖模型，85–99% 方差来自一阶项，比 ModelOpt 低 17–21% KL）。系统/硬件侧 [[2607.13649]] CIMERA 存算互连、[[2607.13898]] FPGA MXFP 张量块、[[2607.14618]] PolyQ 逐通道 {2,3,4,8,16}-bit CPU 量化、[[2607.12550]] JoLT 把 KV cache 视为三阶张量做近无损压缩。可靠性理论本周给出可立即落地的指导：[[2607.13918]] 证明级联验证器失败率按幂律（非指数）衰减、独立性外推低估 3000×，应把钱花在去相关而非加门。

The theoretical star of quantization this week is [[2607.12266]] (saturation coverage model: 85–99% of variance is first-order, 17–21% lower KL than ModelOpt). Systems/hardware: [[2607.13649]] CIMERA compute-in-interconnect, [[2607.13898]] FPGA MXFP tensor block, [[2607.14618]] PolyQ per-channel CPU quantization, [[2607.12550]] JoLT treating the KV cache as a 3rd-order tensor for near-lossless compression. Reliability theory delivers immediately actionable guidance: [[2607.13918]] proves verifier-cascade failure decays polynomially (not exponentially), independence-based extrapolation underestimates by 3000×, and the lever is decorrelation rather than more gates.

代表 / Highlights: [[2607.12266]] · [[2607.13918]] · [[2607.13649]] · [[2607.14618]] · [[2607.12550]] · [[2607.13898]]

### 5. 训练动力学、优化与采样理论 / Training Dynamics, Optimization & Sampling Theory

理论侧本周最锋利的是 [[2607.13631]]（锐度∝α_max，反驳 Edge-of-Stability，把稳定性归因到数据几何）。优化器诊断上 [[2607.14516]] 在算力严格匹配下证明 RK3(2)-Adam 训练损失低 40× 但泛化无收益、"自适应"步长实为惰性，[[2607.14536]] 把 Muon 的矩阵化重定义为几何选择。训练理论还包括 [[2607.14576]] 残差块速度场亚线性增长 q≤1 是稳定性尖锐阈值、[[2607.12438]] Fisher 有效秩膨胀作为记忆谱签名、[[2607.12360]] 冷却是否有益由噪声结构而非损失决定。采样/集成理论有 [[2607.14862]] 首个驯服版 SGHMC、[[2607.14889]] 把 Bartlett 校准风险推广到 m 维。

The sharpest theoretical result is [[2607.13631]] (sharpness ∝ α_max, contradicting Edge-of-Stability and rooting stability in data geometry). Optimizer diagnostics: [[2607.14516]] shows under compute-matched protocol RK3(2)-Adam lowers full-batch loss 40× but yields no generalization gain — the "adaptive" step is effectively inert — and [[2607.14536]] reframes Muon's matrixization as a geometric choice. Training theory also includes [[2607.14576]] (sublinear velocity growth q≤1 is the sharp residual stability threshold), [[2607.12438]] (Fisher rank inflation as a spectral signature of memorization), and [[2607.12360]] (cooldown's benefit is set by noise structure, not the loss). Sampling/ensemble theory: [[2607.14862]] (first tamed SGHMC) and [[2607.14889]] (generalizing Bartlett's calibrated risk to m dimensions).

代表 / Highlights: [[2607.13631]] · [[2607.14516]] · [[2607.14536]] · [[2607.14576]] · [[2607.12438]] · [[2607.12360]]

### 6. 智能体系统、安全与 RLVR 病理 / Agent Systems, Safety & RLVR Pathologies

智能体应用与安全工程本周有 [[2607.11388]] StructAgent（OSWorld-Verified 78.9% 开源 SOTA）、[[2607.12625]] KnowAct-GUIClaw（MobileWorld 64.1% 超 GPT-5.5）。失败归因侧 [[2607.12747]] Oat 仅用约 100 条成功轨迹训练 Neural CDE 做步骤级异常定位（F1 超 GPT-4o/5 +20%、快 200–5000×）、[[2607.14275]] 指出 agent 失败的根因常在上下文而非模型。RLVR 病理诊断上 [[2607.12640]] 以罕见统计严谨性给出 GRPO 在已掌握任务上的受控零结果并用权重嫁接因果定位损伤。安全侧 [[2607.14890]] 把编码 agent 的"已测试/已合并"声明重定义为需证据裁决的 claim（9,240-cell 预注册消融削减假通过 76%）。

Agent applications and safety engineering this week include [[2607.11388]] StructAgent (OSWorld-Verified 78.9% open-source SOTA) and [[2607.12625]] KnowAct-GUIClaw (MobileWorld 64.1% beating GPT-5.5). Failure attribution: [[2607.12747]] Oat trains a Neural CDE on ~100 successful trajectories for per-step anomaly localization (F1 beats GPT-4o/5 prompting by +20%, 200–5000× faster), and [[2607.14275]] argues agent failures usually originate in the context, not the model. On RLVR pathology, [[2607.12640]] delivers a controlled null of GRPO on mastered tasks with rare statistical rigor and a weight-grafting causal mechanism. Safety: [[2607.14890]] reframes coding-agent lifecycle claims as admissibility decisions requiring evidence (9,240-cell pre-registered ablation cuts false passes by 76%).

代表 / Highlights: [[2607.11388]] · [[2607.12625]] · [[2607.12747]] · [[2607.14275]] · [[2607.12640]] · [[2607.14890]]

---

## 全部论文 / All Papers

### 2026-07-13 (44)

- [[2607.10970]] Enhanced Byzantine-Robust Federated Learning Via Truncated-Quadratic Loss for Heterogeneous Data — 截断二次 (TQ) 损失聚合器达阶最优鲁棒性，MNIST ρ=0.5 下 91.5% vs Huber 9.8% / Truncated-Quadratic loss aggregator clips outliers for order-optimal Byzantine robustness (91.5% vs 9.8% Huber).
- [[2607.11007]] TabPFN beyond Tabular Data: Calibration and Accuracy on Multimodal Embeddings — TabPFN 作零训练分类头接冻结多模态编码器，NLL/ECE 平均最佳排名 / TabPFN as training-free head on frozen multimodal encoders wins best mean rank on NLL & ECE (ECE 2.1–5.3× lower).
- [[2607.11022]] When the Reward Suite Is Leaky: A Preregistered Causal Contrast of Natural Verifier False Positives in RLVR — 预注册因果对照显示 MBPP 泄漏奖励损害在 1–1.5B/400 步内被限制在 1.5pt，约半数为真实错误代码买单 / Preregistered causal study bounds reward-leak harm to ≤1.5pt at 1–1.5B/400 steps; ~47% pays for wrong code.
- [[2607.11052]] Domain-Aware Scaling Laws Uncover Data Synergy — 领域感知缩放律量化数据协同，最优 vs 反最优 HumanEval 改善 31–38% BPB / Domain-aware scaling laws quantify data synergy; 31–38% BPB gap optimal vs anti-optimal on HumanEval.
- [[2607.11079]] Are LLMs Ready for Scientific Discovery? A Capability-Oriented Benchmark for AI Scientists — SDABench 以六种科学推理能力评测，模型在机制/因果任务断崖式下降，跨度>50pt / Probes six scientific-reasoning capabilities; frontier models cliff-drop on causal/mechanistic tasks (>50pt spread).
- [[2607.11081]] Controlling Motion Transfer in Diffusion Transformers via Attention Heads — 首次发现视频 DiT 中运动/结构专用注意力头，免训练 HALO 运动保真度 62.5→66.2 / First discovery of motion/structure attention heads in video DiT; training-free HALO lifts motion fidelity 62.5→66.2.
- [[2607.11084]] NVAITC AI Scientist: A Governed End-to-End Research System — A Hypertension GWAS Case Study — 治理优先的端到端智能体研究系统，28.6 万人高血压 GWAS 复现 FGF5 等位点，DILI AUC 提至 0.842 / Governed agentic system replicates hypertension GWAS loci (FGF5) on 286k people; lifts DILI AUC to 0.842.
- [[2607.11098]] AgentCheck: A Reproduce–Intervene–Mitigate Workbench for LLM Agents over MCP — 把 MCP 变成可干预故障注入面，最强 agent 105/120、最弱 77/120，陈旧数据故障无法缓解 / Turns MCP into a fault-injection surface; 28pt agent spread, stale-data faults unmitigable.
- [[2607.11116]] The Equilibrium Is the Initialization: Lazy Identity Collapse in Physics-Structured Deep Equilibrium Reasoning — 负面结果：port-Hamiltonian DEQ 均衡点等于初始点，隐式计算是空操作 / Negative result: port-Hamiltonian DEQ equilibrium equals init; implicit compute is a silent no-op.
- [[2607.11122]] Implicit Neural Networks as Static Controllers: Certificates and Performance Separation — 隐式神经控制器稳定性/LQ 性能可写成 LMI，静态 ReLU 严格优于有限阶动态线性控制器 / Implicit neural controllers give LMI certificates; static ReLU provably beats finite-order dynamic linear controllers.
- [[2607.11149]] The Hidden Footprint: Making Storage a First-Class Metric for LLM Agent Evaluation — 首个跨框架智能体存储足迹基准，同等精度下留存字节相差 15.7× / First cross-framework agent storage-footprint benchmark; 15.7× persisted-byte spread at identical accuracy.
- [[2607.11163]] Unified Gradient Projection: Language-Balanced Continual Learning for Multilingual Low-Resource ASR — 多语 ASR 持续学习 / Multilingual ASR continual learning
- [[2607.11170]] TC-MAF: Train-Calibrated Bounded Multi-Evidence Fusion for Multimodal Industrial Anomaly Detection — 像素级凸融合多模态证据，MVTec-3D 达 0.979 I-AUROC / Convex-fuses multimodal evidence; 0.979 I-AUROC on MVTec-3D.
- [[2607.11175]] The Path to Self-Evolving Clinical Systems: Scaling Medical Agents from Assistance to Autonomy — 综述：医学影像 agent 三级自治分类与"框架/能力/环境"三轴 scaling / Survey: medical-imaging agents via three-level autonomy & framework/capability/environment scaling spine.
- [[2607.11193]] REPTRAN: Search-Based Repair of Transformer Models — 搜索式修复 Transformer FFN，平均修复率 74.7% vs ARACHNE 17.1% / Search-based Transformer repair; 74.7% repair rate vs ARACHNE's 17.1%.
- [[2607.11211]] FastTPS: An Optimized Method for LLM Token Phase for AI Accelerators — LLM 解码 NPU 加速 / LLM decode NPU speedup
- [[2607.11214]] A Novel Method to Evaluate Models on Unreliable, Noisy and Inconsistent Labels (ARLA) — 推理时按子块重采样+阈值抑制标签噪声，洪水分割 precision 0.52→0.80 / Inference-time subpatch re-binning denoises labels; precision 0.52→0.80.
- [[2607.11226]] Heterogeneous Agent Cohorts for Safe Open-Ended Exploration with Runtime Constraint Memory — 异构小队分离探索与安全，AgentHarm 0% 越界 vs ReAct 14.2% / Heterogeneous cohort separates exploration from safety; 0% breach on AgentHarm vs 14.2% ReAct.
- [[2607.11250]] Multi-Agent LLMs Fail to Explore Each Other — 当前 LLM 智能体过早承诺、不探索对方，MACE (LinUCB) 显著降遗憾 / LLM agents fail to explore peers; MACE cuts regret and lifts HotpotQA EM.
- [[2607.11266]] Valid ≠ Necessary: Diagnosing Latent Inefficiency in Chain-of-Thought — 评估器只判对错不判必要，PACE 压缩 token 降 31–53% 精度基本不变 / Evaluators miss "valid but unnecessary" CoT steps; PACE cuts tokens 31–53% near-zero loss.
- [[2607.11267]] Enhancing LLMs through human feedback: a journey towards self-improvement — FLARE 双路检索注入用户反馈，Trivia 评分 3.06→3.91 / FLARE injects user feedback via dual retrieval; Trivia 3.06→3.91.
- [[2607.11288]] Mako: A Self-Evolving Agentic Operating System (SE-AOS) for Autonomous Web Exploitation — 自进化智能体 OS 在 XBOW-104 取 104/104 全覆盖，能力而非推理是瓶颈 / Self-evolving agentic OS hits 104/104 on XBOW-104; capability — not reasoning — is the bottleneck.
- [[2607.11289]] Backpropagation as a Nilpotent Linear System — 将反向传播重写为幂零线性系统，Neumann 级数恰 L 项终止 / Backprop recast as a nilpotent linear system; Neumann series terminates in exactly L terms.
- [[2607.11317]] Calibrated e-CUSUM Decoding for Quantized Reasoning Models — 校准 e-CUSUM 控制器把量化模型解码监控误报从 93–95% 降至可用水平 / Calibrated e-CUSUM controller makes the decoding monitor for quantized reasoning models usable (FP 93–95%→selective).
- [[2607.11327]] PRISM Edit: One Vector for All Temporal Answers — 时序知识单向量编辑 / Temporal knowledge single-vector edit ↻07-15
- [[2607.11347]] From Neural Network Decisions to Training Cases: An Exact Account via Case-Based Decision Theory — 证明 OLS 读出层可精确分解为训练样本回报加权和，免再训练审计 / Exact case-based decomposition of OLS readout; retraining-free audit (Top-30 consistency 0.941).
- [[2607.11359]] Efficient Tuning Before Low-Bit Post-Training Quantization for SGD-optimized Models — ETBQ 在 PTQ 前注入量化误差扰动，ImageNet MobileNetV2 W2A4 +8.53% / Pre-conditions before PTQ; +8.53% on ImageNet MobileNetV2 W2A4.
- [[2607.11368]] Decomposing Runtime, Kernel, and Quantization Speedups via a Matched FP16 Intermediate — 用匹配 FP16 基线拆分 vLLM-Marlin 加速，运行时占 2/3 对数增益 / Matched FP16 baseline decomposes vLLM-Marlin speedup; runtime carries 2/3 of log-gain.
- [[2607.11388]] StructAgent: Harness Long-horizon Digital Agents with Unified Causal Structure — 统一状态+结构化工作流，OSWorld-Verified 78.9% 开源 SOTA / Unified verifier-backed task state; OSWorld-Verified 78.9% open-source SOTA (+30.6 on 27B).
- [[2607.11414]] Confidently Wrong: Detecting Hallucinations in Financial Question Answering from LLM Internal States — 残差流线性探针检测金融问答幻觉，自信答案 AUROC +0.13~0.15 / Residual-stream probes detect "confidently wrong" finance-QA hallucinations (+0.13–0.15 AUROC).
- [[2607.11444]] Unlocking Every Expert in Domain-Specific Training — UMoE 重组专家池后再 SFT，数学均分 +3.40、SWE-bench +6.0 / Reorganizes MoE expert pool before SFT; +3.40 math avg, +6.0 SWE-bench, no extra inference cost.
- [[2607.11475]] HyperSafe: Inference-Time Safety Recovery for Fine-Tuned Language Models — 超网络从激活指纹生成安全侧网络，有害率 19–31%→<1% / Hypernetwork-generated side-network cuts harmful rate 19–31%→<1% without touching weights.
- [[2607.11541]] Random Label Prediction Heads for Studying Memorization in Deep Neural Networks — 记忆度量与正则化 / Memorization metric & regularization
- [[2607.11542]] Condition-Stratified Robustness Analysis of Post-Hoc Calibration Methods for Probabilistic Classifiers — 预注册条件分层分析温度缩放 vs 保序回归，结论高度依赖条件与指标 / Pre-registered condition-stratified study; TEMP directionally better but conclusion condition/metric-dependent.
- [[2607.11586]] HCRMap: Pressure-Aware Hot-Expert Residency Mapping for 3.5D MoE Chiplet Inference — MoE chiplet 专家驻留 / MoE chiplet expert residency
- [[2607.11598]] Interaction Scaling: Grounding the Third Axis of Test-Time Compute — 把测试时计算归纳为三轴，接地交互把硬代码任务 66.7%→100% / Frames test-time compute as 3 axes; grounded interaction lifts hard-code 66.7%→100%.
- [[2607.11607]] Auditing the Risk Claims of Distributional Reinforcement Learning — 决策级审计分布式 RL，40–95% 的"最强风险权衡"声明被证伪 / Decision-level audit refutes 40–95% of distributional-RL's strongest risk-tradeoff claims.
- [[2607.11666]] How to Tame Grokking: Representation Geometry as a Control Signal — GeomDR 几何正则化器加速 grokking 最多 52.5× / GeomDR spectral regularizer accelerates grokking up to 52.5×.
- [[2607.11698]] Agent Hacks Agent: Autoresearch for Production-Agent Red-Teaming — 把生产级智能体红队重构成自动研究循环，冻结 VCG 单次部署 ASR 47.0% / Reframes agent red-teaming as autoresearch; frozen VCG reaches 47.0% held-out ASR.
- [[2607.11751]] When Local Monitors Miss Compositional Harm: Diagnosing Distributed Backdoors in Multi-Agent Systems — 分布式后门突破局部监控可观测性边界，解码视图门把 ASR 1.00→0.00 / Distributed backdoors beat local monitors; decoded-view gate drops ASR 1.00→0.00.
- [[2607.11796]] An Exact Instrument for State Usage in Selective State-Space Models, and the Input-Driven Migration It Reveals — Mamba SSM 的精确状态使用测量工具，揭示随输入的模式迁移 / Exact Mamba state-usage instrument reveals input-driven mode migration; matches full model at half budget.
- [[2607.11801]] Encoder-Side Neuron Identification and Amplification for Acoustic Perception in Large Audio-Language Models — IAAN 推理时放大编码器音频感知神经元，VoxParadox +25.7 pp / Amplifies encoder audio neurons at inference; +25.7 pp on VoxParadox.
- [[2607.11871]] Inside the Unfair Judge: A Mechanistic Interpretability Account of LLM-as-Judge Bias — 表示层解释评判偏差，双向引导恢复公平，未见基准预测 AUC 0.82 / Representation-level account of judge bias; steering restores fairness, predicts failure AUC 0.82.
- [[2607.11875]] Invariant Learning Dynamics of Transformers in Inductive Reasoning Tasks — 归纳推理任务中 Transformer 的低维不变流形，刻画 ICL/IWL 电路竞争 / Invariant manifold traps GD trajectories in inductive-reasoning Transformers; ICL/IWL circuit competition.

### 2026-07-14 (39)

- [[2607.12227]] Rethinking Harness Evolution Evaluation — 统一预算 + disjoint 评估证伪 harness 演化优势，held-out 仅 +0.6 分，增益主要来自额外搜索。 / Unified-budget + disjoint-split evaluation falsifies harness evolution's advantage (held-out +0.6 pts); gains are mostly extra search. ⭐ ↻07-15
- [[2607.12252]] FinResearchBench II — 104 真实金融查询 × 10 报告，经一致性 + 可区分性过滤得到 2,600 条"共识金标准"评分细则，对 10 个深度研究产品给出 22%–59% 的清晰分层。 / 104 real financial queries × 10 reports, filtered to 2,600 consensus gold rubrics, cleanly tiering 10 deep-research products from 22%–59% pass rate.
- [[2607.12254]] Recursively Self-Improving Agents — 提出受治理的多智能体架构（目标/范围/工具/基准契约）以实现递归自我改进，并定义"个人奇点"为有界目标；纯立场论文，无实验。 / A governed multi-agent architecture (goal/scope/tool/benchmark contracts) for recursive self-improvement, with "personal singularity" as a bounded objective; position paper, no experiments. ↻07-15
- [[2607.12266]] Saturation Quantization Coverage Model — 把量化损失分解为一阶主导（85–99% 方差，根源是饱和），给出闭式误差下限，匹配内存下比 ModelOpt 低 17–21% KL，子 4-bit 区间决定模型存活。 / Decomposes quantization loss as first-order dominated (85–99% variance, cause: saturation), gives a closed-form certificate, beats ModelOpt by 17–21% KL at matched memory, decides survival below 4 bits. ⭐ ↻07-15
- [[2607.12273]] Code-MUE — 纯黑盒、基于执行的代码不确定性量化：构建语义交互图并用 Von Neumann 熵，与功能正确性的 Spearman 相关高达 -0.98，远超词法基线。 / Black-box execution-based code uncertainty via Semantic Interaction Graphs + Von Neumann entropy; Spearman ρ up to -0.98 with correctness, far beating lexical baselines. (ISSTA 2026)
- [[2607.12279]] Countdown Subcircuit — 因果定位三个"倒计时注意力头"，跨任务（推文/SHA-256/俳句/DNA）甚至跨模型（Claude 3.5 Haiku 几何一致）复用。 / Causally isolates three "countdown" attention heads reused across tasks (tweets/SHA-256/haiku/DNA) and even across models (geometry matches Claude 3.5 Haiku). ⭐ ↻07-15
- [[2607.12298]] EIR FPGA Self-Healing — 层次化数字孪生（Rabbit 快检 + Tortoise 精确恢复）在 FPGA SoC 上实现自愈，≥95% 故障检出率且保持基线面积，DMR 则把功耗提升 +89%。 / Hierarchical digital twins (Rabbit fast-detect + Tortoise precise-recover) enable FPGA SoC self-healing at ≥95% detection preserving baseline area, vs DMR's +89% power. ↻07-15
- [[2607.12332]] Diagonal Linear Network Dynamics — 推广鞍点到鞍点动力学到深层与一般两层对角线性网络，证明隐式偏置是"修正的 ℓ1 范数"（权重依赖初始化方向），并用结构不变流形解释机制。 / Extends saddle-to-saddle dynamics to deep/general two-layer diagonal linear networks; implicit bias is a modified ℓ1 (weights depend on init direction), explained via Structural Invariant Manifolds. ↻07-15
- [[2607.12338]] How Many Tasks Are Enough — 重放 SWE-bench/AppWorld/tau-bench，定义"最小充分任务预算"，发现其随基准剧烈变化（AppWorld 15% vs SWE-bench Lite 95% 仍未达标），任务比例不是决策规则。 / Replays public agent benchmarks and defines a minimum sufficient task budget that varies sharply (AppWorld 15% vs SWE-bench Lite failing by 95%); task fraction is not a decision rule. ↻07-15
- [[2607.12360]] LR Cooldown Noise Structure — 证明冷却是否有益由噪声结构（各向同性 vs 各向异性）与优化器归一化共同决定，而非损失本身；同一损失同一噪声大小可产生相反效果。 / Shows cooldown's benefit is jointly set by noise structure (iso- vs anisotropic) and optimizer normalization, not the loss; same loss/noise can yield opposite outcomes.
- [[2607.12385]] PM-Bench Prospective Memory — 受认知科学"Virtual Week"启发，评测智能体"前瞻记忆"；最佳方法（GPT-5.4）仅 65.1% Set-F1，"该出手时不出手"仍是核心瓶颈。 / Adapts cognitive science's Virtual Week to test agent prospective memory; best setup (GPT-5.4) reaches only 65.1% Set-F1 — "acting at the right moment" remains the bottleneck.
- [[2607.12397]] Critic Experience Bank (CEB) — 免训练、自进化的评论家，用事后回看的执行经验做步骤级置信度估计，9/9 组合全部最优，ECE 相对最强基线降低高达 54%。 / Training-free self-evolving critic using hindsight execution experience for step-level confidence; best ECE/Brier/AUC in all 9 combos, cutting ECE up to 54%. ↻07-15
- [[2607.12438]] Fisher Rank Inflation — 发现含噪标签训练中 Fisher 有效秩在记忆噪声时先膨胀后塌缩，噪声样本在峰值期留一归因中高度富集（top-100 占比高达 96.2%），是记忆的谱签名。 / Identifies Fisher Rank Inflation — effective rank inflates then collapses during memorization; corrupted samples dominate peak-rank attribution (top-100 up to 96.2%), a spectral signature. ↻07-15
- [[2607.12447]] SDC Confidence in LLMs — 借用神经科学的统计决策置信度框架，证明 logit 差在简单感知/记忆任务上满足全部四签名，驱动近最优拒答（92.2%→99.95%），但在 CLEVR 复杂推理上失效。 / Imports the statistical-decision-confidence framework; logit difference satisfies all four signatures on perceptual/memory tasks and drives near-optimal abstention (92.2%→99.95%), but fails on CLEVR.
- [[2607.12455]] EvoQuant Trading — 把量化策略优化定义为"验证器引导的程序进化"，A 股 + 比特币 7 个策略家族平均 Sharpe +0.829，自适应晋升引擎是核心（去掉则跌至 +0.128）。 / Frames quant strategy optimization as verifier-guided program evolution; +0.829 avg Sharpe across 7 A-share/Bitcoin families, with the adaptive promotion engine as the key enabler. ↻07-15
- [[2607.12469]] Agent-Safety Reconstructability — 厂商中立的"重构性"指标，按八类决策属性打分；四张证据充分性卡 0.458–0.833，所有卡的反事实重放前置条件均未满足。 / A vendor-neutral reconstructability metric scoring 8 decision-property classes; sufficiency spans 0.458–0.833 and replay preconditions are unmet in all cards. ↻07-15
- [[2607.12474]] Mechanistic World Models — 立场论文：把科学发现重构为"知识组织"问题，提出以可复用"机制"为中心的表征范式，统一变量/机制/结构发现与简约性、组合性。 / Position paper reframing scientific discovery as knowledge organisation around reusable "mechanisms," unifying variable/mechanism/structure discovery with parsimony and compositionality.
- [[2607.12526]] Source-Grounded Feature Inversion — 把特征反演重构为沿源-局部计算 DAG 的闭式 Wiener 修复，单次标定复用，像素余弦 0.939 vs 迭代法 0.035，176× 在线加速。 / Reframes feature inversion as closed-form Wiener repair along the source-local DAG; one calibration reused, pixel cosine 0.939 vs 0.035 for iterative search, 176× faster online.
- [[2607.12545]] VanillaBench — 系统量化 186 个对抗训练模型相对 vanilla 基线的干净准确率差距，即使最强鲁棒模型也落后 vanilla SOTA 4–29 个百分点。 / Quantifies the clean-accuracy gap of all 186 RobustBench models vs vanilla references; even the most robust model trails vanilla SOTA by 4–29 pp.
- [[2607.12616]] FTSS Flow Matching Memorization — 提出有限时间谱敏感度，无梯度、仅前向传播地暴露流匹配的"谱坍缩"，谱坍缩比 M 在 N≥1000 时饱和至 ~1.0，无需访问训练集即可判定记忆。 / Proposes Finite-Time Spectral Sensitivity, a gradient-free forward-pass metric exposing spectral collapse in flow matching; ratio M saturates at ~1.0 for N≥1000, auditing memorization without training-pool access.
- [[2607.12625]] KnowAct-GUIClaw — "Know-Route-Act-Reflect" 闭环 + 类型化黑板 + 自演化技能库，在 MobileWorld 上以开源 Kimi-K2.6 取得 64.1% SOTA，超 GPT-5.5。 / Know-Route-Act-Reflect loop with typed blackboard and self-evolving skills reaches 64.1% SOTA on MobileWorld with open-source Kimi-K2.6, beating GPT-5.5.
- [[2607.12640]] GRPO Failure Web Agent — 在 4B/8B Qwen3-VL 上严格证明：对已掌握任务 GRPO 无可信提升，中高学习率反而损害能力；该零结果源于任务缺乏 headroom，并给出权重嫁接的因果机制。 / Rigorously shows GRPO adds no credible skill on mastered tasks (4B/8B Qwen3-VL) and mid/high LRs degrade it; the null is a headroom property, with a weight-grafting causal mechanism. ↻07-15
- [[2607.12687]] CARE-PPO — 把 PPO 的 critic 当作置信度估计器（奖励=预测误差单调函数），AUSE 相比 logit/verbalized 基线减半，仅 2.4% 额外推理延迟，OOD 下更鲁棒。 / Repurposes PPO's critic as a confidence estimator (reward = monotonic in error); halves AUSE vs logit/verbalized baselines at 2.4% extra latency, more robust OOD.
- [[2607.12735]] Grokking Representational Priors — 在模运算 grokking 上证明泛化由特征族对齐（而非"连贯性"）决定，完全无标签的交换不变性先验即足够，配合范数钳制获 17× 加速。 / Shows grokking generalization is gated by feature-family alignment (not coherence); a fully label-free commutativity prior suffices, and with a norm clamp yields 17× speedup.
- [[2607.12739]] ESFP Epistemic Stance — 固定内容、变化提问框架衡量"认知立场灵活性"；发现它与通用能力基本正交——27B 开源模型并列第一，旗舰 Gemini-3.1-Pro 反而垫底。 / Measures prompt-conditioned epistemic register shift; flexibility is orthogonal to capability — a 27B open model ties for first while flagship Gemini-3.1-Pro ranks last.
- [[2607.12747]] Oat Failure Attribution — 仅用约 100 条成功轨迹训练 Neural CDE，对失败轨迹做步骤级异常定位，F1 超 GPT-4o/5 提示法 +20%，推理快 200–5000×、零 token 成本。 / Trains a Neural CDE on ~100 successful trajectories only, flags per-step errors in failed runs; F1 beats GPT-4o/5 prompting by +20%, 200–5000× faster with zero token cost.
- [[2607.12767]] Bayesian Accuracy Length Bias — 揭示标准准确率偏短、长度归一化偏长，提出即插即用的"贝叶斯准确率"将长度偏差降低 4–8×，无需额外前向传播。 / Shows standard accuracy is short-biased and normalization is long-biased; proposes drop-in Bayesian accuracy cutting length bias 4–8× with no extra forward passes.
- [[2607.12780]] Quantum Circuit Autoregressive Drift — 44.8M Transformer 做量子电路优化，参数化电路达中位保真度 1.000，但 Clifford+T 因"自回归漂移"（长度主导）从 88% 跌到 ≥26 门的近 0%。 / A 44.8M transformer optimizes quantum circuits: median fidelity 1.000 on parameterized circuits, but Clifford+T exact-match collapses from 88% to ~0% beyond 26 gates due to autoregressive drift.
- [[2607.12790]] Double Ratchet — 把评估指标当作可演化对象（原子缺陷检测器组合 + 锚定 + 共识），与技能环路协同，恢复 88–110% 的 oracle 提升，并捕获一个真实 Goodhart 投机失败。 / Co-evolves an evaluation metric (compositions of atomic drawback detectors, anchored + consensus-regularized) with a skill loop, recovering 88–110% of oracle lift and catching a real Goodhart gaming failure. ↻07-15
- [[2607.12792]] JADR J-Space Safety — 用雅可比透镜在生成前读取 J-space 刻画"危险识别"，单次前向传播、无需裁判；INT8 基本无害，INT4 主要伤害 compliance 而非 safety。 / Reads J-space via the Jacobian lens before generation to score danger recognition; INT8 is essentially neutral, INT4 hurts compliance more than safety. ↻07-15
- [[2607.12796]] One-Word Census — 用 31 个"命名一个类别词"提示量化 44 个模型的从众性，跨度 1.05–3.21 比特，最新旗舰最从众；连"发散"本身也收敛到同一个亚军答案。 / Quantifies conformity of 44 models on 31 one-word prompts, spanning 1.05–3.21 bits; newest flagships conform most, and even divergence converges to the same runner-up.
- [[2607.12835]] LLM Rubric Meta-Evaluation — 首个针对论文复现的 LLM 生成 rubric 元评估；最强"蒸馏技能"设置在外在对齐上逼近人类（Spearman 0.78 vs 0.83），但仍偏细粒度、代码中心化。 / First meta-evaluation of LLM-generated rubrics for paper reproduction; strongest Distilled Skill setting nears humans (Spearman 0.78 vs 0.83) but stays over-fine-grained and code-centric. ↻07-15
- [[2607.12863]] ROBIN Attention Bias — 白盒头部级公平性调试：Fisher 敏感度排序 + 子空间投影去除偏置，BERT WinoBias 差距 45.97→19.14，且语言建模损失增加 ≤7.2%，远优于整头置零。 / White-box head-level fairness debugging via Fisher-sensitivity ranking + subspace projection; BERT WinoBias gap 45.97→19.14 with ≤7.2% LM loss increase, far better than whole-head zeroing.
- [[2607.12868]] Deep4ge DNN Faults — 发布 14,227 次 DNN 训练运行的公开故障轨迹数据集（27 变异算子 × 7 类故障），证明完整轨迹特征（MCC 0.227）显著优于末轮特征（0.150）。 / Releases 14,227 public DNN training-run trajectories (27 mutation operators × 7 fault categories); trajectory features (MCC 0.227) substantially beat final-epoch features (0.150). ↻07-15
- [[2607.12885]] LLM Judges Too Generous — 多语言 QA 上无参考答案时评判者过度放行（泰卢固语错误答案放行率高达 60%），引入参考答案最多翻转 85% 判定且更贴近人类。 / In reference-free settings judges over-credit incorrect answers (up to 60% on Telugu); reference-answer visibility flips up to 85% of verdicts toward human agreement.
- [[2607.12893]] MemOps Memory Benchmark — 把长期对话记忆重定义为生命周期操作（记忆/遗忘/更新/反思/轨迹），最强模型在长上下文重建有序状态轨迹时仍严重退化，session 级检索远胜 turn 级。 / Reformulates long-conversation memory as lifecycle operations; even top models degrade sharply at reconstructing ordered state trajectories under long context, and session-level RAG beats turn-level by ~23 pts.
- [[2607.12954]] PV Forecasting Robustness — 物理约束的 NWP 误差注入框架跨 5 美国气候区压测 6 个预测模型，LightGBM 干净数据最强但随噪声劣化，GRU/PatchTST 在中高噪声下更韧。 / Physically constrained NWP error-injection benchmark across 5 US climate zones; LightGBM is strongest on clean data but degrades fast, while GRU/PatchTST are more robust under noise.
- [[2607.12962]] PoPE Self-Repair — 预注册、安慰剂对照评估冻结小代码模型（≤1.5B）的"学习式错误条件自修复"，提示/权重两通道均未超过安慰剂孪生，并撤回自身最强正向收益。 / Preregistered placebo-controlled evaluation of learned self-repair in frozen small code models (≤1.5B); neither prompt nor weight channel beats form-matched placebo, and its own positive is withdrawn.
- [[2607.12963]] Illusion of Robustness — 揭示"鲁棒性错觉"：任务无关上下文下整体准确率几乎不变（±2.1%），但掩盖了严重的样本级双向波动（WTD 最高 53.2%），且 SFT/DPO 会放大它。 / Reveals an "illusion of robustness": aggregate accuracy is stable (±2.1%) under irrelevant context but masks large two-sided per-example flips (WTD up to 53.2%), amplified by SFT/DPO.

### 2026-07-15 (24)

- [[2405.11667]] Local SGD Limits & Potentials — 系统刻画 Local SGD 的极限与潜力 / Characterizes limits and potentials of Local SGD
- [[2511.04689]] ATLAS Adaptive Testing — 面向 LLM 的自适应测试评测 / Adaptive testing for LLM evaluation
- [[2602.19938]] R&Q Replicate-and-Quantize for MoE — 面向 MoE 的复制再量化方法 / Replicate-and-quantize method for MoE
- [[2603.06592]] Hierarchical Latent Structures — Interpretability
- [[2603.24787]] ReLope LoRA Probes for Routing — KL 正则化 LoRA 探针做 MLLM 路由 / KL-regularized LoRA probes for MLLM routing
- [[2605.05686]] Attractor Geometry of Transformer Memory — Interpretability
- [[2605.12765]] GUARD-IT Inference-Time Unlearning — 推理时按需遗忘的轻量化方案 / Lightweight inference-time unlearning on demand
- [[2605.22432]] AMUSE Anytime Muon Optimizer — 任意时刻可暂停的 Muon 优化器 / Anytime pausable Muon optimizer
- [[2606.04115]] dMX Differentiable Mixed-Precision — 可微混合精度量化 / Differentiable mixed-precision quantization
- [[2606.17930]] Inference Compute Shapes Frontier Eval — 推理算力如何重塑前沿 LLM 评测 / How inference compute reshapes frontier LLM eval
- [[2606.27321]] Sparsity Regularizers for Top-k SAEs — Interpretability
- [[2607.11183]] Amplitude-Only FFN Intervention — Inference Intervention
- [[2607.11990]] Sparse Inter-Layer FFN Dependencies — Interpretability
- [[2607.12085]] GenAI Eval for Conversational Agents — 会话式智能体的 GenAI 评估框架 / GenAI evaluation for conversational agents
- [[2607.12094]] SAID SAEs for OOD Detection — 用稀疏自编码器做 OOD 检测 / Uses sparse autoencoders for OOD detection
- [[2607.12113]] Trustworthy Autonomous Science (AISLE-2) — 可信自主科学智能体的路线图 / Roadmap for trustworthy autonomous science agents
- [[2607.12122]] AI-SC Agentic Operator Discovery — 智能体驱动的神经算子发现 / Agentic discovery of neural operators
- [[2607.12166]] SAE Causal Audit — Interpretability
- [[2607.12395]] Ring-Zero RL to 1T — 将 Zero RL 扩展到 1T 规模 / Scales Zero RL to 1T scale
- [[2607.12523]] OOD-RL-Bench — 强化学习轨迹 OOD 检测评测框架 / RL trajectory OOD detection benchmark framework
- [[2607.12550]] JoLT KV Cache Compression — Tucker + JL 残差的近无损 KV 压缩 / Near-lossless KV compression via Tucker + JL residual
- [[2607.12789]] AVQ-Attention — Efficient Attention
- [[2607.12815]] Visual Access Boundaries (VAB) — 因果掩蔽证明 CoT 不延长图像访问，瓶颈在读出 / Causal masking shows CoT does not extend image access; bottleneck is readout
- [[2607.12985]] Resist and Update (CRC) — 因果识别报告坐标并用反事实钳制兼顾抵抗与更新 / Causally identifies report coordinates and uses counterfactual clamp for dual control

### 2026-07-16 (50)

- [[2607.13608]] Auto ODE Discovery (Bio) — LLM agent 自动发现生物 ODE / LLM agent discovers biological ODEs
- [[2607.13631]] Hessian-Spectrum Depends on Data — GGN 下证明锐度 ∝ α_max,反驳 Edge-of-Stability / Proves sharpness ∝ α_max under GGN, contradicting Edge-of-Stability ⭐
- [[2607.13649]] CIMERA Compute-in-Interconnect — 可重构精度的存算互连 / Reconfigurable-precision compute-in-interconnect
- [[2607.13660]] CLIP Hyperspherical Geometry — 语义混合模型刻画 CLIP 超球几何 / Semantic mixture model for CLIP hyperspherical geometry
- [[2607.13683]] GSME Self-Evolving Harness — 提出与归因分离,配对 2σ 门控,+9~15.5pp held-out / Separates proposal from credit, paired-2σ gate, +9~15.5pp held-out ⭐
- [[2607.13707]] Test Oracle Problem LLM-as-Judge — max_tokens 共用制造假跨语言偏差,四重检验未发现 / Shared max_tokens fabricates cross-lingual bias surviving 4 robustness checks
- [[2607.13753]] Post-Training Shifts Confidence — 三阶段分析后训练如何改变置信度校准 / Three-stage analysis of how post-training shifts calibration
- [[2607.13898]] FPGA MXFP Tensor Block — 多精度 MXFP 的 FPGA 张量块 / Versatile FPGA tensor block for MXFP precisions
- [[2607.13899]] AIMO Interpretability Challenge — 鲁棒 vs 伪相关特征 / Robust vs spurious features in math reasoning
- [[2607.13918]] Partially Correlated Verifier Cascades — 相关门下凹性+幂律衰减,独立性低估 3000× / Concave + polynomial decay under correlation; independence underestimates 3000× ⭐
- [[2607.13940]] Self-Evolving Health Agent — 自演化个性化健康管理 / Self-evolving personalized health management
- [[2607.14004]] Do Agent Optimizers Compound? — Terminal-Bench 2.0 上优化器是否复利 / Whether optimizers compound on Terminal-Bench 2.0
- [[2607.14018]] Transforming Rank: Spectral Pathologies — 架构如何规避深度带来的谱病态 / How architecture navigates spectral pathologies of depth
- [[2607.14178]] ReasFlow Math Discovery — 知识驱动的应用数学发现 / Knowledge-based multi-agent for applied-math discovery
- [[2607.14181]] Quantize with Confidence? (Code Gen) — 量化对代码生成可靠性的实证 / Empirical study of quantization effects on code generation
- [[2607.14185]] Closed-Loop Knowledge Dynamics — 饱和与逃逸的操作框架 / Operational framework for saturation and escape
- [[2607.14228]] SeeSE3: 3D Space in Vision — 视觉特征里 SE3 三维结构的涌现 / Emergence of SE3 3D structure in vision features
- [[2607.14275]] Context Fails First — agent 失败的根因常在上下文而非模型 / Root cause of agent failure is often the context, not the model
- [[2607.14306]] ENTD: Trace to Training Data — 经验下一 token 分布追溯到训练数据 / Trace behavior to training data via empirical next-token distributions
- [[2607.14375]] Random Noise vs ReLU Verification — 随机参数噪声不能使 ReLU 验证变易 / Random parameter noise does not make exact ReLU verification easy
- [[2607.14399]] Instrument Effects in Honesty Eval — 单系统可审计地展示评测工具效应 / Auditable single-system demo of evaluation instrument effects
- [[2607.14408]] Reward-Free Evolving Agents — 成对验证器驱动的免奖励演化 / Reward-free evolution driven by a pairwise validator
- [[2607.14427]] Per-Token Fixed-Point Convergence — 逐 token 不动点收敛分析 / Per-token fixed-point convergence analysis
- [[2607.14431]] Byte-Exact KV-State Grafting Flywheel — 字节精确 KV 嫁接,冻结小模型变可信知识飞轮 / Byte-exact KV grafting turns a frozen small model into a verified flywheel
- [[2607.14463]] Hidden-State Collapse (LiDAR AE) — LiDAR 点云动力系统 AE 的深度塌缩 / Depth-dependent collapse in LiDAR point-cloud autoencoders ↻07-17
- [[2607.14480]] LLM Evaluators Biased across Languages — 点值分数随语言偏移,pairwise accuracy 掩盖 / Pointwise scores shift by language; pairwise accuracy hides it ↻07-17
- [[2607.14506]] Non-vacuous Bounds for RLVR — 首个 RLVR 非空 PAC-Bayes 界,Gumbel-max 外置随机性 / First non-vacuous PAC-Bayes bound for RLVR; Gumbel-max externalizes randomness ↻07-17
- [[2607.14516]] RK3(2)-Adam Compute-Matched Study — 严格按梯度计算量对齐后 RK3(2)-Adam 输给 Adam,控制器失效 / Under per-gradient compute matching, RK3(2)-Adam loses to Adam; step controller is inert ↻07-17
- [[2607.14528]] CRTBench: Logical Consistency — 等价改写下准确率高≠一致,推理增强反崩量化 / High accuracy ≠ consistency; reasoning effort collapses quantifier reasoning ↻07-17
- [[2607.14536]] Muse: Muon Representation Geometry — 把矩阵化当作设计轴,Vector 端点退化为 nSGDM / Reframes matrixization as a design axis; Vector endpoint collapses to nSGDM ↻07-17
- [[2607.14541]] Atrex-Bench: GPU Kernels — 最强 agent 仅达 roofline 10.7%,揭示正确性幻觉 / Best agent reaches 10.7% of roofline; exposes correctness illusion ↻07-17
- [[2607.14552]] Answer-Conditioned CoT Degrades — 一位比特实验:看答案 CoT 伤 MATH-500 16.2 分 / One-bit experiment: answer-conditioned CoT costs 16.2 MATH-500 pts ⭐ ↻07-17
- [[2607.14568]] Multimodal on 2011 Fermi GPU — 2011 年 6GB Fermi 跑通 MiniCPM-V,测量驱动 / Runs MiniCPM-V on 2011 6GB Fermi; measurement-driven
- [[2607.14576]] Sharp Stability Threshold (Residual) — 次线性增长原理 q≤1 为尖锐阈值,免归一化 / Sublinear-growth q≤1 is a sharp threshold; normalization-free ↻07-17
- [[2607.14618]] PolyQ: Edge CPU Quantization — {2,3,4,8,16} 调色板 + 编译期布局正则化 / {2,3,4,8,16} palette + compile-time layout regularization ↻07-17
- [[2607.14622]] ExaGEMM In-Register Computing — 支持点选择框架,剪枝 99.2% 候选 / Support-selection framework; prunes 99.2% of candidates
- [[2607.14658]] TopoAgent: Self-Evolving Topological — DAG 替代线性轨迹,上下文隔离 + 自适应裂变 / DAG replaces linear trajectories; context isolation + adaptive fission ↻07-17
- [[2607.14777]] SEED: Self-Evolving OPD — 同一策略既当 actor 又当事后 analyzer,ALFWorld 75→91.8 / Same policy as actor + hindsight analyzer; ALFWorld 75→91.8 ↻07-17
- [[2607.14791]] Transcoders for Deception — PLT 建归因图,两枢纽特征占 60% 输入 / PLT attribution graphs; two hub features hold 60% of inputs ↻07-17
- [[2607.14817]] Evaluating Epistemic Uncertainty — OOD/AL 代理与真实后悔排名翻转,统一拒判框架 / Proxy rankings invert vs true regret; unified reject framework ↻07-17
- [[2607.14943]] WA-LQR: Steering Robustness into WAMs — LQR 闭环转向 WAM 激活,LIBERO +41pp / Closed-loop LQR steers WAM activations; LIBERO +41pp ↻07-17
- [[2607.15001]] LQCDMaster: Agentic Lattice QCD — 确定性 Wick 工具 + 机器精度复现 90% / Deterministic Wick tool + 90% machine-precision reproduction ↻07-17
- [[2607.15079]] BrainPilot: Agentic Brain Discovery — PI+Auditor+Graph of Trace,低成本可审计 / PI + Auditor + Graph of Trace; low-cost, auditable ↻07-17
- [[2607.15084]] Face Embedding Geometry MIA — 180 模型因子实验,训练身份数为主导因子 / 180-model factorial study; training-id count dominates ↻07-17
- [[2607.15175]] Linear Representations of Grammaticality — 25 模型验证语法性是线性可解码维度 / Grammaticality is a linearly decodable dimension across 25 models ↻07-17
- [[2607.15190]] Can We Trust IRT for AI Evaluation? — ~18000 模拟条件揭示 IRT 估计器在 AI 体制下失效 / ~18k simulation conditions reveal IRT estimator breakdown in AI regime ↻07-17
- [[2607.15196]] Subjective Risk Decomposition — 主观风险反偏差-方差-熵分解还原多种 A/E 度量 / Reverse bias-variance-entropy of subjective risk recovers many A/E measures ↻07-17
- [[2607.15218]] PRISM: Physical Danger Beyond Text — 隐藏态两方向可分离,单层探针 86% 准确 / Two separable hidden-state directions; single-layer probe 86% acc ↻07-17
- [[2607.15247]] AutoSynthesis: Automated Meta-Analysis — 端到端 PRISMA 流水线,g=0.143 vs 专家 0.020 / End-to-end PRISMA pipeline; g=0.143 vs expert 0.020 ↻07-17
- [[2607.15277]] Statistical Self-Consistency in LLMs — 全概率公式检验,前沿模型普遍违反;宏观谬误 / Law-of-total-probability check; frontier models violate it; macro fallacy ↻07-17

### 2026-07-17 (26)

- [[2607.14460]] Precise sample covariance spectral norm error – an RDT view — 随机对偶理论给出中心化高斯样本协方差谱范数误差的精确极限闭式表达。 RDT gives the sharp closed-form limiting spectral-norm error for centered Gaussian sample covariance.
- [[2607.14466]] Interleaved Noise Injection Improves Clean, Corrupted, and OOD Performance — 干净/噪声 epoch 开关式切换，CIFAR-100-C/ImageNet-C/R 上同时提升精度与鲁棒性。 Square-wave clean/noise epoch switching improves clean acc, corruption robustness, and OOD on CIFAR-100-C/ImageNet-C/R.
- [[2607.14530]] xHC: Expanded Hyper-Connections — 残差流扩展率 N 推到 16，18B/28B MoE 下游均值 +4.5、FLOPs 更低。 Pushes residual-stream expansion N to 16; +4.5 downstream avg on 18B/28B MoE at lower FLOPs. ⭐
- [[2607.14545]] CASP: Learning-Augmented Offline Approximation with Verifiable Certificates — 倒转信息流：用负向证书 + 多项式验证器，使 NP-hard 近似比率脱离预测质量。 Reverses the signal: negative certificates + polynomial verifier decouple NP-hard approximation ratios from prediction quality.
- [[2607.14560]] Breaking the Model Forgetting Cycle in Long-Incremental 3D Object Detection — 长期增量 3D 检测 / Long-incremental 3D detection
- [[2607.14570]] Democratizing Agent Deployment Safety: A Structural Monitoring Approach — 用未训练的信息流图监视器在 iac_cdk 上 AUROC 0.86，无需攻击日志训练。 An untrained Information Flow Graph monitor reaches AUROC 0.86 on iac_cdk without attack-log training.
- [[2607.14582]] MathCoPilot: Interactive Human-AI Symbiotic Theorem Proving — "活态证明蓝图"为核心的工作台，在 FormalMATH 子集与真实 PDE 定理上系统对比多个前沿模型。 A "living proof blueprint" workbench; benchmarks Gemini 3.1 Pro/GPT-5.4/etc on FormalMATH and real PDE theorems.
- [[2607.14707]] Harnessing LLMs for Reliable Academic Supervision — 用 LangGraph 包装 GPT-4o-mini 的七模块系统在六维盲评上全面胜过无脚手架 GPT-5（4.08 vs 2.79）。 A LangGraph-wrapped GPT-4o-mini seven-module system beats bare GPT-5 on all six blind-eval dimensions (4.08 vs 2.79).
- [[2607.14720]] Causal-Adversarial Probing of Clinical Covariates for Prostate MRI Grading — 梯度反转对抗抑制 PSA/前列腺体积使 AUC 降 7.61%，证明模型依赖真实病理而非捷径。 Gradient-reversal suppression of PSA/prostate volume drops AUC by 7.61%, showing reliance on real pathology not shortcuts.
- [[2607.14731]] What's in a Smoothness Constant? Tighter Rates for Local SGD — 证明有界二阶异质性即可使 Local SGD 在远比一阶假设宽松的条件下优于 Mini-batch SGD。 Proves bounded second-order heterogeneity suffices for Local SGD to beat Mini-batch SGD under far weaker assumptions.
- [[2607.14737]] GeoDetect: Geometric Adversarial Detection for VLPs — 利用 VLP 嵌入各向异性，无微调跨 ALBEF/CLIP/TCL 检测对抗样本。 Exploits VLP embedding anisotropy; detects adversarial examples across ALBEF/CLIP/TCL without fine-tuning.
- [[2607.14760]] Clean-Reference Streaming Detection of Lens Occlusion — 轻量可审计状态机，320 序列上 F1=0.800，比直方图差异基线配对正胜。 Auditable state machine reaches F1=0.800 on 320 sequences, paired-beating histogram-diff baselines.
- [[2607.14826]] Interventional Causal Circuits for Safe Robot Action Testing — 将 JPT 升级为因果电路，使被拒动作能自动定位失败参数并一次性修正。 Upgrades a Joint Probability Tree into a causal circuit that pinpoints failing action params and suggests one-shot fixes.
- [[2607.14862]] Tamed Stochastic Gradient Hamiltonian Monte Carlo — 首个驯服版 SGHMC，对超线性增长梯度证明 Wasserstein-2 收敛率 1/2。 First tamed SGHMC variant; achieves Wasserstein-2 rate 1/2 under relaxed conditions for superlinearly growing gradients.
- [[2607.14877]] PAC Learning in Turn-Based Stochastic Games with Reachability Objectives — 首个回合制随机博弈可达性目标的去中心化 PAC 正面结果，LeTuReGa 给出多项式样本复杂度。 First positive decentralized PAC result for TBSG reachability; LeTuReGa gives polynomial sample complexity.
- [[2607.14889]] Analytical Study of the Optimal Combination of Binary Classifiers — 把 Bartlett 的 1D classification-calibrated risk 推广到 m 维并证明凸化全局最小唯一性。 Generalizes Bartlett's 1D calibrated risk to m dimensions and proves uniqueness of the convexified global minimum.
- [[2607.14890]] Proof-or-Stop: Don't Trust the Agent, Trust the Evidence — 把 agent claim 视作可裁决的 admissibility decision，预注册消融把假通过削减 76%。 Treats agent claims as admissibility decisions; pre-registered ablation cuts false passes by 76%. ⭐
- [[2607.14947]] Optimal Self-Distillation for Rectified Flow via Linear Probing — 在岭回归下证明真/教师速度最优混合（系数可负）严格优于教师，给闭式系数。 Under ridge regression, optimally mixing true/teacher velocities (coefficients can be negative) strictly beats the teacher; closed form given.
- [[2607.14952]] LongStraw: Long-Context RL Beyond 2M Tokens under a Fixed GPU Budget — 张量生命周期重写把 GRPO 活图从 P+R 压到 R，8×H20 上 Qwen3 训到 2M+ token。 Reframes GRPO as a tensor-lifetime problem, compressing live graph from P+R to R; trains Qwen3 to 2M+ tokens on 8×H20.
- [[2607.14967]] Latent Trajectory Discrimination for AI-Generated Text Detection — 把 AI 文本检测重建模为潜空间轨迹判别，在 RAID/NYT-AI/Reviews 上超越基线。 Reframes AI-text detection as latent-trajectory discrimination; beats baselines on RAID/NYT-AI/Reviews.
- [[2607.15003]] SMC-ES: Automated Synthesis of Formally Verified Control Policies — 进化策略 + 统计模型检验交替，为 MuJoCo/Safety Gymnasium 合成带形式化保证的 NN 策略。 ES + statistical model checking synthesize NN policies with formal guarantees on MuJoCo/Safety Gymnasium.
- [[2607.15067]] Kernel Weighted Importance Sampling for Off-Policy Evaluation — 用 Nadaraya-Watson 核回归统一 WIS 有界性与 VIS 独立性。 Replaces self-normalization with Nadaraya-Watson kernel regression, unifying WIS boundedness and VIS independence.
- [[2607.15080]] Evaluating Covariate Balance for Long-Horizon MDPs — 将协变量均衡诊断扩展到时间相关 OPE，证明脓毒症 RL 研究多无法通过该检验。 Extends covariate-balance diagnostics to time-dependent OPE; shows sepsis RL studies largely fail the test.
- [[2607.15105]] Long-Context Fine-Tuning with Limited VRAM — HGA + 分段反向传播 + 分层 KV 存储，16GB 上对 Qwen3-8B 做 4-bit QLoRA 微调。 HGA + segment-wise backprop + tiered KV storage enables 4-bit QLoRA of Qwen3-8B on 16 GB VRAM.
- [[2607.15164]] The Industrialization of Research: On AI-Driven Science — 立场文章，以 DOE Genesis Mission 为案例剖析 AI 驱动科研从 craft 到 pipeline 的伦理后果。 Position essay using DOE Genesis Mission to analyze the craft→pipeline shift and its ethical consequences.
- [[2607.15208]] Delocalization of Bias in Unadjusted Hamiltonian Monte Carlo — 将"偏差离域化"从过阻尼 Langevin 推广到未校正 HMC 与 BAOAB，控制任意可观测的总误差。 Extends "delocalization of bias" to unadjusted HMC and BAOAB; total error of any observable can be controlled.


---

*本周摘要是每日 arxiv 日报的汇总。逐日回链如下：This weekly digest rolls up the daily digests. Per-day links: [2026-07-13](../../2026-07-13/overview.md) · [2026-07-14](../../2026-07-14/overview.md) · [2026-07-15](../../2026-07-15/overview.md) · [2026-07-16](../../2026-07-16/overview.md) · [2026-07-17](../../2026-07-17/overview.md).*
