---
title: "Arxiv Daily Overview — 2026-06-19"
date: 2026-06-19
tags:
  - arxiv-daily
  - llm
  - interpretability
  - quantization
  - rl
  - agents
  - reliability
  - 2026-06-19
papers: 50
---

## 今日必读 / Must Read Today

### [[2606.20381]] Rethinking Shrinkage Bias in LLM FP4 Pretraining: Geometric Origin, Systemic Impact, and UFP4 Recipe

- **推荐理由：** 从量化 bin 的几何不对称出发，揭示 E2M1 (FP4) 在 Round-to-Nearest-Even 下的系统性负向"收缩偏置"随层乘性累积、被 Random Hadamard Transform 放大，是 NVFP4 训练不稳定的统一根因；提出的 UFP4（E1M2/INT4 均匀网格 + 全程 RHT + 仅对 dY 随机舍入）在 Dense 1.5B / MoE 7.9B / MoE 124B 长时预训练中持续降低 BF16 相对损失误差——直击计算精度可靠性 + 训练稳定性。
- **Why read:** Derives the geometric origin of FP4 (E2M1) "shrinkage bias" under RNE that accumulates multiplicatively across layers and is amplified by RHT — the unifying root cause of NVFP4 training instability. UFP4 (uniform E1M2/INT4 grid + RHT on all GEMMs + stochastic rounding on dY) cuts BF16-relative loss error across Dense 1.5B / MoE 7.9B / MoE 124B pretraining. Directly hits computation-precision reliability + LLM training stability.

### [[2606.20075]] What Makes Effective Supervision in Latent Chain-of-Thought: An Information-Theoretic Analysis (ICML 2026)

- **推荐理由：** 从信息论视角将潜在 CoT 的监督失效诊断为"双重坍缩"（梯度衰减 + 流形漂移），用统一潜在探针 (ULP) 度量潜在状态与显式推理步骤的互信息，并验证"信息-性能绑定"——推理准确率严格受限于潜在链中保留的互信息——直击隐藏状态可解释性 + 训练稳定性。
- **Why read:** Reframes latent-CoT supervision failure as a "dual collapse" (gradient decay along the optimization path + manifold drift in latent space) and introduces the Unified Latent Probe (ULP) to measure mutual information between latent states and explicit reasoning steps. Demonstrates an "Information-Performance Binding" — reasoning accuracy is strictly bounded by the MI retained in the latent chain. Directly hits hidden-states interpretability + training stability.

### [[2606.20128]] The Correctness Illusion in LLM-Generated GPU Kernels

- **推荐理由：** 用 24 内核受控语料 + 种子化 fuzzing + fp64 CPU 参考 + 每 (op, dtype) 绝对容差，证明 KernelBench/TritonBench/GEAK 的"单形状 allclose"判定器会把植入 bug 的内核错误认证为正确；种子化 oracle 在 5 类 GPU 上 100% 捕获 10/10"正确性幻觉"、控制样本零误报，每次失败可逐字节复现——直击推理评估 + 计算可靠性/硬件正确性。
- **Why read:** Builds a controlled 24-kernel corpus (15 correct controls + 9 documented-transcription-error variants) and uses seeded fuzzing with an fp64 CPU reference and per-(op, dtype) tolerances to show that KernelBench/TritonBench/GEAK single-shape allclose oracles mis-certify buggy kernels as correct. The seeded oracle catches 10/10 "correctness illusions" on 5 GPU classes with zero false positives on controls, each failure byte-reproducible from stored seeds. Directly hits inference evaluation + computation reliability.

---

## 按主题分类 / Papers by Topic

### A. 计算可靠性、精度、量化与硬件故障 / Computation Reliability, Precision, Quantization & Hardware Faults

