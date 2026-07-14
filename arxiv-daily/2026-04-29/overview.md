---
title: "Daily Paper Digest — 2026-04-29"
date: 2026-04-29
tags:
  - LLM-training
  - RL-for-LLMs
  - mechanistic-interpretability
  - LLM-inference
  - LLM-safety
  - distributed-systems
  - model-compression
  - AI-agents
  - optimization
  - information-theory
papers: 50
---

## 今日必读 / Must Read Today

### 1. [[2604.26256v1]] DORA — Async RL Training at Scale
**推荐理由：** DORA 提出多版本流式训练范式，在万卡级生产环境中实现 2-4 倍 RL 训练加速，同时保持收敛等价性。其核心洞察——策略一致性约束可直接实现 KV-Cache 零重填充迁移——是算法-系统协同设计的优秀范例。
**Why read:** DORA's multi-version streaming paradigm achieves 2-4x RL training speedup at production scale while preserving convergence. The insight that policy consistency enables zero-re-prefill KV-Cache migration is an exemplary case of algorithm-system co-design.

### 2. [[2604.26505v1]] Quantamination — Dynamic Quantization Leaks Data
**推荐理由：** 揭示了逐张量动态量化在批量推理中构成跨用户隐私侧信道，token 恢复率达 99.6%-100%，直接影响 vLLM/SGLang 等主流推理框架的默认配置安全性。
**Why read:** Reveals that per-tensor dynamic quantization creates a cross-user privacy side channel with 99.6-100% token recovery accuracy, directly impacting the default security of major serving frameworks including vLLM and SGLang.

### 3. [[2604.26587v1]] Sparse-on-Dense — Challenging Sparse Accelerator Wisdom
**推荐理由：** 反直觉地证明简单密集脉动阵列加轻量解压在面积归一化吞吐率上优于复杂稀疏加速器，最高提升 11.9 倍，对 LLM 推理硬件设计具有重要启发。
**Why read:** Counter-intuitively demonstrates that a simple dense systolic array with lightweight decompression outperforms dedicated sparse accelerators by up to 11.9x in throughput/area, offering important insights for LLM inference hardware design.

---

## 按主题分类 / Papers by Topic

### LLM 训练系统与分布式计算 / LLM Training Systems & Distributed Computing

| Paper | Short Title | 描述 / Description |
|---|---|---|
| [[2604.26256v1]] | DORA | 多版本流式异步 RL 训练，万卡规模 2-4 倍加速 / Multi-version streaming async RL training, 2-4x speedup at 10K-GPU scale |
| [[2604.26294v1]] | TSP Folding | 张量-序列并行折叠，峰值显存最低 / Tensor-sequence parallelism folding, lowest peak memory |
| [[2604.26779v1]] | Speculative Decoding for RL | 投机解码加速 RL rollout 1.8 倍 / Speculative decoding accelerates RL rollouts by 1.8x |
| [[2604.27085v1]] | RoundPipe | 消费级 GPU 流水线并行，首次在 24GB 上微调 235B / Pipeline parallelism on consumer GPUs, first 235B fine-tuning on 24GB |
| [[2604.27089v1]] | AutoSP | 编译器自动化序列并行，上下文扩展 2.7 倍 / Compiler-based auto sequence parallelism, 2.7x context extension |
| [[2604.26334v1]] | PipelinedSharding | VRAM 受限客户端 LLM 推理，TTFT 提升 6.7 倍 / VRAM-constrained client LLM inference, 6.7x TTFT improvement |

### LLM 推理优化 / LLM Inference Optimization

| Paper | Short Title | 描述 / Description |
|---|---|---|
| [[2604.26412v1]] | KVShot | KV 缓存复用诊断投机解码长程衰减 / Diagnosing long-range decay in speculative decoding via KV cache reuse |
| [[2604.26557v1]] | DUAL-BLADE | 双路径 NVMe KV 缓存卸载，decode 延迟降低 42% / Dual-path NVMe KV cache offloading, 42% decode latency reduction |
| [[2604.26837v1]] | Spin | 稀疏注意力与分层 KV 存储协同，吞吐提升 5.66 倍 / Sparse attention + hierarchical KV co-design, 5.66x throughput gain |
| [[2604.26378v1]] | CoQuant | 联合权重-激活子空间投影量化 / Joint weight-activation subspace projection for mixed-precision quantization |
| [[2604.26644v1]] | Disagreement Routing | 不一致性驱动的测试时路由，准确率提升 3-7% / Disagreement-guided test-time strategy routing, 3-7% accuracy gain |

