---
title: "Daily Arxiv Digest — 2026-05-20"
date: 2026-05-20
tags:
  - daily-digest
  - arxiv
papers: 50
---

## 今日必读 / Must Read Today

### 1. [[2605.20798]] Most Transformer Modifications Still Do Not Transfer at 1-3B

> **推荐理由 / Reason:** 在1.2B和3B规模严格多种子测试20种Transformer改进，绝大多数未通过Bonferroni校正；发现注意力输出修改中验证损失与下游性能严重脱钩。A rigorous multi-seed benchmark of 20 Transformer modifications at 1-3B scale, revealing that pretrain loss is dangerously unreliable for ranking attention changes.

### 2. [[2605.21125]] Advantage Collapse in GRPO: Diagnosis and Mitigation (ICML 2026)

> **推荐理由 / Reason:** 揭示GRPO训练中28-45%的batch存在优势崩塌（梯度消失），提出ACR诊断指标和AVSPO算法，在0.5B-14B模型上提升4-6个百分点。Identifies "advantage collapse" affecting 28-45% of GRPO batches; ACR metric explains 62% of final performance variance; AVSPO reduces collapse by 58-63%.

### 3. [[2605.20868]] Runtime-Certified Bounded-Error Quantized Attention

> **推荐理由 / Reason:** 提出分层KV缓存架构，通过两项量化误差界和四级回退阶梯实现运行时可验证的量化推理，将朴素量化的灾难性检索失败恢复至FP16同等质量。A tiered KV cache with formal per-head per-step error bounds and a four-rung fallback ladder, matching FP16 quality while naive quantization catastrophically fails on retrieval.

---

## 按主题分类 / Papers by Topic

### RLVR与策略优化 / RLVR & Policy Optimization

| Paper | 描述 / Description |
|-------|-------------------|
| [[2605.20643]] AVSD | 多视角自适应自蒸馏，分离共识与视角特异性残差信号 / Multi-view self-distillation separating consensus from view-specific residuals, +2-3% Avg@8 |
| [[2605.20722]] AGPO | 自适应裁剪+自适应温度采样的策略优化 / Adaptive clipping and temperature sampling via group-level statistics, outperforms PPO/GRPO |
| [[2605.20740]] DAR | 基于CRPS的分布感知奖励用于LLM回归 / CRPS-based distribution-aware reward for LLM regression, improves rank correlation and calibration |
| [[2605.20863]] PlexRL | 集群级RLVR执行多路复用，降低37.58% GPU小时 / Cluster-level RLVR multiplexing exploiting cross-job idle time complementarity |
| [[2605.20865]] NFPO | N步前向迹似然比校正，控制偏差-方差权衡 / N-step forward trace likelihood-ratio correction for tunable bias-variance tradeoff in PPO |
| [[2605.21125]] AVSPO | **Must Read.** 揭示GRPO优势崩塌并提出修复算法 / Identifies advantage collapse in GRPO and proposes ACR diagnostic + AVSPO fix |

### 推理与验证 / Reasoning & Verification

| Paper | 描述 / Description |
|-------|-------------------|
| [[2605.20745]] VerifySteer | 潜在空间选择性干预验证器严格度，4-7x更少计算超越自一致性 / Latent steering of verifier strictness, outperforms self-consistency at 4-7x less compute |
| [[2605.20988]] Generalization in Transformers | PAC-Bayes界O(ωD_f³)，证明CoT将Parity泛化误差从指数降为线性 / PAC-Bayes bounds O(ωD_f³); CoT reduces Parity error from exponential to linear |
| [[2605.21127]] Reasoning-Trace Collapse | 揭示推理模型微调后推理链坍塌但答案准确率不变的现象 / Reasoning models lose structurally valid chains during SFT while answer accuracy stays stable |

### 机制可解释性与表征分析 / Mechanistic Interpretability & Representation Analysis

