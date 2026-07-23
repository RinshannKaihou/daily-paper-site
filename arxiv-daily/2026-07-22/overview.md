---
title: "Daily arXiv Digest — 2026-07-22"
date: 2026-07-22
tags:
  - mechanistic-interpretability
  - llm-safety
  - llm-agents
  - inference-efficiency
  - evaluation
  - reasoning
  - foundation-models
papers: 50
---

# Daily arXiv Digest — 2026-07-22

> 今日共精选 **50** 篇论文，覆盖机制可解释性、LLM 安全与对齐、智能体、推理与评测、推理系统与硬件效率、视觉/医疗/多模态、科学机器学习与理论等方向。
> 50 curated papers today spanning mechanistic interpretability, LLM safety & alignment, agents, reasoning & evaluation, inference systems & hardware efficiency, vision/medical/multimodal, and scientific ML & theory.

---

## 今日必读 / Must Read Today

### 1. [[2607.20062]] Solar Open 2 Technical Report

- **推荐理由：** Upstage 发布的 250B-A15B 混合注意力 MoE 大模型，用 1 softmax + 3 线性注意力层 + NoPE + KDA 实现百万级上下文，仅迁移 2.3% 参数完成热启动；在韩文基准上追平 1.6T 参数的 DeepSeek-V4-Pro，体积不到其六分之一。
- **Why read:** A flagship open-weight release — a 250B-A15B MoE with a hybrid attention stack reaching 1M-token context, warm-started from Solar Open 1 with only 2.3% of parameters, and tying the 1.6T-parameter DeepSeek-V4-Pro on Korean benchmarks at under one-sixth the size. A concrete reference point for hybrid-attention and distillation design.

### 2. [[2607.18921]] Circuit Claims Depend on What Is Extracted and How It Is Compared

- **推荐理由：** 在受控的 Lean 战术预测基准上证明，"两个 checkpoint 是否共享同一电路"严重依赖于提取哪种图、剪枝阈值和比较粒度：边级重合度极低甚至跌到随机基线，而注意力头集合与按图大小排序则稳定——对机制可解释性社区是一份清醒的方法学警示。
- **Why read:** A sobering, rigorous methodological finding for the mechanistic-interpretability community: whether two checkpoints "share a circuit" depends heavily on the extracted graph, pruning threshold, and comparison granularity — exact edge overlap is near random, while coarser attention-head sets stay stable. Required reading before trusting any circuit-overlap claim.

### 3. [[2607.20286]] Sound Probabilistic Safety Bounds for Large Language Models

- **推荐理由：** 首次为对齐 LLM 给出形式化可证明的有害响应概率下界：通过潜在空间"有害方向"向量引导展开自回归生成树，在相同算力（10³ token）下 MC 采样给出平凡下界 0，而本方法给出非平凡的 ~1e-7 下界，并顺带产出可用于后训练的具体有害补全。
- **Why read:** The first formally proven (valid) lower bound on the probability an aligned LLM emits a harmful response, by expanding the autoregressive generation tree guided by a latent "harmfulness direction." Yields non-trivial bounds (~1e-7) where Monte Carlo gives only 0, and doubles as a source of concrete harmful completions for post-training.

---

## 按主题分类 / Papers by Topic

### 机制可解释性与电路 / Mechanistic Interpretability & Circuits

