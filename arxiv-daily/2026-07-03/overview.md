---
title: "Daily Arxiv Digest — 2026-07-03"
date: 2026-07-03
tags:
  - llm-agents
  - mechanistic-interpretability
  - llm-safety
  - llm-training
  - reasoning
  - autonomous-science
  - representation-geometry
papers: 34
---

## 今日必读 / Must Read Today

### 1. [[2607.02513]] LACUNA: A Testbed for Evaluating Localization Precision for LLM Unlearning
- **推荐理由 (zh)**：首个带有"参数级真值标注"的 LLM 遗忘评测平台，直接证伪"输出好等于真遗忘"的普遍假设——SOTA 遗忘方法定位精度近乎随机（AUC≈0.5），而一个简单的梯度 oracle 配合正确掩码就能达到 0.915，证明"定位精度"才是真正瓶颈。
- **Why read (en)**：First unlearning testbed with ground-truth parameter-level localization (PII injected into a predefined 5% of an OLMo-1B/7B via masked continual pretraining); exposes that SimNPO/AlphaEdit/MemFlex score ~0.5 AUC on localization despite strong output behavior, while a gradient oracle with the correct mask reaches 0.915 — a paradigm-shifting negative result.

### 2. [[2607.02329]] Grounded Autonomous Research: A Fault-Tolerant LLM Pipeline from Corpus to Manuscript in Frontier Computational Physics
- **推荐理由 (zh)**：从 11,083 篇 arXiv 凝聚态物理语料到投稿级论文的端到端容错流水线，自主产出三项 altermagnetic-piezomagnetism 发现；核心创新是把"接地"操作化为"校准检查点处的结构化数值对质"，并用成对消融分离出该机制。
- **Why read (en)**：A corpus-to-manuscript LLM pipeline (47 fresh-context sessions, 6 phases, 2,162 literature consultations) that autonomously produces a publication-grade physics manuscript with three novel findings; the "structurally enforced numerical confrontation" grounding primitive is rigorously isolated via paired ablations (pre-architecture baseline + no-pilot).

### 3. [[2607.02510]] Online Safety Monitoring for LLMs
- **推荐理由 (zh)**：一个用 conformal risk control 校准的单阈值在线监测器，竟与复杂的序贯假设检验方法持平且更早告警——"强简单基线"论文，为未来在线安全监测设立了必须超越的门槛。
- **Why read (en)**：A deliberately simple conformal-risk-calibrated threshold monitor matches sequential-hypothesis-testing baselines on math reasoning and red-teaming while raising alarms earlier; a normative "must-beat" baseline for the online-monitoring subfield.

---

## 按主题分类 / Papers by Topic

### 🧠 Mechanistic Interpretability & Representation Geometry / 机制可解释性与表征几何

