---
title: "Daily Paper Overview — 2026-05-05"
date: 2026-05-05
tags:
  - daily-overview
  - arxiv
papers: 39
---

## 今日必读 / Must Read Today

### 1. [[2605.03327]] DGPO: Distribution-Guided Policy Optimization for Fine-Grained Credit Assignment

> **推荐理由 / Why read:** DGPO 将 GRPO 粗粒度的序列级信用分配改进为细粒度 token 级信用，用有界 Hellinger 距离替代无界 KL 散度，在 AIME 2024 上达到 60.0%（超越 DAPO 10pp），仅增加 3.6% 训练开销。
>
> DGPO upgrades GRPO's coarse sequence-level credit assignment to fine-grained token-level via bounded Hellinger distance, achieving 60.0% on AIME 2024 (+10pp over DAPO) with only 3.6% overhead.

### 2. [[2605.03871]] EvoLM: Self-Evolving Language Models through Co-Evolved Discriminative Rubrics

> **推荐理由 / Why read:** 首个完全无需外部监督的后训练框架——单一模型内共同进化评分准则生成器与策略，Qwen3-8B 生成的准则在 RewardBench-2 上超越 GPT-4.1 达 25.7%，对自改进闭环设计有重要启示。
>
> First fully self-supervised post-training paradigm co-evolving rubric generator and policy in one LM; Qwen3-8B rubrics beat GPT-4.1 by 25.7% on RewardBench-2.

### 3. [[2605.03255]] Do LLMs have core beliefs?

> **推荐理由 / Why read:** 通过对抗性对话树（ADT）系统测试 16 个 LLM 的认知稳定性，发现 2026 旗舰模型虽能抵抗社会压力但在元论证攻击下崩溃，且"友好"人设消融实验证明抵抗力是安全对齐产物而非真正认知基础——对理解 LLM 内在推理可靠性至关重要。
>
> Adversarial Dialogue Trees reveal that 2026 flagship LLMs resist social pressure but collapse under meta-argumentative attacks; persona ablation proves epistemic stability is a guardrail artifact, not genuine cognition.

---

## 按主题分类 / Papers by Topic

### 优化与训练 / Optimization & Training

| Paper | 一句话 / One-line |
|-------|-------------------|
| [[2605.03327]] DGPO | 用 Hellinger 距离实现 token 级信用分配，AIME 60% / Token-level credit via Hellinger distance, AIME 60% |
| [[2605.03769]] Nora | 行正交投影+行归一化矩阵优化器，LLaMA 训练超越 Muon / Row-orthogonal matrix optimizer beating Muon on LLaMA |
| [[2605.03373]] ZO Kernel Perspective | 零阶 SGD 的 NTK 视角，近似误差与参数维度无关 / ZO-SGD NTK view with dimension-free approximation error |
| [[2605.03869]] MEAZO | 标量全局自适应零阶优化器，匹配 ZO-Adam 性能 / Scalar-adaptive ZO optimizer matching ZO-Adam |
| [[2605.03667]] ELAS | 低秩训练+2:4 激活稀疏，1.5-2.75× 推理加速 / Low-rank + 2:4 activation sparsity, 1.5-2.75× inference |
| [[2605.03724]] Rethinking LoRA Rank | 证明二分类 LoRA rank=1 即最优，挑战 rank≥12 建议 / Proves rank-1 suffices for binary LoRA, challenging rank≥12 |
| [[2605.03425]] FIBER | 滤波感知差分隐私优化器，严格隐私下超越 DP-AdamW / Filter-aware DP optimizer outperforming DP-AdamW |

### 机制可解释性 / Mechanistic Interpretability

