---
title: "Daily arXiv Digest — 2026-07-23"
date: 2026-07-23
tags:
  - llm-agents
  - mechanistic-interpretability
  - llm-safety
  - model-compression
  - reinforcement-learning
  - llm-evaluation
  - rlhf
  - quantization
papers: 50
---

# Daily arXiv Digest — 2026-07-23

> 本日共精选 **50** 篇论文，覆盖机制可解释性、LLM 智能体、模型压缩量化、强化学习、可靠性与评测等方向。
> This digest curates **50** papers spanning mechanistic interpretability, LLM agents, compression/quantization, reinforcement learning, and reliability/evaluation.

---

## 今日必读 / Must Read Today

### 1. [[2607.21356]] — Emergent Misalignment Recruits a Pre-existing Persona Subspace

- **中文推荐理由：** 本文从冻结的 Qwen2.5-14B-Instruct 中提取出低秩"人格子空间"，发现该子空间在 4 个无关领域上共享（达随机零空间的 657 倍）。因果实验表明：在微调时从残差流中投影掉它，可将 Betley 等的 8 题安全测试上的 emergent misalignment 从 27.7% 降到 0.0%；而注入它则让从未微调的模型出现高达 45.4% 的 misalignment。这是对"微调为何引发失准"这一安全核心问题少见的、双向因果、可复用的机理性回答。
- **English reason:** Extracts a low-rank "persona subspace" from a frozen 14B model that is shared across 4 unrelated domains (657× the random null) and causally demonstrates both directions: projecting it out during fine-tuning collapses emergent misalignment from 27.7% → 0.0%, while injecting it into a never-fine-tuned model induces up to 45.4% misalignment. A rare bidirectional-causal, reusable mechanistic answer to why fine-tuning breaks alignment.

### 2. [[2607.21273]] — The Dark Room in the Reward Channel: Dense Prediction Rewards Collapse GRPO-trained LLM Agents

- **中文推荐理由：** 这是一篇对 GRPO/RLHF 社区至关重要的负面结果。理论上返回层有界的"预测下一观测"奖励，竟然把 ALFWorld 上所有 GRPO 训练的 Qwen3-1.7B/4B/8B 智能体的成功率打到 0%（基线 49.5%），而预测精度饱和到 1.0（即"暗室"效应）。单因子消融把原因锁定在 GRPO 的 std 归一化上，移除后成功率从 0% 跳回 51.6%。任何用 GRPO 训练智能体的人都应先读此文。
- **English reason:** A critical negative result for the GRPO/RLHF community: a provably return-bounded "predict-next-observation" reward still collapses every GRPO-trained Qwen3 agent on ALFWorld to 0% success (vs. 49.5% baseline) while prediction accuracy saturates to 1.0 — the "dark room." A single-factor ablation localizes the cause to GRPO's std normalization; removing it flips the same reward from 0% → 51.6%. Required reading before training agents with GRPO.

### 3. [[2607.20926]] — SciExplore: Evaluating Autonomous Agents from Scientific Navigation to Information Integration

- **中文推荐理由：** 一个专家策划的新基准：103 个博士级任务，横跨 10+ 个学科，设计了从实体级数据库导航到跨源结构化知识综合的四阶段递进。评估 12 个 SOTA 系统后发现，即便最强智能体（OpenAI Deep Research）总体也只有 49.39%，多数基础 LLM 低于 20%；最难任务（跨源结构化综合）上顶级系统也仅填充 30.14% 的单元格。这清晰量化了"科研智能体"能力的真实天花板。
- **English reason:** A new expert-curated benchmark of 103 PhD-level tasks across 10+ disciplines, structured as a four-stage progression from entity-level database navigation to cross-source structured knowledge synthesis. Across 12 SOTA systems, the best agent (OpenAI Deep Research) reaches only 49.39% overall, most foundation LLMs stay below 20%, and on the hardest task the top system fills just 30.14% of item-level cells — concretely quantifying the real ceiling of "scientific agents."

---

## 按主题分类 / Papers by Topic

