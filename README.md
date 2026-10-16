# thinc-slides: a Claude skill for slides that are pictures, not text

## What it does
You give Claude your content (a run sheet, notes, an old texty deck). It plans one picture per slide, draws every slide in the Thinc. dark style, and hands you a 1920x1080 PDF. It can also put the deck into Canva with editable text, and each drawing as its own image.

- One big bold title per slide. Everything else is a drawing: objects, flows, big numbers, short labels.
- Same font (Prompt) and same sizes on every slide, so the deck looks like one person made it.
- Big enough to read over a Discord screen share.
- For big decks it splits the work: one agent per slide, all at the same time.

See `assets/example-contact.jpg` for a full 34-slide deck it made.

## What you need
Works on **Mac and Windows** (and Claude's cloud sessions).
- **Claude Code** (the terminal app or the Code tab in the Claude desktop app), so Claude has a shell. In a cloud session Claude pulls this repo itself.
- **Python 3** and **Google Chrome** (on Windows, Microsoft Edge also works: it's found automatically). If Chrome lives somewhere unusual, set `CHROME` to its full path.
- Two Python packages, once:

Mac (Terminal):
```bash
python3 -m pip install --user pillow pypdfium2
```

Windows (PowerShell):
```powershell
py -m pip install --user pillow pypdfium2
```

- For the Canva step only: the Canva connector turned on in Claude.

## Install
Mac (Terminal):
```bash
git clone https://github.com/Daranpop-s/thinc-slide-skill ~/.claude/skills/thinc-slides
```

Windows (PowerShell):
```powershell
git clone https://github.com/Daranpop-s/thinc-slide-skill "$env:USERPROFILE\.claude\skills\thinc-slides"
```

To update later: `git pull` inside that folder. Restart Claude Code. Check it worked by asking "what skills do you have?" — `thinc-slides` should be in the list.

## Commands (same on both)
Use `python3` on Mac, `py` on Windows:
```
python3 scripts/new_deck.py <deck_dir>     # new deck folder
python3 scripts/build.py <deck_dir>        # build + lint
python3 scripts/render.py <deck_dir>       # PDF + PNG pages + contact sheet
python3 scripts/to_canva.py <deck_dir>     # Canva version (asks first, see below)
```
The old `new_deck.sh` / `render.sh` still work on Mac; they just call the Python versions.

Options for `new_deck.py`:
- `--starter workshop`: step-by-step workshop deck (method in `starters/workshop/METHOD.md`, run sheet with a running clock in `out/runsheet.md`).
- `--brand michelin`: Michelin NKE internal look (private: no Canva upload).

## How to use it
Just ask. For example:
- "Make 10 Thinc slides for our onboarding from this run sheet. Make it visual, not texty."
- "These slides are too texty. Redo pages 5–20 as graphics." (attach the PDF or the notes)
- "Add a slide: dinner after the event at <restaurant> on <street>."

Claude will show you the slides as a PDF first. Tell it what to fix, the same way you would tell a designer.

## Canva
If you want the deck in Canva, Claude will ask before uploading. The upload goes to a public file host for 1 hour (anyone with the link can see it), then it deletes itself. After the import, copy the pages into your own deck and delete the imported one.

## Tips
- Give it the real facts (times, names, places). It won't invent them, and it marks anything unsure as "not decided".
- Real photos (people, news) are best added by you in Canva afterwards.
