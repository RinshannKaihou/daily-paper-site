---
title: "Daily Paper Overview — 2026-05-18"
date: 2026-05-18
tags:
  - daily-paper
  - arxiv
papers: 50
---

## 今日必读 / Must Read Today

### 1. [[2605.18163]] — TRACE: Trajectory Correction from Cross-layer Evidence for Hallucination Reduction

> **推荐理由：** 无需训练、无需检索、单一冻结超参数设置，在15个模型、3个事实性基准的45个评估单元上实现零回归、平均+12.26 MC1提升，是当前最实用的LLM幻觉纠正方案。
> **Reason:** A training-free, deterministic inference-time algorithm achieving zero regressions across 15 models from 8 families on 3 factuality benchmarks with a single frozen hyperparameter setting — the most practical hallucination correction method to date.

### 2. [[2605.18106]] — Symmetry-Compatible Principle for Optimizer Design

> **推荐理由：** 提出对称性兼容的优化器设计原则，将梯度更新与权重块的对称群保持等变，统一了Muon/Scion/PolarGrad等方法的几何解释，在四种架构的预训练中一致优于AdamW。
> **Reason:** Establishes that optimizer updates should be equivariant under each weight block's symmetry group, unifying Muon/Scion/PolarGrad and consistently outperforming AdamW across four dense and MoE architectures.

### 3. [[2605.18229]] — Are Sparse Autoencoder Benchmarks Reliable?

> **推荐理由：** 系统性审计了SAEBench全部六个评估指标，发现TPP和SCR在标准设置下多项合理性检验均失败，揭示了当前机制可解释性领域基准测试的严重可靠性危机。
> **Reason:** A systematic three-dimensional audit of all six SAEBench metrics reveals that TPP and SCR fail multiple sanity checks, exposing a severe reliability crisis in current SAE evaluation.

---

## 按主题分类 / Papers by Topic

### 优化与训练动力学 / Optimization & Training Dynamics

| Paper | 中文摘要 | English Summary |
|-------|---------|-----------------|
| [[2605.17787]] Revisiting the Adam-SGD Gap | 揭示SGD表现远逊于Adam的核心原因是无法维持足够大的有效学习率，简单梯度裁剪即可将差距缩小至3.5% | SGD's inability to sustain large effective learning rates explains the Adam-SGD gap; targeted clipping closes it to 3.5% |
| [[2605.17806]] AMO: Adaptive Muon Orthogonalization | 自适应为不同算子类型的Newton-Schulz迭代分配步数预算，在0.6B-1.7B模型上一致优于均匀Muon | Observe-then-commit method allocating per-operator-type NS iteration budgets, consistently outperforming uniform Muon |
| [[2605.17770]] Entropy-Gradient Inversion / CorR-PO | 发现推理模型的熵-梯度反转现象并据此设计RL奖励正则化，稳定超越GRPO/DAPO | Identifies entropy-gradient inversion as reasoning fingerprint, proposes CorR-PO that consistently beats GRPO/DAPO |
| [[2605.18106]] Symmetry-Compatible Optimizer Design | 对称性兼容优化器设计原则，统一Muon/Scion/PolarGrad几何解释，一致优于AdamW | Equivariant optimizer design principle unifying Muon/Scion/PolarGrad, consistently outperforming AdamW |
| [[2605.18174]] Ringmaster LMO | 首个异步LMO动量优化方法，支持Muon等结构化优化器的异构分布式训练 | First asynchronous LMO momentum method enabling heterogeneous distributed training for Muon-class optimizers |
| [[2605.18609]] Perfect Parallelization in Mini-Batch SGD | 证明mini-batch SGD+动量迭代复杂度O((κ/m+√κ)log(κ/ε))，与m成正比至饱和，实现完美并行化 | Proves mini-batch SGD+momentum complexity O((κ/m+√κ)log(κ/ε)), linear in m to saturation — perfect parallelization |
| [[2605.18694]] AdaGrad under Heavy-Tailed Noise | 首次证明AdaGrad在重尾噪声下的非凸优化收敛速率 | First provable convergence rate for AdaGrad under heavy-tailed gradient noise in non-convex optimization |

