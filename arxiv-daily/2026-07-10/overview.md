---
title: "Daily arXiv Digest — 2026-07-10"
date: 2026-07-10
tags:
  - LLM-Agents
  - Interpretability
  - Model-Compression
  - Uncertainty-Quantification
  - Optimization-Theory
  - LLM-Scaling
  - Evaluation
  - Hardware-Acceleration
papers: 50
---

## 今日必读 / Must Read Today

### 1. [[2607.08186]] Hidden Decoding at Scale: Latent Computation Scaling for Large Language Models

**推荐理由 / Why read:** WeChat AI 团队首次将"序列长度扩展"作为固定主干缩放路径推到 100B+ MoE 规模——通过把每个 token 展开为多个流并将注意力代价从二次降到近线性，训练出的 WeLM-HD4-617B 在全部九项难基准上击败匹配的非 HD 基线。这是继稀疏 MoE 之后又一个被工程验证的、可用于已训练大模型的正向缩放维度，对关注大模型架构与训练的人极具参考价值。
The WeChat AI team demonstrates the first sequence-length scaling method at the 100B+ MoE scale: by expanding each token into n streams and cutting attention cost from quadratic to near-linear via Stream-Factorized Attention, WeLM-HD4-617B beats matched non-HD baselines on all nine shared hard benchmarks (e.g., GPQA Diamond 89.1 → 91.2). A genuinely new, engineered scaling dimension beyond sparse MoE.

### 2. [[2607.08284]] Understanding Axes of Difficulty For Long Context Tasks Via PredicateLongBench

**推荐理由 / Why read:** 这篇基准揭示了一个令人不安的事实——闭源强模型在 baseline 长上下文任务上能达 87%–97%，但只要插入 8 个分散的 near-sorted decoy，所有前沿模型（包括 Opus 4.6、GPT-5.4）全部崩溃到 ≤2%。对任何依赖长上下文 LLM 做检索、推理或 Agent 的人，这是必须知道的失效模式。
A sobering benchmark: frontier models hit 87–97% on baseline long-context tasks, but inserting just 8 scattered near-sorted decoys collapses every model (Opus 4.6, GPT-5.4, Gemini 3.1 Pro) to ≤2% on synthetic data and ≤36% on real text. An essential failure mode for anyone building retrieval, reasoning, or agent systems on long-context LLMs.

### 3. [[2607.08124]] TTHE: Test-Time Harness Evolution

**推荐理由 / Why read:** TTHE 把 LLM agent 的可执行控制程序当作测试时适应的状态——仅用无标签执行轨迹驱动种群搜索改写 harness 代码，不更新权重、不需 gold 标签，在 BIRD 困难切片上把基线从 12.0% 拉到 50.0%。这种"改程序而非改权重"的测试时适应思路简洁、实用、可复现，对 Agent 工程方向有直接启发。
TTHE reformulates test-time adaptation as evolution over an agent's executable harness program — proposers rewrite harness code from unlabeled traces, a label-free judge commits changes, lifting BIRD hard-slice from 12.0% to 50.0% with zero weight updates or gold labels. A clean, practical, reproducible idea that directly inspires agent engineering.

---

## 按主题分类 / Papers by Topic

### LLM Agents & Autonomous Research / LLM 智能体与自主研究

