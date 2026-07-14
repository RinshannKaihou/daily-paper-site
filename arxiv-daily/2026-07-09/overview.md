---
title: "每日论文速递 / Daily Paper Digest — 2026-07-09"
date: 2026-07-09
tags:
  - llm-agents
  - ai-safety
  - uncertainty-quantification
  - model-compression
  - interpretability
  - calibration
  - mechanistic-interpretability
  - quantization
  - vision-language
  - optimization-theory
  - diffusion-models
  - long-context
  - benchmark
  - autonomous-research
  - self-evolving
papers: 50
---

## 今日必读 / Must Read Today

### 1. [[2607.08349]] — Certified Interventional Fidelity (CIF)

> **为什么必读：** 本文为机制可解释性评估（IIA、activation patching、circuit completeness）提出了首个统一的"因果被估量 + anytime-valid 置信序列"统计层，将散落的点估计分数统一为带有限样本保证的区间，betting 序列使认证成本降低 10–30 倍，并暴露出在强扰动下没有任何非恒等抽象能通过 F≥0.90 这一被点估计掩盖的事实。它直接回应了"可解释性评估不可靠、被自适应采样污染"的社区痛点，是一个有可能改变评估规范的模块化框架。
>
> **Why must-read:** CIF reframes heterogeneous interpretability metrics (IIA, patching recovery, circuit completeness, causal scrubbing) into one bounded causal estimand and wraps it with anytime-valid confidence sequences, cutting certification cost 10–30× via variance-adaptive betting sequences while exposing a masked negative result (no non-identity abstraction reaches F≥0.90 at p=0.5) that point estimates hide. It is a modular layer that could change how the community reports interventional evidence.

### 2. [[2607.08456]] — Two Axes of LLM Abstention: Answer Correctness and Question Answerability

> **为什么必读：** 本文揭示了一个被忽视的几何结构——LLM 的拒答问题在"答案是否正确"和"问题是否可答"两个轴上分离，而单一置信度阈值只能读取前者；隐藏状态探针在可答性上达到 0.97–0.99 AUROC（远超输出端的 0.54–0.67），由此提出的"因子化拒答"双风险策略在 8B 模型上以 0.75 覆盖率同时认证两个误差预算（置信度单阈值仅 0.31）。对任何关心 LLM 可靠部署与 conformal 拒答的人都极具价值。
>
> **Why must-read:** The paper uncovers a neglected geometric structure — LLM abstention decomposes along two axes (answer correctness vs. question answerability) that separate on the same decisions but need different signals; ordinary confidence reads only the first, while a hidden-state answerability probe reaches 0.97–0.99 AUROC, enabling a Factorized Abstention policy that certifies both error budgets at 0.75 coverage on an 8B model where confidence-only conformal abstention manages only 0.31.

### 3. [[2607.08066]] — Persuasion Attacks on Chain-of-Thought Monitoring

> **为什么必读：** 随着 CoT 监控被广泛部署为前沿 AI 安全的主要防线，本文系统研究了其脆弱性——对抗性 CoT 能通过说服策略使监控者误判危险行为，揭示了"监控者与被监控者能力不对称"这一根本性风险。对于关心 AI 安全审计、alignment monitoring 与 scalable oversight 的读者，这是理解当前安全范式局限性的关键工作。
>
> **Why must-read:** As chain-of-thought monitoring becomes a primary defense line for frontier AI safety, this work systematically studies its vulnerability to persuasion attacks, where adversarial reasoning persuades the monitor to misclassify dangerous behavior — exposing the fundamental risk of a capability asymmetry between monitor and monitored, which is essential reading for anyone working on alignment monitoring and scalable oversight.

---

## 按主题分类 / Papers by Topic

### LLM 智能体与自主研究 / LLM Agents & Autonomous Research

