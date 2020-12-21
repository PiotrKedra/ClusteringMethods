import pandas as pd
import matplotlib.pyplot as plt
from math import dist
import numpy as np


def single_linkage(data, n_clusters=3):

    clusters = []
    for index, row in data.iterrows():
        clusters.append({'data_points': [row.values.tolist()], 'cluster_number': index})
     
    while len(clusters) > n_clusters:
        size = len(clusters)
        print(size)
        # iterate trough all pairs of clusters for example (100 cluster -> 99 cluster)
        # initialize min distance and clusters
        min_index1 = 0
        min_index2 = 1
        min_dist = distance(clusters[0]['data_points'], clusters[1]['data_points']) 

        for i in range(0, size):
            for j in range(i, size):

                tmp_dist = distance(clusters[i]['data_points'], clusters[j]['data_points'])
                if tmp_dist < min_dist:
                    min_dist = tmp_dist
                    min_index1 = i
                    min_index2 = j

        # merge min clusetrs
        cluster_to_merge = clusters.pop(min_index2)
        # remove the second cluster and merge it to first one
        clusters[min_index1]['data_points'].extend(cluster_to_merge['data_points'])

        """
        c1 = [(1,2),(3,2),(2,1)]
        c2 = [(9,1), (8,1)]
        c1.extend(c2)
    
        print(c1) ->  [(1,2),(3,2),(2,1), (9,1), (8,1)]
        """
        clusters[min_index1]['data_points'].extend(cluster_to_merge['data_points'])

    print(len(clusters))
    for cluster in clusters:
        print(cluster)

    # convert clusters to the just cluster number (ordered)
    y = []
    for index, row in data.iterrows():
        for cluster in clusters:
            if row.values.tolist() in cluster['data_points']:
                y.append(cluster['cluster_number'])
                break
    return y

# do the matrix of distances
def distance(cluster1, cluster2):
    size1 = len(cluster1)
    size2 = len(cluster2)
    min_dist = dist(cluster1[0], cluster2[0])
    for i in range(0, size1):
        for j in range(0, size2):
            point1 = cluster1[i]
            point2 = cluster2[j]
            tmp_dist = dist(point1, point2)
            # print('p1: ' + str(point1) + ' p2: ' + str(point2) + ' D: ' + str(distance))
            if tmp_dist < min_dist:
                min_dist = tmp_dist
    
    return min_dist


data = pd.read_csv('../meanshift/testing.csv')
y_c = single_linkage(data)

plt.scatter(data[['x']], data[['y']], c=y_c)
plt.show()
