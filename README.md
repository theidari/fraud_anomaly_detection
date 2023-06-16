<img src="https://img.shields.io/badge/ -yellow.svg?style=for-the-badge" width="1500px" height="1px">
<a href="https://public.tableau.com/app/profile/ali.t.heidari/viz/FraudAnomalyDetection/FADDashboard"><img src="https://img.shields.io/badge/tableau dashboard-yellow.svg?style=for-the-badge&logo=tableau&logoColor=darkblue"></a>
<p align="center"><img src="https://github.com/theidari/fraud_anomaly_detection/blob/main/assets/fad_header.png" width="300px"></p>
<h3>1.Project Overview</h3>
<p align="justify">Fraud anomaly detection refers to the process of identifying unusual or suspicious patterns, behaviors, or activities that deviate from normal or expected behavior within a system, with the goal of detecting fraudulent or malicious activities. It is a vital technique used in various industries, such as finance, insurance, e-commerce, and cybersecurity, to identify and mitigate potential fraud risks.</p>
<h4 align="center"><ins>Goal</ins></h4>
<p align="center"><img src="https://img.shields.io/badge/Detect and flag irregular bank transactions for fraud or money laundering-yellow.svg?style=for-the-badge"></p>
<img src="https://img.shields.io/badge/ -yellow.svg?style=for-the-badge" width="1500px" height="1px">
<h3>2.Methods</h3>
<p align="justify">I would classify the mathematical approaches to this problem into two categories: Easily explainable <b>statistical methods</b>, somewhat explainable unsupervised machine learning methods.</p>
<h4>1.2. Statistical Methods</h4>
<h5>1.1.2. Interquartile range (IQR)</h5>
<p align="justify">&emsp;&emsp;The interquartile range (IQR) is a measure of variability used in statistical analysis. It is a measure of the spread of a dataset and is defined as the difference between the upper and lower quartiles of the dataset.
To calculate the IQR, the dataset is first sorted in ascending order. The median is then calculated, and the dataset is split into two halves - the lower half and the upper half. The lower quartile (Q1) is the median of the lower half, and the upper quartile (Q3) is the median of the upper half. The IQR is then calculated as the difference between Q3 and Q1. The IQR method is often used to identify outliers in a dataset. Any value that falls below Q1 - 1.5IQR or above Q3 + 1.5IQR is considered an outlier and may be removed from the dataset.</p>
<h5>2.1.2. Standard deviation analysis</h5>


<h4>2.2.Unsupervised Machine Learning Methods</h4>
<h5>1.2.2. Evaluating the optimal number of clusters</h5>
<p align="justify">&emsp;&emsp;Evaluating the optimal number of clusters in a clustering algorithm is an important task to determine the appropriate level of granularity in the data. The determination of the best number of clusters (k) depends on the specific problem and the data being analyzed. However, we can use the information provided by two common methods to make a recommendation. Firstly, the <b><ins>elbow method</ins></b> suggests that the optimal number of clusters is reached where the change in Within-Cluster Sum of Squares (WCSS) begins to level off. Secondly, the <b><ins>silhouette method</ins></b> measures how well each data point fits into its assigned cluster and produces a range of values from -1 to 1, where values closer to 1 indicate a better fit.</p>
<h5>2.2.2. K-Means</h5>
<p align="justify">&emsp;&emsp;K-means is an unsupervised machine learning algorithm used for clustering data. It aims to partition n observations into k clusters, where each observation belongs to the cluster with the nearest mean. The algorithm works by iteratively updating the cluster centroids and assigning data points to their closest centroid until convergence. K-means is widely used in various fields, including image segmentation, customer segmentation, and anomaly detection.</p>
<h3>3.Dataset</h3>
<p align="justify">The <a href="https://data.world/lpetrocelli/czech-financial-dataset-real-anonymized-transactions">dataset</a> being examined consists of real anonymized transactions from a Czech bank, spanning the period between 1993 and 1999. These transactions do not have explicit labels indicating fraud or money laundering. While the majority of the transactions are considered legitimate, given the nature of the bank's operations, there is a possibility that a small portion of them may involve illicit activities. It is important to note that, for this project, the month of October 1997 was randomly chosen using below code as the sample month.</p>

```python
import random
# Create a list representing the months from 1 to 84
months = list(range(1, 85))
# Randomly sample one month
random_month = random.choice(months)
print("Randomly sampled month:", random_month)
```
<h4>1.3.Feature Profiling</h4>
<a href="https://theidari.github.io/fraud_anomaly_detection/results/df_trans_profile">Data Profile</a>
<h6 align="center">Fig 1-Original and Synthetic Features</h6>
<p align="center">
<img src="https://github.com/theidari/fraud_anomaly_detection/blob/main/assets/features_fig.png" width="700px">
</p>
<h3>4.Results</h3>
<h6 align="center">Fig 2-Tableau Dashboard View 1</h6>
<p align="center">
<img src="https://github.com/theidari/fraud_anomaly_detection/blob/main/assets/dash_fig_1.png" width="700px">
</p>
<h6 align="center">Fig 3-Tableau Dashboard View 2</h6>
<p align="center">
<img src="https://github.com/theidari/fraud_anomaly_detection/blob/main/assets/dash_fig_2.png" width="300px">
</p>
<h3>5.Conclusions</h3>
<ul>
<li>Utilizing K-means clustering and validation metrics such as WCSS elbow and silhouette score, we can effectively detect anomalies and outliers in transaction data.</li>
<li>This method offers a data-driven approach to enhance decision-making, fraud detection, and risk management in various industries.</li>
<li>Fraud can be identified more easily in accounts with higher number of transactions.</li>
</ul>
<h3>6.Future Improvement and Discussion</h3>
<ul>
<li>Develop a systematic approach to integrate results from standard deviation analysis, box plot method, and K-means clustering.</li>
<li>Compare against known outliers or expert-labeled data for effectiveness evaluation.</li>
<li>Assign weights or confidence levels to each method based on their effectiveness and reliability.</li>
<li>Analyze performance metrics (precision, recall, F1 score) to assess accuracy and reliability.</li>
<li>Thoroughly validate and refine the combined results.</li>
</ul>

<h3>References</h3>



