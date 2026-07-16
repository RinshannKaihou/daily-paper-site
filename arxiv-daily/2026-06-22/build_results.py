#!/usr/bin/env python3
"""Compile WebFetch results into search_results.json"""
import json

papers = {}

# cs.LG listing (titles only)
lg_listing = [
    "2606.23676|Open Problem: Is AdamW Effective Under Heavy-Tailed Noise?",
    "2606.23670|Tapered Language Models",
    "2606.23668|On the Limits of Prompt-Conditioned Language Models as General-Purpose Learners",
    "2606.23664|MAS-PromptBench: When Does Prompt Optimization Improve Multi-Agent LLM Systems?",
    "2606.23655|Dynamic estimation of slowly varying sequences",
    "2606.23640|Learning Process Rewards via Success Visitation Matching for Efficient RL",
    "2606.23637|Muown Implicitly Performs Angular Step-size Decay",
    "2606.23626|DiT-Reward: Generative Representations for Text-to-Image Reward Modeling",
    "2606.23609|Discovering Latent Groups for Robust Classification",
    "2606.23607|Scaling Linear Mode Connectivity and Merging to Billion Parameter Pretrained Transformers",
    "2606.23603|MORL-A2C: Multi-Objective Reinforcement Learning Reranker for Optimizing Healthiness in MOPI-HFRS",
    "2606.23591|Quantifying the Agreement Between Data-Influence and Data-Similarity to Understand LLM Behavior",
    "2606.23587|It's Much Easier for Neural Networks to learn Game of Life Dynamics with the Right Activation Function: Polynomial Kolmogorov-Arnold Networks",
    "2606.23575|Solve for the Hyperparameter, Skip the Search: Kolmogorov-Optimal Scaling Laws for Spline Regression",
    "2606.23572|A Spectral Theory of Normalized Corrected GNN Propagation",
    "2606.23568|SVD-Surgeon: Optimal Singular-Value Surgery for Large Language Model Compression",
    "2606.23567|Scheduling Thoughts: Learning the Order of Thought in Diffusion Language Models",
    "2606.23546|The Energy Consumption of Transformer Fine-Tuning: A Roofline-Inspired Scaling Model",
    "2606.23496|TROPT: An Open Framework for Unifying and Advancing Discrete Text Optimization",
    "2606.23419|GRINQH: Graded Input-based Quantization Hierarchy for Efficient LLM Generation",
    "2606.23406|HyperQuant: A Rate-Distortion-Optimal Quantization Pipeline for Large Language and Diffusion Models",
    "2606.23391|Distribution-Aware Diffusion-LLM for Robust Ultra-Long-Term Time Series Forecasting",
    "2606.23364|Convergence of Gradient Descent for General Neural Network Architectures Beyond the NTK Regime",
    "2606.23357|SOAP-Bubbles: Structured Weight Uncertainty for Neural Networks",
    "2606.23348|Superhuman AI for Generals.io Using Self-Play Reinforcement Learning",
    "2606.23299|GRIMIP: A General Framework for Instance-Specific Configuration of MIP Solvers Using LLMs",
    "2606.23276|Exposing the Illusion of Erasure in Knowledge Editing for LLMs",
    "2606.23195|Memory Contagion: Cross-Temporal Propagation of Evaluator Bias via Agent Memory",
    "2606.23175|Position: Correct Answer, Wrong Mechanism -- When AI Scientists Defend General Claims Their Own Data Contradicts",
]

