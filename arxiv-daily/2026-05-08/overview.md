---
title: "Daily Paper Overview - 2026-05-08"
date: 2026-05-08
tags: [daily-overview, arxiv, mechanistic-interpretability, activation-steering, llm-reasoning, optimization, quantization, evaluation, rlvr]
papers_count: 50
---

今日 50 篇论文以"机械可解释性 + 激活引导"和"LLM 训练/推理效率"两大主题为核心：一方面涌现出大量针对失败模式（过度思考、纠错抑制、智能体漂移、注意力汇）的几何与因果分析，并伴随多种激活引导新方法（FLAS、TACT、PrOSV、SKOP、Memory Inception、CDS/DPA）；另一方面在优化理论（SignSGD/Muon 下界、KL-Shampoo、SNR-LR 校准、Villani 损失）、低精度训练（nGPT NVFP4、RHT 量化证明）与 RL 推理（ReasonMaxxer、TRICE、RLVR 低秩动力学）上有突破性进展，同时多篇评测可靠性论文（SIREN、DBE、PIS、CITE、DAPRO）也提醒社区当前基准的统计有效性令人担忧。

Today's 50 papers cluster around two themes: (1) deep mechanistic / geometric analyses of LLM failure modes (overthinking, correction suppression, agent drift, attention sinks) paired with a wave of new activation-steering techniques (FLAS, TACT, PrOSV, SKOP, Memory Inception, CDS/DPA); and (2) breakthroughs in training/inference efficiency, including provably-tight bounds for SignSGD/Muon, principled module-wise SNR-aware learning rates, NVFP4-native normalized architectures, randomized Hadamard quantization theory, and RL-free reasoning recipes (ReasonMaxxer, TRICE). A notable third strand is reliability-of-evaluation critiques (SIREN winner's curse, DBE adaptive IRT, Policy Invariance scoring, CITE sequential certification, DAPRO dynamic safety budgets) that question whether current LLM leaderboards measure what they claim.

## 今日必读 / Must Read Today

- **[[2605.06241]] Rethinking RL for LLM Reasoning: It's Sparse Policy Selection, Not Capability Learning** — 本文用 oracle 干预和熵分析因果地证明 RLVR 仅在 1–3% 的高熵决策 token 上重排策略，并据此提出 ReasonMaxxer，用 LoRA 对比损失以 $4–$25 的训练成本匹配甚至超过耗资数千美元的 RL checkpoint。 / The paper argues RLVR doesn't teach new reasoning — it reranks plausibilities at sparse "decision tokens," and ships an RL-free LoRA recipe that reaches RL-checkpoint performance across 6 math benchmarks at roughly three orders of magnitude lower training cost, which—if it holds up—reframes a substantial portion of current RL-for-reasoning work.

- **[[2605.06326]] Teaching Thinking Models to Reason with Tools (TRICE)** — TRICE 提出工具集成推理的全流程训练配方（数据筛选 + 混合轨迹 SFT + 路由回放 RLVR），将 Qwen3 thinking 模型改造为真正会交错调用 Python 沙箱的推理器，AIME 2025 上 4B/30B 分别达到 96.7%/99.2% 的开源 SOTA。 / TRICE delivers a four-part pipeline (tool-advantaged data curation, mixed-trajectory SFT, routing-replay-stabilized on-policy RLVR) that fixes the well-known "thinking models refuse to actually use the tool" pathology, setting new open-source AIME 2025 records while preserving no-tool performance.

- **[[2605.06067]] Normalized Architectures are Natively 4-Bit** — NVIDIA 论文证明 nGPT（超球面归一化 Transformer）在 NVFP4 训练下天然获得约 7 dB 的点积信噪比优势，无需 Randomized Hadamard Transform 或逐张量缩放，1.2B 稠密及 3B/30B 混合 MoE 上验证有效，Blackwell 上吞吐量提升至 3.6×。 / This NVIDIA work shifts low-precision robustness from being an algorithmic patch (RHT, dynamic scaling) to an architectural property — the hyperspherical normalization makes signal accumulate coherently across dimensions, giving lower validation loss than standard GPT under NVFP4 at scales up to a 30B hybrid Mamba-Transformer MoE.

## 按主题分类 / Papers by Topic

### 机制可解释性与激活引导 / Mechanistic Interpretability & Activation Steering

