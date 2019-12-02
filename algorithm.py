import math
from functools import reduce

import numpy


def check_auth(v):
    sum_sqr = reduce(lambda x, y: x + y**2, v, 0)
    return reduce(lambda x, y: x + (y/math.sqrt(sum_sqr))**2, v, 0)


page_n = 4
auth = list()
hub = [[1] * page_n]

A = numpy.array([
    [0, 1, 1, 1],
    [0, 0, 1, 1],
    [1, 0, 0, 1],
    [0, 0, 0, 1]
], dtype='byte')
At = A.transpose()

for i in range(3):
    auth.append(At.dot(hub[-1]))
    hub.append(A.dot(auth[-1]))
    print('{:>6}|{:>6}|{:>6}{:>6}'.format(*auth[-1]))
    print('{:>6}|{:>6}|{:>6}{:>6}'.format(*hub[-1]))
