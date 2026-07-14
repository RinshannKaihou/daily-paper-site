---
title: "arXiv Daily — 2026-05-14"
date: 2026-05-14
tags:
  - daily-overview
  - arxiv
papers: 50
---

# arXiv Daily — 2026-05-14

> 本日共收录 **50** 篇论文，覆盖 LLM 推理优化、训练对齐、可解释性、扩散模型、量化安全、持续学习、神经网络理论等方向。
> **50 papers** curated across LLM inference, training & alignment, interpretability, diffusion models, quantization & safety, continual learning, neural network theory, and more.

---

## 今日必读 / Must Read Today

### 1. [[2605.14220]] Diagnosing Training Inference Mismatch in LLM Reinforcement Learning

> **推荐理由：** 揭示了 LLM 强化学习（如 RLHF/GRPO）中 rollout 生成与策略优化之间存在数值不一致（TIM），这种微小差异可独立导致训练崩溃，对所有 LLM 对齐训练具有根本性影响。
> **Why read:** Reveals Training-Inference Mismatch (TIM) — numerical disagreements between rollout and policy optimization in LLM RL that can independently cause training collapse. Fundamental finding for all LLM alignment pipelines.

### 2. [[2605.14588]] Silent Collapse in Recursive Learning Systems

> **推荐理由：** 发现递归/自训练系统中存在"静默崩塌"——模型的预测熵、表征多样性和尾部覆盖率在 loss/perplexity/accuracy 看似正常时持续收缩，这对 AI 自我改进的安全性提出严峻警示。
> **Why read:** Identifies "silent collapse" in recursive/self-training systems where internal distributions contract while surface metrics remain healthy. Critical safety concern for AI self-improvement loops.

### 3. [[2605.14694]] The Rate-Distortion-Polysemanticity Tradeoff in SAEs

> **推荐理由：** 从信息论角度严格证明了 SAE 中重建质量、编码效率与单义性之间存在根本性三方权衡——迫使 SAE 学出单义特征必然增加码率或失真。这是可解释性领域的核心理论贡献。
> **Why read:** Formally proves a fundamental three-way tradeoff (Rate-Distortion-Polysemanticity) in SAEs: forcing monosemantic features provably raises rate or distortion. A cornerstone theoretical result for mechanistic interpretability.

---

## 按主题分类 / Papers by Topic

### LLM推理优化 / LLM Inference Optimization

| Paper | 简述 / Summary |
|-------|---------------|
| [[2605.14217]] PreFT | 仅在 prefill 阶段应用适配器，decode 阶段丢弃，512 适配器同时服务 Llama 3.1 70B 时实现 1.9x 吞吐提升 / Applies LoRA/ReFT adapters only during prefill; discards at decode, achieving 1.9x throughput with 512 adapters on Llama 3.1 70B |
| [[2605.14249]] EnergyLens | 基于 einsum 接口的端到端框架，无需 GPU 即可预测多卡 LLM 推理的能耗与延迟 / End-to-end framework predicting multi-GPU LLM inference energy and latency from einsum specs without GPU access |
| [[2605.14292]] KV Retention | 系统研究 KV-cache 压缩的七种机制，提出基于多样性惩罚的保留评分器 / Rigorous study of seven KV-cache compression mechanisms; proposes diversity-penalized retention scorer |
| [[2605.14841]] GPart | 用随机稀疏等距分区矩阵替代 LoRA 双线性低秩分解，实现端到端直接维度微调 / Replaces LoRA's bilinear low-rank structure with isometric random partition matrix for end-to-end fine-tuning |
| [[2605.14844]] XFP | 质量驱动的自适应码本量化，通过稀疏离群值分离和余弦相似度自动选择机制 / Quality-targeted adaptive codebook quantization with sparse outlier separation and auto channel selection |
| [[2605.14929]] SOP | 硬件感知的逐层 PTQ 方法，结合码本搜索、带符号缩放和背包分配 / Hardware-aware per-layer PTQ combining codebook search, signed scaling, and knapsack allocation |
| [[2605.14978]] PPOW | 用强化学习将推测解码的草稿模型优化从 token 级提升到窗口级 / Reframes speculative decoding drafter training from token-level to window-level RL optimization |
| [[2605.15051]] Speculative Decoding Latency | 基于 Little's Law 推导可解释的投机解码延迟模型，分解为预填充、草稿生成和验证三组件 / Derives closed-form interpretable latency model for speculative decoding via Little's Law decomposition |

### LLM训练与对齐 / LLM Training & Alignment

