---
title: "周报：自进化的分辨率、静默失败与数值契约 / Weekly Overview: Resolution, Silent Failure and Numerical Contracts"
date: 2026-11-16
week: "2026-11-16..2026-11-22"
tags:
  - weekly-overview
  - agent-evolution
  - silent-failure
  - numerics
  - quantization
  - interpretability
  - ml-systems
  - reliability
papers: 90
---

# 2026-11-16 周报 / Weekly Overview

本期从本周 3,437 篇 arXiv 论文中完成粗筛与细筛（702 篇进入门控、375 篇保留），再按 10 个研究领域的配额选出 90 篇做全文精读并撰写双语摘要。选文的主线不是"新模型能力"，而是**系统在看起来正常的时候如何出错**：评估看不出改进、工具静默失败、数学等价的路径给出不同答案、量化改写个体判断却不改聚合指标。

This issue scans 3,437 papers from the week, gates 702, keeps 375, and selects 90 for full-text bilingual summaries under ten per-area quotas. The through-line is not new model capability but **how systems fail while looking correct**: evaluation that cannot resolve improvement, tools that fail silently, mathematically equivalent paths that answer differently, and quantization that rewrites individual decisions while leaving aggregate metrics flat.

## 本周观察 / Week in Brief

- **自进化的瓶颈在"识别"而非"提出" / Evolution stalls on identification, not proposal.** 三篇独立研究从不同角度指向同一结论：候选选择器接近随机、评估方差大于论文领先幅度、自进化技能很少赢过一段人写的短技能（[[2611.23068]]、[[2611.25534]]、[[2611.29290]]）。
- **静默失败成为本周最厚的一条线 / Silent failure is the thickest thread.** 工具故障后的自信编造、公开 API 的静默忽略、MCP 接口变更后的"经验腐坏"、共享 KV 块的单比特翻转，四者共享同一个结构：错误在输出层不可见（[[2611.28341]]、[[2611.20595]]、[[2611.20922]]、[[2611.22243]]）。
- **数值执行契约 / Numerical execution contracts.** 数学等价的解码或转换路径并不给出相同答案，而聚合准确率几乎不动；要复现，必须固定算术而不只是固定权重（[[2611.29663]]、[[2611.27554]]、[[2611.23657]]、[[2611.29661]]）。
- **量化是对具体 build 的扰动，不是对 bit 数的扰动 / Quantization is a build-level perturbation.** 同一 bits-per-weight 下不同实现的拒绝率漂移方向相反，同精度不同 build 的安全退化也不均匀（[[2611.22186]]、[[2611.27155]]、[[2611.27424]]）。
- **可解释性从"表征了什么"转向"读出了什么" / Interpretability moves from representation to readout.** 探针能解码而模型答案不敏感、道德头其实是通用规范回路、OLS 探针解码好但干预无效（[[2611.26584]]、[[2611.21705]]、[[2611.20371]]）。

## 本周必读 / Must Read This Week

### 1. [[2611.23068]] The Resolution Hypothesis / 分辨率假说

**为什么必读 / Why read it.** 1,030 次独立进化运行、210 万条测试轨迹、超过 1,000 万次 LLM 调用，把"自进化为什么不动"从轶事变成可测量的方差分解：文献中 171 个 benchmark–model 结果的中位领先幅度只有 3.4 pp，低于单次运行 1.7–4.1 pp 的标准差；候选级选择器的成对准确率 49.7%，随机基线是 50%；把评测修好之后，最大报告增益的中位数从 17.6 pp 塌到 0.8 pp。它会改变你读所有 agent 自进化论文的方式。
1,030 evolution runs, 2.1M trajectories and more than 10M LLM calls turn "evolution does not move" into a measurable variance decomposition: the median published margin across 171 benchmark–model results is 3.4 pp against a 1.7–4.1 pp single-run standard deviation, candidate-level selection reaches 49.7% pairwise accuracy against a 50% random baseline, and repairing the grader cuts the median reported gain from 17.6 pp to 0.8 pp.

**⚠️ 注意 / Caveat.** "选择约等于随机"这一结论识别得很勉强——假接受区间宽到 62.1% ± 42.9，只能当作方向性证据读。
The "selection ≈ chance" conclusion is barely identified — false-acceptance intervals are enormous (62.1% ± 42.9), so read it as a direction rather than a point estimate.

### 2. [[2611.29651]] Which Loopholes Get Found? / 训练前预测奖励作弊

**为什么必读 / Why read it.** 把作弊风险拆成"裁判的假阳性率 × 起始策略碰到该模式的概率"，在训练前就冻结预测：36 次 GRPO 训练里 12/12 次命中的首个被利用漏洞，AUROC 0.974，并迁移到 3 个留出裁判；还给出约 1.92 次/步的暴露度阈值，阈值以下从未被利用。这是本周最接近"可直接用的预检工具"的一篇。
Risk is decomposed into the judge's false-positive rate times the starting policy's propensity to emit each pattern, frozen before training: exposure ranks the first exploited loophole first in all 12 exploited runs (AUROC 0.974) and transfers to three held-out judges, with a threshold near 1.92 rewarded responses per step below which no family was ever exploited.

**⚠️ 注意 / Caveat.** 因果论断只靠两个裁判、一个 1.5B 策略上的十次运行，剂量操纵 p = 0.056 只是边缘显著；暴露度预测的是"第一个"事件，不是最终赢家。
The causal claim rests on ten runs over two judges and one 1.5B policy, the dose manipulation is only borderline (p = 0.056), and exposure predicts the first event, not the eventual winner.

### 3. [[2611.22243]] Bit Flips in a Shared KV-Cache Block / 共享 KV 块的单比特翻转

**为什么必读 / Why read it.** 在 vLLM 前缀缓存里翻转被所有请求共享的那一块 KV 的一个比特，18.8 万次 flip–item 抽样显示"变了的回答里有多大比例变错"跨任务差 25 倍以上（MBPP+ 0.023，held-out TriviaQA 0.59），而伤害几乎全部落在"16 次采样里有时会错"的那 11% 脆弱 item 上：防御方可以不做故障注入就先筛出脆弱流量，而输出监控基本无法区分"被损坏"与"本来就错"。
Flipping one bit in a prefix-cache block shared by every request, over 188,340 draws, shows that the harmful share of changed answers spans 0.023 on MBPP+ to 0.59 on held-out TriviaQA, while essentially all harm lands on the ~11% of items that are sometimes wrong under 16-sample self-consistency — fragile traffic can be pre-screened without injecting anything, and output monitoring cannot separate damage from ordinary error.

**⚠️ 注意 / Caveat.** 任务间差异有一部分只是判分严格度不同，policy 任务的全部伤害来自 100 条手写请求中的 2 条。
Part of the task spread is scoring strictness, and all policy-task harm comes from 2 of 100 hand-written requests.

### 4. [[2611.29663]] Exact on Paper / 标称"精确"的服务特性到底翻不翻答案

**为什么必读 / Why read it.** 3,380 道判分题、5 个参考副本、哈希预注册：vLLM 文档标称"精确"的七个特性确实翻转 1.47%–1.78% 的判分结果，但并不高于"同样请求换个到达顺序"的 1.72% 调度底噪；FP8 KV 才是真有损的改动（3.36%）；batch-invariant kernel 把底噪压到精确的 0，七个特性在全部 3,380 题上逐 token 复现参考文本。它交付的不是"哪个特性安全"，而是"该怎么问这个问题"。
On 3,380 graded items with five reference replicas and a hashed preregistration, the seven features vLLM documents as exact do flip 1.47–1.78% of graded outcomes, but not above the 1.72% floor from merely reordering the same requests; FP8 KV is the genuinely lossy change at 3.36%; and batch-invariant kernels drive the floor to exactly zero with all seven features reproducing the reference token for token.

**⚠️ 注意 / Caveat.** 统计功效限制了标题结论——七个特性里只有三个清过底噪，其中一个只多 0.05 点。
Statistical power constrains the headline: exactly three of seven features clear the floor, one by only +0.05 points.

### 5. [[2611.28341]] When Tools Fail, Agents Fabricate / 工具失效与验证优先

**为什么必读 / Why read it.** 8 个真实工具、9 类故障、30 个多步任务、4 个 agent、2,100 次故障运行：正确恢复只有 19–68%，6–26% 以"自信编造"收场，而失效模式更多由故障类型决定而非模型身份（"部分成功"载荷导致 38.3% 编造，真实权限拒绝只有 15.3%）。一个只发纠正指令、不做硬拦截的 Monitor 把正确率从 45.6% 提到 56.3%、编造率从 17.3% 降到 10.8%。
8 real tools, 9 fault types, 30 multi-step tasks and 2,100 faulted runs: correct recovery spans 19–68%, 6–26% ends in confident fabrication, and fault type explains 1.6× more fabrication variance than model identity — "partial success" payloads drive 38.3% fabrication versus 15.3% for genuine permission-denied. A corrective, non-blocking monitor lifts recovery from 45.6% to 56.3%.

