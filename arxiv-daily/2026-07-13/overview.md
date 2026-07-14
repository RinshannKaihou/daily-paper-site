---
title: "Daily arXiv Digest — 2026-07-13"
date: 2026-07-13
tags: [agents, safety, theory, interpretability, efficiency, quantization, training, reasoning, evaluation, calibration, multimodal, scaling-laws]
papers: 44
---

## 今日必读 / Must Read Today

1. **[[2607.11288]] Mako: A Self-Evolving Agentic Operating System (SE-AOS) for Autonomous Web Exploitation** — 提出自进化智能体操作系统架构，把"能力"当作运行时可热加载的可变内核，在 XBOW-104 取得 104/104 全覆盖，揭示了"能力而非推理才是成熟系统的瓶颈" / A paradigm-shifting self-evolving agentic OS that treats exploit capability as a mutable runtime kernel, achieving 104/104 on XBOW-104 and showing capability — not reasoning — is the real bottleneck.
2. **[[2607.11598]] Interaction Scaling: Grounding the Third Axis of Test-Time Compute** — 用数据处理不等式证明推理与采样两轴必然饱和，唯有"接地交互"能突破内部上限，硬代码任务从 66.7% 拉到 100% / A foundational reframe of test-time compute into three axes, proving via the data-processing inequality that only grounded external interaction can break the internal ceiling (66.7%→100%).
3. **[[2607.11052]] Domain-Aware Scaling Laws Uncover Data Synergy** — 用一阶/二阶协同系数量化预训练数据混合的协同与干扰，实测最优混合较反最优在 HumanEval 上带来 31–38% BPB 改善 / Quantifies pretraining data synergy via first/second-order coefficients, validated by a 31–38% BPB gap between optimal and anti-optimal mixtures on HumanEval.

## 按主题分类 / Papers by Topic

### 智能体系统 / Agents & Agentic Systems

| ID | Title | 一句话总结 / Summary |
|----|-------|---------------------|
| [[2607.11084]] | NVAITC AI Scientist: A Governed End-to-End Research System — A Hypertension GWAS Case Study | 治理优先的端到端智能体研究系统，28.6 万人高血压 GWAS 复现 FGF5 等位点，DILI AUC 提至 0.842 / Governed agentic system replicates hypertension GWAS loci (FGF5) on 286k people; lifts DILI AUC to 0.842. |
| [[2607.11098]] | AgentCheck: A Reproduce–Intervene–Mitigate Workbench for LLM Agents over MCP | 把 MCP 变成可干预故障注入面，最强 agent 105/120、最弱 77/120，陈旧数据故障无法缓解 / Turns MCP into a fault-injection surface; 28pt agent spread, stale-data faults unmitigable. |
| [[2607.11149]] | The Hidden Footprint: Making Storage a First-Class Metric for LLM Agent Evaluation | 首个跨框架智能体存储足迹基准，同等精度下留存字节相差 15.7× / First cross-framework agent storage-footprint benchmark; 15.7× persisted-byte spread at identical accuracy. |
| [[2607.11175]] | The Path to Self-Evolving Clinical Systems: Scaling Medical Agents from Assistance to Autonomy | 综述：医学影像 agent 三级自治分类与"框架/能力/环境"三轴 scaling / Survey: medical-imaging agents via three-level autonomy & framework/capability/environment scaling spine. |
| [[2607.11250]] | Multi-Agent LLMs Fail to Explore Each Other | 当前 LLM 智能体过早承诺、不探索对方，MACE (LinUCB) 显著降遗憾 / LLM agents fail to explore peers; MACE cuts regret and lifts HotpotQA EM. |
| [[2607.11388]] | StructAgent: Harness Long-horizon Digital Agents with Unified Causal Structure | 统一状态+结构化工作流，OSWorld-Verified 78.9% 开源 SOTA / Unified verifier-backed task state; OSWorld-Verified 78.9% open-source SOTA (+30.6 on 27B). |

### 智能体安全与红队 / Agent Safety, Security & Red-Teaming

