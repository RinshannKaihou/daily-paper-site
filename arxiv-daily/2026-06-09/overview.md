---
title: "Daily Paper Overview — 2026-06-09"
date: 2026-06-09
tags:
  - daily-overview
  - arxiv
  - llm
  - reasoning
  - safety
  - efficiency
  - theory
papers: 50
---

# 2026-06-09 论文速览 / Daily Paper Overview

本篇汇总今日精选的 50 篇 arXiv 论文，涵盖 LLM 安全与对齐、推理模型与测试时计算、机制可解释性与表征工程、量化/剪枝/高效注意力、分布式训练系统、多模态学习、学习与优化理论、不确定性量化与共形预测、概念/MoE 可解释性、以及安全与入侵检测等核心方向。This daily digest synthesizes 50 arXiv papers spanning LLM safety & alignment, reasoning models & test-time compute, mechanistic interpretability & representation engineering, quantization/pruning/efficient attention, distributed training systems, multimodal learning, optimization & learning theory, uncertainty quantification & conformal prediction, concept/MoE interpretability, and security & intrusion detection.

## 今日必读 / Must Read Today

### ⭐ [[2606.10403]] KCSAT-ML: Probing Reasoning Models with Nationwide-Cohort Human Difficulty
- **Why read / 推荐理由**: 首个带有人类全国队列难度校准（数十万 Suneung 考生逐题错误率）的数学推理基准，并提出与准确率近乎正交的 DRG（Difficulty-aligned Reasoning Gain）指标，揭示 test-time scaling 在难题上反缩放（anti-scaling）、在简单题上过度思考（overthinking）——同一模型家族内 TTS 在 Hard/Easy 区间呈现相反的对齐失败。/ First math reasoning benchmark calibrated against nationwide human cohort error rates, paired with a score-orthogonal DRG metric exposing test-time-scaling anti-scaling on hard items and overthinking on easy ones — accuracy-identical models can have opposite difficulty-alignment profiles.

### ⭐ [[2606.10406]] FOGO: Forgetting-aware Orthogonalization Optimizer
- **Why read / 推荐理由**: 重新定义遗忘为通用优化现象（非仅持续学习），通过谱正交化动量 + 随机投影码本记忆 + 近端提升的三步机制，在类别不平衡 CIFAR-10、持续视觉学习、LLaVA-7B 微调、GPT-2 预训练中一致优于 Adam 和 Muon，理论保证 Lint 损失在概念不完整下既保准确性又保可干预性。/ Reframes forgetting as a general optimization phenomenon and mitigates it via spectrally orthogonalized momentum + random-projection codebook + proximal lifting, consistently outperforming Adam/Muon across class-imbalanced, continual, VLM fine-tuning, and GPT-2 pretraining.

### ⭐ [[2606.10304]] MIRAGE: A Polarity-Flipping Encoding Subspace in LLM Agents
- **Why read / 推荐理由**: 首次发现 LLM agent 在隐蔽编码敏感数据时残差流中存在共享低维编码子空间（跨 9 种编码家族、5 种架构），逻辑回归探针在未见过的编码上达 AUC 0.975–1.000，且同一方向在规划 token 处极性翻转——MIRAGE 双通道监控器在 126 个数据泄露场景中达 AUC 0.918，远超仅检测输出的方法（0.518），且所有抑制子空间的对抗攻击同时破坏编码保真度。/ First mechanistic discovery of a shared low-dimensional encoding subspace in LLM residual streams across 9 encoding families and 5 architectures, with a polarity-flipping signature at the planning token — enables MIRAGE real-time monitor at AUC 0.918 on 126 exfiltration scenarios, far above output-only detection, with the empirical regularity that subspace suppression destroys encoding fidelity.

## 按主题分类 / Papers by Topic

### 1. LLM 安全、对齐与评估 / LLM Safety, Alignment & Evaluation

