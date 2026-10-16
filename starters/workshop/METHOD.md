# Workshop method: one hard concept, broken into bites the room can follow

Learned from Seven's Coach by ChAMP decks (WS0 2023/2024, WS101 2025/2026, his E+R=O module).
A **module** = one concept, 45–80 min, ~40–60 slides. Many slides is GOOD: each slide is one beat (~10 seconds),
so the room always knows exactly where they are. The slides do the pacing; the presenter does the talking.

## The arc of one module (in this order)

| # | Beat | What happens | Slide pattern | Time |
|---|---|---|---|---|
| 1 | **Open** | Module title + who's teaching (name, roles, one human detail) | divider, presenter card | 1 min |
| 2 | **Agenda** | The 2–3 questions this module answers ("How do we treat each event?") | agenda list, current one bright | 1 min |
| 3 | **Check-in / ice-breaker** | A tiny story with a character (e.g. น้อง Miss) told one beat per slide; the room helps the character | story beats, reveal | 3–8 min |
| 4 | **Key Question** | The character turns to the room: "เราเคยมีตอนไหนที่…?" Personal, answerable, no theory yet | big question | 10 s + think time |
| 5 | **Situation** | The presenter's own real story, built up line by line: situation → feelings / blame thoughts (red) → "ช่วยแนะนำหน่อย" → options he found (green) | story build-up, reveal | 5–10 min |
| 6 | **Name the concept** | The pattern in the story gets its name: wrong state vs right state lanes (At Effect ✗ / At Cause ✓) + one 💡 line | two lanes | 3 min |
| 7 | **Disclaimer** | What the concept is NOT (✗) and IS (✓). Stops the room from misusing it | ✗ / ✓ list | 1 min |
| 8 | **Workshop 1** | Apply to themselves, small: numbered steps with minutes each, then discuss in group | activity + timer | 10 min |
| 9 | **Half-way check point** | Recap in 1–2 lines what we know so far | check point | 1 min |
| 10 | **Formula / model** | The model built piece by piece: E ≠ O → E + R = O → focus R (the rest dimmed) | formula build | 3 min |
| 11 | **Worked example** | "ตัวอย่างใกล้ตัว (มากๆ)": a relatable, funny case filled in E → R → O; the bad R crossed out | formula slots, reveal | 3 min |
| 12 | **Let's Try** | Same frame, R = ??? ??? ???; the room answers; then **เฉลย** reveals | ??? slots → answer | 4 min |
| 13 | **Tool** | One tool that helps do it ("How to find R?" → circle of control) | one picture | 2 min |
| 14 | **Help a friend** | Back to the example: now the room fixes it → celebrate ("Good Job! Relationship Restored") | slots + divider | 4 min |
| 15 | **Workshop 2** | Apply to their own life with a template (1 E, 1 goal, 3 R, expected O) | activity + timer + worksheet | 10–12 min |
| 16 | **Final check point** | Full recap: every idea from the module in one view | check point | 1 min |
| 17 | **Key Takeaway** | 2–3 lenses: ต่อตัวเอง / ต่อคนอื่น (coachee) / ต่อการใช้งาน (coaching) | 3 cards | 2 min |
| 18 | **Bridge / check-out** | "How would you use this in …?" + one check-out question; homework if any | question | 2–5 min |

Shorter modules keep 3, 4, 6, 8 or 15, 16, 17. Never skip **Key Question**, **one workshop** and **Key Takeaway**.

## Rules that make it easy to follow
1. **One beat per slide.** If the presenter says two things, it's two slides. Build-ups (`builds=N, reveal=True`) for lines that appear one by one; `builds=N` (dim) to point at one part of a whole.
2. **Story before theory.** Character story → personal question → presenter's own story → only then the name of the concept.
3. **Concrete, close to life, a bit funny.** Examples from their world (exams, interns, partners, club work). The funny example is what they remember.
4. **The same frame repeats.** Once E + R = O is on screen, every example uses the same slots in the same place. Only the content changes.
5. **Ask, then reveal.** Show ??? first, let the room answer, then เฉลย. Never show the answer on the question slide.
6. **Wrong way first, then right way.** The wrong response / state is red and crossed out; the right one green.
7. **Check points.** Half-way and final recap slides so late joiners and drifting minds can catch up.
8. **Activities are explicit.** Every activity slide has: what to do (numbered steps), with whom (alone / pair / group of 3–6), how long per step, and a big timer. Pair rules are specific ("คนพูดเร็ว กับ คนพูดช้า", "คนละคณะ").
9. **Sharing has ground rules.** Before personal sharing: listen, respect, no judging, what's said here stays here.
10. **Timing lives in the run sheet.** Every slide gets `min`; the run sheet shows the running clock so the presenter knows if they're late.
11. **Takeaways in lenses.** Not a summary of slides: what it means for me / for the other person / for the job.
12. **Thai stays Thai, terms stay English** (At Cause, Response, Rapport, GROW). Casual "เรา" voice, emoji as icons are fine in labels (💡 ✅ ❌).

## Slide fields for workshops (on top of the normal ones)
- `min`: minutes this slide takes (feeds the run sheet clock).
- `say`: one line for the presenter: what to say or ask, what the room does.
- `reveal=True` with `builds=N`: parts appear one by one (groups after k hidden) instead of dimming.
- `time`: the chip top-right, e.g. "10 นาที" on an activity slide.
- `out`: the green OUTPUT bar: what each person / group has at the end of the activity.
