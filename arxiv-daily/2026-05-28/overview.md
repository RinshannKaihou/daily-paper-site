---
title: "Daily Paper Digest — 2026-05-28"
date: 2026-05-28
tags:
  - llm-training
  - mechanistic-interpretability
  - quantization
  - llm-safety
  - reinforcement-learning
  - representation-engineering
  - llm-evaluation
  - optimization
  - moe
  - lora
papers: 50
---

## 今日必读 / Must Read Today

### 1. [[2605.29491]] The Curse of Helpfulness: Inverse Scaling Law in Robustness to Distractor Instructions

逆缩放定律 / Inverse scaling law: Qwen3 0.6B→235B 的干扰指令鲁棒性从 65.97 降至 37.6，RMR（鲁棒性边界比率）从 2.24 压缩至 1.30 / Qwen3 robustness to distractor instructions drops from 65.97 to 37.6 as scale grows 0.6B→235B, with RMR compressing from 2.24 to 1.30. GRPO RL 训练可恢复 15.5% 鲁棒性 / GRPO RL training recovers up to 15.5% robustness.

### 2. [[2605.29548]] Why Larger Models Learn More: Effects of Capacity, Interference, and Rare-Task Retention

大模型为何能学到小模型学不到的任务 / Why larger models learn tasks that smaller models fail on. 通过 OLMo 4M→4B 的受控实验证明：小模型神经元被高频任务占满、稀有任务被挤出；大模型通过减弱梯度干扰保留稀有特征 / OLMo 4M→4B experiments prove small models crowd out rare tasks while larger models retain them via reduced gradient interference. 含机制化分析（行为、表征、梯度三层）/ Includes mechanistic analysis at behavioral, representational, and gradient levels.

### 3. [[2605.29756]] LFQ: Logit-aware Final-block Quantization for Boosting Generation Quality of Low-Bit Quantized LLMs

仅替换最终 Transformer 块的 MSE 为交叉熵损失即可显著提升量化 LLM 的生成质量 / Simply replacing MSE with cross-entropy loss for the final transformer block significantly boosts quantized LLM generation quality. ICML 2026 接收，AIME 上 +13pp / Accepted at ICML 2026, +13pp on AIME for reasoning models.

---

## 按主题分类 / Papers by Topic

### LLM 训练稳定性与优化 / LLM Training Stability & Optimization

| Paper | 一句话总结 / One-line Summary |
|-------|-----------------------------|
| [[2605.29396]] | 零阶优化精调安全关键层，W4A4量化ASR从0.25降至0.18 / Zeroth-order refinement on safety-critical layers reduces W4A4 ASR from 0.25 to 0.18 |
| [[2605.29494]] | 梯度扰动统一框架（SAM/裁剪/噪声均为 g+delta_g），在长尾和噪声标签上持续优于现有方法 / Unified gradient perturbation framework (SAM/clipping/noise all as g+delta_g), outperforms existing methods on long-tail and noisy labels |
| [[2605.29525]] | 隐藏层激活扰动统一分析（Dropout/Mixup/对抗扰动），LPA在长尾分类上超越LPL 5.4% / Unified hidden activation perturbation analysis, LPA surpasses LPL by 5.4% on long-tail classification |
| [[2605.29547]] | S-Adam 优化器通过随机方向导数方差探测奇异性，2-bit QAT准确率提升6% / S-Adam optimizer probes singularity via randomized directional derivative variance, +6% on 2-bit QAT |
| [[2605.29664]] | AMDP 异步多方向流水线并行，首阶段限2微批次保证不匹配≤1步，吞吐提升17% / AMDP async multi-directional pipeline parallelism, mismatch bounded to 1 step, +17% throughput |
| [[2605.29823]] | 多项式有效次数（Effective Degree）作为简洁性度量优于sharpness预测泛化 / Polynomial Effective Degree as simplicity metric outperforms sharpness for predicting generalization |
| [[2605.30334]] | LLM训练数据组织四原则（边界锐化/循环调度/连续性/局部多样性），近零额外开销 / Four data organization principles for LLM training at near-zero extra cost |
| [[2605.30260]] | LoRA 参数记忆定律 ΔL=C·r^α·ℓ^-β+b，p>0.5 是逐字回忆相变临界点 / LoRA parametric memory law ΔL=C·r^α·ℓ^-β+b, p>0.5 is phase transition threshold for verbatim recall |

