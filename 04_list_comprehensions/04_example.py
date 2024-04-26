# Example-4: Flattening a matrix

matrix = [[1,2,3], [4,5,6], [7,8,9]]
flattened = []
for i in matrix:
    for j in i:
        flattened.append(j)

print(flattened)


# Using list comprehension 

flat2 = [j for i in matrix for j in i]

print(flat2)