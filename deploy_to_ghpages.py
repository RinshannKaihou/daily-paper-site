#!/usr/bin/env python3
"""Build a GitHub Pages-ready HTML snapshot of the daily-paper archive.

Usage:
    python3 deploy_to_ghpages.py [--dry-run]

Outputs a ``_site/`` directory next to this script containing only the files
that should be published. The existing vault (PDFs, markdown, config) is left
untouched.
"""

from __future__ import annotations

import argparse
import html
import os
import re
import shutil
import sys
from datetime import datetime
from pathlib import Path

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------
PROJECT_ROOT = Path(__file__).resolve().parent
ARXIV_DAILY = PROJECT_ROOT / "arxiv-daily"
SITE_DIR = PROJECT_ROOT / "_site"

DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
ARXIV_ID_RE = re.compile(r"^(\d{4}\.\d{4,5})(?:v\d+)?$")

# ---------------------------------------------------------------------------
# Logging
# ---------------------------------------------------------------------------
def log(msg: str) -> None:
    print(f"[deploy] {msg}")


# ---------------------------------------------------------------------------
# File discovery
# ---------------------------------------------------------------------------
def discover_existing_html() -> list[Path]:
    """Return all HTML files that already exist in the vault."""
    if not ARXIV_DAILY.exists():
        return []
    html_files = []
    for path in ARXIV_DAILY.rglob("*.html"):
        html_files.append(path)
    root_index = PROJECT_ROOT / "index.html"
    if root_index.exists():
        html_files.append(root_index)
    return html_files


def discover_markdown() -> list[Path]:
    """Return all markdown files under arxiv-daily."""
    if not ARXIV_DAILY.exists():
        return []
    return list(ARXIV_DAILY.rglob("*.md"))


def is_per_paper_md(path: Path) -> tuple[bool, str]:
    """True for <arxiv_id>[vN].md files. Returns (is_paper, canonical_id_without_version)."""
    m = ARXIV_ID_RE.match(path.stem)
    if m:
        return True, m.group(1)
    return False, ""


# ---------------------------------------------------------------------------
# Copy existing HTML
# ---------------------------------------------------------------------------
def copy_existing_html(dry_run: bool) -> dict[Path, Path]:
    """Copy existing HTML into _site preserving relative structure."""
    copied: dict[Path, Path] = {}  # source -> dest
    for src in discover_existing_html():
        rel = src.relative_to(PROJECT_ROOT)
        dest = SITE_DIR / rel
        if not dry_run:
            dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src, dest)
        copied[src] = dest
    log(f"{'would copy' if dry_run else 'copied'} {len(copied)} existing HTML files")
    return copied


# ---------------------------------------------------------------------------
# Markdown -> simple HTML
# ---------------------------------------------------------------------------
def extract_frontmatter(text: str) -> tuple[str, str]:
    """Return (frontmatter_block, remainder). Empty frontmatter if none."""
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n", text, re.DOTALL)
    if not m:
        return "", text
    return m.group(1), text[m.end():]


def parse_frontmatter(block: str) -> dict[str, str]:
    data: dict[str, str] = {}
    for line in block.splitlines():
        if ":" not in line:
            continue
        key, val = line.split(":", 1)
        key = key.strip()
        val = val.strip().strip('"').strip("'")
        data[key] = val
    return data


def inline_md_to_html(text: str) -> str:
    # Obsidian wiki-links: [[id]] or [[id|Title]]
    def wiki_link(m: re.Match) -> str:
        inner = m.group(1)
        if "|" in inner:
            aid, title = inner.split("|", 1)
            return f'<a href="{html.escape(aid.strip())}.html">{html.escape(title.strip())}</a>'
        return f'<a href="{html.escape(inner.strip())}.html">{html.escape(inner.strip())}</a>'

    text = re.sub(r"\[\[([^\]]+)\]\]", wiki_link, text)

    # Bold / italic
    text = re.sub(r"\*\*\*(.+?)\*\*\*", r"<strong><em>\1</em></strong>", text)
    text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"(?<!\*)\*(?!\*)(.+?)(?<!\*)\*(?!\*)", r"<em>\1</em>", text)

    # Inline code
    text = re.sub(r"`([^`]+)`", r"<code>\1</code>", text)

    # External links [text](url)
    def ext_link(m: re.Match) -> str:
        t, u = m.group(1), m.group(2)
        return f'<a href="{html.escape(u, quote=True)}">{html.escape(t)}</a>'
    text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", ext_link, text)

    return text


