---
title: "Arxiv Daily Overview — 2026-06-22"
date: 2026-06-22
tags:
  - arxiv-daily
  - interpretability
  - quantization
  - agents
  - optimization
  - rl
  - evaluation
  - architecture
  - 2026-06-22
papers: 50
---

## 今日必读 / Must Read Today

### [[2606.20937]] Learning through Internalization

- **推荐理由：** 从半自动机模拟视角首次形式化研究"内化"——神经网络如何将显式多步推理（CoT）压缩进权重，揭示了"宽度优于深度"的反直觉规律、素数阶任务更难内化的代数解释、以及内化伴随的根本性OOD退化权衡，并给出了稀疏奇偶校验任务的可证明内化保证——直击隐式推理的计算本质与可靠性边界。
- **Why read:** First formal study of "internalization" — how networks absorb explicit chain-of-thought into weights. On semiautomata and parity tasks, the paper finds width-over-depth beats depth for internalization, prime-order tasks are algebraically harder to compress, and internalization carries a fundamental OOD degradation tradeoff. Theorem 2 provides the first provable example of learning via internalization. Directly hits the computational nature of implicit reasoning and its reliability boundary.

### [[2606.20657]] A-Evolve-Training: Autonomous Post-Training of a 30B Model

- **推荐理由：** 首次在前沿规模（30B参数、多周H200集群训练）公开报告全自主后训练系统，在NVIDIA Nemotron-Reasoning Challenge上达到0.86分（人类最佳0.87）；更关键的是系统自主检测到内部开发指标已成为误导性代理指标并主动反转搜索策略——展示了超越优化的"发现"能力，直击自主AI研究的可行性与可靠性。
- **Why read:** First public autonomous post-training at frontier scale (30B params, multi-week H200 runs). Achieves 0.86 on Nemotron-Reasoning Challenge (human best 0.87, rank 8/~4000). The key finding is a "strategic reversal": the loop autonomously detected that its internal dev metric had become a misleading proxy and revised its search policy — evidence of discovery beyond fixed-frame optimization. Directly hits feasibility and reliability of autonomous AI research.

### [[2606.21023]] HEAL: Demystifying Numerical Instability in LLM Inference

- **推荐理由：** 通过SASS指令级剖析证明LLM推理不可复现性的根源是CUDA内核边界处高精度寄存器向低精度存储的截断误差（而非浮点算术本身），提出HEAL方法——INT16量化Q/K/V（实际比BF16更精确）+代数误差补偿GEMM——在5个模型、3种GPU上实现FP32级可复现性，性能开销比FP32低最高7.1倍——直击LLM在高可靠性场景（医疗/法律/金融）的数值可信度。
- **Why read:** SASS-level profiling reveals LLM inference non-reproducibility stems from boundary truncation at CUDA kernel edges, not arithmetic itself. HEAL uses INT16 Q/K/V quantization (actually more precise than BF16 for typical value distributions) plus algebraic error compensation for GEMM, achieving FP32-level reproducibility across 5 models and 3 GPU types at only 40-109% TPOT overhead vs. native BF16 (7.1x faster than full FP32). Directly hits numerical trustworthiness for mission-critical LLM deployment.

---

## 按主题分类 / Papers by Topic

### A. 机制可解释性与表示分析 / Mechanistic Interpretability & Representation Analysis

