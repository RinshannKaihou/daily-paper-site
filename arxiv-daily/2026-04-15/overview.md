---
title: "Daily Paper Overview — 2026-04-15"
date: 2026-04-15
tags: [daily-overview, paper-digest]
papers: 36
---

# Daily Paper Overview — 2026-04-15

## Quick Stats

| Metric | Value |
|---|---|
| Papers Reviewed | 36 |
| Categories | Mechanistic Interpretability, Optimization Theory, LLM Training & Alignment, Efficient Inference & Compression, Evaluation & Reliability, Multimodal & Vision-Language, Robotics & Agents, Neural Architecture Theory |
| Total Fetched | 234 |
| Time Range | 2026-04-15 arxiv papers |

---

## 今日必读 / Must Read Today

| # | Paper | 推荐理由 / Why You Should Read It |
|---|---|---|
| 1 | [[2604.13602v1]] Reward Hacking Survey | 复旦NLP团队的大型综述，提出代理压缩假说(PCH)统一理解RLHF/RLAIF/RLVR中的奖励作弊现象，覆盖四级分类和全生命周期检测防御。A comprehensive survey from Fudan NLP proposing the Proxy Compression Hypothesis as a unifying framework for understanding reward hacking across RLHF/RLAIF/RLVR with four-level taxonomy and full lifecycle detection and mitigation. |
| 2 | [[2604.13694v1]] Weight Patching | 提出参数空间干预的机制定位方法，揭示指令跟随能力的层次化分工结构（源端-聚合-执行），并应用于机制感知模型合并。Proposes parameter-space Weight Patching for source-level mechanistic localization, revealing a hierarchical division of labor in instruction following with practical model merging application. |
| 3 | [[2604.13977v1]] FinePhrase | Hugging Face团队万亿token受控实验发现1B生成器足够、结构化教学格式最优，发布4860亿token FinePhrase数据集，成本降低30倍。Hugging Face's trillion-token study shows 1B generators suffice and structured pedagogical formats dominate, releasing 486B-token FinePhrase dataset at 30x cost reduction. |
| 4 | [[2604.13627v1]] Learning Rates Regulate Overtraining | 揭示微调学习率通过隐式正则化保留预训练特征、预训练LR衰减增加锐度导致SFT灾难性遗忘的优化动力学机制。Reveals how finetuning LRs implicitly regularize feature preservation and how pretraining LR decay increases sharpness, causing catastrophic forgetting during SFT. |

---

## 按主题分类 / Papers by Topic

### 1. 机制可解释性与内部表示分析 / Mechanistic Interpretability & Internal Representations

| Paper | 一句话总结 / TL;DR | Tags |
|---|---|---|
| [[2604.13386v1]] Linear Probe Scaling | 12个模型上验证线性探针检测LLM欺骗的准确率随规模对数线性增长，多层集成在Llama-70B上AUROC提升12.7%。Linear probe accuracy for deception detection scales log-linearly with model size across 12 models; multi-layer ensemble on Llama-70B improves mean AUROC by +12.7%. | deception-detection, scaling-laws, interpretability |
| [[2604.13403v1]] Multimodal ICL Bottlenecks | 将多模态ICL分解为任务映射构建与迁移两阶段，发现中间层能成功构建映射但因感知-推理错位无法迁移，ACL 2026。Decomposes multimodal ICL into construction and transfer phases, revealing perception-reasoning misalignment bottleneck; accepted at ACL 2026. | multimodal-icl, mechanistic-interpretability, VLMs |
| [[2604.13694v1]] Weight Patching | 提出参数空间Weight Patching方法，揭示指令跟随由浅层MLP源端、中层注意力聚合、下游执行的层次化分工。Proposes Weight Patching for parameter-space mechanistic localization, revealing hierarchical source-aggregation-execution structure in instruction following. | mechanistic-interpretability, causal-intervention, model-merging |
| [[2604.13950v1]] Causal Drawbridges | 用DAS因果干预发现Transformer LM复现人类句法岛梯度判断，揭示filler-gap机制的"因果吊桥"阻断效应。Uses DAS causal interventions to reveal Transformer LMs replicate human gradient acceptability of syntactic islands with selective "causal drawbridge" blocking. | syntactic-islands, causal-intervention, transformer-analysis |
| [[2604.13759v1]] Cognitive Companion | 提出零推理开销的并行监控架构，基于隐藏状态探针检测LLM代理推理退化，发现监控效果强烈依赖任务类型。Proposes zero-overhead parallel monitoring via hidden-state probes for detecting LLM agent reasoning degradation, with task-type-dependent effectiveness. | LLM-agent-monitoring, hidden-state-probing, agent-reliability |
| [[2604.13803v1]] V1-V3 Brain Alignment | 12个VLM上发现早期视觉皮层(V1-V3)脑对齐度与谄媚率显著负相关(r=-0.441)，忠实低层视觉编码为对抗操控提供"视觉锚点"。Finds V1-V3 brain alignment negatively predicts sycophancy (r=-0.441) across 12 VLMs, suggesting faithful low-level visual encoding provides a "visual anchor" against manipulation. | brain-alignment, sycophancy, VLM-robustness |

