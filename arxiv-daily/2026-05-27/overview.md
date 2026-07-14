---
title: "Daily Paper Overview — 2026-05-27"
date: 2026-05-27
tags:
  - daily-overview
  - arxiv
papers: 50
---

## 今日必读 / Must Read Today

| # | Paper | Reason / 理由 |
|---|-------|---------------|
| 1 | [[2605.27733]] Entry-Wise Clipping for Spectral Control | 揭示LLM梯度噪声的"局部化"特性，推导出贝叶斯最优逐元素收缩算子，无需SVD即实现谱控制，在NanoGPT上节省~7%训练token。Exploits localization of heavy-tailed gradient noise to derive a Bayes-optimal smooth shrinkage operator for spectral control — no SVD needed, saves ~7% training tokens on NanoGPT. |
| 2 | [[2605.27954]] Cyclical Entropy Eruption (SEAL) | 首次发现Agent RL训练中独特的"周期性熵爆发"现象，提出SEAL辅助损失将Llama3.2-1B在WebShop上从0%恢复至79.69%。Discovers recurring entropy eruption cycles in Agent RL (unlike monotonic collapse in single-turn RL) and proposes SEAL auxiliary loss to stabilize training across 4 models. |
| 3 | [[2605.28704]] Floating-Point NN Expressive Power | 提出"可区分性"框架，证明浮点神经网络在任意归约顺序和有界ulp误差下仍为通用表示器，同时揭示cos/cosh等函数无法实现通用表示。Proves floating-point NNs with arbitrary reduction orders and bounded ulp errors remain universal representators for most activations, while cos/cosh provably fail — foundational for computation reliability. |

## 按主题分类 / Papers by Topic

### LLM Training Stability & Observability / LLM训练稳定性与可观测性

| Paper | 摘要 / Summary |
|-------|---------------|
| [[2605.27733]] Entry-Wise Clipping | 利用梯度噪声局部化特性推导逐元素平滑收缩算子，以O(ε⁻⁴)复杂度实现谱范数控制。Derives Bayes-optimal smooth shrinkage for spectral gradient control without SVD, saving ~7% tokens on NanoGPT. |
| [[2605.27954]] SEAL (Cyclical Entropy Eruption) | 发现Agent RL中周期性熵爆发现象，提出SEAL辅助交叉熵损失分离正确/错误轨迹表示。Discovers entropy eruption cycles in Agent RL; SEAL auxiliary loss separates correct/incorrect trajectory representations. |
| [[2605.27541]] SparseOpt | 揭示Batch Normalization在稀疏训练中放大梯度偏转(1-s)^(-1/2)，提出感知稀疏度的预条件优化器。Shows BN amplifies sparse-neuron gradients by (1-s)^(-1/2); proposes sparsity-aware diagonal preconditioner. |
| [[2605.27739]] Worker Disagreement in Local SGD | 证明Local SGD中worker分歧天然揭示损失曲面尖锐方向，可作为无需Hessian的子空间估计器。Worker-average gap in Local SGD reveals sharp loss directions as a Hessian-free subspace estimator. |
| [[2605.28585]] Outer-Momentum Restarting | 在DiLoCo等两阶段优化器中周期性重置外层动量，利用相位消除扩大稳定超参数区间。Periodic outer-momentum reset in two-phase optimizers exploits phase cancellation to widen stable HP region. |
| [[2605.28184]] RL-MTP (OCC) | 分析多Token预测与RL联合训练失败原因，提出最优系数校准自适应调节MTP系数。Identifies MTP-RL gradient decorrelation as failure cause; proposes Optimal Coefficient Calibration. |
| [[2605.28819]] PEFT-Arena | 从稳定性-可塑性视角评估PEFT方法，发现正交微调(OFT)在权重谱保持上表现最优。Benchmarks PEFT stability-plasticity trade-off; orthogonal finetuning achieves best Pareto frontier. |
| [[2605.27678]] Heterogeneous Parallelism | 提出多模态LLM训练的异构并行抽象，共置模式下TFLOPS/GPU提升高达49.3%。Heterogeneous parallelism for MLLM training with up to 49.3% TFLOPS/GPU improvement in colocated mode. |

### LLM Inference Evaluation / LLM推理评估

