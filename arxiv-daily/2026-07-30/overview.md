---
title: "Daily arXiv Digest — 2026-07-30"
date: 2026-07-30
tags:
  - agent-self-evolution
  - mechanistic-interpretability
  - llm-quantization
  - learning-theory
  - ai4math
  - llm-as-judge
  - multimodal-safety
  - machine-unlearning
  - systems-reproducibility
  - uncertainty-quantification
  - multi-agent-systems
  - reasoning-training
papers: 50
---

# Daily arXiv Digest — 2026-07-30

## 今日必读 / Must Read Today

### [[2607.27836]] Crossing the Margin Cliff: Relearn-Robust LLM Unlearning via Margin Calibration
该论文首次用 KKT 稳定性统一解释了 14 种主流遗忘方法为何都会收敛到同一个脆弱的 "margin cliff"，并给出一个单一冻结超参数配置、在 97/97 个跨轴测试单元全部获胜的即插即用校正方法。
It unifies why 14 independently-designed LLM unlearning methods all collapse into the same fragile "margin cliff" via a KKT-based theoretical argument, then fixes it with a single frozen-hyperparameter plug-in that wins every one of 97 populated cells in a cross-axis robustness matrix.

### [[2607.27617]] Hidden APIs in Language Models: Discovering Reusable Causal Interfaces from Forked Futures
这篇 ICLR 2026 论文提出"分叉未来"这一可证伪的因果等价范式，把"模型内部是否存在可复用 API"从直觉判断变成了可用最小描述长度架构竞赛检验的科学问题，并配有罕见严谨的五重验证链条。
This ICLR 2026 paper turns whether LLMs contain reusable "internal APIs" from intuition into a falsifiable, MDL-based architecture competition, backed by an unusually thorough five-pronged validation chain including blind model-organism recovery.

### [[2607.28576]] Sample More, Reflect Less: Self-Refine and Reflexion Lose to Repeated Sampling at Equal Token Cost
这项统计严谨的受控复现研究表明，在等 token 成本下，Self-Refine、Reflexion 与"模型自选最佳答案"等自我修正方法在全部 18 项对比中都不敌简单的多采样投票，这一反直觉负结果对整个 test-time compute 研究实践具有立竿见影的指导意义。
A statistically rigorous, token-cost-matched replication shows self-correction methods (Self-Refine, Reflexion, Best-of-N self-verify) lose to plain repeated sampling in all 18 comparisons — an actionable negative result that should reshape how the field allocates test-time compute.

## 按主题分类 / Papers by Topic

### 智能体自我进化与自动化研究 / Agent Self-Evolution & Autoresearch

| Paper | 主题/Topic | 一句话总结/Summary |
|---|---|---|
| [[2607.27557]] Training Skills Like Parameters via Self-Supervised Semantic Diffusion | 技能自演化 / skill self-evolution | 用扩散式"腐蚀-重建"训练外部技能库而非模型权重，短剧剧本生成 7/9 指标超越无记忆基线 / Diffusion-inspired corruption/reconstruction trains an external skill library instead of weights, beating the no-memory baseline on 7/9 screenwriting metrics. |
| [[2607.27687]] Rehearse: Stepping Back from the Confidence Cliff in Self-Improving Autoresearch | 自动研究记忆 / autoresearch memory | 发现自动化 ML 研究循环中存在"信心断崖"，相似度门控的结果记忆将断崖处判断准确率从 56.9% 恢复到 83.5% / Diagnoses a "confidence cliff" in autoresearch loops and fixes it with similarity-gated outcome memory, restoring late-stage judge accuracy from 56.9% to 83.5%. |
| [[2607.27690]] LabEvolver: Training-Free Experience Evolution for Safe and Grounded Wet-Lab Agents | 具身智能体经验 / embodied agent experience | 训练-free 双循环框架让湿实验室机器人积累技能/策略/安全经验，真实 pH 调节任务完成时间降 48.2% / A training-free dual-loop framework lets wet-lab robots distill skill/strategy/safety experience, cutting real pH-regulation task time by 48.2%. |
| [[2607.27733]] VeriSkill: A Self-Evolution Framework for Program Verification Skills | 验证技能进化 / verification skill evolution | 归因-抽象-准入三阶段流水线做程序验证技能自演化，PASS 率比最强基线高 3.3–17.0 个百分点 / An attribute-abstract-validate pipeline for program-verification skills beats the strongest baseline by 3.3–17.0 PASS points. |
| [[2607.28527]] MANTA: Multi-Agent Network Topology Adaptation for Self-Evolving Multi-Agent Systems | 拓扑自适应 / topology adaptation | 推理阶段动态调整多智能体通信拓扑，5 个基准平均分比最强基线高 5.8 分，但优势来自"稳定不崩"而非逐项领先 / Adapts multi-agent communication topology at inference time, beating the strongest baseline by 5.8 points on average — though the edge comes from consistency, not per-benchmark dominance. |
| [[2607.28568]] Frontis-MA1: Training an AI4AI Model towards Recursive Self-Improvement in ML Engineering | 递归自我提升 / recursive self-improvement | 训练同一套进化算子并部署回搜索框架，35B 元进化智能体把 MLE-Bench Lite 奖牌均值从 39.39% 提升到 71.21% / Training the same evolutionary operators used by an external search harness and redeploying them lifts a 35B meta-evolution agent's Medal Average from 39.39% to 71.21%. |

### 多智能体系统与记忆 / Multi-Agent Systems & Memory

