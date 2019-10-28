#!/bin/python3


# Complete the activityNotifications function below.
import timeit
from typing import Callable

import numpy


def median_v1(nums):
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


def make_histogram(_nums):
    histogram = {i: 0 for i in range(0, 200)}
    for i in _nums:
        histogram[i] += 1
    return histogram


def median_v2(nums):
    histogram = make_histogram(nums)
    total = 0
    median_index = (sum(histogram.values()) + 1) / 2
    for value in sorted(histogram.keys()):
        total += histogram[value]
        if total > median_index:
            return value


def median_v4(nums):
    return numpy.median(nums)


def median_v5(nums):
    nums = sorted(nums)
    if len(nums) % 2 == 1:
        return nums[int(len(nums) / 2)]
    else:
        return 0.5 * (nums[int(len(nums) / 2 - 1)] + nums[int(len(nums) / 2)])


def activityNotifications(expenditure, d, median_method: Callable):
    notifications_count = 0
    initial_part, other_part = expenditure[:d], expenditure[d:]
    processed_items = len(initial_part)
    total_items = len(expenditure)
    progress = 0
    for i in other_part:
        _med = median_method(initial_part)
        if i >= _med * 2:
            notifications_count += 1
        initial_part.__delitem__(0)
        initial_part.append(i)
        progress_new = int(processed_items / (total_items * 0.01))
        if progress != progress_new:
            print(f'progress: {progress_new}%')
        progress = progress_new
        processed_items += 1
    return notifications_count


def median_v6(histogram):
    total = 0
    median_index = (sum(histogram.values()) + 1) / 2
    for value in sorted(histogram.keys()):
        total += histogram[value]
        if total > median_index:
            return value


def activityNotifications_v2(expenditure, d, median_method: Callable):
    notifications_count = 0
    initial_part, other_part = expenditure[:d], expenditure[d:]
    processed_items = len(initial_part)
    total_items = len(expenditure)
    progress = 0
    histogram = make_histogram(initial_part)
    for i in other_part:
        histogram[i] = histogram[i]+1
        total = 0
        median_index = (sum(histogram.values()) + 1) / 2
        for value in sorted(histogram.keys()):
            total += histogram[value]
            if total > median_index:
                if i > value * 2:
                    notifications_count += 1
                else:
                    break
        histogram[i] = histogram[i]-1
        # initial_part.__delitem__(0)
        # initial_part.append(i)
        progress_new = int(processed_items / (total_items * 0.01)) + 1
        if progress != progress_new:
            print(f'progress: {progress_new}%')
        progress = progress_new
        processed_items += 1
    return notifications_count


if __name__ == '__main__':
    input_data = open('input_data/1.txt', 'r')

    nd = input_data.readline().split()

    n = int(nd[0])

    d = int(nd[1])

    expenditure = list(map(int, input_data.readline().rstrip().split()))
    start = timeit.default_timer()
    method = median_v2
    result = activityNotifications_v2(expenditure, d, median_method=method)
    end = timeit.default_timer()
    total_time = end - start
    print(f'{method.__name__}: notification_count = {result}, time elapsed {int(total_time / 60)}m {int(total_time % 60)}s')
