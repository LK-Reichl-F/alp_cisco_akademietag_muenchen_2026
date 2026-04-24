# Wiki-Log

Unveränderliches Protokoll aller Wiki-Operationen.

---

## 2026-04-24 — GOFA/Good Old-Fashioned AI ersetzt

„GOFA" und „Good Old-Fashioned AI" aus allen Unterlagen entfernt. Begründung: Es handelt sich um Firewall-Konfiguration, nicht um eine KI-Anwendung. Ersatz:
- Vollform: **Regelkonfiguration (Signaturpflege)**
- Kurzform (bei Platzmangel): **Regelkonfiguration**

Geänderte Dateien:
- `praesentation.md`: Block-Titel, Spaltenüberschrift, Kernformel-Alertblock, Speaker Notes (4×), Abschluss-Lernpunkte
- `Wiki/Workshop_Arbeitsplan.md`: Verlaufsplan Phase 1

Nicht geändert: `Wiki/Log.md` (historische Einträge, unveränderlich).

---

## 2026-04-24 — CRISP-DM als Prozessrahmen eingeführt

**Neue Quellen**: `Cross-industry standard process for data mining.md` (Wikipedia), `CRISP-DM_Process_Diagram.png` (offizielle Prozessdiagramm-Grafik).

**`Wiki/CRISP-DM.md`** neu erstellt: Überblick über die sechs CRISP-DM-Phasen, Mermaid-Flussdiagramm mit Rückschleifen, vollständiges Mapping aller Phasen auf den Workshop-Ablauf, didaktische Einordnung.

**`Wiki/Index.md`**: Neue Rubrik „Prozessrahmen" mit Eintrag für CRISP-DM.

**`praesentation.md`**:
- Lernziel 6 ergänzt: „das heutige Vorgehen den sechs Phasen von CRISP-DM zuordnen"
- Neue Folie „Unser Prozessrahmen: CRISP-DM" nach Lernziele: linke Spalte Erklärtext + Mapping-Tabelle, rechte Spalte offizielles Prozessdiagramm (`CRISP-DM_Process_Diagram.png`), Speaker Notes

**`handout.tex`**:
- Vollbreiter CRISP-DM-Rahmenblock vor `\begin{multicols}{2}` mit kompakter Sechs-Phasen-Zuordnung
- Glossar-Eintrag CRISP-DM ergänzt

---

## 2026-04-19 — Nachzügler nach Konsistenzprüfung bereinigt

**`Workshop_Handout.md`**: „Das Szenario" auf neue Rahmen-Story aktualisiert (Cisco NGFW, DDoS-Überlastungskette, ML als Vorfilter). Datum auf 2026-04-19 gesetzt.

**`Workshop_Arbeitsplan.md`**: Lernziel 1 auf „ML-Vorfilterung Cisco-Geräte entlasten" aktualisiert. Phase-1-Verlaufsplan auf neue Narrativ (Überlastungskette, GOFA vs. ML) umgestellt.

**`Orange_Klassifikations_Workflow.md`**: Beispielbaum-Feature-Namen korrigiert (`fl_byt_s` → `Flow Bytes/s`, `tot_fw_pk` → `Down/Up Ratio`); Werte konsistent mit Präsentation (`> 45.000`).

**`praesentation.md`** – Folie „Entscheidungsbaum – Flowchart-Logik" (Modellvergleich): Duplikation des Beispielbaums entfernt. Folie zeigt jetzt Positionstabelle (Accuracy, Lesbarkeit, Vorfilter) + Kernregel-Kurzform + Vergleich zu Random Forest statt Wiederholung der früheren Erklärungsfolie.

---

## 2026-04-19 — Konsistenzprüfung aller Artefakte