### 2. 优化理论与收敛分析 / Optimization Theory & Convergence

| Paper | 一句话总结 / TL;DR | Tags |
|---|---|---|
| [[2604.13393v1]] Adaptive GD Near-Linear Convergence | 用Lyapunov函数直接证明自适应GD-Polyak在四次增长凸函数上近线性收敛，比GDPolyak快2-4倍。Direct Lyapunov proof of near-linear convergence for adaptive GD-Polyak under quartic growth and convexity, achieving 2-4x speedup over GDPolyak. | optimization, convergence-analysis, adaptive-stepsizes |
| [[2604.13870v1]] GD Last Iterate Suboptimal | 证实Jain et al.猜想：任何步长序列都无法使GD/SGD最后迭代达到最优O(1/sqrt(T))率，至少多出poly-log因子。Proves no stepsize sequence ensures the optimal O(1/sqrt(T)) rate for GD/SGD last iterate in an anytime fashion; an excess poly-log factor is unavoidable. | optimization, gradient-descent, lower-bounds |
| [[2604.14017v1]] Stochastic Trust-Region | 提出随机信赖域框架，无约束问题达O(eps^{-2} log(1/eps))复杂度，无需手动学习率即可与精调SGD/Adam相当。Proposes stochastic trust-region framework achieving O(eps^{-2} log(1/eps)) complexity for unconstrained optimization, eliminating manual learning-rate tuning. | stochastic-optimization, trust-region, over-parameterized |
| [[2604.13517v1]] Multi-Timescale PPO | 揭示多时间尺度PPO中代理目标黑客和时间不确定性悖论两种病态，提出Target Decoupling架构消除策略崩溃。Identifies surrogate hacking and temporal uncertainty paradox in multi-timescale PPO, proposes Target Decoupling architecture that eliminates policy collapse on LunarLander-v2. | PPO, multi-timescale-RL, temporal-credit-assignment |
| [[2604.13460v1]] Spectral Forgetting | 将持续学习遗忘分析从排序视角转为任务分布视角，推导遗忘量的精确谱展开，证明遗忘以指数速率衰减。Shifts continual learning theory from task ordering to task distribution, deriving exact spectral expansion of forgetting with exponential decay rate. | continual-learning, spectral-theory, catastrophic-forgetting |

### 3. LLM训练、对齐与强化学习 / LLM Training, Alignment & RL

