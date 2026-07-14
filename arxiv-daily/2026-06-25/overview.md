---
title: "Daily arXiv Digest — 2026-06-25"
date: "2026-06-25"
tags:
  - mechanistic-interpretability
  - sparse-autoencoders
  - representation-geometry
  - autonomous-agents
  - rl-optimization
  - quantization
  - efficient-inference
  - llm-evaluation
  - hardware-systems
papers: 41
---

## 今日必读 / Must Read Today

### 1. [[2606.26836]] The Capability Frontier: Benchmarks Miss 82% of Model Performance

> **推荐理由 / Why read:** 传统单模型、单次运行的基准评测系统性低估了 LLM 的真实能力。作者提出经去偏的 quality-cost 帕累托前沿，在 21 个模型 × 16 个基准上证明仅纠正单模型偏差即可把错误率降低 54%，叠加单次采样纠正后达 82%，并以 85% 的成本匹配 SOTA。
> Standard single-model, single-run benchmarks systematically underestimate real-world LLM capability. Across 21 LLMs × 16 benchmarks, a debiased quality-cost Pareto frontier shows correcting single-model selection cuts error by 54% (82% when also correcting single-run sampling), matching SOTA accuracy at 85% lower cost. A landmark reframing of how we evaluate models.

### 2. [[2606.27091]] Inherited Circuits, Learned Semantics: How Fine-Tuning Creates Evasion Vulnerabilities Invisible to Standard Evaluation

> **推荐理由 / Why read:** 机制可解释性揭示安全微调的暗面——Foundation-Sec-8B 对恶意 PowerShell 的分类电路是继承自 Llama 的 Layer-12 注意力束，微调使其语义化却也引入了 Llama 没有的规避漏洞（别名/格式串重构/大小写变异全漏），并给出基于线性探针的部署前监控。
> Mechanistic interpretability exposes the dark side of safety fine-tuning: Foundation-Sec-8B's malicious-script classifier is an *inherited* Layer-12 circuit from Llama; fine-tuning specializes it but creates transformation-sensitive evasion misses (alias/format-string/case-mutation all evade) that the base model never suffers, plus a cheap pre-deployment probe monitor. High-impact for safety auditing.

### 3. [[2606.26749]] Structure Before Collapse: Transient Semantic Geometry in Next-Token Prediction

> **推荐理由 / Why read:** 揭示一个反直觉现象——严格 one-hot 监督下 Transformer 仍会在训练早期自发形成语义聚类几何，但该结构是短暂的，最终塌缩为神经坍塌理论预测的对称 ETF。调和了"神经坍塌抹除语义"与"语言模型显然学到语义"之间的张力。
> Reveals a counterintuitive phase transition: even under strict one-hot next-token supervision, transformers spontaneously form semantic, attribute-driven geometry early in training — but it is transient and eventually collapses to the symmetric, label-driven ETF geometry predicted by Neural Collapse theory. Reconciles a genuine tension between NC theory and observed semantic structure.

---

## 按主题分类 / Papers by Topic

### Interpretability & Mechanistic Analysis (SAEs, circuits, representation geometry) / 可解释性与机制分析

