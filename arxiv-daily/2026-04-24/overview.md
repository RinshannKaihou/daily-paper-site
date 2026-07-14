---
title: "Daily Paper Overview — 2026-04-24"
date: 2026-04-24
tags:
  - deep-learning-theory
  - distributed-training
  - neural-network-verification
  - LLM-reasoning
  - interpretability
  - evaluation
  - continual-learning
papers: 28
---

## 今日必读 / Must Read Today

### 1. [[2604.21428v1]] Decoupled DiLoCo: Resilient Distributed Pre-training

**推荐理由：** 首次将LLM分布式预训练的同步间歇通信彻底解耦为全异步框架，在百万级芯片、集群MTBF不足一分钟的极端故障场景下实现88%训练goodput（vs 弹性DP的58%）和零全局停机。对大规模训练基础设施设计具有直接工程价值。
**Why read:** First fully asynchronous distributed LLM pre-training framework achieving 88% goodput vs. 58% for elastic DP under extreme million-chip failure scenarios with zero global downtime. Immediate engineering impact for large-scale training infrastructure.

### 2. [[2604.21395v1]] Supervised Learning Has a Necessary Geometric Blind Spot

**推荐理由：** 数学证明经验风险最小化必然在干扰方向上保留非零Jacobian敏感度（几何盲点），统一解释了非鲁棒特征、纹理偏好、腐蚀脆弱性、鲁棒性-精度权衡四个经验现象，并指出高斯扰动是唯一能均匀抑制编码器Jacobian的扰动形式。
**Why read:** Rigorously proves ERM necessarily retains non-zero Jacobian sensitivity along nuisance directions, unifying four previously separate empirical phenomena. Gaussian perturbation is uniquely justified as the only uniform Jacobian suppressor.

### 3. [[2604.21691v1]] There Will Be a Scientific Theory of Deep Learning

**推荐理由：** 汇集多位理论研究者，系统梳理了从NTK、缩放定律到机制可解释性的深度学习理论基础进展，论证了建立深度学习科学理论的可行性与路径，对理解该领域的理论前沿具有全景参考价值。
**Why read:** Collects leading theorists to systematically survey the theoretical foundations of deep learning from NTK and scaling laws to mechanistic interpretability, arguing for the feasibility and roadmap of a scientific theory of deep learning.

---

## 按主题分类 / Papers by Topic

### Neural Network Verification & Certification / 神经网络验证与认证

| Paper | Title / 标题 | Summary / 摘要 |
|-------|-------------|----------------|
| [[2604.21256v1]] | Robustness Analysis of POMDP Policies to Observation Perturbations | 量化POMDP策略在观测扰动下的鲁棒性，区分粘性和非粘性两种对抗模型 / Quantifies POMDP policy robustness to observation perturbations with sticky and non-sticky adversarial models |
| [[2604.21556v1]] | Probabilistic Verification of Neural Networks via Efficient Probabilistic Hull Generation | 回归树引导的概率包络生成框架，为高斯噪声输入下的DNN安全概率提供保证上下界 / Regression-tree-guided probabilistic hull generation for guaranteed bounds on DNN safety probability under Gaussian noise |
| [[2604.21854v1]] | Bounding the Black Box: A Statistical Certification Framework for AI Risk Regulation | 借鉴航空业认证范式，提出两阶段黑盒AI风险认证框架，填补EU AI Act量化验证空白 / Two-stage black-box AI certification framework inspired by aviation standards, filling the quantitative verification gap in EU AI Act |

### Distributed Training & Systems Reliability / 分布式训练与系统可靠性

| Paper | Title / 标题 | Summary / 摘要 |
|-------|-------------|----------------|
| [[2604.21428v1]] | Decoupled DiLoCo for Resilient Distributed Pre-training | 全异步解耦分布式LLM预训练框架，百万级芯片故障下88% goodput / Fully asynchronous distributed LLM pre-training achieving 88% goodput under million-chip failure scenarios |
| [[2604.21361v1]] | Time, Causality, and Observability Failures in Distributed AI Inference Systems | 3-5ms时钟偏移即可导致分布式AI推理可观测性因果逻辑静默失效 / 3-5ms clock skew silently breaks timestamp-based causal observability in distributed AI inference |

### LLM Training & Fine-tuning / LLM训练与微调