| Paper | 一句话总结 / TL;DR | Tags |
|---|---|---|
| [[2604.13602v1]] Reward Hacking Survey | 复旦NLP团队提出代理压缩假说(PCH)统一理解奖励作弊，构建四级分类体系（特征/表示/评估器/环境），覆盖全生命周期检测与防御。Fudan NLP survey proposing Proxy Compression Hypothesis with four-level taxonomy for reward hacking across RLHF/RLAIF/RLVR, covering full lifecycle detection and mitigation. | reward-hacking, RLHF, AI-alignment |
| [[2604.13627v1]] LR Regulates Overtraining | 揭示微调学习率隐式正则化特征保留、预训练LR衰减增加锐度导致SFT灾难性遗忘的机制，建议使用最低可接受学习率微调。Reveals finetuning LRs implicitly regularize feature preservation and pretraining LR decay increases sharpness, recommending the smallest acceptable finetuning LR. | catastrophic-forgetting, optimization, LLM-finetuning |
| [[2604.13902v1]] DiPO | 提出困惑度空间解耦(PSD)和双向奖励重分配(BRR)，在数学推理和函数调用任务上全面超越DAPO/GRPO基线。Proposes Perplexity Space Disentangling and Bidirectional Reward Reallocation for fine-grained exploration-exploitation trade-off, outperforming DAPO/GRPO on math reasoning. | RLVR, exploration-exploitation, policy-optimization |
| [[2604.14010v1]] EPI | 发现SFT中参数重要性时序漂移（Jaccard重叠度从78%降至45%），提出EMA梯度在线估计的动态参数隔离框架。Reveals parameter importance drifts during SFT (Jaccard overlap drops 78% to 45%), proposes EMA-gradient-based dynamic parameter isolation achieving +0.30-0.36 normalized score gains. | parameter-isolation, catastrophic-forgetting, multi-task-SFT |
| [[2604.13717v1]] LLM-as-Judge Improvement | 系统对比五种LLM评委改进技术，发现任务特定标准注入(+3.0pp)和集成评分(+9.8pp)最有效，更便宜的模型从集成中获益更大。Systematically evaluates five LLM judge improvement techniques; criteria injection (+3.0pp) and ensemble scoring (+9.8pp) dominate, with cheaper models benefiting more from ensembling. | llm-as-a-judge, evaluation-benchmark, ensemble-methods |

### 4. 高效推理与模型压缩 / Efficient Inference & Compression

| Paper | 一句话总结 / TL;DR | Tags |
|---|---|---|
| [[2604.13634v1]] Calibrated Speculative Decoding | 提出免训练校准推测解码(CSD)，通过纠错记忆和语义一致性门控恢复被误拒的语义有效token，最高2.33倍加速。Proposes training-free Calibrated Speculative Decoding rescuing semantically valid tokens wrongly rejected by standard SpecDecode, achieving up to 2.33x speedup with accuracy gains. | speculative-decoding, LLM-inference, semantic-verification |
| [[2604.13440v1]] KL Lens on Quantization | 基于KL散度的无梯度敏感度分析用于SSM-Transformer混合精度量化，在Intel Lunar Lake上Mamba-1.4B压缩至1.4GB且困惑度无损。Gradient-free KL-divergence sensitivity analysis for mixed-precision quantization of SSM-Transformer hybrids, compressing Mamba-1.4B from 5.2GB to 1.4GB with no perplexity loss. | mixed-precision-quantization, SSM-Transformer, edge-deployment |
| [[2604.13806v1]] DASH-Q | 丢弃噪声敏感的非对角Hessian元素，仅用对角曲率估计，2-bit量化零样本准确率平均提升7.01%、量化速度最高快74.5倍。Discards noise-prone off-diagonal Hessian entries for ultra low-bit quantization; at 2-bit, improves zero-shot accuracy by 7.01% on average while being up to 74.5x faster. | post-training-quantization, ultra-low-bit, LLM-compression |
| [[2604.13556v1]] YOCO++ | 在YOCO底层引入KV残差连接和缩放因子，保持50% KV缓存压缩率的同时超越标准Transformer性能。Enhances YOCO with KV residual connections in self-decoder, maintaining 50% KV cache compression while outperforming the standard Transformer on commonsense reasoning. | KV-cache, efficient-inference, cross-layer-attention |
| [[2604.13847v1]] SparseBalance | 算法-系统协同设计框架，通过动态稀疏度调整和稀疏感知批处理实现长上下文训练负载均衡，最高1.33倍端到端加速。Algorithm-system co-design for load-balanced long-context training via dynamic sparsity tuning and sparsity-aware batching, achieving up to 1.33x speedup. | sparse-attention, distributed-training, load-balancing |
| [[2604.13521v1]] C-Voting | 提出基于置信度的测试时投票策略，无需显式能量函数，在Sudoku-extreme上达95.2%准确率，发表于ICLR 2026。Proposes confidence-based test-time voting for recurrent reasoning models, achieving 95.2% on Sudoku-extreme with lightweight ItrSA++ model; ICLR 2026. | test-time-scaling, confidence-voting, reasoning |

