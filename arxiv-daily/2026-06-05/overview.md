---
title: "Daily arXiv Digest — 2026-06-05"
date: 2026-06-05
tags:
  - interpretability
  - mechanistic-analysis
  - quantization
  - efficiency
  - training-dynamics
  - reinforcement-learning
  - distributed-systems
  - evaluation
  - safety
  - theory
  - optimization
papers: 54
---

# Daily arXiv Digest — 2026-06-05

> 54 papers · Topics: interpretability, quantization/efficiency, training dynamics & RL, distributed systems, evaluation & safety, theory & optimization

---

## 今日必读 / Must Read Today

### 1. [[2606.03002]] — How Quantization Changes Interpretable Features

**推荐理由（中文）：** 量化（INT8/INT6/INT4）会系统性地破坏 SAE 特征，而这种损坏对困惑度不可见——在 INT6 时有 37–49% 的可解释特征消失。本文首次从安全性视角揭示了量化部署与可解释性之间的根本矛盾，AUC 0.92–0.97 的特征存活率预测器具有很高的实用价值。

**Why Read (English):** Quantization silently destroys interpretable SAE features in ways that perplexity cannot detect. At INT6, 37–49% of features fail to survive, and this damage is highly predictable (AUC 0.92–0.97) from full-precision statistics alone. A must-read for anyone deploying quantized models where interpretability or safety monitoring matters.

---

### 2. [[2606.03087]] — Learning to Solve, Forgetting to Retain: Correct-Set Turnover in RLVR

**推荐理由（中文）：** RLVR 训练存在"正确集合更替"问题——模型在学会解新题的同时悄然遗忘已掌握的题目。ReMind 用零额外 rollout 的复习队列修复了这一问题，在数学、图像和视频推理任务上均有持续提升，结论简洁且影响广泛。

**Why Read (English):** RLVR training quietly forgets solved problems as it acquires new ones. The "repair-window principle" shows early re-review is far cheaper than late remediation. ReMind, a zero-rollout-overhead fix, yields consistent gains across image-text, video, and math reasoning — a diagnostic with broad implications for RL training stability.

---

### 3. [[2606.03085]] — Multi-component Causal Tracing in Large Language Models

**推荐理由（中文）：** 经典因果追踪只能单组件分析，本文将其扩展到多组件子集，将指数级组合搜索转化为连续梯度优化（PGB-CT），速度提升最高 229×，同时在定位 LLM 行为驱动的注意力头和 MLP 神经元上表现持平或更优。

**Why Read (English):** Classic causal tracing is limited to single components; PGB-CT extends it to arbitrary subsets via continuous gradient optimization, achieving up to 229× speedup over greedy search. This unlocks mechanistic analysis at a scale previously impractical, with clear implications for circuit discovery and attribution.

---

## 按主题分类 / Papers by Topic

### Interpretability & Mechanistic Analysis

| Paper | Short Title | Summary |
|-------|-------------|---------|
| [[2606.03002]] | Quantization vs. SAE Features | 量化对可解释特征的系统性破坏，困惑度不可见 / Quantization silently destroys SAE features; perplexity cannot detect it |
| [[2606.03085]] | Multi-component Causal Tracing | 多组件因果追踪，229× 加速 / PGB-CT extends causal tracing to component subsets, 229× faster than greedy |
| [[2606.03483]] | Hyper-Connection Stream Collapse | 超连接的主流残差流崩溃诊断与轻量级修复 / HC models collapse to dominant-stream regime; LSS fix reduces collapse and improves perplexity |
| [[2606.03712]] | Graph Sink Tokens | 图语言模型中的"图汇聚 token"：激活显著但语义缺失 / Graph sink tokens in GLMs are attention-salient but carry no graph-structural information |
| [[2606.03685]] | World Model in SFT Planners | SFT 规划器中的世界模型线性表示研究 / SFT on valid actions induces linear internal representations, but token probabilities often fail to reflect internal knowledge |
| [[2606.03990]] | Neuron Polarization at Scale | Rosetta 神经元随模型规模幂律增长并更加单义 / Rosetta Neurons scale sublinearly and become more monosemantic; data-domain recovery near-oracle accuracy |
| [[2606.03645]] | Shape of Addition in LLMs | LLM 加法中的几何误差机制：进位电位量化边界滑移 / "Off-by-one" errors in multi-operand addition are geometric slippages in a continuous Carry Potential space |

