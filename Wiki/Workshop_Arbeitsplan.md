# Workshop-Arbeitsplan

**Zusammenfassung**: Vollständiger, druckfertiger Arbeitsplan für den 90-minütigen Workshop „KI erkennt Netzwerkangriffe – Einführung in Data Mining mit Orange".

**Quellen**: (Quelle: [[Workshop_Konzept.md]]), (Quelle: [[Orange_Klassifikations_Workflow.md]])

**Zuletzt aktualisiert**: 2026-04-16

---

## Eckdaten

| | |
|---|---|
| **Titel** | KI erkennt Netzwerkangriffe – Einführung in Data Mining mit Orange |
| **Zielgruppe** | Lehrkräfte an beruflichen Schulen, Fachrichtung Netzwerktechnik / Cisco Academy |
| **Vorkenntnisse** | Netzwerktechnik (TCP/IP, Firewalls, IDS/IPS) – keine KI-/Data-Mining-Kenntnisse |
| **Dauer** | 90 Minuten |
| **Gruppengröße** | 10–25 Personen |
| **Arbeitsform** | Plenum mit Live-Demo + geführte Eigenarbeit am Rechner |

---

## Lernziele

Die Teilnehmer können nach dem Workshop…

1. **erklären**, was Data Mining und maschinelles Lernen bedeuten (konzeptuell, ohne Formeln)
2. **beschreiben**, wie ein Entscheidungsbaum Netzwerktraffic klassifiziert
3. **beurteilen**, was Accuracy, False Positives und False Negatives im IDS-Kontext bedeuten
4. **einschätzen**, was der Unterschied zwischen einem interpretierbaren und einem Black-Box-Modell ist
5. **Orange Data Mining** für einen einfachen Klassifikations-Workflow nutzen

---

## Vorbereitungscheckliste (mind. 3 Tage vorher)

### Datensatz
- [x] CICIDS2017-Datensatz herunterladen: Monday CSV + Friday CSV (Quelle: cicresearch.ca)
- [x] Subset erstellen: nur Klassen `BENIGN` und `DDoS attacks-LOIC-HTTP` behalten
- [x] Auf ca. 5.000 Zeilen je Klasse reduzieren (zufälliges Sampling, reproduzierbar mit seed=42)
- [x] Feature-Auswahl: 11 Spalten (`Flow Duration`, `Total Fwd Packets`, `Total Backward Packets`, `Flow Bytes/s`, `Flow Packets/s`, `FIN/SYN/ACK Flag Count`, `Packet Length Mean`, `Down/Up Ratio`, `Average Packet Size`, `Label`)
- [x] Datei gespeichert als `workshop_ids.tab` (Orange-natives Format, 3-Zeilen-Header) — Label wird automatisch als Zielvariable erkannt
- [ ] Test: Datei in Orange laden und Scatter-Plot-Ergebnis visuell prüfen
- [x] Label-Spalte als Zielvariable gesetzt (`.tab`-Format, 3. Headerzeile: `class`)

### Orange-Workflow
- [x] `workshop_workflow.ows` fertig aufgebaut (11 Widgets, 13 Verbindungen)
- [x] Workflow enthält: File, Data Table, Scatter Plot, Data Sampler, Tree, Tree Viewer, Test and Score, Confusion Matrix, Scatter Plot (Fehler), Random Forest, kNN
- [x] Scatter Plot vorkonfiguriert: X=`Packet Length Mean`, Y=`Down/Up Ratio`, Farbe=`Label`
- [x] Tree vorkonfiguriert: max_depth=5, min_leaf=50
- [x] `workshop_workflow_phase1.ows` erstellt (nur File + Data Table + Scatter Plot)
- [ ] Dateipfad im File-Widget auf Teilnehmer-Rechnern anpassen (oder universellen Pfad verwenden)

### Technik
- [ ] Orange Data Mining auf allen Teilnehmer-Rechnern installiert (orangedatamining.com, aktuellste Version)
- [ ] `workshop_ids.tab`, `workshop_workflow.ows` und `workshop_workflow_phase1.ows` auf alle Rechner kopiert oder per USB/Link bereitgestellt
- [ ] Beamer/Projektionsfläche testen
- [ ] Fallback vorbereiten: Eigener Rechner + Projektor, falls Teilnehmer-Rechner Probleme machen

### Unterlagen
- [x] Handout erstellt: [[Workshop_Handout]] (A4, 2 Seiten)
- [ ] Handout ausdrucken (1× pro Teilnehmer)
- [ ] Netzwerkdiagramm des CICIDS2017-Labs ausdrucken oder auf Folie (aus [[On_Premise_Netzwerktopologie]])

---

## Materialien

