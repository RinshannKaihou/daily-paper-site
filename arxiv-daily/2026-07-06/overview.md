---
title: "Daily arXiv Digest — 2026-07-06"
date: 2026-07-06
tags:
  - llm-interpretability
  - hidden-states
  - training-reliability
  - llm-evaluation
  - self-evolving-agents
  - mathematical-foundations
  - computation-reliability
  - jailbreak-safety
  - mechanistic-interpretability
  - inference-optimization
papers: 28
---

## 今日必读 / Must Read Today

### 1. [[2607.04640]] Wrong Before Right: Late Rescue and Interface Failure in Aligned Language Models

**推荐理由 / why-read:** 这篇论文用因果 patchscope 验证（17 个模型、278 个最小对）揭示对齐 LLM 在中层"先选错答案再靠后层补救"的"wrong-dip"现象，并证明它能预测结构化压缩失效（3–7×）但对量化失效完全失明——这是一种在输出完美时仍可审计内部组装过程的可靠性工具。
*Why read:* With causal patchscope verification across 17 models, this work shows aligned LLMs transiently commit to the *wrong* answer in mid layers and are rescued only by late layers — a "wrong-dip" that predicts structural-compression failures (3–7×) but is blind to quantization, giving a zero-overhead audit for deployment-time reliability that catches silent fragility hidden behind perfect surface accuracy.

### 2. [[2607.05184]] Rethinking On-Policy Self-Distillation for Thinking Models

**推荐理由 / why-read:** 一个反直觉、机制清晰的负面结果：给思维模型提供特权参考答案的自蒸馏反而降低长链推理（avg@16 最高 −17%），根因是特权教师信号在"分叉位置"翻转了自纠错 token 的优势符号，抑制了审议行为——直接挑战当前流行的 OPSD 训练范式。
*Why read:* A clean, counterintuitive negative result: privileged-context on-policy self-distillation *degrades* thinking models (up to −17% avg@16) because the teacher flips the advantage sign on self-correction tokens ("but"/"wait") at fork positions, suppressing the very deliberation that powers long-chain gains — directly challenging a trending training recipe.

### 3. [[2607.05355]] Faithfulness to Refusal: A Causal Audit of Neuron Selectors

**推荐理由 / why-read:** 用单一"神经元行置零"干预因果审计七种重要性选择器，得到一个对剪枝/安全编辑实践有直接意义的尖锐发现：排名稳定性与因果有效性完全解离（最稳定的 MeanActivation 因果失效），且拒答子空间高度冗余（LRP↔IG top-1% 重叠仅 3–6% 却都能安装拒答）。
*Why read:* A single neuron-row-zeroing intervention audits seven importance selectors and lands a sharp, practitioner-relevant finding: rank-stability and causal-validity *completely dissociate* (the most stable selector is causally invalid), and the refusal subspace is highly redundant — warning that the cheap stability proxies the pruning/safety-editing community relies on are systematically blind.

---

## 按主题分类 / Papers by Topic

### 可解释性与隐藏状态 / Interpretability & Hidden States

