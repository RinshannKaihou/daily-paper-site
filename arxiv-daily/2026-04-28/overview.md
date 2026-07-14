---
title: "ArXiv Daily Paper Digest — 2026-04-28"
date: "2026-04-28"
tags:
  - arxiv-daily
  - LLM
  - alignment
  - interpretability
  - evaluation
  - RL
  - training
  - safety
papers_count: 40
---

# ArXiv Daily Paper Overview — 2026-04-28

---

## 今日必读 / Must Read Today

### 1. [[2604.25866v1|From Syntax to Emotion: Mechanistic Analysis of Emotion Inference in LLMs]]

**为何必读 / Why read:** 该工作首次利用稀疏自编码器(SAE)系统揭示了LLM在情绪推理中的三阶段前馈机制（语法→语义→情绪特征），发现Disgust缺乏专用表征、Surprise特征与其他情绪共激活等关键弱点，并提出仅需5个标注样本即可实现的数据高效因果引导方法。This is the most important paper today for anyone working on LLM hidden states and interpretability — it discovers a consistent three-phase representational flow (syntax → semantics → emotion) during emotion inference across Gemma and Llama families, provides causal evidence through SAE feature ablation, and offers a data-efficient steering method requiring only 5 labeled examples per emotion. (Relevance: LLM Hidden States & Interpretability)

### 2. [[2604.25235v1|VLM Judges Can Rank but Cannot Score]]

**为何必读 / Why read:** 首次系统性地将共形预测应用于VLM-as-Judge评测，揭示了“排序可靠但绝对评分不可靠”(ranking-scoring decoupling)这一关键失效模式——视觉密集型任务（图表理解、数学推理）的预测区间覆盖约70%评分范围，且标注质量对区间宽度的影响是模型规模的4.5倍。This paper is indispensable for anyone using LLM/VLM-as-judge pipelines — it applies conformal prediction to reveal that VLM judges produce trustworthy rankings but untrustworthy absolute scores, with a task-dependent uncertainty map spanning 14 visual categories. The finding that annotation quality matters 4.5x more than model scale for prediction interval width has immediate practical implications for benchmark design. (Relevance: LLM Inference Evaluation)

### 3. [[2604.25077v1|Evaluating Risks in Weak-to-Strong Alignment: A Bias-Variance Perspective]]

**为何必读 / Why read:** 通过偏差-方差-协方差分解框架，发现强模型置信度方差是弱到强对齐中盲点欺骗(blind-spot deception)的最强预测信号(Spearman ρ = 0.929)，并提供了仅需held-out数据即可计算的实用诊断工具，无需上限模型。This paper directly addresses LLM training stability by providing a rigorous bias-variance-covariance decomposition of weak-to-strong alignment failure modes, demonstrating that strong-model variance serves as a powerful early-warning signal for blind-spot deception across RLHF and SFT pipelines, with immediate practical value for post-training safety monitoring. (Relevance: LLM Training Stability & Observability)

---

## 按主题分类 / Papers by Topic

### Alignment & Safety / 对齐与安全

| # | Paper | Key Insight / 核心洞见 |
|---|-------|----------------------|
| 1 | [[2604.25077v1\|Weak-to-Strong Alignment Bias-Variance]] | Strong-model variance is the strongest predictor of blind-spot deception (ρ=0.929). / 强模型方差是盲点欺骗的最强预测信号。 |
| 2 | [[2604.25119v1\|Gaussian Probing for CSAM Detection]] | Detects harmful LoRA specialization via internal activations on Gaussian noise, zero generation required. / 通过高斯噪声输入的内部激活检测CSAM专用LoRA，无需生成。 |
| 3 | [[2604.25136v1\|Frictive Policy Optimization (FPO)]] | Reframes alignment as epistemic control — learn when to clarify/refuse/verify, not just what to answer. / 将对齐重新定义为认知控制问题，学习何时澄清/拒绝/验证。 |
| 4 | [[2604.25249v1\|Below-Chance Blindness in Small LLMs]] | BCB detection fails at 7-9B scale; models use positional heuristics instead of answer-aware avoidance. / 低于随机水平检测在小模型上失败，模型采用位置启发式而非答案回避。 |
| 5 | [[2604.25580v1\|Bye Bye Perspective API]] | Systematic critique of NLP's dependence on a single closed-source toxicity tool, with 10 infrastructure requirements. / 系统批判NLP对单一闭源毒性工具的依赖，提出10项基础设施需求。 |
| 6 | [[2604.25779v1\|Subliminal Learning via Gradient Alignment]] | Sustained weak positive gradient alignment (~0.008 cos sim) causally drives subliminal learning. / 持续微弱正梯度对齐是subliminal learning的因果驱动力。 |
| 7 | [[2604.25783v1\|Subliminal Steering]] | Trainable steering vectors replace system prompts for stronger hidden bias transfer; vectors can be recovered from generated data. / 可训练引导向量替代系统提示实现更强的隐藏偏差传递。 |
| 8 | [[2604.25872v1\|When Errors Can Be Beneficial]] | Reward errors categorized into harmful/benign/beneficial; some errors accelerate optimization by preventing stalling. / 奖励错误分为有害/无害/有益三类，某些错误可加速优化。 |

