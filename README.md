# KI erkennt Netzwerkangriffe – Workshop mit Orange Data Mining

Materialien für einen **90-minütigen Workshop** für Lehrkräfte an beruflichen Schulen (Cisco Academy) zum Thema maschinelles Lernen und Netzwerksicherheit.

Entwickelt an der [Akademie für Lehrerfortbildung und Personalführung Dillingen](https://alp.dillingen.de).

---

## Inhalt

```
Datensätze/
  workshop_ids.tab              Datensatz-Subset (10 000 Flows, 11 Features, BENIGN vs. DDoS)
  workshop_workflow.ows         Vollständiger Orange-Workflow (alle Phasen)
  workshop_workflow_phase1.ows  Einstiegs-Workflow (Daten erkunden)
Folien/
  praesentation.md              Folienquelle (Pandoc/Beamer)
  praesentation.pdf             Fertige Präsentation
Wiki/
  Workshop_Arbeitsplan.md       Verlaufsplan mit Minutenplanung und Trainer-Hinweisen
  Workshop_Handout.md           Teilnehmer-Handout (A4, 2 Seiten)
  ...                           Weitere Hintergrundseiten zu Datensatz, Algorithmen, Angriffen
```

## Szenario

Ein On-Premise-Unternehmensnetzwerk mit Cisco NGFW/ASA ist Ziel eines DDoS-Angriffs. Die Firewall nutzt Deep Packet Inspection (DPI) – bei Tausenden Flows pro Sekunde steigt die CPU auf 100 %, die DPI bricht zusammen, und echte Angriffe bleiben unbemerkt (**Alert Fatigue**).

**Die Idee:** Ein ML-Modell analysiert nur Flow-Metriken (kein Payload) und sortiert den Traffic vor:

- Eindeutig BENIGN → durchlassen
- Eindeutig DDoS → blockieren
- Unklar → weiter an die NGFW zur DPI

Ein einfacher Entscheidungsbaum mit 2–3 Regeln erreicht dabei ca. 98 % Genauigkeit. Nur noch 10–20 % des Traffics muss die DPI-Stufe passieren.

## Ablauf (90 Minuten, strukturiert nach CRISP-DM)

| Phase | Zeit | CRISP-DM | Inhalt |
|-------|------|----------|--------|
| Einstieg | 10 min | Business Understanding | Cisco NGFW, DDoS-Problem, ML als Vorfilter, Lernziele |
| Daten erkunden | 15 min | Data Understanding | Datensatz laden, Data Table, Scatter Plot, Struktur erkennen |
| Entscheidungsbaum | 25 min | Modeling | Modell trainieren, Tree Viewer, Regeln lesen |
| Modellbewertung | 20 min | Evaluation | Accuracy, Confusion Matrix, Precision, Recall, Alert Fatigue |
| Modellvergleich | 10 min | Evaluation | Random Forest vs. kNN vs. Entscheidungsbaum |
| Abschluss | 10 min | Deployment | Transfer in den Unterricht, Materialien, Feedback |

## Kernkonzepte

### Regelkonfiguration vs. maschinelles Lernen

| | Regelkonfiguration (Signaturpflege) | Machine Learning |
|---|---|---|
| Regeln | Experte schreibt per Hand | Algorithmus lernt aus Daten |
| Neue Angriffe | Manuelles Signatur-Update nötig | Neue Trainingsdaten genügen |
| Beispiel | Cisco-IPS-Signaturen | Entscheidungsbaum aus CICIDS2017 |

**Die Kernformel:** Regelkonfiguration: Mensch → Regeln → Ergebnisse. ML: Daten + Ergebnisse → Maschine → Regeln.

### Modellvergleich

| Modell | Accuracy | Regeln lesbar? | Als Vorfilter? |
|--------|----------|----------------|----------------|
| Entscheidungsbaum | ca. 97–98 % | Ja – jede Regel nachvollziehbar | Ja – erklärbar |
| Random Forest | ca. 99 % | Nein – 100 Bäume, nicht lesbar | Ja – genauer |
| k-Nearest Neighbors | ca. 95–97 % | Bedingt – Nachbarn zeigbar | Nein – zu langsam |

### Precision vs. Recall im IDS-Kontext

- **False Positive** (Fehlalarm) → Admins bearbeiten unnötige Tickets → Alert Fatigue → echter Angriff wird übersehen
- **False Negative** (übersehener Angriff) → Angreifer operiert unbemerkt

Hohe Precision und hoher Recall gleichzeitig zu maximieren ist nicht möglich. Welches Übel schwerer wiegt, ist eine **fachliche**, keine technische Entscheidung.

## Datensatz

Subset aus **CICIDS2017** (Canadian Institute for Cybersecurity):
- 5 000 BENIGN-Flows (Montag) + 5 000 DDoS-Flows (Freitag)
- 11 Features: u. a. `Flow Bytes/s`, `Packet Length Mean`, `Down/Up Ratio`, `SYN Flag Count`
- Bereinigt (kein NaN/Inf), reproduzierbares Sampling (seed=42)
- Format: Orange `.tab` mit automatischer Zielvariablen-Erkennung

Die vollständigen Rohdaten sind öffentlich verfügbar unter [cicresearch.ca](https://cicresearch.ca).

## Lernziele

Nach dem Workshop können die Teilnehmer …

1. erläutern, was **maschinelles Lernen** ist und wie es sich von **vom Menschen vorgenommener Regelkonfiguration (Signaturpflege)** unterscheidet
2. erklären, wie **ML-Vorfilterung** Cisco-Geräte bei DDoS entlasten kann
3. beschreiben, wie ein **Entscheidungsbaum** Netzwerktraffic klassifiziert
4. beurteilen, was **Accuracy, False Positives** und **False Negatives** im IDS-Kontext bedeuten
5. einschätzen, was den Unterschied zwischen einem **interpretierbaren** und einem **Black-Box-Modell** ausmacht
6. **Orange Data Mining** für einen einfachen Klassifikations-Workflow nutzen
7. das heutige Vorgehen den **sechs Phasen von CRISP-DM** zuordnen

## Voraussetzungen

- [Orange Data Mining](https://orangedatamining.com) (kostenlos, Windows/Mac/Linux)
- Keine Programmierkenntnisse erforderlich

## Lizenz

Die Workshop-Materialien stehen unter [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.de).  
Der Datensatz `workshop_ids.tab` basiert auf CICIDS2017 (University of New Brunswick).
