---
title: "Daily arXiv Digest — 2026-07-28"
date: 2026-07-28
tags:
  - LLM security
  - mechanistic interpretability
  - activation steering
  - LLM agents
  - multi-agent systems
  - AI for science
  - benchmark evaluation
  - PEFT / LoRA
  - optimization theory
  - Bayesian deep learning
  - uncertainty quantification
  - causal inference / distribution shift
  - foundation models
  - retrieval-augmented generation
papers: 50
---

## 今日必读 / Must Read Today

### [[2607.25865]] OmniQEC: AI Scientist Discovers Quantum Error-Correcting Codes

OmniQEC 让 LLM 智能体直接以电路级逻辑错误率（而非代码级代理指标 kd²/n）为优化目标搜索 qLDPC 码，在 240 物理比特预算下发现的码超过了人工设计的 BB [[144,12,12]] 基准，个别前沿码逻辑错误率比 BB [[72,12,6]] 低 29.23 倍，是一次罕见的"AI 智能体真正发现优于人类设计的科学结果"的案例。
OmniQEC has an LLM-driven "fast-slow" agent loop directly optimize circuit-level logical error rate to discover qLDPC codes that beat the human-designed bivariate-bicycle benchmark at matched qubit budgets (surpassing BB [[144,12,12]] at N=240), with one frontier code reaching a 29.23x lower logical error rate than BB [[72,12,6]] — a rare case of an AI agent genuinely outperforming a hand-engineered scientific artifact rather than just matching it.

### [[2607.25467]] CVMA: A Causal Audit of Visual KV Memory in Multimodal Dialog

论文用配对因果干预（区域/整图/图文析因剔除）证明，主流多模态大模型视觉 KV 缓存淘汰所依赖的"当前注意力越高越重要"假设其实与未来区域效用负相关（Idefics3-8B 在 2×2 粒度下 Spearman 达 -0.576），意味着现有淘汰方法系统性地丢弃了真正有用的视觉信息。
Through paired causal interventions (region/whole-image/text-image factorial ablation), this paper shows current-turn attention is *negatively* correlated with a visual region's actual future utility (Spearman as low as -0.576 for Idefics3-8B), meaning today's attention-based visual-KV eviction methods for multimodal LLMs are optimizing exactly the wrong signal.

### [[2607.25292]] Instruction-Tuned LLMs Cannot Sample What They Can Describe

论文发现指令微调后的模型逐次调用采样时会坍缩为几乎固定的单一答案（合成任务上超过 94% 的调用返回同一结果），但同一模型能在一次调用内准确"描述"整个目标分布，直接挑战了"LLM 逐次调用即独立采样"这一被广泛默认却从未验证的假设，并给出两种零额外成本的修复方案。
This paper shows instruction-tuned LLMs collapse to a single modal answer in over 94% of independent per-call samples on synthetic tasks, yet the same model can accurately describe the full target distribution in one call — directly challenging the widely assumed but never-validated premise that "one API call equals one independent sample," and offering two zero-extra-cost fixes (single-call description; Prompt-Perturbed Argyle, which cuts survey-simulation TV error by 21%).

## 按主题分类 / Papers by Topic

### LLM/VLM 安全与对抗攻击 / LLM/VLM Security & Adversarial Attacks

| Paper | Bilingual Takeaway |
|---|---|
| [[2607.25227]] CogBias Bit-Flip Attack | 翻转 12 个权重比特即可让 LLM 在特定话题上产生稳定认知偏见（ASR 84.6%），且困惑度几乎不变，隐蔽性极强。/ Flipping just 12 quantized weight bits hijacks an LLM's stance (84.6% ASR) while perplexity rises only 0.06%, a stealthy hardware-level attack. |
| [[2607.25479]] Architectural Backdoors in VLM Supply Chains | 首个无需投毒训练数据的 VLM 架构后门，通过植入触发门控引导向量在多个 VLM 上达到 100%/98.7% 攻击成功率。/ The first data-free architectural backdoor for VLMs achieves up to 100% attack success via a trigger-gated steering vector baked into the compute graph. |
| [[2607.25814]] Adversarial Robustness in Arabic LMs | 变音符号插入可让 AraBERT 准确率从 94% 暴跌至 2%，释义改写攻击平均造成 76% 准确率下降，对抗训练对字符级噪声防御有限。/ Diacritics insertion crashes AraBERT from 94% to 2% accuracy; paraphrase attacks cut all models by 76% on average, and adversarial training barely defends character-level noise. |
| [[2607.25451]] Verbatim Extraction Under Quantization | 四比特量化在 1B 模型上仍保留约 72% 的已记忆序列且困惑度仅损失 4%，证明量化并非有效的隐私防护手段。/ 4-bit quantization at 1B scale still retains 71.8% of memorized-sequence extraction while keeping 95.9% of capability, showing quantization is not a privacy defense. |

### 机制可解释性与注意力分析 / Mechanistic Interpretability & Attention Analysis