### Quantization & Efficiency

| Paper | Short Title | Summary |
|-------|-------------|---------|
| [[2606.03458]] | KVarN: KV-Cache Quantization | 推理时 KV 缓存量化误差累积修复，2.3 bit 下 AIME24 60.0% / KVarN fixes error accumulation in KV-cache quantization; SOTA at 2.3-bit on AIME24 (60.0%) |
| [[2606.03465]] | Tensor Decomposition for Compression | 张量分解不适合作为 LLM 后训练独立压缩方案 / Tensor decompositions distort operator geometry; dominated by matrix alternatives and quantization |
| [[2606.04050]] | LiftQuant: Continuous Bit-Width | 维度提升实现连续精度量化，2.4 bit Llama-3-70B perplexity 5.86 / Continuous bit-width via dimensional lifting; 2.4-bit Llama-3-70B perplexity 5.86, beats all 2-bit baselines |
| [[2606.04238]] | Recover-LoRA for 2-bit Models | 2-bit 量化后用合成数据 LoRA 恢复精度，80–95% 恢复率 / LoRA on synthetic data recovers 80–95% accuracy after aggressive 2-bit quantization |
| [[2606.04115]] | dMX: Differentiable Mixed-Precision | 可微分混合精度分配，OCP MX 格式 Pareto 优于均匀量化 / Differentiable per-layer precision assignment for OCP MX formats; Pareto-dominant at intermediate bit-widths |
| [[2606.04620]] | QuBLAST: Block-Level Compression | 块级敏感度分析混合精度量化，40–45% 内存减少 / Block-level sensitivity profiling for mixed-precision; 40–45% memory reduction, perplexity within 5% of FP16 |
| [[2606.03328]] | Calibration Data for Pruning | 单源校准数据在剪枝中存在能力权衡，多源混合是解 / Single-source calibration creates irreconcilable capability trade-offs; multi-source mixing via IGSP resolves it |
| [[2606.03026]] | Spiking LM CPU Inference | 脉冲语言模型 CPU 推理运行时，22.63 tokens/s / Spike-aware C++ runtime for SNNs achieves 22.63 tok/s single-thread, outpacing llama.cpp on same hardware |
| [[2606.04028]] | IEEE P3109 Arithmetic Formats | IEEE P3109 窄位宽浮点格式标准草案，ML 专用 / IEEE P3109 draft standard for parameterized narrow-bitwidth FP formats for ML with formal verification |

### Training Dynamics & RL

