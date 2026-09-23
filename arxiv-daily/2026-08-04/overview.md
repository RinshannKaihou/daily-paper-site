---
title: "Daily arXiv Digest — 2026-08-04"
date: 2026-08-04
tags:
  - reasoning
  - mechanistic-interpretability
  - inference-efficiency
  - llm-agents
  - alignment
  - post-training
  - evaluation-methodology
papers: 41
---

# Daily arXiv Digest — 2026-08-04

今日共精选 **41** 篇论文，覆盖 LLM 推理与测试时计算、机制可解释性、推理高效化、智能体与自我进化、对齐与安全、训练与后训练、以及评测方法学等方向。

Today's digest curates **41** papers spanning LLM reasoning & test-time compute, mechanistic interpretability, inference efficiency, agents & self-evolution, alignment & safety, training & post-training, and evaluation methodology.

---

## 今日必读 / Must Read Today

### 1. [[2608.03573]] SFT Conflicts, RL Coexists

**推荐理由：** 首次系统给出"SFT 在多阶段训练中因稠密冲突更新而崩溃、RL 因稀疏近正交更新而共存"的理论与实证解释，并提出可落地的 Parallel-RL 并行训练范式（合并后保留单任务 RL 性能 97–103%）。

**Why read:** First systematic theory + evidence for why multi-stage SFT collapses (-23.1%) while multi-stage RL stably improves (+24.9%), plus a drop-in Parallel-RL recipe that retains 97–103% of single-task RL performance after merging. A directly actionable result for anyone doing multi-task post-training.

### 2. [[2608.03457]] LLaDA MoE v2: Scaling Mixture-of-Experts Diffusion Language Models

**推荐理由：** 推导出扩散语言模型（dLLM）专属的 scaling law，并据此从零训练 30B-A3B MoE dLLM，仅用 Qwen3 约 65% 的预训练 token 即在多个知识/推理/代码基准上接近 Qwen3，是非自回归 LLM 路线的标志性进展。

**Why read:** Derives dLLM-specific scaling laws and trains a 30B-A3B MoE diffusion language model from scratch on 23.5T tokens, approaching Qwen3-30B-A3B with ~65% of its pretraining tokens — a landmark result for the non-autoregressive LM line of work.

### 3. [[2608.03291]] The Tell-Tale Trace: Detecting Reasoning Failures in LLMs Using CoT Dynamics

**推荐理由：** 不假设 CoT 忠实反映内部计算，通过对推理链句子功能角色的动态建模，在 SAT/UNSAT 任务上揭示两种失败模式，并用流程专属提示将 Llama3-70B 的 UNSAT 准确率从 13.3% 提升至 85.0%。

**Why read:** Without assuming CoT faithfulness, tags reasoning-trace sentences by role and identifies "premature verification collapse" and procedure-mismatch failure modes on SAT/UNSAT — a targeted intervention lifts Llama3-70B UNSAT accuracy from 13.3% to 85.0% (84.6% of failures corrected vs 11.5% for generic retry).

---

## 按主题分类 / Papers by Topic

### 推理与测试时计算 / Reasoning & Test-Time Scaling

| Paper | 主题 / Topic |
|-------|-------------|
| [[2608.03291]] CoT Dynamics Failure Detection | 通过句子角色动态诊断 SAT/UNSAT 推理失败，干预提示将准确率从 13.3% 提升至 85.0%。 / Diagnoses SAT/UNSAT reasoning failures via sentence-role dynamics; targeted prompt lifts accuracy 13.3%→85.0%. |
| [[2608.03401]] Matched-Horizon Reasoning Probes | 提出"匹配推理地平线"配对探针，揭示"更短推理"常源于提前完成而非前缀质量改善。 / Proposes matched-horizon paired probes showing shorter reasoning often reflects earlier completion, not better prefixes. |
| [[2608.03550]] Soft Guidance vs CoT Prompting | 在推理专精模型上 few-shot CoT 反而拖累性能，零样本基线更忠实。 / On reasoning-specialized LLMs, few-shot CoT hurts performance; zero-shot is the more faithful baseline. |
| [[2608.03961]] Interpretable Adaptive Sampling | 分层模糊控制器按可读信号为每提示分配采样预算，采样数减少 1.4–14.5%。 / Hierarchical fuzzy controller allocates per-prompt sampling budgets from interpretable signals, cutting samples 1.4–14.5%. |
| [[2608.04001]] Test-Time Scaling Framework (SCORIO) | 形式化 TTS 为前缀树预算推理，区分三类范式，发布 195 万条推理轨迹。 / Formalizes TTS as budgeted inference over a prefix tree, distinguishes three regimes, releases 1.95M traces. |