| 论文 / Paper | 一句话总结 / TL;DR |
| --- | --- |
| [[2606.20678]] IGSD | 配对替换与零消融干预的Sobol方差指数分解Transformer组件的"内容通道"与"基底"角色 / Paired swap-vs-zero Sobol indices decompose transformer component roles into "content channel" vs. "substrate." |
| [[2606.20743]] Ledger Residuals | 即使给Transformer专用干净解码通道，巨大激活值仍被重建，证明其为功能性必需 / Even with a protected decode-only channel, massive activations are rebuilt — functionally necessary, not removable. |
| [[2606.21249]] RoPE-Retrieval Heads | RoPE低频维度是检索头功能的因果关键轴，反驳了高theta阻止检索头的假说 / RoPE low-frequency dimensions are the causal axis for retrieval heads; higher theta does NOT prevent them. |
| [[2606.21345]] Factual Retrieval Paths | LLM事实检索是多步骤、非连续、高度冗余的分布式过程，挑战"知识局部存储于MLP"观点 / Factual retrieval in LLMs is multi-step, non-contiguous, and highly redundant, challenging the "facts in MLPs" view. |
| [[2606.23345]] Abstract Geometry | LLM成功推理时内部形成类海马体正交解耦流形，几何正则化可因果性增强推理 / LLMs form hippocampal-like orthogonal manifolds during successful inference; GeoStruct regularization causally enhances reasoning. |
| [[2606.23590]] Topology of Ill-Posed Questions | 用持久同调检测LLM隐藏状态中的病态问题拓扑特征，并做拓扑条件激活引导 / Persistent homology detects ill-posedness in hidden-state topology and enables topology-conditioned activation steering. |
| [[2606.23591]] Data-Influence vs Similarity | 量化数据影响与数据相似性的一致性以理解LLM输出归因 / Quantifies agreement between data-influence and data-similarity to understand LLM output tracing. |
| [[2606.23394]] LLM Embedding Expert Structure | RSA分析LLM嵌入空间能否恢复领域专家定义的概念结构 / RSA probes whether LLM embedding spaces recover expert-defined concept structures. |

### B. 模型架构与高效设计 / Model Architecture & Efficient Design

| 论文 / Paper | 一句话总结 / TL;DR |
| --- | --- |
| [[2606.20936]] Token-Level Hybrid vs Transformer | Token级别比较揭示混合模型优势集中在状态依赖内容词，检索/结构匹配偏向Transformer / Hybrid advantages concentrate on state-conditioned content words; retrieval/closure favors transformer. |
| [[2606.20945]] GQE | GQA组内MoE路由query头，9/16激活率匹配密集基线精度，长上下文1.7-1.8x prefill加速 / MoE routing on query heads within GQA groups: 56% activation matches baseline accuracy, 1.7-1.8x prefill speedup. |
| [[2606.23670]] Tapered LMs | MLP宽度沿深度余弦衰减（浅宽深窄），零额外代价提升四种架构的困惑度与下游性能 / Cosine-tapering MLP width (wide-early, narrow-late) improves perplexity across 4 architectures at zero extra cost. |
| [[2606.21228]] Sakana Fugu | 学习型LLM编排器通过行为级模型组合在SWE-Bench Pro等多基准超越所有单一前沿模型 / Learned LLM orchestrator composes frontier models, beating each individually on SWE-Bench Pro, GPQA-Diamond, etc. |

### C. 量化、压缩与推理效率 / Quantization, Compression & Inference Efficiency

| 论文 / Paper | 一句话总结 / TL;DR |
| --- | --- |
| [[2606.21023]] HEAL | INT16量化Q/K/V + 代数误差补偿实现FP32级推理可复现性，比FP32快最高7.1x / INT16 Q/K/V + algebraic error compensation achieves FP32-level reproducibility, up to 7.1x faster than FP32. |
| [[2606.23419]] GRINQH | 运行时激活感知动态精度分配（0-8 bit），2-4 bit有效位宽超越GPTQ/AWQ / Runtime activation-aware dynamic 0-8 bit per-channel precision beats GPTQ/AWQ at 2-4 effective bits. |
| [[2606.23406]] HyperQuant | Hadamard + 最优格量化 + Rice熵编码 + KV缓存偏差校正的统一无数据PTQ流水线 / Hadamard + optimal lattice quantization + Rice entropy coding + KV-cache bias correction in one data-free PTQ pipeline. |
| [[2606.23568]] SVD-Surgeon | 在奇异值基底上应用OBS框架修复SVD截断后的补偿误差，大幅改善高压缩率困惑度 / Applies OBS in singular-value coordinates to optimally compensate post-truncation SVD compression loss. |
| [[2606.23607]] LMC-DM | 双向学习匹配将线性模式连通性与模型合并扩展到十亿参数级预训练Transformer / Dual learned matching scales linear mode connectivity and merging to billion-parameter pretrained transformers. |