| 论文 / Paper | 一句话总结 / TL;DR |
|---|---|
| [[2607.08010]] Tool-Making Agents | 亚马逊物流中心生产环境部署的工具制造智能体 / Tool-making agents deployed at Amazon fulfillment centers in production. |
| [[2607.08124]] TTHE | 测试时工具演化框架让智能体在部署中自主进化工具 / Test-Time Harness Evolution lets agents self-evolve tools during deployment. |
| [[2607.08252]] AutoPersonas | 自动生成角色智能体以模拟多元用户行为 / Automated persona-driven agents for simulating diverse user behavior. |
| [[2607.08332]] XALPHA | 记忆驱动的 AI 量化研究员实现假说到代码的 Alpha 发现闭环 / Memory-driven AI quant researcher for hypothesis-to-code alpha discovery (IR=1.59). |
| [[2607.08662]] WebSwarm | 递归多智能体委派框架实现深而广的网页信息检索 / Recursive multi-agent orchestration for deep-and-wide web search (+17.5 ACC). |
| [[2607.08665]] RoR | 预算感知的"重采样还是重路由"测试时模型选择策略 / Budget-aware resample-or-reroute test-time model selection (+10.7 pts on GPQA). |
| [[2607.08758]] IdeaGene-Bench | 科学谱系推理与谱系锚定的创意生成基准 / Benchmark for scientific lineage reasoning and lineage-grounded idea generation. |
| [[2607.08003]] CoThinker | LLM 驱动的 CO2 电还原催化剂发现 / LLM-driven catalyst discovery for CO2 electroreduction. |

### AI 安全、审计与对齐 / AI Safety, Auditing & Alignment

| 论文 / Paper | 一句话总结 / TL;DR |
|---|---|
| [[2607.08054]] Constitutional Meta-STPA | 用宪法方法让 LLM 对自身安全规约进行自验证 / Constitutional method for LLM safety self-validation via STPA. |
| [[2607.08065]] Self-Consistency Audit | 揭示"自一致性≠准确性"，一致性协议可能掩盖缺陷 / Reveals agreement≠accuracy; self-consistency can mask defects. |
| [[2607.08066]] Persuasion Attacks on CoT | 对抗性推理能说服 CoT 监控者误判危险行为 / Adversarial reasoning persuades CoT monitors to misclassify danger. |
| [[2607.08077]] GRAM | 梯度路由辅助模块实现访问控制 / Gradient-routed auxiliary modules for access control. |
| [[2607.08173]] Overthinking | 审计推理放大现象中的过度思考行为 / Auditing overthinking behaviors in reasoning amplification. |
| [[2607.08550]] ESBMC-Arduino | 修复开源硬件 PLC 形式化验证的部署鸿沟（误报 54→0）/ Closes the deployment gap in formal verification of open-hardware PLCs (54→0 false alarms). |

### 不确定性量化、校准与统计评估 / Uncertainty, Calibration & Statistical Evaluation

| 论文 / Paper | 一句话总结 / TL;DR |
|---|---|
| [[2607.08017]] GRAPHEVAL | 基于图的不确定性量化方法评估 LLM 推理 / Graph-based uncertainty quantification for LLM reasoning evaluation. |
| [[2607.08046]] LLM Forecaster Probing | 探针研究 LLM 预测器的校准特性 / Probing calibration properties of LLM forecasters. |
| [[2607.08377]] Eigenvalue Calibration | 首次将密度矩阵特征值作为校准对象，提出矩阵温度缩放 / First calibration of density-matrix eigenvalues via matrix temperature scaling. |
| [[2607.08456]] Two Axes of Abstention | 拒答分解为答案正确性与问题可答性两个轴 / Abstention decomposes into answer-correctness and answerability axes. |
| [[2607.08349]] Certified Interventional Fidelity | 为干预式可解释性评估提供 anytime-valid 置信序列 / Anytime-valid confidence sequences for interventional interpretability evaluation (10–30× cheaper). |
| [[2607.08522]] Stop Guessing When to Stop Testing | 分组序贯检验使 VLM 评测成本降低约 80% / Group sequential testing cuts VLM evaluation cost ~80%. |

### 模型压缩、量化与高效推理 / Model Compression, Quantization & Efficient Inference

