---
title: "Weekly arXiv Digest — 2026-06-22–2026-06-26"
week: 2026-0622-0628
date_range: ["2026-06-22", "2026-06-26"]
tags:
  - mechanistic-interpretability
  - self-evolving-agents
  - autonomous-research
  - quantization
  - llm-evaluation
  - training-theory
papers: 189
---

# Weekly arXiv Digest — 2026-06-22–2026-06-26

> 本周汇总 2026-06-22 至 2026-06-26 五日日报共 189 篇去重论文，主线为自进化与自主研究智能体、机制可解释性与表示几何、量化压缩与高效推理、评测与可靠性、训练动力学与理论。
> A weekly rollup of 189 deduplicated papers (2026-06-22 → 2026-06-26) organized around self-evolving/autonomous agents, mechanistic interpretability & representation geometry, quantization/compression & efficient inference, evaluation & reliability, and training dynamics & theory.

---

## 本周必读 / Must Read This Week

### [[2606.26650]] CAT-Q: Ternary Quantization for LLMs

> 推荐理由（中）：仅用 512 校准样本（~1M tokens）即可将 1.7B–235B 的预训练 LLM 量化为 1.58-bit 三值模型，性能超越用 100B tokens 训练的 BitNet，训练 token 减少约 10 万倍、235B 模型 60 GPU-小时完成——把极低比特 PTQ 从"奇技"变为可落地现实，直接决定前沿模型能否上消费/边缘硬件。（连续两日入选 06-25/26）
>
> Why read (EN): CAT-Q turns ternary (1.58-bit) post-training quantization from a curiosity into a deployable reality, beating QAT-trained BitNet with ~100,000x fewer tokens and quantizing a 235B model in 60 GPU-hours — a step change for edge/consumer deployment of frontier-scale LLMs. (recurred 06-25/26)

### [[2606.26749]] Transient Semantic Geometry in Next-Token

> 推荐理由（中）：揭示一个反直觉现象——严格 one-hot 监督下 Transformer 仍在训练早期自发形成语义聚类几何，但该结构是短暂的，随容量/时间最终塌缩为神经坍塌预测的对称 ETF；调和了"神经坍塌抹除语义"与"语言模型显然学到语义"之间的长期张力。（连续两日入选 06-25/26）
>
> Why read (EN): Under strict one-hot supervision, transformers spontaneously form semantic geometry early in training as a transient phase, then collapse to the neural-collapse-predicted ETF geometry — reconciling "neural collapse erases semantics" with "LLMs plainly learn semantics." (recurred 06-25/26)

### [[2606.26836]] Capability Frontier: Benchmarks Miss 82%

> 推荐理由（中）：传统单模型、单次运行的基准评测系统性低估 LLM 真实能力。在 21 模型 × 16 基准上，仅纠正单模型偏差即可把错误率降低 54%，叠加单次采样纠正后达 82%，并以 85% 成本匹配 SOTA——直击评测方法论与推理时算力扩展。（连续两日入选 06-25/26）
>
> Why read (EN): Standard single-model, single-run benchmarks systematically understate LLM capability; across 21 models × 16 benchmarks, debiasing alone cuts error 54% (82% with single-sample correction) while matching SOTA at 85% cost — directly relevant to eval methodology and inference-time scaling. (recurred 06-25/26)

### [[2606.20657]] A-Evolve-Training

> 推荐理由（中）：首次在前沿规模（30B 参数、多周 H200 集群训练）公开报告全自主后训练系统，在 NVIDIA Nemotron-Reasoning Challenge 达 0.86（人类最佳 0.87，排名 8/~4000）；更关键的是系统自主检测到内部开发指标已成误导代理并主动反转搜索策略，展示了超越固定框架优化的"发现"能力。（06-22 必读）
>
> Why read (EN): First public autonomous post-training at frontier scale (30B, multi-week H200 runs); scores 0.86 on Nemotron-Reasoning Challenge (human best 0.87). The loop autonomously detected its dev metric had become a misleading proxy and reversed its search policy — evidence of discovery beyond fixed-frame optimization. (06-22)

### [[2606.05080]] AutoLab

> 推荐理由（中）：用 36 个跨系统优化/谜题/模型开发/CUDA kernel 的真实任务、2544 壁钟小时评 17 个前沿模型，揭示决定胜负的不是一次性代码质量而是持续迭代、反馈吸收与时间感知；harness 消融证明智能体基础设施单独即可让同模型分数摆动高达 0.43。（06-23 必读）
>
> Why read (EN): AutoLab benchmarks 17 frontier models on 36 ultra long-horizon tasks (2,544 wall-clock hours): the dominant success predictor is persistence (iterating, absorbing feedback, time awareness), not one-shot quality; a harness ablation shows framework design alone can swing scores by up to 0.43. (06-23)

### [[2606.09052]] INFUSER

