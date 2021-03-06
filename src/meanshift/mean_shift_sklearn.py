import pandas as pd
from matplotlib import pyplot
import matplotlib.pyplot as plt
from sklearn.cluster import MeanShift

# LOAD DATA
plt.figure(1)
data = pd.read_csv('../../resources/2d_dataset/r15.csv')

# PREPARE MODEL
kmeans = MeanShift(bandwidth=1)
kmeans.fit(data)
y_kmeans = kmeans.predict(data)

# SHOW CLUSTERS
plt.scatter(data[['x']], data[['y']], c=y_kmeans)


plt.figure(2)
data = pd.read_csv('../../resources/2d_dataset/pathbased.csv')
kmeans = MeanShift(bandwidth=6)
kmeans.fit(data)
y_kmeans = kmeans.predict(data)
plt.scatter(data[['x']], data[['y']], c=y_kmeans)

pyplot.show()

