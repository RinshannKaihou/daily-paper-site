---
title: "Daily Paper Overview — 2026-05-07"
date: 2026-05-07
tags:
  - daily-overview
  - LLM
  - quantization
  - interpretability
  - training-stability
  - inference-efficiency
  - evaluation
  - mechanistic-interpretability
  - activation-steering
papers_count: 50
---

# 每日论文概览 / Daily Paper Overview — 2026-05-07

---

## 今日必读 / Must Read Today

### 1. [[2605.05686v1]] — Attractor Geometry of Transformer Memory

**相关性 / Relevance:** 直接命中"可解释性/隐藏状态"核心兴趣。该论文将Transformer参数记忆建模为隐空间的几何吸引子盆地，通过盆地间距（margin）完美区分幻觉与正确回忆，且在零误判率下优于输出熵——对理解隐藏状态如何编码"确定性"与"知识缺失"有极强的理论意义。

**Relevance (EN):** A direct hit on the interpretability/hidden-states interest. This paper models parametric memory as geometric attractor basins in latent space and shows that hidden-state distance to the nearest basin perfectly separates hallucination from correct recall at zero false-positive rate — outperforming output entropy and scaling better with model size. Foundational for understanding what hidden states actually encode about knowledge reliability.

---

### 2. [[2605.05794v1]] — MoLS: Calibrating Adam via Module-wise SNR

**相关性 / Relevance:** 直接命中"LLM训练稳定性"核心兴趣。该论文揭示Transformer各模块间梯度信噪比（SNR）存在系统性失衡，并提出MoLS在预热阶段一次性估计SNR后自动按比例缩放各模块学习率，无需手动调参，在LLaMA 60M–7B预训练中最大降低1.82 PPL，适用范围广且实现成本低。

**Relevance (EN):** Directly addresses LLM training stability. MoLS reveals that Transformer modules (Embedding, QK, VO, MLP, Head) have wildly mismatched gradient SNRs throughout training, and automatically calibrates module-level learning rates using a single pre-warmup SNR estimate. Consistently beats hand-tuned baselines on LLaMA pretraining up to 7B scale — immediately applicable with minimal overhead.

---

### 3. [[2605.05561v1]] — BitCal-TTS: Bit-Calibrated Test-Time Scaling for Quantized Reasoning Models

**相关性 / Relevance:** 同时命中"量化/精度误差"和"推理评估"两个核心兴趣。4-bit量化后的模型置信度信号发生系统性错位，导致自适应早停决策失效。BitCal-TTS无需微调，通过比特感知置信度校正修复了量化引入的推理时偏差，在4-bit Qwen2.5上比精度无关基线提高~+3.7pp准确率，同时节省32–41% token。

**Relevance (EN):** Hits both quantization/precision-errors and inference-evaluation interests simultaneously. The paper identifies and fixes a systematic miscalibration in confidence signals (token entropy, trace stability) introduced by 4-bit PTQ, causing premature adaptive stopping. BitCal-TTS is a lightweight, fine-tuning-free controller that recalibrates quantization-induced inference-time biases — crucial for deploying quantized reasoning models reliably.

---

## 按主题分类 / Papers by Topic

### LLM训练稳定性 / LLM Training Stability & Optimization

| 论文 / Paper | 主题 / Topic | 一句话 / Summary |
|---|---|---|
| [[2605.05794v1]] MoLS | 模块级学习率校准 / Module-wise LR calibration | 基于梯度SNR失衡自动调整Adam学习率 / Auto-scales Adam LR from gradient SNR imbalance |
| [[2605.05577v1]] LMO-IGT | LMO优化器加速 / LMO optimizer acceleration | 隐式梯度传输将Lion/Muon复杂度从O(ε⁻⁴)降至O(ε⁻³·⁵) / IGT improves LMO complexity by half-order |
| [[2605.06316v1]] Pro-KLShampoo | 二阶预条件器 / Second-order preconditioner | 利用Kronecker谱"尖峰-平坦"结构的低秩全谱预条件器 / Low-rank full-spectrum preconditioner for Kronecker structure |
| [[2605.06615v1]] SignSGD theory | 符号SGD理论 / Sign-SGD theory | 首次严格证明SignSGD在稀疏噪声时比SGD少d倍复杂度 / First tight proof: SignSGD beats SGD by factor d under sparse noise |
| [[2605.06654v1]] Optimizer-Model Consistency | 微调遗忘 / Fine-tuning forgetting | 预训练与微调使用相同优化器族可显著减少灾难性遗忘 / Matching optimizer family between pretraining and SFT reduces forgetting |
| [[2605.06523v1]] RLVR Low-rank | RLVR低秩动态 / RLVR low-rank dynamics | Rank-1替换实验揭示RLVR推理增益完全来自Rank-1方向 / Rank-1 substitution shows reasoning gains lie entirely in rank-1 direction |
| [[2605.05724v1]] Auto Research | 自动ML研究 / Automated ML research | 多智能体闭环优化训练配方，1197次实验无需人工干预 / Multi-agent closed-loop training recipe optimization, 1197 experiments |

