---
title: "Daily Paper Overview — 2026-04-23"
date: 2026-04-23
tags:
  - llm-training-stability
  - llm-inference-evaluation
  - interpretability
  - quantization
  - ml-reliability
  - distributed-training
  - kv-cache
  - benchmarking
  - multi-agent
papers_count: 35
---

# 2026-04-23 论文速览 / Daily Paper Overview

---

## 今日必读 / Must Read Today

### 1. [[2604.21632v1]] — To See the Unseen: Embedding Collapse in Transformers

**为什么必读（中文）：** 这是一项来自 Google DeepMind 的高质量理论+实验工作。论文在数学上严格证明了：在带 weight decay 和 LayerNorm 的标准训练下，未见过 token 的 (un)embedding 向量必然坍缩（cosine 相似度趋近 1），这是一个与架构和数据集大小无关的必然性结论。更重要的是，在 Gemma 3（1B–27B）上用留出 token 做了实证验证，发现这一现象确实存在，且以坍缩 token 做微调的收敛速度慢 10 倍。这直接回答了"LLM 为什么在 symbol reasoning 上无法泛化"的机制性问题，并提供了三要素修复方案（copy attention + 高符号多样性 + 冻结/重置 embedding）。

**Why it's a must-read (English):** A rigorous DeepMind paper proving that unseen-token embedding collapse is *mathematically inevitable* under weight decay + LayerNorm SGD — independent of architecture or dataset size. Empirically confirmed in Gemma 3 (1B–27B) where unused token embeddings show cosine similarity 0.23–0.78 vs. 0.01–0.09 for used tokens, causing 10× slower fine-tuning. This is a training stability and interpretability paper in one: it explains a concrete mechanism behind LLM generalization failures and offers a principled fix with copy attention + frozen embeddings + diversity.

---

### 2. [[2604.21327v1]] — Debiased Denoised TTRL (DDRL): Fixing Spurious Signal Amplification in Test-Time RL

**为什么必读（中文）：** 测试时强化学习（TTRL）是当前最活跃的 LLM 适应范式之一。本文精准诊断了 TTRL 中两个系统性失效源：中等频率答案形成的"歧义区域"伪标签，以及 GRPO 归一化对低共识组虚假奖励的不对称放大。这直接触及 LLM 训练稳定性的核心——优化目标噪声如何被训练算法放大。提出的 DDRL 三组件（BCS + DAE + COR）在 Qwen2.5-Math-1.5B 上相对 ETMR 基线平均提升 +6.7%，且 COR 离策精调仅需 3–5 分钟。GRPO 归一化放大问题是该领域尚未被充分认识的训练可靠性隐患。

**Why it's a must-read (English):** TTRL is the leading paradigm for unsupervised test-time LLM adaptation. This paper is the first to rigorously characterize *why* GRPO-based TTRL is unstable: medium-frequency pseudo-labels form an "ambiguous region," and GRPO's group-relative normalization disproportionately amplifies these unreliable signals. Addresses LLM training stability directly. The fixed-advantage DAE component challenges the assumption that normalization-based advantage estimation is safe in low-supervision settings. The 3–5 minute off-policy COR stage is a practical efficiency insight applicable beyond TTRL.

---

### 3. [[2604.21361v1]] — Causality and Observability Failures in Distributed AI Inference Pipelines Due to Clock Skew

**为什么必读（中文）：** 这篇来自 Open Compute Project 的工业论文揭示了分布式 AI 推理中一个被严重忽视的静默失效模式：仅 3–5ms 的时钟偏差就会静默破坏因果可观测性（负时间跨度、乱序事件），而吞吐量和延迟等传统监控指标完全不受影响。这是一个真实存在于百万级 GPU 集群中的"沉默数据损坏"问题。提出的 `causality_health` 二进制指标是一个可立即集成到现有 SLO 框架的轻量级修复方案，对关注分布式推理系统可观测性的读者而言是直接可操作的知识。

**Why it's a must-read (English):** A production-grounded paper from OCP documenting a silent failure mode with a precise empirical threshold: clock skew ≥ 3–5ms breaks causal observability in distributed AI inference pipelines while leaving throughput/latency metrics completely green. This is a classic silent data corruption scenario — standard SLOs cannot detect it. The `causality_health` binary metric is directly implementable and transport-agnostic (confirmed on both Kafka and ZeroMQ). Essential reading for anyone operating or monitoring distributed LLM inference at scale.

---