| Paper | Summary (中 / En) |
|---|---|
| [[2607.01571]] Geometric Signatures of Reasoning | 用有效维度 $d_\rho$ 刻画 CoT 推理几何，MATH500 上 0.93 AUC 区分难度，20% token 即预测正确性。 / Spectral effective dimension $d_\rho$ separates MATH500 difficulty at AUC>0.93; kinematic features predict correctness from the first 20% of tokens (AUC 0.806). |
| [[2607.01774]] Subliminal Clocks | 扩散语言模型残差流隐式编码去噪进度 τ，跨层 R²>0.5（峰值 0.94），呈低维有序"时钟"流形。 / DLMs implicitly encode a latent denoising-progress τ in the residual stream (probe R²>0.5 all layers, peak 0.94); corresponds to a low-dimensional ordered "clock" manifold (PC1 >90% variance), steerable to modulate confidence/entropy. |
| [[2607.01799]] Expander SAEs | 扩展图掩码把 SAE 解码器参数从 $O(mn)$ 降到 $O(dn)$，Qwen2.5-3B 上 d=7 用 293× 更少参数保 84% CE-loss。 / Expander-graph masks cut SAE decoder params to 1/293 while keeping 84% of dense CE-loss recovered on Qwen2.5-3B; theory gives identifiability + OMP support recovery. |
| [[2607.01940]] CoAx (Conditional Co-Ablation) | 把自我修复重述为"条件电路补全"，备份头恢复 ROC-AUC 0.33→0.91，1.76 vs 0.22 logit-diff 归因。 / Recasts self-repair as conditional circuit completion; CoAx raises backup-head recovery ROC-AUC 0.33→0.91, restores attribution 1.76 vs 0.22 logit-diff. |
| [[2607.01987]] Geosubprobe (ViT Geometry) | SVD 子空间干预剖析 DINOv2/MAE 几何编码，DINOv2 高度对齐（Linear 0.9157），MAE 分散。 / SVD subspace intervention reveals DINOv2 aligns geometry (Linear 0.9157) vs MAE disperses (0.6033, +0.0632 spatial fragmentation); geometric precision peaks at mid layers. |
| [[2607.02386]] TGO-II | 用 CKA/SVCCA/TwoNN/token 协方差追踪 ViT-S/16 训练动态，提出"流形扩张"假说。 / Tracks ViT-S/16 representational geometry over 100 ImageNet-100 epochs with CKA/SVCCA/TwoNN/token-covariance; proposes a "Manifold Expansion" hypothesis. |
| [[2607.01746]] Finite-Lag Operator Geometry | 为循环表征构建有向有限滞后传输律 $Q_\Delta$，分离静态快照几何缺失的相干位移（Elman 比 GRU/LSTM 大 ~15%）。 / Directed finite-lag transport geometry for recurrent states; Elman shows ~15% larger total transport tr($\bar G_\Delta$) (1.0085) than GRU/LSTM; separates coherent motion invisible to snapshot geometry. |
| [[2607.02368]] Dual Nature of LLM Persona | 题目顺序操控揭示 LLM 人格"几何"是框架依赖的测量伪影，错位时崩塌 95.3%→52.9%。 / IPIP-50 order manipulation on GPT-4o shows persona "geometry" (SPD manifold) is frame-dependent: drops 95.3%→52.9% on misalignment, recovers to 84.5% on shared frame — a measurement artifact, not intrinsic trait. |
| [[2607.02494]] SamplingTAR (Typographic Attack) | 无训练定位 CLIP 编码文字的注意力头电路，OCA +12.4~+22.8 pts，clean 83.3% 保持。 / Training-free circuit localization in CLIP beats supervised defenses (OCA +12.4 to +22.8 pts, TCR −17.8 to −27.6) and improves LVLMs on RIO-Bench; clean accuracy held at 83.3%. |

### 🛡️ LLM Safety, Auditing & Alignment / 安全、审计与对齐

| Paper | Summary (中 / En) |
|---|---|
| [[2607.02510]] Online Safety Monitoring | conformal risk control 校准单阈值监测器，与序贯假设检验持平且更早告警。 / Conformal-risk-calibrated threshold monitor matches sequential testing and alarms earlier on math reasoning + red-teaming. |
| [[2607.02513]] LACUNA | 首个参数级真值遗忘评测；SOTA 定位 AUC≈0.5，OracleGrad 达 0.915。 / First parameter-level ground-truth unlearning testbed; SOTA localization AUC≈0.5, gradient oracle 0.915 on OLMo-1B/7B. |
| [[2607.01854]] Abliteration Audit | 双信号无阈值审计检测去拒绝化模型，AUROC 0.95，诚实刻画 spoofed-reference 与白盒攻击失效。 / Two-signal (ρ + E₁) threshold-free audit detects abliterated checkpoints at AUROC 0.95, transfers leave-one-family-out at bal.acc 0.89; honestly maps spoofed-reference + white-box evasion failures. |
| [[2607.02072]] kNNGuard | 无训练多层 kNN 护栏，50 样本匹敌微调 SOTA，快 2.7–10×，域适配 <10s。 / Training-free multi-layer kNN guardrail (Fisher-weighted) matches fine-tuned SOTA at F1 87.4%, 2.7× faster, domain-adapt <10s (61× vs LoRA). |
| [[2607.02396]] RFM-AGOP Refusal Subspaces | RFM 数秒提取多维拒绝子空间，≥8B 需 ≥3 方向才超 50% ASR。 / Adapts RFM-AGOP to extract multi-dimensional refusal subspaces in seconds; ≥8B models need ≥3 ablated directions to exceed 50% ASR (scale-dependent multi-dimensionality). |
| [[2607.01802]] Steering Vectors Limits | 系统揭示引导向量在特质、任务迁移与多特质组合上的偏好对齐局限（组合 ≥15% 退化）。 / Benchmarks steering vectors on PLUME (36 traits, 2 models): top-10 global-structural traits steerable; multi-vector composition suffers ≥15% trait-expression drop with coherence/expressibility tradeoff. |
| [[2607.01951]] Robust for Wrong Reasons | LLM 对科学怀疑的"稳健性"可能源于未感知信号；Mistral 线性探针仅 72%。 / Shows LLM "robustness" to science skepticism may stem from failing to perceive the signal (Mistral linear probe 72% vs Llama/Qwen perfect separation); active vs accidental robustness taxonomy; reverses in vaccine domain. |
| [[2607.02175]] Clinical Reasoning Rubric | 医生撰写高难度临床推理评测，critical 权重-5 通过率仅 32.4–41.7%（52% 无模型满足）。 / Clinician-authored hard rubric (184 criteria, 5 scenarios) reveals "clinical priority inversion": weight-5 critical criteria pass at only 32.4–41.7%, 56/108 met by no model (GPT 5.4/Opus 4.7/Gemini 3.1 Pro). |