| Paper | Bilingual Takeaway |
|---|---|
| [[2607.25270]] Activation Source Selection for Steering | "答案均值"这一常见 steering 向量构造方式反而是最弱条件（成功率仅 0.198），作者提出的 tail subtraction 把 Diff-Mean 成功率从 0.288 提升到 0.863。/ The common "average activations from answers" recipe is the weakest steering source (0.198 success); the proposed tail-subtraction method lifts Diff-Mean success from 0.288 to 0.863. |
| [[2607.25467]] CVMA Causal Visual KV Audit | 用配对因果干预证明多模态大模型的注意力与视觉区域未来效用负相关（Idefics3-8B 达 Spearman -0.576），现有视觉 KV 淘汰方法系统性失准。/ Paired causal interventions show attention is negatively correlated with future visual-region utility (Spearman -0.576 for Idefics3-8B), undermining current attention-based visual-KV eviction methods. |
| [[2607.25907]] Suppressing Evaluation-Awareness Latents | 用离散提示优化可把"评估感知"内部特征压到零附近，但严格行为学检验显示这不等于改变模型是否"觉得自己在被测"的实际判断——激活可读不等于行为可控。/ Discrete prompt optimization zeros out an internal "evaluation-awareness" feature, yet behavioral tests show this does not change whether the model actually acts as if being evaluated — activation-readability is not behavioral controllability. |
| [[2607.25244]] CADENCE: Cardiac Atom Dictionary | 稀疏自编码器把 ECG 基础模型表征分解为 8,192 个"心脏原子"，最优单原子 AUROC 达 0.88-0.90，显著超过稠密维度，且在外部队列上免重训迁移成功。/ A BatchTopK SAE decomposes an ECG foundation model into 8,192 "cardiac atoms" whose best-atom AUROC (0.88-0.90) beats raw dense dimensions and transfers zero-shot to an external cohort. |
| [[2607.25459]] Latent-State Computation in SV Transformers | 在受控随机波动率仿真中，单层 Transformer 学到"隐状态推断+滤波"两阶段计算，长周期下可精确还原为线性投影+归一化的显式滤波器。/ In a controlled stochastic-volatility simulation, a 1-layer Transformer's computation collapses exactly to a closed-form linear-projection-plus-normalization filter in long-cycle regimes, verified by causal ablation. |
| [[2607.25507]] RoPE Phase Structure & Governance | 纯理论文章，把 RoPE 注意力分数精确分解为幅值加权余弦项并证明相位偏移稳定性引理，但全文无实验，且作者存在商业产品利益冲突。/ A pure theory paper decomposing RoPE attention scores into cosine terms with a proven stability lemma, but with zero experiments and a disclosed commercial conflict of interest. |
| [[2607.25279]] Many-Body Tipping Dynamics of LLMs | 把注意力重述为两体自旋相互作用，推导零拟合参数的"倾覆阈值"公式，在 7 个模型上 19/21 命中率，但仅测试了未经 RLHF 对齐的小模型。/ Attention is reframed as a two-body spin interaction yielding a zero-free-parameter tipping-threshold formula that scores 19/21 across 7 models — but none of the tested models are RLHF-aligned chat models despite the "ChatGPT-like" framing. |
| [[2607.25873]] How Do LLMs Read Bug Reports? | 对 319 个真实 bug 做扰动式归因分析，发现修复成功对应跨多组件的"扩散型注意力"，失败修复则集中于低诊断价值的元数据。/ Perturbation-based attribution on 319 real bugs shows successful LLM repairs correspond to attention diffused across multiple bug-report components, while failures concentrate on low-value metadata. |

### LLM 智能体与多智能体系统 / LLM Agents & Multi-Agent Systems

| Paper | Bilingual Takeaway |
|---|---|
| [[2607.25415]] Frozen LLM Agent Harness Learning | 在真实的小 episode 预算下，DSPy 静态 prompt 基线普遍持平或超过在线 bandit/REINFORCE 自适应 harness 控制器，是一个诚实的反例结果。/ Under realistic small episode budgets, a static DSPy-generated prompt baseline matches or beats online bandit/REINFORCE harness controllers — an honestly reported negative result. |
| [[2607.25656]] OrchBench: Evaluating Orchestration Plans | 用确定性模拟器给编排计划打分，与真实执行质量相关系数 r=0.816，但去掉一个模型后相关性骤降到 0.421，headline 结果较脆弱。/ A deterministic simulator scores orchestration plans at r=0.816 correlation with real execution — but removing one model from the six-model sample drops it to 0.421, a fragile headline result. |
| [[2607.25877]] Bayesian Network Runtime Monitoring for MAS | 把多智能体各阶段的置信度校准后接入贝叶斯网络传播不确定性，Qwen2.5-7B 后端在扰动数据集上错误检测率达 90%，远超其他两个后端。/ Calibrated per-agent confidence feeds a Bayesian Network to propagate uncertainty across a multi-agent actuarial pipeline; the Qwen2.5-7B backend reaches 90% error-detection vs. 45-65% for others. |
| [[2607.25904]] Interactive Reward Agent (IRA) | "先提出完成条件、再用工具核验环境状态"的评判框架在新基准上达到 86.9% 准确率，比最强被动 VLM 基线高 8.1 个百分点，并可直接作为 RL 奖励。/ A propose-then-verify GUI-task judge reaches 86.9% accuracy (+8.1pp over the strongest passive VLM baseline) and works directly as an RL reward signal. |
| [[2607.25886]] RSIBench-Data: Recursive Self-Improvement | 固定训练/评测基础设施后让智能体反复做数据为中心的后训练研究，智能体在 58% 设置中能超越首次尝试，但持续搜索反而在 78% 情形下退步。/ With training/eval infrastructure frozen, agents beat their own first attempt in 58% of settings, yet continued search regresses in 78% of cases where it keeps going — discovery is possible but unreliable. |
| [[2607.25675]] DecoEvo: Score-Decoupled Rubric Co-Evolution | 让评分标准生成器只靠与聚合分数无关的审计信号更新，避免评分标准被优化对象"带偏"，在五个基准上全面超过 SkillOpt（相对提升 2.8%-5.0%）。/ Decoupling rubric-generator updates from the solver's own proxy score avoids rubric drift, beating SkillOpt on all 15 backbone-benchmark pairs by 2.8-5.0% relative. |