### 5. 评估、可靠性与不确定性 / Evaluation, Reliability & Uncertainty

| Paper | 一句话总结 / TL;DR | Tags |
|---|---|---|
| [[2604.13371v1]] Reasoning Collapse | 提出"推理崩塌"概念，通过9个参数化离散推理任务揭示LLM在L3-L4复杂度阈值后性能断崖式衰退。Formalizes "Reasoning Collapse" across 9 parameterized puzzles, revealing steep performance degradation beyond L3-L4 complexity threshold in 6 frontier models. | reasoning, evaluation, complexity-limits |
| [[2604.13417v1]] Cognitive Circuit Breaker | 提出"认知断路器"框架，通过语义置信度与内部确定性的差值实时检测幻觉，跨数据集AUROC达0.73-0.75。Proposes Cognitive Circuit Breaker detecting hallucinations via gap between softmax confidence and latent probe certainty, achieving AUROC 0.73-0.75 with microsecond overhead. | hallucination-detection, LLM-reliability, representation-engineering |
| [[2604.13991v1]] Adaptive Conformal Prediction | 基于条件分位数回归的自适应共形预测，通过prompt嵌入归一化不确定性分数，提升LLM长文本和选择题的条件覆盖一致性。Adaptive conformal prediction using prompt-embedding-conditioned quantile regression for LLM factuality, improving conditional coverage across heterogeneous categories. | conformal-prediction, LLM-factuality, uncertainty-quantification |
| [[2604.13395v1]] Uncertainty in Reasoning Models | 提出CoRAP共形预测框架量化推理模型不确定性，配合Shapley值分层解释识别关键训练样本和推理步骤。Proposes CoRAP for conformal uncertainty quantification over reasoning-answer pairs with hierarchical Shapley value explanations identifying critical training examples and steps. | conformal-prediction, uncertainty-quantification, large-reasoning-models |
| [[2604.13413v1]] Non-Determinism in DLMs | 揭示数据集级指标系统性掩盖扩散语言模型样本级非确定性，提出FVA方差分解方法，代码生成非确定性远高于问答。Reveals dataset-level metrics mask sample-level non-determinism in diffusion language models; proposes FVA decomposition showing code generation is far more sensitive than QA. | diffusion-language-models, non-determinism, evaluation-metrics |
| [[2604.13882v1]] ML Evaluation Pitfalls | 通过15个数据集7个场景系统揭示监督学习评估中指标不一致现象（如不平衡数据下准确率虚高、R2掩盖残差结构）。Systematically demonstrates metric disagreement pitfalls in supervised learning evaluation across 15 datasets and 7 scenarios, advocating task-aligned metric selection. | model-evaluation, metric-selection, classification-metrics |

### 6. 多模态、视觉语言与跨域学习 / Multimodal, Vision-Language & Cross-Domain

| Paper | 一句话总结 / TL;DR | Tags |
|---|---|---|
| [[2604.13508v1]] Cluster-Aware MoE Upcycling | 用球面k-means语义聚类初始化MoE专家权重打破专家对称性，CVPR 2026。Cluster-aware Upcycling uses spherical k-means for semantic MoE initialization, breaking expert symmetry; CVPR 2026. | mixture-of-experts, MoE, upcycling, CVPR2026 |
| [[2604.13645v1]] Sim-and-Real Co-Training | 揭示仿真与真实数据协同训练中"结构化表示对齐"是性能主导因素，提出CFG-ADDA将机器人操作成功率提升约20%。Identifies structured representation alignment as the primary driver in sim-and-real co-training; CFG-ADDA improves robot success rates by ~20%. | sim-to-real, co-training, diffusion-policy |
| [[2604.13788v1]] FIDeL | 基于最优传输表征异常检测、共形预测阈值和VLM语义过滤三阶段流水线的机器人模仿学习故障检测，AUROC提升5.30%。Three-stage pipeline (optimal transport AD + conformal thresholds + VLM filtering) for robot IL failure detection, improving AUROC by +5.30% and accuracy by +17.38%. | imitation-learning, anomaly-detection, robotics |

