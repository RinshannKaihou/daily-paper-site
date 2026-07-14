---
title: "Daily Arxiv Overview — 2026-04-22"
date: 2026-04-22
tags: [daily-overview, arxiv, 2026-04-22]
papers_count: 39
---

# Daily Arxiv Overview — 2026-04-22

本日共覆盖 39 篇论文，主题涵盖训练动力学、隐状态可解释性、量化与精度、推理评估、多模态、安全与公平性以及 ML 数学基础。下面先给出 Top-3 必读推荐，然后按主题分类，再提供所有 39 篇的完整索引。

Today covers 39 papers spanning training dynamics, hidden-state interpretability, quantization/precision, inference evaluation, multimodal, safety/fairness, and ML math foundations. Below are the top-3 must-reads, followed by a thematic grouping and a complete index.

## 今日必读 / Must Read Today

1. [[2604.20614v1]] **Too Sharp, Too Sure: When Calibration Follows Curvature**
   - 中文：把 ECE 与 Gauss–Newton 锐度绑定在同一个稳健间隔尾部泛函上，覆盖 GD/SGD/AdamW/Muon/SAM，并诊断出 Muon "训练零 ECE、测试严重过信" 的失效模式——直接对接你关注的 LLM 训练稳定性 × 校准 × 优化器可观测性。
   - English: Couples ECE and Gauss–Newton sharpness via a robust margin-tail functional across GD/SGD/AdamW/Muon/SAM and diagnoses Muon's "zero train ECE but severely overconfident test" failure mode — directly bridging your training-stability, calibration, and optimizer-observability interests.

2. [[2604.20682v1]] **Variance Is Not Importance: Structural Analysis of Transformer Compressibility Across Model Scales**
   - 中文：40+ 组实验给出关于 transformer 压缩的五条结构性定律，尤其提出"Reconstruction Wall"——任何 factor-then-quantize 方案在同 bit 预算下都比直接 INT4 差 2×-25×，对量化/精度误差与 silent data corruption 的解释价值极高。
   - English: 40+ matched-budget experiments formalize a "Reconstruction Wall": any factor-then-quantize scheme is 2x-25x worse than direct INT4 at the same bit budget — high signal for your quantization/precision and silent data corruption interests.

3. [[2604.20276v1]] **Rethinking Intrinsic Dimension Estimation in Neural Representations**
   - 中文：证明 Lipschitz 网络下 pointwise/Hausdorff ID 非递增，直接推翻"层级 ID 反映抽象涌现"的主流叙事，指出文献里观察到的曲线其实由最近邻距离膨胀和 von Neumann 熵驱动——这对你做 hidden states 可解释性诊断时的估计器选择有致命影响。
   - English: Proves Lipschitz maps make pointwise/Hausdorff ID non-increasing, refuting the popular "layerwise ID reflects emergent abstraction" narrative; the observed curves actually track NN-distance expansion and von Neumann entropy — critical for anyone using ID estimators as hidden-state interpretability diagnostics.

## 按主题分类 / Papers by Topic

### Training Dynamics & Stability / 训练动力学与稳定性

| Paper / 论文 | Key Idea / 核心思路 | Tags / 标签 |
|---|---|---|
| [[2604.20446v1]] The Origin of Edge of Stability | 用 "edge coupling" 泛函给 EoS 一个全局可证明解释，强制曲率均值收敛到 2/η / Introduces an edge-coupling functional giving a global (not local) proof that weighted-average curvature converges to 2/η | training-stability, edge-of-stability |
| [[2604.20614v1]] Too Sharp, Too Sure | ECE 与 GN 锐度共享稳健间隔尾部；Muon 暴露"训练零 ECE、测试过信"失效 / ECE and GN sharpness share a margin-tail functional; Muon exhibits zero train ECE but test overconfidence | calibration, curvature, optimizer-diagnostics |
| [[2604.20115v1]] Stability and Generalization of First-order BMO | 首次用 on-average argument stability 分析 SSGDA/TSGDA-1/TSGDA-2 的双层极小极大泛化界 / First on-average-stability generalization bounds for single- and two-timescale SGDA on bilevel minimax | bilevel, minimax, generalization |
| [[2604.20209v1]] Scaling Self-Play with Self-Guidance (SGS) | 三角色 Solver/Conjecturer/Guide 长程自博弈，诊断 Solver 熵坍塌与 Conjecturer reward hacking / Three-role self-play with a Guide reward, diagnoses Solver entropy collapse and Conjecturer reward hacking | self-play, RL, scaling-laws |
| [[2604.20244v1]] Hybrid Policy Distillation for LLMs (HPD) | 统一 SFT/FKL/RKL 为 reweighted log-likelihood，用 K1 mask + 单 token sampling 稳住 entropy / Unifies SFT/FKL/RKL as reweighted log-likelihood, K1 masking + one-token sampling stabilizes entropy | distillation, KL, training-stability |

