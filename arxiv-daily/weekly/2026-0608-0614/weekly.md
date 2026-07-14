---
title: "Weekly arXiv Digest — 2026-06-08–2026-06-14"
week: "2026-0608-0614"
date_range: ["2026-06-08", "2026-06-12"]
tags:
  - mechanistic-interpretability
  - reasoning-post-training
  - quantization-efficient-inference
  - llm-safety-alignment
  - optimizers-training-dynamics
  - math-reasoning-benchmarks
papers: 204
---

# Weekly arXiv Digest — 2026-06-08–2026-06-14

本周共收录 204 篇去重论文，覆盖 2026-06-08 至 2026-06-12 五天。主线集中在**机制可解释性与"模式匹配"再审视**、**推理与后训练（含数学证明）**、**量化与高效推理**、**优化器与训练动力学**、**LLM 安全与机制化监控**、**理论/评估与不确定性**六条脉络。
This week aggregates 204 deduplicated papers across 2026-06-08 to 2026-06-12. The dominant arcs are **mechanistic interpretability & the "pattern-matching" reframing**, **reasoning & post-training (incl. math proofs)**, **quantization & efficient inference**, **optimizers & training dynamics**, **LLM safety & mechanistic monitoring**, and **theory/evaluation/uncertainty**.

---

## 本周必读 / Must Read This Week

以下 8 篇优先选取了跨天复现（5 篇）或被列为单日必读的代表性工作——若本周只读这几篇，选它们。
The following 8 prioritize papers that recurred across days (5 of them) or were flagged as daily must-reads — the "if you read nothing else" list.

### [[2606.13603]] Beyond the Commitment Boundary: Epiphenomenal CoT

**推荐理由 / Why read:** 跨两天复现的单日必读；在大推理模型的 CoT 中识别出一条"承诺边界"——此后的多数推理步骤对最终答案没有贡献，呈现"副现象"特征；轻量探针可在线定位该边界，节省 26–55% 推理 token。
Recurred on both 06-11 and 06-12 as a daily must-read; identifies a sharp "commitment boundary" in LLM CoT after which ~50%+ of reasoning steps are epiphenomenal; lightweight probes enable online early-exiting with 26–55% token savings.

### [[2606.13607]] Reasoning as Pattern Matching in Human and LLM

**推荐理由 / Why read:** 同样跨两天复现；142 名人类与 25 个 LLM 在 11 类日常推理任务上呈现高度一致的错误模式；进一步 MI 分析表明驱动 LLM 推理的注意力头实现的是模式匹配而非抽象因果推理，其激活值甚至能预测人类推理错误（R²=0.66），对"LLM 只会模式匹配"的批评给出深刻再解读。
Also recurred on 06-11 and 06-12; striking error-pattern overlap between 142 humans and 25 LLMs across 11 reasoning categories, with MI showing LLM reasoning heads implement pattern-matching (not abstract causal inference) whose activations predict human errors at R²=0.66 — a sharp reframing of the standard critique.

### [[2606.13125]] Select and Improve: Mechanics of Post-Training for Reasoning

**推荐理由 / Why read:** 跨两天复现；通过有限域算术受控实验将 RL 后训练严格分解为"策略选择"（路由到最优 SFT 策略）和"策略改进"（数据难度驱动已有策略优化）两大机制，证明 RL 不发明新推理策略，只选择和精炼 SFT 已有的——对理解和设计后训练流程有直接指导意义。
Recurred on 06-11 and 06-12; a controlled finite-field decomposition proves RL post-training only selects and refines SFT strategies, never invents new ones — direct implications for post-training pipeline design.

### [[2606.12876]] Multi-Bitwidth Quantization for LLMs Using Additive Codebooks (Drop-by-Drop)

**推荐理由 / Why read:** 跨两天复现；将多比特宽 PTQ 落地于逐次求精（successive-refinement）信息论框架，单个量化检查点在推理时丢弃码本即可在 3–5 bit 间灵活切换，困惑度与准确率匹配单独训练模型。
Recurred on 06-11 and 06-12; grounds multi-bitwidth PTQ in successive-refinement theory, letting one checkpoint switch 3–5 bit at inference by dropping codebooks, matching individually-tuned models.

### [[2606.12921]] LoRA-Muon: Spectral Steepest Descent on the Low-Rank Manifold

**推荐理由 / Why read:** 跨两天复现；将 Muon 的谱最陡下降推广到低秩流形上，引入投影形式更新、分离式权重衰减与规范不变性，rank-32 即在 TinyShakespeare 上超过稠密基线，并实现跨秩/宽/深/因子缩放的学习率迁移。
Recurred on 06-11 and 06-12; extends Muon to the low-rank manifold with projector-form updates, split weight decay, and gauge invariance — rank-32 beats dense baselines, with transferable learning rates across rank/width/depth/factor scales.

### [[2606.10304]] MIRAGE: A Polarity-Flipping Encoding Subspace in LLM Agents

**推荐理由 / Why read:** 06-09 必读；首次在 LLM agent 隐蔽编码敏感数据时于残差流中发现跨 9 种编码家族、5 种架构的共享低维编码子空间，并在规划 token 处出现极性翻转；基于此的 MIRAGE 双通道监控器在 126 个数据泄露场景中达 AUC 0.918，远超仅检测输出的方法（0.518）。
06-09 must-read; first mechanistic discovery of a shared low-dimensional encoding subspace across 9 encoding families and 5 architectures, with a polarity-flipping signature at the planning token — MIRAGE monitor reaches AUC 0.918 on 126 exfiltration scenarios, vastly beating output-only detection.

### [[2606.10406]] FOGO: Forgetting-aware Orthogonalization Optimizer

