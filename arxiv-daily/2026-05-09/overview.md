---
title: "Daily Paper Overview — 2026-05-09"
date: 2026-05-09
tags:
  - llm-compression
  - mixture-of-experts
  - mechanistic-interpretability
  - llm-quantization
  - efficient-inference
  - kv-cache
  - reinforcement-learning
  - activation-steering
  - scaling-laws
  - distributed-training
papers: 49
---

## 今日必读 / Must Read Today

1. **[[2605.08575]] Uncovering Intra-expert Activation Sparsity for Efficient MoE Execution**
   发现现有MoE模型中高达90%的专家内激活稀疏性，无需修改模型参数即可在vLLM中实现2.5倍MoE层加速。
   Discovers up to 90% intra-expert sparsity in pretrained MoE models (1B-400B), achieving 2.5x MoE-layer speedup in vLLM with zero model modification.

2. **[[2605.08840]] ReST-KV: Robust KV Cache Eviction via Layer-wise Output Reconstruction**
   将KV缓存驱逐建模为逐层输出重建问题，推导闭式重要性指标，128k上下文下解码延迟降低10.61倍，ICLR 2026接收。
   Reformulates KV eviction as output reconstruction, achieving 10.61x decoding latency reduction at 128k context. Accepted at ICLR 2026.

3. **[[2605.09154]] Predicting Large Model Test Losses with a Noisy Quadratic System**
   首个支持可变batch size的LLM损失预测模型，在1000倍计算预算外推下显著优于Chinchilla，ICML 2026接收。
   First loss prediction model handling variable batch sizes, outperforming Chinchilla at 1000x compute extrapolation. Accepted at ICML 2026.

---

## 按主题分类 / Papers by Topic

### Efficient Inference & Serving / 高效推理与服务

| Paper | Short Title | Contribution / 贡献 |
|-------|-------------|---------------------|
| [[2605.08568]] | PARSE: Prompt-Aware Rank Selection | 动态SVD秩选择提升LLaMA-7B准确率10%，2.5倍加速 / Dynamic SVD rank selection for 10% accuracy gain and 2.5x speedup |
| [[2605.08575]] | Intra-expert Activation Sparsity | MoE专家内90%稀疏性，vLLM中2.5倍加速 / 90% intra-expert sparsity, 2.5x speedup in vLLM |
| [[2605.08692]] | AAAC: Adaptive Codebooks for 4-bit Quant | 轻量4-bit自适应码本量化，超越7种基线 / Lightweight 4-bit adaptive codebook quantization outperforming 7 baselines |
| [[2605.08755]] | LAQuant: Layer-wise Lookahead Quantization | 逐层前瞻损失解决推理模型量化精度损失，3.42倍解码加速 / Layer-wise lookahead loss for reasoning-model quantization, 3.42x decode speedup |
| [[2605.08840]] | ReST-KV: Output Reconstruction Eviction | 闭式KV驱逐指标，128k下10.61倍延迟降低，ICLR 2026 / Closed-form KV eviction, 10.61x latency reduction at 128k, ICLR 2026 |
| [[2605.08894]] | FINE: Smoothness in Quantized LLMs | 揭示极低比特量化中的平滑性退化问题 / Identifies smoothness degradation in extreme LLM quantization |
| [[2605.08913]] | Non-Monotonic Latency in Apple MPS | Apple MPS解码延迟尖峰达21倍 / 21x latency spikes in Apple MPS decoding |
| [[2605.09008]] | RKU: Reasoning-Aware Structural Pruning | 曲率感知剪枝保持CoT推理，40%稀疏度下GSM8K翻倍 / Curvature-aware pruning preserving CoT reasoning, 2x GSM8K at 40% sparsity |
| [[2605.09176]] | Navigating LLM Valley: Optimizer Survey | 65页LLM优化器综述，五维分类体系 / 65-page LLM optimizer survey with five-axis taxonomy |

### Mechanistic Interpretability & Representation / 机制可解释性与表示

