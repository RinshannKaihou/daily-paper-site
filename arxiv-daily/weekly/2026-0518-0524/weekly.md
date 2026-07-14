---
title: "Weekly arXiv Digest — 2026-05-18–2026-05-24"
week: 2026-0518-0524
date_range: ["2026-05-18", "2026-05-24"]
tags: [训练与优化, 其他前沿, 可解释性与机制分析, 安全、对齐与评估]
papers: 230
---

> 本周共收录 **230** 篇精选论文，来自 2 个工作日的每日精选。 / **230** curated papers this week, rolled up from 2 daily digests.

## 本周必读 / Must Read This Week

> 如果你只读几篇 — 看这些。优先挑选了跨天复现或被每日必读的论文。 / If you read nothing else, read these. Prioritizes papers recurring across days or picked as daily must-reads.

### [[2605.22488]] Represented Is Not Computed: A Causal Test in Transformers

- **推荐理由：** 可解码≠被因果使用：探针成功解码中间量但因果回路不通过它们 （2 天复现 / 2 days）
- **Why read:** Decodable ≠ causally used: probes decode intermediates but the causal circuit bypasses them （2 天复现 / 2 days）
- _Topic: Mechanistic Interpretability & Representation Analysis_

### [[2605.18106]] Symmetry-Compatible Optimizer

- 等变优化器一致优于AdamW 
- _Topic: 优化与训练动力学_

### [[2605.18163]] TRACE

- 无训练幻觉纠正，15模型零回归 
- _Topic: 大模型安全与对齐_

### [[2605.18229]] Are SAE Benchmarks Reliable?

- SAE基准测试可靠性危机 
- _Topic: 机制可解释性_

### [[2605.19461]] Beyond Mode Collapse (DMPO)

- **推荐理由：** 诊断GRPO模式坍塌，DMPO分布匹配在NP-hard和数学推理上大幅提升 
- **Why read:** Diagnoses GRPO mode collapse; DMPO distribution matching achieves 9–12% gains on NP-hard and math reasoning 
- _Topic: 强化学习与推理_

### [[2605.19775]] Understanding Inference Scaling

- **推荐理由：** 揭示推理负载容量陷阱与最优并行策略 
- **Why read:** Reveals capacity trap and optimal parallelism strategies for reasoning workloads 
- _Topic: LLM系统与推理_

### [[2605.20005]] FINCH

- **推荐理由：** Loss自适应学习率平均减少93%灾难性遗忘 
- **Why read:** Loss-adaptive learning rate reducing catastrophic forgetting by 93% 
- _Topic: 优化与训练_

### [[2605.20798]] Transformer Modifications Don't Transfer

- **推荐理由：** **Must Read.** 20种改进仅1种通过多种子3B测试 
- **Why read:** Only 1/20 modifications survives multi-seed 3B test 
- _Topic: 注意力与Transformer架构_

## 本周主题脉络 / Themes This Week

### Training & Optimization / 训练与优化

本周该方向共 **58** 篇论文。 / **58** papers this week on this line.

代表论文 / Highlights: [[2605.21851]] · [[2605.21933]] · [[2605.21968]] · [[2605.22217]] · [[2605.22297]] · [[2605.22432]]

### Other Frontiers / 其他前沿

本周该方向共 **39** 篇论文。 / **39** papers this week on this line.

代表论文 / Highlights: [[2605.20606]] · [[2605.20681]] · [[2605.20726]] · [[2605.21060]] · [[2605.21088]] · [[2605.21227]]

### Interpretability & Mechanistic Analysis / 可解释性与机制分析

本周该方向共 **35** 篇论文。 / **35** papers this week on this line.

代表论文 / Highlights: [[2605.21849]] · [[2605.21958]] · [[2605.21980]] · [[2605.22005]] · [[2605.22007]] · [[2605.22170]]

### Safety, Alignment & Evaluation / 安全、对齐与评估

本周该方向共 **30** 篇论文。 / **30** papers this week on this line.

代表论文 / Highlights: [[2605.21999]] · [[2605.22437]] · [[2605.22441]] · [[2605.22446]] · [[2605.22472]] · [[2605.22493]]

### Inference Efficiency & Compression / 推理效率与压缩

本周该方向共 **29** 篇论文。 / **29** papers this week on this line.

代表论文 / Highlights: [[2605.17745]] · [[2605.17757]] · [[2605.17887]] · [[2605.17997]] · [[2605.18331]] · [[2605.18475]]

### Hardware, Systems & Infrastructure / 硬件、系统与基础设施

本周该方向共 **15** 篇论文。 / **15** papers this week on this line.

代表论文 / Highlights: [[2605.18068]] · [[2605.18327]] · [[2605.18361]] · [[2605.18444]] · [[2605.18522]] · [[2605.18612]]

## 全部论文 / All Papers

### 2026-05-18 (50)