| Paper | 简述 / Summary |
|-------|---------------|
| [[2605.14220]] TIM | 揭示 LLM 强化学习中 rollout 与策略优化间的数值不一致可独立导致训练崩溃 / Reveals numerical mismatch between rollout and policy optimization in LLM RL causing training instability |
| [[2605.14967]] InfoSFT | 在 SFT 中对 token 损失按信息量加权，聚焦中等置信度 token，持续改善数学/代码/推理 / Token-weighting scheme for SFT focusing on medium-confidence tokens; improves math/code/reasoning tasks |
| [[2605.14517]] Intent Fidelity | 通过 5W3H 结构化提示消融实验提出维度级意图保真度评估框架 / Dimension-level intent fidelity evaluation via 5W3H structured prompt ablation across 2,880 outputs |

### 推理与推理扩展 / Reasoning & Inference-Time Scaling

| Paper | 简述 / Summary |
|-------|---------------|
| [[2605.14358]] Minimal Cores | 提出"最小核心"概念，从 CoT 中提取最少必要步骤，发现 46% 的步骤可被移除 / Introduces minimal cores — smallest CoT subsets preserving answers; 46% of steps are removable |
| [[2605.14588]] Silent Collapse | 发现递归学习中内部分布在表面指标正常时持续收缩，对 AI 自我改进提出安全警示 / Silent internal distribution collapse during recursive learning while surface metrics remain healthy |
| [[2605.14619]] SliceGraph | 通过稀疏激活键构建 mutual-kNN 图分析多次 CoT 推理结构，发现 85.5% 的问题存在过程同分异构体 / Builds activation-key overlap graphs for multi-run CoT; 85.5% of problems contain process isomers |
| [[2605.14659]] Slower Generalization | 发现小 Transformer 学习结构化输出时验证集收敛最快的数据集大小为中间值而非最大值 / Small Transformers learn structured output fastest at intermediate dataset sizes, not the largest |
| [[2605.15100]] DDC | 联合优化采样宽度与推理路径深度的自适应推理扩展框架，10x token 效率提升 / Unifies inter-path early stopping with intra-path pruning for 10x token efficiency in inference scaling |

### 可解释性与机制分析 / Interpretability & Mechanistic Analysis

| Paper | 简述 / Summary |
|-------|---------------|
| [[2605.14258]] Transformer Dynamics | 对三个生产级 LLM 完整雅可比矩阵特征分解，发现训练安装了从旋转主导到近对称的单调梯度 / Full Jacobian eigendecomposition reveals learned monotonic non-normality gradient through depth |
| [[2605.14347]] Exemplar Partitioning | 无需训练的激活空间聚类方法，以约 1000 倍低于 SAE 的计算成本实现可解释特征字典 / Training-free activation clustering via streaming leader-clustering; ~1000x cheaper than SAE |
| [[2605.14535]] Geographic Space | 使用激活补丁探究 LLM 如何处理地理相对空间概念，发现多尺度距离编码 / Activation patching reveals multi-scale numerical distance encoding in LLM geographic reasoning |
| [[2605.14694]] SAE RDP | 信息论证明 SAE 中重建质量、编码效率与单义性存在根本三方权衡 / Proves fundamental Rate-Distortion-Polysemanticity tradeoff in SAEs via information theory |
| [[2605.14749]] Non-linear Interventions | 用可逆非线性特征映射替代线性干预方法，在拒绝绕过任务上以两个数量级更低误差实现目标行为 / Replaces linear interventions with invertible non-linear feature maps; 100x lower error on refusal bypass |
| [[2605.15183]] Tensor Similarity | 提出基于权重空间且排列不变的张量相似度度量，通过极化同构高效计算功能等价性 / Closed-form symmetry-invariant weight-based metric for comparing multilinear networks via polarization |
| [[2605.15154]] RoSHAP | 通过 Bootstrap 重采样估计 SHAP 特征归因分布，构建基于活跃度、强度和稳定性的稳健排序 / Models SHAP attribution distributions via bootstrap resampling; robust ranking across activity/intensity/stability |

### 扩散模型与生成 / Diffusion Models & Generation