| 论文 / Paper | 一句话总结 / TL;DR |
| --- | --- |
| [[2606.20381]] | UFP4 揭示并修复 FP4 预训练的几何"收缩偏置" / UFP4 exposes and fixes the geometric shrinkage bias of FP4 pretraining. |
| [[2606.20474]] | UltraQuant 用 FP4+UE8M0 把 KV 缓存压到 ~4.25 bit，折叠进原生 MFMA，P50 延迟降 3.47x / UltraQuant packs KV cache to ~4.25 bit with FP4+UE8M0, folding into native MFMA, cutting P50 latency 3.47x. |
| [[2606.20195]] | CountSketch 的嵌入质量对 FP16 舍入几乎不敏感，确定性舍入最优 / CountSketch embedding quality is nearly insensitive to FP16 rounding; deterministic rounding wins. |
| [[2606.20451]] | SSH-Net 结构化分段危险率网络预测 GPU 竞争风险下的失效时间分布 / SSH-Net predicts GPU failure-time distributions under competing risks. |

### B. 机制可解释性、隐藏状态与表示 / Mechanistic Interpretability, Hidden States & Representations

| 论文 / Paper | 一句话总结 / TL;DR |
| --- | --- |
| [[2606.20075]] | 潜在 CoT 监督的"双重坍缩"诊断与信息-性能绑定 / Dual-collapse diagnosis of latent-CoT supervision and the Information-Performance Binding. |
| [[2606.19831]] | 单神经元干预的"控制窗口律"：杠杆不等于触及 / A control-window law for single-neuron steering: leverage is not reach. |
| [[2606.19946]] | GEMS 几何约束实现无训练并行多语义激活注入 / GEMS geometric constraints enable training-free parallel multi-semantic activation steering. |
| [[2606.20077]] | VLM 中 in-context 视觉 token 经历渐进语义演化偏向高频 / In-context visual tokens in VLMs undergo progressive semantic drift toward high-frequency features. |
| [[2606.20097]] | HydraHead 因果定位稀疏检索头并混合 FA/GDN 长上下文 / HydraHead causally locates sparse retrieval heads and hybridizes FA/GDN for long context. |
| [[2606.20347]] | 临界渗流作为可解释性的解析可控合成数据 / Critical percolation as analytically tractable synthetic data for interpretability. |
| [[2606.20431]] | superposition 随 experience replay 上升，遗忘只在"低 R、高 S、刚出现"区最脆弱 / Superposition rises under replay; forgetting is worst in low-R, high-S, freshly-emergent regions. |
| [[2606.19941]] | 组合性只在狭窄的"连接-深度甜区"中涌现 / Compositionality emerges only in a narrow depth-connectivity sweet spot. |
| [[2606.20152]] | 作文质量表示线性可解码、随层深渐进涌现并向深层迁移 / Essay-quality representations are linearly decodable, emerge with depth, and drift deeper with length. |
| [[2606.20225]] | 涌现性不对齐激活可用差分均值方向 99.6% 分离并因果抑制 / Emergent-misalignment activations are 99.6% separable by a difference-in-means direction and causally suppressible. |
| [[2606.20560]] | DiffusionGemma 用 top-k/top-p 瓶颈把不透明串行深度压到 1.1x / DiffusionGemma compresses opaque serial depth to 1.1x via top-k/top-p bottleneck. |

### C. 训练动力学、优化与 RL/对齐 / Training Dynamics, Optimization & RL/Alignment

