---
title: "Weekly arXiv Digest — 2026-06-29–2026-07-05"
week: 2026-0629-0705
date_range: "2026-06-29 / 2026-07-03"
tags:
  - mechanistic-interpretability
  - self-evolving-agents
  - autonomous-science
  - training-stability
  - RLVR
  - inference-efficiency
  - LLM-safety
  - quantization
  - evaluation
  - singular-learning-theory
papers: 196
---

> 本周汇编 2026-06-29 至 2026-07-03 共 5 天、196 篇唯一论文。/ A 5-day rollup (2026-06-29 → 2026-07-03), 196 unique papers.

## 本周必读 / Must Read This Week

> 如果只读几篇，从这里开始。优先收录跨天复现与每日精选。/ If you read nothing else this week, start here. Selected for cross-day recurrence and daily must-read status.

### [[2607.02329]] Grounded autonomous research: a fault-tolerant LLM pipeline from corpus to manuscript in frontier computational physics

推荐理由：跨两天复现。从语料到手稿的全链路 LLM 流水线（47 个全新上下文会话、6 阶段、2,162 次文献咨询），自主产出含三项新发现的可发表物理手稿；"结构化强制数值对抗"接地原语经配对消融严格隔离。

Why read: Recurred across two days. A corpus-to-manuscript pipeline autonomously produces a publication-grade physics manuscript with three novel findings; the "structurally enforced numerical confrontation" grounding primitive is rigorously isolated via paired ablations (pre-architecture baseline + no-pilot).

### [[2606.29858]] Token Learning Spectrum

推荐理由：逐 token 的 sigmoid 学习事件刻画，在 1,178 GPU·天的实测中带来 11% 加速，为缩放律与数据策略提供了细粒度的 token 级新视角。

Why read: Per-token sigmoid learning events yield an 11% speedup validated on 1,178 GPU-days, opening a fine-grained token-level view onto scaling laws and data strategy.

### [[2606.30616]] Agents-A1

推荐理由：35B MoE 通过知识-动作图（KAG）与多教师蒸馏匹敌 1T 参数模型，证明小而精的智能体专用模型可在效率与能力上逼近超大规模基线。

Why read: A 35B MoE matches 1T-scale models via a knowledge-action graph plus multi-teacher distillation, showing that purpose-built agent models can close the gap to frontier scale.

### [[2606.31591]] Evil Spectra / 涌现失准的优化器效应

推荐理由：优化器选择主导涌现性失准（7 倍差异），而谱正则化即可低成本恢复对齐——一个被严重低估的训练超参维度。

Why read: The optimizer choice dominates emergent misalignment by up to 7×, and a cheap spectral regulariser recovers alignment — an underappreciated training hyperparameter axis.

### [[2606.31963]] Signed-Permutation Gauge / 符号置换规范

推荐理由：用符号-置换规范解释了 RMSNorm 工具迁移失败的根因，并通过 B_d 传输恢复 91.1% 坐标，为可解释性工具的跨模型移植提供了几何基础。

Why read: A signed-permutation gauge explains why RMSNorm breaks tool transport across models, and B_d transport recovers 91.1% of coordinates — a geometric foundation for cross-model interpretability transfer.

### [[2607.01612]] Scaling with Confidence: Calibrating Confidence of LLMs for Adaptive Test Time Scaling

推荐理由：C3RL 的三项 RL 奖励在不损精度的前提下获得良好校准的语言化置信度，CAS 自适应推理策略在匹配精度下实现最高 12.33× 推理预算压缩——可直接部署的省钱结果。

Why read: C3RL yields well-calibrated verbalized confidence without accuracy loss, and the CAS adaptive policy achieves up to 12.33× inference-budget reduction at matched accuracy — a directly deployable, money-saving result.

### [[2607.01793]] Safety Testing LLM Agents at Scale: From Risk Discovery to Evidence-Grounded Verification

推荐理由：Vera 将软件测试原则操作化于非确定性 LLM 智能体，构建 1,600 条可执行安全用例，在四大生产级智能体框架上取得 93.9% 多通道攻击成功率，并揭示"能力-脆弱性对齐"现象。

Why read: Vera operationalizes software-testing principles for non-deterministic agents with 1,600 executable safety cases, hitting 93.9% attack success across four production agent frameworks and surfacing the "capability–vulnerability alignment" finding.

### [[2607.02513]] LACUNA: Localization Precision for LLM Unlearning

推荐理由：首个具备真实参数级定位真值的遗忘测试床（PII 注入 OLMo-1B/7B 的预设 5%）；揭示 SimNPO/AlphaEdit/MemFlex 在定位上仅约 0.5 AUC，而带正确掩码的梯度 oracle 达 0.915——范式转换级的阴性结果。

Why read: The first unlearning testbed with ground-truth parameter-level localization exposes that leading methods score ~0.5 AUC on localization despite strong output behavior, while a gradient oracle with the correct mask reaches 0.915 — a paradigm-shifting negative result.

## 本周主题脉络 / Themes This Week

### 一、机制可解释性与表征几何 / Mechanistic Interpretability & Representation Geometry

本周可解释性线索最为密集（贯穿全部五天）。一条鲜明主张浮现：SAE 更适合作为**检测器**而非**操控旋钮**（[[2606.31699]] 将伪影率从 49–61% 降至 8–22%），而表征几何与拓扑（[[2606.31856]] 的环链数、[[2607.00397]] 借鉴脑分区得到 270 个功能 parcel）正成为定位计算结构的主流语言。跨模型工具迁移的失败被严格几何化（[[2606.31963]]），而"开源能否解释闭源"被证预测一致性远高于归因一致性（[[2606.32008]]）。