# cs.CL listing
cl_listing = [
    "2606.23687|Randomized YaRN Improves Length Generalization for Long-Context Reasoning",
    "2606.23671|Can LLMs Reliably Self-Report Adversarial Prefills, and How?",
    "2606.23654|EnterpriseClawBench: Benchmarking Agents from Real Workplace Sessions",
    "2606.23583|Evaluation Awareness Is Not One Capability: Evidence from Open Language Models",
    "2606.23566|LangMAP: A Language-Adaptive Approach to Tokenization",
    "2606.23525|Self-Compacting Language Model Agents",
    "2606.23459|TriggerBench: Investigating Prospective Memory for Large Language Models",
    "2606.23404|ReasoningLens: Hierarchical Visualization and Diagnostic Auditing for Large Reasoning Models",
    "2606.23394|Do LLM Embedding Spaces Recover Expert Structure?",
    "2606.23382|Energy-Based Transformers as Predictors of Reading Difficulty",
    "2606.23375|Measuring & Mitigating Over-Alignment for LLMs in Multilingual Criminal Law Courts",
    "2606.23336|WaveDetect: Robust Framework for Machine-Generated Text Detection via Wavelet Transform",
    "2606.23321|Tmax: A simple recipe for terminal agents",
    "2606.23283|Towards Root Memories: Benchmarking and Enhancing Implicit Logical Memory Retrieval for Personalized LLMs",
    "2606.23271|Scaling LLM Knowledge Boundaries via Distribution-Optimized Synthesis",
    "2606.23196|When Does Intrinsic Self-Correction Help? A Task-Sensitive Analysis",
    "2606.22942|Understanding Knowledge Distillation in Post-Training: When It Helps and When It Fails",
    "2606.22877|DynamicMem: A Long-Horizon Memory Benchmark in Real-World Settings",
    "2606.22807|KaLM-Reranker-V1: Fast but Not Late Interaction for Compressed Document Reranking",
    "2606.22798|Does the Same Token Mean the Same State? MoE Routing as Signal for Reasoning Control",
    "2606.22728|When Confidence Takes the Wrong Path: Diagnosing Retrieval-State Lock-In in RAG",
    "2606.22681|Only Ask What You Don't Know: Grounded Delta Planning for Efficient Multi-step RAG",
    "2606.22627|Orthogonal Representation Editing: Decoupling Semantic Entanglement in Batch Knowledge Editing of LLMs",
    "2606.22570|What are Key Factors for Updates in RL for LLM Reasoning?",
]

# cs.AI listing
ai_listing = [
    "2606.23673|PsyBridge: A Hybrid Intelligent Framework for Multi-Dimensional Mental Health Assessment and Decision Support",
    "2606.23672|Teaching LLMs String Matching, Backtracking, and Error Recovery to Deduce Bases and Truth Tables for the Combinatorially Exploding Bit Manipulation Puzzles",
    "2606.23643|TailorMind: Towards Preference-Aligned Multimodal Content Generation",
    "2606.23608|Causal Discovery in the Era of Agents",
    "2606.23597|Against Proxy Optimization",
    "2606.23595|SPIRAL: Learning to Search and Aggregate",
    "2606.23590|The Topology of Ill-Posed Questions: Persistent Homology for Detection and Steering in LLMs",
    "2606.23543|VeriEvol: Scaling Multimodal Mathematical Reasoning via Verifiable Evol-Instruct",
    "2606.23449|AOHP: An Open-Source OS-Level Agent Harness for Personalized, Efficient and Secure Interaction",
    "2606.23403|Litmus: Zero-Label, Code-Driven Metric Specification for Evaluating AI Systems",
    "2606.23345|Abstract representational geometry supports inference in large language models",
    "2606.23277|GIF: Locally Sound Geometric Information Flow Control for LLMs",
    "2606.23238|HOLMES: Evaluating Higher-Order Logical Reasoning in LLMs",
    "2606.23181|DART: Draft-Agreement Routing for Training-Free Adaptive Thinking Budgets in Hybrid Reasoning Models",
    "2606.23127|Managing Procedural Memory in LLM Agents: Control, Adaptation, and Evaluation",
    "2606.22974|When Preferences Fail to Become Incentives: A Utility-Behavior Gap in Large Language Models",
    "2606.22953|Plans Don't Persist: Why Context Management Is Load Bearing for LLM Agents",
    "2606.22948|ENVS: Environment-Native Verified Search for Long-Horizon GUI Agents",
    "2606.22936|When Agents Commit Too Soon: Diagnosing Premature Commitment in LLM Agents",
    "2606.22916|Intent-Governed Tool Authorization for AI Agents",
    "2606.22902|Agent-as-a-Router: Agentic Model Routing for Coding Tasks",
    "2606.22883|CLI-Universe: Towards Verifiable Task Synthesis Engine for Terminal Agents",
    "2606.22859|AI Scientists as Engines of Discovery: A Case for Development within Reformed Institutions",
    "2606.22844|RaMem: Contextual Reinstatement for Long-term Agentic Memory",
    "2606.22830|Finding the Evidence: Discovering Decision-Supporting Tokens for On-Policy Reasoning Distillation",
    "2606.22826|MINCE: Shrinking LLM Evaluation Datasets via Few-Model Monte Carlo Calibration",
    "2606.22813|Active Inference as the Test-Time Scaling Law for Physical AI Agents",
    "2606.22797|Measuring Behavior Portability in Large Language Models",
    "2606.22793|A Formula-Driven Survey and Research Agenda for On-Policy Distillation",
]