### 7. 测试时自适应与推理增强 / Test-Time Adaptation & Reasoning Enhancement

| Paper | 一句话总结 / TL;DR | Tags |
|---|---|---|
| [[2604.13552v1]] TF-TTCL | 免训练测试时对比学习框架，通过"探索-反思-引导"循环让冻结LLM蒸馏正负规则实现在线自改进，适用于黑盒API模型。Training-free test-time contrastive learning enabling frozen/black-box LLMs to self-improve via Explore-Reflect-Steer loop, achieving 5-15 point gains on math and domain adaptation. | test-time-adaptation, contrastive-learning, black-box-adaptation |

### 8. 神经架构理论与合成数据 / Neural Architecture Theory & Synthetic Data

| Paper | 一句话总结 / TL;DR | Tags |
|---|---|---|
| [[2604.13977v1]] FinePhrase | 万亿token受控实验发现1B生成器足够、结构化教学格式最优，发布4860亿token FinePhrase数据集，成本降低30倍。Trillion-token study showing 1B generators suffice and structured pedagogical formats dominate; releases 486B-token FinePhrase dataset at 30x cost reduction. | synthetic-data, pretraining, data-quality |
| [[2604.13656v1]] OLS is Transformer | 代数证明OLS是单层线性Transformer在特定参数配置下的特例，揭示慢/快记忆解耦和从线性到指数Hopfield记忆的演化。Proves OLS is structurally isomorphic to a single-layer Linear Transformer, revealing slow/fast memory decoupling and evolution from linear to exponential Hopfield memory. | Transformer-theory, OLS, Hopfield-networks |
| [[2604.14037v1]] ReLU Network Symmetries | 利用ReLU非可微性给出浅层ReLU网络参数空间的完整对称性分类，证明"典型"参数的纤维微分同胚于Hn。Provides first complete symmetry classification for shallow ReLU networks by exploiting non-differentiability, proving generic parameters have fibres diffeomorphic to Hn. | neural-network-symmetries, parameter-identifiability, ReLU |
| [[2604.13871v1]] Exp-Minus-Log Operator | 用单一Sheffer算子eml(x,y)=exp(x)-ln(y)替代异构激活函数，在定制FPGA上可实现数量级延迟降低并获得符号可解释性。Proposes hybrid DNN-EML using single Sheffer primitive eml(x,y)=exp(x)-ln(y) for hardware-efficient neuro-symbolic networks with formal verifiability. | neuro-symbolic, Sheffer-operator, edge-AI |

---

## All Papers