| Paper | 描述 / Description |
|-------|-------------------|
| [[2605.20607]] MI for Landing System | 将K-SVD字典学习引入航空安全认证，提出OOMS运行时监控 / K-SVD dictionary learning for aviation safety certification with out-of-model-scope detection |
| [[2605.20610]] Vision MoE Experts | 路由统计严重低估专家调谐多样性，发现稳定的生命-无生命二分 / Routing stats underestimate expert tuning diversity; stable animate-inanimate bipartition |
| [[2605.20824]] Markovian Circuit Tracing | HMM合成基准验证Transformer编码近似贝叶斯信念状态 / HMM benchmarks show transformers encode near-Bayesian belief states |
| [[2605.21049]] LLM-Brain Alignment | Transformer-大脑对齐具有跨语言鲁棒性，但源于词汇-语义而非计算机制 / Cross-lingual LLM-brain alignment robust but driven by lexical-semantic correspondence |
| [[2605.21288]] Tabular Foundation Models | 三种表格基础模型精度趋同但使用本质不同的上下文学习算法 / Three tabular FMs achieve comparable accuracy through qualitatively different ICL algorithms |
| [[2605.21303]] Circuit Evidence to Theory | 将电路发现建模为归纳理论构建，提出CFS和ILP结构签名 / Circuits as inductive theory construction with Causal Functional Signatures and ILP |
| [[2605.21324]] Stimulus Symmetries & RSA | 输入对称性使功能等价表示产生不同RSM，RSA/CKA可能误判 / Stimulus symmetries make functionally equivalent representations yield different RSMs |
| [[2605.21391]] Metaphor Processing CSE | 条件尺度熵揭示隐喻token在早期-中期层产生更高多尺度协调 / Conditional Scale Entropy reveals higher multi-scale coordination for metaphorical tokens |

### KV缓存与高效推理 / KV Cache & Efficient Inference

| Paper | 描述 / Description |
|-------|-------------------|
| [[2605.20600]] HeadKV | 头部感知KV缓存压缩，局部/全局头分配不对称预算，1/6缓存接近完整质量 / Head-aware KV compression with asymmetric budgets, near-full quality at 1/6 cache |
| [[2605.20868]] Runtime-Certified Quantized Attention | **Must Read.** 分层KV缓存+两项误差界+四级回退，恢复朴素量化的灾难性检索失败 / Tiered KV cache with formal error bounds and fallback ladder |
| [[2605.21226]] OCTOPUS | 八面体参数化KV缓存量化，非对称比特分配，零额外解码延迟 / Octahedral parametrization with MSE-optimal asymmetric bit split, zero decode overhead |
| [[2605.21325]] Delta-Rule Triangular Inversion | 混合递归算法MXR，NPU上4.3x内核加速，保持端到端MMLU精度 / MXR hybrid algorithm achieves 4.3x kernel speedup on NPUs with full MMLU accuracy |

### 注意力与Transformer架构 / Attention & Transformer Architecture

| Paper | 描述 / Description |
|-------|-------------------|
| [[2605.20670]] LT2 | 循环Transformer中用线性/稀疏注意力替代二次方softmax，5x解码吞吐 / Linear-time looped transformers matching full attention with 5x decode throughput |
| [[2605.20749]] GLU Condition Numbers | NTK分析揭示GLU门控将条件数从O(n/d)降至O(n/d²)加速训练 / NTK analysis shows GLU gating reduces condition number from O(n/d) to O(n/d²) |
| [[2605.20798]] Transformer Modifications Don't Transfer | **Must Read.** 20种改进仅Softpick通过Bonferroni+3B稳定性测试 / Only 1/20 Transformer modifications survives multi-seed Bonferroni correction at 3B |
| [[2605.20813]] PulseCol | 列稀疏注意力用于扩散语言模型，1.95x端到端加速 / Column-sparse attention for diffusion LMs, 1.95x end-to-end speedup |
| [[2605.21070]] Self-Pretraining for Sequences | 掩码重建将位置编码转化为近邻偏置注意力，突破标签监督瓶颈 / Masked reconstruction converts positional encodings to proximity-biased attention |