| 论文 / Paper | 一句话总结 / TL;DR |
| --- | --- |
| [[2606.20469]] | Fisher 几何尖锐度在重标定下不变，证明 SGD 偏向黎曼平坦极小 / Fisher-geometric sharpness is reparam-invariant; SGD provably favors Riemannian-flat minima. |
| [[2606.19818]] | UARM 用分位数共形不确定性对 GRPO 优势做异方差重加权，压制奖励黑客 / UARM uses quantile-conformal uncertainty to heteroscedastically reweight GRPO advantages, curbing reward hacking. |
| [[2606.19771]] | ICT 用 Jensen-Shannon 散度选最具分布独特性 token 做稀疏梯度更新 / ICT uses Jensen-Shannon divergence to pick the most distribution-distinctive tokens for sparse updates. |
| [[2606.19744]] | 顺序 DPO 不存在统一遗忘模式，"梯度对抗"非主因 / Sequential DPO shows no uniform forgetting pattern; gradient opposition is not the main cause. |
| [[2606.20008]] | VIMPO 从 KL-RL 最优性条件推出隐式价值函数，无 critic / VIMPO derives an implicit value function from KL-RL optimality, critic-free. |
| [[2606.20068]] | 把 Lean 当过程级奖励预言机融入 GRPO 做定理证明 / Lean as a process-level reward oracle fused into GRPO for theorem proving. |
| [[2606.19750]] | 流形 Bandit + 层次 Thompson Sampling 做贝叶斯课程学习 / Manifold bandits + hierarchical Thompson Sampling for Bayesian curriculum learning. |
| [[2606.19989]] | ODB 将 batch 构造延迟到真实代价点，DGAP 协议保证无死锁 / ODB defers batch construction to true-cost points; DGAP protocol guarantees deadlock-freedom. |
| [[2606.19697]] | CoT Transformer 可在 Word RAM 指令层仅多对数开销模拟任意算法 / CoT Transformers simulate arbitrary algorithms at Word-RAM level with only poly-log overhead. |

### D. LLM 与生成式模型评测及可靠性 / LLM & Generative Model Evaluation & Reliability

| 论文 / Paper | 一句话总结 / TL;DR |
| --- | --- |
| [[2606.20128]] | 种子化 fuzzing + fp64 参考暴露 KernelBench/TritonBench 的"正确性幻觉" / Seeded fuzzing + fp64 reference exposes KernelBench/TritonBench "correctness illusions". |
| [[2606.19704]] | 立场论文：用预测效度替代静态排行榜均值评 LLM 智能体 / Position paper: replace static-leaderboard means with predictive validity for LLM agents. |
| [[2606.19868]] | 24 种黑盒 LLM 不确定性方法系统评测，无单一方法持续占优 / Systematic eval of 24 black-box LLM uncertainty methods; no single winner. |
| [[2606.20536]] | FID 是种子面板上的随机变量，重训离散是重采样的 3.2x；提 GS-FID / FID is a random variable over seed panels; retraining variance is 3.2x resampling; propose GS-FID. |
| [[2606.20205]] | LLM "心理画像"差异 81-90% 来自方向性响应偏差而非真实特质 / LLM "psychological profiles" are 81-90% a directional-response-bias measurement artifact. |
| [[2606.20155]] | 全黑盒行为探针 + NAMESAKES 基准判别 T2I 身份记忆 / Fully black-box behavioral probe + NAMESAKES benchmark for T2I identity memorization. |
| [[2606.20502]] | 微调漏洞检测 LLM 是"校准而无理解"，最强仅 52.1% / Fine-tuned vuln-detection LLMs are "calibration without comprehension"; best only 52.1%. |
| [[2606.20312]] | RPC 后处理分数校准提升冻结视频异常检测器帧级 AUROC / RPC post-hoc score calibration boosts frozen video-anomaly AUROC. |

### E. 智能体、自演化与自动化研究 / Agents, Self-Evolution & Automated Research

| 论文 / Paper | 一句话总结 / TL;DR |
| --- | --- |
| [[2606.19893]] | MetaResearcher 四维协同框架，但是无实验结果的立场论文 / MetaResearcher is a 4-axis framework but a position paper with no real experiments. |
| [[2606.19980]] | ENPIRE 真实世界双臂机器人车队上的物理自研究回路 / ENPIRE: physical autoresearch loop on a real dual-arm robot fleet. |
| [[2606.20122]] | ScaffoldAgent 用效用引导动态大纲优化开放式深度研究 / ScaffoldAgent does utility-guided dynamic outline optimization for open-ended deep research. |
| [[2606.19749]] | 系统评测四类智能审稿系统，最佳达 83% 成对准确率 / Systematic eval of four agentic review systems; best reaches 83% pairwise accuracy. |
| [[2606.20002]] | 阿里 CoD 用端到端 RL 训练长生命周期智能体跨域泛化 / Alibaba CoD trains long-lifecycle cross-domain agents via end-to-end RL. |
| [[2606.19990]] | "Reward as Agent" 代理式奖励 + 动态感知随机 rollout 改进具身世界模型 RL / "Reward as an Agent" + dynamics-aware stochastic rollout improves embodied-world-model RL. |
| [[2606.20475]] | MAA 用边际优势 EMA 累积做后处理式记忆自演化 / MAA does post-hoc memory self-evolution via marginal-advantage EMA accumulation. |
| [[2606.20537]] | 执行状态胶囊在 RTX 5090 实现亚毫秒级 GPU 驻留快照/恢复 / Execution-state capsules give sub-ms GPU-resident snapshot/restore on RTX 5090. |
| [[2606.19998]] | Tri-Info 用三信息论信号 + 共形预测在线检测 VLA 失败 / Tri-Info detects VLA failures online via three info-theoretic signals + conformal prediction. |

