---
title: "Daily Paper Overview — 2026-05-25"
date: 2026-05-25
tags:
  - daily-overview
  - arxiv
  - mechanistic-interpretability
  - llm-evaluation
  - inference-optimization
  - training-stability
  - automated-research
papers: 47
---

## 今日必读 / Must Read Today

### 1. [[2605.26099]] Language Models Need Sleep

> **推荐理由 / Reason:** 提出类"睡眠"整合机制，在上下文窗口满时通过多轮离线循环将KV缓存信息压缩到SSM快速权重中，巧妙地将额外计算与推理延迟解耦。概念优雅，实验设计严谨（从元胞自动机到数学推理的递进），对长上下文推理的架构设计有深远启示。
>
> A biologically-inspired sleep consolidation mechanism that decouples extra compute from inference latency via iterative fast-weight refinement in SSM blocks. Elegant concept, rigorous experimental ladder from synthetic to realistic tasks, with significant implications for long-context reasoning architectures.

### 2. [[2605.26097]] Forgetting in Language Models: Capacity, Optimization, and Self-Generated Replay

> **推荐理由 / Reason:** 系统性地揭示了灾难性遗忘的容量瓶颈——过度训练的小模型即使有正则化也无法避免遗忘，而自生成回放数据可替代真实预训练数据并打破学习率-遗忘权衡。实验简洁有力，对LLM持续学习的实践有直接指导意义。
>
> Systematic dissection showing overtrained small models cannot avoid forgetting regardless of regularization, while self-generated replay breaks the LR-forgetting tradeoff. Clean, impactful experiments with direct practical implications for continual LLM finetuning.

### 3. [[2605.25507]] Credit Assignment with Resets in Language Model Reasoning

> **推荐理由 / Reason:** SRPO通过自定位首个错误推理步骤并重采样后续推理，在无需外部步骤监督的情况下持续超越GRPO，在10个推理基准和LiveCodeBench上收敛速度快2-3倍。方法简单直接，效果显著，有望成为RL后训练的新标准。
>
> SRPO self-localizes the first erroneous reasoning step and resamples continuations, consistently outperforming GRPO across 10 benchmarks with 2-3× faster convergence on coding tasks — all without external step-level supervision. Simple, effective, and poised to become a new standard for RL post-training.

---

## 按主题分类 / Papers by Topic

### 系统与基础设施 / Systems & Infrastructure

| Paper | 描述 / Description |
|-------|-------------------|
| [[2605.19169]] | 光纤延迟对地理分布式AI训练的影响 / Impact of fiber latency on geo-distributed AI training |
| [[2605.19775]] | LLM推理扩展瓶颈分析 / Inference scaling bottlenecks for LLMs on GPU clusters |
| [[2605.22416]] | 混合Mamba-Transformer非对称虚拟内存分页 / Asymmetric virtual memory paging for hybrid Mamba-Transformer |
| [[2605.23918]] | GPU模型常驻能耗（"停车税"）/ Hidden energy cost of always-on GPU model deployment |
| [[2605.24022]] | 频域引导的自适应KV缓存复用 / Frequency-guided adaptive KV cache reuse for long-context serving |
| [[2605.24461]] | 150MW/83K GPU数据中心端到端功率管理 / End-to-end power management for a +100MW AI cluster |
| [[2605.26099]] | 语言模型"睡眠"机制：KV缓存到SSM快速权重整合 / Sleep-like consolidation for LLMs: KV cache to SSM fast weights |

### 量化与硬件 / Quantization & Hardware

| Paper | 描述 / Description |
|-------|-------------------|
| [[2605.24144]] | EVA：向量量化硬件加速LLM解码 / EVA: Vector quantization hardware for accelerated LLM decoding |
| [[2605.24391]] | MX-SAFE自适应微缩放格式 / Versatile microscaling format with on-the-fly bit allocation |
| [[2605.24665]] | Posit数制统一近似乘除法单元 / Energy-efficient approximate posit multiply-divide unit |
| [[2605.25880]] | 残差自由Transformer的量化优势 / Quantization benefits of residual-free transformers |
| [[2605.25966]] | 量化感知训练中学习率调度与位宽的关系 / Schedule × bit-width boundary in quantization-aware training |
| [[2605.26092]] | OrpQuant：正交残差投影乘法器免费量化 / Geometric orthogonal residual projection for multiplier-free PoT quantization |

### 强化学习与对齐 / Reinforcement Learning & Alignment