| Paper | 摘要 / Summary |
|-------|---------------|
| [[2605.27763]] Batch-Conditioned Refusal Testing | 配对测试协议揭示batch条件可改变拒绝决策，但效应率仅~0.16%，可通过batch-invariant内核消除。Paired protocol shows batch-conditioned refusal flips at ~0.16% rate, eliminable via batch-invariant kernels. |
| [[2605.28398]] HRBench | 首个评估混合推理LLM思考模式切换策略的统一基准，覆盖12种配置。First unified benchmark for thinking-mode switching in hybrid-reasoning LLMs across 12 configurations. |
| [[2605.28302]] Attention-FFN Disaggregation | 系统探索MoE推理中AFD设计空间，在DeepSeek-V3.2上实现~4k tokens/s吞吐量。Design-space exploration of Attention-FFN Disaggregation for MoE serving, achieving ~4k tok/s on DeepSeek-V3.2. |
| [[2605.28142]] Marginal Sharpening | 对答案边缘分布进行power sharpening，在数学/代码生成上超越传统power sampling且快38倍。Power sharpening on answer marginals beats traditional power sampling at 38x speed on math/code generation. |
| [[2605.28751]] EWA Code RL | 在代码RL中发现不同覆盖率checkpoint形成正确性-效率前沿，外推可扩展该前沿。Checkpoints at different test coverage form correctness-efficiency frontiers; extrapolation extends beyond endpoints. |

### LLM Hidden States & Interpretability / LLM隐藏状态与可解释性

| Paper | 摘要 / Summary |
|-------|---------------|
| [[2605.27970]] Perceptual Geometry in LLMs | 纯文本训练的LLM残差流中短暂涌现出与人类感知域高度对齐的几何结构。Text-trained LLMs transiently develop geometric structures in residual streams mirroring human perceptual organization. |
| [[2605.27819]] ReSAE | 残差化SAE减少多层干预中的特征冗余，在Gemma-2-9B上将∆CE大致减半。Residualized SAEs reduce multi-layer intervention redundancy, roughly halving ∆CE on Gemma-2-9B. |
| [[2605.28149]] SA-GSAE | Bi-Jump-ReLU使单个潜在变量编码反相关概念，半宽度SAE Pareto优于全宽度Gated SAE。Bi-Jump-ReLU enables single latents to encode anticorrelated concepts; half-width SAE Pareto-dominates full-width. |
| [[2605.28567]] Semantic OT for SAE | 将SAE特征表示为激活加权分布，通过最优传输计算跨层Wasserstein距离统一特征匹配与电路压缩。Represents SAE features as activation-weighted distributions; OT unifies cross-layer matching and circuit compression. |
| [[2605.28388]] Sample Difficulty in RLVR | 通过T-SAE分析样本难度对RLVR的非单调影响，中等难度样本效果最佳。T-SAE analysis shows non-monotonic effect of sample difficulty on RLVR; medium difficulty is optimal. |
| [[2605.28553]] Refusal Before Decoding | 证明拒绝行为可从中间层残差流线性解码，Mechanistic AutoDAN搜索时间减少最多72%。Refusal linearly decodable from intermediate layers; Mechanistic AutoDAN reduces search time by up to 72%. |
| [[2605.27824]] Algorithmic Deductive Circuits | 定位约3%注意力头构成稀疏电路负责演绎推理各子步骤。~3% of attention heads form sparse circuits for deductive reasoning sub-steps via causal mediation analysis. |
| [[2605.27935]] Do Agents Think Deeper | 自主式LLM智能体在多轮规划中递进式动员更深层次计算，呈"构建-精炼"模式。Autonomous LLM agents progressively engage deeper layers across planning turns in a build-refine pattern. |
| [[2605.27458]] Heterogeneous Attention Interpretation | 通用异质注意力结构Transformer解释方法，在DETR和LXMERT上优于GAE/ODAM基线。Generic interpretation for heterogeneous-attention Transformers, outperforming GAE/ODAM on DETR and LXMERT. |
| [[2605.28639]] Attentional White Bear Effect | 指令抑制某概念时其内部表征反而保持高度可恢复——行为与表征对齐存在根本差距。Concept suppression instructions make internal representations more recoverable — behavioral vs. representational alignment gap. |
| [[2605.28649]] SAEs as Stethoscopes | SAE子空间投影丢失~97%修改能量，改用SAE诊断层后注入原始任务向量更有效。SAE subspace projection discards ~97% modification energy; using SAEs only for layer diagnosis works better. |
| [[2605.28631]] SHIFT (RIRS) | 单次推理隐藏状态变化作为无训练数据选择代理，0.1-2%数据超越全量RLVR。Single-rollout hidden-state shift as training-free data selection proxy; 0.1-2% data beats full RLVR. |
| [[2605.28247]] IRDS | SAE聚类实现可解释RLVR数据选择，超越最强基线+3.9/+4.0 pp且成本低一个数量级。SAE-cluster-based interpretable RLVR data selection, +3.9/+4.0 pp over strongest baseline at 10x lower cost. |
| [[2605.28467]] ACT (Activation Consistency) | 激活一致性约束防御推理模型越狱攻击，防御机制编码为近似线性方向。Activation consistency at assistant-turn boundary defends against jailbreaks; encoded as a linear refusal direction. |
| [[2605.28722]] MARI | 竞争性多适配器+能量门控实现自适应表示干预，6个模型(7B-32B)上达到SOTA对齐。Competitive multi-adapter with energy gating for adaptive representation intervention across 6 models (7B-32B). |
| [[2605.28664]] Activation Steering Diversity | 激活转向生成安全检测合成数据需同时满足概念对齐、语义连贯和多样性。Activation steering for safety data requires success + coherence + diversity for downstream utility. |