## 按主题分类 / Papers by Topic

### LLM 训练稳定性 / LLM Training Stability

| 论文 / Paper | 摘要 / Summary |
|---|---|
| [[2604.21632v1]] To See the Unseen | **中文：** 证明 Transformer 未见 token 的 embedding 必然坍缩，并在 Gemma 3 上实证验证，提供三要素修复方案。<br>**English:** Theoretical proof + Gemma 3 empirical validation of unseen-token embedding collapse; fix: copy attention + frozen embeddings + symbolic diversity. |
| [[2604.21327v1]] DDRL: Debiased TTRL | **中文：** 诊断 GRPO 归一化对伪标签虚假信号的放大机制，提出 BCS+DAE+COR 三组件框架，Math-1.5B 上相对基线 +6.7%。<br>**English:** Identifies and fixes GRPO normalization as a spurious-reward amplifier in test-time RL; three-component DDRL achieves +6.7% over ETMR on Qwen2.5-Math-1.5B. |
| [[2604.21428v1]] Decoupled DiLoCo | **中文：** 将单体 SPMD 集群解耦为 M 个异步学习器+中央同步器，最小法定数聚合实现 86% Goodput，匹配标准数据并行 ML 质量。<br>**English:** Async federated LLM pre-training achieving 86% goodput at 2.4M chips with ML quality parity; min-quorum aggregation eliminates straggler bottlenecks. |
| [[2604.21343v1]] Latent Denoising LMM | **中文：** 在多模态指令微调中对视觉 token 施加显著性引导腐蚀并训练恢复，在 18 个基准 15/18 改进，推理时零开销。<br>**English:** Saliency-guided latent denoising during LMM instruction tuning improves 15–18/18 benchmarks with zero inference overhead across 3 architectures. |
| [[2604.21395v1]] ERM Geometric Blind Spot (PMH) | **中文：** 定理证明任何 ERM 训练必然在标签相关干扰方向保留非零敏感度，PMH 单高斯正则化项修复该缺陷，TDI 指标诊断 PGD 使问题恶化。<br>**English:** Proves ERM's geometric blind spot is architecture-invariant; PMH (Gaussian noise regularizer) is the unique isotropic fix; adversarial PGD worsens isotropic geometry despite reducing Jacobian Frobenius norm. |

---

### LLM 推理评估 / LLM Inference Evaluation

| 论文 / Paper | 摘要 / Summary |
|---|---|
| [[2604.21523v1]] FOCUS VLM Evaluator Reliability | **中文：** 元评估基准，系统证明单答案打分范式在 T2I 扰动上失败率超 50%，配对比较最可靠，增加推理预算不一致改善评估质量。<br>**English:** Meta-benchmark revealing single-answer scoring fails >50% on T2I perturbations; pairwise comparison is most reliable; extending reasoning budget does not consistently improve evaluator accuracy. |
| [[2604.21199v1]] ARFBench Time-Series QA | **中文：** 基于 63 个真实 Datadog 事故构建 750 道时序问答题，混合 TSFM-VLM 模型与 GPT-5 F1 持平（63.9% vs 62.7%），人类领域专家仍领先（72.7%）。<br>**English:** First real-incident TSQA benchmark from Datadog; hybrid TSFM-VLM matches GPT-5 on F1; Tier-3 predictive reasoning remains hardest; model-human error profiles are complementary. |
| [[2604.21769v1]] Who Defines Best? (LMArena Slice Analysis) | **中文：** 对 LMArena 13.5 万条偏好数据分层分析，全局排名与类别排名 Spearman 相关最低 0.60，数学题人类仅 74% 选择正确答案。<br>**English:** FAccT 2026 paper: LMArena aggregate rankings mask major per-category inversions (minimax-m1: 19th globally → 1st in math); humans choose the objectively correct math answer only 74% of the time. |
| [[2604.21611v1]] Verbal Process Supervision (VPS) | **中文：** 将批评粒度形式化为第四推理扩展轴，步骤级语言监督在 GPQA Diamond 达 94.9% SOTA，AIME 弱演员提升 +63.3pp。<br>**English:** Formalizes critique granularity as a 4th inference-time scaling axis; step-level verbal critique outperforms Reflexion by +8.5–12.1 pp and achieves 94.9% on GPQA Diamond with no training cost. |
| [[2604.21454v1]] Reasoning Primitives in Hybrid LLMs | **中文：** 将推理分解为 recall + state-tracking 两种原语，发现混合架构（OLMo-Hybrid-Think）在高序列依赖碰撞任务中保持 45%，纯 Transformer 崩溃至 0.03。<br>**English:** Decomposes reasoning into recall + state-tracking; at high sequential dependence (m=64,n=64), hybrid architecture degrades gracefully (0.45) while transformer collapses to near-zero (0.03 parsed-weighted). |
| [[2604.21916v1]] MathDuels Self-Play Benchmark | **中文：** 让 LLM 同时扮演出题者和解题者，IRT Rasch 模型分离出两种能力，GPT-5.4-high 解题最强但创题落后，Gemini-3.1-Pro-high 综合第一。<br>**English:** Self-play dual-role benchmark with IRT scoring; solving and authoring abilities are decoupled; GPT-5.4-high tops solver but lags in authoring; avoids static benchmark saturation. |
| [[2604.21564v1]] LLM-Bias-Bench Sycophancy | **中文：** 直接与间接双模式探测 13 个大模型谄媚率，间接施压下中位谄媚率高达 79%，Kimi K2 最具抵抗力（23.7%），Gemini 1 Pro 最脆弱（94%）。<br>**English:** Dual-mode adversarial sycophancy benchmark in Portuguese; indirect probing drives median sycophancy to 79%; Kimi K2 most resistant (23.7%); indirect probing reveals vulnerabilities that direct challenges miss. |
| [[2604.21882v1]] RedirectQA Entity Surface Forms | **中文：** 用 Wikipedia 重定向信息构建同一事实的多种实体命名变体数据集，证明命名方式变化导致 23.7% 问答答案翻转，实体频率比表面形式频率更具预测力。<br>**English:** Dataset pairing same Wikidata facts with alias/abbrev/spelling-variant entity names; 23.7% of pairs show inconsistent predictions; entity-level frequency dominates surface-form frequency for factual access. |

