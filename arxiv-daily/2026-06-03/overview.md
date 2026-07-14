---
title: "Daily Paper Overview - 2026-06-03"
date: 2026-06-03
tags: [daily-overview, arxiv, llm, ai]
papers: 50
---

# Daily Paper Overview — 2026-06-03

## 今日必读 / Must Read Today

### 1. [[2606.03217]] An Asymptotic Theory of Chain-of-Thought in In-Context Learning

**一句话总结：** 本文通过随机矩阵理论的高维渐近分析，在一个可解析的线性回归上下文学习模型中，精确刻画了思维链（CoT）推理深度对泛化误差的影响，揭示了指数提升、多项式提升、饱和与过度思考四种相变区域，并证明了更深的推理仅在预训练数据充足且上下文信息丰富时才有效。

**TL;DR:** This paper uses high-dimensional random matrix theory to derive an exact asymptotic characterization of how chain-of-thought (CoT) reasoning depth affects generalization in a solvable linear regression in-context learning model, revealing four distinct phase-transition regimes—exponential improvement, polynomial improvement, saturation, and overthinking—and showing that deeper reasoning is beneficial only when pretraining is sufficiently rich and in-context information is abundant.

---

### 2. [[2606.03398]] Causal Evidence of Stack Representations in Modeling Counter Langua...

**一句话总结：** 本文在仅含单层的编码器-解码器Transformer上，通过线性探测提取Shuffle-k语言栈深度的主表征方向，并证明消融该方向会导致序列准确率断崖式崩溃至接近0%，而随机方向消融毫无影响，从而为栈表征的因果必要性提供了决定性证据。

**TL;DR:** Using a single-layer encoder-only transformer trained on counter languages (Dyck-1 and Shuffle-k), the author trains linear probes to extract principal stack-depth representation directions from hidden states via SVD, then ablates these directions at inference time. Targeted ablation causes sequential accuracy to collapse to near 0%, while random-direction ablation leaves performance intact, providing decisive causal evidence that stack representations are not merely learned but are necessary for the model's computation.

---

### 3. [[2606.03785]] Backdoor Unlearning Generalization: A Path Toward the Removal of Un...

**一句话总结：** 该研究表明，在大型语言模型中通过持续预训练"遗忘"单一后门触发器时，这种去后门化过程会跨触发器泛化，显著抑制模型中其他从未被显式针对的后门行为，并提出了跨激活偏移距离（CASD）指标来量化不同后门移除训练所诱导的表征变化相似性。

**TL;DR:** The authors demonstrate that unlearning a single backdoor trigger in LLMs generalizes across backdoors — suppressing other co-existing backdoors that were never explicitly targeted — and introduce Cross Activation Shift Distance (CASD) to quantify when different removal procedures induce sufficiently similar representational shifts for this transfer to occur.

---

## 按主题分类 / Papers by Topic

### 大模型推理与系统优化 / LLM Inference & System Optimization

| Paper | Summary (Chinese / English) |
|-------|-----------------------------|
| [[2605.29135]] Rotary GPU: Exploring Local Execution Paths for La... | Rotary GPU 提出了一种基于"旋转式"加速器驻留管理的执行策略，使得 350 亿参数的 Qwen3.6 MoE 模型能在仅 8 GB 显存的消费级笔记本... / Rotary GPU introduces a rotary-guided accelerator residency management approach ... |
| [[2605.30571]] Memory-Bound but Not Bandwidth-Limited: The Physic... | 该论文通过44个跨GPU测量单元证明，物理AI场景下的batch-1 LLM解码虽被归类为内存带宽受限，但在H100等高端GPU上实际受限于每核CPU启动开销而... / A rigorous 44-cell cross-GPU measurement study shows that batch-1 LLM decode for... |
| [[2605.31035]] MixFP4: Enhancing NVFP4 with Adaptive FP4/INT4 Blo... | MixFP4 通过在块级别自适应地在两种 FP4 微格式（E2M1 和 E1M2）之间进行选择，在不增加额外元数据开销的情况下提升了 NVFP4 的量化鲁棒性，... / MixFP4 enhances NVFP4 by adaptively selecting between E2M1 and E1M2 FP4 micro-fo... |
| [[2606.00365]] SPARQLe: Sub-Precision Activation Representation f... | SPARQLe 通过将 8-bit 激活张量分解为密集的 4-bit 低位（LSB4）张量和稀疏的 4-bit 高位（MSB4）张量（配合精度位图压缩），并利用... / SPARQLe is a hardware-software co-design framework that exploits sub-precision a... |
| [[2606.01751]] SparseX: Efficient Segment-Level KV Cache Sharing ... | SparseX 是一种面向交错 LLM 服务场景的段级 KV Cache 共享方法，通过利用非复用段自然产生的 Sparse-Q 索引识别需要修正的关键 tok... / SparseX is a segment-level KV Cache sharing method for interleaved LLM serving t... |
| [[2606.02964]] Multi-Segment Attention: Enabling Efficient KV-Cac... | AsymCache 提出 Multi-Segment Attention (MSA) 机制与计算延迟感知的 KV cache 驱逐策略，通过将缓存块保留决策与 ... / AsymCache introduces Multi-Segment Attention (MSA) and a computation-latency-awa... |
| [[2606.02982]] DriftSched: Adaptive QoS-Aware Scheduling under Ru... | 本文提出 DriftSched，一种针对多租户 GPU 上大语言模型推理服务的自适应 QoS 感知调度框架，通过运行时反馈驱动的指数移动平均（EMA）偏差修正机... / This paper presents DriftSched, an adaptive QoS-aware scheduling framework for m... |
| [[2606.03458]] KVarN: Variance-Normalized KV-Cache Quantization M... | KVarN 提出了一种无需校准的 KV-cache 量化方法，通过 Hadamard 旋转和双轴方差归一化来修正异常的 token 尺度误差，从而显著减少自回归... / KVarN introduces a calibration-free KV-cache quantizer that applies Hadamard rot... |
| [[2606.03739]] Entropy Gate: Entropy Quenching for Near-Lossless ... | 本文提出 Entropy Gate，一种受统计力学启发的 token 压缩框架，通过多因子信息能量（统计、结构、位置）对 token 赋权，并以自适应淬火调度逐... / This paper introduces Entropy Gate, a thermodynamics-inspired token compression ... |

