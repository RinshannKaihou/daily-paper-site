---
title: "Daily Paper Overview - 2026-06-04"
date: 2026-06-04
tags: [daily-overview, arxiv, llm, ai]
papers: 50
---

# Daily Paper Overview — 2026-06-04

## 今日必读 / Must Read Today

### 1. [[2606.05403]] Trust, but Don't Verify: Epistemic Blind Spots in LLM Source Evaluation

**一句话总结：** LLM 在多源量化合成中具备孤立检测伪造统计的能力（CIR 0.76–1.00），却由 **methodology-register gate** 按「分析文体」而非数值有效性加权来源；不可能 CI 与有效 CI 的 SPI 几乎相同（伪造数字恢复约 **79%** 有效数字的拉力），线性探针与 ROME 因果追踪一致，且提示甚至 oracle checklist 只能产生 blanket skepticism 而非选择性甄别。

**TL;DR:** Amazon authors test 5 models (Claude Haiku/Sonnet/Opus 4.5, Qwen 32B, OLMo 3.1 Think) synthesizing conflicting estimates from 4-source workplace threads across VC/MKT/PH (>1M trials). Isolation: CIR high for specious methodology; numerics follow domain gradient (VC CI near-universal). Synthesis: impossible stats ≈ valid stats (SPI); specious jargon ≈ bare claim. Mechanism: cross-domain methodology probes AUC 0.83–0.92 (L8), numerics at chance; isolation separability 0.87→0.52 in synthesis; ROME/DLA show consensus-gated presentation tokens, no numerics correction (r=0.78). Prompting fails selective discernment. Term **epistemic alignment**: deploy evaluation capability, not just possess it—distinct from user sycophancy.

**为何必读 / Why read:** 超过百万次试验揭示「能检测却不用」的认知对齐盲区，对 RAG、多源分析与高风险决策系统有直接警示意义。 / Over 1M trials show models detect bad sources in isolation but deploy methodology-register heuristics in synthesis—critical for RAG, multi-source analytics, and high-stakes decision pipelines.

---

### 2. [[2606.06188]] The Tell-Tale Norm: ℓ₂ Magnitude as a Signal for Reasoning Dynamics in Large Language Models

**一句话总结：** 北大/浙大团队用逐层 SAE 揭示 LLM 推理集中在**后 25% 层**且与 hidden state **ℓ₂ 范数**同步飙升；理论上证明 ℓ₂ 双向界住 SAE 推理特征激活，因果抑制高范数状态会严重损伤推理；据此提出三种**无需训练/数据**的测试时方法——ALRR（层内递归精炼）、ERSS（内生状态引导）、LRS（ℓ₂ 重排序）——在 Qwen3 与 R1-Distill-Llama 七模型、七基准上平均 **+4.51%**，难题（AIME 等）**+9.13%**；代码开源。

**TL;DR:** LLM reasoning lacks a principled, model-intrinsic layer-wise signal. This paper shows **ℓ₂ norm of hidden states** tracks reasoning intensity: SAE probes reveal reasoning features spike in **late ~25% layers**, mirroring ℓ₂ trends. **Theorem 1** bounds SAE reasoning-feature activation by observable ℓ₂ expansion. **Three training-free test-time methods:** ALRR, ERSS, LRS—**+4.51%** avg across seven models/benchmarks, **+9.13%** on hard tasks (AIME). Code released.

**为何必读 / Why read:** 用可观测 ℓ₂ 范数替代昂贵 SAE 探测，并提供即插即用的测试时推理增强，工程落地价值高。 / Observable ℓ₂ norm substitutes for costly SAE probes and enables plug-and-play test-time reasoning gains with strong empirical gains.

---

### 3. [[2606.05644]] FIDES: Faithful Inference via Deep Evidence Signals for Retrieval-Memory Conflict in RAG

**一句话总结：** 浙大滨江研究院/浙大/GenTel.io/广师大团队提出 **FIDES**——无需训练的 RAG 解码器：在检索证据与参数记忆冲突时，用 **Opposition（输出 JSD）+ Shift（跨层隐状态 ℓ₂）+ Noise（中点→末层 Logit-Lens KL）** 三信号融合为逐步 **α_t**，将对比解码从「全局压多少」转为「**在哪些 token 压**」；在 NQ-Swap / PopQA / TriviaQA 三基准、四款 7B/8B 骨干上 **12/12 设定 CF 最优**，较最强同预算无训练基线 AdaCAD **+3~+13**、较 Standard RAG **+14~+28**；70B 上 CF **92–94%**、F1 **62–63%**，答案 token 平均 α 为功能词 **3.3×**（AUROC **0.923**）。

**TL;DR:** When retrieved context contradicts parametric memory, **FIDES** fuses Opposition (JSD), Shift (layer ℓ₂), and Noise (Logit-Lens KL) into token-specific **α_t** for contrastive decoding—**12/12** best context-fidelity settings, **+3~+13** over AdaCAD, **+14~+28** over standard RAG; 70B CF **92–94%**, answer-token α AUROC **0.923**. Training-free.