| Paper | 描述 / Description |
|-------|-------------------|
| [[2605.25507]] | 重置机制改善推理信用分配（SRPO）/ Reset-based credit assignment for reasoning (SRPO) |
| [[2605.25604]] | DVAO：多奖励RL中方差自适应优势优化 / Dynamic variance-adaptive advantage optimization for multi-reward RL |
| [[2605.25739]] | 行为可信度不可能三角 / Behavioral Credibility Trilemma: calibrated autonomy impossibility |
| [[2605.26037]] | 知识图谱工具调用的峰崩现象与四通道信号理论 / Peak-then-collapse and four interface channels of KG tool use |
| [[2605.25698]] | 高质量数据最优调度策略（DSR）/ Optimal data scheduling via quality-aware scaling laws (DSR) |

### 奖励模型与偏好学习 / Reward Models & Preference Learning

| Paper | 描述 / Description |
|-------|-------------------|
| [[2605.24749]] | 神经奖励模型的特征学习机制 / How neural reward models learn features under single-index analysis |
| [[2605.25629]] | 弱到强奖励模型的分布外迁移脆弱性 / Weak-to-strong reward models fail under preference shift (ANCHOR) |
| [[2605.25988]] | 医学RAG中检查器的信号坍塌与奖励黑客 / Signal collapse and reward hacking in checker-guided medical RAG |

### 可解释性与机制分析 / Interpretability & Mechanistic Analysis

| Paper | 描述 / Description |
|-------|-------------------|
| [[2605.25151]] | 表征不等于控制：实现效应测试 / Representation without control: realization effect in LLMs |
| [[2605.25520]] | LLM是否编码语义操作子空间 / Whether LLMs encode distinct semantic operation subspaces |
| [[2605.25603]] | CIE-Scorer检测不忠实CoT推理 / Circuit-guided detection of unfaithful chain-of-thought |
| [[2605.25619]] | Transformer层与幂迭代法的类比 / Analogies between transformer layers and power method |
| [[2605.25848]] | 几何演化图提取稳定概念探针 / Geometric Evolution Maps for stable concept probes from residual streams |
| [[2605.25891]] | Causal Tongue-Tie：LLM知道但说不出来 / LLMs encode causal direction but outputs fail to express it |
| [[2605.25903]] | UAV：跨模型通用激活解释框架 / Universal activation verbalizer for cross-model explanation |
| [[2605.26045]] | 激活预言机的置信度校准 / Confidence and calibration of activation oracles |

### 因果推断 / Causal Inference

| Paper | 描述 / Description |
|-------|-------------------|
| [[2605.24076]] | 因果推断是AI的统计良知 / Causality as the statistical conscience of AI |
| [[2605.25998]] | 因果方法用于LLM开发与评估（KDD Blue Sky）/ Causal methods for LLM development and evaluation |

### 基准评测与评估 / Benchmarking & Evaluation

| Paper | 描述 / Description |
|-------|-------------------|
| [[2605.25272]] | AI基准生态系统的心理测量学分析 / Psychometric mapping of AI benchmark ecosystems |
| [[2605.25997]] | 部署完备基准测试框架 / Deployment-complete benchmarking framework |
| [[2605.26046]] | 多目标提示优化的梯度冲突失败模式 / Gradient collision failure modes in multi-objective prompt optimization |
| [[2605.26079]] | 自动化基准审计框架（ABA）/ Automated benchmark auditing for AI agents and LLMs |

### 安全与隐私 / Safety & Privacy

| Paper | 描述 / Description |
|-------|-------------------|
| [[2605.24817]] | RouteScan：非侵入式MoE安全审计 / Non-intrusive MoE safety audit via expert routing telemetry |
| [[2605.25893]] | D²-Monitor：扩散LLM动态安全监控 / Dynamic safety monitoring for diffusion LLMs |
| [[2605.25902]] | 对比解码差异法恢复微调植入内容 / Verbatim content recovery via contrastive decoding diffing |

### 神经网络理论 / Neural Network Theory

| Paper | 描述 / Description |
|-------|-------------------|
| [[2605.24710]] | μP下宽神经网络的特征学习 / Feature learning in wide networks under μP: mean-field limit |
| [[2605.25234]] | 过参数化网络的认知不确定性 / Epistemic uncertainty in overparametrized neural networks |
| [[2605.25674]] | 逐层Hessian迹随机估计用于训练监控 / Stochastic layer-wise Hessian trace for training monitoring |
| [[2605.25939]] | 最小MLP中的可解释特化 / Explainable specialization in minimal MLPs |

### 训练优化与架构 / Training Optimization & Architecture

| Paper | 描述 / Description |
|-------|-------------------|
| [[2605.25704]] | PowLU激活函数消除LLM训练loss spike / PowLU activation for stable LLM pretraining |
| [[2605.26097]] | 语言模型遗忘：容量、优化与自生成回放 / Forgetting in LMs: capacity, optimization, self-generated replay |
| [[2605.25991]] | Fuzzy PyTorch：数值变异性快速评估 / Rapid numerical variability evaluation for deep learning models |