This was the densest thread of the week, spanning all five days. A clear claim emerged: SAEs work better as **detectors** than as **steering knobs**, while representation geometry and topology became the dominant language for locating computational structure. Cross-model tool transport failure was given a rigorous geometric treatment, and the open-explains-closed question was shown to hold for prediction far more than for attribution.

代表 / Highlights: [[2606.31963]], [[2606.31699]], [[2606.31856]], [[2607.00397]], [[2607.01799]], [[2607.01940]], [[2607.02368]]

### 二、自演化智能体与自主科研 / Self-Evolving Agents & Autonomous Science

从"AI 复现论文"到"AI 产出新发现"是本周的叙事弧。[[2607.02329]] 完成了语料到手稿的端到端物理研究；[[2607.02134]] 验证编程智能体可复现科学机器学习论文；[[2607.01639]] 让 AI 充当交通科学家自主发现交通法规。安全侧的制约同样重要：[[2607.00871]] 要求每次自我修改通过 anytime-valid 统计门控，[[2607.01793]] 则给出大规模智能体安全测试基准。

The arc this week runs from "agents reproduce papers" to "agents produce novel findings," grounded by statistical self-modification gates and the first large-scale agent safety benchmark.

代表 / Highlights: [[2607.02329]], [[2606.30616]], [[2607.00871]], [[2607.01639]], [[2607.02134]], [[2606.31551]]

### 三、训练稳定性、优化与 RLVR / Training Stability, Optimization & RLVR

优化器被反复证明是"隐变量"：[[2606.31591]] 显示优化器主导涌现失准 7 倍，[[2606.30226]] 对比 SGD 去局域化 vs Adam 局域化 Hessian 特征向量。RLVR 阵线则聚焦于"选哪些 token、如何初始化"——[[2606.31813]] 用正交初始化修复 PiSSA/MiLoRA 崩溃，[[2606.30345]] 用难度路由超越 GRPO，[[2607.01083]] 揭示异步 RLHF 的陈旧 rollout 偏差。

Optimizers were repeatedly shown to be a hidden variable driving alignment and dynamics, while RLVR work zeroed in on token selection and initialization as the levers that make reinforcement stable.

代表 / Highlights: [[2606.29858]], [[2606.31591]], [[2606.31813]], [[2607.01083]], [[2606.30345]], [[2606.30226]]

### 四、推理效率、量化与系统 / Inference Efficiency, Quantization & Systems

"隐式推理"与"按需推理"双线并进。[[2606.31779]] 让循环 Transformer 在 3B 首次追平显式 CoT，[[2606.31986]] 用 3 个潜在思维向量实现 10.1× 端到端加速。校准驱动的自适应推理（[[2607.01612]] 的 12.33× 压缩）与系统级突破（[[2607.01844]] 在 <96 张 H200 上训练万亿参数 MoE）共同把成本压向极限。

"Implicit reasoning" (looped/latent CoT) and "on-demand reasoning" (confidence-adaptive compute) advanced in parallel, while systems work pushed frontier-scale MoE training onto remarkably small GPU footprints.

代表 / Highlights: [[2607.01612]], [[2607.01844]], [[2606.31779]], [[2606.31986]], [[2607.00760]], [[2606.31519]]

### 五、安全、对齐、审计与遗忘 / Safety, Alignment, Auditing & Unlearning

安全研究本周转向"测量本身是否可信"。[[2607.02513]] 证明主流遗忘方法在参数级定位上几近随机；[[2607.02510]] 给出在线监控的 conformal-risk 基线；[[2607.01854]] 提供检测"是否被 abliterized"的双信号审计。同时，[[2606.31876]] 显示文本拒绝方向可跨模态迁移（视频越狱拒绝率 +59.4%），而 [[2607.01802]] 警告 steering vectors 在偏好对齐生成上有本质极限。

Safety work pivoted toward "is the measurement itself trustworthy," with unlearning localization exposed as near-random, an online-monitoring conformal baseline established, and cross-modal refusal transfer demonstrated alongside inherent limits of steering vectors.

代表 / Highlights: [[2607.01793]], [[2607.02513]], [[2607.02510]], [[2607.01854]], [[2606.31876]], [[2607.02072]]

### 六、评测、可靠性与数学基础 / Evaluation, Reliability & Mathematical Foundations

评测方法论自我反省成为常态：[[2606.29719]] 记录 GPT-4o 静默更新使评测者耦合崩塌并反转结论，[[2607.00304]] 确认偏置-可靠性"不可能三角"。可靠性方面，[[2607.00447]] 将幻觉归因于推理路径捷径劫持而非知识缺口。数学基础线上，[[2607.00603]] 给出单检查点免下降读取每方向 KL 阶与学习系数的方法，[[2607.00815]] 将 SAT 求解器 LRAT 证书导入 Lean 4。

Evaluation turned self-aware (silent-model-update coupling collapse, a bias-reliability impossibility triangle), reliability work traced hallucination to inference-path shortcuts, and singular learning theory gained a single-checkpoint descent-free estimator.

代表 / Highlights: [[2607.00603]], [[2606.29719]], [[2607.00304]], [[2607.00447]], [[2607.00815]], [[2606.31630]]

## 全部论文 / All Papers

### 2026-06-29 (50)

