---
title: "Daily ArXiv Digest — 2026-06-17"
date: 2026-06-17
tags: [daily-digest, arxiv]
papers: 48
---

> 本日共筛选出 **48** 篇论文，涵盖 LLM 训练稳定性、推理评估、隐状态可解释性、计算可靠性、自演化智能体、ML 可靠性基础六大方向。
> 48 papers curated today across LLM training stability, inference evaluation, hidden-state interpretability, computation reliability, self-evolving agents, and ML mathematical foundations.

## 今日必读 / Must Read Today

### [[2606.19236]] STARE: Surprisal-Guided Token-Level Advantage Reweighting for Policy Entropy Stability

> **推荐理由：** STARE 首次从一阶梯度分析揭示了 GRPO 熵崩溃的 advantage–surprisal 四象限机制，并证明了仅需 O(T⁻¹) 量级的重加权即可阻止崩溃——在 1.5B–32B 模型上 AIME24/25 提升 4–8%。
> **Why read:** STARE provides the cleanest mechanistic diagnosis of GRPO entropy collapse via a four-quadrant advantage–surprisal structure, proving a near-criticality result (W*−1 = O(T⁻¹)) and delivering +4–8% on AIME24/25 across 1.5B–32B models.

### [[2606.18874]] Externalizing Research Synthesis and Validation in AI Scientists through a Research Harness

> **推荐理由：** Xcientist 将 AI 科学家的研究综合与验证流程外化为契约治理的可审计工件，首次形式化了「claim drift」这一隐性失败模式——在三个案例中显著优于 AI-Scientist-v2。
> **Why read:** Xcientist externalizes the AI scientist's opaque research chain into contract-governed artifacts, formalizing 'claim drift' as a first-class failure mode — outperforming AI-Scientist-v2 on three case studies.

### [[2606.18656]] The Wrong Kind of Right: Quantifying and Localizing Misfired Alignment in LLMs

> **推荐理由：** 本文提出「误触发对齐」概念：安全对齐的 LLM 在面对刻板印象相关问题时会自信地给出错误答案（而非拒绝），25 个模型全部中招，并定位到晚期层的「否决」注意力头。
> **Why read:** This paper formalizes 'misfired alignment' — aligned LLMs confidently answer wrong on stereotype-related questions. All 25 models tested misfire (up to 18.9%), and the failure is localized to late-layer 'veto' attention heads.

---

## 按主题分类 / Papers by Topic

### LLM 训练稳定性与可观测性 / LLM Training Stability & Observability

