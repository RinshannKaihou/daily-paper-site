---
title: "Daily arXiv Digest — 2026-06-11"
date: 2026-06-11
papers: 50
tags: ["AI", "Adversarial-Robustness", "Agent-Evaluation", "Alignment", "Circuits", "Continual-Learning", "Ethical-AI", "Federated-Learning", "Grokking", "Interpretability", "KV-Cache", "LLM-Agents", "LoRA", "Multi-Agent", "Neuromorphic", "On-Policy-Distillation", "Optimization", "PAC-Learning", "Pluralism", "Post-Training", "Quantization", "Reasoning", "Reward-Models", "RLHF", "Robustness", "Spiking-NN", "Test-Time-Scaling", "Training-Dynamics", "Weight-Space-Geometry"]
---

# Daily arXiv Digest — 2026-06-11

共筛选 **50** 篇论文 / **50** papers curated from arXiv across cs.LG, cs.CL, cs.AI, cs.CV, cs.PF, cs.AR, stat.ML.

## 今日必读 / Must Read Today

如果只读三篇 / If you only read three papers today:

### 1. [[2606.13603]] Beyond the Commitment Boundary: Probing Epiphenomenal Chain-of-Thought in Large Reasoning Models
- **推荐理由：** 发现大推理模型的思维链中存在"承诺边界"，约一半以上的 CoT 步骤是不改变最终答案的副现象推理；基于隐藏状态训练的探针可在线定位该边界，节省 26–55% 推理 token
- **Why read:** Identifies a sharp "commitment boundary" in LLM CoT after which ~50%+ of reasoning steps are epiphenomenal; lightweight probes enable online early-exiting with 26–55% token savings

### 2. [[2606.12876]] Multi-Bitwidth Quantization for LLMs Using Additive Codebooks (Drop-by-Drop)
- **推荐理由：** 基于信息论逐次求精理论，使单个量化检查点在推理时通过丢弃码本即可在 3-bit 到 5-bit 之间灵活切换，接近单独训练模型的困惑度与准确率
- **Why read:** Grounds multi-bitwidth PTQ in successive-refinement theory; a single checkpoint flexibly switches between 3–5 bit at inference by dropping codebooks, matching individually-tuned models

### 3. [[2606.12921]] LoRA-Muon: Spectral Steepest Descent on the Low-Rank Manifold
- **推荐理由：** 将 Muon 优化器的谱最陡下降推广到低秩流形，实现跨秩、宽度、深度和因子缩放的学习率迁移，rank-32 在 TinyShakespeare 上超过稠密基线
- **Why read:** Extends Muon's spectral steepest-descent to the low-rank manifold with projector-form updates, split weight decay, and gauge invariance; rank-32 beats the dense baseline

## 按主题分类 / Papers by Topic

### Mechanistic Interpretability & Circuits / 机制可解释性与电路（8 篇）

| Paper | Title | 描述 / Description |
|:------|:------|:-------------------|
| [[2606.12818]] | Localizing Anchoring Pathways in Language Models | 利用归因电路定位锚定敏感通路 / Attribution-based circuit localization of anchoring bias in 7B–8B LLMs |
| [[2606.12917]] | Where Computation Lives Inside TabPFN | 首次对 TabPFN 进行因果机制分析 / First causal mechanistic analysis of TabPFN 2.5 attention heads |
| [[2606.12966]] | Circuit Synchronization Precedes Generalization | 傅里叶电路在顿悟前同步 / Fourier circuits synchronize 500–3k steps before grokking |
| [[2606.13209]] | Understanding helpfulness and harmless tension in reward models | 揭示奖励模型中对齐张力的表征重叠 / Overlapping neuronal representations drive helpfulness–harmlessness tension |
| [[2606.13276]] | Different Layers, Different Manifolds | 不同模块应使用不同权重空间几何 / Stiefel for attention + DGram for MLP yields best validation loss |
| [[2606.13603]] | Beyond the Commitment Boundary | 发现 CoT 中的承诺边界与副现象推理 / Commitment boundary and epiphenomenal reasoning in LLM CoT |
| [[2606.13607]] | Reasoning as Pattern Matching | 人类与 LLM 日常推理共享模式匹配机制 / Human and LLM everyday reasoning share pattern-matching mechanisms |
| [[2606.13649]] | Operadic Consistency | 基于 operad 理论的无标签推理失败检测 / Label-free compositional reasoning failure detection via operad theory |

### LLM Reasoning & Post-Training / 大模型推理与后训练（5 篇）

