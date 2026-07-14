---
title: "Daily arXiv Digest — 2026-07-02"
date: 2026-07-02
tags:
  - llm-safety
  - mechanistic-interpretability
  - agent-systems
  - autonomous-science
  - inference-efficiency
  - training-systems
  - evaluation
  - uncertainty
  - scientific-ml
papers: 26
---

# Daily arXiv Digest — 2026-07-02

> 本日共收录 26 篇论文，覆盖 LLM 安全、机制可解释性、智能体系统、自主科研、推理效率、训练系统、评测与不确定性等方向。
> 26 papers curated today, spanning LLM safety, mechanistic interpretability, agent systems, autonomous science, inference efficiency, training systems, evaluation, and uncertainty.

---

## 今日必读 / Must Read Today

### 1. [[2607.01612]] Scaling with Confidence: Calibrating Confidence of LLMs for Adaptive Test Time Scaling

> **推荐理由：** C3RL 通过"正确性+校准+数据集先验参考准确率"三联奖励，在不损失准确率的前提下获得良好校准的言语化置信度；基于此的 CAS 自适应推理策略在 OOD 文本上实现 12.33× 推理预算缩减，对实际 LLM 部署具有直接且显著的工程价值。
>
> **Why read:** C3RL's three-term RL reward yields well-calibrated verbalized confidence without accuracy loss, and the CAS adaptive inference policy achieves up to 12.33× inference budget reduction at matched accuracy — a directly deployable, money-saving result that unifies confidence calibration with test-time compute scaling.

### 2. [[2607.01844]] Mixture-of-Parallelisms: Towards Memory-Efficient Training Stack for Mixture-of-Experts Models

> **推荐理由：** MoP 用"组件特化并行 + 重叠子群"的设计，在仅 12 个 8×H200 节点上无损训练万亿参数、百万上下文 MoE 模型，相对已调优 FSDP2 实现单 GPU 4.7×–8.2× 吞吐提升，大幅降低了前沿大模型训练的硬件门槛。
>
> **Why read:** MoP's component-specialized parallelism trains trillion-parameter, 1M-context MoE models on fewer than 96 H200 GPUs, delivering 4.7×–8.2× per-GPU throughput over a strongly-tuned FSDP2 baseline — a potentially high-impact systems contribution for frontier-scale training.

### 3. [[2607.01793]] Safety Testing LLM Agents at Scale: From Risk Discovery to Evidence-Grounded Verification

> **推荐理由：** Vera 将软件工程测试原则迁移到非确定性 LLM Agent，构建了 1,600 条可执行安全案例（124 风险 × 77 攻击 × 30 环境），在 Claude Code/Codex 等四个生产级框架上获得 93.9% 多通道攻击成功率，并发现"能力越强越易受攻击"的对齐悖论，是 Agent 安全评测领域的重要基准。
>
> **Why read:** Vera operationalizes software-testing principles for non-deterministic LLM agents with 1,600 executable safety cases, achieving 93.9% multi-channel attack success on four production agent frameworks and surfacing the alarming "capability–vulnerability alignment" finding — an essential benchmark for agent safety research.

---

## 按主题分类 / Papers by Topic

### 🛡️ LLM 安全与对齐 / LLM Safety & Alignment

