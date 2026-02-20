# Metro Career Map — Build Log

**How we're building:** Iterate on `metro-career-map.html`. Single file, no build step. Open in browser (or Figma embed) for the Shishir pitch and working sessions.

---

## First pass (2026-02-19)

- **Required copy in place:** "Your squiggle" (draw section title), "Two very different looks. Both Expert." and "When the business wins, I win" in the Expert hover card.
- **Expert dual-pole moment:** Hovering Expert shows headline → quote → description. No "Stage" label; card is sharp and load-bearing.
- **Paths as hero:** Blobs softened (lower fill and stroke opacity) so they sit in the background; path strokes slightly bolder (3.2px, 0.92 opacity).
- **Tone:** Subtitle and hints tightened; placeholder "Hover a zone or toggle a path"; draw hint "The squiggle is the point — intentional, not broken."

---

## Second pass: X-axis + level-guide treatment (2026-02-19)

**Reference used:** [Interactive Engineering Ladders](https://interactive-engineering-ladders.pages.dev/) — clear axis treatment, bold dimension labels, defined plot area.

- **X-axis (bottom) — bolder and better described:**
  - **Strip:** Gradient band (light → slightly darker) under the axis so the horizontal dimension has visual weight.
  - **Scale:** Tick marks at 0%, 25%, 50%, 75%, 100% (longer at ends) so the axis reads as a real scale.
  - **Typography:** "Narrow" and "Broad" are 15px, font-weight 800, #111 at the ends. "Scope & complexity" as a short descriptor above the verbatim label. Full phrase "Complexity · Scope · # of Directs · Amount of Ambiguity →" is 11.5px, #333, inside the strip.
  - **Axis line:** Darker (#6B6B6B), 2px, with arrowhead so the direction is obvious.
- **Plot area:** Light border around the main canvas so the 2D space is clearly defined (level-guide style).
- **Y-axis:** Slightly bolder labels (#444, font-weight 800) and stronger tick lines (#999) so both axes feel intentional.

---

## Third pass: Level arches (2026-02-19)

- **Level arches** added as diagonal curved bands ("rainbows") per the brief. Each level (Entry, Career, Senior, Expert) is a soft, filled arch shape that sweeps diagonally across the space. **Expert** has two arches (two poles): one upper-left (narrow/deep), one upper-right (broad problem spotter).
- Arches are drawn after the grid, before the blobs; they use the same level colors with low fill-opacity and a light stroke. **Hover** on an arch highlights it and shows the same level card as hovering the blob.
- If "arches" on the whiteboard look different (e.g. semicircles, or different placement), we can adjust the path shapes.

---

## Path draw animation (Codrops / Josh Comeau style)

When a career path is toggled on, it **draws** onto the map over ~0.7s (stroke-dasharray / stroke-dashoffset), instead of appearing all at once. Toggle a path off and on again to see the animation again. Style refs: [Codrops Animated Map Path](https://tympanus.net/codrops/2015/12/16/animated-map-path-for-interactive-storytelling/), [Josh Comeau SVG Paths](https://www.joshwcomeau.com/svg/interactive-guide-to-paths/).

---

## Next (pick as needed)
- [ ] React version in same repo if we want shareable state / component reuse later.
- [ ] Any copy or blob position tweaks from Leah/Brady pressure-test.

---

*Reference: METRO_FULL_BRIEF.md, CONTEXT.md, PROJECT_SCOPE.md. Level-guide examples: CONTEXT.md → Reference examples.*