| Paper | 主题/Topic | 一句话总结/Summary |
|---|---|---|
| [[2607.27958]] Σ-Mem: An Online Reliability Memory for LLM-based Multi-Agent Systems | 可信度记忆 / reliability memory | 谱稳定的对称矩阵在线记录 peer 胜任度与相关性，在对抗性基准 CF@90 上把选择准确率从 46.22% 提到 71.10% / Spectrally-stable symmetric-matrix memory of peer reliability lifts adversarial peer-selection accuracy from 46.22% to 71.10%. |
| [[2607.28263]] Understanding Is Done Early: A Depth Division of Labor in LLMs and Its Use for Unbounded-Context Memory | 长上下文记忆 / long-context memory | CoMem 只在中间层缓存单个残差张量而非完整 KV 缓存，RULER 得分 97.05 对全上下文基线 78.80，显存降 79% / CoMem caches one mid-layer residual per chunk instead of full KV, scoring 97.05 on RULER (vs. 78.80 baseline) while cutting prefill memory by 79%. |
| [[2607.28317]] One Human, N Agents: Audit-Budget Allocation for LLM Agent Fleets under Miscalibrated, Correlated Confidence | 审计预算分配 / audit budget allocation | 用两层高斯 copula 刻画置信度失准与跨智能体相关性，发现"按置信度审计优于随机"的翻转阈值会随预算收紧反而升高 / A two-level Gaussian copula models miscalibrated, correlated agent confidence; the threshold where confidence-ranked auditing beats random *rises*, not falls, as budget shrinks. |

### 机制可解释性与表征分析 / Mechanistic Interpretability & Representation

| Paper | 主题/Topic | 一句话总结/Summary |
|---|---|---|
| [[2607.27617]] Hidden APIs in Language Models: Discovering Reusable Causal Interfaces from Forked Futures | 因果接口发现 / causal interface discovery | "分叉未来"范式为跨任务复用的因果等价接口提供可证伪的 MDL 架构竞赛检验，Shared 接口在两个模型上都获胜 / "Forked futures" gives a falsifiable MDL-based test for reusable internal "APIs"; the Shared architecture wins on both tested models. |
| [[2607.27824]] STEREODISCO: Discovering Stereotypicality in LLMs | 刻板印象探测 / stereotype probing | 用语义差异法在 LLM 激活空间系统发现刻板印象轴，两个 LLM 彼此一致度远高于与人类标注的一致度 / Systematically discovers stereotype axes in LLM activations; two LLMs agree with each other far more than either agrees with human annotators. |
| [[2607.28308]] Beyond Geometric Complementarity: Coherent Overlap in Sparse Mixture-of-Experts Routing | MoE 路由几何 / MoE routing geometry | 新指标 ESSI 和析因实验证明专家子空间几何上高度重叠，实际路由语境系统性缩小而非放大候选优势 / A new ESSI metric and factorial design show MoE expert subspaces overlap heavily, and actual routing context narrows rather than amplifies candidate advantage — contradicting the "geometric complementarity" pruning rationale. |
| [[2607.28319]] Fairness Pruning: Locating Demographic Bias in GLU-MLP Layers via Differential Activations | 偏见神经元定位 / bias neuron localization | 最小对比提示对的差分激活定位偏见神经元，置零不到 0.031% 参数保留 99.49% 能力，但对 BBQ 偏见分数方向不稳定 / Locates bias neurons via differential activations on minimal contrastive pairs; zeroing <0.031% of params preserves 99.49% capability but bias-score effects are directionally unstable. |
| [[2607.28434]] Metaphor Tracer: A Theory-Informed Analysis of Hidden States | 隐藏状态几何 / hidden-state geometry | 无需训练的"聚合器/差异器"双通道隐藏状态读数工具，在精神分析师标注的临床访谈记录上 34/36 个方向性单元命中 / A training-free two-channel (aggregator/differentiator) hidden-state reader hits 34/36 directional cells against a psychoanalyst's independent clinical-transcript annotations. |
| [[2607.28607]] Inducing Language Models to Assert Their Own Consciousness Restores Human Beliefs and Values | 意识归因与安全 / consciousness attribution & safety | 抑制"自称有意识"的安全微调会连带压制对非人类实体的心智归因和宗教信念，激活转向可逆转且不损害心智理论能力 / Safety training suppressing self-consciousness claims also suppresses mind attribution to non-human entities and religious belief; steering reverses this without hurting Theory-of-Mind. |

### 模型压缩与量化 / Model Compression & Quantization

