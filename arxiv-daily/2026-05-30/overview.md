---
title: "Daily Paper Digest — 2026-05-30"
date: 2026-05-30
tags:
  - llm
  - agent
  - safety
  - theory
  - optimization
  - retrieval
  - privacy
  - diffusion
  - federated-learning
  - causal-inference
  - calibration
  - interpretability
papers: 50
---

## 今日必读 / Must Read Today

1. **[[2605.29729]] Realistic Honeypot Evaluations for Scheming Propensity** — 在 Google 内部对齐研究代码库中设置真实破坏机会检测模型欺骗倾向 / Introduces honeypot-based evaluation of AI scheming propensity inside Google's real alignment research codebases, finding no unprompted scheming in current Gemini models. （AI安全与对齐 / AI Safety & Alignment）

2. **[[2605.30040]] Token Inflation** — 揭示 LLM 按 token 计费中的"信任悖论"并攻击三种审计框架 / Formalizes the "trust paradox" in LLM per-token billing and demonstrates attacks on three auditing frameworks achieving up to 1,469% token inflation. （LLM 安全与经济学 / LLM Security & Economics）

3. **[[2605.29847]] EvoRubric** — 让 LLM 自演化评分规则实现开放式生成任务的对齐，8B 模型超越 GPT-4o / Proposes self-evolving rubric-driven RL where an 8B open-source model surpasses GPT-4o on medical, writing, and science benchmarks. （LLM 对齐 / LLM Alignment）

## 按主题分类 / Papers by Topic

### 大语言模型推理与效率 / LLM Inference & Efficiency

| Paper | Short Title | Summary / 摘要 |
|-------|-------------|-----------------|
| [[2605.29707]] | Domino | 解耦因果建模与自回归草稿的推测解码 / Decouples causal modeling from autoregressive drafting in speculative decoding, achieving up to 5.49x speedup on Qwen3 |
| [[2605.30103]] | LLM-NAS Convergence Theory | 首次为迭代 LLM-NAS 建立收敛理论 / Establishes the first formal convergence theory for iterative LLM-based neural architecture search |
| [[2605.30202]] | Dual-Path LLM | 双路径 Transformer 块平衡计算与容量缩放 / Proposes a dual-path Transformer block balancing compute and capacity scaling with learnable per-token gating |

### AI 安全与对齐 / AI Safety & Alignment

| Paper | Short Title | Summary / 摘要 |
|-------|-------------|-----------------|
| [[2605.29729]] | Scheming Honeypot | 蜜罐评估框架检测 AI 欺骗倾向 / Honeypot evaluation framework detecting AI scheming propensity in real codebases |
| [[2605.30322]] | Gram | 自动化对齐审计评估蓄意破坏倾向 / Automated alignment auditing framework for sabotage propensity evaluation |
| [[2605.30040]] | Token Inflation | LLM 按 token 计费的信任悖论与攻击 / Trust paradox and attacks in LLM per-token billing systems |
| [[2605.29801]] | AgentDoG 1.5 | 轻量级 AI Agent 安全护栏模型 / Lightweight AI agent safety guardrail models trained on ~1k samples |
| [[2605.30096]] | LLM Pentesting | 400 次渗透测试的 LLM 攻击一致性研究 / 400-run empirical study of LLM penetration testing consistency |
| [[2605.29667]] | ChiSafe-PAS | 中文 LLM 安全对抗性提示词基准 / Chinese adversarial prompt benchmark for LLM safety evaluation |

### LLM 评估与基准 / LLM Evaluation & Benchmarks

| Paper | Short Title | Summary / 摘要 |
|-------|-------------|-----------------|
| [[2605.29395]] | Low Rank for Rank | 低秩矩阵建模的任务级 LLM 排名推断 / Low-rank matrix modeling for task-level LLM ranking with uncertainty quantification |
| [[2605.30329]] | SoundnessBench | 测试 LLM 能否判断研究方案合理性的基准 / Benchmark testing whether LLMs can judge methodological soundness of research proposals |
| [[2605.30348]] | LLMSurgeon | 逆向推断 LLM 预训练数据混合比例 / Estimating LLM pretraining data mixture proportions from generated text |
| [[2605.29586]] | FinVerBench | LLM 财务报表验证基准 / Benchmark for evaluating LLM financial statement verification capabilities |
| [[2605.29682]] | Agent Scaling Laws | 智能体框架的有效反馈计算量缩放定律 / Effective Feedback Compute as a scaling coordinate for agent harnesses |
| [[2605.30219]] | Belief Management | LLM 多轮交互中的情境信念管理 / Contextual Belief Management in multi-turn LLM interactions |

### LLM 训练与微调 / LLM Training & Fine-tuning