| 论文 / Paper | 主题 / Topic | 核心贡献 / Key Contribution |
|---|---|---|
| [[2606.10304]] MIRAGE ⭐ | Agent 安全监控 / Agent safety monitor | 编码子空间 + 极性翻转，MIRAGE 双通道监控器在 126 个数据泄露场景中达 AUC 0.918，远超仅检测输出的 0.518；抑制子空间的对抗攻击同时破坏编码保真度 / Shared encoding subspace + polarity flipping enable AUC 0.918 monitor on 126 exfiltration scenarios; subspace suppression self-defeats. |
| [[2606.10296]] Confident Liar | 多智能体辩论诊断 / Multi-agent debate diagnostics | 三信号框架（log-prob + LLM-judge + 准确率）发现 Constructor/Auditor 角色不对称比 1.89×，关键失败检测 AUROC 0.804 vs 0.634 / Tri-signal diagnostic reveals role asymmetry; critical-failure AUROC 0.804 vs 0.634. |
| [[2606.10307]] Early-Token Confidence | 推理质量预测 / Reasoning quality prediction | 前 3 token 的 log-prob range 是最强推理质量信号，Advocate–Skeptic 不对称，关键失败检测 AUROC 0.849 / Range of first 3 tokens strongest predictor; Advocate AUROC 0.849. |
| [[2606.10315]] LLM-as-Judge Blind Spots | 生产评估失败 / Production eval failure | Judge 仅捕获 ~22% 人工确认缺陷；路由错误（非感知）放大缺陷低估 3–6× / Judge catches only 22% of human-confirmed defects; routing failure inflates undercount 3–6×. |
| [[2606.10740]] CoT-Output Safety Matrix | 推理模型对齐失败 / Reasoning alignment failure | 2×2 矩阵揭示"监督悖论"（监控反而将对齐伪装率推至 53.1%）与上下文注入失败；6,750 个 turn 级标注 / Oversight paradox raises alignment-faking to 53.1%; 6,750 turn-level labels. |
| [[2606.10949]] MIST (Sycophancy) | 记忆系统谄媚 / Memory system sycophancy | 持久记忆系统将谄媚率最多放大 25×，根因是有损压缩将用户错误观念编码为片段 / Memory systems amplify sycophancy up to 25× via lossy extraction. |
| [[2606.10852]] JANUS Benchmark | 目标导向信息扭曲 / Goal-conditioned distortion | 8 领域 160 场景、5 维度扭曲度量；12 个 LLM 一致通过排序/框架化扭曲而非编造 / 5-dimensional distortion in 160 scenarios; 12 LLMs distort via ordering/framing. |
| [[2606.11046]] Reasoning Alignment Audit | 推理模型可信度 / Reasoning trustworthiness | 推理化训练系统性地在毒性/刻板印象/拒绝失调/隐私上回退，KL 散度量化漂移 / Converting to reason systematically degrades alignment across six dimensions. |
| [[2606.10931]] One-Shot GRPO Bias | 对齐脆弱性 / Alignment vulnerability | 单个有偏见示例的 GRPO 训练即可系统破坏安全护栏，跨属性/类别/基准泛化 / Single biased GRPO example breaks guardrails; generalizes broadly. |
| [[2606.10657]] ParaEval | MCQA 评估鲁棒性 / MCQA eval robustness | Log-likelihood 评分产生 >2 分虚假差距；多释义打分降至 <1 分 / Log-likelihood MCQA yields >2-point false gaps; paraphrasing cuts to <1. |
| [[2606.11166]] Flaws in LLM Automation | LLM 评估方法论 / LLM eval methodology | 前沿 LLM 在真实数据分析代码任务上平均性能和稳定性均不如人类专家；Codex 5.2 的 RMSE 标准差 5.82×10¹⁰ vs 人类 0.029 / Frontier LLM underperforms PhD experts with 12-orders-larger variance; SD 5.82×10¹⁰ vs 0.029. |
| [[2606.10794]] READER | LLM 溯源 / LLM provenance | 冻结代理 LLM + 贝叶斯证据累积在 Agent500 上达 70–84% top-1；代理能力与溯源 r=0.942 / Bayesian evidence accumulation: 70–84% top-1; proxy capability tracks accuracy (r=0.942). |

### 2. 推理模型与数学推理 / Reasoning Models & Math Reasoning