> 推荐理由（中）：把"求解器–生成器协同自演化"的目标从难度启发式换成"对当前求解器有用"，用优化器感知的影响力分数驱动生成器奖励并配 DuGRPO；Qwen3-8B 在 Olympiad/SuperGPQA 相对提升 >20%，8B 共演化生成器在数学/代码上超过冻结 32B 思维生成器——"有用 > 大 > 难"。（06-23 必读）
>
> Why read (EN): INFUSER replaces difficulty heuristics with an optimizer-aware influence score as the generator's reward (with DuGRPO for continuous noisy signals); Qwen3-8B gains >20% on Olympiad/SuperGPQA, and an 8B co-evolving generator beats a frozen 32B thinking generator on math/code. (06-23)

### [[2606.25519]] Quantization Inflates Reasoning

> 推荐理由（中）：揭示被标准量化评测掩盖的真实代价——低比特量化让推理模型即使保持正确率也生成明显更长的思维链（CTIR 度量），这一隐藏的测试时开销直接侵蚀量化本应带来的每 token 加速——量化与推理这两条主线在本周正面相撞。（06-24 必读）
>
> Why read (EN): Exposes a hidden cost standard quantization evals miss — low-bit quantization makes reasoning models emit substantially longer CoT (the CTIR metric) even when accuracy holds, eroding the very per-token speedup quantization is meant to deliver. (06-24)

### [[2606.27288]] Co-Failure Ceiling on Routing, Voting, and Mixture-of-Agents

> 推荐理由（中）：证明任何 LLM 选择策略（路由/投票/级联/MoA）的准确率上限是 1−β（所有模型同时答错的比例），而非业界惯用的成对错误相关性 ρ；67 个前沿模型上 ρ 系统性低估共失败尾部约 2.5 倍，β 可转化为零成本的部署前 Clopper–Pearson 证书。（06-26 必读）
>
> Why read (EN): Proves the accuracy ceiling of any LLM orchestration is 1−β (the all-models-wrong rate), not pairwise error correlation ρ — which underestimates the co-failure tail ~2.5x across 67 frontier models; β yields a $0 pre-deployment Clopper–Pearson certificate. (06-26)

---

## 本周主题脉络 / Themes This Week

### 1. 自进化与自主研究智能体 / Self-Evolving & Autonomous Agents

> 本周体量最大的主线（~40 篇）。周一以 A-Evolve-Training 展示前沿规模的全自主后训练开场；周二是一整波自进化智能体（AutoLab 长时程评测、OpenSkill 开放世界技能、INFUSER 影响函数驱动数据生成）；周末转向技能库与记忆固化（SkillDisCo、MemStrata）与自主科学发现（AHOIS、meta-optimization）。脉络从"智能体能否自我改进"走向"它把改进固化为什么样的显式 artifact"。
>
> The week's largest thread (~40 papers). Monday opened with frontier-scale fully-autonomous post-training; Tuesday was a dedicated wave of self-evolving agents; late week pivoted to skill libraries/memory consolidation and autonomous science. The arc moves from "can agents self-improve" to "what do they consolidate improvements into."

代表论文 / Highlights: [[2606.20657]] · [[2606.05080]] · [[2606.06741]] · [[2606.09052]] · [[2606.26722]] · [[2606.27376]]

### 2. 机制可解释性与表示几何 / Mechanistic Interpretability & Representation Geometry

> 两条子线本周交叉推进：一是 SAE/电路定位（RL 工具调用被定位到单个 crosscoder 特征、Qwen3 全层 SAE 套件），二是表示几何（瞬态语义几何最终塌缩为神经坍塌 ETF、安全微调继承的电路引入规避漏洞）。06-25/26 的反复簇显示"电路即监控"正成为新范式。
>
> Two sublines crossed this week — SAE/circuit localization and representation geometry (transient semantic geometry collapsing to the neural-collapse ETF; inherited circuits creating evasion holes). The recurring 06-25/26 cluster signals a maturing "circuits as monitoring" turn.

代表论文 / Highlights: [[2606.26749]] · [[2606.26474]] · [[2606.26620]] · [[2606.27091]] · [[2606.27321]]

### 3. 量化、压缩与高效推理 / Quantization, Compression & Efficient Inference

> 效率主线本周既有旗舰也有反例：CAT-Q 让 1.58-bit 真正可部署，而 Quantization Inflates Reasoning 警告低比特模型会生成更长的 CoT、侵蚀加速收益。其余工作攻向 KV 缓存压缩、稀疏×FP4、投机解码，并首次揭示低比特量化与深层/递归推理架构之间的耦合失效模式。
>
> The efficiency thread had a flagship (CAT-Q making 1.58-bit deployable) and a cautionary counterpoint — Quantization Inflates Reasoning. Other work attacked KV cache, FP4×sparsity, speculative decoding, and surfaced a new tension between quantization and deep/recurrent reasoning architectures.

