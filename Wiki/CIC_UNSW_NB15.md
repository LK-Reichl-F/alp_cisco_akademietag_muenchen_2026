# CIC-UNSW-NB15

**Zusammenfassung**: Augmentierter Datensatz, der das UNSW-NB15-Dataset mit CICFlowMeter neu aufbereitet. Kompakt, balanciert, 9 Angriffskategorien. Sekundäre Option für den Workshop.

**Quellen**: (Quelle: [[UNSW-NB15 Augmented Dataset  Datasets  Research  Canadian Institute for Cybersecurity.md]])

**Zuletzt aktualisiert**: 2026-04-16

---

## Überblick

| Eigenschaft | Wert |
|---|---|
| Vollständiger Name | CIC-UNSW-NB15 |
| Herausgeber | Canadian Institute for Cybersecurity |
| Basis | UNSW-NB15 (University of New South Wales, 2015), re-labeled 2024 |
| Tool | IXIA PerfectStorm (Traffic-Erzeugung) + CICFlowMeter (Feature-Extraktion) |
| Angriffskategorien | 9 + Benign |
| Verhältnis | 80% Benign / 20% Malicious (bewusst balanciert) |
| Gesamtzeilen | ~448.000 |
| Features | 80+ (CICFlowMeter, gleich wie CICIDS2017) |

## Angriffskategorien

| Kategorie | Beschreibung |
|---|---|
| **Fuzzers** | Zufällige/unerwartete Eingaben, um Softwareschwächen zu finden |
| **Analysis** | Informationssammlung: Traffic-Analyse, Code-Analyse, Protokollanalyse |
| **Backdoor** | Versteckter Zugangspunkt durch Schadcode im System |
| **DoS** | Denial-of-Service durch Überlastung |
| **Exploits** | Ausnutzung von Schwachstellen in Software oder Protokollen |
| **Generic** | Angriff auf Kryptosysteme, unabhängig von der Blockcipher-Struktur |
| **Reconnaissance** | Informationssammlung über Zielsystem ohne direkten Schaden |
| **Shellcode** | In vulnerables Programm injizierter Maschinencode |
| **Worms** | Sich selbst verbreitende Schadsoftware ohne Benutzerinteraktion |

## Datensatz-Dateien

| Datei | Inhalt |
|---|---|
| `CICFlowMeter_out.csv` | Alle extrahierten Flows (inkl. nicht verwendete) |
| `Data.csv` | 80/20-balancierter Datensatz (~448k Zeilen) |
| `Label.csv` | Numerische Labels für `Data.csv` |
| `Readme.txt` | Zuordnung Label-Nummern zu Kategorienamen |

## Klassenverteilung

| Klasse | Original UNSW-NB15 | CICFlowMeter | CIC-UNSW-NB15 (80/20) |
|---|---|---|---|
| Benign | 2.218.764 | 3.450.658 | **358.332** |
| Analysis | 2.677 | 385 | 385 |
| Backdoor | 2.329 | 452 | 452 |
| DoS | 16.353 | 4.467 | 4.467 |
| Exploits | 44.525 | 30.951 | 30.951 |
| Fuzzers | 24.246 | 29.613 | 29.613 |
| Generic | 215.481 | 4.632 | 4.632 |
| Reconnaissance | 13.987 | 16.735 | 16.735 |
| Shellcode | 1.511 | 2.102 | 2.102 |
| Worms | 174 | 246 | 246 |

## Vergleich mit CICIDS2017 für den Workshop

| Kriterium | CICIDS2017 | CIC-UNSW-NB15 |
|---|---|---|
| Topologie | On-Premise (Firewall, LAN) | Generierter Traffic |
| Zielgruppe-Fit | ✅ Sehr hoch (bekannte Angriffe) | ⚠️ Mittel (abstraktere Kategorien) |
| Größe | Groß (Subset nötig) | Handhabbar (~448k) |
| Balancierung | Nicht balanciert | ✅ 80/20 bereits optimiert |
| Narrativer Rahmen | ✅ Wochenstruktur | ❌ Kein Zeitrahmen |
| Bekannte Angriffe | DoS, DDoS, Brute Force | Fuzzer, Shellcode, Generic (weniger bekannt) |

## Wann könnte CIC-UNSW-NB15 sinnvoll sein?

- Als **Vergleichsdatensatz** für Fortgeschrittene: „Funktioniert unser Modell auch auf anderen Daten?"
- Wenn die 80/20-Balancierung wichtig ist (bei sehr unbalancierten Klassen schlägt Imbalanced Learning an)
- Als kompaktere Alternative, wenn CICIDS2017-Dateien zu groß sind

## Verwandte Seiten

- [[CICIDS2017]]
- [[CICFlowMeter_Features]]
- [[Workshop_Konzept]]
- [[Angriffsszenarien]]
