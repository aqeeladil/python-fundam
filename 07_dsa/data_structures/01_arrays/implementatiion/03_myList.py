#ctypes is a foreign function library for python. It provides 'C' compatible data types used 
# to create C type array

import ctypes


class MyList():

    def __init__(self):
        # total capactity to store
        self.size = 1         
        # total no. of items
        self.n = 0            
        # creates a C type array with size -> self.size
        self.A = self.__myArray(self.size)

    # private methods

    def __myArray(self, capacity):
        # creates referential array (C type)
        return (capacity*ctypes.py_object)()
    
    def __resize(self, new_capacity):
        # create a new array with new capacity
        B = self.__myArray(new_capacity)
        self.size = new_capacity
        # copy the content of old array to new one
        for i in range(self.n):
            B[i] = self.A[i]
            # reassign A
        self.A = B


    # magic methods

    def __len__(self):
        return self.n
    
    def __str__(self):
        result = ''
        for i in range(self.n):
            result = result + str(self.A[i]) + ','
        return '[' + result[:-1] + ']'

    def __getitem__(self, index):
        if 0 <= index < self.n:
            return self.A[index]
        else:
            return 'IndexError'

    def __delitem__(self, pos):
        if 0 <= pos < self.n:
            for i in range(pos, self.n-1):
                self.A[i] = self.A[i+1]

            self.n = self.n - 1

    # public methods

    def append(self, item):
        # check if vacant
        if self.n == self.size:
            # array is full -> resize
            self.__resize(self.size * 2)
        self.A[self.n] = item
        self.n = self.n + 1

    def pop(self):
        if self.n == 0:
            return 'Empty List'
        print(self.A[self.n - 1])
        self.n = self.n - 1
    
    def clear(self):
        self.n = 0
        self.size = 1
    
    def find(self, item):
        for i in range(self.n):
            if self.A[i] == item:
                return i
        return 'ValueError - not in list'
    
    def insert(self, pos, item):
        if self.n == self.size:
            self.__resize(self.size * 2)
        
        for i in range(self.n, pos, -1):
            self.A[i] = self.A[i-1]
        
        self.A[pos] = item
        self.n = self.n + 1

    def remove(self, item):
        pos = self.find(item)
        if type(pos) == int:
            self.__delitem__(pos)
        else:
            return pos
        




L = MyList()

print(L)
print(len(L))

L.append(7)
L.append('Hello')
L.append(3.6)
L.append(True)
print(len(L))

print(L)

print(L[0])
print(L[3])
print(L[4])

L.pop()
print(L)
print(len(L))

L.clear()
print(L)
print(len(L))

L.append('aqeel')
L.append(2024)
print(L.find(2024))


L.insert(0, 'house')
print(L)

L.__delitem__(1)
print(L)

print(L.remove(100))
L.remove('house')
print(L)