### Computation Reliability & Precision / 计算可靠性与精度

| Paper | 摘要 / Summary |
|-------|---------------|
| [[2605.28451]] BFP FP16 SAR | FP16 FFT瓶颈是指数范围溢出而非精度，两行BFP代码修改实现Apple Silicon上2.2×加速。FP16 FFT bottleneck is exponent range overflow, not precision; 2-line BFP fix achieves 2.2x speedup on Apple Silicon. |
| [[2605.28704]] Floating-Point NN Expressivity | 浮点NN在任意归约顺序和有界ulp误差下仍为通用表示器，cos/cosh则不行。Floating-point NNs with arbitrary reduction orders remain universal representators; cos/cosh provably fail. |
| [[2605.27616]] NVFP4 QAT Architecture Study | FP4量化中模型架构选择（Swin Transformer）比量化配方对分割质量影响更大。Model architecture choice (Swin Transformer) matters more than quantization recipe for FP4 anomaly segmentation. |
| [[2605.27646]] HQMQ KV Cache | Hurwitz四元数乘法量化用于KV Cache压缩。Hurwitz Quaternion Multiplicative Quantization for KV cache compression in LLM inference. |

### Model System Cards & Technical Reports / 模型系统卡与技术报告

| Paper | 摘要 / Summary |
|-------|---------------|
| [[2605.27605]] Laguna M.1/XS.2 | Poolside 225.8B/23.4B MoE模型面向长程智能体编码，XS.2从启动到发布仅5周，SWE-bench 74.6%。Poolside MoE foundation models for agentic coding; XS.2 built in 5 weeks, 74.6% on SWE-bench Verified. |

### Hardware Reliability & SDC / 硬件可靠性与静默数据损坏

| Paper | 摘要 / Summary |
|-------|---------------|
| [[2605.27803]] HammerSim | 系统级RowHammer建模工具，基于gem5仿真器模拟DRAM行锤击漏洞。System-level RowHammer modeling tool built on gem5 simulator for DRAM vulnerability analysis. |
| [[2605.28169]] FT-Pilot | GNN引导LLM自动识别RTL易受攻击资产并生成容错代码，实现漏洞分析到加固的全自动闭环。GNN-guided LLM framework for automated fault-tolerant RTL rewriting from vulnerability analysis to hardening. |

### ML Reliability & Mathematical Foundations / ML可靠性与数学基础

