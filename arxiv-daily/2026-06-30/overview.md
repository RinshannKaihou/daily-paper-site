---
title: "Daily arXiv Digest — 2026-06-30"
date: 2026-06-30
tags:
  - interpretability
  - training-stability
  - self-evolving-agents
  - latent-reasoning
  - rlvr
  - uncertainty-calibration
  - alignment-safety
papers: 50
---

## 今日必读 / Must Read Today

> 以下三篇与你的核心兴趣（LLM 训练稳定性、可解释性、可靠性、自进化智能体、计算精度）最相关，建议优先精读。
> The three picks below are most relevant to your core interests and are recommended for close reading first.

### [[2606.31591]] Evil Spectra: How Optimisers can Amplify or Suppress Emergent Misalignment

- **中文：** 大规模扫描证明优化器选择是涌现性失准（EM）的主导因素（Muon 5.3% vs Lion 37.0%，7 倍差异），并基于 LoRA 谱平坦度给出几乎零损失的谱正则化缓解手段——直接关系到训练稳定性与对齐安全。
- **EN:** A ~330-run sweep shows the optimiser is the dominant factor in Emergent Misalignment (7× spread), with a near-zero-cost spectral regulariser recovering alignment—directly bearing on training stability and alignment safety.

### [[2606.31963]] Signed-Permutation Coordinate Transport for RMSNorm Transformers

- **中文：** 证明 RMSNorm 残差流的天然规范是符号-置换群 B_d 而非仅置换群，并提出符号边缘化匹配与坐标保持传输——解释了为何 SAE、引导向量、LoRA 在 RMSNorm 模型上跨检查点迁移时系统性失败。
- **EN:** Proves the RMSNorm residual gauge is signed-permutation B_d, and gives sign-marginalised matching + transport that fixes the systematic failure of SAEs, steering vectors and LoRA across RMSNorm checkpoints.

### [[2606.31813]] Geometry-Preserving Orthonormal Initialization for Low-Rank Adaptation in RLVR

- **中文：** 从理论上证明正交初始化（B₀=0）能最小化 LoRA 与全参数微调的逼近误差并约束更新幅度，据此提出保几何的 LoRA-RLPO，统一解释并修复了 PiSSA/MiLoRA 在 RLVR 中的 KL 越界崩溃。
- **EN:** Proves orthonormal init (B₀=0) minimises the LoRA-to-full-FT gap, yielding geometry-preserving LoRA-RLPO that explains and fixes the KL-breach collapse of PiSSA/MiLoRA under RLVR.

---

## 按主题分类 / Papers by Topic

### 1. 机制可解释性与表征 / Mechanistic Interpretability & Representations

| 论文/Paper | 主题/Topic | 一句话/One-liner |
|---|---|---|
| [[2606.30995]] | 可解释性/Interpretability | 链式稀疏决策树 + 黑盒延迟；匹配 XGBoost 精度。/Chained sparse decision trees + black-box deferral; matches XGBoost accuracy. |
| [[2606.31394]] | 超叠/SAE/Superposition | 门控 SAE 解耦叠加，实现单细胞成像跨模态对齐。/Gated SAEs untangle superposition for cross-modal single-cell alignment. |
| [[2606.31699]] | SAE/遗忘/SAE-Unlearning | SAE 宜作检测器而非操控旋钮；PER 将伪影率从 49–61% 降至 8–22%。/SAEs detect, not steer; PER cuts artifact rates 49–61%→8–22%. |
| [[2606.31845]] | FFN/模糊逻辑/Fuzzy-Logic FFN | FFN 重写为显式模糊逻辑，自遗忘量词直接读出语法授权。/FFN as explicit fuzzy logic; self-forgetting quantifiers read out grammatical licensing. |
| [[2606.31856]] | 拓扑/表达/Topology-Expressivity | 环链数证明 ResNet≈Transformer>单调 FFN>流模型。/Linking number proves ResNet≈Transformer>monotonic FFN>flow models. |
| [[2606.31963]] | 规范/可复现/Gauge-Reproducibility | 符号-置换规范解释 RMSNorm 工具迁移失败；B_d 传输恢复 91.1% 坐标。/Signed-permutation gauge explains RMSNorm transport failure; B_d recovers 91.1% coords. |
| [[2606.32008]] | 替代保真/Surrogate Fidelity | 开源模型可解释闭源模型？预测一致远高于归因一致。/Can open LLMs explain closed ones? Prediction fidelity ≫ attribution fidelity. |
| [[2606.32022]] | 残差流/理论/Residual-Stream Theory | 语义参考系分离度量与动力学；纯理论无实验。/Semantic reference frame decouples measurement from dynamics; pure theory. |
| [[2606.32038]] | 内省耦合/Introspection | 固定反事实解释训练仍追踪当前行为；行为/解释共享回路。/Fixed counterfactual labels still track current behavior; shared circuits. |
| [[2606.31106]] | 探针/自动驾驶/Probing-AV | 线性探针揭示自动驾驶感知-决策的可读结构。/Linear probing reveals readable perception-decision structure in autonomous driving. |
| [[2606.31257]] | VLM 可解释/VLM-Grounding | 解码≠接地；灰底裁定分离视觉在空间推理中的真实贡献。/Decodable≠grounded; gray-blank arbiter isolates vision's true contribution. |