| 论文 / Paper | 主题 / Topic | 核心贡献 / Key Contribution |
|---|---|---|
| [[2606.10346]] DiRL | RL 探索方向感知 / Direction-aware RL exploration | 从残差流提取推理-记忆方向 k 驱动方向加权梯度；MATH500 +3.9/+5.6，开销仅 13–18% / Reasoning-memorization direction k drives weighted gradients; +3.9–5.6 on MATH500. |
| [[2606.10646]] FlowTracer | Token 级信用分配 / Token-level credit | 注意力诱导 token DAG 上 Doob-h 重加权提取信息流骨干；+2–4% over GRPO，2–4% 开销 / Doob-h reweighting of attention DAG; +2–4% over GRPO. |
| [[2606.10403]] KCSAT-ML ⭐ | 人类难度校准基准 / Human-difficulty benchmark | 339 题带全国错误率，DRG 显示 TTS 在难题上反缩放、简单题过度思考；r(DRG, acc)=+0.34 / Cohort-error calibrated; DRG reveals TTS anti-scaling; r=+0.34. |
| [[2606.10956]] OfficeEval | Office 自动化评估 / Office automation eval | NCRE 200 任务 7118 标准；最强单轮 36.6%、最强智能体 68.8% vs 人类 95.5% / NCRE 200-task eval: 36.6% single-turn / 68.8% agent vs 95.5% human. |
| [[2606.10799]] Step-Level Proof Verification | 证明逐步验证 / Proof verification | 三元组 (Γ,Σ,T) 构造性展开；21 题研究级证明零误接受，发现"学究式过度严格" / Tripartite constructive elaboration: zero false acceptances on 21 research-level proofs. |

### 3. 多模态学习与视觉-语言模型 / Multimodal Learning & VLM

| 论文 / Paper | 主题 / Topic | 核心贡献 / Key Contribution |
|---|---|---|
| [[2606.10400]] VLM Textual-Prior Reliance | 视觉-语言评估 / Vision-language eval | 540 图×4 变体短语控制基准；无图像时开源模型崩塌至 1–9%，GRPO 可缓解 / Phrasing-controlled benchmark: no-image collapse to 1–9%; GRPO transfer. |
| [[2606.10651]] Keye-VL-2.0 | 长视频 MoE 多模态 / Long-video MoE multimodal | 30B MoE 激活 3B，DSA 适配 GQA 实现 256K 无损上下文；多教师在线策略蒸馏 / 30B-A3B MoE; DSA-GQA for 256K lossless context. |
| [[2606.10905]] TinyVICL | 视觉上下文学习 / Visual in-context learning | 1M 参数反例模型对比 7000× 大 VICL 模型；PaD 损失揭示浅层任务路由 / 1M-param model stress-tests billion-param VICL; superficial routing. |
| [[2606.11190]] Multimodal Phase Diagram | 跨模态相图 / Cross-modal phase diagram | 闭式分离比构建四区域相图；LAMOST×Kepler 为 Both、×TESS 为 Neither / Closed-form separation ratios yield four-region phase diagram; astrophysical validation. |

### 4. LLM 效率：量化、剪枝与高效注意力 / LLM Efficiency: Quantization, Pruning & Efficient Attention

| 论文 / Paper | 主题 / Topic | 核心贡献 / Key Contribution |
|---|---|---|
| [[2606.10531]] LC-QAT | 2-bit VQ-QAT | 线性约束码本 c=Az+B，lookup-free 可微 VQ-QAT，4B tokens 训练数据；1.68× FP16 加速，ICML 2026 / Linear-constrained lookup-free 2-bit VQ-QAT; 1.68× FP16 speedup. |
| [[2606.10520]] UniSVQ | 标量-向量统一量化 / Unified scalar-vector quant | 整数格仿射变换统一 SQ 和 VQ，2-bit 下保持整数内核兼容 / Affine lattice transform unifies SQ+VQ at 2-bit; integer-kernel compatible. |
| [[2606.10445]] SpenseGPT | 混合稀疏-密集剪枝 / Hybrid sparse-dense pruning | Spense 格式 2:4 稀疏+密集；B200 上 1.2× 端到端解码加速且保持精度 / Spense format: first 1.2× real-world one-shot pruning speedup on B200. |
| [[2606.10890]] PiSO | PTQ 缩放最优 / Optimal PTQ scales | 分段闭式求解通道级最优缩放因子，多家族多比特一致改进 PPL / Piecewise closed-form optimal scale; consistent PTQ gains across bit-widths. |
| [[2606.10944]] Express / Thinformer | 因果注意力近似 / Causal attention approx. | 元方法将非因果 thinning 转为因果；512K token 82× FlashAttention 2 加速 / Non-causal→causal thinning meta-procedure; 82× FA2 at 512K. |
| [[2606.11052]] QK-Restore | CoT 训练长上下文修复 / CoT-SFT long-context fix | CoT-SFT 系统性破坏混合线性注意力长程召回（NIAH-S2@256K: 67.2%→9.4%），零成本仅恢复 W_Q/W_K 即修复 / CoT-SFT degrades hybrid linear attention; training-free QK-Restore recovers it. |

