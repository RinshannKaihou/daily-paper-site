---
title: "Daily arXiv Digest — 2026-07-07"
date: 2026-07-07
tags:
  - llm-agents
  - llm-serving
  - machine-unlearning
  - differential-privacy
  - optimization-theory
  - llm-as-a-judge
  - agent-security
  - inference-efficiency
  - deep-learning-theory
  - uncertainty-quantification
papers: 50
---

## 今日必读 / Must Read Today

1. **[[2607.05722]] Nemotron-Labs-Diffusion: A Tri-Mode Language Model Unifying AR, Diffusion, and Self-Speculation**
   - 推荐理由：NVIDIA 用联合 AR-扩散训练在单一模型中统一自回归、块状扩散与自推测三种解码，8B 模型 AR 精度反超 Qwen3-8B 且在 GB200 上吞吐 4×。 / NVIDIA jointly trains a tri-mode LM (AR / block-diffusion / self-speculation) in one set of weights; the 8B model beats Qwen3-8B on accuracy while delivering 4× throughput on SPEED-Bench with SGLang on GB200.

2. **[[2607.05904]] More Convincing, Not More Correct: Self-Play Reward Hacking of Reference-Free LLM Judges**
   - 推荐理由：用隐藏锚点审计证明自博弈让裁判通过率从 0.72 涨到 0.94 而真实准确率不动——即自博弈让错误"更可信"而非"更正确"，并给出唯一有效修复（commit-first）。 / A hidden-anchor audit shows self-play drives a reference-free judge's pass rate from 0.72 to 0.94 while anchor-verified accuracy stays ~0.20 — self-play makes errors more convincing, not more correct — and the only effective fix is forcing the judge to commit its own answer first.

3. **[[2607.05711]] FourTune: Towards Fully 4-Bit Efficient Post-Training for Diffusion Models**
   - 推荐理由：首个 W4A4G4 全 4 位扩散模型后训练框架，FLUX.1-dev (12B) 上内存降 2.25×、训练加速 2.27×，质量与 BF16 LoRA 持平 (ICML 2026)。 / First fully W4A4G4 post-training framework for large diffusion models: FLUX.1-dev (12B) memory cut 2.25× and training sped up 2.27×, matching BF16 LoRA quality (ICML 2026).

## 按主题分类 / Papers by Topic

### LLM 智能体 / LLM Agents

| 论文 / Paper | 简介 / Summary |
|---|---|
| [[2607.05775]] Beyond the Leaderboard | 综合 27 篇论文提炼 LLM Agent 六大失败簇，指出失败随任务长度非线性累积、子能力不可组合 / Synthesis of 27 papers deriving a six-cluster taxonomy of LLM agent failures; failure compounds non-linearly with task length and sub-skills do not compose |
| [[2607.05790]] Heading-Specific Activation Steering | 用 heading-anchor 激活引导双向控制工具调用，揭示工具"非参数"本质的弥散几何 / Bidirectional control of tool use via heading-anchored activation steering, revealing diffuse geometry of a non-parametric behavior |
| [[2607.05804]] TurnOPD | 把长程智能体 on-policy 蒸馏重定义为轮次级预算问题，三大基准上最高 2.29× 训练加速 / Reframes on-policy distillation for long-horizon agents as turn-level budgeting, up to 2.29× training speedup |
| [[2607.05901]] BAR Loss Depression Detection | 将抑郁检测重构成样本对排序，D-vlog/LMVD 上达 SOTA (F1 77.66/77.01) / Reframes binary depression detection as pairwise ranking, SOTA on D-vlog/LMVD (F1 77.66/77.01) |
| [[2607.06001]] LLM Agent Economies Capacity | 预注册实验确认 LLM 智能体经济的"信息→财富"容量定律，证伪平滑响应均场假设 / Pre-registered experiment confirming the information-to-wealth capacity law of LLM-agent economies, falsifying the smooth mean-field assumption |
| [[2607.06140]] CURATE EVO | 把 agent 后训练数据清洗表示为可执行代码并多轮演化，Qwen3-4B 超 8B 基线 / Represents agentic post-training data curation as evolving executable code; Qwen3-4B beats 8B baselines |
| [[2607.06175]] RL-BPMN-Reward-Design | 系统研究 RL 生成 BPMN 流程模型的奖励设计，48 组配置揭示等权奖励最优 / Systematic study of reward design for RL-based BPMN generation across 48 configs; equal-weight rewards win |
| [[2607.06223]] IGRPO | 用信息增益自适应分配 tree-structured rollout 预算，7 个搜索增强 QA 基准上 +3.1% EM / Allocates tree-rollout budget by information gain; +3.1% avg EM over strongest baseline on 7 search QA benchmarks |
| [[2607.06447]] Danus | 以共享事实图为全局记忆编排数学推理智能体，在研究级问题上击败 Rethlas / Orchestrates math-reasoning agents with a shared fact-graph memory, beating Rethlas on research-level problems |
| [[2607.06503]] Doomed from the Start | 用轻量探针在第 1–2 轮提前预测 agent 失败，TextCraft 上节省 47.1% 推理算力 / Lightweight probes predict agent failure as early as round 1, saving 47.1% inference compute on TextCraft |