| Paper | Short Title | Contribution / 贡献 |
|-------|-------------|---------------------|
| [[2605.08611]] | Emotion Echo: Somatic Markers in LLMs | 情绪回声向量复现Damasio体感标记假说的核心分离 / Emotion echo vectors replicate Damasio's somatic marker dissociation |
| [[2605.08740]] | Causal Dimensionality of Transformers | 发现表征-因果楔形，~98% SAE特征因果惰性 / Representational-causal wedge: ~98% SAE features are causally inert |
| [[2605.08853]] | Architecture Not Scale: Circuit Localization | GQA架构比模型规模更决定电路可定位性 / GQA architecture determines circuit localizability more than scale |
| [[2605.08891]] | Bilinear Autoencoders for Manifolds | 二次乘积空间字典学习发现LLM中的多维流形 / Quadratic product-space dictionary learning for multidimensional manifold discovery |
| [[2605.08934]] | Compositional Interpretability Framework | 范畴论统一SAE/transcoder/crosscoder为精炼子类 / Category-theoretic framework unifying SAEs/transcoders/crosscoders as refinements |
| [[2605.08942]] | Functional Metacognition in LLMs | 六维元认知状态可线性解码且近正交 / Six metacognitive dimensions linearly decodable and near-orthogonal |
| [[2605.09011]] | Three Geometric Phases in LLM Forward Pass | 三阶段几何结构：播种、消歧、收敛 / Three-phase geometry: seeding, disambiguation, convergence |
| [[2605.09129]] | Data-driven Circuit Discovery (DCD) | 数据驱动聚类发现多个独立电路 / Data-driven clustering discovers multiple independent circuits |
| [[2605.09160]] | Privileged Bases via Matryoshka Learning | 证明MRL在线性设定下恢复有序主方向 / Proves MRL recovers ordered principal directions in linear setting |
| [[2605.09224]] | SMIXAE: Unsupervised Manifold Discovery | 混合专家自编码器发现LLM多维流形特征 / Mixture-of-experts autoencoder discovers multidimensional manifold features |
| [[2605.16362]] | GRACE: Rank-1 Steering Geometry | 秩1引导的几何分析与预算搜索 / Geometry, granularity, and budgeted search for rank-1 steering |
| [[2605.09195]] | Geometry of Forgetting: Temporal Drift | 时序知识漂移作为LLM表示的独立轴 / Temporal knowledge drift as an independent axis in LLM representations |
| [[2605.09159]] | Internal Polylogue: Persona Tracking | 将persona向量视为动态推理监控信号 / Persona vectors as dynamic signals for reasoning monitoring |

### Training Systems & Optimization / 训练系统与优化

| Paper | Short Title | Contribution / 贡献 |
|-------|-------------|---------------------|
| [[2605.08639]] | ReLibra: Load Balancing for MoE RL Training | 路由重放机制实现MoE+RL训练1.58倍吞吐提升 / Routing replay achieves 1.58x throughput for MoE+RL training |
| [[2605.08809]] | SimReg: Embedding Similarity Regularization | 对比正则化实现预训练30%+加速 / Contrastive regularization for 30%+ pretraining speedup |
| [[2605.08817]] | IMAX: Prefix-Tuned RLVR Exploration | 软前缀+InfoMax奖励提升RLVR Pass@4达11.6% / Soft prefixes with InfoMax reward improve RLVR Pass@4 by 11.6% |
| [[2605.08949]] | Muon-OGD: Spectral CL for LLMs | 谱范数正交梯度投影用于LLM持续学习 / Spectral-norm orthogonal gradient projection for LLM continual learning |
| [[2605.09034]] | ZO-MOPI: Zeroth-Order Spectral Optimization | 流式幂迭代替代Newton-Schulz实现1.5-4倍收敛加速 / Streaming power iteration replaces Newton-Schulz for 1.5-4x speedup |
| [[2605.09126]] | CGAD: Staleness-Aware DiLoCo Optimizer | 余弦门控+指数衰减解决异步DiLoCo梯度陈旧性 / Cosine gating + exponential decay for async DiLoCo staleness |
| [[2605.09204]] | LBI: Parallel Scan Backpropagation | 潜空间有界接口降低反向传播计算代价 / Latent bounded interfaces reduce backpropagation cost |