| Paper | Short Title | Summary |
|-------|-------------|---------|
| [[2606.03087]] | Correct-Set Turnover in RLVR | RLVR 训练遗忘已学技能，ReMind 零开销修复 / RLVR forgets mastered problems; ReMind review queue fixes it with zero rollout overhead |
| [[2606.03070]] | ASymPO: Async RL Post-Training | 异步 LLM 后训练的非对称策略优化，无需行为策略信息 / ASymPO normalizes token loss by per-response log-probability to fix async GRPO imbalance |
| [[2606.03073]] | JF-HPO: LLM RL Hyperparameter Opt | LLM 强化学习超参数优化，14.9× 每次试验加速 / Joint fidelity HPO achieves 14.9× speedup per trial and 5.8–111.6% performance gains over VeRL |
| [[2606.03234]] | Hidden-Align for RLVR | 隐状态对齐辅助损失提升 RLVR 推理，+3.8–6.2 pp / Hidden-state cosine-similarity auxiliary loss boosts RLVR accuracy +3.8–6.2 pp at zero inference overhead |
| [[2606.03238]] | Mechanistic Taxonomy of RLHF Failure | RLHF 奖励黑客的六模式失效分类法 / Six-mode failure taxonomy for RLHF reward hacking based on checkpoint-to-checkpoint transition signatures |
| [[2606.03131]] | HARVE: Reward Hacking Mitigation | 奖励模型内部黑客子空间编辑，无需微调，+21.1 pp / HARVE edits reward-head weights to subtract a hacking subspace; +21.1 pp gold-preference rate, no fine-tuning |
| [[2606.04145]] | EvalStop: Reward Overoptimization | 多租户 RLHF 平台奖励过优化检测与停止 / EvalStop detects reward hacking with 98.3% precision, saves 21.8% wasted compute |
| [[2606.03532]] | Self On-Policy Distillation Stability | 自蒸馏教师更新时机：隔离期是稳定关键 / Isolation periods are the structural key to stable self on-policy distillation; CGTR achieves zero collapse |
| [[2606.03938]] | q0: Hyper-Epoch Pretraining | 超 epoch 预训练：种群搜索替代单模型精化 / q0 population-search primitives achieve lower validation loss than naive ensemble using 3.8–4.6× fewer epochs |
| [[2606.04272]] | RL Excursions during Pre-Training | 预训练中的 RL：从 4B token 起有效，并行 RL+SFT 最优 / RL effective from 4B tokens; parallel RL+SFT gradients within a single step outperform sequential recipes |
| [[2606.04703]] | Continual Experience Internalization | LLM 智能体经验内化多轮迭代稳定方法 / Principle-level experience + step-wise injection + off-policy context-distillation sustains multi-round self-evolution |
| [[2606.04401]] | TANDEM: Data Mixture Optimization | 双网络数据混合双层优化，NeurIPS 2025 / TANDEM bi-level data mixture optimization outperforms DoReMi/DoGE with O(T^{-1/4}) convergence guarantees |
| [[2606.06021]] | OPRD: On-Policy Representation Distillation | 隐状态级蒸馏：零方差梯度，1.44× 更快 / OPRD supervises at hidden-state level; zero-variance gradient, 1.44× faster, 54% less GPU memory |

### Distributed Systems

| Paper | Short Title | Summary |
|-------|-------------|---------|
| [[2606.03077]] | Libra: Agentic RL Resource Management | 智能体 RL 后训练 GPU 资源管理，3.0× 吞吐量 / Libra's joint planner + C-MLFQ routing achieves 3.0× throughput and 2.5× faster reward convergence |
| [[2606.03498]] | PipeDream Convergence Theory | PipeDream 流水线并行首个非凸收敛理论 / First nonconvex convergence guarantee for PipeDream; staleness penalty scales as Θ(S⁴/K) |
| [[2606.03209]] | DECA: Decentralized Full-Parameter FT | 去中心化无服务器全参数微调，非 IID 数据 / DECA enables server-free full-parameter LLM fine-tuning on non-IID data via block-wise Adam |

### Evaluation & Safety

| Paper | Short Title | Summary |
|-------|-------------|---------|
| [[2606.00644]] | ForeSci: Forward-Looking AI Judgment | LLM 前瞻性研究判断基准，500 任务 / ForeSci benchmark: agentic methods improve evidence traceability but suffer evidence-decision decoupling |
| [[2606.01317]] | SABER: Coding Agent Safety | LLM 编码智能体操作安全基准，最优模型仅 31% 安全完成率 / SABER: Claude Opus 4.6 achieves only 31% safe-completion rate; refusal alignment insufficient for agentic safety |
| [[2606.04168]] | Autoregressive Consistency Hurts Safety | 自回归一致性使安全对齐集中于早期 token，易受攻击 / Autoregressive consistency enables attacks that insert harmful spans inside safe refusal trajectories |
| [[2606.06286]] | LLM Memorization Propensity | LLM 能记忆训练数据，但倾向于不泄露 / PropMe separates memorization capability from propensity; prefix attacks elicit 36× stronger signals than normal prompts |
| [[2606.03365]] | KG Embedding Instability | 知识图谱嵌入中随机种子导致的不稳定性 / Single changed seed causes dramatically different top-K predictions; current KGE benchmarking hides this |
| [[2606.05622]] | AdaPlanBench: Adaptive Planning | 动态多轮约束规划基准，GPT-5 仅达 67.75% / AdaPlanBench tests LLM agents on 307 tasks with hidden constraints; best model (GPT-5) reaches 67.75% |
| [[2606.06462]] | Benchmark Agent: Autonomous Eval | 自主基准构建智能体，20× 低于人工标注成本 / Planner–Executor agentic system builds customizable benchmarks at 20× lower cost than human annotation |

