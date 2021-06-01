import math

def swap(bucket, index_one, index_two):
    temp = bucket[index_one]
    bucket[index_one] = bucket[index_two]
    bucket[index_two] = temp

def shrink_sort(bucket):
    print(bucket)

    done = False
    passes = 0
    swaps = 0

    for offset in range(0, math.floor(len(bucket)/2)):
        done = True
        passes += 1
        for index in range(offset, len(bucket) - offset - 1):
            value = bucket[index]
            if value > bucket[-(offset + 1)]:
                swap(bucket, index, len(bucket) - (offset + 1))
                done = False
                swaps += 1
                continue
            elif value < bucket[offset]:
                swap(bucket, index, offset)
                done = False
                swaps += 1
                continue
        # print(bucket)
        if done:
            break
    
    return bucket, passes, swaps