| Paper | 一句话 / One-liner |
|---|---|
| [[2606.26749]] Structure Before Collapse | One-hot 监督下早期形成短暂语义几何，最终塌缩为 NC 的对称 ETF；One-hot supervision yields transient semantic geometry that collapses to symmetric ETF. |
| [[2606.26474]] RL Tool Use = Single Crosscoder Feature | DFC 模型 diff 显示 RL 工具调用能力压缩到单个 A-exclusive 神经元（+65pp），无需重训；RL tool-use concentrates into one steerable A-exclusive feature (+65pp, zero retraining). |
| [[2606.26620]] Millions of Interpretable SAE Features | 发布 Qwen3-Instruct (1.7B/4B/8B) 的 JumpReLU SAE，残差流/MLP/注意力全覆盖，拒答引导推至 0.93–0.95；Releases Qwen3-Instruct JumpReLU SAEs across positions; refusal steering hits 0.93–0.95. |
| [[2606.26629]] SAE-Guided Activation Reg for Continual Learning | 在 SAE 单义特征空间做受限优化导出平方铰链损失，TRACE/MedCL 上为非架构方法最优；Regularize in pretrained SAE's monosemantic space → strongest non-architectural continual-learning result. |
| [[2606.26987]] Emotion Vectors in Open-Source LLMs | 将 Anthropic 情感向量复现到 Apertus-8B/Gemma-4B（效价 r=0.76/0.83），揭示不同的深度构建路径；Replicates Anthropic emotion vectors in open-weight LLMs (valence r=0.76/0.83) with divergent depth profiles. |
| [[2606.27199]] Forecasting via SAE Feature Steering | 放大时间感知 SAE 特征可因果降低前瞻偏差而保通用推理；Amplifying time-awareness SAE features causally cuts look-ahead bias while preserving general reasoning. |
| [[2606.27091]] Inherited Circuits Evasion Vulnerabilities | 继承自 Llama 的 Layer-12 电路经微调语义化，引入标准评测不可见的规避漏洞；Inherited Llama circuit is specialized by fine-tuning, creating evasion gaps invisible to standard eval. |
| [[2606.26935]] Where Do CoT Training Gains Land? | CoT 训练主要提升 prompt-action 质量而非放大推理优势，后期更少依赖 CoT；CoT training mainly improves prompt-action quality, not reasoning advantage; later checkpoints rely less on CoT. |
| [[2606.26982]] Framing-Sensitive Behavioral Instability | 非对抗性语境框架系统性改变心理健康 LLM 路由倾向，可逐层探针解码并由 CAA 干预；Non-adversarial framings systematically shift mental-health LLM routing, decodable by probes, partly steerable. |
| [[2606.26502]] Humans Disengage, Reasoning Models Persist | 人类答错即放弃，推理模型答错反而拉长（Cohen's d 1.47–3.13），揭示相反停止策略；Humans abandon failed trials; reasoning models lengthen them (d=1.47–3.13) — opposite stopping rules. |
| [[2606.26523]] Radical AI Interpretability | 哲学专著，把激进解释传统(Lewis/Davidson)映射到机制可解释性，给出信念/欲望归赋标准；Philosophy monograph mapping radical interpretation to mechanistic interpretability, with belief/desire attribution criteria. |

### Autonomous Research & Self-Evolving Agents / 自主研究与自进化智能体

| Paper | 一句话 / One-liner |
|---|---|
| [[2606.26722]] AHOIS Socratic Agents | 苏格拉底诘问嵌入闭环物理实验，在多模光纤平台自主发现随机干涉编码假设；Embeds Socratic midwifery into closed-loop physics experiments; autonomously discovers random-interference encoding hypothesis on a multimode-fibre rig. |
| [[2606.26728]] Scientific Discovery as Meta-Optimization | 共识目标聚合机制把 3-SAT MemComputing 求解器标度从 N^2.51 降到 N^1.33（最大 67×）；Consensus objective aggregation cuts 3-SAT solver scaling N^2.51→N^1.33 (~67× on largest instance). |
| [[2606.26578]] EvoOptiGraph Weakness-Driven Coevolution | 图演化+弱点向量驱动数据-模型协同进化，8B 在六个 OR 基准达 78.1% 超越 72B；Graph evolution + weakness-vector coevolution lets an 8B model hit 78.1% Pass@1, beating 72B generalists. |
| [[2606.26806]] Memory Depth vs Memory Access | 区分"记忆访问"与"记忆深度"，EVAF 实现目标持久性而 RAG 擅长浅层事实；Separates retrieval (access) from durable parametric tendencies (depth); EVAF wins goal persistence vs RAG's shallow recall. |
| [[2606.26511]] MemStrata Temporal Validity Memory | 确定性 (s,p,o) 替代规则退役过时事实，把 RAG 的 15–40% 过时错误率降至约 0%；Deterministic supersession retires stale facts, dropping RAG's 15–40% stale-fact error rate to ~0%. |
| [[2606.27009]] Semantic Early-Stopping Agent Loops | 草稿 embedding 距离稳态即停，零判断开销变体省 38% 算力且质量持平；Stop when draft embeddings stabilize; judge-free variant saves 38% tokens at parity quality. |

