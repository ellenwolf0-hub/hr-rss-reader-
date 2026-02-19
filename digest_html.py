"""
Generate a styled HTML version of the digest (digest.html).
Single file with embedded CSS so it works when opened locally or hosted anywhere.
"""

import re
from datetime import datetime, timezone

try:
    import markdown
    HAS_MARKDOWN = True
except ImportError:
    HAS_MARKDOWN = False

# Output alongside digest.md
DIGEST_HTML_PATH = "digest.html"


HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>Weekly People Team AI Digest</title>
  <style>
    :root {
      --bg: #faf9f7;
      --surface: #ffffff;
      --text: #1a1a1a;
      --text-muted: #5c5c5c;
      --accent: #2563eb;
      --accent-soft: #eff6ff;
      --border: #e5e5e5;
      --radius: 8px;
      --max-width: 720px;
    }
    * { box-sizing: border-box; }
    body {
      margin: 0;
      padding: 2rem 1.5rem 3rem;
      font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
      font-size: 16px;
      line-height: 1.6;
      color: var(--text);
      background: var(--bg);
      min-height: 100vh;
    }
    .wrap { max-width: var(--max-width); margin: 0 auto; }
    h1 {
      font-size: 1.75rem;
      font-weight: 700;
      margin: 0 0 0.5rem;
      letter-spacing: -0.02em;
    }
    .subtitle {
      color: var(--text-muted);
      font-size: 0.95rem;
      margin-bottom: 2rem;
    }
    h2 {
      font-size: 1.15rem;
      font-weight: 600;
      margin: 2rem 0 1rem;
      padding: 0.5rem 0;
      border-bottom: 1px solid var(--border);
      color: var(--text);
    }
    h2:first-of-type { margin-top: 1.5rem; }
    /* Table of contents */
    .toc {
      background: var(--surface);
      border: 1px solid var(--border);
      border-radius: var(--radius);
      padding: 1rem 1.25rem;
      margin-bottom: 2rem;
    }
    .toc-title { font-weight: 600; margin: 0 0 0.75rem; font-size: 0.9rem; text-transform: uppercase; letter-spacing: 0.04em; color: var(--text-muted); }
    .toc ul { list-style: none; padding: 0; margin: 0; }
    .toc li { margin: 0.35rem 0; }
    .toc a {
      color: var(--accent);
      text-decoration: none;
      font-size: 0.95rem;
    }
    .toc a:hover { text-decoration: underline; }
    /* Articles */
    .article {
      margin-bottom: 1.5rem;
      padding: 1rem 0;
      border-bottom: 1px solid var(--border);
    }
    .article:last-child { border-bottom: none; }
    .article-title {
      font-weight: 600;
      font-size: 1.05rem;
      margin: 0 0 0.35rem;
    }
    .article-title a {
      color: var(--text);
      text-decoration: none;
    }
    .article-title a:hover { color: var(--accent); text-decoration: underline; }
    .article-source {
      font-size: 0.85rem;
      color: var(--text-muted);
      font-style: italic;
      margin-bottom: 0.5rem;
    }
    .article-bullets {
      margin: 0;
      padding-left: 1.25rem;
      font-size: 0.95rem;
      color: var(--text);
    }
    .article-bullets li { margin: 0.25rem 0; }
    .content ul { padding-left: 1.25rem; margin: 0.5rem 0 1rem; }
    .content li { margin: 0.35rem 0; }
    .content a { color: var(--accent); text-decoration: none; }
    .content a:hover { text-decoration: underline; }
    .content strong { font-weight: 600; }
    .footer {
      margin-top: 2.5rem;
      padding-top: 1rem;
      border-top: 1px solid var(--border);
      font-size: 0.85rem;
      color: var(--text-muted);
    }
  </style>
</head>
<body>
  <div class="wrap">
    <h1>Weekly People Team AI Digest</h1>
    <p class="subtitle">{subtitle}</p>
    <div class="toc">
      <div class="toc-title">Table of contents</div>
      {toc_html}
    </div>
    <main class="content">
      {body_html}
    </main>
    <footer class="footer">
      Generated {generated}. Open <code>digest.md</code> for the raw Markdown.
    </footer>
  </div>