### 优化与训练理论 / Optimization & Training Theory

| Paper | 描述 / Description |
|-------|-------------------|
| [[2605.20756]] Stochastic Update Bias | 揭示预条件优化器的梯度-预条件器耦合偏差和非线性逆偏差 / Identifies gradient-preconditioner coupling and nonlinear inversion biases in AdamW/Sophia |
| [[2605.21104]] HORST | 双曲熵镜像映射+AdamW组合优化器，80-90%稀疏度下提升10个百分点 / Hyperbolic entropy mirror map composed with AdamW, +10pp at 80-90% sparsity |
| [[2605.21292]] Large-Step Training Dynamics | 大学习率根本性改变训练吸引子类型而非仅加速，立方相变+Chebyshev混沌 / Large LR changes what training converges to; cubic phase transitions and Chebyshev chaos |
| [[2605.21486]] Hyperparameter Transfer | μP优势仅来自嵌入层学习率，SP放大嵌入层LR即可匹配μP / μP advantage comes entirely from embedding LR; scaling it in SP matches μP transfer |

### 分布式训练与系统 / Distributed Training & Systems

| Paper | 描述 / Description |
|-------|-------------------|
| [[2605.20696]] Distributed DPO | 首次为联邦和去中心化DPO建立收敛性理论 / First convergence analysis for federated and decentralized DPO |
| [[2605.20799]] OFU GPU Efficiency | 基于硬件计数器的精度无关GPU利用率指标，与MFU相关系数r=0.78 / Hardware-counter-based precision-agnostic GPU efficiency metric, r=0.78 with MFU |
| [[2605.20866]] LOSCAR-SGD | 局部训练+稀疏同步+通信重叠的分布式SGD，延迟校正合并规则 / Local SGD with sparse sync and communication overlap, delay-corrected merge rule |
| [[2605.20982]] DODOCO | MoE路由不均衡与EP扩展无关，mock数据高估Gini达2.35x / MoE routing imbalance intrinsic to model; mock data overestimates Gini by 2.35x |
| [[2605.21312]] Frontier Simulator | LLM推理离散事件模拟器，延迟误差从44.9%降至2.6% / Discrete-event LLM inference simulator reducing latency error from 44.9% to 2.6% |

### 量化与模型压缩 / Quantization & Model Compression

| Paper | 描述 / Description |
|-------|-------------------|
| [[2605.20706]] LlamaWeb | WebGPU浏览器LLM推理，内存降低29-33%，解码吞吐提升45-69% / WebGPU browser LLM inference with 29-33% less memory and 45-69% higher throughput |
| [[2605.21072]] Q-ARVD | 自回归视频扩散模型量化，W8A8下1.30x加速和1.97x压缩 / First quantization framework for autoregressive video diffusion models |
| [[2605.21171]] FTerViT | 全组件三值化ViT，82.43% top-1 at 6.09MB，首次部署至ESP32微控制器 / Fully ternary ViT at 6.09MB with 82.43% top-1, first deployment on ESP32 microcontroller |

### LLM安全与鲁棒性 / LLM Safety & Robustness

| Paper | 描述 / Description |
|-------|-------------------|
| [[2605.20602]] Self-Training Restructures Language | 自训练按语法深度非对称重构语言：表层标记放大，深层句法崩溃 / Self-training amplifies surface markers while deep syntax collapses |
| [[2605.20641]] Optimization-Triggered Backdoor | torch.compile编译优化引入的数值偏差可被LoRA后门利用，ASR约90% / Exploiting numerical deviations from torch.compile for backdoor attacks, ~90% ASR |
| [[2605.20744]] Hack-Verifiable Environments | 将可验证的奖励作弊机会嵌入评估环境，实现自动化检测 / Embedding verifiable hack opportunities into evaluation environments |

### 统计学习理论 / Statistical Learning Theory