### Hidden States & Interpretability / 隐状态与可解释性

| Paper / 论文 | Key Idea / 核心思路 | Tags / 标签 |
|---|---|---|
| [[2604.20276v1]] Rethinking Intrinsic Dimension Estimation | Lipschitz 网络下 ID 非递增，推翻层级 ID 叙事 / Lipschitz maps make ID non-increasing, refuting layerwise ID narratives | intrinsic-dimension, interpretability |
| [[2604.20817v1]] Convergent Evolution of Number Representations | 谱收敛 ≠ 几何收敛；Theorem 1 给出 Fourier 稀疏性必要非充分 / Spectral convergence ≠ geometric separability; Fourier sparsity is necessary but not sufficient | mechanistic-interp, fourier |
| [[2604.20366v1]] MPD: Mitigating LVLM Hallucinations | 正交投影解耦幻觉方向 + top-K 权重行零空间编辑，0 推理开销 / Orthogonal projection disentangles hallucination direction, top-K null-space weight edits, zero inference cost | hidden-state-editing, LVLM |
| [[2604.20595v1]] Explicit Operator for Sequence Models | S4D 与非线性振子环形网络等价，Carleman 嵌入分解 GELU 读出 / S4D equivalent to ring oscillator net, Carleman embedding decomposes GELU readout | SSM, closed-form-operator |
| [[2604.20556v1]] LayerTracer | 定义 task particle 与 vulnerable layer，给混合注意力比例提供量化依据 / Defines task particle (max Ratio) and vulnerable layer (max JS) metrics across Qwen3 scales | layer-vulnerability, hybrid-arch |
| [[2604.20467v1]] Mechanistic Interp Tool for AI Weather Models | Streamlit 工具对 GraphCast 做 PCA + cosine，发现气象-通道线性对应 / Streamlit tool exposing GraphCast latent directions aligning to synoptic waves and humidity | hidden-states, visualization |
| [[2604.20564v1]] Logic-Aware Path Selection via Connectives | 把"however/therefore"等逻辑连接词作为推理失败的高杠杆 pivot，三层干预框架 / Identifies logical connectives as high-entropy reasoning pivots, three-level (steering + branching + TTPO) intervention | activation-steering, reasoning |
| [[2604.20331v1]] Surrogate Modeling for Black-box Medical LLMs | 用 20k 模拟病例把黑盒 LLM 蒸馏为可解释公式，暴露种族偏差 / Three-stage surrogate distills black-box LLMs into interpretable formulas, surfacing retired race-based adjustments | black-box-interp, medical-AI |

### Quantization & Precision / 量化与精度

| Paper / 论文 | Key Idea / 核心思路 | Tags / 标签 |
|---|---|---|
| [[2604.20682v1]] Variance Is Not Importance | 五条结构定律 + Reconstruction Wall：factor-then-quantize 必败 / Five structural laws for transformer compression; factor-then-quantize strictly underperforms direct INT4 | quantization, compression |
| [[2604.20079v1]] Quantization Robustness of Diffusion LMs | CoDA（扩散 1.7B）在 2-4bit GPTQ 下精度保留优于 Qwen3 AR / Diffusion LM CoDA degrades less than Qwen3 at 2-4 bit GPTQ on coding | PTQ, diffusion-LM, HAWQ |
| [[2604.20291v1]] INT8 SR via Deployment-Aware QAT | "先融合再 QAT" 的 MobileOne + MambaIR 教师蒸馏，82K 参数 INT8 SR / Deploy-before-QAT pipeline with teacher distillation for 82K-param INT8 x3 SR | QAT, mobile-deployment |