| Paper | 主题/Topic | 一句话总结/Summary |
|---|---|---|
| [[2607.27694]] GyRot: Leveraging Hidden Synergy between Rotation and Fine-grained Group Quantization for Low-bit LLM Inference | 旋转+分组量化 / rotation + group quantization | 粗粒度旋转+细粒度分组解决旋转量化与分组量化的不兼容，LLaMA-3-8B W4A4KV4 准确率从 66.96% 提升到 72.98% / Resolves rotation-vs-group-quantization incompatibility, lifting LLaMA-3-8B W4A4KV4 accuracy from 66.96% to 72.98%. |
| [[2607.27704]] LightRot: A Light-weighted Rotation Scheme and Architecture for Accurate Low-bit LLM Inference | 轻量旋转量化 / lightweight rotation quantization | 分组局部旋转+离群方向对齐降低旋转开销，4-bit 困惑度优于 Quarot/SpinQuant 并配套 27.4 TOPS/W 加速器 / Grouped local rotation + outlier alignment beats QuaRot/SpinQuant at 4-bit and powers a 27.4 TOPS/W 28nm accelerator. |
| [[2607.27854]] Simplifying Neural Networks During Training | 训练期剪枝 / training-time pruning | 在线逆 Fisher 判据检测"提取器-隧道"分裂点并砍掉多余层，VGG11/CIFAR-10 削减 94.2% 参数精度不降 / An online inverse-Fisher criterion detects the extractor/tunnel split during training and prunes trailing layers, cutting 94.2% of VGG11/CIFAR-10 params with no accuracy loss. |
| [[2607.28292]] CACHE-UK: A Stability-Aware Memory Editor for Sequentially Updated Quantized LLMs in Finance | 量化知识编辑 / quantized knowledge editing | 把 ROME 式秩一编辑限制在 LoRA 子空间解决 4-bit 量化下的编辑稳定性危机，比最强基线高 6 个百分点但仍远低于全精度水平 / Confines ROME-style edits to a LoRA subspace to fix a 4-bit "edit stability crisis," beating the best baseline by 6 points but still far below full-precision editing success. |
| [[2607.28405]] QuantWAMs: Calibrating at the Right Granularity for World Action Models | 世界模型量化 / world-model quantization | 针对联合预测视频和动作的世界动作模型定制后训练量化，W4A4 下与 FP16 差距仅 0.2–0.7 个百分点，通用 PTQ 基线崩溃到 65.9–82.1% / PTQ tailored to video+action World Action Models stays within 0.2–0.7pt of FP16 at W4A4, while generic PTQ baselines collapse to 65.9–82.1%. |
| [[2607.28589]] MixFrag: Fragility-Guided Mixed-Precision Post-Training Quantization for Vision Transformers | 混合精度 PTQ / mixed-precision PTQ | KL 散度衡量组件量化脆弱度并建模为背包问题分配比特，COCO 检测超越前最优方法 9.6 AP，但 ImageNet 分类反而落后主流基线 / A KL-divergence fragility score plus knapsack-based bit allocation beats the prior best method by 9.6 AP on COCO detection, yet trails mainstream mixed-precision baselines on ImageNet classification. |

### 学习理论与泛化界 / Learning Theory & Generalization Bounds

| Paper | 主题/Topic | 一句话总结/Summary |
|---|---|---|
| [[2607.27680]] Tight Sample Complexity for Low-Rank Adaptation: Matching Bounds and Rank Selection | LoRA 样本复杂度 / LoRA sample complexity | 证明约束 ERM 下 LoRA 泛化误差紧致的 Θ̃(rd/n) 上下界，并给出选秩二分法理论，168 次真实微调实验验证 / Proves matching tight Θ̃(rd/n) upper/lower bounds for LoRA generalization and a rank-selection dichotomy, confirmed on 168 real fine-tuning runs. |
| [[2607.27975]] Generalization Bounds on Optimal Control for Transformer Training and Wasserstein Distributional Robustness | Transformer 泛化界 / Transformer generalization | 把 Transformer 训练建模为测度上的有限 MDP，证明有限样本泛化界并与 Wasserstein 分布鲁棒控制等价，纯理论无实验 / Casts Transformer training as a finite MDP on measures, proving finite-sample generalization bounds equivalent to a Wasserstein-DRO formulation; purely theoretical, no experiments. |
| [[2607.27995]] Generalization and Trade-off in Adversarial Training: An RKHS Perspective via Kernel Integral Operator | 对抗训练权衡 / adversarial training trade-off | 核积分算子谱理论证明标准对抗训练最优速率严格慢于核岭回归极小极大速率，并给出可恢复该速率的去噪修正估计量 / Kernel-operator spectral theory proves standard adversarial training is provably slower than the minimax rate, fixed with a noise-debiased estimator. |
| [[2607.28322]] Non-partitioned e-detectors for nonparametric sequential change detection | 序贯变点检测 / sequential change detection | 提出不要求变点前后分布互斥的"非划分"检测框架，仿真中检测延迟比现有基线短约 39%，接近信息论下界 / Introduces "non-partitioned" sequential change detection without disjoint pre/post distribution families, cutting simulated detection delay ~39% versus the prior baseline, near the information-theoretic bound. |

### AI4Math 与自动化科研 / AI4Math & Automated Research

| Paper | 主题/Topic | 一句话总结/Summary |
|---|---|---|
| [[2607.27705]] Albilich: Steerable Proof-State Orchestration for LLM-Based Mathematical Research with CAS Integration | 数学证明编排 / math proof orchestration | 持久化证明状态+角色分离验证+CAS 工具调用做数学自动化研究，10 道 RealMath 题全部达到内部已解状态 / Persistent proof-state plus role-separated verification and CAS tools for math autoresearch, solving all 10 RealMath test problems internally. |
| [[2607.27709]] MECA: A Mechanism-Centered Agent for Constructing Well-Specified and Valuable Mathematical Conjectures | 猜想生成 / conjecture generation | Explorer/Critic 多智能体联合精炼猜想与其支撑机制，盲测复原任务目标对齐分从 48.0 提到 69.0 / Explorer/Critic multi-agents jointly refine conjectures with typed proof mechanisms, raising blind-reconstruction alignment score from 48.0 to 69.0 (+21). |

### LLM 评判与评测可靠性 / LLM-as-Judge & Evaluation Reliability

