#!/usr/bin/env python
import math

def sort(array, base=10):
    max_digits = int(math.ceil(math.log(max(array) + 1, base))) # O(N)

    for iter_round in range(0, max_digits):
        buckets = [[] for i in range(0, base)]
        for number in array:
            buckets[number % (base ** (iter_round + 1)) // (base ** iter_round)].append(number)

        array = []
        for bucket in buckets:
            array.extend(bucket)

    return array
