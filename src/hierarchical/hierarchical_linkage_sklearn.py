import pandas as pd
from matplotlib import pyplot
import matplotlib.pyplot as plt
from sklearn.cluster import AgglomerativeClustering

# data = pd.read_csv("/Users/baur/desktop/study/ai/ClusteringMethods/resources/2d_dataset/compound.csv", sep = ",")


plt.figure(1)
data = pd.read_csv('../../resources/2d_dataset/jain.csv')
hc = AgglomerativeClustering(n_clusters=2, affinity='euclidean', linkage='complete')
y_hc = hc.fit_predict(data)
plt.scatter(data[['x']], data[['y']], c=y_hc)

pyplot.show()
