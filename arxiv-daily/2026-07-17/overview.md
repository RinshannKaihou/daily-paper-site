---
title: "Daily arXiv Digest — 2026-07-17"
date: 2026-07-17
tags:
  - llm-evaluation
  - llm-agents
  - ai-safety
  - mechanistic-interpretability
  - optimization-theory
  - uncertainty-quantification
  - causal-reasoning
  - rlvr
  - long-context
  - scientific-automation
papers: 50
---

# Daily arXiv Digest — 2026-07-17

> 本日共筛选 **50** 篇论文，覆盖 LLM 评测、智能体安全、机制可解释性、优化与采样理论、不确定性量化、因果推理、长上下文训练与科学自动化等方向。
> **50 papers** curated today, spanning LLM evaluation, agent safety, mechanistic interpretability, optimization & sampling theory, uncertainty quantification, causal reasoning, long-context training, and scientific automation.

---

## 今日必读 / Must Read Today

### 1. [[2607.14530]] xHC: Expanded Hyper-Connections

- **中文推荐理由**：xHC 是首个将 Hyper-Connections 的残差流扩展率 N 从 4 显著推到 16 的方法，通过多尺度因果卷积 + 稀疏残差流架构，在 18B/28B MoE 上让下游平均提升 4.5 个点且 pretraining FLOPs 反而更低。对关心 Transformer 架构创新与 MoE 预训练效率的人来说，这是今天最有工程价值的一篇。
- **English reason**: xHC is the first Hyper-Connections variant to push the residual-stream expansion rate N meaningfully beyond 4 (up to 16), and on 18B/28B MoE it lifts downstream average by ~4.5 points while *lowering* pretraining FLOPs — easily the most engineering-relevant architecture paper today for anyone tracking Transformer/MoE pretraining.

### 2. [[2607.14552]] Answer-Conditioned Chains of Thought Degrade Verifiable-Reasoning Distillation

- **中文推荐理由**：作者用一个"控制单一变量"的实验干净地证明——让生成器在看到金答案后再写 CoT（即使最终答案正确）也会显著伤害学生模型的可验证推理能力（Qwen3-8B 在 MATH 上掉点）。这条结论直接冲击了当下主流的"答案条件蒸馏"数据构造范式，方法论漂亮、结论可立即指导 SFT 数据管线。
- **English reason**: A pristine one-bit controlled experiment shows that letting the generator write CoT after seeing the gold answer (even when correct) measurably degrades a student's verifiable reasoning (Qwen3-8B drops on MATH). The finding directly challenges the dominant answer-conditioned distillation recipe and is immediately actionable for SFT data pipelines.

### 3. [[2607.14890]] Proof-or-Stop: Don't Trust the Agent, Trust the Evidence

- **中文推荐理由**：Proof-or-Stop 把自主编码 Agent 的"已测试/已审阅/可合并"等状态声明重新定义为需被证据裁决的 claim，在 9,240 个 cell 的预注册消融中把"可见测试通过但隐藏 oracle 仍失败"的情况削减 76%。这是今天对 AI 编码智能体生命周期治理与安全工程最系统的一篇。
- **English reason**: Proof-or-Stop reframes autonomous coding-agent lifecycle claims (reviewed / tested / ready-to-merge) as admissibility decisions requiring evidence, and in a 9,240-cell pre-registered ablation cuts "visible-tests-pass-but-hidden-oracle-fails" cases by 76%. The most systematic treatment of AI coding-agent governance and safety engineering today.

---

## 按主题分类 / Papers by Topic

### LLM 评测与基准 / LLM Evaluation & Benchmarking

