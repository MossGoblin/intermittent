from copy import deepcopy
import math


def sort(incoming_bucket):

    bucket = deepcopy(incoming_bucket)
    for offset in range(0, math.floor(len(bucket)/2)):
        subset_start_index = offset
        subset_end_index = - (offset + 1)
        for index in range(subset_start_index, len(bucket) + subset_end_index):
            value = bucket[index]
            if value > bucket[subset_end_index]:
                bucket[index], bucket[subset_end_index] = bucket[subset_end_index], bucket[index]
                continue
            else:
                if value < bucket[subset_start_index]:
                    bucket[index], bucket[subset_start_index] = bucket[subset_start_index], bucket[index]
                    continue

    return bucket