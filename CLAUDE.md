# LLM Wiki

Eine persönliche Wissensdatenbank, gepflegt von Claude Code.
Basiert auf Andrej Karpathys LLM-Wiki-Muster.

## Zweck

Dieses Wiki ist eine strukturierte, vernetzte Wissensdatenbank zur Planung eines Workshops für 90 Minuten zum Thema Orange Data Mining für Lehrkräfte aus dem Umfeld von Netzwerktechnik an beruflichen Schulen (Cisco Academy).
Claude pflegt das Wiki. Der Mensch kuratiert Quellen, stellt Fragen und leitet die Analyse.

## Ordnerstruktur

```
Quellen/          -- Quelldokumente (unveränderlich -- niemals bearbeiten)
Wiki/         -- Markdown-Seiten, gepflegt von Claude
Wiki/Index.md -- Inhaltsverzeichnis des gesamten Wikis
Wiki/Log.md   -- Unveränderliches Protokoll aller Operationen
```

## Ingest-Workflow

Wenn der Benutzer eine neue Quelle zu `raw/` hinzufügt und dich bittet, sie einzupflegen:

1. Quelldokument vollständig lesen
2. Wichtigste Erkenntnisse mit dem Benutzer besprechen, bevor etwas geschrieben wird
3. Eine Zusammenfassungsseite in `Wiki/` anlegen, benannt nach der Quelle
4. Konzeptseiten für jede wichtige Idee oder Entität erstellen oder aktualisieren
5. Wiki-Links ([[Seitenname]]) hinzufügen, um verwandte Seiten zu verknüpfen
6. `Wiki/Index.md` mit neuen Seiten und einzeiligen Beschreibungen aktualisieren
7. Einen Eintrag in `Wiki/Log.md` anhängen mit Datum, Quellenname und den vorgenommenen Änderungen

Eine einzelne Quelle kann 10–15 Wiki-Seiten berühren. Das ist normal.

## Seitenformat

Jede Wiki-Seite sollte dieser Struktur folgen:

```markdown
# Seitentitel

**Zusammenfassung**: Ein bis zwei Sätze, die diese Seite beschreiben.

**Quellen**: Liste der Quelldateien, auf die sich diese Seite stützt.

**Zuletzt aktualisiert**: Datum der letzten Aktualisierung.

---

Hauptinhalt hier. Klare Überschriften und kurze Absätze verwenden.

Verwandte Konzepte mit [[Wiki-Links]] im Text verknüpfen.

## Verwandte Seiten

- [[Verwandtes-Konzept-1]]
- [[Verwandtes-Konzept-2]]
```

Zeichnung nach Möglichkeit mit Mermaid erstellen.
## Zitierregeln

- Jede sachliche Aussage sollte ihre Quelldatei referenzieren
- Format: (Quelle: [[Markdowndatei.md]]) nach der Aussage
- Falls zwei Quellen widersprechen, den Widerspruch ausdrücklich vermerken
- Falls eine Aussage keine Quelle hat, als verifizierungsbedürftig markieren

## Fragen beantworten

Wenn der Benutzer eine Frage stellt:

1. Zuerst `Wiki/Index.md` lesen, um relevante Seiten zu finden
2. Diese Seiten lesen und eine Antwort synthetisieren
3. Spezifische Wiki-Seiten in der Antwort zitieren
4. Falls die Antwort nicht im Wiki enthalten ist, dies klar sagen
5. Falls die Antwort wertvoll ist, anbieten, sie als neue Wiki-Seite zu speichern

Gute Antworten sollten ins Wiki zurückgeführt werden, damit sie sich im Laufe der Zeit akkumulieren.

## Lint

Wenn der Benutzer darum bittet, das Wiki zu linten oder zu prüfen:

- Widersprüche zwischen Seiten prüfen
- Verwaiste Seiten finden (keine eingehenden Links von anderen Seiten)
- Konzepte identifizieren, die in Seiten erwähnt werden, aber keine eigene Seite haben
- Aussagen markieren, die aufgrund neuerer Quellen veraltet sein könnten
- Prüfen, ob alle Seiten dem obigen Seitenformat folgen
- Ergebnisse als nummerierte Liste mit Korrekturvorschlägen melden

## Regeln