### D. 训练动力学、优化与理论 / Training Dynamics, Optimization & Theory

| 论文 / Paper | 一句话总结 / TL;DR |
| --- | --- |
| [[2606.20937]] Internalization | CoT内化偏好宽度、素数阶更难、伴随OOD退化，首个可证明内化保证 / CoT internalization favors width, primes are harder, comes with OOD degradation; first provable internalization guarantee. |
| [[2606.22326]] Adam Nonsmooth | 首次证明原始Adam（含偏差校正、无裁剪）在非光滑非凸优化中收敛 / First convergence proof for the original Adam (with bias correction, no clipping) in nonsmooth nonconvex optimization. |
| [[2606.22406]] Softmax Signal Recovery | 首次严格证明softmax注意力训练可渐近恢复噪声中的隐藏信号方向 / First rigorous proof that softmax attention trained via SGA asymptotically recovers a hidden signal direction. |
| [[2606.23235]] MFC Transformer | 将Transformer残差层视为受控ODE的显式Euler格式，导出Pontryagin一阶条件 / Casts transformer residual layers as Euler scheme for controlled ODE, derives Pontryagin first-order conditions. |
| [[2606.23364]] GD Beyond NTK | 多项式广义光滑性+解析非退化=几乎所有初始化下GD收敛到驻点邻域 / Polynomial generalized smoothness + analytic nondegeneracy yields GD convergence for almost all initializations. |
| [[2606.23637]] AngularMuown | 揭示Muown隐式执行斜流形黎曼优化，显式角步长调度实现~2x AdamW加速 / Muown implicitly does Riemannian optimization on oblique manifold; explicit angular scheduling yields ~2x over AdamW. |
| [[2606.23676]] AdamW Heavy-Tailed | 形式化提出开放问题：AdamW在重尾噪声下能否匹配符号优化器的收敛率 / Open problem: can AdamW match sign-optimizer convergence rates under heavy-tailed gradient noise? |
| [[2606.21158]] DDS | 廉价谱可观测量替代昂贵SGLD采样读取损失奇异点几何复杂度，成本降300x / Cheap spectral observables replace expensive SGLD sampling to read singular complexity, ~300x cost reduction. |
| [[2606.23357]] SOAP-Bubbles | 结构化权重不确定性用于神经网络的变分推断与贝叶斯预训练 / Structured weight uncertainty via variational inference for Bayesian neural network pretraining. |

### E. RL、对齐与后训练 / RL, Alignment & Post-Training

| 论文 / Paper | 一句话总结 / TL;DR |
| --- | --- |
| [[2606.20657]] A-Evolve-Training | 30B规模全自主后训练，系统自主检测代理指标失效并反转策略 / Autonomous post-training at 30B scale; system detects proxy metric failure and reverses strategy. |
| [[2606.22570]] ACPO | off-policy程度决定哪些token主导梯度，自适应裁剪ACPO超越DAPO/CISPO / Off-policy degree determines token gradient dominance; adaptive clip ACPO outperforms DAPO/CISPO. |
| [[2606.20814]] EM Training Dynamics | 涌现式对齐失败由域内损失主导，预训练激活可部分预测微调后的对齐脆弱性 / Emergent misalignment dominated by in-domain loss; pre-trained activations partially predict post-FT vulnerability. |
| [[2606.22942]] KD Post-Training | 系统研究后训练阶段知识蒸馏：低数据场景优于SFT，大数据时退化为SFT / KD outperforms SFT in low-data post-training regimes but degrades to SFT at large data scales. |

