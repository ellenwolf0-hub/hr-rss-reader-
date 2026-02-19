# Build prompts for the Weekly People Team AI Digest

Use these prompts when building (or briefing someone to build) each step. They’re based on PROJECT_SCOPE.md.

---

## Step 2: RSS reader

**Use this prompt to build the RSS reader:**

---

Build the RSS reader for the Weekly People Team AI Digest. It should do the following.

**Inputs**

- Use **only** these 5 RSS feed URLs (no other sources). See FEEDS.md for current list.
  - Josh Bersin Blog: `https://joshbersin.com/feed`
  - Recruiting Brainfood: `https://recruitingbrainfood.com/feed`
  - HR Exchange Network (Articles): `https://www.hrexchangenetwork.com/rss/articles`
  - HR Exchange Network (News): `https://www.hrexchangenetwork.com/rss/news`
  - HR Exchange Network (Learning): `https://www.hrexchangenetwork.com/rss/categories/learning`

**Rules**

1. Fetch each feed and collect every **item** (article/post) that:
   - was **published in the last 7 days** (use the item’s publication date),
   - and has a **link** (URL to the full article).
2. Do **not** filter by word count, article length, or type (e.g. don’t exclude short blurbs or event posts here). The next step (Claude) will decide what’s worth including.
3. Do **not** save or persist the raw RSS data to disk or a database. The reader runs, produces a list in memory, and that list is passed to the next step (summarization). No storage of raw feed data.

**Output**

Produce a single list (e.g. a Python list of dicts or a JSON-serializable structure) where each item includes at least:

- `title` (string)
- `link` (string, URL to the full article)
- `summary` or `description` (string, whatever the feed provides — may be short or long)
- `published` or `published_parsed` (so we know the date)
- `source` (string, name of the feed, e.g. "HR Brew", "Josh Bersin Blog", "SHRM", "People Managing People", "Recruiting Brainfood")

This list is the only output of step 2. It will be passed as input to step 3 (Claude summarization). Handle feed errors gracefully (e.g. if one feed is down, still return items from the others and optionally log the failure).

---

## Step 3: Claude summarization layer

**Use this prompt to build the summarization layer:**

---

Build the Claude summarization layer for the Weekly People Team AI Digest. It receives the list of RSS items from step 2 and produces structured content ready for the digest.

**Input**

- A list of items from the RSS reader (step 2). Each item has at least: `title`, `link`, `summary`/`description`, `published`, `source`.
- **Before summarization:** For each item, **fetch the full article text** from the `link`. If the full article cannot be fetched (paywall, broken link, block, etc.), **skip that article** — do not include it in the digest. Only summarize from the **full article text** when we have it.

**Topic buckets**

Assign each included article to **exactly one** topic bucket (primary fit only; each article appears once in the digest).

**Default buckets** (use these when they fit):

- Recruiting & Talent Acquisition  
- Employee Engagement & Culture  
- Learning & Development  
- Workplace Experience & HR Tech  

**When content doesn’t fit the four above,** Claude may **add additional buckets** (e.g. Compensation & Benefits, DEI, Wellbeing). Over time we’ll identify patterns and can add new weekly categories as needed. The number of buckets can vary from run to run.

**Cap and selection**

- **Maximum 5 articles per bucket.** We may decrease this cap later.
- When a bucket has **more than 5** articles that pass the filters, **Claude selects the 5** that are most relevant, interesting, or useful for the audience (inspiring, curiosity-building for a People Team). The rest are dropped.
- **Order within each bucket:** “Best” first — order the 5 articles by what’s most interesting or useful for the audience (strongest hook first), not by date.

**Filter and tone**

- Exclude obvious non-articles (e.g. event announcements, job posts, pure promo).
- **Be discerning about content:** Prioritize articles that are **interesting and curiosity-building** — content that makes people want to explore AI and build themselves. That’s the main filter.
- Include articles from smaller orgs or startups; no need to add a “small startup” or org-size note. Focus on whether the content is interesting and curiosity-building, not on company size.
- Tone: **inspiring and curiosity-opening** — “what could AI do for me and my team?” — not intimidating or a laundry list of advanced use cases.

**Summarize**

- For each included article, write a short, **bulleted** summary (not one jam-packed paragraph). Include 2–4 **key findings or takeaways** that are interesting and useful for a People Team audience.
- Every summarized item must include the **link to the full article** so readers can click through and read the whole thing.

