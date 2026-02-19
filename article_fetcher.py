"""
Fetch full article text from a URL for the digest pipeline.
Uses requests + BeautifulSoup per SCOPE_DECISIONS. No delay between requests.
"""

import re
from typing import Optional

import requests
from bs4 import BeautifulSoup

# Reasonable timeout; no retries per scope
REQUEST_TIMEOUT = 15
# Max chars to send to Claude per article
MAX_TEXT_LENGTH = 12000

# Common header so we don't get blocked as easily
HEADERS = {
    "User-Agent": "WeeklyPeopleDigest/1.0 (HR RSS reader; +https://github.com)",
}


def fetch_article_text(url: str) -> Optional[str]:
    """
    Fetch URL and extract main article text. Returns None if fetch fails
    or we can't get meaningful text.
    """
    try:
        resp = requests.get(url, headers=HEADERS, timeout=REQUEST_TIMEOUT)
        resp.raise_for_status()
    except requests.RequestException:
        return None

    soup = BeautifulSoup(resp.text, "html.parser")

    # Remove script and style
    for tag in soup(["script", "style"]):
        tag.decompose()

    # Prefer article/main, then common content containers
    body = (
        soup.find("article")
        or soup.find("main")
        or soup.find("div", class_=re.compile(r"post|article|content|entry", re.I))
        or soup.find("body")
    )
    if not body:
        body = soup

    text = body.get_text(separator="\n", strip=True)
    # Collapse multiple newlines
    text = re.sub(r"\n{3,}", "\n\n", text)
    text = text.strip()

    if len(text) < 100:
        return None

    return text[:MAX_TEXT_LENGTH] if len(text) > MAX_TEXT_LENGTH else text