| Paper | Summary (中 / EN) |
|--------------------------|
| [[2607.08003]] Reaction-network reasoning (CoThinker) | 强制 GPT-5.4 在显式反应网络上推理，前瞻性合成出乙酸选择性提升约 3 倍的 Cu-Fe 催化剂。 / Forces GPT-5.4 to reason over an explicit reaction network, prospectively guiding a Cu-Fe catalyst with ~3× acetate selectivity gain. |
| [[2607.08010]] Tool-Making LLM Agents | 离线将重复 SOP 编译为版本化工具，亚马逊告警分诊 p50 延迟降 42%、错误率最高降 53%。 / Offline-compiled versioned tools cut Amazon triage p50 latency 42% and error rate up to 53%. |
| [[2607.08093]] CausalDS Benchmark | 因果数据科学 Agent 基准，前沿模型内容正确但不确定度校准差异巨大，Claude Opus 4.8 最优。 / Causal-reasoning agent benchmark; models are correct on content but differ hugely on uncertainty calibration; Claude Opus 4.8 leads. |
| [[2607.08124]] TTHE | 无标签、无权重更新的 harness 种群搜索，BIRD 困难切片 12%→50%。 / Label-free, weight-free harness evolution lifts BIRD hard-slice 12%→50%. |
| [[2607.08332]] XALPHA | 记忆驱动的 AI 量化研究员，CSI300 上 IR 1.5853 远超 CogAlpha 的 0.3743。 / Memory-driven AI quant researcher beats CogAlpha on CSI300 portfolio IR (1.5853 vs 0.3743). |
| [[2607.08662]] WebSwarm | 递归多智能体网页搜索，BrowseComp-Plus 准确率 +17.5pp 超 ReAct。 / Recursive multi-agent web search beats ReAct by +17.5 pp on BrowseComp-Plus. |
| [[2607.08716]] Proactive Memory Agent | 主动干预式记忆代理，Terminal-Bench 2.0 上为 Sonnet 4.5 提升 +8.3pp。 / Proactive memory agent lifts Sonnet 4.5 by +8.3 pp on Terminal-Bench 2.0. |
| [[2607.08758]] Ideas Have Genomes | 科学谱系推理与思想生成基准，最强系统精确准确率仅 27.3%。 / Scientific-lineage reasoning benchmark; best system reaches only 27.3% exact accuracy. |

### Interpretability & Mechanistic Understanding / 可解释性与机制理解

| Paper | Summary (中 / EN) |
|-------|-------------------|
| [[2607.08173]] Overthinking | 放大推理任务向量（α>1）使模型泄露训练秘密，泄露率最高提升约 10 倍。 / Amplifying reasoning task vectors (α>1) leaks training secrets, up to ~10× baseline leak rate. |
| [[2607.08339]] TypeProbe | 线性探针从代码模型隐藏态恢复跨语言类型表征，但对对抗重命名仅部分鲁棒。 / Linear probes recover cross-lingual type representations from code LLMs, only partly robust to adversarial renaming. |
| [[2607.08349]] Certified Interventional Fidelity | 为机制可解释性干预评估引入 anytime-valid 置信序列，认证开销降低 10-30 倍。 / Anytime-valid confidence sequences for mech-interp intervention evaluation cut certification cost 10-30×. |
| [[2607.08393]] Knowing-Using Gap | 形式化"记住但不会用"现象，self-patching 揭示知识存储层与推理层错位。 / Formalizes the "remembering but not using" gap; self-patching reveals storage-circuit misalignment. |
| [[2607.08499]] Cross-seed SAE | Procrustes 旋转预对齐 + 联合 SAE 提取跨种子通用特征，Pearson r ≥ 0.70。 / Procrustes-aligned joint SAE extracts cross-seed universal features with Pearson r ≥ 0.70. |
| [[2607.08605]] Structured SAE (S²AE) | 结构化稀疏 SAE 提升 VLM 视觉概念对齐 mIoU +6.06%，并溢出提升语言侧。 / Structured-sparsity SAE lifts VLM visual concept mIoU +6.06%, with spillover gains on language side. |
| [[2607.08733]] Super Weights | 单独训练最重要的"超级权重"反令精度跌回随机，LoRA 全层分解才有效。 / Training only "Super Weights" collapses accuracy to random; LoRA's layer-wide decomposition is what works. |

### Uncertainty, Calibration & Reliability / 不确定度、校准与可靠性

| Paper | Summary (中 / EN) |
|-------|-------------------|
| [[2607.08017]] GRAPH EVAL | 将 CoT 转为因果 DAG 量化推理忠实度，GSC 解码把忠实胜率提到 79.5%。 / Converts CoT to causal DAGs to measure faithfulness; GSC decoder lifts faithful-win share to 79.5%. |
| [[2607.08046]] LLM Forecasters Probing | 内部激活探针将校准误差从 0.093 降到 0.044，并节省 30-47% token。 / Internal-activation probes cut calibration error 0.093→0.044 and save 30-47% tokens. |
| [[2607.08059]] When Thinking Hurts (VLMs) | 思考链把 VLM 幻觉检测 AUROC 从 0.899 压塌到 0.492，链内熵可恢复信号。 / Thinking chains collapse VLM hallucination-detection AUROC 0.899→0.492; within-chain entropy restores it. |
| [[2607.08065]] Self-Consistency Audit | 26.5 万次采样证明自洽性是弱正确性代理，gpt-4.1 高一致性答案 48% 是错的。 / 265k-sample audit shows self-consistency is a weak correctness proxy; gpt-4.1 high-agreement answers are wrong 48% of the time. |
| [[2607.08377]] Eigenvalue Calibration | 为 LLM 语义嵌入密度矩阵特征值提出校准理论，校准后 AUROC 多有提升。 / Calibration theory for density-matrix eigenvalues of LLM embeddings; recalibration improves AUROC in most settings. |
| [[2607.08456]] Two Axes of Abstention | LLM 拒答混淆"答错"与"误答不可答题"，隐藏态探针才能读出可答性。 / LLM abstention conflates answer-correctness and question-answerability; hidden-state probes are needed for the latter. |
| [[2607.08535]] LLM-as-Judge Audit | 审计 LLM 评判可靠性，强模型仍残留 14.7% 位置翻转，陪审投票因高相关几乎无效。 / Audits LLM-as-judge reliability; strong judges still flip 14.7% of verdicts; jury voting adds ~nothing due to error correlation. |

