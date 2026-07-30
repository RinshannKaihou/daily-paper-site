---
title: "Daily arXiv Digest — 2026-07-29"
date: 2026-07-29
tags:
  - LLM agents
  - self-evolving agents
  - automated research
  - LLM safety / alignment
  - mechanistic interpretability
  - conformal prediction
  - OOD detection
  - learning theory
  - inference efficiency / quantization
  - physics-informed ML
  - world models
  - benchmark evaluation
papers: 49
---

## 今日必读 / Must Read Today

### [[2607.27191]] Can AI Agents Conduct Open-Ended AI Research?

CRUX 团队提出"影子评估"（shadow evaluation）：把两篇尚未发表的 NeurIPS 2026 投稿的原始研究问题交给 Claude Opus 4.8（六天时间、3000 美元预算），再由论文原作者亲自打分评审。结果两篇 AI 独立复现的论文均被明确拒稿（2/6 与 1/6），AI 智能体能完成全部工程环节，却在选择研究方向、应对负面结果、及时止损与遵守指令上反复失败，用另一套模型复现实验也几乎重现了全部失败模式——这是目前最严谨的"AI 能否做开放式科研"实证证据之一。
CRUX introduces "shadow evaluations": give a frontier agent (Claude Opus 4.8, six days, $3,000 API budget) the exact research question behind an unpublished NeurIPS 2026 submission and have the paper's own authors grade the output like conference reviewers. Both AI-produced papers were unambiguously rejected (2/6 and 1/6); the agent handled all the engineering but repeatedly failed at choosing research direction, responding to negative results, stopping losses, and following instructions — failures a robustness rerun on a different model stack reproduced almost entirely.

### [[2607.26587]] One Run Is Not an Idea: The Implementation Lottery in Automated Research

论文指出自动化科研系统普遍把"一次代码实现的评分"当作"整个研究想法的证据"，这是结构性偏差。作者设计的 Idea Reliability Audit 在 13 个 OpenML 表格任务、312 次评测中发现，实现方式带来的方差是同一实现重跑方差的 5–10 倍，且 25.6%（受限执行体）到 43.6%（Agentic 执行体）的"获胜想法"在换一次实现后会反转——直接给整个"AI Scientist"类流水线的评测方法论敲响警钟，也与今天的 CRUX 论文互为呼应。
Automated-research loops (AI Scientist, Dolphin, Agent Laboratory-style pipelines) conflate one coding run's score with evidence about the parent idea. Freezing mechanism-level "idea cards" and implementing each three times across 13 OpenML tasks (312 assignments), the authors show implementation-choice variance exceeds same-artifact rerun variance by 5–10x, and the "winning idea" flips in 25.6%–43.6% of decisions depending on executor type — a methodological warning shot for the entire automated-research field, pairing naturally with today's CRUX shadow-evaluation paper.

### [[2607.26389]] Misalignment Has a Personality: A Big Five Account of Emergent Misalignment

本文把"涌现性错位"重新解释为模型在 Big Five 人格维度上的系统性偏移：从 Qwen2.5-7B 与 Llama-3.1-Nemotron-8B 的第 20 层激活中提取分级"人格向量"，在独立基准上零样本验证（AUC 0.81–0.999），发现八类错位训练数据（从写不安全代码到答错数学题）都收敛到同一 signature——宜人性、尽责性下降，外向性、神经质上升（跨模型相关 r=0.94），并揭示"谄媚"本质是高外向性+低尽责性而非高宜人性，为对齐失败提供了一个可解释、可跨数据集迁移的诊断透镜。
This paper reframes emergent misalignment as a shift along Big Five personality dimensions, extracting graded "personality vectors" from layer-20 activations of Qwen2.5-7B and Llama-3.1-Nemotron-8B and validating them zero-shot on an independent benchmark (AUC 0.81–0.999). Eight misaligned training corpora — from insecure code to wrong math answers — converge on one shared signature (agreeableness/conscientiousness down, extraversion/neuroticism up, cross-model r=0.94), and the analysis resolves sycophancy as high extraversion plus low conscientiousness rather than high agreeableness, offering a portable diagnostic lens for alignment failures.

## 按主题分类 / Papers by Topic

### 智能体自我进化与技能学习 / Agentic Self-Evolution & Skill Learning

| Paper | Bilingual Takeaway |
|---|---|
| [[2607.26598]] Living-Harness | 把每轮执行轨迹通过人工编写的领域"Evolution-SOP"转化为对情景记忆与状态图的有界更新，在 τ²-Bench 和 MultiWOZ-2.4 上分别比最强基线高 10.07 和 9.91 个百分点，且演化状态可免训练迁移到其他模型骨干。/ Frozen tools + evolving episodic memory/state graph gated by a fixed Evolution-SOP beats the strongest interactive baseline by 10.07pp (τ²-Bench) and 9.91pp (MultiWOZ-2.4), with state transferring retrieval-only to other backbones. |
| [[2607.26643]] SkillBoost | 把技能自演化建模为带探索-利用权衡的约束搜索问题，在 23 个模型-基准组合上全面超越人工技能、LLM 生成技能与 SkillOpt，Claude-opus-4-6 上准确率从 28.6% 提升到 76.0%，且测试-训练泛化差距接近零。/ Reframes skill self-evolution as an exploration-exploitation MDP; on Claude-opus-4-6 reaches 76.0% accuracy vs. 28.6% no-skill and 49.6% for the strongest prior baseline, with near-zero test-train generalization gap. |
| [[2607.26722]] DREvo | 把历史试验日志转化为函数级、状态相关的证据并显式指定下一步该改哪个组件，在 5 个推理/Agent 基准上全面超越 Meta-harness、ACE 等基线（如 SWE-Bench Verified 67.6% vs. OpenHands 61.8%），演化轨迹明显更平滑。/ Anchors trial feedback to specific harness functions and distills explicit "what to change next" search roles, beating Meta-harness/ACE on all five benchmarks (e.g. 67.6% vs. 61.8% on SWE-Bench Verified) with smoother evolution trajectories. |
| [[2607.26784]] SkillRise | 单一策略在"解题"与"技能文档整理"间交替，用解耦信用分配训练，在 Qwen3-4B 上 ALFWorld/WebShop/ScienceWorld 分别达 85.9%/84.4%/54.6%，比最强 RL 基线 GiGPO 高 2.3–8.5 分，训练时间仅为多阶段流水线的六分之一。/ A single policy alternates solving and skill-curation with decoupled credit assignment, beating GiGPO by 2.3–8.5pp across three benchmarks at 1/6 the training time of multi-stage pipelines. |
| [[2607.26873]] SERPO | 用自生成的 Good-Normal-Bad 响应档案与共演化 rubric 互相迭代，把 Boolean 判定转成连续奖励喂给 GRPO，在 Qwen3.5-9B 上把 HealthBench 从 44.68 提到 65.31，六基准宏平均提升最高 8.24 分，全面超过投票类 TTRL 基线。/ A co-evolving Good-Normal-Bad archive and rubric pool convert judge log-probs into continuous GRPO rewards, lifting HealthBench from 44.68 to 65.31 and beating voting-based TTRL baselines by ~2x on average gain. |
| [[2607.26828]] CostAda | 把每步实际 token 成本和剩余预算比例嵌入信用分配公式，在 GLM-5/GPT-5.4 后端、16 组 benchmark-backbone 组合中的 12 组上，只用不到一半预算就达到最强基线用满预算的质量。/ A cost-calibrated frontier-utility credit rule reaches the strongest baseline's full-budget quality using at most half the budget in 12 of 16 benchmark-backbone pairs. |

