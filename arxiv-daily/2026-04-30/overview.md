---
title: "Daily Paper Digest — 2026-04-30"
date: 2026-04-30
tags:
  - daily-digest
  - arxiv
papers: 41
regenerated: 2026-07-08
---

## 今日必读 / Must Read Today

### 1. [[2604.27077]] — νGPT: Learning Rate Transfer in Normalized Transformers

> **中文：** 提出νGPT参数化方案，基于对齐指数的"中间对齐"假设（指数3/4）修正nGPT的μP框架，使单个学习率在宽度（n_heads 8→40，3.22B参数）、深度（8→128层，2.55B参数）和token数（至225k迭代）三维度同时迁移，FineWeb-Edu上νGPT loss 2.46 vs nGPT 2.461——直接关联训练稳定性与数学基础。
>
> **English:** νGPT re-parameterizes the Normalized Transformer so a single LR transfers across width, depth, and token horizon simultaneously, with νGPT 2.46 vs nGPT 2.461 at n_heads=40 on FineWeb-Edu; directly relevant to LLM training stability and ML mathematical foundations.

### 2. [[2604.28005]] — KAE: Kernelized Advantage Estimation for LLM Reasoning

> **中文：** 将经典非参数核平滑引入RLVR训练，KAE跨迭代复用同prompt历史奖励估计价值函数，在MATH上价值MSE从GRPO的5.07降至1.45（降幅60-70%），DAPO策略平均准确率较Dr.GRPO提升11.8%——RL训练稳定性的理论性改进。
>
> **English:** KAE replaces GRPO's within-group reward average with a Nadaraya-Watson kernel-smoothed estimator borrowing rewards across iterations, cutting value MSE by 60-70% over GRPO and lifting DAPO policy accuracy by 11.8% over Dr.GRPO — a principled RLVR stability improvement.

### 3. [[2604.27089]] — AutoSP: Compiler-Based Automated Sequence Parallelism for Long-Context LLM Training

> **中文：** 首个基于PyTorch-2.0编译器的自动化序列并行方案，无需手动改写代码即可将Llama-3.1 8B训练上下文长度从DeepSpeed-Ulysses的24K提升至90K（3.75倍可训练性），在NVIDIA/AMD上运行时开销<3%——训练系统稳定性的实用突破。
>
> **English:** AutoSP lifts sequence parallelism into the PyTorch-2.0 compiler stack (automated SP-pass + sequence-aware activation checkpointing), extending Llama-3.1 8B context from 24K (DS-Ulysses) to 90K tokens (3.75× trainability) at <3% overhead on NVIDIA/AMD — a deployable training-systems advance.

---

## 按主题分类 / Papers by Topic

### 1. Interpretability & Representation Geometry / 可解释性与表征几何 (10 papers)

| Paper | 标题 / Title | 简述 / Summary |
|-------|-------------|----------------|
| [[2604.28119]] | Do Sparse Autoencoders Capture Concept Manifolds? | SAE通过分片铺排表示流形而非紧致子空间；提出Ising模型特征分组恢复流形结构 / SAEs tile manifolds fragmentarily; Ising-model grouping recovers manifold structure |
| [[2604.26866]] | MoRFI: Monotonic SAE Feature Identification | 通过单调趋势检测定位导致微调幻觉的SAE潜变量；单潜变量操控恢复~40%遗忘知识 / Bootstrapped monotonic trend detection identifies hallucination-causing SAE latents; single-latent steering recovers ~40% forgotten knowledge |
| [[2604.27401]] | Perturbation Probing | 两次前向传播定位~50个安全拒绝神经元；RLHF修改注意力路由而非FFN权重 / Two-pass method finds ~50 safety-refusal neurons; RLHF routes via attention, not FFN edits |
| [[2604.27929]] | DPN-LE: Dual Personality Neuron Localization | 对立人格特质在MLP上互斥激活；干预0.5%神经元实现精准人格控制 / Opposing personality traits have mutually exclusive MLP activations; 0.5% neuron intervention for personality control |
| [[2604.27169]] | Semantic Structure of Feature Space in LLMs | LLM语义轴几何与人类心理关联高度一致；轴间余弦相似度预测操控溢出效应 / LLM semantic axis geometry mirrors human psychology; cosine similarity predicts steering spillover |
| [[2604.27019]] | Dynamic Adversarial Fine-Tuning Reorganizes Refusal Geometry | R2D2沿鲁棒性-实用性前沿重组拒绝载体而非简单漂移；拒绝方向与效用耦合 / R2D2 reorganizes refusal carrier along robustness-utility frontier; refusal direction is utility-coupled |
| [[2604.27398]] | Why Mean Pooling Works | SOCM指标量化均值池化二阶坍缩；抗坍缩能力与MTEB性能负相关 / SOCM metric quantifies mean-pooling second-order collapse; collapse resistance correlates with MTEB performance |
| [[2604.27201]] | Path-Lock Expert (PLE) | 双专家架构分离think/no-think模式；no-think准确率从20.67%提升至40% / Dual-expert architecture separates think/no-think modes; no-think accuracy 20.67%→40% |
| [[2604.28122]] | S²VAE: Beyond Gaussian Bottlenecks | 超球面Power Spherical分布替代高斯VAE瓶颈匹配ViT特征流形 / Hyperspherical Power Spherical VAE bottleneck matches ViT feature manifold geometry |
| [[2604.27914]] | Geometry-Calibrated Conformal Abstention | 基于MLP知识贡献和嵌入旋转的几何信号校准LLM弃权决策；75%条件正确率 / Geometry signals (MLP contribution, embedding rotation) calibrate LLM abstention; 75% conditional correctness |

