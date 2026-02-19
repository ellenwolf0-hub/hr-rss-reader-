# Scope decisions (steps 2–5)

*Locked-in choices so we never lose them. Sourced from PROMPTS.md + PROJECT_SCOPE.md; defaults filled in where those don’t specify. Change any line when we hit it if it feels wrong.*

---

## Step 2: RSS reader

| Question | Decision |
|----------|----------|
| **Feed fetching** | `feedparser` for RSS only. Full-article fetch is step 3. |
| **Date filtering** | Use item’s **published** date. Last **30 days** (UTC). |
| **Items without dates** | **Exclude** — only include items with a valid publication date in the last 30 days. |
| **Rate limiting** | No explicit delay for RSS fetches (5 feeds, one-off). Step 3: no delay between article fetches. |
| **Raw RSS storage** | **Never write to disk.** In-memory only; list is passed straight to step 3. (PROJECT_SCOPE + PROMPTS) |
| **Errors** | If one feed fails, return items from the others and log the failure. (PROMPTS) |

---

## Step 3: Claude summarization

| Question | Decision |
|----------|----------|
| **Full-article fetch** | **requests + BeautifulSoup** — fetch HTML, parse and strip boilerplate ourselves. (A/B: B) |
| **Article fetch delay** | **No delay** — fetch as fast as we can. (A/B: B) |
| **When fetch fails** | **Skip that article** — do not include in digest. No retries (keeps runs fast). Log skip to console. (PROMPTS) |
| **Bucket assignment** | One primary bucket per article. Default 4 buckets; **Claude may add more** when content doesn’t fit (e.g. Compensation, DEI). (PROMPTS) |
| **Cap of 5 per bucket** | **5 max.** When >5, Claude picks the 5 most relevant/interesting for the audience. (PROMPTS) |
| **Order within bucket** | “Best” first — most interesting/useful first, not by date. (PROMPTS) |
| **Model** | `claude-sonnet-4-6` (already in `claude_summarizer.py`). |
| **Prompt location** | Prompts can live in code; PROMPTS.md is the reference for *what* to ask Claude, not necessarily the literal string. |

---

## Step 4: Digest output

| Question | Decision |
|----------|----------|
| **Output file** | **Same file every time:** `digest.md` in project root. (PROMPTS) |
| **Intro line** | **“Week of [date range]”** (e.g. *Week of Feb 10–17, 2026*). (A/B: B) |
| **Table of contents** | Yes — after intro, list each topic section with a link that jumps to that section. (PROMPTS) |
| **Section order** | **Variable** — not fixed; whatever order makes sense for that week. (PROMPTS) |
| **Overwrite vs append** | **Overwrite** the full file each run (one digest per run). (PROMPTS) |

---

## Step 5: Coda integration

| Question | Decision |
|----------|----------|
| **Which Coda doc** | **One fixed doc** — user provides doc ID (or we store it in `.env`). No “new doc per run.” |
| **Where in the doc** | **One page we replace each week** (or one section) so it’s idempotent — re-run doesn’t duplicate. (PROMPTS: “avoid duplicating”) |
| **Auth** | `CODA_API_TOKEN` in `.env` (same token as Coda MCP). (REFERENCE_BAUCOM_AND_CODA) |
| **When to implement** | **After** steps 2–4 work locally. (PROJECT_SCOPE: “later”) |
| **MCP vs API** | **MCP** in Cursor for one-time doc/setup; **Coda REST API from Python** for the weekly job. (REFERENCE_BAUCOM_AND_CODA) |
| **Primary output** | **Link to the Coda doc** that contains the weekly recap and all the articles. (Not just digest.md on disk.) |

---

**Learning path (GitHub backup + Spec Kit + Cursor):** see **`LEARNING_JOURNEY.md`** in the project root.

*Last updated: 2025-02-18. If something here doesn’t match what you chose, tell me and we’ll fix this file.*
