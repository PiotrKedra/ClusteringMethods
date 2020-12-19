# 1. Select a data point (not visited yet).
# 2. If number of neighbours is sufficient - becomes a new cluster, else - label as noise.
# 3. Points close to the selected points also included to the cluster.
# 4. Repeat step 3 until all possible points are added to the cluster.
# 5. Select new starting point from not visited
# and repeat all steps until all points are in clusters or don’t have enough neighbours.

import matplotlib.pyplot as plt
import pandas as pan
import numpy as np
from math import dist


def print_all():
    plt.scatter(x[:, 0], x[:, 1], c=x[:, 2])
    plt.show()


def find_not_visited():
    for i in range(n):
        if x[i][2] < 0:
            return i

    return -1


def find_not_visited_neighbours(x_curr_i, neighbours):
    added = False
    x_curr = x[x_curr_i][:-1]
    for i in range(n):
        distance = dist(x_curr, x[i][:-1])
        # print(distance)
        if x[i][2] < 0 and distance <= eps and i not in neighbours:
            neighbours.add(i)
            added = True
    return added


def how_many_neighbours(x_curr_i):
    count = 0
    x_curr = x[x_curr_i][:-1]
    for i in range(n):
        distance = dist(x_curr, x[i][:-1])
        # print(distance)
        if distance <= eps:
            count += 1

    return count


def add_neighbours_to_cluster(neighbours, cluster_no):
    while len(neighbours) > 0:
        neighbour_id = neighbours.pop()
        find_not_visited_neighbours(neighbour_id, neighbours)
        x[neighbour_id, 2] = cluster_no


# def mark_singles_as_noise():
#     number_of_clusters = np.max(x[:, 2].astype(np.int64))
#     singles = set()
#     for i in range(number_of_clusters):
#         number_of_points_in_cluster = np.count_nonzero(x[:, 2] == i + 1)
#         if number_of_points_in_cluster == 1:
#             singles.add(i + 1)
#
#     for curr_row in x:
#         if curr_row[2] in singles:
#             curr_row[2] = 0


if __name__ == '__main__':
    # import data
    df = pan.read_csv('../../resources/2d_dataset/compound.csv')
    np.set_printoptions(precision=3, suppress=True)

    # normalize
    data = df.to_numpy()
    n = data.shape[0]
    x_without_clusters = data[:, :-1]
    initial_clusters = np.ones((n, 1)) * (-1)
    x = np.concatenate((x_without_clusters, initial_clusters), axis=1)

    # given values
    eps = 1
    min_no_of_neighbours = 3

    last_cluster = 0
    all_visited = False
    while not all_visited:
        x_to_add = find_not_visited()
        if x_to_add < 0:
            all_visited = True
        else:
            no_of_n = how_many_neighbours(x_to_add)
            if no_of_n < min_no_of_neighbours:
                x[x_to_add, 2] = 0
            else:
                found = True
                to_add = set()
                last_cluster += 1
                while found:
                    found = find_not_visited_neighbours(x_to_add, to_add)
                    add_neighbours_to_cluster(to_add, last_cluster)

    for x_curr_pr in x:
        print(x_curr_pr)

    print_all()