- Niemals etwas im `Quellen/`-Ordner bearbeiten
- Nach Änderungen immer `Wiki/Index.md` und `Wiki/Log.md` aktualisieren
- Seitennamen Worten mit Unterstrichen halten (z. B. `Maschinelles_Lernen.md`)
- In klarer, einfacher Sprache schreiben
- Bei Unsicherheit über die Kategorisierung den Benutzer fragen

---

## Aktueller Stand — 2026-04-24

### Artefakte

| Datei | Status |
|---|---|
| `Folien/praesentation.md` | Hauptquelle, wird mit `make` zu `praesentation.pdf` gebaut |
| `Folien/handout.tex` | LuaLaTeX-Handout, wird mit `make` zu `handout.pdf` gebaut |
| `Folien/Makefile` | Baut beide PDFs; Inkscape für SVG→PDF, pandoc+lualatex für Beamer |
| `Wiki/CRISP-DM.md` | Neu erstellt; vollständiges Mapping aller 6 Phasen auf den Workshop |
| `Wiki/Log.md` | Unveränderlich; alle Operationen protokolliert |

### Folienreihenfolge (Stand 2026-04-24)

```
# Einstieg
  Agenda
  Cisco NGFW schützt unser Netzwerk
  Das Problem: DDoS überlastet die Firewall
  Die Idee: ML als Vorfilter
  Lernziele                          ← hierher verschoben (war zu spät)
  Maschinelles Lernen                ← Bild MaschinellesLernen.pdf
  Regelbasiert vs. maschinell lernen
  Der Unterschied im Kern
  Unser Prozessrahmen: CRISP-DM

# Daten erkunden
  CRISP-DM · Phase 2: Data Understanding
  Der Datensatz: CICIDS2017
  Daten erkunden: Data Table
  Was sehen wir im Scatter Plot?
  Zwischensicherung: Daten haben Struktur

# Entscheidungsbaum
  CRISP-DM · Phase 4: Modeling
  Was ist ein Entscheidungsbaum?
  Der Entscheidungsbaum in Orange
  Welche Frage steht ganz oben?
  Ist das Magie?

# Modellbewertung
  CRISP-DM · Phase 5: Evaluation
  Wie gut ist unser Modell?
  Die Confusion Matrix
  Accuracy, Precision und Recall
  Die Spannung im IDS              ← eigene Folie (war im vorigen Block)
  Alert Fatigue – ein reales Problem

# Modellvergleich
  CRISP-DM · Phase 5: Evaluation (Fortsetzung)
  Entscheidungsbaum – Flowchart-Logik
  Random Forest – das Komitee
  k-Nearest Neighbors – Ähnlichkeitssuche
  Drei Modelle im Vergleich
  Genauigkeit vs. Erklärbarkeit

# Abschluss
  CRISP-DM · Phase 6: Deployment
  Was haben wir gelernt?
  Transfer in den Unterricht
  Materialien
  Danke – und ein Wort zum Schluss
```

### Wichtige Designentscheidungen

- **Regelkonfiguration (Signaturpflege)** ersetzt überall „GOFA / Good Old-Fashioned AI" (kein KI-Begriff, sondern manuelle Firewall-Arbeit)
- **Lernziel 1** lautet: „erläutern, was maschinelles Lernen ist und wie es sich von *vom Menschen vorgenommener* Regelkonfiguration (Signaturpflege) unterscheidet" — betont, dass in beiden Fällen Regeln konfiguriert werden, der Unterschied nur im Wer liegt
- **Explainable AI**-Kasten auf der Folie „Entscheidungsbaum – Flowchart-Logik": bewusst abgeschwächt zu „wünschenswert" (nicht „müssen")
- **kNN-Folie**: TikZ-Scatter-Plot mit Abstandslinien; Ergebniskasten oben rechts bei (4.2, 3.2)
- **CRISP-DM-Folie**: Speaker Notes enthalten Quellenbelege (KDnuggets 2002–2014, Forbes 2015, Mariscal 2010)
- **Build**: `cd Folien && make` — benötigt Inkscape (SVG→PDF) und pandoc+lualatex

### Offene Punkte / mögliche nächste Schritte

- Handout spiegelt die neuen Lernziele (7 statt 6) noch nicht wider
- Handout enthält noch keinen Abschnitt zu Accuracy/Precision/Recall anhand der Konfusionsmatrix
- Präsentation wurde zuletzt erfolgreich gebaut (kein Fehler)