**Behobene Fehler:**
- `workshop_ids.csv` → `workshop_ids.tab` in: `praesentation.md` (2×), `Workshop_Arbeitsplan.md` (3×), `Orange_Klassifikations_Workflow.md` (2×), `CICIDS2017.md` (1×)
- `LOIT` → `LOIC` in: `praesentation.md` (Notes), `handout.tex`

**Neue Folien in `praesentation.md`:**
- Folie „Der Unterschied im Kern": 4-Schritte-Prozess GOFA vs. ML, Kernformel-Alertblock (ersetzt den überlaufenden Alertblock am Ende von „Regelbasiert vs. maschinell lernen")
- Folie „Entscheidungsbaum – Flowchart-Logik": Wiederholung im Modellvergleich (bewusste Redundanz für didaktischen Bogen)
- Folie „Random Forest – das Komitee": Bootstrap, Voting, Black-Box-Nachteil
- Folie „k-Nearest Neighbors – Ähnlichkeitssuche": Kein Training, Latenz-Problem, Forensik-Nutzen
- Präsentation: 33 Folien (vorher 28)

**Verbleibende bekannte Inkonsistenzen (offen, s. u.):**
- `Workshop_Handout.md` (Wiki) und `Workshop_Arbeitsplan.md` Phase 1 spiegeln noch die alte Narrativ vor der Rahmen-Story-Revision wider
- `Workshop_Arbeitsplan.md` Lernziel 1 noch nicht auf neue Formulierung aktualisiert
- `Orange_Klassifikations_Workflow.md` Beispielbaum nutzt noch alte kurze Feature-Namen (`fl_byt_s`, `tot_fw_pk`)
- `LOIT` als Angriffsname (kein Tool-Name) verbleibt in mehreren Wiki-Dateien (`Angriffsszenarien.md`, `CICIDS2017.md`, `On_Premise_Netzwerktopologie.md`, `Workshop_Konzept.md`, `Cisco_Sicherheitsarchitektur.md`) — Konsens: „DDoS LOIT" ist etablierter Kurzname im Datensatz-Kontext

---

## 2026-04-19 — Algorithmen-Erklärungen ergänzt

Neue Quellen eingepflegt: `Entscheidungsbaum in Orange.md`, `Random Forest Orange.md`, `kNN Orange.md`.