**为何必读 / Why read:** 将 RAG 冲突消解从全局对比权重推进到 token 级深度证据信号，在多个基准上全面领先且无训练成本。 / Moves RAG conflict resolution from global contrast weights to per-token deep evidence signals with SOTA, training-free gains across benchmarks.

---

## 按主题分类 / Papers by Topic

### 大模型推理、机制分析与可解释性 / LLM Reasoning, Mechanisms & Interpretability

| Paper | Summary (Chinese / English) |
|-------|-----------------------------|
| [[2606.05173]] Predict and Reconstruct: Joint Objectives for Self-Supervised Language Representation Learning | 共享编码器上联合 JEPA 预测与 MLM 重建，嵌入更均匀、谱几何更丰富，GLUE 线性探测几乎持平。 / Hybrid JEPA+MLM encoder yields more uniform embeddings and richer spectral geometry with near-flat GLUE linear-probe accuracy. |
| [[2606.05194]] Temporal Preference Concepts and their Functions in a Large Language Model | 在 Qwen3-4B 上因果定位 L17–L35 时间偏好子图；CAA 引导可将长/短期偏好赔率提升约 3.4×。 / Causal localization of temporal-preference subgraph (L17–L35) in Qwen3-4B; CAA steering boosts long/short preference odds ~3.4×. |
| [[2606.05219]] Gradient Descent with Large Step Size Restores Symmetry in Deep Linear Networks with Multi-Pathway | 大学习率在 Edge of Stability 上逆转「赢家通吃」，偏好跨通路共享表征而非持久单通路主导。 / Large-step GD at EoS reverses winner-take-all symmetry breaking, favoring shared multi-pathway representations. |
| [[2606.05326]] Gradient descent at the Edge of Stability: free energy model and kinetic description of the two-layer network | EoS 下提出耦合 θ 与 Σ 的有效自由能模型，两层网络动能方程可解释为 W₂ 梯度流。 / Slow–fast EoS model with effective free energy F(θ,Σ); two-layer kinetic equation as W₂ gradient flow. |
| [[2606.05346]] Trajectory Dynamics in Language Model Hidden States Predict Human Processing Costs Beyond Surprisal | 「轨迹外推误差」与 surprisal 近乎正交，却能独立预测 Natural Stories 阅读时间。 / Trajectory extrapolation error is near-orthogonal to surprisal yet predicts human reading times on Natural Stories. |
| [[2606.05378]] Pattern Selectivity is Not Task-Causal Structure: A Cross-Architecture Mechanistic Study of Composed-Task Circuits in 1B-Class Language Models | 1B 级模型上组合任务因果电路跨架构完全不同；提出五类筛选分类学与 MoE prev-token 假说。 / Composed-task causal circuits differ across 1B architectures; five-class screening taxonomy and falsifiable MoE prev-token hypothesis. |
| [[2606.05402]] ReasoningFlow: Discourse Structures for Understanding LLM Reasoning Traces | 将 LRM 推理轨迹标注为子句级 DAG（8 节点、14 边），扩展至 1,260 条轨迹；约 85% 错误步骤不因果影响最终答案。 / Sub-clause DAG annotation of LRM traces (1,260 traces); ~85% error steps do not causally affect final answers. |
| [[2606.05486]] Localizing Prompt Ambiguity in Large Language Models with Probe-Targeted Attribution | PRIG 将潜藏 prompt 歧义定位到 token/句子级，合成数据 AUROC **0.840**，人类 gold **0.891**。 / PRIG localizes latent prompt ambiguity to token/sentence level—AUROC 0.840 synthetic, 0.891 human gold. |
| [[2606.05616]] What's in a Name? Morphological Shortcuts by LLMs in Pharmacology | LLM 仅凭 INN 词缀即可对虚构药名产生与真药同等级别的药理推断；激活修补定位早期–中层。 / LLMs infer pharmacology from INN affixes alone on fictitious drug names; activation patching localizes early–mid layers. |
| [[2606.05843]] Mechanistic Insights into Functional Sparsity in Multimodal LLMs via CoRe Heads | 约 5% CoRe 头因果不可或缺；头级混合稀疏注意力 prefill **1.8–2.3×** 加速且性能不降。 / ~5% CoRe heads are causally essential; head-level sparse attention yields 1.8–2.3× prefill speedup with minimal quality loss. |
| [[2606.05957]] Dead Directions: Geometric Singular Learning | 用 Fisher 退化「死方向」统一 Watanabe 奇异学习与 Amari 信息几何，单次 checkpoint 即可读轨迹速率。 / Fisher-degenerate "dead directions" unify singular learning theory and information geometry with single-checkpoint rate readouts. |
| [[2606.06188]] The Tell-Tale Norm: ℓ₂ Magnitude as a Signal for Reasoning Dynamics in Large Language Models | ℓ₂ 范数追踪推理强度；ALRR/ERSS/LRS 七模型七基准平均 **+4.51%**。 / ℓ₂ norm tracks reasoning intensity; training-free ALRR/ERSS/LRS average +4.51% across seven models/benchmarks. |
| [[2606.06238]] Generative Criticality in Large Language Model Temperature Scaling | token 嵌入统计场框架下 T_c≈1.4 处 χ 幂律发散，低 T 输出坍缩到单一语义方向。 / Statistical-field framework: susceptibility peak at T_c≈1.4; low-T semantic directional collapse in Qwen3 0.6B–32B. |
| [[2606.06333]] Subspace-Aware Sparse Autoencoders for Effective Mechanistic Interpretability | SASA 用块级子空间解码解决 feature splitting；约一半 token 预算匹配或超越标准 SAE。 / SASA block subspace decoders fix feature splitting; ~half token budget matches or beats standard SAEs on GPT-2/Mistral-7B. |

