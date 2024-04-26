import sys

L = []

for i in range(30):
    print(i, sys.getsizeof(L))
    L.append(i)