代表论文 / Highlights: [[2606.26650]] · [[2606.25519]] · [[2606.26587]] · [[2606.26488]] · [[2606.26875]]

### 4. 评测、可靠性与推理分析 / Evaluation, Reliability & Reasoning Analysis

> 评测方法论本周持续被审视：基准漏掉 82% 的能力、共失败率 β（而非 ρ）封顶多模型编排、长时程胜负取决于坚持而非一次性质量、Cliff Tokens 定位使正确率坍缩的单 token。共同信息——我们如何测量，和测量对象本身一样需要修复。
>
> Evaluation methodology was under scrutiny all week: benchmarks miss 82% of capability; co-failure rate β (not ρ) caps orchestration; long-horizon success is about persistence; cliff tokens localize single-token reasoning collapse. The shared message — how we measure is as broken as what we measure.

代表论文 / Highlights: [[2606.26836]] · [[2606.27288]] · [[2606.25524]] · [[2606.26935]] · [[2606.26502]]

### 5. 训练动力学、优化与理论 / Training Dynamics, Optimization & Theory

> 理论本周同步推进：Internalization 给出 CoT 如何压缩进权重的首个可证明刻画（宽度胜过深度）；算法基础论文以电路复杂度重铸表达能力；多项工作给出新收敛证明（原始 Adam 在非光滑非凸下收敛），并伴随 Muon/优化器系统的成熟（DMuon、Hierarchical Muon）。
>
> Theory kept pace: Internalization gave the first provable account of how CoT compresses into weights (width beats depth); the algorithmic-foundations paper recast expressivity via circuit complexity; new convergence proofs (original Adam in nonsmooth nonconvex) arrived alongside Muon/optimizer-systems maturation.

代表论文 / Highlights: [[2606.20937]] · [[2606.26705]] · [[2606.22326]] · [[2606.27153]] · [[2606.26466]]

---

## 全部论文 / All Papers

### 2026-06-22 (50)