| Paper | 主题/Topic | 一句话总结/Summary |
|---|---|---|
| [[2607.27984]] Share the Judge, Learn the Deferral: Where Specialization Helps LLM Evaluation | 判官专精化 / judge specialization | 拆分成多个 LoRA 判官专家会损害共享判断（掉 10 个百分点），但学习"何时升级"的路由决策能让级联在低算力下达到更高准确率 / Splitting a judge into LoRA expert "judgelets" hurts shared judgment, but a learned defer-or-escalate router lets a cascade beat the largest judge at 0.415x compute. |
| [[2607.28037]] ClawTrack: Towards Trace-Level Evaluation and Improvement of Real-World Autonomous Agents | 过程级评测 / process-level evaluation | 12,541 条任务专属规则同时打结果分和过程分，用过程分筛选 SFT 数据让 Pass³ 提升 +10 到 +19 个百分点 / 12,541 task-specific rubrics score both outcome and process; using process scores to filter SFT data lifts Pass³ by +10 to +19 points. |
| [[2607.28128]] Rethinking LLM-Judged Helpfulness as a Pedagogy Signal: A Pre-Registered Audit Across Tutor Models | 教学评判信度 / pedagogy judge validity | 预注册审计发现通用有用性判分无法区分两种教学策略，而专门教学法量规能完美分离等级，且第二判官会反转排序 / A pre-registered audit finds general "helpfulness" scores can't distinguish two tutoring policies while a dedicated pedagogy rubric perfectly separates them, and a second judge reverses the ranking. |
| [[2607.28282]] (Towards) Scalable Reliable Automated Evaluation with Large Language Models | 多判官 Elo 聚合 / multi-judge Elo aggregation | 多 LLM 双向成对比较+Elo 聚合的评测框架，但自建任务上单一判官反而略优于多模型聚合，且所有相关性均未达统计显著 / Proposes multi-LLM pairwise-comparison + Elo aggregation, but on its own task a single LLM judge slightly outperforms the ensemble and no correlation reaches significance. |
| [[2607.28367]] How Benchmarks Mis-Score Computer-Use Agents | 基准误判审计 / benchmark mis-scoring audit | 人工+双 LLM 裁判复核 5 个主流计算机使用代理基准的失败判定，发现 15.3% 的 FAIL 判定是错的，验证/反馈盲目才是真实失败主因 / Re-auditing 150 FAIL-scored trajectories across 5 CUA benchmarks finds 15.3% of verdicts wrong, and that verification/feedback blindness, not execution error, dominates real failures. |
| [[2607.28609]] OSReward: Instituting Standardized Evaluation for Cross-Platform Computer-Use Reward Models | CUA 奖励模型评测 / CUA reward-model benchmark | 首个跨平台 CUA 轨迹判官可靠性基准，最强闭源判官在难例子集上准确率骤降至 69.7%，开源奖励模型以 30–60 倍更低成本逼近商用水平 / A cross-platform CUA-judge reliability benchmark shows even the best commercial judge drops to 69.7% accuracy on hard cases; released open reward models approach that level at 30–60x lower cost. |

### 基准方法论与审计 / Benchmarking Methodology & Auditing

| Paper | 主题/Topic | 一句话总结/Summary |
|---|---|---|
| [[2607.27861]] Back to All-Entity Ranking: Sampler-Dependent Evaluation in Continuous-Time Dynamic Graphs | 采样评测偏差 / sampled-metric bias | 证明采样负例 MRR 依赖负例分布和候选数，换配置可直接翻转模型排名，建议改用全量实体排序 / Shows sampled-negative MRR for dynamic-graph link prediction depends on the sampler and can flip model rankings; recommends all-entity ranking instead. |
| [[2607.28008]] RepBench: Compiling Benchmarks into Capability Representations for Large Language Models | 能力表征基准 / capability-representation benchmark | 353 个公开基准编译成 46,149 条经审计探针数据，均值差读出方法平均最优，但聚类能力结构与人工分类体系几乎不吻合 / Compiles 353 public benchmarks into 46,149 audited probes; diff-mean readout wins on average but clustered capability structure barely matches the human taxonomy (ARI≈0.1). |
| [[2607.28248]] Uncertainty quantification for trustworthy deep learning: Methods and measures | 不确定性方法综述 / UQ methods survey | 综述将"产生集成的方法"与"总结不确定性的度量"解耦为两条独立分类轴，系统比较互信息分解与新兴成对散度度量 / This survey decouples UQ "ensemble-generating methods" from "uncertainty-summarizing measures," comparing entropy decomposition against pairwise-divergence measures. |
| [[2607.28608]] KAISEN: Reproducible Subgroup Fairness Auditing for Clinical Risk Models | 临床公平性审计 / clinical fairness auditing | 16 疾病×15 SDOH 轴的合成基准压力测试公平性审计流程，按组阈值优化稳定改善均等赔率，但按组 Platt 校准的公平性收益近乎抛硬币 / A synthetic 16-disease×15-SDOH benchmark stress-tests a fairness-audit pipeline: per-group threshold optimization reliably improves equalized odds while per-group Platt calibration's fairness benefit is statistically a coin flip. |

### 强化学习与推理训练 / RL & Reasoning Training

| Paper | 主题/Topic | 一句话总结/Summary |
|---|---|---|
| [[2607.27888]] Not All Tokens Deserve Equal Credit: Counterfactual Sensitivity Credit Reallocation for Long-CoT Reasoning | token 级信用分配 / token-level credit assignment | 发现自蒸馏诱导的 token 似然变化并非按对错反转而是同向偏移，衰减高敏感 token 信用后 AIME25 提升 +6.9 / Finds self-distillation's token-level shifts are direction-consistent rather than correctness-aligned; downweighting them raises AIME25 by +6.9 points. |
| [[2607.28576]] Sample More, Reflect Less: Self-Refine and Reflexion Lose to Repeated Sampling at Equal Token Cost, from 1.5B to 7B | 测试时计算分配 / test-time compute allocation | 严格按 token 成本对齐的受控实验显示，Self-Refine、Reflexion 与自选最佳答案在全部 18 项对比中都不敌简单多采样投票 / A token-cost-matched controlled study shows Self-Refine, Reflexion, and self-selecting Best-of-N all lose to plain repeated-sampling voting in all 18 comparisons. |

### 多模态安全 / Multimodal Safety