def markdown_to_html(text: str, title: str = "Paper summary") -> str:
    front_block, body = extract_frontmatter(text)
    fm = parse_frontmatter(front_block)

    display_title = fm.get("title") or title
    authors = fm.get("authors", "")
    arxiv_id = fm.get("arxiv_id", "")
    url = fm.get("url", "")
    date = fm.get("date", "")
    tags = fm.get("tags", "")

    # Header block from frontmatter
    meta_parts = []
    if authors:
        meta_parts.append(f"<p class=\"authors\">{html.escape(authors)}</p>")
    if arxiv_id:
        meta_parts.append(f'<p class=\"meta\">arXiv: {html.escape(arxiv_id)}</p>')
    if date:
        meta_parts.append(f'<p class=\"meta\">Date: {html.escape(date)}</p>')
    if tags:
        meta_parts.append(f'<p class=\"meta\">Tags: {html.escape(tags)}</p>')
    if url:
        meta_parts.append(f'<p class=\"meta\"><a href="{html.escape(url, quote=True)}">{html.escape(url)}</a></p>')

    meta_html = "\n".join(meta_parts)

    # Convert body blocks
    lines = body.splitlines()
    out_lines: list[str] = []
    in_code = False
    code_buffer: list[str] = []
    in_list = False
    list_buffer: list[str] = []
    list_ordered = False

    def flush_list() -> None:
        nonlocal in_list, list_buffer, list_ordered
        if not in_list:
            return
        tag = "ol" if list_ordered else "ul"
        items = "\n".join(f"<li>{inline_md_to_html(item)}</li>" for item in list_buffer)
        out_lines.append(f"<{tag}>\n{items}\n</{tag}>")
        in_list = False
        list_buffer = []

    def flush_code() -> None:
        nonlocal in_code, code_buffer
        if not in_code:
            return
        code = html.escape("\n".join(code_buffer))
        out_lines.append(f"<pre><code>{code}</code></pre>")
        in_code = False
        code_buffer = []

    for raw in lines:
        stripped = raw.strip()

        # Code fences
        if stripped.startswith("```"):
            if in_code:
                flush_code()
            else:
                in_code = True
            continue

        if in_code:
            code_buffer.append(raw)
            continue

        # Headings
        if stripped.startswith("#"):
            flush_list()
            level = len(stripped) - len(stripped.lstrip("#"))
            level = min(max(level, 1), 6)
            content = stripped.lstrip("#").strip()
            out_lines.append(f"<h{level}>{inline_md_to_html(content)}</h{level}>")
            continue

        # Blockquotes
        if stripped.startswith(">"):
            flush_list()
            content = stripped.lstrip(">").strip()
            out_lines.append(f'<blockquote>{inline_md_to_html(content)}</blockquote>')
            continue

        # Lists
        unordered = re.match(r"^[-*+]\s+(.+)$", stripped)
        ordered = re.match(r"^\d+\.\s+(.+)$", stripped)
        if unordered or ordered:
            is_ordered = bool(ordered)
            item_text = (unordered or ordered).group(1)
            if in_list and list_ordered != is_ordered:
                flush_list()
            if not in_list:
                in_list = True
                list_ordered = is_ordered
            list_buffer.append(item_text)
            continue
        else:
            flush_list()

        # Empty line -> paragraph break
        if not stripped:
            continue

        # Plain paragraph
        out_lines.append(f"<p>{inline_md_to_html(stripped)}</p>")

    flush_list()
    flush_code()

    body_html = "\n".join(out_lines)

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{html.escape(display_title)}</title>
<style>
:root {{ --paper:#fafafa; --ink:#1a1a1a; --muted:#555; --accent:#1a5276; --line:#ddd; --sans:-apple-system,BlinkMacSystemFont,"Segoe UI",Helvetica,Arial,sans-serif; --serif:Georgia,"Noto Serif SC",serif; }}
body {{ font-family:var(--serif); background:var(--paper); color:var(--ink); line-height:1.6; margin:0; padding:0; }}
.container {{ max-width:min(95vw, 760px); margin:0 auto; padding:28px 20px 60px; }}
.topnav {{ position:fixed; top:12px; left:14px; z-index:50; font-family:var(--sans); font-size:.75rem; background:var(--paper); border:1px solid var(--line); padding:5px 10px; border-radius:999px; }}
.topnav a {{ color:var(--muted); text-decoration:none; font-weight:600; }}
.topnav a:hover {{ color:var(--accent); }}
h1 {{ font-size:1.6rem; margin:2.2rem 0 1rem; border-bottom:2px solid var(--accent); padding-bottom:.3rem; }}
h2 {{ font-size:1.3rem; margin:1.8rem 0 .8rem; color:var(--accent); }}
h3 {{ font-size:1.1rem; margin:1.4rem 0 .6rem; }}
p {{ margin:.8rem 0; }}
.authors {{ font-style:italic; color:var(--muted); margin-top:-.4rem; }}
.meta {{ font-family:var(--sans); font-size:.82rem; color:var(--muted); margin:.2rem 0; }}
a {{ color:var(--accent); text-decoration:none; }}
a:hover {{ text-decoration:underline; }}
blockquote {{ border-left:3px solid var(--accent); margin:1rem 0; padding:.2rem 0 .2rem 1rem; color:var(--muted); font-style:italic; }}
code {{ font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace; background:#f0f0f0; padding:2px 5px; border-radius:3px; font-size:.9em; }}
pre {{ background:#f5f5f5; padding:14px; overflow-x:auto; border-radius:4px; border:1px solid var(--line); }}
pre code {{ background:transparent; padding:0; }}
ul,ol {{ margin:.6rem 0; padding-left:1.5rem; }}
li {{ margin:.25rem 0; }}
table {{ border-collapse:collapse; width:100%; margin:1rem 0; font-family:var(--sans); font-size:.9rem; }}
th,td {{ border:1px solid var(--line); padding:6px 10px; text-align:left; }}
th {{ background:#f0f0f0; }}
hr {{ border:none; border-top:1px solid var(--line); margin:1.5rem 0; }}
.note {{ font-family:var(--sans); font-size:.78rem; color:var(--muted); border-top:1px solid var(--line); margin-top:2rem; padding-top:1rem; }}
@media (max-width: 600px) {{ .container {{ padding:22px 14px 40px; }} h1 {{ font-size:1.35rem; }} }}
</style>
</head>
<body>
<div class="topnav"><a href="./index.html">← Today's digest</a></div>
<div class="container">
<h1>{html.escape(display_title)}</h1>
{meta_html}
{body_html}
<p class="note">Generated from Markdown summary. Full paper: <a href="https://arxiv.org/abs/{html.escape(arxiv_id)}">arXiv:{html.escape(arxiv_id)}</a></p>
</div>
</body>
</html>
"""


def generate_missing_html(dry_run: bool) -> list[tuple[Path, Path]]:
    """Generate simple HTML for every per-paper .md without a dashboard .html."""
    generated: list[tuple[Path, Path]] = []
    md_files = discover_markdown()
    for md_path in md_files:
        is_paper, canonical_id = is_per_paper_md(md_path)
        if not is_paper:
            continue
        # Output file uses canonical id without version suffix
        html_dest = SITE_DIR / md_path.relative_to(PROJECT_ROOT).with_name(f"{canonical_id}.html")
        if html_dest.exists():
            continue  # dashboard HTML already exists
        if dry_run:
            generated.append((md_path, html_dest))
            continue
        try:
            text = md_path.read_text(encoding="utf-8", errors="replace")
        except OSError as e:
            log(f"warning: could not read {md_path}: {e}")
            continue
        html_dest.parent.mkdir(parents=True, exist_ok=True)
        html_content = markdown_to_html(text, title=canonical_id)
        html_dest.write_text(html_content, encoding="utf-8")
        generated.append((md_path, html_dest))
    log(f"{'would generate' if dry_run else 'generated'} {len(generated)} simple HTML pages from Markdown")
    return generated


def generate_missing_daily_indices(dry_run: bool) -> list[tuple[Path, Path]]:
    """Generate index.html for any day folder that lacks a dashboard index.html.

    Prefer converting overview.md. If no overview exists, build a minimal
    listing page from the per-paper HTML files in that folder.
    """
    generated: list[tuple[Path, Path]] = []
    if not ARXIV_DAILY.exists():
        return generated
    for day_dir in ARXIV_DAILY.iterdir():
        if not day_dir.is_dir() or day_dir.name == "weekly":
            continue
        index_html = SITE_DIR / "arxiv-daily" / day_dir.name / "index.html"
        if index_html.exists():
            continue

        overview = day_dir / "overview.md"
        if overview.exists():
            if dry_run:
                generated.append((overview, index_html))
                continue
            try:
                text = overview.read_text(encoding="utf-8", errors="replace")
            except OSError as e:
                log(f"warning: could not read {overview}: {e}")
                continue
            index_html.parent.mkdir(parents=True, exist_ok=True)
            html_content = markdown_to_html(text, title=f"Daily arXiv Digest — {day_dir.name}")
            index_html.write_text(html_content, encoding="utf-8")
            generated.append((overview, index_html))
            continue

        # No overview: build a minimal listing from paper HTMLs
        site_day_dir = SITE_DIR / "arxiv-daily" / day_dir.name
        if not site_day_dir.exists():
            continue
        paper_links = []
        for p in sorted(site_day_dir.glob("*.html")):
            if p.name == "index.html":
                continue
            title = p.stem
            paper_links.append(f'<li><a href="./{p.name}">{html.escape(title)}</a></li>')
        if not paper_links:
            continue
        if dry_run:
            generated.append((day_dir, index_html))
            continue
        index_html.parent.mkdir(parents=True, exist_ok=True)
        html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Daily arXiv Digest — {day_dir.name}</title>
<style>
:root {{ --paper:#fafafa; --ink:#1a1a1a; --muted:#555; --accent:#1a5276; --line:#ddd; --sans:-apple-system,BlinkMacSystemFont,"Segoe UI",Helvetica,Arial,sans-serif; --serif:Georgia,"Noto Serif SC",serif; }}
body {{ font-family:var(--serif); background:var(--paper); color:var(--ink); line-height:1.6; margin:0; padding:0; }}
.container {{ max-width:min(95vw, 760px); margin:0 auto; padding:28px 20px 60px; }}
.topnav {{ position:fixed; top:12px; left:14px; z-index:50; font-family:var(--sans); font-size:.75rem; background:var(--paper); border:1px solid var(--line); padding:5px 10px; border-radius:999px; }}
.topnav a {{ color:var(--muted); text-decoration:none; font-weight:600; }}
.topnav a:hover {{ color:var(--accent); }}
h1 {{ font-size:1.6rem; margin:2.2rem 0 1rem; border-bottom:2px solid var(--accent); padding-bottom:.3rem; }}
a {{ color:var(--accent); text-decoration:none; }}
a:hover {{ text-decoration:underline; }}
ul {{ margin:.6rem 0; padding-left:1.5rem; }}
li {{ margin:.35rem 0; }}
.note {{ font-family:var(--sans); font-size:.78rem; color:var(--muted); border-top:1px solid var(--line); margin-top:2rem; padding-top:1rem; }}
</style>
</head>
<body>
<div class="topnav"><a href="../../index.html">← Archive</a></div>
<div class="container">
<h1>Daily arXiv Digest — {day_dir.name}</h1>
<p>{len(paper_links)} papers curated for this date.</p>
<ul>
{chr(10).join(paper_links)}
</ul>
<p class="note">Generated automatically from available paper summaries.</p>
</div>
</body>
</html>
"""
        index_html.write_text(html_content, encoding="utf-8")
        generated.append((day_dir, index_html))
    log(f"{'would generate' if dry_run else 'generated'} {len(generated)} daily index.html pages")
    return generated


# ---------------------------------------------------------------------------
# Link rewriting
# ---------------------------------------------------------------------------
def fix_internal_links(dry_run: bool) -> tuple[int, int]:
    """Rewrite internal .md links to .html in all _site HTML files."""
    md_link_re = re.compile(r'href="([^"]*\.md)"')
    # Weekly pages embed paper paths in JS data arrays like
    # ["2606.20622","../../2026-06-22/2606.20622.md","md"]
    embedded_md_re = re.compile(r'((?:\.\./)+\d{4}-\d{2}-\d{2}/\d{4}\.\d{4,5})\.md')
    fixed_files = 0
    total_replacements = 0

    for html_path in SITE_DIR.rglob("*.html"):
        text = html_path.read_text(encoding="utf-8", errors="replace")
        new_text, n = md_link_re.subn(lambda m: rewrite_one_link(html_path, m.group(1)), text)
        new_text, n2 = embedded_md_re.subn(r'\1.html', new_text)
        n += n2
        if n:
            total_replacements += n
            fixed_files += 1
            if not dry_run:
                html_path.write_text(new_text, encoding="utf-8")

    log(f"{'would rewrite' if dry_run else 'rewrote'} {total_replacements} .md links in {fixed_files} files")
    return fixed_files, total_replacements


def fix_pdf_links(dry_run: bool) -> tuple[int, int]:
    """Rewrite local PDF links to arxiv.org/pdf/<id>.pdf."""
    pdf_link_re = re.compile(r'href="([^"]*\.pdf)"')
    arxiv_pdf_re = re.compile(r'(\d{4}\.\d{4,5})(?:v\d+)?\.pdf$')
    fixed_files = 0
    total_replacements = 0

    for html_path in SITE_DIR.rglob("*.html"):
        text = html_path.read_text(encoding="utf-8", errors="replace")
        new_text = text
        n = 0

        def pdf_repl(m: re.Match) -> str:
            href = m.group(1)
            if "://" in href or href.startswith("#"):
                return m.group(0)
            fname = Path(href).name
            am = arxiv_pdf_re.search(fname)
            if am:
                aid = am.group(1)
                return f'href="https://arxiv.org/pdf/{aid}.pdf"'
            return m.group(0)

        new_text, n = pdf_link_re.subn(pdf_repl, text)
        if n:
            total_replacements += n
            fixed_files += 1
            if not dry_run:
                html_path.write_text(new_text, encoding="utf-8")

    log(f"{'would rewrite' if dry_run else 'rewrote'} {total_replacements} local PDF links in {fixed_files} files")
    return fixed_files, total_replacements


def strip_version_suffixes(dry_run: bool) -> tuple[int, int]:
    """Strip arXiv version suffixes from internal HTML links (e.g. 2604.12345v1.html -> 2604.12345.html)."""
    version_href_re = re.compile(r'href="([^"]*(\d{4}\.\d{4,5})v\d+\.html)"')
    fixed_files = 0
    total_replacements = 0

    for html_path in SITE_DIR.rglob("*.html"):
        text = html_path.read_text(encoding="utf-8", errors="replace")

        def version_repl(m: re.Match) -> str:
            href = m.group(1)
            if "://" in href:
                return m.group(0)
            aid = m.group(2)
            # Build replacement href with same path prefix but stripped version
            prefix = href[:href.rfind('/') + 1] if '/' in href else ''
            return f'href="{prefix}{aid}.html"'

        new_text, n = version_href_re.subn(version_repl, text)
        if n:
            total_replacements += n
            fixed_files += 1
            if not dry_run:
                html_path.write_text(new_text, encoding="utf-8")

    log(f"{'would strip' if dry_run else 'stripped'} {total_replacements} version suffixes in {fixed_files} files")
    return fixed_files, total_replacements


def fix_orphan_paper_links(dry_run: bool) -> tuple[int, int]:
    """Final pass: rewrite relative paper links to arxiv.org/abs/<id> when the local HTML is missing."""
    paper_href_re = re.compile(r'href="([^"]*(\d{4}\.\d{4,5})\.html)"')
    fixed_files = 0
    total_replacements = 0

    for html_path in SITE_DIR.rglob("*.html"):
        text = html_path.read_text(encoding="utf-8", errors="replace")

        def orphan_repl(m: re.Match) -> str:
            href = m.group(1)
            if "://" in href or href.startswith("#"):
                return m.group(0)
            target = (html_path.parent / href).resolve()
            try:
                target.relative_to(SITE_DIR.resolve())
            except ValueError:
                return m.group(0)
            if target.exists():
                return m.group(0)
            aid = m.group(2)
            return f'href="https://arxiv.org/abs/{aid}"'

        new_text, n = paper_href_re.subn(orphan_repl, text)
        if n:
            total_replacements += n
            fixed_files += 1
            if not dry_run:
                html_path.write_text(new_text, encoding="utf-8")

    log(f"{'would rewrite' if dry_run else 'rewrote'} {total_replacements} orphan paper links in {fixed_files} files")
    return fixed_files, total_replacements


def rewrite_one_link(from_html: Path, href: str) -> str:
    """Return the replacement href=... string for a single .md link."""
    # If the href is already absolute (http/https/mailto/etc), leave it.
    if "://" in href or href.startswith("#"):
        return f'href="{href}"'

    # Resolve relative to the site root
    target = (from_html.parent / href).resolve()
    try:
        target_rel = target.relative_to(SITE_DIR.resolve())
    except ValueError:
        return f'href="{href}"'

    # overview.md -> index.html
    if target_rel.name == "overview.md":
        new_rel = target_rel.with_name("index.html")
        new_href = compute_relative(from_html.parent, SITE_DIR / new_rel)
        return f'href="{new_href}"'

    # <id>.md -> <id>.html
    new_rel = target_rel.with_suffix(".html")
    new_href = compute_relative(from_html.parent, SITE_DIR / new_rel)
    return f'href="{new_href}"'


def compute_relative(from_dir: Path, to_file: Path) -> str:
    """Return a relative path string from from_dir to to_file."""
    return os.path.relpath(to_file, from_dir)


def fix_absolute_paths(dry_run: bool) -> int:
    """Remove absolute filesystem paths that accidentally leaked into HTML."""
    abs_re = re.compile(re.escape(str(PROJECT_ROOT)) + r"[^\"'<>\s]*")
    fixed = 0
    for html_path in SITE_DIR.rglob("*.html"):
        text = html_path.read_text(encoding="utf-8", errors="replace")
        if abs_re.search(text):
            # Replace with empty or a relative fragment; specific fix for known leak.
            new_text = abs_re.sub("", text)
            fixed += 1
            if not dry_run:
                html_path.write_text(new_text, encoding="utf-8")
    log(f"{'would fix' if dry_run else 'fixed'} absolute paths in {fixed} files")
    return fixed


# ---------------------------------------------------------------------------
# Landing page
# ---------------------------------------------------------------------------
def regenerate_landing(dry_run: bool) -> None:
    """Regenerate the root index.html so all day cards point to index.html."""
    if dry_run:
        log("would regenerate global landing page")
        return

    skill_script = Path.home() / ".claude" / "skills" / "daily-paper-overview" / "scripts" / "generate_landing.py"
    if not skill_script.exists():
        skill_script = Path.home() / ".kimi" / "skills" / "daily-paper-overview" / "scripts" / "generate_landing.py"

    if skill_script.exists():
        # generate_landing.py writes to the parent of its arg; pass _site/arxiv-daily
        site_arxiv = SITE_DIR / "arxiv-daily"
        if site_arxiv.exists():
            import subprocess
            result = subprocess.run(
                [sys.executable, str(skill_script), str(site_arxiv)],
                capture_output=True, text=True
            )
            if result.returncode == 0:
                log("regenerated global landing page via generate_landing.py")
                return
            log(f"generate_landing.py failed: {result.stderr}; falling back to post-processing")

    # Fallback: fix only the known .md links in the copied root index.html
    root_index = SITE_DIR / "index.html"
    if root_index.exists():
        text = root_index.read_text(encoding="utf-8")
        text = re.sub(r'href="(arxiv-daily/[^"]+/)overview\.md"', r'href="\1index.html"', text)
        root_index.write_text(text, encoding="utf-8")
        log("post-processed root landing page .md links")


# ---------------------------------------------------------------------------
# Cleanup / finalize
# ---------------------------------------------------------------------------
def add_nojekyll(dry_run: bool) -> None:
    if dry_run:
        log("would add .nojekyll")
        return
    (SITE_DIR / ".nojekyll").write_text("", encoding="utf-8")


def add_readme(dry_run: bool) -> None:
    if dry_run:
        log("would add README.md")
        return
    (SITE_DIR / "README.md").write_text(
        "# Daily arXiv HTML Archive\n\n"
        "This is the GitHub Pages deploy set for the personal arXiv digest archive.\n\n"
        "- Generated by `deploy_to_ghpages.py` in the source vault.\n"
        "- Contains only static HTML — no PDFs, no pipeline code, no private config.\n"
        "- Served at `https://<user>.github.io/daily-paper-site/`.\n\n"
        "Do not edit files here directly; regenerate from the source vault and push.\n",
        encoding="utf-8",
    )


def remove_unwanted_files(dry_run: bool) -> None:
    """Ensure no PDFs, JSON manifests, or per-paper markdown files remain in _site."""
    removed = 0
    for pattern in ("*.pdf", "*.json", "*.md"):
        for p in SITE_DIR.rglob(pattern):
            if p.name == "README.md":
                continue
            if dry_run:
                removed += 1
                continue
            p.unlink()
            removed += 1
    log(f"{'would remove' if dry_run else 'removed'} {removed} unwanted files")


def report_size() -> None:
    total = 0
    count = 0
    for p in SITE_DIR.rglob("*"):
        if p.is_file():
            total += p.stat().st_size
            count += 1
    log(f"_site/ contains {count} files, {total / 1024 / 1024:.1f} MB")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main() -> None:
    ap = argparse.ArgumentParser(description="Build GitHub Pages deploy snapshot.")
    ap.add_argument("--dry-run", action="store_true", help="simulate without writing files")
    args = ap.parse_args()

    if not ARXIV_DAILY.exists():
        raise SystemExit(f"error: {ARXIV_DAILY} not found")

    if not args.dry_run:
        if SITE_DIR.exists():
            # Preserve .git so iterative deploys keep history; remove everything else.
            for p in SITE_DIR.iterdir():
                if p.name == ".git":
                    continue
                if p.is_dir():
                    shutil.rmtree(p)
                else:
                    p.unlink()
        else:
            SITE_DIR.mkdir(parents=True)

    log(f"building snapshot in {SITE_DIR}")

    copy_existing_html(args.dry_run)
    generate_missing_html(args.dry_run)
    generate_missing_daily_indices(args.dry_run)
    add_nojekyll(args.dry_run)
    add_readme(args.dry_run)
    fix_internal_links(args.dry_run)
    fix_pdf_links(args.dry_run)
    strip_version_suffixes(args.dry_run)
    fix_orphan_paper_links(args.dry_run)
    fix_absolute_paths(args.dry_run)
    regenerate_landing(args.dry_run)
    remove_unwanted_files(args.dry_run)

    if not args.dry_run:
        report_size()
        log("done. Next: cd _site && git init && git add -A && git commit -m 'initial deploy'")


if __name__ == "__main__":
    main()