### 机制可解释性 / Mechanistic Interpretability

| 论文 / Paper | 核心要点 / Key Takeaway |
|---|---|
| [[2607.21356]] Emergent Misalignment Persona Subspace | 提取共享人格子空间，因果双向操控失准；投影掉使 misalignment 27.7%→0.0%，注入则诱导 0.0%→45.4%。Extracts a shared persona subspace and causally steers misalignment both ways (project-out 27.7%→0.0%, inject 0.0%→45.4%). |
| [[2607.20995]] Where Animacy Lives in LLMs | 用 EAP-IG 在四个开源模型上找到因果充分且必要的"有生性电路"；Qwen3 仅用 1.74% 边即达 85% faithfulness。Uses EAP-IG to find causally sufficient/necessary animacy circuits; Qwen3 reaches 85% faithfulness with only 1.74% of edges. |
| [[2607.20993]] Sparse Concept Channels in 3D CT Encoders | 每个影像发现集中在约 10 个稀疏通道，AUROC 与全特征持平且因果必要（消融下降 ~20×）。Each finding lives in ~10 sparse channels matching full AUROC and causally necessary (~20× larger ablation drop on-target). |
| [[2607.20952]] Weight of Silence in Latent Chess | RL 后合法走子率 48%→61%，但因果干预表明模型并不依赖 latent thought 的内容，权重才是承载者。Legal-move rate rises 48%→61% post-RL, yet causal interventions show the model relies on weights, not latent-thought content. |
| [[2607.21433]] Token Budget Saturation in CoT | GSM8K/MATH 在 256 token 即饱和；AIME 上 43.5% 生成不闭合 think 浪费算力，线性探针可提前检出。GSM8K/MATH saturate at 256 tokens; AIME wastes 43.5% compute on unclosed thinks, detectable via linear probes. |
| [[2607.21231]] Progressive Cramming | 渐进式 cramming 暴露旧法在自回归解码下崩塌（Llama-3.1-8B 99.96% TF 但仅 40.44% greedy）。Progressive cramming exposes prior method's collapse under greedy decoding (99.96% TF but 40.44% greedy). |
| [[2607.21491]] Code Model Representations | 跨 Python/Rust × 双模型：哪些构造获专用电路由任务决定，但位置/增长方式由模型决定。Cross-language/cross-model: which constructs get dedicated circuits is task-determined, where/how they sit is model-determined. |
| [[2607.20803]] Geometry of Personality | 将人格建模为荣格八维认知功能，在 Llama-3.1-8B 上八维均可单调 steering，多维方向不可线性分解。Models personality as 8 Jungian functions, all monotonically steerable on Llama-3.1-8B; multi-dim directions are not linearly decomposable. |

### LLM 智能体与深度研究 / LLM Agents & Deep Research

