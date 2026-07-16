#!/usr/bin/env python3
"""Generate the weekly newspaper-style index.html for 2026-0608-0614.

Single-file deliverable: reads week_papers.json and emits index.html.
Output: ~/Documents/daily_paper/arxiv-daily/weekly/2026-0608-0614/index.html
"""
import json
import html
from pathlib import Path

WEEK_DIR = Path("/Users/ywang2397/Documents/daily_paper/arxiv-daily/weekly/2026-0608-0614")
WEEK_JSON = WEEK_DIR / "week_papers.json"
OUT = WEEK_DIR / "index.html"


def esc(s):
    if s is None:
        return ""
    return html.escape(str(s))


# Must-read curation. Order is editorial. The 5 recurring ones lead the band.
# Strings use Python single-quote delimiters so we can freely embed ASCII "
# inside (these were originally Chinese curly quotes that got normalized).
MUST_READ = [
    {
        "id": "2606.13603",
        "chip_zh": "机制可解释性 · CoT",
        "chip_en": "Mech. Interp. · CoT",
        "title_zh": "承诺边界之后：约一半 CoT 步骤对最终答案没有贡献",
        "title_en": "Beyond the Commitment Boundary: ~50% of LLM CoT is epiphenomenal",
        "blurb_zh": '跨两天复现的单日必读；在大推理模型的 CoT 中识别出一条 "承诺边界" —— 此后的多数推理步骤对最终答案没有贡献，呈现 "副现象" 特征；轻量探针可在线定位该边界，节省 26–55% 推理 token。',
        "blurb_en": 'Recurred on 06-11 & 06-12 as a daily must-read; lightweight probes enable online early-exit with 26–55% token savings once a sharp commitment boundary is crossed.',
        "recurs": "↻ 06-11 + 06-12",
    },
    {
        "id": "2606.13607",
        "chip_zh": "机制可解释性 · 人类对照",
        "chip_en": "Mech. Interp. · Human",
        "title_zh": "LLM 与人类的错误模式惊人同构 — 注意力头实现的是模式匹配",
        "title_en": "Reasoning as Pattern Matching: LLM activations predict human errors (R²=0.66)",
        "blurb_zh": '跨两天复现；142 名人类与 25 个 LLM 在 11 类日常推理任务上呈现高度一致的错误模式；MI 分析表明驱动 LLM 推理的注意力头实现模式匹配而非抽象因果推理。',
        "blurb_en": 'Recurred on 06-11 & 06-12; striking human-LLM error-pattern overlap across 11 reasoning categories — a sharp reframing of the standard "pattern matching" critique.',
        "recurs": "↻ 06-11 + 06-12",
    },
    {
        "id": "2606.13125",
        "chip_zh": "后训练 · 推理",
        "chip_en": "Post-Training",
        "title_zh": "RL 不发明新推理策略 — 只选择和精炼 SFT 已有的",
        "title_en": "Select and Improve: RL only selects and refines SFT strategies",
        "blurb_zh": '跨两天复现；通过有限域算术受控实验将 RL 后训练严格分解为 "策略选择" 和 "策略改进" 两大机制，证明 RL 不发明新推理策略 — 对后训练流程设计有直接指导意义。',
        "blurb_en": 'Recurred on 06-11 & 06-12; a controlled finite-field decomposition that ends the "RL invents strategies" myth — direct implications for post-training pipelines.',
        "recurs": "↻ 06-11 + 06-12",
    },
    {
        "id": "2606.12876",
        "chip_zh": "量化 · 信息论",
        "chip_en": "Quantization",
        "title_zh": "Drop-by-Drop：单 checkpoint 在 3–5 bit 间灵活切换",
        "title_en": "Multi-Bitwidth PTQ via Additive Codebooks (Drop-by-Drop)",
        "blurb_zh": "跨两天复现；将多比特宽 PTQ 落地于逐次求精信息论框架，单个量化检查点在推理时丢弃码本即可在 3–5 bit 间灵活切换，匹配单独训练模型。",
        "blurb_en": "Recurred on 06-11 & 06-12; successive-refinement information theory turns one checkpoint into a flexible 3–5 bit model — matching individually-tuned models at inference.",
        "recurs": "↻ 06-11 + 06-12",
    },
    {
        "id": "2606.12921",
        "chip_zh": "优化器 · 谱方法",
        "chip_en": "Optimizer",
        "title_zh": "LoRA-Muon：把谱最陡下降搬到低秩流形上",
        "title_en": "LoRA-Muon: Spectral Steepest Descent on the Low-Rank Manifold",
        "blurb_zh": "跨两天复现；将 Muon 的谱最陡下降推广到低秩流形上，引入投影形式更新、分离式权重衰减与规范不变性，rank-32 即在 TinyShakespeare 上超过稠密基线。",
        "blurb_en": "Recurred on 06-11 & 06-12; rank-32 LoRA beats the dense baseline with transferable learning rates across rank/width/depth/factor scales.",
        "recurs": "↻ 06-11 + 06-12",
    },
    {
        "id": "2606.10304",
        "chip_zh": "LLM 安全 · 机制化监控",
        "chip_en": "LLM Safety",
        "title_zh": "MIRAGE：跨 9 种编码家族的共享子空间泄露监控",
        "title_en": "MIRAGE: A Polarity-Flipping Encoding Subspace in LLM Agents",
        "blurb_zh": "06-09 必读；首次在 LLM agent 隐蔽编码敏感数据时于残差流中发现跨 9 种编码家族、5 种架构的共享低维编码子空间，规划 token 处出现极性翻转；MIRAGE 监控器 AUC 0.918。",
        "blurb_en": "06-09 must-read; first mechanistic discovery of a shared encoding subspace + polarity flip — MIRAGE monitor reaches AUC 0.918 on 126 exfiltration scenarios.",
        "recurs": "★ 06-09",
    },
    {
        "id": "2606.10406",
        "chip_zh": "优化器 · 持续学习",
        "chip_en": "Optimizer",
        "title_zh": "FOGO：把遗忘重铸为通用优化现象",
        "title_en": "FOGO: Forgetting-aware Orthogonalization Optimizer",
        "blurb_zh": '06-09 必读；将 "遗忘" 重新定义为通用优化现象（而非仅持续学习问题），通过谱正交化动量 + 随机投影码本 + 近端提升三步机制，在 CIFAR-10、CL、VLM 微调、GPT-2 预训练上全面超越 Adam 与 Muon。',
        "blurb_en": "06-09 must-read; spectrally orthogonalized momentum + codebook + proximal lifting — consistently beats Adam and Muon across four training regimes.",
        "recurs": "★ 06-09",
    },
    {
        "id": "2606.13473",
        "chip_zh": "数学证明 · RL + TTS",
        "chip_en": "Math Proofs",
        "title_zh": "MaxProof：IMO 2025 从 27 提升至 35/42，跨过金牌线",
        "title_en": "MaxProof: IMO 2025 27→35/42, surpassing the human gold-medal line",
        "blurb_zh": "06-12 必读；将证明生成、验证与修复统一到单一模型，通过四层验证器实现低假阳性 RL 训练，测试时进化式群体搜索将 IMO 2025 从 27/42 提升至 35/42，超越人类金牌线。",
        "blurb_en": "06-12 must-read; four-layer defense-in-depth verifier + population search — the landmark for test-time scaling in rigorous mathematical reasoning.",
        "recurs": "★ 06-12",
    },
]


