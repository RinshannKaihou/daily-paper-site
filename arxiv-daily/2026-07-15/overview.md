---
title: "Daily Paper Overview — 2026-07-15"
date: 2026-07-15
tags:
  - daily-paper
  - mechanistic-interpretability
  - llm-agents
  - rlvr
  - efficiency
  - evaluation
  - safety
papers: 41
---

> 本日共收录 41 篇论文，涵盖机制可解释性、RL/RLVR、智能体、效率与量化、学习理论、评测、安全等方向。
> 41 papers today, spanning mechanistic interpretability, RL/RLVR, agents, efficiency/quantization, learning theory, evaluation, and safety.

## 今日必读 / Must Read Today

1. **[[2607.12640]] A Learning-Rate-Gated Failure of GRPO in a Small Web Agent**
   - 理由：以罕见的统计严谨性（配对 McNemar + 任务聚类自助法 + TOST 等价检验 + 多种子复现）给出了 GRPO 在已掌握任务上的受控零结果，并用权重嫁接因果定位损伤到 attention/MLP 块，同时提出零成本预筛器 Δhead。是 RLVR「锐化还是增益能力」之争在交互式智能体上的高质量负结果研究。
   - Reason: A controlled null of GRPO on mastered web-agent tasks with rare statistical rigor (paired McNemar, task-clustered bootstrap, TOST equivalence, multi-seed replication), plus a causal weight-grafting mechanism localizing damage to attention/MLP blocks and a free Δhead pre-screen. A high-quality negative result for the sharpening-vs-gain debate in RLVR agents.

2. **[[2607.12550]] JoLT: Near-Lossless KV Cache Compression via Joint Tucker and JL-Residual Allocation**
   - 理由：把 KV cache 视为三阶张量，谱分析证明 head/layer 轴不可压缩、K/V 不对称，仅压缩 token/feature 轴 + JL 旋转残差 + 单一 Lagrangian 对偶联合分配秩与比特，在 2–3× 区间达到比 int4/xKV 低约一个数量级的重建误差。方法优雅、理论扎实、工程意义明确。
   - Reason: Treats the KV cache as a 3rd-order tensor, spectral analysis shows head/layer axes are incompressible and K/V are asymmetric; a partial Tucker + JL-rotated residual + single Lagrangian dual jointly allocating ranks and bits achieves ~order-of-magnitude lower reconstruction error than int4/xKV in the 2–3× zone. Elegant, principled, and practically meaningful.

3. **[[2607.12985]] Resist and Update: Counterfactual Report Coordinates for Incentive-Compatible LLMs**
   - 理由：将「压力下误报」重新框架为内部激励兼容性失效，提出 (resist, update) 双重控制评估轴取代标量奉承率，用交换干预因果识别出低秩、近正交的答案/置信度/保留意见报告坐标，并提出无训练 CRC 钳制在构造基准上达到 1.00/1.00。机制分析与评估范式都有实质创新。
   - Reason: Reframes pressured misreporting as internal incentive-compatibility failure, introduces the (resist, update) dual-control axis replacing a scalar sycophancy rate, causally identifies low-rank near-orthogonal answer/confidence/caveat report coordinates via interchange interventions, and proposes a training-free CRC clamp reaching 1.00/1.00 on a constructed benchmark. Substantive novelty in both mechanism and evaluation.

## 按主题分类 / Papers by Topic

### 机制可解释性 / Mechanistic Interpretability

