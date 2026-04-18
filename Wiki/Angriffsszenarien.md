# Angriffsszenarien

**Zusammenfassung**: Übersicht aller Angriffstypen im CICIDS2017-Datensatz mit Erklärungen, Zeitplan und didaktischer Einschätzung für den Workshop.

**Quellen**: (Quelle: [[IDS 2017  Datasets  Research  Canadian Institute for Cybersecurity.md]])

**Zuletzt aktualisiert**: 2026-04-16

---

## Überblick

Der [[CICIDS2017]]-Datensatz enthält folgende Angriffstypen:

| Tag | Zeit | Angriff | Angreifer → Opfer |
|---|---|---|---|
| Di, 04.07. | 09:20–10:20 | FTP-Patator (Brute Force) | Kali → Web Server |
| Di, 04.07. | 14:00–15:00 | SSH-Patator (Brute Force) | Kali → Web Server |
| Mi, 05.07. | 09:47–11:23 | DoS (Slowloris, Slowhttptest, Hulk, GoldenEye) | Kali → Web Server |
| Mi, 05.07. | 15:12–15:32 | Heartbleed | Kali → Debian Server |
| Do, 06.07. | 09:20–10:42 | Web Attack (Brute Force, XSS, SQL Injection) | Kali → Web Server |
| Do, 06.07. | 14:19–15:45 | Infiltration (Dropbox, Metasploit, Port Scan) | Kali → Vista, Mac |
| Fr, 07.07. | 10:02–11:02 | Botnet ARES | Kali → 5x Windows |
| Fr, 07.07. | 13:55–14:35 | Port Scan (Firewall aktiv) | Kali → Debian |
| Fr, 07.07. | 14:51–15:29 | Port Scan (Firewall inaktiv) | Kali → Debian |
| Fr, 07.07. | 15:56–16:16 | DDoS LOIT | 3x Windows → Debian |

---

## Einzelne Angriffstypen

### Brute Force (FTP-Patator, SSH-Patator)
Automatisiertes Durchprobieren von Passwörtern aus einer Wörterliste (90 Millionen Einträge).
Tool: **Patator** (Python, multi-threading).

**Im Netzwerktraffic erkennbar durch**:
- Sehr viele Verbindungsversuche in kurzer Zeit
- Hohe Paketanzahl, kurze Flow-Dauer
- Gleiches Quell-IP / Ziel-IP-Paar, wechselnde Ports

**Didaktisch**: Sehr bekanntes Angriffsmuster, einfach zu erklären. Guter Einstieg für Tag 2.

---

### DoS – Denial of Service
Ziel: Webserver durch Überlastung unzugänglich machen.

| Variante | Beschreibung |
|---|---|
| **Slowloris** | Hält viele TCP-Verbindungen offen durch unvollständige HTTP-Anfragen |
| **Slowhttptest** | Ähnlich Slowloris, variiert den Angriffsmodus |
| **Hulk** | HTTP-Flood mit zufälligen Anfragen, umgeht Caching |
| **GoldenEye** | HTTP/S-DoS-Tool, hält Keep-Alive-Verbindungen offen |

**Im Traffic erkennbar durch**:
- Extreme Paketanzahl vom Angreifer
- Ungewöhnlich lange Flow-Dauer (Slowloris) oder sehr hohe Byte-Rate (Hulk)
- Stark reduzierter oder kein Traffic vom Opfer-Server zurück

**Didaktisch**: Sehr anschaulich – „Der Server ist tot". Unterschied zwischen Slowloris (wenig Bandbreite, viele Verbindungen) und Hulk (hohe Last) ist gut erklärbar.

---

### Heartbleed
Ausnutzung einer Schwachstelle in OpenSSL (CVE-2014-0160). Ermöglicht das Auslesen von Arbeitsspeicher des Servers – ohne Authentifizierung.

**Im Traffic erkennbar durch**:
- Anomale TLS-Heartbeat-Pakete auf Port 444
- Ungewöhnliche Antwortgrößen (Speicherinhalt wird zurückgegeben)

