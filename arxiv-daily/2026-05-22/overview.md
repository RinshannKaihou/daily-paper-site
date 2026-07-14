---
title: "Daily Paper Overview - 2026-05-22"
date: 2026-05-22
tags:
  - mechanistic-interpretability
  - optimization
  - reinforcement-learning
  - representation-learning
  - differential-privacy
  - LLM-reasoning
  - post-training
  - adversarial-robustness
  - model-compression
  - embedding-models
papers: 50
---

## 今日必读 / Must Read Today

### 1. [[2605.22488]] Represented Is Not Computed

**为什么必读：** 本文通过精心设计的底数提取任务，发现线性探针能高精度解码 Transformer 的中间计算步骤（R^2=0.96），但因果干预证明模型根本不使用这些中间量——直接证明"可解码不等于被使用"，对整个 mechanistic interpretability 领域的方法论提出了严格警告。

**Why must-read:** A meticulously controlled experiment demonstrating that linear probes decode algorithmic intermediates with R^2=0.96 that causal interventions prove the model never uses -- a clean, quantitative demonstration that "decodable ≠ computed" with direct methodological implications for the entire mechanistic interpretability field.

### 2. [[2605.21692]] Representation Gap

**为什么必读：** 提出商流形内在维度作为理解神经网络泛化能力的统一几何原理，证明等变架构通过维度降低获得可证明的泛化改进，将最优量化理论与表示学习优雅统一。

**Why must-read:** Proposes the intrinsic dimension of the quotient manifold as a unifying geometric principle for generalization, proves equivariant architectures gain provably better generalization through dimension reduction, and elegantly unifies optimal quantization theory with representation learning.

### 3. [[2605.21803]] Optimizer-Induced Spectral Scaling Laws

**为什么必读：** 揭示优化器选择（AdamW vs. Muon）在同一 Transformer 架构上产生截然不同的 FFN 频谱缩放规律，发现"匹配的困惑度不意味着匹配的表示结构"，挑战了仅用 loss 评估模型的传统做法。

**Why must-read:** Reveals that optimizer choice fundamentally changes FFN spectral scaling exponents on the same Transformer architecture, and that matched perplexity does NOT imply matched representation geometry -- challenging the practice of evaluating models by loss alone.

---

## 按主题分类 / Papers by Topic

### 机制可解释性 / Mechanistic Interpretability

| ArXiv ID | 短标题 / Short Title | 核心贡献 / Core Contribution |
|----------|---------------------|------------------------------|
| [[2605.22488]] | Represented Is Not Computed | 探针可解码中间量但因果干预证明模型不使用 / Probes decode intermediates but causal interventions show the model doesn't use them |
| [[2605.22462]] | Five-Stage Feature Analysis | SAE特征的检测鲁棒性与因果鲁棒性存在关键差距 / Detection robustness of SAE features does not imply causal robustness |
| [[2605.22719]] | Sparse-Feature Audit of IOI | SAE增加可解释性但不增加预测力 / SAE adds interpretability but not predictive power over raw representations |
| [[2605.22679]] | CEDAR | 正交旋转解耦VLM嵌入无需维度扩展 / Orthogonal rotation disentangles VLM embeddings without dimension expansion |
| [[2605.22170]] | Factual Recall Text to Speech | 文本事实回忆机制仅部分迁移到语音模态 / Text factual recall mechanisms only partially transfer to speech |
| [[2605.21980]] | Emotional Circuits in LVLMs | 发现"适应-聚合-执行"三阶段情感处理机制 / Discovers "Adapt-Aggregate-Execute" three-stage emotion processing |
| [[2605.22532]] | Relational Linear Properties | KL散度探针揭示表层句法特征在浅层线性编码 / KL-divergence probes reveal surface syntactic features are linearly encoded in early layers |
| [[2605.22377]] | Token Level Activation SLMs | L2范式量化BERT第8层语义整合 / L2 norm quantifies semantic consolidation at BERT Layer 8 |
| [[2605.22658]] | SegCompass | SAE首次引入推理分割实现可解释对齐 / First SAE integration into reasoning segmentation for interpretable alignment |

