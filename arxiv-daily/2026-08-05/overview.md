---
title: "Daily arXiv Digest — 2026-08-05"
date: 2026-08-05
tags:
  - llm-agents
  - llm-evaluation
  - llm-safety
  - foundation-models
  - optimization
  - reasoning
  - interpretability
  - decision-theory
  - learning-theory
  - multimodal
papers: 50
---

## 今日必读 / Must Read Today

### 1. [[2608.04505]] K-EXAONE 2.0 Technical Report

**推荐理由 / Why read:** 韩国 LG AI Research 发布的开源前沿级 MoE 基础模型，通过"模型 upcycling"将上一代沿深度与宽度扩展，得到 750B 总参/37B 激活/256K 上下文/10 语言的 Apache 2.0 模型，在 24 个基准上较前代平均提升超 10%，SWE-Bench Verified 从 49.4 跃升至 68.2，并在长上下文检索上明显领先 Qwen3.5、GLM-5.1、DeepSeek V4 Pro。
*LG AI Research releases an open-weight frontier-scale MoE foundation model (750B total / 37B active / 256K context), built efficiently via "model upcycling" rather than from scratch, with double-digit average gains and the clearest edge over open-weight rivals in long-context retrieval and Korean safety — a notable new entrant in the open frontier-model landscape.*

### 2. [[2608.04975]] SCICODE-VERIFIED

**推荐理由 / Why read:** 对 SCIENCE 科学代码基准全部 65 题的专家审计发现了 263 个缺陷（其中 192 个压低分数、覆盖 91% 的主问题），修复后 12 个前沿模型的主问题准确率从 9–27% 跃升至 69–92%——证明此前普遍认为的"能力停滞"其实是基准缺陷而非模型天花板。这对所有引用 SCICODE 分数的研究都有追溯性影响。
*A domain-expert audit of the SCICODE benchmark uncovers 263 defects that suppressed scores; after correction, frontier models jump from single-digit main-problem accuracy to 69–92%, showing the field's perceived plateau was an instrument defect, not a capability ceiling — essential reading for anyone citing prior scientific-coding benchmarks.*

### 3. [[2608.04458]] Architectural Implications of Agentic AI Workflows

**推荐理由 / Why read:** 首个基于 Microsoft Azure 超大规模生产集群 + 四个开源框架（SWE-Agent、Trae、CORAL、Owl）的 agentic 工作负载架构剖析，揭示其碎片化、突发性、异构性的本质，并据此提出的 Agora 原型通过 CPU/GPU 空闲资源收割与角色感知核心池化，在保持尾部延迟的前提下将单机吞吐提升 82%–106%。对未来数据中心与推理系统设计有直接指导意义。
*The first production-fleet study of agentic AI workloads reveals they are fragmented, bursty, and heterogeneous, stranding capacity on uniform servers; the proposed Agora prototype lifts throughput 82–106% via CPU/GPU idle harvesting and role-aware core pooling — concrete, systems-level guidance for the agentic-AI era.*

---

## 按主题分类 / Papers by Topic

### 智能体系统 / Agentic Systems & Autonomous Agents

| 论文 / Paper | 核心要点 / Key Point |
|---|---|
| [[2608.04458]] Agentic AI Workflow Architecture | 首个生产级 agentic 负载剖析；Agora 原型吞吐提升 82–106%。 *First production-fleet study of agentic workloads; Agora prototype lifts throughput 82–106%.* |
| [[2608.05144]] Argus | 持久化、可自我演化的通用智能体运行时，SWE-Bench Pro 达 ~78%。 *Persistent self-evolving agentic runtime reaching ~78% on SWE-Bench Pro via verification-gated pivoting.* |
| [[2608.04738]] EviGraph | 把自主研究建模为有类型证据图并按依赖回滚修复，ARC-Bench-ML 达 86.45%。 *Models autonomous research as a typed evidence graph with dependency-aware repair; 86.45% on ARC-Bench-ML.* |
| [[2608.04968]] EvolveNet | 联邦式协作 harness 演化，聚合专家程序差分而非权重，5 基准提升 8.3–33.4 点。 *Federated collaborative harness evolution aggregating program diffs not weights; +8.3–33.4 pts on 5 benchmarks.* |
| [[2608.04587]] MetaVideoAgent | 首个面向视频分布的自动 Agent 演化框架，准确率 38.44%→51.47%。 *First auto-evolving video agent framework; accuracy 38.44%→51.47% on VA-EvoBench.* |
| [[2608.04625]] A/B Agent | 工业推荐系统策略迭代闭环智能体，快手电商 GMV +4.829%。 *Closed-loop agent for industrial A/B testing strategy iteration; +4.829% GMV in Kuaishou production.* |
| [[2608.05124]] Chained RLM | 推理时链式递归调用同模型，四个长上下文基准平均 +13.75 点。 *Inference-time chained recursive LLM calls; +13.75 pts average on 4 long-context benchmarks.* |

