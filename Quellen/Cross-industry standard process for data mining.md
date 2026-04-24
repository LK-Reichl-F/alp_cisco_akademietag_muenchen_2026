---
title: "Cross-industry standard process for data mining"
source: "https://en.wikipedia.org/wiki/Cross-industry_standard_process_for_data_mining#/media/File:CRISP-DM_Process_Diagram.png"
author:
  - "[[Wikipedia]]"
published:
created: 2026-04-24
description:
tags:
  - "clippings"
---
**The Cross-industry standard process for data mining**, known as **CRISP-DM**,[^1] is an [open standard](https://en.wikipedia.org/wiki/Open_standard "Open standard") process model that describes common approaches used by [data mining](https://en.wikipedia.org/wiki/Data_mining "Data mining") experts. It is the most widely-used [analytics](https://en.wikipedia.org/wiki/Analytics "Analytics") model.[^2]

In 2015, [IBM](https://en.wikipedia.org/wiki/IBM "IBM") released a new methodology called *[Analytics Solutions Unified Method](https://en.wikipedia.org/w/index.php?title=Analytics_Solutions_Unified_Method&action=edit&redlink=1 "Analytics Solutions Unified Method (page does not exist)") for Data Mining/Predictive Analytics* [^3] [^4] (also known as ASUM-DM), which refines and extends CRISP-DM.

## History

CRISP-DM was conceived in 1996 and became a European Union project under the [ESPRIT](https://en.wikipedia.org/wiki/European_Strategic_Program_on_Research_in_Information_Technology "European Strategic Program on Research in Information Technology") funding initiative in 1997. The project was led by five companies: [Integral Solutions Ltd (ISL)](https://en.wikipedia.org/w/index.php?title=Integral_Solutions_Ltd_\(ISL\)&action=edit&redlink=1 "Integral Solutions Ltd (ISL) (page does not exist)"), [Teradata](https://en.wikipedia.org/wiki/Teradata "Teradata"), [Daimler AG](https://en.wikipedia.org/wiki/Daimler_AG "Daimler AG"), [NCR Corporation](https://en.wikipedia.org/wiki/NCR_Corporation "NCR Corporation"), and [OHRA](https://en.wikipedia.org/w/index.php?title=OHRA&action=edit&redlink=1 "OHRA (page does not exist)"), an insurance company.

This core consortium brought different experiences to the project. ISL, was later acquired and merged into [SPSS](https://en.wikipedia.org/wiki/SPSS_Inc. "SPSS Inc."). The computer giant NCR Corporation produced the Teradata [data warehouse](https://en.wikipedia.org/wiki/Data_warehouse "Data warehouse") and its own data mining software. Daimler-Benz had a significant data mining team. OHRA was starting to explore the potential use of data mining.

The first version of the methodology was presented at the 4th CRISP-DM SIG Workshop in Brussels in March 1999,[^5] and published as a step-by-step data mining guide later that year.[^6]

Between 2006 and 2008, a CRISP-DM 2.0 SIG was formed, and there were discussions about updating the CRISP-DM process model.[^7] The current status of these efforts is not known. However, the original crisp-dm.org website cited in the reviews,[^8] [^9] and the CRISP-DM 2.0 SIG website are both no longer active.[^7]

While many non-IBM data mining practitioners use CRISP-DM,[^10] [^11] [^12] IBM is the primary corporation that currently uses the CRISP-DM process model. It makes some of the old CRISP-DM documents available for download and it has incorporated it into its [SPSS Modeler](https://en.wikipedia.org/wiki/SPSS_Modeler "SPSS Modeler") product.[^6]

Based on current research, CRISP-DM is the most widely used form of data-mining model because of its various advantages which solved the existing problems in the data mining industries. Some of the drawbacks of this model is that it does not perform project management activities. The success of CRISP-DM is largely attributable to the fact that it is industry, tool, and application neutral.[^13] [^14]

## Major phases

![](https://upload.wikimedia.org/wikipedia/commons/thumb/b/b9/CRISP-DM_Process_Diagram.png/330px-CRISP-DM_Process_Diagram.png)

Process diagram showing the relationship between the different phases of CRISP-DM

CRISP-DM breaks the process of [data mining](https://en.wikipedia.org/wiki/Data_mining "Data mining") into six major phases:[^15]

- Business Understanding
- Data Understanding
- Data Preparation
- Modeling
- Evaluation
- Deployment

The sequence of the phases is not strict and moving back and forth between different phases is usually required. The arrows in the process diagram indicate the most important and frequent dependencies between phases. The outer circle in the diagram symbolizes the cyclic nature of data mining itself. A data mining process continues after a solution has been deployed. The lessons learned during the process can trigger new, often more focused business questions, and subsequent data mining processes will benefit from the experiences of previous ones.

## Polls and Alternative Process Frameworks

Polls conducted at the same website ([KDNuggets](https://en.wikipedia.org/wiki/KDnuggets "KDnuggets")) in 2002, 2004, 2007, and 2014 show that it was the leading methodology used by industry data miners who decided to respond to the survey.[^10] [^11] [^12] [^16] The only other data mining approach named in these polls was [SEMMA](https://en.wikipedia.org/wiki/SEMMA "SEMMA"). However, SAS Institute clearly states that SEMMA is not a data mining methodology, but rather a "logical organization of the functional toolset of SAS Enterprise Miner." A review and critique of data mining process models in 2009 called the CRISP-DM the "de facto standard for developing data mining and knowledge discovery projects." [^17] Other reviews of CRISP-DM and data mining process models include Kurgan and Musilek's 2006 review,[^8] and Azevedo and Santos' 2008 comparison of CRISP-DM and SEMMA.[^9] Efforts to update the methodology started in 2006, but have, as of June 2015, not led to a new version, and the "Special Interest Group" (SIG) responsible along with the website has long disappeared (see [History of CRISP-DM](#History)).

In 2024, [Harvard Business Review](https://en.wikipedia.org/wiki/Harvard_Business_Review "Harvard Business Review") published an updated framework, bizML, that is designed for greater relevance to business personnel and to be specific for [machine learning](https://en.wikipedia.org/wiki/Machine_learning "Machine learning") projects in particular, rather than for [analytics](https://en.wikipedia.org/wiki/Analytics "Analytics"), [data science](https://en.wikipedia.org/wiki/Data_science "Data science"), or [data mining](https://en.wikipedia.org/wiki/Data_mining "Data mining") projects in general.[^18]

## References

[^1]: Shearer C., *The CRISP-DM model: the new blueprint for data mining*, J Data Warehousing (2000); 5:13—22.

[^2]: [What IT Needs To Know About The Data Mining Process](https://www.forbes.com/sites/metabrown/2015/07/29/what-it-needs-to-know-about-the-data-mining-process/#2065f3a3515f) Published by Forbes, 29 July 2015, retrieved June 24, 2018

[^3]: [Have you seen ASUM-DM?](https://developer.ibm.com/predictiveanalytics/2015/10/16/have-you-seen-asum-dm/), By Jason Haffar, 16 October 2015, SPSS Predictive Analytics, IBM [Archived](https://web.archive.org/web/20160308065035/https://developer.ibm.com/predictiveanalytics/2015/10/16/have-you-seen-asum-dm/) 8 March 2016 at the [Wayback Machine](https://en.wikipedia.org/wiki/Wayback_Machine "Wayback Machine")

[^4]: [Analytics Solutions Unified Method - Implementations with Agile principles](https://public.dhe.ibm.com/software/data/sw-library/services/ASUM.pdf) Published by IBM, 1 March 2016, retrieved October 5, 2018

[^5]: Pete Chapman (1999); [*The CRISP-DM User Guide*](https://s2.smu.edu/~mhd/8331f03/crisp.pdf).

[^6]: Pete Chapman, Julian Clinton, Randy Kerber, Thomas Khabaza, Thomas Reinartz, Colin Shearer, and Rüdiger Wirth (2000); *The CRISP-DM User Guide* ([entry on semantic scholar, including links to PDFs](https://www.semanticscholar.org/paper/CRISP-DM-1.0%3A-Step-by-step-data-mining-guide-Chapman-Clinton/54bad20bbc7938991bf34f86dde0babfbd2d5a72)), ([PDF version with high-resolution graphics](https://www.the-modeling-agency.com/crisp-dm.pdf) [Archived](https://web.archive.org/web/20200912023158/https://www.the-modeling-agency.com/crisp-dm.pdf) 12 September 2020 at the [Wayback Machine](https://en.wikipedia.org/wiki/Wayback_Machine "Wayback Machine")).

[^7]: Colin Shearer (2006); [*First CRISP-DM 2.0 Workshop Held*](http://www.kdnuggets.com/news/2006/n19/4i.html)

[^8]: Lukasz Kurgan and Petr Musilek (2006); [*A survey of Knowledge Discovery and Data Mining process models*](http://journals.cambridge.org/action/displayAbstract?fromPage=online&aid=451120). The Knowledge Engineering Review. Volume 21 Issue 1, March 2006, pp 1–24, Cambridge University Press, New York, NY, USA doi: 10.1017/S0269888906000737.

[^9]: Azevedo, A. and Santos, M. F. (2008); [KDD, SEMMA and CRISP-DM: a parallel overview](http://recipp.ipp.pt/bitstream/10400.22/136/3/KDD-CRISP-SEMMA.pdf). In Proceedings of the IADIS European Conference on Data Mining 2008, pp 182–185.

[^10]: Gregory Piatetsky-Shapiro (2002); [*KDnuggets Methodology Poll*](http://www.kdnuggets.com/polls/2002/methodology.htm)

[^11]: Gregory Piatetsky-Shapiro (2004); [*KDnuggets Methodology Poll*](http://www.kdnuggets.com/polls/2004/data_mining_methodology.htm)

[^12]: Gregory Piatetsky-Shapiro (2007); [*KDnuggets Methodology Poll*](http://www.kdnuggets.com/polls/2007/data_mining_methodology.htm)

[^13]: Mariscal, G., Marban, O., Fernandez, C. (2010). "A Survey of Data Mining and knowledge discovery process Models and methodologies". *The Knowledge Engineering Review*. **25** (2): 137–166. [doi](https://en.wikipedia.org/wiki/Doi_\(identifier\) "Doi (identifier)"):[10.1017/S0269888910000032](https://doi.org/10.1017%2FS0269888910000032). [S2CID](https://en.wikipedia.org/wiki/S2CID_\(identifier\) "S2CID (identifier)") [31359633](https://api.semanticscholar.org/CorpusID:31359633).

[^14]: Costa, C. J.; Aparicio, J. T. (2020). *POST-DS: A Methodology to Boost Data Science*. 2020 15th Iberian Conference on Information Systems and Technologies. Seville, Spain. pp. 1–6. [doi](https://en.wikipedia.org/wiki/Doi_\(identifier\) "Doi (identifier)"):[10.23919/CISTI49556.2020.9140932](https://doi.org/10.23919%2FCISTI49556.2020.9140932).

[^15]: Harper, Gavin; Stephen D. Pickett (August 2006). ["Methods for mining HTS data"](https://caridokumen.com/download/methods-for-mining-hts-data-_5a462410b7d7bc7b7af27f4a_pdf). *[Drug Discovery Today](https://en.wikipedia.org/wiki/Drug_Discovery_Today "Drug Discovery Today")*. **11** (15–16): 694–699. [doi](https://en.wikipedia.org/wiki/Doi_\(identifier\) "Doi (identifier)"):[10.1016/j.drudis.2006.06.006](https://doi.org/10.1016%2Fj.drudis.2006.06.006). [PMID](https://en.wikipedia.org/wiki/PMID_\(identifier\) "PMID (identifier)") [16846796](https://pubmed.ncbi.nlm.nih.gov/16846796).

[^16]: Gregory Piatetsky-Shapiro (2014); [*KDnuggets Methodology Poll*](http://www.kdnuggets.com/polls/2014/analytics-data-mining-data-science-methodology.html)

[^17]: Martínez-Plumed, Fernando; Contreras-Ochando, Lidia; Ferri, Cèsar; Flach, Peter; Hernández-Orallo, José; Kull, Meelis; Lachiche, Nicolas; Ramírez-Quintana, María José (19 September 2017). "CASP-DM: Context Aware Standard Process for Data Mining". [arXiv](https://en.wikipedia.org/wiki/ArXiv_\(identifier\) "ArXiv (identifier)"):[1709.09003](https://arxiv.org/abs/1709.09003) \[[cs.DB](https://arxiv.org/archive/cs.DB)\].

[^18]: Eric Siegel (2024); [*Getting Machine Learning Projects from Idea to Execution*](https://hbr.org/2024/01/getting-machine-learning-projects-from-idea-to-execution)