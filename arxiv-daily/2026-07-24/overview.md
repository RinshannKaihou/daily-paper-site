---
title: "Daily arXiv Digest — 2026-07-24"
date: 2026-07-24
tags:
  - arxiv-daily
  - mechanistic-interpretability
  - llm-agents
  - quantization
  - reinforcement-learning
  - safety-alignment
  - training-dynamics
papers: 41
---

# Daily arXiv Digest — 2026-07-24

> 41 篇论文 · Curated across mechanistic interpretability, LLM agents, quantization/efficiency, RL/training dynamics, safety/alignment, evaluation, and theory.

## 今日必读 / Must Read Today

### 1. [[2607.21461]] AREX: Towards a Recursively Self-Improving Agent for Deep Research

- **推荐理由：** BAAI 提出的递归自改进深度研究智能体，122B-A10B MoE 在 BrowseComp 上达 82.5、WideSearch-en 达 82.0，超越 Qwen3.5-397B 与 GPT-5.4，证明"发现难、验证易"的 RSI 范式可在生产级基准上刷新 SOTA，且权重开源。
- **Why read:** A recursively self-improving deep-research agent whose 122B-A10B MoE hits 82.5 on BrowseComp and 82.0 on WideSearch-en — beating Qwen3.5-397B and GPT-5.4 — turning verification into a transition operator between research rounds and shipping open weights. The strongest agentic result today.

### 2. [[2607.21356]] Emergent Misalignment Recruits a Pre-existing Persona Subspace

- **推荐理由：** 从冻结 Qwen2.5-14B-Instruct 中提取出一个微调前就存在的低秩"人格子空间"，因果实验证明投影掉它可将失准率从 27.7% 降到 0.0%，注入未微调模型则剂量依赖地诱导失准（最高 45.4%），对"涌现式失准"给出了精确的机制性解释。
- **Why read:** Extracts a pre-existing low-rank "persona subspace" from a frozen model and causally shows that projecting it out during fine-tuning drops emergent misalignment from 27.7% to 0.0%, while injection induces it dose-dependently up to 45.4% — the cleanest mechanistic account of emergent misalignment to date.

### 3. [[2607.21075]] VibeVoice-ASR-BitNet Technical Report

- **推荐理由：** 微软团队对 VibeVoice-ASR 做异构量化（VAE 全 INT8 + LM BitNet 三值），将 4.62 GB 压到 1.58 GB，在仅 3 个 CPU 线程下实现 RTF<1 实时识别，比 Whisper.cpp 快 1.6–2.3×，是端侧语音部署的重要工程里程碑。
- **Why read:** Heterogeneous quantization (full-pipeline INT8 for the VAE tokenizer + BitNet ternary weights for the LM decoder) compresses VibeVoice-ASR from 4.62 GB to 1.58 GB and reaches real-time (RTF<1) on just 3 CPU threads, 1.6–2.3× faster than Whisper.cpp — a real edge-deployment milestone.

---

## 按主题分类 / Papers by Topic

### Mechanistic Interpretability / 机制可解释性

| Paper | Title | Description |
|-------|-------|-------------|
| [[2607.20803]] | Geometry of Personality | 将人格重构为荣格八种认知功能，激活引导实现八维同时可控，定位人格信息于中间层 / Recasts personality as 8 Jungian cognitive functions, achieves monotonic activation control and localizes personality to middle layers 7–12. |
| [[2607.20848]] | Auditing Evidence Use in Medical LLM Diagnosis | 行为审计协议追踪证据子集对诊断的影响，揭示准确率掩盖候选证据误用 / A behavioral audit traces how evidence subsets shift diagnostic margins, showing accuracy masks evidence misuse. |
| [[2607.20952]] | The Weight of Silence | 六条件因果干预证明 RL 改善的是权重鲁棒性而非让模型"读"隐式思维向量 / Six-condition causal interventions show RL improves weight robustness, not inference-time consultation of a latent scratchpad. |
| [[2607.20993]] | Sparse Concept Channels in 3D CT | 无训练探针发现每个放射学发现仅由约 10 个稀疏通道因果编码 / A training-free probe shows each clinical finding lives in ~10 causally necessary sparse channels in frozen 3D CT encoders. |
| [[2607.20995]] | Where Animacy Lives in LLMs | 用 EAP-IG 在四个模型定位"有生性电路"，Qwen 3 仅 1.74% 边即达 85% 忠实度 / EAP-IG isolates a causally sufficient animacy circuit across four LLMs; Qwen 3 hits 85% faithfulness with 1.74% of edges. |
| [[2607.21231]] | Progressive Cramming | 可靠压缩评测揭示"完美重建"≠"可迁移语义"，压缩嵌入劫持早期注意力而非稠密编码 / A reliable cramming protocol reveals perfect reconstruction hijacks early attention rather than encoding dense semantics; downstream tasks crash. |
| [[2607.21491]] | What, Where, and How in Code Models | 把"电路普适性"分解为三轴：What 由任务定、Where/How 由模型定 / Decomposes circuit universality into three axes — "what" is task-determined, "where/how" are model-determined across Qwen/DeepSeek coders. |