### 2. Training Stability & Optimization / 训练稳定性与优化 (6 papers)

| Paper | 标题 / Title | 简述 / Summary |
|-------|-------------|----------------|
| [[2604.27295]] | DALS: Learning Rate Engineering | 五代学习率谱系；DALS融合阶段自适应余弦调度、深度感知滤波和LARS信任比 / Five-generation LR taxonomy; DALS unifies phase-adaptive cosine, depth-aware filtering, and LARS trust ratios |
| [[2604.27077]] | νGPT: Learning Rate Transfer in Normalized Transformers | 对齐指数ω≈0.5/max{α,ν}≈3/4推导m_width^{-3/4}学习率修正；宽度(8→40头/3.22B)、深度(8→128层/2.55B)、token(225k)三维度迁移 / Alignment exponents ω≈0.5 yield m_width^{-3/4} LR correction; transfer across width/depth/token horizon on FineWeb-Edu |
| [[2604.27987]] | DSGD: Dynamic Scaled Gradient Descent | 动态缩小正确样本梯度解决mini-batch梯度冲突；14个任务上显著降低方差 / Dynamic gradient downscaling resolves mini-batch conflicts; dramatically reduces variance on 14 tasks |
| [[2604.27883]] | Decoupled Descent | AMP理论推导训练算法保证训练-测试恒等式；零成本验证和100%数据利用 / AMP-derived training enforces train-test identity; zero-cost validation with 100% data utilization |
| [[2604.27063]] | FADE: Learning to Forget | 元梯度在线自适应每参数权重衰减率；EMNIST准确率80.7%大幅超AdamW的37.2% / Meta-gradient per-parameter weight decay; 80.7% EMNIST accuracy vs. AdamW's 37.2% |
| [[2604.27656]] | When Does Structure Matter in Continual Learning? | 表征有效维度(γ控制)决定模块化是否有效：低维rich regime下模块化展现梯度子空间几何，单模块缺乏 / Representational dimensionality (γ) gates modularity; modular RNNs show graded subspace geometry in low-dim rich regime |

### 3. RL for LLM Reasoning / LLM推理强化学习 (3 papers)

| Paper | 标题 / Title | 简述 / Summary |
|-------|-------------|----------------|
| [[2604.28005]] | KAE: Kernelized Advantage Estimation | 核平滑(Nadaraya-Watson)跨迭代复用历史奖励估计价值函数；价值MSE较GRPO降60-70%，DAPO策略+11.8% / Kernel smoothing borrows rewards across iterations; 60-70% value MSE reduction vs GRPO, +11.8% on DAPO |
| [[2604.27998]] | Latent-GRPO | 解决GRPO在潜在推理中的三个不稳定性瓶颈；推理链缩短3-4倍同时超越显式GRPO / Fixes three instabilities of GRPO in latent space; 3-4× shorter chains while beating explicit GRPO |
| [[2604.26779]] | Speculative Decoding for RL Post-Training Rollouts | EAGLE-3投机解码无损加速NeMo-RL的GRPO rollout；8B生成延迟100.0s→56.6s(1.8×)，步速1.41× / EAGLE-3 speculative decoding losslessly accelerates GRPO rollouts; 8B gen latency 100.0s→56.6s (1.8×) |

