---
title: "Daily Arxiv Overview — 2026-06-29"
date: 2026-06-29
tags:
  - arxiv-daily
  - llm
  - agents
  - interpretability
  - training-dynamics
  - scaling-laws
  - reinforcement-learning
papers: 50
---

# 每日论文总览 / Daily Arxiv Overview — 2026-06-29

> 本日共收录 **50** 篇论文，涵盖训练动力学/优化理论、缩放律与数据策略、推理加速与服务系统、自改进/强化学习/对齐、LLM 智能体、机制可解释性、评测基准、视觉语言模型、验证与数值计算等方向。
>
> This issue collects **50** papers spanning training dynamics & optimization theory, scaling laws & data strategy, inference & serving systems, self-improvement / RL / alignment, LLM agents, mechanistic interpretability, evaluation benchmarks, vision-language models, and verification & numerics.

---

## 今日必读 / Must Read Today

### 1. [[2606.29858]] — Token Learning Spectrum（Token 学习谱）

**为什么必读 / Why you must read it：**

- **中文：** 将宏观缩放律分解为"逐 token 的 sigmoid 学习事件"，首次给出 token 级可预测的学习进度模型。基于 **1178 A100 GPU·天** 的工业规模实验验证，在 Llama/Diffusion 等模型上实现 **11% 验证损失加速**，并公开代码——是数据筛选与训练规划的直接可用工具。
- **English:** Decomposes macroscopic scaling laws into per-token sigmoid "learning events," yielding the first token-level model of learning progress. Validated at industrial scale (**1178 A100 GPU-days**), it delivers an **11% validation-loss speedup** across Llama/Diffusion models with public code — directly actionable for data curation and training planning.

### 2. [[2606.30616]] — Agents-A1（35B MoE 智能体匹敌 1T）

**为什么必读 / Why you must read it：**

- **中文：** 上海 AI Lab 提出"扩展视野而非参数"的智能体扩展范式：以可部署的 35B MoE 模型，通过知识-动作图（KAG）基础设施与带显著词表对齐的多教师领域路由式蒸馏，在多个长程智能体基准上达到或超过 Kimi-K2.6、DeepSeek-V4-pro 等 **1T 参数级**模型，为低成本部署长程智能体提供清晰范式。
- **English:** Shanghai AI Lab's "scale the horizon, not the parameters" paradigm: a deployable 35B MoE agent that, via a knowledge-action graph (KAG) infrastructure and multi-teacher domain-routed distillation with salient vocabulary alignment, matches or beats **1T-parameter** models (Kimi-K2.6, DeepSeek-V4-pro) on several long-horizon agent benchmarks — a clear recipe for cost-effective long-horizon agents.

### 3. [[2606.30345]] — DRIFT（难度路由自蒸馏 + 节奏门控）

**为什么必读 / Why you must read it：**

- **中文：** 在问题级（难度路由）与 token 级（节奏门控）联合调度自蒸馏与强化学习信号，无需外部专家监督即可稳定自演化。在五个科学推理/工具使用基准上平均 **79.5%**，全面超越 GRPO/SDPO **7.5–9.5 个百分点**，为细粒度信用分配与课程学习提供可直接借鉴的机制设计。
- **English:** Jointly routes self-distillation vs. RL signals at the problem level (difficulty routing) and token level (rhythm gating), enabling stable self-evolution without external expert supervision. It reaches **79.5%** average across five science-reasoning / tool-use benchmarks, beating GRPO/SDPO by **7.5–9.5 points** — a directly reusable mechanism design for fine-grained credit assignment and curriculum learning.

---

## 按主题分类 / Papers by Topic

### A. 训练动力学与优化理论 / Training Dynamics & Optimization Theory

