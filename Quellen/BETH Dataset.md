---
title: "BETH Dataset"
source: "https://www.kaggle.com/datasets/katehighnam/beth-dataset"
author:
published:
created: 2026-04-16
description: "Real Cybersecurity Data for Anomaly Detection Research"
tags:
  - "clippings"
---
Kaggle uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic.

OK, Got it.

Kate Highnam · Updated 5 years ago

Real Cybersecurity Data for Anomaly Detection Research

## BETH Dataset

## About Dataset

This dataset corresponds to the paper ["BETH Dataset: Real Cybersecurity Data for Anomaly Detection Research"](http://www.gatsby.ucl.ac.uk/~balaji/udl2021/accepted-papers/UDL2021-paper-033.pdf) by **Kate Highnam** \* (@jinxmirror13), **Kai Arulkumaran** \* (@kaixhin), **Zachary Hanif** \*, and **Nicholas R. Jennings** (@LboroVC).

This paper was published in the [ICML](https://icml.cc/) Workshop on [Uncertainty and Robustness in Deep Learning 2021](https://sites.google.com/view/udlworkshop2021/home) and [Conference on Applied Machine Learning for Information Security (CAMLIS 2021)](https://www.camlis.org/2021/schedule)

---

## THIS DATASET IS STILL BEING UPDATED

---

### Context

When deploying machine learning (ML) models in the real world, anomalous data points and shifts in the data distribution are inevitable. From a cyber security perspective, these anomalies and dataset shifts are driven by both defensive and adversarial advancement. To withstand the cost of critical system failure, the development of robust models is therefore key to the performance, protection, and longevity of deployed defensive systems.

We present the BPF-extended tracking honeypot (BETH) dataset as the first cybersecurity dataset for uncertainty and robustness benchmarking. Collected using a novel honeypot tracking system, our dataset has the following properties that make it attractive for the development of robust ML methods:

1. At over eight million data points, this is one of the largest cyber security datasets available
2. It contains modern host activity and attacks
3. It is fully labelled
4. It contains highly structured but heterogeneous features
5. Each host contains benign activity and at most a single attack, which is ideal for behavioural analysis and other research tasks. In addition to the described dataset

Further data is currently being collected and analysed to add alternative attack vectors to the dataset.

There are several existing cyber security datasets used in ML research, including the KDD Cup 1999 Data (Hettich & Bay, 1999), the 1998 DARPA Intrusion Detection Evaluation Dataset (Labs, 1998; Lippmann et al., 2000), the ISCX IDS 2012 dataset (Shiravi et al., 2012), and NSL-KDD (Tavallaee et al., 2009), which primarily removes duplicates from the KDD Cup 1999 Data. Each includes millions of records of realistic activity for enterprise applications, with labels for attacks or benign activity. The KDD1999, NSLKDD, and ISCX datasets contain network traffic, while the DARPA1998 dataset also includes limited process calls. However, these datasets are at best almost a decade old, and are collected on in-premise servers. In contrast, BETH contains modern host activity and activity collected from cloud services, making it relevant for current real-world deployments. In addition, some datasets include artificial user activity (Shiravi et al., 2012) while BETH contains only real activity. BETH is also one of the few datasets to include both kernel-process and network logs, providing a holistic view of malicious behaviour.

### Content

The BETH dataset currently represents 8,004,918 events collected over 23 honeypots, running for about five noncontiguous hours on a major cloud provider. For benchmarking and discussion, we selected the initial subset of the process logs. This subset was further divided into training, validation, and testing sets with a rough 60/20/20 split based on host, quantity of logs generated, and the activity logged—only the test set includes an attack

The dataset is composed of two sensor logs: kernel-level process calls and network traffic. The initial benchmark subset only includes process logs. Each process call consists of 14 raw features and 2 hand-crafted labels.

See [the paper](http://www.gatsby.ucl.ac.uk/~balaji/udl2021/accepted-papers/UDL2021-paper-033.pdf) for more details. For details on the events recorded within the logs, see [this report](https://docs.google.com/document/d/1WuplS5KKBRtw5edQS_HxlhXNrhTBmhio2pLR0zUCzEk/edit?usp=sharing).

### Benchmarks

Code for our benchmarks, as detailed in the paper, are available through Github at: [https://github.com/jinxmirror13/BETH\_Dataset\_Analysis](https://github.com/jinxmirror13/BETH_Dataset_Analysis)

### Acknowledgements

Thank you to Dr. Arinbjörn Kolbeinsson for his assistance in analysing the data and the reviewers for their positive feedback.

## Usability

info

8.24

## License

[CC0: Public Domain](https://creativecommons.org/publicdomain/zero/1.0/)

## Expected update frequency

Monthly

## Tags

## labelled\_2021may-ip-10-100-1-105-dns.csv(40.35 kB)

get\_app

fullscreen

chevron\_right

| DateTime | Count |
| --- | --- |
| 05/16/2021 - 05/16/2021 | 61 |
| 05/16/2021 - 05/16/2021 | 46 |
| 05/16/2021 - 05/16/2021 | 20 |
| 05/16/2021 - 05/16/2021 | 21 |
| 05/16/2021 - 05/16/2021 | 22 |
| 05/16/2021 - 05/16/2021 | 1 |
| 05/16/2021 - 05/16/2021 | 21 |
| 05/16/2021 - 05/16/2021 | 20 |
| 05/16/2021 - 05/16/2021 | 12 |
| 05/16/2021 - 05/16/2021 | 45 |

2021-05-16

2021-05-16

10.100.0.248%

10.100.1.9513%

Other (103)38%

10.100.0.248%

10.100.1.9514%

Other (102)38%

ssm.us-east-2.amazonaws.com83%

motd.ubuntu.com3%

Other (37)14%

\[null\]76%

\['52.95.19.240'\]7%

Other (46)17%

\[null\]76%

\['17'\]1%

Other (62)23%

ssm.us-east-2.amazonaws.com83%

motd.ubuntu.com3%

Other (37)14%

\['IN'\]99%

\['CH'\]1%

\['A'\]47%

\['AAAA'\]47%

Other (17)6%

| Label | Count |
| --- | --- |
| 0.00 - 0.80 | 204 |
| 0.80 - 1.60 | 55 |
| 1.60 - 2.40 | 7 |
| 4.80 - 5.60 | 1 |
| 5.60 - 6.40 | 1 |
| 7.20 - 8.00 | 1 |

0

8

2021-05-16T17:13:14Z 10.100.1.95 10.100.0.2 ssm.us-east-2.amazonaws.com ssm.us-east-2.amazonaws.com \['IN'\] \['A'\] 0 2021-05-16T17:13:14Z 10.100.0.2 10.100.1.95 ssm.us-east-2.amazonaws.com \['52.95.19.240'\] \['17'\] ssm.us-east-2.amazonaws.com \['IN'\] \['A'\] 1 2021-05-16T17:13:14Z 10.100.1.95 10.100.0.2 ssm.us-east-2.amazonaws.com ssm.us-east-2.amazonaws.com \['IN'\] \['AAAA'\] 0 2021-05-16T17:13:14Z 10.100.0.2 10.100.1.95 ssm.us-east-2.amazonaws.com ssm.us-east-2.amazonaws.com \['IN'\] \['AAAA'\] 0 2021-05-16T17:13:16Z 10.100.1.186 10.100.0.2 ssm.us-east-2.amazonaws.com ssm.us-east-2.amazonaws.com \['IN'\] \['A'\] 0 2021-05-16T17:13:16Z 10.100.0.2 10.100.1.186 ssm.us-east-2.amazonaws.com \['52.95.21.209'\] \['41'\] ssm.us-east-2.amazonaws.com \['IN'\] \['A'\] 1 2021-05-16T17:13:16Z 10.100.1.186 10.100.0.2 ssm.us-east-2.amazonaws.com ssm.us-east-2.amazonaws.com \['IN'\] \['AAAA'\] 0 2021-05-16T17:13:17Z 10.100.0.2 10.100.1.186 ssm.us-east-2.amazonaws.com ssm.us-east-2.amazonaws.com \['IN'\] \['AAAA'\] 0 2021-05-16T17:13:17Z 10.100.1.105 10.100.0.2 ssm.us-east-2.amazonaws.com ssm.us-east-2.amazonaws.com \['IN'\] \['A'\] 0 2021-05-16T17:13:17Z 10.100.1.105 10.100.0.2 ssm.us-east-2.amazonaws.com ssm.us-east-2.amazonaws.com \['IN'\] \['AAAA'\] 0 2021-05-16T17:13:17Z 10.100.0.2 10.100.1.105 ssm.us-east-2.amazonaws.com \['52.95.21.209'\] \['40'\] ssm.us-east-2.amazonaws.com \['IN'\] \['A'\] 1 2021-05-16T17:13:17Z 10.100.0.2 10.100.1.105 ssm.us-east-2.amazonaws.com ssm.us-east-2.amazonaws.com \['IN'\] \['AAAA'\] 0 2021-05-16T17:13:20Z 10.100.1.26 10.100.0.2 ssm.us-east-2.amazonaws.com ssm.us-east-2.amazonaws.com \['IN'\] \['A'\] 0 2021-05-16T17:13:20Z 10.100.0.2 10.100.1.26 ssm.us-east-2.amazonaws.com \['52.95.19.240'\] \['26'\] ssm.us-east-2.amazonaws.com \['IN'\] \['A'\] 1 2021-05-16T17:13:20Z 10.100.1.26 10.100.0.2 ssm.us-east-2.amazonaws.com ssm.us-east-2.amazonaws.com \['IN'\] \['AAAA'\] 0 2021-05-16T17:13:20Z 10.100.0.2 10.100.1.26 ssm.us-east-2.amazonaws.com ssm.us-east-2.amazonaws.com \['IN'\] \['AAAA'\] 0 2021-05-16T17:13:20Z 10.100.1.4 10.100.0.2 ssm.us-east-2.amazonaws.com ssm.us-east-2.amazonaws.com \['IN'\] \['A'\] 0 2021-05-16T17:13:20Z 10.100.0.2 10.100.1.4 ssm.us-east-2.amazonaws.com \['52.95.21.209'\] \['39'\] ssm.us-east-2.amazonaws.com \['IN'\] \['A'\] 1 2021-05-16T17:13:20Z 10.100.1.4 10.100.0.2 ssm.us-east-2.amazonaws.com ssm.us-east-2.amazonaws.com \['IN'\] \['AAAA'\] 0 2021-05-16T17:13:20Z 10.100.0.2 10.100.1.4 ssm.us-east-2.amazonaws.com ssm.us-east-2.amazonaws.com \['IN'\] \['AAAA'\] 0 2021-05-16T17:23:13Z 10.100.1.95 10.100.0.2 ssm.us-east-2.amazonaws.com ssm.us-east-2.amazonaws.com \['IN'\] \['A'\] 0 2021-05-16T17:23:13Z 10.100.1.95 10.100.0.2 ssm.us-east-2.amazonaws.com ssm.us-east-2.amazonaws.com \['IN'\] \['AAAA'\] 0 2021-05-16T17:23:13Z 10.100.0.2 10.100.1.95 ssm.us-east-2.amazonaws.com \['52.95.22.56'\] \['16'\] ssm.us-east-2.amazonaws.com \['IN'\] \['A'\] 1 2021-05-16T17:23:13Z 10.100.0.2 10.100.1.95 ssm.us-east-2.amazonaws.com ssm.us-east-2.amazonaws.com \['IN'\] \['AAAA'\] 0 2021-05-16T17:23:16Z 10.100.1.186 10.100.0.2 ssm.us-east-2.amazonaws.com ssm.us-east-2.amazonaws.com \['IN'\] \['A'\] 0 2021-05-16T17:23:16Z 10.100.1.186 10.100.0.2 ssm.us-east-2.amazonaws.com ssm.us-east-2.amazonaws.com \['IN'\] \['AAAA'\] 0 2021-05-16T17:23:16Z 10.100.0.2 10.100.1.186 ssm.us-east-2.amazonaws.com \['52.95.19.240'\] \['48'\] ssm.us-east-2.amazonaws.com \['IN'\] \['A'\] 1 2021-05-16T17:23:16Z 10.100.0.2 10.100.1.186 ssm.us-east-2.amazonaws.com ssm.us-east-2.amazonaws.com \['IN'\] \['AAAA'\] 0 2021-05-16T17:23:17Z 10.100.1.105 10.100.0.2 ssm.us-east-2.amazonaws.com ssm.us-east-2.amazonaws.com \['IN'\] \['A'\] 0 2021-05-16T17:23:17Z 10.100.0.2 10.100.1.105 ssm.us-east-2.amazonaws.com \['52.95.22.56'\] \['10'\] ssm.us-east-2.amazonaws.com \['IN'\] \['A'\] 1 2021-05-16T17:23:17Z 10.100.1.105 10.100.0.2 ssm.us-east-2.amazonaws.com ssm.us-east-2.amazonaws.com \['IN'\] \['AAAA'\] 0 2021-05-16T17:23:17Z 10.100.0.2 10.100.1.105 ssm.us-east-2.amazonaws.com ssm.us-east-2.amazonaws.com \['IN'\] \['AAAA'\] 0 2021-05-16T17:23:20Z 10.100.1.26 10.100.0.2 ssm.us-east-2.amazonaws.com ssm.us-east-2.amazonaws.com \['IN'\] \['A'\] 0 2021-05-16T17:23:20Z 10.100.0.2 10.100.1.26 ssm.us-east-2.amazonaws.com \['52.95.21.209'\] \['25'\] ssm.us-east-2.amazonaws.com \['IN'\] \['A'\] 1 2021-05-16T17:23:20Z 10.100.1.26 10.100.0.2 ssm.us-east-2.amazonaws.com ssm.us-east-2.amazonaws.com \['IN'\] \['AAAA'\] 0 2021-05-16T17:23:20Z 10.100.0.2 10.100.1.26 ssm.us-east-2.amazonaws.com ssm.us-east-2.amazonaws.com \['IN'\] \['AAAA'\] 0 2021-05-16T17:23:20Z 10.100.1.4 10.100.0.2 ssm.us-east-2.amazonaws.com ssm.us-east-2.amazonaws.com \['IN'\] \['A'\] 0 2021-05-16T17:23:20Z 10.100.1.4 10.100.0.2 ssm.us-east-2.amazonaws.com ssm.us-east-2.amazonaws.com \['IN'\] \['AAAA'\] 0 2021-05-16T17:23:20Z 10.100.0.2 10.100.1.4 ssm.us-east-2.amazonaws.com \['52.95.22.56'\] \['17'\] ssm.us-east-2.amazonaws.com \['IN'\] \['A'\] 1 2021-05-16T17:23:20Z 10.100.0.2 10.100.1.4 ssm.us-east-2.amazonaws.com ssm.us-east-2.amazonaws.com \['IN'\] \['AAAA'\] 0 2021-05-16T17:28:27Z 141.212.123.189 10.100.1.26 researchscan541.eecs.umich.edu researchscan541.eecs.umich.edu \['IN'\] \['A'\] 0 2021-05-16T17:33:13Z 10.100.1.95 10.100.0.2 ssm.us-east-2.amazonaws.com ssm.us-east-2.amazonaws.com \['IN'\] \['A'\] 0 2021-05-16T17:33:13Z 10.100.0.2 10.100.1.95 ssm.us-east-2.amazonaws.com \['52.95.22.56'\] \['20'\] ssm.us-east-2.amazonaws.com \['IN'\] \['A'\] 1 2021-05-16T17:33:13Z 10.100.1.95 10.100.0.2 ssm.us-east-2.amazonaws.com ssm.us-east-2.amazonaws.com \['IN'\] \['AAAA'\] 0 2021-05-16T17:33:13Z 10.100.0.2 10.100.1.95 ssm.us-east-2.amazonaws.com ssm.us-east-2.amazonaws.com \['IN'\] \['AAAA'\] 0 2021-05-16T17:33:16Z 10.100.1.186 10.100.0.2 ssm.us-east-2.amazonaws.com ssm.us-east-2.amazonaws.com \['IN'\] \['A'\] 0 2021-05-16T17:33:16Z 10.100.0.2 10.100.1.186 ssm.us-east-2.amazonaws.com \['52.95.19.240'\] \['14'\] ssm.us-east-2.amazonaws.com \['IN'\] \['A'\] 1 2021-05-16T17:33:16Z 10.100.1.186 10.100.0.2 ssm.us-east-2.amazonaws.com ssm.us-east-2.amazonaws.com \['IN'\] \['AAAA'\] 0 2021-05-16T17:33:16Z 10.100.0.2 10.100.1.186 ssm.us-east-2.amazonaws.com ssm.us-east-2.amazonaws.com \['IN'\] \['AAAA'\] 0 2021-05-16T17:33:17Z 10.100.1.105 10.100.0.2 ssm.us-east-2.amazonaws.com ssm.us-east-2.amazonaws.com \['IN'\] \['A'\] 0

## Data Explorer

(928.19 MB)

- labelled\_2021may-ip-10-100-1-105-dns.csv
- labelled\_2021may-ip-10-100-1-105.csv
- labelled\_2021may-ip-10-100-1-186-dns.csv
- labelled\_2021may-ip-10-100-1-186.csv
- labelled\_2021may-ip-10-100-1-26-dns.csv
- labelled\_2021may-ip-10-100-1-26.csv
- labelled\_2021may-ip-10-100-1-4-dns.csv
- labelled\_2021may-ip-10-100-1-4.csv
- labelled\_2021may-ip-10-100-1-95-dns.csv
- labelled\_2021may-ip-10-100-1-95.csv
- labelled\_2021may-ubuntu-dns.csv
- labelled\_2021may-ubuntu.csv
- labelled\_testing\_data.csv
- labelled\_training\_data.csv
- labelled\_validation\_data.csv

## Summary

15 files

216 columns

## See what others are saying about this dataset

### What have you used this dataset for?

### How would you describe this dataset?

## Metadata

### Collaborators

### Authors

### Coverage

### DOI Citation

### Provenance

### License

### Expected Update Frequency

## Activity Overview

### Views

65.4K

| date | Views |
| --- | --- |
| Mar 18, 2026 | 16 |
| Mar 19, 2026 | 35 |
| Mar 20, 2026 | 28 |
| Mar 21, 2026 | 30 |
| Mar 22, 2026 | 28 |
| Mar 23, 2026 | 64 |
| Mar 24, 2026 | 52 |
| Mar 25, 2026 | 49 |
| Mar 26, 2026 | 41 |
| Mar 27, 2026 | 38 |
| Mar 28, 2026 | 22 |
| Mar 29, 2026 | 42 |
| Mar 30, 2026 | 32 |
| Mar 31, 2026 | 27 |
| Apr 1, 2026 | 40 |
| Apr 2, 2026 | 49 |
| Apr 3, 2026 | 29 |
| Apr 4, 2026 | 43 |
| Apr 5, 2026 | 24 |
| Apr 6, 2026 | 35 |
| Apr 7, 2026 | 33 |
| Apr 8, 2026 | 37 |
| Apr 9, 2026 | 37 |
| Apr 10, 2026 | 35 |
| Apr 11, 2026 | 45 |
| Apr 12, 2026 | 27 |
| Apr 13, 2026 | 42 |
| Apr 14, 2026 | 42 |
| Apr 15, 2026 | 44 |

| date | Views |
| --- | --- |
| Mar 18, 2026 | 16 |
| Mar 19, 2026 | 35 |
| Mar 20, 2026 | 28 |
| Mar 21, 2026 | 30 |
| Mar 22, 2026 | 28 |
| Mar 23, 2026 | 64 |
| Mar 24, 2026 | 52 |
| Mar 25, 2026 | 49 |
| Mar 26, 2026 | 41 |
| Mar 27, 2026 | 38 |
| Mar 28, 2026 | 22 |
| Mar 29, 2026 | 42 |
| Mar 30, 2026 | 32 |
| Mar 31, 2026 | 27 |
| Apr 1, 2026 | 40 |
| Apr 2, 2026 | 49 |
| Apr 3, 2026 | 29 |
| Apr 4, 2026 | 43 |
| Apr 5, 2026 | 24 |
| Apr 6, 2026 | 35 |
| Apr 7, 2026 | 33 |
| Apr 8, 2026 | 37 |
| Apr 9, 2026 | 37 |
| Apr 10, 2026 | 35 |
| Apr 11, 2026 | 45 |
| Apr 12, 2026 | 27 |
| Apr 13, 2026 | 42 |
| Apr 14, 2026 | 42 |
| Apr 15, 2026 | 44 |

1066in the last 30 days

### Downloads

8306

| date | Downloads |
| --- | --- |
| Mar 18, 2026 | 9 |
| Mar 19, 2026 | 5 |
| Mar 20, 2026 | 5 |
| Mar 21, 2026 | 5 |
| Mar 22, 2026 | 4 |
| Mar 23, 2026 | 15 |
| Mar 24, 2026 | 12 |
| Mar 25, 2026 | 7 |
| Mar 26, 2026 | 2 |
| Mar 27, 2026 | 2 |
| Mar 28, 2026 | 3 |
| Mar 29, 2026 | 4 |
| Mar 30, 2026 | 2 |
| Mar 31, 2026 | 4 |
| Apr 1, 2026 | 4 |
| Apr 2, 2026 | 12 |
| Apr 3, 2026 | 7 |
| Apr 4, 2026 | 2 |
| Apr 5, 2026 | 3 |
| Apr 6, 2026 | 7 |
| Apr 7, 2026 | 9 |
| Apr 8, 2026 | 8 |
| Apr 9, 2026 | 5 |
| Apr 10, 2026 | 8 |
| Apr 11, 2026 | 1 |
| Apr 12, 2026 | 7 |
| Apr 13, 2026 | 9 |
| Apr 14, 2026 | 5 |

| date | Downloads |
| --- | --- |
| Mar 18, 2026 | 9 |
| Mar 19, 2026 | 5 |
| Mar 20, 2026 | 5 |
| Mar 21, 2026 | 5 |
| Mar 22, 2026 | 4 |
| Mar 23, 2026 | 15 |
| Mar 24, 2026 | 12 |
| Mar 25, 2026 | 7 |
| Mar 26, 2026 | 2 |
| Mar 27, 2026 | 2 |
| Mar 28, 2026 | 3 |
| Mar 29, 2026 | 4 |
| Mar 30, 2026 | 2 |
| Mar 31, 2026 | 4 |
| Apr 1, 2026 | 4 |
| Apr 2, 2026 | 12 |
| Apr 3, 2026 | 7 |
| Apr 4, 2026 | 2 |
| Apr 5, 2026 | 3 |
| Apr 6, 2026 | 7 |
| Apr 7, 2026 | 9 |
| Apr 8, 2026 | 8 |
| Apr 9, 2026 | 5 |
| Apr 10, 2026 | 8 |
| Apr 11, 2026 | 1 |
| Apr 12, 2026 | 7 |
| Apr 13, 2026 | 9 |
| Apr 14, 2026 | 5 |

166in the last 30 days

### Engagement

0.12704

downloads per view