| 论文 / Paper | 中文描述 / Chinese | English |
|---|---|---|
| [[2606.18650]] BLADE: Scalable Bi-level Adaptive Data Selection for LLM Tra | BLADE 通过拉格朗日乘子将基于影响的 bi-level 数据选择目标重写为无 Hessian 的单层惩罚形式，并用动态参考模型（每 τ 步与代理模型同步）替代 RHO-1 的静态参考，配合 mem… | BLADE bridges influence-based and excess-loss data selection by reformulating the bi-level selection… |
| [[2606.18663]] RegMix-D: Dynamic Data Mixing via Proxy Training Trajectorie | RegMix-D 把 RegMix 的"端点 loss → 静态配比"扩展为"轨迹 loss → 阶段化动态配比"，用一个拟合 (step, mixture, loss) → next-loss 的 … | RegMix-D extends RegMix to dynamic data mixing by training a regression model on the *full* loss tra… |
| [[2606.18810]] Learning from Own Solutions: Self-Conditioned Credit Assignm | 提出 SC-GRPO（Self-Conditioned GRPO），对模型自身的 verified rollout 做 in-context 条件化并用产生的 per-token KL 散度作为 GR… | SC-GRPO is a drop-in modification of GRPO that uses the model's own verified rollouts as an implicit… |
| [[2606.18910]] REVES: REvision and VErification--Augmented Training for Tes | REVES 把 test-time scaling 形式化为 meta-RL 问题，证明了 sequential-revision 的单步恢复价值可以迁移到所有"使用 revision"的 TTS 算… | REVES reframes test-time scaling as a meta-RL problem, proves that improving one-step revision recov… |
| [[2606.18967]] EfficientRollout: System-Aware Self-Speculative Decoding for | EfficientRollout 把目标模型自身的 4-bit 权重量化副本作为 self-speculative decoding 草稿器，结合 roofline 模型的"系统感知切换"和基于块效率… | EfficientRollout is a system-aware self-speculative decoding framework for on-policy RL rollouts. Th… |
| [[2606.19004]] Spotlight: Synergizing Seed Exploration and Spot GPUs for Di | Spotlight 是首个将 DiT 强化学习后训练中的种子探索(选高对比度种子)与廉价 Spot GPU 协同利用的系统——通过证明探索可容忍上一代模型权重(种子相对排序在迭代间保持稳定)、把 Se… | Spotlight is a systems contribution that makes Diffusion Transformer RL post-training cheap by explo… |
| [[2606.19025]] FoMoE: Breaking the Full-Replica Barrier with a Federation o | FoMoE 通过把 MoE 专家层分片到不同数据中心（打破 DiLoCo/Photon 的"全量副本"假设）实现跨 WAN 训练，在 54M proxy 上将通信量相对高效 baseline 降低最多… | FoMoE targets geo-distributed LLM pre-training of MoE models by partitioning expert layers across we… |
| [[2606.19236]] STARE: Surprisal-Guided Token-Level Advantage Reweighting fo | STARE 通过对 GRPO 进行 token 级熵的一阶梯度分析，识别出 advantage–surprisal 四象限结构和「near-criticality」性质，进而用 batch 内 sur… | STARE is a minimally intrusive, token-level credit-rebalancing scheme that mitigates policy-entropy … |
| [[2606.19262]] Detecting Hidden ML Training With Zero-Overhead Telemetry | 利用 9 个零开销、隐私保护的 NVML 计数器，在 9 张 GPU（覆盖 Ampere–Blackwell 四代架构）上完成 1404 次、162 种工作负载的运行，经 5 轮"监控者-规避者"对抗… | The authors build and stress-test a privacy-preserving classifier that detects ML training from nine… |

### LLM 推理评估 / LLM Inference Evaluation

