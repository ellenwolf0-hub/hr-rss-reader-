# Project Metro — Full Brief for Cursor

*Paste/source of truth. Use this for product, copy, and tech decisions.*

---

Project Metro is Grammarly's internal career framework redesign. It touches levels, titles, compensation philosophy, and promotions — but the real work is a **philosophical reframe**: moving away from a ladder metaphor (linear, hierarchical, one "right" path) toward a **2D space** where career growth is about **expanding the kind of problems you own**, not just climbing a fixed structure.

The framework is built around **two axes**. The **Y-axis** represents the type of work someone owns: at the bottom is **Execution** (you know exactly what to do and you do it well), then **How to Do** (you figure out the method), then **Solution** (you identify the right answer), then **Problem** (you define what we should even be solving). The **X-axis** represents scope and complexity: number of directs, amount of ambiguity, complexity of the work, breadth of impact. Movement along either axis — or both — represents growth.

There are **four archetypal career path shapes** that Leah drew on a whiteboard during a working session:

1. **Classic Ladder** — A diagonal staircase from bottom-left to top-right, moving up in both problem ownership and scope over time.
2. **Execution Machine** — Someone who extends far right on scope and scale while staying in the Execution/How to Do zone, then pivots sharply upward — high-impact but operationally oriented.
3. **PSHE Climber** — Moves nearly vertically; narrow scope but rapidly climbing into Problem ownership, the "brilliant but focused" archetype.
4. **Squiggler** — A looping, backtracking, nonlinear path that represents how most real careers actually look. The goal is for this to feel **intentional and interesting, not broken**.

The framework defines **two "Expert" poles** — both are valid endpoints, both are labeled Expert, but they look completely different. One Expert is the **execution master** who has scaled operationally and owns enormous scope. The other Expert is the **problem identifier** who lives in the Problem row and shapes what the company works on. The key unlock is that these two people look nothing alike, and the old framework would have evaluated them by the same rubric. **Metro says: both are legitimate.** That's the philosophical shift.

---

## The tool we're building

An **interactive SVG visualization** of this 2D career space.

- **Visual hero:** The **four paths** — dynamic, alive, clickable. Behind them, **soft, tilted ellipse blobs** for the level zones are **background context, not the main event**.
- **Interactions:** Toggle paths on and off, hover to learn about each archetype, **draw your own squiggle** on the canvas.
- **Emotional job:** Make ambiguity feel like **possibility**. Someone should see the Squiggler path and feel **relief, not shame**. The **Expert dual-poles moment** is the most important interaction: seeing two totally different-looking paths both arrive at "Expert" is the **aha moment** the team needs to land with leadership.

**Exact axis labels (verbatim, non-negotiable):**
- **Y-axis (bottom → top):** Execution, How to Do, Solution, Problem.
- **X-axis footer:** `Complexity · Scope · # of Directs · Amount of Ambiguity →`

These are part of the vocabulary shift Metro is trying to install.

---

## Tone and design direction

**Sharp, impressive, not soft.** This is not a wellness tool or a reflection exercise. It should feel like something a **thoughtful product team** built, not a People team slide.

- No Radford language, no band/level jargon, no checklist energy.
- **UI copy that must appear:**
  - **"Your squiggle"** — possessive, humanizing.
  - **"Two very different looks. Both Expert."** — the dual-pole headline.
  - **"When the business wins, I win"** — Expert orientation framing, not a loyalty statement.

---

## Use cases

1. **Immediate:** Pitch to **Shishir (Grammarly's CEO)**. Leah needs to show that the People team hasn't just understood this framework intellectually — **they've built on it**. The tool is the **proof of concept**. If it lands, it validates the whole Metro reframe.
2. **Secondary:** Individual ICs using it to map their own path and start better career conversations with their managers.

---

## Tech stack (target)

- **React + SVG.** All path coordinates in **normalized 0–1 space**, converted to pixel space at render time (resolution-flexible). **Cubic bezier** interpolation for organic-feeling lines. **Mouse events on the SVG** for freehand drawing. State in React (`useState`), no external dependencies beyond React.

*Note: Current deliverable is a single HTML file (no build) for maximum portability and "open in meeting" use. A React version can be added later if needed.*

---

*Added 2026-02-19. Source: Ellen + Sonnet 4.6.*
