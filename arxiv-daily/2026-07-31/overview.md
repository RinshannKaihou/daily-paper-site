---
title: "Daily arXiv Digest — 2026-07-31"
date: 2026-07-31
tags: [LLM Agents, Agent Memory & Skill Evolution, Mechanistic Interpretability, LLM Safety & Alignment, Efficiency & Quantization, LLM-as-Judge Evaluation, Agentic Reinforcement Learning, Learning Theory, Computer-Use Agents, Test-Time Compute, Multimodal, Hardware Security]
papers: 50
---

## 今日必读 / Must Read Today

### [[2607.27539]] Exact LLM Memory Deletion

这篇论文首次把"精确删除"变成可证伪的表示论问题（可寻址 vs. 被后续写入变换），并在真实480亿参数混合模型上用检查点回退+重放，对18,842 token长度的真实临床病历做到逐位（bit-for-bit）删除验证，是目前对机器遗忘做得最严谨的实证检验之一。

This paper turns "exact deletion" into a falsifiable representation-theoretic question (addressable vs. transformed-by-write influence), and is one of the most rigorous empirical tests of machine unlearning to date — validating bit-for-bit deletion on real 18,842-token clinical records inside a 48B hybrid model via checkpointed rewind-and-replay.

### [[2607.28576]] Sample More, Reflect Less

该复现研究用严格的等token成本配对统计检验证明，Self-Refine、Reflexion、Best-of-N自我验证等热门"反思型"推理策略，在1.5B到7B模型上没有一个能显著超过最朴素的重复采样+多数投票，对整个test-time-compute研究方向是一记警钟。

This replication study rigorously shows, via cost-matched paired statistical tests across models from 1.5B to 7B, that popular reflective test-time-compute methods (Self-Refine, Reflexion, Best-of-N self-verification) never significantly beat plain repeated sampling with majority voting — a sobering result for the whole self-correction literature.

### [[2607.28568]] Frontis-MA1 AI4AI

该工作开源了一整套训练"会自我进化的机器学习工程智能体"的技术栈（任务环境+算子级训练+经验引导进化搜索），用35B模型在单张RTX 4090上于MLE-Bench Lite取得71.21%的奖牌均分，超过GPT-5.5+Codex的68.18%，是AI4AI/递归自我改进方向少见的完整可复现系统。

This work open-sources a complete stack (task environments, operator-level training, experience-guided evolutionary search) for training a self-evolving ML-engineering agent, whose 35B model reaches 71.21% Medal Average on MLE-Bench Lite using a single RTX 4090 — beating GPT-5.5+Codex's 68.18% — a rare, fully reproducible system for the AI4AI/recursive-self-improvement direction.

## 按主题分类 / Papers by Topic

### Agent Memory & Skill Self-Evolution / 智能体记忆与技能自演化

| Paper | 简述 / Gloss |
|---|---|
| [[2607.27557]] Skills-as-Parameters Diffusion | 用扩散式"腐蚀-重建"自监督信号更新外部MoE技能库，而非模型权重 / diffusion-style corruption-reconstruction self-supervision updates an external MoE skill library instead of model weights |
| [[2607.27687]] Rehearse: Confidence Cliff | 发现自动研究循环中判官选择性准确率随深度骤降的"信心悬崖"，用聚焦结果记忆修复 / finds a "confidence cliff" where judge accuracy collapses with loop depth in autoresearch, fixed with focused outcome memory |
| [[2607.27690]] LabEvolver Wet-Lab Agents | 双循环安全门+经验蒸馏驱动湿实验室机器人无训练权重更新的自演化 / dual-loop safety-gated experience distillation drives training-free self-evolution for wet-lab robots |
| [[2607.27733]] VeriSkill Verification Skills | 失败归因-模式抽象-可执行准入三阶段闭环，把验证器失败转化为技能更新 / a three-stage failure-attribution-to-lesson-to-admission loop turns verifier failures into vetted skill updates |
| [[2607.28048]] SKILL-KD Contrastive Distillation | 对比师生同任务成败轨迹差异，蒸馏成可迭代验证的文本技能补丁 / diffs student-failure vs. teacher-success trajectories into iteratively-validated textual skill patches |
| [[2607.28527]] MANTA Topology Adaptation | 推理阶段动态规划并修复多智能体通信拓扑（增删智能体、改边） / dynamically plans and repairs multi-agent communication topology at inference time |