### 优化与训练动力学 / Optimization & Training Dynamics

| ArXiv ID | 短标题 / Short Title | 核心贡献 / Core Contribution |
|----------|---------------------|------------------------------|
| [[2605.21803]] | Optimizer-Induced Spectral Scaling | 优化器是表示缩放的一等公民 / Optimizer is a first-class citizen in representation scaling |
| [[2605.22644]] | Why SGD is Not Brownian Motion | SGD噪声不是布朗运动，有限学习率下存在定性差异 / SGD noise is not Brownian motion; qualitative differences at finite learning rates |
| [[2605.21933]] | Thermodynamic Irreversibility | 四种不可逆性度量等价于同一标量势 / Four irreversibility measures are equivalent to the same scalar potential |
| [[2605.22297]] | LLR Layerwise Learning Rate | 基于HT-SR理论为不同层分配差异化学习率 / HT-SR-theory-guided layerwise learning rate assignment |
| [[2605.21968]] | IAdaPID-ADG Optimizer | AMSGrad收敛性修复+DiffGrad稳定性修复 / AMSGrad convergence fix + DiffGrad stability fix for PID optimizer |
| [[2605.21860]] | Empirical Sensitivity Estimators | 提出比传统鲁棒性更强的新度量 / Introduces a stronger robustness measure than classical robustness |
| [[2605.22010]] | Uniform-in-Time PoC | 确定性梯度下降的时间均匀传播混沌 / Uniform-in-time propagation of chaos for deterministic gradient descent |

### 后训练与强化学习 / Post-Training & RL

| ArXiv ID | 短标题 / Short Title | 核心贡献 / Core Contribution |
|----------|---------------------|------------------------------|
| [[2605.22703]] | Clipping Bottleneck NSR | GRPO裁剪决策导致信号丢失，随机救援机制修复 / GRPO clipping decisions lose signals; stochastic rescue mechanism fixes it |
| [[2605.22156]] | OWPO Self-Evolving LLMs | 非对称信任区域解决力反转问题 / Asymmetric trust region solves the force reversal problem |
| [[2605.22217]] | Data Gating Self-Play RL | 数据门控比奖励设计更决定训练稳定性 / Data gating matters more than reward design for training stability |
| [[2605.22620]] | Multi-Reward RLIF | 双奖励互补+KL-Cov正则化解决熵崩塌 / Dual complementary rewards + KL-Cov regularization solve entropy collapse |
| [[2605.22731]] | State Distribution View | 后训练本质在于状态分布来源而非损失函数 / Post-training is about state distribution source, not loss function |
| [[2605.21801]] | GCPO Uncertainty Policy Opt | 几何感知和奖励校准的不确定性信号提升GRPO / Geometry-aware and reward-calibrated uncertainty improves GRPO |

### LLM评估与安全 / LLM Evaluation & Safety

| ArXiv ID | 短标题 / Short Title | 核心贡献 / Core Contribution |
|----------|---------------------|------------------------------|
| [[2605.21856]] | Zero-CoT Probe | 截断CoT暴露隐蔽数据污染 / Truncating CoT reveals evasive data contamination |
| [[2605.21706]] | Latent-Space Attacks | 拒绝抑制等价于最弱潜在空间规避攻击 / Refusal suppression equals the weakest latent-space evasion attack |
| [[2605.22007]] | Commitment Failure | 幻觉源于概率分散而非知识缺失，随规模恶化 / Hallucination stems from probability fragmentation, worsens with scale |
| [[2605.22005]] | LLM Secret Dictionary | lm_head的SVD揭示训练数据构成和安全隐患 / SVD of lm_head reveals training data composition and safety risks |
| [[2605.22785]] | AI Chatbots News Evaluation | 六大商业AI聊天机器人的新闻准确性评估 / Evaluation of six commercial AI chatbots on news accuracy |

### Transformer架构与注意力 / Transformer Architecture & Attention