**Output**

Produce a structured object (e.g. dict or list of dicts) that the digest formatter (step 4) can use. For each included article, include: topic bucket, title, bulleted summary/key findings, link, and **source** (feed name, e.g. HR Brew, SHRM). Order articles within each bucket “best” first. The number of buckets may be 4 or more. No need to save to disk here unless we explicitly ask for it; the output is passed to step 4.

---

## Step 4: Digest output (clean, readable format)

**Use this prompt to build the digest formatter:**

---

Build the digest output step for the Weekly People Team AI Digest. It receives the summarized, bucketed content from step 3 and turns it into a clean, readable digest.

**Input**

- Structured content from step 3: articles grouped by topic bucket (there may be 4 or more buckets), each with title, bulleted summary/key findings, link to the full article, and **source** (e.g. HR Brew, SHRM).

**Requirements**

1. **Intro:** At the top, include a short intro line that includes the **date the digest was generated** (e.g. “Here’s your weekly People Team AI Digest. Generated Monday, February 18, 2026.” or “Week of Feb 10–17, 2026.”).
2. **Table of contents:** Right after the intro, add a **table of contents** that lists each topic section with a link that jumps to that section. The number of sections will vary (4 default + any additional buckets Claude added).
3. **Sections:** Use a heading for each topic bucket. The **order of sections** can change (not fixed); use whatever order makes sense for that week’s content.
4. **Per article:** Under each bucket, list articles with:
   - Article **title** (as a link to the full article)
   - **Source** (e.g. *HR Brew*, *SHRM*) so readers know where it came from
   - **Bulleted** key findings or takeaways (no single jam-packed paragraph per article)
5. **Links:** Every article must have a **clickable link** to the full article (e.g. in the title).
6. **Tone:** Keep the tone consistent: inspiring, curiosity-opening, relevant to a People Team (e.g. Superhuman scaling toward ~1,500 people). No intimidating or overly advanced framing.
7. **Output format:** Produce the digest as **Markdown**. Write it to the **same file** every time (e.g. `digest.md` in the project folder) so each run overwrites the previous digest.

**Output**

- The digest as a Markdown string, written to a single file (e.g. `digest.md`). This is the artifact we’ll eventually post to Coda in step 5; for now, the file is the deliverable.

---

## Step 5: Coda integration (later)

**Use this prompt when we’re ready to add Coda:**

---

Add Coda integration to the Weekly People Team AI Digest so the digest is **posted automatically to a Coda doc** once a week on **Mondays**.

**Input**

- The digest output from step 4 (Markdown or the structured content that generates it).

**Requirements**

1. **Destination:** Post the digest (or its formatted content) to a **Coda doc** (table or page) that the user specifies. The user will need to provide Coda API credentials and doc/table IDs (or equivalent) in a secure way (e.g. environment variables or `.env`).
2. **Schedule:** Run the full pipeline (steps 2 → 3 → 4 → 5) **on a schedule** so that the digest is generated and posted every **Monday** (or another weekday we choose). This will require a hosted runner (e.g. GitHub Actions, Cloudflare Worker, or a small server with cron). Document what’s needed so a non-expert can set it up or get help.
3. **Idempotent:** If the pipeline runs more than once in a week, avoid duplicating the same digest in Coda (e.g. by updating the same section or appending with a date check).

**Output**

- The digest appears in the designated Coda doc on the scheduled day. No change to the digest format itself; step 4 still produces the same Markdown/content.

**Note:** Step 5 is deferred until the user is ready to set up Coda and a scheduler. The codebase should be structured so that step 5 can be added without rewriting steps 2–4.

---

## Feature spec: Date script

**What I want**

- A small script I can run (e.g. from the command line).
- When I run it, it prints the current date.
- No other behavior required.

**Plan (how we build it)**

- **Language:** Python.
- **Scope:** One file only.
- **Dependencies:** No new dependencies (use only the standard library).

**Tasks**

1. Create one Python file in the project root (e.g. `print_date.py`) that is runnable from the command line.
2. In that file, use the standard library to get the current date and print it (e.g. `datetime.date.today()`).
3. Verify: running `python print_date.py` (or `python3 print_date.py`) prints the current date.