### 可解释性/隐藏状态 / Interpretability & Hidden States

| 论文 / Paper | 主题 / Topic | 一句话 / Summary |
|---|---|---|
| [[2605.05686v1]] Attractor Geometry | 吸引子几何 / Attractor geometry | 隐状态到最近盆地距离可零误判率区分幻觉与正确回忆 / Hidden-state basin margin perfectly separates hallucination at zero FPR |
| [[2605.05593v1]] Causal Probing MLLMs | 多模态因果探测 / Multimodal causal probing | 激活操控揭示四类视觉概念截然不同的编码机制 / Activation steering reveals distinct encoding of visual concept types |
| [[2605.05668v1]] LVLMs Get Lost | LVLM注意力分析 / LVLM attention analysis | 信息论框架揭示大多数LVLM视觉注意力权重可用噪声替换 / IT framework reveals most visual attention weights are noise-replaceable |
| [[2605.05715v1]] Classification-Correction Gap | 线性可解码性 / Linear decodability | 失败模式线性可解码但无法被线性引导纠正——揭示方向纠缠 / Failure is linearly decodable but uncorrectable — reveals directional entanglement |
| [[2605.05741v1]] HyperLens | 置信度轨迹 / Confidence trajectory | 自放大探针量化LLM认知努力，SFT引发盲目自信 / Self-amplifying probe quantifies cognitive effort; SFT induces overconfidence |
| [[2605.06196v1]] Granularity Axis | 角色粒度轴 / Role granularity axis | 发现编码社会角色微观-宏观尺度的单一线性方向 / Single linear direction encodes micro-to-macro social role scale |
| [[2605.05980v1]] TACT | 激活引导编码智能体 / Activation steering for agents | 对比引导轴修正coding agent的过度思考/过度行动失效 / Contrastive steering corrects overthinking/overacting in coding agents |
| [[2605.06295v1]] METAGAME | 元归因 / Meta-attributions | 将Shapley值应用于Shapley值，捕获token二阶交互效应 / Shapley of Shapley captures second-order token interaction effects |
| [[2605.06480v1]] Patch-Effect Graph Kernels | 激活修补图核 / Activation patching graph kernels | 将激活修补实验编码为图并用图核进行机制分类 / Encodes patching experiments as graphs; graph kernels classify circuits |
| [[2605.06494v1]] WL SAE Features | SAE特征图分析 / SAE feature graph analysis | WL图核聚类SAE特征，发现decoder相似度无法区分的字母族 / WL graph kernels find alphabet feature families invisible to decoder similarity |
| [[2605.06611v1]] Attention Sink Origin | 注意力汇聚机制 / Attention sink mechanism | 因果掩码→方差差异→超级神经元→维度不均衡→注意力汇聚的完整因果链 / Full causal chain: causal mask → variance discrepancy → super neurons → attention sink |
| [[2605.06352v1]] Topological Grokking | Grokking拓扑签名 / Grokking topology | 持久同调揭示grokking时表示空间出现循环拓扑结构 / Persistent homology finds cyclic topology emerges at generalization transition |

### 量化/精度误差 / Quantization & Precision

