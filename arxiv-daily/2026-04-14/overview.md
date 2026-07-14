---
title: "Daily Paper Overview — 2026-04-14"
date: 2026-04-14
tags:
  - daily-overview
  - paper-digest
papers: 44
---

# Daily Paper Overview — 2026-04-14

## Quick Stats

| Metric | Value |
|--------|-------|
| Papers reviewed | 332 |
| Papers summarized | 44 |
| Categories | cs.CL, cs.AI, cs.LG, cs.CV, cs.PF, cs.AR, stat.ML |
| Relevance score 5 | 10 |
| Relevance score 4 | 17 |
| Relevance score 3 | 17 |

## 今日必读 / Must Read Today

> Top picks based on relevance to your interests.

| Paper | 推荐理由 / Why |
|-------|----------------|
| [[2604.13016v1]] Rethinking On-Policy Distillation of Large Lang... | This paper systematically identifies two governing conditions for on-policy distillation (OPD) success—thinking-patte... |
| [[2604.12875v1]] AISafetyBenchExplorer: A Metric-Aware Catalogue... | A structured, metric-level audit of 195 AI safety benchmarks shows the field's core problem is not scarcity but measu... |
| [[2604.12806v1]] Interpretable Relational Inference with LLM-Gui... | COSINE jointly discovers latent interaction graphs and sparse symbolic governing equations via differentiable co-opti... |
| [[2604.12627v1]] KnowRL: Boosting LLM Reasoning via Reinforcemen... | This paper proposes KnowRL, which addresses reward sparsity in RLVR by decomposing hints into atomic Knowledge Points... |
| [[2604.12469v1]] Analyzing the Effect of Noise in LLM Fine-tuning | A systematic study of label, typographical, and grammatical noise during LLM fine-tuning across three model families ... |
| [[2604.12452v1]] Latent-Condensed Transformer for Efficient Long... | Latent-Condensed Attention (LCA) performs structured context condensation directly within MLA's latent space: query-a... |

---

## 按主题分类 / Papers by Topic

### 可解释性与机制分析 / Interpretability & Mechanistic Analysis