### 🤖 LLM Agents & Autonomous Science / 智能体与自主科学

| Paper | Summary (中 / En) |
|---|---|
| [[2607.02329]] Grounded Autonomous Research | 端到端容错 LLM 流水线从 11k 论文语料产出投稿级物理论文与三项发现。 / End-to-end fault-tolerant pipeline (47 sessions, 6 phases) turns 11k-paper corpus into publication-grade physics with three novel altermagnetic-piezomagnetism findings. |
| [[2607.01639]] TrafficSci (AI Traffic Scientists) | 智能体重现已知交通定律，发现跨 8 城市（Argoverse2+nuScenes）τ∈[0,4]s 驾驶时间记忆尺度。 / Agentic system rediscovers three traffic laws and finds a cross-8-city τ∈[0,4]s temporal-memory scale (Wasserstein<0.24, bootstrap 95% CI<0.10) in driving. |
| [[2607.01584]] EO-Agents | 三智能体 LLM 流水线接地 NASA EO KG（150,351 节点/436,203 边），1475 数据集产出 160 假设。 / Three-agent pipeline grounded in NASA EO KG (150,351 nodes/436,203 edges) yields 160 hypotheses; 2×2×2 factorial shows rankings stable but ~25% score variance from judge identity. |
| [[2607.01709]] COMFYCLAW | ComfyUI 工作流智能体把构建建模为带类型图编辑，技能库随使用自演化。 / ComfyUI agent models workflow construction as typed graph editing with a self-evolving skill library; region-level VLM verifier + auto-revert invalid edits. |
| [[2607.01874]] SkillCoach | 自演化过程级 rubric（四维技能元能力），rubric 质量四指标全面提升（覆盖 71.56→83.70）。 / Self-evolving process rubrics along four skill dimensions; rubric self-evolution lifts gold-keypoint coverage 71.56→83.70, usability 81.53→94.33, hallucination 2.00→0.00. |
| [[2607.02440]] EvoPolicyGym | 受控"自主策略演化"评测（Core16/128-episode），GPT-5.5 居首，Claude Opus 4.7 领先 MiniGrid。 / Controlled "autonomous policy evolution" benchmark (Core16: Gym/Box2D/MuJoCo/MiniGrid/Robotics, 128-episode budget); GPT-5.5 tops aggregate rank, Claude Opus 4.7 leads MiniGrid. |
| [[2607.01935]] A-TMA (Ghost Memory) | 识别长期记忆"幽灵记忆"，ATMA 在 LTP 上冲突准确率 +0.240（0.480→0.720）。 / Identifies "ghost memory" in agent memory; A-TMA overlay improves LTP conflict accuracy 0.480→0.720 (+0.240) and LoCoMo temporal F1 0.0295→0.1705. |
| [[2607.01595]] PASE (Cloud Self-Healing) | 神经符号云故障恢复：LLM 计划 + 世界模型验证 + DRL 元提示，MTTR 降 >40%（72s vs 85s）。 / Neuro-symbolic cloud recovery (LLM plan synthesis + NSWM verification + SAC meta-prompt); F1 0.94, MTTR 72s vs IFSHM 85s (>40% faster), novel-fault adaptation 40%→80% in ~15 episodes. |

### ⚙️ LLM Training, Inference & Systems / 训练、推理与系统