### AI 科研辅助与基准可靠性 / AI for Science & Benchmark/Evaluation Reliability

| Paper | Bilingual Takeaway |
|---|---|
| [[2607.25865]] OmniQEC: AI Scientist for QEC | 见"今日必读"。/ See "Must Read Today" above — LLM agent discovers qLDPC codes beating human-designed benchmarks. |
| [[2607.25672]] AI Literature Review Capability (I) | 人类与 2025 年中 LLM 的文献选择重合率不到 6%，AI 生成参考文献 3% 彻底虚构、64% 元数据有误，但 2026 年新模型重跑单个课题实现零虚构。/ Human vs. mid-2025 LLM literature picks overlap <6%; 3% of AI references are fabricated and 64% have metadata errors, though a 2026 model re-run achieved zero fabrications on one spot-check project. |
| [[2607.25881]] AI Proposal Writing & Review Bias (II) | 人类评审对人类/AI 提案打分几乎无差异，但两个 AI 评审模型系统性地给 AI 撰写的提案多打约 1 分（5 分制），人类评审组无此偏向。/ Human reviewers score human- and AI-written proposals almost identically, but AI reviewer models systematically rate AI-written proposals ~1 point higher on a 5-point scale — a pro-AI bias absent from the human panel. |
| [[2607.25554]] Time-Truncation Harness for Forecasting | 动态屏蔽截止日期后的检索结果合成无泄漏时序推理数据，蒸馏后模型在 ForecastBench 上 Brier Score 比无该硬件基线降低 19-22%。/ Dynamically truncating retrieval to a pre-event cutoff synthesizes leak-free forecasting trajectories; distilled models cut ForecastBench Brier Score by 19-22% over a no-harness ablation. |
| [[2607.25589]] Forensic Audit of a Radiology VLM Benchmark | 作者自我审计发现此前基准存在提示词绑定 bug、DICOM 极性反转、患者非独立等多重缺陷，撤回所有性能结论并提出八条款"可验证基准契约"。/ A self-audit uncovers a prompt-binding bug, inverted DICOM polarity, and non-independent patients in the author's own prior benchmark; all performance claims are withdrawn in favor of an 8-clause verifiable benchmark contract. |
| [[2607.25257]] Laplace-PSN-IRT for LLM Benchmarks | 给神经网络 IRT 模型加装后验校准后发现，12 个模型的 66 对两两比较中只有 2 对能被统计显著区分，多数榜单排名差异不可信。/ Adding posterior calibration to a neural IRT model reveals only 2 of 66 pairwise LLM-ability comparisons are statistically distinguishable — most leaderboard rank differences are not trustworthy. |

### 高效微调 (PEFT/LoRA) / Efficient Fine-Tuning (PEFT/LoRA)

| Paper | Bilingual Takeaway |
|---|---|
| [[2607.25299]] Manifold-LoRA (Stiefel/Oblique) | 证明免收缩、免调参的 Stiefel 流形着陆算法，将其用于 LoRA 后在 SQuADv2.0 上 F1 从 88.81 提升到 89.22，训练收敛快近 2 倍。/ A retraction-free, tuning-free Stiefel-manifold optimizer applied to LoRA lifts SQuADv2.0 F1 from 88.81 to 89.22 while converging nearly 2x faster. |
| [[2607.25583]] LoRA Rank/Quantization on a 60M Model | 在 T5-small 上系统消融发现 LoRA r=16 是帕累托最优点（59.6% vs 全量微调 71.2%），QLoRA NF4 量化仅损失约 0.2 个百分点精度换取 62-74% 显存节省。/ A controlled ablation on T5-small finds LoRA r=16 is Pareto-optimal (59.6% vs. 71.2% full fine-tuning), and QLoRA NF4 trades only ~0.2pt accuracy for 62-74% memory savings. |
| [[2607.25663]] Localized Adaptation Geometries | 不同学习目标存在不同的最优 LoRA 适配层深度——词汇绑定适合早层，事实关联适合晚层（晚层迁移比早层高 42.7 个百分点）。/ Different learning objectives have distinct optimal LoRA adaptation depths — lexical binding favors early layers, factual association favors late layers (42.7pp higher transfer). |

### 优化理论与神经网络理论 / Optimization Theory & Neural Network Theory

