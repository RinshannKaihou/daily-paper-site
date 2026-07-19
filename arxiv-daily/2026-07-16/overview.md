---
title: "Daily Paper Overview — 2026-07-16"
date: 2026-07-16
tags:
  - daily-paper
  - llm-training-stability
  - interpretability
  - self-evolving-agents
  - computation-reliability
  - ml-reliability
  - llm-evaluation
papers: 50
---

# Daily Paper Overview — 2026-07-16

共 50 篇 / 50 papers total.

---

## 今日必读 / Must Read Today

### 1. [[2607.13631]] — How the Hessian-Spectrum of Neural Networks Depends on Data

**为什么必读 / Why read this**

中:本文在广义 Gauss-Newton (GGN) 近似下给出任意宽度/深度线性网络 Hessian 特征值的闭式表达,并证明 MSE 分类解的锐度 (sharpness) 正比于最大类别占比 α_max——与 Cohen 等人 Edge-of-Stability 的两条经验论断直接矛盾。它把"训练为什么在某个学习率失稳"这一稳定性问题归因到**数据几何**而非模型规模,对关注训练稳定性与损失景观理论的研究者是直接的、可证伪的起点。

EN:Derives closed-form Hessian eigenvalues (via the GGN approximation) for linear networks of arbitrary width/depth and proves that solution sharpness for MSE classification is proportional to the maximum class proportion α_max, directly contradicting two empirical claims of the Edge-of-Stability literature. This re-roots training stability in **data geometry** rather than model size — a falsifiable, theory-first anchor for anyone studying loss-landscape dynamics.

### 2. [[2607.13683]] — Self-Evolving Agent Harnesses via Gated Semantic Quality-Diversity (GSME)

**为什么必读 / Why read this**

中:GSME 提出可审计的自演化闭环——把"提出修改"与"归因增益"分离,由更强的模型诊断失败写补丁,由确定性代码负责采样与三道门控(有效性/激活/配对 2σ 显著性)。跨 7 个领域在冻结模型上拿到 +9~+15.5pp 的封存测试增益(保留训练增益的 86–147%)。对关注自演化 agent 的研究者,它给出了"可信归因"与"held-out 泛化"两个一直欠缺的正面证据。

EN:GSME separates proposal from credit in a git-tracked self-evolving loop — a stronger model diagnoses failures and writes patches while deterministic code owns sampling and three gates (validity, activation, paired-2σ significance). It earns +9 to +15.5pp sealed-test gains across seven domains on a frozen model (retaining 86–147% of the training lift), supplying the two pieces self-evolving-agent work has most lacked: trustworthy credit assignment and held-out generalization.

### 3. [[2607.13918]] — Partially Correlated Verifier Cascades in LLM Harnesses

**为什么必读 / Why read this**

中:针对"全接受"级联验证,本文用 de Finetti 把每个错误实例的假接受率建模为潜在变量,证明级联后验对门数 k 严格凹、Beta 潜变量下失败概率按幂律(而非指数)衰减、盲点质量给出可靠性上限。合成实验里,独立性外推把失败率低估 20×(k=5)到约 3000×(k=10)。核心结论:把钱花在"去相关"(换模型族/模态/外部证据)而非"加门"——对依赖多验证器级联的可靠性系统是即时可用的指导。

EN:Treats each erroneous instance's false-accept rate as a latent variable and proves the cascade posterior is strictly concave in k, that failure decays polynomially (not exponentially) under Beta latents, and that blind-spot mass caps the reliability ceiling. Independence-based extrapolation underestimates the failure rate by 20× at k=5 and ~3000× at k=10. The actionable lever is **decorrelation** (different model family / modality / external oracle), not more gates — immediately useful guidance for any multi-verifier reliability stack.

---

## 按主题分类 / Papers by Topic

### A. 训练动力学与优化稳定性 / Training Dynamics & Optimization Stability

