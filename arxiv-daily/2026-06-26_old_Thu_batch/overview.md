---
title: "Daily arXiv Digest — 2026-06-26"
date: 2026-06-26
tags:
  - mechanistic-interpretability
  - llm-efficiency
  - quantization
  - training-optimization
  - reasoning-evaluation
  - agents
  - theory
  - safety
papers: 46
---

# Daily arXiv Digest — 2026-06-26

> 本日精选 46 篇论文，覆盖机制可解释性、大模型效率与量化、训练优化、推理与评测、智能体与自演化、理论与基础、安全与可靠性七大主题。
> A curated digest of 46 papers spanning mechanistic interpretability, LLM efficiency/quantization, training optimization, reasoning & evaluation, agents & self-evolution, theory & foundations, and safety & reliability.

---

## 今日必读 / Must Read Today

### [[2606.26650]] CAT-Q: 训练免费的三值量化，1.58-bit 部署千亿模型

> 推荐理由（中）：CAT-Q 仅用 512 个校准样本（约 1M tokens）就把 1.7B–235B 的预训练 LLM 量化成 1.58-bit 三值模型，性能超越用 100B tokens 训练的 BitNet，训练 token 减少约 10 万倍——这是当前最具实用价值的 PTQ 极低比特方案，直接决定百亿/千亿模型能否在消费级与边缘硬件上落地。
>
> Why read (EN): CAT-Q turns ternary (1.58-bit) post-training quantization from a curiosity into a deployable reality, beating QAT-trained BitNet baselines with ~100,000x fewer tokens and quantizing a 235B model in 60 GPU-hours — a step change for edge/consumer deployment of frontier-scale LLMs.

### [[2606.26705]] 深度学习的算法复杂度基础：通用逼近与电路编译定理

> 推荐理由（中）：这篇纯理论奠基性工作以 o-极小可定义性与电路复杂度严格刻画了神经网络的通用逼近能力，并给出"电路编译为神经网络"的量化定理，在最短路径问题上实现了 1/ε 上的指数改进——它为表示几何、可解释性与逼近论提供了一条统一的"算法复杂度"主线。
>
> Why read (EN): A foundational theory paper recasting neural expressivity around algorithmic (circuit) complexity rather than smoothness alone — proving a universal-approximation characterization and a circuit-to-ANN compilation theorem with an exponential-in-1/ε improvement on all-pairs shortest paths. A unifying backbone for representation geometry and approximation theory.

### [[2606.27288]] 多模型编排的上限：共失败率 β 而非错误相关性 ρ

> 推荐理由（中）：本文证明任何 LLM 选择策略（路由/投票/级联/MoA）的准确率上限是 1−β（所有模型同时答错的比例），而业界惯用的成对错误相关性 ρ 在数学上无法识别 β；在 67 个前沿模型上实测发现 ρ 系统性低估共失败尾部约 2.5 倍。它为"组合模型到底能不能超过单最佳模型"给出了零成本的部署前判据。
>
> Why read (EN): Proves the accuracy ceiling of any LLM orchestration is 1−β (the all-models-wrong rate), not pairwise error correlation ρ — and shows ρ underestimates the co-failure tail ~2.5x across 67 frontier models. Converts β into a $0 pre-deployment Clopper–Pearson certificate that reframes when ensembling is worth it at all.

---

## 按主题分类 / Papers by Topic

### 机制可解释性 / Mechanistic Interpretability

