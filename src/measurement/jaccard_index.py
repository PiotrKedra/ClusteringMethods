from sklearn.metrics import jaccard_score
import statistics


# J(A,B) = |AnB| / |AuB|
def jaccard_index(set_a, set_b):
    if len(set_a) != len(set_b):
        raise Exception('Both sets should have same numbers of samples: '
                        '[' + str(len(set_a)) + ', ' + str(len(set_b)) + ']')

    # union = 0
    # for i in range(len(set_a)):
    #     if set_a[i] == set_b[i]:
    #         union += 1

    clusters_a = [{
        'number': set_a[0],
        'indexes': [0]
    }]
    for i in range(1, len(set_a)):
        cluster_exist = False
        for cluster in clusters_a:
            if cluster['number'] == set_a[i]:
                cluster['indexes'].append(i)
                cluster_exist = True
                break
        if cluster_exist is False:
            clusters_a.append({
                'number': set_a[i],
                'indexes': [i]
            })

    clusters_b = [{
        'number': set_b[0],
        'indexes': [0]
    }]
    for i in range(1, len(set_b)):
        cluster_exist = False
        for cluster in clusters_b:
            if cluster['number'] == set_b[i]:
                cluster['indexes'].append(i)
                cluster_exist = True
                break
        if cluster_exist is False:
            clusters_b.append({
                'number': set_b[i],
                'indexes': [i]
            })

    result = []
    for cluster_a in clusters_a:
        best = 0
        for cluster_b in clusters_b:
            intersection = len(set(cluster_a['indexes']).intersection(set(cluster_b['indexes'])))
            union = len(set(cluster_a['indexes'] + cluster_b['indexes']))
            score = intersection/union
            if score > best:
                best = score
        result.append(best)
    return statistics.mean(result)


# A = [1, 0, 1, 5, 1]
# B = [1, 0, 1, 2, 2]
# print(jaccard_score(A, B, average='weighted'))
# print(jaccard_index(A, B))