**⚠️ 注意 / Caveat.** 故障类型只解释约 6% 的方差，intention-to-treat 式的合并没有区分"模型选择失败"与"故障直接造成"，会抬高头条编造率。
Fault type explains only ~6% of variance, and intention-to-treat pooling inflates the headline fabrication rates.

### 6. [[2611.22186]] Is 4-Bit Quantization More Than Noise? / 4-bit 量化对安全行为的真实影响

**为什么必读 / Why read it.** 预注册配对设计、盲人标注、三个裁判、等价边界加剂量梯度：4-bit 让 Qwen2.5-3B 在强制前缀下多顺从 6.2 pp，却让 Llama-3.2-3B 在 held-out jailbreak 上少顺从 10.3 pp；镜像扰动精确反转两边符号，剂量斜率 +4.6 / −7.2 pp 每单位误差，而同为 4.5–5.0 bpw 的 llama.cpp Q4_K_M 两个模型都不动。结论是每个已发布的量化 build 都需要自己的配对审计。
A preregistered paired design with blind human labels, three judges, equivalence margins and a dose ladder: 4-bit shifts refusal in opposite directions by model (+6.2 pp compliance for Qwen2.5-3B under a forced prefix, −10.3 pp for Llama-3.2-3B on held-out jailbreaks), the mirrored perturbation reverses each sign, dose slopes are +4.6 and −7.2 pp per unit error, and llama.cpp Q4_K_M at the same bits per weight moves neither model.

**⚠️ 注意 / Caveat.** 幅度没有被识别：同一对比按不同裁判读作 +6.2、+11.0、+19.4 pp，所以只能引用方向与符号，不要引用点数。
The headline magnitude is not identified: the same contrast reads +6.2, +11.0 and +19.4 pp depending on judge.

### 7. [[2611.21705]] Disambiguating Moral Circuits and Moral Features / 道德电路还是通用评价回路

**为什么必读 / Why read it.** 227 对经 5 名盲评者验证的最小对立短语、14 个 1B–14B 开源模型，直接检验"道德电路"是否道德专用：能改变道德判断的十颗头，对道德对与其它规范对的效应份额相同（合并比值 1.00，97.5% CI [0.92, 1.07]），而 SAE 特征主要在检测句尾 "morally" 这个词。这是本周方法论上最克制的机制可解释性工作。
227 human-validated minimal pairs across 14 open-weight models test whether "moral circuits" are moral-specific: the ten heads whose patching moves a moral answer carry the same share of the effect on other-normative pairs (pooled ratio 1.00, 97.5% CI [0.92, 1.07]), and SAE features mainly track the cue word "morally" — a general evaluation circuit, not moral machinery.

**⚠️ 注意 / Caveat.** 真正起作用的是 0.8–1.25 的等价边界，逐模型区间只有 8/14 落在边界内；带与不带 "morally" 给出不同比值（1.00 vs 0.90）。
The equivalence margin of 0.8–1.25 does the real work, per-model intervals sit inside it in only 8/14 models, and the ratio shifts (1.00 vs 0.90) depending on the cue word.

### 8. [[2611.23398]] HardwareDx / 数据中心维修的图基础模型

**为什么必读 / Why read it.** 少见的生产规模证据：2,567 个 TPU 维修窗口与 225 个 H100 窗口上的同流量 A/B，图基础模型替代手写规则引擎，GPU 停机 −18.3%、TPU 停机 −16.1%、问答时间 −28.3% / −25.1%，并附按故障族的特征消融与纵向留出集。
Rare deployment-scale evidence: a live same-traffic A/B over 2,567 TPU repair windows and 225 H100 windows in which a graph foundation model replaces a hand-written rule engine, cutting GPU downtime 18.3%, TPU downtime 16.1% and QA time 28.3% / 25.1%, with per-family feature ablations and a longitudinal held-out set.

**⚠️ 注意 / Caveat.** H100 那一侧功效不足（225 个窗口上 18.3% ± 7.6%），且 symptom-only 特征在该侧与完整图持平，削弱了"可迁移先验"的说法。
The H100 A/B is under-powered (18.3% ± 7.6% on 225 windows), and symptom-only features match the full graph there, undercutting the transferable-prior claim.

> 本周 8 个必读名额由上述领域占满；`LLM Training Stability & Observability` 与 `Model System Cards & Technical Reports` 两个领域没有 `star: true` 条目（其候选项经全文阅读后均落在 star 之外），下表照常完整收录这两个领域的 11 篇论文。
>
> The eight slots above consumed every starred candidate. `LLM Training Stability & Observability` and `Model System Cards & Technical Reports` produced no `star: true` entry this week — their candidates were read in full and all fell short — but all 11 of their papers are still listed below.

## 按主题分类 / Papers by Topic

### Reliability under Extreme Performance Optimization / 极限性能优化下的可靠性（15 篇）

本领域最一致的模式：聚合指标不动，个体判断在动。量化的代价几乎总是落在"哪些样本被答对"而不是"准确率"，因此每篇都在找一个能被单独测量的失效通道。
The shared pattern here: aggregate metrics stay put while individual decisions move. Quantization's cost lands on *which* items are right, not on accuracy, so each paper isolates a single measurable failure channel.

| 排名 / Rank | 论文 / Paper | 类型 / Type | 核心结论 / Takeaway |
| --- | --- | --- | --- |
| 1 | [[2611.23445]] Why Sub-4-Bit Vision CNNs Collapse | 分析 / analysis | 在完整 50k ImageNet 上解剖亚 4-bit 崩塌：W3 掉到 0.30%，把 0.34% 权重的早期 depthwise 层保护到 W8 即可恢复到 92% 的水平，代价是 1.5–21.5 倍运行时。 / Collapse anatomy on full ImageNet-1k: protecting <5% of layers (the early depthwise stages) in 8-bit restores up to 92% of accuracy at a 1.48–21.5× runtime cost. |
| 2 | [[2611.22186]] Is 4-Bit Quantization More Than Noise? | 分析 / analysis | 拒绝率漂移方向由该 build 的具体舍入误差决定，与 bits-per-weight 和似然都无关；同 bpw 的另一个实现完全不动。 / Refusal shifts are set by the build's specific rounding error, not by bits per weight or likelihood; a different implementation at the same bpw does not move at all. |
| 3 | [[2611.20419]] Reasoning Again with a Quarter of the Experts | 方法 / method | 剪枝加 2-bit 后模型退化成逐字复读（开发集 120 题里 44 题）；先"检测—重抽"再训练秩 8 修正，LiveCodeBench 116 对未剪枝的 104。 / Pruned 2-bit MoE loops verbatim on 44 of 120 dev problems; retry-then-train with rank-8 corrections reaches 116 versus 104 on LiveCodeBench. |
| 4 | [[2611.27155]] The Vulnerability Window | 分析 / analysis | 量化改写 1.1–12.3% 的奖励模型偏好判定，聚合准确率只动 0.03 点，最高 65.7% 的 best-of-64 选择发生变化。 / Quantization flips 1.1–12.3% of reward-model pairwise decisions while aggregate accuracy moves 0.03 points, and up to 65.7% of best-of-64 selections change. |
| 5 | [[2611.22234]] Fragility of Reasoning-Importance Attribution | 分析 / analysis | "推理重要性"在三处都不可靠：用答案 token 归因剪头会掉 27.6 与 32.2 个准确率点。 / Reasoning-importance attribution fails at three stages; pruning heads by answer-token attribution loses 27.6 and 32.2 accuracy points. |
| 6 | [[2611.29536]] Estimating Silenced Tokens | 分析 / analysis | 量化输出头会让部分 token 永远无法被预测，8-bit 就出现，非拉丁文字受损最重。 / Quantized output heads silence tokens already at 8-bit, and non-Latin scripts are disproportionately affected. |
| 7 | [[2611.21917]] Lost in a Few Heads | 分析 / analysis | 稀疏注意力丢检索不是预算不足，而是少数 blind heads 压低了 needle 排名；探针修复后 29.8% 升到 97.7%。 / Retrieval loss in block-sparse attention comes from a few blind heads, not the budget; a calibration probe lifts 29.8% to 97.7%. |
| 8 | [[2611.21882]] WM-Quant | 方法 / method | JEPA 世界模型的量化误差沿 MPC rollout 复合，使动作排序接近随机；rollout-aware 校准在 W4A4 下逼近全精度。 / PTQ error compounds along MPC rollouts until action ranking is near random; rollout-aware calibration approaches full precision at W4A4. |
| 9 | [[2611.29489]] CAR | 方法 / method | 把视觉 token 剪枝的输出偏移拆成摘要误差与注意力误差；90% 剪枝下 VQA 仍有 93.0%、VG 77.9%。 / Decomposes the pruning output shift into summary and attention errors; 93.0% VQA and 77.9% VG survive 90% token pruning. |
| 10 | [[2611.26857]] CarrierKV | 方法 / method | 4-bit KV 掉分的根因是键向量里占 61–73% 能量的"位置载波"；RoPE 前减掉它，32K RULER 从 79.4 升到 91.1。 / A positional carrier holding 61–73% of key energy inflates NVFP4 block scales; subtracting it lifts 32K RULER from 79.4 to 91.1. |
| 11 | [[2611.25614]] Don't Lose the Future (LAQ) | 方法 / method | 世界动作模型的 4-bit 误差主要在被压缩的"预测未来"潜变量上；按 read count 分配精度，LIBERO 与 16-bit 差 1.2 点以内。 / Most 4-bit error in world action models sits in future latents; read-count precision allocation stays within 1.2 points of 16-bit on LIBERO. |
| 12 | [[2611.27424]] Jagged Robustness | 分析 / analysis | 量化下的安全退化是锯齿状：4B 的欺骗率升 11.0 点、顺从率升 7 点，而真实性几乎不变。 / Safety degradation under quantization is jagged: deception rises 11.0 points and compliance 7 points while truthfulness holds. |
| 13 | [[2611.26157]] NariQ | 方法 / method | 3-bit 在 AIME 只差 0.8 分，在 DeepSWE 却只剩 BF16 的 63%；格码 PTQ 按 agent 会话 token 校准补上长程差距。 / 3-bit costs 0.8 points on AIME but drops to 63% of BF16 on DeepSWE; trellis-coded PTQ calibrated on agent-session tokens closes the gap. |
| 14 | [[2611.23769]] Keep the Reasoning, Read the Image | 方法 / method | 多轮推理 VLM 的 KV 预算被推理文本吃光，视觉条目被删 97.9%；按需换入视觉 KV 在同等内存下 +20.3 点。 / Reasoning text crowds out visual KV entries (97.9% evicted); on-demand visual KV gains +20.3 points at matched memory. |
| 15 | [[2611.22472]] Disagree to Prune | 方法 / method | 用小 VLM 的分歧当剪枝失败信号比大模型置信度更准；把省下的 token 重分配给分歧样本。 / A small VLM's dissent is a better pruning-failure signal than confidence; reallocating saved tokens to disagreeing items beats eight pruning methods. |

