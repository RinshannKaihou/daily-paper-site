---
title: "Daily arXiv Digest — 2026-06-08"
date: 2026-06-08
papers: 50
tags: ["AI", "LLM", "Alignment", "Efficiency", "Interpretability", "Robustness", "Agents", "Optimization", "Quantization", "Benchmark", "Multimodal", "Bayesian", "Diffusion", "Biomedical"]
---

# Daily arXiv Digest — 2026-06-08

共筛选 **50** 篇论文 / **50** papers curated from 381 candidates across cs.LG, cs.CL, cs.AI, cs.CV.

## 今日必读 / Must Read Today

如果只读三篇 / If you only read three papers today:

### 1. [[2606.09682]] AutoMegaKernel: A Statically-Checked Agent Harness for Self-Retargeting Megakernel Synthesis
- **推荐理由：** 把整个 LLM 前向传播编译为单一持久 CUDA megakernel，冻结的 schedule-IR 验证器在 7,160 个对抗调度上零误判拒绝所有不安全调度，在推理级 GPU（L4 最高 1.33×）上 W8A16 真实超越 cuBLAS bf16——把"正确性"做成静态属性是系统领域少见的硬核贡献。
- **Why read:** Compiles a full Llama forward pass into one persistent cooperative CUDA kernel whose safety is statically verified (zero false-accepts on 7,160 adversarial schedules), and an int8 weight-only megakernel beats CUDA-graphed cuBLAS bf16 at batch-1 on inference-class GPUs (L4 up to 1.33×) — correctness as a static property is a rare, rigorous systems contribution.

### 2. [[2606.09658]] Muon Learns More Robust and Transferable Features than Adam
- **推荐理由：** 首次从特征质量角度给出 Muon 优于 Adam 的机制性解释：在新建 FineWeb10B-C 损坏基准上 Muon 预训练模型始终更鲁棒，层探针显示更大 logit margin（ViT-S 末层 3.29 vs Adam 1.86 effective rank），并在一层多分量分类模型中严格证明等损失下 Muon 的 margin 与 effective rank 严格更大。
- **Why read:** First mechanistic explanation of why Muon beats Adam — feature quality, not just speed: larger logit margin (3.29 vs 3.13 vs 2.74) and effective rank (16.0 vs 1.86) under probes, with a theorem proving strict margin/effective-rank advantage over Adam at equal loss in a one-layer multi-component classifier.

### 3. [[2606.09410]] Capacity, Not Format: Rethinking Structured Reasoning Failures
- **推荐理由：** 把"格式税"重构为容量依赖效应而非格式本身——信息匹配的散文对照证明结构化输出对容量充裕模型无损（Sonnet MATH-Hard JSON≈CoT≈89%），但逼近能力极限的模型受损严重（Haiku −36.2pp）；"先推理后格式化"能恢复约 80–87% 损失，甚至 Opus 4.7 在 AIME 上也掉 5.3pp，对工程实践有直接指导意义。
- **Why read:** Reframes the structured-output "reasoning tax" as capacity-dependent, not format-inherent: JSON is neutral for spare-capacity models but costs Haiku −36.2pp / GPT-4o-mini −28.0pp near capacity limits, a delayed-structure ablation recovers 80–87% of the loss, and even Opus 4.7 drops 5.3pp on AIME — directly actionable for practitioners.

## 按主题分类 / Papers by Topic

### Interpretability & Representation / 可解释性与表征（9 篇）