**Erkenntnisse aus den Quellen:**
- Entscheidungsbaum (Tree): teilt Daten per Information Gain (Klassenreinheit) – Vorläufer von Random Forest in Orange
- Random Forest: Ensemble aus Bäumen, jeder auf Bootstrap-Sample trainiert; bei jedem Split zufällige Feature-Auswahl (daher „random"); Mehrheitsentscheid
- kNN: speichert alle Trainingsdaten; für neue Instanz werden k nächste Nachbarn im Feature-Raum gesucht; normalisiert Daten automatisch; zu langsam für Leitungsgeschwindigkeit

**Änderungen an `praesentation.md`:**
- „Was ist ein Entscheidungsbaum?" → Analogie: Cisco-Troubleshooting-Flowchart, automatisch aus Daten generiert
- Neue Folie „Drei Modelle – drei Ideen": je ein Block mit intuitiver Analogie (Flowchart / Komitee / Ähnlichkeitssuche)
- Neue Folie „Drei Modelle im Vergleich": Tabelle mit Accuracy, Lesbarkeit, Vorfilter-Eignung; Fußnote zu kNN-Latenz
- „Genauigkeit vs. Erklärbarkeit": konkrete Zitate für beide Szenarien ergänzt
- Alle `→` durch `$\rightarrow$` ersetzt (Roboto Slab hat kein Unicode-Pfeilzeichen)
- `$\sim$`-Prozentangaben durch `ca.` ersetzt (kein Math-Glyph-Problem mehr)

**Änderungen an `handout.tex`:**
- Phase-5-Abschnitt: je ein Erklärungsabsatz für Entscheidungsbaum, Random Forest, kNN (mit Analogie)
- Vergleichstabelle: vierte Spalte „Vorfilter?" ergänzt
- Glossar: drei neue Einträge (Entscheidungsbaum, Random Forest, kNN)
- Roboto Flex als Fallback-Font für fehlende Zeichen in Roboto Slab (`directlua` + `RawFeature`)

---

## 2026-04-19 — Präsentation nach Rahmen-Story überarbeitet

`praesentation.md` grundlegend überarbeitet:
- „Das ist euer Netzwerk" → „Cisco NGFW schützt euer Netzwerk": Fokus auf DPI statt Topologie
- „Eine Woche im Netzwerk" → „Das Problem: DDoS überlastet die Firewall": Überlastungskette mit Alert Fatigue
- „Die zentrale Frage" → „Die Idee: ML als Vorfilter": ML-Modell als Entlastung vor DPI, konkrete Architektur
- Neue Folie „Regelbasiert vs. maschinell lernen": GOFA vs. ML, basierend auf `MaschinellesLernen.drawio.svg`
- Feature-Namen auf CICIDS-Folie korrigiert (echte CSV-Spaltennamen)
- Abschlussfolien auf Cisco-Entlastungs-Narrativ ausgerichtet
- Schlusszitat durch Rückbezug auf Cisco Secure Network Analytics ersetzt
- Beide PDFs (`praesentation.pdf`, `handout.pdf`) neu gebaut; Schrift Roboto → Roboto Flex

---

## 2026-04-16 — Initiale Erstellung

**Ingested Quellen:**
- `Examples.md` — Orange-Workflow-Beispiele (allgemein)
- `Orange Data Mining.md` — Orange-Klassifikations-Beispiele
- `Widget Catalog.md` — Vollständiger Widget-Katalog
- `IDS 2017 Datasets Research Canadian Institute for Cybersecurity.md` — CICIDS2017
- `UNSW-NB15 Augmented Dataset Datasets Research Canadian Institute for Cybersecurity.md` — CIC-UNSW-NB15
- `BETH Dataset.md` — BETH (Kaggle)
- `IDS 2018 Datasets Research Canadian Institute for Cybersecurity.md` — CIC-IDS-2018

**Besprechung vor dem Schreiben:**
- Zielgruppe: Cisco-Academy-Lehrkräfte, berufliche Schulen, keine KI-Vorkenntnisse
- CICIDS2017 als primärer Datensatz gewählt (On-Premise-Szenario auf Nutzerwunsch)
- BETH ausgeschlossen (host-basiert, Cloud, falsche Domäne)
- CIC-IDS-2018 ausgeschlossen (AWS, kein On-Premise)
- Roter Faden: „Eine Arbeitswoche als Netzwerkadmin – erkennt euer IDS die Angriffe?"

## 2026-04-16 — Teilnehmer-Handout erstellt

`Workshop_Handout.md` erstellt: A4, 2 Seiten (Vorder-/Rückseite).
Enthält: Szenario-Einführung, Orange-Kurzanleitung, Feature-Tabelle mit echten Datenwerten, Begriffsglossar, Diskussionsfragen, Ressourcen.

---

## 2026-04-16 — Workflow getestet und funktionsfähig

`workshop_workflow.ows` vollständig konfiguriert und getestet. Alle Widgets (Scatter Plot, Tree Viewer, Test & Bewertung, Confusion Matrix) laufen fehlerfrei.

---

## 2026-04-16 — Datensatz als .tab neu erstellt, Workflow aktualisiert

`workshop_ids.csv` ersetzt durch `workshop_ids.tab` (Orange-natives Format mit 3-Zeilen-Header: Variablenname, Typ, Rolle). Label wird jetzt automatisch als Zielvariable erkannt – kein Select-Columns-Widget nötig.

---

## 2026-04-16 — Orange-Workflow erstellt

**`Datensätze/workshop_workflow.ows`** erstellt (11 Widgets, 13 Verbindungen).
Enthält: Datensatz laden, Datentabelle, 2× Scatter Plot, Train/Test-Split, Entscheidungsbaum, Baum-Visualisierung, Test & Bewertung, Confusion Matrix, Random Forest, kNN.
Manuell in Orange noch zu konfigurieren: Dateipfad im File-Widget, Scatter-Plot-Achsen, Baum-Tiefe.

---

## 2026-04-16 — Datensatz-Subset erstellt und analysiert

**`Datensätze/workshop_ids.csv`** erstellt:
- 5.000 BENIGN (Monday) + 5.000 DDoS (Friday Afternoon), seed=42
- 11 Features, Inf/NaN bereinigt
- Beste Scatter-Plot-Achsen empirisch bestätigt: `Packet Length Mean` vs. `Down/Up Ratio`
- Key Finding: DDoS-Flows haben `Down/Up Ratio = 0` (Opfer antwortet nicht), Paketgröße 14× größer als BENIGN

**Aktualisierte Seiten**: `CICIDS2017.md`, `Orange_Klassifikations_Workflow.md`, `Workshop_Arbeitsplan.md`

---

## 2026-04-16 — Workshop-Arbeitsplan erstellt

**Neu erstellte Seiten:**
- `Workshop_Arbeitsplan.md` — vollständiger Verlaufsplan mit Minutenplanung, Contingency und Kernbotschaften
- `Index.md` aktualisiert

---

## 2026-04-19 — Cisco-Sicherheitsarchitektur ergänzt

- `Cisco_Sicherheitsarchitektur.md` neu erstellt: Firepower, Stealthwatch, ASA; Überlastungsproblem bei DDoS; Traffic Triage; Vergleich Workshop-Konzept ↔ Stealthwatch; didaktische Anschlussfragen
- `Workshop_Konzept.md`: Link auf neue Seite ergänzt
- `Index.md`: neue Seite eingetragen

---

## 2026-04-18 — ASCII-Diagramme durch Mermaid ersetzt

- `On_Premise_Netzwerktopologie.md`: Netzwerktopologie → `graph TD` mit Angreifer/Opfer-Subgraphen
- `Orange_Klassifikations_Workflow.md`: Gesamtworkflow → `flowchart TD`; Scatter-Plot-Illustration → `quadrantChart`; Entscheidungsbaum-Beispiel → `graph TD`; Confusion-Matrix-ASCII → Markdown-Tabelle; vollständige Widget-Verbindungen → `flowchart LR`
- `Workshop_Handout.md`: Workflow-Kurzanleitung → `flowchart LR`
- Hinweis: Umlaute in unquoted Mermaid-Kontexten (z. B. `quadrantChart`-Labels) vermeiden

---

## 2026-04-18 — Offene Schritte geprüft und nachgezogen

- `workshop_workflow_phase1.ows` erstellt (fehlte trotz Referenz in Präsentation und Arbeitsplan)
- Scatter-Plot-Achsenbezeichnungen in `praesentation.md` korrigiert: Kurznamen (`pkt_len_avg`, `down_up_ratio`) durch echte CSV-Spaltennamen (`Packet Length Mean`, `Down/Up Ratio`) ersetzt
- Checkliste in `Workshop_Arbeitsplan.md` aktualisiert: erledigte Punkte als `[x]` markiert, Hinweis „noch zu erstellen" beim Handout entfernt

---

## 2026-04-16 — Initiale Wiki-Erstellung

**Neu erstellte Seiten:**
- `Index.md`, `Log.md`
- `Workshop_Konzept.md`
- `CICIDS2017.md`
- `CIC_UNSW_NB15.md`
- `CIC_IDS_2018.md`
- `BETH_Dataset.md`
- `Orange_Data_Mining.md`
- `CICFlowMeter_Features.md`
- `On_Premise_Netzwerktopologie.md`
- `Orange_Klassifikations_Workflow.md`
- `Angriffsszenarien.md`
