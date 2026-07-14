---
title: "Daily Paper Overview — 2026-05-06"
date: 2026-05-06
tags:
  - llm-training-stability
  - llm-interpretability
  - llm-reliability
  - hidden-states
  - inference-evaluation
  - computation-precision
  - silent-data-corruption
  - ml-foundations
papers_count: 51
---

# Daily Paper Overview — 2026-05-06

## 今日必读 / Must Read Today

### 1. [[2605.04431v1]] — Towards Robust LLM Post-Training: Automatic Failure Management for Reinforcement Fine-Tuning

**为什么必读 / Why Must-Read:**

这篇论文构建了首个专门面向强化微调（RFT）训练异常的细粒度基准 RFT-FaultBench（5 大故障族 / 16 故障类型 / 779 次训练运行 / 22,549 train-step），并提出 RFT-FM 框架将训练异常检测、故障归因与 agentic 闭环干预统一起来。这直接覆盖了用户最核心的关注点：LLM 训练稳定性与可观测性——它把 reward hacking、KL explosion、entropy collapse 等典型 RFT 病态作为可结构化、可量化、可自动修复的对象，是目前该方向最系统的工程实践论文。

This paper builds the first fine-grained benchmark for reinforcement fine-tuning (RFT) failure modes (RFT-FaultBench: 5 fault families, 16 fault types, 779 training runs), and proposes RFT-FM — an agentic closed-loop framework that unifies anomaly detection, fault attribution, and automated intervention. This directly addresses LLM Training Stability & Observability at its most operational level: reward hacking, KL explosion, and entropy collapse are treated as structured, observable, and automatically recoverable events. Hard-setting results (73.88% detection F1, 46.25% repair success rate) make this a must-read for anyone building reliable post-training pipelines.

---

### 2. [[2605.04418v1]] — Demystifying Manifold Constraints in LLM Pre-training

**为什么必读 / Why Must-Read:**

本文提出 MACRO 优化器，通过可证明收敛的单循环黎曼约束优化，从理论上"祛魅"了 RMSNorm 与解耦权重衰减在 LLM 预训练中的作用——证明流形约束可以同时约束激活尺度并强制稳定旋转平衡，从而完全替代这两种最常用的启发式。这是一篇同时具备理论深度和实践意义的训练稳定性论文，为理解预训练归一化机制的本质提供了迄今最清晰的框架。

MACRO demystifies two of LLM pre-training's most relied-upon heuristics — RMSNorm and decoupled weight decay — by showing that Frobenius/Spectral ball manifold constraints provably subsume both: they bound forward activation scale AND enforce stable rotational equilibrium simultaneously. A single-loop, provably convergent Riemannian optimizer replaces these ad-hoc components. For researchers who care about why LLM pre-training is (or isn't) stable, this paper offers the clearest theoretical framework to date on what normalization and regularization are actually doing geometrically.

---

### 3. [[2605.04563v1]] — RangeGuard: Efficient, Bounded Approximate Error Correction for Reliable DNNs

**为什么必读 / Why Must-Read:**

RangeGuard 系统量化了 BF16 指数位翻转如何在 transformer 层中被注意力/残差/归一化路径放大为 LLM 推理的灾难性失败（HBM 比特错误率 1e-5），并提出以"值域标识符"（RID）替代逐比特 ECC 保护，每块可容忍 64+ 比特错误，同时保持 Llama-3.2-1B 接近无错基线精度。这直接覆盖了 Silent Data Corruption (SDC)、Computation Reliability & Precision Errors 以及 ML Reliability 三个核心兴趣点，是连接硬件故障与 LLM 推理可靠性的关键工程论文。

RangeGuard directly connects hardware-level HBM bit errors to LLM inference failure: the paper systematically characterizes how BF16 exponent bit flips are amplified through attention/residual/normalization paths to cause catastrophic output degradation, then proposes a Range Identifier (RID) scheme that protects semantic ranges rather than raw bits — tolerating 64+ bit errors per block within existing 16-bit ECC budgets. This is a landmark paper for SDC, precision error, and ML reliability interests, offering both a failure characterization study and a practical mitigation deployed on real GPU/HBM systems.

---

## 按主题分类 / Papers by Topic