### 大模型评测与基准 / LLM Evaluation & Benchmarking

| 论文 / Paper | 核心要点 / Key Point |
|---|---|
| [[2608.04975]] SCICODE-VERIFIED | 修复 SCICODE 263 个缺陷后，模型主问题准确率从 9–27% 升至 69–92%。 *Fixing 263 SCICODE defects lifts main-problem accuracy from 9–27% to 69–92%.* |
| [[2608.05086]] Item Response Theory for AI Safety | IRT 拟合 8 基准 192 模型，三因子解释 77% 方差，~75 题即可恢复排名。 *IRT across 8 safety benchmarks and 192 models; 3 factors explain 77% variance, ~75 items recover rankings.* |
| [[2608.04549]] EuroExec | 47 位专家手写 413 道欧洲高管决策任务，最强模型 Solve Rate 仅 56.9% vs 专家 92.4%。 *Expert-authored European executive-decision benchmark; best model 56.9% vs expert 92.4%.* |
| [[2608.04714]] Inference Backend Side-effects | 仅切换推理后端即可显著改变基准得分，结构性后端效应占~39% 方差。 *Switching inference backend alone shifts benchmark scores; structural backend effect ~39% of variance.* |
| [[2608.04613]] Anomaly Detection Ranking Instability | 异常检测算法排名高度不稳定，约需 200 个数据集才达可靠排名。 *Anomaly-detection rankings highly unstable; ~200 datasets needed for reliable σ_rank ≈ 0.2.* |
| [[2608.04463]] LLM Conformity Measurement | 分离四通道的从众测量协议，同侪呈现引发评判者特定方向漂移。 *Four-channel conformity protocol; peer presentation causes judge-specific directional rating shifts.* |

### 安全、对齐与遗忘 / Safety, Alignment & Unlearning

| 论文 / Paper | 核心要点 / Key Point |
|---|---|
| [[2608.04347]] Side-Effect Introspection | 提出"副作用内省"任务与 DAIA 适配器，OOD 平均高约 6 个 F1 点。 *Introduces "side-effect introspection" and DAIA adapter; ~+6 pts F1 over LoRA introspection on OOD.* |
| [[2608.04366]] SecureCollaRAG | 拜占庭鲁棒协作 RAG，把 PoisonedRAG 攻击成功率从 97% 降到 5.24%。 *Byzantine-tolerant collaborative RAG cuts PoisonedRAG attack success from 97% to 5.24%.* |
| [[2608.04519]] Leak-Resistant Unlearning | 6 种多跳推理结构 + 3 种恢复攻击揭示遗忘"不可能三角"。 *6 multi-hop structures and 3 recovery attacks reveal an unlearning "impossible triangle."* |
| [[2608.04928]] CoT Monitorability | 隐式 CoT 不必然更难监控，监控效果更多取决于任务与内部访问。 *Latent CoT is not necessarily less monitorable; depends more on task and internal access than reasoning mode.* |
| [[2608.04692]] VLA Task-Vector Audit | 首个闭环 VLA task-vector 减法审计，保留率仅 52%。 *First closed-loop VLA task-vector negation audit; mean control retention only 52%.* |

### 优化器与训练方法 / Optimization & Training Methods

