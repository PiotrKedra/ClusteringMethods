import pandas as pd
import matplotlib.pyplot as plt
from math import dist


def hierarchical_linkage(data, linkage='complete', n_clusters=3):

    if linkage == 'complete':
        distance = distance_for_complete_linkage
    elif linkage == 'single':
        distance = distance_for_single_linkage
    else:
        raise Exception('Allowed linkage methods: \'complete\' or \'single\'')

    clusters = []
    for index, row in data.iterrows():
        clusters.append({'data_points': [index], 'cluster_number': index})

    distance_matrix = get_distance_matrix(data)

    while len(clusters) > n_clusters:

        # iterate trough all pairs of clusters for example (100 cluster -> 99 cluster)
        # initialize min distance and clusters
        min_index1 = 0
        min_index2 = 1
        min_dist = distance(clusters[0]['data_points'], clusters[1]['data_points'], distance_matrix)

        size = len(clusters)
        print(size)
        for i in range(0, size - 1):
            for j in range(i + 1, size):
                tmp_dist = distance(clusters[i]['data_points'], clusters[j]['data_points'], distance_matrix)
                if tmp_dist < min_dist:
                    min_dist = tmp_dist
                    min_index1 = i
                    min_index2 = j

        # merge min clusters
        # remove the second cluster and merge it to first one
        cluster_to_merge = clusters.pop(min_index2)
        clusters[min_index1]['data_points'].extend(cluster_to_merge['data_points'])

    # convert clusters to the just cluster number (ordered)
    y = []
    for index, row in data.iterrows():
        for cluster in clusters:
            if index in cluster['data_points']:
                y.append(cluster['cluster_number'])
                break
    return y


def distance_for_single_linkage(cluster1, cluster2, distance_matrix):
    min_dist = distance_matrix[cluster1[0]][cluster2[0]]
    for index_1 in cluster1:
        for index_2 in cluster2:
            if distance_matrix[index_1][index_2] < min_dist:
                min_dist = distance_matrix[index_1][index_2]
    return min_dist


def distance_for_complete_linkage(cluster1, cluster2, distance_matrix):
    max_dist = distance_matrix[cluster1[0]][cluster2[0]]
    for index_1 in cluster1:
        for index_2 in cluster2:
            if distance_matrix[index_1][index_2] > max_dist:
                max_dist = distance_matrix[index_1][index_2]
    return max_dist


def get_distance_matrix(data):
    distance_matrix = []
    for i1, row1 in data.iterrows():
        distance_matrix.append([])
        for i2, row2 in data.iterrows():
            distance_matrix[i1].append(dist(row1.values.tolist(), row2.values.tolist()))
    return distance_matrix


df = pd.read_csv('../../resources/2d_dataset/jain.csv')
y_c = hierarchical_linkage(df, linkage='complete', n_clusters=2)
plt.scatter(df[['x']], df[['y']], c=y_c)
plt.show()