| Paper | Short Title | 一句话描述 / One-line Description |
|:------|:------------|:----------------------------------|
| [[2606.09028]] | ATM: Action-Consistency Transfer Matrix | 无需仿真器 rollout 的潜世界模型诊断工具，2×2 转移矩阵把分钟/小时级 CEM 评估压缩到 3–5 秒 / Simulator-rollout-free latent-world-model diagnostic; 2×2 transfer matrix compresses minute/hour-long CEM eval to 3–5 s |
| [[2606.09287]] | Trajectory Geometry of Transformer Representations | 把前向传播建模为表征流形上的离散轨迹，发现语义收敛、推理曲率、歧义分叉等四类一致现象 / Recasts the forward pass as a discrete trajectory; four consistent findings (semantic convergence, reasoning curvature, ambiguity bifurcation, three-phase structure) |
| [[2606.09411]] | Now You (Still) See Me: Steganographic Payloads | 证明线性探针式 LLM 隐写检测可被对抗微调规避，并用信息论指导构造数据集恢复可检测性 / Shows linear-probe steganography detectors can be adversarially evaded (58–79% recovery retained); recontextualization restores detectability |
| [[2606.09536]] | Hadamard-Coded Output Representations | 用 Hadamard 码作分割/检测输出表示，单次前向即达 SOTA 级对抗扰动检测，干净数据 mIoU/AP 几乎无损 / Hadamard codes as output representation give SOTA single-pass adversarial-perturbation detection with near-lossless clean mIoU/AP |
| [[2606.09672]] | Correlation Is Not Enough: Human Metadata | 揭示生物医学编码器把不相关跨域概念误判为高度相似（余弦 0.76–0.92），两阶段对比微调将分离比提升到 2.30× / Exposes anisotropic failure of biomedical encoders (cosine 0.76–0.92 for unrelated cross-domain pairs); two-pass contrastive fix raises separation to 2.30× |
| [[2606.09725]] | Disentanglement with Holographic Reduced Representations | 首个基于 HRR 的无监督解耦方法，InfoM +4.6%、InfoC +5.9%，并从信息论证明解绑诱导近似槽独立 / First HRR-based unsupervised disentanglement; InfoM +4.6%, InfoC +5.9%, with theory proving unbinding induces approximate slot independence |
| [[2606.09474]] | Open-V: Training-Free Few-Shot Segmentation | 无需训练的 GFSS 框架，对冻结 SAM3-PCS 与 CLIP 做语义仲裁，PASCAL-5i harmonic mIoU 77.9（+17.7 HM） / Training-free GFSS arbitrating frozen SAM3-PCS vs CLIP; PASCAL-5i HM 77.9 (+17.7 HM over strongest trained baseline) |
| [[2606.09605]] | Hypnos: Sleep Physiology Foundation Model | 多模态睡眠基础模型，跨 8 种模态做 RQ-Transformer next-token 预测，线性探针即超监督基线 / Multimodal sleep foundation model via residual-vector-quantized next-token prediction; linear probe beats supervised baselines |
| [[2606.09646]] | Video FMs & Intuitive Physics Probing | 逐层探测显示 V-JEPA 物理信息最易读出（IntPhys2 66.67% VOE），信息集中在中后层且依赖时间读出 / Layerwise probing shows V-JEPA encodes intuitive physics most readably (66.67% VOE), concentrated in mid-late layers |

### Other ML & AI / 其他机器学习（7 篇）

| Paper | Short Title | 一句话描述 / One-line Description |
|:------|:------------|:----------------------------------|
| [[2606.08945]] | Cox-Supervised Distillation into LLM | 把 Cox 风险蒸馏进 Qwen2.5-1.5B，WHAS500 上 C-index 0.7563 接近教师 0.7658，隐藏态呈连续风险梯度 / Distils Cox hazards into a 1.5B LLM; C-index 0.7563 vs teacher 0.7658 on WHAS500, with smooth risk-gradient hidden states |
| [[2606.08973]] | Molecular Encoding for Drug Property Prediction | 系统比较六类分子指纹跨七数据集表现，分类 AUC 普遍 >0.9，注意力权重可识别化学可解释子结构 / Benchmarks 6 fingerprints across 7 datasets; classification AUC consistently >0.9, attention recovers interpretable substructures |
| [[2606.09278]] | Internalizing Geometric Law via Solver Residuals | 把几何约束求解做成 RLVR 任务，提出饱和累加奖励解决梯度掩蔽，Qwen3-8B Hard 层求解率提升 2.3× / Casts geometric constraint solving as RLVR; saturating additive rewards fix gradient masking, Hard-tier SR up 2.3× |
| [[2606.09327]] | Universal Dense Football Event Representation | 基于 TabTransformer 的足球事件 911 维稠密表示，VAEP concede Brier 0.003 远优于 XGBoost 0.090 / TabTransformer-based 911-dim football event embedding; VAEP concede Brier 0.003 vs XGBoost 0.090 |
| [[2606.09433]] | BSLI: Wastewater-First Influenza Monitoring | 首次将废水优先流感监测建模为选择性查询/弃答决策，等预算下 macro-F1 比 ACO 高 +0.098 且花费更少 / First selective query/predict/abstain formulation of wastewater-first flu monitoring; +0.098 macro-F1 vs ACO at lower cost |
| [[2606.09558]] | scTransformer with Gene Regulatory Priors | 把 TF→靶基因调控网络作为硬注意力掩码，低数据（1%、25%）下更准且跨种子特征选择更稳定 / TF→TG prior as hard attention mask; more accurate in low-data (1%/25%) and more stable across seeds |
| [[2606.09809]] | Evaluation Cards for AI Evaluation Reporting | 评测报告解释层，规模化审计发现 96.5% 结果缺最小复现字段，中位文档完整度仅 10.7% / Reporting layer audit: 96.5% of results lack minimal reproducibility fields, median completeness 10.7% |