| Paper | Short Title | Description |
|-------|-------------|-------------|
| [[2603.06592]] | Hierarchical Latent Structures | 用层次化潜在结构统一多种机制现象 / Unifies diverse mechanistic phenomena via hierarchical latent structures |
| [[2605.05686]] | Attractor Geometry of Transformer Memory | 用吸引子几何刻画 Transformer 记忆与幻觉 / Characterizes transformer memory and hallucination via attractor geometry |
| [[2606.27321]] | Sparsity Regularizers for Top-k SAEs | 系统评估 top-k SAE 的稀疏正则化选择 / Systematically evaluates sparsity regularizers for top-k SAEs |
| [[2607.11990]] | Sparse Inter-Layer FFN Dependencies | 揭示 FFN 神经元跨层的稀疏依赖结构 / Reveals sparse inter-layer dependency structure of FFN neurons |
| [[2607.12166]] | SAE Causal Audit: Superposition→Monosemanticity | 用 SAE 因果审计追踪叠加到单语义的演化 / Uses SAE causal audits to trace superposition-to-monosemanticity |
| [[2607.12279]] | Countdown Subcircuit in LLMs | 在 LLM 中定位实现倒数计数的子电路 / Localizes a countdown-implementing subcircuit in LLMs |
| [[2607.12792]] | Silent Alarm (JADR) | Jacobian lens 读内部危险识别，量化对安全的损伤 / Reads internal danger recognition via Jacobian lens to quantify safety erosion |
| [[2607.12985]] | Resist and Update (CRC) | 因果识别报告坐标并用反事实钳制兼顾抵抗与更新 / Causally identifies report coordinates and uses counterfactual clamp for dual control |
| [[2607.12815]] | Visual Access Boundaries (VAB) | 因果掩蔽证明 CoT 不延长图像访问，瓶颈在读出 / Causal masking shows CoT does not extend image access; bottleneck is readout |
| [[2607.11183]] | Amplitude-Only FFN Intervention (AG) | 仅用幅度调制 FFN 做推理时干预 / Modulates FFN amplitudes only for inference-time intervention |

### 知识编辑与遗忘 / Knowledge Editing & Unlearning

| Paper | Short Title | Description |
|-------|-------------|-------------|
| [[2607.11327]] | PRISM Edit | 面向时序知识的编辑方法 / A temporal knowledge editing method |
| [[2605.12765]] | GUARD-IT | 推理时按需遗忘的轻量化方案 / Lightweight inference-time unlearning on demand |

### RL / RLVR / 推理 / RL & Reasoning

| Paper | Short Title | Description |
|-------|-------------|-------------|
| [[2607.12395]] | Ring-Zero | 将 Zero RL 扩展到 1T 规模 / Scales Zero RL to 1T scale |
| [[2607.12640]] | GRPO Failure (Learning-Rate-Gated) | 受控零结果 + 因果机制揭示 GRPO 在已掌握任务上失效 / Controlled null + causal mechanism showing GRPO failure on mastered tasks |

### LLM 智能体 / LLM Agents

| Paper | Short Title | Description |
|-------|-------------|-------------|
| [[2607.12113]] | AISLE-2 Roadmap | 可信自主科学智能体的路线图 / Roadmap for trustworthy autonomous science agents |
| [[2607.12122]] | AI-SC Agentic Operator Discovery | 智能体驱动的神经算子发现 / Agentic discovery of neural operators |
| [[2607.12254]] | RSI Agents & Personal Singularity | 递归自我改进智能体与个人奇异性 / Recursive self-improvement agents and personal singularity |
| [[2607.12397]] | Critic Experience Bank (CEB) | 无训练、自演化的 step 级置信度估计 / Training-free self-evolving step-level confidence estimation |
| [[2607.12455]] | EvoQuant | 自演化 verifier 引导的量化策略优化 / Self-evolving verifier-guided quant strategy optimization |
| [[2607.12227]] | Rethinking Harness Evolution | 重新审视测试框架演化对评估的影响 / Re-examines harness evolution's effect on evaluation |

### 效率、量化与 KV 压缩 / Efficiency, Quantization & KV Cache

