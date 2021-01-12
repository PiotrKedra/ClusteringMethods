import pandas as pd
from matplotlib import pyplot
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import numpy as np


def k_means(df, clusters):
    # LOAD DATA
    # df = pd.read_csv('../../resources/2d_dataset/r15.csv')
    data = df.to_numpy()

    # print(data)

    # PREPARE MODEL

    kmeans = KMeans(n_clusters=clusters)
    kmeans.fit(data)
    y_kmeans = kmeans.predict(data)

    data = np.concatenate((data[:, :-1], y_kmeans.reshape((y_kmeans.shape[0], 1))), axis=1)

    # print(data)
    # SHOW CLUSTERS
    plt.scatter(data[:, 0], data[:, 1], c=y_kmeans)
    pyplot.show()

    return data