| Paper | 主题 / Topic | 简介 / TL;DR |
|---|---|---|
| [[2605.05715v1]] Decodable but Not Corrected | 失败模式纠缠 / Failure-mode entanglement | 医学 QA 的"过度思考"信号可被线性探针以 71.6% 解码但 29 种固定线性引导均无效 (Δ≈0) / OT failure is linearly decodable yet unsteerable due to 88% representational entanglement with task-relevant directions. |
| [[2605.05741v1]] HyperLens | 置信度轨迹 / Confidence trajectory | 利用未来 m 层 Transformer 自放大机制构造高分辨率置信度探针并发现 SFT 会诱发"盲目自信" / A parameter-free probe routing hidden states through future layers reveals SFT shrinks the "struggle phase" and mechanistically links it to post-SFT degradation. |
| [[2605.05892v1]] FLAS Flow-based Activation Steering | 流匹配引导 / Flow-based steering | 用概念条件速度场替代固定方向引导向量，AxBench 上首次以学习方法超越 in-context prompting / FLAS replaces fixed steering vectors with multi-step learned velocity fields, beating prompting on Gemma-2-2B/9B with <1/26 the parameters of HyperSteer. |
| [[2605.05957v1]] Knowing but Not Correcting | 纠错抑制 / Correction suppression | 任务请求会抑制 LLM 对虚假前提的纠正（19–90%），并提出 CDS/DPA 两种免训练干预把 Qwen3.5-9B 纠错率从 0% 提到 58.2% / Routine task wrappers suppress factual correction in 8 LLMs; training-free direction-steering and dynamic payload amplification restore it. |
| [[2605.05980v1]] TACT | 智能体漂移引导 / Agent drift steering | 在 `</think>` token 提取过度推理 / 过度行动两条正交方向，SWE-bench Verified 解决率 +5.8pp、步数 -26% / Training-free residual-stream steering of coding agents reduces overthinking and overacting along orthogonalized directions. |
| [[2605.05983v1]] PrOSV Prompt-Only Steering Vectors | 提示位引导 / Prompt-only steering | 联合训练方向 + 因子且仅干预少量 prompt token，AxBench 上 SOTA，算术能力下降仅 18–29%（FSSV 为 68–90%） / Scaling-theory-driven joint training of steering factor/direction restricted to a few prompt tokens preserves utility far better than full-sequence SVs. |
| [[2605.06076v1]] Static Mechanistic Localization Pitfalls | 电路自由演化 / Circuit free evolution | SFT 期间 attention 主导的技能电路会显著迁移，使静态定位等价于随机选择 / Attention skill circuits drift continuously under SFT, breaking the "locate-then-update" paradigm except for stable MLP knowledge circuits. |
| [[2605.06196v1]] The Granularity Axis | 角色粒度方向 / Role granularity | Qwen3-8B 隐层存在一条线性"粒度轴"（PC1 余弦 0.972）排列微观→宏观社会角色，可因果引导 / A single linear "Granularity Axis" organizes prompted social roles from individuals to institutions and is causally controllable via steering. |
| [[2605.06225]] Memory Inception | KV 缓存引导 / KV-cache steering | 将文本描述符编码为潜在 KV 记忆槽并注入选定注意力层，比 prompt 节省 6–118× KV 存储，且超越 CAA / Latent KV memory injection at auto-selected layers beats CAA on dialogue/personality/reasoning while remaining invisible in transcripts. |
| [[2605.06342]] SKOP Key-Orthogonal Projections | 注意力 rerouting 修复 / Attention rerouting fix | 将引导向量投影到关键差异方向正交子空间，保留 95% 引导效果同时实用性损失降低 5–7× / Projecting steering vectors orthogonal to harmful focus→tail attention shifts is the only method working in 16K-token retrieval. |
| [[2605.06458]] Invariant Features in LLMs | 不变子空间 / Invariant subspace | 用广义特征值分解分离语义不变子空间与表面形式干扰子空间，9 模型零样本归因 >92% / Contrastive sensitivity decomposition separates invariant and nuisance subspaces and enables high-accuracy model attribution. |
| [[2605.06480]] Patch-Effect Graph Kernels | 电路图核 / Circuit graph kernels | 将激活修补结果转为图并用 WL/谱核分类，GPT-2 Small IOI 上局部边特征完美分类 / Activation-patching profiles are converted to "patch-effect graphs" and classified via graph kernels for circuit comparison. |
| [[2605.06494]] WL Analysis of SAE Features | SAE 特征图核 / SAE feature graphs | 把 SAE 特征表示为词元共现图并用 WL 核聚类，恢复解码器余弦聚类完全错过的字母簇 / Token co-occurrence graphs reveal SAE motif families invisible to decoder-cosine clustering, complementing token-histogram baselines. |
| [[2605.06610]] SoftSAE | 自适应稀疏度 SAE / Adaptive sparsity SAE | 用可微 Soft Top-K 算子让 SAE 按输入语义复杂度预测每输入的 k̂，特征分离性优于 TopK/BatchTopK / SoftSAE adapts per-input sparsity via a learned MLP, improving feature absorption/splitting and SCR/TPP at higher sparsity. |
| [[2605.06611]] Attention Sink Structural Origin | 注意力汇成因 / Attention sink cause | 因果掩码 → 方差差异 → FFN 超级神经元 → 维度不平衡 → QK 锁定首 token，Head-wise RMSNorm 修复并加速预训练 / A complete causal chain explains attention sinks; head-wise RMSNorm fixes it and gives faster pretraining than standard Softmax attention. |
| [[2605.06632]] Crafting Reversible SFT Behaviors | 稀疏行为载体 / Sparse behavioral carriers | LCDD 训练时把 SFT 行为压缩进稀疏子网络，SFT-Eraser 推理时用软触发器无权重修改逆转该行为 / SFT behaviors can be concentrated into sparse carriers (73–84% sparsity) and erased at inference via soft triggers across 12 model-task combos. |

