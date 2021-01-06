import matplotlib.pyplot as plt
import pandas as pan
import numpy as np
from math import dist


def print_all(x, clusters):
    plt.scatter(x[:, 0], x[:, 1], c=x[:, 2])
    plt.scatter(clusters[:, 0], clusters[:, 1], c=clusters[:, 2], edgecolors='black', linewidth=2)
    plt.show()


def initialize_clusters(x, k):
    numb_of_features = x.shape[1] - 1

    clusters_rand = [0] * numb_of_features
    xi_max = max(x[:, 0])
    xi_min = min(x[:, 0])
    clusters_rand[0] = np.random.uniform(low=xi_min, high=xi_max, size=(k, 1))

    clusters_without_numbers = clusters_rand[0]
    for i in range(1, numb_of_features):
        xi_max = max(x[:, i])
        xi_min = min(x[:, i])
        clusters_rand[i] = np.random.uniform(low=xi_min, high=xi_max, size=(k, 1))
        clusters_without_numbers = np.concatenate((clusters_without_numbers, clusters_rand[i]), axis=1)

    one_to_k = np.reshape(np.arange(k), (k, 1))

    return np.concatenate((clusters_without_numbers, one_to_k), axis=1)


def find_closest_cluster(x_row, clusters):
    numb_of_features = len(x_row) - 1
    closest_cluster = 0
    for i in range(numb_of_features):
        closest_dist = dist(x_row[:-1], clusters[i][:-1])
        for j in range(clusters.shape[0]):
            curr_dist = dist(x_row[:-1], clusters[j][:-1])
            # print("curr i: " + str(i) + " curr dist: " + str(curr_dist))
            if curr_dist < closest_dist:
                closest_cluster = j
                closest_dist = curr_dist
    return closest_cluster


def set_closest_clusters(x, clusters):
    for curr_x in x:
        closest_cluster = find_closest_cluster(curr_x, clusters)
        curr_x[-1] = closest_cluster


def recompute_centers(x, clusters, k):
    changed = False
    temp_clusters_sums = np.zeros((k, x.shape[1]))
    numb_of_features = x.shape[1] - 1
    for x_temp in x:
        for i in range(numb_of_features):
            temp_clusters_sums[int(x_temp[-1])][i] += x_temp[i]

        temp_clusters_sums[int(x_temp[-1])][-1] += 1

    new_cluster = np.zeros((k, numb_of_features))
    for i in range(k):
        if int(temp_clusters_sums[i][-1]) != 0:
            for j in range(numb_of_features):
                new_cluster[i][j] = temp_clusters_sums[i][j] / temp_clusters_sums[i][-1]

            if any_cluster_to_change(new_cluster[i], clusters[i], numb_of_features):
                changed = True
                for j in range(numb_of_features):
                    clusters[i][j] = new_cluster[i][j]

    return changed


def any_cluster_to_change(new_cluster_i, clusters_i, numb_of_features):
    for j in range(numb_of_features):
        if new_cluster_i[j] != clusters_i[j]:
            return True

    return False


def k_means(k, filename, print_plot=False):
    # import data
    df = pan.read_csv(filename)

    np.set_printoptions(precision=3, suppress=True)

    # normalize
    data = df.to_numpy()
    n = data.shape[0]
    x_without_clusters = data[:, :-1]
    initial_clusters = np.ones((n, 1)) * (-1)
    x = np.concatenate((x_without_clusters, initial_clusters), axis=1)

    clusters = initialize_clusters(x, k)
    # print("clusters.shape")
    # print(clusters)

    change = True
    while change:
        set_closest_clusters(x, clusters)
        change = recompute_centers(x, clusters, k)
        # print_all()
    if print_plot:
        print_all(x, clusters)

    return x