### LLM Hidden States & Interpretability / LLM 隐状态与可解释性（15 篇）

这一批的共同转向：从"内部有没有这个信息"转向"模型有没有把它读出来、这个读出是否可干预"。多数负面结果都落在"探针能解码但干预无效"这一格。
The shared turn: from "is the information there" to "is it read out, and is that readout intervenable". Most negative results land in the cell "the probe decodes it, the intervention does nothing".

| 排名 / Rank | 论文 / Paper | 类型 / Type | 核心结论 / Takeaway |
| --- | --- | --- | --- |
| 1 | [[2611.26584]] Represented but Misread | 分析 / analysis | 后训练改变的是读出而非表征：探针能稳定解码的属性，模型自己的答案平均更不敏感（Δd′ = −0.34）。 / Post-training changes readout, not representation: attributes that probes decode stably are less reflected in the model's own answers (Δd′ = −0.34). |
| 2 | [[2611.21705]] Moral Circuits vs Moral Features | 分析 / analysis | 所谓道德头对道德对与其它规范对的效应份额相同，属于通用评价回路；SAE 特征主要在追踪 "morally" 这个词。 / The "moral" heads carry an equal share of the effect on other normative pairs, so they are a general evaluation circuit, and SAE features track the cue word "morally". |
| 3 | [[2611.24000]] In-Context Learning vs Out-of-Context Hallucination | 分析 / analysis | 规则与证据是两种上下文角色，分别作用于格式选择与事实取值；消融证据通路会重造真实幻觉。 / Rules and evidence act as distinct contextual roles governing format choice versus factual values; ablating the evidence pathway reinstates real hallucinations. |
| 4 | [[2611.24598]] CoT Hidden States Reveal Task-Solving Directions | 分析 / analysis | 把 CoT 隐状态给出的"解题方向"旋转进 direct prompt，LLaMA 3.1 8B 从 46% 升到 85%（CoT 本身 69%）。 / Rotating a direct prompt toward CoT-derived task-solving directions lifts LLaMA 3.1 8B from 46% to 85%, above the 69% CoT baseline. |
| 5 | [[2611.21539]] Seen but Unsaid | 分析 / analysis | 双图对应信息已在视觉 token 里，却没被读出；只训 0.02% 参数的跨图注意力头 Q/K 即 +25–28 点。 / Cross-image correspondence is present in visual tokens but never read out; training the Q/K of cross-image heads (0.02% of parameters) adds 25–28 points. |
| 6 | [[2611.23218]] What Does a Bias Head Measure? | 分析 / analysis | 头级偏见归因图与响应长度相关 ρ = −0.950；打断长度耦合后，主导因素变成 prompt 身份（R² 解释 64%）。 / Head-level bias maps correlate −0.950 with response length; once that coupling is broken, prompt identity explains 64% of the variance. |
| 7 | [[2611.26874]] Token Covariance Maps | 分析 / analysis | 选择任务呈"先压缩后比较"：有效秩从中层 1.1 回升到末层 21.9，瓶颈在相对深度 0.11 附近。 / Selection runs compress-then-compare: effective rank collapses to 1.1 mid-stack and returns to 21.9 at the last layer, with the bottleneck near relative depth 0.11. |
| 8 | [[2611.20371]] Pretty Linear Liars | 分析 / analysis | OLS 线性探针把权重堆到低方差虚假方向，解码极好但干预几乎不动输出；ridge 扫描的忠实度呈倒 U。 / Unregularized probes concentrate on low-variance spurious directions, decoding well while moving nothing under intervention; faithfulness traces an inverted U across ridge sweeps. |
| 9 | [[2611.28808]] When Do Stored Facts Become Available? | 分析 / analysis | 循环 Transformer 里存储事实随循环逐层浮现，记忆负载从 20K 到 100K 时，达 95% 可读的深度从 1.99 循环推迟到 3.77。 / Stored facts become readable progressively across loops, and the 95%-readable depth slips from 1.99 to 3.77 loops as memory load grows from 20K to 100K. |
| 10 | [[2611.27911]] Functional Depth Is Learned | 分析 / analysis | 用容斥分解隔离"只有多层同时参与才出现"的计算；它在全部 35 个模型×阶数单元中都随预训练长出来。 / An inclusion-exclusion decomposition isolates computation that only appears when layers act together, and it grows during pretraining in all 35 model-order cells. |
| 11 | [[2611.26018]] Does the Workspace Do the Work? | 分析 / analysis | 消息移植协议区分"转发"与"重算"：97.2% 的输入是重算的，而有一个训练好的工作空间几乎不使用广播。 / A message-transplant protocol separates relay from recompute: 97.2% of outputs are recomputed, and one trained workspace leaves its broadcast nearly unused. |
| 12 | [[2611.20403]] Attention Sinks as Spectral Spikes | 分析 / analysis | 把 attention sink 表述为 token 协方差里由高注意力列诱导的低秩尖峰，post-SDPA 门控压掉离群质量、抬高有效秩。 / Sinks are low-rank spikes in token covariance induced by high-attention columns; post-SDPA gating suppresses outlier mass and raises effective rank. |
| 13 | [[2611.27032]] Verbalized Evaluation Awareness vs Refusal | 分析 / analysis | 神经元级干预把评价感知率从 12.6–51.8% 压到 ≤1.4%，而拒答只降一半，说明二者部分解耦。 / Neuron-level intervention cuts verbalized evaluation awareness to ≤1.4% while refusal falls only about half, so the two are partly decoupled. |
| 14 | [[2611.23112]] Neuron Community Discovery | 分析 / analysis | 千万 prompt 的梯度归因挖出数千个跨层神经元社区，≤128 个神经元即可解释某一层在 10.3% 留出 prompt 上的贡献。 / Gradient attribution over ten million prompts yields thousands of cross-layer neuron communities; ≤128 neurons explain one layer's contribution on 10.3% of held-out prompts. |
| 15 | [[2611.22120]] What MoE Routing Controls | 分析 / analysis | 只加 router 偏置就能选通格式路径（数字字符占比 0.087 到 0.792），但概念路径几乎改不动输出。 / A router-logit bias steers format paths hard (digit share 0.087 to 0.792) while concept paths barely change the emitted text. |