- [[2606.20622]] Darwin Mobile Agent — 首个开源RL移动GUI智能体训练系统+自进化路线图 / First open-source RL training system for mobile GUI agents.
- [[2606.20625]] AlphaMemo — 结构化搜索过程记忆改进LLM驱动的alpha因子挖掘 / Structured search-process memory improves LLM-driven alpha mining.
- [[2606.20657]] A-Evolve-Training — 30B规模全自主后训练，自主检测代理指标失效 / 30B autonomous post-training with self-detected proxy failure. ⭐
- [[2606.20662]] Confidence Laundering — 多智能体"置信度洗白"失效与潜在不确定性载体 / Multi-agent confidence laundering and latent uncertainty carriers.
- [[2606.20678]] IGSD — Sobol配对干预分解Transformer内容通道与基底角色 / Sobol paired interventions decompose content vs. substrate roles.
- [[2606.20743]] Ledger Residuals — 巨大激活值在保护通道中仍重建，证明功能必需性 / Massive activations rebuild in protected channel; functionally necessary.
- [[2606.20814]] EM Training Dynamics — 涌现式对齐失败由域内损失主导，预训练激活可预测脆弱性 / Emergent misalignment dominated by in-domain loss; activations predict vulnerability.
- [[2606.20820]] CELEUS — E-process任意时刻有效置信区间，评估样本减少54-62% / E-process anytime-valid CIs cut evaluation samples 54-62%.
- [[2606.20839]] PRTE — 过程奖励策略演化用于长程生物信息学工作流 / Process-reward tactic evolution for long-horizon bioinformatics workflows.
- [[2606.20936]] Token-Level Hybrid — 混合模型优势集中在状态依赖内容词，结构匹配偏向Transformer / Hybrid advantage on state-conditioned words; structural closure favors transformer.
- [[2606.20937]] Internalization — CoT内化偏好宽度、素数更难，首个可证明内化保证 / CoT internalization favors width, primes harder; first provable guarantee. ⭐
- [[2606.20945]] GQE — GQA组内query头MoE路由，56%激活匹配基线精度 / MoE on GQA query heads: 56% activation matches baseline accuracy.
- [[2606.20959]] TAS — 推理时三阶段干预恢复LLM被压制的新事实 / Test-time 3-stage steering recovers suppressed newer facts.
- [[2606.21023]] HEAL — INT16+代数补偿实现FP32级推理可复现性，比FP32快7.1x / INT16 + algebraic compensation gives FP32-level reproducibility, 7.1x faster. ⭐
- [[2606.21158]] DDS — 廉价谱可观测量替代SGLD采样读取奇异复杂度，成本降300x / Cheap spectral observables replace SGLD for singular complexity, ~300x cheaper.
- [[2606.21228]] Sakana Fugu — 学习型LLM编排器多基准超越所有单一前沿模型 / Learned orchestrator beats each frontier model individually on multiple benchmarks.
- [[2606.21249]] RoPE-Retrieval — RoPE低频维度是检索头因果关键轴 / Low-frequency RoPE dims are the causal axis for retrieval heads.
- [[2606.21255]] SCOPE — 保形预测+E-process构建LLM服务OOD拒绝门控 / Conformal + e-process OOD rejection gate for LLM services.
- [[2606.21345]] Factual Retrieval Paths — 事实检索是冗余分布式非连续过程 / Factual retrieval is redundant, distributed, non-contiguous.
- [[2606.22326]] Adam Nonsmooth — 原始Adam在非光滑非凸优化中首个收敛证明 / First convergence proof for original Adam in nonsmooth nonconvex.
- [[2606.22406]] Softmax Signal Recovery — Softmax注意力训练渐近恢复隐藏信号方向的严格证明 / Rigorous proof: softmax attention training recovers hidden signal direction.
- [[2606.22511]] VCM — PMI+方差惩罚打破解码似然陷阱，提升多样性保推理 / PMI + variance penalty breaks likelihood trap; improves diversity, preserves reasoning.
- [[2606.22570]] ACPO — off-policy程度决定token梯度主导权，自适应裁剪超越DAPO / Off-policy degree determines token gradient dominance; ACPO beats DAPO.
- [[2606.22627]] ORE — 正交投影消除批量知识编辑语义纠缠 / Orthogonal projection decouples semantic entanglement in batch editing.
- [[2606.22798]] RAD — MoE路由模式作为推理rollout选择的无字符串信号 / MoE routing as string-free signal for reasoning rollout selection.
- [[2606.22826]] MINCE — 蒙特卡罗N值确定缩减评估基准规模，MMLU -89% / Monte Carlo N-sizing shrinks benchmarks; MMLU -89%.
- [[2606.22942]] KD Post-Training — 后训练知识蒸馏低数据优于SFT，大数据退化 / Post-training KD beats SFT in low-data; degrades at scale.
- [[2606.23175]] CAWM — AI科学家"正确答案错误机制"失效模式 / "Correct Answer, Wrong Mechanism" failure in AI scientists.
- [[2606.23195]] Memory Contagion — 评估器偏差通过记忆跨时间传播，无安全阈值 / Evaluator bias propagates via memory; no safe threshold.
- [[2606.23235]] MFC Transformer — 均场控制理论分析Transformer残差层+Pontryagin条件 / Mean field control analysis of transformer layers + Pontryagin conditions.
- [[2606.23276]] KE Illusion of Erasure — 知识编辑"擦除假象"——编辑后知识可对抗恢复 / Knowledge editing "illusion of erasure" — edited knowledge is recoverable.
- [[2606.23277]] GIF — 几何信息流控制防御LLM提示注入 / Geometric information flow control defends prompt injection.
- [[2606.23345]] Abstract Geometry — LLM推理时形成类海马体正交几何，几何正则化增强推理 / Hippocampal-like orthogonal geometry in LLMs; GeoStruct enhances inference.
- [[2606.23357]] SOAP-Bubbles — 结构化权重不确定性的变分贝叶斯深度学习 / Structured weight uncertainty for variational Bayesian deep learning.
- [[2606.23364]] GD Beyond NTK — 超越NTK范式的通用架构GD收敛框架 / GD convergence framework for general architectures beyond NTK.
- [[2606.23394]] LLM Embedding Expert — RSA分析LLM嵌入空间能否恢复专家概念结构 / RSA probes LLM embedding recovery of expert concept structures.
- [[2606.23403]] Litmus — 零标签代码驱动AI评估指标自动设计 / Zero-label code-driven automatic metric specification for AI.
- [[2606.23404]] ReasoningLens — LRM思维链层级可视化与诊断审计框架 / Hierarchical CoT visualization and diagnostic auditing for LRMs.
- [[2606.23406]] HyperQuant — Hadamard+格量化+Rice编码的统一无数据PTQ / Hadamard + lattice + Rice coding unified data-free PTQ.
- [[2606.23419]] GRINQH — 激活感知动态精度分配，2-4 bit有效位宽超越GPTQ/AWQ / Activation-aware dynamic precision: 2-4 bit effective beats GPTQ/AWQ.
- [[2606.23525]] SelfCompact — 无训练自压缩脚手架，数学+18.1分/成本-70% / Training-free self-compaction: +18.1 pts math, -70% cost.
- [[2606.23546]] Energy Scaling — Roofline启发的Transformer微调能耗缩放律 / Roofline-inspired transformer fine-tuning energy scaling law.
- [[2606.23568]] SVD-Surgeon — OBS框架在奇异值基底修复SVD压缩损失 / OBS in singular-value basis repairs SVD compression loss.
- [[2606.23583]] Evaluation Awareness — 评估感知三轴分解+基准幻觉概念 / Evaluation awareness 3-axis decomposition + benchmark illusion.
- [[2606.23590]] Topology Ill-Posed — 持久同调检测病态问题+拓扑条件激活引导 / Persistent homology detects ill-posed questions + topology-conditioned steering.
- [[2606.23591]] Influence vs Similarity — 数据影响与数据相似性一致性量化 / Quantifies data-influence vs. data-similarity agreement.
- [[2606.23607]] LMC-DM — 双向学习匹配实现十亿参数模型合并 / Dual learned matching for billion-parameter model merging.
- [[2606.23637]] AngularMuown — Muown隐式黎曼优化+显式角步长调度~2x AdamW / Muown is implicit Riemannian; angular scheduling yields ~2x over AdamW.
- [[2606.23670]] Tapered LMs — MLP宽度沿深度余弦衰减，零代价提升性能 / Cosine-tapering MLP width improves performance at zero extra cost.
- [[2606.23676]] AdamW Heavy-Tailed — 开放问题：AdamW在重尾噪声下能否匹配符号优化器 / Open problem: AdamW vs. sign optimizers under heavy-tailed noise.

