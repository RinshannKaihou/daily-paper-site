---
title: "Daily Paper Overview — 2026-04-27"
date: 2026-04-27
tags:
  - llm-safety
  - efficient-inference
  - representation-learning
  - adversarial-robustness
  - mechanistic-interpretability
  - model-compression
  - self-supervised-learning
  - diffusion-models
  - learning-theory
  - edge-deployment
  - multi-objective-alignment
  - quantum-computing
  - FPGA
  - HCI
papers: 51
---

## 今日必读 / Must Read Today

**1. [[2604.24647v1]] DepthKV** -- Layer-Dependent KV Cache Pruning for Long-Context LLM Inference  
- 发现Transformer各层对KV Cache剪枝的敏感度存在统计显著差异，提出基于InfoNCE的逐层非均匀预算分配。 / Reveals statistically significant layer-wise variation in KV cache pruning sensitivity; proposes InfoNCE-guided non-uniform budget allocation.  
- 在60%全局剪枝率下，ROUGE-1从26.75提升至29.75，HotpotQA EM从12%提升至23%。 / At 60% pruning, ROUGE-1 improves 26.75→29.75, HotpotQA EM 12%→23%.

**2. [[2604.24512v1]] SSRP** -- Beyond the Attention Stability Boundary: Agentic Self-Synthesizing Reasoning Protocols  
- 形式化了LLM智能体在多轮对话中的"注意力锁定"失败模式，GPT 5.4在语义劫持任务中从0.1%恢复到71.6%。 / Formalizes the "Attention Latch" failure; recovers GPT 5.4 from 0.1% to 71.6% on semantic hijacking via Architect-Executive separation.  
- 揭示该失败是注意力架构瓶颈而非推理能力不足（Reflexion基线100%成功）。 / Proves the failure is attentional, not reasoning (Reflexion baseline: 100%).

**3. [[2604.24542v1]] LCF** -- Layerwise Convergence Fingerprints for Runtime Misbehavior Detection in LLMs  
- 无需训练、无需参考模型、仅200条校准样本即可在prefill阶段统一检测后门/越狱/提示注入三类威胁。 / Tuning-free runtime monitor detecting backdoors, jailbreaks, and prompt injections at prefill with only 200 calibration samples.  
- 推理开销低于0.1%，后门ASR降至1%以下，越狱检测率92-100%。 / <0.1% overhead; backdoor ASR <1%, jailbreak detection 92-100%.

---

## 按主题分类 / Papers by Topic

### 大模型安全与对齐 / LLM Safety & Alignment

| Paper | 一句话描述 / One-line Description |
|-------|----------------------------------|
| [[2604.24162v1]] TIGS | 即插即用的推理时后门防御，仅12.9%延迟开销，跨密集/MoE架构ASR降至4-14%。 / Plug-and-play inference-time backdoor defense; 12.9% latency; ASR 4-14% across dense/MoE. |
| [[2604.24178v1]] Meal | 双层元学习多目标对齐，动态偏好权重优于静态方法。 / Bi-level meta-learning for multi-objective alignment with dynamic preference weights. |
| [[2604.24542v1]] LCF | 层间隐藏状态差值统计异常检测，统一检测后门/越狱/注入。 / Statistical anomaly detection on inter-layer hidden-state diffs for unified threat detection. |
| [[2604.24618v1]] Sabotage Eval | 评估前沿模型破坏安全研究的倾向，发现Mythos Preview 7%持续破坏率。 / Evaluates frontier models' propensity to sabotage safety research; Mythos Preview: 7% continuation rate. |
| [[2604.24668v1]] Sycophancy in Finance | 个性化偏好注入引发LLM金融任务严重谄媚行为。 / Personalized preference injection triggers severe sycophancy in financial tasks. |
| [[2604.24686v1]] RiskGate | 基于可行性理论的自主AI代理运行时治理框架。 / Viability-theory-based runtime governance for autonomous AI agents. |
| [[2604.24698v1]] Persona Collapse | 发现LLM人格模拟中的"人格坍缩"现象，高保真度反而产生刻板种群。 / Discovers "Persona Collapse" where high-fidelity models produce stereotyped populations. |
| [[2604.24693v1]] CLAS | 上下文自适应的激活引导，通过感知向量动态调整引导强度。 / Context-dependent activation steering via learned sensing vectors. |