### Training Stability & RL Optimization / 训练稳定性与强化学习优化

| Paper | 一句话 / One-liner |
|---|---|
| [[2606.26917]] GEOALIGN Geometric Rollout Curation | 检测"方向不一致"高奖励 rollout 并替换，稳定在线 RL 且对奖励噪声更鲁棒；Detects directionally inconsistent high-reward rollouts and rectifies them, stabilizing online RL and adding reward-noise robustness. |
| [[2606.26671]] NebulaExp-8B Post-Training Ablation | 全透明消融流水线，揭示数据正确性过滤是一阶因子，4K OPD 在 IFEval 超 RL；Transparent ablation pipeline: correctness filtering is first-order; 4K on-policy distillation beats RL on IFEval. |
| [[2606.26797]] Reasoning Quality Emerges Early (TEMP) | 仅用轨迹开头 100–1k token 的扰动损失信号即可挑高质量 SFT 数据，token 效率+91%；Difficulty/diversity detectable from first 100–1k tokens via perturbed-checkpoint loss; +91% token efficiency. |
| [[2606.26466]] SOLAR Cross-Lingual Soft-Token Alignment | 软 token 余弦对齐把英语作锚点，四个多语言基准平均 +3.8 准确率，低资源语言增益最大；Soft-token cosine alignment to English anchor: +3.8 avg accuracy across 4 multilingual benchmarks, largest gains on low-resource languages. |

### Quantization & Efficient Inference / 量化与高效推理

| Paper | 一句话 / One-liner |
|---|---|
| [[2606.26587]] SharQ Sparsity + FP4 | 训练无关的稀疏-稠密分解补偿量化误差，恢复 43–63% 精度差距，RTX 5090 上 2.2–2.4× 加速；Training-free sparse-dense decomposition recovers 43–63% of FP4 accuracy gap; 2.2–2.4× speedup on RTX 5090. |
| [[2606.26650]] CAT-Q Ternary Quantization | LM+ST 后训练三值化，512 样本压 1.7B–235B，超越 100B-token 训练的 BitNet；Post-training ternarization with 512 samples scales to 235B and beats BitNet trained on 100B tokens. |
| [[2606.26744]] HyperDFlash Speculative Decoding | MHC 对齐三项优化让 DeepSeek-V4 块并行投机解码接受长度 3.69、加速 2.80×；MHC-aligned optimizations lift DeepSeek-V4 block-parallel speculative decoding to 3.69 accepted length / 2.80× speedup. |
| [[2606.26488]] Recursive Reasoner Compression | 量化误差跨递归周期累积致全局坍塌；INT8+flash 在 8MB SoC 以 1/6 FLOPs 匹配全精度；Quantization noise compounds across recursive cycles; INT8+flash matches FP32 at 6× fewer FLOPs on an 8 MB SoC. |
| [[2606.26822]] Quantization in Federated Learning (Survey) | 首个 FL 为中心、PRISMA 量化综述，把量化定位为塑造 FL 的基础系统组件；First FL-centric PRISMA survey positioning quantization as a foundational FL systems component. |
| [[2606.26472]] EpiKV Attention-Free Cache Eviction | 读隐藏状态"顿悟分数"驱逐 KV cache，兼容 FlashAttention，上下文长 16×；Hidden-state "epiphany score" evicts KV cache without the attention matrix; 16× longer feasible context. |
| [[2606.26875]] InfoKV Cache Compression | 用预测熵+跨层演化作信息论信号，高熵 token 主导远期影响，持续超注意力基线；Predictive entropy + cross-layer evolution as info-theoretic signals; high-entropy tokens dominate long-range influence, beating attention baselines. |

### Evaluation & Reliability / 评测与可靠性

