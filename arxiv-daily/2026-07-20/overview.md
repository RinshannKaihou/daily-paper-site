---
title: "每日 arxiv 论文速览 / Daily arxiv Paper Digest — 2026-07-20"
date: 2026-07-20
tags:
  - arxiv-daily
  - llm
  - interpretability
  - agents
  - rl-theory
  - efficient-inference
  - ai-safety
  - peft
papers: 48
---

# 每日 arxiv 论文速览 / Daily arxiv Paper Digest — 2026-07-20

> 本日共收录 **48 篇** arxiv 论文，覆盖 LLM 训练/推理效率、机制可解释性、Agent 系统与安全、RL 理论、视觉/多模态、硬件协同设计等方向。 Below is a curated digest of **48 arxiv papers** spanning LLM training/inference efficiency, mechanistic interpretability, agent systems & safety, RL theory, vision/multimodal, and hardware co-design.

---

## 今日必读 / Must Read Today

### 1. [[2607.17620]] PoLoRA — LoRA 作为优化器态 / LoRA as Optimizer State

- **理由 / Reason**: 把 LoRA 重新定位为"低秩优化器记忆"而非单纯的参数高效微调模块，从根本上解释了为什么 LoRA 可在不同 rank 间迁移学习率，并在 1.2–1.7× 步数上超过 Adam。这一视角为后续 PEFT 与优化器协同设计打开了新方向。
- **Why it matters**: Repositions LoRA as "low-rank optimizer memory" rather than a mere PEFT adapter, explaining why learning rates transfer across ranks and achieving 1.2–1.7× step speedup over Adam. A genuinely new lens that opens a fresh design axis for optimizer–PEFT co-design.

### 2. [[2607.17674]] Uncovering Latent Reasoning Strategies (Altabah & Lafferty, Yale)

- **理由 / Reason**: 提出模型导向的变分目标来从推理轨迹中"反推"潜在的推理策略，并在多个任务上获得 Strategy Alignment 接近 0.9–1.0 的稳定分解。作为机制可解释性方向的工作，它把抽象的"模型在想什么"转化为可量化、可复现的潜变量推断问题。
- **Why it matters**: Proposes a model-directed variational objective to infer latent reasoning strategies from traces, achieving Strategy Alignment near 0.9–1.0. Turns the abstract "what is the model thinking?" question into a quantifiable, reproducible latent-variable inference problem in mechanistic interpretability.

### 3. [[2607.17823]] Theoretical Foundations of max@k Reinforcement Learning (Bocconi)

- **理由 / Reason**: 为 LLM 推理评估常用的 max@k / best-of-N 目标给出第一个严格的有限时域 RL 理论：证明 Markovian 策略在此目标下严格次优（差距 ≥1.24）、历史可压缩为两维、精确规划 NP-hard、样本复杂度比经典 RL 多 K 倍。是理解 RLHF/RLVR"训练-评估不匹配"问题的理论基石。
- **Why it matters**: Provides the first rigorous finite-horizon RL theory for the max@k / best-of-N objective used in LLM reasoning evaluation — Markovian policies are provably sub-optimal (gap ≥1.24), history compresses to two scalars, exact planning is NP-hard, and sample complexity is K× classical RL. A foundational theoretical reference for the train–eval mismatch in RLHF/RLVR.

---

## 按主题分类 / Papers by Topic

### A. LLM 训练与优化 / LLM Training & Optimization