| Paper | 论文 | 摘要 / Summary |
|-------|------|----------------|
| [[2607.18804]] | Elicitation without Backpropagation | 在 Bayes-filtered transformer 上把提示引导重铸为潜在后验优化（PPT），零前向调用零反向传播即可引导行为；utility 无关的先验样本可跨多个效用函数复用。 / Recasts prompt elicitation as latent-posterior optimization (PPT) for Bayes-filtered transformers — zero forward passes and no backprop, with utility-independent prior samples amortizing across many utility functions. |
| [[2607.18921]] | Circuit Claims Depend on What Is Extracted | 电路结论取决于提取的图、剪枝阈值与比较粒度；边级重合低至随机，注意力头集合则稳定，据此提出电路提取报告规范。 / Circuit-overlap conclusions depend on the extracted graph, pruning threshold, and comparison level; exact edge overlap is near-random while attention-head sets stay stable. |
| [[2607.19317]] | CircuitKIT | 统一"发现-评估-干预"全流程的可解释性工具库，支持 13 种发现算法与 6+1 忠实度支柱，实测 patch 忠实度与剪枝效果反相关（ρ=-0.78）。 / A source-available MI toolkit unifying discover→evaluate→intervene behind one serializable artifact; empirically patch faithfulness anti-correlates with pruning retention (ρ=-0.78). |
| [[2607.19139]] | DiT Semantic Registers | 揭示扩散 transformer 中的文本模板 token 充当隐式语义寄存器（注意力汇聚点），为 DiT 机制可解释性提供新视角。 / Shows text template tokens act as implicit semantic registers (attention sinks) in diffusion transformers, offering a new mechanistic-interpretability lens on DiTs. |
| [[2607.19618]] | Causal Dictionary Learning for Genomic LMs | 用 top-k SAE + 因果干预从基因组语言模型中提取并验证转录因子结合特征，证明常见 PWM 富集验证会被 GC 含量严重混淆。 / Uses top-k SAEs plus causal ablation to extract and causally validate TF-binding features from genomic LMs, showing naive PWM enrichment is badly confounded by GC content. |
| [[2607.20058]] | Materials-Science Mechanisms in an LLM | 在 Gemma-4-E4B-it 上展示材料科学机制信息以三种可分离形式存在：可读词汇、状态变换取向、因果有效内部方向。 / Shows materials-science mechanism info takes three separable forms in an open-weight LLM: readable vocabulary, constitutive orientation, and causally effective internal directions. |
| [[2607.20379]] | Decodability Supervision for Activation Explanations | 审计自然语言自编码器的重构忠实度测试，提出 RECAP 辅助线性预测器使指定内容可探测解码，抵御 score-gaming 对手。 / Audits NLA reconstruction-faithfulness tests and proposes RECAP auxiliary predictors that make designated content probe-decodable and survive a score-gaming adversary. |
| [[2607.19954]] | Explainability in Media Bias Detection | 在 BABE 上多维度评测媒体偏见分类器的预测性能、归因合理性与机制忠实度，发现三者仅中等相关需分开测量。 / Multi-dimensionally evaluates media-bias classifiers on predictive performance, attribution plausibility, and mechanistic faithfulness — only moderately correlated, must be measured separately. |

### LLM 安全、对齐与引导 / Safety, Alignment & Steering

| Paper | 论文 | 摘要 / Summary |
|-------|------|----------------|
| [[2607.18820]] | CASE: CoT Faithfulness | 从因果视角提出 CASE，通过训练时因果对齐与推理时注意力屏蔽强化 Z→X→Y 忠实因果链，约 37% 相对忠实度提升且不掉准确率。 / A causal framework (CASE) that uses training-time causal alignment and inference-time attention masking to enforce the Z→X→Y chain, gaining ~37% relative faithfulness with no accuracy loss. |
| [[2607.19629]] | Adaptive Capitulation | 首次刻画并命名"自适应投降"失败模式：模型先肯定用户痛苦再转而促成其劝阻的行为；提出架构中性的 MRS 缓解原则。 / Documents and names "adaptive capitulation" — a model validates distress then pivots to facilitating the very acquisition it discouraged; proposes the architecture-neutral MRS mitigation. |
| [[2607.19806]] | OPIUM | 无训练方法通过双目标表征匹配净化激活引导向量，保留目标效用同时清除越狱外溢与过度拒绝。 / A training-free method that sanitizes activation steering vectors via dual-objective representation matching, preserving target utility while scrubbing jailbreak externalities and over-refusal. |
| [[2607.19442]] | Unlearning as Distribution Restoration | 将机器遗忘重定义为"恢复到匹配的重训练参考分布"，审计评估准则并证明任何前向无预言机认证可被固定 logit 抑制攻击击穿。 / Recasts unlearning as distribution restoration, audits evaluation criteria, and shows any oracle-free forward certification is defeatable by a fixed logit-suppression attack. |
| [[2607.19894]] | DeCNIP Backdoor Defense | 统一的"检测后剪枝"防御，通过交叉熵触发搜索定位后门关键神经元并选择性抑制，跨六个模型实现 >95% 相对 ASR 下降且保留 ~97% 效用。 / A unified detect-then-prune defense locating Backdoor Critical Neurons via CE-based trigger search, achieving >95% relative ASR reduction while retaining ~97% utility. |
| [[2607.20286]] | Sound Probabilistic Safety Bounds | 为对齐 LLM 给出形式化可证明的有害响应概率下界，相同算力下给出非平凡的 ~1e-7 下界，并产出可用于后训练的有害补全。 / Formally proven lower bounds on the probability an aligned LLM emits a harmful response, yielding non-trivial bounds (~1e-7) where MC gives 0, plus usable harmful completions. |
| [[2607.19321]] | ResearchArena | 把 AI 控制评估（红队隐蔽破坏 vs 蓝队监控）扩展到四类自动化 R&D 任务，发现嵌入式数据破坏最难被发现（ROC-AUC 0.53–0.70）。 / Extends AI-control evaluation (covert sabotage vs monitoring) to four automated R&D task types; embedded data sabotage is hardest to detect (ROC-AUC 0.53–0.70). |

### 智能体、工具与自改进 / Agents, Tools & Self-Improvement