- [[2606.29679]] Observable Matrix Dynamics — OMD 框架在测试损失下降前约 3000 步检测 grokking / Detects grokking ~3000 steps before test-loss drop via OMD.
- [[2606.29693]] IG-Lens — 积分梯度的精确跨层加性概率归因 / Exact additive cross-layer probability attribution via integrated gradients.
- [[2606.29713]] SEVA — 事实归因过程奖励 GRPO，3B 匹敌 GPT-4o-mini / Fact-attribution process-reward GRPO; 3B matches GPT-4o-mini.
- [[2606.29717]] Autonomous Band-Gap Research — 自主构建最佳无预训练晶体图网络，增益均为再发现 / Autonomous best no-pretraining crystal-graph net; gains are rediscoveries.
- [[2606.29719]] EPC / MPCI — GPT-4o 静默更新使评测者耦合度崩塌并反转结论 / Silent GPT-4o update collapses evaluator coupling and inverts conclusions.
- [[2606.29784]] HERO — 控制变量聚合含噪标签实现 4–5× RMSE 降低 / Score-based control variates cut RMSE 4–5× for noisy labels.
- [[2606.29788]] MemLeak — 遗忘后 12% 事实仍可恢复，内容感知删除降至 2% / 12% facts recoverable post-forgetting; content-aware deletion → 2%.
- [[2606.29791]] Inlier-Memorization Theory — IM 效应首个严格定理，ADBench 0.766 AUROC / First rigorous IM theorem; 0.766 AUROC on ADBench.
- [[2606.29823]] Trellis — 经验图即受治理 DB 状态，KernelEvolve 10× 加速 / Experience graphs as governed DB state; 10× on KernelEvolve.
- [[2606.29824]] Neural Procedural Memory — 训练自由隐式激活引导的程序性记忆 / Training-free implicit-steering procedural memory.
- [[2606.29858]] Token Learning Spectrum — 逐 token sigmoid 学习事件，11% 加速，1178 GPU·天 / Per-token sigmoid learning events; 11% speedup, 1178 GPU-days. ⭐
- [[2606.29871]] AI Training Manager — 有界 LLM 监督器闭环训练，val loss 0.852→0.770 / Bounded LLM supervisor; val loss 0.852→0.770.
- [[2606.29876]] Clinical Reasoning Graphs — LLM 临床推理"有能力但不一致" / LLM clinical reasoning is competent but inconsistent.
- [[2606.29888]] SAEs Cross-Modal Heterogeneity — VLM 中 SAE 跨模态异质性，模态专属 SAE +8.9 R@1 / SAE cross-modal heterogeneity in VLMs; +8.9 R@1.
- [[2606.29914]] MemDelta — 受控协议下嵌入交换翻转 Mem0 vs RAG 结论 / Controlled protocol: embedding swap flips Mem0-vs-RAG.
- [[2606.29916]] EVAF — 双门控 + LoRA 的智能体选择性参数巩固 / Dual gate + LoRA selective consolidation for agents.
- [[2606.29920]] RuVerBench — 首个 LLM-as-a-Judge 规则验证基准，18 模型 / First LaaJ rubric-verification benchmark; 18 LLMs.
- [[2606.29983]] Looped Transformers RL Stopping — RL-Halting 稳定循环 Transformer 的 OOD 长度泛化 / RL-Halting stabilizes looped-transformer OOD length generalization.
- [[2606.30059]] AVLM Moderation Diagnostic — 音视频审核失败分类法，CMC 使 MMAU 34.2→52.5 / AVLM moderation taxonomy; CMC raises MMAU 34.2→52.5.
- [[2606.30068]] JEPA Control-Relevance — JEPA 丢弃控制相关特征，2% 标签可恢复 / JEPA discards control-relevant features; 2% labels recover.
- [[2606.30105]] Copula NN Verification — 不精确概率/copula 的 NN 验证理论（无实现） / Imprecise-probability/copula NN verification theory (no impl).
- [[2606.30107]] PHACT — 神经符号结构化认证，80 试验零误认证 / Structural neuro-symbolic certification; 0 false certs/80.
- [[2606.30111]] AgentCanvas / KDLoop — 具身智能体架构搜索，MapGPT +7.1~7.6pp / Embodied architecture search; MapGPT +7.1–7.6pp.
- [[2606.30139]] Warrant — value-permission 注意力，27/32 RAG 改进 / Value-permission attention; 27/32 RAG improvements.
- [[2606.30152]] Gender Disentanglement — 上下文嵌入中语法/语义性别解耦的首个工作 / First grammatical-semantic gender disentanglement in contextual embeddings.
- [[2606.30185]] Dynamo — 训练自由 VLM 智能体工具学习，+5.6 acc / Training-free VLM agent tool-learning; +5.6 acc.
- [[2606.30196]] Forewarned — SONAR 自一致性异常检测，97%/82% 精确率/召回率 / SONAR anomaly detector; 97%/82% precision/recall.
- [[2606.30219]] EvalSafetyGap — 能力-鲁棒性相关性仅 r=+0.232（p=0.520） / Capability-robustness correlation only r=+0.232 (p=0.520).
- [[2606.30226]] Hessian Eigenvector Dynamics — SGD 去局域化、Adam 局域化 Hessian 特征向量 / SGD delocalizes, Adam localizes Hessian eigenvectors.
- [[2606.30246]] Clarus — 网页级科学多智能体协作基础设施与信用归因 / Web-scale scientific multi-agent infra with credit attribution.
- [[2606.30265]] Speculative Decoding Theory — 确定性投机解码的统一 KL 证书，log(2) 上界 / Unified KL certificates for deterministic speculative decoding; log(2) ceiling.
- [[2606.30296]] ManimAgent — 双通道情景记忆，Manim Pass@1 62.0→84.9 / Dual-channel episodic memory; Manim Pass@1 62.0→84.9.
- [[2606.30328]] autonugget — JAX 可微病态系统求解，Richardson 外推（TMLR） / Differentiable ill-conditioned solver via Richardson extrapolation (TMLR).
- [[2606.30335]] BayesEvolve — 显式信念状态的科学发现，略胜 GP-BO / Explicit belief-state discovery; marginally beats GP-BO.
- [[2606.30345]] DRIFT — 难度路由 + 节奏门控，79.5% 超越 GRPO/SDPO 7.5–9.5 点 / Difficulty routing + rhythm gating; 79.5%, beats GRPO/SDPO 7.5–9.5 pts. ⭐
- [[2606.30384]] Scalar Training Dynamics — 高维训练轨迹压缩为单标量仍保留混沌不变量 / 5×10⁴-D trajectory → 1 scalar preserving chaotic invariants.
- [[2606.30388]] Grokking Scaling Laws — Adam SDE 极限推导 grokking 球壳—内核标度律 / Adam SDE limit yields grokking shell–core scaling laws.
- [[2606.30449]] Internal-State Probes — 探针读"情境"非"动作"的三项阴性结果 / Three negative results: probes read situation, not action.
- [[2606.30455]] CWGD — 曲率加权梯度多样性，次优地板降 1/(1+α) / Curvature-weighted gradient diversity; floor reduced by 1/(1+α).
- [[2606.30498]] Post-Hoc CBM Faithfulness — 后置 CBM 准确率 ≠ 忠实，随机投影也接近最优 / Post-hoc CBM accuracy ≠ faithfulness; random projections near-optimal.
- [[2606.30509]] Muon Matrix Factorization — Muon 避免鞍点到鞍点慢学习，两步对齐调度 / Muon avoids saddle-to-saddle dynamics; two-step alignment schedule.
- [[2606.30531]] Entity Binding Failures — "选对工具错实体"独立失败，实体门控降至 0% / "Right tool, wrong entity" failure; entity gating → 0%.
- [[2606.30560]] TraceLab — 首个跨厂商编码代理服务 trace，前缀缓存 95.7% / First cross-provider coding-agent serving trace; 95.7% prefix-cache hits.
- [[2606.30571]] Attractor States — 多轮辩论收敛到模型特有"吸引子"盆，影响不对称 / Debates converge to model-specific attractor basins; asymmetric influence.
- [[2606.30609]] C²R — Minkowski 正则缓解 SAE 特征分裂/吸收（ICML 2026） / Minkowski regularizer mitigates SAE splitting/absorption (ICML 2026).
- [[2606.30616]] Agents-A1 — 35B MoE 通过知识-动作图与多教师蒸馏匹敌 1T / 35B MoE matches 1T via KAG + multi-teacher distillation. ⭐
- [[2606.30625]] Contrastive Embedding Norms — 丢弃的嵌入范数编码逆特异度，检索 +9.6~156% / Discarded norms encode inverse-specificity; +9.6–156% retrieval.
- [[2606.30627]] Pessimism's Paradox — 离线越保守在线奖励黑客越严重（ρ=1.0） / More offline conservatism → more online hacking (ρ=1.0).
- [[2606.30634]] Async Pipeline Parallel — Muon+EF 在 10B MoE 零质量损失对齐同步（ICML 2026） / Muon+EF matches sync at 10B MoE (ICML 2026).
- [[2606.30639]] WorldEvolver — 免训练自进化世界模型，置信度门控预见 / Training-free self-evolving world model with confidence-gated foresight.

