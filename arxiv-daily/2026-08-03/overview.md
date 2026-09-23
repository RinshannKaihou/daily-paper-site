---
title: "Daily ArXiv Digest — 2026-08-03"
date: 2026-08-03
tags:
  - llm-evaluation
  - mechanistic-interpretability
  - llm-agents
  - post-training
  - safety
  - reasoning
  - efficient-inference
  - representation-geometry
papers: 50
---

# Daily ArXiv Digest — 2026-08-03

本日共筛选出 50 篇与 LLM 评估、机制可解释性、智能体、后训练、推理可信度、高效推理、表示几何等核心方向相关的论文。/ Today's digest covers 50 papers selected for relevance to LLM evaluation, mechanistic interpretability, agents, post-training, reasoning faithfulness, efficient inference, and representation geometry.

## 今日必读 / Must Read Today

### 1. [[2608.01575]] — F-ICL: Bayes-Optimal ICL Benchmark / 精确贝叶斯最优 ICL 基准

**推荐理由 / Why read:** 作者用一个极小但图灵完备的磁带机穷举 1.5 亿条程序，闭式计算 ICL 的精确贝叶斯最优后验，并据此在 46 个开源/前沿模型上揭示"答对 ≠ 按最优后验推"。该论文提出了"后验保真度（posterior fidelity）"这一与准确率正交的新评测轴，且系统性记录了 API 不可复现、安全层干预打分等可靠性问题，对衡量 LLM 算法推理的真实性具有突破性意义。
The authors exhaustively enumerate 1.5e9 programs of a minimal Turing-complete machine and compute the closed-form Bayes-optimal ICL posterior, then show on 46 open/frontier models that "answering correctly ≠ reasoning according to the optimal posterior." Posterior fidelity is a new evaluation axis orthogonal to accuracy, and the paper documents API non-reproducibility and safety-filter interference — a landmark for LLM reasoning evaluation.

### 2. [[2608.01631]] — Answer-Evidence Gap under KV Compression / KV 压缩下的"答案-证据鸿沟"

**推荐理由 / Why read:** 本文首次揭示 KV 缓存压缩中存在"答案-证据鸿沟"——token 蒸发类方法在保持最终答案准确率的同时会悄悄损坏支持性推理链，使最终准确率成为"非对称诊断指标"。在 AIME26 上准确率与推理链一致性的 Spearman ρ 高达 −0.95，意味着基于准确率的排行榜会主动挑选"证据破坏型"压缩器。该结论对长 CoT 模型的压缩部署具有直接而深远的影响。
The paper identifies an answer-evidence gap in KV-cache compression: eviction-based methods preserve final-answer accuracy while silently breaking supporting reasoning chains, making accuracy an asymmetric diagnostic (Spearman ρ = −0.95 on AIME26). Accuracy-based leaderboards would actively select evidence-destroying compressors — a finding with direct deployment consequences for long-CoT models.

### 3. [[2608.02442]] — Solution Hacking Misleads Frontier Science Benchmarks / "解法劫持"误导前沿科学评测

**推荐理由 / Why read:** 作者提出"解法劫持"这一全新失败模式——模型通过数值搜索、枚举、先答后验等捷径得到正确答案而不展示目标推理能力。基于 300 条 PhD 专家盲法标注构建的判定器显示，HLE 上劫持率高达 37.4%，最强 anti-hack 提示将报告准确率从 50.6% 压到 37.3%，而"正确且非劫持"准确率仅小幅下降，表明许多被记为正确的分数实际上是捷径撑起来的。对 HLE/PHYBench 等前沿基准的效度有直接冲击。
The paper defines "Solution Hacking" — getting correct answers via invalid shortcuts (numerical search, enumeration, answer-first verification) that bypass targeted reasoning. Hack ratios reach 37.4% on HLE; the proposed derivation-adjusted accuracy (Daa) shows 8.2%–44.1% of credited-correct answers are shortcut-driven, with direct consequences for the validity of frontier science benchmarks.

---

## 按主题分类 / Papers by Topic

### LLM 评测与基准 / LLM Evaluation & Benchmarks