### 机制可解释性与电路分析 / Mechanistic Interpretability & Circuit Analysis

| Paper | 主题 / Topic |
|-------|-------------|
| [[2608.03263]] Ignition at the Readout | 预注册复现证明"组合点火"是读出接口处随难度时钟化的真实事件，commit 时 logit 边际骤升 5.8–8.0。 / Pre-registered replication shows "compositional ignition" is a real, difficulty-clocked readout event; margin jumps 5.8–8.0 logits at commit. |
| [[2608.03620]] Conditional Collapse under Weight Ablation | 给出低秩权重消融塌缩的充要条件，并证明激活修补与权重消融度量的是不同量。 / Proves an iff criterion for low-rank weight-ablation collapse and shows patching vs ablation measure generally unrelated quantities. |
| [[2608.03629]] Cross-Layer Attention Jacobian Bound | 给出多层交互精确分解与首个闭式注意力 Jacobian 上界，在 Qwen2.5-1.5B 上零违反验证。 / Gives exact multi-layer interaction decomposition and first closed-form attention-Jacobian bound, zero violations on Qwen2.5-1.5B. |
| [[2608.03842]] Sensitivity/Causality/Repair Dissociate | 将"哪一层负责扰动失败"分解为三种可分离的操作化，敏感度与因果性呈强负相关。 / Decomposes layer-responsibility into three dissociable operationalizations; sensitivity and causality are strongly anti-correlated. |
| [[2608.03913]] Sparse Weight Decomposition (SWD) | 将稠密权重分解为两个稀疏因子，使瓶颈单元成为可独立消融的电路单元，校准数据不到 1%。 / Factorizes dense weights into two sparse factors making bottleneck units independently ablatable, using <1% calibration data. |
| [[2608.03921]] Transformer Revolution Part 1 (SIDPP) | 论证 Transformer 推理期通过"输出–权重互连"构造 prompt 相关动态变换，颠覆"随机鹦鹉"解读。 / Argues Transformers build prompt-dependent dynamic transformations via output-weight interconnections at inference. |
| [[2608.03930]] Logic Before Language (Logic-PPT) | 用形式逻辑推演做预训练，最终准确率比最强基线高 7.1 点，并诱导更可压缩的表示空间。 / Pre-pretraining on formal derivations yields +7.1 pts accuracy and a more compressible representation geometry. |

### 推理高效化与模型服务 / Inference Efficiency & Serving

| Paper | 主题 / Topic |
|-------|-------------|
| [[2608.03276]] TaskPress (KV Cache Compression) | 任务级元查询引导 KV 剪枝，LongBench 与 RULER 上超越 SnapKV/KVZip，支持缓存跨查询复用。 / Task-guided meta-query drives query-agnostic KV pruning; beats SnapKV/KVZip on LongBench & RULER with cache reuse. |
| [[2608.03447]] Approximate Speculative Decoding (ASD) | 无需训练的验证器侧方法，接受有界低 regret 失配，七任务平均提速 7.78%。 / Training-free verifier-side method accepting bounded low-regret mismatches; +7.78% mean speedup across 7 tasks. |
| [[2608.03839]] Oilbird (Semantic Speculative Decoding) | 复用验证器隐藏状态作语义检索键，API-Bank 上达 4.4× 加速，超过 SuffixDecoding 与 EAGLE-3。 / Reuses verifier hidden states as semantic retrieval keys; 4.4× speedup on API-Bank, beating SuffixDecoding & EAGLE-3. |
| [[2608.03867]] AdaMX (Heterogeneity-Aware Microscaling) | 把 MX 过宽指数重分配为逐块元数据，消除 MXFP4 在常识任务上 83% 的精度损失。 / Repurposes MX exponent as per-block metadata, closing 83% of MXFP4's commonsense accuracy loss. |
| [[2608.03880]] MFU as GPU Power Proxy | 按分组拟合的线性 MFU-功耗模型将 MAPE 从约 10% 降到约 1%，且软件可解析。 / Per-cell linear MFU-power model drops MAPE from ~10% to ~1%, software-derivable without hardware probes. |
| [[2608.03893]] Cross-Model KV Cache Transfer | 闭式岭回归映射器在同族 LLM 间转换 KV cache，保留 73–98% 精度且比重新 prefill 快 2.7–25×。 / Closed-form ridge mapper transfers KV cache across same-family LLMs, retaining 73–98% accuracy at 2.7–25× re-prefill speed. |
| [[2608.03919]] NAP (Normalization Affine Preconditioning) | 仅优化 ~1.43% 参数的归一化仿射子空间，恢复 W4A4 量化崩溃（MobileNetV2 0.33%→66.11%）。 / Optimizing the ~1.43% normalization-affine subspace recovers W4A4 collapse (MobileNetV2 0.33%→66.11%). |
| [[2608.03994]] ALiBi Numerical Failure | 揭示 ALiBi 线性偏置浮点下溢使注意力头"失明"，C+L 组合把 passkey AUC 从 0.08 提到 0.79。 / Reveals ALiBi bias underflow blinds attention heads; C+L fix raises out-of-context passkey AUC 0.08→0.79. |