| Paper | Summary (中 / En) |
|---|---|
| [[2607.01646]] DeadPool | 大模型训练容错：零开销内存检查点 + 热替换，512 A100 上 <40s 恢复（vs 150s restart）。 / LLM training fault tolerance: zero-overhead in-memory optimizer-state replication + hot-swapping; <40s recovery vs 150s checkpoint-restart (3.7×), 18.8× time-to-resume over 100K-step run. |
| [[2607.01678]] SCAPE | 基于 Adam 一阶矩的稀疏化在 99% 稀疏度下保持质量，预训练墙钟时间降 43.3%。 / First-moment-based sparsification preserves quality at 99% sparsity, cutting Llama-500M pretraining wall-clock by 43.3% and 3.26× per-step on Llama-1.8B (32 GH200). |
| [[2607.01831]] Lynx | 渐进式分流 KV 传输（Anchor/Residual）+ 推测解码，TTFT 接近 INT4、精度匹配 BF16。 / Progressive split-stream KV transfer (Anchor MSB + Residual) + speculative decode; TTFT 1.6s near INT4, accuracy 85.20% matches BF16 85.25% (Qwen3-32B MMLU-Pro 16K); 1.43× over INT8. |
| [[2607.02182]] DALorRA | 变分贝叶斯稀疏 LoRA（秩级 Bernoulli 掩码后验 + Gumbel-Sigmoid），9/10 设定最佳/次佳，精度无损。 / Variational Bayesian sparse LoRA with rank-level Bernoulli mask posterior; on Llama3.1-8B best/2nd on 9/10 PLUME settings, no accuracy loss; ablation shows learned posterior (not dropout) drives gains. |
| [[2607.02187]] GPBACC Framework | 统一 FL/DL 隐私编码计算 + 鲁棒聚合 + group testing 验证；CNN-MNIST R10 0.9853 vs FedAvg 0.9855。 / Unified privacy-preserving coded computing + robust aggregation (FL) + decode-and-compare/group-testing (DL); CNN-MNIST R10 0.9853 vs FedAvg 0.9855, DP-SVT collapses to 0.10–0.50. |

### 🧪 AI4Science, Scientific Methods & Theory / 科学计算与理论

| Paper | Summary (中 / En) |
|---|---|
| [[2607.02194]] DSGNAR (PINNs) | 双重 sketch Gauss-Newton 二阶优化把 PINNs 精度提升 5–8 个数量级，接近机器精度。 / Doubly-sketched Gauss-Newton with adaptive ratio lifts PINN accuracy by 5–8 orders (rel. ℓ2 error down to 3×10⁻¹⁶ in double precision); Burgers fp32 4.75×10⁻⁷ in <10s. |
| [[2607.02055]] SASP-CDRO | 结构感知分层划分 + 课程 DRO，泄漏降 98.5%，BCCD Test mAP 85.6→89.2。 / Structure-aware stratified partitioning + curriculum DRO; reduces near-duplicate leakage 98.5% (DINOv2 cosine>0.95), Test-mAP gains BCCD 85.6→89.2, GWHD-v5x 61.5→68.0. |
| [[2607.01686]] WARP | 模型合并模拟训练轨迹 + Mimic Score 几何足迹，从权重反推数据混合（BERT MAE 0.046）。 / Model-merging simulates training trajectory + Mimic-Score footprints recover fine-tune data mixture from weights alone; BERT avg MAE 0.046, beats Sample-level MI (0.064) and real-trajectory oracle (0.080). |
| [[2607.01602]] ProWAFT | FPGA CNN 主动负载感知容错，ZCU104 上吞吐 +45.9%、能耗 −30.3%、成功率 98.8%。 / Proactive workload-aware fault tolerance for FPGA CNN accelerators via partial-reconfiguration selective TMR; ZCU104 throughput 0.61→0.89 (+45.9%), energy 302.5J→210.7J (−30.3%), success 98.8%. |

---

## All Papers