| 论文 / Paper | 主题 / Topic | 要点 / Key Point |
|---|---|---|
| [[2607.13631]] Hessian-Spectrum Depends on Data | 锐度与数据几何 / Sharpness vs data geometry | GGN 下证明锐度 ∝ α_max,反驳 Edge-of-Stability / Proves sharpness ∝ α_max under GGN, contradicting Edge-of-Stability |
| [[2607.14536]] Muse: Muon Representation Geometry | Muon 优化器几何 / Muon optimizer geometry | 把矩阵化当作设计轴,Vector 端点退化为 nSGDM / Reframes matrixization as a design axis; Vector endpoint collapses to nSGDM |
| [[2607.14516]] RK3(2)-Adam Compute-Matched Study | 高阶优化器失效诊断 / Higher-order optimizer inertness | 严格按梯度计算量对齐后 RK3(2)-Adam 输给 Adam,控制器失效 / Under per-gradient compute matching, RK3(2)-Adam loses to Adam; step controller is inert |
| [[2607.14576]] Sharp Stability Threshold for Residual Architectures | 残差网络稳定性阈值 / Residual stability threshold | 次线性增长原理 q≤1 为尖锐阈值,免归一化 / Sublinear-growth q≤1 is a sharp threshold; normalization-free |
| [[2607.14018]] Transforming Rank: Spectral Pathologies of Depth | 深度谱病态 / Spectral pathologies of depth | 架构如何规避深度带来的谱病态 / How architecture navigates spectral pathologies of depth |
| [[2607.14427]] Per-Token Fixed-Point Convergence in Depth-Recurrent Transformers | 深度循环 Transformer 收敛 / Depth-recurrent convergence | 逐 token 不动点收敛分析 / Per-token fixed-point convergence analysis |
| [[2607.14185]] Closed-Loop Knowledge Dynamics | 知识饱和与逃逸 / Knowledge saturation and escape | 饱和与逃逸的操作框架 / Operational framework for saturation and escape |

### B. 自演化 Agent 与自动化科研 / Self-Evolving Agents & Automated Research

| 论文 / Paper | 主题 / Topic | 要点 / Key Point |
|---|---|---|
| [[2607.13683]] GSME Self-Evolving Agent Harnesses | 自演化 harness + 统计归因 / Self-evolving harness + crediting | 提出与归因分离,配对 2σ 门控,+9~15.5pp held-out / Separates proposal from credit, paired-2σ gate, +9~15.5pp held-out |
| [[2607.13940]] Self-Evolving Agent for Longitudinal Health | 纵向健康管理 agent / Longitudinal health agent | 自演化个性化健康管理 / Self-evolving personalized health management |
| [[2607.14004]] Do Agent Optimizers Compound? | 持续学习评估 / Continual-learning evaluation | Terminal-Bench 2.0 上优化器是否复利 / Whether optimizers compound on Terminal-Bench 2.0 |
| [[2607.14408]] Reward-Free Evolving Agents via Pairwise Validator | 免奖励演化 / Reward-free evolution | 成对验证器驱动的免奖励演化 / Reward-free evolution driven by a pairwise validator |
| [[2607.14431]] Byte-Exact KV-State Grafting Flywheel | 知识飞轮 / Knowledge flywheel | 字节精确 KV 嫁接,冻结小模型变可信知识飞轮 / Byte-exact KV grafting turns a frozen small model into a verified flywheel |
| [[2607.14777]] SEED: Self-Evolving On-Policy Distillation | 自蒸馏 agentic RL / Self-distillation for agentic RL | 同一策略既当 actor 又当事后 analyzer,ALFWorld 75→91.8 / Same policy as actor + hindsight analyzer; ALFWorld 75→91.8 |
| [[2607.14658]] TopoAgent: Self-Evolving Topological Agent | DAG 拓扑 + 任务裂变 / DAG + atomic fission | DAG 替代线性轨迹,上下文隔离 + 自适应裂变 / DAG replaces linear trajectories; context isolation + adaptive fission |
| [[2607.13608]] Automatic ODE Discovery (Agentic) | 生物系统 ODE 发现 / Biological ODE discovery | LLM agent 自动发现生物 ODE / LLM agent discovers biological ODEs |
| [[2607.14178]] ReasFlow: Multi-Agent for Math Discovery | 数学发现多智能体 / Math-discovery multi-agent | 知识驱动的应用数学发现 / Knowledge-based multi-agent for applied-math discovery |
| [[2607.15001]] LQCDMaster: Agentic Lattice QCD | 格点 QCD 智能体 / Lattice-QCD agent | 确定性 Wick 工具 + 机器精度复现 90% / Deterministic Wick tool + 90% machine-precision reproduction |
| [[2607.15079]] BrainPilot: Agentic Brain Discovery | 脑科学多智能体 / Brain-science multi-agent | PI+Auditor+Graph of Trace,低成本可审计 / PI + Auditor + Graph of Trace; low-cost, auditable |
| [[2607.15247]] AutoSynthesis: Automated Meta-Analysis | 自动化元分析 / Automated meta-analysis | 端到端 PRISMA 流水线,g=0.143 vs 专家 0.020 / End-to-end PRISMA pipeline; g=0.143 vs expert 0.020 |