| Paper | Title | 描述 / Description |
|:------|:------|:-------------------|
| [[2606.12935]] | MARS | 边界对抗早停节省 25–47% 推理 token / Margin-adversarial early stopping saves 25–47% self-consistency tokens |
| [[2606.13106]] | SWITCH | 可切换隐藏状态循环推理 / Switchable latent reasoning with learnable boundary tokens |
| [[2606.13125]] | Select and Improve | RL 后训练通过策略选择与改进提升推理 / RL post-training improves reasoning via strategy selection and improvement |
| [[2606.13657]] | Dense Supervision, Sparse Updates | On-policy distillation 产生坐标稀疏更新 / OPD produces coordinate-sparse, spectrally concentrated updates |
| [[2606.13680]] | RA-RFT | 检索增强强化微调提升推理 / Retrieval-augmented RL fine-tuning with reasoning-utility-aware retrieval |

### Quantization & Low-Precision Inference / 量化与低精度推理（4 篇）

| Paper | Title | 描述 / Description |
|:------|:------|:-------------------|
| [[2606.12876]] | Drop-by-Drop | 信息论多比特宽度后训练量化 / Multi-bitwidth PTQ grounded in successive-refinement theory |
| [[2606.13054]] | TWLA | 1.58-bit 三元权重 + 4-bit 激活后训练量化 / W1.58A4 post-training quantization for LLMs |
| [[2606.13233]] | ReSET | 面向 NVFP4 的步感知温度缩放 / Step-aware temperature scaling for NVFP4 reasoning models |
| [[2606.13300]] | TQS | 基于轨迹的时序模型量化敏感度 / Trajectory-based quantization sensitivity for time-series models |

### LLM Alignment & Safety / 大模型对齐与安全（5 篇）

| Paper | Title | 描述 / Description |
|:------|:------|:-------------------|
| [[2606.13104]] | AuthorityBench | 220k 提示证明引用存在即提升幻觉率 / 220k prompts show citation presence raises hallucination rates |
| [[2606.13221]] | Soft-Elo / Conformal Elo | 校准软胜负概率 + 共形预测 Elo 区间 / Calibrated soft win-probability Elo with conformal prediction intervals |
| [[2606.13254]] | Evaluating Pluralism in LLMs | LLM 系统性低估稀有视角 / LLMs systematically underrepresent rare perspectives |
| [[2606.13282]] | ERTS | 22 维伦理后果空间中的对抗稳健性测试 / Adversarial robustness testing in 22D ethical consequence space |
| [[2606.13610]] | FORGE | 单条污染页面即可操纵生成式推荐 / Single polluted page can manipulate generative recommender outputs |

### LLM Inference & Efficiency / 大模型推理与效率（2 篇）

| Paper | Title | 描述 / Description |
|:------|:------|:-------------------|
| [[2606.13097]] | FCGraft | 函数级 KV 缓存拼接与修补 / Function-level KV cache stitching and patching for embodied agents |
| [[2606.13126]] | MiniPIC | 78 行代码实现位置无关缓存 / 78 LOC position-independent KV caching in vLLM |

### Optimization & Training Dynamics / 优化与训练动态（4 篇）

| Paper | Title | 描述 / Description |
|:------|:------|:-------------------|
| [[2606.12921]] | LoRA-Muon | 低秩流形上的谱最陡下降 / Spectral steepest descent on the low-rank manifold |
| [[2606.13287]] | Clipping for Async SGD | 梯度裁剪消除异步 SGD 对最大延迟的依赖 / Gradient clipping removes straggler dependence in async SGD |
| [[2606.13370]] | Training Dynamics in Small Llama | 重复测量实验揭示非单调训练轨迹 / Repeated-measures study reveals non-monotonic training in small LM |
| [[2606.13637]] | Stable Recovery Manifold | 遗忘是流形对齐失败而非信息破坏 / Forgetting is manifold alignment failure, not information destruction |

### Robustness & Adversarial Defense / 鲁棒性与对抗防御（4 篇）

| Paper | Title | 描述 / Description |
|:------|:------|:-------------------|
| [[2606.12896]] | PolicyGuard | 高斯过程逐时间步 RL 后门检测 / GP-based step-level backdoor detection for RL agents |
| [[2606.12930]] | Spurious Correlation Removal | 伪相关去除的计算–统计分离 / Computational–statistical gap in spurious correlation removal |
| [[2606.13092]] | Certified Predictability for Equivariant World Models | 等变世界模型的可认证预测视界 / Certified predictable horizon for equivariant latent world models |
| [[2606.13439]] | S-GBT | 二阶曲率约束的 NLP 认证鲁棒性 / Hessian-bounded certified robustness against word substitution attacks |

### Multi-Agent & Agent Systems / 多智能体与 Agent 系统（6 篇）

