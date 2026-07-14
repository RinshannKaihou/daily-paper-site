# AGENTS.md — Daily Paper Overview

> This file describes the `daily_paper` project for AI coding agents. The project is a personal arXiv paper curation and summarization pipeline that runs inside an Obsidian vault. All documentation, scripts, and orchestration logic are in English; the generated paper summaries are bilingual (Chinese + English).

---

## Project Overview

This project automatically fetches, filters, and summarizes recent arXiv papers according to a user-defined set of research interests. It is **not** a traditional software application with a build step or deployment target. Instead, it is a **content-generation pipeline** managed by the `daily-paper-overview` skill (a Kimi/Claude skill) and stored as an Obsidian vault for human reading.

### What it does

1. Queries the arXiv API (with HTML fallback) for recent papers across configured categories.
2. Uses an LLM subagent to semantically filter papers by relevance to the user's research interests.
3. Downloads PDFs for the filtered papers.
4. Dispatches LLM subagents to write detailed **bilingual** summaries (one `.md` file per paper).
5. Generates a daily `overview.md` that categorizes papers and highlights top picks.

### Where the code lives

- **Project root / data directory:** `~/Documents/daily_paper/`
- **Skill logic (scripts & workflow definitions):** `~/.kimi/skills/daily-paper-overview/`
  - `SKILL.md` — the master workflow document (orchestration steps, subagent prompts, context-budget rules).
  - `RUNBOOK.md` — recovery procedures after rate limits, crashes, or classifier blocks.
  - `scripts/pipeline.py` — manifest-driven pipeline orchestrator (Python 3, no external deps).
  - `scripts/arxiv_search.py` — arXiv API client with retry/backoff and HTML fallback.
  - `assets/interests_template.md` — template for new users.

---

## Technology Stack

| Layer | Technology |
|-------|------------|
| Language | Python 3 (stdlib only — no `requirements.txt`, no `pyproject.toml`) |
| API | arXiv Atom API (`export.arxiv.org/api/query`) + HTML listing fallback |
| Data format | JSON (manifests, search results, filtered lists) + Markdown (summaries) |
| Vault / Reader | Obsidian (`.obsidian/` config at project root) |
| Orchestration | Kimi/Claude skill (`daily-paper-overview`) dispatching subagents |

**No package managers, no build tools, no test framework.** The Python scripts are self-contained and use only the standard library.

---

## Directory Structure

```
~/Documents/daily_paper/
├── interests.md                    # User research interests config (editable)
├── AGENTS.md                       # This file
├── arxiv-daily/
│   └── <YYYY-MM-DD>/               # One folder per run date
│       ├── manifest.json           # Pipeline state (stages, per-paper status, retry queue)
│       ├── search_results.json     # Raw arXiv API output
│       ├── filtered_papers.json    # LLM-filtered relevance list
│       ├── overview.md             # Daily overview (categorized, bilingual)
│       ├── <arxiv_id>.md           # Bilingual paper summary
│       ├── <arxiv_id>.pdf          # Downloaded PDF
│       └── … (auxiliary JSONs from older runs)
│   └── weekly/
│       └── <YYYY-MMDD-MMDD>/      # One folder per ISO week, named by Mon-Sun bounds (e.g. 2026-0525-0531)
│           ├── week_papers.json    # Deterministic weekly aggregate (source of truth)
│           ├── all_papers_block.md # Verbatim full-index block for weekly.md
│           ├── weekly.md           # Weekly digest (must-reads + themes + index)
│           └── index.html          # Newspaper-style weekly front page
├── .obsidian/                      # Obsidian vault configuration
│   ├── app.json
│   ├── appearance.json
│   ├── core-plugins.json
│   └── workspace.json
└── .claude/
    └── settings.local.json         # Claude permissions (bash allow-list)
```

### Key files per date folder

| File | Purpose |
|------|---------|
| `manifest.json` | **Single source of truth** for pipeline state. Tracks `stages` (`fetched`, `filtered`, `overview_generated`, `html_rendered`) and per-paper `pdf_status` / `summary_status` / `html_status` (summary statuses: `pending`, `retry-pending`, `done`, `degraded`, `skipped`, `failed`). Atomic writes (tmp + rename). |
| `search_results.json` | Raw metadata from arXiv API (titles, authors, abstracts, URLs). |
| `filtered_papers.json` | Output of the semantic-filter subagent. Contains `total_evaluated`, `total_selected`, and a `papers` array with `relevance_score` (1–5) and `relevance_reason`. |
| `overview.md` | Human-readable daily digest with YAML frontmatter, "Must Read" picks, topic tables, and a full paper index. Uses Obsidian wiki-links. |
| `<arxiv_id>.md` | Individual paper summary. See **Content Format** below. |