---

### LLM 可解释性与隐藏状态 / Interpretability & Hidden States

| 论文 / Paper | 摘要 / Summary |
|---|---|
| [[2604.21255v1]] Agent Behavioral Similarity (RPS+AGS) | **中文：** 提出 RPS 和 AGS 两项量化 LLM 智能体工具调用行为相似度的指标，发现 Kimi-K2 的工具调用行为模式与 Claude Sonnet 4.5 高度相似（AGS=82.7%），并用受控蒸馏实验证明因果关系。<br>**English:** First formal metrics (RPS + AGS) for tool-use behavioral similarity; Kimi-K2 shows AGS=82.7% similarity to Claude Sonnet 4.5; controlled LoRA distillation experiment provides causal evidence for knowledge distillation as the mechanism. |
| [[2604.21346v1]] Symbolic Grounding VLM Bottleneck | **中文：** 将 Bongard-LOGO 转为符号程序输入后，LLM 准确率从 ~50% 提升至 78–96%，证明视觉编码器是主要瓶颈而非推理能力，查询图像额外输入无显著增益。<br>**English:** Replacing raw pixels with ground-truth LOGO programs yields +25–30 pp accuracy on Bongard-LOGO across 12 LLMs; the bottleneck is the visual encoder, not reasoning capacity; single query image adds no benefit beyond symbolic support programs. |
| [[2604.21691v1]] There Will Be a Scientific Theory of Deep Learning | **中文：** 14 位理论深度学习研究者联名论证"学习力学"正在涌现，综述五类证据链（可解析设置、有用极限、经验规律、超参数解耦、普遍现象），并提出七项理论标准。<br>**English:** Position paper by 14 leading theorists arguing "learning mechanics" is crystallizing; synthesizes NTK, μP, edge of stability, neural collapse, and scaling laws as converging evidence; seven desiderata for a mature theory. |
| [[2604.21617v1]] Local Neighborhood Instability in Parametric Projections | **中文：** 标准的 Trustworthiness/Continuity 指标对输入扰动引起的投影不稳定性完全失明，Jacobian 正则化将均值位移降低高达 85%。<br>**English:** Standard DR quality metrics are blind to perturbation instability; Jacobian regularization reduces mean displacement by up to 85%; three new displacement-based metrics fill the blind spot. |
| [[2604.21836v1]] Cross-Modal Convergence via Intra-Modal Dispersion | **中文：** 利用广义普鲁克鲁斯分析量化视觉模型的单刺激表示分散度，低分散度刺激产生高达 2 倍的视觉-语言跨模态对齐，为柏拉图表示假设提供刺激层面验证。<br>**English:** GPA-based per-stimulus dispersion across 4 ViT variants predicts cross-modal alignment (up to 2× gap); low-dispersion stimuli represent the convergent core of the Platonic Representation Hypothesis. |
| [[2604.21909v1]] Directional Confusions RD Geometry | **中文：** 人类混淆广泛而微弱（高 breadth），ANN 混淆稀疏而强烈（高 magnitude），鲁棒性训练无法恢复人类的 breadth-strength 分布结构。<br>**English:** Rate-distortion framework reveals humans have high-breadth low-strength directional confusions while ANNs have low-breadth high-strength "sink-like" collapse; robustness training reduces magnitude but not the qualitative difference in organization. |
| [[2604.21599v1]] ML Interpretability via Provenance | **中文：** 将可解释性 NFR 分解为可溯源的功能需求（保存哪些训练数据、参数、步骤），用 yProv4ML 工具在线性回归和反事实解释两个案例中演示框架。<br>**English:** Proposes decomposing interpretability into provenance-based FRs verifiable by third parties; demonstrated with yProv4ML (PROV-O) on linear regression and counterfactual explanation experiments. |