| 论文 / Paper | 一句话总结 / One-line Summary |
|---|---|
| [[2606.29679]] Observable Matrix Dynamics | 用可观测矩阵动力学（OMD）框架把训练刻画为算子演化，可在测试损失下降前约 3000 步检测到 grokking / Detects grokking ~3000 steps before test-loss drop via an operator-evolution (OMD) framework. |
| [[2606.30384]] Scalar Training Dynamics | 将 ~5×10⁴ 维训练轨迹经 MDS 压缩为单标量并保留 Lyapunov 指数、去相关时间等混沌不变量 / Compresses a ~5×10⁴-D trajectory to one scalar while preserving Lyapunov exponent and decorrelation time. |
| [[2606.30388]] Grokking Scaling Laws | 用 Adam 联合状态 SDE 极限推导 grokking 的"球壳—内核"拓扑与关于 η、b、λ 的闭式标度律 / Derives closed-form grokking scaling laws (shell–core topology) for η, b, λ via Adam's joint-state SDE limit. |
| [[2606.30455]] CWGD | 提出 Hessian 逆平方根加权的梯度多样性噪声度量，在强凸二次下证明可将余弦退火次优地板降低 1/(1+α) / Curvature-weighted gradient diversity reduces the asymptotic suboptimality floor by 1/(1+α) on convex quadratics. |
| [[2606.30509]] Muon Matrix Factorization | 理论分析 Muon 在矩阵分解上避免鞍点到鞍点慢学习、学习率不受条件数限制，构造两步对齐调度 / Shows Muon avoids slow saddle-to-saddle dynamics on matrix factorization and is condition-number-free; designs a two-step alignment schedule. |
| [[2606.30226]] Hessian Eigenvector Dynamics | 揭示 SGD 稳定/去局域化而 Adam 重组/局域化 Hessian 特征向量，给出优化器动力学的统计物理图景 / Shows SGD stabilizes/delocalizes while Adam reorganizes/localizes Hessian eigenvectors — a statistical-physics view of optimizer dynamics. |
| [[2606.30625]] Contrastive Embedding Norms | 证明被对比损失丢弃的嵌入范数是权重衰减与梯度统计的平衡产物，可作"逆特异度"的免费推理信号 / Proves discarded embedding norms encode inverse-specificity via an optimization-dynamics equilibrium, usable as a free inference signal. |
| [[2606.29791]] Inlier-Memorization Theory | 给出 inlier-memorization 效应的首个严格定理并在 ADBench 取得 0.766 AUROC / First rigorous theorem for the inlier-memorization effect; 0.766 AUROC on ADBench. |

### B. 缩放律与数据策略 / Scaling Laws & Data Strategy

| 论文 / Paper | 一句话总结 / One-line Summary |
|---|---|
| [[2606.29858]] Token Learning Spectrum | 将缩放律分解为逐 token 的 sigmoid 学习事件，工业规模验证带来 11% 验证损失加速 / Decomposes scaling laws into per-token sigmoid learning events; 11% validation-loss speedup at industrial scale. |

### C. 推理加速与服务系统 / Inference & Serving Systems

| 论文 / Paper | 一句话总结 / One-line Summary |
|---|---|
| [[2606.30265]] Speculative Decoding Theory | 为确定性投机解码建立统一的下水平集/KL 证书理论，证明单 token 的 log(2) 上界与树的 log(m+1) 上界 / Unified level-set / KL-certificate theory for deterministic speculative decoding; log(2) single-token and log(m+1) tree ceilings. |
| [[2606.30560]] TraceLab | 发布首个跨厂商大规模编码代理服务 trace，量化长上下文短输出、前缀缓存 95.7% 命中与人类思考占 92.3% 墙钟时间 / First large cross-provider coding-agent serving trace; quantifies prefix-cache 95.7% hits and human-thinking 92.3% of wall-clock. |
| [[2606.30634]] Async Pipeline Parallel | 证明异步流水线退化的关键在优化器而非延迟本身，Muon+Error Feedback 在 10B MoE 上零质量损失对齐同步训练（ICML 2026） / Shows staleness harm is optimizer-dependent; Muon + Error Feedback matches sync loss at 10B MoE (ICML 2026). |

### D. 自改进、强化学习与对齐 / Self-Improvement, RL & Alignment

