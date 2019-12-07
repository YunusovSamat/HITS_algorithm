#!/usr/bin/python3

import sys

for line in sys.stdin:
    key, values = line.rstrip().split('\t')
    graph, auth_hub = values.split(';')
    # print(f'{key}\t{graph}')
    for edge in graph[1:-1].split(','):
        # print(f'{edge}\t({key})')
        print(f'{edge}\t{auth_hub}')
