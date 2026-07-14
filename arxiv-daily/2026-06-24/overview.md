---
title: "Daily Paper Overview — 2026-06-24"
date: 2026-06-24
tags:
  - daily-overview
  - arxiv
  - LLM
  - reasoning
  - quantization
  - agents
  - statistical-methods
  - safe-control
papers: 29
---

# Daily Paper Overview — 2026-06-24

> 29 篇论文，横跨 LLM 推理、量化压缩、智能体评测、统计方法、安全控制与高效计算。Today's batch of 29 papers spans LLM reasoning, quantization/compression, agent evaluation, statistical methodology, safe control, and efficient computing.

---

## 今日必读 / Must Read Today

### 1. [[2606.25519]] — Quantization Inflates Reasoning (Token Inflation as a Hidden Cost of Low-Bit Reasoning Models)

- **理由 (中):** 揭示了一个被标准量化评测掩盖的真实代价——低比特量化会让推理模型即使保持答案正确率也生成明显更长的思维链，并提出 CTIR 度量这一隐藏测试时开销，证明它直接侵蚀量化的每 token 加速。
- **Reason (EN):** Exposes a hidden cost that standard quantization evals miss — low-bit quantization makes reasoning models emit substantially longer chains-of-thought even when accuracy holds — and introduces the CTIR metric showing this inflation erodes the per-token speedup that quantization is supposed to deliver.

### 2. [[2606.25524]] — Cliff Tokens (Single-Token Failure Triggers in LLM Mathematical Reasoning)

- **理由 (中):** 提出"悬崖 token"概念精确定位推理轨迹中使到达正确答案概率坍缩的单个 token，并用统计检验识别；据此训练的 Cliff-DPO 仅用 ~3.3 万 loss token（比 cDPO 少 177 倍）即可获得 +6.6 的准确率提升，机制性洞察与方法效率俱佳。
- **Reason (EN):** Introduces the "cliff token" — the single token where the probability of reaching the correct answer collapses — and a statistically-grounded detector for it; the resulting Cliff-DPO training matches or beats cDPO using ~177× fewer loss tokens with up to +6.6 accuracy gain, combining genuine mechanistic insight with methodological efficiency.

### 3. [[2606.25819]] — ToolBench-X (Benchmarking Tool-Using Agents under Tool-Environment Unreliability)

- **理由 (中):** 重新定义了工具型智能体的鲁棒性评测——在 1106 个任务上注入五类可恢复可靠性危害，发现最强模型成功率仍低于 60%，并用 Hint/TTS/Oracle 对照实验干净地证明瓶颈是"危害诊断能力"而非算力或调用次数。
- **Reason (EN):** Reframes agent-robustness evaluation by injecting five recoverable reliability hazards into 1,106 tasks, finding no frontier model exceeds 60% success, and uses a clean Hint/TTS/Oracle ablation to show the bottleneck is hazard *diagnosis* — not compute or call volume — an actionable, well-supported conclusion.

---

## 按主题分类 / Papers by Topic

### 推理与可解释性 / Reasoning & Interpretability

| Paper | 主题与贡献 / Topic & Contribution |
|---|---|
| [[2606.25524]] Cliff Tokens | 识别推理轨迹中使正确率坍缩的单个 token 并据此训练高效 DPO。Identifies the single token where answer-probability collapses in a reasoning trace and uses it to train highly token-efficient DPO. |
| [[2606.25657]] Joint Sparse Autoencoders (JSAE) | 用跨模态稀疏自编码器对齐图像/文本隐码，实现可解释的视觉-语言双向 steering。Aligns sparse codes across vision/text with a paired cosine loss, enabling interpretable bidirectional steering of vision-language models. |
| [[2606.25459]] Probing Mandarin Sub-dialects | 无监督发音探针分析 wav2vec 2.0 在八种官话次方言上的表征，揭示北京话过拟合与层级化跨方言可解码性。Unsupervised articulatory probing of wav2vec 2.0 over eight Mandarin sub-dialects reveals Beijing-centric overfitting and a hierarchical cross-dialect decodability structure. |

