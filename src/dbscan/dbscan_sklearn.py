def warn(*args, **kwargs):
    pass


import warnings

warnings.warn = warn
import pandas as pd
from matplotlib import pyplot
import matplotlib.pyplot as plt
from sklearn.cluster import DBSCAN
import numpy as np


def dbscan(df, my_eps, my_min_samples):
    # LOAD DATA
    # df = pd.read_csv('../../resources/2d_dataset/compound.csv')
    data = df.to_numpy()

    # PREPARE MODEL

    dbscan = DBSCAN(eps=my_eps, min_samples=my_min_samples)
    dbscan.fit(data)
    y_dbscan = dbscan.fit_predict(data)

    # SHOW CLUSTERS
    # plt.scatter(data[:, 0], data[:, 1], c=y_dbscan)
    # pyplot.show()

    data = np.concatenate((data[:, :-1], y_dbscan.reshape((y_dbscan.shape[0], 1))), axis=1)

    return data
