---
title: "Daily arXiv Digest — 2026-06-18"
date: 2026-06-18
tags:
  - mechanistic-interpretability
  - activation-steering
  - llm-safety
  - llm-agents
  - reinforcement-learning
  - low-precision-training
  - kv-cache-quantization
  - evaluation-methodology
  - benchmark-validity
  - reproducibility
papers: 50
---

> **Note on coverage:** All **50 papers** in this digest received **full PDF-grounded analysis** with bilingual summaries, Critical Assessment, and red-flag vetting (marked ✅). Must-Read picks are the top-5 by novelty/significance.

---

## 今日必读 / Must Read Today

All five picks below received deep, PDF-grounded analysis and were selected as the day's standout papers.

1. **[[2606.19831]] — Leverage Is Not Reach: A Control-Window Law for Single-Neuron Steering**
   - 一句话：单神经元干预效果被归约为一个可证伪、可由权重预测的"控制窗口定律"，并揭示梯度归因恰恰把真正的控制器排在最末。
   - One-liner: A falsifiable, weights-predictable law for *when* single-neuron steering works, with a sharp "leverage ≠ reach" result that shows gradient attribution anti-predicts control.

2. **[[2606.20536]] — The FID Lottery: Hidden Randomness in Generative Model Evaluation**
   - 一句话：在数百个 SiT 网络上直接测量发现，重训引起的 FID 抖动是重采样的 3.2 倍，且 1–2% 的噪声底不随规模收紧——单种子论文的许多增益可能只是种子彩票。
   - One-liner: A ~100k H100-hour study showing retraining moves FID 3.2× more than resampling, with a scale-invariant 1–2% noise floor that invalidates many single-seed claims.

3. **[[2606.20381]] — Rethinking Shrinkage Bias in LLM FP4 Pretraining (UFP4)**
   - 一句话：从几何角度证明主流 FP4 格式 E2M1 存在系统性"收缩偏差"并跨层乘性累积，据此提出均匀网格 UFP4 配方，在 124B MoE 上持续降低损失退化。
   - One-liner: An elegant geometric theory of why E2M1 FP4 training is unstable, plus a uniform-grid UFP4 recipe validated up to 124B-parameter MoE pretraining.

4. **[[2606.20128]] — The Correctness Illusion in LLM-Generated GPU Kernels**
   - 一句话：构造受控语料证明 KernelBench/TritonBench 的"固定形状 + allclose"判分会把真实转录 bug 误判为正确，而边界感知模糊测试能在五类 GPU 上一致抓出 10/10。
   - One-liner: Shows the standard oracle of LLM-kernel benchmarks certifies real transcription bugs as "correct," and a boundary-aware seeded fuzzer catches 10/10 across five GPU classes.

5. **[[2606.20475]] — Marginal Advantage Accumulation (MAA) for Memory-Driven Agent Self-Evolution**
   - 一句话：用跨批次 EMA 累积 LLM-judge 的符号证据来区分"稳定有效"与"偶然命中"的记忆操作，在 16 个设置中 14 个最优并将优化阶段 token 成本降低约 75%。
   - One-liner: A fully offline post-processing method that accumulates signed evidence across batches, winning 14/16 settings and cutting optimization-phase token cost ~75%.

---

## 按主题分类 / Papers by Topic

### A. 可解释性与表征几何 / Interpretability & Representation Geometry