### Scaling Laws & Loss Prediction / 缩放定律与损失预测

| Paper | Short Title | Contribution / 贡献 |
|-------|-------------|---------------------|
| [[2605.09154]] | Noisy Quadratic System for Loss Prediction | 机制性损失模型，1000倍外推优于Chinchilla，ICML 2026 / Mechanistic loss model outperforming Chinchilla at 1000x extrapolation, ICML 2026 |
| [[2605.09189]] | Practical Scaling Laws: Data-Constrained | 闭式缩放定律分解欠容量/欠训练/过拟合三项 / Closed-form scaling law decomposing undercapacity/undertraining/overfitting |

### Distributed Training & Multi-Agent Systems / 分布式训练与多智能体

| Paper | Short Title | Contribution / 贡献 |
|-------|-------------|---------------------|
| [[2605.09076]] | SAC: Byzantine-Robust Multi-Agent LLMs | 接收端评分消除自报告置信度攻击面 / Receiver-side scoring eliminates self-reported confidence attack surface |
| [[2605.08853]] | Architecture Not Scale: Circuit Localization | GQA架构比模型规模更决定电路可定位性 / GQA architecture determines circuit localizability more than scale |

### Reasoning & Post-Training / 推理与后训练

| Paper | Short Title | Contribution / 贡献 |
|-------|-------------|---------------------|
| [[2605.08737]] | Extrapolation Cliff in On-Policy Distillation | 推导奖励外推系数闭式安全阈值，预注册实验精确验证 / Closed-form safety threshold for reward extrapolation with pre-registered verification |
| [[2605.08817]] | IMAX: Prefix-Tuned RLVR Exploration | 软前缀+InfoMax奖励提升RLVR Pass@4达11.6% / Soft prefixes with InfoMax reward improve RLVR Pass@4 by 11.6% |
| [[2605.08766]] | UserGPT: Generative User Profiling | 8B模型在用户画像任务上匹配235B模型 / 8B model matches 235B on user profiling tasks |

### Hardware & Systems / 硬件与系统

| Paper | Short Title | Contribution / 贡献 |
|-------|-------------|---------------------|
| [[2605.08594]] | FLARE: Systolic Array Fault Localization | 互素数测试向量实现脉动阵列PE级故障定位 / Coprime test vectors for PE-level fault localization in systolic arrays |
| [[2605.08615]] | DSPE: Edge Processor for DeepSeek Inference | 28nm边缘处理器109.4 TFLOPS/W能效 / 28nm edge processor achieving 109.4 TFLOPS/W |
| [[2605.08725]] | Single Sub-Channel DDR5 DIMMs | DDR5单子通道架构分析与标准化空白 / DDR5 single sub-channel architecture analysis and standardization gaps |
| [[2605.08792]] | Quantum Simulation on Apple M4 Pro | UMA上量子仿真28->29比特4.46倍DRAM带宽悬崖 / 4.46x DRAM bandwidth cliff at 28->29 qubits on Apple M4 Pro UMA |

### Neural Operators & Scientific Computing / 神经算子与科学计算

| Paper | Short Title | Contribution / 贡献 |
|-------|-------------|---------------------|
| [[2605.08856]] | Commutativity Regularization for Rollouts | Jacobian正规化实现FourCastNet 41% RMSE改进 / Jacobian normalization achieves 41% RMSE improvement on FourCastNet |
| [[2605.08882]] | Discrete Flow Matching Convergence | 首个DFM非渐近收敛界，URW复杂度与词表大小无关 / First non-asymptotic DFM convergence bounds, URW complexity independent of vocabulary |
| [[2605.09096]] | SpectraNet: Stable Autoregressive PDE Surrogates | 残差目标参数化将指数误差增长转化为线性漂移 / Residual-target parametrization converts exponential to linear error growth |
| [[2605.08938]] | Formal Verification of Neural PDE Surrogates | 首个FNO的形式化正性证明，Z3编译 / First formal positivity proofs for neural PDE operators via Z3 compilation |