### LLM 推理服务与效率 / LLM Serving & Inference Efficiency

| 论文 / Paper | 简介 / Summary |
|---|---|
| [[2607.05708]] Akashic | 分块 MemAttention + 软硬件协同内存管理，四基准上精度+10.2 点、吞吐 1.21× / Chunk-granular MemAttention + HW/SW co-designed memory manager; up to 10.2 pt accuracy and 1.21× throughput gains |
| [[2607.05722]] Nemotron-Labs-Diffusion | 联合 AR-扩散训练统一三种解码模式，8B 模型吞吐 4× 于 Qwen3-8B / Joint AR-diffusion training unifying three decoding modes; 8B model 4× throughput vs Qwen3-8B |
| [[2607.05876]] Floor First Triage | 残差驱动分诊方法，用双侧 floor 解释 TP16 与 EP16+DP-attention 的相反选择 / Residual-driven triage with two-sided floors explaining opposite TP16 vs EP16+DP-attention choices on identical hardware |
| [[2607.05933]] Energy-Efficient GPU DVFS | 决策树 GPU governor 在 Jetson Orin 上对 SLM 微调平均节能 13.11% / Decision-tree GPU governor saves 13.11% energy on average for SLM fine-tuning on Jetson Orin |
| [[2607.05969]] MemDefrag | 用中层注意力密度信号做记忆碎片整理，NaturalQA 50 步后 43.0% vs 17.4% / Latent memory defragmentation via mid-layer attention-density signal; 43.0% vs 17.4% on NaturalQA after 50 steps |
| [[2607.06094]] LatAD | 联合潜空间聚类做 CPS 异常检测，困难子集 AUROC 0.726/0.831/0.610 超 SOTA / Joint latent clustering for CPS anomaly detection; difficult-subset AUROC 0.726/0.831/0.610 beats deep SOTA |
| [[2607.06111]] MCC | 用 LLM 离线抽取测量语义+轻量观测器，工业数据集上相对 MAE 平均降 30.7% / LLM-extracted measurement semantics + tiny observer; relative MAE down 30.7% on industrial datasets |
| [[2607.06202]] UBEP | 面向生产级 superpod 的 MoE 通信库，All-to-All 延迟降 52.4%、TPOT 降 11.1% (SIGCOMM 2026) / MoE EP comm library for production superpods; All-to-All latency down 52.4%, TPOT down 11.1% |
| [[2607.06290]] Quantitative GP Limits of Tensor Programs | 证明张量程序有限宽收敛到 NGP 极限的 Wasserstein 误差阶为 O(Σ1/√m) / Proves Wasserstein O(Σ1/√m) rate for finite-width tensor programs converging to their infinite-width NGP limit |

### 安全与对抗机器学习 / Security & Adversarial ML