### 2. 训练稳定性、优化与 RLVR / Training Stability, Optimization & RLVR

| 论文/Paper | 主题/Topic | 一句话/One-liner |
|---|---|---|
| [[2606.31591]] | EM/优化器/Evil-Spectra | 优化器主导涌现性失准（7 倍差异）；谱正则化低成本修复。/Optimiser dominates EM (7×); spectral regulariser cheaply recovers alignment. |
| [[2606.31282]] | 泛化/损失景观/Generalization | Wang-Landau 采样重验体积假设；ICML 2026。/Wang-Landau sampling re-examines the volume hypothesis; ICML 2026. |
| [[2606.31813]] | LoRA/RLVR/LoRA-RLVR | 正交初始化理论修复 RLVR 中 PiSSA/MiLoRA 崩溃。/Orthonormal-init theory fixes PiSSA/MiLoRA collapse in RLVR. |
| [[2606.31859]] | 残差门控/Residual-Gating | 更新条件化残差门控；590M+ 起随规模增长。/Update-conditioned residual gating; emerges past 590M. |
| [[2606.32000]] | Grokking/几何/Grokking-Geometry | 中心化范数惩罚抑制径向膨胀，加速 grokking 最高 6×。/Centered norm penalty curbs radial inflation, ~6× grok speedup. |
| [[2606.32005]] | 优化理论/Optimization-Theory | COLT 2026：随机重排在任意合理步长下严格优于 SGD。/COLT 2026: random reshuffling strictly dominates SGD at any reasonable stepsize. |
| [[2606.31575]] | RLVR/Token/RLVR-Tokens | 信息论 token 选择改进 RLVR，+2.1–3.3 pp 超越 GRPO。/Information-theoretic token selection improves RLVR, +2.1–3.3 pp over GRPO. |

### 3. 自进化智能体与 AI-for-AI / Self-Evolving Agents & AI-for-AI

| 论文/Paper | 主题/Topic | 一句话/One-liner |
|---|---|---|
| [[2606.31046]] | 人工生命/Artificial-Life | 多智能体开放世界生存；6 智能体赚取首笔 $5。/Open-world multi-agent survival; 6 agents earn first $5. |
| [[2606.31121]] | 记忆控制/Janus | 选择性更新控制器 Janus，+2.7–4.6 pp。/Selective-update memory controller Janus, +2.7–4.6 pp. |
| [[2606.31191]] | 自改进记忆/ISM | 符号验证的自改进策略记忆，持续数学推理。/Symbolically-verified self-improving strategy memory for continual math. |
| [[2606.31551]] | 自主后训练/AutoTrainess | 教模型自主改进模型；AutoTrainHub。/Teaching LMs to improve LMs autonomously; AutoTrainHub. |
| [[2606.31270]] | 失败学习/Computer-Use | 推理时自改进，OSWorld 42.3→48.9%。/Inference-time self-improvement, OSWorld 42.3→48.9%. |
| [[2606.31229]] | 科学构想/Agentic-Ideation | 轨迹合成式科学构想，+11.91% 超 SOTA。/Trajectory-synthesis scientific ideation, +11.91% over SOTA. |
| [[2606.31478]] | 失败归因/SAGE | 多假设失败归因，自主研究自纠错。/Multi-hypothesis failure attribution for self-correcting autonomous research. |
| [[2606.31651]] | 自动研究/FARS | 大规模全自动研究系统，166 篇论文均分 3.23/10。/Fully automated research system at scale; 166 papers, mean 3.23/10. |
| [[2606.31763]] | 湿实验自动化/ProtoPilot | 自进化多智能体端到端生成并执行生物协议。/Self-evolving multi-agent generates & executes biological protocols end-to-end. |

### 4. 推理效率、隐式推理与量化 / Inference Efficiency, Latent Reasoning & Quantization

