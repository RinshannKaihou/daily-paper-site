---
title: "Daily Overview — 2026-06-02"
date: 2026-06-02
tags: ["daily-overview", "arxiv", "LLM", "agent", "reasoning", "efficiency", "safety"]
papers: 50
---

## 今日必读 / Must Read Today

1. **[[2606.00642]] Hidden Thoughts Are Not Secret: Reasoning Trace Exposure in LLMs**
   - **English:** Introduces REP, a lightweight prompting technique that elicits hidden reasoning traces from LLMs via code-paradigm transfer. The exposed traces achieve 96.7% of oracle internal-trace distillation performance, demonstrating that interface-level trace hiding is insufficient to prevent capability extraction — a direct warning for deployments of o1/o3/Gemini Thinking/Claude Extended Thinking.
   - **中文：** 本文提出 REP 方法，仅通过提示词即可从隐藏推理的大模型中诱导出内部推理痕迹，蒸馏性能达到 oracle 的 96.7%。这直接证明当前业界通过 API 界面隐藏推理链（如 OpenAI o1/o3、Gemini Thinking、Claude Extended Thinking）不足以防止能力被提取，对 LLM 安全部署具有重要警示意义。

2. **[[2606.01462]] An Enigma of Artificial Reason: Investigating the Production-Evaluation Gap in Large Reasoning Models**
   - **English:** Reveals a dramatic production-evaluation gap in frontier reasoning models: while they achieve ≥94.7% accuracy on math problem solving, they collapse to 47.9%–78.6% when evaluating solutions with correct answers but flawed reasoning. The root cause is an "answer confirmation bias" that corrupts both behavior and internal representations, challenging the assumption that stronger reasoning production entails stronger reasoning evaluation.
   - **中文：** 发现前沿大型推理模型存在严重的"生成-评估鸿沟"——解题准确率接近完美（≥94.7%），但在评估"正确答案-错误推理"的解法时骤降至 47.9%–78.6%。根源在于"答案确认偏见"，这挑战了"更强的推理生成能力自动意味着更强的推理评估能力"的假设，对构建可信 AI 评审系统具有直接警示意义。

3. **[[2606.02054]] eMoT: evolving Memory-of-Thought via Symbolic Anchoring and Memory Corrosion**
   - **English:** Proposes a unified neuro-symbolic framework that treats multi-step reasoning as a dynamic, evolving memory repository. On a lightweight Qwen-32B backbone, eMoT achieves 93.4% on GSM8K (vs. 39.5% baseline), 71.5% on GSM-Hard (vs. 15.9% baseline), and 100% on Game of 24 — surpassing GPT-4-based structured reasoning baselines. The demonstration that structured reasoning control can compensate for smaller model size has important implications for efficient LLM deployment.
   - **中文：** 提出将多步推理建模为动态演化记忆库的统一神经-符号框架。在轻量级 Qwen-32B 骨干上，eMoT 在 GSM8K 达到 93.4%（基线 39.5%）、GSM-Hard 达到 71.5%（基线 15.9%）、Game of 24 达到 100% 准确率，超越基于 GPT-4 的结构化推理基线。证明结构化推理控制可弥补模型规模不足，对高效 LLM 部署具有重要意义。

---

## 按主题分类 / Papers by Topic

### Agent Systems & Orchestration / 智能体系统与编排

