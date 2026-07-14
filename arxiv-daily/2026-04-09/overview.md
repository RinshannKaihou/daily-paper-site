---
title: "Daily Paper Overview — 2026-04-09"
date: 2026-04-09
tags:
  - daily-overview
  - paper-digest
papers: 34
---

# Daily Paper Overview — 2026-04-09

## Quick Stats

| Metric | Value |
|--------|-------|
| Papers reviewed | 34 |
| Categories | cs.CL, cs.AI, cs.LG, cs.CV, cs.PF, cs.AR, stat.ML |
| Source papers scanned | 364 |
| Filter pass rate | 9.3% |
| Time range | 2026-04-09 |

## 今日必读 / Must Read Today

> Top picks based on relevance to your interests.

| Paper | 推荐理由 / Why |
|-------|---------------|
| [[2604.08527v1]] Demystifying OPD | 揭示了on-policy蒸馏中重复token导致训练崩溃的机制，提出Stable-OPD修复方案 (+7.2%准确率)。Identifies repetition-saturation failure in on-policy distillation; proposes Stable-OPD with 7.2% avg accuracy gains. |
| [[2604.08524v1]] Representation Steering | 机制分析发现引导向量通过OV电路（而非QK电路）传播，可稀疏化90-99%而不损失效果。Steering vectors act via OV circuits; 90-99% sparsification with minimal loss. |
| [[2604.08510v1]] Implicit Curriculum | 证明LLM预训练中存在可组合的技能学习课程，可预测训练进度 (R²=.68-.84)。LLMs learn compositional skill curriculum during pretraining; trajectory prediction R²=.68-.84. |
| [[2604.07955v1]] Residual Errors in Quantization | ICLR 2026论文，发现GPTQ/GPTAQ中补偿感知误差，修复Llama2-7B困惑度从13.60→8.34。Finds sub-optimal calibration in GPTQ/GPTAQ; fixes Llama2-7B perplexity 13.60→8.34. |
| [[2604.08118v1]] Codebook Initialisation | 证明2-bit量化中码本初始化主导优化，OA-EM方法达到Pareto前沿。Codebook init dominates optimization at 2-bit; OA-EM achieves Pareto frontier. |

---

## 按主题分类 / Papers by Topic

### LLM 训练稳定性与动力学 / Training Stability & Dynamics

| Paper | 一句话总结 / TL;DR | Tags |
|-------|-------------------|------|
| [[2604.08527v1]] Demystifying OPD | 重复token获得4-9倍过大优势信号导致OPD训练崩溃；Stable-OPD通过KL正则+混合蒸馏修复。Repetition-saturation causes length inflation; Stable-OPD fixes it with KL + mixture distillation. | `training-stability` `distillation` |
| [[2604.07963v1]] Rethinking Data Mixing | 从梯度动力学重新定义"域"概念，DoGraph框架跨尺度提升性能。Redefines domain via gradient dynamics; DoGraph achieves 37.9% avg accuracy on GPT-2. | `data-mixing` `training-dynamics` |
| [[2604.07941v1]] LLM Post-Training Survey | 以轨迹来源为轴统一解读off/on-policy学习方法。Unified framework for off/on-policy learning via trajectory provenance lens. | `post-training` `RLHF` `survey` |
| [[2604.08539v1]] OpenVLThinkerV2 | 基于最优传输的G2RPO算法，通过标准正态映射稳定多任务RL训练。Gaussian GRPO via optimal transport for RL training stability; beats GPT-4o on MMMU. | `RLVR` `training-stability` `multimodal` |

### 机制可解释性与隐藏状态 / Mechanistic Interpretability & Hidden States

