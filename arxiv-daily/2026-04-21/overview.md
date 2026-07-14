---
title: "Daily arxiv Papers — 2026-04-21"
date: "2026-04-21"
tags:
  - training-stability
  - mechanistic-interpretability
  - quantization
  - inference-efficiency
  - reliability
  - evaluation
  - preference-optimization
  - fairness
  - model-compression
  - random-matrix-theory
papers: 29
---

## 今日必读 / Must Read Today

| # | Paper | 为什么必读 / Why You Must Read |
|---|-------|-------------------------------|
| 1 | [[2604.16809]] — Delayed Loss Spikes in BN Linear Models | **训练稳定性理论突破 / Training Stability Theory Breakthrough**: 首次从定理层面证明BatchNorm通过逐步放大有效学习率引发延迟方向性不稳定，并证明不稳定会在有限步内因负反馈自我稳定，为理解大模型预训练中的loss spike提供了具体机制路径。First theorem-level proof that BN induces delayed directional instability via gradual effective learning rate increase, with guaranteed finite-time self-stabilization through negative feedback. |
| 2 | [[2604.17849]] — Reliability of Computer Use Agents | **智能体可靠性系统化评估 / Systematic Agent Reliability Evaluation**: 提出Pass^k指标和三因素不可靠性分解框架，在OSWorld上评估6种前沿模型，发现指令澄清是最有效的可靠性干预，揭示当前CUA仍存在显著可靠性差距。Introduces Pass^k metrics and three-factor unreliability decomposition; finds instruction clarification most effective, revealing significant reliability gaps in current CUAs. |
| 3 | [[2604.18493]] — Too Correct to Learn: RL on Saturated Reasoning Data | **RL训练信号消失诊断 / RL Training Signal Vanishing Diagnosis**: 发现GRPO在饱和推理数据上因所有轨迹都正确导致优势信号消失的"饱和诱导坍塌"问题，提出Mixed-CUTS双流框架在AIME25上Pass@1提升15.1%。Diagnoses saturation-induced collapse in GRPO where all-correct trajectories kill advantage signals; Mixed-CUTS boosts AIME25 Pass@1 by 15.1%. |

---

## 按主题分类 / Papers by Topic

### A. 训练稳定性与优化理论 / Training Stability & Optimization Theory

| Paper | 主题描述 / Topic | 关键贡献 / Key Contribution |
|-------|-----------------|-----------------------------|
| [[2604.16809]] Delayed Loss Spikes in BN Linear Models | BatchNorm导致的延迟loss spike机制 / Delayed loss spike mechanism induced by BatchNorm | 证明BN通过逐步增大有效学习率引发延迟方向性不稳定，并保证有限步内自我稳定 / Proves BN induces delayed directional instability via rising effective LR, with finite-time self-stabilization guarantees |
| [[2604.18235]] CalibAdv: Calibrating Advantage in GRPO | GRPO训练中的优势校准与稳定性 / Advantage calibration and stability in GRPO training | 揭示负优势主导导致训练崩溃的机理，提出三组件校准方法，平均F1相对提升11.80% / Reveals negative-advantage-dominance collapse mechanism; three-component calibration yields 11.80% avg F1 improvement |
| [[2604.18493]] Too Correct to Learn | 饱和数据上的RL训练信号消失 / RL training signal vanishing on saturated data | 诊断GRPO在饱和数据上的优势信号消失问题，提出Mixed-CUTS在AIME25提升15.1% / Diagnoses vanishing advantage in GRPO on saturated data; Mixed-CUTS boosts AIME25 by 15.1% |
| [[2604.18239]] Disentangled Preference Optimization | 偏好优化中的likelihood位移动力学 / Likelihood displacement dynamics in preference optimization | 统一激励-分数分解揭示不同目标共享更新方向仅标量权重不同；解耦带(DB)条件+即插即用奖励校准(RC)在Mistral-7B将DPO从24.26提升到36.44(+12.18) / Unified incentive-score decomposition; disentanglement band + plug-and-play reward calibration lifts Mistral-7B DPO 24.26→36.44 (+12.18) |
| [[2604.18450]] RMT of Early-Stopped Gradient Flow | 早停现象的随机矩阵理论 / Random matrix theory for early stopping | 两块各向异性协方差下用2×2 Dyson方程和rank-two行列式条件解析出瞬态BBP相变，给出三种学习相的完整相图与最优停时 / Solves transient BBP transition via 2×2 Dyson equation and rank-two determinant; full phase diagrams of three learning regimes |