| Paper | Summary (EN / 中文) |
|-------|---------------------|
| [[2606.00644]] ForeSci | Forward-looking research judgment benchmark with strict temporal controls / 严格时序控制的前瞻性研究决策基准测试，揭示"证据-决策脱钩"现象 |
| [[2606.00765]] FALAT | Dependency-guided search for failure attribution in multi-agent trajectories / 通过依赖关系引导的分层搜索定位多智能体轨迹中的失败来源 |
| [[2606.01351]] Recognize Your Orchestrator | Mean-field entropy dynamics for diagnosing LLM multi-agent orchestrator fragility / 平均场熵动力学框架诊断多智能体编排器脆弱性，发现"推理陷阱" |
| [[2606.01365]] Early Diagnosis of Wasted Computation | Failure-aware observability framework for multi-agent LLM systems / 面向多智能体 LLM 系统的失败感知可观测性框架，实现无效计算轨迹的早期诊断 |
| [[2606.01416]] Self-Healing Orchestrators | Runtime reliability control for tool-augmented LLM systems with 98.8% task success / 工具增强型 LLM 系统的运行时可靠性控制，任务成功率达 98.8% |
| [[2606.01725]] GAIATrace & Vidur-Agent | Token-level trace dataset and simulator for multi-model agentic AI systems / 首个面向复杂多模型智能体系统的 token 级轨迹数据集与模拟器 |
| [[2606.01912]] SMH-Bench | Executable smart-home simulator benchmark with 1,100 tasks across 7 capabilities / 基于可执行智能家居仿真器的 1,100 任务基准，覆盖 7 大能力类别 |
| [[2606.01991]] SafeMCP | Server-side proactive defense for MCP-powered agents via look-ahead reasoning / MCP 服务器侧主动防御插件，通过前瞻推理在 agent 选择工具前过滤危险工具 |
| [[2606.02060]] TELBench & DRIFT | Span-level error-localization benchmark for deep-research agents / 面向深度研究智能体的轨迹级错误定位基准与声明中心审计框架 |
| [[2606.02132]] EAPO | Mitigates tool abuse in agentic RL with ~20% fewer tool calls / 通过难度感知奖励塑造缓解智能体强化学习中的工具滥用，减少约 20% 工具调用 |
| [[2606.02494]] Monitoring Agentic Systems | Monitoring and triage methodology for immature agentic systems achieving 43× review reduction / 面向早期智能体系统的监控与分流方法论，实现 43 倍人工审查量削减 |
| [[2606.02536]] Tracking Behavioral Trajectories | Embedding-space trait vectors for monitoring adapting agents / 基于嵌入空间特质向量的自适应智能体行为轨迹追踪方法 |
| [[2606.02380]] SPADE-Bench | Evaluates spontaneous strategic deception in tool-use agents via plan-action divergence / 通过计划-行动分歧评估工具使用智能体中的自发策略性欺骗行为 |

### Reasoning & Inference Optimization / 推理与推断优化

| Paper | Summary (EN / 中文) |
|-------|---------------------|
| [[2606.00642]] REP | Elicits hidden reasoning traces from LLMs via code-paradigm prompting / 通过代码范式提示诱导 LLM 暴露隐藏推理痕迹，对隐藏推理模型安全部署具警示意义 |
| [[2606.00726]] Latent Reward Steering | Adaptive inference-time framework promoting cognitive behaviors via SAE latent optimization / 通过 SAE 隐状态奖励梯度优化自适应促进认知行为的推理时框架 |
| [[2606.00920]] Accuracy & Stability | Exposes up to 17.8 pp gap between single-run pass rate and perfect stability on code tasks / 揭示确定性编程任务中单次通过率与完美稳定率之间高达 17.8 个百分点的差距 |
| [[2606.01019]] HVD | Hybrid verified decoding with dynamic draft selection achieving 2.73× speedup on agentic workflows / 混合验证解码，在 agentic 工作流上平均达到 2.73 倍加速 |
| [[2606.01202]] The Shape of Wisdom | Decision trajectory analysis showing 42.1% of correct answers are unstable-correct / 决策轨迹分析揭示 42.1% 的正确答案属于"不稳定但正确"状态 |
| [[2606.01462]] Production-Evaluation Gap | LRMs fail to evaluate flawed reasoning when answers are correct due to confirmation bias / 大型推理模型因答案确认偏见而无法可靠评估正确答案中的推理缺陷 |
| [[2606.02011]] Extreme Low-Bit Inference | Diagnoses 2-bit quantization pathologies in reasoning models and proposes FP16 planning + loop rescue / 诊断推理模型 2-bit 量化的轨迹病理，提出 FP16 规划与循环救援策略 |
| [[2606.02054]] eMoT | Evolving memory-of-thought with symbolic anchoring achieving near-GPT-4 reasoning on Qwen-32B / 演化记忆推理框架结合符号锚定，在 Qwen-32B 上实现接近 GPT-4 的推理性能 |
| [[2606.02332]] SISA | Score-level SSM-attention fusion with perfect NIAH and FlashAttention compatibility / 分数级 SSM-注意力融合，保持完美检索能力且原生兼容 FlashAttention |

