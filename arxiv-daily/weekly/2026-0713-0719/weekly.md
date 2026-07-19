---
title: "Weekly arXiv Digest — 2026-07-13–2026-07-19"
week: 2026-0713-0719
date_range:
  - 2026-07-13
  - 2026-07-17
tags:
  - weekly-digest
  - self-evolving-agents
  - interpretability
  - reliability
  - quantization
  - training-dynamics
  - agent-safety
papers: 183
---

# Weekly arXiv Digest — 2026-07-13–2026-07-19

本周汇总 5 个工作日(2026-07-13 至 2026-07-17)共 **183** 篇去重论文 / A rollup of 5 weekdays (2026-07-13 to 2026-07-17), **183** unique papers.

---

## 本周必读 / Must Read This Week

> "如果只读这周八篇"——优先挑选跨天复现或当日必读的论文。/ The "if you read nothing else" list — prioritized by cross-day recurrence and daily must-read status.

### [[2607.12279]] Countdown Subcircuit

**推荐理由 / Why read**

中:因果干预在 Llama-3.1-70B 中定位出三个"倒计时注意力头",并证明同一子回路在推文、SHA-256、俳句、DNA 等大量任务中被复用,其几何与 Claude 3.5 Haiku 的换行回路一致——为"跨任务、跨模型共享机制"提供了干净实证。
EN:Activation patching isolates three "countdown" attention heads in Llama-3.1-70B reused across tweets, SHA-256, haikus and DNA, with key/query geometry matching Claude 3.5 Haiku's line-wrapping circuit — clean evidence for motifs shared across both tasks and models.

### [[2607.12266]] Saturation Quantization Coverage Model

**推荐理由 / Why read**

中:把混合精度量化损失形式化为布尔立方体上的集合函数,证明 W4A4 下 85–99% 方差来自一阶"饱和"项并给出闭式误差下限;在匹配内存下比 NVIDIA ModelOpt 基线低 17–21% KL 散度,子 4-bit 区间决定模型能否存活。
EN:Reframes mixed-precision loss as a Boolean-cube set function, proves 85–99% of variance is first-order "saturation" at W4A4 with a closed-form error certificate, and beats NVIDIA ModelOpt by 17–21% KL at matched memory — deciding model survival below 4 bits.

### [[2607.12227]] Rethinking Harness Evolution Evaluation

**推荐理由 / Why read**

中:在统一反馈与推理预算下,harness 演化既未稳定超越并行采样基线(pass@1 75.8 vs 86.0),演化出的 harness 也几乎不泛化到 held-out(平均仅 +0.6 分),提示当前收益主要来自额外搜索而非真正的 harness 设计——直接挑战了一个热门方向。
EN:Under matched budgets harness evolution neither beats parallel sampling (75.8 vs 86.0) nor generalizes to held-out tasks (+0.6 pts), showing reported gains stem from extra test-time search rather than genuine harness design — a sharp challenge to a fashionable subfield.

### [[2607.13631]] Hessian-Spectrum Depends on Data

**推荐理由 / Why read**

中:在广义 Gauss-Newton (GGN) 近似下给出任意宽度/深度线性网络 Hessian 特征值的闭式表达,并证明 MSE 分类解的锐度正比于最大类别占比 α_max,与 Edge-of-Stability 的经验论断直接矛盾——把训练稳定性归因到数据几何而非模型规模。
EN:Closed-form Hessian eigenvalues under GGN show MSE-classification sharpness ∝ α_max, directly contradicting the Edge-of-Stability literature and re-rooting training stability in data geometry rather than model size.

### [[2607.13683]] GSME Self-Evolving Harness

**推荐理由 / Why read**

中:GSME 把"提出修改"与"归因增益"分离,由更强的模型诊断失败写补丁,由确定性代码负责采样与三道门控(有效性/激活/配对 2σ 显著性);冻结模型跨 7 个领域拿 +9~+15.5pp 的 held-out 增益——补齐了自演化 agent 一直欠缺的可信归因与泛化证据。
EN:Separates proposal from credit via deterministic sampling and three gates (validity / activation / paired-2σ), earning +9~+15.5pp held-out gains across 7 domains on a frozen model — supplying the credit-assignment and held-out-generalization evidence self-evolving-agent work has most lacked.

### [[2607.13918]] Partially Correlated Verifier Cascades

