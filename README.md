# thinc-slides: a Claude skill for slides that are pictures, not text

## What it does
You give Claude your content (a run sheet, notes, an old texty deck). It plans one picture per slide, draws every slide in the Thinc. dark style, and hands you a 1920x1080 PDF. It can also put the deck into Canva with editable text, and each drawing as its own image.

- One big bold title per slide. Everything else is a drawing: objects, flows, big numbers, short labels.
- Same font (Prompt) and same sizes on every slide, so the deck looks like one person made it.
- Big enough to read over a Discord screen share.
- For big decks it splits the work: one agent per slide, all at the same time.

See `assets/example-contact.jpg` for a full 34-slide deck it made.

## What you need
- A Mac with **Claude Code** (the terminal app or the Code tab in the Claude desktop app). It does not work in plain claude.ai chat: it needs Chrome and a shell on your Mac.
- Google Chrome in `/Applications` (used to draw the slides).
- poppler and Pillow. Run these in Terminal once:

```bash
brew install poppler
```

```bash
python3 -m pip install --user pillow
```

- For the Canva step only: the Canva connector turned on in Claude.

## Install
Put the zip in your Downloads folder, then run:

```bash
unzip ~/Downloads/thinc-slides.zip -d ~/.claude/skills/
```

Restart Claude Code. Check it worked by asking "what skills do you have?" — `thinc-slides` should be in the list.

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
