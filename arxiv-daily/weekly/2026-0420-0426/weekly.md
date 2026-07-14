---
title: "Weekly arXiv Digest — 2026-04-21–2026-04-24"
week: 2026-0420-0426
date_range: ["2026-04-21", "2026-04-24"]
tags: [可解释性与机制分析, 推理效率与压缩, 训练与优化, 安全、对齐与评估]
papers: 29
---

> 本周共收录 **29** 篇精选论文，来自 2 个工作日的每日精选。 / **29** curated papers this week, rolled up from 2 daily digests.

## 本周必读 / Must Read This Week

> 如果你只读几篇 — 看这些。优先挑选了跨天复现或被每日必读的论文。 / If you read nothing else, read these. Prioritizes papers recurring across days or picked as daily must-reads.

### [[2604.16809]] Delayed Loss Spikes in BN Linear Models

- **推荐理由：** 证明BN通过逐步放大有效学习率引发延迟方向性不稳定并在有限步内自稳定 
- **Why read:** Proves BN induces delayed directional instability via rising effective LR with finite-time self-stabilization 
- _Topic: A. 训练稳定性与优化理论_

### [[2604.17849]] Reliability of Computer Use Agents

- **推荐理由：** Pass^k指标和三因素不可靠性分解，指令澄清是最有效干预手段 
- **Why read:** Pass^k metrics and three-factor decomposition; instruction clarification most effective intervention 
- _Topic: E. 可靠性评估与基准_

### [[2604.18493]] Too Correct to Learn

- **推荐理由：** GRPO在饱和数据上优势信号消失，Mixed-CUTS在AIME25提升15.1% 
- **Why read:** GRPO advantage vanishes on saturated data; Mixed-CUTS boosts AIME25 by 15.1% 
- _Topic: A. 训练稳定性与优化理论_

### [[2604.17224]] LASER: Low-Rank Activation SVD

- **推荐理由：** 递归模型激活占据低维子空间，LASER动态压缩框架实现约60%内存节省 
- **Why read:** Recursive model activations lie in low-dim subspace; LASER achieves ~60% memory savings 
- _Topic: C. 推理效率与模型压缩_

### [[2604.17694]] Random Seed Stability via Bagging

- **推荐理由：** 形式化随机种子稳定性，subbagging保证有界算法稳定性，消除debiased ML种子依赖 
- **Why read:** Formalizes random seed stability; subbagging guarantees stability; eliminates seed dependence in debiased ML 
- _Topic: F. 可解释性与探测方法_

### [[2604.17753]] ENMP: Evolutionary Negative Module Pruning

- **推荐理由：** 发现LoRA合并中的"负模块"现象，ENMP进化搜索剪除有害模块达到新SOTA 
- **Why read:** Discovers negative modules in LoRA merging; ENMP prunes detrimental modules to new SOTA 
- _Topic: G. 模型合并与对齐_

### [[2604.17761]] Contrastive Attribution in the Wild

- **推荐理由：** LRP对比归因用于LLM失败分析，token级归因有信息但在部分案例中解释力有限 
- **Why read:** LRP contrastive attribution for LLM failure analysis; informative in some cases but not universally applicable 
- _Topic: B. 机制可解释性与隐藏状态分析_

### [[2604.17837]] Polysemantic Experts, Monosemantic Paths

- **推荐理由：** MoE残差流分解为控制信号和内容通道，专家轨迹是可解释性基本单元 
- **Why read:** MoE residual stream decomposed into control/content channels; trajectories are interpretability unit 
- _Topic: B. 机制可解释性与隐藏状态分析_

## 本周主题脉络 / Themes This Week

### Interpretability & Mechanistic Analysis / 可解释性与机制分析

本周该方向共 **10** 篇论文。 / **10** papers this week on this line.

代表论文 / Highlights: [[2604.17761]] · [[2604.17837]] · [[2604.18158]] · [[2604.18307]] · [[2604.18519]] · [[2604.18563]]

### Inference Efficiency & Compression / 推理效率与压缩

本周该方向共 **9** 篇论文。 / **9** papers this week on this line.