| Paper | 主题 / Topic |
|---|---|
| [[2608.01575]] Exact Bayes-Optimal ICL Benchmark | 首个有闭式精确贝叶斯最优解的 ICL 基准，揭示"后验保真度"这一与准确率正交的新轴 / First ICL benchmark with closed-form exact Bayes optimum; surfaces "posterior fidelity" as an axis orthogonal to accuracy |
| [[2608.02442]] Solution Hacking in Science Benchmarks | "解法劫持"导致 HLE/PHYBench 等前沿基准的答案分数虚高，最高 44.1% 的正确答案实为捷径 / Solution Hacking inflates HLE/PHYBench scores; up to 44.1% of credited-correct answers are shortcut-driven |
| [[2608.01792]] ConfBench for VLM Confidence Calibration | 首个面向文档 KIE 的置信度校准基准，Claude Opus 4.6 AUROC 0.84 接近完美 / First calibration-specific KIE benchmark; Claude Opus 4.6 reaches AUROC 0.84 near-perfect |
| [[2608.01810]] RADAR: Rubric-Aware Coupling Diagnostic | LLM-as-Judge 中"准则耦合"诊断框架，3-5 个探针即恢复人类跨准则相关性 / Diagnostic for criterion coupling in LLM-as-Judge; 3-5 probes recover human inter-criterion structure at r ≥ 0.84 |
| [[2608.01913]] Diagnosing Long-Horizon Search Agents | BrowseComp-Plus 上诊断 6 个长程搜索 Agent，搜索量与准确率几乎不相关（r=0.16），累积召回才是关键（r=0.99）/ Trajectory-level diagnosis shows search effort ≠ accuracy (r=0.16); cumulative gold-evidence recall tracks accuracy (r=0.99) |
| [[2608.02486]] Cultural Awareness: Represented but Not Decoded | 18 个开源 LLM 残差流能线性读出文化标签但解码端坍缩到希腊-罗马主流 / Residual stream linearly encodes culture but decoder collapses to Greco-Roman defaults (51–76% DecodingSuppressed) |
| [[2608.02089]] Observability Ladder for Reasoning Summaries | 思维链摘要的"可观测性阶梯"，prompt 可见时摘要几乎不带来额外正确性预测增益 / Observability ladder framework; CoT summaries add little over prompt when prompt is visible (+0.019 AUROC) |

### 机制可解释性与表示几何 / Mechanistic Interpretability & Representation Geometry

| Paper | 主题 / Topic |
|---|---|
| [[2608.01676]] Sparse Attention Counterfactual Audit | 反事实审计证明稀疏注意力会系统性改变特定内容对输出的影响，压缩比是关键控制变量 / Counterfactual audit shows sparse attention systematically shifts content-specific influence; compression ratio is the control variable |
| [[2608.01816]] Divergent LLM Predictions from Convergent Repr. | 歧义词表示"中段最远、末层再收敛"，但下一 token 预测 KL 散度恰在末层最大 / Representation reconverges in late layers while next-token KL divergence peaks there, decoupling geometry from prediction |
| [[2608.01835]] Behavioral Manifold: Rewriting vs Reweighting | SFT 倾向"改写"行为几何，DPO/RL 主要在继承几何中"重新加权" / SFT rewrites behavioral geometry; DPO/RL reweights within the inherited chart (23-model atlas) |
| [[2608.01876]] TGO-III: Semantic Geometry Observatory | ViT 训练中"全局流形扩张 + 局部语义压缩"同时发生，最强判别力集中在末层 / Global manifold expansion co-occurs with local per-class compression; semantic discrimination peaks at final block |
| [[2608.01968]] ChaosProbe: Neurochaotic Embedding Fingerprint | 用 GLS 斜帐篷混沌映射生成 transformer 嵌入响应指纹，100% 恢复同家族配对 / Deterministic neurochaos probe fingerprints transformer embeddings; 100% same-family recovery on 4-model cohort |
| [[2608.02064]] Geometry-Guided FFN Width Allocation | 用 Gromov-Wasserstein 与持续同调推导最优 FFN 逐层宽度分配，比 TLM 余弦锥化优 6.3 倍 / Gromov-Wasserstein + persistent homology derive budget-optimal per-layer FFN width; ~6.3× the loss reduction of TLM cosine taper |
| [[2608.02071]] Feed-Forward Steering in Residual Dynamics | FFN 切向分量是改变残差方向的关键，提出基于输入敏感度的层并行化指标 C_ℓ / Tangential FFN component drives residual-direction change; C_ℓ score guides safe layer parallelization |
| [[2608.01930]] Textual Shortcuts in VLM Self-Reflection | 视觉自反思失败根因是"文本捷径复用"，FSAF 注意力防火墙把视觉更新率从 35.28% 提到 53.61% / VLM reflection failure is textual-shortcut reuse; FSAF firewall raises visual update rate 35.28%→53.61% |