| Paper | 一句话总结 / TL;DR | Tags |
|-------|-------------------|------|
| [[2604.08524v1]] Representation Steering | 引导向量通过OV电路传播，不同方法共享功能可互换电路。Steering vectors act through OV circuits; 90-99% sparsification possible. | `mechanistic-interpretability` `steering` |
| [[2604.08510v1]] Implicit Curriculum | 预训练中技能以可组合课程涌现，跨模型Spearman ρ=.81。Compositional skill emergence during pretraining; cross-model Spearman ρ=.81. | `pretraining-dynamics` `emergence` |
| [[2604.08039v1]] LINE | LLM驱动的迭代神经元解释框架，自动标注视觉模型神经元。LLM-driven iterative neuron explanations for vision models; up to +0.18 AUC on CoSy. | `neuron-interpretability` `vision` |
| [[2604.08284v1]] DMLE | 因果追踪揭示公式/描述与实例定位到不同层。Causal tracing reveals formulas/descriptions vs instances localize to different layers. | `knowledge-editing` `mechanistic` |
| [[2604.08169v1]] Activation Steering | 投影感知方法选择性干预失调token，多轮对话中保持连贯性。Projection-aware steering for aligned generation; multi-turn evaluation. | `activation-steering` `alignment` |
| [[2604.08271v1]] Illusion of Unlearning | 遗忘后特征仍具92.5%线性探针准确率。Hidden features remain discriminative despite apparent unlearning (92.5% accuracy). | `unlearning` `representations` |

### 量化与数值精度 / Quantization & Numerical Precision

| Paper | 一句话总结 / TL;DR | Tags |
|-------|-------------------|------|
| [[2604.07955v1]] Residual Errors | ICLR 2026：GPTQ/GPTAQ补偿感知误差导致Llama2-7B困惑度13.60→8.34。Compensation-aware error r₂ in GPTQ/GPTAQ; Llama2-7B C4 PPL 13.60→8.34. | `quantization` `LLM` |
| [[2604.08118v1]] Codebook Init | 2-bit量化中码本初始化主导优化，OA-EM达Pareto前沿。Init dominates optimization at 2-bit; OA-EM achieves Pareto frontier. | `quantization` `vector-quantization` |
| [[2604.08474v1]] Quantization in FL | INT4在8x通信压缩下匹配FP32；INT2导致灾难性分数不稳定。INT4 matches FP32 at 8x comm reduction; INT2 causes catastrophic score instability. | `quantization` `federated-learning` |
| [[2604.07925v1]] Sinkhorn Attention Rank | 双指数秩衰减证明，经验上缓解了Softmax的坍缩。Doubly exponential rank decay proof for Sinkhorn attention; empirically mitigates collapse. | `attention` `rank-collapse` `theory` |

### 推理可靠性与服务 / Inference Reliability & Serving

| Paper | 一句话总结 / TL;DR | Tags |
|-------|-------------------|------|
| [[2604.07931v1]] Robust Length Prediction | 输出长度服从重尾分布，ProD实现最高25% MAE降低。Output lengths follow heavy-tailed distribution; ProD achieves up to 25% MAE reduction. | `inference` `serving` |
| [[2604.08075v1]] Dual-Pool Routing | Token-budget路由减少31-42% GPU时间，年省$2.86M。Token-budget routing reduces GPU-hours 31-42%, saves $2.86M/yr on A100. | `LLM-serving` `cost-optimization` |
| [[2604.08133v1]] Alloc-MoE | 预算感知专家激活分配，半预算下1.15-1.34x加速。Budget-aware expert activation; 1.15-1.34x speedup at half budget (ACL 2026). | `MoE` `inference` |
| [[2604.08541v1]] Routing Distraction | 视觉输入导致中间层路由偏离，未能充分激活领域专家。Cross-modal semantic sharing causes routing divergence in multimodal MoE. | `MoE` `multimodal` `routing` |

### 表示分析与评估 / Representation Analysis & Evaluation

