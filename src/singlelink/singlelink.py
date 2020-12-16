import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import AgglomerativeClustering
from sklearn.preprocessing import normalize
import scipy.cluster.hierarchy as shc

#Load Data
data = pd.read_csv("../../resources/2d_dataset/compound.csv", sep = ",")
data

#Normalize the Data
data_scaled = normalize(data)
data_scaled = pd.DataFrame(data_scaled, columns=data.columns)
data_scaled

#Show dendogram
plt.figure(figsize=(10, 7))  
plt.title("Dendrograms")  
dend = shc.dendrogram(shc.linkage(data_scaled, method='ward'))
plt.axhline(y=6, color='r', linestyle='--')

cluster = AgglomerativeClustering(n_clusters=2, affinity='euclidean', linkage='ward')  
cluster.fit_predict(data_scaled)

#SHow clusters
plt.figure(figsize=(10, 7))  
plt.scatter(data_scaled['x'], data_scaled['y'], c=cluster.labels_)
plt.show()