### 大模型量化、压缩与高效推理 / LLM Quantization, Compression & Efficient Inference

| Paper | 主题与贡献 / Topic & Contribution |
|---|---|
| [[2606.25519]] Quantization Inflates Reasoning | 低比特量化让推理模型生成更长思维链(CTIR)，侵蚀加速收益。Low-bit quantization makes reasoning models generate longer chains-of-thought (CTIR), eroding the speedup. |
| [[2606.25532]] Agentic Compression Discovery | 以进化知识图谱为锚的多智能体引擎，自动设计硬件感知压缩算法，235B 模型部署双 A100。Evolutionary-knowledge-graph–anchored multi-agent engine auto-designs hardware-aware compression; deploys a 235B model on dual A100. |
| [[2606.25674]] BitNet Text Embeddings (BITEMBED) | 三值权重 LLM 嵌入编码器配合对比+蒸馏，在 MMTEB 接近全精度教师、CPU 吞吐 ~2×。Ternary-weight LLM embedding encoder with continual contrastive pre-training and distillation matches FP teachers on MMTEB at ~2× CPU throughput. |

### 高效计算与硬件 / Efficient Computing & Hardware

| Paper | 主题与贡献 / Topic & Contribution |
|---|---|
| [[2606.25426]] Above the Inner Loop (M1 AMX) | 手写 fp32 GEMM 在 Apple M1 AMX 上以"内循环之上"的工程杠杆超越 Accelerate 全部路径。Hand-tuned fp32 GEMM on Apple M1 AMX beats all Accelerate paths via "above-the-inner-loop" engineering levers, not faster inner loops. |
| [[2606.25453]] EmuGEMM | 用 INT8 Tensor Core 模拟 FP32/FP64 GEMM 的融合内核，Hopper 上 1639 Top/s。Fused-kernel library reconstructs FP32/FP64 GEMM from INT8 tensor-core ops, sustaining 1,639 Top/s on GH200. |
| [[2606.25562]] MSDF CNN FPGA Accelerator | MSDF 数字串行融合乘加 FPGA 卷积器，U-Net 上达 15.14 GOPS/W。MSDF digit-serial fused multiply-add FPGA convolver reaches 15.14 GOPS/W on a U-Net segmentation task. |

### 模型安全与对齐 / Model Safety & Alignment

| Paper | 主题与贡献 / Topic & Contribution |
|---|---|
| [[2606.25487]] Jailbreak Judge Reliability | 系统审计越狱评测判官，发现专用分类器与 LLM-judge 以相反方式失效。Audits jailbreak judges, finding dedicated classifiers and LLM-as-judges fail in opposite ways (low precision vs erratic recall). |
| [[2606.25750]] RAS (Refusal Alignment Score) | 白盒从隐藏状态测"拒绝方向"对齐度，比判官评测快 ~210×。White-box score from hidden-state alignment with a "refusal direction", ~210× faster than judge-based evaluation. |
| [[2606.25296]] SafeGen | LLM+形式化验证从设计文档自动生成功能安全断言并分级故障危害度。LLM + formal verification auto-generates functional-safety assertions and grades fault criticality from design documents. |

### 智能体、工具使用与评测 / Agents, Tool Use & Evaluation

| Paper | 主题与贡献 / Topic & Contribution |
|---|---|
| [[2606.25819]] ToolBench-X | 注入五类可恢复可靠性危害的工具使用基准，最强模型 <60%。Tool-use benchmark injecting five recoverable reliability hazards; best agent below 60% success. |
| [[2606.25605]] Constraint Tax in Open-Weight LLMs | 发现同时开启 Tool Calling 与 JSON Schema 约束会让多个开源模型停止调用工具(100%→0%)。Reproduces that enabling Tool Calling + JSON Schema constraints jointly makes multiple open-weight models stop calling tools (100%→0%). |
| [[2606.25760]] ARGUS (UQ for Computer-Use Agents) | 首个 GUI 点击定位的不确定性量化跨场景基准，揭示选择性迁移规律。First cross-regime uncertainty-quantification benchmark for GUI grounding, revealing a selective-transfer pattern. |
| [[2606.25402]] LibEvoBench | 多版本代码生成基准，揭示 LLM 对 API 版本基本无感。Multi-version code-generation benchmark showing LLMs are essentially version-oblivious to evolving APIs. |
| [[2606.25879]] AI-Assisted Reproducibility (FABRIC) | FABRIC + Claude/LoomAI 的"结论级"复现方法学，AI 提速 ~4–6×。FABRIC + Claude/LoomAI conclusion-level reproducibility methodology, ~4–6× faster at ~$34. |