| 论文 / Paper | 一句话总结 / One-line summary | 相关性 / Relevance |
|---|---|---|
| [[2606.26474]] RL 工具调用定位到单特征 | 用 Dedicated Feature Crosscoders 把 Qwen2.5-3B 经 ToolRL 后的工具调用能力定位到单个神经元，免重训转向即提升 65pp；RL 能力会"溢出"到冻结基线模型。/ Localizes ToolRL-induced tool use in a Qwen2.5-3B to a single crosscoder neuron (+65pp via retraining-free steering); capability partially spills into the frozen base. | RL×可解释性安全方向首个系统性证据，为运行时监控与可控转向提供方法论。/ First systematic evidence for runtime monitoring and steering of RL-induced agentic capability. |
| [[2606.26620]] Qwen3-Instruct SAE 套件 | 阿里发布覆盖 Qwen3-1.7B/4B/8B 全层的 JumpReLU SAE，并用单特征将模型引导至拒绝行为。/ Alibaba releases full-layer JumpReLU SAEs for Qwen3-Instruct (1.7B/4B/8B), causally steering refusal via a single feature. | 开箱即用的可解释性基础设施与拒绝行为干预参考。/ Ready-to-use interpretability infrastructure for steering/refusal work. |
| [[2606.26629]] SAE 特征正则化的 LLM 持续学习 | 用预训练 SAE 特征空间作为单义保护坐标替代失效的权重正则化，在 TRACE/MedCL 上成最强非架构方法。/ Uses pretrained SAE features as concept-separable protection coordinates, becoming the strongest non-architectural continual-learning method on TRACE/MedCL. | 把可解释性工具从分析推进到训练时正则化，无回放持续微调新范式。/ Pushes interpretability tools from analysis to training-time regularization. |
| [[2606.27321]] Top-k SAE 稀疏正则化 | 在 Top-k SAE 选择前的预选激活上加 off-support ℓ1 与 ℓ1/ℓ2 比率正则，无重建代价地提升单义性。/ Off-support ℓ1 + scale-invariant ℓ1/ℓ2-ratio regularizers on pre-selection activations improve Top-k SAE monosemanticity at no reconstruction cost. | 直接改进主流 Top-k SAE，轻量即插即用，附带推理时 k 鲁棒性结论。/ Lightweight, plug-and-play improvement to the mainstream Top-k SAE. |
| [[2606.26523]] 激进 AI 可解释性（书） | 将哲学"激进解释"传统与可解释性工具结合，给出何时可对 AI 归因信念/欲望的可检验判据。/ Unites radical-interpretation philosophy with mech-interp tooling to give testable criteria for attributing beliefs/desires to AI. | 为"何时相信模型内部信念"提供哲学严格判据，指出命题投射隐患。/ Principled criteria for trusting internal beliefs, flags the propositional projection problem. |
| [[2606.26987]] 开源模型的情绪向量 | 在 Apertus-8B/Gemma-4-E4B 上复现 Anthropic 情绪向量，效价几何可提取但层级轨迹因模型而异。/ Replicates emotion vectors in open LLMs; valence geometry recovers but layer trajectories differ, arousal is corpus-dependent. | 验证情绪向量可迁移性，为对齐安全监控提供开源可复现基础方法。/ Validates emotion-vector transferability for alignment monitoring. |
| [[2606.27237]] LM 作为任务专属知识库 | 证明 LM 不以任务无关方式存储事实，同一事实在不同任务格式下依赖不同参数子集。/ Shows LMs store facts in task-specific parameter subsets, not a task-invariant KB; CoT routes through alternative encodings. | 机制层面回答"LM 即知识库"，对知识编辑/遗忘/CoT 机制研究有直接指导。/ Mechanistic answer to "LM-as-KB" guiding editing/unlearning/CoT. |
| [[2606.27091]] 继承电路与规避漏洞 | 安全微调继承并强化 Llama Layer-12 注意力回路，引入别名/重构/大小写突变等规避漏洞。/ Security fine-tuning inherits a Layer-12 attention circuit, creating transformation-sensitive evasion failures invisible to standard eval. | 网络安全 LLM 安全微调的部署前监控范式，把电路分析引入该领域。/ Pre-deployment monitoring paradigm bringing circuit analysis to security LLMs. |
| [[2606.26982]] 框架敏感性行为不稳定审计 | 受控匹配提示揭示心理健康对话中 LLM 行为随语境框架系统性偏移，信号可被探针解码与激活引导干预。/ Audits framing-sensitive behavioral instability in mental-health dialogue; signal decodable in hidden states, partially steerable. | 可信 AI 行为校准完整审计范式，可作一致性评测体系参考。/ Complete audit paradigm for trustworthy-AI behavioral calibration. |

### 大模型效率与量化 / LLM Efficiency & Quantization

