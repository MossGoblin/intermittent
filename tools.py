import json
import numpy
from datetime import datetime

from sort import *



def get_rand_set(min: int, max: int, size: int):
    result = numpy.random.randint(min, max, size=size)
    return result


input = []
# input.append([3, 5, 1, 6, 8, 4, 9, 7, 2])
# input.append([3, 5, 1, 6, 8, 4, 9, 7, 2, 7, 5, 3, 1, 4, 6, 8, 9, 2])
# input.append(get_rand_set(0, 1000, 10000))
# input.append([1, 2, 3, 4, 5, 6, 7, 8, 9])
# input.append([9, 8, 7, 6, 5, 4, 3, 2, 1])
# input.append([3, 1, 2, 4, 6, 5, 7, 9, 8])

repetition = 10

for magnitude in range(1, 5):
    for rep in range(repetition):
        input.append(get_rand_set(0, 10*magnitude, 10**magnitude))

log = {}

print("-- -- --")
for index, set in enumerate(input):
    range = len(set)
    print(range)
    bucket = set
    start = datetime.utcnow()
    bucket, passes, swaps = shrink_sort(bucket)
    end = datetime.utcnow()
    log[index] = {}
    log[index]['range'] = range
    log[index]['passes'] = passes
    log[index]['swaps'] = swaps
    # log[index]['bucket'] = bucket
    print(f"passes: {passes}")
    print(f"swaps: {swaps}")
    print(bucket)
    print(end - start)
    print("-- -- --")

with open('log.log', 'w') as logfile:
    content = json.dumps(log)
    logfile.write(content)
pass