### 强化学习与多智能体 / Reinforcement Learning & Multi-Agent

| Paper | 主题与贡献 / Topic & Contribution |
|---|---|
| [[2606.25335]] Stagnant Neuron (KNIFE) | 揭示 MARL 价值分解可塑性丧失源于停滞神经元，提出神经元级修复 KNIFE。Traces MARL value-factorization plasticity loss to "stagnant neurons"; proposes neuron-level KNIFE repair. |

### 安全控制与形式化验证 / Safe Control & Formal Verification

| Paper | 主题与贡献 / Topic & Contribution |
|---|---|
| [[2606.25366]] AMPLE-GNC | 可靠性非对称航天器 GNC 栈，学习模块外裹验证运行时安全盾。Reliability-asymmetric spacecraft GNC stack wrapping capable learned modules in a verified runtime shield. |
| [[2606.25371]] Conformal Recovery-Deadline Certificates | 用 split-conformal 上界给自适应控制器设恢复截止期限，解耦自主性与安全性。Uses a split-conformal upper bound as a recovery deadline for adapting controllers, decoupling autonomy from safety. |
| [[2606.25374]] Spacecraft FTC Honest Benchmark | 诚实航天器容错基准，证明"结构优于裸学习"，自校正观测器破 0% 硬墙。Honest spacecraft FTC benchmark showing structure beats raw learning; self-correcting observer breaks a 0% wall. |

### 统计方法、不确定性度量与概率模型 / Statistical Methods, Uncertainty & Probabilistic Models

| Paper | 主题与贡献 / Topic & Contribution |
|---|---|
| [[2606.25601]] Statistically Valid Hyperparameter Selection | 以 Learn-Then-Test 把超参选择重述为多重假设检验并给有限样本保证。Recasts hyperparameter selection as multiple hypothesis testing (LTT) with explicit finite-sample guarantees. |
| [[2606.25743]] Black-Box Assisted Regression | 把基础模型当黑箱先验的非参数回归极小化刻画与相变。Minimax characterization and phase transition for black-box-assisted nonparametric regression. |
| [[2606.25745]] MFVI Overestimates Predictive Variance | 指出"MFVI 低估方差"共识不完整，ID 测试点反而高估。Shows the "MFVI underestimates variance" picture is incomplete — it overestimates for in-distribution test points. |
| [[2606.25882]] Posterior Collapse in Deep GPs | 重新解释 PCA 先验均值与白化在深度 GP 训练中的真正机理。Re-explains the real mechanism behind the PCA prior mean and whitening in variational Deep GP training. |
| [[2606.25797]] Confidence Sequences for MDP-SMC | 用置信序列修复并加速 MDP 在线统计模型检验，平均省 50× 样本。Fixes and accelerates online statistical model checking of MDPs via confidence sequences, ~50× fewer samples. |

### 理论与表示学习 / Theory & Representation Learning

| Paper | 主题与贡献 / Topic & Contribution |
|---|---|
| [[2606.25269]] Task-Oriented Randomization | 自适应扰动输入以稳定黑箱输出的 noisification 框架，统一 bootstrap/子采样。Noisification framework stabilizing black-box outputs by adaptively perturbing inputs; unifies bootstrap/sub-sampling. |
| [[2606.25777]] Space-Efficient Language Generation in the Limit | 空间受限学习者在 DFA 类上的极限生成能力刻画。Characterizes space-bounded language generation in the limit over DFA classes. |
| [[2606.25821]] SARA (Semantically Anchored Routing Alignment) | 以高资源语言路由分布为锚对齐低资源 MoE 路由，提升多语能力。Aligns low-resource MoE routing to high-resource anchors via JS divergence, improving multilingual capability. |