| 论文 / Paper | 一句话总结 / One-line summary | 相关性 / Relevance |
|---|---|---|
| [[2606.26650]] CAT-Q 三值量化 | 512 样本即可将 1.7B–235B LLM 量化为 1.58-bit 三值，超越用 100B tokens 训练的 BitNet，训练 token 减少约 10 万倍。/ PTQ ternary quantization beating QAT BitNet with ~100k fewer tokens, 235B in 60 GPU-hours. | 1.58-bit 部署最具实用价值 PTQ 方案，直接关系边缘硬件部署。/ Most practical PTQ scheme for 1.58-bit edge deployment. |
| [[2606.26587]] SharQ 稀疏×FP4 | 无需训练的在线稀疏-稠密分解，把激活离群值路由到 N:M 稀疏 FP4，RTX 5090 上延迟降 2.2–2.4×，恢复 43–63% 精度损失。/ Training-free sparse–dense decomposition fusing N:M sparsity with FP4, 2.2–2.4× latency cut, recovers 43–63% of the NVFP4 gap. | 低比特大模型推理加速工程范例，适配 vLLM/Blackwell 部署。/ Engineering template for low-bit inference on Blackwell/vLLM. |
| [[2606.26488]] 递归推理模型边缘压缩 | 激进量化摧毁递归推理模型的全局推理（局部存活、全局崩塌），用每通道 INT4 + 无标签 carry-trajectory 诊断修复。/ Aggressive quantization breaks global reasoning in recursive reasoners (local survives, global collapses); fixed via per-channel INT4 + label-free carry-trajectory diagnostic. | 揭示低比特量化与深度循环架构耦合失效模式，轻量推理模型设计参考。/ Reveals low-bit×recurrent coupling failures for edge reasoner design. |
| [[2606.26822]] 联邦学习量化综述 | 首个专门聚焦联邦学习量化的系统综述（PRISMA），提出 FL 中心化量化分类法与六大系统级维度。/ First PRISMA survey dedicated to quantization in Federated Learning, with an FL-centric taxonomy and six system-level dimensions. | 边缘/IoT/隐私分布式学习的量化选型指南与路线图。/ Selection guide and roadmap for quantized FL on edge/IoT. |
| [[2606.26744]] HyperDFlash MHC 投机解码 | 针对 DeepSeek-V4 多超连接架构，三项 MHC 对齐设计把投机解码接受长度从 2.93 提升到 3.69。/ Three MHC-aligned designs boost block speculative decoding for DeepSeek-V4, draft acceptance 2.93→3.69, speedup 2.25×→2.80×. | DeepSeek-V4 系列 MHC 架构推理加速的直接工程价值。/ Direct engineering value for DeepSeek-V4 MHC inference acceleration. |
| [[2606.26875]] InfoKV 长推理 KV 压缩 | 从"向前看"视角用熵信号重排 KV 缓存压缩，高熵 token 主导长程未来影响。/ Forward-looking, entropy-based KV compression; high-entropy tokens dominate long-range future impact. | 长链式推理 KV 膨胀问题，兼具理论洞察与工程实用。/ Long-chain reasoning KV bloat, theory + engineering value. |
| [[2606.26538]] CascadeFormer 梯度扇入不对称 | 用梯度扇入不对称解释深层贡献递减，设计宽度递减架构与梯度剪枝，-8.6% 延迟/+9.4% 吞吐。/ Gradient Fan-in Asymmetry explains deep-layer diminishing returns; width-tapered CascadeFormer + gradient pruning, -8.6% latency / +9.4% throughput. | 高效推理与层冗余分析的新结构化解释与可即插即用方法。/ New structural account and plug-in methods for efficient inference. |
| [[2606.26560]] Erase-then-Delta 注意力 | 在 delta 规则线性注意力中"先擦除、再写入"，独立地址清除过期记忆，提升 dense 2.5B 与 MoE 25B 表现。/ Decouples erase vs write addresses in delta-rule linear attention, targeted cleanup; tops dense 2.5B and MoE 25B baselines. | 下一代高效线性注意力核心组件，delta 规则变体通用插件。/ Core component for next-gen linear attention; universal delta-rule plug-in. |
| [[2606.26493]] Nemotron-TwoTower 扩散语言建模 | NVIDIA 双塔：冻结 AR 上下文塔 + 可训练扩散去噪塔，30B MoE 上保留 98.7% 质量同时吞吐提升 2.42×。/ NVIDIA TwoTower: frozen AR context tower + trainable diffusion denoiser; 98.7% quality at 2.42× throughput on 30B MoE. | 解码加速与扩散式语言建模的工程可行路径，已开源。/ Engineering-ready path for decoding acceleration and diffusion LMs. |

### 训练与优化 / Training & Optimization