| Paper | 描述 / Description |
|-------|-------------------|
| [[2605.20635]] General Theory of Localization | 局部化方法统一框架，将自注意力、MeanShift、扩散模型等十余种方法统一 / Unifying framework for localization methods spanning attention, MeanShift, diffusion |
| [[2605.20999]] Concentration of SA | 随机逼近的极大浓度界，误差尾部从次高斯到重尾取决于步长和算子性质 / Maximal concentration bounds for SA; tails range from sub-Gaussian to heavy |
| [[2605.21107]] COCO via Self-Contraction | 约束在线凸优化的自收缩曲线方法，强凸CCV从O(√TlogT)改善至O(logT) / Self-contraction improves constrained OCO cumulative violation from O(√TlogT) to O(logT) |

### 其他主题 / Other Topics

| Paper | 描述 / Description |
|-------|-------------------|
| [[2605.20606]] C²R Robust Dataset Distillation | 攻击感知课程+类间对比鲁棒性损失，鲁棒准确率提升2.8% / Attack-aware curriculum + contrastive robustness loss, +2.8% robust accuracy |
| [[2605.20681]] Scale-Calibrated MoM PCA | 乘积流形上的尺度校准中位数均值估计，用于鲁棒分布式PCA / Scale-calibrated median-of-means on product manifold for robust distributed PCA |
| [[2605.20726]] FDP Bounds in Conformal Inference | 所有可能阈值上同时有效的有限样本FDP上界 / Finite-sample simultaneous FDP upper bounds across all rejection thresholds |
| [[2605.21060]] Divide et Calibra | 向量量化分区隐空间实现多类局部校准，LCE降低25-60% / VQ-partitioned latent space for local calibration, 25-60% LCE reduction |
| [[2605.21088]] UEC-STD Time-Series | 通用误差校正模块，4种骨干+10个数据集平均MSE降低2.32% / Universal error corrector for time-series forecasting, 2.32% average MSE reduction |
| [[2605.21227]] LexNeo-Bench | 卢森堡语词汇借用分类基准，知识图谱prompt将准确率提升至71-81% / Luxembourgish borrowing classification benchmark, KG prompts boost accuracy to 71-81% |

---

## All Papers