### C. 可解释性、隐藏态与探测 / Interpretability, Hidden States & Probing

| 论文 / Paper | 主题 / Topic | 要点 / Key Point |
|---|---|---|
| [[2607.14306]] ENTD: Tracing LLM Behavior to Training Data | 训练数据归因 / Training-data attribution | 经验下一 token 分布追溯到训练数据 / Trace behavior to training data via empirical next-token distributions |
| [[2607.13899]] AIMO Interpretability Challenge | 数学推理可解释挑战 / Math-reasoning interpretability | 鲁棒 vs 伪相关特征 / Robust vs spurious features in math reasoning |
| [[2607.14791]] Transcoders for Investigating Deception | 欺骗电路分析 / Deception circuit analysis | PLT 建归因图,两枢纽特征占 60% 输入 / PLT attribution graphs; two hub features hold 60% of inputs |
| [[2607.15175]] Linear Representations of Grammaticality | 语法性线性方向 / Grammaticality linear direction | 25 模型验证语法性是线性可解码维度 / Grammaticality is a linearly decodable dimension across 25 models |
| [[2607.15218]] PRISM: Physical Danger Beyond Text Safety | 物理危险 vs 内容危险 / Physical vs content danger | 隐藏态两方向可分离,单层探针 86% 准确 / Two separable hidden-state directions; single-layer probe 86% acc |
| [[2607.14463]] Depth-Dependent Hidden-State Collapse | 自编码器隐藏态塌缩 / Hidden-state collapse in autoencoders | LiDAR 点云动力系统 AE 的深度塌缩 / Depth-dependent collapse in LiDAR point-cloud autoencoders |
| [[2607.14943]] WA-LQR: Steering Robustness into WAMs | 激活转向 + 最优控制 / Activation steering + optimal control | LQR 闭环转向 WAM 激活,LIBERO +41pp / Closed-loop LQR steers WAM activations; LIBERO +41pp |
| [[2607.14399]] Instrument Effects in Honesty Evaluation | 诚实评测的工具效应 / Instrument effects in honesty eval | 单系统可审计地展示评测工具效应 / Auditable single-system demo of evaluation instrument effects |

### D. 计算可靠性、量化与高效推理 / Computation Reliability, Quantization & Efficient Inference