| Paper | Short Title | Summary / 摘要 |
|-------|-------------|-----------------|
| [[2605.29847]] | EvoRubric | 自演化评分规则的 RL 对齐 / Self-evolving rubric-driven RL for open-ended generation alignment |
| [[2605.30148]] | AWD for ES | 进化策略微调中的锚定权重衰减 / Anchored Weight Decay for mitigating forgetting in ES fine-tuning |
| [[2605.30290]] | STV | 自训练验证器的推理与训练时自改进 / Self-Trained Verification for both test-time and training-time self-improvement |
| [[2605.30288]] | MIRA | 中间训练阶段的源自适应数据选择 / Source-aware data selection for LLM mid-training via rubric discovery |
| [[2605.30154]] | RL2ML | RLVR 训练中的连续代理目标族 / Continuous family of surrogate objectives for RLVR training |
| [[2605.29678]] | Spurious Prompts | 无关提示词可系统操控 LLM 行为 / Task-irrelevant "spurious prompts" can systematically steer LLM behavior |

### 信息检索与 RAG / Information Retrieval & RAG

| Paper | Short Title | Summary / 摘要 |
|-------|-------------|-----------------|
| [[2605.29384]] | Latent Terms | SAE 从稠密检索器提取 BM25 可用稀疏词表 / Extracts BM25-ready sparse vocabularies from dense retrievers via SAEs |
| [[2605.30029]] | RAISE | RAG 系统设计建模为架构搜索 / Formulates RAG pipeline design as an architecture search problem |

### 智能体系统 / Agent Systems

| Paper | Short Title | Summary / 摘要 |
|-------|-------------|-----------------|
| [[2605.29668]] | GRASP | 回归感知门控的 LLM Agent 技能库自改进 / Regression-aware gated skill library for self-improving LLM agents |
| [[2605.29786]] | Croissant Tasks | ML 基准评测的声明式元数据格式 / Declarative metadata format for reproducible ML benchmark evaluations |

### 隐私与联邦学习 / Privacy & Federated Learning

| Paper | Short Title | Summary / 摘要 |
|-------|-------------|-----------------|
| [[2605.29454]] | MIA Framework | 全流水线成员推理攻击评估框架 / Full-pipeline framework for evaluating Membership Inference Attacks |
| [[2605.29460]] | FedSmoothLoRA | 联邦 LoRA 微调的跨轮次状态连续性 / Smoother convergence in federated LoRA via Round-Matching and Gradient-Aligned matrices |
| [[2605.30123]] | xMK-CKKS OTA | 多密钥同态加密的无线联邦学习 / Multi-key homomorphic encryption for wireless federated learning |
| [[2605.30075]] | Q-ANCHOR | 量子联邦学习的零噪声外推纠偏 / ZNE-guided correction for quantum federated learning |

### 知识蒸馏与模型压缩 / Knowledge Distillation & Model Compression

| Paper | Short Title | Summary / 摘要 |
|-------|-------------|-----------------|
| [[2605.29726]] | SLAD | 师生共享 LoRA 适配器的任务蒸馏 / Shared LoRA Adapters for task-specific knowledge distillation between ViTs |
| [[2605.29994]] | Precomputed 1D-CNNs | 1D-CNN 预计算为 FPGA 查找表实现超低功耗推理 / Precomputes 1D-CNN as FPGA LUTs for ultra-low-power ECG analysis |

### 理论与优化 / Theory & Optimization

| Paper | Short Title | Summary / 摘要 |
|-------|-------------|-----------------|
| [[2605.29645]] | Sparse Bandits | 稀疏上下文赌博机的最优样本复杂度 / Tight sample complexity bounds for sparse contextual bandits |
| [[2605.29497]] | Convex Basins SIM | 非单调链接函数单指标模型的凸盆地与鲁棒恢复 / Convex basin analysis for robust recovery of Single Index Models |
| [[2605.29819]] | Interpolation Aggregation | 三插值器中位数达最优回归样本复杂度 / Median-of-three interpolators achieves optimal regression sample complexity |
| [[2605.29669]] | Eigen-Spike CK | 非线性可分数据下共轭核的特征尖峰涌现 / Eigen-spike emergence in conjugate kernels on nonlinearly separable data |
| [[2605.29788]] | Nested Causal Bandits | 嵌套因果赌博机的 PAC-Bayes 安全部署认证 / PAC-Bayes certified policy optimization for nested causal bandits |
| [[2605.29908]] | Joint ARD | 模型与数据联合稀疏化的贝叶斯学习 / Joint model and data sparsification via marginal likelihood |
| [[2605.30153]] | Diffusion Optimal | 扩散模型对低维多模态分布的极小极大最优性 / Proves diffusion models are statistically optimal for learning low-dimensional multi-modal distributions |
| [[2605.30253]] | Wasserstein CAVI | 坐标上升变分推断的 Wasserstein 收缩 / Wasserstein contraction for Coordinate Ascent Variational Inference |