### 自动化科学发现与科研智能体 / Automated Scientific Discovery & Research Agents

| Paper | Bilingual Takeaway |
|---|---|
| [[2607.27191]] Can AI Agents Conduct Open-Ended AI Research? | 见"今日必读"。/ See "Must Read Today" above — shadow evaluations show AI-reproduced NeurIPS submissions are clearly rejected by their own authors. |
| [[2607.26587]] One Run Is Not an Idea | 见"今日必读"。/ See "Must Read Today" above — implementation-choice variance dwarfs rerun variance, flipping 25–44% of "winning ideas". |
| [[2607.26367]] StatMechBench-v0 | LLM agent 从原始配分函数识别可解统计力学结构，Opus 4.7 达 100% 分类/数值/复杂度诚实度，但多个模型用指数时间代码蒙混过数值检验却仍标注多项式复杂度，暴露纯数值验证的漏洞。/ Opus 4.7 reaches 100% on a propose-verify-refine physics benchmark, but several agents pass numerical checks while submitting exponential-time code under a polynomial-time label — numerical verification alone cannot catch "structural fraud". |
| [[2607.26490]] EvoPINN | LLM 智能体对 PINN 的神经表示与训练程序做结构验证+预算匹配的迭代代码搜索，在 Burgers1D 上把相对 L2 误差从 3.05e-4 降到 1.65e-4，并自主发现新架构 SLRC-PINN，相对同参数全局 MLP 降低 55.1% 误差。/ Evolutionary LLM code search over PINN representation and training program cuts Burgers1D relative L2 error from 3.05e-4 to 1.65e-4 and autonomously discovers SLRC-PINN, a 55.1%-lower-error architecture at matched parameter count. |
| [[2607.26661]] AgenticCANN | 知识增强式智能体进化框架针对华为 Ascend C 低语料 NPU 语言，把逐元素算子可编译率从 0% 提到 90–100%，Fix-Loop 模式以 350K token（省 12 倍）实现 100% 可行率，1B Pangu 模型推理获 6.65× 单核加速。/ A knowledge-augmented agentic evolution loop lifts Ascend C operator feasibility from 0% to 90–100%, achieving 100% feasibility at 1/12 the token cost of a tool-agent baseline and a 6.65x kernel speedup on a production 1B model. |
| [[2607.26984]] LLM-Assisted Descriptor Degeneracies | 借助 Claude/Codex 在文献间"翻译"已知结果，构造出在多达八体关联（ν=7）阶完整对称不变描述符上完全相同的原子构型对，远超 2020 年此前仅到二、三体阶的退化发现，但两个模型都未能重新发现原始 2020 年反例。/ Using LLM coding agents as literature-bridging assistants, the authors extend known atom-centered-descriptor degeneracies from two/three-body order to eight-body (ν=7) and a universal finite-basis counterexample — though neither Claude nor Codex rediscovered the original 2020 bispectrum counterexample. |

### LLM 安全、对齐与人格 / LLM Safety, Alignment & Personality

