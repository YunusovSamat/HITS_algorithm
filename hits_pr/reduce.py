#!/usr/bin/python3

import sys

last_key, graph, auth_hub_sum = None, list(), 0
for line in sys.stdin:
    key, values = line.rstrip().split('\t')

    if last_key and last_key != key:
        print(f'{last_key}\t({",".join(graph)});{auth_hub_sum}')
        # Если значение является графом.
        if '(' in values:
            graph = [values[1:-1]]
            auth_hub_sum = 0
        # Если значение является оценкой.
        else:
            graph = list()
            auth_hub_sum = int(values)
    else:
        # Если значение является графом.
        if '(' in values:
            graph.append(values[1:-1])
        # Если значение является оценкой.
        else:
            auth_hub_sum += int(values)
    last_key = key

if last_key:
    print(f'{last_key}\t({",".join(graph)});{auth_hub_sum}')