| Paper | Short Title | Description |
|-------|-------------|-------------|
| [[2602.19938]] | R&Q Replicate-and-Quantize | 面向 MoE 的复制再量化方法 / Replicate-and-quantize method for MoE |
| [[2603.24787]] | ReLope | KL 正则化 LoRA 探针做 MLLM 路由 / KL-regularized LoRA probes for MLLM routing |
| [[2606.04115]] | dMX | 可微混合精度量化 / Differentiable mixed-precision quantization |
| [[2607.12266]] | Saturation Coverage Model | 用饱和覆盖模型刻画量化 / Characterizes quantization via a saturation coverage model |
| [[2607.12550]] | JoLT (KV Cache) | Tucker + JL 残差的近无损 KV 压缩 / Near-lossless KV compression via Tucker + JL residual |
| [[2607.12789]] | AVQ-Attention | 自适应向量量化注意力，重要性来自注意力本身 / Adaptive vector-quantized attention; importance from attention itself |

### 优化与学习理论 / Optimization & Learning Theory

| Paper | Short Title | Description |
|-------|-------------|-------------|
| [[2405.11667]] | Local SGD Limits & Potentials | 系统刻画 Local SGD 的极限与潜力 / Characterizes limits and potentials of Local SGD |
| [[2605.22432]] | AMUSE Anytime Muon | 任意时刻可暂停的 Muon 优化器 / Anytime pausable Muon optimizer |
| [[2607.12332]] | Diagonal Linear Networks Implicit Bias | 对角线性网络的隐式偏置（ICML 2026）/ Implicit bias of diagonal linear networks (ICML 2026) |
| [[2607.12438]] | Fisher Rank Inflation | 标签噪声下 Fisher 有效秩膨胀作为记忆谱签名 / Fisher effective-rank inflation as a spectral signature of memorization |

### 评测与基准 / Evaluation & Benchmarks

| Paper | Short Title | Description |
|-------|-------------|-------------|
| [[2511.04689]] | ATLAS Adaptive Testing | 面向 LLM 的自适应测试评测 / Adaptive testing for LLM evaluation |
| [[2606.17930]] | Inference Compute Shapes Eval | 推理算力如何重塑前沿 LLM 评测 / How inference compute reshapes frontier LLM eval |
| [[2607.12085]] | GenAI Eval for Conversational Agents | 会话式智能体的 GenAI 评估框架 / GenAI evaluation for conversational agents |
| [[2607.12338]] | Minimum Sufficient Task Budget | 回放分析定义 agent 基准的最小充分任务预算 / Replay analysis defining minimum sufficient task budget for agent benchmarks |
| [[2607.12790]] | Double Ratchet | 评估指标作为可演化对象与技能共进化 / Evaluation metric as an evolvable object co-evolving with skills |
| [[2607.12835]] | Can LLMs Write Reliable Rubrics | LLM 自动生成论文复现 rubric 的元评估 / Meta-evaluation of LLM-authored paper-reproduction rubrics |
| [[2607.12868]] | Deep4ge | DNN 训练轨迹的故障检测与诊断基准 / DNN training-trajectory fault detection and diagnosis benchmark |

### OOD 检测 / Out-of-Distribution Detection

| Paper | Short Title | Description |
|-------|-------------|-------------|
| [[2607.12094]] | SAID for OOD Detection | 用稀疏自编码器做 OOD 检测 / Uses sparse autoencoders for OOD detection |
| [[2607.12523]] | OOD-RL-Bench | 强化学习轨迹 OOD 检测评测框架 / RL trajectory OOD detection benchmark framework |

### 安全与对齐 / Safety & Alignment

| Paper | Short Title | Description |
|-------|-------------|-------------|
| [[2607.12469]] | Agent-Safety Reconstructability | 厂商无关的智能体安全评测可重构性度量 / Vendor-neutral reconstructability metric for agent-safety evaluation |

### 硬件与容错 / Hardware & Fault Tolerance

| Paper | Short Title | Description |
|-------|-------------|-------------|
| [[2607.12298]] | EIR Self-Healing on FPGA SoCs | FPGA SoC 上的自愈机制 / Self-healing mechanism on FPGA SoCs |

