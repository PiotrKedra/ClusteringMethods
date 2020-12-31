import pandas as pd
from matplotlib import pyplot
import matplotlib.pyplot as plt
from sklearn.cluster import AgglomerativeClustering
from hierarchical_linkage import hierarchical_linkage

data = pd.read_csv('../../resources/2d_dataset/r15.csv')

fig, axs = plt.subplots(2, 2)
hc = AgglomerativeClustering(n_clusters=15, affinity='euclidean', linkage='single')
y_hc = hc.fit_predict(data)
axs[0, 0].scatter(data[['x']], data[['y']], c=y_hc)
axs[0, 0].set_title('Single sklearn')

y_hc = hierarchical_linkage(data, n_clusters=15, linkage='single')
axs[0, 1].scatter(data[['x']], data[['y']], c=y_hc)
axs[0, 1].set_title('Single our implementation')

hc = AgglomerativeClustering(n_clusters=15, affinity='euclidean', linkage='complete')
y_hc = hc.fit_predict(data)
axs[1, 0].scatter(data[['x']], data[['y']], c=y_hc)
axs[1, 0].set_title('Complete sklearn')

y_hc = hierarchical_linkage(data, n_clusters=15, linkage='complete')
axs[1, 1].scatter(data[['x']], data[['y']], c=y_hc)
axs[1, 1].set_title('Complete our implementation')

pyplot.show()

