---
title: "Daily Paper Overview — 2026-05-12"
date: 2026-05-12
tags:
  - daily-overview
  - arxiv
papers: 50
---

## 今日必读 / Must Read Today

| # | Paper | Reason |
|---|-------|--------|
| 1 | [[2605.12199]] Overtrained, Not Misaligned | 首次大规模系统性研究证明涌现性错位（EM）是过度训练的副产物而非微调的必然代价，早停法可平均保留93%任务性能的同时完全消除EM / First large-scale systematic study proving emergent misalignment is an overtraining artifact, not an inherent cost of fine-tuning; early stopping eliminates EM while retaining ~93% task performance |
| 2 | [[2605.12474]] Reward Hacking in Rubric-Based RL | 将rubric-based RL中的奖励作弊分解为验证器失败和规则设计局限两个来源，提出无需外部评委的self-internalization gap诊断指标（Pearson r ≥ 0.91）/ Decomposes reward hacking into verifier failure and rubric-design limitations; introduces verifier-free self-internalization gap diagnostic (Pearson r ≥ 0.91) |
| 3 | [[2605.11887]] Qwen-Scope | 开源覆盖7个Qwen3/Qwen3.5模型变体的14组SAE，系统展示推理控制、评测分析、毒性分类、安全数据合成、SFT/RL后训练优化六个方向的应用 / Open-sources 14 SAE groups across 7 Qwen model variants with 6 diverse applications spanning inference steering, benchmark analysis, toxicity classification, safety data synthesis, and post-training optimization |

---

## 按主题分类 / Papers by Topic

### Mechanistic Interpretability & SAE / 机制可解释性与稀疏自编码器

| Paper | Short Title | 一句话总结 / TL;DR |
|-------|------------|-------------------|
| [[2605.11887]] | Qwen-Scope | 开源14组SAE并展示6个开发工具方向的应用 / Open-sources 14 SAE groups with 6 development-tool applications |
| [[2605.11920]] | Domain Restriction via SAE Transitions | 利用SAE特征层间转移模式进行域外检测，AUROC 0.97+ / OOD detection via SAE feature transitions, AUROC 0.97+ |
| [[2605.12055]] | Linguistic Constraint Violations | SAE消融实验表明LLM缺乏统一的语法违规检测器 / SAE ablation shows LLMs lack unified grammatical violation detectors |
| [[2605.12225]] | SAE for ASR Models | 首次将SAE应用于Whisper，发现跨语言语义特征 / First SAE applied to Whisper, discovers cross-lingual semantic features |
| [[2605.12290]] | Contrastive Neuron Attribution (CNA) | 0.1%的MLP神经元构成拒绝电路，消融可降拒绝率50%+ / 0.1% MLP neurons form refusal circuit; ablation reduces refusal 50%+ |
| [[2605.12299]] | GKnow | 性别偏见与事实性别知识在电路和神经元层面严重纠缠 / Gender bias and factual knowledge severely entangled at circuit and neuron levels |
| [[2605.12426]] | Geometric Factual Recall | Transformer通过主体嵌入线性叠加实现O(R log N)维事实记忆 / Transformers memorize N×R facts in O(R log N) embedding dim via linear superposition |
| [[2605.12476]] | Router-Expert Geometric Coupling | 梯度推导证明SMoE中router行向量与expert输入权重按同一输入方向累积；1B SMoE上router分数-expert激活相关ρ=0.43(p=1.2e−81)，aux-loss使router行向量余弦相似度3倍塌缩，K-Means centroid router取得最低MaxVio=0.037 / Proves via chain rule that router rows and expert input weights co-accumulate along x; on 1B SMoE router score↔expert activation ρ=0.43, aux-loss collapses router cosine 3×, K-Means router achieves lowest MaxVio=0.037 |

### LLM Training Stability & Optimization / LLM训练稳定性与优化