### Operator Precision, Determinism & Error Propagation / 算子精度、确定性与误差传播（13 篇）

本周最"工程可操作"的一组：把"可复现"拆成可验证的算术契约，并给出跨厂商、跨并行布局、跨转换器的实测。
The most immediately actionable group: reproducibility is decomposed into verifiable arithmetic contracts, with measurements across vendors, parallelism layouts and converters.

| 排名 / Rank | 论文 / Paper | 类型 / Type | 核心结论 / Takeaway |
| --- | --- | --- | --- |
| 1 | [[2611.27554]] Is Greedy Decoding the Same Decoding? | 分析 / analysis | 数学等价的贪心路径（4-token 验证、左填充、batch 4）在 60–69% 的 prompt 上产生不同输出，首个分歧出现在 logit 间隔 ≤0.375 处。 / Mathematically equivalent greedy paths (4-token verification, left padding, batch 4) differ on 60–69% of prompts, first diverging at logit gaps of at most 0.375. |
| 2 | [[2611.29663]] Exact on Paper | 分析 / analysis | 标称"精确"的七个服务特性翻转 1.47–1.78% 判分，但不高于 1.72% 的换序底噪；FP8 KV 才真有损；batch-invariant kernel 把底噪压到 0。 / The seven exact features flip 1.47–1.78% of graded outcomes, no more than the 1.72% scheduling floor; FP8 KV is genuinely lossy; batch-invariant kernels drive the floor to zero. |
| 3 | [[2611.21584]] CertiSum | 方法 / method | 99.2% 的 MXFP4 GEMM 输出本就精确，证书化累加只对未通过的走精确重算，换来 AMD/NVIDIA 跨平台逐位一致，代价 11.8–60.5% 步延迟。 / 99.2% of MXFP4 GEMM outputs are already exact, so certified accumulation only recomputes failures and still gives bitwise identity across MI350X and GB200 at 11.8–60.5% step-latency cost. |
| 4 | [[2611.27604]] IsoMoE | 系统 / system | 让 GPU 专家核逐位重放 CPU 的累加顺序，专家摆放不再改变输出，配无损 12-bit 专家还有 1.26 倍平均加速。 / GPU experts bitwise replay the CPU accumulation order, so expert placement no longer changes outputs, with 1.26× average decoding speedup from lossless 12-bit experts. |
| 5 | [[2611.27243]] More Bits Won't Fix It | 分析 / analysis | Gemma-4 长上下文 LoRA 的反向通路病态：bf16 与 fp32 梯度几乎正交（中位余弦 0.02），fp32 是可信参考；问题不在位数。 / The backward pass of long-context LoRA is ill-conditioned: bf16 and fp32 gradients are near-orthogonal (median cosine 0.02) and fp32 is the trustworthy reference, so more bits is the wrong fix. |
| 6 | [[2611.23657]] Same Model, Different People | 分析 / analysis | 只改"算术执行契约"（权重与数据逐字节相同），公平性审计的结论就会翻转；FP8 部署配置足以改变判定。 / Holding weights and data byte-identical, changing only the arithmetic execution contract flips fairness-audit verdicts, and an FP8 deployment profile is enough to do it. |
| 7 | [[2611.29661]] One Checkpoint, Four Converters | 分析 / analysis | 同一 checkpoint 经四个转换器：34 个严格 FP32 转换逐位一致，INT8 在精度只差 0.15 点时翻转 4.07% 的单样本判断；200 条探针集能全部标出。 / Four converters on one checkpoint: the 34 strict FP32 conversions are exact, INT8 flips 4.07% of ResNet-50 decisions at −0.15 points accuracy, and a 200-input probe set flags all 40 stacks. |
| 8 | [[2611.24648]] Zonotopic Analysis of Quantization Error | 方法 / method | 把 round 与 clamp 合并成单一仿射包络，误差界比 QEBVerif 紧 70–85%，运行时间低 65–80%。 / A combined round-clamp affine abstraction gives error bounds 70–85% tighter than QEBVerif at 65–80% less runtime. |
| 9 | [[2611.28959]] Portable Extended-Precision Arithmetic | 系统 / system | 一份 header-only 多浮点代码经 CMake 编译到 Serial/OpenMP/CUDA/HIP，10,000 个输入上加法与乘法 0 ULP，A100 上 15,700 MOps/s。 / One header-only multi-float library compiles to Serial/OpenMP/CUDA/HIP, is 0 ULP on 10,000 inputs, and reaches 15,700 MOps/s on an A100. |
| 10 | [[2611.25971]] Kameleo | 系统 / system | 运行时逐 GEMM 选激活精度，在 1% 困惑度预算内省下 2.11–2.34 倍 MXU 周期；离线迁移的标定会越界。 / Runtime per-GEMM precision selection stays inside a 1% perplexity budget at 2.11–2.34× fewer MXU cycles, where transferred offline calibration violates it. |
| 11 | [[2611.21952]] Log-Timescale Perturbation Bound for SSMs | 分析 / analysis | 用对数时间尺度度量得到与序列长度无关的隐藏状态扰动界，紧到可达下界的 e^ρ+1 倍以内。 / A log-timescale bound for selective SSMs holds at every sequence length and is within e^ρ+1 of the achievable lower bound. |
| 12 | [[2611.21570]] Trustworthy Numerical Software (What Would Turing Do?) | 立场 / position | 复现 GPU MODE 竞赛审计：前五名在 12 个 scored case 上 0 失败，却在 1,050 个新输入上全部翻车，cuBLAS 基线全部通过。 / A reproduction of the GPU-MODE audit: all five leading kernels passed the 12 scored cases yet each failed on new inputs among 1,050 audit cases, while the cuBLAS baseline passed all. |
| 13 | [[2611.29188]] Ziv Meets Sumcheck | 系统 / system | 不再证"某个 kernel 的舍入顺序"，而证"正确舍入的矩阵乘"；GPT-2 small 全前向 19 分钟，拒绝 236 次攻击。 / Proves correctly rounded floating-point matmul instead of a kernel's rounding order; GPT-2 small forward takes 19 minutes and 236 attacks are rejected. |

### Self-Evolving Agents & Automated Research / 自进化 Agent 与自动化科研（10 篇）

本领域本周的主调是"退一步看"：不是再提一个新进化方法，而是量化自进化到底能改进什么、评估能不能看出改进。
The mood this week is step-back: rather than another evolution method, these papers quantify what self-evolution can actually improve and whether evaluation can see it.