- [[2605.17704]] Lottery Tickets in Feature Space — 特征空间前驱脚手架是中奖彩票的本质
- [[2605.17718]] Feature Learning Reshapes Function Space — 一次大步GD诱导目标相关数据自适应核
- [[2605.17745]] StatQAT — 统计误差分析框架优化量化器
- [[2605.17757]] OSCAR — 离线协方差2-bit KV Cache量化
- [[2605.17770]] Entropy-Gradient Inversion / CorR-PO — 熵-梯度反演作为RL奖励正则化
- [[2605.17787]] Revisiting the Adam-SGD Gap — 梯度裁剪使SGD匹配Adam
- [[2605.17806]] AMO — 自适应Muon正交化迭代预算
- [[2605.17821]] TierCheck — 三层分级检查点降低82%开销
- [[2605.17862]] f-OPD — 新鲜度感知异步on-policy蒸馏
- [[2605.17879]] Guard — 生产级灰节点检测，MFU提升1.7倍
- [[2605.17887]] OASIS — Softmax1空空间解决注意力汇聚异常
- [[2605.17967]] SFT Interaction Perspective — SFT本质是1000步去噪阶段
- [[2605.17971]] Babel Jailbreak — 稀疏安全注意力头的黑盒越狱
- [[2605.17997]] MARR — PID控制的模块自适应残差量化
- [[2605.18008]] UQ for PPG Blood Pressure — 深度集成在域偏移下最鲁棒
- [[2605.18022]] Memorization-Generalization Coexistence — 80%噪声下泛化与记忆共存
- [[2605.18053]] KV Cache Structural Protection — 结构性保护远比评分策略重要
- [[2605.18068]] Teger — 图曲率重连缓解过度压缩
- [[2605.18071]] KVDrive — 跨GPU/DRAM/SSD三层KV缓存管理
- [[2605.18079]] Low Precision Transformers + CoT — 低精度Transformer通过CoT模拟图灵机
- [[2605.18104]] Safety Geometry Collapse / ReGap — 多模态安全几何坍塌的自适应修正
- [[2605.18106]] Symmetry-Compatible Optimizer — 等变优化器一致优于AdamW ⭐
- [[2605.18163]] TRACE — 无训练幻觉纠正，15模型零回归 ⭐
- [[2605.18174]] Ringmaster LMO — 异步LMO动量支持Muon分布式训练
- [[2605.18180]] Canonical Regularisation — Ridge正则在特征学习中的归纳偏置扭曲
- [[2605.18202]] COCOCO — 逻辑一致保形预测满足三大需求
- [[2605.18224]] Simplex Witness for VAE — 常数坍塌的训练全周期证书
- [[2605.18229]] Are SAE Benchmarks Reliable? — SAE基准测试可靠性危机 ⭐
- [[2605.18281]] Temporal Task Diversity — 非平稳性降低记忆-泛化阈值
- [[2605.18309]] Alignment Dynamics — 对齐分数闭式更新与排练启动效应
- [[2605.18315]] Attention-based PCA — Attention梯度流收敛到PCA主成分
- [[2605.18327]] Causely — 因果智能层提升SRE根因诊断至100%
- [[2605.18329]] Lost in the Folds — CV集成与深度集成不可互换
- [[2605.18331]] Putri — 首个95%稀疏度下可用的LLM剪枝
- [[2605.18361]] iHAC — 混合集群架构降低40%响应时间
- [[2605.18444]] Reliable Multipliers under NBTI — 符号不变性老化缓解提升75%寿命
- [[2605.18475]] GAMMA — 量化器无关混合精度，2.5-bit匹配3-bit
- [[2605.18522]] Color Features in Cancer — 仅颜色特征达89%癌症分类准确率
- [[2605.18537]] Manifold Probe — 发现LLM中连续概念的多维流形
- [[2605.18549]] Probe Trajectories — 逐token探针轨迹AUROC达97%
- [[2605.18598]] Pointwise Generalization — 逐点黎曼维度比VC维紧10³倍
- [[2605.18607]] Proxy Metrics for LLM Forecasting — 80个代理指标跨家族模型排序ρ=0.81
- [[2605.18609]] Perfect Parallelization in SGD — 动量加速与batch大小成正比
- [[2605.18612]] XRM-SSD V24 — 软件调度先发式热补偿，漂移仅21%容差
- [[2605.18629]] Aligned Training for SAE — 无参数SAE对齐训练消除死亡特征
- [[2605.18646]] Language-Switching Backdoor — 触发信号在正交子空间中隐蔽传播
- [[2605.18672]] Three-Layer A/G Safety — 三层概率架构保障LLM Agent安全
- [[2605.18694]] AdaGrad under Heavy-Tailed Noise — 首次证明AdaGrad在重尾噪声下收敛
- [[2605.18739]] LongLive-2.0 — NVFP4端到端长视频生成，45.7 FPS
- [[2605.18750]] RRFP — 就绪驱动流水线并行最高2.77倍加速

### 2026-05-19 (22)

