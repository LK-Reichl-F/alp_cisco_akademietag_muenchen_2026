---
title: "Orange Data Mining"
source: "https://orangedatamining.com/examples/?tag=Classification"
author:
  - "[[Bioinformatics Laboratory]]"
  - "[[University of Ljubljana]]"
published:
created: 2026-04-16
description: "Orange Data Mining Toolbox"
tags:
  - "clippings"
---
## Examples

- Classification Tree, Classification
	## Classification Tree
	This workflow combines the interface and visualization of classification trees with scatter plot. When both the tree viewer and the scatter plot are open, selection of any node of the tree sends the related data instances to scatter plot. In the workflow, the selected data is treated as a subset of the entire dataset and is highlighted in the scatter plot. With simple combination of widgets we have constructed an interactive classification tree browser.
	[Download](https://orangedatamining.com/examples/tree-scatterplot/250-tree-scatterplot.ows)
	![](https://orangedatamining.com/examples/tree-scatterplot/tree-scatterplot.png)
- Classification, Data Sampler, Predictive models
	## Train and Test Data
	In building predictive models it is important to have a separate train and test data sets in order to avoid overfitting and to properly score the models. Here we use Data Sampler to split the data into training and test data, use training data for building a model and, finally, test on test data. Try several other classifiers to see how the scores change.
	[Download](https://orangedatamining.com/examples/data-sampler/420-data-sampler.ows)
	![](https://orangedatamining.com/examples/data-sampler/data-sampler.png)
- Cross Validation, Predictive models, Classification
	## Cross Validation
	How good are supervised data mining methods on your classification dataset? Here's a workflow that scores various classification techniques on a dataset from medicine. The central widget here is the one for testing and scoring, which is given the data and a set of learners, does cross-validation and scores predictive accuracy, and outputs the scores for further examination.
	[Download](https://orangedatamining.com/examples/cross-validation/450-cross-validation.ows)
	![](https://orangedatamining.com/examples/cross-validation/cross-validation.png)
- Confusion Matrix, Classification, Scatter Plot
	## Where Are Misclassifications
	Cross-validation of, say, logistic regression can expose the data instances which were misclassified. There are six such instances for iris dataset and ridge-regularized logistic regression. We can select different types of misclassification in Confusion Matrix and highlight them in the Scatter Plot. No surprise: the misclassified instances are close to the class-bordering regions in the scatter plot projection.
	[Download](https://orangedatamining.com/examples/where-are-misclassifications/470-misclassification-scatterplot.ows)
	![](https://orangedatamining.com/examples/where-are-misclassifications/misclassifications.png)
- Text Mining, Classification, Nomogram, Bag of Words
	## Text Classification
	We can use predictive models to classify documents by authorship, their type, sentiment and so on. In this workflow we classify documents by their Aarne-Thompshon-Uther index, that is the defining topic of the tale. We use two simple learners, Logistic Regression and Naive Bayes, both of which can be inspected in the Nomogram.
	[Download](https://orangedatamining.com/examples/text-classification/630-text-classification.ows)
	![](https://orangedatamining.com/examples/text-classification/text-classification.png)