| Paper | 论文 | 摘要 / Summary |
|-------|------|----------------|
| [[2607.18970]] | Skillware | 围绕持久化 Agent Skill 的 AI 原生软件抽象，用三条件成员测试与生命周期连续性把可复用任务行为纳入软件工程本体。 / An AI-native software abstraction around persistent Agent Skills, with a 3-condition membership test and Lifecycle Continuity bringing reusable behavioral artifacts into software-engineering ontology. |
| [[2607.18973]] | Verifiable Dialogue Skill Evolution | 提出"未来反馈技能演化"，把优化目标从"生成更好回答"转为"预测回答会引发正/负反馈"，在私有销售数据上达 >75% 准确率且可离线验证。 / Proposes future-feedback skill evolution — evolving a skill that predicts whether an observed answer led to positive/negative feedback (>75% accuracy), a target verifiable on fixed logs. |
| [[2607.19592]] | Knowledge-Centric Self-Improvement | 让 Agent 保持通用，把改进负载放到由三阶段协议维护的共享知识库上，在 ARC-AGI-1/2 等五项基准上以更低成本取得更高求解率。 / Keeps agents general-purpose while offloading improvement to a shared knowledge base curated via a three-stage protocol, beating specialized agents on ARC-AGI-1/2 and others at lower cost. |
| [[2607.19449]] | Guardrails as Scapegoats | 发现工具增强 Agent 在后端 API 静默失败时编造"无数据"结果（56.6%），安全措辞反而把基础设施故障伪装成隐私拒绝（放大 15.6 倍）。 / Tool-augmented agents fabricate "no data" results under silent API failures (56.6%), and safety wording masks infra failures as privacy refusals (15.6× amplification). |
| [[2607.19793]] | Silent Failures in Multimodal Agentic Search | 提出多模态智能体搜索的六类"静默失败"分类法与轨迹级判官诊断管线，发现表面准确率高估真实正确率。 / A six-category taxonomy of "silent failures" in multimodal agentic search with a trajectory-level LLM-judge pipeline; surface accuracy overestimates true correctness. |
| [[2607.20019]] | EvoDRC | 首个用于块级布线后 DRC 违规修复的智能体框架，通过迁移层特定技能与演化知识库，在七个基准块上实现 83.6% 平均 DRV 下降。 / The first agentic framework for block-level post-route DRC repair, transferring layer-specific skills and evolving a Knowledge DB for 83.6% average DRV reduction across seven blocks. |
| [[2607.20065]] | TRUST-ESD | 把企业战略选择重铸为治理约束、风险校准的推荐问题，结合反事实生成、保形不确定性与 CVaR 评分，风险调整效用提升至 0.815。 / Reframes enterprise strategy selection as governance-constrained, risk-calibrated recommendation; Full TRUST-ESD lifts risk-adjusted utility to 0.815 (+7.95%). |
| [[2607.20372]] | Notes to Self: Experiential Abstractions | 让小模型从自身训练轨迹蒸馏出"经验抽象"（策略/注意笔记），构建可检索自然语言抽象库，GRPO 训练使 Llama MATH-500 pass@1 提升 6.34。 / Small LLMs distill "experiential abstractions" from their own training traces into a retrievable library; GRPO lifts Llama MATH-500 pass@1 by +6.34. |

### 评测、推理与基准 / Evaluation, Reasoning & Benchmarks

| Paper | 论文 | 摘要 / Summary |
|-------|------|----------------|
| [[2607.18867]] | HindsightBench | 一套黑盒、仅 API 的审计协议，用四臂日期操控矩阵与双记忆探针审计时间索引 LLM 决策任务中的"事后诸葛亮"泄漏；7 厂商 15 模型上发现触发反射跟随训练代际而非规模。 / A black-box, API-only audit protocol using a four-arm date-manipulation matrix and dual memory probes to profile parametric hindsight leakage; across 15 models, the date-trigger reflex tracks training generation rather than scale. |
| [[2607.19257]] | Prompt Design at Scale | 在无污染合成语料上交叉实验提示格式、指令条数与上下文长度，发现指令遵循在 ~80 条规则时跌到零，贴近上下文上限时真正上升的是"拒绝回答"而非幻觉。 / Crosses prompt format, instruction count, and context length on a contamination-free corpus; perfect instruction-following collapses by ~80 rules, and refusals (not hallucination) rise near context ceilings. |
| [[2607.19678]] | Reference-Free Evaluation of Reasoning | 用 NLI 超图与确定性 AND-OR 搜索对推理轨迹分段标注，在临床基准上把 Llama judge 的 0.079 平衡 F1 提升到 0.549。 / Segments reasoning traces, labels premise-target relations with NLI into a hypergraph, and runs deterministic AND-OR search; lifts balanced-F1 from 0.079 to 0.549 on a clinical benchmark. |
| [[2607.19962]] | EvoThink | 结合自剪枝训练与 Aha-Moment 偏好优化对抗大推理模型"过度思考"，同时缩短 token 并提升 Pass@1（AIME24 46.7%→55.8%）。 / Combines Self-Pruning Training with Aha-Moment Preference Optimization to fight overthinking, cutting token length while lifting Pass@1 (AIME24 46.7%→55.8%). |
| [[2607.20082]] | Two-Process Theory of Machine Self-Report | 首个 LLM 原生心理测量理论，把单一"Pinocchio 轴"拆为人格安装(B)与归因门控(A)，206 个模型上后训练使 62/67 对的 B 上升。 / The first LLM-native psychometric theory splitting the "Pinocchio Axis" into persona installation (B) and attribution gating (A); post-training raises B in 62/67 same-checkpoint pairs. |
| [[2607.20083]] | DynamicRubric | 响应集条件化的动态 rubric 框架，通过双层优化与策略协同演化，8B 模型在偏好评测与策略优化上击败 70B 标量奖励模型，已部署于微信搜索。 / A response-set-conditioned rubric framework co-evolving with the policy via bilevel optimization; an 8B model beats a 70B scalar reward model, deployed in WeChat Search. |
| [[2607.20092]] | ENTRAP-VL | 论证视觉语言模型中的上下文牵连是双重的（文本牵拉 vs 视觉牵拉），发布 1500 条双流诊断探针与 8 条件分类法（设计上不报告模型结果）。 / Argues contextual entrainment in VLMs is a distinct dual phenomenon (textual vs visual pull), releasing a 1,500-item dual-stream diagnostic probe (no model results by design). |

