---
title: "Daily Paper Overview — 2026-06-12"
date: 2026-06-12
tags:
  - daily-overview
  - arxiv
papers: 46
---

## 今日必读 / Must Read Today

### 1. [[2606.13473]] MaxProof: Scaling Mathematical Proof with Generative-Verifier RL and Population-Level Test-Time Scaling

> **推荐理由 / Why read:** MaxProof将证明生成、验证和修复统一到单一模型，通过四层验证器实现低假阳性RL训练，测试时进化式群体搜索将IMO 2025从27/42提升至35/42，超越人类金牌线。这是将测试时扩展成功应用于严格数学推理的重要突破。
> **Recommendation:** MaxProof unifies proof generation, verification, and repair in a single model via a four-layer verifier for low false-positive RL training. Test-time evolutionary population search lifts IMO 2025 from 27/42 to 35/42, surpassing human gold-medal thresholds — a landmark result in test-time scaling for rigorous mathematical reasoning.

### 2. [[2606.13607]] Reasoning as Pattern Matching: Shared Mechanisms in Human and LLM Everyday Reasoning

> **推荐理由 / Why read:** 通过对比142名人类和25个LLM在11类日常推理任务上的表现，发现两者错误模式高度一致；进一步通过MI分析发现LLM中驱动推理的注意力头实现的是模式匹配而非抽象因果推理，且其激活值能预测人类推理错误（R²=0.66），对"LLM只是模式匹配"的批评提供了深刻的重新解读。
> **Recommendation:** By comparing 142 humans and 25 LLMs across 11 everyday reasoning categories, the study reveals strikingly similar error patterns. Mechanistic interpretability shows LLM reasoning heads implement pattern-matching, not abstract causal inference — and these activations predict human errors (R²=0.66), reframing the "LLMs merely pattern-match" critique.

### 3. [[2606.13125]] Select and Improve: Understanding the Mechanics of Post-Training for Reasoning

> **推荐理由 / Why read:** 通过有限域算术受控实验严格分解RL后训练的两大机制——策略选择（路由到最优SFT策略）和策略改进（数据难度驱动已有策略优化），证明RL不发明新推理策略，只选择和精炼SFT已有的，对理解和设计后训练流程有直接指导意义。
> **Recommendation:** Rigorous mechanistic decomposition via controlled finite-field arithmetic reveals two RL post-training mechanisms — strategy selection and strategy improvement — and proves RL never invents new reasoning strategies, only selects and refines what SFT provides. Direct implications for post-training pipeline design.

---

## 按主题分类 / Papers by Topic

### 🧠 机制可解释性 / Mechanistic Interpretability

| Paper | 简述 / Summary |
|-------|----------------|
| [[2606.12818]] Localizing Anchoring Pathways in Language Models | 用EAP-IG在LLM中定位数值锚定回路，发现低/高锚回路高度共享但指令微调改变关键稀疏边。 / Localizes anchoring circuits in LLMs via EAP-IG; low/high-anchor circuits overlap ~70% but instruction tuning reshapes critical sparse edges. |
| [[2606.12917]] Where Computation Lives Inside TabPFN | 首次对表格基础模型TabPFN进行因果机制分析，发现Head 2的因果必要性远超其他头。 / First causal mechanistic analysis of TabPFN; Head 2 dominates causal necessity 2–5× over other heads. |
| [[2606.12966]] Circuit Synchronization Precedes Generalization | 提出FSD指标，证明Fourier电路形成比grokking提前500–3000步。 / Proposes FSD metric detecting Fourier circuit formation 500–3000 steps before grokking. |
| [[2606.13168]] When Does Routing Become Interpretable? | 证明Block AttnRes路由仅在参与训练时才形成可解释结构，路由权重不等于因果重要性。 / Shows Block AttnRes routing is interpretable only when trained; routing mass ≠ causal importance. |
| [[2606.13209]] Understanding helpfulness and harmless tension in reward models | 揭示RLHF奖励模型中~50%目标特异性神经元被两个目标共享，是多目标对齐困难的根源。 / Reveals ~50% of objective-specific neurons are shared between helpfulness and harmlessness in reward models. |
| [[2606.13603]] Beyond the Commitment Boundary | 发现大型推理模型存在"承诺边界"，之后55%+的CoT步骤对最终答案无实质影响，可截断实现55%推理缩短。 / Discovers "commitment boundary" in reasoning models after which 55%+ of CoT steps are causally inert. |
| [[2606.13607]] Reasoning as Pattern Matching | 发现人类和LLM日常推理错误模式高度一致，LLM推理头实现模式匹配且能预测人类错误。 / Shows human-LLM reasoning error patterns align; LLM reasoning heads implement pattern-matching predictive of human errors. |