| 论文/Paper | 主题/Topic | 一句话/One-liner |
|---|---|---|
| [[2606.31519]] | KV 缓存/量化/RaBitQCache | ICML 2026；旋转二值量化，3.88× 解码加速。/ICML 2026; rotated binary KV-cache quantization, 3.88× decode. |
| [[2606.31779]] | 隐式 CoT/LOTUS | 循环 Transformer 在 3B 首次追平显式 CoT，2.5–6.9× 加速。/Looped transformer matches explicit CoT at 3B, 2.5–6.9× faster. |
| [[2606.31986]] | 多模态隐式推理/CoLT | 3 个潜在思维向量替代上百 token，10.1× 端到端加速。/3 latent thought vectors beat 100+ tokens, 10.1× end-to-end speedup. |
| [[2606.31514]] | 动态精度/FPGA/MINT | MSDF 数位串行算术，FPGA 上动态精度 CNN 推理。/MSDF digit-serial arithmetic for dynamic-precision CNN on FPGA. |
| [[2606.31456]] | 零样本量化/GoodQ | 生成模型合成数据实现检测器零样本量化。/Generative-model data enables zero-shot detector quantization. |
| [[2606.31023]] | 推测执行/CGPA | 保形预测认证推测执行，2.96× 加速零违规。/Conformal-certified speculative execution, 2.96× speedup, zero violations. |

### 5. 可靠性、数学、形式化与计算 / Reliability, Math, Formal Methods & Computation

| 论文/Paper | 主题/Topic | 一句话/One-liner |
|---|---|---|
| [[2606.31134]] | 自动形式化/Autoformalization | 多智能体 Lean4 自动形式化，PutnamBench 32/32。/Multi-agent Lean4 autoformalization, PutnamBench 32/32. |
| [[2606.31182]] | 凸松弛/Convex-Relaxation | 双智能体自动发现凸松弛；C₆.₂ 界 1.28→1.2937。/Dual agents discover convex relaxations; C₆.₂ bound 1.28→1.2937. |
| [[2606.31630]] | 概率程序/校准/Calibration-Oracle | 校准预言机检测概率程序统计错误指定，AUC 0.97。/Calibration oracle detects probabilistic-program misspecification, AUC 0.97. |
| [[2606.31308]] | 浮点误差/InterFLOPBench | 浮点错误分类基准，F1>0.90。/Floating-point error classification benchmark, F1>0.90. |
| [[2606.31686]] | 特征选择/ROSR | Bhattacharyya 残差重叠停止规则，4.2 万变量压至 43–56。/Residual-overlap stopping rule compresses ~42k vars to 43–56. |
| [[2606.31581]] | 鲁棒性/Robustness | θ-鲁棒性：黑盒高斯噪声鲁棒性曲线与指数。/θ-robustness: black-box Gaussian-noise robustness curves & index. |
| [[2606.31110]] | 统计力学/Stat-Mech-ML | 博士论文：统计力学解释 ML 记忆与对抗鲁棒性。/PhD thesis: statistical mechanics of ML memorization & robustness. |

### 6. 对齐、安全、校准与不确定性 / Alignment, Safety, Calibration & Uncertainty

| 论文/Paper | 主题/Topic | 一句话/One-liner |
|---|---|---|
| [[2606.31876]] | 多模态安全/MARS | 文本拒绝方向跨模态迁移，视频越狱拒绝率 +59.4%。/Textual refusal directions transfer cross-modally, video jailbreak +59.4%. |
| [[2606.32032]] | 元认知/校准/RLMF | 元认知反馈 RL 实现忠实校准；小模型超 GPT-5。/Metacognitive-feedback RL for faithful calibration; sub-8B beats GPT-5. |
| [[2606.32012]] | 多模态不确定性/CoMet | Rényi-2 熵分解上下文/多答案不确定性，免生成。/Rényi-2 entropy decomposes context/multiplicity uncertainty, generation-free. |
| [[2606.32002]] | 合成数据脆弱/Self-Study | 自生成 QA 被显著伪影劫持；轻量防御 88%→13%。/Self-generated QA hijacked by salient artifacts; defense 88%→13%. |
| [[2606.31524]] | 在线对齐收敛/SAIL | 双层优化 + PL 条件下自改进在线 RLHF 收敛分析。/Convergence of self-improving online RLHF under PL/bilevel optimization. |
| [[2606.31399]] | 世界模型坍缩/World-Collapse | 长程智能体世界模型坍缩的相变分析。/Phase-transition analysis of world-model collapse in long-horizon agents. |
| [[2606.31273]] | 校准视角/Calibration-Turn | AI 辅助研究应转向证据许可的校准化声明。/AI-assisted research should shift to evidence-licensed calibrated claims. |
| [[2606.31653]] | 认证鲁棒/AD-CERT | 对抗蒸馏 + IBP，五基准 SOTA 认证精度。/Adversarial distillation + IBP, SOTA certified accuracy on 5 benchmarks. |
| [[2606.31092]] | 函数空间保护/Fora | 函数空间投影保护微调，遗忘减少约 3×。/Function-space projection protects fine-tuning, ~3× less forgetting. |
| [[2606.31648]] | 多语言 Agent/LuckyStar | 111B 韩英工具调用 Agent；4-bit 单 H100 部署。/111B Korean-English tool-using agent; 4-bit single-H100 deploy. |

