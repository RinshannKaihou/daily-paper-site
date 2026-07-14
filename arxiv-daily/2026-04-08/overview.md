---
title: "Daily Paper Overview — 2026-04-08"
date: 2026-04-08
tags:
  - daily-overview
  - paper-digest
papers: 43
---

# Daily Paper Overview — 2026-04-08

## Quick Stats

| Metric | Value |
|--------|-------|
| Papers reviewed | 43 |
| Categories | cs.LG, cs.CL, cs.AI, cs.CV, cs.PF, cs.AR, stat.ML |
| Time range | 2026-04-08 |
| Total fetched | 316 |
| After filtering | 43 |

## Must Read Today

> Top picks based on relevance to your interests.

| Paper | Why |
|-------|-----|
| [[2604.07019v1]] ConceptTracer: Interactive Analysis of Concept Sal | Directly addresses mechanistic interpretability by introducing information-th... |
| [[2604.06899v1]] Data Leakage in Automotive Perception: Practitione | Systematically investigates data leakage as a reliability risk in ML models f... |
| [[2604.06916v1]] FP4 Explore, BF16 Train: Diffusion Reinforcement L | Directly addresses FP4 quantization effects on training integrity, proposing ... |
| [[2604.06767v1]] Geometric Properties of the Voronoi Tessellation i | Directly studies representation geometry in LLMs, analyzing Voronoi tessellat... |
| [[2604.07328v1]] How to sketch a learning algorithm | Addresses data deletion and stability in deep learning training, proposing a ... |

---

## Interpretability & Representation Analysis

