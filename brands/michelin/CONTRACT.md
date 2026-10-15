# Slide-body contract: Michelin (NKE internal)

You draw the BODY of ONE 1920×1080 slide for an internal Michelin Nong Khae deck. The coordinator tells you the deck folder (`$D`) and your slide number (`NN`).

## The rule
Plant managers decide fast. One idea per slide, shown as a picture: process boxes, flows, before/after, bars, big numbers, short labels. If it's all text, nobody reads it.

## What you get and what you write
- Your row in `$D/slides.py` (the dict with `n="NN"`): title, sub (= the takeaway), phase, ask, builds, and the **brief** = what to draw. The brief wins.
- The frame is already drawn: background, DMAIC tracker, accent bars + title, takeaway line, ASK bar, navy footer band, logo. **Don't draw any of those.**
- You write ONLY `$D/body/NN.html`: absolutely-positioned elements (no `<html>`, `<section>`, `<style>`, `<script>`).
- Run `python3 <skill>/scripts/build.py $D NN` (Windows: `py`). Fix every `LINT` line. Don't render with Chrome.
- Reply with one line: `NN done` (+ anything you weren't sure about).

## Body area
- x 110 to 1810.
- y 290 to 870 when the row has `ask`, else 290 to 970.
- Nothing over the tracker (y < 110), the title block (y < 280) or the footer (y > 1000).

## Facts
- **Never invent a number, saving, date, owner or machine name.** Use only the brief and the source files named by the coordinator. Missing = `<div class="chip tbc" ...>[TBC]</div>`.
- Units the plant feels: THB / year, min / shift, % scrap, OEE %, pcs / h. Always with a comparison: before → after, actual vs target.

## Building blocks (classes in `kit/kit.css`)
- Text: `<div class="a l" style="left:..px;top:..px;width:..px">Label</div>`. Size ONLY by class:
  `.h` 44 heading, `.l` 34 main label, `.m` 30 secondary, `.q` 32 quote, `.s` 24 minor sub-label, `.big` 96 key number, `.huge` 150.
  Colour: `.blu .nav .red .grn .grey .wht`, `.yel` only on navy. Default text is navy. Align `.c` `.r`. No wrap `.nw`.
- Boxes: `.card` (+ `.blue`, `.bad`, `.good`, `.navy`, `.dash`, `.edge` = thick left edge, combine `.edge.bad`), `.chip` (+ `.blu .nav .red .grn .yel .dash .tbc`), `.num` numbered disc (+ `.red .grn .nav .grey`), `.disc` (+ `.blu .red .grn .nav .light`). Give them `style="left;top;width;height"`.
- Inline `style` may contain ONLY: left, top, width, height, color, background (flat colour), border-color, opacity, text-align. **Never font, font-size, line-height, letter-spacing, text-transform.** No CSS gradient, box-shadow, filter.
- Drawings (process icons, arrows, charts, triangles, ladders): inline SVG in EXACTLY this form:
  `<svg class="a" style="left:XXXpx;top:YYYpx" width="W" height="H" viewBox="0 0 W H"> … </svg>`
  - **No words inside SVG.** Every label and number is an HTML div on top.
  - Style: flat fills, stroke 4–6 with round joins, corners radius ≤ 10. Corporate and clean: no cartoons, no sticky notes.
  - **Never draw the Michelin logo, the Bibendum, or any brand mark.** The logo comes from the frame.
- Write SVG drawings first, then text divs (later elements sit on top).
- Build-up slide (`builds=N`): wrap each part in `<div data-b="1"> … </div><!--/b-->`, `data-b="2"`, …

## Colours (same meaning on every slide)
Blue #27509B = ours, the main series, the solution. Navy #153663 = structure, text, neutral boxes.
Red #BE5350 = problem, before, the bottleneck, gap to target. Green #2E9E5B = after, on target, done.
Yellow #FCE500 = inventory triangles, one highlight on navy. Grey #6B7785 = baseline, not ours, minor.
Card fill white or #EAF1FA, border #C9D8E6. Background is light.

## Patterns
- **VSM:** process boxes in a row (bottleneck `.card.bad.edge`), yellow inventory triangles between with wait time under, lead-time ladder below (wait up, work down), value-add % as the big number in a navy card.
- **Before / after:** two cards `.bad.edge` → `.good.edge`, big numbers inside, arrow between, what changed as 3 numbered labels under.
- **KPI tiles:** metric name, actual `.big`, target `.s`, status chip red/green.
- **Pareto:** bars sorted high→low (top causes red, rest grey), cumulative line navy, values as divs above bars.
- **Fishbone (6M):** navy spine to a red head box; 6 ribs; the verified cause highlighted red.
- **Timeline:** done (green discs), now (red), next (grey) on one line with dates under.
- **Action plan:** max 6 rows of card strips: action, owner chip, date chip, status chip.

## Words
- Labels 1–4 words, sub-labels up to 6. No paragraphs, no bullet lists.
- English for management by default; Thai labels when the audience is operators (Thai stays Thai). Lean terms stay English (VSM, SMED, OEE, C/O, CT).

## Layout tips
- Fill the body area; generous spacing; align to a grid.
- Text div height ≥ 1.35 × font size; wide enough not to wrap, or `.nw`.
- Width estimate: 34px ≈ 19px per character, 30px ≈ 17px, 24px ≈ 13px.
- Look at `$D/body/03.html` and `04.html` in a fresh deck for working examples.