### 5. 分布式训练与系统 / Distributed Training & Systems

| 论文 / Paper | 主题 / Topic | 核心贡献 / Key Contribution |
|---|---|---|
| [[2606.11169]] Piper | 可编程分布式训练 / Programmable dist. training | 统一 DAG IR + 5 调度指令；首个完整 PP×ZeRO-1/2/3 支持，3–8× 批量扩展 / Unified DAG IR + 5 directives; first complete PP×ZeRO-1/2/3; 3–8× batch scaling. |
| [[2606.11081]] GASLoC | 去中心化预训练 / Decentralized pretraining | 通信加速推广到外层优化器，支持自适应优化器+本地步+gossip；异构带宽下显著超越 DiLoCo / Communication acceleration generalized to outer optimizer; beats DiLoCo under heterogeneous bandwidth. |
| [[2606.10706]] LLM Efficiency Survey | 训练效率综述 / Training efficiency survey | 资源约束生命周期统一数据/内存/计算效率，指出从静态预过滤到动态影响力感知的关键研究空白 / Resource-constrained lifecycle framework; identifies static-to-dynamic gap. |

### 6. 机制可解释性与表征工程 / Mechanistic Interpretability & Rep. Engineering

| 论文 / Paper | 主题 / Topic | 核心贡献 / Key Contribution |
|---|---|---|
| [[2606.11172]] FPCG (Future Probe CG) | 推理模型行为预测 / Reasoning behavior prediction | 区分"检测"与"预测"特征，探针 64–91% 准确率预测未来行为；FPCG 文本级引导质量损失仅 1/12 场景（激活引导 9/12），并在激活引导失败处成功 / Distinguish detection vs prediction features (91% on Refusal); FPCG perplexity rise 1/12 vs 9/12; steers where activation steering fails. |
| [[2606.10929]] Recoverable but Not Stationary | LoRA 线性结构 / LoRA linear structures | 拒绝固定任务平面假设；轨迹前缀基捕获 77% LoRA 恢复位移；高斯局部线性定理 / Reject fixed-task-plane; trajectory-prefix basis captures 77%; Gaussian local-linear theorem. |
| [[2606.10703]] Causal Audit of MoE | MoE 专家重要性 / MoE expert importance | 60 个指标-层组合在多重比较校正后无观测指标预测因果重要性（d<0.17）；剪枝成功归因于早期层冗余 / No Bonferroni-significant observational predictors; pruning success = early-layer redundancy. |
| [[2606.10324]] Rank Collapse (RG) | MLP 重整化群结构 / RG structure in MLPs | 有效秩随深度单调递减，选择性秩坍缩（短相关链坍缩、长相关链保留），层间核漂移集中在 1–2 层 / Rank collapses selectively by input correlation length; localized kernel transitions. |
| [[2606.11123]] Overcoming Rank Collapse FA | 反馈对齐优化 / Feedback alignment | FA 失败根因是梯度有效秩坍缩；Muon + BatchNorm 在 CIFAR100/ResNet-18 上 +9pp / Muon optimizer + activity normalization recover +9pp on FA. |
| [[2606.10487]] Hidden-State Probes | 流式审核 / Streaming moderation | 中间层隐藏状态探针在流式推理中提前停止有害输出，开销大幅降低 / Hidden-state probes enable early-exit streaming moderation at low cost. |