## All Papers

| Paper | Short Title | Primary Topic |
|-------|-------------|---------------|
| [[2405.11667]] | Local SGD Limits & Potentials | Theory/Optimization |
| [[2511.04689]] | ATLAS Adaptive Testing | Evaluation |
| [[2602.19938]] | R&Q Replicate-and-Quantize for MoE | Efficiency/Quantization |
| [[2603.06592]] | Hierarchical Latent Structures | Interpretability |
| [[2603.24787]] | ReLope LoRA Probes for Routing | Routing/Efficiency |
| [[2605.05686]] | Attractor Geometry of Transformer Memory | Interpretability |
| [[2605.12765]] | GUARD-IT Inference-Time Unlearning | Safety/Unlearning |
| [[2605.22432]] | AMUSE Anytime Muon Optimizer | Optimization |
| [[2606.04115]] | dMX Differentiable Mixed-Precision | Quantization |
| [[2606.17930]] | Inference Compute Shapes Frontier Eval | Evaluation |
| [[2606.27321]] | Sparsity Regularizers for Top-k SAEs | Interpretability |
| [[2607.11183]] | Amplitude-Only FFN Intervention | Inference Intervention |
| [[2607.11327]] | PRISM Edit Temporal Knowledge Editing | Knowledge Editing |
| [[2607.11990]] | Sparse Inter-Layer FFN Dependencies | Interpretability |
| [[2607.12085]] | GenAI Eval for Conversational Agents | Evaluation |
| [[2607.12094]] | SAID SAEs for OOD Detection | OOD Detection |
| [[2607.12113]] | Trustworthy Autonomous Science (AISLE-2) | Agents/Position |
| [[2607.12122]] | AI-SC Agentic Operator Discovery | Agents/Science |
| [[2607.12166]] | SAE Causal Audit | Interpretability |
| [[2607.12227]] | Rethinking Harness Evolution | Agents/Evaluation |
| [[2607.12254]] | RSI Agents & Personal Singularity | Agents/Position |
| [[2607.12266]] | Saturation Coverage Model for Quantization | Quantization/Theory |
| [[2607.12279]] | Countdown Subcircuit in LLMs | Interpretability |
| [[2607.12298]] | EIR Self-Healing on FPGA SoCs | Hardware/Fault Tolerance |
| [[2607.12332]] | Diagonal Linear Networks Implicit Bias | Theory |
| [[2607.12338]] | Minimum Sufficient Task Budget | Evaluation/Agents |
| [[2607.12395]] | Ring-Zero RL to 1T | RL/Reasoning |
| [[2607.12397]] | Critic Experience Bank (CEB) | Agents/Confidence |
| [[2607.12438]] | Fisher Rank Inflation | Theory/Memorization |
| [[2607.12455]] | EvoQuant Quantitative Trading | Agents/Finance |
| [[2607.12469]] | Agent-Safety Reconstructability | Safety/Evaluation |
| [[2607.12523]] | OOD-RL-Bench | OOD/RL Safety |
| [[2607.12550]] | JoLT KV Cache Compression | KV Cache |
| [[2607.12640]] | GRPO Failure (Learning-Rate-Gated) | RL/Agents |
| [[2607.12789]] | AVQ-Attention | Efficient Attention |
| [[2607.12790]] | Double Ratchet Metric Evolution | Agents/Evaluation |
| [[2607.12792]] | Silent Alarm (JADR) | Safety/Interpretability |
| [[2607.12815]] | Visual Access Boundaries (VAB) | VLM/Interpretability |
| [[2607.12835]] | LLM Rubric Meta-Evaluation | Evaluation |
| [[2607.12868]] | Deep4ge Fault Detection | ML Testing/Benchmark |
| [[2607.12985]] | Resist and Update (CRC) | Interpretability/Sycophancy |