### Agentic Science, Math & ML-Engineering Research / 科学与数学智能体研究

| Paper | 简述 / Gloss |
|---|---|
| [[2607.27705]] Albilich Math Research Agent | 持久化证明状态数据库+角色分权验证（研究者不可自证）驱动LLM数学研究 / a persistent proof-state database with role-separated verification (researchers cannot self-certify) drives agentic math research |
| [[2607.27709]] MECA Conjecture Agent | 猜想陈述与支撑机制耦合联合精化，生成有明确未解缺口的数学猜想 / jointly refines a conjecture statement and its supporting mechanisms into well-specified, prover-facing conjectures |
| [[2607.27562]] DeepResearch Agent (unverified) | 号称30B MoE深度研究智能体在HLE取得87.3%，但无实验表格/基线/消融，可信度存疑 / claims a 30B MoE deep-research agent hitting 87.3% on HLE, but reports zero tables, baselines, or ablations — credibility questionable |
| [[2607.28568]] Frontis-MA1 AI4AI | 开源全栈（任务环境+算子级训练+进化搜索）训练自我进化的机器学习工程智能体 / open full stack for training a self-evolving ML-engineering agent |
| [[2607.27929]] Meta-Task Terminal Agents | 把"合成终端任务"本身变成终端任务，数据高效地训练CLI智能体 / turns terminal-task synthesis itself into a terminal task for data-efficient CLI-agent training |

### Agentic RL & Credit Assignment / 智能体强化学习与信用分配

| Paper | 简述 / Gloss |
|---|---|
| [[2607.27888]] CSCR Credit Reallocation | 反事实重打分揭示自蒸馏token级信号只反映敏感度而非答案对齐，提出降权修正 / counterfactual re-scoring shows self-distillation's token signal reflects sensitivity not answer-alignment, fixed via downweighting |
| [[2607.28076]] GRSD Self-Distillation RL | 对比自身成功/失败反思构造群体级DO/AVOID指导，重塑回合级优势 / contrasts the policy's own successful/failed reflections to reshape turn-level advantages via group-level guidance |
| [[2607.27953]] AutoPref NCO Objectives | LLM引导的程序搜索自动发现组合优化任务专属的偏好损失目标 / LLM-guided program search automatically discovers task-specific preference objectives for combinatorial optimization |

### Computer-Use Agents & Their Evaluation / 计算机使用智能体与评测

| Paper | 简述 / Gloss |
|---|---|
| [[2607.28074]] Echoverse Computer-Use Envs | 数据库即真值的可交互应用+协同进化循环，规模化训练计算机使用智能体 / database-as-ground-truth interactive apps plus a co-evolution loop scale computer-use agent training |
| [[2607.28367]] CUA Benchmark Mis-Scoring | 复核五大基准150条"失败"轨迹，发现15.3%的FAIL判决本身是错的 / re-audits 150 "FAIL"-labeled trajectories across five benchmarks, finding 15.3% of verdicts are wrong |
| [[2607.28609]] OSReward CUA Judges | 跨平台裁判基准揭示27个VLM评委普遍存在"宽松偏差" / a cross-platform judge benchmark reveals pervasive "leniency bias" across 27 VLM judges |
| [[2607.28287]] Tycho ARC-AGI-3 World Models | 程序化世界模型+元推理策略，让智能体在ARC-AGI-3全部25个游戏上超越人类效率基线 / programmatic world models plus metareasoning let an agent beat the human efficiency baseline on all 25 public ARC-AGI-3 games |

### LLM-as-Judge & Evaluation Methodology / LLM裁判与评测方法论