| 论文 / Paper | 主题 / Topic | 要点 / Key Point |
|---|---|---|
| [[2607.13918]] Partially Correlated Verifier Cascades | 级联验证可靠性理论 / Cascade reliability theory | 相关门下凹性+幂律衰减,独立性低估 3000× / Concave + polynomial decay under correlation; independence underestimates 3000× |
| [[2607.14541]] Atrex-Bench: GPU Kernels Production-Ready? | 生产 trace kernel 基准 / Production-trace kernel benchmark | 最强 agent 仅达 roofline 10.7%,揭示正确性幻觉 / Best agent reaches 10.7% of roofline; exposes correctness illusion |
| [[2607.14181]] Quantize with Confidence? | 代码生成量化研究 / Quantization for code gen | 量化对代码生成可靠性的实证 / Empirical study of quantization effects on code generation |
| [[2607.14618]] PolyQ: Edge CPU LLM Quantization | 分数比特 CPU 量化 / Fractional-bit CPU quantization | {2,3,4,8,16} 调色板 + 编译期布局正则化 / {2,3,4,8,16} palette + compile-time layout regularization |
| [[2607.14622]] ExaGEMM: In-Register Low-Bit GEMM | CPU 低比特 GEMM 探索 / CPU low-bit GEMM exploration | 支持点选择框架,剪枝 99.2% 候选 / Support-selection framework; prunes 99.2% of candidates |
| [[2607.13649]] CIMERA: Compute-in-Interconnect and Memory | 存算一体 LLM 推理 / Compute-in-interconnect inference | 可重构精度的存算互连 / Reconfigurable-precision compute-in-interconnect |
| [[2607.13898]] Jack of All Scales: FPGA MXFP Tensor Block | FPGA MXFP 张量块 / FPGA MXFP tensor block | 多精度 MXFP 的 FPGA 张量块 / Versatile FPGA tensor block for MXFP precisions |
| [[2607.14568]] Multimodal Assistant on 2011 Fermi GPU | 老旧硬件多模态推理 / Legacy-hardware multimodal | 2011 年 6GB Fermi 跑通 MiniCPM-V,测量驱动 / Runs MiniCPM-V on 2011 6GB Fermi; measurement-driven |
| [[2607.14375]] Random Parameter Noise vs ReLU Verification | 精确 ReLU 验证 / Exact ReLU verification | 随机参数噪声不能使 ReLU 验证变易 / Random parameter noise does not make exact ReLU verification easy |

### E. LLM 评测、校准与推理可靠性 / LLM Evaluation, Calibration & Inference Reliability

| 论文 / Paper | 主题 / Topic | 要点 / Key Point |
|---|---|---|
| [[2607.13707]] Test Oracle Problem in LLM-as-Judge Corpora | 评测完整性 / Evaluation integrity | max_tokens 共用制造假跨语言偏差,四重检验未发现 / Shared max_tokens fabricates cross-lingual bias surviving 4 robustness checks |
| [[2607.13753]] Post-Training Shifts Confidence | SFT/RL/OPD 校准 / SFT/RL/OPD calibration | 三阶段分析后训练如何改变置信度校准 / Three-stage analysis of how post-training shifts calibration |
| [[2607.14480]] LLM Evaluators Biased across Languages | 多语言评测偏差 / Multilingual evaluator bias | 点值分数随语言偏移,pairwise accuracy 掩盖 / Pointwise scores shift by language; pairwise accuracy hides it |
| [[2607.14552]] Answer-Conditioned CoT Degrades Distillation | 答案泄露蒸馏伤害 / Answer-leakage distillation harm | 一位比特实验:看答案 CoT 伤 MATH-500 16.2 分 / One-bit experiment: answer-conditioned CoT costs 16.2 MATH-500 pts |
| [[2607.14528]] CRTBench: Logical Consistency | 逻辑一致性评测 / Logical consistency benchmark | 等价改写下准确率高≠一致,推理增强反崩量化 / High accuracy ≠ consistency; reasoning effort collapses quantifier reasoning |
| [[2607.14275]] AI Agents Do Not Fail Alone: Context Fails First | 上下文失败归因 / Context-failure attribution | agent 失败的根因常在上下文而非模型 / Root cause of agent failure is often the context, not the model |
| [[2607.15190]] Can We Trust IRT for AI Evaluation? | IRT 评测可靠性 / IRT reliability for AI eval | ~18000 模拟条件揭示 IRT 估计器在 AI 体制下失效 / ~18k simulation conditions reveal IRT estimator breakdown in AI regime |
| [[2607.15277]] Statistical Self-Consistency in LLMs | 统计自洽性 / Statistical self-consistency | 全概率公式检验,前沿模型普遍违反;宏观谬误 / Law-of-total-probability check; frontier models violate it; macro fallacy |

### F. 数学基础、理论与可靠性 / Mathematical Foundations, Theory & Reliability

