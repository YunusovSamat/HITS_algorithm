#!/usr/bin/python3

import sys

last_key, auth = None, 0
for line in sys.stdin:
    key, values = line.rstrip().split('\t')

    if last_key and last_key != key:
        print(f'{last_key}\t{graph};{auth}')
        if '(' in values:
            graph = values
        else:
            auth = int(values)
    else:
        if '(' in values:
            graph = values
        else:
            auth += int(values)
    last_key = key

if last_key:
    print(f'{last_key}\t{graph};{auth}')