### Interpretability & Mechanistic Analysis / 可解释性与机制分析

| #   | Paper                                                               | Key Insight / 核心洞见                                                                                                                          |
| --- | ------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| 1   | [[2604.25143v1\|Gradient-Direction Sensitivity]]                    | SVD on raw gradients (vs. AdamW updates) amplifies SED-LCH coupling by 1-2 orders of magnitude. / 对原始梯度而非AdamW更新量做SVD，将SED-LCH耦合提升1-2个数量级。  |
| 2   | [[2604.25167v1\|IGDS: Interpretability-Guided Data Selection]]      | Uses SAE causal features to select training data; 50% data beats full SFT by +17.4% on Math. / 用SAE因果特征筛选训练数据，50%数据超越全量微调17.4%。             |
| 3   | [[2604.25315v1\|SaliencyDecor]]                                     | ZCA whitening during training fixes gradient entanglement from correlated features; zero inference overhead. / 训练中ZCA白化解耦相关特征导致的梯度纠缠，无推理开销。 |
| 4   | [[2604.25866v1\|From Syntax to Emotion: Emotion Inference in LLMs]] | Three-phase flow (syntax→semantics→emotion); Disgust lacks dedicated features; 5-example steering works. / 三阶段信息流(语法→语义→情绪)；Disgust缺乏专用特征。  |

### Evaluation & Benchmarks / 评估与基准测试

| # | Paper | Key Insight / 核心洞见 |
|---|-------|----------------------|
| 1 | [[2604.25110v1\|Knowledge Distillation Must Account for What It Loses]] | Proposes Distillation Loss Statement (DLS) as a standardized accountability framework for 8 off-metric loss dimensions. / 提出蒸馏损失声明(DLS)作为8个非指标性损失维度的标准化问责框架。 |
| 2 | [[2604.25149v1\|Semantic Layers for Reliable LLM Analytics]] | A 4KB semantic-layer document boosts analytical accuracy by +17 to +23 pp; context dominates model choice. / 4KB语义层文档将分析准确率提升17-23个百分点，上下文比模型选择更重要。 |
| 3 | [[2604.25224v1\|ValueAlpha: Agreement-Gated Stress Testing]] | Preregistered protocol for testing LLM-judged investment rationales; reveals pervasive verbosity bias (Δ=-2.81). / 预注册的LLM评委压力测试协议，揭示普遍的冗长偏差(Δ=-2.81)。 |
| 4 | [[2604.25235v1\|VLM Judges Can Rank but Cannot Score]] | Conformal prediction reveals ranking-scoring decoupling in VLM judges; annotation quality matters 4.5x more than model scale. / 共形预测揭示VLM评判者的排序-评分脱耦，标注质量重要性是模型规模的4.5倍。 |
| 5 | [[2604.25345v1\|Plausible but Wrong: Agentic Failures in Astrophysics]] | Silent failure taxonomy for AI science agents; domain context drives ~6x performance gain. / 科学AI智能体的静默失败分类体系；领域上下文驱动约6倍性能增益。 |
| 6 | [[2604.25359v1\|SOB: Structured Output Benchmark]] | Multi-source benchmark reveals near-perfect schema compliance masks 17-31% value errors; audio value accuracy only 23.7%. / 多模态结构化输出基准揭示接近完美的schema合规掩盖17-31%值错误。 |
| 7 | [[2604.25591v1\|Uncertainty Estimation for Audio-Aware LLMs]] | Semantic/verification methods outperform token-level; trustworthiness rankings highly model-dependent. / 语义/验证方法优于token级方法；可信度排名高度依赖模型。 |
| 8 | [[2604.25634v1\|Universality of LLM Output Distributions]] | 6 frontier LLMs converge to same Mandelbrot distribution (R²>0.94); enables 2.6μs/token CPU scoring. / 6个前沿LLM收敛到同一Mandelbrot分布(R²>0.94)；支持2.6微秒/token的CPU评分。 |
| 9 | [[2604.25765v1\|Error Sensitivity Profile (ESP)]] | Counterintuitive: ~91% of significant data corruption scenarios improved model performance. / 反直觉发现：约91%的显著数据污染场景反而提升了模型性能。 |

