# Michelin (NKE internal) deck. One dict per slide. build.py draws the frame from kit/frame.py:
# background, DMAIC tracker, accent bars + italic uppercase title, takeaway line, navy footer band, logo slot.
# Fields:
#   n       file key: body/<n>.html (required)
#   title   topic, written in normal case (CSS makes it uppercase), max ~30 chars (required)
#   sub     the TAKEAWAY line under the title: the point, not the topic, max ~70 chars
#   phase   DMAIC step shown red in the tracker ("Define" ... "Control"); omit = all navy
#   ask     optional bottom bar: the decision / help needed from this audience
#   kind    "cover" | "divider" | default content
#   meta    cover only: presenter, team, date
#   builds  N = N copies, group <div data-b="k"> bright on copy k, others dimmed
#   brief   what to draw (not shown)
# THE NUMBERS BELOW ARE EXAMPLE DATA for the starter deck. Real decks: only numbers from Seven's sources, else [TBC].
STEPS = ["Define", "Measure", "Analyze", "Improve", "Control"]
FOOTER = "Example project"

S = [
 dict(n="01", kind="cover", title="Project update", sub="Example project", meta="Presenter name, team, month year",
      brief="Cover. Frame only."),
 dict(n="02", kind="divider", phase="Measure", title="Measure", sub="Where does the time go?",
      brief="Divider. Frame only."),
 dict(n="03", phase="Measure", title="Value stream mapping", sub="Changeover is the longest wait in the line",
      ask="Agree changeover as the focus for Analyze",
      brief="VSM: 5 process boxes left to right (bottleneck red), inventory triangles between with wait time, lead-time ladder under, navy card right with VA % as the big number. Chip: example data."),
 dict(n="04", phase="Improve", title="Changeover time", sub="SMED pilot cut changeover by more than half",
      ask="Approve rollout to 2 more lines",
      brief="Before card (red) 45 min -> arrow -> After card (green) 20 min. Under: 3 numbered changes. Savings chip [TBC]. Chip: example data."),
]