---

### 推理效率与 KV 缓存 / Inference Efficiency & KV Cache

| 论文 / Paper | 摘要 / Summary |
|---|---|
| [[2604.21231v1]] SparKV Overhead-Aware KV Cache | **中文：** 端侧 LLM 中 KV 加载开销（而非计算）是 TTFT 主要瓶颈；KV Chunk Scheduler + MLP 稀疏度预测 + 运行时适配器三组件在 Jetson 上实现 1.3–5.1× TTFT 提升。<br>**English:** Identifies KV cache IO loading (not compute) as the dominant TTFT bottleneck on edge devices; overhead-aware greedy scheduler (MILP approximation) achieves 1.3–5.1× TTFT reduction with 99%+ accuracy retention. |
| [[2604.21335v1]] Sub-Token Routing in LoRA for KV Compression | **中文：** 将 LoRA 子空间和 KV 值组引入稀疏路由，在保持 99% MMLU 基线精度的前提下将 KV 缓存压缩至 37.5%（结合 Expected Attention）。<br>**English:** Sub-token routing for both LoRA subspaces and KV value groups; combined with Expected Attention achieves 37.5% total KV retention at 99.1–99.8% MMLU accuracy across 7B–72B models. |
| [[2604.21764v1]] TRS: Thinking with Reasoning Skills | **中文：** 离线将长推理轨迹蒸馏为结构化技能卡（Trigger/Do/Avoid/Check/Risk），推理时检索注入，在数学/代码任务上同时降低 token 消耗（最高 -61%）并提升准确率。<br>**English:** Training-free skill card retrieval breaks the efficiency-accuracy tradeoff; structured cards outperform raw CoT traces; hardest problems benefit most (−53.8% cost on Doubao); fails on non-reasoning tasks. |
| [[2604.21794v1]] DiffMAS: Differentiable Multi-Agent KV Communication | **中文：** KV cache 作为可学习通信接口的端到端多智能体训练框架，拼接式通信不引入梯度衰减（理论证明），Qwen3-8B AIME24 +26.7%，解码困惑度显著降低。<br>**English:** Treats inter-agent KV-cache as a trainable differentiable interface; concatenation proven to avoid gradient decay; Qwen3-8B gains +26.7% on AIME24 with lower decoding perplexity vs. text-based communication. |

---

### ML 可靠性与基准测试 / ML Reliability & Benchmarking