### 主题 1：LLM 训练稳定性与可观测性 / LLM Training Stability & Observability

| 论文 Paper | 核心贡献 Key Contribution | 相关性 Relevance |
|---|---|---|
| [[2605.04431v1]] Robust RFT Failure Mgmt | 首个 RFT 训练异常基准+自动修复框架 / First RFT fault benchmark + agentic auto-repair framework | 直接覆盖训练稳定性 / Directly covers training stability |
| [[2605.04418v1]] MACRO Manifold Constraints | 黎曼优化替代 RMSNorm+权重衰减 / Riemannian optimization replaces RMSNorm+WD | 预训练稳定性理论基础 / Pre-training stability foundations |
| [[2605.04468v1]] Anchored Learning SFT | 显式 KL 上界防止灾难性遗忘 / Explicit KL bound prevents catastrophic forgetting | SFT 分布漂移控制 / SFT distributional drift control |
| [[2605.04478v1]] CCL-D Slow/Hang Diagnosis | 在 4000 GPU 集群上将慢/挂定位缩短到 6 分钟 / Reduces slow/hang root-cause to <6 min on 4k GPUs | 大规模训练可观测性 / Large-scale training observability |
| [[2605.04396v1]] Critical Windows Transformer | 发现权重衰减施加时机决定记忆vs推理命运 / Weight decay timing determines memorize-vs-reason fate | 训练动力学关键窗口 / Critical training dynamics window |
| [[2605.05113v1]] Signal Propagation Recurrences | Glorot 初始化在 √n 深度即失稳 / Glorot init fails at √n depth for linear recurrences | 递归模型初始化稳定性 / Recurrent model init stability |
| [[2605.04711v1]] BAOC Budget-Aware Optimizer | MILP 驱动的按块优化器配置 / MILP-driven block-wise optimizer configuration | 优化器状态显存与训练效率 / Optimizer memory & efficiency |
| [[2605.05436v1]] Implicit Regularization DL | 梯度匹配量化隐式正则化 / Gradient matching quantifies implicit regularization | 训练动力学可解释性 / Training dynamics interpretability |
| [[2605.05438v1]] Semantic Loss Model Collapse | 语义损失消除因果推理微调崩溃 / Semantic loss eliminates collapse in causal reasoning FT | 微调崩溃预防 / Fine-tuning collapse prevention |

---

### 主题 2：LLM 可解释性与隐藏状态 / LLM Interpretability & Hidden States

| 论文 Paper | 核心贡献 Key Contribution | 相关性 Relevance |
|---|---|---|
| [[2605.05197v1]] Grammaticality in Hidden States | 线性探针揭示语法表征仅需~10个神经元 / Linear probes show grammar encoded in ~10 neurons | LLM 隐藏状态结构分析 / LLM hidden state structure |
| [[2605.04980v1]] Conceptors Semantic Steering | Conceptor 子空间替代单向量激活引导 / Conceptor subspace replaces single-vector activation steering | 可组合语义控制 / Composable semantic control |
| [[2605.05115v1]] Manifold Steering | 用测地线插值替代线性激活引导 / Geodesic interpolation replaces linear activation steering | 表征几何与引导方法 / Representation geometry & steering |
| [[2605.04893v1]] Self-Attention as Transport | 双轴谱诊断替代对称谱（幻觉检测 AUROC 0.84） / Dual-axis spectral diagnostics vs symmetric spectra (hallucination AUROC 0.84) | 注意力可解释性诊断 / Attention interpretability diagnostics |
| [[2605.05341v1]] Feature Starvation SAE | 将死特征率从 95% 降至 39% 的稳定 SAE 训练 / Reduce dead feature rate from 95% to 39% with stable SAE | SAE 字典学习可靠性 / SAE dictionary learning reliability |
| [[2605.05443v1]] SLAM Structural Watermarking | SAE 定位句法方向+因果激活操控实现 100% 水印检测 / SAE locates syntactic directions + causal steering for 100% watermark detection | SAE 句法结构与激活引导 / SAE syntax & activation steering |
| [[2605.04971v1]] Geometric Continuity DNN | 残差连接+对称破缺非线性解释跨层权重连续性 / Residual+symmetry-breaking nonlinearity explains cross-layer weight continuity | LLM 权重几何可解释性 / LLM weight geometry interpretability |
| [[2605.04572v1]] Parameter Dynamics Safety | 样本级危险方向投影分数量化微调安全退化 / Sample-level dangerous-direction projection scores quantify safety degradation | 参数动力学与对齐退化 / Parameter dynamics & alignment |
| [[2605.04899v1]] Geometric Error LM Hidden State | 曲率（holonomy）作为取向化不确定性联结内部状态与世界模型 / Holonomy as oriented uncertainty links internal state to world models | 几何不确定性与隐藏状态 / Geometric uncertainty & hidden states |
| [[2605.05176v1]] ICL Nonlinear Regression Theory | 注意力作为特征化器给出非线性 ICL 泛化误差界 / Attention as featurizer gives nonlinear ICL generalization bounds | ICL 机制理论 / ICL mechanism theory |