### F. LLM评估与可靠性 / LLM Evaluation & Reliability

| 论文 / Paper | 一句话总结 / TL;DR |
| --- | --- |
| [[2606.20820]] CELEUS | E-process构建任意时刻有效置信区间，以54-62%更少样本达标评估精度 / E-process anytime-valid CIs achieve target evaluation precision with 54-62% fewer samples. |
| [[2606.22826]] MINCE | 蒙特卡罗N值确定缩减评估基准规模（MMLU -89%），最大漂移<2.62pp / Monte Carlo N-sizing shrinks benchmarks (MMLU -89%) with max accuracy drift <2.62 pp. |
| [[2606.23403]] Litmus | 零标签代码驱动的AI流水线评估指标自动设计系统 / Zero-label code-driven automatic metric specification for evaluating AI pipelines. |
| [[2606.23404]] ReasoningLens | 将LRM思维链轨迹转化为层级图的开源可视化与诊断框架 / Open-source framework transforming LRM CoT traces into structured hierarchical graphs for diagnostic auditing. |
| [[2606.23583]] Evaluation Awareness | 评估感知由检测/行为/可控三个弱耦合轴构成，揭示"基准幻觉"现象 / Evaluation awareness decomposes into 3 weakly-coupled axes; introduces the "benchmark illusion" concept. |
| [[2606.22511]] VCM | PMI上下文聚光灯+自适应方差惩罚打破LLM解码似然陷阱，提升多样性不损推理 / PMI searchlight + adaptive variance penalty breaks the likelihood trap, improving diversity without hurting reasoning. |

### G. 知识编辑与事实管理 / Knowledge Editing & Fact Management

| 论文 / Paper | 一句话总结 / TL;DR |
| --- | --- |
| [[2606.20959]] TAS | 三阶段推理时干预恢复LLM中被压制的新知识，无需重训练或外部检索 / Three-stage test-time intervention recovers suppressed newer knowledge without retraining or retrieval. |
| [[2606.22627]] ORE | 正交投影消除批量知识编辑中的语义纠缠，跨语言编辑+4.4pp / Orthogonal projection decouples semantic entanglement in batch editing; +4.4 pp on cross-lingual Bi-ZsRE. |
| [[2606.23276]] KE Illusion of Erasure | 暴露知识编辑中"擦除假象"——编辑后知识可被对抗性恢复 / Exposes the "illusion of erasure" in knowledge editing — edited knowledge is adversarially recoverable. |

### H. 智能体、自进化与工具使用 / Agents, Self-Evolution & Tool Use

| 论文 / Paper | 一句话总结 / TL;DR |
| --- | --- |
| [[2606.20622]] Darwin Mobile Agent | 首个开源端到端RL移动GUI智能体训练系统+三阶段自进化路线图 / First open-source end-to-end RL training system for mobile GUI agents + three-stage self-evolution roadmap. |
| [[2606.20625]] AlphaMemo | 结构化搜索过程记忆用残差编辑模式+非对称否决改进alpha因子挖掘 / Structured search-process memory with residual edit motifs + asymmetric veto improves alpha mining. |
| [[2606.20839]] PRTE | 过程奖励策略演化将生物信息学工作流轨迹转化为可复用策略库 / Process-reward tactic evolution converts bioinformatics workflow rollouts into reusable tactic libraries. |
| [[2606.23525]] SelfCompact | 无训练脚手架让LM智能体自主决定何时压缩上下文，数学+18.1分/成本-70% / Training-free scaffold for self-timed context compression: +18.1 pts on math, -70% per-question cost. |
| [[2606.22798]] RAD | MoE路由模式作为无需解析答案字符串的推理rollout选择信号 / MoE routing patterns serve as answer-string-free signals for selecting among reasoning rollouts. |

