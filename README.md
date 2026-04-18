# KI erkennt Netzwerkangriffe – Workshop mit Orange Data Mining

Materialien für einen **90-minütigen Workshop** für Lehrkräfte an beruflichen Schulen (Cisco Academy) zum Thema maschinelles Lernen und Netzwerksicherheit.

Entwickelt an der [Akademie für Lehrerfortbildung und Personalführung Dillingen](https://alp.dillingen.de).

---

## Inhalt

```
Datensätze/
  workshop_ids.tab          Datensatz-Subset (10 000 Flows, 11 Features, BENIGN vs. DDoS)
  workshop_workflow.ows     Vollständiger Orange-Workflow (alle Phasen)
  workshop_workflow_phase1.ows  Einstiegs-Workflow (Daten erkunden)
Folien/
  praesentation.md          Folienquelle (Pandoc/Beamer)
  praesentation.pdf         Fertige Präsentation
Wiki/
  Workshop_Arbeitsplan.md   Verlaufsplan mit Minutenplanung und Trainer-Hinweisen
  Workshop_Handout.md       Teilnehmer-Handout (A4, 2 Seiten)
  ...                       Weitere Hintergrundseiten zu Datensatz, Algorithmen, Angriffen
```

## Szenario

Die Teilnehmer schlüpfen in die Rolle von Netzwerkadministratoren. Eine simulierte Arbeitswoche in einem On-Premise-Unternehmensnetzwerk (Firewall, Switch, 10 Clients, 2 Server) liefert den Rahmen:

| Tag | Ereignis |
|-----|----------|
| Mo | Normalbetrieb – 25 simulierte Nutzer |
| Di | Brute Force (FTP/SSH) |
| Mi | DoS-Angriffe (Slowloris, Hulk, Heartbleed) |
| Do | Web Attack, XSS, SQL Injection |
| Fr | Botnet, Port Scan, **DDoS LOIT** |

**Zentrale Frage**: Kann ein KI-Modell normalen Traffic von DDoS-Angriffen unterscheiden – ohne Payload-Inspektion, nur anhand von Flow-Metriken?

## Ablauf (90 Minuten)

| Phase | Zeit | Inhalt |
|-------|------|--------|
| Einstieg | 10 min | Szenario, Lernziele, Vorwissen aktivieren |
| Daten erkunden | 15 min | Datensatz laden, Scatter Plot, Struktur erkennen |
| Entscheidungsbaum | 25 min | Modell trainieren, Tree Viewer, Regeln lesen |
| Modellbewertung | 20 min | Accuracy, Confusion Matrix, False Positives diskutieren |
| Modellvergleich | 10 min | Random Forest vs. Entscheidungsbaum |
| Abschluss | 10 min | Transfer in den Unterricht, Feedback |

## Datensatz

Subset aus **CICIDS2017** (Canadian Institute for Cybersecurity):
- 5 000 BENIGN-Flows (Montag) + 5 000 DDoS-Flows (Freitag)
- 11 Features, bereinigt (kein NaN/Inf), reproduzierbares Sampling (seed=42)
- Format: Orange `.tab` mit automatischer Zielvariablen-Erkennung

Die vollständigen Rohdaten sind öffentlich verfügbar unter [cicresearch.ca](https://cicresearch.ca).

## Voraussetzungen

- [Orange Data Mining](https://orangedatamining.com) (kostenlos, Windows/Mac/Linux)
- Keine Programmierkenntnisse erforderlich

## Lernziele

Nach dem Workshop können die Teilnehmer …

1. erklären, was Data Mining und maschinelles Lernen bedeuten
2. beschreiben, wie ein Entscheidungsbaum Netzwerktraffic klassifiziert
3. beurteilen, was Accuracy, False Positives und False Negatives im IDS-Kontext bedeuten
4. den Unterschied zwischen interpretierbaren und Black-Box-Modellen einschätzen
5. Orange Data Mining für einen einfachen Klassifikations-Workflow nutzen

## Lizenz

Die Workshop-Materialien stehen unter [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.de).  
Der Datensatz `workshop_ids.tab` basiert auf CICIDS2017 (University of New Brunswick).