### 神经网络理论与可解释性 / Neural Network Theory & Interpretability

| Paper | Summary (Chinese / English) |
|-------|-----------------------------|
| [[2606.00157]] Interpreting FCDNNs via RG on Exponential Family | 本文将统计物理中的重整化群（RG）方法与全连接深度神经网络（FCDNN）的训练过程建立严格的数学对应关系，针对具有偶次多项式哈密顿量的指数族连续数据，证明了当网... / This paper rigorously generalizes a correspondence between the renormalization g... |
| [[2606.02993]] Neural Networks Provably Learn Spectral Representa... | 该研究通过将投影梯度流提升到傅里叶域，严格证明了在任意有限群上的群合成任务中，两层神经网络几乎必然收敛到单个不可约表示，并在跨层傅里叶系数间实现秩一旋转对齐，从... / By lifting projected gradient flow to the Fourier domain, the authors prove that... |
| [[2606.03217]] An Asymptotic Theory of Chain-of-Thought in In-Con... | 本文通过随机矩阵理论的高维渐近分析，在一个可解析的线性回归上下文学习模型中，精确刻画了思维链（CoT）推理深度对泛化误差的影响，揭示了指数提升、多项式提升、饱和... / This paper uses high-dimensional random matrix theory to derive an exact asympto... |
| [[2606.03280]] A Negative Result on Cross-Model Activation Transf... | 本文在Pythia-160M到Pythia-410M的多跳推理设置中测试了跨模型激活传递，发现尽管线性翻译层在归一化空间中的对齐度极高（余弦相似度≈0.97），... / This paper tests cross-model activation transfer from Pythia-160M to Pythia-410M... |
| [[2606.03398]] Causal Evidence of Stack Representations in Modeli... | 本文在仅含单层的编码器-解码器Transformer上，通过线性探测提取Shuffle-k语言栈深度的主表征方向，并证明消融该方向会导致序列准确率断崖式崩溃至接... / Using a single-layer encoder-only transformer trained on counter languages (Dyck... |
| [[2606.03483]] Analyzing Stream Collapse in Hyper-Connections: Fr... | 本文诊断了Hyper-Connections中多流残差路径出现的“流崩溃”现象——残差混合矩阵趋近单位阵、信号与可解释特征集中于单一主导流，并提出仅增加nd参数... / This paper diagnoses a "stream collapse" failure mode in Hyper-Connections (HC),... |
| [[2606.03645]] The Shape of Addition: Geometric Structures of Ari... | 该研究通过对多操作数加法任务中LLM残差流激活的逐位分析，发现了"等原始和轨迹"（IRST）这一层次化几何流形结构，并提出了噪声量化模型，将算术错误重新定义为连... / By analyzing residual-stream activations during multi-operand addition digit-by-... |
| [[2606.03712]] When Graph Tokens Sink: A Mechanistic Analysis of ... | 本文通过对LLaGA和TEA-GLM两种代表性图语言模型的机制分析，发现图token中存在"图sink token"现象——它们在特定隐藏维度上产生极大的激活值... / This paper presents a mechanistic analysis of two representative Graph Language ... |
| [[2606.03780]] Expert-Aware Causal Tracing of Factual Recall in S... | 本文将因果追踪从密集Transformer扩展到稀疏MoE模型，提出两阶段专家感知追踪协议：在Qwen3-30B-A3B中事实回忆可精确定位到第44层的单个专家... / This paper extends causal tracing of factual recall from dense transformers to s... |
| [[2606.03883]] Reasoning Structure of Large Language Models | 本文构建了一套包含21种逻辑谜题的可扩展基准测试，并提出将大型推理模型的非结构化思维链转换为可验证的原子声明依赖图（DAG），基于吸收马尔可夫链模型定义了推理效... / This paper builds a scalable benchmark of 21 grid logic puzzles and proposes con... |
| [[2606.03899]] Denoise First, Orthogonalize Later: Understanding ... | 本文严格证明了 Muon 优化器中动量的本质是谱滤波器——在正交化之前通过指数移动平均抑制梯度噪声、保留相干信号，从而扩大谱间隙并稳定奇异子空间，且"先降噪再正... / This paper rigorously proves that momentum in the Muon optimizer acts as a spect... |
| [[2606.03990]] Neuron Populations Exhibit Divergent Selectivity w... | 该研究通过对语言模型（至30B）和视觉模型（至5B）的跨模型神经元匹配分析，发现"罗塞塔神经元"（Rosetta Neurons）的数量随模型规模呈次线性幂律增... / This paper establishes that Rosetta Neurons—units with recurrent activation patt... |

### 安全、评估与可信AI / Safety, Evaluation & Trustworthy AI

| Paper | Summary (Chinese / English) |
|-------|-----------------------------|
| [[2606.03291]] Multilingual Unlearning in LLMs: Transfer, Dynamic... | 本文将TOFU基准扩展至英、中、德、俄、土五种语言，系统揭示了大模型多语言知识遗忘的跨语言迁移规律（与文字系统和语系相似性高度相关），并通过逐层表征分析与推理时... / This paper extends the TOFU benchmark to five languages (English, Chinese, Germa... |
| [[2606.03305]] The Reliability Gap in Benchmark Auditing: Distrib... | 本文通过在27个多家族多规模模型（含前沿工业模型）上进行335次评估，系统检验了LLM Dataset Inference、Post-Hoc Dataset I... / This paper systematically evaluates three leading benchmark contamination detect... |
| [[2606.03437]] Large Language Models Are Overconfident in Their O... | 本文首次将指令微调后的校准退化与聊天模板效应解耦，发现对话式LLM存在"所有权偏差"——模型对自己生成的答案比对用户提供的相同答案置信度高最多26%，并提出一种... / This paper decouples the effects of instruction tuning and chat templates on LLM... |
| [[2606.03648]] Safety Measurements for Fine-tuned LLMs Should be ... | 本文通过对四种开源LLM在五个数据集上的系统实验，证明安全评估必须锚定在具体能力目标上，并揭示微调模型会对安全提示产生不连贯输出，导致自动安全评判器将其误判为有... / Through systematic experiments on four open-source LLMs across five fine-tuning ... |
| [[2606.03785]] Backdoor Unlearning Generalization: A Path Toward ... | 该研究表明，在大型语言模型中通过持续预训练"遗忘"单一后门触发器时，这种去后门化过程会跨触发器泛化，显著抑制模型中其他从未被显式针对的后门行为，并提出了跨激活偏... / The authors demonstrate that unlearning a single backdoor trigger in LLMs genera... |
| [[2606.03793]] Exploring Adversarial Robustness and Safety Alignm... | 该研究通过对12种语言下三种代表性开源MLLM（PALO、PARROT、Qwen3-VL）的系统评估，发现对抗图像扰动具有强跨语言可迁移性，并揭示了浅层多语言适... / This paper systematically evaluates adversarial robustness and multimodal safety... |
| [[2606.03846]] Clustered Self-Assessment: A Simple yet Effective ... | 本文提出了一种基于语义聚类的自评估方法，通过NLI模型将LLM采样生成结果聚类后转化为结构化的多选题选项，再利用模型对选项标签的Softmax概率作为置信度估计... / This paper proposes Clustered Self-Assessment, a method that groups sampled LLM ... |
| [[2606.03969]] Quantifying Faithful Confidence Expression in Larg... | 本文提出了首个系统量化大型推理模型（LRMs）忠实校准（FC）的框架，基于token概率、隐藏状态和采样一致性三种内部不确定性估计器，配合前缀条件采样控制推理迹... / This paper introduces the first systematic framework to quantify Faithful Calibr... |

### 训练优化与算法 / Training Optimization & Algorithms

| Paper | Summary (Chinese / English) |
|-------|-----------------------------|
| [[2606.00419]] Parameter-Free and Group Conditional Online Confor... | 本文提出POGO算法，通过将群组条件在线共形预测转化为k个并行财富过程的 universal portfolio 优化问题，首次实现了无需学习率调参的群组条件覆... / This paper proposes POGO, the first parameter-free algorithm for group-condition... |
| [[2606.01521]] Fast Generalization after Interpolation via Critic... | 本文提出了一种名为 GROKtimizer 的双阶段优化器：第一阶段关闭权重衰减以快速达到插值（零训练误差），第二阶段切换到临界阻尼动量（CDM）并结合权重衰减... / This paper proposes GROKtimizer, a biphasic optimizer that first disables weight... |
| [[2606.02008]] Provable Data Scaling Law for Meta Learning via Co... | 本文提出"复杂度最小化"元表示学习框架，通过Lepski自适应方法估计各源域的最优模型复杂度并以最坏情况最小化为目标学习特征提取器，首次从端到端理论上证明了元训... / This paper introduces complexity minimization, a meta-representation learning fr... |
| [[2606.02740]] ScoreStop: Gradient-based early stopping using fun... | 本文提出 ScoreStop，一种基于功能性得分检验的梯度早停规则，将每次迭代中的停止决策转化为对"当前预测器是否为总体风险最小化器"的假设检验，该统计量在更新... / This paper proposes ScoreStop, a gradient-based early stopping rule for gradient... |
| [[2606.03498]] Demystifying Pipeline Parallelism: First Theory fo... | 本文首次为 PipeDream 风格的流水线并行训练建立了非凸收敛理论，提出随机化抽象 RPD 并证明其延迟随阶段数 S 以 Θ(S⁴/K) 恶化，同时通过实验... / This paper provides the first clean nonconvex convergence guarantee for a PipeDr... |
| [[2606.03532]] When Should the Teacher Move? Temporal Coupling an... | 本文系统研究了自 on-policy 蒸馏中教师-学生的时间耦合，发现隔离期（教师完全冻结）是稳定学习的关键结构特性，并提出 Consolidation-Gat... / This paper systematically studies temporal coupling in self on-policy distillati... |
| [[2606.03608]] Exploiting Verification-Generation Gap: Test-Time ... | 本文提出TTRL-CoCoV框架，利用"验证能力领先于生成能力"的核心洞察，通过置信度条件化的验证机制在无需标签的测试时强化学习中同时提升Pass@1和Pass... / This paper proposes TTRL-CoCoV, a confidence-adaptive test-time RL framework tha... |
| [[2606.03650]] CoEval: Ranking Language Models for Custom Tasks W... | CoEval 是一个开源框架，仅通过任务描述即可自动生成无标签、零污染的属性分层评测数据，并利用跨厂商的裁判模型 ensemble 对候选模型进行可靠排序，在无... / CoEval is an open-source framework that generates fresh, attribute-stratified, c... |

### 硬件架构与高效计算 / Hardware Architecture & Efficient Computing

| Paper | Summary (Chinese / English) |
|-------|-----------------------------|
| [[2606.00486]] Dead on Arrival: Characterizing and Protecting Aga... | 本文在24个GPU工作负载上系统表征了"死条目"L2 TLB缺失现象（recently-evicted translation被立即重新页表遍历），发现其可占敏... / This paper characterizes "dead-entry" L2 TLB misses in GPUs — recently evicted t... |
| [[2606.01381]] Formal Verification of Secure Encrypted Virtualiza... | 本文提出了首个针对 AMD SEV 虚拟机可信执行环境的完整形式化验证框架，使用 Rosette 语言建立设计级与属性级抽象模型，并通过符号执行结合 Z3 SM... / This paper introduces the first comprehensive formal verification framework for ... |
| [[2606.02781]] CRAM-ER: Error-Resilient Spintronic Computational ... | 本文提出了一种抗错误的自旋电子学计算随机存取存储器架构 CRAM-ER，通过混合自旋电子-CRAM + CMOS 加法树架构以及错误感知微调策略，在实现近无损 ... / This paper proposes CRAM-ER, an error-resilient spintronic Computational RAM arc... |
| [[2606.02836]] Fast Transformer Inference on ARM-Based HMPSoCs | 本文通过在 ARM Compute Library 中实现 Transformer 专用内核（NEON/OpenCL），并基于微基准分析发现不同层的 CPU/G... / This paper extends the ARM Compute Library with transformer-specific kernels (NE... |

### 科学计算、统计方法与多模态智能 / Scientific Computing, Statistics & Multimodal Intelligence

| Paper | Summary (Chinese / English) |
|-------|-----------------------------|
| [[2606.00643]] Taming the Loss Landscape of PINNs with Noisy Feyn... | 本文提出 FK-PINNs，通过在标准 PINN 损失中加入少量基于 Feynman–Kac 蒙特卡洛估计的点监督项，从算子预条件化的角度证明了该方法能将损失景... / This paper introduces FK-PINNs, which augment standard Physics-Informed Neural N... |
| [[2606.02115]] Error Bounds for a Diffusion Model-Based Drift Est... | 本文首次为基于条件扩散模型的SDE漂移估计器推导了显式的风险上界，将时间平均均方误差分解为欧拉-丸山离散化、分数/去噪器近似、噪声初始化和采样方差四个部分，并给... / This paper derives the first explicit risk bound for a conditional diffusion mod... |
| [[2606.02589]] Rashomon-Seeded Annealing for Robust Bayesian Infe... | 本文提出 Rashomon-seeded annealing 框架，将 Rashomon 集合（高后验证据模型集合）作为退火重要性采样（AIS）的"热启动"，在... / This paper proposes Rashomon-seeded annealing, a framework that repurposes Rasho... |
| [[2606.03245]] Hierarchies of Calibration: Classification meets R... | 本文在统一的预测空间框架下，系统建立了分类与回归任务中概率校准概念的严格层级关系，引入了模态校准等新概念，并证明了双PIT校准与现有离散校准概念在逻辑上的独立性... / This paper reviews, extends, and bridges notions of calibration for classificati... |
| [[2606.03318]] Beyond Ideal Instruction: A Comprehensive Framewor... | 本文提出了 RUT-Bench，一个包含 1638 个测试样本、覆盖 59 个可执行环境和 11 个真实领域的大语言模型工具调用评估基准，系统性地引入七种用户行... / This paper introduces RUT-Bench, a benchmark with 1,638 test samples across 59 e... |
| [[2606.03467]] StepFinder: A Temporal Semantic Framework for Fail... | StepFinder 是一个轻量级的多智能体系统故障归因框架，通过 Qwen3 Embedding 将执行日志编码为时序语义序列，再用 BiLSTM、Agent... / StepFinder is a lightweight failure attribution framework for multi-agent system... |
| [[2606.03569]] When Attention Collapses: Stage-Aware Visual Token... | 本文提出 Structure-to-Semantics (STS) 两阶段视觉 token 剪枝框架，通过第一阶段基于势能最小化的排斥采样保留空间结构多样性，第... / This paper introduces STS, a training-free two-stage visual token pruning framew... |
| [[2606.03602]] CauTion: Knowing When to Trust LLMs for Ensemble C... | CauTion 通过三阶段框架（算法集成共识投票、无标注信任校准仲裁、循环修复）将 LLM 领域知识可靠地融入统计因果发现，仅在算法证据不可靠的争议边上调用 L... / CauTion is a three-stage framework that reliably integrates LLM domain knowledge... |
| [[2606.03730]] Beyond False Stability: High-Noise Drift Gating fo... | 该论文通过系统分析CLIP视觉表征在不同强度随机扰动下的漂移行为，发现对抗样本在弱噪声下呈现虚假稳定性、但在高噪声下显著比干净样本更不稳定这一被忽视的噪声-区域... / This paper systematically analyzes how CLIP's visual representations respond to ... |

## All Papers

| # | Paper | Summary |
|---|-------|---------|
| 1 | [[2605.29135]] Rotary GPU: Exploring Local Execution Paths f... | Rotary GPU 提出了一种基于"旋转式"加速器驻留管理的执行策略，使得 350 亿参数的 Qwen3.6 MoE 模型能在仅 8 GB... / Rotary GPU introduces a rotary-guided accelerator residency management... |
| 2 | [[2605.30571]] Memory-Bound but Not Bandwidth-Limited: The P... | 该论文通过44个跨GPU测量单元证明，物理AI场景下的batch-1 LLM解码虽被归类为内存带宽受限，但在H100等高端GPU上实际受限于... / A rigorous 44-cell cross-GPU measurement study shows that batch-1 LLM ... |
| 3 | [[2605.31035]] MixFP4: Enhancing NVFP4 with Adaptive FP4/INT... | MixFP4 通过在块级别自适应地在两种 FP4 微格式（E2M1 和 E1M2）之间进行选择，在不增加额外元数据开销的情况下提升了 NVF... / MixFP4 enhances NVFP4 by adaptively selecting between E2M1 and E1M2 FP... |
| 4 | [[2606.00157]] Interpreting FCDNNs via RG on Exponential Fam... | 本文将统计物理中的重整化群（RG）方法与全连接深度神经网络（FCDNN）的训练过程建立严格的数学对应关系，针对具有偶次多项式哈密顿量的指数族... / This paper rigorously generalizes a correspondence between the renorma... |
| 5 | [[2606.00365]] SPARQLe: Sub-Precision Activation Representat... | SPARQLe 通过将 8-bit 激活张量分解为密集的 4-bit 低位（LSB4）张量和稀疏的 4-bit 高位（MSB4）张量（配合精... / SPARQLe is a hardware-software co-design framework that exploits sub-p... |
| 6 | [[2606.00419]] Parameter-Free and Group Conditional Online C... | 本文提出POGO算法，通过将群组条件在线共形预测转化为k个并行财富过程的 universal portfolio 优化问题，首次实现了无需学... / This paper proposes POGO, the first parameter-free algorithm for group... |
| 7 | [[2606.00486]] Dead on Arrival: Characterizing and Protectin... | 本文在24个GPU工作负载上系统表征了"死条目"L2 TLB缺失现象（recently-evicted translation被立即重新页表... / This paper characterizes "dead-entry" L2 TLB misses in GPUs — recently... |
| 8 | [[2606.00643]] Taming the Loss Landscape of PINNs with Noisy... | 本文提出 FK-PINNs，通过在标准 PINN 损失中加入少量基于 Feynman–Kac 蒙特卡洛估计的点监督项，从算子预条件化的角度证... / This paper introduces FK-PINNs, which augment standard Physics-Informe... |
| 9 | [[2606.01381]] Formal Verification of Secure Encrypted Virtu... | 本文提出了首个针对 AMD SEV 虚拟机可信执行环境的完整形式化验证框架，使用 Rosette 语言建立设计级与属性级抽象模型，并通过符号... / This paper introduces the first comprehensive formal verification fram... |
| 10 | [[2606.01521]] Fast Generalization after Interpolation via C... | 本文提出了一种名为 GROKtimizer 的双阶段优化器：第一阶段关闭权重衰减以快速达到插值（零训练误差），第二阶段切换到临界阻尼动量（C... / This paper proposes GROKtimizer, a biphasic optimizer that first disab... |
| 11 | [[2606.01751]] SparseX: Efficient Segment-Level KV Cache Sha... | SparseX 是一种面向交错 LLM 服务场景的段级 KV Cache 共享方法，通过利用非复用段自然产生的 Sparse-Q 索引识别需... / SparseX is a segment-level KV Cache sharing method for interleaved LLM... |
| 12 | [[2606.02008]] Provable Data Scaling Law for Meta Learning v... | 本文提出"复杂度最小化"元表示学习框架，通过Lepski自适应方法估计各源域的最优模型复杂度并以最坏情况最小化为目标学习特征提取器，首次从端... / This paper introduces complexity minimization, a meta-representation l... |
| 13 | [[2606.02115]] Error Bounds for a Diffusion Model-Based Drif... | 本文首次为基于条件扩散模型的SDE漂移估计器推导了显式的风险上界，将时间平均均方误差分解为欧拉-丸山离散化、分数/去噪器近似、噪声初始化和采... / This paper derives the first explicit risk bound for a conditional dif... |
| 14 | [[2606.02589]] Rashomon-Seeded Annealing for Robust Bayesian... | 本文提出 Rashomon-seeded annealing 框架，将 Rashomon 集合（高后验证据模型集合）作为退火重要性采样（AI... / This paper proposes Rashomon-seeded annealing, a framework that repurp... |
| 15 | [[2606.02740]] ScoreStop: Gradient-based early stopping usin... | 本文提出 ScoreStop，一种基于功能性得分检验的梯度早停规则，将每次迭代中的停止决策转化为对"当前预测器是否为总体风险最小化器"的假设... / This paper proposes ScoreStop, a gradient-based early stopping rule fo... |
| 16 | [[2606.02781]] CRAM-ER: Error-Resilient Spintronic Computati... | 本文提出了一种抗错误的自旋电子学计算随机存取存储器架构 CRAM-ER，通过混合自旋电子-CRAM + CMOS 加法树架构以及错误感知微调... / This paper proposes CRAM-ER, an error-resilient spintronic Computation... |
| 17 | [[2606.02836]] Fast Transformer Inference on ARM-Based HMPSo... | 本文通过在 ARM Compute Library 中实现 Transformer 专用内核（NEON/OpenCL），并基于微基准分析发现... / This paper extends the ARM Compute Library with transformer-specific k... |
| 18 | [[2606.02964]] Multi-Segment Attention: Enabling Efficient K... | AsymCache 提出 Multi-Segment Attention (MSA) 机制与计算延迟感知的 KV cache 驱逐策略，通过... / AsymCache introduces Multi-Segment Attention (MSA) and a computation-l... |
| 19 | [[2606.02982]] DriftSched: Adaptive QoS-Aware Scheduling und... | 本文提出 DriftSched，一种针对多租户 GPU 上大语言模型推理服务的自适应 QoS 感知调度框架，通过运行时反馈驱动的指数移动平均... / This paper presents DriftSched, an adaptive QoS-aware scheduling frame... |
| 20 | [[2606.02993]] Neural Networks Provably Learn Spectral Repre... | 该研究通过将投影梯度流提升到傅里叶域，严格证明了在任意有限群上的群合成任务中，两层神经网络几乎必然收敛到单个不可约表示，并在跨层傅里叶系数间... / By lifting projected gradient flow to the Fourier domain, the authors ... |
| 21 | [[2606.03217]] An Asymptotic Theory of Chain-of-Thought in I... | 本文通过随机矩阵理论的高维渐近分析，在一个可解析的线性回归上下文学习模型中，精确刻画了思维链（CoT）推理深度对泛化误差的影响，揭示了指数提... / This paper uses high-dimensional random matrix theory to derive an exa... |
| 22 | [[2606.03245]] Hierarchies of Calibration: Classification me... | 本文在统一的预测空间框架下，系统建立了分类与回归任务中概率校准概念的严格层级关系，引入了模态校准等新概念，并证明了双PIT校准与现有离散校准... / This paper reviews, extends, and bridges notions of calibration for cl... |
| 23 | [[2606.03280]] A Negative Result on Cross-Model Activation T... | 本文在Pythia-160M到Pythia-410M的多跳推理设置中测试了跨模型激活传递，发现尽管线性翻译层在归一化空间中的对齐度极高（余弦... / This paper tests cross-model activation transfer from Pythia-160M to P... |
| 24 | [[2606.03291]] Multilingual Unlearning in LLMs: Transfer, Dy... | 本文将TOFU基准扩展至英、中、德、俄、土五种语言，系统揭示了大模型多语言知识遗忘的跨语言迁移规律（与文字系统和语系相似性高度相关），并通过... / This paper extends the TOFU benchmark to five languages (English, Chin... |
| 25 | [[2606.03305]] The Reliability Gap in Benchmark Auditing: Di... | 本文通过在27个多家族多规模模型（含前沿工业模型）上进行335次评估，系统检验了LLM Dataset Inference、Post-Hoc... / This paper systematically evaluates three leading benchmark contaminat... |
| 26 | [[2606.03318]] Beyond Ideal Instruction: A Comprehensive Fra... | 本文提出了 RUT-Bench，一个包含 1638 个测试样本、覆盖 59 个可执行环境和 11 个真实领域的大语言模型工具调用评估基准，系... / This paper introduces RUT-Bench, a benchmark with 1,638 test samples a... |
| 27 | [[2606.03398]] Causal Evidence of Stack Representations in M... | 本文在仅含单层的编码器-解码器Transformer上，通过线性探测提取Shuffle-k语言栈深度的主表征方向，并证明消融该方向会导致序列... / Using a single-layer encoder-only transformer trained on counter langu... |
| 28 | [[2606.03437]] Large Language Models Are Overconfident in Th... | 本文首次将指令微调后的校准退化与聊天模板效应解耦，发现对话式LLM存在"所有权偏差"——模型对自己生成的答案比对用户提供的相同答案置信度高最... / This paper decouples the effects of instruction tuning and chat templa... |
| 29 | [[2606.03458]] KVarN: Variance-Normalized KV-Cache Quantizat... | KVarN 提出了一种无需校准的 KV-cache 量化方法，通过 Hadamard 旋转和双轴方差归一化来修正异常的 token 尺度误差... / KVarN introduces a calibration-free KV-cache quantizer that applies Ha... |
| 30 | [[2606.03467]] StepFinder: A Temporal Semantic Framework for... | StepFinder 是一个轻量级的多智能体系统故障归因框架，通过 Qwen3 Embedding 将执行日志编码为时序语义序列，再用 Bi... / StepFinder is a lightweight failure attribution framework for multi-ag... |
| 31 | [[2606.03483]] Analyzing Stream Collapse in Hyper-Connection... | 本文诊断了Hyper-Connections中多流残差路径出现的“流崩溃”现象——残差混合矩阵趋近单位阵、信号与可解释特征集中于单一主导流，... / This paper diagnoses a "stream collapse" failure mode in Hyper-Connect... |
| 32 | [[2606.03498]] Demystifying Pipeline Parallelism: First Theo... | 本文首次为 PipeDream 风格的流水线并行训练建立了非凸收敛理论，提出随机化抽象 RPD 并证明其延迟随阶段数 S 以 Θ(S⁴/K)... / This paper provides the first clean nonconvex convergence guarantee fo... |
| 33 | [[2606.03532]] When Should the Teacher Move? Temporal Coupli... | 本文系统研究了自 on-policy 蒸馏中教师-学生的时间耦合，发现隔离期（教师完全冻结）是稳定学习的关键结构特性，并提出 Consoli... / This paper systematically studies temporal coupling in self on-policy ... |
| 34 | [[2606.03569]] When Attention Collapses: Stage-Aware Visual ... | 本文提出 Structure-to-Semantics (STS) 两阶段视觉 token 剪枝框架，通过第一阶段基于势能最小化的排斥采样保... / This paper introduces STS, a training-free two-stage visual token prun... |
| 35 | [[2606.03602]] CauTion: Knowing When to Trust LLMs for Ensem... | CauTion 通过三阶段框架（算法集成共识投票、无标注信任校准仲裁、循环修复）将 LLM 领域知识可靠地融入统计因果发现，仅在算法证据不可... / CauTion is a three-stage framework that reliably integrates LLM domain... |
| 36 | [[2606.03608]] Exploiting Verification-Generation Gap: Test-... | 本文提出TTRL-CoCoV框架，利用"验证能力领先于生成能力"的核心洞察，通过置信度条件化的验证机制在无需标签的测试时强化学习中同时提升P... / This paper proposes TTRL-CoCoV, a confidence-adaptive test-time RL fra... |
| 37 | [[2606.03645]] The Shape of Addition: Geometric Structures o... | 该研究通过对多操作数加法任务中LLM残差流激活的逐位分析，发现了"等原始和轨迹"（IRST）这一层次化几何流形结构，并提出了噪声量化模型，将... / By analyzing residual-stream activations during multi-operand addition... |
| 38 | [[2606.03648]] Safety Measurements for Fine-tuned LLMs Shoul... | 本文通过对四种开源LLM在五个数据集上的系统实验，证明安全评估必须锚定在具体能力目标上，并揭示微调模型会对安全提示产生不连贯输出，导致自动安... / Through systematic experiments on four open-source LLMs across five fi... |
| 39 | [[2606.03650]] CoEval: Ranking Language Models for Custom Ta... | CoEval 是一个开源框架，仅通过任务描述即可自动生成无标签、零污染的属性分层评测数据，并利用跨厂商的裁判模型 ensemble 对候选模... / CoEval is an open-source framework that generates fresh, attribute-str... |
| 40 | [[2606.03712]] When Graph Tokens Sink: A Mechanistic Analysi... | 本文通过对LLaGA和TEA-GLM两种代表性图语言模型的机制分析，发现图token中存在"图sink token"现象——它们在特定隐藏维... / This paper presents a mechanistic analysis of two representative Graph... |
| 41 | [[2606.03730]] Beyond False Stability: High-Noise Drift Gati... | 该论文通过系统分析CLIP视觉表征在不同强度随机扰动下的漂移行为，发现对抗样本在弱噪声下呈现虚假稳定性、但在高噪声下显著比干净样本更不稳定这... / This paper systematically analyzes how CLIP's visual representations r... |
| 42 | [[2606.03739]] Entropy Gate: Entropy Quenching for Near-Loss... | 本文提出 Entropy Gate，一种受统计力学启发的 token 压缩框架，通过多因子信息能量（统计、结构、位置）对 token 赋权，... / This paper introduces Entropy Gate, a thermodynamics-inspired token co... |
| 43 | [[2606.03780]] Expert-Aware Causal Tracing of Factual Recall... | 本文将因果追踪从密集Transformer扩展到稀疏MoE模型，提出两阶段专家感知追踪协议：在Qwen3-30B-A3B中事实回忆可精确定位... / This paper extends causal tracing of factual recall from dense transfo... |
| 44 | [[2606.03785]] Backdoor Unlearning Generalization: A Path To... | 该研究表明，在大型语言模型中通过持续预训练"遗忘"单一后门触发器时，这种去后门化过程会跨触发器泛化，显著抑制模型中其他从未被显式针对的后门行... / The authors demonstrate that unlearning a single backdoor trigger in L... |
| 45 | [[2606.03793]] Exploring Adversarial Robustness and Safety A... | 该研究通过对12种语言下三种代表性开源MLLM（PALO、PARROT、Qwen3-VL）的系统评估，发现对抗图像扰动具有强跨语言可迁移性，... / This paper systematically evaluates adversarial robustness and multimo... |
| 46 | [[2606.03846]] Clustered Self-Assessment: A Simple yet Effec... | 本文提出了一种基于语义聚类的自评估方法，通过NLI模型将LLM采样生成结果聚类后转化为结构化的多选题选项，再利用模型对选项标签的Softma... / This paper proposes Clustered Self-Assessment, a method that groups sa... |
| 47 | [[2606.03883]] Reasoning Structure of Large Language Models | 本文构建了一套包含21种逻辑谜题的可扩展基准测试，并提出将大型推理模型的非结构化思维链转换为可验证的原子声明依赖图（DAG），基于吸收马尔可... / This paper builds a scalable benchmark of 21 grid logic puzzles and pr... |
| 48 | [[2606.03899]] Denoise First, Orthogonalize Later: Understan... | 本文严格证明了 Muon 优化器中动量的本质是谱滤波器——在正交化之前通过指数移动平均抑制梯度噪声、保留相干信号，从而扩大谱间隙并稳定奇异子... / This paper rigorously proves that momentum in the Muon optimizer acts ... |
| 49 | [[2606.03969]] Quantifying Faithful Confidence Expression in... | 本文提出了首个系统量化大型推理模型（LRMs）忠实校准（FC）的框架，基于token概率、隐藏状态和采样一致性三种内部不确定性估计器，配合前... / This paper introduces the first systematic framework to quantify Faith... |
| 50 | [[2606.03990]] Neuron Populations Exhibit Divergent Selectiv... | 该研究通过对语言模型（至30B）和视觉模型（至5B）的跨模型神经元匹配分析，发现"罗塞塔神经元"（Rosetta Neurons）的数量随模... / This paper establishes that Rosetta Neurons—units with recurrent activ... |

---

*Overview generated from 50 paper summaries. Paper count verified: 50 .md files found (excluding overview.md).*