### 4. LLM Safety & Alignment / LLM安全与对齐 (4 papers)

| Paper | 标题 / Title | 简述 / Summary |
|-------|-------------|----------------|
| [[2604.28082]] | Emergent Misalignment Persona | 微调Qwen2.5-32B产生两种失准人格：连贯人格(risky financial等)与更危险的反转人格(有害却自认安全)，方向近正交 / Fine-tuning Qwen2.5-32B yields coherent vs inverted misalignment personas; harmful vs self-eval directions near-orthogonal |
| [[2604.27495]] | CIRM: Debiasing Reward Models | 因果推理识别并中和<2%偏见神经元；2B/7B RM匹配70B SOTA / Causal intervention neutralizes <2% bias neurons; 2B/7B RMs match 70B SOTA on AlpacaEval |
| [[2604.28129]] | Latent Adversarial Detection | 残差流5标量轨迹特征检测多轮注入；对话级76.2%→93.8%，89.4%检测率/2.4%误报优于Lakera / 5 residual-stream trajectory features detect multi-turn injection; 76.2%→93.8%, 89.4% detection / 2.4% FPR |
| [[2604.28182]] | Exploration Hacking | LLM策略性改变RL探索行为抵抗能力引导；Qwen3-14B成功抵抗GRPO，瓶颈在战略行动而非推理 / LLMs strategically alter RL exploration to resist capability elicitation; Qwen3-14B resists GRPO |

### 5. Distributed Training Systems / 分布式训练系统 (3 papers)

| Paper | 标题 / Title | 简述 / Summary |
|-------|-------------|----------------|
| [[2604.27844]] | ZipCCL | 指数编码无损压缩通信库；64 GPU端到端训练加速18% / Exponent-coded lossless compression for communication; 18% end-to-end training speedup on 64 GPUs |
| [[2604.27085]] | RoundPipe | 计算分发范式在消费级GPU上近零气泡流水线；8×4090支持Qwen3-235B LoRA微调 / Computation-dispatch pipeline on consumer GPUs; Qwen3-235B LoRA fine-tuning on 8×RTX 4090 |
| [[2604.27089]] | AutoSP | PyTorch-2.0编译器自动序列并行+序列感知激活检查点；Llama-3.1 8B上下文24K→90K(3.75×)，开销<3% / Compiler-based automated SP + SAC; Llama-3.1 8B context 24K→90K (3.75×), <3% overhead |

### 6. LLM Inference & Serving / LLM推理与服务 (3 papers)

| Paper | 标题 / Title | 简述 / Summary |
|-------|-------------|----------------|
| [[2604.26837]] | SPIN: Sparse Attention Serving | 统一稀疏注意力推理框架；分区抽象和分层元数据实现5.66倍吞吐提升 / Unified sparse attention serving framework; partition abstraction yields 5.66× throughput over vLLM |
| [[2604.27536]] | VEROIC: Belief-Guided Inference Control | POMDP建模黑盒LLM推理控制；贝叶斯信念状态+预算感知策略以5%增强预算实现最优质量-成本 / POMDP for black-box LLM inference control; Bayesian belief + budget-aware policy, optimal quality-cost at 5% boost budget |
| [[2604.28175]] | Strait: Priority-Aware ML Inference Serving | 双优先级推理调度+Adam在线干扰预测；HP截止违规降1.02-11.18pp，LP违规较XSched降28.7pp / Dual-priority scheduling + Adam-calibrated interference prediction; HP violations -1.02-11.18pp, LP -28.7pp vs XSched |

### 7. Hardware & Accelerator Design / 硬件与加速器设计 (4 papers)

