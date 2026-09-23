---
title: "Daily arXiv Overview — 2026-08-10"
date: 2026-08-10
tags:
  - arxiv-daily
  - llm
  - agents
  - self-evolving-agents
  - interpretability
  - safety
  - optimization-theory
  - mechanistic-interpretability
  - agentic-science
papers: 50
---

# 每日论文速览 / Daily arXiv Overview — 2026-08-10

> 本日共精选 **50** 篇论文。整体主线：**自进化智能体与 agent harness（8 篇）** 与 **智能体驱动科学发现（5 篇）** 是最密集的两条脉络，辅以一批扎实的**理论与优化**及**可解释性/安全**工作。
>
> Today's curated set spans **50** papers. The densest threads are **self-evolving agents & harnesses (8)** and **agentic scientific discovery (5)**, supported by strong clusters in **theory/optimization** and **interpretability/safety**.

---

## 今日必读 / Must Read Today

### 1. [[2608.08996]] Multi-agent discovery of practical quantum LDPC codes

> **推荐理由：** 一个 LLM 多智能体闭环（研究员议会 + 策展人 + worker）演化出 coset-orbit balanced-product CSS 码的可执行生成器，在多个权重类拿到领先甚至刷新纪录的有限长参数（如 w=10 的 `[[234,28,18]]` Q=38.77），并在 BP-OSD 解码下全程优于 bivariate-bicycle 基准——"智能体驱动科学发现"的硬核范例。
>
> **Why read:** An LLM multi-agent loop evolves executable generators of balanced-product CSS codes and discovers leading or record finite-length quantum LDPC codes across weight classes (e.g. `[[234,28,18]]` at w=10, Q=38.77), beating bivariate-bicycle baselines under BP-OSD — a striking hard-result demonstration of agentic AI for science.

### 2. [[2608.09096]] Evo-Bench: Can Language Models Improve Agent Harness?

> **推荐理由：** 首个把"模型能否自己改进 agent harness"隔离成受控基准的工作——冻结策略模型、种子 harness 与研究协议，只让 evolver 模型不同，从而衡量模型的"内在 harness 进化能力"。GPT-5.6-Sol/Opus-4.8 把 Overall 从 29.7 推到 ~46，逼近人工 harness 组合的 47.5，为自改进智能体定义了新的评测维度。
>
> **Why read:** The first benchmark isolating a model's intrinsic ability to *evolve* an agent harness — freezing policy model, seed harness and protocol while varying only the evolver LLM. GPT-5.6-Sol / Opus-4.8 lift Overall from 29.7 to ~46, approaching a human-engineered harness composite (47.5), defining a new evaluation axis for self-improving agents.

### 3. [[2608.09095]] Who Bridges Safety? Cross-Lingual Shared Safety Pathways

> **推荐理由：** 把多语言安全的机制分析从"孤立安全神经元"推进到"跨层共享安全通路"，因果实验证明屏蔽共享通路会让 ASR 从 32.54% 飙到 91.67%；据此只微调 <1% 参数就把 Llama-3.1-8B 的 AdvBench-x ASR 从 24.39% 压到 1.00%，机制可解释性与实用对齐兼得。
>
> **Why read:** Advances multilingual safety from isolated safety neurons to sparse *cross-layer pathways*, with causal masking raising ASR 32.54%→91.67%; fine-tuning <1% of params then cuts Llama-3.1-8B AdvBench-x ASR from 24.39% to 1.00% — mechanistic interpretability paired with practical alignment.

---

## 按主题分类 / Papers by Topic

### 推理 / 训练与蒸馏 — Reasoning / Training & Distillation

| 论文 / Paper | 简称 / Short Title | 一句话简介（中 / EN） |
|---|---|---|
| [[2608.09228]] | OP²SD | 把 OPSD 教师的特权答案换成另一道题的解答仍保持增益，证明收益来自上下文诱导的教师行为而非特权答案 / Swapping the teacher's privileged answer for another problem's solution still matches OPSD — gains come from context-induced teacher behavior, not privileged transfer. |
| [[2608.09263]] | Token Credit Three Checks | 形式化命题 + 严格配对实验证明"特权似然"不可直接当 token 级 credit（AUC≈0.505，全部配方劣于纯结果奖励）/ Formal propositions + paired experiments show privileged likelihood is not valid token-level credit (AUC≈0.505; all recipes lose to outcome-only reward). |
| [[2608.09109]] | SLIFT | 把用户反馈分解为 Fix/Spec/Null 三类原子成分，训练 Generalist+Specialist 双 LoRA，MemoryBench 上 Norm-Score +6.7 / Decomposes user feedback into Fix/Spec/Null and trains two LoRA adapters, +6.7 Norm-Score on MemoryBench. |