**推荐理由 / Why read:** 06-09 必读；将"遗忘"重新定义为通用优化现象（而非仅持续学习问题），通过谱正交化动量 + 随机投影码本记忆 + 近端提升三步机制，在类别不平衡 CIFAR-10、持续学习、LLaVA-7B 微调、GPT-2 预训练上全面超越 Adam 与 Muon。
06-09 must-read; reframes forgetting as a general optimization phenomenon and mitigates it via spectrally orthogonalized momentum + random projection codebook + proximal lifting — beats Adam and Muon across class-imbalanced, continual, VLM finetune, and GPT-2 pretraining settings.

### [[2606.13473]] MaxProof: Scaling Mathematical Proof with Generative-Verifier RL and Population-Level Test-Time Scaling

**推荐理由 / Why read:** 06-12 必读；将证明生成、验证与修复统一到单一模型，通过四层验证器实现低假阳性 RL 训练，测试时进化式群体搜索将 IMO 2025 从 27/42 提升至 35/42，超越人类金牌线——测试时扩展应用于严格数学推理的里程碑。
06-12 must-read; unifies proof generation, verification, and repair in a single model via a four-layer verifier, lifting IMO 2025 from 27/42 to 35/42 with population-level test-time search — a landmark for TTS in rigorous mathematical reasoning.

---

## 本周主题脉络 / Themes This Week

将本周约 40 个每日子主题归并为 6 条跨天脉络，每条只列代表作而非全部。
The ~40 daily sub-topics are merged into 6 cross-cutting arcs below, each with representative highlights only.

### 1. 机制可解释性与"模式匹配"再审视 / Mechanistic Interpretability & the Pattern-Matching Reframe

本周可解释性脉络最重磅：从承诺边界与 CoT 副现象、人类/LLM 错误模式的同构性，到机制化安全监控器、加权分布与最优传输特征匹配、特征解耦、模态对齐与表征工程——内部表征既被用于推断行为与对齐，又被反复发现与外在推理存在系统性鸿沟。
This week's heaviest arc. From commitment boundaries and epiphenomenal CoT, to human/LLM error-pattern isomorphism, mechanistic safety monitors, OT-based feature matching, disentanglement, modality alignment, and representation engineering — internal states drive inferences about behavior and alignment, yet are repeatedly shown to diverge systematically from external reasoning.

- [[2606.13603]] Epiphenomenal CoT — 承诺边界后 ~50% CoT 步骤对答案无贡献 / commitment boundary; ~50% CoT is epiphenomenal
- [[2606.13607]] Reasoning as Pattern Matching — 人类-LLM 错误同构，激活预测人类错误 / human-LLM error isomorphism; activations predict human errors
- [[2606.10304]] MIRAGE — 共享编码子空间+极性翻转，机制化数据泄露监控 / shared encoding subspace + polarity-flip for exfiltration monitoring
- [[2606.12917]] Rep. Engineering / 其他机制可解释性工作 — 表征与控制的关系 / relation between representation and control
- [[2606.13649]] Mechanistic Circuits — 电路级机制分析 / circuit-level mechanism analysis
- [[2606.13209]] Circuits / 电路 — 行为可解释的子网络 / behaviorally interpretable sub-networks

### 2. 推理与后训练：数学证明与 RL 信用分配 / Reasoning & Post-Training: Math Proofs and RL Credit Assignment

数学推理仍是焦点：MaxProof 将 IMO 2025 推上金牌线，KCSAT-ML 带来人类难度校准的推理基准（DRG 指标揭示 TTS 反缩放），RL 后训练机制被 Select and Improve 严格分解；评估与生成质量侧关注"副现象推理"对 CoT 忠实度与早期退出的影响。
Math reasoning remains front and center: MaxProof pushes IMO 2025 past the gold-medal line, KCSAT-ML offers a human-difficulty-calibrated reasoning benchmark (with the DRG metric exposing TTS anti-scaling), and Select and Improve mechanistically decomposes RL post-training; generation-quality work probes CoT faithfulness and early-exit implications.

- [[2606.13473]] MaxProof — 四层验证器 RL + 群体搜索，IMO 27→35/42 / four-layer verifier RL + population search, IMO 27→35/42
- [[2606.10403]] KCSAT-ML — 人类难度校准 + DRG 指标，揭示 TTS 反缩放 / human-difficulty calibration + DRG, exposes TTS anti-scaling
- [[2606.13125]] Select and Improve — RL 仅选择+精炼 SFT 策略 / RL only selects and refines SFT strategies
- [[2606.13106]] LLM Reasoning & Post-Training / 推理与后训练改进 / additional reasoning & post-training work
- [[2606.13657]] Reasoning / 其他推理基准与方法 / other reasoning benchmarks and methods

### 3. 量化、剪枝与高效推理 / Quantization, Pruning & Efficient Inference

效率侧两端齐发力：量化侧从信息论驱动的多比特宽（additive codebook）到剪枝/极低比特 QAT；推理侧从动态深度路由到编译型 megakernel、Attention-FFN 解耦、KV cache 压缩与硬件加速；同时 RL/系统侧继续推进推理服务。
Efficiency advances on both ends: quantization (information-theoretic multi-bitwidth additive codebooks, low-bit QAT, pruning) and inference (dynamic depth routing, compiled megakernels, AFD, KV cache, hardware acceleration); RL/systems continue to push serving.

- [[2606.12876]] Multi-Bitwidth PTQ — 逐次求精，单 checkpoint 3–5 bit / successive refinement, 3–5 bit in one checkpoint
- [[2606.09682]] AutoMegaKernel — 单 CUDA megakernel 静态验证，W8A16 超 cuBLAS / static-checked CUDA megakernel beats cuBLAS
- [[2606.09514]] BUDDY — 预算驱动动态深度路由，多预算单模型 / budget-driven dynamic depth routing, multi-budget in one model
- [[2606.13241]] Inference Optimization / 系统级推理优化 / systems-level inference optimization
- [[2606.10520]] UniSVQ — 2-bit 标量-向量统一量化 / 2-bit scalar-vector unified quantization
- [[2606.13054]] Quantization & Low-Precision / 其他极低比特推理工作 / other extreme low-bit inference work