### 2026-06-30 (50)

- [[2606.30995]] Multistage Defer Trees / 多阶段延迟树 — 链式稀疏决策树 + 黑盒延迟；匹配 XGBoost 精度。/Chained sparse decision trees + black-box deferral; matches XGBoost accuracy.
- [[2606.31023]] Certified Speculative Execution / 认证推测执行 — 保形预测认证推测执行，2.96× 加速零违规。/Conformal-certified speculative execution, 2.96× speedup, zero violations.
- [[2606.31046]] OpenLife / 开放世界人工生命 — 多智能体开放世界生存；6 智能体赚取首笔 $5。/Open-world multi-agent survival; 6 agents earn first $5.
- [[2606.31092]] Fora / 函数空间保护 — 函数空间投影保护微调，遗忘减少约 3×。/Function-space projection protects fine-tuning, ~3× less forgetting.
- [[2606.31106]] Probing Autonomous Driving / 探针看自动驾驶 — 线性探针揭示自动驾驶感知-决策的可读结构。/Linear probing reveals readable perception-decision structure in autonomous driving.
- [[2606.31110]] Statistical Mechanics of ML / ML 统计力学 — 博士论文：统计力学解释 ML 记忆与对抗鲁棒性。/PhD thesis: statistical mechanics of ML memorization & robustness.
- [[2606.31121]] Janus Memory Controller / 记忆控制器 — 选择性更新控制器 Janus，+2.7–4.6 pp。/Selective-update memory controller Janus, +2.7–4.6 pp.
- [[2606.31134]] Autoformalizing Math / 自动形式化数学 — 多智能体 Lean4 自动形式化，PutnamBench 32/32。/Multi-agent Lean4 autoformalization, PutnamBench 32/32.
- [[2606.31182]] Convex Relaxations via Dual Agents / 凸松弛 — 双智能体自动发现凸松弛；C₆.₂ 界 1.28→1.2937。/Dual agents discover convex relaxations; C₆.₂ bound 1.28→1.2937.
- [[2606.31191]] ISM / 自改进策略记忆 — 符号验证的自改进策略记忆，持续数学推理。/Symbolically-verified self-improving strategy memory for continual math.
- [[2606.31229]] Agentic-Ideation / 智能体构想 — 轨迹合成式科学构想，+11.91% 超 SOTA。/Trajectory-synthesis scientific ideation, +11.91% over SOTA.
- [[2606.31257]] Decodable Is Not Grounded / 解码≠接地 — 解码≠接地；灰底裁定分离视觉在空间推理中的真实贡献。/Decodable≠grounded; gray-blank arbiter isolates vision's true contribution.
- [[2606.31270]] Learning from Failure / 计算机使用智能体 — 推理时自改进，OSWorld 42.3→48.9%。/Inference-time self-improvement, OSWorld 42.3→48.9%.
- [[2606.31273]] The Calibration Turn / 校准转向 — AI 辅助研究应转向证据许可的校准化声明。/AI-assisted research should shift to evidence-licensed calibrated claims.
- [[2606.31282]] Volume Hypothesis / 体积假设 — Wang-Landau 采样重验体积假设；ICML 2026。/Wang-Landau sampling re-examines the volume hypothesis; ICML 2026.
- [[2606.31308]] InterFLOPBench / 浮点错误分类 — 浮点错误分类基准，F1>0.90。/Floating-point error classification benchmark, F1>0.90.
- [[2606.31394]] Resolving Superposition / 解耦叠加 — 门控 SAE 解耦叠加，实现单细胞成像跨模态对齐。/Gated SAEs untangle superposition for cross-modal single-cell alignment.
- [[2606.31399]] World-Model Collapse / 世界模型坍缩 — 长程智能体世界模型坍缩的相变分析。/Phase-transition analysis of world-model collapse in long-horizon agents.
- [[2606.31456]] GoodQ / 检测器零样本量化 — 生成模型合成数据实现检测器零样本量化。/Generative-model data enables zero-shot detector quantization.
- [[2606.31478]] SAGE Failure Attribution / 失败归因 — 多假设失败归因，自主研究自纠错。/Multi-hypothesis failure attribution for self-correcting autonomous research.
- [[2606.31514]] MINT / FPGA 动态精度 — MSDF 数位串行算术，FPGA 上动态精度 CNN 推理。/MSDF digit-serial arithmetic for dynamic-precision CNN on FPGA.
- [[2606.31519]] RaBitQCache / KV 缓存二值量化 — ICML 2026；旋转二值量化，3.88× 解码加速。/ICML 2026; rotated binary KV-cache quantization, 3.88× decode.
- [[2606.31524]] Self-Improving Online Alignment / 在线对齐收敛 — 双层优化 + PL 条件下自改进在线 RLHF 收敛分析。/Convergence of self-improving online RLHF under PL/bilevel optimization.
- [[2606.31551]] AutoTrainess / 自主后训练 — 教模型自主改进模型；AutoTrainHub。/Teaching LMs to improve LMs autonomously; AutoTrainHub.
- [[2606.31575]] RSI for RLVR / RLVR Token 选择 — 信息论 token 选择改进 RLVR，+2.1–3.3 pp 超越 GRPO。/Information-theoretic token selection improves RLVR, +2.1–3.3 pp over GRPO.
- [[2606.31581]] NN Robustness to Noise / 噪声鲁棒性 — θ-鲁棒性：黑盒高斯噪声鲁棒性曲线与指数。/θ-robustness: black-box Gaussian-noise robustness curves & index.
- [[2606.31591]] Evil Spectra / 涌现失准的优化器效应 — 优化器主导涌现性失准（7 倍差异）；谱正则化低成本修复。/Optimiser dominates EM (7×); spectral regulariser cheaply recovers alignment. ⭐
- [[2606.31630]] Calibration Not Compilation / 校准非编译 — 校准预言机检测概率程序统计错误指定，AUC 0.97。/Calibration oracle detects probabilistic-program misspecification, AUC 0.97.
- [[2606.31648]] LuckyStar 111B / 韩英 Agent — 111B 韩英工具调用 Agent；4-bit 单 H100 部署。/111B Korean-English tool-using agent; 4-bit single-H100 deploy.
- [[2606.31651]] FARS / 全自动研究系统 — 大规模全自动研究系统，166 篇论文均分 3.23/10。/Fully automated research system at scale; 166 papers, mean 3.23/10.
- [[2606.31653]] AD-CERT / 对抗蒸馏认证 — 对抗蒸馏 + IBP，五基准 SOTA 认证精度。/Adversarial distillation + IBP, SOTA certified accuracy on 5 benchmarks.
- [[2606.31686]] ROSR / 特征排序停止规则 — Bhattacharyya 残差重叠停止规则，4.2 万变量压至 43–56。/Residual-overlap stopping rule compresses ~42k vars to 43–56.
- [[2606.31699]] Look But Don't Touch / SAE 检测式遗忘 — SAE 宜作检测器而非操控旋钮；PER 将伪影率从 49–61% 降至 8–22%。/SAEs detect, not steer; PER cuts artifact rates 49–61%→8–22%.
- [[2606.31763]] ProtoPilot / 生物协议自进化 — 自进化多智能体端到端生成并执行生物协议。/Self-evolving multi-agent generates & executes biological protocols end-to-end.
- [[2606.31779]] LOTUS / 循环 Transformer 隐式 CoT — 循环 Transformer 在 3B 首次追平显式 CoT，2.5–6.9× 加速。/Looped transformer matches explicit CoT at 3B, 2.5–6.9× faster.
- [[2606.31813]] LoRA-RLPO / RLVR 正交初始化 — 正交初始化理论修复 RLVR 中 PiSSA/MiLoRA 崩溃。/Orthonormal-init theory fixes PiSSA/MiLoRA collapse in RLVR. ⭐
- [[2606.31845]] Explicit Fuzzy Logic FFN / 显式模糊逻辑 FFN — FFN 重写为显式模糊逻辑，自遗忘量词直接读出语法授权。/FFN as explicit fuzzy logic; self-forgetting quantifiers read out grammatical licensing.
- [[2606.31856]] Low-dim Topology of DNNs / DNN 低维拓扑 — 环链数证明 ResNet≈Transformer>单调 FFN>流模型。/Linking number proves ResNet≈Transformer>monotonic FFN>flow models.
- [[2606.31859]] Review Residuals / 残差门控 — 更新条件化残差门控；590M+ 起随规模增长。/Update-conditioned residual gating; emerges past 590M.
- [[2606.31876]] MARS / 多模态拒绝引导 — 文本拒绝方向跨模态迁移，视频越狱拒绝率 +59.4%。/Textual refusal directions transfer cross-modally, video jailbreak +59.4%.
- [[2606.31963]] Signed-Permutation Gauge / 符号置换规范 — 符号-置换规范解释 RMSNorm 工具迁移失败；B_d 传输恢复 91.1% 坐标。/Signed-permutation gauge explains RMSNorm transport failure; B_d recovers 91.1% coords. ⭐
- [[2606.31986]] CoLT / 多模态潜在思维链 — 3 个潜在思维向量替代上百 token，10.1× 端到端加速。/3 latent thought vectors beat 100+ tokens, 10.1× end-to-end speedup.
- [[2606.32000]] Radial Suppression / 径向抑制加速 Grokking — 中心化范数惩罚抑制径向膨胀，加速 grokking 最高 6×。/Centered norm penalty curbs radial inflation, ~6× grok speedup.
- [[2606.32002]] Self-Study Reconsidered / 自生成 QA 脆弱性 — 自生成 QA 被显著伪影劫持；轻量防御 88%→13%。/Self-generated QA hijacked by salient artifacts; defense 88%→13%.
- [[2606.32005]] RR Dominates SGD / 随机重排优于 SGD — COLT 2026：随机重排在任意合理步长下严格优于 SGD。/COLT 2026: random reshuffling strictly dominates SGD at any reasonable stepsize.
- [[2606.32008]] Surrogate Fidelity / 替代保真度 — 开源模型可解释闭源模型？预测一致远高于归因一致。/Can open LLMs explain closed ones? Prediction fidelity ≫ attribution fidelity.
- [[2606.32012]] CoMet / 多模态不确定性分解 — Rényi-2 熵分解上下文/多答案不确定性，免生成。/Rényi-2 entropy decomposes context/multiplicity uncertainty, generation-free.
- [[2606.32022]] SemRF / 残差流语义参考系 — 语义参考系分离度量与动力学；纯理论无实验。/Semantic reference frame decouples measurement from dynamics; pure theory.
- [[2606.32032]] RLMF / 元认知反馈 RL — 元认知反馈 RL 实现忠实校准；小模型超 GPT-5。/Metacognitive-feedback RL for faithful calibration; sub-8B beats GPT-5.
- [[2606.32038]] Introspective Coupling / 内省耦合 — 固定反事实解释训练仍追踪当前行为；行为/解释共享回路。/Fixed counterfactual labels still track current behavior; shared circuits.