---

## All Papers

| # | arxiv_id | Short Title | 一句话 / One-line |
|---|---|---|---|
| 1 | [[2606.25269]] | Stabilizing black-box via task-oriented randomization | 自适应扰动输入并集成以稳定黑箱输出，提供 (s,δ) 稳定性保证。Adaptively perturb inputs and ensemble to stabilize black-box outputs with (s,δ)-stability guarantees. |
| 2 | [[2606.25296]] | SafeGen | LLM+形式化验证从文档自动生成功能安全断言并分级故障。LLM + formal verification auto-generates functional-safety assertions and grades faults from documents. |
| 3 | [[2606.25335]] | Stagnant Neuron (KNIFE) | MARL 价值分解可塑性丧失源于停滞神经元，KNIFE 做神经元级修复。MARL value-factorization plasticity loss stems from stagnant neurons; KNIFE repairs them neuron-by-neuron. |
| 4 | [[2606.25366]] | AMPLE-GNC | 可靠性非对称航天器 GNC 栈，学习模块外包验证安全盾。Reliability-asymmetric spacecraft GNC stack wrapping learned modules in a verified shield. |
| 5 | [[2606.25371]] | Conformal Recovery-Deadline Certificates | conformal 上界设恢复截止期限，解耦自适应控制器的自主性与安全性。Conformal upper bound sets a recovery deadline, decoupling autonomy from safety for adapting controllers. |
| 6 | [[2606.25374]] | Spacecraft FTC Honest Benchmark | 诚实基准证明结构优于裸学习，自校正观测器破 0% 硬墙。Honest benchmark shows structure beats raw learning; self-correcting observer breaks a 0% wall. |
| 7 | [[2606.25402]] | LibEvoBench | 多版本代码生成基准，揭示 LLM 对 API 版本基本无感。Multi-version code-gen benchmark showing LLMs are essentially version-oblivious to APIs. |
| 8 | [[2606.25426]] | Above the Inner Loop (M1 AMX) | M1 AMX 上手写 fp32 GEMM 以内循环之上杠杆超越 Accelerate。Hand-tuned fp32 GEMM on M1 AMX beats Accelerate via above-the-inner-loop levers. |
| 9 | [[2606.25453]] | EmuGEMM | INT8 Tensor Core 模拟高精度 GEMM 的融合内核，Hopper 1639 Top/s。Fused kernels emulate high-precision GEMM via INT8 tensor cores, 1,639 Top/s on Hopper. |
| 10 | [[2606.25459]] | Probing Mandarin Sub-dialects | 无监督发音探针揭示 wav2vec 2.0 北京话过拟合与层级化跨方言结构。Unsupervised articulatory probing reveals wav2vec 2.0's Beijing-centric overfitting and hierarchical cross-dialect structure. |
| 11 | [[2606.25487]] | Jailbreak Judge Reliability | 审计越狱评测判官，专用分类器与 LLM-judge 以相反方式失效。Audits jailbreak judges; classifiers and LLM-judges fail in opposite ways. |
| 12 | [[2606.25519]] | Quantization Inflates Reasoning | 低比特量化使推理模型生成更长思维链(CTIR)，侵蚀加速。Low-bit quantization makes reasoning models emit longer CoT (CTIR), eroding speedup. |
| 13 | [[2606.25524]] | Cliff Tokens | 识别推理轨迹中使正确率坍缩的单 token 并训练高效 Cliff-DPO。Identifies the single token where answer-probability collapses and trains token-efficient Cliff-DPO. |
| 14 | [[2606.25532]] | Agentic Compression Discovery | 进化知识图谱多智能体自动设计硬件感知压缩，部署 235B 模型。Evolutionary-KG multi-agent engine auto-designs hardware-aware compression, deploys a 235B model. |
| 15 | [[2606.25562]] | MSDF CNN FPGA Accelerator | MSDF 数字串行融合乘加 FPGA 卷积器，U-Net 15.14 GOPS/W。MSDF digit-serial fused-multiply-add FPGA convolver, 15.14 GOPS/W on U-Net. |
| 16 | [[2606.25601]] | Statistically Valid Hyperparameter Selection | LTT 把超参选择重述为多重假设检验并给有限样本保证。LTT recasts hyperparameter selection as multiple hypothesis testing with finite-sample guarantees. |
| 17 | [[2606.25605]] | Constraint Tax in Open-Weight LLMs | 同时开 Tool Calling 与 JSON Schema 让多个开源模型停止调用工具(100%→0%)。Enabling Tool Calling + JSON Schema jointly stops multiple open-weight models calling tools (100%→0%). |
| 18 | [[2606.25657]] | Joint Sparse Autoencoders (JSAE) | 跨模态稀疏自编码器对齐图像/文本隐码，实现可解释 VLM steering。Cross-modal sparse autoencoders align image/text codes for interpretable VLM steering. |
| 19 | [[2606.25674]] | BitNet Text Embeddings (BITEMBED) | 三值权重 LLM 嵌入编码器，MMTEB 接近全精度、CPU 吞吐 ~2×。Ternary-weight LLM embedding encoder matches FP teachers on MMTEB at ~2× CPU throughput. |
| 20 | [[2606.25743]] | Black-Box Assisted Regression | 黑箱先验非参数回归的极小化刻画与相变，提出 Safe Residual Estimator。Minimax characterization and phase transition for black-box-prior regression; proposes Safe Residual Estimator. |
| 21 | [[2606.25745]] | MFVI Overestimates Predictive Variance | "MFVI 低估方差"不完整，ID 测试点反而高估并与冷后验效应关联。"MFVI underestimates variance" is incomplete; it overestimates for ID points and links to the Cold Posterior Effect. |
| 22 | [[2606.25750]] | RAS (Refusal Alignment Score) | 白盒从隐藏状态测拒绝方向对齐度，比判官评测快 ~210×。White-box score from hidden-state refusal-direction alignment, ~210× faster than judge evals. |
| 23 | [[2606.25760]] | ARGUS (UQ for Computer-Use Agents) | 首个 GUI 点击定位不确定性量化跨场景基准，揭示选择性迁移。First cross-regime UQ benchmark for GUI grounding, revealing selective transfer. |
| 24 | [[2606.25777]] | Space-Efficient Language Generation | 空间受限学习者在 DFA 类上的极限生成能力刻画。Characterizes space-bounded language generation in the limit over DFA classes. |
| 25 | [[2606.25797]] | Confidence Sequences for MDP-SMC | 置信序列修复并加速 MDP 在线统计模型检验，平均省 50× 样本。Confidence sequences fix and accelerate online MDP statistical model checking, ~50× fewer samples. |
| 26 | [[2606.25819]] | ToolBench-X | 注入五类可恢复危害的工具使用基准，最强模型 <60%，瓶颈在诊断。Tool-use benchmark injecting five recoverable hazards; best agent <60%, bottleneck is diagnosis. |
| 27 | [[2606.25821]] | SARA (Semantically Anchored Routing Alignment) | 以高资源路由分布为锚对齐低资源 MoE 路由，提升多语能力。Aligns low-resource MoE routing to high-resource anchors, improving multilingual capability. |
| 28 | [[2606.25879]] | AI-Assisted Reproducibility (FABRIC) | FABRIC + Claude/LoomAI 结论级复现方法学，AI 提速 ~4–6×。FABRIC + Claude/LoomAI conclusion-level reproducibility methodology, ~4–6× faster. |
| 29 | [[2606.25882]] | Posterior Collapse in Deep GPs | 重新解释 PCA 先验均值与白化在变分深度 GP 中的真正机理。Re-explains the real mechanism of the PCA prior mean and whitening in variational Deep GPs. |

---

## 统计核对 / Count Check

- 论文计数 / Paper count in this overview: **29**（与 2026-06-24 目录下 29 个论文 `.md` 文件一致 / matches the 29 paper `.md` files in the 2026-06-24 folder）。无偏差 / No mismatch.