THEMES = [
    {
        "key": "mech-interp",
        "icon": "🧠",
        "zh": '机制可解释性与 "模式匹配" 再审视',
        "en": "Mechanistic Interpretability & the Pattern-Matching Reframe",
        "lead_zh": "内部表征既被用来推断行为与对齐，又反复被发现与外在推理存在系统性鸿沟 — 本周最重磅的脉络。",
        "lead_en": "Internal states drive inferences about behaviour and alignment, yet repeatedly diverge from external reasoning — the week's heaviest arc.",
        "match_topics": [
            "Mechanistic Interpretability & Circuits",
            "机制可解释性与分析",
            "机制可解释性与表征工程",
            "Mechanistic Interpretability",
        ],
        "boost_ids": [
            "2606.13603", "2606.13607", "2606.10304",
            "2606.12917", "2606.13649", "2606.13209",
            "2606.12818", "2606.12966", "2606.13276",
            "2606.10324", "2606.10703", "2606.10929",
            "2606.11123", "2606.11172", "2606.11722",
            "2606.12138", "2606.12289", "2606.11893",
            "2606.13168", "2606.12058", "2606.13634",
            "2606.12841", "2606.09028", "2606.09287",
            "2606.09411", "2606.09605", "2606.09725",
            "2606.10669",
        ],
    },
    {
        "key": "reasoning",
        "icon": "🧮",
        "zh": "推理与后训练：数学证明与 RL 信用分配",
        "en": "Reasoning & Post-Training: Math Proofs and RL Credit Assignment",
        "lead_zh": "MaxProof 推上 IMO 金牌线，KCSAT-ML 带来人类难度校准基准，Select and Improve 严格分解 RL 后训练。",
        "lead_en": "MaxProof clears the IMO gold-medal bar, KCSAT-ML anchors reasoning to human difficulty, and Select and Improve mechanistically decomposes RL post-training.",
        "match_topics": [
            "LLM Reasoning & Post-Training",
            "推理模型与数学推理",
            "Reasoning & Agents",
            "Reasoning & Post-Training",
        ],
        "boost_ids": [
            "2606.13473", "2606.10403", "2606.13125",
            "2606.13106", "2606.13657", "2606.13680",
            "2606.10346", "2606.10646", "2606.10799",
            "2606.10956", "2606.12935", "2606.13634",
            "2606.09450", "2606.08894", "2606.10307",
            "2606.08960", "2606.11998",
        ],
    },
    {
        "key": "efficiency",
        "icon": "⚙️",
        "zh": "量化、剪枝与高效推理",
        "en": "Quantization, Pruning & Efficient Inference",
        "lead_zh": "从信息论驱动的多比特宽到 megakernel、动态深度路由、KV cache 与硬件加速 — 效率两端齐发力。",
        "lead_en": "Information-theoretic multi-bitwidth PTQ meets compiled megakernels, dynamic depth routing, KV-cache compression, and analog hardware — efficiency advances on both ends.",
        "match_topics": [
            "LLM Inference & Efficiency",
            "Quantization & Low-Precision",
            "Quantization & Low-Precision Inference",
            "LLM 推理效率与部署",
            "LLM 效率",
            "推理优化与系统",
            "Model Compression & Quantization",
        ],
        "boost_ids": [
            "2606.12876", "2606.09682", "2606.09514",
            "2606.13241", "2606.10520", "2606.13054",
            "2606.13097", "2606.13126", "2606.13233",
            "2606.13300", "2606.13328", "2606.13361",
            "2606.13392", "2606.13426", "2606.09012",
            "2606.09048", "2606.09508", "2606.10445",
            "2606.10531", "2606.10890", "2606.10944",
            "2606.11052", "2606.11686", "2606.11690",
            "2606.11780", "2606.11806", "2606.11916",
            "2606.12154", "2606.12243", "2606.12280",
            "2606.12370", "2606.12940", "2606.13379",
        ],
    },
    {
        "key": "optimizers",
        "icon": "📈",
        "zh": "优化器、训练动力学与遗忘",
        "en": "Optimizers, Training Dynamics & Forgetting",
        "lead_zh": "Muon 家族继续深化，FOGO 把遗忘重铸为通用优化现象，对接持续学习与 QAT。",
        "lead_en": "The Muon family deepens (low-rank-manifold spectral descent, adversarial variants); FOGO recasts forgetting as a universal optimization phenomenon.",
        "match_topics": [
            "Optimization & Training Dynamics",
            "优化与训练动态",
            "优化与学习理论",
            "Training Stability & Optimization",
            "Architecture & Training Methods",
        ],
        "boost_ids": [
            "2606.12921", "2606.10406", "2606.13287",
            "2606.13370", "2606.13637", "2606.12883",
            "2606.09410", "2606.09658", "2606.09734",
            "2606.09762", "2606.11854", "2606.12050",
            "2606.12054", "2606.12364", "2606.12397",
        ],
    },
    {
        "key": "safety",
        "icon": "🛡️",
        "zh": "LLM 安全、对齐与机制化监控",
        "en": "LLM Safety, Alignment & Mechanistic Monitoring",
        "lead_zh": 'MIRAGE 给出机制化泄露监控，"中性掩码" + 推理时梯度引导奖励优化共同推进对齐深度。',
        "lead_en": 'MIRAGE delivers mechanistic exfiltration monitoring, "neutral mask" exposes shallow RLHF alignment, and inference-time gradient guidance shores up reward hacking.',
        "match_topics": [
            "LLM Alignment & Safety",
            "Robustness & Adversarial",
            "Robustness & Adversarial Defense",
            "AI Safety & Alignment",
            "Multi-Agent & Agent Systems",
        ],
        "boost_ids": [
            "2606.10304", "2606.09735", "2606.09635",
            "2606.12896", "2606.12930", "2606.13092",
            "2606.13104", "2606.13221", "2606.13254",
            "2606.13282", "2606.13439", "2606.13610",
            "2606.10296", "2606.10487", "2606.10657",
            "2606.10740", "2606.10794", "2606.10852",
            "2606.10931", "2606.10949", "2606.11046",
            "2606.11098", "2606.11166", "2606.11712",
            "2606.11961", "2606.11998", "2606.12016",
            "2606.12071", "2606.12117", "2606.12160",
            "2606.12232", "2606.12234", "2606.12251",
            "2606.12268", "2606.12360", "2606.12385",
            "2606.13174", "2606.13591", "2606.13598",
            "2606.13608", "2606.13621", "2606.13681",
            "2606.08948", "2606.09005", "2606.09189",
            "2606.09388", "2606.09453", "2606.09653",
            "2606.09495", "2606.09697", "2606.09758",
            "2606.09447", "2606.08894", "2606.08960",
        ],
    },
    {
        "key": "theory",
        "icon": "🧪",
        "zh": "理论、评估与不确定性",
        "en": "Theory, Evaluation & Uncertainty",
        "lead_zh": "LLM 评委有效投票坍塌、共形校准、注意力平均场分析；KCSAT-ML 的 DRG 指标首次让评估难度对齐独立于准确率。",
        "lead_en": "LLM-judge effective-vote collapse, conformal calibration, mean-field attention analyses, and a difficulty-aligned DRG metric that is nearly orthogonal to accuracy.",
        "match_topics": [
            "ML Theory & Foundations",
            "Uncertainty, Conformal Prediction & Calibration",
            "机器学习理论与基础",
            "理论与基础工作",
            "Theory: Network Dynamics, Attention & Approximation",
            "理论",
            "Bayesian Methods & Uncertainty",
            "Benchmarks & Evaluation",
            "基准与评测",
            "Generative Models",
            "生成模型",
            "Hardware & Analog Computing",
            "知识编辑与表达",
            "Knowledge Editing & Representation",
        ],
        "boost_ids": [
            "2606.10315", "2606.10469", "2606.10384",
            "2606.11044", "2606.11136", "2606.11104",
            "2606.11045", "2606.11130", "2606.11149",
            "2606.10777", "2606.10906", "2606.10706",
            "2606.10934", "2606.13020", "2606.13111",
            "2606.12864", "2606.13216", "2606.13172",
            "2606.13223", "2606.13576", "2606.13614",
            "2606.09312", "2606.09376", "2606.09389",
            "2606.09541", "2606.09664", "2606.09809",
            "2606.09816", "2606.09433", "2606.11949",
            "2606.11988", "2606.11937", "2606.12003",
            "2606.11081", "2606.11169", "2606.12879",
            "2606.12925", "2606.13105", "2606.13146",
            "2606.13560", "2606.13589", "2606.13671",
            "2606.12997", "2606.13191", "2606.13179",
            "2606.08945", "2606.08973", "2606.09278",
            "2606.09327", "2606.09558", "2606.12841",
            "2606.10669", "2606.10324",
        ],
    },
]


