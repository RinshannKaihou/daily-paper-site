---
title: "Daily Overview — 2026-06-23"
date: 2026-06-23
tags:
  - daily-overview
  - arxiv
  - self-evolving-agents
  - quantization
  - interpretability
papers: 50
---

# Daily Overview — 2026-06-23

今日共筛选 50 篇 arXiv 论文,按主题分为 8 个组。Self-evolving agents 与 quantized inference 两组占比最大,反映了当前 LLM 研究的两个主轴——**让 agent 持续自我改进** 与 **让模型在更低精度下保持可靠性**。Interpretability 一组也有 9 篇,体现出对 hidden states 几何结构与稀疏特征机制的新一波兴趣。

---

## 今日必读 / Must Read Today

### [[2606.05080]] AutoLab — 长时程智能体评测:坚持比才华更重要

**中文:** AutoLab 用 36 个跨系统优化 / 谜题 / 模型开发 / CUDA kernel 的真实任务、2544 壁钟小时对 17 个前沿模型做评估,揭示 Claude Opus 4.6 以 Avg@3 0.68 显著领先,但决定胜负的不是一次性代码质量,而是**持续迭代、反馈吸收与时间感知**——同时给出 harness 消融实证,证明 agent 基础设施单独可让同一模型的分数摆动高达 0.43,颠覆"长时程能力可与 harness 解耦评测"的常识。

**English:** AutoLab benchmarks 17 frontier models on 36 ultra long-horizon tasks across 4 domains (2,544 wall-clock hours). Claude Opus 4.6 leads decisively (Avg@3 0.68 vs. 0.50 for the runner-up), but the dominant predictor of success is **persistence** — repeatedly benchmarking, editing, and incorporating empirical feedback — rather than one-shot solution quality. A 302-rollout manual failure-mode analysis reveals a cross-model **lack of time awareness**, and a harness ablation shows framework design alone can shift scores by up to 0.43, meaning long-horizon capability cannot be measured independently of agent infrastructure.

### [[2606.06741]] OpenSkill — 开放世界自进化与跨模型技能迁移

**中文:** OpenSkill 提出"开放世界自进化"新设定:智能体只拿到任务指令和公网资源,须自行从文档 / 仓库 / 网页抓取知识合成可迁移技能,并用自建 pytest 虚拟任务做无监督打磨。SkillsBench 上以 43.6%/42.1% (Opus/GPT) 拿下最强自动方法,且同一组 Opus 4.6 生成的技能**无需适配即可迁移**到 Haiku 4.5 / Qwen 3 Coder / DeepSeek V3 / Mistral Large 3,验证了"技能是一等公民的显式 artifact"而非模型专属权重。

**English:** OpenSkill formalizes **open-world self-evolution** where an LLM agent must bootstrap both its skill library and its verifier from public web knowledge — no target-task supervision allowed. The three-stage pipeline (Gemini Deep Research → Opus 4.6 skill synthesis with virtual pytest verifier → zero-shot deployment) hits 43.6% / 42.1% on SkillsBench, beating the strongest closed-world baseline by +8.9/+8.8 pp. The most striking result: Opus-built skills transfer as-is to 4 weaker models (Haiku, Qwen 3 Coder, DeepSeek V3, Mistral Large 3) with +5.5–14.8 pp gains, proving skills are first-class portable artifacts, not model-specific weights.

### [[2606.09052]] INFUSER — 影响函数驱动的自进化数据生成

**中文:** INFUSER 把"求解器–生成器协同自演化"的目标从难度启发式换成了"对当前求解器有用的题目",用优化器感知的影响力分数驱动生成器奖励,并配套 DuGRPO(双归一化 GRPO)处理连续含噪信号。Qwen3-8B-Base 在 Olympiad / SuperGPQA 上相对提升 >20%,**8B 共演化生成器在数学 / 代码上超过冻结 32B 思维生成器**——给"为何用大模型生成数据"提供了"有用 > 大 > 难"的新论证。

**English:** INFUSER reframes self-evolving reasoning as a *two-role co-training* problem where the **Generator** is rewarded by an *optimizer-aware influence score* measuring each candidate question's effect on the solver's loss on the target distribution — replacing difficulty heuristics with a quantitative "usefulness to the current solver" signal. A **DuGRPO** (dual-normalized GRPO) variant handles the continuous, noisy influence reward. On Qwen3-8B-Base, INFUSER gains >20% on Olympiad/SuperGPQA, and an **8B co-evolving generator outperforms a frozen 32B thinking generator** on math/coding — a strong "purpose-trained small > generic large" data point.