| ID | Title | 一句话总结 / Summary |
|----|-------|---------------------|
| [[2607.11226]] | Heterogeneous Agent Cohorts for Safe Open-Ended Exploration with Runtime Constraint Memory | 异构小队分离探索与安全，AgentHarm 0% 越界 vs ReAct 14.2% / Heterogeneous cohort separates exploration from safety; 0% breach on AgentHarm vs 14.2% ReAct. |
| [[2607.11288]] | Mako: A Self-Evolving Agentic Operating System (SE-AOS) for Autonomous Web Exploitation | 自进化智能体 OS 在 XBOW-104 取 104/104 全覆盖，能力而非推理是瓶颈 / Self-evolving agentic OS hits 104/104 on XBOW-104; capability — not reasoning — is the bottleneck. |
| [[2607.11475]] | HyperSafe: Inference-Time Safety Recovery for Fine-Tuned Language Models | 超网络从激活指纹生成安全侧网络，有害率 19–31%→<1% / Hypernetwork-generated side-network cuts harmful rate 19–31%→<1% without touching weights. |
| [[2607.11698]] | Agent Hacks Agent: Autoresearch for Production-Agent Red-Teaming | 把生产级智能体红队重构成自动研究循环，冻结 VCG 单次部署 ASR 47.0% / Reframes agent red-teaming as autoresearch; frozen VCG reaches 47.0% held-out ASR. |
| [[2607.11751]] | When Local Monitors Miss Compositional Harm: Diagnosing Distributed Backdoors in Multi-Agent Systems | 分布式后门突破局部监控可观测性边界，解码视图门把 ASR 1.00→0.00 / Distributed backdoors beat local monitors; decoded-view gate drops ASR 1.00→0.00. |

### 理论与训练动力学 / Theory & Training Dynamics

| ID | Title | 一句话总结 / Summary |
|----|-------|---------------------|
| [[2607.11116]] | The Equilibrium Is the Initialization: Lazy Identity Collapse in Physics-Structured Deep Equilibrium Reasoning | 负面结果：port-Hamiltonian DEQ 均衡点等于初始点，隐式计算是空操作 / Negative result: port-Hamiltonian DEQ equilibrium equals init; implicit compute is a silent no-op. |
| [[2607.11122]] | Implicit Neural Networks as Static Controllers: Certificates and Performance Separation | 隐式神经控制器稳定性/LQ 性能可写成 LMI，静态 ReLU 严格优于有限阶动态线性控制器 / Implicit neural controllers give LMI certificates; static ReLU provably beats finite-order dynamic linear controllers. |
| [[2607.11289]] | Backpropagation as a Nilpotent Linear System | 将反向传播重写为幂零线性系统，Neumann 级数恰 L 项终止 / Backprop recast as a nilpotent linear system; Neumann series terminates in exactly L terms. |
| [[2607.11666]] | How to Tame Grokking: Representation Geometry as a Control Signal | GeomDR 几何正则化器加速 grokking 最多 52.5× / GeomDR spectral regularizer accelerates grokking up to 52.5×. |
| [[2607.11875]] | Invariant Learning Dynamics of Transformers in Inductive Reasoning Tasks | 归纳推理任务中 Transformer 的低维不变流形，刻画 ICL/IWL 电路竞争 / Invariant manifold traps GD trajectories in inductive-reasoning Transformers; ICL/IWL circuit competition. |

### 可解释性与机制分析 / Interpretability & Mechanistic Analysis

| ID | Title | 一句话总结 / Summary |
|----|-------|---------------------|
| [[2607.11081]] | Controlling Motion Transfer in Diffusion Transformers via Attention Heads | 首次发现视频 DiT 中运动/结构专用注意力头，免训练 HALO 运动保真度 62.5→66.2 / First discovery of motion/structure attention heads in video DiT; training-free HALO lifts motion fidelity 62.5→66.2. |
| [[2607.11327]] | PRISM Edit: One Vector for All Temporal Answers | 写入单个多义向量处理时序知识，TC/CRS 较最强基线 +23.3/+33.7 / Writes one polysemous vector for temporal knowledge; +23.3 TC / +33.7 CRS over best baseline. |
| [[2607.11347]] | From Neural Network Decisions to Training Cases: An Exact Account via Case-Based Decision Theory | 证明 OLS 读出层可精确分解为训练样本回报加权和，免再训练审计 / Exact case-based decomposition of OLS readout; retraining-free audit (Top-30 consistency 0.941). |
| [[2607.11541]] | Random Label Prediction Heads for Studying Memorization in Deep Neural Networks | 随机标签头作为记忆度量，正则化 ImageNet 67.0%→68.5% 但欠采样 CIFAR 反而有害 / Random-label head measures memorization; +1.5% ImageNet but hurts undersampled CIFAR. |
| [[2607.11796]] | An Exact Instrument for State Usage in Selective State-Space Models, and the Input-Driven Migration It Reveals | Mamba SSM 的精确状态使用测量工具，揭示随输入的模式迁移 / Exact Mamba state-usage instrument reveals input-driven mode migration; matches full model at half budget. |
| [[2607.11871]] | Inside the Unfair Judge: A Mechanistic Interpretability Account of LLM-as-Judge Bias | 表示层解释评判偏差，双向引导恢复公平，未见基准预测 AUC 0.82 / Representation-level account of judge bias; steering restores fairness, predicts failure AUC 0.82. |