### 自进化智能体与框架 — Self-Evolving Agents & Harnesses

| 论文 / Paper | 简称 / Short Title | 一句话简介（中 / EN） |
|---|---|---|
| [[2608.09044]] | Tree-of-Experience (ToE) | 用与推理层级对齐的"分析视角树"为 agent 经验做可靠度归因，Game of 24 准确率 +20.4 pts 且 LLM 调用 −78.7% / A tree of analytical perspectives attributes delayed outcomes to reasoning views; +20.4 pts on Game of 24 with −78.7% LLM calls. |
| [[2608.09096]] | Evo-Bench | 首个衡量模型自改 agent harness 内在能力的受控基准 / First controlled benchmark for a model's intrinsic harness-evolving ability. |
| [[2608.09292]] | ZOForLLMAgents | 零阶优化扰动实例 LoRA、以答案困惑度为损失挖掘难题成功轨迹，GAIA 23.3%→47.5% / Zeroth-order LoRA perturbation with answer-perplexity loss recovers hard-task trajectories; GAIA 23.3%→47.5%. |
| [[2608.09380]] | OpenLoopEvolve | 把 agent 八组件执行环路抽成可演化版本资产，YC-Bench 年终资金 +88% / Externalizes the agent's 8-component loop as an evolvable versioned asset; +88% final funds on YC-Bench. |
| [[2608.09537]] | VERDI | 把世界模型优化经验降级为需目标端验证的假设，负迁移率 0.34→0.06 / Treats world-model optimization experience as target-side-verifiable hypotheses; negative transfer 0.34→0.06. |
| [[2608.09629]] | Rethinking Self-Evolving (OEO) | 拆分优化契约与元策略，让前沿模型在线自组合，14 格对比 12 胜且只用 34% 预算 / Separates optimization contract from meta-policy; GPT-5.5 composes it online — 12/14 wins at 34% of the token budget. |
| [[2608.09855]] | Auto-Research is Fuzz Testing | 立场论文：主张自动科研 agent 照搬灰盒模糊测试的"引导 vs 验证"控制回路 / Position paper: auto-research agents should adopt greybox-fuzzing guidance-vs-oracle control loops. |
| [[2608.09885]] | SHE Safety Harness | 把 agent 安全护栏拆成四构件并做归因局部编辑，Agent-SafetyBench ASR 17.1%→5.5% / Decomposes the agent safety harness into 4 artifacts with attribution-guided edits; ASR 17.1%→5.5%. |

### 智能体、工具与应用 — Agents, Tools & Operations

| 论文 / Paper | 简称 / Short Title | 一句话简介（中 / EN） |
|---|---|---|
| [[2608.09184]] | Agentic Router (SONiC) | 执行驱动的双路径持续学习智能体做 SONiC 网络运维（记忆 + LoRA 后果预测）/ Execution-grounded dual-path continual-learning agent for SONiC network operations. |
| [[2608.09248]] | Emotion2Skill | 从残差流抽取 27 维情绪向量驱动技能路由，ALFWorld 47.4% / Reads a 27-dim emotion vector from the residual stream to drive skill routing; ALFWorld 47.4%. |
| [[2608.09253]] | SkillSentry | 把 skill 文档解析成 FSM 并在运行期 hook 保证执行，成功率 62.6%→77.7% / Parses skills into a runtime-assurance FSM enforced via pre-action hooks; success 62.6%→77.7%. |
| [[2608.09316]] | MemeMind | 用离线参考答案反向构造经核验的工具轨迹做上下文优化，MemeX +22% / Constructs verified tool traces from offline answers for context optimization; MemeX +22%. |
| [[2608.09343]] | LLM Heuristic Design (AGV) | 事件级仿真轨迹驱动 LLM 改写调度策略代码，DES 得分 62.49→78.61 / Event-level sim traces drive LLM to rewrite scheduling heuristics; DES score 62.49→78.61. |
| [[2608.09254]] | QueryProof / WRB | 以"业务真值率"重定义分析 agent 评测，7B 规则智能体超过直接提示的 32B / Redefines analytics-agent eval as Business Truth Rate; a 7B rule-gated agent beats a direct-prompted 32B. |