| Paper | 一句话总结 / TL;DR | Tags |
|-------|-------------------|------|
| [[2604.13016v1]] Rethinking On-Policy Distillation of Large... | 本文系统揭示了大规模语言模型在策略蒸馏（OPD）成功与失败的两大核心条件——思维模式的兼容性与教师是否具备学生未见过的新知识，并发现成功的OPD本质上依赖... | `paper arxiv distillation` |
| [[2604.12806v1]] Interpretable Relational Inference with LL... | 提出COSINE框架，通过可微分协同优化与LLM外循环引导的基函数库进化，在未知网络结构下同时推断潜在交互图并发现稀疏可解释的符号动力学方程，在多个合成系... | `paper arxiv cs.LG` |
| [[2604.12469v1]] Analyzing the Effect of Noise in LLM Fine-... | 系统研究了标签噪声、拼写噪声和语法噪声对GPT-2、Qwen2和Llama-2在情感分类、问答和机器翻译任务上微调时的内部学习动态，发现标签噪声最具破坏性... | `paper arxiv cs.LG` |
| [[2604.12337v1]] Identifying and Mitigating Gender Cues in ... | 在去除姓名、代词等显性性别标识后的美国麻醉科住院医师推荐信（LoR）中，DistilBERT、RoBERTa 和 Llama 2 仍能以最高 63% 的准... | `paper arxiv cs.LG` |
| [[2604.13006v1]] One Token Away from Collapse: The Fragilit... | 简单的词汇级约束（如禁止逗号或单词"the"）会导致指令微调LLM的回答全面性崩溃式下降14–48%，这是规划失败而非能力缺失——两阶段生成可恢复59–9... | `paper arxiv cs.CL` |
| [[2604.12820v1]] RePAIR: Interactive Machine Unlearning thr... | 提出交互式机器遗忘（IMU）新范式，通过RePAIR框架让终端用户用自然语言在推理时指令LLM遗忘特定知识，核心方法STAMP以无训练、闭式伪逆更新MLP... | `paper arxiv cs.AI` |
| [[2604.12771v1]] Asymptotic Theory for Graphical SLOPE: Pre... | 本文在固定维度渐近框架下建立了Graphical SLOPE的极限理论，刻画了精度矩阵估计误差与SLOPE模式聚类结构的收敛行为，量化了高斯损失在厚尾椭圆... | `paper arxiv statistical-learning` |
| [[2604.12573v1]] IDEA: An Interpretable and Editable Decisi... | 本文提出IDEA框架，通过将LLM的决策知识提取到语义可解释的二元因子模型中，联合学习言语-数值概率映射与决策参数，实现了概率校准、可解释推理和可定量编辑... | `paper arxiv llm-interpretability` |
| [[2604.12384v1]] Preventing Safety Drift in Large Language ... | 本文首次从理论上证明仅约束权重或激活任一层面都不足以保持LLM的安全对齐，并提出CWAC方法——通过耦合权重子空间投影与稀疏自编码器激活正则化，在下游微调... | `paper arxiv cs.AI` |
| [[2604.12378v1]] ReasonXL: Shifting LLM Reasoning Language ... | 本文提出了首个大规模五语言平行推理语料库ReasonXL，并通过SFT+RLVR的两阶段训练证明可以将LLM的推理语言稳定迁移到目标语言，同时通过表示分析... | `paper arxiv multilingual-reasoning` |
| [[2604.12373v1]] Masked by Consensus: Disentangling Privile... | 通过在“分歧子集”上评估探针性能，研究发现LLM在事实知识任务中存在关于自身答案正确性的特权知识（privileged knowledge），但在数学推理... | `paper arxiv cs.CL` |
| [[2604.12359v1]] Compiling Activation Steering into Weights... | 本文提出STEEREDIT方法，通过将顺从行为的激活导向向量编译为仅对触发词生效的权重修改，并施加零空间约束使其在正常输入上保持休眠，从而实现了持久、隐蔽... | `paper arxiv llm-safety` |
| [[2604.12151v1]] Distinct mechanisms underlying in-context ... | 本文在离散马尔可夫链任务上完整刻画了Transformer实现上下文学习的四种算法阶段，发现了归纳头（induction head）与任务识别头（task... | `paper arxiv mechanistic-interpretability` |
| [[2604.13024v1]] CLAD: Efficient Log Anomaly Detection Dire... | 本文提出首个直接在压缩字节流上进行日志异常检测的深度学习框架CLAD，通过挖掘正常日志压缩后的规则字节模式与异常日志对其的系统性破坏之间的差异，在五个基准... | `paper arxiv log-anomaly-detection` |

### 训练稳定性与优化 / Training Stability & Optimization