| Paper | 简述 / Summary |
|-------|---------------|
| [[2605.14305]] FeF-DLLM | 通过前缀条件化精确后验消除离散扩散语言模型的因式分解误差，推测解码加速推理 / Eliminates factorization error in discrete diffusion LMs via prefix-conditioned exact posterior; speculative decoding |
| [[2605.14368]] DiHAL | 利用几何代理指标定位 Transformer 中对扩散最友好的隐藏空间层，用条件扩散桥替换前缀 / Geometry-guided identification of diffusion-friendly layers; replaces lower prefix with conditional diffusion bridge |
| [[2605.14530]] LDVLM | 揭示大型扩散视觉语言模型存在掩码先验漂移和位置注意力坍塌，提出两种无需训练的修复方法 / Identifies mask prior drift and positional attention collapse in large diffusion VLMs; training-free fixes |
| [[2605.14570]] UQ for LLDMs | 首次系统研究大型语言扩散模型的不确定性量化，提出基于去噪轨迹语义不稳定性的 D-CoCoA / First systematic UQ study for large language diffusion models; D-CoCoA via denoising trajectory semantics |
| [[2605.14819]] Velocity Deficit | 发现 Flow Matching 中 MSE 损失导致速度场系统性低估速度幅值，提出一行无训练修复 / Identifies systematic velocity underestimation in Flow Matching MSE; proposes one-line training-free fix |

### 量化与AI安全 / Quantization & AI Safety

| Paper | 简述 / Summary |
|-------|---------------|
| [[2605.14359]] RQ-MoE | 将残差量化与 MoE 结合，双流量化实现输入相关动态码本，解码速度提升 6-17x / Combines residual quantization with MoE for input-dependent dynamic codebooks; 6-17x faster decoding |
| [[2605.15138]] MANSU | 揭示现有遗忘方法在 4-bit 量化后知识恢复的原因，提出基于因果电路归因的量化永久遗忘 / Existing unlearning fails under 4-bit quantization; MANSU achieves quantization-permanent unlearning via circuit attribution |
| [[2605.15152]] Outlier Injection | 首个量化条件攻击，通过注入权重异常值使 AWQ/GPTQ/GGUF 等方法目标权重坍塌 / First quantization-conditioned attack exploiting AWQ/GPTQ/GGUF via outlier-induced weight collapse |
| [[2605.15134]] Predictable Failures | 提出"可预测性损失"使模型失效尾部分布更易用极值理论外推预测 / Proposes forecastability loss making model failure tails predictable via extreme value theory extrapolation |
| [[2605.15164]] Behavioural Assurance | 系统论证行为评估方法在认知论上无法验证高风险安全性声明（如无隐藏目标、无欺骗性对齐）/ Argues behavioural assurance is epistemically insufficient for verifying high-consequence AI safety claims |

### 持续学习 / Continual Learning

| Paper | 简述 / Summary |
|-------|---------------|
| [[2605.14785]] Imbalanced Forgetting | 揭示回放式类增量学习中不同类别遗忘程度差异显著且普遍，推导三个最后一层梯度因子 / Demonstrates systematic imbalanced forgetting across classes despite equal rehearsal; derives gradient factors |
| [[2605.14938]] Octopus | 无需历史数据的梯度正交化两阶段持续学习框架，在多模态大模型上达到 SOTA / History-free gradient orthogonalization for MLLM continual learning; SOTA on UCIT benchmark |
| [[2605.15053]] TFGN | 架构级覆盖层通过读/写分解使跨域梯度更新保持 ≥99.59% 正交，实现近零灾难性遗忘 / Architectural overlay achieving near-zero catastrophic forgetting (BWT=-0.007) via Read/Write decomposition |

### 神经网络理论 / Neural Network Theory

| Paper | 简述 / Summary |
|-------|---------------|
| [[2605.14567]] Scaling Laws | 通过可求解层次化模型证明 scaling law 从逐层特征学习的级联相变中涌现 / Proves scaling laws emerge from cascade of sharp feature-learning transitions in solvable hierarchical model |
| [[2605.14663]] Optimal GD Rates | 利用微分几何证明局部 PL 条件下梯度下降的渐近收敛速率与强凸最优速率一致 / Proves GD asymptotic rate under local PL matches optimal strongly convex rate via differential geometry |
| [[2605.14685]] Goldstone Modes | 借鉴物理学证明深层等变网络中自发对称性破缺产生的 Goldstone 模式可实现深层信息传播 / Spontaneous symmetry breaking yields Goldstone-like modes enabling deep information propagation without residuals |
| [[2605.14489]] Schur Decomposition | 基于 Schur 分解的状态矩阵投影保证离散时间状态空间层的渐近稳定性 / Schur-decomposition-based projection enforcing asymptotic stability in state-space neural network layers |
| [[2605.14521]] LayerNorm → RMSNorm | 通过列中心约束将 LayerNorm 的中心化操作折叠进上游线性层，实现 LN 到 RMSNorm 的精确替换 / Exactly replaces LayerNorm with computationally cheaper RMSNorm by folding centering into upstream linear layers |

### 形式验证 / Formal Verification

