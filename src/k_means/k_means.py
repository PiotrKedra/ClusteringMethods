import matplotlib.pyplot as plt
import pandas as pan
import numpy as np
from math import dist


def print_all():
    plt.scatter(x[:, 0], x[:, 1], c=x[:, 2])
    plt.scatter(clusters[:, 0], clusters[:, 1], c=clusters[:, 2], edgecolors='black', linewidth=2)
    plt.show()


def find_closest_cluster(x0, x1):
    closest_dist = dist((x0, x1), (clusters[0][0], clusters[0][1]))
    closest_cluster = 0
    for i in range(clusters.shape[0]):
        curr_dist = dist((x0, x1), (clusters[i][0], clusters[i][1]))
        # print("curr i: " + str(i) + " curr dist: " + str(curr_dist))
        if curr_dist < closest_dist:
            closest_cluster = i
            closest_dist = curr_dist
    return closest_cluster


def set_closest_clusters():
    for curr_x in x:
        closest_cluster = find_closest_cluster(curr_x[0], curr_x[1])
        curr_x[2] = closest_cluster


def recompute_centers():
    changed = False
    temp_clusters_sums = np.zeros((k, 3))
    for x_temp in x:
        temp_clusters_sums[int(x_temp[2])][0] += x_temp[0]
        temp_clusters_sums[int(x_temp[2])][1] += x_temp[1]
        temp_clusters_sums[int(x_temp[2])][2] += 1

    for i in range(k):
        if int(temp_clusters_sums[i][2]) != 0:
            new_cluster_i_0 = temp_clusters_sums[i][0]/temp_clusters_sums[i][2]
            new_cluster_i_1 = temp_clusters_sums[i][1]/temp_clusters_sums[i][2]

            if new_cluster_i_0 != clusters[i][0] or new_cluster_i_1 != clusters[i][1]:
                changed = True
                clusters[i][0] = new_cluster_i_0
                clusters[i][1] = new_cluster_i_1

    return changed


if __name__ == '__main__':
    # import data
    df = pan.read_csv('../../resources/2d_dataset/d31.csv')

    np.set_printoptions(precision=3, suppress=True)

    # normalize
    data = df.to_numpy()
    n = data.shape[0]
    x_without_clusters = data[:, :-1]
    initial_clusters = np.ones((n, 1)) * (-1)
    x = np.concatenate((x_without_clusters, initial_clusters), axis=1)
    # print(x)

    # number of clusters
    k = 31

    # init clusters center
    # print("x.shape")
    # print(x.shape)
    x0_max = max(x[:, 0])
    x0_min = min(x[:, 0])
    x1_max = max(x[:, 1])
    x1_min = min(x[:, 1])
    clusters_rand_x0 = np.random.uniform(low=x0_min, high=x0_max, size=(k, 1))
    # print("clusters_rand_x0.shape")
    # print(clusters_rand_x0.shape)
    clusters_rand_x1 = np.random.uniform(low=x1_min, high=x1_max, size=(k, 1))
    # print("clusters_rand_x1.shape")
    # print(clusters_rand_x1.shape)
    one_to_k = np.reshape(np.arange(k), (k, 1))
    clusters_without_numbers = np.concatenate((clusters_rand_x0, clusters_rand_x1), axis=1)
    clusters = np.concatenate((clusters_without_numbers, one_to_k), axis=1)
    # print("clusters.shape")
    # print(clusters)

    change = True
    while change:
        set_closest_clusters()
        change = recompute_centers()
        print_all()

    print("Final result:")
    print_all()
