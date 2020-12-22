from sklearn.metrics import jaccard_score


# J(A,B) = |AnB| / |AuB|
def jaccard_index(set_a, set_b):
    if len(set_a) != len(set_b):
        raise Exception('Both sets should have same numbers of samples: '
                        '[' + str(len(set_a)) + ', ' + str(len(set_b)) + ']')

    union = 0
    for i in range(len(set_a)):
        if set_a[i] == set_b[i]:
            union += 1

    return union/len(set_a)


A = [1, 0, 1, 3, 1]
B = [1, 0, 1, 1, 1]
print(jaccard_score(A, B, average='micro'))
print(jaccard_index(A, B))