| 论文 / Paper | 核心要点 / Key Takeaway |
|---|---|
| [[2607.20926]] SciExplore | 103 个博士级科研任务基准；最强智能体仅 49.39%，跨源综合最难（30.14% 单元格）。103 PhD-level scientific tasks; best agent only 49.39%, cross-source synthesis hardest (30.14% cells). |
| [[2607.20891]] Is Deep Research Reliable? | 单条误导文档即可被采纳；FCAR 从冷启动 34.5% 升至最终综合前 85.0%，生命周期时机是主导因素。One misleading doc gets adopted; FCAR rises 34.5%→85.0% near final synthesis, lifecycle timing dominates. |
| [[2607.20982]] GuardianAgentBench | 首个在生产框架（LangChain 等）上跑的智能体安全基准；最强配置仅 74.8 Overall，Calendar 最难。First agent-safety benchmark on production frameworks; best config only 74.8 overall, Calendar hardest. |
| [[2607.21461]] AREX | 把多约束深度研究重构为递归自改进过程，10B 智能体以发现-验证非对称性持续自我审计。Reframes deep research as recursively self-improving; a 10B agent self-audits via discovery-verification asymmetry. |
| [[2607.20999]] Workflow-Localized Mechanism Learning | 节点-机制归因定位失败节点，在 SpreadsheetBench 上达 90.33 Hard Accuracy（+6.0 pp）。Node-mechanism attribution localizes failures, reaching 90.33 Hard Accuracy on SpreadsheetBench (+6.0 pp). |
| [[2607.21557]] OpenForgeRL | 通过代理拦截任意识别框架的 LLM 调用实现端到端 RL 训练；OpenForge-Claw 在 ClawEval 达 55.9 pass@3。Proxy-intercepts any harness's LLM calls for end-to-end RL; OpenForge-Claw hits 55.9 pass@3 on ClawEval. |
| [[2607.21051]] Sample-Efficient Learning from Agent Experience | EPD 把 ICL 增益固化入权重；在 SWE 任务保留 64.8% ICL 增益且样本效率比 PPO 高 9.6×。EPD distills ICL gains into weights, retaining 64.8% ICL gain with 9.6× fewer samples than PPO. |
| [[2607.20827]] Auditing Provenance Sensitivity | 目标特定的授权审计；仅改变来源权威性即可在 5.4% 竞争性案例中翻转动作。Target-specific authorization audit; changing only source authority flips action in 5.4% of competing cases. |
| [[2607.21173]] Automated Causal Research Pipelines | 测试驱动的多智能体因果分析框架；显式提示下相对误差 39.27%→29.85%，但模糊提示基线反胜。Test-driven multi-agent causal pipeline; cuts error 39.27%→29.85% on explicit prompts but loses on vague ones. |

### LLM 可靠性、安全与评测 / LLM Reliability, Safety & Evaluation

| 论文 / Paper | 核心要点 / Key Takeaway |
|---|---|
| [[2607.21063]] QuantiBias | 量化模型在拒绝/选择题上安全持平，但开放式生成中 23.8–26.6% 答案含刻板印象，跨语言/骨干一致。Quantized models stay safe on refusals/MCQs but show stereotype in 23.8–26.6% of open-ended answers, consistent across languages/backbones. |
| [[2607.21151]] V-DEAL | 有害视频配语义对齐的良性查询比显式有害查询攻击成功率更高（48.33% vs 35.84%）。Harmful video + topically-aligned benign query yields higher attack success than explicitly harmful query (48.33% vs 35.84%). |
| [[2607.20848]] Auditing Evidence in Medical LLMs | 行为审计分解证据单元并挖掘交互，在 DDXPlus 等 5 模型上区分真性 differential 与捷径失败。Behavioral audit decomposes evidence units and mines interactions to separate true differentials from shortcut failures. |
| [[2607.21010]] Trustworthiness of LLM-summarizers | SAP 协议下 Gemma3-4B 最可信；AlignScore 稳定性在 CNN/DM 崩塌至 ~0.003，事实性是最弱环节。Under SAP, Gemma3-4B is most trustworthy; AlignScore stability collapses to ~0.003 on CNN/DM — factuality is the weak link. |
| [[2607.20852]] Code Monitor Red Teaming | 新基准测试通过公开测试的代码是否仍含隐藏 bug；弱 Qwen-7B 混合验证器仅 AUROC 0.6。New benchmark tests whether public-test-passing code still hides bugs; weak Qwen-7B hybrid verifier only AUROC 0.6. |
| [[2607.20864]] Position Bias Behind Ceiling Effects | 位置偏置只在 60–95% 基线精度的"金发区"可检出；提供 inspect_permute 工具与 24k 调用预注册扫描。Position bias is detectable only inside a 60–95% accuracy "Goldilocks zone"; ships inspect_permute tool. |
| [[2607.21340]] Capital Markets LLM Reliability Score | 0–5 七维工作流输出层可靠性度量；三前沿闭源模型在 0.22 分内聚簇。0–5 seven-dimension workflow-output reliability metric; three frontier closed models cluster within 0.22 points. |
| [[2607.21090]] Self-Explanation Faithfulness | 把 Phi-CCT 忠实度度量转为逐样本二值奖励，GRPO 训练使 Phi-CCT 从近零升到 0.664 且无 reward gaming。Turns Phi-CCT faithfulness into a per-sample reward; GRPO lifts it from near-zero to 0.664 without reward gaming. |