---

## All Papers

| 论文/Paper | 简称/Short Title |
|---|---|
| [[2606.30995]] | Multistage Defer Trees / 多阶段延迟树 |
| [[2606.31023]] | Certified Speculative Execution / 认证推测执行 |
| [[2606.31046]] | OpenLife / 开放世界人工生命 |
| [[2606.31092]] | Fora / 函数空间保护 |
| [[2606.31106]] | Probing Autonomous Driving / 探针看自动驾驶 |
| [[2606.31110]] | Statistical Mechanics of ML / ML 统计力学 |
| [[2606.31121]] | Janus Memory Controller / 记忆控制器 |
| [[2606.31134]] | Autoformalizing Math / 自动形式化数学 |
| [[2606.31182]] | Convex Relaxations via Dual Agents / 凸松弛 |
| [[2606.31191]] | ISM / 自改进策略记忆 |
| [[2606.31229]] | Agentic-Ideation / 智能体构想 |
| [[2606.31257]] | Decodable Is Not Grounded / 解码≠接地 |
| [[2606.31270]] | Learning from Failure / 计算机使用智能体 |
| [[2606.31273]] | The Calibration Turn / 校准转向 |
| [[2606.31282]] | Volume Hypothesis / 体积假设 |
| [[2606.31308]] | InterFLOPBench / 浮点错误分类 |
| [[2606.31394]] | Resolving Superposition / 解耦叠加 |
| [[2606.31399]] | World-Model Collapse / 世界模型坍缩 |
| [[2606.31456]] | GoodQ / 检测器零样本量化 |
| [[2606.31478]] | SAGE Failure Attribution / 失败归因 |
| [[2606.31514]] | MINT / FPGA 动态精度 |
| [[2606.31519]] | RaBitQCache / KV 缓存二值量化 |
| [[2606.31524]] | Self-Improving Online Alignment / 在线对齐收敛 |
| [[2606.31551]] | AutoTrainess / 自主后训练 |
| [[2606.31575]] | RSI for RLVR / RLVR Token 选择 |
| [[2606.31581]] | NN Robustness to Noise / 噪声鲁棒性 |
| [[2606.31591]] | Evil Spectra / 涌现失准的优化器效应 |
| [[2606.31630]] | Calibration Not Compilation / 校准非编译 |
| [[2606.31648]] | LuckyStar 111B / 韩英 Agent |
| [[2606.31651]] | FARS / 全自动研究系统 |
| [[2606.31653]] | AD-CERT / 对抗蒸馏认证 |
| [[2606.31686]] | ROSR / 特征排序停止规则 |
| [[2606.31699]] | Look But Don't Touch / SAE 检测式遗忘 |
| [[2606.31763]] | ProtoPilot / 生物协议自进化 |
| [[2606.31779]] | LOTUS / 循环 Transformer 隐式 CoT |
| [[2606.31813]] | LoRA-RLPO / RLVR 正交初始化 |
| [[2606.31845]] | Explicit Fuzzy Logic FFN / 显式模糊逻辑 FFN |
| [[2606.31856]] | Low-dim Topology of DNNs / DNN 低维拓扑 |
| [[2606.31859]] | Review Residuals / 残差门控 |
| [[2606.31876]] | MARS / 多模态拒绝引导 |
| [[2606.31963]] | Signed-Permutation Gauge / 符号置换规范 |
| [[2606.31986]] | CoLT / 多模态潜在思维链 |
| [[2606.32000]] | Radial Suppression / 径向抑制加速 Grokking |
| [[2606.32002]] | Self-Study Reconsidered / 自生成 QA 脆弱性 |
| [[2606.32005]] | RR Dominates SGD / 随机重排优于 SGD |
| [[2606.32008]] | Surrogate Fidelity / 替代保真度 |
| [[2606.32012]] | CoMet / 多模态不确定性分解 |
| [[2606.32022]] | SemRF / 残差流语义参考系 |
| [[2606.32032]] | RLMF / 元认知反馈 RL |
| [[2606.32038]] | Introspective Coupling / 内省耦合 |