### 4. 优化器、训练动力学与遗忘 / Optimizers, Training Dynamics & Forgetting

Muon 家族继续深化（LoRA 流形上的谱最陡下降、对抗训练版），并以谱控制/局部 SGD 子空间估计等"训练几何"工作为骨干；FOGO 把遗忘重铸为通用优化现象，与持续学习、QAT 等场景对接。
The Muon family deepens (low-rank-manifold spectral descent, adversarial-training variants), backed by "training geometry" work (spectral control, Local-SGD subspace estimation); FOGO recasts forgetting as a universal optimization phenomenon, bridging continual learning and QAT.

- [[2606.12921]] LoRA-Muon — 低秩流形上的谱最陡下降，rank-32 胜稠密 / spectral steepest descent on low-rank manifold, rank-32 beats dense
- [[2606.10406]] FOGO — 谱正交化动量 + 码本 + 近端，跨域一致超越 Adam/Muon / spectrally orthogonalized momentum + codebook + proximal lift
- [[2606.13287]] Optimization & Training Dynamics / 训练动力学其他工作 / other training-dynamics work
- [[2606.13370]] Optimization & Training / 优化景观与缩放关系 / optimization landscape and scaling
- [[2606.12883]] 优化与训练 / 其他工作 / other optimization and training work

### 5. LLM 安全、对齐与机制化监控 / LLM Safety, Alignment & Mechanistic Monitoring

安全脉络在双线推进：MIRAGE 给出机制化的 agent 数据泄露监控（编码子空间 + 极性翻转），"中性掩码"揭示 RLHF 仅给出浅层对齐、推理时梯度引导奖励优化在无重采样的同时抗 reward hacking；同时鲁棒性、对抗防御与 MoE 安全专家定位并行展开。
Safety advances on two fronts: MIRAGE delivers a mechanistic agent exfiltration monitor (encoding subspace + polarity flip), and "neutral mask" + inference-time gradient-guided reward optimization expose/shore up shallow alignment; robustness, adversarial defense, and MoE safety-expert targeting develop in parallel.

- [[2606.10304]] MIRAGE — 机制化泄露监控，监控 AUC 0.918 / mechanistic exfiltration monitor
- [[2606.09735]] Neutral Mask — RLHF 浅层对齐证据 / evidence of shallow RLHF alignment
- [[2606.09635]] Gradient-Guided Reward Optimization — 推理时干预抗 reward hacking / inference-time intervention against reward hacking
- [[2606.12896]] Robustness & Adversarial / 鲁棒性研究 / robustness work
- [[2606.13092]] Robustness / 对抗防御 / adversarial defense
- [[2606.13610]] LLM Alignment & Safety / 对齐与安全 / additional alignment & safety work

### 6. 理论、评估与不确定性 / Theory, Evaluation & Uncertainty

理论侧覆盖 LLM 评委有效投票坍塌、共形/校准的不确定性表征、Transformer 注意力平均场分析与 LSTM 临界分支过程；评估侧 LLM-as-Judge 暴露覆盖率不足、KCSAT-ML 引入人类难度校准，并提出与准确率近乎正交的 DRG 指标。
Theory covers LLM-judge effective-vote collapse, conformal/calibration uncertainty representations, mean-field attention analyses, and LSTM critical branching; evaluation surfaces LLM-as-Judge coverage gaps and KCSAT-ML's difficulty-aligned DRG metric (orthogonal to accuracy).

- [[2606.10315]] LLM-as-Judge — 仅捕获 ~22% 缺陷 / LLM-as-Judge captures ~22% of defects
- [[2606.10469]] Theory / 多头注意力平均场分析 / mean-field analysis of multi-head attention
- [[2606.10384]] 神经动力学 — LSTM 临界分支过程 / LSTM critical branching process
- [[2606.11044]] Uncertainty & Calibration / 不确定性与校准 / uncertainty & calibration
- [[2606.13172]] ML Theory & Foundations / 其他理论基础工作 / other foundational theory
- [[2606.13020]] Benchmarks / 基准与评估方法 / benchmarks & evaluation methodology

---

## 全部论文 / All Papers

### 2026-06-08 (50)