def link_kind_tag(kind):
    if kind == "arxiv":
        return '<span class="link-kind arxiv">arxiv</span>'
    if kind == "markdown":
        return '<span class="link-kind md">note</span>'
    return ""


def trim_blurb(s, n=220):
    if not s:
        return ""
    s = s.strip()
    if len(s) <= n:
        return s
    cut = s.rfind("。", 0, n)
    if cut == -1:
        cut = s.rfind(". ", 0, n)
    if cut == -1 or cut < n // 2:
        cut = n
    return s[:cut] + "…"


def findings_for(pid, paper):
    if paper is None:
        return "", ""
    title = paper.get("title", "").rstrip(".")
    one = paper.get("one_liner", "")
    finding_en = title if not one else f"{title} — {one}"
    finding_zh = finding_en
    if one and any('\u4e00' <= c <= '\u9fff' for c in one):
        finding_zh = one
    return finding_zh, finding_en


def main():
    data = json.loads(WEEK_JSON.read_text(encoding="utf-8"))
    papers = data["papers"]
    by_id = {p["id"]: p for p in papers}
    days_used = data["days_used"]
    total = data["total_unique"]
    n_days = len(days_used)
    day_range = f"{days_used[0]} → {days_used[-1]}"

    lead = MUST_READ[0]
    lead_paper = by_id[lead["id"]]
    supporting = MUST_READ[1:5]
    lower = MUST_READ[5:]

    def render_headline(card, paper, is_lead):
        link = esc(paper["link"])
        kind_tag = link_kind_tag(paper["link_kind"])
        title_zh = esc(card["title_zh"])
        title_en = esc(card["title_en"])
        blurb_zh = esc(trim_blurb(card["blurb_zh"], 180))
        blurb_en = esc(trim_blurb(card["blurb_en"], 200))
        chip = esc(card["chip_en"])
        recurs = esc(card["recurs"])
        title_html = (
            f'<a href="{link}">'
            f'<span class="cn">{title_zh}</span>'
            f'<span class="en">{title_en}</span>'
            f'</a>'
        )
        return f'''
        <article class="headline-card{' lead' if is_lead else ''}">
          <div class="card-top">
            <span class="topic-chip">{chip}</span>
            <span class="recurs-pill">{recurs}</span>
          </div>
          <h3 class="headline-title">{title_html}</h3>
          <div class="bilingual-line">
            <span class="cn">{blurb_zh}</span>
            <span class="en">{blurb_en}</span>
          </div>
          <div class="card-bottom">
            <a href="{link}" class="read-more">→ Read &rsaquo;</a>
            {kind_tag}
          </div>
        </article>'''

    lead_html = render_headline(lead, lead_paper, True)
    supporting_html = "\n".join(
        render_headline(c, by_id[c["id"]], False) for c in supporting
    )
    lower_html = "\n".join(
        render_headline(c, by_id[c["id"]], False) for c in lower
    )

    theme_html_parts = []
    for theme in THEMES:
        match_topics = set(theme["match_topics"])
        boost_ids = set(theme["boost_ids"])

        def belongs(p):
            if p["id"] in boost_ids:
                return True
            return p.get("topic", "") in match_topics

        candidates = [p for p in papers if belongs(p)]

        def sort_key(p):
            is_must = 0 if (p.get("daily_must_read") or len(p.get("days_seen", [])) >= 2) else 1
            return (is_must, p["id"])

        candidates.sort(key=sort_key)

        if len(candidates) > 18:
            must = [p for p in candidates if p.get("daily_must_read") or len(p.get("days_seen", [])) >= 2]
            rest = [p for p in candidates if p not in must]
            candidates = must + rest[: max(0, 18 - len(must))]

        cards = []
        for p in candidates:
            link = esc(p["link"])
            kind_tag = link_kind_tag(p["link_kind"])
            f_zh, f_en = findings_for(p["id"], p)
            title = esc(p["title"])
            is_must = p.get("daily_must_read") or len(p.get("days_seen", [])) >= 2
            must_pill = ""
            if p.get("daily_must_read"):
                must_pill = '<span class="paper-flag must">★ must-read</span>'
            elif len(p.get("days_seen", [])) >= 2:
                must_pill = f'<span class="paper-flag recur">↻ ×{len(p["days_seen"])}</span>'
            prominent = ' prominent' if is_must else ''
            cards.append(f'''
        <article class="paper-card{prominent}">
          <div class="card-top">
            <span class="card-id">{esc(p["id"])}</span>
            {must_pill}
          </div>
          <h4 class="card-title"><a href="{link}">{title}</a></h4>
          <p class="card-finding">
            <span class="cn">{esc(trim_blurb(f_zh, 140))}</span>
            <span class="en">{esc(trim_blurb(f_en, 160))}</span>
          </p>
          <div class="card-bottom">
            <a href="{link}" class="card-link">→ open &rsaquo;</a>
            {kind_tag}
          </div>
        </article>''')
        grid = "\n".join(cards)
        theme_html_parts.append(f'''
      <section class="section" id="theme-{esc(theme['key'])}">
        <div class="section-nameplate">
          <span class="section-icon">{theme['icon']}</span>
          <div class="section-titles">
            <h2 class="zh">{esc(theme['zh'])}</h2>
            <h2 class="en">{esc(theme['en'])}</h2>
          </div>
          <span class="section-count">{len(candidates)} papers</span>
        </div>
        <p class="section-lede">
          <span class="cn">{esc(theme['lead_zh'])}</span>
          <span class="en">{esc(theme['lead_en'])}</span>
        </p>
        <div class="paper-grid">{grid}
        </div>
      </section>''')

    themes_html = "\n".join(theme_html_parts)

    daily_links = "\n".join(
        f'        <li><a href="../../{d}/index.html">{d}</a></li>' for d in days_used
    )
    theme_links = "\n".join(
        f'        <li><a href="#theme-{t["key"]}">{esc(t["zh"])}</a></li>' for t in THEMES
    )

    theme_nav_html = "\n".join(
        f'      <a href="#theme-{t["key"]}"><span class="ic">{t["icon"]}</span><span class="lbl">{esc(t["en"])}</span></a>'
        for t in THEMES
    )

    html_doc = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Weekly arXiv Digest — 2026-06-08–2026-06-14</title>