### F. 安全、验证与确定性 / Safety, Verification & Determinism

| 论文 / Paper | 一句话总结 / TL;DR |
| --- | --- |
| [[2606.20510]] | DRO + 多项式 SDP 松弛给 AI Agent 策略违反概率 sound 上界 / DRO + polynomial SDP relaxation gives sound policy-violation-probability bounds for AI agents. |
| [[2606.19753]] | 确定性封装生成模型的原子原语；"temperature=0 即确定性"是错觉 / Atomic primitives for deterministically encapsulating generative models; "temp=0 ⇒ deterministic" is a myth. |
| [[2606.19899]] | RAND 报告：生物 agentic 评估的隐性设计选择如何塑造结论 / RAND report: how hidden design choices in bio-agentic evals shape conclusions. |

### G. 数学与算法基础、理论及终身知识 / Mathematical & Algorithmic Foundations, Theory & Lifelong Knowledge

| 论文 / Paper | 一句话总结 / TL;DR |
| --- | --- |
| [[2606.19876]] | 反向 Fisher 散度 score matching 在高斯混合下以高概率全局收敛 / Reverse-Fisher score matching converges globally w.h.p. for Gaussian mixtures. |
| [[2606.19878]] | PPI-GD 把插值梯度下降的数据维条件放宽到 d=O(log^γ n) / PPI-GD relaxes interpolation-GD data-dimension condition to d=O(log^γ n). |
| [[2606.20469]] | Fisher 几何尖锐度的重标定不变性与 SGD 平坦偏置 / (见 C 组 / see group C) |
| [[2606.20299]] | 物理学视角综述深度学习训练与泛化的统计特性 / Physics-perspective review of statistical properties of DL training & generalization. |
| [[2606.19741]] | EPB 把神经组合优化策略蒸馏为可读程序并揭示决策瓶颈 / EPB distills NCO policies into readable programs and reveals decision bottlenecks. |
| [[2606.19924]] | 自生目的 AI 的统一框架；嵌入性是必要非充分条件 / Unified framework for Autotelic AI; embeddedness is necessary but not sufficient. |
| [[2606.19679]] | LOKI 无需历史数据的终身知识编辑，权重零空间投影保留旧知识 / LOKI: history-free lifelong knowledge editing via weight-null-space projection. |

---

## All Papers