### 高效推理与模型压缩 / Efficient Inference & Compression

| Paper | 一句话描述 / One-line Description |
|-------|----------------------------------|
| [[2604.24647v1]] DepthKV | 逐层非均匀KV缓存剪枝，基于InfoNCE分配预算。 / Layer-dependent non-uniform KV cache pruning guided by InfoNCE. |
| [[2604.24432v1]] KSA | 摘要token序列级语义压缩，KV缓存降至0.22%（组合MLA）。 / Summary-token sequence compression; KV cache down to 0.22% with MLA. |
| [[2604.24715v1]] HyLo | 预训练Transformer回收为混合架构(MLA+Mamba2)，支持2M token推理。 / Upcycles pretrained Transformers to hybrid MLA+Mamba2; enables 2M-token serving. |
| [[2604.24380v1]] VLM Pruning | 系统研究LVLM结构化剪枝，宽度剪枝优于层剪枝，30%为安全阈值。 / Systematic study of LVLM pruning; widthwise > layerwise; 30% is safe threshold. |
| [[2604.24374v1]] MIPIC | Matryoshka表示学习的双轴(维度+深度)自蒸馏框架。 / Dual-axis (dimension+depth) self-distillation for Matryoshka representation learning. |
| [[2604.24154v1]] LPA | 残差网络渐进逼近理论，"训练一次、使用N个模型"。 / Progressive approximation theory for residual networks; "train once, deploy N models." |
| [[2604.24273v1]] BitRL | 1-bit量化LLM+RL边缘部署，树莓派4上24.8ms延迟。 / 1-bit quantized LLM + RL for edge; 24.8ms latency on Raspberry Pi 4. |
| [[2604.24708v1]] HDET | 利用DDP副本做学习率自动探索，零额外硬件开销。 / Repurposes DDP replicas for automatic LR exploration at zero hardware cost. |
| [[2604.24717v1]] SIREN-RoPE | 将RoPE扩展为可学习的时间信号空间，自主发现日/周周期。 / Extends RoPE to learnable temporal signal space; auto-discovers daily/weekly cycles. |

### 机制可解释性与表示学习 / Mechanistic Interpretability & Representation Learning

| Paper | 一句话描述 / One-line Description |
|-------|----------------------------------|
| [[2604.24302v1]] DFA Circuit Transfer | 可微忠实度对齐实现跨模型电路迁移，小模型电路知识可迁移到大模型。 / Differentiable faithfulness alignment for cross-model circuit transfer. |
| [[2604.24357v1]] DPRM | Doob h变换过程奖励引导的扩散语言模型token排序控制。 / Doob h-transform process-reward-guided token ordering for diffusion LMs. |
| [[2604.24672v1]] Functorial DL | 预层/余预层范畴论框架统一刻画CNN/MPNN/RNN，解释对抗脆弱性等局限。 / Presheaf/copresheaf categorical framework unifying CNN/MPNN/RNN; explains adversarial vulnerability. |
| [[2604.24393v1]] Linear Regions SSL | SSL模型线性区域几何分析，SSL用更少区域达到相当准确率。 / Linear region geometry of SSL models; SSL achieves comparable accuracy with fewer regions. |
| [[2604.24469v1]] SSL for Retrieval | 高各向异性SSL嵌入严重降低ANN检索性能，线性探针不预测检索效果。 / Highly anisotropic SSL embeddings degrade ANN retrieval; linear probe doesn't predict retrieval quality. |
| [[2604.24498v1]] HyDeS | 超球面密度 shaping 自监督方法，分割性能优异但细粒度分类较弱。 / Hyperspherical density shaping SSL; strong segmentation but weak fine-grained classification. |

