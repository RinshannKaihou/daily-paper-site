---
title: "Daily Paper Overview - 2025-04-21"
date: 2025-04-21
tags:
  - llm-interpretability
  - training-stability
  - inference-efficiency
  - hardware-systems
  - safety-evaluation
  - mathematical-foundations
  - model-cards
  - ai-policy
papers: 34
---

## 今日必读 / Must Read Today

### 1. [[2504.14871]] Natural Fingerprints of Large Language Models

**入选理由 / Why this paper:** 即使在完全相同的训练数据和架构下，仅因随机种子差异，LLM也会在输出中留下可被分类器识别的"自然指纹"。This paper reveals that training dynamics alone -- not just training data -- create identifiable patterns in LLM outputs, with profound implications for model provenance and accountability.

### 2. [[2504.15236]] Values in the Wild

**入选理由 / Why this paper:** Anthropic团队从30万条真实Claude对话中自下而上发现3307种AI价值观，首次构建了大规模实证AI价值观分类体系。The first large-scale empirical taxonomy of AI values from real-world deployment, revealing how abstract alignment principles manifest as thousands of specific contextual expressions.

### 3. [[2504.15471]] Bigram Subnetworks

**入选理由 / Why this paper:** 仅需约10M参数（不到总参数0.2%）的稀疏"bigram子网络"即可高精度复现Transformer的二元语法预测，揭示了语言模型的基础计算回路。Identifies a minimal, interpretable foundation circuit (~10M params, <0.2% of total) that is both sufficient for bigram predictions and critical for overall model performance.

---

## 按主题分类 / Papers by Topic

### Interpretability & Mechanistic Analysis / 可解释性与机制分析

| Paper | Title / 标题 | Summary / 摘要 |
|-------|-------------|----------------|
| [[2504.14871]] | Natural Fingerprints of LLMs / LLM的自然指纹 | 训练动态本身产生可识别的输出模式 / Training dynamics create identifiable output patterns distinguishable by classifiers |
| [[2504.15471]] | Bigram Subnetworks / 二元语法子网络 | ~10M参数的稀疏子网络复现bigram预测 / Sparse ~10M-param subnetworks suffice for bigram prediction in Transformers |
| [[2504.15473]] | Emergence of Concepts in Diffusion Models / 扩散模型中概念的涌现 | SAE揭示图像构图在去噪第一步即确定 / SAEs reveal image composition is fixed at the first denoising step |
| [[2504.16948]] | Intrinsic Barriers to Explaining DFMs / 深度基础模型可解释性的内在屏障 | 三大结构性屏障使完全机制化解释不可达 / Three intrinsic barriers make full mechanistic transparency unattainable |

### Training Stability & Optimization / 训练稳定性与优化

| Paper | Title / 标题 | Summary / 摘要 |
|-------|-------------|----------------|
| [[2504.14945]] | LUFFY / 混合策略GRPO推理框架 | 离策略推理轨迹+策略整形防止熵坍塌 / Off-policy traces + policy shaping prevent entropy collapse in RLVR |
| [[2504.15051]] | VeLU / 方差增强学习单元 | 基于输入方差动态调节的激活函数 / Variance-adaptive activation with W2 regularization for training stability |
| [[2504.15275]] | PURE / 最小式信用分配 | 最小式信用分配消除PRM引发的reward hacking / Min-form credit assignment eliminates PRM-induced reward hacking |
| [[2504.15399]] | L2O with Parameter Symmetries / 对称性增强的学习式优化器 | Teleportation局部近似牛顿法 / Teleportation locally approximates Newton's method in meta-optimization |
| [[2504.15432]] | LLM Annotations to BERT / LLM标注风险警示 | LLM伪标签导致小型分类器性能不稳定 / LLM-generated labels cause instability in fine-tuned encoder models |

### Inference Efficiency & Quantization / 推理效率与量化

| Paper | Title / 标题 | Summary / 摘要 |
|-------|-------------|----------------|
| [[2504.14915]] | StableQuant / 稳定量化 | 面向语音模型的逐层自适应PTQ / Layer-adaptive PTQ for speech foundation models with <0.3% WER degradation |
| [[2504.14992]] | PHD-Transformer / 高效预训练长度扩展 | 重复token+选择性KV cache实现长度扩展 / Token repetition with selective KV cache enables length scaling at no memory cost |
| [[2504.15364]] | KeyDiff / 基于Key相似度的KV cache驱逐 | 保留几何独特key实现近无损KV cache压缩 / Retaining geometrically distinctive keys achieves near-lossless KV cache eviction |
| [[2504.15475]] | ERSD / 指数竞赛投机解码 | 建立投机解码与信道模拟的信息论联系 / Establishes information-theoretic link between speculative decoding and channel simulation |