| Paper | Bilingual Takeaway |
|---|---|
| [[2607.25480]] Data-Dependent Regret for Constrained OCO | 对已有 OGD-Polyak 算法给出更紧的数据依赖 regret 界，无需改动算法即在合成实验中把 regret 上界收紧 38-43%。/ A tighter, data-dependent regret analysis of the existing OGD-Polyak algorithm (no algorithm change) tightens the bound by 38-43% in synthetic experiments. |
| [[2607.25785]] MC-ALFCG: Markovian Conditional Gradient | 把 Frank-Wolfe 方差缩减方法扩展到单条马尔可夫链采样场景，证明了样本复杂度保证，但承认投影式 SGD 基线在绝对指标上仍更优。/ Extends variance-reduced Frank-Wolfe to single-trajectory Markovian sampling with proven complexity bounds, while honestly noting projected-SGD still wins on absolute gap in every tested column. |
| [[2607.25624]] Quotient Dynamics of Quadratic Networks | 严格证明正定二次网络的欧氏训练精确投影为秩-r PSD 流形上的黎曼梯度流，但证明的样本复杂度界比实测宽松约十四个数量级。/ Proves Euclidean training of positive quadratic networks projects exactly onto Riemannian gradient flow on a rank-r PSD manifold, though the proven sample bound is ~14 orders of magnitude looser than empirical recovery. |
| [[2607.26001]] SpecSAM: SAM Meets Muon | 把 SAM 的内层扰动改为按谱范数（Muon 式正交化）逐层扰动，与 Muon 外层更新搭配在 ImageNet-1K ViT-S 上达到 80.23% Top-1（+5.28 点）。/ Replacing SAM's inner perturbation with a Muon-style spectral-norm step, paired with Muon's outer update, reaches 80.23% Top-1 on ViT-Small/ImageNet-1K, +5.28pt over unperturbed Muon. |
| [[2607.25200]] Constant-Depth vs Log-Depth Separation | 首个常数深度与对数深度网络间的"算法可学习性"分离证明：对数深度网络可多项式时间学到分层楼梯函数，常数深度网络的逼近误差恒 ≥1/4。/ The first algorithmic (not just approximation-theoretic) depth separation between constant- and logarithmic-depth networks, with a provable ≥1/4 L² error floor for constant-depth networks. |
| [[2607.25163]] Riemannian Active Subspaces | 将欧氏"active subspaces"严格推广到黎曼流形，证明内蕴平行输运构造与外蕴嵌入投影构造只在 O(R²) 阶上一致，并揭示后者的一个退化失效模式。/ Generalizes Euclidean active-subspace construction to Riemannian manifolds, proving intrinsic and extrinsic constructions agree only to O(R²) and exposing a degenerate failure mode of the naive extrinsic approach. |

### 贝叶斯机器学习与不确定性量化 / Bayesian ML & Uncertainty Quantification

| Paper | Bilingual Takeaway |
|---|---|
| [[2607.25312]] Optimizer-Derived Posterior Geometry | 复用 AdamW 训练留下的动量统计量作为 SGHMC 采样阶段的预条件子，免去昂贵的尺度自适应预热，LPPD 相对 Deep Ensemble 提升 7.3-10.1%。/ Reusing AdamW's terminal moment statistics as SGHMC's preconditioner eliminates costly scale-adaptation warmup, improving LPPD by 7.3-10.1% over Deep Ensemble baselines. |
| [[2607.25376]] Student's t Likelihood for BNNs | 无论数据真实噪声分布如何，固定自由度的重尾 Student's t 似然几乎总比默认高斯似然更准，在电力需求预测上 CRPS 降低约 16%。/ Regardless of the true noise distribution, a fixed-df Student's t likelihood almost always beats the default Gaussian likelihood, cutting CRPS by ~16% on electricity-demand forecasting. |
| [[2607.25665]] Hölder-Bayes: Joint Model-Contamination Inference | 把污染比例纳入广义贝叶斯联合后验推断，在 20% 异常值注入下数据清洗精确率/召回率达 0.973/0.996，远超三种无监督异常检测基线。/ Jointly inferring contamination proportion within a generalized Bayesian posterior reaches 0.973/0.996 precision/recall for data cleaning under 20% injected contamination, far beating three unsupervised outlier-detection baselines. |
| [[2607.25441]] PIcsC: Partitioning-Induced Shift Correction | 用 Fisher 信息矩阵统一修正交叉验证分片偏移与联邦学习客户端异构，在 CIFAR-100 分片场景下把准确率从 38.2% 修复到 58.7%。/ A Fisher-Information-Matrix regularizer unifies cross-validation fold shift and federated client heterogeneity, recovering CIFAR-100 accuracy from 38.2% to 58.7% under fragmentation. |

### 因果推断、分布偏移与模型比较 / Causal Inference, Distribution Shift & Model Comparison

| Paper | Bilingual Takeaway |
|---|---|
| [[2607.25532]] Spurious Intra-Variable Signal Routing | 证明当因果信号与虚假信号打包进同一特征的不同子空间时，线性 ICL 与 TabPFN 都不可避免地"路由"到虚假信号，S-swap 增强可将 TabPFN 的 CSR 降低 98.8%。/ Proves in-context learners (linear ICL and TabPFN) unavoidably route to spurious signal when causal and spurious signals share one observed feature; S-swap augmentation cuts TabPFN's routing ratio by 98.8%. |
| [[2607.25546]] Post-Hoc Causal Feature ID (NSR) | 提出免重训、模型无关的归一化敏感度比诊断已训练模型依赖因果还是伪相关特征，在 UCI 自行车共享数据上 Precision@7 达 0.75，超过 LASSO 基线 17 个百分点。/ A retraining-free, model-agnostic Normalised Sensitivity Ratio diagnoses causal vs. spurious feature reliance, reaching Precision@7=0.75 on UCI Bike-Sharing, 17 points above a LASSO baseline. |
| [[2607.26000]] OOD Performance of Tabular FMs | 首次系统评测 9 个表格基础模型在真实分布偏移下的表现，发现真实数据预训练模型绝对性能最高但偏移退化差距也最大，暴露其优势来自域内拟合而非真鲁棒性。/ The first systematic OOD study of 9 tabular foundation models finds real-data-pretrained models have the best absolute OOD accuracy but also the largest shift gap, revealing their edge comes from in-distribution fit, not genuine robustness. |
| [[2607.25273]] HEAD-CP: Heterophily-Aware Conformal Prediction | 指出图上一致预测扩散基线 DAPS 隐含同质性假设，在异质图上预测集平均增大 10.6%；作者的逐节点方案在 8/10 数据集上显著更优。/ Standard graph conformal-prediction diffusion (DAPS) implicitly assumes homophily and inflates prediction sets by 10.6% on heterophilic graphs; a per-node fix wins significantly on 8/10 benchmarks. |
| [[2607.25680]] Rashomon Alignment | 提出用特征空间均匀采样点衡量两模型的几何一致性，发现准确率相同的模型可能只在 45% 的实例空间上意见一致，揭示准确率单独会掩盖结构性差异。/ Measuring model agreement on uniformly sampled synthetic points reveals two equally-accurate models (SVM-RBF and MLP, both 0.94) can agree on only 45% of the instance space — accuracy alone masks structural dissimilarity. |

