from copy import deepcopy
import math


def crystal_sort(incoming_bucket):
    bucket = deepcopy(incoming_bucket)
    passes = 0
    swaps = 0
    comparisons = 0

    for offset in range(0, math.floor(len(bucket)/2)):
        subset_start_index = offset
        subset_end_index = - (offset + 1)
        for index in range(subset_start_index, len(bucket) + subset_end_index):
            passes += 1
            value = bucket[index]
            comparisons += 1
            if value > bucket[subset_end_index]:
                bucket[index], bucket[subset_end_index] = bucket[subset_end_index], bucket[index]
                continue
            else:
                swaps += 1
                if value < bucket[subset_start_index]:
                    comparisons += 1
                    bucket[index], bucket[subset_start_index] = bucket[subset_start_index], bucket[index]
                    swaps += 1
                    continue
    
    return bucket, passes, comparisons, swaps