---

## 按主题分类 / Papers by Topic

### Self-Evolving Agents & Automated Research

| 论文 | 一句中文 | One-line English | Score |
|---|---|---|---|
| [[2606.09052]] INFUSER | 影响函数驱动的生成器–求解器共演化,DuGRPO 配合 | Influence-guided generator-solver co-evolution with DuGRPO | 5 |
| [[2606.06741]] OpenSkill | 开放世界自进化技能库,可跨模型零适配迁移 | Open-world self-evolution skills with cross-model transfer | 5 |
| [[2606.04507]] SCORE | Deep-Research 求解器–评测器共进化,避免 LLD 崩塌 | Self-Evolving Deep Research via joint generation/evaluation | 5 |
| [[2606.04703]] ExpInternalization | 经验内化三原则:principle + step-wise + off-policy | Rethinking continual experience internalization | 5 |
| [[2606.05080]] AutoLab | 36 任务 17 模型评测,长时程靠坚持而非一次质量 | 36-task long-horizon eval, persistence > one-shot quality | 5 |
| [[2606.08405]] Self-Evolving Fluid Agent | LLM 驱动源代碼演化,6 步解决两关节机器鱼目标到达 | Self-evolving scientific agent for FSI fluid control | 5 |
| [[2606.01993]] MMG2Skill | 多模态网络教程蒸馏成 SKILL.md + 轨迹诊断闭环 | Distill in-the-wild guides into self-evolving skills | 4 |
| [[2606.01640]] MobEvolve | 智能体自演化的人类出行生成系统 | Agentic self-evolving heuristic for mobility | 4 |
| [[2606.01770]] Adaptive Auto-Harness | 开放任务流的可持续自改进 harness | Sustained self-improvement for open-ended task streams | 4 |
| [[2606.02484]] Iteris | 智能体探索–规划–执行解决两个 Simons 开放问题 | Agentic loops for computational mathematics | 4 |
| [[2606.02812]] Traj-Evolve | 临床肺癌早筛的自演化多智能体框架 | Self-evolving multi-agent for lung-cancer EHR | 4 |
| [[2606.03099]] PhotoCraft | 工作/情景/语义三层记忆的深度图像检索智能体 | Hierarchical self-evolving memory for image search | 4 |
| [[2606.03692]] SkillPyramid | 离散技能重组为金字塔层级结构 | Hierarchical skill consolidation framework | 4 |
| [[2606.03979]] Sleep for LLMs | 睡眠范式:周期性参数激活 + 知识播种 + 梦境自改进 | Sleep paradigm with Knowledge Seeding + Dreaming | 4 |
| [[2606.04465]] SePO | 提示词优化器自身的提示也可进化 | Self-Evolving Prompt Agent | 4 |
| [[2606.05513]] EpiEvolve | 50 州 81 周流式疫情预测,漂移感知自演化 | Streaming pandemic forecasting with regime shift | 4 |
| [[2606.05661]] CL-Bench | 持续学习基准:朴素 ICL 优于专用记忆系统 | Continual learning benchmark in real-world environments | 4 |
| [[2606.06473]] MLEvolve | 渐进 MCGS + 回溯记忆,击败 AlphaEvolve | Self-evolving automated ML algorithm discovery | 4 |
| [[2606.01075]] SE Generalization Gap | 闭环自进化 vs. oracle:8–13% 不可消除差距 | Closed-loop self-evolution generalization gap | 4 |
| [[2606.01314]] SkillSmith | 技能–工具共同进化的原子化提案空间 | Co-evolving skills and tools | 4 |
| [[2606.01961]] AutoMedBench | 24 任务 5 阶段工作流的医疗 AI 自主研究评测 | Medical AutoResearch workflow benchmark | 4 |
| [[2606.02215]] EvoNote | 健康类社区注释的阶段化记忆自演化 | Self-evolving LLM agents for health notes | 4 |
| [[2606.03056]] SkillDAG | 五类边类型图的结构化检索接口 | Typed skill graphs for LLM skill selection | 4 |
| [[2606.03678]] EvoDrive | 安全关键自动驾驶场景的帕累托进化 | Pareto evolution for safety-critical driving | 4 |
| [[2606.03841]] EvoDS | Manager + 5 子代理 + 自演化技能采集 | Self-evolving data-science agent | 4 |
| [[2606.04536]] TMEM | 把长时程记忆从 prompt 下沉到 LoRA 快权重 | Scaling self-evolving agents via parametric memory | 4 |

