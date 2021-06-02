from copy import deepcopy
import json
import numpy
from datetime import datetime
from typing import List, Dict

from crystal_sort import *
from sort import *

algo_list = [
    'crystal',
    'insertion',
]


def get_rand_set(min: int, max: int, size: int):
    set = numpy.random.randint(min, max, size=size)
    set = set.tolist()
    return set


def confirm_sort(bucket: List) -> bool:
    sorted_bucket = deepcopy(bucket)
    sorted_bucket.sort()
    if bucket == sorted_bucket:
        return True
    else:
        return False


def add_average_to_log(log: Dict):
    for set_size, set_info in log.items():
        set_info['average comparisons'] = set_info['comparisons'] / \
            int(set_size)
        set_info['average swaps'] = set_info['swaps'] / int(set_size)
    return log


def record_run(log, set_length, passes, comparisons, swaps):
    if set_length not in log:
        log[set_length] = {}

    if 'passes' in log[set_length]:
        log[set_length]['passes'] = log[set_length]['passes'] + passes
    else:
        log[set_length]['passes'] = passes

    if 'comparisons' in log[set_length]:
        log[set_length]['comparisons'] = log[set_length]['comparisons'] + comparisons
    else:
        log[set_length]['comparisons'] = comparisons

    if 'swaps' in log[set_length]:
        log[set_length]['swaps'] = log[set_length]['swaps'] + swaps
    else:
        log[set_length]['swaps'] = swaps

    return log


def process(algos: List, repetition: int, min: int, max: int):
    start = datetime.utcnow()

    input = []

    for power in range(min, max+1):
        for rep in range(repetition):
            input.append(get_rand_set(0, 10*power, 10**power))

    # input.append([2.3, -3.5, 77.14, 77.1, -1, 0])

    log = {}
    fails = {}

    for algo in algos:
        if algo not in algo_list:
            print(f'No {algo} algorithm')
            continue
        print("-- -- --")
        print(algo)
        for index, set in enumerate(input):
            set_length = len(set)
            print(f"run: {index}/{len(input)}")
            print(f"set length: {set_length}")
            print(f"min magnitude: {min}")
            print(f"max magnitude: {max}")
            # print(set) # DBG VISIBILITY ONLY
            start_bucket = deepcopy(set)
            sort_start = datetime.utcnow()
            if algo == 'crystal':
                bucket, passes, comparisons, swaps = crystal_sort(start_bucket)
            elif algo == 'insertion':
                bucket, passes, comparisons, swaps = insertion_sort(
                    start_bucket)

            sort_end = datetime.utcnow()
            # print(bucket) # DBG VISIBILITY ONLY

            # DBG TEST FAIL
            # Uncomment the next row to replace the sorted buket with the unsorted one
            # .. in order to test reposrting of failed sorts
            # bucket = deepcopy(set)

            confirmed = confirm_sort(bucket)
            print(f"confirmed: {confirmed}")
            print(f"passes: {passes}")
            print(f"comparisons: {comparisons}")
            print(f"swaps: {swaps}")
            if not confirmed:
                print(set)
                print(bucket)
                sorted_bucket = deepcopy(bucket)
                sorted_bucket.sort()
                print(sorted_bucket)
                fails[index] = {}
                fails[index]['range'] = set_length
                fails[index]['passes'] = passes
                fails[index]['swaps'] = swaps
                fails[index]['set'] = set
                fails[index]['processed'] = bucket
                fails[index]['sorted'] = sorted_bucket
                print(fails)
            print(f"sort time: {sort_end - sort_start}")
            print("-- -- --")
            log = record_run(log, set_length, passes, comparisons, swaps)

        if len(fails) > 0:
            with open('fails.log', 'w') as logfile:
                content = json.dumps(fails)
                logfile.write(content)

        end = datetime.utcnow()
        print(f"Total time: {end - start}")

        log = add_average_to_log(log)

        with open('log.log', 'w') as logfile:
            content = json.dumps(log)
            logfile.write(content)


if __name__ == '__main__':
    process(['crystal'], 50, 1, 4)
