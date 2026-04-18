# CICFlowMeter Features

**Zusammenfassung**: CICFlowMeter ist ein Tool des Canadian Institute for Cybersecurity, das aus PCAP-Dateien statistische Netzwerkflow-Features extrahiert. Die resultierenden CSV-Dateien sind Grundlage aller CIC-Datensätze.

**Quellen**: (Quelle: [[IDS 2018  Datasets  Research  Canadian Institute for Cybersecurity.md]]), (Quelle: [[IDS 2017  Datasets  Research  Canadian Institute for Cybersecurity.md]])

**Zuletzt aktualisiert**: 2026-04-16

---

## Was ist CICFlowMeter?

CICFlowMeter analysiert PCAP-Dateien und berechnet für jeden **Bidirektionalen Flow** (Biflow) über 80 statistische Merkmale. Ein Flow ist definiert durch:
- Quell-IP + Ziel-IP
- Quell-Port + Ziel-Port
- Protokoll

Ausgabe: CSV-Datei, eine Zeile pro Flow, mit Label (Angriffstyp oder „Benign").

## Für den Workshop besonders geeignete Features

Diese Features sind intuitiv verständlich für Netzwerktechniker:

| Feature | Beschreibung | Warum für Unterricht |
|---|---|---|
| `fl_dur` | Flow-Dauer (Mikrosekunden) | DoS-Flows sind extrem kurz oder lang je nach Typ |
| `tot_fw_pk` | Pakete in Vorwärtsrichtung | DDoS hat extrem hohe Werte |
| `tot_bw_pk` | Pakete in Rückwärtsrichtung | Bei DoS-Opfer: kaum Rückantworten |
| `fl_byt_s` | Byte-Rate des Flows | Unterschied normal vs. Flood sofort sichtbar |
| `fl_pkt_s` | Paketrate des Flows | Scan-Traffic: sehr hoch, sehr kurz |
| `syn_cnt` | Anzahl SYN-Pakete | SYN-Flood direkt erkennbar |
| `fin_cnt` | Anzahl FIN-Pakete | Normale Verbindungen enden mit FIN |
| `ack_cnt` | Anzahl ACK-Pakete | Verhältnis SYN/ACK → Connection State |
| `pkt_len_avg` | Durchschnittliche Paketgröße | Scan-Pakete: klein; Datenübertragung: groß |
| `down_up_ratio` | Download/Upload-Verhältnis | DDoS: Verhältnis kollabiert |

## Vollständige Feature-Liste (CICFlowMeter-V3)

### Flow-Eigenschaften
| Feature | Beschreibung |
|---|---|
| `fl_dur` | Flow-Dauer |
| `fl_byt_s` | Flow-Byte-Rate |
| `fl_pkt_s` | Flow-Paketrate |
| `fl_iat_avg` | Ø Zeit zwischen zwei Flows |
| `fl_iat_std` | Standardabweichung Zeit zwischen Flows |
| `fl_iat_max` | Maximale Zeit zwischen Flows |
| `fl_iat_min` | Minimale Zeit zwischen Flows |

### Paketanzahl
| Feature | Beschreibung |
|---|---|
| `tot_fw_pk` | Gesamtpakete vorwärts |
| `tot_bw_pk` | Gesamtpakete rückwärts |
| `tot_l_fw_pkt` | Gesamtgröße vorwärts (Bytes) |

### Paketgrößen – Vorwärtsrichtung
| Feature | Beschreibung |
|---|---|
| `fw_pkt_l_max` | Maximale Paketgröße vorwärts |
| `fw_pkt_l_min` | Minimale Paketgröße vorwärts |
| `fw_pkt_l_avg` | Ø Paketgröße vorwärts |
| `fw_pkt_l_std` | Stdabw. Paketgröße vorwärts |

### Paketgrößen – Rückwärtsrichtung
| Feature | Beschreibung |
|---|---|
| `Bw_pkt_l_max` | Maximale Paketgröße rückwärts |
| `Bw_pkt_l_min` | Minimale Paketgröße rückwärts |
| `Bw_pkt_l_avg` | Ø Paketgröße rückwärts |
| `Bw_pkt_l_std` | Stdabw. Paketgröße rückwärts |

### Inter-Arrival-Times (IAT) – Vorwärtsrichtung
| Feature | Beschreibung |
|---|---|
| `fw_iat_tot` | Gesamtzeit zwischen Vorwärtspaketen |
| `fw_iat_avg` | Ø Zeit zwischen Vorwärtspaketen |
| `fw_iat_std` | Stdabw. Zeit Vorwärtspakete |
| `fw_iat_max` | Max. Zeit zwischen Vorwärtspaketen |
| `fw_iat_min` | Min. Zeit zwischen Vorwärtspaketen |

### Inter-Arrival-Times (IAT) – Rückwärtsrichtung
| Feature | Beschreibung |
|---|---|
| `bw_iat_tot` | Gesamtzeit zwischen Rückwärtspaketen |
| `bw_iat_avg` | Ø Zeit zwischen Rückwärtspaketen |
| `bw_iat_std` | Stdabw. Zeit Rückwärtspakete |
| `bw_iat_max` | Max. Zeit zwischen Rückwärtspaketen |
| `bw_iat_min` | Min. Zeit zwischen Rückwärtspaketen |

### TCP-Flags
| Feature | Beschreibung |
|---|---|
| `fw_psh_flag` | PSH-Flags vorwärts |
| `bw_psh_flag` | PSH-Flags rückwärts |
| `fw_urg_flag` | URG-Flags vorwärts |
| `bw_urg_flag` | URG-Flags rückwärts |
| `fin_cnt` | FIN-Pakete gesamt |
| `syn_cnt` | SYN-Pakete gesamt |
| `rst_cnt` | RST-Pakete gesamt |
| `pst_cnt` | PUSH-Pakete gesamt |
| `ack_cnt` | ACK-Pakete gesamt |
| `urg_cnt` | URG-Pakete gesamt |
| `cwe_cnt` | CWE-Pakete gesamt |
| `ece_cnt` | ECE-Pakete gesamt |

### Header und Segmente
| Feature | Beschreibung |
|---|---|
| `fw_hdr_len` | Header-Bytes vorwärts |
| `bw_hdr_len` | Header-Bytes rückwärts |
| `fw_pkt_s` | Vorwärtspakete pro Sekunde |
| `bw_pkt_s` | Rückwärtspakete pro Sekunde |
| `fw_seg_avg` | Ø Segmentgröße vorwärts |
| `bw_seg_avg` | Ø Segmentgröße rückwärts |
| `fw_seg_min` | Min. Segmentgröße vorwärts |

### Gesamtpaketlängen
| Feature | Beschreibung |
|---|---|
| `pkt_len_min` | Minimale Flow-Länge |
| `pkt_len_max` | Maximale Flow-Länge |
| `pkt_len_avg` | Ø Flow-Länge |
| `pkt_len_std` | Stdabw. Flow-Länge |
| `pkt_len_va` | Min. Inter-Arrival-Time |
| `pkt_size_avg` | Ø Paketgröße |

### Verhältnisse und Bulk-Statistiken
| Feature | Beschreibung |
|---|---|
| `down_up_ratio` | Download/Upload-Verhältnis |
| `fw_byt_blk_avg` | Ø Bulk-Byte-Rate vorwärts |
| `fw_pkt_blk_avg` | Ø Bulk-Paketrate vorwärts |
| `fw_blk_rate_avg` | Ø Bulk-Rate vorwärts |
| `bw_byt_blk_avg` | Ø Bulk-Byte-Rate rückwärts |
| `bw_pkt_blk_avg` | Ø Bulk-Paketrate rückwärts |
| `bw_blk_rate_avg` | Ø Bulk-Rate rückwärts |

### Subflows
| Feature | Beschreibung |
|---|---|
| `subfl_fw_pk` | Ø Pakete pro Subflow vorwärts |
| `subfl_fw_byt` | Ø Bytes pro Subflow vorwärts |
| `subfl_bw_pkt` | Ø Pakete pro Subflow rückwärts |
| `subfl_bw_byt` | Ø Bytes pro Subflow rückwärts |

### Fenstergröße und Payload
| Feature | Beschreibung |
|---|---|
| `fw_win_byt` | Initial Window Bytes vorwärts |
| `bw_win_byt` | Initial Window Bytes rückwärts |
| `Fw_act_pkt` | Pakete mit TCP-Nutzdaten vorwärts |

### Aktiv/Inaktiv-Zeiten
| Feature | Beschreibung |
|---|---|
| `atv_avg` | Ø Aktiv-Zeit des Flows |
| `atv_std` | Stdabw. Aktiv-Zeit |
| `atv_max` | Max. Aktiv-Zeit |
| `atv_min` | Min. Aktiv-Zeit |
| `idl_avg` | Ø Idle-Zeit des Flows |
| `idl_std` | Stdabw. Idle-Zeit |
| `idl_max` | Max. Idle-Zeit |
| `idl_min` | Min. Idle-Zeit |

## Verwandte Seiten

- [[CICIDS2017]]
- [[CIC_IDS_2018]]
- [[CIC_UNSW_NB15]]
- [[Orange_Klassifikations_Workflow]]