---

## Workflow & Pipeline Stages

The pipeline is **fully resumable**. Every stage writes to `manifest.json`, so a session can restart exactly where it left off after rate limits, context-limit failures, or crashes.

### Stage 1 — Fetch

```bash
python3 ~/.kimi/skills/daily-paper-overview/scripts/pipeline.py init --date <YYYY-MM-DD>
python3 ~/.kimi/skills/daily-paper-overview/scripts/arxiv_search.py \
  --categories "cs.LG,cs.CL,cs.AI,cs.CV,cs.PF,cs.AR,stat.ML" \
  --date <YYYY-MM-DD> --max-results 500 \
  --output ~/Documents/daily_paper/arxiv-daily/<YYYY-MM-DD>/search_results.json
python3 ~/.kimi/skills/daily-paper-overview/scripts/pipeline.py mark-stage \
  --date <YYYY-MM-DD> --stage fetched --status done
```

(There is no `pipeline.py fetch` subcommand — fetching is `arxiv_search.py` directly, bracketed by `init` and `mark-stage`.)

- `arxiv_search.py` retries with exponential backoff + jitter on 429/5xx/timeout.
- Falls back to a 2-day range if a single date returns < 5 papers, and to HTML listing scrape if the API fails.
- Read the category list from `interests.md` (`categories` block) rather than hardcoding.

### Stage 2 — Filter (semantic)

An LLM subagent reads `search_results.json` + `interests.md`, rates each paper 1–5, and writes `filtered_papers.json`. After that:

```bash
python3 ~/.kimi/skills/daily-paper-overview/scripts/pipeline.py ingest --date <YYYY-MM-DD>
```

This seeds the manifest's `papers` dict and marks `filtered = "done"`.

### Stage 3 — Download PDFs

```bash
curl -L -o ~/Documents/daily_paper/arxiv-daily/<DATE>/<arxiv_id>.pdf \
  https://arxiv.org/pdf/<arxiv_id>.pdf
```

After each download, mark the manifest:

```bash
python3 ~/.kimi/skills/daily-paper-overview/scripts/pipeline.py mark-paper \
  --date <DATE> --arxiv-id <ID> --field pdf --status done
```

### Stage 4 — Summarize (batched subagents)

```bash
python3 ~/.kimi/skills/daily-paper-overview/scripts/pipeline.py pending --date <DATE>
```

Outputs one arxiv ID per line that needs a summary. Dispatch subagents in **parallel batches of max 5**, using the FULL Step 5 subagent prompt from `SKILL.md` (section format, content contract, honesty rules — do not improvise a shorter prompt). Each subagent:

- **Reads the PDF FIRST** at `~/Documents/daily_paper/arxiv-daily/<DATE>/<arxiv_id>.pdf` — the PDF is the primary source.
- Writes to `~/Documents/daily_paper/arxiv-daily/<DATE>/<arxiv_id>.md`
- ONLY if the PDF is missing/unreadable: writes an abstract-based fallback starting with `⚠️ Abstract-only summary`. Placeholder text (`[待生成]`, "To be assessed from full paper", etc.) is FORBIDDEN — such files fail validation and are re-opened.

After each subagent, update the manifest (`mark-paper` re-reads the file and REFUSES `--status done` for stub/thin/abstract-only content — fix the summary rather than forcing):

```bash
# Success
python3 ~/.kimi/skills/daily-paper-overview/scripts/pipeline.py mark-paper \
  --date <DATE> --arxiv-id <ID> --field summary --status done --path <path>.md

# Honest abstract-only fallback (PDF missing/unreadable)
python3 ~/.kimi/skills/daily-paper-overview/scripts/pipeline.py mark-paper \
  --date <DATE> --arxiv-id <ID> --field summary --status degraded --path <path>.md

# Rate-limit / transient failure → retry queue
python3 ~/.kimi/skills/daily-paper-overview/scripts/pipeline.py requeue \
  --date <DATE> --arxiv-id <ID> --reason "rate-limit"
```