| Paper | 主题 / Topic | 核心发现 / Key Finding |
|---|---|---|
| [[2607.14480]] LLM Evaluators are Biased across Languages | 多语言评估器偏差 / Multilingual evaluator bias | 揭示 LLM 评估器在 23 种语言下对低资源语言系统性更宽容（Spearman ρ=−0.81），偏差在校准后依然存在。 Shows LLM evaluators systematically grade low-resource languages more leniently across 23 languages (ρ=−0.81); bias persists after calibration. |
| [[2607.14528]] CRTBench | 逻辑一致性评测 / Logical consistency benchmark | 350 题族、1750 道题的受控改写基准，GPT-5.4-mini 单题 98.9% 但改写后一致性仅 ~50%。 A 350-family controlled-reformulation benchmark; GPT-5.4-mini hits 98.9% single-question acc but only ~50% reformulation consistency. |
| [[2607.14707]] LLMs for Academic Supervision | 工程化 vs 裸 LLM / Engineered vs bare LLM | 用 LangGraph 包装 GPT-4o-mini 的七模块系统在六维盲评上全面胜过无脚手架 GPT-5（4.08 vs 2.79）。 A LangGraph-wrapped GPT-4o-mini seven-module system beats bare GPT-5 on all six blind-eval dimensions (4.08 vs 2.79). |
| [[2607.14817]] Epistemic Uncertainty Beyond OOD | 不确定性评测框架 / Uncertainty eval framework | 指出 OOD/AL 代理任务与"最小化部署 regret"在贝叶斯最优层面不一致，提出统一的覆盖/风险/regret 阈值框架。 Argues OOD/active-learning proxies are Bayes-suboptimal vs deployment regret; proposes a unified coverage/risk/regret threshold framework. |
| [[2607.15190]] Can We Trust IRT for AI Eval? | IRT 在 LLM 评测的失效 / IRT failure in LLM eval | 18000 种条件模拟揭示经典 IRT 估计器在大基准上不可行、小样本下严重失真。 An 18,000-condition simulation shows classical IRT estimators are infeasible on large benchmarks and badly biased at small samples. |
| [[2607.15277]] Partition, Prompt, Aggregate | 自洽性检查 / Self-consistency check | 提出无参考答案的 split/order 一致性检查，并指出"宏观谬误"使条件估计重组反而更准。 Proposes reference-free split/order consistency checks and identifies a "macro fallacy" where conditional estimates re-aggregate closer to truth. |

### 智能体安全与控制 / Agent Safety & Control

| Paper | 主题 / Topic | 核心发现 / Key Finding |
|---|---|---|
| [[2607.14570]] IFG Structural Monitoring | IaC 篡改检测 / IaC sabotage detection | 用未训练的信息流图监视器在 iac_cdk 上 AUROC 0.86，无需攻击日志训练。 An untrained Information Flow Graph monitor reaches AUROC 0.86 on iac_cdk without attack-log training. |
| [[2607.14890]] Proof-or-Stop | 智能体生命周期证据门控 / Agent lifecycle evidence gating | 把 agent claim 视作可裁决的 admissibility decision，预注册消融把假通过削减 76%。 Treats agent claims as admissibility decisions; pre-registered ablation cuts false passes by 76%. |
| [[2607.15218]] Physical Danger Beyond Text | 物理 vs 文本危险 / Physical vs content danger | 证明 LLM 表示空间中"物理危险"与"内容危险"是两个可分离方向，据此训练 PRISM 检测器。 Shows physical danger and content danger occupy separable directions in LLM hidden state; trains a PRISM detector from this. |
| [[2607.14791]] Transcoders for Deception | 欺骗电路 / Deception circuits | 用 Qwen3-4B 逐层 transcoder 构建 attribution graph，对指令下的隐瞒行为做电路级解释。 Builds attribution graphs with per-layer transcoders on Qwen3-4B to circuit-explain instruction-induced deception. |
| [[2607.14826]] Interventional Causal Circuits | 机器人动作因果调试 / Causal robot action debugging | 将 JPT 升级为因果电路，使被拒动作能自动定位失败参数并一次性修正。 Upgrades a Joint Probability Tree into a causal circuit that pinpoints failing action params and suggests one-shot fixes. |

### 机制可解释性与探测 / Mechanistic Interpretability & Probing