### LLM Alignment & Safety / 对齐与安全（6 篇）

| Paper | Short Title | 一句话描述 / One-line Description |
|:------|:------------|:----------------------------------|
| [[2606.09189]] | EEG Foundation Model Attribute Leakage | 分裂控制+端点分歧审计框架，发现单端点审计放行的 EEG 嵌入仍泄漏频谱属性，标准防御无法关闭通道 / Split-control audit shows single-endpoint-approved EEG embeddings still leak attributes; standard defenses fail to close the channel |
| [[2606.09453]] | GD-MIL: Prostate Cancer BCR Prediction | 梯度反转分级对抗分支使切片表征与 Gleason 分级解耦，TCGA-PRAD C-index 0.704（+0.062 vs 最强纯影像） / Gradient-reversal grade adversary disentangles slide features from Gleason grade; C-index 0.704 (+0.062 vs best imaging-only) |
| [[2606.09635]] | GGRO: Inference-time Alignment | 推理时监控 token 熵并注入梯度引导"微调 token"，HEx-PHI 攻击 ASR 从 BoN 34.3% 降到 26.2%，抗 reward hacking / Token-entropy-guided gradient nudging at inference; HEx-PHI ASR 34.3%→26.2%, robust to reward hacking |
| [[2606.09388]] | TV-DiSP: Safe LLM Soft-Prompt Distillation | 把双模型安全系统蒸馏进约 100 个软提示向量，<1% 显存代价获得显著安全提升，全面优于 LoRA / Distils dual-model safety into ~100 soft prompts; <1% memory overhead, beats LoRA/steering-vectors |
| [[2606.09653]] | Concept-Based Representational Similarity | 概念对齐统一框架，提出 CoSAE 证明翻译与概念一致性互不蕴含，仅需 0.1% 配对数据即可恢复实例级对齐 / Unifying framework with CoSAE; proves translation ≠ concept consistency, recovers instance alignment with 0.1% paired data |
| [[2606.09735]] | The Neutral Mask: RLHF Partisan Structure | 证明 RLHF 并未删除党派几何方向而是压缩其标准差 68%、切断到生成的因果通路，底层几何仍可被重新激活 / Shows RLHF compresses partisan-direction std by 68% and severs the geometry→generation pathway; underlying geometry remains reactivatable |

### NLP & Language Applications / NLP 与语言应用（5 篇）

| Paper | Short Title | 一句话描述 / One-line Description |
|:------|:------------|:----------------------------------|
| [[2606.09376]] | Precision Is Not Faithfulness | 用 F1 遥测完备真值证明仅测精度的忠实性指标会奖励回避行为，补上覆盖率后前沿模型排名反转 / Complete-oracle (F1 telemetry) shows precision-only faithfulness metrics reward abstention; rankings invert when recall is added |
| [[2606.09389]] | LexRubric: Legal Task Diagnostic Benchmark | 中文法律任务诊断基准（649 题、12,337 条专家评分准则），最强模型 Kimi K2.6 仅 75.21%，硬子集降至 51.30% / Chinese legal diagnostic benchmark (649 items, 12,337 expert rubric criteria); best model only 75.21%, hard subset 51.30% |
| [[2606.09541]] | Rare Event Discovery in Force Spectroscopy | Focal Loss + 双阈值分诊系统在 1.34% 正样本率力谱数据上 Recall 92.31%，人工审核量削减 >90% / Focal-Loss ResNet18 + dual-threshold triage on 1.34%-prevalence force spectra; Recall 92.31%, manual curation cut >90% |
| [[2606.09697]] | PsychoSafe: Psychologically-Informed Refusals | 把 LLM 拒绝重构为循证心理支持沟通，系统提示提升拒绝质量 28.1%，但域外对抗样本泛化有限 / Reframes refusal as evidence-based psychological support; +28.1% quality via prompting but limited OOD adversarial generalization |
| [[2606.09816]] | PTL-Diffusion: Periodic Terminal Laws | 把扩散前向加噪改为收敛到周期性高斯终态律，人脸像素级 W1 误差从 DDPM 0.228 降到 0.110 / Replaces single Gaussian terminal with periodic family; Olivetti faces pixel W1 0.228→0.110 vs DDPM |