### I. 安全、对齐验证与部署 / Safety, Alignment Verification & Deployment

| 论文 / Paper | 一句话总结 / TL;DR |
| --- | --- |
| [[2606.20662]] Confidence Laundering | 识别多智能体系统中"置信度洗白"失效模式，提出潜在不确定性载体方案 / Identifies "confidence laundering" in multi-agent systems; proposes latent uncertainty carriers. |
| [[2606.23175]] CAWM | AI科学家系统"正确答案、错误机制"失效模式：Geant4实验中25%回合出现 / "Correct Answer, Wrong Mechanism" failure in AI scientists: 25% of episodes in Geant4 experiments. |
| [[2606.23195]] Memory Contagion | 评估器偏差通过智能体记忆跨时间传播，不存在安全污染阈值 / Evaluator bias propagates through agent memory across time; no safe contamination threshold exists. |
| [[2606.23277]] GIF | 局部可靠的几何信息流控制防御LLM中的提示注入攻击 / Locally sound geometric information flow control defends against prompt injection in LLMs. |
| [[2606.21255]] SCOPE | 保形预测+E-process为LLM服务构建校准化的OOD拒绝门控与序贯认证 / Conformal prediction + e-process builds calibrated OOD rejection gates with sequential certification for LLM services. |

### J. 解码、生成与推理控制 / Decoding, Generation & Inference Control

| 论文 / Paper | 一句话总结 / TL;DR |
| --- | --- |
| [[2606.23546]] Energy Scaling | 受Roofline启发的Transformer微调能耗可解释缩放律 / Roofline-inspired interpretable scaling law for transformer fine-tuning energy consumption. |
| [[2606.23394]] LLM Embedding Expert | （见A组 / see group A） |

---

## All Papers