### 隐状态与可解释性 / Hidden States & Interpretability (SAEs, circuits, representation geometry)

| Paper | 一句话总结 / One-line Summary |
|-------|-----------------------------|
| [[2605.29507]] | Xetrieval 首个嵌入层面稠密检索机制化解释框架，TopK-SAE分解推理增强嵌入 / Xetrieval first embedding-level mechanistic explanation for dense retrieval via TopK-SAE decomposition |
| [[2605.29548]] | 大模型通过减弱梯度干扰保留稀有任务特征，含OLMo 4M-4B表征/梯度分析 / Larger models retain rare-task features via reduced gradient interference, OLMo 4M-4B representation/gradient analysis |
| [[2605.29580]] | LoRA-Curve 在 LoRA 空间中用 Bezier 曲线构建连续低损失谷地，贝叶斯推理新范式 / LoRA-Curve constructs continuous low-loss valleys in LoRA space via Bezier curves, new paradigm for Bayesian inference |
| [[2605.29628]] | COMET 揭示 CLAP 嵌入空间呈"均值+共享语义头(~100维)+模态私有尾(~924维)"结构 / COMET reveals CLAP embedding space structure: mean + shared semantic head (~100 dims) + modality-private tail (~924 dims) |
| [[2605.29634]] | Plucker 符号熵检测 Transformer 隐藏状态中关系元组的秩匹配方向签名 / Plucker sign entropy detects rank-matched orientation signatures of relation tuples in transformer hidden states |
| [[2605.29889]] | SAE 揭示 LLM 分诊失败源于输出映射而非医学知识缺失，决策 token 处医学特征沉默 / SAE reveals LLM triage failure is in output mapping not medical knowledge, medical features silent at decision token |
| [[2605.29901]] | Gemma-2-2b 漏洞检测采用"安全模式检测器"策略，仅16.1%参数参与检测电路 / Gemma-2-2b vulnerability detection uses "safety pattern detector" strategy, only 16.1% params in detection circuit |
| [[2605.29971]] | 连续变量因果干预方法（PCA+回归定位+最小L2编辑），动词偏好可系统性调控句法选择 / Continuous variable causal intervention method (PCA+regression+min-L2 editing), verb bias causally steers syntactic choices |
| [[2605.30018]] | LPP 从隐藏层提取三个任务无关指标（最小熵/有效秩/参与比），揭示 benchmark 相似模型的内部差异 / LPP extracts three task-agnostic metrics from hidden layers, revealing internal differences in benchmark-similar models |
| [[2605.30022]] | DSTG-NeoBERT 将语义/AP/RP 三流解耦，AP 自发塌缩为二维正弦流形（94.1%方差）/ DSTG-NeoBERT disentangles semantic/AP/RP streams, AP spontaneously collapses to 2D sinusoidal manifold (94.1% variance) |
| [[2605.30161]] | VLM 普遍存在"垂直-距离纠缠"（更高=更远），表征层面对比探针量化纠缠指数 / VLMs universally conflate "higher in image" with "farther" (vertical-distance entanglement), quantified via contrastive probing |
| [[2605.30232]] | RL 训练征用预存"功能性福祉轴"（惩罚向量促进失败token、负面情绪、病态回溯）/ RL training recruits pre-existing "functional welfare axis" (punishment vector promotes failure tokens, negative emotions, pathological backtracking) |
| [[2605.30233]] | LLM 实体追踪采用并行聚合而非增量更新，REMOVE 使用脆弱全局抑制标签 / LLM entity tracking uses parallel aggregation not incremental updates, REMOVE uses fragile global suppression tag |
| [[2605.30049]] | SafeDIG 在 DiT 不同功能层构建 SAE，中间层（Double Stream Block）安全迁移最稳定 / SafeDIG builds SAEs at different DiT functional layers, middle-layer (Double Stream Block) transfer most stable |
| [[2605.30076]] | UniSteer 用流匹配在激活空间实现文本引导的统一操控（行为控制/真实性/分类五类任务）/ UniSteer uses flow matching for text-guided unified activation-space steering across 5 task categories |
| [[2605.30162]] | SAE 特征分析揭示生物安全拒绝行为更多反映法律/文化敏感性而非实际 CBRN 危险等级 / SAE feature analysis reveals biosecurity refusal tracks legal/cultural salience over actual CBRN hazard |
| [[2605.29634]] | Relational Rank Geometry: Plucker 坐标检测 Transformer 关系帧秩签名（8B→405B）/ Relational Rank Geometry via Plucker coordinates detects relation frame rank signatures (8B→405B) |
| [[2605.29782]] | Hista 用隐藏状态相似度加权估计状态价值，揭示 PPO critic 在 LLM RL 中退化为组平均 / Hista uses hidden-state similarity for state value estimation, reveals PPO critic collapses to group-average in LLM RL |
| [[2605.29888]] | LaRA 通过逐层表征几何分析检测 RL 后训练数据污染，AUC 提升 +9.6% / LaRA detects RL post-training data contamination via layer-wise representation geometry analysis, +9.6% AUC |
| [[2605.29751]] | DySem 利用多语言共识从 LLM 内部提取语义维度，累计注意力输出优于最终隐藏状态 / DySem extracts semantic dimensions via multilingual consensus, cumulative attention outputs outperform final hidden states |

