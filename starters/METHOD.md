# Workshop methods (A: teach one concept and B: challenge workshop)

Format A (teach one concept). Learned from Seven's Coach by ChAMP decks (WS0 2023/2024, WS101 2025/2026, his E+R=O module).
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

---

# Format B: Challenge workshop (teams solve a real case, under time, and get assessed)

Learned from Seven's *Thinc. Support Team Recruitment Workshop* ("High-Stakes Performance Assessment"). Use it for recruitment / selection days, hackathon-style sessions, case competitions, team-building with a real output. Here the slides are the **operating screen** of the room: they state the mission, set up teams and rules, then stay up as a big phase clock.

| # | Beat | Slide pattern |
|---|---|---|
| 1 | **Title** with the stakes ("High-Stakes Performance Assessment") | divider + one small picture |
| 2 | **Mission (โจทย์ของเรา)**: one sentence; the part they usually forget highlighted ("และสื่อสารออกมาได้") | big card, one phrase in red / orange |
| 3 | **What every team must answer**: 4–5 questions per track, side by side; say they will be assessed on it | two columns of numbered questions |
| 4 | **Answer sheets**: one printable page per track, a box per question (white background, prints well) | handout page, `bg="bright"` or white card |
| 5 | **Teams**: how many teams and the role mix per team (3 ER + 2 Dreamscape + 1 PR), drawn as tables of avatars coloured by role | team-mix diagram |
| 6 | **Information you get**: people to interview (problem owner, sponsor) and documents (forms, case booklet), with arrows to the teams | sources → teams |
| 7 | **Ground rules**: allowed sources (1 AI tool per team + the documents), no phones, one pen colour per person (to see who contributed), process counts more than the answer, help other teams but own your own, "ไม่มีถูกผิด" | rule tiles |
| 8 | **How to approach this?**: phases with minutes (collect 20, analyse 20, make slides 10, present 2 min / team) | phase road |
| 9 | **Phase screens**: during each phase the same road with the current phase bright (`builds=N`), left on the projector as the room's clock | build-up of 8 |
| 10 | **Show-off!**: presentation round | divider |

Rules: everything a team needs to work without asking (mission, questions, sources, rules, time) must be on a slide they can look back at; the phase screen is always visible; assessment criteria are stated up front ("คำตอบเหล่านี้จะถูกนำไปประเมิน"); keep it warm ("Have fun!", "พี่ๆ แค่อยากรู้จักเรามากขึ้น").