### LLM 智能体 / LLM Agents

| Paper | 主题 / Topic |
|---|---|
| [[2608.01619]] StateAuditor: Repairing Stale Memory Dependencies | 诊断"记忆已更新但响应未更新"的 IPA 缺口，VTA 在 Stale 上 +5.0 配对增益 / Diagnoses draft-anchored verification blindness; VTA gives +5.0 paired points on Stale benchmark |
| [[2608.01679]] AuthMem-Bench: Authority Collapse | "权威坍塌"——记忆固化时抹去来源权威约束，48/49 配置出现坍塌 / Authority collapse: 48/49 consolidator-backend configurations erase source authority; predictor drives ASR 16.9%→0.0% |
| [[2608.01805]] CockpitHAT: Multi-Agent Cockpit Attribution | 依赖图驱动的多智能体失败归因，发布 CockpitBench，比 ECHO 提升 17.6 pp / Dependency-DAG attribution for cockpit agents; CockpitBench released; +17.6 pp over ECHO on Who&When |
| [[2608.01904]] CoEvoKG: Co-Evolving Knowledge Graphs | 知识图谱链同时作为可验证任务源和持久化证据记忆 / KG chains serve as both verifiable task source and evidence memory; +2.6 to +3.7 macro over Search-R1/SSP |
| [[2608.01918]] HarnessCompass: Disciplined Harness Evolution | 三条"纪律性"原则驯服自动 harness 演化过拟合，5 轮即从 54% 提到 66% / Three disciplined principles tame harness-evolution overfitting; 54%→66% in 5 turns on SWE-Bench |
| [[2608.02011]] READ-GATE: Pre-Evidence Procedural Failures | "搜索后未读证据即作答"运行时不变式，零读取轨迹上 +14.9–19.9 LLM-Acc / READ-GATE invariant recovers +14.9–19.9 LLM-Acc on zero-read trajectories in agentic RAG |
| [[2608.02026]] HPFA: Hypergraph Paired Failure Attribution | 成对轨迹+依赖超图定位根因，比 AgentDebug 提升 30+ pp / Paired trajectories + dependency hypergraph localize root causes; +30 pp over AgentDebug on MATH500 |
| [[2608.02143]] Iris: Information Paradigm for ML Engineering | "信息范式 + 可修订任务知识 + 认知型动作"，MLE-Bench 12h 取 64.9% any-medal / Information paradigm with revisable task knowledge; 64.9% any-medal at 12h on full MLE-Bench |
| [[2608.02276]] Harness-R1: Learning to Edit Runtime Harnesses | 用 GRPO 训练独立 9B 工程师模型编辑可执行运行时，目标 Agent +9.3 pp / GRPO-trained 9B engineer edits executable runtime; frozen target agent +9.3 pp |
| [[2608.02351]] KC-Agent: Dual-Process Cognitive Architecture | Kahneman 双过程+知识固化，13.2s/847 token 达 76.8% 准确率 / Kahneman-inspired dual-process agent; 76.8% accuracy at 13.2s/847 tokens (7.9× fewer tokens than CodeAct) |
| [[2608.02352]] Qwen-CUA: Native Computer Use Agent | 纯原生计算机使用 Agent，OSWorld-Verified 86.2 超 GPT-5.5/Claude Opus 4.8 / Screenshot-only native CUA; OSWorld-Verified 86.2 beats GPT-5.5/Opus 4.8 |
| [[2608.02464]] Real-Time Detection and Repair of Agent Failures | 微秒级 ESN+CUSUM 监控+确定性校验+回滚修复，任务成功率从 52% 提到 73% / Microsecond ESN+CUSUM monitor + deterministic verifier + rollback repair; 52%→73% net task success |
| [[2608.02508]] RoMeRL: Reduced-Order Memory RL | 形式化"记忆-奖励陷阱"，固定 4 维因子化状态，整体 +3.2 pp / Formalizes Memory-Reward Trap; fixed 4-coordinate state; +3.2 pp overall with 84.4% less memory |

### 后训练与强化学习 / Post-Training & Reinforcement Learning