### 量化与计算可靠性 / Quantization & Computation Reliability

| Paper | 一句话总结 / One-line Summary |
|-------|-----------------------------|
| [[2605.29705]] | BitTP 将 T5-small 轨迹预测模型通过 1.58-bit 权重量化转换，仅权重可量化 / BitTP converts T5-small trajectory predictor via 1.58-bit weight-only quantization, activations must stay full precision |
| [[2605.29843]] | HARP 可学习正交旋转替代固定 Hadamard，Llama 2 7B 2-bit PPL 从 8.22 降至 7.24 / HARP learnable orthogonal rotation replaces fixed Hadamard, Llama 2 7B 2-bit PPL drops from 8.22 to 7.24 |
| [[2605.29756]] | LFQ 仅替换最终块 MSE 为交叉熵，AIME 推理模型 +13pp（ICML 2026）/ LFQ replaces only final-block MSE with cross-entropy, +13pp on AIME reasoning models (ICML 2026) |
| [[2605.29537]] | 量化 FNN 验证完整复杂度图谱：量化 NP 完全、动态量化 BV PSPACE 完全 / Complete complexity landscape for quantised FNN verification: quantised NP-complete, dynamically quantised BV PSPACE-complete |
| [[2605.30218]] | MarginGate 用 top-1/top-2 logit margin 稀疏触发验证，LLM 推理确定性 2x 加速 / MarginGate uses logit margin for sparse verification, 2x faster deterministic LLM inference |

### LLM 安全与对齐 / LLM Safety & Alignment

| Paper | 一句话总结 / One-line Summary |
|-------|-----------------------------|
| [[2605.29396]] | 零阶优化精调安全关键层提升鲁棒性，13.3% 额外训练时间 / Zeroth-order refinement on safety-critical layers, 13.3% extra training time |
| [[2605.29491]] | 干扰指令逆缩放定律：大模型更易受参考文本干扰，GRPO 可恢复 15.5% / Inverse scaling in distractor robustness: larger models more vulnerable, GRPO recovers 15.5% |
| [[2605.29601]] | 训练审议式监控器检测 agentic scheming，Qwen3.5-27B 超越 Gemini 2.5 Pro / Training deliberative monitors for scheming detection, Qwen3.5-27B beats Gemini 2.5 Pro |
| [[2605.29629]] | Temporal Logit Observability 解码时序 logit 动态揭示 ASR 无法区分的失败路径差异 / Temporal Logit Observability reveals failure path differences invisible to ASR |
| [[2605.29708]] | MoE 安全行为由少量专家参数控制（0.12%-0.95%），非路由驱动 / MoE safety controlled by few expert params (0.12%-0.95%), not routing-driven |
| [[2605.29737]] | 单字符 prompt 扰动可将 LLM 生成代码从安全翻转为含漏洞 / Single-character prompt mutations flip LLM code from secure to vulnerable |
| [[2605.29816]] | "扰动诱导偏差"是 LLM prompt 鲁棒性下降关键因素，去偏可提供认证保证 / "Perturbation-induced bias" is key factor in LLM prompt fragility, debiasing provides certified guarantees |

### 强化学习后训练 / Reinforcement Learning Post-Training

| Paper | 一句话总结 / One-line Summary |
|-------|-----------------------------|
| [[2605.29782]] | Hista 用隐藏状态 MinDistance 加权估计状态价值，ICML 2026 / Hista uses hidden-state MinDistance for state value estimation, ICML 2026 |
| [[2605.30201]] | HPO 通过滞后权重和批次平均长度归一化修复 GRPO 稀疏奖励问题 / HPO fixes GRPO sparse-reward issues via hysteretic weighting and batch mean-length normalization |
| [[2605.30343]] | RiM 用固定长度 memory blocks 替代自回归推理，延迟与直接回答持平 / RiM replaces autoregressive reasoning with fixed-length memory blocks, same latency as direct answer |

