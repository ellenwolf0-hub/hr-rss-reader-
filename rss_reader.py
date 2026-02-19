"""
RSS reader for the Weekly People Team AI Digest.
Fetches the 5 curated feeds, filters to last 7 days, returns a list in memory.
No raw RSS data is written to disk.
"""

import time
from datetime import datetime, timezone, timedelta
from typing import Any, Optional

import feedparser

# Only these 5 feeds (PROJECT_SCOPE). Three original feeds were replaced (see FEEDS.md):
# - HR Brew: domain unreachable; SHRM: 404; People Managing People: 403 (bot block).
FEEDS = [
    ("Josh Bersin Blog", "https://joshbersin.com/feed"),
    ("Recruiting Brainfood", "https://recruitingbrainfood.com/feed"),
    ("HR Exchange Network (Articles)", "https://www.hrexchangenetwork.com/rss/articles"),
    ("HR Exchange Network (News)", "https://www.hrexchangenetwork.com/rss/news"),
    ("HR Exchange Network (Learning)", "https://www.hrexchangenetwork.com/rss/categories/learning"),
]


# User-Agent so feeds that block generic clients will respond (e.g. SHRM, HR Brew)
FEED_USER_AGENT = "WeeklyPeopleDigest/1.0 (HR RSS reader; +https://github.com)"


def _parse_published(entry: Any) -> Optional[datetime]:
    """Get published (or updated) datetime in UTC from a feed entry, or None if missing/invalid."""
    for attr in ("published_parsed", "updated_parsed"):
        if hasattr(entry, attr) and getattr(entry, attr):
            try:
                t = getattr(entry, attr)
                return datetime(*t[:6], tzinfo=timezone.utc)
            except (TypeError, ValueError):
                pass
    return None


def _item_in_last_7_days(published: Optional[datetime], cutoff: datetime) -> bool:
    """True if published is in the last 7 days (on or after cutoff)."""
    if published is None:
        return False
    return published >= cutoff


def fetch_all_items() -> list[dict[str, Any]]:
    """
    Fetch all 5 feeds and return a single list of items from the last 30 days
    that have a link. Does not save anything to disk.

    Returns:
        List of dicts with keys: title, link, summary, published, source.
        published is a datetime (UTC). summary may be empty string if feed has none.
    """
    now = datetime.now(timezone.utc)
    cutoff = now - timedelta(days=30)
    results: list[dict[str, Any]] = []

    for source_name, url in FEEDS:
        try:
            parsed = feedparser.parse(url, agent=FEED_USER_AGENT)
        except Exception as e:
            print(f"[RSS] Failed to fetch {source_name}: {e}")
            continue

        entries = getattr(parsed, "entries", []) or []
        if not entries:
            print(f"[RSS] No entries in feed: {source_name}")
            continue

        for entry in getattr(parsed, "entries", []) or []:
            link = (entry.get("link") or "").strip()
            if not link:
                continue

            published = _parse_published(entry)
            if not _item_in_last_7_days(published, cutoff):
                continue

            summary = ""
            if hasattr(entry, "summary") and entry.summary:
                summary = entry.summary
            elif hasattr(entry, "description") and entry.description:
                summary = entry.description

            results.append({
                "title": (entry.get("title") or "").strip(),
                "link": link,
                "summary": summary,
                "published": published,
                "source": source_name,
            })

    return results


if __name__ == "__main__":
    items = fetch_all_items()
    print(f"Found {len(items)} items from the last 30 days.")
    for i, item in enumerate(items[:5]):
        print(f"  {i + 1}. [{item['source']}] {item['title'][:60]}...")
    if len(items) > 5:
        print(f"  ... and {len(items) - 5} more.")