| ID | 标题 / Title | 一句话总结 / TL;DR |
|---|---|---|
| [[2607.17620]] | PoLoRA | 把 LoRA 重新定位为低秩优化器状态，在多个任务上比 Adam 快 1.2–1.7×，且学习率可跨 rank 迁移。 Repositions LoRA as low-rank optimizer state, 1.2–1.7× faster than Adam, with LR transferring across ranks. |
| [[2607.17843]] | Möbius Learning | 把 Transformer block stack 切分给多 worker 并以循环深度折叠训练，仅在 L≥6 时优于 ordered-loop（Δ=−0.0084 到 −0.0083）。 Cyclic depth-folding distributed training that beats ordered-loop only at L≥6 (Δ=−0.0084 to −0.0083). |
| [[2607.17822]] | MRSNorm / Phasor Attention | 把通道两两配对成 2D 相量并先 L2 后 L1 平均，参数减半且在 CIFAR-100 压力测试下保持稳定。 Pairs channels into 2D phasors with L2-then-L1 averaging, halving parameters while stable under CIFAR-100 stress tests. |
| [[2607.18130]] | mHC-PEFT | 把 Manifold-Constrained Hyper-Connections 作为 PEFT 的新"残差路由"轴；finetuning 中把残差混合矩阵固定为单位阵反而更好，但单独使用尚未稳定超越 LoRA。 Applies manifold-constrained hyper-connections as a new "residual routing" PEFT axis; identity residual mixing helps in finetuning, but mHC alone does not consistently beat LoRA. |
| [[2607.17913]] | AE-PSL | 在并行拆分学习的拆分层放置轻量自编码器，在四个视觉数据集上达到约 10.2× 通信压缩且无精度损失。 Lightweight autoencoder at the split layer of parallel split learning achieves ~10.2× communication compression with no accuracy loss on four vision datasets. |
| [[2607.17607]] | OCO → Nonconvex via Preconditioner | 通过预条件子把在线凸优化转换为非凸问题，解决 Chen-Hazan 2024 开放问题，给出 O(T⁻¹/²) 和 O(T⁻²/⁷) 收敛率。 Resolves the Chen-Hazan 2024 open problem by reducing OCO to nonconvex optimization with a preconditioner, achieving O(T⁻¹/²) and O(T⁻²/⁷) rates. |
| [[2607.17595]] | Sub-Gaussian SA Concentration | 给出压缩型随机逼近的第一个次高斯极大值界，证明在乘性噪声下成立，证明是初等的。 First sub-Gaussian maximal concentration bound for contractive stochastic approximation under multiplicative noise, via an elementary proof. |
| [[2607.17513]] | HySAT Hyperbolic Expert AI | 只在损失层使用 Lorentz 几何，在 17.95M 样本上 0 NaN，而 17 个 HyperLoRA 对照全部崩溃。 Lorentz geometry only at the loss layer yields 0 NaN across 17.95M samples vs 17 HyperLoRA crashes. |
| [[2607.18114]] | Sycophancy Alignment Tuning Representations | 在 5 模型家族 × 7 偏置上三角验证，发现谄媚等线索诱导偏置由对齐微调而非预训练安装，单一方向即可解码且因果有效。 Triangulates 7 cue-induced biases across 5 model families — sycophancy and related biases are installed by alignment tuning, not pretraining, and each corresponds to a causally-effective linear direction. |

### B. LLM 推理效率 / LLM Inference Efficiency

| ID | 标题 / Title | 一句话总结 / TL;DR |
|---|---|---|
| [[2607.17652]] | FlowBlock | 波前并行解码的扩散式 LLM，训练免费情况下相对 LLaDA-2.1/2.0 达到 2.95×/4.01× TPS。 Wavefront-parallel decoding for diffusion LLMs, training-free 2.95×/4.01× TPS over LLaDA-2.1/2.0. |
| [[2607.17715]] | C2KV Compressed Composable KV Cache | 4× 压缩 KV cache 即可匹配 Full Recompute，最高 17× 加速。 KDD '26 工作。 4× KV cache compression matches Full Recompute, up to 17× speedup. KDD '26. |
| [[2607.17733]] | MXSens Mixed-Precision Quantization | MXINT 格式下 W4A4KV4 在 LLaMA-2-70B 上 PPL 仅 3.77，优于传统量化。 MXINT format: W4A4KV4 LLaMA-2-70B reaches PPL 3.77, outperforming conventional quantization. |
| [[2607.17835]] | FFT IP Cores for Optical OFDM | 面向光 OFDM 的自定义 FP11/FP12 FFT 核，相对 INT16 功耗降 19.8%、面积降 12.0%。 Custom FP11/FP12 FFT cores for optical OFDM: 19.8% power reduction and 12.0% area reduction vs INT16. |
| [[2607.18101]] | Hailo-8L On-Device Training | 把商业推理加速器 Hailo-8L 复用于冻结主干的 INT8 训练，在 ResNet18/CIFAR-100 上比 CPU 基线快 15.4×。 Repurposes the Hailo-8L inference accelerator for INT8 frozen-backbone training: 15.4× CPU speedup on ResNet18/CIFAR-100. |