---

### 主题 3：LLM 推理评估与幻觉检测 / LLM Inference Evaluation & Hallucination Detection

| 论文 Paper | 核心贡献 Key Contribution | 相关性 Relevance |
|---|---|---|
| [[2605.05166v1]] First Token Hallucination | 首 token 归一化熵以 1/11 代价匹配语义自洽性 AUROC / First-token normalized entropy matches semantic consistency at 1/11 cost | 低成本幻觉检测 / Low-cost hallucination detection |
| [[2605.05025v1]] Attention Divergence Hallucination | 注意力分布 KL 散度探针 AUROC 0.78-0.91 / Attention distribution KL divergence probe AUROC 0.78-0.91 | 白盒幻觉检测 / White-box hallucination detection |
| [[2605.04638v1]] SemGrad Uncertainty | 语义保留嵌入梯度范数量化 LLM 不确定性 / Semantic-preserving embedding gradient norm quantifies LLM uncertainty | 梯度不确定性量化 / Gradient-based uncertainty quantification |
| [[2605.05134v1]] Koopman Hallucination | Koopman 算子动力系统拟合幻觉轨迹 / Koopman operator dynamical system fits hallucination trajectories | 黑盒幻觉检测 / Black-box hallucination detection |
| [[2605.04665v1]] Paraphrase Output Collapse | 语义等价改写下 78% 封闭式响应丢失正确标签 / 78% closed-form responses lose correct labels under paraphrase | 推理评估鲁棒性 / Inference evaluation robustness |
| [[2605.04454v1]] Deployment Alignment Evaluation | 16个基准审计揭示缺失验证支持与过程可控性维度 / Audit of 16 benchmarks reveals missing verification & process-control dimensions | 对齐评估方法论 / Alignment evaluation methodology |
| [[2605.04624v1]] AuditRepairBench | 96,000 条配对执行轨迹揭示评估器-选择器耦合导致排行榜不稳 / 96k paired traces reveal evaluator-selector coupling causing leaderboard instability | 基准可靠性 / Benchmark reliability |
| [[2605.04727v1]] Knowledge Tracing Reliability | 修正注意力 Softmax 轴向错误消除评估数据泄漏 / Fix attention Softmax axis error to eliminate evaluation data leakage | 评估实现可靠性 / Evaluation implementation reliability |

---

### 主题 4：计算可靠性与精度错误 / Computation Reliability & Precision Errors

| 论文 Paper | 核心贡献 Key Contribution | 相关性 Relevance |
|---|---|---|
| [[2605.04563v1]] RangeGuard Approximate ECC | 值域 ECC 保护使 LLM 在 BER 1e-5 下保持精度 / Range-based ECC keeps LLM accurate at BER 1e-5 | SDC 与 LLM 推理容错 / SDC & LLM inference fault tolerance |
| [[2605.04803v1]] RISC-V Vector Fault Injection | 10万次 RTL 故障注入揭示 FP32/BF16 指数位 SDC 最严重 / 100k RTL injections show FP32/BF16 exponent bits cause worst SDC | 硬件瞬态故障与 SDC / Hardware transient faults & SDC |
| [[2605.04738v1]] OSAQ LLM Quantization | Hessian 零空间闭式解将 2-bit 困惑度降低 40%+ / Hessian null-space closed-form solution reduces 2-bit perplexity 40%+ | LLM 量化精度可靠性 / LLM quantization precision |
| [[2605.04754v1]] AxMoE Approximate Multipliers | 近似乘法器×MoE 拓扑交互：ViT Hard MoE r=0.25 最抗噪 / Approx multiplier×MoE topology: ViT Hard MoE r=0.25 most noise-robust | 近似计算与 MoE 可靠性 / Approximate computing & MoE |