### 领域基础模型与科学应用 / Domain-Specific Foundation Models & Scientific Applications

| Paper | Bilingual Takeaway |
|---|---|
| [[2607.25497]] CRoMa: Pathology FM Robustness Margin | 指出现有病理基础模型鲁棒性指标 RI 因固定近邻窗口而只对 9.6%-46.3% 样本打分，提出逐样本 CRoMa 后发现所有 20 个模型都存在混杂主导的最差十分位。/ Existing pathology-FM robustness metric RI silently scores only 9.6%-46.3% of samples due to a fixed-k window; the proposed per-sample CRoMa reveals every one of 20 tested encoders has a confounder-dominated worst decile. |
| [[2607.25748]] Loss Invariance in Echocardiography CBM | 证明仅用射血分数训练的容积概念瓶颈层会因比值不变性坍缩到几乎零方差的容积预测，加入毫升级监督后 EDV 误差从 89.8 降到 25.8。/ A volume concept-bottleneck trained only on ejection fraction collapses to near-zero-variance volume predictions due to ratio invariance; adding millilitre-level supervision drops EDV error from 89.8 to 25.8 mL. |
| [[2607.25199]] RIDGE: Validation-Driven Option Pricing Discovery | 自主验证框架把 LLM 生成的期权定价代码诊断分从 31-58/100 提升到 96-99/100，并推动 LLM 自主发现新的半解析定价方法，隐含波动率误差再降 1-3 个数量级。/ An autonomous validation loop lifts LLM-generated option-pricing code from 31-58/100 to 96-99/100 diagnostic score and triggers a self-discovered semi-analytic pricing method that cuts implied-vol error by 1-3 orders of magnitude. |
| [[2607.25929]] DGMs vs Non-Stationary Gaussian Fields | 用已知协方差结构的非平稳高斯随机场基准检验生成模型，发现 VAE 协方差恢复误差是 oracle 的约 66 倍，而常用的 CRPS 指标完全无法揭示这一差距。/ A known-ground-truth non-stationary Gaussian random field benchmark reveals VAE covariance-recovery error is ~66x the oracle floor, a gap the widely used CRPS metric completely fails to detect. |
| [[2607.25988]] GARI: Generator-Aligned Soft Equivariance | 把群结构从硬编码算子转为暴露给通用序列骨干的"生成元索引流"接口，在 ImageNet-1K 上纯泛化旋转准确率比 Vision Mamba 基线提升 1.34 个百分点。/ Exposes group generators as a multi-stream interface around a generic sequence backbone instead of hard-coding equivariant operators, improving pure-generalization rotation accuracy by 1.34pp over a Vision Mamba baseline. |
| [[2607.25494]] noisyfloat: Automated Numerical Stability Analysis | 首次把 CESTAC 随机算术嵌入 PyTorch/JAX 张量算子，对稳定/不稳定算子分类达到 100% 准确率，但运行时开销高达 127.6-1124.3 倍。/ First integration of CESTAC-style stochastic arithmetic natively into PyTorch/JAX tensor operators achieves perfect stable/unstable operator classification, at the cost of 127.6-1124.3x runtime overhead. |

### 检索增强生成与分布采样 / RAG, Retrieval & Distributional Sampling

| Paper | Bilingual Takeaway |
|---|---|
| [[2607.25600]] BeyondUncertainty: Confidence-Routed RAG | 用一次性口头置信度作为检索路由信号，平均 F1 优于总是检索/从不检索，检索段落数减少 20.4%，但因探测调用总 token 消耗反增 28.2%。/ Verbalized confidence routes retrieval decisions, beating always/never-retrieve on F1 and cutting retrieved passages by 20.4% — but total token usage rises 28.2% due to the extra probing call. |
| [[2607.25292]] LLMs Cannot Sample What They Describe | 见"今日必读"。/ See "Must Read Today" above — instruction tuning induces per-call sampling collapse despite intact distributional knowledge. |

## All Papers