| Paper | 主题 / Topic | 核心发现 / Key Finding |
|---|---|---|
| [[2607.14943]] Steering Robustness into WAMs | WAM 鲁棒性激活分析 / WAM robustness activation analysis | 发现 Cosmos-Policy/DiT4DiT 的鲁棒性特征呈低维线性可分，单向量 steering 即可提升 OOD 表现。 Finds robustness features in Cosmos-Policy/DiT4DiT are low-dim linearly separable; single-vector steering improves OOD behavior. |
| [[2607.15175]] Linear Representations of Grammaticality | 合语法性线性表示 / Linear grammaticality | 25 个模型上证明合语法/不合语法句子沿单一方向分离，可跨语言跨现象泛化。 Across 25 PLMs, grammatical vs ungrammatical sentences separate along one linear direction generalizing across languages. |
| [[2607.15084]] Membership Info in Hyperspherical Embeddings | 人脸模型隐私审计 / Face model privacy audit | 180 个人脸模型全因子实验量化超球面聚类中残留的成员推断信号。 A 180-model factorial study quantifies residual membership-inference signal in hyperspherical face embeddings. |
| [[2607.14967]] Latent Trajectory AIGTD | AI 文本检测 / AI-text detection | 把 AI 文本检测重建模为潜空间轨迹判别，在 RAID/NYT-AI/Reviews 上超越基线。 Reframes AI-text detection as latent-trajectory discrimination; beats baselines on RAID/NYT-AI/Reviews. |

### 优化器、采样与训练理论 / Optimizers, Sampling & Training Theory

| Paper | 主题 / Topic | 核心发现 / Key Finding |
|---|---|---|
| [[2607.14536]] Muse: Muon Representation Geometry | Muon 优化器几何 / Muon optimizer geometry | 把 Muon 的矩阵化表示重定义为几何选择，构造从 Native 到 nSGDM 的表示阶梯并证明 rank/norm scaling 由短边决定。 Reframes Muon's matrix representation as geometry; builds a Native→nSGDM ladder and proves rank/norm scaling is governed by the short side. |
| [[2607.14516]] Adaptive RK–Adam Compute-Matched Study | RK-Adam 严格对照 / RK-Adam controlled study | 算力严格匹配下 RK3(2)-Adam 训练损失低 40 倍但泛化无收益，揭示"自适应步长"实为惰性。 Under compute-matched protocol RK3(2)-Adam lowers full-batch loss 40× but yields no generalization gain; "adaptive" step is effectively inert. |
| [[2607.14731]] Local SGD Smoothness Constant | Local SGD 收敛率 / Local SGD convergence | 证明有界二阶异质性即可使 Local SGD 在远比一阶假设宽松的条件下优于 Mini-batch SGD。 Proves bounded second-order heterogeneity suffices for Local SGD to beat Mini-batch SGD under far weaker assumptions. |
| [[2607.14576]] Stable Residual Networks Sharp Threshold | 残差网络稳定性阈值 / ResNet stability threshold | 残差块速度场的亚线性增长（q≤1）是训练稳定性的尖锐充要阈值。 Sublinear growth (q≤1) of a residual block's velocity field is the sharp necessary-and-sufficient stability threshold. |
| [[2607.14862]] Tamed Stochastic Gradient HMC | 驯服 SGHMC / Tamed SGHMC | 首个驯服版 SGHMC，对超线性增长梯度证明 Wasserstein-2 收敛率 1/2。 First tamed SGHMC variant; achieves Wasserstein-2 rate 1/2 under relaxed conditions for superlinearly growing gradients. |
| [[2607.15208]] Delocalization of Bias in HMC | HMC 偏差离域化 / HMC bias delocalization | 将"偏差离域化"从过阻尼 Langevin 推广到未校正 HMC 与 BAOAB，控制任意可观测的总误差。 Extends "delocalization of bias" to unadjusted HMC and BAOAB; total error of any observable can be controlled. |
| [[2607.14889]] Optimal Combination of Binary Classifiers | 分类器集成理论 / Classifier ensemble theory | 把 Bartlett 的 1D classification-calibrated risk 推广到 m 维并证明凸化全局最小唯一性。 Generalizes Bartlett's 1D calibrated risk to m dimensions and proves uniqueness of the convexified global minimum. |

### LLM 训练、推理与对齐 / LLM Training, Inference & Alignment