### 2026-06-23 (50)

- [[2606.00027]] Medical Red Teaming Framework — 4
- [[2606.00079]] BitsMoE — 4
- [[2606.00365]] SPARQLe — 4
- [[2606.00390]] Zamba2-VL — 4
- [[2606.00539]] GNMR — 4
- [[2606.01075]] Generalization Gap in Self-Evolving Reasoning — 4
- [[2606.01314]] SkillSmith — 4
- [[2606.01400]] MIS Prompt Selection — 4
- [[2606.01479]] SAE Emotion TTS — 4
- [[2606.01640]] MobEvolve — 4
- [[2606.01770]] Adaptive Auto-Harness — 4
- [[2606.01850]] Conformal Prediction Compression — 4
- [[2606.01961]] AutoMedBench — 4
- [[2606.01993]] MMG2Skill — 4
- [[2606.02215]] EvoNote — 4
- [[2606.02288]] INSERTQUANT — 5
- [[2606.02484]] Iteris — 4
- [[2606.02628]] Hallucination Linear Decodable — 5
- [[2606.02812]] Traj-Evolve — 4
- [[2606.02907]] Linear Probes — 4
- [[2606.03002]] SAE Feature Damage — 4
- [[2606.03056]] SkillDAG — 4
- [[2606.03085]] Multi-Component Causal Tracing — 5
- [[2606.03099]] PhotoCraft — 4
- [[2606.03678]] EvoDrive — 4
- [[2606.03692]] SkillPyramid — 4
- [[2606.03780]] Expert-Aware MoE Causal Tracing — 5
- [[2606.03841]] EvoDS — 4
- [[2606.03979]] Sleep for LLMs — 4
- [[2606.04465]] SePO — 4
- [[2606.04507]] SCORE — 5
- [[2606.04536]] TMEM — 4
- [[2606.04703]] ExpInternalization — 5
- [[2606.05080]] AutoLab — 5 ⭐
- [[2606.05346]] Trajectory Extrapolation Error — 4
- [[2606.05433]] ZK Frontier Training — 4
- [[2606.05513]] EpiEvolve — 4
- [[2606.05661]] CL-Bench — 4
- [[2606.06473]] MLEvolve — 4
- [[2606.06510]] FP8 is All You Need — 4
- [[2606.06521]] P-Cast FP8 — 4
- [[2606.06741]] OpenSkill — 5 ⭐
- [[2606.06857]] Sparse Features Brain — 5
- [[2606.07720]] AGCLR — 4
- [[2606.08405]] Self-Evolving Fluid Agent — 5
- [[2606.09052]] INFUSER — 5 ⭐
- [[2606.09686]] t27 Numeric Catalog — 4
- [[2606.11244]] SPEAR — 4
- [[2606.11357]] TileFuse — 4
- [[2606.19526]] SPINE — 5

### 2026-06-24 (29)