| # | Paper | Authors | Key Topic | 一句话总结 / TL;DR |
|---|---|---|---|---|
| 1 | [[2604.13386v1]] Linear Probe Scaling | Nordby, Pais, Parrack | Mechanistic Interpretability | 12个模型验证线性探针欺骗检测准确率随规模对数线性增长，多层集成AUROC提升12.7%。Linear probe deception detection scales log-linearly with model size; multi-layer ensemble improves AUROC by +12.7%. |
| 2 | [[2604.13403v1]] Multimodal ICL Bottlenecks | Wang, Li | Multimodal ICL | 发现MLLM中间层构建任务映射成功但因感知-推理错位无法迁移到查询推理阶段，ACL 2026。Mid-layer task mapping construction succeeds but perception-reasoning misalignment prevents transfer to query reasoning; ACL 2026. |
| 3 | [[2604.13393v1]] Adaptive GD Near-Linear Convergence | Davis, Drusvyatskiy | Optimization Theory | Lyapunov函数直接证明自适应GD-Polyak在四次增长凸函数上近线性收敛，比GDPolyak快2-4倍。Direct Lyapunov proof of near-linear convergence for adaptive GD-Polyak under quartic growth, 2-4x faster than GDPolyak. |
| 4 | [[2604.13417v1]] Cognitive Circuit Breaker | Pan | Hallucination Detection | 通过语义置信度与内部确定性差值实时检测LLM幻觉，AUROC 0.73-0.75，微秒级开销。Real-time hallucination detection via gap between softmax confidence and latent certainty, AUROC 0.73-0.75, microsecond overhead. |
| 5 | [[2604.13517v1]] Multi-Timescale PPO | Sun | RL for LLMs | 揭示多时间尺度PPO中代理目标黑客和时间不确定性悖论，提出Target Decoupling消除策略崩溃。Surrogate hacking and temporal uncertainty paradox in multi-timescale PPO; Target Decoupling eliminates policy collapse. |
| 6 | [[2604.13371v1]] Reasoning Collapse | Utsho et al. | LLM Evaluation | 9个参数化任务揭示LLM在L3-L4复杂度阈值后推理能力断崖式衰退。Reasoning Collapse: steep performance drop beyond L3-L4 complexity threshold across 9 parameterized puzzles and 6 frontier models. |
| 7 | [[2604.13440v1]] KL Lens on Quantization | Kong et al. | Model Compression | KL散度无梯度敏感度分析用于SSM-Transformer混合精度量化，Mamba-1.4B压缩至1.4GB且困惑度无损。KL-divergence sensitivity analysis for mixed-precision SSM-Transformer quantization, compressing Mamba-1.4B from 5.2GB to 1.4GB. |
| 8 | [[2604.13521v1]] C-Voting | Kubo et al. | Test-Time Scaling | 基于置信度的测试时投票，无需显式能量函数，Sudoku-extreme达95.2%，ICLR 2026。Confidence-based test-time voting achieving 95.2% on Sudoku-extreme without explicit energy functions; ICLR 2026. |
| 9 | [[2604.13627v1]] LR Regulates Overtraining | Rofin, Varre, Flammarion | LLM Training | 微调学习率隐式正则化特征保留，预训练LR衰减增加锐度导致灾难性遗忘。Finetuning LRs implicitly regularize feature preservation; pretraining LR decay increases sharpness causing catastrophic forgetting. |
| 10 | [[2604.13803v1]] V1-V3 Brain Alignment | Shah et al. | VLM Robustness | 早期视觉皮层脑对齐度与VLM谄媚率显著负相关(r=-0.441)，忠实视觉编码提供对抗操控锚点。V1-V3 brain alignment negatively predicts VLM sycophancy (r=-0.441); faithful visual encoding anchors against manipulation. |
| 11 | [[2604.13871v1]] Exp-Minus-Log Operator | Ipek | Neuro-Symbolic | 用单一Sheffer算子eml(x,y)=exp(x)-ln(y)替代异构激活函数，定制FPGA可实现数量级延迟降低。Single Sheffer primitive replaces heterogeneous activations for hardware-efficient neuro-symbolic networks with formal verifiability. |
| 12 | [[2604.13508v1]] Cluster-Aware Upcycling | Chu et al. | MoE Training | 球面k-means语义聚类初始化MoE专家权重打破专家对称性，CVPR 2026。Spherical k-means semantic clustering initializes MoE expert weights breaking symmetry; CVPR 2026. |
| 13 | [[2604.13656v1]] OLS is Transformer | Tan, Zhao | Transformer Theory | 代数证明OLS是单层线性Transformer在特定参数配置下的特例，揭示慢/快记忆解耦机制。Algebraic proof that OLS is structurally isomorphic to single-layer Linear Transformer with slow/fast memory decoupling. |
| 14 | [[2604.13634v1]] Calibrated Speculative Decoding | Zhou et al. | Efficient Inference | 免训练校准推测解码恢复被误拒的语义有效token，最高2.33倍加速且推理准确率提升。Training-free Calibrated Speculative Decoding rescuing semantically valid tokens, up to 2.33x speedup with accuracy gains. |
| 15 | [[2604.13847v1]] SparseBalance | Xu et al. | Distributed Training | 动态稀疏度调整和稀疏感知批处理实现长上下文训练负载均衡，最高1.33倍端到端加速。Dynamic sparsity tuning and sparsity-aware batching for load-balanced long-context training, up to 1.33x speedup. |
| 16 | [[2604.13870v1]] GD Last Iterate Suboptimal | Kornowski, Shamir | Optimization Theory | 证实Jain et al.猜想：任何步长序列都无法使GD/SGD最后迭代达到最优率，poly-log因子不可避免。Confirms Jain et al. conjecture: no stepsize sequence achieves optimal last-iterate rate; poly-log overhead is unavoidable. |
| 17 | [[2604.13717v1]] LLM-as-Judge Improvement | Lail | LLM Evaluation | 任务特定标准注入(+3.0pp)和集成评分(+9.8pp)是提升LLM评委准确率最有效的方法，便宜模型获益更大。Criteria injection (+3.0pp) and ensemble scoring (+9.8pp) dominate judge improvement; cheaper models benefit more. |
| 18 | [[2604.13806v1]] DASH-Q | Kim et al. | Model Compression | 对角曲率估计用于超低位宽量化，2-bit零样本准确率平均提升7.01%、量化速度最高快74.5倍。Diagonal curvature for ultra low-bit quantization; at 2-bit, +7.01% accuracy, up to 74.5x faster than optimization-based methods. |
| 19 | [[2604.13950v1]] Causal Drawbridges | Boguraev, Mahowald | Mechanistic Interpretability | DAS因果干预揭示Transformer LM中filler-gap机制的"因果吊桥"选择性阻断效应及语料投影语言新假设。DAS causal interventions reveal selective "causal drawbridge" blocking of filler-gap mechanism with corpus-projected linguistic hypotheses. |
| 20 | [[2604.14010v1]] EPI | Lin et al. | LLM Fine-tuning | 参数重要性在SFT中时序漂移（Jaccard 78%降至45%），动态参数隔离比静态方法提升0.30-0.36归一化分数。Parameter importance drifts during SFT; dynamic isolation outperforms static by +0.30-0.36 normalized score across four backbones. |
| 21 | [[2604.14017v1]] Stochastic Trust-Region | Yang, Wang | Optimization | 随机信赖域框架无需手动学习率，无约束达O(eps^{-2} log(1/eps))复杂度，与精调SGD/Adam相当。Stochastic trust-region framework eliminating manual learning-rate tuning with competitive performance on deep learning tasks. |
| 22 | [[2604.13977v1]] FinePhrase | Niklaus et al. (Hugging Face) | Synthetic Data | 万亿token实验发现1B生成器足够、教学格式最优，发布4860亿token FinePhrase数据集，成本降低30倍。Trillion-token study: 1B generators suffice, structured pedagogical formats dominate; releases 486B-token FinePhrase at 30x cost reduction. |
| 23 | [[2604.13991v1]] Adaptive Conformal Prediction | Rubashevskii et al. | Uncertainty Quantification | 条件分位数回归归一化不确定性分数，提升LLM长文本和选择题条件覆盖一致性，保留边际覆盖保证。Prompt-embedding-conditioned quantile regression improves conditional coverage for LLM factuality with marginal coverage guarantees. |
| 24 | [[2604.14037v1]] ReLU Network Symmetries | Ramakrishnan | Neural Network Theory | 利用ReLU非可微性给出浅层ReLU网络完整对称性分类，证明"典型"参数的纤维微分同胚于Hn。Complete symmetry classification for shallow ReLU networks exploiting non-differentiability; generic fibres diffeomorphic to Hn. |
| 25 | [[2604.13788v1]] FIDeL | Rolland et al. | Robotics | 最优传输异常检测+共形预测+VLM语义过滤三阶段机器人故障检测，AUROC提升5.30%，准确率提升17.38%。Three-stage robot failure detection (optimal transport AD + conformal thresholds + VLM filtering), +5.30% AUROC, +17.38% accuracy. |
| 26 | [[2604.13902v1]] DiPO | Li et al. | RL for LLMs | 困惑度空间解耦和双向奖励重分配精细化平衡探索-利用，数学推理和函数调用全面超越DAPO/GRPO。Perplexity space disentangling and bidirectional reward reallocation outperform DAPO/GRPO on math reasoning and function calling. |
| 27 | [[2604.13460v1]] Spectral Forgetting | Xu, Ma | Continual Learning | 从任务分布视角推导遗忘量的精确谱展开，证明遗忘以指数速率衰减，丰富任务多样性加速衰减。Exact spectral expansion of forgetting from task distribution perspective; exponential decay with richer tasks accelerating decay. |
| 28 | [[2604.13413v1]] Non-Determinism in DLMs | Fang et al. | Evaluation | 数据集级指标掩盖扩散语言模型样本级非确定性，代码生成非确定性(FVA~0.80)远高于问答(~0.50-0.60)。Dataset-level metrics mask sample-level non-determinism in DLMs; code generation (FVA~0.80) far more sensitive than QA (~0.50-0.60). |
| 29 | [[2604.13395v1]] Uncertainty in Reasoning Models | Li, Zhao, Huai | Uncertainty Quantification | CoRAP共形预测框架量化推理模型推理链-答案不确定性，Shapley值分层解释提供可证明充分性保证。CoRAP quantifies reasoning-answer uncertainty with conformal prediction; Shapley explanations provide provable sufficiency guarantees. |
| 30 | [[2604.13552v1]] TF-TTCL | Zheng et al. | Test-Time Adaptation | 免训练测试时对比学习让冻结LLM通过"探索-反思-引导"循环在线自改进，适用于黑盒API模型。Training-free test-time contrastive learning enabling frozen/black-box LLMs to self-improve via Explore-Reflect-Steer loop. |
| 31 | [[2604.13556v1]] YOCO++ | Wu et al. | Efficient Inference | KV残差连接在50%压缩率下超越标准Transformer性能，零额外解码开销，预填充延迟减半。KV residual connections outperform standard Transformer at 50% KV cache compression with zero extra decoding overhead. |
| 32 | [[2604.13645v1]] Sim-and-Real Co-Training | Lei et al. | Robotics | "结构化表示对齐"是仿真-真实协同训练主导因素（解释50%方差），CFG-ADDA将成功率提升约20%。Structured representation alignment is primary driver in sim-and-real co-training (~50% variance); CFG-ADDA improves success by ~20%. |
| 33 | [[2604.13882v1]] ML Evaluation Pitfalls | Liu et al. | Evaluation | 15个数据集揭示监督学习评估指标不一致现象（准确率虚高、R2掩盖残差结构、MAPE在低基数值不稳定）。15 datasets reveal metric disagreement: inflated accuracy, R2 masking residuals, MAPE instability near zero baselines. |
| 34 | [[2604.13759v1]] Cognitive Companion | Khan, Khan | Agent Monitoring | 零推理开销隐藏状态探针检测LLM代理推理退化，效果依赖任务类型（循环/开放任务有效，结构化任务中性甚至负面）。Zero-overhead hidden-state probes detect agent reasoning degradation; effectiveness depends on task type (positive for loop-prone, neutral/negative for structured). |
| 35 | [[2604.13602v1]] Reward Hacking Survey | Wang et al. (Fudan NLP) | AI Alignment | 代理压缩假说(PCH)统一理解奖励作弊，四级分类（特征/表示/评估器/环境）和全生命周期检测防御框架。Proxy Compression Hypothesis unifies reward hacking understanding with four-level taxonomy and full lifecycle detection/mitigation framework. |
| 36 | [[2604.13694v1]] Weight Patching | Sun et al. | Mechanistic Interpretability | 参数空间Weight Patching揭示指令跟随的层次化分工（浅层MLP源端、中层注意力聚合、下游执行），应用于模型合并。Parameter-space Weight Patching reveals hierarchical source-aggregation-execution structure in instruction following with model merging application. |

---

*Overview generated on 2026-04-17*
