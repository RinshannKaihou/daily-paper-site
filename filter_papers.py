#!/usr/bin/env python3
"""Simple keyword-based paper filter for daily-paper-overview pipeline."""

import json
import re
import sys

def main():
    date = "2026-05-19"
    base_dir = f"/Users/ywang2397/Documents/daily_paper/arxiv-daily/{date}"

    # Read interests
    with open("/Users/ywang2397/Documents/daily_paper/interests.md") as f:
        interests_content = f.read()

    areas_match = re.search(r"```areas\n(.*?)\n```", interests_content, re.DOTALL)
    areas = areas_match.group(1).strip() if areas_match else ""

    # Read search results
    with open(f"{base_dir}/search_results.json") as f:
        search = json.load(f)

    papers = search.get("papers", [])
    print(f"Total papers to evaluate: {len(papers)}", file=sys.stderr)

    # Keyword filter based on interests areas
    keywords = [
        "llm", "training", "stability", "inference", "interpretability",
        "reliability", "quantization", "hidden state", "observability",
        "silent data", "precision", "model card", "system card", "gradient",
        "checkpoint", "distributed", "reproducibility", "anomaly", "robustness"
    ]

    selected = []
    for p in papers:
        text = (p.get("title", "") + " " + p.get("abstract", "")).lower()
        score = sum(1 for k in keywords if k in text)
        if score >= 2:
            arxiv_id = re.sub(r"v\d+$", "", p.get("arxiv_id", ""))
            selected.append({
                "arxiv_id": arxiv_id,
                "title": p.get("title"),
                "relevance_score": min(5, max(3, score)),
                "relevance_reason": "Matches LLM training/stability/inference/interpretability topics"
            })
        if len(selected) >= 50:
            break

    result = {
        "total_evaluated": len(papers),
        "total_selected": len(selected),
        "papers": selected
    }

    with open(f"{base_dir}/filtered_papers.json", "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2, ensure_ascii=False)

    print(f"Selected {len(selected)} papers out of {len(papers)}. Written to filtered_papers.json")

if __name__ == "__main__":
    main()