### B. 机制可解释性与隐藏状态分析 / Mechanistic Interpretability & Hidden State Analysis

| Paper | 主题描述 / Topic | 关键贡献 / Key Contribution |
|-------|-----------------|-----------------------------|
| [[2604.17837]] Polysemantic Experts, Monosemantic Paths | MoE路由的因果分解与轨迹单义性 / Causal decomposition of MoE routing and trajectory monosemanticity | 无参数SVD分解将MoE残差流正交拆分为控制信号与内容通道，证明专家轨迹（而非单个专家）是可解释性的基本单元 / Parameter-free SVD decomposition splits MoE residual stream into control/content channels; proves trajectories (not experts) are the interpretability unit |
| [[2604.18307]] Reasoning Models Know What's Important | 推理步骤重要性的激活编码 / Activation encoding of reasoning step importance | 探针准确率80%+预测步骤重要性，信号跨模型迁移且不与表面特征相关 / Probes achieve 80%+ accuracy predicting step importance; signal transfers cross-model and is uncorrelated with surface features |
| [[2604.17761]] Contrastive Attribution in the Wild | LLM失败案例的对比归因分析 / Contrastive attribution analysis of LLM failures | 将LLM失败分析形式化为LRP对比归因问题，发现token级归因并非普遍适用 / Formulates LLM failure analysis as LRP contrastive attribution; finds token-level attribution is not universally applicable |
| [[2604.18158]] State Transfer Reveals Reuse | 注意力头K/V状态的零重训练迁移 / Zero-retrain transfer of attention head K/V states | K/V向量可零重训练迁移至新上下文，证明固定接口的"编译式迁移"机制 / K/V vectors transfer zero-retrain to new contexts, proving fixed-interface compiled transfer mechanism |
| [[2604.18519]] SIREN: Safety From Within | LLM内部安全神经元识别 / Identifying safety neurons inside LLMs | L1正则化探针识别多层安全神经元，超越LlamaGuard3和Qwen3Guard / L1-regularized probes identify multi-layer safety neurons, outperforming LlamaGuard3 and Qwen3Guard |
| [[2604.18563]] Dual Alignment: LM Layers & Human Processing | LM层级与人类句子处理的双重对齐 / Dual alignment between LM layers and human sentence processing | 自然阅读与早期层对齐，句法歧义处理与后期层对齐，挑战最终层surprisal作为统一认知度量 / Natural reading aligns with early layers, ambiguity resolution with later layers; challenges final-layer surprisal as universal cognitive proxy |
| [[2604.18567]] LPSR: Latent Phase-Shift Rollback | 残差流监控的推理错误实时纠错 / Real-time reasoning error correction via residual stream monitoring | 监控残差流相位反转信号回退KV-Cache注入校正向量，8B模型在MATH-500达44.0%超越70B / Monitors phase shifts in residual stream to rollback and inject corrections; 8B model hits 44.0% on MATH-500, surpassing 70B |

### C. 推理效率与模型压缩 / Inference Efficiency & Model Compression