| ArXiv ID | 短标题 / Short Title | 核心贡献 / Core Contribution |
|----------|---------------------|------------------------------|
| [[2605.21770]] | Manifold-Guided Attention | 正确性流形引导的条件干预 / Correctness-manifold-guided conditional intervention |
| [[2605.21842]] | Energy-Gated Attention | 谱能量门控注意力聚合 / Spectral energy gating for attention aggregation |
| [[2605.22106]] | ArborKV | 树结构推理的KV缓存管理 / Tree-structure-aware KV cache management |
| [[2605.21724]] | TBP-mHC Hyper-Connections | 运输多面体实现精确双随机矩阵 / Transportation polytope achieves exact doubly-stochastic matrices |

### 表示学习与泛化理论 / Representation Learning & Generalization Theory

| ArXiv ID | 短标题 / Short Title | 核心贡献 / Core Contribution |
|----------|---------------------|------------------------------|
| [[2605.21692]] | Representation Gap | 商流形内在维度决定泛化缩放律 / Quotient manifold intrinsic dimension governs generalization scaling |
| [[2605.22800]] | The Matching Principle | 统一鲁棒性方法为同一统计框架 / Unifies robustness methods under a single statistical framework |
| [[2605.22691]] | Posterior Collapse as Pruning | 后验坍缩是自动谱剪枝而非训练失败 / Posterior collapse is automatic spectral pruning, not training failure |
| [[2605.22202]] | Embedding Structure Retention | k近邻重叠度预测嵌入模型性能 / k-NN overlap predicts embedding model performance |

### 差分隐私与鲁棒性 / Differential Privacy & Robustness

| ArXiv ID | 短标题 / Short Title | 核心贡献 / Core Contribution |
|----------|---------------------|------------------------------|
| [[2605.21780]] | Primal-Dual DP Robustness | f-DP与隐私轮廓的等价关系用于后门认证 / Equivalence of f-DP and privacy profiles for backdoor certification |
| [[2605.21938]] | RDP Auditing | 首个直接审计Renyi差分隐私的方法 / First method to directly audit Renyi Differential Privacy |
| [[2605.21860]] | Empirical Sensitivity | 新的鲁棒性度量，比传统鲁棒性更强 / New robustness measure stronger than classical robustness |

### 系统与硬件 / Systems & Hardware

| ArXiv ID | 短标题 / Short Title | 核心贡献 / Core Contribution |
|----------|---------------------|------------------------------|
| [[2605.21847]] | CompPow GPU Power | GPU内部组件级功耗管理 / Component-level GPU power management |
| [[2605.21912]] | Emerging Memory Technologies | 室温到低温存储技术综述 / Survey of memory technologies from room to cryogenic temperature |
| [[2605.22437]] | NCS2 EMFI Faults | 电磁故障注入下边缘AI加速器故障模式 / EMFI fault modes on edge AI accelerators |

### 模型压缩与高效推理 / Model Compression & Efficient Inference

| ArXiv ID | 短标题 / Short Title | 核心贡献 / Core Contribution |
|----------|---------------------|------------------------------|
| [[2605.22351]] | QuantSR+ | 2-bit量化超分辨率匹配全精度 / 2-bit quantized SR matches full precision |
| [[2605.22237]] | QUAD4FHE | 决策感知的ReLU替换用于同态加密推理 / Decision-aware ReLU replacement for FHE inference |
| [[2605.21972]] | Sparsity Allocation Recoverability | 稀疏分配策略决定剪枝后可修复性 / Sparsity allocation determines post-pruning recoverability |

### 分布偏移与域适应 / Distribution Shift & Domain Adaptation

| ArXiv ID | 短标题 / Short Title | 核心贡献 / Core Contribution |
|----------|---------------------|------------------------------|
| [[2605.21849]] | GAE Geometry-Adaptive Explainer | 闭式旋转修复SAE在OOD下的忠实性 / Closed-form rotation fixes SAE faithfulness under OOD |
| [[2605.21783]] | MMD Credal TTA | MMD球作为credal sets的理论框架 / MMD-balls as credal sets for TTA uncertainty |
| [[2605.22164]] | Trajectory Reachability Metrics | 替代欧氏距离提升潜空间规划 / Replaces Euclidean distance to improve latent-space planning |