| 论文 / Paper | 一句话总结 / One-line Summary |
|---|---|
| [[2606.30345]] DRIFT | 难度路由 + 节奏门控的自蒸馏/RL 联合调度，平均 79.5% 全面超越 GRPO/SDPO 7.5–9.5 点 / Difficulty routing + rhythm gating of self-distillation/RL; 79.5% avg beating GRPO/SDPO by 7.5–9.5 pts. |
| [[2606.30627]] Pessimism's Paradox | 实证发现 DPO 离线保守度越高，在线适配时奖励黑客损害越大（Spearman ρ=1.0），主张"校准的保守主义" / Higher offline DPO conservatism monotonically amplifies online reward hacking (ρ=1.0); argues for calibrated conservatism. |
| [[2606.29983]] Looped Transformers RL Stopping | 用 RL-Halting 稳定循环 Transformer 的长度泛化，避免 OOD 退化 / Stabilizes looped-transformer out-of-distribution length generalization via RL-Halting. |
| [[2606.30068]] JEPA Control-Relevance | 证明 JEPA 预测目标会丢弃外生的控制相关特征，仅用 2% 奖励标签即可恢复 / Shows JEPA predictive objectives discard exogenous control-relevant features; 2% reward labels recover them. |
| [[2606.29713]] SEVA | 形式化"优势塌缩"并提出事实归因的过程奖励 GRPO，3B 模型匹敌 GPT-4o-mini / Formalizes advantage collapse and proposes fact-attribution process-reward GRPO; 3B matches GPT-4o-mini. |
| [[2606.29871]] AI Training Manager | 用有界 LLM 监督器闭环监控训练，将 TinyStories 验证损失从 0.852 降至 0.770 / A bounded LLM supervisor in a closed training loop cuts TinyStories val loss 0.852→0.770. |

### E. LLM 智能体 / LLM Agents

| 论文 / Paper | 一句话总结 / One-line Summary |
|---|---|
| [[2606.30616]] Agents-A1 | 35B MoE 智能体通过知识-动作图与多教师蒸馏匹敌 1T 模型的长程能力 / A 35B MoE agent matches 1T-class long-horizon performance via knowledge-action graphs and multi-teacher distillation. |
| [[2606.29823]] Trellis | 将智能体搜索历史建模为受治理的数据库状态（经验图），在 KernelEvolve 上 10× 加速收敛 / Models agent search history as governed DB state (experience graphs); 10× faster convergence on KernelEvolve. |
| [[2606.29824]] Neural Procedural Memory | 训练自由的隐式激活引导，为智能体提供程序性记忆 / Training-free implicit activation steering for agent procedural memory. |
| [[2606.29916]] EVAF | 通过双门控 + LoRA 的选择性参数巩固实现智能体持续学习 / Selective parametric continual learning for agents via dual gate + LoRA consolidation. |
| [[2606.30296]] ManimAgent | 双通道情景记忆（正例参考+负例陷阱）将 Manim 代码 Pass@1 从 62.0 提升到 84.9，反思轮数减半 / Dual-channel episodic memory raises Manim Pass@1 62.0→84.9 and halves reflection rounds. |
| [[2606.30246]] Clarus | 构建网页级科学协作的多智能体基础设施与信用归因机制 / Builds web-scale scientific multi-agent collaboration infrastructure with credit attribution. |
| [[2606.29717]] Autonomous Band-Gap Research | Claude Opus 自主构建最佳无预训练晶体图网络（MAE 0.148 eV），但增益均为再发现 / Autonomous Claude Opus builds best no-pretraining crystal-graph net (MAE 0.148 eV), though gains are rediscoveries. |
| [[2606.30531]] Entity Binding Failures | 将"选对工具却操作错实体"定义为一类独立安全问题，实体感知门控将错误实体操作降至 0% / Defines "right tool, wrong entity" as a distinct safety failure; entity-aware gating cuts wrong-entity actions to 0%. |
| [[2606.30639]] WorldEvolver | 免训练自进化世界模型，通过情景/语义记忆与置信度门控的预见在部署时修正上下文 / Training-free self-evolving world model revising deployment-time context via episodic/semantic memory + confidence-gated foresight. |
| [[2606.29914]] MemDelta | 受控评测协议揭示嵌入交换可翻转 Mem0 与 RAG 的优劣结论 / Controlled protocol shows an embedding swap flips the Mem0-vs-RAG verdict. |

### F. 机制可解释性与探针 / Mechanistic Interpretability & Probes

