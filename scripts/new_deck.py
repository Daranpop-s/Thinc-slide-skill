"""Make a fresh deck folder: the kit, a starter slides.py, the starter bodies and the agent contract.

usage: python3 new_deck.py <deck_dir>          (Windows: py new_deck.py <deck_dir>)
"""
import sys, shutil, pathlib
SK = pathlib.Path(__file__).resolve().parent.parent
D = pathlib.Path(sys.argv[1]).resolve()
if (D / "slides.py").exists(): raise SystemExit(f"{D} already has slides.py - not touching it")
(D / "body").mkdir(parents=True, exist_ok=True); (D / "out").mkdir(exist_ok=True)
shutil.copytree(SK / "kit", D / "kit", dirs_exist_ok=True)
shutil.copy2(SK / "template" / "slides.py", D / "slides.py")
for f in (SK / "template" / "body").glob("*.html"): shutil.copy2(f, D / "body" / f.name)
shutil.copy2(SK / "CONTRACT.md", D / "CONTRACT.md")
print(f"deck ready: {D}  (edit slides.py, write body/NN.html, then build + render)")