- [[2606.25269]] Stabilizing black-box via task-oriented randomization — 自适应扰动输入并集成以稳定黑箱输出，提供 (s,δ) 稳定性保证。Adaptively perturb inputs and ensemble to stabilize black-box outputs with (s,δ)-stability guarantees.
- [[2606.25296]] SafeGen — LLM+形式化验证从文档自动生成功能安全断言并分级故障。LLM + formal verification auto-generates functional-safety assertions and grades faults from documents.
- [[2606.25335]] Stagnant Neuron (KNIFE) — MARL 价值分解可塑性丧失源于停滞神经元，KNIFE 做神经元级修复。MARL value-factorization plasticity loss stems from stagnant neurons; KNIFE repairs them neuron-by-neuron.
- [[2606.25366]] AMPLE-GNC — 可靠性非对称航天器 GNC 栈，学习模块外包验证安全盾。Reliability-asymmetric spacecraft GNC stack wrapping learned modules in a verified shield.
- [[2606.25371]] Conformal Recovery-Deadline Certificates — conformal 上界设恢复截止期限，解耦自适应控制器的自主性与安全性。Conformal upper bound sets a recovery deadline, decoupling autonomy from safety for adapting controllers.
- [[2606.25374]] Spacecraft FTC Honest Benchmark — 诚实基准证明结构优于裸学习，自校正观测器破 0% 硬墙。Honest benchmark shows structure beats raw learning; self-correcting observer breaks a 0% wall.
- [[2606.25402]] LibEvoBench — 多版本代码生成基准，揭示 LLM 对 API 版本基本无感。Multi-version code-gen benchmark showing LLMs are essentially version-oblivious to APIs.
- [[2606.25426]] Above the Inner Loop (M1 AMX) — M1 AMX 上手写 fp32 GEMM 以内循环之上杠杆超越 Accelerate。Hand-tuned fp32 GEMM on M1 AMX beats Accelerate via above-the-inner-loop levers.
- [[2606.25453]] EmuGEMM — INT8 Tensor Core 模拟高精度 GEMM 的融合内核，Hopper 1639 Top/s。Fused kernels emulate high-precision GEMM via INT8 tensor cores, 1,639 Top/s on Hopper.
- [[2606.25459]] Probing Mandarin Sub-dialects — 无监督发音探针揭示 wav2vec 2.0 北京话过拟合与层级化跨方言结构。Unsupervised articulatory probing reveals wav2vec 2.0's Beijing-centric overfitting and hierarchical cross-dialect structure.
- [[2606.25487]] Jailbreak Judge Reliability — 审计越狱评测判官，专用分类器与 LLM-judge 以相反方式失效。Audits jailbreak judges; classifiers and LLM-judges fail in opposite ways.
- [[2606.25519]] Quantization Inflates Reasoning — 低比特量化使推理模型生成更长思维链(CTIR)，侵蚀加速。Low-bit quantization makes reasoning models emit longer CoT (CTIR), eroding speedup. ⭐
- [[2606.25524]] Cliff Tokens — 识别推理轨迹中使正确率坍缩的单 token 并训练高效 Cliff-DPO。Identifies the single token where answer-probability collapses and trains token-efficient Cliff-DPO. ⭐
- [[2606.25532]] Agentic Compression Discovery — 进化知识图谱多智能体自动设计硬件感知压缩，部署 235B 模型。Evolutionary-KG multi-agent engine auto-designs hardware-aware compression, deploys a 235B model.
- [[2606.25562]] MSDF CNN FPGA Accelerator — MSDF 数字串行融合乘加 FPGA 卷积器，U-Net 15.14 GOPS/W。MSDF digit-serial fused-multiply-add FPGA convolver, 15.14 GOPS/W on U-Net.
- [[2606.25601]] Statistically Valid Hyperparameter Selection — LTT 把超参选择重述为多重假设检验并给有限样本保证。LTT recasts hyperparameter selection as multiple hypothesis testing with finite-sample guarantees.
- [[2606.25605]] Constraint Tax in Open-Weight LLMs — 同时开 Tool Calling 与 JSON Schema 让多个开源模型停止调用工具(100%→0%)。Enabling Tool Calling + JSON Schema jointly stops multiple open-weight models calling tools (100%→0%).
- [[2606.25657]] Joint Sparse Autoencoders (JSAE) — 跨模态稀疏自编码器对齐图像/文本隐码，实现可解释 VLM steering。Cross-modal sparse autoencoders align image/text codes for interpretable VLM steering.
- [[2606.25674]] BitNet Text Embeddings (BITEMBED) — 三值权重 LLM 嵌入编码器，MMTEB 接近全精度、CPU 吞吐 ~2×。Ternary-weight LLM embedding encoder matches FP teachers on MMTEB at ~2× CPU throughput.
- [[2606.25743]] Black-Box Assisted Regression — 黑箱先验非参数回归的极小化刻画与相变，提出 Safe Residual Estimator。Minimax characterization and phase transition for black-box-prior regression; proposes Safe Residual Estimator.
- [[2606.25745]] MFVI Overestimates Predictive Variance — "MFVI 低估方差"不完整，ID 测试点反而高估并与冷后验效应关联。"MFVI underestimates variance" is incomplete; it overestimates for ID points and links to the Cold Posterior Effect.
- [[2606.25750]] RAS (Refusal Alignment Score) — 白盒从隐藏状态测拒绝方向对齐度，比判官评测快 ~210×。White-box score from hidden-state refusal-direction alignment, ~210× faster than judge evals.
- [[2606.25760]] ARGUS (UQ for Computer-Use Agents) — 首个 GUI 点击定位不确定性量化跨场景基准，揭示选择性迁移。First cross-regime UQ benchmark for GUI grounding, revealing selective transfer.
- [[2606.25777]] Space-Efficient Language Generation — 空间受限学习者在 DFA 类上的极限生成能力刻画。Characterizes space-bounded language generation in the limit over DFA classes.
- [[2606.25797]] Confidence Sequences for MDP-SMC — 置信序列修复并加速 MDP 在线统计模型检验，平均省 50× 样本。Confidence sequences fix and accelerate online MDP statistical model checking, ~50× fewer samples.
- [[2606.25819]] ToolBench-X — 注入五类可恢复危害的工具使用基准，最强模型 <60%，瓶颈在诊断。Tool-use benchmark injecting five recoverable hazards; best agent <60%, bottleneck is diagnosis. ⭐
- [[2606.25821]] SARA (Semantically Anchored Routing Alignment) — 以高资源路由分布为锚对齐低资源 MoE 路由，提升多语能力。Aligns low-resource MoE routing to high-resource anchors, improving multilingual capability.
- [[2606.25879]] AI-Assisted Reproducibility (FABRIC) — FABRIC + Claude/LoomAI 结论级复现方法学，AI 提速 ~4–6×。FABRIC + Claude/LoomAI conclusion-level reproducibility methodology, ~4–6× faster.
- [[2606.25882]] Posterior Collapse in Deep GPs — 重新解释 PCA 先验均值与白化在变分深度 GP 中的真正机理。Re-explains the real mechanism of the PCA prior mean and whitening in variational Deep GPs.

