# CICIDS2017

**Zusammenfassung**: Labeled Network-Intrusion-Detection-Datensatz des Canadian Institute for Cybersecurity (CIC), erhoben über 5 Tage in einem realistischen On-Premise-Unternehmensnetzwerk. Primärer Datensatz für den Workshop.

**Quellen**: (Quelle: [[IDS 2017  Datasets  Research  Canadian Institute for Cybersecurity.md]])

**Zuletzt aktualisiert**: 2026-04-16

---

## Überblick

| Eigenschaft | Wert |
|---|---|
| Vollständiger Name | CICIDS2017 / CIC-IDS-2017 |
| Herausgeber | Canadian Institute for Cybersecurity, University of New Brunswick |
| Erhebungszeitraum | 03.–07. Juli 2017 (Mo–Fr) |
| Infrastruktur | On-Premise-Labor (Modem, Firewall, Switches, Router) |
| Angriffskategorien | 8 (+ benign) |
| Features | 80+ (extrahiert mit CICFlowMeter) |
| Format | PCAP + CSV |
| Lizenz | Frei für Forschung, Zitierung erforderlich |

## Warum geeignet für den Workshop

- **On-Premise-Topologie**: Cisco-Lehrkräfte erkennen den Netzwerkaufbau sofort (Firewall, Switch, Windows-/Debian-/Mac-Rechner)
- **Bekannte Angriffstypen**: DoS, DDoS, Brute Force, Botnet – alles Unterrichtsstoff in Cisco Academy
- **Wochenstruktur**: Montag = normal, Di–Fr = eskalierende Angriffe → narrativer Rahmen für den Workshop
- **CSV-Format**: Direkt in Orange ladbar, kein Preprocessing nötig
- **Gut dokumentiert**: Viele Tutorials und wissenschaftliche Arbeiten verfügbar

## Netzwerktopologie

Siehe [[On_Premise_Netzwerktopologie]] für Details.

Kurzübersicht:
- **Angreiferseite**: Kali Linux (205.174.165.73), 3x Windows (205.174.165.69–71)
- **Firewall**: 205.174.165.80 / 172.16.0.1
- **Opfernetzwerk**: 12 Maschinen (Windows 7/8/10/Vista, Debian 12/14/16, Mac) im Subnetz 192.168.10.0/24

## Angriffsszenarien nach Tag

| Tag | Datum | Angriffe |
|---|---|---|
| Montag | 03.07.2017 | Nur normaler Verkehr (benign) |
| Dienstag | 04.07.2017 | FTP-Patator Brute Force, SSH-Patator Brute Force |
| Mittwoch | 05.07.2017 | DoS Slowloris, DoS Slowhttptest, DoS Hulk, DoS GoldenEye, Heartbleed |
| Donnerstag | 06.07.2017 | Web Attack (Brute Force, XSS, SQL Injection), Infiltration |
| Freitag | 07.07.2017 | Botnet ARES, Port Scan, DDoS LOIT |

Detaillierte Beschreibungen: [[Angriffsszenarien]]

## Features

Über 80 Flow-Features, extrahiert mit CICFlowMeter. Beispiele:

| Feature | Bedeutung |
|---|---|
| `fl_dur` | Flow-Dauer |
| `tot_fw_pk` | Gesamtpakete vorwärts |
| `tot_bw_pk` | Gesamtpakete rückwärts |
| `fl_byt_s` | Byte-Rate des Flows |
| `syn_cnt` | Anzahl SYN-Pakete |
| `fin_cnt` | Anzahl FIN-Pakete |

Vollständige Liste: [[CICFlowMeter_Features]]

## Workshop-Subset (erstellt, bereit)

Datei: `Datensätze/workshop_ids.csv`

- **Klassen**: BENIGN (5.000 Zeilen, Montag) + DDoS (5.000 Zeilen, Freitag Nachmittag)
- **Gesamt**: 10.000 Zeilen, zufällig gemischt (seed=42, reproduzierbar)
- **Features (11)**: `Total Fwd Packets`, `Total Backward Packets`, `Flow Bytes/s`, `Flow Packets/s`, `Flow Duration`, `FIN Flag Count`, `SYN Flag Count`, `ACK Flag Count`, `Packet Length Mean`, `Down/Up Ratio`, `Average Packet Size`
- **Bereinigt**: Inf/NaN-Werte entfernt (bekanntes CICIDS2017-Problem bei Flow Duration = 0)

**Empirische Trennschärfe der Features** (Median BENIGN vs. DDoS):

| Feature | BENIGN Median | DDoS Median | Faktor |
|---|---|---|---|
| `Packet Length Mean` | 60 | 834 | **14×** |
| `Average Packet Size` | 76 | 898 | **12×** |
| `Down/Up Ratio` | 1.0 | 0.0 | ∞ (binär!) |
| `Flow Duration` | 31.288 µs | 1.893.436 µs | **60×** |
| `Flow Packets/s` | 119 | 2.5 | **48×** (umgekehrt) |

**Empfohlene Scatter-Plot-Achsen für den Workshop**:
- X = `Packet Length Mean`, Y = `Down/Up Ratio` → sofort verständlich: DDoS sendet große Pakete, bekommt keine Antwort

## Bekannte Einschränkungen

- Einige bekannte Datenqualitätsprobleme (z. B. unbalancierte Klassen in bestimmten Tages-CSVs)
- Daten aus 2017 – für Forschung ggf. veraltet, für Lehrzwecke aber vollkommen ausreichend
- Große Rohdateien (~50 GB PCAP) – nur CSV-Dateien für den Workshop relevant

## Zitation

Sharafaldin, I., Lashkari, A. H., & Ghorbani, A. A. (2018). Toward Generating a New Intrusion Detection Dataset and Intrusion Traffic Characterization. ICISSP, Portugal.

## Verwandte Seiten

- [[On_Premise_Netzwerktopologie]]
- [[Angriffsszenarien]]
- [[CICFlowMeter_Features]]
- [[Workshop_Konzept]]
- [[CIC_IDS_2018]]
