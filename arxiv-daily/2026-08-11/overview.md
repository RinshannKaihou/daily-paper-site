---
title: "Daily Paper Overview — 2026-08-11"
date: 2026-08-11
tags:
  - daily-overview
  - llm-agents
  - interpretability
  - efficiency
  - quantization
  - theory
  - safety-alignment
  - vision-multimodal
  - self-evolving
papers: 50
---

# Daily Paper Overview — 2026-08-11

> 2026-08-11 共精选 50 篇论文，覆盖智能体与自演化、可解释性、效率/量化系统、理论优化、视觉多模态、安全对齐等方向。Today's 50 selected papers span agents & self-evolution, interpretability, efficiency/quantization systems, theory & optimization, vision/multimodal, and safety/alignment.

## 今日必读 / Must Read Today

### 1. [[2608.11195]] Long-Horizon AI Research for the Grothendieck Constant

**中文理由：** 用「推理智能体 + 编码智能体 + 文件式记忆」的双智能体系统（约 240 个会话、1.52 亿 token、约 5400 美元），把 Grothendieck 常数 $K_G$ 的下界从沿用四十余年的 1.6760… 推进到 1.6770…，是少见的"AI 真正推进纯数学开放问题"的案例，并系统总结了长时程人机协作的方法论。

**English reason:** A two-agent harness (reasoning model + coding agent, file-based memory, ~240 sessions, ~$5,400) improved the lower bound of the Grothendieck constant $K_G$ from the four-decade-old 1.6760… to 1.6770… — a rare case of AI genuinely advancing an open pure-math problem, with a reusable methodology for long-horizon human–AI research.

### 2. [[2608.10605]] Compute-Optimal Is Not Cluster-Optimal (MOSAIC)

**中文理由：** 指出纯 model-FLOPs 预算下 MoE 稀疏度优化退化为"越大越好"，只有换成"集群可交付 FLOPs"预算（耦合算子级 MFU/显存性能模型）才出现可部署的内点最优解；为 MoE 架构选择给出了系统感知的处方，工具开源为 ScalePlan。

**English reason:** Argues that under a pure model-FLOPs budget MoE sparsity optimization degenerates to "the sparser the better"; only by folding a systems-level MFU/memory performance model into the scaling law (cluster-deliverable FLOPs) do deployable interior optima emerge. Practical MoE scaling recipe, tooling open-sourced as ScalePlan.

### 3. [[2608.10850]] Diffract — A Spectral View of LLM Domain Adaptation

**中文理由：** 对 OLMo 2 全系列做 SVD 频谱解剖，发现继续预训练（CPT）几乎不改奇异值谱、适应由奇异向量旋转承载；据此提出"缩放 Frobenius 范数差"的头重要性判据——回滚约 15% 低重要性头即可让 7B 数学 CPT 模型的 GSM8K 提升约 4%。可解释性直接反哺训练。

**English reason:** SVD dissection of OLMo 2 shows continual pre-training barely changes singular-value spectra — adaptation is carried by singular-vector rotation. A scaled-Frobenius head-importance criterion then lets rolling back ~15% of low-importance heads *improve* a 7B math-CPT model's GSM8K by ~4%. Interpretability that directly improves training.

## 按主题分类 / Papers by Topic

### 智能体与自演化 / Agents & Self-Evolution

| Paper | Short Title | 描述 / Description |
|-------|-------------|-------------------|
| [[2608.10504]] | MEGA (Wisdom Graph) | 三层自演化基础设施，把 agent session 蒸馏成原子 PCR 三元组存入 Wisdom Graph，用 PCST 检索复用。Three-layer self-evolving infra distilling agent sessions into atomic PCR triplets in a typed Wisdom Graph retrieved via PCST. |
| [[2608.10502]] | Rollback Repair | 把错误记忆形式化，用 provenance 依赖图前向追踪受污染节点、保留可信证据、只重放相关计算。Formalizes post-failure memory recovery, tracing tainted nodes via a provenance dependency graph and replaying only answer-relevant computation. |
| [[2608.10538]] | SKILLER | 把 Skill 文本当 RL 策略，前沿大模型当 actor/critic、小模型 agent loop 当环境，全自然语言信号不更新权重。Treats a textual skill as the RL policy with a frontier model as actor/critic and a small model's loop as environment — all-natural-language signals, no weight updates. |
| [[2608.11079]] | SkillZip | 把 SKILL.md 解析成类型化契约，用最小描述长度目标做确定性压缩，无需任何 rollout，技能平均压缩 31.2%。Typed minimum-description-length skill compression needing no rollouts or rewards; averages 31.2% compression. |
| [[2608.10494]] | GeoForge | 免训练自演化遥感智能体，三级非参数记忆把任务准确率从 52% 提到 77%。Training-free self-evolving Earth-observation agent with three-level non-parametric memory, lifting accuracy 52%→77%. |
| [[2608.10792]] | ChemWorld | 把化学世界变成可编程、可精确重放的实验基础设施，公开 agent 契约与私有化学定律严格分离。Programmable, exactly replayable chemical-world infra separating the public agent contract from private chemical laws. |
| [[2608.10626]] | Dual-Loop Emotion RL | 双环框架复用 group 结果估计"策略相对交互效用"，把 rollout 预算重分配到能力边界交互状态。Dual-loop framework reusing group outcomes to reallocate rollout budget toward boundary-of-ability interaction states. |