- [[2605.19250]] Causal Evidence for Attention Head Imbalance — 路径修补揭示幻觉头不对称分布，MACI条件干预最大降低幻觉 / Path-patching reveals asymmetric hallucination heads; MACI achieves largest hallucination reduction
- [[2605.19282]] Rethinking Muon Beyond Pretraining — Pion替代Muon的均匀谱白化为高通滤波，在VLA和RLVR中显著提升 / Replaces Muon's uniform spectral whitening with high-pass filtering for strong gains in VLA and RLVR
- [[2605.19444]] TTRL-Guard — 发现TTRL灭绝窗口并提出三机制防护 / Discovers TTRL extinction window and proposes three-mechanism guard
- [[2605.19458]] Mirror Flow Implicit Bias — 推导镜像流平衡方程，揭示稀疏到稠密的特征学习谱 / Derives mirror flow balance equations showing sparse-to-dense feature learning spectrum
- [[2605.19461]] Beyond Mode Collapse (DMPO) — 诊断GRPO模式坍塌，DMPO分布匹配在NP-hard和数学推理上大幅提升 / Diagnoses GRPO mode collapse; DMPO distribution matching achieves 9–12% gains on NP-hard and math reasoning ⭐
- [[2605.19483]] Dynamical Systems Memorization — 用随机逼近和坍塌理论解释生成模型记忆化 / Explains generative memorization via stochastic approximation collapse theory
- [[2605.19537]] The Silent Hyperparameter — 推理后端可导致16.6pp差异但极少被报告 / Inference backends cause up to 16.6pp score differences yet are rarely reported
- [[2605.19561]] TORQ — 两级正交旋转MXFP4量化，Qwen3-32B达73.63%精度 / Two-level orthogonal rotation MXFP4 quantization reaching 73.63% on Qwen3-32B
- [[2605.19576]] Library Drift — 发现技能库漂移，治理方案将pass@1从0.258提升至0.584 / Identifies skill library drift; governance lifts pass@1 from 0.258 to 0.584
- [[2605.19645]] K-Quantization — 系统评估量化鲁棒性，7-9B为最优平衡点 / Systematic quantization evaluation showing 7–9B as optimal efficiency-performance balance
- [[2605.19660]] OScaR — 两步方案实现INT2近乎无损KV缓存压缩 / Two-step fix achieving near-lossless INT2 KV cache compression
- [[2605.19775]] Understanding Inference Scaling — 揭示推理负载容量陷阱与最优并行策略 / Reveals capacity trap and optimal parallelism strategies for reasoning workloads ⭐
- [[2605.19813]] DP Federated Learning Bounds — 最一般交互模型下的联邦差分隐私极小化下界 / Minimax lower bounds for DP federated estimation under most general interaction model
- [[2605.19856]] StableGrad — 优化器级梯度重缩放稳定深度PINN和CNN训练 / Optimizer-level gradient rescaling stabilizing deep PINN and CNN training
- [[2605.19929]] SplitQ — 模态特异性解耦实现VLM低比特量化93.5%保留率 / Modality-specific decoupling for VLM low-bit PTQ preserving 93.5% accuracy
- [[2605.19945]] GEM — GPU差异感知MoE专家映射降低7.9%延迟 / GPU-variability-aware MoE expert mapping reducing latency by 7.9%
- [[2605.19999]] Contamination-Resistant Datasets — KV缓存形式抗污染基准数据集 / KV-cache-based benchmark datasets resistant to pretraining contamination
- [[2605.20005]] FINCH — Loss自适应学习率平均减少93%灾难性遗忘 / Loss-adaptive learning rate reducing catastrophic forgetting by 93% ⭐
- [[2605.20074]] Distillation Guarantees — GNN-DP对齐下的知识蒸馏理论保证 / Theoretical distillation guarantees under GNN-DP algorithmic alignment
- [[2605.20107]] HamJEPA — 辛预测器在JEPA中替代各向同性正则化，CIFAR-100提升+10.64 / Symplectic predictor replacing isotropic regularization in JEPA, +10.64 on CIFAR-100
- [[2605.20151]] Model Collapse in Interactive Learning — 有向图建模多模型交互并推导坍缩充要条件 / Directed-graph formalization with necessary and sufficient collapse conditions
- [[2605.20173]] Runtime Architecture Patterns — 随机-确定边界原语指导生产LLM Agent运行时设计 / SDB primitive guiding production LLM agent runtime design

### 2026-05-20 (50)

