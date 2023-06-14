# --------------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------ All libraries, variables and functions are defined in this file ---------------------------------------
# --------------------------------------------------------------------------------------------------------------------------------------------

# main dependencies and setup
import os
import numpy as np
import pandas as pd
from pandas_profiling import ProfileReport # data statistic profiling
from pathlib import Path
import datetime as datetime
import statsmodels.api as sm

# ml dependencies and setup
from sklearn.pipeline import Pipeline # pipeline
from sklearn.cluster import KMeans # KMeans
from sklearn.decomposition import PCA # PCA
from sklearn.preprocessing import StandardScaler, MinMaxScaler # StandardScale to resize the distribution of values 
from sklearn.metrics import balanced_accuracy_score, confusion_matrix, classification_report, roc_curve, auc, r2_score, mean_squared_error, accuracy_score
from sklearn import svm
from sklearn.datasets import make_classification
from sklearn.svm import SVC
from sklearn.base import BaseEstimator, TransformerMixin # estimators and transformers 

# plotting dependencies and setup  
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.io as pio
import matplotlib.pyplot as plt

# package dependencies and setup
from fadpackage.constants import * # constants

# --------------------------------------------------------------------------------------------------------------------------------------------
# functions
# investigation functions ____________________________________________________________________________________________________________________