# Weekly People Team AI Digest — Project Scope

## Constitution (how we build)

- **Prefer simple, readable code** — clarity over cleverness.
- **Prefer small functions** — do one thing per function; split when logic grows.
- **Prefer minimal dependencies** — add a library only when the benefit clearly outweighs the cost.

---

## Vision

Build a **weekly People Team AI Digest** that:

1. **Reads RSS feeds** from a curated list of HR and People team publications  
2. **Filters** for articles published in the **last 7 days**  
3. **Uses the Anthropic Claude API** to summarize and organize those articles into **4 topic buckets**:
   - Recruiting & Talent Acquisition  
   - Employee Engagement & Culture  
   - Learning & Development  
   - Workplace Experience & HR Tech  
4. **Outputs** a clean, readable digest and posts it to a **Coda doc** — so the primary deliverable is **a link to that Coda doc** with the weekly recap and all the articles. (Eventually runs automatically once a week on Mondays.)

---

## Build order (step by step)

| Step | What we're building | Status |
|------|--------------------|--------|
| **1** | Project structure + Anthropic API key connected securely | ✅ Done |
| **2** | RSS reader (fetch feeds, filter last 7 days) | Next |
| **3** | Claude summarization layer (summarize + assign to topic buckets) | Pending |
| **4** | Output: clean digest (e.g. Markdown/HTML) | Pending |
| **5** | Coda integration (post digest to Coda doc weekly on Mondays) | Later |

---

## Audience & tone

- **Who it’s for:** Superhuman’s Global People Team (scaling toward ~1,500 people).  
- **Goal:** Inspire and open curiosity — “what could AI do for me and my team?” — not intimidate or feel like a laundry list of advanced AI use cases.  
- **Relevance:** Prefer content about **larger tech companies and their HR/People teams**; articles from very small startups (e.g. 70 people) building in-house tools may be less relevant because of different scaling context.

---

## Curated RSS feeds (trusted sources — step 2)

We **only** pull from these 5 feeds (no other sources). See **FEEDS.md** for why some original feeds were replaced.

- Josh Bersin Blog: `https://joshbersin.com/feed`  
- Recruiting Brainfood: `https://recruitingbrainfood.com/feed`  
- HR Exchange Network (Articles): `https://www.hrexchangenetwork.com/rss/articles`  
- HR Exchange Network (News): `https://www.hrexchangenetwork.com/rss/news`  
- HR Exchange Network (Learning): `https://www.hrexchangenetwork.com/rss/categories/learning`  

**Step 2:** Pull every item from the 5 feeds from the **last 7 days** that has a **link**. No word-count or “full article” filter here — we send it all to step 3.  
**Step 3 (Claude summarization):** Fetch **full article text** from each link; if we can’t fetch it, **skip** that article. Summarize from full article only. One **primary bucket** per article (appears once). **Default buckets:** Recruiting & Talent Acquisition, Employee Engagement & Culture, Learning & Development, Workplace Experience & HR Tech. **Claude may add more buckets** when a theme doesn’t fit (e.g. Compensation & Benefits, DEI). We’ll identify patterns over time and can add new weekly categories as needed. **Cap: 5 articles per bucket.** When a bucket has more than 5, **Claude picks the 5** most relevant/interesting. Include small-org articles; no “small startup” note. Be **discerning on content**: prioritize **interesting, curiosity-building** pieces. **Order within each bucket:** “best” first.  
**Step 4 (digest output):** Show **source** (e.g. HR Brew, SHRM) per article. Write to **same file** each time (e.g. `digest.md`). **Table of contents** at top linking to each section. **Intro includes date generated.** **Order of sections** can change (not fixed). **Number of sections** can vary (4 default + more when Claude added buckets).

---

## How it runs & where things live

- **Schedule:** Run **automatically** on a schedule (e.g. weekly). We’ll add the actual scheduler (e.g. GitHub Actions, Cloudflare, or a small server) when you’re ready — for now we build so it runs locally on demand, then we plug in “run this every Monday” later.
- **Raw RSS data:** **Don’t save it.** Pull → pass to Claude → produce digest. No need to store the raw feed data as long as the summary is shipped to the right place.
- **Digest format (step 4):**  
  - **Not** one jam-packed paragraph.  
  - **Clear, bulleted** summaries.  
  - **Key findings** for the week.  
  - **Link to the full article** on every item so people can click through and read the whole thing.  
- **Coda:** Eventually post the digest to a Coda doc; not solving for that in the first version.
- **Code/repo:** Keep as a **local project** for now; add a GitHub repo (or similar) later. Heavier backend (Cloudflare, hosted runner, etc.) can come when you’re ready.

---

## Notes

- You're a beginner; we go step by step.  
- This file is the single source of truth for what we're building. We can update it as we go.
