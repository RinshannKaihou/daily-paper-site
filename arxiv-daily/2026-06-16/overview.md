---
title: "Daily Paper Overview — 2026-06-16"
date: 2026-06-16
tags: [arxiv-daily, llm, mechanistic-interpretability, self-evolving-agents, safety, optimization]
papers: 50
---

# 2026-06-16 论文速览 / Daily Paper Overview

本批共 50 篇论文，覆盖 LLM 机理可解释性、推理与后训练、Agent 自我演化、安全与对齐、训练优化、理论与数学基础、多模态、机器人与世界模型等方向。 / This batch contains 50 papers spanning mechanistic interpretability, reasoning & post-training, self-evolving agents, safety & alignment, training optimization, theory & mathematical foundations, multimodal, and robotics & world models.

## 今日必读 / Must Read Today

| # | 论文 / Paper | 一句话理由 / Why Read (中 + En) |
|---|---|---|
| 1 | [[2606.17478]] — *StateWitness* | 把"对目标 LLM 隐藏状态的标量探针"升级为"独立审计解码器 + 自然语言报告 + 结构化 Schema"，在 GPT-OSS-20B / Gemma4 上对 7 个欺骗基准达到 0.916 平均 AUROC，比最强黑箱监视器高 11.6%、比最强线性探针高 25.0%，并支持 token / 句子 / 报告级多粒度证据。 / Upgrades scalar probes of a target LLM's hidden states into a queryable, schema-formatted audit decoder that returns both calibrated scores and inspectable evidence. Mean AUROC 0.916 across 2 targets × 7 benchmarks; +11.6% over the best black-box monitor and +25.0% over the best linear probe. |
| 2 | [[2606.18089]] — *Compositional Generalization in Reasoning* | 用"层级潜变量选择"形式化 SFT+RL 流水线，理论证明 SFT 永远"鉴定"不出支持外的关键局部事件，而 RL 在 reward-informative + rollout-reachable 时会以 ∝ p̂₀(E)(1−p̂₀(E))ΔE 的强度富集这些事件；提出"SFT 覆盖原子 / SFT 与 RL 数据应"分工不重叠"的可操作协议。 / Formalizes SFT+RL post-training as hierarchical latent selection. Proves SFT has a hidden-support obstruction while RL can enrich identification-critical events; the disjoint SFT/RL composition-set protocol emerges as the optimal curriculum. |
| 3 | [[2606.17830]] — *Functional Equivalence in Attention* | 形式化注意力与位置编码的函数等价对称群，严格证明 sinusoidal PE 保持 vanilla 注意力的完整对称群，而 RoPE 将其严格缩小为 `S_h × H(d_h) × GL(d_h)`（`H(d_h) ≅ (C×)^{d_h/2}`），并据此解释 RoPE 的实际主导地位；附带两阶段 weight-matching 算法，揭示大规模 decoder-only LLM 的 LMC 行为失败。 / Formalizes MHA's functional-equivalence symmetry group. Proves sinusoidal PE preserves the full group while RoPE strictly reduces it to `S_h × H(d_h) × GL(d_h)`, giving a principled explanation for RoPE's dominance; the LMC study on large decoder-only LMs is an empirically important negative result. |

## 按主题分类 / Papers by Topic

### 1. LLM 机理可解释性 / Mechanistic Interpretability

| 论文 / Paper | 核心贡献 / Key Contribution (中 + En) |
|---|---|
| [[2606.17389]] — *Visuals Lie, Consistency Speaks (VRP)* | 跨 3 个 VLM 家族提出"可靠性探针"框架，发现空间注意力与正确性几乎零相关（R≈0.001），自一致性是最佳行为信号（R=0.429），隐藏状态探针是最强单次推理信号（AUROC>0.95），并存在"LLaVA 晚期脆弱瓶颈 vs PaliGemma/Qwen2-VL 全局分布"的架构级因果分歧。 / Cross-family reliability probe showing attention correlates near zero with correctness while self-consistency and hidden-state probes are the strong signals; reveals an architectural divergence between LLaVA's fragile late-stage bottleneck and the distributed reliability of PaliGemma / Qwen2-VL. |
| [[2606.17648]] — *From Brewing to Resolution* | 提出"酿造—消解"双阶段代码推理生命周期，线性探测（CSD 与 CSD 信息可用性/就绪度）显示答案在层间 ~14% 深度可恢复、~50% 才可自解码；通过三类因果干预验证 Resolved/Overprocessed/Misresolved/Unresolved 四分类对应可因果干预的计算状态。 / Dual-diagnostic framework (linear probing + Context-Stripped Decoding) reveals a ~38% brewing interval in code-reasoning LLMs. Three causal interventions validate the four-outcome taxonomy as intervention-sensitive computational states. |
| [[2606.17832]] — *From Drift to Coherence* | 在 MCQA 场景下检验 LLM 信念的鞅性质：通过 Prompted Predictive Resampling (PPR) 揭示"早期信念漂移—后期自稳定"两阶段；提出答案种子化和自一致性损失微调（SC loss），摊销 burn-in 阶段，使模型零样本即可输出近似鞅的稳定预测分布。 / Tests the martingale property of LLM beliefs in MCQA via Prompted Predictive Resampling. Identifies a two-phase drift-then-stabilize dynamic and proposes answer seeding + SC loss to amortize stabilization. |
| [[2606.17953]] — *MLLMs Get It Right, Then Get It Wrong* | 通过逐层 Modal Dominance Ratio (MDR) 诊断发现 MLLM 在中间层已形成正确视觉预测，末层被文本覆盖（"late-layer textual override"）；提出训练免费解码方法 CALRD，在 5 个 MLLM 上取得最高 9.4% 冲突基准绝对提升。 / Layer-wise Modal Dominance Ratio (MDR) diagnosis reveals late-layer textual override. The training-free CALRD intervention yields up to 9.4% absolute gains on conflict benchmarks across 5 MLLMs. |