| Paper | Title | 描述 / Description |
|:------|:------|:-------------------|
| [[2606.13174]] | TRACE | 将用户纠正编译为运行时强制规则 / Compiling user corrections into runtime enforcement for coding agents |
| [[2606.13591]] | Multiagent Protocols with Aggregated Confidence | 置信度驱动的多智能体聚合协议 / Confidence-driven aggregation protocols for multiagent debate |
| [[2606.13598]] | Orch-RM | 自监督编排层奖励模型 / Self-supervised orchestration-level reward model for multi-agent systems |
| [[2606.13608]] | AgentBeats | Agent 化的 Agent 评估框架 / Agentified agent assessment via A2A/MCP protocols |
| [[2606.13621]] | Shield Synthesis as Defensibility Analysis | 护盾合成作为对抗网络防御性分析 / Shield synthesis as design-time defensibility analysis for adversarial networks |
| [[2606.13681]] | EvoArena | 动态环境中 LLM Agent 记忆演化基准 / Benchmarking memory evolution for LLM agents in dynamic environments |

### ML Theory & Foundations / 机器学习理论与基础（4 篇）

| Paper | Title | 描述 / Description |
|:------|:------|:-------------------|
| [[2606.13172]] | VER | 检测学习表示的解释性不足 / Detecting explanatory insufficiency in learned representations |
| [[2606.13223]] | Distributional Loss | 双峰高斯目标替代 one-hot 的分类损失 / Bimodal Gaussian target replaces one-hot for robust classification |
| [[2606.13576]] | Learning with Simulators | 可模拟过程的在线学习无遗憾保证 / No-regret online learning with access to approximate simulators |
| [[2606.13614]] | Majority-of-Three is Optimal | 三分样本多数投票是最优 PAC 学习器 / Majority vote of three consistent classifiers is an optimal PAC learner |

### Other ML & Applications / 其他机器学习与应用（8 篇）

| Paper | Title | 描述 / Description |
|:------|:------|:-------------------|
| [[2606.12879]] | Diffusion-Network Alignment | 扩散树与相关网络的顶点匹配 / Polynomial-time alignment of diffusion trees to correlated networks |
| [[2606.12925]] | BCP | 贝叶斯条件先验多标签测试时自适应 / Bayesian conditional priors for multi-label test-time adaptation |
| [[2606.13105]] | Disparate Impact in Synthetic Data | 合成数据中的差别影响分析 / Disparate impact analysis in synthetic data generation |
| [[2606.13146]] | Robust Feature-Weighted Jump Models | 稳健特征加权时序聚类 / Robust state-conditional feature-weighted temporal clustering |
| [[2606.13328]] | Dual-Manifold 8-Bit Mapping | 8 位整数双流形神经形态推理 / 8-bit integer dual-manifold neuromorphic inference |
| [[2606.13560]] | ReSCom | 随机计算可重构 SNN 加速器 / Reconfigurable SNN accelerator using stochastic computing |
| [[2606.13589]] | SCSB | 单纯形约束稀疏集成剪枝 / Simplex-constrained sparse bagging for ensemble compression |
| [[2606.13671]] | Truncated Positional Encodings for GNNs | 截断位置编码对 GNN 表达能力的影响 / Truncation breaks expressive-power equivalence of GNN positional encodings |

## All Papers