**推荐理由 / Why read**

中:用 de Finetti 把每个错误实例的假接受率建模为潜变量,证明级联后验对门数 k 严格凹、Beta 潜变量下失败概率按幂律(而非指数)衰减;合成实验里独立性外推低估失败率 20×(k=5)到 ~3000×(k=10)。核心杠杆是"去相关"(换模型族/模态/外部证据)而非"加门"。
EN:Models false-accept rates as latent variables, proves the cascade posterior is strictly concave in k with polynomial (not exponential) decay; independence extrapolation underestimates failure 20×–3000×, so the actionable lever is decorrelation (different family / modality / oracle), not stacking more gates.

### [[2607.14552]] Answer-Conditioned CoT Degrades

**推荐理由 / Why read**

中:用一个"控制单一变量"实验干净地证明——让生成器在看到金答案后再写 CoT(即使最终答案正确)也会显著伤害学生模型的可验证推理能力(Qwen3-8B 在 MATH 上掉点),直接冲击当下主流的"答案条件蒸馏"数据构造范式。
EN:A one-bit controlled experiment cleanly shows that letting the generator see the gold answer before writing CoT (even when the answer is correct) measurably hurts a student's verifiable reasoning — an immediate red flag for mainstream answer-conditioned distillation pipelines.

### [[2607.14890]] Proof-or-Stop: Don't Trust the Agent, Trust the Evidence

**推荐理由 / Why read**

中:把自主编码 Agent 的"已测试/已审阅/可合并"等状态声明重新定义为需被证据裁决的 claim,在 9,240 个 cell 的预注册消融中把"可见测试通过但隐藏 oracle 仍失败"的情况削减 76%——本周对 AI 编码智能体生命周期治理与安全工程最系统的一篇。
EN:Reframes agent lifecycle states (tested/reviewed/mergeable) as evidence-adjudicated claims; a 9,240-cell preregistered ablation cuts "visible-pass-but-hidden-oracle-fails" by 76% — the most systematic agent-lifecycle governance and safety-engineering paper of the week.

---

## 本周主题脉络 / Themes This Week

### 1. 自演化 Agent 与自动化科研 / Self-Evolving Agents & Automated Research

本周最大的单一主线(12 篇),从"提出-归因分离"的方法论到具体科研领域的智能体落地,主线是"如何让自演化变得可信、可审计"。GSME 用统计门控给出 held-out 泛化证据,而 AutoSynthesis、LQCDMaster、BrainPilot 则把同一范式推到元分析、格点 QCD、脑科学等真问题。 / The single biggest thread this week (12 papers): from methodology that separates proposal from credit, to domain-specific deployments. GSME supplies the missing held-out generalization evidence, while AutoSynthesis / LQCDMaster / BrainPilot push the same paradigm into real meta-analysis, lattice QCD and brain science.

代表 / Highlights: [[2607.13683]] · [[2607.14777]] · [[2607.14431]] · [[2607.15247]] · [[2607.14658]] · [[2607.15001]]

### 2. 机制可解释性、电路与探测 / Mechanistic Interpretability, Circuits & Probing

本周持续高产,呈现"电路级证据 + 线性方向探测"两条并行的脉络。Countdown Subcircuit 给出跨任务、跨模型的复用机制,SAE Causal Audit / Transcoders for Deception 把审计落到欺骗电路上,Linear Grammaticality / PRISM 则在隐藏态里找到语法性与物理危险的可分离方向。 / Interpretability stayed high-volume, splitting into circuit-level evidence and linear-direction probing. Countdown Subcircuit shows cross-task/cross-model motif reuse, SAE/transcoder audits pin down deception circuits, and Linear Grammaticality / PRISM find separable hidden-state directions for grammar and physical danger.

代表 / Highlights: [[2607.12279]] · [[2607.11990]] · [[2607.12166]] · [[2607.15175]] · [[2607.15218]] · [[2607.14791]]

### 3. 可靠性、验证器级联与评测完整性 / Reliability, Verifier Cascades & Evaluation Integrity