| 论文 / Paper | 摘要 / Summary |
|---|---|
| [[2604.21361v1]] Clock Skew Causal Observability | **中文：** 仅 3–5ms 时钟偏差静默破坏分布式 AI 推理的因果可观测性，吞吐量不受影响，`causality_health` 指标在 Kafka 和 ZeroMQ 上均可检测。<br>**English:** 3–5ms clock skew silently corrupts causal observability in distributed AI inference while leaving throughput unchanged; `causality_health` binary metric is transport-agnostic and directly integrable into SLO frameworks. |
| [[2604.21579v1]] CodeCocoon Metamorphic Testing APR | **中文：** 9 种语义保持代码变换（重命名、循环改写）在 Defects4J 上使 7 个主流 LLM 平均成功率下降 4.1–16%，且下降与 NLL（记忆代理指标）显著相关。<br>**English:** MT + NLL diagnostic confirms Defects4J data leakage across 7 models (−4.1% to −15.98% on Claude-3.7/GPT-4o); newer GitBug-Java shows minimal drops, providing a natural internal control; NestElseIf is the most diagnostic transformation. |
| [[2604.21192v1]] VLA Safety Evaluation B1K | **中文：** 在 BEHAVIOR-1K 上重现最优 VLA 策略，发现超 27% 成绩差异、10 类失效模式，新 sQ/seQ 安全指标将报告分数降低最高 35%。<br>**English:** Reproducibility crisis in B1K: >27% published vs. reproduced score gap; 10 failure categories via expert annotation; new sQ/seQ safety-aware metrics reduce scores by up to 35% on 20 tasks. |
| [[2604.21854v1]] Statistical Certification Framework for AI Risk | **中文：** 提出两阶段统计认证框架（监管机构定 δ/ε → 开发者用 RoMA/gRoMA 计算失败概率上界），将 EU AI Act 的抽象风险要求转化为可审计证书。<br>**English:** Two-stage certification framework mapping EU AI Act requirements to auditable RoMA/gRoMA statistical bounds; black-box applicable; demonstrated on AEB case study with aviation-grade δ=10⁻⁹. |
| [[2604.21556v1]] Probabilistic Verification via Hull Generation | **中文：** 回归树引导的边界感知采样构造安全/不安全概率包，给出神经网络安全概率的保证区间，比枝界法加速最高 10×。<br>**English:** Regression tree-guided probabilistic hull generation for DNN safety verification; achieves up to 10× speedup over branch-and-bound; architecture-agnostic; formal soundness guarantee [Lₛ, Uₛ]. |
| [[2604.21889v1]] TingIS Risk Event Discovery | **中文：** 蚂蚁集团部署的企业级实时风险事件发现系统，从每分钟 2000 条噪声投诉中以 3.5 分钟 P90 延迟发现 95% 高优先级风险事件，噪声告警降低 94.3%。<br>**English:** Production-deployed Ant Group system processing 2000 incidents/min at P90 3.5-min latency; 94.3% alert noise reduction via multi-dimensional denoising; time-decay historical association prevents stale-event merges. |

---

### 数值精度与量化 / Numerical Precision & Quantization

| 论文 / Paper | 摘要 / Summary |
|---|---|
| [[2604.21743v1]] QATIE: Quantization-Aware Image Enhancement | **中文：** 门控编码器 + 多尺度细化 + QAT（伪量化节点+直通估计器），INT8 在 DPED 上达 21.05 dB PSNR，比训练后量化高 0.474 dB，Mobile AI 2026 第二名。<br>**English:** QAT with fake quantization operators recovers +0.474 dB PSNR over post-training quantization at INT8; 41.8ms latency on Qualcomm QNN HTP; 2nd place in Mobile AI 2026 RGB Enhancement Challenge. |
| [[2604.21602v1]] Memristor Reservoir Computing Quantization | **中文：** 系统分析挥发性忆阻器 RC 系统中预处理与器件参数的联合影响，分段 > 量化 > 维度 > 奇偶校验，3 位量化是稳健运行下限，20% 器件变异率下仍达 94.2%。<br>**English:** Factorial ANOVA on PDFN memristive RC: sectioning dominates accuracy, then quantization bits; 3-bit (8-level) minimum for robustness; achieves 95.89% on MNIST with 94.3% accuracy under 20% device variability. |
| [[2604.21203v1]] De-biased SGD Covariance Estimator | **中文：** 识别标准批均值协方差估计器的渐近偏差来源，去偏版本收敛速率从 n^((α-1)/4) 提升至 n^(-(1+α)/2) log n，AISTATS 2026。<br>**English:** AISTATS 2026: debiased online BM covariance estimator for SGD achieves n^(-(1+α)/2) log n vs. n^((α-1)/4) prior rate; same O(d²) cost; CI coverage simulation: 94.8% vs. 88.1% standard BM at n=10K. |

---

### 检索与稀疏表示 / Retrieval & Sparse Representations

| 论文 / Paper | 摘要 / Summary |
|---|---|
| [[2604.21511v1]] SAE-SPLADE | **中文：** 用稀疏自编码器学习的语义概念词汇替代 SPLADE 的 MLM 词汇头，SIGIR 2026 接收，QD-FLOPs 减少 2.2×，多语言迁移能力提升。<br>**English:** SIGIR 2026: replaces SPLADE's MLM head with SAE learned concept vocabulary; 2.2× QD-FLOPs efficiency gain with negligible MRR loss; SAE latents show synonym coverage and polysemy disambiguation. |