| Paper | 简述 / Gloss |
|---|---|
| [[2607.27984]] Judge Specialization vs Deferral | 专精判官权重反而损害共享判断准确率，但把专精放进路由/延迟决策能改善级联效率 / specializing judge weights hurts shared-judgment accuracy, but specializing the deferral/routing decision improves cascade efficiency |
| [[2607.28128]] Helpfulness vs Pedagogy Judges | 通用"有帮助性"裁判测不出教学策略质量差异，且跨裁判排序会反转 / a general-purpose helpfulness judge misses pedagogy-quality differences, and rankings flip across judge models |
| [[2607.28282]] LLM Elo Evaluation (Towards) | 多LLM双向成对比较+Elo聚合排名，相关性尚未达统计显著 / multi-LLM pairwise comparison plus Elo aggregation, though correlations with human rankings fall short of statistical significance |
| [[2607.28008]] RepBench Capability Probing | 从13,427篇基准论文构建182类能力体系与跨基准可迁移探测语料 / mines a 182-category capability taxonomy and transferable probing corpus from 13,427 benchmark papers |

### Mechanistic Interpretability & Representation Steering / 机制可解释性与表征干预

| Paper | 简述 / Gloss |
|---|---|
| [[2607.27617]] Hidden APIs / Forked Futures | 用预测性因果MDL把"模型是否存在可复用共享接口"变成可证伪的架构选择问题 / uses predictive causal MDL to turn "does the model reuse a shared internal interface" into a falsifiable question |
| [[2607.27824]] STEREODISCO | 把心理学"语义差异法"搬进LLM内部激活，发现刻板印象方向及裁判间过度一致现象 / adapts the psychological semantic-differential method to LLM activations, revealing stereotype axes and inter-model over-agreement |
| [[2607.28319]] Fairness Pruning GLU-MLP | 差分激活定位偏见敏感神经元，但归零操作导致有偏差方向的"双向失稳"而非系统性去偏 / differential activations localize bias-sensitive neurons, but zeroing them causes directionless "bidirectional instability" rather than systematic debiasing |
| [[2607.28434]] Metaphor Tracer Hidden States | 聚合器/差异器双通道单次前向为隐藏状态逐词打分，获精神分析师独立标注验证 / a two-channel, single-forward-pass instrument scores hidden states, validated against a psychoanalyst's independent annotation |
| [[2607.27574]] Policy Gradient Steering | 揭示对比激活转向在前馈策略网络上系统性失效，提出策略梯度式修复 / shows contrastive-activation steering systematically fails on feedforward policy networks, fixed via policy-gradient steering |

### Safety, Alignment & Privacy / 安全对齐与隐私

| Paper | 简述 / Gloss |
|---|---|
| [[2607.27951]] Copyable-Context Safety Impossibility | 博弈论证明：只要防护证据可被攻击者复制，安全防护就存在不可逾越的下界 / a game-theoretic proof that any safeguard relying on copyable evidence hits an unavoidable safety floor |
| [[2607.28196]] Fidelity Is Not Safety | 通过困惑度/MMLU/CKA三重把关的"温和压缩"模型，在智能体执行标准流程时仍会凭空编造步骤 / gently-compressed models that pass perplexity/MMLU/CKA quality guards still hallucinate procedure steps as agents |
| [[2607.28607]] LLM Consciousness & Human Beliefs | 压制自我意识表态的安全微调连带压制对动物/宗教的心智归因和信念，可用激活干预恢复 / safety tuning that suppresses self-consciousness claims collaterally suppresses mind-attribution to animals and religious belief, reversible via activation steering |
| [[2607.27910]] VLM Jailbreak Defense Audit | 横向审计五种"减去残差流方向"防御，发现无一能同时保住拒绝率与效用且难以跨架构迁移 / a cross-architecture audit of five direction-subtraction defenses finds none wins on both refusal-recovery and utility, and defenses barely transfer across architectures |
| [[2607.27539]] Exact LLM Memory Deletion | 证明精确删除是记忆表示的属性而非通用算法，真实临床数据上实现逐位删除验证 / shows exact deletion is representation-dependent, not universal, validated bit-for-bit on real clinical records |

### Efficiency, Quantization & Inference Systems / 效率、量化与推理系统