| 论文 / Paper | 中文描述 / Chinese | English |
|---|---|---|
| [[2606.18656]] The Wrong Kind of Right: Quantifying and Localizing Misfired | 本文提出"Misfired Alignment（误触发对齐）"概念，构建 VETO 基准（2032 对来自 BBQ 的对比样本）量化 LLM 因安全对齐而拒绝有明确上下文证据支持的合理结论的现象，并提… | This paper formalizes "misfired alignment" — the failure mode where safety-aligned LLMs override exp… |
| [[2606.18709]] LLMs Struggle to Measure What Distinguishes Students of Diff | 在 42 个 LLM × 4 个角色设定下系统评估其对阅读理解题区分度（item discrimination）的预测能力：直接数值预测最高 Spearman 仅 0.152（GPT-5.5），且多数… | This paper systematically evaluates 42 LLMs on **item discrimination** — the psychometric property m… |
| [[2606.18847]] WorldLines: Benchmarking and Modeling Long-Horizon Stateful  | 提出 WorldLines 长程具身家庭辅助基准（含 310 个 Memory QA 样本 + 21 个 Embodied Task Planning 样本）与 ObsMem 观察者视角记忆框架，通过… | WorldLines is a project-driven benchmark for long-horizon embodied household assistance built on Hab… |
| [[2606.18950]] RTSGameBench: An RTS Benchmark for Strategic Reasoning by Vi | 基于开源大场景 RTS 游戏 Beyond All Reason(BAR),提出 RTSGameBench:通过 1v1/团队/自由对战等整局评估、五个针对单点战略能力的诊断性 mini-game,以… | RTSGameBench is a holistic, diagnostic, and extensible VLM benchmark built on the open-source RTS ga… |
| [[2606.18989]] G-IdiomAlign: A Gloss-Pivoted Benchmark for Cross-Lingual Id | 提出以 Wiktionary 英文释义为语义枢轴、覆盖 9 种核心语言 18,785 对习语的 G-IdiomAlign 基准，并通过"带类型化干扰项的多选题"和"No-gloss vs With-g… | G-IdiomAlign is a gloss-pivoted, precision-first benchmark of 18,785 idiom pairs across 9 core langu… |
| [[2606.19036]] Geometric and Stochastic Analysis of Discontinuities in Spar | 对稀疏 MoE 中由 Top-k 路由产生的不连续性按"阶"分类，并用测度论切片与扩散过程给出体积渐近估计与首达概率界（首达几乎必然落在 order-1），基于此提出 ℓ∞,ϵ 局部平滑 + boun… | The paper provides a rigorous geometric and stochastic theory for the discontinuities that Top-k rou… |
| [[2606.19057]] Quantifying and Auditing LLM Evaluation via Positive--Unlabe | 将"选择性人类监督"下 LLM 评判器偏置问题重构为正-无标注 (PU) 学习任务，并提出基于部分最优传输 (POT) 的几何审计框架 PUAUDIT：在冻结的奖励模型嵌入空间中用"差分向量"刻画"胜… | PUAUDIT treats selective human supervision in LLM-as-a-Judge as a Positive–Unlabelled (PU) learning … |
| [[2606.19157]] IndicContextEval: A Benchmark for Evaluating Context Utilisa | 构建 56 小时、跨 8 种印度语言与 23 个专业领域的 IndicContextEval 真实语音基准，配合 L0–L6 七级渐进式提示框架（涵盖元数据、自然语言描述、英文字体/本地文字实体列表及… | IndicContextEval (55.93 hours, 555 speakers, 8 Indic languages, 23 professional domains, natural spe… |
| [[2606.19218]] RECOM: A Validity–Discrimination Tradeoff in Automatic Metri | 作者发布 15K 条污染无关 r/AskReddit 问答的 RECOM 评测集，对 BLEU/ROUGE/BERTScore/MoverScore/cosine/NLI/LLM-judge 七类指标… | RECOM is a 15,000-question, contamination-free r/AskReddit evaluation set (Sept 1–30, 2025, all post… |

### LLM 隐状态与可解释性 / LLM Hidden States & Interpretability

| 论文 / Paper | 中文描述 / Chinese | English |
|---|---|---|
| [[2606.18694]] Attention as Frustrated Synchronization | 提出挫败同步网络(FSN)，把自注意力的 value 通路替换为学到的复数耦合核(KS 挫败相位 + Daido 谐波 + 一步延迟)，并证明"延迟项代数等价于被数据自身下一 token 转移挫败的 … | Joshua Nunley (Indiana University Bloomington) reframes attention as frustrated synchronization. Tok… |
| [[2606.18767]] Output Vector Editing for Memorization Mitigation in Large L | 提出"输出向量编辑（OVE）"——对负责记忆的 MLP 神经元施加沿干扰 token 方向的秩一权重编辑，把它们的残差流贡献从 verbatim 记忆重定向到词汇空间中的局部合理替代，从而在 OLMo… | Output Vector Editing (OVE) is a constrained-optimization weight edit that locates a small set of ML… |
| [[2606.18790]] Closing the Loop: PID Feedback Control for Interpretable Act | 本文在多轨音乐 Transformer (MMT) 的稀疏激活引导 (SAS) 框架中引入 PID 反馈控制，提出 Spatial PID 与 Temporal PID 两种形式：前者将控制论方法在浅… | The paper adapts PID feedback control to inference-time activation steering on the Multitrack Music … |
| [[2606.18897]] SAERec: Constructing Fine-grained Interpretable Intents Prio | SAERec 用 Top-K 稀疏自编码器从 P5 文本嵌入中解耦出大规模、语义可解释的意图集，再通过 LLM-as-judge 过滤后检索个人/公共双层意图，并用多分支注意力 + 自适应融合注入序列… | SAERec constructs a large over-complete intent dictionary from user-review text embeddings (via P5 +… |
| [[2606.19222]] Mechanism-Guided Selective Unlearning for RLVR-Induced Reaso | 提出 MAST（Mechanism-Aligned Selective Targeting），通过 "非主成分能量 × 更新幅度 × 遗忘梯度耦合" 对注意力投影张量排序，仅更新 top-96/112… | MAST diagnoses the SFT-to-RLVR increment as direction-specific and off-principal (Δlog-prob 0.45 SFT… |
| [[2606.19249]] Transformer Geometry Observatory TGO-I: Spectral Geometry Ob | 提出 TGO（Transformer Geometry Observatory）系统化分析框架，在 ViT-Small/16 训练 ImageNet-100 的 100 个 epoch 过程中追踪 9… | TGO-I is the first installment of a "Transformer Geometry Observatory" framework that instruments a … |
| [[2606.19317]] Explaining Attention with Program Synthesis | 用 Claude Sonnet 4 作为程序合成代理（每头一次 refine，JSD 排序），在 BERT-base / GPT-2 / TinyLlama-1.1B / Llama-3B 上共生成 … | The authors turn transformer attention heads into compact, human-readable Python programs. For each … |

### 计算可靠性与精度误差 / Computation Reliability & Precision Errors

| 论文 / Paper | 中文描述 / Chinese | English |
|---|---|---|
| [[2606.19119]] PuDGhost: Experimental Analysis of Computation Result Corrup | 本文在 96 颗真实 DDR4 芯片上首次系统性地揭示了 PuD（Processing-using-DRAM）操作中由非激活行数据（最高 10%）和并发计算列数据（最高 48%）引发的新型干扰现象 "… | This paper experimentally reveals "PuDGhost," a previously unstudied interference phenomenon in Proc… |

### 自演化智能体与自动化研究 / Self-Evolving Agents & Automated Research

| 论文 / Paper | 中文描述 / Chinese | English |
|---|---|---|
| [[2606.18746]] What Must Generalist Agents Remember? | 在"无域标签、仅凭轨迹推断"的潜在域 POMDP 设定下,本文证明:当两个域在共享观测瓶颈处要求不相交的近似最优动作时,任何一致近似最优的策略必须在瓶颈时刻维持可由总变差距离下界区分的记忆分布(The… | A theoretical paper that asks *what* memory must encode for generalist agents that must infer their … |
| [[2606.18747]] Generating Natural and Expressive Robot Gestures through Ite | 在 Pepper 人形机器人上以 GPT-4.1 直接生成由低层运动原语函数组成的协同手势代码，并通过 5 轮、每轮 50 人（累计 250 人、4000 条反馈）的众包用户研究同时做在线 few-s… | This paper deploys GPT-4.1 as a runtime gesture-code generator for the SoftBank Pepper humanoid, whe… |
| [[2606.18831]] Beyond Reward Engineering: A Data Recipe for Long-Context Re | 该工作从数据视角出发,把长上下文推理拆为检索、多证据合成、推理三类互补能力,据此构建 8 个数据集共 ~14K 样例的"数据配方",配合极简 outcome-based GRPO + 任务平衡采样与任… | A data-centric long-context RL recipe that decomposes long-context reasoning into **retrieval, multi… |
| [[2606.18837]] Skill-MAS: Evolving Meta-Skill for Automatic Multi-Agent Sys | Skill-MAS 把"自动多智能体系统生成"从参数更新中解耦出来，将 Meta-agent 的高层编排能力建模为一份可演化的 **Meta-Skill**（任务分解 + 智能体工程 + 工作流编排三… | Skill-MAS reformulates automatic Multi-Agent System (MAS) generation as **evolving a textual Meta-Sk… |
| [[2606.18874]] Externalizing Research Synthesis and Validation in AI Scient | Xcientist 提出一种"研究抓手(research harness)"，把 AI 科学家内部隐式的研究综合(文献综述+立意)与实验验证流程外化为有契约约束、可审计的持久化 artifact 集合… | Xcientist is a research-harness framework that turns the normally opaque chain (literature → idea → … |
| [[2606.18902]] SAGE: Stochastic Prompt Optimization via Agent-Guided Explor | 将自动提示优化重新形式化为带"昂贵评估 + 低有效维度 + 局部结构"的黑盒搜索问题，提出 SPO 框架（含 SPO-RS、SPO-GA、SAGE 三种递进策略），其中 SAGE 首次把代码执行用于统… | SPO formalizes automatic prompt optimization as noisy black-box stochastic search over a low-dimensi… |
| [[2606.18947]] Decoupling Search from Reasoning: A Vendor-Agnostic Groundin | DoorDash 团队提出 Decoupled Search Grounding (DSG) — 通过 MCP 兼容网关把搜索/检索从推理模型中解耦为可控子系统，在五个前沿模型 × SimpleQA/… | DSG is a vendor-agnostic MCP-compatible grounding gateway that externalizes retrieval policy from th… |
| [[2606.19121]] Written by AI, Managed by AI: Semantic Space Control and Ind | 在一项横跨约一个月、391 次会话的真实软件重构项目（Bang-v3）中，作者用行动研究法记录并命名了长程 LLM 协作中的 "Index Sickness"（索引病）现象——当符号系统复杂度过高时，… | A single-project action-research report (~1 month, 391 sessions, ~80K LOC refactor) documenting "Ind… |
| [[2606.19135]] A Technical Taxonomy of LLM Agent Communication Protocols | 本文采用 Nickerson 迭代分类法，对九个主流开源 LLM Agent 通信协议（MCP、A2A、LAP、agents.json、Agora、ANP、LMOS、ACP、agntcy）进行五轮系统… | This paper builds a 5-dimension technical taxonomy of LLM agent communication protocols by iterative… |

### ML 可靠性与数学基础 / ML Reliability & Mathematical Foundations

| 论文 / Paper | 中文描述 / Chinese | English |
|---|---|---|
| [[2606.18627]] PACT: Preserving Anchored Cores in Task-vectors for Model Me | PACT 通过"承重墙（LBW）"概念指出预训练权重本身就承担着关键任务知识，提出在合并前用 SVD 构建"全局正交护盾"剥离任务向量中会侵入其他任务 LBW 子空间的分量，可即插即用地提升 Task… | PACT challenges the unspoken premise of Task Arithmetic–style model merging — that the pre-trained b… |
| [[2606.18697]] Stealthy World Model Manipulation via Data Poisoning | 本文提出 SWAAP——首个针对学习型世界模型的两阶段数据投毒框架：第一阶段用一阶 BOME 双层优化（依赖本文新证的"转移梯度定理"）在模型空间搜索"有害但低偏差"的目标动力学，第二阶段以隐蔽约束的… | SWAAP is a two-stage data poisoning attack on learned world models used for planning. **Stage 1** so… |
| [[2606.18811]] Rescaling MLM-Head for Neural Sparse Retrieval | 这篇论文发现把 ModernBERT、RoBERTa、Ettin 等大 MLM-head 范数骨干用于 SPLADE 时,因 MLM 输出尺度与无归一化点积打分耦合,会出现训练不稳定甚至崩溃;只需在训… | This paper shows that under the standard SPLADE recipe, swapping BERT for stronger modern encoders (… |
| [[2606.18918]] Some Complexity Results for Robustness Verification of Binar | 本文证明二值化神经网络 (BNN) 的可满足性 (BNN-SAT) 是 NP-完全的（从 SAT 通过 NOT/OR/AND 神经组件归约），并利用"均匀遮挡下第一层前置激活对遮挡颜色 c 是仿射函数… | A short (~8-page) theoretical paper from IIT Goa studying two verification problems on Binarized Neu… |
| [[2606.18993]] Sequential Kernel-based Conditional Independence Testing via | 提出 SKCI——一种基于 testing-by-betting 与自适应优化 KCI 核统计量的序列条件独立性检验方法，借助自归一化 payoff 和 truncate-and-shift 高斯校准… | SKCI is a sequential kernel-based CI test that combines testing-by-betting with an adaptively optimi… |
| [[2606.19084]] Optimal score function estimation via derivatives constraint | 在平坦环面上证明用 Sobolev 球约束假设空间、加 $(s-1)$ 阶导数的 $L^2$ 罚项就能让 score function 的 ERM 估计器达到 minimax 速率 $n^{-(s-1… | The paper studies empirical-risk-minimization (ERM) estimators of the score function $\nabla \log f$… |
| [[2606.19105]] Smoothness-Based Derandomization of PAC-Bayes Bounds | 本文提出一种基于光滑性的 PAC-Bayes 去随机化新策略——将 Gibbs 预测器到确定性后验均值预测器的转换代价精确刻画为 "Jensen gap 类" 的泛化差距，用 Rademacher 复… | This paper develops a **smoothness-based derandomization of PAC-Bayes** generalization bounds. The k… |
| [[2606.19147]] On Local Population-Risk Certificates | 针对当前模型 θ 周围的局部候选集 D，提出一种固定掩码分解 δv = Jv⁰ + Rv^(m),∘ + Cv，将群体风险增量 P(ℓ_{θ+v} − ℓ_θ) 的证书拆为 Taylor 项、Rade… | This paper builds finite-sample *local* certificates for the population-risk increment P(ℓ_{θ+v} − ℓ… |
| [[2606.19183]] Language Models as Interfaces, Not Oracles: A Hybrid LLM–ML  | 本文提出 ClaMPAPP 混合系统，将 LLM 限定为"接口"（用工具调用从叙述式临床文本中抽取 schema 受限特征并做硬规则合理性校验），由 XGBoost 在两个德国儿科阑尾炎队列上完成最终… | ClaMPAPP decouples language understanding from clinical prediction: an LLM (Llama-3.1-8B as a rewrit… |
| [[2606.19212]] Generalised Eigenvalue Geometry of Semantic Adversarial Atta | 在"代理 + 目标"双 embedding 设置下，构造由两个 embedder 的 Jacobian 拉回得到的矩阵束 $(A,B)$，用其最大广义特征值 $\lambda^*(x)$ 度量 par… | The paper models semantic paraphrase attacks as a *two-embedder* problem: a proxy embedding defines … |
| [[2606.19264]] Structured Inference with Large Language Gibbs | 提出 Large Language Gibbs (LL-Gibbs)，把 LLM 的 next-token 条件分布定义为 Gibbs 转移算子，对结构化变量做迭代重采样；理论上证明平稳分布 $q^\… | Large Language Gibbs (LL-Gibbs) casts an LLM's next-token conditionals as the transition operator of… |
| [[2606.19270]] Beyond Algorithms: Conceptual Innovation in Medical Imaging  | 本文是一篇 IEEE 风格 Perspective,在医学影像 AI 中正式区分"算法创新"(在固定问题定义下优化实现)与"概念创新"(重新定义任务、评价标准与临床意义),诊断当前社区过度奖励算法新颖… | A Perspective in medical imaging AI that draws a sharp, operational distinction between **algorithmi… |
| [[2606.19325]] Reference-Driven Multi-Speaker Audio Scene Generation from I | ScenA 把多说话人对话生成重新建模为通用文本-音频场景合成任务：在 LTX-2.3 音频流匹配基础模型上，把多条参考语音 latent 与目标 token 拼接并用身份感知位置编码区分，以一段自由… | ScenA removes the structured supervision (per-turn tags, multi-stream transcripts, speaker embedding… |

---

## All Papers

| # | Link | Title | Brief |
|---|---|---|---|
| 1 | [[2606.18627]] | PACT: Preserving Anchored Cores in Task-vectors for Model Merging | PACT challenges the unspoken premise of Task Arithmetic–style model merging — th… |
| 2 | [[2606.18650]] | BLADE: Scalable Bi-level Adaptive Data Selection for LLM Training | BLADE bridges influence-based and excess-loss data selection by reformulating th… |
| 3 | [[2606.18656]] | The Wrong Kind of Right: Quantifying and Localizing Misfired Alignment | This paper formalizes "misfired alignment" — the failure mode where safety-align… |
| 4 | [[2606.18663]] | RegMix-D: Dynamic Data Mixing via Proxy Training Trajectories | RegMix-D extends RegMix to dynamic data mixing by training a regression model on… |
| 5 | [[2606.18694]] | Attention as Frustrated Synchronization | Joshua Nunley (Indiana University Bloomington) reframes attention as frustrated … |
| 6 | [[2606.18697]] | Stealthy World Model Manipulation via Data Poisoning | SWAAP is a two-stage data poisoning attack on learned world models used for plan… |
| 7 | [[2606.18709]] | LLMs Struggle to Measure What Distinguishes Students of Different Prof | This paper systematically evaluates 42 LLMs on **item discrimination** — the psy… |
| 8 | [[2606.18746]] | What Must Generalist Agents Remember? | A theoretical paper that asks *what* memory must encode for generalist agents th… |
| 9 | [[2606.18747]] | Generating Natural and Expressive Robot Gestures through Iterative Rei | This paper deploys GPT-4.1 as a runtime gesture-code generator for the SoftBank … |
| 10 | [[2606.18767]] | Output Vector Editing for Memorization Mitigation in Large Language Mo | Output Vector Editing (OVE) is a constrained-optimization weight edit that locat… |
| 11 | [[2606.18790]] | Closing the Loop: PID Feedback Control for Interpretable Activation St | The paper adapts PID feedback control to inference-time activation steering on t… |
| 12 | [[2606.18810]] | Learning from Own Solutions: Self-Conditioned Credit Assignment for Re | SC-GRPO is a drop-in modification of GRPO that uses the model's own verified rol… |
| 13 | [[2606.18811]] | Rescaling MLM-Head for Neural Sparse Retrieval | This paper shows that under the standard SPLADE recipe, swapping BERT for strong… |
| 14 | [[2606.18831]] | Beyond Reward Engineering: A Data Recipe for Long-Context Reinforcemen | A data-centric long-context RL recipe that decomposes long-context reasoning int… |
| 15 | [[2606.18837]] | Skill-MAS: Evolving Meta-Skill for Automatic Multi-Agent Systems | Skill-MAS reformulates automatic Multi-Agent System (MAS) generation as **evolvi… |
| 16 | [[2606.18847]] | WorldLines: Benchmarking and Modeling Long-Horizon Stateful Embodied A | WorldLines is a project-driven benchmark for long-horizon embodied household ass… |
| 17 | [[2606.18874]] | Externalizing Research Synthesis and Validation in AI Scientists throu | Xcientist is a research-harness framework that turns the normally opaque chain (… |
| 18 | [[2606.18897]] | SAERec: Constructing Fine-grained Interpretable Intents Priors via Spa | SAERec constructs a large over-complete intent dictionary from user-review text … |
| 19 | [[2606.18902]] | SAGE: Stochastic Prompt Optimization via Agent-Guided Exploration | SPO formalizes automatic prompt optimization as noisy black-box stochastic searc… |
| 20 | [[2606.18910]] | REVES: REvision and VErification--Augmented Training for Test-Time Sca | REVES reframes test-time scaling as a meta-RL problem, proves that improving one… |
| 21 | [[2606.18918]] | Some Complexity Results for Robustness Verification of Binarized Neura | A short (~8-page) theoretical paper from IIT Goa studying two verification probl… |
| 22 | [[2606.18947]] | Decoupling Search from Reasoning: A Vendor-Agnostic Grounding Architec | DSG is a vendor-agnostic MCP-compatible grounding gateway that externalizes retr… |
| 23 | [[2606.18950]] | RTSGameBench: An RTS Benchmark for Strategic Reasoning by Vision-Langu | RTSGameBench is a holistic, diagnostic, and extensible VLM benchmark built on th… |
| 24 | [[2606.18967]] | EfficientRollout: System-Aware Self-Speculative Decoding for RL Rollou | EfficientRollout is a system-aware self-speculative decoding framework for on-po… |
| 25 | [[2606.18989]] | G-IdiomAlign: A Gloss-Pivoted Benchmark for Cross-Lingual Idiom Alignm | G-IdiomAlign is a gloss-pivoted, precision-first benchmark of 18,785 idiom pairs… |
| 26 | [[2606.18993]] | Sequential Kernel-based Conditional Independence Testing via Adaptive  | SKCI is a sequential kernel-based CI test that combines testing-by-betting with … |
| 27 | [[2606.19004]] | Spotlight: Synergizing Seed Exploration and Spot GPUs for DiT RL Post- | Spotlight is a systems contribution that makes Diffusion Transformer RL post-tra… |
| 28 | [[2606.19025]] | FoMoE: Breaking the Full-Replica Barrier with a Federation of MoEs | FoMoE targets geo-distributed LLM pre-training of MoE models by partitioning exp… |
| 29 | [[2606.19036]] | Geometric and Stochastic Analysis of Discontinuities in Sparse Mixture | The paper provides a rigorous geometric and stochastic theory for the discontinu… |
| 30 | [[2606.19057]] | Quantifying and Auditing LLM Evaluation via Positive--Unlabeled Learni | PUAUDIT treats selective human supervision in LLM-as-a-Judge as a Positive–Unlab… |
| 31 | [[2606.19084]] | Optimal score function estimation via derivatives constraints | The paper studies empirical-risk-minimization (ERM) estimators of the score func… |
| 32 | [[2606.19105]] | Smoothness-Based Derandomization of PAC-Bayes Bounds | This paper develops a **smoothness-based derandomization of PAC-Bayes** generali… |
| 33 | [[2606.19119]] | PuDGhost: Experimental Analysis of Computation Result Corruption in Pr | This paper experimentally reveals "PuDGhost," a previously unstudied interferenc… |
| 34 | [[2606.19121]] | Written by AI, Managed by AI: Semantic Space Control and Index Sicknes | A single-project action-research report (~1 month, 391 sessions, ~80K LOC refact… |
| 35 | [[2606.19135]] | A Technical Taxonomy of LLM Agent Communication Protocols | This paper builds a 5-dimension technical taxonomy of LLM agent communication pr… |
| 36 | [[2606.19147]] | On Local Population-Risk Certificates | This paper builds finite-sample *local* certificates for the population-risk inc… |
| 37 | [[2606.19157]] | IndicContextEval: A Benchmark for Evaluating Context Utilisation in Au | IndicContextEval (55.93 hours, 555 speakers, 8 Indic languages, 23 professional … |
| 38 | [[2606.19183]] | Language Models as Interfaces, Not Oracles: A Hybrid LLM–ML System for | ClaMPAPP decouples language understanding from clinical prediction: an LLM (Llam… |
| 39 | [[2606.19212]] | Generalised Eigenvalue Geometry of Semantic Adversarial Attacks | The paper models semantic paraphrase attacks as a *two-embedder* problem: a prox… |
| 40 | [[2606.19218]] | RECOM: A Validity–Discrimination Tradeoff in Automatic Metrics for Ope | RECOM is a 15,000-question, contamination-free r/AskReddit evaluation set (Sept … |
| 41 | [[2606.19222]] | Mechanism-Guided Selective Unlearning for RLVR-Induced Reasoning | MAST diagnoses the SFT-to-RLVR increment as direction-specific and off-principal… |
| 42 | [[2606.19236]] | STARE: Surprisal-Guided Token-Level Advantage Reweighting for Policy E | STARE is a minimally intrusive, token-level credit-rebalancing scheme that mitig… |
| 43 | [[2606.19249]] | Transformer Geometry Observatory TGO-I: Spectral Geometry Observatory | TGO-I is the first installment of a "Transformer Geometry Observatory" framework… |
| 44 | [[2606.19262]] | Detecting Hidden ML Training With Zero-Overhead Telemetry | The authors build and stress-test a privacy-preserving classifier that detects M… |
| 45 | [[2606.19264]] | Structured Inference with Large Language Gibbs | Large Language Gibbs (LL-Gibbs) casts an LLM's next-token conditionals as the tr… |
| 46 | [[2606.19270]] | Beyond Algorithms: Conceptual Innovation in Medical Imaging AI | A Perspective in medical imaging AI that draws a sharp, operational distinction … |
| 47 | [[2606.19317]] | Explaining Attention with Program Synthesis | The authors turn transformer attention heads into compact, human-readable Python… |
| 48 | [[2606.19325]] | Reference-Driven Multi-Speaker Audio Scene Generation from In-the-Wild | ScenA removes the structured supervision (per-turn tags, multi-stream transcript… |

> 📁 Markdown vault: `~/Documents/daily_paper/arxiv-daily/2026-06-17/`
> 📰 Newspaper front page: `index.html` (per-paper dashboards: `<arxiv_id>.html`)