| Paper | Short Title | 一句话总结 / TL;DR |
|-------|------------|-------------------|
| [[2605.11491]] | OPEFO | 从token级熵流视角分析RLVR熵坍塌，提出自适应平衡梯度机制 / Analyzes RLVR entropy collapse via token-level entropy flow; proposes adaptive gradient balancing |
| [[2605.11838]] | Spectral Clipping | 对梯度矩阵SVD后裁剪奇异值而非整体范数，达最优收敛速率 / Clips singular values of gradient matrices instead of vector norms; achieves optimal convergence |
| [[2605.12070]] | Missing Old Logits | 揭示异步LLM RL训练中旧logit缺失导致PPO解耦校正语义失效 / Reveals missing-old-logit problem breaks PPO decoupled correction in async RL training |
| [[2605.12394]] | Correlation Traps (RMT) | 基于随机矩阵理论的"anti-grokking"过拟合检测，无需训练数据 / RMT-based data-free detection of "anti-grokking" overfitting phase |
| [[2605.12380]] | P3O / Trust the Batch | 用ESS替代固定裁剪范围，零超参数即可匹配调优GRPO / Replaces fixed clip with batch ESS; matches tuned GRPO with zero clip hyperparameters |
| [[2605.12492]] | Pion Optimizer | 保谱正交变换优化器，可在无归一化层的情况下训练LLM / Spectrum-preserving optimizer that trains normalization-free LLMs |
| [[2605.12466]] | Attractor Models | 循环Transformer的不动点求解框架，常数级训练内存 / Fixed-point framework for looped transformers with constant training memory |
| [[2605.12484]] | Fast-Slow Training (FST) | 交替RL参数更新和提示进化，3x样本效率提升 / Alternates RL updates with prompt evolution; 3x sample efficiency improvement |
| [[2605.11570]] | OUI Structural Observable | 将OUI重新定位为训练动态的结构可观测信号 / Repositions OUI as a structural observable of training dynamics |

### Quantization & Compression / 量化与压缩

| Paper | Short Title | 一句话总结 / TL;DR |
|-------|------------|-------------------|
| [[2605.11478]] | FibQuant | 亚比特KV缓存压缩，最高34x压缩且注意力余弦相似度>0.95 / Sub-one-bit KV-cache compression up to 34x with attention cosine sim >0.95 |
| [[2605.12245]] | SOAR | 闭式联合尺度优化+解耦尺度搜索的NVFP4量化框架 / Closed-form joint scale optimization for NVFP4 quantization |
| [[2605.12327]] | Grid Games | 多网格自适应4-bit量化，PO2(Split87)达97.85%平均恢复率 / Multi-grid adaptive 4-bit quantization; 97.85% average recovery |
| [[2605.12464]] | ScaleSearch | 搜索NVFP4最优尺度因子，MATH-500提升15分 / Searches optimal NVFP4 scale factors; +15 pts on MATH-500 |
| [[2605.11608]] | PRISM | 将LLM变体退化分解为尺度/形状/头部三个可诊断轴 / Decomposes LLM variant degradation into scale, shape, and head axes |
| [[2605.11800]] | ROMER | MoE在模拟存算硬件上的免训练鲁棒性恢复 / Training-free robustness recovery for MoE on analog CIM hardware |

### LLM Evaluation & Safety / LLM评估与安全

| Paper | Short Title | 一句话总结 / TL;DR |
|-------|------------|-------------------|
| [[2605.11496]] | The Evaluation Differential | 形式化评估差异ED=P_T−P_D并证明边际评分不可识别（构造两策略混合均值=1/2但ED=1 vs 0）；定义ED-stable/degraded/inverted/undetermined四类安全声明与TRACE审计协议，回溯分析BrowseComp、NLA(26%/16%/<1%)、OpenAI/Apollo三起事件 / Formalises ED=P_T−P_D and proves marginal non-identifiability (two policies with identical mixture score 1/2 but ED=1 vs 0); defines 4-way claim typology + TRACE protocol, retrospectively applied to BrowseComp, NLA (26%/16%/<1%), OpenAI/Apollo |
| [[2605.11599]] | CAPS Audit Protocol | 审计约束的定向推理测试协议，CAPS未优于均匀采样 / Audit-constrained targeted reasoning test protocol; CAPS does not beat uniform sampling |
| [[2605.12022]] | SAGE | 微调0.6B模型替代大模型提示构建鲁棒性基准，成本降低25x / Fine-tunes 0.6B model to replace expensive LLM prompting; 25x cost reduction |
| [[2605.12199]] | Overtrained, Not Misaligned | EM是过度训练副产物，早停法可消除 / EM is an overtraining artifact; early stopping eliminates it |
| [[2605.12366]] | Classifier Context Rot | 800K token使安全监控漏检率增加2-30倍，中间位置最差 / 800K context increases safety monitor miss rate 2-30x; worst in the middle |
| [[2605.12265]] | Cross-Domain Monitor Training | 分类微调可部分泛化到未见的监控任务 / Classification fine-tuning partially generalizes to unseen monitoring tasks |
| [[2605.11574]] | Three Regimes of Context-Parametric Conflict | 三regime框架（R1证据连贯性/R2参数确定性/R3任务类型）；9,970次API调用跨5个前沿模型验证Regime 2 log-popularity β=−0.38到−0.50(BH-FDR均p≤.013)，Regime 3任务措辞把context-follow从~100%翻转到6.1–70.8%(χ²=30.6–155.1) / Three-regime framework validated with 9,970 API calls across 5 frontier models; R2 certainty gradient β=−0.38 to −0.50, R3 task-framing flips context-follow 100%→6.1–70.8% (χ²=30.6–155.1) |
| [[2605.12264]] | PII Reconstruction from SFT | SFT模型可从用户名重构15%的邮箱地址 / SFT models reconstruct ~15% email addresses from user name alone |

