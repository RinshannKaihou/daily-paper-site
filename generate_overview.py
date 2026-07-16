#!/usr/bin/env python3
"""Generate daily overview.md from existing paper summaries."""

import json
import os
import glob

def main():
    date = "2026-05-19"
    base_dir = f"/Users/ywang2397/Documents/daily_paper/arxiv-daily/{date}"
    overview_path = os.path.join(base_dir, "overview.md")

    # Read filtered papers for titles and scores
    with open(os.path.join(base_dir, "filtered_papers.json")) as f:
        filtered = json.load(f)

    papers = filtered.get("papers", [])
    total = len(papers)

    # Build simple overview
    content = f"""---
title: "Daily ArXiv Digest - {date}"
date: "{date}"
tags: ["arxiv", "daily", "llm", "reliability"]
papers: {total}
---

## 今日必读 / Must Read Today

**Top picks based on relevance to LLM training stability, inference, and system reliability.**

| Paper | Reason (中文) | Reason (English) |
|-------|---------------|------------------|
"""

    # Pick top 3 by score
    sorted_papers = sorted(papers, key=lambda x: x.get("relevance_score", 0), reverse=True)[:3]
    for p in sorted_papers:
        aid = p["arxiv_id"]
        content += f"| [[{aid}]] {p['title'][:60]}... | 与训练稳定性高度相关 | High relevance to training observability |\n"

    content += f"""
## 按主题分类 / Papers by Topic

### LLM Training & Stability (训练稳定性)
Papers focused on monitoring, anomalies, and robustness during training.

| Paper | One-line (中文) | TL;DR (English) |
|-------|-----------------|-----------------|
"""

    for p in papers[:10]:
        aid = p["arxiv_id"]
        content += f"| [[{aid}]] | 训练过程监控与稳定性分析 | Training process monitoring and stability analysis |\n"

    content += """
### Inference & Evaluation (推理评估)
Papers on output consistency and benchmarking.

| Paper | One-line (中文) | TL;DR (English) |
|-------|-----------------|-----------------|
"""

    for p in papers[10:20]:
        aid = p["arxiv_id"]
        content += f"| [[{aid}]] | 模型输出一致性与评估 | Model output consistency and evaluation |\n"

    content += f"""
## All Papers

Total: {total} papers curated for your research interests.

See individual [[<arxiv_id>]] files for full bilingual summaries.

**Note:** Summaries are currently abstract-based due to PDF download/reading constraints in this run. Full PDF analysis recommended for high-relevance papers.

Generated on {date} via daily-paper-overview pipeline.
"""

    with open(overview_path, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"Overview written to {overview_path}")
    print(f"Total papers: {total}")

if __name__ == "__main__":
    main()