| 论文 / Paper | 核心要点 / Key Point |
|---|---|
| [[2608.04607]] MUON Error Analysis | MUON 首个严格误差分析，并证明在简单二次问题上对几乎所有批大小不收敛。 *First rigorous MUON error analysis + first non-convergence result for almost all batch sizes on a simple SOP.* |
| [[2608.05088]] MALT | 曲率感知 Muon 变体，GPT-2 上验证损失较 Muon 进一步降 0.016–0.028。 *Curvature-aware Muon via diagonal preconditioning; GPT-2 val loss 0.016–0.028 lower than Muon.* |
| [[2608.04407]] MESH | 隐式动量 Sinkhorn，MoE 优化器内存降 62.5% 但损失高约 0.049。 *Hidden-momentum Sinkhorn cuts MoE optimizer memory 62.5% at +0.049 eval loss cost.* |
| [[2608.05136]] Loss vs Adam Basis | 分解损失规范等变，Adam 等逐坐标法第一步即破坏隐式低秩偏好。 *Factored loss is gauge-equivariant; coordinate-wise methods (Adam) break the low-rank bias at step one.* |

### 推理、思维链与蒸馏 / Reasoning, CoT & Distillation

| 论文 / Paper | 核心要点 / Key Point |
|---|---|
| [[2608.04355]] The Calibration Floor | 自我修正增益实为格式修复伪信号，语法受限解码关闭 71% 差距。 *Self-correction gains are mostly format-repair artifacts; grammar-constrained decoding closes 71% of the gap.* |
| [[2608.04794]] PI-Conditioned Self-Distillation | 严格因果实验证明 PI 条件化自蒸馏在困难推理上零学习。 *Causal experiments show PI-conditioned self-distillation alone teaches zero reasoning.* |
| [[2608.04408]] Counterfactual Recoverability | 反事实可恢复性是比散度更优的选择性监督决策变量，AUC 1.0 vs 0.39。 *Counterfactual recoverability beats divergence as supervision signal; AUC 1.000 vs 0.392.* |
| [[2608.04980]] Protoreasoning | 1M 参数微型 Transformer 上的"原型推理"链显著缩小 OOD 泛化差距。 *Primitive "protoreasoning" traces help ~1M-param tiny transformers generalize OOD.* |

### 基础模型与多模态 / Foundation Models & Multimodal

| 论文 / Paper | 核心要点 / Key Point |
|---|---|
| [[2608.04505]] K-EXAONE 2.0 | 开源 750B/37B MoE 基础模型，24 基准平均提升超 10%。 *Open-weight 750B/37B MoE foundation model; >10% average gain across 24 benchmarks.* |
| [[2608.05000]] Physics of Multimodal Pretraining | 揭示跨模态知识流高度不对称，提出 L70/U25/G5 配比仅用 5% 生成数据。 *Asymmetric cross-modal knowledge flow; L70/U25/G5 recipe uses 5x fewer generation tokens.* |
| [[2608.04935]] PE-SPC AIGI Detection | 语义原型校准让 PE 冻结特征刷新五大 AIGI 检测 SOTA，1.9B 反超 6.7B。 *Semantic prototype calibration makes frozen PE features SOTA on 5 AIGI-detection benchmarks at 1.9B params.* |
| [[2608.04949]] UG-UMRE | 不确定性建模引入统一多模态关系抽取，三基准 F1 +2.34/+3.95/+2.25。 *Uncertainty modeling for unified multimodal RE; F1 +2.34/+3.95/+2.25 on 3 benchmarks.* |
| [[2608.05122]] IRIS | 视觉皮层启发的 ViT 方向选择性分析框架，训练范式是决定因素。 *Visual-cortex-inspired ViT orientation-selectivity framework; training objective is the key determinant.* |

### 可解释性与机理分析 / Interpretability & Mechanistic Analysis

| 论文 / Paper | 核心要点 / Key Point |
|---|---|
| [[2608.04904]] SAE Multilingual Steering | 稀疏自编码器引导向量在 Gemma-3-12B 上提升多语言推理，XCOPA +11.3 点。 *SAE-derived steering vector lifts multilingual inference; XCOPA +11.3 pp on Gemma-3-12B.* |
| [[2608.04893]] Latent Communication Audit | 因果审计 KV-cache 中继，标准基准上 example-pairing 效应被界定在 ±2.8 分内。 *Causal audit of relayed KV caches bounds the example-pairing effect within ±2.8 pts on standard benchmarks.* |

### 决策理论与学习理论 / Decision Theory & Learning Theory

