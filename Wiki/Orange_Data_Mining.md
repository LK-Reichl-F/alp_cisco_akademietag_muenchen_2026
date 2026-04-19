# Orange Data Mining

**Zusammenfassung**: Orange ist ein visuelles, flow-basiertes Data-Mining-Tool der Universität Ljubljana. Widgets werden per Drag-and-Drop verbunden – kein Programmieren erforderlich.

**Quellen**: (Quelle: [[Orange Data Mining]]), (Quelle: [[Examples.md]]), (Quelle: [[Widget Catalog.md]])

**Zuletzt aktualisiert**: 2026-04-16

---

## Was ist Orange?

Orange Data Mining ist eine Open-Source-Software für Datenanalyse, maschinelles Lernen und Visualisierung. Entwickelt am Bioinformatics Laboratory der Universität Ljubljana (Slowenien).

**Kernkonzept**: Datenflüsse zwischen **Widgets**. Jedes Widget hat Eingaben und Ausgaben. Man verbindet sie mit Pfeilen – das Ergebnis des einen Widget wird automatisch zum Input des nächsten.

Beispiel für einen einfachen Workflow:
```
[File] → [Data Table]
           ↓
        [Scatter Plot]
```

## Warum Orange für den Workshop?

- **Kein Programmieren**: Alle Operationen über grafische Oberfläche
- **Sofortige Rückmeldung**: Änderungen propagieren live durch den Workflow
- **Interaktiv**: Punkte im Scatter Plot auswählen → Auswahl erscheint in anderen Widgets
- **Kostenlos und Open Source**: Schüler/Lehrkräfte können es zu Hause installieren
- **Gut dokumentiert**: Offizielle Beispiele und Tutorials verfügbar

## Für den Workshop relevante Widget-Kategorien

### Data (Daten laden und ansehen)
| Widget | Funktion |
|---|---|
| **File** | CSV oder andere Daten laden |
| **Data Table** | Daten als Tabelle anzeigen |
| **Data Sampler** | Zufällige Teilmenge ziehen (für große Datensätze) |
| **Select Columns** | Features auswählen |
| **Select Rows** | Zeilen nach Bedingung filtern |

### Visualize (Visualisierungen)
| Widget | Funktion |
|---|---|
| **Scatter Plot** | Streudiagramm, interaktiv |
| **Distributions** | Verteilung einzelner Features |
| **Box Plot** | Vergleich von Klassen |
| **Heat Map** | Korrelationsmatrix |

### Model (Klassifikation)
| Widget | Funktion |
|---|---|
| **Tree** | Entscheidungsbaum |
| **Random Forest** | Ensemble aus Entscheidungsbäumen |
| **kNN** | k-Nearest-Neighbors |
| **Naive Bayes** | Probabilistischer Klassifikator |

### Visualize (Modelle)
| Widget | Funktion |
|---|---|
| **Tree Viewer** | Entscheidungsbaum grafisch anzeigen – sehr gut für Einsteiger |

### Evaluate (Modellbewertung)
| Widget | Funktion |
|---|---|
| **Test and Score** | Cross-Validation, Accuracy, AUC etc. |
| **Confusion Matrix** | Interaktive Fehlermatrix |

## Beispiel-Workflows aus den Quellen

### 1. Daten erkunden
`File → Data Table → Scatter Plot`
Grundlegender Einstieg: Daten laden, anschauen, visualisieren.
(Quelle: [[Examples.md]])

### 2. Klassifikationsbaum mit Visualisierung
`File → Tree → Tree Viewer`
`File → Tree → Scatter Plot` (Auswahl im Baum → Hervorhebung im Plot)
Interaktiver Klassifikationsbaum-Browser – ideal für den Workshop.
(Quelle: [[Orange Data Mining]])

### 3. Train/Test-Split
`File → Data Sampler → Tree → Test and Score`
Trainings- und Testdaten trennen, Modell bauen, bewerten.
(Quelle: [[Examples.md]])

### 4. Cross-Validation mit mehreren Modellen
`File → Test and Score ← [Tree, Random Forest, kNN, Naive Bayes]`
Mehrere Klassifikatoren auf einmal vergleichen.
(Quelle: [[Examples.md]])

### 5. Confusion Matrix mit Scatter Plot
`File → Test and Score → Confusion Matrix → Scatter Plot`
Fehlklassifizierungen auswählen und im Scatter Plot hervorheben.
(Quelle: [[Orange Data Mining]])

## Weitere Widget-Kategorien (nicht im Workshop, aber erwähnenswert)

- **Unsupervised**: k-Means, DBSCAN, PCA, t-SNE, Hierarchical Clustering, Outliers
- **Transform**: Preprocess, Impute, Normalize, Formula
- **Explain**: Feature Importance, Explain Model (SHAP)
- **Networks**: Network Explorer, Network Analysis (für Netzwerkvisualisierung)

## Installation

Orange ist verfügbar für Windows, macOS und Linux. Download: orangedatamining.com

## Verwandte Seiten

- [[Orange_Klassifikations_Workflow]]
- [[Workshop_Konzept]]
- [[CICIDS2017]]