| Paper | Description |
|---|---|
| [[2607.01793]] Vera | 可执行安全案例基准：124 风险 × 77 攻击 × 30 环境，多通道攻击成功率 93.9%。Executable safety-case benchmark: 124 risks × 77 attacks × 30 environments, 93.9% multi-channel ASR on production agents. |
| [[2607.01854]] Abliteration Audit | 双信号检查点审计检测去拒绝化，AUROC 0.95；诚实披露伪造参考零训练绕过。Two-signal checkpoint audit detects abliteration at AUROC 0.95; honestly documents spoofed-reference zero-training bypass. |
| [[2607.02072]] kNNGuard | 无训练防护栏，基于激活空间 kNN，仅 50 样本/类即达 87.4% F1，域适应 8 秒。Training-free guardrail via activation-space kNN, 87.4% F1 with 50 samples/class, domain adaptation in 8 seconds. |
| [[2607.01951]] Robust for Wrong Reasons | 表征几何视角揭示"稳健但未感知信号"现象，疫苗域稳健性可反转。Representational geometry reveals "accidental robustness"; vaccine-domain resistance can reverse under skepticism. |
| [[2607.01802]] Steering Vectors Limits | 系统刻画导向向量的泛化瓶颈：任务迁移脆弱、多向量组合下降 15–40%。Systematically characterizes steering-vector limits: fragile task transfer, 15–40% composition degradation. |
| [[2607.02210]] GRV Framework | 电信自治网络 AI 决策的分级运行时验证，纯架构设计无实证。Tiered runtime guard-rail validation for autonomous telecom networks; architecture-only, no empirical evaluation. |

### 🔬 机制可解释性 / Mechanistic Interpretability

| Paper | Description |
|---|---|
| [[2607.01940]] CoAx | 条件共消融评分恢复自我修复备份头，ROC-AUC 0.33→0.91，无标签迁移 8 模型。Conditional Co-Ablation recovers self-repair backup heads (ROC-AUC 0.33→0.91), label-free transfer across 8 models. |
| [[2607.01799]] Expander SAEs | 扩展图掩码将 SAE 解码器参数降 293×，保留 84% 稠密恢复率。Expander-graph mask cuts SAE decoder parameters 293× while retaining 84% dense CE recovery. |
| [[2607.01571]] Geometric Signatures of Reasoning | 谱有效维度 d_ρ 度量 CoT 轨迹复杂度，0.93 AUC 区分难题/易题。Spectral effective dimension d_ρ measures CoT complexity, 0.93 AUC separating hard/easy problems. |

### 🤖 智能体系统与记忆 / Agent Systems & Memory

| Paper | Description |
|---|---|
| [[2607.01919]] ElephantAgent | 基于 TEE 的可验证状态连续性，确定性防御工具/记忆投毒，开销仅 1.02–1.04×。TEE-based verifiable state continuity, deterministically rejects tool/memory poisoning at 1.02–1.04× overhead. |
| [[2607.01935]] A-TMA | "幽灵记忆"问题形式化 + 三层解耦评估 + 状态感知覆盖层，冲突准确率 0.480→0.720。Formalizes "ghost memory" + three-level decoupled evaluation + state-aware overlay, conflict accuracy 0.480→0.720. |
| [[2607.01874]] SkillCoach | 自进化 rubric 评估 Agent 技能使用，暴露被准确率掩盖的失败，SFT 提升 24–32%。Self-evolving rubrics evaluate agentic skill-use, exposing accuracy-hidden failures, SFT gains 24–32%. |
| [[2607.01846]] CLAP | 领域智能体后训练闭环治理：数据治理、双阶段门控、应用链回放。Closed-loop governance for domain-agent post-training: data normalization, two-gate control, application-chain replay. |

### 🔬 自主科研与编程智能体 / Autonomous Science & Coding Agents

| Paper | Description |
|---|---|
| [[2607.02329]] Grounded Autonomous Research | 从 11k 论文到手稿的端到端容错 LLM 物理科研流水线，发现新压磁效应。End-to-end fault-tolerant LLM pipeline from 11k papers to manuscript, discovering novel piezomagnetic effects. |
| [[2607.01639]] TrafficSci | LLM 智能体闭环自主发现交通定律，复现 3 条已知定律 + 发现新时间记忆尺度 τ。LLM-agent closed-loop autonomously rediscovers 3 traffic laws + discovers new temporal-memory scale τ. |
| [[2607.02134]] Coding-agents Replicate Papers | 论文复制工作流（coding-agent skill），12 次运行 158 目标全部通过门控。Paper-replication workflow as coding-agent skill; 12 runs, 158 targets all pass completion gate. |
| [[2607.02186]] UA-ChatDev | ChatDev 子任务间插入不确定性门控，SRDD 质量 0.395→0.649，开销约 2×。Uncertainty gating between ChatDev subtasks lifts quality 0.395→0.649 at ~2× cost. |

