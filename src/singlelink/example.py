import pandas as pd
from matplotlib import pyplot
import matplotlib.pyplot as plt
from sklearn.cluster import AgglomerativeClustering
from math import dist

def singlelink(data, n_clusters=3):

    clusters = []

    for index, row in data.iterrows():
        clusters.append({'data_points': [row.values.tolist()], 'cluster_number': index})
     
    size = len(clusters)
    
    while len(clusters) > n_clusters:
    
    # iterate trought all pairs of clasters for example (100 cluster -> 99 cluster)
    # inizialaize min distanc and clusters
        min_index1 = 0
        min_index2 = 1
        min_dist = distance(clusters[0]['data_points'], clusters[1]['data_points']) 
    # todo while len(clusters) > n_clusters

    for i in range(0, size): 
        for j in range(i, size):
        
            tmp_dist = distance(clusters[i]['data_points'], clusters[j]['data_points'])
            if tmp_dist < min_dist:
                min_dist = tmp_dist
                min_index1 = i
                min_index2 = j

    # merge min clusetrs
    cluster_to_merge = clusters.pop(min_index2)
    clusters[min_index1]['data_points'].extend(cluster_to_merge['data_points'])

    # remove the second cluster and merge it to first one
    cluster_to_merge = clusters.pop(min_index2) # len(clusters) - 1
    """
    c1 = [(1,2),(3,2),(2,1)]
    c2 = [(9,1), (8,1)]
    c1.extend(c2)

    print(c1) ->  [(1,2),(3,2),(2,1), (9,1), (8,1)]
    """
    clusters[min_index1]['data_points'].extend(cluster_to_merge['data_points'])

    for cluster in clusters:
        print(cluster)

    # convert clusters to the jsut cluster number (odreder)
    # COPY PASTE FROM WARD'S
    # copay past from sklearn to show             

def distance(cluster1, cluster2):

    size1 = len(cluster1)
    size2 = len(cluster2)

    min_dist = dist(cluster1[0], cluster2[0])
    for i in range(0, size1):
        for j in range(0, size2):
            point1 = cluster1[i]
            point2 = cluster2[j]
            distance = dist(point1, point2)
            #print('p1: ' + str(point1) + ' p2: ' + str(point2) + ' D: ' + str(distance))

            if distance < min_dist:
                min_dist = distance
    
    return distance

data = pd.read_csv('../meanshift/testing.csv')
singlelink(data)