| Paper | 主题描述 / Topic | 关键贡献 / Key Contribution |
|-------|-----------------|-----------------------------|
| [[2604.18103]] DASH: Delta Attention Selective Halting | 免训练的token选择性停止 / Training-free token selective halting | 监控注意力更新幅度在语义不动点后停止token计算，1.74-1.89x加速 / Monitors attention update magnitudes to halt tokens at semantic fixed points; 1.74-1.89x speedup |
| [[2604.18396]] River-LLM | 无训练LLM早退框架 / Training-free LLM early exit framework | KV-Shared Exit River让跳过层KV cache在退出过程自然生成(>0.97余弦相似度)，状态转移相似度指导退出，1.71-2.16x实际加速且近乎无损 / KV-Shared Exit River synthesizes skipped-layer KV (>0.97 cosine); state-transition-similarity exit; 1.71-2.16x practical speedup near-lossless |
| [[2604.17224]] LASER: Low-Rank Activation SVD | 递归模型的激活低秩压缩 / Activation low-rank compression for recursive models | 递归推理激活占据低维子空间，LASER实现约60%激活内存节省 / Recursive reasoning activations occupy low-dim subspace; LASER achieves ~60% activation memory savings |
| [[2604.18092]] Generalization Boundaries of Fine-Tuned SLMs | 微调小模型在图推理上的泛化边界 / Generalization boundaries of fine-tuned SLMs on graph reasoning | 3-4B模型跨图族保持ρ>0.88、尺寸外推到n=150保持ρ>0.74；邻接表编码始终优于边表且差距随尺寸扩大；序一致性比数值精度衰减更平缓 / 3-4B models keep ρ>0.88 cross-family and ρ>0.74 to n=150; adjacency-list beats edge-list; ordinal consistency degrades more gracefully than magnitude |

### D. 量化与数值精度 / Quantization & Numerical Precision

| Paper | 主题描述 / Topic | 关键贡献 / Key Contribution |
|-------|-----------------|-----------------------------|
| [[2604.18117]] LoRaQ | 全量化4-bit扩散Transformer / Fully quantized 4-bit diffusion transformers | 首个全低于16位量化流程，低秩补偿分支本身也可量化，超越Q-PTQ和LoRA-Q / First fully sub-16-bit quantization pipeline; compensation branch itself quantized, outperforming Q-PTQ and LoRA-Q |
| [[2604.18128]] Depth Registers for W4A4 on SwiGLU | SwiGLU的读取器/生成器分解与W4A4 / Reader/generator decomposition for SwiGLU W4A4 | 将SwiGLU层分解为读取器和生成器，Depth Registers将W4A4 PPL从1727降至39.9 / Decomposes SwiGLU layers into readers/generators; Depth Registers reduce W4A4 PPL from 1727 to 39.9 |
| [[2604.18556]] GSQ: Gumbel-Softmax Quantization | Gumbel-Softmax可微标量量化 / Differentiable scalar quantization via Gumbel-Softmax | 将离散网格分配转化为可微优化，2-bit接近VQ方法精度，成功扩展至万亿参数MoE / Converts discrete grid assignment to differentiable optimization; 2-bit approaches VQ accuracy, scales to trillion-param MoE |
| [[2604.18085]] Predicting LLM Compression Degradation | 基于谱统计量预测压缩退化 / Predicting compression degradation from spectral statistics | 交互项 gamma*rho_s 在注意力层LOO-CV Pearson R=0.890预测精度退化 / Interaction term gamma*rho_s achieves LOO-CV Pearson R=0.890 for predicting accuracy degradation in attention layers |
| [[2604.18555]] TurboQuant vs DRIVE/EDEN | 量化方法优先关系澄清 / Clarifying quantization method priority | 证明TurboQuant是更早的EDEN的特例和次优变体，EDEN在所有场景中均优 / Proves TurboQuant is a special case and suboptimal variant of earlier EDEN; EDEN outperforms in all tested settings |

### E. 可靠性评估与基准 / Reliability Evaluation & Benchmarks