| Paper | 一句话 / One-line |
|-------|-------------------|
| [[2605.03354]] Agent Memory Circuits | 追踪 Qwen-3 记忆框架电路，发现"控制先于内容"不对称 / Traces Qwen-3 memory circuits, finds "control-before-content" asymmetry |
| [[2605.03258]] Counting in Transformers | 计数方向与数字输出行正交（|cos|≤0.032），9行修复受限60-100%，LoRA Q/V 7.67M 真生成 83.1% / Count direction orthogonal to digit rows (|cos|≤0.032); 9-row repair 60-100% constrained, 7.67M LoRA Q/V 83.1% in generation |
| [[2605.03598]] R-RNN Graph Resolvent | 图论 resolvent 揭示 RNN 多跳时间路由结构 / Graph resolvent reveals RNN multi-hop temporal routing |
| [[2605.03780]] Task Vector Geometry | 任务向量凸组合=贝叶斯检索，近正交子空间=外推学习 / Convex task vectors = Bayesian retrieval; orthogonal subspace = extrapolation |
| [[2605.03907]] PSR Steering | 从 prompt steering 蒸馏 token 级转向系数，超越 prompting / Distills token-level steering from prompting, outperforms prompting |
| [[2605.03609]] Moral Reasoning Control | 定位伦理推理分支点，闭式校准实现精细道德偏好调节 / Locates moral branch points, closed-form calibration for fine-grained control |

### LLM 推理与效率 / LLM Inference & Efficiency

| Paper | 一句话 / One-line |
|-------|-------------------|
| [[2605.03562]] HeadQ | 从模型可见 score 空间衡量 KV-cache 量化误差，2-bit 消除 84-94% 困惑度 / Score-space KV quantization removing 84-94% excess PPL at 2-bit |
| [[2605.03351]] FrameMogging | 无训练视频 VLM 视觉状态复用，延迟降低 14.9-35.9× / Training-free video VLM reuse, 14.9-35.9× latency reduction |
| [[2605.03644]] AdapShot | 熵探针动态选 shot+RoPE 位置重编码 KV 复用，DBSA +10% / 4.64× / Entropy-probe dynamic shots + RoPE position re-encoding KV reuse, +10% / 4.64× over DBSA |
| [[2605.03884]] QKVShare | 量化 KV 缓存跨智能体传递，8K 上下文 TTFT 降至 397ms / Quantized KV handoff across agents, TTFT 397ms at 8K |
| [[2605.03379]] Vote-Accuracy Curve | 两次调用即可预测任意投票预算精度，揭示单次精度非可靠指标 / Two calls suffice to predict vote accuracy at any budget |
| [[2605.03255]] LLM Core Beliefs | ADT 框架测试 LLM 认知稳定性，抵抗力是安全对齐产物 / ADT framework testing LLM epistemic stability, resistance is guardrail artifact |

### 自监督与表示学习 / Self-Supervised & Representation Learning

| Paper | 一句话 / One-line |
|-------|-------------------|
| [[2605.03517]] Latent Distribution Matching | 统一 ICA/SimCLR/VICReg/CPC/JEPA 的 LDM 框架，证明可识别性，CPC 与 stopgrad 均 R²=0.99 / Unifies ICA/SimCLR/VICReg/CPC/JEPA via LDM; identifiability theorems; CPC & stopgrad both R²=0.99 |
| [[2605.03346]] Embedding Accuracy Collapse | 维度低于真实维度常数比例时，三元组准确率坍塌至 50% / Accuracy collapses to 50% when embedding dimension falls below constant fraction |
| [[2605.03953]] SATFormer | 逐 token/head 门控复用第一层 value 表示，检索任务 +1.5 点 / Per-token/head gated V1 reuse, +1.5 points on retrieval tasks |

### 理论与数学基础 / Theory & Mathematical Foundations

| Paper | 一句话 / One-line |
|-------|-------------------|
| [[2605.03313]] Adversarial Gradient Perturbations | 对抗梯度扰动下分布式凸优化的紧致可行性阈值与查询复杂度 / Tight feasibility and query complexity for distributed convex optimization under adversarial gradients |
| [[2605.03499]] FL Generalization Bounds | 层次采样 + Wasserstein 距离的联邦学习泛化界，严格蕴含 CMI 界 / Hierarchical Wasserstein FL bounds strictly implying CMI bounds |
| [[2605.03601]] ReLU Identifiability | 几乎所有 ReLU 网络存在可识别参数，功能维度 = 参数数-隐藏神经元数 / Most ReLU nets have identifiable params; functional dim = #params − #hidden |
| [[2605.03823]] Realizable Bayes-Consistency | 无界间隙 Littlestone 树刻画+Gale-Stewart 构造性上界 / Unbounded-gap Littlestone tree characterization + Gale-Stewart constructive upper bound |
| [[2605.03634]] Free Decompression | 代数谱曲线自由解压缩，26K 维 192K 秒降至 39 秒 / Algebraic spectral curve free decompression; 26K-dim 192K s → 39 s |
| [[2605.03636]] BNN Information Plane | 二值网络信息平面分析，压缩现象常见但不稳定关联泛化 / BNN information plane analysis; compression common but not consistently linked to generalization |