### Reinforcement Learning / 强化学习

| # | Paper | Key Insight / 核心洞见 |
|---|-------|----------------------|
| 1 | [[2604.25379v1\|Safe-Support Q-Learning]] | KL-regularized Q-learning with behavior policy on safe set ensures zero unsafe state visits during training. / 安全集支撑行为策略下的KL正则化Q学习，训练中零不安全状态访问。 |
| 2 | [[2604.25416v1\|Biased Dreams: Attractor Bias in Dreamer]] | Latent dynamics exhibit attractor bias toward well-represented regions, undermining epistemic uncertainty for exploration. / 潜动力学表现出对高密度区域的吸引子偏差，破坏探索的不确定性估计。 |
| 3 | [[2604.25419v1\|JURY-RL: Label-Free RLVR with Formal Verification]] | Decouples voting-based proposal from Lean verification; ResZero fallback prevents reward collapse. / 解耦投票提议与Lean验证；ResZero回退防止奖励崩塌。 |
| 4 | [[2604.25907v1\|Tsallis Loss Continuum for Cold-Start RLVR]] | GARL (q=0.75) escapes cold-start stalling where GRPO fails; PAFT achieves 47.9 maj@16 on HotPotQA. / GARL(q=0.75)逃离GRPO失败的冷启动停滞；PAFT在HotPotQA上达到47.9 maj@16。 |

### Training & Optimization / 训练与优化

| # | Paper | Key Insight / 核心洞见 |
|---|-------|----------------------|
| 1 | [[2604.25150v1\|Symmetry in Overparameterized Networks]] | Weight-space symmetries act as diagonal Hessian preconditioners and increase probability mass of minima near initialization. / 权重空间对称性充当Hessian对角预条件器，增加初始化附近的极小值概率质量。 |
| 2 | [[2604.25467v1\|SSF: Subspace SCAFFOLD for Federated Learning]] | Native heterogeneity correction in low-dimensional subspace with backfill mechanism preserving full-dim control info. / 低维子空间原生异构性校正，回填机制保留全维控制信息。 |
| 3 | [[2604.25550v1\|SignSGD Dithering and Hybrid Switching]] | Pre-sign Gaussian dithering restores lost magnitude info; calibrated switch to SGD hits 92.18% on CIFAR-10. / 预符号高斯抖动恢复幅度信息；校准切换至SGD在CIFAR-10上达92.18%。 |
| 4 | [[2604.25845v1\|Label Noise Transfer Learning]] | Bayes-optimal extraction with safety threshold purifies large noisy datasets using small clean set. / 贝叶斯最优提取加安全阈值，用小型干净集纯化大型噪声数据集。 |

### Model Architecture & Deployment / 模型架构与部署