# cs.CV listing (selected relevant ones)
cv_listing = [
    "2606.23678|AIR: Adaptive Interleaved Reasoning with Code in MLLMs",
    "2606.23611|Data Selection Through Iterative Self-Filtering for Vision-Language Settings",
    "2606.23539|LightSTAR: Efficient Visual Document Retrieval via Lightweight Selection with Vision-Adaptive Refinement",
    "2606.23524|Scaling State-Space Models from Lines to Paragraphs: An Ablation of Mamba-based OCR",
    "2606.23344|RT-DocLayout: Real-Time End-to-End Document Layout Analysis with Reading Order in the Wild",
    "2606.23327|VideoAgent: All-in-One Framework for Video Understanding and Editing",
    "2606.23132|T-VSS: Test-Time Visual Subspace Steering for Adversarial Robustness of Vision-Language Models",
    "2606.23129|Spectral Gating via Damped Oscillations for Adaptive Implicit Neural Representations",
    "2606.23126|MambaADv2: Evolving Duality-enhanced State Space Model for Unsupervised Anomaly Detection",
    "2606.23206|CFPO: Counterfactual Policy Optimization for Multimodal Reasoning",
]

# stat.ML listing (selected relevant ones)
statml_listing = [
    "2606.23662|Action-BED: Task-Driven Bayesian Experimental Design with Singly Intractable Objectives",
    "2606.23627|Diffusion Models Adapt to Low-Dimensional Structure Under Flexible Coefficient Choices",
    "2606.23601|Neural Networks as Linear Regression: An Introduction for Statisticians",
    "2606.23477|Sublinearly Structured Deep Neural Networks Achieve Feature Learning Consistency for Compositional Functions",
    "2606.22521|Robust Diffusion Models via Divergence-Induced Weighted Denoising",
    "2606.22511|Breaking the Likelihood Trap: Variance-Calibrated Modulation for Large Language Model Decoding",
    "2606.22406|Asymptotic Signal Subspace Recovery in Softmax Attention Models",
    "2606.22326|Adam Converges in Nonsmooth Nonconvex Optimization",
    "2606.21036|Diffusion-Driven State Space Models",
    "2606.20678|Beyond Importance: Interchange-Sobol Sensitivity Reveals Task-Specific Content Channels in Transformer Components",
    "2606.23235|A First-Order Mean Field Control Analysis of Transformer Layers under Cross-Entropy Training",
    "2606.22652|A Markov Chain Approach to Preference Alignment",
]