**Didaktisch**: Bekanntes Beispiel für eine Software-Schwachstelle, die viele Systeme betraf. Zeigt, dass nicht alle Angriffe durch Volumen auffallen.

---

### Web Attack (Brute Force, XSS, SQL Injection)
Drei klassische Web-Angriffe gegen einen Apache-Webserver:

| Angriff | Beschreibung |
|---|---|
| **Brute Force** | Wörterbuchangriff auf Login-Formular |
| **XSS** | Einschleusen von JavaScript in Webseiten |
| **SQL Injection** | Manipulation von Datenbankabfragen via URL/Formular |

**Didaktisch**: Aus dem Cisco-Curriculum bekannte Angriffe. Zeigt, dass KI auch Webangriffe im Netzwerktraffic erkennen kann – ohne Payload-Inspektion.

---

### Infiltration
Mehrstufiger Angriff:
1. Opfer öffnet manipuliertes Dokument (per Dropbox-Link/E-Mail)
2. Backdoor wird installiert (Metasploit)
3. Angreifer nutzt kompromittierten Rechner für internes Port-Scanning (Nmap)

**Im Traffic erkennbar durch**:
- Ungewöhnliche ausgehende Verbindungen vom Opferrechner
- Plötzlicher interner Port-Scan aus dem Netz

**Didaktisch**: APT-Szenario (Advanced Persistent Threat). Zeigt die Schwierigkeit, mehrstufige Angriffe zu erkennen – erhöht die Komplexität des Modells.

---

### Botnet ARES
Infektion von 5 Windows-Maschinen mit dem **Ares**-Botnet (Open Source, Python).
Fähigkeiten: Remote-Shell, Dateiübertragung, Screenshots, Key-Logging.

**Im Traffic erkennbar durch**:
- Regelmäßige Verbindungen zu Command-and-Control-Server
- Screenshot-Übertragungen alle 400 Sekunden
- Gleichmäßige, periodische Paketmuster

**Didaktisch**: Hochaktuelles Thema (Botnets für DDoS, Spam, Ransomware). Die Regelmäßigkeit des C2-Traffic ist im Scatter Plot gut sichtbar.

---

### Port Scan
Systematisches Abfragen von Ports auf Zielsystem, um offene Dienste zu finden. Tool: **Nmap**.

Zwei Varianten:
- **Mit Firewall**: Firewall filtert, weniger Antworten
- **Ohne Firewall**: Alle Ports erreichbar, klares Scan-Muster

Nmap-Scantypen im Datensatz: sS, sT, sF, sX, sN, sP, sV, sU, sO, sA, sW, sR, sL, sI, b

**Didaktisch**: Reconnaissance-Phase ist den Teilnehmern bekannt. Die Unterschiede zwischen Scan-Typen in den Feature-Werten zeigen den Mehrwert der Datenanalyse.

---

### DDoS LOIT (Low Orbit Ion Cannon)
Verteilter DoS-Angriff von 3 Windows-Maschinen gleichzeitig.
Tool: **LOIC** (UDP/TCP/HTTP-Flood).

**Im Traffic erkennbar durch**:
- Extrem hohe Paketrate von mehreren Quellen
- Sehr kurze Flow-Dauer, identische Paketgrößen
- Massiver Einbruch des Down/Up-Ratios beim Opfer

**Didaktisch**: **Empfohlener Angriff für den Workshop-Subset** (Montag benign + Freitag DDoS). Maximaler Kontrast, hohe Klassifikationsgenauigkeit, direkter Cisco-Bezug.

---

## Didaktische Reihenfolge für den Workshop

Empfehlung: Beginne mit der einfachsten binären Klassifikation:

1. **Benign vs. DDoS** → klarer Kontrast, hohe Genauigkeit, starkes Aha-Erlebnis
2. **Benign vs. DoS** → ähnlich, aber subtiler
3. **Mehrklassen** (alle Angriffe) → komplexer, für Vertiefung

## Verwandte Seiten

- [[CICIDS2017]]
- [[On_Premise_Netzwerktopologie]]
- [[Orange_Klassifikations_Workflow]]
- [[CICFlowMeter_Features]]