### 编码、研究与数学智能体 / Coding, Research & Math Agents

| Paper | Short Title | 描述 / Description |
|-------|-------------|-------------------|
| [[2608.10424]] | Autoresearch Compute Recovery | 诊断 AIDE 等智能体浪费算力的失效模式，用 debug consultant + 超参回路 + Thompson 回溯提升金牌数。Diagnoses wasted-compute failure modes in AIDE; a debug consultant + control loop + Thompson backtracking lifts gold medals 22→38. |
| [[2608.10450]] | Persistent Recursive Worlds | 把持久性从 agent 转到项目本身，递归委派 + 父节点验证，仅 $44 token 成本长出复杂系统。Persistence moves from agent to project; recursive delegation with parental validation grows complex systems for ~$44. |
| [[2608.10795]] | EvoMem | 在进化式代码搜索上加跨 run 持久记忆，把成功变异蒸馏成记忆卡片注入 prompt。Adds persistent cross-run memory to evolutionary code search, distilling successful mutations into injectable memory cards. |
| [[2608.11095]] | Catastrophic Remembering | 证明 CLAUDE.md/AGENTS.md 单调膨胀源于"删除理由"遗忘，提出"灾难性记忆"概念。Shows agentic context files grow monotonically from forgetting deletion justification — names "catastrophic remembering." |
| [[2608.10740]] | Tree-of-Ideas | 把引用图展开成研究空白演化树，跨轨迹找收敛空白生成想法，逼近已发表论文质量。Unfolds citation graphs into gap-centered evolution trees, mining convergent gaps to generate near-published-quality ideas. |
| [[2608.11195]] | Grothendieck Constant | 推理+编码双智能体改进 $K_G$ 下界，长时程人机数学协作方法论。Two-agent harness improving the Grothendieck-constant lower bound, with a reusable long-horizon math-collaboration methodology. |

### GUI 与多模态智能体 / GUI & Multimodal Agents

| Paper | Short Title | 描述 / Description |
|-------|-------------|-------------------|
| [[2608.10775]] | SkillLens | 把 GUI 轨迹归一化成可检索"视觉技能卡"，冻结 VLM 执行器 Step SR 大幅提升。Normalizes GUI traces into retrievable Visual Skill Cards; frozen-VLM executor step-success rises sharply. |
| [[2608.11191]] | Test-Time GUI Grounding | 用 GRPO 训练的 MLLM Reflector 在无标注界面反思，on-policy 自蒸馏 + 对比校准。An MLLM Reflector critiques unlabeled GUIs; reflections are internalized via on-policy self-distillation with contrastive calibration. |

### 效率、量化与系统 / Efficiency, Quantization & Systems

