# Metro Career Map — Project Scope

**What this is:** The single source of truth for what we're building in the Metro Map and how. Run through Spec Kit style so the AI (and you) have clear context. Update this file when we lock in decisions.

---

## Key context: Shishir’s PSHE framework

The map is grounded in the **PSHE** career framework (Problem → Solution → How → Execution), from Shishir Mehrotra (Coda CEO, ex-YouTube CPO). Core ideas we’re encoding:

| Idea | Why it matters for the map |
|------|----------------------------|
| **Scope is the wrong metric** | Evaluating people on “how broad” their area is led to conflict and away from risky work. So the map has a separate axis for scope/complexity and one for *problem ownership* (PSHE). |
| **PSHE progression** | You start with Problem, Solution, How given — you **Execute**. Then you get Problem + Solution and figure out **How**. Then you get the Problem and devise **Solution + How**. At the top you get the space and must **find the Problem**. |
| **“The best people create clarity out of ambiguity”** | The map should make it obvious that growth isn’t “more scope” — it’s moving up the ownership axis and handling more ambiguity. |
| **Multiple valid paths** | Like the Lane Shackleton story (sales → PM, redefining the problem): the map shows different career shapes — ladder, execution machine, PSHE climber, squiggler — so people see more than one way to “level up.” |

**Source:** [This Framework Will Change How You Think about Your Career \| Shishir Mehrotra (Coda)](https://creatoreconomy.so/p/the-best-framework-for-career-growth-shishir) — Creator Economy / Behind the Craft.

---

## Constitution (how we build)

Same as the repo. When writing or changing Metro Map code:

- **Simple, readable code** — clarity over cleverness.
- **Small functions** — one clear responsibility per function.
- **Minimal dependencies** — no build step; single HTML + inline SVG + vanilla JS is preferred so it “just opens in a browser.”

---

## Vision (what this is for)

An **interactive career visualization** for **Project Metro** (talent transformation at Grammarly/Superhuman): shift from promotion-focused to impact-focused — *“When the business wins, I win.”*

The map shows that careers aren’t ladders; they’re multidirectional journeys in a 2D space. It should work in two modes:

- **Executive pitch** — Clear enough for Shishir (and others) to see the Metro concept in one view.
- **1:1 coaching** — Someone can hover a zone, toggle a path, or draw their own squiggle and immediately get that their career doesn’t have to go in a straight line.

---

## Spec (what we’re building — plain language)

1. **Two axes**
   - **Y (bottom → top):** Problem ownership (PSHE) — Execution → How to Do → Solution → Problem.
   - **X (left → right):** Complexity · Scope · # of Directs · Amount of Ambiguity (narrow → broad).

2. **Career level zones (“rainbows”)**
   - Soft, overlapping blobs (Entry, Career, Senior, Expert) that sit diagonally in the space. Not rigid boxes; they overlap. Expert has two poles: narrow-but-deep craft master and broad problem-spotter.

3. **Four career path lines**
   - Classic Ladder, Execution Machine, PSHE Climber, The Squiggler — each a distinct *shape* through the space (from Leah’s whiteboard).

4. **Interactivity**
   - Toggle each path on/off; “Show all” to overlay all paths.
   - Hover a level blob → highlight it and show a short description card.
   - “Draw your own” mode: user draws a squiggle on the map (smooth line); Clear resets it.

5. **Vibe**
   - **Sharp, impressive, not soft.** Thoughtful product team, not People slide. Soft blobs are **background context**; the **four paths are the visual hero** — dynamic, alive, clickable. Fits in a meeting and lands the philosophical shift.

---

## Plan (tech / constraints)

| Choice | Decision |
|--------|----------|
| **Format** | Single **HTML file** that opens in a browser. No React build, no npm. |
| **Visualization** | **SVG** (paths, ellipses, gradients). Scales cleanly; mouse events for drawing are straightforward. |
| **Drawing** | Track mouse on SVG; convert to normalized 0–1 coordinates; smooth with cubic bezier. |
| **Dependencies** | None. Inline CSS and JS. |
| **Where it lives** | `metro-map/metro-career-map.html` in this repo. |

---

## Done looks like

- Opens in a browser and looks polished.
- Both axes labeled; four soft overlapping level blobs; four toggleable path lines; “Draw your own” + Clear.
- Works on a laptop without scrolling.
- Usable in an exec meeting and in a 1:1.

---

## Reference

- **Full brief (canonical):** **`metro-map/METRO_FULL_BRIEF.md`** — Project Metro reframe, two axes, four paths, two Expert poles, tool description, tone, required copy, use cases, tech. Single source of truth.
- **Rich context (Q&A):** **`metro-map/CONTEXT.md`** — primary user, success, banned words, required quotes, emotional job. Use for every product/copy decision.
- **Brief:** `Ellen's Vault/metro-map-cursor-brief.md` (original whiteboard spec, paths, copy).
- **Reference code:** `Ellen's Vault/metro-career-map.jsx` (data and coordinate system).
- **Shishir/PSHE:** [Creator Economy — Shishir Mehrotra](https://creatoreconomy.so/p/the-best-framework-for-career-growth-shishir).

*Spec Kit pass: Constitution (inherited) · Specify (above) · Plan (above). Tasks and implement = iterate on `metro-career-map.html`.*