### 应用与工具 / Applications & Tools

| Paper | 描述 / Description |
|-------|-------------------|
| [[2605.25658]] | AutoSG：LLM自动生成优化求解器 / LLM-driven solver generation from task prompts |
| [[2605.25799]] | 跨域小样本学习中的注意力汇聚加剧 / Exacerbated attention sink in cross-domain few-shot learning |

---

## All Papers

| # | ID | Title (EN) | 标题 (ZH) |
|---|-----|-----------|----------|
| 1 | [[2605.19169]] | Modeling the Impact of Fiber Latency on Compute-Communication Overlap in Geo-Distributed Multi-Datacenter AI Training | 光纤延迟对地理分布式AI训练计算通信重叠的影响建模 |
| 2 | [[2605.19775]] | Understanding Inference Scaling for LLMs: Bottlenecks, Trade-offs, and Performance Principles | LLM推理扩展性理解：瓶颈、权衡与性能原则 |
| 3 | [[2605.22416]] | Asymmetric Virtual Memory Paging for Hybrid Mamba-Transformer Inference | 混合Mamba-Transformer推理的非对称虚拟内存分页 |
| 4 | [[2605.23918]] | The Model Parking Tax: Quantifying the Hidden Energy Cost of Always-On GPU Model Deployment | 模型停车税：GPU常驻部署隐藏能耗量化 |
| 5 | [[2605.24022]] | Adaptive KV Cache Reuse for Fast Long-Context LLM Serving | 面向快速长上下文LLM服务的自适应KV缓存复用 |
| 6 | [[2605.24076]] | Causality as the Statistical Conscience of AI: From Pearl's Ladder to Trustworthy Machines | 因果推断作为AI的统计良知：从Pearl阶梯到可信机器 |
| 7 | [[2605.24144]] | EVA: Accelerating LLM Decoding via an Efficient Vector Quantization Architecture | EVA：基于高效向量量化架构加速LLM解码 |
| 8 | [[2605.24391]] | MX-SAFE: Versatile Inference- and Training-Proof Microscaling Format | MX-SAFE：同时支持推理和训练的自适应微缩放格式 |
| 9 | [[2605.24461]] | Provisioning to Runtime Optimization of a +100 MW AI Cluster | 百兆瓦级AI集群从规划到运行时的优化 |
| 10 | [[2605.24665]] | An Energy-Efficient Approximate Posit Multiply-Divide Unit | 基于Posit数制的能效近似乘除法单元 |
| 11 | [[2605.24710]] | Feature Learning in Wide Neural Networks under μP: Identifiability and Sparse-Dictionary Decomposition | μP下宽神经网络特征学习：可辨识性与稀疏字典分解 |
| 12 | [[2605.24749]] | How Neural Reward Models Learn Features for Policy Optimization: A Single-Index Analysis | 神经奖励模型如何学习特征：单指数模型分析 |
| 13 | [[2605.24817]] | RouteScan: A Non-Intrusive Approach to Auditing MoE LLMs Safety via Expert Routing Telemetry | RouteScan：基于专家路由遥测的非侵入式MoE安全审计 |
| 14 | [[2605.25151]] | Representation Without Control: Testing the Realization Effect in Language Models | 表征不等于控制：语言模型中实现效应的测试 |
| 15 | [[2605.25234]] | On the Epistemic Uncertainty of Overparametrized Neural Networks | 过参数化神经网络的认知不确定性 |
| 16 | [[2605.25272]] | AI Cartography: Mapping the Latent Landscape of AI Benchmark Ecosystems | AI制图学：AI基准生态系统的潜变量景观映射 |
| 17 | [[2605.25507]] | Credit Assignment with Resets in Language Model Reasoning | 语言模型推理中基于重置的信用分配 |
| 18 | [[2605.25520]] | Is Inference Mediated by Distinct Semantic Structures in LLMs? | LLM推理是否由不同的语义结构介导？ |
| 19 | [[2605.25603]] | Detecting Unfaithful Chain-of-Thought via Circuit-Guided Internal-External Discrepancy | 通过电路引导的内外差异检测不忠实思维链 |
| 20 | [[2605.25604]] | DVAO: Dynamic Variance-adaptive Advantage Optimization for Multi-reward RL | DVAO：多奖励强化学习中的动态方差自适应优势优化 |
| 21 | [[2605.25619]] | Analogies between Transformer Layers and Power Method | Transformer层与幂迭代法的类比 |
| 22 | [[2605.25629]] | When In-Distribution Gains Fail: Evaluating Weak-to-Strong Reward Models under Preference Shift | 分布内收益何时失效：偏好偏移下弱到强奖励模型评估 |
| 23 | [[2605.25658]] | AutoSG: LLM-Driven Solver Generation Solely from Task Prompts | AutoSG：仅从任务提示生成优化求解器的LLM驱动流水线 |
| 24 | [[2605.25674]] | Stochastic Estimation of the Layer-wise Hessian Trace for Monitoring Neural-network Training | 用于神经网络训练监控的逐层Hessian迹随机估计 |
| 25 | [[2605.25698]] | How Should LLMs Consume High-Quality Data? Optimal Data Scheduling via Quality-Aware Functional Scaling Laws | LLM应如何消费高质量数据：基于质量感知缩放定律的最优调度 |
| 26 | [[2605.25704]] | PowLU: An Activation Function for Stable Pre-Training of LLMs | PowLU：面向LLM稳定预训练的激活函数 |
| 27 | [[2605.25739]] | The Behavioral Credibility Trilemma: When Calibrated Autonomy Becomes Impossible | 行为可信度不可能三角：校准自主性何时不可能 |
| 28 | [[2605.25799]] | Addressing Exacerbated Attention Sink for Source-Free Cross-Domain Few-Shot Learning | 解决无源跨域小样本学习中加剧的注意力汇聚问题 |
| 29 | [[2605.25848]] | Geometric Evolution Maps: Extracting Stable Concept Probes from Transformer Residual Streams | 几何演化图：从Transformer残差流中提取稳定概念探针 |
| 30 | [[2605.25880]] | The Quantization Benefits of Residual-Free Transformers | 残差自由Transformer的量化优势 |
| 31 | [[2605.25891]] | Causal Tongue-Tie: LLMs Can Encode Causal Direction, But Their Yes/No Outputs Fail to Express | Causal Tongue-Tie：LLM能编码因果方向但无法通过输出表达 |
| 32 | [[2605.25893]] | D²-Monitor: Dynamic Safety Monitoring for Diffusion LLMs via Hesitation-Aware Routing | D²-Monitor：基于犹豫感知路由的扩散LLM动态安全监控 |
| 33 | [[2605.25902]] | Reading the Finetuning Prior: Verbatim Content Recovery via Contrastive Decoding Diffing | 读取微调先验：通过对比解码差异法逐字恢复内容 |
| 34 | [[2605.25903]] | Universal Activation Verbalizer: A Unified Framework for Cross-Model Activation Explanation | 通用激活解释器：跨模型激活解释的统一框架 |
| 35 | [[2605.25939]] | From Latent Space to Training Data: Explainable Specialization in Minimal MLPs | 从潜空间到训练数据：最小MLP中的可解释特化 |
| 36 | [[2605.25966]] | Mapping the Schedule x Bit-Width Boundary in Sub-100M Quantisation-Aware Training | 1亿参数以下量化感知训练中调度与位宽的边界映射 |
| 37 | [[2605.25988]] | What Makes a Medical Checker Trainable? Signal Collapse and Reward Hacking in Checker-Guided RAG | 医学检查器何时可训练？检查器引导RAG中的信号坍塌与奖励黑客 |
| 38 | [[2605.25991]] | Fuzzy PyTorch: Rapid Numerical Variability Evaluation for Deep Learning Models | Fuzzy PyTorch：深度学习模型的快速数值变异性评估 |
| 39 | [[2605.25997]] | Deployment-complete benchmarking | 部署完备基准测试 |
| 40 | [[2605.25998]] | Causal Methods for LLM Development and Evaluation | 面向LLM开发与评估的因果方法 |
| 41 | [[2605.26037]] | Peak-Then-Collapse and the Four Interface Channels of Knowledge-Graph Tool Use | 知识图谱工具调用的峰崩现象与四接口通道 |
| 42 | [[2605.26045]] | Confidence and Calibration of Activation Oracles for Reliable Interpretation of LLM Internals | 激活预言机的置信度与校准：可靠解读LLM内部状态 |
| 43 | [[2605.26046]] | When Gradients Collide: Failure Modes of Multi-Objective Prompt Optimization for LLM Judges | 梯度冲突：LLM评判多目标提示优化的失败模式 |
| 44 | [[2605.26079]] | Automated Benchmark Auditing for AI Agents and Large Language Models | AI智能体和大语言模型的自动化基准审计 |
| 45 | [[2605.26092]] | OrpQuant: Geometric Orthogonal Residual Projection for Multiplier-Free PoT Quantization | OrpQuant：面向无乘法器PoT量化的几何正交残差投影 |
| 46 | [[2605.26097]] | Forgetting in Language Models: Capacity, Optimization, and Self-Generated Replay | 语言模型中的遗忘：容量、优化与自生成回放 |
| 47 | [[2605.26099]] | Language Models Need Sleep | 语言模型需要睡眠 |