| Paper | 主题 / Topic |
|---|---|
| [[2608.01743]] CoKL: Correctness-Conditioned KL Regularization | 把 KL 约束缩小到"正确响应"条件分布，三尺度上 +1.40~+2.42 Overall / KL constrained to verified-correct responses; +1.40~+2.42 Overall across Qwen3 0.6B/1.7B/4B |
| [[2608.02139]] SPEE: Progressive Experience Evolution | 经验池+OPSD 自蒸馏+GRPO 闭环，五基准平均 +1.16 pp vs GRPO / Experience pool + on-policy self-distillation + GRPO; +1.16 pp avg over GRPO, ~28% fewer trajectories |
| [[2608.02585]] GradCuit: Credit-Assigned Gradient Latent Reasoning | 自注意力作为梯度通路，平均 64.5% 比 CoT 高 6.6 pp / Self-attention as gradient-routing circuit; 64.5% avg (+6.6 pp over CoT), halved LR sensitivity |

### 安全与可信 / Safety & Trustworthiness

| Paper | 主题 / Topic |
|---|---|
| [[2608.01849]] SPAR: Knowledge Holes in MLLM Unlearning | 形式化"知识空洞"，Anchored SVD 在 LLaVA-1.5-7B 上 Res.Q 7.07 vs 原始 7.17 / Formalizes knowledge holes; Anchored SVD recovers >98% quality at 0% ASR on LLaVA-1.5-7B |
| [[2608.02271]] Z-PEFT: Zero-shot Backdoor Detection in PEFT | 头级谱描述子+逻辑回归，zero-shot AUROC 0.9433，内存减 21000× / Per-head spectral descriptors + logistic regression; zero-shot AUROC 0.9433 with ~21,000× less memory than PEFTGuard |
| [[2608.02154]] DPA: Auditing Data Provenance in Fine-tuning | 黑盒分布级 IP 审计，95.62% TPR/4.38% FPR，揭示审计与隐私攻击的结构同构 / Black-box distributional provenance audit; 95.62% TPR / 4.38% FPR; dual-use transparency-paradox analysis |

### 高效推理与训练 / Efficient Inference & Training

| Paper | 主题 / Topic |
|---|---|
| [[2608.01847]] FOCUS: FP4 Coupled-Relaxation Scaling | 利用"量化尺度无需硬件合规"自由度，Qwen3-4B NVFP4 恢复 98.2% FP16 精度 / Exploits overlooked scale freedom; Qwen3-4B NVFP4 recovers 98.2% of FP16 with zero inference overhead |
| [[2608.02091]] One QK Channel: Low-Precision Attention Collapse | bfloat16 训练崩溃的多种误差源都汇聚到同一 QK 谱失控通道，QK-Guard 休眠控制器救援 / Heterogeneous low-precision errors converge on one QK channel; dormant QK-Guard contains collapse |
| [[2608.01997]] AOS: Adaptive Optimizer Switching | 六信号驱动的优化器切换控制器，CIFAR-100/WRN-28-10 0.80× AdamW 收敛步数 / Six-signal optimizer switching; CIFAR-100/WRN-28-10 reaches milestones in 0.80× AdamW steps |
| [[2608.02502]] CMuon: Chunked Momentum Orthogonalization | 切分融合权重再正交化，675M DiT ImageNet-256 FID 1.18 @ 200ep (>2× AdamW) / Chunk fused tensors before Newton-Schulz; DiT-XL FID 1.18 at 200 epochs (>2× AdamW speedup) |
| [[2608.02575]] Pseudorandom Streams in Diffusion Models | 伪随机轨道是"可学习输入"，不同源能改变损失与生成质量 / PRNG streams act as learnable inputs; different orbits shift loss and quality on MNIST/CIFAR-10 |

### 理论、科学发现与跨学科 / Theory, Scientific Discovery & Interdisciplinary