本周一股"评测自我反思"的暗流:Verifier Cascades 给出去相关的理论指导,Harness Evolution Evaluation 是对热门方向的负面证据,Answer-Conditioned CoT 揭示数据构造范式缺陷,Statistical Self-Consistency 与"Can We Trust IRT"则用大模拟暴露前沿模型在概率自洽与 IRT 估计上的失效。 / A strong "evaluation self-audit" undercurrent: Verifier Cascades gives decorrelation theory, Harness Evolution Evaluation is negative evidence for a hot direction, Answer-Conditioned CoT exposes a distillation-pipeline flaw, and Statistical Self-Consistency / IRT-trust papers use large simulations to reveal frontier-model breakdowns.

代表 / Highlights: [[2607.13918]] · [[2607.12227]] · [[2607.14552]] · [[2607.15277]] · [[2607.15190]] · [[2607.13707]]

### 4. 量化、效率与推理计算 / Quantization, Efficiency & Inference Compute

从理论到硬件的全栈讨论:Saturation Quantization 给出 W4A4 的闭式误差下限,Atrex-Bench 用生产 trace 揭示"最强 agent 仅达 roofline 10.7%"的正确性幻觉,PolyQ / ExaGEMM / CIMERA 把分数比特与存算互连推到边缘 CPU 与新硬件,xHC 则在架构侧把 Hyper-Connections 残差扩展率从 4 推到 16。 / A full-stack week from theory to hardware: Saturation Quantization gives closed-form W4A4 error certificates, Atrex-Bench exposes a 10.7%-of-roofline correctness illusion for kernel agents, PolyQ / ExaGEMM / CIMERA push fractional-bit and compute-in-interconnect designs, and xHC scales Hyper-Connections' residual expansion from 4 to 16.

代表 / Highlights: [[2607.12266]] · [[2607.14541]] · [[2607.14618]] · [[2607.13649]] · [[2607.14530]]

### 5. 训练动力学与优化理论 / Training Dynamics & Optimization Theory

Hessian-Spectrum 把稳定性归因到数据几何并反驳 Edge-of-Stability,是本周理论侧最尖锐的一击;Muse、RK3(2)-Adam、Sharp Stability Threshold 围绕优化器几何、高阶优化器失效与残差稳定性阈值展开,How to Tame Grokking 则把表征几何当作可控信号。 / Hessian-Spectrum is the sharpest theoretical blow of the week, re-rooting stability in data geometry and contradicting Edge-of-Stability; Muse / RK3(2)-Adam / Sharp Stability Threshold circle optimizer geometry, higher-order-inertness and residual thresholds, while How to Tame Grokking treats representation geometry as a control signal.

代表 / Highlights: [[2607.13631]] · [[2607.14536]] · [[2607.14576]] · [[2607.14516]] · [[2607.11666]]

### 6. 智能体安全、基准与控制 / Agent Safety, Benchmarks & Control

自主编码 Agent 治理是重点:Proof-or-Stop 把生命周期状态变成证据裁决的 claim;同时 Mako 的自演化攻击 OS、分布式后门诊断、IaC 篡改检测与机器人动作因果调试共同把"如何信任一个会自我修改的智能体"摆到台前。 / Autonomous-coding-agent governance takes center stage: Proof-or-Stop turns lifecycle states into evidence-adjudicated claims, while Mako's self-evolving attack OS, distributed-backdoor diagnostics, IaC sabotage detection and causal robot-action debugging collectively foreground "how do you trust an agent that modifies itself?"

代表 / Highlights: [[2607.14890]] · [[2607.14570]] · [[2607.14826]] · [[2607.11288]] · [[2607.11751]]

---

## 全部论文 / All Papers

### 2026-07-13 (44)