| Paper | 一句话总结 / TL;DR | Tags |
|-------|-------------------|------|
| [[2604.12627v1]] KnowRL: Boosting LLM Reasoning via Reinfor... | 本文提出KnowRL，通过将提示解耦为原子知识点（KPs）并采用约束子集搜索（CSS）选取最小充分提示子集，显著缓解了RLVR中的奖励稀疏问题，在1.5B... | `paper arxiv cs.AI` |
| [[2604.13010v1]] Lightning OPD: Efficient Post-Training for... | 通过揭示并满足"教师一致性"（teacher consistency）条件，Lightning OPD 将标准在线 On-Policy Distillat... | `paper arxiv cs.LG` |
| [[2604.12817v1]] Understanding and Improving Continuous Adv... | 首次基于上下文学习（ICL）理论分析了大语言模型的连续对抗训练（CAT），证明嵌入空间扰动半径与鲁棒泛化上界负相关，并据此提出嵌入矩阵奇异值正则化的ER-... | `paper arxiv cs.LG` |
| [[2604.12434v1]] A Bayesian Perspective on the Role of Epis... | 本文从贝叶斯视角研究了上下文学习中的延迟泛化（grokking）现象，发现认知不确定性在模型发生grokking转变时会急剧崩溃，从而成为一种无需标签的泛... | `paper arxiv in-context-learning` |
| [[2604.12322v1]] Self-Adversarial One Step Generation via C... | 该论文提出APEX，一种通过条件偏移（condition shifting）在流模型内部生成对抗信号的无判别器单步生成框架，理论上证明其梯度与GAN对齐且... | `paper arxiv cs.CV` |
| [[2604.12196v1]] Beyond Majority Voting: Efficient Best-Of-... | 提出径向共识分数（RCS），通过在答案嵌入空间中计算加权 Fréchet 均值作为语义中心，并按候选答案到中心的径向距离排序，从而在无训练、黑盒友好的条件... | `paper arxiv cs.CL` |
| [[2604.12968v1]] Evolution of Optimization Methods: Algorit... | 本文系统回顾了深度学习优化方法的演进轨迹，提出统一的数学分类框架，并在标准化基准上评估了23种主流优化器，发现SGD在LLM上会出现灾难性崩溃，而Muon... | `paper arxiv optimization` |
| [[2604.12952v1]] An Optimal Sauer Lemma Over $k$-ary Alphabets | 该论文基于DS维度建立了k元字母表上的最优Sauer不等式，将多分类与列表预测中假设类大小的上界从Natarajan维度的指数级依赖改进为最优多项式级依赖... | `paper arxiv cs.LG` |
| [[2604.12946v1]] Parcae: Scaling Laws For Stable Looped Lan... | 通过将循环架构重新建模为非线性时变动力系统，Parcae 约束注入参数的谱范数以解决训练不稳定性，并首次建立了循环深度作为训练和测试时计算的正交扩展轴的幂... | `paper arxiv cs.LG` |
| [[2604.12827v1]] Loop Corrections to the Training and Gener... | 本文从有效场论视角出发，为随机特征模型推导了训练误差、测试误差和泛化 gap 的显式 loop 修正，量化了有限宽度下核函数涨落对泛化行为的 O(1/n)... | `paper arxiv random-feature-models` |
| [[2604.12811v1]] Algorithmic Analysis of Dense Associative ... | 针对高阶密集联想记忆（DAM），在有限系统尺寸下首次证明了异步检索动态的几何收敛性、对抗鲁棒性显式边界以及 Θ(N^{n−1}) 量级的容量保证，并将其检... | `paper arxiv cs.LG` |
| [[2604.12780v1]] Efficient Adversarial Training via Critica... | 提出Criticality-Aware Adversarial Training（CAAT），通过Robust Parameter Criticality... | `paper arxiv cs.CV` |
| [[2604.12748v1]] Generating Effective CoT Traces for Mitiga... | 本文提出了首个针对事件因果关系识别（ECI）的CoT思维链生成流水线，通过系统分析困惑度、轨迹长度与分布差距，发现了小模型反而受益于更长语义解释的新规律，... | `paper arxiv causal-reasoning` |
| [[2604.12736v1]] Token-Level Policy Optimization: Linking G... | 提出TEPO框架，通过序列级似然实现group reward到token的软聚合，并引入针对正优势且熵减token的选择性KL掩码，解决了GRPO在CoT... | `paper arxiv cs.CL` |
| [[2604.12651v1]] Learning Chain Of Thoughts Prompts for Pre... | 本文提出RALP，将知识图谱链接预测重新定义为提示学习问题，通过MIPRO贝叶斯优化学习基于思维链的字符串评分函数，在仅使用≤30个样本且无需梯度的情况下... | `paper arxiv cs.AI` |
| [[2604.12312v1]] CompliBench: Benchmarking LLM Judges for C... | 该论文提出COMPLIBENCH，首个系统评估LLM Judge在多轮对话中检测和定位企业合规违规行为的基准，通过可控缺陷注入与对抗搜索生成318条带精确... | `paper arxiv cs.CL` |

### 计算可靠性与效率 / Computation Reliability & Efficiency