# RSS abstracts (cs.LG)
lg_abstracts = {
    "2606.20743": "Trained transformers reliably develop massive activations, a small number of hidden dimensions whose magnitude is far above the median and which concentrate on the sequence-start token. Whether these outliers are a removable artifact of the residual stream's overloaded read and write role, or instead a functional necessity, is actively debated.",
    "2606.20820": "Can we trust evaluation scores to capture an LLM's true real-world performance? Certifiable evaluation answers this question by providing guarantee for LLM evaluation. In particular, existing methods sequentially curate evaluation samples and keep updating confidence intervals (CIs) that cover the true performance with high probability.",
    "2606.20945": "Self-attention is central to Transformer performance and is often the most expensive part of the Transformer at long context lengths because its pairwise token interactions scale quadratically with sequence length. Standard dense attention also applies the same set of attention heads to every token regardless of token difficulty or information content.",
    "2606.20959": "Large language models can store both outdated facts and newer superseding facts in their parameters, but standard prompting may still elicit the outdated answer. We formalize this problem as Parametric Temporal Conflict (PTC) and introduce Temporal Attractor Steering (TAS), a three-stage test-time intervention that detects likely conflicts.",
    "2606.20937": "We study internalization processes, by which neural-network-based systems absorb an explicit computational procedure into their own weights, and how they facilitate learning. We investigate how transformers internalize the simulation of semiautomata by internalizing chain-of-thought (CoT) tokens.",
    "2606.21023": "As Large Language Models (LLMs) deploy into mission-critical domains (e.g., finance, medicine, and law), output reproducibility has become a strict system requirement. While practitioners use greedy decoding to eliminate algorithmic stochasticity, empirical deployments with 16-bit precisions still exhibit catastrophic output divergence.",
    "2606.21158": "Singular learning theory characterises the complexity of a deep network through the geometry of its loss singularities. The local learning coefficient (LLC), the standard estimator of Watanabe's real log canonical threshold (RLCT), reads this geometry as an integrated Bayesian scalar through SGLD.",
    "2606.21228": "The capabilities of frontier Large Language Models (LLMs) continue to advance, with different providers increasingly specializing in distinct domains. This raises a natural next objective: how to combine the individual specializations of various LLMs into a collectively intelligent system. To this end, we report the development of Sakana Fugu, a family of orchestrator models.",
    "2606.21249": "Retrieval heads, attention heads that copy information from earlier context to the current position, have been proposed as the mechanistic substrate for long-context recall. Rotary position embeddings (RoPE) rotate queries and keys by frequencies decaying with a base hyperparameter theta.",
}

# RSS abstracts (cs.CL)
cl_abstracts = {
    "2606.20740": "Process Reward Models provide step-level verification for LLM reasoning, yet training data acquisition remains a bottleneck. This work proposes VeriBound, providing PAC-Bayesian bounds for PRMs trained with formal verification tools like Z3.",
    "2606.20936": "Hybrid language models mixing attention and recurrent layers show promise, yet which data drives gains remains unclear. This work compares matched transformer and hybrid models at token level using Olmo 3.",
    "2606.20954": "Long-running LLM systems accumulate interaction history exceeding context windows. This work presents LRE, a few-kilobyte CPU-only scorer learning which units of history are load-bearing for task completion.",
    "2606.21345": "LLMs store factual knowledge, yet how entity representations transform for attribute retrieval remains underexplored. This work identifies attribute-computation paths revealing redundancy and non-contiguity.",
    "2606.21359": "LLMs communicate scientific concepts yet hallucinate. This work introduces SciFactCheck, a benchmark of 2,500 prompts across five domains evaluating factuality hallucination types.",
    "2606.21255": "Rejecting inputs outside service scope is critical for LLM services. SCOPE selects readable hidden layers, constructs conformal gates, and uses supermartingale e-processes.",
    "2606.21075": "Standard Transformers use single self-attention pathways modeling both global and local dependencies. This work proposes a dual-branch design with feature-wise linear modulation for dynamic cross-branch coordination.",
    "2606.21082": "Multi-turn jailbreaks evade turn-level moderation by spreading unsafe intent across dialogue. This work introduces an efficient hierarchical detector avoiding expensive long-context concatenation.",
    "2606.21144": "Long-term memory systems accumulate histories exceeding context budgets. AdaMem learns what to remember for each user from feedback through lightweight, patch-style self-reflection.",
}