### 自我改进与对齐 / Self-Improvement & Alignment

| Paper | 一句话 / One-line |
|-------|-------------------|
| [[2605.03871]] EvoLM | 无外部监督的后训练，准则生成器与策略共同进化 / Fully self-supervised post-training with co-evolved rubrics and policy |
| [[2605.03998]] EQUITRIAGE | 五模型急诊分诊性别公平性审计，CoT 反而恶化公平性 / Five-model ED triage gender fairness audit; CoT worsens fairness |

### 可信 AI 与安全 / Trustworthy AI & Safety

| Paper | 一句话 / One-line |
|-------|-------------------|
| [[2605.04039]] SaFE-Scale | 临床 LLM 安全性是部署属性而非规模属性，34 模型大规模评估 / Clinical LLM safety is deployment property not scaling property; 34-model eval |
| [[2605.03847]] Mechanical Conscience | 最小干预监管滤波器框架，多智能体碰撞率从 18.7% 降至 2.4% / Minimal-intervention supervisory filter; multi-agent collisions 18.7%→2.4% |
| [[2605.03838]] TRACE Framework | 计量学基础的可信智能体 AI 四层参考架构 / Metrologically-grounded four-layer trustworthy agentic AI architecture |

### 硬件与系统 / Hardware & Systems

| Paper | 一句话 / One-line |
|-------|-------------------|
| [[2605.03561]] Exascale Diagnostics | HPC 性能分析 GPU 加速，Aurora 10 万 MPI 9.69 秒导入 / HPC performance analysis GPU acceleration; 100K MPI ranks in 9.69s |
| [[2605.03396]] BNN FPGA Detection | BNN YOLOv3-tiny FPGA 实现，VOC 39.6% mAP50 / BNN YOLOv3-tiny on FPGA, 39.6% mAP50 on VOC |
| [[2605.03713]] SPEC CPU2026 | 首次跨 9 平台 SPEC CPU2026 微架构特征分析 / First 9-platform SPEC CPU2026 microarchitectural characterization |
| [[2605.03974]] LIPPEN | 全 64 位指针加密替代 ARM PAC，零元数据开销 / Full 64-bit pointer encryption replacing ARM PAC, zero metadata overhead |

### 主动学习与应用 / Active Learning & Applications

| Paper | 一句话 / One-line |
|-------|-------------------|
| [[2605.03964]] MLIP Active Learning | 预训练模型表示作主动学习信号，数据需求减少 28-38% / Pretrained representations as AL signals, 28-38% data reduction |
| [[2605.04008]] Brain Tumor Segmentation | SegResNet + 混合精度 3D 脑肿瘤分割，整体 Dice 0.84 / SegResNet + mixed-precision 3D brain tumor segmentation, Dice 0.84 |

---

## All Papers