### 🔧 优化与训练 / Optimization & Training

| Paper | 简述 / Summary |
|-------|----------------|
| [[2606.12883]] The Hidden Power of Scaling Factor in LoRA Optimization | 揭示LoRA的α因子比学习率更能有效驱动优化，最优α∝256√r，提出LoRA-α超越现有变体。 / Reveals LoRA α dominates learning rate as optimization driver; optimal α∝256√r; LoRA-α outperforms variants. |
| [[2606.12921]] LoRA-Muon: Spectral Steepest Descent on the Low-Rank Manifold | 从流形优化推导LoRA-Muon，实现规范不变性，秩32超越稠密基线。 / Derives LoRA-Muon from manifold optimization with gauge invariance; rank-32 beats dense baseline. |
| [[2606.13276]] Different Layers, Different Manifolds | 发现attention层需Stiefel约束、MLP层适合DGram约束，组合配置HETERO取得最优。 / Attention needs Stiefel constraints, MLP benefits from DGram; HETERO combination wins. |
| [[2606.13287]] Clipping Makes Distributed and Federated ASGD Robust to Stragglers | 证明梯度裁剪消除异步SGD对最大延迟的依赖，提供首个高概率收敛保证。 / Proves gradient clipping removes max-delay dependence in async SGD; first high-probability convergence guarantee. |
| [[2606.13657]] Dense Supervision, Sparse Updates | 揭示on-policy distillation更新呈坐标稀疏（66–90%无变化），仅训练17.5%坐标即可恢复完整性能。 / Shows on-policy distillation updates are coordinate-sparse (66–90% unchanged); 17.5% coordinates recover full performance. |

### 🧊 量化与压缩 / Quantization & Compression

| Paper | 简述 / Summary |
|-------|----------------|
| [[2606.12876]] Multi-Bitwidth Quantization for LLMs Using Additive Codebooks | Drop-by-Drop框架单一模型支持3/4/5-bit切换，存储和训练开销降3倍。 / Drop-by-Drop enables 3/4/5-bit switching from single model; 3× storage and training savings. |
| [[2606.13054]] TWLA: Ternary Weights and Low-Bit Activations | 首次在PTQ下实现1.58-bit权重+4-bit激活联合量化，大幅超越2-bit方法。 / First PTQ framework achieving 1.58-bit weights + 4-bit activations jointly, surpassing 2-bit methods. |
| [[2606.13233]] ReSET: Step-Aware Temperature Scaling for NVFP4 | 基于步骤级熵的自适应温度缩放，NVFP4推理恢复+2.6准确度点，1.97×解码加速。 / Step-aware temperature scaling for NVFP4 reasoning recovers +2.6 accuracy points with 1.97× decoding speedup. |
| [[2606.13300]] Quantizing Time-Series Models As Dynamical Systems | TQS受Lyapunov理论启发量化层灵敏度，发现时序模型量化敏感集中在I/O边界模块。 / TQS uses Lyapunov-inspired sensitivity scoring; time-series quantization sensitivity concentrates at I/O boundary modules. |
| [[2606.13328]] Non-Parametric Dual-Manifold Mapping via 8-Bit Matrices | 8位整数替代浮点MAC，90%截断下仍完美重构，挑战GPU浮点范式。 / Replaces all FP MACs with 8-bit integer sign-voting; perfect reconstruction under 90% truncation. |

### 🤖 推理与后训练 / Reasoning & Post-Training