### RAG、记忆与智能体系统 / RAG, Memory & Agent Systems

| Paper | Summary (Chinese / English) |
|-------|-----------------------------|
| [[2606.04037]] Toward Pre-Deployment Assurance for Enterprise AI Agents: Ontology-Grounded Simulation and Trust Certification | 企业 Agent 部署前验证：本体驱动场景生成 + Trust Certificate；监管覆盖率 G4 显著优于 persona 基线。 / Pre-deployment enterprise-agent assurance with ontology-grounded scenarios and graduated Trust Certificates. |
| [[2606.05182]] LANTERN: Layered Archival and Temporal Episodic Retrieval Network for Long-Context LLM Conversations | 零 LLM 调用主动归档 + RRF 四路检索，恢复 **78.3%** 被压缩丢失事实，优于 MemGPT-Faithful。 / Zero-LLM archival + RRF hybrid retrieval recovers 78.3% compaction-lost facts, beating MemGPT-Faithful. |
| [[2606.05233]] Domain-Conditioned Safety in Frontier Computer-Using Agents: A 793-Episode Browser Benchmark, a Coding-Domain Cross-Reference, and a Reproducibility Audit of Recent Red-Teaming | CUA-HandCrafted 793 集基准：前沿 CUA 浏览器 ASR **0/140**，但 SkillBench 编码注入可达 **100%**。 / 793-episode CUA benchmark: 0/140 browser ASR on frontier models but up to 100% coding skill injection—domain-conditioned safety. |
| [[2606.05241]] Search-Time Contamination in Deep Research Agents: Measuring Performance Inflation in Public Benchmark Evaluation | 定义搜索时污染（STC）三级分类；医学 QA 上 STC 普遍，HLE 子集性能可虚高约 4%。 / Search-Time Contamination taxonomy for deep-research agents; up to ~4% benchmark score inflation from web retrieval. |
| [[2606.05339]] A Taxonomy of Runtime Faults in Model Context Protocol Servers | 首份 MCP 服务端运行时故障分类：837 线程 → **11 类 / 27 子类 / 73 叶节点**。 / First empirical MCP server runtime-fault taxonomy from 837 threads into 11 top-level, 27 sub-, 73 leaf categories. |
| [[2606.05557]] AURA: Intent-Directed Probing for Implicit-Need Surfacing in Situated LLM Agents | IntentFrame + gap 路由探测预算；隐含需求覆盖率 **+0.07**，事实查询探测减少 **82%**。 / IntentFrame gap-routed probing: +0.07 implicit-need coverage, 82% fewer probes on factual queries. |
| [[2606.05644]] FIDES: Faithful Inference via Deep Evidence Signals for Retrieval-Memory Conflict in RAG | 三深度证据信号 token 级对比解码；**12/12** CF 最优，较 AdaCAD **+3~+13**。 / Token-level FIDES contrastive decoding from three deep evidence signals—12/12 best CF, +3–13 over AdaCAD. |
| [[2606.05711]] Beyond tokens: a unified framework for latent communication in LLM-based multi-agent systems | WHAT/WHICH/HOW 三轴统一 **18** 种潜空间多智能体通信方法（2024–2026）综述。 / WHAT/WHICH/HOW framework surveying 18 latent multi-agent communication methods (2024–2026). |
| [[2606.06223]] From Reward-Hack Activations to Agentic Risk States: Context-Calibrated Mechanistic Monitoring in LLM Agents | 将 reward-hack 激活监测迁移到 ReAct 循环，结合熵与上下文做下一步风险估计。 / Reward-hack activation monitoring extended to ReAct agents with context-calibrated next-step risk estimation. |

### 安全、评估与可信 AI / Safety, Evaluation & Trustworthy AI