| 论文 / Paper | 一句话总结 / TL;DR |
|---|---|
| [[2607.08015]] CRIMP | ReRAM 交叉栏压缩方法 / ReRAM crossbar compression for efficient inference. |
| [[2607.08029]] Small VLM Quantization (Jetson) | Jetson 平台上小型视觉语言模型量化 / Small VLM quantization on Jetson edge platforms. |
| [[2607.08241]] GAMP | CFG 扩散模型的量化方法 / Quantization for CFG-based diffusion models. |
| [[2607.08526]] aria | 无依赖的量化原生运行时跑 Stable Audio 3（含树莓派 5）/ Dependency-free quantized native runtime for Stable Audio 3 (runs on Pi 5). |
| [[2607.08643]] BiSCo-LLM | 无码本二进制球面编码实现约 2-bit LLM 压缩 / Codebook-free binary spherical coding for ~2-bit LLM compression (PPL 10.18). |
| [[2607.08734]] Illusion of Equivalency | "正确性一致度"指标揭示量化隐藏的行为漂移 / "Correctness agreement" metric exposes hidden quantization behavioral drift. |
| [[2607.08733]] Super Weights | 证明"超级权重"重要但不等于可孤立训练；LoRA 靠整层分解成功 / Shows Super Weights are important but not isolately trainable; LoRA succeeds via full-layer decomposition. |
| [[2607.08399]] Activation Prompt Compression | 激活空间提示压缩，MLP 学习 patch 向量注入早期层 / Activation-space prompt compression via learned MLP patch vector injected at early layers (~2% drop). |

### 视觉语言与多模态 / Vision-Language & Multimodal

| 论文 / Paper | 一句话总结 / TL;DR |
|---|---|
| [[2607.08059]] When Thinking Hurts | 揭示 VLM 推理时答案熵坍缩现象 / Reveals answer-entropy collapse during VLM reasoning. |
| [[2607.08194]] Low-Rank VL Alignment | 低秩对齐方法改进视觉语言模型 / Low-rank alignment for vision-language models. |
| [[2607.08605]] S²AE | 结构化稀疏自编码器使 VLM 概念更连贯且跨模态一致 / Structured sparse autoencoder for more coherent and cross-modally consistent VLM concepts. |
| [[2607.08317]] Blind-Spots-Bench | 235 个人类简单但 AI 困难的多模态盲点基准 / 235-question benchmark of human-easy but AI-hard multimodal blind spots (38 models). |

### 可解释性与探测 / Interpretability & Probing

| 论文 / Paper | 一句话总结 / TL;DR |
|---|---|
| [[2607.08499]] Procrustes Joint SAE | Procrustes 旋转对齐后共享 SAE 提取跨种子通用特征 / Procrustes-aligned joint SAE extracts cross-seed universal BERT features (r: 0.646→0.865). |
| [[2607.08339]] TypeProbe | 线性探针从代码模型隐藏状态恢复跨语言类型表示 / Linear probes recover cross-lingual type representations from code model hidden states. |
| [[2607.08170]] Layer Patching | 层级补丁方法实现模型尺寸插值 / Layer patching for model size interpolation. |

### 长上下文、记忆与知识 / Long-Context, Memory & Knowledge

| 论文 / Paper | 一句话总结 / TL;DR |
|---|---|
| [[2607.08032]] COMPACT-Bench | 率失真记忆压缩方法综述与基准 / Survey and benchmark for rate-distortion memory compaction. |
| [[2607.08284]] PredicateLongBench | 谓词级长上下文难度基准 / Predicate-level long-context difficulty benchmark. |
| [[2607.08393]] Knowing-Using Gap | 揭示微调中"记住但不会用"的知识电路错位，self-patching 恢复 58–75% / Formalizes the memorize-but-can't-use gap; self-patching recovers 58–75% of oracle. |

### 扩散模型 / Diffusion Models

| 论文 / Paper | 一句话总结 / TL;DR |
|---|---|
| [[2607.08041]] BIRD | 贝叶斯扩散模型的信息论分析 / Information-theoretic analysis of Bayesian diffusion models. |
| [[2607.08757]] Score Stability | 证明 on-path score 误差小不保证采样数值稳定性；denoiser 投影可修复 / Forward-marginal score error does NOT certify sampling stability; denoiser projection fixes it. |