| 论文 / Paper | 一句话总结 / One-line summary | 相关性 / Relevance |
|---|---|---|
| [[2606.27153]] DMuon 分布式 Muon | 通过 owner-centric 执行与形状自适应内核，把分布式 Muon 每步开销压到接近 AdamW（仅高约 2%）。/ Distributed Muon brings per-step overhead within ~2% of AdamW via owner-centric execution and shape-adaptive kernels. | 大规模预训练 Muon 落地必需的系统侧基础设施。/ Systems infrastructure needed to deploy Muon at pretraining scale. |
| [[2606.27216]] 层次化 Muon | 把整矩阵 Newton-Schulz 改为每个 T×T tile 独立执行，主要算力显著降低，Qwen3 训练损失接近全矩阵 Muon。/ Tiled Newton-Schulz (per T×T tile) cuts NS work while matching full-matrix Muon loss in Qwen3 training. | 显存/加速器上 Muon 步效率瓶颈的直接实用价值。/ Direct value for Muon step-efficiency under memory/hardware limits. |
| [[2606.26997]] RolloutPipe 流水线 | 分离式 on-policy GRPO 中，prompt group 一完成即送训练并优先调度前沿 group，rollout-to-train 时间缩短 30.7%–42.3%。/ Pipelines rollout and training in disaggregated GRPO, handing off groups as they materialize; 30.7–42.3% time cut, strict on-policy. | GRPO/RLVR 训练系统真实痛点的可落地流水线方案。/ Deployable pipeline for the rollout/training idle-pain in GRPO/RLVR. |
| [[2606.26917]] GeoAlign 几何 rollout 整理 | 发现在线 LLM RL 的"方向不一致"失效，用前向传播的几何偏差评分替换离群 rollout，提升性能与稳定性。/ Forward-pass-only geometric rollout curation fixes directional inconsistency in LLM RL, improving performance and stability. | 极低开销即插即用 RLHF 可靠性信号，可叠加 GRPO/PPO 流水线。/ Near-zero-cost plug-in RLHF reliability signal for GRPO/PPO. |
| [[2606.26671]] NebulaExp-8B 后训练消融 | 基于 Qwen3-8B 的透明消融驱动后训练流水线（SFT→GRPO→OPD），证明数据正确性是一阶因子、教师兼容性胜过规模。/ Transparent ablation-driven Qwen3-8B post-training pipeline; data correctness is first-order, teacher compatibility beats scale; multi-teacher OPD exceeds single-teacher ceiling. | 开源小模型后训练完整可参照配方，8B 规模数据筛选/混合/蒸馏直接借鉴。/ Complete reference recipe for 8B-scale post-training. |
| [[2606.26783]] AlphaEdit 复现研究 | 确认 AlphaEdit 在原始范围内有效，但在新架构、超长编辑规模与安全行为上零空间保护显著失效。/ Reproducibility study: AlphaEdit works in original scope but null-space protection fails on newer architectures, long edit scales, and safety behavior. | 知识编辑/持续学习边界条件，对部署决策与后续方法设计有直接参考。/ Boundary conditions for knowledge editing informing deployment/design. |

### 推理与评测 / Reasoning & Evaluation

| 论文 / Paper | 一句话总结 / One-line summary | 相关性 / Relevance |
|---|---|---|
| [[2606.27288]] 共失败率 β 编排上限 | 多模型编排准确率上限是 1−β 而非 ρ；67 个前沿模型上 ρ 系统性低估共失败尾部约 2.5 倍。/ Orchestration ceiling is 1−β not ρ; ρ underestimates the co-failure tail ~2.5x across 67 frontier models. | 多模型编排/路由/级联的零成本部署前判据。/ Zero-cost pre-deployment certificate for orchestration/routing. |
| [[2606.26836]] Capability Frontier 评测偏差 | 标准单模型评测使错误率高估，去偏可降 54%，叠加多次生成重选可达 82%。/ Standard benchmarks overstate error; debiasing cuts 54%, multi-generation selection reaches 82% (with ideal judge). | LLM 评测方法论、模型选型/路由、推理时算力扩展高度相关。/ Highly relevant for LLM eval methodology, routing, inference-time scaling. |
| [[2606.27359]] 序列概率与正确性 | 跨 prompt-answer 对序列概率能预测正确性，但不能迁移到解码决策层面，同 prompt 多采样几乎不能区分对错。/ Sequence probability predicts correctness across prompt-answer pairs but not decoding decisions; within-sample correlation ~0. | 划定"概率信号可用/不可用"边界，指导解码策略与 verifier-free 自改进。/ Demarcates when probability signals help in decoding/self-improvement. |
| [[2606.26502]] 难度登记 vs 慎思分配 | 大推理模型与人类跨题目"难题更久"一致，但固定题目后策略相反：LRM 答错时生成更长链，人类更快放弃。/ LRMs and humans align cross-item but diverge within-item: LRMs generate more tokens when wrong, humans give up faster. | "LRM 当认知模型比对人类"研究线的可操作诊断工具。/ Actionable diagnostic for the LRM-as-cognitive-model comparison line. |
| [[2606.26935]] CoT 训练增益落在哪 | 长上下文智能体中 CoT 训练增益更多落在"提示词直接预测动作"捷径而非推理式修正。/ In long-context agents, CoT training gains land on direct prompt-to-action shortcuts, not reasoning-mediated revision. | "用 CoT 训练智能体"实践者的直接提醒与零成本干预。/ Direct reminder + zero-cost intervention for CoT-trained agents. |
| [[2606.27047]] NuclearQAv2 核工程基准 | 面向核工程的 ~1239 题 LLM 评测基准，揭示模型定量推理与概念理解短板。/ ~1239-question nuclear-engineering benchmark exposing LLM weakness in quantitative reasoning and conceptual understanding. | 高风险技术领域部署 LLM 与领域 benchmark 方法论借鉴。/ Domain benchmark methodology for high-stakes technical deployment. |
| [[2606.26492]] DL 故障诊断评估差距 | 用 DynFault（5542 轨迹）揭示现有 DL 故障诊断在程序内评估虚高约 0.19 均衡准确率。/ DynFault reveals a 0.190 balanced-accuracy gap between within-program and program-held-out DL fault diagnosis evaluation. | 构建 DL 训练诊断/监控/调试工具的基准与对照实验范式。/ Benchmark + control paradigm for DL training fault-diagnosis tooling. |