### LoRA 与参数高效微调 / LoRA & Parameter-Efficient Fine-Tuning

| Paper | 一句话总结 / One-line Summary |
|-------|-----------------------------|
| [[2605.29498]] | TMKL 屏蔽真实 token 后对非目标词表做 KL，LoRA 灾难性遗忘降至 1-4% / TMKL masks ground-truth token and applies KL over non-target vocab, LoRA forgetting reduced to 1-4% |
| [[2605.29580]] | LoRA-Curve Bezier 曲线在 LoRA 空间构建连续低损失谷地 / LoRA-Curve Bezier curves build continuous low-loss valleys in LoRA space |
| [[2605.29716]] | NaRA 噪声感知 LoRA 用于扩散语言模型，全局超网络按噪声水平动态生成核心矩阵 / NaRA noise-aware LoRA for diffusion LLMs, global hypernetwork generates core matrix by noise level |
| [[2605.30260]] | LoRA 参数记忆定律 ΔL=C·r^α·ℓ^-β+b，MemFT 达到 100% 精确匹配 / LoRA parametric memory law, MemFT achieves 100% exact match |

### MoE 架构 / Mixture-of-Experts Architecture

| Paper | 一句话总结 / One-line Summary |
|-------|-----------------------------|
| [[2605.29708]] | MoE 安全行为集中在 5-8 个专家中，RASET 仅修改 0.12%-0.95% 参数即达 78.6% ASR / MoE safety concentrated in 5-8 experts, RASET modifies 0.12%-0.95% params for 78.6% ASR |
| [[2605.29714]] | MoE 路由受词汇重叠驱动而非语言家族，SSFT 仅更新 <2% 参数 / MoE routing driven by vocabulary overlap not language family, SSFT updates <2% params |

### LLM 评估与推理 / LLM Evaluation & Inference

| Paper | 一句话总结 / One-line Summary |
|-------|-----------------------------|
| [[2605.29524]] | KBF 利用知识边界数值召回（包括稳定错误值）作为模型指纹，$0.39 全量审计 / KBF uses knowledge-boundary numerical recall as fingerprint, $0.39 full audit |
| [[2605.29979]] | 文本级黑盒推理系统指纹识别（无需 logit），T=0 准确率 100% / Text-only black-box inference system fingerprinting (no logit access), 100% at T=0 |
| [[2605.30315]] | LLM 排行榜统计分辨力诊断，MMLU-Pro 4-6/9 相邻排名对在统计上未分辨 / LLM leaderboard resolution diagnostics, 4-6/9 MMLU-Pro adjacent pairs statistically unresolved |
| [[2605.30335]] | 多组件 LLM 代理"局部一致全局不一致"形式化，33-94% 组合输出违反概率公理 / Multi-component LLM agents "locally coherent globally incoherent" formalized, 33-94% violate probability axioms |
| [[2605.29752]] | GEMM 性能崎岖度分析，相邻尺寸可达 30% 吞吐差异，DP 优化器降低 70% / GEMM performance ruggedness analysis, adjacent sizes vary 30%, DP optimizer reduces roughness 70% |

### 嵌入与架构 / Embedding Methods & Architecture

| Paper | 一句话总结 / One-line Summary |
|-------|-----------------------------|
| [[2605.29459]] | Kronecker Embeddings 用字节级字符-位置分解替代嵌入表，参数减少 91-94% / Kronecker Embeddings replace embedding table with byte-level factorization, 91-94% parameter reduction |
| [[2605.29580]] | LoRA-Curve Bezier 曲线在 LoRA 空间构建连续低损失路径 / LoRA-Curve Bezier curves build continuous low-loss paths in LoRA space |

---

## All Papers