| Paper | 主题 / Topic | 核心发现 / Key Finding |
|---|---|---|
| [[2607.14530]] xHC: Expanded Hyper-Connections | Transformer 架构 / Transformer architecture | 残差流扩展率 N 推到 16，18B/28B MoE 下游均值 +4.5、FLOPs 更低。 Pushes residual-stream expansion N to 16; +4.5 downstream avg on 18B/28B MoE at lower FLOPs. |
| [[2607.14506]] Non-vacuous RLVR Generalization Bounds | RLVR PAC-Bayes 界 / RLVR PAC-Bayes bounds | 首个 RLVR 非空 PAC-Bayes 界，Progressive RLVR 流水线给出可证明泛化保证。 First non-vacuous PAC-Bayes bound for RLVR; Progressive RLVR pipeline gives provable generalization. |
| [[2607.14552]] Answer-Conditioned CoT Degrades Distillation | 答案条件蒸馏危害 / Answer-conditioned distillation harm | 一比特对照实验证明看金答案写 CoT 即使答案正确也伤害学生可验证推理。 A one-bit controlled experiment: CoT written after seeing the gold answer degrades student's verifiable reasoning even when correct. |
| [[2607.14777]] SEED On-Policy Distillation | 自演化策略蒸馏 / Self-evolving policy distillation | 策略自做 hindsight 分析生成密集 token 级蒸馏信号，长程 agentic RL 任务显著提升。 Policy acts as its own hindsight analyzer producing dense token-level distillation; large gains on long-horizon agentic RL. |
| [[2607.14466]] Interleaved Noise Injection | 交替噪声课程 / Interleaved noise curriculum | 干净/噪声 epoch 开关式切换，CIFAR-100-C/ImageNet-C/R 上同时提升精度与鲁棒性。 Square-wave clean/noise epoch switching improves clean acc, corruption robustness, and OOD on CIFAR-100-C/ImageNet-C/R. |
| [[2607.14463]] DSAE Hidden-State Collapse | 表示坍缩 / Representation collapse | DSAE 在 K=5 编码器深度下隐藏状态坍缩至 1e-5，LiDAR 分类退化至多数类。 DSAE hidden state collapses to ~1e-5 at depth K=5; LiDAR classification degrades to majority class. |

### 长上下文、量化与系统 / Long-Context, Quantization & Systems

| Paper | 主题 / Topic | 核心发现 / Key Finding |
|---|---|---|
| [[2607.14952]] LongStraw | 固定预算长上下文 RL / Fixed-budget long-context RL | 张量生命周期重写把 GRPO 活图从 P+R 压到 R，8×H20 上 Qwen3 训到 2M+ token。 Reframes GRPO as a tensor-lifetime problem, compressing live graph from P+R to R; trains Qwen3 to 2M+ tokens on 8×H20. |
| [[2607.15105]] Long-Context Fine-Tuning with Limited VRAM | 低 VRAM 长上下文 QLoRA / Low-VRAM long-context QLoRA | HGA + 分段反向传播 + 分层 KV 存储，16GB 上对 Qwen3-8B 做 4-bit QLoRA 微调。 HGA + segment-wise backprop + tiered KV storage enables 4-bit QLoRA of Qwen3-8B on 16 GB VRAM. |
| [[2607.14618]] PolyQ | CPU 量化-编译器协同 / CPU quant-compiler co-design | 逐通道 {2,3,4,8,16}-bit 分配，3-bit 目标下相比 AWQ 显著提速且精度持平。 Per-channel {2,3,4,8,16}-bit allocation; 3-bit target beats AWQ in speed at parity accuracy. |
| [[2607.14541]] Atrex-Bench | GPU kernel 生成基准 / GPU kernel-gen benchmark | 首个生产 trace 采样基准（30 算子 440 shape），Atrex-Kernel-Agent 大幅超越通用编码 agent。 First production-trace-sampled kernel benchmark (30 ops, 440 shapes); Atrex-Kernel-Agent beats general coding agents. |

### 强化学习与决策理论 / RL & Decision Theory