- [[2607.10970]] Enhanced Byzantine-Robust Federated Learning Via Truncated-Quadratic Loss for Heterogeneous Data — Training / 训练
- [[2607.11007]] TabPFN beyond Tabular Data: Calibration and Accuracy on Multimodal Embeddings — Evaluation / 评估
- [[2607.11022]] When the Reward Suite Is Leaky: A Preregistered Causal Contrast of Natural Verifier False Positives in RLVR — Reasoning / 推理
- [[2607.11052]] Domain-Aware Scaling Laws Uncover Data Synergy — Training / 训练
- [[2607.11079]] Are LLMs Ready for Scientific Discovery? A Capability-Oriented Benchmark for AI Scientists — Evaluation / 评估
- [[2607.11081]] Controlling Motion Transfer in Diffusion Transformers via Attention Heads — Interpretability / 可解释性
- [[2607.11084]] NVAITC AI Scientist: A Governed End-to-End Research System — A Hypertension GWAS Case Study — Agents / 智能体
- [[2607.11098]] AgentCheck: A Reproduce–Intervene–Mitigate Workbench for LLM Agents over MCP — Agents / 智能体
- [[2607.11116]] The Equilibrium Is the Initialization: Lazy Identity Collapse in Physics-Structured Deep Equilibrium Reasoning — Theory / 理论
- [[2607.11122]] Implicit Neural Networks as Static Controllers: Certificates and Performance Separation — Theory / 理论
- [[2607.11149]] The Hidden Footprint: Making Storage a First-Class Metric for LLM Agent Evaluation — Agents / 智能体
- [[2607.11163]] Unified Gradient Projection: Language-Balanced Continual Learning for Multilingual Low-Resource ASR — Training / 训练
- [[2607.11170]] TC-MAF: Train-Calibrated Bounded Multi-Evidence Fusion for Multimodal Industrial Anomaly Detection — Evaluation / 评估
- [[2607.11175]] The Path to Self-Evolving Clinical Systems: Scaling Medical Agents from Assistance to Autonomy — Agents / 智能体
- [[2607.11193]] REPTRAN: Search-Based Repair of Transformer Models — Training / 训练
- [[2607.11211]] FastTPS: An Optimized Method for LLM Token Phase for AI Accelerators — Efficiency / 效率
- [[2607.11214]] A Novel Method to Evaluate Models on Unreliable, Noisy and Inconsistent Labels (ARLA) — Evaluation / 评估
- [[2607.11226]] Heterogeneous Agent Cohorts for Safe Open-Ended Exploration with Runtime Constraint Memory — Safety / 安全
- [[2607.11250]] Multi-Agent LLMs Fail to Explore Each Other — Agents / 智能体
- [[2607.11266]] Valid ≠ Necessary: Diagnosing Latent Inefficiency in Chain-of-Thought — Reasoning / 推理
- [[2607.11267]] Enhancing LLMs through human feedback: a journey towards self-improvement — Training / 训练
- [[2607.11288]] Mako: A Self-Evolving Agentic Operating System (SE-AOS) for Autonomous Web Exploitation — Safety / 安全
- [[2607.11289]] Backpropagation as a Nilpotent Linear System — Theory / 理论
- [[2607.11317]] Calibrated e-CUSUM Decoding for Quantized Reasoning Models — Efficiency / 效率
- [[2607.11327]] PRISM Edit: One Vector for All Temporal Answers — Interpretability / 可解释性 ↻07-15
- [[2607.11347]] From Neural Network Decisions to Training Cases: An Exact Account via Case-Based Decision Theory — Interpretability / 可解释性
- [[2607.11359]] Efficient Tuning Before Low-Bit Post-Training Quantization for SGD-optimized Models — Efficiency / 效率
- [[2607.11368]] Decomposing Runtime, Kernel, and Quantization Speedups via a Matched FP16 Intermediate — Efficiency / 效率
- [[2607.11388]] StructAgent: Harness Long-horizon Digital Agents with Unified Causal Structure — Agents / 智能体
- [[2607.11414]] Confidently Wrong: Detecting Hallucinations in Financial Question Answering from LLM Internal States — Reasoning / 推理
- [[2607.11444]] Unlocking Every Expert in Domain-Specific Training — Training / 训练
- [[2607.11475]] HyperSafe: Inference-Time Safety Recovery for Fine-Tuned Language Models — Safety / 安全
- [[2607.11541]] Random Label Prediction Heads for Studying Memorization in Deep Neural Networks — Interpretability / 可解释性
- [[2607.11542]] Condition-Stratified Robustness Analysis of Post-Hoc Calibration Methods for Probabilistic Classifiers — Evaluation / 评估
- [[2607.11586]] HCRMap: Pressure-Aware Hot-Expert Residency Mapping for 3.5D MoE Chiplet Inference — Efficiency / 效率
- [[2607.11598]] Interaction Scaling: Grounding the Third Axis of Test-Time Compute — Reasoning / 推理
- [[2607.11607]] Auditing the Risk Claims of Distributional Reinforcement Learning — Reasoning / 推理
- [[2607.11666]] How to Tame Grokking: Representation Geometry as a Control Signal — Theory / 理论
- [[2607.11698]] Agent Hacks Agent: Autoresearch for Production-Agent Red-Teaming — Safety / 安全
- [[2607.11751]] When Local Monitors Miss Compositional Harm: Diagnosing Distributed Backdoors in Multi-Agent Systems — Safety / 安全
- [[2607.11796]] An Exact Instrument for State Usage in Selective State-Space Models, and the Input-Driven Migration It Reveals — Interpretability / 可解释性
- [[2607.11801]] Encoder-Side Neuron Identification and Amplification for Acoustic Perception in Large Audio-Language Models — Evaluation / 评估
- [[2607.11871]] Inside the Unfair Judge: A Mechanistic Interpretability Account of LLM-as-Judge Bias — Interpretability / 可解释性
- [[2607.11875]] Invariant Learning Dynamics of Transformers in Inductive Reasoning Tasks — Theory / 理论