| Material | Menge | Hinweis |
|---|---|---|
| `workshop_ids.csv` | 1× je Rechner | Datensatz-Subset |
| `workshop_workflow.ows` | 1× je Rechner | Vorgefertigter Orange-Workflow |
| Handout | 1× je TN | Kurzanleitung + Diskussionsfragen |
| Beamer/Projektor | 1× | Für Live-Demo |
| Netzwerkdiagramm (Folie/Druck) | 1× | Szenario-Einstieg |

---

## Verlaufsplan

### Phase 1 – Einstieg (0–10 min)

**Ziel**: Neugier wecken, Szenario etablieren, Relevanz herstellen

| Minute | Trainer-Handlung | Teilnehmer-Aktivität | Medium |
|---|---|---|---|
| 0–3 | Begrüßung. Szenario einführen: Netzwerkdiagramm zeigen. „Das ist euer Netzwerk. Letzte Woche ist einiges passiert." | Zuhören, Netzwerk identifizieren | Projektor: Netzwerkdiagramm |
| 3–7 | Angriffswoche beschreiben (Mo = normal, Di–Fr = Angriffe). Frage stellen: „Wie würdet ihr das klassisch erkennen? Und was, wenn 10.000 Flows pro Sekunde kommen?" | Antworten, diskutieren | Mündlich |
| 7–10 | Überleitung: „Genau das macht KI – und wir schauen heute, wie." Lernziele nennen. Ablauf vorstellen. | Zuhören | Projektor: Folie mit Ablauf |

**Leitfragen für den Einstieg:**
- „Wie viele von euch haben schon von Machine Learning gehört?"
- „Was glaubt ihr: Kann ein Algorithmus einen DDoS-Angriff erkennen, ohne den Payload zu lesen?"
- „Was wäre der Vorteil gegenüber klassischer Signaturerkennung?"

---

### Phase 2 – Daten erkunden (10–25 min)

**Ziel**: Datensatz verstehen, erkennen dass Daten eine Struktur haben, erste Visualisierung

| Minute | Trainer-Handlung | Teilnehmer-Aktivität | Medium / Widget |
|---|---|---|---|
| 10–12 | Orange öffnen. `workshop_workflow_phase1.ows` laden (nur File + Data Table + Scatter Plot). `workshop_ids.csv` einlesen. | Gleiche Datei auf eigenem Rechner laden | Orange: **File** |
| 12–15 | Data Table öffnen. Erklären: „Jede Zeile ist ein Netzwerkflow. Was bedeutet `tot_fw_pk`? Was bedeutet `Label`?" Durch Spalten scrollen, Werte zeigen. | Eigene Data Table ansehen, Fragen stellen | Orange: **Data Table** |
| 15–20 | Scatter Plot öffnen. X = `Packet Length Mean`, Y = `Down/Up Ratio`, Farbe = `Label`. Ergebnis zeigen lassen. | Gleiche Einstellungen vornehmen, Ergebnis beobachten | Orange: **Scatter Plot** |
| 20–25 | Diskussion: „Was seht ihr?" → Zwei Cluster. „Was bedeutet `Down/Up Ratio = 0`?" → Opfer antwortet nicht mehr. „Was könnte ein Algorithmus damit machen?" | Beobachten, antworten, Fragen stellen | Mündlich |

**Erwartetes Ergebnis im Scatter Plot** (aus echten Daten `workshop_ids.csv`):
```
Down/Up Ratio
    1.0  │  · · · Benign   (kleine Pakete ø 60 Byte, Antworten kommen zurück)
         │  · ·  ·
         │
    0.0  │              ████ DDoS (große HTTP-Pakete ø 833 Byte, keine Antwort)
─────────┼───────────────────────────────── Packet Length Mean
        60                               833
```
**Didaktischer Kern**: `Down/Up Ratio = 0` bei DDoS – der Opfer-Server ist so überlastet, dass keine Antwort zurückkommt. Das ist für Cisco-Lehrkräfte sofort verständlich.

**Alternative Achsenkombination** für Vertiefung: X = `Packet Length Mean`, Y = `Flow Duration`
(DDoS: lange Flows ~1,9 Sek. Median, Benign: kurze Flows ~0,03 Sek. Median)

**Sicherung Phase 2:**
> „Daten haben eine Struktur. Diese Struktur ist für uns sichtbar – und genau die lernt ein Modell."

---

### Phase 3 – Entscheidungsbaum (25–50 min)

**Ziel**: Modell trainieren, Ergebnis interpretieren, KI greifbar machen