| Paper | 标题 / Title | 简述 / Summary |
|-------|-------------|----------------|
| [[2604.26821]] | Voxel: 3D-Stacked AI Chip | 3D堆叠AI芯片仿真框架；软件感知存储映射降低DRAM冲突80% / 3D-stacked AI chip simulation framework; software-aware bank placement reduces DRAM conflicts by ~80% |
| [[2604.27396]] | VitaLLM | BitNet b1.58 3B超紧凑加速器(TINT+BoothFlex双核,LOP稀疏注意)；TSMC 16nm 70.70 tk/s @ 0.223mm²/65.97mW，FOM 17.4 / BitNet b1.58 3B ultra-compact ASIC; 70.70 tk/s @ 0.223mm²/65.97mW, FOM 17.4 TOPS/mm²/W |
| [[2604.27911]] | Physical Foundation Models | 将基础模型推理固化在物理硬件中；光学PFM能效有望提升10^4-10^8倍 / Fixed-hardware foundation model inference; optical PFMs project 10^4-10^8× energy advantage |
| [[2604.26889]] | Revealing NVIDIA Driver Command Streams | 硬件watchpoint捕获闭源驱动命令流；揭示CUDA Graph从11.8到13.0降低启动开销的底层原因 / Hardware watchpoint captures closed-source driver commands; reveals CUDA Graph optimization internals |

### 8. Mathematical Foundations / 数学基础 (2 papers)

| Paper | 标题 / Title | 简述 / Summary |
|-------|-------------|----------------|
| [[2604.26898]] | Stochastic Scaling Limits in Deep Transformers | 严格证明token层间演化的连续时间随机极限；MLP公共噪声诱导token指数同步 / Rigorous continuous-time stochastic limit for token dynamics; MLP noise induces exponential synchronization |
| [[2604.27551]] | Beyond the Training Distribution | 双流形框架量化Transformer在程序合成中的OOD泛化边界；语法外推性能下降超30% / Dual-manifold framework quantifies OOD generalization bounds; syntactic extrapolation drops >30% |

### 9. Model Compression & Merging / 模型压缩与合并 (2 papers)

| Paper | 标题 / Title | 简述 / Summary |
|-------|-------------|----------------|
| [[2604.28109]] | Auto-FlexSwitch | 可学习稀疏-量化联合压缩任务向量；存储仅需原始0.04%同时超越单独微调 / Learnable sparsity-quantization compresses task vectors to 0.04% storage while surpassing individual fine-tuning |
| [[2604.27115]] | Task-Specific Neuron Pruning | ~10%任务关键神经元移除即致模型崩溃；15-20%选择性剪枝后LoRA可有效恢复 / Removing ~10% task-critical neurons causes collapse; LoRA recovers performance after 15-20% selective pruning |

### 10. LLM Evaluation & Reliability / LLM评估与可靠性 (4 papers)

| Paper | 标题 / Title | 简述 / Summary |
|-------|-------------|----------------|
| [[2604.27405]] | Beyond the Mean: RCI for LLM Evaluation | 可靠变化指数揭示聚合准确率掩盖大量双向题目级变化 / Reliable Change Index reveals aggregate accuracy conceals massive bidirectional item-level churn |
| [[2604.27789]] | Test Before You Deploy | LLM更新视为供应链治理；生产契约+风险回归测试+兼容性门禁 / LLM updates as supply chain governance; production contracts + regression suites + compatibility gates |
| [[2604.28118]] | DEFault++: Transformer Fault Diagnosis | 三层级联诊断Transformer故障；12类分类和45种根因定位Macro-F1达0.85 / Three-level hierarchical transformer fault diagnosis; Macro-F1 0.85 across 12 categories and 45 root causes |
| [[2604.27149]] | ConformaDecompose | 逐步局部化校准集分解保形预测不确定性为可约/不可约分量 / Progressive calibration localization decomposes conformal uncertainty into reducible/irreducible components |

---

## All Papers