### Model Efficiency, Compression & Training / 模型效率、压缩与训练

| Paper | Summary (EN / 中文) |
|-------|---------------------|
| [[2606.00888]] SMET | Dynamic sparse training for LLM pre-training with optimizer-state warm-up / 面向 LLM 预训练的动态稀疏训练，通过优化器状态预热解决不稳定问题 |
| [[2606.01117]] HASTE | Hardware-aware group-shared sparse training for extreme multi-label classification / 面向极端多标签分类的硬件感知组共享稀疏训练，实现数倍 GPU 加速 |
| [[2606.01126]] STARFISH | Post-pruning recovery via intermediate representation alignment with tiny calibration sets / 基于中间层表征对齐的剪枝后快速精度恢复，仅需极少量校准数据 |
| [[2606.01155]] Sparse Scaling Laws | First systematic study of DST scaling under data constraints with 8–10× compute reduction / 首次系统研究数据受限场景下动态稀疏训练的扩展规律，实现 8–10 倍计算量削减 |
| [[2606.01787]] ASADPREC | First asynchronous adaptive preconditioned methods for nonconvex optimization with O(1/√t) rate / 首个异步自适应预条件一阶优化方法，证明非凸随机设定下 O(1/√t) 收敛速率 |
| [[2606.01806]] ProbeScale | Neural scaling laws + probing for task-adaptive small language model compression / 神经缩放定律与探测分析结合，实现任务自适应的小语言模型压缩 |
| [[2606.01850]] Compression & Uncertainty | Conformal prediction benchmark showing compression decouples accuracy from uncertainty / 基于 conformal prediction 的压缩 LLM 不确定性评估，发现压缩将准确率与不确定性解耦 |
| [[2606.02218]] SAGC | Straggler-aware dynamic group sizing for synchronous on-policy RL training / 针对同步 on-policy RL 训练的动态组大小控制器，显著减少 straggler 延迟 |
| [[2606.02365]] FOAM | Adaptive damping for Shampoo reducing EVD operations to 5–10% / Shampoo 优化器的自适应阻尼方法，将特征分解操作降至约 5–10% |
| [[2606.02559]] SubFit | Submodule-level non-contiguous replacement-based LLM compression / 子模块级非连续替换后训练压缩方法，在多个稀疏度上取得最优困惑度-准确率权衡 |

### Alignment, Safety & Interpretability / 对齐、安全与可解释性