### Hardware & Systems / 硬件与系统

| Paper | Title / 标题 | Summary / 摘要 |
|-------|-------------|----------------|
| [[2504.14893]] | H2M2 / 异构内存LLM推理 | HBM+LPDDR非对称架构加速LLM推理 / Asymmetric HBM+LPDDR memory architecture achieves 1.46-2.94x LLM inference speedup |
| [[2504.14960]] | MoE Parallel Folding / MoE并行折叠 | 解耦Attention与MoE层并行策略 / Decoupled parallelism for attention and MoE layers reaches 49.3% MFU |
| [[2504.15377]] | SCALE-Sim v3 / 脉动阵列仿真器v3 | 延迟-带宽-功耗全系统端到端分析 / End-to-end systolic array simulation with DRAM, energy, and multi-core support |
| [[2504.15465]] | LithOS / GPU操作系统 | TPC粒度调度实现推理3x尾延迟降低 / TPC-granularity GPU scheduling achieves 3x tail latency reduction for inference |
| [[2505.00011]] | PFE Computing Survey / 印刷柔性电子计算综述 | 从IGZO-TFT到RISC-V柔性处理器的全栈综述 / Full-stack survey from IGZO-TFT fabrication to RISC-V flexible processors |
| [[2504.15021]] | OSML+ / 智能多维资源调度 | 三模型协作实现云环境多维资源调度 / Three-model ML system for multi-resource scheduling in cloud environments |

### Safety & Evaluation / 安全与评估

| Paper | Title / 标题 | Summary / 摘要 |
|-------|-------------|----------------|
| [[2504.14985]] | aiXamine / LLM安全评估平台 | 8维度40+基准评估50+个LLM安全漏洞 / 8-service 40+ benchmark evaluation revealing vulnerabilities in 50+ LLMs |
| [[2504.15236]] | Values in the Wild / 野生环境中的AI价值观 | 30万对话中发现的3307种AI价值观 / 3,307 AI values discovered from 308K real-world conversations |
| [[2504.15253]] | JETTS Benchmark / LLM-Judge测试时扩展评估 | Judge批判式优化失效的重要发现 / Sobering finding: judge-generated critiques fail to improve generator outputs |
| [[2504.15211]] | Bayesian GenAI Safety Evaluation / 贝叶斯生成式AI安全评估 | 多重性感知框架量化解码配置尾部风险 / Multiplicity-aware framework quantifies tail risks across decoding configurations |
| [[2504.15240]] | Conformalized-KANs / 共形预测KAN | 首个面向KAN的覆盖率保证UQ框架 / First conformal prediction UQ framework for KANs with coverage guarantees |
| [[2504.15360]] | Conformal IT2 Fuzzy / 共形区间二型模糊分类 | 模糊规则分类器的共形预测增强 / Conformal prediction with interval-type 2 fuzzy rule-based classifiers |
| [[2504.18565]] | RepliBench / 自主复制能力评估 | 86个任务评估LLM自主复制能力，当前模型尚不构成威胁 / 86-task evaluation of autonomous replication; models not yet a credible threat |

### Mathematical Foundations / 数学基础

| Paper | Title / 标题 | Summary / 摘要 |
|-------|-------------|----------------|
| [[2504.15208]] | Compute-Optimal Generalization / 计算最优泛化 | 证明Chinchilla缩放律下泛化界随规模收紧 / Proves generalization bounds tighten with scale under Chinchilla scaling |
| [[2504.15110]] | Res-KAN Besov Approximation / Res-KAN Besov逼近 | KAN的Besov空间最优逼近率与无维样本复杂度 / Optimal Besov approximation rates and dimension-free sample complexity for KANs |
| [[2504.15266]] | NTP Creativity Limits / NTP创造力极限 | Next-token预测在创造性任务中存在短视性 / NTP is myopic on creative tasks; multi-token approaches achieve 5x higher creativity |
| [[2504.15240]] | Conformalized-KANs / 共形预测KAN | KAN的共形预测不确定性量化 / Conformal prediction for KAN uncertainty quantification |

### Model Cards & Technical Reports / 模型卡与技术报告

| Paper | Title / 标题 | Summary / 摘要 |
|-------|-------------|----------------|
| [[2504.15431]] | Trillion-7B / Trillion-7B技术报告 | XLDA跨语言文档注意力实现高效韩语LLM / Cross-lingual document attention enables efficient Korean-centric multilingual LLM |
| [[2504.15027]] | DistilQwen2.5 / DistilQwen2.5蒸馏框架 | 两阶段黑盒+白盒蒸馏压缩Qwen系列 / Two-stage black-box + white-box KD for Qwen2.5 family (0.5B-7B) |
| [[2504.15477]] | IRPO / 上下文排序偏好优化 | 基于NDCG权重的Plackett-Luce偏好对齐 / NDCG-weighted Plackett-Luce preference optimization for LLM alignment |