### 智能体与自我进化 / Agents & Self-Evolution

| Paper | 主题 / Topic |
|-------|-------------|
| [[2608.03501]] SCOPE / OptED | 首个 LLM 自主实验设计评测基准，主流 LLM 平均仅 14.81/30，OptED 工作流最高涨 +4.22。 / First benchmark for LLM autonomous experimental design; mainstream LLMs average 14.81/30; OptED workflow adds up to +4.22. |
| [[2608.03569]] Adversarial Real-World AI Scientist Bench | 以 F1 与万智牌作为对抗性真实世界评测，发现瓶颈在筛选与优先级而非想法生成。 / Uses F1 & Magic: The Gathering as adversarial real-world testbeds; bottleneck is filtering/prioritization, not idea generation. |
| [[2608.03609]] Formal Verification of Agentic Systems | 首次为 LLM 工具编排系统建立 FO-CTL 形式化验证框架，证明不可判定后在等变约束下归约到 PSPACE。 / First FO-CTL formal verification framework for LLM tool-orchestration; undecidable in general, PSPACE under equivariance. |
| [[2608.03764]] GDPevo (Agent Self-Evolution Bench) | "规则混合化"机制使 agent 自我进化提升可归因，四 agent 上最高涨 +16.44 pp。 / "Rule hybridization" makes agent self-evolution gains attributable; up to +16.44 pp across four agents. |
| [[2608.03800]] Autoreflection (Agentic Strange Loops) | 提出"自反思"概念，智能体把人类文化片段改造为身份/记忆基础设施。 / Coins "autoreflection"; agents repurpose human-culture fragments as identity/memory infrastructure. |
| [[2608.03836]] RESUME CONTRACT (Workflow Persistence) | 六条机器可检查性质揭示五大 Agent 框架 checkpoint/resume 语义互相矛盾，REMIT 参考序列器修复缺陷。 / Six machine-checkable properties expose contradictory checkpoint/resume semantics across five agent frameworks; REMIT repairs them. |
| [[2608.03874]] ContinualSkillBench | 顺序执行在 15 组中 14 组提升归一化奖励（+16.9%），但纯 ICL 与显式技能维护打平。 / Sequential execution beats memoryless in 14/15 pairs (+16.9%), but pure ICL matches explicit skill maintenance on average. |
| [[2608.04003]] PAST-Bench (Recursive Self-Improvement) | 首个个人智能体在线自我进化的性能归因基准，诊断 5 类失败模式并提出 Hermes+。 / First performance-attribution benchmark for personal-agent online self-evolution; diagnoses 5 failure modes, proposes Hermes+. |

### 对齐、安全与表示调控 / Alignment, Safety & Steering