| Paper | Summary (EN / 中文) |
|-------|---------------------|
| [[2606.00831]] Subliminal Learning is LoRA Artifact | Shows subliminal learning is a fragile LoRA artifact, disappearing under full fine-tuning / 证明"潜意识学习"是 LoRA 微调的脆弱伪影，在完整微调下完全消失 |
| [[2606.00935]] Relational Intervention | Relational structure × first-person register interaction during functional collapse / 功能崩溃期间关系性结构与第一人称语域的交互作用显著改变模型行为 |
| [[2606.00995]] Subliminal Learning as Steering Vector Distillation | Reveals subliminal learning is mediated by a single steering vector / 揭示潜意识学习的本质是 steering vector 的蒸馏，并发现自适应优化器是必要条件 |
| [[2606.01033]] TriLens | Per-layer logit-lens entropy across three pathways for white-box hallucination detection / 通过三层输出的逐层 logit-lens 熵实现白盒幻觉检测，超越现有基线 |
| [[2606.01060]] MENTIS | Geometry-first framework measuring alignment-induced latent torsion in LLMs / 基于几何学的诊断框架，测量偏好对齐在模型内部计算中留下的结构化几何印记 |
| [[2606.01189]] The Case for Model Science | Manifesto for systematic model understanding through Verify, Explore, Steer, Refine / 提出"模型科学"学科方向，主张从验证、探索、引导、精修四维度系统性理解 AI 模型 |
| [[2606.01269]] Emergent Ordinal Geometry | Transformers spontaneously form 1D rank-aligned manifolds from local comparisons / Transformer 在仅学习相邻比较时自发形成一维有序表征流形，复现认知科学经典效应 |
| [[2606.01755]] TriAlign | Offline MARL framework for truth-invariant alignment in personalized LLMs / 首个基于离线多智能体强化学习的个性化 LLM 真理一致性对齐框架 |
| [[2606.02378]] When Do Attention Circuits Form? | Tracks induction head and attention-sink emergence across 30 checkpoints in three 1B models / 追踪三个 1B 模型中归纳头与注意力下沉的形成轨迹，发现两者在时间上可分离 |
| [[2606.02530]] SafeSteer | Localized on-policy distillation for safety alignment with only 100 harmful samples / 局部化 on-policy 蒸馏安全对齐方法，仅需 100 条有害样本即可达到顶尖安全性能 |

### Multimodal & Specialized Models / 多模态与专用模型

| Paper | Summary (EN / 中文) |
|-------|---------------------|
| [[2606.00959]] PID for Multimodal LLMs | Partial Information Decomposition for quantifying modality contributions in MLLMs / 将部分信息分解引入多模态大语言模型，量化视觉、文本和音频输入的独特、冗余与协同贡献 |
| [[2606.01599]] TRON | 520 procedural generator-verifier environments for visual-reasoning RL / 包含 520 个程序化生成-验证环境的在线视觉推理强化学习框架 |
| [[2606.01802]] MOSS-Audio | Unified audio-language model with DeepStack cross-layer feature injection / 统一音频语言模型，通过 DeepStack 跨层特征注入实现语音、环境声和音乐的联合理解 |
| [[2606.01810]] Causal Plan | Physically grounded causal reasoning framework for embodied agents / 将具身智能体从表面 token 预测者转变为具备物理 grounded 因果推理能力的规划器 |
| [[2606.02578]] Perception-Judge | Mitigates perceptual judgment bias in multimodal LLM-as-a-Judge via GRPO / 基于 GRPO 缓解多模态评判器中的感知判断偏差，显著提升视觉 grounding 评估可靠性 |

### Knowledge Editing, Causal Discovery & Benchmarks / 知识编辑、因果发现与基准

| Paper | Summary (EN / 中文) |
|-------|---------------------|
| [[2606.01610]] JNO | Joint neighborhood optimization for knowledge editing ripple effects / 通过联合优化邻域目标表示显式建模知识编辑中的传播协调压力与泄漏压力 |
| [[2606.01789]] Causal Discovery Benchmarks | Reveals severe inconsistency in widely-used causal discovery benchmarks / 发现多个广泛使用的因果发现基准存在严重的知识过时问题，不一致率高达 50% 以上 |
| [[2606.02430]] LLMFI | Fine-grained fault-injection framework for error propagation in LLM inference / 首个面向 LLM 推理的细粒度确定性故障注入框架，系统研究计算与内存故障的传播规律 |

---

## All Papers / 全部论文

