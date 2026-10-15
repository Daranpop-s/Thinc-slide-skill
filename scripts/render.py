"""deck.html -> out/deck.pdf -> out/p-N.png (one per slide) + out/contact.png (all slides on one sheet).

usage: python3 render.py <deck_dir>            (Windows: py render.py <deck_dir>)
Works on macOS, Windows and Linux. Chrome is found automatically; set CHROME=<path> to override.
Needs: pip install pillow pypdfium2   (pypdfium2 replaces poppler's pdftoppm, so nothing else to install)
"""
import sys, time, shutil, pathlib, subprocess
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from _chrome import base_args, popen, stop

D = pathlib.Path(sys.argv[1]).resolve(); out = D / "out"; out.mkdir(exist_ok=True)
for f in out.glob("p-*.png"): f.unlink()
pdf = out / "deck.pdf"
if pdf.exists(): pdf.unlink()

p = popen(base_args(D / ".chr") + ["--no-pdf-header-footer", f"--print-to-pdf={pdf}", (D / "deck.html").as_uri()])
for _ in range(90):                          # Chrome sometimes keeps running after the PDF is written: watch the file, then stop it
    if pdf.exists() and pdf.stat().st_size and p.poll() is not None: break
    if pdf.exists() and pdf.stat().st_size: time.sleep(2); break
    time.sleep(1)
stop(p)
if not (pdf.exists() and pdf.stat().st_size): raise SystemExit("render failed: no PDF (is Chrome installed? or set CHROME=<path>)")

try:                                         # PDF -> PNG pages
    import pypdfium2 as pdfium
    doc = pdfium.PdfDocument(str(pdf))
    for i in range(len(doc)):
        doc[i].render(scale=96 / 72).to_pil().save(out / f"p-{i + 1}.png")
    doc.close()
except ImportError:
    if not shutil.which("pdftoppm"): raise SystemExit("install a PDF renderer: python3 -m pip install pypdfium2")
    subprocess.run(["pdftoppm", "-r", "96", "-png", str(pdf), str(out / "p")], check=True)

from PIL import Image                        # contact sheet
fs = sorted(out.glob("p-*.png"), key=lambda f: int(f.stem.split("-")[1]))
ims = [Image.open(f).resize((640, 360)) for f in fs]
cols = 4; rows = (len(ims) + cols - 1) // cols
S = Image.new("RGB", (cols * 640, rows * 360), "white")
for i, im in enumerate(ims): S.paste(im, ((i % cols) * 640, (i // cols) * 360))
S.save(out / "contact.png")
print(len(fs), "pages -> out/deck.pdf, out/contact.png")