# RSS abstracts (cs.AI)
ai_abstracts = {
    "2606.20657": "Autonomous post-training system running without human intervention, achieving 0.86 on held-out score while detecting when measurement frame became misleading and revising search policy.",
    "2606.20622": "Introduction of open-source infrastructure for autonomous reinforcement learning using mobile GUI as proxy for complex environments, with roadmap for removing human priors from task curricula, verification, and memory.",
    "2606.20625": "Proposal of self-evolving alpha mining agent with structured search-process memory recording reusable evidence about edit motifs, using confidence-gated residual memory and asymmetric veto control.",
    "2606.20631": "Study of agent skill harnessing providing ten empirically grounded architectural patterns synthesized into reference architecture with four responsibility layers for skill-in-use management.",
    "2606.20638": "Continual adaptation framework for language-model systems learning through verifier-gated memory, routing, and prompt compilation with dynamically spawned memory branches.",
    "2606.20661": "Framework KAPRO evaluating cognitive-behavioral alignment by decoupling metacognitive judgment from spontaneous execution, showing sharp degradation in internal-capability settings.",
    "2606.20662": "Identification of confidence laundering failure mode where fragile upstream decisions repackaged as valid artifacts downstream, proposing latent uncertainty as solution.",
    "2606.20814": "Study examining emergent misalignment through training dynamics, model priors, and data, showing pre-trained model activations predict fine-grained alignment scores.",
    "2606.20839": "Training framework turning verified workflow rollouts into reusable tactics, evaluating process-supervised tactic accumulation for bioinformatics workflow completion.",
    "2606.20624": "Mathematical formalization of rational value risk showing gap between deployed reasoning strategies and utility-maximizing counterparts, with extensive experiments demonstrating widespread irrationality in LLM reasoning.",
    "2606.20718": "Mathematical framework using dynamical systems theory demonstrating how sycophantic feedback creates deep attractor basins, showing strong external evidence can restore objective belief.",
    "2606.20785": "Scalable data pipeline for computer use agents using live websites and synthetic environments, training Fara1.5 family achieving new state-of-art for size classes.",
}

def add_papers(entries, category):
    for entry in entries:
        parts = entry.split("|", 1)
        aid = parts[0].strip()
        title = parts[1].strip()
        if aid not in papers:
            papers[aid] = {
                "arxiv_id": aid,
                "title": title,
                "authors": [],
                "abstract": "",
                "categories": [category],
                "published": "2026-06-22",
                "pdf_url": f"https://arxiv.org/pdf/{aid}.pdf",
                "abs_url": f"https://arxiv.org/abs/{aid}",
            }
        else:
            if category not in papers[aid]["categories"]:
                papers[aid]["categories"].append(category)

add_papers(lg_listing, "cs.LG")
add_papers(cl_listing, "cs.CL")
add_papers(ai_listing, "cs.AI")
add_papers(cv_listing, "cs.CV")
add_papers(statml_listing, "stat.ML")

# Merge in abstracts
for abstracts in [lg_abstracts, cl_abstracts, ai_abstracts]:
    for aid, abstract in abstracts.items():
        if aid in papers:
            papers[aid]["abstract"] = abstract
        else:
            papers[aid] = {
                "arxiv_id": aid,
                "title": f"[from RSS - {aid}]",
                "authors": [],
                "abstract": abstract,
                "categories": [],
                "published": "2026-06-22",
                "pdf_url": f"https://arxiv.org/pdf/{aid}.pdf",
                "abs_url": f"https://arxiv.org/abs/{aid}",
            }