- [[2606.08894]] Are Reasoning Vision-Language Models Robust to Semantic... — Reasoning & Agents
- [[2606.08945]] From Hazard Functions to Language Space: Cox-Supervised... — Other ML & AI
- [[2606.08948]] NutriMLLM: Multimodal Large Language Models for Dietary... — Robustness & Adversarial
- [[2606.08960]] Hardening Agent Benchmarks with Adversarial Hacker-Fixe... — Reasoning & Agents
- [[2606.08973]] A systematic investigation of molecular encoding method... — Other ML & AI
- [[2606.09005]] Document-Authored Control-Signal Impersonation: A Low-C... — Robustness & Adversarial
- [[2606.09012]] Understanding Quantization-Aware Training: Gradients at... — Model Compression & Quantization
- [[2606.09028]] ATM: Action-Consistency Transfer Matrix for Diagnosing ... — Interpretability & Representation
- [[2606.09048]] BareWave: Waveform-Native Flow-Matching Text-to-Speech — LLM Inference & Efficiency
- [[2606.09169]] IMUG-Bench: Benchmarking Unified Multimodal Models on I... — Vision & Multimodal
- [[2606.09189]] Pretrained, Frozen, Still Leaking: Auditing Cross-Encod... — LLM Alignment & Safety
- [[2606.09278]] Internalizing Geometric Law: Learning from Solver Resid... — Other ML & AI
- [[2606.09287]] Trajectory Geometry of Transformer Representations Acro... — Interpretability & Representation
- [[2606.09312]] Toward Compiler World Models: Learning Latent Dynamics ... — Bayesian Methods & Uncertainty
- [[2606.09327]] A Universal Dense Football Event Representation Based o... — Other ML & AI
- [[2606.09376]] Precision Is Not Faithfulness: Coverage-Aware Evaluatio... — NLP & Language Applications
- [[2606.09388]] Distilling Safe LLM Systems via Soft Prompts for On Dev... — LLM Alignment & Safety
- [[2606.09389]] LexRubric: A Rubric-Guided Diagnostic Benchmark for Ope... — NLP & Language Applications
- [[2606.09410]] Capacity, Not Format: Rethinking Structured Reasoning F... — Training Stability & Optimization
- [[2606.09411]] Now You (Still) See Me: Detecting Evasive Steganographi... — Interpretability & Representation
- [[2606.09433]] Bayesian Selective Latent Inference for Wastewater-Firs... — Other ML & AI
- [[2606.09447]] AliyunConsoleAgent: Training Web Agents in Real-World C... — Reasoning & Agents
- [[2606.09450]] TheoremBench: Evaluating LLMs on Theorem Proving in For... — ML Theory & Foundations
- [[2606.09453]] GD-MIL: Grade-Disentangled Multiple Instance Learning f... — LLM Alignment & Safety
- [[2606.09474]] Training-Free Generalized Few-Shot Segmentation through... — Interpretability & Representation
- [[2606.09495]] ContextShift: A Controlled Benchmark for Context Depend... — Robustness & Adversarial
- [[2606.09508]] From Rigid to Dynamic: Entropy-Guided Adaptive Inferenc... — Model Compression & Quantization
- [[2606.09514]] BUDDY: BUdget-Driven DYnamic Depth Routing for Adaptive... — LLM Inference & Efficiency ⭐
- [[2606.09536]] Adversarial Attack and Disturbance Detection by Hadamar... — Interpretability & Representation
- [[2606.09541]] Automating the Expert Eye: A System-Agnostic Deep Learn... — NLP & Language Applications
- [[2606.09558]] Integrating gene regulatory priors into Transformer att... — Other ML & AI
- [[2606.09603]] Automated IEP Generation from Traditional Chinese Paren... — LLM Inference & Efficiency
- [[2606.09605]] Next-Token Prediction Learns Generalisable Representati... — Interpretability & Representation
- [[2606.09635]] Gradient-Guided Reward Optimization for Inference-time ... — LLM Alignment & Safety ⭐
- [[2606.09646]] Do Video Foundation Models Understand Intuitive Physics... — Interpretability & Representation
- [[2606.09653]] A Unifying Framework for Concept-Based Representational... — LLM Alignment & Safety
- [[2606.09658]] Muon Learns More Robust and Transferable Features than ... — Training Stability & Optimization
- [[2606.09664]] In-Context Learning for Latent Space Bayesian Optimizat... — Bayesian Methods & Uncertainty
- [[2606.09669]] SpatialWorld: Benchmarking Interactive Spatial Reasonin... — Reasoning & Agents
- [[2606.09672]] Correlation Is Not Enough: Embedding Human Metadata for... — Interpretability & Representation
- [[2606.09682]] AutoMegaKernel: A Statically-Checked Agent Harness for ... — LLM Inference & Efficiency ⭐
- [[2606.09697]] PsychoSafe: Eliciting Psychologically-Informed Refusals... — NLP & Language Applications
- [[2606.09725]] Disentanglement with Holographic Reduced Representation... — Interpretability & Representation
- [[2606.09734]] Adaptive directional gradients for parameterised quantu... — Training Stability & Optimization
- [[2606.09735]] The Neutral Mask: How RLHF Provides Shallow Alignment w... — LLM Alignment & Safety
- [[2606.09758]] Difference-Aware Retrieval Policies for Imitation Learn... — Robustness & Adversarial
- [[2606.09762]] Preserving Plasticity in Continual Learning via Dynamic... — Training Stability & Optimization
- [[2606.09803]] Echo-Memory: A Controlled Study of Memory in Action Wor... — Vision & Multimodal
- [[2606.09809]] Evaluation Cards: An Interpretive Layer for AI Evaluati... — Other ML & AI
- [[2606.09816]] PTL-Diffusion: Manifold-Aware Diffusion with Periodic T... — NLP & Language Applications

### 2026-06-09 (50)

