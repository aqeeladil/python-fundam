# Implement the transpose of a matrix.
# The transpose of a matrix is obtained by swapping rows with columns.


def transpose(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    transposed = [[0] * rows for _ in range(cols)]
    
    for i in range(rows):
        for j in range(cols):
            transposed[j][i] = matrix[i][j]
    
    return transposed

# Example usage
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
transposed_matrix = transpose(matrix)
for row in transposed_matrix:
    print(row)