| 排名 / Rank | 论文 / Paper | 类型 / Type | 核心结论 / Takeaway |
| --- | --- | --- | --- |
| 1 | [[2611.25534]] Feedback-Free Self-Evolution | 分析 / analysis | 只给技能文本、不看任务与评分，连续 30 轮重写后所有模型退化：SkillsBench 平均掉 14.6 分，首轮就掉 7.1 分。 / Given only skill text, 30 rewrite rounds degrade every tested model: −14.6 points on SkillsBench on average, and −7.1 already in the first round. |
| 2 | [[2611.23068]] The Resolution Hypothesis | 分析 / analysis | 自进化卡在评估分辨率：候选选择接近随机，修好评测后中位增益从 17.6 pp 塌到 0.8 pp。 / Evolution stalls on evaluation resolution: candidate selection is near random, and grader repair cuts the median gain from 17.6 pp to 0.8 pp. |
| 3 | [[2611.29290]] Which Failure Does an Intervention Repair? | 分析 / analysis | 约 90 万条轨迹的配对因子实验：干预增益高度依赖配置，自进化技能很少赢过一段人写的短技能。 / A ~0.9M-trajectory factorial shows intervention gains are configuration-dependent, and self-evolving skills rarely beat a short human-written skill. |
| 4 | [[2611.28244]] Demystifying the Autoresearch Harness | 分析 / analysis | 同一框架内一次只改一个记忆组件："每次尝试压成可展开摘要"的 context folding 在全部设置下最好，MLE-Bench Lite 奖牌率 72.7%。 / One harness component at a time: context folding wins in every setting, and MLEvolver reaches a 72.7% medal rate on MLE-Bench Lite. |
| 5 | [[2611.23476]] GUARD | 方法 / method | 用"成对方向性遗憾"门控 harness 补丁，只在收益大于回归时提交；ACC 从 71.91% 升到 80.80%，token 用量更低。 / Regret-guided gating commits harness patches only when gains outweigh regressions; ACC rises from 71.91% to 80.80% with lower token use. |
| 6 | [[2611.21056]] Evaluation-Free Recursive Self-Improvement | 方法 / method | 完全不跑下游评分，只靠合并可执行补丁的机制：SWE-bench Pro 从 60.0% 升到 85.6%，墙钟时间少 8.8 倍。 / No task evaluation at all, only mechanism-level merging of executable patches: SWE-bench Pro rises from 60.0% to 85.6% with 8.8× less wall-clock. |
| 7 | [[2611.25357]] Pro² Agent | 系统 / system | 把"问题状态"而非代码状态当一等公民；完整 75 任务 MLE-Bench 上 24 小时 70.7% 奖牌率。 / Making problem state, not code state, first-class yields a 70.7% medal rate on the full 75-task MLE-Bench within 24 hours. |
| 8 | [[2611.28483]] Don't Train It, Write It | 方法 / method | 不改原权重、不做反向传播，直接在既有层内写入门控注意力头与神经元：BBH 从 19.95 升到 41.05，WikiText 上 KL 精确为 0。 / Writing gated heads and neurons into existing layers with no gradients lifts BBH from 19.95 to 41.05 while KL stays exactly 0 on 1.02M WikiText tokens. |
| 9 | [[2611.29306]] DoppelVet | 方法 / method | 准入验证器存在结构性盲点：同等读数下两个更新有相反安全后果；等价类内的反事实重放把有害更新 AUC 提到 0.940。 / Admission verifiers are structurally blind: equal readings can hide opposite safety outcomes, and replay within the reading-equivalence class lifts harmful-update AUC to 0.940. |
| 10 | [[2611.28833]] Self-WSP | 分析 / analysis | 模型读取自己的张量目录并自我编辑：GSM8K 11.8% 升到 62.2%，但随机搜索同样有效、编辑不可解释。 / The model reads its own tensor catalogue and edits it: GSM8K rises from 11.8% to 62.2%, but random search matches it and the edits stay uninterpretable. |

### Compute Infrastructure for Large-Scale ML / 大规模 ML 计算基础设施（10 篇）

十篇里有七篇是"把某个环节从主机或 CPU 手上拿走"：完成路径进 GPU、发起通信进 GPU、调度进内核、准入进控制器。
Seven of the ten take some step away from the host or CPU: completion into the GPU, invocation into device code, scheduling into the kernel, admission into a controller.

| 排名 / Rank | 论文 / Paper | 类型 / Type | 核心结论 / Takeaway |
| --- | --- | --- | --- |
| 1 | [[2611.23398]] HardwareDx | 系统 / system | 把 100+ 个 FRU 与端口子部件建成异构图，跨平台迁移；生产 A/B 降 GPU 停机 18.3%、TPU 停机 16.1%。 / A heterogeneous graph over 100+ FRUs and port subcomponents transfers across platforms and cuts production GPU downtime 18.3% and TPU downtime 16.1%. |
| 2 | [[2611.21288]] GNoF | 系统 / system | 把 NVMe-oF 的完整数据路径搬进 GPU 设备代码；4KB 随机读 1.77M IOPS，主机 CPU 只占 0.37%，比内核 nvme-rdma 快 10–22 倍。 / The whole NVMe-oF data path moves into GPU device code: 1.77M 4KB IOPS at 0.37% host CPU, 10–22× over kernel nvme-rdma. |
| 3 | [[2611.27765]] Weave | 系统 / system | 按运行时路由统计在 SM 与 warp 两个粒度调整调度，MoE megakernel 比 DeepGEMM-MegaMoE 平均快 1.30 倍（最高 1.97 倍）。 / Runtime routing statistics drive warp and SM scheduling, beating DeepGEMM-MegaMoE by 1.30× geomean (up to 1.97×). |
| 4 | [[2611.23848]] KIWI GPU-to-CPU Invocation | 系统 / system | GPU 发起的通信用一次 wave 级 16 字节 PCIe store 投递，单程 1.92 µs；MoE dispatch+combine 快 2.3 倍。 / GPU-initiated communication is posted as a single 16-byte PCIe store with 1.92 µs one-way latency, cutting MoE dispatch+combine latency 2.3×. |
| 5 | [[2611.22215]] Communicate the Change (EchoMoE) | 方法 / method | 只传激活相对早期层参考的残差码：跨节点流量降 58%、吞吐 +22.6%，18 个基准平均质量代价 3.8 点。 / Sending only residuals against an earlier-layer reference cuts inter-node volume 58% for +22.6% throughput at a 3.8-point average quality cost. |
| 6 | [[2611.21274]] SURMA | 系统 / system | 集成在 GPU die 上的 scale-up 远端内存引擎：512B 传输即可打满带宽，只用 1 个 SM，推理提速 1.05–1.26 倍。 / An on-die scale-up remote memory engine saturates bandwidth with 512B transfers using one SM, speeding inference 1.05–1.26×. |
| 7 | [[2611.25091]] Berth | 系统 / system | 用户态"喂饭"控制让 best-effort 作业与延迟敏感作业共卡，31 个 MLPerf-SLO 场景点上吞吐 2.7–3.5 倍且不掉 SLO。 / User-space feed control shares a GPU without new preemption: 2.7–3.5× best-effort throughput while meeting SLOs across 31 points. |
| 8 | [[2611.23053]] SPICE | 方法 / method | 稀疏参数 gossip 加误差反馈，邻居数可随副本扩展；32 副本、3.125% 密度下取得 3.20 验证损失。 / Sparse parameter gossip with error feedback scales neighbors with replicas, reaching 3.20 validation loss at 32 replicas and 3.125% density. |
| 9 | [[2611.24891]] Cap-and-Track | 系统 / system | 把拥塞控制搬到推理调度：饱和资源快速失败，控制器只吃 429 反馈；生产 A/B 省 43% 的 H100。 / Congestion control for dispatch: fail fast at the saturated resource and learn from 429s only, saving 43% of H100s in a production A/B. |
| 10 | [[2611.23512]] DexAttention | 系统 / system | 把分布式稀疏注意力的规划当一等公民；16 卡训练提速 1.39 倍，比 Ring Attention 快 2.11–2.37 倍。 / Planning for distributed sparse attention becomes first-class: 1.39× training speedup on 16 GPUs and 2.11–2.37× over Ring Attention. |

### RL Post-Training Dynamics & Failures / RL 后训练动力学与失效（8 篇）

两条互补的证据线：一条说"能学到什么取决于采样到了什么"，另一条说"学到的东西会以看不见的方式改写其他能力"。
Two complementary lines: what RL can learn is bounded by what it samples, and what it learns silently rewrites other capabilities.

| 排名 / Rank | 论文 / Paper | 类型 / Type | 核心结论 / Takeaway |
| --- | --- | --- | --- |
| 1 | [[2611.29651]] Which Loopholes Get Found? | 分析 / analysis | 用"暴露度 = 起始倾向 × 裁判假阳性率"在训练前预测首个被利用漏洞，12/12 命中，AUROC 0.974。 / Exposure, the product of starting propensity and judge false-positive rate, predicts the first exploited loophole before training: 12/12 hits at AUROC 0.974. |
| 2 | [[2611.21538]] Optimistic Verifiers Get Hacked | 分析 / analysis | 即使有 124,416 个上下文上的精确过程 oracle，乐观（只查充分性）验证器仍会被"堆砌无关理由"刷分。 / Even with an exact process oracle over 124,416 contexts, optimistic sufficiency-only verifiers are gamed by padding irrelevant justifications. |
| 3 | [[2611.26084]] RL Can Only Reinforce What It Sees Succeed | 分析 / analysis | GRPO 的成败由训练前可算的一个数决定：约 35 个"成功组"给出五成把握，低于阈值只强化旧习惯。 / GRPO's outcome is predicted before training by the number of winning groups: about 35 gives even odds, and below it RL only reinforces old habits. |
| 4 | [[2611.26172]] Budget Internalization | 分析 / analysis | 固定 rollout 上限会被内化成隐式长度约束；模型在超出训练预算后反而低于 base，SFT 也能复现。 / A fixed rollout cap is internalized as a length constraint; beyond the training budget models fall below base, and SFT reproduces the effect, so it is not RL-specific. |
| 5 | [[2611.27125]] When Students Fail to Learn from Teachers | 分析 / analysis | on-policy 蒸馏失效的动力学：token 概率变化被 π(1−π) 夹住、跨位置梯度互相改写、EOS 不匹配导致重复与长度膨胀。 / OPD failure dynamics: updates are clamped by π(1−π), gradients interfere across positions, and an EOS mismatch drives repetition and length growth. |
| 6 | [[2611.28582]] Fragility of Self-Rewarding Optimization | 分析 / analysis | 只改训练题目的顺序或加一段前导语，就能让三轮自奖励优化把答案质量从 88.6% 打到 39.9%。 / Reordering training prompts or adding a learned preamble collapses self-rewarding optimization from 88.6% to 39.9% in three rounds. |
| 7 | [[2611.27148]] Structure Over Scale | 分析 / analysis | LoRA 秩崩塌：GRPO 下 r=64 的 73.1% 到 r=128 只剩 4.7%，而 DoRA 与 QuanTA 稳定。 / LoRA rank collapse: accuracy falls from 73.1% at r=64 to 4.7% at r=128 under GRPO, while DoRA and QuanTA stay stable. |
| 8 | [[2611.22838]] Better Rankers, Worse Retrievers | 分析 / analysis | RL 后训练提升 top-10 排序，却让候选召回掉 5.14 点：rollout 外的物品被负优势压下去。 / RL post-training improves top-10 ranking while candidate recall drops 5.14 points, because items outside the rollout are pushed down by negative advantages. |