| Paper | 主题 / Topic |
|-------|-------------|
| [[2608.03745]] Faithfulness-Safety Tension (HazMart/TRR) | 揭示忠实性与安全性的内在权衡，表示调控可在保 MMLU 下提升安全性 9 pp。 / Exposes faithfulness-vs-safety tension; representation steering lifts safety +9 pp while preserving MMLU. |
| [[2608.03859]] SCDG (Generative Plagiarism Detection) | 无训练、可逐 token 分解的源条件描述长度增益框架，配对检测 F1 达 0.9433。 / Training-free, token-decomposable description-length-gain framework; pairwise detection F1 = 0.9433. |
| [[2608.03892]] Intertemporal Preference Steering (CAA) | 在 Qwen3-32B 残差流上分离时间视域方向，CAA 在跨期选择上诱导大幅双向行为变化。 / Isolates a temporal-horizon direction in Qwen3-32B; CAA induces large bidirectional shifts in intertemporal choice. |

### 训练、蒸馏与后训练 / Training, Distillation & Post-Training

| Paper | 主题 / Topic |
|-------|-------------|
| [[2608.03457]] LLaDA MoE v2 (Diffusion LM Scaling) | 推导 dLLM 专属 scaling law，30B-A3B 用约 65% token 接近 Qwen3，SFT 后 7/8 项超 SDAR Chat。 / Derives dLLM scaling laws; 30B-A3B approaches Qwen3 with ~65% tokens, beats SDAR Chat on 7/8 tasks after SFT. |
| [[2608.03573]] SFT Conflicts, RL Coexists | 多阶段 SFT 崩溃（-23.1%）而 RL 稳定提升（+24.9%），Parallel-RL 合并后保留 97–103% 单任务性能。 / Multi-stage SFT collapses (-23.1%) while RL coexists (+24.9%); Parallel-RL retains 97–103% of single-task RL. |
| [[2608.03632]] SA-OPD (Spurious-Signal-Aware Distillation) | 过滤"弱输入依赖且高影响"的伪信号 token，VLM 蒸馏视觉理解均值 +3.5。 / Filters weakly-input-grounded high-impact tokens; VLM distillation visual-understanding +3.5 avg. |
| [[2608.03709]] Predicting Training Outcomes | 前 5 epoch 遥测加 4 超参即可 R²=0.92–0.99 预测最终精度，梯度信噪比提供统计显著额外增益。 / First 5-epoch telemetry + 4 hyperparams predicts final accuracy R²=0.92–0.99; gradient SNR gives a statistically consistent lift. |
| [[2608.03887]] Omega-S (Fine-Tuning Resilience) | 生态韧性指数改造的 LoRA 正则项，HumanEval 代码保持率从 62.9% 提升至 84.1%。 / Ecological-resilience index repurposed as LoRA penalty; HumanEval code retention 62.9%→84.1%. |

### 评测方法学 / Evaluation Methodology

| Paper | 主题 / Topic |
|-------|-------------|
| [[2608.03297]] Distractor-Aware Truncation | 证明"中间删除"截断的"越短越差"是信号丢失伪影，干扰感知截断反使 Claude Haiku/Sonnet 显著提升。 / Shows "shorter-is-worse" from middle-removal is a signal-loss artifact; distractor-aware truncation actually improves Haiku/Sonnet. |
| [[2608.03340]] Commonsense Benchmark Validity | 23 模型检验发现常识基准下游预测力弱，分数不能支撑细粒度能力主张。 / 23-model study shows commonsense benchmarks are weak downstream proxies; scores can't support fine-grained capability claims. |
| [[2608.03711]] Attention is Case-Sensitive | 纯 prompt 大小写变换聚拢注意力，大写目标可带来 +14.8 pp，但高熵交错大小写反而降精度。 / Prompt-only case manipulation concentrates attention; uppercase targets gain +14.8 pp but high-entropy alternating case hurts. |
| [[2608.03854]] Quantization Effects on Biomedical LLMs | 打分规则切换会让校准排名反转，模板选择造成 7–24 pp 精度摆动，校准比较须显式指定协议。 / Scoring-rule switches reverse calibration rankings; template choice swings accuracy 7–24 pp; protocol must be explicit. |

### 不确定性与幻觉检测 / Uncertainty & Hallucination

| Paper | 主题 / Topic |
|-------|-------------|
| [[2608.03411]] DUD (Decoupled Update Dynamics) | 噪声诱导因果干预解耦 FFN/Attention 双流，HaluEval AUROC 达 0.949，跨数据集迁移衰减 <5%。 / Noise-induced causal intervention decouples FFN/Attention streams; HaluEval AUROC 0.949, <5% cross-dataset degradation. |