| Paper | 一句话总结 / TL;DR | Tags |
|-------|-------------------|------|
| [[2604.08192v1]] Inside-Out ViT | 电路发现指标DDB/CSS预测泛化性能(+13.4%/+34.1%)。Circuit-discovery metrics DDB/CSS predict generalization. | `generalization` `ViT` `circuits` |
| [[2604.08492v1]] Node Embedding Stability | 无通用维度-稳定性趋势，最大稳定性≠最优性能。No universal dimension-stability trend; max stability ≠ optimal performance. | `embeddings` `stability` |
| [[2604.08502v1]] C-Score | 无标注的CAM解释一致性度量，可检测模型崩溃前兆。Annotation-free metric for CAM explanation consistency; detects pre-collapse signals. | `explainability` `medical-imaging` |
| [[2604.08513v1]] Semantic Drift | 微调以架构依赖方式系统性地改变医学解释。Fine-tuning causes architecture-dependent semantic drift in medical explanations. | `fine-tuning` `explainability` |
| [[2604.08335v1]] Dead Weights, Live Signals | 5个冻结LLM的前馈图，仅17M训练参数超越单一模型。Feedforward graph of 5 frozen LLMs; only 17M trained params beat individual models. | `model-combination` `frozen-models` |

### 机器遗忘与偏差 / Machine Unlearning & Bias

| Paper | 一句话总结 / TL;DR | Tags |
|-------|-------------------|------|
| [[2604.08111v1]] Bias Redistribution | 遗忘沿性别（非年龄）边界重新分配CLIP空间中的偏差。Unlearning redistributes bias along gender boundaries in CLIP space. | `unlearning` `fairness` `CLIP` |
| [[2604.08271v1]] Illusion of Unlearning | 特征-分类器错位，遗忘后模型仍保留92.5%线性探针准确率。Feature-classifier misalignment; 92.5% linear-probe accuracy after unlearning (AISTATS 2026). | `unlearning` `representations` |

### RL 推理 / RL for Reasoning

| Paper | 一句话总结 / TL;DR | Tags |
|-------|-------------------|------|
| [[2604.08476v1]] Faithful GRPO | 约束GRPO防止CoT-answer不一致，提升视觉空间推理。Constrains GRPO for visual-spatial reasoning; prevents CoT-answer inconsistency. | `GRPO` `spatial-reasoning` |
| [[2604.08299v1]] SeLaR | 熵门控潜在推理，Qwen3-8B上平均+4.63%提升。Entropy-gated latent reasoning; +4.63% avg improvement on Qwen3-8B (ACL 2026). | `latent-reasoning` `inference` |

### 数学基础与架构 / Mathematical Foundations & Architecture

| Paper | 一句话总结 / TL;DR | Tags |
|-------|-------------------|------|
| [[2604.07904v1]] Kuramoto Phase | 神经启发的同步机制在Transformer中的应用。Neuro-inspired synchronization in transformers; 0.1-0.7pp gains on SSL benchmarks. | `attention` `synchronization` |
| [[2604.07935v1]] Hyperscale Lottery | Mamba-1→3牺牲边缘延迟换取云端吞吐量，28-48%边缘惩罚。Mamba-1→3 trades edge latency for cloud throughput; 28-48% edge penalty. | `SSM` `edge-efficiency` |
| [[2604.08245v1]] Meta-Principle Physics | 将物理元原理嵌入架构模块，"436x"声明有误导性。Embeds physical meta-principles as architectural modules; "436x" claim is misleading. | `physics-informed` `architecture` |

### 硬件与系统 / Hardware & Systems

| Paper | 一句话总结 / TL;DR | Tags |
|-------|-------------------|------|
| [[2604.08044v1]] 3D-DRAM LLM Accelerators | 全栈评估框架，2.53x加速/6.66x能效优于H200。Full-stack evaluation framework; 2.53x speedup / 6.66x energy efficiency over H200. | `hardware` `LLM-accelerator` |
| [[2604.08182v1]] Wattlytics | HPC集群性能/能耗/TCO协同优化平台。HPC cluster co-optimization platform for performance/energy/TCO. | `HPC` `energy` `systems` |
| [[2604.08357v1]] Bias-Constrained Diffusion | 自适应噪声调度用于PDE仿真，FSD大幅改善。Adaptive noise schedules for PDE emulation; dramatic FSD improvements. | `diffusion` `PDE` `training-stability` |