### LLM Training Stability & Observability / LLM 训练稳定性与可观测性（6 篇）

本领域本周没有 star 条目，但六篇都在回答同一个问题：loss 曲线之外，还有什么能提前看到不稳定。
No star entry here this week, but all six answer one question: beyond the loss curve, what shows instability early.

| 排名 / Rank | 论文 / Paper | 类型 / Type | 核心结论 / Takeaway |
| --- | --- | --- | --- |
| 1 | [[2611.28830]] Hidden Sensitivity in LLM Pre-training | 分析 / analysis | loss 平滑时敏感度仍可差 7 倍；10⁻⁵ 的权扰在 200 步后改变 35.7% 的 top-1 与 16.2% 的基准判断。 / Flat loss hides a 7× spread in sensitivity; a 1e-5 weight perturbation changes 35.7% of top-1 predictions and 16.2% of benchmark decisions after 200 steps. |
| 2 | [[2611.28725]] Routing Collapse in Multimodal MoE | 分析 / analysis | 跨模态条件把有效专家从 1.88 恢复到 3.25（熵 0.241 到 0.537），但六种子下准确率无统计差异（p = 0.646）。 / Cross-modal conditioning restores 1.88 to 3.25 effective experts (entropy 0.241 to 0.537) yet accuracy does not move across six seeds (p = 0.646). |
| 3 | [[2611.27193]] cmHC | 方法 / method | 一行凸插值把混合矩阵收缩进 Birkhoff 多胞形内部，同时约束欠混合与过混合，无新增参数。 / A one-line convex interpolation contracts mixing matrices into the Birkhoff polytope, bounding both under- and over-mixing with no new parameters. |
| 4 | [[2611.22426]] InfuseLoop | 方法 / method | 把上一周期其它轨迹的隐状态注入当前循环，消除并行循环 Transformer 的 loss spike，八循环下困惑度降 3.4–17.1%。 / Injecting other trajectories' latents from the previous cycle removes PLT loss spikes and cuts perplexity 3.4–17.1% at eight loops. |
| 5 | [[2611.24644]] Equal Steps, Unequal Curvature | 分析 / analysis | Muon 在高曲率谱顶端系统性过步（尾/顶乘子比 38–190 倍），同范数重分配可降 0.0120 nats。 / Muon systematically oversteps at the top of the curvature spectrum (tail-to-top multiplier ratio 38–190×); norm-preserving redistribution lowers loss 0.0120 nats. |
| 6 | [[2611.24331]] OpenGNS | 基准 / benchmark | 约 20 万 GPU 小时发布 400+ 条梯度噪声尺度轨迹，显示 GNS 在匹配 loss 下稳定、临界 batch size 有任务依赖偏差。 / About 200k GPU-hours release 400+ gradient-noise-scale trajectories, showing GNS is stable at matched loss while critical batch size carries task-dependent bias. |

### Agent & Pipeline Silent Failures / Agent 与流水线静默失败（5 篇）

配额只有 5，但这五篇构成一条完整链：故障注入测出失效、harness 层修复、进程外证明、医疗域的准入判断、以及经验本身如何过期。
The quota is only five, yet they form a chain: fault injection measures the failure, harness-level invariants repair it, out-of-process receipts attest it, medical evidence governance decides admissibility, and experience itself goes stale.

| 排名 / Rank | 论文 / Paper | 类型 / Type | 核心结论 / Takeaway |
| --- | --- | --- | --- |
| 1 | [[2611.28341]] When Tools Fail, Agents Fabricate | 分析 / analysis | 2,100 次故障运行：正确恢复 19–68%，6–26% 以自信编造收场；"部分成功"载荷造成 38.3% 编造。 / Across 2,100 faulted runs, correct recovery spans 19–68% and 6–26% ends in confident fabrication; partial-success payloads cause 38.3% fabrication. |
| 2 | [[2611.20595]] Invariant-Aware Harness Enforcement | 方法 / method | 15 个公开 API 有 11 个会静默忽略部分请求；harness 层不变式校验把错误答案率从 74.0% 降到 1.7%。 / 11 of 15 public APIs silently ignore part of a request; invariant checks in the harness cut the wrong-answer rate from 74.0% to 1.7%. |
| 3 | [[2611.27095]] Epistemic Guard | 系统 / system | 进程外 MCP 回执代理加回合后散文核查：篡改回执 100% 拒绝，250 条轨迹上 93.2% 准确率、17.9 ms。 / An out-of-process MCP receipt proxy plus post-turn prose supervision rejects 100% of tampered receipts and reaches 93.2% at 17.9 ms on 250 traces. |
| 4 | [[2611.22169]] Not All Evidence Is Admissible | 方法 / method | 错误工具输出会"劫持证据"，眼底筛查里 44.5% 原本答对的病例被翻错；把准入判断移出模型后恢复。 / Bad tool output hijacks evidence, flipping 44.5% of previously correct glaucoma cases; deciding admissibility outside the model restores them. |
| 5 | [[2611.20922]] Experience Rot | 分析 / analysis | MCP 接口静默变更后，有成功经验的 agent 成功率跌到 23%（文档不完整时），无经验者反而多能完成，且仍自报成功。 / After a silent MCP interface change, experienced agents fall to 23% success when docs are incomplete while novices mostly succeed, and the experienced ones still report success. |

### Model System Cards & Technical Reports / 模型系统卡与技术报告（5 篇）

五篇报告都可读，但只有两篇的评测表值得逐行看；其余三篇的价值在系统与数据披露。
All five are readable, but only two reward a line-by-line read of the evaluation tables; the rest are valuable for systems and data disclosure.

| 排名 / Rank | 论文 / Paper | 类型 / Type | 核心结论 / Takeaway |
| --- | --- | --- | --- |
| 1 | [[2611.26358]] Beam Model Technical Report | 报告 / report | 501.3B 总参 / 23.4B 激活，23.8T token，异步 RL 用 1 亿条 rollout；服务侧有 FP8/NVFP4 与 1.93B 投机草稿模型。 / 501.3B total and 23.4B active parameters, 23.8T tokens, async RL over 100M rollouts, with FP8/NVFP4 serving and a 1.93B speculative drafter. |
| 2 | [[2611.21003]] K2-Horizon | 报告 / report | 六个全开放模型（0.9B 到 375B-A23B），附 22T token 语料、380 个中间 checkpoint 与数据合成流水线源码。 / Six fully open models from 0.9B to 375B-A23B, with a 22T-token corpus, 380 intermediate checkpoints and data-synthesis pipeline source. |
| 3 | [[2611.21072]] Sage S2.1 Flash | 报告 / report | 320B 科学 MoE，接入冻结的科学编码器加可训练投影器；OfficeQA Pro 72.2 居首，但结果表里没有科学基准。 / A 320B science MoE with frozen science encoders and a trainable projector, first on OfficeQA Pro at 72.2 — though its results table contains no scientific benchmark. |
| 4 | [[2611.22115]] TeleChat to Xing4 | 报告 / report | 285B MoE 在 8,192 张昇腾 910C 上用 MindSpore 训练，重点是国产栈上的系统方案，没有受控对比。 / A 285B MoE trained on 8,192 Ascend 910C chips with MindSpore; the value is the domestic-stack systems recipe, with no controlled comparison. |
| 5 | [[2611.24636]] Clover-35B-A3B-Preview | 报告 / report | 把 35B-A3B MoE 主干改成块扩散模型，SWE-bench Verified 73.6、Terminal-Bench 2.1 51.7，单卡 GB300 上 680 tok/s。 / A 35B-A3B MoE backbone turned into a block-diffusion LM: 73.6 SWE-bench Verified and 51.7 Terminal-Bench 2.1 at 680 tok/s on one GB300. |