### 智能体驱动科学发现 — Agentic Scientific Discovery

| 论文 / Paper | 简称 / Short Title | 一句话简介（中 / EN） |
|---|---|---|
| [[2608.08996]] | Multi-Agent Quantum LDPC | LLM 多智能体演化出多个权重类领先/刷新纪录的 qLDPC 码 / LLM multi-agent loop discovers leading or record finite-length quantum LDPC codes. |
| [[2608.09696]] | Model Discovery Agent | LLM 仅作结构提案器，贝叶斯机器（SMC+VoI+SBI）做机理模型发现，ForceBench 仅 8 次实验达 93% / LLM as proposer, Bayesian machinery does mechanistic discovery; 93% pass with 8 experiments on ForceBench. |
| [[2608.09874]] | ArchAgent v2 | 级联进化 + 编译期硬件预算反馈自动设计三级数据预取器，IPC +3.82% / Cascaded evolution + compile-time hardware feedback for 3-level prefetcher design; IPC +3.82%. |
| [[2608.09622]] | MCTS Reliability Qualification | 把半导体可靠性鉴定建模为约束 POMDP，MCTS+EKF 在仿真上把成品率 19.4%→54.0% / Casts semiconductor reliability qualification as a constrained POMDP; MCTS+EKF lifts yield 19.4%→54.0% in sim. |
| [[2608.09350]] | Lunar Anomaly Search | β-VAE 重建误差在 LRO 月面影像上做异常候选筛选（3× 随机基线）/ β-VAE reconstruction error screens lunar anomalies (3× random baseline). |

### 可解释性与引导 — Interpretability & Steering

| 论文 / Paper | 简称 / Short Title | 一句话简介（中 / EN） |
|---|---|---|
| [[2608.09095]] | Cross-Lingual Safety Pathways | 发现并微调跨语言共享安全通路，Llama AdvBench-x ASR 24.39%→1.00% / Identifies & fine-tunes shared cross-lingual safety pathways; Llama AdvBench-x ASR 24.39%→1.00%. |
| [[2608.09521]] | Universal Activation Bus | 每模型一对 adapter 让可解释工具（probe/SAE/NLA）跨模型复用 / One adapter pair per model lets interpretability tools transfer across LLMs. |
| [[2608.09643]] | Activation Probes (Code Security) | 线性探针零样本捕获模型输出漏掉的漏洞信号，成对胜率 61–67% / Linear probes surface code-security signals the model's output misses; 61–67% pairwise win-rate. |
| [[2608.09928]] | Multimodal Model Diffing | 对比 LM 与多模态 SAE 字典发现并控制 VLM 特征，单特征消融掉 6–31% 空间准确率 / Diffs LM vs multimodal SAE dictionaries to discover & control VLM features; −6–31% spatial acc per feature. |
| [[2608.09490]] | Task Vector Interference | 测量任务向量功能非可加性的有效边界，换模板即令对比塌缩 / Maps the validity boundaries of task-vector composition; an Alpaca template collapses the contrast. |

### 安全、对齐与可靠性 — Safety, Alignment & Reliability

