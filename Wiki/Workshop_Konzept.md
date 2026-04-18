# Workshop-Konzept

**Zusammenfassung**: Planung eines 90-minütigen Einführungsworkshops zu Data Mining und KI für Cisco-Academy-Lehrkräfte an beruflichen Schulen, mit Orange Data Mining und dem CICIDS2017-Datensatz.

**Quellen**: Diskussion mit Nutzer (2026-04-16)

**Zuletzt aktualisiert**: 2026-04-16

---

## Zielgruppe

- Lehrkräfte an beruflichen Schulen im Bereich Netzwerktechnik
- Cisco-Academy-Hintergrund: vertraute Konzepte sind TCP/IP, Routing, Switching, Firewalls, IDS/IPS, Angriffsvektoren
- **Keine Vorkenntnisse** in Data Mining, maschinellem Lernen oder Statistik
- Hohe Motivation durch Domänennähe (Netzwerksicherheit)

## Ziele

1. KI-Methoden und Data Mining **verständlich** machen (kein Expertenwissen erforderlich)
2. **Interesse wecken** – die Teilnehmer sollen den Workshop als relevant für ihren Unterricht erleben
3. Ein konkretes Werkzeug (Orange) und einen konkreten Datensatz (CICIDS2017) kennenlernen
4. Den Transfer in den eigenen Unterricht anstoßen

## Roter Faden: Die Arbeitswoche als Netzwerkadmin

Das Szenario: **On-Premise-Unternehmensnetzwerk**, eine typische Arbeitswoche.

> „Ihr seid Netzwerkadministratoren. Das ist euer Netzwerk. Diese Woche ist einiges passiert – kann ein KI-Modell die Angriffe erkennen?"

Diese Erzählung hat mehrere Vorteile:
- Sofortiger Wiedererkennungseffekt (Cisco-Topologie, bekannte Angriffstypen)
- Klare Dramaturgie: normaler Montag → eskalierender Freitag
- Die Frage „Wie gut ist das Modell?" ist direkt anschlussfähig an Unterrichtsthemen (Alert Fatigue, False Positives)

## Datensatz

[[CICIDS2017]] – On-Premise-Labor mit realistischer Unternehmenstopologie.

Empfohlener Subset für den Workshop:
- **Montag** (benign) + **Freitag Nachmittag** (DDoS LOIT) = binäre Klassifikation
- Ca. 5.000–10.000 Zeilen, 10–12 ausgewählte [[CICFlowMeter_Features]]
- Vorbereitet als CSV, direkt in Orange ladbar

## Werkzeug

[[Orange_Data_Mining]] – visuelles, flow-basiertes Data-Mining-Tool, kein Programmieren nötig.

## Vorgeschlagener Ablauf (90 Minuten)

| Phase | Zeit | Inhalt | Orange-Widgets |
|---|---|---|---|
| **1. Einstieg** | 10 min | Was ist Data Mining? Warum KI für Netzwerksicherheit? | — |
| **2. Daten erkunden** | 15 min | Datensatz laden, Tabelle, erste Visualisierung | File, Data Table, Scatter Plot |
| **3. Klassifikation** | 25 min | Entscheidungsbaum trainieren, Ergebnis visualisieren | Tree, Tree Viewer, Scatter Plot |
| **4. Bewertung** | 20 min | Wie gut ist das Modell? Confusion Matrix, False Positives | Test and Score, Confusion Matrix |
| **5. Vergleich** | 10 min | Random Forest vs. Entscheidungsbaum | Random Forest, Test and Score |
| **6. Diskussion** | 10 min | Was bedeuten False Positives im IDS-Kontext? Transfer | — |

## Didaktische Hinweise

- **Phase 2 ist entscheidend**: Die Teilnehmer müssen den Datensatz verstehen, bevor sie ein Modell bauen. Leitfrage: „Was seht ihr im Scatter Plot?"
- **Tree Viewer ist der Aha-Moment**: Der Entscheidungsbaum zeigt lesbare Regeln – das macht KI greifbar.
- **Confusion Matrix als Brücke**: False Positive = Fehlalarm im IDS. Diesen Begriff kennen alle Teilnehmer.
- **Zeitpuffer einplanen**: Orange-Installation kann auf Workshop-Rechnern Zeit kosten → vorab prüfen.

## Offene Fragen / Nächste Schritte

- Subset aus CICIDS2017 vorbereiten (Feature-Auswahl, Sampling) → verifizierungsbedürftig
- Orange-Version und Kompatibilität prüfen → verifizierungsbedürftig
- Handout / Arbeitsblatt erstellen → offen

## Verwandte Seiten

- [[CICIDS2017]]
- [[Orange_Data_Mining]]
- [[Orange_Klassifikations_Workflow]]
- [[Angriffsszenarien]]
- [[On_Premise_Netzwerktopologie]]