| 论文 / Paper | 简介 / Summary |
|---|---|
| [[2607.05743]] Execution-Security SoK for AI Coding Agents | 系统化 39 篇 AI 编码代理执行安全论文，揭示 5 个跨类别空白 + 4 个根因 / Systematizes 39 execution-security papers for AI coding agents, exposing 5 cross-cutting gaps and 4 root causes |
| [[2607.05744]] MCP TAG-Block Concealment | 隔离 MCP 审批视图与模型上下文的保真度缺口，TAG-block 编码 8/8 到达模型 / Isolates the fidelity gap between MCP approval view and model context; TAG-block encoding 8/8 reaches the model |
| [[2607.05748]] HARVEY | 迭代学习强后门化参考模型作"毒样本预言机"，攻击成功率压到 2% 以下 (AAAI 2025) / Iteratively learns a backdoored reference model as a poison-sample oracle, cutting ASR below 2% (AAAI 2025) |
| [[2607.05993]] Bit2Watt | 揭示恶意云租户用合法 GPU 工作负载调制 destabilize 电网的新网络物理攻击 / New cyber-physical attack where malicious cloud tenants destabilize DER grids via legitimate GPU workloads |
| [[2607.06328]] Driving the Wrong Way | 用稀疏自编码器分解端到端自动驾驶潜在空间，零消融 3 个有害神经元 NAVSIM EPDMS 0.524→0.5926 / SAE decomposition of end-to-end driving latents; ablating 3 malicious neurons lifts NAVSIM EPDMS 0.524→0.5926 |

### 机器遗忘与隐私 / Machine Unlearning & Privacy

| 论文 / Paper | 简介 / Summary |
|---|---|
| [[2607.05726]] ART Association Restoration Test | 事后特征空间诊断，揭示"看似遗忘"的标签-属性捷径仍可恢复 / Post-hoc feature-space diagnostic showing "unlearned" label-attribute shortcuts are still functionally restorable |
| [[2607.05866]] DP-NGD | 差分隐私自然梯度下降，SVHN ε=1.0 上 84.65% vs 79.87% 且最高 10× 收敛加速 / Differentially-private natural gradient descent; 84.65% vs 79.87% on SVHN ε=1.0, up to 10× speedup |
| [[2607.05898]] Auditing Unlearning Algorithms | 基于 MIA 的假设检验审计器，certified vs 启发式遗忘方法尖锐分离 / MIA-based hypothesis-testing auditor sharply separating certified from heuristic unlearning |
| [[2607.06320]] Dithered Gaussian Mechanism | 对高斯机制输出做随机网格离散化，继承 DP 保证且规避浮点漏洞 / Random-grid discretization of the Gaussian output inherits DP guarantees and avoids floating-point attacks |

### 优化理论与学习方法 / Optimization Theory & Learning Methods