- [[2605.20600]] HeadKV — 头部感知KV缓存压缩，局部/全局头不对称预算，1/6缓存接近完整质量 / Head-aware KV compression with asymmetric budgets at 1/6 cache
- [[2605.20602]] Self-Training Restructures Language — 自训练按语法深度非对称重构：表层放大深层崩溃 / Self-training amplifies surface markers while deep syntax collapses
- [[2605.20606]] C²R Dataset Distillation — 攻击感知课程+对比鲁棒性损失的鲁棒数据蒸馏 / Attack-aware curriculum for robust dataset distillation
- [[2605.20607]] MI for Landing System — K-SVD字典学习+OOMS检测用于航空安全 / K-SVD + OOMS detection for aviation safety
- [[2605.20610]] Vision MoE Experts — MoE专家调谐多样性被路由统计低估，稳定涌现生命-无生命二分 / MoE expert tuning diversity underestimated by routing; stable animate-inanimate split
- [[2605.20635]] General Theory of Localization — 统一十余种ML方法的局部化框架 / Unifying localization framework spanning attention, MeanShift, diffusion
- [[2605.20641]] Optimization-Triggered Backdoor — torch.compile数值偏差被LoRA后门利用 / torch.compile deviations exploited for backdoor attacks
- [[2605.20643]] AVSD — 多视角自适应自蒸馏分离共识与残差 / Multi-view self-distillation separating consensus from residuals
- [[2605.20670]] LT2 — 线性时间循环Transformer，5x解码吞吐 / Linear-time looped transformers with 5x decode throughput
- [[2605.20681]] Scale-Calibrated MoM PCA — 乘积流形上尺度校准的鲁棒分布式PCA / Scale-calibrated MoM on product manifold for robust distributed PCA
- [[2605.20696]] Distributed DPO — 首次为联邦/去中心化DPO建立收敛理论 / First convergence analysis for federated and decentralized DPO
- [[2605.20706]] LlamaWeb — WebGPU浏览器LLM推理，内存降29-33% / WebGPU browser LLM inference with 29-33% less memory
- [[2605.20722]] AGPO — 自适应裁剪+温度采样的策略优化 / Adaptive clipping and temperature policy optimization
- [[2605.20726]] FDP Bounds in Conformal — 所有阈值同时有效的有限样本FDP上界 / Simultaneous finite-sample FDP bounds across all thresholds
- [[2605.20740]] DAR — CRPS分布感知奖励用于LLM回归 / CRPS-based distribution-aware reward for LLM regression
- [[2605.20744]] Hack-Verifiable Environments — 可验证的奖励作弊机会嵌入评估环境 / Verifiable hack opportunities embedded in evaluation environments
- [[2605.20745]] VerifySteer — 潜在空间选择性干预验证器严格度 / Latent steering of verifier strictness at 4-7x less compute
- [[2605.20749]] GLU Condition Numbers — NTK证明GLU将条件数从O(n/d)降至O(n/d²) / NTK shows GLU reduces condition number from O(n/d) to O(n/d²)
- [[2605.20756]] Stochastic Update Bias — 揭示AdamW/Sophia的梯度-预条件器耦合偏差 / Identifies gradient-preconditioner coupling bias in AdamW/Sophia
- [[2605.20798]] Transformer Modifications Don't Transfer — **Must Read.** 20种改进仅1种通过多种子3B测试 / Only 1/20 modifications survives multi-seed 3B test ⭐
- [[2605.20799]] OFU GPU Efficiency — 硬件计数器精度无关GPU效率指标 / Hardware-counter precision-agnostic GPU efficiency metric
- [[2605.20813]] PulseCol — 扩散语言模型列稀疏注意力，1.95x加速 / Column-sparse attention for diffusion LMs, 1.95x speedup
- [[2605.20824]] Markovian Circuit Tracing — HMM基准验证Transformer编码贝叶斯信念状态 / HMM benchmarks show transformers encode Bayesian belief states
- [[2605.20863]] PlexRL — 集群级RLVR多路复用，降低37.58% GPU小时 / Cluster-level RLVR multiplexing, -37.58% GPU hours
- [[2605.20865]] NFPO — N步前向迹似然比校正控制偏差-方差 / N-step forward trace for tunable bias-variance tradeoff
- [[2605.20866]] LOSCAR-SGD — 局部训练+稀疏同步+重叠的分布式SGD / Local SGD with sparse sync and communication overlap
- [[2605.20868]] Runtime-Certified Quantized Attention — **Must Read.** 分层KV缓存+误差界+四级回退 / Tiered KV cache with error bounds and 4-rung fallback ⭐
- [[2605.20982]] DODOCO — MoE路由不均衡是模型内在特性，mock数据高估Gini 2.35x / MoE routing imbalance is intrinsic; mock data overestimates Gini 2.35x
- [[2605.20988]] Generalization in Transformers — PAC-Bayes界O(ωD_f³)，CoT将Parity误差从指数降为线性 / PAC-Bayes O(ωD_f³); CoT reduces Parity error exponential to linear
- [[2605.20999]] Concentration of SA — 随机逼近极大浓度界，尾部从次高斯到重尾 / Maximal concentration for SA; tails sub-Gaussian to heavy
- [[2605.21049]] LLM-Brain Alignment — 跨语言LLM-大脑对齐源于词汇-语义而非计算机制 / Cross-lingual alignment from lexical-semantic not computation
- [[2605.21060]] Divide et Calibra — VQ分区隐空间实现多类局部校准，LCE降25-60% / VQ-partitioned local calibration, 25-60% LCE reduction
- [[2605.21070]] Self-Pretraining for Sequences — 掩码重建将位置编码转化为近邻偏置注意力 / Masked reconstruction converts positional encodings to proximity bias
- [[2605.21072]] Q-ARVD — 自回归视频扩散模型量化，W8A8下1.30x加速 / Quantization for autoregressive video diffusion, 1.30x speedup at W8A8
- [[2605.21088]] UEC-STD Time-Series — 通用误差校正模块，10个数据集平均MSE降2.32% / Universal error corrector, 2.32% average MSE reduction
- [[2605.21104]] HORST — 双曲熵镜像+AdamW组合优化器，90%稀疏度提升10pp / Hyperbolic entropy + AdamW optimizer, +10pp at 90% sparsity
- [[2605.21107]] COCO via Self-Contraction — 约束在线凸优化CCV从O(√TlogT)改善至O(logT) / Constrained OCO CCV improved from O(√TlogT) to O(logT)
- [[2605.21125]] AVSPO (GRPO Collapse) — **Must Read.** GRPO优势崩塌诊断与修复，准确率提升4-6pp / GRPO advantage collapse diagnosis and fix, +4-6pp accuracy ⭐
- [[2605.21127]] Reasoning-Trace Collapse — 推理模型微调后推理链坍塌但答案准确率不变 / Reasoning chains collapse during SFT while answer accuracy stays stable
- [[2605.21171]] FTerViT — 全组件三值化ViT，6.09MB 82.43%，首次部署ESP32 / Fully ternary ViT at 6.09MB, first ESP32 deployment
- [[2605.21226]] OCTOPUS — 八面体参数化KV缓存量化，零额外解码延迟 / Octahedral KV cache quantization with zero decode overhead
- [[2605.21227]] LexNeo-Bench — 卢森堡语词汇借用基准，KG prompt提升至71-81% / Luxembourgish borrowing benchmark, KG prompts 71-81%
- [[2605.21288]] Tabular Foundation Models — 三种表格基础模型使用本质不同的ICL算法 / Three tabular FMs use qualitatively different ICL algorithms
- [[2605.21292]] Large-Step Training Dynamics — 大学习率改变训练吸引子类型，立方相变+Chebyshev混沌 / Large LR changes attractor type; cubic phase transitions
- [[2605.21303]] Circuit Evidence to Theory — 电路发现建模为归纳理论构建+CFS签名 / Circuits as inductive theory with Causal Functional Signatures
- [[2605.21312]] Frontier Simulator — LLM推理模拟器，延迟误差从44.9%降至2.6% / LLM inference simulator reducing latency error to 2.6%
- [[2605.21324]] Stimulus Symmetries & RSA — 输入对称性使RSA/CKA误判功能等价表示 / Stimulus symmetries make RSA/CKA misjudge equivalent representations
- [[2605.21325]] Delta-Rule Triangular Inversion — MXR混合算法NPU上4.3x加速保持MMLU精度 / MXR hybrid algorithm 4.3x NPU speedup with full MMLU accuracy
- [[2605.21391]] Metaphor Processing CSE — 条件尺度熵揭示隐喻token的多尺度协调 / Conditional Scale Entropy reveals metaphor multi-scale coordination
- [[2605.21486]] Hyperparameter Transfer — μP优势仅来自嵌入层LR，SP放大即可匹配 / μP advantage is embedding LR only; scaling in SP matches μP