| Paper | 简述 / Summary |
|-------|---------------|
| [[2605.14294]] BuFFeT | 通过 ReLU 函数融合自注意力层点积的双互补平面界限，收紧 Transformer 鲁棒性验证 / Fuses dual planar bounds for attention dot products as ReLU expressions; tightens Transformer robustness verification |
| [[2605.14758]] RNN-ProVe | 通过策略驱动采样和统计误差边界对 RNN 强化学习策略进行概率性验证 / Probabilistic verification of RNN-based RL policies via policy-driven sampling with statistical error bounds |
| [[2605.14666]] LTLfMT Monitoring | 首个基于有限迹线性时序逻辑的预期性监控框架，结合自动机理论与 SMT 求解 / First anticipatory monitoring framework for data-aware temporal properties via LTLfMT with automata + SMT |

### 表示学习与OOD / Representation Learning & OOD

| Paper | 简述 / Summary |
|-------|---------------|
| [[2605.14413]] MahaVar | 在马氏距离基础上引入类间距离方差项，利用 Neural Collapse 几何结构区分 OOD / Augments Mahalanobis distance with class-wise variance term under Neural Collapse for OOD detection |
| [[2605.14893]] CLIP Noise | 发现 CLIP/SigLIP 嵌入中存在大量共享噪声维度（如 ViT-L/14 有 164 维），剪除后性能不降反升 / Reveals shared noise subspace in CLIP/SigLIP embeddings (164/768 dims); pruning improves performance |

### 科学计算 / Scientific Computing

| Paper | 简述 / Summary |
|-------|---------------|
| [[2605.14546]] PDE Experts | 发现从同一基座微调的 PDE 专家在权重空间形成可校准的物理方向，提出校准条件合并方法 / PDE fine-tuned experts define calibratable physical directions in weight space; proposes Calibration-Conditioned Merge |
| [[2605.14643]] Unbiased PDE Training | 分析 BSDE 方法中 Euler-Maruyama 离散化引入的偏差，提出无需二阶导数的无偏训练框架 / Corrects Euler-Maruyama bias in BSDE-based deep learning; proposes unbiased training without second-order derivatives |

### 软件工程与AI Agent / Software Engineering & AI Agents

| Paper | 简述 / Summary |
|-------|---------------|
| [[2605.14362]] SizeFilter | 基于文件大小的预执行启发式过滤框架，利用 OS 级元数据在 token 化前移除大型非代码产物 / Pre-execution size-based filtering removing non-code artifacts before tokenization using OS-level stat() metadata |
| [[2605.14865]] AI Agent Eval | 结合自顶向下 agent 级和自底向上 span 级评估的整体框架，实现可扩展的 AI Agent 故障定位与分类 / Holistic agent evaluation combining agent-level diagnosis with span-level decomposition; SOTA on TRAIL |

---

## All Papers

