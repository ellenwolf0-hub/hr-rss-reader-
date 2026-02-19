# RSS feeds for the digest

We use **exactly 5 feeds**. Three of the original feeds are currently unavailable, so we use working alternatives.

## Current feeds (in code)

| Source | URL |
|--------|-----|
| Josh Bersin Blog | https://joshbersin.com/feed |
| Recruiting Brainfood | https://recruitingbrainfood.com/feed |
| HR Exchange Network (Articles) | https://www.hrexchangenetwork.com/rss/articles |
| HR Exchange Network (News) | https://www.hrexchangenetwork.com/rss/news |
| HR Exchange Network (Learning) | https://www.hrexchangenetwork.com/rss/categories/learning |

## Replaced feeds (as of Feb 2026)

| Original | Reason replaced |
|----------|-----------------|
| HR Brew (`hrbrewsletter.com/rss`) | Domain does not resolve. HR Brew may have moved or discontinued the feed. |
| SHRM (`shrm.org/rss/articles.aspx`) | Returns 404; SHRM’s RSS URLs have changed. |
| People Managing People (`peoplemanagingpeople.com/feed`) | Returns 403 (bot protection); feed cannot be fetched by script. |

If you find updated URLs for HR Brew, SHRM, or People Managing People that work, you can switch back by editing `rss_reader.py` (list `FEEDS`) and this file.
