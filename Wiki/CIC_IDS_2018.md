# CIC-IDS-2018

**Zusammenfassung**: Nachfolgedatensatz von CICIDS2017, erhoben auf AWS-Infrastruktur. Größere Angreiferinfrastruktur, gleiche Feature-Extraktion. Für den On-Premise-Workshop nicht geeignet.

**Quellen**: (Quelle: [[IDS 2018  Datasets  Research  Canadian Institute for Cybersecurity.md]])

**Zuletzt aktualisiert**: 2026-04-16

---

## Überblick

| Eigenschaft | Wert |
|---|---|
| Vollständiger Name | CSE-CIC-IDS2018 |
| Herausgeber | CSE (Communications Security Establishment) + CIC |
| Erhebungszeitraum | Februar–März 2018 |
| Infrastruktur | **AWS-Cloud** (5 Subnetze, 420 Maschinen, 50 Angreifer) |
| Angriffsszenarien | 7 (Brute Force, Heartbleed, Botnet, DoS, DDoS, Web Attack, Infiltration) |
| Features | 83 (CICFlowMeter-V3) |
| Download | AWS S3: `aws s3 sync --no-sign-request "s3://cse-cic-ids2018/" dest-dir` |

## Verbesserungen gegenüber CICIDS2017

- Deutlich größere Infrastruktur (50 Angreifer vs. 1 Kali, 420 Opfer vs. 12)
- AWS-Umgebung: realistischer für Cloud-basierte Unternehmensnetzwerke
- Vollständigere Feature-Dokumentation (83 Features mit Beschreibung)
- Botnets: Zeus + Ares (statt nur Ares)

## Warum nicht für diesen Workshop

**Infrastruktur ist Cloud-basiert, nicht On-Premise.** Das Netzwerk läuft auf AWS-EC2-Instanzen mit öffentlichen IP-Adressen (`18.x.x.x`, `13.x.x.x`) – kein klassischer Unternehmensaufbau mit Firewall/NAT/Switch.

Für den Workshop, der bewusst ein **On-Premise-Szenario** thematisiert, ist [[CICIDS2017]] die bessere Wahl.

## Wann könnte CIC-IDS-2018 sinnvoll sein?

- Workshop-Fortsetzung mit Fokus auf Cloud-Sicherheit
- Größere Datenmenge gewünscht (mehr Angriffsvarianten)
- Vergleich On-Premise vs. Cloud-Angriffsmuster

## Download-Hinweis

Erfordert AWS CLI:
```bash
aws s3 sync --no-sign-request --region <your-region> "s3://cse-cic-ids2018/" dest-dir
```
Deutlich aufwändiger als der direkte CSV-Download von CICIDS2017.

## Verwandte Seiten

- [[CICIDS2017]]
- [[CICFlowMeter_Features]]
- [[Workshop_Konzept]]