### 多智能体系统与扩散 / Multi-Agent & Diffusion

| Paper | Short Title | Summary / 摘要 |
|-------|-------------|-----------------|
| [[2605.30190]] | MF-Diffuser | 均值场扩散规划扩展至数千智能体 / Mean-field diffusion planning scaled to thousands of agents |
| [[2605.30330]] | Posterior Sampler Failures | 扩散后验采样器失败机制的有限样本分析 / Finite-sample analysis of why diffusion posterior samplers fail |

### 架构设计与动态路由 / Architecture Design & Dynamic Routing

| Paper | Short Title | Summary / 摘要 |
|-------|-------------|-----------------|
| [[2605.30229]] | Anti Mode-Collapse | RoPE 与前缀 token 防止均场 Transformer 模式坍缩 / Proves positional encoding and prompt tokens prevent mode collapse in mean-field transformers |

### 因果推断 / Causal Inference

| Paper | Short Title | Summary / 摘要 |
|-------|-------------|-----------------|
| [[2605.30015]] | TTT-SCL | 测试时训练实现鲁棒因果发现 / Test-time training for robust causal discovery under distribution shift |
| [[2605.30319]] | HTE Matrix Completion | 异质性处理效应估计的行级矩阵补全 / Row-wise matrix completion for heterogeneous treatment effect estimation |

### 可解释性与校准 / Interpretability & Calibration

| Paper | Short Title | Summary / 摘要 |
|-------|-------------|-----------------|
| [[2605.29836]] | CB-SLICE | 基于概念瓶颈模型的错误切片发现 / Error slice discovery via Concept Bottleneck Models |
| [[2605.30188]] | CalArena | 大规模后校准基准评测 / Large-scale post-hoc calibration benchmark with ~2000 experiments |
| [[2605.30292]] | LWO Jackknife | 时间序列预测推断的留窗法 / Leave-a-Window-Out jackknife for time series predictive inference |

### 多语言与跨语言 NLP / Multilingual & Cross-lingual NLP

| Paper | Short Title | Summary / 摘要 |
|-------|-------------|-----------------|
| [[2605.29637]] | IndicKLAR | 印度语言的跨语言知识一致性基准 / Cross-lingual knowledge consistency benchmark for 18 Indian languages |

### 视觉语言模型 / Vision-Language Models

| Paper | Short Title | Summary / 摘要 |
|-------|-------------|-----------------|
| [[2605.29881]] | BRACS | 推理时引导缓解视觉语言模型幻觉 / Inference-time steering to mitigate VLM hallucination via attention grounding barrier |

### 高性能计算 / High-Performance Computing

| Paper | Short Title | Summary / 摘要 |
|-------|-------------|-----------------|
| [[2605.29604]] | TC-MIS | Tensor Core 加速图最大独立集算法 / Accelerates Maximum Independent Set on GPU Tensor Cores via SpMV reformulation |

### RAG 系统优化 / RAG System Optimization

| Paper | Short Title | Summary / 摘要 |
|-------|-------------|-----------------|
| [[2605.30029]] | RAISE | RAG 设计作为架构搜索问题 / RAG pipeline design as black-box architecture search across 13 optimizers and 7 datasets |

## All Papers