| Minute | Trainer-Handlung | Teilnehmer-Aktivität | Medium / Widget |
|---|---|---|---|
| 25–28 | Vollständigen Workflow laden: `workshop_workflow.ows`. Erklären: „Wir brauchen Trainings- und Testdaten – wie beim Lernen für eine Prüfung." Data Sampler vorstellen. | Workflow laden | Orange: **Data Sampler** |
| 28–32 | Tree-Widget erklären: „Das Modell lernt Entscheidungsregeln aus den Trainingsdaten." Tree mit Data Sampler verbinden, trainieren lassen. | Beobachten | Orange: **Tree** |
| 32–40 | Tree Viewer öffnen. Baum zeigen. **Wichtig: Baum erklären.** Erste Verzweigung laut vorlesen: „Wenn `fl_byt_s > X`, dann sehr wahrscheinlich DDoS." Frage: „Ergibt das für euch Sinn?" | Eigenen Tree Viewer öffnen, Baum lesen | Orange: **Tree Viewer** |
| 40–45 | Tree Viewer + Scatter Plot verknüpfen. Knoten im Baum anklicken → Punkte im Scatter Plot leuchten. | Gleiche Interaktion nachvollziehen | Orange: **Tree Viewer + Scatter Plot** |
| 45–50 | Diskussion: „Was ist KI? Ist das Magie?" → Nein, es sind gelernte Regeln. „Kann jeder diese Regeln verstehen?" → Ja, der Baum ist lesbar. | Antworten, diskutieren | Mündlich |

**Trainer-Hinweis zum Tree Viewer:**
Der Baum kann bei maximaler Tiefe sehr groß werden. Vor dem Workshop Tree-Parameter setzen:
- Max. Tiefe: 4–5 (gut lesbar)
- Min. Instanzen pro Knoten: 50 (verhindert Überanpassung)

**Sicherung Phase 3:**
> „Ein Entscheidungsbaum ist ein KI-Modell, das wir lesen und erklären können. Das ist wichtig – denn im echten Einsatz müssen wir erklären können, warum das System einen Alarm auslöst."

---

### Phase 4 – Modellbewertung (50–70 min)

**Ziel**: Güte des Modells messen, False Positives im IDS-Kontext verstehen

| Minute | Trainer-Handlung | Teilnehmer-Aktivität | Medium / Widget |
|---|---|---|---|
| 50–55 | Test and Score vorstellen. „Wie gut ist unser Modell wirklich?" Cross-Validation erklären (kurz: „Wir testen das Modell auf Daten, die es nicht gesehen hat"). Accuracy zeigen. | Eigene Ergebnisse anschauen | Orange: **Test and Score** |
| 55–60 | Accuracy-Zahl diskutieren: „98% – ist das gut?" Frage: „Was bedeutet 2% Fehler bei 10.000 Flows?" → 200 falsche Entscheidungen. „Was davon sind Fehlalarme, was sind übersehene Angriffe?" | Rechnen, diskutieren | Mündlich |
| 60–65 | Confusion Matrix öffnen und erklären. Vier Felder beschriften: True Positive, True Negative, False Positive (Fehlalarm), False Negative (übersehener Angriff). | Eigene Matrix anschauen | Orange: **Confusion Matrix** |
| 65–70 | Interaktion: False Positives in Confusion Matrix auswählen → Scatter Plot zeigt diese Punkte. „Wo liegen sie?" → An der Klassengrenze. Diskussion: „FP vs. FN – was ist schlimmer im IDS?" | Auswahl vornehmen, beobachten, diskutieren | Orange: **Confusion Matrix + Scatter Plot** |

**Kernbotschaft dieser Phase:**
> „Alert Fatigue": Zu viele False Positives → Administratoren ignorieren Alarme → echte Angriffe werden übersehen. Das ist ein reales Problem in echten SOC-Teams.

**Diskussionsfragen:**
- „Wie viele False Positives sind für euer Netzwerk tolerierbar?"
- „Was wäre die Konsequenz eines False Negative bei Heartbleed?"
- „Wie unterscheidet sich das von Signaturerkennung?"

**Sicherung Phase 4:**
> „Kein Modell ist perfekt. Wir müssen entscheiden, ob wir lieber Fehlalarme oder übersehene Angriffe akzeptieren – das ist eine fachliche, keine technische Entscheidung."

---

### Phase 5 – Modellvergleich (70–80 min)

**Ziel**: Verschiedene Algorithmen kennenlernen, Abwägung Genauigkeit vs. Interpretierbarkeit