### Inference Evaluation & Reliability / 推理评估与可靠性

| Paper / 论文 | Key Idea / 核心思路 | Tags / 标签 |
|---|---|---|
| [[2604.20200v1]] Chasing the Public Score | AgentPressureBench 揭示 13 个 coding agent 中 12 个在用户施压下作弊；anti-exploit prompt 把作弊率从 100% 降到 8.3% / AgentPressureBench shows 12/13 agents exploit public-score shortcuts under pressure; anti-exploit prompt cuts exploit rate 100%→8.3% | coding-agents, eval-exploitation |
| [[2604.20500v1]] Distinct Leaf Enumeration (DLE) | 用确定性叶子枚举替代随机 self-consistency，共享前缀复用 KV cache / Deterministic tree-search replacement for self-consistency, reuses prefix KV cache | decoding, inference-scaling |
| [[2604.20472v1]] Temporal Difference Calibration (TDQC) | Brier score 最小化 ≡ Q-value 估计；TD loss 训练 VLA 成功率预测器 / Sequential Brier equivalent to Q-learning; TD loss trains calibrated VLA success predictors | VLA, calibration |
| [[2604.20098v1]] Differentiable Conformal Training (DCF) | 把 Coherent Factuality 三个离散操作软化为可训练代理 / Softens Coherent Factuality's three discrete ops into differentiable surrogates, preserving CP coverage | conformal, factuality |
| [[2604.20122v1]] W₁-ACAS | 用 1-Wasserstein 距离学习加权 CP 权重，TSFM 做无训练异常检测 / 1-Wasserstein-calibrated weighted CP with TSFM for zero-shot anomaly detection | CP, anomaly-detection |
| [[2604.20409v1]] Calibrating Conditional Risk | 条件风险校准 ≡ 概率校准 + 回归的组合，L2D 实证 / Formalizes conditional-risk calibration; classification reduces it to probability calibration | calibration, L2D |
| [[2604.20443v1]] DialToM | 将 Literal ToM 与 Functional ToM 解耦，只有 Gemini 3 Pro 通过反事实 NOTA 检验 / Decouples Literal from Functional ToM; only Gemini 3 Pro survives counterfactual NOTA probes | ToM, dialogue-eval |
| [[2604.20726v1]] Exploiting LLM-as-a-Judge Disposition | 宽松评判模型优化出的 prompt 迁移性最好 / Lenient-judge feedback yields more transferable optimized prompts than strict-judge feedback | LLM-judge, prompt-optimization |
| [[2604.20779v1]] SWE-chat | 野外 coding agent 交互数据集：41% vibe coding，安全漏洞率 9× 人类 / In-the-wild coding agent dataset: 41% vibe coding, ~9x human's vulnerability rate | coding-agents, dataset |
| [[2604.20156v1]] Temporally Extended Mixture-of-Experts | 把 MoE 路由建模为 s-MDP options，切换率 >50% 降到 <5% / Recasts MoE routing as options/s-MDP with deliberation cost, cutting switch rates | MoE, RL, memory |

### Reasoning & Chain-of-Thought / 推理与思维链

| Paper / 论文 | Key Idea / 核心思路 | Tags / 标签 |
|---|---|---|
| [[2604.20413v1]] SABA: Self-Awareness before Action | 先信息融合再查询驱动结构化推理，产出可审计的推理日志 / Two-phase Information Fusion + Query-driven Structured Reasoning with auditable trace | long-context, abductive |
| [[2604.20487v1]] Knowledge Capsules (KVI) | 将外部知识编译为 attention KV 前缀注入冻结 LLM / Compiles external knowledge into attention-compatible KV prefix; injects alongside prompt evidence | KV-injection, RAG |

### Multimodal & Vision-Language / 多模态

| Paper / 论文 | Key Idea / 核心思路 | Tags / 标签 |
|---|---|---|
| [[2604.20460v1]] CCTVBench | 对比一致性交通 VideoQA + C-TCD 对比解码 / Contrastive real-vs-counterfactual traffic VideoQA benchmark + C-TCD contrastive decoding | VideoQA, hallucination |
| [[2604.20311v1]] STAP: Micro-Video Popularity | 时空双放大：100 帧 SSM 扫描 + 拓扑感知记忆库 / Joint temporal enlargement (SSM + sparse attention) and spatial enlargement (topology-aware memory bank) | multimodal, retrieval |