### LLM Inference, Quantization & Hardware

| 论文 | 一句中文 | One-line English | Score |
|---|---|---|---|
| [[2606.02288]] INSERTQUANT | 尖峰本质是刚性偏置向量,W4A4 跨 LLM / ViT 一致 | Massive spikes are bias vectors, spike-free quantization | 5 |
| [[2606.06521]] P-Cast FP8 | FP8 Attention 中 P 塌缩闭式解,S=256 唯一最优 | Sink-induced collapse and S=2^8 optimality in FP8 attention | 4 |
| [[2606.06510]] FP8 is All You Need | Ozaki II + 五层框架:FP8 MMA 作为 FP64 唯一原语 | FP8 is all you need for HPC on AI GPUs | 4 |
| [[2606.09686]] t27 Numeric Catalog | 83 格式 6 个 bit-exact 一致性测试包 | 83-format numeric catalog with conformance vectors | 4 |
| [[2606.11357]] TileFuse | AMD XDNA2 NPU 的 AWQ 融合混合精度内核 | Fused mixed-precision kernels on AMD NPUs | 4 |
| [[2606.00079]] BitsMoE | SVD 共享基 + ILP 比特分配,2-bit 比 GPTQ +27.83pp | Spectral-energy-guided bit allocation for MoE | 4 |
| [[2606.11244]] SPEAR | 4-bit 推理的低秩门控补偿 + CKA 引导模块选择 | Post-quantization error-adaptive recovery | 4 |
| [[2606.00365]] SPARQLe | 8-bit 激活拆为稠密 LSB4 + 稀疏 MSB4 + PBM | Sub-precision activation representation | 4 |

### Interpretability & Mechanistic Analysis

| 论文 | 一句中文 | One-line English | Score |
|---|---|---|---|
| [[2606.03085]] Multi-Component Causal Tracing | PGB-CT:软 mask + 变换奖励 + 调度惩罚,组合搜索松为连续优化 | PGB-CT: penalized gradient-based causal tracing | 5 |
| [[2606.03780]] Expert-Aware MoE Causal Tracing | 单专家 L44E069 在 Qwen3-30B-A3B 承担事实回路 | Expert-aware causal tracing of factual recall | 5 |
| [[2606.06857]] Sparse Features Brain | SAE + Matryoshka 层级解释 fMRI 体素响应 | Brain-language alignment with sparse features | 5 |
| [[2606.02628]] Hallucination Linear Decodable | 4-bit 量化 LLM 中层隐藏态线性探针 AUROC 0.904–1.000 | Hallucination linearly decodable from mid-layer | 5 |
| [[2606.07720]] AGCLR | 门控概念流解决连续潜推理的概念瓶颈 | Persistent memory for continuous latent reasoning | 4 |
| [[2606.02907]] Linear Probes | 探针所谓"区分推理模式"几乎完全是格式混淆 | Probes detect task format, not reasoning mode | 4 |
| [[2606.03002]] SAE Feature Damage | 量化下 SAE 特征"梯度式"损伤,困惑度会漏报 | Perplexity misses SAE feature damage under quantization | 4 |
| [[2606.01479]] SAE Emotion TTS | SAE 在 LLM-TTS 语义骨干实现双向情感控制 | Sparse autoencoders for emotion control in TTS | 4 |
| [[2606.05346]] Trajectory Extrapolation Error | 隐藏态方向连续性独立于 surprisal 预测阅读时间 | Trajectory dynamics predict human processing costs | 4 |

### System Cards & Frontier Models

| 论文 | 一句中文 | One-line English | Score |
|---|---|---|---|
| [[2606.00027]] Medical Red Teaming | 690 临床对抗场景红队,11 LLM 七维度评分 | Multi-domain red-teaming framework for medical LLMs | 4 |
| [[2606.05433]] ZK Frontier Training | 三锚点 zkVM 验证前沿 405B 训练,36 个月内可行 | Zero-knowledge verification of frontier training | 4 |

### Training Stability & Reliability

| 论文 | 一句中文 | One-line English | Score |
|---|---|---|---|
| [[2606.00539]] GNMR | 运行时梯度范数比控制 FP4/INT8 训练稳定性 | Runtime stability control for low-precision training | 4 |