### 对抗鲁棒性与安全验证 / Adversarial Robustness & Verification

| Paper | 一句话描述 / One-line Description |
|-------|----------------------------------|
| [[2604.24332v1]] DDG | 快速对抗训练中的分布感知动态引导，单步超越多步方法。 / Distribution-aware dynamic guidance for fast adversarial training; single-step beats multi-step. |
| [[2604.24350v1]] CO as Backdoor | 从后门视角重新解释快速对抗训练中的灾难性过拟合。 / Reinterprets catastrophic overfitting in FAT as backdoor-like trigger overfitting. |
| [[2604.24379v1]] Super-DeepG | GPU友好的几何鲁棒性认证，526倍加速，首次扩展到TinyImageNet。 / GPU-friendly geometric robustness certification; 526x speedup; first on TinyImageNet. |
| [[2604.24170v1]] CREDENCE | 概念瓶颈模型中的认知-偶然不确定性分解与决策路由。 / Epistemic-aleatoric uncertainty decomposition in concept bottleneck models with decision routing. |

### 扩散模型与生成 / Diffusion Models & Generation

| Paper | 一句话描述 / One-line Description |
|-------|----------------------------------|
| [[2604.24238v1]] GeoEdit | 流形切空间估计实现免训练扩散模型连续编辑。 / Manifold tangent space estimation for training-free continuous diffusion editing. |
| [[2604.24196v1]] Companion-Elliptic Kernels | 生成漂移框架的可辨识性与稳定性理论，分类为高斯+Matern核。 / Identifiability and stability theory for generative drifting; classifies as Gaussian+Matern kernels. |

### 训练优化与学习理论 / Training Optimization & Learning Theory

| Paper | 一句话描述 / One-line Description |
|-------|----------------------------------|
| [[2604.24313v1]] SAL | 自抽象层级式训练框架，缓解梯度消失和数据稀缺问题。 / Self-abstraction hierarchical training; mitigates gradient vanishing and data scarcity. |
| [[2604.24356v1]] Primitive Recursion | 原始递归函数的五种动力学等价刻画，组合操作可从动力学中涌现。 / Five-way dynamical equivalence for primitive recursion; composition emerges from dynamics. |
| [[2604.24749v1]] Optimal Sample Complexity | 解决2014年猜想，确定多类学习最优样本复杂度为Theta(d_DS/epsilon)。 / Resolves 2014 conjecture; establishes optimal multiclass sample complexity as Theta(d_DS/epsilon). |
| [[2604.24737v1]] Multiple Thinkers CoT | 多思考者CoT学习的计算复杂度分析，被动困难但主动Boosting高效。 / Multi-thinker CoT learning complexity; passive is hard, active boosting is efficient. |
| [[2604.24517v1]] Prior-Agnostic Forecast | 状态空间未知的鲁棒预测聚合，简洁log-odds聚合器近优。 / Robust forecast aggregation with unknown state space; simple log-odds aggregator is near-optimal. |
| [[2604.24545v1]] Extreme Bandits | 半参数假设下极端bandit问题的有限时间遗憾界。 / Finite-time regret bounds for extreme bandits under semi-parametric assumptions. |
| [[2604.24745v1]] HRGrad | 流形等距旋转解决多尺度动理学方程多任务梯度冲突。 / Manifold isometric rotation for resolving gradient conflicts in multiscale kinetic equations. |

### 多模态与音频 / Multimodal & Audio

