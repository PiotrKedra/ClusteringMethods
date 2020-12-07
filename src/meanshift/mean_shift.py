"""
1. Start at the random point (initialize sliding points)
2. Calculate the mean of points within a sliding window -> center for next sliding window
3. Repeat 2 for each sliding point until there will be no possibility to accommodate more points within sliding window.
   It will result in all peaks.
4. Remove near duplicates among all peaks
5. Assign proper cluster number for each datapoint
"""
import pandas as pd
from math import dist

from numpy import mean
from matplotlib import pyplot


def mean_shift(df, bandwidth=4.0):
    all_peaks = find_all_peaks(df, bandwidth)
    highest_peaks = remove_near_duplicates(all_peaks, bandwidth)
    return assign_points_to_proper_cluster(df, highest_peaks)


def find_all_peaks(df, bandwidth):
    sliding_points = get_starting_points(df, bandwidth)
    full_dataset = df.to_numpy()
    points_in_peak = []
    for point in sliding_points:
        at_peak = False
        accommodated_points = 0
        toward_peak_point = point
        while not at_peak:
            points_within_kernel = find_points_within_kernel(point, full_dataset, bandwidth)
            quantity_of_points = len(points_within_kernel)
            if accommodated_points >= quantity_of_points:
                at_peak = True
            accommodated_points = quantity_of_points
            mean_within_kernel = mean(points_within_kernel, axis=0)
            toward_peak_point = find_nearest_point(mean_within_kernel, full_dataset)
        points_in_peak.append(toward_peak_point)
    return points_in_peak


def get_starting_points(dataset, bandwidth):
    # todo we dont need every datapoint to be sliding point
    return dataset.to_numpy()


def find_points_within_kernel(point, full_dataset, bandwidth):
    points_within_kernel = []
    for tmp_point in full_dataset:
        distance = dist(point, tmp_point)
        if distance <= bandwidth:
            points_within_kernel.append(tmp_point)
    return points_within_kernel


def find_nearest_point(point, dataset):
    distance = dist(point, dataset[0])
    closest_point = dataset[0]
    for datapoint in dataset:
        tmp_distance = dist(point, datapoint)
        if tmp_distance < distance:
            distance = tmp_distance
            closest_point = datapoint
    return closest_point


def remove_near_duplicates(peaks, bandwidth):
    segregated = segregate_peaks(peaks)
    highest_peak = segregated.pop(0)
    cluster_number = 0
    highest_peak.append(cluster_number)
    highest_peaks = [highest_peak]
    current_peak = highest_peak
    index = 0
    # iterate thorough segregated peaks and pop ones that are relevant
    while len(segregated) != 0:
        distance = dist(current_peak[0], segregated[index][0])
        if distance <= bandwidth:
            segregated.pop(index)
            if index == len(segregated):
                index = 0
            continue
        if index + 1 >= len(segregated):
            index = 0
            cluster_number += 1
            current_peak = segregated.pop(0)
            current_peak.append(cluster_number)
            highest_peaks.append(current_peak)
        else:
            index += 1
    return remove_noise(highest_peaks)


def segregate_peaks(peaks):
    peaks_by_counted = []
    for peak in peaks:
        duplicate = False
        for peak_count in peaks_by_counted:
            if (peak == peak_count[0]).all():
                peak_count[1] += 1
                duplicate = True
        if duplicate is False:
            peaks_by_counted.append([peak, 1])
    return sorted(peaks_by_counted, key=lambda x: x[1], reverse=True)


def remove_noise(highest_peaks):
    result = []
    for i in range(0, len(highest_peaks)):
        # remove every peak that hase only 1 occurrences
        if highest_peaks[i][1] > 1:
            result.append([highest_peaks[i][0], highest_peaks[i][2]])
    return result


def assign_points_to_proper_cluster(dataset, peaks):
    result = []
    for (idx, datapoint) in dataset.iterrows():
        closest_distance = dist(datapoint, peaks[0][0])
        cluster_number = peaks[0][1]
        # finding nearest peak for given datapoint and assigning it its cluster number
        for peak in peaks:
            tmp_distance = dist(datapoint, peak[0])
            if tmp_distance < closest_distance:
                closest_distance = tmp_distance
                cluster_number = peak[1]
        result.append(cluster_number)
    return result


data = pd.read_csv('../../resources/2d_dataset/r15.csv')
data.drop(['label'], axis=1, inplace=True)
labels = mean_shift(data, bandwidth=1)

pyplot.scatter(data[['x']], data[['y']], c=labels)
pyplot.show()
