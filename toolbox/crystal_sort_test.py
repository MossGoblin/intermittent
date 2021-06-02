from copy import deepcopy
import math


def crystal_sort(incoming_bucket):
    bucket = deepcopy(incoming_bucket)
    passes = 0
    swaps = 0
    comparisons = 0

    for offset in range(0, math.floor(len(bucket)/2)):
        subset_start_index = offset
        subset_end_index = len(bucket) - (offset + 1)
        lowest_found = False
        higest_found = False
        for index in range(subset_start_index, subset_end_index):
            passes += 1
            value = bucket[index]
            if not higest_found:
                comparisons += 1
                if value > bucket[subset_end_index]:
                    if offset > 0 and value == current_highest:
                        higest_found = True
                    bucket[index], bucket[subset_end_index] = bucket[subset_end_index], bucket[index]
                    swaps += 1
            value = bucket[index]
            if not lowest_found:
                comparisons += 1
                if value < bucket[subset_start_index]:
                    if offset > 0 and value == current_lowest:
                        lowest_found = True
                    bucket[index], bucket[subset_start_index] = bucket[subset_start_index], bucket[index]
                    swaps += 1
            if higest_found and lowest_found:
                break
        current_lowest = bucket[subset_start_index]
        current_highest = bucket[subset_end_index]
    
    return bucket, passes, comparisons, swaps