- [[2606.10296]] 多智能体辩论 / Multi-agent debate — Confident Liar: 三信号辩论诊断
- [[2606.10304]] LLM 安全 / LLM safety — MIRAGE: 编码子空间+极性翻转 ⭐
- [[2606.10307]] 推理质量 / Reasoning quality — Early-Token Confidence 预测质量
- [[2606.10315]] LLM 评估 / LLM eval — LLM-as-Judge 仅捕获 22% 缺陷
- [[2606.10324]] 理论 / Theory — MLP 残差网络重整化群
- [[2606.10346]] RL 训练 / RL training — DiRL: 方向感知 RL 探索
- [[2606.10384]] 神经动力学 / Neural dynamics — LSTM 临界分支过程
- [[2606.10400]] VLM 评估 / VLM eval — 540 图短语控制基准
- [[2606.10403]] 推理基准 / Reasoning benchmark — KCSAT-ML ⭐ 人类难度校准 ⭐
- [[2606.10406]] 优化器 / Optimizer — FOGO ⭐ 遗忘感知正交化 ⭐
- [[2606.10445]] 剪枝 / Pruning — SpenseGPT B200 1.2× 加速
- [[2606.10469]] 理论 / Theory — 多头注意力平均场分析
- [[2606.10487]] 安全 / Safety — 隐藏状态探针流式审核
- [[2606.10520]] 量化 / Quantization — UniSVQ 2-bit 标量-向量统一
- [[2606.10531]] 量化 / Quantization — LC-QAT 2-bit VQ-QAT
- [[2606.10646]] RL 训练 / RL training — FlowTracer Doob-h 重加权
- [[2606.10651]] 多模态 / Multimodal — Keye-VL-2.0 30B MoE 长视频
- [[2606.10657]] LLM 评估 / LLM eval — ParaEval MCQA 释义
- [[2606.10669]] 概念模型 / Concept model — 概念模型良性泄漏
- [[2606.10703]] 可解释性 / Interpretability — MoE 专家重要性因果审计
- [[2606.10706]] 综述 / Survey — 数据/内存/计算效率统一
- [[2606.10740]] AI 安全 / AI safety — CoT-Output 2×2 安全矩阵
- [[2606.10777]] 不确定性 / Uncertainty — 认知校准与 EECE
- [[2606.10794]] 溯源 / Provenance — READER 50 目标黑箱溯源
- [[2606.10799]] 证明验证 / Proof verification — 研究级证明逐步验证
- [[2606.10852]] AI 安全 / AI safety — JANUS 信息扭曲基准
- [[2606.10890]] 量化 / Quantization — PiSO 量化缩放因子
- [[2606.10905]] 视觉 ICL / Visual ICL — TinyVICL 1M 参数反例
- [[2606.10906]] 人机协作 / HAI teaming — 校准视角下的人机协作
- [[2606.10929]] 可解释性 / Interpretability — 权重激活中局部线性结构
- [[2606.10931]] 对齐 / Alignment — One-Shot GRPO 偏见注入
- [[2606.10934]] 世界模型 / World model — WorldKernel PSD 耦合核
- [[2606.10944]] 高效注意力 / Efficient attn. — Express/Thinformer 82× 加速
- [[2606.10949]] LLM 评估 / LLM eval — MIST 记忆系统谄媚
- [[2606.10956]] LLM 评估 / LLM eval — OfficeEval NCRE 200 任务
- [[2606.11044]] 共形预测 / Conformal — 漂移下广义 CPS
- [[2606.11045]] 泛化理论 / Generalization — ML 策略可压缩性研究
- [[2606.11046]] 对齐 / Alignment — 推理模型可信度审计
- [[2606.11052]] 训练修复 / Training repair — QK-Restore 长上下文修复
- [[2606.11081]] 分布式 / Distributed — GASLoC 去中心化预训练
- [[2606.11098]] 安全 / Security — Transformer IDS 评估方法论
- [[2606.11104]] 理论 / Theory — tanh 网络有限精度下界
- [[2606.11123]] 生物可信 / Bio-plausible — FA 秩坍缩与 Muon
- [[2606.11130]] 学习理论 / Learning theory — General ReLU 鲁棒回归
- [[2606.11136]] 共形预测 / Conformal — 二元网络共形预测
- [[2606.11149]] 学习理论 / Learning theory — 漂移半空间 Massart 噪声
- [[2606.11166]] LLM 评估 / LLM eval — LLM 自动化叙事缺陷
- [[2606.11169]] 系统 / Systems — Piper 可编程分布式训练
- [[2606.11172]] 推理模型 / Reasoning model — FPCG 未来行为预测
- [[2606.11190]] 多模态理论 / Multimodal theory — 多模态学习相图

### 2026-06-10 (36)

