---
name: thinc-slides
description: Builds Thinc.-style presentation slides that explain with pictures, not text. Every slide is a graphic made of drawn objects, shapes, flows, big numbers and short labels on the dark Thinc. background (orange glow top-left, blue glow bottom-right, Prompt font, "Thinc." top-right), with one big bold title. Writes many slides at once with parallel agents, renders a 1920x1080 PDF, and can import the deck into Canva as editable text plus separate drawings. Use it whenever someone asks for slides, a deck, a workshop or event section, or says the slides are "too texty", "hard to read", "people won't read it", "make it visual", or "graphic not text", even if they don't name the skill.
---

# Thinc. slides

**The rule: if it's all text, people won't read it.** Every slide is ONE idea shown as a picture: real objects, shapes, flows, big numbers, short labels. Details go in what the presenter says, not on the slide.

Look at these before you start. They are the bar:
- `assets/example-contact.jpg`: a whole 34-slide workshop deck built with this skill.
- `assets/example-scene-soup.png` and `assets/example-scene-checklist.png`: scene slides (draw the real thing, add numbered tags).
- `assets/example-buildup.png`: a build-up slide (one part bright, the rest dimmed).
- `assets/header-before-after.png`: the header style to use, and the one to avoid.

## Look rules (from the deck owner's own edits in Canva)

1. **Header = one big bold title.** 68px, white, normal case, at most ~40 characters. An optional one-line plain subtitle under it.
   - No small orange uppercase "eyebrow" line above the title. No letter-spacing. No "·" separators in the header. It looks AI-made and clutters the slide.
   - No step-tracker dots by default (`TRACKER = 0`). Turn them on only if asked.
2. **Dark background on content slides** (`kit/bg-dark.jpg`, the Thinc. background at about 1/3 brightness) so the graphics pop. The bright `kit/bg.jpg` is for covers, agenda and divider slides (`bg="bright"` or `kind="divider"`).
3. **One font, one type scale.** Prompt only. Every title matches every other title, and every label matches every other label. Sizes come from classes, never inline (the lint enforces this).
4. **Big and readable from the back of the room or over a screen share.** Nothing under 24px. Key numbers and key words are 96–150px.
5. **Words are labels, not sentences.** Labels 1–4 words, sub-labels up to 6. No paragraphs, no bullet lists.
6. **Colour means the same thing everywhere.** Orange = us / main action. Blue = team / tech / solution. Green = good / ✓. Red = problem / ✗ / the wrong way. Yellow = sticky notes / money. Pink = people. Grey = dim / not ours.
7. **Flat fills only in HTML.** No CSS gradients, box-shadow or blur: Canva turns them into ugly square boxes.
8. **Thai stays Thai.** English startup terms stay English (MVP, pitch, sprint, user).

## Patterns that work

| Need to show | Draw this | Example body (`examples/team-matching/body/`) |
|---|---|---|
| A place, a setup, "what to bring" | **Scene**: draw the real objects (bowl of soup, street map, laptop with the real tool screen, phone with QR). Each object gets one numbered tag pill, 2–4 words, numbered in reading order | 31 (dinner), 07 (Discord share), 06 (seating map) |
| Wrong way vs right way | Two lanes. The wrong one is red and **crossed out with a big red ✗ across the whole lane**; the right one is orange/green | 05 (agile), 13, 19 (MVP skateboard → car) |
| Steps in order | Numbered discs or cards on a road with arrows; time under each | 03, 12 (flow), 29 |
| A loop | 3 discs on a circle with arc arrows, label in the middle | 04, 25 (build → measure → learn) |
| Several phases on one slide | **Build-up**: same slide repeated, one phase bright, the others dimmed (`builds=N`) | 18 (Ideate → Vote → MVP) |
| Growth, comparison | Bars with the big number on top; the winner in orange | 26, 27 |
| A goal or bar to hit | **Big keyword** instead of a sentence ("ยอมจ่าย", "signup", "1 วัน") | 23, 08 |
| Gates / deadlines | Rising staircase with flags, chips on each step | 28 |
| Options to pick from | Tile grid: icon disc + name + 2-word "how" | 22 |
| Teams, roles | Avatar rows with brackets and counts | 02 |
| Section break, celebration | **Divider**: big centred words only (`kind="divider"`) | 12d, 23d |
| An emotional point | A real photo, full bleed (the presenter adds it in Canva) | — |
| Where we are in the agenda | Repeat the agenda slide, current row bright, the rest dimmed (a build-up) | — |

