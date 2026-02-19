# Step-by-step: Anthropic API key and Claude in this project

Follow these steps to get an Anthropic API key and use it securely for article summarization.

---

## Step 1: Create an Anthropic account (if needed)

1. Go to **https://console.anthropic.com/**
2. Sign up or log in with your email (or Google/SSO if offered)
3. Complete any verification Anthropic requires

---

## Step 2: Get your API key

1. In the Anthropic console, open **Settings** → **API Keys**, or go directly to:
   - **https://console.anthropic.com/settings/keys**
2. Click **Create key** (or **Create API key**)
3. Give the key a name (e.g. `HR RSS reader` or `Local dev`)
4. Copy the key and store it somewhere safe (e.g. a password manager)
   - **Important:** The key is often shown only once. If you lose it, create a new key and revoke the old one.

---

## Step 3: Add credits (if required)

- Anthropic may require you to add credits or set up billing before the API works.
- In the console, check **Billing** or **Usage** and add a payment method or credits if prompted.

---

## Step 4: Store the key securely in this project

**Do not** put your API key in code or commit it to git.

1. In this project folder, create a file named `.env` (no filename before the dot).
2. Add one line (replace with your real key):

   ```bash
   ANTHROPIC_API_KEY=sk-ant-your-actual-key-here
   ```

3. Save the file.
4. The file `.env` is listed in `.gitignore`, so it will **not** be committed to git. Your key stays only on your machine.

**Optional:** If you prefer to set the key in your shell instead of a file:

- **macOS/Linux (zsh/bash):**  
  `export ANTHROPIC_API_KEY="sk-ant-your-actual-key-here"`  
  Add that line to `~/.zshrc` or `~/.bashrc` if you want it in every new terminal.

---

## Step 5: Install dependencies

From the project folder (`hr-rss-reader`), run:

```bash
pip install -r requirements.txt
```

Or install the packages directly:

```bash
pip install anthropic python-dotenv
```

---

## Step 6: Verify the setup

Run the small check script:

```bash
python -c "from dotenv import load_dotenv; import os; load_dotenv(); key = os.getenv('ANTHROPIC_API_KEY'); print('Key found!' if key else 'No ANTHROPIC_API_KEY in .env or environment')"
```

If you see **Key found!**, you’re set. If not, make sure:

- `.env` is in the same directory you run the command from (or that you’re loading it from the project root), and
- The line is exactly `ANTHROPIC_API_KEY=sk-ant-...` with no spaces around `=`.

---

## Step 7: Use Claude in your code

- Use the helper in `claude_summarizer.py`: it reads `ANTHROPIC_API_KEY` from the environment (via `.env` when you call `load_dotenv()`).
- Example: call `summarize_article(title, summary_or_text)` to get a short summary from Claude.

**Security recap:**

- ✅ Key is in `.env` (or in your environment), not in source code.
- ✅ `.env` is in `.gitignore`, so it won’t be committed.
- ✅ You can share the repo; others add their own `.env` with their key.

If a key is ever exposed, revoke it in **https://console.anthropic.com/settings/keys** and create a new one.
