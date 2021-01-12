import pandas as pd
import matplotlib.pyplot as plt
from numpy import mean
from math import dist
import numpy as np


def ward(df, n_clusters=5):
    clusters = []
    for index, row in df.iterrows():
        clusters.append({'data_points': [row.values.tolist()], 'cluster_number': index})

    single_e_values = init_list_e_value_single(clusters)
    e_value_matrix = init_matrix_for_sum_of_squared_deviations_for_merged_cluster(clusters)

    while n_clusters != len(clusters):
        print(len(clusters))
        cluster_to_merge_1 = 0
        cluster_to_merge_2 = 1
        min_e_value = e_value_matrix[cluster_to_merge_1][cluster_to_merge_2]['e_value'] \
            + e_value_single_clusters(single_e_values, cluster_to_merge_1, cluster_to_merge_2)

        for i in range(len(e_value_matrix)-1):
            for j in range(i+1, len(e_value_matrix)):
                tmp_e_value = e_value_matrix[i][j]['e_value'] \
                    + e_value_single_clusters(single_e_values, e_value_matrix[i][j]['cluster_1_number'],
                                              e_value_matrix[i][j]['cluster_2_number'])
                if tmp_e_value <= min_e_value:
                    min_e_value = tmp_e_value
                    cluster_to_merge_1 = e_value_matrix[i][j]['cluster_1_number']
                    cluster_to_merge_2 = e_value_matrix[i][j]['cluster_2_number']

        merge_clusters(cluster_to_merge_1, cluster_to_merge_2, clusters)
        update_single_e_values(single_e_values, cluster_to_merge_1, cluster_to_merge_2, clusters)
        e_value_matrix = update_e_value_matrix(e_value_matrix, clusters, cluster_to_merge_1, cluster_to_merge_2)

    y = []
    for index, row in df.iterrows():
        for cluster in clusters:
            if row.values.tolist() in cluster['data_points']:
                y.append(cluster['cluster_number'])
                break
    return y


def init_list_e_value_single(clusters):
    single_sums_of_squared_deviations = []
    for cluster in clusters:
        single_sum_object = {
            'value': 0,
            'cluster_number': cluster['cluster_number']
        }
        single_sums_of_squared_deviations.append(single_sum_object)
    return {
        'total_sum': 0,
        'list_of_sums_of_squared_deviations': single_sums_of_squared_deviations
    }


def init_matrix_for_sum_of_squared_deviations_for_merged_cluster(clusters):
    matrix = []
    for i in range(len(clusters)):
        cluster1 = clusters[i]
        matrix.append([])
        for cluster2 in clusters:
            merged_cluster = cluster1['data_points'] + cluster2['data_points']
            centroid = get_centroid_of_cluster(merged_cluster)
            e_value_pair_part = dist(merged_cluster[0], centroid)
            e_value_pair_part += dist(merged_cluster[1], centroid)
            e_value_pair_part_object = {
                'e_value': e_value_pair_part,
                'cluster_1_number': cluster1['cluster_number'],
                'cluster_2_number': cluster2['cluster_number'],
            }
            matrix[i].append(e_value_pair_part_object)
    return matrix


def e_value_single_clusters(single_sums_of_squared_deviations, cluster_to_merge_1, cluster_to_merge_2):
    total_value = single_sums_of_squared_deviations['total_sum']
    exit_flag = 0
    for single_sum_object in single_sums_of_squared_deviations['list_of_sums_of_squared_deviations']:
        if single_sum_object['cluster_number'] == cluster_to_merge_1 \
                or single_sum_object['cluster_number'] == cluster_to_merge_2:
            total_value -= single_sum_object['value']
            if exit_flag == 1:
                break
            exit_flag += 1
    return total_value


def merge_clusters(cluster_to_merge_1, cluster_to_merge_2, clusters):
    extend_index = 0
    pop_index = 1
    for i, cluster in enumerate(clusters):
        if cluster['cluster_number'] == cluster_to_merge_1:
            extend_index = i
        elif cluster['cluster_number'] == cluster_to_merge_2:
            pop_index = i
            break
    cluster_to_merge = clusters.pop(pop_index)
    clusters[extend_index]['data_points'].extend(cluster_to_merge['data_points'])


def update_single_e_values(single_e_values, cluster_to_merge_1, cluster_to_merge_2, clusters):
    total_sum = single_e_values['total_sum']
    single_e_values_list = single_e_values['list_of_sums_of_squared_deviations']
    for i in range(len(single_e_values_list)):
        if single_e_values_list[i]['cluster_number'] == cluster_to_merge_1:
            cluster_data_points = clusters[i]['data_points']
            centroid = get_centroid_of_cluster(cluster_data_points)
            single_e_value = 0
            for data_point in cluster_data_points:
                single_e_value += dist(centroid, data_point)
            total_sum = total_sum - single_e_values_list[i]['value'] + single_e_value
            single_e_values_list[i]['value'] = single_e_value
        elif single_e_values_list[i]['cluster_number'] == cluster_to_merge_2:
            popped = single_e_values_list.pop(i)
            total_sum -= popped['value']
            break
    single_e_values['total_sum'] = total_sum


def update_e_value_matrix(e_value_matrix, clusters, cluster_to_merge_1, cluster_to_merge_2):
    index_to_update = 0
    for i in range(len(e_value_matrix)):
        if e_value_matrix[0][i]['cluster_2_number'] == cluster_to_merge_1:
            index_to_update = i
        if e_value_matrix[0][i]['cluster_2_number'] == cluster_to_merge_2:
            e_value_matrix = np.delete(e_value_matrix, i, 0)
            e_value_matrix = np.delete(e_value_matrix, i, 1)
            break
    for i in range(len(e_value_matrix)-1):
        for j in range(i+1, len(e_value_matrix)):
            if i == index_to_update or j == index_to_update:
                e_value = get_e_value(clusters[i]['data_points'], clusters[j]['data_points'])
                e_value_matrix[i][j]['e_value'] = e_value
    return e_value_matrix


def get_e_value(cluster1, cluster2):
    merged_cluster = cluster1 + cluster2
    centroid = get_centroid_of_cluster(merged_cluster)

    sum_of_squared_deviations = 0
    for datapoint in merged_cluster:
        sum_of_squared_deviations += dist(datapoint, centroid)

    return sum_of_squared_deviations


def get_centroid_of_cluster(merged_cluster):
    return mean(merged_cluster, axis=0)


# data = pd.read_csv('../../resources/2d_dataset/jain.csv')
# data.drop(['label'], axis=1, inplace=True)
# # data = pd.read_csv('../meanshift/testing.csv')
# y_c = ward(data, n_clusters=2)
# plt.scatter(data[['x']], data[['y']], c=y_c)
# plt.show()
