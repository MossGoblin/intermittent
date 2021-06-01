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
        passes += 1
        for index in range(offset, len(bucket) - offset - 1):
            value = bucket[index]
            comparisons += 1
            if value > bucket[-(offset + 1)]:
                swap(bucket, index, len(bucket) - (offset + 1))
                continue
            else:
                swaps += 1
                if value < bucket[offset]:
                    comparisons += 1
                    swap(bucket, index, offset)
                    swaps += 1
                    continue
    
    return bucket, passes, comparisons, swaps