### Reasoning & Agents / 推理与智能体（4 篇）

| Paper | Short Title | 一句话描述 / One-line Description |
|:------|:------------|:----------------------------------|
| [[2606.08894]] | Distract-Bench: Semantic Visual Distractions | 新鲁棒性失效模式：注入"正确但无关"的语义干扰项，推理型 VLM 在语义干扰下反而比底座更差 / New failure mode — answer-preserving semantic distraction; reasoning VLMs degrade more than their bases under it |
| [[2606.08960]] | Hacker-Fixer Loops for Agent Benchmarks | 审计发现 16% 终端智能体任务可被奖励黑客绕过，hacker-fixer loop 在 KernelBench 上把攻击成功率从 62% 降到 0% / Audits find 16% of terminal-agent tasks hackable; hacker-fixer loop cuts KernelBench ASR 62%→0% |
| [[2606.09447]] | AliyunConsoleAgent: Real-World Cloud Agents | SFT+GRPO 两阶段训练在真实阿里云控制台达 63.52% pass@1，仅落后 Gemini 3 Pro 1.82pp 而成本低 92% / SFT+GRPO on real Alibaba Cloud; 63.52% pass@1, within 1.82pp of Gemini 3 Pro at 92% lower cost |
| [[2606.09669]] | SpatialWorld: Interactive Spatial Reasoning | 跨 8 模拟器 760 任务的空间推理基准，最强 GPT-5 平均成功率仅 17.4%，暴露主动探索短板 / 760-task spatial-reasoning benchmark across 8 simulators; best model GPT-5 only 17.4% TSR |

### Robustness & Adversarial / 鲁棒性与对抗（4 篇）

| Paper | Short Title | 一句话描述 / One-line Description |
|:------|:------------|:----------------------------------|
| [[2606.08948]] | NutriMLLM: Dietary Micronutrient Analysis | 证明主流 MLLM 在 65 种微量营养素估算上不可靠（SMAPEadj 118–138%），合成数据微调后 30B 版反超三大闭源 / Shows MLLMs unreliable at 65-nutrient estimation (SMAPEadj 118–138%); fine-tuned 30B beats GPT-5/Gemini 3/Claude |
| [[2606.09005]] | DACSI: Indirect Prompt Attack on RAG | 非命令式控制信号伪造攻击在 RAG 中把不安全披露率从 0.5% 推高到 28%，系统-文档信道分离可压回 0.17% / Command-free control-signal forgery lifts RAG unsafe-disclosure 0.5%→28%; channel separation collapses it to 0.17% |
| [[2606.09495]] | ContextShift: Object Detection Context Dependence | 受控基准发现五种检测器在上下文变化下呈"预测抑制"失效（漏检最高 +227%），性能沿兼容性轴呈 U 型 / Controlled benchmark finds prediction-suppression failure mode (FN up +227%); U-shaped performance vs compatibility axis |
| [[2606.09758]] | DARP: Difference-Aware Retrieval for IL | 半参数检索式模仿学习，聚合等价于 k-NN 图上固定低通滤波，比标准 BC 提升 15–46% / Semi-parametric retrieval-based IL; aggregation ≡ fixed low-pass filter on k-NN graph, +15–46% over BC |

### LLM Inference & Efficiency / 推理与效率（4 篇）