</body>
</html>
"""


def _markdown_to_html(md: str) -> str:
    """Convert Markdown to HTML. Use markdown lib if available, else minimal conversion."""
    if HAS_MARKDOWN:
        return markdown.markdown(
            md,
            extensions=["extra", "nl2br"],
            extension_configs={"extra": {"enable_attributes": False}},
        )
    return _minimal_md_to_html(md)


def _minimal_md_to_html(md: str) -> str:
    """Minimal Markdown to HTML (no extra dependency). Handles #, ##, -, links, bold."""
    out = []
    in_list = False
    for line in md.split("\n"):
        stripped = line.strip()
        if stripped.startswith("## "):
            if in_list:
                out.append("</ul>")
                in_list = False
            out.append(f"<h2>{_escape(stripped[3:])}</h2>")
        elif stripped.startswith("# "):
            if in_list:
                out.append("</ul>")
                in_list = False
            out.append(f"<h1>{_escape(stripped[2:])}</h1>")
        elif stripped.startswith("- ") or stripped.startswith("• "):
            content = stripped[2:].strip()
            if not in_list:
                out.append("<ul>")
                in_list = True
            # Inline: **bold**, [text](url), *italic*
            content = _inline_md(content)
            out.append(f"<li>{content}</li>")
        elif stripped.startswith("  ") and in_list:
            content = _inline_md(stripped.strip())
            out.append(f"<li>{content}</li>")
        else:
            if in_list:
                out.append("</ul>")
                in_list = False
            if stripped:
                out.append(f"<p>{_inline_md(stripped)}</p>")
    if in_list:
        out.append("</ul>")
    return "\n".join(out)


def _escape(s: str) -> str:
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")


def _inline_md(s: str) -> str:
    """Convert inline MD: [text](url), **bold**, *italic*."""
    s = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"\*([^*]+)\*", r"<em>\1</em>", s)
    s = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', s)
    return s


def _build_toc_from_buckets(buckets: list) -> str:
    """Build TOC list from bucket names (anchor links)."""
    lines = []
    for name in buckets:
        anchor = "#" + name.lower().replace("&", "").replace(",", "").replace(" ", "-").replace("--", "-").strip("-")
        lines.append(f'<li><a href="{anchor}">{name}</a></li>')
    return "<ul>\n" + "\n".join(lines) + "\n</ul>"


def _extract_buckets_from_md(md: str) -> list:
    """Get ## section names from digest markdown for TOC (in order)."""
    buckets = []
    for line in md.splitlines():
        line = line.strip()
        if line.startswith("## ") and line != "## Table of contents":
            buckets.append(line[3:].strip())
    return buckets


def write_digest_html(md_content: str, path: str = DIGEST_HTML_PATH) -> str:
    """
    Convert digest Markdown to a styled single-file HTML and write to path.
    Returns the HTML string.
    """
    # Pull out subtitle (first line after the title that has the date range)
    lines = md_content.strip().split("\n")
    subtitle = "Month of …"
    for line in lines:
        if "**Month of" in line or "**Week of" in line:
            # Extract the bold part
            start = line.find("**") + 2
            end = line.find("**", start)
            if end > start:
                subtitle = line[start:end]
            break

    # Build TOC from ## headers (skip "Table of contents")
    buckets = _extract_buckets_from_md(md_content)
    toc_html = _build_toc_from_buckets(buckets) if buckets else "<ul></ul>"

    # Convert full body to HTML
    body_html = _markdown_to_html(md_content)

    # Remove the first h1 from body (we have it in template) and optionally TOC heading
    # markdown wraps in <p> and headers; we use the full body and could strip first h1
    # For simplicity, leave body as-is; the template has its own h1 and we have TOC in template.
    # So we need to strip from body the title and "Table of contents" section so we don't duplicate.
    # Easier: pass only the content after TOC. Actually the cleanest is to convert the whole thing
    # and then in the template we don't repeat. Let me use a different approach: build body from
    # the same structured data. But we only have md_content here. So convert full md and replace
    # the first h1 and the first h2 (Table of contents) + its list with empty string so we don't
    # duplicate. Or: just use the converted HTML for the "main" part and in template only have
    # subtitle and toc. So body_html = full converted content. Then we're duplicating title and
    # TOC. Let me strip from body the first h1 and the TOC block (h2 "Table of contents" followed by ul).
    # Simple approach: in the template, don't output body for the intro - only output from first
    # real section. I'll do a quick strip: remove everything from start until we see "<h2" that
    # is not "Table of contents". So body = from first <h2> that is a section name.
    # Keep only the main content: drop title, subtitle, and TOC (we have those in template)
    body_html = re.sub(r"<h1>.*?</h1>\s*", "", body_html, count=1, flags=re.DOTALL)
    body_html = re.sub(r"<p>Here's your weekly.*?</p>\s*", "", body_html, count=1, flags=re.DOTALL)
    body_html = re.sub(r"<h2>Table of contents</h2>\s*<ul>.*?</ul>", "", body_html, count=1, flags=re.DOTALL)

    generated = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    html = (
        HTML_TEMPLATE.replace("{subtitle}", subtitle)
        .replace("{toc_html}", toc_html)
        .replace("{body_html}", body_html)
        .replace("{generated}", generated)
    )

    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    return html


def write_digest_html_from_md_file(md_path: str = "digest.md", html_path: str = DIGEST_HTML_PATH) -> str:
    """Read digest.md and write digest.html. Use when you only have the file."""
    with open(md_path, "r", encoding="utf-8") as f:
        md_content = f.read()
    return write_digest_html(md_content, path=html_path)
