"""
for single sliding-window:
1. Start at the random point (initialize sliding point)
2. Calculate the mean of points within a sliding window -> center for next sliding window
(3. Need to filter candidate windows to eliminate near-duplicates)
4. Move sliding point to calculated center
5. Repeat 2-4 until there will be no possibility to accommodate more points within sliding window
"""
import pandas as pd
from math import dist

from sklearn.datasets import make_moons
from numpy import mean
from matplotlib import pyplot


def euclidean_distance(p1, p2):
    return dist(p1, p2)


def mean_shift(df, bandwidth=4.0):
    sample_points = starting_points(df, bandwidth)
    full_dataset = df.to_numpy()
    points_in_peak = []
    for point in sample_points:
        at_peak = False
        points_within_kernel = []
        accommodated_points = 0
        toward_peak_point = point
        while not at_peak:
            for tmp_point in full_dataset:
                distance = euclidean_distance(point, tmp_point)
                if distance <= bandwidth:
                    points_within_kernel.append(tmp_point)

            quantity_of_points = len(points_within_kernel)
            if accommodated_points >= quantity_of_points:
                at_peak = True
            accommodated_points = quantity_of_points
            mean_within_kernel = mean(points_within_kernel, axis=0)
            toward_peak_point = mean_within_kernel
            points_within_kernel = []
        points_in_peak.append(toward_peak_point)
    return points_in_peak


def starting_points(dataset, bandwidth):
    # todo we dont need every datapoint to be starting point
    return dataset.to_numpy()

# from sklearn.datasets import make_blobs, make_circles

# X, y = make_circles(n_samples=100)
# data = pd.DataFrame(dict(x=X[:, 0], y=X[:, 1], label=y))
# data.drop(['label'], axis=1, inplace=True)
# data.to_csv('testing.csv')

# data = pd.DataFrame([[0.0, .0],
#                      [2.0, .0],
#                      [2.0, 2.0],
#                      [.0, 2.0]])


data = pd.read_csv('testing.csv')
a = mean_shift(data, bandwidth=3)
b = pd.DataFrame(a)
print(data)

pyplot.plot(data['x'], data['y'], 'o', color='yellow')
pyplot.plot(b[0], b[1], 'o', color='black')
pyplot.show()