| # | ID | Title (标题) | Topic (主题) | Score |
|---:|:----|:------------|:-------------|------:|
| 1 | [[2606.12818]] | Localizing Anchoring Pathways in Language Models | Mechanistic Interpretability | 5 |
| 2 | [[2606.12876]] | Multi-Bitwidth Quantization for LLMs Using Additive Codebooks | Quantization | 5 |
| 3 | [[2606.12879]] | Diffusion-Network Alignment | Other ML | 4 |
| 4 | [[2606.12896]] | PolicyGuard: Test-time and Step-level Adversary Defense for RL | Robustness | 4 |
| 5 | [[2606.12917]] | Where Computation Lives Inside TabPFN | Mechanistic Interpretability | 5 |
| 6 | [[2606.12921]] | LoRA-Muon: Spectral Steepest Descent on the Low-Rank Manifold | Optimization | 5 |
| 7 | [[2606.12925]] | Multi-Label Test-Time Adaptation with Bayesian Conditional Priors | Other ML | 4 |
| 8 | [[2606.12930]] | Is Spurious Correlation Removal Always Learnable? | Robustness | 4 |
| 9 | [[2606.12935]] | MARS: Margin-Adversarial Risk-controlled Stopping | LLM Reasoning | 5 |
| 10 | [[2606.12966]] | Circuit Synchronization Precedes Generalization | Mechanistic Interpretability | 5 |
| 11 | [[2606.13054]] | TWLA: Ternary Weights and Low-Bit Activations for LLMs | Quantization | 5 |
| 12 | [[2606.13092]] | Scale Buys Interpolation, Structure Buys a Horizon | Robustness | 4 |
| 13 | [[2606.13097]] | FCGraft: Functional Cache Grafting for Embodied Agents | LLM Inference | 4 |
| 14 | [[2606.13104]] | AuthorityBench: Citation Bias in LLMs | Alignment & Safety | 4 |
| 15 | [[2606.13105]] | Disparate Impact in Synthetic Data Generation | Other ML | 4 |
| 16 | [[2606.13106]] | SWITCH: Switchable Latent Reasoning with On-Policy RL | LLM Reasoning | 5 |
| 17 | [[2606.13125]] | Select and Improve: Mechanics of Post-Training for Reasoning | LLM Reasoning | 5 |
| 18 | [[2606.13126]] | MiniPIC: Flexible Position-Independent Caching in <100LOC | LLM Inference | 4 |
| 19 | [[2606.13146]] | Robust State-Conditional Feature-Weighted Jump Models | Other ML | 4 |
| 20 | [[2606.13172]] | VER: Detecting Explanatory Insufficiency in Representations | ML Theory | 4 |
| 21 | [[2606.13174]] | TRACE: Compiling User Corrections into Runtime Enforcement | Agent Systems | 4 |
| 22 | [[2606.13209]] | Understanding helpfulness and harmless tension in reward models | Mechanistic Interpretability | 5 |
| 23 | [[2606.13221]] | Conformal Elo Estimation for LLM Evaluation | Alignment & Safety | 4 |
| 24 | [[2606.13223]] | Distributional Loss for Robust Classification | ML Theory | 4 |
| 25 | [[2606.13233]] | ReSET: Step-Aware Temperature Scaling for NVFP4 | Quantization | 5 |
| 26 | [[2606.13254]] | Evaluating Pluralism in LLMs through Latent Perspectives | Alignment & Safety | 4 |
| 27 | [[2606.13276]] | Different Layers, Different Manifolds in Transformer Optimization | Mechanistic Interpretability | 5 |
| 28 | [[2606.13282]] | ERTS: Adversarial Robustness Testing of Ethical AI | Alignment & Safety | 4 |
| 29 | [[2606.13287]] | Clipping Makes Async SGD Robust to Stragglers | Optimization | 5 |
| 30 | [[2606.13300]] | TQS: Trajectory-Based Quantization Sensitivity Score | Quantization | 5 |
| 31 | [[2606.13328]] | Non-Parametric Dual-Manifold 8-Bit Mapping | Other ML | 4 |
| 32 | [[2606.13370]] | Training Dynamics in a Small Llama Style LM | Optimization | 5 |
| 33 | [[2606.13439]] | S-GBT: Certified Robustness Against Word Substitution | Robustness | 4 |
| 34 | [[2606.13560]] | ReSCom: Reconfigurable SNN Accelerator via Stochastic Computing | Other ML | 4 |
| 35 | [[2606.13576]] | Learning with Simulators: No Regret in a Bounded World | ML Theory | 4 |
| 36 | [[2606.13589]] | SCSB: Simplex-Constrained Sparse Bagging | Other ML | 4 |
| 37 | [[2606.13591]] | Multiagent Protocols with Aggregated Confidence Signals | Agent Systems | 4 |
| 38 | [[2606.13598]] | Orch-RM: Reward Modeling for Multi-Agent Orchestration | Agent Systems | 4 |
| 39 | [[2606.13603]] | Beyond the Commitment Boundary: Epiphenomenal CoT | Mechanistic Interpretability | 5 |
| 40 | [[2606.13607]] | Reasoning as Pattern Matching in Human and LLM | Mechanistic Interpretability | 5 |
| 41 | [[2606.13608]] | AgentBeats: Agentifying Agent Assessment | Agent Systems | 4 |
| 42 | [[2606.13610]] | FORGE: Web Content Pollution in Generative Recommenders | Alignment & Safety | 4 |
| 43 | [[2606.13614]] | Majority-of-Three is Optimal | ML Theory | 4 |
| 44 | [[2606.13621]] | Shield Synthesis as Defensibility Analysis | Agent Systems | 4 |
| 45 | [[2606.13637]] | Stable Recovery Manifold in Continual Learning | Optimization | 5 |
| 46 | [[2606.13649]] | Operadic Consistency: Compositional Reasoning Failures | Mechanistic Interpretability | 5 |
| 47 | [[2606.13657]] | Dense Supervision, Sparse Updates: On-Policy Distillation | LLM Reasoning | 5 |
| 48 | [[2606.13671]] | Understanding Truncated Positional Encodings for GNNs | Other ML | 4 |
| 49 | [[2606.13680]] | RA-RFT: Retrieval-Augmented Reinforcement Fine-Tuning | LLM Reasoning | 5 |
| 50 | [[2606.13681]] | EvoArena: Memory Evolution for Robust LLM Agents | Agent Systems | 4 |

---
*Generated on 2026-06-11. Total: 50 papers across 10 topics.*
*论文数量验证：目录中有 50 篇 .md 论文文件（不含 overview.md）。匹配：✓*
