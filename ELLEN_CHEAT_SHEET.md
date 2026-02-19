# Ellen’s vibe coding cheat sheet

**What this is:** Your personal reference for the way *you* learn and the terms that work for you. Use it when you need a quick reminder, or share it so an AI (or a human) can “talk Ellen” and give you the right amount of support.

---

## How Ellen likes to learn

*(Notes for you + for anyone helping you. We’ll update this as we notice what works.)*

| What works | What to do |
|------------|------------|
| **Super prescriptive** | One small step at a time. “Do this, then this.” Not “here are five options.” |
| **“Click here” / where things live** | Say exactly where to look: “Right panel,” “New chat,” “bottom = terminal.” Visual cues > long paragraphs. |
| **Short text** | Small blocks. Tables and bullets. One checkpoint question at a time. |
| **Checkpoints** | After a step, one simple question: “Did X happen? (yes/no/not sure)” so you can confirm before moving on. |
| **Big picture first (short)** | One short “why” or “what this is” before the steps. Then the steps. |
| **Your words** | You said: “prompt a build,” “basic infrastructure,” “dumb it down,” “noob,” “vibe.” This sheet uses that kind of language. |

**Where you need more support (we’ll add as we go):**

- *(To fill in)* Things that felt confusing or needed extra prompting.
- *(To fill in)* Topics where you want more “why” or more “click here.”

**What you grok more easily (we’ll add as we go):**

- *(To fill in)* Things that clicked quickly.
- *(To fill in)* Formats that work (e.g. tables, one-step-then-checkpoint).

---

## Glossary (terms to get comfortable with)

Short, dumbed-down definitions. Use when you’re reading docs or talking to an AI. If a term isn’t here, we can add it.

**Cursor & coding**

| Term | Ellen’s version |
|------|-----------------|
| **IDE** | The app where you write and run code. For you: **Cursor**. |
| **Chat** | The right-side panel in Cursor where you talk to the AI. Same place as “agent chats.” |
| **Agent** | Mode where the AI can run commands and edit files. vs **Chat** = just conversation. |
| **Terminal** | Bottom panel in Cursor. You type text commands and press Enter. |
| **CLI** | “Command-line interface” — doing things by typing commands (e.g. in the terminal) instead of clicking. |
| **Repo** | Short for **repository**. Your project folder plus its version history. “The repo” = this project (e.g. hr-rss-reader). |
| **Dependency** | A library or package your code uses (e.g. `requests`). “Minimal dependencies” = don’t add more than you need. |

**Git & GitHub**

| Term | Ellen’s version |
|------|-----------------|
| **Git** | The tool that tracks changes and backs up your project. You use it in the terminal. |
| **GitHub** | The website where your backup lives (e.g. github.com/ellenwolf0-hub/hr-rss-reader-). |
| **Version control** | Keeping a history of changes so you can back up and (if needed) undo. Git does this. |
| **Commit** | Saving a snapshot of your project with a short message (e.g. “Added print_date script”). |
| **Push** | Sending your commits from your computer up to GitHub (backup). |
| **Pull** | Bringing changes from GitHub down to your computer (when someone else changed the repo or you’re on another machine). |
| **Remote** | The place on the internet your repo talks to — usually “origin” = your GitHub repo. |
| **Branch** | A separate line of changes. You’re on `main` by default; branches are for trying things without messing up main. |

**Spec Kit & building**

| Term | Ellen’s version |
|------|-----------------|
| **Spec** | Plain-English description of *what* you want to build (no tech details yet). |
| **Constitution** | The “rules of the road” for how we build this project (e.g. simple code, small functions). |
| **Prompt a build** | You describe what you want; the AI turns that into a plan and then into code. |
| **Infrastructure (of a build)** | The structure: spec → plan → tasks → implement. The pipeline, not the code itself. |
| **Slash command** | Something you type in chat that starts with `/` (e.g. `/speckit.constitution`). Tells the AI to do a specific kind of thing. |

---

## Spec Kit: the flow (Ellen’s vibe)

**What it is:** A way to **prompt a build** in order. You do these in sequence.

**Why we use example prompts first:** The small examples (e.g. “script that prints the current date”) are so you get comfortable with the *steps* — not so you have to decide what you really want to build yet. Learn the pipeline first; use it for something you actually want later.

| Step | Command | Ellen’s version |
|------|---------|-----------------|
| 1 | `/speckit.constitution` | “How should we build this project?” (principles, style, constraints) |
| 2 | `/speckit.specify` | “*What* do I want?” (goal in plain language; no tech yet) |
| 3 | `/speckit.plan` | “What tech / limits?” (e.g. Python, one file, no new dependencies) |
| 4 | `/speckit.tasks` | “Break it into small steps.” (AI gives you a task list) |
| 5 | `/speckit.implement` | “Do it.” (AI writes/edits the code) |

