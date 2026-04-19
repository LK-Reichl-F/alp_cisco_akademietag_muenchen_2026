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
sansfont: Roboto Flex
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

## Cisco NGFW schützt euer Netzwerk

:::: columns

::: column
**On-Premise-Unternehmensnetzwerk**

- Cisco NGFW / ASA mit IPS-Modul
- Switch, Web-Server, 10 Clients

\medskip

**Deep Packet Inspection (DPI)**

Jedes Paket wird gegen eine \textbf{Signatur-Datenbank} geprüft – Header \emph{und} Payload.
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
% Botnet (Angreifer)
\node[red box, minimum width=1.1cm] (r1) at (-0.25, 4.2) {TP-Link};
\node[red box, minimum width=1.1cm] (r2) at ( 0.95, 4.2) {TP-Link};
\node[red box, minimum width=1.1cm] (r3) at ( 2.15, 4.2) {TP-Link};
\node[red!60, font=\tiny] at (0.95, 4.75)
  {BOTNET · 100\,000+ kompromittierte Router};

% Firewall
\node[gray box, minimum width=2.6cm] (fw) at (0.95, 3.2)
  {{\color{ALPBlau}\textbf{Cisco NGFW}} · DPI};

% Switch
\node[gray box, minimum width=2.6cm] (sw) at (0.95, 2.35)
  {Switch · Mirror-Port};

% Opfernetz-Label
\node[ALPBlau!70, font=\tiny, fill=white, inner sep=1pt] at (0.95, 2.0)
  {OPFERNETZWERK · 192.168.10.0/24};

% Opfer
\node[blue box] (web) at (-0.85, 1.2) {Web Server\\Debian};
\node[blue box] (deb) at ( 0.95, 1.2) {Debian Server};
\node[blue box] (cli) at ( 2.75, 1.2) {10× Clients\\Win · Mac};

% Pfeile
\draw[arr] (fw) -- (sw);
\draw[arr] (sw.south) -- ++(0, -0.25) -| (web.north);
\draw[arr] (sw.south) -- (deb.north);
\draw[arr] (sw.south) -- ++(0, -0.25) -| (cli.north);
\draw[atk] (r1.south) -- (fw.north west);
\draw[atk] (r2.south) -- (fw.north);
\draw[atk] (r3.south) -- (fw.north east);
\end{tikzpicture}
:::

::::

::: notes
Topologie kurz benennen. Fokus auf die NGFW: „Die Cisco NGFW prüft jeden Paket-Header
UND Payload gegen bekannte Angriffssignaturen – das nennt sich Deep Packet Inspection."
Frage stellen: „Was passiert, wenn plötzlich 100.000 Pakete pro Sekunde ankommen?"
:::

## Das Problem: DDoS überlastet die Firewall

\begin{alertblock}{Angriffsszenario}
Tausende Flows pro Sekunde treffen gleichzeitig ein – ein DDoS-Angriff.
\end{alertblock}

\bigskip

**Die Überlastungskette:**

\medskip

\begin{tabular}{cl}
\textbf{1.} & DDoS flutet das Netz mit Flows \\[3pt]
\textbf{2.} & NGFW-CPU steigt auf 100\,\% – DPI bricht zusammen \\[3pt]
\textbf{3.} & Alarme häufen sich – Admins können nicht mehr priorisieren \\[3pt]
\textbf{4.} & \textbf{Alert Fatigue:} echte Angriffe bleiben unbemerkt \\
\end{tabular}

::: notes
Alert Fatigue ist ein reales SOC-Problem: Je mehr Fehlalarme, desto mehr ignorieren
Admins die Alarme – bis echte Angriffe durchkommen. Frage: „Kennt ihr das aus der Praxis?"
Überleitung: „Was wäre, wenn ein einfaches Modell 80–90 % des Traffics schon VOR der DPI
vorsortiert? Die NGFW müsste nur noch den Rest prüfen."
:::

## Die Idee: ML als Vorfilter

:::: columns

::: column
**Heute:**

\medskip

Jeder Flow $\rightarrow$ NGFW $\rightarrow$ DPI

\bigskip

**Mit Vorfilter:**

\medskip

\begin{tabular}{@{}l@{}}
Jeder Flow $\rightarrow$ \textbf{ML-Modell}\\
\quad $\rightarrow$ eindeutig BENIGN $\rightarrow$ durchlassen\\
\quad $\rightarrow$ eindeutig DDoS $\rightarrow$ blockieren\\
\quad $\rightarrow$ unklar $\rightarrow$ NGFW $\rightarrow$ DPI
\end{tabular}