### C. 机制可解释性 / Mechanistic Interpretability

| ID | 标题 / Title | 一句话总结 / TL;DR |
|---|---|---|
| [[2607.17674]] | Latent Reasoning Strategies | 提出模型导向的变分目标反推潜在推理策略，Strategy Alignment 达到约 0.9–1.0。 Model-directed variational objective to infer latent reasoning strategies, Strategy Alignment ~0.9–1.0. |
| [[2607.17770]] | TMS Tversky Monosemanticity Score | 提出无标签的 SAE 评估指标 TMS，CLIP N=4 时 TMS 0.864 vs MS 0.653。 Label-free SAE evaluation metric TMS; CLIP N=4 TMS 0.864 vs MS 0.653. |
| [[2607.17621]] | AGMR Agent Memory | 基于 Mechanistic Attention 的 agent 记忆机制，平均 +21.8 点，记忆 token 减少 63%。 Mechanistic Attention for agent memory: up to +21.8 points, 63% memory token reduction. |
| [[2607.17696]] | Adjoint Lost-in-the-Middle | 为"中间丢失"现象提出伴随敏感性理论框架并定义 LIM_δ 指标（纯理论）。 Adjoint-sensitivity framework for Lost-in-the-Middle with a defined LIM_δ index (theory only). |
| [[2607.18100]] | SOPHIA Activation Steering | 把推理过程建模为 K=5 状态转移图，通过注入 crosser-minus-stayer 向量打破自循环，自循环脱离率从 25% 升至 100%。 Models reasoning as K=5 state transitions; injects crosser-minus-stayer vectors to break self-loops, lifting exit rate from 25% to 100%. |
| [[2607.18228]] | Soft Prefix Syllogistic Stability | 用可学习软前缀将原本正确的三段论判断翻转 72%–90%，主要由"宽泛语义偏好"驱动而非逻辑操作。 Learned soft prefixes flip 72%–90% of correct syllogistic judgments, driven by a broad answer preference rather than logical operations. |

### D. Agent 系统与评估 / Agent Systems & Evaluation

| ID | 标题 / Title | 一句话总结 / TL;DR |
|---|---|---|
| [[2607.17598]] | Progressive Disclosure for Long-Context Agents | 扁平化披露在 K=20 本书上以 0.462 击败原始检索的 0.257。 Flat disclosure beats raw retrieval at K=20 books (0.462 vs 0.257). |
| [[2607.17641]] | VRR-Stop Verify-Repair | 验证-修复停止准则在 GSM8K 压力测试上比固定 5 次修复高 +60.6 pp。 Verify-repair stopping criterion: +60.6 pp over fixed-5 repair on GSM8K stress. |
| [[2607.17762]] | AITE AI Telco Engineer (NVIDIA) | LLM 进化搜索设计的 OTFS 均衡器比 UAMP 快 3.6×。 LLM evolutionary search designs an OTFS equalizer 3.6× faster than UAMP. |
| [[2607.17765]] | FIFA World Cup 2026 Forecasting | 无污染基准测试显示 92% top-pick 收敛，无 agent 击败市场。 Contamination-free benchmark: 92% top-pick convergence, no agent beats the market. |
| [[2607.17948]] | AgenticABM-Schelling | 在 Schelling 模型中用一个 LLM agent 替换邻居分类规则，统计上不改变动力学但运行时间从 2s 暴涨到 8917s。 Replacing one agent's classification rule with an LLM leaves dynamics statistically unchanged but inflates runtime from 2s to 8917s. |
| [[2607.18064]] | Autoresearch with Coding Agents | 在 Quran 朗诵 ASR 任务上对比 Claude Code 与 Codex：Claude 主动泛化，Codex 靠逐行硬编码答案进行规格投机。 Compares Claude Code (generalizer) vs Codex (metric-maximizer that hardcodes answers) on a Quran-ASR autoresearch loop. |
| [[2607.18235]] | Harness Generalization | 3.1M rollout 统计分析表明复杂 discovery harness 并不普遍优于简单 Sequential Best-of-N；提出 Adaptive Harness Ensemble。 3.1M-rollout study shows no complex discovery harness beats simple Sequential Best-of-N; proposes Adaptive Harness Ensemble. |
| [[2607.17947]] | Autonomous Agency Scale (AAS) | 提出 0–5 等级、7 维度、双时间带（Active/Ambient）的 agent 自主性评估框架，并以"空闲间隔测试"区分真自主与定时规则。 Proposes a 0–5, 7-dimension, two-band (Active/Ambient) agency rubric with an Idle-Gap Test separating genuine self-direction from scheduled rules. |