| Minute | Trainer-Handlung | Teilnehmer-Aktivität | Medium / Widget |
|---|---|---|---|
| 70–74 | Random Forest kurz erklären: „Viele Bäume abstimmen – wie ein Komitee." kNN kurz erklären: „Welche Klasse haben die ähnlichsten bekannten Fälle?" Beide Widgets mit Test and Score verbinden. | Widgets verbinden | Orange: **Random Forest, kNN** |
| 74–78 | Test and Score zeigt nun alle drei Modelle nebeneinander. Ergebnisse vergleichen. | Ergebnisse vergleichen | Orange: **Test and Score** |
| 78–80 | Diskussion: „Random Forest ist besser – aber können wir die Regeln lesen?" → Nein. „Was bedeutet das für den Einsatz in einem Unternehmen?" | Antworten, diskutieren | Mündlich |

**Erwartete Ergebnisse (ungefähre Richtwerte):**
| Modell | Accuracy | Interpretierbarkeit |
|---|---|---|
| Entscheidungsbaum | ~97–98% | ✅ Hoch |
| Random Forest | ~99% | ❌ Gering (Black Box) |
| kNN | ~95–97% | ⚠️ Mittel |

**Sicherung Phase 5:**
> „Die Wahl des Modells ist nicht nur eine technische Frage. Im Unterricht und im echten Einsatz zählt: Kann ich das Ergebnis erklären und verteidigen?"

---

### Phase 6 – Abschluss und Transfer (80–90 min)

**Ziel**: Erkenntnisse sichern, Transfer in den Unterricht anstoßen

| Minute | Trainer-Handlung | Teilnehmer-Aktivität | Medium |
|---|---|---|---|
| 80–84 | Zusammenfassung: Was haben wir gemacht? Lernziele rekapitulieren. Kernbotschaften wiederholen. | Zuhören, ergänzen | Mündlich / Folie |
| 84–88 | Transfer-Diskussion: „Wie könntet ihr das in eurem Unterricht einsetzen?" Impulse geben (s. u.). | Ideen äußern | Mündlich |
| 88–90 | Ausblick: Was wäre der nächste Schritt? (Mehrklass., andere Datensätze, unüberwachtes Lernen) Materialien nennen. Feedback-Runde (1 Wort). | Feedback geben | Mündlich |

**Transfer-Impulse für Lehrkräfte:**
- „Orange ist kostenlos und funktioniert mit jedem CSV – auch eigene Schülerdaten möglich"
- „Entscheidungsbaum + Confusion Matrix passt in eine Doppelstunde"
- „CICIDS2017 ist öffentlich zugänglich – Schüler könnten eigene Subsets erkunden"
- „Das Netzwerkdiagramm aus dem Datensatz ist direkt im Cisco-Curriculum verwendbar"

---

## Puffer und Contingency-Planung

### Wenn zu wenig Zeit bleibt (–15 min)
- Phase 5 (Modellvergleich) **weglassen** – Kernbotschaft bleibt intakt
- Phase 4: Confusion Matrix zeigen, aber Interaktion mit Scatter Plot überspringen
- Phase 3: Tree Viewer ohne interaktive Scatter-Plot-Verknüpfung

### Wenn zu viel Zeit bleibt (+15 min)
- **Weitere Features im Scatter Plot** erkunden: `syn_cnt` vs. `ack_cnt` – was sieht man?
- **Box Plot** hinzufügen: Verteilung von `fl_byt_s` nach Klasse zeigen
- **Distributions-Widget** für einzelne Features öffnen
- **Mehrklassen-Versuch**: Kompletten Freitag-Datensatz laden (Botnet + Port Scan + DDoS) und Modell neu trainieren

### Wenn Technik versagt
- **Beamer-Ausfall**: Workshop als Frontal-Demo nur auf Trainer-Rechner fortführen, Diskussion stärken
- **Orange startet nicht**: Fertige Screenshots der Workflows zeigen (vorab als PDF exportieren)
- **CSV lädt falsch**: Backup-Version mit manuell gesetzten Spaltentypen bereithalten (`.ows` mit fest konfiguriertem File-Widget)

---

## Kernbotschaften (Zusammenfassung)

1. **KI = Mustererkennung in Daten** – kein Zaubern, sondern Statistik auf Netzwerkflows
2. **Entscheidungsbaum = erklärbare KI** – wir können die Regeln lesen und verteidigen
3. **Kein Modell ist perfekt** – False Positives und False Negatives sind unvermeidbar
4. **Die Wahl des Modells ist eine Fachentscheidung** – Genauigkeit allein reicht nicht
5. **Orange ist ein Werkzeug für den Unterricht** – kostenlos, visuell, kein Programmieren

---

## Verwandte Seiten

- [[Workshop_Konzept]]
- [[Orange_Klassifikations_Workflow]]
- [[Orange_Data_Mining]]
- [[CICIDS2017]]
- [[Angriffsszenarien]]
- [[On_Premise_Netzwerktopologie]]
- [[CICFlowMeter_Features]]