| # | ID | Title | Topic |
|---|---|---|---|
| 1 | [[2607.01571]] | Geometric Signatures of Reasoning | Mechanistic Interpretability |
| 2 | [[2607.01584]] | EO-Agents: Three-Agent LLM Pipeline for Earth Observation | LLM Agents / Autonomous Science |
| 3 | [[2607.01595]] | PASE: Safe and Adaptive Cloud Healing | LLM Agents / Systems |
| 4 | [[2607.01602]] | ProWAFT: Workload-Aware Fault Tolerance in FPGA CNN Accelerators | AI4Science / Hardware |
| 5 | [[2607.01639]] | Autonomous Discovery of Traffic Laws with AI Traffic Scientists | Autonomous Science |
| 6 | [[2607.01646]] | DeadPool: Resilient LLM Training with Hot-Swapping | LLM Training / Systems |
| 7 | [[2607.01678]] | SCAPE: Extreme Sparse Communication for LLM Training | LLM Training / Systems |
| 8 | [[2607.01686]] | WARP: Recovering Training Data Portfolios from Weights | Interpretability / Privacy |
| 9 | [[2607.01709]] | COMFYCLAW: Self-Evolving Skill Harnesses for Image Generation | LLM Agents |
| 10 | [[2607.01746]] | Finite-Lag Operator Geometry of Recurrent Representations | Representation Geometry / Theory |
| 11 | [[2607.01774]] | Subliminal Clocks: Latent Time in Diffusion Language Models | Mechanistic Interpretability |
| 12 | [[2607.01799]] | Expander Sparse Autoencoders for Mechanistic Interpretability | Mechanistic Interpretability |
| 13 | [[2607.01802]] | On the Limits of Steering Vectors for Preference Alignment | Alignment / Representation Eng |
| 14 | [[2607.01831]] | Lynx: Progressive Speculative Quantization for KV Transfer | Inference / Systems |
| 15 | [[2607.01854]] | Has This Checkpoint Been Abliterated? Two-Signal Audit | LLM Safety / Auditing |
| 16 | [[2607.01874]] | SkillCoach: Self-Evolving Rubrics for Agentic Skill-Use | LLM Agents / Evaluation |
| 17 | [[2607.01935]] | A-TMA: Decoupling State-Aware Memory Failures | LLM Agents / Memory |
| 18 | [[2607.01940]] | Conditional Co-Ablation (CoAx): Self-Repair Backups | Mechanistic Interpretability |
| 19 | [[2607.01951]] | Robust for the Wrong Reasons: LLM Robustness to Science Skepticism | LLM Safety / Interpretability |
| 20 | [[2607.01987]] | Geometric Representations in Self-Supervised ViTs | Representation Geometry / Vision |
| 21 | [[2607.02055]] | SASP-CDRO: Structure-Aware Stratified Partitioning | Evaluation Methodology / DRO |
| 22 | [[2607.02072]] | kNNGuard: Training-Free Configurable LLM Guardrail | LLM Safety |
| 23 | [[2607.02175]] | Rubric-Based Comparison of Frontier Models on Clinical Reasoning | Evaluation / AI Safety |
| 24 | [[2607.02182]] | DALorRA: Bayesian Sparse LoRA for Uncertainty Estimation | PEFT / Bayesian |
| 25 | [[2607.02187]] | Privacy-Preserving Verifiable Approximate Coded Computing | Distributed ML / Privacy |
| 26 | [[2607.02194]] | DSGNAR: Well-Conditioned Training of PINNs | Scientific Computing |
| 27 | [[2607.02329]] | Grounded Autonomous Research in Frontier Computational Physics | Autonomous Science |
| 28 | [[2607.02368]] | The Dual Nature of LLM Persona | Psychometrics / Evaluation |
| 29 | [[2607.02386]] | TGO-II: Representational Similarity Observatory | Representation Geometry / Vision |
| 30 | [[2607.02396]] | Fast Multi-dimensional Refusal Subspaces via RFM-AGOP | LLM Safety / Interpretability |
| 31 | [[2607.02440]] | EvoPolicyGym: Evaluating Autonomous Policy Evolution | LLM Agents / Benchmark |
| 32 | [[2607.02494]] | SamplingTAR: Typographic Attack Robustness via Concept Localization | VLM Safety / Interpretability |
| 33 | [[2607.02510]] | Online Safety Monitoring for LLMs | LLM Safety / Risk Control |
| 34 | [[2607.02513]] | LACUNA: Localization Precision for LLM Unlearning | LLM Safety / Unlearning |

---

**Verification:** Overview lists 34 papers; actual `.md` files excluding `overview.md` = 34. ✅ Count matches — no discrepancy. All 34 summaries `done` (validate exit 0, 0 degraded, 0 pending).