### Safety & Formal Verification / 安全与形式化验证

| Paper | Short Title | Contribution / 贡献 |
|-------|-------------|---------------------|
| [[2605.09045]] | Containment Verification for AI Safety | 首次用Dafny对智能体框架进行演绎形式化验证 / First deductive formal verification of an agentic framework using Dafny |

### Speech & Multimodal / 语音与多模态

| Paper | Short Title | Contribution / 贡献 |
|-------|-------------|---------------------|
| [[2605.08961]] | Dolphin-CN-Dialect: Chinese Dialect ASR | 0.4B参数模型在22种中文方言上达亚十亿级最优 / 0.4B model achieves sub-1B SOTA across 22 Chinese dialects, Interspeech |
| [[2605.08888]] | DocScope: Long-Document Verifiable Reasoning | 四级解耦评估揭示GPT-5.4完整证据链仅29% / Four-stage decoupled evaluation reveals GPT-5.4 achieves only 29% complete evidence chains |

### Theory & Mathematical Foundations / 理论与数学基础

| Paper | Short Title | Contribution / 贡献 |
|-------|-------------|---------------------|
| [[2605.08882]] | Discrete Flow Matching Convergence | DFM非渐近KL/TV收敛界 / Non-asymptotic KL/TV convergence bounds for discrete flow matching |
| [[2605.08934]] | Compositional Interpretability Framework | 范畴论形式化可解释性 / Category-theoretic formalization of interpretability |
| [[2605.09160]] | Privileged Bases via Matryoshka Learning | MRL诱导特权基的理论证明 / Theoretical proof that MRL induces privileged bases |

### Domain-Specific Applications / 领域应用

| Paper | Short Title | Contribution / 贡献 |
|-------|-------------|---------------------|
| [[2605.10984]] | PriUS: Medical Image Uncertainty | 原则引导的可解释不确定性医学图像分割 / Principle-guided interpretable uncertainty in medical image segmentation |
| [[2605.10985]] | Protein LM Interpretability via Graph Partition | 可微分图分割解析蛋白质语言模型 / Differentiable graph partitioning for protein LM interpretability |
| [[2605.10989]] | SURGE: Binary Neural Network Gradients | 代理梯度自适应二值神经网络 / Surrogate gradient adaptation for binary neural networks |
| [[2605.15212]] | Fault Tolerance via Generative Networks | GAN映射到Hopfield能量算子量化电路故障容忍度 / GAN-to-Hopfield energy mapping for circuit fault tolerance estimation |

---

## All Papers