| # | ID | Title |
|---|-----|-------|
| 1 | [[2605.14217]] | PreFT: Prefill-only finetuning for efficient inference |
| 2 | [[2605.14220]] | Diagnosing Training Inference Mismatch in LLM Reinforcement Learning |
| 3 | [[2605.14249]] | EnergyLens: Predictive Energy-Aware Exploration for Multi-GPU LLM Inference Optimization |
| 4 | [[2605.14258]] | Dynamics of the Transformer Residual Stream: Coupling Spectral Geometry to Network Topology |
| 5 | [[2605.14292]] | Minimal-Intervention KV Retention: A Design-Space Study and a Diversity-Penalty Survivor |
| 6 | [[2605.14294]] | Precise Verification of Transformers through ReLU-Catalyzed Abstraction Refinement |
| 7 | [[2605.14305]] | Factorization-Error-Free Discrete Diffusion Language Model via Speculative Decoding |
| 8 | [[2605.14347]] | Exemplar Partitioning for Mechanistic Interpretability |
| 9 | [[2605.14358]] | Uncovering the Representation Geometry of Minimal Cores in Overcomplete Reasoning Traces |
| 10 | [[2605.14359]] | RQ-MoE: Residual Quantization via Mixture of Experts for Efficient Input-Dependent Vector Compression |
| 11 | [[2605.14362]] | Correctness-Aware Repository Filtering Under Maximum Effective Context Window Constraints |
| 12 | [[2605.14368]] | Where Should Diffusion Enter a Language Model? Geometry-Guided Hidden-State Replacement |
| 13 | [[2605.14413]] | MahaVar: OOD Detection via Class-wise Mahalanobis Distance Variance under Neural Collapse |
| 14 | [[2605.14489]] | A Novel Schur-Decomposition-Based Weight Projection Method for Stable State-Space Neural-Network Architectures |
| 15 | [[2605.14517]] | Dimension-Level Intent Fidelity Evaluation for Large Language Models: Evidence from Structured Prompt Ablation |
| 16 | [[2605.14521]] | Enjoy Your Layer Normalization with the Computational Efficiency of RMSNorm |
| 17 | [[2605.14530]] | Mitigating Mask Prior Drift and Positional Attention Collapse in Large Diffusion Vision-Language Models |
| 18 | [[2605.14535]] | Exploring Geographic Relative Space in Large Language Models through Activation Patching |
| 19 | [[2605.14546]] | Discovering Physical Directions in Weight Space: Composing Neural PDE Experts |
| 20 | [[2605.14567]] | Scaling Laws from Sequential Feature Recovery: A Solvable Hierarchical Model |
| 21 | [[2605.14570]] | Uncertainty Quantification for Large Language Diffusion Models |
| 22 | [[2605.14588]] | Silent Collapse in Recursive Learning Systems |
| 23 | [[2605.14619]] | SliceGraph: Mapping Process Isomers in Multi-Run Chain-of-Thought Reasoning |
| 24 | [[2605.14643]] | Unbiased and Second-Order-Free Training for High-Dimensional PDEs |
| 25 | [[2605.14659]] | Slower Generalization, Faster Memorization: A Sweet Spot in Algorithmic Learning |
| 26 | [[2605.14663]] | Optimal Asymptotic Rates for (Stochastic) Gradient Descent under the Local PL-Condition: A Geometric Approach |
| 27 | [[2605.14666]] | Monitoring Data-aware Temporal Properties (Extended Version) |
| 28 | [[2605.14685]] | Spontaneous Symmetry Breaking and Goldstone Modes for Deep Information Propagation |
| 29 | [[2605.14694]] | The Rate-Distortion-Polysemanticity Tradeoff in SAEs |
| 30 | [[2605.14749]] | Non-linear Interventions on Large Language Models |
| 31 | [[2605.14758]] | Probabilistic Verification of Recurrent Neural Networks for Single and Multi-Agent Reinforcement Learning |
| 32 | [[2605.14785]] | Understanding Imbalanced Forgetting in Rehearsal-Based Class-Incremental Learning |
| 33 | [[2605.14819]] | The Velocity Deficit: Initial Energy Injection for Flow Matching |
| 34 | [[2605.14841]] | GPart: End-to-End Isometric Fine-Tuning via Global Parameter Partitioning |
| 35 | [[2605.14844]] | XFP: Quality-Targeted Adaptive Codebook Quantization with Sparse Outlier Separation for LLM Inference |
| 36 | [[2605.14865]] | Holistic Evaluation and Failure Diagnosis of AI Agents |
| 37 | [[2605.14893]] | Your CLIP has 164 dimensions of noise: Exploring the embeddings covariance eigenspectrum of contrastively pretrained vision-language transformers |
| 38 | [[2605.14929]] | A Hardware-Aware, Per-Layer Methodology for Post-Training Quantization of Large Language Models |
| 39 | [[2605.14938]] | Octopus: History-Free Gradient Orthogonalization for Continual Learning in Multimodal Large Language Models |
| 40 | [[2605.14967]] | InfoSFT: Learn More and Forget Less with Information-Aware Token Weighting |
| 41 | [[2605.14978]] | Performance-Driven Policy Optimization for Speculative Decoding with Adaptive Windowing |
| 42 | [[2605.15051]] | An Interpretable Latency Model for Speculative Decoding in LLM Serving |
| 43 | [[2605.15053]] | TFGN: Task-Free, Replay-Free Continual Pre-Training Without Catastrophic Forgetting at LLM Scale |
| 44 | [[2605.15100]] | Dual-Dimensional Consistency: Balancing Budget and Quality in Adaptive Inference-Time Scaling |
| 45 | [[2605.15134]] | Training ML Models with Predictable Failures |
| 46 | [[2605.15138]] | Forgetting That Sticks: Quantization-Permanent Unlearning via Circuit Attribution |
| 47 | [[2605.15152]] | Widening the Gap: Exploiting LLM Quantization via Outlier Injection |
| 48 | [[2605.15154]] | RoSHAP: A Distributional Framework and Robust Metric for Stable Feature Attribution |
| 49 | [[2605.15164]] | Position: Behavioural Assurance Cannot Verify the Safety Claims Governance Now Demands |
| 50 | [[2605.15183]] | When Are Two Networks the Same? Tensor Similarity for Mechanistic Interpretability |