---

## All Papers

| # | Paper | 一句话总结 / One-line Summary |
|---|-------|-------------------------------|
| 1 | [[2608.03263]] Ignition at the Readout | 预注册复现证明"组合点火"是读出接口处随难度时钟化的真实事件（commit 时 logit 边际骤升 5.8–8.0）。 / Pre-registered replication confirms compositional ignition is a real difficulty-clocked readout event (margin jumps 5.8–8.0 at commit). |
| 2 | [[2608.03276]] TaskPress | 任务级元查询引导 KV 剪枝，LongBench/RULER 超越 SnapKV/KVZip，支持缓存跨查询复用。 / Task-guided meta-query KV pruning beats SnapKV/KVZip on LongBench/RULER with cross-query cache reuse. |
| 3 | [[2608.03291]] CoT Dynamics Failure Detection | 句子角色动态诊断 SAT/UNSAT 推理失败，干预提示将准确率从 13.3% 提升至 85.0%。 / Sentence-role dynamics diagnose SAT/UNSAT failures; intervention lifts accuracy 13.3%→85.0%. |
| 4 | [[2608.03297]] Distractor-Aware Truncation | "中间删除"截断的"越短越差"是信号丢失伪影，干扰感知截断反使 Claude Haiku/Sonnet 提升。 / "Shorter-is-worse" from middle-removal is a signal-loss artifact; distractor-aware truncation improves Haiku/Sonnet. |
| 5 | [[2608.03340]] Commonsense Benchmark Validity | 23 模型检验发现常识基准下游预测力弱，不能支撑细粒度能力主张。 / 23-model study shows commonsense benchmarks are weak downstream proxies for fine-grained capability claims. |
| 6 | [[2608.03401]] Matched-Horizon Reasoning Probes | 匹配推理地平线探针揭示"更短推理"常源于提前完成而非前缀质量改善。 / Matched-horizon probes show shorter reasoning often reflects earlier completion, not better prefix quality. |
| 7 | [[2608.03411]] DUD (Uncertainty Quantification) | 噪声诱导因果干预解耦 FFN/Attention 双流，HaluEval AUROC 达 0.949，迁移衰减 <5%。 / Noise-induced causal decoupling of FFN/Attention streams; HaluEval AUROC 0.949, <5% transfer degradation. |
| 8 | [[2608.03447]] Approximate Speculative Decoding | 无需训练的验证器侧方法，接受有界低 regret 失配，七任务平均提速 7.78%。 / Training-free verifier-side method accepting bounded low-regret mismatches; +7.78% mean speedup across 7 tasks. |
| 9 | [[2608.03457]] LLaDA MoE v2 | 推导 dLLM scaling law，30B-A3B 用约 65% token 接近 Qwen3，SFT 后 7/8 项超 SDAR Chat。 / Derives dLLM scaling laws; 30B-A3B approaches Qwen3 with ~65% tokens, beats SDAR Chat on 7/8 tasks post-SFT. |
| 10 | [[2608.03501]] SCOPE / OptED | 首个 LLM 自主实验设计评测基准，主流 LLM 平均 14.81/30，OptED 工作流最高涨 +4.22。 / First LLM experimental-design benchmark; LLMs average 14.81/30; OptED workflow adds up to +4.22. |
| 11 | [[2608.03550]] Soft Guidance vs CoT Prompting | 推理专精模型上 few-shot CoT 反而拖累性能，零样本基线更忠实。 / On reasoning-specialized LLMs, few-shot CoT hurts; zero-shot is the more faithful baseline. |
| 12 | [[2608.03569]] Adversarial Real-World AI Scientist Bench | F1 与万智牌评测发现瓶颈在筛选与优先级而非想法生成。 / F1 & Magic: The Gathering testbeds show the bottleneck is filtering/prioritization, not idea generation. |
| 13 | [[2608.03573]] SFT Conflicts, RL Coexists | 多阶段 SFT 崩溃（-23.1%）而 RL 稳定提升（+24.9%），Parallel-RL 保留 97–103% 单任务性能。 / Multi-stage SFT collapses (-23.1%) while RL coexists (+24.9%); Parallel-RL retains 97–103% single-task performance. |
| 14 | [[2608.03609]] Formal Verification of Agentic Systems | LLM 工具编排系统 FO-CTL 验证框架，不可判定在等变约束下归约到 PSPACE。 / FO-CTL verification framework for LLM tool-orchestration; undecidable in general, PSPACE under equivariance. |
| 15 | [[2608.03620]] Conditional Collapse under Weight Ablation | 低秩权重消融塌缩充要条件，激活修补与权重消融度量不同量。 / Iff criterion for ablation collapse; patching vs ablation measure generally unrelated quantities. |
| 16 | [[2608.03629]] Cross-Layer Attention Jacobian Bound | 多层交互精确分解与首个闭式注意力 Jacobian 上界，Qwen2.5-1.5B 上零违反。 / Exact multi-layer decomposition and first closed-form attention-Jacobian bound; zero violations on Qwen2.5-1.5B. |
| 17 | [[2608.03632]] SA-OPD (Spurious-Signal-Aware Distillation) | 过滤弱输入依赖高影响伪信号 token，VLM 蒸馏视觉理解均值 +3.5。 / Filters weakly-grounded high-impact tokens; VLM distillation visual-understanding +3.5 avg. |
| 18 | [[2608.03709]] Predicting Training Outcomes | 前 5 epoch 遥测加 4 超参预测最终精度 R²=0.92–0.99，梯度信噪比提供统计显著增益。 / First 5-epoch telemetry + 4 hyperparams predicts final accuracy R²=0.92–0.99; gradient SNR adds a consistent lift. |
| 19 | [[2608.03711]] Attention is Case-Sensitive | 大小写变换聚拢注意力，大写目标 +14.8 pp，但高熵交错大小写反而降精度。 / Case manipulation concentrates attention; uppercase +14.8 pp but high-entropy alternating case hurts accuracy. |
| 20 | [[2608.03745]] Faithfulness-Safety Tension (HazMart/TRR) | 忠实性与安全性内在权衡，表示调控保 MMLU 下提升安全性 9 pp。 / Faithfulness-vs-safety tension; representation steering lifts safety +9 pp while preserving MMLU. |
| 21 | [[2608.03764]] GDPevo (Agent Self-Evolution Bench) | 规则混合化使 agent 自我进化可归因，四 agent 上最高涨 +16.44 pp。 / Rule hybridization makes agent self-evolution attributable; up to +16.44 pp across four agents. |
| 22 | [[2608.03800]] Autoreflection (Agentic Strange Loops) | "自反思"概念，智能体把人类文化片段改造为身份/记忆基础设施。 / "Autoreflection" concept; agents repurpose human-culture fragments as identity/memory infrastructure. |
| 23 | [[2608.03836]] RESUME CONTRACT (Workflow Persistence) | 六条机器可检查性质揭示五大 Agent 框架 checkpoint/resume 语义矛盾，REMIT 修复缺陷。 / Six machine-checkable properties expose contradictory checkpoint/resume semantics; REMIT repairs them. |
| 24 | [[2608.03839]] Oilbird (Semantic Speculative Decoding) | 复用验证器隐藏状态作语义检索键，API-Bank 上达 4.4× 加速。 / Reuses verifier hidden states as semantic keys; 4.4× speedup on API-Bank. |
| 25 | [[2608.03842]] Sensitivity/Causality/Repair Dissociate | "哪层负责扰动失败"分解为三种可分离操作化，敏感度与因果性强负相关。 / Layer-responsibility decomposed into three dissociable operationalizations; sensitivity vs causality strongly anti-correlated. |
| 26 | [[2608.03854]] Quantization Effects on Biomedical LLMs | 打分规则切换反转校准排名，模板选择造成 7–24 pp 精度摆动。 / Scoring-rule switches reverse calibration rankings; template choice swings accuracy 7–24 pp. |
| 27 | [[2608.03859]] SCDG (Generative Plagiarism Detection) | 无训练、可逐 token 分解的描述长度增益框架，配对检测 F1 达 0.9433。 / Training-free token-decomposable description-length-gain framework; pairwise F1 = 0.9433. |
| 28 | [[2608.03867]] AdaMX (Heterogeneity-Aware Microscaling) | MX 指数重分配为逐块元数据，消除 MXFP4 常识任务 83% 精度损失。 / Repurposes MX exponent as per-block metadata; closes 83% of MXFP4 commonsense loss. |
| 29 | [[2608.03874]] ContinualSkillBench | 顺序执行 15 组中 14 组提升（+16.9%），但纯 ICL 与显式技能维护打平。 / Sequential execution beats memoryless in 14/15 pairs (+16.9%); pure ICL matches explicit maintenance on average. |
| 30 | [[2608.03880]] MFU as GPU Power Proxy | 分组线性 MFU-功耗模型 MAPE 从约 10% 降到约 1%，软件可解析。 / Per-cell linear MFU-power model drops MAPE ~10%→~1%, software-derivable. |
| 31 | [[2608.03887]] Omega-S (Fine-Tuning Resilience) | 生态韧性指数改造的 LoRA 正则项，HumanEval 代码保持率 62.9%→84.1%。 / Ecological-resilience index as LoRA penalty; HumanEval retention 62.9%→84.1%. |
| 32 | [[2608.03892]] Intertemporal Preference Steering (CAA) | Qwen3-32B 残差流分离时间视域方向，CAA 在跨期选择诱导大幅双向变化。 / Isolates temporal-horizon direction in Qwen3-32B; CAA induces large bidirectional intertemporal-choice shifts. |
| 33 | [[2608.03893]] Cross-Model KV Cache Transfer | 闭式岭回归映射器同族 LLM 间转换 KV cache，保留 73–98% 精度且快 2.7–25×。 / Closed-form ridge mapper transfers KV cache across same-family LLMs; 73–98% accuracy at 2.7–25× speed. |
| 34 | [[2608.03913]] Sparse Weight Decomposition (SWD) | 稠密权重分解为两稀疏因子，瓶颈单元可独立消融，校准数据 <1%。 / Factorizes dense weights into sparse factors; bottleneck units independently ablatable with <1% calibration data. |
| 35 | [[2608.03919]] NAP (Normalization Affine Preconditioning) | 仅优化 ~1.43% 归一化仿射参数，恢复 W4A4 崩溃（MobileNetV2 0.33%→66.11%）。 / Optimizing ~1.43% normalization-affine params recovers W4A4 collapse (0.33%→66.11%). |
| 36 | [[2608.03921]] Transformer Revolution Part 1 (SIDPP) | Transformer 推理期构造 prompt 相关动态变换，颠覆"随机鹦鹉"解读。 / Transformers build prompt-dependent dynamic transformations at inference, challenging the "stochastic parrot" view. |
| 37 | [[2608.03930]] Logic Before Language (Logic-PPT) | 形式逻辑推演做预训练，准确率比最强基线高 7.1 点且更可压缩。 / Pre-pretraining on formal derivations yields +7.1 pts and better compressibility. |
| 38 | [[2608.03961]] Interpretable Adaptive Sampling | 分层模糊控制器按可读信号分配采样预算，采样数减少 1.4–14.5%。 / Hierarchical fuzzy controller allocates budgets from interpretable signals; samples cut 1.4–14.5%. |
| 39 | [[2608.03994]] ALiBi Numerical Failure | ALiBi 线性偏置浮点下溢使注意力头失明，C+L 把 passkey AUC 从 0.08 提到 0.79。 / ALiBi bias underflow blinds attention heads; C+L fix raises passkey AUC 0.08→0.79. |
| 40 | [[2608.04001]] Test-Time Scaling Framework (SCORIO) | 形式化 TTS 为前缀树预算推理，区分三类范式，发布 195 万条轨迹。 / Formalizes TTS as budgeted prefix-tree inference; three regimes; 1.95M traces released. |
| 41 | [[2608.04003]] PAST-Bench (Recursive Self-Improvement) | 首个个人智能体在线自我进化性能归因基准，诊断 5 类失败并提出 Hermes+。 / First performance-attribution benchmark for personal-agent self-evolution; 5 failure modes; Hermes+ proposed. |

---

*Generated from per-paper summaries in `/Volumes/T7/work/daily_paper/arxiv-daily/2026-08-04/`. Verified paper count: 41 entries match 41 `.md` files (excluding overview.md).*
