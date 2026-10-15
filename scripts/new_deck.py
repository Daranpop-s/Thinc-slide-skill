"""Make a fresh deck folder: the kit, a starter slides.py, the starter bodies and the agent contract.

usage: python3 new_deck.py <deck_dir> [--brand michelin]     (Windows: py new_deck.py ...)
Default brand = Thinc. (kit/, template/, CONTRACT.md at the repo root). --brand X uses brands/X/.
"""
import sys, shutil, pathlib
args = [a for a in sys.argv[1:] if not a.startswith("--brand")]
brand = next((a.split("=", 1)[1] for a in sys.argv[1:] if a.startswith("--brand=")), None)
if "--brand" in sys.argv: brand = sys.argv[sys.argv.index("--brand") + 1]; args = [a for a in args if a != brand]
if not args: raise SystemExit(__doc__)
SK = pathlib.Path(__file__).resolve().parent.parent
SRC = SK / "brands" / brand if brand else SK
if not (SRC / "kit").exists(): raise SystemExit(f"unknown brand '{brand}' (no {SRC / 'kit'})")
D = pathlib.Path(args[0]).resolve()
if (D / "slides.py").exists(): raise SystemExit(f"{D} already has slides.py - not touching it")
(D / "body").mkdir(parents=True, exist_ok=True); (D / "out").mkdir(exist_ok=True)
shutil.copytree(SRC / "kit", D / "kit", dirs_exist_ok=True)
shutil.copy2(SRC / "template" / "slides.py", D / "slides.py")
for f in (SRC / "template" / "body").glob("*.html"): shutil.copy2(f, D / "body" / f.name)
shutil.copy2(SRC / "CONTRACT.md", D / "CONTRACT.md")
print(f"deck ready ({brand or 'thinc'}): {D}  (edit slides.py, write body/NN.html, then build + render)")