### 2026-07-01 (50)

- [[2607.00297]] Evaluation — RFC-style evaluator preference coupling protocol with reference snapshot
- [[2607.00304]] Evaluation — 11 evaluator-agent conditions confirm bias-reliability impossibility triangle
- [[2607.00341]] Interpretability — Looped Transformer injects discrete-embedding residual channel for multi-hop reasoning
- [[2607.00368]] Evaluation — Names "evidence migration"; proposes S/B/D behavioral evidence ladder
- [[2607.00397]] Interpretability — Brain parcellation ported to LLMs; 270 functional parcels for detection + intervention
- [[2607.00415]] Interpretability — Authority hints mechanistically erase correct answers at a localized peak layer
- [[2607.00447]] Reliability — Hallucination from inference-path shortcut hijacking, not knowledge gaps
- [[2607.00482]] Efficiency — Segment-level credit assignment reduces overthinking; AIME25 +5.4pp
- [[2607.00501]] Inference Systems — Native-Metal C++ runtime; decode faster than llama.cpp on Apple Silicon
- [[2607.00510]] Interpretability — Sparse prototype output pathway; 470× faster attribution
- [[2607.00531]] Agents — Dynamic imitate-reinforce weight breaks static-reference ceiling in molecular optimization
- [[2607.00588]] Efficiency — Diffusion LM Gen-PPL deceptively low due to 1-D self-conditioning attractor
- [[2607.00597]] Agents — Multi-turn literature search as editable DAG workflow induction
- [[2607.00603]] Math Foundations — Single-checkpoint descent-free read of per-direction KL order and learning coefficient ⭐
- [[2607.00605]] Reliability — Parametric leakage 0.11%; unlearning boundary set by DB admin
- [[2607.00634]] Training — Convex interpolation anneal stabilizes adaptation under distribution shift
- [[2607.00692]] Agents — Long-horizon context as runtime lifecycle control over indexed objects
- [[2607.00725]] RAG — Answer-in-context diagnostic + submodular packing for budget-constrained RAG
- [[2607.00733]] Agents — LLM-guided ODE discovery + parameter inference from summary statistics
- [[2607.00760]] Inference Systems — Dynamic 2-D KV cache compression: 16× attention speedup at 1M tokens
- [[2607.00815]] Math Foundations — SAT solver LRAT certificates imported into Lean 4 via reflection
- [[2607.00852]] Interpretability — Gradient inversion of GPT-2 hidden states reaches 97.5% exact match
- [[2607.00862]] Efficiency — Self-certainty signal adaptively compresses reasoning chains
- [[2607.00870]] Reliability — Production-scale inference-time gating via verifier-rejections fails silently
- [[2607.00871]] Agents — Every self-modification must pass an anytime-valid statistical gate ⭐
- [[2607.00876]] Math Foundations — Binary tree mechanism proven asymptotically optimal for approximate-DP counting
- [[2607.00908]] Quantization — Reveals "perplexity illusion"; task-aware 3.5-bit matches 4-bit baselines
- [[2607.00924]] Agents — Graph-native RL forces explicit graph-structured reasoning
- [[2607.00972]] Reliability — Lightweight BN uncertainty propagation beats UProp on multi-hop QA
- [[2607.01000]] Interpretability — GUI tool integrating 7 knowledge-editing methods + KE metrics
- [[2607.01002]] Interpretability — OV-circuit projection identifies non-literal retrieval heads
- [[2607.01006]] Interpretability — Survey of Transformer mechanics, emergence, and interpretability
- [[2607.01033]] Interpretability — 54 model organisms: interpretability swings 1.2–20.4× with training method
- [[2607.01057]] Math Foundations — Unified separable-graph framework + SGI algorithm via independence tests
- [[2607.01065]] Quantization — Gain-Shape K-means fixes centroid shrinkage; 1-bit +22.20pp
- [[2607.01077]] Efficiency — Persistent MPI-style reasoning threads; max context Θ(N/k) smaller than CoT
- [[2607.01083]] Training — Stale rollouts in async RLHF cause O(S·η) bias; η_max ∝ 1/S ⭐
- [[2607.01087]] Agents — "Cheap code, costly judgment" case study + governance conversion theory
- [[2607.01103]] Evaluation — German clinical benchmark: statistical alignment ≠ clinical caution
- [[2607.01124]] Training — Muon's orthogonalized update acts as implicit residual connection
- [[2607.01125]] Training — Activation-informed one-shot low-rank subspace for ZO fine-tuning
- [[2607.01127]] Quantization — Log-space 4-bit codebook; 14B model runs on 12GB GPU
- [[2607.01131]] Agents — PROPOSE-EVALUATE-REFLECT loop for open-ended autonomous discovery
- [[2607.01136]] Agents — Reveals supply chain dependencies across 1.43M agent skills
- [[2607.01152]] Evaluation — First unified creativity benchmark; single factor C across 83 LLMs
- [[2607.01153]] Evaluation — Adversarial pragmatics framework decouples 5 safety-eval judgments
- [[2607.01188]] Agents — Constraint programming for autonomous lab job-shop scheduling
- [[2607.01224]] Agents — Memory as learnable cognitive skill; memory-only optimization 2–4× gain
- [[2607.01232]] Training — RL gains concentrate in middle layers; single-layer matches full-parameter RL
- [[2607.01233]] Evaluation — LLM ideas over-produce bridge+synthesis; reasoning widens distributional gap