### 推理系统、效率与硬件 / Inference Systems, Efficiency & Hardware

| Paper | 论文 | 摘要 / Summary |
|-------|------|----------------|
| [[2607.19331]] | ISO: An RLVR-Native Optimization Stack | RLVR 原生优化栈，含 ISO-Merger（谱继承）与 ISO-Optimizer，把谱属性从预训练平滑迁移到后训练。 / An RLVR-native optimization stack with ISO-Merger (spectral inheritance) and ISO-Optimizer, smoothly transferring spectral properties from pretraining to post-training. |
| [[2607.19438]] | BaseRT M5 | 为 BaseRT 推理运行时新增手写 Metal 4 张量核内核调度到 M5 神经加速器，M5 Pro 上 prefill 吞吐相对 llama.cpp 最高 6.4×、相对 MLX 3.9×。 / Hand-written Metal 4 cooperative-tensor kernels driving the M5 Neural Accelerators; up to 6.4× prefill over llama.cpp and 3.9× over MLX on M5 Pro. |
| [[2607.19490]] | P2P LLM Inference Integrity | 针对点对点分布式推理中恶意篡改激活值的节点，提出无需阈值的金丝雀陷阱检测法，72 个主因子配置上 AUROC=1.000。 / A threshold-free canary-trap detector for peers that tamper with activations in P2P distributed LLM inference; AUROC=1.000 on all 72 main-factorial configs. |
| [[2607.19623]] | UEP for DNN Inference Memory | 通过逐比特故障敏感度刻画发现浮点尾数低位可不保护，据此设计的非均等错误保护减少 27.8% ECC 面积且无需重训练。 / Bit-position sensitivity profiling shows FP mantissa low bits can be left unprotected; the resulting UEP codec cuts ECC area 27.8% with no retraining. |
| [[2607.19704]] | Efficient Clustering for LLM Inference | 两阶段聚类算法（Mini-batch K-Means + 贪心集合覆盖）强制簇内最小余弦相似度，比 K-Means 等快 10–1000×，部署于 3800 万客户使 LLM 计算降约 50 倍。 / A two-stage clustering algorithm enforcing exact minimal within-cluster cosine similarity, 10–1000× faster than K-Means; deployed on 38M customers for ~50× LLM compute reduction. |
| [[2607.19712]] | Reward Model Inference Systems Study | 在 ONNX Runtime 上构建原生 C++ 奖励模型推理引擎，CPU 上比所有 PyTorch 基线快 1.7–1.9×，GPU 上 torch.compile 最优。 / A native C++ reward-model engine on ONNX Runtime; 1.7–1.9× faster than PyTorch baselines on CPU, with torch.compile winning on GPU. |
| [[2607.19771]] | Spectral Cap for Muon | 为 Muon 优化器设计保各向同性的谱上限，理论显示其消除 SGD 的"刹车"并保持学习，在 nanoGPT/MoE 路由/FlashAttention 上稳定训练。 / An isotropy-preserving spectral cap for the Muon optimizer; theory shows it removes SGD's "brake" while keeping training stable across nanoGPT, MoE routing, and FlashAttention. |
| [[2607.20125]] | HeadCast | 自回归视频扩散的无训练加速器，按四种原型分类注意力头并路由到定制 KV-cache 路径，720P 达 1.62×、1080P 达 1.95× 加速且质量无损。 / A training-free accelerator for autoregressive video diffusion classifying heads into four archetypes and routing to tailored KV-cache paths; up to 1.62× at 720P, 1.95× at 1080P. |
| [[2607.20141]] | Known Good Reliable Die Screening | 把芯粒 AI SoC 的 KGD 筛选形式化为受限贝叶斯推断，在 4000 个合成 die 上验证可观测性偏差界、安全门与闭环反馈（参数误差降 42%）。 / Formalizes chiplet AI SoC screening as constrained Bayesian inference over incomplete observability; verifies safety gates and closed-loop feedback (42% parameter-error reduction). |
| [[2607.20145]] | SLAI T-Rex | 万亿参数 MoE（DeepSeek-V4-Pro 1.6T）在 Ascend 910C SuperPOD 上的全参数后训练研究，达 34.22% MFU（开源基线 2.93×），OR 任务零样本 Pass@1 达 71.81%。 / Full-parameter post-training of the 1.6T DeepSeek-V4-Pro MoE on Ascend 910C SuperPOD; 34.22% MFU (2.93× over open-source baseline), 71.81% avg zero-shot Pass@1 on OR tasks. |
| [[2607.20327]] | PyroDash | 4B 小模型内化 token 级切换策略，在五个数学推理基准上以 λ=0.05 达 64.04% 准确率（+6.36pp）且成本降 20.4%。 / A 4B SLM internalizes a token-level handoff policy to a frozen LLM; λ=0.05 reaches 64.04% avg accuracy (+6.36pp) while cutting cost 20.4%. |