| # | 论文 / Paper | 简称 / Short Title | 一句话总结 / TL;DR |
| --- | --- | --- | --- |
| 1 | [[2606.19679]] | LOKI | 零空间约束的免历史终身知识编辑 / History-free lifelong editing via null-space projection. |
| 2 | [[2606.19697]] | CoT-Algorithms | CoT Transformer 在 Word RAM 层仅多对数开销模拟算法 / CoT Transformers simulate algorithms at Word-RAM level poly-log overhead. |
| 3 | [[2606.19704]] | Predictive Validity | 用预测效度替代静态排行榜评智能体 / Predictive validity over static leaderboards for agents. |
| 4 | [[2606.19741]] | EPB | NCO 策略蒸馏为可读程序揭示瓶颈 / Distill NCO into readable programs, reveal bottlenecks. |
| 5 | [[2606.19744]] | Sequential DPO | 顺序 DPO 无统一遗忘模式，梯度对抗非主因 / No uniform forgetting in sequential DPO. |
| 6 | [[2606.19749]] | Agentic Review | 评测四类智能审稿系统，最佳 83% / Eval four agentic review systems; best 83%. |
| 7 | [[2606.19750]] | Manifold Bandits | 流形 Bandit + 层次 Thompson 课程学习 / Manifold bandits + hierarchical Thompson curriculum. |
| 8 | [[2606.19753]] | Grounded Inference | 确定性封装生成模型的原子原语 / Atomic primitives to encapsulate generative models. |
| 9 | [[2606.19771]] | ICT | JS 散度选独特 token 做稀疏梯度更新 / JS-divergence distinctive-token sparse updates. |
| 10 | [[2606.19818]] | UARM | 分位数共形不确定性重加权 GRPO 抑制奖励黑客 / Quantile-conformal reweighting curbs reward hacking. |
| 11 | [[2606.19831]] | Control-Window Law | 单神经元干预：杠杆不等于触及 / Single-neuron steering: leverage ≠ reach. |
| 12 | [[2606.19868]] | Black-Box UQ | 24 种黑盒 LLM 不确定性方法系统评测 / Systematic eval of 24 black-box UQ methods. |
| 13 | [[2606.19876]] | Reverse Fisher SM | 反向 Fisher score matching 高斯混合全局收敛 / Reverse-Fisher SM global convergence for GMM. |
| 14 | [[2606.19878]] | PPI-GD | 插值梯度下降数据维条件放宽到 d=O(log^γ n) / Interpolation-GD dimension condition relaxed. |
| 15 | [[2606.19893]] | MetaResearcher | 四维协同自研究框架，无真实实验 / 4-axis self-research framework, no real experiments. |
| 16 | [[2606.19899]] | Bio Agentic Risk | RAND 报告：生物 agentic 评估的隐性设计选择 / RAND: hidden choices in bio-agentic evals. |
| 17 | [[2606.19924]] | Autotelic AI | 自生目的 AI 统一框架，嵌入性必要非充分 / Autotelic AI framework; embeddedness necessary. |
| 18 | [[2606.19941]] | Compositionality | 组合性只在狭窄连接-深度甜区涌现 / Compositionality in narrow depth-connectivity sweet spot. |
| 19 | [[2606.19946]] | GEMS | 几何约束无训练并行多语义激活注入 / Geometric training-free multi-semantic steering. |
| 20 | [[2606.19980]] | ENPIRE | 真实机器人车队上的物理自研究回路 / Physical autoresearch loop on real robot fleet. |
| 21 | [[2606.19989]] | ODB | batch 延迟到真实代价点，DGAP 无死锁 / Defer batching to true-cost points; deadlock-free. |
| 22 | [[2606.19990]] | Reward-as-Agent | 代理式奖励 + 动态随机 rollout 改进具身 RL / Agentic reward + dynamic rollout for embodied RL. |
| 23 | [[2606.19998]] | Tri-Info | 三信息信号 + 共形预测在线检测 VLA 失败 / Three info signals + conformal VLA failure detection. |
| 24 | [[2606.20002]] | Connect-the-Dots | 端到端 RL 训练长生命周期跨域智能体 / E2E RL for long-lifecycle cross-domain agents. |
| 25 | [[2606.20008]] | VIMPO | 隐式价值函数无 critic 的 LLM 策略优化 / Critic-free value-implicit LLM policy optimization. |
| 26 | [[2606.20068]] | Lean-Process-RL | Lean 过程级奖励融入 GRPO 定理证明 / Lean process rewards into GRPO for theorem proving. |
| 27 | [[2606.20075]] | Latent-CoT-IT | 潜在 CoT 双重坍缩与信息-性能绑定 / Latent-CoT dual collapse + Information-Performance Binding. |
| 28 | [[2606.20077]] | VLM Visual Evolution | in-context 视觉 token 渐进语义演化偏高频 / In-context visual tokens drift to high-frequency. |
| 29 | [[2606.20097]] | HydraHead | 因果定位稀疏检索头 + FA/GDN 混合长上下文 / Causally locate retrieval heads + FA/GDN hybrid. |
| 30 | [[2606.20122]] | ScaffoldAgent | 效用引导动态大纲优化深度研究 / Utility-guided dynamic outline for deep research. |
| 31 | [[2606.20128]] | Kernel Correctness | 种子化 fuzzing 暴露 GPU 内核"正确性幻觉" / Seeded fuzzing exposes GPU-kernel correctness illusions. |
| 32 | [[2606.20152]] | Essay-Quality-Reps | 作文质量表示线性可解码随层深涌现迁移 / Essay-quality reps linearly decodable, depth-emergent. |
| 33 | [[2606.20155]] | NAMESAKES | 黑盒探针 + 基准判别 T2I 身份记忆 / Black-box probe + benchmark for T2I identity memory. |
| 34 | [[2606.20195]] | Sketch Rounding | CountSketch 嵌入对 FP16 舍入不敏感 / CountSketch robust to FP16 rounding. |
| 35 | [[2606.20205]] | LLM Psychometry | LLM 心理画像 81-90% 是测量伪影 / LLM psych profiles 81-90% measurement artifact. |
| 36 | [[2606.20225]] | Emergent Misalignment | 差分均值方向 99.6% 分离并因果抑制不对齐 / Diff-in-means 99.6% separates & suppresses misalignment. |
| 37 | [[2606.20299]] | Training Stats Review | 物理视角综述训练与泛化统计特性 / Physics review of training & generalization stats. |
| 38 | [[2606.20312]] | RPC Calibration | 后处理分数校准提升视频异常 AUROC / Post-hoc calibration boosts video-anomaly AUROC. |
| 39 | [[2606.20347]] | Percolation Interp | 临界渗流作解析可控合成可解释性数据 / Critical percolation as tractable synthetic interp data. |
| 40 | [[2606.20381]] | UFP4 | 揭示并修复 FP4 预训练几何收缩偏置 / Expose & fix FP4 shrinkage bias. |
| 41 | [[2606.20431]] | Superposition-Forgetting | superposition 随 replay 上升，脆弱区可定位 / Superposition rises under replay; vulnerable regions localized. |
| 42 | [[2606.20451]] | SSH-Net | 结构化分段危险率网络预测 GPU 失效时间 / Structured piecewise-hazard net for GPU failure time. |
| 43 | [[2606.20469]] | Fisher Sharpness | Fisher 几何尖锐度重标定不变，SGD 偏平坦 / Fisher-geometric sharpness reparam-invariant; SGD favors flat. |
| 44 | [[2606.20474]] | UltraQuant | FP4 KV 缓存折叠进 MFMA，P50 延迟降 3.47x / FP4 KV cache into MFMA, P50 latency -3.47x. |
| 45 | [[2606.20475]] | MAA | 边际优势 EMA 累积后处理记忆自演化 / Marginal-advantage EMA post-hoc memory self-evolution. |
| 46 | [[2606.20502]] | Vuln Detection | 微调漏洞检测是"校准而无理解" / Fine-tuned vuln detection is "calibration w/o comprehension". |
| 47 | [[2606.20510]] | Probabilistic Verify | DRO+SDP 松弛给 Agent 违反概率 sound 上界 / DRO+SDP sound bound on agent violation prob. |
| 48 | [[2606.20536]] | FID Lottery | FID 是种子面板随机变量，重训离散 3.2x 重采样 / FID variance: retrain CoV 3.2x resampling; GS-FID. |
| 49 | [[2606.20537]] | Exec-State Capsules | 计算图边界可恢复状态，亚毫秒 GPU 快照/恢复 / Graph-bound recoverable state, sub-ms snapshot/restore. |
| 50 | [[2606.20560]] | DiffusionGemma | top-k/p 瓶颈把扩散 LM 不透明深度压到 1.1x / Top-k/p bottleneck cuts diffusion-LM opacity to 1.1x. |

---

**计数核对 / Count check:** Papers in `All Papers` table = 50. Files in `2026-06-19/2606.*.md` = 50. No discrepancy / 无出入。