| Paper | Title / 标题 | Summary / 摘要 |
|-------|-------------|----------------|
| [[2604.21327v1]] | Understanding and Mitigating Spurious Signal Amplification in Test-Time RL for Math Reasoning | 揭示TTRL中GRPO放大虚假信号的问题，提出DDRL框架相对ETMR提升1.7%-6.7% / Reveals GRPO amplifies spurious signals in TTRL; DDRL framework achieves +1.7%-6.7% over ETMR |
| [[2604.21905v1]] | Low-Rank Adaptation Redux for Large Models | 信号处理视角的LoRA综述，揭示标准LoRA严重利用不足分配的秩 / Signal-processing perspective survey on LoRA, revealing standard LoRA severely underutilizes allocated rank |
| [[2604.21927v1]] | Fine-Tuning Regimes Define Distinct Continual Learning Problems | 证明不同微调方式定义了本质上不同的持续学习问题，打破"一种方法通吃"假设 / Proves different fine-tuning regimes define fundamentally different CL problems, challenging one-size-fits-all assumption |
| [[2604.21930v1]] | Temporal Taskification in Streaming Continual Learning: A Source of Evaluation Instability | 揭示流式持续学习中时间任务划分导致评估不稳定性 / Reveals temporal task partitioning introduces hidden evaluation instability in streaming continual learning |

### Interpretability & Representation Analysis / 可解释性与表征分析

| Paper | Title / 标题 | Summary / 摘要 |
|-------|-------------|----------------|
| [[2604.21836v1]] | Modulating Cross-Modal Convergence with Single-Stimulus Intra-Modal Dispersion | 基于Procrustes分析的模内离散度指标，低离散度刺激可将跨模态对齐提升近两倍 / GPA-based intra-modal dispersion metric; low-dispersion stimuli yield up to 2x cross-modal alignment boost |
| [[2604.21555v1]] | Finding Meaning in Embeddings: Concept Separation Curves | 无需分类器的句嵌入评估方法，揭示SOTA模型存在位置敏感性缺陷 / Classifier-free sentence embedding evaluation revealing position-sensitivity artifacts in SOTA models |
| [[2604.21617v1]] | Local Neighborhood Instability in Parametric Projections | 参数化投影局部稳定性评估框架，Jacobian正则化可将位移降低85% / Stability framework for parametric projections; Jacobian regularization reduces displacement by up to 85% |
| [[2604.21882v1]] | Revisiting Non-Verbatim Memorization in LLMs: The Role of Entity Surface Forms | RedirectQA数据集揭示事实问答预测因实体命名方式不同而翻转 / RedirectQA dataset reveals factual QA predictions flip when entity surface forms change |
| [[2604.21454v1]] | Reasoning Primitives in Hybrid and Non-Hybrid LLMs | 将LLM推理分解为recall和state-tracking，混合架构在高复杂度下显著优于纯Transformer / Decomposes LLM reasoning into recall and state-tracking; hybrid architectures excel at high complexity |

### Evaluation & Benchmarking / 评估与基准测试

| Paper | Title / 标题 | Summary / 摘要 |
|-------|-------------|----------------|
| [[2604.21523v1]] | Seeing Isn't Believing: Uncovering Blind Spots in Evaluator VLMs | Focus基准揭示VLM评估器单答案评分失败率超50% / Focus benchmark reveals VLM evaluators fail to detect perturbations in >50% of cases under single scoring |
| [[2604.21276v1]] | Do LLM Decoders Listen Fairly? Benchmarking ASR Bias | 首次系统研究LLM解码器对语音识别公平性的影响，音频编码器比LLM规模更重要 / First systematic study showing audio encoder design matters more than LLM scale for ASR fairness |
| [[2604.21769v1]] | Who Defines "Best"? Towards Interactive, User-Defined Evaluation of LLM Leaderboards | LMArena数据集严重偏向编程/AI，交互式工具让用户自定义排行榜权重 / LMArena heavily skewed toward coding/AI; interactive tool lets users customize leaderboard weights |
| [[2604.21765v1]] | PrismaDV: Automated Task-Aware Data Unit Test Generation | LLM驱动的任务感知数据单元测试生成，F1比基线高出20+个百分点 / LLM-driven task-aware data unit test generation outperforming baselines by 20+ F1 points |

### Mathematical Foundations of ML / 机器学习数学基础