### 2. LLM 安全、对齐与可解释审计 / Safety, Alignment & Auditing

| 论文 / Paper | 核心贡献 / Key Contribution (中 + En) |
|---|---|
| [[2606.17467]] — *PARSE* | 提出六阶段"领域有效性门控"流水线（域分类 + 指令性门 + 句子级注入打分 + 结构化事实预提取 + 事实一致性校验循环），将攻击成功率从 25.4% 降至 15.6%，utility 维持 86.9%，是真实长文档场景下"基于接地审计而非准确率"的部署范式。 / Six-stage provenance-aware sanitization pipeline reducing ASR from 25.4% to 15.6% on real enterprise documents (5 domains, 122 tasks); argues for grounding audits over accuracy as the clinical-deployment gate. |
| [[2606.17478]] — *StateWitness* (见 Must Read #1) / See Must Read #1 | 详见今日必读第一项 / See Must Read entry #1. |
| [[2606.18037]] — *ProvenanceGuard* | 为 MCP 协议 LLM Agent 提出源感知事实核查器，独立判断"是否被某来源支持"与"是否归因到正确来源"，在 40 轨迹 held-out 上 block F1 0.802、源准确率 0.858，50 个临床 conflation 探针全部检出。 / Source-aware factuality verifier for MCP-based agents that detects "cross-source conflation" missed by pooled-evidence metrics; reaches block F1 0.802 / source-accuracy 0.858 on a held-out medical agent benchmark. |
| [[2606.18060]] — *PseudoBench* | 首个面向 auto-research 智能体的伪科学对抗基准（200 对人工策划的伪科学主张-证据），测试 7 款 SOTA 系统发现最高抵抗力仅 27.4%，且"更强的智能体反而把伪科学包装得更具说服力"。 / First adversarial benchmark targeting pseudoscience-resistance in agentic auto-research. All 7 SOTA systems produce polished pseudoscientific papers in minutes; stronger systems package pseudoscience more persuasively. |
| [[2606.18062]] — *WildChat S&P Prompts* | 基于 WildChat 3.2M 真实对话挖掘 14,727 条 S&P 提示，建立 9 类主题分类法；270 条建议型提示上 5 模型 × 10 次运行表明，GPT 5.5 质量最高（8.67/10）但跨次仍 ~3% 给出矛盾回复，Llama 4 一致性最高（97.4%）但质量最低（6.71）。 / First large-scale empirical corpus of real-world S&P prompts. Quality-consistency are decoupled: GPT 5.5 is highest-quality (8.67) but Llama 4 is most consistent (97.4%) at lowest quality (6.71). |
| [[2606.18120]] — *Handlebars Structural Role Injection* | 5760 次跨 4 模型 × 7 定界符家族 × 2 攻击目标的对照实验证明：Handlebars `{{x}}` HTML 转义对 ChatML/Llama-3/XML 完全中和（存活率 0.00），但对 `Human:`/`Assistant:`、Markdown `###` 完全无防护（存活率 1.00）；Claude Haiku 4.5 全场景 0% ASR。 / 5,760-trial factorial study isolating Handlebars' escaped vs raw mode. Markdown, Anthropic-style, and Llama-2 square-bracket delimiters survive escaping byte-for-byte; Claude Haiku 4.5 holds at 0% across all conditions. |
| [[2606.18193]] — *Red-Team Fable 5 & Opus 4.8* | 独立第三方（AI4I）对 Anthropic Opus 4.8 / Fable 5 发起 4 类自动越狱（TAP/PAIR/PAP/h4rm3l）× 7,826 有害意图 × 10 类别；TAP 在 Opus 4.8 上 11.51% ASR（儿童安全子类 27.6%），静态混淆几乎被压制（≤ 0.18%），但自适应迭代攻击占绝对主导。 | Third-party red-team audit of Anthropic Opus 4.8 and Fable 5 on 7,826 intents. Adaptive iterative attacks dominate (TAP 11.51% on Opus 4.8; 27.6% on child-safety cell). |
| [[2606.17872]] — *AnchorKV* | 在 FastKV 的 token-selective propagation 评分中注入一个离线预计算的"refusal 方向"软惩罚；在 25% 缓存保留率下将 Llama-3.1-8B 的 AdvPrompter 越狱 ASR 从 0.68 降至 0.13（相对降低 81%），同时 LongBench 16 任务平均分仅下降约 1 分。 / Adds a refusal-direction soft penalty to FastKV's TSP retention score. Reduces ASR from 0.68 to 0.13 (81% relative) at 25% cache retention with <1 pt LongBench regression. |

### 3. 推理、强化学习后训练与蒸馏 / Reasoning, RL Post-Training & Distillation

| 论文 / Paper | 核心贡献 / Key Contribution (中 + En) |
|---|---|
| [[2606.17524]] — *ReLAR* | ReLAR 是一个在解码前用强化学习训练的深度+动作控制器迭代精炼 LLM 隐藏状态的框架，0.14s 推理延迟 vs CoT 的 9.09s，在 PubMedQA、GSM-Hard、HotpotQA、开放式生成上一致击败 SFT 基线。 / Reinforcement-guided latent-refinement controller. 0.14 s vs CoT's 9.09 s with comparable or higher accuracy on medical, math, multi-hop, and open-ended benchmarks. |
| [[2606.17591]] — *Verbal RL Insight Governance* | 在 S&P 500 五大科技股 2017 测试集上证明：同一份累积经验在无治理时跌破 zero-shot（46.3% vs 51.2%，负 Sharpe），在完整 critic–proposer–curator 治理回路下则显著优于基线（56.5% 准确率，Sharpe 翻倍至 1.00）。 | Empirical test of "retention-forgetting dilemma" in training-free verbal RL. Same experience degrades without governance; the critic–proposer–curator loop doubles Sharpe and halves MaxDD. |
| [[2606.17628]] — *OPD-Evolver* | 提出"快慢协同进化"框架，将四层记忆层次（轨迹 / 提示 / 技能 / 工具）与结果校准的归因 + 特权后视的策略内自蒸馏结合；使 9B 模型以 6/10 胜率挑战 Qwen3.5-397B-A17B、9/10 胜率压过 Step-3.5-Flash (196B)。 | Fast/slow co-evolution of a four-level memory hierarchy with outcome-calibrated credit assignment and privileged-hindsight self-distillation. 9B beats Step-3.5-Flash (196B) on 9/10 subsets. |
| [[2606.17682]] — *LLM-as-Environment-Engineer* | 提出 "LLM-as-Environment-Engineer" 闭环框架，让当前策略模型在每轮 GRPO 训练后基于失败证据改写下一阶段 MAPF-FrozenLake 配置；Qwen3-4B 在 3/4/5 智能体评估集上以 51.67/33.14/18.67 的有效率击败 GPT-5.4、Gemini-3.1-Pro、Kimi-K2.5。 / Closed-loop LLM-as-Environment-Engineer. The RL-trained checkpoint is a *better* engineer than the base model, and bookkeeping-only training context outperforms the full RL context. |
| [[2606.17890]] — *DRE (Dynamic Rollout Editing)* | 针对 GRPO 训练中"答对后还继续思考"的过度思考现象，提出训练时干预方法 DRE：在答案出现后找到安全的可编辑边界并截断冗余思考；3 个 Qwen3 推理模型上平均节省 22–28% 思考 token 同时保持或提升准确率。 | Training-time intervention attacking "overthinking" as a GRPO credit-assignment artifact. Reduces thinking tokens by 22–28% with no accuracy loss across 3 Qwen3 backbones. |
| [[2606.18089]] — *Compositional Generalization* (见 Must Read #2) | 详见今日必读第二项 / See Must Read entry #2. |
| [[2606.18216]] — *ZPPO* | 把教师"留在 prompt 里"而非梯度中，用 BCQ（教师对 vs 学生错）和 NCQ（聚合学生自己的错误）两道 prompt 改写"全班错"的难题；Qwen3.5 的 0.8B–9B 四档学生上 31 个基准一致击败 on/off-policy 蒸馏与 GRPO，小模型差距越大收益越大。 | RL post-training paradigm that routes teacher signal into the prompt rather than the policy gradient. ZPPO > off-policy KD ≈ on-policy KD ≈ GRPO at every scale; OOD result is the strongest selling point. |

### 4. 自演化 Agent 与持续学习 / Self-Evolving Agents & Continual Learning

| 论文 / Paper | 核心贡献 / Key Contribution (中 + En) |
|---|---|
| [[2606.17546]] — *SEAGym* | 把"agent harness"（prompt + memory + tools + middleware + runtime + 模型-工具 loop）作为自演化的对象，提供 RL 风格的多视角评测环境（训练 / 更新验证 / ID 转移 / OOD 转移 / replay / cost），揭示"频繁更新可能不提升 held-out 性能"、"源多样性对 harness 可靠性有显著影响"等非平凡结论。 | Reframes evaluation of self-evolving agents on the harness update process via six complementary views. AHE is the only method that lifts validation, ID, and OOD together. |
| [[2606.17803]] — *ELM* | ELM 方法将每个测试样本上消耗的推理时计算蒸馏为 20-token 软提示"潜在记忆"（~0.001% 参数），用 GRPO + 多数投票自奖励训练 10 步后存储检索，并在不可靠时由 PRM 验证器路由；在 MATH500/AMC23/AIME24 上以在线方式匹配甚至超过全数据集离线训练。 | Strictly online continual self-improvement with per-sample ~0.001%-parameter latent memories. Beats or matches full-dataset offline GRPO/TTRL on math benchmarks. |
| [[2606.18144]] — *Memory as a Wasting Asset* | 将机器人闪存耐久度建模为不可再生资本品，引入耐久度影子价格 η 与"价值–写入"耦合系数 χ，推导出磨损加权的放置指数在 χ>0 时关于价值呈非单调最优；在 LIBERO-Long × SmolVLA-0.5B 上 χ̂=+1.016×10⁻³（Holm 拒绝零），DROID 上 χ̂ 为负。 | Prices on-board NAND as depreciating capital with a single shadow price η. The wear-augmented index is non-monotone in value when χ > 0, but the realized controller does not beat price-based routing. |

### 5. 训练优化与架构 / Training Optimization & Architecture

| 论文 / Paper | 核心贡献 / Key Contribution (中 + En) |
|---|---|
| [[2606.17522]] — *Bounded-Depth CFG Transformers* | 对固定深度、非递归的均匀 CFG 显式构造位置注意力 Transformer，使深度随文法深度线性增长、宽度随推导树形状数线性 / 随产生式数平方增长，并在每一层实现自底向上的动态规划解析。 | Constructive capacity proof for bounded-depth non-recursive CFGs: transformer depth scales with grammar depth (improvement over Zhao et al. 2023's depth-in-L). |
| [[2606.17526]] — *MGUP* | 提出"动量-梯度对齐"的层内选择性更新策略，包装 AdamW/Lion/Muon，对 top-τd 参数放大步长 η_t/τ、其余施以 τη_t，并附带 MGUP-AdamW 的 O(log T/√T) 收敛率证明；在 LLaMA-71M / Qwen-150M 上取得 1.6–2.5× 加速。 | Momentum-gradient alignment update policy with O(log T/√T) convergence rate. 1.6–2.5× speedup over AdamW/Lion/Muon on LLaMA-71M and Qwen-150M. |
| [[2606.17816]] — *Conservation Laws for Modern Architectures* | 系统给出 GELU/SiLU FFN（无任何非平凡守恒律）、SwiGLU FFN（‖A:,i‖²−‖C_i,:‖²）、vanilla MHA、RoPE（复结构 J 耦合）、稠密/稀疏 MoE 的全部显式守恒不变量；方法上将"找全部守恒律"等价刻画为对守恒函数的 PDE 求解问题。 | Reframes conservation-law characterization as a PDE on the conserved function. Proves GELU/SiLU FFNs admit only trivial laws; SwiGLU admits per-unit ‖A:,i‖²−‖C_i,:‖². |
| [[2606.17945]] — *Small Initialization Matters* | 系统证明 LLM 预训练中的"小初始化"是一种近乎零成本的"基因式"调控旋钮——减小初始化尺度能持续降低预训练损失（推理任务上增益最大），但默认架构中 RMSNorm 的 ε 与"注意力沉头"会掩盖这一收益；通过将 ε 从 10⁻⁵ 调到 10⁻¹² 并加入 gated attention 即可释放该收益。 | Small initialization (γ=1 vs γ=0.5) is a "gene-like" lever. RMSNorm ε saturation and attention-sink intensification mask the benefit; ε=1e-12 + gated attention releases it. |
| [[2606.18080]] — *Edge Flow* | 提出 Edge Flow——一个由"中心、振荡方向、振荡幅度"三条耦合 ODE 组成的连续时间模型，在边沿稳定区间内对 GD 的振荡动力学进行可分解、可预测的建模；衍生出比 GD 更稳定的离散化算法 EGD。 | Three-ODE continuous-time model (center / direction / magnitude) for gradient descent at edge-of-stability. Reproduces sharpness overshoot + damped ringing that Central Flow cannot. |
| [[2606.18114]] — *Ternary Mamba* | 通过分组（W1.58A16）+FP16 教师知识蒸馏的 QAT 训练，仅用 102M tokens（单卡 H100 4 GPU-小时）将 Mamba-2 1.3B 压缩 3.61×（2,687→744MB），零样本 7 任务平均 48.1% 逼近 Bi-Mamba 48.4%；并发现 QAT-from-pretrained 特有的"零比率坍缩"现象。 | Ternary QAT-from-pretrained for SSM. 4 GPU-hours vs Bi-Mamba's 5,780 GPU-hours. Identifies "zero-ratio collapse" failure mode unique to QAT-from-pretrained SSMs. |

### 6. 评估基准与微调预测 / Evaluation, Benchmarks & Fine-Tuning Prediction

| 论文 / Paper | 核心贡献 / Key Contribution (中 + En) |
|---|---|
| [[2606.17417]] — *LALM Failure Modes* | 实证揭示 LALM 在时序推理任务上的系统失败，构建 TACOS 衍生的 1,657 题基准，在 Audio-Flamingo-3 与 DeSTA-2.5-Audio 上首次做因果机制干预——发现"注意力重分配（scaling）优于单纯放大（upweighting）"，瓶颈层干预可在零微调下将平均准确率从 55.9% 提升至 59.1%。 | Diagnostic benchmark + first causal mechanistic intervention on open-source LALMs. Bottleneck-layer attention scaling intervention improves accuracy from 55.9% to 59.1% with no fine-tuning. |
| [[2606.17541]] — *Offline Preference-Based Trajectory Evaluation* | 提出 LR/RPP/IPP 三种成对轨迹偏好度量，用时间偏好替代二元成功度量，将 agentic benchmark 的并列率从 ~75% 降至 ~35%，oracle 偏好恢复率从 PR/SR 的 12.8% 提升至 ~95%。 | Three trajectory-preference measures (LR/RPP/IPP) that cut tie rates from ~75% to ~35% and lift oracle-preference recovery from ~13% (SR/PR) to ~95% on agentic benchmarks. |
| [[2606.17588]] — *Title-Abstract Screening* | 在 6 项软件工程 SR（>1,000 篇 primary study，Cohen's Kappa 0.52–0.77）上系统归纳 LLM 标题-摘要筛选阶段的分歧，建立含 7 类模式的两层错误分类法（词法→语义），并基于失败模式给出 5 条可执行部署建议。 | Qualitative taxonomy of LLM–human disagreements in title-abstract screening with 7 patterns (Term-Boundary, Abstract-Omission, Keyword-Overweight, etc.) and 5 actionable recommendations. |
| [[2606.17649]] — *Risk Decomposition for Fine-Tuning* | 通过全方差分解把预测风险拆成静态数据-模型兼容性下限和可约减的优化方差，推导出预算最优的探测停止条件 c* = (αK/(γλ))^{1/(α+1)}；并把任务划分为 Static-Sufficient / Dynamic-Critical / Noise-Dominant 三类可预测性相区。 | Two-component risk decomposition (L_int + V_opt) with a closed-form budget-optimal probing depth and a "predictability phase diagram" classifying fine-tuning tasks. |
| [[2606.17660]] — *TuneAhead* | 提出 14 个静态数据集描述符 + 10 个来自 100 步 standardized probe 的动态特征拼成 24 维 meta-feature，用 LightGBM 预测细调得分；在 1,300+ Qwen2.5-7B LoRA 微调上达到 1.47 pp RMSE、95.1% Acc@3pp；SHAP attribution 还能驱动针对性干预，把一个 20.2% MMLU 失败 run 救回到 48.7%。 | 24-dim meta-feature + LightGBM + TreeSHAP for pre-hoc fine-tuning performance prediction. 1.47 RMSE, 95.1% Acc@3pp on 1,300+ Qwen2.5-7B LoRA runs. |
| [[2606.17930]] — *How Inference Compute Shapes Frontier LLM Evaluation* | 基于 UK AISI 的统一受控评估框架（6 个前沿模型 × 5 个主基准 + 2 个网络空间基准，5M–100M token 预算），证明推理时算力会以"领域相关"的方式显著抬升基准分数，代际增益主要来自 reach（解锁更难的题）和 reliability（更稳定地解出）而非 token 效率。 | AISI controlled evaluation shows inference-scaling gains are benchmark-dependent; generational gains come from reach + reliability, not token efficiency. |

### 7. 多模态 / VLM / 视觉 / Multimodal & Vision

| 论文 / Paper | 核心贡献 / Key Contribution (中 + En) |
|---|---|
| [[2606.17410]] — *VLM-Human Attention Alignment* | 2×2 因子对比（CNN vs ViT 编码器 × LSTM vs Transformer 解码器）及两个大型 VLM（Molmo 7B-D、Qwen3.5 9B），发现 LSTM 解码器比 Transformer 解码器在与人眼注视对齐上高出 25–45 个百分点，但这种对齐以空间弥散、任务无关为代价。 | 2×2 factorial (CNN/ViT × LSTM/Transformer) shows LSTM decoders beat Transformer decoders by 25–45 pp on human gaze alignment but at the cost of spatial diffuseness. |
| [[2606.17603]] — *SPHERE-JEPA Family* | 把切片式统计正则化（SIGReg / SUSReg）的随机投影方差解析积掉，得到原生的全维 MMD / KSD / KL 正则化族，配以旋转不变 Heat / Bandlimited 核，在 ImageNet / Galaxy10 上同时获得更稳定训练和更强下游表现。 | Analytic-equivalence bridge from sliced variance to deterministic MMD, plus rotationally invariant kernel families; MMD/KSD favor object-centric, KDE-KL favors instance-separated layouts. |
| [[2606.17710]] — *Chest X-ray VLM Grounding* | 设计因果"图像干预三联审计"评估 9 个胸片 VLM，发现 3 个完全忽略图像、1 个不稳定、5 个选择性使用图像；纯文本模型与放射科医生准确率统计不可区分但 grounding 为零，作者据此提出"以接地审计而非准确率"作为临床部署门槛。 | Causal image-intervention triad classifies 9 chest-X-ray VLMs into 3 ignoring / 1 unstable / 5 selectively using. A 119B multimodal is statistically indistinguishable from a 7B text-only on accuracy. |
| [[2606.17824]] — *3D Asset Segmentation* | 端到端人机协同分割流水线：先以路径规划启发的贪婪集合覆盖算法挑选覆盖整个 3D 模型的最小相机视角集（8 个对象均收敛到 8 视图），再借助 SAM 2 + Label Studio 在 2D 视图上交互式分割并通过索引 pass 反向投影到 UV atlas；平均 ~21 分钟生成可用的分段 atlas。 | Greedy set-cover view selection + SAM 2 + index-pass back-projection. ~21 min per object on 8 cultural-heritage assets. |
| [[2606.17961]] — *simPE Rotation Robustness* | 给出 simPE 位置编码关于旋转扰动的 Lipschitz 稳定性证明（Frobenius 范数显式界），在 4 个受控数据集上证明在小到中等角度上 simPE 一致优于标准学习型位置编码（Arrow 在 25° 领先 ~50pp）。 | First rigorous Lipschitz-stability analysis of simPE under rotations. Strong gains at small-to-moderate angles; crossovers at large angles. |
| [[2606.18124]] — *Geographic Conditioning* | 系统评估 5 个 SOTA LLM 在 3 种地理元数据注入方式下的"位置泄漏"现象，最高泄漏达 793×基线；"Unknown" 占位符控制实验分离出独立的结构性条件效应（12–72×），LoRA 微调无法有效缓解该偏差。 | Location-leakage audit across 5 SOTA LLMs × 3 injection methods × 193 countries. "Unknown" control isolates a structural conditioning effect (12–72×) that LoRA cannot debias. |

### 8. 理论与数学基础 / Theory & Mathematical Foundations

| 论文 / Paper | 核心贡献 / Key Contribution (中 + En) |
|---|---|
| [[2606.17399]] — *Discrete-Log Clock* | 用乘法特征变换（而非标准加法 DFT）分析 grokked Transformer 在 a·b mod 113 上的嵌入，证明频谱是稀疏的（仅 4 个关键频率、Gini 0.58、96.9% 神经元单频调谐），并据此提出"离散对数钟"算法。 | Multiplicative character transform reveals sparse grokked spectrum. 96.9% of MLP neurons are mono-frequency in the multiplicative basis. |
| [[2606.17426]] — *Concentration for Exchangeable Sequences* | 借助 de Finetti 表示给出无限可交换序列有界差分函数的有效方差代理 σ_eff² = (1/4)∑c_i² + σ_mix²；证明零和线性对比下 σ_mix² 精确消去；在 MMLU 全部 14,042 题上对 6 个开源模型实证，用 5,000 题可获得 1.54 pp 95% 误差保证。 | de Finetti–McDiarmid concentration with zero-sum cancellation. 5,000 MMLU items yield 1.54 pp 95% bound — 35.6% of the full benchmark. |
| [[2606.17830]] — *Functional Equivalence* (见 Must Read #3) | 详见今日必读第三项 / See Must Read entry #3. |
| [[2606.18218]] — *Finite-Time Queue Peak Laws* | 在一致内点松弛条件下，证明 MaxWeight 调度的有限时队列峰值存在两阶段包络——几何阈值以下保持 √T 律，超过阈值后仅以 D/ε 的（与容量几何无关的）系数对数增长；在输入排队交换机上给出紧对数系数。 | Two-phase finite-horizon peak law for MaxWeight. Geometry-free log coefficient D/ε; sharp n^{3/2}/ε for generalized IQS improving to n/ε under Bernoulli arrivals. |

### 9. 机器人、具身与世界模型 / Robotics, Embodied AI & World Models

| 论文 / Paper | 核心贡献 / Key Contribution (中 + En) |
|---|---|
| [[2606.18043]] — *UQ-VLA (SAVE)* | 推导 flow-matching 模型间 KL 散度与速度场差异的解析关系，提出基于速度场不一致（VFD）的认知不确定性估计器，并构建 SAVE 主动多任务微调框架；在 LIBERO-10 上 VFD 校准优于六种基线，SAVE 用至少少 22% 的专家示范即达到 67% 的多任务成功率。 | Velocity-Field Disagreement (VFD) estimator for flow-matching VLAs. SAVE active fine-tuning needs 22% fewer demos than the next-best UQ baseline. |
| [[2606.18186]] — *Kolmogorov Regression* | 将有限维扩散策略提升到 Cameron-Martin 子空间，用 Matérn-3/2 协方差的有色噪声 + precision-weighted Cameron-Martin 损失 + 反向 Kolmogorov 残差诊断三处替换；在 PushT 上提升最大回合奖励 17%、漂移降低 67.6%，并在 6 工位 CONWIP 制造线上以 Hamilton-Jacobi 到达性认证减少 96% 死锁。 | Cameron-Martin diffusion policies via three drop-in substitutions. +17% max reward on PushT; Hamilton-Jacobi reachability prevents 96% of deadlocks on a 6-station CONWIP line. |
| [[2606.18208]] — *Looped World Models* | 首次将参数共享的循环 Transformer 架构用于世界建模；通过谱约束状态保留矩阵保证长 rollout 稳定性，并引入"延迟解码"只对潜在轨迹做端点解码；在 ScienceWorld / AlfWorld 上以约 1B 参数超越 Claude Opus 4.6 / Gemini 3 Flash。 | First looped-transformer world model. Prelude–Recurrent–Coda structure with spectrally-contractive Ā; Deferred Decoding. ⚠️ Comparators are zero-shot LLMs, not purpose-built world models. |

### 10. 专业领域方法 / Specialized Domains

| 论文 / Paper | 核心贡献 / Key Contribution (中 + En) |
|---|---|
| [[2606.17529]] — *DVG-MET* | 提出"领域有效性门控"的蜕变测试流水线，把候选蜕变关系经由"四条件 rubric + MR-card 可执行资产 + 二维 verdict + claim ledger"筛选为可审计的 oracle-free SciML 测试资产；主证据来自 MeshGraphNets 圆柱流 6 checkpoint × 3 轨迹。 | Domain-validity-gated metamorphic testing for SciML surrogates. MeshGraphNets primary evidence + cross-family transfer to FNO/PINN and a compressible airfoil task. |
| [[2606.18122]] — *Embedded ML* | 单作者 IEEE 综述以"系统工程"视角贯穿 MCU 嵌入式机器学习的完整流水线，以惯性动作识别与音频关键词唤醒两条链路为统一示例，总结 8 条实用设计规则与若干开放研究方向。 | Systems-oriented synthesis of the end-to-end embedded-ML lifecycle for microcontrollers. Two reference pipelines + 8 design rules + 5 open research directions. |

## All Papers

完整索引（按 arXiv ID 升序） / Complete index (sorted by arxiv_id):

| arXiv ID | 标题 / Title | 主题 / Topic |
|---|---|---|
| [[2606.17389]] | *Visuals Lie, Consistency Speaks (VRP)* | 机理可解释性 / Mechanistic Interpretability |
| [[2606.17399]] | *Discrete-Log Clock* | 理论与数学基础 / Theory |
| [[2606.17410]] | *VLM-Human Attention Alignment* | 多模态 / Multimodal |
| [[2606.17417]] | *LALM Temporal Failure Modes* | 评估基准 / Evaluation |
| [[2606.17426]] | *Bounded Difference Concentration* | 理论与数学基础 / Theory |
| [[2606.17467]] | *PARSE* | 安全 / Safety |
| [[2606.17478]] | *StateWitness* ⭐ | 安全 / Safety |
| [[2606.17506]] | *Second-Order Bias (SOB)* | 评估 / Evaluation |
| [[2606.17522]] | *Bounded-Depth CFG Transformers* | 训练优化 / Training Optimization |
| [[2606.17524]] | *ReLAR* | 推理与后训练 / Reasoning & Post-Training |
| [[2606.17526]] | *MGUP* | 训练优化 / Training Optimization |
| [[2606.17529]] | *DVG-MET* | 专业方法 / Specialized |
| [[2606.17541]] | *Offline Preference Trajectory Evaluation* | 评估 / Evaluation |
| [[2606.17546]] | *SEAGym* | 自演化 Agent / Self-Evolving Agents |
| [[2606.17588]] | *Title-Abstract Screening* | 评估 / Evaluation |
| [[2606.17591]] | *Verbal RL Insight Governance* | 推理与后训练 / Reasoning & Post-Training |
| [[2606.17603]] | *SPHERE-JEPA Family* | 多模态 / Multimodal |
| [[2606.17628]] | *OPD-Evolver* | 推理与后训练 / Reasoning & Post-Training |
| [[2606.17648]] | *From Brewing to Resolution* | 机理可解释性 / Mechanistic Interpretability |
| [[2606.17649]] | *Risk Decomposition for Fine-Tuning* | 评估 / Evaluation |
| [[2606.17660]] | *TuneAhead* | 评估 / Evaluation |
| [[2606.17682]] | *LLM-as-Environment-Engineer* | 推理与后训练 / Reasoning & Post-Training |
| [[2606.17710]] | *Chest X-ray VLM Grounding* | 多模态 / Multimodal |
| [[2606.17803]] | *ELM* | 自演化 Agent / Self-Evolving Agents |
| [[2606.17816]] | *Conservation Laws for Architectures* | 训练优化 / Training Optimization |
| [[2606.17824]] | *3D Asset Segmentation* | 多模态 / Multimodal |
| [[2606.17830]] | *Functional Equivalence in Attention* ⭐ | 理论与数学基础 / Theory |
| [[2606.17832]] | *Drift to Coherence (Martingale)* | 机理可解释性 / Mechanistic Interpretability |
| [[2606.17872]] | *AnchorKV* | 安全 / Safety |
| [[2606.17890]] | *DRE* | 推理与后训练 / Reasoning & Post-Training |
| [[2606.17930]] | *Inference Compute Evaluation* | 评估 / Evaluation |
| [[2606.17945]] | *Small Initialization* | 训练优化 / Training Optimization |
| [[2606.17953]] | *Late-Layer Textual Override (CALRD)* | 机理可解释性 / Mechanistic Interpretability |
| [[2606.17961]] | *simPE Rotation Robustness* | 多模态 / Multimodal |
| [[2606.18037]] | *ProvenanceGuard* | 安全 / Safety |
| [[2606.18043]] | *UQ-VLA (SAVE)* | 机器人 / Robotics |
| [[2606.18060]] | *PseudoBench* | 安全 / Safety |
| [[2606.18062]] | *WildChat S&P Prompts* | 安全 / Safety |
| [[2606.18080]] | *Edge Flow* | 训练优化 / Training Optimization |
| [[2606.18089]] | *Compositional Generalization in Reasoning* ⭐ | 推理与后训练 / Reasoning & Post-Training |
| [[2606.18114]] | *Ternary Mamba* | 训练优化 / Training Optimization |
| [[2606.18120]] | *Handlebars Structural Role Injection* | 安全 / Safety |
| [[2606.18122]] | *Embedded ML (TinyML)* | 专业方法 / Specialized |
| [[2606.18124]] | *Geographic Conditioning* | 多模态 / Multimodal |
| [[2606.18144]] | *Memory as a Wasting Asset* | 自演化 Agent / Self-Evolving Agents |
| [[2606.18186]] | *Kolmogorov Regression* | 机器人 / Robotics |
| [[2606.18193]] | *Red-Team Fable 5 & Opus 4.8* | 安全 / Safety |
| [[2606.18208]] | *Looped World Models* | 机器人 / Robotics |
| [[2606.18216]] | *ZPPO* | 推理与后训练 / Reasoning & Post-Training |
| [[2606.18218]] | *Finite-Time Queue Peak Laws* | 理论与数学基础 / Theory |

---

**统计 / Stats**: 50 篇论文 / 50 papers. ⭐ 标记为今日必读。 / ⭐ marks Must-Read papers.
