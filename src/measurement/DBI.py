import numpy as np
from math import dist


def how_many_clusters(y):
    return len(set(y))


def calculate_centroids(x, n):
    cluster_numbers = np.array(list(set(x[:, -1])))
    cluster_numbers = cluster_numbers[:, np.newaxis]
    centroids = np.concatenate((np.zeros((len(set(x[:, -1])), x.shape[1] - 1)), cluster_numbers), axis=1)

    for i in range(n):
        sum = np.zeros(x.shape[1] - 1)
        denominator = 0
        for curr_x in x:
            if curr_x[-1] == centroids[i][-1]:
                sum[0] += curr_x[0]
                sum[1] += curr_x[1]
                denominator += 1
        centroids[i][0] = sum[0] / denominator
        centroids[i][1] = sum[1] / denominator

    return centroids


def compute_avg_distance_to_centroids(x, centroids, n):
    centroids_with_avg_dist = np.hstack((centroids, np.zeros((n, 1))))

    for i in range(n):
        sum = 0
        denominator = 0
        for curr_x in x:
            if curr_x[-1] == centroids[i][-1]:
                sum += dist(curr_x[:-1], centroids[i][:-1])
                denominator += 1
        centroids_with_avg_dist[i][len(centroids_with_avg_dist[0]) - 1] = sum / denominator

    return centroids_with_avg_dist


def find_max_sum_of_avg_dist_by_dist_between_centroids(centroids, n):
    centroids_with_dist_from_other_centroids = np.hstack((centroids, np.zeros((n, 1))))
    for i in range(n):
        curr_max = 0
        avg_dist1 = centroids_with_dist_from_other_centroids[i][len(centroids_with_dist_from_other_centroids[0]) - 2]
        for j in range(n):
            if i != j:
                avg_dist2 = centroids_with_dist_from_other_centroids[j][len(centroids_with_dist_from_other_centroids[0]) - 2]
                dist_centroids = dist(centroids_with_dist_from_other_centroids[i][:-2], centroids_with_dist_from_other_centroids[j][:-2])

                val = (avg_dist1 + avg_dist2) / dist_centroids

                if val > curr_max:
                    curr_max = val

        centroids_with_dist_from_other_centroids[i][-1] = curr_max

    return centroids_with_dist_from_other_centroids


def computeDBI(x):
    number_of_clusters = how_many_clusters(x[:, -1])
    centroids = calculate_centroids(x, number_of_clusters)

    centroids_with_dist = compute_avg_distance_to_centroids(x, centroids, number_of_clusters)
    centroids_with_dist_and_max = find_max_sum_of_avg_dist_by_dist_between_centroids(centroids_with_dist, number_of_clusters)

    index = np.mean(centroids_with_dist_and_max[:, len(centroids_with_dist_and_max[0]) - 1])

    return index
