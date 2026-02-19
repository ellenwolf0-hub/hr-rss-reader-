"""
Claude (Anthropic) integration for summarizing HR/People articles.
Loads ANTHROPIC_API_KEY from .env or environment; never hardcode the key.
"""

import os

from dotenv import load_dotenv

# Load .env from the project directory so ANTHROPIC_API_KEY is available
load_dotenv()


def get_client():
    """Return an Anthropic client using the API key from environment."""
    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        raise ValueError(
            "ANTHROPIC_API_KEY not set. Add it to a .env file or export it. See ANTHROPIC_SETUP.md."
        )
    from anthropic import Anthropic
    return Anthropic(api_key=api_key)


def summarize_article(title: str, content: str, max_tokens: int = 300) -> str:
    """
    Ask Claude to summarize an article. Uses title + content (e.g. RSS summary or excerpt).

    Args:
        title: Article title.
        content: Article summary, excerpt, or full text to summarize.
        max_tokens: Max length of the summary (default 300).

    Returns:
        Summary text from Claude.

    Raises:
        ValueError: If ANTHROPIC_API_KEY is not set.
    """
    client = get_client()
    prompt = f"""Summarize this HR/People article in 2–4 concise sentences. Focus on the main point and any actionable takeaways.

Title: {title}

Content:
{content[:12000]}

Summary:"""

    message = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=max_tokens,
        messages=[{"role": "user", "content": prompt}],
    )
    return message.content[0].text.strip()


if __name__ == "__main__":
    # Quick test: run only if API key is set
    load_dotenv()
    if not os.getenv("ANTHROPIC_API_KEY"):
        print("Set ANTHROPIC_API_KEY in .env (see ANTHROPIC_SETUP.md), then run again.")
    else:
        summary = summarize_article(
            "Example: Why Employee Feedback Matters",
            "Regular feedback improves engagement and performance. This article covers best practices for 1:1s and pulse surveys.",
        )
        print("Claude summary:", summary)
