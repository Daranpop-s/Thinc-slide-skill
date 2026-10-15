#!/bin/bash
# usage: render.sh <deck_dir>
# deck.html -> <deck>/out/deck.pdf -> out/p-NN.png (one per slide) + out/contact.png (all slides on one sheet)
D=$(cd "$1" && pwd); cd "$D" || exit 1
CH="${CHROME:-/Applications/Google Chrome.app/Contents/MacOS/Google Chrome}"
NS=""; [ "$(id -u)" = "0" ] && NS="--no-sandbox"   # Chrome refuses to run as root without it (Linux/cloud)
mkdir -p out; rm -f out/p-*.png out/deck.pdf
"$CH" $NS --headless=new --disable-gpu --no-pdf-header-footer --user-data-dir="$D/.chr" --print-to-pdf="$D/out/deck.pdf" "file://$D/deck.html" >/dev/null 2>&1 &
P=$!; for i in $(seq 1 90); do [ -s out/deck.pdf ] && break; sleep 1; done; sleep 2; kill $P 2>/dev/null; pkill -f "user-data-dir=$D/.chr" 2>/dev/null
[ -s out/deck.pdf ] || { echo "render failed: no PDF (check the Chrome path, or set CHROME=...)"; exit 1; }
pdftoppm -r 96 -png out/deck.pdf out/p
python3 - <<'PY'
from PIL import Image; import glob
fs=sorted(glob.glob('out/p-*.png')); ims=[Image.open(f).resize((640,360)) for f in fs]
cols=4; rows=(len(ims)+cols-1)//cols
S=Image.new('RGB',(cols*640,rows*360),'white')
for i,im in enumerate(ims): S.paste(im,((i%cols)*640,(i//cols)*360))
S.save('out/contact.png'); print(len(fs),'pages -> out/deck.pdf, out/contact.png')
PY