---

### 主题 5：ML 可靠性与数学基础 / ML Reliability & Mathematical Foundations

| 论文 Paper | 核心贡献 Key Contribution | 相关性 Relevance |
|---|---|---|
| [[2605.05066v1]] Impossibility Triangle Long-Context | 信息论证明效率/紧凑性/召回不可兼得 / Information-theoretic proof: efficiency, compactness, recall cannot coexist | 长上下文架构基本限制 / Long-context architecture limits |
| [[2605.04683v1]] Average Attention Arithmetic Circuits | Transformer 编码器与 FSAC⁰_R[sign] 精确等价 / Transformer encoder exactly equivalent to FSAC⁰_R[sign] | Transformer 表达力理论 / Transformer expressivity theory |
| [[2605.05189v1]] Linear Associative Memory Capacity | Winner-take-all 容量瓶颈 d²≍n log n，TAM 提升至 d²≍n / WTA capacity bottleneck d²≍n log n, TAM improves to d²≍n | 注意力层记忆容量理论 / Attention memory capacity theory |
| [[2605.04946v1]] Batch Normalization Geometry | BN 在每个神经元处诱导参考超平面精化局部分区 / BN induces reference hyperplane refining local partitions per neuron | 归一化层几何理论 / Normalization layer geometry theory |
| [[2605.04932v1]] Jacobian-Velocity Deployment Risk | 方向性 Jacobian 能量上界部署风险漂移 / Directional Jacobian energy bounds deployment risk under drift | 分布漂移鲁棒性理论 / Distribution drift robustness theory |
| [[2605.05029v1]] Predictive-Causal Gap | 最小化预测目标必然偏离因果编码器（不可能定理） / Minimizing predictive objective necessarily deviates from causal encoder (impossibility) | 表征学习可靠性基础 / Representation learning reliability |
| [[2605.05179v1]] Cumulant Propagation MLP | 无采样算法以 100× 少 FLOPs 估计随机 MLP 期望输出 / Sampling-free algorithm estimates random MLP expected output at 100× less FLOPs | 随机神经网络可靠性估计 / Stochastic NN reliability estimation |
| [[2605.04373v1]] REGUARD RL Controller | 双层遗憾最大化+逻辑规则实现推理时 RL 保护 / Bilevel regret maximization + logic rules for inference-time RL protection | RL 可靠性与可解释性 / RL reliability & interpretability |

---

### 主题 6：其他相关 / Other Relevant Papers