### 智能体与自演化 / Agents & Self-Evolution

| 论文 / Paper | 一句话总结 / One-line summary | 相关性 / Relevance |
|---|---|---|
| [[2606.26722]] AHOIS 苏格拉底式 AI 科学家 | 多智能体 AI 科学家在真实多模光纤平台上嵌入苏格拉底式产婆术，自主提出假说并诊断失败模式。/ Multi-agent AI scientist embedding Socratic midwifery on a real multimode-fibre platform; autonomously proposes hypotheses and diagnoses failures. | 自主科学发现/可信 AI for Science 的清晰工程化范式。/ Clear engineering paradigm for autonomous scientific discovery. |
| [[2606.26728]] 科学发现即元优化 | 将科研形式化为同时优化解决方案与评价标准的元优化，用共识聚合把 3-SAT 求解标度从 N²·⁵¹ 降到 N¹·³³。/ Treats discovery as co-optimizing solutions and objectives; consensus aggregation cuts 3-SAT scaling from N²·⁵¹ to N¹·³³ (~67× speedup). | 评价标准难以精确刻画的多目标自动搜索场景参考。/ Reference for multi-objective auto-search with hard-to-specify objectives. |
| [[2606.26669]] SkillDisCo 智能体技能蒸馏 | 将成功轨迹蒸馏为参数化有限状态机子图并编译为可调用技能，在 ALFWorld/WebArena 上提升成功率与效率。/ Distills agent traces into parameterized FSM subgraphs compiled to callable, verified skills; improves ALFWorld/WebArena success and efficiency. | 长期积累可复用技能库与"强模型诱导、弱模型执行"跨模型迁移范式。/ Reusable skill libraries and strong-to-weak transfer paradigm. |
| [[2606.26806]] 记忆深度 vs 记忆访问 | 区分检索访问与"惊讶度×价值度"门控的稀疏 LoRA 固化，loop-drift 协议中现"深度翻转"现象。/ Distinguishes memory access from surprise×valence-gated LoRA consolidation; "depth flip" — RAG wins shallow recall, EVAF wins goal persistence. | 长期运行 Agent 记忆设计精确靶点，持续学习型助手记忆架构启发。/ Precise target for long-running-agent memory architecture. |
| [[2606.27154]] OpenRCA 2.0 过程级因果监督 | PAVE 协议从结果标签转向过程级因果监督，首个带逐步因果路径标注的跨系统 RCA 基准。/ PAVE converts outcome labels to process-level causal supervision; first cross-system RCA benchmark with step-wise causal-path labels. | "大模型能否可靠诊断故障"更严格评测范式，过程奖励模型方向指引。/ Stricter eval paradigm for LLM fault diagnosis, PRM direction. |
| [[2606.27376]] 统一多模态自演化（无标注） | Proposer-Solver-Generator 三 LoRA 角色仅用无标注图像同时提升统一多模态模型理解与生成。/ Three-LoRA (Proposer/Solver/Generator) unsupervised self-evolution improves unified LMM understanding + generation across diffusion/flow/AR backbones. | 统一多模态模型无监督后训练直接方法论，降低人工标注依赖。/ Direct methodology for unsupervised unified-LMM post-training. |
| [[2606.27373]] VISE 多模态自演化视觉关注 | 解决自演化 LMM 的"视觉欠条件化"，仅用两张不变性奖励在无标注图像上单模型自演化。/ Fixes "visual under-conditioning" in self-evolving LMMs via two self-supervised invariance rewards on unlabeled images. | 多模态视觉对齐与无标注自演化训练范式参考。/ Reference for multimodal visual alignment and unsupervised self-evolution. |
| [[2606.27326]] 世界模型幻觉可预测可预防 | 把生成式世界模型幻觉重定义为数据覆盖问题，三个无标签信号预测三种幻觉模式，50 条轨迹即适配新环境。/ Reframes world-model hallucination as data coverage; three label-free signals predict three hallucination modes; adapt with 50 trajectories. | 世界模型/具身智能幻觉检测与数据采集策略借鉴。/ Hallucination detection and data-collection strategy for world models. |

