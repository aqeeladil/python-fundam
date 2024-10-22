import sys

L = []

for i in range(30):
    print(i, sys.getsizeof(L))
    L.append(i)

'''
# Python lists are implemented as dynamic arrays, meaning they automatically resize when they run 
out of space.

# When you append an element to a list that doesn't have enough allocated space, Python allocates 
a larger chunk of memory to accommodate more elements. This avoids the need to reallocate 
memory each time an element is added, which would be inefficient.
'''