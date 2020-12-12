import pandas as pd
from matplotlib import pyplot
import matplotlib.pyplot as plt
from sklearn.cluster import AgglomerativeClustering


plt.figure(1)
data = pd.read_csv('../../resources/2d_dataset/r15.csv')
hc = AgglomerativeClustering(n_clusters=15, affinity='euclidean', linkage='ward')
y_hc = hc.fit_predict(data)
plt.scatter(data[['x']], data[['y']], c=y_hc)

plt.figure(2)
data = pd.read_csv('../../resources/2d_dataset/aggregation.csv')
hc = AgglomerativeClustering(n_clusters=6, affinity='euclidean', linkage='ward')
y_hc = hc.fit_predict(data)
plt.scatter(data[['x']], data[['y']], c=y_hc)

plt.figure(3)
data = pd.read_csv('../../resources/2d_dataset/jain.csv')
hc = AgglomerativeClustering(n_clusters=2, affinity='euclidean', linkage='ward')
y_hc = hc.fit_predict(data)
plt.scatter(data[['x']], data[['y']], c=y_hc)

pyplot.show()