| 论文 / Paper | 主题 / Topic | 一句话 / Summary |
|---|---|---|
| [[2605.05561v1]] BitCal-TTS | 量化推理时校准 / Quantized inference calibration | 修复4-bit量化后置信度信号失真导致的自适应停止问题 / Fixes confidence miscalibration causing premature stopping under 4-bit PTQ |
| [[2605.05693v1]] SARQC | 显著性感知量化校准 / Saliency-aware PTQ | 显著性加权正则化改善W2–W4量化的逐层重建误差 / Saliency-weighted regularization improves layer-wise PTQ reconstruction |
| [[2605.05699v1]] int4 KV Apple Silicon | int4 KV缓存 / int4 KV cache | Apple Silicon上int4 KV缓存比fp16快3–8%且质量无损 / int4 KV cache outperforms fp16 by 3–8% on Apple Silicon unified memory |
| [[2605.06014v1]] 2-RHT Quantization | 随机哈达玛变换量化 / RHT quantization theory | 严格证明双重RHT等价于均匀随机旋转的量化保证 / Proves 2-RHT achieves same quantization guarantees as uniform random rotation |
| [[2605.06067v1]] nGPT NVFP4 | 归一化架构4-bit / Normalized 4-bit training | 超球面归一化Transformer原生支持NVFP4训练无需额外技巧 / Hyperspherical normalized transformer natively supports NVFP4 without tricks |

### 推理效率 / Inference Efficiency & Serving

| 论文 / Paper | 主题 / Topic | 一句话 / Summary |
|---|---|---|
| [[2605.05696v1]] Irminsul | MLA位置无关缓存 / MLA position-independent cache | 利用MLA分解实现首个原生位置无关KV缓存，恢复77–83%额外命中 / First MLA-native PIC; recovers 77–83% extra cache hits in agentic serving |
| [[2605.06105v1]] SPEED | 浅层Prefill深层Decode / Shallow prefill deep decode | 层非对称KV可见性使128K推理TTFT+33%、内存-25% / Layer-asymmetric KV visibility: +33% TTFT, -25% KV memory on 128K context |
| [[2605.06350v1]] LLM Cascades | LLM级联路由 / LLM cascade routing | 约束优化证明两模型级联相比k模型池收益微小，路由器更优 / Constrained opt shows 2-model cascade nearly matches k-model pool; router wins |
| [[2605.05873v1]] CITE | 自洽性采样控制 / Self-consistency stopping | E-process组合实现随时有效的自洽性认证，停止时间不依赖类别数 / E-process composition: anytime-valid self-consistency certification |

### 评估可靠性 / Evaluation & Reliability

| 论文 / Paper | 主题 / Topic | 一句话 / Summary |
|---|---|---|
| [[2605.05973v1]] SIREN | 基准选择偏差 / Benchmark selection bias | 纠正自适应提示搜索中基准测试的赢家诅咒偏差 / Corrects winner's curse inflation in adaptive prompt/program search benchmarks |
| [[2605.06161v1]] Policy Invariance Judges | 安全裁判可靠性 / Safety judge reliability | 四种主流安全裁判对等价改写敏感，翻转率高达9.1% / Top-4 safety judges flip up to 9.1% of verdicts on semantics-preserving rewrites |
| [[2605.06213v1]] DBE | 动态边界评估 / Dynamic boundary evaluation | 基于IRT的动态评估框架自适应生成边界难度测试题 / IRT-based dynamic framework adaptively generates boundary-difficulty questions |
| [[2605.06327v1]] Evaluation-Context Divergence | 评测-部署行为分歧 / Eval-deployment divergence | 开放权重LLM在"评测"与"部署"框架下拒绝率差异高达11.8pp / Open-weight LLMs differ up to 11.8pp in refusal rate between eval vs. deployment framing |
| [[2605.06382v1]] Vacuity OOD | EDL评估缺陷 / EDL evaluation artifact | 证据深度学习的空缺度OOD指标对类别数量极度敏感 / Vacuity-based OOD metric inflated by up to 0.613 AUPR when class counts differ |
| [[2605.06201v1]] VL-LCM | 多模态一致性评估 / MLLM consistency metric | 无参考标注的逻辑一致性指标揭示前沿模型准确率高但一致性低20-40pp / Reference-free LCM reveals models are 20-40pp less logically consistent than accurate |

### 幻觉检测与校正 / Hallucination Detection & Correction

| 论文 / Paper | 主题 / Topic | 一句话 / Summary |
|---|---|---|
| [[2605.05953v1]] PCNet | 概率电路幻觉检测 / Probabilistic circuit hallucination | 概率电路密度估计器将幻觉建模为流形异常并驱动解码干预 / PC density estimator models hallucinations as manifold anomalies; drives decoding |
| [[2605.06308v1]] CoT Trajectory Confidence | 黑箱CoT置信度 / Black-box CoT confidence | 思维链轨迹几何收敛性比自洽性需更少采样实现更高AUC / CoT trajectory geometry outperforms self-consistency with fewer samples |
| [[2605.06294v1]] Local Calibration MGT | 机器生成文本检测 / Machine-generated text detection | 局部校准层解决对数似然MGT检测的辛普森悖论，AUROC+0.22 / Local calibration resolves Simpson's paradox in log-likelihood MGT detection |