## How to build

1. **Get the content first.** Read the sources (run sheet, brief, notes). Keep the facts. Don't invent numbers, names, times or places. Mark anything unsure with a dashed `.chip.dash` ("not decided").
2. **Make a deck folder:** `bash <skill>/scripts/new_deck.sh <deck_dir>`. It copies the kit, a starter `slides.py`, and `CONTRACT.md`.
3. **Plan the deck in `slides.py`.** One dict per slide: `n`, `title`, optional `sub`, `time`, `out`, `kind`, `bg`, `builds`, and a `brief` that says exactly what to draw (pick a pattern from the table). See `template/slides.py` for the field list and `examples/team-matching/slides.py` for 34 real rows.
4. **Write the bodies, one file per slide: `body/NN.html`.**
   - For more than ~5 slides, use parallel agents: one agent per slide, a cheaper model (Sonnet) is fine. Each agent's prompt is: "Read `<deck>/CONTRACT.md` fully and follow it. Deck folder `<deck>`, your slide `NN`." plus the source files they may quote.
   - At most ~20 agents run at once. Launch in waves, then list `body/` and relaunch only the missing slides.
   - The coordinator owns the frame (titles, header style). Agents never touch it. That is what keeps 30 slides consistent.
5. **Build and lint:** `python3 <skill>/scripts/build.py <deck_dir>`. Fix every `LINT` line.
6. **Render:** `bash <skill>/scripts/render.sh <deck_dir>` → `out/deck.pdf`, `out/p-NN.png`, `out/contact.png`.
7. **Look at every slide.** Open `out/contact.png`, then the single pages. Fix overlaps, wrapped labels, arrows crossing text, text under 24px, empty corners. Re-render until it is clean.
8. **Deliver** the PDF, and the Canva version if wanted (below).

## Getting it into Canva (editable)

| Route | Result |
|---|---|
| PDF → Canva import | **Broken for Thai.** Vowels and tone marks split off. Never use it for Thai slides. |
| HTML with big inline SVG | Canva drops or crops the drawings. |
| **HTML with each drawing as a transparent 2x PNG + real HTML text** | **Clean.** Each drawing is its own image, every word is editable text, Thai is correct. Use this. |

1. **Ask the deck owner first.** `to_canva.py` uploads the drawings and the page to litterbox.catbox.moe, a public host. Anyone with the link can open it for 1 hour, then it deletes itself.
2. `python3 <skill>/scripts/to_canva.py <deck_dir>` → prints a URL. (`THINC_DRYRUN=1` in front = local test, nothing uploaded.)
3. Canva connector: `import-design-from-url` with that URL, design type presentation.
4. Check it: Canva thumbnails are often not ready right after import, so export the new design to PDF and look at the pages.
5. Tell the owner to copy the pages into the main deck, then delete the imported design.
- The title text arrives in Prompt. If any text box shows another font: select one, set Prompt, then "Change all".
- Build-up dimming arrives as element transparency. If a dimmed part looks wrong, set its transparency in Canva (about 20%).

## Rendering tips
- Fonts are local (`kit/fonts`). Loading Google Fonts in headless Chrome can hang it.
- Print the whole deck once and split it with `pdftoppm`. One Chrome per slide stalls.
- Chrome path: set `CHROME=/path/to/chrome` if it isn't in `/Applications`.
- Stuck renders: `pkill -f "user-data-dir=<deck_dir>/.chr"`.
