# Reference: Baucom Report + Coda setup

## Baucom Report (reference build)

**What it is:** A similar weekly digest / trend report built by your friend. It aggregates podcasts and Substacks, processes them with AI, and produces a “Weekly Trend Analysis” with trending topics and a comprehensive analysis.

**Tech stack (for reference):**
- **Frontend:** React 19, TanStack Router (file-based), TanStack React Start, Tailwind CSS 4  
- **Database:** Cloudflare D1 (SQLite) via Drizzle ORM  
- **Storage:** Cloudflare R2 (audio)  
- **AI:** Whisper (transcription), GLM-4.7-flash (episode analysis + weekly trend reports, 131k context)

**UI highlights (from screenshots):**
- **Admin panel:** Add podcasts (RSS) and Substacks, “Poll All Feeds,” “Weekly Analysis” button, “Force Refresh,” “Cancel All Jobs.” Tracked feeds with per-episode status (pending/complete) and “Process” per episode.
- **Home / dashboard:** Tracked Podcasts (cards with episode counts, latest episode), Tracked Substacks (same idea). Then **Weekly Trend Analysis** with date range (e.g. 2/9–2/16), **“Trending Topics”** as pill-shaped tags (dynamic categories), **“Comprehensive Trend Analysis”** text, and a **“Generate New”** button.

**What we’re borrowing for our digest:** Weekly summary with a clear date range, dynamic/trending topics (we allow variable buckets), one “run” that produces the analysis. We’re not building the full React app, D1, or R2; we’re building a pipeline (RSS → Claude → digest) that outputs to a file and then to Coda (and later Slack).

---

## Coda: two ways to connect

### 1. Coda MCP (for Cursor)

**What it is:** A Model Context Protocol server that lets an AI assistant in Cursor talk to Coda (list docs, create pages, read/append/replace page content, etc.).

**Yes, you can hook up Cursor to the Coda MCP with an API token.**

- **Repo:** [orellazri/coda-mcp](https://github.com/orellazri/coda-mcp)  
- **Capabilities:** List docs/pages, create pages with markdown, read/replace/append page content, duplicate/rename pages, resolve Coda links.  
- **Setup:** Add the MCP server to Cursor’s MCP settings and set your Coda API key in the `env` block.

**Example MCP config (in Cursor):**

```json
{
  "mcpServers": {
    "coda": {
      "command": "npx",
      "args": ["-y", "coda-mcp@latest"],
      "env": {
        "API_KEY": "your-coda-api-token-here"
      }
    }
  }
}
```

**Getting a Coda API token:** In Coda, go to Account/Settings and create an API token. Keep it secret (e.g. in env only, not in code).

**When to use the MCP:** Creating or editing a Coda doc from inside Cursor (e.g. “create a doc for the digest” or “add a page with this structure”). The agent in Cursor needs to have the Coda MCP enabled in that chat/session.

**Note:** In this project we haven’t enabled the Coda MCP in the current Cursor workspace. So right now we’re using the **Coda API from Python** for the weekly automation. You can still add the Coda MCP to Cursor for ad‑hoc doc setup, then use the script (below) for the weekly run.

---

### 2. Coda API from Python (for weekly automation)

**What it is:** Your Python script calls Coda’s REST API (with the same API token) to create or update a doc/page and push the digest content. No MCP needed when the script runs (e.g. on a schedule).

**Why we use this for the digest:** The pipeline (steps 2 → 3 → 4) runs as a single script. Step 5 will do something like: “take `digest.md` (or the structured content), then POST/PATCH to Coda so the weekly summary appears in the right doc or table.” That’s easiest with the Coda API and a token in `.env` (e.g. `CODA_API_TOKEN`).

**Coda API basics:**  
- Base URL: `https://coda.io/apis/v1`  
- Auth: Bearer token (your API token).  
- You can create docs, create pages in a doc, insert/update rows in tables, and update page content (depending on endpoints). We’ll use the endpoints that fit “append or replace the weekly digest in this doc.”

So:
- **Cursor + Coda MCP + API token:** For creating/editing the Coda doc from Cursor (optional, one-time or ad‑hoc).  
- **Python + Coda API + same API token in `.env`:** For the actual weekly automation that posts the digest into that doc.

Both use the same Coda API token; one goes through the MCP in Cursor, the other through HTTP from your script.