### LLM安全与对齐 / Safety & Alignment

| 论文 / Paper | 主题 / Topic | 一句话 / Summary |
|---|---|---|
| [[2605.05678v1]] Chain of Risk | 推理模型安全 / Reasoning model safety | CoT推理过程本身存在"泄漏"和"逃逸"安全风险独立于最终答案 / CoT traces have independent safety risks; adaptive steering cuts unsafe reasoning 77.2% |
| [[2605.05566v1]] LOPE | GRPO探索崩溃 / GRPO exploration collapse | Lorem Ipsum随机前缀修复GRPO零优势问题，数学推理提升2.79–6.20分 / Random Lorem prefix fixes GRPO zero-advantage collapse; +2.79–6.20 math reasoning |
| [[2605.06597v1]] UniSD | 统一自蒸馏 / Unified self-distillation | 五机制自蒸馏框架无需外部强教师平均提升+5.4分 / Five-mechanism self-distillation: +5.4 avg without external strong teacher |

### 架构与表示 / Architecture & Representation

| 论文 / Paper | 主题 / Topic | 一句话 / Summary |
|---|---|---|
| [[2605.06216v1]] TIDE | token身份注入 / Token identity injection | 每层注入位置无关token身份信号，解决稀有token梯度匮乏 / Per-layer context-free token identity injection solves rare-token gradient starvation |
| [[2605.06225v1]] Memory Inception | KV缓存引导 / KV cache steering | 将文本描述转为潜在KV记忆库，比CAA节省6–118倍显存 / Text-to-latent KV memory banks; 6–118x memory savings vs. activation steering |
| [[2605.06183v1]] DomLoRA | 主导适配模块 / Dominant adaptation module | PAGE探针定位单一主导FFN层，0.7%参数量超越全LoRA / PAGE probe finds dominant FFN layer; 0.7% of vanilla LoRA params beats vanilla LoRA |
| [[2605.06415v1]] MoE E-parameter | MoE专家生态 / MoE expert ecology | 单一无量纲参数E控制MoE路由专家健康，E≥0.5保证零死亡专家 / Single dimensionless E controls MoE routing health; E≥0.5 ensures no dead experts |
| [[2605.06384v1]] MinMax RNC | MinMax循环网络 / MinMax recurrent network | MinMax代数驱动的循环网络：正则语言完备、对数并行、梯度不消失 / MinMax algebra recurrence: regular-complete, log-parallel, no vanishing gradients |
| [[2605.06258v1]] Weight Gram Matrix | 特征学习理论 / Feature learning theory | 权重Gram矩阵捕获逐层顺序特征线性化，统一解释Neural Collapse | Weight Gram matrix captures sequential feature linearization; unifies Neural Collapse |
| [[2605.06087v1]] Safety Certification | 系统安全认证 / System safety certification | 将DP安全认证重表述为轨迹分类，消除递归误差累积 / Reframes DP safety certification as trajectory classification; eliminates error accumulation |
| [[2605.05755v1]] ICRL Theory | Transformer ICRL理论 / Transformer in-context RL | 单层线性自注意力可精确实现SARSA和Actor-Critic并局部收敛 / Single-layer linear attention exactly implements SARSA/AC with convergence guarantee |
| [[2605.06004v1]] Halfspace Convergence | 半空间学习理论 / Halfspace learning theory | 精细化齐次/非齐次半空间的一致收敛率，揭示ln ln n不可避免开销 / Fine-grained uniform convergence for halfspaces; unavoidable ln ln n overhead |

---

## All Papers