| Paper | Summary (Chinese / English) |
|-------|-----------------------------|
| [[2606.05170]] ERRORQUAKE: Heavy-Tailed Error Severity Distributions in Open-Weight Large Language Models | ERRORQUAKE-10K 用 Gutenberg–Richter *b* 指数刻画错误严重度尾分布；准确率相近模型 *b* 仍可显著不同。 / ERRORQUAKE-10K uses Gutenberg–Richter *b* for error-severity tails—models with similar accuracy can differ in *b*. |
| [[2606.05183]] The Granularity Gap: A Multi-Dimensional Longitudinal Audit of Sycophancy in Gemini Models | 二元 Challenge Rate 仅解释 29% 谄媚方差；**94%** 中度案例被二元过滤器漏检。 / Binary challenge rate explains only 29% of sycophancy variance; 94% of moderate cases missed by binary filters. |
| [[2606.05290]] Do Models Share Safety Representations? Cross-Model Steering for Safe Visual Generation | 源 LLM 安全方向经良性对齐迁移至文生图/视频，目标侧无需不安全数据即可降 ASR。 / Cross-model safety steering from source LLM to T2I/T2V via benign-only alignment—ASR drops without unsafe target data. |
| [[2606.05308]] Statistically Reliable LLM-Based Ranking Evaluation via Prediction-Powered Inference | PRECISE 将 PPI++ 扩展到排序指标，少量人工标注校正 LLM 评判系统性偏差。 / PRECISE extends prediction-powered inference to ranking metrics with unbiased, lower-variance Precision@K estimates. |
| [[2606.05384]] Stability vs. Manipulability: Evaluating Robustness Under Post-Decision Interaction in LLM Judges | 决策后对话挑战下近半数 LLM 评判偏好可翻转；提出 ERS 量化交互鲁棒性。 / Post-decision challenge flips ~49% of LLM-judge preferences; Evaluation Robustness Score (ERS) quantifies manipulability. |
| [[2606.05403]] Trust, but Don't Verify: Epistemic Blind Spots in LLM Source Evaluation | 方法论文体门使不可能统计与有效统计 SPI 几乎相同；提出 epistemic alignment。 / Methodology-register gate weights sources by analytical register, not numeric validity—epistemic alignment needed. |
| [[2606.05433]] Zero knowledge verification for frontier AI training is possible | 预提交 arch_spec + 网络锚点 + Merkle 承诺 + BF16/FP32 zkVM，训练验证开销估个位数百分比。 / Deployable ZK training verification with arch_spec, network anchors, Merkle commitments, native BF16/FP32 zkVM—~2–10% overhead. |
| [[2606.05799]] CaliDist: Calibrating Large Language Models via Behavioral Robustness to Distraction | 分心鲁棒性后验校准：七基准六模型 ECE 从 **23%** 降至 **7%**。 / Distraction-robust post-hoc calibration cuts average ECE from ~23% to ~7% across seven NLU benchmarks. |
| [[2606.05817]] Consistency Training Along the Transformer Stack | MLPCT/AttCT 沿 Transformer 栈一致性训练；六类威胁上表征级与轨迹级方法互补。 / MLPCT/AttCT stack-level consistency training across six threat families—complementary activation vs. trajectory targets. |
| [[2606.05874]] Evaluating Stochastic Collapse and Implicit Bias in Multimodal Large Language Models | RandomBench 揭示 MLLM「请随机选择」下的 Stochastic Collapse 与能力–一致性悖论。 / RandomBench exposes stochastic collapse and capability–consistency paradox under logic-neutral random-choice probes. |
| [[2606.05958]] Steering Vectors are an Adversarial Attack Surface | 仅替换 4–6% 词元的隐身投毒可使共享 steering 向量越狱成功率达 20–55%。 / Stealth poisoning of 4–6% tokens in shared steering datasets raises jailbreak ASR to 20–55%. |

### 训练优化、压缩与效率 / Training, Compression & Efficiency

| Paper | Summary (Chinese / English) |
|-------|-----------------------------|
| [[2606.04032]] Do Transformers Need Three Projections? Systematic Study of QKV Variants | **Q-K=V** 削减 **50%** KV cache，困惑度仅 **+3.1%**（300M）；与 GQA/MQA 正交叠加。 / Q-K=V halves KV cache with +3.1% perplexity (300M); stacks orthogonally with GQA/MQA for up to 96.9% cache reduction. |
| [[2606.04560]] Rollout-Level Advantage-Prioritized Experience Replay for GRPO | GRPO rollout 级经验回放：五套数学基准平均 **+4.35 pp**，4B 上 pass@k 增益最大。 / Rollout-level advantage-prioritized replay for GRPO—+4.35 pp average on five math benchmarks, largest at 4B. |
| [[2606.05168]] Epidemiology of Model Collapse: Modeling Synthetic Data Contamination via Bilayer SIR Dynamics | 双层 SIR 模型 R₀>1 超临界；合成文本检测 γ_D 为最高杠杆参数。 / Bilayer SIR model collapse epidemiology: R₀>1 supercritical; synthetic-text detection γ_D is highest-leverage parameter. |
| [[2606.05429]] Minimizing the Hidden Cost of Scales: Graph-Guided Ultra-Low-Bit Quantization for Large Language Models | SAGE-PTQ 将隐藏 scale 开销压至约 **0.004 bit/权重**；LLaMA-2-70B 解码约快 **1.5×**。 / SAGE-PTQ cuts hidden scale overhead to ~0.004 bit/weight; ~1.5× decode speedup on LLaMA-2-70B. |
| [[2606.05610]] Predictable Scaling Laws of Optimal Hyperparameters for LLM Continued Pre-training | CPT 最优 LR/BS 幂律缩放 + 等效预训练算力 C_pre；节省 **73–92%** 搜索算力。 / CPT hyperparameter scaling laws with equivalent pre-training compute C_pre—73–92% less search compute. |
| [[2606.05682]] Beyond Output Matching: Preserving Internal Geometry in NVFP4 LLM Distillation | CKA-QAD 在 top-k KL 外对齐 decoder Gram 结构，恢复 NVFP4 蒸馏内部几何与下游精度。 / CKA-QAD aligns decoder Gram geometry beyond KL in NVFP4 QAD—restores internal geometry and downstream accuracy. |
| [[2606.05688]] Value-and-Structure Alignment for Routing-Consistent Quantization of Mixture-of-Experts Models | VSRAQ 联合数值与路由结构对齐，Solar-100B/Nemotron-Nano 上优于纯重建 PTQ。 / VSRAQ value+structure alignment for routing-consistent MoE PTQ—beats reconstruction-only baselines. |
| [[2606.05861]] LLMCodec: Adapting Video Codecs for Efficient Weight Compression of Large Language Models | FlatQuant + YUV420 + VVC 串联；LLaMA-3-8B 2-bit PPL **41.15→26.53**。 / FlatQuant + YUV420 + VVC pipeline; LLaMA-3-8B 2-bit WikiText2 PPL 41.15→26.53. |
| [[2606.06032]] Catastrophic Forgetting as Accessibility Collapse: A Three-Level Framework for Knowledge Persistence in Continual Learning | 遗忘是可访问性崩溃：线性探针保留 **76%** 表征，冻结骨干重训头可恢复 **75.7%**。 / Forgetting as accessibility collapse—76% representation retained by linear probe, 75.7% recoverable via classifier reset. |
| [[2606.06034]] When Good Enough Is Optimal: Multiplication-Only Matrix Inversion Approximation for Quantized Gated DeltaNet | Neumann 截断 + 并行残差校正；Snapdragon NPU 逆核最高 **5×** 加速。 / MatMul-only approximate inverse for Gated DeltaNet—up to 5× inverse-kernel speedup on Snapdragon NPU. |
| [[2606.06293]] PAC-Bayesian Adversarially Robust Generalization for Message Passing Graph Neural Networks: A Sensitivity Analysis | 灵敏度感知各向异性 PAC-Bayes 将 leading 维度从 h log(lh) 降至 K。 / Sensitivity-aware anisotropic PAC-Bayes tightens MPGNN adversarial generalization bound—leading term O(K) not O(h log lh). |

