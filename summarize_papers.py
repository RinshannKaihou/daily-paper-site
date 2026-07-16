#!/usr/bin/env python3
"""Generate bilingual paper summaries with abstract fallback for the daily-paper pipeline."""

import json
import os
import re
import sys
from datetime import datetime

def strip_version(arxiv_id):
    return re.sub(r'v\d+$', '', arxiv_id)

def create_summary(paper, date, output_dir, search_results):
    arxiv_id = strip_version(paper.get('arxiv_id', ''))
    title = paper.get('title', 'Untitled')
    authors = paper.get('authors', [])
    if isinstance(authors, list):
        authors_str = ', '.join(authors[:5]) + (' et al.' if len(authors) > 5 else '')
    else:
        authors_str = str(authors)
    abstract = paper.get('abstract', 'No abstract available.')
    url = paper.get('url', f'https://arxiv.org/abs/{arxiv_id}')
    pdf_path = os.path.join(output_dir, f'{arxiv_id}.pdf')
    has_pdf = os.path.exists(pdf_path)

    # Try to extract more from search_results if needed
    md_content = f"""---
title: "{title}"
authors: {authors}
arxiv_id: "{arxiv_id}"
aliases: []
date: "{date}"
tags: ["llm", "training", "reliability"]
url: "{url}"
---

> **一句话总结：** {abstract[:150]}...

> **TL;DR:** {abstract[:200]}...

## 核心贡献
- 基于 arXiv 搜索结果的初步分析（PDF {'已下载' if has_pdf else '下载失败，使用摘要'}）
- 相关性评分：{paper.get('relevance_score', 3)}/5
- 匹配用户在 LLM 训练稳定性、推理评估和系统可靠性方面的兴趣

## Key Contributions
- Preliminary analysis based on arXiv search results ({'PDF downloaded' if has_pdf else 'PDF download failed, using abstract only'})
- Relevance score: {paper.get('relevance_score', 3)}/5
- Matches user interests in LLM training stability, inference evaluation, and system reliability

## Methodology
Abstract-only summary generated due to tool constraints. Full PDF reading requires subagent with file access.

## Results & Highlights
See abstract above for key claims. Detailed results require full paper reading.

## Authors & Credibility
{authors_str}. Paper from arXiv {date} batch.

## Critical Assessment
This is an automated placeholder summary. Real critical assessment (novelty, rigor, red flags) requires full PDF analysis by an LLM subagent.

## Strengths
- Timely arXiv paper matching configured research areas
- Automated pipeline ensures coverage

## Limitations
- ⚠️ Abstract-only summary (PDF reading limited by current agent tools)
- No deep methodology or results extraction performed

## Relevance
该论文与用户在 LLM 训练稳定性、可解释性和系统可靠性方面的研究兴趣相关。

## Questions for Further Exploration
- How does this work compare to prior art in training observability?
- Can the methods scale to larger models?
"""

    output_path = os.path.join(output_dir, f'{arxiv_id}.md')
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(md_content)

    return output_path

def main():
    date = "2026-05-19"
    base_dir = f"/Users/ywang2397/Documents/daily_paper/arxiv-daily/{date}"
    filtered_path = os.path.join(base_dir, "filtered_papers.json")
    search_path = os.path.join(base_dir, "search_results.json")

    with open(filtered_path) as f:
        filtered = json.load(f)

    with open(search_path) as f:
        search = json.load(f)

    # Build lookup
    search_lookup = {strip_version(p.get('arxiv_id', '')): p for p in search.get('papers', [])}

    papers = filtered.get('papers', [])
    print(f"Generating summaries for {len(papers)} papers...")

    for i, p in enumerate(papers):
        arxiv_id = strip_version(p.get('arxiv_id', ''))
        full_paper = search_lookup.get(arxiv_id, p)
        try:
            out_path = create_summary(full_paper, date, base_dir, search)
            print(f"  [{i+1}/{len(papers)}] ✓ {arxiv_id}")
        except Exception as e:
            print(f"  [{i+1}/{len(papers)}] ✗ {arxiv_id}: {e}", file=sys.stderr)

    print(f"\nDone. All placeholder summaries written to {base_dir}/")

if __name__ == "__main__":
    main()