| Paper | 一句话 / One-liner |
|---|---|
| [[2606.26836]] Capability Frontier | 去偏帕累托前沿揭示基准低估 82% 能力，纠正后可 85% 成本匹配 SOTA；Debiased Pareto frontier shows benchmarks miss 82% of performance; matches SOTA at 85% lower cost. |
| [[2606.26783]] AlphaEdit Reproducibility Study | 概率指标可复现但零空间保护在新架构失效、5000 次编辑后崩溃、损害安全拒绝；Probability metrics reproduce, but null-space protection fails on new architectures, breaks past ~5000 edits, and degrades safety refusals. |
| [[2606.26492]] DL Fault Diagnosis Eval Gap | 程序内 vs 留程序评估存在 0.190 平衡准确率鸿沟，曲率特征可跨程序迁移；0.190 balanced-accuracy gap between within-program and held-out evaluation; curvature features transfer across programs. |
| [[2606.27023]] Medical VQA Verbalized Calibration | 2×2 因子扰动+复合损失做 LoRA 校准，同时降 ECE/Brier 并升 AUROC；LoRA calibration via 2×2 perturbation + composite loss lowers ECE/Brier while raising AUROC across 3 medical-VQA benchmarks. |
| [[2606.26585]] Telescope Scheduling Validation | 多层级验证+原子推理单元表示，在执行前校验 AI 调度可靠性；Multi-level validation with atomic reasoning units verifies AI telescope-scheduling decisions before execution. |
| [[2606.27226]] BINEVAL Binary-Question Evaluation | 原子化二元问题替代不透明整体评分，提升评估可解释性与区分度，形成"评估—改进"闭环；Atomic binary questions replace opaque holistic scoring, improving interpretability and discrimination, closing the evaluate-improve loop. |

### Hardware & Systems / 硬件与系统

| Paper | 一句话 / One-liner |
|---|---|
| [[2606.27153]] DMuon Distributed Optimizer | 把 Muon 的 Newton-Schulz 开销压缩到近 AdamW，端到端提速 1.48–3.01×；Compresses Muon's Newton-Schulz overhead to near-AdamW latency; 1.48–3.01× end-to-end speedup. |
| [[2606.27216]] Hierarchical Muon (HiMuon) | 分块 Newton-Schulz 把每步开销从 O(r²sK) 降到 O(HWTK) 并提升并行；Tiles Newton-Schulz updates, cutting per-step work O(r²sK)→O(HWTK) with better parallelism. |
| [[2606.26997]] RolloutPipe RLVR Pipelining | CGP+FGD 重叠 rollout 与训练，把 rollout-to-train 时间缩短 30.7–42.3%；Complete-group pipelining overlaps rollout and training in disaggregated RLVR, cutting time 30.7–42.3%. |
| [[2606.27098]] Apple M4 Pro GPU Cache State | GPU 大足迹后首次 CPU 访问变慢，二次访问即恢复，证明是缓存挤占；First CPU traversal after a large-footprint GPU kernel slows down; a second traversal recovers — shared-cache displacement. |
| [[2606.26701]] SegFold Sparse GEMM | Segment 动态数据流让 SpGEMM 加速器较 Spada 提升 1.95×；Segment dynamic dataflow gives the SpGEMM accelerator 1.95× geomean speedup over Spada. |
| [[2606.26666]] PersistentKV Page-Aware Decode | 原生块表 GQA decode 引擎+页感知调度，在 RTX 3060 上 1.063–1.399× 超过 FlashInfer；Native block-table GQA decode engine + page-aware scheduler beats FlashInfer 1.063–1.399× on RTX 3060. |
| [[2606.26547]] ApproxHDC Approximation Tuning | 编译器自动搜索 HDC 软件/硬件近似配置，可重定向到 CPU/GPU/ReRAM/PCM；Compiler auto-tunes HDC software/hardware approximations, retargeting to CPU/GPU/ReRAM/PCM. |

---

## All Papers