| Paper | Short Title | 描述 / Description |
|-------|-------------|-------------------|
| [[2608.10605]] | MOSAIC MoE Scaling | 系统 MoE 缩放律：纯 FLOPs 预算退化为越大越好，集群可交付 FLOPs 才给可部署解。Systems-aware MoE scaling law: pure-FLOPs budgets degenerate; cluster-deliverable FLOPs yield deployable optima. |
| [[2608.10805]] | I/O-Aware Wavelet Conv | 指出 WTConv 是显存带宽瓶颈，三项代数等价重写大幅提速。Shows WTConv is memory-bound; three exact algebraic reformulations markedly speed it up. |
| [[2608.10823]] | MoE Proxy Models | 多视角专家剪枝构造小型代理，在 8 NPU 上复现 RL 后训练故障。Multi-view expert pruning builds small proxies to reproduce RL post-training failures on far fewer NPUs. |
| [[2608.10709]] | SQuaT | 无标签 QAT 中用学生自己的量化参数投影教师特征做蒸馏，消除不可达残差。Label-free QAT quantizes teacher features with the student's own quantization params, removing unreachable residuals. |
| [[2608.11045]] | ReRound | 免校准量化后处理，仅翻转中点附近权重，扩散模型重建决定取整方向。Calibration-free PTQ post-step flipping only midpoint-near weights, a diffusion model deciding rounding. |
| [[2608.11034]] | SCOUT | 用数据并行等价副本的多数共识定位预训练 hang/straggler/SDC 故障。Uses majority consensus among data-parallel replicas to localize latent pre-training failures. |
| [[2608.11116]] | YOCO 2.0 (Charge-CIM) | 可重构开关电容网络兼任 DAC/乘法/累加/ADC，取消比特切分，能效 2.71×。A reconfigurable switched-capacitor fabric doubles as DAC/multiply/accumulate/ADC, eliminating bit-slicing, 2.71× efficiency. |
| [[2608.11147]] | CKKS Transient Errors | 注入单比特瞬时故障，发现对称污染低位被掩蔽、单处污染全部脆弱。Single-bit fault injection: symmetric contamination masks low bits while single-spot flips are all vulnerable. |
| [[2608.11155]] | CKKS Error Sensitivity | 穷举翻转刻画 CKKS 客户端容错两种固定模式，边界由 log∆、logQ 决定。Exhaustive flips characterize two fixed CKKS client-tolerance modes bounded by log∆ and logQ. |

### 可解释性与探测 / Interpretability & Probing

| Paper | Short Title | 描述 / Description |
|-------|-------------|-------------------|
| [[2608.10537]] | SAE Feature Nonlocality | 用特征激活的位置梯度熵无标签度量"读了多长上下文"。Entropy of per-position gradient influence gives a label-free measure of how much context an SAE feature reads. |
| [[2608.10566]] | Erasure Count Not Affine-Invariant | 证明 INLP 擦除计数是过程相关而非本征，仿射变换可改变维度计数。Proves INLP erasure counts are procedure-relative, not affine-invariant concept dimensions. |
| [[2608.10985]] | PEAK (Concept Erasure) | 用 BatchTopK SAE 定位概念特征，双项损失精确擦除且保互补特征。BatchTopK SAE localizes concept features for precise erasure while preserving complementary features. |
| [[2608.10986]] | Self-Feeding Probes | token 环形元胞自动机测 Lyapunov 指数，区分"构造"与"模型"两类量。A token ring-CA measures Lyapunov exponents, separating construction-driven from model-driven signals. |
| [[2608.11197]] | SAE Set-Level Instability | 把 SAE 活跃 latent 集合当分析单元，发现真实 LLM 上既不稳定也不更贴近人类类别。Treating SAE active-latent sets as units reveals they are unstable and no closer to human categories than dense streams. |
| [[2608.10850]] | Diffract (CPT Spectral) | CPT 不改奇异值谱、由奇异向量旋转承载；头重要性判据可回滚提升精度。CPT leaves singular-value spectra invariant; a head-importance criterion lets selective rollback improve accuracy. |

### 视觉与多模态理解 / Vision & Multimodal Understanding

| Paper | Short Title | 描述 / Description |
|-------|-------------|-------------------|
| [[2608.10758]] | Causal Tracing VLM Encoders | 把 activation patching 搬到 VLM 视觉编码器，分析因果贡献与 IoU 相关性。Adapts causal tracing to VLM vision encoders, correlating causal contribution with bounding-box IoU. |
| [[2608.10835]] | UniProbe (VLM Hallucination) | ~16M 探针把冻结 LVLM 计算轨迹建成注意力图，逐 token 幻觉定位。A ~16M probe reads a frozen LVLM's trace as an attention graph for token-level hallucination localization. |
| [[2608.11024]] | Attribute Hallucination in VLM | 真图 vs 空白图双前向分解视觉 logit 差，视觉信号是属性幻觉主因。Real-vs-blank dual-forward decomposition shows visual logit margin drives attribute hallucination. |

### 安全、对齐与可信 AI / Safety, Alignment & Trustworthy AI

