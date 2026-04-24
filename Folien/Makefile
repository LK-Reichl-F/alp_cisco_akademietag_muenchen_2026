SRC      := praesentation.md
OUT      := praesentation.pdf
LOGO     := alp-logo.pdf
LOGO_ICO := alp-logo-icon.pdf
ML_IMG   := MaschinellesLernen.pdf
ENGINE   := lualatex

.PHONY: all logo clean

all: logo $(ML_IMG) $(OUT)

# Logos: SVG → PDF (benötigt Inkscape)
logo: $(LOGO) $(LOGO_ICO)
$(LOGO):
	inkscape --export-type=pdf \
	         --export-filename=$(LOGO) \
	         ../Quellen/ALP-Logo_Wort-Bild-Marke_RGB.svg
$(LOGO_ICO):
	inkscape --export-type=pdf \
	         --export-filename=$(LOGO_ICO) \
	         ../Quellen/ALP-Logo.svg

# Grafik: MaschinellesLernen SVG → PDF
$(ML_IMG):
	inkscape --export-type=pdf \
	         --export-filename=$(ML_IMG) \
	         ../Quellen/MaschinellesLernen.drawio.svg

# Präsentation bauen
$(OUT): $(SRC) $(LOGO) $(LOGO_ICO) $(ML_IMG)
	pandoc $(SRC) \
	  --to beamer \
	  --pdf-engine=$(ENGINE) \
	  --output $(OUT) \
	  --highlight-style tango

clean:
	rm -f $(OUT) $(LOGO) $(LOGO_ICO) $(ML_IMG)
