---
title: "UNSW-NB15 Augmented Dataset | Datasets | Research | Canadian Institute for Cybersecurity"
source: "https://www.unb.ca/cic/datasets/cic-unsw-nb15.html"
author:
published:
created: 2026-04-16
description: "UNSW-NB15 used the IXIA PerfectStorm tool to generate the dataset to create modern normal and abnormal network traffic."
tags:
  - "clippings"
---
## Global Site Navigation (use tab and down arrow)

## CIC UNSW-NB15 Augmented Dataset

[UNSW-NB15](https://research.unsw.edu.au/projects/unsw-nb15-dataset) used the IXIA PerfectStorm tool to generate the dataset to create modern normal and abnormal network traffic. Their dataset includes nine attack categories and benign traffic. They captured 100GBs of network traffic in two days, and to extract features from the captured network traffic, they used Argus and Bro-IDS tools. They extracted 47 features in categories, including Basic, Content, Time, and additional generated features. In the following, we briefly explain each attack category in the dataset.

- **Fuzzers:** A fuzzer attack, or fuzzing, is a technique used to discover vulnerabilities in software. It involves sending unexpected or random input data to an application to see how it responds. Overwhelming the application with varied inputs can identify weaknesses or flaws. Fuzzing is an automated process using specialized tools called fuzzers. When a vulnerability is found, attackers can further analyze it and potentially exploit it.
- **Analysis:** This attack is a method where attackers gather and study information to exploit vulnerabilities in a system. This attack involves techniques such as traffic analysis, cryptographic analysis, code analysis, data analysis, and protocol analysis. Attackers use these techniques to gain insights, extract sensitive data, or identify weaknesses that can be exploited for malicious purposes.
- **Backdoor:** A backdoor attack is a cybersecurity threat where unauthorized access is gained to a computer system or network by exploiting hidden vulnerabilities or intentionally creating openings. It involves the insertion of malicious code or modifications to existing code within a system, allowing attackers to bypass standard security measures and gain control over the targeted system to perform various malicious activities, such as stealing sensitive data, installing additional malware, or launching further attacks on the system or network.
- **Exploit:** An exploit attack refers to exploiting computer systems or software vulnerabilities to gain unauthorized access or perform malicious activities. Exploits take advantage of weaknesses or flaws in a system's design or implementation, allowing attackers to execute specific commands or actions not intended by the system's developers. These vulnerabilities can exist in various components, such as operating systems, applications, or network protocols.
- **Generic:** It is a kind of attack against the cryptography systems, which can run against all block-ciphers independently of their structure.
- **Reconnaissance:** This attack, also known as information gathering or footprinting, is a cyber attack that focuses on gathering valuable intelligence and information about a target system or network. The main objective of a reconnaissance attack is to gain a deeper understanding of the target's infrastructure, vulnerabilities, and potential entry points without directly causing any damage.
- **Shellcode:** The term shellcode refers to a small piece of code that is injected into a vulnerable program, typically to gain unauthorized access and control over the system. The attacker first identifies a vulnerability in the target software, such as a buffer overflow or a code injection flaw. They then craft a payload, usually written in assembly language or machine code and designed to perform specific actions once executed. This payload is the shellcode.
- **Worms:** This malicious cyber-attack spreads through computer networks, targeting vulnerable systems and exploiting security vulnerabilities. Unlike viruses or Trojans, worms do not require user interaction to propagate. They can independently replicate and spread across a network, infecting multiple computers and devices.

## CIC-UNSW-NB15

To generate the CIC-UNSW-NB15 we used [CICFlowMeter](https://www.unb.ca/cic/datasets/flowmeter.html) to extract the new set of features from the provided captured network traffic data by the UNSW-NB15.

After extracting the flows using CICFlowMeter, we need to label them using the ground truth from the original dataset files. We matched the extracted flows with the records in the ground truth file based on the source IP, destination IP, source port, destination port, and protocol.

If any flows match with a record from the ground truth file, we set the label using the ground truth attack category. If the flow is matched with more than one record from the ground truth file, we compare the timestamps and choose the record's label that matches the flow timestamp.

In the worst case, the flow will be dropped even if we cannot decide on the label by comparing the timestamp. Any remaining flows will be labeled benign after labeling all the malicious flows.

| Category | Original Dataset | CICFlowMeter | CIC-UNSW-NB15 |
| --- | --- | --- | --- |
| **Benign** | 2218764 | 3450658 | 358332 |
| **Analysis** | 2677 | 385 | 385 |
| **Backdoor** | 2329 | 452 | 452 |
| **DoS** | 16353 | 4467 | 4467 |
| **Exploits** | 44525 | 30951 | 30951 |
| **Fuzzers** | 24246 | 29613 | 29613 |
| **Generic** | 215481 | 4632 | 4632 |
| **Reconnaissance** | 13987 | 16735 | 16735 |
| **Shellcode** | 1511 | 2102 | 2102 |
| **Worms** | 174 | 246 | 246 |

The above table includes the details of the original UNSW-NB15 dataset and the extracted flows using CICFlowMeter. In most of the network traffic datasets to be closer to the real world, they keep the ratio between the benign and malicious samples 80 percent to 20 percent.

To gain this ratio, we keep all the malicious flows extracted by the CICFlowMeter and randomly sample the required number of flows from the benign flows. The last column of the table shows the final details of the newly generated dataset.

Since we used the raw packet files from UNSW-NB15 and the CICFlowMeter to generate this dataset and augment UNSW-NB15, we will call it CIC-UNSW-NB15.

## Dataset files

The CIC-UNSW-NB15 dataset directory includes four files:

- **CICFlowMeter\_out.csv:** Includes the extracted and labeled flows using the CICFlowMeter (CICFlowMeter column in the above table).
- **Data.csv:** Includes the extracted flows for the 80-20 ratio dataset (CIC-UNSW-NB15 column in the above table).
- **Label.csv:** Includes the numerical labels for the 80-20 ratio dataset.
- **Readme.txt:** Includes the labels and their respective numerical values.

## Citation

H. Mohammadian, A. H. Lashkari, A. Ghorbani. “ [Poisoning and Evasion: Deep Learning-Based NIDS under Adversarial Attacks](https://www.researchgate.net/publication/387115398_Poisoning_and_Evasion_Deep_Learning-Based_NIDS_under_Adversarial_Attacks),” 21st Annual International Conference on Privacy, Security and Trust (PST), 2024.

[Download the dataset](http://cicresearch.ca//CICDataset/CIC-UNSW/)