| Paper | Short Title | 描述 / Description |
|-------|-------------|-------------------|
| [[2608.11025]] | Emergent Misalignment | SAE 模型差分定位 persona 特征，正向 steering 推高失准、反向 steering 修复。SAE model-diffing locates persona features; forward steering induces misalignment, reverse steering repairs it. |
| [[2608.11146]] | Cross-Lingual Safety | 低资源语言上英语拒绝信号几乎丢失，构建文化本地化 LoDNA 基准。English refusal signals largely vanish in low-resource languages; introduces a culturally-localized LoDNA benchmark. |
| [[2608.11171]] | TrustNLP Survey | 多方标注 TrustNLP 六届 144 篇论文，真实性与可控性维度逐年上升。Multi-annotator meta-analysis of 144 TrustNLP papers; truthfulness and control dimensions rise over six years. |
| [[2608.10893]] | Certify or Refuse | 证明覆盖率下限把选择性风险控制劈成风险轴与下限轴两条资源轴。Proves a coverage floor splits selective risk control into two irreducible resource axes (risk vs. floor). |

### 理论、优化与学习 / Theory, Optimization & Learning

| Paper | Short Title | 描述 / Description |
|-------|-------------|-------------------|
| [[2608.10374]] | Fisher8 | 只在输出层乘精确逆 Fisher 矩阵稳定异方差回归，零数据相关超参。Multiplies the exact inverse Fisher only on the output layer to stabilize heteroscedastic regression, zero data-dependent hyperparameters. |
| [[2608.10394]] | Cross-Validated Distances | 证明交叉验证欧氏距离等价类间减类内，提出广义交叉验证与免正则相关距离。Shows CV Euclidean distance equals between-minus-within; proposes generalized CV and regularization-free correlation distance. |
| [[2608.10599]] | β-VAE Effective Theories | 把 β-VAE 的 KL 权重当 Wilsonian 截断，扫描温度揭示坍缩阈值排序。Treats the β-VAE KL price as a Wilsonian cutoff; a temperature scan reveals collapse-threshold ordering. |
| [[2608.10857]] | FiGuRO | 自编码器瓶颈处插可截断 SVD，用率失真规则在训练中双向调秩估本征维度。Truncated-SVD bottleneck layers with a rate-distortion rank schedule jointly estimate shared/private intrinsic dimensions. |
| [[2608.10869]] | Multiclass PAC Learning | 给出多类 PAC 学习任意 oracle 风险下的最优超额风险刻画，差对数因子。Optimal (up to logs) excess-risk rate for multiclass PAC learning at arbitrary oracle risk. |
| [[2608.11181]] | Probabilistic Claim Consistency | 形式化概率断言自洽问题，证明显式断言近似一致性属 NP、一般情形 NP-难。Formalizes Model-Consistency of probabilistic claims; approximate consistency is in NP, the general case NP-hard. |
| [[2608.11020]] | PINN Derivative Computation | 把 PINN 导数从 AD 换成周期性重标定的有限差分，精度与 AD 不可区分。Replaces AD derivatives in PINNs with periodically recalibrated finite differences matching AD accuracy. |

### LLM 行为、控制与优化 / LLM Behavior, Control & Optimization

| Paper | Short Title | 描述 / Description |
|-------|-------------|-------------------|
| [[2608.10471]] | RLMOpt | 把提示优化的外层搜索交给递归语言模型智能体自主决定，四基准全胜。A recursive-language-model agent controls the prompt-optimization outer loop; wins all four benchmarks. |
| [[2608.10694]] | Cost-Aware Cross-Tier | 用最便宜模型跑 fitness 评估、强模型跑变异，再零样本部署到更强层级。Cheapest model runs fitness, strong model mutates, then zero-shot deploy to a stronger tier at lower cost. |
| [[2608.10703]] | Behavioral Mode Axes | 用情境化行为探针取代人格问卷，从思维链理由提取行为控制方向。Situated behavioral probes replace personality questionnaires; control directions extracted from CoC reasoning. |
| [[2608.10729]] | Optimal Stopping Self-Refine | 把自精炼形式化为最优停止问题，证明最优策略退化为单一阈值。Casts self-refinement as optimal stopping; the optimal policy collapses to a single stage-invariant threshold. |
| [[2608.11138]] | ASMI (Attention Fragility) | 随机掩蔽注意力头 + BALD 互信息做免训练 token 级不确定性估计。Random attention-head masking + BALD mutual information for training-free token-level uncertainty. |
| [[2608.11027]] | LLM Behavioral Evolution | 同一 prompt 库下用三种嵌入距离画 32 个 LLM 的行为地图，家族自成簇。Three embedding distances draw a behavioral map of 32 LLMs; model families form natural clusters. |

## All Papers

