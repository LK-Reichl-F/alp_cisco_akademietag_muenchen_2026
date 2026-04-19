---
title: "undefined"
source: "https://orangedatamining.com/widget-catalog/model/tree/"
author:
  - "[[Bioinformatics Laboratory]]"
  - "[[University of Ljubljana]]"
published:
created: 2026-04-19
description: "Orange Data Mining Toolbox"
tags:
  - "clippings"
---
## Tree

A tree algorithm with forward pruning.

**Inputs**

**Outputs**

**Tree** is a simple algorithm that splits the data into nodes by class purity (information gain for categorical and MSE for numeric target variable). It is a precursor to [Random Forest](https://orangedatamining.com/widget-catalog/model/randomforest). Tree in Orange is designed in-house and can handle both categorical and numeric datasets.

It can also be used for both classification and regression tasks.

[![](https://orangedatamining.com/widget-catalog/model/images/__optimized-images__/Tree-stamped.png)](https://orangedatamining.com/widget-catalog/model/images/__optimized-images__/Tree-stamped.png)
1. The learner can be given a name under which it will appear in other widgets. The default name is "Tree".
2. Tree parameters:
	- **Induce binary tree**: build a binary tree (split into two child nodes)
		- **Min. number of instances in leaves**: if checked, the algorithm will never construct a split which would put less than the specified number of training examples into any of the branches.
		- **Do not split subsets smaller than**: forbids the algorithm to split the nodes with less than the given number of instances.
		- **Limit the maximal tree depth**: limits the depth of the classification tree to the specified number of node levels.
3. **Stop when majority reaches \[%\]**: stop splitting the nodes after a specified majority threshold is reached
4. Produce a report. After changing the settings, you need to click *Apply*, which will put the new learner on the output and, if the training examples are given, construct a new classifier and output it as well. Alternatively, tick the box on the left and changes will be communicated automatically.

## Preprocessing

Tree does not use any preprocessing.

## Examples

There are two typical uses for this widget. First, you may want to induce a model and check what it looks like in [Tree Viewer](https://orangedatamining.com/widget-catalog/visualize/treeviewer).

[![](https://orangedatamining.com/widget-catalog/model/images/__optimized-images__/Tree-classification-visualize.png)](https://orangedatamining.com/widget-catalog/model/images/__optimized-images__/Tree-classification-visualize.png)

The second schema trains a model and evaluates its performance against [Logistic Regression](https://orangedatamining.com/widget-catalog/model/logisticregression).

[![](https://orangedatamining.com/widget-catalog/model/images/__optimized-images__/Tree-classification-model.png)](https://orangedatamining.com/widget-catalog/model/images/__optimized-images__/Tree-classification-model.png)

We used the *iris* dataset in both examples. However, **Tree** works for regression tasks as well. Use *housing* dataset and pass it to **Tree**. The selected tree node from [Tree Viewer](https://orangedatamining.com/widget-catalog/visualize/treeviewer) is presented in the [Scatter Plot](https://orangedatamining.com/widget-catalog/visualize/scatterplot) and we can see that the selected examples exhibit the same features.

[![](https://orangedatamining.com/widget-catalog/model/images/__optimized-images__/Tree-regression-subset.png)](https://orangedatamining.com/widget-catalog/model/images/__optimized-images__/Tree-regression-subset.png)