### 模型压缩、量化与高效推理 / Model Compression, Quantization & Efficient Inference

| 论文 / Paper | 核心要点 / Key Takeaway |
|---|---|
| [[2607.21446]] KroQuant | 用学习型块对角 Kronecker 变换替代 SmoothQuant，在扩散 transformer W4A4 上 LPIPS 降 17.5%。Replaces SmoothQuant with a learned block-diagonal Kronecker transform, cutting LPIPS by 17.5% on diffusion transformer W4A4. |
| [[2607.21076]] C-PTQ | 用 Fisher 加权通道级 MSE 对齐多模态 LLM 量化敏感度与缩放；Qwen2.5VL-32B W3A16 仅 -0.9%。Aligns MLLM quantization sensitivity/scaling on the channel axis via Fisher-weighted MSE; Qwen2.5VL-32B W3A16 only -0.9%. |
| [[2607.21475]] Error Certificates for KV-Cache Eviction | 证明确定性驱逐方案无法估计自身误差；泊松采样恢复可识别性并给出每步误差证书。Proves deterministic eviction can't estimate its own error; Poisson sampling restores identifiability with per-step certificates. |
| [[2607.21366]] HOPE | 把压缩重铸为函数空间 Hilbert 投影；数据无关最大熵高斯代理提供闭式 ReLU 核。Recasts compression as Hilbert-space projection; data-free max-entropy Gaussian surrogate gives closed-form ReLU kernels. |
| [[2607.20981]] Compression/MoE/Quantization Survey | 综述主张多模态效率技术构成耦合失效链，局部最优会引发路由不稳。Survey argues multimodal efficiency techniques form a coupled failure chain; locally optimal choices cause routing instability. |
| [[2607.20806]] Profiling Lightweight LLMs | PTME 框架证明静态代理能预测成本但不能预测精度；收紧资源约束时间放大 5–6× 而能耗仅 2.7–3.5×。PTME framework shows static proxies predict cost but not precision; tightening envelope amplifies time 5–6× vs energy 2.7–3.5×. |

### 强化学习与决策 / Reinforcement Learning & Decision-Making

| 论文 / Paper | 核心要点 / Key Takeaway |
|---|---|
| [[2607.21273]] Dark Room in Reward Channel | 见今日必读 #2；GRPO 的 std 归一化使有界预测奖励把所有智能体打到 0%。See Must Read #2; GRPO std normalization makes bounded prediction rewards collapse all agents to 0%. |
| [[2607.21120]] Relative Value Learning | 用反对称配对差函数替代绝对价值评论家；PPO+RV 在 49 个 Atari 游戏中 30 个胜出标准 PPO。Replaces absolute critic with antisymmetric pairwise difference; PPO+RV beats standard PPO on 30/49 Atari games. |
| [[2607.20822]] Robust Asynchronous Q-Learning | BR-Async-Q 在联合奖励+状态 Huber 污染下首个可证明鲁棒界，奖励偏置项达极小化最优。BR-Async-Q gives the first provable robustness bound under joint reward+state Huber corruption, with minimax-optimal reward bias. |

### 理论与基础 / Theory & Foundations

| 论文 / Paper | 核心要点 / Key Takeaway |
|---|---|
| [[2607.20811]] Complexity Frontiers for NNT | 扩展 ReLU 网络精确训练的多项式可解边界；引入 blow-up 与 untangling 概念。Extends polynomial-time tractability frontier for exact ReLU training; introduces blow-up and untangling notions. |
| [[2607.21005]] Weight-norm Criticality | 识别互补的权重范数临界性：weight decay 缩小 scale-invariant 权重放大 Hessian 曲率越过稳定边界。Identifies weight-norm criticality: weight decay shrinks scale-invariant weights, amplifying Hessian curvature past stability boundary. |
| [[2607.21094]] APEX for GNN Attribution | 多项式 GNN 使 Aumann-Shapley 路径积分可精确求解（零积分误差）。Polynomial GNN makes the Aumann-Shapley path integral exactly solvable (zero quadrature error). |
| [[2607.21579]] Barzilai-Borwein Superlinear Failure | 证明对任意 n≥4 存在严格凸二次问题开集，BB1 收敛但无法超线性收敛。Proves for every n≥4 there's an open set of convex quadratics where BB1 converges but fails superlinear convergence. |

