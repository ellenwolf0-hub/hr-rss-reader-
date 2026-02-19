"""
Run the full digest pipeline: RSS (step 2) → Summarizer (step 3) → Digest file (step 4).
Step 5 (Coda + link) will be added when Coda is configured.
"""

from dotenv import load_dotenv

load_dotenv()

from digest_formatter import DIGEST_PATH, write_digest
from digest_html import DIGEST_HTML_PATH, write_digest_html
from rss_reader import fetch_all_items
from summarizer import run_summarizer


def main():
    print("Step 2: Fetching RSS feeds...")
    items = fetch_all_items()
    print(f"  → {len(items)} items from the last 30 days.\n")

    if not items:
        print("No items to summarize. Exiting.")
        return

    print("Step 3: Fetching full articles and summarizing with Claude...")
    buckets = run_summarizer(items)
    total = sum(len(a) for a in buckets.values())
    print(f"  → {total} articles in {len(buckets)} buckets.\n")

    print("Step 4: Writing digest...")
    md = write_digest(buckets)
    print(f"  → Wrote {DIGEST_PATH}")
    write_digest_html(md)
    print(f"  → Wrote {DIGEST_HTML_PATH}\n")

    print("Done. Open digest.md for the recap, or digest.html in a browser for the styled view.")
    # Step 5: will print Coda doc link here when implemented


if __name__ == "__main__":
    main()