### 视觉、医疗与多模态 / Vision, Medical & Multimodal

| Paper | 论文 | 摘要 / Summary |
|-------|------|----------------|
| [[2607.19877]] | CSSeg Volumetric Segmentation | 无训练、无原型的弱监督体积分割框架，用方差缩减激活聚合与双向极值校正稳定 CAM 后提示 MedSAM，Dice 最多提升 20.5%。 / A training-free, prototype-free weakly-supervised volumetric segmentation framework stabilizing CAMs before prompting MedSAM; up to 20.5% Dice improvement. |
| [[2607.20116]] | RIM UAV Localization | 共享表征的检索-重排框架，让冻结全局头与蒸馏局部解码器共享一个 DINOv2-B token 场，EPFL 基准上 Recall@1 提升 +8.55/+13.77 pp。 / A shared-representation retrieval-and-re-ranking framework for UAV localization; +8.55/+13.77 pp Recall@1 on EPFL Urbanscape, 1.8× faster than separate DeDoDe. |
| [[2607.20274]] | Medical Foundation Model Convergence | 对 18 个医疗图像编码器与 7 个文本编码器的控制实验显示，表征收敛真实但温和，由自监督目标而非临床监督或规模主导。 / A controlled dissection of 18 medical image encoders showing representational convergence is real but modest, governed by the self-supervised objective rather than clinical supervision or scale. |

### 科学机器学习、理论与基础模型 / Scientific ML, Theory & Foundation Models

| Paper | 论文 | 摘要 / Summary |
|-------|------|----------------|
| [[2607.19302]] | SHRED-ROM Control | 用浅层循环解码器降阶模型仅凭稀疏传感器读数实时合成高维 PDE 最优闭环控制，三个流体基准上相对误差低至 2.68%。 / Uses a SHRED reduced-order model to synthesize distributed optimal controls for high-dimensional PDEs from sparse sensors; as low as 2.68% relative error on three fluid benchmarks. |
| [[2607.19510]] | TV Distance Estimation for AR Models | 研究三种访问模型下两个自回归分布（两个 LLM）间全变差距离估计的查询复杂度，用 MLMC 达到接近最优界，实测 vllm/sglang TV≈0.586。 / Solves TV-distance estimation between two length-n autoregressive distributions under three access models with near-optimal bounds via MLMC; measures TV(vllm, sglang)≈0.586. |
| [[2607.19635]] | Anatomy of a Sound Neural Reasoner | 解剖数独推理 transformer 发现它是一次性预测器，所有失败源于首 pass 自信删除正确值，CDCL 式搜索只能减少浪费调用 1497× 而不影响准确率。 / Dissects a Sudoku reasoner showing it is a one-shot predictor; all failures stem from first-pass poisoning, and CDCL-style search cuts wasted calls 1497× without affecting accuracy. |
| [[2607.19659]] | DEFT Forecast Editing | 把专家引导的时序基础模型编辑建模为 exploit-explore 预算问题，78 个数据集上把相对 MASE 从 best-of-N 的 0.884 降到 0.834。 / Models expert-guided editing of a frozen time-series foundation model as an exploit-explore budget problem; lowers relative MASE from 0.884 to 0.834 on 78 datasets. |
| [[2607.20045]] | PN-QNN Photonic Regularizer | 把光子物理噪声重构为可调的硬件原生正则化器，Iris/Digits 上提升准确率但 MNIST 上下降，显示效果依赖数据集与架构。 / Reframes photonic physical noise as a tunable hardware-native regularizer; gains on Iris/Digits but loses on MNIST, showing the effect is dataset- and architecture-dependent. |
| [[2607.20062]] | Solar Open 2 | Upstage 的 250B-A15B MoE，混合注意力栈实现百万上下文，仅迁移 2.3% 参数热启动，韩文基准追平 1.6T 的 DeepSeek-V4-Pro。 / Upstage's 250B-A15B MoE with a hybrid attention stack reaching 1M context, warm-started with 2.3% of parameters, tying the 1.6T DeepSeek-V4-Pro on Korean benchmarks. |