\bigskip

\small\textit{Nur noch 10–20\,\% des Traffics erreicht die DPI-Stufe.}
:::

::: column
\begin{block}{Entscheidend}
Das ML-Modell analysiert \textbf{keine Payloads} –
nur statistische Flow-Metriken:\\[6pt]
Paketgröße · Antwortverhalten · Durchsatz\\[6pt]
Das ist schnell genug für Leitungsgeschwindigkeit.
\end{block}

\bigskip

\begin{block}{Heute bauen wir genau das}
Ein einfacher \textbf{Entscheidungsbaum}
mit 2–3 Regeln erreicht ca.\ 98\,\% Genauigkeit.
\end{block}
:::

::::

::: notes
„Was ihr heute baut, ist konzeptionell dasselbe wie Cisco Secure Network Analytics /
Stealthwatch – nur auf einem Laptop und mit 10.000 Flows statt Millionen."
Betonen: kein Payload, keine Entschlüsselung nötig – das ist der Clou.
:::

## Regelbasiert vs. maschinell lernen

:::: columns

::: column
\begin{block}{Good Old-Fashioned AI}
\textbf{Experte schreibt Regeln per Hand:}

\medskip

\texttt{if SYN\_count > 1000 $\rightarrow$ BLOCK}\\
\texttt{if payload contains "exploit" $\rightarrow$ ALERT}

\medskip

\small
Problem: Neue Angriffe erfordern neue Regeln.\\
Cisco-IPS: täglich neue Signaturen nötig.
\end{block}
:::

::: column
\begin{block}{Machine Learning}
\textbf{Algorithmus lernt Regeln aus Daten:}

\medskip

Beispiele mit bekannten Labels $\rightarrow$\\
Modell erkennt Muster selbst $\rightarrow$\\
Regeln entstehen automatisch

\medskip

\small
Neue Angriffe: neue Trainingsdaten genügen.\\
Kein manuelles Signatur-Update.
\end{block}
:::

::::

::: notes
Diagramm aus MaschinellesLernen.drawio.svg erklären.
GOFA: Experten-Wissen kodiert in handgeschriebenen Regeln.
ML: Das System „sieht" Tausende Beispiele und findet selbst die Grenzen.
„Signatur-Updates bei Cisco – das ist GOFA. Was wir heute bauen, ist ML."
:::

## Der Unterschied im Kern

:::: columns

::: column
**Good Old-Fashioned AI**

\bigskip

\begin{enumerate}
\item Experte analysiert Angriffs\-muster
\item Experte schreibt Regel: \texttt{if SYN > 1000 $\rightarrow$ BLOCK}
\item Regel wird deployed
\item Neuer Angriff $\rightarrow$ zurück zu Schritt 1
\end{enumerate}

\bigskip

\small\textit{Cisco IPS: täglich neue Signaturen. Jede Regel ist handgemacht.}
:::

::: column
**Machine Learning**

\bigskip

\begin{enumerate}
\item Trainingsdaten sammeln (Flows + Labels)
\item Algorithmus analysiert Muster \textbf{selbst}
\item Modell generiert Regeln automatisch
\item Neuer Angriff $\rightarrow$ neue Daten genügen
\end{enumerate}

\bigskip

\small\textit{Kein manuelles Signatur-Update. Das Modell lernt neu.}
:::

::::

\begin{alertblock}{Die Kernformel}
GOFA: Mensch $\rightarrow$ Regeln $\rightarrow$ Ergebnisse\quad|\quad
ML: Daten + Ergebnisse $\rightarrow$ Maschine $\rightarrow$ Regeln
\end{alertblock}

::: notes
Diese Folie ist der konzeptuelle Kern des Workshops.
Betonen: „Bei GOFA ist der Mensch der Flaschenhals – Experten sind teuer und langsam.
Bei ML ist der Flaschenhals die Datenqualität – aber die haben wir."
Signatur-Updates: jede neue Malware braucht einen Experten + Deployment-Zyklus.
ML: Neue Trainingsdaten sammeln, Modell neu trainieren – fertig.
:::

## Lernziele

Nach diesem Workshop können Sie …

1. erklären, wie **ML-Vorfilterung** Cisco-Geräte bei DDoS entlasten kann
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
- Datei: `workshop_ids.tab`
:::

::: column
**Ausgewählte Features**

