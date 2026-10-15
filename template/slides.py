# One dict per slide. build.py draws the frame (background, "Thinc.", title, subtitle, time chip, OUTPUT bar);
# body/NN.html holds the picture. Fields:
#   n       file key: body/<n>.html            (required)
#   title   one big bold title, max ~40 chars  (required) no "·", no ALL CAPS
#   sub     optional plain subtitle, one line
#   time    optional chip top-right, e.g. "18:00–18:05 (5 นาที)"
#   out     optional green OUTPUT bar at the bottom (what each team walks away with)
#   kind    "divider" = big centred words only (section break, "we made it!"). Default = normal slide
#   bg      "bright" = the bright Thinc. background. Default = dark (graphics pop more)
#   builds  N = make N copies of the slide; copy k shows group <div data-b="k"> bright and dims the rest
#   step    step number, only shown when TRACKER > 0
#   brief   what to draw (for you or for the agent that writes this body). Not shown on the slide.
BRAND = "Thinc."
TRACKER = 0

S = [
 dict(n="01", title="เริ่มจากปัญหา ไม่ใช่ solution", time="18:00–18:05 (5 นาที)",
      out="list pain point ของโต๊ะ → เลือก 1 อันเป็น hypothesis",
      brief="Left: red ✗ card ไอเดีย → Solution, green ✓ card ปัญหา → ถาม user → Solution. Right: 6 sticky notes of example pain points."),
 dict(n="02", kind="divider", title="ถ้าเข้าใจแล้ว เรามาเริ่มกันเลย", sub="Mini Startup Workshop"),
]