### 2026-07-14 (39)

- [[2607.12227]] Rethinking Harness Evolution Evaluation — Agent Benchmarks / 智能体基准 ⭐ ↻07-15
- [[2607.12252]] FinResearchBench II — Agent Benchmarks / 智能体基准
- [[2607.12254]] Recursively Self-Improving Agents — Agents & Memory / 智能体与记忆 ↻07-15
- [[2607.12266]] Saturation Quantization Coverage Model — Quantization / 量化 ⭐ ↻07-15
- [[2607.12273]] Code-MUE — Code & SE / 代码与软件工程
- [[2607.12279]] Countdown Subcircuit — Mechanistic Interp / 机制可解释性 ⭐ ↻07-15
- [[2607.12298]] EIR FPGA Self-Healing — Applications / 应用 ↻07-15
- [[2607.12332]] Diagonal Linear Network Dynamics — Training Dynamics / 训练动力学 ↻07-15
- [[2607.12338]] How Many Tasks Are Enough — Agent Benchmarks / 智能体基准 ↻07-15
- [[2607.12360]] LR Cooldown Noise Structure — Training Dynamics / 训练动力学
- [[2607.12385]] PM-Bench Prospective Memory — Agent Benchmarks / 智能体基准
- [[2607.12397]] Critic Experience Bank (CEB) — Confidence & Safety / 置信度与安全 ↻07-15
- [[2607.12438]] Fisher Rank Inflation — Training Dynamics / 训练动力学 ↻07-15
- [[2607.12447]] SDC Confidence in LLMs — Confidence & Safety / 置信度与安全
- [[2607.12455]] EvoQuant Trading — Applications / 应用 ↻07-15
- [[2607.12469]] Agent-Safety Reconstructability — Agent Benchmarks / 智能体基准 ↻07-15
- [[2607.12474]] Mechanistic World Models — Position / 立场论文
- [[2607.12526]] Source-Grounded Feature Inversion — Mechanistic Interp / 机制可解释性
- [[2607.12545]] VanillaBench — LLM-as-Judge / 评判者方法学
- [[2607.12616]] FTSS Flow Matching Memorization — Training Dynamics / 训练动力学
- [[2607.12625]] KnowAct-GUIClaw — Agents & Memory / 智能体与记忆
- [[2607.12640]] GRPO Failure Web Agent — Agents & Memory / 智能体与记忆 ↻07-15
- [[2607.12687]] CARE-PPO — Confidence & Safety / 置信度与安全
- [[2607.12735]] Grokking Representational Priors — Training Dynamics / 训练动力学
- [[2607.12739]] ESFP Epistemic Stance — LLM-as-Judge / 评判者方法学
- [[2607.12747]] Oat Failure Attribution — Agents & Memory / 智能体与记忆
- [[2607.12767]] Bayesian Accuracy Length Bias — LLM-as-Judge / 评判者方法学
- [[2607.12780]] Quantum Circuit Autoregressive Drift — Applications / 应用
- [[2607.12790]] Double Ratchet — Agents & Memory / 智能体与记忆 ↻07-15
- [[2607.12792]] JADR J-Space Safety — Confidence & Safety / 置信度与安全 ↻07-15
- [[2607.12796]] One-Word Census — Confidence & Safety / 置信度与安全
- [[2607.12835]] LLM Rubric Meta-Evaluation — LLM-as-Judge / 评判者方法学 ↻07-15
- [[2607.12863]] ROBIN Attention Bias — Mechanistic Interp / 机制可解释性
- [[2607.12868]] Deep4ge DNN Faults — Code & SE / 代码与软件工程 ↻07-15
- [[2607.12885]] LLM Judges Too Generous — LLM-as-Judge / 评判者方法学
- [[2607.12893]] MemOps Memory Benchmark — Agents & Memory / 智能体与记忆
- [[2607.12954]] PV Forecasting Robustness — Applications / 应用
- [[2607.12962]] PoPE Self-Repair — Code & SE / 代码与软件工程
- [[2607.12963]] Illusion of Robustness — Confidence & Safety / 置信度与安全