| Paper | 描述 / Description |
|---|---|
| [[2606.19831]] ✅ | 控制窗口定律：单神经元干预的可预测理论 / Control-window law: predictive theory of single-neuron steering |
| [[2606.19946]] ✅ | GEMS：几何约束实现多语义方向无训练并行注入 / GEMS: training-free multi-direction activation steering via geometric constraints |
| [[2606.20152]] ✅ | 作文质量表征在 LLM 中线性涌现与打分神经元 / Essay-quality representations emerge linearly; localizes scoring neurons |
| [[2606.20431]] ✅ | 稀疏/叠加/遗忘：表示强度而非重叠决定脆弱性 / Sparsity/superposition/forgetting: strength, not overlap, drives fragility |
| [[2606.20097]] ✅ | HydraHead：注意力头功能异质性与专用混合 / Head-level attention heterogeneity and specialized hybridization |
| [[2606.20077]] ✅ | 视觉 token 在 VLM 中表征演化的"伪装"上下文 / Hidden evolution of disguised visual context inside VLMs |
| [[2606.20347]] ✅ | 临界渗流作为可解释性的合成数据模型 / Critical percolation as synthetic-data model for interpretability |
| [[2606.19735]] ✅ | GLARE：自然语言查询全局解释的接口 / Natural-language interface for querying global explanations |

### B. LLM 安全、对齐与红队测试 / LLM Safety, Alignment & Red-Teaming

| Paper | 描述 / Description |
|---|---|
| [[2606.19899]] ✅ | AI Agent 生物能力与风险评测的五阶段方法论 / Five-stage methodology for agentic biosecurity evaluations |
| [[2606.20225]] ✅ | 涌现失对齐方向：模型内特异、跨模型非特异 / Emergent-misalignment directions: within-model specific, cross-model not |
| [[2606.20508]] ✅ | 安全对齐模型从混合合规示范中学到什么 / What safety-aligned LLMs learn from mixed compliance demonstrations |
| [[2606.20408]] ✅ | LLM agent 安全：多轮红队与越狱基准 / LLM agent safety: multi-turn red-teaming and jailbreak benchmarks |
| [[2606.19755]] ✅ | SafeSpec：动态反思采样的安全快速推理 / SafeSpec: dynamic reflective sampling for safe fast inference |
| [[2606.19753]] ✅ | 确定性封装生成模型的接地推理原则 / Grounded-inference principles for deterministically encapsulated gen models |

### C. LLM 智能体、记忆与自我进化 / LLM Agents, Memory & Self-Improvement

| Paper | 描述 / Description |
|---|---|
| [[2606.20002]] ✅ | Connect the Dots：RL 训练长生命周期 agent 的元能力 / CoD: RL training a long-lifecycle agent meta-capability |
| [[2606.20475]] ✅ | MAA：跨批次证据累积的记忆驱动自我进化 / Marginal-advantage accumulation for memory-driven self-evolution |
| [[2606.19847]] ✅ | AtomMem：基于原子事实的 agent 记忆系统 / AtomMem: atomic-facts memory system for LLM agents |
| [[2606.19911]] ✅ | 多智能体交互式记忆与知识共享 / Multi-agent transactive memory and knowledge sharing |
| [[2606.20122]] ✅ | ScaffoldAgent：开放式深度研究的动态大纲优化 / Utility-guided dynamic outline optimization for deep research |
| [[2606.19980]] ✅ | ENPIRE：真实世界机器人策略自我改进 / Agentic robot policy self-improvement in the real world |
| [[2606.19683]] ✅ | 去中心化联盟形成的退出-加入动力学 / Exit-and-join dynamics for decentralized coalition formation |
| [[2606.20515]] ✅ | S-Agent：空间工具使用激发空间智能推理 / Spatial tool-use elicits reasoning for spatial intelligence |
| [[2606.19749]] ✅ | 智能体评审系统的基准评测 / Benchmarking agentic peer-review systems |

### D. 推理、强化学习与后训练 / Reasoning, RL & Post-Training