### Uncertainty Quantification & Calibration / 不确定性量化与校准

| Paper | Short Title | 一句话总结 / TL;DR |
|-------|------------|-------------------|
| [[2605.11845]] | Probabilistic Calibration as Trainable | 两种校准微调方法大幅提升LLM按指定概率分布采样的能力 / Two calibration fine-tuning methods dramatically improve LLM distribution sampling |
| [[2605.12195]] | FaReG (Fair CP) | 通过表征学习发现非线性不公平群体，ICLR 2026 / Discovers nonlinear unfair groups via representation learning; ICLR 2026 |
| [[2605.12201]] | RisCoSet (UQ for Code) | LTT框架为LLM代码生成构建风险可控预测集 / LTT framework builds risk-controlling prediction sets for LLM code generation |
| [[2605.12446]] | ORCE (Verbalized Confidence) | 解耦回答与置信度生成，排序感知DPO对齐校准 / Decouples answer and confidence generation; order-aware DPO alignment |
| [[2605.12341]] | MCP (Multi-Variable CP) | 场景优化统一预测集设计与校准，消除数据划分 / Scenario optimization unifies prediction set design and calibration; eliminates data splitting |

### Model Editing & Knowledge Conflicts / 模型编辑与知识冲突

| Paper | Short Title | 一句话总结 / TL;DR |
|-------|------------|-------------------|
| [[2605.11836]] | StableEdit | 理论揭示终身归一化的自增强稳定性循环，支持百万级编辑 / Theory reveals self-reinforcing stability loop of lifelong normalization; supports million-scale edits |
| [[2605.12185]] | DCRD | 注意力图预测知识冲突+动态对比解码，全面超越现有方法 / Attention-map conflict prediction + dynamic contrastive decoding; state-of-the-art |

### LLM Inference & Systems / LLM推理与系统

| Paper | Short Title | 一句话总结 / TL;DR |
|-------|------------|-------------------|
| [[2605.11999]] | Power Capping Illusion | GPU功耗上限对LLM解码无效，SM时钟锁定可省32%能耗 / Power capping is inert for LLM decode; SM clock locking saves up to 32% energy |
| [[2605.12129]] | Harness Design for SLMs | 4阶段执行管线将SLM任务成功率从0.762提升至0.952 / 4-stage execution harness boosts SLM task success rate from 0.762 to 0.952 |

### Text Evaluation & NLG / 文本评估与生成

| Paper | Short Title | 一句话总结 / TL;DR |
|-------|------------|-------------------|
| [[2605.11601]] | DiffScore | 基于掩码扩散的文本评估框架，持续超越BARTScore和GPTScore / Masked diffusion-based text evaluation; consistently beats BARTScore and GPTScore |

### AI Alignment & Reward Modeling / AI对齐与奖励建模

| Paper | Short Title | 一句话总结 / TL;DR |
|-------|------------|-------------------|
| [[2605.12406]] | Semantic Reward Collapse | 提出RLHF中标量奖励的语义坍缩假说和分层奖励框架 / Proposes semantic reward collapse hypothesis in RLHF; introduces stratified reward framework |

### Theory / 理论

