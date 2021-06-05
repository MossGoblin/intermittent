from copy import deepcopy
import math


def sort_00(incoming_bucket):
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
                swaps += 1
                continue
            else:
                comparisons += 1
                if value < bucket[subset_start_index]:
                    comparisons += 1
                    bucket[index], bucket[subset_start_index] = bucket[subset_start_index], bucket[index]
                    swaps += 1
                    continue

    return bucket, passes, comparisons, swaps


def sort_01(incoming_bucket):
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
            seed = bucket[index]
            if not higest_found:
                comparisons += 1
                if seed > bucket[subset_end_index]:
                    if offset > 0 and seed == current_highest:
                        higest_found = True
                    bucket[index], bucket[subset_end_index] = bucket[subset_end_index], bucket[index]
                    swaps += 1
            seed = bucket[index]
            if not lowest_found:
                comparisons += 1
                if seed < bucket[subset_start_index]:
                    if offset > 0 and seed == current_lowest:
                        lowest_found = True
                    bucket[index], bucket[subset_start_index] = bucket[subset_start_index], bucket[index]
                    swaps += 1
            if higest_found and lowest_found:
                break
        current_lowest = bucket[subset_start_index]
        current_highest = bucket[subset_end_index]

    return bucket, passes, comparisons, swaps

# HERE


def sort_02(incoming_bucket):
    bucket = deepcopy(incoming_bucket)
    passes = 0
    swaps = 0
    comparisons = 0

    offset_start = 0
    offset_end = 0

    while len(bucket) - (offset_start + offset_end) > 1:
        match_highest_count = 0
        match_lowest_count = 0
        has_inner_highest = False
        has_inner_lowest = False

        subset_start_index = offset_start
        subset_end_index = len(bucket) - (offset_end + 1)

        iteration_start = subset_start_index
        iteration_end = subset_end_index
        index = iteration_start

        # DBG TRYING HERE OR BELOW
        current_lowest = bucket[subset_start_index]
        has_inner_lowest = True
        current_highest = bucket[subset_end_index]
        has_inner_highest = True

        while index < iteration_end:
            passes += 1
            seed = bucket[index]
            comparisons += 1
            if seed > bucket[subset_end_index]:
                bucket[index], bucket[subset_end_index] = bucket[subset_end_index], bucket[index]
                current_highest = seed
                has_inner_highest = False
                index += 1
                swaps += 1
                continue

            elif seed < bucket[subset_start_index]:
                comparisons += 1
                bucket[index], bucket[subset_start_index] = bucket[subset_start_index], bucket[index]
                current_lowest = seed
                has_inner_lowest = False
                index += 1
                swaps += 1
                continue

            elif has_inner_highest and seed == current_highest:
                comparisons += 1
                match_swap_position = subset_end_index - 1 - match_highest_count
                if index > iteration_start and index != match_swap_position:
                    bucket[index], bucket[match_swap_position] = bucket[match_swap_position], bucket[index]
                    match_highest_count += 1
                    index -= 1
                    swaps += 1

            elif has_inner_lowest and seed == current_lowest:
                comparisons += 1
                match_swap_position = subset_start_index + 1 + match_lowest_count
                if index > iteration_start and index != match_swap_position:
                    bucket[index], bucket[match_swap_position] = bucket[match_swap_position], bucket[index]
                    match_lowest_count += 1
                    swaps += 1

            index += 1

        offset_start += 1
        offset_end += 1

    return bucket, passes, comparisons, swaps

def sort_03(incoming_bucket):
    bucket = deepcopy(incoming_bucket)
    passes = 0
    swaps = 0
    comparisons = 0

    offset_start    = 0
    offset_end      = 0


    subset_start_index = 0
    subset_end_index = 0

    index = 0
    while len(bucket) > (offset_start + offset_end):

        passes += 1

        subset_start_index  = offset_start
        subset_end_index    = len(bucket) - 1 - offset_end

        # Primary pass - find the lowest and highest for the subset 
        # and position them
        for index in range(subset_start_index, subset_end_index + 1):
            seed = bucket[index]

            if seed > bucket[subset_end_index]:
                bucket[index], bucket[subset_end_index] = bucket[subset_end_index], bucket[index]
                swaps += 1
                continue
            else:
                if seed < bucket[subset_start_index]:
                    comparisons += 1
                    bucket[index], bucket[subset_start_index] = bucket[subset_start_index], bucket[index]
                    swaps += 1
                    continue
        
        # Secondary pass - with the brachets of the current subset,
        # find all matches to the lower and higher bracket and move them
        # to the edges
        search_offset_start = 0
        search_offset_end = 0
        lowest = bucket[subset_start_index]
        highest = bucket[subset_end_index]
        search_start_index = subset_start_index + 1
        search_end_index = subset_end_index
        index = search_start_index

        while index < (subset_end_index - search_offset_end) and (subset_start_index + search_offset_start + search_offset_end < subset_end_index):

            passes += 1

            seed = bucket[index]

            comparisons += 1
            if seed == lowest:
                if index == search_start_index:
                    search_offset_start += 1
                    index += 1
                    continue
                search_offset_start += 1
                swap_position = subset_start_index + search_offset_start
                bucket[index], bucket[swap_position] = bucket[swap_position], bucket[index]
                index += 1
                swaps += 1
            elif seed == highest:
                comparisons += 1
                if index == search_end_index:
                    search_offset_end += 1
                    index += 1
                    continue
                search_offset_end += 1
                swap_position = subset_end_index - search_offset_end
                bucket[index], bucket[swap_position] = bucket[swap_position], bucket[index]
                swaps += 1
            else:
                index += 1
            
        offset_start = offset_start + search_offset_start + 1
        offset_end   = offset_end + search_offset_end + 1

    return bucket, passes, comparisons, swaps