| 论文 / Paper | 简称 / Short Title | 一句话简介（中 / EN） |
|---|---|---|
| [[2608.09624]] | Internal Harmfulness Anti-Rank | 内部有害分数对真实越狱成功反向排序（AUROC 0.220），属构造效度失败 / Internal harmfulness scores anti-rank successful jailbreaks (AUROC 0.220) — a construct-validity failure. |
| [[2608.09900]] | Decoding-Level Taboo | 词首 logit 屏蔽的零提示诊断式鲁棒性压力测试 / Word-initial logit masking as a zero-prompt diagnostic robustness stress test. |
| [[2608.09768]] | ReliableNet | 机会约束训练显式压低"高置信且错误"概率，6 数据集上唯一全种子认证通过 / Chance-constrained training bounds joint confident-wrong probability; only method certified on all seeds. |
| [[2608.09080]] | LLM Overconfidence (Clinical) | 临床不确定/答案缺失下 LLM 置信度与准确率脱钩，少弃答且高置信编造 / LLM confidence stays decoupled from epistemic uncertainty in clinical settings; rare abstention, high-confidence hallucination. |

### 效率、系统与训练 — Efficiency, Systems & Training

| 论文 / Paper | 简称 / Short Title | 一句话简介（中 / EN） |
|---|---|---|
| [[2608.09119]] | Motif 3 | 314B/13.2B MoE（GDLA 注意力），agentic 任务领先但科学推理明显落后 / 314B/13.2B MoE (GDLA attention); leads on agentic tasks but trails on scientific reasoning. |
| [[2608.09160]] | SwiftQK | 张量并行 QK-Norm 同步降为标量归约，端到端 TPOT 平均 −29.5% / Reduces TP QK-Norm sync to a scalar reduction; end-to-end TPOT −29.5% on average. |
| [[2608.09595]] | ICBQ | 交错跨块后训练量化，三值 DBF 下 Qwen3-8B 困惑度 5752.9→29.90 / Interleaved cross-block PTQ; ternary DBF Qwen3-8B perplexity 5752.9→29.90. |
| [[2608.09412]] | KVDiagnosis | 同源配对抽取 KV-cache 压缩失败并定位机理（63.2% 源于证据覆盖低）/ Paired diagnostics localize why KV-cache compression breaks answers (63.2% low evidence coverage). |
| [[2608.09819]] | Macaron-V1 | 冻结 744B 底座 + 四 LoRA 专家的 agent 模型族，GenUI 基准领先 / Frozen 744B base + four LoRA specialists agent-model family; leads on generative-UI bench. |

### 视觉、多模态与检索 — Vision, Multimodal & Retrieval

| 论文 / Paper | 简称 / Short Title | 一句话简介（中 / EN） |
|---|---|---|
| [[2608.08976]] | Label-Free Parkinson's Screening | 免标注语音+人脸帕金森筛查，等权融合 AUROC 0.802 / Label-free face+voice Parkinson screen; equal-weight fusion reaches AUROC 0.802. |
| [[2608.09152]] | LightAIR | 黎曼梯度修正 + 零空间投影做文本行人异常检索，PAB R@1 84.73% / Riemannian-gradient rectification + null-space projection for person anomaly search; PAB R@1 84.73%. |
| [[2608.09474]] | FaLCon | 锚+facet 检索叠加多专家不确定性门控共识，PAB mAP@10 95.41% / Anchor+facet retrieval with uncertainty-gated multi-expert consensus; PAB mAP@10 95.41%. |
| [[2608.09572]] | HMCL | 双曲空间正交投影抑制多模态连续学习遗忘，整体 BWT −3.49→−1.07 / Orthogonal projection in hyperbolic space curbs multimodal continual forgetting; overall BWT −3.49→−1.07. |

### 理论与优化 — Theory & Optimization

