# Your learning journey: GitHub backup + Spec Kit + Cursor

**You said:** You want to be told exactly what to do, one small step at a time, with clear “click here” guidance. This doc is written that way.

We’ll do three things, in order:

1. **Back up this project with GitHub** (version control)
2. **Learn GitHub’s Spec Kit** for basic assisted programming
3. **Use Cursor as your main IDE** (you’re already in it)

---

## Part 0: Cursor basics (so you know where things live)

You’re in **Cursor** — that’s your IDE (where you write and run code). A few places you’ll use a lot:

| What you want to do | Where to look / what to click |
|---------------------|--------------------------------|
| **Ask the AI a question** | **Right side:** the **Chat** panel. If you don’t see it, try **View → Chat** or the chat icon in the top-right. |
| **Start a brand‑new conversation** | In the Chat panel, look for **“New chat”** or the **+** (plus) button near the top of the chat area. Click that. |
| **Use “Agent” (AI that can run commands and edit files)** | In the chat panel, there’s usually a **model/agent switcher** (e.g. “Chat” vs “Agent”). Choose **Agent** when you want the AI to run terminal commands or edit multiple files. |
| **Open a file** | **Left sidebar** = file explorer. Click a file to open it in the main editor. |
| **Run a command in the terminal** | **Bottom panel** = terminal. If you don’t see it: **View → Terminal**. You type commands here and press Enter. |

**Quick checkpoint:**  
Can you see (1) the left sidebar with files, (2) the chat on the right, and (3) the terminal at the bottom?  
If not, say which one is missing and we’ll fix it.

---

## Part 1: Back up this project with GitHub

Goal: put your **hr-rss-reader** project on GitHub so it’s backed up and you have version history.

### Step 1.1: Do you have Git installed?

1. In Cursor, open the **terminal** (bottom panel).
2. Type exactly:  
   `git --version`  
   then press **Enter**.
3. **If you see something like** `git version 2.x.x` → Git is installed. Go to Step 1.2.  
4. **If you see** “command not found” or an error → you need to install Git first.  
   - On Mac: install Xcode Command Line Tools (run in terminal: `xcode-select --install`) or install Git from https://git-scm.com .

**Checkpoint:** What did `git --version` show? (version number or “not found”)

---

### Step 1.2: Do you have a GitHub account?

- If **yes** → go to Step 1.3.  
- If **no** → open https://github.com and click **Sign up**. Create an account, then come back here.

**Checkpoint:** Are you logged in at github.com? (yes/no)

---

### Step 1.3: Create a new repository on GitHub (empty, no files yet)

1. Go to https://github.com in your browser.
2. Click the **green “New”** button (or **“+”** in the top right → **“New repository”**).
3. **Repository name:** type `hr-rss-reader` (or another name you prefer).
4. Leave it **Public**.
5. **Do not** check “Add a README” or “Add .gitignore” — we already have a project. Leave everything unchecked.
6. Click **“Create repository”**.

You’ll see a page that says “Quick setup” and shows a URL like  
`https://github.com/YOUR_USERNAME/hr-rss-reader.git`.  
Leave that page open.

**Checkpoint:** Do you see the new empty repo and the URL? (yes/no)

---

### Step 1.4: Turn your project folder into a Git repo and push it

Do these **one at a time** in the **Cursor terminal**. Make sure you’re in the project folder (you should see something like `…/hr-rss-reader` in the terminal prompt).

| Step | Type this (replace `YOUR_USERNAME` with your GitHub username) |
|------|---------------------------------------------------------------|
| 1 | `git init` |
| 2 | `git add .` |
| 3 | `git status` (you should see a list of files to be committed) |
| 4 | `git commit -m "Initial backup of hr-rss-reader"` |
| 5 | `git branch -M main` |
| 6 | `git remote add origin https://github.com/YOUR_USERNAME/hr-rss-reader.git` |
| 7 | `git push -u origin main` |

- For **step 7**, GitHub may ask you to **log in**. Use the browser or token method they show.  
- If it asks for a **password**, use a **Personal Access Token** from GitHub (Settings → Developer settings → Personal access tokens), not your account password.

**Checkpoint:** After `git push`, do you see your files on the GitHub repo page after you refresh? (yes/no)

---

### You’re done with Part 1 when…

- You can open https://github.com/YOUR_USERNAME/hr-rss-reader and see your project files there.

**Next time you want to “back up”:**  
Run in the terminal:  
`git add .`  
`git commit -m "Short description of what you changed"`  
`git push`

---

## Part 2: Learn GitHub’s Spec Kit (basic assisted programming)