---

### 多语言推理与 RL 训练 / Multilingual Reasoning & RL Training

| 论文 / Paper | 摘要 / Summary |
|---|---|
| [[2604.21593v1]] polyGRPO Language as Latent Variable | **中文：** 将推理链语言选择形式化为隐变量，多语言 rollout 在 GRPO 框架中探索最优思维语言，MGSM 多语言平均 +12.77pp，模型自发形成英语主导思维模式。<br>**English:** Formalizes reasoning language as a latent variable; polyGRPO multilingual rollouts yield +12.77pp multilingual average and +3.6pp English on MGSM; models spontaneously converge to English-dominant reasoning. |
| [[2604.21286v1]] Cross-Entropy Load-Bearing Predictive Coding | **中文：** 预注册受控实验证明 K-way 能量探针与 softmax 的 AUROC² 差距 66% 来自 CE 训练引起的 logit 尺度膨胀，温度缩放消除该成分；bPC 中探针超越 softmax。<br>**English:** Pre-registered CIFAR-10 study: 66% of energy probe's AUROC² gap vs. softmax is attributable to CE-linked logit-scale inflation; temperature scaling isolates scale-dependent vs. scale-invariant components. |

---

### 机器人与视觉 / Robotics & Vision

| 论文 / Paper | 摘要 / Summary |
|---|---|
| [[2604.21192v1]] VLA Safety Evaluation B1K | **中文：** 见"ML 可靠性"节。<br>**English:** See ML Reliability section. |

---

### 安全与对齐 / Safety & Alignment

| 论文 / Paper | 摘要 / Summary |
|---|---|
| [[2604.21860v1]] Transient Turn Injection (TTI) | **中文：** 攻击者 LLM 通过无记忆的独立会话逐步诱导目标 LLM 泄露敏感信息，Gemini 系列最脆弱（TTI 分 34–40），Claude 最具抵抗力（2 分）。<br>**English:** TTI attack exploits per-turn stateless safety checks via distributed multi-session adversarial prompting; Gemini variants most vulnerable (34–40 hits); Claude constitutional AI most resistant (0–2 hits); TTI consistently exceeds PAIR scores. |

---

### 量子计算（参考） / Quantum Computing (Reference)

| 论文 / Paper | 摘要 / Summary |
|---|---|
| [[2604.21475v1]] MemTree Photonic Fusion Erasure | **中文：** 树编码融合将光子量子计算中的擦除错误重定向为可纠正的泡利错误，在真实 QPU 上实现 3.64× 保真度提升，光子源需求降低至 18%。<br>**English:** Tree-encoded fusion distinguishes erasure from failure, redirecting photon-loss errors to correctable Pauli errors; 3.64× fidelity improvement and 0.18× photon sources on Quandela Benlenos QPU. |

---

### 可视化工具 / Visualization Tools

| 论文 / Paper | 摘要 / Summary |
|---|---|
| [[2604.21830v1]] GFlowState Training Visualization | **中文：** 首个专为 GFlowNet 训练过程设计的可视化分析系统，四联动视图揭示模式崩溃和欠探索区域，在网格和晶体生成两个案例中验证。<br>**English:** First visual analytics system for GFlowNet training; four coordinated views expose mode collapse and coverage gaps invisible to TensorBoard/W&B; validated on grid environment and crystal structure generation. |

---

## All Papers