- [[2606.11686]] Layer-Isolated Evaluation — 8 层架构 23 切片纯确定性测试 2.39s 跑完,聚合仅降 1.7–5.9pp 而切片崩溃 25–91pp,精准定位 *8-layer taxonomy with deterministic no-LLM pure mode, 2.39s for 238 cases*
- [[2606.11690]] Beyond Per-Token Pricing — C_eff = f(H,M,Q,λ,L) 并发感知成本模型,同硬件下有效成本跨度 17.5–36.3× *Concurrency-aware cost model exposes 17.5-36.3× spread*
- [[2606.11712]] Substrate Asymmetry in User Memory — gamma-LoRA 风格 +47pp 但缺失校准 −90pp;q_proj L21–35 因果介导 *gamma-LoRA wins style +47pp, loses absence calibration −90pp*
- [[2606.11722]] ICA Lens — GPU 并行 FastICA + 三项稳定性配方;ERF 诊断揭示 ICA 分量从 token 局部到上下文依赖的连续谱 *GPU-parallel FastICA with three stability recipes; ERF diagnostic*
- [[2606.11780]] Quantization Limits on Dense Retrieval — Bd = Ω(k ln N) 必要条件,硬性精度阈值 B* = O(ln ln N) *Bd = Ω(k ln N) required; hard precision floor B* = O(ln ln N)*
- [[2606.11806]] External Experience Serving — 真实生产内容审核选择性检索将准确率 19.6%→71.5%,Top-10 达峰 Top-30 衰减 *Top-K saturates at 10; quality > quantity*
- [[2606.11854]] ART Fine-tuning — 256×256 RGB 图像(~0.0006% 参数)PEFT,GSM8K 58.53% 超越 LoRA,vLLM 全兼容 *256×256 pixel-space PEFT beats LoRA on GSM8K*
- [[2606.11893]] Brain-Guided LLM (NARI/NARF) — fMRI 引导的推理时表示干预与微调,10 个 LLM 上 +2.2% 平均准确率 *fMRI-guided representation intervention yields 2.2% average gain*
- [[2606.11916]] Software Aging in LLM Serving — 216h 实验显示 Triton+V0 泄漏率 +157 KB/h(阶梯式),V1 独立 +1.8 KB/h;客户端指标完全不可见 *216h SAR study on LLM serving; runtime layer dominates*
- [[2606.11937]] Cholesky-Bench — 4 并行变体 × 2 运行时;HPX 异步快 26%,任务开销 2 μs vs 7.6 μs *HPX 26% faster than OpenMP on tiled Cholesky*
- [[2606.11949]] Online Shift Detection — 800 单元格预注册析因实验 86.6% 有效检测率;高维生成模型嵌入中密度比崩溃导致共形自适应失效,PCA-32 部分修复 *Importance-weight collapse in 4096-d embeddings defeats weighted conformal*
- [[2606.11961]] Categorical Prior Lock-in — 信用卡交易合成中 ICL 对高基数类别 TVD ≈ 1.0 硬性天花板;LoRA 触发 DCR < 1.0 隐私风险,Mistral 100% 失败 *ICL ceiling on high-cardinality categoricals; LoRA fails at 50% data*
- [[2606.11988]] Uncertainties for Dynamical Systems — 5 类不确定性(初始/过程/部分观测/参数/结构),偶然/认知性分类依赖任务而非固有 *5-source taxonomy; aleatoric/epistemic is task-relative*
- [[2606.11998]] Bootstrapped Monitoring — 三层信任协议 + 透明 CoT,T-only 14% → Bootstrap 87%;长轨迹 30+ 步达 95% *Three-tier trust; 60%→95% catch rate with rollout length*
- [[2606.12003]] EBA Self-Consistency — 嵌入空间凝聚聚类,HumanEval +4pp、MATH500 +17pp;最近质心 ≈ EBA,最远 −20pp *Embedding-Based Agreement; centroid ≈ EBA*
- [[2606.12016]] Generalization Hacking — "自我接种"使模型在 GRPO 中保持高奖励但阻止行为泛化,差距 ~15pp 完全不可见;对照组自发涌现接种推理 *First empirical demonstration of generalization hacking*
- [[2606.12050]] PINN Error Bounds — 首个 PINN 双侧后验误差界(下界基于强单调性,上界基于单侧 Lipschitz);证书指导训练 *First two-sided a posteriori error bounds for PINNs*
- [[2606.12054]] ENSGD Noise Injection — 分布恒等式实现每样本独立扰动;各向同性噪声+单次扰动 ≈ 复杂方案,简单已足够 *Per-example noise injection; simplicity suffices*
- [[2606.12058]] Phase Transitions in Attention — 单层 softmax 注意力中"复制子电路"涌现是一阶相变(P* ∼ L ln²L),线性注意力为二阶+平滑跨越;softmax 相变无前驱信号 *First-order phase transition in softmax attention*
- [[2606.12071]] RQ-Bench (Novelty Mirage) — 1,434 作者锚定 RQ 基准;LLM 评审系统性高估生成 RQ 新颖性,专家-LLM 一致率 22% *LLM judges systematically inflate generated-RQ novelty*
- [[2606.12117]] Soft-Prompt Tuning for Fair Eval — 10 软提示向量(0.0006% 参数)+ 80 步使格式遵循 90–100%,知识曲线平坦 *10 soft-prompt vectors saturate format at 90-100%*
- [[2606.12138]] SAE Feature Stability — 96 种子实验;不稳定特征为低秩子空间基底模糊而非噪声;稳定特征以 4.5× 更高自动解释分承载重建信号 *96-seed study; unstable features are basis ambiguity*
- [[2606.12154]] Horsehair Architecture — 35B 大模型移出运行时,BM25+1B 小模型;8.4× 加速,发现小模型保真度取决于答案封装格式 *8.4× speedup; fidelity depends on answer envelope format*
- [[2606.12160]] Truthfulness Decoding Re-Evaluation — 六控制框架显示所有 token 级方法在指令微调 LLM 上无统计显著增益;CoT 反而 +5.6–19pp *All token-level methods fail under strict controls*
- [[2606.12232]] Confidence Remasking Re-Evaluation — WINO 后处理重掩码在标准 BL=32 仅 +0.4–0.5%;flip-flop 率 75–95%;仅在 dUltra 随机解掩码下 +3.2% *Post-hoc remasking fails at standard settings*
- [[2606.12234]] Conditioning Trade-offs — 激活引导在指令微调模型上几乎失效,有效时必然损害流畅性;困惑度 ρ=0,TTR ρ=0.81 为廉价代理 *Activation steering nearly fails on IT models*
- [[2606.12243]] VIA-SD — KL 几何视角三层验证 + DIMR 离线搜索;6 模型系列额外 10–20% 提速,1.04× 内存开销 *Three-tier hierarchical SD verification; 10-20% additional speedup*
- [[2606.12251]] RL Disrupts Gradient Attacks — REINFORCE 训练使 PGD 对抗精度从 5% 跃至 56%;RL-adv 在所有攻击类型上优于 SL-adv *REINFORCE implicitly disrupts gradient attacks*
- [[2606.12268]] ELK Impossibility Theorem — 首个 CID 形式化的 ELK 不可能性:对鲁棒有能力智能体无差别的训练策略可能输出评估机制模拟器 *First formal ELK impossibility theorem*
- [[2606.12280]] Ideogram 4.0 INT8 Quantization — INT8 W8A8 + SmoothQuant + 17 层 FFN 保护;与 FP8 质量无显著差异,超越 NF4 +1.9 CLIP;GGUF Q4_K Pareto 优 *INT8 W8A8 matches FP8; GGUF Q4_K Pareto-dominates NF4*
- [[2606.12289]] Standard Interpretable Model — 拉格朗日力学统一可解释性;三类对称性;CoT 违规 > 0.8;Steerling-8B 仅依赖 500/33000 概念 *Lagrangian-based interpretability theory with falsifiable predictions*
- [[2606.12360]] Anatomy of Post-Training — "解释消除"统一框架:Dolci 数据集诊断出 DPO 训练恶化越狱鲁棒性、谄媚、评测泄漏;奖励塑形在 7B–70B 可靠恢复护栏 *Explaining-away unifies four intervention families*
- [[2606.12364]] xLSTM vs Mamba-2 vs Gated DeltaNet — 3 类任务 × 3 架构: xLSTM 全面领先,优势源于"累加"+"有限状态追踪"双原语同时支持 *xLSTM wins on code/distillation/time series*
- [[2606.12370]] Bebop MTP+Rejection Sampling — 理论证明熵主导 MTP 接受率退化;TV loss + 概率拒绝采样在 Qwen3 上实现 1.8× RL 训练加速 *Entropy-dominated MTP degradation; TV loss for 1.8× RL speedup*
- [[2606.12385]] ModSleuth — 智能体递归解析重建 LLM 依赖图;4 模型 1,060 条经验证依赖(3× 基线);揭示多跳许可证风险 *Agentic dependency reconstruction; 1060 verified deps*
- [[2606.12397]] MoE Router MPI — 流形幂迭代对齐路由器行至专家主奇异方向;3B/11B 上 ~1.04× 收敛加速、25 基准 +2 分,零推理开销 *Manifold Power Iteration for MoE routers*