| Paper | TL;DR | Tags |
|-------|-------|------|
| [[2604.07282v1]] Are Face Embeddings Compatible Across Deep Ne | Simple linear transformations can align face embeddings across independently trained DNN models, ... | `cs` |
| [[2604.07154v1]] Bridging MRI and PET physiology: Untangling c | A subspace decomposition framework separates PSMA PET uptake into MRI-explainable and orthogonal ... | `cs` |
| [[2604.07019v1]] ConceptTracer: Interactive Analysis of Concep | Introduces ConceptTracer, an interactive tool using two information-theoretic measures (saliency ... | `cs` |
| [[2604.07006v1]] Continuous Interpretive Steering for Scalar D | Continuous Interpretive Steering (CIS) treats activation steering strength as a continuous variab... | `cs` |
| [[2604.06899v1]] Data Leakage in Automotive Perception: Practi | Through 10 semi-structured interviews with automotive perception practitioners at an OEM (Volvo C... | `cs` |
| [[2604.07166v1]] DINO-QPM: Adapting Visual Foundation Models f | DINO-QPM adapts the QPM framework to frozen DINOv2 backbones, converting entangled features into ... | `cs` |
| [[2604.06893v1]] Energy-Regularized Spatial Masking: A Novel A | ERSM reformulates feature selection as a differentiable energy minimization problem, producing em... | `cs` |
| [[2604.06652v1]] FlowAdam: Implicit Regularization via Geometr | Introduces FlowAdam, a hybrid optimizer that augments Adam with continuous gradient-flow ODE inte... | `cs` |
| [[2604.07035v1]] Gemma 4, Phi-4, and Qwen3: Accuracy-Efficienc | Controlled benchmark of 7 dense/MoE reasoning models across 4 benchmarks and 3 prompting strategi... | `cs` |
| [[2604.06767v1]] Geometric Properties of the Voronoi Tessellat | Validates the Voronoi tessellation linear scaling law on Qwen3.5-4B-Base with R^2 = 0.9997 by res... | `cs` |
| [[2604.07328v1]] How to sketch a learning algorithm | Introduces a data deletion scheme based on a "stability" assumption, using local sketching of ari... | `cs` |
| [[2604.07095v1]] Multilingual Embedding Probes Fail to General | Probes trained on hidden-state activations from Qwen3-Embedding achieve strong in-distribution pe... | `cs` |
| [[2604.07254v1]] Non-identifiability of Explanations from Mode | Deep networks predicting human authenticity judgments produce divergent attribution explanations ... | `cs` |
| [[2604.07016v1]] Predictive Representations for Skill Transfer | OPSRs provide task-independent state abstractions based on outcome predictions, enabling skill tr... | `cs` |
| [[2604.06695v1]] Reasoning Fails Where Step Flow Breaks | Step-Saliency aggregates attention-gradient scores into step-level maps to reveal Shallow Lock-in... | `cs` |
| [[2604.07098v1]] Selective Neuron Amplification for Training-F | Introduces SNA, which identifies task-relevant neurons via differential activation analysis and s... | `cs` |
| [[2604.07102v1]] The Impact of Steering Large Language Models  | Persona vector steering in LLMs degrades answer quality in educational settings, with open-ended ... | `cs` |

## Training Stability & Optimization

| Paper | TL;DR | Tags |
|-------|-------|------|
| [[2604.07306v1]] Beyond Loss Values: Robust Dynamic Pruning vi | AlignPrune replaces per-sample loss-based ranking with Dynamic Alignment Score (DAS) that measure... | `cs` |
| [[2604.06542v1]] Does a Global Perspective Help Prune Sparse M | GRAPE (Global Redundancy-Aware Pruning of Experts) dynamically allocates pruning budgets based on... | `cs` |
| [[2604.06652v1]] FlowAdam: Implicit Regularization via Geometr | Introduces FlowAdam, a hybrid optimizer that augments Adam with continuous gradient-flow ODE inte... | `cs` |
| [[2604.06916v1]] FP4 Explore, BF16 Train: Diffusion Reinforcem | Proposes Sol-RL, a two-stage RL framework that uses NVFP4 quantization for high-throughput candid... | `cs` |
| [[2604.07035v1]] Gemma 4, Phi-4, and Qwen3: Accuracy-Efficienc | Controlled benchmark of 7 dense/MoE reasoning models across 4 benchmarks and 3 prompting strategi... | `cs` |
| [[2604.07328v1]] How to sketch a learning algorithm | Introduces a data deletion scheme based on a "stability" assumption, using local sketching of ari... | `cs` |
| [[2604.07172v1]] Improving Semantic Uncertainty Quantification | First systematic evaluation of both calibration and discrimination in semantic UQ reveals fixed-t... | `cs` |
| [[2604.07108v1]] Information as Structural Alignment: A Dynami | Introduces IBF, a continual learning framework based on structural alignment rather than paramete... | `cs` |
| [[2604.06966v1]] MAR-GRPO: Stabilized GRPO for AR-diffusion Hy | Identifies the diffusion head as a key source of optimization instability in hybrid AR-diffusion ... | `cs` |
| [[2604.06798v1]] MoBiE: Efficient Inference of Mixture of Bina | MoBiE is the first binarization framework tailored for MoE LLMs, using joint SVD to reduce cross-... | `cs` |
| [[2604.07030v1]] MoE Routing Testbed: Studying Expert Speciali | The MoE Routing Testbed uses clearly separable data domains with a reference router to measure ex... | `cs` |
| [[2604.06956v1]] NestPipe: Large-Scale Recommendation Training | NestPipe introduces dual-level nested pipelining (DBP for inter-batch lookup, FWP for intra-batch... | `cs` |
| [[2604.06695v1]] Reasoning Fails Where Step Flow Breaks | Step-Saliency aggregates attention-gradient scores into step-level maps to reveal Shallow Lock-in... | `cs` |
| [[2604.06628v1]] Rethinking Generalization in Reasoning SFT: A | Demonstrates that cross-domain generalization in reasoning SFT is conditional, jointly shaped by ... | `cs` |
| [[2604.07171v1]] Smart Commander: A Hierarchical Reinforcement | Proposes Smart Commander, a two-tier hierarchical RL framework that decomposes fleet-level aviati... | `cs` |
| [[2604.06836v1]] STQuant: Spatio-Temporal Adaptive Framework f | STQuant dynamically allocates quantization precision for optimizer states across layers, state va... | `cs` |
| [[2604.07102v1]] The Impact of Steering Large Language Models  | Persona vector steering in LLMs degrades answer quality in educational settings, with open-ended ... | `cs` |

## Quantization & Precision

| Paper | TL;DR | Tags |
|-------|-------|------|
| [[2604.06832v1]] Fast-dVLM: Efficient Block-Diffusion VLM via  | Fast-dVLM converts autoregressive VLMs to block-diffusion models via direct one-stage conversion,... | `cs` |
| [[2604.06916v1]] FP4 Explore, BF16 Train: Diffusion Reinforcem | Proposes Sol-RL, a two-stage RL framework that uses NVFP4 quantization for high-throughput candid... | `cs` |
| [[2604.06767v1]] Geometric Properties of the Voronoi Tessellat | Validates the Voronoi tessellation linear scaling law on Qwen3.5-4B-Base with R^2 = 0.9997 by res... | `cs` |
| [[2604.06798v1]] MoBiE: Efficient Inference of Mixture of Bina | MoBiE is the first binarization framework tailored for MoE LLMs, using joint SVD to reduce cross-... | `cs` |
| [[2604.06836v1]] STQuant: Spatio-Temporal Adaptive Framework f | STQuant dynamically allocates quantization precision for optimizer states across layers, state va... | `cs` |

## LLM Evaluation & Benchmarking

| Paper | TL;DR | Tags |
|-------|-------|------|
| [[2604.06812v1]] AGSC: Adaptive Granularity and Semantic Clust | Proposes AGSC, an uncertainty quantification framework for long-form LLM generation that uses NLI... | `cs` |
| [[2604.06832v1]] Fast-dVLM: Efficient Block-Diffusion VLM via  | Fast-dVLM converts autoregressive VLMs to block-diffusion models via direct one-stage conversion,... | `cs` |
| [[2604.06723v1]] Fine-grained Approaches for Confidence Calibr | Proposes fine-grained local Platt-scaling for LLM confidence calibration in automated code revisi... | `cs` |
| [[2604.06652v1]] FlowAdam: Implicit Regularization via Geometr | Introduces FlowAdam, a hybrid optimizer that augments Adam with continuous gradient-flow ODE inte... | `cs` |
| [[2604.07035v1]] Gemma 4, Phi-4, and Qwen3: Accuracy-Efficienc | Controlled benchmark of 7 dense/MoE reasoning models across 4 benchmarks and 3 prompting strategi... | `cs` |
| [[2604.06767v1]] Geometric Properties of the Voronoi Tessellat | Validates the Voronoi tessellation linear scaling law on Qwen3.5-4B-Base with R^2 = 0.9997 by res... | `cs` |
| [[2604.07172v1]] Improving Semantic Uncertainty Quantification | First systematic evaluation of both calibration and discrimination in semantic UQ reveals fixed-t... | `cs` |
| [[2604.07095v1]] Multilingual Embedding Probes Fail to General | Probes trained on hidden-state activations from Qwen3-Embedding achieve strong in-distribution pe... | `cs` |
| [[2604.07343v1]] Personalized RewardBench: Evaluating Reward M | Introduces Personalized RewardBench, a benchmark that constructs chosen/rejected pairs based on u... | `cs` |
| [[2604.06996v1]] Self-Preference Bias in Rubric-Based Evaluati | LLM judges exhibit systematic self-preference bias in rubric-based evaluation, being up to 50% mo... | `cs` |
| [[2604.07190v1]] The ATOM Report: Measuring the Open Language  | A comprehensive ecosystem analysis of ~1.5K open language models reveals Chinese models (led by Q... | `cs` |
| [[2604.06613v1]] The Detection--Extraction Gap: Models Know th | Reveals that 52-88% of chain-of-thought tokens are produced after the answer is already recoverab... | `cs` |
| [[2604.07102v1]] The Impact of Steering Large Language Models  | Persona vector steering in LLMs degrades answer quality in educational settings, with open-ended ... | `cs` |

## Reasoning & Inference

| Paper | TL;DR | Tags |
|-------|-------|------|
| [[2604.06812v1]] AGSC: Adaptive Granularity and Semantic Clust | Proposes AGSC, an uncertainty quantification framework for long-form LLM generation that uses NLI... | `cs` |
| [[2604.07006v1]] Continuous Interpretive Steering for Scalar D | Continuous Interpretive Steering (CIS) treats activation steering strength as a continuous variab... | `cs` |
| [[2604.06832v1]] Fast-dVLM: Efficient Block-Diffusion VLM via  | Fast-dVLM converts autoregressive VLMs to block-diffusion models via direct one-stage conversion,... | `cs` |
| [[2604.06723v1]] Fine-grained Approaches for Confidence Calibr | Proposes fine-grained local Platt-scaling for LLM confidence calibration in automated code revisi... | `cs` |
| [[2604.07035v1]] Gemma 4, Phi-4, and Qwen3: Accuracy-Efficienc | Controlled benchmark of 7 dense/MoE reasoning models across 4 benchmarks and 3 prompting strategi... | `cs` |
| [[2604.07328v1]] How to sketch a learning algorithm | Introduces a data deletion scheme based on a "stability" assumption, using local sketching of ari... | `cs` |
| [[2604.07172v1]] Improving Semantic Uncertainty Quantification | First systematic evaluation of both calibration and discrimination in semantic UQ reveals fixed-t... | `cs` |
| [[2604.06798v1]] MoBiE: Efficient Inference of Mixture of Bina | MoBiE is the first binarization framework tailored for MoE LLMs, using joint SVD to reduce cross-... | `cs` |
| [[2604.07343v1]] Personalized RewardBench: Evaluating Reward M | Introduces Personalized RewardBench, a benchmark that constructs chosen/rejected pairs based on u... | `cs` |
| [[2604.06695v1]] Reasoning Fails Where Step Flow Breaks | Step-Saliency aggregates attention-gradient scores into step-level maps to reveal Shallow Lock-in... | `cs` |
| [[2604.07036v1]] ReDAct: Uncertainty-Aware Deferral for LLM Ag | ReDAct defers only ~15% of action decisions from a small LLM to a large LLM based on predictive u... | `cs` |
| [[2604.06628v1]] Rethinking Generalization in Reasoning SFT: A | Demonstrates that cross-domain generalization in reasoning SFT is conditional, jointly shaped by ... | `cs` |
| [[2604.07098v1]] Selective Neuron Amplification for Training-F | Introduces SNA, which identifies task-relevant neurons via differential activation analysis and s... | `cs` |
| [[2604.06996v1]] Self-Preference Bias in Rubric-Based Evaluati | LLM judges exhibit systematic self-preference bias in rubric-based evaluation, being up to 50% mo... | `cs` |
| [[2604.06746v1]] StructKV: Preserving the Structural Skeleton  | Proposes StructKV, a structure-aware KV cache compression framework that uses Global In-Degree Ce... | `cs` |
| [[2604.06613v1]] The Detection--Extraction Gap: Models Know th | Reveals that 52-88% of chain-of-thought tokens are produced after the answer is already recoverab... | `cs` |
| [[2604.06543v1]] The Illusion of Stochasticity in LLMs | LLMs fundamentally fail to map their internal probability estimates to stochastic outputs when ac... | `cs` |
| [[2604.07102v1]] The Impact of Steering Large Language Models  | Persona vector steering in LLMs degrades answer quality in educational settings, with open-ended ... | `cs` |

## Uncertainty & Calibration

| Paper | TL;DR | Tags |
|-------|-------|------|
| [[2604.06812v1]] AGSC: Adaptive Granularity and Semantic Clust | Proposes AGSC, an uncertainty quantification framework for long-form LLM generation that uses NLI... | `cs` |
| [[2604.07325v1]] Conformal Prediction with Time-Series Data vi | Proposes Sequential Conformalized Density Regions (SCDR), a conformal prediction method for time-... | `stat` |
| [[2604.06723v1]] Fine-grained Approaches for Confidence Calibr | Proposes fine-grained local Platt-scaling for LLM confidence calibration in automated code revisi... | `cs` |
| [[2604.07172v1]] Improving Semantic Uncertainty Quantification | First systematic evaluation of both calibration and discrimination in semantic UQ reveals fixed-t... | `cs` |
| [[2604.07036v1]] ReDAct: Uncertainty-Aware Deferral for LLM Ag | ReDAct defers only ~15% of action decisions from a small LLM to a large LLM based on predictive u... | `cs` |
| [[2604.07102v1]] The Impact of Steering Large Language Models  | Persona vector steering in LLMs degrades answer quality in educational settings, with open-ended ... | `cs` |

## ML Reliability & Robustness

| Paper | TL;DR | Tags |
|-------|-------|------|
| [[2604.07306v1]] Beyond Loss Values: Robust Dynamic Pruning vi | AlignPrune replaces per-sample loss-based ranking with Dynamic Alignment Score (DAS) that measure... | `cs` |
| [[2604.07325v1]] Conformal Prediction with Time-Series Data vi | Proposes Sequential Conformalized Density Regions (SCDR), a conformal prediction method for time-... | `stat` |
| [[2604.06899v1]] Data Leakage in Automotive Perception: Practi | Through 10 semi-structured interviews with automotive perception practitioners at an OEM (Volvo C... | `cs` |
| [[2604.06542v1]] Does a Global Perspective Help Prune Sparse M | GRAPE (Global Redundancy-Aware Pruning of Experts) dynamically allocates pruning budgets based on... | `cs` |
| [[2604.06893v1]] Energy-Regularized Spatial Masking: A Novel A | ERSM reformulates feature selection as a differentiable energy minimization problem, producing em... | `cs` |
| [[2604.06723v1]] Fine-grained Approaches for Confidence Calibr | Proposes fine-grained local Platt-scaling for LLM confidence calibration in automated code revisi... | `cs` |
| [[2604.06652v1]] FlowAdam: Implicit Regularization via Geometr | Introduces FlowAdam, a hybrid optimizer that augments Adam with continuous gradient-flow ODE inte... | `cs` |
| [[2604.06664v1]] Foundry: Template-Based CUDA Graph Context Ma | Foundry materializes CUDA graph execution context during offline processing and reconstructs exec... | `cs` |
| [[2604.06916v1]] FP4 Explore, BF16 Train: Diffusion Reinforcem | Proposes Sol-RL, a two-stage RL framework that uses NVFP4 quantization for high-throughput candid... | `cs` |
| [[2604.07233v1]] How Does Machine Learning Manage Complexity? | Abstracts ML models as P/poly-computable distributions with polynomially-bounded max entropy, pro... | `cs` |
| [[2604.07328v1]] How to sketch a learning algorithm | Introduces a data deletion scheme based on a "stability" assumption, using local sketching of ari... | `cs` |
| [[2604.06798v1]] MoBiE: Efficient Inference of Mixture of Bina | MoBiE is the first binarization framework tailored for MoE LLMs, using joint SVD to reduce cross-... | `cs` |
| [[2604.07030v1]] MoE Routing Testbed: Studying Expert Speciali | The MoE Routing Testbed uses clearly separable data domains with a reference router to measure ex... | `cs` |
| [[2604.06956v1]] NestPipe: Large-Scale Recommendation Training | NestPipe introduces dual-level nested pipelining (DBP for inter-batch lookup, FWP for intra-batch... | `cs` |
| [[2604.07254v1]] Non-identifiability of Explanations from Mode | Deep networks predicting human authenticity judgments produce divergent attribution explanations ... | `cs` |
| [[2604.07036v1]] ReDAct: Uncertainty-Aware Deferral for LLM Ag | ReDAct defers only ~15% of action decisions from a small LLM to a large LLM based on predictive u... | `cs` |
| [[2604.06996v1]] Self-Preference Bias in Rubric-Based Evaluati | LLM judges exhibit systematic self-preference bias in rubric-based evaluation, being up to 50% mo... | `cs` |
| [[2604.07171v1]] Smart Commander: A Hierarchical Reinforcement | Proposes Smart Commander, a two-tier hierarchical RL framework that decomposes fleet-level aviati... | `cs` |
| [[2604.06836v1]] STQuant: Spatio-Temporal Adaptive Framework f | STQuant dynamically allocates quantization precision for optimizer states across layers, state va... | `cs` |
| [[2604.06746v1]] StructKV: Preserving the Structural Skeleton  | Proposes StructKV, a structure-aware KV cache compression framework that uses Global In-Degree Ce... | `cs` |
| [[2604.06543v1]] The Illusion of Stochasticity in LLMs | LLMs fundamentally fail to map their internal probability estimates to stochastic outputs when ac... | `cs` |

## Other Relevant

| Paper | TL;DR | Tags |
|-------|-------|------|
| [[2604.07242v1]] Weaves, Wires, and Morphisms: Formalizing and | Introduces a categorical framework formalizing broadcasting in deep learning through axis-stride ... | `cs` |

---

## All Papers

| # | Paper | Authors | Key Topic | TL;DR |
|---|-------|---------|-----------|-------|
| 1 | [[2604.06812v1]] AGSC: Adaptive Granularity and Semantic  | Guanran Luo et al. | LLM Evaluation | Proposes AGSC, an uncertainty quantification framework for long-form LLM gene... |
| 2 | [[2604.07282v1]] Are Face Embeddings Compatible Across De | Fizza Rubab et al. | Interpretability | Simple linear transformations can align face embeddings across independently ... |
| 3 | [[2604.07306v1]] Beyond Loss Values: Robust Dynamic Pruni | Huaiyuan Qin et al. | Training Stability | AlignPrune replaces per-sample loss-based ranking with Dynamic Alignment Scor... |
| 4 | [[2604.07154v1]] Bridging MRI and PET physiology: Untangl | Sonja Adomeit et al. | Interpretability | A subspace decomposition framework separates PSMA PET uptake into MRI-explain... |
| 5 | [[2604.07019v1]] ConceptTracer: Interactive Analysis of C | Ricardo Knauer et al. | Interpretability | Introduces ConceptTracer, an interactive tool using two information-theoretic... |
| 6 | [[2604.07325v1]] Conformal Prediction with Time-Series Da | M. Sampson et al. | Uncertainty | Proposes Sequential Conformalized Density Regions (SCDR), a conformal predict... |
| 7 | [[2604.07006v1]] Continuous Interpretive Steering for Sca | Ye-eun Cho et al. | Interpretability | Continuous Interpretive Steering (CIS) treats activation steering strength as... |
| 8 | [[2604.06899v1]] Data Leakage in Automotive Perception: P | Md Abu Ahammed Babu et al. | Interpretability | Through 10 semi-structured interviews with automotive perception practitioner... |
| 9 | [[2604.07166v1]] DINO-QPM: Adapting Visual Foundation Mod | Robert Zimmermann et al. | Interpretability | DINO-QPM adapts the QPM framework to frozen DINOv2 backbones, converting enta... |
| 10 | [[2604.06542v1]] Does a Global Perspective Help Prune Spa | Zeliang Zhang et al. | Training Stability | GRAPE (Global Redundancy-Aware Pruning of Experts) dynamically allocates prun... |
| 11 | [[2604.06893v1]] Energy-Regularized Spatial Masking: A No | Tom Devynck et al. | Interpretability | ERSM reformulates feature selection as a differentiable energy minimization p... |
| 12 | [[2604.06832v1]] Fast-dVLM: Efficient Block-Diffusion VLM | Chengyue Wu et al. | Quantization | Fast-dVLM converts autoregressive VLMs to block-diffusion models via direct o... |
| 13 | [[2604.06723v1]] Fine-grained Approaches for Confidence C | Hong Yi Lin et al. | LLM Evaluation | Proposes fine-grained local Platt-scaling for LLM confidence calibration in a... |
| 14 | [[2604.06652v1]] FlowAdam: Implicit Regularization via Ge | Devender Singh et al. | Interpretability | Introduces FlowAdam, a hybrid optimizer that augments Adam with continuous gr... |
| 15 | [[2604.06664v1]] Foundry: Template-Based CUDA Graph Conte | Xueshen Liu et al. | ML Reliability | Foundry materializes CUDA graph execution context during offline processing a... |
| 16 | [[2604.06916v1]] FP4 Explore, BF16 Train: Diffusion Reinf | Yitong Li et al. | Training Stability | Proposes Sol-RL, a two-stage RL framework that uses NVFP4 quantization for hi... |
| 17 | [[2604.07035v1]] Gemma 4, Phi-4, and Qwen3: Accuracy-Effi | Md Motaleb Hossen... et al. | Interpretability | Controlled benchmark of 7 dense/MoE reasoning models across 4 benchmarks and ... |
| 18 | [[2604.06767v1]] Geometric Properties of the Voronoi Tess | Marshall Brett et al. | Interpretability | Validates the Voronoi tessellation linear scaling law on Qwen3.5-4B-Base with... |
| 19 | [[2604.07233v1]] How Does Machine Learning Manage Complex | Lance Fortnow et al. | ML Reliability | Abstracts ML models as P/poly-computable distributions with polynomially-boun... |
| 20 | [[2604.07328v1]] How to sketch a learning algorithm | Sam Gunn et al. | Interpretability | Introduces a data deletion scheme based on a "stability" assumption, using lo... |
| 21 | [[2604.07172v1]] Improving Semantic Uncertainty Quantific | Tom A. Lamb et al. | Training Stability | First systematic evaluation of both calibration and discrimination in semanti... |
| 22 | [[2604.07108v1]] Information as Structural Alignment: A D | Radu Negulescu et al. | Training Stability | Introduces IBF, a continual learning framework based on structural alignment ... |
| 23 | [[2604.06966v1]] MAR-GRPO: Stabilized GRPO for AR-diffusi | Xiaoxiao Ma et al. | Training Stability | Identifies the diffusion head as a key source of optimization instability in ... |
| 24 | [[2604.06798v1]] MoBiE: Efficient Inference of Mixture of | Zhixiong Zhao et al. | Training Stability | MoBiE is the first binarization framework tailored for MoE LLMs, using joint ... |
| 25 | [[2604.07030v1]] MoE Routing Testbed: Studying Expert Spe | Tobias Falke et al. | Training Stability | The MoE Routing Testbed uses clearly separable data domains with a reference ... |
| 26 | [[2604.07095v1]] Multilingual Embedding Probes Fail to Ge | Laurits Lyngbaek et al. | Interpretability | Probes trained on hidden-state activations from Qwen3-Embedding achieve stron... |
| 27 | [[2604.06956v1]] NestPipe: Large-Scale Recommendation Tra | Zhida Jiang et al. | Training Stability | NestPipe introduces dual-level nested pipelining (DBP for inter-batch lookup,... |
| 28 | [[2604.07254v1]] Non-identifiability of Explanations from | Icaro Re Depaolini et al. | Interpretability | Deep networks predicting human authenticity judgments produce divergent attri... |
| 29 | [[2604.07343v1]] Personalized RewardBench: Evaluating Rew | Qiyao Ma et al. | LLM Evaluation | Introduces Personalized RewardBench, a benchmark that constructs chosen/rejec... |
| 30 | [[2604.07016v1]] Predictive Representations for Skill Tra | Ruben Vereecken et al. | Interpretability | OPSRs provide task-independent state abstractions based on outcome prediction... |
| 31 | [[2604.06695v1]] Reasoning Fails Where Step Flow Breaks | Xiaoyu Xu et al. | Interpretability | Step-Saliency aggregates attention-gradient scores into step-level maps to re... |
| 32 | [[2604.07036v1]] ReDAct: Uncertainty-Aware Deferral for L | Dzianis Piatrashyn et al. | Reasoning | ReDAct defers only ~15% of action decisions from a small LLM to a large LLM b... |
| 33 | [[2604.06628v1]] Rethinking Generalization in Reasoning S | Qihan Ren et al. | Training Stability | Demonstrates that cross-domain generalization in reasoning SFT is conditional... |
| 34 | [[2604.07098v1]] Selective Neuron Amplification for Train | Ryyan Akhtar et al. | Interpretability | Introduces SNA, which identifies task-relevant neurons via differential activ... |
| 35 | [[2604.06996v1]] Self-Preference Bias in Rubric-Based Eva | Jose Pombal et al. | LLM Evaluation | LLM judges exhibit systematic self-preference bias in rubric-based evaluation... |
| 36 | [[2604.07171v1]] Smart Commander: A Hierarchical Reinforc | Yong Si et al. | Training Stability | Proposes Smart Commander, a two-tier hierarchical RL framework that decompose... |
| 37 | [[2604.06836v1]] STQuant: Spatio-Temporal Adaptive Framew | Minglu Liu et al. | Training Stability | STQuant dynamically allocates quantization precision for optimizer states acr... |
| 38 | [[2604.06746v1]] StructKV: Preserving the Structural Skel | Zhirui Chen et al. | Reasoning | Proposes StructKV, a structure-aware KV cache compression framework that uses... |
| 39 | [[2604.07190v1]] The ATOM Report: Measuring the Open Lang | Nathan Lambert et al. | LLM Evaluation | A comprehensive ecosystem analysis of ~1.5K open language models reveals Chin... |
| 40 | [[2604.06613v1]] The Detection--Extraction Gap: Models Kn | Hanyang Wang et al. | LLM Evaluation | Reveals that 52-88% of chain-of-thought tokens are produced after the answer ... |
| 41 | [[2604.06543v1]] The Illusion of Stochasticity in LLMs | Xiangming Gu et al. | Reasoning | LLMs fundamentally fail to map their internal probability estimates to stocha... |
| 42 | [[2604.07102v1]] The Impact of Steering Large Language Mo | Yongchao Wu et al. | Interpretability | Persona vector steering in LLMs degrades answer quality in educational settin... |
| 43 | [[2604.07242v1]] Weaves, Wires, and Morphisms: Formalizin | Vincent Abbott et al. | Other Relevant | Introduces a categorical framework formalizing broadcasting in deep learning ... |

---
*Overview generated on 2026-04-10*