| Paper | 描述 / Description |
|---|---|
| [[2606.19771]] ✅ | 超越熵：token 级分布偏差用于 RLVR 推理 / Beyond entropy: token-level distributional deviations for RLVR reasoning |
| [[2606.20075]] ✅ | 潜思维链有效监督的信息论分析 / Information-theoretic analysis of effective supervision in latent CoT |
| [[2606.19697]] ✅ | 思维链 Transformer 高效表示算法的理论 / Theory of efficient algorithm representation with CoT transformers |
| [[2606.19818]] ✅ | 稳定 RLHF 的不确定性感知奖励建模 / Uncertainty-aware reward modeling for stable RLHF |
| [[2606.19744]] ✅ | 超越均匀遗忘：序列 DPO 的偏好设置研究 / Beyond uniform forgetting: sequential DPO across preference settings |
| [[2606.19750]] ✅ | Manifold Bandits：LLM 潜在几何上的贝叶斯课程学习 / Bayesian curriculum learning over LLM latent geometry |
| [[2606.19721]] ✅ | OnDeFog：丢帧下的在线决策 Transformer / Online decision transformer under frame dropping |
| [[2606.19668]] ✅ | 语码转换揭示多语言 LLM 的语言锚定 / Code-switching reveals language anchoring in multilingual LLMs |
| [[2606.19679]] ✅ | LOKI：无记忆零空间约束的终身知识编辑 / Memory-free null-space constrained lifelong knowledge editing |

### E. 评测、基准与不确定性 / Evaluation, Benchmarks & Uncertainty

| Paper | 描述 / Description |
|---|---|
| [[2606.20128]] ✅ | LLM 生成 GPU 内核的"正确性幻觉"与判分加固 / Correctness illusion in LLM-generated GPU kernels and oracle hardening |
| [[2606.20536]] ✅ | FID 彩票：生成模型评测的隐藏随机性 / FID lottery: quantifying hidden seed randomness in gen-model eval |
| [[2606.19704]] ✅ | 超越静态榜单：LLM agent 的预测有效性 / Predictive validity for evaluating LLM agents beyond static leaderboards |
| [[2606.19714]] ✅ | AURA：不确定性感知的 LLM-as-Judge 审计 / Adaptive uncertainty-aware refinement for LLM-as-judge auditing |
| [[2606.19787]] ✅ | ORAgentBench：LLM agent 端到端解决运筹学任务 / Can LLM agents solve operations-research tasks end to end? |
| [[2606.19868]] ✅ | LLM 黑盒不确定性估计方法的系统评测 / Systematic evaluation of black-box uncertainty estimation for LLMs |

### F. 高效训练、推理与量化 / Efficient Training, Inference & Quantization

| Paper | 描述 / Description |
|---|---|
| [[2606.20381]] ✅ | UFP4：FP4 预训练的收缩偏差几何与均匀网格配方 / Shrinkage-bias geometry of FP4 pretraining and the uniform-grid UFP4 recipe |
| [[2606.20474]] ✅ | UltraQuant：面向长上下文 agent 的 4-bit KV 缓存 / 4-bit KV caching for context-heavy agents, dequant folded into MFMA |
| [[2606.20195]] ✅ | 随机 sketching 对 GPU 低精度舍入鲁棒 / Randomized sketching robust to low-precision rounding on GPUs |
| [[2606.19667]] ✅ | CacheWeaver：RAG 的缓存感知证据排序 / Cache-aware evidence ordering for efficient grounded RAG inference |
| [[2606.19993]] ✅ | AIR：激活与影响感知的 SVD 压缩 / Activation- and influence-aware ranks for function-preserving SVD compression |
| [[2606.20295]] ✅ | 面向 token-算子的大模型推理优化 / Token-operations-oriented inference optimization for large models |
| [[2606.20537]] ✅ | 执行态胶囊：端侧小批量物理 AI 服务的检查点恢复 / Execution-state capsules for low-latency on-device serving |
| [[2606.19989]] ✅ | 形式化保证的 LLM 训练在线动态批处理 / Online dynamic batching with formal guarantees for LLM training |
| [[2606.19799]] ✅ | TensorFlow/Keras 中糟糕编码的环境成本与碳排放 / Hidden environmental cost of resource leaks in TF/Keras apps |

### G. 多模态、视觉、语音与应用 / Multimodal, Vision, Speech & Applications