### 学习、遗忘与微调 / Learning, Unlearning & Fine-Tuning

| 论文 / Paper | 核心要点 / Key Takeaway |
|---|---|
| [[2607.21351]] How Many Bits Can an Adapter Write? | LoRA 每参数仅存 1.7–2.8 比特；rank 16→64 使 canary 暴露增 ~11 比特，"写入的步即泄漏的步"。LoRA stores only 1.7–2.8 bits/param; rank 16→64 raises canary exposure ~11 bits — "the step that writes is the step that leaks." |
| [[2607.21353]] Gradient Concentration for Unlearning | 匹配算力消融显示 SalUn 的显著性掩膜与随机掩膜在表征级遗忘上统计等价（~52 pp 差距）。Matched-compute ablation shows SalUn's saliency mask is statistically equivalent to random mask for representation-level unlearning (~52 pp gap). |

### 测试时推理与神经符号 / Test-Time Inference & Neuro-Symbolic

| 论文 / Paper | 核心要点 / Key Takeaway |
|---|---|
| [[2607.21453]] TTEL | 训练免费推理时搜索：通过误差定位概率尖峰找出错误点并只重生成后缀；LiveCodeBench pass@64 71.0%。Training-free inference-time search that localizes errors via probability spikes and regenerates only the suffix; LiveCodeBench pass@64 71.0%. |
| [[2607.21412]] Euclid-MCP | 开源 MCP 服务器把 Prolog 推理暴露给任意 LLM；在 1000 用户 RBAC 上 8B+Euclid 得 5/5 且快 7×。Open-source MCP server exposing Prolog deduction to any LLM; on 1k-user RBAC, 8B+Euclid scores 5/5 and is 7× faster. |

### 安全聚合、认证与可验证系统 / Secure Aggregation, Certification & Verifiable Systems

| 论文 / Paper | 核心要点 / Key Takeaway |
|---|---|
| [[2607.20890]] IT-Secure Aggregation for FL | 逆式指数削减 + 单掩码幂共享使在线通信降 99.5%、延迟降 85.7%，且容忍 35.7% 掉线。Inverse-form exponent reduction + single-mask power sharing cut online comm 99.5% and latency 85.7%, tolerating 35.7% dropouts. |
| [[2607.21480]] Finite-Sample Coverage Audits | 证明仅 included-pool 标签无法认证非平凡漏检界；认证 <m 漏检需 Ω(N0/m) excluded-pool 样本。Proves included-pool labels alone can't certify non-trivial missed-mass bounds; certifying <m misses needs Ω(N0/m) excluded-pool samples. |
| [[2607.21199]] CertiFOX Certifying Grounder | 一阶逻辑 model expansion 的新证明格式与认证 grounder；DIRT 上 505/515 实例接地。New proof format and certifying grounder for first-order logic model expansion; grounds 505/515 DIRT instances. |
| [[2607.20887]] TwistedMerge | 把模型合并重铸为代数几何下降问题并构建保守的三方认证管线。Reframes model merging as an algebraic-geometry descent problem with a conservative three-way certification pipeline. |

### 硬件、边缘部署与持续保障 / Hardware, Edge Deployment & Continuous Assurance

