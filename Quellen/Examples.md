---
title: "Examples"
source: "https://orangedatamining.com/examples/"
author:
  - "[[Bioinformatics Laboratory]]"
  - "[[University of Ljubljana]]"
published:
created: 2026-04-16
description: "Orange Data Mining Toolbox"
tags:
  - "clippings"
---
- Data Table, Data Loading
	## File and Data Table
	The basic data mining units in Orange are called widgets. In this workflow, the File widget reads the data. File widget communicates this data to Data Table widget that shows the data in a spreadsheet. The output of File is connected to the input of Data Table.
	[Download](https://orangedatamining.com/examples/file-and-data-table-widget/110-file-and-data-table-widget.ows)
	![](https://orangedatamining.com/examples/file-and-data-table-widget/file-and-data-table-widget.png)
- Scatter Plot, Visualization
	## Interactive Visualizations
	Most visualizations in Orange are interactive. Scatter Plot for example. Double click its icon to open it and click-and-drag to select a few data points from the plot. Selected data will automatically propagate to Data Table. Double click it to check which data was selected. Change selection and observe the change in the Data Table. This works best if both widgets are open.
	[Download](https://orangedatamining.com/examples/scatterplot-data-table/120-scatterplot-data-table.ows)
	![](https://orangedatamining.com/examples/scatterplot-data-table/scatterplot-data-table.png)
- Scatter Plot, Visualization
	## Visalization of Data Subsets
	Some visualization widget, like Scatter Plot and several data projection widgets, can expose the data instances in the data subset. In this workflow, Scatter Plot visualizes the data from the input data file, but also marks the data points that have been selected in the Data Table (selected rows).
	[Download](https://orangedatamining.com/examples/data-subsets/130-scatterplot-visualize-subset.ows)
	![](https://orangedatamining.com/examples/data-subsets/scatterplot-visualize-subset.png)
- Data, Pivot Table
	## Pivot Table
	Pivot Table can help us aggregate and transform the data. This workflow takes Kickstarter projects and aggregates them by month. We can inspect the frequency of the published projects per month and observe the difference between funded and non-funded projects. Try constructing several tables with pivot and experiment with different aggregation methods.
	[Download](https://orangedatamining.com/examples/pivot-table/140-pivot-table.ows)
	![](https://orangedatamining.com/examples/pivot-table/pivot-table.png)
- Classification Tree, Classification
	## Classification Tree
	This workflow combines the interface and visualization of classification trees with scatter plot. When both the tree viewer and the scatter plot are open, selection of any node of the tree sends the related data instances to scatter plot. In the workflow, the selected data is treated as a subset of the entire dataset and is highlighted in the scatter plot. With simple combination of widgets we have constructed an interactive classification tree browser.
	[Download](https://orangedatamining.com/examples/tree-scatterplot/250-tree-scatterplot.ows)
	![](https://orangedatamining.com/examples/tree-scatterplot/tree-scatterplot.png)

...