| 论文 / Paper | 一句话总结 / One-line Summary |
|---|---|
| [[2606.29693]] IG-Lens | 基于积分梯度的 Transformer 层归因方法，实现跨层的精确加性概率归因 / Exact additive probability attribution across transformer layers via integrated gradients. |
| [[2606.29888]] SAEs Cross-Modal Heterogeneity | 揭示 VLM 中 SAE 的跨模态特征异质性，模态专属 SAE + Hungarian 对齐带来 +8.9 R@1 / Reveals SAE cross-modal feature heterogeneity in VLMs; modality-specific SAEs + Hungarian alignment yield +8.9 R@1. |
| [[2606.30609]] C²R | 基于 Minkowski 不等式的跨样本一致性正则，同时缓解 SAE 特征分裂与吸收（ICML 2026） / Cross-sample consistency regularizer from the Minkowski inequality mitigates SAE feature splitting & absorption (ICML 2026). |
| [[2606.30449]] Internal-State Probes | 严谨阴性结果：内部状态探针读的是"情境"而非"动作"，不能作为可靠的预动作监控器 / Rigorous negative result: internal-state probes read the situation, not the action — unreliable as pre-action monitors. |
| [[2606.30498]] Post-Hoc CBM Faithfulness | 证明后置 CBM 的高下游准确率不等于概念忠实，随机投影也能达到接近最优准确率 / Shows post-hoc CBM accuracy ≠ faithfulness; random projections also achieve near-optimal accuracy. |
| [[2606.29876]] Clinical Reasoning Graphs | 发现 LLM 临床推理"有能力但不一致"，缺乏跨病例的 schema 级一致性 / Finds LLM clinical reasoning is "competent but inconsistent," lacking schema-scale cross-case consistency. |

### G. 评测与基准 / Evaluation & Benchmarks

| 论文 / Paper | 一句话总结 / One-line Summary |
|---|---|
| [[2606.29719]] EPC / MPCI | 记录 GPT-4o 静默更新使评测者耦合度从 1.176 崩塌到 0.0，并反转研究结论 / Documents a silent GPT-4o update collapsing evaluator coupling 1.176→0.0 and inverting study conclusions. |
| [[2606.29784]] HERO | 用基于分数的控制变量从含噪标签聚合中实现 4–5× RMSE 降低 / Achieves 4–5× RMSE reduction vs majority vote via score-based control variates for noisy-label aggregation. |
| [[2606.29920]] RuVerBench | 首个 LLM-as-a-Judge 评分规则验证基准，评测 18 个模型共 2458 实例 / First benchmark for LLM-as-a-judge rubric verification; 18 LLMs, 2458 instances. |
| [[2606.30219]] EvalSafetyGap | 混合调研 + 10 模型审计发现能力与鲁棒性相关性仅 r=+0.232（p=0.520） / Hybrid survey + 10-model audit finds capability-robustness correlation only r=+0.232 (p=0.520). |
| [[2606.30571]] Attractor States | 多轮 LLM 辩论收敛到模型特有的潜在"吸引子"盆，跨模型影响高度不对称 / Multi-turn LLM debates converge to model-specific latent "attractor" basins; cross-model influence is strongly asymmetric. |
| [[2606.29788]] MemLeak | 多模态智能体遗忘后仍有 12% 事实可从保留图像恢复，内容感知删除可降至 2% / After forgetting, 12% of facts remain recoverable from retained images; content-aware deletion cuts this to 2%. |

### H. 视觉语言模型与多模态 / Vision-Language Models & Multimodal

| 论文 / Paper | 一句话总结 / One-line Summary |
|---|---|
| [[2606.30185]] Dynamo | 训练自由的 VLM 智能体工具学习，平均 +5.6 准确率，恢复 65–99% 到 RL 的差距 / Training-free VLM agent tool-learning; +5.6 avg accuracy, recovering 65–99% of the gap to RL. |
| [[2606.30196]] Forewarned | 基于 SONAR 的自一致性异常检测，多模态嵌入异常精确率/召回率 97%/82% / SONAR self-consistency anomaly detector on multimodal embeddings; 97%/82% precision/recall. |
| [[2606.30111]] AgentCanvas / KDLoop | 面向具身智能体的架构搜索与视觉语言导航，MapGPT +7.1~7.6pp / Architecture search for embodied VLN agents; MapGPT +7.1–7.6pp. |
| [[2606.30059]] AVLM Moderation Diagnostic | 音视频大模型内容审核失败分类法，CMC 干预将 MMAU 从 34.2 提升到 52.5 / Audio-visual LLM moderation failure taxonomy; CMC intervention raises MMAU 34.2→52.5. |

