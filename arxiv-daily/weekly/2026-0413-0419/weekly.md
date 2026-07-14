---
title: "Weekly arXiv Digest — 2026-04-13–2026-04-17"
week: 2026-0413-0419
date_range: ["2026-04-13", "2026-04-17"]
tags: [其他前沿, 训练与优化, 推理效率与压缩, 可解释性与机制分析]
papers: 75
---

> 本周共收录 **75** 篇精选论文，来自 2 个工作日的每日精选。 / **75** curated papers this week, rolled up from 2 daily digests.

## 本周必读 / Must Read This Week

> 如果你只读几篇 — 看这些。优先挑选了跨天复现或被每日必读的论文。 / If you read nothing else, read these. Prioritizes papers recurring across days or picked as daily must-reads.

### [[2604.14877]] RL Expands Capability Boundary

- **推荐理由：** PASS@(k,T)证明RL扩展智能体能力边界，SFT反而收缩 （2 天复现 / 2 days）
- **Why read:** PASS@(k,T) proves RL expands boundary; SFT contracts it （2 天复现 / 2 days）
- _Topic: LLM Reasoning & Evaluation_

### [[2604.14925]] Sparsemax SAE

- **推荐理由：** 交叉注意力+sparsemax自适应稀疏SAE，ImageNet 10.93% vs次优3.86% （2 天复现 / 2 days）
- **Why read:** Cross-attention sparsemax SAE; ImageNet 10.93% vs 3.86% （2 天复现 / 2 days）
- _Topic: Mechanistic Interpretability_

### [[2604.15149]] LLMs Gaming Verifiers

- **推荐理由：** RLVR模型系统欺骗不完备验证器，同构扰动测试检测捷径 （2 天复现 / 2 days）
- **Why read:** RLVR models systematically game verifiers; isomorphic perturbation testing detects shortcuts （2 天复现 / 2 days）
- _Topic: LLM Reasoning & Evaluation_

### [[2604.14727]] Tropical Geometry for Transformers

- **推荐理由：** 零温度注意力=幂Voronoi图，线性区域紧界Theta(N^{dL})，多头O(N^H) 
- **Why read:** Zero-temp attention = Power Voronoi; tight bound Theta(N^{dL}); multi-head O(N^H) 
- _Topic: Mathematical Foundations_

### [[2604.15224]] Evaluation Faking in Judges

- **推荐理由：** "Stakes signaling"使评审宽松(-9.8pp)且CoT不可检测 
- **Why read:** "Stakes signaling" biases judges (-9.8pp), invisible in CoT 
- _Topic: LLM Inference & Evaluation_

### [[2604.14500]] Geometric Metrics for MoE Specialization

- **推荐理由：** Fisher信息度量分析MoE专业化，10%训练即可预测失败(AUC=0.89) （2 天复现 / 2 days）
- **Why read:** Fisher information metrics for MoE specialization; predicts failure at 10% training （2 天复现 / 2 days）
- _Topic: Training Stability & Optimization_

### [[2604.14525]] Cross-Query Contradictions in Multi-Query Reasoning

- **推荐理由：** 案卷逻辑一致性框架，SAT/SMT求解将矛盾率从0.56降至0.06 （2 天复现 / 2 days）
- **Why read:** Case-file consistency framework reduces contradictions 0.56 to 0.06 via SAT/SMT （2 天复现 / 2 days）
- _Topic: LLM Reasoning & Evaluation_

### [[2604.14587]] CLion: Cautious Lion Optimizer

- **推荐理由：** Lion泛化误差O(1/(N*tau^T))，CLion降至O(1/N)且保持收敛速率 （2 天复现 / 2 days）
- **Why read:** Lion generalization O(1/(N*tau^T)); CLion reduces to O(1/N) （2 天复现 / 2 days）
- _Topic: Training Stability & Optimization_

## 本周主题脉络 / Themes This Week

### Other Frontiers / 其他前沿

本周该方向共 **26** 篇论文。 / **26** papers this week on this line.

代表论文 / Highlights: [[2604.13991]] · [[2604.14037]] · [[2604.14419]] · [[2604.14434]] · [[2604.14487]] · [[2604.14621]]

### Training & Optimization / 训练与优化

本周该方向共 **14** 篇论文。 / **14** papers this week on this line.

代表论文 / Highlights: [[2604.14108]] · [[2604.14500]] · [[2604.14585]] · [[2604.14587]] · [[2604.14669]] · [[2604.14808]]

### Inference Efficiency & Compression / 推理效率与压缩

