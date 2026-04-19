# Wiki-Log

Unveränderliches Protokoll aller Wiki-Operationen.

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