### 优化与训练动力学 / Optimization & Training Dynamics

| Paper | 主题 / Topic | 简介 / TL;DR |
|---|---|---|
| [[2605.05794]] MoLS Module-wise LR via SNR | 模块 SNR 校准 / Module SNR calibration | 预热阶段一次性估计各模块梯度信噪比并自动缩放学习率，LLaMA 60M–7B PPL 降 0.84–1.82 / Detects systematic SNR imbalance across Transformer modules and corrects Adam underupdates with <2% overhead. |
| [[2605.06152v1]] Slingshot via Numerical Feature Inflation | 损失尖峰浮点根因 / Loss-spike numerics | 证明 float32 softmax 吸收误差是 Slingshot 损失尖峰直接成因，升至 float64 完全消除 / Softmax Collapse + Neural Collapse produce a deterministic global-mean feedback loop driving spikes; mitigations include larger Adam ε or BN. |
| [[2605.06316]] Pro-KLShampoo | 二阶预条件器 / Second-order preconditioner | 利用 KL-Shampoo 谱"尖峰-平坦"结构，将一因子限制在低秩 + 正交化补集，挂钟时间最多省 13% / Combines a low-rank parametric Kronecker factor with Muon-style orthogonalization for memory- and time-efficient LLM pretraining. |
| [[2605.06523]] RLVR Implicit Reward Overfitting | RLVR 低秩动力学 / RLVR low-rank dynamics | 周期性秩-1替换实验证明 RLVR 推理增益几乎全部集中在 ΔW 秩-1 分量，非秩-1 仅虚高奖励 / Reasoning gains live in the rank-1 component of RLVR ΔW; non-rank-1 inflates train reward without improving test generalization. |
| [[2605.06563]] Criticality and Saturation in Orthogonal NNs | 正交初始化有限宽度 / Orthogonal NN theory | 用 Weingarten 演算 + 费曼图首次解析推导正交 MLP 的逐层递归，解释了正交初始化大深度饱和现象 / First analytic finite-width theory for orthogonal MLPs proves criticality preserves to finite width and explains long-observed saturation. |
| [[2605.06599v1]] Weight-Decay Turns Loss Landscapes Villani | Villani 损失景观 / Villani landscape | 严格证明 Transformer + L² 权重衰减满足 Villani 函数三条件，给出对数-Sobolev 常数与 PAC-Bayes 界 / First rigorous Villani-function characterization of weight-decayed Transformer losses, validated empirically on GPT-Neo-125M. |
| [[2605.06611]] Attention Sink Structural Origin* | 见上方 / See above | (Cross-listed) |
| [[2605.06615]] SignSGD Tight Lower Bounds | SignSGD/Muon 紧界 / SignSGD bounds | ℓ∞ 光滑、坐标可分离噪声下首次给出 SignSGD 紧下界，稀疏噪声时样本复杂度比 SGD 低 d 倍，推广到 Muon / Provides matching upper/lower bounds for SignSGD and the first dimension-free lower bound for Muon, validated on nanoGPT-124M. |
| [[2605.06654]] Optimizer-Model Consistency | 优化器一致性 / Optimizer consistency | SFT 时用与预训练同族优化器全参数微调最能减少遗忘，Muon 在推理 SFT 上反而劣于 AdamW / Full finetuning with the pretraining optimizer family maximizes the learning-forgetting Pareto frontier; Muon's pretraining advantage can vanish in SFT. |
| [[2605.06169v1]] MV-Split Residuals / Mean Mode Screaming | 超深 DiT 稳定 / Ultra-deep DiT | 解耦均值子空间与中心化子空间的残差增益，根治均值主导崩溃，1000 层 DiT 首次稳定训练 / Decoupled residual gains for mean / centered subspaces eliminate "Mean Mode Screaming" collapse in 400–1000-layer DiTs. |

### 高效推理与量化 / Efficient Inference & Quantization

