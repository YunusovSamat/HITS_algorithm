#!/usr/bin/python3

import sys

last_key = None
ah_list, uv_dict = list(), dict()
outputs_list = list()

for line in sys.stdin:
    key, values = line.rstrip().split('\t')
    ah, uv = values.split(';')

    if last_key and last_key != key:
        outputs_list.append(f'{last_key}\t({",".join(ah_list)})')
        last_key = key
        ah_list.clear()
    else:
        last_key = key

    if ah[1: -1]:
        ah_list.extend(ah[1: -1].split(','))  # may be more or one
        if uv[1: -1]:
            uv_dict[ah[1: -1]] = uv[1: -1]

if last_key:
    outputs_list.append(f'{last_key}\t({",".join(ah_list)})')

    uv_all = ",".join([uv_dict[k] for k in sorted(uv_dict)])
    for output in outputs_list:
        print(f'{output};({uv_all})')