| # | Paper | Key Insight / 核心洞见 |
|---|-------|----------------------|
| 1 | [[2604.25306v1\|QFlash: Integer-Only FlashAttention for ViT]] | End-to-end INT8 FlashAttention in single Triton kernel; up to 6.73x speedup over I-ViT, 18.8% energy savings. / 端到端INT8 FlashAttention单Triton内核；比I-ViT加速最高6.73倍，节能18.8%。 |
| 2 | [[2604.25699v1\|NVLLM: 3D NAND-Centric LLM Inference]] | Wafer-to-wafer 3D stacking offloads FFN to Flash; error-resilient dot-product engine; 37.9x throughput over GPU-SSD. / 晶圆级3D集成将FFN卸载至Flash；容错点积引擎；吞吐比GPU-SSD高37.9倍。 |
| 3 | [[2604.25724v1\|Scalable Inference for Compound AI Systems]] | Salesforce production study: >50% P95 latency reduction, 3.9x throughput, 30-40% cost savings. / Salesforce生产部署研究：P95延迟降低>50%，吞吐提升3.9倍，成本节约30-40%。 |

### Theory & Foundations / 理论与基础

| #   | Paper                                                                    | Key Insight / 核心洞见                                                                                                                                       |
| --- | ------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1   | [[2604.25334v1\|VAE-Inf for Imbalanced Classification]]                  | Two-stage VAE framework with projection statistics and distribution-free Type-I error control. / 两阶段VAE框架，投影统计量+无分布第一类错误控制。                              |
| 2   | [[2604.25372v1\|Closing the ZO-FO Gap via Input-to-State Stability]]     | ZO methods achieve same decay rate as FO; dimension dependence only in neighborhood size, not iteration complexity. / 零阶方法享有与一阶相同的衰减速率，维度依赖仅在收敛邻域大小。     |
| 3   | [[2604.25409v1\|Scaling Probabilistic Transformer via μP]]               | Zero-shot hyperparameter transfer from 17M to 0.4B by reconstructing potential functions. / 通过重构势函数实现从17M到0.4B的零样本超参数迁移。                                 |
| 4   | [[2604.25655v1\|RAA-PINNs: Change-Point Detection in Dynamical Systems]] | Two-stage framework using residual anomalies for change-point screening and differentiable joint inference. / 两阶段框架，利用残差异常进行变点筛选和可微分联合推断。                |
| 5   | [[2604.25733v1\|Verification of Neural Networks (Lecture Notes)]]        | 72-page theoretical introduction spanning FFNs, RNNs, attention, and Transformers with formal methods. / 72页讲义，覆盖前馈/循环/注意力/Transformer的形式化验证理论。          |
| 6   | [[2604.25800v1\|Barriers to Universal Reasoning with Transformers]]      | CoT Transformers bounded by TC⁰ under length generalization; signpost tokens overcome the limit. / 长度泛化下CoT Transformer的表达能力上限为TC⁰；signpost tokens突破此限制。 |
| 7   | [[2604.25904v1\|Teacher Forcing as Generalized Bayes]]                   | ITF inflates curvature by conditioning on single forced path; evidence fine-tuning degrades dynamical invariants. / ITF因条件化单一强制路径而膨胀曲率；证据微调恶化动力学不变量。     |

### Multilingual & Multimodal / 多语言与多模态

| # | Paper | Key Insight / 核心洞见 |
|---|-------|----------------------|
| 1 | [[2604.25578v1\|Marco-MoE: Multilingual MoE with Efficient Upcycling]] | Fine-grained MoE upcycling achieves 0.6-0.86B active params matching models with 3-14x more; 29→64 languages. / 细粒度MoE Upcycling以0.6-0.86B激活参数匹敌3-14倍激活参数模型。 |

---

## All Papers

