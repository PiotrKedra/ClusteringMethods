import pandas as pd
import matplotlib.pyplot as plt
from numpy import mean
from math import dist


def ward(df, n_clusters=5):
    clusters = []
    for index, row in df.iterrows():
        clusters.append({'data_points': [row.values.tolist()], 'cluster_number': index})

    while n_clusters != len(clusters):
        index_of_cluster_to_connect_1 = 0
        index_of_cluster_to_connect_2 = 1
        min_e_value = get_e_value(clusters[index_of_cluster_to_connect_1]['data_points'],
                                  clusters[index_of_cluster_to_connect_2]['data_points'])
        print(len(clusters))
        # one iteration (epoch?)
        for i, item1 in enumerate(clusters[0:-1]):
            for j_tmp, item2 in enumerate(clusters[i+1:]):
                e_value = get_e_value(item1['data_points'], item2['data_points'])
                if e_value < min_e_value:
                    min_e_value = e_value
                    index_of_cluster_to_connect_1 = i
                    j = j_tmp + i + 1
                    index_of_cluster_to_connect_2 = j

        # merge to closest clusters
        cluster_to_merge = clusters.pop(index_of_cluster_to_connect_2)
        clusters[index_of_cluster_to_connect_1]['data_points'].extend(cluster_to_merge['data_points'])

    print([o['cluster_number'] for o in clusters])

    y = []
    for index, row in df.iterrows():
        for cluster in clusters:
            if row.values.tolist() in cluster['data_points']:
                y.append(cluster['cluster_number'])
                break
    return y


def get_e_value(cluster1, cluster2):
    merged_cluster = cluster1+cluster2
    centroid = get_centroid_of_merged_clusters(merged_cluster)

    sum_of_squared_deviations = 0
    for datapoint in merged_cluster:
        sum_of_squared_deviations += dist(datapoint, centroid)

    return sum_of_squared_deviations


def get_centroid_of_merged_clusters(merged_cluster):
    return mean(merged_cluster, axis=0)


data = pd.read_csv('../../resources/2d_dataset/compound.csv')
data.drop(['label'], axis=1, inplace=True)
# data = pd.read_csv('../meanshift/testing.csv')

clusters = ward(data, n_clusters=3)

plt.scatter(data[['x']], data[['y']], c=clusters)
plt.show()
