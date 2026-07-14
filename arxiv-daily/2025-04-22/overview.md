---
title: "ArXiv Daily Papers - 2025-04-22 / ArXiv 每日论文 - 2025年4月22日"
date: 2025-04-22
tags: [arxiv, daily-papers, LLM, interpretability, training-dynamics, mathematical-foundations]
papers: 50
---

> **Note / 注意**: All summaries in this overview are **abstract-only** (⚠️ Abstract-only) due to API rate limits. Full critical assessments require reading the complete papers.
> 本概述中所有摘要均为**仅基于论文摘要**生成，受限于API调用频率。完整的批判性评估需阅读全文。

---

## 今日必读 / Must Read Today

Top picks ranked by relevance score (5/5), selected from 674 candidates.

### 1. [[2504.14496v1]] Functional Abstraction of Knowledge Recall in LLMs
**Relevance: 5/5**
- **EN**: Proposes that during knowledge recall, LLM hidden activation space entails a function execution process where activation vectors align with functional components (Input argument, Function body, Return values). Directly relevant to hidden states and mechanistic interpretability.
- **CN**: 提出在知识回忆过程中，LLM隐藏激活空间隐含函数执行过程，激活向量与功能组件（输入参数、函数体、返回值）对齐。直接关联隐藏状态与机制可解释性。

### 2. [[2504.15471v3]] Bigram Subnetworks: Mapping to Next Tokens in Transformer LMs
**Relevance: 5/5**
- **EN**: Identifies minimal subnetworks (less than 0.2% of parameters) responsible for bigram next-token predictions in Transformer LMs up to 1B parameters, concentrated in the first MLP layer. Core mechanistic interpretability work.
- **CN**: 在高达1B参数的Transformer语言模型中，识别出负责二元语法下一token预测的最小子网络（不足0.2%参数），集中于第一层MLP。核心机制可解释性研究。

### 3. [[2504.15208v1]] Compute-Optimal LLMs Provably Generalize Better With Scale
**Relevance: 5/5**
- **EN**: Develops novel Freedman-type generalization bounds for LLMs in the compute-optimal (Chinchilla) regime, showing larger models have smaller generalization gaps due to decreased loss variance and quantization error.
- **CN**: 为计算最优（Chinchilla）体制下的LLM开发了新型Freedman型泛化界，证明更大模型因损失方差和量化误差降低而具有更小泛化差距。

### 4. [[2504.16084v3]] TTRL: Test-Time Reinforcement Learning
**Relevance: 5/5**
- **EN**: Introduces TTRL, a method for training LLMs with RL on unlabeled data using majority voting as reward. Boosts Qwen-2.5-Math-7B pass@1 by ~211% on AIME 2024 with only unlabeled test data.
- **CN**: 提出TTRL，利用多数投票作为奖励在无标签数据上用RL训练LLM。仅用无标签测试数据将Qwen-2.5-Math-7B在AIME 2024上的pass@1提升约211%。

### 5. [[2504.15956v2]] Universal Approximation with Softmax Attention
**Relevance: 5/5**
- **EN**: Proves that two-layer self-attention and one-layer self-attention followed by softmax are universal approximators for continuous sequence-to-sequence functions, without relying on feed-forward networks.
- **CN**: 证明两层自注意力和一层自注意力加softmax是连续序列到序列函数的通用逼近器，无需依赖前馈网络。

---

## 按主题分类 / Papers by Topic

### Mechanistic Interpretability & Hidden States / 机制可解释性与隐藏状态 (12 papers)