### Model Compression & Efficient Inference / 模型压缩与高效推理

| Paper | Summary (中 / EN) |
|-------|-------------------|
| [[2607.08027]] Structured Pruning (Power Transform) | 改造 AFR 为结构化剪枝，Llama-3-8B 50% 剪枝得 1.57× 加速且超 CFSP +6.47pp。 / Adapts AFR to structured pruning; Llama-3-8B at 50% gets 1.57× speedup and beats CFSP by +6.47 pp. |
| [[2607.08029]] Small VLM Quantization | 首个组件级 VLM 量化研究，MoE 模型 INT4 反而涨点，Dense 模型退化。 / First component-wise VLM quantization study; MoE models gain from INT4 while dense models degrade. |
| [[2607.08241]] Guidance-Aware Quantization (GAMP) | 揭示 CFG 扩散量化零空间陷阱，GAMP 在 6 位取得 FID 39.4（改善 49%）。 / Reveals CFG diffusion quantization null-space trap; GAMP reaches FID 39.4 at 6 bits (49% improvement). |
| [[2607.08399]] Prompt Compression | 用单个激活向量压缩固定指令提示，精度仅降约 1.6pp。 / Compresses a fixed instruction prompt into one activation vector with ~1.6 pp accuracy drop. |
| [[2607.08170]] Layer Patching (KLPatch) | 将最优层 patching 形式化为最短路径，搜索加速 548-1722×。 / Casts optimal layer patching as shortest-path; 548-1722× speedup over exhaustive search. |
| [[2607.08643]] BiSCo-LLM | 无码本二值球面编码用于 ~2-bit LLM 量化，Qwen3-8B 下游精度优于 AQLM/QuIP#。 / Lookup-free binary spherical coding for ~2-bit LLM weight compression; beats AQLM/QuIP# on Qwen3-8B. |
| [[2607.08690]] Relaxed Speculative Decoding | 统一六种无训练松弛投机解码方法，发现调 draft length 常等同松弛收益。 / Unifies six training-free relaxed spec-dec methods; tuning draft length often matches relaxation gains. |
| [[2607.08734]] Quantization Effects (Illusion of Equivalency) | 提出决策级 Correctness Agreement 指标，揭示量化模型逐样本决策大幅背离。 / Decision-level Correctness Agreement metric reveals large per-sample divergence under quantization. |
| [[2607.08526]] aria (On-Device Audio) | 零依赖 C/CUDA 运行时把 Stable Audio 3 搬到树莓派，冷启动快 7.2-7.7×。 / Dependency-free C/CUDA runtime runs Stable Audio 3 on a Raspberry Pi 5; cold-start 7.2-7.7× faster. |

### Optimization & Training / 优化与训练