### 神经科学 / Neuroscience & Brain Decoding

| Paper | 一句话总结 / TL;DR | Tags |
|-------|-------------------|------|
| [[2604.08537v1]] Brain Decoding | 分层上下文学习实现跨受试者脑解码，Top-1 22.7% vs 前作3.9%。Hierarchical ICL for cross-subject brain decoding; 22.7% Top-1 vs 3.9% prior work. | `brain-decoding` `meta-learning` `fMRI` |

---

## All Papers

| # | Paper | Authors | Key Topic | 一句话总结 / TL;DR |
|---|-------|---------|-----------|-------------------|
| 1 | [[2604.08527v1]] Demystifying OPD | Feng Luo et al. | Training Stability | 重复token导致OPD训练崩溃；Stable-OPD修复 (+7.2%)。Repetition-saturation failure; Stable-OPD fixes it. |
| 2 | [[2604.08524v1]] Representation Steering | Stephen Cheng et al. | Mechanistic Interpretability | 引导向量通过OV电路传播，可稀疏化90-99%。Steering acts via OV circuits; 90-99% sparsification. |
| 3 | [[2604.08510v1]] Implicit Curriculum | Emmy Liu et al. | Pretraining Dynamics | 预训练中技能以可组合课程涌现。Compositional skill curriculum during pretraining. |
| 4 | [[2604.07955v1]] Residual Errors | Shuaiting Li et al. | Quantization (ICLR 2026) | GPTQ/GPTAQ补偿感知误差；Llama2-7B PPL 13.60→8.34。Compensation-aware error in GPTQ/GPTAQ. |
| 5 | [[2604.08118v1]] Codebook Init | Ian W. Kennedy et al. | Extreme Quantization | 2-bit量化中码本初始化主导优化。Codebook init dominates at 2-bit. |
| 6 | [[2604.08474v1]] Quantization in FL | Abdelkarim Loukili | Quantization / Federated | INT4匹配FP32；INT2灾难性不稳定。INT4 matches FP32; INT2 catastrophic instability. |
| 7 | [[2604.08539v1]] OpenVLThinkerV2 | Wenbo Hu et al. | Multimodal RL Training | 基于最优传输的G2RPO稳定多任务RL。Gaussian GRPO via optimal transport. |
| 8 | [[2604.08541v1]] Routing Distraction | Haolei Xu et al. | MoE Interpretability | 视觉输入导致路由偏离。Cross-modal routing divergence in multimodal MoE. |
| 9 | [[2604.08502v1]] C-Score Metric | Kabilan Elangovan et al. | Explanation Consistency | 无标注CAM解释一致性度量。Annotation-free explanation consistency metric. |
| 10 | [[2604.08513v1]] Semantic Drift | Kabilan Elangovan et al. | Fine-tuning Stability | 微调以架构依赖方式改变医学解释。Architecture-dependent semantic drift. |
| 11 | [[2604.08492v1]] Node Embedding Stability | Tobias Schumacher et al. | Embedding Reliability | 无通用维度-稳定性趋势。No universal dimension-stability trend. |
| 12 | [[2604.08271v1]] Illusion of Unlearning | Yichen Gao et al. | Unlearning (AISTATS 2026) | 遗忘后仍保留92.5%探针准确率。92.5% accuracy retained after unlearning. |
| 13 | [[2604.08335v1]] Dead Weights | Marcus Armstrong et al. | Frozen Model Graphs | 5个冻结LLM+17M参数超越单一模型。5 frozen LLMs + 17M params beat individuals. |
| 14 | [[2604.08333v1]] Lost in the Hype | Xun Zhu et al. | Medical MLLM Failure | MLLM在医学图像分类上系统性退步。Systematic MLLM degradation on medical images. |
| 15 | [[2604.08284v1]] DMLE | Yating Wang et al. | Knowledge Editing | 因果追踪揭示知识按类型分布在不同层。Causal tracing reveals type-specific layer localization. |
| 16 | [[2604.08192v1]] Inside-Out ViT | Yunxiang Peng et al. | ViT Generalization | 电路指标预测泛化 (+13.4%/+34.1%)。Circuit metrics predict generalization. |
| 17 | [[2604.08039v1]] LINE | Vladimir Zaigrajew et al. | Neuron Explanations | LLM驱动迭代神经元自动标注。LLM-driven iterative neuron labeling. |
| 18 | [[2604.08075v1]] Dual-Pool Routing | Xunzhuo Liu et al. | LLM Serving | 减31-42% GPU时间。31-42% GPU-hour reduction. |
| 19 | [[2604.07931v1]] Robust Length Prediction | Jing Wang et al. | Inference Reliability | 重尾输出长度预测。Heavy-tailed output length prediction. |
| 20 | [[2604.07925v1]] Sinkhorn Attention Rank | Michela Lapenna et al. | Attention Theory | Sinkhorn注意力双指数秩衰减证明。Doubly exponential rank decay proof. |
| 21 | [[2604.07935v1]] Hyperscale Lottery | Robin Geens et al. | SSM Edge Efficiency | Mamba边缘延迟惩罚28-48%。28-48% edge latency penalty. |
| 22 | [[2604.08169v1]] Activation Steering | Niklas Herbster et al. | Alignment Steering | 投影感知方法保持多轮连贯性。Projection-aware steering preserves multi-turn coherence. |
| 23 | [[2604.08357v1]] Bias-Constrained Diffusion | Constantin Le Clei et al. | Diffusion Training | 自适应噪声调度改善PDE仿真。Adaptive noise schedules for PDE emulation. |
| 24 | [[2604.08245v1]] Meta-Principle Physics | Helong Hu et al. | Physics-Informed | 物理元原理嵌入架构。Physical meta-principles as architecture modules. |
| 25 | [[2604.08133v1]] Alloc-MoE | Baihui Liu et al. | MoE Inference (ACL 2026) | 半预算下1.15-1.34x加速。1.15-1.34x speedup at half budget. |
| 26 | [[2604.08182v1]] Wattlytics | Ayesha Afzal et al. | HPC Energy | HPC性能/能耗/TCO协同优化。HPC performance/energy/TCO co-optimization. |
| 27 | [[2604.08044v1]] 3D-DRAM Accelerators | Cong Li et al. | Hardware Evaluation | 全栈3D-DRAM LLM加速器仿真。Full-stack 3D-DRAM LLM accelerator simulation. |
| 28 | [[2604.07904v1]] Kuramoto Phase | Mingqing Xiao et al. | Attention Mechanism | 神经启发同步机制。Neuro-inspired synchronization in transformers. |
| 29 | [[2604.07963v1]] Data Mixing | Yuanjian Xu et al. | Training Data | 梯度动力学重新定义域。Gradient-dynamics-based domain definition. |
| 30 | [[2604.08476v1]] Faithful GRPO | Sai Srinivas Kancheti et al. | RL Reasoning | 约束GRPO防止CoT-answer不一致。Constrained GRPO for visual-spatial reasoning. |
| 31 | [[2604.08111v1]] Bias Redistribution | Yunusa Haruna et al. | Unlearning Bias | 遗忘沿性别边界重分配偏差。Unlearning redistributes bias along gender boundaries. |
| 32 | [[2604.08537v1]] Brain Decoding | Mu Nan et al. | fMRI / Meta-learning | 分层上下文学习跨受试者脑解码。Hierarchical ICL for brain decoding. |
| 33 | [[2604.07941v1]] LLM Post-Training Survey | Shiwan Zhao et al. | RLHF Survey (Huawei) | 以轨迹来源统一off/on-policy方法。Unified view via trajectory provenance. |
| 34 | [[2604.08299v1]] SeLaR | Renyu Fu et al. | Latent Reasoning (ACL 2026) | 熵门控潜在推理。Entropy-gated latent reasoning. |

---

*Overview generated on 2026-04-11*