| ArXiv ID | Title / 标题 | Relevance | Key Insight / 关键洞见 |
|----------|-------------|-----------|----------------------|
| [[2504.14496v1]] | Functional Abstraction of Knowledge Recall in LLMs / LLM中知识回忆的功能抽象 | 5 | Hidden activation space as function execution / 隐藏激活空间即函数执行过程 |
| [[2504.15471v3]] | Bigram Subnetworks / 二元语法子网络 | 5 | Minimal subnetworks for next-token prediction / 下一token预测的最小子网络 |
| [[2504.14492v2]] | FairSteer: Inference Time Debiasing / FairSteer推理时去偏 | 4 | Activation steering for fairness / 激活导向实现公平性 |
| [[2504.14640v1]] | Risk Assessment via Internal States / 基于内部状态的风险评估 | 4 | LLM internal states for code risk assessment / LLM内部状态用于代码风险评估 |
| [[2504.14766v1]] | Disentangling Linguistic Features / 解耦语言特征 | 4 | Dimension-wise analysis of BERT embeddings / BERT嵌入的逐维分析 |
| [[2504.15630v1]] | CaLE: Context-aware Layer Enhancement / 上下文感知层增强 | 4 | V-usable information for layer enhancement / V可用信息驱动的层增强 |
| [[2504.16053v1]] | LongMamba / 长程Mamba | 4 | Local vs global hidden channels in Mamba / Mamba中局部与全局隐藏通道 |
| [[2504.15473v2]] | Interpretable Concepts in Diffusion Models / 扩散模型中的可解释概念 | 4 | SAE-based concept emergence during denoising / SAE揭示去噪中概念涌现 |
| [[2504.15133v3]] | EasyEdit2: Steering Framework / EasyEdit2模型导向框架 | 3 | Plug-and-play steering vectors / 即插即用导向向量 |
| [[2504.14871v2]] | Natural Fingerprints of LLMs / LLM的自然指纹 | 4 | Training dynamics create distinguishable outputs / 训练动态产生可区分输出 |
| [[2504.16948v1]] | Intrinsic Barriers to Explaining DFMs / 深度基础模型解释的固有障碍 | 4 | Fundamental limits of model interpretability / 模型可解释性的根本限制 |
| [[2504.15758v2]] | Observability in Neural State-Space Models / 神经状态空间模型可观测性 | 4 | Observability conditions for Mamba / Mamba可观测性条件 |

### Mathematical Foundations / 数学基础 (12 papers)

| ArXiv ID | Title / 标题 | Relevance | Key Insight / 关键洞见 |
|----------|-------------|-----------|----------------------|
| [[2504.15208v1]] | Compute-Optimal LLMs Generalization / 计算最优LLM泛化 | 5 | Freedman-type bounds for scaling laws / Freedman型缩放定律界 |
| [[2504.15956v2]] | Universal Approximation with Softmax Attention / Softmax注意力的通用逼近 | 5 | Attention alone suffices as universal approximator / 仅注意力即为通用逼近器 |
| [[2507.12469v1]] | Perfect diffusion is TC^0 / 完美扩散属于TC^0 | 5 | Complexity dichotomy for diffusion models / 扩散模型复杂度二分法 |
| [[2504.14697v2]] | Quantitative Clustering in Mean-Field Transformers / 均值场Transformer定量聚类 | 4 | Exponential clustering rates / 指数聚类收敛率 |
| [[2504.14701v1]] | Parameter Magnitudes & Hessian Eigenspaces / 参数幅度与Hessian特征空间 | 4 | Large parameters align with high curvature / 大参数对齐高曲率方向 |
| [[2504.14728v3]] | Geometric Learning Dynamics / 几何学习动态 | 4 | Three regimes: quantum, efficient, equilibration / 三种体制：量子、高效、平衡 |
| [[2504.14762v2]] | Combinatorial Theory of Dropout / Dropout组合理论 | 4 | Random walk over subnetwork graph / 子网络图上的随机游走 |
| [[2504.14514v1]] | Dimension-Free Transformer via STP / 基于STP的无维Transformer | 3 | Semi-tensor product for arbitrary dimensions / 半张量积处理任意维度 |
| [[2504.15110v3]] | Approximation Rates for KANs / KAN逼近速率 | 3 | Optimal Besov approximation rates / 最优Besov逼近速率 |
| [[2504.14882v2]] | Optimizers and Group Fairness / 优化器与群组公平性 | 3 | SDE analysis: adaptive optimizers fairer / SDE分析：自适应优化器更公平 |
| [[2504.14814v4]] | Error Diffusion Learning Algorithm / 误差扩散学习算法 | 3 | Diagnostic evaluation vs backpropagation / 对比反向传播的诊断评估 |
| [[2504.16275v2]] | Quantum Doubly Stochastic Transformers / 量子双随机Transformer | 4 | Quantum circuits for doubly stochastic attention / 量子电路实现双随机注意力 |

### Training Dynamics & Optimization / 训练动态与优化 (11 papers)