| Paper | 主题 / Topic | 核心发现 / Key Finding |
|---|---|---|
| [[2607.15003]] SMC-ES | 形式验证控制策略 / Formally verified control | 进化策略 + 统计模型检验交替，为 MuJoCo/Safety Gymnasium 合成带形式化保证的 NN 策略。 ES + statistical model checking synthesize NN policies with formal guarantees on MuJoCo/Safety Gymnasium. |
| [[2607.14877]] PAC Learning in Stochastic Games | 随机博弈 PAC 学习 / TBSG PAC learning | 首个回合制随机博弈可达性目标的去中心化 PAC 正面结果，LeTuReGa 给出多项式样本复杂度。 First positive decentralized PAC result for TBSG reachability; LeTuReGa gives polynomial sample complexity. |
| [[2607.15067]] Kernel-WIS Off-Policy Evaluation | 核加权 OPE / Kernel-weighted OPE | 用 Nadaraya-Watson 核回归统一 WIS 有界性与 VIS 独立性。 Replaces self-normalization with Nadaraya-Watson kernel regression, unifying WIS boundedness and VIS independence. |
| [[2607.15080]] Covariate Balance for Offline RL | 离线 RL 协变量均衡 / Offline-RL covariate balance | 将协变量均衡诊断扩展到时间相关 OPE，证明脓毒症 RL 研究多无法通过该检验。 Extends covariate-balance diagnostics to time-dependent OPE; shows sepsis RL studies largely fail the test. |
| [[2607.14658]] TopoAgent | 多模态科学推理 agent / Multimodal science agent | DAG 拓扑规划 + 上下文隔离 + 自适应裂变，6 基准上 66.3% 平均准确率超 AutoGen 62.x%。 DAG planning + context isolation + adaptive fission reaches 66.3% avg on 6 benchmarks, beating AutoGen 62.x%. |

### 因果推理与可解释 ML / Causal Reasoning & Explainable ML

| Paper | 主题 / Topic | 核心发现 / Key Finding |
|---|---|---|
| [[2607.14720]] Causal-Adversarial Prostate MRI | 协变量因果探测 / Causal covariate probing | 梯度反转对抗抑制 PSA/前列腺体积使 AUC 降 7.61%，证明模型依赖真实病理而非捷径。 Gradient-reversal suppression of PSA/prostate volume drops AUC by 7.61%, showing reliance on real pathology not shortcuts. |
| [[2607.14737]] GeoDetect | VLP 对抗检测 / VLP adversarial detection | 利用 VLP 嵌入各向异性，无微调跨 ALBEF/CLIP/TCL 检测对抗样本。 Exploits VLP embedding anisotropy; detects adversarial examples across ALBEF/CLIP/TCL without fine-tuning. |
| [[2607.14947]] Self-Distillation for Rectified Flow | 线性 RF 自蒸馏 / Linear RF self-distillation | 在岭回归下证明真/教师速度最优混合（系数可负）严格优于教师，给闭式系数。 Under ridge regression, optimally mixing true/teacher velocities (coefficients can be negative) strictly beats the teacher; closed form given. |

### 科学自动化与 LLM Agent / Scientific Automation & LLM Agents

| Paper | 主题 / Topic | 核心发现 / Key Finding |
|---|---|---|
| [[2607.15001]] LQCDMaster | 格点 QCD 智能体 / Lattice-QCD agent | 70 项前沿任务中精确复现 63 项专家实现，Wick 收缩工具确定性可审计。 Reproduces 63/70 expert lattice-QCD tasks; deterministic Wick-contraction tool keeps results auditable. |
| [[2607.15079]] BrainPilot | 脑科学多智能体 / Brain-science multi-agent | PI Agent 协调五专家 Agent，7233 条知识库支持人机协同脑科学发现。 A PI agent coordinates five expert agents over 7,233-entry KB for human-in-the-loop brain-science discovery. |
| [[2607.15247]] AutoSynthesis | 自动元分析 / Automated meta-analysis | LangGraph 多智能体全自动完成随机效应元分析（PRISMA/森林图/偏倚评估），Hedges' g=0.143 与人类专家一致。 LangGraph multi-agent fully automates random-effects meta-analysis (PRISMA/forest/bias); Hedges' g=0.143 matches human experts. |
| [[2607.14582]] MathCoPilot | 人机协同定理证明 / Human-AI theorem proving | "活态证明蓝图"为核心的工作台，在 FormalMATH 子集与真实 PDE 定理上系统对比多个前沿模型。 A "living proof blueprint" workbench; benchmarks Gemini 3.1 Pro/GPT-5.4/etc on FormalMATH and real PDE theorems. |
| [[2607.15164]] The Industrialization of Research | AI 科学的工业化批判 / AI-science industrialization critique | 立场文章，以 DOE Genesis Mission 为案例剖析 AI 驱动科研从 craft 到 pipeline 的伦理后果。 Position essay using DOE Genesis Mission to analyze the craft→pipeline shift and its ethical consequences. |