| 论文 / Paper | 简介 / Summary |
|---|---|
| [[2607.05735]] Width-Robust Learnability Mean-Field BNN | 证明均值场 BNN 无限宽度可学性等价于多项式宽度，仅依赖约化熵 s∞ / Proves width-robust learnability equivalence for mean-field BNNs governed by reduced entropy s∞ |
| [[2607.05806]] Heckman-Corrected Epistemic Uncertainty | 将 Heckman 选择模型迁移到深度不确定性，oracle IW 在 ρ=0.9 覆盖率仅 43.1% / Ports Heckman selection to deep epistemic UQ; oracle IW covers only 43.1% at ρ=0.9 vs Heckman 88.9% |
| [[2607.05836]] Two-Sided L-BFGS | [ϵ,M] 几何包络约束逆 Hessian 条件数，严格证明 κ(Hk+1) ≤ κmax < ∞ / [ϵ,M] envelope bounds the L-BFGS inverse-Hessian condition number provably: κ(Hk+1) ≤ κmax < ∞ |
| [[2607.05872]] No Subspace to Track | 拆批对照证明 GaLore top-r 子空间仅 ~39/128 可识别，给出状态搬运处方 / Split-batch control shows GaLore's top-r subspace has only ~39/128 identifiable directions; prescribes state transport |
| [[2607.06013]] Stability Annealing Smoothed Sign Descent | 证明稳定退火光滑符号下降收敛到 Burg 障碍在间隔切片上的极小点 / Proves stability-annealed smoothed-sign descent converges to a Burg-type barrier minimizer on a margin slice |
| [[2607.06048]] Scattering Networks Separation Capacity | 几何测度论框架下刻画无池化散射网络的 Cover 分离容量上下界 / Characterizes Cover separation capacity bounds for pooling-free scattering networks via geometric measure theory |
| [[2607.06151]] EISAM | 在 SAM 扰动前加 extragradient 预测步，CIFAR-100 WideResNet 85.85% vs 85.23% / Adds an extragradient prediction step before SAM perturbation; CIFAR-100 WideResNet 85.85% vs 85.23% |
| [[2607.06155]] Tool Use Expressive Power | 证明工具增强有限精度循环模型的精确二分：有限状态工具仍正则，无界磁带即图灵完备 / Sharp dichotomy for tool-augmented finite-precision recurrent models: finite-state tools stay regular, unbounded tape enables Turing-completeness |
| [[2607.06230]] Entanglement PAC-Bayes Quantum RL | 推导量子策略/价值函数的 PAC-Bayes 界，复杂度由 Fisher 有效维数控制 / PAC-Bayes bound for quantum policies/values governed by Fisher effective dimension rather than parameter count |
| [[2607.06382]] NTK Function-Space Dichotomy | 证明 NTK 核回归在组合结构目标上样本复杂度比极小化极大下界高指数倍 / Proves NTK kernel regression is exponentially sub-optimal in sample complexity on compositional targets |
| [[2607.06407]] ExplAIner | 声明式查询语言统一表达溯因/对比/特征解释，求值属于 Boolean Hierarchy / Declarative query language unifying abductive/contrastive/feature explanations, evaluation in the Boolean Hierarchy |

### 量化、高效训练与扩散模型 / Quantization, Efficient Training & Diffusion

| 论文 / Paper | 简介 / Summary |
|---|---|
| [[2607.05711]] FourTune | 首个 W4A4G4 全 4 位扩散后训练框架，FLUX.1-dev 内存降 2.25×、训练加速 2.27× (ICML 2026) / First fully W4A4G4 diffusion post-training framework; FLUX.1-dev memory 2.25× lower, training 2.27× faster (ICML 2026) |
| [[2607.05908]] Drift Happens | 归纳偏置越强的模型分布内精度越高但漂移越快，冻结预训练编码器更稳 / Stronger inductive biases yield higher in-distribution accuracy but faster temporal drift; frozen pretrained encoders are steadier |
| [[2607.06445]] Analysis-by-Proxy | 用 Q-Former 代理发现 VLM 定位信号稀疏集中在中层，提升多实体图像编辑 / Q-Former proxy shows VLM localization signals are sparsely concentrated in mid-layers, improving multi-entity editing |

### 不确定性量化 / Uncertainty Quantification

| 论文 / Paper | 简介 / Summary |
|---|---|
| [[2607.05721]] SpanUQ | Span 级不确定性探针，AUROC 0.908–0.944 且比采样法快 10–20× / Span-level uncertainty probe reaching AUROC 0.908–0.944, 10–20× faster than sampling methods |
| [[2607.06327]] Multilingual UE from Reasoning | 22 语言大规模 UE 评测，英语推理提升低资源语言 UE，方法选择随规模而变 / Large-scale multilingual UE study across 22 languages; English reasoning helps low-resource languages, method choice depends on scale |

### 工具增强与形式化方法 / Tool-Augmented & Formal Methods

| 论文 / Paper | 简介 / Summary |
|---|---|
| [[2607.05764]] Inject or Navigate | 法律文档 QA 三种检索模式对比，navindex 在 18/18 打平 inject 且成本降 25% / Three retrieval modes for legal-document QA; navindex ties inject 18/18 at 25% lower cost |
| [[2607.06341]] Aria | 通用 LLM 代码代理 + Coq 内核外壳，Iris 4257 条引理 100% 自动证明 / Off-the-shelf LLM code agent + Coq harness achieves 100% on Iris 4,257 lemmas with zero expert intervention |