### Agents & Tool Use / 智能体与工具使用

| Paper | Title | Description |
|-------|-------|-------------|
| [[2607.20852]] | Code Monitor Red Teaming | 将"公开测试通过后残留 bug"建模为监控红队，弱验证器漏掉 80–94% 隐藏 bug / Models residual post-public-test bugs as monitor red-teaming; weak verifiers miss 80–94% of hidden bugs at 5% FPR. |
| [[2607.20891]] | Is Deep Research Reliable? | 误导知识使 Deep Research 智能体错误结论采纳率从 34.5% 飙升至 85.0% / Misleading evidence seeded before synthesis drives false-conclusion adoption from 34.5% cold-start to 85.0%. |
| [[2607.20982]] | GuardianAgentBench | 首个生产级框架上的 Agent 安全基准，最强配置仅 74.8 准确率 / First agent-safety benchmark on production frameworks (LangChain/LlamaIndex/Vectara); best config reaches only 74.8 accuracy. |
| [[2607.21125]] | Causal-AgentIR | 分层多智能体图像修复，因果记忆图使 PSNR 从 33.58 提升到 35.55 dB / Hierarchical six-agent image restoration with a self-evolving causal memory graph lifts PSNR from 33.58 to 35.55 dB. |
| [[2607.21173]] | Automated Synthesis of Causal Pipelines | 测试驱动的多智能体因果分析，把假设转为可执行测试以暴露有效性顾虑 / Test-driven multi-agent causal analysis converts assumptions into executable tests that surface validity concerns instead of silent bias. |
| [[2607.21461]] | AREX: Recursively Self-Improving Agent | 递归自改进深度研究智能体，BrowseComp 82.5 超 Qwen3.5-397B / Recursive self-improvement reaches 82.5 on BrowseComp, beating Qwen3.5-397B and GPT-5.4; open-weight. |
| [[2607.21495]] | Continuous Assurance for AI Agents | 为平民化 Agent 创建提出持续保障框架，9 类失效分类 + 5 要素治理 / A continuous-assurance framework (9-class failure taxonomy + 5 elements) for citizen-developer-created AI agents. |

### Safety & Alignment / 安全与对齐

| Paper | Title | Description |
|-------|-------|-------------|
| [[2607.20827]] | Auditing Provenance Sensitivity | 来源特异性授权审计发现 2.4% 案例仍保留对未授权证据的敏感性 / Target-specific authorization audit finds models retain sensitivity to unauthorized evidence in 2.4% of degradation comparisons. |
| [[2607.21063]] | QuantiBias | 量化让短形式安全控制不变，却使开放式刻板印象率升至 24–27% / Quantization leaves refusal/multiple-choice bias flat but raises open-ended stereotype rates to 24–27% across 8 languages. |
| [[2607.21151]] | V-DEAL: Video Safety De-Calibration | 三层诊断揭示"有害视频+良性查询"ASR 48.33%，无训练干预降至 0.80% / Three-layer diagnosis reveals harmful-video + benign-query ASR of 48.33%; a training-free intervention drops it to 0.80%. |
| [[2607.21353]] | Gradient Concentration Unlearning | SalUn 的显著性掩码与随机掩码统计等价，真正决定因素是梯度集中 / SalUn's saliency mask is statistically equivalent to a random mask; the real driver is gradient concentration (~92% in late layers). |
| [[2607.21356]] | Emergent Misalignment Persona Subspace | 预存人格子空间投影掉可将失准从 27.7% 降到 0.0% / Projecting out a pre-existing persona subspace drives emergent misalignment from 27.7% to 0.0%; injection induces it dose-dependently. |