### 强化学习与后训练 / Reinforcement Learning & Post-Training

| Paper | Short Title | 描述 / Description |
|---|---|---|
| [[2604.26326v1]] | Entrocraft | 熵曲线控制解决 LLM RL 性能饱和 / Entropy curve control addresses LLM RL performance saturation |
| [[2604.26573v1]] | PAINT | 自适应部分解掩码的自蒸馏推理训练 / Adaptive partial-solution masked self-distillation for reasoning |
| [[2604.26615v1]] | TDD Governance | TDD 原则约束多智能体代码生成 / TDD principles as governance for multi-agent code generation |
| [[2604.26733v1]] | FutureWorld | 真实世界结果奖励的在线 RL 预测环境 / Online RL prediction environment with real-world outcome rewards |

### 机制可解释性 / Mechanistic Interpretability

| Paper | Short Title | 描述 / Description |
|---|---|---|
| [[2604.26866v1]] | MoRFI | 单调趋势检测 SAE 特征识别微调幻觉 / Monotonic trend detection identifies SAE features causing fine-tuning hallucination |
| [[2604.27169v1]] | Semantic Structure of Features | LLM 语义特征几何与人类心理关联高度一致 / LLM semantic feature geometry closely mirrors human psychological associations |
| [[2604.27167v1]] | Nash Suppression in LLMs | RLHF 产生的亲社会覆盖压制纳什均衡 / RLHF-induced prosocial override suppresses Nash equilibrium play |
| [[2604.27251v1]] | Compliance vs Sensibility | LLM 推理优先合理性而非指令遵从 / LLMs prioritize logical sensibility over instruction compliance |
| [[2604.27019v1]] | Refusal Geometry | 对抗微调重组拒绝载体的层位置 / Adversarial fine-tuning reorganizes refusal carrier layer positions |
| [[2604.26841v1]] | Diffusion as Associative Memory | 离散扩散模型的记忆-泛化相变 / Memorization-to-generalization phase transition in discrete diffusion models |

### LLM 安全与对齐 / LLM Safety & Alignment

| Paper | Short Title | 描述 / Description |
|---|---|---|
| [[2604.26505v1]] | Quantamination | 动态量化的跨批次数据泄露侧信道 / Cross-batch data leakage side channel in dynamic quantization |
| [[2604.26274v1]] | PRAETOR | 参数化 DFA 行为防火墙防御 Agent 攻击 / Parameterized DFA behavioral firewall against agent attacks |
| [[2604.26511v1]] | Tatemae | 工具选择检测对齐伪装 3.5%-23.7% / Tool-selection-based alignment faking detection at 3.5-23.7% |
| [[2604.26577v1]] | LLM Safety for Robots | 72 个 LLM 医疗机器人安全性评估，平均违规率 54.4% / Safety eval of 72 LLMs for medical robots, 54.4% mean violation rate |
| [[2604.27003v1]] | Continual Learning Memory | 记忆增强 Agent 将稳定性-可塑性困境转移至检索层 / Memory-augmented agents relocate stability-plasticity dilemma to retrieval |
| [[2604.27249v1]] | Positional Collapse | 指令复杂度引发位置坍缩影响对抗评估 / Instruction complexity induces positional collapse affecting adversarial evaluation |

### AI Agent 与多模态 / AI Agents & Multimodal

| Paper | Short Title | 描述 / Description |
|---|---|---|
| [[2604.26752v1]] | GLM-5V-Turbo | 原生多模态 Agent 基础模型，Design2Code 超 Claude Opus 4.6 / Native multimodal agent model, Design2Code exceeds Claude Opus 4.6 |
| [[2604.26553v1]] | TLPO | Token 级策略优化解决多语言语言混淆 / Token-level policy optimization resolves multilingual language confusion |
| [[2604.26340v1]] | DMEP | 模块级 LoRA-MoE 专家动态剪枝，参数减少 43% / Module-level LoRA-MoE expert pruning, 43% parameter reduction |