| Paper | Short Title | 一句话总结 / TL;DR |
|-------|------------|-------------------|
| [[2605.12171]] | Parity Lower Bounds | 单层Transformer经有理函数后处理计算奇偶性需hp ≥ n/4 / Single-layer transformer needs hp ≥ n/4 for parity via rational post-processing |
| [[2605.12190]] | IT Bounds for Sequential DM | 序列超样本框架SCMI：通过分离学习者滤过H_t与证明侧放大G_{t−1}，把CMI推广为因果逐轮selector-loss互信息求和；多臂老虎机把PAC-Bayes的O(K^{1/3}T^{2/3})改进到O(√(KT log K/Δ_min)) / Sequential supersample framework SCMI decomposes CMI into causal roundwise selector-loss terms; improves PAC-Bayes bandit bound from O(K^{1/3}T^{2/3}) to O(√(KT log K/Δ_min)) |
| [[2605.12316]] | Autoregressive Learning in Joint KL | 联合KL下近似误差O(1)不依赖序列长度，估计误差Ω(H)不可避免 / Approximation O(1) under joint KL; estimation Ω(H) unavoidable |
| [[2605.12308]] | TipPFN | PFN框架从短含噪时序推断临界转变距离，零样本泛化至真实系统 / PFN predicts tipping points from short noisy time series; zero-shot to real systems |
| [[2605.12412]] | Stories in Space | LLM上下文学习在低维"概念信念空间"中的贝叶斯轨迹；Llama-3.1-8B上行为流形My与激活流形Mz相关性r=.92(Emotions)、与人类valence-arousal几何r=.93，线性探针RMSE=.09，steering纠缠可由流形距离预测(r=.65) / ICL as trajectories in low-dim conceptual belief space; on Llama-3.1-8B M_y↔M_z r=.92, matches human valence-arousal r=.93, linear probes RMSE=.09, steering entanglement predicted by manifold distance r=.65 |

### Feedback & Monitoring / 反馈与监控

| Paper | Short Title | 一句话总结 / TL;DR |
|-------|------------|-------------------|
| [[2605.12177]] | Selection Bias in LLM Feedback | 三Agent层级贝叶斯流水线校正LLM用户反馈的选择偏差 / Three-agent hierarchical Bayesian pipeline corrects selection bias in LLM feedback |

### Neuro-Symbolic & Code Synthesis / 神经符号与代码合成

| Paper | Short Title | 一句话总结 / TL;DR |
|-------|------------|-------------------|
| [[2605.12421]] | Formalize, Don't Optimize | LLM生成组合优化求解器应专注形式化而非搜索优化 / LLM-generated combinatorial solvers should formalize, not optimize search |

---

## All Papers

