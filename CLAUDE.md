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