| 论文 / Paper | 简称 / Short Title | 一句话简介（中 / EN） |
|---|---|---|
| [[2608.09004]] | Tight Lower Bound, Bounded Noise | 证明几乎必然有界梯度噪声不改善非凸优化最坏复杂度，解决 Arjevski 等开放问题 / Proves a.s.-bounded gradient noise gives zero complexity improvement, resolving an open question. |
| [[2608.09396]] | Landau Theory of Invariant Learning | 用铁磁相变理论统一不变学习目标，给出七种正则化"表型" / Unifies invariant-learning objectives via ferromagnetic phase-transition theory into seven regularizer phenotypes. |
| [[2608.09417]] | Post-Norm Rank Collapse | 两阶段机理解释 Post-Norm 解码器为何 rank collapse（注意力放大+梯度修复失败）/ Two-stage mechanistic account of Post-Norm rank collapse (attention amplification + gradient-repair failure). |
| [[2608.09523]] | Generalized Convexity (Conjugate) | 共轭对偶推广凸性/光滑性，广义 GD 最优学习率恒为 1 / Conjugate-dual generalized convexity/smoothness; generalized GD has provably optimal LR=1. |
| [[2608.09558]] | Prompting Random Transformers | 证明随机权重 Transformer 仅靠构造 prompt 即可复现 NW 核估计器并达 minimax 率 / Random-weight Transformers emulate the Nadaraya-Watson estimator purely via prompt, hitting minimax rate. |
| [[2608.09870]] | Log-free Stability Bounds | 去掉一致稳定泛化界矩不等式中的 log n 因子，正面回答 BKZ 上界问题 / Removes the log n factor from uniform-stability moment inequalities, answering BKZ's open question. |
| [[2608.09763]] | GO-Muon | 谱几何+K-FAC 曲率的二阶 Muon，grokking 步数 8×–20× 加速 / Second-order Muon marrying spectral geometry and K-FAC curvature; 8–20× faster grokking. |
| [[2608.09030]] | Missing Data as Control | 把含缺失数据监督学习重建模为闭环自适应控制，方向感知更新显著优于掩码 SGD / Recasts missing-data learning as closed-loop adaptive control; directional update beats masked SGD. |

### 评测与基准 — Evaluation & Benchmarks

| 论文 / Paper | 简称 / Short Title | 一句话简介（中 / EN） |
|---|---|---|
| [[2608.09538]] | TCS-Bench | 首个研究级理论计算机证明生成基准，GPT 5.6 Pro 取得 68% 最高分 / First benchmark for research-level TCS theorem-proof generation; GPT 5.6 Pro tops at 68%. |
| [[2608.08975]] | AI Review Rhetoric Hacking | 沿六修辞维度双向改写稿件揭示 AI 审稿可被证据框架/新奇性左右，但非普遍"奖励黑客" / Rhetoric rewritings show AI review is swayed by evidence framing & novelty stance, but selectively, not a universal reward hack. |

---

## All Papers