**What Spec Kit is:** A way to work with an AI assistant in a structured way: you describe **what** you want (a spec), then **plan**, then **tasks**, then the AI helps **implement**. It works inside Cursor (and other AI tools) using special **slash commands**.

### Step 2.1: Install the Specify CLI (optional but useful)

Spec Kit can be used in two ways:  
- **Only in Cursor:** use the slash commands in chat (Steps 2.2–2.5).  
- **With the CLI too:** you can run `specify init` in your project so Spec Kit is “attached” to this repo.

**If you want the CLI** (recommended later, not required for the first try):

1. You need **uv** (Python tool installer). In terminal:  
   `uv --version`  
   If that fails, install uv: https://docs.astral.sh/uv/getting-started/installation/
2. Then run:  
   `uv tool install specify-cli --from git+https://github.com/github/spec-kit.git`
3. Then in your project folder:  
   `specify init . --ai claude`  
   (or `specify init --here --ai claude`)

**Checkpoint:** Do you want to try “chat only” first, or install the CLI now? (chat only / install CLI)

---

### Step 2.2: Open a new chat and try your first Spec Kit command

1. In Cursor, open the **Chat** panel (right side).
2. Start a **New chat** (plus button or “New chat”).
3. Make sure you’re in the **Agent** mode if you want the AI to edit files or run commands.
4. In the chat box, type **exactly** (or copy‑paste):  
   `/speckit.constitution`  
   then add a short sentence, for example:  
   `/speckit.constitution Prefer simple, readable code and small functions.`

**What should happen:** The AI should recognize the Spec Kit command and help you create or update “project principles” (how this project should be built).

**Checkpoint:** After you send that message, do you get a reply that talks about “constitution” or “principles”? (yes/no / not sure)

---

### Step 2.3: Describe what you want to build (the “spec”)

In the **same** chat, try:

`/speckit.specify`  
then in the same message describe one small thing you want — for example:  
“Add a small script that prints the current date when I run it.”

Rule of thumb: say **what** you want and **why**, not the tech details. The AI will use that to propose a plan.

**Checkpoint:** Did the AI respond with a spec or a short plan? (yes/no / not sure)

---

### Step 2.4: Give your tech choices (the “plan”)

Next, try:

`/speckit.plan`  
and add something like:  
“Use Python. No extra dependencies. One file is fine.”

**Checkpoint:** Did the AI confirm the plan or suggest tasks? (yes/no / not sure)

---

### Step 2.5: Turn the plan into tasks, then implement

- Type:  
  `/speckit.tasks`  
  The AI should break the work into small steps.
- Then type:  
  `/speckit.implement`  
  The AI should actually create or change files and code.

**Checkpoint:** Did the AI create or edit a file? (yes/no / not sure)

---

### Order of Spec Kit commands (for later)

When you use Spec Kit on a real feature, use them in this order:

1. `/speckit.constitution` — how this project should be built (once per project).
2. `/speckit.specify` — what you want (user goal, not tech).
3. `/speckit.plan` — tech stack and constraints.
4. `/speckit.tasks` — break the plan into small tasks.
5. `/speckit.implement` — AI implements the tasks.

---

## Part 3: Use Cursor as your primary IDE

You’re already in Cursor. Here’s a minimal “daily use” checklist so it stays your main place to work.

| Goal | What to do in Cursor |
|------|----------------------|
| **Open your project** | File → Open Folder → choose `hr-rss-reader`. |
| **Ask the AI something** | Open Chat (right), type in the box at the bottom, press Enter. |
| **New topic / new task** | In Chat, click **New chat** (or +) so the old context doesn’t confuse the AI. |
| **Let the AI run commands or edit files** | In Chat, switch to **Agent** (or the mode that can run terminal/edit files). |
| **Run your Python scripts** | In the **terminal** (bottom): `python run_digest.py` (or whatever script you use). |
| **Back up to GitHub** | In terminal: `git add .` → `git commit -m "what you did"` → `git push`. |

**Checkpoint:** What’s one thing you’re still unsure about in Cursor? (e.g. “where is Agent?” / “how to run a file?”) — we can add a single “click here” step for that next.

---

## What to do right now (one thing)

Pick **one** and reply in chat:

- **A)** “I’ll do Part 0 checkpoints” — confirm you see sidebar, chat, terminal.
- **B)** “I’ll do Part 1” — backup to GitHub (tell me when you’re at Step 1.1, 1.2, etc.).
- **C)** “I’ll try Part 2” — first Spec Kit command in a new chat (tell me what happened after `/speckit.constitution`).
- **D)** “I’m stuck at [describe where]” — and we’ll do one small step with “click here” instructions.

I’ll keep answers short and prescriptive, and we can add more “click here” details or screenshots later if you want.