### 2026-07-15 (24)

- [[2405.11667]] Local SGD Limits & Potentials — Theory/Optimization
- [[2511.04689]] ATLAS Adaptive Testing — Evaluation
- [[2602.19938]] R&Q Replicate-and-Quantize for MoE — Efficiency/Quantization
- [[2603.06592]] Hierarchical Latent Structures — Interpretability
- [[2603.24787]] ReLope LoRA Probes for Routing — Routing/Efficiency
- [[2605.05686]] Attractor Geometry of Transformer Memory — Interpretability
- [[2605.12765]] GUARD-IT Inference-Time Unlearning — Safety/Unlearning
- [[2605.22432]] AMUSE Anytime Muon Optimizer — Optimization
- [[2606.04115]] dMX Differentiable Mixed-Precision — Quantization
- [[2606.17930]] Inference Compute Shapes Frontier Eval — Evaluation
- [[2606.27321]] Sparsity Regularizers for Top-k SAEs — Interpretability
- [[2607.11183]] Amplitude-Only FFN Intervention — Inference Intervention
- [[2607.11990]] Sparse Inter-Layer FFN Dependencies — Interpretability
- [[2607.12085]] GenAI Eval for Conversational Agents — Evaluation
- [[2607.12094]] SAID SAEs for OOD Detection — OOD Detection
- [[2607.12113]] Trustworthy Autonomous Science (AISLE-2) — Agents/Position
- [[2607.12122]] AI-SC Agentic Operator Discovery — Agents/Science
- [[2607.12166]] SAE Causal Audit — Interpretability
- [[2607.12395]] Ring-Zero RL to 1T — RL/Reasoning
- [[2607.12523]] OOD-RL-Bench — OOD/RL Safety
- [[2607.12550]] JoLT KV Cache Compression — KV Cache
- [[2607.12789]] AVQ-Attention — Efficient Attention
- [[2607.12815]] Visual Access Boundaries (VAB) — VLM/Interpretability
- [[2607.12985]] Resist and Update (CRC) — Interpretability/Sycophancy

### 2026-07-16 (50)