### 2026-05-21 (50)

- [[2605.21849]] GAE: Geometry-Adaptive Explainer for Dictionary-Based Interpretability — 分布偏移旋转激活子空间导致字典解释器失效，闭式Procrustes旋转3秒修复 / Distribution shift rotates activation subspaces; closed-form Procrustes rotation fixes explainer in <3s ↻05-22
- [[2605.21851]] OPPO: Bayesian Value Recursion for Token-Level Credit Assignment — 闭式贝叶斯递归实现无需critic的token级信用分配，长序列优势更显著 / Closed-form Bayesian recursion for critic-free token-level credit assignment with widening gains on longer sequences ⭐
- [[2605.21856]] The Illusion of Reasoning: Evasive Data Contamination in LLMs — CoT推理主动掩盖记忆，Zero-CoT Probe检测隐蔽数据污染 / CoT reasoning actively masks memorization; Zero-CoT Probe detects evasive data contamination ↻05-22
- [[2605.21933]] Thermodynamic Irreversibility of Training Algorithms — 四种不可逆性度量等价，学习率产生打破时间反演对称的涌现力 / Four irreversibility measures are equivalent; learning rate creates an emergent symmetry-breaking force ↻05-22
- [[2605.21958]] Diagnosis Is Not Prescription: Linguistic Co-Adaptation in LLM Pipelines — 诊断悖论：瓶颈模块是最差修补目标，语言契约解释共适应机制 / Diagnostic Paradox: the bottleneck is the worst patching target; Linguistic Contract explains co-adaptation ⭐
- [[2605.21968]] IAdaPID-ADG: Improved Adaptive PID Optimizer — 融合AMSGrad和DiffGrad的PID优化器，训练损失降低2-3个数量级 / PID optimizer integrating AMSGrad and DiffGrad, reducing training loss by 2-3 orders of magnitude ↻05-22
- [[2605.21969]] LLM Retrieval for Stable Ad Recommendations — 微调LLaMA-8B语义候选生成，A/B实验中可预测性降低8.62%同时性能提升0.45% / Fine-tuned LLaMA-8B semantic retrieval reduces prediction instability 8.62% while lifting performance 0.45%
- [[2605.21980]] Interpreting Emotional Circuits in LVLMs via Cross-Modal Information Flow — 揭示LVLM中"适配-聚合-执行"三阶段情感处理及特异性/通用通路解耦 / Reveals 3-stage emotion processing in LVLMs with sentiment-specific/universal pathway decoupling ↻05-22
- [[2605.21999]] Toward Understanding Adversarial Distillation: Why Robust Teachers Fail — 鲁棒不可学习样本集上的教师置信度失配导致学生过拟合 / Teacher confidence mismatch on robustly unlearnable samples drives student overfitting
- [[2605.22005]] Check Your LLM's Secret Dictionary! — lm_head SVD五行代码揭示训练数据组成和有害词汇子空间，RLHF无法消除预训练有害子空间 / 5-line lm_head SVD reveals training data composition and harmful subspaces; RLHF fails to remove them ↻05-22
- [[2605.22007]] Hallucination as Commitment Failure — 幻觉不是知识缺失而是"承诺失败"——概率分散随模型规模单调增加 / Hallucination is commitment failure, not knowledge absence — probability dispersion rises monotonically with scale ↻05-22
- [[2605.22098]] TextTeacher: What Can Language Teach About Images? — 文本语义锚点引导视觉模型训练，推理时无需文本组件，提升最高+2.7pp / Text semantic anchors guide vision training with no inference overhead; up to +2.7pp on ImageNet
- [[2605.22102]] ExComm: Exploration-Stage Communication for Agentic Test-Time Scaling — 探索阶段通信检测跨智能体事实冲突，软信念更新保持轨迹多样性 / Exploration-stage communication detects cross-agent factual conflicts with soft belief updates preserving diversity
- [[2605.22166]] Life-Harness: Runtime Harness Adaptation for Deterministic LLM Agents — 运行时接口适配不修改模型权重，88.5%平均提升且跨17个模型迁移 / Runtime interface adaptation without weight modification; 88.5% avg improvement with cross-model transfer to 17 backbones
- [[2605.22170]] Do Factual Recall Mechanisms Carry over from Text to Speech? — 文本模态事实召回机制完整迁移，语音模态因果效应大幅减弱 / Factual recall mechanisms transfer fully in text but are drastically weakened in speech ↻05-22
- [[2605.22217]] Survive or Collapse: Data Gating vs Reward in Self-Play RL — 数据门控比奖励设计更关键——移除门控后所有奖励变体均崩溃 / Data gating is the binding constraint on stability, not reward design — every reward variant collapses without the gate ↻05-22
- [[2605.22223]] How Many Different Outputs Can a Transformer Generate? — 严格证明Transformer可输出序列数量有限，可访问序列长度随prompt线性增长 / Proves finite accessible sequences for transformers; max length scales linearly with prompt length
- [[2605.22297]] One LR Doesn't Fit All: Heavy-Tail Guided Layerwise Learning Rates — 谱分析揭示Transformer层间异质性，自适应层学习率带来1.5倍训练加速 / Spectral analysis reveals Transformer layer heterogeneity; adaptive layerwise LR yields 1.5x training speedup ↻05-22
- [[2605.22377]] Towards Explainability of SLMs by Token Level Activation — BERT Layer 8隐藏状态L2范数量化token重要性，语义内容词占主导 / L2 norms of BERT Layer-8 hidden states quantify token importance; semantic content words dominate ↻05-22
- [[2605.22401]] Cross-Species RSA Reveals Conserved Early Visual Alignment — 早期视觉皮层对齐跨物种一致，局部学习规则优于反向传播 / Early visual alignment is conserved across species; local learning rules outperform backpropagation ↻05-22
- [[2605.22432]] AMUSE: Anytime Muon with Stable Gradient Evaluation — 时变插值结合Muon与Schedule-Free，无需LR调度，720M LLM上1.51倍加速 / Time-varying interpolation combining Muon with Schedule-Free, 1.51x speedup on 720M LLM without LR scheduling
- [[2605.22437]] Intel NCS2 EMFI Fault Response Characterization — 电磁故障注入可破坏空闲设备上已加载模型权重，架构依赖的鲁棒性差异 / EM fault injection corrupts pre-loaded model weights on idle devices; architecture-dependent robustness differences ↻05-22
- [[2605.22441]] Constant-Time Activation Functions on Microcontrollers — 无分支+Padé逼近实现ARM Cortex-M4上所有激活函数相同时钟周期 / Branchless + Padé approximation makes all activation functions execute in identical cycles on ARM Cortex-M4 ↻05-22
- [[2605.22446]] Pre-VLA: Preemptive Runtime Verification for VLA Models — PPO Critic构建安全信号在动作执行前拦截低质量VLA动作 / PPO Critic-based safety signal intercepts low-quality VLA actions before execution
- [[2605.22462]] From Correlation to Cause: Five-Stage Feature Analysis — SAE特征选择性与因果力负相关(r=-0.56)，检测鲁棒性≠因果鲁棒性 / SAE feature selectivity anticorrelates with causal force (r=-0.56); detection robustness ≠ causal robustness ↻05-22
- [[2605.22472]] Winner-Take-All Bottlenecks for Disentangled Representations — 理论证明WTA瓶颈在多任务学习中精确恢复分类潜变量 / Proves WTA bottlenecks exactly recover categorical latents under multi-task learning
- [[2605.22488]] Represented Is Not Computed: A Causal Test in Transformers — 可解码≠被因果使用：探针成功解码中间量但因果回路不通过它们 / Decodable ≠ causally used: probes decode intermediates but the causal circuit bypasses them ⭐ ↻05-22
- [[2605.22493]] Understanding Multimodal Failure in Action-Chunking Behavioral Cloning — Fano不等式和Lipschitz分析揭示行为克隆中多模态策略失效的信息论机制 / Fano inequality and Lipschitz analysis reveal information-theoretic mechanism of multimodal failure in BC
- [[2605.22496]] SITN: OOD Detection Through Goodness-of-Fit Testing — 噪声空间拟合优度检测OOD，无需OOD数据且可控制假阳性率 / Goodness-of-fit testing in noise space for OOD detection; no OOD data needed with controlled FPR
- [[2605.22532]] Relational Linear Properties in Language Models — KL-RP探针揭示时态和真实性在中间层具有强线性结构 / KL-RP probe reveals strong linear structure for tense and truthfulness in middle layers ↻05-22
- [[2605.22544]] One Prompt Is Not Enough: Instruction Sensitivity in Embedding Models — 单提示词评估系统性歪曲模型排名，对抗性提示词选择可使任意模型登顶 / Single-prompt evaluation systematically misrepresents rankings; adversarial prompt selection makes any model rank first
- [[2605.22579]] Beyond Temperature: Hyperfitting as Late-Stage Geometric Expansion — 超拟合改善贪心解码的机制是末端层的几何维度展开，仅微调最后5层即可复现 / Hyperfitting improves greedy decoding via terminal-layer geometric expansion; last-5-layer LoRA suffices
- [[2605.22593]] Do Deep Ensembles Capture Uncertainty in GNNs? — GNN深度集成存在"认知坍塌"——独立训练模型收敛到近乎相同的预测 / GNN deep ensembles suffer epistemic collapse — independently trained models converge to nearly identical predictions
- [[2605.22620]] Collapse-free Multi-Reward RLIF Training Framework — 多奖励+KL-Cov正则化解决无监督RL中的熵坍塌 / Multi-reward + KL-Cov regularization prevents entropy collapse in unsupervised RL for LLM reasoning ↻05-22
- [[2605.22644]] Why SGD Is Not Brownian Motion — 离散Fokker-Planck推导证明标准Langevin近似遗漏O(η²)项，SGD在临界点分解为受限/扩散两种模式 / Discrete Fokker-Planck derivation shows Langevin approximation omits O(η²) terms; SGD splits into confined/diffusive modes near critical points ↻05-22
- [[2605.22658]] SegCompass: SAE for Interpretable Reasoning Segmentation — SAE映射CoT和视觉特征到共享稀疏概念空间，实现可解释推理分割 / SAE maps CoT and visual features to shared sparse concept space for interpretable reasoning segmentation ↻05-22
- [[2605.22672]] Is Capability a Liability? Inverse Scaling in LLM Forecasting — 能力越强的模型在尾部风险预测中越差，标准指标掩盖失败 / More capable models are worse at tail-risk forecasting; standard metrics mask the failure ⭐
- [[2605.22679]] CEDAR: Conceptualizing Embeddings via Sparse Disentanglement — 正交变换在不扩展维度的情况下解耦VLM嵌入，用户研究验证优于MSAE / Orthogonal transformation disentangles VLM embeddings without dimensionality expansion; user studies confirm superiority over MSAE ↻05-22
- [[2605.22691]] Posterior Collapse as Automatic Spectral Pruning — β-VAE后验坍缩是自动谱剪枝机制，坍缩谱/效用谱/PCA谱三者一致 / β-VAE posterior collapse is automatic spectral pruning; collapse/utility/PCA spectra coincide ↻05-22
- [[2605.22703]] Clipping Bottleneck: Stabilizing RLVR via Stochastic Recovery — 硬裁剪的二元决策是RLVR瓶颈，随机恢复近边界信号带来2-6%提升 / Hard clipping's binary decision is the RLVR bottleneck; stochastic near-boundary rescue yields 2-6% gains ↻05-22
- [[2605.22714]] AMEL: Accumulated Message Effects on LLM Judgments — 对话历史偏置LLM判断(d=-0.17)，负面历史影响比正面强62%，5轮即饱和 / Conversation history biases LLM judgments (d=-0.17); negativity asymmetry 1.62x; saturates after 5 turns
- [[2605.22719]] Reading Task Failure Off the Activations: SAE Audit of IOI — SAE最强失败相关特征是词汇混淆而非因果机制，SAE附加值在可解释性而非预测力 / Strongest SAE failure correlate is a lexical confound, not causal; SAE adds interpretability, not predictive power ↻05-22
- [[2605.22723]] The Value of Covariance Matching in Gaussian DDPMs — 匹配完整后验协方差将路径KL从Ω(1/T)降至O(1/T²)，3次JVP即可实现 / Full covariance matching reduces path KL from Ω(1/T) to O(1/T²); 3 JVPs suffice
- [[2605.22731]] Post-Training Is About States, Not Tokens — 状态分布视角统一SFT/RL/蒸馏，在线蒸馏可从退化教师中恢复 / State-distribution view unifies post-training; on-policy distillation recovers from degraded teachers ↻05-22
- [[2605.22769]] Understanding Data Temporality Impact on LLM Pre-training — 时序预训练的6B模型在近期事实上超越更大的打乱训练模型 / Chronologically pre-trained 6B model beats larger shuffled models on recent facts
- [[2605.22779]] FAME: Failure-Aware MoE for Log Anomaly Detection — 失败感知MoE实现消息级日志异常检测，标注量减少76倍 / Failure-aware MoE for message-level log anomaly detection with 76x annotation reduction
- [[2605.22781]] DeltaBox: Millisecond-Level Sandbox Checkpoint/Rollback — OS级增量检查点/回滚14ms/5ms，MCTS状态管理开销从47-77%降至3-6% / OS-level delta checkpoint/rollback at 14ms/5ms; MCTS state overhead drops from 47-77% to 3-6%
- [[2605.22791]] Gated DeltaNet-2: Decoupling Erase and Write in Linear Attention — 擦除/写入门解耦提升线性注意力，MK-NIAH多键检索优势显著 / Decoupled erase/write gates improve linear attention; strong gains on MK-NIAH multi-key retrieval
- [[2605.22795]] Finite-Particle Convergence Rates for Drifting Models — 保守型drifting方法的有限粒子收敛速率N^{-1/(d+4)}，Laplace核的不可约尺度失配残差 / Conservative drifting achieves N^{-1/(d+4)} convergence; irreducible scale-mismatch residual for Laplace kernel
- [[2605.22800]] The Matching Principle: A Geometric Theory of Loss Functions — 统一鲁棒性/域适应/对抗训练为编码器Jacobian的几何正则化 / Unifies robustness/domain adaptation/adversarial training as geometric regularization of encoder Jacobian ↻05-22