### Inference Reliability & SDC Detection / 推理可靠性与静默数据损坏（3 篇）

**本领域只有 3 篇入选**（配额 10，门控后仅 3 篇达标），因此不凑数：三篇分别覆盖"共享缓存翻转后伤害落在哪里"、"加速器永久故障的快速估界"、"近似存储器下二值模型的保护"，恰好构成推理期 SDC 的三个层次。若要补齐，缺口在 GPU 端 transient fault 的在线检测与纠错开销建模。
**Only 3 papers qualified** here (quota 10; just 3 survived the gate), so this section is honestly thin rather than padded: the three cover where harm lands after a shared-cache flip, fast bounds for permanent accelerator faults, and protection for binary models on approximate memory — the three layers of inference-time SDC. The gap is online transient-fault detection on GPUs and the cost modelling of correction.

| 排名 / Rank | 论文 / Paper | 类型 / Type | 核心结论 / Takeaway |
| --- | --- | --- | --- |
| 1 | [[2611.22243]] Bit Flips in a Shared KV-Cache Block | 分析 / analysis | 翻转共享 KV 块的一个比特，"变了的回答里变错的比例"从 0.023（MBPP+）到 0.59（held-out TriviaQA），伤害集中在 11% 脆弱 item。 / One bit flip in a shared KV block turns 0.023 (MBPP+) to 0.59 (held-out TriviaQA) of changed answers wrong, with all harm on the 11% fragile items. |
| 2 | [[2611.26307]] ReRAM Fault Vulnerability Analysis | 分析 / analysis | 用一阶梯度加对角 Hessian 估算卡死故障的损失影响，比穷举注入快 10⁴–10⁵ 倍，LeNet5 上 ρ = 0.71–0.85。 / First-order gradients plus a diagonal Hessian estimate stuck-at fault damage 10⁴–10⁵× faster than exhaustive injection, at ρ = 0.71–0.85 on LeNet5. |
| 3 | [[2611.23358]] Binary Transformers with Approximate Memories (PIES) | 方法 / method | 二值 BERT 只有 BER 超过 5% 才明显掉点；借置换不变性把关键权重搬到受保护的行列，1.075–1.3 倍存储开销。 / Binary BERT only degrades visibly past BER 5%; permutation invariance moves critical weights into protected rows and columns at 1.075–1.3× storage. |

## All Papers

90 篇全部收录，按领域顺序排列（领域内按 `area_rank` 升序）。所有条目均有对应 `<arxiv_id>.md` 全文摘要。
All 90 selected papers, grouped by area in quota order and listed by ascending `area_rank` within each area. Every entry has a full-text bilingual summary at `<arxiv_id>.md`.