| # | Paper | 一句话 / One-Line Summary |
|---|-------|--------------------------|
| 1 | [[2605.20600]] HeadKV | 头部感知KV缓存压缩，局部/全局头不对称预算，1/6缓存接近完整质量 / Head-aware KV compression with asymmetric budgets at 1/6 cache |
| 2 | [[2605.20602]] Self-Training Restructures Language | 自训练按语法深度非对称重构：表层放大深层崩溃 / Self-training amplifies surface markers while deep syntax collapses |
| 3 | [[2605.20606]] C²R Dataset Distillation | 攻击感知课程+对比鲁棒性损失的鲁棒数据蒸馏 / Attack-aware curriculum for robust dataset distillation |
| 4 | [[2605.20607]] MI for Landing System | K-SVD字典学习+OOMS检测用于航空安全 / K-SVD + OOMS detection for aviation safety |
| 5 | [[2605.20610]] Vision MoE Experts | MoE专家调谐多样性被路由统计低估，稳定涌现生命-无生命二分 / MoE expert tuning diversity underestimated by routing; stable animate-inanimate split |
| 6 | [[2605.20635]] General Theory of Localization | 统一十余种ML方法的局部化框架 / Unifying localization framework spanning attention, MeanShift, diffusion |
| 7 | [[2605.20641]] Optimization-Triggered Backdoor | torch.compile数值偏差被LoRA后门利用 / torch.compile deviations exploited for backdoor attacks |
| 8 | [[2605.20643]] AVSD | 多视角自适应自蒸馏分离共识与残差 / Multi-view self-distillation separating consensus from residuals |
| 9 | [[2605.20670]] LT2 | 线性时间循环Transformer，5x解码吞吐 / Linear-time looped transformers with 5x decode throughput |
| 10 | [[2605.20681]] Scale-Calibrated MoM PCA | 乘积流形上尺度校准的鲁棒分布式PCA / Scale-calibrated MoM on product manifold for robust distributed PCA |
| 11 | [[2605.20696]] Distributed DPO | 首次为联邦/去中心化DPO建立收敛理论 / First convergence analysis for federated and decentralized DPO |
| 12 | [[2605.20706]] LlamaWeb | WebGPU浏览器LLM推理，内存降29-33% / WebGPU browser LLM inference with 29-33% less memory |
| 13 | [[2605.20722]] AGPO | 自适应裁剪+温度采样的策略优化 / Adaptive clipping and temperature policy optimization |
| 14 | [[2605.20726]] FDP Bounds in Conformal | 所有阈值同时有效的有限样本FDP上界 / Simultaneous finite-sample FDP bounds across all thresholds |
| 15 | [[2605.20740]] DAR | CRPS分布感知奖励用于LLM回归 / CRPS-based distribution-aware reward for LLM regression |
| 16 | [[2605.20744]] Hack-Verifiable Environments | 可验证的奖励作弊机会嵌入评估环境 / Verifiable hack opportunities embedded in evaluation environments |
| 17 | [[2605.20745]] VerifySteer | 潜在空间选择性干预验证器严格度 / Latent steering of verifier strictness at 4-7x less compute |
| 18 | [[2605.20749]] GLU Condition Numbers | NTK证明GLU将条件数从O(n/d)降至O(n/d²) / NTK shows GLU reduces condition number from O(n/d) to O(n/d²) |
| 19 | [[2605.20756]] Stochastic Update Bias | 揭示AdamW/Sophia的梯度-预条件器耦合偏差 / Identifies gradient-preconditioner coupling bias in AdamW/Sophia |
| 20 | [[2605.20798]] Transformer Modifications Don't Transfer | **Must Read.** 20种改进仅1种通过多种子3B测试 / Only 1/20 modifications survives multi-seed 3B test |
| 21 | [[2605.20799]] OFU GPU Efficiency | 硬件计数器精度无关GPU效率指标 / Hardware-counter precision-agnostic GPU efficiency metric |
| 22 | [[2605.20813]] PulseCol | 扩散语言模型列稀疏注意力，1.95x加速 / Column-sparse attention for diffusion LMs, 1.95x speedup |
| 23 | [[2605.20824]] Markovian Circuit Tracing | HMM基准验证Transformer编码贝叶斯信念状态 / HMM benchmarks show transformers encode Bayesian belief states |
| 24 | [[2605.20863]] PlexRL | 集群级RLVR多路复用，降低37.58% GPU小时 / Cluster-level RLVR multiplexing, -37.58% GPU hours |
| 25 | [[2605.20865]] NFPO | N步前向迹似然比校正控制偏差-方差 / N-step forward trace for tunable bias-variance tradeoff |
| 26 | [[2605.20866]] LOSCAR-SGD | 局部训练+稀疏同步+重叠的分布式SGD / Local SGD with sparse sync and communication overlap |
| 27 | [[2605.20868]] Runtime-Certified Quantized Attention | **Must Read.** 分层KV缓存+误差界+四级回退 / Tiered KV cache with error bounds and 4-rung fallback |
| 28 | [[2605.20982]] DODOCO | MoE路由不均衡是模型内在特性，mock数据高估Gini 2.35x / MoE routing imbalance is intrinsic; mock data overestimates Gini 2.35x |
| 29 | [[2605.20988]] Generalization in Transformers | PAC-Bayes界O(ωD_f³)，CoT将Parity误差从指数降为线性 / PAC-Bayes O(ωD_f³); CoT reduces Parity error exponential to linear |
| 30 | [[2605.20999]] Concentration of SA | 随机逼近极大浓度界，尾部从次高斯到重尾 / Maximal concentration for SA; tails sub-Gaussian to heavy |
| 31 | [[2605.21049]] LLM-Brain Alignment | 跨语言LLM-大脑对齐源于词汇-语义而非计算机制 / Cross-lingual alignment from lexical-semantic not computation |
| 32 | [[2605.21060]] Divide et Calibra | VQ分区隐空间实现多类局部校准，LCE降25-60% / VQ-partitioned local calibration, 25-60% LCE reduction |
| 33 | [[2605.21070]] Self-Pretraining for Sequences | 掩码重建将位置编码转化为近邻偏置注意力 / Masked reconstruction converts positional encodings to proximity bias |
| 34 | [[2605.21072]] Q-ARVD | 自回归视频扩散模型量化，W8A8下1.30x加速 / Quantization for autoregressive video diffusion, 1.30x speedup at W8A8 |
| 35 | [[2605.21088]] UEC-STD Time-Series | 通用误差校正模块，10个数据集平均MSE降2.32% / Universal error corrector, 2.32% average MSE reduction |
| 36 | [[2605.21104]] HORST | 双曲熵镜像+AdamW组合优化器，90%稀疏度提升10pp / Hyperbolic entropy + AdamW optimizer, +10pp at 90% sparsity |
| 37 | [[2605.21107]] COCO via Self-Contraction | 约束在线凸优化CCV从O(√TlogT)改善至O(logT) / Constrained OCO CCV improved from O(√TlogT) to O(logT) |
| 38 | [[2605.21125]] AVSPO (GRPO Collapse) | **Must Read.** GRPO优势崩塌诊断与修复，准确率提升4-6pp / GRPO advantage collapse diagnosis and fix, +4-6pp accuracy |
| 39 | [[2605.21127]] Reasoning-Trace Collapse | 推理模型微调后推理链坍塌但答案准确率不变 / Reasoning chains collapse during SFT while answer accuracy stays stable |
| 40 | [[2605.21171]] FTerViT | 全组件三值化ViT，6.09MB 82.43%，首次部署ESP32 / Fully ternary ViT at 6.09MB, first ESP32 deployment |
| 41 | [[2605.21226]] OCTOPUS | 八面体参数化KV缓存量化，零额外解码延迟 / Octahedral KV cache quantization with zero decode overhead |
| 42 | [[2605.21227]] LexNeo-Bench | 卢森堡语词汇借用基准，KG prompt提升至71-81% / Luxembourgish borrowing benchmark, KG prompts 71-81% |
| 43 | [[2605.21288]] Tabular Foundation Models | 三种表格基础模型使用本质不同的ICL算法 / Three tabular FMs use qualitatively different ICL algorithms |
| 44 | [[2605.21292]] Large-Step Training Dynamics | 大学习率改变训练吸引子类型，立方相变+Chebyshev混沌 / Large LR changes attractor type; cubic phase transitions |
| 45 | [[2605.21303]] Circuit Evidence to Theory | 电路发现建模为归纳理论构建+CFS签名 / Circuits as inductive theory with Causal Functional Signatures |
| 46 | [[2605.21312]] Frontier Simulator | LLM推理模拟器，延迟误差从44.9%降至2.6% / LLM inference simulator reducing latency error to 2.6% |
| 47 | [[2605.21324]] Stimulus Symmetries & RSA | 输入对称性使RSA/CKA误判功能等价表示 / Stimulus symmetries make RSA/CKA misjudge equivalent representations |
| 48 | [[2605.21325]] Delta-Rule Triangular Inversion | MXR混合算法NPU上4.3x加速保持MMLU精度 / MXR hybrid algorithm 4.3x NPU speedup with full MMLU accuracy |
| 49 | [[2605.21391]] Metaphor Processing CSE | 条件尺度熵揭示隐喻token的多尺度协调 / Conditional Scale Entropy reveals metaphor multi-scale coordination |
| 50 | [[2605.21486]] Hyperparameter Transfer | μP优势仅来自嵌入层LR，SP放大即可匹配 / μP advantage is embedding LR only; scaling in SP matches μP |
