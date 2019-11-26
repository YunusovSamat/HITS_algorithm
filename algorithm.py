import numpy

page_n = 4
auth = [[1] * page_n]
hub = [[1] * page_n]

A = numpy.array([
    [0, 1, 1, 0],
    [0, 0, 0, 1],
    [0, 0, 0, 1],
    [0, 0, 0, 0]
], dtype='byte')
At = A.transpose()

for i in range(10):
    auth.append(At.dot(hub[-1]))
    hub.append(A.dot(auth[-1]))
    print('{:>6}|{:>6}|{:>6}'.format(*auth[-1]))

# for i in range(9):
#     if not any(auth[i] % auth[i+1]):
#         print('{:>6}|{:>6}|{:>6}'.format(*(auth[i] / auth[i+1])))


# while True:
#     auth.append(At.dot(hub[-1]))
#     hub.append(A.dot(auth[-1]))
#
#     if not any(auth[-1] % auth[-2]):
#         print(auth[-2])
#         break