### RL & Training Dynamics / 强化学习与训练动力学

| Paper | Title | Description |
|-------|-------|-------------|
| [[2607.21005]] | Weight-norm Criticality | 归一化+权重衰减使范数逼近零致 Hessian 爆炸，推导逐层稳定边界 / Normalization + weight decay shrink norms toward zero, exploding the Hessian; a layer-wise stability boundary predicts loss spikes. |
| [[2607.21089]] | Loss Landscape Topology in 3D Segmentation | 11 种不平衡方法中标准交叉熵即相当，不平衡严重程度塑造景观几何 / Standard CE matches 11 specialized imbalance methods; imbalance severity, not loss form, shapes the landscape geometry. |
| [[2607.21090]] | Self-Explanation Faithfulness RL | 将反事实忠实度转为 RL 奖励，忠实度相关系数从近零提升至 0.664 / Converting faithfulness into an RL reward lifts self-explanation faithfulness correlation from near-zero to 0.664. |
| [[2607.21273]] | Dark Room in the Reward Channel | GRPO 下稠密预测奖励将策略驱赶到"暗室"吸收态，须切到辅助损失通道 / Dense prediction rewards collapse GRPO agents into a "dark room" absorbing state; only the auxiliary-loss channel gains ~20 points. |
| [[2607.20822]] | Robust Asynchronous Q-Learning | BR-Async-Q 首次在奖励+状态联合污染下给出与标准 Q-learning 同阶误差界 / BR-Async-Q gives the first robust Q-learning bound under joint reward+state corruption matching vanilla Q-learning rates. |

### Quantization & Efficiency / 量化与效率

| Paper | Title | Description |
|-------|-------|-------------|
| [[2607.20806]] | Profiling Lightweight LLMs | PTME 四维实测表明静态代理能预测成本但无法预测精度 / PTME 4-axis measurement shows static proxies predict cost but not precision; Pareto analysis favors mid-size models at the edge. |
| [[2607.20981]] | Beyond Independent Optimization | 综述论证压缩/MoE 路由/量化构成故障传播链，提出 TRC 诊断指标 / Survey argues compression/MoE routing/quantization form a failure-propagation chain; proposes Temporal Routing Consistency. |
| [[2607.21075]] | VibeVoice-ASR-BitNet | 异构量化将 ASR 从 4.62 GB 压到 1.58 GB，3 线程 RTF<1 / Heterogeneous quantization compresses ASR from 4.62 to 1.58 GB, real-time on 3 CPU threads, 1.6–2.3× faster than Whisper.cpp. |
| [[2607.21076]] | C-PTQ for MLLMs | 对角 Fisher 矩阵对齐通道级量化误差与任务损失，Qwen2.5VL W3A16 达 77.1 / Diagonal Fisher weighting aligns channel quantization error with task loss; Qwen2.5VL-7B W3A16 reaches 77.1 average. |
| [[2607.21130]] | Float16 On-Device Training on RISC-V | 开源全 FP16 端侧训练库，内存降 50%，适配 Zvfh RISC-V 单核 / Open-source full-float16 on-device training for Zvfh RISC-V; ~50% memory reduction with minimal accuracy loss. |
| [[2607.21446]] | KroQuant for Diffusion Transformers | Kronecker 结构可逆变换替代 SmoothQuant，LPIPS 降 17.5%，内核快 14% / A learned Kronecker-structured transform replaces SmoothQuant for DiT W4A4; LPIPS down 17.5%, kernel 14% faster on MI350. |
| [[2607.21475]] | Error Certificates for KV-Cache Eviction | 证明确定性驱逐无法自估误差，Poisson 采样给出 0.97 覆盖率误差证书 / Proves deterministic eviction can't self-estimate error; a Poisson-sampled certificate achieves 0.97 coverage for attribution. |

### Evaluation & Benchmarks / 评测与基准