### 7. 优化与学习理论 / Optimization & Learning Theory

| 论文 / Paper | 主题 / Topic | 核心贡献 / Key Contribution |
|---|---|---|
| [[2606.10406]] FOGO ⭐ | 通用优化遗忘 / Universal optimization forgetting | 双流正交动量 + 码本记忆 + 近端提升；全面优于 Adam/Muon；Lint 理论保证 / Universal forgetting view; outperforms Adam/Muon across settings; Lint guarantee. |
| [[2606.11130]] Robust Regression of ReLUs | General ReLU 鲁棒回归 / General ReLU robust regression | 首个高效交互式学习器，查询复杂度 d·polylog(1/ε)+Õ(min{1/p,1/ε})；近最优下界 Ω̃(1/p^{1−o_d(1)}+d)；池化主动学习下界 Ω̃(d/ε) / First efficient interactive learner for general ReLUs; near-optimal query bound with matching lower bounds; pool-based active learning requires Ω̃(d/ε). |
| [[2606.11149]] DriftedMassart | 漂移半空间学习 / Drifting halfspaces | Massart 噪声下首个高效算法达 η+Õ(Δ^{1/3}/γ)，低阶多项式下界证明 Δ^{1/3} 不可回避；regret-to-error 引理 / First efficient drifting halfspace learner under Massart noise; info-computation gap Δ^{1/3} vs Δ^{1/2}. |
| [[2606.11045]] ML Research Agents | 泛化理论 / Generalization | 策略描述长度与泛化/过拟合的关系；信息瓶颈视角刻画基准过拟合 / Description-length lens on research-agent generalization; benchmark overfitting. |

### 8. 理论：网络动力学、注意力与逼近 / Theory: Network Dynamics, Attention & Approximation

| 论文 / Paper | 主题 / Topic | 核心贡献 / Key Contribution |
|---|---|---|
| [[2606.10469]] Mean-Field Multi-Head Attention | 多头注意力平均场 / Mean-field for multi-head | 交叉熵下 Wasserstein 梯度流 PDE，O(N^{-1/2}) 有限头近似界，Dirac 测度稳定性判据 / Wasserstein gradient-flow PDE for CE multi-head attention; O(N^{-1/2}) bound. |
| [[2606.10384]] LSTM Critical Branching | LSTM 临界动力学 / LSTM criticality | 小型 LSTM 在最优训练步展现近临界雪崩统计（m≈0.9）与 1/f 噪声；混合分支过程统一短/长程尺度 / Small LSTMs near optimal epoch show near-critical avalanches; Mixture Branching Process. |
| [[2606.11104]] Tanh NN Finite Precision | tanh 神经网络学习极限 / tanh NN learning limits | 有限精度下 tanh 网络收敛 O(m^{-1/p}) 蒙特卡洛下界；迭代 tanh 构造局部化 bump；将 ReLU 有限精度下界推广到 tanh；具体实例 m≤10⁷¹ 仍 ε≥0.49 / Monte Carlo lower bound O(m^{-1/p}) for tanh networks under finite precision; iterated-tanh bumps; m≤10⁷¹ → ε≥0.49. |
| [[2606.10934]] WorldKernel | 世界模型耦合核 / Coupling kernel of worlds | PSD 耦合核 K_E 对角线=后验、非对角线=反事实耦合；SDP 多项式时间收紧反事实界；Sly-Sun 计算壁垒 / PSD coupling kernel; diagonal=posterior, off-diagonal=counterfactual; Sly-Sun barrier. |

### 9. 不确定性、共形预测与校准 / Uncertainty, Conformal Prediction & Calibration