### AI Policy & Governance / AI政策与治理

| Paper | Title / 标题 | Summary / 摘要 |
|-------|-------------|----------------|
| [[2504.15181]] | GPAI Code of Practice vs Industry / GPAI准则与行业对比 | 欧盟AI法案准则72项措施中52项已有行业先例 / 52 of 72 EU AI Act measures have strong industry precedent |
| [[2504.16138]] | Frontier AI Model Forecast / 前沿AI模型数量预测 | 预测2028年103-306个模型超过EU AI法案阈值 / Forecasts 103-306 models exceeding EU AI Act threshold by 2028 |

---

## All Papers

| # | arXiv ID | Title / 标题 | Topic / 主题 | Summary / 摘要 |
|---|----------|-------------|--------------|----------------|
| 1 | [[2504.14871]] | Natural Fingerprints of LLMs / LLM的自然指纹 | Interpretability / 可解释性 | 训练动态产生可识别的模型输出指纹 / Training dynamics create identifiable "natural fingerprints" in LLM outputs |
| 2 | [[2504.14893]] | H2M2 / 异构内存LLM推理 | Hardware / 硬件 | HBM+LPDDR非对称内存架构加速推理 / Asymmetric heterogeneous memory for 1.46-2.94x LLM inference speedup |
| 3 | [[2504.14915]] | StableQuant / 稳定量化 | Quantization / 量化 | 面向语音模型的逐层自适应后训练量化 / Layer-adaptive PTQ for speech models with <0.3% WER loss |
| 4 | [[2504.14945]] | LUFFY / 混合策略GRPO | Training / 训练 | 离策略推理轨迹+策略整形解决RLVR熵坍塌 / Off-policy guidance + policy shaping prevent entropy collapse in RLVR |
| 5 | [[2504.14960]] | MoE Parallel Folding / MoE并行折叠 | Systems / 系统 | 解耦Attention与MoE层并行策略达49.3% MFU / Decoupled parallelism achieves 49.3% MFU for MoE training |
| 6 | [[2504.14985]] | aiXamine / LLM安全评估平台 | Safety / 安全 | 8维度评估揭示50+个LLM安全漏洞 / 8-service evaluation reveals vulnerabilities in 50+ LLMs |
| 7 | [[2504.14992]] | PHD-Transformer / 高效预训练长度扩展 | Inference / 推理 | 重复token+选择性KV cache实现高效长度扩展 / Token repetition with selective KV cache for efficient length scaling |
| 8 | [[2504.15021]] | OSML+ / 智能多维资源调度 | Systems / 系统 | 三模型ML协作实现云环境多维资源调度 / Three-model ML collaboration for multi-resource cloud scheduling |
| 9 | [[2504.15027]] | DistilQwen2.5 / Qwen蒸馏框架 | Model Card / 模型卡 | 两阶段黑盒+白盒蒸馏压缩Qwen2.5系列 / Two-stage KD framework for Qwen2.5 (0.5B-7B) |
| 10 | [[2504.15051]] | VeLU / 方差增强激活函数 | Training / 训练 | 基于输入方差动态调节的激活函数 / Variance-adaptive activation function with W2 regularization |
| 11 | [[2504.15110]] | Res-KAN Besov Approximation / Res-KAN Besov逼近 | Math / 数学 | KAN的Besov最优逼近率与无维样本复杂度 / Optimal Besov rates and dimension-free sample complexity for Res-KANs |
| 12 | [[2504.15181]] | GPAI Code vs Industry / GPAI准则与行业对比 | Policy / 政策 | EU AI法案72项措施中52项已有行业先例 / 52/72 EU AI Act measures have strong industry precedent |
| 13 | [[2504.15208]] | Compute-Optimal Generalization / 计算最优泛化 | Math / 数学 | 证明Chinchilla缩放下泛化界随规模收紧 / Provable generalization improvement under Chinchilla scaling |
| 14 | [[2504.15211]] | Bayesian GenAI Safety / 贝叶斯生成式AI安全 | Safety / 安全 | 多重性感知框架量化解码配置的尾部风险 / Multiplicity-aware framework quantifying tail risks across decoding configs |
| 15 | [[2504.15236]] | Values in the Wild / 野生环境中的AI价值观 | Safety / 安全 | 30万对话中发现3307种AI价值观 / 3,307 AI values discovered from 308K real-world Claude conversations |
| 16 | [[2504.15240]] | Conformalized-KANs / 共形预测KAN | Math & Safety / 数学与安全 | 首个面向KAN的覆盖率保证UQ框架 / First UQ framework for KANs with conformal coverage guarantees |
| 17 | [[2504.15253]] | JETTS Benchmark / LLM-Judge评估基准 | Safety / 安全 | Judge批判式优化失效的重要发现 / Reveals judge-generated critiques fail to improve generator outputs |
| 18 | [[2504.15266]] | NTP Creativity Limits / NTP创造力极限 | Math / 数学 | Next-token预测在创造性任务中存在短视性 / NTP is myopic on creative tasks; multi-token approaches are 5x better |
| 19 | [[2504.15275]] | PURE / 最小式信用分配 | Training / 训练 | 最小式信用分配消除PRM引发的reward hacking / Min-form credit assignment eliminates PRM-induced reward hacking |
| 20 | [[2504.15360]] | Conformal IT2 Fuzzy / 共形区间二型模糊 | Safety / 安全 | 模糊规则分类器的共形预测增强 / Conformal prediction enhanced by interval-type 2 fuzzy classifiers |
| 21 | [[2504.15364]] | KeyDiff / Key相似度KV cache驱逐 | Inference / 推理 | 保留几何独特key实现近无损KV cache压缩 / Geometrically distinctive key retention for near-lossless KV cache eviction |
| 22 | [[2504.15377]] | SCALE-Sim v3 / 脉动阵列仿真器v3 | Hardware / 硬件 | 延迟-带宽-功耗全系统端到端脉动阵列仿真 / End-to-end systolic array simulation with DRAM, energy, multi-core |
| 23 | [[2504.15399]] | L2O Symmetry / 对称性增强L2O | Training / 训练 | Teleportation局部近似牛顿法的理论分析 / Theoretical analysis: teleportation locally approximates Newton's method |
| 24 | [[2504.15431]] | Trillion-7B / Trillion-7B技术报告 | Model Card / 模型卡 | XLDA跨语言注意力实现高效韩语LLM / Cross-lingual document attention for Korean-centric multilingual LLM |
| 25 | [[2504.15432]] | LLM Annotations Risk / LLM标注风险 | Training / 训练 | LLM伪标签导致小型分类器不稳定 / LLM-generated pseudo-labels degrade and destabilize fine-tuned classifiers |
| 26 | [[2504.15465]] | LithOS / GPU操作系统 | Hardware / 硬件 | TPC粒度GPU调度实现推理3x尾延迟降低 / TPC-granularity GPU OS scheduling for 3x tail latency reduction |
| 27 | [[2504.15471]] | Bigram Subnetworks / 二元语法子网络 | Interpretability / 可解释性 | ~10M参数稀疏子网络复现bigram预测 / Sparse ~10M-param subnetworks sufficient for bigram predictions |
| 28 | [[2504.15473]] | Diffusion Concept Emergence / 扩散模型概念涌现 | Interpretability / 可解释性 | SAE揭示构图在去噪第一步即确定 / SAEs reveal composition is fixed at the first denoising step |
| 29 | [[2504.15475]] | ERSD / 指数竞赛投机解码 | Inference / 推理 | 建立投机解码与信道模拟的信息论联系 / Information-theoretic link between speculative decoding and channel simulation |
| 30 | [[2504.15477]] | IRPO / 上下文排序偏好优化 | Model Card / 模型卡 | NDCG权重的Plackett-Luce偏好对齐 / NDCG-weighted Plackett-Luce preference optimization for LLM ranking |
| 31 | [[2504.16138]] | Frontier Model Forecast / 前沿模型数量预测 | Policy / 政策 | 预测2028年103-306个模型超过EU AI法案阈值 / Forecasts 103-306 models exceeding EU AI Act threshold by 2028 |
| 32 | [[2504.16948]] | Intrinsic Barriers to Explainability / 可解释性内在屏障 | Interpretability / 可解释性 | 三大结构性屏障使完全解释不可达 / Three intrinsic barriers make full mechanistic transparency unattainable |
| 33 | [[2505.00011]] | PFE Computing Survey / 印刷柔性电子综述 | Hardware / 硬件 | 从IGZO-TFT到RISC-V柔性处理器的全栈综述 / Full-stack survey from flexible electronics to RISC-V processors |
| 34 | [[2504.18565]] | RepliBench / 自主复制能力评估 | Safety / 安全 | 86任务评估LLM自主复制能力，当前尚不构成威胁 / 86-task suite evaluating autonomous replication; no model poses credible threat yet |