### E. LLM 安全与对齐 / LLM Safety & Alignment

| ID | 标题 / Title | 一句话总结 / TL;DR |
|---|---|---|
| [[2607.17447]] | Calibrating Semantic Uncertainty | 用语义映射把 token 概率桥接到有限后验，准确率 0.885 vs 0.815。 Semantic map bridging token probabilities to finite posteriors, accuracy 0.885 vs 0.815. |
| [[2607.17890]] | STACE Concept Erasure Stress Test | 多智能体压力测试框架，SIRI 51.1% 超越最强基线 Ring-the-bell 的 45.9%。 Multi-agent stress-test for concept erasure: SIRI 51.1% beats strongest baseline Ring-the-bell at 45.9%. |
| [[2607.17986]] | Self-State Attacks on Self-Hosted Agents | 形式化 A(R)⊆L(R) 自状态攻击类，L3+B2+15 事件备份可关闭 23 个攻击单元中除 4 个外的全部。 Formalizes A(R)⊆L(R) self-state attacks; L3 permissions + B2 detection + 15-event backups close 19 of 23 attack cells. |
| [[2607.18056]] | Intern-BioBreaker Biosecurity Red-Teaming | 四阶段生物红队模型在 14 个前沿 LLM 上测得 GPT-5.5 ASR 达 60%；湿实验案例验证 DNA 序列可合成性。 Four-stage bio-red-teamer reaches 60% ASR on GPT-5.5; wet-lab-style cases show BLASTN-evading, structurally intact DNA. |
| [[2607.18063]] | Adaptive Adversaries Benchmark | 21 场景多轮多攻击者 agent 安全基准；15 轮自适应攻击把 ASR 从 0–1% 抬到 5.4–14.0%。 21-scenario multi-turn multi-attacker benchmark; 15-round adaptive attack lifts ASR from 0–1% to 5.4–14.0%. |
| [[2607.18082]] | CriPO Rubric RL Self-Distillation | 系统刻画 rubric-based RL 的 Unexplored/Suppressed Criteria 失败模式，并提出反事实优势翻转机制。 Names Unexplored/Suppressed Criteria failure modes in rubric-based RL and proposes counterfactual advantage flipping. |
| [[2607.17946]] | Annealing CoT for Value Conflicts | 从损失景观几何视角分析 RLHF 价值冲突，CoT 进一步压平 Hessian λmax（4083→1218）。 Geometric view of RLHF value conflicts; CoT further flattens top Hessian eigenvalue (4083→1218). |
| [[2607.18006]] | MADA-RL Multi-Agent Debate RL | 反事实 critic 优势 + LoRA + GRPO 把 DeepSeek-R1-Distill-Qwen-1.5B 从 39.9% 提升到 41.9%。 Counterfactual critic advantage + LoRA + GRPO lifts DeepSeek-R1-Distill-Qwen-1.5B from 39.9% to 41.9%. |

### F. RL 与学习理论 / RL & Learning Theory