| ArXiv ID | Title / 标题 | Relevance | Key Insight / 关键洞见 |
|----------|-------------|-----------|----------------------|
| [[2504.16084v3]] | TTRL: Test-Time RL / 测试时强化学习 | 5 | RL on unlabeled data via majority voting / 多数投票实现无标签RL |
| [[2504.14838v1]] | Reliability Metrics for Reward Models / 奖励模型可靠性度量 | 5 | RETA metric for RM reliability / RETA度量评估RM可靠性 |
| [[2504.15777v1]] | Tina: Tiny Reasoning via LoRA / Tina: 通过LoRA实现微型推理 | 4 | $9 USD training for competitive reasoning / 9美元训练达到竞争性推理 |
| [[2504.16041v1]] | Muon Optimizer Accelerates Grokking / Muon优化器加速顿悟 | 4 | Grokking epoch reduced by 33% / 顿悟轮次降低33% |
| [[2504.15895v3]] | Dynamic Early Exit in Reasoning / 推理中的动态早退 | 4 | Confidence-based CoT truncation / 基于置信度的CoT截断 |
| [[2504.14519v1]] | SlimPipe: Pipeline Parallelism / SlimPipe流水线并行 | 4 | Near-zero memory overhead for long context / 长上下文近零内存开销 |
| [[2504.15051v2]] | VeLU: Variance-enhanced Learning Unit / 方差增强学习单元 | 3 | Variance-aware activation function / 方差感知激活函数 |
| [[2504.14945v5]] | LUFFY: Off-Policy Guidance for RLVR / LUFFY: RLVR离策略指导 | 3 | Off-policy traces break on-policy limits / 离策略轨迹突破同策略限制 |
| [[2504.14597v1]] | a1: Environment Augmented Generation / a1: 环境增强生成 | 3 | Test-time scaling via environment feedback / 通过环境反馈实现测试时缩放 |
| [[2504.14662v1]] | Sharpness-Aware Fine-Tuning for Merging / 锐度感知微调用于合并 | 3 | SAM for model merging / SAM用于模型合并 |
| [[2504.14893v1]] | Heterogeneous Memory for LLM Inference / LLM推理异构内存 | 3 | Asymmetric memory architecture / 非对称内存架构 |

### Model Compression & Efficiency / 模型压缩与效率 (6 papers)

| ArXiv ID | Title / 标题 | Relevance | Key Insight / 关键洞见 |
|----------|-------------|-----------|----------------------|
| [[2504.14915v1]] | StableQuant for Speech Models / 语音模型StableQuant | 4 | Layer-adaptive post-training quantization / 层自适应训练后量化 |
| [[2504.14569v5]] | NoWag: Shape Preserving Compression / NoWag: 保形压缩 | 3 | Unified VQ and pruning framework / 统一向量量化与剪枝框架 |
| [[2504.14772v2]] | KD & Dataset Distillation Survey / 知识蒸馏与数据集蒸馏综述 | 3 | Comprehensive KD+DD for LLMs / LLM知识蒸馏+数据集蒸馏综合综述 |
| [[2504.15027v1]] | DistilQwen2.5 / 蒸馏Qwen2.5 | 3 | Industrial multi-agent distillation / 工业多智能体蒸馏 |
| [[2504.14992v2]] | PHD-Transformer: Length Scaling / PHD-Transformer: 长度缩放 | 3 | Efficient KV cache for length scaling / 高效KV缓存实现长度缩放 |
| [[2504.14667v2]] | Split Federated Learning for LLMs / LLM分割联邦学习 | 3 | LoRA-based split FL framework / 基于LoRA的分割联邦学习 |

### Reliability, Safety & Alignment / 可靠性、安全与对齐 (6 papers)

| ArXiv ID | Title / 标题 | Relevance | Key Insight / 关键洞见 |
|----------|-------------|-----------|----------------------|
| [[2504.14798v1]] | Verifying Robust Unlearning / 验证鲁棒遗忘 | 3 | Adversarial probing for residual knowledge / 对抗性探测残余知识 |
| [[2504.14520v1]] | Meta-Thinking via MARL Survey / 多智能体RL元思维综述 | 3 | Multi-agent architectures for introspection / 多智能体架构实现内省 |
| [[2504.14545v1]] | TrustLoRA for Failure Detection / TrustLoRA失败检测 | 3 | LoRA for OOD failure detection / LoRA用于分布外失败检测 |
| [[2504.15181v2]] | EU AI Act vs Industry Practices / 欧盟AI法案与行业实践 | 3 | Mapping safety measures to industry / 安全措施映射行业实践 |
| [[2504.15210v2]] | Symbolic Execution for Code LLMs / 代码LLM符号执行 | 3 | Symbolic execution for reward model training / 符号执行用于奖励模型训练 |
| [[2504.15240v1]] | Conformalized-KANs / 保形KAN | 3 | Conformal prediction for KANs / KAN的保形预测 |