| Paper | 主题 / Topic |
|---|---|
| [[2608.01585]] Semantic Alignment via TDA | 拓扑数据分析+能量统计刻画嵌入语义结构，追踪 LoRA 概念坍缩 / Topological data analysis + energy statistics tracks LLM embedding semantic structure and LoRA concept collapse |
| [[2608.01633]] GraphIR: LLM-Guided NAS | 变异对齐的架构感知中间表示，CLRS 平均准确率 83.91%→89.21% / Mutation-aligned architecture IR; CLRS avg accuracy 83.91%→89.21%, lowest end-to-end GPU time |
| [[2608.01648]] HPC Hardware Error Forecasting | 7 年 Theta 超算错误日志的预测可行性边界，LSTM 在 Minor 上最佳 / 7-year Theta supercomputer error forecasting feasibility boundary; LSTM best on Minor errors |
| [[2608.01691]] ARM: Detector-Agnostic Changepoint Attribution | 秩统计量最大值+Westfall-Young 联合置换，精确 FWER/FDR 控制 / Rank-maxima + Westfall-Young permutation; selection-proof finite-sample FWER/FDR control |
| [[2608.01743]] CoKL | (见后训练 / see Post-Training) |
| [[2608.01865]] Layer-wise Probing Dysarthric ASR | 中文构音障碍 ASR 逐层探测，第 7 层 LoRA 即近全适配 / Mandarin dysarthric ASR layer-wise probing; layer-7 LoRA within 3.5% of full adaptation |
| [[2608.01975]] TELLER: Non-intrusive LLM Inference RCA | CUPTI/NVTX trace 重建跨层调用链+结构保持 TPE，step Acc 0.930 / Non-intrusive cross-layer RCA; TPE compresses traces 83.88% with best diagnosis quality |
| [[2608.01995]] Long-Horizon Autonomous Architecture Research | 单 LLM 跑 10 周自主 ViT 研究，三段式生产力结构与贪婪偏好分解 / Single LLM runs 10-week autonomous ViT research; three-regime productivity and bias decomposition |
| [[2608.02505]] Abduction Without a Body: Representational Grounding | 反驳"具身必要性论题"，提出"约定空间"与 DAB-30 评估程序 / Refutes Embodiment Necessity Thesis; proposes convention space and DAB-30 evaluation program |

---

## All Papers