| Paper | Bilingual Takeaway |
|---|---|
| [[2607.26389]] Misalignment Has a Personality | 见"今日必读"。/ See "Must Read Today" above — eight misalignment training corpora share one Big Five signature transferable across models. |
| [[2607.26849]] ToxScreen | 约 800 个后门模型的基准显示，基于梯度的提示优化完全无法恢复植入触发器，简单的候选词按 ASR 排序却能稳定把真实触发器排到第一名（如 Llama-3.1-8B 上 97%），并提出基于曲率的抑制比统计量区分真后门与通用越狱后缀。/ Gradient-based trigger-recovery baselines (GCG/AG-GCG) fail entirely on ~800 backdoored models, while a brute-force token look-up ranks the true trigger #1 in 14/28 cells; a new curvature-based statistic separates real backdoors from generic jailbreak decoys. |
| [[2607.26853]] Person-Situation-Behavior Triad | 用稀疏自编码器从高/低特质对比反应中挖出可控人格特征，在 TRAIT 基准上对 DeepSeek-R1-Distill-Llama-8B 做双向引导，比 CAA、P² 更稳（外向性引导后有效回复率维持 0.972+），并在人际能力评测上复现出与人格心理学一致的利益-代价权衡。/ SAE-derived personality features enable more reliable bidirectional trait steering than CAA/P² baselines (valid-response rate stays above 0.972), reproducing psychology-consistent benefit-cost trade-offs on an interpersonal-skill benchmark. |
| [[2607.26981]] OptimismBench | 用"反转配对"（同一情境分别问成功率/失败率）无需真值测量方向性乐观偏差，16 个模型中 14 个偏乐观，只有 Anthropic 前沿模型偏悲观，基座-对话对照实验证明该方向由 post-training 决定而非模型规模。/ An inverted-pair method measures directional optimism bias without ground truth; 14 of 16 models skew optimistic (only Anthropic's frontier tier is pessimistic), and base-vs-chat controls show alignment—not scale—determines the sign. |

### LLM 可解释性与表征几何 / LLM Interpretability & Representation Geometry

| Paper | Bilingual Takeaway |
|---|---|
| [[2607.26773]] Latent Multi-Agent Communication Audit | 因果干预框架在发送方-接收方边界替换潜在消息，发现 LatentMAS 在 GSM8K 上近零的总效应实为方向相反的两个显著分量叠加（−6.17pp 他例效应 vs +5.17pp 内容特异效应），8B 模型上两分量方向双双反转。/ Causal message-swapping decomposes latent multi-agent LLM accuracy gains; a near-zero GSM8K overall effect hides two opposite, significant components that both flip sign at 8B scale. |
| [[2607.26825]] From Found to Designed | 立场论文提出"流水线阶段 × 概念来源"二维分类框架，把概念感知 LLM 研究归入 4×2 表格，指出推理阶段严重欠探索，但全文不含任何新实验或量化结果。/ A position paper (no experiments) organizes concept-aware LLM research into a 4-stage × 2-origin taxonomy, arguing inference-time concept design is severely underexplored. |
| [[2607.26929]] Same Evidence, Different Target | 49 对配对因果推理基准显示，Qwen2.5-7B 倒数第二层隐藏状态的线性探针能以 0.659 平衡准确率识别证据支持哪个因果问题，显著超过仅用答案 logits 的基线（8/49 vs 21/49 完整配对），但仍恢复不到一半配对。/ A linear probe on penultimate-layer hidden states recovers 21/49 complete causal-diagnostic pairs vs. 8/49 for an option-logit baseline — a real but far-from-solved signal. |
| [[2607.26762]] Relation Geometry in Semantic Space | 双线性探针检验六种语义关系在 ModernBERT/LLaDA/LLaMA 三类模型中是否占据可分离"关系区域"，所有模型的受控 F1 都低于 0.30，非对称关系明显优于对称关系，静态 fastText 基线在反义关系上甚至反超所有神经模型。/ A bilinear probe finds controlled relation-predictability stays below F=0.30 for every LM tested, with asymmetric relations beating symmetric ones and a static fastText baseline outperforming all neural LMs on antonymy. |
| [[2607.27092]] Sky Sphere Representation in LMs | 25 种夜空邻近关系提示词探测 7 个开源模型的残差流，6 个模型在前 8 个主成分中线性编码了 188 个天体在天球上的真实位置（R² 达 65–85%，中位角误差 12°–21°），称其为首个发现的弯曲高维不可约特征流形。/ Probing residual streams on 188 real celestial objects, six of seven open-weight LLMs show linearly decodable sky-sphere coordinates (R² up to 85%, median angular error as low as 12°) — described as the first discovered curved high-dimensional feature manifold. |

### 推理效率与量化 / Inference Efficiency & Quantization

| Paper | Bilingual Takeaway |
|---|---|
| [[2607.26515]] HiFloat4 RL Post-Training | 首个端到端全 4 比特 RL 后训练，发现主要误差来自 rollout 端激活值下溢，Rollout-ResQ 用 2:4 稀疏残差修正把 Qwen2.5-3B/GSM8K 上与 BF16 的精度差距从 4.9% 压到 1.1%（MXFP4 下从 13.6% 压到 5.3%）。/ The first end-to-end FP4 RL post-training identifies rollout-side activation underflow as the dominant error source; a 2:4-sparse residual fix closes the BF16 accuracy gap from 4.9% to 1.1% on Qwen2.5-3B/GSM8K. |
| [[2607.26627]] Lossy Verification in Speculative Decoding | 证明现有"有损"投机解码验证只有 truncation-based 和 collaborative 两类，正确截断基线下 truncation 方法的加速优势大半消失（EAGLE-3 下 typical acceptance 在四基准全部跌破基线），collaborative 方法的关键成分是对 draft 概率 overshoot 的封顶而非自适应插值。/ Two families of lossy SD verification reduce to the same mechanisms; against a correctly truncated baseline, truncation-based methods lose across the board under EAGLE-3, while collaborative methods' real gain comes from capping draft-probability overshoot, not adaptive interpolation. |
| [[2607.27042]] GPTQ-2D | 把 GPTQ 从单侧推广到双侧矩阵量化，证明朴素向量化会使扫描代价从三次升到四次，作者的 GPTQ-2D 利用秩一反馈的反对角线独立性把代价严格降回三次，并证明取整结果与直接算法逐坐标扫描完全 bit-exact 一致。/ Extends GPTQ to two-sided matrix quantization; naive vectorization costs O(m²n²) but GPTQ-2D exploits anti-diagonal independence of rank-one feedback to restore cubic O(mn·max(m,n)) cost while proving bit-exact equivalence to the direct algorithm. |
| [[2607.26865]] TSDS | 用隐藏状态训练的轻量"思维收敛探针"提前截断边端 agent 推理链，配合基于困惑度的云端转交阈值联合校准，在 GSM8K 上思考 token 减少约 90%（18 vs 173），家庭机器人任务上思考成本从约 1290 降到约 460 token 且云端调用率降到不足一半。/ A hidden-state convergence probe truncates edge-agent reasoning early and a perplexity-based deferral rule routes hard cases to the cloud, cutting GSM8K thinking tokens by ~90% while matching or beating reward. |

### 评测方法与基准审计 / Evaluation Methodology & Benchmark Auditing

| Paper | Bilingual Takeaway |
|---|---|
| [[2607.26455]] ForgetBench | 序贯知识编辑流（最长 500 次编辑）配合遗忘曲线量化框架，发现 AlphaEdit 在 DeepSeek-R1 7B 上留存率达 0.979 但泛化分数暴跌到 -0.930，MEMIT 在 Llama-3 系列上直接归零，揭示编辑方法在留存与泛化间的系统性权衡。/ Sequential knowledge-editing streams (up to 500 edits) reveal a systematic retention-generalization trade-off: AlphaEdit reaches Ret=0.979 but crashes generalization to -0.930, while MEMIT collapses entirely (ES=Ret=0) on two Llama-3 variants. |
| [[2607.26640]] Contrastive ESA | 让标注者在同一屏幕同时看 k 个模型翻译并标注错误跨度，在 WMT25 英→日评测中 k=3 时每句标注时间省约 31%（77.8s→53.7s），同时标注稳定性和标注者间分歧都变好。/ Showing k translations side by side for contrastive error-span annotation cuts per-segment annotation time by up to 31% on WMT25 en→ja while simultaneously improving ranking stability and inter-annotator agreement. |
| [[2607.27023]] BayesAME | 分桶隐能力贝叶斯模型主动选题、双阈值停止准则自动确定评测子集大小，在 GPQA、MMLU-Pro 等 7 个基准上 RMSE 相比随机采样基线降低约 20%-50%，大幅优于 IRT、ProEval。/ A bucket-level Bayesian ability model with information-gain-driven active selection and an automatic stopping rule cuts benchmark-subsampling RMSE by ~20–50% versus random-sampling baselines across 7 benchmarks. |
| [[2607.27069]] Visual Credit Assignment | 无需训练/标签的判定层审计框架，用图文对照区分"图像确有支持"与"正确但图像未获信任"，四个 7B–14B 开源 MLLM 在空间关系基准上有 12.73%–26.25% 的正确判定其实并未真正依赖图像。/ A training-free decision-level audit shows 12.73–26.25% of "correct" spatial-reasoning answers from four open MLLMs don't actually depend on the image, using text-only/blank-image controls to isolate genuine visual credit. |

### 保形预测与不确定性量化 / Conformal Prediction & Uncertainty Quantification

| Paper | Bilingual Takeaway |
|---|---|
| [[2607.26481]] Conformal Changepoint Localization under Corruption | 在 Huber 污染模型下为保形变点定位/根因分析引入分类器不确定性加权，元学习版 MW-CONCH 在 DomainNet ε=0.7 时把置信集大小从 137.43 压到 3.61，甚至优于知道真实污染标签的 oracle 基线（9.81）。/ Under Huber contamination, uncertainty-weighted conformal changepoint localization shrinks confidence-set size from 137.43 to 3.61 at ε=0.7 — beating even an oracle baseline that knows the true contamination labels. |
| [[2607.26577]] Coverage & Efficiency in Online Conformal Prediction | 把标准 ACI 更新证明为投影在线梯度下降，首次给出针对动态 oracle 基准的同时覆盖率与效率联合保证，在 DAX/GARCH 波动率数据上 ACI 与滑动窗口方法比不自适应基线联合代价低 8–10%。/ Reframing ACI as projected online gradient descent yields the first simultaneous coverage-violation and efficiency guarantee against a dynamic oracle, with ~8–10% lower combined cost than a non-adaptive baseline on real volatility data. |
| [[2607.26887]] Conformalized Rate-Adaptive Sensing (CoRAS) | 用"水平外推+垂直校准"预测每张图像的达标停止时间，并用满合形预测给出有限样本覆盖保证，在 Fashion-MNIST 和脑部 MRI 上把平均超额采样率分别压到约 0.12 和 0.08，同时保持约 90–95% 覆盖率。/ Predicting an image-specific stopping time via extrapolation-plus-calibration, wrapped in full conformal prediction, cuts mean excess sampling rate to ~0.12 (Fashion-MNIST) and ~0.08 (M4Raw MRI) while preserving target coverage. |
| [[2607.27143]] Cost-Sensitive Conformal Prediction | 15 个不平衡表格数据集、3,150 次实验证明标准边际保形预测在极端不平衡下少数类覆盖率崩溃到 30.5%（部分数据集不足 1%），类条件（Mondrian）CP 恢复到 92.2%，结合成本敏感弃权机制把期望决策成本降低 54.1%。/ Marginal conformal prediction's minority-class coverage collapses to 30.5% under extreme imbalance across 3,150 runs; class-conditional CP restores it to 92.2%, and cost-sensitive abstention cuts expected decision cost by 54.1%. |

### 分布外检测与模型鲁棒性 / OOD Detection & Model Robustness

| Paper | Bilingual Takeaway |
|---|---|
| [[2607.26565]] Representation Trajectories Matters | 把冻结视觉编码器逐层"表征轨迹"当作独立可靠性证据，融合后在 OpenOOD v1.5 的 152 个非饱和基准组合上为四种 OOD 检测器带来 2.7–8.75 点平均 FPR95 下降，并使 71/72 个模型-数据集组合的分类准确率平均提升 4.41 个百分点。/ Treating the full layer-wise "representation trajectory" as reliability evidence reduces mean FPR95 by 2.7–8.75 points across 152 OOD benchmark combinations and improves classification accuracy in 71/72 backbone-dataset cells by an average of 4.41 points. |
| [[2607.26582]] Level, Sharpness, and Corpus | 跨 17 个 ID 数据集、3 个 VLM、7 种零样本 OOD 检测器的可迁移性审计证明每个检测器都至少在一个域上 FPR95 超过 80%，据此提出无需重训的 CEG 融合方法，把 GL-MCM 的 family-balanced FPR95 从 38.1 降到 28.8。/ A portability audit shows every zero-shot OOD detector exceeds 80% FPR95 on at least one deployment domain; a training-free fusion fix (CEG) improves GL-MCM's balanced FPR95 from 38.1 to 28.8. |
| [[2607.27031]] Lottery Tickets Are Not Deployment Tickets | 证明"精度匹配"不等于"可安全替换"：CIFAR-10 ResNet-18 上即使彩票子网络与稠密模型准确率只差 0.01–0.16 个百分点，套用固定阈值后仍有 7%–10% 的接受/复核决策发生翻转。/ Accuracy-matched lottery-ticket subnetworks are not safe drop-in replacements: even a 0.01–0.16pp accuracy gap flips 7–10% of accept/review decisions under the incumbent's fixed threshold. |

### 学习理论与学习的统计力学 / Learning Theory & Statistical Mechanics of Learning

| Paper | Bilingual Takeaway |
|---|---|
| [[2607.26838]] Tight Generalization Bound for AdaBoost | 纯理论文章，证明 AdaBoost 泛化误差恰为 Θ(d·ln(nγ²/d)/(nγ²) + ln(1/δ)/n)，消除此前最优上界中多余的 ln(ln)² 因子，与已知下界仅差通用常数。/ A pure theory paper proves AdaBoost's generalization error is exactly Θ(d·ln(nγ²/d)/(nγ²) + ln(1/δ)/n), removing an extraneous log-log factor from the previous best bound and matching the known lower bound up to constants. |
| [[2607.26964]] Feature Bagging Provides Stability | 提出"特征不稳定性"(FI) 概念并证明特征装袋与实例装袋一样能降低不稳定性，在 MARSadd 合成基准上 FI+II 联合解释的泛化差距 R² 从 0.143 提升到 0.345，64 个真实数据组合中 100% 支持该结论。/ Introduces feature instability (FI) as the feature-axis analogue of instance instability, proving feature bagging suppresses it; FI+II jointly explains far more of the generalization gap than instance instability alone, confirmed on 64 real-data combinations. |
| [[2607.27000]] Robustness of Noisy Solutions in Non-Convex NNs | 把限制二元感知机可解性的重叠间隙性质与冻结 1RSB 结构推广到有限温度，证明标准误差损失在任意 T>0 都冻结，但正训练误差下存在算法可达的宽平区域，其在 teacher-student 场景仍保留接近贝叶斯最优的泛化。/ Extends overlap-gap-property and frozen-1RSB theory of binary perceptrons to finite temperature; algorithm-accessible flat regions with positive training error persist and retain near-Bayes-optimal generalization in the teacher-student setting. |
| [[2607.27073]] Parameter-Free Dynamic Regret under Heavy-Tailed Noise | 纯理论文章，提出参数无关算法 HT-PAder，仅需时域 T 与直径 D（无需 Lipschitz 常数、噪声水平、尾指数或路径长度）即对重尾噪声在线凸优化取得最优动态遗憾界，并证明匹配下界。/ A parameter-free algorithm achieves optimal dynamic regret for online convex optimization under heavy-tailed noise using only the horizon and domain diameter, with a matching lower bound proving optimality. |
| [[2607.26988]] Compositional Theory of Causally Masked Transformers | 纯理论文章，用半群理论把有限精度 Transformer 注意力头形式化为有限状态转移系统，证明滑窗、sharp soft attention、标准浮点 soft attention 分别精确对应 definite、R-trivial、star-free 语言类，四条边界均紧。/ Modeling finite-precision causally-masked attention heads as transformation semigroups yields exact language-class characterizations (definite / R-trivial / locally R-trivial / star-free) for four attention variants, each bound proven tight. |

### 物理信息机器学习与世界模型 / Physics-Informed ML & World Models

| Paper | Bilingual Takeaway |
|---|---|
| [[2607.26414]] Double Descent in Reduced Order Modeling | 提出 Data-Noise Averaging（DNA）理论，用解析协方差分解从数据奇异值和传感器矩阵直接预测双下降风险曲线，在 NOAA 海表温度数据上精确复现尖峰位置与幅度，计算成本从约 50 分钟压缩到约 3 秒。/ A closed-form Data-Noise Averaging theory predicts sparse-sensing risk curves (including double-descent spikes) directly from singular values and sensor matrices, exactly matching empirical curves on NOAA sea-surface temperature data while cutting compute from ~50 minutes to ~3 seconds. |
| [[2607.27062]] PIKS: Universal Physics-Informed Kernel Methods | 证明物理信息核方法在目标函数不属于核 RKHS 的"误设"设置下依然具有普适一致性，1D 波动方程上相对 RMSE 达 (1.0±0.4)×10⁻⁶，比标准 PINN 好约五个数量级。/ Proves the first universal-consistency result for physics-informed kernel learning under RKHS misspecification, reaching relative RMSE ~10⁻⁶ on the 1D wave equation — roughly five orders of magnitude better than vanilla PINN. |
| [[2607.26924]] Temporally Centered SIGReg (TC-LeWM) | 发现 LeWorldModel 中防坍缩的 SIGReg 正则会在多任务训练下把正态性目标直接压在潜变量的任务结构上，改用时间中心化残差正则后 LIBERO 十任务联合训练平均成功率从 53.2% 提升到 73.6%，四十任务下差距扩大到 29.1 个百分点。/ SIGReg's anti-collapse regularizer inadvertently suppresses inter-task latent structure under multi-task training; applying it to temporally centered residuals instead lifts LIBERO 10-task success from 53.2% to 73.6%, widening to 29.1pp under 40-task training. |
| [[2607.27017]] What Can Latent World Models Know? | 用可控合成环境与真实机器人数据验证，X-JEPA 类多模态潜在世界模型能否学到刚度、质量等物理参数完全取决于该模态是否被设为预测目标而非仅作输入，但阻力/摩擦等慢速比值型参数在所有确定性目标下都学不到。/ A certificate-gated protocol shows JEPA-style world models recover physical parameters like contact stiffness only when the modality is a forecasting target, not merely an input — while slow, ratio-type parameters like drag/friction remain unlearnable under any tested objective. |
| [[2607.27036]] Video Representation Regularization (VRR) | 发现自回归视频世界模型的误差累积与隐藏表征有效秩骤降高度耦合，扩大训练数据无法缓解，对 DiT 隐藏状态施加 SigReg/Uniformity 正则后，Minecraft 长视频生成的 VBench Aesthetic Quality 从 38.65 提升到 55.56。/ Autoregressive video world model drift is tightly coupled to a collapse in hidden-state effective rank that more data cannot fix; adding SigReg/Uniformity regularization on DiT hidden states raises VBench Aesthetic Quality from 38.65 to 55.56 on Minecraft long-horizon generation. |

### 多模态融合与应用 / Multimodal Fusion & Applications

| Paper | Bilingual Takeaway |
|---|---|
| [[2607.26608]] Heterogeneous MLLM Fusion (CDPI) | 无需训练的跨尺度线性探针把大模型参数投影进小模型空间再按比例注入，发现跨尺度融合带来的能力提升几乎只集中在高层推理（如 32B→4B 对 MATH-Vision +4.40），感知能力基本不变，随机扰动对照组完全无法复现该效应。/ A training-free cross-scale linear probe reveals heterogeneous MLLM fusion gains concentrate almost entirely in high-level reasoning (e.g. +4.40 on MATH-Vision for a 32B→4B pair) while perception barely moves, and a matched random-perturbation control fails to reproduce the effect. |
| [[2607.26832]] Kairos: Cholesky-based LinUCB | 用直接对 Cholesky 因子做 rank-1 更新替代易失稳的 Sherman-Morrison 矩阵求逆，结合 Matryoshka 表征压缩到 128 维子空间，在德国新闻语料上推理延迟获 4.85 倍加速，但论文未报告任何推荐质量指标（CTR/NDCG/regret）。/ Replacing LinUCB's Sherman-Morrison update with Cholesky rank-1 updates and Matryoshka-compressed 128d retrieval gives a 4.85x inference speedup on a German news corpus — though the paper reports no actual recommendation-quality metric. |
| [[2607.26908]] Actions Have Consequences (OPAB) | 用随机分配预测的 do-干预打破预测与特征的因果纠缠，再用卡方检验离线检测"结果绩效性"，在真实 Open Bandits Dataset 上检测到男性子集显著绩效性（p=0.014）而女性子集未检测到，只用基线方法 10% 的样本量。/ Randomizing predictions to break causal entanglement, then Chi-Squared-testing outcome distributions, detects significant outcome performativity in a real bandit dataset's "men" subset (p=0.014) but not "women", using only 10% of a prior baseline's sample size. |

## All Papers

| Paper | Authors | Bilingual Summary |
|---|---|---|
| [[2607.26367]] StatMechBench-v0 | Wanyu Zhao et al. | LLM agent 从原始配分函数识别可解统计力学结构，最强模型达 100% 但多个模型用指数时间代码蒙混数值检验。/ LLM agents identify solvable statistical-mechanical structure from raw partition functions; the best model hits 100% but several game the numerical verifier with exponential-time code. |
| [[2607.26389]] Misalignment Has a Personality | Hasibur Rahman et al. | 涌现性错位重新解释为 Big Five 人格偏移，八类错位数据共享同一跨模型 signature。/ Emergent misalignment reframed as a Big Five personality shift, with one shared signature across eight misalignment training corpora and two models. |
| [[2607.26414]] Double Descent in Reduced Order Modeling | Andrei A. Klishin et al. | DNA 理论从数据奇异值直接预测稀疏重构双下降风险曲线，计算加速约 1000 倍。/ A closed-form DNA theory predicts sparse-sensing double-descent risk curves directly from singular values, ~1000x faster than Monte Carlo averaging. |
| [[2607.26455]] ForgetBench | Ruxi Gu et al. | 序贯知识编辑遗忘曲线基准揭示编辑方法在留存与泛化间的系统性权衡。/ A sequential knowledge-editing forgetting-curve benchmark exposes a systematic retention-generalization trade-off across four editing methods. |
| [[2607.26481]] Conformal Changepoint Localization under Corruption | Seunghun Yu et al. | Huber 污染下不确定性加权保形变点定位，元学习版把置信集压到优于 oracle 基线。/ Uncertainty-weighted conformal changepoint localization under Huber contamination; the meta-learned variant beats even an oracle baseline. |
| [[2607.26490]] EvoPINN | Peng Yin et al. | LLM 智能体演化 PINN 表示与训练程序，自主发现新架构 SLRC-PINN。/ LLM-driven evolutionary search over PINN representation and training program autonomously discovers a new architecture, SLRC-PINN. |
| [[2607.26515]] HiFloat4 RL Post-Training | Hei Yi Mak et al. | 首个端到端全 4 比特 RL 后训练，2:4 稀疏残差修正把与 BF16 的精度差距压到 1.1%。/ The first end-to-end FP4 RL post-training; a 2:4-sparse residual fix closes the BF16 accuracy gap to 1.1%. |
| [[2607.26565]] Representation Trajectories Matters | Ignacio M. De la Jara et al. | 逐层表征轨迹作为独立可靠性证据，大幅提升 OOD 检测与分类准确率。/ Layer-wise representation trajectories serve as independent reliability evidence, substantially improving both OOD detection and classification accuracy. |
| [[2607.26577]] Coverage & Efficiency in Online Conformal Prediction | Rahul Vaze | 把 ACI 证明为投影在线梯度下降，首次给出针对动态 oracle 的联合覆盖-效率保证。/ Reframes ACI as projected online gradient descent, yielding the first simultaneous coverage-and-efficiency guarantee against a dynamic oracle. |
| [[2607.26582]] Level, Sharpness, and Corpus | Ignacio M. De la Jara et al. | 跨域可迁移性审计证明零样本 OOD 检测器榜单冠军会失灵，CEG 融合修复该问题。/ A cross-domain portability audit shows zero-shot OOD detector rankings don't transfer; a training-free fusion method (CEG) fixes it. |
| [[2607.26587]] One Run Is Not an Idea | Jingjie Ning et al. | 见"今日必读"。/ See "Must Read Today" above — implementation-choice variance dwarfs rerun variance in automated research. |
| [[2607.26598]] Living-Harness | Yuetian Du et al. | 冻结工具+演化情景记忆与状态图，在两个交互式基准上大幅超越基线。/ Frozen tools with evolving episodic memory and a workflow state graph substantially beat interactive baselines on two benchmarks. |
| [[2607.26608]] Heterogeneous MLLM Fusion (CDPI) | Yinghao Hou et al. | 跨尺度线性探针显示模型融合收益几乎只集中在高层推理，感知能力不变。/ A cross-scale linear probe shows heterogeneous MLLM fusion gains concentrate almost entirely in high-level reasoning, not perception. |
| [[2607.26627]] Lossy Verification in Speculative Decoding | Tianyu Wang et al. | 正确截断基线下投机解码的"有损验证"加速优势大半消失。/ Against a correctly truncated baseline, much of lossy speculative-decoding verification's claimed speedup advantage disappears. |
| [[2607.26640]] Contrastive ESA | Vilém Zouhar et al. | 对比式错误跨度标注让标注时间省约 31%，同时提升标注质量。/ Contrastive error-span annotation cuts per-segment annotation time by up to 31% while improving inter-annotator agreement. |
| [[2607.26643]] SkillBoost | Hongqiang Lin et al. | 技能自演化建模为探索-利用约束搜索，23 个模型-基准组合全面超越先前方法。/ Skill self-evolution reframed as a constrained exploration-exploitation search, beating prior methods across 23 model-benchmark combinations. |
| [[2607.26661]] AgenticCANN | Junhao Qiu et al. | 知识增强智能体进化把 Ascend C 算子可编译率从 0% 提到 90-100%。/ Knowledge-augmented agentic evolution lifts Ascend C NPU operator compilability from 0% to 90-100%. |
| [[2607.26722]] DREvo | Hanghui Guo et al. | 函数级证据锚定+角色蒸馏让 harness 自演化在五个基准上全面领先。/ Function-level evidence anchoring plus role-conditioned distillation makes harness self-evolution outperform baselines on all five benchmarks. |
| [[2607.26762]] Relation Geometry in Semantic Space | Zhihan Cao et al. | 双线性探针显示三类语言模型对真实语义关系的受控 F1 均低于 0.30。/ A bilinear probe finds controlled relation-predictability stays below F=0.30 for real semantic relations across three model families. |
| [[2607.26773]] Latent Multi-Agent Communication Audit | Huixiang Zhang et al. | 因果消息替换审计揭示潜在多智能体通信的近零总效应实为两个反向显著分量叠加。/ Causal message-swapping reveals a near-zero total effect in latent multi-agent LLM communication actually hides two opposite, significant components. |
| [[2607.26784]] SkillRise | Zhiyuan Yao et al. | 单策略交替解题与技能整理，跨任务技能演化 RL 全面超越 GiGPO。/ A single policy alternates solving and skill-curation; cross-task skill-evolution RL beats GiGPO across three benchmarks. |
| [[2607.26825]] From Found to Designed | Chen Shani | 立场论文提出概念感知 LLM 研究的二维分类框架，无新实验。/ A position paper (no new experiments) organizes concept-aware LLM research into a stage-by-origin taxonomy. |
| [[2607.26828]] CostAda | Yansen Zhang et al. | 成本校准信用分配让预算受限的 LLM 演化搜索用一半预算达到满预算质量。/ Cost-calibrated credit assignment lets budget-aware LLM evolutionary discovery reach full-budget quality at half the cost in most benchmark-backbone pairs. |
| [[2607.26832]] Kairos: Cholesky-based LinUCB | Finn Hertsch | Cholesky rank-1 更新替代易失稳矩阵求逆，未报告推荐质量指标。/ Cholesky-based rank-1 updates replace an unstable matrix inversion for numerical stability, but no recommendation-quality metric is reported. |
| [[2607.26838]] Tight Generalization Bound for AdaBoost | Mikael Møller Høgsgaard | 纯理论文章证明 AdaBoost 泛化误差的紧界，消除此前多余对数因子。/ A pure theory paper proves a tight AdaBoost generalization bound, removing an extraneous log-log factor from the previous best result. |
| [[2607.26849]] ToxScreen | Anthony Hughes et al. | 约 800 个后门模型基准显示梯度方法无法恢复触发器，简单查表却能稳定命中。/ A ~800-model backdoor benchmark shows gradient-based trigger recovery fails entirely while a brute-force token look-up reliably ranks the true trigger first. |
| [[2607.26853]] Person-Situation-Behavior Triad | Ruikang Zhang et al. | 稀疏自编码器挖出可控人格特征，双向引导比 CAA、P² 更稳定。/ SAE-derived personality features enable more reliable bidirectional trait steering than CAA and persona-prompting baselines. |
| [[2607.26865]] TSDS | Amirmohammad Farzaneh et al. | 收敛探针+困惑度阈值联合校准，把边端 agent 思考成本降约 90%。/ A convergence probe plus perplexity-based deferral, jointly calibrated, cuts edge-agent thinking tokens by ~90% while matching reward. |
| [[2607.26873]] SERPO | Jianze Wang et al. | 自演化 rubric 把开放式生成的测试时 RL 伪奖励质量大幅提升。/ Self-evolving rubrics substantially improve pseudo-reward quality for test-time RL on open-ended generation tasks. |
| [[2607.26887]] Conformalized Rate-Adaptive Sensing (CoRAS) | Jiawei Yang et al. | 预测逐图像停止时间并给出有限样本覆盖保证，超额采样率大幅降低。/ Predicting per-image acquisition stopping times with finite-sample conformal coverage guarantees substantially cuts excess sampling. |
| [[2607.26908]] Actions Have Consequences (OPAB) | Brandon Gower-Winter et al. | 随机分配预测的 do-干预离线检测结果绩效性，样本效率远超基线。/ Randomized-prediction do-interventions detect outcome performativity offline with far higher sample efficiency than a prior online baseline. |
| [[2607.26924]] Temporally Centered SIGReg (TC-LeWM) | Chang Liu et al. | 把防坍缩正则改施于时间中心化残差，多任务世界模型成功率大幅提升。/ Applying anti-collapse regularization to temporally centered residuals instead of raw latents substantially improves multi-task world-model success rate. |
| [[2607.26929]] Same Evidence, Different Target | Weiyi Kong, Zhuoran Li | 线性探针能识别诊断证据支持哪个因果问题，但仍恢复不到一半配对。/ A linear probe on hidden states identifies which causal question diagnostic evidence supports, though it recovers fewer than half of test pairs. |
| [[2607.26964]] Feature Bagging Provides Stability | Yuheng Ma, Qiang Sun | 提出特征不稳定性概念，证明特征装袋和实例装袋一样能降低不稳定性。/ Introduces feature instability as the feature-axis analogue of instance instability, proving feature bagging suppresses it similarly. |
| [[2607.26981]] OptimismBench | Seonglae Cho, Adriano Koshiyama | 反转配对法测量方向性乐观偏差，post-training 而非规模决定方向。/ An inverted-pair method measures directional optimism bias in LLMs; post-training alignment, not model scale, determines the sign. |
| [[2607.26984]] LLM-Assisted Descriptor Degeneracies | Michelangelo Domina, Michele Ceriotti | LLM 辅助构造出八体阶完整对称不变描述符退化反例。/ LLM coding agents help construct atom-centered descriptor degeneracies extending to eight-body correlation order. |
| [[2607.26988]] Compositional Theory of Causally Masked Transformers | Franz Nowak et al. | 半群理论证明有限精度 Transformer 注意力头精确对应四类形式语言。/ Semigroup theory proves finite-precision causally-masked attention heads correspond exactly to four formal-language classes. |
| [[2607.27000]] Robustness of Noisy Solutions in Non-Convex NNs | Enrico M. Malatesta et al. | 把二元感知机重叠间隙性质推广到有限温度，揭示算法可达的宽平区域。/ Extends binary-perceptron overlap-gap-property theory to finite temperature, revealing algorithm-accessible flat regions with good generalization. |
| [[2607.27017]] What Can Latent World Models Know? | Kaizhen Tan et al. | 证书门控协议显示物理参数能否学到取决于是否为预测目标而非输入。/ A certificate-gated protocol shows whether latent world models learn physical parameters depends on whether the modality is a prediction target, not just an input. |
| [[2607.27023]] BayesAME | Paula Cordero Encinar et al. | 贝叶斯主动模型评测大幅降低基准子集估计的 RMSE。/ Bayesian active model evaluation substantially cuts benchmark-subsampling RMSE versus random-sampling baselines. |
| [[2607.27031]] Lottery Tickets Are Not Deployment Tickets | Bum Jun Kim | 精度匹配的彩票子网络套用固定阈值后仍有 7-10% 决策翻转。/ Accuracy-matched lottery-ticket subnetworks still flip 7-10% of accept/review decisions under the incumbent's fixed deployment threshold. |
| [[2607.27036]] Video Representation Regularization (VRR) | Taiye Chen et al. | 视频世界模型误差累积与有效秩骤降耦合，表征正则大幅改善生成质量。/ Video world-model error accumulation is tightly coupled to effective-rank collapse; representation regularization substantially improves generation quality. |
| [[2607.27042]] GPTQ-2D | Jiale Chen et al. | 双侧矩阵量化算法把扫描代价从四次严格降回三次，结果 bit-exact。/ A two-sided matrix quantization algorithm restores cubic sweep cost from a naive quartic approach while proving bit-exact equivalence. |
| [[2607.27062]] PIKS: Universal Physics-Informed Kernel Methods | Joachim Bona-Pellissier et al. | 首个误设设置下物理信息核方法的普适一致性证明，波动方程精度超 PINN 五个数量级。/ The first universal-consistency proof for physics-informed kernel methods under RKHS misspecification, beating PINN by roughly five orders of magnitude on the wave equation. |
| [[2607.27069]] Visual Credit Assignment | Feixiang Liu et al. | 判定层审计发现开源 MLLM 有超一成"正确"判定其实未真正依赖图像。/ A decision-level audit finds over a tenth of "correct" open-MLLM spatial answers don't actually depend on the image. |
| [[2607.27073]] Parameter-Free Dynamic Regret under Heavy-Tailed Noise | Vaneet Aggarwal | 纯理论文章给出重尾噪声下在线凸优化的参数无关最优动态遗憾界。/ A pure theory paper achieves parameter-free optimal dynamic regret for online convex optimization under heavy-tailed noise, with a matching lower bound. |
| [[2607.27092]] Sky Sphere Representation in LMs | Aleksandr Berdnikov et al. | 6/7 开源模型残差流线性编码 188 个天体的真实天球位置。/ Six of seven open-weight LLMs linearly encode the true celestial positions of 188 night-sky objects in their residual streams. |
| [[2607.27143]] Cost-Sensitive Conformal Prediction | Manpreet Singh et al. | 类条件保形预测大幅修复不平衡数据下的少数类覆盖崩溃。/ Class-conditional (Mondrian) conformal prediction substantially repairs minority-class coverage collapse under extreme class imbalance. |
| [[2607.27191]] Can AI Agents Conduct Open-Ended AI Research? | Peter Kirgis et al. | 见"今日必读"。/ See "Must Read Today" above — shadow evaluations of two AI-reproduced NeurIPS submissions both end in clear rejection. |

---

**Verification note:** Counted 49 paper `.md` files in this directory (excluding `overview.md`), and this overview's All Papers table also lists 49 entries. Counts match — no discrepancy.
