#!/bin/bash
# Same as: python3 render.py <deck_dir>  (kept so old instructions still work on Mac/Linux)
exec python3 "$(dirname "$0")/render.py" "$@"