| # | arXiv ID | Title / 标题 | Category / 分类 |
|---|---------|-------------|-----------------|
| 1 | [[2604.25077v1]] | Evaluating Risks in Weak-to-Strong Alignment: A Bias-Variance Perspective / 弱到强对齐中的风险评估：偏差-方差视角 | Alignment & Safety |
| 2 | [[2604.25110v1]] | Knowledge Distillation Must Account for What It Loses / 知识蒸馏必须报告其丢失了什么 | Evaluation & Benchmarks |
| 3 | [[2604.25119v1]] | Evaluation without Generation: Non-Generative Assessment of Harmful Model Specialization (CSAM) / 无生成的评估：有害模型专项能力的非生成式检测 | Alignment & Safety |
| 4 | [[2604.25136v1]] | Frictive Policy Optimization: Epistemic Intervention, Risk-Sensitive Control, and Reflective Alignment / 摩擦策略优化：认知干预、风险敏感控制与反思对齐 | Alignment & Safety |
| 5 | [[2604.25143v1]] | Gradient-Direction Sensitivity Reveals Linear-Centroid Coupling Hidden by Optimizer Trajectories / 梯度方向敏感性揭示优化器轨迹隐藏的线性-质心耦合 | Interpretability & Mech. Analysis |
| 6 | [[2604.25149v1]] | Semantic Layers for Reliable LLM-Powered Data Analytics / 面向可靠LLM数据分析的语义层 | Evaluation & Benchmarks |
| 7 | [[2604.25150v1]] | The Role of Symmetry in Optimizing Overparameterized Networks / 对称性在过参数化网络优化中的作用 | Training & Optimization |
| 8 | [[2604.25167v1]] | IGDS: Interpretability-Guided Data Selection for LLMs / 可解释性引导的大模型数据选择 | Interpretability & Mech. Analysis |
| 9 | [[2604.25224v1]] | ValueAlpha: Agreement-Gated Stress Testing of LLM-Judged Investment Rationales / ValueAlpha：一致性门控的LLM投资决策理由压力测试 | Evaluation & Benchmarks |
| 10 | [[2604.25235v1]] | VLM Judges Can Rank but Cannot Score: Task-Dependent Uncertainty in Multimodal Evaluation / VLM评判者可排序但无法评分：多模态评估中的任务依赖不确定性 | Evaluation & Benchmarks |
| 11 | [[2604.25249v1]] | Below-Chance Blindness: Prompted Underperformance in Small LLMs / 低于随机水平的盲区：小型LLM中的提示性表现不佳 | Alignment & Safety |
| 12 | [[2604.25306v1]] | QFlash: Bridging Quantization and Memory Efficiency in Vision Transformer Attention / QFlash：连接ViT注意力中的量化与内存效率 | Model Architecture & Deployment |
| 13 | [[2604.25315v1]] | SaliencyDecor: Enhancing Neural Network Interpretability through Feature Decorrelation / SaliencyDecor：通过特征去相关增强神经网络可解释性 | Interpretability & Mech. Analysis |
| 14 | [[2604.25334v1]] | VAE-Inf: A Statistically Interpretable Generative Paradigm for Imbalanced Classification / VAE-Inf：不平衡分类的统计可解释生成范式 | Theory & Foundations |
| 15 | [[2604.25345v1]] | Plausible but Wrong: Agentic Failures in Astrophysical Workflows / 看似合理但错误：天体物理工作流中的智能体失败 | Evaluation & Benchmarks |
| 16 | [[2604.25359v1]] | SOB: A Multi-Source Benchmark for Evaluating Structured Output Quality in LLMs / SOB：评估LLM结构化输出质量的多源基准 | Evaluation & Benchmarks |
| 17 | [[2604.25372v1]] | From Cursed to Competitive: Closing the ZO-FO Gap via Input-to-State Stability / 从诅咒到竞争力：通过输入-状态稳定性缩小零阶-一阶差距 | Theory & Foundations |
| 18 | [[2604.25379v1]] | Safe-Support Q-Learning: Learning without Unsafe Exploration / 安全支撑Q学习：无需不安全探索的学习 | Reinforcement Learning |
| 19 | [[2604.25409v1]] | Scaling Probabilistic Transformer via Efficient Cross-Scale Hyperparameter Transfer / 通过高效跨尺度超参数迁移扩展概率Transformer | Theory & Foundations |
| 20 | [[2604.25416v1]] | Biased Dreams: Limitations to Epistemic Uncertainty in Latent Space Models / 有偏之梦：潜空间模型中认知不确定性的局限 | Reinforcement Learning |
| 21 | [[2604.25419v1]] | JURY-RL: Votes Propose, Proofs Dispose for Label-Free RLVR / JURY-RL：投票提议，证明分发——无标签RLVR | Reinforcement Learning |
| 22 | [[2604.25467v1]] | Subspace SCAFFOLD for Efficient Federated Learning under Heterogeneous Data / 异构数据下高效联邦学习的子空间SCAFFOLD | Training & Optimization |
| 23 | [[2604.25550v1]] | Enhancing SignSGD: Small-Batch Convergence and Hybrid Switching / 增强SignSGD：小批量收敛与混合切换策略 | Training & Optimization |
| 24 | [[2604.25578v1]] | Marco-MoE: Open Multilingual Mixture-of-Expert Language Models with Efficient Upcycling / Marco-MoE：开放多语言MoE语言模型的高效Upcycling | Multilingual & Multimodal |
| 25 | [[2604.25580v1]] | Bye Bye Perspective API: Lessons for Measurement Infrastructure in NLP, CSS and LLM Evaluation / 再见Perspective API：NLP/CSS/LLM评估的测量基础设施教训 | Evaluation & Benchmarks |
| 26 | [[2604.25591v1]] | Walking Through Uncertainty: Uncertainty Estimation for Audio-Aware LLMs / 穿越不确定性：音频感知LLM的不确定性估计 | Evaluation & Benchmarks |
| 27 | [[2604.25634v1]] | The Surprising Universality of LLM Outputs: A Real-Time Verification Primitive / LLM输出的惊人普适性：实时验证基元 | Evaluation & Benchmarks |
| 28 | [[2604.25655v1]] | RAA-PINNs: Residual-loss Anomaly Analysis for Change-Point Detection in Dynamical Systems / RAA-PINNs：基于残差异常的动力系统变点检测 | Theory & Foundations |
| 29 | [[2604.25699v1]] | NVLLM: A 3D NAND-Centric Architecture for Edge on-Device LLM Inference / NVLLM：面向边缘端侧LLM推理的3D NAND中心架构 | Model Architecture & Deployment |
| 30 | [[2604.25724v1]] | Scalable Inference Architectures for Compound AI Systems: A Production Deployment Study / 复合AI系统的可扩展推理架构：生产部署研究 | Model Architecture & Deployment |
| 31 | [[2604.25733v1]] | Verification of Neural Networks (Lecture Notes) / 神经网络验证（讲义） | Theory & Foundations |
| 32 | [[2604.25765v1]] | Measuring the Sensitivity of Classification Models with the Error Sensitivity Profile / 用错误敏感性剖面测量分类模型的敏感性 | Evaluation & Benchmarks |
| 33 | [[2604.25779v1]] | Sustained Gradient Alignment Mediates Subliminal Learning in Multi-Step Setting / 持续梯度对齐在多步设置中中介潜意识学习 | Alignment & Safety |
| 34 | [[2604.25783v1]] | Subliminal Steering: Stronger Encoding of Hidden Signals / 潜意识引导：隐藏信号的更强编码 | Interpretability & Mech. Analysis |
| 35 | [[2604.25800v1]] | Barriers to Universal Reasoning With Transformers (And How to Overcome Them) / Transformer通用推理的障碍（及如何克服） | Theory & Foundations |
| 36 | [[2604.25845v1]] | Model-Agnostic Information Transfer and Fusion for Classification with Label Noise / 标签噪声分类的模型无关信息迁移与融合 | Training & Optimization |
| 37 | [[2604.25866v1]] | From Syntax to Emotion: A Mechanistic Analysis of Emotion Inference in LLMs / 从句法到情绪：LLM情绪推理的机制性分析 | Interpretability & Mech. Analysis |
| 38 | [[2604.25872v1]] | When Errors Can Be Beneficial: A Categorization of Imperfect Rewards for Policy Gradient / 当错误可能有益：策略梯度中不完美奖励的分类 | Reinforcement Learning |
| 39 | [[2604.25904v1]] | Teacher Forcing as Generalized Bayes: Optimization Geometry Mismatch in Switching Surrogates / 教师强制作为广义贝叶斯：切换代理中的优化几何失配 | Theory & Foundations |
| 40 | [[2604.25907v1]] | How Fast Should a Model Commit to Supervision? Training Reasoning Models on the Tsallis Loss Continuum / 模型应以多快速度承诺于监督？在Tsallis损失连续体上训练推理模型 | Reinforcement Learning |