| 论文 Paper | 核心贡献 Key Contribution | 相关性 Relevance |
|---|---|---|
| [[2605.05080v1]] Pinocchio Dimension LLM | LLM 心理测量差异主轴是现象性自我表征而非人格 / Primary axis of LLM psychometric differences is phenomenal self-representation not personality | 后训练效果与自我表征 / Post-training effects & self-representation |
| [[2605.05090v1]] Intervention Side Effects | 对比式自动审计发现 ROME/蒸馏/遗忘的意外副作用 / Contrastive audit reveals unexpected side effects of ROME/distillation/unlearning | LLM 干预副作用检测 / LLM intervention side-effect detection |
| [[2605.04830v1]] Diffusion Model Phase Transitions | DiT 中对称破缺与非局域性相变临界窗口同时出现 / Symmetry breaking and nonlocality phase transitions co-occur in DiT | 生成模型训练动力学 / Generative model training dynamics |
| [[2605.05058v1]] SoK Jailbreak Robustness | 11 模型×13 攻击×5 防御的越狱系统综述+安全立方体框架 / SoK of 11 models×13 attacks×5 defenses + Security Cube framework | LLM 安全鲁棒性 / LLM security robustness |
| [[2605.05116v1]] Hardness of Junking LLMs | 纯随机 token 在对齐模型上实现 52-90% 攻击成功率 / Pure random tokens achieve 52-90% ASR on aligned models | 对齐鲁棒性 / Alignment robustness |
| [[2605.05267v1]] LLM Code Quality Review | 114 篇论文揭示 18 种训练数据缺陷传播到代码生成缺陷 / 114-paper review reveals 18 training data defect→code generation defect pathways | 训练数据与生成可靠性 / Training data & generation reliability |
| [[2605.05151v1]] SAE Time Series Superposition | SAE 证明时序预测 Transformer 不依赖叠加机制 / SAE proves time-series prediction Transformers don't rely on superposition | 机理可解释性工具验证 / Mechanistic interpretability tool validation |
| [[2605.05125v2]] LLM Causal Healthcare Imputation | LLM 驱动进化搜索生成可验证 MNAR 插补代码 / LLM-driven evolutionary search generates verifiable MNAR imputation code | LLM 可靠性应用 / LLM reliability applications |
| [[2605.04506v1]] ILOV3SPLAT 3D Scene | 3D-GS 框架内开放词汇实例级 3D 检索与分割 / Open-vocabulary instance-level 3D retrieval & segmentation within 3D-GS | 场景理解（间接相关）/ Scene understanding (indirect) |
| [[2605.04573v1]] Mixed FEM Geometrically Exact Beams | 离散曲率允许不连续转动的无锁梁单元 / Discrete curvature allows locking-free beam elements with discontinuous rotations | 数值稳定性方法论（弱相关）/ Numerical stability methodology (weak) |
| [[2605.05360v1]] CopyCop GNN Fingerprinting | 嵌入稳定点不变量用于 GNN 所有权验证 / Embedding stationary point invariants for GNN ownership verification | 模型可信度（间接）/ Model trustworthiness (indirect) |
| [[2605.05192v1]] Almost-Orthogonality Lp | 反驳 Lp 空间近似正交三角不等式猜想 / Refutes conjectured triangle inequality for almost-orthogonality in Lp spaces | 数学基础（弱相关）/ Mathematical foundations (weak) |

---

## All Papers