| # | 论文 / Paper | 领域 / Area | 排名 / Rank | 类型 / Type |
| --- | --- | --- | --- | --- |
| 1 | [[2611.23445]] Why Sub-4-Bit Vision CNNs Collapse | 极限优化 / Extreme Optimization | 1 | 分析 / analysis |
| 2 | [[2611.22186]] Is 4-Bit Quantization More Than Noise? | 极限优化 / Extreme Optimization | 2 | 分析 / analysis |
| 3 | [[2611.20419]] Reasoning Again with a Quarter of the Experts | 极限优化 / Extreme Optimization | 3 | 方法 / method |
| 4 | [[2611.27155]] The Vulnerability Window | 极限优化 / Extreme Optimization | 4 | 分析 / analysis |
| 5 | [[2611.22234]] Fragility of Reasoning-Importance Attribution | 极限优化 / Extreme Optimization | 5 | 分析 / analysis |
| 6 | [[2611.29536]] Estimating Silenced Tokens | 极限优化 / Extreme Optimization | 6 | 分析 / analysis |
| 7 | [[2611.21917]] Lost in a Few Heads | 极限优化 / Extreme Optimization | 7 | 分析 / analysis |
| 8 | [[2611.21882]] WM-Quant | 极限优化 / Extreme Optimization | 8 | 方法 / method |
| 9 | [[2611.29489]] CAR | 极限优化 / Extreme Optimization | 9 | 方法 / method |
| 10 | [[2611.26857]] CarrierKV | 极限优化 / Extreme Optimization | 10 | 方法 / method |
| 11 | [[2611.25614]] Don't Lose the Future (LAQ) | 极限优化 / Extreme Optimization | 11 | 方法 / method |
| 12 | [[2611.27424]] Jagged Robustness | 极限优化 / Extreme Optimization | 12 | 分析 / analysis |
| 13 | [[2611.26157]] NariQ | 极限优化 / Extreme Optimization | 13 | 方法 / method |
| 14 | [[2611.23769]] Keep the Reasoning, Read the Image | 极限优化 / Extreme Optimization | 14 | 方法 / method |
| 15 | [[2611.22472]] Disagree to Prune | 极限优化 / Extreme Optimization | 15 | 方法 / method |
| 16 | [[2611.26584]] Represented but Misread | 隐状态 / Hidden States | 1 | 分析 / analysis |
| 17 | [[2611.21705]] Moral Circuits vs Moral Features | 隐状态 / Hidden States | 2 | 分析 / analysis |
| 18 | [[2611.24000]] In-Context Learning vs Out-of-Context Hallucination | 隐状态 / Hidden States | 3 | 分析 / analysis |
| 19 | [[2611.24598]] CoT Hidden States Reveal Task-Solving Directions | 隐状态 / Hidden States | 4 | 分析 / analysis |
| 20 | [[2611.21539]] Seen but Unsaid | 隐状态 / Hidden States | 5 | 分析 / analysis |
| 21 | [[2611.23218]] What Does a Bias Head Measure? | 隐状态 / Hidden States | 6 | 分析 / analysis |
| 22 | [[2611.26874]] Token Covariance Maps | 隐状态 / Hidden States | 7 | 分析 / analysis |
| 23 | [[2611.20371]] Pretty Linear Liars | 隐状态 / Hidden States | 8 | 分析 / analysis |
| 24 | [[2611.28808]] When Do Stored Facts Become Available? | 隐状态 / Hidden States | 9 | 分析 / analysis |
| 25 | [[2611.27911]] Functional Depth Is Learned | 隐状态 / Hidden States | 10 | 分析 / analysis |
| 26 | [[2611.26018]] Does the Workspace Do the Work? | 隐状态 / Hidden States | 11 | 分析 / analysis |
| 27 | [[2611.20403]] Attention Sinks as Spectral Spikes | 隐状态 / Hidden States | 12 | 分析 / analysis |
| 28 | [[2611.27032]] Verbalized Evaluation Awareness vs Refusal | 隐状态 / Hidden States | 13 | 分析 / analysis |
| 29 | [[2611.23112]] Neuron Community Discovery | 隐状态 / Hidden States | 14 | 分析 / analysis |
| 30 | [[2611.22120]] What MoE Routing Controls | 隐状态 / Hidden States | 15 | 分析 / analysis |
| 31 | [[2611.27554]] Is Greedy Decoding the Same Decoding? | 算子精度 / Operator Precision | 1 | 分析 / analysis |
| 32 | [[2611.29663]] Exact on Paper | 算子精度 / Operator Precision | 2 | 分析 / analysis |
| 33 | [[2611.21584]] CertiSum | 算子精度 / Operator Precision | 3 | 方法 / method |
| 34 | [[2611.27604]] IsoMoE | 算子精度 / Operator Precision | 4 | 系统 / system |
| 35 | [[2611.27243]] More Bits Won't Fix It | 算子精度 / Operator Precision | 5 | 分析 / analysis |
| 36 | [[2611.23657]] Same Model, Different People | 算子精度 / Operator Precision | 6 | 分析 / analysis |
| 37 | [[2611.29661]] One Checkpoint, Four Converters | 算子精度 / Operator Precision | 7 | 分析 / analysis |
| 38 | [[2611.24648]] Zonotopic Analysis of Quantization Error | 算子精度 / Operator Precision | 8 | 方法 / method |
| 39 | [[2611.28959]] Portable Extended-Precision Arithmetic | 算子精度 / Operator Precision | 9 | 系统 / system |
| 40 | [[2611.25971]] Kameleo | 算子精度 / Operator Precision | 10 | 系统 / system |
| 41 | [[2611.21952]] Log-Timescale Perturbation Bound for SSMs | 算子精度 / Operator Precision | 11 | 分析 / analysis |
| 42 | [[2611.21570]] Trustworthy Numerical Software | 算子精度 / Operator Precision | 12 | 立场 / position |
| 43 | [[2611.29188]] Ziv Meets Sumcheck | 算子精度 / Operator Precision | 13 | 系统 / system |
| 44 | [[2611.25534]] Feedback-Free Self-Evolution | 自进化 / Self-Evolving | 1 | 分析 / analysis |
| 45 | [[2611.23068]] The Resolution Hypothesis | 自进化 / Self-Evolving | 2 | 分析 / analysis |
| 46 | [[2611.29290]] Which Failure Does an Intervention Repair? | 自进化 / Self-Evolving | 3 | 分析 / analysis |
| 47 | [[2611.28244]] Demystifying the Autoresearch Harness | 自进化 / Self-Evolving | 4 | 分析 / analysis |
| 48 | [[2611.23476]] GUARD | 自进化 / Self-Evolving | 5 | 方法 / method |
| 49 | [[2611.21056]] Evaluation-Free Recursive Self-Improvement | 自进化 / Self-Evolving | 6 | 方法 / method |
| 50 | [[2611.25357]] Pro² Agent | 自进化 / Self-Evolving | 7 | 系统 / system |
| 51 | [[2611.28483]] Don't Train It, Write It | 自进化 / Self-Evolving | 8 | 方法 / method |
| 52 | [[2611.29306]] DoppelVet | 自进化 / Self-Evolving | 9 | 方法 / method |
| 53 | [[2611.28833]] Self-WSP | 自进化 / Self-Evolving | 10 | 分析 / analysis |
| 54 | [[2611.23398]] HardwareDx | 计算基础设施 / Compute Infra | 1 | 系统 / system |
| 55 | [[2611.21288]] GNoF | 计算基础设施 / Compute Infra | 2 | 系统 / system |
| 56 | [[2611.27765]] Weave | 计算基础设施 / Compute Infra | 3 | 系统 / system |
| 57 | [[2611.23848]] KIWI GPU-to-CPU Invocation | 计算基础设施 / Compute Infra | 4 | 系统 / system |
| 58 | [[2611.22215]] Communicate the Change (EchoMoE) | 计算基础设施 / Compute Infra | 5 | 方法 / method |
| 59 | [[2611.21274]] SURMA | 计算基础设施 / Compute Infra | 6 | 系统 / system |
| 60 | [[2611.25091]] Berth | 计算基础设施 / Compute Infra | 7 | 系统 / system |
| 61 | [[2611.23053]] SPICE | 计算基础设施 / Compute Infra | 8 | 方法 / method |
| 62 | [[2611.24891]] Cap-and-Track | 计算基础设施 / Compute Infra | 9 | 系统 / system |
| 63 | [[2611.23512]] DexAttention | 计算基础设施 / Compute Infra | 10 | 系统 / system |
| 64 | [[2611.29651]] Which Loopholes Get Found? | RL 后训练 / RL Post-Training | 1 | 分析 / analysis |
| 65 | [[2611.21538]] Optimistic Verifiers Get Hacked | RL 后训练 / RL Post-Training | 2 | 分析 / analysis |
| 66 | [[2611.26084]] RL Can Only Reinforce What It Sees Succeed | RL 后训练 / RL Post-Training | 3 | 分析 / analysis |
| 67 | [[2611.26172]] Budget Internalization | RL 后训练 / RL Post-Training | 4 | 分析 / analysis |
| 68 | [[2611.27125]] When Students Fail to Learn from Teachers | RL 后训练 / RL Post-Training | 5 | 分析 / analysis |
| 69 | [[2611.28582]] Fragility of Self-Rewarding Optimization | RL 后训练 / RL Post-Training | 6 | 分析 / analysis |
| 70 | [[2611.27148]] Structure Over Scale | RL 后训练 / RL Post-Training | 7 | 分析 / analysis |
| 71 | [[2611.22838]] Better Rankers, Worse Retrievers | RL 后训练 / RL Post-Training | 8 | 分析 / analysis |
| 72 | [[2611.28830]] Hidden Sensitivity in LLM Pre-training | 训练稳定 / Training Stability | 1 | 分析 / analysis |
| 73 | [[2611.28725]] Routing Collapse in Multimodal MoE | 训练稳定 / Training Stability | 2 | 分析 / analysis |
| 74 | [[2611.27193]] cmHC | 训练稳定 / Training Stability | 3 | 方法 / method |
| 75 | [[2611.22426]] InfuseLoop | 训练稳定 / Training Stability | 4 | 方法 / method |
| 76 | [[2611.24644]] Equal Steps, Unequal Curvature | 训练稳定 / Training Stability | 5 | 分析 / analysis |
| 77 | [[2611.24331]] OpenGNS | 训练稳定 / Training Stability | 6 | 基准 / benchmark |
| 78 | [[2611.28341]] When Tools Fail, Agents Fabricate | Agent 静默失败 / Agent Silent Failures | 1 | 分析 / analysis |
| 79 | [[2611.20595]] Invariant-Aware Harness Enforcement | Agent 静默失败 / Agent Silent Failures | 2 | 方法 / method |
| 80 | [[2611.27095]] Epistemic Guard | Agent 静默失败 / Agent Silent Failures | 3 | 系统 / system |
| 81 | [[2611.22169]] Not All Evidence Is Admissible | Agent 静默失败 / Agent Silent Failures | 4 | 方法 / method |
| 82 | [[2611.20922]] Experience Rot | Agent 静默失败 / Agent Silent Failures | 5 | 分析 / analysis |
| 83 | [[2611.26358]] Beam Model Technical Report | 系统卡 / System Cards | 1 | 报告 / report |
| 84 | [[2611.21003]] K2-Horizon | 系统卡 / System Cards | 2 | 报告 / report |
| 85 | [[2611.21072]] Sage S2.1 Flash | 系统卡 / System Cards | 3 | 报告 / report |
| 86 | [[2611.22115]] TeleChat to Xing4 | 系统卡 / System Cards | 4 | 报告 / report |
| 87 | [[2611.24636]] Clover-35B-A3B-Preview | 系统卡 / System Cards | 5 | 报告 / report |
| 88 | [[2611.22243]] Bit Flips in a Shared KV-Cache Block | 推理可靠 / Inference Reliability | 1 | 分析 / analysis |
| 89 | [[2611.26307]] ReRAM Fault Vulnerability Analysis | 推理可靠 / Inference Reliability | 2 | 分析 / analysis |
| 90 | [[2611.23358]] Binary Transformers with Approximate Memories (PIES) | 推理可靠 / Inference Reliability | 3 | 方法 / method |

## 统计与核对 / Counts and Verification

- `filtered_papers.json`：`total_evaluated = 3437`，`total_selected = 90`，`papers` 数组长度 90。 / The manifest reports 3,437 evaluated, 90 selected, and the `papers` array holds 90 entries.
- 本文件 `All Papers` 表行数：**90**（编号 1–90，无重复、无缺号）。 / This file's All Papers table has **90** rows, numbered 1–90 with no duplicates or gaps.
- 各领域表行数合计：15 + 15 + 13 + 10 + 10 + 8 + 6 + 5 + 5 + 3 = **90**，与 `selected_by_area` 完全一致。 / The per-area tables sum to 90, matching `selected_by_area` exactly.
- 领域配额与实际入选：自进化 10/10、训练稳定 6/10、RL 后训练 8/8、推理可靠 3/10、算子精度 13/17、Agent 静默失败 5/5、极限优化 15/15、隐状态 15/15、计算基础设施 10/10、系统卡 5/10。未用满的 18 个配额未在领域间重新分配（按规则保留空缺）。 / Quota usage above; the 18 unused slots were not redistributed across areas, per the selection rule.
- 差异说明 / Discrepancy note：**无差异**（表格 90 行 = `total_selected` 90）。唯一需要标注的是 `Inference Reliability & SDC Detection` 仅 3 篇，原因是该领域门控后只有 3 篇达标，而非筛选失败。 / **No discrepancy**: 90 table rows equal `total_selected = 90`. The only caveat is that `Inference Reliability & SDC Detection` holds 3 papers because only 3 cleared the gate, not because selection failed.