| Paper | Summary (中 / EN) |
|-------|-------------------|
| [[2607.08104]] SGD with Heavy-Tailed Noise | 首次证明带动的 vanilla SGD 无需梯度裁剪即可在重尾噪声下收敛。 / First convergence proof for vanilla SGD-with-momentum under heavy-tailed noise without clipping. |
| [[2607.08380]] GD Large Step Size | 将大步长 GD 动力学推广到任意余维平坦极小值流形，证明 flip 分岔与收缩。 / Generalizes large-step GD dynamics to arbitrary-codimension flat-minima manifolds with flip bifurcation. |
| [[2607.08406]] Monte Carlo Training | 最朴素突变-选择算法无需梯度即可训练深网，MNIST 达 98.3%。 / Simplest mutation-selection Monte Carlo trains deep nets without gradients; 98.3% on MNIST. |
| [[2607.08511]] LR Scheduling Evaluation | 3938 个变体系统评估学习率调度，发现最优调度强依赖架构类型。 / Systematic 3,938-variant evaluation shows best LR scheduler is strongly architecture-dependent. |
| [[2607.08581]] ELM Spectral Stability | 谱分析表明 SVD 求解器 36/36 成功而迭代超幂法 0/36 失败。 / Spectral analysis shows SVD pseudoinverse succeeds 36/36 while iterative methods fail 0/36 under ill-conditioning. |
| [[2607.08590]] AR-DEIG | 对抗鲁棒的贝叶斯决策感知实验设计，最坏情况风险指标显著更稳定。 / Adversarially robust decision-aware Bayesian experimental design; significantly better worst-case tail risk. |

### Theory & Mathematical Foundations / 理论与数学基础

| Paper | Summary (中 / EN) |
|-------|-------------------|
| [[2607.08041]] BIRD (Diffusion Generalization) | 提出贝叶斯信息受限扩散模型，精确刻画"记忆—泛化"相变边界。 / Bayesian Information Restricted Diffusion model gives an exact memorization-generalization phase boundary. |
| [[2607.08370]] Pfaffian Sets & Neural Networks | 将管状邻域体积界推广到 Pfaffian 超曲面，给出 NN 鲁棒性尾界。 / Generalizes tubular-neighbourhood bounds to Pfaffian hypersurfaces for NN robustness tail bounds. |
| [[2607.08757]] Diffusion Numerical Stability | 证明前向 score 误差任意小仍不能保证 EM 离散采样的矩收敛。 / Proves arbitrarily small forward score error does not certify EM sampling moment convergence. |

### Hardware Acceleration / 硬件加速

| Paper | Summary (中 / EN) |
|-------|-------------------|
| [[2607.08002]] SAP (Stochastic Activity Prediction) | Qualcomm 的纯理论框架预测 Wallace 树低翻转活动，五个形式化定理但无实证。 / Qualcomm's purely theoretical framework predicts Wallace-tree low-switching activity; five formal theorems, no empirical validation. |
| [[2607.08015]] CRIMP (In-Memory Processing) | 单次训练协同量化+剪枝+非理想性自适应，功耗降 122× 且无额外硬件。 / Co-optimizes quantization+pruning+non-ideality adaptation in one pass; 122× power reduction, zero extra hardware. |

### Memory, Context & World Models / 记忆、上下文与世界模型

| Paper | Summary (中 / EN) |
|-------|-------------------|
| [[2607.08032]] Rate-Distortion Memory Compaction | 将 KV-cache/prompt/agent 记忆统一建模为率–失真问题，含 ~70 方法分类。 / Unifies KV-cache/prompt/agent-memory compaction as one rate–distortion problem; ~70-method taxonomy. |
| [[2607.08312]] Discrete Bottlenecks (World Models) | 证明语言梯度进入离散符号瓶颈会结构性崩溃，提出三层最小修复实现零塌缩。 / Shows language gradients through discrete bottlenecks cause structural collapse; a three-layer fix achieves zero collapse. |
| [[2607.08254]] CASL-VAE | 对比式 VAE 从非配对数据学习结构化隐变量，用于疾病子型发现。 / Contrastive VAE learns structured latents from unpaired data for disease subtyping. |

### Evaluation & Benchmarks / 评估与基准

| Paper | Summary (中 / EN) |
|-------|-------------------|
| [[2607.08203]] Colonoscopy Segmentation Audit | 审计 27 篇论文发现评估严重不一致，Dice 掩盖边界与召回失败。 / Audit of 27 papers finds severe evaluation inconsistency; Dice conceals boundary/recall failures. |
| [[2607.08256]] TTS Best-of-N Confound | 揭示 BoN TTS 评估的验证器排序依赖 ASR 家族，提出跨家族集成。 / Exposes BoN TTS evaluator ranking dependence on ASR family; proposes cross-family rank ensembles. |
| [[2607.08284]] PredicateLongBench | 8 个对抗 decoy 即让所有前沿长上下文模型崩溃到 ≤2%。 / 8 adversarial decoys collapse every frontier long-context model to ≤2%. |

