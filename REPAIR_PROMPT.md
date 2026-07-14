# TASK: Repair historical stub paper summaries in ~/Documents/daily_paper

You are repairing ~231 low-quality "stub" paper summaries across ~30 date folders.
A stub is a `.md` file that was written from only the paper's abstract (or contains
unfilled placeholders like `[待生成]`) even though the full PDF sits next to it on disk.
Your job: rewrite each stub as a REAL summary based on the actual PDF.

Work methodically. Do NOT try to do everything in one pass. One day at a time,
one paper at a time. Everything is resumable — state lives in each day's manifest.

## Paths and tools

- Data: `~/Documents/daily_paper/arxiv-daily/<YYYY-MM-DD>/` (per day: `<id>.md`, `<id>.pdf`, `search_results.json`, `manifest.json`, `overview.md`)
- Pipeline CLI: `python3 ~/.zcode/skills/daily-paper-overview/scripts/pipeline.py <cmd>`
- User interests (for the Relevance section): `~/Documents/daily_paper/interests.md` — read once at the start, keep the 8 area names in mind.
- Extract PDF text with: `pdftotext ~/Documents/daily_paper/arxiv-daily/<D>/<id>.pdf - | head -c 60000`

## IMPORTANT: deterministic quality gates are active

- `pipeline.py validate --date <D>` classifies every summary (`ok` / `abstract_only` / `thin` / `missing_sections` / `malformed` / `missing`) and exits 1 if any fail.
- `pipeline.py mark-paper ... --status done` RE-READS your file and EXITS 2 (refused) if it is still a stub, under ~800 effective words, or missing required sections. If refused: your summary is genuinely not good enough — improve it and retry. The most common refusal cause: you left the `⚠️ Abstract-only` banner or a placeholder line in the file after rewriting it. Delete those lines, re-check, retry.
- **`--force` is FORBIDDEN. You are not authorized to use it under any circumstances.** Every forced mark is recorded in the manifest as `quality_override`, audited after your session, and reverted — the paper will be redone, so forcing only wastes your work. If you believe a refusal is wrong, leave the paper in `retry-pending` and note it in your final report instead.
- `--status degraded` is ONLY for papers whose PDF text cannot be extracted (pdftotext < 500 bytes); it requires the file to start with a `⚠️ Abstract-only summary` banner and contain zero placeholder text.

## Accuracy rules (audits compare your summaries against the PDFs)

- Every number must keep its exact context: WHICH hardware/config/model size it was measured on, WHICH method/classifier produced it, and WHICH baseline it is compared against. Do not pair a number with a different setup mentioned nearby.
- Write `## Critical Assessment` from the FULL PDF, not the abstract. Before claiming "no scaling study" / "limited evaluation" / "missing ablation", check the experiments section actually lacks it.
- Never cite papers/methods from memory in Questions for Further Exploration — only reference work the PDF itself cites.

## Workflow

### Step 0 — Survey (read-only)
```bash
python3 ~/.zcode/skills/daily-paper-overview/scripts/pipeline.py repair-scan --all
```
Note each day's `repairable_with_pdf` list. IGNORE `legacy_missing_sections` (old-format but rich files — do not touch them). Note any `manifest_missing` days — do not touch those either; list them in your final report.

### Step 1 — Pick the newest unrepaired day D from the survey
```bash
python3 ~/.zcode/skills/daily-paper-overview/scripts/pipeline.py validate --date <D> --requeue
python3 ~/.zcode/skills/daily-paper-overview/scripts/pipeline.py retry-pending --date <D>
```

