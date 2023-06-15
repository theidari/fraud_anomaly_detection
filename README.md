<p align="center"><img src="https://github.com/theidari/fraud_anomaly_detection/blob/main/assets/fad_header.png" width="300px"></p>
<h3>1.Project Overview</h3>
<p align="justify">Fraud anomaly detection refers to the process of identifying unusual or suspicious patterns, behaviors, or activities that deviate from normal or expected behavior within a system, with the goal of detecting fraudulent or malicious activities. It is a vital technique used in various industries, such as finance, insurance, e-commerce, and cybersecurity, to identify and mitigate potential fraud risks.</p>
<h3>2.Methods</h3>
<p align="justify">I would classify the mathematical approaches to this problem into two categories: Easily explainable <b>statistical methods</b>, somewhat explainable unsupervised machine learning methods.</p>
<h4>1.2.Statistical Methods</h4>
<h5>1.1.2.Interquartile range (IQR)</h5>
<p align="justify">&emsp;&emsp;The interquartile range (IQR) is a measure of variability used in statistical analysis. It is a measure of the spread of a dataset and is defined as the difference between the upper and lower quartiles of the dataset.
To calculate the IQR, the dataset is first sorted in ascending order. The median is then calculated, and the dataset is split into two halves - the lower half and the upper half. The lower quartile (Q1) is the median of the lower half, and the upper quartile (Q3) is the median of the upper half. The IQR is then calculated as the difference between Q3 and Q1. The IQR method is often used to identify outliers in a dataset. Any value that falls below Q1 - 1.5IQR or above Q3 + 1.5IQR is considered an outlier and may be removed from the dataset.</p>
<h4>2.2.Unsupervised Machine Learning Methods</h4>
<h5>1.2.2. Evaluating the optimal number of clusters</h5>
<p align="justify">&emsp;&emsp;Evaluating the optimal number of clusters in a clustering algorithm is an important task to determine the appropriate level of granularity in the data. The determination of the best number of clusters (k) depends on the specific problem and the data being analyzed. However, we can use the information provided by two common methods to make a recommendation. Firstly, the <b><ins>elbow method</ins></b> suggests that the optimal number of clusters is reached where the change in Within-Cluster Sum of Squares (WCSS) begins to level off. Secondly, the <b><ins>silhouette method</ins></b> measures how well each data point fits into its assigned cluster and produces a range of values from -1 to 1, where values closer to 1 indicate a better fit.</p>
<h5>2.2.2. K-Means</h5>
<p align="justify">&emsp;&emsp;K-means is an unsupervised machine learning algorithm used for clustering data. It aims to partition n observations into k clusters, where each observation belongs to the cluster with the nearest mean. The algorithm works by iteratively updating the cluster centroids and assigning data points to their closest centroid until convergence. K-means is widely used in various fields, including image segmentation, customer segmentation, and anomaly detection.</p>
<h3>3.Dataset</h3>