### 2026-05-22 (24)

- [[2605.21692]] Representation Gap — 表示间隙的渐近缩放律由商流形内在维度唯一决定 ⭐
- [[2605.21706]] Latent-Space Attacks — 拒绝抑制等价于最弱潜在空间规避攻击
- [[2605.21724]] TBP-mHC — 运输多面体实现精确双随机矩阵参数化
- [[2605.21731]] I-SAFE Wasserstein Auditing — 基于Wasserstein距离的科学AI模型分布审计
- [[2605.21770]] Manifold-Guided Attention — 正确性流形引导的轨迹感知推理时干预
- [[2605.21780]] Primal-Dual DP Robustness — f-DP与隐私轮廓的原始-对偶等价用于后门认证
- [[2605.21783]] MMD Credal TTA — MMD球作为credal sets的PAC-Bayesian TTA框架
- [[2605.21801]] GCPO Uncertainty Policy Opt — 几何感知不确定性信号提升GRPO后训练
- [[2605.21803]] Optimizer-Induced Spectral Scaling — 优化器选择根本改变FFN频谱缩放规律 ⭐
- [[2605.21842]] Energy-Gated Attention — 谱能量门控注意力聚合
- [[2605.21847]] CompPow GPU Power — GPU内部组件级感知功耗管理 / Component-aware GPU power management
- [[2605.21860]] Empirical Sensitivity Estimators — 提出经验敏感性作为新的鲁棒性度量 / Introduces empirical sensitivity as a new robustness measure
- [[2605.21912]] Emerging Memory Technologies — 室温到低温存储技术综述 / Survey of room-to-cryogenic memory technologies
- [[2605.21938]] RDP Auditing — 首个直接审计Renyi差分隐私的黑盒框架 / First black-box RDP auditing framework
- [[2605.21972]] Sparsity Allocation Recoverability — 稀疏分配策略决定剪枝后无标签修复效果 / Sparsity allocation determines label-free post-pruning recoverability
- [[2605.22010]] Uniform-in-Time PoC — 确定性梯度下降的时间均匀传播混沌 / Uniform-in-time propagation of chaos for deterministic gradient flow
- [[2605.22106]] ArborKV — 树结构推理的KV缓存结构感知管理 / Structure-aware KV cache management for tree-based reasoning
- [[2605.22156]] OWPO Self-Evolving LLMs — 非对称信任区域解决力反转实现自进化 / Asymmetric trust region solves force reversal for self-evolution
- [[2605.22164]] Trajectory Reachability Metrics — 轨迹可达性度量替代欧氏距离提升规划 / Trajectory reachability metrics replace Euclidean distance for latent planning
- [[2605.22168]] Cross-Modal Synergy Benchmark — 揭示VLM可解释性评估崩塌并提出Synergistic Faithfulness / Reveals VLM explainability evaluation collapse
- [[2605.22202]] Embedding Structure Retention — k近邻重叠度和ICA峰值显著性预测嵌入模型性能 / k-NN overlap and ICA peak prominence predict embedding performance
- [[2605.22237]] QUAD4FHE — 决策感知的二次ReLU替换用于同态加密推理 / Decision-aware quadratic ReLU replacement for FHE inference
- [[2605.22351]] QuantSR+ — 2-bit量化超分辨率匹配全精度性能 / 2-bit quantized SR matches full-precision performance
- [[2605.22785]] AI Chatbots News Evaluation — 六大商业AI新闻准确性评估揭示区域不平等 / Six commercial AI chatbots show regional inequality in news accuracy