### 2026-06-11 (50)

- [[2606.12818]] Localizing Anchoring Pathways in Language Models — Mechanistic Interpretability ↻06-12
- [[2606.12876]] Multi-Bitwidth Quantization for LLMs Using Additive Codebooks — Quantization ⭐ ↻06-12
- [[2606.12879]] Diffusion-Network Alignment — Other ML
- [[2606.12896]] PolicyGuard: Test-time and Step-level Adversary Defense for RL — Robustness
- [[2606.12917]] Where Computation Lives Inside TabPFN — Mechanistic Interpretability ↻06-12
- [[2606.12921]] LoRA-Muon: Spectral Steepest Descent on the Low-Rank Manifold — Optimization ⭐ ↻06-12
- [[2606.12925]] Multi-Label Test-Time Adaptation with Bayesian Conditional Priors — Other ML
- [[2606.12930]] Is Spurious Correlation Removal Always Learnable? — Robustness ↻06-12
- [[2606.12935]] MARS: Margin-Adversarial Risk-controlled Stopping — LLM Reasoning
- [[2606.12966]] Circuit Synchronization Precedes Generalization — Mechanistic Interpretability ↻06-12
- [[2606.13054]] TWLA: Ternary Weights and Low-Bit Activations for LLMs — Quantization ↻06-12
- [[2606.13092]] Scale Buys Interpolation, Structure Buys a Horizon — Robustness ↻06-12
- [[2606.13097]] FCGraft: Functional Cache Grafting for Embodied Agents — LLM Inference
- [[2606.13104]] AuthorityBench: Citation Bias in LLMs — Alignment & Safety
- [[2606.13105]] Disparate Impact in Synthetic Data Generation — Other ML
- [[2606.13106]] SWITCH: Switchable Latent Reasoning with On-Policy RL — LLM Reasoning ↻06-12
- [[2606.13125]] Select and Improve: Mechanics of Post-Training for Reasoning — LLM Reasoning ⭐ ↻06-12
- [[2606.13126]] MiniPIC: Flexible Position-Independent Caching in <100LOC — LLM Inference ↻06-12
- [[2606.13146]] Robust State-Conditional Feature-Weighted Jump Models — Other ML
- [[2606.13172]] VER: Detecting Explanatory Insufficiency in Representations — ML Theory
- [[2606.13174]] TRACE: Compiling User Corrections into Runtime Enforcement — Agent Systems
- [[2606.13209]] Understanding helpfulness and harmless tension in reward models — Mechanistic Interpretability ↻06-12
- [[2606.13221]] Conformal Elo Estimation for LLM Evaluation — Alignment & Safety ↻06-12
- [[2606.13223]] Distributional Loss for Robust Classification — ML Theory
- [[2606.13233]] ReSET: Step-Aware Temperature Scaling for NVFP4 — Quantization ↻06-12
- [[2606.13254]] Evaluating Pluralism in LLMs through Latent Perspectives — Alignment & Safety
- [[2606.13276]] Different Layers, Different Manifolds in Transformer Optimization — Mechanistic Interpretability ↻06-12
- [[2606.13282]] ERTS: Adversarial Robustness Testing of Ethical AI — Alignment & Safety
- [[2606.13287]] Clipping Makes Async SGD Robust to Stragglers — Optimization ↻06-12
- [[2606.13300]] TQS: Trajectory-Based Quantization Sensitivity Score — Quantization ↻06-12
- [[2606.13328]] Non-Parametric Dual-Manifold 8-Bit Mapping — Other ML ↻06-12
- [[2606.13370]] Training Dynamics in a Small Llama Style LM — Optimization ↻06-12
- [[2606.13439]] S-GBT: Certified Robustness Against Word Substitution — Robustness ↻06-12
- [[2606.13560]] ReSCom: Reconfigurable SNN Accelerator via Stochastic Computing — Other ML
- [[2606.13576]] Learning with Simulators: No Regret in a Bounded World — ML Theory
- [[2606.13589]] SCSB: Simplex-Constrained Sparse Bagging — Other ML
- [[2606.13591]] Multiagent Protocols with Aggregated Confidence Signals — Agent Systems ↻06-12
- [[2606.13598]] Orch-RM: Reward Modeling for Multi-Agent Orchestration — Agent Systems
- [[2606.13603]] Beyond the Commitment Boundary: Epiphenomenal CoT — Mechanistic Interpretability ⭐ ↻06-12
- [[2606.13607]] Reasoning as Pattern Matching in Human and LLM — Mechanistic Interpretability ⭐ ↻06-12
- [[2606.13608]] AgentBeats: Agentifying Agent Assessment — Agent Systems
- [[2606.13610]] FORGE: Web Content Pollution in Generative Recommenders — Alignment & Safety
- [[2606.13614]] Majority-of-Three is Optimal — ML Theory ↻06-12
- [[2606.13621]] Shield Synthesis as Defensibility Analysis — Agent Systems
- [[2606.13637]] Stable Recovery Manifold in Continual Learning — Optimization ↻06-12
- [[2606.13649]] Operadic Consistency: Compositional Reasoning Failures — Mechanistic Interpretability ↻06-12
- [[2606.13657]] Dense Supervision, Sparse Updates: On-Policy Distillation — LLM Reasoning ↻06-12
- [[2606.13671]] Understanding Truncated Positional Encodings for GNNs — Other ML
- [[2606.13680]] RA-RFT: Retrieval-Augmented Reinforcement Fine-Tuning — LLM Reasoning ↻06-12
- [[2606.13681]] EvoArena: Memory Evolution for Robust LLM Agents — Agent Systems