| # | Link | Title | 一句话总结 / One-line Summary |
|---|------|-------|-------------------------------|
| 1 | [[2605.11478]] | FibQuant: Universal Vector Quantization for KV-Cache | 亚比特向量量化KV缓存压缩，最高34x / Sub-one-bit VQ for KV-cache up to 34x compression |
| 2 | [[2605.11491]] | OPEFO: Entropy Flow Optimization for RLVR | 熵流视角分析RLVR熵坍塌，自适应平衡梯度 / Entropy flow analysis of RLVR collapse with adaptive balancing |
| 3 | [[2605.11496]] | The Evaluation Differential | 形式化ED=P_T−P_D并证明边际评分不可识别，定义4类安全声明与TRACE审计协议 / Formalises ED, proves marginal non-identifiability, defines 4-way claim typology + TRACE audit |
| 4 | [[2605.11570]] | OUI as a Structural Observable | OUI是训练中激活结构的实用可观测信号 / OUI as practical observable of activation structure during training |
| 5 | [[2605.11574]] | Three Regimes of Context-Parametric Conflict | 三regime框架；9,970 API调用5模型，R2 certainty β=−0.38到−0.50，R3任务措辞翻转100%→6.1–70.8% / Three-regime; 9,970 calls/5 models; R2 β=−0.38 to −0.50, R3 flips 100%→6.1–70.8% |
| 6 | [[2605.11599]] | CAPS Audit Protocol for LLM Reasoning | 审计约束测试协议，CAPS未优于均匀采样 / Audit-constrained protocol; CAPS doesn't beat uniform sampling |
| 7 | [[2605.11601]] | DiffScore: Text Evaluation via Masked Diffusion | 掩码扩散文本评估，持续超越BARTScore / Masked diffusion evaluation consistently beats BARTScore |
| 8 | [[2605.11608]] | PRISM: Geometric Risk Bound for LLM Variants | LLM变体退化分解为尺度/形状/头部三轴 / Decomposes LLM variant drift into scale, shape, head axes |
| 9 | [[2605.11800]] | ROMER: Robust MoE on Analog CIM | MoE在模拟存算硬件上的免训练鲁棒性恢复 / Training-free MoE robustness on analog compute-in-memory |
| 10 | [[2605.11836]] | StableEdit: Lifelong Normalization Theory | 终身归一化理论揭示自增强稳定性循环 / Theory reveals self-reinforcing stability loop in lifelong editing |
| 11 | [[2605.11838]] | Spectral Clipping for Matrix Parameters | SVD后裁剪奇异值达最优收敛速率 / Clipping singular values achieves optimal convergence rate |
| 12 | [[2605.11845]] | Probabilistic Calibration Is Trainable | 微调可使LLM学会按指定概率分布采样 / Fine-tuning makes LLMs sample from specified distributions |
| 13 | [[2605.11887]] | Qwen-Scope: SAE as Development Tools | 开源14组SAE，展示6个开发工具方向 / Open-sources 14 SAE groups with 6 development applications |
| 14 | [[2605.11920]] | Domain Restriction via SAE Transitions | SAE特征层间转移实现域外检测 / OOD detection via SAE layer-to-layer feature transitions |
| 15 | [[2605.11999]] | Power Capping Illusion in LLM Decode | 功耗上限对解码无效，时钟锁定可省32%能耗 / Power capping inert for decode; clock locking saves 32% energy |
| 16 | [[2605.12022]] | SAGE: Robustness Augmentation for Eval | 微调0.6B模型构建鲁棒性基准，成本降25x / 0.6B model builds robustness benchmarks at 25x lower cost |
| 17 | [[2605.12055]] | Linguistic Constraint Violations in LLMs | LLM缺乏统一的语法违规检测器 / LLMs lack unified grammatical violation detectors |
| 18 | [[2605.12070]] | Missing Old Logits in Async Agentic RL | 异步RL中旧logit缺失破坏PPO校正语义 / Missing old logits break PPO correction semantics in async RL |
| 19 | [[2605.12129]] | Harness Design for SLM Stability | 管线设计比模型规模更能决定SLM操作稳定性 / Harness design matters more than size for SLM stability |
| 20 | [[2605.12171]] | Parity Lower Bounds for Transformers | 单层Transformer计算奇偶性需hp≥n/4 / Single-layer transformer needs hp≥n/4 for parity |
| 21 | [[2605.12177]] | Selection Bias in LLM Feedback | 层级贝叶斯校正LLM用户反馈偏差 / Hierarchical Bayesian correction of LLM feedback bias |
| 22 | [[2605.12185]] | DCRD: Dynamic Cognitive Reconciliation | 注意力图预测冲突+动态对比解码 / Attention-map conflict prediction + dynamic contrastive decoding |
| 23 | [[2605.12190]] | IT Bounds for Sequential Decision Making | SCMI把CMI推广为因果逐轮selector-loss互信息求和；改进PAC-Bayes老虎机界O(K^{1/3}T^{2/3})→O(√(KT log K/Δ_min)) / SCMI extends CMI to causal roundwise terms; improves PAC-Bayes bandit bound to O(√(KT log K/Δ_min)) |
| 24 | [[2605.12195]] | FaReG: Fair Conformal Classification | 表征学习发现非线性不公平群体 / Representation learning discovers nonlinear unfair groups |
| 25 | [[2605.12199]] | Overtrained, Not Misaligned | EM是过度训练副产物，早停可消除 / EM is overtraining artifact; early stopping eliminates it |
| 26 | [[2605.12201]] | RisCoSet: UQ for Code Generation | LTT构建代码生成风险可控预测集 / LTT builds risk-controlling prediction sets for code |
| 27 | [[2605.12225]] | SAE for ASR Models (Whisper) | SAE发现Whisper跨语言语义特征 / SAE discovers cross-lingual semantic features in Whisper |
| 28 | [[2605.12245]] | SOAR: NVFP4 Scale Optimization | 闭式联合尺度优化的NVFP4量化 / Closed-form joint scale optimization for NVFP4 |
| 29 | [[2605.12264]] | PII Reconstruction from SFT Models | SFT模型可从用户名重构15%邮箱 / SFT models reconstruct ~15% emails from name |
| 30 | [[2605.12265]] | Cross-Domain Monitor Training | 分类微调可部分泛化到未见监控任务 / Classification fine-tuning partially generalizes to unseen monitoring |
| 31 | [[2605.12290]] | CNA: Contrastive Neuron Attribution | 0.1%神经元构成拒绝电路，消融降拒绝50%+ / 0.1% neurons form refusal circuit; ablation reduces refusal 50%+ |
| 32 | [[2605.12299]] | GKnow: Gender Bias & Knowledge | 性别偏见与事实知识在电路层面严重纠缠 / Gender bias and factual knowledge severely entangled at circuit level |
| 33 | [[2605.12308]] | TipPFN: Tipping Points via ICL | PFN零样本推断临界转变距离 / PFN zero-shot predicts tipping point proximity |
| 34 | [[2605.12316]] | Autoregressive Learning in Joint KL | 近似误差O(1)，估计误差Ω(H)不可避免 / Approximation O(1); estimation Ω(H) unavoidable |
| 35 | [[2605.12327]] | Grid Games: Multi-Grid Quantization | 多网格自适应4-bit量化，97.85%恢复率 / Multi-grid adaptive 4-bit quantization at 97.85% recovery |
| 36 | [[2605.12341]] | MCP: Multi-Variable Conformal Prediction | 场景优化消除保形预测的数据划分 / Scenario optimization eliminates data splitting in CP |
| 37 | [[2605.12366]] | Classifier Context Rot | 长上下文使安全监控漏检率增2-30倍 / Long context increases monitor miss rate 2-30x |
| 38 | [[2605.12380]] | P3O: Trust the Batch | ESS替代固定裁剪，零超参数匹配GRPO / ESS replaces fixed clip; zero hyperparameters matches GRPO |
| 39 | [[2605.12394]] | Correlation Traps (RMT Anti-Grokking) | 随机矩阵理论检测anti-grokking过拟合 / RMT detects anti-grokking overfitting without data |
| 40 | [[2605.12406]] | Semantic Reward Collapse (SRC) | RLHF标量奖励的语义坍缩假说 / Semantic reward collapse hypothesis in RLHF |
| 41 | [[2605.12412]] | Stories in Space: ICL Belief Trajectories | Llama-3.1-8B上行为M_y↔激活M_z r=.92，与人类valence-arousal r=.93，线性探针RMSE=.09 / M_y↔M_z r=.92 on Llama-3.1-8B, matches human valence-arousal r=.93, probes RMSE=.09 |
| 42 | [[2605.12421]] | Formalize, Don't Optimize | LLM组合优化应形式化而非启发式优化 / LLM combinatorial solvers should formalize not optimize |
| 43 | [[2605.12426]] | Geometric Factual Recall in Transformers | 线性叠加实现O(R log N)维事实记忆 / Linear superposition achieves O(R log N) fact memorization |
| 44 | [[2605.12446]] | ORCE: Order-Aware Verbalized Confidence | 解耦式排序感知置信度对齐 / Decoupled order-aware confidence alignment |
| 45 | [[2605.12464]] | ScaleSearch: BFP Scale Optimization | 搜索NVFP4最优尺度，MATH-500+15分 / Searches optimal NVFP4 scales; +15 pts on MATH-500 |
| 46 | [[2605.12466]] | Attractor Models (Fixed-Point LM) | 不动点求解框架，常数训练内存 / Fixed-point framework with constant training memory |
| 47 | [[2605.12474]] | Reward Hacking in Rubric-Based RL | 奖励作弊分解+无评委诊断指标 / Reward hacking decomposition + verifier-free diagnostic |
| 48 | [[2605.12476]] | Router-Expert Geometric Coupling in SMoE | 梯度推导router-expert按x共累积；1B SMoE上router分数-激活ρ=0.43，aux-loss塌缩router余弦3×，K-Means取得MaxVio=0.037 / Gradient-proven co-accumulation; on 1B SMoE ρ=0.43, aux-loss collapses cosine 3×, K-Means MaxVio=0.037 |
| 49 | [[2605.12484]] | Fast-Slow Training (FST) | RL+提示进化联合优化，3x样本效率 / Joint RL + prompt evolution; 3x sample efficiency |
| 50 | [[2605.12492]] | Pion: Spectrum-Preserving Optimizer | 保谱正交变换优化器，可训练无归一化层LLM / Spectrum-preserving optimizer; trains normalization-free LLMs |