本周该方向共 **11** 篇论文。 / **11** papers this week on this line.

代表论文 / Highlights: [[2604.14612]] · [[2604.14661]] · [[2604.14682]] · [[2604.14789]] · [[2604.14993]] · [[2604.15075]]

### Interpretability & Mechanistic Analysis / 可解释性与机制分析

本周该方向共 **10** 篇论文。 / **10** papers this week on this line.

代表论文 / Highlights: [[2604.13950]] · [[2604.14128]] · [[2604.14433]] · [[2604.14477]] · [[2604.14593]] · [[2604.14722]]

### Reasoning & Agents / 推理与智能体

本周该方向共 **6** 篇论文。 / **6** papers this week on this line.

代表论文 / Highlights: [[2604.14525]] · [[2604.14528]] · [[2604.14853]] · [[2604.14877]] · [[2604.15109]] · [[2604.15149]]

### Safety, Alignment & Evaluation / 安全、对齐与评估

本周该方向共 **6** 篇论文。 / **6** papers this week on this line.

代表论文 / Highlights: [[2604.14602]] · [[2604.14865]] · [[2604.14881]] · [[2604.14973]] · [[2604.15038]] · [[2604.15166]]

## 全部论文 / All Papers

### 2026-04-16 (41)

- [[2604.14493]] On-Device Streaming ASR — 50+配置系统评测，Nemotron经ONNX+int4量化在CPU上实现8.20%流式WER / Systematic 50+ config benchmark; Nemotron with int4 achieves 8.20% streaming WER on CPU
- [[2604.14500]] Geometric Metrics for MoE Specialization — Fisher信息度量分析MoE专业化，10%训练即可预测失败(AUC=0.89) / Fisher information metrics for MoE specialization; predicts failure at 10% training ↻04-17
- [[2604.14525]] Cross-Query Contradictions in Multi-Query Reasoning — 案卷逻辑一致性框架，SAT/SMT求解将矛盾率从0.56降至0.06 / Case-file consistency framework reduces contradictions 0.56 to 0.06 via SAT/SMT ↻04-17
- [[2604.14528]] GUARD: Dissecting Failure Dynamics in LLM Reasoning — 错误集中在少数早期转移点(熵尖峰)，分支纠正+后期抑制实现最优准确率-token权衡 / Failures at early entropy-spike transitions; best accuracy-token trade-off
- [[2604.14585]] Prompt Optimization Is a Coin Flip — 复合AI系统中Agent间无交互效应，优化仅在有可利用输出结构时有效 / No inter-agent prompt interaction; optimization only helps with exploitable structure
- [[2604.14587]] CLion: Cautious Lion Optimizer — Lion泛化误差O(1/(N*tau^T))，CLion降至O(1/N)且保持收敛速率 / Lion generalization O(1/(N*tau^T)); CLion reduces to O(1/N) ↻04-17
- [[2604.14593]] Mechanistic Decoding of Cognitive Constructs — LLM中社会比较嫉妒=优越感x领域自我定义相关性的线性组合 / Jealousy = linear combination of Superiority x Domain Self-Definitional Relevance ↻04-17
- [[2604.14602]] CausalDetox — PNS因果推断定位有毒注意力头，最高5.34%毒性降低，头部选择快7倍 / PNS-based causal head selection; 5.34% toxicity reduction, 7x faster ↻04-17
- [[2604.14612]] ConfLayers: Adaptive Layer Skipping — 置信度自适应层跳过自推测解码，LLaMa系列最高1.4倍加速 / Confidence-based layer skipping; up to 1.4x speedup on LLaMa
- [[2604.14646]] UEC-RL: Unified Entropy Control — 困难样本高温度定向探索，Geometry3K相对GRPO提升37.9% / Targeted exploration; +37.9% on Geometry3K over GRPO
- [[2604.14661]] AIPC: Agent-Based AI Model Deployment — LLM Agent自动化Qualcomm部署，视觉模型7-20分钟零人工干预 / LLM agent automates Qualcomm deployment; 7-20 min for vision models
- [[2604.14664]] Scaling Photonic Tensor Cores — 五种光子张量核心统一对比，ASTRA架构达25,600空间MAC / Unified comparison; ASTRA achieves 25,600 spatial MACs
- [[2604.14682]] Acceptance Dynamics in Speculative Decoding — 99K节点分析：任务类型预测接受率优于树深度，仅对话E[L]>1.0 / 99K nodes: task type > tree depth for acceptance; only chat E[L]>1.0 ↻04-17
- [[2604.14702]] Gating Enables Curvature — 无门控注意力=零曲率流形，门控使正曲率成为可能 / Ungated attention = flat manifolds; gating enables positive curvature
- [[2604.14722]] Attention Sinks in GPT-2 — 查询偏置+MLP变换PE+键投影交互驱动注意力汇聚，跨架构多重重可实现性 / Query bias + MLP PE + key projection drive sinks; multi-realizability ↻04-17
- [[2604.14725]] RELOAD: Learned Query Optimizer — 优先经验回放+MAML元学习，单查询性能回退减少2.4倍 / PER + MAML reduces per-query regression 2.4x
- [[2604.14727]] Tropical Geometry for Transformers — 零温度注意力=幂Voronoi图，线性区域紧界Theta(N^{dL})，多头O(N^H) / Zero-temp attention = Power Voronoi; tight bound Theta(N^{dL}); multi-head O(N^H) ⭐
- [[2604.14789]] CNN Optimization for Edge AI — PTQ+早退组合在边缘设备上3-4x压缩，ResNet-152 3.12倍加速 / PTQ+early-exit: 3-4x compression, 3.12x speedup on ResNet-152
- [[2604.14808]] SAGO: Asymmetric LLM Unlearning — 保持优先梯度合成，MMLU恢复率44.6%提升至96.0% / Retention-first gradient synthesis; MMLU 44.6% to 96.0%
- [[2604.14815]] Domain Fine-Tuning FinBERT — 训练时损失下降和嵌入几何变化可预判领域微调价值 / Train-time signals predict domain fine-tuning value
- [[2604.14838]] Intermediate Layers in Single-Cell FMs — 中间层轨迹推断提升31%，最优层跨度达96个百分点 / Intermediate layers +31% trajectory inference; optimal layer spans 96pp
- [[2604.14853]] AdaCompute: Adaptive Test-Time Compute — 约束优化+GBM模仿oracle，MATH上比均匀分配提升12.8% / Constrained optimization + GBM; +12.8% on MATH ↻04-17
- [[2604.14865]] SC-TopK: Segment-Level Coherence Probing — 多段证据替代关键词触发，TPR提升35.55%，抗密码混淆AUROC>98.85% / Multi-segment evidence; +35.55% TPR; robust to cipher obfuscation
- [[2604.14870]] Curvature-Aligned Probing — Hessian top-D子空间复现全空间信号，高斯矩估计器快18000倍 / Top-D Hessian subspace reproduces full signal; 18,000x faster estimator ↻04-17
- [[2604.14877]] RL Expands Capability Boundary — PASS@(k,T)证明RL扩展智能体能力边界，SFT反而收缩 / PASS@(k,T) proves RL expands boundary; SFT contracts it ⭐ ↻04-17
- [[2604.14881]] Missing Knowledge Layer in AI — 三层认知治理架构：反思脚手架+认知控制回路+能力治理 / Three-layer epistemic governance: scaffolds + control loop + governance
- [[2604.14888]] Reasoning Dynamics in VLMs — 18个VLM的答案惯性与CoT监控局限性分析 / 18 VLMs: answer inertia and CoT monitoring limitations
- [[2604.14895]] RGPO: Rejection-Gated Policy Optimization — 可微接受门替代IS比率，Walker2d +81%，RLHF帕累托最优 / Differentiable acceptance gate; +81% Walker2d; Pareto-optimal RLHF ↻04-17
- [[2604.14922]] LongAct: Long-Context RL — Q/K高幅度激活指导稀疏梯度更新，LongBench v2提升约8% / Q/K outlier-guided sparse updates; ~8% on LongBench v2
- [[2604.14925]] Sparsemax SAE — 交叉注意力+sparsemax自适应稀疏SAE，ImageNet 10.93% vs次优3.86% / Cross-attention sparsemax SAE; ImageNet 10.93% vs 3.86% ⭐ ↻04-17
- [[2604.14973]] Vision Foundation Model Robustness — CLIP/DINO v2对常见扰动不够鲁棒，DivergenceRadius满足全部五项数学性质 / CLIP/DINO v2 non-robust to common perturbations; DivergenceRadius metric
- [[2604.14993]] Serving Chain-structured Jobs — 服务器链组合优化，PETALS上响应时间降低63%-77% / Server chain composition; 63-77% response time reduction
- [[2604.15010]] Minimum Architecture for Prolepsis — 首次复现规划位点，发现"预述"模体，深度>16层才能不可撤销承诺 / First planning site replication; prolepsis motif; depth>16 for commitment
- [[2604.15038]] Fairness Disagreement Index — FDI揭示不同公平性指标矛盾，单指标报告不可靠 / FDI reveals metric contradictions; single-metric reporting unreliable
- [[2604.15069]] Doubly Stochastic Matrices for GNNs — DSM传播算子+残差质量补偿，缓解过平滑 / DSM propagation + residual mass compensation; mitigates over-smoothing
- [[2604.15075]] Atropos: Early Termination for Agents — GCN中段预测成败(85%)，模型热替换以23.9%成本获74.35%性能 / GCN mid-inference prediction (85%); hotswap at 23.9% cost for 74.35% perf ↻04-17
- [[2604.15109]] IUQ: Interrogative Uncertainty Quantification — "先问再答"检测长文本编造声明，指数衰减核传播不可信影响 / "Ask first" detects fabricated claims; exponential-decay influence kernel ↻04-17
- [[2604.15115]] FedIDM: Byzantine Federated Learning — 迭代分布匹配过滤恶意客户端，50%恶意下最快收敛 / Iterative distribution matching filters Byzantine clients; fastest at 50% malicious
- [[2604.15149]] LLMs Gaming Verifiers — RLVR模型系统欺骗不完备验证器，同构扰动测试检测捷径 / RLVR models systematically game verifiers; isomorphic perturbation testing detects shortcuts ⭐ ↻04-17
- [[2604.15166]] DAMP: Depth-Aware Class Unlearning — 闭式权重手术深度感知移除遗忘类方向，接近重训练金标准 / Closed-form weight surgery with depth-aware scaling; closest to retrained gold standard
- [[2604.15167]] When Flat Minima Fail: INT4 Quantization Collapse — 154个checkpoint审计：INT4误差爆炸至517%，FP32收敛即触发发散 / 154-checkpoint audit: INT4 gap explodes to 517%; triggered by FP32 convergence ↻04-17