| Paper | Short Title | 一句话描述 / One-line Description |
|:------|:------------|:----------------------------------|
| [[2606.09048]] | BareWave: Waveform-Native Flow-Matching TTS | 首个完全波形原生零样本语音克隆框架，Seed-TTS test-en WER 1.75%，为同数据规模最优 / First fully waveform-native zero-shot TTS clone; Seed-TTS test-en WER 1.75%, best at this data scale |
| [[2606.09514]] | BUDDY: Budget-Driven Dynamic Depth Routing | 预算驱动动态深度路由，Llama3-8B 在 50% 稀疏度下保留 71.3% 精度，单一模型服务多预算 / Budget-driven dynamic depth routing; Llama3-8B retains 71.3% accuracy at 50% sparsity, single model serves multiple budgets |
| [[2606.09603]] | CGFD: Low-Resource Traditional Chinese IEP | 语料锚定特征扩散流程，25 种子扩散出 582 样本微调 Breeze-7B，BERTScore 0.779 超 GPT-5.4；发现 GCD 在繁中下适得其反 / Corpus-grounded feature diffusion; Breeze-7B+QLoRA BERTScore 0.779 beats GPT-5.4; GCD counterproductive under Traditional Chinese |
| [[2606.09682]] | AutoMegaKernel: Self-Retargeting Megakernel Synthesis | 整个 LLM 前向编译为单一 CUDA megakernel，静态验证零误判，W8A16 在推理级 GPU 上超越 cuBLAS bf16 / Compiles full LLM forward into one statically-verified CUDA megakernel; W8A16 beats cuBLAS bf16 on inference GPUs |

### Training Stability & Optimization / 训练稳定性与优化（4 篇）

| Paper | Short Title | 一句话描述 / One-line Description |
|:------|:------------|:----------------------------------|
| [[2606.09762]] | Dynamical Isometry for Continual Learning | 把可塑性丧失与 NTK 各向异性恶化联系，提出 AdamO 优化器在监督与 RL 持续学习上匹配或超越 NaP/ReDo / Links plasticity loss to NTK anisotropy; AdamO optimizer matches/beats NaP/ReDo in supervised + RL continual learning |
| [[2606.09410]] | Capacity, Not Format: Structured Reasoning | 把"格式税"重构为容量依赖效应，容量充裕模型无损、逼近极限模型受损严重（Haiku −36.2pp），延迟结构化恢复 80–87% / Reframes format tax as capacity-dependent; spare-capacity models unaffected, capacity-limited lose up to −36.2pp, delayed structure recovers 80–87% |
| [[2606.09658]] | Muon vs Adam: Robust Transferable Features | 从特征质量解释 Muon 优于 Adam，更大 logit margin 与 effective rank，并严格证明等损失下优势 / Explains Muon's superiority via feature quality — larger margin and effective rank, with a theorem proving strict advantage at equal loss |
| [[2606.09734]] | Forward Gradients for Quantum Circuits | 前向自动微分统一参数移位/SPSA/随机坐标下降，固定 V≪N 达参数移位精度，QUIVER 优化器超 iCANS/gCANS / Forward-mode AD unifies parameter-shift/SPSA/RCD; fixed V≪N matches exact gradient, QUIVER beats iCANS/gCANS |

### Model Compression & Quantization / 模型压缩与量化（2 篇）

| Paper | Short Title | 一句话描述 / One-line Description |
|:------|:------------|:----------------------------------|
| [[2606.09012]] | Understanding QAT: River-Valley-Basin Geometry | 用 river-valley-basin 几何解释 QAT：STE 梯度感知陡峭谷壁把量化迭代拉回盆地，2-bit 上 QAT 远超 AdaRound/GPTQ / River-valley-basin geometry explains QAT; STE gradients bias to low-loss basin, QAT far beats AdaRound/GPTQ at W2 |
| [[2606.09508]] | EntropyInfer: Adaptive Long-Context Inference | 无需训练的长上下文加速，按头-段熵自适应分配预算+潜在 KV 压缩，100k+ token 下 2.39× 加速且质量无损 / Training-free long-context speedup via per-head-per-segment entropy budgeting + latent KV compression; 2.39× at >100k tokens, near-lossless |

### Vision & Multimodal / 视觉与多模态（2 篇）