**After every batch**, run the content-aware validation gate (exits non-zero if any summary is a stub / abstract-only / thin / malformed):

```bash
python3 ~/.kimi/skills/daily-paper-overview/scripts/pipeline.py validate --date <DATE>

# Re-open everything repairable (PDF on disk) in one step, then re-dispatch those IDs:
python3 ~/.kimi/skills/daily-paper-overview/scripts/pipeline.py validate --date <DATE> --requeue
```

Retry queue papers are processed in a second pass with **batches of max 3**. Do not proceed to Stage 5 while `validate` fails.

### Stage 5 — Overview generation

When all summaries are done (`pending` and `retry-pending` are empty), dispatch one subagent to read all `.md` files in the date folder and write `overview.md`. Then mark:

```bash
python3 ~/.kimi/skills/daily-paper-overview/scripts/pipeline.py mark-stage \
  --date <DATE> --stage overview_generated --status done
```

### Stage 6 — Weekly Digest (rollup of daily overviews)

A separate, on-demand stage that condenses a week of daily `overview.md` files
into one digest (**Top ~8 must-reads + 4-6 themes + complete index**). Triggered
by "weekly summary / 周报 / 每周总结 / this week's papers". The daily overviews are
the only input — never re-read per-paper `.md` or PDFs.

Driven by `scripts/weekly_digest.py` (stdlib only, atomic writes; same style as
`pipeline.py`). The script does the **deterministic, lossless** aggregation;
subagents do the **editorial** synthesis. (Real skill dir on this machine:
`~/.claude/skills/daily-paper-overview/`; this file uses the `~/.kimi/...` mirror
path for consistency with the commands above.)

```bash
# 1. Resolve the ISO week (Mon-Sun) and see which days have an overview.
#    --week accepts: last | YYYY-MMDD-MMDD | YYYY-Www | YYYY-MM-DD  (folders named by Mon-Sun bounds)
python3 ~/.kimi/skills/daily-paper-overview/scripts/weekly_digest.py resolve --week last
#    If the week is ambiguous or weekdays are missing, ASK the user first.

# 2. Aggregate → weekly/<YYYY-MMDD-MMDD>/week_papers.json + all_papers_block.md
python3 ~/.kimi/skills/daily-paper-overview/scripts/weekly_digest.py aggregate --week <YYYY-MMDD-MMDD>
```

