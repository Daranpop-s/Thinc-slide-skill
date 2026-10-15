"""deck.html -> a Canva-importable HTML page, hosted for 1 hour. Prints the URL to give to Canva's import-design-from-url.

usage: python3 to_canva.py <deck_dir>

What it does: every <svg class="a"> drawing becomes a transparent 2x PNG <img> (Canva drops big inline SVGs),
the backgrounds are hosted once, kit.css is inlined, and Prompt comes from Google Fonts. Text stays real, editable text.

PRIVACY: this uploads the slide drawings and the page to litterbox.catbox.moe, a PUBLIC file host. Anyone with the link
can open it for 1 hour, then it deletes itself. Ask the deck owner before running it.
Test without uploading: THINC_DRYRUN=1 python3 to_canva.py <deck_dir>
"""
import re, subprocess, pathlib, time, sys, os
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from _chrome import base_args, popen, stop
from concurrent.futures import ThreadPoolExecutor
D = pathlib.Path(sys.argv[1]).resolve(); W = D / "canva"; W.mkdir(exist_ok=True)
if (D / "kit" / "PRIVATE").exists() and not (os.environ.get("THINC_DRYRUN") or os.environ.get("THINC_INLINE")):
    raise SystemExit("This deck's kit is marked PRIVATE (company content): no upload to a public host. Deliver the PDF instead.")
h = (D / "deck.html").read_text(encoding="utf-8")
SVG = re.compile(r'<svg class="a" style="left:(\d+)px;top:(\d+)px(;opacity:[\d.]+)?" width="(\d+)" height="(\d+)".*?</svg>', re.S)

def host(p):
    if os.environ.get("THINC_INLINE"):                                             # self-contained file for Canva's own upload (no public host)
        import base64, mimetypes
        return f"data:{mimetypes.guess_type(str(p))[0]};base64," + base64.b64encode(pathlib.Path(p).read_bytes()).decode()
    if os.environ.get("THINC_DRYRUN"): return pathlib.Path(p).resolve().as_uri()   # test run: no upload
    if not __import__("shutil").which("curl"): raise SystemExit("curl not found (Windows 10+ and macOS ship it)")
    u = ""
    for _ in range(4):
        u = subprocess.run(["curl", "-s", "-F", "reqtype=fileupload", "-F", "time=1h", "-F", f"fileToUpload=@{p}",
                            "https://litterbox.catbox.moe/resources/internals/api.php"], capture_output=True, text=True).stdout.strip()
        if u.startswith("https://"): return u
        time.sleep(2)
    raise SystemExit(f"upload failed {p}: {u}")

def render(job):
    i, svg, w, hh = job
    f = W / f"a{i}.html"; png = W / f"a{i}.png"
    if png.exists(): png.unlink()
    f.write_text(f'<!doctype html><html><head><meta charset="utf-8"><link rel="stylesheet" href="../kit/fonts.css"><style>html,body{{margin:0;background:transparent;overflow:hidden;font-family:Prompt}}svg{{display:block}}</style></head><body>{svg}</body></html>', encoding="utf-8")
    for attempt in range(3):                      # Chrome sometimes stalls under load: retry, then fail loudly
        p = popen(base_args(W / f"ch{i}") + ["--hide-scrollbars", "--force-device-scale-factor=2",
                   "--default-background-color=00000000", f"--window-size={w},{hh}", f"--screenshot={png}", f.as_uri()])
        for _ in range(60):
            if png.exists() and png.stat().st_size: break
            time.sleep(0.5)
        time.sleep(0.5); stop(p)
        if png.exists() and png.stat().st_size: break
    else:
        raise SystemExit(f"drawing {i} did not render (see {f})")
    return host(png)

jobs = []
for i, m in enumerate(SVG.finditer(h)):
    l, t, op, w, hh = m.groups()
    svg = re.sub(r'^<svg class="a" style="[^"]*" ', "<svg ", m.group(0))
    jobs.append((i, svg, w, hh))
with ThreadPoolExecutor(6) as ex: urls = list(ex.map(render, jobs))
out, last = [], 0
for m, u in zip(SVG.finditer(h), urls):
    l, t, op, w, hh = m.groups()
    out.append(h[last:m.start()] + f'<img class="a" src="{u}" style="left:{l}px;top:{t}px;width:{w}px;height:{hh}px{op or ""}">'); last = m.end()
out.append(h[last:]); h2 = "".join(out)
assert "<svg" not in h2, "svg left in output"
for bg in ("bg.jpg", "bg-dark.jpg"):
    if f'src="kit/{bg}"' in h2: h2 = h2.replace(f'src="kit/{bg}"', f'src="{host(D / "kit" / bg)}"')
css = (D / "kit" / "kit.css").read_text(encoding="utf-8")
h2 = h2.replace('<link rel="stylesheet" href="kit/fonts.css">',
                '<link href="https://fonts.googleapis.com/css2?family=Prompt:wght@400;500;600;700&display=swap" rel="stylesheet">')
h2 = h2.replace('<link rel="stylesheet" href="kit/kit.css">', f"<style>{css}</style>")
final = W / "deck_canva.html"; final.write_text(h2, encoding="utf-8")
print(len(jobs), "drawings")
print(final if os.environ.get("THINC_INLINE") else host(final))