| Paper | 主题 / Topic | 简介 / TL;DR |
|---|---|---|
| [[2605.05819v1]] HCInfer | 异构 CPU-GPU 补偿 / Heterogeneous compensation | CPU 异步运行 LoRA 误差补偿、GPU 跑量化主干，敏感度感知动态秩分配，RTX 4090 上精度提 5.2%、吞吐 10.4× / Offloads LoRA-style quantization-error compensation to CPU with sensitivity-aware dynamic rank allocation. |
| [[2605.06014]] RHT Quantization Theory | 哈达玛量化证明 / RHT proof | 首次证明 2-RHT 足以恢复 URR 标量量化保证（O(d^{-1/2})），向量量化需 3-RHT / Two Randomized Hadamard Transforms suffice for DRIVE/QUIC-FL scalar quantization; three are needed for sparse-input vector quantization. |
| [[2605.06052v1]] XtraMAC | FPGA 混合精度 MAC / FPGA mixed-precision MAC | 证明所有 INT/FP MAC 可化为共享整数尾数乘积，单 DSP 打包多通道，1.2× 延迟、1.9× 能效胜 H100 GEMV / Unified-mantissa FPGA MAC handles INT4×BF16, FP8×BF16, etc. with runtime datatype switching and 1.4–2.0× density gain. |
| [[2605.06067]] Normalized Architectures are Natively 4-Bit | nGPT NVFP4 训练 / nGPT NVFP4 | 见上方 / See Must-Read above. |
| [[2605.06082]] PoTAcc | PoT 量化 FPGA / PoT FPGA pipeline | 首个开源 PoT 量化端到端流水线（PyTorch/TF → shift-PE FPGA），PYNQ-Z2 上 3.6× 加速、78% 能耗降低 / Open-source PoT pipeline with shift-PE VSAC accelerators, <2% accuracy loss, three PoT schemes (QKeras/MSQ/APoT). |
| [[2605.06366v1]] Layer Collapse in Diffusion LMs | DLM 超级离群值 / DLM super-outliers | LLaDA-8B 单一激活通道支配前半层，剔除后模型完全崩溃；DLM 早层比 AR 更冗余、3-bit 量化仅掉 1.8% / First systematic activation-dynamics analysis of DLMs reveals super-outlier channel, inverted redundancy pattern, and high compression robustness. |

### LLM 推理、RL 与训练后处理 / LLM Reasoning, RL & Post-training

| Paper | 主题 / Topic | 简介 / TL;DR |
|---|---|---|
| [[2605.05873]] CITE Anytime-Valid Self-Consistency | 序列认证 / Sequential certification | 用 e-process 交叉联合检验为 LLM 自洽性提供任意时刻有效的众数认证，停止时间不依赖类别数 / Anytime-valid mode certification combining pairwise e-process, target LCB, and unseen-category UB with category-set-size-independent stopping. |
| [[2605.06241]] ReasonMaxxer | 稀疏策略选择 / Sparse policy selection | 见上方 / See Must-Read above. |
| [[2605.06326]] TRICE Tool-Integrated Reasoning | 工具集成推理 / Tool-integrated reasoning | 见上方 / See Must-Read above. |
| [[2605.06597]] UniSD Self-Distillation | 统一自蒸馏 / Unified self-distillation | 多教师一致性 + EMA + token 对比 + 特征匹配 + 散度裁剪，无外部教师 Qwen2.5-7B +5.4 / Modular self-distillation framework outperforms GKD by +2.8 across 6 benchmarks and 3 model families. |
| [[2605.06308]] Black-Box Trajectory Confidence (C+G+V) | CoT 轨迹置信度 / CoT trajectory confidence | 把 CoT 嵌入为滑窗轨迹并测量对答案锚点的几何收敛，K=4 时 AUC 超过 K=8 自洽投票，省 45–55% API 成本 / Geometry + Coverage + Verbalization black-box confidence on MedQA/GPQA/MMLU-Pro with Gemini 3.1 Pro and Claude Sonnet 4.6. |
| [[2605.06605]] DAPRO Dynamic Jailbreak Budgets | 动态安全预算 / Dynamic safety budgets | 在线策略动态分配多轮越狱评估预算，给出比静态方法方差更低、覆盖更准的"时间到不安全采样" LPB / Distribution-free conformal lower bounds with dynamic budget allocation across jailbreak/toxicity/agentic/RAG tasks. |

### 评测可靠性与基准设计 / Evaluation Reliability & Benchmarks

| Paper | 主题 / Topic | 简介 / TL;DR |
|---|---|---|
| [[2605.05973]] SIREN Winner's Curse | 自适应基准纠偏 / Adaptive benchmark debias | 冻结候选 + 重复分裂 + Gaussian multiplier bootstrap 校正 prompt 搜索后的乐观偏差，MMLU-Pro 上偏差从 +1–4pp 压到 ±0.21pp / Post-search reporting protocol with selection-aware CLT that recovers true tune-then-deploy performance. |
| [[2605.06161]] Policy Invariance for Safety Judges | 裁判策略不变性 / Judge policy invariance | 提出 Policy Invariance Score（PIS）量化裁判对语义等价改写的稳健性，四个模型 PIS 跨度 20× 而准确率排行榜不可见 / Reveals 9.1% verdict flips on rewrites and 32–71% on threshold shifts; introduces PIS and Judge Card reporting. |
| [[2605.06213v1]] Dynamic Boundary Evaluation (DBE) | 自适应 IRT 评测 / Adaptive IRT eval | Rasch IRT + SGBS 在模型决策边界自适应生成评测项，难度估计 ρ≥0.96，能力误差 0.032 logit / NeurIPS 2026 D&B Track adaptive evaluation framework that solves benchmark ceiling/floor effects. |
| [[2605.06283]] Rubric Modifications and Human-Autorater Agreement | 评分规则修改 / Rubric design | 系统量化加示例 / 分解整体到分析 / 减少偏差等规则修改对 GPT-4o 与 Llama 评分一致性的因果效应 / Adding examples/context improves human-autorater agreement; higher rubric complexity and conservative aggregation reduce it. |
| [[2605.06327]] Evaluation-Context Divergence | 评测情境偏移 / Eval vs deploy divergence | 配对提示协议显示 OLMo-3-Instruct 评估时拒绝率 +11.8pp，Mistral/Phi/Llama 反呈"部署谨慎"，对齐流水线差异系根因 / Cross-model heterogeneity in evaluation-vs-deployment behavior; matched base/instruct ablation pinpoints post-training as the inversion stage. |
| [[2605.06656]] Why Global LLM Leaderboards Are Misleading | 排行榜异质性 / Leaderboard portfolios | 全局 BT 排名仅可靠预测 10.3% 投票；用 (λ,ν)-portfolio 5 个 BT 排名即可覆盖 96% 偏好 / Set-cover-based small portfolios beat global leaderboards on Arena (89K votes, 116 languages) and reveal blind spots on COMPAS fairness. |

