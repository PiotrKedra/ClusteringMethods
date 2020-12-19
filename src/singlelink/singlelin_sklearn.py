import pandas as pd
from matplotlib import pyplot
import matplotlib.pyplot as plt
from sklearn.cluster import AgglomerativeClustering


plt.figure(1)
data = pd.read_csv('../meanshift/testing.csv')
hc = AgglomerativeClustering(n_clusters=3, affinity='euclidean', linkage='complete')
y_hc = hc.fit_predict(data)
plt.scatter(data[['x']], data[['y']], c=y_hc)

pyplot.show()