| Paper | 简述 / Summary |
|-------|----------------|
| [[2606.13125]] Select and Improve: Post-Training for Reasoning | 严格分解RL后训练为策略选择和策略改进，证明RL不发明新策略只选择和精炼。 / Decomposes RL post-training into strategy selection and improvement; RL never invents new strategies. |
| [[2606.13680]] Learning to Reason by Analogy via RA-RFT | RA-RFT训练按推理价值排序的检索器，注入类比范例到RLVR，AIME提升7.1pp。 / RA-RFT trains reasoning-value retriever, injects analogies into RLVR; AIME +7.1pp over GRPO. |
| [[2606.13634]] Operads for Compositional Reasoning in LLMs | 用范畴论operad结构形式化问题分解，提出operadic一致性衡量推理可靠性。 / Formalizes question decomposition via operads; proposes operadic consistency for reasoning reliability. |
| [[2606.13649]] Operadic Consistency: Label-Free Signal | OC信号通过直接回答与分解回答的一致性检测推理失败，与准确率相关r=0.86–0.94。 / OC detects reasoning failures via direct-vs-decomposed answer agreement; correlates r=0.86–0.94 with accuracy. |
| [[2606.13614]] Majority-of-Three is Optimal | 证明三分类器多数投票达到最优PAC样本复杂度，是最简最优投票方案。 / Proves majority-of-three achieves optimal PAC sample complexity — simplest optimal voting scheme. |

### 📊 基准与评测 / Benchmarks & Evaluation

| Paper | 简述 / Summary |
|-------|----------------|
| [[2606.12864]] UOJ-Bench: Code Generation, Hacking, and Repair | 基于真实竞技编程平台的三维评测基准，即使最强模型也无法识别>50%已知错误。 / Three-dimensional benchmark from real competitive programming; frontier models miss >50% of known bugs. |
| [[2606.13020]] SciR: Scientific Reasoning in LLMs | 首个多范式科学推理基准，独立调控推理复杂度和前提提取难度，揭示两者效果叠加。 / First multi-paradigm scientific reasoning benchmark with independent control of complexity and extraction difficulty. |
| [[2606.13111]] MÖVE: German Public Sector LLM Benchmark | 首个德国公共部门综合评测，39个模型上同时评估性能和治理，无单一模型全面领先。 / First holistic German public sector benchmark; 39 models on performance + governance; no single winner. |
| [[2606.13221]] From Uncertain Judgments to Calibrated Rankings | Soft-Elo用校准连续概率替代硬标签，Elo MAE从45.9降至17.9，置信区间缩减39–73%。 / Soft-Elo replaces hard labels with calibrated probabilities; Elo MAE 45.9→17.9, intervals shrink 39–73%. |

### 🧪 知识编辑与表达 / Knowledge Editing & Representation

| Paper | 简述 / Summary |
|-------|----------------|
| [[2606.12841]] TimeROME-DLM: Knowledge Editing for Diffusion LMs | 首个面向扩散语言模型的无训练知识编辑，遗忘log-prob降低83 nats，零额外显存。 / First training-free knowledge editing for diffusion LMs; forget-set log-prob drops ~83 nats, zero extra VRAM. |
| [[2606.13106]] SWITCH: Switchable Latent Reasoning with RL | 通过可切换的隐状态递归结合策略强化学习，提升潜在推理能力。 / Switchable latent recurrence combined with on-policy RL for enhanced latent reasoning. |
| [[2606.13637]] The Stable Recovery Manifold in Continual Learning | 遗忘知识保存在~8维紧凑流形中，灾难性遗忘是流形旋转问题而非信息破坏。 / Forgotten knowledge persists in ~8D recovery manifold; catastrophic forgetting is alignment failure, not information destruction. |

### ⚡ 推理优化与系统 / Inference Optimization & Systems