| Paper | 主题描述 / Topic | 关键贡献 / Key Contribution |
|-------|-----------------|-----------------------------|
| [[2604.17849]] Reliability of Computer Use Agents | 计算机使用智能体的可靠性 / Reliability of computer use agents | Pass^k指标和三因素分解，发现指令澄清是最有效干预，前沿模型仍有显著可靠性差距 / Pass^k metrics and three-factor decomposition; instruction clarification most effective; frontier models still unreliable |
| [[2604.18245]] Correction and Corruption in LLM Protocols | LLM协议中的校正-腐化双指标 / Correction-corruption dual metrics for LLM protocols | 提出校正率c和腐化率gamma分解，揭示高基线下腐化被放大的关键现象 / Proposes correction rate c and corruption rate gamma decomposition; reveals corruption amplification at high baselines |
| [[2604.18164]] MM-JudgeBias | 多模态评判的组合偏差基准 / Compositional bias benchmark for multimodal judgment | 定义3维度9种组合偏差，评估26个MLLM，发现图像相关偏差最严重 / Defines 3-dimension 9-type compositional biases; evaluates 26 MLLMs; image-related biases most severe |
| [[2604.18389]] Understanding Prompt Sensitivity | 提示敏感性的理论分析 / Theoretical analysis of prompt sensitivity | 推导提示变化导致log概率差异的上界，发现模板影响大于问题内容，LLM隐藏状态分散而非聚类 / Derives upper bounds for log-prob differences from prompt changes; templates matter more than questions; LLM hidden states disperse rather than cluster |

### F. 可解释性与探测方法 / Interpretability & Probing Methods

| Paper | 主题描述 / Topic | 关键贡献 / Key Contribution |
|-------|-----------------|-----------------------------|
| [[2604.18109]] FLiP: Multimodal Sentence Embeddings | 句子嵌入的词汇内容恢复与诊断 / Lexical content recovery and diagnosis from sentence embeddings | 因子化线性投影从嵌入中恢复75%+词汇内容，揭示SONAR的英语中心偏差 / Factorized linear projection recovers 75%+ lexical content from embeddings; reveals SONAR's English-centric bias |
| [[2604.18249]] Where Do S3Ms Become Unfair? | 自监督语音模型的逐层公平性 / Layerwise fairness of self-supervised speech models | SID偏置在浅层最小，ASR偏置在深层最大，偏置在预训练阶段已固化 / SID bias lowest at shallow layers, ASR bias highest at deep layers; bias baked in during pretraining |
| [[2604.17694]] Random Seed Stability via Bagging | 随机种子稳定性与可复现性 / Random seed stability and reproducibility | (ε,δ)浓度条件形式化种子稳定性，Theorem 1证明subbagging保证任意有界回归算法稳定，adaptive cross-bagging在AIPW达r=1.04(目标1)且比LOO+平均快约20× / (ε,δ) concentration condition; Theorem 1 proves subbagging stabilizes any bounded regressor; adaptive cross-bagging hits r=1.04 vs 90.5 (2-fold), ~20× faster than LOO+averaging |

### G. 模型合并与对齐 / Model Merging & Alignment

| Paper | 主题描述 / Topic | 关键贡献 / Key Contribution |
|-------|-----------------|-----------------------------|
| [[2604.17753]] ENMP: Evolutionary Negative Module Pruning | LoRA合并中的负模块剪除 / Negative module pruning in LoRA merging | 发现"负模块"现象，CMA-ES进化搜索在合并前定位剪除有害模块，NLP上DARE +6.97/KnOTS达97.29 SOTA，视觉上KnOTS +5.54%，零推理开销 / Discovers negative modules; CMA-ES prunes detrimental modules; DARE +6.97, KnOTS 97.29 SOTA on NLP, +5.54% on vision; zero inference overhead |

---

## All Papers

