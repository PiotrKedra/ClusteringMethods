import pandas as pd
from matplotlib import pyplot
import matplotlib.pyplot as plt
from sklearn.cluster import MeanShift

# LOAD DATA
data_file = pd.read_csv('../../resources/2d_dataset/aggregation.csv')
data_file.columns = ["c1", "c2", "group"]
data = data_file.iloc[:, 0:2].copy()
# data_file.plot(kind='scatter', x='c1', y='c2')

# PREPARE MODEL
kmeans = MeanShift(bandwidth=5)
kmeans.fit(data)
y_kmeans = kmeans.predict(data)

# SHOW CLUSTERS
plt.scatter(data[['c1']], data[['c2']], c=y_kmeans)
pyplot.show()

