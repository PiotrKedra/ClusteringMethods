import pandas as pd
from sklearn.cluster import estimate_bandwidth, MeanShift
from math import dist
from statistics import mean
from sklearn.metrics import silhouette_score


def silhouette_index(df, y):
    if len(df) != len(y):
        raise Exception("Data length should be same as result length.")

    distance_matrix = get_distance_matrix(df)
    scores_for_for_each_data_point = []
    for i in range(len(y)):
        current_cluster_number = y[i]
        score_for_i = {
            'a': [],
            'b': []
        }
        for j in range(len(y)):
            if i == j:
                continue

            if current_cluster_number == y[j]:
                score_for_i['a'].append(distance_matrix[i][j])
            else:
                cluster_exist = False
                for cluster in score_for_i['b']:
                    if cluster['number'] == y[j]:
                        cluster['distances'].append(distance_matrix[i][j])
                        cluster_exist = True
                        break
                if cluster_exist is False:
                    score_for_i['b'].append({
                        'number': y[j],
                        'distances': [distance_matrix[i][j]]
                    })

        if len(score_for_i['a']) == 0:
            continue
        a_i = mean(score_for_i['a'])
        b_i = mean(score_for_i['b'][0]['distances'])
        for k in range(1, len(score_for_i['b'])):
            tmp_b_i = mean(score_for_i['b'][k]['distances'])
            if tmp_b_i < b_i:
                b_i = tmp_b_i

        score = (b_i-a_i)/max(a_i, b_i)
        scores_for_for_each_data_point.append(score)

    return mean(scores_for_for_each_data_point)


def get_distance_matrix(df):
    distance_matrix = []
    for i1, row1 in df.iterrows():
        distance_matrix.append([])
        for i2, row2 in df.iterrows():
            distance_matrix[i1].append(dist(row1.values.tolist(), row2.values.tolist()))
    return distance_matrix


# data = pd.read_csv('../../resources/multidimensional_dataset/Wine.csv', header=None)
# bandwidth = estimate_bandwidth(data)
# mean_shift = MeanShift(bandwidth=bandwidth)
# mean_shift.fit(data)
# y_m = mean_shift.predict(data)
# print(silhouette_index(data, y_m))
# print(silhouette_score(data, y_m))