### 多模态、视觉与科学应用 / Multimodal, Vision & Scientific Applications

| Paper | Summary (Chinese / English) |
|-------|-----------------------------|
| [[2606.04804]] The Right Measure for Physics-Constrained Generation: A Co-Area Correction for Posterior-Consistent PDE Inverse Problems | 硬 PDE 约束投影忽略 co-area Jacobian；CoCoS/CoCo-Flow 恢复与金标准后验一致的不确定性。 / Co-area Fixman Jacobian correction for physics-constrained generation—CoCoS/CoCo-Flow match gold-standard PDE posteriors. |
| [[2606.05180]] From Scoring to Explanations: Evaluating SHAP and LLM Rationales for Rubric-based Teaching Quality Assessment | CLASS 反馈质量评分：SHAP 比 LLM 理由更能忠实驱动预测且可跨架构迁移。 / On CLASS feedback-quality scoring, SHAP attributions are more faithful and transferable than LLM rationales. |
| [[2606.05328]] The Invisible Hand of Physics: When Video Diffusion Models Know More Than They Show | 反向流匹配探测 DiT 中间态物理合理性 **~81.27%**，信号在去噪 Transformer 内部涌现。 / Reverse flow-matching probes DiT internals for physical plausibility ~81.27%—signal emerges in denoising transformer, not VAE. |
| [[2606.05576]] UltraVR: A Diagnostic Ultra-Resolution Image-VQA Benchmark for Evidence-Grounded Reasoning | 四域超高分辨率 VQA 诊断基准 + GT-CoT；最强 VLM 宏准确率仅 **44.9%**。 / Four-domain ultra-resolution evidence-grounded VQA benchmark; best VLM macro accuracy 44.9%. |
| [[2606.06260]] OneReason Technical Report | OneReason 使生成式推荐 thinking 模式稳定超越 non-thinking；开源 8B/0.8B 与 OneReason-Bench。 / OneReason makes thinking mode beat non-thinking in generative recommendation; open 8B/0.8B + OneReason-Bench. |

## All Papers