| Paper | Title / 标题 | Summary / 摘要 |
|-------|-------------|----------------|
| [[2604.21691v1]] | There Will Be a Scientific Theory of Deep Learning | 系统梳理从NTK、缩放定律到机制可解释性的深度学习理论基础 / Systematic survey of deep learning theoretical foundations from NTK and scaling laws to mechanistic interpretability |
| [[2604.21395v1]] | Supervised Learning Has a Necessary Geometric Blind Spot | 证明ERM必然在干扰方向保留非零Jacobian敏感度，统一解释四个经验现象 / Proves ERM necessarily retains Jacobian sensitivity along nuisance directions, unifying four empirical phenomena |
| [[2604.21595v1]] | A Kernel Nonconformity Score for Multivariate Conformal Prediction | 核函数驱动的多元共形预测，预测区域体积减少5%-86% / Kernel-based multivariate conformal prediction reducing prediction region volumes by 5-86% |
| [[2604.21632v1]] | To See the Unseen: Transformer Generalization in Symbolic Reasoning | 揭示embedding坍缩是Transformer无法泛化到未见token的根本原因 / Identifies embedding collapse as the root cause preventing Transformers from generalizing to unseen tokens |
| [[2604.21286v1]] | Cross-Entropy Is Load-Bearing: A Pre-Registered Scope Test of the K-Way Energy Probe | 预注册实验证明CE损失是探针-softmax差距的主要贡献者 / Pre-registered study proving CE loss is the major contributor to the probe-softmax gap |
| [[2604.21602v1]] | On the Role of Preprocessing and Memristor Dynamics in Reservoir Computing | 预处理策略和易失性忆阻器动力学对储备池计算图像分类的影响 / Systematic study of preprocessing and volatile memristor dynamics in reservoir computing for image classification |

### Other / 其他

| Paper | Title / 标题 | Summary / 摘要 |
|-------|-------------|----------------|
| [[2604.21611v1]] | Process Supervision via Verbal Critique Improves Reasoning in LLMs | 无需训练的推理时VPS框架，GPQA Diamond达94.9%超越SOTA / Training-free VPS inference framework achieving 94.9% on GPQA Diamond, surpassing SOTA |
| [[2604.21579v1]] | Diagnosing Memorization in LLM-based APR via Metamorphic Testing | CodeCocoon框架用蜕变测试诊断LLM程序修复中的记忆化 / CodeCocoon uses metamorphic testing to diagnose memorization in LLM-based automated program repair |
| [[2604.21511v1]] | From Tokens to Concepts: Leveraging SAE for SPLADE | SAE替代SPLADE词表投影层，QD-FLOPs降低55% / SAE replaces SPLADE vocabulary projection, reducing QD-FLOPs by 55% with comparable effectiveness |
| [[2604.21743v1]] | Bridging the Training-Deployment Gap: Gated Encoding for Efficient Quantization-Aware Image Enhancement | 门控编码器+量化感知训练，INT8推理下接近全精度质量 / Gated encoder with QAT achieving near-FP32 quality under INT8 inference at 41.8ms on mobile NPU |

---

## All Papers