| Paper | Short Title 简称 | Key Contribution 核心贡献 |
|-------|------------------|---------------------------|
| [[2607.04640]] | Wrong-Dip Late Rescue 迟到补救 / Late-Rescue in Aligned LLMs | 因果验证中层"先错后对"现象，预测结构化压缩失效但盲于量化。Causally verifies mid-layer wrong-dip; predicts structural-compression but not quantization failures. |
| [[2607.05316]] | Remaining Output Length 剩余长度编码 / Length Tracking in LLMs | 冻结残差流上线性探针即可解码剩余输出长度，且在回撤 token 处动态上调。Linear probe on frozen residual stream decodes remaining output length and shifts upward at retraction tokens. |
| [[2607.05013]] | K vs V Solvability 解耦知识-语言化 / Knowledge vs. Verbalization | 用两个线性探针解耦"知道题目不可解"与"说出来"，证明编造答案源于语言化偏移。Two linear probes disentangle knowing-vs-saying of math unsolvability; fabrication stems from verbalization shift. |
| [[2607.05188]] | Latent Coding Horizons 编码agent潜在视野 / Latent Programming Horizons | 编码 agent 残差流线性解码程序正确性，且能在编辑落地前~25步预测结果。Coding-agent residual stream linearly decodes program correctness and predicts edit outcomes ~25 steps ahead. |
| [[2607.04683]] | VLM Error Attribution VLM错误归因 / Attributing VLM Errors | 归因树将 VQA 错误分解为视觉/实体/事实/召回四类，解码前即可预测并路由修复。Attribution tree decomposes VQA errors into 4 causes; pre-decoding probes enable targeted repair (+30–39pts). |
| [[2607.05355]] | Neuron Selector Audit 神经元选择器审计 / Causal Audit of Selectors | 单一神经元行置零审计选择器，证明排名稳定性与因果有效性完全解离。One-shot neuron-row zeroing shows rank-stability ≠ causal-validity; refusal subspace is redundant. |
| [[2607.05175]] | Platonic Projection Structures 柏拉图投影 / Operator-Induced Observability | 用自伴算子的核刻画输出可解释性的结构性盲区：ker(Π)内潜方向不可观测。Self-adjoint operator kernel defines structural limits of output-based interpretability (SHAP/LIME). |
| [[2607.04926]] | Tiny-Transformer Binding 微小模型绑定 / Few-Shot Binding in Tiny Transformers | 可全枚举测试床证明零样本组合绑定在所有输入路径下失败，少样本效率只由参数共享与可读性决定。Fully-enumerable testbed shows zero-shot binding fails on all pathways; few-shot governed by sharing + readability. |
| [[2607.04800]] | L4 Computation in Superposition L4超叠加计算 / Superposition via L4 Loss | 仅把损失从 L2 换成 L4 即让 50 神经元网络涌现超叠加计算，并逆向工程出稀疏二进制码+伪逆机制。Swapping L2→L4 loss elicits computation in superposition; fully reverse-engineered sparse-code + pseudoinverse. |

### 训练可靠性与稳定性 / Training Reliability & Stability

| Paper | Short Title 简称 | Key Contribution 核心贡献 |
|-------|------------------|---------------------------|
| [[2607.05184]] | OPSD Thinking Models 自蒸馏负面结果 / Privileged Self-Distillation Harms Thinking Models | 特权自蒸馏在分叉位置翻转自纠错 token 优势，降低思维模型长链推理。Privileged self-distillation flips advantage on self-correction tokens, degrading long-chain reasoning. |
| [[2607.04728]] | SIS Off-Policy→On-Policy 选择性重要性采样 / Selective Importance Sampling | 拒绝采样把离线 rollout 的 off-policy token 转为 on-policy（权重置1），~1%开销收紧梯度误差界。Rejection sampling converts off-policy tokens to on-policy (~1% overhead), tightening the gradient-error bound. |
| [[2607.04969]] | Memorization Data Reuse 记忆窗口数据重用 / Memorization-Guided Data Reuse | "记忆窗口"框架刻画数据重用安全区间，挑战 4-epoch 经验上限，可达 125+ epochs。Memorization-window framework defines safe data-reuse interval; challenges the 4-epoch heuristic. |
| [[2607.05104]] | Grokking Fragility Grokking脆弱性 / Fragile Grokking at 12K Params | 仅改变 CPU 线程数即翻转 16% 同种子 grok 结果，证明 grokking 是受浮点环境门控的脆弱相变。Changing CPU thread count flips 16% same-seed grok outcomes; grokking is numerically fragile. |

### 推理与评估 / Inference & Evaluation