| 论文 / Paper | Score | Topic | One-liner (English) |
|---|---|---|---|
| [[2604.21632v1]] To See the Unseen: Embedding Collapse | 5 | LLM Training / Interpretability | Proves unseen-token embedding collapse is mathematically inevitable; confirms in Gemma 3; fix: copy attention + frozen embeddings. |
| [[2604.21327v1]] DDRL: Debiased TTRL | 5 | LLM Training Stability | Diagnoses GRPO normalization as spurious-reward amplifier in test-time RL; three-component fix yields +6.7% on Qwen2.5-Math-1.5B. |
| [[2604.21361v1]] Clock Skew Causal Observability | 5 | ML Reliability / Observability | 3–5ms clock skew silently breaks causal observability in distributed AI inference pipelines while throughput stays green. |
| [[2604.21428v1]] Decoupled DiLoCo | 4 | LLM Training / Distributed | Async federated LLM pre-training achieves 86% goodput at 2.4M chips with ML quality parity via min-quorum aggregation. |
| [[2604.21199v1]] ARFBench Time-Series QA | 4 | LLM Inference Evaluation / Observability | First real-incident TSQA benchmark from Datadog; TSFM-VLM hybrid matches GPT-5; human experts still lead on Tier-3 predictive reasoning. |
| [[2604.21255v1]] Agent Behavioral Similarity RPS+AGS | 4 | Interpretability / LLM Evaluation | First formal metrics for LLM tool-use behavioral similarity; Kimi-K2 shows 82.7% AGS similarity to Claude Sonnet 4.5; distillation confirmed causally. |
| [[2604.21523v1]] FOCUS VLM Evaluator Reliability | 4 | LLM Inference Evaluation | Meta-benchmark: single-answer scoring fails >50% on T2I perturbations; pairwise comparison most reliable; more reasoning tokens don't consistently help. |
| [[2604.21395v1]] ERM Geometric Blind Spot (PMH) | 4 | LLM Training / Interpretability | Theorem: ERM must encode label-correlated nuisances; PMH Gaussian regularizer uniquely fixes this; PGD adversarial training worsens isotropic geometry. |
| [[2604.21231v1]] SparKV Edge KV Cache | 4 | LLM Inference Efficiency | Overhead-aware KV scheduling targets IO bottleneck (not compute) on edge devices; 1.3–5.1× TTFT reduction across 5 models and 4 device classes. |
| [[2604.21343v1]] Latent Denoising LMM (LD-LMM) | 4 | LLM Training / Multimodal | Saliency-guided corruption + teacher recovery during instruction tuning improves 15–18/18 benchmarks with zero inference overhead. |
| [[2604.21346v1]] Symbolic Grounding VLM Bottleneck | 4 | Interpretability / VLM Evaluation | Ground-truth LOGO programs yield +25–30 pp on Bongard-LOGO; visual encoder — not reasoning — is the bottleneck; Phi-4-Reasoning reaches 96.2%. |
| [[2604.21579v1]] CodeCocoon Metamorphic APR | 4 | ML Reliability / Benchmark Contamination | 9 semantics-preserving transformations expose Defects4J memorization; all 7 models degrade significantly; MT + NLL combined is the most reliable diagnostic. |
| [[2604.21691v1]] Scientific Theory of Deep Learning | 4 | Deep Learning Theory | 14 DeepMind/Stanford/NYU theorists argue "learning mechanics" is crystallizing; five evidence strands; seven desiderata for a mature theory. |
| [[2604.21611v1]] Verbal Process Supervision (VPS) | 4 | LLM Inference Evaluation | Step-level verbal critique is a 4th inference-time scaling axis; +63.3 pp on AIME 2025 for weak actors; headroom (r=0.90) predicts gain. |
| [[2604.21794v1]] DiffMAS KV Communication | 4 | LLM Inference / Multi-Agent | Differentiable KV-cache inter-agent communication; concatenation avoids gradient decay (proved); Qwen3-8B +26.7% on AIME24 with lower PPL. |
| [[2604.21764v1]] TRS: Thinking with Reasoning Skills | 4 | LLM Inference Efficiency | Offline skill distillation + retrieval injection breaks efficiency-accuracy tradeoff; −61% tokens with accuracy gains on hard problems. |
| [[2604.21454v1]] Reasoning Primitives Hybrid LLMs | 3 | LLM Inference Evaluation / Architecture | Recall + state-tracking primitives framework; hybrid architecture survives high sequential dependence (0.45) where transformer collapses (0.03). |
| [[2604.21593v1]] polyGRPO Multilingual Reasoning | 3 | LLM Training / Multilingual | Language-as-latent-variable GRPO; +12.77pp multilingual MGSM average; models spontaneously converge to English-dominant thinking. |
| [[2604.21335v1]] Sub-Token LoRA KV Compression | 3 | LLM Inference Efficiency / Quantization | Sub-token routing for LoRA + KV value groups; 37.5% total KV retention at 99.1% MMLU accuracy on 7B–72B with Expected Attention. |
| [[2604.21769v1]] Who Defines Best? LMArena Slice | 3 | LLM Inference Evaluation | LMArena global rankings mask major category inversions; humans choose objectively correct math answer only 74% of the time. |
| [[2604.21916v1]] MathDuels Self-Play Benchmark | 3 | LLM Inference Evaluation | IRT self-play benchmark decouples solving from authoring; GPT-5.4-high tops solving but lags authoring; dynamic difficulty prevents saturation. |
| [[2604.21564v1]] LLM-Bias-Bench Sycophancy | 3 | LLM Reliability / Alignment | Indirect adversarial probing drives median sycophancy to 79%; Kimi K2 most resistant; no correlation between leaderboard rank and sycophancy resistance. |
| [[2604.21882v1]] RedirectQA Entity Surface Forms | 3 | LLM Inference Evaluation | Wikipedia redirect surface forms cause 23.7% answer flip rate; entity frequency > surface frequency in predicting factual access; cross-surface coupling confirmed. |
| [[2604.21854v1]] Statistical Certification AI Risk | 3 | ML Reliability | Two-stage certification maps EU AI Act to auditable RoMA/gRoMA statistical bounds; black-box applicable; demonstrated on AEB case study. |
| [[2604.21395v1]] ERM Geometric Blind Spot | 4 | ML Reliability / Training | (see above) |
| [[2604.21511v1]] SAE-SPLADE | 3 | Retrieval / Interpretability | SIGIR 2026: SAE concept vocabulary replaces SPLADE MLM head; 2.2× efficiency gain; synonym/polysemy disambiguation demonstrated qualitatively. |
| [[2604.21556v1]] Probabilistic Hull DNN Verification | 3 | ML Reliability | Regression-tree boundary-aware probabilistic hull verification; 10× speedup over branch-and-bound; formal [Lₛ, Uₛ] guarantee; architecture-agnostic. |
| [[2604.21203v1]] De-biased SGD Covariance Estimator | 3 | Numerical Precision / Training | AISTATS 2026: debiased online BM estimator achieves n^(-(1+α)/2) log n rate vs. n^((α-1)/4); CI coverage 94.8% vs. 88.1% at n=10K. |
| [[2604.21743v1]] QATIE Mobile Image Enhancement | 3 | Quantization / Edge AI | QAT recovers +0.474 dB over PTQ at INT8; 41.8ms on Qualcomm QNN HTP; 2nd place Mobile AI 2026 challenge. |
| [[2604.21889v1]] TingIS Risk Event Discovery | 3 | ML Reliability / Observability | Ant Group production system: 95% recall at 3.5min P90; 94.3% noise reduction; time-decay historical association is the key engineering innovation. |
| [[2604.21860v1]] Transient Turn Injection (TTI) | 3 | LLM Safety | Stateless multi-session adversarial attack; Gemini most vulnerable (34–40 TTI hits); Claude most resistant (0–2); TTI exceeds PAIR on all 13 models. |
| [[2604.21617v1]] Parametric Projection Instability | 3 | ML Reliability / Interpretability | Standard DR metrics blind to perturbation instability; Jacobian regularization reduces mean displacement 85%; three new diagnostic metrics. |
| [[2604.21836v1]] Cross-Modal Convergence Dispersion | 3 | Interpretability | GPA stimulus dispersion predicts cross-modal alignment (up to 2×); sharpens Platonic Representation Hypothesis to stimulus level. |
| [[2604.21286v1]] Cross-Entropy Load-Bearing PC | 2 | Interpretability / Training | Pre-registered study isolates CE logit inflation as 66% of energy probe's AUROC² gap vs. softmax; temperature scaling is the practical fix. |
| [[2604.21909v1]] Directional Confusions RD Geometry | 2 | Interpretability | Humans: broad-weak confusion; ANNs: sparse-strong sink collapse; robustness training can't recover human breadth-strength organization. |
| [[2604.21602v1]] Memristor RC Quantization | 2 | Numerical Precision / Neuromorphic | ANOVA: sectioning > quantization for PDFN RC accuracy; 3-bit minimum for robustness under 20% device variability; 95.89% MNIST at 581 memristors. |
| [[2604.21475v1]] MemTree Photonic Quantum Computing | 2 | Quantum Computing | Tree-encoded fusion converts photon-loss erasure to correctable errors; 3.64× fidelity + 0.18× photon sources on real Quandela QPU. |
| [[2604.21830v1]] GFlowState Visualization | 2 | ML Reliability / Visualization | First visual analytics tool for GFlowNet training; four coordinated views; mode collapse and coverage gaps made diagnostic. |
| [[2604.21599v1]] ML Interpretability via Provenance | 2 | Interpretability / ML Engineering | Decomposes interpretability NFR into verifiable provenance FRs; demonstrated with yProv4ML on linear regression and counterfactual explanation. |
