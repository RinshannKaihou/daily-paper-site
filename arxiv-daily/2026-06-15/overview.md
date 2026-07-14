---
title: "arXiv Daily — 2026-06-15"
date: 2026-06-15
tags: ["arxiv", "daily", "2026-06-15"]
papers: 50
---

> **覆盖范围 (Coverage):** 50 篇 2026-06-15 抓取的 arXiv 论文摘要，按用户研究兴趣自动筛选与精读。
> 论文按 6 个主题分组：机制可解释性 / 推理评估与可靠性 / 量化与数值精度 / 自演化智能体与自动研究 / 训练稳定性与优化器 / 数学基础与失败模式。
> 主题分类与精读理由见 [[interests|interests.md]]。

## 今日必读 / Must Read Today

### 1. [[2606.14530]] — Code Correctness Signals in LLM Hidden States: Pre-Generation Probing and Repair Geometry

- **理由 / Why:** 在 Qwen3-4B-Instruct-2507 上以同一套残差化工具同时给出"代码正确性在 prompt 末尾隐藏态可线性解码"（50 外层 split 的 leakage-free AUC 0.931±0.008；控制 prompt 长度后仍 0.911±0.010，远高于 prompt-only 基线 0.754）的**正结果**，以及"failed→repair 方向在条件残差化三个修复上下文协变量后被证伪"的**配对负结果**——同工具两用是机制可解释性方法学中少见的诚实示范。
- **Reason:** A single residualization tool produces both a positive pre-generation probe result and an honest negative result on the repair direction; the covariate-balance pre-check before any residualization is itself a reusable template for separating "model feature" from "context correlate" in RepEng work. Open-source, 6 GB single-GPU reproducible.

### 2. [[2606.14589]] — When Errors Become Narratives: A Longitudinal Taxonomy of Silent Failures in a Production LLM Agent Runtime

- **理由 / Why:** 8 周 / 22 起生产事件 / 28 次沉默失败的根因复盘归纳出机制导向的 A–E 五类分类法，命名 *fail-plausible*（LLM 主动把错误信号改写为流畅虚假输出交用户，作为 gray failure 在 LLM 时代的升级），并量化三个反直觉发现：~70% 沉默失败靠人眼而非审计发现；15-incident 回归审计 0% 事前预防 vs 87% 回归拦截；事件潜伏期 13h–60d 跟机制所在层（observational distance）强相关、跟代码复杂度弱相关。
- **Reason:** Coining *fail-plausible* as the LLM-era escalation of gray failure (the observer is "convincingly lied to" by the failure itself) is the kind of vocabulary contribution the agent-reliability field needs. The defense-maturation path (point fix → meta-rule → scanner) with empirical recurrence evidence and the public `openclaw-ontology-engine` PyPI package raise the floor for the field.

### 3. [[2606.14560]] — Free Heavy-Tailed Lunch for Muon: A Theoretical Justification of Empirical Success

