import json
import re
import os

with open('/Users/ywang2397/Documents/daily_paper/arxiv-daily/2026-06-01/search_results.json', 'r') as f:
    data = json.load(f)

papers = data['papers']

def clean_arxiv_id(arxiv_id):
    return re.sub(r'\.v\d+$', '', arxiv_id)

manual_scores = {
    # === Area 1: LLM Training Stability & Observability ===
    '2606.02365': (5, 'FOAM adapts damping and eigendecomposition frequency to control staleness-oriented error in Shampoo preconditioner, linking training stability to numerical robustness'),
    '2606.02218': (5, 'Straggler-aware dynamic group sizing for synchronous GRPO/DAPO on-policy RL directly addresses distributed training robustness and wall-clock efficiency'),
    '2606.02398': (5, 'Local perturbation theory explains multi-domain RL interference through sparse route conflicts and second-order damage, with selective recovery via domain refresh'),
    '2606.02221': (4, 'CORE-MTL rethinks gradient balancing via causal orthogonal representations to disentangle task-relevant structure and reduce negative transfer'),
    '2606.02322': (4, 'Repurposes adversarial perturbations as a geometric control signal for stable continual learning with lower forgetting and stronger transfer'),
    '2606.01717': (4, 'Conflict-aware splitting and weight merging for decentralized instruction tuning addresses gradient interference across distributed domains'),
    '2606.01827': (4, 'Theory-grounded adaptive sharpness-aware minimization with Polyak-type step size improves optimization stability and generalization'),
    '2606.01787': (4, 'Stochastic convergence analysis of parallel asynchronous adaptive first-order methods under delayed updates and gradient noise'),
    '2606.01521': (4, 'Fast generalization via critically damped momentum optimization with explicit convergence analysis beyond interpolation'),
    '2606.02078': (3, 'Curvature-inspired dynamic lp-norm scheme for DNN optimizers that adapts to curvature anisotropy across training phases'),
    '2606.01680': (4, 'Fault-tolerant AllReduce algorithm that prevents a few network failures from stalling the entire distributed training operation'),
    '2606.02282': (3, 'POIROT repurposes a system\'s own agents as a diagnostic layer for failure detection in multi-agent systems, scaling with problem complexity'),
    '2606.01967': (3, 'State-adaptive prompt optimization that mitigates catastrophic forgetting while improving generalization by treating training prompts as dynamic variables'),
    
    # === Area 2: LLM Inference Evaluation ===
    '2606.02289': (5, 'DECK taxonomy classifies LLM hallucinations by detectability signature along consistency and confidence axes, mapping each cell to scorer families'),
    '2606.02020': (5, 'Entropy dynamics of CoT reasoning reveals Uncertainty-to-Confidence region transition, enabling training-free early exit and test-time scaling via CUSUM'),
    '2606.02093': (4, 'Disentangles input ambiguity from uncertainty quantification signals for improved LLM error prediction across model families and datasets'),
    '2606.02211': (4, 'Rate Matching Consistency Training reduces sycophancy without constraining how bias cues are verbalized, preserving monitorability'),
    '2606.02158': (4, 'Multiscale uncertainty estimator focusing on low-probability tokens for AI-generated text detection with strong generalization and robustness'),
    '2606.02493': (4, 'Communicative audit of LLM response framing across cultural positioning, generalizing language, anthropomorphism, and conversational maxims'),
    '2606.02528': (3, 'Audits asset-specific preferences in financial LLMs by identifying a dominant Bitcoin-selective SAE feature with causal leverage over outputs'),
    '2606.02060': (3, 'Span-level error localization in deep-research agent trajectories with claim-centric auditing framework DRIFT for process-level reliability assessment'),
    
    # === Area 3: LLM Hidden States & Interpretability ===
    '2606.02385': (5, 'Theory for understanding SAE representations via local optimality analysis; derives constraints explaining hierarchical splitting, residuals, and dense antipodal features'),
    '2606.02378': (5, 'Developmental trajectories of attention circuits and attention-sink emergence across 1B-class architectures, separating induction and sink transitions by order of magnitude in tokens'),
    '2606.02061': (5, 'Shows archetypal SAE stability is an artifact of deterministic k-means initialization; clarifies stability vs stabilization distinction critical for mechanistic interpretability'),
    '2606.01695': (4, 'CANARY uses SAEs for zero-label detection of fine-tuning contamination in language models via activation-distribution anomaly detection'),
    '2606.02288': (5, 'Mechanistic uncovering of massive activation spikes as structural vector biases driving attention sink and value-state drain; proposes spike-free quantization INSERTQUANT'),
    '2606.02576': (3, 'ProtoAda uses format-aware task prototypes and geometry-aware consolidation for multimodal continual instruction tuning with reduced gradient interference'),
    
    # === Area 4: Computation Reliability & Precision Errors ===
    '2606.02430': (5, 'Systematic fault-injection study of soft error propagation in LLM inference across 3 models and 13 tasks, yielding 17 takeaways and 4 software-only mitigation directions'),
    '2606.02011': (5, 'Extreme 2-bit inference in reasoning models produces process-level failures (repetitive loops, unclosed segments); proposes FP16 planning and loop rescue for targeted recovery'),
    '2606.01850': (4, 'Unified benchmark for quantized and sparse LLMs using conformal prediction to assess whether compression preserves predictive uncertainty and calibration'),
    '2606.02427': (4, 'Spectral audit of in-context operator networks via Jacobian-based tangent operator analysis, detecting high-frequency degradation and prompt-operator inconsistencies hidden by prediction error'),
    '2606.02081': (3, 'Decision-calibrated prediction sets using conformal risk control where calibration targets downstream decision reliability rather than coverage alone'),
    
    # === Area 5: Model System Cards & Technical Reports ===
    '2606.02530': (4, 'SafeSteer performs localized on-policy distillation confined to safety tokens via activation steering, achieving strong safety with only 100 harmful samples'),
    '2606.02111': (4, 'Jailbreaking MLLMs using multi-clip video; finds attack success increases with clip diversity and video is more vulnerable than image modality'),
    '2606.02423': (4, 'HarmAmp benchmark for multi-turn harm amplification across 12 risk categories, with TrajSafe proactive monitor that anticipates harmful trajectories'),
    '2606.02041': (4, 'SentGuard sentence-level streaming guardrail detecting 90.5% of unsafe cases within two sentences with 7.41% false-positive rate'),
    '2606.02562': (3, 'Verifiable belief-space neural safety filters using conformal prediction for high-probability safety certification in interactive robotics'),
    '2606.02461': (3, 'AGENTCL framework for rigorous evaluation of continual learning in language agents with controlled task streams and memory design probes'),
    
    # === Area 6: Silent Data Corruption ===
    '2606.02430': (5, 'Fault injection framework LLMFI for studying soft error propagation in LLM inference on HPC systems with deterministic error injection'),
    '2606.01680': (4, 'Fault-tolerant AllReduce that handles network failures without stalling the entire distributed training collective operation'),
    
    # === Area 7: ML Reliability & Mathematical Foundations ===
    '2606.02134': (5, 'Rethinking IBP-based certified training evaluation via Pareto front comparisons and automated multi-objective hyperparameter optimization'),
    '2606.01557': (4, 'Everywhere Learning with pointwise constraints provides formal guarantees for constrained learning and generalization bounds'),
    '2606.01596': (3, 'Learning chaotic dynamics through second-order geometric supervision with mathematical analysis of stability and convergence'),
    '2606.02363': (4, 'Minimax-optimal policy regret in POMGs with explicit dependence on horizon, adversary memory, and aggregate Eluder dimension, plus matching lower bound'),
    '2606.02232': (4, 'Doeblin-anchored contrastive chart for learning valid Markov transition kernels with nonparametric rates, oracle inequalities, and beta-mixing extensions'),
    '2606.02267': (4, 'Supralinear adversarial robustness via theoretically grounded combination of Gaussian noise and bilateral filtering, ranking second on AutoAttack with ~35% training FLOPs'),
    '2606.02008': (4, 'Provable data scaling law for meta learning via complexity minimization with end-to-end theoretical analysis showing improved few-shot error rates'),
    '2606.02047': (3, 'Convex Distance Operator Transport with pseudometric validity, non-asymptotic risk bounds, and Frank-Wolfe convergence for attributed metric-measure spaces'),
    '2606.02515': (3, 'Biconvex formulation for stable transport of mixture models with unique global minimizer and bounded stability guarantees under perturbation'),
    '2606.02119': (3, 'Hardness-aware multi-objective unlearning with constrained optimization guarantees applicable to non-convex models'),
    '2606.02172': (3, 'Federated prototype learning with scheduled alignment curriculum and geometry-driven proxy separation for stability under severe non-IID'),
    '2606.02231': (3, 'Identifiable Markov switching models with instantaneous effects and exponential families, subsuming non-temporal causal mixtures'),
    '2606.01973': (3, 'Systematic benchmark of open-set test-time adaptation methods revealing struggle to balance InD accuracy and OOD rejection under distribution shift'),
    
    # === CRAM - manual fix ===
    '2606.02502': (3, 'CRAM uses adaptive MoE with centroid routing and orthogonality penalty for multimodal continual instruction tuning with reduced catastrophic forgetting'),
    
    # === Explicitly excluded ===
    '2606.02404': (1, 'Korean web browsing agent benchmark'),
    '2606.02523': (1, 'Suicide meme dataset'),
    '2606.02510': (1, '4D LiDAR scene synthesis'),
    '2606.02418': (1, 'Quantum LDPC code discovery'),
    '2606.02507': (1, 'Materials discovery review'),
    '2606.02342': (1, 'Pen-in-air detection'),
    '2606.01757': (1, '3D object detection'),
    '2606.02042': (1, 'Industrial anomaly detection'),
    '2606.02223': (1, 'Network learning with Gromov-Wasserstein'),
    '2606.02487': (1, 'Hospital stay summarization'),
    '2606.02333': (1, 'GEMM accelerator hardware'),
    '2606.02204': (1, 'Cross-environment neural reranking for text agents'),
    '2606.02105': (1, 'Autonomous driving action diffusion'),
    '2606.02100': (1, 'Portuguese language model'),
    '2606.01985': (1, 'Multi-turn image editing with flow matching'),
}