### LLM Scaling & Multi-modal RL / LLM 缩放与多模态强化学习

| Paper | Summary (中 / EN) |
|-------|-------------------|
| [[2607.08186]] Hidden Decoding (WeChat AI) | 首次在 100B+ MoE 上验证序列长度扩展，WeLM-HD4-617B 全九项基准超越基线。 / First sequence-length scaling at 100B+ MoE scale; WeLM-HD4-617B beats baselines on all 9 hard benchmarks. |
| [[2607.08193]] VIP (Autocurricula) | 视频语言模型观看策略视频推荐课程，SMAC 胜率 ~84%，交互量减少 100×。 / Video LM watches policy videos to recommend curricula; ~84% SMAC win rate with ~100× fewer interactions. |

---

## All Papers

| # | Link | Title | Topic |
|---|------|-------|-------|
| 1 | [[2607.08002]] | A Theoretical Framework for Stochastic Activity Prediction in Tensor Accelerator Wallace-Tree Multipliers | Hardware Acceleration |
| 2 | [[2607.08003]] | Reaction-network reasoning with frontier models for experimentally confirmed catalyst-selectivity hypotheses | LLM Agents & Autonomous Research |
| 3 | [[2607.08010]] | Tool-Making and Self-Evolving LLM Agents in Low-Latency Systems | LLM Agents & Autonomous Research |
| 4 | [[2607.08015]] | CRIMP: Compact & Reliable DNN Inference on In-Memory Processing via Crossbar-Aligned Compression | Hardware Acceleration |
| 5 | [[2607.08017]] | Can We Trust LLM's Logic? Quantifying Uncertainty, Coherence, and Robustness via a Graph-Based Framework | Uncertainty, Calibration & Reliability |
| 6 | [[2607.08027]] | Structured Pruning of Large Language Models via Power Transformation and Sign-Preserving Score Aggregation | Model Compression & Efficient Inference |
| 7 | [[2607.08029]] | Rethinking Small VLM Quantization: From Component-Wise Analysis to Hardware-Aware Edge Deployment | Model Compression & Efficient Inference |
| 8 | [[2607.08032]] | What to Keep, What to Forget: A Rate–Distortion View of Memory Compaction in LLMs and Agents | Memory, Context & World Models |
| 9 | [[2607.08041]] | An exact information theory of generalization phase transitions in Bayesian diffusion models | Theory & Mathematical Foundations |
| 10 | [[2607.08046]] | What LLM Forecasters Know but Don't Say: Probing Internal Representations for Calibration and Faithfulness | Uncertainty, Calibration & Reliability |
| 11 | [[2607.08059]] | When Thinking Hurts: Epistemic Signals in the Reasoning Chains of Visual Language Models | Uncertainty, Calibration & Reliability |
| 12 | [[2607.08065]] | When LLMs Agree, Are They Right? Auditing Self-Consistency and Cross-Model Agreement | Uncertainty, Calibration & Reliability |
| 13 | [[2607.08093]] | CausalDS: Benchmarking Causal Reasoning in Data-Science Agents | LLM Agents & Autonomous Research |
| 14 | [[2607.08104]] | Vanilla SGD with Momentum Survives Heavy-Tailed Noise | Optimization & Training |
| 15 | [[2607.08124]] | TTHE: Test-Time Harness Evolution | LLM Agents & Autonomous Research |
| 16 | [[2607.08170]] | Understanding Layer Patching in Model Size Interpolation | Model Compression & Efficient Inference |
| 17 | [[2607.08173]] | Overthinking: Amplifying Reasoning Weights to Extract Learned Secrets | Interpretability & Mechanistic Understanding |
| 18 | [[2607.08186]] | Hidden Decoding at Scale: Latent Computation Scaling for Large Language Models | LLM Scaling & Multi-modal RL |
| 19 | [[2607.08193]] | Open-ended Multi-agent Autocurricula via Visual Inspection of Policies | LLM Scaling & Multi-modal RL |
| 20 | [[2607.08203]] | Metrics or Mirage? An Audit of Evaluation Inconsistencies in Colonoscopy Polyp Segmentation | Evaluation & Benchmarks |
| 21 | [[2607.08241]] | Closing the Null Space: Guidance-Aware Quantization for Classifier-Free Diffusion | Model Compression & Efficient Inference |
| 22 | [[2607.08254]] | CASL-VAE: Learning Structured Latent Variables from Unpaired Data | Memory, Context & World Models |
| 23 | [[2607.08256]] | Best-of-N TTS Evaluation is Confounded by ASR Family Alignment | Evaluation & Benchmarks |
| 24 | [[2607.08284]] | Understanding Axes of Difficulty For Long Context Tasks Via PredicateLongBench | Evaluation & Benchmarks |
| 25 | [[2607.08312]] | Write-Protected Discrete Bottlenecks for Language-Grounded World Models | Memory, Context & World Models |
| 26 | [[2607.08332]] | XALPHA: A Memory-Driven AI Quant Researcher | LLM Agents & Autonomous Research |
| 27 | [[2607.08339]] | TypeProbe: Recovering Type Representations from Hidden States of Pre-trained Code Models | Interpretability & Mechanistic Understanding |
| 28 | [[2607.08349]] | Certified Interventional Fidelity for Mechanistic Interpretability | Interpretability & Mechanistic Understanding |
| 29 | [[2607.08370]] | Tubular Neighbourhoods of Pfaffian Sets and Applications to Neural Networks | Theory & Mathematical Foundations |
| 30 | [[2607.08377]] | Eigenvalue Calibration for Semantic Embeddings of Large Language Models | Uncertainty, Calibration & Reliability |
| 31 | [[2607.08380]] | Dynamics of Gradient Descent with Large Step Size Near a Manifold of Flat Minima | Optimization & Training |
| 32 | [[2607.08393]] | Towards Mechanistically Understanding Why Memorized Knowledge Fails to Generalize | Interpretability & Mechanistic Understanding |
| 33 | [[2607.08399]] | Prompt Compression via Activation Aggregation | Model Compression & Efficient Inference |
| 34 | [[2607.08406]] | Beyond Backpropagation: Monte Carlo Method Can Train Deep Neural Networks | Optimization & Training |
| 35 | [[2607.08456]] | Two Axes of LLM Abstention: Answer Correctness and Question Answerability | Uncertainty, Calibration & Reliability |
| 36 | [[2607.08499]] | Cross-seed explainability using Procrustes-conditioned Joint Top-K Sparse Autoencoders | Interpretability & Mechanistic Understanding |
| 37 | [[2607.08511]] | Systematic Evaluation of Learning Rate Scheduling Strategies Across Heterogeneous Architectures | Optimization & Training |
| 38 | [[2607.08526]] | A Quantized Native Runtime for On-Device Semantic Audio Generation | Model Compression & Efficient Inference |
| 39 | [[2607.08535]] | When the Judge Changes, So Does the Measurement: Auditing LLM-as-Judge Reliability | Uncertainty, Calibration & Reliability |
| 40 | [[2607.08581]] | Spectral Stability of Pseudoinverse-Based Extreme Learning Machine | Optimization & Training |
| 41 | [[2607.08590]] | Robust Bayesian Decision Making under Adversarial Uncertainty | Optimization & Training |
| 42 | [[2607.08605]] | When Structured Sparse Autoencoders Learn Consistent Concepts Across Modalities | Interpretability & Mechanistic Understanding |
| 43 | [[2607.08643]] | BiSCo-LLM: Lookup-Free Binary Spherical Coding for Extreme Low-Bit LLM Compression | Model Compression & Efficient Inference |
| 44 | [[2607.08662]] | WebSwarm: Recursive Multi-Agent Orchestration for Deep-and-Wide Web Search | LLM Agents & Autonomous Research |
| 45 | [[2607.08690]] | A Practical Investigation of Training-free Relaxed Speculative Decoding | Model Compression & Efficient Inference |
| 46 | [[2607.08716]] | Remember When It Matters: Proactive Memory Agent for Long-Horizon Agents | LLM Agents & Autonomous Research |
| 47 | [[2607.08733]] | Super Weights in LLMs and the Failure of Selective Training | Interpretability & Mechanistic Understanding |
| 48 | [[2607.08734]] | The Illusion of Equivalency: Statistical Characterization of Quantization Effects in LLMs | Model Compression & Efficient Inference |
| 49 | [[2607.08757]] | Score Accuracy Along the Forward Diffusion Does Not Certify Numerical Stability | Theory & Mathematical Foundations |
| 50 | [[2607.08758]] | Ideas Have Genomes: Benchmarking Scientific Lineage Reasoning and Idea Generation | LLM Agents & Autonomous Research |