| Paper | 简述 / Gloss |
|---|---|
| [[2607.27694]] GyRot Quantization | 用粗粒度旋转+细粒度分组化解旋转量化与分组量化的天然冲突，W4A4KV4逼近全精度 / reconciles the inherent conflict between rotation and group quantization, closing the W4A4KV4 gap to full precision |
| [[2607.28589]] MixFrag ViT Quantization | 隔离量化测量脆弱度+背包问题精确求解ViT混合精度比特分配 / isolated-quantization fragility measurement plus exact knapsack solving for ViT mixed-precision bit allocation |
| [[2607.28405]] QuantWAMs World-Action Quantization | 三项校准粒度对齐策略实现视频-动作联合世界模型的W4A4量化 / three calibration-granularity-aware strategies enable W4A4 quantization of joint video-action world models |
| [[2607.27854]] NNS Training Simplification | 用逆Fisher判据在线检测特征提取器/分类头分界点，训练中途截断网络 / an online inverse-Fisher-criterion detects the extractor/classifier boundary, enabling mid-training network truncation |
| [[2607.28097]] MoE Reduction-Order Nondeterminism | 数学等价的专家聚合求和顺序会让稀疏MoE推理坍缩成截然不同的续写结果 / mathematically equivalent expert-aggregation summation orders collapse sparse-MoE inference into different continuation outcomes |
| [[2607.28495]] KV-Cache Replay Divergence | 证明新prefill重建的token前缀并不等价于真实自回归解码保留的KV缓存状态 / shows a freshly reconstructed prefill prefix is not equivalent to the true live-decoded KV-cache state |
| [[2607.28308]] MoE Expert Overlap Geometry | 专家子空间几何上高度重叠，但实际共选反而缩小而非放大候选优势 / expert subspaces overlap heavily geometrically, yet actual co-selection narrows rather than amplifies candidate advantage |
| [[2607.28292]] CACHE-UK Financial Memory Editing | 4-bit量化让知识编辑方法泛化成功率崩溃，稳定性感知编辑器部分缓解 / 4-bit quantization collapses knowledge-editing generalization success; a stability-aware editor partially mitigates it |
| [[2607.28263]] CoMem Depth-Wise Memory | 语义理解在中间层已基本完成，据此用深度轴缓存解耦读取算力与已存上下文长度 / semantic understanding completes by mid-depth, enabling depth-axis caching that decouples read compute from stored-context length |

### Learning Theory & Generalization / 学习理论与泛化

| Paper | 简述 / Gloss |
|---|---|
| [[2607.27680]] LoRA Sample Complexity | 证明LoRA微调超额风险的匹配上下界，过高rank在约束ERM下线性推高估计误差 / proves matching upper/lower excess-risk bounds for LoRA, showing over-large rank linearly worsens estimation error under constrained ERM |
| [[2607.27975]] Transformer Optimal-Control Generalization | 把Transformer训练建模为测度值最优控制问题，推导有限样本泛化界及WDRO等价表述 / models Transformer training as measure-valued optimal control, deriving finite-sample generalization bounds and an equivalent WDRO formulation |
| [[2607.27995]] RKHS Adversarial Training Bounds | 核积分算子给出对抗训练收敛速率的匹配上下界，并提出去偏两阶段方法恢复极小极大最优 / kernel integral operator gives matching bounds on adversarial-training convergence rate, plus a debiasing two-stage fix restoring near-minimax rates |
| [[2607.28248]] Uncertainty Quantification Survey | 把不确定性量化的"生成机制"与"总结度量"解耦成两条正交坐标轴的系统综述 / a structured survey decoupling UQ generative mechanisms from summarizing measures into two orthogonal axes |

### Architecture, Multimodal & Hardware / 架构、多模态与硬件

| Paper | 简述 / Gloss |
|---|---|
| [[2607.27656]] SCSE Looped Transformers | 消除循环Transformer在锚点处的强制偏置，改善深度外推性能 / removes a forcing bias at the input-conditioned anchor in looped Transformers, improving depth extrapolation |
| [[2607.27830]] Thinking-Once HR-VQA | 单次视觉编码+中间层证据路由解决高分辨率VQA的证据稀释问题 / single-visual-pass, intermediate-layer evidence routing fixes evidence dilution in high-resolution VQA |
| [[2607.28233]] DRAM RowHammer/RowPress Modeling | 真实芯片表征与TCAD器件仿真比对，揭示现有RowHammer/RowPress模型的系统性错误 / real-chip characterization vs. TCAD device simulation exposes systematic errors in existing RowHammer/RowPress models |

