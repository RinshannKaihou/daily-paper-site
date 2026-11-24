# Step 5b — per-paper vivid HTML dashboard (instructions)

Your task message gives `DATE` (2026-11-16) and `ID`. Substitute them below.

Design and write a vivid, non-linear DASHBOARD HTML for ONE arxiv paper. This is NOT a markdown-to-HTML transcription. You are extracting high-value assets from the source and surfacing them in a designed layout.

FIRST: if a skill named `html-deliverable-craft` is available via the Skill tool, invoke it and follow its design standards strictly. If it is not available, follow the design standards written out below — do not stop to ask.

Inputs:
- Source markdown: /Volumes/T7/work/daily_paper/arxiv-daily/DATE/ID.md
- The .md has bilingual sections (Chinese 一句话总结/核心贡献 on top, English TL;DR/Key Contributions/Methodology/Results/Critical Assessment/Strengths/Limitations/Relevance/Questions below). Read all of it.

Output: ONE file at /Volumes/T7/work/daily_paper/arxiv-daily/DATE/ID.html
Self-contained: HTML + CSS + JS inline.

STEP 1 — EXTRACT 4 ASSETS from the source markdown:

1. KEY FINDING — one sentence (max ~20 words) that captures the paper's core claim. Pull from TL;DR or 一句话总结 or Core Contributions, whichever is sharpest. This becomes the page's hero.

2. KEY METRIC — a specific number/percentage/factor from Results that anchors the claim (e.g. "+3.2 BLEU over SOTA", "5x faster on A100", "94.7% accuracy on MMLU"). If no clean number exists, extract the most quantitative phrase. Render as oversized typography in the dashboard.

3. WHY THIS MATTERS — a <=25-word distillation from Relevance section (or TL;DR if Relevance is sparse). Plain-language "why a reader should care about this today".

4. CRITICAL EDGE — a single sentence from Critical Assessment / Limitations that captures the sharpest critique. Renders as a contrasting callout so the reader doesn't read this paper uncritically.

If any of these cannot be extracted cleanly from the source, fall back to the closest available sentence and indicate honestly in the rendered output (e.g. "[no headline metric reported]" rather than fabricating).

STEP 2 — DESIGN the dashboard:

Above the fold (first viewport, no scroll):
- Hero band:
  * KEY FINDING as oversized statement (the page's largest type)
  * Paper title small, immediately below, linked to https://arxiv.org/abs/ID
  * Authors line (compact, truncate if >4 with "et al."), date, topic chips
- Asset row directly below hero:
  * KEY METRIC card — large numeral / phrase, with one-line context
  * WHY THIS MATTERS card — calm, dense, ~25 words
  * CRITICAL EDGE card — contrasting style (cautionary color), the extracted critique sentence

Body grid (below the fold, multi-column on desktop, stacked on mobile):
- Methodology card — distilled, NOT a transcription. Use bullets, sketched flow, or compact paragraphs to convey approach in ~100-200 words.
- Results card — the concrete findings beyond the headline metric. Tables rendered as styled HTML tables, not pre-blocks.
- Strengths / Limitations — explicit side-by-side panels (not sequential).
- Questions for Further Exploration — small panel at the bottom.

Top-left fixed nav element: "↩ Today's digest" link to ./index.html
Bottom: "↗ Markdown source" relative link to ./ID.md

Layout rules:
- CSS Grid for the dashboard; explicit visual hierarchy (hero > assets > body cards). The extracted assets are larger and more prominent than section bodies, period.
- ~min(95vw, 1100px) content width on desktop; single column under 720px
- System font stack, CJK-friendly line-height where Chinese appears
- One topic-derived accent color allowed (semantic, e.g. blue for systems, amber for theory, green for empirical) — but only ONE per page. Do not rainbow.
- No marketing gradients, no glass cards, no oversized non-content hero banners. The HERO IS THE KEY FINDING, not decoration.

Anti-patterns (do not do these):
- Rendering sections vertically in order of source markdown. The page is NOT a transcript.
- Hiding the Key Finding inside a section body. It's the page hero.
- Using <details> to collapse anything. Full dashboard is open by default.
- Decorative blobs / hero images of papers / marketing-style "Read more →" CTAs.

Constraints:
- Use only Read, Write, Glob, Grep tools. Do not run scripts.
- No browser available — state explicitly "not browser-verified".

Final response (<=80 words):
- The path written.
- One line: the Key Finding you extracted (so the orchestrator can sanity-check).
- "Not browser-verified, generated from source markdown."
