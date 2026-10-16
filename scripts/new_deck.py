"""Make a fresh deck folder: the kit, a starter slides.py, the starter bodies and the agent contract.

usage: python3 new_deck.py <deck_dir> [--brand michelin] [--starter workshop]     (Windows: py new_deck.py ...)
--brand X    look (kit) from brands/X/. Default = Thinc. (kit/ at the repo root).
--starter Y  starter slides + method from starters/Y/ (slides.py, body/, METHOD.md). Default = the brand's template/.
"""
import sys, shutil, pathlib
def opt(name):
    v = next((a.split("=", 1)[1] for a in sys.argv[1:] if a.startswith(f"--{name}=")), None)
    if f"--{name}" in sys.argv: v = sys.argv[sys.argv.index(f"--{name}") + 1]
    return v
brand, starter = opt("brand"), opt("starter")
skip = {brand, starter}
args = [a for a in sys.argv[1:] if not a.startswith("--") and a not in skip]
if not args: raise SystemExit(__doc__)
SK = pathlib.Path(__file__).resolve().parent.parent
SRC = SK / "brands" / brand if brand else SK
if not (SRC / "kit").exists(): raise SystemExit(f"unknown brand '{brand}' (no {SRC / 'kit'})")
D = pathlib.Path(args[0]).resolve()
if (D / "slides.py").exists(): raise SystemExit(f"{D} already has slides.py - not touching it")
(D / "body").mkdir(parents=True, exist_ok=True); (D / "out").mkdir(exist_ok=True)
shutil.copytree(SRC / "kit", D / "kit", dirs_exist_ok=True)
TPL = SK / "starters" / starter if starter else SRC / "template"
if not (TPL / "slides.py").exists(): raise SystemExit(f"unknown starter '{starter}' (no {TPL / 'slides.py'})")
shutil.copy2(TPL / "slides.py", D / "slides.py")
for f in (TPL / "body").glob("*.html"): shutil.copy2(f, D / "body" / f.name)
shutil.copy2(SRC / "CONTRACT.md", D / "CONTRACT.md")
if (TPL / "METHOD.md").exists(): shutil.copy2(TPL / "METHOD.md", D / "METHOD.md")
print(f"deck ready ({brand or 'thinc'}{' + ' + starter if starter else ''}): {D}  (edit slides.py, write body/NN.html, then build + render)")