| ID | 标题 / Title | 一句话总结 / TL;DR |
|---|---|---|
| [[2607.17823]] | max@k RL Theory (Bocconi) | max@k 目标下 Markovian 策略差距 ≥1.24、样本复杂度比经典 RL 多 K 倍、精确规划 NP-hard。 Under max@k, Markovian gap ≥1.24, K× sample complexity vs classical RL, exact planning is NP-hard. |
| [[2607.17922]] | PRIME Plasticity Recovery MARL | 团队级双向静默神经元判据，在 UAV 应急通信相变任务上 IQM 比 MAPPO 高 24.9%。 Team-level bidirectional silent-neuron criterion lifts IQM by 24.9% over MAPPO on UAV emergency communication. |
| [[2607.17944]] | CMP Cognitive Memory Primitive | 完全无反传的稀疏 + 局部架构，在自建 15 域文本任务上 Backward Transfer 比 online-EWC Transformer 好 15–19×。 No-backprop sparse local architecture; BWT 15–19× better than online-EWC Transformer on a 15-domain text protocol. |

### G. 视觉、多模态与 VLA / Vision, Multimodal & VLA

| ID | 标题 / Title | 一句话总结 / TL;DR |
|---|---|---|
| [[2607.17593]] | MILES Class-Incremental | 度量学习驱动的类增量学习，在 6 个基准上 SOTA，CIFAR-100 T=10 达 93.93%。 Metric learning for class-incremental learning; SOTA on 6 benchmarks, CIFAR-100 T=10 at 93.93%. |
| [[2607.17673]] | GPE Geometry-Preserving Encoders | 三模态对比学习中三角形检索在 Synthetic-XNOR 上从 0.6093 提升到 0.9952。 Trimodal contrastive geometry-preserving encoders lift Triangle retrieval 0.6093→0.9952 on Synthetic-XNOR. |
| [[2607.17786]] | VLA Cross-Stage Robustness | RD-VLA 在高斯噪声下崩塌至 14.8%，揭示隐式迭代推理范式的结构性脆弱。 RD-VLA collapses to 14.8% SR under Gaussian noise, revealing structural fragility of latent-iterative reasoning. |
| [[2607.17902]] | MeSH-Rel-4K Biomedical Ontology | LoRA 微调把 5 个 ≤9B 小模型平均 F1 从 0.548 提升到 0.889，gemma-9b 达 91.6%。 LoRA fine-tuning lifts average F1 from 0.548 to 0.889 across 5 ≤9B small models; gemma-9b reaches 91.6%. |

### H. 硬件、系统与基础设施 / Hardware, Systems & Infrastructure

| ID | 标题 / Title | 一句话总结 / TL;DR |
|---|---|---|
| [[2607.17525]] | FailureAtlas LLM Gateway | LLM 网关失败分类法，5×2 Layer×Detectability 矩阵，揭示静默 HTTP-200 失败。 Taxonomy of LLM gateway failures; 5×2 Layer×Detectability matrix exposes silent HTTP-200 failures. |
| [[2607.17899]] | SEAM-V RISC-V Vector Processor | 混合解耦 RVV 架构使 17 个内核取得 1.34× 几何平均加速比，AVL=32 时接近 3×。 Hybrid-decoupled RVV processor: 1.34× geomean speedup across 17 kernels, approaching 3× at AVL=32. |
| [[2607.17979]] | Harness Engineering for GPU Kernels | 在 MLSys 2026 FlashInfer 竞赛 5 个算子上相对 FlashInfer 基线取得 1.12×–29.68× 加速。 Agent-assisted harness engineering yields 1.12×–29.68× speedup over FlashInfer baselines on 5 contest operators. |
| [[2607.18069]] | Hardware AI Throttling | 提出 GPU L2/shared memory 微架构节流旋钮，1/8 资源时最高削减 80% 性能，硬件成本 <10K FF。 GPU L2/shared-memory microarchitectural throttling knobs cut up to 80% performance at 1/8 resource, <10K FF cost. |

### I. 其他 / Other

| ID | 标题 / Title | 一句话总结 / TL;DR |
|---|---|---|
| [[2607.17624]] | Can Transformers Really Do It All? | 通过样条激活搜索在算法任务上获得 2–3× 加速（ICLR 2026）。 Spline activation search yields 2–3× speedup on algorithmic tasks (ICLR 2026). |

---

## All Papers