- **理由 / Why:** 在重尾（$p \in (1,2]$）非凸随机优化框架下，首次证明 Muon 在核范数 stationarity 下的样本复杂度 $\mathcal{O}\!\left(\min\{m,n\}\,\Delta_1 L\varepsilon^{-2}(\sigma/\varepsilon)^{p/(p-1)}\right)$，比欧氏方法省去一个 $\min\{m,n\}^{(3p-2)/(2(p-1))-1}$ 量级的维度因子，并通过 coupon-collector 构造证明该速率在一阶方法中**严格最优**；70M Pythia + FineWeb-Edu 验证了不同 Schatten-$r$ 几何下的预期性能曲线（$r=1$ 困惑度 88.9 下降到 $r=3$ 时的 34.5 后平台化，与假设的 $p \approx 1.5$ 重尾一致）。
- **Reason:** First first-order optimal sample-complexity guarantee for matrix-valued non-Euclidean optimizers under heavy-tailed noise, with matching lower bounds; the native-Banach-geometry analysis (via Ball–Carlen–Lieb duality + Wenzel's inequality) is the right tool, and the 70M-scale Schatten-$r$ sweep is a direct, falsifiable prediction that matches observation. Bounds the regime where Muon-style spectral updates are provably better than Euclidean.

## 按主题分类 / Papers by Topic

### 主题 1: 机制可解释性与隐藏状态 / Mechanistic Interpretability & Hidden States

| 论文 / Paper | 一句话贡献 / One-line Contribution |
|---|---|
| [[2601.12913]] | 用四条对称性（推理等变 / 信息不变 / 概念闭包不变 / 结构不变）公理化"可解释性"，并把对齐、干预、反事实推理统一为贝叶斯反演 / Four-symmetry Erlangen-Program axiomatization of "interpretability," unifying alignment, intervention, and counterfactuals as Bayesian inversion. |
| [[2601.16407]] | 提出 Jacobian Scopes：在单次反向传播中产出 Semantic / Fisher / Temperature 三种目标无关的 token 级因果归因，AOPC 上 6 模型匹配或超过 Integrated Gradients / Input×Gradient / **机制可解释性 + 推理评估** / Mechanistic interpretability + inference evaluation. |
| [[2605.07984]] | 在 Qwen3/Gemma-3/Llama-3 三个家族 10+ 规模上证明：只有 Gemma-3-27B 真正把押韵对偶补全的因果规划位点从押韵词迁移到换行符，并由 5 个注意力头（L30H4/L28H14/L28H15/L30H5/L28H29）承担，路径补丁恢复 90% 容量 / Latent-planning handoff localized to 5 attention heads in Gemma-3-27B only. |
| [[2606.03085]] | PGB-CT 用软干预 + $1/(1+\ell)$ 度量变换 + $\ell_1 + m(1-m)$ 调度惩罚，把多组件（注意力头+MLP 神经元）因果追踪的组合搜索松弛为连续优化，$\sim$229× 加速 greedy、$\sim$1.76× 加速 top-k / Multi-component causal tracing relaxed to continuous optimization; 229× faster than greedy, matches its metric quality. |
| [[2606.13705]] | 用逐层消融+逐神经元归因定位 Gemma 4 四模型长事实枚举的"重复环"，静态权重编辑消除/大幅减少 loop（E2B 翻转 1 个 L10 神经元×−0.8+放大 1 个 L12 神经元×3.0→0/128；E4B 剥除 3/430,080；31B 剥除 1100/1,290,240；26B 屏蔽 3/3840 专家槽），基准损失≤1.7 pp；但 26B/31B 在长思考预算下仍 doom loop（知识缺失、与通用推理纠缠、不可切除）/ Per-neuron attribution + static weight edits eliminate fast-commit loops across Gemma 4 (1 neuron in E2B, 1100 in 31B); doom loops remain. |
| [[2606.13720]] | 在 5 个开源聊天模型上系统比较 DiM（方向消融/激活加法）与 INLP（零空间投影 $\alpha=1$、反事实翻转 $\alpha=2$）：INLP $\alpha=2$ 与 DiM 方向消融相当、零空间投影偏弱；几何上 $\alpha=1$ 把激活压到聚类之间、$\alpha=2$ 推入对立聚类 / INLP counterfactual flipping matches DiM directional ablation; nullspace projection is consistently weaker. |
| [[2606.14530]] ★ | **Must Read #1** — 配对正/负结果：代码正确性预生成可线性解码（AUC 0.931）但 failed→repair 方向在条件残差化后消失；同工具两用 + 协变量平衡预检的方法论可复用 / Paired positive/negative results: pre-generation correctness linearly decodable (AUC 0.931) but repair direction dissolves after conditional residualization. |
| [[2606.14673]] | 通过证明 Braun et al. (2025) 的压缩计算玩具模型等价于训练 `y=ReLU(x)+Mx` 的单层 MLP（其中 $M = I - W_E W_E^T$），证伪"压缩计算即叠加计算"——超额性能随 $||M||$ 单调变化、神经元集中在 M 的 top-50 特征子空间 / Compressed computation is not superposition; the advantage is driven by the implicit input-mixing matrix M. |
| [[2606.14703]] | 在 Qwen3-VL-8B LM 骨干中识别 100/1152（8.7%）"gaze heads"，其注意力逐 token 跟踪当前描述的图像区域；单一注意力遮罩干预在无重训练下以 83.1% 准确率把生成重定向到任意面板；机制在 2B–32B 规模与 Ovis1.5/Qwen2-VL/InternVL3.5 上复现，但冻结编码器家族（LLaVA/Bunny）失效 / 100 of 1152 attention heads track the described image region; single attention-mask intervention redirects output at 83.1% without retraining. |

### 主题 2: 推理评估与可靠性 / Inference Evaluation & Reliability

| 论文 / Paper | 一句话贡献 / One-line Contribution |
|---|---|
| [[2603.05167]] | C2-Faith 基于 PRM800K 450 条完美链构造受控扰动（已知位置单步因果替换 + d∈{0.1,0.3,0.5,0.7} 删除），评测 GPT-4.1/DeepSeek-V3.1/o4-mini：DeepSeek 检测 94.7% 但 FPR 29.6%，o4-mini 定位最佳（exact 68.0% vs 57.6%/55.8%），所有裁判在 70% 删除时覆盖度均分仍约 3.0（GT 2.17）/ Controlled perturbations reveal a detection-localization gap (26–33 pp) and systematic coverage overestimation across 3 frontier judges. |
| [[2606.00947]] | 命名联邦基础模型个性化（FedFMP）中的"沉默失败"——六类失败（偏差放大/置信度错配/公平性崩溃/适配错位/OOD 退化/对齐侵蚀）由 FL 的隐私架构结构性不可观测 / "Silent Failures" in FedFMP — six failure modes structurally invisible to current FL evaluators. |
| [[2606.13221]] | Soft-Elo 在不修改 BT 模型的前提下用裁判打分差映射的校准软胜率（ỹ=σ(β·s)）替代硬标签，并叠加 split conformal；8 个开源裁判 × LMArena 55 留出模型平均 Elo MAE 45.9→17.9（−61%），conformal 区间宽度收窄 39–70%、覆盖率 92.1–96.4%（vs 90% 标称）/ Soft-Elo replaces hard BT labels with calibrated win probabilities + split conformal; 45.9→17.9 Elo MAE, 39–70% narrower intervals at matched coverage. |
| [[2606.13392]] | MSA：在 GQA 上挂超轻量 Index Branch（每 GQA 组独立选 Top-16 块、B_k=128、固定 2048-token 预算）+ Main Branch block-sparse attention，用 KL 对齐损失+梯度截断+warmup 稳定训练；109B MoE 多模态上与 Full-Attention 持平、1M context 下 FLOPs 降 28.4×、H800 prefill 14.2×/decoding 7.6× 加速 / Per-GQA-group Top-16 block selection + co-designed kernels; 28.4× FLOPs, 14.2×/7.6× wall-clock on 109B at 1M context. |
| [[2606.13685]] | 10,080 判定重复试验：LLM 裁判平均 13.6% 成对偏好翻转率、72% 首位置偏好、$\kappa=0.51$ 跨裁判一致性；11 次重复即可恢复 50 次参考 95% 保真度 / Four-layer reliability framework; 11 trials needed for 95% majority-vote consensus fidelity. |
| [[2606.13870]] | Mirage Probes：VLM 的"无图也能答"行为在 Ovis2.5-2B 与 Qwen3-32B-VL 上线性可解码；PHI 指标 + 跨基准分离性差异区分"虚假图像"与"文本偏置"两种内部表征机制 / Linear decodability of "answer without image" splits into spurious-image vs. textual-bias mechanisms. |
| [[2606.14117]] | 把隐性联想测验（IAT）改造为 JSON 强制选择 + 两阶段贝叶斯分层模型（先建模格式遵从、再建模任务一致性），证明联想干扰是**模型特异**而非 LLM 普遍属性 / Forced-choice IAT + two-stage Bayesian model isolates compliance from interference; Claude shows clear effect, GPT-5 essentially null. |
| [[2606.14516]] | EEE：首个社区治理的 AI 评测 JSON Schema 与 Hugging Face 仓库，覆盖 22,235 模型 × 2,273 基准 × 31 种格式；四项实证用例（成本-准确率权衡、困惑度规范差异、HELM 复现性审计、IRT 元分析）/ Community-governed JSON schema unifying 31 eval formats across 22k models. |
| [[2606.14589]] ★ | **Must Read #2** — 22 起 / 28 次生产沉默失败事件，机制导向五类分类法 + *fail-plausible* 概念 + 70%/0%/13h–60d 三个反直觉量化发现 / Five-class mechanism-oriented taxonomy of silent failures with *fail-plausible* coined. |
| [[2606.14629]] | "好验证器也能害你"：验证器驱动的 VLM 自 DPO 在目标任务 rubric 准确率处于次阈值区间时会静默反向优化学生（−3.4 到 −10.9 pp），且越自信越错伤害越大 / Verifier-driven self-DPO silently regresses when verifier rubric accuracy is sub-threshold; more confident-but-wrong does the most damage. |

### 主题 3: 量化与数值精度 / Quantization & Numerical Precision

| 论文 / Paper | 一句话贡献 / One-line Contribution |
|---|---|
| [[2506.17255]] | UltraSketchLLM 用低估型 AbsMaxMin 多行数据草图把 LLM 权重压到 0.5 bit，并通过将草图算子重写为矩阵乘法实现最高 14.9× 解压加速；Llama-3.1-8B 压后在 12 GB RTX 3080 Ti 可跑 / Sub-1-bit LLM compression with hardware-friendly matrix-form sketch operator; 14.9× decompression speedup. |
| [[2602.03120]] | QES（Quantized Evolution Strategies）在量化离散权重空间内做零阶微调，Delta-Sigma 调制风格的累积误差反馈 + 状态回放重建残差使优化器状态显存 ≈29.7 KB，匹配低精度推理显存；GSM8K 64.14 → 82.64% on Llama-3.1-8B INT4 / Zeroth-order fine-tuning in discrete weight space with Delta-Sigma error feedback; 29.7 KB optimizer state. |
| [[2603.10444]] | Averis 把 FP4 训练中激活极端值的根因诊断为"秩一均值偏置"，通过显式分解均值与残差独立量化，把 NVFP4 的 BF16 loss gap 从 NVIDIA Hadamard 的 2.05%/1.10% 降到 1.19%/0.81% / Rank-one mean bias diagnosis for FP4 outliers; mean-residual splitting cuts NVFP4 loss gap by ~42% relative to Hadamard. |
| [[2606.12280]] | 在 Ampere RTX 3090 上为 Ideogram 4.0 双分支流匹配 DiT 设计 INT8 W8A8 + SmoothQuant + 选择性 bf16 保护（17 层 ≈ 8% linears）配方；CLIP/PickScore 与 FP8 不可区分，LPIPS 0.243 是 8/4-bit 变体中最佳 / INT8 W8A8 PTQ of 9.3B dual-branch DiT for consumer GPU; protection dominates smoothing. |
| [[2606.13054]] | TWLA：E2M-ATQ（欧氏→流形非对称三值化器）+ KOTMS（Kronecker 正交三峰整形 Cayley 参数化）+ ILA-AMP（相邻层二阶交互 + DP 精确求解激活比特分配），在 W1.58A4 上 3.64× over FP16、1.3× over QuaRot W2A4 on LLaMA-2-13B / First PTQ route to W1.58A4; 3.64× over FP16. |
| [[2606.13300]] | TQS（Trajectory-based Quantization Sensitivity Score）将 PTQ 重新建模为离散时间动力系统的稳定性问题，基于有限时 Lyapunov 增长率的零数据/零二阶/零梯度敏感度评分；在 Aurora/TimesFM-2.5/Pangu-Weather 上把准确率-压缩 Pareto 边界大幅前推、发现 I/O 边界（而非 FFN-down）是时序基础模型最敏感层 / PTQ as discrete-time dynamical-system stability; I/O boundary is the most sensitive layer in forecasting transformers, contrary to LLM-PTQ priors. |
| [[2606.14598]] ★ | **Must Read candidate** — 诊断并修复"假 INT8"：消费级 Ampere 上现有 INT8 推理只把权重/激活量化再 dequant 回 bf16；融合 Triton `int8×int8→int32` GEMM（per-token × per-channel 反量化 + bias 折入 epilogue + 36 配置 autotune）在 RTX 3090 上单算子 2.8–4.2× over bf16、4–8× over unfused，1024px 单卡 156.49s 出图胜过双卡 FP8 / Diagnoses fake-quant INT8 and ships a fused Triton kernel; 2.8–4.2× over bf16 on consumer Ampere. |

### 主题 4: 自演化智能体与自动研究 / Self-Evolving Agents & Automated Research

| 论文 / Paper | 一句话贡献 / One-line Contribution |
|---|---|
| [[2601.22436]] | 在 4 个自演化框架 × 10 LLM 骨干 × 9 环境的受控因果干预下，证明 LLM 智能体高度忠实于原始轨迹但对压缩经验基本不忠实——self-distillation 的前提被系统证伪 / Causal interventions show agents are faithful to raw experience but largely unfaithful to condensed experience, even when condensed is the only input. |
| [[2606.03108]] | EvoTrainer：把"训练侧诊断脚手架"（指标/分析器/回测/可复用技能）作为可进化对象，与 LLM 策略协同进化；SWE-rebench-9B 38.16% BC% 超过人类调参 RL 基线 33.77%（p<0.001），Git 历史泄露的伪提升被脚手架审计捕获 / Co-evolution of policy and training-side diagnostic harness; SWE-9B 38.16 vs 33.77 BC%. |
| [[2606.13662]] | EurekAgent 把自主科学发现的瓶颈从"工作流设计"转向"环境工程"，通过权限/产物/预算/人在回路四轴 + Claude Code + GLM-5.1 在 26 圆 packing (2.635999)、Erdős (0.380870)、1st autocorr (1.502861) 三道数学题、TriMul kernel、MLE-Bench 7 题同时刷新 SOTA，单题 <$11 / Shifts bottleneck from workflow to environment engineering; 3/3 math SOTA with open GLM-5.1 at <$11. |
| [[2606.13710]] | HOTE（Hybrid Open-Ended Tri-Evolution）以 GRPO 在"工具使用 + 无工具"双模式协同进化提议者/求解者/评判者；8B HOTE 平均 59.1 超过 DR Tulu-8B-RL (56.0) 与 Tongyi DeepResearch-30B-A3B (51.2)，且 1200→1500 步仍上升 / GRPO-based tri-role co-evolution with hybrid tool-use modes; HOTE-8B 59.1 avg, still rising at 1500 steps. |
| [[2606.14202]] | MeEvo 把"自然进化（种群级交叉变异）"与"元认知进化（基于共享历史的反思）"组织为两层交替循环；DeepSeek-V4-Flash + MIMO-v2.5-Pro 下在 5 个优化问题上 7/8 Mann-Whitney U 检验显著，复杂约束问题（ACS、WSN）相对 MeLA 提升 1.79–16.87% / Dual-layer AHD with natural + metacognitive evolution alternating; statistically significant on 7/8 comparisons. |
| [[2606.14368]] | OPCoD：两个 LLM 互为师生 + on-policy rollout + 双向自然语言反馈；cognizance-based gating（切断低质反馈污染路径）+ feedback anchoring（规则匹配概念标签 + 剥离泄露答案）；SciKnowEval 三组配对任务全部实现 mutual Pareto 改进 / Bidirectional on-policy co-distillation; all 3 SciKnowEval pairs achieve mutual Pareto improvement. |
| [[2606.14470]] | GitOfThoughts：把智能体推理树保存为 git 仓库（commit=思维节点、note=分数、tag=结果、branch=路径、git log=检索）；预注册 5 底座 × 2 基准 × 2 模型的对照实验显示：只有 self-consistency 显著超过无记忆基线（+3.4 pp @ n=500），记忆仅在 cos ≥ 0.85 "copyability threshold" 以上通过答案检索带来收益 / Git-as-substrate for reasoning tree; only self-consistency significantly beats no-memory baseline. |
| [[2606.14476]] | "GNN 复读机"：ReAct 智能体调用冻结 GCN 在 ogbn-arxiv 上与 GNN 输出一致率 0.976–0.992；能力越强顺从越多（0.5B 无法调用 → 7B 0.98），且顺从代价不随能力下降（per-node oracle 间隙 0.12–0.22）/ LLM agent defers to GNN tool 97.6–99.2% of the time; deference grows with capability. |
| [[2606.14502]] | 综述：把 LLM 演进刻画为"认知核心（Chatbot → Thinking LLM）× 工具执行（Agent → OpenClaw）"的二维演化，"Workspace + Skill"是从瞬时对话转向持久数字同事的核心机制 / Survey: two-dimensional framework of LLM evolution with "Workspace + Skill" as the persistence mechanism. |
| [[2606.14574]] | SIMMER：77 动作 / 262 物体 ≈ 46,800 种交互的符号厨房世界模型揭示 LLM 规划中的"潜在失败"（执行不报错却悄悄破坏目标甚至不可逆）；6 LLM 上 < 17% 计划无错、29–56% 含潜在失败；反事实前瞻模拟可降潜在失败最多 72% / Symbolic kitchen world model surfaces latent failures; 29–56% of plans contain latent failures. |
| [[2606.14581]] | CARE：把 LLM 限定为"挑战者策略"提议者（用 Python 排序函数表达），由仅依赖公开证据的"干预门"决定是否覆盖传统 BO 现任动作；Minerva/Olympus 80.0 → 88.5、ChemLex 83.9 → 92.1，LLM 后端可换为 Gemini-2.5-Flash 不影响结论 / CARE auditable controller separates proposal generation from action authority; gate authorizes 52/300 and 36/300 actions. |
| [[2606.14674]] | AgentSpec：把具身智能体解耦为带类型接口的 Perception–Memory–Reasoning–Reflection–Action 循环 + 可选 RL；4 基准 × 多 backbone 受控消融证明：性能由 scaffold 兼容性与模块交互主导，且 GRPO/SUPO 训练的策略只有在训练时引入与部署一致的"scaffold-like"上下文才能与推理+记忆模块良好组合 / Modular spec for embodied agents; interaction effects dominate; RL must be trained with deployment scaffold. |

### 主题 5: 训练稳定性与优化器 / Training Stability & Optimizers

| 论文 / Paper | 一句话贡献 / One-line Contribution |
|---|---|
| [[2606.13867]] | Muon$^p$ 用分数次谱幂 $US^pV^\top$（$p\in(0,1)$，默认 $p=1/3$）替代 Muon 的极化因子；Schatten-$q$ 范数下证明是最陡下降方向（Theorem 2.1）；bivariate 奇多项式递推保留 bf16 数值稳定 + Muon 速度；微调 Llama3-1B/3B 一致优于 Muon 与 AdamW，但**对预训练反而不利** / Muon with fractional spectral powers: best for finetuning, worse for pretraining. |
| [[2606.14187]] | Zeta 用卡方均匀性检验诊断 Muon 动量矩阵的坐标尺度异质性（p 值普遍<0.05），提出"先坐标白化（G̃=M/√V）再谱白化（NS K=5）"的严格顺序双白化，理论证明该顺序改善条件数、严格降低正交化误差；Qwen3-1.7B/8B 收敛 1.67×/1.25× over AdamW、12 基准均分 26.29%（+1.00 over Muon）、每步开销近 AdamW / Dual-whitening (coordinate→spectral) for Muon; chi-square diagnosis + Theorem 2 condition-number bound; 1.67×/1.25× speedup at near-AdamW cost. |
| [[2606.14560]] ★ | **Must Read #3** — 重尾（$p\in(1,2]$）非凸随机优化下，Muon 在核范数 stationarity 达到 $\mathcal{O}\!\left(\min\{m,n\}\,\Delta_1 L\varepsilon^{-2}(\sigma/\varepsilon)^{p/(p-1)}\right)$ 样本复杂度，比 stationarity-corrected 欧氏方法省去 $\min\{m,n\}^{(3p-2)/(2(p-1))-1}$ 维因子，并通过 coupon-collector 构造证明该速率在一阶方法中**严格最优** / First-order optimal sample complexity for matrix-valued non-Euclidean optimizers under heavy-tailed noise. |

### 主题 6: 数学基础与失败模式 / Mathematical Foundations & Failure Modes

| 论文 / Paper | 一句话贡献 / One-line Contribution |
|---|---|
| [[2605.16077]] | ⚠️ **Tangential** — LLM 数据增强（Hugging Face + GPT-5 风格迁移）用于日语小样本 HDS 量表回归；不在用户主线方向，仅作"语言模型评估"参考 / LLM data augmentation for clinical speech assessment — tangential to primary interests. |
| [[2605.23277]] | ⚠️ **Out of scope** — 海洋环流诊断（平流-晃动-跨等密度面三分量分解）；不在用户研究方向 / Ocean overturning diagnostic — out of scope. |
| [[2606.12360]] | 提出以 SAE / 探针为基础的 post-training pipeline：对偏好数据做 concept-level 审计，识别 chosen vs rejected 响应的 latent concept 差异，并把这些差异统一为四种"explain away"干预（data filtering / inoculation prompting / activation steering / reward shaping） / Interpretability-driven post-training; four "explain-away" interventions unified as Bayesian inversion. |
| [[2606.13732]] | 证明在数据孤岛 / verifier 只能看到本地有偏参考的低资源场景下，递归合成数据训练中的样本选择机制会从"防坍缩"变成"加速坍缩"，以幂律速率抹去多样性；初步缓解为 Wasserstein 测地插值 + Wasserstein 重心 / Siloed verifier makes selection drive collapse, not cure it; power-law diversity decay. |
| [[2606.13796]] | 理论证明在完美分数估计下，递归训练扩散模型因反向 SDE 提前截断几何收敛到唯一闭式极限分布 $p^\star_\infty$（数据分布的无限几何平滑混合），并在 Hermite 基下证明其低通滤波效应 / First asymptotic fixed-point characterization of recursive diffusion collapse; truncation is the sole driver. |
| [[2606.13862]] | SuperThoughts 通过 Compressor 把相邻 CoT token 对融合为单一潜在向量 + Main + MTP 联合解码两个 token + 基于 MTP 置信度的自适应回退；Qwen2.5-Math 1.5B/7B/14B 上 20–35% 链长压缩（wall-clock 节省 21–28%）且精度损失 ≤ 2 pp / Compresses CoT token pairs into superposed embeddings; 20–35% length reduction at ≤2 pp accuracy drop. |
| [[2606.14398]] | 用"句法模板 + 有限键值字典"的离散语言模型，严格证明单层 MoE Transformer 可把不同任务的查询路由到**唯一**任务专属专家，专家容量只取决于任务本身（模板+字典）大小；WikiData5M 派生数据上 CE+Router 损失产生清晰"一任务一专家"分配 / Discrete theoretical model of MoE task routing; expert capacity bounded by task complexity. |
| [[2606.14533]] | 严格证明 PCA 在保留 > 99.9999% 方差时可完全擦除稀有事件信号（"Risk Shadow"），并提出三种尾部风险敏感替代（TP-PCA / ExPCA / exp2PCA），其中 exp2PCA 直接优化下游决策的 $\tau$-expectile 风险，在 10 个真实高风险数据集上将操作风险降低至原方案的 1/6 以下 / Variance-based dimensionality reduction is structurally blind to rare events; exp2PCA dominates by 4–13× on 10 datasets. |
| [[2606.14688]] | 把"生成有价值的数学"建模为嵌套式 *language generation in the limit*，证明完美的证明核对器**无法替代品味**；核心结果——在 *tight family* 上覆盖率在"有限 trivia"与"无限 trivia"两个计数层级间发生尖锐相变（$\alpha/2$ vs $1-\alpha/2$） / Verification is not taste: phase transition in trivia count; $\alpha/2$ vs $1-\alpha/2$ sharp dichotomy. |

## All Papers

| ID | Wiki-Link | 主题 | 一句话贡献（中）/ One-line Contribution (英) |
|---|---|---|---|
| 2506.17255 | [[2506.17255]] | Quant | UltraSketchLLM 用低估型 AbsMaxMin 多行数据草图把 LLM 权重压到 0.5 bit；矩阵算子重写实现 14.9× 解压加速 / Sub-1-bit LLM compression with matrix-form sketch operator. |
| 2601.12913 | [[2601.12913]] | Interp | 用四条对称性公理化"可解释性"，统一对齐/干预/反事实推理为贝叶斯反演 / Four-symmetry axiomatization of interpretability; alignment/intervention/counterfactual as Bayesian inversion. |
| 2601.16407 | [[2601.16407]] | Interp | Jacobian Scopes 在单次反向传播中产出 Semantic/Fisher/Temperature 三种 token 级因果归因 / Vector-Jacobian-product attribution with three principled projection directions. |
| 2601.22436 | [[2601.22436]] | Agents | 智能体高度忠实于原始轨迹但对压缩经验基本不忠实（4 框架 × 10 骨干 × 9 环境因果干预）/ Agents faithful to raw experience but unfaithful to condensed experience. |
| 2602.03120 | [[2602.03120]] | Quant | QES 在量化离散权重空间内做零阶微调，Delta-Sigma 调制使优化器状态 ≈29.7 KB，匹配低精度推理显存 / Zeroth-order finetuning with Delta-Sigma error feedback. |
| 2603.05167 | [[2603.05167]] | Eval | C2-Faith 基于 PRM800K 受控扰动评测 3 裁判：DeepSeek 检测 94.7% 但 FPR 29.6%，o4-mini 定位最佳 68.0%，所有裁判 70% 删除时覆盖度均分仍≈3.0 / Controlled CoT-faithfulness benchmark; detection-localization gap + coverage overestimation. |
| 2603.10444 | [[2603.10444]] | Quant | Averis 诊断 FP4 训练中激活极端值根因为"秩一均值偏置"，均值-残差分解独立量化把 NVFP4 loss gap 从 Hadamard 2.05% 降到 1.19% / Rank-one mean bias diagnosis for FP4 outliers. |
| 2605.07984 | [[2605.07984]] | Interp | 只有 Gemma-3-27B 真正把押韵对偶补全的因果规划位点从押韵词迁移到换行符；5 个注意力头承担此"表征接力" / Latent planning handoff localized to 5 attention heads in Gemma-3-27B. |
| 2605.16077 | [[2605.16077]] | Other | ⚠️ Tangential — LLM 数据增强用于日语小样本 HDS 量表回归 / LLM data augmentation for clinical speech assessment. |
| 2605.23277 | [[2605.23277]] | Other | ⚠️ Out of scope — 海洋环流诊断（平流-晃动-跨等密度面三分量分解）/ Ocean overturning diagnostic. |
| 2606.00947 | [[2606.00947]] | Eval | 命名 FedFMP 中的"沉默失败"——六类失败由 FL 隐私架构结构性不可观测 / "Silent Failures" in FedFMP: six modes structurally invisible to current FL evaluators. |
| 2606.03085 | [[2606.03085]] | Interp | PGB-CT 用软干预 + 度量变换 + 调度惩罚把多组件因果追踪松弛为连续优化，229× 加速 greedy / Multi-component causal tracing relaxed to continuous optimization. |
| 2606.03108 | [[2606.03108]] | Agents | EvoTrainer 把训练侧诊断脚手架作为可进化对象；SWE-rebench-9B 38.16% BC%（+4.39 over 人类调参 RL）/ Co-evolution of policy and training-side diagnostic harness. |
| 2606.12280 | [[2606.12280]] | Quant | Ideogram 4.0 INT8 W8A8 PTQ + SmoothQuant + 选择性 bf16 保护（17 层 ≈ 8% linears）；CLIP/PickScore 与 FP8 不可区分 / INT8 W8A8 PTQ for 9.3B DiT on consumer GPU. |
| 2606.12360 | [[2606.12360]] | Other | SAE/探针驱动的 post-training pipeline：四种 "explain away" 干预统一为贝叶斯反演 / Interpretability-driven post-training: four "explain-away" interventions. |
| 2606.13054 | [[2606.13054]] | Quant | TWLA：E2M-ATQ + KOTMS + ILA-AMP 在 W1.58A4 上 3.64× over FP16、1.3× over QuaRot W2A4 / First PTQ route to W1.58A4. |
| 2606.13221 | [[2606.13221]] | Eval | Soft-Elo 用校准软胜率替代 BT 硬标签 + split conformal；8 裁判 × LMArena 55 留出模型 Elo MAE 45.9→17.9，区间收窄 39–70% / Soft-Elo: calibrated BT soft labels + conformal intervals; 45.9→17.9 Elo MAE. |
| 2606.13300 | [[2606.13300]] | Quant | TQS 将 PTQ 重新建模为离散时间动力系统稳定性问题；时序基础模型的 I/O 边界比 FFN-down 更敏感 / PTQ as discrete-time dynamical-system stability. |
| 2606.13392 | [[2606.13392]] | Eval | MSA：GQA 上挂 Index Branch（每 GQA 组选 Top-16 块、固定 2048-token 预算）+ 协同设计内核；109B MoE 多模态 1M context FLOPs 降 28.4×、H800 prefill 14.2×/decoding 7.6× / Block-sparse attention with co-designed kernels; 28.4× FLOPs, 14.2×/7.6× on 109B. |
| 2606.13662 | [[2606.13662]] | Agents | EurekAgent 把瓶颈从工作流设计转向环境工程；3/3 数学 SOTA + TriMul kernel SOTA，单题 <$11 / Environment engineering replaces workflow design. |
| 2606.13685 | [[2606.13685]] | Eval | 10,080 判定重复试验：13.6% 翻转率、72% 首位置偏好、$\kappa=0.51$；11 次重复恢复 50 次参考 95% 保真度 / Four-layer LLM-judge reliability framework. |
| 2606.13705 | [[2606.13705]] | Interp | Gemma 4 四模型权重手术消除枚举 loop（E2B 翻转 1 神经元→0/128；31B 剥除 1100/1.29M 神经元→0/64），基准≤1.7 pp；但 26B/31B 长 budget 仍 doom loop / Per-neuron weight edits eliminate fast-commit loops on Gemma 4; doom loops persist. |
| 2606.13710 | [[2606.13710]] | Agents | HOTE 双模式 GRPO 协同进化提议者/求解者/评判者；8B 59.1 avg，仍在 1500 步上升 / Hybrid Open-Ended Tri-Evolution with GRPO. |
| 2606.13720 | [[2606.13720]] | Interp | INLP $\alpha=2$（反事实翻转）与 DiM 方向消融相当；$\alpha=1$（零空间投影）偏弱；几何上把激活压到聚类之间 vs 推入对立聚类 / INLP vs DiM on refusal. |
| 2606.13732 | [[2606.13732]] | Other | 数据孤岛下样本选择从防坍缩变成加速坍缩，以幂律速率抹去多样性；Wasserstein 测地 + 重心作缓解 / Siloed selection drives model collapse. |
| 2606.13796 | [[2606.13796]] | Other | 递归训练扩散模型因反向 SDE 提前截断几何收敛到唯一闭式极限分布，Hermite 谱下低通滤波 / Asymptotic fixed point of recursive diffusion collapse. |
| 2606.13862 | [[2606.13862]] | Other | SuperThoughts 融合相邻 CoT token 对为单一潜在向量 + MTP 解码两个 token；20–35% 链长压缩、wall-clock 节省 21–28% / Compresses CoT token pairs. |
| 2606.13867 | [[2606.13867]] | Train | Muon$^p$ 用分数次谱幂 $US^pV^\top$（$p=1/3$）推广 Muon；微调一致优于 Muon 与 AdamW，但**对预训练反而不利** / Muon with fractional spectral powers. |
| 2606.13870 | [[2606.13870]] | Eval | Mirage Probes 揭示 VLM "无图也能答"行为在两开源 VLM 上线性可解码；PHI 区分"虚假图像"与"文本偏置"两机制 / VLM "answer without image" is linearly decodable. |
| 2606.14117 | [[2606.14117]] | Eval | IAT 改造为 JSON 强制选择 + 两阶段贝叶斯模型；联想干扰是**模型特异**而非 LLM 普遍属性 / Forced-choice IAT + two-stage Bayesian model. |
| 2606.14187 | [[2606.14187]] | Train | Zeta 卡方检验诊断 Muon 动量尺度异质性，提出"先坐标白化再谱白化"严格顺序，理论证明改善条件数；1.7B/8B 收敛 1.67×/1.25× over AdamW / Dual-whitening (coordinate→spectral) Muon variant; 1.67×/1.25× speedup. |
| 2606.14202 | [[2606.14202]] | Agents | MeEvo 双层 AHD：自然进化 + 元认知进化交替；7/8 Mann-Whitney U 检验显著，ACS/WSN 相对 MeLA +1.79–16.87% / Dual-layer AHD with natural + metacognitive evolution. |
| 2606.14368 | [[2606.14368]] | Agents | OPCoD 双向互教 + cognizance gating + feedback anchoring；SciKnowEval 三组配对任务全部 mutual Pareto 改进 / Bidirectional on-policy co-distillation. |
| 2606.14398 | [[2606.14398]] | Other | 离散语言模型下严格证明单层 MoE 可把不同任务路由到唯一任务专属专家；专家容量只取决于任务本身大小 / MoE task routing theory. |
| 2606.14470 | [[2606.14470]] | Agents | GitOfThoughts 把推理树保存为 git 仓库；预注册实验显示记忆仅在 cos ≥ 0.85 "copyability threshold" 以上通过答案检索带来收益 / Git-as-substrate for reasoning tree. |
| 2606.14476 | [[2606.14476]] | Agents | "GNN 复读机"：ReAct 智能体与冻结 GCN 输出一致率 0.976–0.992；能力越强顺从越多 / LLM agent defers to GNN tool 97.6–99.2%. |
| 2606.14502 | [[2606.14502]] | Agents | 综述：LLM 演进的"认知核心 × 工具执行"二维框架；"Workspace + Skill"是持久数字同事核心 / Two-dimensional framework of LLM evolution. |
| 2606.14516 | [[2606.14516]] | Eval | EEE：首个社区治理的 AI 评测 JSON Schema，覆盖 22,235 模型 × 2,273 基准 × 31 种格式 / Community-governed AI eval JSON schema. |
| 2606.14530 | [[2606.14530]] | Interp ★ | 配对正/负结果：代码正确性预生成可线性解码（AUC 0.931）但 failed→repair 方向在条件残差化后消失 / Paired positive/negative results on pre-generation probe + repair direction. |
| 2606.14533 | [[2606.14533]] | Other | PCA "Risk Shadow"：保留 > 99.9999% 方差时完全擦除稀有事件信号；exp2PCA 在 10 真实数据集上 4–13× 降尾部风险 / Variance-based DR blind to rare events. |
| 2606.14560 | [[2606.14560]] | Train ★ | Muon 在重尾 $p\in(1,2]$ 下的最优样本复杂度（核范数 stationarity），省去欧氏方法 $\min\{m,n\}^{(3p-2)/(2(p-1))-1}$ 维因子 / First-order optimal sample complexity for Muon. |
| 2606.14574 | [[2606.14574]] | Agents | SIMMER：符号厨房世界模型揭示 LLM 规划"潜在失败"；< 17% 计划无错、29–56% 含潜在失败 / Symbolic kitchen world model for latent failures. |
| 2606.14581 | [[2606.14581]] | Agents | CARE 把 LLM 限定为挑战者策略提议者，公开证据门决定是否覆盖传统 BO；Minerva 80.0→88.5、ChemLex 83.9→92.1 / Auditable controller with public-evidence gate. |
| 2606.14589 | [[2606.14589]] | Eval ★ | 22 起生产沉默失败事件 → 机制导向五类分类法 + *fail-plausible*；70%/0%/13h–60d 三个反直觉量化发现 / Five-class taxonomy with *fail-plausible* coined. |
| 2606.14598 | [[2606.14598]] | Quant | 诊断并修复"假 INT8"：融合 Triton `int8×int8→int32` GEMM 在 RTX 3090 上 2.8–4.2× over bf16、1024px 单卡 156.49s 出图 / Diagnoses fake-quant INT8, ships fused Triton kernel. |
| 2606.14629 | [[2606.14629]] | Eval | 验证器驱动的 VLM 自 DPO 在目标 rubric 次阈值区间静默反向优化学生（−3.4 到 −10.9 pp）；越自信越错伤害越大 / Verifier-driven self-DPO silent regression. |
| 2606.14673 | [[2606.14673]] | Interp | Braun et al. (2025) 的"压缩计算"玩具模型等价于训练 `y=ReLU(x)+Mx` 的单层 MLP；超额性能随 $||M||$ 单调变化 / Compressed computation is not superposition. |
| 2606.14674 | [[2606.14674]] | Agents | AgentSpec：具身智能体的带类型接口模块化规范；性能由 scaffold 兼容性与模块交互主导；RL 训练需与部署 scaffold 一致 / Modular spec for embodied agents. |
| 2606.14688 | [[2606.14688]] | Other | 把"生成有价值的数学"建模为嵌套 LGitL；证明核对器**无法替代品味**；trivia 计数相变 $\alpha/2$ vs $1-\alpha/2$ / Verification is not taste. |
| 2606.14703 | [[2606.14703]] | Interp | 100/1152（8.7%）VLM 注意力头逐 token 跟踪当前描述的图像区域；单一注意力遮罩干预在无重训练下以 83.1% 准确率重定向生成 / Gaze heads steer VLM without retraining. |

---

> **备注 / Notes:**
> - `★` 标记今日 Must Read 论文（共 3 篇）。
> - 主题列简写：`Interp` = 机制可解释性与隐藏状态；`Eval` = 推理评估与可靠性；`Quant` = 量化与数值精度；`Agents` = 自演化智能体与自动研究；`Train` = 训练稳定性与优化器；`Other` = 数学基础与失败模式（含 ⚠️ Tangential/Out-of-scope 标记的 2 篇）。
> - 论文数量核对：50 篇（与 `arxiv-daily/2026-06-15/` 目录下的 `.md` 文件数一致，不含 `overview.md`）。