| 论文 / Paper | 主题 / Topic | 要点 / Key Point |
|---|---|---|
| [[2607.14817]] Evaluating Epistemic Uncertainty | 认知不确定性评测 / Epistemic uncertainty evaluation | OOD/AL 代理与真实后悔排名翻转,统一拒判框架 / Proxy rankings invert vs true regret; unified reject framework |
| [[2607.15196]] Subjective Risk Decomposition | 不确定性统一分解 / Unified UQ decomposition | 主观风险反偏差-方差-熵分解还原多种 A/E 度量 / Reverse bias-variance-entropy of subjective risk recovers many A/E measures |
| [[2607.14506]] Non-vacuous Generalization Bounds for RLVR | RLVR 泛化界 / RLVR generalization bounds | 首个 RLVR 非空 PAC-Bayes 界,Gumbel-max 外置随机性 / First non-vacuous PAC-Bayes bound for RLVR; Gumbel-max externalizes randomness |
| [[2607.15084]] Membership Info in Face Embedding Geometry | 嵌入几何成员推断 / Embedding-geometry MIA | 180 模型因子实验,训练身份数为主导因子 / 180-model factorial study; training-id count dominates |
| [[2607.13660]] Hyperspherical Geometry of CLIP Latent Space | CLIP 潜空间几何 / CLIP latent geometry | 语义混合模型刻画 CLIP 超球几何 / Semantic mixture model for CLIP hyperspherical geometry |
| [[2607.14228]] SeeSE3: 3D Space in Vision Features | 视觉特征中 3D 空间涌现 / 3D space emergence in vision | 视觉特征里 SE3 三维结构的涌现 / Emergence of SE3 3D structure in vision features |

---

## All Papers