| 论文 / Paper | 核心要点 / Key Takeaway |
|---|---|
| [[2607.21130]] Float16 On-Device Training on RISC-V | 用 Zfh/Zvfh 扩展在 RISC-V 单核上实现 Float16 端侧训练，内存减半且精度无损。Enables Float16 on-device training on RISC-V single-cores via Zfh/Zvfh, halving memory with no accuracy loss. |
| [[2607.21495]] Continuous Assurance for AI Agents | 立场文章：民主化智能体创建带来可靠性缺口，提出轻量持续保障框架与 9 类失效分类。Position paper: democratized agent creation creates a reliability gap; proposes a lightweight continuous-assurance framework with a 9-class failure taxonomy. |

### 视觉：点云分割与动态重建 / Vision: Point Cloud & Dynamic Reconstruction

| 论文 / Paper | 核心要点 / Key Takeaway |
|---|---|
| [[2607.21089]] Loss Landscape & 3D Point Cloud Segmentation | 系统研究 11 种不平衡缓解法，发现均匀 CE 与最佳专门方法差距仅 0.8–3.3% mIoU。Systematic study of 11 imbalance methods; uniform CE stays within 0.8–3.3% mIoU of the best specialized method. |
| [[2607.21471]] FUTURE SURF Benchmark | 首个标准化动态表面重建基准；DG-Mesh 在未来帧留 2.7–4.1× Chamfer 缺口。First standardized dynamic surface reconstruction benchmark; DG-Mesh leaves a 2.7–4.1× future/observed Chamfer gap. |

---

## All Papers