| Paper | Short Title 简称 | Key Contribution 核心贡献 |
|-------|------------------|---------------------------|
| [[2607.05391]] | LLM-as-a-Verifier LLM验证器 / General-Purpose Verification | 对打分 token logits 取期望得连续奖励，三轴缩放，四基准 SOTA 且可作 RL 密集奖励。Expectation over scoring-token logits gives continuous reward; 3-axis scaling; SOTA on 4 benchmarks + RL reward. |
| [[2607.05046]] | CollabEval Matrix Completion 矩阵补全评测 / Collaborative Eval via Completion | 把评测建模为模型×提示词矩阵补全，CrossPPI 控制变量保证无偏，CI 宽度缩窄 20–30%。Models eval as matrix completion; CrossPPI control variates give unbiased CIs, 20–30% narrower. |
| [[2607.04686]] | ToolFailBench 工具失败诊断 / Diagnosing Tool-Use Failures | 参数化陷阱分离 4 类工具失败，同规模 Llama/Qwen 差 89 分，证明聚合分数掩盖机制。Parametric traps isolate 4 tool-use failures; same-scale Llama/Qwen differ 89pts on control accuracy. |
| [[2607.04681]] | VLA Faithfulness VLA忠实性 / Faithful Embodied Reasoning | 区分功能性与忠实性推理，训练 Pinocchio 评判器作 GRPO 密集奖励提升忠实性。Separates functional vs. faithful reasoning in VLAs; Pinocchio critic + GRPO lifts faithfulness. |
| [[2607.05198]] | Noisy-Channel MBR 噪声通道MBR解码 / Noisy-Channel MBR Decoding | 将 MBR 打分分解为四概率通道，统一 5 种变体，揭示指标方向性非对称。Decomposes MBR into 4 probabilistic channels; unifies 5 variants; reveals metric asymmetry. |
| [[2607.04572]] | Truncated CoT Auditing 截断CoT审计 / Truncated CoT Auditing | 截断式探针检测教育辅导中"答案驱动推理"，答案钥匙使 TRACE AUC 从 0.375 升到 0.900。Truncated-prefix probing detects answer-driven reasoning in tutoring; AUC 0.375→0.900 with answer-key. |

### 自进化智能体 / Self-Evolving Agents

| Paper | Short Title 简称 | Key Contribution 核心贡献 |
|-------|------------------|---------------------------|
| [[2607.05297]] | MetaSkill-Evolve 元技能进化 / Recursive Meta-Skill Evolution | 双时间尺度框架让 meta-skill 被同一管线递归改写，OfficeQA/SealQA +23.5/+16.1。Two-timescale recursion co-evolves meta-skills via the same pipeline; +23.5/+16.1 on QA benchmarks. |
| [[2607.05202]] | EvoAgentBench 能力迁移评测 / Benchmarking Ability Transfer | 首个保证训练侧能力支撑的迁移评测基准，揭示自动抽取/路由方法的脆弱性。First ability-supported transfer benchmark; exposes brittleness of automatic skill extraction/routing. |
| [[2607.04645]] | RETROCOT Jailbreak 回溯CoT越狱 / Retroactive CoT Jailbreak | 法医式逆向重建绕过对齐，GPT-4o ASR 0→58%，GPT-5 拒绝但一轮反馈即升至 85%。Forensic reconstruction jailbreak lifts GPT-4o ASR 0→58%; GPT-5 resists but feedback raises it to 85%. |

### 数学基础 / Mathematical Foundations

| Paper | Short Title 简称 | Key Contribution 核心贡献 |
|-------|------------------|---------------------------|
| [[2607.05381]] | Discrete Diffusion Theory 离散扩散理论 / What Discrete Diffusion Learns | 证明负 ELBO 减熵等于"神谕反向"到"所学反向"的路径 KL，统一 MDM/UDM/SEDD/GIDD。Proves NELBO−entropy = path KL from oracle to learned reverse; unifies MDM/UDM/SEDD/GIDD. |
| [[2607.04993]] | GD Dynamical System 梯度下降动力系统 / Finite-Step GD as Dynamics | 把稳定边界重定义为首次分岔，给出 Ricker 型大深度极限，学习率是结构性参数。Reframes edge-of-stability as first bifurcation; universal Ricker depth limit; LR selects representations. |
| [[2607.04627]] | PTMC Reliability 市场仿真可靠性 / Persona-Trained Monte Carlo Reliability | 为智能体市场仿真器建立统计可靠性理论，含 Lucas 批判的极小化界。Statistical reliability theory for agent-based market simulators; Lucas-critique minimax separation. |