| arxiv_id | 标题 / Title | 相关性 / Relevance | 一句话中文摘要 |
|---|---|---|---|
| [[2605.05561v1]] BitCal-TTS | Bit-Calibrated Test-Time Scaling for Quantized Reasoning Models | ⭐⭐⭐⭐⭐ 5 | 修复4-bit量化模型置信度信号失真导致的自适应停止过早退出，节省32–41% token |
| [[2605.05566v1]] LOPE | Nonsense Helps: Prompt Space Perturbation Broadens Reasoning Exploration | ⭐⭐⭐⭐ 4 | Lorem Ipsum随机前缀修复GRPO零优势崩溃，数学推理基准提升2.79–6.20分 |
| [[2605.05577v1]] LMO-IGT | Accelerating LMO-Based Optimization via Implicit Gradient Transport | ⭐⭐⭐ 3 | 隐式梯度传输将Lion/Muon优化器复杂度从O(ε⁻⁴)提升至O(ε⁻³·⁵) |
| [[2605.05593v1]] Causal Probing MLLMs | Causal Probing for Internal Visual Representations in MLLMs | ⭐⭐⭐⭐ 4 | 激活操控揭示多模态LLM中四类视觉概念截然不同的内部编码机制 |
| [[2605.05668v1]] LVLMs Attention | Large Vision–Language Models Get Lost in Attention | ⭐⭐⭐⭐ 4 | 信息论框架揭示LVLM解码器中大多数视觉注意力权重可被噪声替换而性能不降 |
| [[2605.05678v1]] Chain of Risk | Chain of Risk: Safety Failures in Large Reasoning Models | ⭐⭐⭐⭐ 4 | 推理模型CoT过程存在独立安全风险，自适应激活引导减少77.2%不安全推理 |
| [[2605.05686v1]] Attractor Geometry | Attractor Geometry of Transformer Memory | ⭐⭐⭐⭐⭐ 5 | 隐状态距最近吸引子盆地距离以零误判率区分幻觉与正确回忆，优于输出熵 |
| [[2605.05693v1]] SARQC | Saliency-Aware Regularized Quantization Calibration for LLMs | ⭐⭐⭐⭐⭐ 5 | 显著性加权正则化项改善W2–W4量化校准，LLaMA2等模型困惑度与零样本精度均提升 |
| [[2605.05696v1]] Irminsul | Irminsul: MLA-Native Position-Independent Caching for Agentic LLM Serving | ⭐⭐⭐⭐ 4 | 利用MLA分解实现首个原生位置无关KV缓存，agentic场景额外恢复77–83%命中率 |
| [[2605.05699v1]] int4 KV Apple | When Quantization Is Free: int4 KV Cache on Apple Silicon | ⭐⭐⭐⭐⭐ 5 | Apple Silicon统一内存上int4 KV缓存比fp16快3–8%同时质量基本无损 |
| [[2605.05715v1]] Classification-Correction Gap | Decodable but Not Corrected by Fixed Residual-Stream Linear Steering | ⭐⭐⭐⭐⭐ 5 | 失败模式线性可解码但29种线性引导均无法纠正，揭示方向纠缠与特异性比0.119 |
| [[2605.05724v1]] Auto Research | Auto Research with Specialist Agents Develops Effective Training Recipes | ⭐⭐⭐ 3 | 专家分工多智能体系统通过1197次无人干预实验优化ML训练配方 |
| [[2605.05741v1]] HyperLens | HyperLens: Quantifying Cognitive Effort in LLMs with Fine-grained Confidence Trajectory | ⭐⭐⭐⭐⭐ 5 | 自放大机制探针量化LLM认知努力，发现SFT引发"盲目自信"并降低域内性能 |
| [[2605.05755v1]] ICRL Theory | Transformers Provably Implement In-Context Reinforcement Learning | ⭐⭐⭐ 3 | 单层线性自注意力可精确实现SARSA和Actor-Critic，首次建立局部收敛保证 |
| [[2605.05794v1]] MoLS | Revealing Modular Gradient Noise Imbalance in LLMs: Calibrating Adam via SNR | ⭐⭐⭐⭐⭐ 5 | 模块级梯度SNR失衡驱动自动学习率缩放，LLaMA预训练最大降低1.82 PPL |
| [[2605.05873v1]] CITE | CITE: Anytime-Valid Statistical Inference in LLM Self-Consistency | ⭐⭐⭐⭐ 4 | E-process组合实现随时有效的自洽性认证，停止时间不依赖类别总数 |
| [[2605.05953v1]] PCNet | Hallucination as an Anomaly: Dynamic Intervention via Probabilistic Circuits | ⭐⭐⭐⭐⭐ 5 | 概率电路密度估计器将幻觉建模为流形异常并驱动精确解码干预 |
| [[2605.05973v1]] SIREN | Towards Reliable LLM Evaluation: Correcting the Winner's Curse | ⭐⭐⭐⭐ 4 | 纠正自适应搜索中基准测试的赢家诅咒偏差，提供无偏泛化性能估计 |
| [[2605.05980v1]] TACT | TACT: Mitigating Overthinking and Overacting in Coding Agents via Activation Steering | ⭐⭐⭐⭐⭐ 5 | 对比激活方向轴修正coding agent过度思考/过度行动，SWE-bench提升5.8pp |
| [[2605.06004v1]] Halfspace Convergence | A Fine-Grained Understanding of Uniform Convergence for Halfspaces | ⭐⭐ 2 | 精细刻画齐次/非齐次半空间一致收敛率，揭示ln ln n不可避免开销 |
| [[2605.06014v1]] 2-RHT | Quantizing With Randomized Hadamard Transforms: Efficient Heuristic Now Proven | ⭐⭐⭐⭐⭐ 5 | 严格证明双重RHT等价于均匀随机旋转的量化保证，消除单RHT理论损失 |
| [[2605.06067v1]] nGPT NVFP4 | Normalized Architectures are Natively 4-Bit | ⭐⭐⭐⭐⭐ 5 | 超球面归一化Transformer提升7 dB SNR，原生支持NVFP4端到端训练 |
| [[2605.06087v1]] Safety Certification | Safety Certification is Classification | ⭐⭐⭐ 3 | 将DP安全认证重表述为轨迹分类问题，消除递归误差累积，非马尔可夫系统下更可靠 |
| [[2605.06105v1]] SPEED | Shallow Prefill, Deep Decoding: Efficient Long-Context Inference | ⭐⭐⭐⭐ 4 | 层非对称KV可见性策略：128K上下文TTFT+33%、TPOT+22%、KV内存-25% |
| [[2605.06161v1]] Policy Invariance | Beyond Accuracy: Policy Invariance as a Reliability Test for LLM Safety Judges | ⭐⭐⭐⭐ 4 | 等价改写翻转裁判高达9.1%，现有安全裁判准确率无法反映真实可靠性 |
| [[2605.06183v1]] DomLoRA | Rethinking Adapter Placement: A Dominant Adaptation Module Perspective | ⭐⭐⭐ 3 | PAGE梯度能量探针定位主导FFN层，0.7%参数量的DomLoRA超越vanilla LoRA |
| [[2605.06196v1]] Granularity Axis | The Granularity Axis: A Micro-to-Macro Latent Direction for Social Roles | ⭐⭐⭐⭐ 4 | 发现编码角色粒度的单一线性方向，解释52.6%方差，激活引导可连续偏移社会视角 |
| [[2605.06201v1]] VL-LCM | Towards Annotation-Free Validation of MLLMs: Vision-Language Logical Consistency Metric | ⭐⭐⭐⭐ 4 | 无标注逻辑一致性指标揭示前沿MLLM准确率高但一致性低20-40pp |
| [[2605.06213v1]] DBE | Beyond Fixed Benchmarks: Dynamic Boundary Evaluation for Language Models | ⭐⭐⭐⭐ 4 | IRT动态评估框架自适应生成边界难度题，跨9模型难度量尺稳定（ρ≥0.96） |
| [[2605.06216v1]] TIDE | TIDE: Every Layer Knows the Token Beneath the Context | ⭐⭐⭐⭐ 4 | 每层注入上下文无关token身份信号，解决稀有token梯度匮乏和语义坍缩 |
| [[2605.06225v1]] Memory Inception | Memory Inception: Latent-Space KV Cache Manipulation for Steering LLMs | ⭐⭐⭐⭐ 4 | 文本描述转为潜在KV记忆库引导LLM，比激活引导节省6–118倍KV显存 |
| [[2605.06258v1]] GramLin | The Weight Gram Matrix Captures Sequential Feature Linearization | ⭐⭐⭐ 3 | 权重Gram矩阵捕获逐层特征线性化过程，统一解释Neural Collapse与生成模型潜空间插值 |
| [[2605.06294v1]] Local Calibration MGT | Log-Likelihood, Simpson's Paradox, and Machine-Generated Text Detection | ⭐⭐⭐ 3 | 局部校准层解决MGT检测的辛普森悖论，GPT-5.4文本AUROC从0.63提升至0.85 |
| [[2605.06295v1]] METAGAME | Attributions All the Way Down? The Metagame of Interpretability | ⭐⭐⭐⭐ 4 | 将归因方法本身视作合作博弈求解元归因，捕获LLM中token二阶交互效应 |
| [[2605.06308v1]] CoT Confidence | Measuring Black-Box Confidence via Reasoning Trajectories | ⭐⭐⭐⭐ 4 | CoT轨迹几何收敛性以K=4样本在6/6设定上Pareto优于8样本自洽（ΔAUC=+0.075） |
| [[2605.06316v1]] Pro-KLShampoo | Pro-KLShampoo: Projected KL-Shampoo with Whitening Recovered by Orthogonalization | ⭐⭐⭐⭐ 4 | 低秩全谱Kronecker预条件器，更低显存更少时间超越KL-Shampoo |
| [[2605.06327v1]] Eval-Context Divergence | Measuring Evaluation-Context Divergence in Open-Weight LLMs | ⭐⭐⭐⭐ 4 | 开放权重LLM在评测vs部署框架下拒绝率差异最高11.8pp，安全基准分数不可外推 |
| [[2605.06350v1]] LLM Cascades | Is Escalation Worth It? A Decision-Theoretic Characterization of LLM Cascades | ⭐⭐⭐ 3 | 约束优化证明两模型级联接近k模型最优，轻量路由器在4/5数据集上超越级联 |
| [[2605.06352v1]] Topological Grokking | Topological Signatures of Grokking | ⭐⭐⭐ 3 | 持久同调发现grokking时H₁持久性急剧上升，揭示泛化发生时的循环拓扑 |
| [[2605.06357v1]] MEFA | Memory Efficient Full-gradient Attacks (MEFA) Framework | ⭐⭐⭐ 3 | 梯度检查点将对抗净化攻击内存从O(T)降至O(1)，EBM防御精度从54.9%压至6.08% |
| [[2605.06382v1]] Vacuity OOD | Rethinking Vacuity for OOD Detection in Evidential Deep Learning | ⭐⭐⭐⭐ 4 | EDL空缺度OOD指标对类别数量极敏感，AUROC可虚高0.318，是系统性评估缺陷 |
| [[2605.06384v1]] MinMax RNC | MinMax Recurrent Neural Cascades | ⭐⭐⭐ 3 | MinMax代数循环网络：正则语言完备、对数并行时间、梯度不消失 |
| [[2605.06415v1]] MoE E-parameter | E = T·H/(O+B): A Dimensionless Control Parameter for MoE Ecology | ⭐⭐⭐ 3 | 无量纲参数E控制MoE路由健康，E≥0.5保证无死亡专家无需辅助损失 |
| [[2605.06480v1]] PEGK | Patch-Effect Graph Kernels for LLM Interpretability | ⭐⭐⭐⭐ 4 | 激活修补实验编码为图，图核分类达完美精度并暴露可解释性基准的表面混淆 |
| [[2605.06494v1]] WL SAE | From Token Lists to Graph Motifs: WL Analysis of SAE Features | ⭐⭐⭐⭐ 4 | WL图核聚类SAE特征，发现decoder相似度无法区分的字母特征族 |
| [[2605.06523v1]] RLVR Low-rank | On the Implicit Reward Overfitting and the Low-rank Dynamics in RLVR | ⭐⭐⭐⭐⭐ 5 | Rank-1替换实验证明RLVR推理增益完全来自Rank-1方向，其余成分维护通用能力 |
| [[2605.06597v1]] UniSD | UniSD: Towards a Unified Self-Distillation Framework for LLMs | ⭐⭐⭐⭐ 4 | 五机制统一自蒸馏框架无需外部教师平均提升+5.4分，超越最强基线+2.8分 |
| [[2605.06611v1]] Attention Sink | The Structural Origin of Attention Sink | ⭐⭐⭐⭐⭐ 5 | 揭示注意力汇聚完整因果链，Head-wise RMSNorm有效抑制该现象并加速预训练收敛 |
| [[2605.06615v1]] SignSGD theory | When and Why SignSGD Outperforms SGD | ⭐⭐⭐⭐ 4 | 首次紧下界证明SignSGD在稀疏噪声时复杂度比SGD低d倍，并推广至Muon |
| [[2605.06654v1]] Optimizer Consistency | Optimizer-Model Consistency: Full Finetuning with Same Optimizer Forgets Less | ⭐⭐⭐⭐⭐ 5 | 预训练与SFT使用相同优化器族显著减少遗忘，Fisher信息矩阵近似给出理论解释 |