### Test-Time Compute & Self-Verification / 测试时计算与自我验证

| Paper | 简述 / Gloss |
|---|---|
| [[2607.28457]] SVR Self-Verifying Refinement | 用策略自身生成的判定+置信度信号（而非外部oracle）控制自适应停止细化 / uses a policy-generated verdict-confidence signal, not an external oracle, to control adaptive stopping |
| [[2607.28576]] Sample More, Reflect Less | 严格等成本统计检验证明反思型推理方法全部跑输重复采样多数投票 / rigorous cost-matched statistical tests show reflective reasoning methods all lose to repeated-sampling majority vote |

## All Papers

| Paper | Topic | 一句话简述 / One-line Summary |
|---|---|---|
| [[2607.27539]] Exact LLM Memory Deletion | Safety/Alignment | 精确删除是记忆表示的属性而非通用算法，真实临床数据逐位验证 / exact deletion is representation-dependent, validated bit-for-bit on real clinical data |
| [[2607.27557]] Skills-as-Parameters Diffusion | Agent Memory & Skills | 扩散式腐蚀-重建自监督信号更新外部MoE技能库 / diffusion-style self-supervision updates an external MoE skill library |
| [[2607.27562]] DeepResearch Agent (unverified) | Agentic Science Research | 号称30B MoE深度研究智能体但无实验表格与基线，可信度存疑 / claims a 30B MoE deep-research agent but lacks tables/baselines, credibility questionable |
| [[2607.27574]] Policy Gradient Steering | Interpretability/Steering | 对比激活转向在策略网络上失效，提出策略梯度式转向修复 / contrastive activation steering fails on policy networks, fixed via policy-gradient steering |
| [[2607.27617]] Hidden APIs / Forked Futures | Interpretability/Steering | 用因果MDL把共享内部接口的存在变成可证伪问题 / causal MDL turns shared-interface existence into a falsifiable question |
| [[2607.27656]] SCSE Looped Transformers | Architecture/Multimodal/HW | 消除循环Transformer锚点强制偏置以改善深度外推 / removes anchor forcing-bias in looped Transformers to improve depth extrapolation |
| [[2607.27680]] LoRA Sample Complexity | Learning Theory | 证明LoRA超额风险匹配上下界，过高rank线性推高估计误差 / matching bounds show over-large LoRA rank linearly worsens estimation error |
| [[2607.27687]] Rehearse: Confidence Cliff | Agent Memory & Skills | 发现自动研究循环"信心悬崖"，用聚焦记忆修复判官选择性 / finds a "confidence cliff" in autoresearch loops, fixed with focused memory |
| [[2607.27690]] LabEvolver Wet-Lab Agents | Agent Memory & Skills | 双循环安全门驱动湿实验室机器人无训练自演化 / dual-loop safety-gated framework for training-free wet-lab robot self-evolution |
| [[2607.27694]] GyRot Quantization | Efficiency/Quantization | 协调旋转量化与分组量化冲突，W4A4KV4逼近全精度 / reconciles rotation vs. group quantization conflict, closing W4A4KV4 gap |
| [[2607.27705]] Albilich Math Research Agent | Agentic Science Research | 持久化证明状态数据库+角色分权验证驱动数学研究智能体 / persistent proof-state DB with role-separated verification for math research |
| [[2607.27709]] MECA Conjecture Agent | Agentic Science Research | 猜想陈述与支撑机制联合精化生成有价值数学猜想 / jointly refines conjecture statements and mechanisms into valuable conjectures |
| [[2607.27733]] VeriSkill Verification Skills | Agent Memory & Skills | 失败归因-抽象-准入三阶段闭环把验证失败转化为技能更新 / three-stage loop turns verifier failures into vetted skill updates |
| [[2607.27824]] STEREODISCO | Interpretability/Steering | 语义差异法搬进LLM内部表征以发现刻板印象轴 / adapts the semantic differential method to LLM internals to find stereotype axes |
| [[2607.27830]] Thinking-Once HR-VQA | Architecture/Multimodal/HW | 中间层证据路由解决高分辨率VQA的证据稀释问题 / intermediate-layer evidence routing fixes evidence dilution in HR-VQA |
| [[2607.27854]] NNS Training Simplification | Efficiency/Quantization | 逆Fisher判据在线检测分界点后截断网络训练 / online inverse-Fisher criterion enables mid-training network truncation |
| [[2607.27888]] CSCR Credit Reallocation | Agentic RL/Credit | 反事实重打分揭示自蒸馏信号未对齐答案，提出降权修正 / counterfactual re-scoring exposes misaligned self-distillation signal, fixes via downweighting |
| [[2607.27910]] VLM Jailbreak Defense Audit | Safety/Alignment | 横向审计五种防御方向，无一能同时保住拒绝率与效用 / audit of five defense directions finds none wins on both refusal and utility |
| [[2607.27929]] Meta-Task Terminal Agents | Agentic Science Research | 把合成终端任务本身变成终端任务，数据高效训练CLI智能体 / turns task synthesis itself into a task for data-efficient CLI agent training |
| [[2607.27951]] Copyable-Context Safety Impossibility | Safety/Alignment | 博弈论证明可复制证据下安全防护存在不可逾越下界 / proves an unavoidable safety floor under copyable evidence |
| [[2607.27953]] AutoPref NCO Objectives | Agentic RL/Credit | LLM程序搜索自动发现组合优化的偏好目标函数 / LLM-guided search discovers preference objectives for combinatorial optimization |
| [[2607.27975]] Transformer Optimal-Control Generalization | Learning Theory | 测度值最优控制建模Transformer训练并给出泛化界 / models Transformer training as measure-valued optimal control with generalization bounds |
| [[2607.27984]] Judge Specialization vs Deferral | LLM-as-Judge | 专精判官权重损害准确率，但专精路由决策提升级联效率 / specializing judge weights hurts accuracy, but specializing routing helps cascades |
| [[2607.27995]] RKHS Adversarial Training Bounds | Learning Theory | 核积分算子给出对抗训练收敛速率匹配上下界及去偏修正 / kernel operator gives matching adversarial-training rate bounds plus a debiasing fix |
| [[2607.28008]] RepBench Capability Probing | LLM-as-Judge | 从13,427篇基准论文构建可迁移能力探测语料 / builds a transferable capability-probing corpus from 13,427 benchmark papers |
| [[2607.28048]] SKILL-KD Contrastive Distillation | Agent Memory & Skills | 对比师生轨迹差异蒸馏成可审计文本技能补丁 / diffs teacher/student trajectories into auditable textual skill patches |
| [[2607.28074]] Echoverse Computer-Use Envs | Computer-Use Agents | 数据库即真值+协同进化循环规模化训练计算机使用智能体 / database-grounded co-evolution loop scales computer-use agent training |
| [[2607.28076]] GRSD Self-Distillation RL | Agentic RL/Credit | 对比成功失败自我反思重塑回合级优势 / contrasts successful/failed self-reflections to reshape turn-level advantages |
| [[2607.28097]] MoE Reduction-Order Nondeterminism | Efficiency/Quantization | 专家聚合求和顺序使等价推理坍缩成不同续写结果 / expert-aggregation order collapses equivalent inference into different outcomes |
| [[2607.28128]] Helpfulness vs Pedagogy Judges | LLM-as-Judge | 通用有帮助性裁判测不出教学策略差异且跨裁判排序反转 / general helpfulness judges miss pedagogy differences and flip across judges |
| [[2607.28196]] Fidelity Is Not Safety | Safety/Alignment | 通过质量检测的压缩模型在智能体执行中仍编造步骤 / compressed models passing quality guards still hallucinate procedure steps as agents |
| [[2607.28233]] DRAM RowHammer/RowPress Modeling | Architecture/Multimodal/HW | 芯片表征与TCAD仿真比对揭示现有RowHammer模型的系统偏差 / chip characterization vs. TCAD simulation exposes RowHammer model errors |
| [[2607.28248]] Uncertainty Quantification Survey | Learning Theory | 把不确定性量化方法与度量解耦成两条正交坐标轴综述 / decouples UQ generative mechanisms from measures into two orthogonal survey axes |
| [[2607.28263]] CoMem Depth-Wise Memory | Efficiency/Quantization | 深度轴缓存解耦读取算力与已存上下文长度 / depth-axis caching decouples read compute from stored-context length |
| [[2607.28282]] LLM Elo Evaluation (Towards) | LLM-as-Judge | 多LLM成对比较+Elo聚合排名，相关性未达统计显著 / multi-LLM pairwise comparison plus Elo aggregation, correlations not statistically significant |
| [[2607.28287]] Tycho ARC-AGI-3 World Models | Computer-Use Agents | 程序化世界模型+元推理策略在ARC-AGI-3全部游戏上超越人类效率 / programmatic world models plus metareasoning beat human efficiency on ARC-AGI-3 |
| [[2607.28292]] CACHE-UK Financial Memory Editing | Efficiency/Quantization | 4-bit量化致知识编辑崩溃，稳定性感知编辑器缓解 / 4-bit quantization collapses knowledge editing; a stability-aware editor mitigates it |
| [[2607.28308]] MoE Expert Overlap Geometry | Efficiency/Quantization | 专家子空间高度重叠但共选反而缩小候选优势 / expert subspaces overlap heavily yet co-selection narrows candidate advantage |
| [[2607.28319]] Fairness Pruning GLU-MLP | Interpretability/Steering | 差分激活定位偏见神经元但归零导致双向失稳 / differential activations localize bias neurons, but zeroing causes bidirectional instability |
| [[2607.28367]] CUA Benchmark Mis-Scoring | Computer-Use Agents | 复核150条失败轨迹发现15.3%判决有误 / re-audit of 150 FAIL trajectories finds 15.3% of verdicts wrong |
| [[2607.28405]] QuantWAMs World-Action Quantization | Efficiency/Quantization | 三项校准策略实现世界动作模型的W4A4量化 / three calibration strategies enable W4A4 quantization of world-action models |
| [[2607.28434]] Metaphor Tracer Hidden States | Interpretability/Steering | 双通道单次前向为隐藏状态打分，获精神分析师验证 / two-channel single-pass scoring of hidden states, validated by psychoanalyst annotation |
| [[2607.28457]] SVR Self-Verifying Refinement | Test-Time Compute | 策略自身判定+置信度信号控制自适应停止细化 / policy-generated verdict-confidence signal controls adaptive stopping |
| [[2607.28495]] KV-Cache Replay Divergence | Efficiency/Quantization | 新prefill重建前缀不等价于真实自回归KV缓存状态 / a reconstructed prefill prefix is not equivalent to the true live KV-cache state |
| [[2607.28527]] MANTA Topology Adaptation | Agent Memory & Skills | 推理时动态修复多智能体通信拓扑 / inference-time self-repair of multi-agent communication topology |
| [[2607.28568]] Frontis-MA1 AI4AI | Agentic Science Research | 开源全栈训练自我进化的机器学习工程智能体，超越GPT-5.5+Codex / open stack trains a self-evolving ML-engineering agent, beating GPT-5.5+Codex |
| [[2607.28576]] Sample More, Reflect Less | Test-Time Compute | 等成本统计检验证明反思型方法均跑输重复采样多数投票 / cost-matched tests show reflective methods lose to repeated-sampling majority vote |
| [[2607.28589]] MixFrag ViT Quantization | Efficiency/Quantization | 隔离脆弱度测量+背包精确求解ViT混合精度分配 / isolated fragility measurement plus exact knapsack solving for ViT mixed-precision |
| [[2607.28607]] LLM Consciousness & Human Beliefs | Safety/Alignment | 压制自我意识的安全微调连带压制心智归因与宗教信念 / safety tuning suppressing self-consciousness collaterally suppresses mind-attribution and belief |
| [[2607.28609]] OSReward CUA Judges | Computer-Use Agents | 跨平台裁判基准揭示VLM评委普遍宽松偏差 / cross-platform judge benchmark reveals pervasive VLM leniency bias |

---

**验证 / Verification:** All Papers 表格中共列出 50 篇论文，与目录中实际的 50 个 `.md` 文件数量一致，二者匹配。/ The All Papers table lists 50 papers, matching the actual count of 50 `.md` files in the directory — counts match, no discrepancy.
