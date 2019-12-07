#!/usr/bin/python3

import sys

for line in sys.stdin:
    key, values = line.rstrip().split('\t')
    graph, auth_hub = values.split(';')
    for edge in graph[1:-1].split(','):
        # Для каждого ребра выводить ребро и вершину,
        # чтобы получить транспонированный граф.
        print(f'{edge}\t({key})')
        # Для каждого ребра выводить ребро и его
        # оценку авторитетности или посредническую оценку.
        print(f'{edge}\t{auth_hub}')
