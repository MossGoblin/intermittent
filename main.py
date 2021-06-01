from copy import deepcopy
import json
import numpy
from datetime import datetime
from typing import List

from sort import *


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


def record_run(log, set_range, passes, swaps):
    if set_range not in log:
        log[set_range] = {}

    if 'passes' in log[set_range]:
        log[set_range]['passes'] = (log[set_range]['passes'] + passes)/2
    else:
        log[set_range]['passes'] = passes

    if 'swaps' in log[set_range]:
        log[set_range]['swaps'] = (log[set_range]['swaps'] + swaps)/2
    else:
        log[set_range]['swaps'] = swaps
    return log


input = []

repetition = 100

for magnitude in range(1, 4):
    for rep in range(repetition):
        input.append(get_rand_set(0, 10*magnitude, 10**magnitude))

# input.append([1, 8, 7, 6, 8, 6, 6, 3, 6, 9])

log = {}
fails = {}


print("-- -- --")
for index, set in enumerate(input):
    set_range = len(set)
    print(set_range)
    start_bucket = set
    start = datetime.utcnow()
    bucket, passes, swaps = shrink_sort(start_bucket)
    end = datetime.utcnow()
    confirmed = confirm_sort(bucket)
    print(f"confirmed: {confirmed}")
    log = record_run(log, set_range, passes, swaps)
    print(f"passes: {passes}")
    print(f"swaps: {swaps}")
    if not confirmed:
        print(start_bucket)
        print(bucket)
        sorted_bucket = deepcopy(bucket)
        sorted_bucket.sort()
        print(sorted_bucket)
        fails[index] = {}
        fails[index]['range'] = set_range
        fails[index]['passes'] = passes
        fails[index]['swaps'] = swaps
        fails[index]['set'] = start_bucket
        fails[index]['processed'] = bucket
        fails[index]['sorted'] = sorted_bucket
        print(fails)
    print(end - start)
    print("-- -- --")

with open('log.log', 'w') as logfile:
    content = json.dumps(log)
    logfile.write(content)
pass