# Add RSS-only papers with titles
rss_titles = {
    "2606.20743": "Massive Activations Are Architecturally Robust: A Controlled Scratch/Commitment Residual Stream Test",
    "2606.20820": "CELEUS: Certifiable and Efficient LLM Evaluation via E-Processes",
    "2606.20945": "Grouped Query Experts: Mixture-of-Experts on GQA Self-Attention",
    "2606.20959": "Right Knowledge, Wrong Answer: Test-Time Steering for Temporal Fact Conflicts in Open-Weight Language Models",
    "2606.20937": "Learning through Internalization",
    "2606.21023": "Demystifying Numerical Instability in LLM Inference: Achieving Reproducible Inference for Mission-Critical Tasks with HEAL",
    "2606.21158": "Dead-Direction Signatures: A Cheap Spectral Reading of Singular Complexity",
    "2606.21228": "Sakana Fugu Technical Report",
    "2606.21249": "Does RoPE Prevent or Degrade Retrieval Heads? A Mechanistic Analysis Across Model Families",
    "2606.20740": "VeriBound: PAC-Bayesian Generalization Bounds for Process Reward Models Trained with Formal Verification Tools",
    "2606.20936": "Comparing Transformers and Hybrid Models at the Token Level",
    "2606.20954": "Learning What Not to Forget: Long-Horizon Agent Memory from a Few Kilobytes of Learning",
    "2606.21345": "Factual Retrieval in LLMs Is a Redundant, Distributed and Non-Contiguous Process",
    "2606.21359": "Finetuning with Scientific Data Increases Hallucinations: A Multi-domain Factuality Evaluation of LLMs",
    "2606.21255": "SCOPE: Sequential Conformal Probing for Reliable OOD Rejection in LLM Services",
    "2606.21075": "FiLM-Coordinated Dual-Branch Transformer for Global-Local Dependency Modeling in Language Modeling",
    "2606.21082": "Scalable Hierarchical Attention Transformers for Multi-Turn Jailbreak Detection in Long Conversations",
    "2606.21144": "AdaMem: Learning What to Remember for Personalized Long-Horizon LLM Agents",
    "2606.20657": "A-Evolve-Training: Autonomous Post-Training of a 30B Model",
    "2606.20622": "Darwin Mobile Agent: A Roadmap for Self-Evolution",
    "2606.20625": "AlphaMemo: Structured Search-Process Memory for Self-Evolving Alpha Mining Agents",
    "2606.20631": "Harnessing Agent Skills: Architectural Patterns and a Reference Architecture for Skill-Mediated LLM Agents",
    "2606.20638": "RIZZ: Routing Interactions to Near Zero-Interference Zones for Continual Adaptation of Black-Box Agents",
    "2606.20661": "From Knowing to Acting: Benchmarking Self-Awareness Capability of LLM Agents",
    "2606.20662": "Confidence Laundering in Agent Systems: Why Uncertainty Needs a Latent Carrier",
    "2606.20814": "What Shapes Emergent Misalignment? Insights from Training Dynamics, Model Priors, and Data",
    "2606.20839": "Process-Reward Tactic Evolution for Long-Horizon Bioinformatics Workflows",
    "2606.20624": "In LLM Reasoning, there is Irrationality on top of Value Misalignment",
    "2606.20718": "Escape from Delusional Echo Trap: Symmetry Breaking, Stochastic Dynamics and Mathematical Mitigation Strategies for Algorithmic Sycophancy",
    "2606.20785": "Fara-1.5: Scalable Learning Environments for Computer Use Agents",
    "2606.20961": "Is Our Benchmark Enough? An Analysis of Continual Learning for MLLMs",
    "2606.20967": "Formalizing Task-Space Complexity for Zero-Shot Generalization",
}

for aid, title in rss_titles.items():
    if aid in papers and papers[aid]["title"].startswith("[from RSS"):
        papers[aid]["title"] = title

result = list(papers.values())
with open("/Users/ywang2397/Documents/daily_paper/arxiv-daily/2026-06-22/search_results.json", "w") as f:
    json.dump(result, f, indent=2, ensure_ascii=False)

print(f"Total unique papers: {len(result)}")