### 不确定性量化与统计学习 / Uncertainty Quantification & Statistical Learning

| Paper | 主题 / Topic | 核心发现 / Key Finding |
|---|---|---|
| [[2607.15196]] Subjective Risk Decomposition | 主观风险分解 / Subjective risk decomposition | 在 proper loss 下做期望主观风险的偏置-方差-熵分解，认知/偶然不确定性作为分解项自然涌现。 Bias-variance-entropy decomposition under proper losses makes epistemic/aleatoric uncertainty emerge as components. |
| [[2607.14545]] CASP Learning-Augmented Approximation | 学习增强近似算法 / Learning-augmented approximation | 倒转信息流：用负向证书 + 多项式验证器，使 NP-hard 近似比率脱离预测质量。 Reverses the signal: negative certificates + polynomial verifier decouple NP-hard approximation ratios from prediction quality. |
| [[2607.14460]] RDT Sample Covariance Spectral Error | 协方差谱范数精确界 / Sharp covariance spectral bound | 随机对偶理论给出中心化高斯样本协方差谱范数误差的精确极限闭式表达。 RDT gives the sharp closed-form limiting spectral-norm error for centered Gaussian sample covariance. |

### 视觉、检测与机器人 / Vision, Detection & Robotics

| Paper | 主题 / Topic | 核心发现 / Key Finding |
|---|---|---|
| [[2607.14560]] Breaking Forgetting in L-I3DOD | 长期增量 3D 检测 / Long-incremental 3D detection | 首次扩展到 3/5/10 增量阶段，LDMR 用学习动态驱动复习，SUN RGB-D/ScanNetV2 上显著抗遗忘。 First 3/5/10-stage incremental 3D detection; LDMR uses learning dynamics for replay, large anti-forgetting gains. |
| [[2607.14760]] Clean-Reference Camera Tamper Detection | 摄像头篡改流式检测 / Streaming camera-tamper detection | 轻量可审计状态机，320 序列上 F1=0.800，比直方图差异基线配对正胜。 Auditable state machine reaches F1=0.800 on 320 sequences, paired-beating histogram-diff baselines. |

---

## All Papers