### Step 2 — For EACH id from retry-pending, one at a time:
1. `pdftotext .../<id>.pdf - | head -c 60000`
2. **If the output is ≥ 500 bytes of real text:** write the full summary to `.../<id>.md`, REPLACING the stub, using EXACTLY this structure:
   - YAML frontmatter: `title, authors, arxiv_id, aliases, date (the folder date), tags, url`
   - `> **一句话总结：**` (Chinese, must name the method AND the key result)
   - `> **TL;DR:**` (English; must name at least one dataset/benchmark, one baseline, and one quantitative delta when the paper has them)
   - `## 核心贡献` (Chinese bullets) and `## Key Contributions` (English bullets)
   - `## Methodology` (English — explain HOW the method works, enough that a reader could re-explain it; name model sizes, datasets, setup values)
   - `## Results & Highlights` (English — MUST contain ≥3 quantitative claims copied from the paper, each with metric + dataset + the paper's number + the strongest baseline's number or delta. If the paper truly has no quantitative results, write the literal line `No quantitative results reported` and describe its evidence instead)
   - `## Authors & Credibility` (ONLY affiliations/venue/code links stated in the PDF — never assert author fame)
   - `## Critical Assessment` (must cite ≥1 paper-specific weakness: a named weak baseline, missing ablation, data quirk — no generic sentences)
   - `## Strengths`, `## Limitations`
   - `## Relevance` (Chinese, 1-2 sentences naming WHICH configured interest area from interests.md this maps to)
   - `## Questions for Further Exploration`
   Never write `[待生成]`, "To be assessed from full paper", or any placeholder. Then:
   ```bash
   python3 ~/.zcode/skills/daily-paper-overview/scripts/pipeline.py mark-paper --date <D> --arxiv-id <id> --field summary --status done --path ~/Documents/daily_paper/arxiv-daily/<D>/<id>.md
   ```
   If exit code 2: read the refusal JSON's `classification`, fix that specific problem (usually: too short → add real detail from the PDF; missing section → add it), retry ONCE. If refused again, treat as unextractable (next case).
3. **If pdftotext output is < 500 bytes or errors:** the PDF is unextractable. Rewrite the file as an HONEST fallback: same frontmatter, then the line `> **⚠️ Abstract-only summary** — PDF text not extractable`, then all sections above filled with real sentences derived ONLY from this paper's abstract in `search_results.json` (no placeholders, no invented numbers). Then:
   ```bash
   python3 ~/.zcode/skills/daily-paper-overview/scripts/pipeline.py mark-paper --date <D> --arxiv-id <id> --field summary --status degraded --path ~/Documents/daily_paper/arxiv-daily/<D>/<id>.md
   ```
4. NEVER leave a paper unsettled: every requeued id ends this session as `done` or `degraded`.

### Step 3 — Close the day
```bash
python3 ~/.zcode/skills/daily-paper-overview/scripts/pipeline.py validate --date <D>
```
Must exit 0. If the day had ≥5 repaired papers, also regenerate `.../<D>/overview.md` (its one-liners were built from the stubs): read all `<id>.md` in the folder, write frontmatter (title/date/tags/papers count), `## 今日必读 / Must Read Today` (top 3 with bilingual reasons), `## 按主题分类 / Papers by Topic` (bilingual cells), `## All Papers` table using `[[id]]` wiki-links. Do NOT touch any `.html` files.

### Step 4 — Repeat Step 1 for the next-newest day. Stop cleanly at a day boundary when the session gets long; the next session resumes automatically (requeued papers stay in `retry-pending`).

## Phase 2 (only after ALL repairable days are done)

Some papers were previously marked `degraded` by runners that could not read PDFs, even though the PDFs extract fine (e.g. 16 papers on 2026-07-03). After the normal sweep is empty, run:
```bash
python3 ~/.zcode/skills/daily-paper-overview/scripts/pipeline.py repair-scan --all --include-degraded
```
For each listed degraded paper, test `pdftotext` yourself: if it yields ≥ 500 bytes, requeue that day with `repair-scan --days <N> --include-degraded --requeue` and repair per Step 2; if not, leave it degraded.

## Final report (each session)
Per day: N repaired (done), N degraded, validate exit code, N left in retry-pending (with reasons). Plus: days remaining, any `manifest_missing` days skipped. Your report is checked against the manifests — report exactly what the manifest says, including any refusals you could not resolve.