### ⚡ 推理效率与测试时计算 / Inference Efficiency & Test-time Compute

| Paper | Description |
|---|---|
| [[2607.01612]] C3RL / CAS | 校准置信度 + 自适应推理缩放，OOD 文本 12.33× 预算缩减。Calibrated confidence + adaptive test-time scaling, 12.33× budget reduction on OOD text. |
| [[2607.01893]] Spec-AUF | 块草稿器训练-推理错配修复，DFlash 平均接受长度 2.40→2.61，零推理开销。Fixes train-inference misalignment in block drafters, τ 2.40→2.61 with zero inference cost. |
| [[2607.01607]] MxGLUT | LUT 中心化统一加速器，FP8-INT4 与 FP8-FP8 共用数据通路，2.16× 加速。LUT-centric unified accelerator sharing FP8-INT4/FP8-FP8 datapath, up to 2.16× speedup. |

### 🏗️ 训练系统与硬件 / Training Systems & Hardware

| Paper | Description |
|---|---|
| [[2607.01844]] MoP | 组件特化并行训练万亿参数 MoE，<96 GPU 实现 4.7–8.2× 吞吐提升。Component-specialized parallelism trains trillion-param MoE on <96 GPUs, 4.7–8.2× throughput. |
| [[2607.01602]] ProWAFT | FPGA CNN 加速器主动容错，部分重构按需 TMR，吞吐提升 45.9%。Proactive fault tolerance for FPGA CNN accelerators, on-demand TMR via partial reconfiguration, +45.9% throughput. |

### 📊 评测与不确定性 / Evaluation & Uncertainty

| Paper | Description |
|---|---|
| [[2607.02032]] PACE | 100 个原子实例预测昂贵 agent 基准，1/100 成本达 84% 排序准确率。100 atomic instances predict expensive agentic benchmarks at 1/100 cost, 84% pairwise accuracy. |
| [[2607.02328]] Cross-Audit Projection | 揭示 K 折 CV 在类别特定风险上劣于经验估计；CAP 两步法渐近校正。Shows K-fold CV worse than empirical for class-specific risk; CAP provides asymptotic correction. |
| [[2607.02182]] DALorRA | LoRA rank 层级贝叶斯掩码，仅 +520 参数，训练比标准 LoRA 更快且 9/10 校准最优。Rank-level Bayesian mask adds only +520 params, trains faster than LoRA, 9/10 best ECE. |

### 🧮 科学机器学习与优化 / Scientific ML & Optimization

| Paper | Description |
|---|---|
| [[2607.02194]] DSGNAR | 双重草图 Gauss-Newton PINN 优化器，精度提升 3–8 个数量级。Doubly-sketched Gauss-Newton PINN optimizer, 3–8 orders of magnitude accuracy improvement. |

---

## All Papers