**Where to do it:** Cursor → Chat (right side) → type the command + your sentence in the box → Enter.

**You’re using:** Chat only (no CLI for now). So everything happens in that chat panel.

**What `/speckit.constitution` did for you:** The AI added your principles to (1) **PROJECT_SCOPE.md** (the “Constitution” section) and (2) **.cursor/rules/constitution.mdc** (a Cursor rule with `alwaysApply: true` so the AI uses those principles in every chat).

---

## Cursor: where things live (Ellen’s vibe)

| You want to… | Where / what to click |
|--------------|------------------------|
| Talk to the AI | **Right side** = Chat panel. (The “agent chats” are the chat.) |
| New conversation | In that panel: **New chat** or **+** at the top. |
| Have the AI run commands or edit files | Same panel: switch to **Agent** (not just Chat). |
| Open a file | **Left sidebar** = file list. Click the file. |
| Run a command (e.g. `git`, `python`) | **Bottom** = terminal. Type there, press Enter. |

---

## Cursor as your main IDE (daily use)

Use Cursor for this project every day. Quick reference:

| Goal | What to do |
|------|------------|
| **Open your project** | **File → Open Folder** → choose `hr-rss-reader`. |
| **Ask the AI** | **Right** = Chat. Type in the box at the bottom, Enter. |
| **New topic / new task** | In Chat: **New chat** or **+** so the AI isn’t confused by old context. |
| **AI edits files or runs commands** | In Chat: use **Agent** mode. |
| **Run a Python script** | **Bottom** = terminal. Example: `python3 run_digest.py` or `python3 print_date.py`. |
| **Back up to GitHub** | Terminal: `git add .` then `git commit -m "what you did"` then `git push`. |

---

## Backing up & repos

**When to back up (“big moments”)**  
Back up whenever you’d be sad to lose what you just did. For example:
- You finished a feature or a clear chunk of work
- You locked in a decision (e.g. updated SCOPE_DECISIONS.md or PROJECT_SCOPE.md)
- You’re about to try something risky or experimental
- End of your work session

**How (same every time)**  
In the **terminal** (bottom), run these three commands. Use a short message that says what you did:

```
git add .
git commit -m "Short description of what you did or decided"
git push
```

**One repo or two?**  
- **Right now:** Your learning journey (LEARNING_JOURNEY.md, ELLEN_CHEAT_SHEET.md) and the HR recap project (digest, RSS, summarizer) are in the **same repo** (hr-rss-reader). That’s fine — the learning docs are *about* this project, so one repo is OK.
- **Different repos:** Use a **separate repo per project** when it’s a different app or a different purpose. Example: “HR recap” = one repo; “personal blog” = another repo.

**How to “move between” repos**  
Each project = a **different folder** on your computer. Each folder is tied to one GitHub repo.

- To work on **this** project: **File → Open Folder** → choose `hr-rss-reader`.
- To work on **another** project: **File → Open Folder** → choose that project’s folder (e.g. `my-other-app`).
- Cursor shows one folder at a time. The terminal and chat are for whatever folder you have open. So “moving between repos” = opening a different folder.

If you later want to split the learning journey into its own repo, we can do that step by step.

---

## Quick prompts you can paste (Spec Kit)

- **Constitution:**  
  `/speckit.constitution Prefer simple, readable code and small functions. Prefer minimal dependencies.`

- **Specify (example):**  
  `/speckit.specify Add a small script that prints the current date when I run it.`

- **Plan (example):**  
  `/speckit.plan Use Python. No extra dependencies. One file is fine.`

- **Tasks:**  
  `/speckit.tasks`

- **Implement:**  
  `/speckit.implement`

---

## Living notes: what Ellen groks vs needs more

*(Update this section as we go. Short bullets are fine.)*

**Grokking so far:**

- **Step 2.2 (constitution):** Got that the AI wrote principles in two places — `PROJECT_SCOPE.md` (human-readable) and `.cursor/rules/constitution.mdc` (Cursor rule so the AI follows it in every chat). No extra prompting needed.
- **Part 2 full flow:** Ran the whole Spec Kit sequence (constitution → specify → plan → tasks → implement) with the example “date script.” AI created `print_date.py`; run it with `python3 print_date.py`.

**Needs more prompting / support:**

- *(Add when something was confusing or needed extra “click here” or “why”)*

**Ellen’s own notes:**

- *(Space for you to add anything that helps you remember or that you want an AI to know)*

---

**Where each step landed:** Constitution → `PROJECT_SCOPE.md` + `.cursor/rules/constitution.mdc`. Specify → `PROMPTS.md` (spec + plan). Implement → actual file (e.g. `print_date.py`).

*Last updated: 2025-02-19. This file is for you; we’ll keep adding to “How Ellen likes to learn” and “Living notes” as we go.*
