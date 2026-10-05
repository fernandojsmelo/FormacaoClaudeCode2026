#!/bin/bash
# build.sh arquivo.html -> arquivo.pdf (pipeline do CLAUDE.md) e mostra páginas
for h in "$@"; do p="${h%.html}.pdf"
google-chrome --headless --disable-gpu --no-sandbox --run-all-compositor-stages-before-draw --virtual-time-budget=4000 --no-pdf-header-footer --print-to-pdf="$PWD/$p" "file://$PWD/$h" 2>/dev/null
echo "$p: $(pdfinfo "$p" | awk '/Pages/{print $2}') págs"; done