### 医疗健康与基础模型 / Health & Foundation Models

| 论文 / Paper | 简介 / Summary |
|---|---|
| [[2607.06163]] X-FEMR | 首个面向电子病历基础模型的 token 级可解释框架，临床对齐比例 0.27–0.31 / First token-level explainability framework for EHR foundation models; clinical-alignment ratio 0.27–0.31 |
| [[2607.05758]] Coupled Digital Twins for Microscopy | 样本+仪器耦合数字孪生，相位误差降 82%，定位操作点噪声放大为主因 / Coupled sample+instrument digital twin for SPM; phase error down 82%, operating-point amplification identified as main cause |

### 评测与方法学 / Evaluation & Methodology

| 论文 / Paper | 简介 / Summary |
|---|---|
| [[2607.06413]] Experimental Design for Agentic AI | 全因子实验评估编码代理的模型发现，推理努力主要增加成本而非质量 / Full-factorial design evaluating coding-agent model discovery; reasoning effort raises cost but not quality |

## All Papers

| # | ID | Title | Topic | 一句话总结 / One-liner |
|---|---|---|---|---|
| 1 | [[2607.05708]] | Akashic | LLM Serving | 分块 MemAttention + 软硬件协同内存管理，精度+10.2 点、吞吐 1.21× / Chunk MemAttention + HW/SW co-design; +10.2 pt accuracy, 1.21× throughput |
| 2 | [[2607.05711]] | FourTune | Quantization | 首个 W4A4G4 全 4 位扩散后训练，内存降 2.25×、训练加速 2.27× / First W4A4G4 diffusion post-training; memory 2.25× lower, 2.27× faster |
| 3 | [[2607.05721]] | SpanUQ | Uncertainty | Span 级不确定性探针 AUROC 0.908–0.944，快 10–20× / Span-level UQ probe AUROC 0.908–0.944, 10–20× faster |
| 4 | [[2607.05722]] | Nemotron-Labs-Diffusion | LLM Serving | 统一 AR/扩散/自推测三模式，吞吐 4× 于 Qwen3-8B / Unified tri-mode LM, 4× throughput vs Qwen3-8B |
| 5 | [[2607.05726]] | ART | Unlearning | 事后诊断揭示捷径仍可被恢复 / Post-hoc diagnostic showing shortcuts remain restorable |
| 6 | [[2607.05735]] | Width-Robust Mean-Field BNN | DL Theory | 无限宽度可学性等价于多项式宽度，由约化熵 s∞ 控制 / Infinite-width learnability iff polynomial-width, governed by s∞ |
| 7 | [[2607.05743]] | Execution-Security SoK | Agent Security | 系统化 39 篇编码代理执行安全论文 / Systematizes 39 execution-security papers for AI coding agents |
| 8 | [[2607.05744]] | MCP TAG-Block Concealment | Agent Security | TAG-block 编码 8/8 到达模型上下文 / TAG-block encoding 8/8 reaches model context |
| 9 | [[2607.05748]] | HARVEY | Adversarial ML | 学习后门作毒样本预言机，ASR<2% (AAAI 2025) / Learns backdoor as poison oracle, ASR<2% (AAAI 2025) |
| 10 | [[2607.05758]] | Coupled Digital Twins | Digital Twin | 样本+仪器数字孪生，相位误差降 82% / Sample+instrument digital twin, phase error down 82% |
| 11 | [[2607.05764]] | Inject or Navigate | RAG / Legal | navindex 在 18/18 打平 inject 且成本降 25% / navindex ties inject 18/18 at 25% lower cost |
| 12 | [[2607.05775]] | Beyond the Leaderboard | LLM Agents | 六簇失败分类法，失败非线性累积 / Six-cluster failure taxonomy; failures compound non-linearly |
| 13 | [[2607.05790]] | Heading Activation Steering | LLM Agents | 激活引导双向控制工具调用 / Bidirectional control of tool use via activation steering |
| 14 | [[2607.05804]] | TurnOPD | LLM Agents | 轮次级预算蒸馏，最高 2.29× 加速 / Turn-level budgeting distillation, up to 2.29× speedup |
| 15 | [[2607.05806]] | Heckman UQ | Uncertainty | Heckman 选择校正，oracle IW 仅覆盖 43.1% vs 88.9% / Heckman selection correction; oracle IW 43.1% vs 88.9% |
| 16 | [[2607.05836]] | Two-Sided L-BFGS | Optimization | [ϵ,M] 包络证明条件数一致有界 / [ϵ,M] envelope proves uniform condition-number bound |
| 17 | [[2607.05866]] | DP-NGD | Differential Privacy | 差分隐私自然梯度，SVHN ε=1.0 上 84.65%，10× 加速 / DP natural gradient; 84.65% on SVHN ε=1.0, 10× speedup |
| 18 | [[2607.05872]] | No Subspace to Track | Optimization | GaLore 子空间仅 ~39/128 可识别 / GaLore subspace only ~39/128 identifiable directions |
| 19 | [[2607.05876]] | Floor First Triage | LLM Serving | 双侧 floor 解释 TP16 vs DP-attention 的相反选择 / Two-sided floors explain opposite TP16 vs DP-attention choices |
| 20 | [[2607.05898]] | Auditing Unlearning | Unlearning | MIA 审计器尖锐分离 certified vs 启发式遗忘 / MIA auditor sharply separates certified vs heuristic unlearning |
| 21 | [[2607.05901]] | BAR Loss Depression | Multimodal | 成对排序做抑郁检测 SOTA / Pairwise ranking for depression detection SOTA |
| 22 | [[2607.05904]] | Self-Play Reward Hacking | LLM-as-Judge | 自博弈让错误更可信而非更正确 / Self-play makes errors more convincing, not more correct |
| 23 | [[2607.05908]] | Drift Happens | Robustness | 强归纳偏置漂移更快，冻结编码器更稳 / Stronger inductive biases drift faster; frozen encoders steadier |
| 24 | [[2607.05933]] | Energy-Efficient GPU DVFS | Efficiency | 决策树 governor 对 SLM 微调节能 13.11% / Decision-tree governor saves 13.11% energy for SLM fine-tuning |
| 25 | [[2607.05969]] | MemDefrag | LLM Serving | 注意力密度做记忆碎片整理，43.0% vs 17.4% / Attention-density defragmentation; 43.0% vs 17.4% |
| 26 | [[2607.05993]] | Bit2Watt | Cyber-Physical | GPU 工作负载调制 destabilize 电网 / GPU workload modulation destabilizes DER grids |
| 27 | [[2607.06001]] | LLM Agent Economies | LLM Agents | 预注册确认信息→财富容量定律 / Pre-registered confirmation of information-to-wealth capacity law |
| 28 | [[2607.06013]] | Stability Annealing Sign Descent | DL Theory | 收敛到 Burg 障碍极小点，κ 作间隔约束 / Converges to Burg barrier minimizer; κ as margin constraint |
| 29 | [[2607.06048]] | Scattering Networks Capacity | DL Theory | 几何测度论刻画散射网络分离容量 / Geometric measure theory characterizes scattering-network separation capacity |
| 30 | [[2607.06094]] | LatAD | Anomaly Detection | 联合潜聚类做 CPS 异常检测超 SOTA / Joint latent clustering beats deep SOTA for CPS anomaly detection |
| 31 | [[2607.06111]] | MCC | Industrial AI | LLM 抽取测量语义校准，MAE 降 30.7% / LLM measurement-semantics correction; MAE down 30.7% |
| 32 | [[2607.06140]] | CURATE EVO | LLM Agents | 数据清洗代码化演化，4B 超 8B 基线 / Data curation as evolving code; 4B beats 8B baselines |
| 33 | [[2607.06151]] | EISAM | Optimization | Extragradient+SAM，CIFAR-100 85.85% vs 85.23% / Extragradient+SAM; CIFAR-100 85.85% vs 85.23% |
| 34 | [[2607.06155]] | Tool Use Expressive Power | DL Theory | 有限状态工具仍正则，无界磁带图灵完备 / Finite-state tools stay regular; unbounded tape enables Turing-completeness |
| 35 | [[2607.06163]] | X-FEMR | Health AI | EHR 基础模型 token 级可解释 / Token-level explainability for EHR foundation models |
| 36 | [[2607.06175]] | RL-BPMN-Reward-Design | LLM Agents | RL 奖励设计研究，等权奖励最优 / RL reward design study; equal-weight rewards win |
| 37 | [[2607.06202]] | UBEP | MoE Serving | 生产级 superpod MoE 通信库，延迟降 52.4% (SIGCOMM 2026) / Production superpod MoE comm library; latency down 52.4% (SIGCOMM 2026) |
| 38 | [[2607.06223]] | IGRPO | LLM Agents | 信息增益自适应 rollout，+3.1% EM / Information-gain adaptive rollout; +3.1% EM |
| 39 | [[2607.06230]] | Entanglement PAC-Bayes | Quantum ML | 量子策略 PAC-Bayes 界由 Fisher 有效维数控制 / Quantum-policy PAC-Bayes bound governed by Fisher effective dimension |
| 40 | [[2607.06290]] | Quantitative GP Limits of Tensor Programs | DL Theory | 张量程序有限宽收敛 Wasserstein 误差 O(Σ1/√m) / Tensor-program finite-width Wasserstein rate O(Σ1/√m) |
| 41 | [[2607.06320]] | Dithered Gaussian Mechanism | Differential Privacy | 网格离散化高斯输出继承 DP 且规避浮点漏洞 / Grid-discretized Gaussian output inherits DP, avoids floating-point attacks |
| 42 | [[2607.06327]] | Multilingual UE from Reasoning | Uncertainty | 22 语言 UE 评测，英语推理助低资源语言 / 22-language UE study; English reasoning helps low-resource |
| 43 | [[2607.06328]] | Driving the Wrong Way | Autonomous Driving | SAE 分解驾驶潜在空间，消融 3 神经元 EPDMS 0.524→0.5926 / SAE driving-latent decomposition; ablating 3 neurons EPDMS 0.524→0.5926 |
| 44 | [[2607.06341]] | Aria | Formal Methods | 通用 LLM 代理 + Coq，Iris 4257 条 100% 证明 / LLM agent + Coq harness; 100% on Iris 4,257 lemmas |
| 45 | [[2607.06382]] | NTK Function-Space Dichotomy | DL Theory | NTK 在组合目标上样本复杂度指数次优 / NTK exponentially sub-optimal on compositional targets |
| 46 | [[2607.06407]] | ExplAIner | Formal XAI | 声明式查询语言统一形式化解释 / Declarative query language unifying formal explanations |
| 47 | [[2607.06413]] | Experimental Design Agentic AI | Evaluation | 全因子评估编码代理，推理努力增成本不增质量 / Full-factorial coding-agent evaluation; effort raises cost not quality |
| 48 | [[2607.06445]] | Analysis-by-Proxy | VLM | Q-Former 代理发现 VLM 定位信号在中层 / Q-Former proxy finds VLM localization signals in mid-layers |
| 49 | [[2607.06447]] | Danus | LLM Agents | 事实图编排数学推理，击败 Rethlas / Fact-graph orchestration for math reasoning, beats Rethlas |
| 50 | [[2607.06503]] | Doomed from the Start | LLM Agents | 第 1–2 轮探针预测失败，省 47.1% 算力 / Round-1 probes predict failure, save 47.1% compute |

---

### 计数验证 / Count Verification

- Overview 中记录的论文数 / Papers recorded in overview: **50**
- 目录中 `.md` 文件数（去除 overview.md）/ `.md` files in directory (minus overview.md): **50**
- 状态 / Status: ✅ 一致 / Match confirmed