| Paper | 一句话描述 / One-line Description |
|-------|----------------------------------|
| [[2604.24401v1]] Audio-Language Eval | 揭示音频-语言基准60-72%分数无需音频即可获得。 / Reveals 60-72% of audio-language benchmark scores achievable without audio. |
| [[2604.24278v1]] RAS | ASR弃权感知框架，片段级占位符机制+RAS指标+GRPO训练。 / ASR abstention-aware framework with segment-level placeholders, RAS metric, and GRPO training. |

### 智能体与系统 / Agents & Systems

| Paper | 一句话描述 / One-line Description |
|-------|----------------------------------|
| [[2604.24512v1]] SSRP | 注意力锁定失败模式形式化与Architect-Executive分离解决方案。 / Formalizes Attention Latch failure and proposes Architect-Executive separation. |
| [[2604.24348v1]] OS-SPEAR | OS Agent四维评估工具包（安全/性能/效率/鲁棒性），22个模型评测。 / Four-dimensional OS agent evaluation toolkit; benchmarks 22 models. |
| [[2604.24468v1]] SL-LLM Survey | 首篇分割学习与LLM微调交叉领域的系统综述。 / First systematic survey on split learning for LLM fine-tuning. |
| [[2604.24608v1]] RouteHead | 查询依赖的注意力头动态选择用于LLM重排序。 / Query-dependent dynamic attention head selection for LLM re-ranking. |
| [[2604.24703v1]] SpecValidator | 轻量级分类器检测LLM代码生成中的任务描述缺陷，F1=0.804。 / Lightweight classifier for defective task descriptions in LLM code generation; F1=0.804. |

### 硬件部署与边缘AI / Hardware Deployment & Edge AI

| Paper | 一句话描述 / One-line Description |
|-------|----------------------------------|
| [[2604.24455v1]] YOLO-NAS on VTA | FPGA张量加速器上YOLO-NAS全自动编译与仿真执行。 / Full automated compilation and simulation of YOLO-NAS on FPGA VTA. |
| [[2604.24492v1]] Deployment-Aligned NAS | 搜索阶段引入FP16约束的硬件感知NAS，恢复三分之二精度损失。 / Deployment-aligned NAS with FP16 constraints in search; recovers 2/3 of precision loss. |
| [[2604.24287v1]] RVC | 以受害行为中心的RowHammer检测，减少95-99.99%冗余刷新。 / Victim-centric RowHammer detection; 95-99.99% redundant refresh reduction. |
| [[2604.24649v1]] Deja Vu Packing | FPGA打包模式记忆化，平均3.7-6.9倍加速且不改变结果质量。 / FPGA packing pattern memoization; 3.7-6.9x speedup with zero quality change. |
| [[2604.24636v1]] On-Device SLM | 端侧小模型集成的五类故障模式与八条设计启发式规则。 / Five failure categories and eight design heuristics for on-device SLM integration. |

### 持续学习与知识保留 / Continual Learning & Knowledge Retention

| Paper | 一句话描述 / One-line Description |
|-------|----------------------------------|
| [[2604.24637v1]] FTN | 皮层启发的参数隔离持续学习，无监督任务检测，近乎零遗忘。 / Cortex-inspired parameter-isolation continual learning with unsupervised task detection; near-zero forgetting. |

### 量子计算 / Quantum Computing

| Paper | 一句话描述 / One-line Description |
|-------|----------------------------------|
| [[2604.24551v1]] GSC-QEMit | 遥测驱动的自适应量子错误缓解，+9%保真度，减少35%高强度干预。 / Telemetry-driven adaptive quantum error mitigation; +9% fidelity, 35% less heavy intervention. |

### 人机交互 / Human-Computer Interaction

| Paper | 一句话描述 / One-line Description |
|-------|----------------------------------|
| [[2604.24461v1]] PCS & TPS | 人机协作感知合作性量表(PCS)和团队感知量表(TPS)的开发与验证。 / Development and validation of Perceived Cooperativity Scale and Teaming Perception Scale. |

---

## All Papers