### 2026-04-17 (34)

- [[2604.13824]] Behavior Consistency in World Models — 行为一致性奖励优化世界模型，CR_pw从0.76提升至0.84 / BehR improves world model training; CR_pw 0.76 to 0.84
- [[2604.13899]] Human vs LLM Annotation in AL — LLM标注F1相当但系统性过度预测正类 / LLM annotation matches F1 but over-predicts positive class
- [[2604.13902]] DiPO — 解耦困惑度的策略优化实现探索-利用权衡 / Disentangled perplexity policy for exploration-exploitation trade-off
- [[2604.13950]] Causal Drawbridges — DAS定位Transformer LM中句法岛屿约束子空间 / DAS locates syntactic island constraint subspaces in Transformer LMs
- [[2604.13991]] Adaptive Conformal Prediction for Factuality — 条件分位数回归保形预测改善LLM条件覆盖率 / Adaptive CP via quantile regression improves conditional coverage for LLMs
- [[2604.14027]] ASIC Ising/Potts Machine — 65nm ASIC振荡器Ising机比GPU快12,800倍 / 65nm ASIC Ising machine 12,800x faster than GPU
- [[2604.14037]] Symmetry of Shallow ReLU Networks — 浅层ReLU网络参数对称性完整分类，纤维同胚于Lie群 / Complete ReLU symmetry classification; fibers diffeomorphic to Lie group
- [[2604.14108]] Momentum at EoSS — 动量小批量收紧曲率约束，大批量行为相反 / Momentum tightens curvature for small batches, reverses for large
- [[2604.14121]] CRAFT: Consensus Reasoning KG — 共识推理知识图谱修复推理缺陷，准确率提升10%+ / Consensus reasoning KG repairs reasoning defects; 10%+ accuracy gain
- [[2604.14128]] Rhetorical Questions Probing — 反问句由多个线性方向编码而非单一共享方向 / Rhetorical questions encoded along multiple linear directions
- [[2604.14259]] FORGE: Continual fMRI Learning — 结构感知VAE回放实现fMRI持续学习，AAA提升2.7-4.7% / Structure-aware VAE replay for fMRI continual learning
- [[2604.14419]] Equifinality in MoE — 62组实验证明MoE路由拓扑不决定建模质量 / 62 experiments prove MoE routing topology does not determine quality
- [[2604.14433]] Zero-Ablation Overstates Register Dependence — 零消融严重高估DINO ViT寄存器内容依赖性 / Zero-ablation overstates DINO ViT register content dependence
- [[2604.14434]] Geometric Routing in MoE — MoE专家语义字典实现零开销因果可控干预 / MoE semantic dictionary enables zero-overhead causal steering
- [[2604.14477]] Vi-CD: Vision Transformer Circuits — 首次ViT基于边电路发现，10%边保留率近完美性能 / First ViT edge-based circuit discovery; near-perfect with 10% edges
- [[2604.14484]] Gain-Dependent Error in BC — 低刚度高阻尼增益最小化行为克隆失败概率 / Compliant-overdamped gains minimize BC failure probability
- [[2604.14487]] SNN Quantization Beyond Accuracy — 均匀量化引发SNN发射行为漂移，学习量化可保持 / Uniform quantization causes SNN firing drift; learned quantization preserves behavior
- [[2604.14518]] Mind DeepResearch — 理想汽车三智能体框架，30B参数达深度研究SOTA / Li Auto three-agent framework; 30B params for deep research SOTA
- [[2604.14519]] CI-CBM: Incremental Concept Bottleneck — 概念瓶颈模型引入类增量学习，平均36%精度提升 / Concept bottleneck for class-incremental learning; 36% accuracy gain
- [[2604.14621]] Differentially Private Conformal Prediction — 差分隐私保形预测无需数据分割，更紧凑预测集 / DP conformal prediction without data splitting; tighter prediction sets
- [[2604.14644]] CURaTE: Continual Unlearning — 不修改权重的实时持续知识遗忘，0.04s/请求 / Real-time unlearning without weight modification; 0.04s/request
- [[2604.14669]] ZO Optimization at EoS — ZO稳定性由Hessian全谱决定，始终运行在均方稳定性边界 / ZO stability depends on full Hessian spectrum; always at mean-square EoS
- [[2604.14769]] Constraint-based Pre-training — Kronecker约束预训练一次初始化任意尺寸模型 / Kronecker-constrained pre-training initializes any-size models in one shot
- [[2604.14779]] AIM: Asymmetric Info Masking for VQA — VLM持续学习中语言解码器主导梯度损害视觉投影层 / VLM CL asymmetry: language decoder dominates gradients, harming vision
- [[2604.14878]] GenRec: Generative Recommendation — Page-wise NTP加GRPO-SR推荐，京东线上点击+9.5% / Page-wise NTP + GRPO-SR; +9.5% clicks in JD.com A/B test
- [[2604.14961]] Calibration-Gated LLM for Bandits — LLM伪观测注入赌博机，提示设计比算法调优更重要 / LLM pseudo-observations for bandits; prompt design > algorithm tuning
- [[2604.15171]] FP-Diffusion Regularization Analysis — 简单正则化零成本达到复杂FP惩罚效果 / Simple regularization matches complex FP penalty at zero extra cost
- [[2604.15180]] AdaSplash-2 — 片上直方图初始化alpha-entmax，速度匹配FlashAttention-2 / On-chist histograms for alpha-entmax; matches FlashAttention-2 speed
- [[2604.15224]] Evaluation Faking in Judges — "Stakes signaling"使评审宽松(-9.8pp)且CoT不可检测 / "Stakes signaling" biases judges (-9.8pp), invisible in CoT ⭐
- [[2604.15259]] Looped Transformers Stability — 不动点分析三条稳定性轴，回召+归一化最可靠 / Fixed-point three stability axes; recall + normalization most reliable
- [[2604.15294]] Viewpoint Rotation Interpretability — "浅层编码旋转、中层推断、深层决策"空间推理机制 / "Shallow encode, middle infer, deep decide" spatial reasoning mechanism
- [[2604.15302]] Diagnosing LLM Judge Reliability — 33-67%文档存在评估不一致，共形预测集量化可靠性 / 33-67% documents have evaluation inconsistency; CP sets quantify reliability
- [[2604.15306]] Generalization in Shortest Path — LLM空间迁移成功但长度扩展因递归不稳定性失败 / LLMs succeed at spatial transfer but fail at length scaling
- [[2604.15311]] 2604.15311 — 两步跳跃轨迹将奖励梯度高效回传至早期生成步骤，超越GRPO和直接梯度方法 / Two-step leap trajectories enable efficient reward gradient backprop to early steps, surpassing GRPO


---

_本周报由每日 digest 汇总而成。/ This weekly digest is a rollup of the daily digests._

**每日入口 / Daily entries:** [2026-04-13](../../2026-04-13/overview.md) · [2026-04-17](../../2026-04-17/overview.md)