- [[2607.13608]] Auto ODE Discovery (Bio) — Self-Evolving Agents / 自演化智能体
- [[2607.13631]] Hessian-Spectrum Depends on Data — Training Dynamics / 训练动力学 ⭐
- [[2607.13649]] CIMERA Compute-in-Interconnect — Quantization & Inference / 量化与推理
- [[2607.13660]] CLIP Hyperspherical Geometry — Math Foundations / 数学基础
- [[2607.13683]] GSME Self-Evolving Harness — Self-Evolving Agents / 自演化智能体 ⭐
- [[2607.13707]] Test Oracle Problem LLM-as-Judge — LLM Evaluation / LLM 评测
- [[2607.13753]] Post-Training Shifts Confidence — LLM Evaluation / LLM 评测
- [[2607.13898]] FPGA MXFP Tensor Block — Quantization & Inference / 量化与推理
- [[2607.13899]] AIMO Interpretability Challenge — Interpretability / 可解释性
- [[2607.13918]] Partially Correlated Verifier Cascades — Computation Reliability / 计算可靠性 ⭐
- [[2607.13940]] Self-Evolving Health Agent — Self-Evolving Agents / 自演化智能体
- [[2607.14004]] Do Agent Optimizers Compound? — Self-Evolving Agents / 自演化智能体
- [[2607.14018]] Transforming Rank: Spectral Pathologies — Training Dynamics / 训练动力学
- [[2607.14178]] ReasFlow Math Discovery — Self-Evolving Agents / 自演化智能体
- [[2607.14181]] Quantize with Confidence? (Code Gen) — Quantization & Inference / 量化与推理
- [[2607.14185]] Closed-Loop Knowledge Dynamics — Training Dynamics / 训练动力学
- [[2607.14228]] SeeSE3: 3D Space in Vision — Math Foundations / 数学基础
- [[2607.14275]] Context Fails First — LLM Evaluation / LLM 评测
- [[2607.14306]] ENTD: Trace to Training Data — Interpretability / 可解释性
- [[2607.14375]] Random Noise vs ReLU Verification — Computation Reliability / 计算可靠性
- [[2607.14399]] Instrument Effects in Honesty Eval — Interpretability / 可解释性
- [[2607.14408]] Reward-Free Evolving Agents — Self-Evolving Agents / 自演化智能体
- [[2607.14427]] Per-Token Fixed-Point Convergence — Training Dynamics / 训练动力学
- [[2607.14431]] Byte-Exact KV-State Grafting Flywheel — Self-Evolving Agents / 自演化智能体
- [[2607.14463]] Hidden-State Collapse (LiDAR AE) — Interpretability / 可解释性 ↻07-17
- [[2607.14480]] LLM Evaluators Biased across Languages — LLM Evaluation / LLM 评测 ↻07-17
- [[2607.14506]] Non-vacuous Bounds for RLVR — Math Foundations / 数学基础 ↻07-17
- [[2607.14516]] RK3(2)-Adam Compute-Matched Study — Training Dynamics / 训练动力学 ↻07-17
- [[2607.14528]] CRTBench: Logical Consistency — LLM Evaluation / LLM 评测 ↻07-17
- [[2607.14536]] Muse: Muon Representation Geometry — Training Dynamics / 训练动力学 ↻07-17
- [[2607.14541]] Atrex-Bench: GPU Kernels — Quantization & Inference / 量化与推理 ↻07-17
- [[2607.14552]] Answer-Conditioned CoT Degrades — LLM Evaluation / LLM 评测 ⭐ ↻07-17
- [[2607.14568]] Multimodal on 2011 Fermi GPU — Quantization & Inference / 量化与推理
- [[2607.14576]] Sharp Stability Threshold (Residual) — Training Dynamics / 训练动力学 ↻07-17
- [[2607.14618]] PolyQ: Edge CPU Quantization — Quantization & Inference / 量化与推理 ↻07-17
- [[2607.14622]] ExaGEMM In-Register Computing — Quantization & Inference / 量化与推理
- [[2607.14658]] TopoAgent: Self-Evolving Topological — Self-Evolving Agents / 自演化智能体 ↻07-17
- [[2607.14777]] SEED: Self-Evolving OPD — Self-Evolving Agents / 自演化智能体 ↻07-17
- [[2607.14791]] Transcoders for Deception — Interpretability / 可解释性 ↻07-17
- [[2607.14817]] Evaluating Epistemic Uncertainty — Math Foundations / 数学基础 ↻07-17
- [[2607.14943]] WA-LQR: Steering Robustness into WAMs — Interpretability / 可解释性 ↻07-17
- [[2607.15001]] LQCDMaster: Agentic Lattice QCD — Self-Evolving Agents / 自演化智能体 ↻07-17
- [[2607.15079]] BrainPilot: Agentic Brain Discovery — Self-Evolving Agents / 自演化智能体 ↻07-17
- [[2607.15084]] Face Embedding Geometry MIA — Math Foundations / 数学基础 ↻07-17
- [[2607.15175]] Linear Representations of Grammaticality — Interpretability / 可解释性 ↻07-17
- [[2607.15190]] Can We Trust IRT for AI Evaluation? — LLM Evaluation / LLM 评测 ↻07-17
- [[2607.15196]] Subjective Risk Decomposition — Math Foundations / 数学基础 ↻07-17
- [[2607.15218]] PRISM: Physical Danger Beyond Text — Interpretability / 可解释性 ↻07-17
- [[2607.15247]] AutoSynthesis: Automated Meta-Analysis — Self-Evolving Agents / 自演化智能体 ↻07-17
- [[2607.15277]] Statistical Self-Consistency in LLMs — LLM Evaluation / LLM 评测 ↻07-17

### 2026-07-17 (26)