### 量化与模型压缩 / Quantization & Model Compression

| Paper | 中文摘要 | English Summary |
|-------|---------|-----------------|
| [[2605.17745]] StatQAT | 基于统计误差分析的量化器优化框架，在FP4/INT4 QAT中匹配LLM-QAT和ParetoQ | Statistical error analysis framework for quantizers, matching LLM-QAT/ParetoQ at FP4/INT4 |
| [[2605.17757]] OSCAR | 离线谱协方差旋转实现2-bit KV Cache量化，Qwen3-8B与BF16仅差1.42点，GLM-4.7-FP8反超+0.27 | Offline spectral covariance rotations for 2-bit KV cache; Qwen3-8B within 1.42 of BF16, GLM-4.7-FP8 +0.27 |
| [[2605.17997]] MARR | 模块自适应残差缩放配合PID控制器，W2A4量化下最高20.2%困惑度降低 | Module-adaptive residual scaling with PID controller, up to 20.2% perplexity gain at W2A4 |
| [[2605.18331]] Putri | 支持GQA的结构化剪枝，首个在95%稀疏度下仍产生可用模型的方法 | GQA-aware structured pruning, first method producing usable models at 95% sparsity |
| [[2605.18475]] GAMMA | 量化器无关的混合精度框架，单次训练服务任意部署目标，2.5-bit匹配3-bit质量 | Quantizer-agnostic mixed-precision framework, single training serving arbitrary budgets at 2.5-bit |
| [[2605.17887]] OASIS | 揭示AttnResidual双归一化的结构性缺陷，Softmax1空空间机制降低73.55% W8A8困惑度 | Reveals AttnResidual dual normalization flaw, Softmax1 null channels reduce W8A8 perplexity 73.55% |

### 机制可解释性 / Mechanistic Interpretability

| Paper | 中文摘要 | English Summary |
|-------|---------|-----------------|
| [[2605.17704]] Lottery Tickets in Feature Space | 中奖彩票是特征空间中的前驱脚手架而非权重稀疏子网络，特征空间探针优于权重剪枝 | Winning tickets are feature-space precursor scaffolds; feature-space probes outperform weight-based methods |
| [[2605.18229]] Are SAE Benchmarks Reliable? | TPP和SCR多项合理性检验失败，sae-probes为最可靠但仍不够 | TPP and SCR fail sanity checks; sae-probes most reliable but still insufficient |
| [[2605.18629]] Aligned Training for SAE | 无参数SAE重参数化，消除死亡特征并提升跨种子稳定性 | Parameter-free SAE reparameterization eliminating dead features and improving cross-seed stability |
| [[2605.18537]] Manifold Probe | 发现LLM表示空间中连续概念的多维流形，可用于因果干预 | Discovers multidimensional representation manifolds for continuous concepts, enables causal steering |
| [[2605.18646]] Language-Switching Backdoor Circuits | 触发信号在中间层以正交子空间传播，语言探针无法检测 | Trigger signal propagates in orthogonal subspace at mid-layers, invisible to language identity probes |
| [[2605.18549]] Probe Trajectories | 逐token探针轨迹揭示推理动态，AUROC最高97% | Token-by-token probe trajectories reveal reasoning dynamics, up to 97% AUROC |

### 大模型安全与对齐 / LLM Safety & Alignment

| Paper | 中文摘要 | English Summary |
|-------|---------|-----------------|
| [[2605.17971]] Babel Jailbreak | 安全注意力头稀疏性驱动的混淆采样越狱，GPT-4o ASR 82.67%（Bon 41.33%），R²=0.998可预测 | Obfuscation-distribution sampling jailbreak; GPT-4o ASR 82.67% vs Bon 41.33%, R²=0.998 predictability |
| [[2605.18104]] Safety Geometry Collapse / ReGap | 揭示多模态LLM中模态漂移压缩安全拒绝方向，ReGap降低30-70个百分点攻击成功率 | Modality drift compresses safety refusal direction; ReGap reduces ASR by 30-70 points |
| [[2605.18163]] TRACE | 无训练幻觉纠正，15个模型零回归，平均+12.26 MC1提升 | Training-free hallucination correction, zero regressions across 15 models, +12.26 MC1 average |
| [[2605.18309]] Alignment Dynamics | 对齐分数闭式更新，分解为反弹力与驱动力，预测排练启动效应 | Closed-form alignment score update decomposed into rebound/driving forces, predicts rehearsal priming |
| [[2605.18672]] Three-Layer A/G Safety | 论证单层护栏无法覆盖三维度安全，提出概率假设-保证三层架构 | Argues single-layer guardrails cannot cover 3 safety dimensions; proposes 3-layer probabilistic A/G |