### 2026-06-25 (41)

- [[2606.26466]] SOLAR: Soft Token Alignment for Cross-Lingual Reasoning — RL & Training
- [[2606.26472]] EpiKV: Attention-Free KV Cache Eviction — Quantization & Inference
- [[2606.26474]] RL Tool Use Localized to a Single Crosscoder Feature — Interpretability ↻06-26
- [[2606.26488]] Compressing a Recursive Reasoner for the Edge — Quantization & Inference ↻06-26
- [[2606.26492]] Evaluation-Strategy Gap in DL Fault Diagnosis — Evaluation & Reliability ↻06-26
- [[2606.26502]] Humans Disengage, Reasoning Models Persist — Interpretability ↻06-26
- [[2606.26511]] MemStrata: Temporal Validity Memory for Agents — Autonomous Agents
- [[2606.26523]] Radical AI Interpretability (philosophy) — Interpretability ↻06-26
- [[2606.26547]] ApproxHDC: Approximation Tuning for HDC — Hardware & Systems
- [[2606.26578]] EvoOptiGraph: Weakness-Driven Coevolution — Autonomous Agents
- [[2606.26585]] Validation for AI Telescope Scheduling — Evaluation & Reliability
- [[2606.26587]] SharQ: Sparsity + FP4 Quantization — Quantization & Inference ↻06-26
- [[2606.26620]] Millions of Interpretable SAE Features (Qwen3) — Interpretability ↻06-26
- [[2606.26629]] SAE-Guided Activation Reg for Continual Learning — Interpretability ↻06-26
- [[2606.26650]] CAT-Q: Ternary Quantization for LLMs — Quantization & Inference ⭐ ↻06-26
- [[2606.26666]] PersistentKV: Page-Aware Decode Scheduling — Hardware & Systems
- [[2606.26671]] NebulaExp-8B: Post-Training Ablation — RL & Training ↻06-26
- [[2606.26701]] SegFold: Sparse GEMM Dynamic Dataflow — Hardware & Systems
- [[2606.26722]] AHOIS: Socratic Agents for Discovery — Autonomous Agents ↻06-26
- [[2606.26728]] Scientific Discovery as Meta-Optimization — Autonomous Agents ↻06-26
- [[2606.26744]] HyperDFlash: Block Speculative Decoding — Quantization & Inference ↻06-26
- [[2606.26749]] Transient Semantic Geometry in Next-Token — Interpretability ⭐ ↻06-26
- [[2606.26783]] AlphaEdit Reproducibility Study — Evaluation & Reliability ↻06-26
- [[2606.26797]] Reasoning Quality Emerges Early (TEMP) — RL & Training
- [[2606.26806]] Memory Depth: Selective Parametric Consolidation — Autonomous Agents ↻06-26
- [[2606.26822]] Quantization in Federated Learning (Survey) — Quantization & Inference ↻06-26
- [[2606.26836]] Capability Frontier: Benchmarks Miss 82% — Evaluation & Reliability ⭐ ↻06-26
- [[2606.26875]] InfoKV: Information-Aware Cache Compression — Quantization & Inference ↻06-26
- [[2606.26917]] GEOALIGN: Geometric Rollout Curation for RL — RL & Training ↻06-26
- [[2606.26935]] Where Do CoT Training Gains Land? — Interpretability ↻06-26
- [[2606.26982]] Framing-Sensitive Behavioral Instability — Interpretability ↻06-26
- [[2606.26987]] Emotion Vectors in Open-Source LLMs — Interpretability ↻06-26
- [[2606.26997]] RolloutPipe: Pipelined Rollout & Training — Hardware & Systems ↻06-26
- [[2606.27009]] Semantic Early-Stopping Agent Loops — Autonomous Agents
- [[2606.27023]] Verbalized Uncertainty Calibration (Med VQA) — Evaluation & Reliability
- [[2606.27091]] Inherited Circuits Evasion Vulnerabilities — Interpretability ⭐ ↻06-26
- [[2606.27098]] Residual GPU Cache State on Apple M4 Pro — Hardware & Systems
- [[2606.27153]] DMuon: Distributed Muon Training — Hardware & Systems ↻06-26
- [[2606.27199]] Forecasting via SAE Feature Steering — Interpretability
- [[2606.27216]] Hierarchical Muon: Tiled Newton-Schulz — Hardware & Systems ↻06-26
- [[2606.27226]] BINEVAL: Binary Questions for Evaluation — Evaluation & Reliability