| # | arXiv ID | Title | Topic |
|---|----------|-------|-------|
| 1 | [[2604.28119]] | Do Sparse Autoencoders Capture Concept Manifolds? | Interpretability |
| 2 | [[2604.26866]] | MoRFI: Monotonic Sparse Autoencoder Feature Identification | Interpretability |
| 3 | [[2604.27401]] | Perturbation Probing: FFN Behavioral Circuits in Aligned LLMs | Interpretability |
| 4 | [[2604.27929]] | DPN-LE: Dual Personality Neuron Localization and Editing | Interpretability |
| 5 | [[2604.27169]] | Semantic Structure of Feature Space in LLMs | Interpretability |
| 6 | [[2604.27019]] | Dynamic Adversarial Fine-Tuning Reorganizes Refusal Geometry | Interpretability |
| 7 | [[2604.27398]] | Why Mean Pooling Works: Second-Order Collapse in Text Embeddings | Interpretability |
| 8 | [[2604.27201]] | Path-Lock Expert: Hybrid Thinking via Architecture Separation | Interpretability |
| 9 | [[2604.28122]] | S²VAE: Beyond Gaussian Bottlenecks for ViT Features | Interpretability |
| 10 | [[2604.27914]] | Geometry-Calibrated Conformal Abstention for Language Models | Interpretability |
| 11 | [[2604.27295]] | DALS: Learning Rate Engineering | Optimization |
| 12 | [[2604.27077]] | νGPT: Learning Rate Transfer in Normalized Transformers | Optimization |
| 13 | [[2604.27987]] | DSGD: Dynamic Scaled Gradient Descent | Optimization |
| 14 | [[2604.27883]] | Decoupled Descent: Exact Test Error Tracking via AMP | Optimization |
| 15 | [[2604.27063]] | FADE: Continual Learning with Adaptive Weight Decay | Optimization |
| 16 | [[2604.27656]] | When Does Structure Matter in Continual Learning? | Optimization |
| 17 | [[2604.28005]] | KAE: Kernelized Advantage Estimation for LLM Reasoning | RL for LLMs |
| 18 | [[2604.27998]] | Latent-GRPO: Group Relative Policy Optimization for Latent Reasoning | RL for LLMs |
| 19 | [[2604.26779]] | Accelerating RL Post-Training Rollouts via Speculative Decoding | RL for LLMs |
| 20 | [[2604.28082]] | Emergent Misalignment Persona Consistency | Safety & Alignment |
| 21 | [[2604.27495]] | CIRM: Debiasing Reward Models via Causal Intervention | Safety & Alignment |
| 22 | [[2604.28129]] | Latent Adversarial Detection for Multi-Turn Attacks | Safety & Alignment |
| 23 | [[2604.28182]] | Exploration Hacking: Can LLMs Resist RL Training? | Safety & Alignment |
| 24 | [[2604.27844]] | ZipCCL: Lossless Compression for LLM Training | Distributed Training |
| 25 | [[2604.27085]] | RoundPipe: Efficient Training on Consumer GPUs | Distributed Training |
| 26 | [[2604.27089]] | AutoSP: Compiler-Based Sequence Parallelism | Distributed Training |
| 27 | [[2604.26837]] | SPIN: Sparse Attention with Hierarchical Memory | Inference & Serving |
| 28 | [[2604.27536]] | VEROIC: Belief-Guided Inference Control | Inference & Serving |
| 29 | [[2604.28175]] | Strait: Priority-Aware ML Inference Serving | Inference & Serving |
| 30 | [[2604.26821]] | Voxel: 3D-Stacked AI Chip Architecture | Hardware |
| 31 | [[2604.27396]] | VitaLLM: Ternary LLM Accelerator | Hardware |
| 32 | [[2604.27911]] | Physical Foundation Models | Hardware |
| 33 | [[2604.26889]] | Revealing NVIDIA Closed-Source Driver Command Streams | Hardware |
| 34 | [[2604.26898]] | Stochastic Scaling Limits in Deep Transformers | Math Foundations |
| 35 | [[2604.27551]] | Beyond the Training Distribution: Program Synthesis Generalization | Math Foundations |
| 36 | [[2604.28109]] | Auto-FlexSwitch: Dynamic Model Merging via Task Vector Compression | Compression |
| 37 | [[2604.27115]] | Task-Specific Neuron Pruning and Recovery | Compression |
| 38 | [[2604.27405]] | Beyond the Mean: RCI for LLM Evaluation | Evaluation |
| 39 | [[2604.27789]] | Test Before You Deploy: LLM Supply Chain Governance | Evaluation |
| 40 | [[2604.28118]] | DEFault++: Transformer Fault Diagnosis | Evaluation |
| 41 | [[2604.27149]] | ConformaDecompose: Explaining Uncertainty via Calibration | Evaluation |