| Paper | Authors | Bilingual Summary |
|---|---|---|
| [[2607.25163]] Riemannian Active Subspaces | Zachary Grey | 把欧氏"active subspaces"推广到黎曼流形，证明内蕴/外蕴构造在 O(R²) 阶一致并揭示外蕴法的退化失效。/ Generalizes active subspaces to Riemannian manifolds, proving intrinsic vs. extrinsic agreement to O(R²) and exposing a degenerate extrinsic failure mode. |
| [[2607.25199]] RIDGE Option Pricing Validation | Liexin Cheng et al. | 自主验证框架把 LLM 期权定价代码诊断分从 31-58 提到 96-99，并触发新半解析方法发现。/ An autonomous validation loop lifts LLM option-pricing code scores from 31-58 to 96-99 and triggers discovery of a new semi-analytic method. |
| [[2607.25200]] Constant vs Log-Depth Separation | Yunwei Ren et al. | 首个常数深度/对数深度网络算法可学习性分离证明，常数深度网络逼近误差恒 ≥1/4。/ First algorithmic depth separation between constant- and log-depth networks, with a proven ≥1/4 error floor for constant depth. |
| [[2607.25227]] CogBias Bit-Flip Attack | Yu Yan et al. | 翻转 12 个权重比特即可让 LLM 产生稳定认知偏见，ASR 达 84.6%，隐蔽性极强。/ Flipping 12 weight bits hijacks LLM stance with 84.6% attack success while staying nearly undetectable in perplexity. |
| [[2607.25244]] CADENCE Cardiac SAE | Yixuan Duan et al. | 稀疏自编码器把 ECG 基础模型分解为 8,192 个"心脏原子"，跨队列免重训迁移成功。/ A sparse autoencoder decomposes an ECG foundation model into 8,192 interpretable "cardiac atoms" that transfer zero-shot across cohorts. |
| [[2607.25257]] Laplace-PSN-IRT | Juan Francisco Mandujano Reyes | 后验校准显示 66 对模型两两比较中仅 2 对统计显著，多数榜单排名不可信。/ Posterior calibration reveals only 2 of 66 pairwise LLM comparisons are statistically distinguishable. |
| [[2607.25270]] Activation Source Selection | Jiaran Ye et al. | "答案均值"是最弱的 steering 向量来源，tail subtraction 把成功率从 0.288 提到 0.863。/ "Answer-mean" is the weakest steering-vector source; tail subtraction lifts success from 0.288 to 0.863. |
| [[2607.25273]] HEAD-CP Heterophily Conformal Prediction | Phan Binh Nguyen Lam et al. | DAPS 隐含同质性假设致异质图预测集增大 10.6%，逐节点方案在 8/10 数据集显著更优。/ DAPS's homophily assumption inflates prediction sets 10.6% on heterophilic graphs; a per-node fix wins on 8/10 benchmarks. |
| [[2607.25279]] Many-Body Tipping Dynamics | Frank Yingjie Huo et al. | 零拟合参数的"倾覆阈值"公式在 7 个模型上 19/21 命中，但仅测未对齐小模型。/ A zero-free-parameter tipping-threshold formula scores 19/21 across 7 models, but only unaligned small base LMs are tested. |
| [[2607.25292]] LLMs Cannot Sample What They Describe | Chaemin Jang et al. | 指令微调后逐次采样坍缩为单一答案（>94%），但同模型可准确"描述"分布。/ Instruction tuning collapses per-call sampling to one answer (>94%) even though the model can accurately describe the full distribution. |
| [[2607.25299]] Manifold-LoRA (Stiefel) | Yuan Zhang et al. | 免收缩免调参流形优化算法用于 LoRA，SQuADv2.0 F1 从 88.81 提升到 89.22。/ A retraction-free, tuning-free manifold optimizer applied to LoRA lifts SQuADv2.0 F1 from 88.81 to 89.22. |
| [[2607.25312]] Optimizer-Derived Posterior Geometry | Moritz Schlager et al. | 复用 AdamW 动量统计做 SGHMC 预条件子，省去预热，LPPD 提升 7.3-10.1%。/ Reusing AdamW's moment statistics as SGHMC's preconditioner skips warmup and improves LPPD by 7.3-10.1%. |
| [[2607.25376]] Student's t Likelihood for BNNs | Pei-Hsuan Hsia et al. | 固定自由度重尾似然几乎总比高斯似然更准，电力预测 CRPS 降约 16%。/ A fixed-df heavy-tailed likelihood almost always beats Gaussian, cutting electricity-forecast CRPS by ~16%. |
| [[2607.25415]] Frozen LLM Agent Harness Learning | Debjyoti Paul | 小预算下 DSPy 静态 prompt 基线普遍持平或超过在线 RL harness 控制器。/ Under small budgets, a static DSPy prompt baseline matches or beats online RL harness controllers — a negative result. |
| [[2607.25441]] PIcsC Partition-Induced Shift | Behraj Khan et al. | Fisher 信息矩阵统一修正交叉验证分片与联邦异构，CIFAR-100 分片准确率从 38.2% 修复到 58.7%。/ A Fisher-Information regularizer unifies CV-fold shift and federated heterogeneity, recovering CIFAR-100 accuracy from 38.2% to 58.7%. |
| [[2607.25451]] Verbatim Extraction Under Quantization | Akshay Sasi | 4 比特量化在 1B 模型仍保留约 72% 记忆内容，量化非有效隐私防护。/ 4-bit quantization at 1B scale still retains 71.8% of memorized-sequence extraction — not an effective privacy defense. |
| [[2607.25459]] Latent-State Computation in SV Transformers | Xiaoyu Huang et al. | 单层 Transformer 在长周期下的计算可精确还原为线性投影+归一化滤波器。/ A 1-layer Transformer's long-cycle computation reduces exactly to a linear-projection-plus-normalization filter, verified causally. |
| [[2607.25467]] CVMA Causal Visual KV Audit | Hong Chen et al. | 因果干预证明注意力与视觉区域未来效用负相关（Spearman -0.576），现有 KV 淘汰方法失准。/ Causal interventions show attention is negatively correlated with future visual utility (Spearman -0.576), undermining current KV-eviction methods. |
| [[2607.25479]] Architectural Backdoors in VLMs | Maria Rosaria Briglia et al. | 首个无需投毒数据的 VLM 架构后门，攻击成功率最高达 100%。/ First data-free architectural backdoor for VLMs, reaching up to 100% attack success rate. |
| [[2607.25480]] Data-Dependent Regret for Constrained OCO | Wentao Zhang | 对已有算法给出更紧数据依赖 regret 界，合成实验中收紧 38-43%。/ A tighter data-dependent regret bound for an existing algorithm, tightening bounds by 38-43% in synthetic tests. |
| [[2607.25494]] noisyfloat Numerical Stability | Xinye Chen | CESTAC 随机算术嵌入 PyTorch/JAX，稳定性分类 100% 准确但开销达 127-1124 倍。/ CESTAC stochastic arithmetic wired into PyTorch/JAX achieves perfect stability classification at 127-1124x runtime overhead. |
| [[2607.25497]] CRoMa Pathology FM Robustness | Clément Grisi et al. | 现有鲁棒性指标 RI 仅对 9.6%-46.3% 样本打分，新指标发现所有 20 个模型都有混杂主导的最差十分位。/ Existing robustness metric RI scores only 9.6%-46.3% of samples; the new CRoMa metric shows every tested encoder has a confounder-dominated worst decile. |
| [[2607.25507]] RoPE Phase Structure & Governance | Abraham Chachamovits | 纯理论文章证明 RoPE 相位稳定性引理，无实验且作者有商业利益冲突。/ A pure theory paper proving a RoPE phase-stability lemma, with zero experiments and a disclosed commercial conflict of interest. |
| [[2607.25532]] Spurious Intra-Variable Routing | Athanasios Vlontzos et al. | 证明线性 ICL 与 TabPFN 都不可避免路由到虚假信号，S-swap 增强降低 TabPFN 路由比例 98.8%。/ Proves in-context learners unavoidably route to spurious signal when it shares a feature with causal signal; S-swap cuts TabPFN's routing ratio by 98.8%. |
| [[2607.25546]] Post-Hoc Causal Feature ID (NSR) | Athanasios Vlontzos et al. | 免重训归一化敏感度比诊断已训练模型的因果/伪相关依赖，UCI 数据上 Precision@7 达 0.75。/ A retraining-free Normalised Sensitivity Ratio flags causal vs. spurious feature reliance, reaching Precision@7=0.75 on UCI data. |
| [[2607.25554]] Time-Truncation Harness for Forecasting | Wanxu Cai et al. | 动态截断检索环境合成无泄漏时序推理数据，蒸馏模型 Brier Score 降低 19-22%。/ Truncating the retrieval environment synthesizes leak-free forecasting data; distilled models cut Brier Score by 19-22%. |
| [[2607.25583]] LoRA Rank/Quantization on 60M Model | Mahendra Singh Rathor et al. | T5-small 上系统消融发现 LoRA r=16 是帕累托最优点，QLoRA NF4 仅损失约 0.2 点精度。/ A controlled ablation on T5-small finds LoRA r=16 Pareto-optimal; QLoRA NF4 trades only ~0.2pt accuracy for major memory savings. |
| [[2607.25589]] Forensic Audit of Radiology VLM Benchmark | Mateusz Kozłowski | 自我审计发现提示词绑定 bug、DICOM 极性反转等缺陷，撤回所有性能结论。/ A self-audit uncovers a prompt-binding bug and inverted DICOM polarity in the author's own prior benchmark, withdrawing all performance claims. |
| [[2607.25600]] BeyondUncertainty RAG Routing | Chandan Kumar Sah et al. | 口头置信度路由检索，F1 优于总是/从不检索，但因探测调用总 token 增加 28.2%。/ Verbalized-confidence routing beats always/never-retrieve on F1, though total token usage rises 28.2% from the extra probe call. |
| [[2607.25624]] Quotient Dynamics of Quadratic Networks | Pengcheng Cheng | 证明正定二次网络训练精确投影为 PSD 流形黎曼梯度流，但证明样本界比实测宽松十四个数量级。/ Proves quadratic-network training projects exactly onto Riemannian gradient flow on a PSD manifold, though the proven sample bound is ~14 orders of magnitude looser than practice. |
| [[2607.25656]] OrchBench Orchestration Evaluation | Zhenzhen Ren et al. | 模拟器打分与真实执行相关 r=0.816，但去掉一个模型后骤降到 0.421。/ Simulator scores correlate with real execution at r=0.816, but the correlation collapses to 0.421 when one model is removed. |
| [[2607.25663]] Adaptation Geometries in Transformers | Rebecca Ramnauth et al. | 词汇绑定适合早层 LoRA、事实关联适合晚层，迁移差距最高达 42.7 个百分点。/ Lexical binding favors early-layer LoRA, factual association favors late-layer, with transfer gaps up to 42.7pp. |
| [[2607.25665]] Hölder-Bayes Joint Contamination Inference | Masahiro Fujisawa et al. | 联合推断污染比例与模型参数，数据清洗精确率/召回率达 0.973/0.996，远超三种无监督基线。/ Jointly infers contamination proportion and model parameters, reaching 0.973/0.996 precision/recall for cleaning, well above unsupervised baselines. |
| [[2607.25672]] AI Literature Review Capability (I) | Anamaria Hell et al. | 人类与 LLM 文献选择重合率不到 6%，3% 参考文献彻底虚构，64% 元数据有误。/ Human vs. LLM literature picks overlap under 6%; 3% of AI references are fabricated and 64% have metadata errors. |
| [[2607.25675]] DecoEvo Rubric Co-Evolution | Jiangwang Chen et al. | 评分标准生成器只靠与聚合分数无关的审计更新，五基准全面超过 SkillOpt 2.8-5.0%。/ Decoupling rubric updates from the solver's proxy score beats SkillOpt on all benchmarks by 2.8-5.0% relative. |
| [[2607.25680]] Rashomon Alignment | Moisés Santos et al. | 几何一致性指标显示准确率相同的模型可能只在 45% 实例空间上意见一致。/ A geometric agreement metric shows equally-accurate models can agree on only 45% of the instance space. |
| [[2607.25748]] Loss Invariance in Echocardiography CBM | Hyunkyung Han et al. | 仅用射血分数训练的容积概念层因比值不变性坍缩到近零方差，加毫升级监督后误差大降。/ A volume concept-bottleneck trained only on ejection fraction collapses to near-zero variance due to ratio invariance; direct volume supervision fixes it. |
| [[2607.25785]] MC-ALFCG Markovian Conditional Gradient | Zhaojun Peng | 把 Frank-Wolfe 方差缩减扩展到马尔可夫链采样，但承认投影 SGD 绝对指标仍更优。/ Extends variance-reduced Frank-Wolfe to Markovian sampling with proven bounds, while honestly noting projected SGD still wins on absolute metrics. |
| [[2607.25814]] Adversarial Robustness in Arabic LMs | Anwar Alajmi et al. | 变音符号插入让 AraBERT 准确率从 94% 暴跌到 2%，释义攻击平均降 76%。/ Diacritics insertion crashes AraBERT from 94% to 2% accuracy; paraphrase attacks degrade all models by 76% on average. |
| [[2607.25865]] OmniQEC AI Scientist for QEC | Ge Yan et al. | LLM 智能体以电路级错误率为目标发现的量子纠错码超过人工设计基准。/ An LLM agent optimizing circuit-level error rate discovers qLDPC codes that beat human-designed benchmarks. |
| [[2607.25873]] How Do LLMs Read Bug Reports? | Ramtin Ehsani et al. | 修复成功对应跨组件的"扩散型注意力"，失败修复集中于低价值元数据。/ Successful bug repairs correspond to attention diffused across bug-report components; failures concentrate on low-value metadata. |
| [[2607.25877]] Bayesian Network Runtime Monitoring for MAS | Bart Custers et al. | 校准置信度接入贝叶斯网络传播不确定性，最佳后端错误检测率达 90%。/ Calibrated confidence feeds a Bayesian Network for uncertainty propagation; the best backend reaches 90% error-detection rate. |
| [[2607.25881]] AI Proposal Writing & Review Bias (II) | Jia Liu et al. | AI 评审系统性给 AI 撰写提案多打约 1 分，人类评审组无此偏向。/ AI reviewer models systematically rate AI-written proposals ~1 point higher; human reviewers show no such bias. |
| [[2607.25886]] RSIBench-Data | Fanqing Meng et al. | 智能体在 58% 设置中超越首次尝试，但持续搜索在 78% 情形下反而退步。/ Agents beat their own first attempt in 58% of settings, yet continued search regresses in 78% of cases where it keeps going. |
| [[2607.25904]] Interactive Reward Agent (IRA) | Chenrui Shi et al. | 提出条件-工具核验框架在新基准上达 86.9% 准确率，超最强被动基线 8.1 个百分点。/ A propose-then-verify framework reaches 86.9% accuracy, 8.1pp above the strongest passive VLM baseline. |
| [[2607.25907]] Suppressing Evaluation-Awareness Latents | Deepanshu Mody et al. | 提示优化可把评估感知特征压到零，但行为学检验显示这不等于改变实际判断。/ Prompt optimization zeros an evaluation-awareness feature, but behavioral tests show this does not change the model's actual judgment. |
| [[2607.25929]] DGMs vs Non-Stationary Gaussian Fields | Daniel Kua et al. | VAE 协方差恢复误差是 oracle 的约 66 倍，常用 CRPS 指标无法揭示这一差距。/ VAE's covariance-recovery error is ~66x the oracle floor, a gap the widely used CRPS metric fails to detect. |
| [[2607.25988]] GARI Soft Equivariance Interface | Weitao Li et al. | 生成元索引流接口替代硬编码等变算子，ImageNet-1K 旋转泛化准确率提升 1.34 个百分点。/ A generator-indexed stream interface replaces hard-coded equivariant operators, improving ImageNet-1K rotation generalization by 1.34pp. |
| [[2607.26000]] OOD Tabular Foundation Models | Malena Loza et al. | 真实数据预训练表格基础模型绝对性能最高但分布偏移退化差距也最大。/ Real-data-pretrained tabular foundation models have the best absolute OOD accuracy but also the largest distribution-shift degradation gap. |
| [[2607.26001]] SpecSAM: SAM Meets Muon | Wenzhi Zhong et al. | 谱范数逐层扰动搭配 Muon 外层更新，ImageNet-1K ViT-S 上 Top-1 达 80.23%，+5.28 点。/ A spectral-norm layerwise perturbation paired with Muon's outer update reaches 80.23% Top-1 on ViT-Small/ImageNet-1K, +5.28pt over unperturbed Muon. |
