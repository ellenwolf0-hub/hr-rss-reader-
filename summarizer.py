"""
Step 3: Claude summarization layer.
Fetches full article text, assigns bucket, produces bullet summary. Cap 5 per bucket.
"""

import json
import re
from collections import defaultdict
from typing import Any, Dict, List, Optional

from dotenv import load_dotenv

load_dotenv()

from article_fetcher import fetch_article_text
from claude_summarizer import get_client

# Default buckets (PROMPTS.md); Claude may add more
DEFAULT_BUCKETS = [
    "Recruiting & Talent Acquisition",
    "Employee Engagement & Culture",
    "Learning & Development",
    "Workplace Experience & HR Tech",
]

CAP_PER_BUCKET = 5


def _analyze_article(client: Any, title: str, source: str, full_text: str, link: str) -> Optional[Dict[str, Any]]:
    """
    One Claude call per article: assign bucket, decide include, return bullet summary.
    Returns None if we should exclude this article.
    """
    buckets_list = ", ".join(DEFAULT_BUCKETS)
    prompt = f"""You are helping build a weekly HR/People Team AI Digest. For this article, do the following.

1. Assign it to exactly ONE topic bucket. Use one of these when it fits: {buckets_list}. If the content doesn't fit any of these, you may add a new bucket name (e.g. "Compensation & Benefits", "DEI", "Wellbeing").
2. INCLUDE any article that is clearly about HR, People, workplace, leadership, recruiting, culture, L&D, DEI, or similar. Set include: false ONLY for: job postings, event-only announcements (e.g. "Register for our webinar"), or pure advertising. When in doubt, include it.
3. If including, write 2-4 bullet points (key findings or takeaways) for a People Team audience. Be concise.

Respond with a single JSON object, no other text:
{{"bucket": "<bucket name>", "include": true or false, "summary_bullets": "<bullet points as a single string, use • for bullets>"}}

If include is false, set summary_bullets to "".

Article title: {title}
Source: {source}
Link: {link}

Article text:
{full_text[:11000]}
"""

    try:
        message = client.messages.create(
            model="claude-sonnet-4-6",
            max_tokens=500,
            messages=[{"role": "user", "content": prompt}],
        )
        text = message.content[0].text.strip()
    except Exception as e:
        print(f"[Summarizer] Claude error for '{title[:50]}...': {e}")
        return None

    # Extract JSON: try code block first, then find first { and matching }
    data = None
    for block in re.finditer(r"```(?:json)?\s*(\{.*?\})\s*```", text, re.DOTALL):
        try:
            data = json.loads(block.group(1))
            break
        except json.JSONDecodeError:
            continue
    if data is None:
        start = text.find("{")
        if start >= 0:
            depth = 0
            for i, c in enumerate(text[start:], start):
                if c == "{":
                    depth += 1
                elif c == "}":
                    depth -= 1
                    if depth == 0:
                        try:
                            data = json.loads(text[start : i + 1])
                        except json.JSONDecodeError:
                            pass
                        break
    if data is None:
        try:
            data = json.loads(text)
        except json.JSONDecodeError:
            print(f"[Summarizer] Could not parse Claude response for '{title[:50]}...'")
            return None

    if not data.get("include"):
        return None

    bucket = (data.get("bucket") or "").strip()
    if not bucket:
        return None

    bullets = (data.get("summary_bullets") or "").strip()
    return {
        "bucket": bucket,
        "title": title,
        "link": link,
        "source": source,
        "summary_bullets": bullets,
    }


def _select_best_five(client: Any, bucket_name: str, articles: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """When a bucket has more than 5 articles, Claude picks the best 5 and orders them (best first)."""
    if len(articles) <= CAP_PER_BUCKET:
        return articles

    # Build a numbered list for Claude
    lines = []
    for i, a in enumerate(articles, 1):
        lines.append(f"{i}. {a['title']} ({a['source']})\n   {a['summary_bullets'][:200]}...")
    listing = "\n".join(lines)

    prompt = f"""From the following list of articles in the bucket "{bucket_name}", pick the 5 that are most relevant, interesting, and useful for a People Team audience (inspiring, curiosity-building). Return them in order: best first.

List (respond with only the numbers in order, comma-separated, e.g. 3, 7, 1, 4, 9):

{listing}
"""

    try:
        message = client.messages.create(
            model="claude-sonnet-4-6",
            max_tokens=100,
            messages=[{"role": "user", "content": prompt}],
        )
        text = message.content[0].text.strip()
    except Exception as e:
        print(f"[Summarizer] Claude select-best-five error: {e}")
        return articles[:CAP_PER_BUCKET]

    # Parse "3, 7, 1, 4, 9" or "3,7,1,4,9"
    indices = []
    for part in re.split(r"[\s,]+", text):
        part = part.strip().strip(".")
        if part.isdigit():
            idx = int(part)
            if 1 <= idx <= len(articles) and idx not in indices:
                indices.append(idx)
        if len(indices) >= CAP_PER_BUCKET:
            break

    if len(indices) < CAP_PER_BUCKET:
        # Fallback: take first 5
        return articles[:CAP_PER_BUCKET]
    return [articles[i - 1] for i in indices]


def run_summarizer(rss_items: List[Dict[str, Any]]) -> Dict[str, List[Dict[str, Any]]]:
    """
    Takes the list from the RSS reader (step 2). Fetches full article for each,
    asks Claude for bucket + summary, caps at 5 per bucket. Returns structure
    for step 4: { "Bucket Name": [ { title, link, source, summary_bullets }, ... ], ... }
    """
    client = get_client()
    by_bucket: Dict[str, List[Dict[str, Any]]] = defaultdict(list)

    for i, item in enumerate(rss_items):
        title = item.get("title") or ""
        link = item.get("link") or ""
        source = item.get("source") or ""
        if not link:
            continue

        print(f"[Summarizer] Fetching ({i+1}/{len(rss_items)}): {title[:50]}...")
        full_text = fetch_article_text(link)
        if not full_text:
            print(f"[Summarizer] Skip (could not fetch): {link[:60]}...")
            continue

        result = _analyze_article(client, title, source, full_text, link)
        if result:
            by_bucket[result["bucket"]].append(result)
        else:
            print(f"[Summarizer] Skip (excluded by Claude or parse error): {title[:55]}...")

    # Cap each bucket at 5, best first
    out: Dict[str, List[Dict[str, Any]]] = {}
    for bucket_name, articles in by_bucket.items():
        if len(articles) > CAP_PER_BUCKET:
            articles = _select_best_five(client, bucket_name, articles)
        out[bucket_name] = articles

    return out