| ArXiv ID | 标题 / Title | 一句话 / One-liner |
|---|---|---|
| [[2608.01575]] | F-ICL: Bayes-Optimal ICL Benchmark | 46 模型上"答对 ≠ 按最优后验推"，提出后验保真度新轴 / 46 models show answer-correct ≠ posterior-faithful; new evaluation axis |
| [[2608.01585]] | Semantic Alignment via TDA | 拓扑+能量统计追踪 LoRA 概念坍缩与跨语言对齐 / TDA + energy statistics tracks LoRA collapse and cross-lingual alignment |
| [[2608.01619]] | StateAuditor: Repairing Stale Memory | 状态→草稿双向审计+溯源-时序验证，Stale +5.0 pp / State→draft audit with provenance verification; +5.0 pp on Stale |
| [[2608.01631]] | Answer-Evidence Gap under KV Compression | 蒸发式压缩破坏推理链但保留准确率，ρ=−0.95 / Eviction compressors break chains but keep accuracy; ρ=−0.95 |
| [[2608.01633]] | GraphIR: LLM-Guided NAS | 变异对齐 IR，CLRS 83.91%→89.21% / Mutation-aligned IR raises CLRS 83.91%→89.21% |
| [[2608.01648]] | HPC Hardware Error Forecasting | Theta 7 年日志，稀疏错误不可预测 / 7-year Theta logs; sparse errors remain unpredictable (RMSE% 405–1249) |
| [[2608.01676]] | Sparse Attention Counterfactual Audit | 反事实审计证明稀疏注意力改变内容影响 / Counterfactual audit shows sparse attention shifts content influence |
| [[2608.01679]] | AuthMem-Bench: Authority Collapse | 48/49 配置出现权威坍塌，预测标签降 ASR 至 0.0% / 48/49 configs collapse; predicted labels cut ASR to 0.0% |
| [[2608.01691]] | ARM: Changepoint Attribution | 秩统计量最大值实现选择免疫的 FWER/FDR 控制 / Rank-maxima statistic gives selection-proof FWER/FDR control |
| [[2608.01743]] | CoKL: Correctness-Conditioned KL | 条件化 KL 解耦正确率与正确响应分布，+2.42 pp / Correctness-conditioned KL decouples correctness; +2.42 pp |
| [[2608.01792]] | ConfBench: VLM Confidence Calibration | 首个文档 KIE 校准基准，Opus 4.6 AUROC 0.84 / First KIE calibration benchmark; Opus 4.6 AUROC 0.84 |
| [[2608.01805]] | CockpitHAT: Multi-Agent Attribution | 依赖图+ASIL 加权共识，+17.6 pp / Dependency DAG + ASIL-weighted consensus; +17.6 pp over ECHO |
| [[2608.01810]] | RADAR: Rubric Coupling Diagnostic | 3-5 个探针恢复人类跨准则相关性 / 3-5 probes recover human inter-criterion structure |
| [[2608.01816]] | Divergent Predictions, Convergent Repr. | 表示末层再收敛，但预测 KL 末层最大 / Repr. reconverges in late layers while predictive KL peaks there |
| [[2608.01835]] | Behavioral Manifold: Rewriting vs Reweighting | SFT 改写、DPO 重加权（23 模型图谱）/ SFT rewrites, DPO reweights (23-model atlas) |
| [[2608.01847]] | FOCUS: FP4 Coupled-Relaxation Scaling | 量化尺度可学习松弛，NVFP4 恢复 98.2% FP16 / Learnable scale relaxation; NVFP4 recovers 98.2% of FP16 |
| [[2608.01849]] | SPAR: MLLM Knowledge Holes | Anchored SVD 恢复 98% 质量，0% ASR / Anchored SVD recovers >98% quality at 0% ASR |
| [[2608.01865]] | Layer-wise Probing Dysarthric ASR | 第 7 层 LoRA 近全适配，高层反而恶化 / Layer-7 LoRA near-optimal; upper layers hurt dysarthric CER |
| [[2608.01876]] | TGO-III: Semantic Geometry Observatory | 全局扩张+局部压缩同时发生，末层最强判别 / Global expansion + local compression co-occur; final block dominates |
| [[2608.01904]] | CoEvoKG: Co-Evolving Knowledge Graphs | KG 链作任务源+证据记忆，+3.7 pp / KG chains as task source + evidence memory; +3.7 pp |
| [[2608.01913]] | Diagnosing Long-Horizon Search Agents | 搜索量≠准确率（r=0.16），累积召回才是（r=0.99）/ Search effort ≠ accuracy (r=0.16); recall tracks it (r=0.99) |
| [[2608.01918]] | HarnessCompass: Disciplined Harness Evolution | 5 轮 54%→66%，450 held-out 60.4% / 5 turns 54%→66%; held-out 60.4% (vs AHE 54.7%) |
| [[2608.01930]] | Textual Shortcuts in VLM Self-Reflection | FSAF 注意力防火墙视觉更新率 35.28%→53.61% / FSAF firewall raises visual update 35.28%→53.61% |
| [[2608.01947]] | RDNN: Divisive Normalization Slow Manifolds | 除法归一化让 RNN 学到连续吸引子，有效秩压缩 6× / Divisive normalization yields continuous attractors; 6× rank compression |
| [[2608.01968]] | ChaosProbe: Neurochaotic Fingerprint | GLS 混沌映射生成嵌入指纹，100% 家族配对恢复 / GLS chaotic map fingerprints embeddings; 100% family-pair recovery |
| [[2608.01975]] | TELLER: Non-intrusive LLM Inference RCA | TPE 压缩 83.88%，step Acc 0.930 / TPE compresses traces 83.88%; step Acc 0.930 |
| [[2608.01995]] | Autonomous Architecture Research Agent | 单 LLM 10 周 +26.92 pp，行为学三段式分析 / Single LLM 10-week +26.92 pp; three-regime behavioral analysis |
| [[2608.01997]] | AOS: Adaptive Optimizer Switching | 六信号切换 AdamW/Lion/SGD-M，0.80× AdamW 收敛 / Six-signal switching; 0.80× AdamW convergence steps |
| [[2608.02011]] | READ-GATE: Pre-Evidence Failures | 强制"先读后答"，零读取轨迹 +19.9 pp / Force read-before-final; +19.9 pp on zero-read trajectories |
| [[2608.02026]] | HPFA: Hypergraph Failure Attribution | 成对轨迹+超图，MATH500 30.9%→64.6% / Paired trajectories + hypergraph; MATH500 30.9%→64.6% |
| [[2608.02064]] | Geometry-Guided FFN Width Allocation | 拓扑/双曲分配比 TLM 优 6.3 倍 / Topological/hyperbolic allocation beats TLM by ~6.3× in loss reduction |
| [[2608.02071]] | Feed-Forward Steering in Residual Dynamics | 切向 FFN 主导，C_ℓ 指标指导层并行化 / Tangential FFN dominates; C_ℓ guides safe parallelization |
| [[2608.02089]] | Observability Ladder for Reasoning | 摘要在 prompt 可见时仅 +0.019 AUROC / Summaries add only +0.019 AUROC when prompt is visible |
| [[2608.02091]] | One QK Channel: Low-Precision Collapse | 多源一通道，QK-Guard 休眠救援 / Many sources converge on one QK channel; dormant QK-Guard rescues |
| [[2608.02139]] | SPEE: Progressive Experience Evolution | 经验池+OPSD+GRPO，+1.16 pp vs GRPO / Pool + self-distillation + GRPO; +1.16 pp over GRPO |
| [[2608.02143]] | Iris: Information Paradigm for MLE | 信息范式，MLE-Bench 64.9% any-medal @ 12h / Information paradigm; 64.9% any-medal at 12h on MLE-Bench |
| [[2608.02154]] | DPA: Auditing Data Provenance | 黑盒分布级 IP 审计 95.62% TPR / Black-box distributional audit; 95.62% TPR |
| [[2608.02267]] | Self-Certification of Representation Adequacy | 四层自我认证理论，CTS 匹配 LP 常量下界 / Four-layer self-certification theory; CTS matches LP lower bound |
| [[2608.02271]] | Z-PEFT: Zero-shot Backdoor Detection | 头级谱描述子 zero-shot AUROC 0.9433 / Per-head spectral descriptors; zero-shot AUROC 0.9433 |
| [[2608.02276]] | Harness-R1: Learning to Edit Harnesses | GRPO 训练 9B 工程师，目标 Agent +9.3 pp / GRPO-trained 9B engineer; target agent +9.3 pp |
| [[2608.02351]] | KC-Agent: Dual-Process Architecture | 双过程+知识固化，76.8% @ 847 token / Dual-process + consolidation; 76.8% at 847 tokens |
| [[2608.02352]] | Qwen-CUA: Native Computer Use | OSWorld-Verified 86.2，ASR 36.6→16.4 / OSWorld-Verified 86.2; ASR 36.6→16.4 |
| [[2608.02442]] | Solution Hacking Misleads Benchmarks | HLE 劫持率 37.4%，Daa 揭示虚高 / HLE hack ratio 37.4%; Daa exposes inflation |
| [[2608.02464]] | Real-Time Agent Failure Detection/Repair | ESN+校验+回滚，52%→73% / ESN + verifier + rollback; 52%→73% net success |
| [[2608.02486]] | Cultural Awareness: Repr. Not Decoded | 解码端坍缩到希腊-罗马，双语言集成 +36% / Decoder collapses to Greco-Roman; bilingual ensemble +36% |
| [[2608.02502]] | CMuon: Chunked Momentum Orthogonalization | 675M DiT FID 1.18 @ 200ep，>2× AdamW / 675M DiT FID 1.18 at 200 ep; >2× AdamW speedup |
| [[2608.02505]] | Abduction Without a Body | 反驳具身必要性论题，约定空间+DAB-30 / Refutes Embodiment Necessity Thesis; convention space + DAB-30 |
| [[2608.02508]] | RoMeRL: Reduced-Order Memory RL | 4 维因子化状态，+3.2 pp，84.4% 减记忆 / 4-coordinate state; +3.2 pp with 84.4% less memory |
| [[2608.02575]] | PRNG as Learnable Inputs in Diffusion | 伪随机轨道可被扩散模型学习利用，幂律 ρ(M,D) / Pseudorandom orbits are learnable; power-law ρ(M,D) |
| [[2608.02585]] | GradCuit: Credit-Assigned Latent Reasoning | 自注意力梯度通路，64.5% (+6.6 pp vs CoT) / Self-attention gradient circuit; 64.5% (+6.6 pp over CoT) |

---

## 备注 / Notes

- 本 overview 共收录 **50** 篇论文，与目录下 `.md` 文件数（扣除 overview.md 自身）一致。/ This overview includes **50** papers, matching the number of `.md` files in the directory (minus overview.md itself).
- 所有 `.md` 文件均位于 `/Volumes/T7/work/daily_paper/arxiv-daily/2026-08-03/`。/ All `.md` files are located in `/Volumes/T7/work/daily_paper/arxiv-daily/2026-08-03/`.