### 2026-05-24 (34)

- [[2605.24786]] CONF-KV: Confidence-Aware KV Cache Eviction — LLM推理效率 / Inference Efficiency
- [[2605.24793]] CoSpec: Collaborative Speculative Decoding — LLM推理效率 / Inference Efficiency ⭐
- [[2605.24817]] RouteScan: MoE Safety Auditing — 安全与验证 / Safety & Verification
- [[2605.24818]] Spiking Training Data for Contamination Correction — 评估与基准 / Evaluation & Benchmarking
- [[2605.24846]] Keystone Neurons of LLM — 机械可解释性 / Mechanistic Interpretability ⭐
- [[2605.24850]] Repeated Sequences: LLM vs Natural Language — 评估与基准 / Evaluation & Benchmarking
- [[2605.24856]] Concept Allocation Zone (CAZ) — 机械可解释性 / Mechanistic Interpretability
- [[2605.24879]] DP-SGD-RC: Efficient DP-SGD for LLMs — 训练与隐私 / Training & Privacy
- [[2605.24908]] Class Imbalance in DNN Learning Dynamics — 训练与隐私 / Training & Privacy
- [[2605.24919]] MultiHaluDet: Multilingual Hallucination Detection — 幻觉检测 / Hallucination Control
- [[2605.24941]] Memory-Induced Tool-Drift in LLM Agents — 安全与验证 / Safety & Verification ⭐
- [[2605.24942]] Riemannian-Manifold Steering (GAGA) — 机械可解释性 / Mechanistic Interpretability
- [[2605.24946]] VISTA: Interpretability Transfer via SAE — 机械可解释性 / Mechanistic Interpretability
- [[2605.24956]] NITP: Next Implicit Token Prediction — 训练与隐私 / Training & Privacy
- [[2605.24960]] FaithMate: CoT Faithfulness Optimization — 评估与基准 / Evaluation & Benchmarking
- [[2605.24977]] SAE Steering for Medical VLM — 幻觉检测 / Hallucination Control
- [[2605.24998]] HSIR: Self-Improvement in Reasoning Models — 推理与RL / Reasoning & RL
- [[2605.25001]] CAML: Gradient Pathology in PINNs — 深度学习理论 / DL Theory
- [[2605.25052]] BonaFide: Faithfulness Metrics Meta-Evaluation — 评估与基准 / Evaluation & Benchmarking
- [[2605.25054]] NMP-QAT: Adaptive Neuron-level Mixed Precision — 模型压缩 / Model Compression
- [[2605.25066]] QML-PipeGuard: QML Pipeline Integrity — 系统与可观测性 / Systems & Observability
- [[2605.25085]] Polynomial Truncation Sensitivity for KV Cache — LLM推理效率 / Inference Efficiency
- [[2605.25133]] PVD: Prover-Verifier Deliberation — 安全与验证 / Safety & Verification
- [[2605.25151]] Representation Without Control — 机械可解释性 / Mechanistic Interpretability
- [[2605.25189]] TDGA: Directional Alignment for Reward Hacking — 安全与验证 / Safety & Verification
- [[2605.25203]] Spectral Rotations for Low-Bit Quantization — 模型压缩 / Model Compression
- [[2605.25225]] Field Theory for Transformer Patching — 机械可解释性 / Mechanistic Interpretability
- [[2605.25234]] Epistemic Uncertainty in Overparametrized Networks — 深度学习理论 / DL Theory
- [[2605.25240]] JudgmentBench: Rubric vs Preference Evaluation — 评估与基准 / Evaluation & Benchmarking
- [[2605.25244]] CDG Voting: Confidence Dynamics for Inference — LLM推理效率 / Inference Efficiency
- [[2605.25252]] Compute-Supervision Tradeoffs in RLVR — 推理与RL / Reasoning & RL
- [[2605.25272]] AI Cartography: Mapping Benchmark Ecosystems — 评估与基准 / Evaluation & Benchmarking
- [[2605.25275]] Label-NTK Alignments & Convergence Bounds — 深度学习理论 / DL Theory
- [[2605.25298]] Prism: eBPF Performance Diagnosis — 系统与可观测性 / Systems & Observability


---

_本周报由每日 digest 汇总而成。/ This weekly digest is a rollup of the daily digests._

**每日入口 / Daily entries:** [2026-05-18](../../2026-05-18/overview.md) · [2026-05-24](../../2026-05-24/overview.md)