### I. 验证、形式化方法与数值计算 / Verification, Formal Methods & Numerics

| 论文 / Paper | 一句话总结 / One-line Summary |
|---|---|
| [[2606.30107]] PHACT | 神经符号的结构化认证，80 次试验中零误认证 / Structural neuro-symbolic certification; zero false certifications in 80 trials. |
| [[2606.30105]] Copula NN Verification | 用不精确概率/copula 的神经网络验证理论（纯理论，无实现） / Theory of NN verification via imprecise probability / copulas (theory-only, no implementation). |
| [[2606.30328]] autonugget | JAX 可微的病态线性系统求解包，Richardson 外推提升解与导数精度（TMLR 已发表） / Differentiable JAX solver for ill-conditioned systems via Richardson extrapolation (TMLR published). |
| [[2606.30335]] BayesEvolve | 将自主科学发现重构为显式信念状态维护，略胜纯 GP-BO / Reframes LLM discovery as explicit belief-state maintenance; marginally beats GP-BO. |

### J. 安全、公平与检索 / Safety, Fairness & Retrieval

| 论文 / Paper | 一句话总结 / One-line Summary |
|---|---|
| [[2606.30139]] Warrant | 引入 value-permission 注意力机制，27/32 任务改进 RAG / Value-permission attention for RAG; improvements on 27/32 tasks. |
| [[2606.30152]] Gender Disentanglement | 首次在上下文嵌入中解耦语法性与语义性，服务于多语言公平 / First disentanglement of grammatical vs semantic gender in contextual embeddings for multilingual fairness. |

---

## All Papers