| # | arXiv ID | 标题 / Title |
|---|---|---|
| 1 | [[2607.14460]] | Precise sample covariance spectral norm error – an RDT view |
| 2 | [[2607.14463]] | Depth-Dependent Hidden-State Collapse in Dynamical System Autoencoders |
| 3 | [[2607.14466]] | Interleaved Noise Injection Improves Clean, Corrupted, and OOD Performance |
| 4 | [[2607.14480]] | LLM Evaluators are Biased across Languages |
| 5 | [[2607.14506]] | Non-vacuous Generalization Bounds for RLVR |
| 6 | [[2607.14516]] | Adaptive Runge–Kutta Step Control Buys Training Loss, Not Generalization |
| 7 | [[2607.14528]] | CRTBench: Controlled Reformulation Testing for Logical Consistency |
| 8 | [[2607.14530]] | xHC: Expanded Hyper-Connections |
| 9 | [[2607.14536]] | Muse: Representation Geometry of Muon Beyond Normalized Momentum |
| 10 | [[2607.14541]] | Atrex-Bench: Are LLM-Generated GPU Kernels Production-Ready? |
| 11 | [[2607.14545]] | CASP: Learning-Augmented Offline Approximation with Verifiable Certificates |
| 12 | [[2607.14552]] | Answer-Conditioned Chains of Thought Degrade Verifiable-Reasoning Distillation |
| 13 | [[2607.14560]] | Breaking the Model Forgetting Cycle in Long-Incremental 3D Object Detection |
| 14 | [[2607.14570]] | Democratizing Agent Deployment Safety: A Structural Monitoring Approach |
| 15 | [[2607.14576]] | Sharp Stability Threshold and Certification for Stable Residual Networks |
| 16 | [[2607.14582]] | MathCoPilot: Interactive Human-AI Symbiotic Theorem Proving |
| 17 | [[2607.14618]] | PolyQ: Codesigning End-to-End Quantization for Scalable Edge |
| 18 | [[2607.14658]] | TopoAgent: A Self-Evolving Topological Agent for Multimodal Scientific Reasoning |
| 19 | [[2607.14707]] | Harnessing LLMs for Reliable Academic Supervision |
| 20 | [[2607.14720]] | Causal-Adversarial Probing of Clinical Covariates for Prostate MRI Grading |
| 21 | [[2607.14731]] | What's in a Smoothness Constant? Tighter Rates for Local SGD |
| 22 | [[2607.14737]] | GeoDetect: Geometric Adversarial Detection for VLPs |
| 23 | [[2607.14760]] | Clean-Reference Streaming Detection of Lens Occlusion |
| 24 | [[2607.14777]] | SEED: Self-Evolving On-Policy Distillation for Agentic RL |
| 25 | [[2607.14791]] | Transcoders for Investigating Deception in Language Models |
| 26 | [[2607.14817]] | Evaluating Epistemic Uncertainty Beyond OOD Detection and Active Learning |
| 27 | [[2607.14826]] | Interventional Causal Circuits for Safe Robot Action Testing |
| 28 | [[2607.14862]] | Tamed Stochastic Gradient Hamiltonian Monte Carlo |
| 29 | [[2607.14877]] | PAC Learning in Turn-Based Stochastic Games with Reachability Objectives |
| 30 | [[2607.14889]] | Analytical Study of the Optimal Combination of Binary Classifiers |
| 31 | [[2607.14890]] | Proof-or-Stop: Don't Trust the Agent, Trust the Evidence |
| 32 | [[2607.14943]] | Steering Robustness into World Action Models via Mechanistic Interpretability |
| 33 | [[2607.14947]] | Optimal Self-Distillation for Rectified Flow via Linear Probing |
| 34 | [[2607.14952]] | LongStraw: Long-Context RL Beyond 2M Tokens under a Fixed GPU Budget |
| 35 | [[2607.14967]] | Latent Trajectory Discrimination for AI-Generated Text Detection |
| 36 | [[2607.15001]] | LQCDMaster: Agentic Scientific Computing for Lattice QCD |
| 37 | [[2607.15003]] | SMC-ES: Automated Synthesis of Formally Verified Control Policies |
| 38 | [[2607.15067]] | Kernel Weighted Importance Sampling for Off-Policy Evaluation |
| 39 | [[2607.15079]] | BrainPilot: Automating Brain Discovery with Agentic Research |
| 40 | [[2607.15080]] | Evaluating Covariate Balance for Long-Horizon MDPs |
| 41 | [[2607.15084]] | Quantifying Training Membership Information in Hyperspherical Embeddings |
| 42 | [[2607.15105]] | Long-Context Fine-Tuning with Limited VRAM |
| 43 | [[2607.15164]] | The Industrialization of Research: On AI-Driven Science |
| 44 | [[2607.15175]] | Linear Representations of Grammaticality in Neural Language Models |
| 45 | [[2607.15190]] | Can We Trust Item Response Theory for AI Evaluation? |
| 46 | [[2607.15196]] | Subjective Risk Decomposition: A New View for Uncertainty Quantification |
| 47 | [[2607.15208]] | Delocalization of Bias in Unadjusted Hamiltonian Monte Carlo |
| 48 | [[2607.15218]] | When Words Are Safe But Actions Kill: Probing Physical Danger |
| 49 | [[2607.15247]] | AutoSynthesis: An Agentic System for Automated Meta-Analysis |
| 50 | [[2607.15277]] | Partition, Prompt, Aggregate: Statistical Self-Consistency in Language Models |

---

## 计数校验 / Count Verification

- 概览中列出的论文数 / Papers listed in this overview: **50**
- 目录中 `.md` 文件数（扣除 overview.md）/ `.md` files in directory (excluding overview.md): **50**
- 状态 / Status: **匹配 / Match** ✓
