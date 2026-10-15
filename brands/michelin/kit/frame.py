"""Michelin (NKE internal) frame, loaded by scripts/build.py when <deck>/kit/frame.py exists.

slides.py fields used here (on top of n, title, sub, kind, builds, brief):
  phase   "Define" | "Measure" | ... : the DMAIC step shown red in the tracker (any name in STEPS)
  ask     optional bar at the bottom: the decision / help needed (replaces Thinc's OUTPUT bar)
  meta    cover only: presenter, team, date
Deck-level (optional) in slides.py:
  STEPS  = ["Define", "Measure", "Analyze", "Improve", "Control"]   tracker labels; [] = no tracker
  FOOTER = "..."    left text in the navy footer band (e.g. the project name)
kind: "cover" | "divider" | default content slide.
Logo: if <deck>/kit/brand/logo.png exists it is placed top-right. Only Seven's official file; never drawn.
"""
import html, pathlib
E = html.escape
KIT = pathlib.Path(__file__).resolve().parent
LOGO = (KIT / "brand" / "logo.png").exists()
DEFAULT_STEPS = ["Define", "Measure", "Analyze", "Improve", "Control"]

def section_class(r):
    return "dark" if r.get("kind") in ("cover", "divider") else ""

def tracker(r, steps, big=False):
    if not steps: return ""
    cells = "".join(f'<b class="on">{E(s)}</b>' if s == r.get("phase") else f"<b>{E(s)}</b>" for s in steps)
    return f'<div class="dmaic{" big" if big else ""}">{cells}</div>'

def frame(r, mod):
    steps = getattr(mod, "STEPS", DEFAULT_STEPS)
    kind = r.get("kind")
    f = [f'<img class="bg" src="kit/{"bg-navy.jpg" if kind in ("cover", "divider") else "bg-light.jpg"}">']
    if LOGO: f.append('<img class="logo" src="kit/brand/logo.png">')
    if kind == "cover":
        f.append(f'<div class="ctitle">{E(r["title"])}</div>')
        if r.get("sub"): f.append(f'<div class="csub">{E(r["sub"])}</div>')
        f.append('<div class="cline"></div>')
        if r.get("meta"): f.append(f'<div class="cmeta">{E(r["meta"])}</div>')
        return f
    if kind == "divider":
        if r.get("phase"): f.append(tracker(r, steps, big=True))
        f.append(f'<div class="dtitle">{E(r["title"])}</div>')
        if r.get("sub"): f.append(f'<div class="dsub">{E(r["sub"])}</div>')
        return f
    f.append(tracker(r, steps))
    f += ['<div class="bar1"></div>', '<div class="bar2"></div>', f'<div class="title">{E(r["title"])}</div>']
    if r.get("sub"): f.append(f'<div class="subtitle">{E(r["sub"])}</div>')
    foot = getattr(mod, "FOOTER", "")
    f.append(f'<div class="foot"><div class="t">{E(foot)}</div><div class="line"></div><div class="n">{E(str(r["n"]))}</div></div>')
    return f

def tail(r, mod):
    if r.get("ask") and r.get("kind") not in ("cover", "divider"):
        return f'<div class="askbar"><span class="k">ASK</span><span class="v">{E(r["ask"])}</span></div>'
    return ""

def lint_head(r):
    errs = []
    if r.get("kind") != "cover" and r.get("kind") != "divider" and len(r.get("sub") or "") > 75:
        errs.append("takeaway line over 75 characters: say the point shorter")
    if r.get("kind") == "cover" and len(r.get("title", "")) > 22: errs.append("cover title over 22 characters (it is 120px)")
    return errs
