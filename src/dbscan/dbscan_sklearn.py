import pandas as pd
from matplotlib import pyplot
import matplotlib.pyplot as plt
from sklearn.cluster import DBSCAN

# LOAD DATA
df = pd.read_csv('../../resources/2d_dataset/compound.csv')
data = df.to_numpy()

print(data)

# PREPARE MODEL

dbscan = DBSCAN(eps=1, min_samples=3)
dbscan.fit(data)
y_dbscan = dbscan.fit_predict(data)

# SHOW CLUSTERS
plt.scatter(data[:, 0], data[:, 1], c=y_dbscan)
pyplot.show()