### 效率、系统与量化 / Efficiency, Systems & Quantization

| ID | Title | 一句话总结 / Summary |
|----|-------|---------------------|
| [[2607.11211]] | FastTPS: An Optimized Method for LLM Token Phase for AI Accelerators | 在 AMD NPU 上把 LLM 解码推至 92.77% 理论峰值，端到端 5.95× 加速 / Pushes LLM decode to 92.77% theoretical peak on AMD NPU (5.95× end-to-end). |
| [[2607.11317]] | Calibrated e-CUSUM Decoding for Quantized Reasoning Models | 校准 e-CUSUM 控制器把量化模型解码监控误报从 93–95% 降至可用水平 / Calibrated e-CUSUM controller makes the decoding monitor for quantized reasoning models usable (FP 93–95%→selective). |
| [[2607.11359]] | Efficient Tuning Before Low-Bit Post-Training Quantization for SGD-optimized Models | ETBQ 在 PTQ 前注入量化误差扰动，ImageNet MobileNetV2 W2A4 +8.53% / Pre-conditions before PTQ; +8.53% on ImageNet MobileNetV2 W2A4. |
| [[2607.11368]] | Decomposing Runtime, Kernel, and Quantization Speedups via a Matched FP16 Intermediate | 用匹配 FP16 基线拆分 vLLM-Marlin 加速，运行时占 2/3 对数增益 / Matched FP16 baseline decomposes vLLM-Marlin speedup; runtime carries 2/3 of log-gain. |
| [[2607.11586]] | HCRMap: Pressure-Aware Hot-Expert Residency Mapping for 3.5D MoE Chiplet Inference | 双时间尺度热专家驻留映射，MoE 推理延迟较基线降 34.5%/33.1% / Dual-timescale hot-expert residency; cuts MoE latency 34.5%/33.1% over baselines. |

### 训练、微调与数据缩放 / Training, Finetuning & Data Scaling

| ID | Title | 一句话总结 / Summary |
|----|-------|---------------------|
| [[2607.10970]] | Enhanced Byzantine-Robust Federated Learning Via Truncated-Quadratic Loss for Heterogeneous Data | 截断二次 (TQ) 损失聚合器达阶最优鲁棒性，MNIST ρ=0.5 下 91.5% vs Huber 9.8% / Truncated-Quadratic loss aggregator clips outliers for order-optimal Byzantine robustness (91.5% vs 9.8% Huber). |
| [[2607.11052]] | Domain-Aware Scaling Laws Uncover Data Synergy | 领域感知缩放律量化数据协同，最优 vs 反最优 HumanEval 改善 31–38% BPB / Domain-aware scaling laws quantify data synergy; 31–38% BPB gap optimal vs anti-optimal on HumanEval. |
| [[2607.11163]] | Unified Gradient Projection: Language-Balanced Continual Learning for Multilingual Low-Resource ASR | UGP 语言均衡参考梯度正交投影，多语 ASR 遗忘 4.11%→0.04% / Language-balanced reference-gradient projection; multilingual ASR forgetting 4.11%→0.04%. |
| [[2607.11193]] | REPTRAN: Search-Based Repair of Transformer Models | 搜索式修复 Transformer FFN，平均修复率 74.7% vs ARACHNE 17.1% / Search-based Transformer repair; 74.7% repair rate vs ARACHNE's 17.1%. |
| [[2607.11267]] | Enhancing LLMs through human feedback: a journey towards self-improvement | FLARE 双路检索注入用户反馈，Trivia 评分 3.06→3.91 / FLARE injects user feedback via dual retrieval; Trivia 3.06→3.91. |
| [[2607.11444]] | Unlocking Every Expert in Domain-Specific Training | UMoE 重组专家池后再 SFT，数学均分 +3.40、SWE-bench +6.0 / Reorganizes MoE expert pool before SFT; +3.40 math avg, +6.0 SWE-bench, no extra inference cost. |