| # | Paper | Short Title | Topic |
|---|-------|-------------|-------|
| 1 | [[2608.10374]] | Fisher8 | Theory/Optimization |
| 2 | [[2608.10394]] | Cross-Validated Distances | Theory/Optimization |
| 3 | [[2608.10424]] | Autoresearch Compute Recovery | Agents/Applications |
| 4 | [[2608.10450]] | Persistent Recursive Worlds | Agents/Applications |
| 5 | [[2608.10471]] | RLMOpt | LLM/Optimization |
| 6 | [[2608.10494]] | GeoForge | Agents/Self-Evolution |
| 7 | [[2608.10502]] | Rollback Repair | Agents/Self-Evolution |
| 8 | [[2608.10504]] | MEGA (Wisdom Graph) | Agents/Self-Evolution |
| 9 | [[2608.10537]] | SAE Feature Nonlocality | Interpretability |
| 10 | [[2608.10538]] | SKILLER | Agents/Self-Evolution |
| 11 | [[2608.10566]] | Erasure Count Not Affine-Invariant | Interpretability |
| 12 | [[2608.10599]] | β-VAE Effective Theories | Theory/Optimization |
| 13 | [[2608.10605]] | MOSAIC MoE Scaling | Efficiency/Training |
| 14 | [[2608.10626]] | Dual-Loop Emotion RL | Agents/Self-Evolution |
| 15 | [[2608.10694]] | Cost-Aware Cross-Tier | LLM/Optimization |
| 16 | [[2608.10703]] | Behavioral Mode Axes | LLM/Control |
| 17 | [[2608.10709]] | SQuaT | Efficiency/Quantization |
| 18 | [[2608.10729]] | Optimal Stopping Self-Refine | LLM/Reasoning |
| 19 | [[2608.10740]] | Tree-of-Ideas | Agents/Applications |
| 20 | [[2608.10758]] | Causal Tracing VLM Encoders | Vision/Interpretability |
| 21 | [[2608.10775]] | SkillLens | Agents/GUI |
| 22 | [[2608.10792]] | ChemWorld | Agents/Environments |
| 23 | [[2608.10795]] | EvoMem | Agents/Coding |
| 24 | [[2608.10805]] | I/O-Aware Wavelet Conv | Efficiency/Systems |
| 25 | [[2608.10823]] | MoE Proxy Models | Efficiency/MoE |
| 26 | [[2608.10835]] | UniProbe (VLM Hallucination) | Vision/Multimodal |
| 27 | [[2608.10850]] | Diffract (CPT Spectral) | Interpretability/Training |
| 28 | [[2608.10857]] | FiGuRO | Theory/Intrinsic-Dim |
| 29 | [[2608.10869]] | Multiclass PAC Learning | Theory/Learning |
| 30 | [[2608.10893]] | Certify or Refuse | Theory/Safety |
| 31 | [[2608.10985]] | PEAK (Concept Erasure) | Interpretability/Safety |
| 32 | [[2608.10986]] | Self-Feeding Probes | Interpretability/Theory |
| 33 | [[2608.11020]] | PINN Derivative Computation | Theory/Methods |
| 34 | [[2608.11024]] | Attribute Hallucination VLM | Vision/Multimodal |
| 35 | [[2608.11025]] | Emergent Misalignment | Safety/Alignment |
| 36 | [[2608.11027]] | LLM Behavioral Evolution | Evaluation/Benchmarks |
| 37 | [[2608.11034]] | SCOUT | Efficiency/Training |
| 38 | [[2608.11045]] | ReRound | Efficiency/Quantization |
| 39 | [[2608.11079]] | SkillZip | Agents/Self-Evolution |
| 40 | [[2608.11095]] | Catastrophic Remembering | Agents/Coding |
| 41 | [[2608.11116]] | YOCO 2.0 (Charge-CIM) | Efficiency/Hardware |
| 42 | [[2608.11138]] | ASMI (Attention Fragility) | LLM/Uncertainty |
| 43 | [[2608.11146]] | Cross-Lingual Safety | Safety/Alignment |
| 44 | [[2608.11147]] | CKKS Transient Errors | Systems/Security |
| 45 | [[2608.11155]] | CKKS Error Sensitivity | Systems/Security |
| 46 | [[2608.11171]] | TrustNLP Survey | Safety/Trustworthy |
| 47 | [[2608.11181]] | Probabilistic Claim Consistency | Theory |
| 48 | [[2608.11191]] | Test-Time GUI Grounding | Agents/GUI |
| 49 | [[2608.11195]] | Grothendieck Constant | Agents/AI-for-Math |
| 50 | [[2608.11197]] | SAE Set-Level Instability | Interpretability |

---

**Count verification:** Overview lists 50 papers; actual `.md` files in the directory (excluding `overview.md`) = 50. Counts match.