| # | 论文 / Paper | 简称 / Short Title | 一句话总结 / TL;DR |
| --- | --- | --- | --- |
| 1 | [[2606.20622]] | Darwin Mobile Agent | 首个开源RL移动GUI智能体训练系统+自进化路线图 / First open-source RL training system for mobile GUI agents. |
| 2 | [[2606.20625]] | AlphaMemo | 结构化搜索过程记忆改进LLM驱动的alpha因子挖掘 / Structured search-process memory improves LLM-driven alpha mining. |
| 3 | [[2606.20657]] | A-Evolve-Training | 30B规模全自主后训练，自主检测代理指标失效 / 30B autonomous post-training with self-detected proxy failure. |
| 4 | [[2606.20662]] | Confidence Laundering | 多智能体"置信度洗白"失效与潜在不确定性载体 / Multi-agent confidence laundering and latent uncertainty carriers. |
| 5 | [[2606.20678]] | IGSD | Sobol配对干预分解Transformer内容通道与基底角色 / Sobol paired interventions decompose content vs. substrate roles. |
| 6 | [[2606.20743]] | Ledger Residuals | 巨大激活值在保护通道中仍重建，证明功能必需性 / Massive activations rebuild in protected channel; functionally necessary. |
| 7 | [[2606.20814]] | EM Training Dynamics | 涌现式对齐失败由域内损失主导，预训练激活可预测脆弱性 / Emergent misalignment dominated by in-domain loss; activations predict vulnerability. |
| 8 | [[2606.20820]] | CELEUS | E-process任意时刻有效置信区间，评估样本减少54-62% / E-process anytime-valid CIs cut evaluation samples 54-62%. |
| 9 | [[2606.20839]] | PRTE | 过程奖励策略演化用于长程生物信息学工作流 / Process-reward tactic evolution for long-horizon bioinformatics workflows. |
| 10 | [[2606.20936]] | Token-Level Hybrid | 混合模型优势集中在状态依赖内容词，结构匹配偏向Transformer / Hybrid advantage on state-conditioned words; structural closure favors transformer. |
| 11 | [[2606.20937]] | Internalization | CoT内化偏好宽度、素数更难，首个可证明内化保证 / CoT internalization favors width, primes harder; first provable guarantee. |
| 12 | [[2606.20945]] | GQE | GQA组内query头MoE路由，56%激活匹配基线精度 / MoE on GQA query heads: 56% activation matches baseline accuracy. |
| 13 | [[2606.20959]] | TAS | 推理时三阶段干预恢复LLM被压制的新事实 / Test-time 3-stage steering recovers suppressed newer facts. |
| 14 | [[2606.21023]] | HEAL | INT16+代数补偿实现FP32级推理可复现性，比FP32快7.1x / INT16 + algebraic compensation gives FP32-level reproducibility, 7.1x faster. |
| 15 | [[2606.21158]] | DDS | 廉价谱可观测量替代SGLD采样读取奇异复杂度，成本降300x / Cheap spectral observables replace SGLD for singular complexity, ~300x cheaper. |
| 16 | [[2606.21228]] | Sakana Fugu | 学习型LLM编排器多基准超越所有单一前沿模型 / Learned orchestrator beats each frontier model individually on multiple benchmarks. |
| 17 | [[2606.21249]] | RoPE-Retrieval | RoPE低频维度是检索头因果关键轴 / Low-frequency RoPE dims are the causal axis for retrieval heads. |
| 18 | [[2606.21255]] | SCOPE | 保形预测+E-process构建LLM服务OOD拒绝门控 / Conformal + e-process OOD rejection gate for LLM services. |
| 19 | [[2606.21345]] | Factual Retrieval Paths | 事实检索是冗余分布式非连续过程 / Factual retrieval is redundant, distributed, non-contiguous. |
| 20 | [[2606.22326]] | Adam Nonsmooth | 原始Adam在非光滑非凸优化中首个收敛证明 / First convergence proof for original Adam in nonsmooth nonconvex. |
| 21 | [[2606.22406]] | Softmax Signal Recovery | Softmax注意力训练渐近恢复隐藏信号方向的严格证明 / Rigorous proof: softmax attention training recovers hidden signal direction. |
| 22 | [[2606.22511]] | VCM | PMI+方差惩罚打破解码似然陷阱，提升多样性保推理 / PMI + variance penalty breaks likelihood trap; improves diversity, preserves reasoning. |
| 23 | [[2606.22570]] | ACPO | off-policy程度决定token梯度主导权，自适应裁剪超越DAPO / Off-policy degree determines token gradient dominance; ACPO beats DAPO. |
| 24 | [[2606.22627]] | ORE | 正交投影消除批量知识编辑语义纠缠 / Orthogonal projection decouples semantic entanglement in batch editing. |
| 25 | [[2606.22798]] | RAD | MoE路由模式作为推理rollout选择的无字符串信号 / MoE routing as string-free signal for reasoning rollout selection. |
| 26 | [[2606.22826]] | MINCE | 蒙特卡罗N值确定缩减评估基准规模，MMLU -89% / Monte Carlo N-sizing shrinks benchmarks; MMLU -89%. |
| 27 | [[2606.22942]] | KD Post-Training | 后训练知识蒸馏低数据优于SFT，大数据退化 / Post-training KD beats SFT in low-data; degrades at scale. |
| 28 | [[2606.23175]] | CAWM | AI科学家"正确答案错误机制"失效模式 / "Correct Answer, Wrong Mechanism" failure in AI scientists. |
| 29 | [[2606.23195]] | Memory Contagion | 评估器偏差通过记忆跨时间传播，无安全阈值 / Evaluator bias propagates via memory; no safe threshold. |
| 30 | [[2606.23235]] | MFC Transformer | 均场控制理论分析Transformer残差层+Pontryagin条件 / Mean field control analysis of transformer layers + Pontryagin conditions. |
| 31 | [[2606.23276]] | KE Illusion of Erasure | 知识编辑"擦除假象"——编辑后知识可对抗恢复 / Knowledge editing "illusion of erasure" — edited knowledge is recoverable. |
| 32 | [[2606.23277]] | GIF | 几何信息流控制防御LLM提示注入 / Geometric information flow control defends prompt injection. |
| 33 | [[2606.23345]] | Abstract Geometry | LLM推理时形成类海马体正交几何，几何正则化增强推理 / Hippocampal-like orthogonal geometry in LLMs; GeoStruct enhances inference. |
| 34 | [[2606.23357]] | SOAP-Bubbles | 结构化权重不确定性的变分贝叶斯深度学习 / Structured weight uncertainty for variational Bayesian deep learning. |
| 35 | [[2606.23364]] | GD Beyond NTK | 超越NTK范式的通用架构GD收敛框架 / GD convergence framework for general architectures beyond NTK. |
| 36 | [[2606.23394]] | LLM Embedding Expert | RSA分析LLM嵌入空间能否恢复专家概念结构 / RSA probes LLM embedding recovery of expert concept structures. |
| 37 | [[2606.23403]] | Litmus | 零标签代码驱动AI评估指标自动设计 / Zero-label code-driven automatic metric specification for AI. |
| 38 | [[2606.23404]] | ReasoningLens | LRM思维链层级可视化与诊断审计框架 / Hierarchical CoT visualization and diagnostic auditing for LRMs. |
| 39 | [[2606.23406]] | HyperQuant | Hadamard+格量化+Rice编码的统一无数据PTQ / Hadamard + lattice + Rice coding unified data-free PTQ. |
| 40 | [[2606.23419]] | GRINQH | 激活感知动态精度分配，2-4 bit有效位宽超越GPTQ/AWQ / Activation-aware dynamic precision: 2-4 bit effective beats GPTQ/AWQ. |
| 41 | [[2606.23525]] | SelfCompact | 无训练自压缩脚手架，数学+18.1分/成本-70% / Training-free self-compaction: +18.1 pts math, -70% cost. |
| 42 | [[2606.23546]] | Energy Scaling | Roofline启发的Transformer微调能耗缩放律 / Roofline-inspired transformer fine-tuning energy scaling law. |
| 43 | [[2606.23568]] | SVD-Surgeon | OBS框架在奇异值基底修复SVD压缩损失 / OBS in singular-value basis repairs SVD compression loss. |
| 44 | [[2606.23583]] | Evaluation Awareness | 评估感知三轴分解+基准幻觉概念 / Evaluation awareness 3-axis decomposition + benchmark illusion. |
| 45 | [[2606.23590]] | Topology Ill-Posed | 持久同调检测病态问题+拓扑条件激活引导 / Persistent homology detects ill-posed questions + topology-conditioned steering. |
| 46 | [[2606.23591]] | Influence vs Similarity | 数据影响与数据相似性一致性量化 / Quantifies data-influence vs. data-similarity agreement. |
| 47 | [[2606.23607]] | LMC-DM | 双向学习匹配实现十亿参数模型合并 / Dual learned matching for billion-parameter model merging. |
| 48 | [[2606.23637]] | AngularMuown | Muown隐式黎曼优化+显式角步长调度~2x AdamW / Muown is implicit Riemannian; angular scheduling yields ~2x over AdamW. |
| 49 | [[2606.23670]] | Tapered LMs | MLP宽度沿深度余弦衰减，零代价提升性能 / Cosine-tapering MLP width improves performance at zero extra cost. |
| 50 | [[2606.23676]] | AdamW Heavy-Tailed | 开放问题：AdamW在重尾噪声下能否匹配符号优化器 / Open problem: AdamW vs. sign optimizers under heavy-tailed noise. |

---

**计数核对 / Count check:** Papers in `All Papers` table = 50. Files in `2026-06-22/2606.*.md` = 50. No discrepancy / 无出入。