| Paper | 摘要 / Summary |
|-------|---------------|
| [[2605.27673]] When do CVNNs Help | 复数神经网络优势取决于数据表示、对称性匹配和优化协议，公平调参下优势大幅缩小。CVNN advantages are conditional on data representation, symmetry matching, and fair HP selection — gains shrink significantly. |
| [[2605.27989]] Law of Neural Interaction | 发现深度-宽度比控制的高效神经交互区间随规模保持稳定，与MMLU-Pro性能相关。Depth-width ratio governs efficient neural interaction interval that remains stable across scales. |
| [[2605.28057]] Recovery Complexity TTA | 首个TTA可学习性理论框架，引入恢复复杂度刻画非平稳测试流下的基本极限。First TTA learnability framework with recovery complexity characterizing fundamental limits under non-stationary streams. |
| [[2605.28109]] IB-TPO | 基于信息瓶颈的IB-Score度量和树结构采样，在相同token预算下多生成50%轨迹。Information-Bottleneck-based IB-Score and tree sampling generate 50% more trajectories under same token budget. |
| [[2605.28150]] Off-Policy Pessimism | 无重要性权重的离策略目标通过Lambert W函数隐式引入悲观性，β偏移优势估计稳定训练。Ratio-free off-policy objectives induce Lambert-tempered pessimism; β-shifted advantage stabilizes training. |
| [[2605.28165]] Robust Supervised Learning Unification | 三轴四阶段统一框架将DRO/VRM/Mixup等方法组织在同一设计空间中，联合HPO达到最佳单方法性能。Three-axis four-stage unified framework for robust learning; joint HPO matches best single-method baselines. |
| [[2605.28513]] SVRG Learning Theory | 首次通过算法稳定性为SVRG建立非平凡泛化界，推广至SAGA方法。First non-vacuous SVRG generalization analysis via algorithmic stability, extended to SAGA. |
| [[2605.28517]] SGDM Stability | 首次为SGD动量建立紧致泛化界，动量仅以O(1/(1-β)^{3/2})影响稳定性。First tight stability bounds for SGD momentum; momentum worsens stability by at most O(1/(1-β)^{3/2}). |
| [[2605.28600]] Log-ICoT | 首次理论分析隐式思维链，证明多层Transformer仅需poly(n)样本和log₂k阶段学会k-奇偶校验。First theoretical analysis of implicit CoT; L-layer Transformer learns k-parity with poly(n) samples in log₂k stages. |
| [[2605.28705]] In-Context Continual Learning | 首个上下文持续学习理论框架，揭示Transformer推理阶段也存在系统性偏差和遗忘。First in-context continual learning theory showing systematic bias and forgetting even without parameter updates. |
| [[2605.28613]] Perturbed Matrix Factorization | 量化加性噪声对深度矩阵分解隐式正则化的影响，给出扰动大小的显式误差界。Quantifies additive noise impact on implicit regularization in deep matrix factorization with explicit error bounds. |
| [[2605.27786]] LoRP Depth Compression | 分析LLM层间表示局部性实现自适应无训练深度剪枝。Analyzes representation locality across LLM layers for adaptive training-free depth pruning. |

### LLM Safety & Alignment / LLM安全与对齐

| Paper | 摘要 / Summary |
|-------|---------------|
| [[2605.28732]] MemTrace | 将LLM记忆管道转化为可执行记忆演化图，归因信号指导提示优化提升最高7.62%。Transforms LLM memory pipelines into evolution graphs; attribution-guided prompt optimization boosts up to 7.62%. |
| [[2605.28554]] TFM Uncertainty | 表格基础模型预测性能优于GBDT但共形预测条件覆盖率显著更低，揭示性能-可靠性权衡。TFMs outperform GBDTs in AUC but show systematically lower conditional coverage under conformal prediction. |

## All Papers

