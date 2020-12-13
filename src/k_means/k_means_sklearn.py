import pandas as pd
from matplotlib import pyplot
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# LOAD DATA
df = pd.read_csv('../../resources/2d_dataset/r15.csv')
data = df.to_numpy()

print(data)

# PREPARE MODEL

kmeans = KMeans(n_clusters=15)
kmeans.fit(data)
y_kmeans = kmeans.predict(data)

# SHOW CLUSTERS
plt.scatter(data[:, 0], data[:, 1], c=y_kmeans)
pyplot.show()