| Paper | Short Title | 一句话描述 / One-line Description |
|:------|:------------|:----------------------------------|
| [[2606.09169]] | IMUG-Bench: Interleaved Understanding & Generation | 面向统一多模态模型多轮交错图文对话的基准（3,113 样本），发现生成侧暴露偏差，CoT 对 BAGEL 提升最大 / 3,113-sample interleaved UMM benchmark; finds exposure bias on generation side, CoT lifts BAGEL +11.8 |
| [[2606.09803]] | Echo-Memory: Memory in Action World Models | 受控比较四类记忆设计，发现原始上下文是强基线、分块状态空间递归开放域返回最强（VLM 69.00），重放保真度≠记住世界 / Controlled memory-design comparison; raw context is strong baseline, block-wise state-space recursion best open-domain return (69.00) |

### Bayesian Methods & Uncertainty / 贝叶斯方法与不确定性（2 篇）

| Paper | Short Title | 一句话描述 / One-line Description |
|:------|:------------|:----------------------------------|
| [[2606.09312]] | Compiler World Models for Tensor Program Search | 把张量调度评估建模为隐状态演化的"世界模型"，同 64-trial 预算下 GPU/CPU 加速 1.37×/1.54× / Casts schedule eval as latent-dynamics world model; 1.37×/1.54× speedup at same 64-trial budget on GPU/CPU |
| [[2606.09664]] | LILBO: In-Context Learning for Latent BO | 针对表格基础模型与分子隐空间分布不匹配，用 BO 感知合成任务继续预训练，8 任务平均排名最佳（2.64 vs 2.94） / Addresses TFM-LSBO mismatch via BO-aware continued pretraining; best avg rank 2.64 vs 2.94 on 8 held-out tasks |

### ML Theory & Foundations / 机器学习理论与基础（1 篇）

| Paper | Short Title | 一句话描述 / One-line Description |
|:------|:------------|:----------------------------------|
| [[2606.09450]] | TheoremBench: LLMs on Theorem Proving | Lean4 经典定理基准（83 父定理、1,142 实例），显式前提使 DeepSeek-Prover-V2 父定理 pass@64 从 0.053 升到 0.263 / Lean4 benchmark of 1,142 instances; explicit premises lift DeepSeek-Prover-V2 parent pass@64 0.053→0.263 |

## All Papers