Then dispatch **two** subagents (full prompts in `SKILL.md` → "Weekly Digest
Workflow"):

1. **Synthesis** → writes `weekly/<YYYY-MMDD-MMDD>/weekly.md`. Reads `week_papers.json`
   (+ the daily overviews for reasons). Picks ~8 must-reads (prefer papers
   recurring across `days_seen`), merges ~12 daily topics into 4-6 themes, and
   emits the literal `<!-- ALL_PAPERS_BLOCK -->` marker — it must NOT paste the
   paper index itself (LLMs truncate long pastes). After it returns, inject the
   full index deterministically:

   ```bash
   # 3. Replace the marker with all_papers_block.md verbatim (guarantees completeness)
   python3 ~/.kimi/skills/daily-paper-overview/scripts/weekly_digest.py assemble --week <YYYY-MMDD-MMDD>
   ```
2. **HTML** → writes `weekly/<YYYY-MMDD-MMDD>/index.html` (newspaper front page,
   mirrors daily Step 7a). Links cards via each paper's pre-resolved `link`
   field. Non-blocking — `weekly.md` is the durable artifact.

`weekly_digest.py` is read-only over the daily folders and only writes under
`weekly/<YYYY-MMDD-MMDD>/`; it never touches `manifest.json` or any daily file.

### Pre-flight / resume check

Always run this before starting work for a date:

```bash
python3 ~/.kimi/skills/daily-paper-overview/scripts/pipeline.py resume --date <DATE>
```

Returns JSON with `manifest_exists`, `stages`, `pending_main`, `pending_retry`, `pending_html`, `needs_overview`, and `next_step` (`init` / `summarize` / `render_per_paper` / `overview` / `html_render` / `done`). Use `next_step` to decide which stage to re-enter.

Also run the quality repair sweep once per session (read-only; ~1s):

```bash
python3 ~/.kimi/skills/daily-paper-overview/scripts/pipeline.py repair-scan --days 14
```

If `total_repairable_with_pdf` > 0, report it to the user and ask before repairing (`repair-scan --days 14 --requeue`, then re-run Stage 4 for the re-opened IDs on each affected date).

### End-of-day audit

Before reporting completion for a date, run:

```bash
python3 ~/.kimi/skills/daily-paper-overview/scripts/pipeline.py finalize --date <DATE>
```

If `passed` is false, surface the `todo` list instead of claiming success.

---

## Content Format

### `interests.md`

A markdown file with fenced code blocks:

- `areas` — natural-language research interests (read by LLM for semantic filtering).
- `categories` — arXiv category codes (one per line).
- `settings` — `max_papers: <int>`.

### Paper summary (`<arxiv_id>.md`)

Every paper summary **must** have:

- YAML frontmatter: `title`, `authors`, `arxiv_id`, `aliases`, `date`, `tags`, `url`.
- A one-line Chinese summary (`> **一句话总结：**`).
- An English TL;DR (`> **TL;DR:**`).
- Sections (bilingual where noted):
  - `## 核心贡献` (Chinese bullet points)
  - `## Key Contributions` (English)
  - `## Methodology` (English)
  - `## Results & Highlights` (English)
  - `## Authors & Credibility` (English)
  - `## Critical Assessment` (English — novelty, rigor, reproducibility, significance, red flags)
  - `## Strengths` (English)
  - `## Limitations` (English)
  - `## Relevance` (Chinese, 1–2 sentences)
  - `## Questions for Further Exploration` (English)

### Daily overview (`overview.md`)

- YAML frontmatter: `title`, `date`, `tags`, `papers`.
- `## 今日必读 / Must Read Today` — top 3 picks with bilingual reasons.
- `## 按主题分类 / Papers by Topic` — tables with bilingual cells.
- `## All Papers` — full index table.
- Obsidian wiki-links: `[[arxiv_id]]` followed by short title.

> The daily template has drifted over time (the must-read and All-Papers tables
> have used several column layouts). `weekly_digest.py` parses them
> **header-aware** and matches arxiv IDs by regex, so the weekly rollup stays
> complete across formats. If you change the daily `overview.md` structure,
> re-verify weekly aggregation (`aggregate` total == union of `[[id]]` across the
> week's overviews).

### Weekly digest (`weekly.md`)

Produced by Stage 6 under `arxiv-daily/weekly/<YYYY-MMDD-MMDD>/`. Bilingual, same house
style as the daily overview:

- YAML frontmatter: `title`, `week`, `date_range`, `tags`, `papers` (unique count).
- `## 本周必读 / Must Read This Week` — ~8 picks (prefer papers recurring across
  days), each with a bilingual reason.
- `## 本周主题脉络 / Themes This Week` — 4-6 cross-cutting themes, each a short
  bilingual narrative + representative `[[arxiv_id]]` highlights.
- `## 全部论文 / All Papers` — the verbatim `all_papers_block.md` (grouped by
  first-seen day; ⭐ = daily must-read, ↻ = recurred on other days) — guarantees
  completeness.
- Companion `week_papers.json` is the deterministic source of truth for the week.

---

## Development Conventions

### Context budget is the #1 constraint

The skill's `SKILL.md` explicitly treats context conservation as the highest priority:

- The **main agent must only orchestrate** — never read large JSON files, PDFs, or summaries into its own context.
- Use **file paths as handoffs** to subagents.
- Keep main-thread responses to **one-line confirmations**.
- Launch summarization subagents in **batches of max 5** (retry pass: max 3).

### Subagent contract

Every subagent dispatch must specify:

1. Input paths (read-only).
2. A single output path (one file).
3. A line forbidding writes outside the date folder.

This prevents subagents from creating unauthorized files in the project root.

### Atomic writes

`pipeline.py` writes `manifest.json` atomically via `mkstemp` + `os.replace`. It is safe to read the manifest manually, but **never write it by hand from the main thread** — always use `pipeline.py` subcommands.

### Date conventions

- Folder names are strict `YYYY-MM-DD`.
- arXiv posts Mon–Fri around 20:00 US/Eastern (DST-aware); weekends have no new batch. Use `pipeline.py resolve-date --when today` to get a machine-readable status (`ok` / `not_yet_published` / `weekend_no_papers`) plus `most_recent_published`. Report and ask on a non-`ok` status rather than silently falling back. Holidays are not modelled — if a chosen date returns <5 papers, `arxiv_search.py`'s existing single-date→2-day auto-expand covers it. (The old rule of thumb — "before 9am Beijing time means yesterday's batch" — is subsumed by this, since 20:00 ET ≈ 08:00–09:00 Beijing.)

---

## Testing & Quality

There is **no automated test suite**. Quality is ensured through:

1. **Resumable idempotency** — re-dispatching `pending` papers is always safe.
2. **Manifest-driven state** — the manifest prevents duplicate work.
3. **Deterministic quality gates** — `pipeline.py validate` classifies every summary's content (`ok` / `abstract_only` / `thin` / `missing_sections` / `malformed` / `missing`) and exits non-zero on failures; `mark-paper` refuses `--status done` for content-invalid files; `finalize` audits the whole day; `repair-scan` re-opens historical stubs once PDFs are available. These gates are framework-independent — they hold regardless of which LLM executes the pipeline.
4. **Human review** — summaries are consumed in Obsidian; the user can manually edit any `.md` file.
5. **Graceful degradation** — if a PDF is unreadable, the subagent falls back to abstract-only, marks `⚠️ Abstract-only summary` at the top, and the orchestrator records it with `mark-paper --status degraded` in the SAME run (the command verifies the banner and refuses placeholder stubs). Degraded is terminal by default — sweeps skip it, so unextractable PDFs don't churn; re-attempt deliberately with `repair-scan --include-degraded --requeue`. Placeholder stubs (`[待生成]` etc.) are never acceptable.

---

## Security Considerations

- **No secrets or credentials** — the arXiv API is public and read-only.
- **SSL handling** — `arxiv_search.py` creates a permissive SSL context (`verify_mode = CERT_NONE`) because macOS Python often lacks proper CA certs for the arXiv API. This is acceptable because the API is public read-only and the data is academic papers.
- **No network egress beyond arXiv** — the only external calls are to `export.arxiv.org`, `arxiv.org/list`, and `arxiv.org/pdf`.
- **Claude permissions** — `.claude/settings.local.json` contains an explicit `allow` list for bash commands (curl, python3, ls, pdftotext, etc.). New commands needed by agents may require updating this allow-list.

---

## Common Commands

```bash
# Check what work remains for a date
python3 ~/.kimi/skills/daily-paper-overview/scripts/pipeline.py resume --date 2026-04-28

# Human-readable status
python3 ~/.kimi/skills/daily-paper-overview/scripts/pipeline.py status --date 2026-04-28

# List IDs needing summary (main pass)
python3 ~/.kimi/skills/daily-paper-overview/scripts/pipeline.py pending --date 2026-04-28

# List IDs in retry queue
python3 ~/.kimi/skills/daily-paper-overview/scripts/pipeline.py retry-pending --date 2026-04-28

# Mark a paper summary as done
python3 ~/.kimi/skills/daily-paper-overview/scripts/pipeline.py mark-paper \
  --date 2026-04-28 --arxiv-id 2604.12345 --field summary --status done \
  --path ~/Documents/daily_paper/arxiv-daily/2026-04-28/2604.12345.md

# Requeue after rate limit
python3 ~/.kimi/skills/daily-paper-overview/scripts/pipeline.py requeue \
  --date 2026-04-28 --arxiv-id 2604.12345 --reason "rate-limit"
```

---

## Obsidian Integration

The project root is an Obsidian vault. All markdown files use standard markdown with YAML frontmatter. Wiki-links (`[[arxiv_id]]`) enable graph navigation between the daily overview and individual paper notes. The `.obsidian/workspace.json` stores the user's UI layout and recently opened files — treat it as user state, not project code.

---

## Notes for Agents

- **Do not assume a traditional build/test/deploy cycle.** This is a content pipeline, not a deployable service.
- **Do not read large JSON or PDF files into the main conversation.** Pass file paths to subagents.
- **Always check the manifest before doing work.** Use `pipeline.py resume --date <DATE>`.
- **Preserve bilingual structure** when editing or regenerating any `.md` file.
- **Respect the subagent contract** (one output file, no writes outside the date folder).
- **Do not modify `.obsidian/` or `.claude/` files** unless explicitly asked.
