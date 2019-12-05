#!/usr/bin/python3

import sys

for line in sys.stdin:
    key, values = line.rstrip().split('\t')
    graph, hub = values.split(';')
    print(f'{key}\t{graph}')
    for edge in graph[1:-1].split(','):
        print(f'{edge}\t{hub}')