| Paper | Score | TL;DR |
|---|---|---|
| [[2605.04373v1]] REGUARD RL Network Controllers | 3 | 双层遗憾最大化+逻辑规则实现推理时 RL 保护，最坏情形性能差距缩减 85% / Bilevel regret maximization + logic rules for inference-time RL protection, closing 85% of worst-case performance gaps |
| [[2605.04396v1]] Critical Windows Transformers | 4 | 权重衰减施加时机（约 25% 训练步、100 步宽窗口）决定 Transformer 记忆vs推理命运 / Weight decay timing (25% into training, 100-step window) determines Transformer memorize-vs-reason fate |
| [[2605.04418v1]] MACRO Manifold Constraints LLM | 5 | 黎曼流形约束可证明地替代 RMSNorm 与权重衰减，从理论上祛魅 LLM 预训练启发式 / Riemannian manifold constraints provably replace RMSNorm and weight decay, demystifying LLM pre-training heuristics |
| [[2605.04431v1]] Robust RFT Failure Management | 5 | RFT-FaultBench+RFT-FM 框架实现强化微调训练异常的自动检测、归因与修复 / RFT-FaultBench+RFT-FM framework for automatic detection, attribution, and repair of reinforcement fine-tuning failures |
| [[2605.04454v1]] Deployment Alignment Evaluation | 3 | 16 个对齐基准审计证明仅凭模型级评估无法推断部署对齐状况 / Audit of 16 alignment benchmarks proves model-level evaluation cannot infer deployment alignment |
| [[2605.04468v1]] Anchored Learning SFT | 4 | 显式 KL 上界动态插值将 SFT 通用能力损失从 53% 压低到 5% / Explicit KL-bounded dynamic interpolation reduces SFT general capability loss from 53% to 5% |
| [[2605.04478v1]] CCL-D Slow/Hang Diagnosis | 5 | NCCL/RCCL 细粒度指标将 4000 GPU 训练慢/挂根因定位缩短到 6 分钟，开销 <1% / Fine-grained NCCL/RCCL metrics reduce slow/hang root-cause localization to <6 minutes on 4k GPUs with <1% overhead |
| [[2605.04506v1]] ILOV3SPLAT 3D Scene Understanding | 2 | CLIP 语言特征场+SAM 实例对比特征场实现无标注开放词汇 3D 实例检索 / CLIP language feature field + SAM instance contrastive feature field for annotation-free open-vocabulary 3D instance retrieval |
| [[2605.04563v1]] RangeGuard Approximate ECC | 5 | 值域 ECC 保护在 BER 1e-5 下保持 LLM 接近无错精度，每块容忍 64+ 比特错误 / Range-based ECC keeps LLM near-error-free at BER 1e-5, tolerating 64+ bit errors per block |
| [[2605.04572v1]] Parameter Dynamics Safety Scoring | 2 | 样本级危险方向参数更新投影差量化微调安全退化风险 / Sample-level dangerous-direction parameter update projection scores quantify fine-tuning safety degradation risk |
| [[2605.04573v1]] Mixed FEM Geometrically Exact Beams | 1 | 离散曲率允许不连续转动的最低阶无锁几何精确梁单元 / Discrete curvature concept enables lowest-order locking-free geometrically exact beam elements with discontinuous rotations |
| [[2605.04624v1]] AuditRepairBench Evaluator Stability | 3 | 96k 配对执行轨迹揭示评估器-选择器耦合导致 agent 排行榜系统性重排 / 96k paired execution traces reveal evaluator-selector coupling causes systematic agent leaderboard reordering |
| [[2605.04638v1]] SemGrad LLM Uncertainty | 3 | 语义保留嵌入梯度范数单次前向传播不确定性量化，AUROC 超语义自洽 3.27 点 / Semantic-preserving embedding gradient norm quantifies uncertainty in single forward pass, +3.27 AUROC over semantic consistency |
| [[2605.04665v1]] Paraphrase Output Mode Collapse | 3 | 语义等价改写使 78% 封闭式答案格式崩溃，任务结构比模型家族更能预测风险 / Semantically equivalent paraphrase collapses 78% of closed-form answer formats; task structure predicts risk better than model family |
| [[2605.04683v1]] Average Attention Arithmetic Circuits | 3 | 平均注意力 Transformer 编码器与 FSAC⁰_R[sign] 函数类精确等价 / Average attention Transformer encoder exactly equivalent to FSAC⁰_R[sign] function class |
| [[2605.04711v1]] BAOC Budget-Aware Optimizer | 3 | 基于梯度统计+MILP 的预算感知按块优化器配置器，显著降低优化器状态显存 / Gradient-statistics+MILP budget-aware block-wise optimizer configurator, significantly reducing optimizer state memory |
| [[2605.04727v1]] Knowledge Tracing Reliability | 3 | 修正注意力 Softmax 轴向错误后注意力增强 PKT 模型优势大幅缩小 / Fixing attention Softmax axis error largely eliminates attention-augmented PKT model advantages |
| [[2605.04738v1]] OSAQ LLM Quantization | 3 | Hessian 零空间闭式权重变换将 2-bit GPTQ 困惑度降低 40%+ / Hessian null-space closed-form weight transform reduces 2-bit GPTQ perplexity by 40%+ |
| [[2605.04754v1]] AxMoE Approximate Multipliers MoE | 3 | 首个近似乘法器×MoE 拓扑交互研究，ViT Hard MoE r=0.25 在最激进近似下超越 Dense | First study of approx-multiplier×MoE topology interactions; ViT Hard MoE r=0.25 outperforms Dense under most aggressive approximation |
| [[2605.04803v1]] RISC-V Vector Fault Injection SDC | 4 | 10 万次 RTL 故障注入证明 FP32/BF16 指数位 SDC 最严重，支持选择性硬化 / 100k RTL fault injections show FP32/BF16 exponent bits cause worst SDC, supporting selective hardening |
| [[2605.04830v1]] Diffusion Phase Transitions DiT | 2 | DiT 中对称破缺与非局域性相变临界窗口在时间轴上近乎同时出现 / Symmetry breaking and nonlocality phase transitions co-occur at nearly the same critical window in DiT |
| [[2605.04893v1]] Self-Attention Transport Spectral Diagnostics | 4 | 双轴谱诊断（电导+反对称系数）纠正注意力"方向盲"缺陷，幻觉检测 AUROC 0.84 / Dual-axis spectral diagnostics (conductance + antisymmetry) fix attention "direction blindness", hallucination AUROC 0.84 |
| [[2605.04899v1]] Geometric Error LM Hidden State | 3 | Holonomy（曲率）作为取向化不确定性测度，与世界模型向量系统性耦合 / Holonomy as oriented uncertainty measure systematically coupled to world model vectors |
| [[2605.04932v1]] Jacobian-Velocity Deployment Risk | 1 | 方向性 Jacobian 能量上界部署风险漂移，提出漂移方向对齐正则化 DTR / Directional Jacobian energy bounds deployment risk under covariate drift; drift-aligned tangent regularization (DTR) proposed |
| [[2605.04946v1]] Batch Normalization Partition Geometry | 2 | BN 在每个神经元处诱导参考超平面，精化 CPA 网络局部仿射分区计数 / BN induces reference hyperplane per neuron, refining local affine partition count in CPA networks |
| [[2605.04971v1]] Geometric Continuity Deep Networks | 3 | 残差连接+对称破缺非线性（缺一不可）解释深度网络跨层权重几何连续性 / Residual connections + symmetry-breaking nonlinearity (both necessary) explain cross-layer weight geometric continuity |
| [[2605.04980v1]] Conceptors Semantic Steering | 4 | Conceptor 软投影矩阵+Boolean 代数实现可组合语义控制，退化输出从 58% 降至 13% / Conceptor soft projection matrices + Boolean algebra enable composable semantic control, reducing degenerate outputs from 58% to 13% |
| [[2605.05025v1]] Attention Divergence Hallucination Detection | 4 | 注意力分布 KL 散度轻量级探针 AUROC 0.78-0.91，单次前向传播无需多次采样 / Attention distribution KL divergence lightweight probe AUROC 0.78-0.91, single forward pass without multiple sampling |
| [[2605.05029v1]] Predictive-Causal Gap Impossibility | 3 | 证明最小化预测目标必然偏离因果编码器，2695 次实验均值因果保真度仅 0.49 / Proves minimizing predictive objective necessarily deviates from causal encoder; mean causal fidelity only 0.49 across 2695 experiments |
| [[2605.05058v1]] SoK Jailbreak Robustness LLM | 3 | 11 模型×13 攻击×5 防御系统综述，深层隐藏状态可区分良性/对抗样本 / SoK of 11 models×13 attacks×5 defenses; deep hidden states separate benign/adversarial samples |
| [[2605.05066v1]] Impossibility Triangle Long-Context | 4 | 信息论证明长序列建模效率/紧凑性/召回不可兼得，52 种架构归类框架 / Information-theoretic proof of efficiency/compactness/recall impossibility triangle; classifies 52 architectures |
| [[2605.05080v1]] Pinocchio Dimension LLM Psychometrics | 3 | LLM 心理测量差异主轴（47.1% 方差）是后训练塑造的现象性自我表征，非人格特质 / Primary axis of LLM psychometric differences (47.1% variance) is post-training-shaped phenomenal self-representation, not personality traits |
| [[2605.05090v1]] Automatic LLM Intervention Audit | 3 | 对比式审计流水线揭示 ROME/蒸馏/遗忘等干预的意外副作用（规范性偏移、话题漂移） / Contrastive audit pipeline reveals unexpected side effects of ROME/distillation/unlearning (normative shift, topic drift) |
| [[2605.05113v1]] Signal Propagation Linear Recurrences | 4 | 精确有限宽度公式证明 Glorot 初始化在 √n 深度（而非 n）即开始失稳 / Exact finite-width formula proves Glorot init destabilizes at √n depth (not n) for linear recurrences |
| [[2605.05115v1]] Manifold Steering Representation Geometry | 4 | 测地线激活引导揭示激活流形与行为流形近似等距同构（r=0.99/0.89） / Geodesic activation steering reveals near-isometry between activation manifold and behavior manifold (r=0.99/0.89) |
| [[2605.05116v1]] Hardness of Junking LLMs | 3 | 纯随机 token 序列在对齐 7B LLM 上实现 52-90% 攻击成功率 / Pure random token sequences achieve 52-90% ASR on aligned 7B LLMs |
| [[2605.05125v2]] LLM-Driven MNAR Imputation Causal | 2 | LLM 进化搜索生成可验证 MNAR 插补代码，因果流估计与 RCT 证据一致 / LLM evolutionary search generates verifiable MNAR imputation code; causal flow estimates consistent with RCT evidence |
| [[2605.05134v1]] Koopman Hallucination Detection | 3 | Koopman 算子动力系统建模幻觉轨迹，单次推理无需外部知识 / Koopman operator dynamical system models hallucination trajectories, single inference without external knowledge |
| [[2605.05151v1]] SAE Time Series Superposition | 3 | SAE 因果干预证明叠加机制在时序预测 Transformer 中非必要 / SAE causal interventions prove superposition is unnecessary in time-series prediction Transformers |
| [[2605.05166v1]] First Token Hallucination Detection | 4 | 首 token 归一化熵以 1/11 代价（AUROC 0.820）匹配或超越语义自洽性方法 / First-token normalized entropy matches semantic consistency (AUROC 0.820) at 1/11 the cost |
| [[2605.05176v1]] ICL Nonlinear Regression Theory | 3 | 注意力作为特征化器严格证明 Transformer ICL 泛化误差界 O(1/n + √(n log L)/√L) / Attention-as-featurizer rigorously proves Transformer ICL generalization bound O(1/n + √(n log L)/√L) |
| [[2605.05179v1]] Cumulant Propagation Random MLP | 3 | 累积量传播算法以 100× 少 FLOPs 估计宽随机 MLP 期望输出 / Cumulant propagation algorithm estimates wide random MLP expected output at 100× fewer FLOPs than sampling |
| [[2605.05189v1]] Linear Associative Memory Capacity | 3 | TAM 准则将线性联想记忆容量从 d²≍n log n 提升至 d²≍n 并给出完整相变理论 / TAM criterion improves linear associative memory capacity from d²≍n log n to d²≍n with complete phase transition theory |
| [[2605.05192v1]] Almost-Orthogonality Lp Spaces | 1 | 反驳 Lp 空间近似正交三角不等式猜想，确定最优临界指数 c=p' / Refutes Lp almost-orthogonality triangle inequality conjecture; determines optimal critical exponent c=p' |
| [[2605.05197v1]] Grammaticality Implicit LLM | 4 | LLM 隐藏状态比字符串概率更精准编码语法性，仅需约 10 个神经元且跨语言稳健 / LLM hidden states encode grammaticality more accurately than string probability, requiring only ~10 neurons and robust cross-lingually |
| [[2605.05267v1]] LLM Code Quality Review | 3 | 114 篇论文系统综述揭示 18 种训练数据缺陷传播路径到代码生成缺陷 / 114-paper systematic review reveals 18 training data defect propagation pathways to code generation defects |
| [[2605.05341v1]] Feature Starvation SAE Stability | 4 | AEN-SAE 将死特征率从 95% 降至 39%，无需重采样或 ghost gradient / AEN-SAE reduces dead feature rate from 95% to 39% without auxiliary heuristics like resampling or ghost gradients |
| [[2605.05360v1]] CopyCop GNN Fingerprinting | 2 | 嵌入稳定点不变量在跨架构、跨变换下识别 GNN 代理模型（73% 组合 AUC=1.0） / Embedding stationary point invariants identify GNN surrogate models across architectures and transforms (73% combinations AUC=1.0) |
| [[2605.05436v1]] Implicit Regularization Estimation | 3 | 梯度匹配量化早停/dropout/离散步长引入的隐式正则化等效惩罚 / Gradient matching quantifies implicit regularization equivalent penalties introduced by early stopping, dropout, and discrete step sizes |
| [[2605.05438v1]] Semantic Loss Model Collapse | 3 | 图逻辑约束语义损失+动态 lambda 消除因果推理微调 100% 崩溃率 / Graph-logic semantic loss + dynamic lambda eliminates 100% collapse rate in causal reasoning fine-tuning |
| [[2605.05443v1]] SLAM Structural Watermarking | 4 | SAE 定位句法方向+因果激活操控实现 100% 水印检测率，质量代价仅 1-2 reward 分 / SAE locates syntactic directions + causal steering achieves 100% watermark detection at only 1-2 reward-score quality cost |