```
Flow Duration       Flow-Dauer
Flow Packets/s      Pakete/Sekunde
Flow Bytes/s        Bytes/Sekunde
SYN Flag Count      SYN-Pakete
Packet Length Mean  Ø Paketgröße
Down/Up Ratio       Antwort-Quote
Label               BENIGN / DDoS
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
„Warum ist die Antwort-Quote beim DDoS null?" $\rightarrow$ Server so überlastet, keine
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
**Kennt ihr das?**

\medskip

Cisco-Troubleshooting-Leitfäden funktionieren genauso:

\smallskip
\textit{„Leuchtet die Link-LED? $\rightarrow$ Nein $\rightarrow$ Kabel prüfen."}\\
\textit{„Ping möglich? $\rightarrow$ Ja $\rightarrow$ Layer-3-Problem."}

\bigskip

**Ein Entscheidungsbaum ist genau das – nur findet das Modell die Fragen selbst, aus den Trainingsdaten.**
:::

::: column
\small
\begin{block}{Beispiel aus unseren Daten}
\texttt{Flow Bytes/s > 45\,000?}\\[3pt]
\hspace*{4mm}Ja $\rightarrow$ DDoS (99\,\%)\\[3pt]
\hspace*{4mm}Nein $\rightarrow$ \texttt{Down/Up Ratio > 0.1?}\\[3pt]
\hspace*{12mm}Ja $\rightarrow$ BENIGN (98\,\%)\\[3pt]
\hspace*{12mm}Nein $\rightarrow$ DDoS (94\,\%)
\end{block}

\medskip

\footnotesize
Trainingsphase: Modell sieht 7\,000 Flows mit bekannten Labels und findet die besten Fragen.

Testphase: 3\,000 neue Flows – kein Label bekannt.
:::

::::

::: notes
Analogie betonen: „Das ist euer Cisco-Troubleshooting-Flowchart – aber automatisch
generiert. Das Modell hat aus 7.000 Beispielen gelernt, welche Frage an welcher
Stelle am meisten Flows korrekt trennt."
Data Sampler erklären: 70/30-Split. Dann Tree + Tree Viewer verbinden.
:::

## Der Entscheidungsbaum in Orange

\begin{center}
\includegraphics[width=0.85\textwidth]{screenshots/tree_viewer.png}
\end{center}

::: notes
Erste Verzweigung laut vorlesen: „Wenn fl_byt_s > X, dann sehr wahrscheinlich
DDoS." Frage: „Ergibt das für euch Sinn?" $\rightarrow$ Ja, DDoS-Flows transportieren
große HTTP-Requests (LOIC). Dann: Knoten anklicken $\rightarrow$ Punkte im Scatter Plot
leuchten auf.
:::

## Ist das Magie?

\begin{block}{KI erklärt}
Ein Entscheidungsbaum ist ein KI-Modell, das wir \textbf{lesen und erklären} können.\\[6pt]
Das ist wichtig: Im echten Einsatz müssen wir erklären können, \textit{warum}
das System einen Alarm auslöst.
\end{block}

::: notes
„Was ist KI?" $\rightarrow$ Kein Zaubern. Gelernte Entscheidungsregeln auf Basis von
Statistik. „Kann jeder diese Regeln verstehen?" $\rightarrow$ Ja, der Baum ist lesbar.
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
\begin{tabular}{@{}ll@{}}
\textbf{TP} & True Positive\\
\textbf{FN} & False Negative\\
\textbf{FP} & False Positive\\
\textbf{TN} & True Negative
\end{tabular}
:::

::::

::: notes
Vier Felder beschriften. Dann: False Positives in der Matrix auswählen $\rightarrow$
Scatter Plot zeigt diese Punkte. „Wo liegen sie?" $\rightarrow$ An der Klassengrenze.
:::

## Alert Fatigue – ein reales Problem

:::: columns

::: column
**False Positive**

$\rightarrow$ Fehlalarm im IDS

$\rightarrow$ Admins bearbeiten unnötige Tickets

$\rightarrow$ Admins ignorieren irgendwann Alarme

$\rightarrow$ **Echter Angriff wird übersehen**
:::

::: column
**False Negative**

$\rightarrow$ Angriff nicht erkannt

$\rightarrow$ Kein Alarm ausgelöst

$\rightarrow$ **Angreifer operiert unbemerkt**

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

## Entscheidungsbaum – Flowchart-Logik

:::: columns

::: column
**Position im Vergleich**

\bigskip

\begin{tabular}{@{}ll@{}}
Accuracy  & ca.\ 97--98\,\% \\[4pt]
Regeln    & \textbf{lesbar}, verteidigbar \\[4pt]
Training  & schnell \\[4pt]
Vorfilter & \textbf{Ja} \\
\end{tabular}

\bigskip

\begin{block}{Kernregel aus unseren Daten}
\small
\texttt{Flow Bytes/s > 45\,000?}\\[2pt]
\hspace*{4mm}Ja $\rightarrow$ \textbf{DDoS} (99\,\%)
\end{block}

\small\textit{Zwei Fragen reichen für 98\,\% Genauigkeit.}
:::

::: column
**Warum für den Einstieg ideal**

\medskip

\begin{itemize}
\item Regeln sind lesbar wie ein Troubleshooting-Leitfaden
\item Jede Entscheidung ist nachvollziehbar und erklärbar
\item Kann einem Vorgesetzten oder Schüler gezeigt werden
\end{itemize}

\bigskip

\begin{alertblock}{Explainable AI}
Im Schulnetz und im echten Betrieb gilt:\\
Wir müssen erklären können, \textbf{warum} das Modell blockt.\\
Der Entscheidungsbaum kann das – Random Forest nicht.
\end{alertblock}
:::

::::

::: notes
Übergang zum Vergleich: „Den Baum kennt ihr schon – ihr habt ihn im Tree Viewer gesehen.
Jetzt schauen wir, was passiert, wenn wir statt einem Baum 100 nehmen."
Betonen: Die 2-Fragen-Regel ist kein Zufall – das Modell hat das aus den Daten gelernt.
:::

## Random Forest – das Komitee

:::: columns

::: column
**Das Prinzip**

\medskip

Nicht ein Baum, sondern \textbf{100 unabhängige Bäume}.

\bigskip

\begin{enumerate}
\item Jeder Baum trainiert auf einem \textbf{zufälligen Ausschnitt} der Daten (Bootstrap)
\item Bei jeder Verzweigung: zufällige Auswahl der Features
\item Alle 100 Bäume stimmen ab – \textbf{Mehrheit entscheidet}
\end{enumerate}

\bigskip

\small\textit{„87 von 100 Bäumen sagen DDoS $\rightarrow$ DDoS"}
:::

::: column
**Warum besser als ein einzelner Baum?**

\medskip

Ein einzelner Baum kann überanpassen.\\
100 Bäume gleichen Fehler aus.

\bigskip

\begin{block}{Vergleich}
\small
\begin{tabular}{@{}ll@{}}
Entscheidungsbaum & ca.\ 98\,\% Accuracy\\
Random Forest     & ca.\ 99\,\% Accuracy\\
\end{tabular}
\end{block}

\bigskip

\begin{alertblock}{Nachteil}
\small
100 Bäume $\rightarrow$ keine lesbaren Regeln mehr.\\
\textbf{Black Box:} Wir sehen das Ergebnis, nicht den Weg.
\end{alertblock}
:::

::::

::: notes
Analogie: „Statt einen Experten zu fragen, befragt ihr 100 unabhängige Experten
und nehmt den Mehrheitsentscheid. Keiner kennt alle Daten – jeder nur einen Ausschnitt.
Das macht das Komitee robuster als jeder Einzelne."
„Random" kommt von der zufälligen Feature-Auswahl bei jedem Split – nicht vom Ergebnis.
In Orange: Random Forest mit Test and Score verbinden, Accuracy mit Tree vergleichen.
:::

## k-Nearest Neighbors – Ähnlichkeitssuche

:::: columns

::: column
**Das Prinzip**

\medskip

kNN \textbf{trainiert gar nichts}.\\
Es speichert alle 7\,000 Trainings-Flows.

\bigskip

\begin{enumerate}
\item Neuer Flow kommt an
\item Berechne Abstand zu allen 7\,000 bekannten Flows
\item Finde die \textbf{5 ähnlichsten} (k=5)
\item Mehrheitsklasse der 5 Nachbarn $\rightarrow$ Vorhersage
\end{enumerate}

\bigskip

\small\textit{„4 von 5 Nachbarn sind DDoS $\rightarrow$ DDoS"}
:::

::: column
**Das Problem in der Praxis**

\bigskip

\begin{alertblock}{Zu langsam für Leitungsgeschwindigkeit}
\small
Jeder neue Flow: Vergleich mit \textbf{allen} 7\,000 Beispielen.\\
Bei 10\,000 Flows/Sekunde: nicht praxistauglich als Vorfilter.
\end{alertblock}

\bigskip

\begin{block}{Aber nützlich für}
\small
\begin{itemize}
\item Forensik: „Zeig mir ähnliche Fälle"
\item Kleine Datenmengen offline analysieren
\item Erklärung: Nachbarn sind sichtbar – teilweise nachvollziehbar
\end{itemize}
\end{block}
:::

::::

::: notes
kNN ist keine KI im klassischen Sinne – es gibt kein trainiertes Modell.
Das System „denkt" bei jeder Anfrage neu nach.
Analogie: „Ihr habt 7.000 beschriftete Netzwerk-Flows auf Karteikarten.
Neuer Flow kommt: Ihr sucht die 5 ähnlichsten Karteikarten. Was steht drauf?"
In Orange: kNN mit Test and Score verbinden. Accuracy zeigen. Dann erklären,
warum kNN trotzdem kein guter Vorfilter ist.
:::

## Drei Modelle im Vergleich

\small
| Modell | Accuracy | Regeln lesbar? | Als Vorfilter? |
|--------|----------|---------------|----------------|
| Entscheidungsbaum | ca. 97--98\,\% | **Ja** – jede Regel nachvollziehbar | Ja – erklärbar |
| Random Forest | ca. 99\,\% | **Nein** – 100 Bäume, nicht lesbar | Ja – genauer |
| kNN | ca. 95--97\,\% | Bedingt – Nachbarn zeigbar | Nein – zu langsam\textsuperscript{*} |

\normalsize
\medskip
\footnotesize\textsuperscript{*}kNN speichert alle Trainingsdaten – jede Vorhersage erfordert einen Vergleich mit allen 7\,000 Beispielen.

::: notes
Beide Widgets (Random Forest, kNN) mit Test and Score verbinden, Ergebnisse
nebeneinander zeigen. Diskussion: kNN zu langsam für Leitungsgeschwindigkeit
(muss für jeden Flow alle Trainingsdaten durchsuchen). Forest und Tree beide
praktisch einsetzbar – aber welchen würdet ihr eurem Chef erklären?
:::

## Genauigkeit vs. Erklärbarkeit

\begin{block}{Kernaussage}
Die Wahl des Modells ist nicht nur eine technische Frage.\\[6pt]
Im Unterricht und im echten Einsatz zählt:\\
\textbf{Kann ich das Ergebnis erklären und verteidigen?}
\end{block}

\bigskip

\begin{columns}
\begin{column}{0.48\textwidth}
\textbf{Entscheidungsbaum:}\\
„Ich kann euch zeigen, warum\\
dieser Flow als DDoS gilt."
\end{column}
\begin{column}{0.48\textwidth}
\textbf{Random Forest:}\\
„87 von 100 Bäumen sagten DDoS –\\
aber warum, kann ich nicht zeigen."
\end{column}
\end{columns}

::: notes
„Was ist im Schulnetz besser? Was wäre im produktiven Rechenzentrum besser?"
„Würdet ihr einem System vertrauen, das blockt, aber nicht erklären kann warum?"
:::

# Abschluss

## Was haben wir gelernt?

1. **DPI überlastet bei DDoS** – Cisco NGFW braucht einen Vorfilter
2. **ML lernt Regeln aus Daten** – kein manuelles Signatur-Update nötig (≠ GOFA)
3. **Entscheidungsbaum = erklärbare KI** – Regeln lesbar, verteidigbar, einsetzbar
4. **Kein Modell ist perfekt** – False Positives und False Negatives sind unvermeidbar
5. **Die Wahl des Modells ist eine Fachentscheidung** – Genauigkeit vs. Erklärbarkeit

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
| `workshop_ids.tab` | Datensatz (10 000 Flows, 11 Features) |
| `workshop_workflow.ows` | Vorgefertigter Orange-Workflow |
| `workshop_workflow_phase1.ows` | Nur Daten-Explorer (Phase 2) |
| Handout (A4) | Kurzanleitung + Diskussionsfragen |

\bigskip

**Orange Data Mining:** [orangedatamining.com](https://orangedatamining.com)

**CICIDS2017:** [cicresearch.ca](https://www.cicresearch.ca)

## Danke – und ein Wort zum Schluss

\begin{center}
\Large
\textit{Was ihr heute gebaut habt,}\\[4pt]
\textit{ist der Vorfilter vor eurer Cisco NGFW.}\\[16pt]
\normalsize
Cisco Secure Network Analytics macht dasselbe –\\
nur mit Millionen Flows pro Minute.\\[18pt]
Feedback: Ein Wort, das diesen Workshop beschreibt.
\end{center}

::: notes
Abschluss-Frage: „Was nehmt ihr mit?" Feedback-Runde: 1 Wort pro Person.
Dann Materialien verteilen / Link schicken.
:::