### 理论与基础 / Theory & Foundations

| 论文 / Paper | 一句话总结 / One-line summary | 相关性 / Relevance |
|---|---|---|
| [[2606.26705]] 深度学习算法复杂度基础 | 以 o-极小可定义性与电路复杂度刻画通用逼近，电路编译定理在最短路径问题上 1/ε 指数改进。/ Recasts expressivity via circuit complexity; universal-approximation characterization + circuit-to-ANN compilation theorem, exponential-in-1/ε improvement on shortest paths. | ML 数学基础奠基性工作，表示几何/可解释性/逼近论统一主线。/ Foundational work unifying representation geometry/interp/approximation. |
| [[2606.26749]] 坍缩前的瞬时语义几何 | one-hot 监督下 Transformer 训练早期自发形成语义几何，随容量/时间最终坍缩为 Neural Collapse 的 ETF 几何。/ Semantic geometry emerges early as a transient phase under one-hot supervision, then collapses to the label-driven ETF geometry. | 表征几何与训练动力学研究，早停/探针时机/语义涌现参考。/ Reference for representation geometry, training dynamics, probe timing. |
| [[2606.26621]] λ-PSD 可扩展 Stein 差异 | 揭示多项式 Stein 差异在高阶下信噪比指数衰减，提出基于 Rayleigh 商优化的重加权方案。/ Reveals polynomial Stein discrepancy SNR decay; proposes λ-PSD reweighting via Rayleigh quotient optimization at linear-time cost. | 贝叶斯计算诊断/MCMC 收敛检验/样本质量评估直接方法学价值。/ Direct methodological value for Bayesian diagnostics/MCMC/sample quality. |
| [[2606.27242]] 更新几何与 Fisher 对齐 | 证明表征相似度指标在"激活暗"区域不可识别，给出 16KB 流式 FisherSketch 用于免训练源数据选择。/ Proves representation-only metrics are non-identifiable in activation-dark regimes; FisherSketch gives 16KB streaming signatures for training-free source selection. | 大模型迁移学习/LoRA 源数据选择/科学序列 LLM 适配有理论支撑。/ Theoretically grounded signal for transfer/LoRA source selection. |
| [[2606.26839]] 有序神经坍缩导航先验 | 将导航动作"序"结构作为视觉编码器表征先验，有序神经坍缩预训练后接 NoMaD 扩散策略。/ Uses ordinal geometry of steering directions as a representation prior; ORION pretrains encoder then fine-tunes NoMaD diffusion policy (+26pp success). | 表征学习/神经坍缩理论与机器人导航实践交叉点参考。/ Intersection of representation learning/neural-collapse theory and robot navigation. |

### 安全与可靠性 / Safety & Reliability

| 论文 / Paper | 一句话总结 / One-line summary | 相关性 / Relevance |
|---|---|---|
| [[2606.26529]] 非注意间隙 | 任务条件化使语言/视觉模型系统性抑制其本可报告的安全关键信号，规模不改善，GPT-5 中仍存在。/ Task conditioning suppresses safety-critical signals models can otherwise report; not fixed by scale, persists in GPT-5. | 医疗影像/自动驾驶感知与安全评测设计的直接警示。/ Direct warning for medical/vision-AI safety evaluation design. |
| [[2606.26686]] LeanGuard 护栏不需推理 | 严格同主干对照证明 CoT 不提升内容审核准确率，395M 判别编码器匹配 1.24B 推理护栏且成本降低约 100 倍。/ Controlled ablation: CoT doesn't improve moderation accuracy; 395M LeanGuard matches 1.24B reasoning guard at ~100x lower cost. | "推理护栏"热潮的重要纠偏证据，同主干消融应成默认基线。/ Important corrective for the reasoning-guardrail trend; same-backbone ablation as default baseline. |