results = []
for paper in papers:
    arxiv_id = clean_arxiv_id(paper['arxiv_id'])
    title = paper['title']
    abstract = paper.get('abstract', '')
    
    if arxiv_id in manual_scores:
        score, reason = manual_scores[arxiv_id]
    else:
        text = (title + ' ' + abstract).lower()
        score = 1
        reason = 'Low relevance'
        
        strong_signals = [
            'sparse autoencoder', 'sae ', 'attention circuit', 'attention sink',
            'catastrophic forgetting', 'multi-domain rl', 'straggler',
            'error propagation', 'fault injection', 'silent data corruption',
            'certified training', 'interval bound', 'formal guarantee',
            'adversarial robustness', 'quantization', 'low-bit', '2-bit inference',
            'hallucination taxonomy', 'entropy dynamics', 'consistency training',
            'conformal prediction', 'minimax-optimal', 'eluder dimension',
            'training stability', 'gradient interference', 'distributed training',
            'network failure', 'allreduce', 'checkpoint reliability', 'loss spike',
        ]
        
        if any(s in text for s in strong_signals):
            score = 3
            matched = [s for s in strong_signals if s in text][:2]
            reason = f"Moderate relevance: addresses {', '.join(matched)}"
    
    results.append({
        'arxiv_id': arxiv_id,
        'title': title,
        'score': score,
        'reason': reason
    })

results.sort(key=lambda x: -x['score'])
selected = [r for r in results if r['score'] >= 3][:50]

output = {
    'total_evaluated': len(papers),
    'total_selected': len(selected),
    'papers': []
}

for r in selected:
    output['papers'].append({
        'arxiv_id': r['arxiv_id'],
        'title': r['title'],
        'relevance_score': r['score'],
        'relevance_reason': r['reason']
    })

out_path = '/Users/ywang2397/Documents/daily_paper/arxiv-daily/2026-06-01/filtered_papers.json'
tmp_path = out_path + '.tmp'
with open(tmp_path, 'w') as f:
    json.dump(output, f, indent=2)
os.replace(tmp_path, out_path)

print(f"Evaluated: {output['total_evaluated']}")
print(f"Selected: {output['total_selected']}")
print("\nSelected papers:")
for p in output['papers']:
    print(f"  [{p['relevance_score']}] {p['arxiv_id']} - {p['title'][:75]}")
    print(f"      {p['relevance_reason']}")