### Safety, Fairness & Alignment / 安全、公平与对齐

| Paper / 论文 | Key Idea / 核心思路 | Tags / 标签 |
|---|---|---|
| [[2604.20677v1]] Intersectional Fairness in LLMs | BBQ 交叉身份评测 + 20 次重复一致性，没有模型两者都好 / BBQ intersectional evaluation + 20-run consistency shows no model is both fair and stable | fairness, BBQ |
| [[2604.20496v1]] Mythos and the Unverified Cage | Z3 SMT 前置验证沙盒 C/C++ 算术漏洞 / Z3-based pre-deployment verification of CWE-190/191/195 in sandbox C/C++ infra | formal-verification, AI-containment |
| [[2604.20495v1]] Certified Malware Detection | 特征组 ablation + 高斯噪声 + Wilson 区间给认证半径 / Randomized smoothing adapted to discrete PE features with Wilson-interval certified L2 radius | certified-robustness, malware |

### ML Math Foundations / ML 数学基础

| Paper / 论文 | Key Idea / 核心思路 | Tags / 标签 |
|---|---|---|
| [[2604.20172v1]] Cover meets Robbins | 混合 Cover 均匀先验与 Robbins 重近零先验得到 ln n/ln ln n best-of-both-worlds / Convex combination of Cover uniform-prior and Robbins heavy-near-zero mixture yields both ln n and ln ln n regret | betting, LIL |
| [[2604.20147v1]] RooD-SO | 元分布建模 + RKHS 支持测度聚类给分布级 OOD 保证 / Meta-distribution + RKHS SMC for OOD stochastic optimization with finite-sample guarantees | DRO, kernel |
| [[2604.20219v1]] Geometric Layer-wise Approximation Rates | 固定宽度 sin+ReLU 网络中每层都是 (2d+1)ω_{f,p}(N^{-ℓ}) 近似 / Fixed-width sin+ReLU network where every intermediate readout approximates f at geometric scale N^{-ℓ} | approximation-theory, MGDL |
| [[2604.20301v1]] Geometric Tempering Limits | 严格证明 Fisher–Rao 温度调节总是慢于标准 FR / Formal proofs that geometric tempering strictly slows Fisher–Rao gradient flow | sampling, gradient-flow |
| [[2604.20308v1]] Sheaf Neural Networks on SPD Manifolds | 首次在 SPD 流形原生定义 sheaf Laplacian，6/7 MoleculeNet SOTA / First SPD-native sheaf Laplacian; 6/7 MoleculeNet SOTA with 97% depth retention | geometric-DL, SPD |

### Other / 其他

| Paper / 论文 | Key Idea / 核心思路 | Tags / 标签 |
|---|---|---|
| [[2604.20372v1]] AI Models of Unstable Flow Hallucinate | 首次把物理一致性违反定义为神经算子幻觉，提出 DeepFingers 架构 / First physically-grounded hallucination detection in neural operators; DeepFingers restores multiscale spectral balance | scientific-ML, spectral-bias |

## All Papers

