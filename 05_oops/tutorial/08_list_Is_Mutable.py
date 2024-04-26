
# def change(L):
#     L.append(4)
#     print(id(L))
     
# L1 = [1,2,3]
# print(L1)
# print(id(L1))

# change(L1)
# print(L1)
# print(id(L1))


####################### better way to write above code ##############################################

def change(L):
    L.append(4)
    print(id(L))
    
    
L1 = [1,2,3]
print(L1)
print(id(L1))

change(L1[:])            ##############
print(L1)
print(id(L1))