### Silent Data Corruption

| 论文 | 一句中文 | One-line English | Score |
|---|---|---|---|
| [[2606.19526]] SPINE | GDB 累积故障注入量化神经网络,指导选择性硬化 | Fault injection profiler for quantized NNs | 5 |

### ML Reliability & Foundations

| 论文 | 一句中文 | One-line English | Score |
|---|---|---|---|
| [[2606.01850]] Conformal Compression | 压缩会解耦精度与不确定性,大模型更能吸收膨胀 | Compression's effect on uncertainty via conformal prediction | 4 |
| [[2606.01400]] MIS Prompt Selection | 图论 MIS 在 4 基准 66 LLM 上压缩 25–48% 提示词 | Maximum Independent Set prompt selection | 4 |

### Multimodal / Vision-Language

| 论文 | 一句中文 | One-line English | Score |
|---|---|---|---|
| [[2606.00390]] Zamba2-VL | 首个开源 Mamba2+Transformer 混合 VLM 家族 (1.2/2.7/7B) | First open hybrid SSM-Transformer VLM family | 4 |

---

## All Papers

| ArXiv ID | Short Title | Score |
|---|---|---|
| [[2606.00027]] | Medical Red Teaming Framework | 4 |
| [[2606.00079]] | BitsMoE | 4 |
| [[2606.00365]] | SPARQLe | 4 |
| [[2606.00390]] | Zamba2-VL | 4 |
| [[2606.00539]] | GNMR | 4 |
| [[2606.01075]] | Generalization Gap in Self-Evolving Reasoning | 4 |
| [[2606.01314]] | SkillSmith | 4 |
| [[2606.01400]] | MIS Prompt Selection | 4 |
| [[2606.01479]] | SAE Emotion TTS | 4 |
| [[2606.01640]] | MobEvolve | 4 |
| [[2606.01770]] | Adaptive Auto-Harness | 4 |
| [[2606.01850]] | Conformal Prediction Compression | 4 |
| [[2606.01961]] | AutoMedBench | 4 |
| [[2606.01993]] | MMG2Skill | 4 |
| [[2606.02215]] | EvoNote | 4 |
| [[2606.02288]] | INSERTQUANT | 5 |
| [[2606.02484]] | Iteris | 4 |
| [[2606.02628]] | Hallucination Linear Decodable | 5 |
| [[2606.02812]] | Traj-Evolve | 4 |
| [[2606.02907]] | Linear Probes | 4 |
| [[2606.03002]] | SAE Feature Damage | 4 |
| [[2606.03056]] | SkillDAG | 4 |
| [[2606.03085]] | Multi-Component Causal Tracing | 5 |
| [[2606.03099]] | PhotoCraft | 4 |
| [[2606.03678]] | EvoDrive | 4 |
| [[2606.03692]] | SkillPyramid | 4 |
| [[2606.03780]] | Expert-Aware MoE Causal Tracing | 5 |
| [[2606.03841]] | EvoDS | 4 |
| [[2606.03979]] | Sleep for LLMs | 4 |
| [[2606.04465]] | SePO | 4 |
| [[2606.04507]] | SCORE | 5 |
| [[2606.04536]] | TMEM | 4 |
| [[2606.04703]] | ExpInternalization | 5 |
| [[2606.05080]] | AutoLab | 5 |
| [[2606.05346]] | Trajectory Extrapolation Error | 4 |
| [[2606.05433]] | ZK Frontier Training | 4 |
| [[2606.05513]] | EpiEvolve | 4 |
| [[2606.05661]] | CL-Bench | 4 |
| [[2606.06473]] | MLEvolve | 4 |
| [[2606.06510]] | FP8 is All You Need | 4 |
| [[2606.06521]] | P-Cast FP8 | 4 |
| [[2606.06741]] | OpenSkill | 5 |
| [[2606.06857]] | Sparse Features Brain | 5 |
| [[2606.07720]] | AGCLR | 4 |
| [[2606.08405]] | Self-Evolving Fluid Agent | 5 |
| [[2606.09052]] | INFUSER | 5 |
| [[2606.09686]] | t27 Numeric Catalog | 4 |
| [[2606.11244]] | SPEAR | 4 |
| [[2606.11357]] | TileFuse | 4 |
| [[2606.19526]] | SPINE | 5 |
