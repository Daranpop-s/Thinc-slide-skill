# Slide-body contract (give this to every agent that writes a slide)

You draw the BODY of ONE 1920×1080 slide. The coordinator tells you the deck folder (`$D`) and your slide number (`NN`).

## The rule
"If it's all text, people won't read it." Every slide is a picture: shapes, simple drawings, big numbers, short labels.
Slides may be screen-shared to each table over Discord (~720p), so everything is BIG and high-contrast.

## What you get and what you write
- Your row in `$D/slides.py` (the dict with `n="NN"`): title, sub, time, out, builds, and the **brief** = what to draw. The brief wins.
- The frame is already drawn for you: background, "Thinc.", title, subtitle, time chip, OUTPUT bar. **Don't draw any of those.**
- You write ONLY `$D/body/NN.html`: a fragment of absolutely-positioned elements (no `<html>`, `<section>`, `<style>`, `<script>`).
- Then run `python3 <skill>/scripts/build.py $D NN`. Fix every `LINT` line until there are none. Don't render with Chrome.
- Reply with one line: `NN done` (+ anything you weren't sure about).

## Body area
- x 110 to 1810.
- y 280 to 910 when the row has `out`, else 280 to 1010.
- Keep x > 1450, y < 250 empty (time chip and brand live there).

## Building blocks (classes in `kit/kit.css`)
- Text: `<div class="a l" style="left:..px;top:..px;width:..px">ข้อความ</div>`. Size ONLY by class:
  `.h` 44 bold heading, `.l` 34 main label, `.m` 30 secondary, `.q` 32 quote, `.s` 24 minor sub-label only, `.big` 96 key number or key word, `.huge` 150.
  Colour: `.or .yel .blu .grn .red .pink .grey .wht`. Align: `.c` `.r`. No wrap: `.nw`.
- Boxes: `.card` (+ `.hot` orange, `.good` green, `.bad` red, `.blue`, `.dash`), `.chip` (+ `.or .grn .blu .red .dash`), `.num` numbered disc (+ `.blu .grn .red .grey`), `.disc` circle (+ `.or .blu .grn .red .dark`). Give them `style="left;top;width;height"`.
- Inline `style` may contain ONLY: left, top, width, height, color, background (flat colour), border-color, opacity, text-align. **Never font, font-size, line-height, letter-spacing, text-transform.** No CSS gradient, box-shadow, filter (Canva turns them into square boxes).
- Drawings (objects, icons, arrows, charts, people, sticky notes): inline SVG in EXACTLY this form:
  `<svg class="a" style="left:XXXpx;top:YYYpx" width="W" height="H" viewBox="0 0 W H"> … </svg>`
  - Each SVG becomes one image in Canva. Split the slide into a few drawings (one per object), not one giant SVG and not 40 tiny ones.
  - **No Thai inside SVG.** Every word is an HTML div on top. (Latin is OK only for tiny mock-UI bits like a URL bar.)
  - Icon style: flat fills, or stroke-width 5–6 with round caps and joins.
- Later elements sit on top. Write the SVG drawings first, then the text divs.
- Build-up slide (row has `builds=N`): wrap each part in `<div data-b="1"> … </div><!--/b-->`, `data-b="2"`, … Elements outside any group stay bright on every copy.

## Colours (same meaning on every slide)
orange #FF8A3D = us / main action. Yellow #FFB547 / #FFD84D = sticky notes, money. Blue #5B9BFF = team, tech, solution.
Green #5BE49B = good, ✓. Red #FF5C5C = problem, ✗, the wrong way. Pink #FF6FB5 = people. Grey #6B7280 = dim, not ours.
Card fill #161922, border #2A2F3A. The background is dark: orange glow top-left, blue bottom-right.

## Words
- Labels 1–4 words. Sub-labels up to 6 words. **No paragraphs, no bullet lists.** One idea per slide.
- Thai stays Thai. Startup terms stay English (MVP, pitch, user, sprint).
- Wording comes from your brief and the source docs the coordinator names. Never invent facts, numbers, names, addresses or times.
- Never copy Thai text out of a Canva text read: it comes back corrupted.

## Look first
- `<skill>/assets/example-contact.jpg` (the bar), `example-scene-soup.png`, `example-scene-checklist.png`, `example-buildup.png`.
- Real bodies to borrow drawing code from: `<skill>/examples/team-matching/body/*.html`.

## Layout tips
- Fill the body area. Big shapes, generous spacing, centred composition.
- Thai with tone marks needs vertical room: text div height ≥ 1.35 × font size. Make it wide enough not to wrap, or use `.nw`.
- Text width estimate: 34px ≈ 19px per character, 30px ≈ 17px, 24px ≈ 13px.