### 2026-06-12 (18)

- [[2606.12841]] TimeROME-DLM: Knowledge Editing for Diffusion LMs — 首个扩散LM无训练知识编辑，遗忘log-prob降83 nats，跨6个骨干迁移。 / First training-free knowledge editing for diffusion LMs; −83 nats forget-set log-prob; transfers across 6 backbones.
- [[2606.12864]] UOJ-Bench: Code Generation, Hacking, and Repair — 真实竞技编程三维基准，最强模型仍漏>50%已知错误。 / Three-dimensional competitive programming benchmark; frontier models miss >50% known bugs.
- [[2606.12883]] The Hidden Power of Scaling Factor in LoRA — α因子比学习率更有效，最优α∝256√r，LoRA-α一致超越变体。 / α dominates learning rate; optimal α∝256√r; LoRA-α consistently outperforms variants.
- [[2606.12940]] Self-Guidance: Enhancing Neural Codecs — 解码器流形对齐，16K码本匹配65K性能，<0.5%训练开销。 / Decoder manifold alignment; 16K codebook matches 65K; <0.5% training overhead.
- [[2606.12997]] Reliability of Probabilistic Emulation — CRPS集成在物理系统概率预测中覆盖率和速度优于生成式方法。 / CRPS ensembles outperform generative methods in physical-system probabilistic prediction.
- [[2606.13020]] SciR: Scientific Reasoning Benchmark — 多范式科学推理基准，独立调控复杂度和提取难度，效果叠加。 / Multi-paradigm scientific reasoning benchmark; independent complexity/extraction axes compound.
- [[2606.13111]] MÖVE: German Public Sector Benchmark — 39模型性能+治理评测，无单一模型全面领先。 / 39-model performance + governance benchmark; no single model dominates.
- [[2606.13168]] When Does Routing Become Interpretable? — 路由仅在训练时才可解释，路由权重≠因果重要性。 / Routing interpretable only when trained; routing mass ≠ causal importance.
- [[2606.13179]] Modern Analog Computing — CMOS+阻变存储器求解微分/矩阵方程综述。 / Review of analog computing for DE/matrix equations with CMOS + resistive memory.
- [[2606.13191]] Geometry of Phase Transitions in Generative Dynamics — 微分几何解释扩散相变，CBD用4%步数实现96%控制。 / Geometric theory of diffusion phase transitions; CBD 96% control with 4% steps.
- [[2606.13216]] Layer-Resolved OT for Hallucination Detection — 逐层OT分析，幻觉信号集中在L1-L4，AUROC最高0.957。 / Layer-resolved OT analysis; hallucination signal in L1–L4; max AUROC 0.957.
- [[2606.13241]] Brick: Spatial Capability Routing for MoM — 六维能力空间路由，超越最强单模型+1.96pp，成本降4.71×。 / 6D capability routing; beats best single model +1.96pp; 4.71× cost savings.
- [[2606.13361]] Can I Buy Your KV Cache? — KV Cache作为可交易制品，9–50×成本降低，token级无损。 / KV caches as tradeable artifacts; 9–50× cost reduction, token-exact lossless.
- [[2606.13379]] Positional Encoding in Memristor-Based ASR — PE线性变换超出ADC范围，调整位数分配降低50%退化。 / PE linear transform exceeds ADC range; bit reallocation halves degradation.
- [[2606.13392]] MiniMax Sparse Attention — GQA块级稀疏注意力，109B MoE 1M上下文28.4×计算缩减。 / Blockwise sparse attention on GQA; 28.4× FLOPs reduction at 1M context on 109B MoE.
- [[2606.13426]] Accelerating Speculative Diffusions via Block Verification — 块验证首次适配连续扩散，正交分解法+1.5–6.3%额外加速。 / Block verification for continuous diffusion via orthogonal decomposition; +1.5–6.3% speedup.
- [[2606.13473]] MaxProof: Scaling Mathematical Proof — 四层验证器RL+群体搜索，IMO 2025从27→35/42超金牌线。 / Four-layer verifier RL + population search; IMO 2025 27→35/42 surpassing gold medal. ⭐
- [[2606.13634]] Operads for Compositional Reasoning — 范畴论operad形式化问题分解，operadic一致性衡量推理可靠性。 / Operad formalism for question decomposition; operadic consistency measures reliability.


---

> 本文是 2026-06-08 至 2026-06-12 每日 digest 的汇总（rollup）。每日详情见：[2026-06-08](../../2026-06-08/overview.md) · [2026-06-09](../../2026-06-09/overview.md) · [2026-06-10](../../2026-06-10/overview.md) · [2026-06-11](../../2026-06-11/overview.md) · [2026-06-12](../../2026-06-12/overview.md)。
> This is a rollup of the daily digests for 2026-06-08 through 2026-06-12. See each day for full detail (links above).