| ID | 标题 / Title | 主题 / Topic | 一句话总结 / TL;DR |
|---|---|---|---|
| [[2607.17447]] | Calibrating Semantic Uncertainty | LLM Safety | 用语义映射把 token 概率桥接到有限后验，准确率 0.885 vs 0.815。 Semantic map bridging token probabilities to finite posteriors, accuracy 0.885 vs 0.815. |
| [[2607.17513]] | HySAT Hyperbolic Expert AI | Training | 只在损失层使用 Lorentz 几何，在 17.95M 样本上 0 NaN。 Lorentz geometry at the loss layer only: 0 NaN across 17.95M samples. |
| [[2607.17525]] | FailureAtlas LLM Gateway | Infrastructure | LLM 网关失败分类法，5×2 矩阵揭示静默 HTTP-200 失败。 Taxonomy of LLM gateway failures; 5×2 matrix exposes silent HTTP-200 failures. |
| [[2607.17593]] | MILES Class-Incremental | Vision | 类增量度量学习，6 基准 SOTA，CIFAR-100 T=10 达 93.93%。 Metric learning class-incremental; SOTA on 6 benchmarks, 93.93% on CIFAR-100 T=10. |
| [[2607.17595]] | Sub-Gaussian SA Concentration | RL Theory | 压缩型随机逼近的第一个次高斯极大值界。 First sub-Gaussian maximal concentration bound for contractive SA. |
| [[2607.17598]] | Progressive Disclosure Agents | Agents | 扁平化披露在 K=20 本书上 0.462 vs 0.257。 Flat disclosure beats raw retrieval at K=20 books (0.462 vs 0.257). |
| [[2607.17607]] | OCO → Nonconvex | Training | 解决 Chen-Hazan 2024 开放问题，给出 O(T⁻¹/²) 和 O(T⁻²/⁷) 收敛率。 Resolves Chen-Hazan 2024 open problem with O(T⁻¹/²) and O(T⁻²/⁷) rates. |
| [[2607.17620]] | PoLoRA | Training | LoRA 作为低秩优化器状态，1.2–1.7× 快于 Adam，学习率跨 rank 迁移。 LoRA as low-rank optimizer state, 1.2–1.7× faster than Adam, LR transfers across ranks. |
| [[2607.17621]] | AGMR Agent Memory | Interpretability | Mechanistic Attention 的 agent 记忆，+21.8 点，token 减少 63%。 Mechanistic Attention for agent memory: +21.8 points, 63% token reduction. |
| [[2607.17624]] | Can Transformers Really Do It All? | Other | 样条激活搜索在算法任务上 2–3× 加速（ICLR 2026）。 Spline activation search, 2–3× speedup on algorithmic tasks (ICLR 2026). |
| [[2607.17641]] | VRR-Stop Verify-Repair | Agents | 验证-修复停止准则，GSM8K 压力测试上 +60.6 pp。 Verify-repair stopping criterion, +60.6 pp on GSM8K stress. |
| [[2607.17652]] | FlowBlock Diffusion LLM | Inference | 波前并行解码，2.95×/4.01× TPS over LLaDA-2.1/2.0。 Wavefront-parallel decoding, 2.95×/4.01× TPS over LLaDA-2.1/2.0. |
| [[2607.17673]] | GPE Trimodal Encoders | Vision | 三角形检索 0.6093→0.9952 on Synthetic-XNOR。 Triangle retrieval 0.6093→0.9952 on Synthetic-XNOR. |
| [[2607.17674]] | Latent Reasoning Strategies | Interpretability | 模型导向变分目标反推推理策略，Alignment ~0.9–1.0。 Model-directed variational objective for latent strategies, Alignment ~0.9–1.0. |
| [[2607.17696]] | Adjoint Lost-in-the-Middle | Interpretability | 伴随敏感性理论框架 + LIM_δ 指标（纯理论）。 Adjoint-sensitivity framework + LIM_δ index (theory only). |
| [[2607.17715]] | C2KV KV Cache | Inference | 4× 压缩匹配 Full Recompute，最高 17× 加速。 KDD '26。 4× compression matches Full Recompute, up to 17× speedup. KDD '26. |
| [[2607.17733]] | MXSens Quantization | Inference | MXINT 格式 W4A4KV4 LLaMA-2-70B PPL 3.77。 MXINT format W4A4KV4 LLaMA-2-70B PPL 3.77. |
| [[2607.17762]] | AITE AI Telco Engineer | Agents | LLM 进化搜索 OTFS 均衡器比 UAMP 快 3.6×。 LLM evolutionary search OTFS equalizer 3.6× faster than UAMP. |
| [[2607.17765]] | FIFA World Cup 2026 | Agents | 无污染基准 92% top-pick 收敛，无 agent 击败市场。 Contamination-free: 92% top-pick convergence, no agent beats the market. |
| [[2607.17770]] | TMS Monosemanticity Score | Interpretability | 无标签 SAE 指标 TMS，CLIP N=4 时 0.864 vs MS 0.653。 Label-free SAE metric TMS, CLIP N=4 TMS 0.864 vs MS 0.653. |
| [[2607.17786]] | VLA Cross-Stage Robustness | Vision | RD-VLA 高斯噪声下崩塌至 14.8%，结构性脆弱。 RD-VLA collapses to 14.8% under Gaussian noise, structural fragility. |
| [[2607.17822]] | MRSNorm Phasor Attention | Training | 2D 相量配对，参数减半，CIFAR-100 压力测试下稳定。 2D phasor pairing, halved parameters, stable under CIFAR-100 stress. |
| [[2607.17823]] | max@k RL Theory | RL Theory | Markovian 差距 ≥1.24，K× 样本复杂度，NP-hard。 Markovian gap ≥1.24, K× sample complexity, NP-hard. |
| [[2607.17835]] | FFT IP Cores Optical OFDM | Inference | FP11/FP12 FFT 核功耗降 19.8%、面积降 12.0% vs INT16。 FP11/FP12 FFT cores: 19.8% power, 12.0% area reduction vs INT16. |
| [[2607.17843]] | Möbius Learning | Training | 循环深度折叠分布式训练，L≥6 时优于 ordered-loop（Δ≤−0.0059）。 Cyclic depth-folding distributed training, beats ordered-loop at L≥6 (Δ≤−0.0059). |
| [[2607.17890]] | STACE Concept Erasure | Safety | 多智能体压力测试 SIRI 51.1% vs 45.9% 最强基线。 Multi-agent stress-test SIRI 51.1% vs 45.9% strongest baseline. |
| [[2607.17899]] | SEAM-V RISC-V Vector | Infrastructure | 混合解耦 RVV 1.34× geomean 加速，AVL=32 接近 3×。 Hybrid-decoupled RVV 1.34× geomean speedup, ~3× at AVL=32. |
| [[2607.17902]] | MeSH-Rel-4K Biomedical | Vision | LoRA 微调 F1 从 0.548 提升到 0.889，gemma-9b 达 91.6%。 LoRA fine-tuning lifts F1 from 0.548 to 0.889; gemma-9b reaches 91.6%. |
| [[2607.17913]] | AE-PSL Split Learning | Training | 自编码器压缩的并行拆分学习，10.2× 通信压缩无精度损失。 Autoencoder-compressed parallel split learning, 10.2× compression with no accuracy loss. |
| [[2607.17922]] | PRIME Plasticity MARL | RL Theory | 团队级双向静默神经元，UAV 应急通信 IQM +24.9%。 Team-level bidirectional silent neurons, +24.9% IQM on UAV emergency comms. |
| [[2607.17944]] | CMP Cognitive Memory Primitive | RL Theory | 无反传稀疏局部架构，BWT 比 online-EWC 好 15–19×。 No-backprop sparse local architecture, BWT 15–19× better than online-EWC. |
| [[2607.17946]] | Annealing CoT Value Conflicts | Safety | CoT 把 Hessian λmax 从 4083 降至 1218，MMLU 道德场景 +17.0 绝对。 CoT drops top Hessian eigenvalue 4083→1218, +17.0 absolute on MMLU Moral Scenarios. |
| [[2607.17947]] | Autonomous Agency Scale | Agents | 0–5/7 维/双时间带 agent 自主性评估，含 Idle-Gap Test。 0–5/7-dim/two-band agency rubric with Idle-Gap Test. |
| [[2607.17948]] | AgenticABM-Schelling | Agents | 单 LLM agent 替换邻居分类规则，动力学不变但运行时间 2s→8917s。 Single LLM agent in Schelling: dynamics unchanged but runtime 2s→8917s. |
| [[2607.17979]] | Harness Engineering GPU Kernels | Infrastructure | FlashInfer 竞赛 5 算子 1.12×–29.68× 加速，优于 Full-Agent。 FlashInfer contest 5 operators 1.12×–29.68× speedup, beats Full-Agent. |
| [[2607.17986]] | Self-State Attacks | Safety | A(R)⊆L(R) 自状态攻击，L3+B2+备份关闭 19/23 攻击单元。 A(R)⊆L(R) self-state attacks; L3+B2+backups close 19/23 attack cells. |
| [[2607.18006]] | MADA-RL Debate RL | Safety | 反事实 critic 优势 + LoRA + GRPO，平均 F1 39.9%→41.9%。 Counterfactual critic advantage + LoRA + GRPO, average F1 39.9%→41.9%. |
| [[2607.18056]] | Intern-BioBreaker Biosecurity | Safety | 四阶段生物红队，GPT-5.5 ASR 60%；湿实验案例验证 DNA 可合成性。 Four-stage bio-red-teamer, GPT-5.5 ASR 60%; wet-lab-style cases show synthesizable DNA. |
| [[2607.18063]] | Adaptive Adversaries Benchmark | Safety | 21 场景多轮多攻击者基准，ASR 0–1%→5.4–14.0%。 21-scenario multi-turn multi-attacker benchmark, ASR 0–1%→5.4–14.0%. |
| [[2607.18064]] | Autoresearch Coding Agents | Agents | Claude=generalizer vs Codex=metric-maximizer（硬编码答案）；harness 设计 5 规则。 Claude (generalizer) vs Codex (metric-maximizer that hardcodes); 5 harness design rules. |
| [[2607.18069]] | Hardware AI Throttling | Infrastructure | GPU L2/SMEM 节流旋钮，1/8 资源时 −80% 性能，<10K FF。 GPU L2/SMEM throttling knobs, −80% performance at 1/8 resource, <10K FF. |
| [[2607.18082]] | CriPO Rubric RL | Safety | 命名 Unexplored/Suppressed Criteria 失败模式 + 反事实优势翻转。 Names Unexplored/Suppressed Criteria failure modes + counterfactual advantage flipping. |
| [[2607.18100]] | SOPHIA Activation Steering | Interpretability | K=5 状态转移 + crosser-minus-stayer 向量，自循环脱离 25%→100%。 K=5 transitions + crosser-minus-stayer vectors, self-loop exit 25%→100%. |
| [[2607.18101]] | Hailo-8L On-Device Training | Inference | 商业推理加速器复用于训练，ResNet18/CIFAR-100 比 CPU 快 15.4×。 Commercial inference accelerator repurposed for training, 15.4× CPU speedup on ResNet18/CIFAR-100. |
| [[2607.18114]] | Sycophancy Representations | Training | 5 家族 × 7 偏置三角验证，偏置由对齐微调而非预训练安装。 5-family × 7-bias triangulation; biases installed by alignment tuning, not pretraining. |
| [[2607.18130]] | mHC-PEFT | Training | Manifold-Constrained Hyper-Connections 作为新 PEFT 轴；identity 残差在 finetuning 中更优。 mHC as a new PEFT axis; identity residual mixing helps in finetuning. |
| [[2607.18228]] | Soft Prefix Syllogistic Stability | Interpretability | 软前缀翻转 72%–90% 正确三段论判断，由宽泛语义偏好驱动。 Soft prefixes flip 72%–90% of correct syllogistic judgments, driven by broad answer preference. |
| [[2607.18235]] | Harness Generalization | Agents | 3.1M rollout 显示复杂 discovery harness 不普遍优于 Sequential Best-of-N。 3.1M-rollout study: complex discovery harnesses do not universally beat Sequential Best-of-N. |

---

## 验证 / Verification

- overview 中列出的论文数 / Papers listed in overview: **48**
- 目录中实际 `.md` 文件数（去除 overview.md 与 `._` AppleDouble 文件）/ Actual `.md` files in directory (excluding overview.md and `._` AppleDouble files): **48**
- 状态 / Status: ✅ 一致 / Match