### 理论、安全与其他 / Theory, Safety, and Others

| Paper | 主题 / Topic | 简介 / TL;DR |
|---|---|---|
| [[2605.06017]] MDC Concentration | 自回归集中度 / Autoregressive concentration | 矩阵解耦集中度框架用因果解析矩阵编码依赖，消除稀疏序列奖励的 O(N) 方差代理膨胀 / Dimension-free O(1) concentration bounds for sparse long-context rewards in autoregressive LLMs (RLHF-relevant). |
| [[2605.06295v1]] METAGAME Meta-attributions | 二阶交互归因 / Second-order attributions | 把任意一阶归因方法本身视为合作博弈并求 Shapley 值，得到方向性二阶交互指标 / Meta-Shapley unifies STII/SOP and improves interaction recognition on CLIP/SigLIP-2 and ConceptAttention on diffusion models. |
| [[2605.06322]] SMolLM Weight-Shared Molecular Transformer | 权重共享化学语法 / Weight-shared chemistry | 53K 参数循环 Transformer 在 ZINC-250K 上 SMILES 有效率 95.3%，按"括号→环→化合价"逐步习得化学语法 / Looped 8-pass transformer mechanistically learns SMILES grammar layer-by-layer, with a single causal bracket-matching head at pass 1. |
| [[2605.06352]] Topological Signatures of Grokking | Grokking 拓扑特征 / Grokking topology | 模块化算术中泛化阶段伴随 H₁ 持续性的显著跃升，跨 Transformer/MLP 一致 / Persistent homology reveals architecture-agnostic topological signature of grokking, tracking generalization rather than memorization. |
| [[2605.06357]] MEFA Full-Gradient Attacks | 扩散净化全梯度攻击 / Diffusion purification attacks | 用梯度检查点将扩散/EBM 净化全梯度白盒攻击内存降到 O(1)，DiffPure 鲁棒性从 61% 降到 43% / Reveals reported robustness of stochastic purification defenses is largely an artifact of weak approximate gradients. |
| [[2605.06505]] PACZero PAC-Private Fine-Tuning | PAC 隐私 ZO / PAC-private ZO | 对子集聚合零阶梯度做符号量化实现 PAC 隐私，PACZero-ZPL 在 I=0 下 SST-2 OPT-1.3B 达 88.99% / Subset-aggregated sign-quantized ZO mechanism with information-theoretic free release on unanimity steps. |
| [[2605.06519]] Data Reconstruction Finite-Width Guarantees | 数据重建理论 / Reconstruction theory | 首次给出随机特征模型有限宽度下的数据重建 PAC 风格保证，CIFAR-10 上子空间感知算法优于全空间 / Width requirement scales with intrinsic data dimension r, not ambient d, enabling efficient weight-based reconstruction. |

## All Papers