| # | ID | Title | 核心主题 / Core Topic |
|---|----|-------|----------------------|
| 1 | [[2605.03255]] | Do LLMs have core beliefs? | LLM 认知稳定性 / LLM epistemic stability |
| 2 | [[2605.03258]] | Right Answer, Wrong Direction | 计数几何瓶颈 / Counting geometric bottleneck |
| 3 | [[2605.03313]] | Adversarial Gradient Perturbations | 分布式对抗优化 / Distributed adversarial optimization |
| 4 | [[2605.03327]] | DGPO | Token 级信用分配 / Token-level credit assignment |
| 5 | [[2605.03346]] | Embedding Accuracy Collapse | 维度-准确率坍塌 / Dimension-accuracy collapse |
| 6 | [[2605.03351]] | FrameMogging | 视频 VLM 缓存复用 / Video VLM cache reuse |
| 7 | [[2605.03354]] | Agent Memory Circuits | 智能体记忆电路 / Agent memory circuits |
| 8 | [[2605.03373]] | ZO Kernel Perspective | 零阶 NTK 动力学 / Zeroth-order NTK dynamics |
| 9 | [[2605.03379]] | Vote-Accuracy Curve | 投票精度预测 / Vote accuracy prediction |
| 10 | [[2605.03396]] | BNN FPGA Detection | FPGA 目标检测 / FPGA object detection |
| 11 | [[2605.03425]] | FIBER | 差分隐私优化 / Differential privacy optimization |
| 12 | [[2605.03499]] | FL Generalization Bounds | 联邦泛化界 / FL generalization bounds |
| 13 | [[2605.03517]] | Latent Distribution Matching | SSL 统一框架 / Unified SSL framework |
| 14 | [[2605.03561]] | Exascale Diagnostics | HPC GPU 加速 / HPC GPU acceleration |
| 15 | [[2605.03562]] | HeadQ | KV-cache 量化 / KV-cache quantization |
| 16 | [[2605.03598]] | R-RNN Graph Resolvent | RNN 图论分析 / RNN graph analysis |
| 17 | [[2605.03601]] | ReLU Identifiability | ReLU 参数可识别性 / ReLU parameter identifiability |
| 18 | [[2605.03609]] | Moral Reasoning Control | 道德推理控制 / Moral reasoning control |
| 19 | [[2605.03634]] | Free Decompression | 谱密度外推 / Spectral density extrapolation |
| 20 | [[2605.03636]] | BNN Information Plane | 二值网络信息平面 / BNN information plane |
| 21 | [[2605.03644]] | AdapShot | 自适应多示例 ICL / Adaptive many-shot ICL |
| 22 | [[2605.03667]] | ELAS | 低秩+稀疏训练 / Low-rank + sparse training |
| 23 | [[2605.03713]] | SPEC CPU2026 | CPU 基准分析 / CPU benchmark analysis |
| 24 | [[2605.03724]] | Rethinking LoRA Rank | LoRA 秩选择理论 / LoRA rank selection theory |
| 25 | [[2605.03769]] | Nora Optimizer | 矩阵优化器设计 / Matrix optimizer design |
| 26 | [[2605.03780]] | Task Vector Geometry | 任务向量几何 / Task vector geometry |
| 27 | [[2605.03823]] | Realizable Bayes-Consistency | 贝叶斯一致性 / Bayes-consistency theory |
| 28 | [[2605.03838]] | TRACE Framework | 可信智能体架构 / Trustworthy agentic AI architecture |
| 29 | [[2605.03847]] | Mechanical Conscience | 多智能体安全 / Multi-agent safety framework |
| 30 | [[2605.03869]] | MEAZO | 自适应零阶优化 / Adaptive zeroth-order optimization |
| 31 | [[2605.03871]] | EvoLM | 自进化语言模型 / Self-evolving language models |
| 32 | [[2605.03884]] | QKVShare | 量化 KV 跨智能体传递 / Quantized KV cross-agent handoff |
| 33 | [[2605.03907]] | PSR Steering | 激活转向蒸馏 / Activation steering distillation |
| 34 | [[2605.03953]] | SATFormer | 选择性访问 Transformer / Selective access Transformer |
| 35 | [[2605.03964]] | MLIP Active Learning | 主动学习采集信号 / Active learning acquisition signals |
| 36 | [[2605.03974]] | LIPPEN | 指针完整性加密 / Pointer integrity encryption |
| 37 | [[2605.03998]] | EQUITRIAGE | LLM 分诊公平性 / LLM triage fairness audit |
| 38 | [[2605.04008]] | Brain Tumor Segmentation | 3D 脑肿瘤分割 / 3D brain tumor segmentation |
| 39 | [[2605.04039]] | SaFE-Scale | 临床 LLM 安全缩放 / Clinical LLM safety scaling |
