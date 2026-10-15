#!/bin/bash
# usage: new_deck.sh <deck_dir>   — makes a fresh deck folder with the kit, a starter slides.py and the agent contract
SK=$(cd "$(dirname "$0")/.." && pwd); D="$1"
[ -e "$D/slides.py" ] && { echo "$D already has slides.py — not touching it"; exit 1; }
mkdir -p "$D/body" "$D/out"
cp -R "$SK/kit" "$D/"
cp "$SK/template/slides.py" "$D/slides.py"
cp "$SK/template/body/"*.html "$D/body/"
cp "$SK/CONTRACT.md" "$D/CONTRACT.md"
echo "deck ready: $D  (edit slides.py, write body/NN.html, then build + render)"