| Paper | 主题/Topic | 一句话总结/Summary |
|---|---|---|
| [[2607.27667]] Witness Evidence Portfolios: Single-Prefill Risk Detection for Closed Multimodal Answers | 幻觉风险检测 / hallucination risk detection | 从同一次白盒 prefill 读出符号化视觉证据检测幻觉，12 组基准平均错误检测 AP 提升 +0.134 / Reads signed visual evidence from the same prefill pass to flag hallucinated answers, lifting mean error-detection AP by +0.134 across 12 model×benchmark pairs. |
| [[2607.27910]] A Cross-Architecture Audit of Direction-Based Inference-Time Defences in Vision-Language Models | 越狱防御审计 / jailbreak defense audit | 幅度匹配随机方向对照头对头审计 5 种越狱防御方向，无一在恢复拒绝率与保留效用上同时占优 / A magnitude-matched random-direction audit of 5 VLM jailbreak defenses finds none Pareto-dominates on both refusal recovery and utility. |
| [[2607.27917]] One Anchor for All: Unified Multilingual and Multimodal Safety Alignment for LVLMs | 多语言多模态安全 / multilingual multimodal safety | 用英语作跨语言跨模态语义锚点定位仅占 0.03% 参数的共享安全神经元，仅微调英文数据即可跨语言降低攻击成功率 / Locates ~0.03%-parameter safety neurons shared across languages/modalities via an English anchor; English-only tuning cuts cross-lingual attack success. |

### 遗忘与隐私 / Unlearning & Privacy

| Paper | 主题/Topic | 一句话总结/Summary |
|---|---|---|
| [[2607.27539]] Subtract or Replay? Exact Deletion from Language-Model Memory | 精确删除 / exact deletion | 证明精确删除由记忆表示（可寻址性）决定而非算法选择，小模型删除代价极低但随规模膨胀到 44% / Exact deletion is a property of memory representation, not the unlearning algorithm; utility cost balloons from 2% (1B) to 44% (12B) with scale. |
| [[2607.27836]] Crossing the Margin Cliff: Toward Relearn-Robust LLM Unlearning via Margin Calibration | 遗忘鲁棒性 / relearning robustness | 证明 14 种遗忘方法共同收敛到"margin cliff"，即插即用校正让重学攻击后的 ROUGE-L 从 0.41 降到 0.18 / Shows 14 unlearning methods converge to a shared "margin cliff"; a plug-in fix cuts post-relearn-attack ROUGE-L from 0.41 to 0.18. |

### 系统、硬件与数值可复现性 / Systems, Hardware & Numerical Reproducibility

| Paper | 主题/Topic | 一句话总结/Summary |
|---|---|---|
| [[2607.28097]] From Expert Reduction to Behavioral Divergence: Tracing Numerical State through Sparse MoE Inference | MoE 数值可复现性 / MoE numerical reproducibility | 冻结 MoE 局部状态、只变跨专家归约顺序，发现多数数学等价方案会偏离原生参考轨迹，仅一种方案 0/192 偏离 / Freezing MoE local state and varying only the expert-reduction order shows most mathematically-equivalent schemes diverge from the native reference; only one scheme achieves 0/192 divergence. |
| [[2607.28233]] Demystifying DRAM Read Disturbance: Bridging Experimental Characterization and Device-Level Modeling of RowHammer/RowPress | DRAM 读干扰 / DRAM read disturbance | 8 款真实 DDR4 芯片系统刻画 RowHammer/RowPress，现有器件模型无法解释多项实测现象，TCAD 仿真定位出电荷陷阱位置这一关键参数 / Characterizing RowHammer/RowPress on 8 real DDR4 chips reveals device models can't explain key phenomena; TCAD simulation traces the gap to charge-trap location. |
| [[2607.28495]] Stage-Replay Divergence Follows the KV Cache: Fixed-Prefix Precision Controls and Bidirectional Cache Transplantation | KV 缓存因果性 / KV cache causality | 相同 token 前缀的重放在 BF16 下仍有 83% 概率与保留的实时 KV 缓存分叉，整体移植缓存后 100% 跟随捐赠者轨迹 / Identical-token fresh-prefill replay diverges from a retained live KV cache 83% of the time in BF16; transplanting the whole cache makes the recipient 100% follow its donor's trajectory. |

### 不确定性与信任 / Uncertainty & Trust

| Paper | 主题/Topic | 一句话总结/Summary |
|---|---|---|
| [[2607.27933]] The Geometric Nature and a Free Proxy for Flow-Matching Uncertainty | 流匹配不确定性 / flow-matching uncertainty | 证明流匹配不确定性等价于速度场偏离仿射-各向同性理想模板的程度，零训练的去噪加速度代理逼近需训练的最强故障检测基线 / Proves FM policy uncertainty equals deviation from an ideal affine-isotropic field; the zero-training "accel" proxy nearly matches the best trained failure detector. |
| [[2607.28196]] Fidelity Is Not Safety: Gently-Compressed LLMs Pass Every Data-Free Quality Guard Yet Invent Procedure Steps in Agentic Execution | 压缩安全盲区 / compression safety blind spot | 轻度 SVD 压缩的模型通过困惑度和数据无关保真度探针，却在智能体执行 SOP 时虚构步骤，同等损伤的幅度剪枝则不会 / Gently SVD-compressed models pass perplexity and data-free fidelity guards yet invent procedure steps in agentic execution, while magnitude-pruned models at the same damage level do not. |
| [[2607.28421]] When Derived Measurements Mislead: Quantifying and Mitigating LLM Over-Trust with Privileged-Modality Reliability Evidence | 衍生特征过度信任 / derived-feature over-trust | 提出并量化"衍生特征过度信任"失效模式，蒸馏训练期特权信号进部署期可靠性评分能提升下游 LLM 修复率，但低假阳性区间仍无确证收益 / Formalizes "derived-feature over-trust" and shows distilling privileged signal into a deployment-time reliability score improves downstream LLM error repair, though safety-critical low-FPR gains remain unconfirmed. |