### 计算可靠性 / Computation Reliability & Precision

| Paper | Short Title 简称 | Key Contribution 核心贡献 |
|-------|------------------|---------------------------|
| [[2607.04668]] | Elastic Gang 弹性帮派调度 / Per-Token Gang Membership | ACK-latch 历元协议让硬屏障 LLM 帮派在 token 间安全改变核心，输出比特级精确。ACK-latch epoch protocol lets hard-barriered LLM gang change core membership per-token, bit-exact. |
| [[2607.04819]] | SNLP-FHE 加密推理非线性深度 / Layer-Parallel Encrypted Inference | 结构化牛顿层并行把加密 Transformer 自举次数从 53 降到 20（2.65×），困惑度仅退化 1.2%。Structured Newton layer-parallelism cuts FHE bootstraps 53→20 (2.65×) at +1.2% perplexity. |
| [[2607.04562]] | HCRC Verification Gate 验证门控提交 / Heaviside Gate for Commits | Heaviside 门 + 非 LLM 检查池把合成软件合成任务的虚假完成率从 4–7% 压到 0%。Heaviside gate + non-LLM checker pool collapses false-completion rate 4–7%→0% on synthetic coding. |

---

## All Papers

| # | arxiv_id | Title | One-line Contribution (Bilingual) |
|---|----------|-------|-----------------------------------|
| 1 | [[2607.04562]] | Heaviside Continuity of Rolling Coefficients (HCRC) | 验证门控把 LLM 降为"提议者"，虚假完成率 4–7%→0%。Verification gate reduces LLM to proposer; FCR 4–7%→0%. |
| 2 | [[2607.04572]] | Detecting Answer-Driven Reasoning (Truncated CoT Audit) | 截断式 CoT 探针检测答案驱动推理，AUC 0.375→0.900。Truncated CoT probing detects answer-driven reasoning; AUC 0.375→0.900. |
| 3 | [[2607.04627]] | Reliability of Persona-Trained Monte Carlo (PTMC) | 智能体市场仿真器的统计可靠性理论 + Lucas 极小化界。Statistical reliability theory for agent market simulators + Lucas minimax bound. |
| 4 | [[2607.04640]] | Wrong Before Right: Late Rescue (Wrong-Dip) | 因果验证中层"先错后对"，预测结构化压缩但盲于量化。Causally verifies mid-layer wrong-dip; predicts structural compression but not quantization. |
| 5 | [[2607.04645]] | Retroactive Chain-of-Thought (RETROCOT) | 法医式逆向重建越狱，GPT-4o ASR 0→58%。Forensic-reconstruction jailbreak; GPT-4o ASR 0→58%. |
| 6 | [[2607.04668]] | Elastic Gang (Per-Token Gang Co-Scheduling) | 弹性帮派在 token 间安全换核，输出比特精确。Elastic gang changes cores per-token, bit-exact output. |
| 7 | [[2607.04681]] | VLA Faithfulness (Pinocchio) | 区分功能/忠实推理，GRPO+评判器提升忠实性。Separates functional/faithful reasoning; GRPO+critic lifts faithfulness. |
| 8 | [[2607.04683]] | Attributing VLM Errors (Attribution Tree) | 归因树分解 VQA 错误为四类，解码前预测并路由。Attribution tree decomposes VQA errors; pre-decoding routing. |
| 9 | [[2607.04686]] | ToolFailBench (Tool-Use Failure Diagnosis) | 参数化陷阱分离 4 类工具失败，同规模差 89 分。Parametric traps isolate 4 tool failures; 89pt same-scale gap. |
| 10 | [[2607.04728]] | SIS (Selective Importance Sampling) | 拒绝采样把 off-policy token 转 on-policy，~1%开销。Rejection sampling converts off-policy→on-policy, ~1% overhead. |
| 11 | [[2607.04800]] | Compressed Computation in Superposition (L4-CiS) | L2→L4 损失即涌现超叠加，逆向工程稀疏码+伪逆。L2→L4 loss elicits superposition; reverse-engineered code+pseudoinverse. |
| 12 | [[2607.04819]] | Layer-Parallel Encrypted Inference (SNLP-FHE) | 层并行把加密自举次数 53→20，困惑度退化 1.2%。Layer-parallel cuts FHE bootstraps 53→20, +1.2% PPL. |
| 13 | [[2607.04926]] | Few-Shot Binding in Tiny Transformers (MicroGround) | 全枚举证明零样本绑定全失败，少样本只看共享+可读性。Exhaustive study: zero-shot binding fails all paths; few-shot = sharing + readability. |
| 14 | [[2607.04969]] | Memorization-Guided Data Reuse | 记忆窗口框架定义重用安全区间，挑战 4-epoch 上限。Memorization window defines safe reuse interval; challenges 4-epoch limit. |
| 15 | [[2607.04993]] | Finite-Step GD as Dynamical System | 稳定边界即首次分岔，Ricker 大深度极限，学习率是结构参数。Edge-of-stability = first bifurcation; Ricker depth limit; LR is structural. |
| 16 | [[2607.05013]] | Knowledge vs. Verbalization (Math Solvability) | 两探针解耦知道/说出不可解，编造源于语言化偏移。Two probes disentangle know/say of unsolvability; fabrication = verbalization shift. |
| 17 | [[2607.05046]] | CollabEval (Matrix Completion Evaluation) | 评测建模为矩阵补全，CI 宽度缩窄 20–30%。Eval as matrix completion; CIs 20–30% narrower. |
| 18 | [[2607.05104]] | Grokking Is Conditional and Fragile | 仅改 CPU 线程数翻转 16% 同种子 grok 结果。Changing CPU threads flips 16% same-seed grok outcomes. |
| 19 | [[2607.05175]] | Platonic Projection Structures (PPS) | 算子核定义输出可解释性的结构性盲区。Operator kernel defines structural limits of output interpretability. |
| 20 | [[2607.05184]] | Rethinking On-Policy Self-Distillation (OPSD) | 特权自蒸馏翻转自纠错 token 优势，伤害思维模型。Privileged self-distillation flips self-correction advantage; harms thinking models. |
| 21 | [[2607.05188]] | Latent Programming Horizons in Coding Agents | 编码 agent 残差流线性解码程序正确性，前 25 步可预测。Coding-agent residual stream decodes correctness, predicts ~25 steps ahead. |
| 22 | [[2607.05198]] | Noisy-Channel MBR Decoding | MBR 打分分解为四概率通道，统一 5 种变体。Decomposes MBR into 4 channels; unifies 5 variants. |
| 23 | [[2607.05202]] | EvoAgentBench (Agent Ability Transfer) | 首个能力支撑迁移基准，揭示自动方法脆弱性。First ability-supported transfer benchmark; exposes auto-method brittleness. |
| 24 | [[2607.05297]] | MetaSkill-Evolve (Recursive Skill Evolution) | 双时间尺度递归进化 meta-skill，+23.5/+16.1。Two-timescale recursive meta-skill evolution; +23.5/+16.1. |
| 25 | [[2607.05316]] | LLMs Linearly Encode Output Length | 残差流线性解码剩余长度，回撤 token 处上调。Residual stream linearly decodes remaining length; shifts at retractions. |
| 26 | [[2607.05355]] | Faithfulness to Refusal (Neuron Selector Audit) | 选择器排名稳定性与因果有效性完全解离。Rank-stability ≠ causal-validity; refusal subspace redundant. |
| 27 | [[2607.05381]] | What Does a Discrete Diffusion Model Learn? | 负 ELBO−熵=路径 KL，统一离散扩散方法。NELBO−entropy = path KL; unifies discrete diffusion methods. |
| 28 | [[2607.05391]] | LLM-as-a-Verifier (General Verification) | logits 期望连续奖励，三轴缩放，四基准 SOTA。Logit-expectation continuous reward; 3-axis scaling; SOTA on 4 benchmarks. |