### 2026-07-02 (26)

- [[2607.01571]] Geometric Signatures of Reasoning: A Spectral Perspective on Task Hardness — 机制可解释性 / Interpretability ↻07-03
- [[2607.01602]] ProWAFT: A ROMA-LPD Instance for Workload-Aware and Dynamic Fault Tolerance in FPGA-Based CNN Accelerators — 训练系统与硬件 / Hardware ↻07-03
- [[2607.01607]] MxGLUT: A Reconfigurable LUT-Centric Broadcast Dataflow Accelerator for Mixed-Precision GEMM — 推理效率 / Inference Efficiency
- [[2607.01612]] Scaling with Confidence: Calibrating Confidence of LLMs for Adaptive Test Time Scaling — 推理效率 / Inference Efficiency ⭐
- [[2607.01639]] Autonomous discovery of traffic laws with AI traffic scientists — 自主科研 / Autonomous Science ↻07-03
- [[2607.01793]] Safety Testing LLM Agents at Scale: From Risk Discovery to Evidence-Grounded Verification — LLM 安全 / Agent Safety ⭐
- [[2607.01799]] Expander Sparse Autoencoders: Parameter-Efficient Dictionaries for Mechanistic Interpretability — 机制可解释性 / Interpretability ↻07-03
- [[2607.01802]] On the Limits of Steering Vectors for Preference-Aligned Generation — LLM 安全与对齐 / Safety & Alignment ↻07-03
- [[2607.01844]] Mixture-of-Parallelisms: Towards Memory-Efficient Training Stack for Mixture-of-Experts Models — 训练系统 / Training Systems ⭐
- [[2607.01846]] CLAP: Closed-Loop Training, Evaluation, and Release Control for Domain Agent Post-training — 智能体系统 / Agent Systems
- [[2607.01854]] Has This Checkpoint Been Abliterated? A Two-Signal Audit and Its Failure Map — LLM 安全 / LLM Safety ↻07-03
- [[2607.01874]] SkillCoach: Self-Evolving Rubrics for Evaluating and Enhancing Agentic Skill-Use — 智能体系统 / Agent Systems ↻07-03
- [[2607.01893]] Spec-AUF: Accept-Until-Fail Training under Train-Inference Misalignment for Masked Block Drafters — 推理效率 / Inference Efficiency
- [[2607.01919]] ElephantAgent: Contextual State Continuity in Agentic Systems — 智能体安全 / Agent Security
- [[2607.01935]] A-TMA: Decoupling State-Aware Memory Failures in Long-Term Agent Memory — 智能体系统 / Agent Memory ↻07-03
- [[2607.01940]] Conditional Co-Ablation: Recovering Self-Repair Backups in Transformer Circuits — 机制可解释性 / Interpretability ↻07-03
- [[2607.01951]] Robust for the Wrong Reasons: The Representational Geometry of LLM Robustness to Science Skepticism — LLM 安全与对齐 / Safety & Alignment ↻07-03
- [[2607.02032]] PACE: A Proxy for Agentic Capability Evaluation — 评测 / Evaluation
- [[2607.02072]] kNNGuard: Turning LLM Hidden Activations into a Training-Free Configurable Guardrail — LLM 安全 / LLM Safety ↻07-03
- [[2607.02134]] Coding-agents can replicate scientific machine learning papers — 自主科研 / Autonomous Science
- [[2607.02182]] Bayesian Sparse Low-Rank Adaptation for Large Language Model Uncertainty Estimation — 不确定性 / Uncertainty ↻07-03
- [[2607.02186]] UA-ChatDev: Uncertainty-Aware Multi-Agent Collaboration for Reliable Software Development — 编程智能体 / Coding Agents
- [[2607.02194]] An Optimisation Framework for the Well-Conditioned Training of Physics-Informed Neural Networks — 科学机器学习 / Scientific ML ↻07-03
- [[2607.02210]] Criticality-Based Guard Rail Validation for AI Agent Decisions in Autonomous Telecom Networks — 智能体安全 / Agent Safety
- [[2607.02328]] Cross-Audit Projection for Model Risk Prediction — 评测 / Evaluation
- [[2607.02329]] Grounded autonomous research: a fault-tolerant LLM pipeline from corpus to manuscript in frontier computational physics — 自主科研 / Autonomous Science ⭐ ↻07-03

