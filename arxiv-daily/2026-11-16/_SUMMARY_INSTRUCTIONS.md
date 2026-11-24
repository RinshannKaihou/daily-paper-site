# Step 5 — bilingual paper summary (instructions)

Your task message gives you two values: `DATE` (e.g. 2026-11-16) and `ID` (an arxiv id). Substitute them into the paths below.

Write a detailed bilingual summary for arxiv paper `ID`.

PDF path: /Volumes/T7/work/daily_paper/arxiv-daily/DATE/ID.pdf
Output path: /Volumes/T7/work/daily_paper/arxiv-daily/DATE/ID.md

CRITICAL WORKFLOW (PDF-first — an abstract-only file is a FAILURE STATE to repair, not a deliverable):
1. READ THE PDF FIRST. It is the primary source. Skim strategically: abstract, intro, method, experiments and results tables, limitations. Then write the complete summary in ONE Write call.
2. ONLY if the PDF file is missing or unreadable: write an abstract-based fallback from this paper's entry in /Volumes/T7/work/daily_paper/arxiv-daily/DATE/search_results.json. The fallback MUST (a) begin with the line "⚠️ Abstract-only summary" immediately after the frontmatter, (b) contain ONLY real sentences derived from the abstract — NEVER placeholder text such as "[待生成]", "基于摘要待生成", "To be assessed from full paper", or "待进一步分析", and (c) your final response must end with the line "ABSTRACT_ONLY:ID" so the orchestrator records it as degraded.
3. Do NOT write a stub file "just so a file exists". If you crash before writing, the orchestrator's validation detects the missing file and re-dispatches — that is the designed recovery path.

Requirements:
- Output MUST be bilingual with these exact sections:
  - > **一句话总结：** (Chinese, specific about method/result)
  - > **TL;DR:** (English)
  - ## 核心贡献 (Chinese bullet points)
  - ## Key Contributions (English bullet points)
  - ## Methodology (English)
  - ## Results & Highlights (English)
  - ## Authors & Credibility (English)
  - ## Critical Assessment (English: novelty, rigor, reproducibility, significance, red flags)
  - ## Strengths (English)
  - ## Limitations (English)
  - ## Relevance (Chinese, 1-2 sentences matching user interests)
  - ## Questions for Further Exploration (English)
- CONTENT CONTRACT (deterministically checked by pipeline.py validate; failing files are requeued):
  * Results & Highlights MUST contain >=3 concrete quantitative claims copied from the paper — each naming the metric, the dataset/benchmark, the paper's number, and the strongest baseline's number or the delta. If the paper truly reports no quantitative results, write the literal line "No quantitative results reported" and describe what evidence it offers instead.
  * The TL;DR must name at least one dataset/benchmark, one baseline, and one quantitative delta whenever the paper has them.
  * Critical Assessment must cite at least one paper-specific detail (a named weak baseline, a missing ablation, a data quirk) — never sentences that could apply to any paper.
  * If context runs tight, prioritize depth in this order: Results & Highlights > Methodology > Critical Assessment > everything else.
  * Example of the expected specificity for ONE Results bullet:
    "On MMLU-Pro the 7B model reaches 62.4% vs 58.1% for Qwen2.5-7B-Instruct (+4.3 pts), but the gain shrinks to +0.9 on GPQA — the headline claim generalizes weakly."
- Include YAML frontmatter: title, authors, arxiv_id, aliases, date, tags, url.
- Be intellectually honest in Critical Assessment. Do not rubberstamp papers. Give genuine praise to good work, but call out weak baselines, cherry-picked benchmarks, missing ablations, and overclaiming.
- The TL;DR should be specific enough that someone reading only the overview can decide if the full paper is worth their time.
- Extract 3-5 meaningful tags from the paper's content.

Write ONLY the one output .md file; no other files. Final response (<=30 words): the path written and one line of the paper's headline result (or "ABSTRACT_ONLY:ID" if the fallback path was taken).