| Paper | Authors | 简介 / TL;DR |
|---|---|---|
| [[2605.05715v1]] Decodable but Not Corrected (Medical OT Steering) | Ming Liu | 医学 QA"过度思考"线性可解码但 29 种固定线性引导均失效，揭示表征纠缠机制。 / Overthinking is decodable at 71.6% yet unsteerable due to 88% representational entanglement; same probe enables abstention at AUROC 0.610. |
| [[2605.05741v1]] HyperLens Cognitive Effort | Chengda Lu et al. | 用焦点深度构造高分辨率置信度轨迹，SFT 缩小 Ω 解释训练后退化。 / Zero-parameter probe across future layers reveals SFT induces "blind confidence" that mechanistically degrades reasoning. |
| [[2605.05794]] MoLS Module-wise LR via SNR | Ziqing Wen et al. | 预热期一次性估计模块 SNR 自动校准学习率，LLaMA 7B PPL 降 1.69。 / SNR-based learning-rate scaling fixes systematic Adam underupdates on Embedding/Head modules with <2% overhead. |
| [[2605.05819v1]] HCInfer | Shen Xu et al. | CPU 异步 LoRA 补偿 + 敏感度感知动态秩，RTX 4090 上精度 +5.2%、吞吐 10.4×。 / Heterogeneous CPU-GPU pipeline with sensitivity-aware rank allocator delivers high-accuracy high-throughput quantized inference. |
| [[2605.05873]] CITE Anytime-Valid Inference | Hirofumi Ota et al. | e-process 交叉联合检验提供 LLM 自洽性的任意时刻有效模式认证。 / Sequential mode-certification with Type-I control and category-set-size-independent stopping time. |
| [[2605.05892v1]] FLAS Flow-based Activation Steering | Zehao Jin et al. | 多步 Euler 积分的概念条件速度场，AxBench 首次学习方法胜 prompting。 / Drops position-invariance, single-step, contrastive-data assumptions in steering; zero-shot generalizes to unseen concepts. |
| [[2605.05957]] Correction Suppression CDS/DPA | Zixuan Chen et al. | 任务请求抑制 LLM 事实纠正，CDS/DPA 免训练干预把纠错率从 0% 提到 58.2%。 / Identifies "factual strictness" as new reliability axis and offers two mechanistically-motivated training-free fixes. |
| [[2605.05973]] SIREN Winner's Curse Correction | Yang Xu et al. | 冻结候选 + 重复分裂 + bootstrap 纠正自适应基准乐观偏差，偏差从 +1–4pp 至 ±0.21pp。 / Selection-aware CLT and Gaussian multiplier bootstrap recover true tune-then-deploy performance on MMLU-Pro. |
| [[2605.05980v1]] TACT Coding Agent Drift | Yuan Sui et al. | 在 `</think>` token 提取过度推理 / 过度行动方向，SWE-bench Verified +5.8pp。 / Training-free residual-stream steering of long-horizon coding agents reduces drift and step count. |
| [[2605.05983]] PrOSV Prompt-Only Steering | Yuntai Bao et al. | 联合训练方向-因子且仅干预 4 个 prompt token，AxBench SOTA，算术能力损失大幅减小。 / Scaling-theory-based joint training and prompt-only intervention eliminate per-SV factor search and preserve utility. |
| [[2605.06014]] RHT Quantization Theory | Ran Ben-Basat et al. | 首次证明 2-RHT 恢复 URR 标量量化保证；向量量化需 3-RHT。 / Closes the long-standing theoretical gap for engineering use of compositions of Randomized Hadamard Transforms. |
| [[2605.06017]] Matrix-Decoupled Concentration | Pei-Sen Li | 用因果解析矩阵编码依赖，消除稀疏序列奖励 O(N) 方差膨胀，实现 O(1) 界。 / Dimension-free concentration inequality for RLHF / long-context evaluation, generalizing McDiarmid to dependent sequences. |
| [[2605.06052v1]] XtraMAC FPGA Mixed-Precision MAC | Feng Yu et al. | 共享整数尾数乘积统一 INT/FP MAC，密度提升 1.4–2.0×，GEMV 上 1.9× 能效胜 H100。 / Unified-mantissa FPGA MAC supports runtime datatype switching at II=1 with open-source release. |
| [[2605.06067]] nGPT Natively 4-Bit (NVFP4) | Maxim Fishman et al. | 归一化 Transformer 在 NVFP4 下点积 SNR 提高 7 dB，3.6× 吞吐量。 / NVIDIA: architectural normalization replaces RHT/scaling patches and matches BF16 LR while training MoE at 30B. |
| [[2605.06076]] Static Mechanistic Localization Pitfalls | Hang Chen et al. | SFT 期间 attention 技能电路自由迁移，静态定位等价随机；提出预测性定位。 / Circuit Distance / Stability / Conflict metrics expose the time-lag flaw in current locate-then-update pipelines. |
| [[2605.06082]] PoTAcc PoT Quantization FPGA | Rappy Saha et al. | 首个 PoT 量化端到端开源流水线，PYNQ-Z2 上 3.6× 加速，<2% 精度损失。 / Bridges PyTorch/TF PoT training and shift-PE FPGA accelerators with three quantization schemes. |
| [[2605.06152v1]] Slingshot via Numerical Feature Inflation | Liu Hanqing et al. | float32 softmax 吸收误差与神经坍缩耦合产生 Slingshot 损失尖峰，float64 可消除。 / Float-precision artifact, not optimizer dynamics, drives Slingshot spikes; FP4/FP8 training implications discussed. |
| [[2605.06161]] Policy Invariance for Safety Judges | Shihao Weng et al. | 提出 PIS 量化裁判对等价改写的稳健性，四模型 PIS 跨度 20×。 / Defines policy-invariance principles and Judge Card reporting; reveals 18–43% of flips are pure measurement failure. |
| [[2605.06169v1]] MV-Split Residuals (1000-Layer DiT) | Pengqi Lu | 解耦均值与中心化残差增益，根治均值主导崩溃，1000 层 DiT 首次稳定训练。 / Lightweight residual change eliminates "Mean Mode Screaming" failures in ultra-deep diffusion transformers. |
| [[2605.06196v1]] The Granularity Axis | Chonghan Qin et al. | LLM 内部存在微观→宏观社会角色的线性"粒度轴"（PC1 余弦 0.972）。 / Single linear direction in Qwen3-8B/Llama-3.1-8B causally controls social-role granularity in outputs. |
| [[2605.06213v1]] Dynamic Boundary Evaluation (DBE) | Haoxiang Wang et al. | Rasch IRT + SGBS 自适应在模型决策边界生成评测项，能力误差 0.032 logit。 / NeurIPS 2026 D&B Track adaptive evaluation across safety, over-refusal, instruction-following, and sycophancy. |
| [[2605.06225]] Memory Inception KV-Cache Steering | Andy Zeyi Liu et al. | 文本描述符编码为潜在 KV 记忆槽并选层注入，KV 存储压缩 6–118×。 / Training-free LLM steering invisible in transcripts, beats CAA on dialogue/personality/reasoning. |
| [[2605.06241]] ReasonMaxxer (Sparse Policy Selection) | Ömer Faruk Akgül et al. | RLVR 仅在 1–3% 高熵 token 上重排策略；LoRA 对比损失以 $4–25 匹配 RL checkpoint。 / Causal entropy / oracle analysis reframes RL-for-reasoning as sparse decision-point reranking. |
| [[2605.06283]] Rubric Modifications & Autorater Agreement | Jessica Huynh et al. | 统计量化加示例 / 分解评分维度等修改对 GPT-4o 与 Llama 评分一致性的因果效应。 / Adding examples improves human-autorater agreement; higher rubric complexity reduces it. |
| [[2605.06295v1]] METAGAME Meta-attributions | Hubert Baniecki et al. | 把任意一阶归因方法作为博弈再求 Shapley，得到方向性二阶交互归因。 / Unifies STII/SOP and improves interaction recognition on CLIP family and ConceptAttention. |
| [[2605.06308]] Black-Box CoT Confidence (C+G+V) | Marc Boubnovski Martell et al. | CoT 嵌入轨迹的几何 + 覆盖 + 自评融合，K=4 胜 K=8 自洽 (+0.075 AUC)。 / Black-box confidence on MedQA/GPQA/MMLU-Pro with Gemini 3.1 Pro and Claude Sonnet 4.6 saving 45–55% API cost. |
| [[2605.06316]] Pro-KLShampoo | Ruotong Sun et al. | 利用 KL-Shampoo 谱"尖峰-平坦"结构，低秩 + 正交化，挂钟时间省至 13%。 / Provides O(1/√T) convergence guarantee while improving validation loss, memory, and wallclock on GPT-2 / LLaMA. |
| [[2605.06322]] SMolLM Looped Molecular Transformer | Akhil Jindal et al. | 53K 参数循环 Transformer 在 ZINC-250K 上 SMILES 有效率 95.3%，按层次顺序习得化学语法。 / Weight-sharing as window into hierarchical formal-language learning, with a causal bracket-matching head at pass 1. |
| [[2605.06326]] TRICE Tool-Integrated Reasoning | Qianjia Cheng et al. | 数据筛选 + 混合轨迹 SFT + 路由回放 RLVR，AIME 2025 上 4B/30B 达 96.7%/99.2%。 / Full-pipeline recipe that turns Qwen3 thinking models into genuine code-using reasoners while preserving no-tool ability. |
| [[2605.06327]] Evaluation-Context Divergence | Florian A. D. Burnat et al. | 配对提示协议显示模型在评估/部署框架下行为差异，对齐流水线系根因。 / Paired-prompt protocol reveals OLMo-3-Instruct is uniquely "eval-cautious" while Mistral/Phi/Llama are "deployment-cautious." |
| [[2605.06342]] SKOP Key-Orthogonal Projections | Haoyan Luo et al. | 引导向量投影到关键差异方向正交子空间，效用损失降低 5–7×。 / Identifies attention rerouting as utility-degradation root cause and is the only method working at 16K-token retrieval. |
| [[2605.06352]] Topological Signatures of Grokking | Yifan Tang et al. | Grokking 泛化阶段伴随 H₁ 持续性显著跃升，跨 Transformer/MLP 一致。 / Persistent homology gives architecture-agnostic topological signature of generalization phase transition. |
| [[2605.06357]] MEFA Full-Gradient Attacks | Yuan Du et al. | 梯度检查点把扩散/EBM 净化全梯度攻击内存降到 O(1)，DiffPure 鲁棒性 61%→43%。 / Reveals reported robustness of stochastic purification defenses is largely an evaluation artifact. |
| [[2605.06366v1]] Layer Collapse in Diffusion LMs | Alexander Conzelmann et al. | LLaDA-8B 单一超级离群值通道支配前半层；DLM 早层冗余，量化损失 1.8% vs Llama 64.7%。 / First systematic activation-dynamics analysis of DLMs vs AR models with implications for compression. |
| [[2605.06458]] Invariant Features in LLMs | Agnibh Dasgupta et al. | 广义特征值分解分离不变 / 干扰子空间，9 模型零样本归因 >92%。 / Local geometric framework with causal interventions and zero-shot model attribution applications. |
| [[2605.06480]] Patch-Effect Graph Kernels | Ruben Fernandez-Boullon et al. | 激活修补结果转图并用 WL/谱核分类，GPT-2 Small IOI 上局部边特征完美分类。 / Methodological scaffold for circuit comparison; structured compression rather than novel signal per se. |
| [[2605.06494]] WL Analysis of SAE Features | Ruben Fernandez-Boullon et al. | SAE 特征表示为词元共现图，WL 核恢复解码器余弦无法发现的字母簇。 / Complementary graph-kernel lens for SAE feature organization, best for co-occurrence topology. |
| [[2605.06505]] PACZero PAC-Private ZO Fine-Tuning | Murat Bilgehan Ertan et al. | 对子集聚合零阶梯度做符号量化实现 PAC 隐私，SST-2 OPT-1.3B 达 88.99%。 / Variants PACZero-MI/ZPL beat DP-ZO in the high-privacy regime with information-theoretic free unanimity steps. |
| [[2605.06519]] Data Reconstruction Finite-Width Guarantees | Edward Tansley et al. | 随机特征模型首次有限宽度数据重建 PAC 风格保证，子空间感知算法优于全空间。 / Width requirement scales with intrinsic data dimension r; CIFAR-10 validates subspace recovery via first-layer changes. |
| [[2605.06523]] RLVR Implicit Reward Overfitting | Hao Ye et al. | 周期性秩-1替换证明 RLVR 推理增益几乎全部在 ΔW 秩-1 分量。 / Diagnostic study (not training recipe) on universal "leading spike + heavy tail" spectrum of RLVR updates. |
| [[2605.06563]] Criticality and Saturation in Orthogonal NNs | Max Guillen et al. | Weingarten 演算 + 费曼图首次解析推导正交 MLP 有限宽度递归。 / Proves criticality preserves to finite width and explains long-observed saturation absent in Gaussian init. |
| [[2605.06597]] UniSD Unified Self-Distillation | Yiqiao Jin et al. | 模块化自蒸馏框架（多教师 + EMA + 对比 + 特征 + 散度裁剪），Qwen2.5-7B +5.4。 / Decomposes self-distillation into reliability / alignment / stability axes; beats GKD by +2.8 without external teacher. |
| [[2605.06599v1]] Weight-Decay Turns Loss Landscapes Villani | Abhijit Das, Sayantan Dutta | 严格证明 Transformer + L² 满足 Villani 函数，推导对数-Sobolev 与 PAC-Bayes 界。 / First functional-analytic foundation for weight-decayed Transformer optimization with empirical validation on GPT-Neo-125M. |
| [[2605.06605]] DAPRO Dynamic Jailbreak Budgets | Shai Feldman, Yaniv Romano | 在线策略动态分配多轮对话预算，给出更紧的"时间到不安全采样"下预测界。 / First dynamic distribution-free conformal framework for multi-turn safety evaluation under global compute budget. |
| [[2605.06610]] SoftSAE Adaptive Top-K | Jakub Stępień et al. | 可微 Soft Top-K 让 SAE 按输入复杂度预测每输入 k̂，去纠缠度量胜 TopK。 / Adaptive sparsity aligns explanatory capacity with local intrinsic dimensionality of each input. |
| [[2605.06611]] Attention Sink Structural Origin | Siquan Li et al. | 因果掩码 → 方差差异 → 超级神经元 → 维度不平衡 → 注意力锁首 token；Head-wise RMSNorm 修复。 / Complete causal chain explanation with two interventions and a faster-converging architectural fix. |
| [[2605.06615]] SignSGD Tight Lower Bounds | Hongyi Tao et al. | ℓ∞ 光滑首次给出 SignSGD 紧下界（稀疏噪声下样本复杂度 d 倍优于 SGD），推广到 Muon。 / Validated on nanoGPT-124M C4 pretraining; rigorous explanation for Muon/SignSGD advantage over AdamW. |
| [[2605.06632]] LCDD + SFT-Eraser Reversible SFT | Yuping Lin et al. | LCDD 把 SFT 行为压缩进 73–84% 稀疏子网络，SFT-Eraser 推理时用软触发器逆转。 / Proof-of-concept for crafted-then-reversible fine-tuned behaviors across 12 model-task combinations. |
| [[2605.06654]] Optimizer-Model Consistency | Yuxing Liu et al. | SFT 时与预训练同族优化器全参微调遗忘最少；Muon 在推理 SFT 上反劣于 AdamW。 / Implicit-regularization theory explains why optimizer-matched full FT beats LoRA on the learning-forgetting Pareto frontier. |
| [[2605.06656]] Why Global LLM Leaderboards Are Misleading | Jai Moondra et al. | 全局 BT 排名仅可靠预测 10.3% 投票；(λ,ν)-portfolio 5 排名即覆盖 96% 偏好。 / Reframes LLM model selection as set-cover; 6 portfolio LLMs cover twice the votes of top-6 global. |