| # | arXiv ID | Title / 标题 | Tags |
|---|----------|--------------|------|
| 1 | [[2605.08568]] | PARSE: Prompt-Aware Dynamic Rank Selection for SVD LLM Compression / 基于提示感知的SVD压缩动态秩选择 | llm-compression, svd, mixture-of-experts |
| 2 | [[2605.08575]] | Uncovering Intra-expert Activation Sparsity for Efficient MoE Execution / 发掘MoE专家内激活稀疏性 | mixture-of-experts, activation-sparsity, vLLM |
| 3 | [[2605.08594]] | FLARE: One-Shot PE-Level Fault Localization in Systolic Arrays / 脉动阵列PE级故障定位 | systolic-arrays, fault-localization, hardware-reliability |
| 4 | [[2605.08611]] | Emotion Echo: Somatic Marker Analogues in Language Models / 语言模型中的体感标记类似物 | mechanistic-interpretability, sparse-autoencoders, emotional-memory |
| 5 | [[2605.08615]] | DSPE: Edge Processor for DeepSeek Inference / DeepSeek推理边缘处理器 | edge-computing, hardware-accelerator, posit-arithmetic |
| 6 | [[2605.08639]] | ReLibra: Routing-Replay Load Balancing for MoE RL Training / MoE强化学习训练负载均衡 | mixture-of-experts, reinforcement-learning, distributed-training |
| 7 | [[2605.08692]] | AAAC: Activation-Aware Adaptive Codebooks for 4-bit Quantization / 激活感知自适应码本4-bit量化 | llm-quantization, post-training-quantization, adaptive-codebook |
| 8 | [[2605.08725]] | Single 32-bit Sub-Channel DDR5 DIMMs / 单32位子通道DDR5 DIMM | ddr5, memory-architecture, hardware-standardisation |
| 9 | [[2605.08737]] | Extrapolation Cliff in On-Policy Distillation / 在策略蒸馏中的外推悬崖 | knowledge-distillation, on-policy-distillation, reward-extrapolation |
| 10 | [[2605.08740]] | Causal Dimensionality of Transformer Representations / Transformer表示的因果维度 | mechanistic-interpretability, sparse-autoencoders, causal-dimensionality |
| 11 | [[2605.08755]] | LAQuant: Layer-wise Lookahead Loss for Reasoning Model Quantization / 逐层前瞻损失推理模型量化 | model-quantization, reasoning-models, weight-only-quantization |
| 12 | [[2605.08766]] | UserGPT: Generative User Profiling Technical Report / 生成式用户画像技术报告 | user-profiling, LLM-personalization, reinforcement-learning |
| 13 | [[2605.08792]] | Quantum Circuit Simulation on Apple M4 Pro UMA / Apple M4 Pro UMA量子电路仿真 | quantum-circuit-simulation, memory-hierarchy, apple-silicon |
| 14 | [[2605.08809]] | SimReg: Embedding Similarity Regularization for Pretraining / 嵌入相似性正则化预训练 | llm-pretraining, representation-learning, regularization |
| 15 | [[2605.08817]] | IMAX: Prefix-Tuned Priors for RLVR Exploration / 前缀调优RLVR探索 | rlvr, soft-prompt-tuning, exploration |
| 16 | [[2605.08840]] | ReST-KV: Robust KV Cache Eviction via Output Reconstruction / 基于输出重建的KV缓存驱逐 | kv-cache, llm-inference, long-context |
| 17 | [[2605.08853]] | Architecture Not Scale: Circuit Localization in LLMs / 架构非规模：LLM电路定位 | mechanistic-interpretability, circuit-analysis, grouped-query-attention |
| 18 | [[2605.08856]] | Commutativity Regularization for Long-horizon Rollouts / 长程rollout的交换性正则化 | neural-simulators, dynamical-systems, jacobian-regularization |
| 19 | [[2605.08882]] | Discrete Flow Matching Convergence Guarantees / 离散流匹配收敛保证 | flow-matching, discrete-generative-models, convergence-analysis |
| 20 | [[2605.08888]] | DocScope: Verifiable Reasoning for Long-Document Understanding / 长文档理解的可验证推理 | document-understanding, multimodal-reasoning, benchmark |
| 21 | [[2605.08891]] | Bilinear Autoencoders Find Interpretable Manifolds / 双线性自编码器发现可解释流形 | mechanistic-interpretability, sparse-autoencoders, bilinear-models |
| 22 | [[2605.08894]] | FINE: Smoothness in Extremely Quantized LLMs / 极低比特量化LLM中的平滑性 | llm-quantization, model-compression, smoothness |
| 23 | [[2605.08913]] | Non-Monotonic Latency in Apple MPS Decoding / Apple MPS解码非单调延迟 | systems, hardware-aware-inference, kv-cache |
| 24 | [[2605.08934]] | From Mechanistic to Compositional Interpretability / 从机制到组合可解释性 | mechanistic-interpretability, category-theory, compositionality |
| 25 | [[2605.08938]] | Formal Verification of Neural PDE Surrogates / 神经PDE代理的形式化验证 | formal-verification, neural-operator, PDE-surrogate |
| 26 | [[2605.08942]] | Functional Metacognition in LLMs / LLM中的功能性元认知 | mechanistic-interpretability, metacognition, activation-steering |
| 27 | [[2605.08949]] | Muon-OGD: Spectral CL for LLMs / 谱范数持续学习LLM | continual-learning, LLM-fine-tuning, Muon-optimizer |
| 28 | [[2605.08961]] | Dolphin-CN-Dialect: Chinese Dialect ASR / 中文方言语音识别 | ASR, chinese-dialects, streaming-speech-recognition |
| 29 | [[2605.09008]] | RKU: Reasoning-Aware Structural Pruning / 推理感知结构剪枝 | structural-pruning, chain-of-thought, model-compression |
| 30 | [[2605.09011]] | Three Geometric Phases in LLM Forward Pass / LLM前向传播三阶段几何 | mechanistic-interpretability, transformer-geometry, next-token-prediction |
| 31 | [[2605.09034]] | ZO-MOPI: Zeroth-Order Spectral Optimization / 零阶谱优化 | zeroth-order-optimization, LLM-fine-tuning, spectral-optimization |
| 32 | [[2605.09045]] | Containment Verification for AI Safety / AI安全遏制验证 | ai-safety, formal-verification, agentic-frameworks |
| 33 | [[2605.09076]] | SAC: Byzantine-Robust Multi-Agent LLMs / 拜占庭鲁棒多智能体LLM | multi-agent-LLM, byzantine-fault-tolerance, decentralized-consensus |
| 34 | [[2605.09096]] | SpectraNet: Stable Autoregressive PDE Surrogates / 稳定自回归PDE代理 | neural-operator, PDE-surrogate, spectral-methods |
| 35 | [[2605.09126]] | CGAD: Staleness-Aware DiLoCo Optimizer / 陈旧性感知DiLoCo优化器 | distributed-training, optimizer-design, asynchronous-SGD |
| 36 | [[2605.09129]] | Data-driven Circuit Discovery (DCD) / 数据驱动电路发现 | mechanistic-interpretability, circuit-discovery, language-model-analysis |
| 37 | [[2605.09154]] | Noisy Quadratic System for Loss Prediction / 噪声二次系统损失预测 | scaling-laws, loss-prediction, pre-training |
| 38 | [[2605.09159]] | Internal Polylogue: Persona Tracking in LLMs / LLM内部多声部对话追踪 | mechanistic-interpretability, persona-vectors, reasoning-monitoring |
| 39 | [[2605.09160]] | Privileged Bases via Matryoshka Learning / Matryoshka学习诱导特权基 | representation-learning, matryoshka, privileged-basis |
| 40 | [[2605.09176]] | Navigating LLM Valley: Optimizer Survey / LLM优化器综述 | llm-optimization, optimizer-survey, memory-efficient-training |
| 41 | [[2605.09189]] | Practical Scaling Laws: Data-Constrained World / 实用缩放定律：数据受限场景 | scaling-laws, data-constrained-training, compute-optimal-allocation |
| 42 | [[2605.09195]] | Geometry of Forgetting: Temporal Knowledge Drift / 遗忘几何：时序知识漂移 | llm-representations, knowledge-drift, mechanistic-interpretability |
| 43 | [[2605.09204]] | LBI: Parallel Scan Backpropagation / 并行扫描反向传播 | parallel-training, backpropagation, sequence-models |
| 44 | [[2605.09224]] | SMIXAE: Unsupervised Manifold Discovery / 无监督流形发现 | mechanistic-interpretability, sparse-autoencoders, manifold-learning |
| 45 | [[2605.10984]] | PriUS: Interpretable Uncertainty in Medical Segmentation / 医学分割可解释不确定性 | uncertainty-quantification, medical-image-segmentation, interpretability |
| 46 | [[2605.10985]] | Protein LM Interpretability via Graph Partition / 图分割蛋白质语言模型解释 | protein-language-models, graph-neural-networks, interpretability |
| 47 | [[2605.10989]] | SURGE: Surrogate Gradient in Binary Neural Networks / 二值神经网络代理梯度 | binary-neural-networks, surrogate-gradient, model-compression |
| 48 | [[2605.15212]] | Fault Tolerance via Visualised Generative Networks / 可视化生成网络故障容忍度 | generative-adversarial-networks, digital-circuit-design, fault-tolerance |
| 49 | [[2605.16362]] | GRACE: Rank-1 Steering Geometry and Budgeted Search / 秩1引导几何与预算搜索 | activation-steering, LLM-control, representation-engineering |