| # | ArXiv ID | Title | Topic |
|---|---|---|---|
| 1 | [[2607.01571]] | Geometric Signatures of Reasoning: A Spectral Perspective on Task Hardness | 机制可解释性 / Interpretability |
| 2 | [[2607.01602]] | ProWAFT: A ROMA-LPD Instance for Workload-Aware and Dynamic Fault Tolerance in FPGA-Based CNN Accelerators | 训练系统与硬件 / Hardware |
| 3 | [[2607.01607]] | MxGLUT: A Reconfigurable LUT-Centric Broadcast Dataflow Accelerator for Mixed-Precision GEMM | 推理效率 / Inference Efficiency |
| 4 | [[2607.01612]] | Scaling with Confidence: Calibrating Confidence of LLMs for Adaptive Test Time Scaling | 推理效率 / Inference Efficiency |
| 5 | [[2607.01639]] | Autonomous discovery of traffic laws with AI traffic scientists | 自主科研 / Autonomous Science |
| 6 | [[2607.01793]] | Safety Testing LLM Agents at Scale: From Risk Discovery to Evidence-Grounded Verification | LLM 安全 / Agent Safety |
| 7 | [[2607.01799]] | Expander Sparse Autoencoders: Parameter-Efficient Dictionaries for Mechanistic Interpretability | 机制可解释性 / Interpretability |
| 8 | [[2607.01802]] | On the Limits of Steering Vectors for Preference-Aligned Generation | LLM 安全与对齐 / Safety & Alignment |
| 9 | [[2607.01844]] | Mixture-of-Parallelisms: Towards Memory-Efficient Training Stack for Mixture-of-Experts Models | 训练系统 / Training Systems |
| 10 | [[2607.01846]] | CLAP: Closed-Loop Training, Evaluation, and Release Control for Domain Agent Post-training | 智能体系统 / Agent Systems |
| 11 | [[2607.01854]] | Has This Checkpoint Been Abliterated? A Two-Signal Audit and Its Failure Map | LLM 安全 / LLM Safety |
| 12 | [[2607.01874]] | SkillCoach: Self-Evolving Rubrics for Evaluating and Enhancing Agentic Skill-Use | 智能体系统 / Agent Systems |
| 13 | [[2607.01893]] | Spec-AUF: Accept-Until-Fail Training under Train-Inference Misalignment for Masked Block Drafters | 推理效率 / Inference Efficiency |
| 14 | [[2607.01919]] | ElephantAgent: Contextual State Continuity in Agentic Systems | 智能体安全 / Agent Security |
| 15 | [[2607.01935]] | A-TMA: Decoupling State-Aware Memory Failures in Long-Term Agent Memory | 智能体系统 / Agent Memory |
| 16 | [[2607.01940]] | Conditional Co-Ablation: Recovering Self-Repair Backups in Transformer Circuits | 机制可解释性 / Interpretability |
| 17 | [[2607.01951]] | Robust for the Wrong Reasons: The Representational Geometry of LLM Robustness to Science Skepticism | LLM 安全与对齐 / Safety & Alignment |
| 18 | [[2607.02032]] | PACE: A Proxy for Agentic Capability Evaluation | 评测 / Evaluation |
| 19 | [[2607.02072]] | kNNGuard: Turning LLM Hidden Activations into a Training-Free Configurable Guardrail | LLM 安全 / LLM Safety |
| 20 | [[2607.02134]] | Coding-agents can replicate scientific machine learning papers | 自主科研 / Autonomous Science |
| 21 | [[2607.02182]] | Bayesian Sparse Low-Rank Adaptation for Large Language Model Uncertainty Estimation | 不确定性 / Uncertainty |
| 22 | [[2607.02186]] | UA-ChatDev: Uncertainty-Aware Multi-Agent Collaboration for Reliable Software Development | 编程智能体 / Coding Agents |
| 23 | [[2607.02194]] | An Optimisation Framework for the Well-Conditioned Training of Physics-Informed Neural Networks | 科学机器学习 / Scientific ML |
| 24 | [[2607.02210]] | Criticality-Based Guard Rail Validation for AI Agent Decisions in Autonomous Telecom Networks | 智能体安全 / Agent Safety |
| 25 | [[2607.02328]] | Cross-Audit Projection for Model Risk Prediction | 评测 / Evaluation |
| 26 | [[2607.02329]] | Grounded autonomous research: a fault-tolerant LLM pipeline from corpus to manuscript in frontier computational physics | 自主科研 / Autonomous Science |

---

> **验证 / Verification:** 目录中 .md 文件共 26 个（不含 overview.md），overview 中收录 26 篇，数量一致。
> The directory contains 26 `.md` files (excluding overview.md); the overview lists 26 papers — counts match. ✅