| # | Paper | Short Title | Topic |
|---|---|---|---|
| 1 | [[2607.13608]] | Auto ODE Discovery (Bio) | Self-Evolving Agents / 自演化智能体 |
| 2 | [[2607.13631]] | Hessian-Spectrum Depends on Data | Training Dynamics / 训练动力学 |
| 3 | [[2607.13649]] | CIMERA Compute-in-Interconnect | Quantization & Inference / 量化与推理 |
| 4 | [[2607.13660]] | CLIP Hyperspherical Geometry | Math Foundations / 数学基础 |
| 5 | [[2607.13683]] | GSME Self-Evolving Harness | Self-Evolving Agents / 自演化智能体 |
| 6 | [[2607.13707]] | Test Oracle Problem LLM-as-Judge | LLM Evaluation / LLM 评测 |
| 7 | [[2607.13753]] | Post-Training Shifts Confidence | LLM Evaluation / LLM 评测 |
| 8 | [[2607.13898]] | FPGA MXFP Tensor Block | Quantization & Inference / 量化与推理 |
| 9 | [[2607.13899]] | AIMO Interpretability Challenge | Interpretability / 可解释性 |
| 10 | [[2607.13918]] | Partially Correlated Verifier Cascades | Computation Reliability / 计算可靠性 |
| 11 | [[2607.13940]] | Self-Evolving Health Agent | Self-Evolving Agents / 自演化智能体 |
| 12 | [[2607.14004]] | Do Agent Optimizers Compound? | Self-Evolving Agents / 自演化智能体 |
| 13 | [[2607.14018]] | Transforming Rank: Spectral Pathologies | Training Dynamics / 训练动力学 |
| 14 | [[2607.14178]] | ReasFlow Math Discovery | Self-Evolving Agents / 自演化智能体 |
| 15 | [[2607.14181]] | Quantize with Confidence? (Code Gen) | Quantization & Inference / 量化与推理 |
| 16 | [[2607.14185]] | Closed-Loop Knowledge Dynamics | Training Dynamics / 训练动力学 |
| 17 | [[2607.14228]] | SeeSE3: 3D Space in Vision | Math Foundations / 数学基础 |
| 18 | [[2607.14275]] | Context Fails First | LLM Evaluation / LLM 评测 |
| 19 | [[2607.14306]] | ENTD: Trace to Training Data | Interpretability / 可解释性 |
| 20 | [[2607.14375]] | Random Noise vs ReLU Verification | Computation Reliability / 计算可靠性 |
| 21 | [[2607.14399]] | Instrument Effects in Honesty Eval | Interpretability / 可解释性 |
| 22 | [[2607.14408]] | Reward-Free Evolving Agents | Self-Evolving Agents / 自演化智能体 |
| 23 | [[2607.14427]] | Per-Token Fixed-Point Convergence | Training Dynamics / 训练动力学 |
| 24 | [[2607.14431]] | Byte-Exact KV-State Grafting Flywheel | Self-Evolving Agents / 自演化智能体 |
| 25 | [[2607.14463]] | Hidden-State Collapse (LiDAR AE) | Interpretability / 可解释性 |
| 26 | [[2607.14480]] | LLM Evaluators Biased across Languages | LLM Evaluation / LLM 评测 |
| 27 | [[2607.14506]] | Non-vacuous Bounds for RLVR | Math Foundations / 数学基础 |
| 28 | [[2607.14516]] | RK3(2)-Adam Compute-Matched Study | Training Dynamics / 训练动力学 |
| 29 | [[2607.14528]] | CRTBench: Logical Consistency | LLM Evaluation / LLM 评测 |
| 30 | [[2607.14536]] | Muse: Muon Representation Geometry | Training Dynamics / 训练动力学 |
| 31 | [[2607.14541]] | Atrex-Bench: GPU Kernels | Quantization & Inference / 量化与推理 |
| 32 | [[2607.14552]] | Answer-Conditioned CoT Degrades | LLM Evaluation / LLM 评测 |
| 33 | [[2607.14568]] | Multimodal on 2011 Fermi GPU | Quantization & Inference / 量化与推理 |
| 34 | [[2607.14576]] | Sharp Stability Threshold (Residual) | Training Dynamics / 训练动力学 |
| 35 | [[2607.14618]] | PolyQ: Edge CPU Quantization | Quantization & Inference / 量化与推理 |
| 36 | [[2607.14622]] | ExaGEMM In-Register Computing | Quantization & Inference / 量化与推理 |
| 37 | [[2607.14658]] | TopoAgent: Self-Evolving Topological | Self-Evolving Agents / 自演化智能体 |
| 38 | [[2607.14777]] | SEED: Self-Evolving OPD | Self-Evolving Agents / 自演化智能体 |
| 39 | [[2607.14791]] | Transcoders for Deception | Interpretability / 可解释性 |
| 40 | [[2607.14817]] | Evaluating Epistemic Uncertainty | Math Foundations / 数学基础 |
| 41 | [[2607.14943]] | WA-LQR: Steering Robustness into WAMs | Interpretability / 可解释性 |
| 42 | [[2607.15001]] | LQCDMaster: Agentic Lattice QCD | Self-Evolving Agents / 自演化智能体 |
| 43 | [[2607.15079]] | BrainPilot: Agentic Brain Discovery | Self-Evolving Agents / 自演化智能体 |
| 44 | [[2607.15084]] | Face Embedding Geometry MIA | Math Foundations / 数学基础 |
| 45 | [[2607.15175]] | Linear Representations of Grammaticality | Interpretability / 可解释性 |
| 46 | [[2607.15190]] | Can We Trust IRT for AI Evaluation? | LLM Evaluation / LLM 评测 |
| 47 | [[2607.15196]] | Subjective Risk Decomposition | Math Foundations / 数学基础 |
| 48 | [[2607.15218]] | PRISM: Physical Danger Beyond Text | Interpretability / 可解释性 |
| 49 | [[2607.15247]] | AutoSynthesis: Automated Meta-Analysis | Self-Evolving Agents / 自演化智能体 |
| 50 | [[2607.15277]] | Statistical Self-Consistency in LLMs | LLM Evaluation / LLM 评测 |

---

## 验证 / Verification

- 目录中 `.md` 文件总数(excluding overview.md)/ `.md` files in directory (excluding overview.md): **50**
- 本 overview 收录论文数 / Papers listed in this overview: **50**
- 计数一致 / Counts match: ✅