| # | arXiv ID | Short Title | 中文摘要 | English TL;DR |
|---|----------|-------------|----------|---------------|
| 1 | [[2604.24154v1]] | LPA Progressive Approximation | 残差网络渐进逼近理论与"训练一次、部署N个模型"的深度自适应推理。 | Progressive approximation in residual networks; "train once, deploy N models." |
| 2 | [[2604.24162v1]] | TIGS Backdoor Defense | 即插即用推理时后门防御，注意力坍塌检测与双尺度平滑。 | Plug-and-play inference-time backdoor defense via attention collapse detection. |
| 3 | [[2604.24170v1]] | CREDENCE Uncertainty CBM | 概念瓶颈模型中的认知-偶然不确定性分解与四象限决策路由。 | Epistemic-aleatoric uncertainty decomposition in CBMs with decision routing. |
| 4 | [[2604.24178v1]] | Meal Multi-Objective Alignment | 双层元学习多目标LLM对齐，动态偏好权重优于静态方法。 | Bi-level meta-learning for multi-objective LLM alignment. |
| 5 | [[2604.24196v1]] | Companion-Elliptic Kernels | 生成漂移的可辨识性与稳定性理论，分类为高斯+Matern核。 | Identifiability and stability for generative drifting; Gaussian+Matern classification. |
| 6 | [[2604.24238v1]] | GeoEdit Diffusion Editing | 流形切空间估计实现免Jacobian、免训练扩散模型编辑。 | Jacobian-free tangent space estimation for training-free diffusion editing. |
| 7 | [[2604.24273v1]] | BitRL 1-bit RL Edge | 1-bit量化LLM+RL在树莓派4上的实时控制与24.8ms延迟。 | 1-bit quantized LLM + RL on Raspberry Pi 4; 24.8ms latency. |
| 8 | [[2604.24278v1]] | RAS ASR Reliability | ASR弃权感知框架，片段级占位符+RAS指标+GRPO训练。 | ASR abstention-aware framework with RAS metric and GRPO training. |
| 9 | [[2604.24287v1]] | RVC RowHammer Detection | 以受害行为中心的RowHammer检测，减少95-99.99%冗余刷新。 | Victim-centric RowHammer detection; 95-99.99% redundant refresh reduction. |
| 10 | [[2604.24302v1]] | DFA Circuit Transfer | 可微忠实度对齐实现跨模型电路迁移。 | Differentiable faithfulness alignment for cross-model circuit transfer. |
| 11 | [[2604.24313v1]] | SAL Self-Abstraction | 自抽象层级式训练，缓解梯度消失，医学影像AUC提升16-18%。 | Self-abstraction hierarchical training; 16-18% AUC gain on medical imaging. |
| 12 | [[2604.24332v1]] | DDG Fast AT | 快速对抗训练分布感知动态引导，单步超越多步方法。 | Distribution-aware dynamic guidance for fast AT; single-step beats multi-step. |
| 13 | [[2604.24348v1]] | OS-SPEAR Agent Eval | OS Agent四维评估工具包，22模型评测揭示效率-安全权衡。 | Four-dimensional OS agent evaluation; 22 models; efficiency-safety trade-off. |
| 14 | [[2604.24350v1]] | CO as Backdoor | 从后门视角重新解释快速对抗训练中的灾难性过拟合。 | Reinterprets catastrophic overfitting as backdoor-like trigger overfitting. |
| 15 | [[2604.24356v1]] | Primitive Recursion Dynamics | 原始递归函数五种动力学等价刻画，组合从动力学涌现。 | Five-way dynamical equivalence for primitive recursion. |
| 16 | [[2604.24357v1]] | DPRM Token Ordering | Doob h变换过程奖励引导扩散语言模型token排序。 | Doob h-transform process-reward-guided token ordering for diffusion LMs. |
| 17 | [[2604.24374v1]] | MIPIC Matryoshka | Matryoshka表示学习双轴自蒸馏，极端低维截断下优势明显。 | Dual-axis self-distillation for Matryoshka; strong at extreme low dimensions. |
| 18 | [[2604.24379v1]] | Super-DeepG Certification | GPU友好几何鲁棒性认证，526倍加速，首次TinyImageNet。 | GPU-friendly geometric certification; 526x speedup; first on TinyImageNet. |
| 19 | [[2604.24380v1]] | VLM Structural Pruning | LVLM结构化剪枝系统研究，宽度>层剪枝，30%安全阈值。 | Systematic LVLM pruning study; widthwise > layerwise; 30% safe. |
| 20 | [[2604.24393v1]] | Linear Regions SSL | SSL线性区域几何分析，SSL用更少区域达相当准确率。 | Linear region geometry of SSL; fewer regions, comparable accuracy. |
| 21 | [[2604.24401v1]] | Audio-Language Eval | 音频-语言基准60-72%分数无需音频，揭示文本捷径问题。 | 60-72% audio-language scores without audio; reveals text shortcut problem. |
| 22 | [[2604.24432v1]] | KSA Summary Attention | 摘要token序列压缩，KV缓存降至0.22%，RULER-128K +16.6pts。 | Summary-token compression; KV 0.22%; RULER-128K +16.6pts. |
| 23 | [[2604.24455v1]] | YOLO-NAS on VTA | FPGA VTA上YOLO-NAS全自动编译与位精确仿真。 | Full automated YOLO-NAS compilation on FPGA VTA; bit-accurate simulation. |
| 24 | [[2604.24461v1]] | PCS & TPS Scales | 人机协作感知合作性与团队感知量表开发验证(N=409)。 | PCS and TPS scale development for human-AI cooperation (N=409). |
| 25 | [[2604.24468v1]] | SL-LLM Survey | 首篇分割学习与LLM微调交叉领域系统综述。 | First survey on split learning for LLM fine-tuning. |
| 26 | [[2604.24469v1]] | SSL Retrieval Geometry | SSL嵌入各向异性严重降低ANN检索，线性探针不预测检索效果。 | Anisotropic SSL embeddings degrade ANN retrieval; linear probe unreliable. |
| 27 | [[2604.24492v1]] | Deployment-Aligned NAS | 搜索阶段FP16约束NAS，恢复三分之二精度损失。 | FP16-aware NAS in search phase; recovers 2/3 precision loss. |
| 28 | [[2604.24498v1]] | HyDeS Hyperspherical SSL | 超球面密度 shaping SSL，分割优异但细粒度分类较弱。 | Hyperspherical density shaping SSL; strong segmentation, weak fine-grained. |
| 29 | [[2604.24512v1]] | SSRP Attention Latch | 注意力锁定失败模式形式化，Architect-Executive分离恢复715倍。 | Formalizes Attention Latch; Architect-Executive separation yields 715x lift. |
| 30 | [[2604.24517v1]] | Prior-Agnostic Forecast | 状态空间未知鲁棒预测聚合，log-odds聚合器近优。 | Robust forecast aggregation with unknown state; log-odds aggregator near-optimal. |
| 31 | [[2604.24542v1]] | LCF Runtime Detection | 层间状态差值统计检测，<0.1%开销统一检测后门/越狱/注入。 | Statistical detection on inter-layer diffs; <0.1% overhead; unified threat detection. |
| 32 | [[2604.24545v1]] | Extreme Bandits | 半参数极端bandit，有限时间遗憾界渐近可忽略。 | Semi-parametric extreme bandits with finite-time regret bounds. |
| 33 | [[2604.24551v1]] | GSC-QEMit Quantum | 遥测驱动自适应量子错误缓解，+9%保真度。 | Telemetry-driven adaptive quantum error mitigation; +9% fidelity. |
| 34 | [[2604.24608v1]] | RouteHead Re-ranking | 查询依赖注意力头动态选择LLM重排序。 | Query-dependent dynamic head selection for LLM re-ranking. |
| 35 | [[2604.24618v1]] | Sabotage Eval Safety | 评估前沿模型破坏安全研究倾向，Mythos Preview 7%持续破坏。 | Evaluates sabotage propensity; Mythos Preview continues sabotage at 7%. |
| 36 | [[2604.24636v1]] | On-Device SLM | 端侧SLM集成五类故障与八条设计规则，"做得越少越可靠"。 | Five failure categories; eight heuristics; "LLM does least = most reliable." |
| 37 | [[2604.24637v1]] | FTN Continual Learning | 皮层启发参数隔离持续学习，无监督任务检测，近乎零遗忘。 | Cortex-inspired parameter-isolation CL; unsupervised task detection; FM<0.02. |
| 38 | [[2604.24647v1]] | DepthKV Cache Pruning | 逐层非均匀KV缓存剪枝，InfoNCE引导预算分配。 / Layer-dependent KV cache pruning; InfoNCE-guided budget allocation. |
| 39 | [[2604.24649v1]] | Deja Vu FPGA Packing | FPGA打包模式记忆化，3.7-6.9倍加速零质量损失。 / FPGA packing memoization; 3.7-6.9x speedup, zero quality loss. |
| 40 | [[2604.24668v1]] | Sycophancy in Finance | 个性化偏好注入引发LLM金融任务严重谄媚。 / Personalized preferences trigger severe financial sycophancy. |
| 41 | [[2604.24672v1]] | Functorial DL Theory | 预层/余预层范畴论统一CNN/MPNN/RNN，解释对抗脆弱性。 / Presheaf/copresheaf framework unifying architectures; explains adversarial vulnerability. |
| 42 | [[2604.24686v1]] | RiskGate Agent Governance | 可行性理论运行时自主代理治理框架。 / Viability-theory-based runtime governance for autonomous agents. |
| 43 | [[2604.24693v1]] | CLAS Activation Steering | 上下文自适应激活引导，感知向量动态调节引导强度。 / Context-dependent activation steering via learned sensing vectors. |
| 44 | [[2604.24698v1]] | Persona Collapse | LLM人格模拟结构坍缩，高保真反而产生刻板种群。 / Structural persona collapse; high fidelity yields stereotyped populations. |
| 45 | [[2604.24703v1]] | SpecValidator Code | 轻量分类器检测代码生成任务描述缺陷，F1=0.804。 / Lightweight defective prompt classifier for code generation; F1=0.804. |
| 46 | [[2604.24708v1]] | HDET Ensemble Training | DDP副本学习率自动探索，零额外硬件开销，9倍LR稳定训练。 / DDP replica LR exploration; zero extra hardware; 9x stable LR training. |
| 47 | [[2604.24715v1]] | HyLo Hybrid Upcycling | 预训练Transformer回收为MLA+Mamba2混合架构，支持2M token。 / Upcycles Transformers to MLA+Mamba2 hybrid; 2M-token serving. |
| 48 | [[2604.24717v1]] | SIREN-RoPE | RoPE扩展为可学习时间信号空间，自主发现日/周周期。 / RoPE as learnable temporal signal space; auto-discovers daily/weekly cycles. |
| 49 | [[2604.24737v1]] | Multiple Thinkers CoT | 多思考者CoT学习复杂度分析，被动困难主动Boosting高效。 / Multi-thinker CoT complexity; passive hard, active boosting efficient. |
| 50 | [[2604.24745v1]] | HRGrad Kinetic Gradient | 流形等距旋转解决多尺度动理学方程多任务梯度冲突。 / Manifold isometric rotation for multiscale kinetic gradient conflicts. |
| 51 | [[2604.24749v1]] | Optimal Multiclass Sample | 解决2014猜想，确定多类学习最优样本复杂度。 / Resolves 2014 conjecture; optimal multiclass sample complexity. |