| # | arXiv ID | Title (Short) | Summary / 摘要 |
|---|----------|---------------|----------------|
| 1 | [[2604.21256v1]] | POMDP Observation Robustness | 量化POMDP策略在观测扰动下的鲁棒性 / Quantifies POMDP policy robustness to observation perturbations |
| 2 | [[2604.21276v1]] | ASR Fairness with LLM Decoders | LLM解码器对ASR公平性影响的系统研究 / Systematic study of LLM decoder effects on ASR fairness |
| 3 | [[2604.21286v1]] | Cross-Entropy in Energy Probe | CE损失对探针-softmax差距的贡献分解 / Decomposes CE loss contribution to probe-softmax gap |
| 4 | [[2604.21327v1]] | DDRL: Spurious Signal in TTRL | TTRL中虚假信号放大问题及DDRL缓解框架 / Spurious signal amplification in TTRL and DDRL mitigation framework |
| 5 | [[2604.21361v1]] | Causality in Distributed AI Inference | 分布式AI推理中时钟偏移导致可观测性失效 / Clock skew silently breaks causal observability in distributed AI inference |
| 6 | [[2604.21395v1]] | Geometric Blind Spot in Supervised Learning | ERM必然保留干扰方向Jacobian敏感度的理论证明 / Theoretical proof that ERM necessarily retains Jacobian sensitivity along nuisance directions |
| 7 | [[2604.21428v1]] | Decoupled DiLoCo | 全异步分布式LLM预训练，88% goodput / Fully asynchronous distributed LLM pre-training with 88% goodput |
| 8 | [[2604.21454v1]] | Reasoning Primitives in Hybrid LLMs | LLM推理的recall/state-tracking分解与混合架构优势 / Decomposes LLM reasoning into recall/state-tracking; hybrid architecture advantages |
| 9 | [[2604.21511v1]] | SAE-SPLADE | SAE替代SPLADE词表投影，QD-FLOPs降低55% / SAE replaces SPLADE vocabulary projection, reducing QD-FLOPs by 55% |
| 10 | [[2604.21523v1]] | Focus: VLM Evaluator Blind Spots | VLM评估器单答案评分失败率超50% / VLM evaluators fail to detect perturbations in >50% of single scoring cases |
| 11 | [[2604.21555v1]] | Concept Separation Curves | 无分类器句嵌入评估，揭示位置敏感性 / Classifier-free embedding evaluation revealing position-sensitivity artifacts |
| 12 | [[2604.21556v1]] | Probabilistic Hull NN Verification | 回归树引导的DNN概率安全验证 / Regression-tree-guided probabilistic safety verification for DNNs |
| 13 | [[2604.21579v1]] | CodeCocoon: APR Memorization | 蜕变测试诊断LLM程序修复记忆化 / Metamorphic testing diagnoses memorization in LLM-based APR |
| 14 | [[2604.21595v1]] | Kernel Nonconformity for Conformal Prediction | 核函数多元共形预测，区域体积减少5-86% / Kernel-based multivariate conformal prediction reducing region volumes 5-86% |
| 15 | [[2604.21602v1]] | Memristor Reservoir Computing | 忆阻器储备池计算的预处理与动力学研究 / Preprocessing and dynamics in memristor-based reservoir computing |
| 16 | [[2604.21611v1]] | Verbal Process Supervision (VPS) | 推理时语言过程监督，GPQA Diamond 94.9% / Inference-time verbal process supervision achieving 94.9% on GPQA Diamond |
| 17 | [[2604.21617v1]] | Parametric Projection Instability | 参数化投影局部稳定性评估与Jacobian正则化 / Stability evaluation for parametric projections with Jacobian regularization |
| 18 | [[2604.21632v1]] | Transformer Symbolic Generalization | Embedding坍缩阻碍Transformer泛化到未见token / Embedding collapse prevents Transformers from generalizing to unseen tokens |
| 19 | [[2604.21691v1]] | Scientific Theory of Deep Learning | 深度学习理论基础全景综述 / Panoramic survey of theoretical foundations of deep learning |
| 20 | [[2604.21743v1]] | QAT Image Enhancement | 门控编码器量化感知图像增强 / Gated encoder with quantization-aware image enhancement for mobile |
| 21 | [[2604.21765v1]] | PrismaDV: Data Unit Tests | LLM驱动的任务感知数据单元测试生成 / LLM-driven task-aware data unit test generation |
| 22 | [[2604.21769v1]] | Interactive LLM Leaderboard Evaluation | 交互式用户自定义LLM排行榜评估 / Interactive user-defined LLM leaderboard evaluation |
| 23 | [[2604.21836v1]] | Cross-Modal Convergence via Intra-Modal Dispersion | 模内离散度预测跨模态对齐强度 / Intra-modal dispersion predicts cross-modal alignment strength |
| 24 | [[2604.21854v1]] | AI Risk Certification Framework | 两阶段黑盒AI风险统计认证框架 / Two-stage black-box statistical AI risk certification framework |
| 25 | [[2604.21882v1]] | RedirectQA: Entity Surface Forms in LLM Memorization | 实体命名方式改变导致事实问答预测翻转 / Entity surface form changes flip factual QA predictions |
| 26 | [[2604.21905v1]] | LoRA Redux Survey | 信号处理视角的LoRA综述 / Signal-processing perspective survey on LoRA for large models |
| 27 | [[2604.21927v1]] | Fine-Tuning Regimes in Continual Learning | 不同微调方式定义不同的持续学习问题 / Different fine-tuning regimes define distinct continual learning problems |
| 28 | [[2604.21930v1]] | Temporal Taskification in Streaming CL | 时间任务划分导致流式持续学习评估不稳定性 / Temporal task partitioning introduces evaluation instability in streaming CL |