### 跨模态与VLM / Cross-Modal & VLM

| ArXiv ID | 短标题 / Short Title | 核心贡献 / Core Contribution |
|----------|---------------------|------------------------------|
| [[2605.22168]] | Cross-Modal Synergy Benchmark | 揭示VLM可解释性评估崩塌问题 / Reveals evaluation collapse in VLM explainability |
| [[2605.22401]] | Cross-Species RSA | 局部学习规则在早期视觉皮层跨物种优于BP / Local learning rules outperform BP in early visual cortex across species |

### 硬件安全 / Hardware Security

| ArXiv ID | 短标题 / Short Title | 核心贡献 / Core Contribution |
|----------|---------------------|------------------------------|
| [[2605.22441]] | Constant-Time Activations MCU | 恒定时间激活函数消除计时侧信道 / Constant-time activation functions eliminate timing side channels |

### 模型审计与可解释性 / Model Auditing & Explainability

| ArXiv ID | 短标题 / Short Title | 核心贡献 / Core Contribution |
|----------|---------------------|------------------------------|
| [[2605.21731]] | I-SAFE Wasserstein Auditing | 基于最优传输的科学AI模型审计 / OT-based auditing for scientific AI models |

---

## All Papers

| # | ArXiv ID | Short Title | Topics | 一句话总结 (Chinese) | One-Sentence Summary (English) |
|---|----------|-------------|--------|----------------------|-------------------------------|
| 1 | [[2605.21692]] | Representation Gap | generalization-theory, intrinsic-dimension | 表示间隙的渐近缩放律由商流形内在维度唯一决定 | Asymptotic scaling of representation gap is governed solely by quotient manifold intrinsic dimension |
| 2 | [[2605.21706]] | Latent-Space Attacks | ai-safety, adversarial-attacks | 拒绝抑制等价于最弱潜在空间规避攻击 | Refusal suppression equals minimum-confidence latent-space evasion attack |
| 3 | [[2605.21724]] | TBP-mHC | hyper-connections, doubly-stochastic | 运输多面体实现精确双随机矩阵参数化 | Transportation polytope achieves exact doubly-stochastic matrix parameterization |
| 4 | [[2605.21731]] | I-SAFE Wasserstein Auditing | model-auditing, wasserstein-distance | 基于Wasserstein距离的科学AI模型分布审计 | Wasserstein-based distributional auditing for scientific AI models |
| 5 | [[2605.21770]] | Manifold-Guided Attention | activation-steering, LLM-reasoning | 正确性流形引导的轨迹感知推理时干预 | Correctness-manifold-guided trajectory-aware inference-time intervention |
| 6 | [[2605.21780]] | Primal-Dual DP Robustness | differential-privacy, backdoor-robustness | f-DP与隐私轮廓的原始-对偶等价用于后门认证 | Primal-dual equivalence of f-DP and privacy profiles for backdoor certification |
| 7 | [[2605.21783]] | MMD Credal TTA | test-time-adaptation, uncertainty-quantification | MMD球作为credal sets的PAC-Bayesian TTA框架 | MMD-balls as credal sets in PAC-Bayesian TTA framework |
| 8 | [[2605.21801]] | GCPO Uncertainty Policy Opt | post-training, uncertainty-quantification | 几何感知不确定性信号提升GRPO后训练 | Geometry-aware uncertainty signals improve GRPO post-training |
| 9 | [[2605.21803]] | Optimizer-Induced Spectral Scaling | scaling-laws, optimizer-design | 优化器选择根本改变FFN频谱缩放规律 | Optimizer choice fundamentally changes FFN spectral scaling laws |
| 10 | [[2605.21842]] | Energy-Gated Attention | transformer-attention, spectral-methods | 谱能量门控注意力聚合 | Spectral energy gating for attention value aggregation |
| 11 | [[2605.21847]] | CompPow GPU Power | GPU-architecture, power-management | GPU内部组件级感知功耗管理 / Component-aware GPU power management | Component-aware intra-GPU power management on MI300X |
| 12 | [[2605.21849]] | GAE Geometry-Adaptive Explainer | mechanistic-interpretability, distribution-shift | 闭式旋转修复SAE在OOD下的忠实性 / Closed-form rotation fixes SAE OOD faithfulness | Closed-form Procrustes rotation restores SAE faithfulness under distribution shift |
| 13 | [[2605.21856]] | Zero-CoT Probe | data-contamination, llm-evaluation | 截断CoT暴露隐蔽数据污染 / Truncating CoT reveals evasive data contamination | Zero-CoT truncation reveals evasive data contamination in LLMs |
| 14 | [[2605.21860]] | Empirical Sensitivity Estimators | robust-statistics, differential-privacy | 提出经验敏感性作为新的鲁棒性度量 / Introduces empirical sensitivity as a new robustness measure | Introduces empirical sensitivity as a stronger robustness measure with tight bounds |
| 15 | [[2605.21912]] | Emerging Memory Technologies | memory-technology, cryogenic-computing | 室温到低温存储技术综述 / Survey of room-to-cryogenic memory technologies | Comprehensive survey of volatile and non-volatile memory technologies at room and cryogenic temperatures |
| 16 | [[2605.21933]] | Thermodynamic Irreversibility | statistical-mechanics, training-dynamics | 四种不可逆性度量等价于同一标量势 / Four irreversibility measures reduce to the same scalar potential | Four irreversibility measures from distinct fields are equivalent to leading order |
| 17 | [[2605.21938]] | RDP Auditing | differential-privacy, auditing | 首个直接审计Renyi差分隐私的黑盒框架 / First black-box RDP auditing framework | First black-box framework for auditing Renyi Differential Privacy with minimax-optimal guarantees |
| 18 | [[2605.21968]] | IAdaPID-ADG Optimizer | optimization, adaptive-learning-rate | AMSGrad收敛+DiffGrad稳定性修复PID优化器 / AMSGrad + DiffGrad fixes for PID optimizer | Combines AMSGrad convergence and DiffGrad stability into adaptive PID optimizer |
| 19 | [[2605.21972]] | Sparsity Allocation Recoverability | neural-network-pruning, model-compression | 稀疏分配策略决定剪枝后无标签修复效果 / Sparsity allocation determines label-free post-pruning recoverability | ERK vs. LAMP allocation shapes post-pruning recoverability across architectures |
| 20 | [[2605.21980]] | Emotional Circuits in LVLMs | mechanistic-interpretability, vision-language-models | 发现三阶段情感处理机制并设计VEEENA干预 / Discovers three-stage emotion mechanism and designs VEEENA intervention | Discovers "Adapt-Aggregate-Execute" emotion mechanism; VEEENA improves VLM emotion understanding +6.7% |
| 21 | [[2605.22005]] | LLM Secret Dictionary | LLM-interpretability, safety-auditing | lm_head的SVD揭示训练数据和安全隐患 / SVD of lm_head reveals training data and safety issues | SVD of lm_head reveals interpretable semantic subspaces and surviving safety risks |
| 22 | [[2605.22007]] | Commitment Failure | LLM-hallucination, instruction-tuning | 幻觉源于概率分散随规模恶化 / Hallucination from probability fragmentation worsens with scale | 16-47% of hallucinations are commitment failures where the model knows the answer but can't commit |
| 23 | [[2605.22010]] | Uniform-in-Time PoC | mean-field-theory, propagation-of-chaos | 确定性梯度下降的时间均匀传播混沌 / Uniform-in-time propagation of chaos for deterministic gradient flow | First uniform-in-time propagation of chaos for deterministic gradient flow on shallow networks |
| 24 | [[2605.22106]] | ArborKV | kv-cache, llm-reasoning | 树结构推理的KV缓存结构感知管理 / Structure-aware KV cache management for tree-based reasoning | Structure-aware KV cache management achieves ~4x memory reduction for tree-of-thought reasoning |
| 25 | [[2605.22156]] | OWPO Self-Evolving LLMs | RLVR, policy-optimization | 非对称信任区域解决力反转实现自进化 / Asymmetric trust region solves force reversal for self-evolution | One-way policy optimization with ratchet effect enables continuous LLM self-evolution |
| 26 | [[2605.22164]] | Trajectory Reachability Metrics | latent-world-models, model-based-RL | 轨迹可达性度量替代欧氏距离提升规划 / Trajectory reachability metrics replace Euclidean distance for latent planning | Replaces Euclidean latent distance with horizon-matched pairwise ranking, boosting success 7% to 97% |
| 27 | [[2605.22168]] | Cross-Modal Synergy Benchmark | VLM, explainability | 揭示VLM可解释性评估崩塌并提出Synergistic Faithfulness / Reveals VLM explainability evaluation collapse | Reveals evaluation collapse in VLM explainability; proposes Shapley-based synergistic faithfulness metric |
| 28 | [[2605.22170]] | Factual Recall Text to Speech | mechanistic-interpretability, speech-language-models | 文本事实回忆仅部分迁移到语音模态 / Text factual recall only partially transfers to speech | Text-based factual recall mechanisms only partially transfer to speech modality in SpiritLM |
| 29 | [[2605.22202]] | Embedding Structure Retention | embedding-models, representation-analysis | k近邻重叠度和ICA峰值显著性预测嵌入模型性能 / k-NN overlap and ICA peak prominence predict embedding performance | k-NN overlap and ICA peak prominence strongly predict embedding model benchmark performance |
| 30 | [[2605.22217]] | Data Gating Self-Play RL | self-play-RL, training-collapse | 数据门控比奖励设计更决定自博弈RL稳定性 / Data gating matters more than reward design for self-play RL stability | Data-level quality gating is the binding constraint on self-play RL stability, not reward design |
| 31 | [[2605.22237]] | QUAD4FHE | FHE, privacy-preserving-inference | 决策感知的二次ReLU替换用于同态加密推理 / Decision-aware quadratic ReLU replacement for FHE inference | Decision-aware quadratic replacement preserves classification decisions under CKKS FHE inference |
| 32 | [[2605.22297]] | LLR Layerwise Learning Rate | llm-training, learning-rate-scheduling | 基于HT-SR理论的逐层差异化学习率 / HT-SR-theory-guided layerwise learning rate for LLM training | HT-SR-theory-guided layerwise learning rates achieve up to 1.5x training speedup |
| 33 | [[2605.22351]] | QuantSR+ | low-bit-quantization, image-super-resolution | 2-bit量化超分辨率匹配全精度性能 / 2-bit quantized SR matches full-precision performance | Unified low-bit quantization framework achieving 4-bit SR matching full precision |
| 34 | [[2605.22377]] | Token Level Activation SLMs | explainability, BERT | L2范式量化BERT Layer 8语义整合 / L2 norm quantifies semantic consolidation at BERT Layer 8 | L2 norms of BERT Layer 8 hidden states quantify token-level representational importance |
| 35 | [[2605.22401]] | Cross-Species RSA | representational-similarity-analysis, cross-species-comparison | 局部学习规则在早期视觉皮层跨物种优于BP / Local learning rules outperform BP in early visual cortex across species | Local learning rules (STDP, PC) consistently outperform BP in early visual cortex across species |
| 36 | [[2605.22437]] | NCS2 EMFI Faults | hardware-security, fault-injection | 电磁故障注入下边缘AI加速器的四类故障模式 / Four fault classes from EMFI on edge AI accelerator | Systematic EMFI characterization of Intel NCS2 reveals four reproducible fault classes |
| 37 | [[2605.22441]] | Constant-Time Activations MCU | side-channel-attacks, embedded-ml | 恒定时间激活函数消除MCU计时侧信道 / Constant-time activation functions eliminate MCU timing side channels | Constant-time Padé approximation eliminates timing side channels for activations on Cortex-M4 |
| 38 | [[2605.22462]] | Five-Stage Feature Analysis | mechanistic-interpretability, causal-analysis | SAE特征检测鲁棒性不等于因果鲁棒性 / SAE detection robustness does not equal causal robustness | Five-stage pipeline reveals detection robustness of SAE features does not imply causal robustness |
| 39 | [[2605.22488]] | Represented Is Not Computed | mechanistic-interpretability, causal-intervention | 探针可解码中间量但模型不使用它们 / Probes decode intermediates but model doesn't use them | Linear probes decode algorithmic intermediates that causal interventions prove the model never uses |
| 40 | [[2605.22532]] | Relational Linear Properties | mechanistic-interpretability, linear-representations | KL散度探针揭示层级线性编码动态 / KL-divergence probes reveal layer-wise linear encoding dynamics | KL-based probes reveal surface features are linearly encoded in early layers, abstract features in middle |
| 41 | [[2605.22620]] | Multi-Reward RLIF | reinforcement-learning, LLM-reasoning | 双奖励互补+KL-Cov解决无监督RL熵崩塌 / Dual rewards + KL-Cov solve unsupervised RL entropy collapse | Multi-reward RLIF with KL-Cov regularization approaches supervised RLVR performance |
| 42 | [[2605.22644]] | Why SGD is Not Brownian Motion | optimization, stochastic-gradient-descent | SGD噪声在有限学习率下与Langevin近似有定性差异 / SGD noise qualitatively differs from Langevin at finite learning rates | Discrete Fokker-Planck analysis reveals SGD dynamics differ qualitatively from Langevin approximation |
| 43 | [[2605.22658]] | SegCompass | reasoning-segmentation, sparse-autoencoder | SAE首次引入推理分割实现可解释对齐 / First SAE integration for interpretable reasoning segmentation | First SAE-based interpretable alignment between CoT reasoning and visual segmentation |
| 44 | [[2605.22679]] | CEDAR | vision-language-models, sparse-representation | 正交旋转解耦VLM嵌入无需维度扩展 / Orthogonal rotation disentangles VLM embeddings without expansion | Orthogonal rotation with top-k sparsity disentangles VLM embeddings in original dimension |
| 45 | [[2605.22691]] | Posterior Collapse as Pruning | VAE, representation-learning | 后验坍缩是自动谱剪枝而非训练失败 / Posterior collapse is automatic spectral pruning, not failure | Reframes beta-VAE posterior collapse as principled spectral pruning via Landau stability analysis |
| 46 | [[2605.22703]] | Clipping Bottleneck NSR | reinforcement-learning, RLVR | 随机救援机制修复GRPO裁剪信号丢失 / Stochastic rescue fixes GRPO clipping signal loss | Near-boundary stochastic rescue converts rigid clipping into probabilistic admission |
| 47 | [[2605.22719]] | Sparse-Feature Audit IOI | mechanistic-interpretability, sparse-autoencoder | SAE增加可解释性但不增加预测力 / SAE adds interpretability but not predictive power | Three-control audit shows SAE features add interpretability but not predictive power over raw activations |
| 48 | [[2605.22731]] | State Distribution View | post-training, state-distribution | 后训练本质在于状态分布来源而非损失函数 / Post-training is about state distribution, not loss function | Unifies SFT/RL/KD through state distribution source; on-policy methods preserve capabilities better |
| 49 | [[2605.22785]] | AI Chatbots News Evaluation | ai-evaluation, news-retrieval | 六大商业AI新闻准确性评估揭示区域不平等 / Six commercial AI chatbots show regional inequality in news accuracy | 14-day evaluation of 6 AI chatbots reveals 95.6% top accuracy but 19% adversarial accuracy and Hindi gap |
| 50 | [[2605.22800]] | The Matching Principle | representation-learning, robustness-theory | 统一多种鲁棒性方法为匹配原则框架 / Unifies diverse robustness methods under the matching principle | Unifies robustness techniques as estimators of nuisance covariance with matched regularizer range |