| Paper | 一句话总结 / TL;DR | Tags |
|-------|-------------------|------|
| [[2604.12452v1]] Latent-Condensed Transformer for Efficient... | 提出Latent-Condensed Attention（LCA），在MLA的潜空间中直接对上下文进行结构化压缩，通过查询感知的加权池化聚合语义信息、通过... | `paper arxiv cs.CL` |
| [[2604.12176v1]] Evaluating Relational Reasoning in LLMs wi... | 本文提出"关系复杂度（RC）"作为衡量LLM关系推理能力的 principled 指标，并构建跨代数、生物学和化学的REL基准测试，发现当前前沿LLM的性... | `paper arxiv cs.AI` |
| [[2604.12168v1]] Fully Homomorphic Encryption on Llama 3 mo... | 本文将基于格的后量子全同态加密（FHE）通过 concrete-ml 库集成到 LLaMA-3 的推理流程中，提出了单头和多头两种量化加密变体，在 CPU... | `paper arxiv privacy` |

### 推理评估与基准 / Inference Evaluation & Benchmarking

| Paper | 一句话总结 / TL;DR | Tags |
|-------|-------------------|------|
| [[2604.12875v1]] AISafetyBenchExplorer: A Metric-Aware Cata... | 通过对195个AI安全基准的结构化编目与指标级审计，本文揭示当前生态的核心症结并非基准稀缺，而是测量碎片化与基准治理薄弱导致的大量“同名异义”指标和难以比... | `paper arxiv ai-safety` |
| [[2604.12232v1]] TEMPLATEFUZZ: Fine-Grained Chat Template F... | 本文提出了首个针对大语言模型对话模板（chat template）的细粒度模糊测试框架TemplateFuzz，通过五种元素级变异规则、启发式搜索策略和主... | `paper arxiv llm-safety` |
| [[2604.12218v1]] LLM-Enhanced Log Anomaly Detection: A Comp... | 该论文在HDFS、BGL、Thunderbird和Spirit四个公开数据集上系统对比了传统日志解析+机器学习、微调Transformer（BERT/Ro... | `paper arxiv cs.LG` |
| [[2604.12737v1]] Evaluating Differential Privacy Against Me... | 基于2025 NIST基因组学红队挑战，提出一种无影子模型的堆叠集成成员推断攻击，实证评估联邦学习中差分隐私（DP）的防御效果：ε=200时仍存残余泄露，... | `paper arxiv cs.CR` |
| [[2604.12379v1]] Beyond Output Correctness: Benchmarking an... | 本文提出了首个跨代码生成、摘要与分类任务的推理质量评估基准CodeRQ-Bench，并通过分析1,069个现有评估器的误判案例总结出四条设计洞见，进而设计... | `paper arxiv LLM` |
| [[2604.12951v1]] The Verification Tax: Fundamental Limits o... | 本文证明在罕见错误区（rare-error regime）中，校准误差（ECE）的估计存在无法逾越的下界 Θ((Lε/m)^{1/3})，意味着模型能力越... | `paper arxiv cs.LG` |
| [[2604.12757v1]] GF-Score: Certified Class-Conditional Robu... | 提出 GF-Score 框架，将 GREAT Score 的全局认证鲁棒性指标精确分解为逐类别的鲁棒性画像，并引入四种基于福利经济学的不公平度量指标，同时... | `paper arxiv cs.LG` |
| [[2604.12311v1]] Is Vibe Coding the Future? An Empirical As... | 通过对450个由前沿LLM生成的建筑施工安全Python脚本进行大规模实证评估，发现虽然代码执行成功率高达~85%，但在可执行脚本中约45%存在“静默失败... | `paper arxiv cs.SE` |
| [[2604.12268v1]] CodeSpecBench: Benchmarking LLMs for Execu... | 本文提出了 CODESPECBENCH，首个覆盖函数级与仓库级任务、基于执行的可执行行为规范生成基准，发现即使最强模型在仓库级任务上的通过率也仅 20.2... | `paper arxiv code-generation` |

### 其他相关研究 / Other Related Research

| Paper | 一句话总结 / TL;DR | Tags |
|-------|-------------------|------|
| [[2604.12247v1]] SpecBound: Adaptive Bounded Self-Speculati... | 提出了一种基于自推测解码的加速框架SpecBound，通过层间温度退火的置信度校准与自适应深度/宽度边界的推测策略，在不修改基座模型参数的前提下实现了最高... | `paper arxiv cs.CL` |
| [[2604.12989v1]] Accelerating Speculative Decoding with Blo... | 本文提出 DDTree，通过将块扩散草稿模型（DFlash）单次前向传播产生的逐位置边际分布构建为最优草稿树，在固定节点预算下用树注意力一次性验证多条候选... | `paper arxiv cs.CL` |