### 推理、可靠性与测试时计算 / Reasoning, Reliability & Test-Time

| ID | Title | 一句话总结 / Summary |
|----|-------|---------------------|
| [[2607.11022]] | When the Reward Suite Is Leaky: A Preregistered Causal Contrast of Natural Verifier False Positives in RLVR | 预注册因果对照显示 MBPP 泄漏奖励损害在 1–1.5B/400 步内被限制在 1.5pt，约半数为真实错误代码买单 / Preregistered causal study bounds reward-leak harm to ≤1.5pt at 1–1.5B/400 steps; ~47% pays for wrong code. |
| [[2607.11266]] | Valid ≠ Necessary: Diagnosing Latent Inefficiency in Chain-of-Thought | 评估器只判对错不判必要，PACE 压缩 token 降 31–53% 精度基本不变 / Evaluators miss "valid but unnecessary" CoT steps; PACE cuts tokens 31–53% near-zero loss. |
| [[2607.11414]] | Confidently Wrong: Detecting Hallucinations in Financial Question Answering from LLM Internal States | 残差流线性探针检测金融问答幻觉，自信答案 AUROC +0.13~0.15 / Residual-stream probes detect "confidently wrong" finance-QA hallucinations (+0.13–0.15 AUROC). |
| [[2607.11598]] | Interaction Scaling: Grounding the Third Axis of Test-Time Compute | 把测试时计算归纳为三轴，接地交互把硬代码任务 66.7%→100% / Frames test-time compute as 3 axes; grounded interaction lifts hard-code 66.7%→100%. |
| [[2607.11607]] | Auditing the Risk Claims of Distributional Reinforcement Learning | 决策级审计分布式 RL，40–95% 的"最强风险权衡"声明被证伪 / Decision-level audit refutes 40–95% of distributional-RL's strongest risk-tradeoff claims. |

### 评估、校准、基准与多模态 / Evaluation, Calibration, Benchmarks & Multimodal

| ID | Title | 一句话总结 / Summary |
|----|-------|---------------------|
| [[2607.11007]] | TabPFN beyond Tabular Data: Calibration and Accuracy on Multimodal Embeddings | TabPFN 作零训练分类头接冻结多模态编码器，NLL/ECE 平均最佳排名 / TabPFN as training-free head on frozen multimodal encoders wins best mean rank on NLL & ECE (ECE 2.1–5.3× lower). |
| [[2607.11079]] | Are LLMs Ready for Scientific Discovery? A Capability-Oriented Benchmark for AI Scientists | SDABench 以六种科学推理能力评测，模型在机制/因果任务断崖式下降，跨度>50pt / Probes six scientific-reasoning capabilities; frontier models cliff-drop on causal/mechanistic tasks (>50pt spread). |
| [[2607.11170]] | TC-MAF: Train-Calibrated Bounded Multi-Evidence Fusion for Multimodal Industrial Anomaly Detection | 像素级凸融合多模态证据，MVTec-3D 达 0.979 I-AUROC / Convex-fuses multimodal evidence; 0.979 I-AUROC on MVTec-3D. |
| [[2607.11214]] | A Novel Method to Evaluate Models on Unreliable, Noisy and Inconsistent Labels: Adaptive Resolution Label Aggregation (ARLA) | 推理时按子块重采样+阈值抑制标签噪声，洪水分割 precision 0.52→0.80 / Inference-time subpatch re-binning denoises labels; precision 0.52→0.80. |
| [[2607.11542]] | Condition-Stratified Robustness Analysis of Post-Hoc Calibration Methods for Probabilistic Classifiers | 预注册条件分层分析温度缩放 vs 保序回归，结论高度依赖条件与指标 / Pre-registered condition-stratified study; TEMP directionally better but conclusion condition/metric-dependent. |
| [[2607.11801]] | Encoder-Side Neuron Identification and Amplification for Acoustic Perception in Large Audio-Language Models | IAAN 推理时放大编码器音频感知神经元，VoxParadox +25.7 pp / Amplifies encoder audio neurons at inference; +25.7 pp on VoxParadox. |

## All Papers