代表论文 / Highlights: [[2604.18085]] · [[2604.18117]] · [[2604.18128]] · [[2604.18555]] · [[2604.18556]] · [[2604.17224]]

### Training & Optimization / 训练与优化

本周该方向共 **5** 篇论文。 / **5** papers this week on this line.

代表论文 / Highlights: [[2604.16809]] · [[2604.18235]] · [[2604.18239]] · [[2604.18450]] · [[2604.18493]]

### Safety, Alignment & Evaluation / 安全、对齐与评估

本周该方向共 **5** 篇论文。 / **5** papers this week on this line.

代表论文 / Highlights: [[2604.17849]] · [[2604.18164]] · [[2604.18245]] · [[2604.18389]] · [[2604.17753]]

## 全部论文 / All Papers

### 2026-04-21 (29)

- [[2604.16809]] Delayed Loss Spikes in BN Linear Models — 证明BN通过逐步放大有效学习率引发延迟方向性不稳定并在有限步内自稳定 / Proves BN induces delayed directional instability via rising effective LR with finite-time self-stabilization ⭐
- [[2604.17224]] LASER: Low-Rank Activation SVD — 递归模型激活占据低维子空间，LASER动态压缩框架实现约60%内存节省 / Recursive model activations lie in low-dim subspace; LASER achieves ~60% memory savings
- [[2604.17694]] Random Seed Stability via Bagging — 形式化随机种子稳定性，subbagging保证有界算法稳定性，消除debiased ML种子依赖 / Formalizes random seed stability; subbagging guarantees stability; eliminates seed dependence in debiased ML
- [[2604.17753]] ENMP: Evolutionary Negative Module Pruning — 发现LoRA合并中的"负模块"现象，ENMP进化搜索剪除有害模块达到新SOTA / Discovers negative modules in LoRA merging; ENMP prunes detrimental modules to new SOTA
- [[2604.17761]] Contrastive Attribution in the Wild — LRP对比归因用于LLM失败分析，token级归因有信息但在部分案例中解释力有限 / LRP contrastive attribution for LLM failure analysis; informative in some cases but not universally applicable
- [[2604.17837]] Polysemantic Experts, Monosemantic Paths — MoE残差流分解为控制信号和内容通道，专家轨迹是可解释性基本单元 / MoE residual stream decomposed into control/content channels; trajectories are interpretability unit
- [[2604.17849]] Reliability of Computer Use Agents — Pass^k指标和三因素不可靠性分解，指令澄清是最有效干预手段 / Pass^k metrics and three-factor decomposition; instruction clarification most effective intervention ⭐
- [[2604.18085]] Predicting LLM Compression Degradation — gamma*rho_s交互项Pearson R=0.890预测压缩退化，支持"先预测再压缩"工作流 / gamma*rho_s interaction term (R=0.890) predicts compression degradation; enables predict-then-compress workflow
- [[2604.18092]] Generalization Boundaries of Fine-Tuned SLMs — 微调3-4B模型在图推理上保持强序数一致性，不同架构有独特退化模式 / Fine-tuned 3-4B models maintain ordinal consistency on graph reasoning; architecture-specific degradation
- [[2604.18103]] DASH: Delta Attention Selective Halting — 免训练token选择性停止，监控注意力更新实现1.74-1.89x推理加速 / Training-free token halting via attention update monitoring; 1.74-1.89x inference speedup
- [[2604.18109]] FLiP: Multimodal Sentence Embeddings — 因子化线性投影恢复75%+嵌入词汇内容，揭示编码器模态和语言偏差 / Factorized projection recovers 75%+ lexical content; reveals modality and language biases in encoders
- [[2604.18117]] LoRaQ: 4-bit Quantization — 首个全低于16位量化流程，低秩补偿分支本身可量化，超越SOTA / First fully sub-16-bit pipeline; compensation branch itself quantized; outperforms SOTA
- [[2604.18128]] Depth Registers for W4A4 on SwiGLU — SwiGLU读取器/生成器分解，Depth Registers将W4A4 PPL从1727降至39.9 / SwiGLU reader/generator decomposition; Depth Registers reduce W4A4 PPL from 1727 to 39.9
- [[2604.18158]] State Transfer Reveals Reuse — K/V向量零重训练迁移证明固定接口编译式迁移机制 / K/V zero-retrain transfer proves fixed-interface compiled transfer mechanism in attention heads
- [[2604.18164]] MM-JudgeBias — 3维度9种组合偏差基准评估26个MLLM评判者，图像相关偏差最严重 / 3-dim 9-type compositional bias benchmark; 26 MLLMs evaluated; image biases most severe
- [[2604.18235]] CalibAdv: Calibrating Advantage in GRPO — 校准GRPO优势信号解决训练崩溃，平均F1相对提升11.80% / Calibrates GRPO advantage to prevent collapse; 11.80% avg relative F1 improvement
- [[2604.18239]] Disentangled Preference Optimization — 统一激励-分数分解揭示偏好优化共享更新方向，提出解耦带条件 / Unified incentive-score decomposition reveals shared update directions; proposes disentanglement band
- [[2604.18245]] Correction and Corruption in LLM Protocols — 校正率-腐化率双指标框架揭示高基线下腐化放大现象 / Correction-corruption framework reveals corruption amplification at high baselines
- [[2604.18249]] Where Do S3Ms Become Unfair? — 语音模型逐层公平性分析，ASR偏置与性能成反比且预训练即固化 / Layerwise fairness analysis; ASR bias inversely correlates with performance; baked in during pretraining
- [[2604.18307]] Reasoning Models Know What's Important — 推理模型在激活中编码步骤重要性，探针80%+准确率且跨模型迁移 / Reasoning models encode step importance in activations; probes 80%+ accuracy with cross-model transfer
- [[2604.18389]] Understanding Prompt Sensitivity — 推导提示敏感性理论上界，发现模板影响大于问题，LLM隐藏状态分散 / Derives upper bounds for prompt sensitivity; templates dominate; LLM hidden states disperse
- [[2604.18396]] River-LLM — KV-Shared Exit River解决早退KV Cache缺失，1.71-2.16x实际加速 / KV-Shared Exit River solves KV cache absence; 1.71-2.16x practical speedup
- [[2604.18450]] RMT of Early-Stopped Gradient Flow — 随机矩阵理论解析早停的瞬态BBP相变，三种学习相的完整谱刻画 / RMT analytically solves transient BBP transition for early stopping; complete spectral characterization of three learning phases
- [[2604.18493]] Too Correct to Learn — GRPO在饱和数据上优势信号消失，Mixed-CUTS在AIME25提升15.1% / GRPO advantage vanishes on saturated data; Mixed-CUTS boosts AIME25 by 15.1% ⭐
- [[2604.18519]] SIREN: Safety From Within — L1探针识别多层安全神经元，超越LlamaGuard3和Qwen3Guard / L1 probes identify multi-layer safety neurons; outperforms LlamaGuard3 and Qwen3Guard
- [[2604.18555]] TurboQuant vs DRIVE/EDEN — 证明TurboQuant是EDEN的次优特例，EDEN在所有场景中均优 / Proves TurboQuant is suboptimal special case of EDEN; EDEN wins in all settings
- [[2604.18556]] GSQ: Gumbel-Softmax Quantization — Gumbel-Softmax可微标量量化，2-bit接近VQ精度，扩展至万亿参数MoE / Differentiable scalar quantization; 2-bit approaches VQ accuracy; scales to trillion-param MoE
- [[2604.18563]] Dual Alignment: LM Layers & Human Processing — LM层级与人类处理双重对齐：自然阅读-浅层，句法歧义-深层 / Dual alignment: natural reading with early layers, ambiguity resolution with later layers
- [[2604.18567]] LPSR: Latent Phase-Shift Rollback — 残差流相位反转检测+KV-Cache回退纠错，8B模型超越70B标准解码 / Residual stream phase-shift detection + KV-cache rollback correction; 8B surpasses 70B standard decoding


---

_本周报由每日 digest 汇总而成。/ This weekly digest is a rollup of the daily digests._

**每日入口 / Daily entries:** [2026-04-21](../../2026-04-21/overview.md) · [2026-04-24](../../2026-04-24/overview.md)