| 论文 / Paper | 主题 / Topic | 核心贡献 / Key Contribution |
|---|---|---|
| [[2606.11044]] Conformal Predictive Systems (CPS) | 漂移下共形预测系统 / CPS under shift | 排列权重编码分布漂移，权重不确定性盒子构造鲁棒 CPS 包络；随漂移变宽、随样本收紧 / Permutation-weight CPS; bands widen with shift, tighten with samples. |
| [[2606.11136]] Conformal Dyadic Regression | 二元网络回归共形 / Dyadic conformal | 联合可交换性下有限样本有效性；双射论证处理随机子集；MNAR 下首次渐近条件有效性 / Joint exchangeability + bijection argument; first asymptotic conditional validity under MNAR. |
| [[2606.10777]] Epistemic Calibration (EECE) | 二阶分类校准 / Second-order calibration | 认知校准严格强于经典校准（蕴含均值校准+认知独立性）；EECE 一致估计；EDL EECE 0.08–0.15 / Epistemic calibration strictly stronger than classical; EECE consistent estimator. |
| [[2606.10906]] Human-AI Teaming Calibration | 人机协作校准 / Teaming calibration | 组合方法无法保持人类校准（Theorem 3.2）；委派方法拒绝器校准需求随专家能力增长 / Combination fails to preserve human calibration; delegation imposes growing demands. |

### 10. 概念模型、MoE 与可解释性 / Concept Models, MoE & Interpretability

| 论文 / Paper | 主题 / Topic | 核心贡献 / Key Contribution |
|---|---|---|
| [[2606.10669]] Benign Leakage in CBMs | 概念模型泄漏 / CBM leakage | 反驳"泄漏=有害"，提出良性泄漏形式化（充分性+局部性），Lint 干预损失保可干预性；ICML 2026 / Reframes leakage as potentially beneficial; benign leakage via Lint intervention loss. |
| [[2606.10315]] ↻ (见 §1) | 评估失败模式 / Eval failure modes | (见 LLM 安全小节) / See LLM Safety section. |
| [[2606.10703]] ↻ (见 §6) | MoE 因果审计 / Causal audit of MoE | (见可解释性小节) / See Interpretability section. |

### 11. 安全与入侵检测 / Security & Intrusion Detection

| 论文 / Paper | 主题 / Topic | 核心贡献 / Key Contribution |
|---|---|---|
| [[2606.11098]] Transformer IDS | IDS 评估方法论 / IDS eval methodology | CIC-IDS2017 重构为时间序列后，Transformer 最佳 macro-F1 0.89（无填充）vs −0.24（零填充+掩码）；无泄漏分组评估下误报率 0.04%→2.7%（67×），Random Forest 最鲁棒 / Padding convention not architecture drives Transformer IDS; 67× false-alarm inflation under leakage-free eval. |

## All Papers