### 分布式系统与训练基础设施 / Distributed Systems & Training Infrastructure

| Paper | 中文摘要 | English Summary |
|-------|---------|-----------------|
| [[2605.17821]] TierCheck | 三层分级检查点系统，降低62.8-82.7%训练开销，8.8秒软件故障恢复 | 3-tier checkpointing reducing overhead 62.8-82.7%, 8.8s software fault recovery |
| [[2605.17879]] Guard | 生产级灰节点检测系统，MFU从10%提升至17%，步长从17秒降至10秒 | Production grey-node detection: MFU 10%→17%, step time 17s→10s |
| [[2605.18750]] RRFP | 就绪状态驱动的流水线并行运行时，多模态任务最高2.77倍加速 | Readiness-driven pipeline parallelism runtime, up to 2.77x speedup on multimodal tasks |
| [[2605.18071]] KVDrive | HBM/DRAM/SSD三层KV缓存管理，360k上下文1.74倍吞吐，RULER 72.56匹配Full | HBM/DRAM/SSD 3-tier KV cache; 1.74x throughput at 360k ctx, RULER 72.56 matches Full |
| [[2605.18053]] KV Cache Structural Protection | 结构性保护是首要因素，10%边界保留即恢复69-90%质量 | Structural protection dominates scoring; 10% boundary reservation recovers 69-90% quality |

### 神经网络理论 / Neural Network Theory

| Paper | 中文摘要 | English Summary |
|-------|---------|-----------------|
| [[2605.17718]] Feature Learning Reshapes Function Space | 证明一次大步长GD将特征分布变为目标相关spiked Gaussian，诱导数据自适应核 | Proves single large GD step induces target-dependent spiked Gaussian, yielding data-adaptive kernel |
| [[2605.18180]] Canonical Regularisation | Ridge正则在特征学习宽网络中λ↓0时偏置持续，提出geodesic/arc ridge与Riemannian Gibbs过程 | Ridge bias persists as λ→0 in feature-learning wide nets; proposes geodesic/arc ridge and Riemannian Gibbs Process |
| [[2605.18022]] Memorization-Generalization Coexistence | 80%标签噪声下模型仍学正确规则，频域滤波可恢复近100%测试准确率 | Model learns correct rules under 80% label noise; frequency filtering recovers near-100% accuracy |
| [[2605.18598]] Pointwise Generalization | 逐点黎曼维度比VC维小10³倍、比谱范数界小10⁶倍，且随过参数化递减 | Pointwise Riemann Dimension 10³x tighter than VC, 10⁶x tighter than spectral bounds |
| [[2605.18315]] Attention-based PCA | 证明softmax attention梯度流收敛到协方差主特征向量，attention本质执行PCA | Proves softmax attention gradient flow converges to principal eigenvector — attention is PCA |
| [[2605.18281]] Temporal Task Diversity | 非平稳任务分布降低Transformer从记忆到泛化的多样性阈值 | Non-stationary task distributions lower the diversity threshold for memorization-to-generalization transition |

### 大模型推理与微调 / LLM Reasoning & Fine-Tuning