| # | Paper | Topic / 主题 | Relevance / 相关性 |
|---|-------|-------------|-------------------|
| 1 | [[2605.27458]] Generic Interpretation for Heterogeneous Attention | Interpretability / 可解释性 | Medium |
| 2 | [[2605.27541]] SparseOpt | Training Stability / 训练稳定性 | Medium |
| 3 | [[2605.27605]] Laguna M.1/XS.2 Technical Report | Technical Report / 技术报告 | Medium |
| 4 | [[2605.27616]] NVFP4 QAT Architecture Study | Precision / 精度 | Medium |
| 5 | [[2605.27646]] HQMQ KV Cache Compression | Inference / 推理 | Low |
| 6 | [[2605.27673]] When do CVNNs Help | Math Foundations / 数学基础 | Medium |
| 7 | [[2605.27678]] Heterogeneous Parallelism for MLLM | Training Systems / 训练系统 | Low |
| 8 | [[2605.27733]] Entry-Wise Clipping for Spectral Control | Training Stability / 训练稳定性 | **High** |
| 9 | [[2605.27739]] Worker Disagreement in Local SGD | Training Stability / 训练稳定性 | Medium |
| 10 | [[2605.27763]] Batch-Conditioned Refusal Testing | Inference Evaluation / 推理评估 | Medium |
| 11 | [[2605.27786]] LoRP Depth Compression | Compression / 压缩 | Low |
| 12 | [[2605.27803]] HammerSim (RowHammer) | SDC / 静默数据损坏 | Medium |
| 13 | [[2605.27819]] ReSAE | Interpretability / 可解释性 | Medium |
| 14 | [[2605.27824]] Algorithmic Deductive Circuits | Interpretability / 可解释性 | Medium |
| 15 | [[2605.27935]] Do Agents Think Deeper | Interpretability / 可解释性 | Medium |
| 16 | [[2605.27954]] SEAL (Cyclical Entropy Eruption) | Training Stability / 训练稳定性 | **High** |
| 17 | [[2605.27970]] Perceptual Geometry in LLMs | Interpretability / 可解释性 | Medium |
| 18 | [[2605.27989]] Law of Neural Interaction | Math Foundations / 数学基础 | Medium |
| 19 | [[2605.28057]] Recovery Complexity TTA | Math Foundations / 数学基础 | Low |
| 20 | [[2605.28109]] IB-TPO | Math Foundations / 数学基础 | Medium |
| 21 | [[2605.28142]] Marginal Sharpening | Inference / 推理 | Low |
| 22 | [[2605.28149]] SA-GSAE | Interpretability / 可解释性 | Medium |
| 23 | [[2605.28150]] Off-Policy Pessimism | Math Foundations / 数学基础 | Medium |
| 24 | [[2605.28165]] Robust Supervised Learning Unification | Math Foundations / 数学基础 | Medium |
| 25 | [[2605.28169]] FT-Pilot | SDC / 静默数据损坏 | Medium |
| 26 | [[2605.28184]] RL-MTP (OCC) | Training Stability / 训练稳定性 | Medium |
| 27 | [[2605.28247]] IRDS | Interpretability / 可解释性 | Medium |
| 28 | [[2605.28302]] Attention-FFN Disaggregation | Inference / 推理 | Low |
| 29 | [[2605.28388]] Sample Difficulty in RLVR | Interpretability / 可解释性 | Medium |
| 30 | [[2605.28398]] HRBench | Inference Evaluation / 推理评估 | Medium |
| 31 | [[2605.28451]] BFP FP16 SAR | Precision / 精度 | Medium |
| 32 | [[2605.28467]] ACT (Activation Consistency) | Safety / 安全 | Medium |
| 33 | [[2605.28513]] SVRG Learning Theory | Math Foundations / 数学基础 | Medium |
| 34 | [[2605.28517]] SGDM Stability | Math Foundations / 数学基础 | Medium |
| 35 | [[2605.28553]] Refusal Before Decoding | Interpretability / 可解释性 | Medium |
| 36 | [[2605.28554]] TFM Uncertainty | Reliability / 可靠性 | Low |
| 37 | [[2605.28567]] Semantic OT for SAE | Interpretability / 可解释性 | Medium |
| 38 | [[2605.28585]] Outer-Momentum Restarting | Training Stability / 训练稳定性 | Medium |
| 39 | [[2605.28600]] Log-ICoT (Transformers Internalize CoT) | Math Foundations / 数学基础 | Medium |
| 40 | [[2605.28613]] Perturbed Matrix Factorization | Math Foundations / 数学基础 | Medium |
| 41 | [[2605.28631]] SHIFT (RIRS) | Hidden States / 隐藏状态 | **High** |
| 42 | [[2605.28639]] Attentional White Bear Effect | Interpretability / 可解释性 | Medium |
| 43 | [[2605.28649]] SAEs as Stethoscopes | Interpretability / 可解释性 | Medium |
| 44 | [[2605.28664]] Activation Steering Diversity | Safety / 安全 | Low |
| 45 | [[2605.28704]] Floating-Point NN Expressivity | Precision / 精度 | **High** |
| 46 | [[2605.28705]] In-Context Continual Learning | Math Foundations / 数学基础 | Low |
| 47 | [[2605.28722]] MARI (Multi-Adapter Interventions) | Interpretability / 可解释性 | Medium |
| 48 | [[2605.28732]] MemTrace | Safety / 安全 | Low |
| 49 | [[2605.28751]] EWA Code RL | Inference Evaluation / 推理评估 | Low |
| 50 | [[2605.28819]] PEFT-Arena | Training Stability / 训练稳定性 | Medium |
