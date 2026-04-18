---
title: KI erkennt Netzwerkangriffe
subtitle: Einführung in Data Mining mit Orange
author: Florian Reichl
date: "2026"
institute: |
  Akademie für Lehrerfortbildung und Personalführung Dillingen
theme: ALP
aspectratio: 169
fontsize: 11pt
lang: de-DE
mainfont: Roboto Slab
sansfont: Roboto
monofont: JetBrains Mono
header-includes:
  - \setbeamercovered{transparent}
  - \usetikzlibrary{positioning,arrows.meta}
  - \newcommand{\bildplatz}[2]{\begin{tikzpicture}\draw[ALPGrau,dashed,fill=ALPHell] (0,0) rectangle (#1,#2);\node[ALPGrau] at (#1/2,#2/2) {\tiny Bild einfügen};\end{tikzpicture}}
---

# Einstieg

## Agenda

\tableofcontents[hideallsubsections]

::: notes
Kurzer Überblick über den Ablauf. Betonen: Kein Programmieren, kein Mathe – wir
arbeiten visuell. 90 Minuten, 6 Phasen.
:::

## Das ist euer Netzwerk

:::: columns

::: column
**On-Premise-Unternehmensnetzwerk**

- Firewall, Switch, 10 Clients
- 1 Web Server (Debian)
- 1 Debian Server

\bigskip

**Letzte Woche war einiges los ...**
:::

::: column
\begin{tikzpicture}[
  box/.style={draw, rounded corners=2pt, font=\tiny,
              minimum width=1.6cm, minimum height=0.45cm,
              inner sep=2pt, align=center},
  red box/.style={box, fill=red!15, draw=red!60},
  blue box/.style={box, fill=ALPBlau!12, draw=ALPBlau!50},
  gray box/.style={box, fill=gray!10, draw=gray!50},
  arr/.style={-{Stealth[length=3pt]}, gray!60, thin},
  atk/.style={-{Stealth[length=3pt]}, red!60, dashed, thin},
]
% Angreifer
\node[red box] (kali) at (0, 4.2) {Kali Linux};
\node[red box] (win)  at (1.9, 4.2) {3× Windows};
\node[red!60, font=\tiny] at (0.95, 4.75) {ANGREIFER};

% Firewall
\node[gray box, minimum width=2.6cm] (fw) at (0.95, 3.2)
  {{\color{ALPBlau}\textbf{Firewall}} · NAT};

% Switch
\node[gray box, minimum width=2.6cm] (sw) at (0.95, 2.35)
  {Switch · Mirror-Port};

% Opfernetz-Label
\node[ALPBlau!70, font=\tiny] at (0.95, 1.85)
  {OPFERNETZWERK · 192.168.10.0/24};

% Opfer – je 1.6 cm breit, Mittelpunkte bei –1.0 / +0.95 / +2.9 cm
\node[blue box] (web) at (-0.85, 1.2) {Web Server\\Debian};
\node[blue box] (deb) at ( 0.95, 1.2) {Debian Server};
\node[blue box] (cli) at ( 2.75, 1.2) {10× Clients\\Win · Mac};

% Pfeile
\draw[arr] (fw) -- (sw);
\draw[arr] (sw.south) -- ++(0, -0.25) -| (web.north);
\draw[arr] (sw.south) -- (deb.north);
\draw[arr] (sw.south) -- ++(0, -0.25) -| (cli.north);
\draw[atk] (kali.south) -- (fw.north west);
\draw[atk] (win.south)  -- (fw.north east);
\end{tikzpicture}
:::

::::

::: notes
Netzwerkdiagramm erklären: „Das ist euer Netzwerk. Ihr seid die Netzwerkadmins."
Topologie benennen: Firewall mit NAT, Switch, Opfernetzwerk 192.168.10.0/24.
Angreifer-Seite zeigen: Kali Linux als Hauptangreifer, 3× Windows für DDoS.
:::

## Eine Woche im Netzwerk

| Tag | Ereignis |
|-----|----------|
| **Mo** | Normalbetrieb – 25 simulierte Nutzer |
| **Di** | Brute Force – FTP/SSH (Patator) |
| **Mi** | DoS – Slowloris, Hulk, Heartbleed |
| **Do** | Web Attack, Infiltration, XSS, SQL Injection |
| **Fr** | Botnet, Port Scan, **DDoS LOIT** 15:56–16:16 |

::: notes
Leitfragen: „Wie viele von euch haben schon von Machine Learning gehört?" –
„Was wäre der Vorteil von KI gegenüber klassischer Signaturerkennung?" –
„Kann ein Algorithmus einen DDoS erkennen, ohne den Payload zu lesen?"
:::

## Die zentrale Frage

\begin{center}
\Large
Kann ein KI-Modell \textbf{normalen Traffic}\\[6pt]
von \textbf{DDoS-Angriffen} unterscheiden?\\[18pt]
\normalsize
\textit{Ohne Payload-Inspektion – nur anhand von Flow-Metriken.}
\end{center}

::: notes
Überleitung: „Genau das schauen wir uns heute an – mit echten Messdaten aus
einem Labor-Netzwerk." Lernziele kurz nennen.
:::

## Lernziele

Nach diesem Workshop können Sie …

1. erklären, was **Data Mining** und **maschinelles Lernen** bedeuten
2. beschreiben, wie ein **Entscheidungsbaum** Netzwerktraffic klassifiziert
3. beurteilen, was **Accuracy, False Positives** und **False Negatives**
   im IDS-Kontext bedeuten
4. einschätzen, was den Unterschied zwischen einem **interpretierbaren**
   und einem **Black-Box-Modell** ausmacht
5. **Orange Data Mining** für einen einfachen Klassifikations-Workflow nutzen

# Daten erkunden

## Der Datensatz: CICIDS2017

:::: columns

::: column
**Quelle**

Canadian Institute for Cybersecurity,
Univ. of New Brunswick

**Unser Subset**

- Montag (BENIGN) + Freitag (DDoS)
- 10 000 Flows, 11 Features
- Datei: `workshop_ids.csv`
:::

::: column
**Ausgewählte Features**

```
fl_dur        Flow-Dauer
tot_fw_pk     Pakete vorwärts
fl_byt_s      Bytes/Sekunde
syn_cnt       SYN-Pakete
pkt_len_avg   Ø Paketgröße
down_up_ratio Antwort-Quote
Label         BENIGN / DDoS
```
:::

::::

::: notes
Orange öffnen. `workshop_workflow_phase1.ows` laden (nur File + Data Table +
Scatter Plot). CSV einlesen, Data Table öffnen. Spalten erklären: „Jede Zeile
ist ein Netzwerkflow." Frage: „Was bedeutet `Label`? Was bedeutet `down_up_ratio`?"
:::

## Daten erkunden: Data Table

\begin{center}
\includegraphics[width=0.85\textwidth]{screenshots/data_table.png}
\end{center}

::: notes
Screenshot Platzhalter – ersetzen durch eigenen Orange-Screenshot.
Durch Spalten scrollen, Werte zeigen, insb. Label-Spalte.
:::

## Was sehen wir im Scatter Plot?

:::: columns

::: column
**Einstellungen**

- X-Achse: `Packet Length Mean`
- Y-Achse: `Down/Up Ratio`
- Farbe: `Label`

\bigskip

**Beobachtung?**
:::

::: column
\begin{center}
\includegraphics[width=\linewidth]{screenshots/scatter_plot.png}
\end{center}
:::

::::

::: notes
Erwartetes Bild: Zwei klar getrennte Cluster. BENIGN: kleine Pakete (~60 Byte),
down_up_ratio > 0. DDoS: große HTTP-Pakete (~833 Byte), down_up_ratio ≈ 0.
„Warum ist die Antwort-Quote beim DDoS null?" → Server so überlastet, keine
Antwort. Das kennen alle Cisco-Lehrkräfte.
:::

## Zwischensicherung: Daten haben Struktur

\begin{alertblock}{Kernaussage}
Daten haben eine Struktur -- und diese Struktur ist für uns sichtbar.\\
Genau diese Struktur \textbf{lernt} ein KI-Modell.
\end{alertblock}

# Entscheidungsbaum

## Was ist ein Entscheidungsbaum?

:::: columns

::: column
**Idee**

Das Modell stellt **Ja/Nein-Fragen** zu den Daten und trifft dann eine Entscheidung.

\bigskip

**Wie beim Lernen für eine Prüfung:**

- Trainingsphase: Modell sieht Beispiele mit bekannten Labels
- Testphase: Modell bewertet neue, unbekannte Flows
:::

::: column
```
fl_byt_s > 45 000?
├── Ja → DDoS (99 %)
└── Nein
    └── down_up_ratio > 0.1?
        ├── Ja → BENIGN (98 %)
        └── Nein → DDoS (94 %)
```
:::

::::

::: notes
Data Sampler erklären: Trainings- und Testdaten trennen. Tree-Widget mit Data
Sampler verbinden, trainieren lassen. Dann Tree Viewer öffnen.
:::

## Der Entscheidungsbaum in Orange

\begin{center}
\includegraphics[width=0.85\textwidth]{screenshots/tree_viewer.png}
\end{center}

::: notes
Erste Verzweigung laut vorlesen: „Wenn fl_byt_s > X, dann sehr wahrscheinlich
DDoS." Frage: „Ergibt das für euch Sinn?" → Ja, DDoS-Flows transportieren
große HTTP-Requests (LOIT). Dann: Knoten anklicken → Punkte im Scatter Plot
leuchten auf.
:::

## Ist das Magie?

\begin{block}{KI erklärt}
Ein Entscheidungsbaum ist ein KI-Modell, das wir \textbf{lesen und erklären} können.\\[6pt]
Das ist wichtig: Im echten Einsatz müssen wir erklären können, \textit{warum}
das System einen Alarm auslöst.
\end{block}

::: notes
„Was ist KI?" → Kein Zaubern. Gelernte Entscheidungsregeln auf Basis von
Statistik. „Kann jeder diese Regeln verstehen?" → Ja, der Baum ist lesbar.
:::

# Modellbewertung

## Wie gut ist unser Modell?

:::: columns

::: column
**Test and Score**

- Cross-Validation: 10-fach
- Modell sieht nur Testdaten

\bigskip

**Typisches Ergebnis**

| Metrik | Wert |
|--------|------|
| Accuracy | ~98 % |
| Precision | ~97 % |
| Recall | ~98 % |
:::

::: column
\begin{alertblock}{Denkanstoß}
98\,\% Genauigkeit -- ist das gut?\\[6pt]
Bei 10\,000 Flows = \textbf{200 falsche Entscheidungen}.\\[6pt]
Was davon sind Fehlalarme?\\
Was davon sind übersehene Angriffe?
\end{alertblock}
:::

::::

::: notes
Test and Score vorstellen. Cross-Validation kurz erklären: „Wir testen das
Modell auf Daten, die es nicht gesehen hat – wie eine echte Prüfung."
Accuracy zeigen. Dann die kritische Frage stellen.
:::

## Die Confusion Matrix

:::: columns

::: column
\begin{center}
\includegraphics[width=\linewidth]{screenshots/confusion_matrix.png}
\end{center}
:::

::: column
\small
| | DDoS | BENIGN |
|---|---|---|
| **DDoS** | TP \textcolor{green!60!black}{$\checkmark$} | **FN** \textcolor{red}{$\times$} |
| **BENIGN** | **FP** \textcolor{orange!80!black}{!} | TN \textcolor{green!60!black}{$\checkmark$} |

\bigskip

\footnotesize
**TP** True Positive\\
**FN** False Negative\\
**FP** False Positive\\
**TN** True Negative
:::

::::

::: notes
Vier Felder beschriften. Dann: False Positives in der Matrix auswählen →
Scatter Plot zeigt diese Punkte. „Wo liegen sie?" → An der Klassengrenze.
:::

## Alert Fatigue – ein reales Problem

:::: columns

::: column
**False Positive**

→ Fehlalarm im IDS

→ Admins bearbeiten unnötige Tickets

→ Admins ignorieren irgendwann Alarme

→ **Echter Angriff wird übersehen**
:::

::: column
**False Negative**

→ Angriff nicht erkannt

→ Kein Alarm ausgelöst

→ **Angreifer operiert unbemerkt**

\bigskip
*Was ist schlimmer in eurem Netzwerk?*
:::

::::

\begin{block}{Kernaussage}
Kein Modell ist perfekt. Wir müssen entscheiden, ob wir lieber Fehlalarme
oder übersehene Angriffe akzeptieren -- das ist eine \textbf{fachliche},
keine technische Entscheidung.
\end{block}

::: notes
Diskussionsfragen: „Wie viele False Positives sind tolerierbar?" –
„Was wäre die Konsequenz eines False Negative bei Heartbleed?" –
„Wie unterscheidet sich das von Signaturerkennung?"
:::

# Modellvergleich

## Drei Modelle im Vergleich

| Modell | Accuracy | Interpretierbar? |
|--------|----------|-----------------|
| Entscheidungsbaum | ~97--98\,\% | ✅ Hoch |
| Random Forest | ~99\,\% | ❌ Gering |
| k-Nearest Neighbor | ~95--97\,\% | ⚠ Mittel |

::: notes
Random Forest: „Viele Bäume abstimmen – wie ein Komitee." kNN: „Welche Klasse
haben die ähnlichsten bekannten Fälle?" Beide Widgets mit Test and Score
verbinden. Ergebnisse nebeneinander zeigen.
:::

## Genauigkeit vs. Erklärbarkeit

\begin{block}{Kernaussage}
Die Wahl des Modells ist nicht nur eine technische Frage.\\[6pt]
Im Unterricht und im echten Einsatz zählt:\\
\textbf{Kann ich das Ergebnis erklären und verteidigen?}
\end{block}

\bigskip

**Random Forest** ist genauer – aber können wir die Regeln lesen?

::: notes
„Random Forest ist besser – aber können wir die Regeln lesen?" → Nein.
„Was bedeutet das für den Einsatz in einem Unternehmen? In der Schule?"
:::

# Abschluss

## Was haben wir gelernt?

1. **KI = Mustererkennung in Daten** – kein Zaubern, sondern Statistik auf Netzwerkflows
2. **Entscheidungsbaum = erklärbare KI** – wir können die Regeln lesen und verteidigen
3. **Kein Modell ist perfekt** – False Positives und False Negatives sind unvermeidbar
4. **Die Wahl des Modells ist eine Fachentscheidung** – Genauigkeit allein reicht nicht
5. **Orange ist ein Werkzeug für den Unterricht** – kostenlos, visuell, kein Programmieren

## Transfer in den Unterricht

**Orange ist kostenlos und sofort einsetzbar:**

- Funktioniert mit jedem CSV – auch eigene Datensätze möglich
- Entscheidungsbaum + Confusion Matrix passt in eine **Doppelstunde**
- CICIDS2017 ist öffentlich zugänglich (cicresearch.ca)
- Das Netzwerkdiagramm passt direkt in das **Cisco-Curriculum**

\bigskip

**Nächste Schritte:**

- Mehrklassen-Klassifikation (Botnet, Port Scan, DDoS)
- Weitere Datensätze erkunden (UNSW-NB15)
- Unüberwachtes Lernen (Clustering ohne Labels)

::: notes
Impulse geben. Fragen: „Wie könntet ihr das in eurem Unterricht einsetzen?"
Materialien nennen: Handout, Datensatz, Workflow-Datei.
:::

## Materialien

| Datei | Inhalt |
|-------|--------|
| `workshop_ids.csv` | Datensatz (10 000 Flows, 11 Features) |
| `workshop_workflow.ows` | Vorgefertigter Orange-Workflow |
| `workshop_workflow_phase1.ows` | Nur Daten-Explorer (Phase 2) |
| Handout (A4) | Kurzanleitung + Diskussionsfragen |

\bigskip

**Orange Data Mining:** [orangedatamining.com](https://orangedatamining.com)

**CICIDS2017:** [cicresearch.ca](https://www.cicresearch.ca)

## Danke – und ein Wort zum Schluss

\begin{center}
\Large
\textit{„Wenn du verstehst, wie ein Algorithmus}\\
\textit{Netzwerktraffic liest,}\\
\textit{verstehst du auch, wie Angreifer}\\
\textit{ihn täuschen."}\\[18pt]
\normalsize
Feedback: Ein Wort, das diesen Workshop beschreibt.
\end{center}

::: notes
Abschluss-Frage: „Was nehmt ihr mit?" Feedback-Runde: 1 Wort pro Person.
Dann Materialien verteilen / Link schicken.
:::