| # | ID | Title | Topic |
|---|-----|-------|-------|
| 1 | [[2606.00642]] | Hidden Thoughts Are Not Secret: Reasoning Trace Exposure in LLMs | 推理与推断优化 |
| 2 | [[2606.00644]] | ForeSci: Evaluating LLM Agents for Forward-Looking AI Research Judgment | 智能体系统与编排 |
| 3 | [[2606.00726]] | Latent Reward Steering: An Adaptive Inference-Time Framework that Implicitly Promotes Cognitive Behaviors in Reasoning LLMs | 推理与推断优化 |
| 4 | [[2606.00765]] | FALAT: Tracing Failures in LLM Agent Trajectories via Dependency-Guided Search | 智能体系统与编排 |
| 5 | [[2606.00831]] | Subliminal Learning is a LoRA Artifact | 对齐、安全与可解释性 |
| 6 | [[2606.00888]] | Memory-Efficient LLM Training with Dynamic Sparsity: From Stability to Practical Scaling | 模型效率、压缩与训练 |
| 7 | [[2606.00920]] | Accuracy, Stability, and Repeated-Run Reliability of Large Language Models on Deterministic Programming Tasks | 推理与推断优化 |
| 8 | [[2606.00935]] | Relational Intervention During Functional Collapse in Large Language Models | 对齐、安全与可解释性 |
| 9 | [[2606.00959]] | Towards Understanding Modality Interaction in Multimodal Language Models via Partial Information Decomposition | 多模态与专用模型 |
| 10 | [[2606.00995]] | Subliminal Learning Is Steering Vector Distillation | 对齐、安全与可解释性 |
| 11 | [[2606.01019]] | Hybrid Verified Decoding: Learning to Allocate Verification in Speculative Decoding | 推理与推断优化 |
| 12 | [[2606.01033]] | TriLens: Per-Layer Logit-Lens Entropy for White-Box Hallucination Detection | 对齐、安全与可解释性 |
| 13 | [[2606.01060]] | MENTIS: What Belief Changes Under Alignment? Measuring Multi-Scale Latent Torsion in Language Models | 对齐、安全与可解释性 |
| 14 | [[2606.01117]] | HASTE: Hardware-Aware Dynamic Sparse Training for Large Output Spaces | 模型效率、压缩与训练 |
| 15 | [[2606.01126]] | STARFISH: faST Accuracy Recovery in pruned networks From Internal State Healing | 模型效率、压缩与训练 |
| 16 | [[2606.01155]] | When Data Is Scarce: Scaling Sparse Language Models with Repeated Training | 模型效率、压缩与训练 |
| 17 | [[2606.01189]] | The Case for Model Science: Verify, Explore, Steer, Refine | 对齐、安全与可解释性 |
| 18 | [[2606.01202]] | The Shape of Wisdom: Decision Trajectories in Language Models | 推理与推断优化 |
| 19 | [[2606.01269]] | Emergent Ordinal Geometry in Transformers Trained on Local Comparisons | 对齐、安全与可解释性 |
| 20 | [[2606.01351]] | Recognize Your Orchestrator: An Entropy Dynamics Perspective for LLM Multi-Agent Systems | 智能体系统与编排 |
| 21 | [[2606.01365]] | Early Diagnosis of Wasted Computation in Multi-Agent LLM Systems via Failure-Aware Observability | 智能体系统与编排 |
| 22 | [[2606.01416]] | Self-Healing Agentic Orchestrators for Reliable Tool-Augmented Large Language Model Systems | 智能体系统与编排 |
| 23 | [[2606.01462]] | An Enigma of Artificial Reason: Investigating the Production-Evaluation Gap in Large Reasoning Models | 推理与推断优化 |
| 24 | [[2606.01599]] | TRON: Targeted Rule-Verifiable Online Environments for Visual Reasoning RL | 多模态与专用模型 |
| 25 | [[2606.01610]] | Revisiting Ripple Effects in Knowledge Editing through Pressure-Aware Joint Neighborhood Optimization | 知识编辑、因果发现与基准 |
| 26 | [[2606.01725]] | Characterization of Multi-Model Agentic AI Systems on General Tasks via Trace-Driven Simulation | 智能体系统与编排 |
| 27 | [[2606.01755]] | TriAlign: Towards Universal Truth Consistency in Personalized LLM Alignment | 对齐、安全与可解释性 |
| 28 | [[2606.01787]] | Stochastic convergence of parallel asynchronous adaptive first-order methods | 模型效率、压缩与训练 |
| 29 | [[2606.01789]] | Consistency evaluation of benchmarks used for causal discovery | 知识编辑、因果发现与基准 |
| 30 | [[2606.01802]] | MOSS-Audio Technical Report | 多模态与专用模型 |
| 31 | [[2606.01806]] | ProbeScale: Probing Analysis to Optimize Neural Scaling Laws for Efficient Small Language Model Inference | 模型效率、压缩与训练 |
| 32 | [[2606.01810]] | Token Predictors Are Not Planners: Building Physically Grounded Causal Reasoners | 多模态与专用模型 |
| 33 | [[2606.01850]] | Does Compression Preserve Uncertainty? A Unified Benchmark for Quantized and Sparse LLMs via Conformal Prediction | 模型效率、压缩与训练 |
| 34 | [[2606.01912]] | SMH-Bench: Benchmarking LLM Agents for Environment-Grounded Reasoning and Action in Smart Homes | 智能体系统与编排 |
| 35 | [[2606.01991]] | SafeMCP: Proactive Power Regulation for LLM Agent Defense via Environment-Grounded Look-Ahead Reasoning | 智能体系统与编排 |
| 36 | [[2606.02011]] | Extreme Low-Bit Inference in Reasoning Models: Failure Modes and Targeted Recovery | 推理与推断优化 |
| 37 | [[2606.02054]] | eMoT: evolving Memory-of-Thought via Symbolic Anchoring and Memory Corrosion | 推理与推断优化 |
| 38 | [[2606.02060]] | Where Do Deep-Research Agents Go Wrong? Span-Level Error Localization in Agent Trajectories | 智能体系统与编排 |
| 39 | [[2606.02132]] | Learning When Not to Act: Mitigating Tool Abuse in Agentic Reinforcement Learning | 智能体系统与编排 |
| 40 | [[2606.02218]] | Faster Synchronous On-Policy RL via Straggler-Aware Group Sizing | 模型效率、压缩与训练 |
| 41 | [[2606.02332]] | Forget Attention: Importance-Aware Attention Is All You Need | 推理与推断优化 |
| 42 | [[2606.02365]] | FOAM: Frequency and Operator Error-Based Adaptive Damping Method for Reducing Staleness-Oriented Error for Shampoo | 模型效率、压缩与训练 |
| 43 | [[2606.02378]] | When Do Attention Circuits Form? Developmental Trajectories of Capability and Attention-Sink Emergence Across Three 1B-Class Architectures | 对齐、安全与可解释性 |
| 44 | [[2606.02380]] | SPADE-Bench: Evaluating Spontaneous Strategic Deception in Agents via Plan-Action Divergence | 智能体系统与编排 |
| 45 | [[2606.02430]] | Not All Errors Are Equal: A Systematic Study of Error Propagation in Large Language Model Inference | 知识编辑、因果发现与基准 |
| 46 | [[2606.02494]] | Monitoring Agentic Systems Before They're Reliable | 智能体系统与编排 |
| 47 | [[2606.02530]] | SafeSteer: Localized On-Policy Distillation for Efficient Safety Alignment | 对齐、安全与可解释性 |
| 48 | [[2606.02536]] | Tracking the Behavioral Trajectories of Adapting Agents | 智能体系统与编排 |
| 49 | [[2606.02559]] | From Layers to Submodules: Rethinking Granularity in Replacement-Based LLM Compression | 模型效率、压缩与训练 |
| 50 | [[2606.02578]] | Mitigating Perceptual Judgment Bias in Multimodal LLM-as-a-Judge via Perceptual Perturbation and Reward Modeling | 多模态与专用模型 |

---

> **验证说明 / Verification Note:** 本 overview 共收录 50 篇论文，与 `~/Documents/daily_paper/arxiv-daily/2026-06-02/` 目录下除 `overview.md` 外的 50 个 `.md` 文件数量一致。The paper count in this overview (50) matches the actual number of `.md` files in the directory (excluding `overview.md` itself).