---

## All Papers

| # | Paper | Key Topic | 一句话总结 / TL;DR |
|---|-------|-----------|-------------------|
| 1 | [[2604.13016v1]] Rethinking On-Policy Distillation of ... | Interp | 本文系统揭示了大规模语言模型在策略蒸馏（OPD）成功与失败的两大核心条件——思维模式的兼容性与教师是否具备学生未见过的新知识，并发现成... |
| 2 | [[2604.12875v1]] AISafetyBenchExplorer: A Metric-Aware... | Eval | 通过对195个AI安全基准的结构化编目与指标级审计，本文揭示当前生态的核心症结并非基准稀缺，而是测量碎片化与基准治理薄弱导致的大量“同... |
| 3 | [[2604.12806v1]] Interpretable Relational Inference wi... | Interp | 提出COSINE框架，通过可微分协同优化与LLM外循环引导的基函数库进化，在未知网络结构下同时推断潜在交互图并发现稀疏可解释的符号动力... |
| 4 | [[2604.12627v1]] KnowRL: Boosting LLM Reasoning via Re... | Train | 本文提出KnowRL，通过将提示解耦为原子知识点（KPs）并采用约束子集搜索（CSS）选取最小充分提示子集，显著缓解了RLVR中的奖励... |
| 5 | [[2604.12469v1]] Analyzing the Effect of Noise in LLM ... | Interp | 系统研究了标签噪声、拼写噪声和语法噪声对GPT-2、Qwen2和Llama-2在情感分类、问答和机器翻译任务上微调时的内部学习动态，发... |
| 6 | [[2604.12452v1]] Latent-Condensed Transformer for Effi... | Comp | 提出Latent-Condensed Attention（LCA），在MLA的潜空间中直接对上下文进行结构化压缩，通过查询感知的加权池... |
| 7 | [[2604.12337v1]] Identifying and Mitigating Gender Cue... | Interp | 在去除姓名、代词等显性性别标识后的美国麻醉科住院医师推荐信（LoR）中，DistilBERT、RoBERTa 和 Llama 2 仍能... |
| 8 | [[2604.12247v1]] SpecBound: Adaptive Bounded Self-Spec... | Other | 提出了一种基于自推测解码的加速框架SpecBound，通过层间温度退火的置信度校准与自适应深度/宽度边界的推测策略，在不修改基座模型参... |
| 9 | [[2604.12232v1]] TEMPLATEFUZZ: Fine-Grained Chat Templ... | Eval | 本文提出了首个针对大语言模型对话模板（chat template）的细粒度模糊测试框架TemplateFuzz，通过五种元素级变异规则... |
| 10 | [[2604.12218v1]] LLM-Enhanced Log Anomaly Detection: A... | Eval | 该论文在HDFS、BGL、Thunderbird和Spirit四个公开数据集上系统对比了传统日志解析+机器学习、微调Transform... |
| 11 | [[2604.13010v1]] Lightning OPD: Efficient Post-Trainin... | Train | 通过揭示并满足"教师一致性"（teacher consistency）条件，Lightning OPD 将标准在线 On-Policy... |
| 12 | [[2604.13006v1]] One Token Away from Collapse: The Fra... | Interp | 简单的词汇级约束（如禁止逗号或单词"the"）会导致指令微调LLM的回答全面性崩溃式下降14–48%，这是规划失败而非能力缺失——两阶... |
| 13 | [[2604.12820v1]] RePAIR: Interactive Machine Unlearnin... | Interp | 提出交互式机器遗忘（IMU）新范式，通过RePAIR框架让终端用户用自然语言在推理时指令LLM遗忘特定知识，核心方法STAMP以无训练... |
| 14 | [[2604.12817v1]] Understanding and Improving Continuou... | Train | 首次基于上下文学习（ICL）理论分析了大语言模型的连续对抗训练（CAT），证明嵌入空间扰动半径与鲁棒泛化上界负相关，并据此提出嵌入矩阵... |
| 15 | [[2604.12771v1]] Asymptotic Theory for Graphical SLOPE... | Interp | 本文在固定维度渐近框架下建立了Graphical SLOPE的极限理论，刻画了精度矩阵估计误差与SLOPE模式聚类结构的收敛行为，量化... |
| 16 | [[2604.12737v1]] Evaluating Differential Privacy Again... | Eval | 基于2025 NIST基因组学红队挑战，提出一种无影子模型的堆叠集成成员推断攻击，实证评估联邦学习中差分隐私（DP）的防御效果：ε=2... |
| 17 | [[2604.12573v1]] IDEA: An Interpretable and Editable D... | Interp | 本文提出IDEA框架，通过将LLM的决策知识提取到语义可解释的二元因子模型中，联合学习言语-数值概率映射与决策参数，实现了概率校准、可... |
| 18 | [[2604.12434v1]] A Bayesian Perspective on the Role of... | Train | 本文从贝叶斯视角研究了上下文学习中的延迟泛化（grokking）现象，发现认知不确定性在模型发生grokking转变时会急剧崩溃，从而... |
| 19 | [[2604.12384v1]] Preventing Safety Drift in Large Lang... | Interp | 本文首次从理论上证明仅约束权重或激活任一层面都不足以保持LLM的安全对齐，并提出CWAC方法——通过耦合权重子空间投影与稀疏自编码器激... |
| 20 | [[2604.12379v1]] Beyond Output Correctness: Benchmarki... | Eval | 本文提出了首个跨代码生成、摘要与分类任务的推理质量评估基准CodeRQ-Bench，并通过分析1,069个现有评估器的误判案例总结出四... |
| 21 | [[2604.12378v1]] ReasonXL: Shifting LLM Reasoning Lang... | Interp | 本文提出了首个大规模五语言平行推理语料库ReasonXL，并通过SFT+RLVR的两阶段训练证明可以将LLM的推理语言稳定迁移到目标语... |
| 22 | [[2604.12373v1]] Masked by Consensus: Disentangling Pr... | Interp | 通过在“分歧子集”上评估探针性能，研究发现LLM在事实知识任务中存在关于自身答案正确性的特权知识（privileged knowled... |
| 23 | [[2604.12359v1]] Compiling Activation Steering into We... | Interp | 本文提出STEEREDIT方法，通过将顺从行为的激活导向向量编译为仅对触发词生效的权重修改，并施加零空间约束使其在正常输入上保持休眠，... |
| 24 | [[2604.12322v1]] Self-Adversarial One Step Generation ... | Train | 该论文提出APEX，一种通过条件偏移（condition shifting）在流模型内部生成对抗信号的无判别器单步生成框架，理论上证明... |
| 25 | [[2604.12196v1]] Beyond Majority Voting: Efficient Bes... | Train | 提出径向共识分数（RCS），通过在答案嵌入空间中计算加权 Fréchet 均值作为语义中心，并按候选答案到中心的径向距离排序，从而在无... |
| 26 | [[2604.12176v1]] Evaluating Relational Reasoning in LL... | Comp | 本文提出"关系复杂度（RC）"作为衡量LLM关系推理能力的 principled 指标，并构建跨代数、生物学和化学的REL基准测试，发... |
| 27 | [[2604.12151v1]] Distinct mechanisms underlying in-con... | Interp | 本文在离散马尔可夫链任务上完整刻画了Transformer实现上下文学习的四种算法阶段，发现了归纳头（induction head）与... |
| 28 | [[2604.13024v1]] CLAD: Efficient Log Anomaly Detection... | Interp | 本文提出首个直接在压缩字节流上进行日志异常检测的深度学习框架CLAD，通过挖掘正常日志压缩后的规则字节模式与异常日志对其的系统性破坏之... |
| 29 | [[2604.12989v1]] Accelerating Speculative Decoding wit... | Other | 本文提出 DDTree，通过将块扩散草稿模型（DFlash）单次前向传播产生的逐位置边际分布构建为最优草稿树，在固定节点预算下用树注意... |
| 30 | [[2604.12968v1]] Evolution of Optimization Methods: Al... | Train | 本文系统回顾了深度学习优化方法的演进轨迹，提出统一的数学分类框架，并在标准化基准上评估了23种主流优化器，发现SGD在LLM上会出现灾... |
| 31 | [[2604.12952v1]] An Optimal Sauer Lemma Over $k$-ary A... | Train | 该论文基于DS维度建立了k元字母表上的最优Sauer不等式，将多分类与列表预测中假设类大小的上界从Natarajan维度的指数级依赖改... |
| 32 | [[2604.12951v1]] The Verification Tax: Fundamental Lim... | Eval | 本文证明在罕见错误区（rare-error regime）中，校准误差（ECE）的估计存在无法逾越的下界 Θ((Lε/m)^{1/3}... |
| 33 | [[2604.12946v1]] Parcae: Scaling Laws For Stable Loope... | Train | 通过将循环架构重新建模为非线性时变动力系统，Parcae 约束注入参数的谱范数以解决训练不稳定性，并首次建立了循环深度作为训练和测试时... |
| 34 | [[2604.12827v1]] Loop Corrections to the Training and ... | Train | 本文从有效场论视角出发，为随机特征模型推导了训练误差、测试误差和泛化 gap 的显式 loop 修正，量化了有限宽度下核函数涨落对泛化... |
| 35 | [[2604.12811v1]] Algorithmic Analysis of Dense Associa... | Train | 针对高阶密集联想记忆（DAM），在有限系统尺寸下首次证明了异步检索动态的几何收敛性、对抗鲁棒性显式边界以及 Θ(N^{n−1}) 量级... |
| 36 | [[2604.12780v1]] Efficient Adversarial Training via Cr... | Train | 提出Criticality-Aware Adversarial Training（CAAT），通过Robust Parameter C... |
| 37 | [[2604.12757v1]] GF-Score: Certified Class-Conditional... | Eval | 提出 GF-Score 框架，将 GREAT Score 的全局认证鲁棒性指标精确分解为逐类别的鲁棒性画像，并引入四种基于福利经济学的... |
| 38 | [[2604.12748v1]] Generating Effective CoT Traces for M... | Train | 本文提出了首个针对事件因果关系识别（ECI）的CoT思维链生成流水线，通过系统分析困惑度、轨迹长度与分布差距，发现了小模型反而受益于更... |
| 39 | [[2604.12736v1]] Token-Level Policy Optimization: Link... | Train | 提出TEPO框架，通过序列级似然实现group reward到token的软聚合，并引入针对正优势且熵减token的选择性KL掩码，解... |
| 40 | [[2604.12651v1]] Learning Chain Of Thoughts Prompts fo... | Train | 本文提出RALP，将知识图谱链接预测重新定义为提示学习问题，通过MIPRO贝叶斯优化学习基于思维链的字符串评分函数，在仅使用≤30个样... |
| 41 | [[2604.12312v1]] CompliBench: Benchmarking LLM Judges ... | Train | 该论文提出COMPLIBENCH，首个系统评估LLM Judge在多轮对话中检测和定位企业合规违规行为的基准，通过可控缺陷注入与对抗搜... |
| 42 | [[2604.12311v1]] Is Vibe Coding the Future? An Empiric... | Eval | 通过对450个由前沿LLM生成的建筑施工安全Python脚本进行大规模实证评估，发现虽然代码执行成功率高达~85%，但在可执行脚本中约... |
| 43 | [[2604.12268v1]] CodeSpecBench: Benchmarking LLMs for ... | Eval | 本文提出了 CODESPECBENCH，首个覆盖函数级与仓库级任务、基于执行的可执行行为规范生成基准，发现即使最强模型在仓库级任务上的... |
| 44 | [[2604.12168v1]] Fully Homomorphic Encryption on Llama... | Comp | 本文将基于格的后量子全同态加密（FHE）通过 concrete-ml 库集成到 LLaMA-3 的推理流程中，提出了单头和多头两种量化... |

---

*Overview generated on 2026-04-14*