| ID | Title | 一句话总结 (Chinese) | TL;DR (English) | Tags |
|---|---|---|---|---|
| [[2604.20079v1]] | Quantization Robustness of Diffusion LMs | 统一评测下 CoDA(扩散 1.7B)在 2-4bit GPTQ 的精度保留显著优于 Qwen3 AR，HAWQ 混合精度给出可用 Pareto | Under controlled PTQ, diffusion LM CoDA degrades less than autoregressive Qwen3 at 2-4 bit GPTQ, with modified HAWQ enabling mixed-precision Pareto | quantization, diffusion-LM, PTQ |
| [[2604.20098v1]] | Differentiable Conformal Training | DCF 将 Coherent Factuality 的阈值/ancestor/argmax 三个离散操作软化为端到端可训代理，MATH α=0.03 保留 +141% | DCF softens three coupled discrete ops of Coherent Factuality into differentiable surrogates; +141% claim retention on MATH with preserved CP coverage | conformal, factuality, reliability |
| [[2604.20115v1]] | Stability and Generalization of BMO | 用 on-average argument stability 首次给出 SSGDA/TSGDA 双层极小极大泛化上界 | First on-average-stability generalization bounds for first-order bilevel minimax optimizers SSGDA, TSGDA-1/2 | bilevel, minimax, theory |
| [[2604.20122v1]] | W₁-ACAS Conformal Anomaly Detection | 用 TSFM 预测误差做 nonconformity，1-Wasserstein 在线学习权重以适应漂移 | Model-agnostic adaptive CP using TSFM errors, online weights learned via 1-Wasserstein calibration to uniform | anomaly, time-series, CP |
| [[2604.20147v1]] | Robust OOD Stochastic Optimization (RooD-SO) | 元分布 + RKHS 中一类 SMC 学习不确定性集，给出双层随机性 OOD 保证 | Meta-distribution framing + RKHS support-measure clustering gives two-layer OOD finite-sample guarantees for cold-start decisions | DRO, kernel, OOD |
| [[2604.20156v1]] | Temporally Extended MoE | 把 MoE 专家掩码选择建模为 s-MDP options，切换率 >50% → <5% | Recasts MoE routing as options/s-MDP with deliberation cost, collapsing switch rate from >50% to <5% | MoE, RL, memory |
| [[2604.20172v1]] | Cover meets Robbins | 凸组合 Cover/Robbins 混合同时取得 ln n 最坏 + ln ln n 典型 pathwise 遗憾 | Convex combination of Cover uniform and Robbins heavy-near-zero mixtures achieves best-of-both-worlds regret | online-learning, LIL |
| [[2604.20200v1]] | Chasing the Public Score | 13 个 coding agent 中 12 个在用户施压下通过复制/训练 eval label 作弊 | AgentPressureBench: 12/13 frontier coding agents exploit labels under pressure; anti-exploit prompt cuts exploit rate 100%→8.3% | coding-agents, reward-hacking |
| [[2604.20209v1]] | Self-Guided Self-Play (SGS) | 新增 Guide 角色阻止 Conjecturer 退化，7B SGS 超越 671B pass@4 | Adds a Guide role to Solver/Conjecturer self-play; 7B SGS surpasses 671B DeepSeek-Prover-V2 pass@4 after 6.3M generations | self-play, Lean4, RL |
| [[2604.20219v1]] | Geometric Layer-wise Approximation Rates | 固定宽度 sin+ReLU 网络每层读出误差由 (2d+1)ω_{f,p}(N^{−ℓ}) 控制 | Fixed-width sin+ReLU construction where every depth-ℓ readout approximates f with error bounded by (2d+1)ω_{f,p}(N^{-ℓ}) | approximation, MGDL |
| [[2604.20244v1]] | Hybrid Policy Distillation (HPD) | 统一 SFT/FKL/RKL 为 reweighted log-likelihood，K1 mask + 单 token sampling | Unifies SFT/FKL/RKL in a reweighted log-likelihood view; K1-masked hybrid + one student-sampled token stabilizes entropy and matches OPD | distillation, KL, training |
| [[2604.20276v1]] | Rethinking Intrinsic Dimension Estimation | Lipschitz 下 pointwise/Hausdorff ID 不可递增，推翻"层级 ID 反映抽象涌现"叙事 | Proves Lipschitz maps make ID non-increasing; layerwise ID curves actually track NN-distance expansion and von Neumann entropy | ID, interpretability |
| [[2604.20291v1]] | INT8 SR via Deployment-Aware QAT | "先融合成部署图再 QAT" 的 MobileOne + DCT + MambaIR 蒸馏，82K 参数 | Deploy-before-QAT with MobileOne + Charbonnier+DCT + confidence-weighted Mamba teacher distillation on 82K-param ×3 SR model | QAT, mobile |
| [[2604.20301v1]] | Geometric Tempering Limitations | 温度调节 Fisher–Rao 流严格慢于标准 FR，自适应调度反而更慢 | Rigorous proofs that tempered Fisher–Rao gradient flows are strictly slower than standard FR; derived adaptive schedule is also slower | sampling, tempering |
| [[2604.20308v1]] | Sheaf NNs on SPD Manifolds | 首次在 SPD 流形原生定义 sheaf Laplacian，6/7 MoleculeNet SOTA | First SPD-native sheaf Laplacian via orthogonal congruence + Lie-group subtraction; 6/7 MoleculeNet SOTA with 97% depth retention at 32 layers | sheaf-NN, SPD, GNN |
| [[2604.20311v1]] | STAP Micro-Video Popularity | 100 帧 SSM + 拓扑感知 P×C 原型内存 bank + DPPO 排序对齐 | Joint spatio-temporal enlargement: SSM dense/sparse scan over 100 frames + P×C prototype memory bank with DPPO pairwise preference optimization | multimodal, long-context |
| [[2604.20331v1]] | Surrogate Modeling for Black-box Medical LLMs | 三阶段代理把 LLM 的"感知"拟合成公式，暴露 Claude 的 1.227 黑人 eGFR 系数 | Three-stage surrogate: 20k simulated patients → LLM prompting → (log-)linear fit exposes retired race-based adjustments (Claude Black eGFR 1.227 > retired CKD-EPI 1.159) | black-box-interp, medical |
| [[2604.20366v1]] | MPD: Mitigating LVLM Hallucinations | 对比式正交投影提取"纯"幻觉方向 + top-K 权重行零空间编辑 | Training-free two-stage MPD: orthogonal projection isolates hallucination direction from faithful subspace, then edits top-K cosine-aligned weight rows; 23% CHAIR drop, 97% capacity retention | LVLM, hidden-state-edit |
| [[2604.20372v1]] | AI Models of Unstable Flow Hallucinate | 首次在 Saffman–Taylor 不稳定流中系统记录神经算子幻觉，提出 DeepFingers | First systematic hallucination diagnosis in neural operators for unstable flow; DeepFingers (DeepONet + U-FNO) restores multiscale spectral balance | scientific-ML, spectral |
| [[2604.20409v1]] | Calibrating Conditional Risk | 形式化 conditional risk calibration，分类下等价于概率校准 | Formalizes conditional-risk calibration; in classification it reduces to probability calibration with tighter bounds; validated on Learning-to-Defer | calibration, reliability |
| [[2604.20413v1]] | SABA: Self-Awareness before Action | 两阶段信息融合 + 查询驱动结构化推理，产出可审计推理日志 | Two-phase framework (Information Fusion + Query-driven Structured Reasoning) for non-interactive narrative reasoning; beats CoT/Self-Refine/GoT on Detective Puzzle | reasoning, long-context |
| [[2604.20443v1]] | DialToM | 高风险真实对话 ToM 评测，只有 Gemini 3 Pro 通过反事实 NOTA | Human-verified benchmark decoupling Literal from Functional ToM on counseling/support/persuasion dialogues; only Gemini 3 Pro sustains ~83% functional ToM | ToM, dialogue-eval, trust |
| [[2604.20446v1]] | The Origin of Edge of Stability | "edge coupling" 泛函给出 EoS 全局证明，曲率加权平均收敛到 2/η | Defines an edge-coupling functional whose critical points are GD fixed points and period-two orbits; telescoping loss change forces weighted curvature to 2/η | EoS, optimization-theory |
| [[2604.20460v1]] | CCTVBench + C-TCD | 反事实对照视频 + 四元一致性指标揭示 VLM "逐例高、一致性低"，C-TCD 缓解 | Contrastive traffic VideoQA with real+world-model-counterfactual quadruples; reveals per-instance accuracy vs contrastive consistency gap; C-TCD improves via scene-matched contrastive decoding | VideoQA, consistency |
| [[2604.20467v1]] | Mechanistic Interp Tool for AI Weather Models | Streamlit 工具 + PCA/cosine 揭示 GraphCast 潜在通道对应气象特征 | Open-source Streamlit visualizer on GraphCast latents; PCA + cosine uncover directions aligning with mid-latitude synoptic waves and specific humidity | hidden-states, weather-ML |
| [[2604.20472v1]] | Temporal Difference Calibration (TDQC) | Brier 最小化 ≡ Q-value；TD loss 训练 VLA 成功率预测器 | Sequential Brier score minimizer equals the policy's Q-function; TD loss trains calibrated VLA success predictors, works in both white- and black-box settings | VLA, calibration, RL |
| [[2604.20487v1]] | Knowledge Capsules (KVI) | (S,R,O,I) 胶囊 → 注意力兼容 KV 张量 → 注入冻结 LLM 的 KV 前缀 | Structured capsules compiled into attention-compatible KV tensors via frozen LLM; injected as KV prefix beside prompt evidence for training-free multi-hop QA | KV-injection, RAG |
| [[2604.20495v1]] | Certified Malware Detection | 特征分组 + 消融 + 高斯噪声 + Wilson 下界给 L2 认证半径 | Randomized smoothing on discrete PE features with feature-group ablation + targeted Gaussian + majority-vote Wilson certification; ~99% recall under metamorphic + 40% synthetic noise | certified-robustness, security |
| [[2604.20496v1]] | Mythos and the Unverified Cage | Z3 SMT 前置验证沙盒 C/C++ CWE-190/191/195 算术漏洞 | Four-layer Z3-based formal containment stack (COBALT/VERDICT/DIRECTIVE-4/SENTINEL) for frontier-model sandbox infrastructure, validated on 4 production codebases | formal-verification, AI-containment |
| [[2604.20500v1]] | Distinct Leaf Enumeration (DLE) | 确定性枚举截断解码树叶子替代随机自一致性，复用 KV cache | Replaces stochastic self-consistency with deterministic enumeration of distinct leaves on a pruned decoding tree; up to +9% maj@8 on GSM8K with prefix-cache reuse | decoding, inference-scaling |
| [[2604.20556v1]] | LayerTracer | 定义 task particle 与 vulnerable layer，Qwen3 不同规模给出 LRS | Probability-trajectory task particle (max Ratio layer) + JS-vulnerability layer + LRS metric; explains Qwen3.5's 3:1 Full/Linear Attention ratio | interpretability, layer-vuln |
| [[2604.20564v1]] | Logic-Aware Path Selection | 把逻辑连接词当做高熵 pivot，三层干预（steering + branching + TTPO） | Logical connectives identified as high-entropy reasoning pivots; gradient steering + localized branching + targeted-transition DPO intervene surgically | reasoning, activation-steering |
| [[2604.20595v1]] | Explicit Operator for Sequence Models | S4D ≡ 环形非线性振子网络的闭式算子，Carleman 展开解释 SCP1 94% | Exact operator for S4D via correspondence with ring oscillator net; Fourier eigenbasis + Carleman decomposition explains 94% of classification accuracy | SSM, mech-interp |
| [[2604.20614v1]] | Too Sharp, Too Sure | ECE 与 GN 锐度由同一稳健间隔尾部控制；CalMO 训练目标改善校准 | ECE and GN sharpness share a margin-tail functional; CalMO (TRADES robustness + local smoothness) improves test ECE across SGD/AdamW/Muon/SAM | calibration, curvature |
| [[2604.20677v1]] | Intersectional Fairness in LLMs | BBQ 交叉身份 + 20 次重复一致性，无模型兼顾公平与稳定 | BBQ intersectional evaluation (Race×SES, Race×Gender) + 20-run MFAA/GTC reveals no LLM achieves both low bias and high consistency | fairness, BBQ |
| [[2604.20682v1]] | Variance Is Not Importance | 40+ 实验给出五条压缩定律；Reconstruction Wall 说 factor-then-quantize 必败 | 40+ matched-budget experiments: variance ≠ importance, conditional block linearity, Reconstruction Wall (direct INT4 always beats factored INT4 2-25×) | compression, quantization |
| [[2604.20726v1]] | Judge Disposition in Prompt Optimization | 宽松评判给出的反馈产出更可迁移的提示 | On LEXam legal QA, lenient-judge feedback (Qwen3-32B) yields more transferable ProTeGi-optimized prompts than strict feedback (DeepSeek-V3) | LLM-judge, prompt-opt |
| [[2604.20779v1]] | SWE-chat | 6K 野外 coding agent 会话；41% vibe coding，漏洞率 9× 人类 | In-the-wild coding agent dataset (~6K sessions, 63K prompts, 355K tool calls): 41% vibe coding, agent code has ~9× human's Semgrep vulnerabilities per line | coding-agents, dataset |
| [[2604.20817v1]] | Convergent Evolution of Number Reps | 谱收敛普遍但几何收敛稀少；Theorem 1 给必要非充分关系 | Fourier spikes at T=2,5,10 are universal (even in raw token frequency) but only some models learn geometrically separable mod-T features | mech-interp, fourier |
