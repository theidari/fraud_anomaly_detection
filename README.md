<p align="center"><img src="https://github.com/theidari/fraud_anomaly_detection/blob/main/assets/fad_header.png" width="300px"></p>
<h3>1.Project Overview</h3>
<h3>2.Methods</h3>
<p align="justify">I would classify the mathematical approaches to this problem into two categories: Easily explainable <b>statistical methods</b>, somewhat explainable unsupervised machine learning methods.</p>
<h4>1.2.Statistical Methods</h4>
<h5>1.1.2.Interquartile range (IQR)</h5>
<p align="justify">&emsp;&emsp;The interquartile range (IQR) is a measure of variability used in statistical analysis. It is a measure of the spread of a dataset and is defined as the difference between the upper and lower quartiles of the dataset.
To calculate the IQR, the dataset is first sorted in ascending order. The median is then calculated, and the dataset is split into two halves - the lower half and the upper half. The lower quartile (Q1) is the median of the lower half, and the upper quartile (Q3) is the median of the upper half. The IQR is then calculated as the difference between Q3 and Q1. The IQR method is often used to identify outliers in a dataset. Any value that falls below Q1 - 1.5IQR or above Q3 + 1.5IQR is considered an outlier and may be removed from the dataset.</p>
<h4>2.2.Unsupervised Machine Learning Methods</h4>