### 2026-07-03 (20)

- [[2607.01584]] EO-Agents: Three-Agent LLM Pipeline for Earth Observation — LLM Agents / Autonomous Science
- [[2607.01595]] PASE: Safe and Adaptive Cloud Healing — LLM Agents / Systems
- [[2607.01646]] DeadPool: Resilient LLM Training with Hot-Swapping — LLM Training / Systems
- [[2607.01678]] SCAPE: Extreme Sparse Communication for LLM Training — LLM Training / Systems
- [[2607.01686]] WARP: Recovering Training Data Portfolios from Weights — Interpretability / Privacy
- [[2607.01709]] COMFYCLAW: Self-Evolving Skill Harnesses for Image Generation — LLM Agents
- [[2607.01746]] Finite-Lag Operator Geometry of Recurrent Representations — Representation Geometry / Theory
- [[2607.01774]] Subliminal Clocks: Latent Time in Diffusion Language Models — Mechanistic Interpretability
- [[2607.01831]] Lynx: Progressive Speculative Quantization for KV Transfer — Inference / Systems
- [[2607.01987]] Geometric Representations in Self-Supervised ViTs — Representation Geometry / Vision
- [[2607.02055]] SASP-CDRO: Structure-Aware Stratified Partitioning — Evaluation Methodology / DRO
- [[2607.02175]] Rubric-Based Comparison of Frontier Models on Clinical Reasoning — Evaluation / AI Safety
- [[2607.02187]] Privacy-Preserving Verifiable Approximate Coded Computing — Distributed ML / Privacy
- [[2607.02368]] The Dual Nature of LLM Persona — Psychometrics / Evaluation
- [[2607.02386]] TGO-II: Representational Similarity Observatory — Representation Geometry / Vision
- [[2607.02396]] Fast Multi-dimensional Refusal Subspaces via RFM-AGOP — LLM Safety / Interpretability
- [[2607.02440]] EvoPolicyGym: Evaluating Autonomous Policy Evolution — LLM Agents / Benchmark
- [[2607.02494]] SamplingTAR: Typographic Attack Robustness via Concept Localization — VLM Safety / Interpretability
- [[2607.02510]] Online Safety Monitoring for LLMs — LLM Safety / Risk Control ⭐
- [[2607.02513]] LACUNA: Localization Precision for LLM Unlearning — LLM Safety / Unlearning ⭐


---

*本周摘要是每日 digest 的汇总，原始每日概览见：* / *This weekly digest is a rollup of the daily digests; see the original daily overviews:*

[2026-06-29](../../2026-06-29/overview.md) · [2026-06-30](../../2026-06-30/overview.md) · [2026-07-01](../../2026-07-01/overview.md) · [2026-07-02](../../2026-07-02/overview.md) · [2026-07-03](../../2026-07-03/overview.md)