| 论文 / Paper | 核心要点 / Key Point |
|---|---|
| [[2608.04312]] First-Order DDO Improvements | EO+ 统一框架证明无免费午餐，常数阶扰动才能拿一阶改进。 *EO+ framework proves no-free-lunch; only constant-order perturbation yields first-order gains.* |
| [[2608.04686]] DRO PAC Sample Complexity | Cressie–Read 散度下鲁棒 PAC 学习样本复杂度上下界，收紧 χ² gap。 *Tight sample complexity for robust PAC learning under Cressie–Read divergences; closes χ² gap.* |
| [[2608.04474]] Local Violation Certification | 线性 PTO 管线单次 LP 求解给出闭式违规证书，场景生成需多 3–4 个数量级。 *Closed-form violation certificate from one LP solve vs 44–3×10⁴ solves for scenario generation.* |
| [[2608.04531]] Functional Flow Matching | 证明函数空间流匹配有限目标强 L2 收敛，给出 O((log n)/√n) 端到端速率。 *Proves functional flow matching convergence; O((log n)/√n) end-to-end rate.* |
| [[2608.04451]] Fourier Alignment Counterexample | 单 ReLU 神经元模加法反例，推翻 Fourier 对齐猜想。 *Counterexample refuting Fourier-alignment conjecture for single-neuron modular addition.* |

### 高效推理与系统 / Efficient Inference & Systems

| 论文 / Paper | 核心要点 / Key Point |
|---|---|
| [[2608.04734]] Chebyshev Systolic Array | 统一激活函数单元，tanh/sigmoid 误差降 71%/41%，面积省 4.6%。 *Unified activation-function unit; tanh/sigmoid error cut 71%/41%, area saved 4.6%.* |
| [[2608.04569]] Referential Dangling | 识别硬提示压缩的"指代悬空"失败模式，补回依赖句 +4.7 点。 *Identifies "referential dangling" in hard prompt compression; restoration adds +4.7 pts.* |
| [[2608.04448]] Downscaled Image Training | 分解下采样梯度差距，选择性低分辨率 LoRA 训练省 14.6% 时间。 *Decomposes downscaled-gradient gap; selective low-res LoRA saves 14.6% training time.* |
| [[2608.05064]] Verbalized Uncertainty Deferral | 小模型口语化置信度的可证推迟框架，20% 风险下仅 3 对获准自主。 *Provable deferral framework for verbalized uncertainty; only 3 model-task pairs certified at 20% risk.* |

### 可靠性与 AI 审计 / Reliability & AI Auditing

| 论文 / Paper | 核心要点 / Key Point |
|---|---|
| [[2608.04457]] Eigenius | 强类型知识图谱 DBMS，重算 Nature 论文复现 52 结论并暴露 4 处差异。 *Typed KG DBMS; end-to-end recomputation of a Nature study reproduces 52 conclusions, surfaces 4 discrepancies.* |
| [[2608.04365]] Manipulation-Proof Audits | R²esPIR 用 PIR 隐藏审计集，操纵所需改写数从 39 提升到 156。 *R²esPIR uses PIR to hide audit set; required manipulations rise from 39 to 156 on COMPAS.* |
| [[2608.04921]] System Integration Audits | 范围综述发现 AI 审计仍以组件级为主，近 2/3 为概念性提案。 *Scoping review finds AI audits are still mostly component-level; ~65% are mere proposals.* |
| [[2608.04552]] Relational Response Fields | 黑盒 LLM 响应一致性理论，受限奇异值 γ_k 精确刻画恢复难度。 *Theory of black-box LLM response consistency; restricted singular value γ_k exactly characterizes recovery difficulty.* |

### 个性化与领域应用 / Personalization & Domain Applications

| 论文 / Paper | 核心要点 / Key Point |
|---|---|
| [[2608.04570]] The Personalization Mirage | MirageBench 揭示"自我监控倒置"，所有模型过度推断率 35%–49%。 *MirageBench reveals a "Self-Monitoring Inversion"; all models over-infer 35%–49% of claims.* |
| [[2608.05132]] MT-GNN Brain Morphometry | 连续时间图网络预测皮层下核团度量张量，顶点误差降 2.29%。 *Continuous-time GNN predicts subcortical metric tensors; vertex error cut 2.29% on ADNI.* |
| [[2608.04847]] Queer Slang Understanding | Slang-Q 数据集评测发现所有 LLM 远低于人类上界（ROUGE-L 0.18 vs 0.48）。 *Slang-Q dataset shows all LLMs far below human upper bound (ROUGE-L 0.18 vs 0.48).* |
| [[2608.05030]] Football Score Reranking | 可审计 LLM+Dixon-Coles 混合架构，精确比分命中率有描述性提升但不显著。 *Auditable LLM+Dixon-Coles hybrid; descriptive but non-significant exact-score gain on EPL.* |