| # | ArXiv ID | Short Title | 中文关键词 / Chinese Keywords | 英文关键词 / English Keywords |
|---|----------|-------------|------------------------------|------------------------------|
| 1 | [[2605.29396]] | Aligned but Fragile | 零阶优化, 安全对齐鲁棒性, 量化鲁棒性 | Zeroth-order optimization, safety alignment robustness, quantization robustness |
| 2 | [[2605.29459]] | Kronecker Embeddings | 字节级嵌入, 参数高效, 拼写鲁棒性 | Byte-level embeddings, parameter-efficient, spelling robustness |
| 3 | [[2605.29491]] | Curse of Helpfulness | 逆缩放定律, 干扰指令鲁棒性, GRPO | Inverse scaling, distractor robustness, GRPO |
| 4 | [[2605.29494]] | Learning to Perturb Gradients | 梯度扰动统一框架, 长尾分类, 噪声标签 | Unified gradient perturbation, long-tail, noisy labels |
| 5 | [[2605.29498]] | Mask the Target (TMKL) | LoRA灾难性遗忘, KL正则化, 无回放 | LoRA forgetting, KL regularization, replay-free |
| 6 | [[2605.29507]] | Xetrieval | 稠密检索机制化解释, TopK-SAE, 推理内化器 | Dense retrieval mechanistic explanation, TopK-SAE, reasoning internalizer |
| 7 | [[2605.29525]] | Learning to Perturb Activations | 隐藏层扰动, 泛化, 域泛化 | Hidden activation perturbation, generalization, domain generalization |
| 8 | [[2605.29537]] | Quantised FNN Verification | 计算复杂度, NP完全, PSPACE完全 | Computational complexity, NP-complete, PSPACE-complete |
| 9 | [[2605.29547]] | S-Adam Optimizer | 非光滑优化, 量化感知训练, Clarke次微分 | Non-smooth optimization, QAT, Clarke subdifferential |
| 10 | [[2605.29548]] | Why Larger Models Learn More | 缩放定律, 多任务学习, 梯度干扰 | Scaling laws, multi-task learning, gradient interference |
| 11 | [[2605.29580]] | LoRA-Curve | 贝叶斯推理, 模式连接, Bezier曲线 | Bayesian inference, mode connectivity, Bezier curves |
| 12 | [[2605.29601]] | Deliberative Monitors | AI安全, scheming检测, 知识蒸馏 | AI safety, scheming detection, knowledge distillation |
| 13 | [[2605.29628]] | COMET | 模态间隙, CLAP嵌入空间, PLS-SVD | Modality gap, CLAP embedding space, PLS-SVD |
| 14 | [[2605.29629]] | Temporal Logit Observability | 解码时序动态, logit分析, 安全评估 | Decoding temporal dynamics, logit analysis, safety evaluation |
| 15 | [[2605.29634]] | Relational Rank Geometry | Plucker坐标, 关系帧, 表示几何 | Plucker coordinates, relation frames, representation geometry |
| 16 | [[2605.29664]] | AMDP | 异步流水线并行, 分布式训练, 收敛保证 | Async pipeline parallelism, distributed training, convergence |
| 17 | [[2605.29700]] | Set Shaping Theory | 哈希表优化, 内存访问, 数据库索引 | Hash table optimization, memory access, database indexing |
| 18 | [[2605.29705]] | BitTP | 1.58-bit量化, 轨迹预测, 边缘部署 | 1.58-bit quantization, trajectory prediction, edge deployment |
| 19 | [[2605.29708]] | MoE Safety Experts | MoE安全, 专家调优, 红队测试 | MoE safety, expert tuning, red-teaming |
| 20 | [[2605.29714]] | MoE Routing for Adaptation | MoE路由动态, 多语言适应, 低资源 | MoE routing dynamics, multilingual adaptation, low-resource |
| 21 | [[2605.29716]] | NaRA | 扩散语言模型, 噪声感知LoRA, 超网络 | Diffusion LLMs, noise-aware LoRA, hypernetwork |
| 22 | [[2605.29737]] | Prompt Fragility in Code | LLM代码安全, 隐藏状态探测, prompt扰动 | LLM code security, hidden-state probing, prompt perturbation |
| 23 | [[2605.29751]] | DySem | 语义相似度, 多语言共识, 注意力输出 | Semantic similarity, multilingual consensus, attention outputs |
| 24 | [[2605.29752]] | GEMM Ruggedness | GEMM性能优化, DP填充, GPU性能分析 | GEMM performance, DP padding, GPU profiling |
| 25 | [[2605.29756]] | LFQ | logit对齐, 最终块量化, 生成质量 | Logit alignment, final-block quantization, generation quality |
| 26 | [[2605.29782]] | Hista | 隐藏状态价值估计, RL信用分配, PPO critic | Hidden-state value estimation, RL credit assignment, PPO critic |
| 27 | [[2605.29816]] | Non-Adversarial Robustness | 扰动诱导偏差, 认证鲁棒性, prompt鲁棒性 | Perturbation-induced bias, certified robustness, prompt robustness |
| 28 | [[2605.29823]] | Polynomial Simplicity | 有效次数, 泛化预测, grokking追踪 | Effective degree, generalization prediction, grokking tracking |
| 29 | [[2605.29843]] | HARP | 自适应旋转, Hadamard替代, 极端量化 | Adaptive rotation, Hadamard replacement, extreme quantization |
| 30 | [[2605.29888]] | LaRA | 数据污染检测, RL后训练, 表征几何 | Data contamination detection, RL post-training, representation geometry |
| 31 | [[2605.29889]] | SAE Clinical Triage | SAE可解释性, 临床分诊, 输出格式偏差 | SAE interpretability, clinical triage, output format bias |
| 32 | [[2605.29901]] | LLM Vulnerability Detection | 机制可解释性, 代码安全, 电路分析 | Mechanistic interpretability, code security, circuit analysis |
| 33 | [[2605.29971]] | Causal Interventions on Verbs | 因果干预, 动词偏好, 结构启动 | Causal intervention, verb bias, structural priming |
| 34 | [[2605.29979]] | Fingerprinting Inference Systems | 推理系统指纹, 数值偏差, 黑盒攻击 | Inference system fingerprinting, numerical deviations, black-box attack |
| 35 | [[2605.30018]] | Latent Performance Profiling | 隐藏状态评估, 不确定性校准, 有效秩 | Hidden-state evaluation, uncertainty calibration, effective rank |
| 36 | [[2605.30022]] | DSTG-NeoBERT | 位置编码解耦, 二维流形塌缩, 注意力头分化 | Positional encoding disentanglement, 2D manifold collapse, head specialization |
| 37 | [[2605.30049]] | SafeDIG | DiT安全干预, SAE, 跨域迁移 | DiT safety intervention, SAE, cross-domain transfer |
| 38 | [[2605.30076]] | UniSteer | 流匹配, 激活空间操控, 文本引导 | Flow matching, activation-space steering, text-guided |
| 39 | [[2605.30161]] | VLM Spatial Representation | 垂直距离纠缠, 空间推理偏差, 合成基准 | Vertical-distance entanglement, spatial reasoning bias, synthetic benchmark |
| 40 | [[2605.30162]] | BioRefusalAudit | SAE生物安全审计, 拒绝深度, 格式敏感性 | SAE biosecurity audit, refusal depth, format sensitivity |
| 41 | [[2605.30201]] | HPO | GRPO改进, 稀疏奖励, 滞后策略优化 | GRPO improvement, sparse rewards, hysteretic policy optimization |
| 42 | [[2605.30218]] | MarginGate | 推理确定性, logit margin, 稀疏验证 | Inference determinism, logit margin, sparse verification |
| 43 | [[2605.30232]] | Functional Welfare Axis | RL表征工程, 福祉轴, 情绪效价 | RL representation engineering, welfare axis, emotion valence |
| 44 | [[2605.30233]] | Entity Tracking in LLMs | 实体追踪, 并行聚合, 全局抑制标签 | Entity tracking, parallel aggregation, global suppression tag |
| 45 | [[2605.30260]] | Parametric Memory Law | LoRA记忆容量, 幂律, 相变 | LoRA memory capacity, power law, phase transition |
| 46 | [[2605.30315]] | Resolution Diagnostics | 假设检验, 排行榜可靠性, 样本量 | Hypothesis testing, leaderboard reliability, sample size |
| 47 | [[2605.30334]] | Data Organization for LLMs | 数据排序, 课程学习, 训练效率 | Data ordering, curriculum learning, training efficiency |
| 48 | [[2605.30335]] | Compositional Incoherence | 多智能体一致性, 概率公理, 几何修复 | Multi-agent coherence, probability axioms, geometric repair |
| 49 | [[2605.30343]] | RiM (Reasoning in Memory) | 潜在推理, 工作记忆, 推理效率 | Latent reasoning, working memory, inference efficiency |
| 50 | [[2605.29524]] | KBF | API审计, 知识边界指纹, 黑盒检测 | API auditing, knowledge boundary fingerprint, black-box detection |

---

> **计数验证 / Count verification:** 目录中实际 .md 文件数（排除 overview.md）= 50，与本文 papers count 一致。