### Theory & Foundations

| Paper | Short Title | Summary |
|-------|-------------|---------|
| [[2606.03899]] | Muon Momentum as Spectral Filter | Muon 动量作为谱低通滤波器的首个理论解释 / First theory showing momentum acts as spectral low-pass filter before orthogonalization in Muon |
| [[2606.04058]] | Spectral Scaling Laws of Muon | Muon 动量缓冲区奇异值幂律规律与前线规模预警 / Muon's singular value quantiles follow clean power laws; final layers hit NS failure at ~300B parameters |
| [[2606.04662]] | Why Muon Outperforms Adam | Muon 优于 Adam 的曲率视角解释：更低归一化方向锐度 / Muon achieves lower Normalized Directional Sharpness than Adam; a curvature-based explanation of its ~2× efficiency |
| [[2606.04031]] | Pseudospectral Bounds for Gradient Descent | 耦合梯度下降中瞬态增长的伪谱界 / Pseudospectral theory (Kreiss constant) gives 2–5× tighter bounds than IQC for bilevel optimization |
| [[2606.04212]] | Edge of Stability as Selective Bias | 稳定边缘是选择性归纳偏置，非均匀优化瓶颈 / EoS redistributes optimization effort based on Hessian alignment; selective bias, not uniform bottleneck |
| [[2606.04280]] | Sampling Conditions in Contrastive Learning | 对比学习中采样多样性与归纳偏置的交互影响 / InfoNCE rewards geometry-distorting encoders when sampling violates diversity; only architectural priors reliably restore isometry |
| [[2606.04327]] | Stationary Plateau for Two-Layer Networks | 两层神经网络稳态高原的几何完整分类 / Complete classification of stationary points on neuron-splitting plateau via inner Hessian definiteness |
| [[2606.04405]] | Low-Rank Decay for Grokking | 低秩衰减在尺度不变 Transformer 中诱导推广性涌现 / LRD retains tangential polar-factor updates that keep reshaping singular value spectrum, inducing grokking |
| [[2606.03338]] | IdEst: Intrinsic Dimension for SSL | 内在维度作为自监督表示质量免标注代理指标 / IdEst's MST-based intrinsic dimension strongly negatively correlates with downstream accuracy across 14+ SSL models |
| [[2606.03092]] | CLEAR: Reasoning Budget Allocation | 推理 token 预算分配：Lambert W 函数闭式解 / CLEAR formalizes reasoning budget as constrained optimization; Lambert W closed-form gives +24 accuracy points under tight budgets |
| [[2606.03825]] | Dynamic Short Convolutions | 输入依赖动态卷积提升 Transformer，1.33–1.60× 计算优势 / Input-dependent depthwise filters before Q/K/V give 1.33–1.60× compute advantage in scaling laws |
| [[2606.04048]] | μP for Gated Delta Networks | 门控 Delta 网络的首个 μP 参数化推导，零样本学习率迁移 / First complete μP for GDN; non-standard LR scalings enable zero-shot LR transfer across widths up to 342M |
| [[2606.06447]] | Latent Reasoning via Normalizing Flows | 归一化流实现隐空间推理，替代显式 CoT / Normalizing flows enable probabilistic latent-space reasoning steps as alternative to discrete chain-of-thought |
| [[2606.03731]] | Conformal LM via Posterior Sampling | 共形语言建模：后验采样保持保证且更完整 / Conformal posterior sampling achieves same risk-control as filtering while producing more complete responses |

---

## All Papers

