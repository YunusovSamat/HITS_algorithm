#!/usr/bin/python3
"""
A = [
    [0, 1, 1, 1],
    [0, 0, 1, 1],
    [1, 0, 0, 1],
    [0, 0, 0, 1]
]
At = [
     [0, 0, 1, 0],
     [1, 0, 0, 0],
     [1, 1, 0, 0],
     [1, 1, 1, 1]
]
"""

import sys
from functools import reduce

for line in sys.stdin:
    key, values = line.rstrip().split('\t')
    ah, uv = values.split(';')
    ah_list = [int(elem) for elem in ah[1:-1].split(',')]
    uv_list = [int(elem) for elem in uv[1:-1].split(',')]
    t = reduce(lambda x, y: x + uv_list[y-1], ah_list, 0)
    for elem in ah_list:
        if t:
            print(f'{elem}\t({key});({t})')
            t = None
        else:
            print(f'{elem}\t({key})')