---

## All Papers

| arxiv_id | title | tags |
|---|---|---|
| [[2606.26474]] | Localizing RL-Induced Tool Use to a Single Crosscoder Feature | mechanistic-interpretability, crosscoder, RL-fine-tuning, tool-use, activation-steering |
| [[2606.26488]] | What Survives When You Compress a Recursive Reasoner for the Edge? | recursive-reasoning, model-compression, edge-deployment, quantization, tiny-models |
| [[2606.26492]] | Evaluation-Strategy Gap in Fault Diagnosis of Deep Learning Programs | deep-learning, fault-diagnosis, software-engineering, generalization, evaluation-methodology |
| [[2606.26493]] | Nemotron-TwoTower: Diffusion Language Modeling with Pretrained Autoregressive Context | diffusion-language-model, masked-diffusion, large-language-model, mixture-of-experts, mamba |
| [[2606.26502]] | Humans Disengage, Reasoning Models Persist | large-reasoning-models, deliberation, chain-of-thought, metacognition, human-model-comparison |
| [[2606.26523]] | Radical AI Interpretability | AI-interpretability, philosophy-of-mind, radical-interpretation, LLM-agency, AI-safety |
| [[2606.26529]] | The Inattentional Gap | ai-safety, inattentional-blindness, llm-evaluation, vision-language-models, radiology-ai |
| [[2606.26538]] | CascadeFormer | transformer-architecture, model-efficiency, layer-pruning, gradient-analysis, residual-networks |
| [[2606.26560]] | Erase-then-Delta Attention | linear-attention, delta-rule, recurrent-memory, efficient-LLM, hybrid-architecture |
| [[2606.26587]] | SharQ: Bridging Activation Sparsity and FP4 Quantization | LLM-inference, FP4-quantization, activation-sparsity, model-serving, training-free |
| [[2606.26620]] | Discovering Millions of Interpretable Features with SAEs | mechanistic-interpretability, sparse-autoencoders, qwen3, refusal-steering, llm-interpretability |
| [[2606.26621]] | λ-PSD: Scalable Approximate SNR-Optimised Polynomial Stein Discrepancies | stein-discrepancy, goodness-of-fit-testing, signal-to-noise-ratio, scalable-statistics |
| [[2606.26629]] | SAE-Guided Activation Regularization for LLM Continual Learning | continual-learning, sparse-autoencoder, LLM-fine-tuning, catastrophic-forgetting, mechanistic-interpretability |
| [[2606.26650]] | CAT-Q: Cost-efficient and Accurate Ternary Quantization | LLM-quantization, ternary-quantization, post-training-quantization, 1.58-bit, model-compression |
| [[2606.26669]] | SkillDisCo: Distilling and Compiling Agent Traces into Skills | llm-agents, skill-discovery, procedural-knowledge, finite-state-machine, experience-reuse |
| [[2606.26671]] | NebulaExp-8B: Empirical Post-Training Pipeline | post-training, SFT, reinforcement-learning, knowledge-distillation, data-curation |
| [[2606.26686]] | LeanGuard: A Fast and Light Approach for Robust Moderation | llm-safety, guardrails, chain-of-thought, efficient-inference, content-moderation |
| [[2606.26705]] | Algorithmic Foundations of Deep Learning | neural-network-approximation-theory, circuit-complexity, universal-approximation, o-minimal-definability |
| [[2606.26722]] | Socratic agents for autonomous scientific discovery | autonomous-scientific-discovery, multi-agent-systems, socratic-reasoning, ai-for-science |
| [[2606.26728]] | Scientific discovery as meta-optimization | llm-agents, scientific-discovery, combinatorial-optimization, sat-solvers, meta-optimization |
| [[2606.26744]] | HyperDFlash: MHC-Aligned Block Speculative Decoding | speculative-decoding, LLM-inference, DeepSeek-V4, multi-hyper-connection, distillation |
| [[2606.26749]] | Structure Before Collapse: Transient semantic geometry | neural-collapse, representation-geometry, next-token-prediction, language-model-training-dynamics |
| [[2606.26783]] | Reproducibility Study of AlphaEdit | model-editing, reproducibility, null-space-projection, knowledge-editing, catastrophic-forgetting |
| [[2606.26806]] | Selective Parametric Consolidation for Long-Running Agents | long-running-agents, parametric-memory, continual-learning, lora, agent-memory |
| [[2606.26822]] | Quantization in Federated Learning: Methods, Challenges | federated_learning, quantization, systematic_review, communication_efficiency, edge_intelligence |
| [[2606.26836]] | The Capability Frontier: Benchmarks Miss 82% of Performance | llm-evaluation, llm-routing, benchmarking, inference-time-scaling, oracle-bias |
| [[2606.26839]] | Ordinal Neural Collapse as a Representation Prior for Navigation | visual-navigation, neural-collapse, representation-learning, imitation-learning, diffusion-policy |
| [[2606.26875]] | Information-Aware KV Cache Compression for Long Reasoning | LLM-efficiency, KV-cache-compression, long-context-reasoning, information-theory, inference-optimization |
| [[2606.26917]] | GEOALIGN: Geometric Rollout Curation for Robust LLM RL | llm-rl, rlhf, grpo, representation-geometry, robustness |
| [[2606.26935]] | Where Do CoT Training Gains Land in LLM based Agents? | chain-of-thought, LLM-agents, faithfulness, shortcut-learning, training-dynamics |
| [[2606.26982]] | Auditing Framing-Sensitive Behavioral Instability in LLMs | LLM, mechanistic-interpretability, mental-health-AI, activation-steering, behavioral-calibration |
| [[2606.26987]] | Where Do Models Find Happiness? Emotion Vectors | mechanistic_interpretability, emotion_vectors, linear_representations, LLM_psychology |
| [[2606.26997]] | RolloutPipe: Overlapping Pipelined Rollout and Training | LLM-reinforcement-learning, GRPO, RLVR, pipeline-optimization, disaggregated-systems |
| [[2606.27047]] | NuclearQAv2: Structured Benchmark for Domain-Science Competence | LLM-benchmark, nuclear-engineering, domain-evaluation, quantitative-reasoning, QA-generation |
| [[2606.27091]] | Inherited Circuits, Learned Semantics: Evasion Vulnerabilities | llm-security, mechanistic-interpretability, adversarial-robustness, malware-detection |
| [[2606.27153]] | DMuon: Efficient Distributed Muon Training | distributed-training, optimizer, muon, systems, llm-training |
| [[2606.27154]] | OpenRCA 2.0: From Outcome Labels to Causal Process Supervision | root-cause-analysis, LLM-agents, causal-reasoning, benchmark, process-supervision |
| [[2606.27216]] | Hierarchical Muon: Tiled Newton-Schulz Updates | muon-optimizer, newton-schulz, llm-training, gpu-kernels, matrix-function |
| [[2606.27237]] | LMs as Task-Specific Knowledge Bases | llm_interpretability, mechanistic_interpretability, knowledge_representation, factual_knowledge, chain_of_thought |
| [[2606.27242]] | The Geometry of Updates: Fisher Alignment at Vocabulary Scale | transfer-learning, fisher-information, source-selection, LLM, training-free |
| [[2606.27288]] | Co-Failure Ceiling on Routing, Voting, and Mixture-of-Agents | llm-orchestration, model-routing, ensemble-methods, copula-modeling, co-failure-analysis |
| [[2606.27321]] | Sparsity Regularizers for More Interpretable Top-k SAEs | sparse-autoencoders, interpretability, top-k-sae, vision-foundation-models, sparsity-regularization |
| [[2606.27326]] | Hallucination in World Models is Predictable and Preventable | world-models, hallucination, data-coverage, reinforcement-learning, generative-models |
| [[2606.27359]] | When are likely answers right? Sequence Probability and Correctness | LLM, decoding, sequence-probability, calibration, self-consistency |
| [[2606.27373]] | Paying More Attention to Visual Tokens in Self-Evolving LMMs | self-evolving-LMM, visual-grounding, multimodal-RL, unsupervised-learning, object-hallucination |
| [[2606.27376]] | Ask, Solve, Generate: Self-Evolving Unified Multimodal Model | self-evolving-LMM, unified-understanding-generation, self-consistency-reward, unsupervised-post-training, multimodal |

---

> 本 overview 基于 2026-06-26 目录下 46 篇论文摘要生成。
> This overview was generated from the 46 paper summaries in the 2026-06-26 directory.