| Paper | Title | Description |
|-------|-------|-------------|
| [[2607.20864]] | Position Bias Hidden by Ceiling Effects | 穷举置换测试发现位置偏差仅在 60–95% 准确率"金发姑娘区"可检测 / Exhaustive permutation testing finds position bias detectable only in a 60–95% "Goldilocks zone"; frontier models sit above it. |
| [[2607.21010]] | Reexamining zero-shot Summarization | 稳定性分析协议发现 AlignScore 极不稳定，Gemma3-4B 最可信 / A stability protocol finds AlignScore highly unstable; Gemma3-4B is the most trustworthy small summarizer. |
| [[2607.21340]] | CM-LRS: Capital Markets LLM Reliability | 七维工作流输出层评分，闭源前沿模型聚于 0.22 分带，决策可用性区分度最大 / A 7-dimension workflow-output rubric; three frontier closed models cluster within 0.22 points, Decision Usefulness is the cleanest separator. |

### Test-Time Compute & Reasoning / 测试时计算与推理

| Paper | Title | Description |
|-------|-------|-------------|
| [[2607.21433]] | Token Budget Saturation in CoT | GSM8K/MATH 仅需 256 token 饱和，AIME 呈双峰失败，第 20 层可早退预测 / Accuracy saturates at 256 thinking tokens on GSM8K/MATH-500; a layer-20 probe detects non-convergence (AUC 0.608). |
| [[2607.21453]] | TTEL: Test-Time Scaling via Error Localization | 比较有/无反馈下 token 概率差异定位出错点，更少 token 更高 pass@k / Compares token probabilities with/without feedback to localize errors; fewer tokens yield higher pass@k on LiveCodeBench/AIME/HMMT. |

### Theory & Architecture / 理论与架构

| Paper | Title | Description |
|-------|-------|-------------|
| [[2607.20811]] | Tractability Frontiers for NNT | 给出 ReLU/线性神经网络训练的多项式时间上界，匹配已知下界 / Gives polynomial-time upper bounds for ReLU/linear network training, matching known lower bounds. |
| [[2607.20887]] | TwistedMerge for Model Merging | 将模型合并形式化为下降问题，三态认证证明环形不一致≠上同调障碍 / Recasts merging as a descent problem; a conservative 3-state certification shows cycle inconsistency ≠ cohomology obstruction. |
| [[2607.21351]] | How Many Bits Can an Adapter Write? | LoRA 每参数仅写 1.7–2.8 比特，隐私泄露随比特而非参数量增长 / Measures LoRA capacity at 1.7–2.8 bits/param; privacy leakage grows with bits written, not parameter count; GRPO writes almost nothing. |
| [[2607.21366]] | HOPE: Hilbert Operator Encoding | 将神经元建模为 Hilbert 空间算子，统一剪枝/合并/驱逐，data-free DEFT 迁移 / Models neurons as rank-1 Hilbert-Schmidt operators, unifying pruning/merging/eviction; data-free DEFT transfer beats EWC 4×. |
| [[2607.21405]] | Möbius RoPE | 反周期边界条件位置编码将 NIAH 方差压低 30.8×，零参数零 FLOPs / Anti-periodic positional encoding collapses NIAH variance by 30.8× with zero parameters and zero FLOPs — a within-window reliability fix. |

---

## All Papers