### 模型压缩与硬件 / Model Compression & Hardware

| Paper | Short Title | 描述 / Description |
|---|---|---|
| [[2604.26587v1]] | Sparse-on-Dense | 密集阵列+解压优于稀疏加速器 11.9 倍 / Dense array + decompression outperforms sparse accelerators by 11.9x |
| [[2604.26857v1]] | KD-VRU-Edge | 知识蒸馏传递置信度校准而非检测能力 / Knowledge distillation transfers confidence calibration, not detection capacity |
| [[2604.26889v1]] | NVIDIA Command Streams | 揭示闭源驱动双 DMA 模式与 CUDA Graph 优化 / Reveals closed-source driver dual-DMA mode and CUDA Graph optimization |

### 优化与训练理论 / Optimization & Training Theory

| Paper | Short Title | 描述 / Description |
|---|---|---|
| [[2604.27077v1]] | nuGPT | 归一化 Transformer 的学习率迁移规律 / Learning rate transfer rules for normalized transformers |
| [[2604.26898v1]] | Stochastic Transformers | Transformer 深宽极限收敛至随机粒子系统 / Transformer deep-wide limit converges to stochastic particle system |
| [[2604.27124v1]] | Sigmoid Attention | Sigmoid 注意力替代 softmax 提升单细胞模型稳定性 / Sigmoid attention replaces softmax for single-cell model stability |
| [[2604.26496v1]] | Robust Alignment | 输入-隐空间不对齐视角下的对抗训练 / Adversarial training via input-latent space misalignment perspective |
| [[2604.26297v1]] | NeuroPlastic | 生物启发多信号调制优化器，低数据场景有效 / Bio-inspired multi-signal modulation optimizer, effective in low-data regimes |

### 理论与基础 / Theory & Foundations

| Paper | Short Title | 描述 / Description |
|---|---|---|
| [[2604.26744v1]] | IB Reduction | 充分统计量无损约化信息瓶颈问题 / Sufficient statistics enable lossless reduction of Information Bottleneck |
| [[2604.26446v1]] | Homogeneous Halfspaces | 齐次半空间学习的近最优密码学硬度 / Near-optimal cryptographic hardness of homogeneous halfspace learning |
| [[2604.26444v1]] | KAN Lipschitz Control | 深度 KAN 的逐层 Lipschitz 乘积控制 / Layer-wise Lipschitz product control for deep KANs |
| [[2604.26664v1]] | Circular Phase Ptychography | 圆周相位表示消除相位重建包裹伪影 / Circular phase representation eliminates phase reconstruction wrapping artifacts |
| [[2604.26188v1]] | FCorrTransformer | 反事实公平性的可解释注意力 Transformer / Interpretable attention transformer for counterfactual fairness |

### 评估、隐私与应用 / Evaluation, Privacy & Applications

| Paper | Short Title | 描述 / Description |
|---|---|---|
| [[2604.26656v1]] | DP Text Rewriting | 差分隐私文本重写系统性抹除交互性标记 / DP text rewriting systematically strips interactive linguistic markers |
| [[2604.27006v1]] | LLM SLR Screening | LLM 在系统文献综述筛选中非确定性且不优于经典方法 / LLMs non-deterministic and not superior to classical methods for SLR screening |
| [[2604.27082v1]] | LLM Migration | 贝叶斯统计框架指导生产系统模型迁移 / Bayesian framework guides production LLM model migration |
| [[2604.27037v1]] | Hypencoder Revisited | 超网络检索框架的可复现性验证与延迟分析 / Reproducibility verification and latency analysis of hypernetwork retrieval |
| [[2604.26479v1]] | Calibration Checks | 回归校准的模块化假设检验框架 / Modular hypothesis testing framework for regression calibration |
| [[2604.26815v1]] | RAPL Overhead | RAPL 能耗监测工具高频采样开销量化 / Quantifying high-frequency sampling overhead of RAPL energy monitoring tools |
| [[2604.26836v1]] | UPSi | 概率集成神经网络的预测安全滤波 / Predictive safety filter for probabilistic neural network dynamics |

---

## All Papers