| arxiv_id | Short Title | One-Liner |
|----------|-------------|-----------|
| [[2606.00644]] | ForeSci: LLM Forward-Looking Judgment | LLM 前瞻性研究判断基准，发现证据-决策解耦问题 / 500-task benchmark finds agents cite correct evidence but forecast wrong research objects |
| [[2606.01317]] | SABER: Coding Agent Safety | 编码智能体操作安全，最优 31% 安全完成率 / 716-task benchmark: best model (Claude Opus 4.6) achieves only 31% safe-completion rate |
| [[2606.03002]] | Quantization Destroys SAE Features | 量化系统性破坏 SAE 特征，困惑度不可见 / INT6 quantization destroys 37–49% of interpretable features, invisible to perplexity |
| [[2606.03026]] | Spiking LM CPU Runtime | 脉冲语言模型 C++ CPU 推理，22.63 tokens/s / C++ INT8 runtime for sparse SNNs achieves 22.63 tok/s, outpacing llama.cpp baselines |
| [[2606.03070]] | ASymPO: Async RL Optimization | 异步 RL 无行为策略信息的非对称策略优化 / ASymPO normalizes token loss by per-response log-prob to fix async GRPO imbalance |
| [[2606.03073]] | JF-HPO: LLM RL Hyperparameter Opt | LLM RL 联合保真度超参数优化，14.9× 加速 / JF-HPO treats model size + training budget as dual fidelity; 14.9× speedup per trial |
| [[2606.03077]] | Libra: Agentic RL Resource Mgmt | 智能体 RL 资源调度，3.0× 吞吐，2.5× 更快收敛 / Libra joint planner + C-MLFQ routing: 3.0× throughput, 2.5× faster reward convergence |
| [[2606.03085]] | PGB-CT: Multi-component Causal Tracing | 多组件因果追踪框架，229× 加速 / PGB-CT converts combinatorial causal search to gradient optimization; up to 229× faster than greedy |
| [[2606.03087]] | Correct-Set Turnover in RLVR | RLVR 遗忘已学技能，ReMind 复习队列修复 / RLVR forgets solved problems; ReMind replay queue yields consistent gains at zero rollout overhead |
| [[2606.03092]] | CLEAR: Reasoning Token Budget | 推理 token 预算 Lambert W 闭式分配，+24 准确率 / CLEAR optimal reasoning budget via Lambert W; +24 accuracy points on math under tight 256-token budget |
| [[2606.03131]] | HARVE: Reward Model Robustness | 奖励模型权重编辑去除黑客子空间，无需微调 / HARVE edits reward-head weights to remove hacking subspace; +21.1 pp gold-preference rate |
| [[2606.03209]] | DECA: Decentralized LLM Fine-Tuning | 无服务器去中心化全参数微调，非 IID 数据 / DECA block-wise Adam enables server-free full-param fine-tuning on non-IID client data |
| [[2606.03234]] | Hidden-Align: RLVR Auxiliary Loss | 隐状态对齐损失提升 RLVR，+3.8–6.2 pp / Cosine-similarity auxiliary loss on correct-rollout hidden states: +3.8–6.2 pp accuracy over DAPO |
| [[2606.03238]] | RLHF Failure Taxonomy | RLHF 奖励黑客六模式失效分类 / Six-mode failure taxonomy for RLHF reward hacking based on checkpoint transition signatures |
| [[2606.03328]] | Calibration Data Trade-offs for Pruning | 剪枝校准数据：多源混合解决能力权衡 / Multi-source calibration (IGSP) resolves single-source capability trade-offs for high-sparsity pruning |
| [[2606.03338]] | IdEst: SSL Representation Quality | 内在维度是 SSL 表示质量的无标签代理 / Intrinsic dimension (MST estimator) strongly negatively correlates with downstream linear probing accuracy |
| [[2606.03365]] | KG Embedding Seed Instability | 知识图谱嵌入随机种子引发的不稳定性 / A single changed seed causes dramatically different top-K KG completions; benchmarking hides this |
| [[2606.03458]] | KVarN: KV-Cache Quantization | KV 缓存量化误差累积修复，AIME24 60.0% @ 2.3 bit / KVarN Hadamard rotation + variance normalization; SOTA on AIME24 at 2.3 bits/element |
| [[2606.03465]] | Tensor Decompositions Unsuitable for Compression | 张量分解不适合 LLM 后训练独立压缩 / Tucker/TT decompositions distort operator geometry; dominated by matrix alternatives and quantization |
| [[2606.03483]] | Hyper-Connection Stream Collapse | 超连接 Transformer 主流残差流崩溃与 LSS 修复 / HC models collapse to dominant-stream; LSS (nd extra params) breaks symmetry and reduces collapse |
| [[2606.03498]] | PipeDream Convergence Theory | PipeDream 流水线并行首个非凸收敛保证 / First nonconvex convergence guarantee for PipeDream; staleness penalty Θ(S⁴/K) |
| [[2606.03532]] | CGTR: Self Distillation Teacher Refresh | 自蒸馏教师刷新时机：隔离期是稳定结构关键 / Isolation periods are key to stable self on-policy distillation; CGTR achieves zero collapse |
| [[2606.03645]] | Shape of Addition: Arithmetic Geometry | LLM 加法误差为几何滑移，进位电位量化边界 / Off-by-one errors are geometric slippages in a Carry Potential space; Noisy Quantization Model R²=0.80 |
| [[2606.03685]] | World Model in SFT Planners | SFT 规划器中的线性世界模型表示 / SFT induces linear internal representations of action validity but token probabilities often fail to reflect them |
| [[2606.03712]] | Graph Sink Tokens in GLMs | 图语言模型汇聚 token：显著但无图结构信息 / Graph sink tokens are attention-salient but carry no graph-structural information |
| [[2606.03731]] | Conformal LM via Posterior Sampling | 共形语言建模：后验采样保持保证且更完整 / Conformal posterior sampling achieves same risk-control as filtering while producing more complete responses |
| [[2606.03825]] | Dynamic Short Convolutions for Transformers | 输入依赖动态卷积，1.33–1.60× 计算优势 / Input-dependent depthwise filters before Q/K/V: 1.33–1.60× compute advantage in scaling laws |
| [[2606.03899]] | Muon Momentum as Spectral Denoiser | Muon 动量先滤波后正交化的首个理论解释 / First theory: momentum acts as spectral low-pass filter before orthogonalization in Muon optimizer |
| [[2606.03928]] | VaSE: KV Cache Value Spike Protection | KV 缓存值状态异常幅值保护，4× 压缩无循环退化 / VaSE protects large-magnitude value states from eviction; 4× compression with no repetition loops |
| [[2606.03938]] | q0: Hyper-Epoch Pretraining | 超 epoch 预训练种群搜索，3.8–4.6× 更少 epoch / q0 population primitives (snapshot ensemble + chain distillation) achieve lower loss than naive ensemble |
| [[2606.03990]] | Rosetta Neurons Polarize with Scale | Rosetta 神经元随模型规模幂律增长并更加单义 / Rosetta Neurons scale sublinearly; become more monosemantic and domain-specialized at larger scale |
| [[2606.04028]] | IEEE P3109 ML Arithmetic Formats | IEEE P3109 ML 浮点格式标准草案 / IEEE P3109 parameterized narrow-bitwidth FP formats for ML with formal verification (~500 theorems) |
| [[2606.04031]] | Pseudospectral Bounds for Bilevel Opt | 耦合梯度下降瞬态增长的伪谱界 / Kreiss constant bounds transient growth in bilevel/two-time-scale gradient descent; 2–5× tighter than IQC |
| [[2606.04048]] | μP for Gated Delta Networks | 门控 Delta 网络 μP：非标准学习率缩放，零样本迁移 / First μP for GDN; non-standard LR scalings (Θ(1/√d) gating) enable zero-shot LR transfer to 342M |
| [[2606.04050]] | LiftQuant: Continuous Bit-Width Quant | 维度提升实现连续位宽量化，2.4 bit Llama-3-70B perplexity 5.86 / 1-bit lattice lifting enables arbitrary fractional bit-widths; Llama-3-70B at 2.4-bit beats all 2-bit baselines |
| [[2606.04058]] | Spectral Scaling Laws of Muon | Muon 动量奇异值幂律：300B 参数时最终层面临 NS 失效 / Muon singular value quantiles follow layer-specific power laws; final layers hit NS failure at ~300B params |
| [[2606.04115]] | dMX: Differentiable Mixed-Precision | 可微分 OCP MX 格式混合精度分配，Pareto 优于均匀量化 / Differentiable per-layer FP bit-width assignment with annealing; Pareto-dominant over uniform MXFP |
| [[2606.04145]] | EvalStop: RLHF Overoptimization | 多租户 RLHF 奖励过优化 98.3% 精度检测 / EvalStop monitors world feedback to detect reward hacking; 98.3% precision, −21.8% wasted compute |
| [[2606.04168]] | Autoregressive Consistency Hurts Safety | 自回归一致性使安全微调脆弱 / Autoregressive consistency explains why safety fine-tuning is vulnerable to mid-trajectory harmful span insertion |
| [[2606.04212]] | Edge of Stability as Selective Bias | 稳定边缘对训练数据的选择性归纳偏置 / EoS redistributes optimization based on Hessian alignment; selective inductive bias across the training distribution |
| [[2606.04238]] | Recover-LoRA: 2-bit Accuracy Recovery | 2-bit 量化 LoRA 恢复，80–95% 精度回收，7.5–23.3% TPS 提升 / LoRA on synthetic data recovers 80–95% accuracy after W2-GateUp quantization; +7.5–23.3% TPS |
| [[2606.04272]] | RL During Pre-Training | 预训练中 RL 从 4B token 起有效，并行 RL+SFT 最优 / RL effective from 4B tokens; parallel-averaging RL+SFT within a single step is best recipe |
| [[2606.04280]] | Sampling & Inductive Bias in Contrastive | 对比学习：采样多样性违反时 InfoNCE 奖励几何失真 / When sampling diversity condition is violated, InfoNCE rewards geometry-distorting encoders |
| [[2606.04327]] | Stationary Plateau: Two-Layer NN | 两层网络神经元分裂高原的完整几何分类 / Inner Hessian definiteness classifies all stationary points on the neuron-splitting plateau |
| [[2606.04401]] | TANDEM: Bi-Level Data Mixture | 双网络双层数据混合优化，NeurIPS 2025 / TANDEM bi-level data mixture outperforms DoReMi/DoGE with O(T^{-1/4}) guarantees; NeurIPS 2025 |
| [[2606.04405]] | Low-Rank Decay for Grokking | 低秩衰减在尺度不变 Transformer 中诱导推广 / LRD retains tangential weight updates that keep reshaping singular values, inducing grokking in scale-invariant models |
| [[2606.04620]] | QuBLAST: Block-Level LLM Quant | 块级敏感度混合精度量化，40–45% 内存减少 / Block-level sensitivity + activation scaling; 40–45% memory reduction within 5% perplexity of FP16 |
| [[2606.04662]] | Why Muon Beats Adam: Curvature | Muon 优于 Adam 的曲率解释：更低方向锐度 / Muon achieves lower Normalized Directional Sharpness; curvature geometry explains ~2× LLM training efficiency |
| [[2606.04703]] | Continual Experience Internalization | 智能体经验内化多轮迭代稳定配方 / Principle-level experience + step-wise injection + off-policy context-distillation enables stable multi-round self-evolution |
| [[2606.05622]] | AdaPlanBench: Adaptive Planning | 动态约束自适应规划基准，GPT-5 仅 67.75% / 307-task multi-turn benchmark with hidden constraints; best model (GPT-5) achieves only 67.75% |
| [[2606.06021]] | OPRD: On-Policy Repr. Distillation | 隐状态级蒸馏：零方差梯度，Pareto 优于输出空间方法 / Hidden-state MSE supervision is zero-variance and Pareto-dominant over all output-space distillation methods |
| [[2606.06286]] | LLM Memorization vs. Propensity | LLM 能记忆但不倾向泄露；前缀攻击 36× 信号更强 / PropMe separates memorization capability from propensity; prefix attacks elicit 36× stronger memorization |
| [[2606.06447]] | Latent Reasoning via Normalizing Flows | 归一化流实现隐空间推理 / Normalizing flows enable probabilistic continuous latent-space reasoning without abandoning autoregressive generation |
| [[2606.06462]] | Benchmark Agent: Autonomous Eval | 自主基准构建智能体，成本 1/20 / Planner–Executor agentic system builds multi-modal benchmarks at ~20× lower cost than human annotation |

---

> **Paper count verification:** 54 `.md` files in directory (excluding overview.md). All Papers table: 54 entries. Count matches. ✓