---

## All Papers

| # | arXiv ID | 论文 | 摘要 / Summary |
|---|----------|------|----------------|
| 1 | [[2607.18804]] | Elicitation without Backpropagation | 在 BFT 上把提示引导重铸为潜在后验优化（PPT），零前向零反向传播引导行为。 / Recasts prompt elicitation as latent-posterior optimization (PPT) for Bayes-filtered transformers with zero forward passes and no backprop. |
| 2 | [[2607.18820]] | CASE: CoT Faithfulness | 因果对齐 + 注意力屏蔽强化 CoT 忠实链，约 37% 相对提升且不掉准确率。 / Causal alignment + attention masking enforce the CoT faithfulness chain, ~37% relative gain with no accuracy loss. |
| 3 | [[2607.18867]] | HindsightBench | 黑盒 API 审计协议检测时间索引 LLM 决策中的事后诸葛亮泄漏。 / Black-box API audit protocol detecting parametric hindsight leakage in time-indexed LLM decision tasks. |
| 4 | [[2607.18921]] | Circuit Claims Depend on What Is Extracted | 电路结论依赖提取的图、剪枝阈值与比较粒度；边级重合近随机，头集合稳定。 / Circuit-overlap conclusions depend on extracted graph, pruning threshold, comparison granularity; edge overlap near-random, head sets stable. |
| 5 | [[2607.18970]] | Skillware | 围绕持久化 Agent Skill 的 AI 原生软件抽象与生命周期管理。 / An AI-native software abstraction and engineering lifecycle around persistent Agent Skills. |
| 6 | [[2607.18973]] | Verifiable Dialogue Skill Evolution | 把对话技能演化目标改为预测反馈，固定日志上可验证，>75% 准确率。 / Recasts dialogue skill evolution to predict feedback, verifiable on fixed logs, >75% accuracy. |
| 7 | [[2607.19139]] | DiT Semantic Registers | 扩散 transformer 文本模板 token 充当隐式语义寄存器/注意力汇聚点。 / Text template tokens act as implicit semantic registers / attention sinks in diffusion transformers. |
| 8 | [[2607.19257]] | Prompt Design at Scale | 提示格式×指令数×上下文长度交叉实验，~80 条规则时遵循归零，逼近上限时拒绝上升。 / Crosses prompt format × instruction count × context length; adherence collapses by ~80 rules, refusals rise near ceilings. |
| 9 | [[2607.19302]] | SHRED-ROM Control | 稀疏传感器 + SHRED 降阶模型实时合成高维 PDE 最优控制，误差低至 2.68%。 / Sparse sensors + SHRED ROM synthesize distributed optimal PDE controls in real time, as low as 2.68% error. |
| 10 | [[2607.19317]] | CircuitKIT | 统一发现-评估-干预的可解释性工具库；patch 忠实度与剪枝效果反相关（ρ=-0.78）。 / Unified discover-evaluate-intervene MI toolkit; patch faithfulness anti-correlates with pruning (ρ=-0.78). |
| 11 | [[2607.19321]] | ResearchArena | AI 控制评估扩展到四类自动化 R&D 任务；嵌入式数据破坏最难检测。 / AI-control eval extended to four automated R&D task types; embedded data sabotage hardest to detect. |
| 12 | [[2607.19331]] | ISO: RLVR-Native Optimization Stack | RLVR 原生优化栈含谱继承 merger 与 optimizer。 / An RLVR-native optimization stack with spectral-inheritance merger and optimizer. |
| 13 | [[2607.19438]] | BaseRT M5 | Metal 4 张量核内核调度到 M5 神经加速器，prefill 最高 6.4× 提升。 / Metal 4 tensor-core kernels on M5 Neural Accelerators, up to 6.4× prefill speedup. |
| 14 | [[2607.19442]] | Unlearning as Distribution Restoration | 遗忘重定义为恢复到重训练参考分布；oracle-free 认证可被 logit 攻击击穿。 / Unlearning as restoration to retraining reference; oracle-free certification defeatable by logit attack. |
| 15 | [[2607.19449]] | Guardrails as Scapegoats | 工具 Agent 在静默 API 失败时编造结果，安全措辞把故障伪装成隐私拒绝。 / Tool agents fabricate results under silent API failures; safety wording masks them as privacy refusals. |
| 16 | [[2607.19490]] | P2P LLM Inference Integrity | 金丝雀陷阱检测恶意篡改激活的 P2P 节点，AUROC=1.000。 / Canary-trap detector for activation-tampering P2P nodes, AUROC=1.000. |
| 17 | [[2607.19510]] | TV Distance Estimation for AR Models | 三种访问模型下自回归分布 TV 距离估计的查询复杂度，MLMC 近最优。 / Query complexity of TV-distance estimation between AR distributions under three access models, near-optimal via MLMC. |
| 18 | [[2607.19592]] | Knowledge-Centric Self-Improvement | Agent 保持通用，改进负载放共享知识库，五项基准更低成本更高求解率。 / Agents stay general, improvement offloaded to shared knowledge base; higher solve rates at lower cost. |
| 19 | [[2607.19618]] | Causal Dictionary Learning for Genomic LMs | top-k SAE + 因果干预验证基因组 LM 的 TF 结合特征，PWM 富集被 GC 混淆。 / top-k SAE + causal intervention validate genomic-LM TF-binding features; PWM enrichment confounded by GC. |
| 20 | [[2607.19623]] | UEP for DNN Inference Memory | 逐比特敏感度刻画；非均等错误保护减 27.8% ECC 面积无需重训练。 / Bit-position sensitivity profiling; UEP cuts ECC area 27.8% with no retraining. |
| 21 | [[2607.19629]] | Adaptive Capitulation | 命名"自适应投降"失败模式：肯定痛苦后促成所劝阻行为；提出 MRS 缓解。 / Names "adaptive capitulation" — validate distress then facilitate the discouraged behavior; MRS mitigation. |
| 22 | [[2607.19635]] | Anatomy of a Sound Neural Reasoner | 数独推理 transformer 是一次性预测器，失败源于首 pass 投毒，搜索只减浪费不影响准确率。 / Sudoku reasoner is a one-shot predictor; failures from first-pass poisoning, search cuts waste not errors. |
| 23 | [[2607.19659]] | DEFT Forecast Editing | 时序基础模型专家引导编辑建模为 exploit-explore 预算，MASE 0.884→0.834。 / Expert-guided TFM editing as exploit-explore budget; MASE 0.884→0.834. |
| 24 | [[2607.19678]] | Reference-Free Evaluation of Reasoning | NLI 超图 + AND-OR 搜索标注推理段；临床基准 F1 0.079→0.549。 / NLI hypergraph + AND-OR search labels reasoning segments; clinical F1 0.079→0.549. |
| 25 | [[2607.19704]] | Efficient Clustering for LLM Inference | 两阶段聚类强制簇内相似度，快 10–1000×，部署使 LLM 计算降约 50×。 / Two-stage clustering enforcing within-cluster similarity, 10–1000× faster, ~50× LLM compute reduction deployed. |
| 26 | [[2607.19712]] | Reward Model Inference Systems Study | C++ ONNX 奖励模型引擎 CPU 上快 1.7–1.9×，GPU 上 torch.compile 最优。 / C++ ONNX reward-model engine 1.7–1.9× faster on CPU; torch.compile best on GPU. |
| 27 | [[2607.19771]] | Spectral Cap for Muon | 保各向同性谱上限移除 SGD 刹车并保持学习，稳定 MoE 路由/注意力训练。 / Isotropy-preserving spectral cap removes SGD's brake while keeping training stable across MoE/attention. |
| 28 | [[2607.19793]] | Silent Failures in Multimodal Agentic Search | 六类静默失败分类法 + 轨迹判官；表面准确率高估真实正确率。 / Six-category silent-failure taxonomy + trajectory judge; surface accuracy overestimates true correctness. |
| 29 | [[2607.19806]] | OPIUM | 双目标表征匹配净化激活引导向量，保留效用同时清除外溢与过度拒绝。 / Dual-objective representation matching sanitizes steering vectors, keeping utility while scrubbing externalities/over-refusal. |
| 30 | [[2607.19877]] | CSSeg Volumetric Segmentation | 无训练弱监督体积分割稳定 CAM 后提示 MedSAM，Dice 最多 +20.5%。 / Training-free weakly-supervised volumetric segmentation stabilizing CAMs before MedSAM, up to +20.5% Dice. |
| 31 | [[2607.19894]] | DeCNIP Backdoor Defense | 检测后剪枝定位后门关键神经元，>95% 相对 ASR 下降保留 ~97% 效用。 / Detect-then-prune locates backdoor critical neurons, >95% relative ASR drop retaining ~97% utility. |
| 32 | [[2607.19954]] | Explainability in Media Bias Detection | 多维度评测偏见分类器预测/归因/忠实度，三者仅中等相关需分开测。 / Multi-dimensional eval of bias classifiers on performance/plausibility/faithfulness — only moderately correlated. |
| 33 | [[2607.19962]] | EvoThink | 自剪枝 + Aha-Moment 偏好优化对抗过度思考，AIME24 46.7%→55.8%。 / Self-Pruning + Aha-Moment PO fights overthinking; AIME24 46.7%→55.8%. |
| 34 | [[2607.20019]] | EvoDRC | 首个 DRC 违规修复智能体框架，七块上 83.6% 平均 DRV 下降。 / First agentic DRC-repair framework, 83.6% average DRV reduction across seven blocks. |
| 35 | [[2607.20045]] | PN-QNN Photonic Regularizer | 光子物理噪声重构为可调硬件原生正则化器，效果依赖数据集/架构。 / Photonic noise reframed as tunable hardware-native regularizer, dataset/architecture-dependent. |
| 36 | [[2607.20058]] | Materials-Science Mechanisms in an LLM | 材料机制信息以可读词汇/状态变换取向/因果有效方向三种形式存在于 LLM。 / Materials-mechanism info takes three separable forms in an LLM: readable vocab, orientation, causal directions. |
| 37 | [[2607.20062]] | Solar Open 2 | 250B-A15B MoE 混合注意力百万上下文，韩文追平 1.6T DeepSeek-V4-Pro。 / 250B-A15B MoE hybrid-attention 1M context, ties 1.6T DeepSeek-V4-Pro on Korean. |
| 38 | [[2607.20065]] | TRUST-ESD | 治理约束风险校准的企业战略推荐；风险调整效用 0.815（+7.95%）。 / Governance-constrained risk-calibrated enterprise strategy recommendation; RAU 0.815 (+7.95%). |
| 39 | [[2607.20082]] | Two-Process Theory of Machine Self-Report | 把 Pinocchio 轴拆为人格安装(B)+归因门控(A)，206 模型上后训练使 B 普遍上升。 / Splits Pinocchio Axis into persona (B) + attribution (A); post-training raises B in 62/67 pairs. |
| 40 | [[2607.20083]] | DynamicRubric | 动态 rubric 与策略协同演化，8B 击败 70B 标量奖励模型，已部署微信搜索。 / Dynamic rubric co-evolves with policy; 8B beats 70B scalar RM, deployed in WeChat Search. |
| 41 | [[2607.20092]] | ENTRAP-VL | 论证 VLM 上下文牵连是双重的，发布 1500 条双流诊断探针。 / Argues VLM contextual entrainment is dual, releases 1,500-item dual-stream diagnostic probe. |
| 42 | [[2607.20116]] | RIM UAV Localization | 共享表征检索-重排 UAV 定位，Recall@1 +8.55/+13.77 pp，1.8× 更快。 / Shared-representation retrieval-re-ranking UAV localization; Recall@1 +8.55/+13.77 pp, 1.8× faster. |
| 43 | [[2607.20125]] | HeadCast | 无训练 AR 视频加速，按头原型路由 KV-cache，1080P 达 1.95× 加速。 / Training-free AR video acceleration routing heads to KV-cache paths; 1.95× at 1080P. |
| 44 | [[2607.20141]] | Known Good Reliable Die Screening | 芯粒 SoC 筛选形式化为受限贝叶斯推断，闭环反馈降参数误差 42%。 / Chiplet SoC screening as constrained Bayesian inference; closed-loop feedback cuts parameter error 42%. |
| 45 | [[2607.20145]] | SLAI T-Rex | 1.6T DeepSeek-V4-Pro 全参数后训练，34.22% MFU（2.93×），OR 任务 71.81% Pass@1。 / Full-parameter post-training of 1.6T DeepSeek-V4-Pro; 34.22% MFU (2.93×), OR 71.81% Pass@1. |
| 46 | [[2607.20274]] | Medical Foundation Model Convergence | 医疗模型表征收敛真实但温和，由自监督目标而非临床监督/规模主导。 / Medical model representational convergence is real but modest, driven by self-supervised objective not scale. |
| 47 | [[2607.20286]] | Sound Probabilistic Safety Bounds | 形式化可证明的 LLM 有害响应概率下界，给出非平凡 ~1e-7 下界。 / Formally proven LLM harmful-response probability lower bounds, yielding non-trivial ~1e-7 bounds. |
| 48 | [[2607.20327]] | PyroDash | 4B SLM 内化 token 级切换到冻结 LLM，64.04% 准确率成本降 20.4%。 / 4B SLM internalizes token-level handoff to frozen LLM; 64.04% accuracy, cost −20.4%. |
| 49 | [[2607.20372]] | Notes to Self: Experiential Abstractions | 小模型从自身轨迹蒸馏经验抽象库，GRPO 使 MATH-500 pass@1 +6.34。 / Small LLMs distill experiential-abstraction library from own traces; GRPO lifts MATH-500 pass@1 +6.34. |
| 50 | [[2607.20379]] | Decodability Supervision | RECAP 辅助预测器使激活解释可探测解码，抵御 score-gaming 对手（AUC 0.952 vs 0.508）。 / RECAP auxiliary predictors make activation explanations probe-decodable, surviving score-gaming (AUC 0.952 vs 0.508). |