<style>
  @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,700;0,900;1,400;1,700&family=Source+Serif+4:ital,wght@0,300;0,400;0,600;0,700;1,400&family=IBM+Plex+Sans:wght@400;500;600;700&display=swap');

  :root {{
    --bg: #FAF8F4;
    --paper: #F5F2EB;
    --ink: #1A1A1A;
    --ink-light: #4A4A4A;
    --ink-faint: #7A7A7A;
    --rule: #C8C3B8;
    --rule-strong: #8A8478;
    --accent: #8B1A1A;
    --accent-light: #A63030;
    --chip-bg: #EDE9E0;
    --lead-bg: #FFFDF8;
  }}

  *, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}

  html {{ font-size: 16px; scroll-behavior: smooth; }}

  body {{
    font-family: 'Source Serif 4', Georgia, 'Times New Roman', serif;
    background: var(--bg);
    color: var(--ink);
    line-height: 1.55;
    -webkit-font-smoothing: antialiased;
  }}

  a {{ color: var(--accent); text-decoration: none; }}
  a:hover {{ color: var(--accent-light); text-decoration: underline; }}

  /* ARCHIVE LINK */
  #archive-link {{
    position: fixed;
    top: 12px;
    left: 16px;
    font-family: 'IBM Plex Sans', sans-serif;
    font-size: 0.72rem;
    font-weight: 500;
    color: var(--accent);
    letter-spacing: 0.04em;
    text-transform: uppercase;
    z-index: 100;
    opacity: 0.7;
    transition: opacity 0.2s;
    background: rgba(250,248,244,0.85);
    padding: 4px 8px;
    border-radius: 3px;
  }}
  #archive-link:hover {{ opacity: 1; text-decoration: none; }}

  /* MASTHEAD */
  .masthead {{
    max-width: 1240px;
    margin: 0 auto;
    padding: 56px 24px 32px;
    text-align: center;
    border-bottom: 3px double var(--rule-strong);
  }}
  .masthead .kicker {{
    font-family: 'IBM Plex Sans', sans-serif;
    font-size: 0.7rem;
    font-weight: 600;
    letter-spacing: 0.32em;
    text-transform: uppercase;
    color: var(--accent);
    margin-bottom: 8px;
  }}
  .masthead-rule {{
    border: none;
    border-top: 1px solid var(--rule);
    margin: 8px auto;
    max-width: 460px;
  }}
  .masthead h1 {{
    font-family: 'Playfair Display', Georgia, serif;
    font-weight: 900;
    font-size: clamp(2.6rem, 6vw, 4.6rem);
    letter-spacing: 0.04em;
    text-transform: uppercase;
    color: var(--ink);
    line-height: 1.02;
    margin: 6px 0 4px;
  }}
  .masthead h1 .sub-en {{
    display: block;
    font-family: 'Source Serif 4', serif;
    font-style: italic;
    font-weight: 400;
    font-size: 0.32em;
    letter-spacing: 0.16em;
    text-transform: none;
    color: var(--ink-light);
    margin-top: 6px;
  }}
  .masthead .date-line {{
    font-family: 'IBM Plex Sans', sans-serif;
    font-size: 0.88rem;
    font-weight: 500;
    letter-spacing: 0.22em;
    text-transform: uppercase;
    color: var(--ink-light);
    margin: 14px 0 6px;
  }}
  .masthead .stats-line {{
    font-family: 'IBM Plex Sans', sans-serif;
    font-size: 0.78rem;
    font-weight: 500;
    letter-spacing: 0.04em;
    color: var(--ink);
    margin-top: 4px;
  }}
  .masthead .stats-line .num {{
    color: var(--accent);
    font-weight: 700;
    font-variant-numeric: tabular-nums;
  }}
  .masthead .subtitle {{
    font-family: 'Source Serif 4', serif;
    font-style: italic;
    font-size: 0.98rem;
    color: var(--ink-faint);
    max-width: 720px;
    margin: 14px auto 0;
  }}

  /* THEME NAV BAND */
  .theme-nav {{
    max-width: 1240px;
    margin: 0 auto;
    padding: 14px 24px;
    border-bottom: 1px solid var(--rule);
    display: flex;
    flex-wrap: wrap;
    gap: 6px 4px;
    justify-content: center;
  }}
  .theme-nav a {{
    font-family: 'IBM Plex Sans', sans-serif;
    font-size: 0.7rem;
    font-weight: 600;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    color: var(--ink-light);
    padding: 5px 10px;
    border: 1px solid var(--rule);
    border-radius: 2px;
    background: var(--paper);
    transition: all 0.15s;
  }}
  .theme-nav a:hover {{
    color: var(--accent);
    border-color: var(--accent);
    text-decoration: none;
    background: var(--lead-bg);
  }}
  .theme-nav .ic {{ margin-right: 4px; }}

  /* HEADLINES BAND */
  .headlines-band {{
    max-width: 1240px;
    margin: 0 auto;
    padding: 36px 24px 32px;
    border-bottom: 2px solid var(--rule-strong);
  }}
  .headlines-label {{
    font-family: 'IBM Plex Sans', sans-serif;
    font-size: 0.7rem;
    font-weight: 700;
    letter-spacing: 0.28em;
    text-transform: uppercase;
    color: var(--accent);
    margin-bottom: 22px;
    display: flex;
    align-items: baseline;
    gap: 10px;
    flex-wrap: wrap;
  }}
  .headlines-label .zh {{ font-weight: 600; opacity: 0.85; }}
  .headlines-grid {{
    display: grid;
    grid-template-columns: 1.45fr 0.95fr 0.95fr;
    gap: 0;
  }}
  .headlines-col {{
    display: flex;
    flex-direction: column;
  }}
  .headlines-col.lead {{
    padding: 0 28px 0 0;
    border-right: 1px solid var(--rule);
  }}
  .headlines-col.mid {{
    padding: 0 24px;
    border-right: 1px solid var(--rule);
  }}
  .headlines-col.last {{
    padding: 0 0 0 24px;
  }}
  .headlines-col .headline-card {{
    flex: 1;
  }}
  .headlines-col.mid .headline-card + .headline-card,
  .headlines-col.last .headline-card + .headline-card {{
    border-top: 1px solid var(--rule);
    margin-top: 18px;
    padding-top: 18px;
  }}
  .headline-card .card-top {{
    display: flex;
    align-items: center;
    gap: 8px;
    margin-bottom: 10px;
    flex-wrap: wrap;
  }}
  .topic-chip {{
    display: inline-block;
    font-family: 'IBM Plex Sans', sans-serif;
    font-size: 0.6rem;
    font-weight: 700;
    letter-spacing: 0.15em;
    text-transform: uppercase;
    color: var(--accent);
    background: var(--chip-bg);
    padding: 3px 10px;
    border-radius: 2px;
  }}
  .recurs-pill {{
    display: inline-block;
    font-family: 'IBM Plex Sans', sans-serif;
    font-size: 0.6rem;
    font-weight: 600;
    letter-spacing: 0.08em;
    color: var(--ink-light);
    background: var(--paper);
    border: 1px solid var(--rule);
    padding: 2px 7px;
    border-radius: 2px;
    font-variant-numeric: tabular-nums;
  }}
  .headline-card .headline-title {{
    font-family: 'Playfair Display', Georgia, serif;
    font-weight: 900;
    line-height: 1.18;
    color: var(--ink);
    margin-bottom: 10px;
  }}
  .headline-card.lead .headline-title {{
    font-size: clamp(1.55rem, 2.6vw, 2.3rem);
  }}
  .headline-card:not(.lead) .headline-title {{
    font-size: clamp(1.05rem, 1.6vw, 1.4rem);
  }}
  .headline-card .headline-title a {{ color: var(--ink); }}
  .headline-card .headline-title a:hover {{ color: var(--accent); text-decoration: none; }}
  .headline-card .headline-title .cn {{
    display: block;
    margin-bottom: 4px;
  }}
  .headline-card .headline-title .en {{
    display: block;
    font-style: italic;
    font-weight: 700;
    color: var(--ink-light);
    font-size: 0.86em;
  }}
  .headline-card .bilingual-line {{
    font-size: 0.9rem;
    color: var(--ink-light);
    line-height: 1.55;
    margin-bottom: 10px;
  }}
  .headline-card .bilingual-line .cn {{
    display: block;
    font-style: normal;
    margin-bottom: 4px;
    color: var(--ink-light);
  }}
  .headline-card .bilingual-line .en {{
    display: block;
    font-style: italic;
    color: var(--ink-faint);
    font-size: 0.92em;
  }}
  .headline-card .card-bottom {{
    display: flex;
    align-items: center;
    gap: 8px;
    margin-top: 6px;
  }}
  .headline-card .read-more {{
    font-family: 'IBM Plex Sans', sans-serif;
    font-size: 0.72rem;
    font-weight: 600;
    letter-spacing: 0.08em;
    color: var(--accent);
    text-transform: uppercase;
  }}
  .headline-card .read-more:hover {{ text-decoration: none; opacity: 0.8; }}

  .link-kind {{
    font-family: 'IBM Plex Sans', sans-serif;
    font-size: 0.55rem;
    font-weight: 600;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    color: var(--ink-faint);
    background: transparent;
    border: 1px solid var(--rule);
    padding: 1px 5px;
    border-radius: 2px;
    line-height: 1;
  }}
  .link-kind.md {{ color: var(--ink-faint); }}
  .link-kind.arxiv {{ color: var(--accent); border-color: var(--accent); opacity: 0.7; }}

  /* SECTIONS */
  .content-body {{
    max-width: 1240px;
    margin: 0 auto;
    padding: 0 24px;
  }}

  .section {{
    padding: 36px 0 30px;
    border-bottom: 1px solid var(--rule);
    scroll-margin-top: 16px;
  }}
  .section:last-of-type {{ border-bottom: none; }}

  .section-nameplate {{
    display: grid;
    grid-template-columns: auto 1fr auto;
    align-items: center;
    gap: 14px;
    margin-bottom: 14px;
    padding-bottom: 10px;
    border-bottom: 2px solid var(--ink);
  }}
  .section-icon {{
    font-size: 1.5rem;
  }}
  .section-titles {{
    display: flex;
    flex-direction: column;
    gap: 1px;
  }}
  .section-titles h2 {{
    font-family: 'Playfair Display', Georgia, serif;
    font-weight: 900;
    line-height: 1.15;
    color: var(--ink);
  }}
  .section-titles h2.zh {{
    font-size: 1.32rem;
    letter-spacing: 0.06em;
  }}
  .section-titles h2.en {{
    font-size: 0.95rem;
    font-style: italic;
    font-weight: 700;
    color: var(--ink-light);
    letter-spacing: 0.02em;
  }}
  .section-count {{
    font-family: 'IBM Plex Sans', sans-serif;
    font-size: 0.7rem;
    font-weight: 600;
    color: var(--ink-faint);
    letter-spacing: 0.06em;
    font-variant-numeric: tabular-nums;
    white-space: nowrap;
  }}
  .section-lede {{
    font-size: 0.92rem;
    color: var(--ink-light);
    line-height: 1.6;
    margin-bottom: 20px;
    max-width: 920px;
  }}
  .section-lede .cn {{
    display: block;
    margin-bottom: 3px;
  }}
  .section-lede .en {{
    display: block;
    font-style: italic;
    color: var(--ink-faint);
    font-size: 0.96em;
  }}

  .paper-grid {{
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
    gap: 14px;
  }}

  .paper-card {{
    padding: 14px 16px 12px;
    background: var(--lead-bg);
    border: 1px solid var(--rule);
    border-radius: 2px;
    transition: border-color 0.15s, transform 0.15s;
  }}
  .paper-card:hover {{
    border-color: var(--rule-strong);
    transform: translateY(-1px);
  }}
  .paper-card.prominent {{
    grid-column: span 2;
    border-left: 3px solid var(--accent);
    background: linear-gradient(to right, var(--lead-bg) 0%, #FFFCF1 100%);
  }}
  .paper-card .card-top {{
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 6px;
    margin-bottom: 6px;
  }}
  .paper-card .card-id {{
    font-family: 'IBM Plex Sans', sans-serif;
    font-size: 0.62rem;
    font-weight: 600;
    color: var(--ink-faint);
    letter-spacing: 0.04em;
    font-variant-numeric: tabular-nums;
  }}
  .paper-flag {{
    font-family: 'IBM Plex Sans', sans-serif;
    font-size: 0.55rem;
    font-weight: 700;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    padding: 1px 6px;
    border-radius: 2px;
    line-height: 1.3;
  }}
  .paper-flag.must {{
    color: #fff;
    background: var(--accent);
  }}
  .paper-flag.recur {{
    color: var(--accent);
    background: var(--chip-bg);
    border: 1px solid var(--accent);
    opacity: 0.75;
  }}
  .paper-card .card-title {{
    font-family: 'Playfair Display', Georgia, serif;
    font-weight: 700;
    font-size: 0.95rem;
    line-height: 1.28;
    margin-bottom: 6px;
  }}
  .paper-card.prominent .card-title {{ font-size: 1.08rem; }}
  .paper-card .card-title a {{ color: var(--ink); }}
  .paper-card .card-title a:hover {{ color: var(--accent); text-decoration: none; }}
  .paper-card .card-finding {{
    font-size: 0.8rem;
    color: var(--ink-light);
    line-height: 1.5;
    margin-bottom: 6px;
  }}
  .paper-card .card-finding .cn {{
    display: block;
    margin-bottom: 2px;
  }}
  .paper-card .card-finding .en {{
    display: block;
    font-style: italic;
    color: var(--ink-faint);
    font-size: 0.95em;
  }}
  .paper-card .card-bottom {{
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 6px;
    margin-top: 6px;
  }}
  .paper-card .card-link {{
    font-family: 'IBM Plex Sans', sans-serif;
    font-size: 0.65rem;
    font-weight: 600;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    color: var(--accent);
  }}
  .paper-card .card-link:hover {{ text-decoration: none; opacity: 0.8; }}

  /* FOOTER */
  .footer {{
    max-width: 1240px;
    margin: 0 auto;
    padding: 36px 24px 44px;
    border-top: 2px solid var(--rule-strong);
  }}
  .footer-grid {{
    display: grid;
    grid-template-columns: 1.2fr 1fr 1.3fr;
    gap: 36px;
    margin-bottom: 24px;
  }}
  .footer-col h3 {{
    font-family: 'IBM Plex Sans', sans-serif;
    font-size: 0.65rem;
    font-weight: 700;
    letter-spacing: 0.22em;
    text-transform: uppercase;
    color: var(--accent);
    margin-bottom: 10px;
  }}
  .footer-col ul {{
    list-style: none;
  }}
  .footer-col li {{
    font-family: 'IBM Plex Sans', sans-serif;
    font-size: 0.78rem;
    line-height: 1.85;
    color: var(--ink-light);
  }}
  .footer-col li a {{
    color: var(--ink);
  }}
  .footer-col li a:hover {{
    color: var(--accent);
  }}
  .footer-meta {{
    border-top: 1px solid var(--rule);
    padding-top: 14px;
    font-family: 'IBM Plex Sans', sans-serif;
    font-size: 0.68rem;
    color: var(--ink-faint);
    font-style: italic;
    display: flex;
    justify-content: space-between;
    flex-wrap: wrap;
    gap: 8px;
  }}
  .footer-meta code {{
    font-family: 'IBM Plex Mono', 'SF Mono', monospace;
    font-style: normal;
    color: var(--ink-light);
    font-size: 0.95em;
  }}
  .not-verified {{
    color: var(--accent);
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    font-style: normal;
  }}

  /* RESPONSIVE */
  @media (max-width: 1080px) {{
    .headlines-grid {{
      grid-template-columns: 1fr 1fr;
    }}
    .headlines-col.lead {{
      grid-column: span 2;
      padding: 0 0 22px 0;
      border-right: none;
      border-bottom: 1px solid var(--rule);
    }}
    .headlines-col.mid {{
      padding: 22px 24px 0 0;
      border-right: 1px solid var(--rule);
    }}
    .headlines-col.last {{
      padding: 22px 0 0 24px;
    }}
    .footer-grid {{ grid-template-columns: 1fr 1fr; gap: 24px; }}
  }}
  @media (max-width: 760px) {{
    .headlines-grid {{
      grid-template-columns: 1fr;
    }}
    .headlines-col.lead,
    .headlines-col.mid,
    .headlines-col.last {{
      grid-column: span 1;
      padding: 0 0 18px 0;
      border-right: none;
      border-bottom: 1px solid var(--rule);
    }}
    .headlines-col.last {{ border-bottom: none; padding-bottom: 0; }}
    .headlines-col.mid .headline-card + .headline-card,
    .headlines-col.last .headline-card + .headline-card {{
      border-top: 1px solid var(--rule);
      margin-top: 18px;
      padding-top: 18px;
    }}
    .paper-grid {{ grid-template-columns: 1fr; }}
    .paper-card.prominent {{ grid-column: span 1; }}
    .footer-grid {{ grid-template-columns: 1fr; }}
  }}
  @media (max-width: 560px) {{
    .masthead {{ padding: 40px 16px 22px; }}
    .masthead h1 {{ font-size: 1.95rem; letter-spacing: 0.02em; }}
    .masthead h1 .sub-en {{ font-size: 0.42em; letter-spacing: 0.1em; }}
    .headlines-band {{ padding: 22px 16px; }}
    .content-body {{ padding: 0 16px; }}
    .section {{ padding: 26px 0 22px; }}
    .section-nameplate {{
      grid-template-columns: auto 1fr;
      grid-template-rows: auto auto;
      gap: 6px 10px;
    }}
    .section-count {{
      grid-column: 2;
      grid-row: 2;
    }}
    .theme-nav {{ padding: 10px 14px; }}
    .footer {{ padding: 26px 16px 32px; }}
    #archive-link {{ font-size: 0.65rem; top: 8px; left: 8px; }}
  }}
</style>
</head>
<body>

<a href="../../../index.html" id="archive-link">← Archive</a>

<!-- MASTHEAD -->
<header class="masthead">
  <div class="kicker">Weekly Rollup · 5 Days · 6 Arcs</div>
  <hr class="masthead-rule">
  <h1>
    Weekly arXiv Digest
    <span class="sub-en">A rollup of {day_range}</span>
  </h1>
  <div class="date-line">{day_range}</div>
  <hr class="masthead-rule">
  <div class="stats-line">
    <span class="num">{total}</span> unique papers &middot; <span class="num">{n_days}</span> days &middot; <span class="num">{len(THEMES)}</span> thematic sections &middot; <span class="num">8</span> must-reads
  </div>
  <div class="subtitle">
    Mechanistic interpretability leads the week: commitment boundaries, human–LLM error-pattern
    isomorphism, and a shared encoding subspace for agent exfiltration. Plus IMO-level proof RL,
    additive-codebook quantization, LoRA-Muon, and a mechanistic safety monitor that beats output
    detection by 0.4 AUC.
  </div>
</header>

<!-- THEME NAV -->
<nav class="theme-nav" aria-label="Jump to section">
{theme_nav_html}
</nav>

<!-- HEADLINES -->
<section class="headlines-band">
  <div class="headlines-label">
    <span>★ Must Read This Week · 本周必读</span>
    <span class="zh">— 8 picks, 5 recurring across days</span>
  </div>
  <div class="headlines-grid">
    <div class="headlines-col lead">{lead_html}
    </div>
    <div class="headlines-col mid">{supporting_html}
    </div>
    <div class="headlines-col last">{lower_html}
    </div>
  </div>
</section>

<!-- CONTENT BODY -->
<div class="content-body">
{themes_html}
</div>

<!-- FOOTER -->
<footer class="footer">
  <div class="footer-grid">
    <div class="footer-col">
      <h3>Daily editions / 单日</h3>
      <ul>
{daily_links}
      </ul>
    </div>
    <div class="footer-col">
      <h3>Themed sections / 主题</h3>
      <ul>
{theme_links}
      </ul>
    </div>
    <div class="footer-col">
      <h3>About this digest / 关于</h3>
      <ul>
        <li>Curated rollup of <strong>{total}</strong> papers across {n_days} days</li>
        <li>Lead = most-recurring must-read (↻ ×2)</li>
        <li>Theme sections = curated, not exhaustive</li>
        <li>Source of truth: <code>week_papers.json</code></li>
      </ul>
    </div>
  </div>
  <div class="footer-meta">
    <span>Weekly vault: <code>~/Documents/daily_paper/arxiv-daily/weekly/2026-0608-0614/</code></span>
    <span class="not-verified">⚠ Not browser-verified</span>
  </div>
</footer>

</body>
</html>
"""

    OUT.write_text(html_doc, encoding="utf-8")
    size = OUT.stat().st_size
    print(f"Wrote {OUT}  ({size:,} bytes)")


if __name__ == "__main__":
    main()
