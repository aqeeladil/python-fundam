def change(L):
    L = L + (4, 5)
    print(L)
    print(id(L))
    
    
L1 = (1,2,3)
print(L1)
print(id(L1))

change(L1)
print(L1)
print(id(L1))