| Paper | 简述 / Summary |
|-------|----------------|
| [[2606.13126]] MiniPIC: Position-Independent Caching in <100LOC | 78行核心代码实现位置无关KV缓存，2WikiMultihopQA prefill吞吐提升49%。 / 78 LOC core changes enable position-independent KV caching; 49% prefill throughput gain on 2WikiMultihopQA. |
| [[2606.13361]] Can I Buy Your KV Cache? | 将KV Cache作为可交易计算制品，Qwen3-4B上9–50×成本降低且token级无损。 / Treats KV caches as tradeable artifacts; 9–50× cost reduction on Qwen3-4B, token-exact lossless. |
| [[2606.13392]] MiniMax Sparse Attention | 基于GQA的块级稀疏注意力，109B MoE上1M上下文28.4×计算缩减和14.2×加速。 / Blockwise sparse attention atop GQA; 28.4× FLOPs reduction and 14.2× speedup at 1M context on 109B MoE. |
| [[2606.13241]] Brick: Spatial Capability Routing for MoM | 六维能力空间几何路由，最高质量配置超越最强单模型+1.96pp，中性配置成本降4.71×。 / 6D capability-space geometric routing; beats best single model +1.96pp at max quality, 4.71× cost savings at neutral. |

### 🎨 生成模型 / Generative Models

| Paper | 简述 / Summary |
|-------|----------------|
| [[2606.13191]] Geometry of Phase Transitions in Generative Dynamics | 从微分几何解释扩散模型类相变行为，CBD检测器用4%步数实现96%类别控制。 / Geometric theory of diffusion phase transitions; CBD achieves 96% class control with 4% intervention steps. |
| [[2606.13426]] Accelerating Speculative Diffusions via Block Verification | 首次将LLM块验证适配到连续扩散模型，正交分解法实现1.5–6.3%额外加速。 / First block verification for continuous diffusion models via orthogonal decomposition; 1.5–6.3% extra speedup. |
| [[2606.13591]] Multiagent Protocols with Aggregated Confidence Signals | 三种置信度聚合多智能体协议，AUARC提升5–10%，恢复歧义任务的F1损失。 / Three confidence-aggregation multiagent protocols; 5–10% AUARC gain, recovers F1 on ambiguous tasks. |

### 📐 理论 / Theory

| Paper | 简述 / Summary |
|-------|----------------|
| [[2606.12930]] Is Spurious Correlation Removal Always Learnable? | 证明去除虚假相关性存在计算-统计差距，引入环境多样性参数刻画相变。 / Proves computational–statistical gap for spurious correlation removal; introduces environment diversity parameter for phase transitions. |
| [[2606.13092]] Scale Buys Interpolation, Structure Buys a Horizon | 等变世界模型的可计算可预测视界证书，尺度不改善校准——"尺度买插值，不买视界"。 / Computable predictability horizon for equivariant world models; scale doesn't improve calibration. |

### 📡 信号处理与物理系统 / Signal Processing & Physical Systems

| Paper | 简述 / Summary |
|-------|----------------|
| [[2606.12940]] Self-Guidance: Enhancing Neural Codecs | 解码器流形对齐训练方案，4×码本缩减（16K匹配65K），改善下游TTS合成。 / Decoder manifold alignment enables 4× codebook reduction; improves downstream TTS synthesis. |
| [[2606.12997]] Reliability of Probabilistic Emulation of Physical Systems | CRPS集成在物理系统概率预测中显著优于生成式方法，覆盖率和速度均更优。 / CRPS-trained ensembles significantly outperform generative methods for probabilistic physical-system prediction. |
| [[2606.13216]] Layer-Resolved Optimal Transport for Hallucination Detection | 逐层OT分析发现幻觉检测信号集中在L1-L4，Wass-to-Unif达AUROC 0.957。 / Layer-resolved OT analysis finds hallucination signal in L1–L4; Wass-to-Unif AUROC 0.957. |
| [[2606.13439]] S-GBT: Certified Robustness Against Word Substitution Attacks | 二阶Hessian约束为文本分类器提供认证鲁棒性，PSO攻击鲁棒准确率提升23.4%。 / Second-order Hessian bounds provide certified robustness; +23.4% robust accuracy under PSO attack. |

### 🔬 硬件与模拟计算 / Hardware & Analog Computing