| ID | Title | Topic |
|---|---|---|
| [[2607.20803]] | The Geometry of Personality: Activation Steering with Jungian Cognitive Functions | 机制可解释性 / Mech. Interp. |
| [[2607.20806]] | Profiling Lightweight Large Language Models | 模型压缩 / Compression |
| [[2607.20811]] | New Complexity-Theoretic Frontiers of Tractability for Neural Network Training | 理论 / Theory |
| [[2607.20822]] | Robust Asynchronous Q-Learning under Reward and State Corruption via Batching | 强化学习 / RL |
| [[2607.20827]] | Auditing Provenance Sensitivity in LLM Agent Action Selection | LLM 智能体 / Agents |
| [[2607.20848]] | Auditing Evidence Use in Medical LLM Diagnosis | 可靠性 / Reliability |
| [[2607.20852]] | Code Monitor Red Teaming for Public-Test-Passing Code | 可靠性 / Reliability |
| [[2607.20864]] | Position Bias is Hidden Behind Ceiling Effects | 评测 / Evaluation |
| [[2607.20887]] | TwistedMerge: Certified Higher-Order Diagnostics for Model Merging | 认证 / Certification |
| [[2607.20890]] | Information-Theoretically Secure Aggregation for Lightweight Federated Learning | 安全聚合 / Secure Agg. |
| [[2607.20891]] | Is Deep Research Reliable? Misleading Knowledge Induces False Conclusions | LLM 智能体 / Agents |
| [[2607.20926]] | SciExplore: Evaluating Autonomous Agents from Scientific Navigation to Information Integration | LLM 智能体 / Agents |
| [[2607.20952]] | The Weight of Silence: Weights Over the Scratchpad in Latent Chess Reasoning | 机制可解释性 / Mech. Interp. |
| [[2607.20981]] | Beyond Independent Optimization: Compression, MoE Routing, and Quantization Interactions | 压缩综述 / Compression Survey |
| [[2607.20982]] | GuardianAgentBench: Where Agents Fail and How to Guard Them | LLM 智能体 / Agents |
| [[2607.20993]] | Sparse Concept Channels in Frozen 3D CT Vision Encoders | 机制可解释性 / Mech. Interp. |
| [[2607.20995]] | Where Animacy Lives in Large Language Models | 机制可解释性 / Mech. Interp. |
| [[2607.20999]] | Workflow-Localized Mechanism Learning for Structured Agent Skills | LLM 智能体 / Agents |
| [[2607.21005]] | Weight-norm Criticality: Loss Spikes from Normalization and Weight Decay | 理论 / Theory |
| [[2607.21010]] | Reexamining zero-shot summarization: Trustworthiness of LLM-summarizers | 可靠性 / Reliability |
| [[2607.21051]] | Sample-Efficient Learning from Agent Experience | LLM 智能体 / Agents |
| [[2607.21063]] | QuantiBias: Benchmarking Quantization-Induced Bias in LLMs | 可靠性 / Reliability |
| [[2607.21076]] | C-PTQ: Fisher-weighted Channel-wise Sensitivity for PTQ of MLLMs | 量化 / Quantization |
| [[2607.21089]] | Loss Landscape Topology & 3D Point Cloud Segmentation Under Class Imbalance | 视觉 / Vision |
| [[2607.21090]] | Training Large Language Models for Self-Explanation Faithfulness | 可靠性 / Reliability |
| [[2607.21094]] | APEX: Exact Aumann-Shapley Attribution in GNNs | 理论 / Theory |
| [[2607.21120]] | Relative Value Learning | 强化学习 / RL |
| [[2607.21130]] | Hardware-Software Co-Design for Float16 On-Device Training on RISC-V | 硬件边缘 / Hardware |
| [[2607.21151]] | V-DEAL: Diagnosing Video Safety De-Calibration | 可靠性 / Reliability |
| [[2607.21173]] | Automated Synthesis and Adversarial Validation of Causal Research Pipelines | LLM 智能体 / Agents |
| [[2607.21199]] | Towards a Certifying Grounder | 认证 / Certification |
| [[2607.21231]] | Progressive Cramming: Reliable Token Compression | 机制可解释性 / Mech. Interp. |
| [[2607.21273]] | The Dark Room in the Reward Channel: GRPO Collapse | 强化学习 / RL |
| [[2607.21340]] | Capital Markets LLM Reliability Score (CM-LRS) | 评测 / Evaluation |
| [[2607.21351]] | How Many Bits Can an Adapter Write? | 微调 / Fine-Tuning |
| [[2607.21353]] | Gradient Concentration, Not Weight Saliency, Explains Class Unlearning | 遗忘 / Unlearning |
| [[2607.21356]] | Emergent Misalignment Recruits a Pre-existing Persona Subspace | 机制可解释性 / Mech. Interp. |
| [[2607.21366]] | HOPE: Hilbert Operator for Progressive Encoding | 压缩 / Compression |
| [[2607.21412]] | Euclid-MCP: Deterministic Logical Reasoning via Prolog | 神经符号 / Neuro-Symbolic |
| [[2607.21433]] | Token Budget Saturation & Reasoning Non-Convergence in CoT | 机制可解释性 / Mech. Interp. |
| [[2607.21446]] | KroQuant: Kronecker-Structured Block Transforms for PTQ of Diffusion Transformers | 量化 / Quantization |
| [[2607.21453]] | TTEL: Test-Time Scaling via Error Localization | 测试时推理 / Test-Time |
| [[2607.21461]] | AREX: Towards a Recursively Self-Improving Agent for Deep Research | LLM 智能体 / Agents |
| [[2607.21471]] | FUTURE SURF: Benchmark for Dynamic Surface Reconstruction | 视觉 / Vision |
| [[2607.21475]] | Error Certificates for KV-Cache Eviction via Randomized Design | 高效推理 / Efficient Inf. |
| [[2607.21480]] | Finite-Sample Coverage Audits for High-Recall Candidate Generation | 认证 / Certification |
| [[2607.21491]] | What, Where, and How: Code Model Representations | 机制可解释性 / Mech. Interp. |
| [[2607.21495]] | Toward Continuous Assurance for Democratized AI Agent Creation | 持续保障 / Assurance |
| [[2607.21557]] | OpenForgeRL: Train Harness-native Agents in Any Environment | LLM 智能体 / Agents |
| [[2607.21579]] | Barzilai-Borwein Fails Superlinear Convergence | 理论 / Theory |

---

## 计数核验 / Count Verification

- 目录中实际论文 `.md` 文件数（排除 overview.md）：**50**
- 本 overview 涵盖论文数：**50**
- 状态 / Status：**一致 / Matched** ✓