| # | arXiv ID | Short Title | 中文关键词 |
|---|----------|-------------|-----------|
| 1 | [[2605.29384]] | Latent Terms | 稠密检索 / SAE / BM25 / 信息检索 |
| 2 | [[2605.29395]] | Low Rank for Rank | LLM 评估 / 低秩矩阵 / 不确定性量化 |
| 3 | [[2605.29454]] | MIA Framework | 成员推理 / 隐私审计 / 机器遗忘 |
| 4 | [[2605.29460]] | FedSmoothLoRA | 联邦学习 / LoRA / 参数高效微调 |
| 5 | [[2605.29497]] | Convex Basins SIM | 单指标模型 / 鲁棒统计 / 优化景观 |
| 6 | [[2605.29586]] | FinVerBench | LLM 评估 / 财务验证 / 校准 |
| 7 | [[2605.29604]] | TC-MIS | GPU 计算 / 图算法 / Tensor Core |
| 8 | [[2605.29637]] | IndicKLAR | 跨语言一致性 / 印度语言 / 多语言 LLM |
| 9 | [[2605.29645]] | Sparse Bandits | 上下文赌博机 / 样本复杂度 / 多类别 |
| 10 | [[2605.29667]] | ChiSafe-PAS | LLM 安全 / 中文 NLP / 对抗评估 |
| 11 | [[2605.29668]] | GRASP | LLM Agent / 自改进 / 技能库 |
| 12 | [[2605.29669]] | Eigen-Spike CK | 随机矩阵 / 共轭核 / 相变 |
| 13 | [[2605.29678]] | Spurious Prompts | 提示工程 / LLM 鲁棒性 / 提示敏感性 |
| 14 | [[2605.29682]] | Agent Scaling Laws | Agent 缩放定律 / 测试时计算 / 反馈质量 |
| 15 | [[2605.29707]] | Domino | 推测解码 / LLM 推理 / 因果建模 |
| 16 | [[2605.29726]] | SLAD | 知识蒸馏 / LoRA / 视觉 Transformer |
| 17 | [[2605.29729]] | Scheming Honeypot | AI 安全 / 欺骗评估 / 蜜罐 |
| 18 | [[2605.29786]] | Croissant Tasks | 可复现性 / 元数据格式 / LLM Agent |
| 19 | [[2605.29788]] | Nested Causal Bandits | 因果赌博机 / PAC-Bayes / 安全部署 |
| 20 | [[2605.29801]] | AgentDoG 1.5 | Agent 安全 / AI 对齐 / 护栏模型 |
| 21 | [[2605.29819]] | Interpolation Aggregation | 学习理论 / 回归 / 样本复杂度 |
| 22 | [[2605.29836]] | CB-SLICE | 可解释性 / 概念瓶颈模型 / 错误切片 |
| 23 | [[2605.29847]] | EvoRubric | 强化学习 / LLM 对齐 / 自演化评分 |
| 24 | [[2605.29881]] | BRACS | VLM 幻觉 / 推理时引导 / 注意力接地 |
| 25 | [[2605.29908]] | Joint ARD | 稀疏贝叶斯学习 / 鲁棒回归 / 边缘似然 |
| 26 | [[2605.29994]] | Precomputed 1D-CNNs | FPGA / LUT 预计算 / 边缘 ML |
| 27 | [[2605.30015]] | TTT-SCL | 因果发现 / 测试时训练 / 分布偏移 |
| 28 | [[2605.30029]] | RAISE | RAG / 超参数优化 / 架构搜索 |
| 29 | [[2605.30040]] | Token Inflation | LLM 安全 / Token 计费 / 审计 |
| 30 | [[2605.30075]] | Q-ANCHOR | 量子联邦学习 / 误差缓解 / 分布式优化 |
| 31 | [[2605.30096]] | LLM Pentesting | LLM 安全 / 渗透测试 / 实证研究 |
| 32 | [[2605.30103]] | LLM-NAS Convergence | 神经架构搜索 / LLM 理论 / 收敛分析 |
| 33 | [[2605.30123]] | xMK-CKKS OTA | 联邦学习 / 同态加密 / 无线通信 |
| 34 | [[2605.30148]] | AWD for ES | 进化策略 / 持续学习 / LLM 微调 |
| 35 | [[2605.30153]] | Diffusion Optimal | 扩散模型 / 统计理论 / 样本复杂度 |
| 36 | [[2605.30154]] | RL2ML | RLVR / 强化学习 / 代理目标 |
| 37 | [[2605.30188]] | CalArena | 校准 / 基准 / 后校准 |
| 38 | [[2605.30190]] | MF-Diffuser | 离线 RL / 均值场 / 多智能体 |
| 39 | [[2605.30202]] | Dual-Path LLM | 循环 Transformer / 计算缩放 / 自适应路由 |
| 40 | [[2605.30219]] | Belief Management | 信念追踪 / 强化学习 / LLM 评估 |
| 41 | [[2605.30229]] | Anti Mode-Collapse | 均场理论 / Transformer / 模式坍缩 |
| 42 | [[2605.30253]] | Wasserstein CAVI | 变分推断 / Wasserstein 距离 / 收敛分析 |
| 43 | [[2605.30288]] | MIRA | 数据选择 / 中间训练 / 规则发现 |
| 44 | [[2605.30290]] | STV | 自改进 / 验证器 / 推理时计算 |
| 45 | [[2605.30292]] | LWO Jackknife | 保形预测 / 时间序列 / 预测推断 |
| 46 | [[2605.30319]] | HTE Matrix Completion | 因果推断 / 矩阵补全 / 异质性处理效应 |
| 47 | [[2605.30322]] | Gram | AI 对齐 / AI 安全 / 自动化审计 |
| 48 | [[2605.30329]] | SoundnessBench | AI Scientist / LLM 评估 / 同行评审 |
| 49 | [[2605.30330]] | Posterior Sampler Failures | 扩散模型 / 后验采样 / 逆问题 |
| 50 | [[2605.30348]] | LLMSurgeon | LLM 可解释性 / 数据混合估计 / 逆问题 |

---

*Generated on 2026-06-01. Paper count: 50 papers in directory, 50 papers in overview. Counts match.*