- [[2607.14460]] Precise sample covariance spectral norm error – an RDT view — 协方差谱范数精确界 / Sharp covariance spectral bound
- [[2607.14466]] Interleaved Noise Injection Improves Clean, Corrupted, and OOD Performance — 交替噪声课程 / Interleaved noise curriculum
- [[2607.14530]] xHC: Expanded Hyper-Connections — Transformer 架构 / Transformer architecture ⭐
- [[2607.14545]] CASP: Learning-Augmented Offline Approximation with Verifiable Certificates — 学习增强近似算法 / Learning-augmented approximation
- [[2607.14560]] Breaking the Model Forgetting Cycle in Long-Incremental 3D Object Detection — 长期增量 3D 检测 / Long-incremental 3D detection
- [[2607.14570]] Democratizing Agent Deployment Safety: A Structural Monitoring Approach — IaC 篡改检测 / IaC sabotage detection
- [[2607.14582]] MathCoPilot: Interactive Human-AI Symbiotic Theorem Proving — 人机协同定理证明 / Human-AI theorem proving
- [[2607.14707]] Harnessing LLMs for Reliable Academic Supervision — 工程化 vs 裸 LLM / Engineered vs bare LLM
- [[2607.14720]] Causal-Adversarial Probing of Clinical Covariates for Prostate MRI Grading — 协变量因果探测 / Causal covariate probing
- [[2607.14731]] What's in a Smoothness Constant? Tighter Rates for Local SGD — Local SGD 收敛率 / Local SGD convergence
- [[2607.14737]] GeoDetect: Geometric Adversarial Detection for VLPs — VLP 对抗检测 / VLP adversarial detection
- [[2607.14760]] Clean-Reference Streaming Detection of Lens Occlusion — 摄像头篡改流式检测 / Streaming camera-tamper detection
- [[2607.14826]] Interventional Causal Circuits for Safe Robot Action Testing — 机器人动作因果调试 / Causal robot action debugging
- [[2607.14862]] Tamed Stochastic Gradient Hamiltonian Monte Carlo — 驯服 SGHMC / Tamed SGHMC
- [[2607.14877]] PAC Learning in Turn-Based Stochastic Games with Reachability Objectives — 随机博弈 PAC 学习 / TBSG PAC learning
- [[2607.14889]] Analytical Study of the Optimal Combination of Binary Classifiers — 分类器集成理论 / Classifier ensemble theory
- [[2607.14890]] Proof-or-Stop: Don't Trust the Agent, Trust the Evidence — 智能体生命周期证据门控 / Agent lifecycle evidence gating ⭐
- [[2607.14947]] Optimal Self-Distillation for Rectified Flow via Linear Probing — 线性 RF 自蒸馏 / Linear RF self-distillation
- [[2607.14952]] LongStraw: Long-Context RL Beyond 2M Tokens under a Fixed GPU Budget — 固定预算长上下文 RL / Fixed-budget long-context RL
- [[2607.14967]] Latent Trajectory Discrimination for AI-Generated Text Detection — AI 文本检测 / AI-text detection
- [[2607.15003]] SMC-ES: Automated Synthesis of Formally Verified Control Policies — 形式验证控制策略 / Formally verified control
- [[2607.15067]] Kernel Weighted Importance Sampling for Off-Policy Evaluation — 核加权 OPE / Kernel-weighted OPE
- [[2607.15080]] Evaluating Covariate Balance for Long-Horizon MDPs — 离线 RL 协变量均衡 / Offline-RL covariate balance
- [[2607.15105]] Long-Context Fine-Tuning with Limited VRAM — 低 VRAM 长上下文 QLoRA / Low-VRAM long-context QLoRA
- [[2607.15164]] The Industrialization of Research: On AI-Driven Science — AI 科学的工业化批判 / AI-science industrialization critique
- [[2607.15208]] Delocalization of Bias in Unadjusted Hamiltonian Monte Carlo — HMC 偏差离域化 / HMC bias delocalization


---

*本周摘要是每日 digest 的汇总。完整每日列表见:* / *This digest is a rollup of the daily overviews. Per-day lists:*

[2026-07-13](../../2026-07-13/overview.md) · [2026-07-14](../../2026-07-14/overview.md) · [2026-07-15](../../2026-07-15/overview.md) · [2026-07-16](../../2026-07-16/overview.md) · [2026-07-17](../../2026-07-17/overview.md)