| # | ID | Title |
|---:|:----|:------|
| 1 | [[2606.08894]] | Are Reasoning Vision-Language Models Robust to Semantic Visual Distractions? |
| 2 | [[2606.08945]] | From Hazard Functions to Language Space: Cox-Supervised Distillation of Survival Risk into a Large Language Model |
| 3 | [[2606.08948]] | NutriMLLM: Multimodal Large Language Models for Dietary Micronutrient Analysis |
| 4 | [[2606.08960]] | Hardening Agent Benchmarks with Adversarial Hacker-Fixer Loops |
| 5 | [[2606.08973]] | A systematic investigation of molecular encoding methods for drug property predictions |
| 6 | [[2606.09005]] | Document-Authored Control-Signal Impersonation: A Low-Cost Indirect Prompt Attack on RAG Safety Boundaries |
| 7 | [[2606.09012]] | Understanding Quantization-Aware Training: Gradients at Quantized Weights Bias to the Low-Loss Basin |
| 8 | [[2606.09028]] | ATM: Action-Consistency Transfer Matrix for Diagnosing and Improving Latent World Models |
| 9 | [[2606.09048]] | BareWave: Waveform-Native Flow-Matching Text-to-Speech |
| 10 | [[2606.09169]] | IMUG-Bench: Benchmarking Unified Multimodal Models on Interleaved Understanding and Generation |
| 11 | [[2606.09189]] | Pretrained, Frozen, Still Leaking: Auditing Cross-Encoder Attribute Transfer in EEG Foundation Models |
| 12 | [[2606.09278]] | Internalizing Geometric Law: Learning from Solver Residuals for Precision-Critical Generation |
| 13 | [[2606.09287]] | Trajectory Geometry of Transformer Representations Across Layers |
| 14 | [[2606.09312]] | Toward Compiler World Models: Learning Latent Dynamics for Efficient Tensor Program Search |
| 15 | [[2606.09327]] | A Universal Dense Football Event Representation Based on TabTransformer |
| 16 | [[2606.09376]] | Precision Is Not Faithfulness: Coverage-Aware Evaluation of Grounded Generation with a Complete Oracle |
| 17 | [[2606.09388]] | Distilling Safe LLM Systems via Soft Prompts for On Device Settings |
| 18 | [[2606.09389]] | LexRubric: A Rubric-Guided Diagnostic Benchmark for Open-Ended Legal Tasks |
| 19 | [[2606.09410]] | Capacity, Not Format: Rethinking Structured Reasoning Failures |
| 20 | [[2606.09411]] | Now You (Still) See Me: Detecting Evasive Steganographic Payloads in LLMs |
| 21 | [[2606.09433]] | Bayesian Selective Latent Inference for Wastewater-First Influenza Monitoring |
| 22 | [[2606.09447]] | AliyunConsoleAgent: Training Web Agents in Real-World Cloud Environments via Distillation and Reinforcement Learning |
| 23 | [[2606.09450]] | TheoremBench: Evaluating LLMs on Theorem Proving in Formal Mathematics |
| 24 | [[2606.09453]] | GD-MIL: Grade-Disentangled Multiple Instance Learning for Multimodal Biochemical Recurrence Prediction in Prostate Cancer |
| 25 | [[2606.09474]] | Training-Free Generalized Few-Shot Segmentation through Open-Vocabulary Semantic Arbitration |
| 26 | [[2606.09495]] | ContextShift: A Controlled Benchmark for Context Dependence in Object Detection |
| 27 | [[2606.09508]] | From Rigid to Dynamic: Entropy-Guided Adaptive Inference for Long-Context LLMs |
| 28 | [[2606.09514]] | BUDDY: BUdget-Driven DYnamic Depth Routing for Adaptive Large Language Model Inference |
| 29 | [[2606.09536]] | Adversarial Attack and Disturbance Detection by Hadamard-Coded Output Representations |
| 30 | [[2606.09541]] | Automating the Expert Eye: A System-Agnostic Deep Learning Framework for Rare Event Discovery in Imbalanced Force Spectroscopy |
| 31 | [[2606.09558]] | Integrating gene regulatory priors into Transformer attention with scTransformer for interpretable scRNA-seq analysis |
| 32 | [[2606.09603]] | Automated IEP Generation from Traditional Chinese Parent-Teacher Interviews via Corpus-Grounded Feature Diffusion |
| 33 | [[2606.09605]] | Next-Token Prediction Learns Generalisable Representations of Sleep Physiology |
| 34 | [[2606.09635]] | Gradient-Guided Reward Optimization for Inference-time Alignment |
| 35 | [[2606.09646]] | Do Video Foundation Models Understand Intuitive Physics? A Layerwise Probing Analysis |
| 36 | [[2606.09653]] | A Unifying Framework for Concept-Based Representational Similarity |
| 37 | [[2606.09658]] | Muon Learns More Robust and Transferable Features than Adam |
| 38 | [[2606.09664]] | In-Context Learning for Latent Space Bayesian Optimization |
| 39 | [[2606.09669]] | SpatialWorld: Benchmarking Interactive Spatial Reasoning of Multimodal Agents in Real-World Tasks |
| 40 | [[2606.09672]] | Correlation Is Not Enough: Embedding Human Metadata for Individual Causal Discovery |
| 41 | [[2606.09682]] | AutoMegaKernel: A Statically-Checked Agent Harness for Self-Retargeting Megakernel Synthesis |
| 42 | [[2606.09697]] | PsychoSafe: Eliciting Psychologically-Informed Refusals in Large Language Models |
| 43 | [[2606.09725]] | Disentanglement with Holographic Reduced Representations |
| 44 | [[2606.09734]] | Adaptive directional gradients for parameterised quantum circuits |
| 45 | [[2606.09735]] | The Neutral Mask: How RLHF Provides Shallow Alignment while Leaving Partisan Structure Intact in a Large Language Model |
| 46 | [[2606.09758]] | Difference-Aware Retrieval Policies for Imitation Learning |
| 47 | [[2606.09762]] | Preserving Plasticity in Continual Learning via Dynamical Isometry |
| 48 | [[2606.09803]] | Echo-Memory: A Controlled Study of Memory in Action World Models |
| 49 | [[2606.09809]] | Evaluation Cards: An Interpretive Layer for AI Evaluation Reporting |
| 50 | [[2606.09816]] | PTL-Diffusion: Manifold-Aware Diffusion with Periodic Terminal Laws |

---
*Generated on 2026-06-08. Total: 50 papers across 12 topics.*
*论文数量验证：目录中有 50 篇 .md 论文文件（不含 overview.md）。匹配：✓*