---

## All Papers

| # | ID | Title | Topic / 主题 |
|---|---|---|---|
| 1 | [[2608.04312]] | Achieving First-Order Statistical Improvements in Data-Driven Optimization | 决策理论 / Decision Theory |
| 2 | [[2608.04347]] | Looking in the Mirror: Introspecting Side-Effect Misalignments Induced by Fine-Tuning | 安全与对齐 / Safety & Alignment |
| 3 | [[2608.04355]] | The Calibration Floor: Format Repair Can Masquerade as Self-Correction | 推理与蒸馏 / Reasoning & Distillation |
| 4 | [[2608.04365]] | Manipulation-Proof Oblivious Audits against Deceptive Model Providers | 可靠性与审计 / Reliability & Auditing |
| 5 | [[2608.04366]] | Combating Knowledge Corruption in Agent Systems: A Byzantine-Tolerant Secure RAG | 安全与对齐 / Safety & Alignment |
| 6 | [[2608.04407]] | MESH: Memory-Efficient Sinkhorn Optimization for Mixture-of-Experts Training | 优化与训练 / Optimization & Training |
| 7 | [[2608.04408]] | Not Every Divergence Should Be Suppressed: Counterfactual Recoverability in On-Policy Distillation | 推理与蒸馏 / Reasoning & Distillation |
| 8 | [[2608.04448]] | When Does Training on Downscaled Images Yield the Same Gradients? | 高效推理与系统 / Efficient Inference & Systems |
| 9 | [[2608.04451]] | A Counterexample to Fourier Alignment in Single-Neuron Modular Addition | 学习理论 / Learning Theory |
| 10 | [[2608.04457]] | Eigenius: A Typed Knowledge-Graph DBMS with Epistemic Stratification | 可靠性与审计 / Reliability & Auditing |
| 11 | [[2608.04458]] | Architectural Implications of Agentic AI Workflows | 智能体系统 / Agentic Systems |
| 12 | [[2608.04463]] | The Evaluator Is Part of the Experiment: Measuring Open-Ended LLM Conformity | 大模型评测 / LLM Evaluation |
| 13 | [[2608.04474]] | Local Violation Certification for Linear Predict-Then-Optimize Pipelines | 决策理论 / Decision Theory |
| 14 | [[2608.04505]] | K-EXAONE 2.0 Technical Report: Journey to Global Frontier-Scale Foundation Models | 基础模型与多模态 / Foundation Models & Multimodal |
| 15 | [[2608.04519]] | Leak-Resistant Unlearning: A New Benchmark for Multi-Hop Reasoning Consistency | 安全与对齐 / Safety & Alignment |
| 16 | [[2608.04531]] | Discretization and Statistical Consistency of Functional Flow Matching | 学习理论 / Learning Theory |
| 17 | [[2608.04549]] | EuroExec: Frontier Language Models Fall Short of Expert Judgment | 大模型评测 / LLM Evaluation |
| 18 | [[2608.04552]] | Relational Response Fields: A General Theory of Black-Box LLM Response Consistency | 可靠性与审计 / Reliability & Auditing |
| 19 | [[2608.04569]] | Relevant but Incomplete: Referential Dangling in Hard Prompt Compression | 高效推理与系统 / Efficient Inference & Systems |
| 20 | [[2608.04570]] | The Personalization Mirage: How LLMs Fabricate User Profiles | 个性化与领域应用 / Personalization & Domain Apps |
| 21 | [[2608.04587]] | MetaVideoAgent: Automated Video-Agent Evolution for Long-Form Video Understanding | 智能体系统 / Agentic Systems |
| 22 | [[2608.04607]] | On MUON optimization: From non-convergence to an error analysis | 优化与训练 / Optimization & Training |
| 23 | [[2608.04613]] | Why Ranking Anomaly Detection Algorithms Isn't as Reliable as You May Think | 大模型评测 / LLM Evaluation |
| 24 | [[2608.04625]] | A/B Agent: A Self-Evolving Agent for Strategy Iteration in Industrial A/B Testing | 智能体系统 / Agentic Systems |
| 25 | [[2608.04686]] | The Sample Complexity of Distributionally Robust PAC Learning under Cressie–Read Divergences | 决策理论 / Decision Theory |
| 26 | [[2608.04692]] | Suppression Sticks, Locality Is Fragile: A Closed-Loop Audit of Task-Vector Negation in VLA Policies | 安全与对齐 / Safety & Alignment |
| 27 | [[2608.04714]] | What We Observe as LLM Behavior Can Be a Side-effect of Inference Backend | 大模型评测 / LLM Evaluation |
| 28 | [[2608.04734]] | A Systolic Array Architecture for Nonlinear Activation Functions and Softmax | 高效推理与系统 / Efficient Inference & Systems |
| 29 | [[2608.04738]] | EviGraph: Evidence-Guided Autonomous Research Agents | 智能体系统 / Agentic Systems |
| 30 | [[2608.04794]] | Privileged, but Biased: How PI-Conditioned Teachers Break Self-Distillation | 推理与蒸馏 / Reasoning & Distillation |
| 31 | [[2608.04847]] | Do Language Models Know Their Slang? Queer Slang Understanding in User-Generated Content | 个性化与领域应用 / Personalization & Domain Apps |
| 32 | [[2608.04893]] | When Does Latent Communication Pay? A Causal Audit of Relayed KV Caches | 可解释性 / Interpretability |
| 33 | [[2608.04904]] | Strengthening Target-Language Features: SAE-Based Steering for Multilingual Inference | 可解释性 / Interpretability |
| 34 | [[2608.04921]] | A Chain Is Only as Strong as Its Weakest Link: A Scoping Review of System Integration Audits | 可靠性与审计 / Reliability & Auditing |
| 35 | [[2608.04928]] | Does Out-of-Sight Equal Out-of-Mind in CoT Monitorability? | 安全与对齐 / Safety & Alignment |
| 36 | [[2608.04935]] | Unleashing the Potential of Vision-Language Models for Generalizable AIGI Detection | 基础模型与多模态 / Foundation Models & Multimodal |
| 37 | [[2608.04949]] | UG-UMRE: Uncertainty-Guided Modality Augmentation for Unified Multimodal Relation Extraction | 基础模型与多模态 / Foundation Models & Multimodal |
| 38 | [[2608.04968]] | EvolveNet: Collaborative Harness Evolution for Agent Self-Improvement | 智能体系统 / Agentic Systems |
| 39 | [[2608.04975]] | SCICODE-VERIFIED: How Benchmark Defects Underestimated the Scientific-Coding Ability of LLMs | 大模型评测 / LLM Evaluation |
| 40 | [[2608.04980]] | Protoreasoning in Tiny Transformers | 推理与蒸馏 / Reasoning & Distillation |
| 41 | [[2608.05000]] | Towards Physics of Multimodal Pretraining: Knowledge Flow, Modality Synergy, Early Unification | 基础模型与多模态 / Foundation Models & Multimodal |
| 42 | [[2608.05030]] | From Score Matrices to Football-Aware Match-State Simulation | 个性化与领域应用 / Personalization & Domain Apps |
| 43 | [[2608.05064]] | Provable Limits and Certified Deferral for Verbalized Uncertainty in Small Language Models | 高效推理与系统 / Efficient Inference & Systems |
| 44 | [[2608.05086]] | Item Response Theory for AI Safety | 大模型评测 / LLM Evaluation |
| 45 | [[2608.05088]] | MALT: Lightweight Curvature-Aware Muon via Diagonal Preconditioning | 优化与训练 / Optimization & Training |
| 46 | [[2608.05122]] | IRIS: A Visual Cortex-Inspired Framework for Analyzing Orientation Selectivity in ViTs | 基础模型与多模态 / Foundation Models & Multimodal |
| 47 | [[2608.05124]] | Chained Recursive Language Models for Multi-Iteration Reasoning | 智能体系统 / Agentic Systems |
| 48 | [[2608.05132]] | Predicting Brain Morphometry with MT-GNN: Mesh Evolution in Continuous Time | 个性化与领域应用 / Personalization & Domain Apps |
| 49 | [[2608.05136]] | The Loss Does Not See the Basis, But Adam Does | 优化与训练 / Optimization & Training |
| 50 | [[2608.05144]] | Argus: A General-Purpose Agentic Runtime for Long-Horizon Reasoning | 智能体系统 / Agentic Systems |