| Paper | Short Title | 所属主题 / Topic |
|---|---|---|
| [[2608.08975]] | AI Review Rhetoric Hacking | 评测与基准 / Evaluation & Benchmarks |
| [[2608.08976]] | Label-Free Parkinson's Screening | 视觉、多模态与检索 / Vision, Multimodal & Retrieval |
| [[2608.08996]] | Multi-Agent Quantum LDPC Codes | 智能体驱动科学发现 / Agentic Scientific Discovery |
| [[2608.09004]] | Tight Lower Bound, Bounded Noise | 理论与优化 / Theory & Optimization |
| [[2608.09030]] | Missing Data as Control | 理论与优化 / Theory & Optimization |
| [[2608.09044]] | Tree-of-Experience (ToE) | 自进化智能体与框架 / Self-Evolving Agents & Harnesses |
| [[2608.09080]] | LLM Overconfidence (Clinical) | 安全、对齐与可靠性 / Safety, Alignment & Reliability |
| [[2608.09095]] | Cross-Lingual Safety Pathways | 可解释性与引导 / Interpretability & Steering |
| [[2608.09096]] | Evo-Bench | 自进化智能体与框架 / Self-Evolving Agents & Harnesses |
| [[2608.09109]] | SLIFT | 推理 / 训练与蒸馏 / Reasoning / Training & Distillation |
| [[2608.09119]] | Motif 3 | 效率、系统与训练 / Efficiency, Systems & Training |
| [[2608.09152]] | LightAIR | 视觉、多模态与检索 / Vision, Multimodal & Retrieval |
| [[2608.09160]] | SwiftQK | 效率、系统与训练 / Efficiency, Systems & Training |
| [[2608.09184]] | Agentic Router (SONiC) | 智能体、工具与应用 / Agents, Tools & Operations |
| [[2608.09228]] | OP²SD | 推理 / 训练与蒸馏 / Reasoning / Training & Distillation |
| [[2608.09248]] | Emotion2Skill | 智能体、工具与应用 / Agents, Tools & Operations |
| [[2608.09253]] | SkillSentry | 智能体、工具与应用 / Agents, Tools & Operations |
| [[2608.09254]] | QueryProof / WRB | 智能体、工具与应用 / Agents, Tools & Operations |
| [[2608.09263]] | Token Credit Three Checks | 推理 / 训练与蒸馏 / Reasoning / Training & Distillation |
| [[2608.09292]] | ZOForLLMAgents | 自进化智能体与框架 / Self-Evolving Agents & Harnesses |
| [[2608.09316]] | MemeMind | 智能体、工具与应用 / Agents, Tools & Operations |
| [[2608.09343]] | LLM Heuristic Design (AGV) | 智能体、工具与应用 / Agents, Tools & Operations |
| [[2608.09350]] | Lunar Anomaly Search | 智能体驱动科学发现 / Agentic Scientific Discovery |
| [[2608.09380]] | OpenLoopEvolve | 自进化智能体与框架 / Self-Evolving Agents & Harnesses |
| [[2608.09396]] | Landau Theory of Invariant Learning | 理论与优化 / Theory & Optimization |
| [[2608.09412]] | KVDiagnosis | 效率、系统与训练 / Efficiency, Systems & Training |
| [[2608.09417]] | Post-Norm Rank Collapse | 理论与优化 / Theory & Optimization |
| [[2608.09474]] | FaLCon | 视觉、多模态与检索 / Vision, Multimodal & Retrieval |
| [[2608.09490]] | Task Vector Interference | 可解释性与引导 / Interpretability & Steering |
| [[2608.09521]] | Universal Activation Bus | 可解释性与引导 / Interpretability & Steering |
| [[2608.09523]] | Generalized Convexity (Conjugate) | 理论与优化 / Theory & Optimization |
| [[2608.09537]] | VERDI | 自进化智能体与框架 / Self-Evolving Agents & Harnesses |
| [[2608.09538]] | TCS-Bench | 评测与基准 / Evaluation & Benchmarks |
| [[2608.09558]] | Prompting Random Transformers | 理论与优化 / Theory & Optimization |
| [[2608.09572]] | HMCL | 视觉、多模态与检索 / Vision, Multimodal & Retrieval |
| [[2608.09595]] | ICBQ | 效率、系统与训练 / Efficiency, Systems & Training |
| [[2608.09622]] | MCTS Reliability Qualification | 智能体驱动科学发现 / Agentic Scientific Discovery |
| [[2608.09624]] | Internal Harmfulness Anti-Rank | 安全、对齐与可靠性 / Safety, Alignment & Reliability |
| [[2608.09629]] | Rethinking Self-Evolving (OEO) | 自进化智能体与框架 / Self-Evolving Agents & Harnesses |
| [[2608.09643]] | Activation Probes (Code Security) | 可解释性与引导 / Interpretability & Steering |
| [[2608.09696]] | Model Discovery Agent | 智能体驱动科学发现 / Agentic Scientific Discovery |
| [[2608.09763]] | GO-Muon | 理论与优化 / Theory & Optimization |
| [[2608.09768]] | ReliableNet | 安全、对齐与可靠性 / Safety, Alignment & Reliability |
| [[2608.09819]] | Macaron-V1 | 效率、系统与训练 / Efficiency, Systems & Training |
| [[2608.09855]] | Auto-Research is Fuzz Testing | 自进化智能体与框架 / Self-Evolving Agents & Harnesses |
| [[2608.09870]] | Log-free Stability Bounds | 理论与优化 / Theory & Optimization |
| [[2608.09874]] | ArchAgent v2 | 智能体驱动科学发现 / Agentic Scientific Discovery |
| [[2608.09885]] | SHE Safety Harness | 自进化智能体与框架 / Self-Evolving Agents & Harnesses |
| [[2608.09900]] | Decoding-Level Taboo | 安全、对齐与可靠性 / Safety, Alignment & Reliability |
| [[2608.09928]] | Multimodal Model Diffing | 可解释性与引导 / Interpretability & Steering |

---

> **数量校验 / Count check：** 本文件索引论文数 = 50；目录中 `.md` 文件数（不含 overview.md）= 50。两者一致，无差异。
> Indexed papers in this overview = 50; `.md` files in the directory (excluding overview.md) = 50. Counts match — no discrepancy.