### Continual Learning & Adaptation / 持续学习与适应 (3 papers)

| ArXiv ID | Title / 标题 | Relevance | Key Insight / 关键洞见 |
|----------|-------------|-----------|----------------------|
| [[2504.14727v1]] | Semi-parametric Memory Consolidation / 半参数记忆巩固 | 3 | Biomimetic continual learning / 仿生持续学习 |
| [[2504.14677v1]] | Temporal Plasticity in Foundation Models / 基础模型时间可塑性 | 3 | Incremental fine-tuning evaluation / 增量微调评估 |
| [[2504.14854v2]] | UQ via Langevin Sampling / Langevin采样不确定性量化 | 3 | Scalable hypernetwork inference / 可扩展超网络推断 |

---

## All Papers

| ArXiv ID | Title / 标题 | Relevance | Categories |
|----------|-------------|-----------|------------|
| [[2504.14496v1]] | Functional Abstraction of Knowledge Recall / 知识回忆的功能抽象 | 5 | cs.CL |
| [[2504.14838v1]] | Reliability Metrics for Reward Models / 奖励模型可靠性度量 | 5 | cs.AI |
| [[2504.15208v1]] | Compute-Optimal LLMs Generalization / 计算最优LLM泛化 | 5 | cs.LG, cs.AI |
| [[2504.15471v3]] | Bigram Subnetworks / 二元语法子网络 | 5 | cs.CL |
| [[2504.15956v2]] | Universal Approximation with Softmax Attention / Softmax注意力通用逼近 | 5 | cs.LG, cs.AI, stat.ML |
| [[2504.16084v3]] | TTRL: Test-Time RL / 测试时强化学习 | 5 | cs.CL, cs.LG |
| [[2507.12469v1]] | Perfect diffusion is TC^0 / 完美扩散属于TC^0 | 5 | cs.CC, cs.CL, cs.LG |
| [[2504.14492v2]] | FairSteer: Inference Time Debiasing / FairSteer推理时去偏 | 4 | cs.CL |
| [[2504.14519v1]] | SlimPipe: Pipeline Parallelism / SlimPipe流水线并行 | 4 | cs.LG, cs.AI |
| [[2504.14640v1]] | Risk Assessment via Internal States / 内部状态风险评估 | 4 | cs.SE, cs.AI, cs.CL |
| [[2504.14697v2]] | Quantitative Clustering in Mean-Field Transformers / 均值场Transformer定量聚类 | 4 | cs.LG, math.AP, math.DS, stat.ML |
| [[2504.14701v1]] | Parameter Magnitudes & Hessian Eigenspaces / 参数幅度与Hessian特征空间 | 4 | cs.LG, stat.ML |
| [[2504.14728v3]] | Geometric Learning Dynamics / 几何学习动态 | 4 | cs.LG, q-bio.PE, quant-ph |
| [[2504.14762v2]] | Combinatorial Theory of Dropout / Dropout组合理论 | 4 | cs.LG, cs.AI |
| [[2504.14766v1]] | Disentangling Linguistic Features / 解耦语言特征 | 4 | cs.CL |
| [[2504.14871v2]] | Natural Fingerprints of LLMs / LLM自然指纹 | 4 | cs.CL |
| [[2504.14915v1]] | StableQuant for Speech Models / 语音模型StableQuant | 4 | eess.AS, cs.AI |
| [[2504.15473v2]] | Interpretable Concepts in Diffusion / 扩散模型可解释概念 | 4 | cs.CV, cs.LG, eess.IV |
| [[2504.15630v1]] | CaLE: Layer Enhancement / 上下文感知层增强 | 4 | cs.CL |
| [[2504.15758v2]] | Observability in Neural State-Space / 神经状态空间可观测性 | 4 | cs.LG, eess.SY, math.DS, math.OC |
| [[2504.15777v1]] | Tina: Tiny Reasoning via LoRA / 微型LoRA推理 | 4 | cs.CL, cs.AI, cs.LG |
| [[2504.15895v3]] | Dynamic Early Exit / 动态早退 | 4 | cs.CL, cs.AI |
| [[2504.16041v1]] | Muon Optimizer Accelerates Grokking / Muon优化器加速顿悟 | 4 | cs.LG, cs.AI |
| [[2504.16053v1]] | LongMamba / 长程Mamba | 4 | cs.CL, cs.AI |
| [[2504.16275v2]] | Quantum Doubly Stochastic Transformers / 量子双随机Transformer | 4 | cs.LG, cs.AI, cs.CE, cs.CV |
| [[2504.16948v1]] | Intrinsic Barriers to Explaining DFMs / 解释DFM的固有障碍 | 4 | cs.CY, cs.AI, cs.ET |
| [[2504.14514v1]] | Dimension-Free Transformer via STP / 基于STP无维Transformer | 3 | cs.LG, cs.AI, eess.SY |
| [[2504.14520v1]] | Meta-Thinking via MARL Survey / 多智能体RL元思维综述 | 3 | cs.AI, cs.CL |
| [[2504.14545v1]] | TrustLoRA for Failure Detection / TrustLoRA失败检测 | 3 | cs.LG |
| [[2504.14569v5]] | NoWag: Shape Preserving Compression / NoWag保形压缩 | 3 | cs.LG, cs.AI |
| [[2504.14597v1]] | a1: Environment Augmented Generation / a1环境增强生成 | 3 | cs.CL |
| [[2504.14662v1]] | Sharpness-Aware Fine-Tuning for Merging / 锐度感知微调合并 | 3 | cs.LG, cs.CV |
| [[2504.14667v2]] | Split Federated Learning for LLMs / LLM分割联邦学习 | 3 | cs.LG, cs.NI |
| [[2504.14677v1]] | Temporal Plasticity in Foundation Models / 基础模型时间可塑性 | 3 | cs.LG, cs.AI |
| [[2504.14727v1]] | Semi-parametric Memory Consolidation / 半参数记忆巩固 | 3 | cs.LG, cs.AI, cs.CV |
| [[2504.14772v2]] | KD & Dataset Distillation Survey / 知识蒸馏与数据集蒸馏综述 | 3 | cs.CL, cs.LG, stat.ML |
| [[2504.14798v1]] | Verifying Robust Unlearning / 验证鲁棒遗忘 | 3 | cs.LG, cs.CV |
| [[2504.14814v4]] | Error Diffusion Learning Algorithm / 误差扩散学习算法 | 3 | cs.LG |
| [[2504.14854v2]] | UQ via Langevin Sampling / Langevin采样不确定性量化 | 3 | cs.LG, stat.ML |
| [[2504.14882v2]] | Optimizers and Group Fairness / 优化器与群组公平性 | 3 | cs.LG, cs.CV, stat.ML |
| [[2504.14893v1]] | Heterogeneous Memory for LLM Inference / LLM推理异构内存 | 3 | cs.AR |
| [[2504.14945v5]] | LUFFY: Off-Policy Guidance / LUFFY离策略指导 | 3 | cs.LG, cs.AI, cs.CL |
| [[2504.14992v2]] | PHD-Transformer: Length Scaling / PHD-Transformer长度缩放 | 3 | cs.CL |
| [[2504.15027v1]] | DistilQwen2.5 / 蒸馏Qwen2.5 | 3 | cs.CL |
| [[2504.15051v2]] | VeLU: Variance-enhanced Learning Unit / 方差增强学习单元 | 3 | cs.LG, cs.AI, cs.CV |
| [[2504.15110v3]] | Approximation Rates for KANs / KAN逼近速率 | 3 | cs.LG, cs.NE, math.FA, math.NA, stat.ML |
| [[2504.15133v3]] | EasyEdit2: Steering Framework / EasyEdit2导向框架 | 3 | cs.CL, cs.AI, cs.CV, cs.HC, cs.LG |
| [[2504.15181v2]] | EU AI Act vs Industry Practices / 欧盟AI法案与行业实践 | 3 | cs.CY, cs.AI |
| [[2504.15210v2]] | Symbolic Execution for Code LLMs / 代码LLM符号执行 | 3 | cs.SE, cs.AI |
| [[2504.15240v1]] | Conformalized-KANs / 保形KAN | 3 | cs.LG |