| # | Paper | Summary |
|---|-------|---------|
| 1 | [[2606.04032]] Do Transformers Need Three Projections? Systematic Study of QKV Variants | **Q-K=V** 削减 **50%** KV cache，困惑度仅 **+3.1%**（300M）；与 GQA/MQA 正交叠加达 **87.5%–96.9%** 压缩。 / Q-K=V halves KV cache with +3.1% PPL (300M); orthogonal to GQA/MQA for up to 96.9% cache reduction. |
| 2 | [[2606.04037]] Toward Pre-Deployment Assurance for Enterprise AI Agents: Ontology-Grounded Simulation and Trust Certification | 企业 Agent 部署前验证框架：本体场景生成 + Trust Certificate；G4 监管覆盖率 **48.3%** vs persona **33.1%**。 / Pre-deployment enterprise-agent assurance with ontology scenarios and graduated Trust Certificates. |
| 3 | [[2606.04560]] Rollout-Level Advantage-Prioritized Experience Replay for GRPO | GRPO rollout 级经验回放以 \|A_i\| 优先回收高梯度信号；五套数学基准平均 **+4.35 pp**。 / Rollout-level advantage-prioritized replay for GRPO—+4.35 pp average on five math benchmarks. |
| 4 | [[2606.04804]] The Right Measure for Physics-Constrained Generation: A Co-Area Correction for Posterior-Consistent PDE Inverse Problems | 硬 PDE 约束投影忽略 co-area Jacobian；CoCoS 恢复与金标准后验一致的不确定性。 / Co-area Jacobian correction—CoCoS/CoCo-Flow match gold-standard PDE inverse posteriors. |
| 5 | [[2606.05168]] Epidemiology of Model Collapse: Modeling Synthetic Data Contamination via Bilayer SIR Dynamics | 双层 SIR 模型 R₀>1 超临界；合成文本检测 γ_D 为最高杠杆参数。 / Bilayer SIR collapse model: supercritical R₀>1; synthetic-text detection γ_D highest leverage. |
| 6 | [[2606.05170]] ERRORQUAKE: Heavy-Tailed Error Severity Distributions in Open-Weight Large Language Models | ERRORQUAKE-10K 用 *b* 指数刻画错误严重度；准确率相近模型 *b* 仍可显著不同。 / ERRORQUAKE-10K: Gutenberg–Richter *b* for error severity—accuracy alone misses tail risk. |
| 7 | [[2606.05173]] Predict and Reconstruct: Joint Objectives for Self-Supervised Language Representation Learning | JEPA+MLM hybrid 嵌入更均匀（uniformity ≤−0.16），GLUE 线性探测几乎持平。 / Hybrid JEPA+MLM yields more uniform embeddings; GLUE linear probes near-flat. |
| 8 | [[2606.05180]] From Scoring to Explanations: Evaluating SHAP and LLM Rationales for Rubric-based Teaching Quality Assessment | CLASS 反馈质量：SHAP 比 LLM 理由更能忠实驱动预测且可跨架构迁移。 / SHAP more faithful than LLM rationales for rubric-based classroom feedback scoring. |
| 9 | [[2606.05182]] LANTERN: Layered Archival and Temporal Episodic Retrieval Network for Long-Context LLM Conversations | 零 LLM 归档 + RRF 检索恢复 **78.3%** 压缩丢失事实；四套模型答题 **+8.4pp**。 / Zero-LLM archival + RRF retrieval—78.3% fact recovery, +8.4pp QA accuracy. |
| 10 | [[2606.05183]] The Granularity Gap: A Multi-Dimensional Longitudinal Audit of Sycophancy in Gemini Models | 粒度缺口：二元过滤器漏检 **94%** 中度谄媚；谄媚与幻觉呈 Alignment Tax（ρ=0.40）。 / Granularity gap: binary filters miss 94% moderate sycophancy; sycophancy–hallucination alignment tax. |
| 11 | [[2606.05194]] Temporal Preference Concepts and their Functions in a Large Language Model | Qwen3-4B L17–L35 时间偏好子图；CAA 引导长/短期偏好赔率 **~3.4×**。 / Temporal-preference subgraph L17–L35 in Qwen3-4B; CAA steering ~3.4× preference odds. |
| 12 | [[2606.05219]] Gradient Descent with Large Step Size Restores Symmetry in Deep Linear Networks with Multi-Pathway | EoS 大学习率逆转对称破缺，偏好跨通路共享表征。 / Large-step EoS GD reverses winner-take-all—favors shared multi-pathway representations. |
| 13 | [[2606.05233]] Domain-Conditioned Safety in Frontier Computer-Using Agents: A 793-Episode Browser Benchmark, a Coding-Domain Cross-Reference, and a Reproducibility Audit of Recent Red-Teaming | CUA 浏览器 ASR **0/140**；同权重 SkillBench 编码注入 **100%**（Sonnet 4.6）。 / Browser ASR 0/140; same weights 100% coding skill injection—domain-conditioned CUA safety. |
| 14 | [[2606.05241]] Search-Time Contamination in Deep Research Agents: Measuring Performance Inflation in Public Benchmark Evaluation | 搜索时污染三级分类；医学 QA 上 STC 普遍，HLE 子集可虚高约 **4%**。 / Search-Time Contamination taxonomy; up to ~4% score inflation on medical QA/HLE subsets. |
| 15 | [[2606.05290]] Do Models Share Safety Representations? Cross-Model Steering for Safe Visual Generation | 源 LLM 安全方向经良性对齐迁移至 T2I/T2V，目标侧无需不安全数据。 / Cross-model safety steering from source LLM to generative vision without unsafe target data. |
| 16 | [[2606.05308]] Statistically Reliable LLM-Based Ranking Evaluation via Prediction-Powered Inference | PRECISE：PPI++ 扩展至排序指标，少量标注校正 LLM 评判偏差。 / PRECISE: prediction-powered inference for unbiased, lower-variance ranking metrics. |
| 17 | [[2606.05326]] Gradient descent at the Edge of Stability: free energy model and kinetic description of the two-layer network | EoS 有效自由能 F(θ,Σ) 与两层网络 W₂ 动能梯度流。 / EoS effective free energy and two-layer W₂ kinetic gradient-flow description. |
| 18 | [[2606.05328]] The Invisible Hand of Physics: When Video Diffusion Models Know More Than They Show | 反向流匹配探测 DiT 物理合理性 **~81.27%**，VAE 潜空间近随机。 / Reverse flow-matching probes DiT physics ~81.27%; VAE latents near chance. |
| 19 | [[2606.05339]] A Taxonomy of Runtime Faults in Model Context Protocol Servers | MCP 运行时故障分类：**11/27/73** 三级，55 开发者调研无一子类零观测。 / MCP runtime-fault taxonomy: 11/27/73 levels; no subcategory unobserved by practitioners. |
| 20 | [[2606.05346]] Trajectory Dynamics in Language Model Hidden States Predict Human Processing Costs Beyond Surprisal | 轨迹外推误差与 surprisal 正交（r=.044），独立预测阅读时间。 / Trajectory extrapolation error orthogonal to surprisal (r=.044), predicts reading times. |
| 21 | [[2606.05378]] Pattern Selectivity is Not Task-Causal Structure: A Cross-Architecture Mechanistic Study of Composed-Task Circuits in 1B-Class Language Models | 组合任务因果电路跨架构不同；五类筛选分类学。 / Composed-task causal circuits differ across 1B architectures; five-class screening taxonomy. |
| 22 | [[2606.05384]] Stability vs. Manipulability: Evaluating Robustness Under Post-Decision Interaction in LLM Judges | 决策后挑战翻转 **~49%** 评判偏好；ERS 量化交互鲁棒性。 / Post-decision challenge flips ~49% judge preferences; ERS quantifies manipulability. |
| 23 | [[2606.05402]] ReasoningFlow: Discourse Structures for Understanding LLM Reasoning Traces | 子句级 DAG 标注 1,260 条 LRM 轨迹；**85%** 错误步骤不因果影响答案。 / Sub-clause DAG on 1,260 LRM traces; 85% error steps don't causally affect answers. |
| 24 | [[2606.05403]] Trust, but Don't Verify: Epistemic Blind Spots in LLM Source Evaluation | 方法论文体门：不可能统计≈有效统计 SPI；epistemic alignment 概念。 / Methodology-register gate: impossible≈valid stats in synthesis—epistemic alignment gap. |
| 25 | [[2606.05429]] Minimizing the Hidden Cost of Scales: Graph-Guided Ultra-Low-Bit Quantization for Large Language Models | SAGE-PTQ 隐藏 scale **~0.004 bit/权重**；LLaMA-2-70B 解码 **~1.5×**。 / SAGE-PTQ ~0.004 bit/weight scale overhead; ~1.5× LLaMA-2-70B decode speedup. |
| 26 | [[2606.05433]] Zero knowledge verification for frontier AI training is possible | zkVM + Merkle 承诺验证真实 BF16/FP32 训练；开销估 **2–10%**。 / ZK training verification with native BF16/FP32 zkVM—estimated 2–10% overhead. |
| 27 | [[2606.05486]] Localizing Prompt Ambiguity in Large Language Models with Probe-Targeted Attribution | PRIG 歧义定位 AUROC **0.840**（gold **0.891**），句子 F1 **0.734**。 / PRIG ambiguity localization AUROC 0.840 (gold 0.891), sentence F1 0.734. |
| 28 | [[2606.05557]] AURA: Intent-Directed Probing for Implicit-Need Surfacing in Situated LLM Agents | IntentFrame gap 路由；隐含需求 **+0.07**，事实查询探测 **−82%**。 / IntentFrame gap routing: +0.07 implicit coverage, 82% fewer factual probes. |
| 29 | [[2606.05576]] UltraVR: A Diagnostic Ultra-Resolution Image-VQA Benchmark for Evidence-Grounded Reasoning | 四域超高分辨率 + GT-CoT；最强 VLM **44.9%** 宏准确率。 / Four-domain ultra-res VQA + GT-CoT; best VLM 44.9% macro accuracy. |
| 30 | [[2606.05610]] Predictable Scaling Laws of Optimal Hyperparameters for LLM Continued Pre-training | CPT 超参幂律 + C_pre 零样本预测；节省 **73–92%** 搜索算力。 / CPT hyperparameter scaling + C_pre prediction—73–92% less search compute. |
| 31 | [[2606.05616]] What's in a Name? Morphological Shortcuts by LLMs in Pharmacology | INN 词缀启发式致虚构药名药理推断；激活修补 L2–10。 / INN affix shortcuts on fictitious drugs; activation patching L2–10. |
| 32 | [[2606.05644]] FIDES: Faithful Inference via Deep Evidence Signals for Retrieval-Memory Conflict in RAG | 三深度证据信号 token 级 α_t；**12/12** CF 最优。 / Three deep evidence signals → token α_t; 12/12 best context fidelity. |
| 33 | [[2606.05682]] Beyond Output Matching: Preserving Internal Geometry in NVFP4 LLM Distillation | CKA-QAD 对齐 decoder Gram；恢复 NVFP4 内部几何与下游精度。 / CKA-QAD aligns decoder Gram beyond KL—restores NVFP4 geometry and accuracy. |
| 34 | [[2606.05688]] Value-and-Structure Alignment for Routing-Consistent Quantization of Mixture-of-Experts Models | VSRAQ 数值+路由结构对齐；MoE PTQ 零推理开销。 / VSRAQ value+structure alignment for routing-consistent MoE PTQ. |
| 35 | [[2606.05711]] Beyond tokens: a unified framework for latent communication in LLM-based multi-agent systems | WHAT/WHICH/HOW 综述 **18** 种潜空间多智能体通信（2024–2026）。 / WHAT/WHICH/HOW survey of 18 latent multi-agent communication methods. |
| 36 | [[2606.05799]] CaliDist: Calibrating Large Language Models via Behavioral Robustness to Distraction | 分心鲁棒性校准：ECE **23%→7%**（七基准六模型）。 / Distraction-robust calibration: ECE 23%→7% across seven benchmarks. |
| 37 | [[2606.05817]] Consistency Training Along the Transformer Stack | MLPCT/AttCT 栈级一致性；六类威胁上轨迹级与表征级互补。 / MLPCT/AttCT stack consistency across six threat families. |
| 38 | [[2606.05843]] Mechanistic Insights into Functional Sparsity in Multimodal LLMs via CoRe Heads | CoRe 头 **~5%** 因果不可或缺；prefill **1.8–2.3×** 加速。 / ~5% CoRe heads causally essential; 1.8–2.3× prefill speedup. |
| 39 | [[2606.05861]] LLMCodec: Adapting Video Codecs for Efficient Weight Compression of Large Language Models | YUV420+VVC 权重压缩；LLaMA-3-8B 2-bit PPL **26.53**。 / YUV420+VVC weight codec; LLaMA-3-8B 2-bit PPL 26.53. |
| 40 | [[2606.05874]] Evaluating Stochastic Collapse and Implicit Bias in Multimodal Large Language Models | RandomBench：MLLM 随机选择下 Stochastic Collapse；RI 低至 **0.068**。 / RandomBench: stochastic collapse under logic-neutral random choice; RI down to 0.068. |
| 41 | [[2606.05957]] Dead Directions: Geometric Singular Learning | Fisher 死方向统一奇异学习理论与信息几何；DDCAdam 等变优化。 / Dead directions unify singular learning theory; DDCAdam equivariant optimizer. |
| 42 | [[2606.05958]] Steering Vectors are an Adversarial Attack Surface | 4–6% 词元隐身投毒致 steering 越狱 **20–55%** ASR。 / 4–6% token stealth poisoning → 20–55% steering jailbreak ASR. |
| 43 | [[2606.06032]] Catastrophic Forgetting as Accessibility Collapse: A Three-Level Framework for Knowledge Persistence in Continual Learning | 可访问性崩溃：探针 **76%** 表征保留，分类头重置恢复 **75.7%**。 / Accessibility collapse: 76% probe retention, 75.7% recoverable via head reset. |
| 44 | [[2606.06034]] When Good Enough Is Optimal: Multiplication-Only Matrix Inversion Approximation for Quantized Gated DeltaNet | Neumann 近似逆；NPU 逆核 **5×** 加速，Qwen3.5 PPL 匹配 FLA。 / MatMul-only approximate inverse; 5× NPU inverse speedup, matched Qwen3.5 PPL. |
| 45 | [[2606.06188]] The Tell-Tale Norm: ℓ₂ Magnitude as a Signal for Reasoning Dynamics in Large Language Models | ℓ₂ 追踪推理；ALRR/ERSS/LRS 平均 **+4.51%**（难题 **+9.13%**）。 / ℓ₂ tracks reasoning; ALRR/ERSS/LRS +4.51% avg (+9.13% hard tasks). |
| 46 | [[2606.06223]] From Reward-Hack Activations to Agentic Risk States: Context-Calibrated Mechanistic Monitoring in LLM Agents | reward-hack 激活→ReAct 风险状态监测；混合 LoRA 行为转移最强。 / Reward-hack activations → ReAct risk-state monitoring; hybrid LoRA strongest shift. |
| 47 | [[2606.06238]] Generative Criticality in Large Language Model Temperature Scaling | T_c≈1.4 处 χ 幂律发散；低 T 语义方向坍缩。 / Generative criticality at T_c≈1.4; low-T semantic directional collapse. |
| 48 | [[2606.06260]] OneReason Technical Report | 生成式推荐 thinking 稳定超越 non-thinking；开源 8B/0.8B。 / Generative-rec thinking beats non-thinking; open 8B/0.8B + bench. |
| 49 | [[2606.06293]] PAC-Bayesian Adversarially Robust Generalization for Message Passing Graph Neural Networks: A Sensitivity Analysis | MPGNN 对抗鲁棒 PAC-Bayes：leading 项 O(K) 非 O(h log lh)。 / MPGNN adversarial PAC-Bayes bound with O(K) leading term. |
| 50 | [[2606.06333]] Subspace-Aware Sparse Autoencoders for Effective Mechanistic Interpretability | SASA 子空间 SAE 解决 feature splitting；约半 token 预算匹配标准 SAE。 / SASA subspace SAEs fix feature splitting at ~half token budget. |

---

*Overview generated from 50 paper summaries. Paper count verified: 50 .md files found (excluding overview.md).*