| # | 论文 / Paper | 主题 / Topic | 一句话总结 / One-line Summary |
|---|---|---|---|
| 1 | [[2606.29679]] Observable Matrix Dynamics | 训练动力学 | OMD 框架在测试损失下降前约 3000 步检测 grokking / Detects grokking ~3000 steps before test-loss drop via OMD. |
| 2 | [[2606.29693]] IG-Lens | 可解释性 | 积分梯度的精确跨层加性概率归因 / Exact additive cross-layer probability attribution via integrated gradients. |
| 3 | [[2606.29713]] SEVA | 强化学习 | 事实归因过程奖励 GRPO，3B 匹敌 GPT-4o-mini / Fact-attribution process-reward GRPO; 3B matches GPT-4o-mini. |
| 4 | [[2606.29717]] Autonomous Band-Gap Research | LLM 智能体 | 自主构建最佳无预训练晶体图网络，增益均为再发现 / Autonomous best no-pretraining crystal-graph net; gains are rediscoveries. |
| 5 | [[2606.29719]] EPC / MPCI | 评测 | GPT-4o 静默更新使评测者耦合度崩塌并反转结论 / Silent GPT-4o update collapses evaluator coupling and inverts conclusions. |
| 6 | [[2606.29784]] HERO | 评测 | 控制变量聚合含噪标签实现 4–5× RMSE 降低 / Score-based control variates cut RMSE 4–5× for noisy labels. |
| 7 | [[2606.29788]] MemLeak | 安全/隐私 | 遗忘后 12% 事实仍可恢复，内容感知删除降至 2% / 12% facts recoverable post-forgetting; content-aware deletion → 2%. |
| 8 | [[2606.29791]] Inlier-Memorization Theory | 学习理论 | IM 效应首个严格定理，ADBench 0.766 AUROC / First rigorous IM theorem; 0.766 AUROC on ADBench. |
| 9 | [[2606.29823]] Trellis | LLM 智能体 | 经验图即受治理 DB 状态，KernelEvolve 10× 加速 / Experience graphs as governed DB state; 10× on KernelEvolve. |
| 10 | [[2606.29824]] Neural Procedural Memory | LLM 智能体 | 训练自由隐式激活引导的程序性记忆 / Training-free implicit-steering procedural memory. |
| 11 | [[2606.29858]] Token Learning Spectrum | 缩放律 | 逐 token sigmoid 学习事件，11% 加速，1178 GPU·天 / Per-token sigmoid learning events; 11% speedup, 1178 GPU-days. |
| 12 | [[2606.29871]] AI Training Manager | 监督控制 | 有界 LLM 监督器闭环训练，val loss 0.852→0.770 / Bounded LLM supervisor; val loss 0.852→0.770. |
| 13 | [[2606.29876]] Clinical Reasoning Graphs | 评测 | LLM 临床推理"有能力但不一致" / LLM clinical reasoning is competent but inconsistent. |
| 14 | [[2606.29888]] SAEs Cross-Modal Heterogeneity | 可解释性 | VLM 中 SAE 跨模态异质性，模态专属 SAE +8.9 R@1 / SAE cross-modal heterogeneity in VLMs; +8.9 R@1. |
| 15 | [[2606.29914]] MemDelta | 评测 | 受控协议下嵌入交换翻转 Mem0 vs RAG 结论 / Controlled protocol: embedding swap flips Mem0-vs-RAG. |
| 16 | [[2606.29916]] EVAF | LLM 智能体 | 双门控 + LoRA 的智能体选择性参数巩固 / Dual gate + LoRA selective consolidation for agents. |
| 17 | [[2606.29920]] RuVerBench | 评测 | 首个 LLM-as-a-Judge 规则验证基准，18 模型 / First LaaJ rubric-verification benchmark; 18 LLMs. |
| 18 | [[2606.29983]] Looped Transformers RL Stopping | 强化学习 | RL-Halting 稳定循环 Transformer 的 OOD 长度泛化 / RL-Halting stabilizes looped-transformer OOD length generalization. |
| 19 | [[2606.30059]] AVLM Moderation Diagnostic | 多模态 | 音视频审核失败分类法，CMC 使 MMAU 34.2→52.5 / AVLM moderation taxonomy; CMC raises MMAU 34.2→52.5. |
| 20 | [[2606.30068]] JEPA Control-Relevance | 强化学习 | JEPA 丢弃控制相关特征，2% 标签可恢复 / JEPA discards control-relevant features; 2% labels recover. |
| 21 | [[2606.30105]] Copula NN Verification | 形式化验证 | 不精确概率/copula 的 NN 验证理论（无实现） / Imprecise-probability/copula NN verification theory (no impl). |
| 22 | [[2606.30107]] PHACT | 形式化验证 | 神经符号结构化认证，80 试验零误认证 / Structural neuro-symbolic certification; 0 false certs/80. |
| 23 | [[2606.30111]] AgentCanvas / KDLoop | 多模态 | 具身智能体架构搜索，MapGPT +7.1~7.6pp / Embodied architecture search; MapGPT +7.1–7.6pp. |
| 24 | [[2606.30139]] Warrant | 检索增强 | value-permission 注意力，27/32 RAG 改进 / Value-permission attention; 27/32 RAG improvements. |
| 25 | [[2606.30152]] Gender Disentanglement | 公平性 | 上下文嵌入中语法/语义性别解耦的首个工作 / First grammatical-semantic gender disentanglement in contextual embeddings. |
| 26 | [[2606.30185]] Dynamo | 视觉语言 | 训练自由 VLM 智能体工具学习，+5.6 acc / Training-free VLM agent tool-learning; +5.6 acc. |
| 27 | [[2606.30196]] Forewarned | 多模态 | SONAR 自一致性异常检测，97%/82% 精确率/召回率 / SONAR anomaly detector; 97%/82% precision/recall. |
| 28 | [[2606.30219]] EvalSafetyGap | 评测 | 能力-鲁棒性相关性仅 r=+0.232（p=0.520） / Capability-robustness correlation only r=+0.232 (p=0.520). |
| 29 | [[2606.30226]] Hessian Eigenvector Dynamics | 优化理论 | SGD 去局域化、Adam 局域化 Hessian 特征向量 / SGD delocalizes, Adam localizes Hessian eigenvectors. |
| 30 | [[2606.30246]] Clarus | LLM 智能体 | 网页级科学多智能体协作基础设施与信用归因 / Web-scale scientific multi-agent infra with credit attribution. |
| 31 | [[2606.30265]] Speculative Decoding Theory | 推理加速 | 确定性投机解码的统一 KL 证书，log(2) 上界 / Unified KL certificates for deterministic speculative decoding; log(2) ceiling. |
| 32 | [[2606.30296]] ManimAgent | LLM 智能体 | 双通道情景记忆，Manim Pass@1 62.0→84.9 / Dual-channel episodic memory; Manim Pass@1 62.0→84.9. |
| 33 | [[2606.30328]] autonugget | 数值计算 | JAX 可微病态系统求解，Richardson 外推（TMLR） / Differentiable ill-conditioned solver via Richardson extrapolation (TMLR). |
| 34 | [[2606.30335]] BayesEvolve | 贝叶斯优化 | 显式信念状态的科学发现，略胜 GP-BO / Explicit belief-state discovery; marginally beats GP-BO. |
| 35 | [[2606.30345]] DRIFT | 强化学习 | 难度路由 + 节奏门控，79.5% 超越 GRPO/SDPO 7.5–9.5 点 / Difficulty routing + rhythm gating; 79.5%, beats GRPO/SDPO 7.5–9.5 pts. |
| 36 | [[2606.30384]] Scalar Training Dynamics | 训练动力学 | 高维训练轨迹压缩为单标量仍保留混沌不变量 / 5×10⁴-D trajectory → 1 scalar preserving chaotic invariants. |
| 37 | [[2606.30388]] Grokking Scaling Laws | 训练动力学 | Adam SDE 极限推导 grokking 球壳—内核标度律 / Adam SDE limit yields grokking shell–core scaling laws. |
| 38 | [[2606.30449]] Internal-State Probes | 可解释性 | 探针读"情境"非"动作"的三项阴性结果 / Three negative results: probes read situation, not action. |
| 39 | [[2606.30455]] CWGD | 优化理论 | 曲率加权梯度多样性，次优地板降 1/(1+α) / Curvature-weighted gradient diversity; floor reduced by 1/(1+α). |
| 40 | [[2606.30498]] Post-Hoc CBM Faithfulness | 可解释性 | 后置 CBM 准确率 ≠ 忠实，随机投影也接近最优 / Post-hoc CBM accuracy ≠ faithfulness; random projections near-optimal. |
| 41 | [[2606.30509]] Muon Matrix Factorization | 优化理论 | Muon 避免鞍点到鞍点慢学习，两步对齐调度 / Muon avoids saddle-to-saddle dynamics; two-step alignment schedule. |
| 42 | [[2606.30531]] Entity Binding Failures | LLM 智能体 | "选对工具错实体"独立失败，实体门控降至 0% / "Right tool, wrong entity" failure; entity gating → 0%. |
| 43 | [[2606.30560]] TraceLab | 服务系统 | 首个跨厂商编码代理服务 trace，前缀缓存 95.7% / First cross-provider coding-agent serving trace; 95.7% prefix-cache hits. |
| 44 | [[2606.30571]] Attractor States | 评测 | 多轮辩论收敛到模型特有"吸引子"盆，影响不对称 / Debates converge to model-specific attractor basins; asymmetric influence. |
| 45 | [[2606.30609]] C²R | 可解释性 | Minkowski 正则缓解 SAE 特征分裂/吸收（ICML 2026） / Minkowski regularizer mitigates SAE splitting/absorption (ICML 2026). |
| 46 | [[2606.30616]] Agents-A1 | LLM 智能体 | 35B MoE 通过知识-动作图与多教师蒸馏匹敌 1T / 35B MoE matches 1T via KAG + multi-teacher distillation. |
| 47 | [[2606.30625]] Contrastive Embedding Norms | 优化理论 | 丢弃的嵌入范数编码逆特异度，检索 +9.6~156% / Discarded norms encode inverse-specificity; +9.6–156% retrieval. |
| 48 | [[2606.30627]] Pessimism's Paradox | 对齐 | 离线越保守在线奖励黑客越严重（ρ=1.0） / More offline conservatism → more online hacking (ρ=1.0). |
| 49 | [[2606.30634]] Async Pipeline Parallel | 服务系统 | Muon+EF 在 10B MoE 零质量损失对齐同步（ICML 2026） / Muon+EF matches sync at 10B MoE (ICML 2026). |
| 50 | [[2606.30639]] WorldEvolver | LLM 智能体 | 免训练自进化世界模型，置信度门控预见 / Training-free self-evolving world model with confidence-gated foresight. |

---

## 计数核对 / Count Verification

- 实际论文 `.md` 文件数（不含 overview.md）：**50** / Actual paper `.md` files (excluding overview.md): **50**
- 上方 `papers` 字段与 All Papers 表格行数：**50** / `papers` field and All Papers table rows: **50**
- ✅ 计数一致 / Count matches.