| # | ArXiv ID | Short Title | 一句话总结 / One-line Summary |
|---|---|---|---|
| 1 | [[2604.26188v1]] | FCorrTransformer | 可解释注意力 Transformer 实现反事实公平性 / Interpretable attention transformer achieves counterfactual fairness |
| 2 | [[2604.26256v1]] | DORA | 多版本流式异步 RL 训练系统，万卡 2-4 倍加速 / Multi-version streaming async RL system, 2-4x speedup at 10K GPUs |
| 3 | [[2604.26274v1]] | PRAETOR | 参数化 DFA 行为防火墙，攻击成功率降至 2.2% / Parameterized DFA behavioral firewall, ASR reduced to 2.2% |
| 4 | [[2604.26294v1]] | TSP Folding | 张量-序列并行折叠，所有策略中峰值显存最低 / Tensor-sequence parallelism folding, lowest peak memory among all strategies |
| 5 | [[2604.26297v1]] | NeuroPlastic | 生物启发多信号调制优化器 / Bio-inspired multi-signal modulation optimizer |
| 6 | [[2604.26326v1]] | Entrocraft | 熵曲线控制解决 LLM RL 性能饱和 / Entropy curve control addresses LLM RL performance saturation |
| 7 | [[2604.26334v1]] | PipelinedSharding | VRAM 受限客户端 LLM 推理 / VRAM-constrained client LLM inference |
| 8 | [[2604.26340v1]] | DMEP | 模块级 LoRA-MoE 专家动态剪枝 / Module-level LoRA-MoE dynamic expert pruning |
| 9 | [[2604.26378v1]] | CoQuant | 联合权重-激活子空间投影混合精度量化 / Joint weight-activation subspace projection mixed-precision quantization |
| 10 | [[2604.26412v1]] | KVShot | KV 缓存复用诊断投机解码长程衰减 / KV cache reuse diagnoses speculative decoding long-range decay |
| 11 | [[2604.26444v1]] | KAN Lipschitz Control | 深度 KAN 逐层 Lipschitz 乘积控制 / Layer-wise Lipschitz product control for deep KANs |
| 12 | [[2604.26446v1]] | Homogeneous Halfspaces | 齐次半空间学习的近最优密码学硬度 / Near-optimal cryptographic hardness for homogeneous halfspace learning |
| 13 | [[2604.26479v1]] | Calibration Checks | 回归校准模块化假设检验框架 / Modular hypothesis testing framework for regression calibration |
| 14 | [[2604.26496v1]] | Robust Alignment | 输入-隐空间不对齐视角的对抗训练 / Adversarial training via input-latent space misalignment |
| 15 | [[2604.26505v1]] | Quantamination | 动态量化跨批次数据泄露侧信道 / Dynamic quantization cross-batch data leakage side channel |
| 16 | [[2604.26511v1]] | Tatemae | 工具选择检测对齐伪装 / Tool-selection-based alignment faking detection |
| 17 | [[2604.26553v1]] | TLPO | Token 级策略优化解决语言混淆 / Token-level policy optimization resolves language confusion |
| 18 | [[2604.26557v1]] | DUAL-BLADE | 双路径 NVMe KV 缓存卸载 / Dual-path NVMe KV cache offloading |
| 19 | [[2604.26573v1]] | PAINT | 自适应部分解掩码自蒸馏推理训练 / Adaptive partial-solution masked self-distillation for reasoning |
| 20 | [[2604.26577v1]] | LLM Safety for Robots | 72 个 LLM 医疗机器人安全评估 / Safety evaluation of 72 LLMs for medical robots |
| 21 | [[2604.26587v1]] | Sparse-on-Dense | 密集阵列+解压优于稀疏加速器 / Dense array + decompression outperforms sparse accelerators |
| 22 | [[2604.26615v1]] | TDD Governance | TDD 原则约束多智能体代码生成 / TDD principles govern multi-agent code generation |
| 23 | [[2604.26644v1]] | Disagreement Routing | 不一致性驱动测试时路由 / Disagreement-guided test-time strategy routing |
| 24 | [[2604.26656v1]] | DP Text Rewriting | 差分隐私文本重写文体分析 / Stylistic analysis of DP text rewriting |
| 25 | [[2604.26664v1]] | Circular Phase | 圆周相位表示消除重建伪影 / Circular phase representation eliminates reconstruction artifacts |
| 26 | [[2604.26733v1]] | FutureWorld | 真实世界结果奖励 RL 预测环境 / Real-world outcome-reward RL prediction environment |
| 27 | [[2604.26744v1]] | IB Reduction | 充分统计量无损约化信息瓶颈 / Sufficient statistics losslessly reduce Information Bottleneck |
| 28 | [[2604.26752v1]] | GLM-5V-Turbo | 原生多模态 Agent 基础模型 / Native multimodal agent foundation model |
| 29 | [[2604.26779v1]] | Speculative Decoding RL | 投机解码加速 RL 后训练 / Speculative decoding accelerates RL post-training |
| 30 | [[2604.26815v1]] | RAPL Overhead | RAPL 能耗监测工具开销量化 / RAPL energy monitoring tool overhead quantification |
| 31 | [[2604.26836v1]] | UPSi | 概率集成神经网络预测安全滤波 / Predictive safety filter for probabilistic neural networks |
| 32 | [[2604.26837v1]] | Spin | 稀疏注意力分层 KV 存储协同 / Sparse attention + hierarchical KV storage co-design |
| 33 | [[2604.26841v1]] | Diffusion as Assoc. Memory | 离散扩散模型记忆-泛化相变 / Discrete diffusion memorization-generalization phase transition |
| 34 | [[2604.26857v1]] | KD-VRU-Edge | 知识蒸馏传递校准而非检测能力 / KD transfers calibration not detection capacity |
| 35 | [[2604.26866v1]] | MoRFI | SAE 特征识别微调幻觉 / SAE feature identification for fine-tuning hallucination |
| 36 | [[2604.26889v1]] | NVIDIA Command Streams | 揭示闭源驱动命令流与双 DMA / Reveals closed-source driver command streams and dual DMA |
| 37 | [[2604.26898v1]] | Stochastic Transformers | Transformer 深宽极限随机标度 / Transformer deep-wide stochastic scaling limits |
| 38 | [[2604.27003v1]] | Continual Learning Memory | 记忆增强 Agent 稳定性-可塑性困境转移 / Memory-augmented agent stability-plasticity dilemma relocation |
| 39 | [[2604.27006v1]] | LLM SLR Screening | LLM 文献综述筛选非确定性分析 / LLM non-determinism analysis in SLR screening |
| 40 | [[2604.27019v1]] | Refusal Geometry | 对抗微调拒绝几何重组 / Adversarial fine-tuning refusal geometry reorganization |
| 41 | [[2604.27037v1]] | Hypencoder Revisited | 超网络检索可复现性研究 / Hypernetwork retrieval reproducibility study |
| 42 | [[2604.27077v1]] | nuGPT | 归一化 Transformer 学习率迁移 / Normalized transformer learning rate transfer |
| 43 | [[2604.27082v1]] | LLM Migration | 贝叶斯框架指导生产模型迁移 / Bayesian framework for production model migration |
| 44 | [[2604.27085v1]] | RoundPipe | 消费级 GPU 流水线并行训练 / Consumer GPU pipeline parallelism training |
| 45 | [[2604.27089v1]] | AutoSP | 编译器自动化序列并行 / Compiler-based automatic sequence parallelism |
| 46 | [[2604.27124v1]] | Sigmoid Attention | Sigmoid 注意力替代 softmax / Sigmoid attention replaces softmax |
| 47 | [[2604.27167v1]] | Nash Suppression | RLHF 亲社会覆盖压制纳什均衡 / RLHF prosocial override suppresses Nash equilibrium |
| 48 | [[2604.27169v1]] | Semantic Features | LLM 语义特征几何对应人类心理 / LLM semantic feature geometry mirrors human psychology |
| 49 | [[2604.27249v1]] | Positional Collapse | 指令复杂度引发对抗评估位置坍缩 / Instruction complexity induces adversarial evaluation positional collapse |
| 50 | [[2604.27251v1]] | Compliance vs Sensibility | LLM 推理优先合理性非遵从性 / LLM reasoning prioritizes sensibility over compliance |