### 2026-06-26 (19)

- [[2606.26493]] Nemotron-TwoTower: Diffusion Language Modeling with Pretrained Autoregressive Context — diffusion-language-model, masked-diffusion, large-language-model, mixture-of-experts, mamba
- [[2606.26529]] The Inattentional Gap — ai-safety, inattentional-blindness, llm-evaluation, vision-language-models, radiology-ai
- [[2606.26538]] CascadeFormer — transformer-architecture, model-efficiency, layer-pruning, gradient-analysis, residual-networks
- [[2606.26560]] Erase-then-Delta Attention — linear-attention, delta-rule, recurrent-memory, efficient-LLM, hybrid-architecture
- [[2606.26621]] λ-PSD: Scalable Approximate SNR-Optimised Polynomial Stein Discrepancies — stein-discrepancy, goodness-of-fit-testing, signal-to-noise-ratio, scalable-statistics
- [[2606.26669]] SkillDisCo: Distilling and Compiling Agent Traces into Skills — llm-agents, skill-discovery, procedural-knowledge, finite-state-machine, experience-reuse
- [[2606.26686]] LeanGuard: A Fast and Light Approach for Robust Moderation — llm-safety, guardrails, chain-of-thought, efficient-inference, content-moderation
- [[2606.26705]] Algorithmic Foundations of Deep Learning — neural-network-approximation-theory, circuit-complexity, universal-approximation, o-minimal-definability ⭐
- [[2606.26839]] Ordinal Neural Collapse as a Representation Prior for Navigation — visual-navigation, neural-collapse, representation-learning, imitation-learning, diffusion-policy
- [[2606.27047]] NuclearQAv2: Structured Benchmark for Domain-Science Competence — LLM-benchmark, nuclear-engineering, domain-evaluation, quantitative-reasoning, QA-generation
- [[2606.27154]] OpenRCA 2.0: From Outcome Labels to Causal Process Supervision — root-cause-analysis, LLM-agents, causal-reasoning, benchmark, process-supervision
- [[2606.27237]] LMs as Task-Specific Knowledge Bases — llm_interpretability, mechanistic_interpretability, knowledge_representation, factual_knowledge, chain_of_thought
- [[2606.27242]] The Geometry of Updates: Fisher Alignment at Vocabulary Scale — transfer-learning, fisher-information, source-selection, LLM, training-free
- [[2606.27288]] Co-Failure Ceiling on Routing, Voting, and Mixture-of-Agents — llm-orchestration, model-routing, ensemble-methods, copula-modeling, co-failure-analysis ⭐
- [[2606.27321]] Sparsity Regularizers for More Interpretable Top-k SAEs — sparse-autoencoders, interpretability, top-k-sae, vision-foundation-models, sparsity-regularization
- [[2606.27326]] Hallucination in World Models is Predictable and Preventable — world-models, hallucination, data-coverage, reinforcement-learning, generative-models
- [[2606.27359]] When are likely answers right? Sequence Probability and Correctness — LLM, decoding, sequence-probability, calibration, self-consistency
- [[2606.27373]] Paying More Attention to Visual Tokens in Self-Evolving LMMs — self-evolving-LMM, visual-grounding, multimodal-RL, unsupervised-learning, object-hallucination
- [[2606.27376]] Ask, Solve, Generate: Self-Evolving Unified Multimodal Model — self-evolving-LMM, unified-understanding-generation, self-consistency-reward, unsupervised-post-training, multimodal


---

> 本文件为本周每日日报的汇总（rollup），完整逐篇索引由后处理步骤注入上方标记处。This file is a rollup of the daily digests; the full per-paper index is injected at the marker above by a deterministic post-step.
>
> 每日入口 / Daily overviews: [2026-06-22](../../2026-06-22/overview.md) · [2026-06-23](../../2026-06-23/overview.md) · [2026-06-24](../../2026-06-24/overview.md) · [2026-06-25](../../2026-06-25/overview.md) · [2026-06-26](../../2026-06-26/overview.md)