### 优化与学习理论 / Optimization & Learning Theory

| 论文 / Paper | 一句话总结 / TL;DR |
|---|---|
| [[2607.08104]] Vanilla SGD Heavy-Tailed | 理论分析 vanilla SGD 的重尾噪声特性 / Theoretical analysis of heavy-tailed noise in vanilla SGD. |
| [[2607.08380]] GD Large Step Size | 大步长 GD 在平坦极小值流形附近的动力学推广 / Generalizes large-step-size GD dynamics near manifolds of flat minima. |
| [[2607.08581]] Spectral Stability ELM | 谱分析揭示伪逆 ELM 的数值稳定性由最小奇异值控制 / Spectral analysis: smallest singular value governs pseudoinverse ELM stability. |

### 硬件与 VLSI / Hardware & VLSI

| 论文 / Paper | 一句话总结 / TL;DR |
|---|---|
| [[2607.08002]] Stochastic Activity Prediction | Wallace-tree 乘法器的随机活动预测理论 / Stochastic activity prediction theory for Wallace-tree multipliers. |

### 语音与音频 / Speech & Audio

| 论文 / Paper | 一句话总结 / TL;DR |
|---|---|
| [[2607.08256]] Best-of-N TTS ASR | 揭示 Best-of-N 选择中 TTS 与 ASR 的家族混淆因素 / Exposes TTS/ASR family confounds in Best-of-N selection. |

### 强化学习与多智能体 / Reinforcement Learning & Multi-Agent

| 论文 / Paper | 一句话总结 / TL;DR |
|---|---|
| [[2607.08193]] VIP | 策略视觉检查方法用于多智能体 RL / Visual Inspection of Policies for multi-agent reinforcement learning. |

### 世界模型与神经符号 / World Models & Neural-Symbolic

| 论文 / Paper | 一句话总结 / TL;DR |
|---|---|
| [[2607.08312]] Write-Protected Bottlenecks | 写保护离散瓶颈改进世界模型 / Write-protected discrete bottlenecks for world models. |

### 医学影像 / Medical Imaging

| 论文 / Paper | 一句话总结 / TL;DR |
|---|---|
| [[2607.08203]] Polyp Segmentation Audit | 息肉分割基准审计揭示评估方法论问题 / Polyp segmentation benchmark audit reveals evaluation methodology issues. |

### 评测方法论 / Benchmark & Evaluation Methodology

| 论文 / Paper | 一句话总结 / TL;DR |
|---|---|
| [[2607.08535]] Auditing LLM-as-Judge | 将换裁判导致分数变化重新定义为测量效度问题 / Reframes judge-replacement score changes as a measurement-validity problem. |
| [[2607.08700]] Citation Verifier Benchmark | 深度研究引文验证基准：廉价 judge 足够且标量 F1 掩盖方向性偏差 / Deep-research citation benchmark: cheaper judges suffice; scalar F1 hides directional bias. |

---

## All Papers