| Paper | 中文摘要 | English Summary |
|-------|---------|-----------------|
| [[2605.17967]] SFT Interaction Perspective | SFT本质是前1000步的短暂去噪阶段，之后引入过拟合高阶交互 | SFT's benefit is a brief ~1000-step denoising phase; continued training adds overfitted interactions |
| [[2605.17862]] f-OPD | 量化异步on-policy蒸馏的样本新鲜度，1.46倍吞吐量恢复94%同步性能 | Quantifies sample freshness in async OPD; 1.46x throughput at 94% synchronous quality |
| [[2605.18079]] Low Precision Softmax Transformers + CoT | 证明低精度Transformer解码器可通过CoT模拟图灵机，模型规模按空间界对数缩放 | Proves low-precision softmax transformers simulate TMs via CoT; model size scales logarithmically in space |
| [[2605.18607]] Proxy Metrics for LLM Forecasting | 专家轨迹上的80个代理指标在跨家族模型选择中达Spearman ρ=0.81 | 80 proxy metrics from expert trajectories achieve ρ=0.81 in cross-family model ranking |

### 不确定性与校准 / Uncertainty Quantification & Calibration

| Paper | 中文摘要 | English Summary |
|-------|---------|-----------------|
| [[2605.18202]] COCOCO | 对概念和标签同时保形预测+逻辑修正，8个基准上实现一致性、覆盖率和简洁性 | Joint concept-label conformal prediction with logical revision, satisfying all 3 desiderata on 8 benchmarks |
| [[2605.18329]] Lost in the Folds | K折交叉验证集成与深度集成不可互换，DE在校准上更优，CV在标注歧义上更好 | CV ensembles and deep ensembles are not interchangeable; DE better for calibration, CV for rater ambiguity |
| [[2605.18008]] UQ for PPG Blood Pressure | 深度集成在域偏移下最鲁棒，GNLL损失提供最佳原生不确定性 | Deep ensembles most robust under domain shift; GNLL loss provides best native uncertainty |
| [[2605.18224]] Simplex Witness for VAE Collapse | 正单纯形见证证书可训练前设计、训练中监控、训练后认证常数坍塌 | Simplex witness certificate enables pre-training design, mid-training monitoring, post-training certification |

### 生成模型与视频 / Generative Models & Video

| Paper | 中文摘要 | English Summary |
|-------|---------|-----------------|
| [[2605.18739]] LongLive-2.0 | 首个端到端NVFP4长视频生成系统，5B模型45.7 FPS实时生成，训练加速2.15倍 | First end-to-end NVFP4 long video generation system; 45.7 FPS on 5B model, 2.15x training speedup |

### 应用机器学习与系统 / Applied ML & Systems

| Paper | 中文摘要 | English Summary |
|-------|---------|-----------------|
| [[2605.18327]] Causely | 因果智能层为SRE AI Agent提供预计算因果知识，诊断时间降低63% | Causal intelligence layer for SRE agents; 63% time-to-diagnosis reduction, 100% root-cause accuracy |
| [[2605.18522]] Color Features in Cancer | 仅颜色统计特征在组织病理学二分类中达89%准确率，可作为轻量预筛查 | Color features alone achieve 89% accuracy in histopathology binary classification |
| [[2605.18361]] iHAC | 混合集群架构融合active-active/passive，HTTP响应时间降低40% | Hybrid cluster merging active-active/passive modes, 40% HTTP response reduction |
| [[2605.18444]] Reliable Multipliers under NBTI | 利用乘法符号不变性的硬件老化缓解，128×128脉动阵列寿命提升75% | Hardware NBTI aging mitigation via sign-invariance, 75% lifetime improvement in 128×128 systolic arrays |
| [[2605.18612]] XRM-SSD V24 | 物理感知软件调度实现先发式热补偿，波长漂移仅占TSMC容差21% | Physics-aware software scheduling for pre-emptive thermal compensation, 21% of TSMC tolerance |
| [[2605.18068]] Teger | 曲率感知重连缓解图过度压缩，42/48基准CRPSsum最优，Brussels超LASER 25.3% | Curvature-aware rewiring mitigates over-squashing; 42/48 best CRPSsum, Brussels +25.3% over LASER |

---

## All Papers

