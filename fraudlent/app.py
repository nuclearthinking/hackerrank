#!/bin/python3


# Complete the activityNotifications function below.
import timeit
from collections import defaultdict

import numpy


def median(nums):
    length = len(nums)
    sorted_nums = sorted(nums)
    if length % 2 == 0:
        while length > 2:
            sorted_nums.__delitem__(0)
            sorted_nums.__delitem__(-1)
            length = len(sorted_nums)
        return sum(sorted_nums) / len(sorted_nums)
    index = int((length - 1) / 2)
    return sorted_nums[index]


def make_histogram(nums):
    histogram_result = defaultdict(int)
    for i in nums:
        histogram_result[i] += 1
    return histogram_result


def make_histogram_v2(nums):
    return {i: nums.count(i) for i in range(0, 201)}


def median_v2(nums):
    histogram = make_histogram(nums)
    total = 0
    median_index = (sum(histogram.values()) + 1) / 2
    for value in sorted(histogram.keys()):
        total += histogram[value]
        if total > median_index:
            return value


def median_v3(nums):
    histogram = make_histogram_v2(nums)
    total = 0
    median_index = (sum(histogram.values()) + 1) / 2
    for value in sorted(histogram.keys()):
        total += histogram[value]
        if total > median_index:
            return value


def median_v4(nums):
    return numpy.median(nums)


def activityNotifications(expenditure, d):
    notifications_count = 0
    initial_part, other_part = expenditure[:d], expenditure[d:]
    other_part = iter(other_part)
    processed_items = len(initial_part)
    total_items = len(expenditure)
    while other_part:
        _med = median_v3(initial_part)
        print(
            f'median is {_med}, current notifications {notifications_count} processed items {processed_items}/{total_items}')
        next_item = next(other_part, None)
        processed_items += 1
        if next_item is not None:
            if next_item >= _med * 2:
                notifications_count += 1
            initial_part.__delitem__(0)
            initial_part.append(next_item)
        else:
            break

    return notifications_count


if __name__ == '__main__':
    input_data = open('1.txt', 'r')

    nd = input_data.readline().split()

    n = int(nd[0])

    d = int(nd[1])

    expenditure = list(map(int, input_data.readline().rstrip().split()))
    start = timeit.default_timer()
    result = activityNotifications(expenditure, d)
    end = timeit.default_timer()

    print(f'Result is {result}')
    print(f'Time spend is {int(end - start) / 60} minutes or {int(end - start)} seconds')
