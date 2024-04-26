# 3D list

lst = []

for a in range(5):
    l1 = []
    for b in range(5):
        l2 = []
        for num in range(5):
            l2.append(num)

        l1.append(l2)

    lst.append(l1)

print(lst)



# Using list comprehension 
lst2 = [[[num for num in range(5)] for _ in range(5)] for _ in range(5)]

print(lst2)