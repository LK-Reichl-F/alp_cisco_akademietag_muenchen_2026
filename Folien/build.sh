#!/bin/bash
set -e

# Logo: SVG → PDF (Inkscape, einmalig nötig)
if [ ! -f alp-logo.pdf ]; then
  inkscape --export-type=pdf \
           --export-filename=alp-logo.pdf \
           ../Quellen/ALP-Logo_Wort-Bild-Marke_RGB.svg
fi

# Präsentation bauen
pandoc praesentation.md \
  --to beamer \
  --pdf-engine=lualatex \
  --output praesentation.pdf \
  --highlight-style tango

echo "Fertig: praesentation.pdf"