| Paper | 简述 / Summary |
|-------|----------------|
| [[2606.13179]] Modern Analog Computing for Differential and Matrix Equations | 综述利用CMOS模拟电路和阻变存储器求解微分/矩阵方程，微秒级求解。 / Reviews analog computing for DE/matrix equations using CMOS and resistive memory; microsecond-scale solving. |
| [[2606.13370]] Training Dynamics in a Small Llama Model | 重复测量实验揭示验证损失在4M token最优后持续退化至3.90，过训练存在隐藏回退。 / Repeated-measures study reveals validation loss degrades from 2.80 (4M tokens) to 3.90 (20M tokens). |
| [[2606.13379]] Positional Encoding in Memristor-Based Analog ASR | 相对位置编码的线性变换超出ADC范围，调整位数分配可降低50%执行退化。 / PE linear transform exceeds ADC range in memristor execution; bit reallocation halves degradation. |

---

## All Papers

| # | ID | Title | 一句话 / One-line Summary |
|---|----|-------|--------------------------|
| 1 | [[2606.12818]] | Localizing Anchoring Pathways in Language Models | EAP-IG定位LLM锚定回路，低/高锚共享66–71%，指令微调改变关键边。 / EAP-IG localizes anchoring circuits; low/high anchors share 66–71%; instruction tuning reshapes edges. |
| 2 | [[2606.12841]] | TimeROME-DLM: Knowledge Editing for Diffusion LMs | 首个扩散LM无训练知识编辑，遗忘log-prob降83 nats，跨6个骨干迁移。 / First training-free knowledge editing for diffusion LMs; −83 nats forget-set log-prob; transfers across 6 backbones. |
| 3 | [[2606.12864]] | UOJ-Bench: Code Generation, Hacking, and Repair | 真实竞技编程三维基准，最强模型仍漏>50%已知错误。 / Three-dimensional competitive programming benchmark; frontier models miss >50% known bugs. |
| 4 | [[2606.12876]] | Multi-Bitwidth Quantization (Drop-by-Drop) | 单一模型3/4/5-bit切换，信息论逐次可精化保证。 / Single model supports 3/4/5-bit switching with information-theoretic successive refinement guarantee. |
| 5 | [[2606.12883]] | The Hidden Power of Scaling Factor in LoRA | α因子比学习率更有效，最优α∝256√r，LoRA-α一致超越变体。 / α dominates learning rate; optimal α∝256√r; LoRA-α consistently outperforms variants. |
| 6 | [[2606.12917]] | Where Computation Lives Inside TabPFN | 首次TabPFN因果机制分析，Head 2因果必要性2–5×领先。 / First causal analysis of TabPFN; Head 2 causal necessity 2–5× larger than others. |
| 7 | [[2606.12921]] | LoRA-Muon: Spectral Steepest Descent | 流形优化推导规范不变LoRA优化器，秩32超越稠密基线。 / Manifold-optimization-derived gauge-invariant LoRA optimizer; rank-32 beats dense baseline. |
| 8 | [[2606.12930]] | Is Spurious Correlation Removal Always Learnable? | 证明去虚假相关性存在计算-统计差距，引入多样性参数γ。 / Proves computational–statistical gap for spurious correlation removal; introduces diversity γ. |
| 9 | [[2606.12940]] | Self-Guidance: Enhancing Neural Codecs | 解码器流形对齐，16K码本匹配65K性能，<0.5%训练开销。 / Decoder manifold alignment; 16K codebook matches 65K; <0.5% training overhead. |
| 10 | [[2606.12966]] | Circuit Synchronization Precedes Generalization | FSD指标提前500–3000步预测grokking，因果证明第二阶段是正则化。 / FSD predicts grokking 500–3000 steps early; causal proof that phase 2 is regularization. |
| 11 | [[2606.12997]] | Reliability of Probabilistic Emulation | CRPS集成在物理系统概率预测中覆盖率和速度优于生成式方法。 / CRPS ensembles outperform generative methods in physical-system probabilistic prediction. |
| 12 | [[2606.13020]] | SciR: Scientific Reasoning Benchmark | 多范式科学推理基准，独立调控复杂度和提取难度，效果叠加。 / Multi-paradigm scientific reasoning benchmark; independent complexity/extraction axes compound. |
| 13 | [[2606.13054]] | TWLA: Ternary Weights Low-Bit Activations | 首次PTQ实现1.58-bit权重+4-bit激活，超越2-bit方法。 / First PTQ achieving 1.58-bit weights + 4-bit activations, surpassing 2-bit methods. |
| 14 | [[2606.13092]] | Scale Buys Interpolation, Structure Buys a Horizon | 等变世界模型的可预测视界证书，尺度不改善校准。 / Predictable horizon certificate for equivariant world models; scale doesn't improve calibration. |
| 15 | [[2606.13106]] | SWITCH: Switchable Latent Reasoning | 可切换隐状态递归结合策略RL提升潜在推理。 / Switchable latent recurrence with on-policy RL for enhanced latent reasoning. |
| 16 | [[2606.13111]] | MÖVE: German Public Sector Benchmark | 39模型性能+治理评测，无单一模型全面领先。 / 39-model performance + governance benchmark; no single model dominates. |
| 17 | [[2606.13125]] | Select and Improve: Post-Training for Reasoning | 严格分解RL后训练为策略选择+改进，RL不发明新策略。 / Decomposes RL post-training into selection + improvement; RL never invents new strategies. |
| 18 | [[2606.13126]] | MiniPIC: Position-Independent Caching | 78行代码实现位置无关KV缓存，prefill吞吐+49%。 / 78 LOC for position-independent KV caching; +49% prefill throughput. |
| 19 | [[2606.13168]] | When Does Routing Become Interpretable? | 路由仅在训练时才可解释，路由权重≠因果重要性。 / Routing interpretable only when trained; routing mass ≠ causal importance. |
| 20 | [[2606.13179]] | Modern Analog Computing | CMOS+阻变存储器求解微分/矩阵方程综述。 / Review of analog computing for DE/matrix equations with CMOS + resistive memory. |
| 21 | [[2606.13191]] | Geometry of Phase Transitions in Generative Dynamics | 微分几何解释扩散相变，CBD用4%步数实现96%控制。 / Geometric theory of diffusion phase transitions; CBD 96% control with 4% steps. |
| 22 | [[2606.13209]] | Helpfulness and Harmless Tension in Reward Models | ~50%目标神经元被两目标共享，是多目标对齐困难的根源。 / ~50% objective-specific neurons shared between objectives; root cause of multi-objective tension. |
| 23 | [[2606.13216]] | Layer-Resolved OT for Hallucination Detection | 逐层OT分析，幻觉信号集中在L1-L4，AUROC最高0.957。 / Layer-resolved OT analysis; hallucination signal in L1–L4; max AUROC 0.957. |
| 24 | [[2606.13221]] | Conformal Elo Estimation for LLM Evaluation | Soft-Elo校准连续胜率，Elo MAE 45.9→17.9，区间缩减39–73%。 / Soft-Elo with calibrated probabilities; Elo MAE 45.9→17.9; intervals shrink 39–73%. |
| 25 | [[2606.13233]] | ReSET: Step-Aware Temperature Scaling for NVFP4 | 步骤级熵自适应温度缩放，NVFP4推理+2.6准确度点，1.97×加速。 / Step-entropy adaptive temperature scaling; NVFP4 +2.6 accuracy, 1.97× speedup. |
| 26 | [[2606.13241]] | Brick: Spatial Capability Routing for MoM | 六维能力空间路由，超越最强单模型+1.96pp，成本降4.71×。 / 6D capability routing; beats best single model +1.96pp; 4.71× cost savings. |
| 27 | [[2606.13276]] | Different Layers, Different Manifolds | Attention需Stiefel约束MLP需DGram，HETERO组合最优。 / Attention needs Stiefel, MLP needs DGram; HETERO combination optimal. |
| 28 | [[2606.13287]] | Clipping Makes ASGD Robust to Stragglers | 梯度裁剪消除异步SGD最大延迟依赖，首个高概率保证。 / Gradient clipping removes max-delay dependence in async SGD; first high-probability guarantee. |
| 29 | [[2606.13300]] | Quantizing Time-Series Models (TQS) | Lyapunov启发的层灵敏度排序，时序模型敏感集中在I/O边界。 / Lyapunov-inspired layer sensitivity; time-series sensitivity at I/O boundaries. |
| 30 | [[2606.13328]] | Non-Parametric Dual-Manifold Mapping via 8-Bit | 8位整数替代浮点MAC，90%截断下完美重构。 / 8-bit integer replaces all FP MACs; perfect reconstruction under 90% truncation. |
| 31 | [[2606.13361]] | Can I Buy Your KV Cache? | KV Cache作为可交易制品，9–50×成本降低，token级无损。 / KV caches as tradeable artifacts; 9–50× cost reduction, token-exact lossless. |
| 32 | [[2606.13370]] | Training Dynamics in a Small Llama Model | 验证损失4M token最优后退化至3.90，过训练存在隐藏回退。 / Validation loss degrades from 2.80 (4M) to 3.90 (20M tokens); hidden overtraining regression. |
| 33 | [[2606.13379]] | Positional Encoding in Memristor-Based ASR | PE线性变换超出ADC范围，调整位数分配降低50%退化。 / PE linear transform exceeds ADC range; bit reallocation halves degradation. |
| 34 | [[2606.13392]] | MiniMax Sparse Attention | GQA块级稀疏注意力，109B MoE 1M上下文28.4×计算缩减。 / Blockwise sparse attention on GQA; 28.4× FLOPs reduction at 1M context on 109B MoE. |
| 35 | [[2606.13426]] | Accelerating Speculative Diffusions via Block Verification | 块验证首次适配连续扩散，正交分解法+1.5–6.3%额外加速。 / Block verification for continuous diffusion via orthogonal decomposition; +1.5–6.3% speedup. |
| 36 | [[2606.13439]] | S-GBT: Certified Robustness Against Word Substitution | 二阶Hessian约束提供认证鲁棒性，PSO鲁棒准确率+23.4%。 / Second-order Hessian bounds for certified robustness; +23.4% under PSO attack. |
| 37 | [[2606.13473]] | MaxProof: Scaling Mathematical Proof | 四层验证器RL+群体搜索，IMO 2025从27→35/42超金牌线。 / Four-layer verifier RL + population search; IMO 2025 27→35/42 surpassing gold medal. |
| 38 | [[2606.13591]] | Multiagent Protocols with Aggregated Confidence | 三种置信度聚合协议，AUARC提升5–10%，恢复歧义任务F1。 / Three confidence-aggregation protocols; 5–10% AUARC gain; recovers ambiguous-task F1. |
| 39 | [[2606.13603]] | Beyond the Commitment Boundary | 承诺边界后55%+ CoT步骤因果无效，可截断缩短55%推理。 / 55%+ CoT steps causally inert after commitment boundary; enables 55% reasoning truncation. |
| 40 | [[2606.13607]] | Reasoning as Pattern Matching | 人类与LLM推理错误高度一致，LLM注意力头实现模式匹配预测人类错误。 / Human-LLM reasoning errors align; LLM attention heads pattern-match and predict human errors. |
| 41 | [[2606.13614]] | Majority-of-Three is Optimal | 三分类器多数投票达到最优PAC样本复杂度。 / Majority-of-three achieves optimal PAC sample complexity. |
| 42 | [[2606.13634]] | Operads for Compositional Reasoning | 范畴论operad形式化问题分解，operadic一致性衡量推理可靠性。 / Operad formalism for question decomposition; operadic consistency measures reliability. |
| 43 | [[2606.13637]] | The Stable Recovery Manifold | 遗忘知识保存在~8维流形，灾难性遗忘是流形旋转而非信息破坏。 / Forgotten knowledge in ~8D manifold; catastrophic forgetting is alignment failure. |
| 44 | [[2606.13649]] | Operadic Consistency: Label-Free Signal | OC检测推理失败，与准确率r=0.86–0.94，是唯一四数据集≥0.85的信号。 / OC detects reasoning failures; r=0.86–0.94 with accuracy; only signal ≥0.85 on all four datasets. |
| 45 | [[2606.13657]] | Dense Supervision, Sparse Updates | On-policy distillation更新坐标稀疏66–90%，17.5%坐标恢复完整性能。 / OPD updates 66–90% coordinate-sparse; 17.5% coordinates recover full performance. |
| 46 | [[2606.13680]] | Learning to Reason by Analogy (RA-RFT) | 按推理价值排序的检索器注入RLVR，AIME +7.1pp。 / Reasoning-value retriever injected into RLVR; AIME +7.1pp over GRPO. |
