---
name: thinc-slides
description: Builds Thinc.-style slides as pictures, not text, on the dark Thinc. background. Use for any slides, deck or workshop section, or when slides are 'too texty' / 'make it visual'.
---

# Thinc. slides

## 0. Setup (do this first, every session)
The bundle (kit with fonts + backgrounds, scripts, examples) lives in Seven's private GitHub repo **Daranpop-s/Thinc-slide-skill**. Set `SK` to wherever it ends up.
1. If `~/.claude/skills/thinc-slides/scripts/build.py` exists (Seven's Mac or Windows PC; on Windows `%USERPROFILE%\.claude\skills\thinc-slides`), use it as `SK`.
2. Else if a clone already exists (e.g. `/home/claude/thinc-slide-skill/scripts/build.py`), use it as `SK`.
3. Else attach the repo (add_repo owner `Daranpop-s`, repo `Thinc-slide-skill`, access read), then `git clone --depth 1 https://github.com/Daranpop-s/thinc-slide-skill <dir>` with a generous timeout, and set `SK=<dir>`.
4. If the repo can't be reached, look for an attached `thinc-slides.zip` and unzip it into a new empty dir. Else ask Seven in one line to attach it. Don't build without the bundle.

**Works on Mac, Windows and Linux/cloud.** All scripts are Python. Use `python3` on Mac/Linux, `py` on Windows. Chrome (or Edge on Windows, or Chromium in the cloud) is found automatically; set `CHROME=<path>` only if it isn't. Needs `pillow` and `pypdfium2` (`python3 -m pip install --user pillow pypdfium2`; in the cloud add `--break-system-packages`). Running as root adds `--no-sandbox` automatically.

**Updating the skill files:** change them in the repo (commit + push), not in a temp copy, so the next session gets the fix. Keep every script cross-platform: Python only, `pathlib` paths, `.as_uri()` for file URLs, `encoding="utf-8"` on every read/write, no bash-only tools (pkill, pdftoppm, cp).

**The rule: if it's all text, people won't read it.** Every slide is ONE idea shown as a picture: real objects, shapes, flows, big numbers, short labels. Details go in what the presenter says, not on the slide.

Look at these before you start. They are the bar:
- `$SK/assets/example-contact.jpg`: a whole 34-slide workshop deck built with this skill.
- `$SK/assets/example-scene-soup.png`, `example-scene-checklist.png`: scene slides (draw the real thing, add numbered tags).
- `$SK/assets/example-buildup.png`: build-up slide (one part bright, the rest dimmed).
- `$SK/assets/header-before-after.png`: the header style to use, and the one to avoid.

## Look rules (from the deck owner's own edits in Canva)
1. **Header = one big bold title.** 68px, white, normal case, at most ~40 characters. Optional one-line plain subtitle.
   - No small orange uppercase eyebrow line, no letter-spacing, no "·" separators in the header.
   - No step-tracker dots by default (`TRACKER = 0`).
2. **Dark background on content slides** (`kit/bg-dark.jpg`). Bright `kit/bg.jpg` for covers, agenda and dividers (`bg="bright"` or `kind="divider"`).
3. **One font, one type scale.** Prompt only. Sizes come from classes, never inline (lint enforces).
4. **Readable from the back of the room / over a screen share.** Nothing under 24px. Key numbers and words 96–150px.
5. **Words are labels, not sentences.** Labels 1–4 words, sub-labels up to 6. No paragraphs, no bullet lists.
6. **Colour means the same everywhere.** Orange = us / main action. Blue = team / tech / solution. Green = good / ✓. Red = problem / ✗ / wrong way. Yellow = sticky notes / money. Pink = people. Grey = dim / not ours.
7. **Flat fills only in HTML.** No CSS gradients, box-shadow or blur (Canva turns them into square boxes).
8. **Thai stays Thai.** English startup terms stay English (MVP, pitch, sprint, user).

## Patterns that work
| Need to show | Draw this | Example body (`$SK/examples/team-matching/body/`) |
|---|---|---|
| A place, a setup, "what to bring" | **Scene**: draw the real objects; each gets one numbered tag pill, 2–4 words, in reading order | 31, 07, 06 |
| Wrong way vs right way | Two lanes; the wrong one red and crossed out with a big red ✗; the right one orange/green | 05, 13, 19 |
| Steps in order | Numbered discs or cards on a road with arrows; time under each | 03, 12, 29 |
| A loop | 3 discs on a circle with arc arrows, label in the middle | 04, 25 |
| Several phases on one slide | **Build-up**: same slide repeated, one phase bright (`builds=N`) | 18 |
| Growth, comparison | Bars with big number on top; winner in orange | 26, 27 |
| A goal or bar to hit | **Big keyword** instead of a sentence | 23, 08 |
| Gates / deadlines | Rising staircase with flags, chips on each step | 28 |
| Options to pick from | Tile grid: icon disc + name + 2-word "how" | 22 |
| Teams, roles | Avatar rows with brackets and counts | 02 |
| Section break, celebration | **Divider**: big centred words only (`kind="divider"`) | 12d, 23d |
| An emotional point | A real photo, full bleed (presenter adds it in Canva) | — |
| Where we are in the agenda | Repeat the agenda slide as a build-up | — |

## How to build
1. **Get the content first.** Read the sources. Keep the facts. Don't invent numbers, names, times or places. Mark anything unsure with a dashed `.chip.dash` ("not decided").
2. **Make a deck folder** (outside the skill folder): `python3 $SK/scripts/new_deck.py <deck_dir>` (copies kit, starter `slides.py`, `CONTRACT.md`).
3. **Plan in `slides.py`.** One dict per slide: `n`, `title`, optional `sub`, `time`, `out`, `kind`, `bg`, `builds`, and a `brief` saying exactly what to draw. See `$SK/template/slides.py` and `$SK/examples/team-matching/slides.py`.
4. **Write bodies, one file per slide: `body/NN.html`.**
   - More than ~5 slides: parallel agents, one per slide (Sonnet is fine). Prompt: "Read `<deck>/CONTRACT.md` fully and follow it. Deck folder `<deck>`, your slide `NN`. Skill folder `$SK`." plus the source files they may quote.
   - At most ~20 agents at once. Launch in waves, then list `body/` and relaunch only missing slides.
   - The coordinator owns the frame (titles, header style). Agents never touch it.
5. **Build and lint:** `python3 $SK/scripts/build.py <deck_dir>`. Fix every `LINT` line.
6. **Render:** `python3 $SK/scripts/render.py <deck_dir>` → `out/deck.pdf`, `out/p-N.png`, `out/contact.png`.
7. **Look at every slide.** Contact sheet first, then single pages. Fix overlaps, wrapped labels, arrows crossing text, text under 24px, empty corners. Re-render until clean.
8. **Deliver** the PDF (SendUserFile), and the Canva version if wanted.

## Getting it into Canva (editable)
| Route | Result |
|---|---|
| PDF → Canva import | **Broken for Thai** (vowels/tone marks split). Never for Thai slides. |
| HTML with big inline SVG | Canva drops or crops drawings. |
| **HTML with each drawing as transparent 2x PNG + real HTML text** | **Clean.** Use this. |

1. **Ask the deck owner first.** `to_canva.py` uploads drawings and page to litterbox.catbox.moe, a PUBLIC host, for 1 hour. Never for confidential/company content.
2. `python3 $SK/scripts/to_canva.py <deck_dir>` → prints a URL. Test modes: `THINC_DRYRUN=1` = local file URLs, no upload; `THINC_INLINE=1` = one self-contained `canva/deck_canva.html` with drawings embedded, no upload.
3. Canva connector: `import-design-from-url` with that URL, design type presentation.
4. Check: export the new Canva design to PDF and look at the pages (thumbnails lag).
5. Tell the owner to copy pages into the main deck, then delete the imported design.
- If a text box shows another font: select one, set Prompt, "Change all".
- Build-up dimming arrives as element transparency (~20%).
- **Cloud sessions can't reach the public host or Canva's upload server** (both blocked). The Canva step only works on Seven's own Mac/PC. In the cloud, deliver the PDF and say the Canva step needs a session on his computer.

## Rendering tips
- Fonts are local (`kit/fonts`). Google Fonts in headless Chrome can hang it.
- Print the whole deck once, then split pages; one Chrome per slide stalls.
- "render failed: no PDF" = Chrome not found or blocked; set `CHROME=<full path>`.
- Stuck Chrome: delete `<deck_dir>/.chr` and rerun (the scripts stop their own Chrome processes on every OS).
