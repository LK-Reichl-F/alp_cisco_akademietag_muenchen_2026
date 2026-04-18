# BETH Dataset

**Zusammenfassung**: Honeypot-basierter Cybersecurity-Datensatz mit Kernel-Level-Prozessdaten aus AWS-Cloud-Umgebung. Für den Workshop nicht geeignet (falsche Domäne, kein Netzwerktraffic).

**Quellen**: (Quelle: [[BETH Dataset.md]])

**Zuletzt aktualisiert**: 2026-04-16

---

## Überblick

| Eigenschaft | Wert |
|---|---|
| Vollständiger Name | BPF-Extended Tracking Honeypot (BETH) Dataset |
| Herausgeber | Kate Highnam et al., UCL / Imperial College / Darktrace |
| Erhebungszeitraum | Mai 2021 |
| Infrastruktur | 23 Honeypots auf AWS (Cloud) |
| Datenmenge | 8.004.918 Events |
| Features | 14 Rohfeatures + 2 Labels (Prozessdaten); DNS-Logs separat |
| Gesamt-Spalten | 216 |
| Lizenz | CC0 Public Domain |
| Verfügbarkeit | Kaggle |

## Art der Daten

**BETH enthält keine klassischen Netzwerkflows**, sondern:
- **Kernel-Level-Prozessaufrufe** (via eBPF/BPF): welche Prozesse wurden gestartet, welche Systemcalls wurden ausgeführt
- **DNS-Logs**: DNS-Anfragen der Honeypots
- Features sind z. B.: Prozess-ID, Parent-Prozess-ID, User-ID, Systemcall-Typ, DNS-Hostname

## Warum nicht für diesen Workshop geeignet

1. **Falsche Domäne**: Cisco-Academy-Lehrkräfte kennen Netzwerkflows, Ports und Protokolle – keine Kernel-Prozesse. Der Wiedererkennungseffekt fehlt vollständig.
2. **216 Spalten**: Zu viele und zu abstrakte Features für eine Einführungsveranstaltung.
3. **Cloud-Infrastruktur**: Widerspruch zum gewünschten On-Premise-Szenario.
4. **Angriff nur im Testset**: Für interaktive Übungen ungünstig – man kann nicht frei explorieren.
5. **Host-basiert**: Kein PCAP, kein CICFlowMeter, kein Bezug zu Wireshark/Netflow.

## Stärken des Datensatzes (für andere Kontexte)

- Sehr modern (2021), echte Angriffe auf echte Honeypots
- Reale Daten (kein simulierter Traffic)
- Ideal für Anomalieerkennung und Unsupervised Learning
- Relevant für SOC-Analysten, die Host-basierte Forensik betreiben

## Mögliche zukünftige Verwendung

Falls der Workshop auf Host-Intrusion-Detection oder Cloud-Security ausgeweitet wird, könnte BETH interessant werden – dann aber mit anderem Zielpublikum (SOC-Analysten, nicht Netzwerktechniker).

## Verwandte Seiten

- [[CICIDS2017]]
- [[Workshop_Konzept]]