| ID | Title | Topic | Relevance |
|----|-------|-------|-----------|
| [[2607.10970]] | Enhanced Byzantine-Robust Federated Learning Via Truncated-Quadratic Loss for Heterogeneous Data | Training / 训练 | 拜占庭鲁棒联邦学习 / Byzantine-robust FL |
| [[2607.11007]] | TabPFN beyond Tabular Data: Calibration and Accuracy on Multimodal Embeddings | Evaluation / 评估 | 零训练校准分类头 / Training-free calibrated head |
| [[2607.11022]] | When the Reward Suite Is Leaky: A Preregistered Causal Contrast of Natural Verifier False Positives in RLVR | Reasoning / 推理 | RLVR 奖励泄漏因果分析 / RLVR reward-leak causality |
| [[2607.11052]] | Domain-Aware Scaling Laws Uncover Data Synergy | Training / 训练 | 领域感知缩放律 / Domain-aware scaling laws |
| [[2607.11079]] | Are LLMs Ready for Scientific Discovery? A Capability-Oriented Benchmark for AI Scientists | Evaluation / 评估 | 科学发现能力基准 / Scientific-discovery benchmark |
| [[2607.11081]] | Controlling Motion Transfer in Diffusion Transformers via Attention Heads | Interpretability / 可解释性 | 视频 DiT 运动注意力头 / Video-DiT motion heads |
| [[2607.11084]] | NVAITC AI Scientist: A Governed End-to-End Research System — A Hypertension GWAS Case Study | Agents / 智能体 | 治理优先医学智能体 / Governed medical agent |
| [[2607.11098]] | AgentCheck: A Reproduce–Intervene–Mitigate Workbench for LLM Agents over MCP | Agents / 智能体 | MCP 故障注入工作台 / MCP fault-injection workbench |
| [[2607.11116]] | The Equilibrium Is the Initialization: Lazy Identity Collapse in Physics-Structured Deep Equilibrium Reasoning | Theory / 理论 | DEQ 隐式计算空操作 / DEQ implicit no-op |
| [[2607.11122]] | Implicit Neural Networks as Static Controllers: Certificates and Performance Separation | Theory / 理论 | 隐式控制器 LMI 证书 / Implicit-controller LMI certificates |
| [[2607.11149]] | The Hidden Footprint: Making Storage a First-Class Metric for LLM Agent Evaluation | Agents / 智能体 | 智能体存储足迹基准 / Agent storage footprint |
| [[2607.11163]] | Unified Gradient Projection: Language-Balanced Continual Learning for Multilingual Low-Resource ASR | Training / 训练 | 多语 ASR 持续学习 / Multilingual ASR continual learning |
| [[2607.11170]] | TC-MAF: Train-Calibrated Bounded Multi-Evidence Fusion for Multimodal Industrial Anomaly Detection | Evaluation / 评估 | 多模态工业异常检测 / Multimodal anomaly detection |
| [[2607.11175]] | The Path to Self-Evolving Clinical Systems: Scaling Medical Agents from Assistance to Autonomy | Agents / 智能体 | 医学智能体综述 / Medical agents survey |
| [[2607.11193]] | REPTRAN: Search-Based Repair of Transformer Models | Training / 训练 | Transformer 模型修复 / Transformer model repair |
| [[2607.11211]] | FastTPS: An Optimized Method for LLM Token Phase for AI Accelerators | Efficiency / 效率 | LLM 解码 NPU 加速 / LLM decode NPU speedup |
| [[2607.11214]] | A Novel Method to Evaluate Models on Unreliable, Noisy and Inconsistent Labels (ARLA) | Evaluation / 评估 | 噪声标签评估 / Noisy-label evaluation |
| [[2607.11226]] | Heterogeneous Agent Cohorts for Safe Open-Ended Exploration with Runtime Constraint Memory | Safety / 安全 | 异构安全探索小队 / Heterogeneous safe-exploration cohort |
| [[2607.11250]] | Multi-Agent LLMs Fail to Explore Each Other | Agents / 智能体 | 多智能体探索缺陷 / Multi-agent exploration failure |
| [[2607.11266]] | Valid ≠ Necessary: Diagnosing Latent Inefficiency in Chain-of-Thought | Reasoning / 推理 | CoT 冗余压缩 / CoT redundancy compression |
| [[2607.11267]] | Enhancing LLMs through human feedback: a journey towards self-improvement | Training / 训练 | 反馈驱动 RAG / Feedback-driven RAG |
| [[2607.11288]] | Mako: A Self-Evolving Agentic Operating System (SE-AOS) for Autonomous Web Exploitation | Safety / 安全 | 自进化智能体 OS / Self-evolving agentic OS |
| [[2607.11289]] | Backpropagation as a Nilpotent Linear System | Theory / 理论 | 反向传播幂零系统 / Nilpotent backprop system |
| [[2607.11317]] | Calibrated e-CUSUM Decoding for Quantized Reasoning Models | Efficiency / 效率 | 量化推理解码监控 / Quantized-reasoning decode monitor |
| [[2607.11327]] | PRISM Edit: One Vector for All Temporal Answers | Interpretability / 可解释性 | 时序知识单向量编辑 / Temporal knowledge single-vector edit |
| [[2607.11347]] | From Neural Network Decisions to Training Cases: An Exact Account via Case-Based Decision Theory | Interpretability / 可解释性 | 精确案例归因审计 / Exact case-based audit |
| [[2607.11359]] | Efficient Tuning Before Low-Bit Post-Training Quantization for SGD-optimized Models | Efficiency / 效率 | PTQ 前预条件调参 / Pre-PTQ conditioning |
| [[2607.11368]] | Decomposing Runtime, Kernel, and Quantization Speedups via a Matched FP16 Intermediate | Efficiency / 效率 | 推理加速归因 / Inference speedup attribution |
| [[2607.11388]] | StructAgent: Harness Long-horizon Digital Agents with Unified Causal Structure | Agents / 智能体 | 长程数字智能体 / Long-horizon digital agent |
| [[2607.11414]] | Confidently Wrong: Detecting Hallucinations in Financial Question Answering from LLM Internal States | Reasoning / 推理 | 金融问答幻觉检测 / Finance-QA hallucination detection |
| [[2607.11444]] | Unlocking Every Expert in Domain-Specific Training | Training / 训练 | MoE 专家池重组 / MoE expert-pool reorganization |
| [[2607.11475]] | HyperSafe: Inference-Time Safety Recovery for Fine-Tuned Language Models | Safety / 安全 | 推理时安全恢复 / Inference-time safety recovery |
| [[2607.11541]] | Random Label Prediction Heads for Studying Memorization in Deep Neural Networks | Interpretability / 可解释性 | 记忆度量与正则化 / Memorization metric & regularization |
| [[2607.11542]] | Condition-Stratified Robustness Analysis of Post-Hoc Calibration Methods for Probabilistic Classifiers | Evaluation / 评估 | 后校准稳健性分析 / Post-hoc calibration robustness |
| [[2607.11586]] | HCRMap: Pressure-Aware Hot-Expert Residency Mapping for 3.5D MoE Chiplet Inference | Efficiency / 效率 | MoE chiplet 专家驻留 / MoE chiplet expert residency |
| [[2607.11598]] | Interaction Scaling: Grounding the Third Axis of Test-Time Compute | Reasoning / 推理 | 测试时交互缩放 / Test-time interaction scaling |
| [[2607.11607]] | Auditing the Risk Claims of Distributional Reinforcement Learning | Reasoning / 推理 | 分布式 RL 风险审计 / Distributional-RL risk audit |
| [[2607.11666]] | How to Tame Grokking: Representation Geometry as a Control Signal | Theory / 理论 | 几何正则加速 grokking / Geometry-accelerated grokking |
| [[2607.11698]] | Agent Hacks Agent: Autoresearch for Production-Agent Red-Teaming | Safety / 安全 | 生产智能体红队 / Production-agent red-teaming |
| [[2607.11751]] | When Local Monitors Miss Compositional Harm: Diagnosing Distributed Backdoors in Multi-Agent Systems | Safety / 安全 | 分布式后门检测 / Distributed backdoor detection |
| [[2607.11796]] | An Exact Instrument for State Usage in Selective State-Space Models, and the Input-Driven Migration It Reveals | Interpretability / 可解释性 | Mamba 状态使用工具 / Mamba state-usage instrument |
| [[2607.11801]] | Encoder-Side Neuron Identification and Amplification for Acoustic Perception in Large Audio-Language Models | Evaluation / 评估 | 音频 LALM 神经元放大 / Audio-LALM neuron amplification |
| [[2607.11871]] | Inside the Unfair Judge: A Mechanistic Interpretability Account of LLM-as-Judge Bias | Interpretability / 可解释性 | 评判偏差机制解释 / Judge-bias mechanism |
| [[2607.11875]] | Invariant Learning Dynamics of Transformers in Inductive Reasoning Tasks | Theory / 理论 | 归纳推理不变流形 / Inductive-reasoning invariant manifold |