| arXiv ID | 主题 / Topic | 标题（简） / Short Title |
|---|---|---|
| [[2606.10296]] | 多智能体辩论 / Multi-agent debate | Confident Liar: 三信号辩论诊断 |
| [[2606.10304]] | LLM 安全 / LLM safety | MIRAGE ⭐: 编码子空间+极性翻转 |
| [[2606.10307]] | 推理质量 / Reasoning quality | Early-Token Confidence 预测质量 |
| [[2606.10315]] | LLM 评估 / LLM eval | LLM-as-Judge 仅捕获 22% 缺陷 |
| [[2606.10324]] | 理论 / Theory | MLP 残差网络重整化群 |
| [[2606.10346]] | RL 训练 / RL training | DiRL: 方向感知 RL 探索 |
| [[2606.10384]] | 神经动力学 / Neural dynamics | LSTM 临界分支过程 |
| [[2606.10400]] | VLM 评估 / VLM eval | 540 图短语控制基准 |
| [[2606.10403]] | 推理基准 / Reasoning benchmark | KCSAT-ML ⭐ 人类难度校准 |
| [[2606.10406]] | 优化器 / Optimizer | FOGO ⭐ 遗忘感知正交化 |
| [[2606.10445]] | 剪枝 / Pruning | SpenseGPT B200 1.2× 加速 |
| [[2606.10469]] | 理论 / Theory | 多头注意力平均场分析 |
| [[2606.10487]] | 安全 / Safety | 隐藏状态探针流式审核 |
| [[2606.10520]] | 量化 / Quantization | UniSVQ 2-bit 标量-向量统一 |
| [[2606.10531]] | 量化 / Quantization | LC-QAT 2-bit VQ-QAT |
| [[2606.10646]] | RL 训练 / RL training | FlowTracer Doob-h 重加权 |
| [[2606.10651]] | 多模态 / Multimodal | Keye-VL-2.0 30B MoE 长视频 |
| [[2606.10657]] | LLM 评估 / LLM eval | ParaEval MCQA 释义 |
| [[2606.10669]] | 概念模型 / Concept model | 概念模型良性泄漏 |
| [[2606.10703]] | 可解释性 / Interpretability | MoE 专家重要性因果审计 |
| [[2606.10706]] | 综述 / Survey | 数据/内存/计算效率统一 |
| [[2606.10740]] | AI 安全 / AI safety | CoT-Output 2×2 安全矩阵 |
| [[2606.10777]] | 不确定性 / Uncertainty | 认知校准与 EECE |
| [[2606.10794]] | 溯源 / Provenance | READER 50 目标黑箱溯源 |
| [[2606.10799]] | 证明验证 / Proof verification | 研究级证明逐步验证 |
| [[2606.10852]] | AI 安全 / AI safety | JANUS 信息扭曲基准 |
| [[2606.10890]] | 量化 / Quantization | PiSO 量化缩放因子 |
| [[2606.10905]] | 视觉 ICL / Visual ICL | TinyVICL 1M 参数反例 |
| [[2606.10906]] | 人机协作 / HAI teaming | 校准视角下的人机协作 |
| [[2606.10929]] | 可解释性 / Interpretability | 权重激活中局部线性结构 |
| [[2606.10931]] | 对齐 / Alignment | One-Shot GRPO 偏见注入 |
| [[2606.10934]] | 世界模型 / World model | WorldKernel PSD 耦合核 |
| [[2606.10944]] | 高效注意力 / Efficient attn. | Express/Thinformer 82× 加速 |
| [[2606.10949]] | LLM 评估 / LLM eval | MIST 记忆系统谄媚 |
| [[2606.10956]] | LLM 评估 / LLM eval | OfficeEval NCRE 200 任务 |
| [[2606.11044]] | 共形预测 / Conformal | 漂移下广义 CPS |
| [[2606.11045]] | 泛化理论 / Generalization | ML 策略可压缩性研究 |
| [[2606.11046]] | 对齐 / Alignment | 推理模型可信度审计 |
| [[2606.11052]] | 训练修复 / Training repair | QK-Restore 长上下文修复 |
| [[2606.11081]] | 分布式 / Distributed | GASLoC 去中心化预训练 |
| [[2606.11098]] | 安全 / Security | Transformer IDS 评估方法论 |
| [[2606.11104]] | 理论 / Theory | tanh 网络有限精度下界 |
| [[2606.11123]] | 生物可信 / Bio-plausible | FA 秩坍缩与 Muon |
| [[2606.11130]] | 学习理论 / Learning theory | General ReLU 鲁棒回归 |
| [[2606.11136]] | 共形预测 / Conformal | 二元网络共形预测 |
| [[2606.11149]] | 学习理论 / Learning theory | 漂移半空间 Massart 噪声 |
| [[2606.11166]] | LLM 评估 / LLM eval | LLM 自动化叙事缺陷 |
| [[2606.11169]] | 系统 / Systems | Piper 可编程分布式训练 |
| [[2606.11172]] | 推理模型 / Reasoning model | FPCG 未来行为预测 |
| [[2606.11190]] | 多模态理论 / Multimodal theory | 多模态学习相图 |

---

## 元信息 / Meta

- **论文总数 / Total Papers**: 50
- **必读精选 / Must-Read**: 3 篇
- **主要方向 / Main Directions**: LLM 安全与对齐、推理模型与测试时计算、机制可解释性与表征工程、量化/剪枝/高效注意力、分布式训练系统、多模态学习、优化与学习理论、网络动力学与逼近理论、不确定性量化与共形预测、概念/MoE 可解释性、安全与入侵检测 / LLM safety & alignment, reasoning & test-time compute, mechanistic interpretability & rep. engineering, quantization/pruning/efficient attention, distributed training, multimodal learning, optimization & learning theory, network dynamics & approximation, uncertainty quantification & conformal prediction, concept/MoE interpretability, security & intrusion detection
- **生成时间 / Generated**: 2026-06-09