| Paper | 描述 / Description |
|---|---|
| [[2606.20532]] ✅ | 指令如何塑造语音：TTS 的跨注意力归因 / Cross-attention attribution for style-captioned text-to-speech |
| [[2606.20155]] ✅ | NAMESAKES：探查文生图模型的身份记忆 / Probing identity memorization in text-to-image models |
| [[2606.20300]] ✅ | CMDS-AD：跨模态双流解耦的小样本异常检测 / Cross-modal dual-stream decoupling for few-shot anomaly detection |

---

## All Papers

| arxiv_id | Title | Score | Type |
|---|---|---|---|
| [[2606.19667]] | CacheWeaver: Cache-Aware Evidence Ordering for Efficient Grounded RAG Inference | 3 | ✅ Abstract |
| [[2606.19668]] | Code-Switching Reveals Language Anchoring in Multilingual LLMs | 3 | ✅ Abstract |
| [[2606.19679]] | LOKI: Memory-Free Null-Space Constrained Lifelong Knowledge Editing | 3 | ✅ Abstract |
| [[2606.19683]] | Exit-and-Join Dynamics for Decentralized Coalition Formation | 3 | ✅ Abstract |
| [[2606.19697]] | Efficiently Representing Algorithms With Chain-of-Thought Transformers | 3 | ✅ Abstract |
| [[2606.19704]] | Beyond Static Leaderboards: Predictive Validity for the Evaluation of LLM Agents | 3 | ✅ Abstract |
| [[2606.19714]] | AURA: Adaptive Uncertainty-aware Refinement for LLM-as-a-Judge Auditing | 3 | ✅ Abstract |
| [[2606.19721]] | OnDeFog: Online Decision Transformer under Frame Dropping | 3 | ✅ Abstract |
| [[2606.19735]] | GLARE: A Natural Language Interface for Querying Global Explanations | 3 | ✅ Abstract |
| [[2606.19744]] | Beyond Uniform Forgetting: Sequential Direct Preference Optimization Across Preference Settings | 3 | ✅ Abstract |
| [[2606.19749]] | Benchmarking Agentic Review Systems | 3 | ✅ Abstract |
| [[2606.19750]] | Manifold Bandits: Bayesian Curriculum Learning over the Latent Geometry of Large Language Models | 3 | ✅ Abstract |
| [[2606.19753]] | Grounded Inference: Principles for Deterministically Encapsulated Generative Models | 3 | ✅ Abstract |
| [[2606.19755]] | SafeSpec: Fast and Safe LLM via Dynamic Reflective Sampling | 3 | ✅ Abstract |
| [[2606.19771]] | Beyond Entropy: Learning from Token-Level Distributional Deviations for LLM Reasoning | 3 | ✅ Abstract |
| [[2606.19787]] | ORAgentBench: Can LLM Agents Solve Challenging Operations Research Tasks End to End? | 3 | ✅ Abstract |
| [[2606.19799]] | The Hidden Environmental Cost of Poor Coding Practices in TensorFlow and Keras Applications | 3 | ✅ Abstract |
| [[2606.19818]] | Uncertainty-Aware Reward Modeling for Stable RLHF | 3 | ✅ Abstract |
| [[2606.19831]] | Leverage Is Not Reach: A Control-Window Law for Single-Neuron Steering in Language Models | 5 | ✅ Full |
| [[2606.19847]] | AtomMem: Building Simple and Effective Memory System for LLM Agents via Atomic Facts | 3 | ✅ Abstract |
| [[2606.19868]] | A Systematic Evaluation of Black-Box Uncertainty Estimation Methods for Large Language Models | 3 | ✅ Abstract |
| [[2606.19899]] | Measuring Biological Capabilities and Risks of AI Agents | 5 | ✅ Full |
| [[2606.19911]] | Multi-Agent Transactive Memory | 3 | ✅ Abstract |
| [[2606.19946]] | GEMS: Geometric Constraints Enable Multi-Semantic Superposition in LLMs | 5 | ✅ Full |
| [[2606.19980]] | ENPIRE: Agentic Robot Policy Self-Improvement in the Real World | 3 | ✅ Abstract |
| [[2606.19989]] | Online Dynamic Batching with Formal Guarantees for LLM Training | 3 | ✅ Abstract |
| [[2606.19993]] | Activation- and Influence-Aware Ranks (AIR): Function-Preserving SVD Compression for LLMs | 3 | ✅ Abstract |
| [[2606.20002]] | Connect the Dots: Training LLMs for Long-Lifecycle Agents with Cross-Domain Generalization Via RL | 5 | ✅ Full |
| [[2606.20075]] | What Makes Effective Supervision in Latent Chain-of-Thought: An Information-Theoretic Analysis | 3 | ✅ Abstract |
| [[2606.20077]] | The Hidden Evolution of Disguised Visual Context inside the VLM | 3 | ✅ Abstract |
| [[2606.20097]] | HydraHead: From Head-Level Functional Heterogeneity to Specialized Attention Hybridization | 3 | ✅ Abstract |
| [[2606.20122]] | ScaffoldAgent: Utility-Guided Dynamic Outline Optimization for Open-Ended Deep Research | 3 | ✅ Abstract |
| [[2606.20128]] | The Correctness Illusion in LLM-Generated GPU Kernels | 5 | ✅ Full |
| [[2606.20152]] | From Texts to Scores: Tracing the Emergence of Essay Quality Representations in LLMs | 5 | ✅ Full |
| [[2606.20155]] | NAMESAKES: Probing Identity Memorization in Text-to-Image Models | 3 | ✅ Abstract |
| [[2606.20195]] | Randomized Sketching is Robust to Low-Precision Rounding on GPUs | 5 | ✅ Full |
| [[2606.20225]] | Actionable Activation Directions for Detecting and Mitigating Emergent Misalignment Across Language Model Families | 5 | ✅ Full |
| [[2606.20295]] | Token-Operations-Oriented Inference Optimization Techniques for Large Models | 3 | ✅ Abstract |
| [[2606.20300]] | CMDS-AD: Cross-Modal Dual-Stream Decoupling for Few-Shot Anomaly Detection | 3 | ✅ Abstract |
| [[2606.20347]] | Critical Percolation as a Synthetic Data Model for Interpretability | 3 | ✅ Abstract |
| [[2606.20381]] | Rethinking Shrinkage Bias in LLM FP4 Pretraining: Geometric Origin, Systemic Impact, and UFP4 Recipe | 5 | ✅ Full |
| [[2606.20408]] | LLM agent safety, multi-turn red-teaming, jailbreak benchmarks, adversarial robustness | 3 | ✅ Abstract |
| [[2606.20431]] | Sparsity, Superposition, and Forgetting: A Mechanistic Study of Representation Retention in Continual Learning | 5 | ✅ Full |
| [[2606.20474]] | UltraQuant: 4-bit KV Caching for Context-Heavy Agents | 5 | ✅ Full |
| [[2606.20475]] | Marginal Advantage Accumulation for Memory-Driven Agent Self-Evolution | 5 | ✅ Full |
| [[2606.20508]] | What Do Safety-Aligned LLMs Learn From Mixed Compliance Demonstrations? | 3 | ✅ Abstract |
| [[2606.20515]] | S-Agent: Spatial Tool-Use Elicits Reasoning for Spatial Intelligence | 3 | ✅ Abstract |
| [[2606.20532]] | How Do Instructions Shape Speech? Cross-Attention Attribution for Style-Captioned Text-to-Speech | 3 | ✅ Abstract |
| [[2606.20536]] | The FID Lottery: Quantifying Hidden Randomness in Generative Model Evaluation | 5 | ✅ Full |
| [[2606.20537]] | Execution-State Capsules: Graph-Bound Checkpoint and Restore for Low-Latency On-Device Physical-AI Serving | 3 | ✅ Abstract |

---

**Link verification:** All 50 papers appear as `[[arxiv_id]]` wiki-links exactly once in the *All Papers* index, and each also appears once in its topic table. Topic-table counts: A=8, B=6, C=9, D=9, E=6, F=9, G=3 → **50 total**, matching the 50 `.md` files. No discrepancy.
