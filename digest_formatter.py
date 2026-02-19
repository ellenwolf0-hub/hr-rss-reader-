"""
Step 4: Digest output. Writes digest.md with intro (Week of ...), TOC, and sections.
"""

from datetime import datetime, timezone, timedelta
from typing import Any, Dict, List

# Output file per SCOPE_DECISIONS
DIGEST_PATH = "digest.md"


def _week_range() -> str:
    """Return 'Month of Mon YYYY' for the last 30 days."""
    now = datetime.now(timezone.utc)
    start = now - timedelta(days=30)
    return f"Month of {start.strftime('%b %d')}–{now.strftime('%b %d, %Y')}"


def _anchor(s: str) -> str:
    """Simple anchor from section title for TOC links (GitHub-style)."""
    a = s.lower().replace("&", "").replace(",", "").replace(" ", "-")
    while "--" in a:
        a = a.replace("--", "-")
    return "#" + a.strip("-")


def format_digest(buckets_with_articles: Dict[str, List[Dict[str, Any]]], week_label: str = None) -> str:
    """
    Build Markdown digest. week_label defaults to last-7-days range.
    """
    if week_label is None:
        week_label = _week_range()

    lines = [
        "# Weekly People Team AI Digest",
        "",
        f"Here’s your weekly People Team AI Digest. **{week_label}**.",
        "",
        "## Table of contents",
        "",
    ]

    for bucket in buckets_with_articles:
        anchor = _anchor(bucket)
        lines.append(f"- [{bucket}]({anchor})")
    lines.append("")

    for bucket, articles in buckets_with_articles.items():
        lines.append(f"## {bucket}")
        lines.append("")
        for a in articles:
            title = a.get("title", "")
            link = a.get("link", "")
            source = a.get("source", "")
            bullets = a.get("summary_bullets", "")
            lines.append(f"- **[{title}]({link})** — *{source}*")
            if bullets:
                for b in bullets.split("\n"):
                    b = b.strip()
                    if b:
                        lines.append(f"  {b}")
            lines.append("")
        lines.append("")

    return "\n".join(lines).strip() + "\n"


def write_digest(buckets_with_articles: Dict[str, List[Dict[str, Any]]], path: str = DIGEST_PATH) -> str:
    """Format and write digest to path. Returns the Markdown string."""
    md = format_digest(buckets_with_articles)
    with open(path, "w", encoding="utf-8") as f:
        f.write(md)
    return md