| # | ID | Title | 中文一句话总结 | English TL;DR |
|---|-----|-------|-------------|--------------|
| 1 | [[2605.17704]] | Lottery Tickets in Feature Space | 特征空间前驱脚手架是中奖彩票的本质 | Winning tickets are feature-space precursor scaffolds |
| 2 | [[2605.17718]] | Feature Learning Reshapes Function Space | 一次大步GD诱导目标相关数据自适应核 | Single large GD step induces target-dependent data-adaptive kernel |
| 3 | [[2605.17745]] | StatQAT | 统计误差分析框架优化量化器 | Statistical error analysis for quantizer optimization |
| 4 | [[2605.17757]] | OSCAR | 谱协方差旋转2-bit KV量化，Qwen3-8B差BF16 1.42 | Spectral covariance 2-bit KV quant, Qwen3-8B within 1.42 of BF16 |
| 5 | [[2605.17770]] | Entropy-Gradient Inversion / CorR-PO | 熵-梯度反演作为RL奖励正则化 | Entropy-gradient inversion as RL reward regularizer |
| 6 | [[2605.17787]] | Revisiting the Adam-SGD Gap | 梯度裁剪使SGD匹配Adam | Gradient clipping enables SGD to match Adam |
| 7 | [[2605.17806]] | AMO | 自适应Muon正交化迭代预算 | Adaptive Muon orthogonalization iteration budgets |
| 8 | [[2605.17821]] | TierCheck | 三层分级检查点降低82%开销 | 3-tier checkpointing reduces 82% overhead |
| 9 | [[2605.17862]] | f-OPD | 新鲜度感知异步on-policy蒸馏 | Freshness-aware asynchronous on-policy distillation |
| 10 | [[2605.17879]] | Guard | 生产级灰节点检测，MFU提升1.7倍 | Production grey-node detection, 1.7x MFU |
| 11 | [[2605.17887]] | OASIS | Softmax1空空间解决注意力汇聚异常 | Softmax1 null channels fix attention sink outliers |
| 12 | [[2605.17967]] | SFT Interaction Perspective | SFT本质是1000步去噪阶段 | SFT is a brief ~1000-step denoising phase |
| 13 | [[2605.17971]] | Babel Jailbreak | 混淆采样越狱GPT-4o ASR 82.67% | Obfuscation-sampling jailbreak, GPT-4o ASR 82.67% |
| 14 | [[2605.17997]] | MARR | PID控制的模块自适应残差量化 | PID-controlled module-adaptive residual quantization |
| 15 | [[2605.18008]] | UQ for PPG Blood Pressure | 深度集成在域偏移下最鲁棒 | Deep ensembles most robust under domain shift |
| 16 | [[2605.18022]] | Memorization-Generalization Coexistence | 80%噪声下泛化与记忆共存 | Generalization and memorization coexist under 80% noise |
| 17 | [[2605.18053]] | KV Cache Structural Protection | 结构性保护远比评分策略重要 | Structural protection dominates scoring strategies |
| 18 | [[2605.18068]] | Teger | 曲率重连42/48基准CRPSsum最优 | Curvature rewiring, 42/48 best CRPSsum |
| 19 | [[2605.18071]] | KVDrive | HBM/DRAM/SSD三层KV，360k上下文1.74x吞吐 | HBM/DRAM/SSD 3-tier KV, 1.74x throughput at 360k ctx |
| 20 | [[2605.18079]] | Low Precision Transformers + CoT | 低精度Transformer通过CoT模拟图灵机 | Low-precision transformers simulate TMs via CoT |
| 21 | [[2605.18104]] | Safety Geometry Collapse / ReGap | 多模态安全几何坍塌的自适应修正 | Adaptive correction of multimodal safety geometry collapse |
| 22 | [[2605.18106]] | Symmetry-Compatible Optimizer | 等变优化器一致优于AdamW | Equivariant optimizers consistently outperform AdamW |
| 23 | [[2605.18163]] | TRACE | 无训练幻觉纠正，15模型零回归 | Training-free hallucination correction, 0 regressions |
| 24 | [[2605.18174]] | Ringmaster LMO | 异步LMO动量支持Muon分布式训练 | Async LMO momentum for distributed Muon training |
| 25 | [[2605.18180]] | Canonical Regularisation | Ridge偏置λ→0持续，提出geodesic ridge | Ridge bias persists as λ→0, proposes geodesic ridge |
| 26 | [[2605.18202]] | COCOCO | 逻辑一致保形预测满足三大需求 | Logically consistent conformal prediction satisfying 3 desiderata |
| 27 | [[2605.18224]] | Simplex Witness for VAE | 常数坍塌的训练全周期证书 | Full-lifecycle certificate for constant collapse in VAEs |
| 28 | [[2605.18229]] | Are SAE Benchmarks Reliable? | SAE基准测试可靠性危机 | SAE benchmark reliability crisis |
| 29 | [[2605.18281]] | Temporal Task Diversity | 非平稳性降低记忆-泛化阈值 | Non-stationarity lowers memorization-to-generalization threshold |
| 30 | [[2605.18309]] | Alignment Dynamics | 对齐分数闭式更新与排练启动效应 | Closed-form alignment score and rehearsal priming effect |
| 31 | [[2605.18315]] | Attention-based PCA | Attention梯度流收敛到PCA主成分 | Attention gradient flow converges to PCA |
| 32 | [[2605.18327]] | Causely | 因果智能层提升SRE根因诊断至100% | Causal intelligence layer achieving 100% root-cause accuracy |
| 33 | [[2605.18329]] | Lost in the Folds | CV集成与深度集成不可互换 | CV ensembles and deep ensembles not interchangeable |
| 34 | [[2605.18331]] | Putri | 首个95%稀疏度下可用的LLM剪枝 | First usable LLM pruning at 95% sparsity |
| 35 | [[2605.18361]] | iHAC | 混合集群架构降低40%响应时间 | Hybrid cluster reducing 40% response time |
| 36 | [[2605.18444]] | Reliable Multipliers under NBTI | 符号不变性老化缓解提升75%寿命 | Sign-invariance aging mitigation, 75% lifetime boost |
| 37 | [[2605.18475]] | GAMMA | 量化器无关混合精度，2.5-bit匹配3-bit | Quantizer-agnostic mixed precision, 2.5-bit matches 3-bit |
| 38 | [[2605.18522]] | Color Features in Cancer | 仅颜色特征达89%癌症分类准确率 | Color features alone achieve 89% cancer classification |
| 39 | [[2605.18537]] | Manifold Probe | 发现LLM中连续概念的多维流形 | Discovers multidimensional concept manifolds in LLMs |
| 40 | [[2605.18549]] | Probe Trajectories | 逐token探针轨迹AUROC达97% | Token-by-token probe trajectories reach 97% AUROC |
| 41 | [[2605.18598]] | Pointwise Generalization | 逐点黎曼维度比VC维紧10³倍 | Pointwise Riemann Dimension 10³x tighter than VC |
| 42 | [[2605.18607]] | Proxy Metrics for LLM Forecasting | 80个代理指标跨家族模型排序ρ=0.81 | 80 proxy metrics achieve ρ=0.81 cross-family ranking |
| 43 | [[2605.18609]] | Perfect Parallelization in SGD | O((κ/m+√κ)log(κ/ε))实现完美并行化 | O((κ/m+√κ)log(κ/ε)) enables perfect parallelization |
| 44 | [[2605.18612]] | XRM-SSD V24 | 软件调度先发式热补偿，漂移仅21%容差 | Software pre-emptive thermal compensation at 21% tolerance |
| 45 | [[2605.18629]] | Aligned Training for SAE | 无参数SAE对齐训练消除死亡特征 | Parameter-free SAE alignment training eliminating dead features |
| 46 | [[2605.18646]] | Language-Switching Backdoor | 触发信号在正交子空间中隐蔽传播 | Trigger signal propagates covertly in orthogonal subspace |
| 47 | [[2605.18672]] | Three-Layer A/G Safety | 三层概率架构保障LLM Agent安全 | 3-layer probabilistic architecture for safe LLM agents |
| 48 | [[2605.18694]] | AdaGrad under Heavy-Tailed Noise | 首次证明AdaGrad在重尾噪声下收敛 | First convergence proof for AdaGrad under heavy-tailed noise |
| 49 | [[2605.18739]] | LongLive-2.0 | NVFP4端到端长视频生成，45.7 FPS | End-to-end NVFP4 long video generation at 45.7 FPS |
| 50 | [[2605.18750]] | RRFP | 就绪驱动流水线并行最高2.77倍加速 | Readiness-driven pipeline parallelism, up to 2.77x speedup |
