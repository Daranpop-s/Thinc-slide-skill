"""Frame + slide bodies -> <deck>/deck.html. Lints every body and every header.

usage: python3 build.py <deck_dir> [NN,NN,...]

<deck_dir>/slides.py holds  S = [dict(...), ...]  (see template/slides.py for the fields).
<deck_dir>/body/NN.html holds the body of slide NN (written by you or by one agent per slide).
"""
import re, sys, pathlib, html, importlib.util
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent)); import _chrome  # noqa: utf-8 console on Windows

D = pathlib.Path(sys.argv[1]).resolve()
only = sys.argv[2].split(",") if len(sys.argv) > 2 else None
spec = importlib.util.spec_from_file_location("slides", D / "slides.py")
mod = importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)
S = mod.S
TRACKER = getattr(mod, "TRACKER", 0)          # 0 = no step dots (default). N = show N step dots.
BRAND = getattr(mod, "BRAND", "Thinc.")
E = html.escape
THAI = re.compile(r"[฀-๿]")
SVG = re.compile(r'<svg class="a" style="left:(\d+)px;top:(\d+)px(?:;opacity:[\d.]+)?" width="(\d+)" height="(\d+)".*?</svg>', re.S)
DIM = ".22"                                     # opacity of the parts that are not in focus on a build-up page
KF = None                                       # brand frame: <deck>/kit/frame.py overrides the Thinc. frame (e.g. --brand michelin)
if (D / "kit" / "frame.py").exists():
    _s = importlib.util.spec_from_file_location("kitframe", D / "kit" / "frame.py")
    KF = importlib.util.module_from_spec(_s); _s.loader.exec_module(KF)

def lint_body(b):
    errs = []
    for m in re.finditer(r'style="([^"]*)"', b):
        if re.search(r"font|letter-spacing|line-height|text-transform", m.group(1)): errs.append(f"inline font style: {m.group(1)[:60]}")
    for m in re.finditer(r"<svg\b.*?</svg>", b, re.S):
        if not SVG.match(m.group(0)): errs.append('svg tag not in exact form <svg class="a" style="left:Xpx;top:Ypx" width="W" height="H" ...')
        if THAI.search(m.group(0)): errs.append("Thai text inside <svg> (put it in an HTML div on top)")
    if re.search(r'style="[^"]*(gradient\(|box-shadow|filter:)', b): errs.append("CSS gradient/shadow/filter in HTML (Canva turns these into square boxes)")
    if "<section" in b: errs.append("body must not contain <section>")
    return errs

def lint_head(r):
    errs = []
    if "eyebrow" in r: errs.append("no eyebrow: the header is one big bold title (+ optional plain subtitle)")
    for k in ("title", "sub", "time"):
        v = r.get(k) or ""
        if "·" in v: errs.append(f"'·' in {k}: write it as plain words")
        lat = re.sub(r"[^A-Za-z]", "", v)
        if k == "title" and len(lat) > 3 and lat.isupper(): errs.append("all-caps title: use normal case")
    if len(r.get("title", "")) > 40 and r.get("kind") != "divider": errs.append("title over 40 characters: say the point shorter")
    return errs

def apply_build(body, k):
    """<div data-b="N"> ... </div> groups: on page k, every group except N==k is dimmed. Wrappers are removed."""
    def dim(m):
        if m.group(1) == str(k): return m.group(2)
        return re.sub(r'(<(?:div|svg|img)\b[^>]*?style=")([^"]*)(")', lambda t: t.group(1) + t.group(2).rstrip(";") + f";opacity:{DIM}" + t.group(3), m.group(2))
    return re.sub(r'<div data-b="(\d+)">(.*?)</div><!--/b-->', dim, body, flags=re.S)

def frame(r):
    bgimg = "kit/bg.jpg" if r.get("bg") == "bright" or r.get("kind") == "divider" else "kit/bg-dark.jpg"
    f = [f'<img class="bg" src="{bgimg}">', f'<div class="brand">{E(BRAND)}</div>']
    if r.get("kind") == "divider":
        f.append(f'<div class="dtitle">{E(r["title"])}</div>')
        if r.get("sub"): f.append(f'<div class="dsub">{E(r["sub"])}</div>')
        return f
    f.append(f'<div class="title">{E(r["title"])}</div>')
    if r.get("sub"): f.append(f'<div class="subtitle">{E(r["sub"])}</div>')
    st = r.get("step") or 0
    if TRACKER and st:
        dots = "".join(f"<b>{i}</b>" if i == st else f'<i class="{"d" if i < st else ""}"></i>' for i in range(1, TRACKER + 1))
        f.append(f'<div class="tracker">{dots}</div>')
    if r.get("time"): f.append(f'<div class="timechip">{E(r["time"])}</div>')
    return f

def page(r, body, label):
    if KF:
        f, tail, cls = KF.frame(r, mod), KF.tail(r, mod), KF.section_class(r)
    else:
        f, cls = frame(r), ""
        tail = f'<div class="outbar"><span class="k">OUTPUT</span><span class="v">{E(r["out"])}</span></div>' if r.get("out") else ""
    return f'<section data-document-role="page" data-label="{label}"' + (f' class="{cls}"' if cls else "") + '>\n' + "\n".join(f) + "\n" + body + "\n" + tail + "\n</section>"

pages, bad = [], {}
for r in S:
    n = r["n"]
    if only and n not in only: continue
    p = D / "body" / f"{n}.html"
    if p.exists(): body = p.read_text(encoding="utf-8")
    elif r.get("kind") == "divider": body = ""
    else: body = '<div class="a l grey" style="left:110px;top:500px">[body missing]</div>'
    e = lint_head(r) + lint_body(body) + (KF.lint_head(r) if KF else [])
    if e: bad[n] = e
    steps = r.get("builds") or 0
    if steps:
        for k in range(1, steps + 1): pages.append(page(r, apply_build(body, k), f"{n}.{k} {E(r['title'])}"))
    else:
        pages.append(page(r, body.replace("<!--/b-->", ""), f"{n} {E(r['title'])}"))
doc = ('<!doctype html><html><head><meta charset="utf-8"><link rel="stylesheet" href="kit/fonts.css">'
       '<link rel="stylesheet" href="kit/kit.css"><style>@page{size:1920px 1080px;margin:0}</style></head><body>\n'
       + "\n".join(pages) + "\n</body></html>")
(D / "deck.html").write_text(doc, encoding="utf-8")
for k, v in bad.items(): print("LINT", k, *v, sep="\n  ")
print("pages", len(pages))