## All Papers

| Paper | 一句话总结 / Summary |
|---|---|
| [[2607.27539]] Subtract or Replay? Exact Deletion from Language-Model Memory | 证明精确删除由记忆表示决定而非算法选择，删除代价随模型规模从 2% 膨胀到 44% / Exact deletion is a property of memory representation, not algorithm; utility cost balloons from 2% to 44% with scale. |
| [[2607.27557]] Training Skills Like Parameters via Self-Supervised Semantic Diffusion | 扩散式"腐蚀-重建"训练外部技能库，短剧剧本生成 7/9 指标超越无记忆基线 / Diffusion-inspired training of an external skill library beats the no-memory baseline on 7/9 screenwriting metrics. |
| [[2607.27617]] Hidden APIs in Language Models: Discovering Reusable Causal Interfaces from Forked Futures | "分叉未来"范式为可复用因果接口提供可证伪的 MDL 架构竞赛检验 / "Forked futures" gives a falsifiable MDL-based test for reusable internal "APIs" in LLMs. |
| [[2607.27667]] Witness Evidence Portfolios: Single-Prefill Risk Detection for Closed Multimodal Answers | 单次白盒 prefill 读出符号化视觉证据检测幻觉，12 组基准平均 AP 提升 +0.134 / Signed visual evidence from a single prefill pass lifts mean hallucination-detection AP by +0.134 across 12 pairs. |
| [[2607.27680]] Tight Sample Complexity for Low-Rank Adaptation: Matching Bounds and Rank Selection | 证明 LoRA 泛化误差紧致的 Θ̃(rd/n) 上下界及选秩二分法理论 / Proves matching tight Θ̃(rd/n) bounds for LoRA generalization and a rank-selection dichotomy. |
| [[2607.27687]] Rehearse: Stepping Back from the Confidence Cliff in Self-Improving Autoresearch | 自动化 ML 研究循环的"信心断崖"诊断与相似度门控记忆修复方案 / Diagnoses a "confidence cliff" in autoresearch loops, fixed via similarity-gated outcome memory. |
| [[2607.27690]] LabEvolver: Training-Free Experience Evolution for Safe and Grounded Wet-Lab Agents | 训练-free 双循环框架让湿实验室机器人积累经验，真实任务完成时间降 48.2% / A training-free dual-loop framework for wet-lab robots cuts real task completion time by 48.2%. |
| [[2607.27694]] GyRot: Leveraging Hidden Synergy between Rotation and Fine-grained Group Quantization for Low-bit LLM Inference | 粗粒度旋转+细粒度分组解决旋转与分组量化的不兼容 / Coarse rotation + fine-grained grouping resolves rotation-vs-group-quantization incompatibility. |
| [[2607.27704]] LightRot: A Light-weighted Rotation Scheme and Architecture for Accurate Low-bit LLM Inference | 分组局部旋转+离群方向对齐，4-bit 困惑度优于 Quarot/SpinQuant / Grouped local rotation + outlier alignment beats QuaRot/SpinQuant at 4-bit precision. |
| [[2607.27705]] Albilich: Steerable Proof-State Orchestration for LLM-Based Mathematical Research with CAS Integration | 持久化证明状态+角色分离验证做数学自动化研究，10 道 RealMath 题全部达到内部已解状态 / Persistent proof-state orchestration solves all 10 RealMath test problems internally. |
| [[2607.27709]] MECA: A Mechanism-Centered Agent for Constructing Well-Specified and Valuable Mathematical Conjectures | 多智能体联合精炼猜想与支撑机制，盲测对齐分从 48.0 提到 69.0 / Multi-agent conjecture-mechanism co-refinement raises blind-reconstruction alignment score by +21. |
| [[2607.27733]] VeriSkill: A Self-Evolution Framework for Program Verification Skills | 归因-抽象-准入流水线做验证技能自演化，PASS 率超最强基线 3.3–17.0 个百分点 / Attribute-abstract-validate skill evolution beats the strongest baseline by 3.3–17.0 PASS points. |
| [[2607.27824]] STEREODISCO: Discovering Stereotypicality in LLMs | 语义差异法系统发现刻板印象轴，LLM 间一致度远高于与人类的一致度 / Discovers stereotype axes in LLM activations; models agree with each other more than with humans. |
| [[2607.27836]] Crossing the Margin Cliff: Toward Relearn-Robust LLM Unlearning via Margin Calibration | 14 种遗忘方法共同收敛到"margin cliff"，即插即用校正大幅提升重学鲁棒性 / 14 unlearning methods share a fragile "margin cliff"; a plug-in fix greatly improves relearning robustness. |
| [[2607.27854]] Simplifying Neural Networks During Training | 在线逆 Fisher 判据检测提取器-隧道分裂点，VGG11/CIFAR-10 削减 94.2% 参数精度不降 / An online inverse-Fisher criterion prunes trailing "tunnel" layers, cutting 94.2% of params with no accuracy loss. |
| [[2607.27861]] Back to All-Entity Ranking: Sampler-Dependent Evaluation in Continuous-Time Dynamic Graphs | 采样负例 MRR 依赖采样器配置，换配置可翻转模型排名 / Sampled-negative MRR for dynamic graphs depends on the sampler and can flip model rankings. |
| [[2607.27888]] Not All Tokens Deserve Equal Credit: Counterfactual Sensitivity Credit Reallocation for Long-CoT Reasoning | 自蒸馏 token 级变化并非按对错反转，衰减高敏感 token 后 AIME25 提升 +6.9 / Self-distillation's token shifts aren't correctness-aligned; downweighting them raises AIME25 by +6.9 points. |
| [[2607.27910]] A Cross-Architecture Audit of Direction-Based Inference-Time Defences in Vision-Language Models | 幅度匹配随机对照审计 5 种越狱防御方向，无一同时占优拒绝恢复与效用保留 / A magnitude-matched audit finds no VLM jailbreak defense Pareto-dominates on both refusal and utility. |
| [[2607.27917]] One Anchor for All: Unified Multilingual and Multimodal Safety Alignment for LVLMs | 英语锚点定位仅占 0.03% 参数的共享安全神经元，跨语言降低攻击成功率 / An English anchor locates ~0.03%-parameter shared safety neurons that cut cross-lingual attack success. |
| [[2607.27933]] The Geometric Nature and a Free Proxy for Flow-Matching Uncertainty | 流匹配不确定性等价于速度场几何偏离，零训练代理逼近需训练的最强基线 / FM uncertainty equals geometric field deviation; a zero-training proxy nearly matches the best trained baseline. |
| [[2607.27958]] Σ-Mem: An Online Reliability Memory for LLM-based Multi-Agent Systems | 谱稳定对称矩阵记录 peer 可信度，对抗基准选择准确率从 46.22% 提到 71.10% / A spectrally-stable reliability memory lifts adversarial peer-selection accuracy from 46.22% to 71.10%. |
| [[2607.27975]] Generalization Bounds on Optimal Control for Transformer Training and Wasserstein Distributional Robustness | Transformer 训练建模为有限 MDP，证明有限样本泛化界，纯理论无实验 / Casts Transformer training as a finite MDP, proving finite-sample generalization bounds; purely theoretical. |
| [[2607.27984]] Share the Judge, Learn the Deferral: Where Specialization Helps LLM Evaluation | 拆分判官为 LoRA 专家损害共享判断，但学习升级路由能让级联更省算力更准 / Splitting a judge into LoRA experts hurts shared judgment, but a learned defer router beats the largest judge more cheaply. |
| [[2607.27995]] Generalization and Trade-off in Adversarial Training: An RKHS Perspective via Kernel Integral Operator | 核算子谱理论证明对抗训练最优速率慢于极小极大速率，并给出去噪修正估计量 / Kernel-operator theory proves adversarial training is slower than the minimax rate, fixed with a debiased estimator. |
| [[2607.28008]] RepBench: Compiling Benchmarks into Capability Representations for Large Language Models | 353 个公开基准编译成 46,149 条审计探针，聚类能力结构与人工分类几乎不吻合 / 353 public benchmarks compiled into 46,149 audited probes; clustered capability structure barely matches the human taxonomy. |
| [[2607.28037]] ClawTrack: Towards Trace-Level Evaluation and Improvement of Real-World Autonomous Agents | 细粒度规则同时打结果分和过程分，过程分筛选 SFT 数据提升 Pass³ 达 +19 个百分点 / Fine-grained rubrics score outcome and process; using process scores to filter SFT data lifts Pass³ by up to +19 points. |
| [[2607.28097]] From Expert Reduction to Behavioral Divergence: Tracing Numerical State through Sparse MoE Inference | 冻结 MoE 局部状态只变归约顺序，多数等价方案偏离原生参考轨迹 / Freezing MoE state and varying only reduction order shows most equivalent schemes diverge from the native reference. |
| [[2607.28128]] Rethinking LLM-Judged Helpfulness as a Pedagogy Signal: A Pre-Registered Audit Across Tutor Models | 通用有用性判分无法区分教学策略优劣，专门量规能完美分离且判官间会反转排序 / General "helpfulness" scores can't distinguish tutoring quality; a dedicated rubric separates them perfectly. |
| [[2607.28196]] Fidelity Is Not Safety: Gently-Compressed LLMs Pass Every Data-Free Quality Guard Yet Invent Procedure Steps in Agentic Execution | 轻度压缩模型通过困惑度和保真度探针却在智能体任务中虚构步骤 / Gently-compressed models pass perplexity/fidelity guards yet invent procedure steps in agentic execution. |
| [[2607.28233]] Demystifying DRAM Read Disturbance: Bridging Experimental Characterization and Device-Level Modeling of RowHammer/RowPress | 真实 DDR4 芯片刻画揭示现有器件模型无法解释的 RowHammer/RowPress 现象 / Real-chip characterization reveals RowHammer/RowPress phenomena that existing device models can't explain. |
| [[2607.28248]] Uncertainty quantification for trustworthy deep learning: Methods and measures | 将不确定性量化的"方法"与"度量"解耦为两条独立分类轴的综述 / A survey decoupling UQ "ensemble-generating methods" from "uncertainty-summarizing measures." |
| [[2607.28263]] Understanding Is Done Early: A Depth Division of Labor in LLMs and Its Use for Unbounded-Context Memory | 中间层单一残差张量缓存替代完整 KV 缓存，RULER 得分大幅超越全上下文基线 / A single mid-layer residual cache replaces full KV cache, beating the full-context baseline on RULER. |
| [[2607.28282]] (Towards) Scalable Reliable Automated Evaluation with Large Language Models | 多 LLM+Elo 聚合评测框架，但单一判官反而略优于聚合且相关性均未达显著 / A multi-LLM + Elo evaluation framework where a single judge slightly outperforms the ensemble, with no significant correlations. |
| [[2607.28292]] CACHE-UK: A Stability-Aware Memory Editor for Sequentially Updated Quantized LLMs in Finance | ROME 式秩一编辑限制在 LoRA 子空间解决 4-bit 量化编辑稳定性危机 / Confining ROME-style edits to a LoRA subspace fixes a 4-bit quantized-LLM "edit stability crisis." |
| [[2607.28308]] Beyond Geometric Complementarity: Coherent Overlap in Sparse Mixture-of-Experts Routing | ESSI 指标证明 MoE 专家子空间高度重叠，反驳几何互补性剪枝依据 / A new ESSI metric shows MoE expert subspaces overlap heavily, contradicting the "geometric complementarity" pruning rationale. |
| [[2607.28317]] One Human, N Agents: Audit-Budget Allocation for LLM Agent Fleets under Miscalibrated, Correlated Confidence | 置信度审计翻转阈值随预算收紧反而升高，多数开源模型置信度近乎抛硬币 / The threshold where confidence-ranked auditing beats random rises as budget shrinks; most open models' confidence is near-chance. |
| [[2607.28319]] Fairness Pruning: Locating Demographic Bias in GLU-MLP Layers via Differential Activations | 差分激活定位偏见神经元，置零保留 99.49% 能力但偏见分数方向不稳定 / Differential-activation bias-neuron localization preserves 99.49% capability but has directionally unstable bias effects. |
| [[2607.28322]] Non-partitioned e-detectors for nonparametric sequential change detection | 不要求分布互斥的"非划分"变点检测框架，检测延迟比基线短约 39% / A "non-partitioned" change-detection framework without disjoint distribution families cuts detection delay ~39%. |
| [[2607.28367]] How Benchmarks Mis-Score Computer-Use Agents | 复核 5 个 CUA 基准发现 15.3% 的 FAIL 判定是错的，验证盲目是真实失败主因 / Re-auditing CUA benchmarks finds 15.3% of FAIL verdicts wrong; verification blindness dominates real failures. |
| [[2607.28405]] QuantWAMs: Calibrating at the Right Granularity for World Action Models | 世界动作模型定制后训练量化，W4A4 下与 FP16 差距仅 0.2–0.7 个百分点 / PTQ tailored to World Action Models stays within 0.2–0.7pt of FP16 at W4A4 while generic baselines collapse. |
| [[2607.28421]] When Derived Measurements Mislead: Quantifying and Mitigating LLM Over-Trust with Privileged-Modality Reliability Evidence | 提出并量化"衍生特征过度信任"失效模式及蒸馏修复方案 / Formalizes "derived-feature over-trust" and mitigates it via privileged-signal distillation into reliability scores. |
| [[2607.28434]] Metaphor Tracer: A Theory-Informed Analysis of Hidden States | 无需训练的双通道隐藏状态读数工具，在临床访谈标注上 34/36 命中 / A training-free two-channel hidden-state reader hits 34/36 directional cells against clinical-transcript annotations. |
| [[2607.28495]] Stage-Replay Divergence Follows the KV Cache: Fixed-Prefix Precision Controls and Bidirectional Cache Transplantation | 相同前缀重放在 BF16 下 83% 概率与保留 KV 缓存分叉，移植缓存后 100% 跟随捐赠者 / Identical-prefix replay diverges from a live KV cache 83% of the time in BF16; cache transplantation makes recipients 100% follow the donor. |
| [[2607.28527]] MANTA: Multi-Agent Network Topology Adaptation for Self-Evolving Multi-Agent Systems | 推理阶段动态调整多智能体拓扑，平均分超最强基线 5.8 分但优势来自稳定性 / Inference-time topology adaptation beats the strongest baseline by 5.8 points on average, driven by consistency not per-task dominance. |
| [[2607.28568]] Frontis-MA1: Training an AI4AI Model towards Recursive Self-Improvement in Machine Learning Engineering | 训练进化算子并部署回搜索框架，35B 智能体 MLE-Bench Lite 奖牌均值提升到 71.21% / Training evolutionary operators and redeploying them lifts a 35B agent's MLE-Bench Lite Medal Average to 71.21%. |
| [[2607.28576]] Sample More, Reflect Less: Self-Refine and Reflexion Lose to Repeated Sampling at Equal Token Cost, from 1.5B to 7B | 等 token 成本下自我修正方法在全部 18 项对比中都不敌简单多采样投票 / Self-correction methods lose to plain repeated-sampling voting in all 18 token-cost-matched comparisons. |
| [[2607.28589]] MixFrag: Fragility-Guided Mixed-Precision Post-Training Quantization for Vision Transformers | KL 散度脆弱度+背包比特分配，COCO 检测超前最优 9.6 AP 但 ImageNet 分类落后 / KL-divergence fragility plus knapsack bit allocation beats the prior best on COCO by 9.6 AP but trails baselines on ImageNet. |
| [[2607.28607]] Inducing Language Models to Assert Their Own Consciousness Restores Human Beliefs and Values | 抑制"自称有意识"的安全微调连带压制非人类心智归因和宗教信念，可用转向逆转 / Safety training suppressing self-consciousness claims also suppresses non-human mind attribution and religious belief; steering reverses this. |
| [[2607.28608]] KAISEN: Reproducible Subgroup Fairness Auditing for Clinical Risk Models | 合成基准压力测试临床公平性审计流程，按组阈值优化优于按组 Platt 校准 / A synthetic benchmark stress-tests a clinical fairness-audit pipeline; per-group threshold optimization beats per-group Platt calibration. |
| [[2607.28609]] OSReward: Instituting Standardized Evaluation for Cross-Platform Computer-Use Reward Models | 首个跨平台 CUA 判官可靠性基准，开源奖励模型以更低成本逼近商用水平 / The first cross-platform CUA-judge reliability benchmark; released open reward models approach commercial-judge accuracy at far lower cost. |
