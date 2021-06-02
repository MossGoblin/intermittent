from copy import deepcopy
import math

def swap(bucket, index_one, index_two):
    temp = bucket[index_one]
    bucket[index_one] = bucket[index_two]
    bucket[index_two] = temp

def crystal_sort(incoming_bucket):
    bucket = deepcopy(incoming_bucket)
    passes = 0
    swaps = 0
    comparisons = 0

    for offset in range(0, math.floor(len(bucket)/2)):
        subset_start_index = offset
        subset_end_index = - (offset + 1)
        passes += 1
        for index in range(subset_start_index, len(bucket) + subset_end_index):
            value = bucket[index]
            comparisons += 1
            if value > bucket[subset_end_index]:
                swap(bucket, index, subset_end_index)
                continue
            else:
                swaps += 1
                if value < bucket[subset_start_index]:
                    comparisons += 1
                    swap(bucket, index, subset_start_index)
                    swaps += 1
                    continue
    
    return bucket, passes, comparisons, swaps