| arxiv_id | Title | Topic |
|---|---|---|
| [[2606.26466]] | SOLAR: Soft Token Alignment for Cross-Lingual Reasoning | RL & Training |
| [[2606.26472]] | EpiKV: Attention-Free KV Cache Eviction | Quantization & Inference |
| [[2606.26474]] | RL Tool Use Localized to a Single Crosscoder Feature | Interpretability |
| [[2606.26488]] | Compressing a Recursive Reasoner for the Edge | Quantization & Inference |
| [[2606.26492]] | Evaluation-Strategy Gap in DL Fault Diagnosis | Evaluation & Reliability |
| [[2606.26502]] | Humans Disengage, Reasoning Models Persist | Interpretability |
| [[2606.26511]] | MemStrata: Temporal Validity Memory for Agents | Autonomous Agents |
| [[2606.26523]] | Radical AI Interpretability (philosophy) | Interpretability |
| [[2606.26547]] | ApproxHDC: Approximation Tuning for HDC | Hardware & Systems |
| [[2606.26578]] | EvoOptiGraph: Weakness-Driven Coevolution | Autonomous Agents |
| [[2606.26585]] | Validation for AI Telescope Scheduling | Evaluation & Reliability |
| [[2606.26587]] | SharQ: Sparsity + FP4 Quantization | Quantization & Inference |
| [[2606.26620]] | Millions of Interpretable SAE Features (Qwen3) | Interpretability |
| [[2606.26629]] | SAE-Guided Activation Reg for Continual Learning | Interpretability |
| [[2606.26650]] | CAT-Q: Ternary Quantization for LLMs | Quantization & Inference |
| [[2606.26666]] | PersistentKV: Page-Aware Decode Scheduling | Hardware & Systems |
| [[2606.26671]] | NebulaExp-8B: Post-Training Ablation | RL & Training |
| [[2606.26701]] | SegFold: Sparse GEMM Dynamic Dataflow | Hardware & Systems |
| [[2606.26722]] | AHOIS: Socratic Agents for Discovery | Autonomous Agents |
| [[2606.26728]] | Scientific Discovery as Meta-Optimization | Autonomous Agents |
| [[2606.26744]] | HyperDFlash: Block Speculative Decoding | Quantization & Inference |
| [[2606.26749]] | Transient Semantic Geometry in Next-Token | Interpretability |
| [[2606.26783]] | AlphaEdit Reproducibility Study | Evaluation & Reliability |
| [[2606.26797]] | Reasoning Quality Emerges Early (TEMP) | RL & Training |
| [[2606.26806]] | Memory Depth: Selective Parametric Consolidation | Autonomous Agents |
| [[2606.26822]] | Quantization in Federated Learning (Survey) | Quantization & Inference |
| [[2606.26836]] | Capability Frontier: Benchmarks Miss 82% | Evaluation & Reliability |
| [[2606.26875]] | InfoKV: Information-Aware Cache Compression | Quantization & Inference |
| [[2606.26917]] | GEOALIGN: Geometric Rollout Curation for RL | RL & Training |
| [[2606.26935]] | Where Do CoT Training Gains Land? | Interpretability |
| [[2606.26982]] | Framing-Sensitive Behavioral Instability | Interpretability |
| [[2606.26987]] | Emotion Vectors in Open-Source LLMs | Interpretability |
| [[2606.26997]] | RolloutPipe: Pipelined Rollout & Training | Hardware & Systems |
| [[2606.27009]] | Semantic Early-Stopping Agent Loops | Autonomous Agents |
| [[2606.27023]] | Verbalized Uncertainty Calibration (Med VQA) | Evaluation & Reliability |
| [[2606.27091]] | Inherited Circuits Evasion Vulnerabilities | Interpretability |
| [[2606.27098]] | Residual GPU Cache State on Apple M4 Pro | Hardware & Systems |
| [[2606.27153]] | DMuon: Distributed Muon Training | Hardware & Systems |
| [[2606.27199]] | Forecasting via SAE Feature Steering | Interpretability |
| [[2606.27216]] | Hierarchical Muon: Tiled Newton-Schulz | Hardware & Systems |
| [[2606.27226]] | BINEVAL: Binary Questions for Evaluation | Evaluation & Reliability |

---

**Paper count verification / 论文计数核对:** Overview lists **41** papers; the directory contains **41** `.md` files (excluding `overview.md` itself). Counts match — no discrepancy.