| arxiv_id | Title | Topic |
|----------|-------|-------|
| 2607.20803 | The Geometry of Personality: Activation Steering with Jungian Cognitive Functions | Mechanistic Interpretability |
| 2607.20806 | Profiling Lightweight Large Language Models | Quantization & Efficiency |
| 2607.20811 | New Complexity-Theoretic Frontiers of Tractability for Neural Network Training | Theory & Architecture |
| 2607.20822 | Robust Asynchronous Q-Learning under Reward and State Corruption via Batching | RL & Training Dynamics |
| 2607.20827 | Auditing Provenance Sensitivity in LLM Agent Action Selection | Safety & Alignment |
| 2607.20848 | Auditing Evidence Use in Medical LLM Diagnosis | Mechanistic Interpretability |
| 2607.20852 | Code Monitor Red Teaming for Public-Test-Passing Code | Agents & Tool Use |
| 2607.20864 | Position Bias is Hidden Behind Ceiling Effects: A Permutation Diagnostic for LLM Benchmarks | Evaluation & Benchmarks |
| 2607.20887 | TwistedMerge: Certified Higher-Order Diagnostics and Abstention for Model Merging | Theory & Architecture |
| 2607.20891 | Is Deep Research Reliable? Misleading Knowledge Induces False Conclusions | Agents & Tool Use |
| 2607.20952 | The Weight of Silence: A Causal Case for Weights Over the Scratchpad in Latent Chess Reasoning | Mechanistic Interpretability |
| 2607.20981 | Beyond Independent Optimization: Compression, MoE Routing, and Quantization Interactions in Multimodal Edge Intelligence | Quantization & Efficiency |
| 2607.20982 | GuardianAgentBench: Where Agents Fail and How to Guard Them | Agents & Tool Use |
| 2607.20993 | Sparse Concept Channels in Frozen 3D CT Vision Encoders | Mechanistic Interpretability |
| 2607.20995 | Where Animacy Lives in Large Language Models: Tracing the Circuits of the Animacy Concept | Mechanistic Interpretability |
| 2607.21005 | Weight-norm Criticality: A Mechanism for Loss Spikes Induced by Normalization and Weight Decay | RL & Training Dynamics |
| 2607.21010 | Reexamining zero-shot summarization: Empirical investigation of trustworthiness of LLM-summarizers | Evaluation & Benchmarks |
| 2607.21063 | QuantiBias: Benchmarking Quantization-Induced Bias in LLMs | Safety & Alignment |
| 2607.21075 | VibeVoice-ASR-BitNet Technical Report | Quantization & Efficiency |
| 2607.21076 | C-PTQ: Fisher-weighted Channel-wise Sensitivity for Post-training Quantization of MLLMs | Quantization & Efficiency |
| 2607.21089 | Loss Landscape Topology Reveals Why Simple Baselines are Competitive at 3D Point Cloud Segmentation Under Class Imbalance | RL & Training Dynamics |
| 2607.21090 | Training Large Language Models for Self-Explanation Faithfulness | RL & Training Dynamics |
| 2607.21125 | Causal-AgentIR: Self-Evolving Causal Memory for Adaptive Image Restoration Agents | Agents & Tool Use |
| 2607.21130 | Hardware-Software Co-Design for Float16 On-Device Training on RISC-V Single-Core | Quantization & Efficiency |
| 2607.21151 | V-DEAL: Diagnosing Video Safety De-Calibration as an Understanding–Refusal Coupling Failure | Safety & Alignment |
| 2607.21173 | Automated Synthesis and Adversarial Validation of Executable Causal Research Pipelines | Agents & Tool Use |
| 2607.21231 | Progressive Cramming: Reliable Token Compression and What It Reveals | Mechanistic Interpretability |
| 2607.21273 | The Dark Room in the Reward Channel: Dense Prediction Rewards Collapse GRPO-Trained LLM Agents | RL & Training Dynamics |
| 2607.21340 | Capital Markets LLM Reliability Score (CM-LRS): From Plausible to Bankable | Evaluation & Benchmarks |
| 2607.21351 | How Many Bits Can an Adapter Write? Measuring the Capacity and Memorization of PEFT | Theory & Architecture |
| 2607.21353 | Gradient Concentration, Not Weight Saliency, Explains Representation-Level Class Unlearning | Safety & Alignment |
| 2607.21356 | Emergent Misalignment Recruits a Pre-existing Persona Subspace | Safety & Alignment |
| 2607.21366 | HOPE: A Mathematical Framework for Deconstructing Learned Representations in Deep Networks | Theory & Architecture |
| 2607.21405 | Anti-Periodic Positional Encoding: Möbius Boundary Conditions Make In-Context Retrieval Reliable | Theory & Architecture |
| 2607.21433 | Token Budget Saturation and Mechanistic Early-Detection of Reasoning Non-Convergence in CoT Models | Test-Time Compute & Reasoning |
| 2607.21446 | KroQuant: Kronecker-Structured Block Transforms for Efficient PTQ of Diffusion Transformers | Quantization & Efficiency |
| 2607.21453 | Test-Time Scaling via Error Localization | Test-Time Compute & Reasoning |
| 2607.21461 | AREX: Towards a Recursively Self-Improving Agent for Deep Research | Agents & Tool Use |
| 2607.21475 | Error Certificates for KV-Cache Eviction via Randomized Design | Quantization & Efficiency |
| 2607.21491 | What, Where, and How: Disentangling the Roles of Task, Language, and Model in Code Model Representations | Mechanistic Interpretability |
| 2607.21495 | Toward Continuous Assurance for the Democratization of AI Agent Creation in Industry | Agents & Tool Use |

---

**Verification:** 41 papers in this overview match 41 `.md` files in the directory (excluding overview.md itself). No discrepancy.