| # | 论文 / Paper | 主题 / Topic | 一句话总结 / TL;DR |
|---|---|---|---|
| 1 | [[2607.08002]] Stochastic Activity Prediction | 硬件 / Hardware | Wallace-tree 乘法器的随机活动预测理论 / Stochastic activity prediction for Wallace-tree multipliers. |
| 2 | [[2607.08003]] CoThinker | 智能体 / Agents | LLM 驱动的 CO2 电还原催化剂发现 / LLM-driven catalyst discovery for CO2 electroreduction. |
| 3 | [[2607.08010]] Tool-Making Agents | 智能体 / Agents | 亚马逊生产环境的工具制造智能体 / Tool-making agents in Amazon production. |
| 4 | [[2607.08015]] CRIMP | 量化 / Quantization | ReRAM 交叉栏压缩方法 / ReRAM crossbar compression. |
| 5 | [[2607.08017]] GRAPHEVAL | 不确定性 / UQ | 基于图的 LLM 推理不确定性量化 / Graph-based UQ for LLM reasoning. |
| 6 | [[2607.08029]] Small VLM Quantization (Jetson) | 量化 / Quantization | Jetson 上小型 VLM 量化 / Small VLM quantization on Jetson. |
| 7 | [[2607.08032]] COMPACT-Bench | 长上下文 / Long-Context | 率失真记忆压缩综述与基准 / Rate-distortion memory compaction benchmark. |
| 8 | [[2607.08041]] BIRD | 扩散模型 / Diffusion | 贝叶斯扩散模型信息论分析 / Information theory of Bayesian diffusion. |
| 9 | [[2607.08046]] LLM Forecaster Probing | 校准 / Calibration | 探针研究 LLM 预测器校准 / Probing LLM forecaster calibration. |
| 10 | [[2607.08054]] Constitutional Meta-STPA | 安全 / Safety | LLM 安全规约自验证 / LLM safety self-validation. |
| 11 | [[2607.08059]] When Thinking Hurts | 多模态 / Multimodal | VLM 推理时答案熵坍缩 / Answer-entropy collapse in VLM reasoning. |
| 12 | [[2607.08065]] Self-Consistency Audit | 安全 / Safety | 自一致性≠准确性 / Agreement≠accuracy. |
| 13 | [[2607.08066]] Persuasion Attacks on CoT | 安全 / Safety | 对抗推理说服 CoT 监控者 / Persuasion attacks on CoT monitors. |
| 14 | [[2607.08077]] GRAM | 安全 / Safety | 梯度路由辅助模块做访问控制 / Gradient-routed access control. |
| 15 | [[2607.08104]] Vanilla SGD | 优化理论 / Optimization | SGD 重尾噪声理论分析 / Heavy-tailed noise in vanilla SGD. |
| 16 | [[2607.08124]] TTHE | 智能体 / Agents | 测试时工具自主演化 / Test-time harness evolution for agents. |
| 17 | [[2607.08170]] Layer Patching | 可解释性 / Interpretability | 层级补丁做模型尺寸插值 / Layer patching for size interpolation. |
| 18 | [[2607.08173]] Overthinking | 安全 / Safety | 审计过度思考行为 / Auditing overthinking. |
| 19 | [[2607.08193]] VIP | 强化学习 / RL | 多智能体策略视觉检查 / Visual inspection of MARL policies. |
| 20 | [[2607.08194]] Low-Rank VL Alignment | 多模态 / Multimodal | 低秩视觉语言对齐 / Low-rank vision-language alignment. |
| 21 | [[2607.08203]] Polyp Segmentation Audit | 医学影像 / Medical | 息肉分割基准审计 / Polyp segmentation benchmark audit. |
| 22 | [[2607.08241]] GAMP | 量化 / Quantization | CFG 扩散模型量化 / CFG diffusion quantization. |
| 23 | [[2607.08252]] AutoPersonas | 智能体 / Agents | 自动角色智能体生成 / Automated persona agents. |
| 24 | [[2607.08256]] Best-of-N TTS ASR | 语音 / Speech | TTS/ASR 家族混淆因素 / TTS/ASR family confounds in Best-of-N. |
| 25 | [[2607.08284]] PredicateLongBench | 长上下文 / Long-Context | 谓词级长上下文难度基准 / Predicate-level long-context benchmark. |
| 26 | [[2607.08312]] Write-Protected Bottlenecks | 世界模型 / World Models | 写保护离散瓶颈 / Write-protected discrete bottlenecks. |
| 27 | [[2607.08317]] Blind-Spots-Bench | 多模态 / Multimodal | 235 题多模态盲点基准 / 235-question multimodal blind-spots benchmark. |
| 28 | [[2607.08332]] XALPHA | 智能体 / Agents | 记忆驱动 AI 量化研究员 (IR=1.59) / Memory-driven AI quant researcher. |
| 29 | [[2607.08339]] TypeProbe | 可解释性 / Interpretability | 代码模型跨语言类型表示恢复 / Cross-lingual type representation recovery from code models. |
| 30 | [[2607.08349]] Certified Interventional Fidelity | 不确定性 / UQ | 干预式可解释性的 anytime-valid 置信序列 / Anytime-valid CS for interventional interpretability. |
| 31 | [[2607.08377]] Eigenvalue Calibration | 校准 / Calibration | 密度矩阵特征值矩阵温度缩放校准 / Matrix temperature scaling for eigenvalue calibration. |
| 32 | [[2607.08380]] GD Large Step Size | 优化理论 / Optimization | 大步长 GD 在平坦极小值流形的动力学 / Large-step GD dynamics near flat-minima manifolds. |
| 33 | [[2607.08393]] Knowing-Using Gap | 知识 / Knowledge | 微调知识电路错位与 self-patching 修复 / Knowledge-circuit misalignment and self-patching repair. |
| 34 | [[2607.08399]] Activation Prompt Compression | 高效推理 / Efficient Inference | 激活空间提示压缩 patch 向量 / Activation-space prompt compression patch vector. |
| 35 | [[2607.08456]] Two Axes of Abstention | 校准 / Calibration | 拒答分解为正确性与可答性两轴 / Abstention decomposes into correctness and answerability axes. |
| 36 | [[2607.08499]] Procrustes Joint SAE | 可解释性 / Interpretability | Procrustes 对齐的跨种子通用 SAE / Procrustes-aligned cross-seed universal SAE. |
| 37 | [[2607.08522]] Stop Guessing When to Stop Testing | 评测 / Evaluation | 分组序贯检验降 VLM 评测成本 80% / Group sequential testing cuts VLM eval cost ~80%. |
| 38 | [[2607.08526]] aria | 量化 / Quantization | 无依赖量化运行时跑 Stable Audio 3 / Dependency-free quantized runtime for Stable Audio 3. |
| 39 | [[2607.08535]] Auditing LLM-as-Judge | 评测 / Evaluation | 换裁判的测量效度问题 / Measurement-validity of judge replacement. |
| 40 | [[2607.08550]] ESBMC-Arduino | 安全 / Safety | 修复 PLC 形式化验证部署鸿沟 (54→0 误报) / Closes PLC formal verification deployment gap. |
| 41 | [[2607.08581]] Spectral Stability ELM | 优化理论 / Optimization | 伪逆 ELM 谱稳定性分析 / Spectral stability of pseudoinverse ELM. |
| 42 | [[2607.08605]] S²AE | 多模态 / Multimodal | 结构化稀疏自编码器改善 VLM 概念一致性 / Structured SAE improves VLM concept consistency. |
| 43 | [[2607.08643]] BiSCo-LLM | 量化 / Quantization | 无码本二进制球面编码 2-bit 压缩 / Codebook-free binary spherical coding at ~2-bit. |
| 44 | [[2607.08662]] WebSwarm | 智能体 / Agents | 递归多智能体网页搜索 (+17.5 ACC) / Recursive multi-agent web search. |
| 45 | [[2607.08665]] RoR | 智能体 / Agents | 预算感知重采样或重路由 (+10.7 pts GPQA) / Budget-aware resample-or-reroute selection. |
| 46 | [[2607.08700]] Citation Verifier Benchmark | 评测 / Evaluation | 深度研究引文验证：廉价 judge 足够 / Citation verification: cheaper judges suffice. |
| 47 | [[2607.08733]] Super Weights | 压缩 / Compression | 超级权重重要但不可孤立训练 / Super Weights important but not isolately trainable. |
| 48 | [[2607.08734]] Illusion of Equivalency | 量化 / Quantization | 正确性一致度揭示量化行为漂移 / Correctness agreement exposes quantization drift. |
| 49 | [[2607.08757]] Score Stability | 扩散模型 / Diffusion | on-path score 误差不保证采样稳定性 / On-path score error does not certify sampling stability. |
| 50 | [[2607.08758]] IdeaGene-Bench | 智能体 / Agents | 科学谱系推理与创意生成基准 / Scientific lineage reasoning and idea generation benchmark. |