| arxiv_id | Title | 一句话总结 / One-line Summary |
|----------|-------|-------------------------------|
| [[2604.16809]] | Delayed Loss Spikes in BN Linear Models | 证明BN通过逐步放大有效学习率引发延迟方向性不稳定并在有限步内自稳定 / Proves BN induces delayed directional instability via rising effective LR with finite-time self-stabilization |
| [[2604.17224]] | LASER: Low-Rank Activation SVD | 递归模型激活占据低维子空间，LASER动态压缩框架实现约60%内存节省 / Recursive model activations lie in low-dim subspace; LASER achieves ~60% memory savings |
| [[2604.17694]] | Random Seed Stability via Bagging | (ε,δ)形式化种子稳定性，subbagging保证有界算法稳定，adaptive cross-bagging消除debiased ML种子依赖达r=1.04 / (ε,δ) formalizes seed stability; subbagging guarantees bounded-algorithm stability; adaptive cross-bagging eliminates seed dependence at r=1.04 |
| [[2604.17753]] | ENMP: Evolutionary Negative Module Pruning | 发现LoRA合并中的"负模块"现象，CMA-ES进化搜索剪除有害模块，NLP DARE +6.97/KnOTS达97.29 SOTA / Discovers negative modules; CMA-ES prunes detrimental modules; DARE +6.97, KnOTS 97.29 SOTA on NLP |
| [[2604.17761]] | Contrastive Attribution in the Wild | LRP对比归因用于LLM失败分析，token级归因有信息但在部分案例中解释力有限 / LRP contrastive attribution for LLM failure analysis; informative in some cases but not universally applicable |
| [[2604.17837]] | Polysemantic Experts, Monosemantic Paths | MoE残差流分解为控制信号和内容通道，专家轨迹是可解释性基本单元 / MoE residual stream decomposed into control/content channels; trajectories are interpretability unit |
| [[2604.17849]] | Reliability of Computer Use Agents | Pass^k指标和三因素不可靠性分解，指令澄清是最有效干预手段 / Pass^k metrics and three-factor decomposition; instruction clarification most effective intervention |
| [[2604.18085]] | Predicting LLM Compression Degradation | gamma*rho_s交互项Pearson R=0.890预测压缩退化，支持"先预测再压缩"工作流 / gamma*rho_s interaction term (R=0.890) predicts compression degradation; enables predict-then-compress workflow |
| [[2604.18092]] | Generalization Boundaries of Fine-Tuned SLMs | 微调3-4B模型在图推理上跨图族保持ρ>0.88、尺寸外推保持ρ>0.74，邻接表编码始终优于边表 / Fine-tuned 3-4B models keep ρ>0.88 cross-family and ρ>0.74 to n=150; adjacency-list consistently beats edge-list |
| [[2604.18103]] | DASH: Delta Attention Selective Halting | 免训练token选择性停止，监控注意力更新实现1.74-1.89x推理加速 / Training-free token halting via attention update monitoring; 1.74-1.89x inference speedup |
| [[2604.18109]] | FLiP: Multimodal Sentence Embeddings | 因子化线性投影恢复75%+嵌入词汇内容，揭示编码器模态和语言偏差 / Factorized projection recovers 75%+ lexical content; reveals modality and language biases in encoders |
| [[2604.18117]] | LoRaQ: 4-bit Quantization | 首个全低于16位量化流程，低秩补偿分支本身可量化，超越SOTA / First fully sub-16-bit pipeline; compensation branch itself quantized; outperforms SOTA |
| [[2604.18128]] | Depth Registers for W4A4 on SwiGLU | SwiGLU读取器/生成器分解，Depth Registers将W4A4 PPL从1727降至39.9 / SwiGLU reader/generator decomposition; Depth Registers reduce W4A4 PPL from 1727 to 39.9 |
| [[2604.18158]] | State Transfer Reveals Reuse | K/V向量零重训练迁移证明固定接口编译式迁移机制 / K/V zero-retrain transfer proves fixed-interface compiled transfer mechanism in attention heads |
| [[2604.18164]] | MM-JudgeBias | 3维度9种组合偏差基准评估26个MLLM评判者，图像相关偏差最严重 / 3-dim 9-type compositional bias benchmark; 26 MLLMs evaluated; image biases most severe |
| [[2604.18235]] | CalibAdv: Calibrating Advantage in GRPO | 校准GRPO优势信号解决训练崩溃，平均F1相对提升11.80% / Calibrates GRPO advantage to prevent collapse; 11.80% avg relative F1 improvement |
| [[2604.18239]] | Disentangled Preference Optimization | 统一激励-分数分解揭示偏好优化共享更新方向仅标量权重不同，解耦带(DB)+奖励校准(RC)在Mistral-7B将DPO 24.26→36.44 / Unified incentive-score decomposition; disentanglement band + reward calibration lifts Mistral-7B DPO 24.26→36.44 |
| [[2604.18245]] | Correction and Corruption in LLM Protocols | 校正率-腐化率双指标框架揭示高基线下腐化放大现象 / Correction-corruption framework reveals corruption amplification at high baselines |
| [[2604.18249]] | Where Do S3Ms Become Unfair? | 语音模型逐层公平性分析，ASR偏置与性能成反比且预训练即固化 / Layerwise fairness analysis; ASR bias inversely correlates with performance; baked in during pretraining |
| [[2604.18307]] | Reasoning Models Know What's Important | 推理模型在激活中编码步骤重要性，探针80%+准确率且跨模型迁移 / Reasoning models encode step importance in activations; probes 80%+ accuracy with cross-model transfer |
| [[2604.18389]] | Understanding Prompt Sensitivity | 推导提示敏感性理论上界，发现模板影响大于问题，LLM隐藏状态分散 / Derives upper bounds for prompt sensitivity; templates dominate; LLM hidden states disperse |
| [[2604.18396]] | River-LLM | KV-Shared Exit River让跳过层KV自然生成(>0.97相似度)，1.71-2.16x实际加速近乎无损 / KV-Shared Exit River synthesizes skipped-layer KV (>0.97 similarity); 1.71-2.16x practical speedup near-lossless |
| [[2604.18450]] | RMT of Early-Stopped Gradient Flow | 随机矩阵理论用2×2 Dyson方程和rank-two行列式解析瞬态BBP相变，三种学习相完整相图 / RMT solves transient BBP transition via 2×2 Dyson equation and rank-two determinant; full phase diagrams of three learning regimes |
| [[2604.18493]] | Too Correct to Learn | GRPO在饱和数据上优势信号消失，Mixed-CUTS在AIME25提升15.1% / GRPO advantage vanishes on saturated data; Mixed-CUTS boosts AIME25 by 15.1% |
| [[2604.18519]] | SIREN: Safety From Within | L1探针识别多层安全神经元，超越LlamaGuard3和Qwen3Guard / L1 probes identify multi-layer safety neurons; outperforms LlamaGuard3 and Qwen3Guard |
| [[2604.18555]] | TurboQuant vs DRIVE/EDEN | 证明TurboQuant是EDEN的次优特例，EDEN在所有场景中均优 / Proves TurboQuant is suboptimal special case of EDEN; EDEN wins in all settings |
| [[2604.18556]] | GSQ: Gumbel-Softmax Quantization | Gumbel-Softmax可微标量量化，2-bit接近VQ精度，扩展至万亿参数MoE / Differentiable scalar quantization; 2-bit approaches VQ accuracy; scales to trillion-param MoE |
| [[2604.18563]] | Dual Alignment: LM Layers & Human Processing | LM层级与人类处理双重对齐：自然阅读-浅层，句法歧义-深层 / Dual alignment: natural reading with early layers, ambiguity resolution with later layers |
| [[2604.18567]] | LPSR: Latent Phase-Shift Rollback | 残差流相位反转检测+KV-Cache回退纠错，8B模型超越70B标准解码 / Residual stream phase-shift detection + KV-cache rollback correction; 8B surpasses 70B standard decoding |
